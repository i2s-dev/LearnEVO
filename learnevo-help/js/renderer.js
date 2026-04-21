/* Renderer — turns page data into HTML, renders sidebar nav, handles
 * related-links and breadcrumbs.
 */
(function (global) {
  'use strict';

  function escapeHtml(s) {
    return String(s || '').replace(/[&<>"']/g, ch => ({
      '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'
    }[ch]));
  }

  function renderPage(page, pages) {
    if (!page) {
      return '<h1>Page not found</h1><p>Try the search above or return to <a href="#welcome">Home</a>.</p>';
    }
    // Route breadcrumbs for recipes
    let breadcrumb = '';
    if (page.kind === 'recipe' && page.route && page.route.length) {
      breadcrumb = '<div class="route">Route: ' +
        page.route.map(r => '<code>' + escapeHtml(r) + '</code>').join(' → ') + '</div>';
    }
    const html = MarkedLite.render(page.body || '');
    return breadcrumb + html;
  }

  function renderBreadcrumbs(page) {
    if (!page) return '';
    const parts = [
      '<a href="#welcome">Home</a>',
      '<span class="sep">›</span>',
      '<a href="#">' + escapeHtml(page.section || '') + '</a>',
      '<span class="sep">›</span>',
      '<span>' + escapeHtml(page.title) + '</span>'
    ];
    return parts.join(' ');
  }

  function renderRelated(page, pages) {
    if (!page) return '';
    const parts = [];
    const extractLinks = (md) => {
      const out = new Set();
      if (!md) return out;
      const re = /\(#([a-zA-Z0-9_\-.]+)\)/g;
      let m;
      while ((m = re.exec(md))) out.add(m[1]);
      return out;
    };
    const outbound = [...extractLinks(page.body)];
    const inbound = [];
    for (const pid in pages) {
      if (pid === page.id) continue;
      if (pages[pid].body && pages[pid].body.includes('#' + page.id + ')')) {
        inbound.push(pid);
      }
    }
    if (outbound.length || inbound.length) {
      parts.push('<strong>Links out:</strong> ' +
        outbound.slice(0, 12).map(pid => {
          const t = pages[pid] ? pages[pid].title : pid;
          return '<a href="#' + pid + '">' + escapeHtml(t) + '</a>';
        }).join(' · '));
      if (inbound.length) {
        parts.push('<br/><strong>Links in:</strong> ' +
          inbound.slice(0, 12).map(pid => {
            const t = pages[pid] ? pages[pid].title : pid;
            return '<a href="#' + pid + '">' + escapeHtml(t) + '</a>';
          }).join(' · '));
      }
    }
    return parts.join(' ');
  }

  function renderSidebar(nav) {
    const parts = [];
    // Priority sections at top
    const priority = ['Getting Started', 'Concepts', 'Architecture', 'Modules',
                      'Recipes', 'Data', 'Reference', 'Integration', 'Glossary',
                      'Menu codes', 'Tables', 'Forms'];
    for (const sec of priority) {
      if (!nav[sec]) continue;
      const items = nav[sec];
      if (Array.isArray(items)) {
        // Flat list
        if (!items.length) continue;
        parts.push('<details' + (['Getting Started', 'Concepts', 'Architecture', 'Modules', 'Recipes'].includes(sec) ? ' open' : '') + '>');
        parts.push('<summary>' + escapeHtml(sec) + ' <span class="count">(' + items.length + ')</span></summary>');
        parts.push('<ul>');
        for (const it of items) {
          parts.push('<li><a href="#' + it.id + '" data-nav="' + it.id + '">' + escapeHtml(it.title) + '</a></li>');
        }
        parts.push('</ul></details>');
      } else {
        // Nested by module
        const mods = Object.keys(items).sort();
        const totalCount = mods.reduce((a, m) => a + items[m].length, 0);
        if (!totalCount) continue;
        parts.push('<details>');
        parts.push('<summary>' + escapeHtml(sec) + ' <span class="count">(' + totalCount + ')</span></summary>');
        for (const mod of mods) {
          const sub = items[mod];
          parts.push('<details>');
          parts.push('<summary>' + escapeHtml(mod) + ' <span class="count">(' + sub.length + ')</span></summary>');
          parts.push('<ul>');
          // Cap list length — unfurl with show-more if needed
          const shown = sub.slice(0, 120);
          for (const it of shown) {
            parts.push('<li><a href="#' + it.id + '" data-nav="' + it.id + '">' + escapeHtml(it.title) + '</a></li>');
          }
          if (sub.length > 120) {
            parts.push('<li><em>... ' + (sub.length - 120) + ' more</em></li>');
          }
          parts.push('</ul></details>');
        }
        parts.push('</details>');
      }
    }
    return parts.join('');
  }

  global.EvoRenderer = {
    renderPage: renderPage,
    renderBreadcrumbs: renderBreadcrumbs,
    renderRelated: renderRelated,
    renderSidebar: renderSidebar
  };
})(window);
