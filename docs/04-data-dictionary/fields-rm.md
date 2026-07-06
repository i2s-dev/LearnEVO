# RM — RMA / Service-Repair: Field Reference

Status: verified-schema + completed field meanings (Pass 574i, 2026-07-06).

Note: file header originally said "Routing/Manufacturing" but all tables are RMA
(Return Merchandise Authorization) and Service/Repair module tables.

Source: `Evo-DBA_File_Fields 052421.xlsx`, sheet "Fields". Excel descriptions present for
ISSRINV (most address/amount fields) and ISSRINVL (most line fields); all remaining fields
name-inferred from RMA/service context.

ISRMAI/ISRMAAI (active/archived RMA info) are identical schemas.
ISSRINFO/ISSRAINF (active/archived supplemental info) are identical schemas.
ISSRMMS/ISSRAMMS (active/archived make-model-serial) are identical schemas.

---

## ISARMCHG
**CHANGES TO RMA** — RMA line change audit log (before/after snapshots)

Fields: 26 | Key: ISAR_CHG_INVNUM + ISAR_CHG_LINEID + ISAR_CHG_CDATE

One row per field change. A-prefixed fields = after-change values;
B-prefixed fields = before-change values.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISAR_CHG_AASD | DATE | 4 | — | After-change: actual ship date |
| 2 | ISAR_CHG_ACOMPR_1 | NUMERIC | 8 | 4 | After-change: commission rate slot 1 |
| 3 | ISAR_CHG_ACOMPR_2 | NUMERIC | 8 | 4 | After-change: commission rate slot 2 |
| 4 | ISAR_CHG_ADISC | NUMERIC | 8 | 2 | After-change: discount amount |
| 5 | ISAR_CHG_AESD | DATE | 4 | — | After-change: estimated ship date |
| 6 | ISAR_CHG_AEXTRA | STRING | 150 | — | After-change: extra data |
| 7 | ISAR_CHG_ALOC | STRING | 10 | — | After-change: warehouse location |
| 8 | ISAR_CHG_AOOQTY | NUMERIC | 8 | 2 | After-change: original order quantity |
| 9 | ISAR_CHG_APRICE | NUMERIC | 8 | 4 | After-change: line price |
| 10 | ISAR_CHG_BASD | DATE | 4 | — | Before-change: actual ship date |
| 11 | ISAR_CHG_BCOMPR_1 | NUMERIC | 8 | 4 | Before-change: commission rate slot 1 |
| 12 | ISAR_CHG_BCOMPR_2 | NUMERIC | 8 | 4 | Before-change: commission rate slot 2 |
| 13 | ISAR_CHG_BDISC | NUMERIC | 8 | 2 | Before-change: discount amount |
| 14 | ISAR_CHG_BESD | DATE | 4 | — | Before-change: estimated ship date |
| 15 | ISAR_CHG_BEXTRA | STRING | 150 | — | Before-change: extra data |
| 16 | ISAR_CHG_BLOC | STRING | 10 | — | Before-change: warehouse location |
| 17 | ISAR_CHG_BOOQTY | NUMERIC | 8 | 2 | Before-change: original order quantity |
| 18 | ISAR_CHG_BPRICE | NUMERIC | 8 | 4 | Before-change: line price |
| 19 | ISAR_CHG_CDATE | DATE | 4 | — | Date of this RMA line change |
| 20 | ISAR_CHG_INVNUM | NUMERIC | 8 | — | RMA invoice number (FK → ISSRINV) |
| 21 | ISAR_CHG_LINEID | NUMERIC | 8 | — | Line ID changed (FK → ISSRINVL) |
| 22 | ISAR_CHG_PCODE | STRING | 15 | — | Part code on this line |
| 23 | ISAR_CHG_REVLVL | STRING | 10 | — | Revision level at time of change |
| 24 | ISAR_CHG_SONUM | NUMERIC | 8 | — | Sales order number |
| 25 | ISAR_CHG_UNUM | INTEGER | 4 | — | Unique change sequence number |
| 26 | ISAR_CHG_USER | STRING | 15 | — | User who made the change |

