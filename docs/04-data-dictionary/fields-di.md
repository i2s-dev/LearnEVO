# DI — Distribution Import: Field Reference

Status: verified-schema + completed field meanings (Pass 574j, 2026-07-06).

Source: `Evo-DBA_File_Fields 052421.xlsx`, sheet "Fields". Excel descriptions present for
most non-blank fields; remaining meanings name-inferred from their counterpart live tables.

The DI module provides import/staging functionality — these are all temp files used to
import data from external systems into EvoERP. Each temp table mirrors a corresponding
live table (BKAPEIVT→AP open items, BKAPEVND→vendor master, BKARECST→customer master, etc.).
BKGLECOA uses 14 period slots: periods 1-12 = Jan-Dec, 13 = year-end adjustment, 14 = audit.

---

## BKAPEIVT
**TEMP FILE FOR IMPORT OPEN AP** — staging table for AP open invoice import

Fields: 19 | Key: BKAP_INVT_CODE + BKAP_INVT_NUM

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAP_INVT_AMT | NUMERIC | 8 | 2 | Amount |
| 2 | BKAP_INVT_AMTRM | NUMERIC | 8 | 2 | Amount Remaining |
| 3 | BKAP_INVT_CHKAC | INTEGER | 2 | — | Checking account number (bank account FK) |
| 4 | BKAP_INVT_CHKNO | NUMERIC | 8 | — | Check number (if paid by check) |
| 5 | BKAP_INVT_CODE | STRING | 10 | — | Vendor Code |
| 6 | BKAP_INVT_DATE | DATE | 4 | — | Transaction Date |
| 7 | BKAP_INVT_DEPNO | NUMERIC | 8 | — | Deposit number |
| 8 | BKAP_INVT_DESC | STRING | 25 | — | Transaction Description |
| 9 | BKAP_INVT_EXTRA | STRING | 50 | — | Extra |
| 10 | BKAP_INVT_FRT | NUMERIC | 8 | 2 | Freight amount on this invoice |
| 11 | BKAP_INVT_GLDPT | STRING | 4 | — | GL Department |
| 12 | BKAP_INVT_MCCOD | STRING | 3 | — | Currency Code |
| 13 | BKAP_INVT_MCRAT | NUMERIC | 8 | 6 | Currency Rate |
| 14 | BKAP_INVT_NUM | STRING | 10 | — | Invoice/Voucher Reference No. |
| 15 | BKAP_INVT_PDATE | DATE | 4 | — | Post Date |
| 16 | BKAP_INVT_SDATE | DATE | 4 | — | Start Date |
| 17 | BKAP_INVT_TAX | NUMERIC | 8 | 2 | Tax amount on this invoice |
| 18 | BKAP_INVT_TERMN | INTEGER | 2 | — | Terms Number |
| 19 | BKAP_INVT_TYPE | STRING | 1 | — | transaction Type (IPCM) |

## BKAPEVND
**TEMP FILE FOR IMPORT VENDOR** — staging table for vendor master import

Fields: 72 | Key: BKAP_VENDCODE

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAP_ADD1_1 | STRING | 30 | — | Vendor address line 1 — main address |
| 2 | BKAP_ADD1_2 | STRING | 30 | — | Vendor address line 1 — remit-to address |
| 3 | BKAP_ADD2_1 | STRING | 30 | — | Vendor address line 2 — main address |
| 4 | BKAP_ADD2_2 | STRING | 30 | — | Vendor address line 2 — remit-to address |
| 5 | BKAP_ADD3 | STRING | 30 | — | Address line 3 |
| 6 | BKAP_ALPHA1 | STRING | 25 | — | User-defined alphanumeric field 1 |
| 7 | BKAP_ALPHA2 | STRING | 25 | — | User-defined alphanumeric field 2 |
| 8 | BKAP_CITY_1 | STRING | 26 | — | Vendor city — main address |
| 9 | BKAP_CITY_2 | STRING | 26 | — | Vendor city — remit-to address |
| 10 | BKAP_CLASS | STRING | 4 | — | Vendor Class - user defined |
| 11 | BKAP_CONTACT_1 | STRING | 30 | — | Contact name 1 |
| 12 | BKAP_CONTACT_2 | STRING | 30 | — | Contact name 2 |
| 13 | BKAP_CONTACT_3 | STRING | 30 | — | Contact name 3 |
| 14 | BKAP_CONTACT_4 | STRING | 30 | — | Contact name 4 |
| 15 | BKAP_COUNTRY_1 | STRING | 30 | — | Country — main address |
| 16 | BKAP_COUNTRY_2 | STRING | 30 | — | Country — remit-to address |
| 17 | BKAP_CREDLIM | NUMERIC | 8 | 2 | Credit limit (AP purchasing limit with this vendor) |
| 18 | BKAP_CUST_CODE | STRING | 15 | — | Customer cross-reference code (AR customer code for this vendor) |
| 19 | BKAP_DATE1 | DATE | 4 | — | User-defined date 1 |
| 20 | BKAP_DATE2 | DATE | 4 | — | User-defined date 2 |
| 21 | BKAP_DESC | STRING | 25 | — | Description |
| 22 | BKAP_EMAIL_1 | STRING | 128 | — | Email address 1 |
| 23 | BKAP_EMAIL_2 | STRING | 128 | — | Email address 2 |
| 24 | BKAP_EMAIL_3 | STRING | 128 | — | Email address 3 |
| 25 | BKAP_EMAIL_4 | STRING | 128 | — | Email address 4 |
| 26 | BKAP_EMAIL_5 | STRING | 128 | — | Email address 5 |
| 27 | BKAP_EXTRA | STRING | 150 | — | Extra line |
| 28 | BKAP_FOB_POINT | STRING | 20 | — | FOB Ship Point |
| 29 | BKAP_FTERMS_NUM | INTEGER | 2 | — | Freight Terms Number |
| 30 | BKAP_GL_ACCT | STRING | 10 | — | Default GL Account |
| 31 | BKAP_GL_DPT | STRING | 4 | — | Default GL Department |
| 32 | BKAP_HIST_YN | STRING | 1 | — | Keep history Y/N |
| 33 | BKAP_IS_DCODE | STRING | 3 | — | Duty Code |
| 34 | BKAP_IS_MCCODE | STRING | 3 | — | Currency Code |
| 35 | BKAP_IS_TAXGRP | STRING | 10 | — | Tax Group Code |
| 36 | BKAP_IS_TAXIN | STRING | 1 | — | Tax In Y.N |
| 37 | BKAP_LASTPMT | DATE | 4 | — | Last Payment Date |
| 38 | BKAP_LASTPURCH | DATE | 4 | — | Last Purchase Date |
| 39 | BKAP_NEW_VEND | STRING | 1 | — | New Vendor Y/N |
| 40 | BKAP_NOTES_1 | STRING | 60 | — | Vendor notes line 1 |
| 41 | BKAP_NOTES_10 | STRING | 60 | — | Vendor notes line 10 |
| 42 | BKAP_NOTES_2 | STRING | 60 | — | Vendor notes line 2 |
| 43 | BKAP_NOTES_3 | STRING | 60 | — | Vendor notes line 3 |
| 44 | BKAP_NOTES_4 | STRING | 60 | — | Vendor notes line 4 |
| 45 | BKAP_NOTES_5 | STRING | 60 | — | Vendor notes line 5 |
| 46 | BKAP_NOTES_6 | STRING | 60 | — | Vendor notes line 6 |
| 47 | BKAP_NOTES_7 | STRING | 60 | — | Vendor notes line 7 |
| 48 | BKAP_NOTES_8 | STRING | 60 | — | Vendor notes line 8 |
| 49 | BKAP_NOTES_9 | STRING | 60 | — | Vendor notes line 9 |
| 50 | BKAP_OUT_CREDIT | NUMERIC | 8 | 2 | Outstanding Credits |
| 51 | BKAP_OUTINV | NUMERIC | 8 | 2 | Number of Outstanding Invoices |
| 52 | BKAP_PURCH_LYR | NUMERIC | 8 | 2 | Purchases Last Year |
| 53 | BKAP_PURCH_MTD | NUMERIC | 8 | 2 | Purchases Month-to-Date |
| 54 | BKAP_PURCH_VAR | NUMERIC | 8 | 4 | Variance Percent- Last Year to YTD |
| 55 | BKAP_PURCH_YTD | NUMERIC | 8 | 2 | Purchases Year-to-Date |
| 56 | BKAP_REM_STATE | STRING | 2 | — | Bill To State |
| 57 | BKAP_REM_ZIP | STRING | 10 | — | Bill To Zip Code |
| 58 | BKAP_REQQC | STRING | 1 | — | Required QC certificate flag (Y/N) |
| 59 | BKAP_SHIP_VIA | STRING | 15 | — | Ship Via Carrier |
| 60 | BKAP_SORT | STRING | 6 | — | Sort Field |
| 61 | BKAP_START_DATE | DATE | 4 | — | Vendor Start Date |
| 62 | BKAP_STATE | STRING | 2 | — | State |
| 63 | BKAP_TAX_ID | STRING | 20 | — | Federal Tax ID Number |
| 64 | BKAP_TELEPHONE_1 | STRING | 25 | — | Telephone number 1 |
| 65 | BKAP_TELEPHONE_2 | STRING | 25 | — | Telephone number 2 |
| 66 | BKAP_TELEPHONE_3 | STRING | 25 | — | Telephone number 3 |
| 67 | BKAP_TELEPHONE_4 | STRING | 25 | — | Telephone number 4 |
| 68 | BKAP_TELEPHONE_5 | STRING | 25 | — | Telephone number 5 |
| 69 | BKAP_TERMS_NUM | INTEGER | 2 | — | Terms Number |
| 70 | BKAP_VENDCODE | STRING | 10 | — | Vendor Code |
| 71 | BKAP_VENDNAME | STRING | 30 | — | Vendor Name |
| 72 | BKAP_ZIP | STRING | 10 | — | Zip Code |

