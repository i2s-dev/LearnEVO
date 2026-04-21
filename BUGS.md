# BUGS — attempts log

Every bug I (Claude) work on in this workspace gets an entry here. For each
bug I record **every single thing I try**, whether it works or not, so I
never repeat a failed fix and the user has a full paper trail.

Format per bug:

```
## <Date> — <Short title>
**Symptom:** what the user saw.
**Root cause (final understanding):** what was actually wrong.
**Attempts:**
1. <date/time> — <what I changed> — RESULT (worked / didn't work / why).
2. ...
**Status:** open | fixed | reverted
**Lesson:** the thing I must not forget.
```

Newest entries at the top.

---

## 2026-04-21 — Glossary see-also refs producing broken-link stubs

**Symptom:** 11 stub pages in the help browser (`Btrieve`, `CFB`, `DCY`,
`DDF`, `DFM`, `FIFO`, `Pervasive`, `RTM`, `Twofish`, `EvoHELP.CHM`,
`tp7runtime.exe`) — auto-generated because something linked to them, but
the real content already existed under `glossary-<slug>` IDs. Users
saw "This topic is referenced but not yet fully written" on click.

**Root cause (final understanding):**

- In [learnevo-help/build.py](learnevo-help/build.py), glossary entries'
  `see_also` lists pass each reference through `_resolve_ref()`, which
  only recognized table names and menu-code patterns. A bare term like
  `"Btrieve"` fell through unchanged and rendered as `[Btrieve](#Btrieve)`
  — a dangling link.
- Similarly, `convert_wiki_links()` (for `[[Term]]` in bodies) didn't
  canonicalize bare glossary terms either.
- Two binary-filename references (`EvoHELP.CHM`, `tp7runtime.exe`) had
  no glossary entries at all — so canonicalizing alone wouldn't fix them.

**Attempts:**

1. 2026-04-21 — Added `_glossary_pid(term)` + `_canonicalize(pid)` helpers
   to [learnevo-help/build.py](learnevo-help/build.py). Threaded
   `_canonicalize` through both `convert_wiki_links` and `_resolve_ref`.
   Added new glossary entries for `EvoHELP.CHM` and `tp7runtime.exe`
   in [learnevo-help/content/glossary.py](learnevo-help/content/glossary.py).
   Rebuild: stub count 104 → 90. **Partial result** — two new stubs
   appeared (`glossary-reportbuilder`, `glossary-tas-professional-tas-pro-7`).

2. 2026-04-21 — First new stub: I wrote `[[glossary-reportbuilder]]` in
   `format-rtm`, but the actual glossary pid is
   `glossary-nevrona-reportbuilder`. Changed to
   `[[Nevrona ReportBuilder|ReportBuilder]]` so the canonicalizer resolves
   it through the standard term lookup. **Worked.**

3. 2026-04-21 — Second new stub: my `_glossary_pid` had `.strip('-')` on
   the slug, but the original pid-generation at line 356 of build.py does
   NOT strip. So `"TAS Professional (TAS Pro 7)"` produced
   `glossary-tas-professional-tas-pro-7-` (trailing dash) in one place
   and `glossary-tas-professional-tas-pro-7` in the other — divergence.
   Removed `.strip('-')` so both paths agree byte-for-byte. **Worked.**

Final stub count: 104 → 88. All 11 broken links gone.

**Status:** fixed.

**Lesson:** When adding a new pid-generating helper, mirror the existing
generator's exact string transform (no extra `.strip()`, no case-folding
differences). A one-character divergence produces silent stub creation
that only shows up via rebuild comparison.

---

## 2026-04-21 — EVO Help hint bar overlapping sidebar + content (localhost:8766)

**Symptom:** The fixed black `.keyhint` bar at the bottom of the EVO Help
viewer overlapped the bottom of both the main article scroll area and the
left sidebar. Content was clipped. The sidebar's scrollbar extended behind
the hint bar, so the last entries (e.g. "other (186)", "Forms (1109)")
could not be scrolled fully into view. User is running the page in
**Microsoft Edge**.

**Root cause (final understanding):**
1. Layout bug: `.keyhint` was `position: fixed; bottom: 0`, so it floated on
   top of `#main`, which itself extended to the viewport bottom. Any scroll
   container inside `#main` (`#sidebar`, `#page`) had its scrollbar end
   behind the overlay. Padding-based workarounds were the wrong layer —
   the real fix was to put `.keyhint` in the document flow as a flex child
   of `<body>` so `#main` is bounded by the topbar above and the hint bar
   below.
2. Caching bug: Python's `SimpleHTTPServer` sends `Last-Modified` but no
   `Cache-Control`. Edge/Chromium then apply heuristic freshness — about
   10% of the (Date − Last-Modified) age — which for a file modified days
   ago is *hours* of silent caching. A plain reload served the stale CSS,
   making every attempted fix look like it hadn't run.