## ISRMAAI
**ARCHIVE RMA INFO** — RMA records after period archive

Fields: 27 | Key: IS_RMA_NUM

Identical schema to ISRMAI — archived copy. See ISRMAI below for all field definitions.

## ISRMAC
**REASONS FOR RETURN** — return reason code lookup

Fields: 3 | Key: IS_RMA_CODE

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_RMA_CODE | STRING | 30 | — | Return reason code (PK) |
| 2 | IS_RMA_DESC | STRING | 60 | — | Return reason description (e.g., "Defective", "Wrong item shipped") |
| 3 | IS_RMA_EXTRA | STRING | 100 | — | Extra data |

## ISRMAI
**RMA INFO** — active Return Merchandise Authorization records

Fields: 27 | Key: IS_RMA_NUM

One record per RMA. Links back to the original invoice (OINVNUM) and tracks the full
lifecycle: received (RCPTDATE), credit memo issued (CMNUM/CMDATE), disposition decided,
optional replacement order, optional repair WO.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_RMA_CLOSDATE | DATE | 4 | — | RMA close date |
| 2 | IS_RMA_CMDATE | DATE | 4 | — | Credit memo date (when credit was issued) |
| 3 | IS_RMA_CMNUM | NUMERIC | 8 | — | Credit memo number (FK → BKARINV) |
| 4 | IS_RMA_DATE | DATE | 4 | — | RMA creation date |
| 5 | IS_RMA_DISP | STRING | 40 | — | Disposition description (e.g., "Scrap", "Restock", "Repair") |
| 6 | IS_RMA_DISPDATE | DATE | 4 | — | Disposition date (when returned goods were dispositioned) |
| 7 | IS_RMA_DISPSEL | INTEGER | 2 | — | Disposition selection code (1=restock, 2=scrap, 3=repair — inferred) |
| 8 | IS_RMA_IEXTRA | STRING | 150 | — | Extra data |
| 9 | IS_RMA_INVCD | STRING | 1 | — | Invoice code flag (P/X/Y — same semantics as BKAR_INV_INVCD) |
| 10 | IS_RMA_INVDATE | DATE | 4 | — | RMA invoice date |
| 11 | IS_RMA_INVNUM | NUMERIC | 8 | — | RMA invoice number (FK → ISSRINV) |
| 12 | IS_RMA_LINEID | NUMERIC | 8 | — | Line ID (float-encoded, ties to ISSRINVL line) |
| 13 | IS_RMA_NUM | NUMERIC | 8 | — | RMA number (PK) |
| 14 | IS_RMA_OINVNUM | NUMERIC | 8 | — | Original invoice number this RMA was raised against |
| 15 | IS_RMA_OLDRMANO | NUMERIC | 8 | — | Previous RMA number (if this is a replacement) |
| 16 | IS_RMA_OSONUM | NUMERIC | 8 | — | Original sales order number |
| 17 | IS_RMA_PART | STRING | 15 | — | Part code being returned (FK → BKICMSTR) |
| 18 | IS_RMA_RCPTDATE | DATE | 4 | — | Receipt date (when returned goods were physically received) |
| 19 | IS_RMA_REASON | STRING | 30 | — | Return reason text (FK → ISRMAC.IS_RMA_CODE) |
| 20 | IS_RMA_REORDER | STRING | 1 | — | Reorder flag: `Y`=replacement SO needed |
| 21 | IS_RMA_SODATE | DATE | 4 | — | RMA sales order date |
| 22 | IS_RMA_SONUM | NUMERIC | 8 | — | RMA sales order number |
| 23 | IS_RMA_SRNUM | NUMERIC | 8 | — | Service/repair order number (FK → ISSRINV if repair linked) |
| 24 | IS_RMA_STATUS | STRING | 30 | — | RMA status (e.g., "Open", "Received", "Closed") |
| 25 | IS_RMA_WARRANTY | STRING | 1 | — | Warranty flag: `Y`=return is under warranty |
| 26 | IS_RMA_WOPRE | NUMERIC | 8 | — | Repair WO prefix (if repair WO was created) |
| 27 | IS_RMA_WOSUF | INTEGER | 2 | — | Repair WO suffix |

