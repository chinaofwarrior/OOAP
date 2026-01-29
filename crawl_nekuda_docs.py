import os
from urllib.parse import urljoin, urlparse, urlunparse

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify


BASE_URL = "https://docs.nekuda.ai"
OUTPUT_DIR = "."
SESSION = requests.Session()


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
    parsed_base = urlparse(BASE_URL)
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
    return path.replace("/", "_") + ".md"


def extract_title(soup: BeautifulSoup, fallback: str) -> str:
    h1 = soup.find("h1")
    if h1 and h1.get_text(strip=True):
        return h1.get_text(strip=True)
    title_tag = soup.find("title")
    if title_tag and title_tag.get_text(strip=True):
        return title_tag.get_text(strip=True)
    return fallback


def extract_main_html(soup: BeautifulSoup) -> str:
    for selector in ("main", "article"):
        tag = soup.find(selector)
        if tag:
            return str(tag)
    if soup.body:
        return str(soup.body)
    return str(soup)


def fetch_page(url: str) -> BeautifulSoup | None:
    try:
        response = SESSION.get(url, timeout=20)
        if response.status_code != 200:
            return None
        return BeautifulSoup(response.text, "html.parser")
    except Exception:
        return None


def convert_html_to_markdown(html: str) -> str:
    return markdownify(html, heading_style="ATX")


def write_markdown_file(rel_path: str, title: str, content_md: str) -> None:
    path = os.path.join(OUTPUT_DIR, rel_path)
    directory = os.path.dirname(path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)
    first_line = content_md.lstrip().splitlines()[0] if content_md.strip() else ""
    if not first_line.startswith("#"):
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


def generate_summary(pages: list[tuple[str, str]]) -> None:
    summary_path = os.path.join(OUTPUT_DIR, "SUMMARY.md")
    lines = ["# Summary", ""]
    pages_sorted = sorted(pages, key=lambda x: x[0].lower())
    root_entries = []
    other_entries = []
    for title, rel_path in pages_sorted:
        if rel_path == "README.md":
            root_entries.append((title, rel_path))
        else:
            other_entries.append((title, rel_path))
    if not root_entries:
        lines.append("* [Home](README.md)")
    else:
        root_title, root_path = root_entries[0]
        lines.append(f"* [{root_title}]({root_path})")
    for title, rel_path in other_entries:
        lines.append(f"* [{title}]({rel_path})")
    with open(summary_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def crawl() -> None:
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

