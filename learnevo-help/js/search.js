/* Search engine — works on the prebuilt inverted index + keyword map.
 *
 * Query behavior:
 *   - Split into tokens.
 *   - For each token, look up postings in the index and score pages by
 *     summed weight. Also consult the keyword alias map.
 *   - Bonus if ALL query tokens appear in the same page.
 *   - Big bonus (multiplier 5) if query matches a page title exactly
 *     or an exact menu-code / table-name.
 */
(function (global) {
  'use strict';

  const STOP = new Set("the a an and or of to in on at for is are was were be been being have has had do does did will would could should may might can shall this that these those i you he she it we they me him her us them my your his their our which what when where why how".split(/\s+/));

  function tokenize(s) {
    if (!s) return [];
    return s.toLowerCase()
      .match(/[a-z0-9_\-]+/g) ?.filter(t => t.length > 1 && !STOP.has(t)) || [];
  }

  function normalize(s) { return s.toLowerCase().trim(); }

  function search(query, indexData, keywordMap, limit) {
    limit = limit || 30;
    const q = normalize(query);
    if (!q) return [];
    const tokens = tokenize(q);
    if (!tokens.length) return [];

    const { index, summaries } = indexData;

    // Score per page_id: start from 0
    const scores = Object.create(null);

    // 1) Exact-match boosts for specific query forms.
    // Menu code like "AR-A" or "AP-H" → boost menu-AR-A page
    const menuMatch = q.match(/^[a-z]{2}-[a-z](?:-[a-z])?$/i);
    if (menuMatch) {
      const code = q.toUpperCase();
      const pid = 'menu-' + code;
      if (summaries[pid]) scores[pid] = (scores[pid] || 0) + 1000;
    }
    // Table name like "BKARCUST"
    const tableMatch = q.match(/^[A-Z][A-Z0-9_]{2,}$/i);
    if (tableMatch) {
      const pid = 'table-' + q.toUpperCase();
      if (summaries[pid]) scores[pid] = (scores[pid] || 0) + 1000;
    }
    // Module code like "AR" or "PR"
    if (/^[a-z]{2}$/i.test(q)) {
      const pid = 'module-' + q.toUpperCase();
      if (summaries[pid]) scores[pid] = (scores[pid] || 0) + 500;
    }
    // DFM form name
    if (/\.dfm$/i.test(q)) {
      const pid = 'form-' + q.toUpperCase().replace(/^FORM-/, '');
      // summaries keys are exact; try both cases
      for (const id in summaries) {
        if (id.toLowerCase() === 'form-' + q.toLowerCase()) {
          scores[id] = (scores[id] || 0) + 1000;
        }
      }
    }

    // 2) Keyword alias map: "customer" → [module-AR, table-BKARCUST, ...]
    if (keywordMap[q]) {
      for (const pid of keywordMap[q]) {
        if (summaries[pid]) scores[pid] = (scores[pid] || 0) + 200;
      }
    }
    // Also try phrase with spaces collapsed and each token
    for (const t of tokens) {
      if (keywordMap[t]) {
        for (const pid of keywordMap[t]) {
          if (summaries[pid]) scores[pid] = (scores[pid] || 0) + 80;
        }
      }
    }

    // 3) Inverted-index scoring
    const tokenPageSets = [];
    for (const tok of tokens) {
      const postings = index[tok];
      if (!postings) {
        // Try prefix match for unknown tokens
        const matchingTokens = Object.keys(index).filter(t => t.startsWith(tok) && t.length <= tok.length + 4).slice(0, 5);
        const mergedPostings = [];
        for (const mt of matchingTokens) {
          for (const [pid, sc] of index[mt]) {
            mergedPostings.push([pid, sc * 0.5]);
          }
        }
        if (mergedPostings.length) {
          const pagesInThisToken = new Set();
          for (const [pid, sc] of mergedPostings) {
            scores[pid] = (scores[pid] || 0) + sc;
            pagesInThisToken.add(pid);
          }
          tokenPageSets.push(pagesInThisToken);
        }
        continue;
      }
      const pagesInThisToken = new Set();
      for (const [pid, sc] of postings) {
        scores[pid] = (scores[pid] || 0) + sc;
        pagesInThisToken.add(pid);
      }
      tokenPageSets.push(pagesInThisToken);
    }

    // 4) AND-bonus: pages that contain all tokens get a boost
    if (tokens.length > 1 && tokenPageSets.length === tokens.length) {
      let intersection = null;
      for (const set of tokenPageSets) {
        if (intersection === null) intersection = new Set(set);
        else intersection = new Set([...intersection].filter(x => set.has(x)));
      }
      for (const pid of intersection || []) {
        scores[pid] = (scores[pid] || 0) + 50 * tokens.length;
      }
    }

    // 5) Kind-based light re-ranking so topics come above form/table floods for general queries
    const RANK_BONUS = { topic: 15, recipe: 12, module: 10, glossary: 8, menu: 4, table: 1, form: 0 };
    for (const pid in scores) {
      const sum = summaries[pid];
      if (sum) scores[pid] += RANK_BONUS[sum.kind] || 0;
      // Also bonus for title containing full query substring
      if (sum && sum.title.toLowerCase().includes(q)) {
        scores[pid] += 200;
      }
    }

    // 6) Sort and cap
    return Object.keys(scores)
      .map(pid => ({ pid, score: scores[pid], sum: summaries[pid] }))
      .filter(r => r.sum)
      .sort((a, b) => b.score - a.score)
      .slice(0, limit);
  }

  global.EvoSearch = { search: search };
})(window);
