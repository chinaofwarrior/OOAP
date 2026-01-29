import os
import re
from urllib.parse import urljoin, urlparse, urlunparse

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify


BASE_URL = "https://docs.fint.io"
OUTPUT_DIR = "."
SESSION = requests.Session()
SESSION.headers.update(
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    }
)


def normalize_url(url: str) -> str:
    parsed = urlparse(url)
    scheme = parsed.scheme or "https"
    netloc = parsed.netloc or urlparse(BASE_URL).netloc
    path = parsed.path or "/"
    path = path.rstrip("/") or "/"
    return urlunparse((scheme, netloc, path, "", "", ""))


def is_same_site(url: str) -> bool:
    base_netloc = urlparse(BASE_URL).netloc
    return urlparse(url).netloc == base_netloc


def is_asset(url: str) -> bool:
    path = urlparse(url).path.lower()
    for ext in (
        ".css",
        ".js",
        ".png",
        ".jpg",
        ".jpeg",
        ".gif",
        ".svg",
        ".ico",
        ".pdf",
        ".zip",
        ".tar",
        ".gz",
        ".tgz",
        ".mp4",
        ".webm",
        ".woff",
        ".woff2",
        ".ttf",
    ):
        if path.endswith(ext):
            return True
    return False


def url_to_rel_path(url: str) -> str:
    parsed = urlparse(url)
    path = parsed.path or "/"
    if path == "/" or path == "":
        return "README.md"
    if path.startswith("/"):
        path = path[1:]
    if path.endswith("/"):
        path = path[:-1]
    if not path:
        return "README.md"
    segments = path.split("/")
    filename = segments[-1] + ".md"
    if len(segments) == 1:
        return filename
    return os.path.join(*segments[:-1], filename)


def extract_title(soup: BeautifulSoup, fallback: str) -> str:
    h1 = soup.find("h1")
    if h1 and h1.get_text(strip=True):
        return h1.get_text(strip=True)
    title_tag = soup.find("title")
    if title_tag and title_tag.get_text(strip=True):
        return title_tag.get_text(strip=True)
    return fallback


def extract_main_html(soup: BeautifulSoup) -> str:
    working = BeautifulSoup(str(soup), "html.parser")
    for tag in working.find_all(["script", "style", "svg", "noscript", "iframe"]):
        tag.decompose()
    for tag in working.find_all(
        ["nav", "header", "footer", "aside", "form", "button", "input", "select", "textarea"]
    ):
        tag.decompose()
    keywords = {
        "nav",
        "sidebar",
        "toc",
        "breadcrumb",
        "search",
        "menu",
        "header",
        "footer",
        "topbar",
        "banner",
        "social",
        "announcement",
        "pagination",
    }
    for tag in list(working.find_all(True)):
        try:
            classes = " ".join(tag.get("class") or []).lower()
            elem_id = (tag.get("id") or "").lower()
        except Exception:
            continue
        if any(k in classes for k in keywords) or any(k in elem_id for k in keywords):
            tag.decompose()
    for selector in (
        "#content-area",
        "#content",
        "#main-content",
        "main",
        "article",
        "[role=main]",
    ):
        tag = working.select_one(selector)
        if tag:
            return str(tag)
    candidates = working.find_all(["main", "article", "section", "div"])
    best = None
    best_len = 0
    for candidate in candidates:
        text_len = len(candidate.get_text(" ", strip=True))
        if text_len > best_len:
            best = candidate
            best_len = text_len
    if best is not None:
        return str(best)
    if working.body:
        return str(working.body)
    return str(working)


def fetch_page(url: str) -> BeautifulSoup | None:
    for attempt in range(3):
        try:
            response = SESSION.get(url, timeout=30)
            if response.status_code != 200:
                return None
            return BeautifulSoup(response.text, "html.parser")
        except requests.exceptions.SSLError:
            try:
                response = SESSION.get(url, timeout=30, verify=False)
                if response.status_code != 200:
                    return None
                return BeautifulSoup(response.text, "html.parser")
            except Exception:
                continue
        except Exception:
            if attempt == 2:
                return None
    return None


