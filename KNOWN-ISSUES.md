# KNOWN-ISSUES.md — EvoERP Known Issues

> **BUGS.md merged into this document 2026-07-06. Do not write to BUGS.md.**
> learnevo-help tool bugs are tracked here under "learnevo-help Tool Bugs (FIXED)" below.
> Individual issue files are in `Issues/BUG-NNN-*.md`.

Live production bugs and workarounds. Each entry has a unique ID (KI-NNN) for cross-referencing.
Newest entries on top within each status group.

**How to search this file:**
- By module: search `[WO-G]`, `[IN]`, `[AR]`, etc.
- By status: search `Status: ACTIVE`, `Status: WORKAROUND`, `Status: FIXED`
- By table: search the table name e.g. `WOBOM`, `BKICMSTR`
- By ID: search `KI-001` etc.
- Cross-references to BROKEN.md research entries are tagged `→ BROKEN.md B-NNN`

**How to add an entry:** Copy the template at the bottom of this file, assign the next KI-NNN
ID, fill in all fields, and prepend it under the appropriate status heading.

---

## Quick-Reference Index

| ID | Module | One-line summary | Status | Workaround? |
|----|--------|-----------------|--------|-------------|
| [KI-001](#ki-001) | WO-G | KIT=L freezes EVO when first mandatory BOM item is fully issued | ACTIVE | Yes — use KIT=Y |
| [BUG-001](#bug-001-glossary-stubs) | learnevo-help | Glossary see-also refs produced broken-link stubs | FIXED | n/a |
| [BUG-002](#bug-002-hint-bar-overlap) | learnevo-help | Hint bar overlapping sidebar + content | FIXED | n/a |

---

## Status: ACTIVE — No permanent fix yet

---

### KI-001

**Module:** WO-G (Issue Material) — `T7WOG.RWN` / `T7WOG4.RWN`
**Tags:** `[WO-G]` `WOBOM` `BKICMSTR` `KIT=L` `KIT=Y` `SMT` `freeze`
**Status:** ACTIVE — root cause confirmed, permanent fix requires EVO vendor or T7WOG4 decode
**Workaround:** ✅ Use **KIT=Y** instead of KIT=L — confirmed working 2026-07-01
**Reported:** 2026-06-29 | **Confirmed:** 2026-07-01
**Research ref:** → BROKEN.md B-018

#### Symptom

When an SMT associate enters a work order in WO-G (Issue Material), enters KIT=**L** (List),
and presses Enter, EvoERP freezes completely. No kit selection list appears. The associate
must force-kill EvoERP to recover. Affects SMT work orders only.

#### Affected work orders (confirmed)

| WO | Freeze trigger |
|----|---------------|
| 75338-2 | No mandatory (OPTION='N') WOBOM items — only OPTION='1' items |
| 75338-4 | No mandatory WOBOM items at all |
| 75405-3 | First mandatory item (055-03950-0) is fully issued (REMAINING=0) |
| 54552-1 | First mandatory item (055-53829-0M40K) is fully issued (REMAINING=0) |

#### Root cause (confirmed by 7/7 database correlation)

`WINPOS` in T7WOG reads the **first** mandatory WOBOM record sorted by `WOBOM_COMPCODE`
(Btrieve key order). It computes `REMAINING = WOBOM_TOTQTY − WOBOM_QTYISSUED` for that
one record and passes it to **T7WOG4** (the kit list display form — a separate program).

- If REMAINING = 0 → T7WOG4 freezes (bug inside T7WOG4)
- If no mandatory records exist → WINPOS terminates with "all processed" message

`WOBOM_OPTION` filtering happens at the Btrieve key level — never in TAS Pro code. WINPOS
contains zero loop instructions: it reads exactly one record.

#### Latent risk

Any SMT work order where the **alphabetically-first mandatory component** (WOBOM_OPTION='N',
sorted by COMPCODE) gets fully issued will freeze on the next KIT=L attempt — even if many
other components still need issuing. "055-*" part numbers sort first for most SMT WOs.

#### Workaround

Use **KIT=Y** (issue all) at the KIT= prompt instead of KIT=L (list). KIT=Y bypasses
T7WOG4 entirely and issues all remaining components directly. Confirmed working 2026-07-01.

#### Permanent fix options (not yet applied)

1. **Code fix (requires T7WOG4.RWN decode or EVO vendor):** Investigate how T7WOG4 handles
   REMAINING=0 input and fix the hang. T7WOG4.RWN is encrypted — needs IV from one Frida
   debugger session to decrypt.
2. **Data workaround per WO:** Reorder `WOBOM_SEQ` so an unissued item sorts first by
   Btrieve key, pushing the fully-issued item out of WINPOS's first-read position.
3. **BOM template fix:** For 75338-2, update WOBOM_OPTION from '1' → 'N' for the 21
   mandatory items (wrong option code at WO creation time).

---

## Status: WORKAROUND CONFIRMED — No permanent fix, but workaround is reliable

*(none yet — entries graduate here from ACTIVE once workaround is live-tested)*

---

## Status: FIXED

*(none yet)*

---

## learnevo-help Tool Bugs (FIXED)

These bugs were originally tracked in `BUGS.md` (now deprecated). Full details in `Issues/`.

---

### BUG-001 — Glossary stubs

**Module:** learnevo-help (`build.py`, `content/glossary.py`)
**Tags:** `glossary` `see_also` `broken-links` `stubs` `pid` `_resolve_ref`
**Status:** ✅ FIXED — 2026-04-21
**Full details:** [Issues/BUG-001-glossary-stubs.md](Issues/BUG-001-glossary-stubs.md)

11 stub pages appeared in the help browser because `_resolve_ref()` in `build.py` did not
canonicalize bare glossary terms (e.g. `"Btrieve"`), producing dangling `#Btrieve` anchors
instead of proper `glossary-btrieve` pids. Fixed by adding `_glossary_pid()` +
`_canonicalize()` helpers and threading them through both `_resolve_ref` and
`convert_wiki_links`. Stub count reduced from 104 → 88 (all 11 broken links eliminated).

---

### BUG-002 — Hint bar overlap

**Module:** learnevo-help (`css/style.css`, `server.py`, `RUN.bat`, `launch.bat`)
**Tags:** `CSS` `layout` `keyhint` `position-fixed` `flex` `cache` `Edge` `zombie-server` `Cache-Control`
**Status:** ✅ FIXED — 2026-04-21
**Full details:** [Issues/BUG-002-hint-bar-overlap.md](Issues/BUG-002-hint-bar-overlap.md)

The `.keyhint` bar was `position: fixed` and floated over both `#sidebar` and `#page`. Fixed
by making `.keyhint` a `flex-shrink: 0` static flex child of `<body>`. A zombie Python server
(PID 36084, running since 2026-04-17) masked the fix until killed. Prevention: added
`kill-help-server.ps1` and wired it into both `RUN.bat` and `launch.bat`. Cache-busted asset
URLs (`?v=20260421b`) + added `Cache-Control: no-store` to `server.py` to prevent recurrence.

---

## Entry Template

Copy this block, assign the next KI-NNN, fill in all fields:

```
### KI-NNN

**Module:** MODULE-CODE (Description) — `program.RWN`
**Tags:** `[MODULE]` `TABLE1` `TABLE2` `keyword`
**Status:** ACTIVE | WORKAROUND | FIXED
**Workaround:** ✅ description | ❌ None known
**Reported:** YYYY-MM-DD | **Confirmed:** YYYY-MM-DD
**Research ref:** → BROKEN.md B-NNN

#### Symptom

One paragraph: what the user sees, when it happens, who is affected.

#### Root cause

What causes it. Mark confirmed vs. inferred.

#### Workaround

Step-by-step. If none, say "None known."

#### Permanent fix options

Options for a real fix, even if not yet applied.
```
