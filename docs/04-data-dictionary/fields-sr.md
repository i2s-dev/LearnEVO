# SR — Service and Repair: Field Reference

Status: verified-schema — SR-specific tables documented with field meanings (Pass 574, 2026-07-06).

Source: `Evo-DBA_File_Fields 052421.xlsx`, sheet "Fields".

The SR module processes service and repair orders using the AR invoice infrastructure.
SR invoices are stored in the BKAR* tables (same as regular AR invoices) with a type flag
distinguishing SR from standard SO invoices. The SR-specific tables below handle SR-only
audit history and SR-extended data.

The core SR module tables are: ISARSCGH (change audit), plus shared BKARINV/BKARINVL
(invoices/lines — see fields-ar.md), BKARCUST (customer — see fields-ar.md).

---

## ISARSCGH
**CHANGES TO S/R** — Service/Repair order change audit log (before/after pairs)

Fields: 26 | Key: ISAR_CHG_SONUM + ISAR_CHG_INVNUM + ISAR_CHG_LINEID + ISAR_CHG_UNUM

This table records edits to SR order lines using the same A*(after)/B*(before) pattern
as WORKCHG (WO change audit). Each row captures one field-level change: original value
in B* fields, new value in A* fields. The CDATE/USER/INVNUM/LINEID identify what changed and when.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISAR_CHG_AASD | DATE | 4 | — | **After** Actual Ship Date |
| 2 | ISAR_CHG_ACOMPR_1 | NUMERIC | 8 | 4 | **After** Compression/compression rate 1 (pricing multiplier or competitive-price compression, first tier) |
| 3 | ISAR_CHG_ACOMPR_2 | NUMERIC | 8 | 4 | **After** Compression rate 2 (second pricing tier) |
| 4 | ISAR_CHG_ADISC | NUMERIC | 8 | 2 | **After** Discount percentage |
| 5 | ISAR_CHG_AESD | DATE | 4 | — | **After** Estimated Ship Date |
| 6 | ISAR_CHG_AEXTRA | STRING | 150 | — | **After** Extra/user-defined data field |
| 7 | ISAR_CHG_ALOC | STRING | 10 | — | **After** Warehouse location code |
| 8 | ISAR_CHG_AOOQTY | NUMERIC | 8 | 2 | **After** Open Order Quantity (remaining unfulfilled qty) |
| 9 | ISAR_CHG_APRICE | NUMERIC | 8 | 4 | **After** Unit price |
| 10 | ISAR_CHG_BASD | DATE | 4 | — | **Before** Actual Ship Date |
| 11 | ISAR_CHG_BCOMPR_1 | NUMERIC | 8 | 4 | **Before** Compression rate 1 |
| 12 | ISAR_CHG_BCOMPR_2 | NUMERIC | 8 | 4 | **Before** Compression rate 2 |
| 13 | ISAR_CHG_BDISC | NUMERIC | 8 | 2 | **Before** Discount percentage |
| 14 | ISAR_CHG_BESD | DATE | 4 | — | **Before** Estimated Ship Date |
| 15 | ISAR_CHG_BEXTRA | STRING | 150 | — | **Before** Extra/user-defined data |
| 16 | ISAR_CHG_BLOC | STRING | 10 | — | **Before** Warehouse location code |
| 17 | ISAR_CHG_BOOQTY | NUMERIC | 8 | 2 | **Before** Open Order Quantity |
| 18 | ISAR_CHG_BPRICE | NUMERIC | 8 | 4 | **Before** Unit price |
| 19 | ISAR_CHG_CDATE | DATE | 4 | — | Change date — when this edit was made |
| 20 | ISAR_CHG_INVNUM | NUMERIC | 8 | — | SR invoice/order number (FK → BKARINV) |
| 21 | ISAR_CHG_LINEID | NUMERIC | 8 | — | Line item ID within the SR order |
| 22 | ISAR_CHG_PCODE | STRING | 15 | — | Part/product code (item number on the changed line) |
| 23 | ISAR_CHG_REVLVL | STRING | 10 | — | Revision level of the item at time of change |
| 24 | ISAR_CHG_SONUM | NUMERIC | 8 | — | Sales Order number (parent SO if SR was created from an SO) |
| 25 | ISAR_CHG_UNUM | INTEGER | 4 | — | Unique record number / sequence within the change log |
| 26 | ISAR_CHG_USER | STRING | 15 | — | User ID who made the change |

**A\* / B\* field pattern:**  
Each changed field has an A\* (after = new value) and B\* (before = original value) counterpart.
Fields tracked: ship dates (ASD/ESD), pricing (PRICE/DISC/COMPR), location, open-order-qty, extra.
Fields NOT tracked per-row (they identify the change): CDATE, INVNUM, LINEID, PCODE, SONUM, USER.

**Confidence: 82/100** — field meanings from naming convention + A/B audit pattern confirmed
from WORKCHG parallel structure; ACOMPR_1/2 semantics inferred (compression = price compression
in SR customer negotiation context — unverified without RWN decryption).
