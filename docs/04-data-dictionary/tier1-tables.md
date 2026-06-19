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

## BKSO* Family — SO Satellite Tables

All confirmed from DDF + rwn_symbols.json — Pass 127 2026-06-19.

### Critical Architecture: SO Uses BKARINV/BKARINVL Directly

There is **no separate BKSOMSTR or BKSODET** table. The Sales Order module stores open orders in `BKARINV` (header) and `BKARINVL` (detail lines) — the same tables used by the AR module. The `BKAR_INV_INVCD` field distinguishes the document lifecycle stage; `BKAR_INV_RTS` = "release to ship" flag. An SO becomes an AR invoice when it is posted.

This was confirmed by inspecting T7SOB, T7SOC, T7SOF, T7SOJ, T7SOR, T7SOS etc. from rwn_symbols.json — every SO program opens BKARINV and BKARINVL as its primary tables; no BKSOMSTR appears in any db_files list.

The BKSO* tables are all **satellite support** tables:

---

### BKSOHLOT / BKSOHSER — SO Lot/Serial Holding

Files: `BKSOHLOT.B`, `BKSOHSER.B` | Module: SO/IN | Fields: 14 each (identical)

Pre-pick lot and serial number staging for open SO lines — populated during pick/pack and cleared on invoice post. Both tables use the `BKAR_TXN_*` prefix and are **byte-for-byte identical to BKARTXN**. BKSOHLOT = lot tracking; BKSOHSER = serial number tracking.

| # | Field | Meaning |
|---|-------|---------|
| 1 | BKAR_TXN_SONUM | SO number — **PK component** |
| 2 | BKAR_TXN_CODE | Part code — **PK component** |
| 3 | BKAR_TXN_DESC | Part description |
| 4–14 | (same as BKARTXN) | See BKARTXN table above |

---

### BKSOLOCK — SO Record Lock

File: `BKSOLOCK.B` | Module: SO | Fields: 5

Pessimistic record-lock table for open SO headers. Prevents two users from editing the same order simultaneously.

| # | Field | Type | Meaning |
|---|-------|------|---------|
| 1 | BKSO_LOCK_REC | STRING | SO/invoice number being locked — **PK** |
| 2 | BKSO_LOCK_ITEM | STRING | Item or field being locked (25 chars) |
| 3 | BKSO_LOCK_DATE | DATE | Lock date |
| 4 | BKSO_LOCK_TIME | TIME | Lock time |
| 5 | BKSO_LOCK_WHO | STRING | User who holds the lock (25 chars) |

---

### BKSONOTE — SO Order Notes

File: `BKSONOTE.B` | Module: SO | Fields: 5

Order-level notes on SOs, using the standard BK_DESC_* pattern. Same 5-field structure as BKAPDESC/BKARDESC.

---

### BKSOPO — MRP-Planned PO Linked to SO

File: `BKSOPO.B` | Module: SO/MRP | Fields: 16

Uses `BKMRP_PO_*` prefix. Stores MRP-generated planned purchase orders that are pegged to specific SO lines. Links demand (SO) to supply (PO) for outside-process or buy components.

| # | Field | Type | Meaning |
|---|-------|------|---------|
| 1 | BKMRP_PO_UID | STRING | Planned order UID (unique ID) — **PK** |
| 2 | BKMRP_PO_VEND | STRING | Vendor code (FK → BKAPVEND) |
| 3 | BKMRP_PO_DATE | DATE | Plan date |
| 4 | BKMRP_PO_ERD | DATE | Expected receipt date |
| 5 | BKMRP_PO_PART | STRING | Part code |
| 6 | BKMRP_PO_QTY | FLOAT | Planned quantity |
| 7 | BKMRP_PO_PRICE | FLOAT | Unit price |
| 8 | BKMRP_PO_WOPRE | FLOAT | WO prefix (FK → WORKORD) |
| 9 | BKMRP_PO_WOSUF | UBINARY | WO suffix |
| 10 | BKMRP_PO_PLANR | STRING | Planner code (4 chars) |
| 11 | BKMRP_PO_CONF | STRING | Confirmed flag |
| 12 | BKMRP_PO_DONE | STRING | Done/completed flag (10 chars) |
| 13 | BKMRP_PO_MTREC | UBINARY | MT record link |
| 14 | BKMRP_PO_EXTRA | STRING | Extra 50 chars |
| 15 | BKMRP_PO_EST | STRING | Estimate number (FK → ISESTCFG) |
| 16 | BKMRP_PO_ESTLNE | FLOAT | Estimate line number |

---

**BKSO* Family Summary Table** (Pass 127 2026-06-19):

| Table | Fields | Role | Mirror |
|-------|--------|------|--------|
| (BKARINV) | 84 | **SO header** — same table as AR invoice | shared with AR |
| (BKARINVL) | 28 | **SO detail lines** — same table as AR lines | shared with AR |
| BKSOHLOT | 14 | Pre-pick lot staging for open SO lines | BKARTXN (identical) |
| BKSOHSER | 14 | Pre-pick serial staging for open SO lines | BKARTXN (identical) |
| BKSOLOCK | 5 | SO record locking | — |
| BKSONOTE | 5 | SO order notes | BK_DESC_* pattern |
| BKSOPO | 16 | MRP-planned PO pegged to SO (BKMRP_PO_ prefix) | — |
| BKSOX | 25 | SO invoice extract (denormalized GL summary) | — |
| BKSOXH | 25 | SO invoice extract history | BKSOX (identical) |

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

---

## BKAR* Family — AR Satellite Tables

All confirmed from DDF — Pass 126 2026-06-19.

### Mirror Architecture (key insight)

The BKAR* family uses four structural mirrors of core tables:

| Source Table | Mirror(s) | Reason |
|---|---|---|
| BKARCUST (106f) | BKARECST (106f) | "E" company; BKARSHIP (106f) = ship-to address record |
| BKARINV (84f) | BKARHINV (84f) = history; BKARRINV (84f) = returns |
| BKARINVL (28f) | BKARHIVL (28f) = hist lines; BKARRIVL (28f) = return lines; BKARSIVL (28f) = ship-to lines |
| BKARTXN (14f) | BKARTXNB (14f) = batch variant; BKARTXNS (14f) = serial variant |

---

### BKARCUST — AR Customer Master (already documented above)

Full 106-field table: see §BKARCUST at the top of this file.

---

### BKARECST — "E" Company Customer Master

File: `BKARECST.B` | Module: AR (multi-company) | Fields: 106

Byte-for-byte identical schema to BKARCUST. Stores customer records for the "E" company in a multi-company deployment. All field names, types, and offsets are the same as BKARCUST.

---

### BKARSHIP — Ship-To Address Master

File: `BKARSHIP.B` | Module: AR | Fields: 106

Byte-for-byte identical schema to BKARCUST. Stores named ship-to locations for customers who ship to multiple addresses. PK is `BKAR_CUSTCODE` (the ship-to code, not the billing customer code). Selected via `BKARCUST.BKAR_SHIPTO` → BKARSHIP lookup. Contains its own set of contacts/phones/emails, analytics accumulators, and compliance fields.

---

### BKARINVV — AR Voucher with Inline GL Distribution

File: `BKARINVV.B` | Module: AR | Fields: 77

AR voucher record with inline 10-slot GL distribution — analogous to BKAPINVL (75-slot) but for AR manual credits/adjustments. Used when AR needs to distribute a transaction across multiple GL accounts without creating a full invoice.

**Header (fields 1–11):**

| # | Field | Type | Size | Meaning |
|---|-------|------|------|---------|
| 1 | BKAR_INVV_CODE | STRING | 10 | Customer code (FK → BKARCUST) — **PK component** |
| 2 | BKAR_INVV_NUM | STRING | 6 | Voucher number — **PK component** |
| 3 | BKAR_INVV_DATE | DATE | 4 | Voucher date |
| 4 | BKAR_INVV_DESC | STRING | 24 | Description |
| 5 | BKAR_INVV_CHK | UBINARY | 2 | Check number |
| 6 | BKAR_INVV_TERMD | STRING | 10 | Terms description |
| 7 | BKAR_INVV_TERMN | UBINARY | 2 | Terms number |
| 8 | BKAR_INVV_TYPED | STRING | 10 | Type description |
| 9 | BKAR_INVV_TYPEN | UBINARY | 2 | Type number |
| 10 | BKAR_INVV_TAMT | FLOAT | 8(2) | Total amount |
| 11 | BKAR_INVV_TDC | STRING | 1 | Total debit/credit flag |

**GL Distribution Block (10 slots × 5 sub-fields, fields 12–61):**

| Group | Fields | Meaning |
|-------|--------|---------|
| BKAR_INVV_GLACT_1..10 | 12–21 | GL account number |
| BKAR_INVV_GLDPT_1..10 | 22–31 | GL department |
| BKAR_INVV_DC_1..10 | 32–41 | Debit/credit indicator |
| BKAR_INVV_GLD_1..10 | 42–51 | GL description (25 chars each) |
| BKAR_INVV_DAMT_1..10 | 52–61 | Distribution amount |

**Footer (fields 62–77):**

| # | Field | Meaning |
|---|-------|---------|
| 62 | BKAR_INVV_ARDPT | AR department |
| 63–64 | BKAR_INVV_SLSP_1/2 | Salesperson numbers |
| 65–66 | BKAR_INVV_COMPR_1/2 | Commission percentages |
| 67 | BKAR_INVV_FRGHT | Freight |
| 68 | BKAR_INVV_COOP | Co-op/promotional allowance |
| 69 | BKAR_INVV_TAX | Tax amount |
| 70 | BKAR_INVV_COGS | Cost of goods sold |
| 71–75 | BKAR_INVV_FLAG_1..5 | Status flags |
| 76 | BKAR_INVV_EXTRA | Extra 50 chars |
| 77 | BKAR_INVV_ISCUR | Multi-currency code |

---

### BKAREIVT — Extended AR Invoice Transaction

File: `BKAREIVT.B` | Module: AR (extended) | Fields: 24

Extended version of BKARINVT (23f). Adds `BKAB_PERIOD` (a LOGICAL bit-field overlay used for period tracking) and `BKAR_INVT_NORMP` (normal-period flag). Otherwise identical structure to BKARINVT.

| Extra Field | Meaning |
|---|---|
| BKAB_PERIOD (field 4, LOGICAL overlay) | Period accumulator bit array |
| BKAR_INVT_NORMP (field 24, STRING 1) | Normal-period posting flag |

---

### BKARINVI — AR Invoice Staging

File: `BKARINVI.B` | Module: AR | Fields: 16

Staging buffer populated during invoice creation before lines are committed to BKARINVL. PK: `BKAR_INVI_SONUM` + `BKAR_INVI_INVNM`. Cleared once the invoice is posted.

