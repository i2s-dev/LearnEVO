# DI — Distribution: Field Reference

Status: verified-schema

Source: `Evo-DBA_File_Fields 052421.xlsx`, sheet "Fields".
Field descriptions where provided by source; otherwise name-inferred.

---

## BKAPEIVT
**TEMP FILE FOR IMPORT OPEN AP**

Fields: 19

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAP_INVT_AMT | NUMERIC | 8 | 2 | Amount |
| 2 | BKAP_INVT_AMTRM | NUMERIC | 8 | 2 | Amount Remaining |
| 3 | BKAP_INVT_CHKAC | INTEGER | 2 | — | — |
| 4 | BKAP_INVT_CHKNO | NUMERIC | 8 | — | — |
| 5 | BKAP_INVT_CODE | STRING | 10 | — | Vendor Code |
| 6 | BKAP_INVT_DATE | DATE | 4 | — | Transaction Date |
| 7 | BKAP_INVT_DEPNO | NUMERIC | 8 | — | — |
| 8 | BKAP_INVT_DESC | STRING | 25 | — | Transaction Description |
| 9 | BKAP_INVT_EXTRA | STRING | 50 | — | Extra |
| 10 | BKAP_INVT_FRT | NUMERIC | 8 | 2 | — |
| 11 | BKAP_INVT_GLDPT | STRING | 4 | — | GL Department |
| 12 | BKAP_INVT_MCCOD | STRING | 3 | — | Currency Code |
| 13 | BKAP_INVT_MCRAT | NUMERIC | 8 | 6 | Currency Rate |
| 14 | BKAP_INVT_NUM | STRING | 10 | — | Invoice/Voucher Reference No. |
| 15 | BKAP_INVT_PDATE | DATE | 4 | — | Post Date |
| 16 | BKAP_INVT_SDATE | DATE | 4 | — | Start Date |
| 17 | BKAP_INVT_TAX | NUMERIC | 8 | 2 | — |
| 18 | BKAP_INVT_TERMN | INTEGER | 2 | — | Terms Number |
| 19 | BKAP_INVT_TYPE | STRING | 1 | — | transaction Type (IPCM) |

## BKAPEVND
**TEMP FILE FOR IMPORT VENDOR**

Fields: 72

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAP_ADD1_1 | STRING | 30 | — | — |
| 2 | BKAP_ADD1_2 | STRING | 30 | — | — |
| 3 | BKAP_ADD2_1 | STRING | 30 | — | — |
| 4 | BKAP_ADD2_2 | STRING | 30 | — | — |
| 5 | BKAP_ADD3 | STRING | 30 | — | Address line 3 |
| 6 | BKAP_ALPHA1 | STRING | 25 | — | — |
| 7 | BKAP_ALPHA2 | STRING | 25 | — | — |
| 8 | BKAP_CITY_1 | STRING | 26 | — | — |
| 9 | BKAP_CITY_2 | STRING | 26 | — | — |
| 10 | BKAP_CLASS | STRING | 4 | — | Vendor Class - user defined |
| 11 | BKAP_CONTACT_1 | STRING | 30 | — | — |
| 12 | BKAP_CONTACT_2 | STRING | 30 | — | — |
| 13 | BKAP_CONTACT_3 | STRING | 30 | — | — |
| 14 | BKAP_CONTACT_4 | STRING | 30 | — | — |
| 15 | BKAP_COUNTRY_1 | STRING | 30 | — | — |
| 16 | BKAP_COUNTRY_2 | STRING | 30 | — | — |
| 17 | BKAP_CREDLIM | NUMERIC | 8 | 2 | — |
| 18 | BKAP_CUST_CODE | STRING | 15 | — | — |
| 19 | BKAP_DATE1 | DATE | 4 | — | — |
| 20 | BKAP_DATE2 | DATE | 4 | — | — |
| 21 | BKAP_DESC | STRING | 25 | — | Description |
| 22 | BKAP_EMAIL_1 | STRING | 128 | — | — |
| 23 | BKAP_EMAIL_2 | STRING | 128 | — | — |
| 24 | BKAP_EMAIL_3 | STRING | 128 | — | — |
| 25 | BKAP_EMAIL_4 | STRING | 128 | — | — |
| 26 | BKAP_EMAIL_5 | STRING | 128 | — | — |
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
| 40 | BKAP_NOTES_1 | STRING | 60 | — | — |
| 41 | BKAP_NOTES_10 | STRING | 60 | — | — |
| 42 | BKAP_NOTES_2 | STRING | 60 | — | — |
| 43 | BKAP_NOTES_3 | STRING | 60 | — | — |
| 44 | BKAP_NOTES_4 | STRING | 60 | — | — |
| 45 | BKAP_NOTES_5 | STRING | 60 | — | — |
| 46 | BKAP_NOTES_6 | STRING | 60 | — | — |
| 47 | BKAP_NOTES_7 | STRING | 60 | — | — |
| 48 | BKAP_NOTES_8 | STRING | 60 | — | — |
| 49 | BKAP_NOTES_9 | STRING | 60 | — | — |
| 50 | BKAP_OUT_CREDIT | NUMERIC | 8 | 2 | Outstanding Credits |
| 51 | BKAP_OUTINV | NUMERIC | 8 | 2 | Number of Outstanding Invoices |
| 52 | BKAP_PURCH_LYR | NUMERIC | 8 | 2 | Purchases Last Year |
| 53 | BKAP_PURCH_MTD | NUMERIC | 8 | 2 | Purchases Month-to-Date |
| 54 | BKAP_PURCH_VAR | NUMERIC | 8 | 4 | Variance Percent- Last Year to YTD |
| 55 | BKAP_PURCH_YTD | NUMERIC | 8 | 2 | Purchases Year-to-Date |
| 56 | BKAP_REM_STATE | STRING | 2 | — | Bill To State |
| 57 | BKAP_REM_ZIP | STRING | 10 | — | Bill To Zip Code |
| 58 | BKAP_REQQC | STRING | 1 | — | — |
| 59 | BKAP_SHIP_VIA | STRING | 15 | — | Ship Via Carrier |
| 60 | BKAP_SORT | STRING | 6 | — | Sort Field |
| 61 | BKAP_START_DATE | DATE | 4 | — | Vendor Start Date |
| 62 | BKAP_STATE | STRING | 2 | — | State |
| 63 | BKAP_TAX_ID | STRING | 20 | — | Federal Tax ID Number |
| 64 | BKAP_TELEPHONE_1 | STRING | 25 | — | — |
| 65 | BKAP_TELEPHONE_2 | STRING | 25 | — | — |
| 66 | BKAP_TELEPHONE_3 | STRING | 25 | — | — |
| 67 | BKAP_TELEPHONE_4 | STRING | 25 | — | — |
| 68 | BKAP_TELEPHONE_5 | STRING | 25 | — | — |
| 69 | BKAP_TERMS_NUM | INTEGER | 2 | — | Terms Number |
| 70 | BKAP_VENDCODE | STRING | 10 | — | Vendor Code |
| 71 | BKAP_VENDNAME | STRING | 30 | — | Vendor Name |
| 72 | BKAP_ZIP | STRING | 10 | — | Zip Code |

