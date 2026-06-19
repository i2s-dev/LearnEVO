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

File: `BKARCUST.B` | Module: AR | Fields: 106 (all confirmed from DDF — Pass 123 2026-06-19)

Primary key: `BKAR_CUSTCODE` (field 1).

| # | Field | Type | Size | Meaning |
|---|-------|------|------|---------|
| 1 | BKAR_CUSTCODE | STRING | 10 | Customer code — **primary key** |
| 2 | BKAR_CUSTNAME | STRING | 30 | Company name |
| 3 | BKAR_ADD1 | STRING | 30 | Address line 1 |
| 4 | BKAR_ADD2_1 | STRING | 30 | Address line 2, part 1 |
| 5 | BKAR_ADD2_2 | STRING | 30 | Address line 2, part 2 |
| 6 | BKAR_CITY | STRING | 26 | City |
| 7 | BKAR_STATE | STRING | 2 | State |
| 8 | BKAR_ZIP | STRING | 10 | ZIP / postal code |
| 9 | BKAR_CONTACT_1 | STRING | 30 | Contact name 1 |
| 10 | BKAR_CONTACT_2 | STRING | 30 | Contact name 2 |
| 11 | BKAR_CONTACT_3 | STRING | 30 | Contact name 3 |
| 12 | BKAR_CONTACT_4 | STRING | 30 | Contact name 4 |
| 13 | BKAR_CONTACT_5 | STRING | 30 | Contact name 5 |
| 14 | BKAR_TELEPHONE_1 | STRING | 25 | Phone 1 |
| 15 | BKAR_TELEPHONE_2 | STRING | 25 | Phone 2 |
| 16 | BKAR_TELEPHONE_3 | STRING | 25 | Phone 3 |
| 17 | BKAR_TELEPHONE_4 | STRING | 25 | Phone 4 |
| 18 | BKAR_TELEPHONE_5 | STRING | 25 | Phone 5 |
| 19 | BKAR_COUNTRY | STRING | 30 | Country |
| 20 | BKAR_CREDITLMT | FLOAT | 8(2) | Credit limit |
| 21 | BKAR_CHG_INTRST | STRING | 1 | Charge interest flag (Y/N) |
| 22 | BKAR_REMAINCRD | FLOAT | 8(2) | Remaining credit (limit − outstanding) |
| 23 | BKAR_OUTINV | FLOAT | 8(2) | Outstanding invoice balance |
| 24 | BKAR_LASTSALE | DATE | 4 | Last sale date |
| 25 | BKAR_LASTPMT | DATE | 4 | Last payment date |
| 26 | BKAR_GROSS_MTD | FLOAT | 8(2) | Gross sales MTD |
| 27 | BKAR_COGS_MTD | FLOAT | 8(2) | COGS MTD |
| 28 | BKAR_NET_MTD | FLOAT | 8(2) | Net sales MTD |
| 29 | BKAR_PNET_MTD | FLOAT | 8(4) | Net profit % MTD |
| 30 | BKAR_GROSS_YTD | FLOAT | 8(2) | Gross sales YTD |
| 31 | BKAR_COGS_YTD | FLOAT | 8(2) | COGS YTD |
| 32 | BKAR_NET_YTD | FLOAT | 8(2) | Net sales YTD |
| 33 | BKAR_PNET_YTD | FLOAT | 8(4) | Net profit % YTD |
| 34 | BKAR_GROSS_LYR | FLOAT | 8(2) | Gross sales last year |
| 35 | BKAR_COGS_LYR | FLOAT | 8(2) | COGS last year |
| 36 | BKAR_NET_LYR | FLOAT | 8(2) | Net sales last year |
| 37 | BKAR_PNET_LYR | FLOAT | 8(4) | Net profit % last year |
| 38 | BKAR_GROSS_PVAR | FLOAT | 8(4) | Gross sales % variance (YTD vs LYR) |
| 39 | BKAR_COGS_PVAR | FLOAT | 8(4) | COGS % variance |
| 40 | BKAR_NET_PVAR | FLOAT | 8(4) | Net sales % variance |
| 41 | BKAR_PNET_PVAR | FLOAT | 8(4) | Net profit % variance |
| 42 | BKAR_NEW_CUST | STRING | 1 | New customer flag |
| 43 | BKAR_OUT_CREDIT_1 | FLOAT | 8(2) | Outstanding credit memo 1 |
| 44 | BKAR_OUT_CREDIT_2 | FLOAT | 8(2) | Outstanding credit memo 2 |
| 45 | BKAR_TAX_STATE | STRING | 2 | Tax state code |
| 46 | BKAR_TAX_LOCAL | STRING | 2 | Tax local code |
| 47 | BKAR_TAX_YN | STRING | 1 | Taxable flag (Y/N) |
| 48 | BKAR_STATEMENT | STRING | 1 | Send statement flag (Y/N) |
| 49 | BKAR_SLSP_NUM_1 | UBINARY | 2 | Salesperson 1 number (index) |
| 50 | BKAR_SLSP_NUM_2 | UBINARY | 2 | Salesperson 2 number (index) |
| 51 | BKAR_TERMS_NUM | UBINARY | 2 | Terms number (index into BKSYMSTR terms array) |
| 52 | BKAR_START_DATE | DATE | 4 | Customer start date |
| 53 | BKAR_CLASS | STRING | 4 | Customer class code |
| 54 | BKAR_PRICE_MAT | UBINARY | 2 | Price matrix number |
| 55 | BKAR_HIST_YN | STRING | 1 | Keep history flag (Y/N) |
| 56 | BKAR_DISC_CODE | STRING | 10 | Discount code |
| 57 | BKAR_NUM_INVCS | FLOAT | 8(0) | Number of invoices (lifetime) |
| 58 | BKAR_DAYS_TOPAY | FLOAT | 8(0) | Average days to pay |
| 59 | BKAR_NOTES_1 | STRING | 80 | Notes line 1 |
| 60 | BKAR_NOTES_2 | STRING | 80 | Notes line 2 |
| 61 | BKAR_NOTES_3 | STRING | 80 | Notes line 3 |
| 62 | BKAR_NOTES_4 | STRING | 80 | Notes line 4 |
| 63 | BKAR_NOTES_5 | STRING | 80 | Notes line 5 |
| 64 | BKAR_NOTES_6 | STRING | 80 | Notes line 6 |
| 65 | BKAR_NOTES_7 | STRING | 80 | Notes line 7 |
| 66 | BKAR_NOTES_8 | STRING | 80 | Notes line 8 |
| 67 | BKAR_NOTES_9 | STRING | 80 | Notes line 9 |
| 68 | BKAR_NOTES_10 | STRING | 80 | Notes line 10 |
| 69 | BKAR_GLACCT | STRING | 10 | Default GL sales account number |
| 70 | BKAR_GLDPT | STRING | 4 | Default GL department |
| 71 | BKAR_FOB | STRING | 15 | Default FOB point |
| 72 | BKAR_SHIPTO | STRING | 10 | Default ship-to code |
| 73 | BKAR_SHIPVIA | STRING | 15 | Default ship via |
| 74 | BKAR_FOLUPDTE | DATE | 4 | Follow-up date (CRM) |
| 75 | BKAR_COMM_1 | FLOAT | 8(4) | Salesperson 1 commission rate |
| 76 | BKAR_COMM_2 | FLOAT | 8(4) | Salesperson 2 commission rate |
| 77 | BKAR_SORT | STRING | 6 | Alpha sort key |
| 78 | BKAR_COOP_RATE | FLOAT | 8(4) | Co-op marketing rate |
| 79 | BKAR_COOP_AMT | FLOAT | 8(2) | Co-op marketing accrued amount |
| 80 | BKAR_TERRITORY | STRING | 4 | Sales territory code |
| 81 | BKAR_LEAD_SRC | STRING | 5 | Lead source code |
| 82 | BKAR_SIC_CODE | STRING | 7 | SIC industry code |
| 83 | BKAR_PURCH_AGMT | STRING | 1 | Purchase agreement flag |
| 84 | BKAR_FORECAST | STRING | 12 | Forecast identifier |
| 85 | BKAR_CUST_YEAR | STRING | 12 | Customer year field |
| 86 | BKAR_QC_INFO | STRING | 30 | QC / quality notes |
| 87 | BKAR_MAIL_LIST | STRING | 1 | Mailing list flag |
| 88 | BKAR_CARRIER | STRING | 15 | Default carrier |
| 89 | BKAR_REQD_CERTS | STRING | 10 | Required certifications |
| 90 | BKAR_SHP_WINDOW | STRING | 30 | Shipping window (text) |
| 91 | BKAR_RECV_HOURS | STRING | 30 | Receiving hours (text) |
| 92 | BKAR_SHP_TOLRNC | STRING | 10 | Shipping tolerance |
| 93 | BKAR_RESALE_NO | STRING | 15 | Resale / tax exemption number |
| 94 | BKAR_FAX_PHONE | STRING | 25 | Fax number |
| 95 | BKAR_CREDIT_HLD | STRING | 1 | Credit hold flag (Y/N) |
| 96 | BKAR_EXTRA | STRING | 30 | Extra / user-defined field |
| 97 | BKAR_EMAIL_1 | STRING | 128 | Email address 1 |
| 98 | BKAR_EMAIL_2 | STRING | 128 | Email address 2 |
| 99 | BKAR_EMAIL_3 | STRING | 128 | Email address 3 |
| 100 | BKAR_EMAIL_4 | STRING | 128 | Email address 4 |
| 101 | BKAR_EMAIL_5 | STRING | 128 | Email address 5 |
| 102 | BKAR_IS_TAXGRP | STRING | 10 | Avalara tax group code |
| 103 | BKAR_IS_TAXIN | STRING | 1 | Avalara tax-inclusive flag |
| 104 | BKAR_IS_MCCODE | STRING | 3 | Avalara multi-company code |
| 105 | BKAR_IS_REP | STRING | 5 | Avalara tax representative |
| 106 | BKAR_LEAD_SRC2 | STRING | 5 | Lead source 2 code |

**Notes:**
- Primary key is `BKAR_CUSTCODE` (10 chars), used in BKARINV, BKARCASH, and all AR transactions.
- Address uses a 2-part line-2 convention (ADD2_1 + ADD2_2) matching other EVO address blocks.
- 5 contacts (`BKAR_CONTACT_1..5`) and 5 phones (`BKAR_TELEPHONE_1..5`) — same pattern as BKAPVEND.
- Sales analytics (fields 26–41): MTD/YTD/last-year gross, COGS, net, profit%, and YTD-vs-LYR variance — all denormalized onto the customer record for fast reporting.
- Fields 102–105 (`BKAR_IS_*`) are Avalara cloud tax integration fields (same IS* pattern as BKARINV.BKAR_INV_ISTXKY).
- `BKAR_REMAINCRD` is a calculated/maintained field: credit limit minus outstanding balance.

---

## BKARINV — AR Invoice Header

File: `BKARINV.B` | Module: AR | Fields: 84 (all confirmed from DDF — Pass 122 2026-06-19)

Primary key: `BKAR_INV_NUM` (field 1, FLOAT auto-increment from `BKSYMSTR.BKSY_ARINV_NUM`).

