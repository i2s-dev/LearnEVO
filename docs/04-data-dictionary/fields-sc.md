# SC — Serial Control: Field Reference

Status: verified-schema + completed field meanings (Pass 574, 2026-07-06).

Source: `Evo-DBA_File_Fields 052421.xlsx`, sheet "Fields". Original Excel descriptions
present for SERIAL/SERIALH; remaining fields inferred from naming.

The SC module tracks individual serialized items through inventory from receipt to shipment.
At i2 Systems, serial control is minimally used: SERIAL=11 and SERIALH=11 records confirmed
from live ODBC (Pass 422, 2026-06-30).

Four tables: SERIAL (active), SERIALH (archive), ISSERCNT (auto-generation config), ISHSERIA (genealogy).

---

## SERIAL
**SERIAL NUMBER MASTER** — one record per serialized unit in inventory

Fields: 30 | Key: MTSER_CODE + MTSER_SERIAL + MTSER_LOC

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTSER_BIN | STRING | 15 | — | Bin location of this serial unit |
| 2 | MTSER_CODE | STRING | 15 | — | Item code (FK → BKICMSTR) |
| 3 | MTSER_CUSTCODE | STRING | 10 | — | Customer code — sold-to customer (FK → BKARCUST) |
| 4 | MTSER_EXPDATE | DATE | 4 | — | Expiration date |
| 5 | MTSER_EXTRA | STRING | 50 | — | User-defined extra data |
| 6 | MTSER_INRECCOST | NUMERIC | 8 | 4 | Initial receipt unit cost |
| 7 | MTSER_INRECDATE | DATE | 4 | — | Initial receipt date (first time this serial entered inventory) |
| 8 | MTSER_INV | NUMERIC | 8 | — | AR invoice number where this serial was shipped |
| 9 | MTSER_ISSCOST | NUMERIC | 8 | 4 | Issue/shipment cost |
| 10 | MTSER_ISSDATE | DATE | 4 | — | Issue/shipment date |
| 11 | MTSER_LOC | STRING | 10 | — | Warehouse location code |
| 12 | MTSER_LOT | STRING | 15 | — | Associated lot number (for lot+serial tracked items) |
| 13 | MTSER_NOTES_1 | STRING | 30 | — | Notes line 1 |
| 14 | MTSER_NOTES_2 | STRING | 30 | — | Notes line 2 |
| 15 | MTSER_NOTES_3 | STRING | 30 | — | Notes line 3 |
| 16 | MTSER_NOTES_4 | STRING | 30 | — | Notes line 4 |
| 17 | MTSER_NOTES_5 | STRING | 30 | — | Notes line 5 |
| 18 | MTSER_ONHAND | NUMERIC | 8 | 2 | On-hand status: 1 = in inventory, 0 = issued/shipped |
| 19 | MTSER_PO | NUMERIC | 8 | — | PO number that received this serial |
| 20 | MTSER_POCOST | NUMERIC | 8 | 4 | PO receipt unit cost |
| 21 | MTSER_RECDATE | DATE | 4 | — | Most recent receipt date |
| 22 | MTSER_RECDOC | NUMERIC | 8 | — | Receiving document number |
| 23 | MTSER_SELLPRICE | NUMERIC | 8 | 4 | Sell price when shipped |
| 24 | MTSER_SERIAL | STRING | 25 | — | Serial number (note: Excel has typo "Serail Number") |
| 25 | MTSER_SHIPDATE | DATE | 4 | — | Ship date |
| 26 | MTSER_SO | NUMERIC | 8 | — | Sales order number that consumed this serial |
| 27 | MTSER_VENDOR | STRING | 10 | — | Vendor code (FK → BKAPVEND) |
| 28 | MTSER_WO | NUMERIC | 8 | — | Work order prefix (if manufactured) |
| 29 | MTSER_WOCODE | STRING | 15 | — | WO item/product code (item built by WO) |
| 30 | MTSER_WOSUF | INTEGER | 2 | — | Work order suffix |

## SERIALH
**ARCHIVED SERIAL NUMBERS** — identical 30-field schema; records moved here after shipment

Fields: 30 | Key: MTSER_CODE + MTSER_SERIAL (archive copy of SERIAL)

Identical schema to SERIAL — see above for all field meanings. Records are archived here
when a serial unit is fully shipped and invoiced. SERIAL=11 / SERIALH=11 live records at i2 Systems.

## ISSERCNT
**SERIAL NUMBER GENERATION MASTER** — auto-increment serial number configuration

Fields: 9 | Key: IS_SERC_ITEM

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_SERC_CLASS | STRING | 4 | — | Class code (groups serial numbering by product class) |
| 2 | IS_SERC_EXTRA | STRING | 100 | — | User-defined extra data |
| 3 | IS_SERC_ITEM | STRING | 15 | — | Item code this counter applies to (FK → BKICMSTR) |
| 4 | IS_SERC_L2 | INTEGER | 2 | — | Length of secondary/prefix portion of serial format |
| 5 | IS_SERC_LAST | STRING | 25 | — | Last serial number generated (full string, not just numeric part) |
| 6 | IS_SERC_LENG | STRING | 2 | — | Length of the auto-increment numeric portion |
| 7 | IS_SERC_NUMBER | NUMERIC | 8 | — | Last sequential number used (counter incremented on each generation) |
| 8 | IS_SERC_SPOS | INTEGER | 2 | — | Start position of the numeric portion within the serial string |
| 9 | IS_SERC_TOTAL | INTEGER | 2 | — | Total length of the generated serial number |

**Notes:** ISSERCNT defines a format mask (position, length) for auto-generating serial numbers
from a counter. The actual generated value is stored in MTSER_SERIAL of the SERIAL table.

## ISHSERIA
**ARCHIVED SERIAL** — serialized assembly genealogy (same schema as ISHLOTS)

Fields: 11 | Key: IS_SER_PARENT + IS_SER_COMP + IS_SER_CSERIAL

Tracks which component serial numbers were used in which parent assembly serials.
Same IS_SER_* prefix and schema as ISHLOTS (lot genealogy equivalent).

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_SER_ADATE | DATE | 4 | — | Assembly date |
| 2 | IS_SER_CDESC | STRING | 30 | — | Component item description |
| 3 | IS_SER_COMP | STRING | 15 | — | Component item code |
| 4 | IS_SER_CSERIAL | STRING | 25 | — | Component serial number used in assembly |
| 5 | IS_SER_EXRA | STRING | 100 | — | Extra data (DDF typo: EXRA not EXTRA) |
| 6 | IS_SER_FDATE | DATE | 4 | — | Assembly finish date |
| 7 | IS_SER_PARENT | STRING | 15 | — | Parent assembly item code |
| 8 | IS_SER_PDESC | STRING | 30 | — | Parent assembly description |
| 9 | IS_SER_PSERIAL | STRING | 25 | — | Parent assembly serial number |
| 10 | IS_SER_WOPRE | NUMERIC | 8 | — | Work order prefix |
| 11 | IS_SER_WOSUF | INTEGER | 2 | — | Work order suffix |

**Confidence: 88/100** — SERIAL/SERIALH partial descriptions from Excel confirmed;
remaining fields clear from naming + lot-control parallel; ISSERCNT format-mask
semantics inferred from auto-serial-number generation context.