## BKARECST
**TEMP FILE FOR IMPORT CUSTOMER**

Fields: 106

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAR_ADD1 | STRING | 30 | — | Address Line 1 |
| 2 | BKAR_ADD2_1 | STRING | 30 | — | — |
| 3 | BKAR_ADD2_2 | STRING | 30 | — | — |
| 4 | BKAR_CARRIER | STRING | 15 | — | Carrier |
| 5 | BKAR_CHG_INTRST | STRING | 1 | — | Charge Interst Y/N |
| 6 | BKAR_CITY | STRING | 26 | — | City |
| 7 | BKAR_CLASS | STRING | 4 | — | Customer Class |
| 8 | BKAR_COGS_LYR | NUMERIC | 8 | 2 | COGS Last Year |
| 9 | BKAR_COGS_MTD | NUMERIC | 8 | 2 | COGS Month To Date |
| 10 | BKAR_COGS_PVAR | NUMERIC | 8 | 4 | COGS Percent Variance |
| 11 | BKAR_COGS_YTD | NUMERIC | 8 | 2 | COGS Year To Date |
| 12 | BKAR_COMM_1 | NUMERIC | 8 | 4 | — |
| 13 | BKAR_COMM_2 | NUMERIC | 8 | 4 | — |
| 14 | BKAR_CONTACT_1 | STRING | 30 | — | — |
| 15 | BKAR_CONTACT_2 | STRING | 30 | — | — |
| 16 | BKAR_CONTACT_3 | STRING | 30 | — | — |
| 17 | BKAR_CONTACT_4 | STRING | 30 | — | — |
| 18 | BKAR_CONTACT_5 | STRING | 30 | — | — |
| 19 | BKAR_COOP_AMT | NUMERIC | 8 | 2 | COOP Amount |
| 20 | BKAR_COOP_RATE | NUMERIC | 8 | 4 | COOP Rate |
| 21 | BKAR_COUNTRY | STRING | 30 | — | Country |
| 22 | BKAR_CREDIT_HLD | STRING | 1 | — | Credit Hold |
| 23 | BKAR_CREDITLMT | NUMERIC | 8 | 2 | Credit Limit |
| 24 | BKAR_CUST_YEAR | STRING | 12 | — | — |
| 25 | BKAR_CUSTCODE | STRING | 10 | — | Customer Code |
| 26 | BKAR_CUSTNAME | STRING | 30 | — | Name |
| 27 | BKAR_DAYS_TOPAY | NUMERIC | 8 | — | Days To Pay |
| 28 | BKAR_DISC_CODE | STRING | 10 | — | Discount Code |
| 29 | BKAR_EMAIL_1 | STRING | 128 | — | — |
| 30 | BKAR_EMAIL_2 | STRING | 128 | — | — |
| 31 | BKAR_EMAIL_3 | STRING | 128 | — | — |
| 32 | BKAR_EMAIL_4 | STRING | 128 | — | — |
| 33 | BKAR_EMAIL_5 | STRING | 128 | — | — |
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
| 47 | BKAR_IS_REP | STRING | 5 | — | — |
| 48 | BKAR_IS_TAXGRP | STRING | 10 | — | Tax Group |
| 49 | BKAR_IS_TAXIN | STRING | 1 | — | Excise Tax-In |
| 50 | BKAR_LASTPMT | DATE | 4 | — | Last Payment Date |
| 51 | BKAR_LASTSALE | DATE | 4 | — | Last Sale Date |
| 52 | BKAR_LEAD_SRC | STRING | 5 | — | Lead Source |
| 53 | BKAR_LEAD_SRC2 | STRING | 5 | — | — |
| 54 | BKAR_MAIL_LIST | STRING | 1 | — | Mail List Y/N |
| 55 | BKAR_NET_LYR | NUMERIC | 8 | 2 | Net Profit Last Year |
| 56 | BKAR_NET_MTD | NUMERIC | 8 | 2 | Net Profit Month To Date |
| 57 | BKAR_NET_PVAR | NUMERIC | 8 | 4 | Net Profit Percent Variance |
| 58 | BKAR_NET_YTD | NUMERIC | 8 | 2 | Net Profit Year To Date |
| 59 | BKAR_NEW_CUST | STRING | 1 | — | New Customer Y/N |
| 60 | BKAR_NOTES_1 | STRING | 80 | — | — |
| 61 | BKAR_NOTES_10 | STRING | 80 | — | — |
| 62 | BKAR_NOTES_2 | STRING | 80 | — | — |
| 63 | BKAR_NOTES_3 | STRING | 80 | — | — |
| 64 | BKAR_NOTES_4 | STRING | 80 | — | — |
| 65 | BKAR_NOTES_5 | STRING | 80 | — | — |
| 66 | BKAR_NOTES_6 | STRING | 80 | — | — |
| 67 | BKAR_NOTES_7 | STRING | 80 | — | — |
| 68 | BKAR_NOTES_8 | STRING | 80 | — | — |
| 69 | BKAR_NOTES_9 | STRING | 80 | — | — |
| 70 | BKAR_NUM_INVCS | NUMERIC | 8 | — | Number Invoices |
| 71 | BKAR_OUT_CREDIT_1 | NUMERIC | 8 | 2 | — |
| 72 | BKAR_OUT_CREDIT_2 | NUMERIC | 8 | 2 | — |
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
| 87 | BKAR_SHP_TOLRNC | STRING | 10 | — | — |
| 88 | BKAR_SHP_WINDOW | STRING | 30 | — | Shipping Window |
| 89 | BKAR_SIC_CODE | STRING | 7 | — | SIC Code |
| 90 | BKAR_SLSP_NUM_1 | INTEGER | 2 | — | — |
| 91 | BKAR_SLSP_NUM_2 | INTEGER | 2 | — | — |
| 92 | BKAR_SORT | STRING | 6 | — | Sort Field |
| 93 | BKAR_START_DATE | DATE | 4 | — | Start Date |
| 94 | BKAR_STATE | STRING | 2 | — | State |
| 95 | BKAR_STATEMENT | STRING | 1 | — | Statement Y/N |
| 96 | BKAR_TAX_LOCAL | STRING | 2 | — | Tax Local |
| 97 | BKAR_TAX_STATE | STRING | 2 | — | Tax State |
| 98 | BKAR_TAX_YN | STRING | 1 | — | Tax Y/N |
| 99 | BKAR_TELEPHONE_1 | STRING | 25 | — | — |
| 100 | BKAR_TELEPHONE_2 | STRING | 25 | — | — |
| 101 | BKAR_TELEPHONE_3 | STRING | 25 | — | — |
| 102 | BKAR_TELEPHONE_4 | STRING | 25 | — | — |
| 103 | BKAR_TELEPHONE_5 | STRING | 25 | — | — |
| 104 | BKAR_TERMS_NUM | INTEGER | 2 | — | Terms Number |
| 105 | BKAR_TERRITORY | STRING | 4 | — | Sales Territory |
| 106 | BKAR_ZIP | STRING | 10 | — | ZIP Code |

