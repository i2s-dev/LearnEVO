# AR — Accounts Receivable: Field Reference

Status: verified-schema

Source: `Evo-DBA_File_Fields 052421.xlsx`, sheet "Fields".
Field descriptions where provided by source; otherwise name-inferred.

---

## BKARCHKF
**CUSTOMER PAYMENT HISTORY**

Fields: 12

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAP_CHK_AMTPD | NUMERIC | 8 | 2 | Amount Payed |
| 2 | BKAP_CHK_CHKACT | INTEGER | 2 | — | Bank Account |
| 3 | BKAP_CHK_CHKDTE | DATE | 4 | — | Check Date |
| 4 | BKAP_CHK_DESC | STRING | 25 | — | Description |
| 5 | BKAP_CHK_DISC | NUMERIC | 8 | 2 | Discount |
| 6 | BKAP_CHK_INVAMT | NUMERIC | 8 | 2 | Invoice Amount |
| 7 | BKAP_CHK_INVDTE | DATE | 4 | — | Invoice Date |
| 8 | BKAP_CHK_INVNUM | STRING | 10 | — | Invoice/Voucer Number |
| 9 | BKAP_CHK_ISCUR | STRING | 3 | — | Currency |
| 10 | BKAP_CHK_NUM | NUMERIC | 8 | — | Check Number |
| 11 | BKAP_CHK_TYPE | STRING | 1 | — | Type |
| 12 | BKAP_CHK_VNDCOD | STRING | 10 | — | Vendor Code |

## BKARCUST
**CUSTOMER MASTER**

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

## BKARDEP
**CUSTOMER DEPOSITS**

Fields: 6

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAR_DEP_CUST | STRING | 10 | — | Customer Code |
| 2 | BKAR_DEP_DATE | DATE | 4 | — | Deposit Date |
| 3 | BKAR_DEP_DEPNO | NUMERIC | 8 | — | Deposit Number |
| 4 | BKAR_DEP_EXTRA | STRING | 50 | — | — |
| 5 | BKAR_DEP_SO | NUMERIC | 8 | — | SO Number |
| 6 | BKAR_DEP_SR | STRING | 1 | — | — |

## BKARDESC
**CUSTOMER WEBSITE & DBA CUSTOMER & SO NOTES**

Fields: 5

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BK_DESC_CODE | STRING | 15 | — | not used |
| 2 | BK_DESC_DESC | STRING | 25 | — | not used |
| 3 | BK_DESC_LINE | INTEGER | 2 | — | Notes line number |
| 4 | BK_DESC_NOTES | STRING | 70 | — | Notes - text |
| 5 | BK_DESC_NUM | NUMERIC | 8 | — | PO Number |

## BKARHDSC
**DBA INVOICE NOTES**

Fields: 5

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BK_DESC_CODE | STRING | 15 | — | not used |
| 2 | BK_DESC_DESC | STRING | 25 | — | not used |
| 3 | BK_DESC_LINE | INTEGER | 2 | — | Notes line number |
| 4 | BK_DESC_NOTES | STRING | 70 | — | Notes - text |
| 5 | BK_DESC_NUM | NUMERIC | 8 | — | PO Number |

## BKARHTAX
**SALES TAX**

Fields: 5

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAR_TAX_AMOUNT | NUMERIC | 8 | 2 | Amount |
| 2 | BKAR_TAX_CODE | STRING | 10 | — | Tax Group Code |
| 3 | BKAR_TAX_ID | STRING | 15 | — | Tax ID |
| 4 | BKAR_TAX_INVNO | NUMERIC | 8 | — | Invoice Number |
| 5 | BKAR_TAX_PID | STRING | 1 | — | Y/N |

## BKARINVT
**AR AGING INVOICE**

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

## BKARINVV
**AR VOUCHER**

Fields: 77

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAR_INVV_ARDPT | STRING | 4 | — | — |
| 2 | BKAR_INVV_CHK | INTEGER | 2 | — | Manual Check Number |
| 3 | BKAR_INVV_CODE | STRING | 10 | — | Customer Code |
| 4 | BKAR_INVV_COGS | NUMERIC | 8 | 2 | COGS |
| 5 | BKAR_INVV_COMPR_1 | NUMERIC | 8 | 4 | — |
| 6 | BKAR_INVV_COMPR_2 | NUMERIC | 8 | 4 | — |
| 7 | BKAR_INVV_COOP | NUMERIC | 8 | 2 | Coop |
| 8 | BKAR_INVV_DAMT_1 | NUMERIC | 8 | 2 | — |
| 9 | BKAR_INVV_DAMT_10 | NUMERIC | 8 | 2 | — |
| 10 | BKAR_INVV_DAMT_2 | NUMERIC | 8 | 2 | — |
| 11 | BKAR_INVV_DAMT_3 | NUMERIC | 8 | 2 | — |
| 12 | BKAR_INVV_DAMT_4 | NUMERIC | 8 | 2 | — |
| 13 | BKAR_INVV_DAMT_5 | NUMERIC | 8 | 2 | — |
| 14 | BKAR_INVV_DAMT_6 | NUMERIC | 8 | 2 | — |
| 15 | BKAR_INVV_DAMT_7 | NUMERIC | 8 | 2 | — |
| 16 | BKAR_INVV_DAMT_8 | NUMERIC | 8 | 2 | — |
| 17 | BKAR_INVV_DAMT_9 | NUMERIC | 8 | 2 | — |
| 18 | BKAR_INVV_DATE | DATE | 4 | — | Date |
| 19 | BKAR_INVV_DC_1 | STRING | 1 | — | — |
| 20 | BKAR_INVV_DC_10 | STRING | 1 | — | — |
| 21 | BKAR_INVV_DC_2 | STRING | 1 | — | — |
| 22 | BKAR_INVV_DC_3 | STRING | 1 | — | — |
| 23 | BKAR_INVV_DC_4 | STRING | 1 | — | — |
| 24 | BKAR_INVV_DC_5 | STRING | 1 | — | — |
| 25 | BKAR_INVV_DC_6 | STRING | 1 | — | — |
| 26 | BKAR_INVV_DC_7 | STRING | 1 | — | — |
| 27 | BKAR_INVV_DC_8 | STRING | 1 | — | — |
| 28 | BKAR_INVV_DC_9 | STRING | 1 | — | — |
| 29 | BKAR_INVV_DESC | STRING | 24 | — | Description |
| 30 | BKAR_INVV_EXTRA | STRING | 50 | — | Extra |
| 31 | BKAR_INVV_FLAG_1 | STRING | 1 | — | — |
| 32 | BKAR_INVV_FLAG_2 | STRING | 1 | — | — |
| 33 | BKAR_INVV_FLAG_3 | STRING | 1 | — | — |
| 34 | BKAR_INVV_FLAG_4 | STRING | 1 | — | — |
| 35 | BKAR_INVV_FLAG_5 | STRING | 1 | — | — |
| 36 | BKAR_INVV_FRGHT | NUMERIC | 8 | 2 | Freight |
| 37 | BKAR_INVV_GLACT_1 | STRING | 10 | — | — |
| 38 | BKAR_INVV_GLACT_10 | STRING | 10 | — | — |
| 39 | BKAR_INVV_GLACT_2 | STRING | 10 | — | — |
| 40 | BKAR_INVV_GLACT_3 | STRING | 10 | — | — |
| 41 | BKAR_INVV_GLACT_4 | STRING | 10 | — | — |
| 42 | BKAR_INVV_GLACT_5 | STRING | 10 | — | — |
| 43 | BKAR_INVV_GLACT_6 | STRING | 10 | — | — |
| 44 | BKAR_INVV_GLACT_7 | STRING | 10 | — | — |
| 45 | BKAR_INVV_GLACT_8 | STRING | 10 | — | — |
| 46 | BKAR_INVV_GLACT_9 | STRING | 10 | — | — |
| 47 | BKAR_INVV_GLD_1 | STRING | 25 | — | — |
| 48 | BKAR_INVV_GLD_10 | STRING | 25 | — | — |
| 49 | BKAR_INVV_GLD_2 | STRING | 25 | — | — |
| 50 | BKAR_INVV_GLD_3 | STRING | 25 | — | — |
| 51 | BKAR_INVV_GLD_4 | STRING | 25 | — | — |
| 52 | BKAR_INVV_GLD_5 | STRING | 25 | — | — |
| 53 | BKAR_INVV_GLD_6 | STRING | 25 | — | — |
| 54 | BKAR_INVV_GLD_7 | STRING | 25 | — | — |
| 55 | BKAR_INVV_GLD_8 | STRING | 25 | — | — |
| 56 | BKAR_INVV_GLD_9 | STRING | 25 | — | — |
| 57 | BKAR_INVV_GLDPT_1 | STRING | 4 | — | — |
| 58 | BKAR_INVV_GLDPT_10 | STRING | 4 | — | — |
| 59 | BKAR_INVV_GLDPT_2 | STRING | 4 | — | — |
| 60 | BKAR_INVV_GLDPT_3 | STRING | 4 | — | — |
| 61 | BKAR_INVV_GLDPT_4 | STRING | 4 | — | — |
| 62 | BKAR_INVV_GLDPT_5 | STRING | 4 | — | — |
| 63 | BKAR_INVV_GLDPT_6 | STRING | 4 | — | — |
| 64 | BKAR_INVV_GLDPT_7 | STRING | 4 | — | — |
| 65 | BKAR_INVV_GLDPT_8 | STRING | 4 | — | — |
| 66 | BKAR_INVV_GLDPT_9 | STRING | 4 | — | — |
| 67 | BKAR_INVV_ISCUR | STRING | 3 | — | Currency |
| 68 | BKAR_INVV_NUM | STRING | 6 | — | Voucher Number |
| 69 | BKAR_INVV_SLSP_1 | INTEGER | 2 | — | — |
| 70 | BKAR_INVV_SLSP_2 | INTEGER | 2 | — | — |
| 71 | BKAR_INVV_TAMT | NUMERIC | 8 | 2 | Amount |
| 72 | BKAR_INVV_TAX | NUMERIC | 8 | 2 | Tax |
| 73 | BKAR_INVV_TDC | STRING | 1 | — | Debit/Credit D/C |
| 74 | BKAR_INVV_TERMD | STRING | 10 | — | Terms Description |
| 75 | BKAR_INVV_TERMN | INTEGER | 2 | — | Terms Number |
| 76 | BKAR_INVV_TYPED | STRING | 10 | — | Type Description |
| 77 | BKAR_INVV_TYPEN | INTEGER | 2 | — | Type Number |