| # | Field | Type | Size | Meaning |
|---|-------|------|------|---------|
| 1 | BKAR_INV_NUM | FLOAT | 8 | Invoice number — **primary key** |
| 2 | BKAR_INV_SONUM | FLOAT | 8 | Sales order number (FK → BKSOX/SO) |
| 3 | BKAR_INV_INVCD | STRING | 1 | Invoice code / type flag |
| 4 | BKAR_INV_INVDTE | DATE | 4 | Invoice date |
| 5 | BKAR_INV_CUSCOD | STRING | 10 | Customer code (FK → BKARCUST) |
| 6 | BKAR_INV_CUSA1 | STRING | 30 | Customer address line 1 (denormalized at invoice time) |
| 7 | BKAR_INV_CUSNME | STRING | 30 | Customer name (denormalized) |
| 8 | BKAR_INV_CUSA2_1 | STRING | 30 | Customer address line 2, part 1 |
| 9 | BKAR_INV_CUSA2_2 | STRING | 30 | Customer address line 2, part 2 |
| 10 | BKAR_INV_CUSCTY | STRING | 26 | Customer city |
| 11 | BKAR_INV_CUSST | STRING | 2 | Customer state |
| 12 | BKAR_INV_CUSZIP | STRING | 10 | Customer ZIP |
| 13 | BKAR_INV_CUSCNT | STRING | 30 | Customer country |
| 14 | BKAR_INV_CUSATT | STRING | 30 | Customer attention/contact |
| 15 | BKAR_INV_SHPCTY | STRING | 26 | Ship-to city |
| 16 | BKAR_INV_SHPST | STRING | 2 | Ship-to state |
| 17 | BKAR_INV_SHPZIP | STRING | 10 | Ship-to ZIP |
| 18 | BKAR_INV_SHPCOD | STRING | 10 | Ship-to code |
| 19 | BKAR_INV_SHPNME | STRING | 30 | Ship-to name |
| 20 | BKAR_INV_SHPA1 | STRING | 30 | Ship-to address line 1 |
| 21 | BKAR_INV_SHPA2_1 | STRING | 30 | Ship-to address line 2, part 1 |
| 22 | BKAR_INV_SHPA2_2 | STRING | 30 | Ship-to address line 2, part 2 |
| 23 | BKAR_INV_SHPATN | STRING | 30 | Ship-to attention |
| 24 | BKAR_INV_SHPVIA | STRING | 15 | Ship-via code |
| 25 | BKAR_INV_SHPCNT | STRING | 30 | Ship-to country |
| 26 | BKAR_INV_TERMD | STRING | 10 | Terms description |
| 27 | BKAR_INV_TERMNM | UBINARY | 2 | Terms number (index into BKSYMSTR terms array) |
| 28 | BKAR_INV_SLSP | UBINARY | 2 | Salesperson 1 number |
| 29 | BKAR_INV_ENTBY | STRING | 5 | Entered-by code |
| 30 | BKAR_INV_CUSORD | STRING | 25 | Customer PO / order number |
| 31 | BKAR_INV_TAXABL | STRING | 1 | Taxable flag |
| 32 | BKAR_INV_SUBTOT | FLOAT | 8(2) | Subtotal (before tax/freight) |
| 33 | BKAR_INV_TAXAMT | FLOAT | 8(2) | Tax amount |
| 34 | BKAR_INV_TOTAL | FLOAT | 8(2) | Invoice total |
| 35 | BKAR_INV_COGS | FLOAT | 8(2) | Cost of goods sold |
| 36 | BKAR_INV_NL | UBINARY | 2 | Number of line items |
| 37 | BKAR_INV_TAXRTE | FLOAT | 8(4) | Tax rate |
| 38 | BKAR_INV_DESC | STRING | 30 | Invoice description |
| 39 | BKAR_INV_GLDPT | STRING | 4 | GL department |
| 40 | BKAR_INV_RTS | STRING | 1 | Release-to-ship flag |
| 41 | BKAR_INV_FRGHT | FLOAT | 8(2) | Freight amount |
| 42 | BKAR_INV_LOC | STRING | 10 | Ship-from location code |
| 43 | BKAR_INV_TAXKEY | STRING | 4 | Tax key code |
| 44 | BKAR_INV_ORDDTE | DATE | 4 | Order date |
| 45 | BKAR_INV_ENDLNE | STRING | 1 | End-of-document line flag |
| 46 | BKAR_INV_DCODE | STRING | 10 | Discount code |
| 47 | BKAR_INV_PCODE | UBINARY | 2 | Price code |
| 48 | BKAR_INV_SHIPDT | DATE | 4 | Ship date |
| 49 | BKAR_INV_FOB | STRING | 15 | FOB point |
| 50 | BKAR_INV_SLSP2 | UBINARY | 2 | Salesperson 2 number |
| 51 | BKAR_INV_COMMPR_1 | FLOAT | 8(4) | Commission percentage (SP1) |
| 52 | BKAR_INV_COMMPR_2 | FLOAT | 8(4) | Commission percentage (SP2) |
| 53 | BKAR_INV_CHKNUM | FLOAT | 8 | Check number (payment applied) |
| 54 | BKAR_INV_DEPAMT | FLOAT | 8(2) | Deposit amount applied |
| 55 | BKAR_INV_SHIPPR | FLOAT | 8 | Shipper/carrier number |
| 56 | BKAR_INV_JOBNUM | STRING | 15 | Job number (FK → ISJOB) |
| 57 | BKAR_INV_ITMZTX_1 | STRING | 1 | Item zero-tax flag 1 |
| 58 | BKAR_INV_ITMZTX_2 | STRING | 1 | Item zero-tax flag 2 |
| 59 | BKAR_INV_RETEN | FLOAT | 8(2) | Retention (holdback) amount |
| 60 | BKAR_INV_COMAMT | FLOAT | 8(2) | Commission amount |
| 61 | BKAR_INV_CCOAMT | FLOAT | 8(2) | CC operation / surcharge amount |
| 62 | BKAR_INV_BILCOD | STRING | 10 | Bill-to code |
| 63 | BKAR_INV_BILNME | STRING | 30 | Bill-to name |
| 64 | BKAR_INV_BILA1 | STRING | 30 | Bill-to address line 1 |
| 65 | BKAR_INV_BILA2 | STRING | 30 | Bill-to address line 2 |
| 66 | BKAR_INV_BILA3 | STRING | 30 | Bill-to address line 3 |
| 67 | BKAR_INV_BILCTY | STRING | 30 | Bill-to city |
| 68 | BKAR_INV_BILST | STRING | 2 | Bill-to state |
| 69 | BKAR_INV_BILZIP | STRING | 10 | Bill-to ZIP |
| 70 | BKAR_INV_BILCNT | STRING | 30 | Bill-to country |
| 71 | BKAR_INV_BILATN | STRING | 30 | Bill-to attention |
| 72 | BKAR_INV_EXTRA | STRING | 150 | Overflow / extra |
| 73 | BKAR_INV_INDATE | DATE | 4 | Creation/entry date |
| 74 | BKAR_INV_SCCOGS | FLOAT | 8(2) | Surcharge COGS amount |
| 75 | BKAR_INV_ISTXKY | STRING | 10 | Avalara tax key |
| 76 | BKAR_INV_ISMCDT | DATE | 4 | Multi-currency exchange date |
| 77 | BKAR_INV_ISREV | STRING | 1 | Reverse invoice flag |
| 78 | BKAR_INV_ISRVDT | DATE | 4 | Reverse date |
| 79 | BKAR_INV_ISCUR | STRING | 3 | Currency code (multi-currency) |
| 80 | BKAR_INV_RELNUM | FLOAT | 8 | Related invoice number (original for reversals) |
| 81 | BKAR_INV_TRACK | STRING | 40 | Tracking number (carrier) |
| 82 | BKAR_INV_QSTAT | STRING | 1 | Quote status flag |
| 83 | BKAR_INV_MDATE | DATE | 4 | Last modification date |
| 84 | BKAR_INV_MISC | STRING | 100 | Miscellaneous / user-defined |

**Address structure:** Three complete address blocks per record — Customer (bill), Ship-to, and Bill-to (when different from Customer). All denormalized at invoice creation time.

**Multi-currency:** ISCUR (currency code), ISMCDT (exchange rate date).

**Avalara:** ISTXKY field matches Avalara transaction key for tax verification.

**Reversals:** ISREV flag + ISRVDT date + RELNUM (original invoice number) support credit memo/reversal chain.

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

File: `BKAPVEND.B` | Module: AP | Fields: 72 (confirmed from DDF — Pass 122 2026-06-19)

Primary key: `BKAP_VENDCODE` (field 1). Note: DDF field names use `BKAP_VENDXXX` not `BKAP_VEND_XXX`.

| # | Field | Type | Size | Meaning |
|---|-------|------|------|---------|
| 1 | BKAP_VENDCODE | STRING | 10 | Vendor code — **primary key** |
| 2 | BKAP_VENDNAME | STRING | 30 | Vendor company name |
| 3 | BKAP_ADD1_1 | STRING | 30 | Address line 1 (main) |
| 4 | BKAP_ADD1_2 | STRING | 30 | Address line 1 (remit-to) |
| 5 | BKAP_ADD2_1 | STRING | 30 | Address line 2 (main) |
| 6 | BKAP_ADD2_2 | STRING | 30 | Address line 2 (remit-to) |
| 7 | BKAP_CITY_1 | STRING | 26 | City (main) |
| 8 | BKAP_CITY_2 | STRING | 26 | City (remit-to) |
| 9 | BKAP_STATE | STRING | 2 | State |
| 10 | BKAP_CONTACT_1 | STRING | 30 | Contact 1 name |
| 11 | BKAP_CONTACT_2 | STRING | 30 | Contact 2 name |
| 12 | BKAP_CONTACT_3 | STRING | 30 | Contact 3 name |
| 13 | BKAP_CONTACT_4 | STRING | 30 | Contact 4 name |
| 14 | BKAP_TELEPHONE_1 | STRING | 25 | Phone 1 |
| 15 | BKAP_TELEPHONE_2 | STRING | 25 | Phone 2 |
| 16 | BKAP_TELEPHONE_3 | STRING | 25 | Phone 3 |
| 17 | BKAP_TELEPHONE_4 | STRING | 25 | Phone 4 |
| 18 | BKAP_TELEPHONE_5 | STRING | 25 | Phone 5 |
| 19 | BKAP_ZIP | STRING | 10 | ZIP code |
| 20 | BKAP_COUNTRY_1 | STRING | 30 | Country (main) |
| 21 | BKAP_COUNTRY_2 | STRING | 30 | Country (remit-to) |
| 22 | BKAP_OUTINV | FLOAT | 8(2) | Outstanding invoice balance |
| 23 | BKAP_LASTPURCH | DATE | 4 | Last purchase date |
| 24 | BKAP_LASTPMT | DATE | 4 | Last payment date |
| 25 | BKAP_PURCH_MTD | FLOAT | 8(2) | Purchases month-to-date |
| 26 | BKAP_PURCH_YTD | FLOAT | 8(2) | Purchases year-to-date |
| 27 | BKAP_PURCH_LYR | FLOAT | 8(2) | Purchases last year |
| 28 | BKAP_PURCH_VAR | FLOAT | 8(4) | Purchase variance |
| 29 | BKAP_OUT_CREDIT | FLOAT | 8(2) | Outstanding credit balance |
| 30 | BKAP_NEW_VEND | STRING | 1 | New vendor flag |
| 31 | BKAP_START_DATE | DATE | 4 | Vendor start date |
| 32 | BKAP_CLASS | STRING | 4 | Vendor classification code |
| 33 | BKAP_TERMS_NUM | UBINARY | 2 | Payment terms index (1–20, into BKSYMSTR terms array) |
| 34 | BKAP_HIST_YN | STRING | 1 | Maintain purchase history flag |
| 35 | BKAP_REM_ZIP | STRING | 10 | Remit-to ZIP |
| 36 | BKAP_REM_STATE | STRING | 2 | Remit-to state |
| 37 | BKAP_NOTES_1 | STRING | 60 | Vendor note line 1 |
| 38 | BKAP_NOTES_2 | STRING | 60 | Vendor note line 2 |
| 39 | BKAP_NOTES_3 | STRING | 60 | Vendor note line 3 |
| 40 | BKAP_NOTES_4 | STRING | 60 | Vendor note line 4 |
| 41 | BKAP_NOTES_5 | STRING | 60 | Vendor note line 5 |
| 42 | BKAP_NOTES_6 | STRING | 60 | Vendor note line 6 |
| 43 | BKAP_NOTES_7 | STRING | 60 | Vendor note line 7 |
| 44 | BKAP_NOTES_8 | STRING | 60 | Vendor note line 8 |
| 45 | BKAP_NOTES_9 | STRING | 60 | Vendor note line 9 |
| 46 | BKAP_NOTES_10 | STRING | 60 | Vendor note line 10 |
| 47 | BKAP_GL_ACCT | STRING | 10 | Vendor-specific AP GL account override |
| 48 | BKAP_GL_DPT | STRING | 4 | Vendor-specific AP GL dept override |
| 49 | BKAP_SORT | STRING | 6 | Sort key |
| 50 | BKAP_SHIP_VIA | STRING | 15 | Default ship-via code |
| 51 | BKAP_FOB_POINT | STRING | 20 | Default FOB point |
| 52 | BKAP_FTERMS_NUM | UBINARY | 2 | Freight terms index |
| 53 | BKAP_TAX_ID | STRING | 20 | Tax ID / EIN (for 1099 reporting) |
| 54 | BKAP_ADD3 | STRING | 30 | Address line 3 |
| 55 | BKAP_EXTRA | STRING | 150 | Overflow / extra config |
| 56 | BKAP_EMAIL_1 | STRING | 128 | Email address 1 |
| 57 | BKAP_EMAIL_2 | STRING | 128 | Email address 2 |
| 58 | BKAP_EMAIL_3 | STRING | 128 | Email address 3 |
| 59 | BKAP_EMAIL_4 | STRING | 128 | Email address 4 |
| 60 | BKAP_EMAIL_5 | STRING | 128 | Email address 5 |
| 61 | BKAP_DESC | STRING | 25 | Vendor short description |
| 62 | BKAP_IS_TAXGRP | STRING | 10 | Avalara tax group code |
| 63 | BKAP_IS_TAXIN | STRING | 1 | Tax inclusive flag |
| 64 | BKAP_IS_MCCODE | STRING | 3 | Multi-currency code |
| 65 | BKAP_IS_DCODE | STRING | 3 | Discount code |
| 66 | BKAP_CUST_CODE | STRING | 15 | Linked customer code (FK → BKARCUST) — vendor-customer cross-reference |
| 67 | BKAP_CREDLIM | FLOAT | 8(2) | Credit limit |
| 68 | BKAP_REQQC | STRING | 1 | Require QC inspection flag |
| 69 | BKAP_ALPHA1 | STRING | 25 | User-defined alpha field 1 |
| 70 | BKAP_ALPHA2 | STRING | 25 | User-defined alpha field 2 |
| 71 | BKAP_DATE1 | DATE | 4 | User-defined date field 1 |
| 72 | BKAP_DATE2 | DATE | 4 | User-defined date field 2 |