## BKAREIVT
**TEMP FILE FOR IMPORT OPEN AR**

Fields: 23

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAR_INVT_AMT | NUMERIC | 8 | 2 | Amount |
| 2 | BKAR_INVT_AMTRM | NUMERIC | 8 | 2 | Amount Remaining |
| 3 | BKAR_INVT_CHKAC | INTEGER | 2 | — | Checking Account |
| 4 | BKAR_INVT_CHKNO | NUMERIC | 8 | — | Check Number |
| 5 | BKAR_INVT_CLOSD | DATE | 4 | — | — |
| 6 | BKAR_INVT_CODE | STRING | 10 | — | Customer Code |
| 7 | BKAR_INVT_DATE | DATE | 4 | — | Transaction Date |
| 8 | BKAR_INVT_DEPNO | NUMERIC | 8 | — | Deposit number |
| 9 | BKAR_INVT_DEPST | STRING | 1 | — | — |
| 10 | BKAR_INVT_DESC | STRING | 25 | — | Description |
| 11 | BKAR_INVT_EXTRA | STRING | 50 | — | Extra |
| 12 | BKAR_INVT_GLDPT | STRING | 4 | — | GL Department |
| 13 | BKAR_INVT_MCCOD | STRING | 3 | — | — |
| 14 | BKAR_INVT_MCRAT | NUMERIC | 8 | 6 | — |
| 15 | BKAR_INVT_NORMP | STRING | 1 | — | — |
| 16 | BKAR_INVT_NUM | NUMERIC | 8 | — | Invoice Number |
| 17 | BKAR_INVT_OPEND | DATE | 4 | — | — |
| 18 | BKAR_INVT_PDATE | DATE | 4 | — | — |
| 19 | BKAR_INVT_SLSP | INTEGER | 2 | — | Salesperson1 |
| 20 | BKAR_INVT_SLSP2 | INTEGER | 2 | — | Salesperson 2 |
| 21 | BKAR_INVT_TERMN | INTEGER | 2 | — | Terms Number |
| 22 | BKAR_INVT_TRXN | NUMERIC | 8 | — | — |
| 23 | BKAR_INVT_TYPE | STRING | 1 | — | Transaction Type |

## BKBMEMTR
**TEMP FILE FOR IMPORT BOM**

Fields: 27

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKBM_C_TYPE | STRING | 10 | — | — |
| 2 | BKBM_COMPONENT | STRING | 15 | — | Component Part Code |
| 3 | BKBM_DATE1 | DATE | 4 | — | — |
| 4 | BKBM_DATE2 | DATE | 4 | — | — |
| 5 | BKBM_EST_LINE | NUMERIC | 8 | — | — |
| 6 | BKBM_EXTRA | STRING | 50 | — | Extra |
| 7 | BKBM_P_TYPE | STRING | 10 | — | — |
| 8 | BKBM_PARENT | STRING | 15 | — | Parent Part Code |
| 9 | BKBM_PROD_DUPOP | STRING | 1 | — | Duplicate Option blank / 1 / 2 |
| 10 | BKBM_PROD_LINE^ | INTEGER | 2 | — | — |
| 11 | BKBM_PROD_OP | STRING | 3 | — | Option ( If  in second position) |
| 12 | BKBM_PROD_OPDSC | STRING | 5 | — | — |
| 13 | BKBM_PROD_OPYN_1 | STRING | 1 | — | — |
| 14 | BKBM_PROD_OPYN_2 | STRING | 1 | — | — |
| 15 | BKBM_PROD_OPYN_3 | STRING | 1 | — | — |
| 16 | BKBM_PROD_OPYN_4 | STRING | 1 | — | — |
| 17 | BKBM_PROD_OPYN_5 | STRING | 1 | — | — |
| 18 | BKBM_PROD_OPYN_6 | STRING | 1 | — | — |
| 19 | BKBM_PROD_PRICE | NUMERIC | 8 | 4 | Option Pricing |
| 20 | BKBM_PROD_RTNUM | INTEGER | 2 | — | Routing  Sequence Number |
| 21 | BKBM_PROD_SCRAP | NUMERIC | 8 | 2 | Scrap Allowance Percent |
| 22 | BKBM_PROD_TYPE | STRING | 1 | — | Part Type |
| 23 | BKBM_PROD_VEND | STRING | 10 | — | Vendor Code |
| 24 | BKBM_QTY_REQD | NUMERIC | 8 | 8 | Quantity Required |
| 25 | BKBM_REFERENCE | STRING | 20 | — | Reference |
| 26 | BKBM_REV | STRING | 5 | — | Revision (not used) |
| 27 | BKBM_UID | STRING | 20 | — | — |

## BKBMERMK
**TEMP FILE FOR IMPORT BOM REMARKS**

