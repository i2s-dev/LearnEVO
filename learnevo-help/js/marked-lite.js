/* Tiny Markdown renderer — supports the subset we use in topics.
 * Not a full parser; deliberately lean. Handles:
 *   # ## ### ####      headings
 *   **bold** _italic_
 *   `code`
 *   ```   fenced code blocks
 *   - /  * /  1.        lists
 *   > blockquote
 *   [label](url)         links
 *   | a | b |            tables (header-row + separator)
 *   ---                  hr
 * Intentionally does NOT support HTML passthrough — safer.
 */
(function (global) {
  'use strict';

  function escapeHtml(s) {
    return s.replace(/[&<>]/g, ch => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;' }[ch]));
  }

  function renderInline(s) {
    // escape first
    s = escapeHtml(s);
    // code
    s = s.replace(/`([^`]+)`/g, (_, c) => '<code>' + c + '</code>');
    // links [label](url)
    s = s.replace(/\[([^\]]+)\]\(([^)\s]+)\)/g, (_, label, url) => {
      return '<a href="' + url + '">' + label + '</a>';
    });
    // bold
    s = s.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');
    // italic (underscore form)
    s = s.replace(/(^|\s)_([^_]+)_(\s|$|[.,;:!?])/g, '$1<em>$2</em>$3');
    return s;
  }

  function render(md) {
    if (!md) return '';
    const lines = md.split(/\r?\n/);
    const out = [];
    let i = 0;
    while (i < lines.length) {
      const line = lines[i];
      // fenced code block
      if (/^```/.test(line)) {
        const lang = line.slice(3).trim();
        i++;
        const codeLines = [];
        while (i < lines.length && !/^```/.test(lines[i])) {
          codeLines.push(lines[i]);
          i++;
        }
        i++;
        out.push('<pre><code' + (lang ? ' class="lang-' + lang + '"' : '') + '>' +
                 escapeHtml(codeLines.join('\n')) + '</code></pre>');
        continue;
      }
      // headings
      const h = /^(#{1,6})\s+(.+)$/.exec(line);
      if (h) {
        const lvl = h[1].length;
        out.push('<h' + lvl + '>' + renderInline(h[2]) + '</h' + lvl + '>');
        i++;
        continue;
      }
      // hr
      if (/^---+\s*$/.test(line)) { out.push('<hr/>'); i++; continue; }
      // blockquote
      if (/^>\s?/.test(line)) {
        const bqLines = [];
        while (i < lines.length && /^>\s?/.test(lines[i])) {
          bqLines.push(lines[i].replace(/^>\s?/, ''));
          i++;
        }
        out.push('<blockquote>' + renderInline(bqLines.join(' ')) + '</blockquote>');
        continue;
      }
      // table (pipe)
      if (/^\|.*\|$/.test(line) && /^\|[\s:|-]+\|$/.test(lines[i + 1] || '')) {
        const header = line.split('|').slice(1, -1).map(c => c.trim());
        i += 2;
        const body = [];
        while (i < lines.length && /^\|.*\|$/.test(lines[i])) {
          body.push(lines[i].split('|').slice(1, -1).map(c => c.trim()));
          i++;
        }
        const th = header.map(c => '<th>' + renderInline(c) + '</th>').join('');
        const rows = body.map(r =>
          '<tr>' + r.map(c => '<td>' + renderInline(c) + '</td>').join('') + '</tr>'
        ).join('');
        out.push('<table><thead><tr>' + th + '</tr></thead><tbody>' + rows + '</tbody></table>');
        continue;
      }
      // list (unordered)
      if (/^(\s*[-*])\s+/.test(line)) {
        const items = [];
        while (i < lines.length && /^(\s*[-*])\s+/.test(lines[i])) {
          items.push(lines[i].replace(/^(\s*[-*])\s+/, ''));
          i++;
        }
        out.push('<ul>' + items.map(t => '<li>' + renderInline(t) + '</li>').join('') + '</ul>');
        continue;
      }
      // list (ordered)
      if (/^(\s*\d+\.)\s+/.test(line)) {
        const items = [];
        while (i < lines.length && /^(\s*\d+\.)\s+/.test(lines[i])) {
          items.push(lines[i].replace(/^(\s*\d+\.)\s+/, ''));
          i++;
        }
        out.push('<ol>' + items.map(t => '<li>' + renderInline(t) + '</li>').join('') + '</ol>');
        continue;
      }
      // paragraph — consume current line, then slurp continuation lines
      // until we hit a blank line or a line that starts a block construct.
      if (line.trim()) {
        const paraLines = [line];
        i++;
        while (i < lines.length) {
          const nxt = lines[i];
          if (!nxt.trim()) break;          // blank ends paragraph
          if (/^```/.test(nxt)) break;
          if (/^#{1,6}\s+/.test(nxt)) break;
          if (/^---+\s*$/.test(nxt)) break;
          if (/^>\s?/.test(nxt)) break;
          if (/^\|.*\|$/.test(nxt)) break;
          if (/^\s*[-*]\s+/.test(nxt)) break;   // list
          if (/^\s*\d+\.\s+/.test(nxt)) break;  // ordered list
          paraLines.push(nxt);
          i++;
        }
        out.push('<p>' + renderInline(paraLines.join(' ')) + '</p>');
        continue;
      }
      i++;
    }
    return out.join('\n');
  }

  global.MarkedLite = { render: render };
})(window);