## BKARECST
**TEMP FILE FOR IMPORT CUSTOMER** — staging table for customer master import

Fields: 106 | Key: BKAR_CUSTCODE

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAR_ADD1 | STRING | 30 | — | Address Line 1 |
| 2 | BKAR_ADD2_1 | STRING | 30 | — | Address line 2 — part 1 |
| 3 | BKAR_ADD2_2 | STRING | 30 | — | Address line 2 — part 2 |
| 4 | BKAR_CARRIER | STRING | 15 | — | Carrier |
| 5 | BKAR_CHG_INTRST | STRING | 1 | — | Charge Interst Y/N |
| 6 | BKAR_CITY | STRING | 26 | — | City |
| 7 | BKAR_CLASS | STRING | 4 | — | Customer Class |
| 8 | BKAR_COGS_LYR | NUMERIC | 8 | 2 | COGS Last Year |
| 9 | BKAR_COGS_MTD | NUMERIC | 8 | 2 | COGS Month To Date |
| 10 | BKAR_COGS_PVAR | NUMERIC | 8 | 4 | COGS Percent Variance |
| 11 | BKAR_COGS_YTD | NUMERIC | 8 | 2 | COGS Year To Date |
| 12 | BKAR_COMM_1 | NUMERIC | 8 | 4 | Commission rate — salesperson 1 |
| 13 | BKAR_COMM_2 | NUMERIC | 8 | 4 | Commission rate — salesperson 2 |
| 14 | BKAR_CONTACT_1 | STRING | 30 | — | Contact name 1 |
| 15 | BKAR_CONTACT_2 | STRING | 30 | — | Contact name 2 |
| 16 | BKAR_CONTACT_3 | STRING | 30 | — | Contact name 3 |
| 17 | BKAR_CONTACT_4 | STRING | 30 | — | Contact name 4 |
| 18 | BKAR_CONTACT_5 | STRING | 30 | — | Contact name 5 |
| 19 | BKAR_COOP_AMT | NUMERIC | 8 | 2 | COOP Amount |
| 20 | BKAR_COOP_RATE | NUMERIC | 8 | 4 | COOP Rate |
| 21 | BKAR_COUNTRY | STRING | 30 | — | Country |
| 22 | BKAR_CREDIT_HLD | STRING | 1 | — | Credit Hold |
| 23 | BKAR_CREDITLMT | NUMERIC | 8 | 2 | Credit Limit |
| 24 | BKAR_CUST_YEAR | STRING | 12 | — | Customer fiscal year (12-char period designation) |
| 25 | BKAR_CUSTCODE | STRING | 10 | — | Customer Code |
| 26 | BKAR_CUSTNAME | STRING | 30 | — | Name |
| 27 | BKAR_DAYS_TOPAY | NUMERIC | 8 | — | Days To Pay |
| 28 | BKAR_DISC_CODE | STRING | 10 | — | Discount Code |
| 29 | BKAR_EMAIL_1 | STRING | 128 | — | Email address 1 |
| 30 | BKAR_EMAIL_2 | STRING | 128 | — | Email address 2 |
| 31 | BKAR_EMAIL_3 | STRING | 128 | — | Email address 3 |
| 32 | BKAR_EMAIL_4 | STRING | 128 | — | Email address 4 |
| 33 | BKAR_EMAIL_5 | STRING | 128 | — | Email address 5 |
| 34 | BKAR_EXTRA | STRING | 30 | — | Extra |
| 35 | BKAR_FAX_PHONE | STRING | 25 | — | Fax  Number |
| 36 | BKAR_FOB | STRING | 15 | — | Ship FOB |
| 37 | BKAR_FOLUPDTE | DATE | 4 | — | Follow-Up Date |
| 38 | BKAR_FORECAST | STRING | 12 | — | Forecast |
| 39 | BKAR_GLACCT | STRING | 10 | — | GL Account |
| 40 | BKAR_GLDPT | STRING | 4 | — | GL Department |
| 41 | BKAR_GROSS_LYR | NUMERIC | 8 | 2 | Gross Last Year |
| 42 | BKAR_GROSS_MTD | NUMERIC | 8 | 2 | Gross Month To Date |
| 43 | BKAR_GROSS_PVAR | NUMERIC | 8 | 4 | Gross Percent Variance |
| 44 | BKAR_GROSS_YTD | NUMERIC | 8 | 2 | Gross Year To Date |
| 45 | BKAR_HIST_YN | STRING | 1 | — | History Y/N |
| 46 | BKAR_IS_MCCODE | STRING | 3 | — | Currency |
| 47 | BKAR_IS_REP | STRING | 5 | — | IS extended rep number/code |
| 48 | BKAR_IS_TAXGRP | STRING | 10 | — | Tax Group |
| 49 | BKAR_IS_TAXIN | STRING | 1 | — | Excise Tax-In |
| 50 | BKAR_LASTPMT | DATE | 4 | — | Last Payment Date |
| 51 | BKAR_LASTSALE | DATE | 4 | — | Last Sale Date |
| 52 | BKAR_LEAD_SRC | STRING | 5 | — | Lead Source |
| 53 | BKAR_LEAD_SRC2 | STRING | 5 | — | Secondary lead source |
| 54 | BKAR_MAIL_LIST | STRING | 1 | — | Mail List Y/N |
| 55 | BKAR_NET_LYR | NUMERIC | 8 | 2 | Net Profit Last Year |
| 56 | BKAR_NET_MTD | NUMERIC | 8 | 2 | Net Profit Month To Date |
| 57 | BKAR_NET_PVAR | NUMERIC | 8 | 4 | Net Profit Percent Variance |
| 58 | BKAR_NET_YTD | NUMERIC | 8 | 2 | Net Profit Year To Date |
| 59 | BKAR_NEW_CUST | STRING | 1 | — | New Customer Y/N |
| 60 | BKAR_NOTES_1 | STRING | 80 | — | Customer notes line 1 |
| 61 | BKAR_NOTES_10 | STRING | 80 | — | Customer notes line 10 |
| 62 | BKAR_NOTES_2 | STRING | 80 | — | Customer notes line 2 |
| 63 | BKAR_NOTES_3 | STRING | 80 | — | Customer notes line 3 |
| 64 | BKAR_NOTES_4 | STRING | 80 | — | Customer notes line 4 |
| 65 | BKAR_NOTES_5 | STRING | 80 | — | Customer notes line 5 |
| 66 | BKAR_NOTES_6 | STRING | 80 | — | Customer notes line 6 |
| 67 | BKAR_NOTES_7 | STRING | 80 | — | Customer notes line 7 |
| 68 | BKAR_NOTES_8 | STRING | 80 | — | Customer notes line 8 |
| 69 | BKAR_NOTES_9 | STRING | 80 | — | Customer notes line 9 |
| 70 | BKAR_NUM_INVCS | NUMERIC | 8 | — | Number Invoices |
| 71 | BKAR_OUT_CREDIT_1 | NUMERIC | 8 | 2 | Outstanding credits — category 1 |
| 72 | BKAR_OUT_CREDIT_2 | NUMERIC | 8 | 2 | Outstanding credits — category 2 |
| 73 | BKAR_OUTINV | NUMERIC | 8 | 2 | Outstanding Invoices |
| 74 | BKAR_PNET_LYR | NUMERIC | 8 | 4 | Percent Profit Last Year |
| 75 | BKAR_PNET_MTD | NUMERIC | 8 | 4 | Percent Profit Month To Date |
| 76 | BKAR_PNET_PVAR | NUMERIC | 8 | 4 | Percent Profit Percent Variance |
| 77 | BKAR_PNET_YTD | NUMERIC | 8 | 4 | Percent Profit Year To Date |
| 78 | BKAR_PRICE_MAT | INTEGER | 2 | — | Price Code |
| 79 | BKAR_PURCH_AGMT | STRING | 1 | — | Purchasing Agent |
| 80 | BKAR_QC_INFO | STRING | 30 | — | QC Data |
| 81 | BKAR_RECV_HOURS | STRING | 30 | — | Receiving Hours |
| 82 | BKAR_REMAINCRD | NUMERIC | 8 | 2 | Credit Remaining |
| 83 | BKAR_REQD_CERTS | STRING | 10 | — | Certs |
| 84 | BKAR_RESALE_NO | STRING | 15 | — | Resale Number |
| 85 | BKAR_SHIPTO | STRING | 10 | — | Ship To Code |
| 86 | BKAR_SHIPVIA | STRING | 15 | — | Ship Via |
| 87 | BKAR_SHP_TOLRNC | STRING | 10 | — | Shipping tolerance (over/under ship %) |
| 88 | BKAR_SHP_WINDOW | STRING | 30 | — | Shipping Window |
| 89 | BKAR_SIC_CODE | STRING | 7 | — | SIC Code |
| 90 | BKAR_SLSP_NUM_1 | INTEGER | 2 | — | Salesperson number 1 (FK → BKPRSALE) |
| 91 | BKAR_SLSP_NUM_2 | INTEGER | 2 | — | Salesperson number 2 |
| 92 | BKAR_SORT | STRING | 6 | — | Sort Field |
| 93 | BKAR_START_DATE | DATE | 4 | — | Start Date |
| 94 | BKAR_STATE | STRING | 2 | — | State |
| 95 | BKAR_STATEMENT | STRING | 1 | — | Statement Y/N |
| 96 | BKAR_TAX_LOCAL | STRING | 2 | — | Tax Local |
| 97 | BKAR_TAX_STATE | STRING | 2 | — | Tax State |
| 98 | BKAR_TAX_YN | STRING | 1 | — | Tax Y/N |
| 99 | BKAR_TELEPHONE_1 | STRING | 25 | — | Telephone number 1 |
| 100 | BKAR_TELEPHONE_2 | STRING | 25 | — | Telephone number 2 |
| 101 | BKAR_TELEPHONE_3 | STRING | 25 | — | Telephone number 3 |
| 102 | BKAR_TELEPHONE_4 | STRING | 25 | — | Telephone number 4 |
| 103 | BKAR_TELEPHONE_5 | STRING | 25 | — | Telephone number 5 |
| 104 | BKAR_TERMS_NUM | INTEGER | 2 | — | Terms Number |
| 105 | BKAR_TERRITORY | STRING | 4 | — | Sales Territory |
| 106 | BKAR_ZIP | STRING | 10 | — | ZIP Code |

