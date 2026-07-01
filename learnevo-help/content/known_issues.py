"""
Known Issues for EvoERP — production bugs with confirmed workarounds.

Each entry is a tuple: (id, title, section, body_markdown, keywords).
Section is always "Known Issues" — build.py groups them under that nav heading.

To add a new issue:
  1. Copy the KI-001 block below.
  2. Assign the next KI-NNN id and update the title.
  3. Fill in all sections (Symptom, Affected, Root cause, Workaround, Fix options).
  4. Add relevant keywords.
  5. Run `python build.py` from the learnevo-help/ folder.

The canonical source of record is KNOWN-ISSUES.md at the repo root.
This file is the help-browser rendering of that document.
"""

KNOWN_ISSUES = [

# -----------------------------------------------------------------------
# KI-001 — WO-G KIT=L freeze
# -----------------------------------------------------------------------
("ki-001",
 "KI-001 — WO-G: KIT=L freezes EVO when first mandatory BOM item is fully issued",
 "Known Issues",
"""
**Status:** ACTIVE — root cause confirmed; permanent fix requires EVO vendor or T7WOG4 decode
**Workaround:** ✅ Use **KIT=Y** instead of KIT=L — confirmed working 2026-07-01
**Module:** [[module-WO|WO-G (Issue Material)]] — `T7WOG.RWN` / `T7WOG4.RWN`
**Research ref:** BROKEN.md B-018

---

## Symptom

When a user enters a work order in **WO-G (Issue Material)**, types **KIT=L** (List)
at the KIT prompt, and presses Enter, EvoERP **freezes completely** before the kit
selection list appears. No error message is shown. The user must force-kill EvoERP
to recover. Primarily affects SMT department work orders.

---

## Affected work orders (confirmed)

| Work Order | Why it freezes |
|------------|---------------|
| 75338-2 | No mandatory (OPTION='N') BOM items — mandatory items incorrectly coded as OPTION='1' |
| 75338-4 | No mandatory BOM items at all |
| 75405-3 | First mandatory item `055-03950-0` is fully issued (zero remaining) |
| 54552-1 | First mandatory item `055-53829-0M40K` is fully issued (zero remaining) |

---

## Root cause

`WINPOS` (a procedure inside `T7WOG.RWN`) reads the **first** mandatory [[WOBOM]] record
sorted by `WOBOM_COMPCODE` (Btrieve key order). It computes:

```
REMAINING = WOBOM_TOTQTY − WOBOM_QTYISSUED
```

for that **one record only**, then launches **T7WOG4** (a separate kit-list display
program) passing REMAINING as a parameter.

- If **REMAINING = 0** → T7WOG4 freezes (bug inside T7WOG4, not yet decoded)
- If **no mandatory records exist** → WINPOS terminates with an "all processed" message (form closes silently)

The `WOBOM_OPTION='N'` filter is applied at the Btrieve key level — never in TAS Pro code.
WINPOS reads exactly one record; it contains zero loop instructions.

---

## Latent risk

Any work order where the **alphabetically-first mandatory component**
(`WOBOM_OPTION='N'`, sorted by `WOBOM_COMPCODE`) becomes fully issued will freeze on
the next KIT=L attempt — even if many other components still need issuing. Part numbers
starting with `055-*` sort first for most SMT work orders, so this typically triggers
as soon as the first SMT component is kitted.

---

## Workaround ✅ CONFIRMED

Use **KIT=Y** (issue all) at the KIT= prompt instead of KIT=L (list).

- KIT=Y bypasses T7WOG4 entirely and issues all remaining components directly.
- Confirmed working on WO 54552-1 (2026-07-01).
- Safe for all affected work orders listed above.

---

## Permanent fix options (not yet applied)

1. **Code fix** — Requires decrypting `T7WOG4.RWN` (needs one Frida debugger session
   to recover the encryption IV) or contacting the EVO vendor. The fix is inside T7WOG4,
   not T7WOG.

2. **Per-WO data workaround** — Reorder `WOBOM_SEQ` so an unissued item sorts first
   by Btrieve key, pushing the fully-issued item out of WINPOS's first-read position.
   Requires write access to the WOBOM table.

3. **BOM template fix (WO 75338-2 only)** — Update `WOBOM_OPTION` from `'1'` → `'N'`
   for the 21 mandatory items. These were coded with the wrong option value at WO
   creation time.
""",
["freeze", "kit", "kit=l", "kit=y", "wobom", "wog", "issue material",
 "smt", "remaining", "winpos", "t7wog", "t7wog4", "workaround",
 "75338", "75405", "54552", "mandatory", "option", "compcode",
 "frozen", "hang", "locks up", "known issue"]),

# -----------------------------------------------------------------------
# Add new issues above this line — newest on top
# -----------------------------------------------------------------------

]