Fields: 20

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKBM_RM_COMP | STRING | 15 | — | Component Part Code |
| 2 | BKBM_RM_EXTRA | STRING | 50 | — | — |
| 3 | BKBM_RM_LINE | INTEGER | 2 | — | Line Number |
| 4 | BKBM_RM_PARENT | STRING | 15 | — | Parent Part Code |
| 5 | BKBM_RM_REMARK_1 | STRING | 64 | — | — |
| 6 | BKBM_RM_REMARK_10 | STRING | 64 | — | — |
| 7 | BKBM_RM_REMARK_11 | STRING | 64 | — | — |
| 8 | BKBM_RM_REMARK_12 | STRING | 64 | — | — |
| 9 | BKBM_RM_REMARK_13 | STRING | 64 | — | — |
| 10 | BKBM_RM_REMARK_14 | STRING | 64 | — | — |
| 11 | BKBM_RM_REMARK_15 | STRING | 64 | — | — |
| 12 | BKBM_RM_REMARK_2 | STRING | 64 | — | — |
| 13 | BKBM_RM_REMARK_3 | STRING | 64 | — | — |
| 14 | BKBM_RM_REMARK_4 | STRING | 64 | — | — |
| 15 | BKBM_RM_REMARK_5 | STRING | 64 | — | — |
| 16 | BKBM_RM_REMARK_6 | STRING | 64 | — | — |
| 17 | BKBM_RM_REMARK_7 | STRING | 64 | — | — |
| 18 | BKBM_RM_REMARK_8 | STRING | 64 | — | — |
| 19 | BKBM_RM_REMARK_9 | STRING | 64 | — | — |
| 20 | BKBM_RM_UID | STRING | 20 | — | — |

## BKGLECOA
**DI CHART OF ACCOUNTS**

Fields: 65

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKGL_1YPAST_1 | NUMERIC | 8 | 2 | — |
| 2 | BKGL_1YPAST_10 | NUMERIC | 8 | 2 | — |
| 3 | BKGL_1YPAST_11 | NUMERIC | 8 | 2 | — |
| 4 | BKGL_1YPAST_12 | NUMERIC | 8 | 2 | — |
| 5 | BKGL_1YPAST_13 | NUMERIC | 8 | 2 | — |
| 6 | BKGL_1YPAST_14 | NUMERIC | 8 | 2 | — |
| 7 | BKGL_1YPAST_2 | NUMERIC | 8 | 2 | — |
| 8 | BKGL_1YPAST_3 | NUMERIC | 8 | 2 | — |
| 9 | BKGL_1YPAST_4 | NUMERIC | 8 | 2 | — |
| 10 | BKGL_1YPAST_5 | NUMERIC | 8 | 2 | — |
| 11 | BKGL_1YPAST_6 | NUMERIC | 8 | 2 | — |
| 12 | BKGL_1YPAST_7 | NUMERIC | 8 | 2 | — |
| 13 | BKGL_1YPAST_8 | NUMERIC | 8 | 2 | — |
| 14 | BKGL_1YPAST_9 | NUMERIC | 8 | 2 | — |
| 15 | BKGL_1YPAST_YE | NUMERIC | 8 | 2 | 1 Yr. Past Year End Entry |
| 16 | BKGL_2YPAST_1 | NUMERIC | 8 | 2 | — |
| 17 | BKGL_2YPAST_10 | NUMERIC | 8 | 2 | — |
| 18 | BKGL_2YPAST_11 | NUMERIC | 8 | 2 | — |
| 19 | BKGL_2YPAST_12 | NUMERIC | 8 | 2 | — |
| 20 | BKGL_2YPAST_13 | NUMERIC | 8 | 2 | — |
| 21 | BKGL_2YPAST_14 | NUMERIC | 8 | 2 | — |
| 22 | BKGL_2YPAST_2 | NUMERIC | 8 | 2 | — |
| 23 | BKGL_2YPAST_3 | NUMERIC | 8 | 2 | — |
| 24 | BKGL_2YPAST_4 | NUMERIC | 8 | 2 | — |
| 25 | BKGL_2YPAST_5 | NUMERIC | 8 | 2 | — |
| 26 | BKGL_2YPAST_6 | NUMERIC | 8 | 2 | — |
| 27 | BKGL_2YPAST_7 | NUMERIC | 8 | 2 | — |
| 28 | BKGL_2YPAST_8 | NUMERIC | 8 | 2 | — |
| 29 | BKGL_2YPAST_9 | NUMERIC | 8 | 2 | — |
| 30 | BKGL_2YPAST_YE | NUMERIC | 8 | 2 | 2 Yr. Past year End Entry |
| 31 | BKGL_ACCT | STRING | 10 | — | GL Account Code |
| 32 | BKGL_ACCTD | STRING | 25 | — | Account Description |
| 33 | BKGL_BUDGET_1 | NUMERIC | 8 | 2 | — |
| 34 | BKGL_BUDGET_10 | NUMERIC | 8 | 2 | — |
| 35 | BKGL_BUDGET_11 | NUMERIC | 8 | 2 | — |
| 36 | BKGL_BUDGET_12 | NUMERIC | 8 | 2 | — |
| 37 | BKGL_BUDGET_13 | NUMERIC | 8 | 2 | — |
| 38 | BKGL_BUDGET_14 | NUMERIC | 8 | 2 | — |
| 39 | BKGL_BUDGET_2 | NUMERIC | 8 | 2 | — |
| 40 | BKGL_BUDGET_3 | NUMERIC | 8 | 2 | — |
| 41 | BKGL_BUDGET_4 | NUMERIC | 8 | 2 | — |
| 42 | BKGL_BUDGET_5 | NUMERIC | 8 | 2 | — |
| 43 | BKGL_BUDGET_6 | NUMERIC | 8 | 2 | — |
| 44 | BKGL_BUDGET_7 | NUMERIC | 8 | 2 | — |
| 45 | BKGL_BUDGET_8 | NUMERIC | 8 | 2 | — |
| 46 | BKGL_BUDGET_9 | NUMERIC | 8 | 2 | — |
| 47 | BKGL_CR_DR | STRING | 1 | — | Normal Credit/Debit |
| 48 | BKGL_CURRENT_1 | NUMERIC | 8 | 2 | — |
| 49 | BKGL_CURRENT_10 | NUMERIC | 8 | 2 | — |
| 50 | BKGL_CURRENT_11 | NUMERIC | 8 | 2 | — |
| 51 | BKGL_CURRENT_12 | NUMERIC | 8 | 2 | — |
| 52 | BKGL_CURRENT_13 | NUMERIC | 8 | 2 | — |
| 53 | BKGL_CURRENT_14 | NUMERIC | 8 | 2 | — |
| 54 | BKGL_CURRENT_2 | NUMERIC | 8 | 2 | — |
| 55 | BKGL_CURRENT_3 | NUMERIC | 8 | 2 | — |
| 56 | BKGL_CURRENT_4 | NUMERIC | 8 | 2 | — |
| 57 | BKGL_CURRENT_5 | NUMERIC | 8 | 2 | — |
| 58 | BKGL_CURRENT_6 | NUMERIC | 8 | 2 | — |
| 59 | BKGL_CURRENT_7 | NUMERIC | 8 | 2 | — |
| 60 | BKGL_CURRENT_8 | NUMERIC | 8 | 2 | — |
| 61 | BKGL_CURRENT_9 | NUMERIC | 8 | 2 | — |
| 62 | BKGL_EXTRA | STRING | 50 | — | Extra |
| 63 | BKGL_GLDPT | STRING | 4 | — | GL Department |
| 64 | BKGL_NON_CASH | STRING | 1 | — | Non Cash Y/N |
| 65 | BKGL_TYPE | STRING | 1 | — | Account Type (ALOIE) |