| # | Field | Type | Meaning |
|---|-------|------|---------|
| 1 | BKAR_INVI_SONUM | FLOAT | SO number — **PK component** |
| 2 | BKAR_INVI_INVNM | FLOAT | Invoice number — **PK component** |
| 3 | BKAR_INVI_ESD | DATE | Expected ship date |
| 4 | BKAR_INVI_PCODE | STRING | Part code |
| 5 | BKAR_INVI_PQTY | FLOAT | Quantity |
| 6 | BKAR_INVI_PPRCE | FLOAT | Unit price |
| 7 | BKAR_INVI_PDISC | FLOAT | Discount % |
| 8 | BKAR_INVI_PEXT | FLOAT | Extended price |
| 9 | BKAR_INVI_PCOGS | FLOAT | Cost of goods |
| 10 | BKAR_INVI_ITYPE | STRING | Item type |
| 11 | BKAR_INVI_EXTRM | FLOAT | Extended remaining |
| 12–13 | BKAR_INVI_COMM_1/2 | FLOAT | Commission % per salesperson |
| 14 | BKAR_INVI_FRGHT | FLOAT | Freight |
| 15 | BKAR_INVI_COOP | FLOAT | Co-op allowance |
| 16 | BKAR_INVI_TAX | FLOAT | Tax amount |

---

### BKART — AR Payment Transaction Log

File: `BKART.B` | Module: AR | Fields: 12

One record per AR payment application event. PK: `BKART_CUST` + `BKART_TRXN`. The `BKART_NOTE` flag links to BKARTNOT for detail lines.

| # | Field | Type | Meaning |
|---|-------|------|---------|
| 1 | BKART_CUST | STRING | Customer code — **PK component** |
| 2 | BKART_TRXN | FLOAT | Transaction number — **PK component** |
| 3 | BKART_TYPE | STRING | Transaction type (P=payment, C=credit, D=debit) |
| 4 | BKART_DISC | FLOAT | Discount taken |
| 5 | BKART_AMOUNT | FLOAT | Payment amount |
| 6 | BKART_POSTDATE | DATE | Post date |
| 7 | BKART_CNTR | UBINARY | Line counter |
| 8 | BKART_ENTDATE | DATE | Entry date |
| 9 | BKART_TRXNLINK | FLOAT | Linked transaction number (chain) |
| 10 | BKART_INVC | FLOAT | Invoice number applied to |
| 11 | BKART_CHECK | FLOAT | Check number received |
| 12 | BKART_NOTE | STRING | Note flag ("Y" = detail in BKARTNOT) |

---

### BKARTNOT — AR Transaction Notes

File: `BKARTNOT.B` | Module: AR | Fields: 3

Detail note lines for BKART payment transactions. PK: `BKART_NOT_TRXN` + `BKART_NOT_CNTR`.

| # | Field | Meaning |
|---|-------|---------|
| 1 | BKART_NOT_TRXN | Transaction number (FK → BKART) |
| 2 | BKART_NOT_CNTR | Line counter |
| 3 | BKART_NOT_DESC | Note text (30 chars) |

---

### BKARTXN / BKARTXNB / BKARTXNS — AR Lot/Serial Shipment Transactions

Files: `BKARTXN.B`, `BKARTXNB.B`, `BKARTXNS.B` | Module: AR/IN | Fields: 14 each (identical)

Tracks lot numbers, serial numbers, and bin locations for items shipped on SO invoices. PK: `BKAR_TXN_SONUM` + `BKAR_TXN_CODE`. BKARTXN = base; BKARTXNB = batch-picking variant; BKARTXNS = serial-number variant (same schema, different lifecycle stage).

| # | Field | Type | Meaning |
|---|-------|------|---------|
| 1 | BKAR_TXN_SONUM | FLOAT | SO number — **PK component** |
| 2 | BKAR_TXN_CODE | STRING | Part code — **PK component** |
| 3 | BKAR_TXN_DESC | STRING | Part description |
| 4 | BKAR_TXN_QTY | FLOAT | Quantity shipped |
| 5 | BKAR_TXN_LOT | STRING | Lot number |
| 6 | BKAR_TXN_SERIAL | STRING | Serial number |
| 7 | BKAR_TXN_DATE | DATE | Ship date |
| 8 | BKAR_TXN_STOCK | STRING | Stock location code |
| 9 | BKAR_TXN_LINE | FLOAT | Invoice line number |
| 10 | BKAR_TXN_LOC | STRING | Location code |
| 11 | BKAR_TXN_TMPSO | STRING | Temp SO reference (40 chars) |
| 12 | BKAR_TXN_SRNUM | FLOAT | Service record number |
| 13 | BKAR_TXN_EXTRA | STRING | Extra 50 chars |
| 14 | BKAR_TXN_BIN | STRING | Bin location (15 chars) |

---

### BKAR* Description Tables (all 5-field BK_DESC_* pattern)

`BKARDESC`, `BKARDPST`, `BKARHDSC`, `BKARRDSC` — all identical 5-field BK_DESC_* pattern (same as BKAPDESC etc.):

| # | Field | Meaning |
|---|-------|---------|
| 1 | BK_DESC_CODE | Entity code (customer/invoice number) |
| 2 | BK_DESC_NUM | Record number |
| 3 | BK_DESC_LINE | Line counter |
| 4 | BK_DESC_NOTES | Note text (70 chars) |
| 5 | BK_DESC_DESC | Short description (25 chars) |

BKARDESC = AR description lines; BKARDPST = drop-ship description; BKARHDSC = history description; BKARRDSC = returns description.

---

**BKAR* Family Summary Table** (Pass 126 2026-06-19):

| Table | Fields | Role | Structural Mirror |
|-------|--------|------|------------------|
| BKARCUST | 106 | Customer master | — |
| BKARECST | 106 | "E" company customer master | BKARCUST (identical) |
| BKARSHIP | 106 | Ship-to address master | BKARCUST (identical) |
| BKARINV | 84 | AR invoice header | — |
| BKARHINV | 84 | AR invoice history | BKARINV (identical) |
| BKARRINV | 84 | AR returns invoice | BKARINV (identical) |
| BKARINVL | 28 | AR invoice lines | — |
| BKARHIVL | 28 | AR invoice history lines | BKARINVL (identical) |
| BKARRIVL | 28 | AR returns invoice lines | BKARINVL (identical) |
| BKARSIVL | 28 | AR ship-to invoice lines | BKARINVL (identical) |
| BKARINVI | 16 | AR invoice staging buffer | — |
| BKARINVT | 23 | AR open-item transaction ledger | — |
| BKAREIVT | 24 | AR extended invoice transaction | BKARINVT + BKAB_PERIOD + NORMP |
| BKARINVV | 77 | AR voucher (10-slot GL dist) | — |
| BKARHTAX | 5 | AR invoice history tax | — |
| BKARDEP | 6 | Customer deposit | — |
| BKART | 12 | AR payment transaction log | — |
| BKARTNOT | 3 | AR transaction notes | — |
| BKARTXN | 14 | AR lot/serial shipment tx | — |
| BKARTXNB | 14 | AR lot/serial tx (batch) | BKARTXN (identical) |
| BKARTXNS | 14 | AR lot/serial tx (serial) | BKARTXN (identical) |
| BKARCHKH/BKARCHKF | 12 | AP check history (BKAP_CHK_ prefix) | BKAPCHKH/BKAPCHKF |
| BKARDESC/BKARDPST/BKARHDSC/BKARRDSC | 5 | Description note lines | BK_DESC_* pattern |

---

*Document updated: 2026-06-19 (Pass 126)*
*Source: `samples/ddf/schema.md` + SRC analysis + DFM analysis*
*Confidence: 68/100 — Field names and types confirmed from DDF schema. Field meanings inferred from naming conventions and confirmed where SRC source code references the fields directly.*

---

---

## BKGL* Family — GL Satellite Tables

All confirmed from DDF — Pass 128 2026-06-19.

### Structural Overview

The BKGL* family (28 tables total) organizes into six functional clusters:

| Cluster | Tables | Schema | Purpose |
|---------|--------|--------|---------|
| COA mirrors | BKGLCOA / BKGLECOA / BKGLFCOA / BKGLCCOA | 65f / 65f / 65f / 62f | Per-company Chart of Accounts |
| Journal headers | BKGLGJRN / BKGLAGJR / BKGLRGJR / BKGLTGJR | 11f each (identical) | Journal entry records (live / archive / recurring / temp) |
| Journal lines | BKGLGJLN / BKGLAGJL / BKGLRGJL / BKGLTGJL | 9f each (identical) | Journal entry detail lines |
| Transactions | BKGLTRAN / BKGLATRN / BKGLHIST / BKGLETRN / BKGLTEMP / BKGLTMP / BKGLTMP2 / BKGLTMP3 | 16f each (identical) | GL audit-trail transactions (live / archive / history / E-co / work tables) |
| Check register | BKGLCHK / BKGLACHK / BKGLICC | 11f / 11f / 11f | Bank clearing checks (BKGL_CHK_* prefix) |
| Cross-reference | BKGLX / BKGLXH | 20f each (identical) | Inventory/WO/PO/SO → GL costing bridge |
| Statement design | BKGLFSTL / BKGLSTMT / BKGLDESC | 12f / 104f / 5f | Financial statement layout and notes |

---

### COA Mirror Architecture

BKGLCOA (main, already documented) is mirrored three times for multi-company deployments:

| Table | Fields | Prefix | Notes |
|-------|--------|--------|-------|
| BKGLCOA | 65 | `BKGL_` | Master COA |
| BKGLECOA | 65 | `BKGL_` | "E" company — identical schema, same prefix |
| BKGLFCOA | 65 | `BKGL_` | "F" company — identical schema, same prefix |
| BKGLCCOA | 62 | `BKGLC_` | "C" company — 3 fields fewer (no EXTRA, no 1YPAST_YE, no 2YPAST_YE) |

Note: BKGLECOA and BKGLFCOA share the same `BKGL_` field-name prefix as the master BKGLCOA, making them indistinguishable by field names alone — the table name (file) differentiates them.

---

### Journal Header Tables (11f each, identical schema)

All four tables share the BKGL_GJ_* prefix:

| # | Field | Type | Size | Meaning |
|---|-------|------|------|---------|
| 1 | BKGL_GJ_TRANSDT | DATE | 4 | Transaction date (PK part 1) |
| 2 | BKGL_GJ_TRANSNM | FLOAT | 8 | Transaction number (PK part 2) |
| 3 | BKGL_GJ_TYPE | STRING | 2 | Journal type (AR/AP/WO/GL etc.) |
| 4 | BKGL_GJ_TYPEN | UBINARY | 2 | Type number |
| 5 | BKGL_GJ_POSTED | STRING | 1 | Posted flag (Y/N) |
| 6 | BKGL_GJ_CVCODE | STRING | 10 | Customer/vendor code |
| 7 | BKGL_GJ_INVCHKN | FLOAT | 8 | Invoice or check number |
| 8 | BKGL_GJ_NUMLNES | UBINARY | 2 | Number of detail lines |
| 9 | BKGL_GJ_CHKACT | UBINARY | 2 | Check/bank account number |
| 10 | BKGL_GJ_JOB | STRING | 15 | Job/WO number |
| 11 | BKGL_GJ_EXTRA | STRING | 50 | Extra/notes |

