(function () {
    var bound = false;

    function ensureProgressBar() {
        var container = document.querySelector('.fintdoc-progress');
        if (!container) {
            container = document.createElement('div');
            container.className = 'fintdoc-progress';
            var bar = document.createElement('div');
            bar.className = 'fintdoc-progress-bar';
            container.appendChild(bar);
            document.body.appendChild(container);
        }
        return container.querySelector('.fintdoc-progress-bar');
    }

    function updateProgressBar() {
        var bar = ensureProgressBar();
        if (!bar) {
            return;
        }
        var doc = document.documentElement;
        var scrollTop = doc.scrollTop || document.body.scrollTop;
        var scrollHeight = doc.scrollHeight - doc.clientHeight;
        var ratio = scrollHeight > 0 ? scrollTop / scrollHeight : 0;
        var clamped = Math.min(1, Math.max(0, ratio));
        bar.style.transform = 'scaleX(' + clamped + ')';
    }

    function getTitleFromLabel(label) {
        return label
            .replace(/^Previous page:\s*/i, '')
            .replace(/^Next page:\s*/i, '')
            .trim();
    }

    function buildBottomLink(source, label) {
        var link = document.createElement('a');
        link.href = source.getAttribute('href') || '#';
        link.className = 'fintdoc-bottom-nav-link';
        link.setAttribute('data-direction', label.toLowerCase());

        var meta = document.createElement('span');
        meta.className = 'fintdoc-bottom-nav-meta';
        meta.textContent = label;

        var title = document.createElement('span');
        title.className = 'fintdoc-bottom-nav-title';
        var ariaLabel = source.getAttribute('aria-label') || '';
        var cleaned = getTitleFromLabel(ariaLabel);
        title.textContent = cleaned || source.textContent.trim() || link.href;

        link.appendChild(meta);
        link.appendChild(title);

        return link;
    }

    function renderBottomNav() {
        var existing = document.querySelector('.fintdoc-bottom-nav');
        if (existing) {
            existing.remove();
        }

        var prev = document.querySelector('.navigation-prev');
        var next = document.querySelector('.navigation-next');
        if (!prev && !next) {
            return;
        }

        var container = document.createElement('div');
        container.className = 'fintdoc-bottom-nav';

        var inner = document.createElement('div');
        inner.className = 'fintdoc-bottom-nav-inner';
        container.appendChild(inner);

        if (prev) {
            inner.appendChild(buildBottomLink(prev, 'Previous'));
        }
        if (next) {
            inner.appendChild(buildBottomLink(next, 'Next'));
        }

        var pageInner = document.querySelector('.page-wrapper .page-inner');
        if (pageInner) {
            pageInner.appendChild(container);
        }
    }

    function initPage() {
        updateProgressBar();
        renderBottomNav();
    }

    function bindScroll() {
        if (bound) {
            return;
        }
        bound = true;
        window.addEventListener('scroll', updateProgressBar, { passive: true });
        window.addEventListener('resize', updateProgressBar);
    }

    if (window.gitbook && gitbook.events && typeof gitbook.events.bind === 'function') {
        gitbook.events.bind('page.change', function () {
            initPage();
            bindScroll();
        });
    } else {
        document.addEventListener('DOMContentLoaded', function () {
            initPage();
            bindScroll();
        });
    }
})();
