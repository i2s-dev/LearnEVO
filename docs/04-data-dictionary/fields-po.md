# PO — Purchase Orders: Field Reference

Status: verified-schema + completed field meanings (Pass 574k-5, 2026-07-06).

Source: `Evo-DBA_File_Fields 052421.xlsx`, sheet "Fields".

Identical-schema notes:
- BKAP_PO_* header (58f): BKAPAPO, BKAPHPO, BKAPPO, BKAPRFQ, ISAPARFQ, ISAPOPO all share same schema.
- BKAP_POL_* lines (38f): BKAPAPOL, BKAPHPOL, BKAPPOL, BKAPRFQL, ISAPARFL, ISAPOPOL all share same schema.
- BKRFQ_* vendor pricing (49f): BKAPQUOT, BKRFQ, ISAPHQT, ISAPQTQT, ISARFQ all share same schema.
- BKPOX_* (19f): BKPOX and BKPOXH are identical.
- BKQC_* QC receipt (14f): BKQCMSTR and ISQCAMST are identical.
- BKQC_TRN_* QC transaction (21f): BKQCTRAN and ISQCATRN are identical.
- BKMRP_PO_* (16f): BKSOPO and BKWOPO are identical.
- BK_DESC_* notes (5f): BKAPHDSC, BKRFQDES, ISRFQADS are identical — all already described.

---

## BKAPAPO
**ARCHIVED PO HEADER**

Fields: 58 | Key: BKAP_PO_NUM

Identical 58-field schema to BKAPHPO / BKAPPO / BKAPRFQ / ISAPARFQ / ISAPOPO (BKAP_PO_* prefix).
Records archived here on PO close/delete.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAP_PO_CONFIRM_1 | STRING | 1 | — | PO confirmation flag 1 (buyer acknowledgment; `Y`=confirmed) |
| 2 | BKAP_PO_CONFIRM_2 | STRING | 1 | — | PO confirmation flag 2 (vendor acknowledgment; `Y`=vendor confirmed) |
| 3 | BKAP_PO_DESC | STRING | 30 | — | PO Description |
| 4 | BKAP_PO_EMPNUM | INTEGER | 2 | — | Employee number of the buyer/purchaser who entered this PO |
| 5 | BKAP_PO_ENDLNE | STRING | 1 | — | Ending Lines Y/N |
| 6 | BKAP_PO_ENTBY | STRING | 2 | — | PO Entered By |
| 7 | BKAP_PO_EXTRA | STRING | 150 | — | Extra |
| 8 | BKAP_PO_FOB | STRING | 20 | — | Ship FOB |
| 9 | BKAP_PO_FTERMD | STRING | 10 | — | Freight Terms Description |
| 10 | BKAP_PO_FTERMNM | INTEGER | 2 | — | Freight Terms Number |
| 11 | BKAP_PO_GLDPT | STRING | 4 | — | GL Department |
| 12 | BKAP_PO_INVNUM | STRING | 10 | — | not used |
| 13 | BKAP_PO_ISBROKE | STRING | 10 | — | Broker Code |
| 14 | BKAP_PO_ISCUR | STRING | 3 | — | Currency |
| 15 | BKAP_PO_ISMCDT | DATE | 4 | — | Multi-Currency Date |
| 16 | BKAP_PO_ISREV | STRING | 1 | — | Rev - only called in POB |
| 17 | BKAP_PO_ISRVDT | DATE | 4 | — | Rev Date - only called in POB |
| 18 | BKAP_PO_ISTXGR | STRING | 10 | — | Tax Group |
| 19 | BKAP_PO_ITOTAL | NUMERIC | 8 | 2 | Invoiced Total |
| 20 | BKAP_PO_LOC | STRING | 10 | — | Location |
| 21 | BKAP_PO_LONGPO | STRING | 25 | — | not used |
| 22 | BKAP_PO_NL | INTEGER | 2 | — | Number of Lines |
| 23 | BKAP_PO_NUM | NUMERIC | 8 | — | PO Number |
| 24 | BKAP_PO_OBYCUS | STRING | 15 | — | Job Number |
| 25 | BKAP_PO_ORDDTE | DATE | 4 | — | Order Date |
| 26 | BKAP_PO_PCKSLP | STRING | 15 | — | Packing slip number associated with this PO |
| 27 | BKAP_PO_PRTD | STRING | 1 | — | Printed   Y/P/R |
| 28 | BKAP_PO_QCTOTAL | NUMERIC | 8 | 2 | QC Total |
| 29 | BKAP_PO_RECNUM | NUMERIC | 8 | — | not used |
| 30 | BKAP_PO_RNI^ | NUMERIC | 8 | 2 | Received-Not-Invoiced amount (computed: value received but not yet invoiced) |
| 31 | BKAP_PO_SHPA1 | STRING | 30 | — | Ship Loc Address Line 1 |
| 32 | BKAP_PO_SHPA2 | STRING | 30 | — | Ship Loc Address Line 2 |
| 33 | BKAP_PO_SHPA3 | STRING | 30 | — | Ship Loc. Address Line 3 |
| 34 | BKAP_PO_SHPATN | STRING | 30 | — | Ship Attention |
| 35 | BKAP_PO_SHPCNT | STRING | 30 | — | Ship Country |
| 36 | BKAP_PO_SHPCOD | STRING | 10 | — | Ship To Loc Code |
| 37 | BKAP_PO_SHPCTY | STRING | 26 | — | Ship Loc City |
| 38 | BKAP_PO_SHPNME | STRING | 30 | — | Ship Loc Name |
| 39 | BKAP_PO_SHPST | STRING | 2 | — | Ship loc State |
| 40 | BKAP_PO_SHPVIA | STRING | 15 | — | Ship VIA |
| 41 | BKAP_PO_SHPZIP | STRING | 10 | — | Ship Loc ZIP Code |
| 42 | BKAP_PO_SUBTOT | NUMERIC | 8 | 2 | Sub Total |
| 43 | BKAP_PO_TAXABLE | STRING | 1 | — | Taxable Y/N |
| 44 | BKAP_PO_TAXAMT | NUMERIC | 8 | 2 | Tax Amount |
| 45 | BKAP_PO_TAXRTE | NUMERIC | 8 | 3 | Tax Rate |
| 46 | BKAP_PO_TERMD | STRING | 10 | — | Terms Description |
| 47 | BKAP_PO_TERMNM | INTEGER | 2 | — | Terms Number |
| 48 | BKAP_PO_TOTAL | NUMERIC | 8 | 2 | Total |
| 49 | BKAP_PO_VNDA1 | STRING | 30 | — | Vendor Address Line 1 |
| 50 | BKAP_PO_VNDA2 | STRING | 30 | — | Vendor Address Line 2 |
| 51 | BKAP_PO_VNDA3 | STRING | 30 | — | Vendor Address 3 |
| 52 | BKAP_PO_VNDATN | STRING | 30 | — | Vendor Attention |
| 53 | BKAP_PO_VNDCNT | STRING | 30 | — | Vendor Country |
| 54 | BKAP_PO_VNDCOD | STRING | 10 | — | Vendor Code |
| 55 | BKAP_PO_VNDCTY | STRING | 26 | — | Vendor City |
| 56 | BKAP_PO_VNDNME | STRING | 30 | — | Vendor Name |
| 57 | BKAP_PO_VNDST | STRING | 2 | — | Vendor State |
| 58 | BKAP_PO_VNDZIP | STRING | 10 | — | Vendor ZIP Code |