def clean_markdown(md: str) -> str:
    md = re.sub(r"\*\*\s+([^*]+?)\s+\*\*", r"**\1**", md)
    md = re.sub(r"([A-Za-z0-9])\*\*([A-Za-z])", r"\1 **\2", md)
    md = re.sub(r"\*\*([^*]+)\*\*(\S)", r"**\1** \2", md)
    lines = []
    for line in md.splitlines():
        line = re.sub(r"^(#+)\s*\[[^\]]*\]\([^)]+\)\s*", r"\1 ", line)
        stripped = line.strip()
        if not stripped:
            lines.append(line)
            continue
        if stripped in {"⌘I", "⌘KAsk AI", "Ask AI"}:
            continue
        if stripped.lower() in {
            "skip to main content",
            "search...",
            "copy page",
            "navigation",
            "get started",
            "on this page",
        }:
            continue
        if stripped.lower() == "copy":
            continue
        if "mintlify.com" in stripped.lower() or stripped.lower().startswith("powered by"):
            continue
        if re.fullmatch(r"(\[[^\]]+\]\([^)]+\)\s*){2,}", stripped):
            if any(
                host in stripped.lower()
                for host in (
                    "x.com/",
                    "github.com/",
                    "linkedin.com/",
                    "fint.io",
                )
            ):
                continue
        lines.append(line)
    cleaned_lines = []
    first_h1 = None
    in_code = False
    for idx, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code = not in_code
            cleaned_lines.append(line)
            continue
        if not in_code and stripped.startswith("# "):
            if first_h1 is None:
                first_h1 = stripped
            elif stripped == first_h1:
                continue
        cleaned_lines.append(line)
    cleaned = "\n".join(cleaned_lines)
    cleaned = clean_path_blocks(cleaned)
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    return cleaned.strip() + "\n"


def clean_path_blocks(md: str) -> str:
    lines = md.splitlines()
    cleaned = []
    in_code = False
    methods = {"get", "post", "put", "patch", "delete"}
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code = not in_code
            cleaned.append(line)
            i += 1
            continue
        if in_code:
            cleaned.append(line)
            i += 1
            continue
        if stripped.lower() in methods:
            j = i + 1
            parts = []
            while j < len(lines):
                token = lines[j].strip()
                if token == "":
                    j += 1
                    continue
                if token == "/":
                    parts.append("/")
                    j += 1
                    continue
                if re.fullmatch(r"[a-z0-9_-]+", token, flags=re.IGNORECASE):
                    parts.append(token)
                    j += 1
                    continue
                break
            if parts:
                path = "".join([p if p == "/" else p for p in parts]).replace("//", "/")
                if not path.startswith("/"):
                    path = "/" + path
                cleaned.append(f"{stripped.upper()} {path}")
                i = j
                continue
        if stripped in {"/"}:
            i += 1
            continue
        cleaned.append(line)
        i += 1
    return "\n".join(cleaned)


def convert_html_to_markdown(html: str) -> str:
    md = markdownify(html, heading_style="ATX")
    return clean_markdown(md)


def write_markdown_file(rel_path: str, title: str, content_md: str) -> None:
    path = os.path.join(OUTPUT_DIR, rel_path)
    directory = os.path.dirname(path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)
    first_line = content_md.lstrip().splitlines()[0] if content_md.strip() else ""
    if not first_line.startswith("# "):
        content_md = f"# {title}\n\n{content_md}"
    with open(path, "w", encoding="utf-8") as f:
        f.write(content_md)


def extract_links(soup: BeautifulSoup) -> list[str]:
    links: list[str] = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if href.startswith("#"):
            continue
        absolute = urljoin(BASE_URL, href)
        normalized = normalize_url(absolute)
        if not is_same_site(normalized):
            continue
        if is_asset(normalized):
            continue
        links.append(normalized)
    return links