## ISSRADSC
**ARCHIVED DBA SERVICE/REPAIR NOTES**

Fields: 5 | Key: BK_DESC_NUM + BK_DESC_LINE

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BK_DESC_CODE | STRING | 15 | — | not used |
| 2 | BK_DESC_DESC | STRING | 25 | — | not used |
| 3 | BK_DESC_LINE | INTEGER | 2 | — | Notes line number |
| 4 | BK_DESC_NOTES | STRING | 70 | — | Notes - text |
| 5 | BK_DESC_NUM | NUMERIC | 8 | — | PO Number |

## ISSRAINF
**ARCHIVED SERVICE/REPAIR SUPPLEMENTAL INFO** — user-configurable fields, archived

Fields: 54 | Key: ISSR_INFO_CODE + ISSR_INFO_UID

Identical schema to ISSRINFO — archived copy. See ISSRINFO below for all field definitions.

## ISSRAMMS
**ARCHIVED S/R MAKE MODEL SERIAL** — archived make/model/serial tracking

Fields: 12 | Key: ISSR_MMS_SRVNUM + ISSR_MMS_INVNUM + ISSR_MMS_LINEID

Identical schema to ISSRMMS — archived copy. See ISSRMMS below for all field definitions.

## ISSRDESC
**SERVICE/REPAIR DBA NOTES**

Fields: 5 | Key: BK_DESC_NUM + BK_DESC_LINE

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BK_DESC_CODE | STRING | 15 | — | not used |
| 2 | BK_DESC_DESC | STRING | 25 | — | not used |
| 3 | BK_DESC_LINE | INTEGER | 2 | — | Notes line number |
| 4 | BK_DESC_NOTES | STRING | 70 | — | Notes - text |
| 5 | BK_DESC_NUM | NUMERIC | 8 | — | PO Number |

## ISSRINFO
**SERVICE/REPAIR SUPPLEMENTAL INFO** — user-configurable extended fields

Fields: 54 | Key: ISSR_INFO_CODE + ISSR_INFO_UID