## BKGLETRN
**TEMP FILE FOR IMPORT GL TRANSACTIONS**

Fields: 16

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
| 12 | BKGL_TRN_PART | STRING | 15 | — | — |
| 13 | BKGL_TRN_PERIOD | INTEGER | 2 | — | Period |
| 14 | BKGL_TRN_POST | STRING | 1 | — | Posted flag |
| 15 | BKGL_TRN_TRXN | NUMERIC | 8 | — | Trans Number |
| 16 | BKGL_TRN_TYPE | STRING | 2 | — | Type |

## BKICELOC
**TEMP FILE FOR IMPORT INVENTORY LOCATION**

Fields: 32

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKIC_LOC_ALPHA1 | STRING | 30 | — | — |
| 2 | BKIC_LOC_ALPHA2 | STRING | 30 | — | — |
| 3 | BKIC_LOC_BIN | STRING | 15 | — | — |
| 4 | BKIC_LOC_CODE | STRING | 10 | — | Location Code |
| 5 | BKIC_LOC_DATE1 | DATE | 4 | — | — |
| 6 | BKIC_LOC_DPTA | STRING | 4 | — | GL Department |
| 7 | BKIC_LOC_DPTC | STRING | 4 | — | GL COGS Department |
| 8 | BKIC_LOC_DPTS | STRING | 4 | — | GL Sales Department |
| 9 | BKIC_LOC_DPTSNT | STRING | 4 | — | GL Sales Non Tax Department |
| 10 | BKIC_LOC_DPTWIP | STRING | 4 | — | GL WIP Department |
| 11 | BKIC_LOC_EXTRA | STRING | 50 | — | — |
| 12 | BKIC_LOC_FLAG1 | STRING | 1 | — | — |
| 13 | BKIC_LOC_GLA | STRING | 10 | — | GL Account |
| 14 | BKIC_LOC_GLC | STRING | 10 | — | GL COGS Account |
| 15 | BKIC_LOC_GLS | STRING | 10 | — | GL Sales Account |
| 16 | BKIC_LOC_GLSNT | STRING | 10 | — | GL Sales Non-Tax Account |
| 17 | BKIC_LOC_GLWIP | STRING | 10 | — | GL WIP Account |
| 18 | BKIC_LOC_LCDATE | DATE | 4 | — | — |
| 19 | BKIC_LOC_LOT | STRING | 15 | — | — |
| 20 | BKIC_LOC_NUM1 | NUMERIC | 8 | — | — |
| 21 | BKIC_LOC_NUM2 | NUMERIC | 8 | — | — |
| 22 | BKIC_LOC_PROD | STRING | 15 | — | Part Number |
| 23 | BKIC_LOC_SER | STRING | 25 | — | — |
| 24 | BKIC_LOC_UALLOC | NUMERIC | 8 | 2 | Units Allocated |
| 25 | BKIC_LOC_UBO | NUMERIC | 8 | 2 | Units on Back Order |
| 26 | BKIC_LOC_UIQC | NUMERIC | 8 | 2 | Units in QC |
| 27 | BKIC_LOC_UOH | NUMERIC | 8 | 2 | Units on Hand |
| 28 | BKIC_LOC_UOO | NUMERIC | 8 | 2 | Units on PO |
| 29 | BKIC_LOC_UOSO | NUMERIC | 8 | 2 | Units on Sales Order |
| 30 | BKIC_LOC_UOWO | NUMERIC | 8 | 2 | Units on Work Order |
| 31 | BKIC_LOC_UWIP | NUMERIC | 8 | 2 | Units in WIP |
| 32 | BKIC_LOC_WHCTRL | STRING | 1 | — | — |

## BKICEMTR
**TEMP FILE FOR IMPORT INVENTORY**

Fields: 64

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
| 32 | BKIC_PROD_LONGP | STRING | 25 | — | — |
| 33 | BKIC_PROD_LORD | DATE | 4 | — | Last Order Date |
| 34 | BKIC_PROD_LRCPT | DATE | 4 | — | Last Receipt Date |
| 35 | BKIC_PROD_LSALE | DATE | 4 | — | Last Sale Date |
| 36 | BKIC_PROD_LSTC | NUMERIC | 8 | 4 | Last Cost |
| 37 | BKIC_PROD_MANUF | STRING | 20 | — | — |
| 38 | BKIC_PROD_NGLYR | NUMERIC | 8 | 4 | — |
| 39 | BKIC_PROD_NGMTD | NUMERIC | 8 | 4 | — |
| 40 | BKIC_PROD_NGVAR | NUMERIC | 8 | 4 | — |
| 41 | BKIC_PROD_NGYTD | NUMERIC | 8 | 4 | — |
| 42 | BKIC_PROD_NOTE | STRING | 30 | — | Description Line 2 |
| 43 | BKIC_PROD_NSLYR | NUMERIC | 8 | 2 | Net Sales Last Year |
| 44 | BKIC_PROD_NSMTD | NUMERIC | 8 | 2 | Net Sales Month-To-Date |
| 45 | BKIC_PROD_NSVAR | NUMERIC | 8 | 4 | Net Sales Variance |
| 46 | BKIC_PROD_NSYTD | NUMERIC | 8 | 2 | Net Sales Year-To-Date |
| 47 | BKIC_PROD_PMAT | INTEGER | 2 | — | — |
| 48 | BKIC_PROD_PRICE | NUMERIC | 8 | 4 | Base Price |
| 49 | BKIC_PROD_RAMT | NUMERIC | 8 | — | Reorder Amount |
| 50 | BKIC_PROD_RLVL | NUMERIC | 8 | — | Reorder Level |
| 51 | BKIC_PROD_TAXIN | STRING | 1 | — | Tax In Y/N |
| 52 | BKIC_PROD_TO | NUMERIC | 8 | 4 | — |
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
**TEMP FILE FOR IMPORT ROUTINGS**

