# SO — Sales Orders: Field Reference

Status: verified-schema

Source: `Evo-DBA_File_Fields 052421.xlsx`, sheet "Fields".
Field descriptions where provided by source; otherwise name-inferred.

Pass 574k-8: all blanks filled. Identical-schema tables collapsed to cross-references.

---

## BKARINV
**SALES ORDER HEADER**

Fields: 82 | Prefix: BKAR_INV_

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
| 11 | BKAR_INV_CCOAMT | NUMERIC | 8 | 2 | Credit card authorization amount |
| 12 | BKAR_INV_CHKNUM | NUMERIC | 8 | — | Check Number |
| 13 | BKAR_INV_COGS | NUMERIC | 8 | 2 | COGS |
| 14 | BKAR_INV_COMAMT | NUMERIC | 8 | 2 | Total commission amount on order |
| 15 | BKAR_INV_COMMPR_1 | NUMERIC | 8 | 4 | Salesperson 1 commission percent |
| 16 | BKAR_INV_COMMPR_2 | NUMERIC | 8 | 4 | Salesperson 2 commission percent |
| 17 | BKAR_INV_CUSA1 | STRING | 30 | — | Customer Address 1 |
| 18 | BKAR_INV_CUSA2_1 | STRING | 30 | — | Customer address line 2, continuation 1 |
| 19 | BKAR_INV_CUSA2_2 | STRING | 30 | — | Customer address line 2, continuation 2 |
| 20 | BKAR_INV_CUSATT | STRING | 30 | — | Attention: |
| 21 | BKAR_INV_CUSCNT | STRING | 30 | — | Country |
| 22 | BKAR_INV_CUSCOD | STRING | 10 | — | Customer Code |
| 23 | BKAR_INV_CUSCTY | STRING | 26 | — | City |
| 24 | BKAR_INV_CUSNME | STRING | 30 | — | Customer Name |
| 25 | BKAR_INV_CUSORD | STRING | 25 | — | Customer Order |
| 26 | BKAR_INV_CUSST | STRING | 2 | — | State |
| 27 | BKAR_INV_CUSZIP | STRING | 10 | — | ZIP Code |
| 28 | BKAR_INV_DCODE | STRING | 10 | — | Discount Code |
| 29 | BKAR_INV_DEPAMT | NUMERIC | 8 | 2 | Deposit / prepayment amount received |
| 30 | BKAR_INV_DESC | STRING | 30 | — | Orser Description |
| 31 | BKAR_INV_ENDLNE | STRING | 1 | — | Ending lines Y/N |
| 32 | BKAR_INV_ENTBY | STRING | 5 | — | Entered By |
| 33 | BKAR_INV_EXTRA | STRING | 150 | — | Extra |
| 34 | BKAR_INV_FOB | STRING | 15 | — | FOB |
| 35 | BKAR_INV_FRGHT | NUMERIC | 8 | 2 | Freight Amount |
| 36 | BKAR_INV_GLDPT | STRING | 4 | — | GL Department |
| 37 | BKAR_INV_INDATE | DATE | 4 | — | System entry / internal date |
| 38 | BKAR_INV_INVCD | STRING | 1 | — | INVCD X/P/Y |
| 39 | BKAR_INV_INVDTE | DATE | 4 | — | Invoice Date |
| 40 | BKAR_INV_ISCUR | STRING | 3 | — | Multi-currency code |
| 41 | BKAR_INV_ISMCDT | DATE | 4 | — | Multi-currency transaction date |
| 42 | BKAR_INV_ISREV | STRING | 1 | — | Reversed order flag (Y/N) |
| 43 | BKAR_INV_ISRVDT | DATE | 4 | — | Reversal date |
| 44 | BKAR_INV_ISTXKY | STRING | 10 | — | Extended tax key (10-char) |
| 45 | BKAR_INV_ITMZTX_1 | STRING | 1 | — | Itemized tax flag, slot 1 |
| 46 | BKAR_INV_ITMZTX_2 | STRING | 1 | — | Itemized tax flag, slot 2 |
| 47 | BKAR_INV_JOBNUM | STRING | 15 | — | Job Number 1 |
| 48 | BKAR_INV_LINV^P | NUMERIC | 8 | — | Linked invoice number (parent/backorder link) |
| 49 | BKAR_INV_LOC | STRING | 10 | — | Location |
| 50 | BKAR_INV_NL | INTEGER | 2 | — | Number Lines |
| 51 | BKAR_INV_NUM | NUMERIC | 8 | — | Invoice Number |
| 52 | BKAR_INV_ORDDTE | DATE | 4 | — | Order Date |
| 53 | BKAR_INV_PCODE | INTEGER | 2 | — | Price Code |
| 54 | BKAR_INV_RELNUM | NUMERIC | 8 | — | Release number (blanket order release) |
| 55 | BKAR_INV_RETEN | NUMERIC | 8 | 2 | Retention / holdback amount |
| 56 | BKAR_INV_RTS | STRING | 1 | — | Ready To Ship Y/N |
| 57 | BKAR_INV_SCCOGS | NUMERIC | 8 | 2 | Sub-contracted component COGS |
| 58 | BKAR_INV_SHIPDT | DATE | 4 | — | Ship Date |
| 59 | BKAR_INV_SHIPPR | NUMERIC | 8 | — | Shipper Number |
| 60 | BKAR_INV_SHPA1 | STRING | 30 | — | Ship Address 1 |
| 61 | BKAR_INV_SHPA2_1 | STRING | 30 | — | Ship address line 2, continuation 1 |
| 62 | BKAR_INV_SHPA2_2 | STRING | 30 | — | Ship address line 2, continuation 2 |
| 63 | BKAR_INV_SHPATN | STRING | 30 | — | Ship Attention |
| 64 | BKAR_INV_SHPCNT | STRING | 30 | — | Ship Country |
| 65 | BKAR_INV_SHPCOD | STRING | 10 | — | Ship To Code |
| 66 | BKAR_INV_SHPCTY | STRING | 26 | — | Ship City |
| 67 | BKAR_INV_SHPNME | STRING | 30 | — | Ship Name |
| 68 | BKAR_INV_SHPST | STRING | 2 | — | Ship State |
| 69 | BKAR_INV_SHPVIA | STRING | 15 | — | Ship Via |
| 70 | BKAR_INV_SHPZIP | STRING | 10 | — | Ship ZIP Code |
| 71 | BKAR_INV_SLSP | INTEGER | 2 | — | Salesperson 1 |
| 72 | BKAR_INV_SLSP2 | INTEGER | 2 | — | Sales Person 2 |
| 73 | BKAR_INV_SONUM | NUMERIC | 8 | — | Sales Order Number |
| 74 | BKAR_INV_SUBTOT | NUMERIC | 8 | 2 | Sub Total |
| 75 | BKAR_INV_TAXABL | STRING | 1 | — | Taxable Y/N |
| 76 | BKAR_INV_TAXAMT | NUMERIC | 8 | 2 | Tax Amount |
| 77 | BKAR_INV_TAXKEY | STRING | 4 | — | Tax key (legacy 4-char) |
| 78 | BKAR_INV_TAXRTE | NUMERIC | 8 | 4 | Tax Rate |
| 79 | BKAR_INV_TERMD | STRING | 10 | — | Terms Description |
| 80 | BKAR_INV_TERMNM | INTEGER | 2 | — | Terms Number |
| 81 | BKAR_INV_TOTAL | NUMERIC | 8 | 2 | Total |
| 82 | BKAR_INV_TRACK | STRING | 40 | — | Shipment tracking number |