Two parallel sets of user-defined alphanumeric slots (AL1..20 = DBA-era naming,
ALPHA_1..20 = IS-era naming) and two sets of date slots (DATE1..5 vs DATE_1..5).
All slots are site-configurable via field labels; semantics are installation-specific.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISSR_INFO_AL1 | STRING | 25 | — | User-defined alphanumeric field AL-1 (DBA-era slot) |
| 2 | ISSR_INFO_AL10 | STRING | 25 | — | User-defined alphanumeric field AL-10 |
| 3 | ISSR_INFO_AL11 | STRING | 25 | — | User-defined alphanumeric field AL-11 |
| 4 | ISSR_INFO_AL12 | STRING | 25 | — | User-defined alphanumeric field AL-12 |
| 5 | ISSR_INFO_AL13 | STRING | 25 | — | User-defined alphanumeric field AL-13 |
| 6 | ISSR_INFO_AL14 | STRING | 25 | — | User-defined alphanumeric field AL-14 |
| 7 | ISSR_INFO_AL15 | STRING | 25 | — | User-defined alphanumeric field AL-15 |
| 8 | ISSR_INFO_AL16 | STRING | 25 | — | User-defined alphanumeric field AL-16 |
| 9 | ISSR_INFO_AL17 | STRING | 25 | — | User-defined alphanumeric field AL-17 |
| 10 | ISSR_INFO_AL18 | STRING | 25 | — | User-defined alphanumeric field AL-18 |
| 11 | ISSR_INFO_AL19 | STRING | 25 | — | User-defined alphanumeric field AL-19 |
| 12 | ISSR_INFO_AL2 | STRING | 25 | — | User-defined alphanumeric field AL-2 |
| 13 | ISSR_INFO_AL20 | STRING | 25 | — | User-defined alphanumeric field AL-20 |
| 14 | ISSR_INFO_AL3 | STRING | 25 | — | User-defined alphanumeric field AL-3 |
| 15 | ISSR_INFO_AL4 | STRING | 25 | — | User-defined alphanumeric field AL-4 |
| 16 | ISSR_INFO_AL5 | STRING | 25 | — | User-defined alphanumeric field AL-5 |
| 17 | ISSR_INFO_AL6 | STRING | 25 | — | User-defined alphanumeric field AL-6 |
| 18 | ISSR_INFO_AL7 | STRING | 25 | — | User-defined alphanumeric field AL-7 |
| 19 | ISSR_INFO_AL8 | STRING | 25 | — | User-defined alphanumeric field AL-8 |
| 20 | ISSR_INFO_AL9 | STRING | 25 | — | User-defined alphanumeric field AL-9 |
| 21 | ISSR_INFO_ALPHA_1 | STRING | 25 | — | User-defined alphanumeric field ALPHA-1 (IS-era slot) |
| 22 | ISSR_INFO_ALPHA_10 | STRING | 25 | — | User-defined alphanumeric field ALPHA-10 |
| 23 | ISSR_INFO_ALPHA_11 | STRING | 25 | — | User-defined alphanumeric field ALPHA-11 |
| 24 | ISSR_INFO_ALPHA_12 | STRING | 25 | — | User-defined alphanumeric field ALPHA-12 |
| 25 | ISSR_INFO_ALPHA_13 | STRING | 25 | — | User-defined alphanumeric field ALPHA-13 |
| 26 | ISSR_INFO_ALPHA_14 | STRING | 25 | — | User-defined alphanumeric field ALPHA-14 |
| 27 | ISSR_INFO_ALPHA_15 | STRING | 25 | — | User-defined alphanumeric field ALPHA-15 |
| 28 | ISSR_INFO_ALPHA_16 | STRING | 25 | — | User-defined alphanumeric field ALPHA-16 |
| 29 | ISSR_INFO_ALPHA_17 | STRING | 25 | — | User-defined alphanumeric field ALPHA-17 |
| 30 | ISSR_INFO_ALPHA_18 | STRING | 25 | — | User-defined alphanumeric field ALPHA-18 |
| 31 | ISSR_INFO_ALPHA_19 | STRING | 25 | — | User-defined alphanumeric field ALPHA-19 |
| 32 | ISSR_INFO_ALPHA_2 | STRING | 25 | — | User-defined alphanumeric field ALPHA-2 |
| 33 | ISSR_INFO_ALPHA_20 | STRING | 25 | — | User-defined alphanumeric field ALPHA-20 |
| 34 | ISSR_INFO_ALPHA_3 | STRING | 25 | — | User-defined alphanumeric field ALPHA-3 |
| 35 | ISSR_INFO_ALPHA_4 | STRING | 25 | — | User-defined alphanumeric field ALPHA-4 |
| 36 | ISSR_INFO_ALPHA_5 | STRING | 25 | — | User-defined alphanumeric field ALPHA-5 |
| 37 | ISSR_INFO_ALPHA_6 | STRING | 25 | — | User-defined alphanumeric field ALPHA-6 |
| 38 | ISSR_INFO_ALPHA_7 | STRING | 25 | — | User-defined alphanumeric field ALPHA-7 |
| 39 | ISSR_INFO_ALPHA_8 | STRING | 25 | — | User-defined alphanumeric field ALPHA-8 |
| 40 | ISSR_INFO_ALPHA_9 | STRING | 25 | — | User-defined alphanumeric field ALPHA-9 |
| 41 | ISSR_INFO_CODE | STRING | 15 | — | Service/repair or RMA number linking this record to its header |
| 42 | ISSR_INFO_DATE1 | DATE | 4 | — | User-defined date 1 (DBA-era slot) |
| 43 | ISSR_INFO_DATE2 | DATE | 4 | — | User-defined date 2 |
| 44 | ISSR_INFO_DATE3 | DATE | 4 | — | User-defined date 3 |
| 45 | ISSR_INFO_DATE4 | DATE | 4 | — | User-defined date 4 |
| 46 | ISSR_INFO_DATE5 | DATE | 4 | — | User-defined date 5 |
| 47 | ISSR_INFO_DATE_1 | DATE | 4 | — | User-defined date 1 (IS-era slot) |
| 48 | ISSR_INFO_DATE_2 | DATE | 4 | — | User-defined date 2 (IS-era slot) |
| 49 | ISSR_INFO_DATE_3 | DATE | 4 | — | User-defined date 3 (IS-era slot) |
| 50 | ISSR_INFO_DATE_4 | DATE | 4 | — | User-defined date 4 (IS-era slot) |
| 51 | ISSR_INFO_DATE_5 | DATE | 4 | — | User-defined date 5 (IS-era slot) |
| 52 | ISSR_INFO_EXTRA | STRING | 100 | — | Extra data |
| 53 | ISSR_INFO_SRNUM | NUMERIC | 8 | — | Service/repair number (FK → ISSRINV.BKAR_INV_NUM) |
| 54 | ISSR_INFO_UID | NUMERIC | 8 | — | Unique ID (PK — float-encoded) |