## BKAREIVT
**TEMP FILE FOR IMPORT OPEN AR** — staging table for AR open invoice import

Fields: 23 | Key: BKAR_INVT_CODE + BKAR_INVT_NUM

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAR_INVT_AMT | NUMERIC | 8 | 2 | Amount |
| 2 | BKAR_INVT_AMTRM | NUMERIC | 8 | 2 | Amount Remaining |
| 3 | BKAR_INVT_CHKAC | INTEGER | 2 | — | Checking Account |
| 4 | BKAR_INVT_CHKNO | NUMERIC | 8 | — | Check Number |
| 5 | BKAR_INVT_CLOSD | DATE | 4 | — | Close date (when invoice was closed/paid in full) |
| 6 | BKAR_INVT_CODE | STRING | 10 | — | Customer Code |
| 7 | BKAR_INVT_DATE | DATE | 4 | — | Transaction Date |
| 8 | BKAR_INVT_DEPNO | NUMERIC | 8 | — | Deposit number |
| 9 | BKAR_INVT_DEPST | STRING | 1 | — | Deposit status flag (D=deposited, P=pending) |
| 10 | BKAR_INVT_DESC | STRING | 25 | — | Description |
| 11 | BKAR_INVT_EXTRA | STRING | 50 | — | Extra |
| 12 | BKAR_INVT_GLDPT | STRING | 4 | — | GL Department |
| 13 | BKAR_INVT_MCCOD | STRING | 3 | — | Multi-currency code |
| 14 | BKAR_INVT_MCRAT | NUMERIC | 8 | 6 | Multi-currency exchange rate |
| 15 | BKAR_INVT_NORMP | STRING | 1 | — | Normal payment flag (Y=standard, C=credit) |
| 16 | BKAR_INVT_NUM | NUMERIC | 8 | — | Invoice Number |
| 17 | BKAR_INVT_OPEND | DATE | 4 | — | Open date (when invoice was first entered) |
| 18 | BKAR_INVT_PDATE | DATE | 4 | — | Post date |
| 19 | BKAR_INVT_SLSP | INTEGER | 2 | — | Salesperson1 |
| 20 | BKAR_INVT_SLSP2 | INTEGER | 2 | — | Salesperson 2 |
| 21 | BKAR_INVT_TERMN | INTEGER | 2 | — | Terms Number |
| 22 | BKAR_INVT_TRXN | NUMERIC | 8 | — | Transaction number (sequence within batch) |
| 23 | BKAR_INVT_TYPE | STRING | 1 | — | Transaction Type |

## BKBMEMTR
**TEMP FILE FOR IMPORT BOM** — staging table for BOM import

Fields: 27 | Key: BKBM_PARENT + BKBM_COMPONENT

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKBM_C_TYPE | STRING | 10 | — | Component type code |
| 2 | BKBM_COMPONENT | STRING | 15 | — | Component Part Code |
| 3 | BKBM_DATE1 | DATE | 4 | — | User-defined date 1 (effectivity from date) |
| 4 | BKBM_DATE2 | DATE | 4 | — | User-defined date 2 (effectivity to date) |
| 5 | BKBM_EST_LINE | NUMERIC | 8 | — | Estimate line number (cost estimating cross-ref) |
| 6 | BKBM_EXTRA | STRING | 50 | — | Extra |
| 7 | BKBM_P_TYPE | STRING | 10 | — | Parent item type code |
| 8 | BKBM_PARENT | STRING | 15 | — | Parent Part Code |
| 9 | BKBM_PROD_DUPOP | STRING | 1 | — | Duplicate Option blank / 1 / 2 |
| 10 | BKBM_PROD_LINE^ | INTEGER | 2 | — | BOM line number (computed/linked) |
| 11 | BKBM_PROD_OP | STRING | 3 | — | Option ( If  in second position) |
| 12 | BKBM_PROD_OPDSC | STRING | 5 | — | Option description code |
| 13 | BKBM_PROD_OPYN_1 | STRING | 1 | — | Option YN flag 1 |
| 14 | BKBM_PROD_OPYN_2 | STRING | 1 | — | Option YN flag 2 |
| 15 | BKBM_PROD_OPYN_3 | STRING | 1 | — | Option YN flag 3 |
| 16 | BKBM_PROD_OPYN_4 | STRING | 1 | — | Option YN flag 4 |
| 17 | BKBM_PROD_OPYN_5 | STRING | 1 | — | Option YN flag 5 |
| 18 | BKBM_PROD_OPYN_6 | STRING | 1 | — | Option YN flag 6 |
| 19 | BKBM_PROD_PRICE | NUMERIC | 8 | 4 | Option Pricing |
| 20 | BKBM_PROD_RTNUM | INTEGER | 2 | — | Routing  Sequence Number |
| 21 | BKBM_PROD_SCRAP | NUMERIC | 8 | 2 | Scrap Allowance Percent |
| 22 | BKBM_PROD_TYPE | STRING | 1 | — | Part Type |
| 23 | BKBM_PROD_VEND | STRING | 10 | — | Vendor Code |
| 24 | BKBM_QTY_REQD | NUMERIC | 8 | 8 | Quantity Required |
| 25 | BKBM_REFERENCE | STRING | 20 | — | Reference |
| 26 | BKBM_REV | STRING | 5 | — | Revision (not used) |
| 27 | BKBM_UID | STRING | 20 | — | Unique ID (import batch line identifier) |

## BKBMERMK
**TEMP FILE FOR IMPORT BOM REMARKS** — staging table for BOM remark lines