Fields: 62

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTRO_CLASS | STRING | 15 | — | not used |
| 2 | MTRO_CODE | STRING | 15 | — | Part Code |
| 3 | MTRO_DEF_TIME | TIME | 4 | — | — |
| 4 | MTRO_DESC | STRING | 30 | — | Description |
| 5 | MTRO_EST_LINE | NUMERIC | 8 | — | — |
| 6 | MTRO_EST_TAG | STRING | 10 | — | — |
| 7 | MTRO_EXTRA | STRING | 150 | — | Extra |
| 8 | MTRO_FOVHD | NUMERIC | 8 | 4 | Fixed Overhead Rate |
| 9 | MTRO_INSTR_1 | STRING | 60 | — | — |
| 10 | MTRO_INSTR_10 | STRING | 60 | — | — |
| 11 | MTRO_INSTR_11 | STRING | 60 | — | — |
| 12 | MTRO_INSTR_12 | STRING | 60 | — | — |
| 13 | MTRO_INSTR_13 | STRING | 60 | — | — |
| 14 | MTRO_INSTR_14 | STRING | 60 | — | — |
| 15 | MTRO_INSTR_15 | STRING | 60 | — | — |
| 16 | MTRO_INSTR_2 | STRING | 60 | — | — |
| 17 | MTRO_INSTR_3 | STRING | 60 | — | — |
| 18 | MTRO_INSTR_4 | STRING | 60 | — | — |
| 19 | MTRO_INSTR_5 | STRING | 60 | — | — |
| 20 | MTRO_INSTR_6 | STRING | 60 | — | — |
| 21 | MTRO_INSTR_7 | STRING | 60 | — | — |
| 22 | MTRO_INSTR_8 | STRING | 60 | — | — |
| 23 | MTRO_INSTR_9 | STRING | 60 | — | — |
| 24 | MTRO_LABOR | NUMERIC | 8 | 4 | Labor Rate |
| 25 | MTRO_LEAD | INTEGER | 2 | — | Lead Time |
| 26 | MTRO_LONGTIME | NUMERIC | 8 | 7 | Longtime - Decimal Hrs. |
| 27 | MTRO_LOTSIZE | NUMERIC | 8 | — | Lot Size |
| 28 | MTRO_MACHINE | NUMERIC | 8 | 4 | Machine Rate |
| 29 | MTRO_MD_PROC_HR | STRING | 1 | — | — |
| 30 | MTRO_MIN_CHG | NUMERIC | 8 | 2 | Minimum Charge (Outside Process) |
| 31 | MTRO_MISC_ACOST | NUMERIC | 8 | 2 | — |
| 32 | MTRO_NEGOVLP | NUMERIC | 8 | 2 | Negative Overlap |
| 33 | MTRO_NUM | INTEGER | 2 | — | Routing Number |
| 34 | MTRO_NUM_PERSON | NUMERIC | 8 | 2 | Number of Persons |
| 35 | MTRO_NUM_PROCES | INTEGER | 2 | — | Number of Processes |
| 36 | MTRO_OP_TEMP_NO | INTEGER | 2 | — | Template Number |
| 37 | MTRO_OPER | INTEGER | 2 | — | Operation |
| 38 | MTRO_OPERDESC | STRING | 30 | — | Operation Desciption |
| 39 | MTRO_OVERLAP | INTEGER | 2 | — | Overlap Hrs. |
| 40 | MTRO_PARTSHR | NUMERIC | 8 | 2 | Parts/Hour |
| 41 | MTRO_PIECE_RATE | NUMERIC | 8 | 2 | Piece Rate |
| 42 | MTRO_PRINT | STRING | 1 | — | not used |
| 43 | MTRO_PROC_PERHR | NUMERIC | 8 | 2 | Processes Per Hour |
| 44 | MTRO_R_TYPE | STRING | 10 | — | — |
| 45 | MTRO_SETUP | NUMERIC | 8 | 4 | Setup Rate |
| 46 | MTRO_SETUPHRS | TIME | 4 | — | Setup Hours |
| 47 | MTRO_STD_TIME | STRING | 1 | — | Standard Time Y/N |
| 48 | MTRO_TIME_PERPR | TIME | 4 | — | — |
| 49 | MTRO_TIMEPART | TIME | 4 | — | Time/Part |
| 50 | MTRO_TMACHDESC | STRING | 30 | — | Machine Description |
| 51 | MTRO_TMACHINE | STRING | 4 | — | Machine Code |
| 52 | MTRO_TOOL | STRING | 15 | — | Tool Code |
| 53 | MTRO_TOOLDESC | STRING | 30 | — | Tool Description |
| 54 | MTRO_TYPE | STRING | 1 | — | Type |
| 55 | MTRO_VENDCODE | STRING | 10 | — | Vendor Code |
| 56 | MTRO_VENDCOST | NUMERIC | 8 | 6 | Vendor Cost |
| 57 | MTRO_VENDNAME | STRING | 25 | — | Vendor Name |
| 58 | MTRO_VOVHD | NUMERIC | 8 | 4 | Variable Overhead Rate |
| 59 | MTRO_WC | STRING | 12 | — | Work Center |
| 60 | MTRO_WCDESC | STRING | 30 | — | Work Center Description |
| 61 | MTWO_MISC_COST | NUMERIC | 8 | 2 | Misc. Cost |
| 62 | MTWO_MISC_DESC | STRING | 30 | — | Misc. Description |

## MTICEMTR
**TEMP INVENTORY IMPORT FILE**