## BKARSHIP
**SHIP TO CUSTOMER MASTER (NOT USED)**

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

## BKART
**AGING TRANSACTION DETAIL**

Fields: 12

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKART_AMOUNT | NUMERIC | 8 | 2 | Amount |
| 2 | BKART_CHECK | NUMERIC | 8 | — | Check Number |
| 3 | BKART_CNTR | INTEGER | 2 | — | Transaction Counter - tied to Trans. Num. |
| 4 | BKART_CUST | STRING | 10 | — | Customer Code |
| 5 | BKART_DISC | NUMERIC | 8 | 2 | Discount |
| 6 | BKART_ENTDATE | DATE | 4 | — | Date Entered |
| 7 | BKART_INVC | NUMERIC | 8 | — | Not used |
| 8 | BKART_NOTE | STRING | 1 | — | Note Y or Blank |
| 9 | BKART_POSTDATE | DATE | 4 | — | Post Date |
| 10 | BKART_TRXN | NUMERIC | 8 | — | Transaction Number |
| 11 | BKART_TRXNLINK | NUMERIC | 8 | — | Transaction Num - Link to BKARINVT |
| 12 | BKART_TYPE | STRING | 1 | — | Transaction Type O/P/A |

## BKARTNOT
**AGING TRANSACTION NOTES**

Fields: 3

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKART_NOT_CNTR | INTEGER | 2 | — | Line Counter |
| 2 | BKART_NOT_DESC | STRING | 30 | — | Descriptipn |
| 3 | BKART_NOT_TRXN | NUMERIC | 8 | — | Transaction Number |

## BKCMDUN
**DUN LETTER HEADER**

Fields: 36

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKCM_DUN_AGE_1 | INTEGER | 2 | — | — |
| 2 | BKCM_DUN_AGE_10 | INTEGER | 2 | — | — |
| 3 | BKCM_DUN_AGE_2 | INTEGER | 2 | — | — |
| 4 | BKCM_DUN_AGE_3 | INTEGER | 2 | — | — |
| 5 | BKCM_DUN_AGE_4 | INTEGER | 2 | — | — |
| 6 | BKCM_DUN_AGE_5 | INTEGER | 2 | — | — |
| 7 | BKCM_DUN_AGE_6 | INTEGER | 2 | — | — |
| 8 | BKCM_DUN_AGE_7 | INTEGER | 2 | — | — |
| 9 | BKCM_DUN_AGE_8 | INTEGER | 2 | — | — |
| 10 | BKCM_DUN_AGE_9 | INTEGER | 2 | — | — |
| 11 | BKCM_DUN_CNUM | INTEGER | 2 | — | — |
| 12 | BKCM_DUN_DESC_1 | STRING | 30 | — | — |
| 13 | BKCM_DUN_DESC_10 | STRING | 30 | — | — |
| 14 | BKCM_DUN_DESC_2 | STRING | 30 | — | — |
| 15 | BKCM_DUN_DESC_3 | STRING | 30 | — | — |
| 16 | BKCM_DUN_DESC_4 | STRING | 30 | — | — |
| 17 | BKCM_DUN_DESC_5 | STRING | 30 | — | — |
| 18 | BKCM_DUN_DESC_6 | STRING | 30 | — | — |
| 19 | BKCM_DUN_DESC_7 | STRING | 30 | — | — |
| 20 | BKCM_DUN_DESC_8 | STRING | 30 | — | — |
| 21 | BKCM_DUN_DESC_9 | STRING | 30 | — | — |
| 22 | BKCM_DUN_DORL | STRING | 1 | — | — |
| 23 | BKCM_DUN_FORM_1 | STRING | 15 | — | — |
| 24 | BKCM_DUN_FORM_10 | STRING | 15 | — | — |
| 25 | BKCM_DUN_FORM_2 | STRING | 15 | — | — |
| 26 | BKCM_DUN_FORM_3 | STRING | 15 | — | — |
| 27 | BKCM_DUN_FORM_4 | STRING | 15 | — | — |
| 28 | BKCM_DUN_FORM_5 | STRING | 15 | — | — |
| 29 | BKCM_DUN_FORM_6 | STRING | 15 | — | — |
| 30 | BKCM_DUN_FORM_7 | STRING | 15 | — | — |
| 31 | BKCM_DUN_FORM_8 | STRING | 15 | — | — |
| 32 | BKCM_DUN_FORM_9 | STRING | 15 | — | — |
| 33 | BKCM_DUN_NUMUP | INTEGER | 2 | — | — |
| 34 | BKCM_DUN_PCONT | STRING | 1 | — | — |
| 35 | BKCM_DUN_REP | STRING | 5 | — | Rep Code |
| 36 | BKCM_DUN_SORT | STRING | 1 | — | — |

## BKCMDUNH
**DUN LETTER HISTORY**

Fields: 6

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKCM_DUNH_ACCT | STRING | 10 | — | Account Code |
| 2 | BKCM_DUNH_AGE | INTEGER | 2 | — | Age # |
| 3 | BKCM_DUNH_AMT | NUMERIC | 8 | 2 | Amount |
| 4 | BKCM_DUNH_DATE | DATE | 4 | — | Date |
| 5 | BKCM_DUNH_FORM | STRING | 15 | — | Form # |
| 6 | BKCM_DUNH_TOT | NUMERIC | 8 | 2 | Total |

## BKCMFORM
**FORM & DUN LETTER TEMPLATE**

