# Tier 1 Table Documentation
Status: partial | verified-schema | open-questions

Complete field lists for the most critical EvoERP tables, extracted from `samples/ddf/schema.md`.
Field meanings are inferred from names unless noted as confirmed.

---

## AHSYLOG — User Security

File: `AHSYLOG.B` | Module: Security | Fields: 23

| # | Field | Type | Size | Meaning |
|---|-------|------|------|---------|
| 1 | AHSY_USER_LEVL | STRING | 2 | Role / security level code |
| 2 | AHSY_USER_MENU | STRING | 4 | Starting menu code after login (e.g., "AR-A") |
| 3 | AHSY_USER_CTRL | STRING | 1 | Control flag (meaning not decoded) |
| 4 | AHSY_USER_ACCES_1 | STRING | 1 | Module permission flag #1 |
| 5 | AHSY_USER_ACCES_2 | STRING | 1 | Module permission flag #2 |
| 6–23 | AHSY_USER_ACCES_3..20 | STRING | 1 each | Module permission flags #3–20 |

**Notes:**
- This is the primary user/security table. One record per user.
- Password is stored in BKLOGON, not here.
- The 20 ACCES flags map to specific modules but the module→flag index is not yet confirmed.
- AHSY_USER_LEVL 2-char code: exact values and meanings not decoded.

**Open questions:** What are the LEVL values? What module does each ACCES_N control?

---

## BKARCUST — AR Customer Master

File: `BKARCUST.B` | Module: AR | Fields: 106

Key fields (extracted from schema; full list in `samples/ddf/schema.md`):

| # | Field | Type | Size | Meaning |
|---|-------|------|------|---------|
| 1 | BKAR_CUST_CODE | STRING | 10 | Customer code — primary key |
| 2 | BKAR_CUST_ALPHA | STRING | 10 | Alpha sort key |
| 3 | BKAR_CUST_NAME | STRING | 30 | Company name |
| 4 | BKAR_CUST_ADDR1 | STRING | 30 | Address line 1 |
| 5 | BKAR_CUST_ADDR2 | STRING | 30 | Address line 2 |
| 6 | BKAR_CUST_ADDR3 | STRING | 30 | Address line 3 (extended) |
| 7 | BKAR_CUST_CITY | STRING | 20 | City |
| 8 | BKAR_CUST_STATE | STRING | 2 | State |
| 9 | BKAR_CUST_ZIP | STRING | 10 | ZIP / postal code |
| 10 | BKAR_CUST_COUNTRY | STRING | 20 | Country |
| 11 | BKAR_CUST_PHONE | STRING | 20 | Main phone |
| 12 | BKAR_CUST_FAX | STRING | 20 | Fax |
| 13 | BKAR_CUST_EMAIL | STRING | 50 | Email |
| 14 | BKAR_CUST_WEBSITE | STRING | 50 | Website URL |
| 15 | BKAR_CUST_GLSALE | STRING | 8 | Default GL sales account |
| 16 | BKAR_CUST_CLASS | STRING | 4 | Customer class code |
| 17 | BKAR_CUST_TERRIT | STRING | 4 | Sales territory |
| 18 | BKAR_CUST_SLSP1 | STRING | 4 | Salesperson 1 code |
| 19 | BKAR_CUST_COMM1 | FLOAT | 8 | Salesperson 1 commission rate |
| 20 | BKAR_CUST_SLSP2 | STRING | 4 | Salesperson 2 code |
| 21 | BKAR_CUST_COMM2 | FLOAT | 8 | Salesperson 2 commission rate |
| 22 | BKAR_CUST_TERMS | STRING | 2 | Payment terms code |
| 23 | BKAR_CUST_PRICE | STRING | 4 | Price code |
| 24 | BKAR_CUST_DISC | STRING | 4 | Discount code |
| 25 | BKAR_CUST_TAXBLE | STRING | 1 | Taxable flag (Y/N) |
| 26 | BKAR_CUST_TAXGRP | STRING | 4 | Tax group code |
| 27 | BKAR_CUST_CRLMT | FLOAT | 8 | Credit limit |
| 28 | BKAR_CUST_CHOLD | STRING | 1 | Credit hold flag |
| 29 | BKAR_CUST_STRTDT | DATE | 4 | Customer start date |
| 30 | BKAR_CUST_LSTPMT | DATE | 4 | Last payment date |
| 31 | BKAR_CUST_LSTINV | DATE | 4 | Last invoice date |
| 32 | BKAR_CUST_BKORD | STRING | 1 | Backorders allowed flag |
| 33 | BKAR_CUST_INTCHG | STRING | 1 | Charge interest flag (Y = yes) |
| 34 | BKAR_CUST_INTRT | FLOAT | 8 | Interest rate |
| 35 | BKAR_CUST_SHIPTO | STRING | 4 | Default ship-to code |
| 36 | BKAR_CUST_SHIVIA | STRING | 10 | Default ship via |
| 37 | BKAR_CUST_FOB | STRING | 15 | FOB point |
| 38 | BKAR_CUST_LEAD | STRING | 4 | Lead source code |
| 39 | BKAR_CUST_GROUP | STRING | 4 | Customer group |
| 40 | BKAR_CUST_RESALE | STRING | 15 | Resale number |
| … | (66 more fields) | | | Contact manager, outstanding balances, notes flags, currency |