## BKAPAPOL
**ARCHIVED PO LINES**

Fields: 38 | Key: BKAP_POL_PONM + BKAP_POL_CNTR

Identical 38-field schema to BKAPHPOL / BKAPPOL / BKAPRFQL / ISAPARFL / ISAPOPOL (BKAP_POL_* prefix).
Records archived here on PO close.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAP_POL_ARD | DATE | 4 | — | Actual Receipt Date |
| 2 | BKAP_POL_BUYOFF | NUMERIC | 8 | 2 | Quantity Buy-Off  From QC |
| 3 | BKAP_POL_CNTR | INTEGER | 2 | — | Line Number |
| 4 | BKAP_POL_ERD | DATE | 4 | — | Estimated Receipt Date |
| 5 | BKAP_POL_EST | NUMERIC | 8 | — | Estimated Receipt Date |
| 6 | BKAP_POL_EXTRA | STRING | 100 | — | Extra |
| 7 | BKAP_POL_GLA | STRING | 10 | — | GL Account Number |
| 8 | BKAP_POL_GLDPTA | STRING | 4 | — | GL Department |
| 9 | BKAP_POL_INVDTE | DATE | 4 | — | Invoice date for this line item |
| 10 | BKAP_POL_INVNUM | STRING | 10 | — | not used |
| 11 | BKAP_POL_IQTY | NUMERIC | 8 | 2 | Invoiced Quantity |
| 12 | BKAP_POL_ITM_NO | STRING | 9 | — | Item Number |
| 13 | BKAP_POL_ITYPE | STRING | 1 | — | not used |
| 14 | BKAP_POL_LOC | STRING | 10 | — | Location |
| 15 | BKAP_POL_OO_QTY | NUMERIC | 8 | 2 | Quantity On Order (remaining) |
| 16 | BKAP_POL_OPER | INTEGER | 2 | — | WO Operation number |
| 17 | BKAP_POL_PARENT | STRING | 15 | — | called from POA, POB |
| 18 | BKAP_POL_PCODE | STRING | 15 | — | Part Code |
| 19 | BKAP_POL_PCOGS | NUMERIC | 8 | 2 | COGS |
| 20 | BKAP_POL_PCONV | NUMERIC | 8 | 5 | PO unit conversion factor (purchase UOM → stock UOM multiplier) |
| 21 | BKAP_POL_PDESC | STRING | 30 | — | Description |
| 22 | BKAP_POL_PDISC | NUMERIC | 8 | 2 | Discount |
| 23 | BKAP_POL_PEXT | NUMERIC | 8 | 2 | Extended  Total |
| 24 | BKAP_POL_PKSQTY | NUMERIC | 8 | 2 | Pack size quantity (standard pack size for this line item) |
| 25 | BKAP_POL_PONM | NUMERIC | 8 | — | PO Number |
| 26 | BKAP_POL_PPRCE | NUMERIC | 8 | 4 | Price |
| 27 | BKAP_POL_PQTY | NUMERIC | 8 | 2 | Quantity Ordered |
| 28 | BKAP_POL_PRTDIM | STRING | 1 | — | called from POA, POB |
| 29 | BKAP_POL_PSTDTE | DATE | 4 | — | Vendor's promised ship/delivery date for this line |
| 30 | BKAP_POL_QC_QTY | NUMERIC | 8 | 2 | QC Quantity |
| 31 | BKAP_POL_RECNUM | NUMERIC | 8 | — | not used |
| 32 | BKAP_POL_RQTY | NUMERIC | 8 | 2 | Received Quantity |
| 33 | BKAP_POL_SCRAP | NUMERIC | 8 | 2 | Quantity Scraped |
| 34 | BKAP_POL_TXBLE | STRING | 1 | — | Taxable Y/N |
| 35 | BKAP_POL_WOPRE | NUMERIC | 8 | — | Work Order Prefix |
| 36 | BKAP_POL_WOSUF | INTEGER | 2 | — | Work Order Suffix |
| 37 | NKAP_POL_UM_LIN_1 | STRING | 3 | — | Unit of measure line 1 (stock UOM; note: NKAP prefix is a source typo for BKAP) |
| 38 | NKAP_POL_UM_LIN_2 | STRING | 3 | — | Unit of measure line 2 (purchase UOM; note: NKAP prefix is a source typo for BKAP) |