## BKARHIVL
**INVOICE LINE (Archived)**

Identical schema to [BKARINVL](#bkarinvl) (BKAR_INVL_ prefix). Archived invoice line items.

## BKARHINV
**INVOICE HEADER (Archived)**

Identical schema to [BKARINV](#bkarinv) (BKAR_INV_ prefix). Archived invoice headers.

## BKARINVL
**SALES ORDER LINES**

Fields: 29 | Prefix: BKAR_INVL_

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAR_INVL_ABQTY | NUMERIC | 8 | 2 | Options / add-on quantity |
| 2 | BKAR_INVL_ASD | DATE | 4 | — | Actual Ship Date |
| 3 | BKAR_INVL_CNTR | INTEGER | 2 | — | Line Counter |
| 4 | BKAR_INVL_COMPR_1 | NUMERIC | 8 | 4 | Salesperson 1 commission percent on line |
| 5 | BKAR_INVL_COMPR_2 | NUMERIC | 8 | 4 | Salesperson 2 commission percent on line |
| 6 | BKAR_INVL_COOP | NUMERIC | 8 | 2 | Co-op / cooperative advertising amount |
| 7 | BKAR_INVL_ESD | DATE | 4 | — | Estimated Ship Date |
| 8 | BKAR_INVL_EXTRA | STRING | 100 | — | Extra |
| 9 | BKAR_INVL_FRGHT | NUMERIC | 8 | 2 | Freight |
| 10 | BKAR_INVL_INVNM | NUMERIC | 8 | — | Sales Order Number |
| 11 | BKAR_INVL_ITYPE | STRING | 1 | — | Part Type |
| 12 | BKAR_INVL_JOB^ | STRING | 10 | — | Job number link (job costing pointer) |
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
| 23 | BKAR_INVL_SCCOG | NUMERIC | 8 | 4 | Sub-contracted component COGS on line |
| 24 | BKAR_INVL_TXAMT | NUMERIC | 8 | 2 | Tax Amount |
| 25 | BKAR_INVL_TXBLE | STRING | 1 | — | Taxable Y/N |
| 26 | BKAR_INVL_UBO | NUMERIC | 8 | 2 | Units on Back Order |
| 27 | BKAR_INVL_UM_LN_1 | STRING | 3 | — | Stock unit of measure (stocking UOM) |
| 28 | BKAR_INVL_UM_LN_2 | STRING | 3 | — | Ordering unit of measure (order UOM) |
| 29 | BKAR_INVL_USTD | NUMERIC | 8 | 2 | Units Shipped To Date |

## BKARRDSC
**DBA RECURRING ORDER NOTES**

Fields: 5

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BK_DESC_CODE | STRING | 15 | — | not used |
| 2 | BK_DESC_DESC | STRING | 25 | — | not used |
| 3 | BK_DESC_LINE | INTEGER | 2 | — | Notes line number |
| 4 | BK_DESC_NOTES | STRING | 70 | — | Notes - text |
| 5 | BK_DESC_NUM | NUMERIC | 8 | — | PO Number |

## BKARRINV
**RECURRING ORDER HEADER**

Identical schema to [BKARINV](#bkarinv) (BKAR_INV_ prefix). Recurring/standing order headers.

## BKARRIVL
**RECURRING ORDER LINE**

Identical schema to [BKARINVL](#bkarinvl) (BKAR_INVL_ prefix). Recurring/standing order lines.

## BKARTXN
**UNPOSTED LOT ALLOCATION TO ORDER LINES**

Fields: 14 | Prefix: BKAR_TXN_

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAR_TXN_BIN | STRING | 15 | — | Bin location |
| 2 | BKAR_TXN_CODE | STRING | 15 | — | Transaction Code |
| 3 | BKAR_TXN_DATE | DATE | 4 | — | Date |
| 4 | BKAR_TXN_DESC | STRING | 30 | — | Description |
| 5 | BKAR_TXN_EXTRA | STRING | 50 | — | Extra/custom data |
| 6 | BKAR_TXN_LINE | NUMERIC | 8 | — | Line Number |
| 7 | BKAR_TXN_LOC | STRING | 10 | — | Warehouse location code |
| 8 | BKAR_TXN_LOT | STRING | 15 | — | Lot ID |
| 9 | BKAR_TXN_QTY | NUMERIC | 8 | 2 | Quantity |
| 10 | BKAR_TXN_SERIAL | STRING | 25 | — | Serial ID |
| 11 | BKAR_TXN_SONUM | NUMERIC | 8 | — | SO Number |
| 12 | BKAR_TXN_SRNUM | NUMERIC | 8 | — | Stock record number (internal lot/serial record key) |
| 13 | BKAR_TXN_STOCK | STRING | 15 | — | Inventory item code (FK→inventory) |
| 14 | BKAR_TXN_TMPSO | STRING | 40 | — | Temporary SO identifier (staging reference) |

## BKARTXNS
**UNPOSTED SERIAL ALLOCATION TO ORDER LINES**

Identical schema to [BKARTXN](#bkartxn) (BKAR_TXN_ prefix). Serial (rather than lot) allocation staging.

## BKESTQT
**SALES QUOTATION HEADER**

Identical schema to [BKARINV](#bkarinv) (BKAR_INV_ prefix). Sales quotation headers.

## BKESTQTL
**SALES QUOTATION LINE ITEMS**

Identical schema to [BKARINVL](#bkarinvl) (BKAR_INVL_ prefix). Sales quotation line items.

## BKICPMAT
**PRICE MATRIX**

Fields: 85 | Prefix: BKIC_PMAT_

10-tier quantity-break pricing per item/customer combination.
QTY_N = break threshold, RATE_N = price at that tier, PER_N = discount percent at that tier.
COMM1_N/COMM2_N = commissions by tier. ISRET_N = IS retail price by tier.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKIC_PMAT_ACCRU | NUMERIC | 8 | 2 | Accrual amount |
| 2 | BKIC_PMAT_BILLB | NUMERIC | 8 | 2 | Billback amount |
| 3 | BKIC_PMAT_CLASS | STRING | 4 | — | Item or customer class |
| 4–13 | BKIC_PMAT_COMM1_1..10 | NUMERIC | 8 | 4 | Salesperson 1 commission percent, qty break 1–10 |
| 14–23 | BKIC_PMAT_COMM2_1..10 | NUMERIC | 8 | 4 | Salesperson 2 commission percent, qty break 1–10 |
| 24 | BKIC_PMAT_CUST | STRING | 10 | — | Customer Code |
| 25 | BKIC_PMAT_DCODE | STRING | 10 | — | Discount code |
| 26 | BKIC_PMAT_EDATE | DATE | 4 | — | Effective start date |
| 27 | BKIC_PMAT_EXP | DATE | 4 | — | Expiration Date |
| 28 | BKIC_PMAT_EXTRA | STRING | 50 | — | Extra/custom data |
| 29 | BKIC_PMAT_FRTAL | NUMERIC | 8 | 2 | Freight allowance |
| 30–39 | BKIC_PMAT_ISRET_1..10 | NUMERIC | 8 | 4 | IS retail price percent, qty break 1–10 |
| 40 | BKIC_PMAT_LUMP | NUMERIC | 8 | 2 | Lump-sum / flat price |
| 41 | BKIC_PMAT_METH | STRING | 11 | — | Pricing method code (PERCENT/FIXED/MARKUP/etc.) |
| 42 | BKIC_PMAT_MIN | NUMERIC | 8 | 2 | Minimum order quantity |
| 43 | BKIC_PMAT_MINPR | NUMERIC | 8 | 4 | Minimum price |
| 44 | BKIC_PMAT_OFFCH | NUMERIC | 8 | 2 | Off-channel charge / rebate |
| 45 | BKIC_PMAT_OFFIN | NUMERIC | 8 | 2 | Off-invoice discount amount |
| 46 | BKIC_PMAT_PCODE | STRING | 15 | — | Item Number |
| 47 | BKIC_PMAT_PDESC | STRING | 30 | — | Item description |
| 48–57 | BKIC_PMAT_PER_1..10 | NUMERIC | 8 | 4 | Discount percent at qty break 1–10 |
| 58 | BKIC_PMAT_PFLAG | STRING | 1 | — | Pricing flag |
| 59 | BKIC_PMAT_PNUM | INTEGER | 2 | — | Quantity |
| 60 | BKIC_PMAT_PROMO | NUMERIC | 8 | 2 | Promotional price |
| 61–70 | BKIC_PMAT_QTY_1..10 | NUMERIC | 8 | 2 | Quantity break thresholds 1–10 |
| 71–80 | BKIC_PMAT_RATE_1..10 | NUMERIC | 8 | 4 | Price rates at qty break 1–10 |
| 81 | BKIC_PMAT_SCAND | NUMERIC | 8 | 2 | Scan / point-of-sale allowance |
| 82 | BKIC_PMAT_SDATE | DATE | 4 | — | Start date |
| 83 | BKIC_PMAT_SRTS | NUMERIC | 8 | 2 | Suggested retail price |
| 84 | BKIC_PMAT_SWELL | NUMERIC | 8 | 2 | Swell allowance (product damage allowance) |
| 85 | BKIC_PMAT_UID | STRING | 40 | — | Unique identifier |

## BKICAPMA
**ARCHIVE PRICE CODE**

Identical schema to [BKICPMAT](#bkicpmat) (BKIC_PMAT_ prefix). Archived/historical price matrix records.

## BKQTNOTE
**DBA QUOTE NOTES**

Identical schema to [BKARRDSC](#bkarrdsc) (BK_DESC_ prefix). Quote note lines.

## BKSAREPT
**REPORT NAMES FOR SA-M & SA-N**

Fields: 57 | Prefix: BKSA_

Saved report parameter sets for the Sales Analysis (SA) reports.
FROM1..26 = filter range start values; THRU1..26 = filter range end values (mixed types by parameter position).

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKSA_BASE | STRING | 1 | — | Base quantity/amount flag |
| 2 | BKSA_FROM1 | NUMERIC | 8 | — | Filter range from, param 1 (invoice/order number) |
| 3 | BKSA_FROM10 | STRING | 10 | — | Filter range from, param 10 (code) |
| 4 | BKSA_FROM11 | STRING | 30 | — | Filter range from, param 11 (name/desc) |
| 5 | BKSA_FROM12 | STRING | 30 | — | Filter range from, param 12 (name/desc) |
| 6 | BKSA_FROM13 | STRING | 4 | — | Filter range from, param 13 (dept) |
| 7 | BKSA_FROM14 | STRING | 4 | — | Filter range from, param 14 (dept) |
| 8 | BKSA_FROM15 | INTEGER | 2 | — | Filter range from, param 15 (integer code) |
| 9 | BKSA_FROM16 | INTEGER | 2 | — | Filter range from, param 16 (integer code) |
| 10 | BKSA_FROM17 | STRING | 10 | — | Filter range from, param 17 (code) |
| 11 | BKSA_FROM18 | STRING | 15 | — | Filter range from, param 18 (code/part) |
| 12 | BKSA_FROM19 | STRING | 25 | — | Filter range from, param 19 (description) |
| 13 | BKSA_FROM2 | DATE | 4 | — | Filter range from, param 2 (start date) |
| 14 | BKSA_FROM20 | NUMERIC | 8 | 2 | Filter range from, param 20 (amount) |
| 15 | BKSA_FROM21 | STRING | 15 | — | Filter range from, param 21 (code) |
| 16 | BKSA_FROM22 | STRING | 4 | — | Filter range from, param 22 (short code) |
| 17 | BKSA_FROM23 | DATE | 4 | — | Filter range from, param 23 (date) |
| 18 | BKSA_FROM24 | NUMERIC | 8 | 2 | Filter range from, param 24 (amount) |
| 19 | BKSA_FROM25 | NUMERIC | 8 | 2 | Filter range from, param 25 (amount) |
| 20 | BKSA_FROM26 | STRING | 3 | — | Filter range from, param 26 (currency) |
| 21 | BKSA_FROM3 | DATE | 4 | — | Filter range from, param 3 (end date) |
| 22 | BKSA_FROM4 | NUMERIC | 8 | — | Filter range from, param 4 (numeric key) |
| 23 | BKSA_FROM5 | STRING | 10 | — | Filter range from, param 5 (customer code) |
| 24 | BKSA_FROM6 | STRING | 10 | — | Filter range from, param 6 (code) |
| 25 | BKSA_FROM7 | STRING | 2 | — | Filter range from, param 7 (state/short code) |
| 26 | BKSA_FROM8 | STRING | 2 | — | Filter range from, param 8 (state/short code) |
| 27 | BKSA_FROM9 | STRING | 10 | — | Filter range from, param 9 (code) |
| 28 | BKSA_NAME | STRING | 15 | — | Saved report set name |
| 29 | BKSA_RTM | STRING | 15 | — | Report template name (.RTM) |
| 30 | BKSA_THRU1 | NUMERIC | 8 | — | Filter range thru, param 1 |
| 31 | BKSA_THRU10 | STRING | 10 | — | Filter range thru, param 10 |
| 32 | BKSA_THRU11 | STRING | 30 | — | Filter range thru, param 11 |
| 33 | BKSA_THRU12 | STRING | 30 | — | Filter range thru, param 12 |
| 34 | BKSA_THRU13 | STRING | 4 | — | Filter range thru, param 13 |
| 35 | BKSA_THRU14 | STRING | 4 | — | Filter range thru, param 14 |
| 36 | BKSA_THRU15 | INTEGER | 2 | — | Filter range thru, param 15 |
| 37 | BKSA_THRU16 | INTEGER | 2 | — | Filter range thru, param 16 |
| 38 | BKSA_THRU17 | STRING | 10 | — | Filter range thru, param 17 |
| 39 | BKSA_THRU18 | STRING | 15 | — | Filter range thru, param 18 |
| 40 | BKSA_THRU19 | STRING | 25 | — | Filter range thru, param 19 |
| 41 | BKSA_THRU2 | DATE | 4 | — | Filter range thru, param 2 |
| 42 | BKSA_THRU20 | NUMERIC | 8 | 2 | Filter range thru, param 20 |
| 43 | BKSA_THRU21 | STRING | 15 | — | Filter range thru, param 21 |
| 44 | BKSA_THRU22 | STRING | 4 | — | Filter range thru, param 22 |
| 45 | BKSA_THRU23 | DATE | 4 | — | Filter range thru, param 23 |
| 46 | BKSA_THRU24 | NUMERIC | 8 | 2 | Filter range thru, param 24 |
| 47 | BKSA_THRU25 | NUMERIC | 8 | 2 | Filter range thru, param 25 |
| 48 | BKSA_THRU26 | STRING | 3 | — | Filter range thru, param 26 |
| 49 | BKSA_THRU3 | DATE | 4 | — | Filter range thru, param 3 |
| 50 | BKSA_THRU4 | NUMERIC | 8 | — | Filter range thru, param 4 |
| 51 | BKSA_THRU5 | STRING | 10 | — | Filter range thru, param 5 |
| 52 | BKSA_THRU6 | STRING | 10 | — | Filter range thru, param 6 |
| 53 | BKSA_THRU7 | STRING | 2 | — | Filter range thru, param 7 |
| 54 | BKSA_THRU8 | STRING | 2 | — | Filter range thru, param 8 |
| 55 | BKSA_THRU9 | STRING | 10 | — | Filter range thru, param 9 |
| 56 | BKSA_TITLE | STRING | 40 | — | Report title |
| 57 | BKSA_TYPE | STRING | 8 | — | Report type code |

## BKSOHLOT
**INVOICE LOT CONTROL**

Identical schema to [BKARTXN](#bkartxn) (BKAR_TXN_ prefix). Posted/invoiced lot allocations.

## BKSOHSER
**INVOICE SERIAL CONTROL**

Identical schema to [BKARTXN](#bkartxn) (BKAR_TXN_ prefix). Posted/invoiced serial allocations.

## BKSOLOCK
**LOCK FILE FOR SO INVOICE POSTING**

Fields: 5

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKSO_LOCK_DATE | DATE | 4 | — | Lock date |
| 2 | BKSO_LOCK_ITEM | STRING | 25 | — | Item being locked |
| 3 | BKSO_LOCK_REC | STRING | 10 | — | Record identifier |
| 4 | BKSO_LOCK_TIME | TIME | 4 | — | Lock time |
| 5 | BKSO_LOCK_WHO | STRING | 25 | — | User holding the lock |

## BKSONOTE
**SALES ORDER ASSIGNED TEMPLATES**

Identical schema to [BKARRDSC](#bkarrdsc) (BK_DESC_ prefix). SO note template assignments.

## BKSOX
**SO DETAIL — ACCOUNTING DISABLED**

Fields: 25 | Prefix: BKSOX_

Flattened SO summary used when GL accounting integration is disabled.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKSOX_ARCHDATE | DATE | 4 | — | Archive date |
| 2 | BKSOX_COMPANY | STRING | 2 | — | Company code |
| 3 | BKSOX_CURRENCY | STRING | 3 | — | Currency code |
| 4 | BKSOX_CUSTCODE | STRING | 10 | — | Customer code |
| 5 | BKSOX_CUSTNAME | STRING | 30 | — | Customer name |
| 6 | BKSOX_CUSTPO | STRING | 25 | — | Customer PO number |
| 7 | BKSOX_DEPOSIT | NUMERIC | 8 | 2 | Deposit amount |
| 8 | BKSOX_ENTDATE | DATE | 4 | — | Entry date |
| 9 | BKSOX_FREIGHT | NUMERIC | 8 | 2 | Freight amount |
| 10 | BKSOX_INVCDATE | DATE | 4 | — | Invoice date |
| 11 | BKSOX_INVCDESC | STRING | 30 | — | Invoice description |
| 12 | BKSOX_INVCNUM | NUMERIC | 8 | — | Invoice number |
| 13 | BKSOX_JOBNUM | STRING | 15 | — | Job number |
| 14 | BKSOX_POSTDATE | DATE | 4 | — | GL post date |
| 15 | BKSOX_RETEN | NUMERIC | 8 | 2 | Retention amount |
| 16 | BKSOX_SHIPDATE | DATE | 4 | — | Ship date |
| 17 | BKSOX_SHIPPER | NUMERIC | 8 | — | Shipper number |
| 18 | BKSOX_SONUM | NUMERIC | 8 | — | SO number |
| 19 | BKSOX_SUBTOT | NUMERIC | 8 | 2 | Subtotal |
| 20 | BKSOX_TAXAMT | NUMERIC | 8 | 2 | Tax amount |
| 21 | BKSOX_TAXCODE | STRING | 10 | — | Tax code |
| 22 | BKSOX_TAXNAME | STRING | 30 | — | Tax name |
| 23 | BKSOX_TERMSCODE | INTEGER | 2 | — | Payment terms code |
| 24 | BKSOX_TERMSDESC | STRING | 20 | — | Payment terms description |
| 25 | BKSOX_TOTAL | NUMERIC | 8 | 2 | Total amount |

## BKSOXH
**SO DETAIL HISTORY — ACCOUNTING DISABLED**

Identical schema to [BKSOX](#bksox) (BKSOX_ prefix). Historical archive of SO detail (accounting disabled).

## DISCOUNT
**DISCOUNT TABLE MASTER**

Identical schema to [BKICPMAT](#bkicpmat) (BKIC_PMAT_ prefix). Discount schedule master records.

## INVETXN
**TEMP FILE FOR UNPOSTED INVENTORY TRANSACTIONS**

Fields: 24 | Prefix: MTIT_

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTIT_AVGCOST | NUMERIC | 8 | 4 | Average cost |
| 2 | MTIT_CLASS | STRING | 4 | — | Item class |
| 3 | MTIT_CODE | STRING | 15 | — | Inventory item code |
| 4 | MTIT_CUST | STRING | 10 | — | Customer code |
| 5 | MTIT_DATE | DATE | 4 | — | Transaction date |
| 6 | MTIT_DEPT | STRING | 4 | — | GL department |
| 7 | MTIT_DESC | STRING | 30 | — | Description |
| 8 | MTIT_EXTRA | STRING | 50 | — | Extra/custom data |
| 9 | MTIT_INVOICE | NUMERIC | 8 | — | Invoice number |
| 10 | MTIT_LOC | STRING | 10 | — | Warehouse location |
| 11 | MTIT_LOT | STRING | 15 | — | Lot ID |
| 12 | MTIT_PO | NUMERIC | 8 | — | PO number |
| 13 | MTIT_PRICE | NUMERIC | 8 | 4 | Unit price |
| 14 | MTIT_PRODLOT | STRING | 15 | — | Production lot ID |
| 15 | MTIT_QC | STRING | 2 | — | QC status code |
| 16 | MTIT_QTY | NUMERIC | 8 | 2 | Quantity |
| 17 | MTIT_REF | STRING | 30 | — | Reference |
| 18 | MTIT_SCRAP | STRING | 2 | — | Scrap code |
| 19 | MTIT_SERIAL | STRING | 25 | — | Serial number |
| 20 | MTIT_STDCST | NUMERIC | 8 | 6 | Standard cost |
| 21 | MTIT_TYPE | STRING | 1 | — | Transaction type |
| 22 | MTIT_VENDOR | STRING | 10 | — | Vendor code |
| 23 | MTIT_WOPRE | NUMERIC | 8 | — | Work order prefix |
| 24 | MTIT_WOSUF | INTEGER | 2 | — | Work order suffix |

## ISARADSC
**ARCHIVED CLOSED SALES ORDER NOTES**

Identical schema to [BKARRDSC](#bkarrdsc) (BK_DESC_ prefix). Archived SO note lines.

## ISARAHDS
**ARCHIVED INVOICE NOTES**

Identical schema to [BKARRDSC](#bkarrdsc) (BK_DESC_ prefix). Archived invoice note lines.

## ISARAHIL
**ARCHIVED INVOICE LINES**

Identical schema to [BKARINVL](#bkarinvl) (BKAR_INVL_ prefix). Archived invoice line items.

## ISARAHIN
**ARCHIVED INVOICE HEADERS**

Identical schema to [BKARINV](#bkarinv) (BKAR_INV_ prefix). Archived invoice headers.

## ISARAINV
**ARCHIVED CLOSED SALES ORDER HEADERS**

Identical schema to [BKARINV](#bkarinv) (BKAR_INV_ prefix). Archived closed/completed SO headers.

## ISARAIVL
**ARCHIVED CLOSED SALES ORDER LINES**

Identical schema to [BKARINVL](#bkarinvl) (BKAR_INVL_ prefix). Archived closed/completed SO lines.

## ISARATXN
**ARCHIVED LOT LINK TO INVOICE LINE**

Identical schema to [BKARTXN](#bkartxn) (BKAR_TXN_ prefix). Archived lot-to-line allocations.

## ISARATXS
**ARCHIVED SERIAL LINK TO INVOICE LINE**

Identical schema to [BKARTXN](#bkartxn) (BKAR_TXN_ prefix). Archived serial-to-line allocations.

## ISARCHG
**CHANGES TO SALES ORDERS**

Fields: 26 | Prefix: ISAR_CHG_

Change audit log: A_ = after-value fields, B_ = before-value fields.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISAR_CHG_AASD | DATE | 4 | — | After: actual ship date |
| 2 | ISAR_CHG_ACOMPR_1 | NUMERIC | 8 | 4 | After: salesperson 1 commission percent |
| 3 | ISAR_CHG_ACOMPR_2 | NUMERIC | 8 | 4 | After: salesperson 2 commission percent |
| 4 | ISAR_CHG_ADISC | NUMERIC | 8 | 2 | After: discount |
| 5 | ISAR_CHG_AESD | DATE | 4 | — | After: estimated ship date |
| 6 | ISAR_CHG_AEXTRA | STRING | 150 | — | After: extra data |
| 7 | ISAR_CHG_ALOC | STRING | 10 | — | After: location |
| 8 | ISAR_CHG_AOOQTY | NUMERIC | 8 | 2 | After: original order quantity |
| 9 | ISAR_CHG_APRICE | NUMERIC | 8 | 4 | After: price |
| 10 | ISAR_CHG_BASD | DATE | 4 | — | Before: actual ship date |
| 11 | ISAR_CHG_BCOMPR_1 | NUMERIC | 8 | 4 | Before: salesperson 1 commission percent |
| 12 | ISAR_CHG_BCOMPR_2 | NUMERIC | 8 | 4 | Before: salesperson 2 commission percent |
| 13 | ISAR_CHG_BDISC | NUMERIC | 8 | 2 | Before: discount |
| 14 | ISAR_CHG_BESD | DATE | 4 | — | Before: estimated ship date |
| 15 | ISAR_CHG_BEXTRA | STRING | 150 | — | Before: extra data |
| 16 | ISAR_CHG_BLOC | STRING | 10 | — | Before: location |
| 17 | ISAR_CHG_BOOQTY | NUMERIC | 8 | 2 | Before: original order quantity |
| 18 | ISAR_CHG_BPRICE | NUMERIC | 8 | 4 | Before: price |
| 19 | ISAR_CHG_CDATE | DATE | 4 | — | Change date |
| 20 | ISAR_CHG_INVNUM | NUMERIC | 8 | — | Invoice / order number |
| 21 | ISAR_CHG_LINEID | NUMERIC | 8 | — | Line item ID |
| 22 | ISAR_CHG_PCODE | STRING | 15 | — | Part code |
| 23 | ISAR_CHG_REVLVL | STRING | 10 | — | Revision level |
| 24 | ISAR_CHG_SONUM | NUMERIC | 8 | — | SO number |
| 25 | ISAR_CHG_UNUM | INTEGER | 4 | — | User number |
| 26 | ISAR_CHG_USER | STRING | 15 | — | User name who made the change |

## ISARHCHG
**ON TIME DELIVERY**

Identical schema to [ISARCHG](#isarchg) (ISAR_CHG_ prefix). On-time delivery tracking / change audit.

## ISARQCHG
**CHANGES TO QUOTES**

Identical schema to [ISARCHG](#isarchg) (ISAR_CHG_ prefix). Quote change audit log.

## ISARRCHG
**CHANGES TO RECURRING SO**

Identical schema to [ISARCHG](#isarchg) (ISAR_CHG_ prefix). Recurring SO change audit log.

## ISARTXNB
**BIN ALLOCATION TO SO LINE**

Fields: 23 | Prefix: ISAR_TXN_

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1–5 | ISAR_TXN_ALPHA_1..5 | STRING | 25 | — | Alpha user-defined fields 1–5 |
| 6 | ISAR_TXN_BIN | STRING | 15 | — | Bin location |
| 7 | ISAR_TXN_BOX | INTEGER | 2 | — | Box number |
| 8 | ISAR_TXN_CODE | STRING | 15 | — | Item code |
| 9 | ISAR_TXN_DATE | DATE | 4 | — | Allocation date |
| 10 | ISAR_TXN_EXTRA | STRING | 100 | — | Extra/custom data |
| 11–15 | ISAR_TXN_FLAG_1..5 | STRING | 1 | — | Boolean flags 1–5 |
| 16 | ISAR_TXN_LINEID | NUMERIC | 8 | — | SO line ID |
| 17 | ISAR_TXN_LOC | STRING | 10 | — | Warehouse location |
| 18 | ISAR_TXN_LOT | STRING | 15 | — | Lot ID |
| 19 | ISAR_TXN_QTY | NUMERIC | 8 | 2 | Quantity allocated |
| 20 | ISAR_TXN_RLEASD | STRING | 1 | — | Released flag (Y/N) |
| 21 | ISAR_TXN_SERIAL | STRING | 25 | — | Serial number |
| 22 | ISAR_TXN_SONUM | NUMERIC | 8 | — | SO number |
| 23 | ISAR_TXN_TMPSO | STRING | 40 | — | Temporary SO reference |

## ISBOLMS
**BILL OF LADING**

Identical schema to [ISSOBOX](#issobox) (ISSO_BOX_ prefix). Bill of lading / shipping manifest record.

## ISESTAQL
**ARCHIVE QUOTE LINES**

Identical schema to [BKARINVL](#bkarinvl) (BKAR_INVL_ prefix). Archived/closed quote line items.

## ISESTAQT
**ARCHIVE QUOTE HEADER**

Identical schema to [BKARINV](#bkarinv) (BKAR_INV_ prefix). Archived/closed quote headers.

## ISORDDSC
**SALES ORDER DESCRIPTION LIST**

Fields: 1

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IORD_DESC_CODE | STRING | 30 | — | Order description code / text |

## ISQSOA
**TEMP FILE FOR QUICK SO ENTRY**

Fields: 12 | Prefix: IS_QSOA_

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_QSOA_CUST | STRING | 10 | — | Customer code |
| 2 | IS_QSOA_DESC | STRING | 30 | — | Item description |
| 3 | IS_QSOA_DISC | NUMERIC | 8 | 2 | Discount percent |
| 4 | IS_QSOA_EXTRA | STRING | 50 | — | Extra/custom data |
| 5 | IS_QSOA_ITEM | STRING | 15 | — | Item / part code |
| 6 | IS_QSOA_MDATE1 | DATE | 4 | — | Must-deliver date 1 |
| 7 | IS_QSOA_MDATE2 | DATE | 4 | — | Must-deliver date 2 |
| 8 | IS_QSOA_PRICE | NUMERIC | 8 | 4 | Unit price |
| 9 | IS_QSOA_QTY | NUMERIC | 8 | 2 | Quantity ordered |
| 10 | IS_QSOA_SHPDTE | DATE | 4 | — | Ship date |
| 11 | IS_QSOA_SHPTO | STRING | 10 | — | Ship-to code |
| 12 | IS_QSOA_UID | STRING | 40 | — | Unique ID / user session ID |

## ISQTINFO
**SUPPLEMENTAL QUOTE INFO**

Identical schema to [ISSOINFO](#issoinfo) (ISSR_INFO_ prefix). Supplemental user-defined fields for quotes.

## ISSOABOX
**ARCHIVED SHIPPING DETAIL**

Identical schema to [ISSOBOX](#issobox) (ISSO_BOX_ prefix). Archived shipping/box detail.

## ISSOAHBX
**ARCHIVED INVOICE BOX ALLOCATION**

Identical schema to [ISSOBOX](#issobox) (ISSO_BOX_ prefix). Archived invoice box allocation records.

## ISSOAINF
**ARCHIVED SOA INFO**

Identical schema to [ISSOINFO](#issoinfo) (ISSR_INFO_ prefix). Archived supplemental SO info.

## ISSOALOT
**ARCHIVED INVOICE LOT CONTROL**

Identical schema to [BKARTXN](#bkartxn) (BKAR_TXN_ prefix). Archived invoice lot control records.

## ISSOASER
**ARCHIVED INVOICE SERIAL CONTROL**

Identical schema to [BKARTXN](#bkartxn) (BKAR_TXN_ prefix). Archived invoice serial control records.

## ISSOBOX
**SHIPPING DETAIL**

Fields: 22 | Prefix: ISSO_BOX_

Per-line, per-box shipping carton detail for ASN / Bill of Lading.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISSO_BOX_BOX | INTEGER | 2 | — | Box number |
| 2 | ISSO_BOX_CODE | STRING | 15 | — | Item code |
| 3 | ISSO_BOX_DATE | DATE | 4 | — | Shipping date |
| 4 | ISSO_BOX_EXTRA | STRING | 150 | — | Extra/custom data |
| 5 | ISSO_BOX_HT | NUMERIC | 8 | 2 | Height (dimension) |
| 6 | ISSO_BOX_INVNUM | NUMERIC | 8 | — | Invoice number |
| 7 | ISSO_BOX_LG | NUMERIC | 8 | 2 | Length (dimension) |
| 8 | ISSO_BOX_LINE | NUMERIC | 8 | — | Line number |
| 9 | ISSO_BOX_LOT | STRING | 15 | — | Lot ID |
| 10 | ISSO_BOX_QTY | NUMERIC | 8 | 2 | Quantity in box |
| 11 | ISSO_BOX_SERIAL | STRING | 25 | — | Serial number |
| 12 | ISSO_BOX_SHIPPR | NUMERIC | 8 | — | Shipper number |
| 13 | ISSO_BOX_SHPCOD | STRING | 10 | — | Ship-to code |
| 14 | ISSO_BOX_SKID | INTEGER | 2 | — | Skid / pallet number |
| 15 | ISSO_BOX_SONUM | NUMERIC | 8 | — | SO number |
| 16 | ISSO_BOX_TEMP | STRING | 1 | — | Temperature-controlled flag (Y/N) |
| 17 | ISSO_BOX_TRACK | STRING | 40 | — | Carrier tracking number |
| 18 | ISSO_BOX_UCC | STRING | 30 | — | UCC-128 barcode |
| 19 | ISSO_BOX_WD | NUMERIC | 8 | 2 | Width (dimension) |
| 20 | ISSO_BOX_WEIGHT | NUMERIC | 8 | 2 | Weight |
| 21 | ISSO_BOX_WOPRE | NUMERIC | 8 | — | Work order prefix |
| 22 | ISSO_BOX_WOSUF | INTEGER | 2 | — | Work order suffix |

## ISSOHNFO
**INVOICE SUPPLEMENTAL INFO**

Identical schema to [ISSOINFO](#issoinfo) (ISSR_INFO_ prefix). Supplemental user-defined fields for invoices.

## ISSOHBOX
**SHIPPED BOX ID**

Identical schema to [ISSOBOX](#issobox) (ISSO_BOX_ prefix). Shipped box ID records.

## ISSOINFO
**SALES ORDER SUPPLEMENTAL INFO**

Fields: 54 | Prefix: ISSR_INFO_

User-defined supplemental fields attached to SOs, invoices, and quotes.
AL1..20 = short alpha label/header fields; ALPHA_1..20 = full alpha value fields.
DATE1..5 and DATE_1..5 = two parallel sets of 5 date UDFs (legacy + extended).

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1–20 | ISSR_INFO_AL1..20 | STRING | 25 | — | Alpha UDF label/header fields 1–20 (short form) |
| 21–40 | ISSR_INFO_ALPHA_1..20 | STRING | 25 | — | Alpha UDF value fields 1–20 (full form) |
| 41 | ISSR_INFO_CODE | STRING | 15 | — | SO / quote number (FK) |
| 42–46 | ISSR_INFO_DATE1..5 | DATE | 4 | — | Date UDFs 1–5 (legacy form) |
| 47–51 | ISSR_INFO_DATE_1..5 | DATE | 4 | — | Date UDFs 1–5 (extended form) |
| 52 | ISSR_INFO_EXTRA | STRING | 100 | — | Extra/custom data |
| 53 | ISSR_INFO_SRNUM | NUMERIC | 8 | — | Record number |
| 54 | ISSR_INFO_UID | NUMERIC | 8 | — | Unique ID |

## ISSRAINV
**ARCHIVED SALES ORDER HEADER**

Identical schema to [BKARINV](#bkarinv) (BKAR_INV_ prefix). Archived sales order headers (secondary archive).

## ISSRAIVL
**ARCHIVED SALES ORDER LINE**

Identical schema to [BKARINVL](#bkarinvl) (BKAR_INVL_ prefix). Archived sales order lines (secondary archive).

## NOTETEMP
**SALES ORDER NOTE TEMPLATES**

Identical schema to [BKARRDSC](#bkarrdsc) (BK_DESC_ prefix). Note template lines for SO.