**Key notes:**
- Dual address fields (_1/_2) = main address / remit-to address on the same record
- `BKAP_TERMS_NUM` is an integer index (1–20) into `BKSYMSTR.BKSY_TERMS_N` array
- `BKAP_CUST_CODE` links the vendor to a matching BKARCUST record — used when the same entity is both vendor and customer
- `BKAP_IS_TAXGRP` / `BKAP_IS_TAXIN` = Avalara integration fields (consistent with ISTS.CFG.AVA* keys)
- `BKAP_REQQC` = requires QC receipt inspection — integrates with BKQCRECV
- 10 notes lines (600 chars total), 5 email addresses, 2 UDF alpha + 2 UDF date fields

---

## BKAPINVL — AP Invoice / Voucher

File: `BKAPINVL.B` | Module: AP | Fields: 390 (all confirmed from DDF — Pass 125 2026-06-19)

Flat AP voucher record: header + inline GL distribution block (up to 75 GL lines). `BKAPRIVL` is **identical** (receipt-invoice lines for 3-way match). Unlike AR (which uses separate BKARINV header + BKARINVL lines), AP vouchers embed all distribution lines in one record.

**Header (fields 1–10):**

| # | Field | Type | Size | Meaning |
|---|-------|------|------|---------|
| 1 | BKAP_INVL_CODE | STRING | 10 | Vendor code (FK → BKAPVEND) — **PK component** |
| 2 | BKAP_INVL_NUM | STRING | 10 | Vendor's invoice number — **PK component** |
| 3 | BKAP_INVL_DATE | DATE | 4 | Invoice date |
| 4 | BKAP_INVL_DESC | STRING | 25 | Description |
| 5 | BKAP_INVL_TERMD | STRING | 10 | Terms description (denormalized) |
| 6 | BKAP_INVL_TERMN | UBINARY | 2 | Terms number (index into BKSYMSTR terms array) |
| 7 | BKAP_INVL_TYPED | STRING | 10 | Type description |
| 8 | BKAP_INVL_TYPEN | UBINARY | 2 | Type number |
| 9 | BKAP_INVL_TAMT | FLOAT | 8(2) | Total amount |
| 10 | BKAP_INVL_TDC | STRING | 1 | Total debit/credit flag |

**GL Distribution Block (fields 11–385) — 75 slots, each with 5 sub-fields:**

| Group | Fields | Meaning |
|-------|--------|---------|
| BKAP_INVL_GLACT_1..75 | 11–85 | GL account number for slot N |
| BKAP_INVL_GLDPT_1..75 | 86–160 | GL department for slot N |
| (DC flags, 75) | 161–235 | Debit/credit indicator for slot N |
| (AMT array, 75) | 236–310 | Amount for slot N |
| BKAP_INVL_DAMT_1..75 | 311–385 | Distribution amount (confirmed field name) |

**Footer (fields 386–390):**

| # | Field | Type | Size | Meaning |
|---|-------|------|------|---------|
| 386 | BKAP_INVL_APDPT | STRING | 4 | AP department |
| 387 | BKAP_INVL_CHK | UBINARY | 2 | Check number (when paid) |
| 388 | BKAP_INVL_EXTRA | STRING | 50 | Extra / user-defined |
| 389 | BKAP_INVL_ISCUR | STRING | 3 | Multi-currency code |
| 390 | BKAP_INVL_JOB | STRING | 15 | Job number |

**Note:** `BKAPRIVL` is byte-for-byte identical to BKAPINVL — it stores AP receipt lines (goods received note) for 3-way match (RFQ → PO → receipt → invoice).

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

## BKAP* Family — AP Satellite Tables

All confirmed from DDF — Pass 125 2026-06-19. These tables support BKAPVEND and the AP transaction lifecycle.

### PO Archive Variants (same 57-field BKAP_PO_* structure)

BKAPPO (active), BKAPAPO (open PO archive, 58f = +1 access control field), BKAPHPO (historical, 57f), and BKAPRFQ (RFQ, 57f) all share the same `BKAP_PO_*` field set:

| # | Key Field | Type | Meaning |
|---|-----------|------|---------|
| 1 | BKAP_PO_NUM | FLOAT | PO number — **primary key** |
| 2 | BKAP_PO_PRTD | STRING | Printed flag |
| 3 | BKAP_PO_VNDCOD | STRING | Vendor code (FK → BKAPVEND) |
| 4 | BKAP_PO_VNDNME | STRING | Vendor name (denormalized) |
| 5–8 | BKAP_PO_VNDA1/2/3/VNDCTY | STRING | Vendor address 3 lines + city |
| 9 | BKAP_PO_VNDST | STRING | Vendor state |
| 10 | BKAP_PO_VNDZIP | STRING | Vendor ZIP |
| 11–16 | BKAP_PO_SHP* | STRING | Ship-to address block (code+name+addr+city+st+zip) |
| 17 | BKAP_PO_SHPVIA | STRING | Ship via |
| 18 | BKAP_PO_TERMD | STRING | Terms description |
| 19 | BKAP_PO_TERMNM | UBINARY | Terms number |
| 20 | BKAP_PO_ENTBY | STRING | Entered-by user |
| 21 | BKAP_PO_OBYCUS | STRING | Order by customer (if job-related) |
| 22 | BKAP_PO_TAXABLE | STRING | Taxable flag |
| 23–24 | BKAP_PO_CONFIRM_1/2 | STRING | Confirmation flags |
| 25 | BKAP_PO_ORDDTE | DATE | Order date |
| 26–28 | BKAP_PO_SUBTOT/TAXAMT/TOTAL | FLOAT | PO subtotal, tax, total |
| 29 | BKAP_PO_NL | UBINARY | Number of lines |
| 30 | BKAP_PO_TAXRTE | FLOAT | Tax rate |
| 31 | BKAP_PO_DESC | STRING | Description |
| 32 | BKAP_PO_GLDPT | STRING | GL department |
| 33 | BKAP_PO_LOC | STRING | Location code |
| 34 | BKAP_PO_ITOTAL | FLOAT | Invoice total |
| 35 | BKAP_PO_ENDLNE | STRING | End-of-line flag |
| 36 | BKAP_PO_FOB | STRING | FOB point |
| 37–38 | BKAP_PO_FTERMNM/FTERMD | UBINARY/STRING | Freight terms |
| 39 | BKAP_PO_QCTOTAL | FLOAT | QC total |
| 40–45 | BKAP_PO_VNDCNT/VNDATN/SHPA3/SHPCNT/SHPATN | STRING | Extended address contacts |
| 46 | BKAP_PO_RECNUM | FLOAT | Receipt number |
| 47 | BKAP_PO_LONGPO | STRING | Long PO description |
| 48 | BKAP_PO_EXTRA | STRING | Extra 150 chars |
| 49 | BKAP_PO_INVNUM | STRING | Invoice number |
| 50–54 | BKAP_PO_IS* | STRING/DATE | Avalara: ISTXGR, ISMCDT, ISBROKE, ISREV, ISRVDT |
| 55 | BKAP_PO_ISCUR | STRING | Multi-currency code |
| 56 | BKAP_PO_PCKSLP | STRING | Packing slip number |
| 57 | BKAP_PO_EMPNUM | UBINARY | Employee number |

**PO Lines Variants** — BKAPPOL, BKAPAPOL, BKAPHPOL, BKAPRFQL all 38-field identical `BKAP_POL_*` structure: PONM (PO number) + CNTR (line counter) as PK, then ERD (expected receipt date), PCODE (part), PDESC, PQTY (ordered qty), IQTY (received qty), OO_QTY (outstanding), PONM_LINK, COST, GLACT, GLDPT, WO links, UOM, etc.

---

### BKAPINVT / BKAPEIVT — AP Invoice Transaction Ledger

Files: `BKAPINVT.B` / `BKAPEIVT.B` | Module: AP | Fields: 19 each (identical)

Running ledger of AP transactions per vendor — one row per invoice/credit/payment event. BKAPINVT = current; BKAPEIVT = expanded/EI variant (same structure).

| # | Field | Type | Size | Meaning |
|---|-------|------|------|---------|
| 1 | BKAP_INVT_CODE | STRING | 10 | Vendor code — **PK component** |
| 2 | BKAP_INVT_DATE | DATE | 4 | Transaction date |
| 3 | BKAP_INVT_NUM | STRING | 10 | Invoice/reference number — **PK component** |
| 4 | BKAP_INVT_AMT | FLOAT | 8(2) | Invoice amount |
| 5 | BKAP_INVT_AMTRM | FLOAT | 8(2) | Amount remaining (balance) |
| 6 | BKAP_INVT_DESC | STRING | 25 | Description |
| 7 | BKAP_INVT_TYPE | STRING | 1 | Transaction type |
| 8 | BKAP_INVT_TERMN | UBINARY | 2 | Terms number |
| 9 | BKAP_INVT_GLDPT | STRING | 4 | GL department |
| 10 | BKAP_INVT_SDATE | DATE | 4 | Statement date |
| 11 | BKAP_INVT_EXTRA | STRING | 50 | Extra / user-defined |
| 12 | BKAP_INVT_PDATE | DATE | 4 | Payment date |
| 13 | BKAP_INVT_MCRAT | FLOAT | 8(6) | Multi-currency exchange rate |
| 14 | BKAP_INVT_MCCOD | STRING | 3 | Multi-currency code |
| 15 | BKAP_INVT_TAX | FLOAT | 8(2) | Tax amount |
| 16 | BKAP_INVT_FRT | FLOAT | 8(2) | Freight amount |
| 17 | BKAP_INVT_DEPNO | FLOAT | 8(0) | Deposit number |
| 18 | BKAP_INVT_CHKNO | FLOAT | 8(0) | Check number |
| 19 | BKAP_INVT_CHKAC | UBINARY | 2 | Check bank account number |

---

### BKAPNOTE — Vendor Notes

File: `BKAPNOTE.B` | Module: AP | Fields: 12

Timestamped note records for vendors (indexed by two search keys).

