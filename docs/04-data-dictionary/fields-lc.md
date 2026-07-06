# LC — Lot Control: Field Reference

Status: verified-schema + inferred meanings (Pass 574, 2026-07-06).

Source: `Evo-DBA_File_Fields 052421.xlsx`, sheet "Fields".

The LC module tracks inventory by lot number — useful for FIFO costing, expiration dates,
and traceability in FDA/ISO environments. Three tables: LOT (lot master), ISBINLOT (bin-level
lot quantities), ISHLOTS (archived lot genealogy / assembly tracing).

At i2 Systems, lot control is minimally used: `LOT=11` and `SERIAL=11` records confirmed from
live ODBC query (Pass 422, 2026-06-30).

---

## LOT
**LOT CONTROL DETAIL** — lot master record

Fields: 25 | Key: MTLOT_CODE + MTLOT_LOT + MTLOT_LOC

One record per item × lot number × location. Tracks quantity, cost source, expiration,
and receiving document for each lot.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTLOT_BEGIN | NUMERIC | 8 | 7 | Beginning quantity when lot was created |
| 2 | MTLOT_CODE | STRING | 15 | — | Item code (FK → BKICMSTR) |
| 3 | MTLOT_EXPDATE | DATE | 4 | — | Expiration date (for perishables / FDA-tracked items) |
| 4 | MTLOT_EXTRA | STRING | 50 | — | User-defined extra data |
| 5 | MTLOT_INRECDATE | DATE | 4 | — | Initial receipt date (when lot first came into inventory) |
| 6 | MTLOT_LOC | STRING | 10 | — | Warehouse location code |
| 7 | MTLOT_LOT | STRING | 15 | — | Lot number (user-assigned or auto-generated) |
| 8 | MTLOT_MAXOUT | NUMERIC | 8 | 7 | Maximum allowed outgoing quantity per transaction |
| 9 | MTLOT_NOTES_1 | STRING | 45 | — | Notes line 1 |
| 10 | MTLOT_NOTES_2 | STRING | 45 | — | Notes line 2 |
| 11 | MTLOT_NOTES_3 | STRING | 45 | — | Notes line 3 |
| 12 | MTLOT_NOTES_4 | STRING | 45 | — | Notes line 4 |
| 13 | MTLOT_NOTES_5 | STRING | 45 | — | Notes line 5 |
| 14 | MTLOT_ONHAND | NUMERIC | 8 | 2 | Current on-hand quantity for this lot |
| 15 | MTLOT_OUT | NUMERIC | 8 | 7 | Total quantity issued/shipped from this lot |
| 16 | MTLOT_PO | NUMERIC | 8 | — | Purchase order number associated with this lot receipt |
| 17 | MTLOT_POCOST | NUMERIC | 8 | 4 | Unit cost from the PO receipt |
| 18 | MTLOT_RECDATE | DATE | 4 | — | Most recent receipt date |
| 19 | MTLOT_RECDOC | NUMERIC | 8 | — | Receiving document number (PO receipt or WO completion) |
| 20 | MTLOT_RECQTY | NUMERIC | 8 | 2 | Quantity received in the most recent receipt |
| 21 | MTLOT_VENDOR | STRING | 10 | — | Vendor code for this lot (FK → BKAPVEND) |
| 22 | MTLOT_WO | NUMERIC | 8 | — | Work order number if lot originated from WO completion |
| 23 | MTLOT_WOCOST | NUMERIC | 8 | 4 | Unit cost from the WO completion |
| 24 | MTLOT_WOQTY | NUMERIC | 8 | 2 | Quantity completed from WO that created this lot |
| 25 | MTLOT_WOSUF | INTEGER | 2 | — | WO suffix (for multi-suffix work orders) |

**Notes:**
- PO and WO source fields are mutually exclusive: a lot comes from either a PO receipt
  or a WO completion, not both.
- MTLOT_NOTES_1..5: 5 lines × 45 chars = 225 chars total per lot.

## ISBINLOT
**LOT/BIN DETAIL** — bin-level lot quantity

Fields: 11 | Key: IS_BINLOT_ITEM + IS_BINLOT_LOC + IS_BINLOT_LOT + IS_BINLOT_BIN

Sub-level below LOT: tracks how lot quantity is distributed across bins within a location.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_BINLOT_BIN | STRING | 15 | — | Bin code within the location |
| 2 | IS_BINLOT_DATE | DATE | 4 | — | Date this bin-lot assignment was created/updated |
| 3 | IS_BINLOT_DFLT | STRING | 1 | — | Default bin flag: `Y` = preferred bin for this lot |
| 4 | IS_BINLOT_EXTRA | STRING | 50 | — | User-defined extra data |
| 5 | IS_BINLOT_FLAG | STRING | 1 | — | Status flag (active/inactive/hold) |
| 6 | IS_BINLOT_ITEM | STRING | 15 | — | Item code (FK → BKICMSTR) |
| 7 | IS_BINLOT_LOC | STRING | 10 | — | Warehouse location code |
| 8 | IS_BINLOT_LOT | STRING | 15 | — | Lot number (FK → LOT) |
| 9 | IS_BINLOT_TMPPO | STRING | 40 | — | Temporary PO reference (staging field during lot receiving) |
| 10 | IS_BINLOT_TMPSO | STRING | 40 | — | Temporary SO reference (staging field during lot picking) |
| 11 | IS_BINLOT_UOH | NUMERIC | 8 | 2 | Units on hand in this specific bin × lot combination |

## ISHLOTS
**ARCHIVED LOTS** — assembly genealogy / lot-to-serial traceability archive

Fields: 11 | Key: IS_SER_PARENT + IS_SER_COMP + IS_SER_CSERIAL

Tracks the parent→child relationship for serialized assemblies that include lot-tracked
components. Uses IS_SER_* prefix (same as ISSERIAL — shared schema family).
Note: field 5 has a confirmed typo in DDF: `IS_SER_EXRA` (not EXTRA) — matches ISSERIAL.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_SER_ADATE | DATE | 4 | — | Assembly date |
| 2 | IS_SER_CDESC | STRING | 30 | — | Component item description |
| 3 | IS_SER_COMP | STRING | 15 | — | Component item code |
| 4 | IS_SER_CSERIAL | STRING | 25 | — | Component lot/serial number |
| 5 | IS_SER_EXRA | STRING | 100 | — | Extra data (DDF typo: EXRA not EXTRA — see B-017 pattern) |
| 6 | IS_SER_FDATE | DATE | 4 | — | Finish/completion date |
| 7 | IS_SER_PARENT | STRING | 15 | — | Parent assembly item code |
| 8 | IS_SER_PDESC | STRING | 30 | — | Parent assembly description |
| 9 | IS_SER_PSERIAL | STRING | 25 | — | Parent serial/lot number |
| 10 | IS_SER_WOPRE | NUMERIC | 8 | — | Work order prefix |
| 11 | IS_SER_WOSUF | INTEGER | 2 | — | Work order suffix |

**Confidence: 85/100** — LOT/ISBINLOT field meanings clear from naming; ISHLOTS IS_SER_*
prefix confirmed from ISSERIAL parallel; MTLOT_MAXOUT and IS_BINLOT_FLAG exact values
require RWN decryption.