Fields: 8

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKCM_FORM_CODE | STRING | 15 | — | Form Code |
| 2 | BKCM_FORM_DESC | STRING | 30 | — | Description |
| 3 | BKCM_FORM_DUN | STRING | 1 | — | Dun Letter Y/N |
| 4 | BKCM_FORM_LEFT | INTEGER | 2 | — | Left Justificaion |
| 5 | BKCM_FORM_LINE | INTEGER | 2 | — | Line |
| 6 | BKCM_FORM_LNSPG | INTEGER | 2 | — | Lines Per Page |
| 7 | BKCM_FORM_NOTE | STRING | 78 | — | Note - body of letter |
| 8 | BKCM_FORM_START | INTEGER | 2 | — | Starting Line |

## BKISHTAX
**PAID SALES TAX DETAIL**

Fields: 13

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKIS_TAX_APINV | STRING | 10 | — | — |
| 2 | BKIS_TAX_CODE | STRING | 10 | — | — |
| 3 | BKIS_TAX_CUST | STRING | 10 | — | — |
| 4 | BKIS_TAX_DATE | DATE | 4 | — | — |
| 5 | BKIS_TAX_INVNO | NUMERIC | 8 | — | — |
| 6 | BKIS_TAX_ISCUR | STRING | 3 | — | — |
| 7 | BKIS_TAX_NONTAX | NUMERIC | 8 | 2 | — |
| 8 | BKIS_TAX_PONO | NUMERIC | 8 | — | — |
| 9 | BKIS_TAX_TAG | STRING | 1 | — | — |
| 10 | BKIS_TAX_TAXABL | NUMERIC | 8 | 2 | — |
| 11 | BKIS_TAX_TAXAMT | NUMERIC | 8 | 2 | — |
| 12 | BKIS_TAX_TRFLAG | STRING | 1 | — | — |
| 13 | BKIS_TAX_VEND | STRING | 10 | — | — |

## BKISTAX
**SALES TAX DETAIL**

Fields: 13

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKIS_TAX_APINV | STRING | 10 | — | — |
| 2 | BKIS_TAX_CODE | STRING | 10 | — | — |
| 3 | BKIS_TAX_CUST | STRING | 10 | — | — |
| 4 | BKIS_TAX_DATE | DATE | 4 | — | — |
| 5 | BKIS_TAX_INVNO | NUMERIC | 8 | — | — |
| 6 | BKIS_TAX_ISCUR | STRING | 3 | — | — |
| 7 | BKIS_TAX_NONTAX | NUMERIC | 8 | 2 | — |
| 8 | BKIS_TAX_PONO | NUMERIC | 8 | — | — |
| 9 | BKIS_TAX_TAG | STRING | 1 | — | — |
| 10 | BKIS_TAX_TAXABL | NUMERIC | 8 | 2 | — |
| 11 | BKIS_TAX_TAXAMT | NUMERIC | 8 | 2 | — |
| 12 | BKIS_TAX_TRFLAG | STRING | 1 | — | — |
| 13 | BKIS_TAX_VEND | STRING | 10 | — | — |

## BKSYAR
**AR DEFAULT MASTER**

Fields: 2

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKSY_AR_DEPNO | NUMERIC | 8 | — | — |
| 2 | BKSY_AR_TRXN | NUMERIC | 8 | — | — |

## CUSTCLAS
**CUSTOMER CLASS MASTER**

Fields: 2

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTCLASS_M_CLASS | STRING | 4 | — | — |
| 2 | MTCLASS_M_DESC | STRING | 30 | — | — |

## IS2DBAR
**2 D BAR CODE PARAMETERS**