## BKAPHDSC
**PO RECEIVER NOTES**

Fields: 5 | Key: BK_DESC_NUM + BK_DESC_LINE

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BK_DESC_CODE | STRING | 15 | — | not used |
| 2 | BK_DESC_DESC | STRING | 25 | — | not used |
| 3 | BK_DESC_LINE | INTEGER | 2 | — | Notes line number |
| 4 | BK_DESC_NOTES | STRING | 70 | — | Notes - text |
| 5 | BK_DESC_NUM | NUMERIC | 8 | — | PO Number |

## BKAPHPO
**PO RECEIVER HEADER**

Fields: 58 | Key: BKAP_PO_NUM

Identical schema to BKAPAPO above. See that table for all field definitions.

## BKAPHPOL
**PO RECEIVER LINES**

Fields: 38 | Key: BKAP_POL_PONM + BKAP_POL_CNTR

Identical schema to BKAPAPOL above. See that table for all field definitions.

## BKAPPO
**OPEN PO HEADER**

Fields: 58 | Key: BKAP_PO_NUM

Identical schema to BKAPAPO above. See that table for all field definitions.

## BKAPPOL
**OPEN PO LINES**

Fields: 38 | Key: BKAP_POL_PONM + BKAP_POL_CNTR

Identical schema to BKAPAPOL above. See that table for all field definitions.

## BKAPQUOT
**VENDOR PRICING**

Fields: 49 | Key: BKRFQ_VEND + BKRFQ_PROD

Identical 49-field schema to BKRFQ / ISAPHQT / ISAPQTQT / ISARFQ (BKRFQ_* prefix). See BKRFQ below for all field definitions.

## BKAPRFQ
**RFQ HEADER**

Fields: 58 | Key: BKAP_PO_NUM

Identical schema to BKAPAPO above. See that table for all field definitions.

## BKAPRFQL
**RFQ LINES**

Fields: 38 | Key: BKAP_POL_PONM + BKAP_POL_CNTR

Identical schema to BKAPAPOL above. See that table for all field definitions.

## BKPOX
**PO DETAIL — ACCOUNTING DISABLED**

Fields: 19 | Key: BKPOX_PONUM + BKPOX_INVCNUM

Identical 19-field schema to BKPOXH (BKPOX_* prefix). Staging table for AP invoice entry when PO
accounting is disabled. See BKPOXH below for all field definitions.

## BKPOXH
**PO DETAIL — ACCOUNTING DISABLED (HISTORY)**

Fields: 19 | Key: BKPOX_PONUM + BKPOX_INVCNUM

AP invoice staging when PO accounting is disabled. One record per AP invoice matched to a PO.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKPOX_ARCHDATE | DATE | 4 | — | Archive date (when record was archived) |
| 2 | BKPOX_COMPANY | STRING | 2 | — | Company code |
| 3 | BKPOX_CURRENCY | STRING | 3 | — | Currency code |
| 4 | BKPOX_ENTDATE | DATE | 4 | — | Entry date (invoice entry date) |
| 5 | BKPOX_FREIGHT | NUMERIC | 8 | 2 | Freight amount on this invoice |
| 6 | BKPOX_INVCDATE | DATE | 4 | — | Invoice date |
| 7 | BKPOX_INVCDESC | STRING | 30 | — | Invoice description |
| 8 | BKPOX_INVCNUM | STRING | 10 | — | Invoice number (FK → BKAP invoice) |
| 9 | BKPOX_PONUM | NUMERIC | 8 | — | PO number (FK → BKAPPO) |
| 10 | BKPOX_POSTDATE | DATE | 4 | — | GL post date |
| 11 | BKPOX_SUBTOT | NUMERIC | 8 | 2 | Subtotal (before tax/freight) |
| 12 | BKPOX_TAXAMT | NUMERIC | 8 | 2 | Tax amount |
| 13 | BKPOX_TAXCODE | STRING | 10 | — | Tax code |
| 14 | BKPOX_TAXNAME | STRING | 30 | — | Tax name |
| 15 | BKPOX_TERMSCODE | INTEGER | 2 | — | Payment terms code |
| 16 | BKPOX_TERMSDESC | STRING | 20 | — | Payment terms description |
| 17 | BKPOX_TOTAL | NUMERIC | 8 | 2 | Total invoice amount |
| 18 | BKPOX_VENDCODE | STRING | 10 | — | Vendor code (FK → BKAPVEND) |
| 19 | BKPOX_VENDNAME | STRING | 30 | — | Vendor name |

## BKQCMSTR
**QUALITY CONTROL MASTER**

Fields: 14 | Key: BKQC_PO_NUM + BKQC_POL_ITM_NO

Identical 14-field schema to ISQCAMST (BKQC_* prefix). See ISQCAMST below for all field definitions.

## BKQCTRAN
**QUALITY CONTROL TRANSACTION**

Fields: 21 | Key: BKQC_TRN_PO + BKQC_TRN_RECNUM

Identical 21-field schema to ISQCATRN (BKQC_TRN_* prefix). See ISQCATRN below for all field definitions.

## BKRFQ
**VERBAL FOR QUOTES (RFQ LINE / VENDOR PRICING)**

Fields: 49 | Key: BKRFQ_VEND + BKRFQ_PROD