Fields: 20 | Key: BKBM_RM_PARENT + BKBM_RM_COMP + BKBM_RM_LINE

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKBM_RM_COMP | STRING | 15 | — | Component Part Code |
| 2 | BKBM_RM_EXTRA | STRING | 50 | — | Extra data |
| 3 | BKBM_RM_LINE | INTEGER | 2 | — | Line Number |
| 4 | BKBM_RM_PARENT | STRING | 15 | — | Parent Part Code |
| 5 | BKBM_RM_REMARK_1 | STRING | 64 | — | BOM remark line 1 |
| 6 | BKBM_RM_REMARK_10 | STRING | 64 | — | BOM remark line 10 |
| 7 | BKBM_RM_REMARK_11 | STRING | 64 | — | BOM remark line 11 |
| 8 | BKBM_RM_REMARK_12 | STRING | 64 | — | BOM remark line 12 |
| 9 | BKBM_RM_REMARK_13 | STRING | 64 | — | BOM remark line 13 |
| 10 | BKBM_RM_REMARK_14 | STRING | 64 | — | BOM remark line 14 |
| 11 | BKBM_RM_REMARK_15 | STRING | 64 | — | BOM remark line 15 |
| 12 | BKBM_RM_REMARK_2 | STRING | 64 | — | BOM remark line 2 |
| 13 | BKBM_RM_REMARK_3 | STRING | 64 | — | BOM remark line 3 |
| 14 | BKBM_RM_REMARK_4 | STRING | 64 | — | BOM remark line 4 |
| 15 | BKBM_RM_REMARK_5 | STRING | 64 | — | BOM remark line 5 |
| 16 | BKBM_RM_REMARK_6 | STRING | 64 | — | BOM remark line 6 |
| 17 | BKBM_RM_REMARK_7 | STRING | 64 | — | BOM remark line 7 |
| 18 | BKBM_RM_REMARK_8 | STRING | 64 | — | BOM remark line 8 |
| 19 | BKBM_RM_REMARK_9 | STRING | 64 | — | BOM remark line 9 |
| 20 | BKBM_RM_UID | STRING | 20 | — | Unique ID (import batch line identifier) |

## BKGLECOA
**DI CHART OF ACCOUNTS** — staging table for GL COA import

Fields: 65 | Key: BKGL_ACCT + BKGL_GLDPT

14 period slots per year-band: periods 1-12 = Jan-Dec, 13 = year-end adjusting entry,
14 = audit/final adjusting entry. Mirrors the live GL COA table (GLCHART).

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKGL_1YPAST_1 | NUMERIC | 8 | 2 | 1-year-past balance — period 1 (Jan) |
| 2 | BKGL_1YPAST_10 | NUMERIC | 8 | 2 | 1-year-past balance — period 10 (Oct) |
| 3 | BKGL_1YPAST_11 | NUMERIC | 8 | 2 | 1-year-past balance — period 11 (Nov) |
| 4 | BKGL_1YPAST_12 | NUMERIC | 8 | 2 | 1-year-past balance — period 12 (Dec) |
| 5 | BKGL_1YPAST_13 | NUMERIC | 8 | 2 | 1-year-past balance — period 13 (year-end adj.) |
| 6 | BKGL_1YPAST_14 | NUMERIC | 8 | 2 | 1-year-past balance — period 14 (audit adj.) |
| 7 | BKGL_1YPAST_2 | NUMERIC | 8 | 2 | 1-year-past balance — period 2 (Feb) |
| 8 | BKGL_1YPAST_3 | NUMERIC | 8 | 2 | 1-year-past balance — period 3 (Mar) |
| 9 | BKGL_1YPAST_4 | NUMERIC | 8 | 2 | 1-year-past balance — period 4 (Apr) |
| 10 | BKGL_1YPAST_5 | NUMERIC | 8 | 2 | 1-year-past balance — period 5 (May) |
| 11 | BKGL_1YPAST_6 | NUMERIC | 8 | 2 | 1-year-past balance — period 6 (Jun) |
| 12 | BKGL_1YPAST_7 | NUMERIC | 8 | 2 | 1-year-past balance — period 7 (Jul) |
| 13 | BKGL_1YPAST_8 | NUMERIC | 8 | 2 | 1-year-past balance — period 8 (Aug) |
| 14 | BKGL_1YPAST_9 | NUMERIC | 8 | 2 | 1-year-past balance — period 9 (Sep) |
| 15 | BKGL_1YPAST_YE | NUMERIC | 8 | 2 | 1 Yr. Past Year End Entry |
| 16 | BKGL_2YPAST_1 | NUMERIC | 8 | 2 | 2-years-past balance — period 1 |
| 17 | BKGL_2YPAST_10 | NUMERIC | 8 | 2 | 2-years-past balance — period 10 |
| 18 | BKGL_2YPAST_11 | NUMERIC | 8 | 2 | 2-years-past balance — period 11 |
| 19 | BKGL_2YPAST_12 | NUMERIC | 8 | 2 | 2-years-past balance — period 12 |
| 20 | BKGL_2YPAST_13 | NUMERIC | 8 | 2 | 2-years-past balance — period 13 (year-end adj.) |
| 21 | BKGL_2YPAST_14 | NUMERIC | 8 | 2 | 2-years-past balance — period 14 (audit adj.) |
| 22 | BKGL_2YPAST_2 | NUMERIC | 8 | 2 | 2-years-past balance — period 2 |
| 23 | BKGL_2YPAST_3 | NUMERIC | 8 | 2 | 2-years-past balance — period 3 |
| 24 | BKGL_2YPAST_4 | NUMERIC | 8 | 2 | 2-years-past balance — period 4 |
| 25 | BKGL_2YPAST_5 | NUMERIC | 8 | 2 | 2-years-past balance — period 5 |
| 26 | BKGL_2YPAST_6 | NUMERIC | 8 | 2 | 2-years-past balance — period 6 |
| 27 | BKGL_2YPAST_7 | NUMERIC | 8 | 2 | 2-years-past balance — period 7 |
| 28 | BKGL_2YPAST_8 | NUMERIC | 8 | 2 | 2-years-past balance — period 8 |
| 29 | BKGL_2YPAST_9 | NUMERIC | 8 | 2 | 2-years-past balance — period 9 |
| 30 | BKGL_2YPAST_YE | NUMERIC | 8 | 2 | 2 Yr. Past year End Entry |
| 31 | BKGL_ACCT | STRING | 10 | — | GL Account Code |
| 32 | BKGL_ACCTD | STRING | 25 | — | Account Description |
| 33 | BKGL_BUDGET_1 | NUMERIC | 8 | 2 | Budget — period 1 |
| 34 | BKGL_BUDGET_10 | NUMERIC | 8 | 2 | Budget — period 10 |
| 35 | BKGL_BUDGET_11 | NUMERIC | 8 | 2 | Budget — period 11 |
| 36 | BKGL_BUDGET_12 | NUMERIC | 8 | 2 | Budget — period 12 |
| 37 | BKGL_BUDGET_13 | NUMERIC | 8 | 2 | Budget — period 13 (year-end adj.) |
| 38 | BKGL_BUDGET_14 | NUMERIC | 8 | 2 | Budget — period 14 (audit adj.) |
| 39 | BKGL_BUDGET_2 | NUMERIC | 8 | 2 | Budget — period 2 |
| 40 | BKGL_BUDGET_3 | NUMERIC | 8 | 2 | Budget — period 3 |
| 41 | BKGL_BUDGET_4 | NUMERIC | 8 | 2 | Budget — period 4 |
| 42 | BKGL_BUDGET_5 | NUMERIC | 8 | 2 | Budget — period 5 |
| 43 | BKGL_BUDGET_6 | NUMERIC | 8 | 2 | Budget — period 6 |
| 44 | BKGL_BUDGET_7 | NUMERIC | 8 | 2 | Budget — period 7 |
| 45 | BKGL_BUDGET_8 | NUMERIC | 8 | 2 | Budget — period 8 |
| 46 | BKGL_BUDGET_9 | NUMERIC | 8 | 2 | Budget — period 9 |
| 47 | BKGL_CR_DR | STRING | 1 | — | Normal Credit/Debit |
| 48 | BKGL_CURRENT_1 | NUMERIC | 8 | 2 | Current year balance — period 1 |
| 49 | BKGL_CURRENT_10 | NUMERIC | 8 | 2 | Current year balance — period 10 |
| 50 | BKGL_CURRENT_11 | NUMERIC | 8 | 2 | Current year balance — period 11 |
| 51 | BKGL_CURRENT_12 | NUMERIC | 8 | 2 | Current year balance — period 12 |
| 52 | BKGL_CURRENT_13 | NUMERIC | 8 | 2 | Current year balance — period 13 (year-end adj.) |
| 53 | BKGL_CURRENT_14 | NUMERIC | 8 | 2 | Current year balance — period 14 (audit adj.) |
| 54 | BKGL_CURRENT_2 | NUMERIC | 8 | 2 | Current year balance — period 2 |
| 55 | BKGL_CURRENT_3 | NUMERIC | 8 | 2 | Current year balance — period 3 |
| 56 | BKGL_CURRENT_4 | NUMERIC | 8 | 2 | Current year balance — period 4 |
| 57 | BKGL_CURRENT_5 | NUMERIC | 8 | 2 | Current year balance — period 5 |
| 58 | BKGL_CURRENT_6 | NUMERIC | 8 | 2 | Current year balance — period 6 |
| 59 | BKGL_CURRENT_7 | NUMERIC | 8 | 2 | Current year balance — period 7 |
| 60 | BKGL_CURRENT_8 | NUMERIC | 8 | 2 | Current year balance — period 8 |
| 61 | BKGL_CURRENT_9 | NUMERIC | 8 | 2 | Current year balance — period 9 |
| 62 | BKGL_EXTRA | STRING | 50 | — | Extra |
| 63 | BKGL_GLDPT | STRING | 4 | — | GL Department |
| 64 | BKGL_NON_CASH | STRING | 1 | — | Non Cash Y/N |
| 65 | BKGL_TYPE | STRING | 1 | — | Account Type (ALOIE) |