Fields: 109

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS2D_BAR_ASCII | INTEGER | 2 | — | — |
| 2 | IS2D_BAR_CHAR | STRING | 5 | — | — |
| 3 | IS2D_BAR_CODE | STRING | 10 | — | — |
| 4 | IS2D_BAR_DESC | STRING | 60 | — | — |
| 5 | IS2D_BAR_DOCPR_1 | STRING | 1 | — | — |
| 6 | IS2D_BAR_DOCPR_10 | STRING | 1 | — | — |
| 7 | IS2D_BAR_DOCPR_100 | STRING | 1 | — | — |
| 8 | IS2D_BAR_DOCPR_11 | STRING | 1 | — | — |
| 9 | IS2D_BAR_DOCPR_12 | STRING | 1 | — | — |
| 10 | IS2D_BAR_DOCPR_13 | STRING | 1 | — | — |
| 11 | IS2D_BAR_DOCPR_14 | STRING | 1 | — | — |
| 12 | IS2D_BAR_DOCPR_15 | STRING | 1 | — | — |
| 13 | IS2D_BAR_DOCPR_16 | STRING | 1 | — | — |
| 14 | IS2D_BAR_DOCPR_17 | STRING | 1 | — | — |
| 15 | IS2D_BAR_DOCPR_18 | STRING | 1 | — | — |
| 16 | IS2D_BAR_DOCPR_19 | STRING | 1 | — | — |
| 17 | IS2D_BAR_DOCPR_2 | STRING | 1 | — | — |
| 18 | IS2D_BAR_DOCPR_20 | STRING | 1 | — | — |
| 19 | IS2D_BAR_DOCPR_21 | STRING | 1 | — | — |
| 20 | IS2D_BAR_DOCPR_22 | STRING | 1 | — | — |
| 21 | IS2D_BAR_DOCPR_23 | STRING | 1 | — | — |
| 22 | IS2D_BAR_DOCPR_24 | STRING | 1 | — | — |
| 23 | IS2D_BAR_DOCPR_25 | STRING | 1 | — | — |
| 24 | IS2D_BAR_DOCPR_26 | STRING | 1 | — | — |
| 25 | IS2D_BAR_DOCPR_27 | STRING | 1 | — | — |
| 26 | IS2D_BAR_DOCPR_28 | STRING | 1 | — | — |
| 27 | IS2D_BAR_DOCPR_29 | STRING | 1 | — | — |
| 28 | IS2D_BAR_DOCPR_3 | STRING | 1 | — | — |
| 29 | IS2D_BAR_DOCPR_30 | STRING | 1 | — | — |
| 30 | IS2D_BAR_DOCPR_31 | STRING | 1 | — | — |
| 31 | IS2D_BAR_DOCPR_32 | STRING | 1 | — | — |
| 32 | IS2D_BAR_DOCPR_33 | STRING | 1 | — | — |
| 33 | IS2D_BAR_DOCPR_34 | STRING | 1 | — | — |
| 34 | IS2D_BAR_DOCPR_35 | STRING | 1 | — | — |
| 35 | IS2D_BAR_DOCPR_36 | STRING | 1 | — | — |
| 36 | IS2D_BAR_DOCPR_37 | STRING | 1 | — | — |
| 37 | IS2D_BAR_DOCPR_38 | STRING | 1 | — | — |
| 38 | IS2D_BAR_DOCPR_39 | STRING | 1 | — | — |
| 39 | IS2D_BAR_DOCPR_4 | STRING | 1 | — | — |
| 40 | IS2D_BAR_DOCPR_40 | STRING | 1 | — | — |
| 41 | IS2D_BAR_DOCPR_41 | STRING | 1 | — | — |
| 42 | IS2D_BAR_DOCPR_42 | STRING | 1 | — | — |
| 43 | IS2D_BAR_DOCPR_43 | STRING | 1 | — | — |
| 44 | IS2D_BAR_DOCPR_44 | STRING | 1 | — | — |
| 45 | IS2D_BAR_DOCPR_45 | STRING | 1 | — | — |
| 46 | IS2D_BAR_DOCPR_46 | STRING | 1 | — | — |
| 47 | IS2D_BAR_DOCPR_47 | STRING | 1 | — | — |
| 48 | IS2D_BAR_DOCPR_48 | STRING | 1 | — | — |
| 49 | IS2D_BAR_DOCPR_49 | STRING | 1 | — | — |
| 50 | IS2D_BAR_DOCPR_5 | STRING | 1 | — | — |
| 51 | IS2D_BAR_DOCPR_50 | STRING | 1 | — | — |
| 52 | IS2D_BAR_DOCPR_51 | STRING | 1 | — | — |
| 53 | IS2D_BAR_DOCPR_52 | STRING | 1 | — | — |
| 54 | IS2D_BAR_DOCPR_53 | STRING | 1 | — | — |
| 55 | IS2D_BAR_DOCPR_54 | STRING | 1 | — | — |
| 56 | IS2D_BAR_DOCPR_55 | STRING | 1 | — | — |
| 57 | IS2D_BAR_DOCPR_56 | STRING | 1 | — | — |
| 58 | IS2D_BAR_DOCPR_57 | STRING | 1 | — | — |
| 59 | IS2D_BAR_DOCPR_58 | STRING | 1 | — | — |
| 60 | IS2D_BAR_DOCPR_59 | STRING | 1 | — | — |
| 61 | IS2D_BAR_DOCPR_6 | STRING | 1 | — | — |
| 62 | IS2D_BAR_DOCPR_60 | STRING | 1 | — | — |
| 63 | IS2D_BAR_DOCPR_61 | STRING | 1 | — | — |
| 64 | IS2D_BAR_DOCPR_62 | STRING | 1 | — | — |
| 65 | IS2D_BAR_DOCPR_63 | STRING | 1 | — | — |
| 66 | IS2D_BAR_DOCPR_64 | STRING | 1 | — | — |
| 67 | IS2D_BAR_DOCPR_65 | STRING | 1 | — | — |
| 68 | IS2D_BAR_DOCPR_66 | STRING | 1 | — | — |
| 69 | IS2D_BAR_DOCPR_67 | STRING | 1 | — | — |
| 70 | IS2D_BAR_DOCPR_68 | STRING | 1 | — | — |
| 71 | IS2D_BAR_DOCPR_69 | STRING | 1 | — | — |
| 72 | IS2D_BAR_DOCPR_7 | STRING | 1 | — | — |
| 73 | IS2D_BAR_DOCPR_70 | STRING | 1 | — | — |
| 74 | IS2D_BAR_DOCPR_71 | STRING | 1 | — | — |
| 75 | IS2D_BAR_DOCPR_72 | STRING | 1 | — | — |
| 76 | IS2D_BAR_DOCPR_73 | STRING | 1 | — | — |
| 77 | IS2D_BAR_DOCPR_74 | STRING | 1 | — | — |
| 78 | IS2D_BAR_DOCPR_75 | STRING | 1 | — | — |
| 79 | IS2D_BAR_DOCPR_76 | STRING | 1 | — | — |
| 80 | IS2D_BAR_DOCPR_77 | STRING | 1 | — | — |
| 81 | IS2D_BAR_DOCPR_78 | STRING | 1 | — | — |
| 82 | IS2D_BAR_DOCPR_79 | STRING | 1 | — | — |
| 83 | IS2D_BAR_DOCPR_8 | STRING | 1 | — | — |
| 84 | IS2D_BAR_DOCPR_80 | STRING | 1 | — | — |
| 85 | IS2D_BAR_DOCPR_81 | STRING | 1 | — | — |
| 86 | IS2D_BAR_DOCPR_82 | STRING | 1 | — | — |
| 87 | IS2D_BAR_DOCPR_83 | STRING | 1 | — | — |
| 88 | IS2D_BAR_DOCPR_84 | STRING | 1 | — | — |
| 89 | IS2D_BAR_DOCPR_85 | STRING | 1 | — | — |
| 90 | IS2D_BAR_DOCPR_86 | STRING | 1 | — | — |
| 91 | IS2D_BAR_DOCPR_87 | STRING | 1 | — | — |
| 92 | IS2D_BAR_DOCPR_88 | STRING | 1 | — | — |
| 93 | IS2D_BAR_DOCPR_89 | STRING | 1 | — | — |
| 94 | IS2D_BAR_DOCPR_9 | STRING | 1 | — | — |
| 95 | IS2D_BAR_DOCPR_90 | STRING | 1 | — | — |
| 96 | IS2D_BAR_DOCPR_91 | STRING | 1 | — | — |
| 97 | IS2D_BAR_DOCPR_92 | STRING | 1 | — | — |
| 98 | IS2D_BAR_DOCPR_93 | STRING | 1 | — | — |
| 99 | IS2D_BAR_DOCPR_94 | STRING | 1 | — | — |
| 100 | IS2D_BAR_DOCPR_95 | STRING | 1 | — | — |
| 101 | IS2D_BAR_DOCPR_96 | STRING | 1 | — | — |
| 102 | IS2D_BAR_DOCPR_97 | STRING | 1 | — | — |
| 103 | IS2D_BAR_DOCPR_98 | STRING | 1 | — | — |
| 104 | IS2D_BAR_DOCPR_99 | STRING | 1 | — | — |
| 105 | IS2D_BAR_EXTRA | STRING | 100 | — | — |
| 106 | IS2D_BAR_FIELD | STRING | 25 | — | — |
| 107 | IS2D_BAR_ITEM | STRING | 15 | — | — |
| 108 | IS2D_BAR_ORDER | INTEGER | 2 | — | — |
| 109 | IS2D_BAR_TYPE | STRING | 10 | — | — |

## ISARACHK
**ARCHIVED CUSTOMER PAYMENT HISTORY**

Fields: 12

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAP_CHK_AMTPD | NUMERIC | 8 | 2 | Amount Payed |
| 2 | BKAP_CHK_CHKACT | INTEGER | 2 | — | Bank Account |
| 3 | BKAP_CHK_CHKDTE | DATE | 4 | — | Check Date |
| 4 | BKAP_CHK_DESC | STRING | 25 | — | Description |
| 5 | BKAP_CHK_DISC | NUMERIC | 8 | 2 | Discount |
| 6 | BKAP_CHK_INVAMT | NUMERIC | 8 | 2 | Invoice Amount |
| 7 | BKAP_CHK_INVDTE | DATE | 4 | — | Invoice Date |
| 8 | BKAP_CHK_INVNUM | STRING | 10 | — | Invoice/Voucer Number |
| 9 | BKAP_CHK_ISCUR | STRING | 3 | — | Currency |
| 10 | BKAP_CHK_NUM | NUMERIC | 8 | — | Check Number |
| 11 | BKAP_CHK_TYPE | STRING | 1 | — | Type |
| 12 | BKAP_CHK_VNDCOD | STRING | 10 | — | Vendor Code |

## ISARACST
**ARCHIVED CUSTOMER MASTER**

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

## ISARAHTX
**ARCHIVED SALES TAX**

Fields: 5

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAR_TAX_AMOUNT | NUMERIC | 8 | 2 | Amount |
| 2 | BKAR_TAX_CODE | STRING | 10 | — | Tax Group Code |
| 3 | BKAR_TAX_ID | STRING | 15 | — | Tax ID |
| 4 | BKAR_TAX_INVNO | NUMERIC | 8 | — | Invoice Number |
| 5 | BKAR_TAX_PID | STRING | 1 | — | Y/N |

## ISARAINT
**ARCHIVED CUSTOMER INVOICES**

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

## ISARAIVV
**ARCHIVED AR VOUCHERS**