BKGLGJRN = live; BKGLAGJR = archived; BKGLRGJR = recurring template; BKGLTGJR = temp during posting.

---

### Journal Line Tables (9f each, identical schema)

All four tables share the BKGL_GJL_* prefix:

| # | Field | Type | Size | Meaning |
|---|-------|------|------|---------|
| 1 | BKGL_GJL_TRANSN | FLOAT | 8 | Transaction number (FK → BKGLGJRN, PK part 1) |
| 2 | BKGL_GJL_ACCTNM | STRING | 10 | GL account number (FK → BKGLCOA) |
| 3 | BKGL_GJL_GLDPT | STRING | 4 | GL department |
| 4 | BKGL_GJL_DESC | STRING | 25 | Line description |
| 5 | BKGL_GJL_DC | STRING | 1 | Debit/credit flag |
| 6 | BKGL_GJL_AMOUNT | FLOAT | 8 | Line amount |
| 7 | BKGL_GJL_JOB | STRING | 15 | Job/WO number |
| 8 | BKGL_GJL_LINE | UBINARY | 2 | Line number (PK part 2) |
| 9 | BKGL_GJL_EXTRA | STRING | 50 | Extra/notes |

BKGLGJLN = live; BKGLAGJL = archived; BKGLRGJL = recurring template lines; BKGLTGJL = temp posting lines.

---

### Transaction Table Cluster (16f each, identical schema)

BKGLTRAN (already documented) plus seven mirrors — all use BKGL_TRN_* prefix, byte-for-byte identical. The same 16-field schema appears in:

| Table | Role |
|-------|------|
| BKGLTRAN | Live/active GL transactions |
| BKGLATRN | Archived GL transactions (year-end close) |
| BKGLHIST | GL transaction history (prior-period read-only) |
| BKGLETRN | "E" company GL transactions |
| BKGLTEMP | Temp table for GL processing |
| BKGLTMP | Work buffer 1 (used during period-end) |
| BKGLTMP2 | Work buffer 2 |
| BKGLTMP3 | Work buffer 3 |

---

### Check Register Tables (BKGLCHK / BKGLACHK)

Files: `BKGLCHK.B`, `BKGLACHK.B` | Fields: 11 each (identical) | Prefix: `BKAP_CHK_`

Despite residing in the GL namespace, these use the AP check prefix. BKGLCHK = current/uncleared checks; BKGLACHK = archived/cleared checks.

| # | Field | Type | Size | Meaning |
|---|-------|------|------|---------|
| 1 | BKAP_CHK_CHKACT | UBINARY | 2 | Bank account number (PK part 1) |
| 2 | BKAP_CHK_NUM | FLOAT | 8 | Check number (PK part 2) |
| 3 | BKAP_CHK_DATE | DATE | 4 | Check date |
| 4 | BKAP_CHK_TYPE | STRING | 1 | Check type (C=check, W=wire, etc.) |
| 5 | BKAP_CHK_NAME | STRING | 25 | Payee name |
| 6 | BKAP_CHK_AMT | FLOAT | 8 | Check amount |
| 7 | BKAP_CHK_FLAG | STRING | 1 | Status flag (cleared, void, etc.) |
| 8 | BKAP_CHK_EXTRA | STRING | 25 | Extra/notes |
| 9 | BKAP_CHK_DATER | DATE | 4 | Reconciliation/cleared date |
| 10 | BKAP_CHK_VEND | STRING | 10 | Vendor code (FK → BKAPVEND) |
| 11 | BKAP_CHK_CUST | STRING | 10 | Customer code (FK → BKARCUST) |

---

### BKGLICC — Inter-Company Check Clearing

File: `BKGLICC.B` | Module: GL | Fields: 11 | Prefix: `BKGL_CHK_`

Inter-company clearing check register. Same 11-field structure as BKGLCHK but uses `BKGL_CHK_` prefix (not `BKAP_CHK_`) and has a larger EXTRA field (100 bytes vs 25):

| # | Field | Type | Size | Difference from BKGLCHK |
|---|-------|------|------|------------------------|
| 1 | BKGL_CHK_CHKACT | UBINARY | 2 | — |
| 2 | BKGL_CHK_NUM | FLOAT | 8 | — |
| 3 | BKGL_CHK_DATE | DATE | 4 | — |
| 4 | BKGL_CHK_TYPE | STRING | 1 | — |
| 5 | BKGL_CHK_NAME | STRING | 25 | — |
| 6 | BKGL_CHK_AMT | FLOAT | 8 | — |
| 7 | BKGL_CHK_FLAG | STRING | 1 | — |
| 8 | BKGL_CHK_EXTRA | STRING | 100 | **100 bytes** (vs 25 in BKGLCHK) |
| 9 | BKGL_CHK_DATER | DATE | 4 | — |
| 10 | BKGL_CHK_VEND | STRING | 10 | — |
| 11 | BKGL_CHK_CUST | STRING | 10 | — |

---

### BKGLFSTL — Financial Statement Line Definition

File: `BKGLFSTL.B` | Module: GL | Fields: 12 | Prefix: `BKFS_`

Defines the lines of user-designed financial statements (Balance Sheet, P&L, etc.). Each row specifies one line in a report: the account range it covers, how to aggregate it, and where on the page to print.

| # | Field | Type | Size | Meaning |
|---|-------|------|------|---------|
| 1 | BKFS_NAME | STRING | 10 | Statement name (PK part 1) |
| 2 | BKFS_LINE_NUM | UBINARY | 2 | Line number (PK part 2) |
| 3 | BKFS_SGL_ACCT | STRING | 10 | Start GL account (range begin) |
| 4 | BKFS_EGL_ACCT | STRING | 10 | End GL account (range end) |
| 5 | BKFS_TOTAL_FLD | UBINARY | 2 | Total/subtotal field number |
| 6 | BKFS_PRT_LOC | UBINARY | 2 | Print location (column) |
| 7 | BKFS_PRT_DOL | STRING | 1 | Print dollar sign flag |
| 8 | BKFS_DESC | STRING | 25 | Line description label |
| 9 | BKFS_PRT_AMT | STRING | 1 | Print amount flag |
| 10 | BKFS_OP | STRING | 2 | Operator (add/subtract this line into total) |
| 11 | BKFS_CALC_BASE | UBINARY | 2 | Calculation base (which total to reference) |
| 12 | BKFS_NDC | STRING | 1 | Normal D/C polarity flag |

---

### BKGLSTMT — Financial Statement Layout Template

File: `BKGLSTMT.B` | Module: GL | Fields: 104 | Prefix: `BKGL_STB_` / `BKGL_STI_` / `BKGL_STC_`

Single-record configuration table that defines the column ranges and titles for the three standard GL financial statements. Organized into three sections:

- **STB** (Balance Sheet) — fields 1–34: main title, up to 4 account ranges (F/T = from/to) with 4 titles each, for assets/liabilities/other
- **STI** (Income Statement) — fields 35–71: main title, income/cost/expense/other sections each with account ranges and titles
- **STC** (Cash Flow Statement) — fields 72–104: main title, operating/investing/financing sections

This table holds the "column headers and account-grouping ranges" that frame each financial report. BKGLFSTL holds the individual line rows within those frames.

---

### BKGLX / BKGLXH — GL Cross-Reference (Inventory Costing Bridge)

Files: `BKGLX.B`, `BKGLXH.B` | Module: GL/IC/WO | Fields: 20 each (identical) | Prefix: `BKGLX_`

The GL cross-reference table links inventory/manufacturing transactions back to the GL posting. Unique among GL tables — it carries part numbers, quantities, WO references, PO numbers, and SO invoice numbers alongside GL amounts, enabling drilldown from a GL account balance to its originating transactions.

| # | Field | Type | Size | Meaning |
|---|-------|------|------|---------|
| 1 | BKGLX_POSTDATE | DATE | 4 | GL posting date |
| 2 | BKGLX_ARCHDATE | DATE | 4 | Archive date |
| 3 | BKGLX_ENTDATE | DATE | 4 | Entry/transaction date |
| 4 | BKGLX_PART | STRING | 15 | Item/part number (FK → BKICMSTR) |
| 5 | BKGLX_QUANTITY | FLOAT | 8 | Quantity transacted |
| 6 | BKGLX_AMOUNT | FLOAT | 8 | Dollar amount |
| 7 | BKGLX_TRXNTYPE | STRING | 1 | Transaction type code |
| 8 | BKGLX_JOURNAL | STRING | 2 | Source journal (AR/AP/WO/IC etc.) |
| 9 | BKGLX_WOPRE | FLOAT | 8 | Work order prefix number |
| 10 | BKGLX_WOSUF | UBINARY | 2 | Work order suffix |
| 11 | BKGLX_PONUM | FLOAT | 8 | PO number (FK → BKAPPO) |
| 12 | BKGLX_SOINVC | FLOAT | 8 | SO invoice number (FK → BKARINV) |
| 13 | BKGLX_POINVC | STRING | 10 | PO invoice number |
| 14 | BKGLX_DESC | STRING | 30 | Description |
| 15 | BKGLX_TRXN | FLOAT | 8 | Transaction sequence number |
| 16 | BKGLX_BATCH | FLOAT | 8 | Batch number |
| 17 | BKGLX_POST | STRING | 1 | Posted flag |
| 18 | BKGLX_COMPANY | STRING | 2 | Company code |
| 19 | BKGLX_ICLASS | STRING | 4 | Inventory class |
| 20 | BKGLX_CCLASS | STRING | 4 | Cost class |

BKGLX = current/active; BKGLXH = history (same schema).

---

### BKGLDESC — GL Description Notes

File: `BKGLDESC.B` | Module: GL | Fields: 5

Standard BK_DESC_* 5-field pattern (CODE/NUM/LINE/NOTES/DESC). GL-specific free-text note lines attached to GL accounts or transactions.

---

**BKGL* Family Summary Table** (Pass 128 2026-06-19):