| # | Field | Type | Size | Meaning |
|---|-------|------|------|---------|
| 1 | BKAP_NOTE_SRCH1 | STRING | 10 | Search key 1 (vendor code) — **PK component** |
| 2 | BKAP_NOTE_SRCH2 | STRING | 10 | Search key 2 (topic/category) |
| 3 | BKAP_NOTE_DATE | DATE | 4 | Note date |
| 4 | BKAP_NOTE_ENTBY | STRING | 10 | Entered-by user |
| 5–12 | BKAP_NOTE_NOTES_1..8 | STRING×8 | 76 | Note lines 1–8 (76 chars each) |

---

### BKAPEVND — Extended Vendor

File: `BKAPEVND.B` | Module: AP | Fields: 73

Extended vendor record using `BKAP_VEND*` prefix. Likely multi-company "E" mirror of BKAPVEND or extended address/contact block.

Primary key: `BKAP_VENDCODE` (field 1). Structure mirrors BKAPVEND with two address blocks (ADD1_1/1_2 and ADD2_1/2) and additional contact/tax fields.

---

### BKAPACCN — Vendor Contacts

File: `BKAPACCN.B` | Module: AP/CRM | Fields: 154

Uses `BKCM_ACCN_*` prefix (Contact Manager namespace). Stores 10 contact slots per vendor — same architecture as BKARCUST contacts but vendor-facing.

| Group | Fields | Meaning |
|-------|--------|---------|
| BKCM_ACCN_CODE | 1 | Vendor/account code — **primary key** |
| BKCM_ACCN_CONT_1..10 | 2–11 | Contact name (10 contacts) |
| BKCM_ACCN_TITLE_1..10 | 12–21 | Contact title |
| BKCM_ACCN_PHONE_1..10 | 22–31 | Contact phone |
| BKCM_ACCN_DEAR_1..10 | 32–41 | Contact salutation |
| BKCM_ACCN_EMAIL_1..10 | 42–51 | Contact email |
| (label + UDF fields) | 52–154 | PHLBL, EMLBL, MSLBL, DTLBL, M2LBL, D2LBL per contact + alpha/date UDFs |

---

### BKAP* Description Tables (all 5-field BK_DESC_* pattern)

`BKAPADSC`, `BKAPDESC`, `BKAPHDSC` — all identical 5-field pattern:

| # | Field | Meaning |
|---|-------|---------|
| 1 | BK_DESC_CODE | AP entity code (vendor/PO number) |
| 2 | BK_DESC_NUM | Record number |
| 3 | BK_DESC_LINE | Line counter |
| 4 | BK_DESC_NOTES | Note text (70 chars) |
| 5 | BK_DESC_DESC | Short description (25 chars) |

---

**BKAP* Family Summary Table** (Pass 125 2026-06-19):

| Table | Fields | Role | Structural Mirror |
|-------|--------|------|------------------|
| BKAPVEND | 72 | Vendor master | — |
| BKAPEVND | 73 | Extended vendor | BKAPVEND variant |
| BKAPACCN | 154 | Vendor contacts (10 slots) | — |
| BKAPPO | 57 | Purchase orders (active) | — |
| BKAPAPO | 58 | PO open archive (+1 field) | BKAPPO |
| BKAPHPO | 57 | PO historical archive | BKAPPO |
| BKAPRFQ | 57 | Request for quotation | BKAPPO |
| BKAPPOL | 38 | PO lines (active) | — |
| BKAPAPOL | 38 | PO lines open archive | BKAPPOL |
| BKAPHPOL | 38 | PO lines historical | BKAPPOL |
| BKAPRFQL | 38 | RFQ lines | BKAPPOL |
| BKAPINVL | 390 | AP voucher (10 hdr + 75 GL dist × 5 + 5 ftr) | — |
| BKAPRIVL | 390 | Receipt-invoice lines (3-way match) | BKAPINVL |
| BKAPINVT | 19 | AP invoice transaction ledger | — |
| BKAPEIVT | 19 | AP invoice transaction (EI variant) | BKAPINVT |
| BKAPCHKH | 12 | Check header | — |
| BKAPCHKF | 12 | Check footer/detail | BKAPCHKH |
| BKAPNOTE | 12 | Vendor notes (8 lines × 76 chars) | — |
| BKAPDEP | 6 | Deposits (shared with BKARDEP) | BKARDEP identical |
| BKAPADSC/BKAPDESC/BKAPHDSC | 5 | Description note lines | BK_DESC_* pattern |
| BKAPQUOT | 49 | Quote (BKRFQ_ prefix) | — |

--- — Inventory Item Master

File: `BKICMSTR.B` | Module: IN | Fields: 64 (all confirmed from DDF — Pass 124 2026-06-19)

Primary key: `BKIC_PROD_CODE` (field 1). BKICAMTR and BKICEMTR are structurally **identical** (multi-company mirrors — "A" company and "E" company variants).

| # | Field | Type | Size | Meaning |
|---|-------|------|------|---------|
| 1 | BKIC_PROD_CODE | STRING | 15 | Part number — **primary key** |
| 2 | BKIC_PROD_DESC | STRING | 30 | Description |
| 3 | BKIC_PROD_TYPE | STRING | 1 | Item type code (R/F/A/M/N/L/B/T/K/O — confirmed from HH filter) |
| 4 | BKIC_PROD_UM | STRING | 3 | Unit of measure |
| 5 | BKIC_PROD_CAT | STRING | 4 | Category code |
| 6 | BKIC_PROD_TXBLE | STRING | 1 | Taxable flag |
| 7 | BKIC_PROD_CLASS | STRING | 4 | Class code |
| 8 | BKIC_PROD_RLVL | FLOAT | 8(0) | Reorder level (quantity) |
| 9 | BKIC_PROD_RAMT | FLOAT | 8(0) | Reorder amount (dollar) |
| 10 | BKIC_PROD_LSALE | DATE | 4 | Last sale date |
| 11 | BKIC_PROD_LORD | DATE | 4 | Last order date |
| 12 | BKIC_PROD_LRCPT | DATE | 4 | Last receipt date |
| 13 | BKIC_PROD_ADTR | UBINARY | 2 | Auto-transfer flag |
| 14 | BKIC_PROD_TO | FLOAT | 8(4) | Turnover (turns per year) |
| 15 | BKIC_PROD_LSTC | FLOAT | 8(4) | Last cost |
| 16 | BKIC_PROD_AVGC | FLOAT | 8(4) | Average cost |
| 17 | BKIC_PROD_UOH | FLOAT | 8(2) | Units on hand |
| 18 | BKIC_PROD_UOSO | FLOAT | 8(2) | Units on sales orders |
| 19 | BKIC_PROD_TOTVL | FLOAT | 8(2) | Total inventory value |
| 20 | BKIC_PROD_UOO | FLOAT | 8(2) | Units on open POs |
| 21 | BKIC_PROD_USMTD | FLOAT | 8(2) | Units sold MTD |
| 22 | BKIC_PROD_GSMTD | FLOAT | 8(2) | Gross sales MTD |
| 23 | BKIC_PROD_CMTD | FLOAT | 8(2) | COGS MTD |
| 24 | BKIC_PROD_NSMTD | FLOAT | 8(2) | Net sales MTD |
| 25 | BKIC_PROD_NGMTD | FLOAT | 8(4) | Net gross margin % MTD |
| 26 | BKIC_PROD_USYTD | FLOAT | 8(2) | Units sold YTD |
| 27 | BKIC_PROD_GSYTD | FLOAT | 8(2) | Gross sales YTD |
| 28 | BKIC_PROD_CYTD | FLOAT | 8(2) | COGS YTD |
| 29 | BKIC_PROD_NSYTD | FLOAT | 8(2) | Net sales YTD |
| 30 | BKIC_PROD_NGYTD | FLOAT | 8(4) | Net gross margin % YTD |
| 31 | BKIC_PROD_USLYR | FLOAT | 8(2) | Units sold last year |
| 32 | BKIC_PROD_GSLYR | FLOAT | 8(2) | Gross sales last year |
| 33 | BKIC_PROD_CLYR | FLOAT | 8(2) | COGS last year |
| 34 | BKIC_PROD_NSLYR | FLOAT | 8(2) | Net sales last year |
| 35 | BKIC_PROD_NGLYR | FLOAT | 8(4) | Net gross margin % last year |
| 36 | BKIC_PROD_USVAR | FLOAT | 8(4) | Units sold % variance (YTD vs LYR) |
| 37 | BKIC_PROD_GSVAR | FLOAT | 8(4) | Gross sales % variance |
| 38 | BKIC_PROD_CVAR | FLOAT | 8(4) | COGS % variance |
| 39 | BKIC_PROD_NSVAR | FLOAT | 8(4) | Net sales % variance |
| 40 | BKIC_PROD_NGVAR | FLOAT | 8(4) | Net margin % variance |
| 41 | BKIC_PROD_GLA | STRING | 10 | GL account — inventory asset |
| 42 | BKIC_PROD_DPTA | STRING | 4 | GL dept — inventory asset |
| 43 | BKIC_PROD_GLC | STRING | 10 | GL account — COGS |
| 44 | BKIC_PROD_DPTC | STRING | 4 | GL dept — COGS |
| 45 | BKIC_PROD_GLS | STRING | 10 | GL account — scrap/variance |
| 46 | BKIC_PROD_DPTS | STRING | 4 | GL dept — scrap/variance |
| 47 | BKIC_PROD_PRICE | FLOAT | 8(4) | Base selling price |
| 48 | BKIC_PROD_GLSNT | STRING | 10 | GL account — non-taxable sales |
| 49 | BKIC_PROD_DPTNT | STRING | 4 | GL dept — non-taxable sales |
| 50 | BKIC_PROD_UBO | FLOAT | 8(2) | Units on backorder |
| 51 | BKIC_PROD_PMAT | UBINARY | 2 | Price matrix number |
| 52 | BKIC_PROD_MANUF | STRING | 20 | Manufacturer name |
| 53 | BKIC_PROD_NOTE | STRING | 30 | Note line |
| 54 | BKIC_PROD_AVLAB | FLOAT | 8(4) | Average labor cost per unit |
| 55 | BKIC_PROD_AVSET | FLOAT | 8(4) | Average setup cost per unit |
| 56 | BKIC_PROD_AVOP | FLOAT | 8(4) | Average outside-process cost per unit |
| 57 | BKIC_PROD_AVMAT | FLOAT | 8(4) | Average material cost per unit |
| 58 | BKIC_PROD_AVFO | FLOAT | 8(4) | Average fixed overhead per unit |
| 59 | BKIC_PROD_AVVO | FLOAT | 8(4) | Average variable overhead per unit |
| 60 | BKIC_PROD_EXTRA | STRING | 100 | Extra / user-defined (100 chars) |
| 61 | BKIC_PROD_TAXIN | STRING | 1 | Tax-inclusive flag |
| 62 | BKIC_PROD_ISUPC | STRING | 12 | IS/Avalara UPC code |
| 63 | BKIC_IS_DCODE | STRING | 3 | Avalara tax decision code |
| 64 | BKIC_PROD_LONGP | STRING | 25 | Long part description |

**Notes:**
- The DDF BKICMSTR stores analytics inline (MTD/YTD/LYR sales units + $ + margins + variance, fields 21–40) and four GL account pairs (41–49) — all denormalized for fast reporting.
- Fields for weight, lead time, min order quantity, drawing number, etc. live in `MTICMSTR` (the MT-prefix item master variant) — NOT in BKICMSTR.
- `BKIC_PROD_ADTR` is a UBINARY auto-transfer flag; exact flags not confirmed.
- BKICAMTR and BKICEMTR are byte-for-byte identical in structure — alternate company mirrors of BKICMSTR.

---

## BKIC* Family — Inventory Item Satellite Tables

All confirmed from DDF — Pass 124 2026-06-19. Tables in this family support the core BKICMSTR item master.

### BKICLOCM — Warehouse / Location Master

File: `BKICLOCM.B` | Module: IN | Fields: 12

Defines physical warehouse locations (the `BKIC_LOC_CODE` values referenced in BKICLOC/BKICELOC).