Fields: 77

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAR_INVV_ARDPT | STRING | 4 | — | — |
| 2 | BKAR_INVV_CHK | INTEGER | 2 | — | Manual Check Number |
| 3 | BKAR_INVV_CODE | STRING | 10 | — | Customer Code |
| 4 | BKAR_INVV_COGS | NUMERIC | 8 | 2 | COGS |
| 5 | BKAR_INVV_COMPR_1 | NUMERIC | 8 | 4 | — |
| 6 | BKAR_INVV_COMPR_2 | NUMERIC | 8 | 4 | — |
| 7 | BKAR_INVV_COOP | NUMERIC | 8 | 2 | Coop |
| 8 | BKAR_INVV_DAMT_1 | NUMERIC | 8 | 2 | — |
| 9 | BKAR_INVV_DAMT_10 | NUMERIC | 8 | 2 | — |
| 10 | BKAR_INVV_DAMT_2 | NUMERIC | 8 | 2 | — |
| 11 | BKAR_INVV_DAMT_3 | NUMERIC | 8 | 2 | — |
| 12 | BKAR_INVV_DAMT_4 | NUMERIC | 8 | 2 | — |
| 13 | BKAR_INVV_DAMT_5 | NUMERIC | 8 | 2 | — |
| 14 | BKAR_INVV_DAMT_6 | NUMERIC | 8 | 2 | — |
| 15 | BKAR_INVV_DAMT_7 | NUMERIC | 8 | 2 | — |
| 16 | BKAR_INVV_DAMT_8 | NUMERIC | 8 | 2 | — |
| 17 | BKAR_INVV_DAMT_9 | NUMERIC | 8 | 2 | — |
| 18 | BKAR_INVV_DATE | DATE | 4 | — | Date |
| 19 | BKAR_INVV_DC_1 | STRING | 1 | — | — |
| 20 | BKAR_INVV_DC_10 | STRING | 1 | — | — |
| 21 | BKAR_INVV_DC_2 | STRING | 1 | — | — |
| 22 | BKAR_INVV_DC_3 | STRING | 1 | — | — |
| 23 | BKAR_INVV_DC_4 | STRING | 1 | — | — |
| 24 | BKAR_INVV_DC_5 | STRING | 1 | — | — |
| 25 | BKAR_INVV_DC_6 | STRING | 1 | — | — |
| 26 | BKAR_INVV_DC_7 | STRING | 1 | — | — |
| 27 | BKAR_INVV_DC_8 | STRING | 1 | — | — |
| 28 | BKAR_INVV_DC_9 | STRING | 1 | — | — |
| 29 | BKAR_INVV_DESC | STRING | 24 | — | Description |
| 30 | BKAR_INVV_EXTRA | STRING | 50 | — | Extra |
| 31 | BKAR_INVV_FLAG_1 | STRING | 1 | — | — |
| 32 | BKAR_INVV_FLAG_2 | STRING | 1 | — | — |
| 33 | BKAR_INVV_FLAG_3 | STRING | 1 | — | — |
| 34 | BKAR_INVV_FLAG_4 | STRING | 1 | — | — |
| 35 | BKAR_INVV_FLAG_5 | STRING | 1 | — | — |
| 36 | BKAR_INVV_FRGHT | NUMERIC | 8 | 2 | Freight |
| 37 | BKAR_INVV_GLACT_1 | STRING | 10 | — | — |
| 38 | BKAR_INVV_GLACT_10 | STRING | 10 | — | — |
| 39 | BKAR_INVV_GLACT_2 | STRING | 10 | — | — |
| 40 | BKAR_INVV_GLACT_3 | STRING | 10 | — | — |
| 41 | BKAR_INVV_GLACT_4 | STRING | 10 | — | — |
| 42 | BKAR_INVV_GLACT_5 | STRING | 10 | — | — |
| 43 | BKAR_INVV_GLACT_6 | STRING | 10 | — | — |
| 44 | BKAR_INVV_GLACT_7 | STRING | 10 | — | — |
| 45 | BKAR_INVV_GLACT_8 | STRING | 10 | — | — |
| 46 | BKAR_INVV_GLACT_9 | STRING | 10 | — | — |
| 47 | BKAR_INVV_GLD_1 | STRING | 25 | — | — |
| 48 | BKAR_INVV_GLD_10 | STRING | 25 | — | — |
| 49 | BKAR_INVV_GLD_2 | STRING | 25 | — | — |
| 50 | BKAR_INVV_GLD_3 | STRING | 25 | — | — |
| 51 | BKAR_INVV_GLD_4 | STRING | 25 | — | — |
| 52 | BKAR_INVV_GLD_5 | STRING | 25 | — | — |
| 53 | BKAR_INVV_GLD_6 | STRING | 25 | — | — |
| 54 | BKAR_INVV_GLD_7 | STRING | 25 | — | — |
| 55 | BKAR_INVV_GLD_8 | STRING | 25 | — | — |
| 56 | BKAR_INVV_GLD_9 | STRING | 25 | — | — |
| 57 | BKAR_INVV_GLDPT_1 | STRING | 4 | — | — |
| 58 | BKAR_INVV_GLDPT_10 | STRING | 4 | — | — |
| 59 | BKAR_INVV_GLDPT_2 | STRING | 4 | — | — |
| 60 | BKAR_INVV_GLDPT_3 | STRING | 4 | — | — |
| 61 | BKAR_INVV_GLDPT_4 | STRING | 4 | — | — |
| 62 | BKAR_INVV_GLDPT_5 | STRING | 4 | — | — |
| 63 | BKAR_INVV_GLDPT_6 | STRING | 4 | — | — |
| 64 | BKAR_INVV_GLDPT_7 | STRING | 4 | — | — |
| 65 | BKAR_INVV_GLDPT_8 | STRING | 4 | — | — |
| 66 | BKAR_INVV_GLDPT_9 | STRING | 4 | — | — |
| 67 | BKAR_INVV_ISCUR | STRING | 3 | — | Currency |
| 68 | BKAR_INVV_NUM | STRING | 6 | — | Voucher Number |
| 69 | BKAR_INVV_SLSP_1 | INTEGER | 2 | — | — |
| 70 | BKAR_INVV_SLSP_2 | INTEGER | 2 | — | — |
| 71 | BKAR_INVV_TAMT | NUMERIC | 8 | 2 | Amount |
| 72 | BKAR_INVV_TAX | NUMERIC | 8 | 2 | Tax |
| 73 | BKAR_INVV_TDC | STRING | 1 | — | Debit/Credit D/C |
| 74 | BKAR_INVV_TERMD | STRING | 10 | — | Terms Description |
| 75 | BKAR_INVV_TERMN | INTEGER | 2 | — | Terms Number |
| 76 | BKAR_INVV_TYPED | STRING | 10 | — | Type Description |
| 77 | BKAR_INVV_TYPEN | INTEGER | 2 | — | Type Number |

## ISARAT
**ARCHIVED TRANSACTION DETAIL**

Fields: 12

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKART_AMOUNT | NUMERIC | 8 | 2 | Amount |
| 2 | BKART_CHECK | NUMERIC | 8 | — | Check Number |
| 3 | BKART_CNTR | INTEGER | 2 | — | Transaction Counter - tied to Trans. Num. |
| 4 | BKART_CUST | STRING | 10 | — | Customer Code |
| 5 | BKART_DISC | NUMERIC | 8 | 2 | Discount |
| 6 | BKART_ENTDATE | DATE | 4 | — | Date Entered |
| 7 | BKART_INVC | NUMERIC | 8 | — | Not used |
| 8 | BKART_NOTE | STRING | 1 | — | Note Y or Blank |
| 9 | BKART_POSTDATE | DATE | 4 | — | Post Date |
| 10 | BKART_TRXN | NUMERIC | 8 | — | Transaction Number |
| 11 | BKART_TRXNLINK | NUMERIC | 8 | — | Transaction Num - Link to BKARINVT |
| 12 | BKART_TYPE | STRING | 1 | — | Transaction Type O/P/A |

## ISARATNT
**ARCHIVED TRANSACTION NOTES**

Fields: 3

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKART_NOT_CNTR | INTEGER | 2 | — | Line Counter |
| 2 | BKART_NOT_DESC | STRING | 30 | — | Descriptipn |
| 3 | BKART_NOT_TRXN | NUMERIC | 8 | — | Transaction Number |

## ISAREX
**CUSTOMER EXTENSION**