def rel_link(from_rel_path: str, to_url: str) -> str:
    to_rel = url_to_rel_path(to_url)
    if to_rel == "README.md":
        to_rel = "README.md"
    from_dir = os.path.dirname(from_rel_path)
    if not from_dir:
        return to_rel.replace("\\", "/")
    rel = os.path.relpath(to_rel, start=from_dir)
    return rel.replace("\\", "/")


def rewrite_links(md: str, from_rel_path: str) -> str:
    def replace_match(match: re.Match) -> str:
        url = match.group(1)
        if url.startswith("http://") or url.startswith("https://"):
            if not is_same_site(url):
                return match.group(0)
            target = normalize_url(url)
            return f"]({rel_link(from_rel_path, target)})"
        if url.startswith("/"):
            target = normalize_url(urljoin(BASE_URL, url))
            return f"]({rel_link(from_rel_path, target)})"
        return match.group(0)

    return re.sub(r"\]\(([^)]+)\)", replace_match, md)


def clear_markdown_files() -> None:
    for root, dirs, files in os.walk(OUTPUT_DIR):
        if ".git" in dirs:
            dirs.remove(".git")
        for name in files:
            if name.lower().endswith(".md"):
                os.remove(os.path.join(root, name))


def generate_summary(pages: list[tuple[str, str]]) -> None:
    summary_path = os.path.join(OUTPUT_DIR, "SUMMARY.md")
    lines = ["# Summary", ""]
    pages_sorted = sorted(pages, key=lambda x: x[0].lower())
    root_entries = [(t, p) for t, p in pages_sorted if p == "README.md"]
    if root_entries:
        root_title, root_path = root_entries[0]
        lines.append(f"* [{root_title}]({root_path})")
    else:
        lines.append("* [Home](README.md)")
    sections: dict[str, list[tuple[str, str]]] = {
        "Get Started": [],
        "Frontend SDK": [],
        "Backend SDK": [],
        "Security": [],
        "Testing": [],
        "API Reference": [],
        "Other": [],
    }
    for title, rel_path in pages_sorted:
        if rel_path == "README.md":
            continue
        rel_norm = rel_path.replace("\\", "/")
        if rel_norm.startswith("frontend/"):
            sections["Frontend SDK"].append((title, rel_path))
        elif rel_norm.startswith("fint-sdk/"):
            sections["Backend SDK"].append((title, rel_path))
        elif rel_norm.startswith("api-reference/"):
            sections["API Reference"].append((title, rel_path))
        elif rel_norm.startswith("testing/"):
            sections["Testing"].append((title, rel_path))
        elif rel_norm in {
            "introduction.md",
            "system-overview.md",
            "payment-flow.md",
            "payment-flow-scenarios.md",
            "support.md",
        }:
            sections["Get Started"].append((title, rel_path))
        elif rel_norm in {"best-practices.md", "policy-engine-safety.md"}:
            sections["Security"].append((title, rel_path))
        else:
            sections["Other"].append((title, rel_path))
    for section, items in sections.items():
        if not items:
            continue
        lines.append(f"")
        lines.append(f"## {section}")
        for title, rel_path in items:
            lines.append(f"* [{title}]({rel_path.replace(os.sep, '/')})")
    with open(summary_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def crawl() -> None:
    clear_markdown_files()
    start_url = normalize_url(BASE_URL)
    queue: list[str] = [start_url]
    visited: set[str] = set()
    pages: list[tuple[str, str]] = []
    while queue:
        url = queue.pop(0)
        if url in visited:
            continue
        visited.add(url)
        soup = fetch_page(url)
        if soup is None:
            continue
        rel_path = url_to_rel_path(url)
        title = extract_title(soup, urlparse(url).path or "/")
        html_main = extract_main_html(soup)
        markdown = convert_html_to_markdown(html_main)
        markdown = rewrite_links(markdown, rel_path)
        write_markdown_file(rel_path, title, markdown)
        pages.append((title, rel_path))
        for link in extract_links(soup):
            if link not in visited and link not in queue:
                queue.append(link)
    if pages:
        generate_summary(pages)


def main() -> None:
    crawl()


if __name__ == "__main__":
    main()

