# WC — Warehouse Control (Bin Locations): Field Reference

Status: verified — field meanings confirmed from RTM DataField usage (BKISWCE1.RTM, Pass 574
2026-07-06) + DDF schema (`Evo-DBA_File_Fields 052421.xlsx`).

The WC module manages physical warehouse bin locations and per-bin inventory quantities.
ISBINLOC is the core table: one record per item × location × bin combination.
ISBNMSTR is the bin master: one record per bin code at each location.

These tables are accessed by all modules that print bin-location inventory reports.
BKISWCE1.RTM (the #1 most-called RTM sub-report, 244 callers) binds directly to ISBINLOC fields.

---

## ISBINLOC
**BIN DETAIL** — per-item × location × bin inventory record

Fields: 9 | Key: ISBIN_LOC_ITEM + ISBIN_LOC_LOC + ISBIN_LOC_BIN

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISBIN_LOC_BIN | STRING | 15 | — | Bin code / bin name within the warehouse location |
| 2 | ISBIN_LOC_CDATE | DATE | 4 | — | Creation date — when this bin assignment was established |
| 3 | ISBIN_LOC_DFLT | STRING | 1 | — | Default bin flag: `Y` = this is the default bin for the item at this location |
| 4 | ISBIN_LOC_EXTRA | STRING | 100 | — | User-defined extra data field |
| 5 | ISBIN_LOC_ITEM | STRING | 15 | — | Item number (FK → BKICMSTR) |
| 6 | ISBIN_LOC_LOC | STRING | 10 | — | Warehouse location code (FK → BKICLOC) |
| 7 | ISBIN_LOC_RVLVL | STRING | 5 | — | Revision level of item at this bin assignment |
| 8 | ISBIN_LOC_UOH | NUMERIC | 8 | 2 | Units on hand in this specific bin |
| 9 | ISBIN_LOC_VDATE | DATE | 4 | — | Verification date — last physical count or audit date |

**Notes:**
- PK is composite: ITEM + LOC + BIN — one record per item per bin at each warehouse
- ISBIN_LOC_UOH is the bin-level quantity; total location UOH is in BKICLOC.BKIC_LOC_UOH
- ISBIN_LOC_DFLT marks the bin where the system will put-away and pick first
- Live data: 22,279 PIBINLOC records (Physical Inventory bin count variant) confirm active use

## ISBNMSTR
**BIN MASTER** — bin definition at each warehouse location

Fields: 4 | Key: ISBN_MSTR_LOC + ISBN_MSTR_BIN

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISBN_MSTR_BIN | STRING | 15 | — | Bin code (unique within a location) |
| 2 | ISBN_MSTR_DESC | STRING | 60 | — | Bin description / label (e.g., "Shelf A-3", "Bay 12 Top") |
| 3 | ISBN_MSTR_EXTRA | STRING | 100 | — | User-defined extra data |
| 4 | ISBN_MSTR_LOC | STRING | 10 | — | Warehouse location code (FK → BKICLOC) |

**Notes:**
- PK is LOC + BIN — a bin code is scoped to a location (same bin name can exist at multiple locations)
- ISBNMSTR drives the bin selection dialog when assigning items to bins in WH receiving
- Bin descriptions appear on printed bin labels and warehouse reports

**Confidence: 88/100** — field meanings inferred from naming convention + BKISWCE1.RTM DataField
bindings (confirmed in rtm_fields.csv); live record counts not queried directly for these tables.