| Table | Fields | Role | Mirror / Notes |
|-------|--------|------|----------------|
| BKGLCOA | 65 | Chart of Accounts (main) | — |
| BKGLECOA | 65 | COA "E" company | BKGLCOA (identical schema, same BKGL_ prefix) |
| BKGLFCOA | 65 | COA "F" company | BKGLCOA (identical schema, same BKGL_ prefix) |
| BKGLCCOA | 62 | COA "C" company | BKGLCOA minus EXTRA+YE fields; BKGLC_ prefix |
| BKGLGJRN | 11 | Journal headers (live) | — |
| BKGLAGJR | 11 | Journal headers (archive) | BKGLGJRN (identical) |
| BKGLRGJR | 11 | Journal headers (recurring) | BKGLGJRN (identical) |
| BKGLTGJR | 11 | Journal headers (temp) | BKGLGJRN (identical) |
| BKGLGJLN | 9 | Journal lines (live) | — |
| BKGLAGJL | 9 | Journal lines (archive) | BKGLGJLN (identical) |
| BKGLRGJL | 9 | Journal lines (recurring) | BKGLGJLN (identical) |
| BKGLTGJL | 9 | Journal lines (temp) | BKGLGJLN (identical) |
| BKGLTRAN | 16 | GL transactions (live) | — |
| BKGLATRN | 16 | GL transactions (archive) | BKGLTRAN (identical) |
| BKGLHIST | 16 | GL transactions (history) | BKGLTRAN (identical) |
| BKGLETRN | 16 | GL transactions ("E" company) | BKGLTRAN (identical) |
| BKGLTEMP | 16 | GL transactions (temp) | BKGLTRAN (identical) |
| BKGLTMP | 16 | GL transactions (work buffer 1) | BKGLTRAN (identical) |
| BKGLTMP2 | 16 | GL transactions (work buffer 2) | BKGLTRAN (identical) |
| BKGLTMP3 | 16 | GL transactions (work buffer 3) | BKGLTRAN (identical) |
| BKGLCHK | 11 | Check register (live) | BKAP_CHK_* prefix |
| BKGLACHK | 11 | Check register (archive) | BKGLCHK (identical) |
| BKGLICC | 11 | Inter-company check clearing | BKGL_CHK_* prefix; EXTRA=100 bytes |
| BKGLFSTL | 12 | Financial statement line defs | BKFS_* prefix |
| BKGLSTMT | 104 | Financial statement layout template | STB_/STI_/STC_* sections |
| BKGLDESC | 5 | GL description notes | BK_DESC_* pattern |
| BKGLX | 20 | GL cross-reference / costing bridge | BKGLX_* prefix; links IC/WO/PO/SO |
| BKGLXH | 20 | GL cross-reference history | BKGLX (identical) |

---

*Document updated: 2026-06-19 (Pass 128)*
*Source: `samples/ddf/schema.md`*
*Confidence: 82/100 — All 28 table schemas extracted from DDF; field meanings interpreted from naming conventions; journal type codes and BKGLSTMT section mapping not confirmed against live data.*

---

---

## BKBM* Family — Bill of Materials Satellite Tables

All confirmed from DDF — Pass 129 2026-06-19.

### Structural Overview

The BKBM* family (10 tables) revolves around one core BOM line schema shared by 5 tables, with 3 satellite annotation tables and 2 utility tables:

| Table | Fields | Role |
|-------|--------|------|
| BKBMMSTR | 26 | BOM master (main company) |
| BKBMAMTR | 26 | BOM master "A" company mirror |
| BKBMEMTR | 26 | BOM master "E" company mirror |
| BKBMAVAL | 26 | Alternate/validated BOM lines |
| BKBMSUMM | 26 | Rolled-up/exploded BOM summary (MRP/WO use) |
| BKBMREMK | 20 | BOM component remarks (main) |
| BKBMERMK | 20 | BOM component remarks "E" company mirror |
| BKBMNOTE | 16 | BOM assembly-level notes |
| BKBMDIM | 11 | BOM component cut dimensions (sheet/material nesting) |
| BKBMCNFG | 7 | BOM module configuration |

---

### Core BOM Line Schema (26f — shared by BKBMMSTR / BKBMAMTR / BKBMEMTR / BKBMAVAL / BKBMSUMM)

All five tables are byte-for-byte identical in schema. The 2-byte gap between PARENT (size 15, offset 0) and COMPONENT (offset 17) is a structural TAS Pro 7 record-layout pad — treat PARENT as a 17-byte slot.

| # | Field | Type | Size | Meaning |
|---|-------|------|------|---------|
| 1 | BKBM_PARENT | STRING | 15 | Parent item code (FK → BKICMSTR, PK part 1) |
| 2 | BKBM_COMPONENT | STRING | 15 | Component item code (FK → BKICMSTR, PK part 2) |
| 3 | BKBM_QTY_REQD | FLOAT | 8 | Quantity required per parent assembly (8 dec places) |
| 4 | BKBM_REFERENCE | STRING | 20 | Reference designator (PCB ref-des, drawing callout, etc.) |
| 5 | BKBM_PROD_TYPE | STRING | 1 | Component type flag (see item type codes) |
| 6 | BKBM_PROD_SCRAP | FLOAT | 8 | Scrap factor % (added to qty when exploded) |
| 7 | BKBM_PROD_OP | STRING | 3 | Routing operation code where this component is consumed |
| 8 | BKBM_PROD_OPYN_1 | STRING | 1 | Operation 1 include flag (Y/N) |
| 9 | BKBM_PROD_OPYN_2 | STRING | 1 | Operation 2 include flag |
| 10 | BKBM_PROD_OPYN_3 | STRING | 1 | Operation 3 include flag |
| 11 | BKBM_PROD_OPYN_4 | STRING | 1 | Operation 4 include flag |
| 12 | BKBM_PROD_OPYN_5 | STRING | 1 | Operation 5 include flag |
| 13 | BKBM_PROD_OPYN_6 | STRING | 1 | Operation 6 include flag |
| 14 | BKBM_PROD_PRICE | FLOAT | 8 | Component unit price (for cost roll-up override) |
| 15 | BKBM_PROD_RTNUM | UBINARY | 2 | Routing number reference |
| 16 | BKBM_PROD_DUPOP | STRING | 1 | Duplicate-operation flag |
| 17 | BKBM_PROD_OPDSC | STRING | 5 | Operation description short code |
| 18 | BKBM_PROD_VEND | STRING | 10 | Preferred vendor for this component (FK → BKAPVEND) |
| 19 | BKBM_DATE1 | DATE | 4 | Effective-from date |
| 20 | BKBM_DATE2 | DATE | 4 | Effective-to date (obsolete after this date) |
| 21 | BKBM_EXTRA | STRING | 50 | Extra/notes |
| 22 | BKBM_REV | STRING | 5 | BOM revision level |
| 23 | BKBM_P_TYPE | STRING | 10 | Parent item type classification |
| 24 | BKBM_C_TYPE | STRING | 10 | Component item type classification |
| 25 | BKBM_EST_LINE | FLOAT | 8 | Estimating line number (sequence for cost estimating) |
| 26 | BKBM_UID | STRING | 20 | User ID of last editor |

**Table roles:**
- **BKBMMSTR** — active BOM (main company); what WO explosion reads
- **BKBMAMTR** — "A" company BOM mirror for multi-company deployments
- **BKBMEMTR** — "E" company BOM mirror
- **BKBMAVAL** — alternate/validated BOM variant; used when a component substitution has been approved
- **BKBMSUMM** — single-level roll-up used by MRP and WO explosion; accumulates total qty across multi-level tree

---

### BKBMREMK / BKBMERMK — BOM Component Remarks (20f each, identical)

Per-component extended remarks. One row per component+line_number, supporting 15 × 64-character remark lines. PK = PARENT + LINE + COMP (3-key composite). BKBMERMK = "E" company mirror.

| # | Field | Type | Size | Meaning |
|---|-------|------|------|---------|
| 1 | BKBM_RM_PARENT | STRING | 15 | Parent item code (PK part 1) |
| 2 | BKBM_RM_LINE | UBINARY | 2 | Line number (PK part 2) |
| 3 | BKBM_RM_COMP | STRING | 15 | Component item code (PK part 3) |
| 4–18 | BKBM_RM_REMARK_1..15 | STRING | 64 each | 15 remark lines (total 960 bytes of text) |
| 19 | BKBM_RM_UID | STRING | 20 | User ID of last editor |
| 20 | BKBM_RM_EXTRA | STRING | 50 | Extra/notes |

---

### BKBMNOTE — BOM Assembly Notes (16f)

Assembly-level notes keyed by PARENT only (not per-component). Supports 15 × 64-character note lines per assembly item.

| # | Field | Type | Size | Meaning |
|---|-------|------|------|---------|
| 1 | BKBM_NT_PARENT | STRING | 15 | Parent item code (PK) |
| 2–16 | BKBM_NT_NOTE_1..15 | STRING | 64 each | 15 note lines (total 960 bytes) |

---

### BKBMDIM — BOM Component Cut Dimensions (11f)

Sheet/material nesting dimensions for components that come from sheet stock (metal, laminate, PCB substrate, etc.). Stores the X/Y cut dimensions, the machine/saw code, and the trim allowance and remnant return dimensions.

| # | Field | Type | Size | Meaning |
|---|-------|------|------|---------|
| 1 | BKBM_DIM_PARENT | STRING | 15 | Parent item code (PK part 1) |
| 2 | BKBM_DIM_LINE | UBINARY | 2 | Line number (PK part 2) |
| 3 | BKBM_DIM_COMP | STRING | 15 | Component item code (PK part 3) |
| 4 | BKBM_DIM_PART_X | FLOAT | 8 | Part dimension X (width/length, 4 dec) |
| 5 | BKBM_DIM_PART_Y | FLOAT | 8 | Part dimension Y (height/width, 4 dec) |
| 6 | BKBM_DIM_MACH | STRING | 4 | Machine/saw code for this cut |
| 7 | BKBM_DIM_TRIM_X | FLOAT | 8 | Trim allowance X (kerf + handling, 2 dec) |
| 8 | BKBM_DIM_TRIM_Y | FLOAT | 8 | Trim allowance Y |
| 9 | BKBM_DIM_REMN_X | FLOAT | 8 | Remnant returned X dimension (4 dec) |
| 10 | BKBM_DIM_REMN_Y | FLOAT | 8 | Remnant returned Y dimension |
| 11 | BKBM_DIM_EXTRA | STRING | 50 | Extra/notes |

---

### BKBMCNFG — BOM Configuration (7f)

Single-record table (keyed by NUM) holding BOM module-level defaults: which GL account to charge, whether to auto-post, whether to roll costs, whether to include labor in cost roll.

| # | Field | Type | Size | Meaning |
|---|-------|------|------|---------|
| 1 | BKBM_CNFG_NUM | FLOAT | 8 | Configuration record number (PK, typically 1) |
| 2 | BKBM_CNFG_GLACT | STRING | 10 | Default GL account for BOM postings |
| 3 | BKBM_CNFG_GLDPT | STRING | 4 | Default GL department |
| 4 | BKBM_CNFG_AUTO | STRING | 1 | Auto-post flag (Y/N) |
| 5 | BKBM_CNFG_POST | STRING | 1 | Post-to-GL flag |
| 6 | BKBM_CNFG_ROLL | STRING | 1 | Cost roll-up enable flag |
| 7 | BKBM_CNFG_LABOR | STRING | 1 | Include labor in cost roll flag |

---

**BKBM* Family Summary Table** (Pass 129 2026-06-19):