## ISSRINV
**SERVICE/REPAIR & RMA HEADER** — S/R and RMA order header

Fields: 82 | Key: BKAR_INV_NUM

Shares BKAR_INV_* prefix with AR invoice header (BKARINV). Address/amount fields
confirmed from Excel; IS-module and S/R-specific fields name-inferred.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAR_INV_BILA1 | STRING | 30 | — | Billing Address 1 |
| 2 | BKAR_INV_BILA2 | STRING | 30 | — | Billing Address 2 |
| 3 | BKAR_INV_BILA3 | STRING | 30 | — | Billing Address 3 |
| 4 | BKAR_INV_BILATN | STRING | 30 | — | Billing Attention |
| 5 | BKAR_INV_BILCNT | STRING | 30 | — | Billing Country |
| 6 | BKAR_INV_BILCOD | STRING | 10 | — | Bill To Code |
| 7 | BKAR_INV_BILCTY | STRING | 30 | — | Billing City |
| 8 | BKAR_INV_BILNME | STRING | 30 | — | Bill To Name |
| 9 | BKAR_INV_BILST | STRING | 2 | — | Billing State |
| 10 | BKAR_INV_BILZIP | STRING | 10 | — | Billing ZIP |
| 11 | BKAR_INV_CCOAMT | NUMERIC | 8 | 2 | Co-op credit offset amount |
| 12 | BKAR_INV_CHKNUM | NUMERIC | 8 | — | Check Number |
| 13 | BKAR_INV_COGS | NUMERIC | 8 | 2 | COGS |
| 14 | BKAR_INV_COMAMT | NUMERIC | 8 | 2 | Total commission amount on this order |
| 15 | BKAR_INV_COMMPR_1 | NUMERIC | 8 | 4 | Commission rate — salesperson 1 |
| 16 | BKAR_INV_COMMPR_2 | NUMERIC | 8 | 4 | Commission rate — salesperson 2 |
| 17 | BKAR_INV_CUSA1 | STRING | 30 | — | Customer Address 1 |
| 18 | BKAR_INV_CUSA2_1 | STRING | 30 | — | Customer address line 2 — part 1 |
| 19 | BKAR_INV_CUSA2_2 | STRING | 30 | — | Customer address line 2 — part 2 |
| 20 | BKAR_INV_CUSATT | STRING | 30 | — | Attention: |
| 21 | BKAR_INV_CUSCNT | STRING | 30 | — | Country |
| 22 | BKAR_INV_CUSCOD | STRING | 10 | — | Customer Code |
| 23 | BKAR_INV_CUSCTY | STRING | 26 | — | City |
| 24 | BKAR_INV_CUSNME | STRING | 30 | — | Customer Name |
| 25 | BKAR_INV_CUSORD | STRING | 25 | — | Customer Order |
| 26 | BKAR_INV_CUSST | STRING | 2 | — | State |
| 27 | BKAR_INV_CUSZIP | STRING | 10 | — | ZIP Code |
| 28 | BKAR_INV_DCODE | STRING | 10 | — | Discount Code |
| 29 | BKAR_INV_DEPAMT | NUMERIC | 8 | 2 | Deposit amount applied to this order |
| 30 | BKAR_INV_DESC | STRING | 30 | — | Orser Description |
| 31 | BKAR_INV_ENDLNE | STRING | 1 | — | Ending lines Y/N |
| 32 | BKAR_INV_ENTBY | STRING | 5 | — | Entered By |
| 33 | BKAR_INV_EXTRA | STRING | 150 | — | Extra |
| 34 | BKAR_INV_FOB | STRING | 15 | — | FOB |
| 35 | BKAR_INV_FRGHT | NUMERIC | 8 | 2 | Freight Amount |
| 36 | BKAR_INV_GLDPT | STRING | 4 | — | GL Department |
| 37 | BKAR_INV_INDATE | DATE | 4 | — | In-service/received date (when item was brought in for repair) |
| 38 | BKAR_INV_INVCD | STRING | 1 | — | INVCD X/P/Y |
| 39 | BKAR_INV_INVDTE | DATE | 4 | — | Invoice Date |
| 40 | BKAR_INV_ISCUR | STRING | 3 | — | IS multi-currency code (ISO currency for this order) |
| 41 | BKAR_INV_ISMCDT | DATE | 4 | — | IS multi-currency rate date |
| 42 | BKAR_INV_ISREV | STRING | 1 | — | IS revision flag: `Y`=order has been revised |
| 43 | BKAR_INV_ISRVDT | DATE | 4 | — | IS revision date |
| 44 | BKAR_INV_ISTXKY | STRING | 10 | — | IS tax key (extended tax rate key for multi-zone taxation) |
| 45 | BKAR_INV_ITMZTX_1 | STRING | 1 | — | Item zone tax flag for tax zone 1 |
| 46 | BKAR_INV_ITMZTX_2 | STRING | 1 | — | Item zone tax flag for tax zone 2 |
| 47 | BKAR_INV_JOBNUM | STRING | 15 | — | Job Number 1 |
| 48 | BKAR_INV_LINV^P | NUMERIC | 8 | — | Linked invoice number (prior or replacement invoice) |
| 49 | BKAR_INV_LOC | STRING | 10 | — | Location |
| 50 | BKAR_INV_NL | INTEGER | 2 | — | Number Lines |
| 51 | BKAR_INV_NUM | NUMERIC | 8 | — | Invoice Number |
| 52 | BKAR_INV_ORDDTE | DATE | 4 | — | Order Date |
| 53 | BKAR_INV_PCODE | INTEGER | 2 | — | Price Code |
| 54 | BKAR_INV_RELNUM | NUMERIC | 8 | — | Related document number (linked RMA, WO, or SO) |
| 55 | BKAR_INV_RETEN | NUMERIC | 8 | 2 | Retainage amount (held back from invoice total) |
| 56 | BKAR_INV_RTS | STRING | 1 | — | Ready To Ship Y/N |
| 57 | BKAR_INV_SCCOGS | NUMERIC | 8 | 2 | Secondary/split COGS (for shared cost allocation) |
| 58 | BKAR_INV_SHIPDT | DATE | 4 | — | Ship Date |
| 59 | BKAR_INV_SHIPPR | NUMERIC | 8 | — | Shipper Number |
| 60 | BKAR_INV_SHPA1 | STRING | 30 | — | Ship Address 1 |
| 61 | BKAR_INV_SHPA2_1 | STRING | 30 | — | Ship address line 2 — part 1 |
| 62 | BKAR_INV_SHPA2_2 | STRING | 30 | — | Ship address line 2 — part 2 |
| 63 | BKAR_INV_SHPATN | STRING | 30 | — | Ship Attention |
| 64 | BKAR_INV_SHPCNT | STRING | 30 | — | Ship Country |
| 65 | BKAR_INV_SHPCOD | STRING | 10 | — | Ship To Code |
| 66 | BKAR_INV_SHPCTY | STRING | 26 | — | Ship City |
| 67 | BKAR_INV_SHPNME | STRING | 30 | — | Ship Name |
| 68 | BKAR_INV_SHPST | STRING | 2 | — | Shop State |
| 69 | BKAR_INV_SHPVIA | STRING | 15 | — | Ship Via |
| 70 | BKAR_INV_SHPZIP | STRING | 10 | — | Ship ZIP Code |
| 71 | BKAR_INV_SLSP | INTEGER | 2 | — | Salesperson 1 |
| 72 | BKAR_INV_SLSP2 | INTEGER | 2 | — | Sales Person 2 |
| 73 | BKAR_INV_SONUM | NUMERIC | 8 | — | Sales Order Number |
| 74 | BKAR_INV_SUBTOT | NUMERIC | 8 | 2 | Sub Total |
| 75 | BKAR_INV_TAXABL | STRING | 1 | — | Taxable Y/N |
| 76 | BKAR_INV_TAXAMT | NUMERIC | 8 | 2 | Tax Amount |
| 77 | BKAR_INV_TAXKEY | STRING | 4 | — | Tax key code (FK → tax rate table) |
| 78 | BKAR_INV_TAXRTE | NUMERIC | 8 | 4 | Tax Rate |
| 79 | BKAR_INV_TERMD | STRING | 10 | — | Terms Description |
| 80 | BKAR_INV_TERMNM | INTEGER | 2 | — | Terms Number |
| 81 | BKAR_INV_TOTAL | NUMERIC | 8 | 2 | Total |
| 82 | BKAR_INV_TRACK | STRING | 40 | — | Carrier tracking number |