**Notes:**
- BKAR_CUST_CODE is the primary key used in BKARINV, BKARCASH, and all AR transactions.
- Outstanding balance totals are maintained on the customer record (denormalized for speed).
- The full 106-field list is in `samples/ddf/schema.md` under `## BKARCUST`.

---

## BKARINV — AR Invoice Header

File: `BKARINV.B` | Module: AR | Fields: 84

Key fields:

| # | Field | Type | Meaning |
|---|-------|------|---------|
| 1 | BKAR_INV_NUM | FLOAT | Invoice number — primary key (auto-increment from BKSYMSTR) |
| 2 | BKAR_INV_CUST | STRING | Customer code (FK → BKARCUST) |
| 3 | BKAR_INV_DATE | DATE | Invoice date |
| 4 | BKAR_INV_PSTDT | DATE | Post date |
| 5 | BKAR_INV_DUEDT | DATE | Due date (calculated from terms) |
| 6 | BKAR_INV_TYPE | STRING | Transaction type (I=invoice, C=credit memo, etc.) |
| 7 | BKAR_INV_TERMS | STRING | Terms code |
| 8 | BKAR_INV_SUBTOT | FLOAT | Subtotal (before tax/freight) |
| 9 | BKAR_INV_TAX | FLOAT | Tax amount |
| 10 | BKAR_INV_FRET | FLOAT | Freight amount |
| 11 | BKAR_INV_TOTAL | FLOAT | Invoice total |
| 12 | BKAR_INV_PAID | FLOAT | Amount paid to date |
| 13 | BKAR_INV_BAL | FLOAT | Remaining balance |
| 14 | BKAR_INV_GLSALE | STRING | GL sales account |
| 15 | BKAR_INV_GLDEPT | STRING | GL department |
| 16 | BKAR_INV_COGS | FLOAT | Cost of goods sold amount |
| 17 | BKAR_INV_SONO | FLOAT | SO number link |
| 18 | BKAR_INV_SHIP | STRING | Ship-to code |
| 19 | BKAR_INV_SHIVIA | STRING | Ship via |
| 20 | BKAR_INV_TRCKNO | STRING | Tracking number |
| … | (64 more fields) | | Discount, retention, deposit, currency, salesperson, tax group, archive flags |

---

## BKARINVL — AR Invoice Lines

File: `BKARINVL.B` | Module: AR | Fields: 28