Fields: 109

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
| 20 | MTIC_PROD_FRT^ | NUMERIC | 8 | 2 | — |
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
| 34 | MTIC_PROD_OPTPR | INTEGER | 2 | — | — |
| 35 | MTIC_PROD_PCONV | NUMERIC | 8 | 5 | PO Conversion Multiplier |
| 36 | MTIC_PROD_PUM | STRING | 3 | — | Purchase Unit Measure |
| 37 | MTIC_PROD_RCOST_1 | NUMERIC | 8 | 6 | — |
| 38 | MTIC_PROD_RCOST_10 | NUMERIC | 8 | 6 | — |
| 39 | MTIC_PROD_RCOST_11 | NUMERIC | 8 | 6 | — |
| 40 | MTIC_PROD_RCOST_12 | NUMERIC | 8 | 6 | — |
| 41 | MTIC_PROD_RCOST_13 | NUMERIC | 8 | 6 | — |
| 42 | MTIC_PROD_RCOST_14 | NUMERIC | 8 | 6 | — |
| 43 | MTIC_PROD_RCOST_15 | NUMERIC | 8 | 6 | — |
| 44 | MTIC_PROD_RCOST_2 | NUMERIC | 8 | 6 | — |
| 45 | MTIC_PROD_RCOST_3 | NUMERIC | 8 | 6 | — |
| 46 | MTIC_PROD_RCOST_4 | NUMERIC | 8 | 6 | — |
| 47 | MTIC_PROD_RCOST_5 | NUMERIC | 8 | 6 | — |
| 48 | MTIC_PROD_RCOST_6 | NUMERIC | 8 | 6 | — |
| 49 | MTIC_PROD_RCOST_7 | NUMERIC | 8 | 6 | — |
| 50 | MTIC_PROD_RCOST_8 | NUMERIC | 8 | 6 | — |
| 51 | MTIC_PROD_RCOST_9 | NUMERIC | 8 | 6 | — |
| 52 | MTIC_PROD_REV | STRING | 5 | — | Revision Level |
| 53 | MTIC_PROD_SER | STRING | 1 | — | Serial Control Y/N |
| 54 | MTIC_PROD_SPECS_1 | STRING | 30 | — | — |
| 55 | MTIC_PROD_SPECS_10 | STRING | 30 | — | — |
| 56 | MTIC_PROD_SPECS_11 | STRING | 30 | — | — |
| 57 | MTIC_PROD_SPECS_12 | STRING | 30 | — | — |
| 58 | MTIC_PROD_SPECS_2 | STRING | 30 | — | — |
| 59 | MTIC_PROD_SPECS_3 | STRING | 30 | — | — |
| 60 | MTIC_PROD_SPECS_4 | STRING | 30 | — | — |
| 61 | MTIC_PROD_SPECS_5 | STRING | 30 | — | — |
| 62 | MTIC_PROD_SPECS_6 | STRING | 30 | — | — |
| 63 | MTIC_PROD_SPECS_7 | STRING | 30 | — | — |
| 64 | MTIC_PROD_SPECS_8 | STRING | 30 | — | — |
| 65 | MTIC_PROD_SPECS_9 | STRING | 30 | — | — |
| 66 | MTIC_PROD_STDC | NUMERIC | 8 | 6 | Not Used |
| 67 | MTIC_PROD_STDPK | NUMERIC | 8 | — | Standard Pack Quantity |
| 68 | MTIC_PROD_SUBST_1 | STRING | 25 | — | — |
| 69 | MTIC_PROD_SUBST_2 | STRING | 25 | — | — |
| 70 | MTIC_PROD_SUBST_3 | STRING | 25 | — | — |
| 71 | MTIC_PROD_SUBST_4 | STRING | 25 | — | — |
| 72 | MTIC_PROD_SUBST_5 | STRING | 25 | — | — |
| 73 | MTIC_PROD_SUM | STRING | 3 | — | Sales Unit Measure |
| 74 | MTIC_PROD_TYPE | STRING | 1 | — | Product TYPE (RFAMKLTBO) |
| 75 | MTIC_PROD_UIQC | NUMERIC | 8 | 2 | Units in QC |
| 76 | MTIC_PROD_UIWIP | NUMERIC | 8 | 2 | Units in WIP |
| 77 | MTIC_PROD_UOA | NUMERIC | 8 | 2 | Units On Allocations |
| 78 | MTIC_PROD_UOWO | NUMERIC | 8 | 2 | Units On Work Order |
| 79 | MTIC_PROD_VEND_1 | STRING | 10 | — | — |
| 80 | MTIC_PROD_VEND_10 | STRING | 10 | — | — |
| 81 | MTIC_PROD_VEND_2 | STRING | 10 | — | — |
| 82 | MTIC_PROD_VEND_3 | STRING | 10 | — | — |
| 83 | MTIC_PROD_VEND_4 | STRING | 10 | — | — |
| 84 | MTIC_PROD_VEND_5 | STRING | 10 | — | — |
| 85 | MTIC_PROD_VEND_6 | STRING | 10 | — | — |
| 86 | MTIC_PROD_VEND_7 | STRING | 10 | — | — |
| 87 | MTIC_PROD_VEND_8 | STRING | 10 | — | — |
| 88 | MTIC_PROD_VEND_9 | STRING | 10 | — | — |
| 89 | MTIC_PROD_VNAM_1 | STRING | 30 | — | — |
| 90 | MTIC_PROD_VNAM_10 | STRING | 30 | — | — |
| 91 | MTIC_PROD_VNAM_2 | STRING | 30 | — | — |
| 92 | MTIC_PROD_VNAM_3 | STRING | 30 | — | — |
| 93 | MTIC_PROD_VNAM_4 | STRING | 30 | — | — |
| 94 | MTIC_PROD_VNAM_5 | STRING | 30 | — | — |
| 95 | MTIC_PROD_VNAM_6 | STRING | 30 | — | — |
| 96 | MTIC_PROD_VNAM_7 | STRING | 30 | — | — |
| 97 | MTIC_PROD_VNAM_8 | STRING | 30 | — | — |
| 98 | MTIC_PROD_VNAM_9 | STRING | 30 | — | — |
| 99 | MTIC_PROD_VPC_1 | STRING | 20 | — | — |
| 100 | MTIC_PROD_VPC_2 | STRING | 20 | — | — |
| 101 | MTIC_PROD_VPC_3 | STRING | 20 | — | — |
| 102 | MTIC_PROD_VPC_4 | STRING | 20 | — | — |
| 103 | MTIC_PROD_VPC_5 | STRING | 20 | — | — |
| 104 | MTIC_PROD_VPC_6 | STRING | 20 | — | — |
| 105 | MTIC_PROD_VPC_7 | STRING | 20 | — | — |
| 106 | MTIC_PROD_VPC_8 | STRING | 20 | — | — |
| 107 | MTIC_PROD_VPC_9 | STRING | 20 | — | — |
| 108 | MTIC_PROD_WIPDP | STRING | 4 | — | GL WIP Department |
| 109 | MTIC_PROD_WT | NUMERIC | 8 | 6 | Weight |