Vendor pricing / RFQ response — one record per vendor per part with up to 10 quantity break
price tiers. Identical schema to BKAPQUOT / ISAPHQT / ISAPQTQT / ISARFQ.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKRFQ_ALPHA1 | STRING | 15 | — | User-defined alpha field |
| 2 | BKRFQ_COST_1 | NUMERIC | 8 | 4 | Quote/bid cost for quantity tier 1 |
| 3 | BKRFQ_COST_10 | NUMERIC | 8 | 4 | Quote/bid cost for quantity tier 10 |
| 4 | BKRFQ_COST_2 | NUMERIC | 8 | 4 | Quote/bid cost for quantity tier 2 |
| 5 | BKRFQ_COST_3 | NUMERIC | 8 | 4 | Quote/bid cost for quantity tier 3 |
| 6 | BKRFQ_COST_4 | NUMERIC | 8 | 4 | Quote/bid cost for quantity tier 4 |
| 7 | BKRFQ_COST_5 | NUMERIC | 8 | 4 | Quote/bid cost for quantity tier 5 |
| 8 | BKRFQ_COST_6 | NUMERIC | 8 | 4 | Quote/bid cost for quantity tier 6 |
| 9 | BKRFQ_COST_7 | NUMERIC | 8 | 4 | Quote/bid cost for quantity tier 7 |
| 10 | BKRFQ_COST_8 | NUMERIC | 8 | 4 | Quote/bid cost for quantity tier 8 |
| 11 | BKRFQ_COST_9 | NUMERIC | 8 | 4 | Quote/bid cost for quantity tier 9 |
| 12 | BKRFQ_CQCHANGE | STRING | 1 | — | Cost quote changed flag (`Y`=quote has been revised) |
| 13 | BKRFQ_CWHO | STRING | 15 | — | User who last revised the cost quote |
| 14 | BKRFQ_EST | NUMERIC | 8 | — | Estimate Number |
| 15 | BKRFQ_EST_LINE | NUMERIC | 8 | — | Estimate line number (FK → estimating module) |
| 16 | BKRFQ_EXP | DATE | 4 | — | Expiration Date |
| 17 | BKRFQ_EXTRA | STRING | 50 | — | Extra |
| 18 | BKRFQ_FLAG | STRING | 1 | — | Status flag |
| 19 | BKRFQ_GDATE | DATE | 4 | — | Good-through date (quote valid through this date) |
| 20 | BKRFQ_ISSUE | DATE | 4 | — | Issue Date |
| 21 | BKRFQ_LCDATE | DATE | 4 | — | Last changed date |
| 22 | BKRFQ_LEAD | INTEGER | 2 | — | Lead Time |
| 23 | BKRFQ_MAXDAYS | INTEGER | 2 | — | Maximum delivery days (upper bound for lead time) |
| 24 | BKRFQ_MIN | NUMERIC | 8 | 2 | Minimum |
| 25 | BKRFQ_MINCST | NUMERIC | 8 | 2 | Minimum Cost |
| 26 | BKRFQ_NUM | NUMERIC | 8 | — | Quote/RFQ Number |
| 27 | BKRFQ_OPER | INTEGER | 2 | — | WO Operation Number |
| 28 | BKRFQ_PARENT | STRING | 15 | — | Parent part Number |
| 29 | BKRFQ_PARNTDESC | STRING | 30 | — | Parent Part Description |
| 30 | BKRFQ_PCONV | NUMERIC | 8 | 4 | PO unit conversion factor (purchase UOM → stock UOM multiplier) |
| 31 | BKRFQ_PROD | STRING | 15 | — | Part Code |
| 32 | BKRFQ_PRODDESC | STRING | 30 | — | Part Description |
| 33 | BKRFQ_PUM | STRING | 3 | — | Unit of Measure |
| 34 | BKRFQ_QTY_1 | NUMERIC | 8 | 2 | Quantity break point 1 (minimum qty for tier 1 pricing) |
| 35 | BKRFQ_QTY_10 | NUMERIC | 8 | 2 | Quantity break point 10 |
| 36 | BKRFQ_QTY_2 | NUMERIC | 8 | 2 | Quantity break point 2 |
| 37 | BKRFQ_QTY_3 | NUMERIC | 8 | 2 | Quantity break point 3 |
| 38 | BKRFQ_QTY_4 | NUMERIC | 8 | 2 | Quantity break point 4 |
| 39 | BKRFQ_QTY_5 | NUMERIC | 8 | 2 | Quantity break point 5 |
| 40 | BKRFQ_QTY_6 | NUMERIC | 8 | 2 | Quantity break point 6 |
| 41 | BKRFQ_QTY_7 | NUMERIC | 8 | 2 | Quantity break point 7 |
| 42 | BKRFQ_QTY_8 | NUMERIC | 8 | 2 | Quantity break point 8 |
| 43 | BKRFQ_QTY_9 | NUMERIC | 8 | 2 | Quantity break point 9 |
| 44 | BKRFQ_USE | STRING | 1 | — | Use this quote flag (`Y`=select this vendor's quote for the PO) |
| 45 | BKRFQ_UWHO | STRING | 15 | — | User who set the USE flag |
| 46 | BKRFQ_VEND | STRING | 10 | — | Vendor Code |
| 47 | BKRFQ_VENDNAME | STRING | 25 | — | Vendor Name |
| 48 | BKRFQ_WOPRE | NUMERIC | 8 | — | WO Prefix |
| 49 | BKRFQ_WOSUF | INTEGER | 2 | — | WO Suffix |

## BKRFQDES
**RFQ NOTES**

Fields: 5 | Key: BK_DESC_NUM + BK_DESC_LINE

Identical schema to BKAPHDSC above. See that table for all field definitions.

## BKSOPO
**TEMP FILE FOR CONVERT SO TO PO**

Fields: 16 | Key: BKMRP_PO_PART + BKMRP_PO_VEND

Identical 16-field schema to BKWOPO (BKMRP_PO_* prefix). See BKWOPO below for all field definitions.

## BKWOPO
**TEMP FILE FOR CONVERT WO TO PO**

Fields: 16 | Key: BKMRP_PO_PART + BKMRP_PO_VEND

Temporary staging table used by MRP/SO/WO-to-PO conversion to collect suggested purchase orders.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKMRP_PO_CONF | STRING | 1 | — | Confirmed/accepted flag (`Y`=approved for PO creation) |
| 2 | BKMRP_PO_DATE | DATE | 4 | — | Required receipt date |
| 3 | BKMRP_PO_DONE | STRING | 10 | — | Processed/done status (batch processing marker) |
| 4 | BKMRP_PO_ERD | DATE | 4 | — | Estimated receipt date |
| 5 | BKMRP_PO_EST | STRING | 10 | — | Estimate number (source estimate for this suggested PO) |
| 6 | BKMRP_PO_ESTLNE | NUMERIC | 8 | — | Estimate line number |
| 7 | BKMRP_PO_EXTRA | STRING | 50 | — | Extra data |
| 8 | BKMRP_PO_MTREC | INTEGER | 4 | — | MRP record ID (internal MRP requirement record reference) |
| 9 | BKMRP_PO_PART | STRING | 15 | — | Part number to be purchased (FK → BKICMSTR) |
| 10 | BKMRP_PO_PLANR | STRING | 4 | — | Planner code (purchaser/buyer responsible for this item) |
| 11 | BKMRP_PO_PRICE | NUMERIC | 8 | 4 | Suggested unit price |
| 12 | BKMRP_PO_QTY | NUMERIC | 8 | 2 | Quantity to order |
| 13 | BKMRP_PO_UID | STRING | 20 | — | Unique session/batch ID (groups records from same planning run) |
| 14 | BKMRP_PO_VEND | STRING | 10 | — | Vendor code (FK → BKAPVEND) |
| 15 | BKMRP_PO_WOPRE | NUMERIC | 8 | — | Work order prefix (source WO for subcontract) |
| 16 | BKMRP_PO_WOSUF | INTEGER | 2 | — | Work order suffix |

## ISAPARFL
**ARCHIVED RFQ LINE**

Fields: 38 | Key: BKAP_POL_PONM + BKAP_POL_CNTR

Identical schema to BKAPAPOL above. See that table for all field definitions.

## ISAPARFQ
**ARCHIVED RFQ HEADER**

Fields: 58 | Key: BKAP_PO_NUM

Identical schema to BKAPAPO above. See that table for all field definitions.

## ISAPCHG
**CHANGES TO PURCHASE ORDERS**

Fields: 32 | Key: ISAP_CHG_PONUM + ISAP_CHG_LINEID + ISAP_CHG_CDATE

Records before (B prefix) and after (A prefix) values for each PO line change.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISAP_CHG_AARD | DATE | 4 | — | After: actual receipt date |
| 2 | ISAP_CHG_ACONV | NUMERIC | 8 | 5 | After: unit conversion factor |
| 3 | ISAP_CHG_ADISC | NUMERIC | 8 | 2 | After: discount |
| 4 | ISAP_CHG_AERD | DATE | 4 | — | After: estimated receipt date |
| 5 | ISAP_CHG_AEXTRA | STRING | 150 | — | After: extra data |
| 6 | ISAP_CHG_AGLA | STRING | 10 | — | After: GL account |
| 7 | ISAP_CHG_AGLD | STRING | 4 | — | After: GL department |
| 8 | ISAP_CHG_ALOC | STRING | 10 | — | After: warehouse location |
| 9 | ISAP_CHG_AOOQTY | NUMERIC | 8 | 2 | After: on-order quantity |
| 10 | ISAP_CHG_AOPER | INTEGER | 2 | — | After: WO operation number |
| 11 | ISAP_CHG_APRICE | NUMERIC | 8 | 4 | After: unit price |
| 12 | ISAP_CHG_AWOP | NUMERIC | 8 | — | After: WO prefix |
| 13 | ISAP_CHG_AWOS | INTEGER | 2 | — | After: WO suffix |
| 14 | ISAP_CHG_BARD | DATE | 4 | — | Before: actual receipt date |
| 15 | ISAP_CHG_BCONV | NUMERIC | 8 | 5 | Before: unit conversion factor |
| 16 | ISAP_CHG_BDISC | NUMERIC | 8 | 2 | Before: discount |
| 17 | ISAP_CHG_BERD | DATE | 4 | — | Before: estimated receipt date |
| 18 | ISAP_CHG_BEXTRA | STRING | 150 | — | Before: extra data |
| 19 | ISAP_CHG_BGLA | STRING | 10 | — | Before: GL account |
| 20 | ISAP_CHG_BGLD | STRING | 4 | — | Before: GL department |
| 21 | ISAP_CHG_BLOC | STRING | 10 | — | Before: warehouse location |
| 22 | ISAP_CHG_BOOQTY | NUMERIC | 8 | 2 | Before: on-order quantity |
| 23 | ISAP_CHG_BOPER | INTEGER | 2 | — | Before: WO operation number |
| 24 | ISAP_CHG_BPRICE | NUMERIC | 8 | 4 | Before: unit price |
| 25 | ISAP_CHG_BWOP | NUMERIC | 8 | — | Before: WO prefix |
| 26 | ISAP_CHG_BWOS | INTEGER | 2 | — | Before: WO suffix |
| 27 | ISAP_CHG_CDATE | DATE | 4 | — | Change date (when this change was made) |
| 28 | ISAP_CHG_LINEID | INTEGER | 2 | — | PO line number changed (FK → BKAPPOL.BKAP_POL_CNTR) |
| 29 | ISAP_CHG_PCODE | STRING | 15 | — | Part code on the changed PO line |
| 30 | ISAP_CHG_PONUM | NUMERIC | 8 | — | PO number (FK → BKAPPO) |
| 31 | ISAP_CHG_REVLVL | STRING | 10 | — | Revision level / change order number |
| 32 | ISAP_CHG_USER | STRING | 15 | — | User who made the change |

## ISAPHQT
**ARCHIVE VENDOR PRICING**

Fields: 49 | Key: BKRFQ_VEND + BKRFQ_PROD

Identical schema to BKRFQ above. See that table for all field definitions.

## ISAPOPO
**ARCHIVED OPEN PO**

Fields: 58 | Key: BKAP_PO_NUM

Identical schema to BKAPAPO above. See that table for all field definitions.

## ISAPOPOL
**ARCHIVED OPEN PO LINES**

Fields: 38 | Key: BKAP_POL_PONM + BKAP_POL_CNTR

Identical schema to BKAPAPOL above. See that table for all field definitions.

## ISAPQTQT
**ARCHIVED VENDOR PRICING**

Fields: 49 | Key: BKRFQ_VEND + BKRFQ_PROD

Identical schema to BKRFQ above. See that table for all field definitions.

## ISARFQ
**ARCHIVE RFQ**

Fields: 49 | Key: BKRFQ_VEND + BKRFQ_PROD

Identical schema to BKRFQ above. See that table for all field definitions.

## ISDIGSIG
**PO DIGITAL SIGNATURE**

Fields: 89 | Key: ISAP_CHG_PONUM (likely)

10-slot multi-approver digital signature workflow. Each slot N (1–10) tracks one approver's
authorization (active flag, approval amount limit, signature date, from/through date window, type).

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_DSIG_ACTIVE_1 | STRING | 1 | — | Approver 1 active flag (`Y`=this slot is assigned to an approver) |
| 2 | IS_DSIG_ACTIVE_10 | STRING | 1 | — | Approver 10 active flag |
| 3 | IS_DSIG_ACTIVE_2 | STRING | 1 | — | Approver 2 active flag |
| 4 | IS_DSIG_ACTIVE_3 | STRING | 1 | — | Approver 3 active flag |
| 5 | IS_DSIG_ACTIVE_4 | STRING | 1 | — | Approver 4 active flag |
| 6 | IS_DSIG_ACTIVE_5 | STRING | 1 | — | Approver 5 active flag |
| 7 | IS_DSIG_ACTIVE_6 | STRING | 1 | — | Approver 6 active flag |
| 8 | IS_DSIG_ACTIVE_7 | STRING | 1 | — | Approver 7 active flag |
| 9 | IS_DSIG_ACTIVE_8 | STRING | 1 | — | Approver 8 active flag |
| 10 | IS_DSIG_ACTIVE_9 | STRING | 1 | — | Approver 9 active flag |
| 11 | IS_DSIG_ADATE | DATE | 4 | — | Most recent approval date (last approver to sign) |
| 12 | IS_DSIG_AMT_1 | NUMERIC | 8 | 2 | Approval amount limit for approver 1 (max PO value this approver can authorize) |
| 13 | IS_DSIG_AMT_10 | NUMERIC | 8 | 2 | Approval amount limit for approver 10 |
| 14 | IS_DSIG_AMT_2 | NUMERIC | 8 | 2 | Approval amount limit for approver 2 |
| 15 | IS_DSIG_AMT_3 | NUMERIC | 8 | 2 | Approval amount limit for approver 3 |
| 16 | IS_DSIG_AMT_4 | NUMERIC | 8 | 2 | Approval amount limit for approver 4 |
| 17 | IS_DSIG_AMT_5 | NUMERIC | 8 | 2 | Approval amount limit for approver 5 |
| 18 | IS_DSIG_AMT_6 | NUMERIC | 8 | 2 | Approval amount limit for approver 6 |
| 19 | IS_DSIG_AMT_7 | NUMERIC | 8 | 2 | Approval amount limit for approver 7 |
| 20 | IS_DSIG_AMT_8 | NUMERIC | 8 | 2 | Approval amount limit for approver 8 |
| 21 | IS_DSIG_AMT_9 | NUMERIC | 8 | 2 | Approval amount limit for approver 9 |
| 22 | IS_DSIG_ATIME | TIME | 4 | — | Most recent approval time |
| 23 | IS_DSIG_DATE_1 | DATE | 4 | — | Date approver 1 signed/approved |
| 24 | IS_DSIG_DATE_10 | DATE | 4 | — | Date approver 10 signed/approved |
| 25 | IS_DSIG_DATE_2 | DATE | 4 | — | Date approver 2 signed/approved |
| 26 | IS_DSIG_DATE_3 | DATE | 4 | — | Date approver 3 signed/approved |
| 27 | IS_DSIG_DATE_4 | DATE | 4 | — | Date approver 4 signed/approved |
| 28 | IS_DSIG_DATE_5 | DATE | 4 | — | Date approver 5 signed/approved |
| 29 | IS_DSIG_DATE_6 | DATE | 4 | — | Date approver 6 signed/approved |
| 30 | IS_DSIG_DATE_7 | DATE | 4 | — | Date approver 7 signed/approved |
| 31 | IS_DSIG_DATE_8 | DATE | 4 | — | Date approver 8 signed/approved |
| 32 | IS_DSIG_DATE_9 | DATE | 4 | — | Date approver 9 signed/approved |
| 33 | IS_DSIG_EMP | INTEGER | 2 | — | Employee number of PO creator (entered-by reference) |
| 34 | IS_DSIG_EXTRA | STRING | 100 | — | Extra data |
| 35 | IS_DSIG_FDATE_1 | DATE | 4 | — | From date for approver 1 (start of this approver's authorization window) |
| 36 | IS_DSIG_FDATE_10 | DATE | 4 | — | From date for approver 10 |
| 37 | IS_DSIG_FDATE_2 | DATE | 4 | — | From date for approver 2 |
| 38 | IS_DSIG_FDATE_3 | DATE | 4 | — | From date for approver 3 |
| 39 | IS_DSIG_FDATE_4 | DATE | 4 | — | From date for approver 4 |
| 40 | IS_DSIG_FDATE_5 | DATE | 4 | — | From date for approver 5 |
| 41 | IS_DSIG_FDATE_6 | DATE | 4 | — | From date for approver 6 |
| 42 | IS_DSIG_FDATE_7 | DATE | 4 | — | From date for approver 7 |
| 43 | IS_DSIG_FDATE_8 | DATE | 4 | — | From date for approver 8 |
| 44 | IS_DSIG_FDATE_9 | DATE | 4 | — | From date for approver 9 |
| 45 | IS_DSIG_FILE | STRING | 256 | — | Digital signature file path (path to stored electronic signature image/data) |
| 46 | IS_DSIG_FLAG_1 | STRING | 1 | — | Approval flag for approver 1 (`Y`=approved, `N`=rejected) |
| 47 | IS_DSIG_FLAG_10 | STRING | 1 | — | Approval flag for approver 10 |
| 48 | IS_DSIG_FLAG_2 | STRING | 1 | — | Approval flag for approver 2 |
| 49 | IS_DSIG_FLAG_3 | STRING | 1 | — | Approval flag for approver 3 |
| 50 | IS_DSIG_FLAG_4 | STRING | 1 | — | Approval flag for approver 4 |
| 51 | IS_DSIG_FLAG_5 | STRING | 1 | — | Approval flag for approver 5 |
| 52 | IS_DSIG_FLAG_6 | STRING | 1 | — | Approval flag for approver 6 |
| 53 | IS_DSIG_FLAG_7 | STRING | 1 | — | Approval flag for approver 7 |
| 54 | IS_DSIG_FLAG_8 | STRING | 1 | — | Approval flag for approver 8 |
| 55 | IS_DSIG_FLAG_9 | STRING | 1 | — | Approval flag for approver 9 |
| 56 | IS_DSIG_MOTCACH | STRING | 16 | — | MOT cache (method-of-transfer hash/token used for signature validation) |
| 57 | IS_DSIG_POAMT | NUMERIC | 8 | 2 | PO total amount at time of approval |
| 58 | IS_DSIG_POENTBY | STRING | 2 | — | PO entered-by user code (2-char) |
| 59 | IS_DSIG_SDATE_1 | DATE | 4 | — | Signature date for approver 1 (date electronic signature was captured) |
| 60 | IS_DSIG_SDATE_10 | DATE | 4 | — | Signature date for approver 10 |
| 61 | IS_DSIG_SDATE_2 | DATE | 4 | — | Signature date for approver 2 |
| 62 | IS_DSIG_SDATE_3 | DATE | 4 | — | Signature date for approver 3 |
| 63 | IS_DSIG_SDATE_4 | DATE | 4 | — | Signature date for approver 4 |
| 64 | IS_DSIG_SDATE_5 | DATE | 4 | — | Signature date for approver 5 |
| 65 | IS_DSIG_SDATE_6 | DATE | 4 | — | Signature date for approver 6 |
| 66 | IS_DSIG_SDATE_7 | DATE | 4 | — | Signature date for approver 7 |
| 67 | IS_DSIG_SDATE_8 | DATE | 4 | — | Signature date for approver 8 |
| 68 | IS_DSIG_SDATE_9 | DATE | 4 | — | Signature date for approver 9 |
| 69 | IS_DSIG_SOENTBY | STRING | 5 | — | SO entered-by user code (5-char; legacy/overflow field) |
| 70 | IS_DSIG_TDATE_1 | DATE | 4 | — | Through date for approver 1 (end of this approver's authorization window) |
| 71 | IS_DSIG_TDATE_10 | DATE | 4 | — | Through date for approver 10 |
| 72 | IS_DSIG_TDATE_2 | DATE | 4 | — | Through date for approver 2 |
| 73 | IS_DSIG_TDATE_3 | DATE | 4 | — | Through date for approver 3 |
| 74 | IS_DSIG_TDATE_4 | DATE | 4 | — | Through date for approver 4 |
| 75 | IS_DSIG_TDATE_5 | DATE | 4 | — | Through date for approver 5 |
| 76 | IS_DSIG_TDATE_6 | DATE | 4 | — | Through date for approver 6 |
| 77 | IS_DSIG_TDATE_7 | DATE | 4 | — | Through date for approver 7 |
| 78 | IS_DSIG_TDATE_8 | DATE | 4 | — | Through date for approver 8 |
| 79 | IS_DSIG_TDATE_9 | DATE | 4 | — | Through date for approver 9 |
| 80 | IS_DSIG_TYPE_1 | STRING | 10 | — | Approval type code for approver 1 (role/authority type) |
| 81 | IS_DSIG_TYPE_10 | STRING | 10 | — | Approval type code for approver 10 |
| 82 | IS_DSIG_TYPE_2 | STRING | 10 | — | Approval type code for approver 2 |
| 83 | IS_DSIG_TYPE_3 | STRING | 10 | — | Approval type code for approver 3 |
| 84 | IS_DSIG_TYPE_4 | STRING | 10 | — | Approval type code for approver 4 |
| 85 | IS_DSIG_TYPE_5 | STRING | 10 | — | Approval type code for approver 5 |
| 86 | IS_DSIG_TYPE_6 | STRING | 10 | — | Approval type code for approver 6 |
| 87 | IS_DSIG_TYPE_7 | STRING | 10 | — | Approval type code for approver 7 |
| 88 | IS_DSIG_TYPE_8 | STRING | 10 | — | Approval type code for approver 8 |
| 89 | IS_DSIG_TYPE_9 | STRING | 10 | — | Approval type code for approver 9 |

## ISPODESC
**PURCHASE ORDER DESCRIPTION LIST**

Fields: 1 | Key: IORD_DESC_CODE

Master list of predefined PO description entries for description pick-lists.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IORD_DESC_CODE | STRING | 30 | — | PO description code / predefined description text (PK) |

## ISQCAMST
**ARCHIVED QC RECEIPTS**

Fields: 14 | Key: BKQC_PO_NUM + BKQC_POL_ITM_NO

Identical schema to BKQCMSTR. See below for all field definitions.

## ISQCATRN
**ARCHIVED QC BUYOFF**

Fields: 21 | Key: BKQC_TRN_PO + BKQC_TRN_RECNUM

Identical schema to BKQCTRAN. See below for all field definitions.

---

*QC tables documented here in their active form; archive tables (ISQCAMST/ISQCATRN) use same schemas.*

## BKQCMSTR — full field list

**QC RECEIPT MASTER**

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKQC_EXTRA | STRING | 25 | — | Extra data |
| 2 | BKQC_OUT_DATE | DATE | 4 | — | QC release / out date (date items were released from QC hold) |
| 3 | BKQC_PKSLIP_NUM | STRING | 15 | — | Packing slip number |
| 4 | BKQC_PKSLIP_QTY | NUMERIC | 8 | 2 | Packing slip quantity (qty shown on vendor's packing slip) |
| 5 | BKQC_PO_NUM | NUMERIC | 8 | — | PO number (FK → BKAPPO) |
| 6 | BKQC_POL_ITM_NO | STRING | 10 | — | PO line item number (FK → BKAPPOL) |
| 7 | BKQC_PROD_CODE | STRING | 15 | — | Part/product code (FK → BKICMSTR) |
| 8 | BKQC_QTY_BUYOFF | NUMERIC | 8 | 2 | Quantity accepted / bought off from QC hold |
| 9 | BKQC_QTY_RECVD | NUMERIC | 8 | 2 | Total quantity received into QC |
| 10 | BKQC_QTY_REJECT | NUMERIC | 8 | 2 | Quantity rejected (returned to vendor or scrapped) |
| 11 | BKQC_RECV_DATE | DATE | 4 | — | Receipt date |
| 12 | BKQC_RECVR_NUM | NUMERIC | 8 | — | Receiver/shipment number |
| 13 | BKQC_UNIT_COST | NUMERIC | 8 | 4 | Unit cost at time of receipt |
| 14 | BKQC_VEND_CODE | STRING | 10 | — | Vendor code (FK → BKAPVEND) |

## BKQCTRAN — full field list

**QC TRANSACTION**

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKQC_TRN_ARDTE | DATE | 4 | — | Actual receipt date |
| 2 | BKQC_TRN_BODTE | DATE | 4 | — | Buy-off date (date QC acceptance was recorded) |
| 3 | BKQC_TRN_BQTY | NUMERIC | 8 | 4 | Buy-off quantity (accepted) |
| 4 | BKQC_TRN_BROKEN | STRING | 1 | — | Broken/damaged flag (`Y`=items arrived damaged) |
| 5 | BKQC_TRN_CODE | STRING | 15 | — | Part code (FK → BKICMSTR) |
| 6 | BKQC_TRN_EMPNUM | INTEGER | 2 | — | QC inspector employee number |
| 7 | BKQC_TRN_EXTRA | STRING | 100 | — | Extra data |
| 8 | BKQC_TRN_FAULT | STRING | 1 | — | Fault code (defect type code) |
| 9 | BKQC_TRN_FIXQTY | NUMERIC | 8 | 4 | Fixed / repaired quantity |
| 10 | BKQC_TRN_FLAG | STRING | 1 | — | Status flag |
| 11 | BKQC_TRN_GQTY | NUMERIC | 8 | 4 | Good quantity (accepted without repair) |
| 12 | BKQC_TRN_INVCD | STRING | 1 | — | Already-in-inventory flag (`Y`=items bypassed QC and went directly to stock) |
| 13 | BKQC_TRN_PO | NUMERIC | 8 | — | PO number (FK → BKAPPO) |
| 14 | BKQC_TRN_PODTE | DATE | 4 | — | PO date |
| 15 | BKQC_TRN_POQTY | NUMERIC | 8 | 4 | PO line quantity |
| 16 | BKQC_TRN_RECNUM | NUMERIC | 8 | — | Receiver number (PK — unique receipt transaction ID) |
| 17 | BKQC_TRN_RECVNM | NUMERIC | 8 | — | Shipment/packing slip number |
| 18 | BKQC_TRN_REWORK | STRING | 2 | — | Rework disposition code |
| 19 | BKQC_TRN_SCRAP | STRING | 2 | — | Scrap disposition code |
| 20 | BKQC_TRN_UQTY | NUMERIC | 8 | 4 | Under inspection / unresolved quantity |
| 21 | BKQC_TRN_VEND | STRING | 10 | — | Vendor code (FK → BKAPVEND) |

## ISRFQADS
**ARCHIVE RFQ NOTES**

Fields: 5 | Key: BK_DESC_NUM + BK_DESC_LINE

Identical schema to BKAPHDSC above. See that table for all field definitions.

**Confidence: 78/100** — PO header/line core fields confirmed from manufacturing PO context;
BKAP_PO_CONFIRM_1/2=buyer/vendor acknowledgment flags, RNI^=received-not-invoiced (computed),
PCKSLP=packing slip, PCONV=UOM conversion factor, PKSQTY=pack size, PSTDTE=promised ship date,
NKAP_POL_UM_LIN_1/2=stock/purchase UOM (source prefix typo confirmed) — all inferred from
standard manufacturing ERP patterns; BKRFQ QTY_N/COST_N tiered pricing structure confirmed
from 10-slot array pattern; ISDIGSIG 10-slot approval workflow with ACTIVE/AMT/FDATE/TDATE/FLAG
per approver confirmed from field-name array pattern; MOTCACH and exact CONFIRM codes require
RWN decryption to verify.