| # | Field | Type | Size | Meaning |
|---|-------|------|------|---------|
| 1 | BKIC_LOCM_CODE | STRING | 10 | Location code — **primary key** |
| 2 | BKIC_LOCM_NAME | STRING | 30 | Location name |
| 3 | BKIC_LOCM_ADDR1 | STRING | 30 | Address line 1 |
| 4 | BKIC_LOCM_ADDR2 | STRING | 30 | Address line 2 |
| 5 | BKIC_LOCM_ADDR3 | STRING | 30 | Address line 3 |
| 6 | BKIC_LOCM_CITY | STRING | 20 | City |
| 7 | BKIC_LOCM_STATE | STRING | 2 | State |
| 8 | BKIC_LOCM_ZIP | STRING | 10 | ZIP |
| 9 | BKIC_LOCM_CNTCT | STRING | 25 | Contact name |
| 10 | BKIC_LOCM_PHONE | STRING | 25 | Phone |
| 11 | BKIC_LOCM_FAX | STRING | 25 | Fax |
| 12 | BKIC_LOCM_TAXGR | STRING | 10 | Tax group (for location-based tax) |

---

### BKICLOC — Item-Location Quantities

File: `BKICLOC.B` | Module: IN | Fields: 32

One row per item × location — tracks quantities and GL accounts per location. `BKICELOC` is **identical** (alternate company "E" mirror).

| # | Field | Type | Size | Meaning |
|---|-------|------|------|---------|
| 1 | BKIC_LOC_PROD | STRING | 15 | Part number (FK → BKICMSTR) — **PK component** |
| 2 | BKIC_LOC_CODE | STRING | 10 | Location code (FK → BKICLOCM) — **PK component** |
| 3 | BKIC_LOC_UOH | FLOAT | 8(2) | Units on hand at this location |
| 4 | BKIC_LOC_UOSO | FLOAT | 8(2) | Units on sales orders (committed) |
| 5 | BKIC_LOC_UBO | FLOAT | 8(2) | Units on backorder |
| 6 | BKIC_LOC_UOO | FLOAT | 8(2) | Units on open POs |
| 7 | BKIC_LOC_GLA | STRING | 10 | GL account — inventory asset (location override) |
| 8 | BKIC_LOC_DPTA | STRING | 4 | GL dept — inventory asset |
| 9 | BKIC_LOC_GLC | STRING | 10 | GL account — COGS |
| 10 | BKIC_LOC_DPTC | STRING | 4 | GL dept — COGS |
| 11 | BKIC_LOC_GLS | STRING | 10 | GL account — scrap/variance |
| 12 | BKIC_LOC_DPTS | STRING | 4 | GL dept — scrap/variance |
| 13 | BKIC_LOC_GLSNT | STRING | 10 | GL account — non-taxable sales |
| 14 | BKIC_LOC_DPTSNT | STRING | 4 | GL dept — non-taxable sales |
| 15 | BKIC_LOC_GLWIP | STRING | 10 | GL account — WIP |
| 16 | BKIC_LOC_DPTWIP | STRING | 4 | GL dept — WIP |
| 17 | BKIC_LOC_UOWO | FLOAT | 8(2) | Units on work orders |
| 18 | BKIC_LOC_UALLOC | FLOAT | 8(2) | Units allocated (reserved) |
| 19 | BKIC_LOC_UWIP | FLOAT | 8(2) | Units in WIP |
| 20 | BKIC_LOC_UIQC | FLOAT | 8(2) | Units in incoming QC hold |
| 21 | BKIC_LOC_EXTRA | STRING | 50 | Extra / user-defined |
| 22 | BKIC_LOC_LCDATE | DATE | 4 | Last count date (cycle count) |
| 23 | BKIC_LOC_BIN | STRING | 15 | Bin code within location |
| 24 | BKIC_LOC_LOT | STRING | 15 | Lot number (if lot-controlled) |
| 25 | BKIC_LOC_SER | STRING | 25 | Serial number (if serial-controlled) |
| 26 | BKIC_LOC_NUM1 | FLOAT | 8(0) | User numeric 1 |
| 27 | BKIC_LOC_NUM2 | FLOAT | 8(0) | User numeric 2 |
| 28 | BKIC_LOC_DATE1 | DATE | 4 | User date 1 |
| 29 | BKIC_LOC_WHCTRL | STRING | 1 | Warehouse control flag |
| 30 | BKIC_LOC_FLAG1 | STRING | 1 | User flag 1 |
| 31 | BKIC_LOC_ALPHA1 | STRING | 30 | User alpha 1 |
| 32 | BKIC_LOC_ALPHA2 | STRING | 30 | User alpha 2 |

---

### BKICPMAT — Item Price Matrix

File: `BKICPMAT.B` | Module: IN/SO | Fields: 85

Per-customer, per-item pricing with quantity breaks. `BKICAPMA` is **identical** (alternate company "A" mirror).

| # | Field | Type | Size | Key groups |
|---|-------|------|------|------------|
| 1 | BKIC_PMAT_CUST | STRING | 10 | Customer code (FK → BKARCUST) — **PK component** |
| 2 | BKIC_PMAT_PCODE | STRING | 15 | Part number (FK → BKICMSTR) — **PK component** |
| 3 | BKIC_PMAT_PNUM | UBINARY | 2 | Price list number — **PK component** |
| 4–13 | BKIC_PMAT_RATE_1..10 | FLOAT×10 | 8(4) | Price rate for each qty break tier (1–10) |
| 14–23 | BKIC_PMAT_QTY_1..10 | FLOAT×10 | 8(2) | Qty break threshold for each tier |
| 24–33 | BKIC_PMAT_PER_1..10 | FLOAT×10 | 8(4) | Percentage discount for each tier |
| 34 | BKIC_PMAT_EXP | DATE | 4 | Expiry date |
| 35 | BKIC_PMAT_DCODE | STRING | 10 | Discount code |
| 36 | BKIC_PMAT_CLASS | STRING | 4 | Customer class |
| 37–46 | BKIC_PMAT_COMM1_1..10 | FLOAT×10 | 8(4) | Salesperson 1 commission by tier |
| 47–56 | BKIC_PMAT_COMM2_1..10 | FLOAT×10 | 8(4) | Salesperson 2 commission by tier |
| 57 | BKIC_PMAT_MIN | FLOAT | 8(2) | Minimum order quantity |
| 58 | BKIC_PMAT_MINPR | FLOAT | 8(4) | Minimum price |
| 59 | BKIC_PMAT_EXTRA | STRING | 50 | Extra / user-defined |
| 60–69 | BKIC_PMAT_ISRET_1..10 | FLOAT×10 | 8(4) | IS retail price by tier |
| 70 | BKIC_PMAT_PDESC | STRING | 30 | Price description |
| 71 | BKIC_PMAT_SDATE | DATE | 4 | Start date |
| 72 | BKIC_PMAT_EDATE | DATE | 4 | End date |
| 73 | BKIC_PMAT_UID | STRING | 40 | Unique identifier |
| 74–81 | BKIC_PMAT_OFFIN/PROMO/SCAND/FRTAL/BILLB/SWELL/ACCRU/OFFCH | FLOAT×8 | 8(2) | Trade-spend types: off-invoice, promotional, scan-down, freight-allowed, bill-back, swell allowance, accrual, off-check |
| 82 | BKIC_PMAT_PFLAG | STRING | 1 | Price flag |
| 83 | BKIC_PMAT_METH | STRING | 11 | Pricing method code |
| 84 | BKIC_PMAT_SRTS | FLOAT | 8(2) | Sort/SRTS amount |
| 85 | BKIC_PMAT_LUMP | FLOAT | 8(2) | Lump sum price |

**Note:** Fields 74–81 (OFFIN/PROMO/SCAND/FRTAL/BILLB/SWELL/ACCRU/OFFCH) are retail trade-spend types — suggests EVO is used by or for retail/grocery channel customers.

---

### BKICTAX — Sales Tax Jurisdiction Table

File: `BKICTAX.B` | Module: IN/AR | Fields: 46

Tax rate and period accumulator by jurisdiction (state + local combo = one row).

| # | Field | Type | Size | Meaning |
|---|-------|------|------|---------|
| 1 | BKIC_TAX_STATE | STRING | 2 | State code — **PK component** |
| 2 | BKIC_TAX_LOCAL | STRING | 2 | Local jurisdiction code — **PK component** |
| 3 | BKIC_TAX_NAME | STRING | 25 | Tax name |
| 4 | BKIC_TAX_NUMBER | STRING | 15 | Tax registration number |
| 5 | BKIC_TAX_RATE | FLOAT | 8(4) | Tax rate |
| 6 | BKIC_TAX_GLACT | STRING | 10 | GL account — tax collected |
| 7 | BKIC_TAX_GLDPT | STRING | 4 | GL dept — tax collected |
| 8 | BKIC_TAX_VENDOR | STRING | 10 | Tax vendor code (AP vendor to remit to) |
| 9–20 | BKIC_TAX_TAXBLE_1..12 | FLOAT×12 | 8(2) | Taxable sales by period 1–12 |
| 21–32 | BKIC_TAX_NONTAX_1..12 | FLOAT×12 | 8(2) | Non-taxable sales by period 1–12 |
| 33–44 | BKIC_TAX_COLECT_1..12 | FLOAT×12 | 8(2) | Tax collected by period 1–12 |
| 45 | BKIC_TAX_OUTSTD | FLOAT | 8(2) | Outstanding tax balance |
| 46 | BKIC_TAX_FRGHT | STRING | 1 | Freight taxable flag (Y/N) |

---

### BKICREQ — Inventory Requisition

File: `BKICREQ.B` | Module: IN | Fields: 41

Requisition for inventory movement or procurement, with links to WO and PO.

| # | Field | Type | Size | Meaning |
|---|-------|------|------|---------|
| 1 | BKIC_REQ_STATUS | STRING | 1 | Status |
| 2 | BKIC_REQ_BY | UBINARY | 2 | Requested-by user number |
| 3 | BKIC_REQ_IDATE | DATE | 4 | Issue date |
| 4 | BKIC_REQ_NUM | FLOAT | 8(0) | Requisition number — **PK** |
| 5 | BKIC_REQ_TYPE | STRING | 1 | Requisition type |
| 6 | BKIC_REQ_TOLOCN | STRING | 10 | To-location code |
| 7 | BKIC_REQ_DDATE | DATE | 4 | Desired delivery date |
| 8 | BKIC_REQ_DESC | STRING | 30 | Description |
| 9–18 | BKIC_REQ_NOTES_1..10 | STRING×10 | 30 | Notes lines 1–10 |
| 19 | BKIC_REQ_RQTY | FLOAT | 8(2) | Requested quantity |
| 20 | BKIC_REQ_MFG | STRING | 25 | Manufacturer |
| 21 | BKIC_REQ_ORDNUM | FLOAT | 8(0) | Linked PO number |
| 22 | BKIC_REQ_ITM_NO | STRING | 9 | PO line item number |
| 23 | BKIC_REQ_ORDQTY | FLOAT | 8(2) | Ordered quantity |
| 24 | BKIC_REQ_FROM | STRING | 10 | From-location code |
| 25 | BKIC_REQ_ERDATE | DATE | 4 | Expected receipt date |
| 26 | BKIC_REQ_PROJ | STRING | 15 | Project code |
| 27 | BKIC_REQ_WOPRE | FLOAT | 8(0) | Linked WO prefix |
| 28 | BKIC_REQ_WOSUF | UBINARY | 2 | Linked WO suffix |
| 29 | BKIC_REQ_OPER | UBINARY | 2 | WO operation number |
| 30 | BKIC_REQ_MATDIM | STRING | 1 | Material dimension flag |
| 31 | BKIC_REQ_PARENT | STRING | 15 | Parent part number |
| 32–38 | BKIC_REQ_TONAME/TOADDR_1..3/TOCITY/TOST/TOZIP | STRING×7 | var | Delivery address block |
| 39 | BKIC_REQ_TOCONT | STRING | 25 | Delivery contact |
| 40 | BKIC_REQ_TOFAX | STRING | 25 | Delivery fax |
| 41 | BKIC_REQ_AGENT | STRING | 25 | Purchasing agent |