## WOELABOR
**TEMP FILE FOR LABOR IMPORT**

Fields: 45

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTWOLA_ASSY | STRING | 15 | — | — |
| 2 | MTWOLA_ASSYDESC | STRING | 30 | — | — |
| 3 | MTWOLA_AUDIT | STRING | 35 | — | — |
| 4 | MTWOLA_COMPLETE | STRING | 1 | — | — |
| 5 | MTWOLA_DATE | DATE | 4 | — | — |
| 6 | MTWOLA_DATE2 | DATE | 4 | — | — |
| 7 | MTWOLA_DEDUCT | TIME | 4 | — | — |
| 8 | MTWOLA_EMP | INTEGER | 2 | — | — |
| 9 | MTWOLA_EMP2 | INTEGER | 2 | — | — |
| 10 | MTWOLA_EXTRA | STRING | 50 | — | — |
| 11 | MTWOLA_FOHCOST | NUMERIC | 8 | 2 | — |
| 12 | MTWOLA_LABCOST | NUMERIC | 8 | 2 | — |
| 13 | MTWOLA_LABRATE | NUMERIC | 8 | 4 | — |
| 14 | MTWOLA_MACH | STRING | 4 | — | — |
| 15 | MTWOLA_MACHCOST | NUMERIC | 8 | 2 | — |
| 16 | MTWOLA_MACHDATE | DATE | 4 | — | — |
| 17 | MTWOLA_MISC | NUMERIC | 8 | 6 | — |
| 18 | MTWOLA_MISCDESC | STRING | 30 | — | — |
| 19 | MTWOLA_NOJOBS | INTEGER | 2 | — | — |
| 20 | MTWOLA_OPER | INTEGER | 2 | — | — |
| 21 | MTWOLA_OTEAM | INTEGER | 2 | — | — |
| 22 | MTWOLA_PARTS | NUMERIC | 8 | 2 | — |
| 23 | MTWOLA_POSTED | STRING | 1 | — | — |
| 24 | MTWOLA_QCCODE | STRING | 2 | — | — |
| 25 | MTWOLA_QCDESC | STRING | 30 | — | — |
| 26 | MTWOLA_REGOVER | STRING | 1 | — | — |
| 27 | MTWOLA_REWORK | STRING | 1 | — | — |
| 28 | MTWOLA_RUNHRS | NUMERIC | 8 | 2 | — |
| 29 | MTWOLA_SCDESC | STRING | 30 | — | — |
| 30 | MTWOLA_SCRAPCD | STRING | 2 | — | — |
| 31 | MTWOLA_SCRAPPED | NUMERIC | 8 | 2 | — |
| 32 | MTWOLA_SETCOST | NUMERIC | 8 | 2 | — |
| 33 | MTWOLA_SETUPHRS | NUMERIC | 8 | 2 | — |
| 34 | MTWOLA_SHIFT | INTEGER | 2 | — | — |
| 35 | MTWOLA_START | TIME | 4 | — | — |
| 36 | MTWOLA_STOP | TIME | 4 | — | — |
| 37 | MTWOLA_TEAM | INTEGER | 2 | — | — |
| 38 | MTWOLA_TOOL | STRING | 15 | — | — |
| 39 | MTWOLA_TOOLDATE | DATE | 4 | — | — |
| 40 | MTWOLA_TRXN | INTEGER | 2 | — | — |
| 41 | MTWOLA_VOHCOST | NUMERIC | 8 | 2 | — |
| 42 | MTWOLA_WC | STRING | 12 | — | — |
| 43 | MTWOLA_WCDATE | DATE | 4 | — | — |
| 44 | MTWOLA_WOPRE | NUMERIC | 8 | — | — |
| 45 | MTWOLA_WOSUF | INTEGER | 2 | — | — |

## WOEMAT
**DI MATERIAL ISSUES**

Fields: 17

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTWO_PRODCODE | STRING | 15 | — | — |
| 2 | WOMAT_COST | NUMERIC | 8 | 2 | — |
| 3 | WOMAT_DATE | DATE | 4 | — | — |
| 4 | WOMAT_EXTRA | STRING | 50 | — | — |
| 5 | WOMAT_KIT | STRING | 1 | — | — |
| 6 | WOMAT_LOT | STRING | 15 | — | — |
| 7 | WOMAT_PCODE | STRING | 15 | — | — |
| 8 | WOMAT_PDESC | STRING | 30 | — | — |
| 9 | WOMAT_PRODDESC | STRING | 30 | — | — |
| 10 | WOMAT_QTYISSUED | NUMERIC | 8 | 4 | — |
| 11 | WOMAT_QTYSCRAP | NUMERIC | 8 | 2 | — |
| 12 | WOMAT_REF | STRING | 15 | — | — |
| 13 | WOMAT_SCDESC | STRING | 30 | — | — |
| 14 | WOMAT_SCRAPCD | STRING | 2 | — | — |
| 15 | WOMAT_SERIAL | STRING | 25 | — | — |
| 16 | WOMAT_WOPRE | NUMERIC | 8 | — | — |
| 17 | WOMAT_WOSUF | INTEGER | 2 | — | — |

## WOERECV
**DI WO RECEIPTS**

Fields: 11

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTWOR_ASSY | STRING | 15 | — | — |
| 2 | MTWOR_AVGC | NUMERIC | 8 | 4 | — |
| 3 | MTWOR_DATE | DATE | 4 | — | — |
| 4 | MTWOR_DESC | STRING | 30 | — | — |
| 5 | MTWOR_LOT | STRING | 15 | — | — |
| 6 | MTWOR_QTY | NUMERIC | 8 | 2 | — |
| 7 | MTWOR_REF | STRING | 15 | — | — |
| 8 | MTWOR_SERIAL | STRING | 25 | — | — |
| 9 | MTWOR_USESTD | STRING | 1 | — | — |
| 10 | MTWOR_WOPRE | NUMERIC | 8 | — | — |
| 11 | MTWOR_WOSUF | INTEGER | 2 | — | — |