## BKGLETRN
**TEMP FILE FOR IMPORT GL TRANSACTIONS**

Fields: 16 | Key: BKGL_TRN_TRXN

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKGL_TRN_AMT | NUMERIC | 8 | 2 | Amount |
| 2 | BKGL_TRN_BATCH | NUMERIC | 8 | — | Batch Number |
| 3 | BKGL_TRN_CODE | STRING | 10 | — | Trans Code |
| 4 | BKGL_TRN_DATE | DATE | 4 | — | Date |
| 5 | BKGL_TRN_DC | STRING | 1 | — | Debit/Credit |
| 6 | BKGL_TRN_DESC | STRING | 25 | — | Description |
| 7 | BKGL_TRN_ENTDTE | DATE | 4 | — | Enter Date |
| 8 | BKGL_TRN_EXTRA | STRING | 25 | — | Extra |
| 9 | BKGL_TRN_GLACCT | STRING | 10 | — | GL Account Code |
| 10 | BKGL_TRN_GLDPT | STRING | 4 | — | GL Department |
| 11 | BKGL_TRN_INVC | STRING | 10 | — | Invoice |
| 12 | BKGL_TRN_PART | STRING | 15 | — | Part code (for inventory-related GL postings) |
| 13 | BKGL_TRN_PERIOD | INTEGER | 2 | — | Period |
| 14 | BKGL_TRN_POST | STRING | 1 | — | Posted flag |
| 15 | BKGL_TRN_TRXN | NUMERIC | 8 | — | Trans Number |
| 16 | BKGL_TRN_TYPE | STRING | 2 | — | Type |

## BKICELOC
**TEMP FILE FOR IMPORT INVENTORY LOCATION** — staging table for inv. location import

Fields: 32 | Key: BKIC_LOC_PROD + BKIC_LOC_CODE + BKIC_LOC_BIN

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKIC_LOC_ALPHA1 | STRING | 30 | — | User-defined alphanumeric field 1 |
| 2 | BKIC_LOC_ALPHA2 | STRING | 30 | — | User-defined alphanumeric field 2 |
| 3 | BKIC_LOC_BIN | STRING | 15 | — | Bin designation within location |
| 4 | BKIC_LOC_CODE | STRING | 10 | — | Location Code |
| 5 | BKIC_LOC_DATE1 | DATE | 4 | — | User-defined date (last count date or effectivity) |
| 6 | BKIC_LOC_DPTA | STRING | 4 | — | GL Department |
| 7 | BKIC_LOC_DPTC | STRING | 4 | — | GL COGS Department |
| 8 | BKIC_LOC_DPTS | STRING | 4 | — | GL Sales Department |
| 9 | BKIC_LOC_DPTSNT | STRING | 4 | — | GL Sales Non Tax Department |
| 10 | BKIC_LOC_DPTWIP | STRING | 4 | — | GL WIP Department |
| 11 | BKIC_LOC_EXTRA | STRING | 50 | — | Extra data |
| 12 | BKIC_LOC_FLAG1 | STRING | 1 | — | User-defined flag 1 |
| 13 | BKIC_LOC_GLA | STRING | 10 | — | GL Account |
| 14 | BKIC_LOC_GLC | STRING | 10 | — | GL COGS Account |
| 15 | BKIC_LOC_GLS | STRING | 10 | — | GL Sales Account |
| 16 | BKIC_LOC_GLSNT | STRING | 10 | — | GL Sales Non-Tax Account |
| 17 | BKIC_LOC_GLWIP | STRING | 10 | — | GL WIP Account |
| 18 | BKIC_LOC_LCDATE | DATE | 4 | — | Last physical count date for this bin |
| 19 | BKIC_LOC_LOT | STRING | 15 | — | Lot number (for lot-controlled items) |
| 20 | BKIC_LOC_NUM1 | NUMERIC | 8 | — | User-defined numeric field 1 |
| 21 | BKIC_LOC_NUM2 | NUMERIC | 8 | — | User-defined numeric field 2 |
| 22 | BKIC_LOC_PROD | STRING | 15 | — | Part Number |
| 23 | BKIC_LOC_SER | STRING | 25 | — | Serial number (for serial-controlled items) |
| 24 | BKIC_LOC_UALLOC | NUMERIC | 8 | 2 | Units Allocated |
| 25 | BKIC_LOC_UBO | NUMERIC | 8 | 2 | Units on Back Order |
| 26 | BKIC_LOC_UIQC | NUMERIC | 8 | 2 | Units in QC |
| 27 | BKIC_LOC_UOH | NUMERIC | 8 | 2 | Units on Hand |
| 28 | BKIC_LOC_UOO | NUMERIC | 8 | 2 | Units on PO |
| 29 | BKIC_LOC_UOSO | NUMERIC | 8 | 2 | Units on Sales Order |
| 30 | BKIC_LOC_UOWO | NUMERIC | 8 | 2 | Units on Work Order |
| 31 | BKIC_LOC_UWIP | NUMERIC | 8 | 2 | Units in WIP |
| 32 | BKIC_LOC_WHCTRL | STRING | 1 | — | Warehouse control flag (W=warehouse controlled) |

## BKICEMTR
**TEMP FILE FOR IMPORT INVENTORY** — staging table for inventory master import

