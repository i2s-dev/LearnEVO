/* Main app — loads data, wires router, search, keyboard shortcuts. */
(function () {
  'use strict';

  const state = {
    pages: null,
    search: null,
    nav: null,
    keywords: null,
    currentId: null,
    searchResults: [],
    selectedResult: -1
  };

  const $ = sel => document.querySelector(sel);
  const $$ = sel => [...document.querySelectorAll(sel)];

  function fetchJSON(path) {
    return fetch(path).then(r => {
      if (!r.ok) throw new Error('Failed to load ' + path + ': ' + r.status);
      return r.json();
    });
  }

  function setLoading(msg) {
    const el = $('#content');
    if (el) el.innerHTML = '<p style="color:#586069">' + msg + '</p>';
  }

  async function boot() {
    try {
      setLoading('Loading…');
      const [pages, search, nav, keywords, stats] = await Promise.all([
        fetchJSON('data/pages.json'),
        fetchJSON('data/search.json'),
        fetchJSON('data/nav.json'),
        fetchJSON('data/keywords.json'),
        fetchJSON('data/stats.json').catch(() => null)
      ]);
      state.pages = pages;
      state.search = search;
      state.nav = nav;
      state.keywords = keywords;
      if (stats) {
        $('#stats-tag').textContent =
          stats.pages + ' pages · ' +
          stats.by_kind.topic + ' topics · ' +
          stats.by_kind.recipe + ' recipes · ' +
          stats.by_kind.module + ' modules · ' +
          stats.by_kind.menu + ' menu codes · ' +
          stats.by_kind.table + ' tables · ' +
          stats.by_kind.form + ' forms';
      }

      wireUp();
      routeFromHash();

      // Defer the heavy sidebar render so the first paint is fast.
      setTimeout(() => {
        $('#sidebar-nav').innerHTML = EvoRenderer.renderSidebar(nav);
        highlightActiveNav();
      }, 20);
    } catch (e) {
      console.error('[EVO Help] Boot failed:', e);
      $('#content').innerHTML =
        '<h1>Failed to load help data</h1>' +
        '<p><strong>Error:</strong> ' + escapeHtml(e.message || String(e)) + '</p>' +
        '<p>If opening directly from the file system: use the <code>RUN.bat</code> launcher ' +
        'or run <code>python server.py</code> from the <code>learnevo-help</code> folder. ' +
        'Open the browser\'s developer console (F12) for more details.</p>';
    }
  }

  function highlightActiveNav() {
    const id = state.currentId;
    if (!id) return;
    $$('#sidebar-nav a.active').forEach(a => a.classList.remove('active'));
    const active = $('#sidebar-nav a[data-nav="' + id + '"]');
    if (active) {
      active.classList.add('active');
      let el = active.parentElement;
      while (el) {
        if (el.tagName === 'DETAILS') el.open = true;
        el = el.parentElement;
      }
    }
  }

  function routeFromHash() {
    let id = (location.hash || '#welcome').replace(/^#/, '') || 'welcome';
    // Check for an anchor jump like "something#menu-AR-A"
    if (!state.pages[id]) {
      // If search-like query, treat as search
      if (id.length > 1) {
        runSearch(decodeURIComponent(id));
        $('#search-input').value = decodeURIComponent(id);
      }
      return;
    }
    state.currentId = id;
    const p = state.pages[id];
    $('#content').innerHTML = EvoRenderer.renderPage(p, state.pages);
    $('#breadcrumbs').innerHTML = EvoRenderer.renderBreadcrumbs(p);
    // Defer the heavy related-links scan — it walks all 2700 pages.
    $('#related-links').innerHTML = '';
    setTimeout(() => {
      if (state.currentId === id) {
        $('#related-links').innerHTML = EvoRenderer.renderRelated(p, state.pages);
      }
    }, 40);
    // Highlight in sidebar (if sidebar is rendered yet)
    highlightActiveNav();
    // Scroll content to top
    $('#page').scrollTop = 0;
    // Close search results if open
    hideResults();
  }

  function wireUp() {
    window.addEventListener('hashchange', routeFromHash);

    const input = $('#search-input');
    let searchTimeout;
    input.addEventListener('input', () => {
      clearTimeout(searchTimeout);
      searchTimeout = setTimeout(() => runSearch(input.value), 80);
    });
    input.addEventListener('focus', () => {
      if (input.value.trim()) runSearch(input.value);
    });
    input.addEventListener('keydown', e => {
      const results = $('#search-results');
      const items = [...results.querySelectorAll('li')];
      if (e.key === 'ArrowDown') {
        e.preventDefault();
        state.selectedResult = Math.min(state.selectedResult + 1, items.length - 1);
        renderActiveResult();
      } else if (e.key === 'ArrowUp') {
        e.preventDefault();
        state.selectedResult = Math.max(state.selectedResult - 1, -1);
        renderActiveResult();
      } else if (e.key === 'Enter') {
        e.preventDefault();
        if (state.selectedResult >= 0 && items[state.selectedResult]) {
          const a = items[state.selectedResult].querySelector('a');
          if (a) { location.hash = a.getAttribute('href'); hideResults(); input.blur(); }
        } else if (state.searchResults.length > 0) {
          location.hash = '#' + state.searchResults[0].pid;
          hideResults();
          input.blur();
        }
      } else if (e.key === 'Escape') {
        hideResults();
        input.blur();
      }
    });

    // Global keyboard shortcuts
    document.addEventListener('keydown', e => {
      const tag = (e.target && e.target.tagName) || '';
      const isInput = tag === 'INPUT' || tag === 'TEXTAREA' || tag === 'SELECT';
      // Ctrl+K / Cmd+K → focus search
      if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
        e.preventDefault();
        $('#search-input').focus();
        $('#search-input').select();
        return;
      }
      if (isInput) return;
      // / → focus search
      if (e.key === '/') {
        e.preventDefault();
        $('#search-input').focus();
        return;
      }
      // Esc → clear search or unfocus
      if (e.key === 'Escape') {
        hideResults();
        return;
      }
      // g h → home
      if (e.key === 'g') {
        state.gPrefix = true;
        setTimeout(() => state.gPrefix = false, 800);
        return;
      }
      if (state.gPrefix) {
        state.gPrefix = false;
        if (e.key === 'h') location.hash = '#welcome';
        else if (e.key === 'r') location.hash = '#recipes-index';
        else if (e.key === 'm') location.hash = '#module-map';
        else if (e.key === 't') location.hash = '#tables-index';
      }
    });

    // Hide search when clicking outside
    document.addEventListener('click', e => {
      if (!e.target.closest('.searchbox')) hideResults();
    });

    // Sidebar toggle
    $('#toggle-sidebar').addEventListener('click', () => {
      $('#sidebar').classList.toggle('collapsed');
    });
  }

  function runSearch(query) {
    query = query.trim();
    const results = $('#search-results');
    if (!query) { hideResults(); return; }
    const hits = EvoSearch.search(query, state.search, state.keywords, 30);
    state.searchResults = hits;
    state.selectedResult = -1;
    if (!hits.length) {
      results.innerHTML = '<li class="no-results">No matches for "' + escapeHtml(query) + '"</li>';
      results.hidden = false;
      return;
    }
    const html = hits.map((h, i) => {
      const s = h.sum;
      const kindClass = s.kind;
      return '<li data-idx="' + i + '"><a href="#' + s.id + '">' +
             '<div class="result-title">' + escapeHtml(s.title) +
             '<span class="result-kind ' + kindClass + '">' + s.kind + '</span></div>' +
             (s.snippet ? '<div class="result-snippet">' + escapeHtml(s.snippet.substring(0, 160)) + '</div>' : '') +
             '<div class="result-path">' + escapeHtml(s.section) + (s.module ? ' · ' + s.module : '') + '</div>' +
             '</a></li>';
    }).join('');
    results.innerHTML = html;
    results.hidden = false;
  }

  function renderActiveResult() {
    const results = $('#search-results');
    [...results.querySelectorAll('li')].forEach((li, i) => {
      if (i === state.selectedResult) li.classList.add('active');
      else li.classList.remove('active');
    });
    const active = results.querySelector('li.active');
    if (active) active.scrollIntoView({ block: 'nearest' });
  }

  function hideResults() {
    const r = $('#search-results');
    r.hidden = true;
    state.selectedResult = -1;
  }

  function escapeHtml(s) {
    return String(s || '').replace(/[&<>"']/g, ch => ({
      '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'
    }[ch]));
  }

  boot();
})();