Fields: 51

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISAREX_ALPHA_1 | STRING | 30 | — | — |
| 2 | ISAREX_ALPHA_2 | STRING | 30 | — | — |
| 3 | ISAREX_ALPHA_3 | STRING | 30 | — | — |
| 4 | ISAREX_ALPHA_4 | STRING | 30 | — | — |
| 5 | ISAREX_ALPHA_5 | STRING | 30 | — | — |
| 6 | ISAREX_CRT_FORM | STRING | 60 | — | — |
| 7 | ISAREX_CUST | STRING | 10 | — | — |
| 8 | ISAREX_DATE_1 | DATE | 4 | — | — |
| 9 | ISAREX_DATE_2 | DATE | 4 | — | — |
| 10 | ISAREX_DATE_3 | DATE | 4 | — | — |
| 11 | ISAREX_DATE_4 | DATE | 4 | — | — |
| 12 | ISAREX_DATE_5 | DATE | 4 | — | — |
| 13 | ISAREX_EXTRA | STRING | 100 | — | — |
| 14 | ISAREX_FLAG_1 | STRING | 1 | — | — |
| 15 | ISAREX_FLAG_10 | STRING | 1 | — | — |
| 16 | ISAREX_FLAG_2 | STRING | 1 | — | — |
| 17 | ISAREX_FLAG_3 | STRING | 1 | — | — |
| 18 | ISAREX_FLAG_4 | STRING | 1 | — | — |
| 19 | ISAREX_FLAG_5 | STRING | 1 | — | — |
| 20 | ISAREX_FLAG_6 | STRING | 1 | — | — |
| 21 | ISAREX_FLAG_7 | STRING | 1 | — | — |
| 22 | ISAREX_FLAG_8 | STRING | 1 | — | — |
| 23 | ISAREX_FLAG_9 | STRING | 1 | — | — |
| 24 | ISAREX_LONGNAME | STRING | 60 | — | — |
| 25 | ISAREX_NUM2_1 | NUMERIC | 8 | — | — |
| 26 | ISAREX_NUM2_2 | NUMERIC | 8 | — | — |
| 27 | ISAREX_NUM2_3 | NUMERIC | 8 | — | — |
| 28 | ISAREX_NUM2_4 | NUMERIC | 8 | — | — |
| 29 | ISAREX_NUM2_5 | NUMERIC | 8 | — | — |
| 30 | ISAREX_NUM_1 | NUMERIC | 8 | 2 | — |
| 31 | ISAREX_NUM_2 | NUMERIC | 8 | 2 | — |
| 32 | ISAREX_NUM_3 | NUMERIC | 8 | 2 | — |
| 33 | ISAREX_NUM_4 | NUMERIC | 8 | 2 | — |
| 34 | ISAREX_NUM_5 | NUMERIC | 8 | 2 | — |
| 35 | ISAREX_RS_EXPDT | DATE | 4 | — | — |
| 36 | ISAREX_RS_FORM | STRING | 60 | — | — |
| 37 | ISAREX_RS_SGNDT | DATE | 4 | — | — |
| 38 | ISAREX_RS_UPDT | DATE | 4 | — | — |
| 39 | ISAREX_RS_WHO | STRING | 15 | — | — |
| 40 | ISAREX_SLS_GOAL_1 | NUMERIC | 8 | 2 | — |
| 41 | ISAREX_SLS_GOAL_10 | NUMERIC | 8 | 2 | — |
| 42 | ISAREX_SLS_GOAL_11 | NUMERIC | 8 | 2 | — |
| 43 | ISAREX_SLS_GOAL_12 | NUMERIC | 8 | 2 | — |
| 44 | ISAREX_SLS_GOAL_2 | NUMERIC | 8 | 2 | — |
| 45 | ISAREX_SLS_GOAL_3 | NUMERIC | 8 | 2 | — |
| 46 | ISAREX_SLS_GOAL_4 | NUMERIC | 8 | 2 | — |
| 47 | ISAREX_SLS_GOAL_5 | NUMERIC | 8 | 2 | — |
| 48 | ISAREX_SLS_GOAL_6 | NUMERIC | 8 | 2 | — |
| 49 | ISAREX_SLS_GOAL_7 | NUMERIC | 8 | 2 | — |
| 50 | ISAREX_SLS_GOAL_8 | NUMERIC | 8 | 2 | — |
| 51 | ISAREX_SLS_GOAL_9 | NUMERIC | 8 | 2 | — |

## ISCC
**CREDIT CARD LISTING**

Fields: 13

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_CC_ADDRESS | STRING | 40 | — | — |
| 2 | IS_CC_CARDNAME | STRING | 25 | — | — |
| 3 | IS_CC_CARDTYPE | STRING | 15 | — | — |
| 4 | IS_CC_CODE | STRING | 10 | — | — |
| 5 | IS_CC_EXP | STRING | 4 | — | — |
| 6 | IS_CC_EXTRA | STRING | 100 | — | — |
| 7 | IS_CC_MASKED | STRING | 24 | — | — |
| 8 | IS_CC_SORT | NUMERIC | 8 | — | — |
| 9 | IS_CC_STATUS | STRING | 25 | — | — |
| 10 | IS_CC_STDATE | DATE | 4 | — | — |
| 11 | IS_CC_TOLKEN | STRING | 20 | — | — |
| 12 | IS_CC_XCTRAN | STRING | 10 | — | — |
| 13 | IS_CC_ZIP | STRING | 10 | — | — |

## ISISATAX
**ARCHIVE SALES TAX**

Fields: 13

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKIS_TAX_APINV | STRING | 10 | — | — |
| 2 | BKIS_TAX_CODE | STRING | 10 | — | — |
| 3 | BKIS_TAX_CUST | STRING | 10 | — | — |
| 4 | BKIS_TAX_DATE | DATE | 4 | — | — |
| 5 | BKIS_TAX_INVNO | NUMERIC | 8 | — | — |
| 6 | BKIS_TAX_ISCUR | STRING | 3 | — | — |
| 7 | BKIS_TAX_NONTAX | NUMERIC | 8 | 2 | — |
| 8 | BKIS_TAX_PONO | NUMERIC | 8 | — | — |
| 9 | BKIS_TAX_TAG | STRING | 1 | — | — |
| 10 | BKIS_TAX_TAXABL | NUMERIC | 8 | 2 | — |
| 11 | BKIS_TAX_TAXAMT | NUMERIC | 8 | 2 | — |
| 12 | BKIS_TAX_TRFLAG | STRING | 1 | — | — |
| 13 | BKIS_TAX_VEND | STRING | 10 | — | — |

## ISTAXFIL
**TAX CODES**