Fields: 64 | Key: BKIC_PROD_CODE

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKIC_IS_DCODE | STRING | 3 | — | Duty Code |
| 2 | BKIC_PROD_ADTR | INTEGER | 2 | — | Average Days To Receive |
| 3 | BKIC_PROD_AVFO | NUMERIC | 8 | 4 | MRP Sensitivity Expedite Buffer |
| 4 | BKIC_PROD_AVGC | NUMERIC | 8 | 4 | Average Cost |
| 5 | BKIC_PROD_AVLAB | NUMERIC | 8 | 4 | Average labor cost |
| 6 | BKIC_PROD_AVMAT | NUMERIC | 8 | 4 | Average Material Cost |
| 7 | BKIC_PROD_AVOP | NUMERIC | 8 | 4 | Commissions Y/N |
| 8 | BKIC_PROD_AVSET | NUMERIC | 8 | 4 | Average Setup cost |
| 9 | BKIC_PROD_AVVO | NUMERIC | 8 | 4 | MRP Sensititity Delay Buffer |
| 10 | BKIC_PROD_CAT | STRING | 4 | — | Category (optional) |
| 11 | BKIC_PROD_CLASS | STRING | 4 | — | Product Class (required) |
| 12 | BKIC_PROD_CLYR | NUMERIC | 8 | 2 | Cost od Goods Last Year |
| 13 | BKIC_PROD_CMTD | NUMERIC | 8 | 2 | Cost of Goods Month-To-Date |
| 14 | BKIC_PROD_CODE | STRING | 15 | — | Product Code |
| 15 | BKIC_PROD_CVAR | NUMERIC | 8 | 4 | Cost of Goods Variance |
| 16 | BKIC_PROD_CYTD | NUMERIC | 8 | 2 | Cost of Goods Year-To-Date |
| 17 | BKIC_PROD_DESC | STRING | 30 | — | Description |
| 18 | BKIC_PROD_DPTA | STRING | 4 | — | GL Dept Asset/Expense Account |
| 19 | BKIC_PROD_DPTC | STRING | 4 | — | GL Dept COGS |
| 20 | BKIC_PROD_DPTNT | STRING | 4 | — | GL Dept. Sales Non Tax |
| 21 | BKIC_PROD_DPTS | STRING | 4 | — | GL Dept. Sales |
| 22 | BKIC_PROD_EXTRA | STRING | 100 | — | Extra |
| 23 | BKIC_PROD_GLA | STRING | 10 | — | GL Asset/Expense Account |
| 24 | BKIC_PROD_GLC | STRING | 10 | — | GL COGS Account |
| 25 | BKIC_PROD_GLS | STRING | 10 | — | GL Sales Account |
| 26 | BKIC_PROD_GLSNT | STRING | 10 | — | GL Sales Non-Tax Account |
| 27 | BKIC_PROD_GSLYR | NUMERIC | 8 | 2 | Gross Sales Last Year |
| 28 | BKIC_PROD_GSMTD | NUMERIC | 8 | 2 | Gross Sales Month-To-Date |
| 29 | BKIC_PROD_GSVAR | NUMERIC | 8 | 4 | Gross Sales Variance |
| 30 | BKIC_PROD_GSYTD | NUMERIC | 8 | 2 | Gross Sales Year-To-Date |
| 31 | BKIC_PROD_ISUPC | STRING | 12 | — | UPC Code |
| 32 | BKIC_PROD_LONGP | STRING | 25 | — | Long part number / cross-reference code |
| 33 | BKIC_PROD_LORD | DATE | 4 | — | Last Order Date |
| 34 | BKIC_PROD_LRCPT | DATE | 4 | — | Last Receipt Date |
| 35 | BKIC_PROD_LSALE | DATE | 4 | — | Last Sale Date |
| 36 | BKIC_PROD_LSTC | NUMERIC | 8 | 4 | Last Cost |
| 37 | BKIC_PROD_MANUF | STRING | 20 | — | Manufacturer code |
| 38 | BKIC_PROD_NGLYR | NUMERIC | 8 | 4 | Net gross profit last year |
| 39 | BKIC_PROD_NGMTD | NUMERIC | 8 | 4 | Net gross profit month-to-date |
| 40 | BKIC_PROD_NGVAR | NUMERIC | 8 | 4 | Net gross profit variance |
| 41 | BKIC_PROD_NGYTD | NUMERIC | 8 | 4 | Net gross profit year-to-date |
| 42 | BKIC_PROD_NOTE | STRING | 30 | — | Description Line 2 |
| 43 | BKIC_PROD_NSLYR | NUMERIC | 8 | 2 | Net Sales Last Year |
| 44 | BKIC_PROD_NSMTD | NUMERIC | 8 | 2 | Net Sales Month-To-Date |
| 45 | BKIC_PROD_NSVAR | NUMERIC | 8 | 4 | Net Sales Variance |
| 46 | BKIC_PROD_NSYTD | NUMERIC | 8 | 2 | Net Sales Year-To-Date |
| 47 | BKIC_PROD_PMAT | INTEGER | 2 | — | Price matrix code |
| 48 | BKIC_PROD_PRICE | NUMERIC | 8 | 4 | Base Price |
| 49 | BKIC_PROD_RAMT | NUMERIC | 8 | — | Reorder Amount |
| 50 | BKIC_PROD_RLVL | NUMERIC | 8 | — | Reorder Level |
| 51 | BKIC_PROD_TAXIN | STRING | 1 | — | Tax In Y/N |
| 52 | BKIC_PROD_TO | NUMERIC | 8 | 4 | Turnover rate |
| 53 | BKIC_PROD_TOTVL | NUMERIC | 8 | 2 | Book Value |
| 54 | BKIC_PROD_TXBLE | STRING | 1 | — | Taxable (Y/N) |
| 55 | BKIC_PROD_TYPE | STRING | 1 | — | Type (NRMFABLTKO) |
| 56 | BKIC_PROD_UBO | NUMERIC | 8 | 2 | Units on Back Order |
| 57 | BKIC_PROD_UM | STRING | 3 | — | Stock  J3491Unit of Measure |
| 58 | BKIC_PROD_UOH | NUMERIC | 8 | 2 | Units On-Hand |
| 59 | BKIC_PROD_UOO | NUMERIC | 8 | 2 | Units on Purchase Order |
| 60 | BKIC_PROD_UOSO | NUMERIC | 8 | 2 | Units on Sales Order |
| 61 | BKIC_PROD_USLYR | NUMERIC | 8 | 2 | Units Sold Last Year |
| 62 | BKIC_PROD_USMTD | NUMERIC | 8 | 2 | Units Sold Month-To-Date |
| 63 | BKIC_PROD_USVAR | NUMERIC | 8 | 4 | Units Sold Variance |
| 64 | BKIC_PROD_USYTD | NUMERIC | 8 | 2 | Units Sold Year-To-Date |

## BKRTEMTR
**TEMP FILE FOR IMPORT ROUTINGS** — staging table for routing master import

Fields: 62 | Key: MTRO_CODE + MTRO_NUM + MTRO_OPER

Identical schema to ROUTING/ROUTAING/ROUTTEMP (MTRO_* prefix). See
[fields-ro.md](fields-ro.md) ROUTAING section for all field definitions including
DEF_TIME, EST_LINE, EST_TAG, INSTR_1..15, MD_PROC_HR, MISC_ACOST, R_TYPE, TIME_PERPR.

## MTICEMTR
**TEMP INVENTORY IMPORT FILE** — extended inventory import with vendor and pricing tiers

Fields: 109 | Key: MTIC_PROD_CODE

