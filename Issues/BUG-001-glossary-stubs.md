# BUG-001: Glossary see-also refs producing broken-link stubs

**Status:** ✅ FIXED
**Date:** 2026-04-21
**Keywords:** learnevo-help, glossary, see_also, broken links, stubs, build.py, _resolve_ref, convert_wiki_links, pid

## Symptom

11 stub pages appeared in the help browser (`Btrieve`, `CFB`, `DCY`, `DDF`, `DFM`, `FIFO`,
`Pervasive`, `RTM`, `Twofish`, `EvoHELP.CHM`, `tp7runtime.exe`) — auto-generated because
something linked to them, but the real content already existed under `glossary-<slug>` IDs.
Users saw "This topic is referenced but not yet fully written" on click.

## Root Cause

- In `learnevo-help/build.py`, glossary entries' `see_also` lists pass each reference through
  `_resolve_ref()`, which only recognized table names and menu-code patterns. A bare term like
  `"Btrieve"` fell through unchanged and rendered as `[Btrieve](#Btrieve)` — a dangling link.
- Similarly, `convert_wiki_links()` (for `[[Term]]` in bodies) didn't canonicalize bare
  glossary terms either.
- Two binary-filename references (`EvoHELP.CHM`, `tp7runtime.exe`) had no glossary entries
  at all — so canonicalizing alone wouldn't fix them.

## Attempts

1. **2026-04-21** — Added `_glossary_pid(term)` + `_canonicalize(pid)` helpers to
   `learnevo-help/build.py`. Threaded `_canonicalize` through both `convert_wiki_links` and
   `_resolve_ref`. Added new glossary entries for `EvoHELP.CHM` and `tp7runtime.exe` in
   `learnevo-help/content/glossary.py`. Rebuild: stub count 104 → 90.
   **Partial result** — two new stubs appeared (`glossary-reportbuilder`,
   `glossary-tas-professional-tas-pro-7`).

2. **2026-04-21** — First new stub: `[[glossary-reportbuilder]]` was written in `format-rtm`,
   but the actual glossary pid is `glossary-nevrona-reportbuilder`. Changed to
   `[[Nevrona ReportBuilder|ReportBuilder]]` so the canonicalizer resolves it through the
   standard term lookup. **Worked.**

3. **2026-04-21** — Second new stub: `_glossary_pid` had `.strip('-')` on the slug, but the
   original pid-generation at line 356 of build.py does NOT strip. So
   `"TAS Professional (TAS Pro 7)"` produced `glossary-tas-professional-tas-pro-7-` (trailing
   dash) in one place and `glossary-tas-professional-tas-pro-7` in the other — divergence.
   Removed `.strip('-')` so both paths agree byte-for-byte. **Worked.**

   Final stub count: 104 → 88. All 11 broken links gone.

## Resolution / Lesson

**Fixed.** When adding a new pid-generating helper, mirror the existing generator's exact
string transform (no extra `.strip()`, no case-folding differences). A one-character
divergence produces silent stub creation that only shows up via rebuild comparison.
