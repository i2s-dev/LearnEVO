# ODBC DDF null-indicator misalignment (I2 database)

Status: verified 2026-10-12 (WORKORD, WOBOM, ISNUMBER decoded against raw files).

## Symptom

Through `DSN=DBA` on i2s-evo, some tables return garbage: WO numbers like `2.36e+189`, "Invalid date, time or
timestamp value", "Numeric value out of range". WHERE filters on those tables silently match nothing
(e.g. `WORKORD WHERE MTWO_WIP_WOPRE=55968` → 0 rows although the record exists).

## Cause

For affected tables, the I2 data dictionary (`X$Field`) defines every column with a **1-byte null indicator**
in front of it (Zen "true null" layout). TAS/EVO records have no null bytes, so every field after the first
is read from the wrong position.

Example — WORKORD (`X$Field` offsets vs actual):

| Field | DDF offset | Actual offset |
|-------|-----------|---------------|
| MTWO_WIP_WOPRE (DOUBLE 8) | 1 | 0 |
| MTWO_WIP_WOSUF (USMALLINT 2) | 10 | 8 |
| MTWO_WIP_BLANK | 13 | 10 |
| MTWO_WIP_SQTY | 17 | 12 |
| MTWO_WIP_SSTART (DATE 4) | 28 | 21 |
| MTWO_WIP_STATUS | 57 | 45 |

**Rule:** `actual_offset = Xe$Offset − (field_index + 1)`, with fields ordered by `Xe$Offset` and
`Xe$DataType < 227` (skips index-only pseudo-fields). Check: DDF end − field count = file's logical record length
(header offset 0x16). WORKORD: 1256 − 83 = 1173. WOBOM: 535 − 39 = 496 ✔.

| Table | DDF OK? | Notes |
|-------|---------|-------|
| WOMAT | ✔ | Queries work normally |
| WORKORD | ✘ | 83 fields, reclen 1173 |
| WOBOM | ✘ | 39 fields, reclen 496 |
| ISNUMBER | ✘ | |
| BKICMSTR | ✔ (earlier scripts work) | |

Dates decode as TAS/Btrieve DATE: `day, month, year(uint16 LE)`.

## Workaround

Read the `.BI2` file directly: copy it to `samples/`, find records by packing the key (e.g. `struct.pack('<dH', pre, suf)`
for WOPRE+WOSUF), and decode with the corrected offsets. Working script: the inline decoder used in
[KI-003](../../Issues/KI-003-wo-a-material-issues-empty-file.md), which pulls the field list from `X$Field`.

Note: `programs/wo-schedule/main.py` treats `MTWO_WIP_WOPRE` as a string (`.strip()`); against today's DDF it would
get a float. Likely broken against i2s-evo — retest.

## Table → file mapping

In `DSN=DBA`, plain table names map to company **I2** files (`X$File.Xf$Loc`): `WORKORD → WORKORD.BI2`,
`WOMAT → WOMAT.BI2`, `WOBOM → WOBOM.BI2`, `BKICMSTR → BKICMSTR.BI2`, `ISNUMBER → ISNUMBER.BI2`.
The root `\\i2s-evo\EVOERP\FILE.DDF` (2024-09-29) is a different multi-company dictionary with `_B99/_BAB/_BI2`
suffixed names; it is **not** the one DSN=DBA uses.