---

### BKICDIM — Material Dimensions

File: `BKICDIM.B` | Module: IN | Fields: 47

Physical dimension and metallurgical properties for raw material items. Specialized for metal/coil stock.

| # | Field | Type | Size | Meaning |
|---|-------|------|------|---------|
| 1 | BKICDIM_PARTNO | STRING | 15 | Part number — **PK** |
| 2 | BKICDIM_PARENT | STRING | 15 | Parent part (for cut-from items) |
| 3 | BKICDIM_FIRST | FLOAT | 8(4) | First dimension (width) |
| 4 | BKICDIM_SECOND | FLOAT | 8(4) | Second dimension (length) |
| 5 | BKICDIM_GENERIC | STRING | 15 | Generic part code |
| 6 | BKICDIM_THICK | FLOAT | 8(4) | Thickness |
| 7 | BKICDIM_ALTDESC | STRING | 30 | Alternate description |
| 8 | BKICDIM_ALLOY | STRING | 20 | Metal alloy (e.g., 6061-T6) |
| 9 | BKICDIM_TEMPER | STRING | 20 | Temper designation |
| 10 | BKICDIM_FINISH_1/2 | STRING | 20 | Finish specification (2 lines) |
| 12–17 | BKICDIM_F/S/T_TOL_1..2 | FLOAT×6 | 8(4) | Tolerances: first/second/thickness (min/max) |
| 18 | BKICDIM_DENSITY | FLOAT | 8(4) | Material density |
| 19 | BKICDIM_SETUP | FLOAT | 8(8) | Setup factor |
| 20 | BKICDIM_HARDNES | STRING | 20 | Hardness specification |
| 21 | BKICDIM_TENSIL | STRING | 20 | Tensile strength |
| 22 | BKICDIM_ELONGAT | STRING | 15 | Elongation |
| 23 | BKICDIM_YIELD | STRING | 20 | Yield strength |
| 24–25 | BKICDIM_COATING_1/2 | STRING×2 | 20 | Coating specs |
| 26–27 | BKICDIM_EDGE_1/2 | STRING×2 | 20 | Edge condition |
| 28 | BKICDIM_CAMBER | STRING | 15 | Camber specification |
| 29–30 | BKICDIM_SHPCOND_1/2 | STRING×2 | 20 | Shipping condition |
| 31–33 | BKICDIM_COIL_1..3 | STRING×3 | 10 | Coil identifiers |
| 34–45 | BKICDIM_NOTES_1..12 | STRING×12 | 30 | Notes lines 1–12 |
| 46 | BKICDIM_APPR_BY | STRING | 20 | Approved by |
| 47 | BKICDIM_APPR_DT | DATE | 4 | Approval date |

**Note:** Coil, alloy, temper, and elongation fields indicate this extension targets metal service center operations.

---

### BKICREF — Customer Part Cross-Reference

File: `BKICREF.B` | Module: IN | Fields: 8

Maps EVO internal part numbers to customer-facing part numbers and descriptions.

| # | Field | Type | Size | Meaning |
|---|-------|------|------|---------|
| 1 | BKIC_REF_CUST | STRING | 10 | Customer code (FK → BKARCUST) — **PK component** |
| 2 | BKIC_REF_CODE | STRING | 15 | Internal part number — **PK component** |
| 3 | BKIC_REF_PDESC | STRING | 30 | Internal part description |
| 4 | BKIC_REF_CUSNME | STRING | 30 | Customer name (denormalized) |
| 5 | BKIC_REF_CUSCOD | STRING | 25 | Customer's part number |
| 6 | BKIC_REF_DESC | STRING | 30 | Customer's part description |
| 7 | BKIC_REF_EXTRA | STRING | 50 | Extra / user-defined |
| 8 | BKIC_REF_DESC2 | STRING | 30 | Customer's part description line 2 |

---

### BKICMFG — Manufacturer Cross-Reference

File: `BKICMFG.B` | Module: IN | Fields: 6

Maps EVO part numbers to manufacturer part numbers.

| # | Field | Type | Size | Meaning |
|---|-------|------|------|---------|
| 1 | BKIC_MFG_PCODE | STRING | 15 | Internal part number — **PK component** |
| 2 | BKIC_MFG_MANUF | STRING | 25 | Manufacturer name — **PK component** |
| 3 | BKIC_MFG_MCODE | STRING | 25 | Manufacturer's part number |
| 4 | BKIC_MFG_REMARK_1 | STRING | 30 | Remark line 1 |
| 5 | BKIC_MFG_REMARK_2 | STRING | 30 | Remark line 2 |
| 6 | BKIC_MFG_REMARK_3 | STRING | 30 | Remark line 3 |

---

### BKICALTD — Alternative Item Detail

File: `BKICALTD.B` | Module: IN | Fields: 16

Details for alternate/substitute items with specification lines.

| # | Field | Type | Size | Meaning |
|---|-------|------|------|---------|
| 1 | BKIC_ALTD_PCODE | STRING | 15 | Part number — **PK component** |
| 2 | BKIC_ALTD_TYPE | STRING | 1 | Alternate type code — **PK component** |
| 3 | BKIC_ALTD_DESC | STRING | 30 | Description |
| 4 | BKIC_ALTD_NOTE | STRING | 30 | Note |
| 5–16 | BKIC_ALTD_SPECS_1..12 | STRING×12 | 30 | Specification attributes (12 lines) |

---

### BKICALTP — Alternative Item Pricing

File: `BKICALTP.B` | Module: IN | Fields: 6

Links alternate items with notes.

| # | Field | Type | Size | Meaning |
|---|-------|------|------|---------|
| 1 | BKIC_ALTP_TYPE | STRING | 1 | Alternate type — **PK component** |
| 2 | BKIC_ALTP_PCODE | STRING | 15 | Primary part number — **PK component** |
| 3 | BKIC_ALTP_ACODE | STRING | 25 | Alternate part code |
| 4–6 | BKIC_ALTP_NOTES_1..3 | STRING×3 | 30 | Notes lines |

---

### BKICVAL — Item Valuation Snapshot

File: `BKICVAL.B` | Module: IN | Fields: 4

Periodic inventory valuation snapshot (one row per part per date).

| # | Field | Type | Size | Meaning |
|---|-------|------|------|---------|
| 1 | BKIC_VAL_CODE | STRING | 15 | Part number — **PK component** |
| 2 | BKIC_VAL_DATE | DATE | 4 | Snapshot date — **PK component** |
| 3 | BKIC_VAL_TOTVL | FLOAT | 8(2) | Total inventory value at snapshot |
| 4 | BKIC_VAL_UOH | FLOAT | 8(2) | Units on hand at snapshot |

---

**BKIC* Family Summary Table** (Pass 124 2026-06-19):

| Table | Fields | Role | Multi-Company Mirror |
|-------|--------|------|---------------------|
| BKICMSTR | 64 | Item master (primary) | BKICAMTR ("A"), BKICEMTR ("E") |
| BKICLOCM | 12 | Warehouse/location address master | — |
| BKICLOC | 32 | Item × location quantities + GL accts | BKICELOC ("E") |
| BKICPMAT | 85 | Per-customer price matrix (10 qty break tiers) | BKICAPMA ("A") |
| BKICTAX | 46 | Tax jurisdiction + 12-period accumulators | — |
| BKICREQ | 41 | Inventory requisition (WO + PO links) | — |
| BKICDIM | 47 | Material dimensions/metallurgy | — |
| BKICREF | 8 | Customer part cross-reference | — |
| BKICMFG | 6 | Manufacturer cross-reference | — |
| BKICALTD | 16 | Alternate item detail + specs | — |
| BKICALTP | 6 | Alternate item pricing links | — |
| BKICVAL | 4 | Periodic valuation snapshot | — |

---

## BKGLCOA — GL Chart of Accounts

File: `BKGLCOA.B` | Module: GL | Fields: 65 (all confirmed from DDF — Pass 123 2026-06-19)

Primary key: composite `BKGL_ACCT` + `BKGL_GLDPT`.

| # | Field | Type | Size | Meaning |
|---|-------|------|------|---------|
| 1 | BKGL_ACCT | STRING | 10 | Account number — **PK component** |
| 2 | BKGL_GLDPT | STRING | 4 | Department code — **PK component** |
| 3 | BKGL_ACCTD | STRING | 25 | Account description |
| 4 | BKGL_TYPE | STRING | 1 | Account type (A=asset, L=liability, E=equity, R=revenue, X=expense) |
| 5 | BKGL_CR_DR | STRING | 1 | Normal balance side (C=credit, D=debit) |
| 6 | BKGL_NON_CASH | STRING | 1 | Non-cash account flag (Y = exclude from cash-basis reports) |
| 7 | BKGL_CURRENT_1 | FLOAT | 8(2) | Current-year balance, period 1 |
| 8 | BKGL_CURRENT_2 | FLOAT | 8(2) | Current-year balance, period 2 |
| 9 | BKGL_CURRENT_3 | FLOAT | 8(2) | Current-year balance, period 3 |
| 10 | BKGL_CURRENT_4 | FLOAT | 8(2) | Current-year balance, period 4 |
| 11 | BKGL_CURRENT_5 | FLOAT | 8(2) | Current-year balance, period 5 |
| 12 | BKGL_CURRENT_6 | FLOAT | 8(2) | Current-year balance, period 6 |
| 13 | BKGL_CURRENT_7 | FLOAT | 8(2) | Current-year balance, period 7 |
| 14 | BKGL_CURRENT_8 | FLOAT | 8(2) | Current-year balance, period 8 |
| 15 | BKGL_CURRENT_9 | FLOAT | 8(2) | Current-year balance, period 9 |
| 16 | BKGL_CURRENT_10 | FLOAT | 8(2) | Current-year balance, period 10 |
| 17 | BKGL_CURRENT_11 | FLOAT | 8(2) | Current-year balance, period 11 |
| 18 | BKGL_CURRENT_12 | FLOAT | 8(2) | Current-year balance, period 12 |
| 19 | BKGL_CURRENT_13 | FLOAT | 8(2) | Current-year balance, period 13 (adjustment) |
| 20 | BKGL_CURRENT_14 | FLOAT | 8(2) | Current-year balance, period 14 (adjustment) |
| 21 | BKGL_BUDGET_1 | FLOAT | 8(2) | Budget, period 1 |
| 22 | BKGL_BUDGET_2 | FLOAT | 8(2) | Budget, period 2 |
| 23 | BKGL_BUDGET_3 | FLOAT | 8(2) | Budget, period 3 |
| 24 | BKGL_BUDGET_4 | FLOAT | 8(2) | Budget, period 4 |
| 25 | BKGL_BUDGET_5 | FLOAT | 8(2) | Budget, period 5 |
| 26 | BKGL_BUDGET_6 | FLOAT | 8(2) | Budget, period 6 |
| 27 | BKGL_BUDGET_7 | FLOAT | 8(2) | Budget, period 7 |
| 28 | BKGL_BUDGET_8 | FLOAT | 8(2) | Budget, period 8 |
| 29 | BKGL_BUDGET_9 | FLOAT | 8(2) | Budget, period 9 |
| 30 | BKGL_BUDGET_10 | FLOAT | 8(2) | Budget, period 10 |
| 31 | BKGL_BUDGET_11 | FLOAT | 8(2) | Budget, period 11 |
| 32 | BKGL_BUDGET_12 | FLOAT | 8(2) | Budget, period 12 |
| 33 | BKGL_BUDGET_13 | FLOAT | 8(2) | Budget, period 13 (adjustment) |
| 34 | BKGL_BUDGET_14 | FLOAT | 8(2) | Budget, period 14 (adjustment) |
| 35 | BKGL_1YPAST_1 | FLOAT | 8(2) | 1-year-prior balance, period 1 |
| 36 | BKGL_1YPAST_2 | FLOAT | 8(2) | 1-year-prior balance, period 2 |
| 37 | BKGL_1YPAST_3 | FLOAT | 8(2) | 1-year-prior balance, period 3 |
| 38 | BKGL_1YPAST_4 | FLOAT | 8(2) | 1-year-prior balance, period 4 |
| 39 | BKGL_1YPAST_5 | FLOAT | 8(2) | 1-year-prior balance, period 5 |
| 40 | BKGL_1YPAST_6 | FLOAT | 8(2) | 1-year-prior balance, period 6 |
| 41 | BKGL_1YPAST_7 | FLOAT | 8(2) | 1-year-prior balance, period 7 |
| 42 | BKGL_1YPAST_8 | FLOAT | 8(2) | 1-year-prior balance, period 8 |
| 43 | BKGL_1YPAST_9 | FLOAT | 8(2) | 1-year-prior balance, period 9 |
| 44 | BKGL_1YPAST_10 | FLOAT | 8(2) | 1-year-prior balance, period 10 |
| 45 | BKGL_1YPAST_11 | FLOAT | 8(2) | 1-year-prior balance, period 11 |
| 46 | BKGL_1YPAST_12 | FLOAT | 8(2) | 1-year-prior balance, period 12 |
| 47 | BKGL_1YPAST_13 | FLOAT | 8(2) | 1-year-prior balance, period 13 |
| 48 | BKGL_1YPAST_14 | FLOAT | 8(2) | 1-year-prior balance, period 14 |
| 49 | BKGL_2YPAST_1 | FLOAT | 8(2) | 2-years-prior balance, period 1 |
| 50 | BKGL_2YPAST_2 | FLOAT | 8(2) | 2-years-prior balance, period 2 |
| 51 | BKGL_2YPAST_3 | FLOAT | 8(2) | 2-years-prior balance, period 3 |
| 52 | BKGL_2YPAST_4 | FLOAT | 8(2) | 2-years-prior balance, period 4 |
| 53 | BKGL_2YPAST_5 | FLOAT | 8(2) | 2-years-prior balance, period 5 |
| 54 | BKGL_2YPAST_6 | FLOAT | 8(2) | 2-years-prior balance, period 6 |
| 55 | BKGL_2YPAST_7 | FLOAT | 8(2) | 2-years-prior balance, period 7 |
| 56 | BKGL_2YPAST_8 | FLOAT | 8(2) | 2-years-prior balance, period 8 |
| 57 | BKGL_2YPAST_9 | FLOAT | 8(2) | 2-years-prior balance, period 9 |
| 58 | BKGL_2YPAST_10 | FLOAT | 8(2) | 2-years-prior balance, period 10 |
| 59 | BKGL_2YPAST_11 | FLOAT | 8(2) | 2-years-prior balance, period 11 |
| 60 | BKGL_2YPAST_12 | FLOAT | 8(2) | 2-years-prior balance, period 12 |
| 61 | BKGL_2YPAST_13 | FLOAT | 8(2) | 2-years-prior balance, period 13 |
| 62 | BKGL_2YPAST_14 | FLOAT | 8(2) | 2-years-prior balance, period 14 |
| 63 | BKGL_EXTRA | STRING | 50 | Extra / user-defined field |
| 64 | BKGL_1YPAST_YE | FLOAT | 8(2) | 1-year-prior year-end balance |
| 65 | BKGL_2YPAST_YE | FLOAT | 8(2) | 2-years-prior year-end balance |