| Table | Fields | Role | Mirror |
|-------|--------|------|--------|
| BKBMMSTR | 26 | BOM component lines (main) | — |
| BKBMAMTR | 26 | BOM lines "A" company | BKBMMSTR (identical) |
| BKBMEMTR | 26 | BOM lines "E" company | BKBMMSTR (identical) |
| BKBMAVAL | 26 | Alternate/validated BOM lines | BKBMMSTR (identical schema, different lifecycle) |
| BKBMSUMM | 26 | Rolled-up BOM for MRP/WO explosion | BKBMMSTR (identical schema, summarized content) |
| BKBMREMK | 20 | Component remarks (main) | — |
| BKBMERMK | 20 | Component remarks "E" company | BKBMREMK (identical) |
| BKBMNOTE | 16 | Assembly-level notes | — |
| BKBMDIM | 11 | Sheet cut dimensions | — |
| BKBMCNFG | 7 | BOM module configuration | — |

---

*Document updated: 2026-06-19 (Pass 129)*
*Source: `samples/ddf/schema.md`*
*Confidence: 80/100 — All 10 table schemas extracted from DDF; core BOM line fields interpreted from names + cross-reference with BM form analysis; PROD_OPYN_1..6 semantics inferred (which routing op uses this component); DUPOP and CNFG flag values not confirmed against live data.*

---

---

## BKDC* Family — Data Collection Satellite Tables

All confirmed from DDF — Pass 130 2026-06-19.

### Structural Overview

The BKDC* family (7 tables) breaks into two clusters: the labor record lifecycle pipeline (5 identical-schema tables) and two configuration tables:

| Table | Fields | Role |
|-------|--------|------|
| BKDCCLAB | 50 | Scanned/unposted labor records (fresh from terminal) |
| BKDCLAB | 50 | Active/posted labor (DC-G approved) |
| BKDCPLAB | 50 | Pending batch-post labor |
| BKDCHLAB | 50 | Historical/archived labor |
| BKDCTLAB | 50 | Temp labor work file (processing buffer) |
| BKDCSHFT | 34 | Shift schedule (3-shift time boundaries) |
| BKDCCFG | 7 | DC module configuration |

---

### DC Labor Schema (50f — shared by BKDCCLAB / BKDCLAB / BKDCPLAB / BKDCHLAB / BKDCTLAB)

All five tables are byte-for-byte identical. PK = DATE + EMP + WOPRE + WOSUF + OPER (5-key composite). The `LAB_POSTED` flag determines which pipeline stage a record is in.

| # | Field | Type | Size | Meaning |
|---|-------|------|------|---------|
| 1 | LAB_DATE | DATE | 4 | Work date (PK part 1) |
| 2 | LAB_EMP | UBINARY | 2 | Employee number (PK part 2, FK → BKPRMSTR) |
| 3 | LAB_WOPRE | FLOAT | 8 | Work order prefix number (PK part 3) |
| 4 | LAB_WOSUF | UBINARY | 2 | Work order suffix (PK part 4) |
| 5 | LAB_OPER | UBINARY | 2 | Routing operation number (PK part 5) |
| 6 | LAB_POSTED | STRING | 1 | Posted flag (Y=posted to WORKORD, N=pending) |
| 7 | LAB_SHIFT | UBINARY | 2 | Shift number (1/2/3, FK → BKDCSHFT) |
| 8 | LAB_START | TIME | 4 | Shift start time |
| 9 | LAB_FINISH | TIME | 4 | Shift finish time |
| 10 | LAB_PARTS | FLOAT | 8 | Parts completed this transaction |
| 11 | LAB_SCRAPPED | FLOAT | 8 | Total parts scrapped |
| 12 | LAB_NOJOBS | UBINARY | 2 | Number of concurrent jobs/setups (for multi-WO setup) |
| 13 | LAB_RUNHRS | FLOAT | 8 | Run hours charged |
| 14 | LAB_SETUPHRS | FLOAT | 8 | Setup hours charged |
| 15 | LAB_REGOVER | STRING | 1 | Regular/overtime flag (R=regular, O=overtime) |
| 16 | LAB_EXTRA | STRING | 50 | Extra/notes |
| 17 | LAB_APPROVAL | STRING | 1 | Supervisor approval status flag |
| 18 | LAB_ADT_SUPER | STRING | 100 | Audit: supervisor name (for approval trail) |
| 19 | LAB_ADT_IN | STRING | 100 | Audit: time-in text |
| 20 | LAB_ADT_OUT | STRING | 100 | Audit: time-out text |
| 21 | LAB_ESSDATE | DATE | 4 | Early/scheduled start date |
| 22 | LAB_DATE1 | DATE | 4 | Generic date UDF 1 |
| 23 | LAB_DATE2 | DATE | 4 | Generic date UDF 2 |
| 24 | LAB_SCRAPCD_1 | STRING | 2 | Scrap reason code 1 |
| 25 | LAB_SCRAPCD_2 | STRING | 2 | Scrap reason code 2 |
| 26 | LAB_SCRAPCD_3 | STRING | 2 | Scrap reason code 3 |
| 27 | LAB_SCRAPCD_4 | STRING | 2 | Scrap reason code 4 |
| 28 | LAB_SCRAPCD_5 | STRING | 2 | Scrap reason code 5 |
| 29 | LAB_SCRAPQTY_1 | FLOAT | 8 | Qty scrapped against reason code 1 |
| 30 | LAB_SCRAPQTY_2 | FLOAT | 8 | Qty scrapped against reason code 2 |
| 31 | LAB_SCRAPQTY_3 | FLOAT | 8 | Qty scrapped against reason code 3 |
| 32 | LAB_SCRAPQTY_4 | FLOAT | 8 | Qty scrapped against reason code 4 |
| 33 | LAB_SCRAPQTY_5 | FLOAT | 8 | Qty scrapped against reason code 5 |
| 34 | LAB_JCNUM | STRING | 12 | Job Costing number (FK to JC module) |
| 35 | LAB_CYCLE_HR | UBINARY | 2 | Cycle time hours component |
| 36 | LAB_CYCLE_MIN | UBINARY | 2 | Cycle time minutes component |
| 37 | LAB_CYCLE_SEC | UBINARY | 2 | Cycle time seconds component |
| 38 | LAB_CYCLE_PARTS | FLOAT | 8 | Parts per cycle (1 dec) |
| 39 | LAB_CYCLE_NOTE | STRING | 255 | Cycle time note (AOI/SPC result text) |
| 40 | LAB_GEN_DATE_1 | DATE | 4 | Generic date UDF 3 |
| 41 | LAB_GEN_DATE_2 | DATE | 4 | Generic date UDF 4 |
| 42 | LAB_GEN_ALPHA_1 | STRING | 30 | Generic alpha UDF 1 |
| 43 | LAB_GEN_ALPHA_2 | STRING | 30 | Generic alpha UDF 2 |
| 44 | LAB_GEN_NUM_1 | FLOAT | 8 | Generic numeric UDF 1 |
| 45 | LAB_GEN_NUM_2 | FLOAT | 8 | Generic numeric UDF 2 |
| 46 | LAB_GEN_FLAG_1 | STRING | 1 | Generic flag UDF 1 |
| 47 | LAB_GEN_FLAG_2 | STRING | 1 | Generic flag UDF 2 |
| 48 | LAB_GEN_FLAG_3 | STRING | 1 | Generic flag UDF 3 |
| 49 | LAB_GEN_FLAG_4 | STRING | 1 | Generic flag UDF 4 |
| 50 | LAB_GEN_FLAG_5 | STRING | 1 | Generic flag UDF 5 |

**Pipeline flow:** Scanner → BKDCCLAB (raw) → DC-G review → LAB_APPROVAL=Y → DC-H post → BKDCLAB (active, LAB_POSTED=N) → batch post → BKDCPLAB (pending) → WORKORD cost update → BKDCHLAB (history). BKDCTLAB is the temp work file used during the DC-H batch posting pass.

---

### BKDCSHFT — Shift Schedule (34f)

Single-record table (no PK key field — entire table is one configuration record) defining the time boundaries for 3 shifts. Each shift has 10 TIME fields: buffer, start, 2 breaks, lunch, end, end-buffer.

| Fields | Type | Per Shift | Meaning |
|--------|------|-----------|---------|
| BKDC_SH_NAME1/2/3 | STRING(25) | one per shift | Shift name (Day / Swing / Night) |
| BKDC_SH_BUFFER_1/2/3 | TIME | one per shift | Pre-shift buffer window |
| BKDC_SH_START_1/2/3 | TIME | one per shift | Official shift start time |
| BKDC_SH_BRK1IN_1/2/3 | TIME | one per shift | Break 1 start |
| BKDC_SH_BRK1OUT_1/2/3 | TIME | one per shift | Break 1 end |
| BKDC_SH_LUNCHIN_1/2/3 | TIME | one per shift | Lunch start |
| BKDC_SH_LUNCHOT_1/2/3 | TIME | one per shift | Lunch end |
| BKDC_SH_BRK2IN_1/2/3 | TIME | one per shift | Break 2 start |
| BKDC_SH_BRK2OUT_1/2/3 | TIME | one per shift | Break 2 end |
| BKDC_SH_FIN_1/2/3 | TIME | one per shift | Official shift end time |
| BKDC_SH_FINBUF_1/2/3 | TIME | one per shift | Post-shift buffer window (holds scan clock open) |
| BKDC_SH_EXTRA | STRING(50) | one total | Extra/notes |

Layout: 3 names + 10 time fields × 3 shifts + 1 extra = 34 fields.

---

### BKDCCFG — DC Configuration (7f)

Single-record configuration table for DC module timeouts and file paths.

| # | Field | Type | Size | Meaning |
|---|-------|------|------|---------|
| 1 | BKDC_CFG_IDLEP | FLOAT | 8 | Idle timeout period (minutes before scanner auto-logs off) |
| 2 | BKDC_CFG_IDLES | UBINARY | 2 | Idle timeout seconds (fractional component) |
| 3 | BKDC_CFG_BANKP | FLOAT | 8 | Bank/screen timeout period |
| 4 | BKDC_CFG_BANKS | UBINARY | 2 | Bank timeout seconds |
| 5 | BKDC_CFG_IMPPTH | STRING | 60 | Import path (handheld sync / barcode scan file import) |
| 6 | BKDC_CFG_EXPPTH | STRING | 60 | Export path (data export to handheld) |
| 7 | BKDC_CFG_JOBTME | STRING | 60 | Job timer path |

---

**BKDC* Family Summary Table** (Pass 130 2026-06-19):

| Table | Fields | Role | Mirror |
|-------|--------|------|--------|
| BKDCCLAB | 50 | Raw scanned labor (unposted, from terminal) | — |
| BKDCLAB | 50 | Active posted labor | BKDCCLAB (identical) |
| BKDCPLAB | 50 | Pending batch-post labor | BKDCCLAB (identical) |
| BKDCHLAB | 50 | Historical/archived labor | BKDCCLAB (identical) |
| BKDCTLAB | 50 | Temp labor work file | BKDCCLAB (identical) |
| BKDCSHFT | 34 | Shift schedule (3 shifts × 10 time boundaries) | — |
| BKDCCFG | 7 | DC configuration (timeouts + paths) | — |