Fields: 84

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISIS_TXF_CODE | STRING | 10 | — | — |
| 2 | ISIS_TXF_DESC | STRING | 30 | — | — |
| 3 | ISIS_TXF_GLAPO | STRING | 10 | — | — |
| 4 | ISIS_TXF_GLASO | STRING | 10 | — | — |
| 5 | ISIS_TXF_GLDPO | STRING | 4 | — | — |
| 6 | ISIS_TXF_GLDSO | STRING | 4 | — | — |
| 7 | ISIS_TXF_IDNUM | STRING | 15 | — | — |
| 8 | ISIS_TXF_ISCUR | STRING | 3 | — | — |
| 9 | ISIS_TXF_POHRNG_1 | NUMERIC | 8 | 2 | — |
| 10 | ISIS_TXF_POHRNG_2 | NUMERIC | 8 | 2 | — |
| 11 | ISIS_TXF_POHRNG_3 | NUMERIC | 8 | 2 | — |
| 12 | ISIS_TXF_POHRNG_4 | NUMERIC | 8 | 2 | — |
| 13 | ISIS_TXF_POHRNG_5 | NUMERIC | 8 | 2 | — |
| 14 | ISIS_TXF_POHRNG_6 | NUMERIC | 8 | 2 | — |
| 15 | ISIS_TXF_POHRNG_7 | NUMERIC | 8 | 2 | — |
| 16 | ISIS_TXF_POHRNG_8 | NUMERIC | 8 | 2 | — |
| 17 | ISIS_TXF_POHRNG_9 | NUMERIC | 8 | 2 | — |
| 18 | ISIS_TXF_POLRNG_1 | NUMERIC | 8 | 2 | — |
| 19 | ISIS_TXF_POLRNG_2 | NUMERIC | 8 | 2 | — |
| 20 | ISIS_TXF_POLRNG_3 | NUMERIC | 8 | 2 | — |
| 21 | ISIS_TXF_POLRNG_4 | NUMERIC | 8 | 2 | — |
| 22 | ISIS_TXF_POLRNG_5 | NUMERIC | 8 | 2 | — |
| 23 | ISIS_TXF_POLRNG_6 | NUMERIC | 8 | 2 | — |
| 24 | ISIS_TXF_POLRNG_7 | NUMERIC | 8 | 2 | — |
| 25 | ISIS_TXF_POLRNG_8 | NUMERIC | 8 | 2 | — |
| 26 | ISIS_TXF_POLRNG_9 | NUMERIC | 8 | 2 | — |
| 27 | ISIS_TXF_POMAX | NUMERIC | 8 | 2 | — |
| 28 | ISIS_TXF_POPERC_1 | NUMERIC | 8 | 3 | — |
| 29 | ISIS_TXF_POPERC_2 | NUMERIC | 8 | 3 | — |
| 30 | ISIS_TXF_POPERC_3 | NUMERIC | 8 | 3 | — |
| 31 | ISIS_TXF_POPERC_4 | NUMERIC | 8 | 3 | — |
| 32 | ISIS_TXF_POPERC_5 | NUMERIC | 8 | 3 | — |
| 33 | ISIS_TXF_POPERC_6 | NUMERIC | 8 | 3 | — |
| 34 | ISIS_TXF_POPERC_7 | NUMERIC | 8 | 3 | — |
| 35 | ISIS_TXF_POPERC_8 | NUMERIC | 8 | 3 | — |
| 36 | ISIS_TXF_POPERC_9 | NUMERIC | 8 | 3 | — |
| 37 | ISIS_TXF_PTICD_1 | STRING | 1 | — | — |
| 38 | ISIS_TXF_PTICD_2 | STRING | 1 | — | — |
| 39 | ISIS_TXF_PTICD_3 | STRING | 1 | — | — |
| 40 | ISIS_TXF_PTICD_4 | STRING | 1 | — | — |
| 41 | ISIS_TXF_PTICD_5 | STRING | 1 | — | — |
| 42 | ISIS_TXF_PTICD_6 | STRING | 1 | — | — |
| 43 | ISIS_TXF_PTICD_7 | STRING | 1 | — | — |
| 44 | ISIS_TXF_PTICD_8 | STRING | 1 | — | — |
| 45 | ISIS_TXF_PTICD_9 | STRING | 1 | — | — |
| 46 | ISIS_TXF_SOHRNG_1 | NUMERIC | 8 | 2 | — |
| 47 | ISIS_TXF_SOHRNG_2 | NUMERIC | 8 | 2 | — |
| 48 | ISIS_TXF_SOHRNG_3 | NUMERIC | 8 | 2 | — |
| 49 | ISIS_TXF_SOHRNG_4 | NUMERIC | 8 | 2 | — |
| 50 | ISIS_TXF_SOHRNG_5 | NUMERIC | 8 | 2 | — |
| 51 | ISIS_TXF_SOHRNG_6 | NUMERIC | 8 | 2 | — |
| 52 | ISIS_TXF_SOHRNG_7 | NUMERIC | 8 | 2 | — |
| 53 | ISIS_TXF_SOHRNG_8 | NUMERIC | 8 | 2 | — |
| 54 | ISIS_TXF_SOHRNG_9 | NUMERIC | 8 | 2 | — |
| 55 | ISIS_TXF_SOLRNG_1 | NUMERIC | 8 | 2 | — |
| 56 | ISIS_TXF_SOLRNG_2 | NUMERIC | 8 | 2 | — |
| 57 | ISIS_TXF_SOLRNG_3 | NUMERIC | 8 | 2 | — |
| 58 | ISIS_TXF_SOLRNG_4 | NUMERIC | 8 | 2 | — |
| 59 | ISIS_TXF_SOLRNG_5 | NUMERIC | 8 | 2 | — |
| 60 | ISIS_TXF_SOLRNG_6 | NUMERIC | 8 | 2 | — |
| 61 | ISIS_TXF_SOLRNG_7 | NUMERIC | 8 | 2 | — |
| 62 | ISIS_TXF_SOLRNG_8 | NUMERIC | 8 | 2 | — |
| 63 | ISIS_TXF_SOLRNG_9 | NUMERIC | 8 | 2 | — |
| 64 | ISIS_TXF_SOMAX | NUMERIC | 8 | 2 | — |
| 65 | ISIS_TXF_SOPERC_1 | NUMERIC | 8 | 3 | — |
| 66 | ISIS_TXF_SOPERC_2 | NUMERIC | 8 | 3 | — |
| 67 | ISIS_TXF_SOPERC_3 | NUMERIC | 8 | 3 | — |
| 68 | ISIS_TXF_SOPERC_4 | NUMERIC | 8 | 3 | — |
| 69 | ISIS_TXF_SOPERC_5 | NUMERIC | 8 | 3 | — |
| 70 | ISIS_TXF_SOPERC_6 | NUMERIC | 8 | 3 | — |
| 71 | ISIS_TXF_SOPERC_7 | NUMERIC | 8 | 3 | — |
| 72 | ISIS_TXF_SOPERC_8 | NUMERIC | 8 | 3 | — |
| 73 | ISIS_TXF_SOPERC_9 | NUMERIC | 8 | 3 | — |
| 74 | ISIS_TXF_TAXIN | STRING | 1 | — | — |
| 75 | ISIS_TXF_TICD_1 | STRING | 1 | — | — |
| 76 | ISIS_TXF_TICD_2 | STRING | 1 | — | — |
| 77 | ISIS_TXF_TICD_3 | STRING | 1 | — | — |
| 78 | ISIS_TXF_TICD_4 | STRING | 1 | — | — |
| 79 | ISIS_TXF_TICD_5 | STRING | 1 | — | — |
| 80 | ISIS_TXF_TICD_6 | STRING | 1 | — | — |
| 81 | ISIS_TXF_TICD_7 | STRING | 1 | — | — |
| 82 | ISIS_TXF_TICD_8 | STRING | 1 | — | — |
| 83 | ISIS_TXF_TICD_9 | STRING | 1 | — | — |
| 84 | ISIS_TXF_VNDCD | STRING | 10 | — | — |

## ISTAXGRP
**TAX GROUPS**