**Notes:**
- Periods 1–12 = accounting months; periods 13–14 = adjustment/closing periods.
- All balance, budget, and prior-year amounts are stored inline (denormalized for fast balance sheet / P&L queries).
- `BKGL_NON_CASH` flag (field 6) — missing from prior documentation — marks accounts to exclude from cash-basis reporting.
- Two full years of prior history (1YPAST + 2YPAST) plus two year-end snapshots (fields 64–65) support multi-year comparative reports.
- The companion table `BKGLDESC` stores free-text description lines for accounts (BK_DESC_CODE → BKGL_ACCT).

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

File: `BKSYMSTR.B` | Module: System | Fields: 286 | Companion: BKSYPRTR.B

Single-record per-company global config table. All 286 DDF fields confirmed from
`samples/ddf/schema.md`. Field name prefix `BKSY_`. Programs access as `BKSY.*` variable.

The 286 fields are organized as **embedded arrays** (not separate records) —
the single BKSYMSTR record holds multiple data slots via array suffixes (_1.._N).

### Field groups

| Group | DDF fields | Description |
|-------|-----------|-------------|
| Auto-number counters | 1–4, 223, 251–253 | Next invoice/PO/GJ/SO/record numbers |
| Tax defaults | 5, 159–160 | Default tax rate + GL accounts |
| Payment terms array (20×7=140) | 6–125, 255–274 | 20 terms slots, 7 fields each |
| Company identity | 126–129 | Name + 3 address lines |
| AR defaults | 130–140, 173–174, 226–227, 235–239, 220 | Ship-via, GL, aging, interest |
| AP defaults | 141–148, 153–158, 240–244, 221 | Entries, GL, aging buckets |
| GL defaults | 149–172 | Clearing, retained earnings, fiscal year, AR interest |
| PO defaults | 161–164, 228–229, 275–276 | Tax, freight, RNI, INR GL accounts |
| Bank accounts array (9×6=54) | 175–219, 278–286 | 9 banks: num/bal/name/act/dept/currency |
| Payroll | 222, 245–250 | PR check account + 6 deduction names |
| System paths | 167, (HELP_PATH) | Program path prefix, help path |
| Presentation flags | 230–234 | Plain invoice/PO/stmt/checks, form company |
| Misc | 224–225, 254, 277 | AUTO_BO, RTS_DEF, TAL, EXTRA(173b) |

### Key fields (individual, not array elements)

| Field | DDF# | Type | Meaning |
|-------|------|------|---------|
| BKSY_ARINV_NUM | 1 | FLOAT | Next AR invoice number (auto-increment) |
| BKSY_APINV_NUM | 2 | FLOAT | Next AP invoice number |
| BKSY_APPO_NUM | 3 | FLOAT | Next AP/PO number |
| BKSY_GJ_NUM | 4 | FLOAT | Next GJ transaction number |
| BKSY_TAX_RATE | 5 | FLOAT(2) | Default sales tax rate |
| BKSY_COMP_NAME | 126 | STRING(25) | Company name |
| BKSY_COMP_ADD1 | 127 | STRING(25) | Company address line 1 |
| BKSY_COMP_ADD2 | 128 | STRING(25) | Company address line 2 |
| BKSY_COMP_CSZ | 129 | STRING(25) | Company city/state/zip |
| BKSY_AR_SHP_VIA | 130 | STRING(15) | AR default ship-via code |
| BKSY_AR_SLSP | 131 | UBINARY | AR default salesperson |
| BKSY_AR_ENTBY | 132 | STRING(5) | AR default entered-by |
| BKSY_AR_TAXABL | 133 | STRING(1) | AR default taxable flag |
| BKSY_AR_TURNOFF | 139 | STRING(1) | AR feature turnoff flag |
| BKSY_AR_PEL | 140 | STRING(1) | AR PEL flag |
| BKSY_AR_GLACT | 151 | STRING(10) | AR GL account |
| BKSY_AR_GLDPT | 152 | STRING(4) | AR GL department |
| BKSY_AR_DISCGL | 153 | STRING(10) | AR discount GL account |
| BKSY_AR_DISCDPT | 154 | STRING(4) | AR discount GL dept |
| BKSY_AP_GLACT | 155 | STRING(10) | AP GL account |
| BKSY_AP_GLDPT | 156 | STRING(4) | AP GL department |
| BKSY_AP_DISCGL | 157 | STRING(10) | AP discount GL account |
| BKSY_AP_DISCDPT | 158 | STRING(4) | AP discount GL dept |
| BKSY_TAX_GLACT | 159 | STRING(10) | Tax GL account |
| BKSY_TAX_GLDPT | 160 | STRING(4) | Tax GL department |
| BKSY_PO_TAXGL | 161 | STRING(10) | PO tax GL account |
| BKSY_PO_TAXDPT | 162 | STRING(4) | PO tax GL dept |
| BKSY_PO_FREIGHT | 163 | STRING(10) | PO freight GL account |
| BKSY_PO_FRGTDPT | 164 | STRING(4) | PO freight GL dept |
| BKSY_GL_RETEARN | 165 | STRING(10) | Retained earnings GL |
| BKSY_GLDPT_RET | 166 | STRING(4) | Retained earnings GL dept |
| BKSY_PRGS_WHR | 167 | STRING(40) | **Program path prefix** — used to chain sub-programs (e.g., BKAPHA) |
| BKSY_FISCAL_YR | 168 | DATE | Fiscal year start date |
| BKSY_GL_RELYR | 169 | STRING(10) | GL related year account |
| BKSY_GLDPT_RELY | 170 | STRING(4) | GL related year dept |
| BKSY_GL_ARINTR | 171 | STRING(10) | AR interest income GL |
| BKSY_GLDPT_ARIN | 172 | STRING(4) | AR interest income GL dept |
| BKSY_AR_INT_RTE | 173 | FLOAT(2) | AR interest rate |
| BKSY_AR_INT_DAY | 174 | UBINARY | AR interest grace days |
| BKSY_AR_CHKACT | 220 | UBINARY | AR bank account index (1–9) |
| BKSY_AP_CHKACT | 221 | UBINARY | AP bank account index (1–9) |
| BKSY_PR_CHKACT | 222 | UBINARY | Payroll bank account index (1–9) |
| BKSY_ARSO_NUM | 223 | FLOAT | Next AR/SO sales order number |
| BKSY_AUTO_BO | 224 | STRING(1) | Auto backorder flag |
| BKSY_RTS_DEF | 225 | STRING(1) | RTS default flag |
| BKSY_AR_FREIGHT | 226 | STRING(10) | AR freight GL account |
| BKSY_AR_FRGTDPT | 227 | STRING(4) | AR freight GL dept |
| BKSY_PO_RNI | 228 | STRING(10) | PO received-not-invoiced GL |
| BKSY_PO_RNIDPT | 229 | STRING(4) | PO RNI GL dept |
| BKSY_PLAIN_INV | 230 | STRING(1) | Plain (no logo) invoice flag |
| BKSY_PLAIN_PO | 231 | STRING(1) | Plain PO flag |
| BKSY_PLAIN_STMT | 232 | STRING(1) | Plain statement flag |
| BKSY_PLAIN_CHKS | 233 | STRING(1) | Plain checks flag |
| BKSY_FORM_CMPNY | 234 | STRING(1) | Form company flag |
| BKSY_AP_RECNUM | 251 | FLOAT | AP record number counter |
| BKSY_GJ_RECNUM | 252 | FLOAT | GJ record number counter |
| BKSY_AR_RECNUM | 253 | FLOAT | AR record number counter |
| BKSY_TAL | 254 | STRING(1) | TAL flag |
| BKSY_PO_INR | 275 | STRING(10) | PO INR GL account |
| BKSY_PO_INRDPT | 276 | STRING(4) | PO INR GL dept |
| BKSY_EXTRA | 277 | STRING(173) | Overflow/extra config blob |
| BKSY_GL_CLRING | 149 | STRING(10) | GL clearing account |
| BKSY_GLDPT_CLR | 150 | STRING(4) | GL clearing dept |

### Embedded arrays

**Payment terms (20 slots, fields 6–125, 255–274):**
Each slot N (1–20) has 7 sub-fields:
`TERMS_N` (20ch desc), `TRM_AMT_N` (amount), `TRM_TYP_N` (type code), `TRM_DAY_N` (days),
`TRM_EOM_N` (EOM flag), `TRM_MAX_N` (max amount), `TRM_DISC_N` (discount %)

**Bank accounts (9 slots, fields 175–219, 278–286):**
Each slot N (1–9) has 6 sub-fields:
`CHK_NUM_N` (check number), `CHK_BAL_N` (balance), `CHK_NAME_N` (30ch name),
`CHK_CHKACT_N` (GL account), `CHK_CHKDPT_N` (GL dept), `CHK_CHKCUR_N` (3ch currency code)
Module-to-bank linkage: AR_CHKACT / AP_CHKACT / PR_CHKACT hold the bank slot index (1–9)

**AR/AP aging buckets (5 slots each, fields 235–244):**
`AR_AGING_1..5` and `AP_AGING_1..5` — day thresholds for 5-bucket aging reports