**Attempts:**
1. 2026-04-21 — Bumped `#page` bottom padding 60px → 96px (default + 920px
   media query). — Fixed the main article only; sidebar still clipped.
   **Wrong layer of fix** (treated a symptom, not the overlap itself).
2. 2026-04-21 — Added `padding: 10px 0 96px` to `#sidebar`. — Did not
   appear to work for the user; either heuristically-cached CSS or the
   old Chromium bug where `padding-bottom` on `overflow-y:auto` containers
   is dropped from the scroll extent. **Do not use `padding-bottom` on a
   flex-item overflow scroll container as the sole fix.**
3. 2026-04-21 — Reverted the sidebar padding and added
   `#sidebar-nav::after { content:""; display:block; height:96px }` as a
   real in-flow spacer. — Still failed for the user. Same root cause as
   above (overlay still on top of scrollbar and content), **plus** Edge
   was serving cached CSS. **Spacer hacks do not solve the problem when
   the overlay itself is the issue; and no CSS edit will help if the
   browser is serving a cached copy.**
4. 2026-04-21 — The real structural fix: removed `position: fixed` from
   `.keyhint`, made it `flex-shrink: 0` so it becomes a static flex child
   of `<body>`. `#main` now takes the remaining vertical space between
   `#topbar` and `.keyhint`, and both scroll containers inside `#main` end
   exactly at the top of the hint bar. Also reverted the padding/spacer
   hacks from attempts 1–3. — Correct fix, but the user kept seeing the
   old behavior because of cached CSS.
5. 2026-04-21 — Patched `server.py` `QuietHandler.end_headers()` to send
   `Cache-Control: no-store, must-revalidate`, `Pragma: no-cache`,
   `Expires: 0`. — **Insufficient by itself.** `no-store` applies to
   *future* responses. While Edge's existing heuristically-cached CSS
   entry is still considered fresh, the browser never hits the server to
   see the new header, so it keeps serving the old CSS with
   `position: fixed .keyhint` from cache. User's screenshot after this
   still showed the hint bar overlaying content.
6. 2026-04-21 — Cache-busted the asset URLs in `index.html`:
   `css/style.css?v=20260421b` and `js/*.js?v=20260421b`. Different URL
   from what Edge has cached, so the browser is forced to fetch the
   current files. Combined with attempt 5, any *future* CSS edit will
   come through on a plain reload (because every fresh response now
   carries `Cache-Control: no-store`), and if I ever need to guarantee a
   fresh fetch again I just bump the `?v=` string. — Still failed for
   the user because of attempt-7's discovery below.
7. 2026-04-21 — Checked what was actually running: **a zombie Python
   server (PID 36084) had been running since 2026-04-17** on port 8765
   with the pre-fix `server.py` and pre-fix CSS. Every `RUN.bat` the
   user had fired since then picked port **8766** (first free port after
   8765) and served correctly, but the user's browser was still bound to
   the zombie's session — the browser kept using cached assets from the
   zombie's port-8765 session and never requested from the new servers.
   The `Cache-Control: no-store` fix from attempt 5 only existed on the
   new servers, which the browser wasn't talking to. Killed PID 36084
   with `Stop-Process -Force`, confirmed port 8765 freed, relaunched
   `server.py` — verified over the wire that the new server returns
   `Cache-Control: no-store, must-revalidate` and CSS without
   `position: fixed` on `.keyhint`.
8. 2026-04-21 — To prevent this zombie scenario recurring: created
   `learnevo-help/kill-help-server.ps1` (stops any `python.exe` whose
   command line matches `*server.py*` or `*http.server*876*`), and made
   both `RUN.bat` and `learnevo-help/launch.bat` invoke it before
   starting `python server.py`. Also changed `launch.bat` to use
   `server.py` instead of the bare `python -m http.server 8765` (the
   bare module does not send `no-store`).

**Status:** fixed — verified on the wire that the running server returns
`Cache-Control: no-store, must-revalidate` and serves the flex-child
`.keyhint` CSS. Pending user's visual confirmation after one browser
reload pointed at the *current* server's port.

**Lessons:**
- When an overlay covers content, remove the overlay from `position: fixed`
  and put it in flow. Do not try to push content up with padding or
  spacers — that leaves the overlay on top of any scrollbar.
- When an edit "doesn't show up" in the browser, verify headers and force
  no-cache at the server before trying a third CSS fix.
- `Cache-Control: no-store` added to the server is **necessary but not
  sufficient** to flush a pre-existing Edge/Chromium heuristic cache
  entry. The browser won't hit the server at all while the cached entry
  is considered fresh. The reliable one-shot fix is a cache-busting query
  string (`?v=YYYYMMDDx`) on `<link>`/`<script>` URLs in the HTML. After
  one successful fetch with `no-store` headers, future edits come through
  on a plain reload without another version bump.
- I must not restrict read-only scope checks: this entire fix was inside
  `learnevo-help/`, which is under the LearnEVO playground — safe to edit.
