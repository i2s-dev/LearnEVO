# Shared Dialogs — Cross-Module Utility Programs

Status: partial | Pass 230 2026-06-23

These programs are not module-specific — they are called from multiple modules as
shared utility dialogs.

---

## T7RTMVALID.RWN — RTM Format Picker

Source: variable extraction from `samples/rwn_decrypted/T7RTMVALID.RWN.dec`

### Overview

`T7RTMVALID.RWN` is a **shared RTM (ReportBuilder report template) format picker dialog**.
It is NOT the RT module (Routings) — the name is `RTMVALID` = "RTM validator/selector".

- **Source library:** NZLICE.LIB
- **Variables:** 440 | **Instructions:** 585 | **Procs:** 20

### What It Does

When any reporting function needs to let the user choose a ReportBuilder template format,
it calls T7RTMVALID.RWN. The dialog presents available `.RTM` files and lets the user
select, save, or preview the format choice before running the report.

### Proc Names (confirmed)

| Proc | Purpose |
|------|---------|
| `SAVE.CLI` | Save button click handler |
| `GO.CLICK` | OK/Go button click — proceeds with selected format |
| `RTMNAME.` (×3) | RTM name field: three event handlers (Change / Click / DblClick) |
| `SHOWHELP` | Display help for current selection |
| `SHOWHLP` | Alternative help display (legacy) |
| `OLDHELP` | Legacy help handler |
| `DATE_VAL` | Date field validation |
| `NZ_GETS5` | NZLICE library: get 5-char string |
| `ALLTRIM` | NZLICE library: trim whitespace |
| `NZ_ENC` | NZLICE library: encode/encrypt |
| `NZ_DCR` | NZLICE library: decode/decrypt |

### Notes

- All 440 vars start as TEMP0–TEMP49 (library scratch block); module-specific vars follow.
- This program is the common entry point for "choose a report format" across all modules.
- The three `RTMNAME.*` proc variants handle combo-box events: on-change, single-click,
  and double-click on the RTM name selection list.
- `NZ_ENC`/`NZ_DCR` in the NZLICE library suggests RTM file paths or names may be stored
  in an obfuscated form in the BKSYMSTR or BKSYPRTR table.

**Confidence: 68/100** — Proc names and library confirmed; var content is dominated by
library block so module-specific fields are not yet extracted. Purpose as RTM picker is
inferred from name + proc patterns.

---

## See Also

- `docs/02-file-formats/rtm-report-templates.md` — RTM file format documentation
- `docs/03-modules/sm-system-manager/workstation-config.md` — Printer/format preferences