---

*Document updated: 2026-06-19 (Pass 130)*
*Source: `samples/ddf/schema.md` + T7DCA SRC analysis*
*Confidence: 82/100 — All schemas confirmed from DDF; pipeline stage roles confirmed from BKDCA.SRC analysis (Pass 118); LAB_REGOVER/APPROVAL flag values inferred from names.*

---

---

## BKPI* Family — Physical Inventory Satellite Tables

All confirmed from DDF — Pass 130 2026-06-19.

### Structural Overview

The BKPI* family (7 tables) supports the freeze → count → compare → post cycle:

| Table | Fields | Role |
|-------|--------|------|
| BKPIMSTR | 3 | PI session header (YEAR+QTR key) |
| BKPIFROZ | 19 | Frozen inventory snapshot per item/location |
| BKPIPHYS | 14 | Physical count tags (actual counted quantities) |
| BKPILOT | 10 | Frozen lot inventory snapshot |
| BKPILCNT | 10 | Lot count entries (actual lot counts) |
| BKPISER | 10 | Frozen serial inventory snapshot |
| BKPISCNT | 10 | Serial count entries (actual serial counts) |

---

### BKPIMSTR — PI Session Header (3f)

One record per physical inventory session. PK = YEAR + QTR.

| # | Field | Type | Size | Meaning |
|---|-------|------|------|---------|
| 1 | BKPI_MSTR_YEAR | STRING | 4 | Fiscal year (4-digit string, PK part 1) |
| 2 | BKPI_MSTR_QTR | STRING | 2 | Quarter (PK part 2) |
| 3 | BKPI_MSTR_DESC | STRING | 30 | Session description |

---

### BKPIFROZ — Frozen Inventory Snapshot (19f)

Created by PI-A (freeze). One record per item/location at the moment of freeze. This is the baseline the count is compared against.

| # | Field | Type | Size | Meaning |
|---|-------|------|------|---------|
| 1 | BKPH_INFO_UOH | FLOAT | 8 | Units on hand at freeze (2 dec) |
| 2 | BKPH_INFO_YEAR | STRING | 4 | PI session year (PK part 1) |
| 3 | BKPH_INFO_QTR | STRING | 2 | PI session quarter (PK part 2) |
| 4 | BKPH_INFO_LOC | STRING | 10 | Location code (PK part 3) |
| 5 | BKPH_INFO_PROD | STRING | 15 | Item/part code (PK part 4) |
| 6 | BKPH_INFO_COST | FLOAT | 8 | Unit cost at freeze (6 dec) |
| 7 | BKPH_INFO_GLPST | STRING | 1 | GL posted flag (Y=variance posted to GL) |
| 8 | BKPH_INFO_INPST | STRING | 1 | Inventory posted flag (Y=BKICMSTR.UOH updated) |
| 9 | BKPH_INFO_FDATE | DATE | 4 | Freeze date |
| 10 | BKPH_INFO_LOT | STRING | 1 | Has-lot flag (Y=lot tracking for this item) |
| 11 | BKPH_INFO_SER | STRING | 1 | Has-serial flag (Y=serial tracking for this item) |
| 12 | BKPH_INFO_PCOST | FLOAT | 8 | Prior period unit cost (6 dec) |
| 13 | BKPH_INFO_PADJ | FLOAT | 8 | Prior period cost adjustment |
| 14 | BKPH_INFO_ACCTA | STRING | 10 | GL variance account (adjustment debit) |
| 15 | BKPH_INFO_DEPTA | STRING | 4 | GL variance department |
| 16 | BKPH_INFO_ACCTC | STRING | 10 | GL clearing account (offset credit) |
| 17 | BKPH_INFO_DEPTC | STRING | 4 | GL clearing department |
| 18 | BKPH_INFO_PUNIT | FLOAT | 8 | Prior period unit cost (alternate slot) |
| 19 | BKPH_INFO_TAGS | UBINARY | 2 | Number of count tags issued for this item |

---

### BKPIPHYS — Physical Count Tags (14f)

Created by PI-C (enter tag counts). One record per physical count tag. A tag is a physical paper form tied to a specific location-item that a counter fills in.

| # | Field | Type | Size | Meaning |
|---|-------|------|------|---------|
| 1 | BKPH_TAGNUM | FLOAT | 8 | Tag number (PK — sequential from BKPIMSTR.BKPI_MSTR_TAGS) |
| 2 | BKPH_ACTQTY | FLOAT | 8 | Actual quantity counted (2 dec) |
| 3 | BKPH_EMPNUM | UBINARY | 2 | Counter employee number |
| 4 | BKPH_EMPNAME | STRING | 15 | Counter employee name |
| 5 | BKPH_COMMENT | STRING | 30 | Tag comment |
| 6 | BKPH_COUNTDATE | DATE | 4 | Date counted |
| 7 | BKPH_YEAR | STRING | 4 | PI session year |
| 8 | BKPH_QTR | STRING | 2 | PI session quarter |
| 9 | BKPH_LOC | STRING | 10 | Location code (FK → BKICLOC) |
| 10 | BKPH_CODE | STRING | 15 | Item/part code (FK → BKICMSTR) |
| 11 | BKPH_FDATE | DATE | 4 | Freeze date (from BKPIFROZ, for linking) |
| 12 | BKPH_LOT | STRING | 15 | Lot number (if lot-tracked) |
| 13 | BKPH_SERIAL | STRING | 25 | Serial number (if serial-tracked) |
| 14 | BKPH_BIN | STRING | 10 | Bin location (if bin-tracking enabled) |

**Variance calculation:** PI-G compares BKPIPHYS.BKPH_ACTQTY (counted) to BKPIFROZ.BKPH_INFO_UOH (frozen). Delta is posted as INVTXN adjustment, BKICMSTR.UOH updated, BKPIFROZ.BKPH_INFO_GLPST+INPST set to Y.

---

### Lot Count Tables (10f each, identical schema)

BKPILOT (frozen lot snapshot) and BKPILCNT (actual lot count) share the same 10-field schema with BKPI_LOT_* prefix:

| # | Field | Type | Size | Meaning |
|---|-------|------|------|---------|
| 1 | BKPI_LOT_YEAR | STRING | 4 | PI session year (PK part 1) |
| 2 | BKPI_LOT_QTR | STRING | 2 | PI session quarter (PK part 2) |
| 3 | BKPI_LOT_CODE | STRING | 15 | Item/part code (PK part 3) |
| 4 | BKPI_LOT_LOT | STRING | 15 | Lot number (PK part 4) |
| 5 | BKPI_LOT_QTY | FLOAT | 8 | Quantity (frozen or counted, 2 dec) |
| 6 | BKPI_LOT_TAG | FLOAT | 8 | Associated count tag number |
| 7 | BKPI_LOT_LOC | STRING | 10 | Location code |
| 8 | BKPI_LOT_SERQTY | FLOAT | 8 | Serial quantity within this lot |
| 9 | BKPI_LOT_PSTD | STRING | 1 | Posted flag |
| 10 | BKPI_LOT_BIN | STRING | 15 | Bin location |

BKPILOT = frozen quantity per lot at freeze time; BKPILCNT = actual quantity counted per lot.

---

### Serial Count Tables (10f each, identical schema)

BKPISER (frozen serial snapshot) and BKPISCNT (actual serial count) share the same 10-field schema with BKPI_SER_* prefix:

| # | Field | Type | Size | Meaning |
|---|-------|------|------|---------|
| 1 | BKPI_SER_YEAR | STRING | 4 | PI session year (PK part 1) |
| 2 | BKPI_SER_QTR | STRING | 2 | PI session quarter (PK part 2) |
| 3 | BKPI_SER_CODE | STRING | 15 | Item/part code (PK part 3) |
| 4 | BKPI_SER_SERIAL | STRING | 25 | Serial number (PK part 4) |
| 5 | BKPI_SER_QTY | FLOAT | 8 | Quantity (1 for most serials, 2 dec) |
| 6 | BKPI_SER_TAG | FLOAT | 8 | Associated count tag number |
| 7 | BKPI_SER_LOC | STRING | 10 | Location code |
| 8 | BKPI_SER_LOTNO | STRING | 15 | Lot number (for lot-and-serial tracked items) |
| 9 | BKPI_SER_PSTD | STRING | 1 | Posted flag |
| 10 | BKPI_SER_BIN | STRING | 15 | Bin location |

BKPISER = frozen serial list at freeze time; BKPISCNT = actuals entered during count.

---

**BKPI* Family Summary Table** (Pass 130 2026-06-19):

| Table | Fields | Prefix | Role | Mirror |
|-------|--------|--------|------|--------|
| BKPIMSTR | 3 | BKPI_MSTR_* | PI session header | — |
| BKPIFROZ | 19 | BKPH_INFO_* | Frozen item inventory snapshot | — |
| BKPIPHYS | 14 | BKPH_* | Physical count tag entries | — |
| BKPILOT | 10 | BKPI_LOT_* | Frozen lot snapshot | — |
| BKPILCNT | 10 | BKPI_LOT_* | Lot count entries | BKPILOT (identical) |
| BKPISER | 10 | BKPI_SER_* | Frozen serial snapshot | — |
| BKPISCNT | 10 | BKPI_SER_* | Serial count entries | BKPISER (identical) |

---

*Document updated: 2026-06-19 (Pass 130)*
*Source: `samples/ddf/schema.md`*
*Confidence: 80/100 — All schemas confirmed from DDF; variance-posting logic confirmed from PI module workflow docs (Pass 111a); BKPH_INFO_TAGS count role inferred from PI-A program analysis.*

---

---

## MT* Family — Multi-Class Catalog Tables

All confirmed from DDF — Pass 131 2026-06-19.

### Structural Overview

The MT* family (6 DDF tables) is the multi-class / multi-company catalog layer that sits above the single-company BK* operational tables. MTICMSTR is the primary catalog; the other three IC tables are mirrors or templates; MTEXCHG holds multi-currency rates; MTMRP is the MRP planning scratch table.

| Table | Fields | Role |
|-------|--------|------|
| MTICMSTR | 108 | Multi-class item master — primary catalog (CLASS+CODE PK) |
| MTICAMTR | 108 | Multi-company archive mirror (identical schema) |
| MTICEMTR | 108 | Edit/temp mirror for multi-class IC changes (identical schema) |
| MTINVDEF | 108 | Item creation defaults template (identical schema, CLASS="DFLT" role) |
| MTEXCHG | 7 | Multi-currency exchange rate table |
| MTMRP | 13 | MRP planning work table (temp scratch, cleared between runs) |

---

### MTICMSTR Cluster — Multi-Class Item Master (108f, 4 identical tables)

MTICMSTR, MTICAMTR, MTICEMTR, and MTINVDEF all share the exact same 108-field schema (confirmed — MTICAMTR and MTINVDEF are byte-for-byte identical to MTICMSTR via DDF offset/type check). PK = CLASS + CODE.