Fields: 105

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISIS_TXG_CODE_1 | STRING | 10 | — | — |
| 2 | ISIS_TXG_CODE_2 | STRING | 10 | — | — |
| 3 | ISIS_TXG_CODE_3 | STRING | 10 | — | — |
| 4 | ISIS_TXG_CODE_4 | STRING | 10 | — | — |
| 5 | ISIS_TXG_CODE_5 | STRING | 10 | — | — |
| 6 | ISIS_TXG_CODE_6 | STRING | 10 | — | — |
| 7 | ISIS_TXG_CODE_7 | STRING | 10 | — | — |
| 8 | ISIS_TXG_CODE_8 | STRING | 10 | — | — |
| 9 | ISIS_TXG_CODE_9 | STRING | 10 | — | — |
| 10 | ISIS_TXG_COLECT_1 | NUMERIC | 8 | 2 | — |
| 11 | ISIS_TXG_COLECT_10 | NUMERIC | 8 | 2 | — |
| 12 | ISIS_TXG_COLECT_11 | NUMERIC | 8 | 2 | — |
| 13 | ISIS_TXG_COLECT_12 | NUMERIC | 8 | 2 | — |
| 14 | ISIS_TXG_COLECT_2 | NUMERIC | 8 | 2 | — |
| 15 | ISIS_TXG_COLECT_3 | NUMERIC | 8 | 2 | — |
| 16 | ISIS_TXG_COLECT_4 | NUMERIC | 8 | 2 | — |
| 17 | ISIS_TXG_COLECT_5 | NUMERIC | 8 | 2 | — |
| 18 | ISIS_TXG_COLECT_6 | NUMERIC | 8 | 2 | — |
| 19 | ISIS_TXG_COLECT_7 | NUMERIC | 8 | 2 | — |
| 20 | ISIS_TXG_COLECT_8 | NUMERIC | 8 | 2 | — |
| 21 | ISIS_TXG_COLECT_9 | NUMERIC | 8 | 2 | — |
| 22 | ISIS_TXG_DESC | STRING | 30 | — | — |
| 23 | ISIS_TXG_DESCF_1 | STRING | 20 | — | — |
| 24 | ISIS_TXG_DESCF_2 | STRING | 20 | — | — |
| 25 | ISIS_TXG_DESCF_3 | STRING | 20 | — | — |
| 26 | ISIS_TXG_DESCF_4 | STRING | 20 | — | — |
| 27 | ISIS_TXG_DESCF_5 | STRING | 20 | — | — |
| 28 | ISIS_TXG_DESCF_6 | STRING | 20 | — | — |
| 29 | ISIS_TXG_DESCF_7 | STRING | 20 | — | — |
| 30 | ISIS_TXG_DESCF_8 | STRING | 20 | — | — |
| 31 | ISIS_TXG_DESCF_9 | STRING | 20 | — | — |
| 32 | ISIS_TXG_FREIGT | STRING | 1 | — | — |
| 33 | ISIS_TXG_FRGT_1 | STRING | 1 | — | — |
| 34 | ISIS_TXG_FRGT_2 | STRING | 1 | — | — |
| 35 | ISIS_TXG_FRGT_3 | STRING | 1 | — | — |
| 36 | ISIS_TXG_FRGT_4 | STRING | 1 | — | — |
| 37 | ISIS_TXG_FRGT_5 | STRING | 1 | — | — |
| 38 | ISIS_TXG_FRGT_6 | STRING | 1 | — | — |
| 39 | ISIS_TXG_FRGT_7 | STRING | 1 | — | — |
| 40 | ISIS_TXG_FRGT_8 | STRING | 1 | — | — |
| 41 | ISIS_TXG_FRGT_9 | STRING | 1 | — | — |
| 42 | ISIS_TXG_IDC_1 | STRING | 15 | — | — |
| 43 | ISIS_TXG_IDC_2 | STRING | 15 | — | — |
| 44 | ISIS_TXG_IDC_3 | STRING | 15 | — | — |
| 45 | ISIS_TXG_IDC_4 | STRING | 15 | — | — |
| 46 | ISIS_TXG_IDC_5 | STRING | 15 | — | — |
| 47 | ISIS_TXG_IDC_6 | STRING | 15 | — | — |
| 48 | ISIS_TXG_IDC_7 | STRING | 15 | — | — |
| 49 | ISIS_TXG_IDC_8 | STRING | 15 | — | — |
| 50 | ISIS_TXG_IDC_9 | STRING | 15 | — | — |
| 51 | ISIS_TXG_NAME | STRING | 10 | — | — |
| 52 | ISIS_TXG_NONTAX_1 | NUMERIC | 8 | 2 | — |
| 53 | ISIS_TXG_NONTAX_10 | NUMERIC | 8 | 2 | — |
| 54 | ISIS_TXG_NONTAX_11 | NUMERIC | 8 | 2 | — |
| 55 | ISIS_TXG_NONTAX_12 | NUMERIC | 8 | 2 | — |
| 56 | ISIS_TXG_NONTAX_2 | NUMERIC | 8 | 2 | — |
| 57 | ISIS_TXG_NONTAX_3 | NUMERIC | 8 | 2 | — |
| 58 | ISIS_TXG_NONTAX_4 | NUMERIC | 8 | 2 | — |
| 59 | ISIS_TXG_NONTAX_5 | NUMERIC | 8 | 2 | — |
| 60 | ISIS_TXG_NONTAX_6 | NUMERIC | 8 | 2 | — |
| 61 | ISIS_TXG_NONTAX_7 | NUMERIC | 8 | 2 | — |
| 62 | ISIS_TXG_NONTAX_8 | NUMERIC | 8 | 2 | — |
| 63 | ISIS_TXG_NONTAX_9 | NUMERIC | 8 | 2 | — |
| 64 | ISIS_TXG_OUTSTD | NUMERIC | 8 | 2 | — |
| 65 | ISIS_TXG_PERCC_1 | NUMERIC | 8 | 3 | — |
| 66 | ISIS_TXG_PERCC_2 | NUMERIC | 8 | 3 | — |
| 67 | ISIS_TXG_PERCC_3 | NUMERIC | 8 | 3 | — |
| 68 | ISIS_TXG_PERCC_4 | NUMERIC | 8 | 3 | — |
| 69 | ISIS_TXG_PERCC_5 | NUMERIC | 8 | 3 | — |
| 70 | ISIS_TXG_PERCC_6 | NUMERIC | 8 | 3 | — |
| 71 | ISIS_TXG_PERCC_7 | NUMERIC | 8 | 3 | — |
| 72 | ISIS_TXG_PERCC_8 | NUMERIC | 8 | 3 | — |
| 73 | ISIS_TXG_PERCC_9 | NUMERIC | 8 | 3 | — |
| 74 | ISIS_TXG_PID_1 | STRING | 1 | — | — |
| 75 | ISIS_TXG_PID_2 | STRING | 1 | — | — |
| 76 | ISIS_TXG_PID_3 | STRING | 1 | — | — |
| 77 | ISIS_TXG_PID_4 | STRING | 1 | — | — |
| 78 | ISIS_TXG_PID_5 | STRING | 1 | — | — |
| 79 | ISIS_TXG_PID_6 | STRING | 1 | — | — |
| 80 | ISIS_TXG_PID_7 | STRING | 1 | — | — |
| 81 | ISIS_TXG_PID_8 | STRING | 1 | — | — |
| 82 | ISIS_TXG_PID_9 | STRING | 1 | — | — |
| 83 | ISIS_TXG_TAXBLE_1 | NUMERIC | 8 | 2 | — |
| 84 | ISIS_TXG_TAXBLE_10 | NUMERIC | 8 | 2 | — |
| 85 | ISIS_TXG_TAXBLE_11 | NUMERIC | 8 | 2 | — |
| 86 | ISIS_TXG_TAXBLE_12 | NUMERIC | 8 | 2 | — |
| 87 | ISIS_TXG_TAXBLE_2 | NUMERIC | 8 | 2 | — |
| 88 | ISIS_TXG_TAXBLE_3 | NUMERIC | 8 | 2 | — |
| 89 | ISIS_TXG_TAXBLE_4 | NUMERIC | 8 | 2 | — |
| 90 | ISIS_TXG_TAXBLE_5 | NUMERIC | 8 | 2 | — |
| 91 | ISIS_TXG_TAXBLE_6 | NUMERIC | 8 | 2 | — |
| 92 | ISIS_TXG_TAXBLE_7 | NUMERIC | 8 | 2 | — |
| 93 | ISIS_TXG_TAXBLE_8 | NUMERIC | 8 | 2 | — |
| 94 | ISIS_TXG_TAXBLE_9 | NUMERIC | 8 | 2 | — |
| 95 | ISIS_TXG_TAXON_1 | STRING | 1 | — | — |
| 96 | ISIS_TXG_TAXON_2 | STRING | 1 | — | — |
| 97 | ISIS_TXG_TAXON_3 | STRING | 1 | — | — |
| 98 | ISIS_TXG_TAXON_4 | STRING | 1 | — | — |
| 99 | ISIS_TXG_TAXON_5 | STRING | 1 | — | — |
| 100 | ISIS_TXG_TAXON_6 | STRING | 1 | — | — |
| 101 | ISIS_TXG_TAXON_7 | STRING | 1 | — | — |
| 102 | ISIS_TXG_TAXON_8 | STRING | 1 | — | — |
| 103 | ISIS_TXG_TAXON_9 | STRING | 1 | — | — |
| 104 | ISIS_TXG_TOFPER | NUMERIC | 8 | 3 | — |
| 105 | ISIS_TXG_TOTPER | NUMERIC | 8 | 3 | — |

## MKECLASS
**AR CUSTOMER CHECK CROSS REFERENCE**

Fields: 3

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MKECLASS_ACTIVE | STRING | 1 | — | — |
| 2 | MKECLASS_DESC | STRING | 45 | — | — |
| 3 | MKECLASS_NUM | NUMERIC | 8 | — | — |