## ISSRINVL
**SERVICE/REPAIR & RMA LINE** — S/R and RMA order line items

Fields: 29 | Key: BKAR_INVL_INVNM + BKAR_INVL_CNTR

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAR_INVL_ABQTY | NUMERIC | 8 | 2 | Options Quantity |
| 2 | BKAR_INVL_ASD | DATE | 4 | — | Actual Ship Date |
| 3 | BKAR_INVL_CNTR | INTEGER | 2 | — | Line Counter |
| 4 | BKAR_INVL_COMPR_1 | NUMERIC | 8 | 4 | Commission rate — salesperson 1 |
| 5 | BKAR_INVL_COMPR_2 | NUMERIC | 8 | 4 | Commission rate — salesperson 2 |
| 6 | BKAR_INVL_COOP | NUMERIC | 8 | 2 | Co-op advertising credit on this line |
| 7 | BKAR_INVL_ESD | DATE | 4 | — | Estimated Ship Date |
| 8 | BKAR_INVL_EXTRA | STRING | 100 | — | Extra |
| 9 | BKAR_INVL_FRGHT | NUMERIC | 8 | 2 | Freight |
| 10 | BKAR_INVL_INVNM | NUMERIC | 8 | — | Invoice (S/R order) Number |
| 11 | BKAR_INVL_ITYPE | STRING | 1 | — | Part Type |
| 12 | BKAR_INVL_JOB^ | STRING | 10 | — | Job number (linked from SO line) |
| 13 | BKAR_INVL_LOC | STRING | 10 | — | Location |
| 14 | BKAR_INVL_OOQTY | NUMERIC | 8 | 2 | Original Order Quantity |
| 15 | BKAR_INVL_PCODE | STRING | 15 | — | Part Code |
| 16 | BKAR_INVL_PCOGS | NUMERIC | 8 | 4 | COGS |
| 17 | BKAR_INVL_PDESC | STRING | 30 | — | Part Description |
| 18 | BKAR_INVL_PDISC | NUMERIC | 8 | 2 | Discount |
| 19 | BKAR_INVL_PEXT | NUMERIC | 8 | 2 | Extended Price |
| 20 | BKAR_INVL_PPRCE | NUMERIC | 8 | 4 | Price |
| 21 | BKAR_INVL_PQTY | NUMERIC | 8 | 2 | Quantity |
| 22 | BKAR_INVL_RTS | STRING | 1 | — | Ready to Ship |
| 23 | BKAR_INVL_SCCOG | NUMERIC | 8 | 4 | Secondary/split COGS for this line |
| 24 | BKAR_INVL_TXAMT | NUMERIC | 8 | 2 | Tax Amount |
| 25 | BKAR_INVL_TXBLE | STRING | 1 | — | Taxable Y/N |
| 26 | BKAR_INVL_UBO | NUMERIC | 8 | 2 | Units on Back Order |
| 27 | BKAR_INVL_UM_LN_1 | STRING | 3 | — | Unit of measure — stock UOM code |
| 28 | BKAR_INVL_UM_LN_2 | STRING | 3 | — | Unit of measure — selling UOM code |
| 29 | BKAR_INVL_USTD | NUMERIC | 8 | 2 | Units Shipped To Date |