**MTICMSTR vs BKICMSTR distinction:** BKICMSTR is single-company operational (64f, CODE PK — no CLASS, no weight/draw/vendor arrays). MTICMSTR is the multi-class catalog (108f, CLASS+CODE PK, adds weight/lead/drawing, 10 vendors, 15 received costs, 12 spec lines, 5 substitutes, MRP/QC flags). BKICMSTR.UOH etc. are transactional; MTICMSTR.STDC/RCOST_* etc. are catalog-level.

Full 108-field table (condensed — arrays collapsed):

| # | Field | Type | Size | Meaning |
|---|-------|------|------|---------|
| 1 | MTIC_PROD_CLASS | STRING | 4 | Item class (PK part 1 — groups items by type/family) |
| 2 | MTIC_PROD_CODE | STRING | 15 | Item/part code (PK part 2) |
| 3 | MTIC_PROD_DESC | STRING | 30 | Description |
| 4 | MTIC_PROD_SUM | STRING | 3 | Sales unit of measure (stocking UOM for sales) |
| 5 | MTIC_PROD_PUM | STRING | 3 | Purchase unit of measure |
| 6 | MTIC_PROD_PCONV | FLOAT | 8 | Purchase-to-stock unit conversion factor (5 dec) |
| 7 | MTIC_PROD_CYCLE | STRING | 1 | Cycle count flag |
| 8 | MTIC_PROD_ABC | STRING | 1 | ABC classification (A/B/C) |
| 9 | MTIC_PROD_LOT | STRING | 1 | Lot tracking flag (Y=lot tracked) |
| 10 | MTIC_PROD_SER | STRING | 1 | Serial tracking flag (Y=serial tracked) |
| 11 | MTIC_PROD_ACTIV | STRING | 1 | Active flag (Y=active) |
| 12 | MTIC_PROD_STDPK | FLOAT | 8 | Standard pack quantity |
| 13 | MTIC_PROD_WT | FLOAT | 8 | Unit weight (6 dec) |
| 14 | MTIC_PROD_CUBFT | FLOAT | 8 | Cubic feet per unit (4 dec) |
| 15 | MTIC_PROD_LEAD | UBINARY | 2 | Lead time (days) |
| 16 | MTIC_PROD_LOC | STRING | 10 | Default warehouse location |
| 17 | MTIC_PROD_DRAW | STRING | 15 | Drawing number |
| 18 | MTIC_PROD_REV | STRING | 5 | Drawing revision |
| 19 | MTIC_PROD_COST | STRING | 1 | Cost method override (A=avg, S=standard, F=FIFO, L=LIFO) |
| 20 | MTIC_PROD_ESTCD | STRING | 1 | Estimating code (used by ES module) |
| 21 | MTIC_PROD_MRP | STRING | 1 | MRP planning flag (Y=include in MRP) |
| 22 | MTIC_PROD_GLINV | STRING | 10 | GL inventory account |
| 23 | MTIC_PROD_INVDP | STRING | 4 | GL inventory department |
| 24 | MTIC_PROD_GLWIP | STRING | 10 | GL WIP account |
| 25 | MTIC_PROD_WIPDP | STRING | 4 | GL WIP department |
| 26–37 | MTIC_PROD_SPECS_1..12 | STRING(30) | — | 12 specification lines (30 chars each) |
| 38 | MTIC_PROD_UOWO | FLOAT | 8 | Units on WO (2 dec) — WO quantity committed |
| 39 | MTIC_PROD_UOA | FLOAT | 8 | Units on allocation (2 dec) |
| 40 | MTIC_PROD_COMM | FLOAT | 8 | Commission percentage (4 dec) |
| 41 | MTIC_PROD_STDC | FLOAT | 8 | Standard cost (6 dec) |
| 42 | MTIC_PROD_TYPE | STRING | 1 | Item type (R/F/A/M/N/L/B/T/K/O) |
| 43–47 | MTIC_PROD_SUBST_1..5 | STRING(25) | — | 5 substitute part codes |
| 48 | MTIC_PROD_FRT | FLOAT | 8 | Freight cost per unit (6 dec) |
| 49 | MTIC_PROD_MRPSW | STRING | 1 | MRP on/off switch (per BKMRPSW) |
| 50 | MTIC_PROD_UIWIP | FLOAT | 8 | Units in WIP (2 dec) |
| 51 | MTIC_PROD_AVAIL | FLOAT | 8 | Available quantity (2 dec, computed) |
| 52 | MTIC_PROD_OPTPR | UBINARY | 2 | Options/pricing level |
| 53 | MTIC_PROD_CUST | STRING | 10 | Customer code (for customer-specific items) |
| 54 | MTIC_PROD_CUSNM | STRING | 30 | Customer name |
| 55 | MTIC_PROD_CLDES | STRING | 30 | Class description |
| 56–65 | MTIC_PROD_VEND_1..10 | STRING(10) | — | 10 approved vendor codes |
| 66–75 | MTIC_PROD_VNAM_1..10 | STRING(30) | — | 10 vendor names |
| 76–84 | MTIC_PROD_VPC_1..9 | STRING(20) | — | 9 vendor part codes |
| 85–99 | MTIC_PROD_RCOST_1..15 | FLOAT(8,6dec) | — | 15 received cost slots (purchase cost history) |
| 100 | MTIC_PROD_OPT | STRING | 1 | Options flag |
| 101 | MTIC_PROD_LOTSZ | FLOAT | 8 | Lot size (reorder quantity) |
| 102 | MTIC_PROD_OPTCS | STRING | 1 | Options cost flag |
| 103 | MTIC_PROD_OPTCD | STRING | 5 | Options code |
| 104 | MTIC_PROD_UIQC | FLOAT | 8 | Units in QC inspection (2 dec) |
| 105 | MTIC_PROD_EXPBF | UBINARY | 2 | Explode backflush level |
| 106 | MTIC_PROD_DELBF | UBINARY | 2 | Delete backflush level |
| 107 | MTIC_PROD_CUM | STRING | 3 | Cumulative UOM code |
| 108 | MTIC_PROD_LONGP | STRING | 25 | Long part number / customer part number |

**Mirror roles:**
- MTICMSTR — primary multi-class catalog (read by most modules)
- MTICAMTR — multi-company archive (populated when a company closes or archives items)
- MTICEMTR — edit temp (used during IC-A save to stage changes before commit)
- MTINVDEF — item defaults template (used when creating a new MTICMSTR record to supply default CLASS/values; "DFLT" class records are the factory defaults)

---

### MTEXCHG — Multi-Currency Exchange Rates (7f)

One record per currency / date combination.

| # | Field | Type | Size | Meaning |
|---|-------|------|------|---------|
| 1 | EXCHG_QUOTE | FLOAT | 8 | Exchange rate quoted (base-to-foreign multiplier) |
| 2 | EXCHG_AMT | FLOAT | 8 | Exchange amount (6 dec) |
| 3 | EXCHG_DESC | STRING | 30 | Currency description (e.g., "Canadian Dollar") |
| 4 | EXCHG_COST | FLOAT | 8 | Cost rate (buying rate, 6 dec) |
| 5 | EXCHG_EXTRA | STRING | 50 | Extra/notes |
| 6 | EXCHG_CODE | STRING | 15 | Currency code (ISO-3 or internal; PK part 1) |
| 7 | EXCHG_LINE | FLOAT | 8 | Line/sequence number (PK part 2 — allows multiple rates per currency) |

BKSO/BKAR/BKAP invoice tables have a CURRENCY(3) field; the runtime multiplies EXCHG_QUOTE to convert amounts. EXCHG_LINE allows date-effective rates (each rate change is a new record).

---

### MTMRP — MRP Planning Work Table (13f)

Scratch table; cleared and rebuilt each time MRP runs (MR-A). One record per planning event per part. Confirmed from BKMRF.SRC analysis (Pass 119) — field 13 (LOC) was not in the original 12-field count but IS in the DDF.

| # | Field | Type | Size | Meaning |
|---|-------|------|------|---------|
| 1 | MTMRP_PARTNO | STRING | 15 | Part code (PK part 1) |
| 2 | MTMRP_DATE | DATE | 4 | Demand/supply date (PK part 2) |
| 3 | MTMRP_QTY | FLOAT | 8 | Net quantity required (2 dec; negative=supply) |
| 4 | MTMRP_ONHAND | FLOAT | 8 | On-hand at this date (running projected balance) |
| 5 | MTMRP_PEGTO | STRING | 10 | Peg-to reference (parent WO/SO that drives this demand) |
| 6 | MTMRP_ORDER | STRING | 10 | Planned order reference number |
| 7 | MTMRP_STARTDT | DATE | 4 | Planned order start date |
| 8 | MTMRP_ACTION | STRING | 10 | MRP action code (ORDER/RESCHEDULE/CANCEL/RELEASE/etc.) |
| 9 | MTMRP_PG_SDATE | DATE | 4 | Pegged demand start date |
| 10 | MTMRP_PG_FDATE | DATE | 4 | Pegged demand finish date |
| 11 | MTMRP_PG_QTY | FLOAT | 8 | Pegged demand quantity (2 dec) |
| 12 | MTMRP_EXTRA | STRING | 50 | Extra/notes |
| 13 | MTMRP_LOC | STRING | 10 | Location code (for multi-location MRP) |

**Correction from prior analysis:** BKMRF.SRC analysis (Pass 119) confirmed 12 fields by name inspection. The DDF shows 13 fields — MTMRP_LOC is the 13th, added to support multi-location MRP. The BKMRF source likely uses `MTMRP_LOC` but was not explicitly called out in the Pass 119 name list.

---

**MT\* Family Summary Table** (Pass 131 2026-06-19):

| Table | Fields | Role | Mirror |
|-------|--------|------|--------|
| MTICMSTR | 108 | Multi-class item catalog (primary) | — |
| MTICAMTR | 108 | Multi-company archive | MTICMSTR (identical) |
| MTICEMTR | 108 | Edit/temp staging | MTICMSTR (identical) |
| MTINVDEF | 108 | Item creation defaults template | MTICMSTR (identical schema) |
| MTEXCHG | 7 | Multi-currency exchange rates | — |
| MTMRP | 13 | MRP planning scratch table | — |

---

*Document updated: 2026-06-19 (Pass 131)*
*Source: `samples/ddf/schema.md` (lines 24661–25142)*
*Confidence: 82/100 — All schemas confirmed from DDF; MTEXCHG field semantics inferred from names + multi-currency context; MTINVDEF role as defaults template inferred from name; MTMRP LOC field confirmed in DDF but not yet seen in BKMRF.SRC.*

---

---

## BKSY* Family — System Configuration and Security Satellite Tables

All confirmed from DDF — Pass 132 2026-06-19.

### Structural Overview

The BKSY* family (8 tables) is the system-manager cluster: global configuration, per-user security permissions, printer setup, and module-state counters. BKSYMSTR is the primary multi-field config table; BKSYLOG is the per-user module permission matrix (the most functionally important table here).