Extended inventory import including 10 vendor slots (VEND/VNAM/VPC), 15 cost tier slots
(RCOST), 12 spec lines, and 5 substitute parts. Mirrors BKICMSTR + vendor cross-ref.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTIC_PROD_ABC | STRING | 1 | — | Vendor Approval ,1,2 |
| 2 | MTIC_PROD_ACTIV | STRING | 1 | — | Active Inventory Y/N |
| 3 | MTIC_PROD_AVAIL | NUMERIC | 8 | 2 | Available |
| 4 | MTIC_PROD_CLASS | STRING | 4 | — | Product Class |
| 5 | MTIC_PROD_CLDES | STRING | 30 | — | Product Class Description |
| 6 | MTIC_PROD_CODE | STRING | 15 | — | Produce Code (Part Number) |
| 7 | MTIC_PROD_COMM | NUMERIC | 8 | 4 | Commission |
| 8 | MTIC_PROD_COST | STRING | 1 | — | Not Used |
| 9 | MTIC_PROD_CUBFT | NUMERIC | 8 | 4 | Cubic Feet |
| 10 | MTIC_PROD_CUM | STRING | 3 | — | Not Used |
| 11 | MTIC_PROD_CUSNM | STRING | 30 | — | Customer Name (not used) |
| 12 | MTIC_PROD_CUST | STRING | 10 | — | Customer Code |
| 13 | MTIC_PROD_CYCLE | STRING | 1 | — | Cycle Count Code |
| 14 | MTIC_PROD_DELBF | INTEGER | 2 | — | MRP Delay Buffer |
| 15 | MTIC_PROD_DESC | STRING | 30 | — | Description - Line 1 |
| 16 | MTIC_PROD_DRAW | STRING | 15 | — | Drawing Number |
| 17 | MTIC_PROD_ESTCD | STRING | 1 | — | Not Used |
| 18 | MTIC_PROD_EXPBF | INTEGER | 2 | — | MRP Expedite Buffer |
| 19 | MTIC_PROD_FRT | NUMERIC | 8 | 6 | Freight Percent |
| 20 | MTIC_PROD_FRT^ | NUMERIC | 8 | 2 | Freight cost flat amount (computed from freight %) |
| 21 | MTIC_PROD_GLINV | STRING | 10 | — | Not Used |
| 22 | MTIC_PROD_GLWIP | STRING | 10 | — | GL WIP Account |
| 23 | MTIC_PROD_INVDP | STRING | 4 | — | Not Used |
| 24 | MTIC_PROD_LEAD | INTEGER | 2 | — | Lead Time - Days |
| 25 | MTIC_PROD_LOC | STRING | 10 | — | Inventory Bin Location |
| 26 | MTIC_PROD_LONGP | STRING | 25 | — | Not Used |
| 27 | MTIC_PROD_LOT | STRING | 1 | — | Lot Control Y/N |
| 28 | MTIC_PROD_LOTSZ | NUMERIC | 8 | — | Lot Size |
| 29 | MTIC_PROD_MRP | STRING | 1 | — | MRP Item Y/N |
| 30 | MTIC_PROD_MRPSW | STRING | 1 | — | MRP Round to Whole Number Y/N |
| 31 | MTIC_PROD_OPT | STRING | 1 | — | Has Options Y/N |
| 32 | MTIC_PROD_OPTCD | STRING | 5 | — | Not Used |
| 33 | MTIC_PROD_OPTCS | STRING | 1 | — | Not Used |
| 34 | MTIC_PROD_OPTPR | INTEGER | 2 | — | Option pricing matrix code |
| 35 | MTIC_PROD_PCONV | NUMERIC | 8 | 5 | PO Conversion Multiplier |
| 36 | MTIC_PROD_PUM | STRING | 3 | — | Purchase Unit Measure |
| 37 | MTIC_PROD_RCOST_1 | NUMERIC | 8 | 6 | Price tier cost — tier 1 |
| 38 | MTIC_PROD_RCOST_10 | NUMERIC | 8 | 6 | Price tier cost — tier 10 |
| 39 | MTIC_PROD_RCOST_11 | NUMERIC | 8 | 6 | Price tier cost — tier 11 |
| 40 | MTIC_PROD_RCOST_12 | NUMERIC | 8 | 6 | Price tier cost — tier 12 |
| 41 | MTIC_PROD_RCOST_13 | NUMERIC | 8 | 6 | Price tier cost — tier 13 |
| 42 | MTIC_PROD_RCOST_14 | NUMERIC | 8 | 6 | Price tier cost — tier 14 |
| 43 | MTIC_PROD_RCOST_15 | NUMERIC | 8 | 6 | Price tier cost — tier 15 |
| 44 | MTIC_PROD_RCOST_2 | NUMERIC | 8 | 6 | Price tier cost — tier 2 |
| 45 | MTIC_PROD_RCOST_3 | NUMERIC | 8 | 6 | Price tier cost — tier 3 |
| 46 | MTIC_PROD_RCOST_4 | NUMERIC | 8 | 6 | Price tier cost — tier 4 |
| 47 | MTIC_PROD_RCOST_5 | NUMERIC | 8 | 6 | Price tier cost — tier 5 |
| 48 | MTIC_PROD_RCOST_6 | NUMERIC | 8 | 6 | Price tier cost — tier 6 |
| 49 | MTIC_PROD_RCOST_7 | NUMERIC | 8 | 6 | Price tier cost — tier 7 |
| 50 | MTIC_PROD_RCOST_8 | NUMERIC | 8 | 6 | Price tier cost — tier 8 |
| 51 | MTIC_PROD_RCOST_9 | NUMERIC | 8 | 6 | Price tier cost — tier 9 |
| 52 | MTIC_PROD_REV | STRING | 5 | — | Revision Level |
| 53 | MTIC_PROD_SER | STRING | 1 | — | Serial Control Y/N |
| 54 | MTIC_PROD_SPECS_1 | STRING | 30 | — | Item specification line 1 |
| 55 | MTIC_PROD_SPECS_10 | STRING | 30 | — | Item specification line 10 |
| 56 | MTIC_PROD_SPECS_11 | STRING | 30 | — | Item specification line 11 |
| 57 | MTIC_PROD_SPECS_12 | STRING | 30 | — | Item specification line 12 |
| 58 | MTIC_PROD_SPECS_2 | STRING | 30 | — | Item specification line 2 |
| 59 | MTIC_PROD_SPECS_3 | STRING | 30 | — | Item specification line 3 |
| 60 | MTIC_PROD_SPECS_4 | STRING | 30 | — | Item specification line 4 |
| 61 | MTIC_PROD_SPECS_5 | STRING | 30 | — | Item specification line 5 |
| 62 | MTIC_PROD_SPECS_6 | STRING | 30 | — | Item specification line 6 |
| 63 | MTIC_PROD_SPECS_7 | STRING | 30 | — | Item specification line 7 |
| 64 | MTIC_PROD_SPECS_8 | STRING | 30 | — | Item specification line 8 |
| 65 | MTIC_PROD_SPECS_9 | STRING | 30 | — | Item specification line 9 |
| 66 | MTIC_PROD_STDC | NUMERIC | 8 | 6 | Not Used |
| 67 | MTIC_PROD_STDPK | NUMERIC | 8 | — | Standard Pack Quantity |
| 68 | MTIC_PROD_SUBST_1 | STRING | 25 | — | Substitute part code 1 |
| 69 | MTIC_PROD_SUBST_2 | STRING | 25 | — | Substitute part code 2 |
| 70 | MTIC_PROD_SUBST_3 | STRING | 25 | — | Substitute part code 3 |
| 71 | MTIC_PROD_SUBST_4 | STRING | 25 | — | Substitute part code 4 |
| 72 | MTIC_PROD_SUBST_5 | STRING | 25 | — | Substitute part code 5 |
| 73 | MTIC_PROD_SUM | STRING | 3 | — | Sales Unit Measure |
| 74 | MTIC_PROD_TYPE | STRING | 1 | — | Product TYPE (RFAMKLTBO) |
| 75 | MTIC_PROD_UIQC | NUMERIC | 8 | 2 | Units in QC |
| 76 | MTIC_PROD_UIWIP | NUMERIC | 8 | 2 | Units in WIP |
| 77 | MTIC_PROD_UOA | NUMERIC | 8 | 2 | Units On Allocations |
| 78 | MTIC_PROD_UOWO | NUMERIC | 8 | 2 | Units On Work Order |
| 79 | MTIC_PROD_VEND_1 | STRING | 10 | — | Vendor code — slot 1 (primary vendor) |
| 80 | MTIC_PROD_VEND_10 | STRING | 10 | — | Vendor code — slot 10 |
| 81 | MTIC_PROD_VEND_2 | STRING | 10 | — | Vendor code — slot 2 |
| 82 | MTIC_PROD_VEND_3 | STRING | 10 | — | Vendor code — slot 3 |
| 83 | MTIC_PROD_VEND_4 | STRING | 10 | — | Vendor code — slot 4 |
| 84 | MTIC_PROD_VEND_5 | STRING | 10 | — | Vendor code — slot 5 |
| 85 | MTIC_PROD_VEND_6 | STRING | 10 | — | Vendor code — slot 6 |
| 86 | MTIC_PROD_VEND_7 | STRING | 10 | — | Vendor code — slot 7 |
| 87 | MTIC_PROD_VEND_8 | STRING | 10 | — | Vendor code — slot 8 |
| 88 | MTIC_PROD_VEND_9 | STRING | 10 | — | Vendor code — slot 9 |
| 89 | MTIC_PROD_VNAM_1 | STRING | 30 | — | Vendor name — slot 1 (denormalized from BKAPVEND) |
| 90 | MTIC_PROD_VNAM_10 | STRING | 30 | — | Vendor name — slot 10 |
| 91 | MTIC_PROD_VNAM_2 | STRING | 30 | — | Vendor name — slot 2 |
| 92 | MTIC_PROD_VNAM_3 | STRING | 30 | — | Vendor name — slot 3 |
| 93 | MTIC_PROD_VNAM_4 | STRING | 30 | — | Vendor name — slot 4 |
| 94 | MTIC_PROD_VNAM_5 | STRING | 30 | — | Vendor name — slot 5 |
| 95 | MTIC_PROD_VNAM_6 | STRING | 30 | — | Vendor name — slot 6 |
| 96 | MTIC_PROD_VNAM_7 | STRING | 30 | — | Vendor name — slot 7 |
| 97 | MTIC_PROD_VNAM_8 | STRING | 30 | — | Vendor name — slot 8 |
| 98 | MTIC_PROD_VNAM_9 | STRING | 30 | — | Vendor name — slot 9 |
| 99 | MTIC_PROD_VPC_1 | STRING | 20 | — | Vendor part code — slot 1 (vendor's item number for this part) |
| 100 | MTIC_PROD_VPC_2 | STRING | 20 | — | Vendor part code — slot 2 |
| 101 | MTIC_PROD_VPC_3 | STRING | 20 | — | Vendor part code — slot 3 |
| 102 | MTIC_PROD_VPC_4 | STRING | 20 | — | Vendor part code — slot 4 |
| 103 | MTIC_PROD_VPC_5 | STRING | 20 | — | Vendor part code — slot 5 |
| 104 | MTIC_PROD_VPC_6 | STRING | 20 | — | Vendor part code — slot 6 |
| 105 | MTIC_PROD_VPC_7 | STRING | 20 | — | Vendor part code — slot 7 |
| 106 | MTIC_PROD_VPC_8 | STRING | 20 | — | Vendor part code — slot 8 |
| 107 | MTIC_PROD_VPC_9 | STRING | 20 | — | Vendor part code — slot 9 |
| 108 | MTIC_PROD_WIPDP | STRING | 4 | — | GL WIP Department |
| 109 | MTIC_PROD_WT | NUMERIC | 8 | 6 | Weight |

## WOELABOR
**TEMP FILE FOR LABOR IMPORT** — staging table for WO labor posting import

Fields: 45 | Key: MTWOLA_WOPRE + MTWOLA_WOSUF + MTWOLA_OPER + MTWOLA_TRXN

Mirrors WO labor posting (MTWOLA_* prefix). All fields are blank in source —
meanings inferred from WO labor module conventions.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTWOLA_ASSY | STRING | 15 | — | Assembly part code (WO finished item) |
| 2 | MTWOLA_ASSYDESC | STRING | 30 | — | Assembly description |
| 3 | MTWOLA_AUDIT | STRING | 35 | — | Audit trail string (who/what/when summary) |
| 4 | MTWOLA_COMPLETE | STRING | 1 | — | Operation complete flag: `Y`=operation marked complete |
| 5 | MTWOLA_DATE | DATE | 4 | — | Labor date (primary work date) |
| 6 | MTWOLA_DATE2 | DATE | 4 | — | Secondary/end date (for multi-day operations) |
| 7 | MTWOLA_DEDUCT | TIME | 4 | — | Deduct time (lunch/break deduction from clocked time) |
| 8 | MTWOLA_EMP | INTEGER | 2 | — | Employee number — primary (FK → employee master) |
| 9 | MTWOLA_EMP2 | INTEGER | 2 | — | Employee number — secondary (2-person operation) |
| 10 | MTWOLA_EXTRA | STRING | 50 | — | Extra data |
| 11 | MTWOLA_FOHCOST | NUMERIC | 8 | 2 | Fixed overhead cost for this posting |
| 12 | MTWOLA_LABCOST | NUMERIC | 8 | 2 | Labor cost amount |
| 13 | MTWOLA_LABRATE | NUMERIC | 8 | 4 | Labor rate applied |
| 14 | MTWOLA_MACH | STRING | 4 | — | Machine code used |
| 15 | MTWOLA_MACHCOST | NUMERIC | 8 | 2 | Machine cost amount |
| 16 | MTWOLA_MACHDATE | DATE | 4 | — | Machine usage date |
| 17 | MTWOLA_MISC | NUMERIC | 8 | 6 | Miscellaneous cost rate or amount |
| 18 | MTWOLA_MISCDESC | STRING | 30 | — | Miscellaneous cost description |
| 19 | MTWOLA_NOJOBS | INTEGER | 2 | — | Number of concurrent jobs in this period |
| 20 | MTWOLA_OPER | INTEGER | 2 | — | Operation number (FK → routing MTRO_OPER) |
| 21 | MTWOLA_OTEAM | INTEGER | 2 | — | Original team size for this operation |
| 22 | MTWOLA_PARTS | NUMERIC | 8 | 2 | Parts completed in this labor posting |
| 23 | MTWOLA_POSTED | STRING | 1 | — | Posted flag: `Y`=labor has been posted to WO |
| 24 | MTWOLA_QCCODE | STRING | 2 | — | QC disposition code |
| 25 | MTWOLA_QCDESC | STRING | 30 | — | QC disposition description |
| 26 | MTWOLA_REGOVER | STRING | 1 | — | Regular or overtime flag: `R`=regular, `O`=overtime |
| 27 | MTWOLA_REWORK | STRING | 1 | — | Rework flag: `Y`=this labor is rework time |
| 28 | MTWOLA_RUNHRS | NUMERIC | 8 | 2 | Run hours clocked |
| 29 | MTWOLA_SCDESC | STRING | 30 | — | Scrap reason code description |
| 30 | MTWOLA_SCRAPCD | STRING | 2 | — | Scrap reason code |
| 31 | MTWOLA_SCRAPPED | NUMERIC | 8 | 2 | Quantity scrapped during this operation |
| 32 | MTWOLA_SETCOST | NUMERIC | 8 | 2 | Setup cost amount |
| 33 | MTWOLA_SETUPHRS | NUMERIC | 8 | 2 | Setup hours |
| 34 | MTWOLA_SHIFT | INTEGER | 2 | — | Shift number (1/2/3) |
| 35 | MTWOLA_START | TIME | 4 | — | Start time (clock-in time) |
| 36 | MTWOLA_STOP | TIME | 4 | — | Stop time (clock-out time) |
| 37 | MTWOLA_TEAM | INTEGER | 2 | — | Team size — number of people working simultaneously |
| 38 | MTWOLA_TOOL | STRING | 15 | — | Tool code used |
| 39 | MTWOLA_TOOLDATE | DATE | 4 | — | Tool usage date |
| 40 | MTWOLA_TRXN | INTEGER | 2 | — | Transaction sequence number |
| 41 | MTWOLA_VOHCOST | NUMERIC | 8 | 2 | Variable overhead cost |
| 42 | MTWOLA_WC | STRING | 12 | — | Work center |
| 43 | MTWOLA_WCDATE | DATE | 4 | — | Work center usage date |
| 44 | MTWOLA_WOPRE | NUMERIC | 8 | — | WO prefix number |
| 45 | MTWOLA_WOSUF | INTEGER | 2 | — | WO suffix number |

## WOEMAT
**DI MATERIAL ISSUES** — staging table for WO material issue import

Fields: 17 | Key: WOMAT_WOPRE + WOMAT_WOSUF + WOMAT_PCODE

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTWO_PRODCODE | STRING | 15 | — | Assembly/WO product code (WO finished item) |
| 2 | WOMAT_COST | NUMERIC | 8 | 2 | Material cost issued |
| 3 | WOMAT_DATE | DATE | 4 | — | Issue date |
| 4 | WOMAT_EXTRA | STRING | 50 | — | Extra data |
| 5 | WOMAT_KIT | STRING | 1 | — | Kit flag: `Y`=kit issue (all BOM components at once) |
| 6 | WOMAT_LOT | STRING | 15 | — | Lot number of issued component |
| 7 | WOMAT_PCODE | STRING | 15 | — | Component part code issued (FK → BKICMSTR) |
| 8 | WOMAT_PDESC | STRING | 30 | — | Component description |
| 9 | WOMAT_PRODDESC | STRING | 30 | — | Assembly description |
| 10 | WOMAT_QTYISSUED | NUMERIC | 8 | 4 | Quantity issued |
| 11 | WOMAT_QTYSCRAP | NUMERIC | 8 | 2 | Quantity scrapped during this issue |
| 12 | WOMAT_REF | STRING | 15 | — | Reference (routing seq. or BOM line cross-ref) |
| 13 | WOMAT_SCDESC | STRING | 30 | — | Scrap reason code description |
| 14 | WOMAT_SCRAPCD | STRING | 2 | — | Scrap reason code |
| 15 | WOMAT_SERIAL | STRING | 25 | — | Serial number of issued component (for serial-tracked parts) |
| 16 | WOMAT_WOPRE | NUMERIC | 8 | — | WO prefix number |
| 17 | WOMAT_WOSUF | INTEGER | 2 | — | WO suffix number |

## WOERECV
**DI WO RECEIPTS** — staging table for WO receipts import

Fields: 11 | Key: MTWOR_WOPRE + MTWOR_WOSUF

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTWOR_ASSY | STRING | 15 | — | Assembly part code (WO finished item) |
| 2 | MTWOR_AVGC | NUMERIC | 8 | 4 | Average cost at time of receipt |
| 3 | MTWOR_DATE | DATE | 4 | — | Receipt date |
| 4 | MTWOR_DESC | STRING | 30 | — | Assembly description |
| 5 | MTWOR_LOT | STRING | 15 | — | Lot number assigned to completed assembly |
| 6 | MTWOR_QTY | NUMERIC | 8 | 2 | Quantity received/completed |
| 7 | MTWOR_REF | STRING | 15 | — | Reference |
| 8 | MTWOR_SERIAL | STRING | 25 | — | Serial number assigned to completed assembly |
| 9 | MTWOR_USESTD | STRING | 1 | — | Use standard cost flag: `Y`=book at std cost |
| 10 | MTWOR_WOPRE | NUMERIC | 8 | — | WO prefix number |
| 11 | MTWOR_WOSUF | INTEGER | 2 | — | WO suffix number |

**Confidence: 82/100** — most DI temp table fields confirmed from their live-table counterparts
(BKAPEIVT mirrors AP, BKARECST mirrors AR customer, BKGLECOA mirrors GL COA, etc.); BKRTEMTR
is identical to ROUTING (fully confirmed in fields-ro.md); WOELABOR/WOEMAT/WOERECV WO labor
field semantics carry from WO module knowledge; BKGLECOA 14-period structure (12+2 adj) is
a GL accounting convention, not confirmed from live GL data; MTICEMTR RCOST tier count (15)
and VEND slot count (10) confirmed from field names.