**AR/AP end-of-document descriptions (5 slots each):**
`AR_ENDDESC_1..5` (30ch each) — text appended to invoices; `AP_ENDDESC_1..5` for AP docs

**Payroll optional deduction names (6 slots, fields 245–250):**
`PR_ODNAME_1..6` (12ch each) — labels for payroll optional deductions

### BKSYPRTR — Printer Registry (companion)

File: `BKSYPRTR.B` | Fields: 6+ (separate table, one record per printer)

| # | Field | Type | Size | Meaning |
|---|-------|------|------|---------|
| 1 | BKSY_PRTR_NAME | STRING | 30 | Printer display name |
| 2 | BKSY_PRTR_EXEC | STRING | 8 | Executable/driver type |
| 3 | BKSY_PRTR_TAS | STRING | 1 | TAS mode flag |
| 4 | BKSY_PRTR_LPTNM | UBINARY | 1 | LPT port number |
| 5 | BKSY_PRTR_TYPE | STRING | 8 | Printer type code |
| 6 | BKSY_PRTR_PWDT | UBINARY | 2 | Paper width |

*(Full 286-field DDF list in `samples/ddf/schema.md` under `## BKSYMSTR` — Pass 121 2026-06-19)*

---

## BKSOX — Sales Order Invoice Extract

File: `BKSOX.B` | Module: SO/GL | Fields: 25 (all confirmed from DDF — Pass 123 2026-06-19)

Summary extract table; one row per posted AR invoice. Used for GL posting summaries and cross-company reporting.

| # | Field | Type | Size | Meaning |
|---|-------|------|------|---------|
| 1 | BKSOX_COMPANY | STRING | 2 | Company code |
| 2 | BKSOX_INVCNUM | FLOAT | 8(0) | Invoice number (FK → BKARINV) — **PK component** |
| 3 | BKSOX_INVCDATE | DATE | 4 | Invoice date |
| 4 | BKSOX_CUSTCODE | STRING | 10 | Customer code (FK → BKARCUST) |
| 5 | BKSOX_CUSTNAME | STRING | 30 | Customer name (denormalized) |
| 6 | BKSOX_SUBTOT | FLOAT | 8(2) | Invoice subtotal |
| 7 | BKSOX_TAXAMT | FLOAT | 8(2) | Tax amount |
| 8 | BKSOX_FREIGHT | FLOAT | 8(2) | Freight charge |
| 9 | BKSOX_DEPOSIT | FLOAT | 8(2) | Deposit applied |
| 10 | BKSOX_RETEN | FLOAT | 8(2) | Retention amount |
| 11 | BKSOX_TOTAL | FLOAT | 8(2) | Invoice total |
| 12 | BKSOX_CURRENCY | STRING | 3 | Currency code |
| 13 | BKSOX_SONUM | FLOAT | 8(0) | Source sales order number |
| 14 | BKSOX_CUSTPO | STRING | 25 | Customer PO number |
| 15 | BKSOX_TERMSCODE | UBINARY | 2 | Terms number (index into BKSYMSTR terms array) |
| 16 | BKSOX_TERMSDESC | STRING | 20 | Terms description (denormalized) |
| 17 | BKSOX_INVCDESC | STRING | 30 | Invoice description |
| 18 | BKSOX_SHIPDATE | DATE | 4 | Ship date |
| 19 | BKSOX_SHIPPER | FLOAT | 8(0) | Shipper ID number |
| 20 | BKSOX_JOBNUM | STRING | 15 | Job number |
| 21 | BKSOX_TAXCODE | STRING | 10 | Tax code |
| 22 | BKSOX_TAXNAME | STRING | 30 | Tax name (denormalized) |
| 23 | BKSOX_POSTDATE | DATE | 4 | GL post date |
| 24 | BKSOX_ARCHDATE | DATE | 4 | Archive date |
| 25 | BKSOX_ENTDATE | DATE | 4 | Entry date |

**Notes:**
- `BKSOX_SHIPPER` is a FLOAT (shipper ID number), not a text carrier name — the shipper name would be looked up separately.
- Three date fields: invoice date (3), ship date (18), GL post date (23), archive date (24), and entry date (25).
- `BKSOXH` (BKSOXH.B) is structurally **identical** (same 25 fields, same names, same sizes) — it is the historical-period archive of the same extract data.

---

---

## BKGLTRAN — GL Journal Transactions

File: `BKGLTRAN.B` | Module: GL | Fields: 16

The audit-trail transaction table. Every accounting posting (AR, AP, PO, WO, etc.) creates
a BKGLTRAN record with the GL account, amount, D/C flag, and source reference.

| # | Field | Type | Size | Meaning |
|---|-------|------|------|---------|
| 1 | BKGL_TRN_GLACCT | STRING | 10 | GL account number (FK → BKGLCOA) |
| 2 | BKGL_TRN_GLDPT | STRING | 4 | GL department |
| 3 | BKGL_TRN_DATE | DATE | 4 | Transaction date |
| 4 | BKGL_TRN_CODE | STRING | 10 | Source code (customer/vendor/item) |
| 5 | BKGL_TRN_INVC | STRING | 10 | Invoice/reference number |
| 6 | BKGL_TRN_DESC | STRING | 25 | Transaction description |
| 7 | BKGL_TRN_DC | STRING | 1 | Debit/credit flag |
| 8 | BKGL_TRN_AMT | FLOAT | 8 | Transaction amount |
| 9 | BKGL_TRN_TYPE | STRING | 2 | Transaction type code (AR/AP/WO/etc.) |
| 10 | BKGL_TRN_ENTDTE | DATE | 4 | Entry date (when posted to system) |
| 11 | BKGL_TRN_EXTRA | STRING | 25 | Extra/notes |
| 12 | BKGL_TRN_TRXN | FLOAT | 8 | Transaction sequence number |
| 13 | BKGL_TRN_POST | STRING | 1 | Posted flag (Y=posted, N=pending) |
| 14 | BKGL_TRN_PERIOD | UBINARY | 2 | Fiscal period number |
| 15 | BKGL_TRN_BATCH | FLOAT | 8 | Batch number (for batch posting) |
| 16 | BKGL_TRN_PART | STRING | 15 | Item/part number (where applicable) |

**Confidence: 80/100** — All 16 fields extracted and interpreted; TYPE code values not confirmed.

---

## BKARINVT — AR Invoice Transactions (Payments)

File: `BKARINVT.B` | Module: AR | Fields: 23

The AR payment application table. Each row represents a payment applied to an invoice.
This is the table EvoERP uses to track what's been paid, when, and by which check/deposit.

| # | Field | Type | Size | Meaning |
|---|-------|------|------|---------|
| 1 | BKAR_INVT_CODE | STRING | 10 | Customer code (PK part 1) |
| 2 | BKAR_INVT_DATE | DATE | 4 | Payment application date |
| 3 | BKAR_INVT_NUM | FLOAT | 8 | Invoice number (PK part 2) |
| 4 | BKAR_INVT_AMT | FLOAT | 8 | Invoice amount |
| 5 | BKAR_INVT_AMTRM | FLOAT | 8 | Amount remaining (open balance) |
| 6 | BKAR_INVT_DESC | STRING | 25 | Description |
| 7 | BKAR_INVT_TERMN | UBINARY | 2 | Terms net days |
| 8 | BKAR_INVT_TYPE | STRING | 1 | Transaction type (I=invoice, C=credit, D=deposit) |
| 9 | BKAR_INVT_GLDPT | STRING | 4 | GL department |
| 10 | BKAR_INVT_SLSP | UBINARY | 2 | Salesperson 1 |
| 11 | BKAR_INVT_DEPST | STRING | 1 | Deposit status flag |
| 12 | BKAR_INVT_SLSP2 | UBINARY | 2 | Salesperson 2 |
| 13 | BKAR_INVT_EXTRA | STRING | 50 | Extra/notes |
| 14 | BKAR_INVT_PDATE | DATE | 4 | Payment date |
| 15 | BKAR_INVT_MCRAT | FLOAT | 8 | Multi-currency exchange rate |
| 16 | BKAR_INVT_MCCOD | STRING | 3 | Multi-currency code |
| 17 | BKAR_INVT_TRXN | FLOAT | 8 | Transaction sequence number |
| 18 | BKAR_INVT_CHKNO | FLOAT | 8 | Check number that paid this invoice |
| 19 | BKAR_INVT_DEPNO | FLOAT | 8 | Deposit number (FK → BKARDEP) |
| 20 | BKAR_INVT_CHKAC | UBINARY | 2 | Check account (bank account) |
| 21 | BKAR_INVT_OPEND | DATE | 4 | Open date (when invoice opened) |
| 22 | BKAR_INVT_CLOSD | DATE | 4 | Close date (when fully paid) |
| 23 | BKAR_INVT_NORMP | STRING | 1 | Normal payment flag (Y/N) |

**Key workflow:** When AR payment is posted, a BKARINVT row is updated: AMTRM decreases
to zero when fully paid, CLOSD is populated, and CHKNO/DEPNO link to the payment source.

**Confidence: 78/100** — All 23 fields extracted and interpreted from names; TYPE code values
not confirmed.

---

## BKARDEP — AR Customer Deposits

File: `BKARDEP.B` | Module: AR/MA | Fields: 6

Customer deposit master. Referenced by MA module (T7MAPDEPO) and linked from BKARINVT.BKAR_INVT_DEPNO.

| # | Field | Type | Size | Meaning |
|---|-------|------|------|---------|
| 1 | BKAR_DEP_DEPNO | FLOAT | 8 | Deposit number (PK) |
| 2 | BKAR_DEP_CUST | STRING | 10 | Customer code (FK → BKARCUST) |
| 3 | BKAR_DEP_DATE | DATE | 4 | Deposit date |
| 4 | BKAR_DEP_SO | FLOAT | 8 | Sales order number (FK → BKSOMSTR) |
| 5 | BKAR_DEP_SR | STRING | 1 | Status/received flag |
| 6 | BKAR_DEP_EXTRA | STRING | 50 | Extra/notes |

**Confidence: 72/100** — All 6 fields interpreted; SR flag values not confirmed.

---

## BKARCHKH / BKARCHKF — AP Check History

Files: `BKARCHKH.B`, `BKARCHKF.B` | Module: AP | Fields: 12 each (identical schema)

Note: Despite the "AR" prefix, these use BKAP_CHK_ fields and are AP check records.
BKARCHKH = active/history, BKARCHKF = final/cleared checks. Both store same data at
different lifecycle stages.

| # | Field | Type | Size | Meaning |
|---|-------|------|------|---------|
| 1 | BKAP_CHK_VNDCOD | STRING | 10 | Vendor code (FK → BKAPVEND) |
| 2 | BKAP_CHK_INVNUM | STRING | 10 | Invoice number being paid |
| 3 | BKAP_CHK_INVAMT | FLOAT | 8 | Invoice total amount |
| 4 | BKAP_CHK_AMTPD | FLOAT | 8 | Amount paid by this check |
| 5 | BKAP_CHK_DISC | FLOAT | 8 | Discount taken |
| 6 | BKAP_CHK_TYPE | STRING | 1 | Payment type (C=check, W=wire, etc.) |
| 7 | BKAP_CHK_DESC | STRING | 25 | Description |
| 8 | BKAP_CHK_INVDTE | DATE | 4 | Invoice date |
| 9 | BKAP_CHK_NUM | FLOAT | 8 | Check number |
| 10 | BKAP_CHK_CHKACT | UBINARY | 2 | Check account (bank account) |
| 11 | BKAP_CHK_CHKDTE | DATE | 4 | Check date |
| 12 | BKAP_CHK_ISCUR | STRING | 3 | Currency code (multi-currency) |

**Confidence: 78/100** — All 12 fields interpreted; TYPE flag values not confirmed.

---

*Document updated: 2026-06-17 (Pass 25)*
*Source: `samples/ddf/schema.md` + SRC analysis + DFM analysis*
*Confidence: 68/100 — Field names and types confirmed from DDF schema. Field meanings inferred from naming conventions and confirmed where SRC source code references the fields directly.*