| Table | Fields | Role |
|-------|--------|------|
| BKSYMSTR | 286 | System configuration master (already documented — C:85) |
| BKSYLOG | 215 | Per-user module permission matrix |
| BKSYPRTR | 11 | Printer configuration records |
| BKSYAP | 11 | AP module working-state counters |
| BKSYAR | 2 | AR module working-state counters |
| BKSYCFG | 4 | Module on/off configuration flags |
| BKSYHELP | 1 | Help file path |
| BKSYUSER | 5 | Legacy user credential record |

Also documented here: **BKUMSRTY** (23f) — security level template table, closely related to BKSYLOG.

---

### BKSYLOG — Per-User Module Permission Matrix (215f)

The most important BKSY* table. One record per user. PK = CHR + CODE. Stores the full per-user module permission state: which modules the user can access (YN flags) and which specific operations within each module (OK_N flags, 20 slots per module).

Structure: user credentials (4f) + 9 module blocks × 21f each (1 module-YN + 20 per-op flags) + OKLM + 2 custom module blocks.

| Fields | Type | Size | Meaning |
|--------|------|------|---------|
| BKSY_LOGON_CHR | STRING | 1 | Record type (PK part 1 — 'Y'=active user, etc.) |
| BKSY_LOGON_CODE | STRING | 15 | User code (PK part 2, FK → AHSYLOG.WHO) |
| BKSY_LOGON_PSWD | STRING | 10 | Password (encrypted) |
| BKSY_LOGON_SCTY | STRING | 2 | Security level code (FK → BKUMSRTY.SCRTY_LEVEL) |
| BKSY_LOGON_GLYN | STRING | 1 | GL module access Y/N |
| BKSY_LOGON_OKGL_1..20 | STRING(1) × 20 | — | GL per-operation grants (20 ops) |
| BKSY_LOGON_ARYN | STRING | 1 | AR module access Y/N |
| BKSY_LOGON_OKAR_1..20 | STRING(1) × 20 | — | AR per-operation grants (20 ops) |
| BKSY_LOGON_SOYN | STRING | 1 | SO module access Y/N |
| BKSY_LOGON_OKSO_1..20 | STRING(1) × 20 | — | SO per-operation grants (20 ops) |
| BKSY_LOGON_APYN | STRING | 1 | AP module access Y/N |
| BKSY_LOGON_OKAP_1..20 | STRING(1) × 20 | — | AP per-operation grants (20 ops) |
| BKSY_LOGON_POYN | STRING | 1 | PO module access Y/N |
| BKSY_LOGON_OKPO_1..20 | STRING(1) × 20 | — | PO per-operation grants (20 ops) |
| BKSY_LOGON_ICYN | STRING | 1 | IC/Inventory module access Y/N |
| BKSY_LOGON_OKIC_1..20 | STRING(1) × 20 | — | IC per-operation grants (20 ops) |
| BKSY_LOGON_PRYN | STRING | 1 | PR/Payroll module access Y/N |
| BKSY_LOGON_OKPR_1..20 | STRING(1) × 20 | — | PR per-operation grants (20 ops) |
| BKSY_LOGON_SYYN | STRING | 1 | SY/System module access Y/N |
| BKSY_LOGON_OKSY_1..20 | STRING(1) × 20 | — | SY per-operation grants (20 ops) |
| BKSY_LOGON_OKLM | STRING | 1 | Lock manager access Y/N |
| BKSY_LOGON_O1YN | STRING | 1 | "Other module 1" access Y/N |
| BKSY_LOGON_OTH1_1..20 | STRING(1) × 20 | — | Other-1 per-operation grants (20 ops, 1 char each) |
| BKSY_LOGON_O2YN | STRING | 1 | "Other module 2" access Y/N |
| BKSY_LOGON_OTH2_1..20 | STRING(2) × 20 | — | Other-2 per-operation grants (20 ops, 2 chars each) |

**Security model:** BKUMSRTY provides the role template (SCRTY_LEVEL + menu → 20 item flags). When a user is created, their BKUMSRTY template is copied into BKSYLOG. Each login checks BKSYLOG to determine per-operation access. BKSLEVEL (422f matrix) is the older generation; BKSYLOG is the active runtime permission store.

---

### BKUMSRTY — Security Level Template (23f)

One record per security level × menu group combination. Defines which operations are permitted for a given role.

| # | Field | Type | Size | Meaning |
|---|-------|------|------|---------|
| 1 | SCRTY_LEVEL | STRING | 2 | Security level code (PK part 1, FK → BKSY_LOGON_SCTY) |
| 2 | SCRTY_MENU | UBINARY | 2 | Menu number (PK part 2) |
| 3 | SCRTY_GROUP | STRING | 1 | Menu group code |
| 4–23 | SCRTY_ITEM_1..20 | STRING(1) × 20 | — | Per-operation permit flags for this level+menu |

When a user logs in with SCTY="10", the runtime finds all BKUMSRTY records for SCRTY_LEVEL="10" and uses them as the initial grant set.

---

### BKSYPRTR — Printer Configuration (11f)

One record per configured printer. PK = BKSY_PRTR_NAME.

| # | Field | Type | Size | Meaning |
|---|-------|------|------|---------|
| 1 | BKSY_PRTR_NAME | STRING | 30 | Printer name (PK) |
| 2 | BKSY_PRTR_EXEC | STRING | 8 | Print executable/command code |
| 3 | BKSY_PRTR_TAS | STRING | 1 | TAS-managed printer flag |
| 4 | BKSY_PRTR_LPTNM | UBINARY | 1 | LPT port number |
| 5 | BKSY_PRTR_TYPE | STRING | 8 | Printer type code |
| 6 | BKSY_PRTR_PWDT | UBINARY | 2 | Page width |
| 7 | BKSY_PRTR_PMAX | UBINARY | 2 | Max pages |
| 8 | BKSY_PRTR_PPLNE | UBINARY | 2 | Lines per page |
| 9 | BKSY_PRTR_LASER | STRING | 1 | Laser printer flag (Y=laser, N=dot-matrix) |
| 10 | BKSY_PRTR_POST | STRING | 8 | PostScript mode |
| 11 | BKSY_PRTR_PRUN | STRING | 1 | Print run flag |

---

### BKSYAP — AP Module Working State (11f)

Single-record state table for AP module working counters and defaults. Read/written by PO receipt programs.

| # | Field | Type | Size | Meaning |
|---|-------|------|------|---------|
| 1 | BKSY_AP_RECVNUM | FLOAT | 8 | Receipt counter (next receipt number) |
| 2 | BKSY_AP_REOPEN | STRING | 1 | Reopen PO flag |
| 3 | BKSY_AP_RQSCRAP | STRING | 1 | Require scrap reason on short receive |
| 4 | BKSY_AP_RQREWRK | STRING | 1 | Require rework reason |
| 5 | BKSY_AP_RECVFLG | STRING | 1 | Receipt flag (processing state) |
| 6 | BKSY_AP_PONUM | FLOAT | 8 | Current PO number being received |
| 7 | BKSY_AP_QCRECV | FLOAT | 8 | QC receipt counter |
| 8 | BKSY_AP_RFQNUM | FLOAT | 8 | RFQ counter |
| 9 | BKSY_AP_VPRICE | UBINARY | 2 | Vendor price verification mode |
| 10 | BKSY_AP_PERCOVR | FLOAT | 8 | Price-over-tolerance percentage (3 dec) |
| 11 | BKSY_AP_CONVDTE | DATE | 4 | Conversion date (multi-currency rate date) |

---

### BKSYAR — AR Module Working State (2f)

Minimal state table for AR working counters.

| # | Field | Type | Size | Meaning |
|---|-------|------|------|---------|
| 1 | BKSY_AR_TRXN | FLOAT | 8 | AR transaction counter (next transaction number) |
| 2 | BKSY_AR_DEPNO | FLOAT | 8 | Deposit number counter (next deposit number) |

---

### BKSYCFG — Module On/Off Configuration (4f)

Single-record configuration controlling which functional areas are enabled.

| # | Field | Type | Size | Meaning |
|---|-------|------|------|---------|
| 1 | BKSY_CFG_ACCTG | STRING | 1 | Accounting module enabled (Y/N) |
| 2 | BKSY_CFG_SALES | STRING | 1 | Sales module enabled (Y/N) |
| 3 | BKSY_CFG_LITEWO | STRING | 1 | Lite work order mode (Y=simplified WO without full routing) |
| 4 | BKSY_CFG_ADVWO | STRING | 1 | Advanced work order mode (Y=full routing + scheduling) |

---

### BKSYHELP — Help Path (1f)

Single-record, single-field configuration.

| # | Field | Type | Size | Meaning |
|---|-------|------|------|---------|
| 1 | BKSY_HELP_PATH | STRING | 70 | Path to EvoHELP.CHM file |

---

### BKSYUSER — Legacy User Credential Record (5f)

Older-generation user record. Contains user code, password, security level, and default company — predates BKSYLOG's per-module expansion. Still read by legacy code.

| # | Field | Type | Size | Meaning |
|---|-------|------|------|---------|
| 1 | BKSY_USER_CHR | STRING | 1 | Record type (PK part 1) |
| 2 | BKSY_USER_CODE | STRING | 15 | User code (PK part 2) |
| 3 | BKSY_USER_PSWD | STRING | 10 | Password (encrypted) |
| 4 | BKSY_USER_SCTY | STRING | 2 | Security level code |
| 5 | BKSY_USER_COMP | STRING | 2 | Default company code |

**Relationship to BKSYLOG:** BKSYUSER = early precursor (5 fields). BKSYLOG = full expansion (215 fields). Both use the same CHR+CODE PK pattern.

---

**BKSY* Family Summary Table** (Pass 132 2026-06-19):

| Table | Fields | Role |
|-------|--------|------|
| BKSYMSTR | 286 | System config master (documented Pass 121) |
| BKSYLOG | 215 | Per-user module permission matrix (CHR+CODE PK) |
| BKUMSRTY | 23 | Security level template (role → operation grants) |
| BKSYPRTR | 11 | Printer configuration records |
| BKSYAP | 11 | AP module working state + receipt counters |
| BKSYAR | 2 | AR module working state (transaction + deposit counters) |
| BKSYCFG | 4 | Module on/off flags (ACCTG/SALES/LITEWO/ADVWO) |
| BKSYHELP | 1 | Help file path |
| BKSYUSER | 5 | Legacy user credential record (precedes BKSYLOG) |

---

*Document updated: 2026-06-19 (Pass 132)*
*Source: `samples/ddf/schema.md` (lines 10032–10633)*
*Confidence: 82/100 — All schemas confirmed from DDF; BKSYLOG security model interpretation (BKUMSRTY templates → BKSYLOG per-user grants) inferred from field names and security architecture; individual OK_N slot assignments (which GL operation maps to OKGL_1, etc.) unknown without RWN analysis.*