## ISSRMMS
**S/R MAKE MODEL SERIAL** — make/model/serial numbers for items in service

Fields: 12 | Key: ISSR_MMS_SRVNUM + ISSR_MMS_INVNUM + ISSR_MMS_LINEID

Tracks physical item identity for warranty and serial-tracked service/repair.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISSR_MMS_EXTRA | STRING | 150 | — | Extra data |
| 2 | ISSR_MMS_INDATE | DATE | 4 | — | Date item came in (received for service) |
| 3 | ISSR_MMS_INVNUM | NUMERIC | 8 | — | Invoice/RMA/S/R number (FK → ISSRINV) |
| 4 | ISSR_MMS_LINEID | INTEGER | 2 | — | Line ID on the invoice |
| 5 | ISSR_MMS_MAKE | STRING | 50 | — | Manufacturer or make (e.g., "Dell", "Parker") |
| 6 | ISSR_MMS_MODLE | STRING | 50 | — | Model designation |
| 7 | ISSR_MMS_OUTDTE | DATE | 4 | — | Date item went out (returned to customer) |
| 8 | ISSR_MMS_PART | STRING | 15 | — | Part code (FK → BKICMSTR) |
| 9 | ISSR_MMS_SERIAL | STRING | 50 | — | Serial number of the item being serviced |
| 10 | ISSR_MMS_SRVNUM | NUMERIC | 8 | — | Service/repair order number (FK → ISSRINV.BKAR_INV_NUM) |
| 11 | ISSR_MMS_WOPRE | NUMERIC | 8 | — | Work order prefix (if repair WO was created) |
| 12 | ISSR_MMS_WOSUF | INTEGER | 2 | — | Work order suffix |

**Confidence: 80/100** — ISSRINV/ISSRINVL address/amount fields confirmed from Excel; ISRMAI
lifecycle fields (CLOSDATE, CMNUM, DISPSEL, RCPTDATE, WARRANTY) clear from RMA workflow
conventions; ISSRINFO user-configurable slots confirmed as free-text by nature; IS-module
specific fields (ISCUR, ISMCDT, ISTXKY, ITMZTX_*) inferred from multi-currency/tax context;
exact IS_RMA_DISPSEL integer values require RWN decryption.