| # | Field | Type | Size | Meaning |
|---|-------|------|------|---------|
| 1 | BKAR_INVL_NUM | FLOAT | 8 | Invoice number (FK → BKARINV) |
| 2 | BKAR_INVL_CNTR | UBINARY | 2 | Line counter (PK with invoice#) |
| 3 | BKAR_INVL_PROD | STRING | 15 | Product code |
| 4 | BKAR_INVL_DESC | STRING | 30 | Line description |
| 5 | BKAR_INVL_QTY | FLOAT | 8 | Quantity |
| 6 | BKAR_INVL_PRICE | FLOAT | 8 | Unit price |
| 7 | BKAR_INVL_DISC | FLOAT | 8 | Discount percentage |
| 8 | BKAR_INVL_EXT | FLOAT | 8 | Extended amount (qty × price × discount) |
| 9 | BKAR_INVL_TAX | FLOAT | 8 | Tax amount for this line |
| 10 | BKAR_INVL_FRET | FLOAT | 8 | Freight for this line |
| 11 | BKAR_INVL_GLSALE | STRING | 8 | GL sales account override |
| 12 | BKAR_INVL_GLDEPT | STRING | 4 | GL department |
| 13 | BKAR_INVL_TAXBL | STRING | 1 | Taxable flag for this line |
| 14 | BKAR_INVL_SONO | FLOAT | 8 | SO number (if from SO) |
| 15 | BKAR_INVL_SOLINE | UBINARY | 2 | SO line number |
| 16 | BKAR_INVL_UOM | STRING | 4 | Unit of measure |
| 17 | BKAR_INVL_COGS | FLOAT | 8 | COGS for this line |
| 18–28 | (additional fields) | | | Commission, lot, serial, class, category |

---

## BKAPVEND — AP Vendor Master

File: `BKAPVEND.B` | Module: AP | Fields: 26+

| # | Field | Type | Meaning |
|---|-------|------|---------|
| 1 | BKAP_VEND_CODE | STRING | Vendor code — primary key |
| 2 | BKAP_VEND_ALPHA | STRING | Alpha sort key |
| 3 | BKAP_VEND_NAME | STRING | Vendor company name |
| 4 | BKAP_VEND_ADDR1 | STRING | Address line 1 |
| 5 | BKAP_VEND_ADDR2 | STRING | Address line 2 |
| 6 | BKAP_VEND_CITY | STRING | City |
| 7 | BKAP_VEND_STATE | STRING | State |
| 8 | BKAP_VEND_ZIP | STRING | ZIP code |
| 9 | BKAP_VEND_PHONE | STRING | Phone |
| 10 | BKAP_VEND_FAX | STRING | Fax |
| 11 | BKAP_VEND_TERMS | STRING | Payment terms code |
| 12 | BKAP_VEND_GLAP | STRING | Default GL AP account |
| 13 | BKAP_VEND_LSTPMT | DATE | Last payment date |
| 14 | BKAP_VEND_LSTPMA | FLOAT | Last payment amount |
| 15 | BKAP_VEND_YTDPUR | FLOAT | Year-to-date purchases |
| 16 | BKAP_VEND_OUTINV | FLOAT | Outstanding invoice balance |
| 17 | BKAP_VEND_OUTCRD | FLOAT | Outstanding credits |
| 18 | BKAP_VEND_1099 | STRING | 1099 type code |
| 19 | BKAP_VEND_TAXID | STRING | Tax ID / EIN for 1099 |
| 20 | BKAP_VEND_CONT | STRING | Contact name |
| 21–26 | (additional fields) | | Discount, currency, notes flags, class |

**Note:** AP uses "VEND" not "CUST" for vendor records. There is no BKAPCUST — vendors are BKAPVEND.

---

## BKAPINVL — AP Invoice / Voucher

File: `BKAPINVL.B` | Module: AP | Fields: 36+

This is a flat table (single table for both header and lines, unlike AR which splits to BKARINV + BKARINVL).

| # | Field | Type | Meaning |
|---|-------|------|---------|
| 1 | BKAP_INVL_VEND | STRING | Vendor code (FK → BKAPVEND) |
| 2 | BKAP_INVL_INVC | STRING | Invoice number (from vendor's invoice) |
| 3 | BKAP_INVL_DATE | DATE | Invoice date |
| 4 | BKAP_INVL_PSTDT | DATE | Post date |
| 5 | BKAP_INVL_DUEDT | DATE | Due date |
| 6 | BKAP_INVL_DESC | STRING | Description |
| 7 | BKAP_INVL_TERMS | STRING | Terms code |
| 8 | BKAP_INVL_TYPE | STRING | Type (A=voucher, B=credit, etc.) |
| 9 | BKAP_INVL_AMT | FLOAT | Total amount |
| 10 | BKAP_INVL_DISC | FLOAT | Discount amount available |
| 11 | BKAP_INVL_PAID | FLOAT | Amount paid |
| 12 | BKAP_INVL_BAL | FLOAT | Remaining balance |
| 13–38 | BKAP_INVL_GL1..GL26 | STRING × 26 | GL distribution accounts (up to 26 per voucher) |
| 39+ | (dept, amount for each GL account) | | |

---

## BKAPCHKH — AP Check Header

File: `BKAPCHKH.B` | Module: AP | Fields: 12

| # | Field | Type | Meaning |
|---|-------|------|---------|
| 1 | BKAP_CHK_VEND | STRING | Vendor code |
| 2 | BKAP_CHK_INVNUM | FLOAT | Internal invoice number |
| 3 | BKAP_CHK_AMT | FLOAT | Check amount |
| 4 | BKAP_CHK_DISC | FLOAT | Discount taken |
| 5 | BKAP_CHK_NET | FLOAT | Net payment amount |
| 6 | BKAP_CHK_DATE | DATE | Check date |
| 7 | BKAP_CHK_NUM | FLOAT | Check number |
| 8 | BKAP_CHK_BANK | STRING | Bank account code |
| 9 | BKAP_CHK_CURR | STRING | Currency code |
| 10 | BKAP_CHK_RATE | FLOAT | Exchange rate |
| 11 | BKAP_CHK_ORIG | FLOAT | Original amount (foreign currency) |
| 12 | BKAP_CHK_VOID | STRING | Void flag |

---

## BKICMSTR — Inventory Item Master

File: `BKICMSTR.B` | Module: IN | Fields: 64

| # | Field | Type | Meaning |
|---|-------|------|---------|
| 1 | BKIC_PROD_CODE | STRING | Product/part number — primary key |
| 2 | BKIC_PROD_DESC | STRING | Description line 1 |
| 3 | BKIC_PROD_DESC2 | STRING | Description line 2 |
| 4 | BKIC_PROD_TYPE | STRING | Item type code |
| 5 | BKIC_PROD_CLASS | STRING | Class code |
| 6 | BKIC_PROD_CAT | STRING | Category code |
| 7 | BKIC_PROD_UOM | STRING | Stock unit of measure |
| 8 | BKIC_PROD_PUOM | STRING | Purchase unit of measure |
| 9 | BKIC_PROD_PRCUOM | STRING | Price unit of measure |
| 10 | BKIC_PROD_PCVT | FLOAT | Purchase UOM conversion factor |
| 11 | BKIC_PROD_COST | FLOAT | Standard/current cost |
| 12 | BKIC_PROD_PRICE | FLOAT | Base selling price |
| 13 | BKIC_PROD_UOH | FLOAT | Units on hand (quantity in stock) |
| 14 | BKIC_PROD_UONORD | FLOAT | Units on order (open POs) |
| 15 | BKIC_PROD_UONSO | FLOAT | Units on sales orders (committed) |
| 16 | BKIC_PROD_UONWO | FLOAT | Units on work orders |
| 17 | BKIC_PROD_REODR | FLOAT | Reorder level (triggers planned PO in MRP) |
| 18 | BKIC_PROD_MINOQ | FLOAT | Minimum order quantity |
| 19 | BKIC_PROD_LTDAYS | FLOAT | Lead time in days |
| 20 | BKIC_PROD_WEIGHT | FLOAT | Weight per unit |
| 21 | BKIC_PROD_FTFCTR | FLOAT | Foot factor (for dimensional items) |
| 22 | BKIC_PROD_STDPK | FLOAT | Standard pack quantity |
| 23 | BKIC_PROD_FRETPCT | FLOAT | Freight percentage |
| 24 | BKIC_PROD_BIN | STRING | Bin/location code |
| 25 | BKIC_PROD_DRAW | STRING | Drawing number |
| 26 | BKIC_PROD_REVLVL | STRING | Revision level |
| 27 | BKIC_PROD_UPC | STRING | UPC / barcode |
| 28 | BKIC_PROD_DELBUF | FLOAT | Delay buffer days (MRP) |
| 29 | BKIC_PROD_PLNR | STRING | Planner code |
| 30 | BKIC_PROD_MRPSW | STRING | MRP planning switch (Y = include) |
| 31 | BKIC_PROD_GLINV | STRING | GL inventory account |
| 32 | BKIC_PROD_GLCOGS | STRING | GL cost of goods sold account |
| 33 | BKIC_PROD_GLVAR | STRING | GL variance account |
| 34 | BKIC_PROD_TAXBL | STRING | Taxable flag |
| 35 | BKIC_PROD_TAXGRP | STRING | Tax group |
| 36 | BKIC_PROD_ACTSTS | STRING | Active status |
| 37 | BKIC_PROD_STRTDT | DATE | Start date |
| 38 | BKIC_PROD_LSTPRC | DATE | Last price change date |
| 39 | BKIC_PROD_LSTCST | DATE | Last cost change date |
| 40 | BKIC_PROD_LSTRCV | DATE | Last receipt date |
| 41 | BKIC_PROD_LSTSLS | DATE | Last sale date |
| 41 | BKIC_PROD_GLA | STRING | GL Account — Inventory Asset |
| 42 | BKIC_PROD_DPTA | STRING | GL Dept — Inventory Asset |
| 43 | BKIC_PROD_GLC | STRING | GL Account — COGS |
| 44 | BKIC_PROD_DPTC | STRING | GL Dept — COGS |
| 45 | BKIC_PROD_GLS | STRING | GL Account — Scrap |
| 46 | BKIC_PROD_DPTS | STRING | GL Dept — Scrap |
| 47 | BKIC_PROD_PRICE | FLOAT | Base selling price (4 dec) |
| 48 | BKIC_PROD_GLSNT | STRING | GL Account — Non-Tax Sales |
| 49 | BKIC_PROD_DPTNT | STRING | GL Dept — Non-Tax Sales |
| 50 | BKIC_PROD_UBO | FLOAT | Units on Backorder |
| 51 | BKIC_PROD_PMAT | UBINARY | Preferred material flag |
| 52 | BKIC_PROD_MANUF | STRING | Manufacturer |
| 53 | BKIC_PROD_NOTE | STRING | Notes |
| 54 | BKIC_PROD_AVLAB | FLOAT | Absorbed Labor cost |
| 55 | BKIC_PROD_AVSET | FLOAT | Absorbed Setup cost |
| 56 | BKIC_PROD_AVOP | FLOAT | Absorbed Operations cost |
| 57 | BKIC_PROD_AVMAT | FLOAT | Absorbed Material cost |
| 58 | BKIC_PROD_AVFO | FLOAT | Absorbed Fixed Overhead |
| 59 | BKIC_PROD_AVVO | FLOAT | Absorbed Variable Overhead |
| 60 | BKIC_PROD_EXTRA | STRING | Extra/User-defined fields |
| 61 | BKIC_PROD_TAXIN | STRING | Tax include flag |
| 62 | BKIC_PROD_ISUPC | STRING | UPC Code |
| 63–64 | (RLVL, RAMT) | FLOAT | Reorder level, Reorder amount (renamed in DDF variant) |

---

## BKGLCOA — GL Chart of Accounts

File: `BKGLCOA.B` | Module: GL | Fields: 65

| # | Field | Type | Meaning |
|---|-------|------|---------|
| 1 | BKGL_COA_ACCT | STRING | Account code — PK component |
| 2 | BKGL_COA_DEPT | STRING | Department code — PK component |
| 3 | BKGL_COA_DESC | STRING | Account description |
| 4 | BKGL_COA_TYPE | STRING | Account type (A=asset, L=liability, E=equity, R=revenue, X=expense) |
| 5 | BKGL_COA_CRDR | STRING | Normal balance side (C=credit, D=debit) |
| 6–19 | BKGL_COA_BAL1..BAL14 | FLOAT × 14 | Current period balances (periods 1–14) |
| 20–33 | BKGL_COA_BUD1..BUD14 | FLOAT × 14 | Budget amounts (periods 1–14) |
| 34–47 | BKGL_COA_PY1..PY14 | FLOAT × 14 | Prior-year balances (periods 1–14) |
| 48–61 | BKGL_COA_YE1..YE4 | FLOAT × 4 | Year-end balances (4 slots) |
| 62 | BKGL_COA_PY2BAL1 | FLOAT | 2-years-prior balance period 1 |
| 63 | BKGL_COA_EXTRA | STRING | Extra field |
| 64–65 | (additional) | | |

**Notes:**
- Period 1–12 = accounting months; periods 13–14 = adjustment periods.
- Budget and prior-year amounts are stored inline (denormalized for fast balance sheet queries).
- Primary key is composite: BKGL_COA_ACCT + BKGL_COA_DEPT.

---

## WORKORD — Work Order Master

File: `WORKORD.B` | Module: WO | Fields: 74

| # | Field | Type | Meaning |
|---|-------|------|---------|
| 1 | WO_PREFIX | STRING | WO number prefix (PK component) |
| 2 | WO_SUFFIX | STRING | WO number suffix (PK component) |
| 3 | WO_BLANK | STRING | Blank / padding field |
| 4 | WO_MULT | FLOAT | Multiplier (for multi-assembly WOs) |
| 5 | WO_QTY | FLOAT | Quantity to make |
| 6 | WO_PRIORITY | STRING | Priority (1, 2, or 3) |
| 7 | WO_SCHED_START | DATE | Scheduled start date |
| 8 | WO_SCHED_FINISH | DATE | Scheduled finish date |
| 9 | WO_ACTUAL_START | DATE | Actual start date |
| 10 | WO_ACTUAL_FINISH | DATE | Actual finish date |
| 11 | WO_DUE_DATE | DATE | Customer due date |
| 12 | WO_QTY_COMP | FLOAT | Quantity completed to date |
| 13 | WO_STATUS | STRING | Status (S=Scheduled, F=Firmed, R=Released, C=Closed, X=Cancelled) |
| 14 | WO_LOCK | STRING | Record lock flag |
| 15 | WO_EST_LAB | FLOAT | Estimated labor cost |
| 16 | WO_EST_MAT | FLOAT | Estimated material cost |
| 17 | WO_EST_OVH | FLOAT | Estimated overhead cost |
| 18 | WO_EST_OUT | FLOAT | Estimated outside process cost |
| 19 | WO_ACT_LAB | FLOAT | Actual labor cost to date |
| 20 | WO_ACT_MAT | FLOAT | Actual material cost to date |
| 21 | WO_ACT_OVH | FLOAT | Actual overhead cost to date |
| 22 | WO_ACT_OUT | FLOAT | Actual outside process cost to date |
| 23 | WO_CUST_ORD | STRING | Customer order / SO number |
| 24–33 | WO_INSTR1..10 | STRING × 10 | Work order instructions (10 lines) |
| 34 | WO_SCHED_FLAG | STRING | Schedule flag |
| 35 | WO_SCRAP_QTY | FLOAT | Scrap quantity |
| 36 | WO_PART | STRING | Part number to produce |
| 37 | WO_CLASS | STRING | Work order class code |
| 38 | WO_JOB | STRING | Job number |
| … | (36 more fields) | | Location, description, schedule slots, extra cost categories |

---

## WORKCHG — Work Order Change Log

File: `WORKCHG.B` | Module: WO | Fields: 25

| # | Field | Type | Meaning |
|---|-------|------|---------|
| 1 | WCH_WO_PRE | STRING | WO prefix (FK → WORKORD) |
| 2 | WCH_WO_SUF | STRING | WO suffix |
| 3 | WCH_CHNG_CODE | STRING | Change code (what changed) |
| 4 | WCH_CHNG_DATE | DATE | Date of change |
| 5 | WCH_USER | STRING | User who made the change |
| 6 | WCH_BEFORE_PRI | STRING | Priority before change |
| 7 | WCH_AFTER_PRI | STRING | Priority after change |
| 8 | WCH_BEFORE_STS | STRING | Status before change |
| 9 | WCH_AFTER_STS | STRING | Status after change |
| 10 | WCH_BEFORE_CLS | STRING | Class before change |
| 11 | WCH_AFTER_CLS | STRING | Class after change |
| 12 | WCH_BEFORE_DESC | STRING | Description before change |
| 13 | WCH_AFTER_DESC | STRING | Description after change |
| 14 | WCH_BEFORE_QTY | FLOAT | Quantity before change |
| 15 | WCH_AFTER_QTY | FLOAT | Quantity after change |
| 16 | WCH_BEFORE_SSTART | DATE | Sched start before |
| 17 | WCH_AFTER_SSTART | DATE | Sched start after |
| 18 | WCH_BEFORE_SFIN | DATE | Sched finish before |
| 19 | WCH_AFTER_SFIN | DATE | Sched finish after |
| 20–25 | (additional flags) | | Extra note fields |

---

## BKLOGON — Active Sessions

File: `BKLOGON.B` | Module: Security | Fields: 10

| # | Field | Type | Meaning |
|---|-------|------|---------|
| 1 | BKLOG_CODE | STRING | User code — primary key |
| 2 | BKLOG_PASS | STRING | Password (encrypted) |
| 3 | BKLOG_COMP | STRING | Company code currently logged into |
| 4 | BKLOG_PROG | STRING | Current program running |
| 5 | BKLOG_PRINT | STRING | Default printer |
| 6 | BKLOG_INUSE | STRING | In-use / logged-in flag |
| 7 | BKLOG_LEVL | STRING | Security level (from AHSYLOG) |
| 8 | BKLOG_MENU | STRING | Starting menu code |
| 9 | BKLOG_SUBMNU | STRING | Current sub-menu position |
| 10 | BKLOG_CURPRT | STRING | Currently selected printer |

---

## BKSYMSTR — System Master Configuration

File: `BKSYMSTR.B` | Module: System | Fields: 286

This is a single-record global configuration table. One record exists per company.
Field names follow `BKSY_*` prefix convention.

Key configuration areas (from schema field names):
- **AR/AP/PO counters:** Next invoice number, next PO number (auto-increment)
- **Tax:** Default tax rate
- **Terms (20 slots):** Each term has: amount, type, days, EOM flag, maximum
- **Check accounts (per bank):** Account balance, name, GL account, GL department
- **AR/AP/PR check accounts:** Separate bank account assignments per module
- **AR SO counter:** Next sales order number
- **Freight GL accounts:** Default freight income and expense accounts
- **Aging buckets:** 4 bucket definitions (days threshold per bucket)
- **PR optional deductions:** Payroll deduction setup
- **Record numbers:** Various auto-increment sequence counters
- **Discount rates:** Default discount percentages
- **PO accounts:** Default GL accounts for PO receipts
- **Currency codes:** Multi-currency rate tables

*(Full 286-field list in `samples/ddf/schema.md` under `## BKSYMSTR`)*

---

## BKSOX — Sales Order Extract / Invoice

File: `BKSOX.B` | Module: SO | Fields: 25

| # | Field | Type | Meaning |
|---|-------|------|---------|
| 1 | BKSO_X_COMP | STRING | Company code |
| 2 | BKSO_X_INVC | FLOAT | Invoice number |
| 3 | BKSO_X_DATE | DATE | Invoice date |
| 4 | BKSO_X_CUST | STRING | Customer code (FK → BKARCUST) |
| 5 | BKSO_X_NAME | STRING | Customer name (denormalized) |
| 6 | BKSO_X_SUBTOT | FLOAT | Subtotal |
| 7 | BKSO_X_TAX | FLOAT | Tax amount |
| 8 | BKSO_X_FRET | FLOAT | Freight |
| 9 | BKSO_X_DEPOS | FLOAT | Deposit applied |
| 10 | BKSO_X_RETEN | FLOAT | Retention amount |
| 11 | BKSO_X_TOTAL | FLOAT | Invoice total |
| 12 | BKSO_X_CURR | STRING | Currency code |
| 13 | BKSO_X_SONO | FLOAT | Sales order number |
| 14 | BKSO_X_CUSTPO | STRING | Customer's PO number |
| 15 | BKSO_X_TERMS | STRING | Terms code |
| 16 | BKSO_X_TERMSDESC | STRING | Terms description (denormalized) |
| 17 | BKSO_X_INVCCODE | STRING | Invoice code |
| 18 | BKSO_X_INVCDESC | STRING | Invoice description |
| 19 | BKSO_X_SHIPDT | DATE | Ship date |
| 20 | BKSO_X_SHIPPER | STRING | Shipping carrier |
| 21 | BKSO_X_JOB | STRING | Job number |
| 22 | BKSO_X_TAXCODE | STRING | Tax code |
| 23 | BKSO_X_TAXNAME | STRING | Tax name (denormalized) |
| 24 | BKSO_X_PSTDT | DATE | Post date |
| 25 | BKSO_X_ENTDT | DATE | Entry date |

**Note:** BKSOXH has the same 25-field structure (header variant of the same data).

---

*Document generated: 2026-06-11*
*Source: `samples/ddf/schema.md` + SRC analysis + DFM analysis*
*Confidence: 68/100 — Field names and types confirmed from DDF schema. Field meanings inferred from naming conventions and confirmed where SRC source code references the fields directly.*
