# AR — Accounts Receivable: Field Reference

Status: verified-schema + completed field meanings (Pass 574k-6, 2026-07-06).

Source: `Evo-DBA_File_Fields 052421.xlsx`, sheet "Fields".

Identical-schema notes:
- BKAR_* customer master (106f): BKARCUST, BKARSHIP (NOT USED), ISARACST all share same schema.
- BKAR_INVT_* aging invoice (23f): BKARINVT and ISARAINT are identical.
- BKAR_INVV_* voucher (77f): BKARINVV and ISARAIVV are identical.
- BKIS_TAX_* tax detail (13f): BKISHTAX, BKISTAX, and ISISATAX are identical.
- BKAP_CHK_* payment history (12f): BKARCHKF and ISARACHK are identical.
- BKAR_TAX_* sales tax (5f): BKARHTAX and ISARAHTX are identical.
- BKART_* aging txn (12f): BKART and ISARAT are identical.
- BKART_NOT_* txn notes (3f): BKARTNOT and ISARATNT are identical.

---

## BKARCHKF
**CUSTOMER PAYMENT HISTORY**

Fields: 12 | Key: BKAP_CHK_NUM + BKAP_CHK_INVNUM

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAP_CHK_AMTPD | NUMERIC | 8 | 2 | Amount Paid |
| 2 | BKAP_CHK_CHKACT | INTEGER | 2 | — | Bank Account |
| 3 | BKAP_CHK_CHKDTE | DATE | 4 | — | Check Date |
| 4 | BKAP_CHK_DESC | STRING | 25 | — | Description |
| 5 | BKAP_CHK_DISC | NUMERIC | 8 | 2 | Discount |
| 6 | BKAP_CHK_INVAMT | NUMERIC | 8 | 2 | Invoice Amount |
| 7 | BKAP_CHK_INVDTE | DATE | 4 | — | Invoice Date |
| 8 | BKAP_CHK_INVNUM | STRING | 10 | — | Invoice/Voucher Number |
| 9 | BKAP_CHK_ISCUR | STRING | 3 | — | Currency |
| 10 | BKAP_CHK_NUM | NUMERIC | 8 | — | Check Number |
| 11 | BKAP_CHK_TYPE | STRING | 1 | — | Type |
| 12 | BKAP_CHK_VNDCOD | STRING | 10 | — | Vendor Code |

## BKARCUST
**CUSTOMER MASTER**

Fields: 106 | Key: BKAR_CUSTCODE

Identical 106-field BKAR_* schema to BKARSHIP (NOT USED) and ISARACST (archive).

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAR_ADD1 | STRING | 30 | — | Address Line 1 |
| 2 | BKAR_ADD2_1 | STRING | 30 | — | Address line 2 (supplemental address) |
| 3 | BKAR_ADD2_2 | STRING | 30 | — | Address line 3 (suite, building, or continuation) |
| 4 | BKAR_CARRIER | STRING | 15 | — | Carrier |
| 5 | BKAR_CHG_INTRST | STRING | 1 | — | Charge Interest Y/N |
| 6 | BKAR_CITY | STRING | 26 | — | City |
| 7 | BKAR_CLASS | STRING | 4 | — | Customer Class |
| 8 | BKAR_COGS_LYR | NUMERIC | 8 | 2 | COGS Last Year |
| 9 | BKAR_COGS_MTD | NUMERIC | 8 | 2 | COGS Month To Date |
| 10 | BKAR_COGS_PVAR | NUMERIC | 8 | 4 | COGS Percent Variance |
| 11 | BKAR_COGS_YTD | NUMERIC | 8 | 2 | COGS Year To Date |
| 12 | BKAR_COMM_1 | NUMERIC | 8 | 4 | Commission rate for salesperson 1 (percentage) |
| 13 | BKAR_COMM_2 | NUMERIC | 8 | 4 | Commission rate for salesperson 2 (percentage) |
| 14 | BKAR_CONTACT_1 | STRING | 30 | — | Contact name 1 |
| 15 | BKAR_CONTACT_2 | STRING | 30 | — | Contact name 2 |
| 16 | BKAR_CONTACT_3 | STRING | 30 | — | Contact name 3 |
| 17 | BKAR_CONTACT_4 | STRING | 30 | — | Contact name 4 |
| 18 | BKAR_CONTACT_5 | STRING | 30 | — | Contact name 5 |
| 19 | BKAR_COOP_AMT | NUMERIC | 8 | 2 | COOP Amount |
| 20 | BKAR_COOP_RATE | NUMERIC | 8 | 4 | COOP Rate |
| 21 | BKAR_COUNTRY | STRING | 30 | — | Country |
| 22 | BKAR_CREDIT_HLD | STRING | 1 | — | Credit Hold Y/N |
| 23 | BKAR_CREDITLMT | NUMERIC | 8 | 2 | Credit Limit |
| 24 | BKAR_CUST_YEAR | STRING | 12 | — | Customer-since year / fiscal year code |
| 25 | BKAR_CUSTCODE | STRING | 10 | — | Customer Code (PK) |
| 26 | BKAR_CUSTNAME | STRING | 30 | — | Customer Name |
| 27 | BKAR_DAYS_TOPAY | NUMERIC | 8 | — | Average Days To Pay |
| 28 | BKAR_DISC_CODE | STRING | 10 | — | Discount Code |
| 29 | BKAR_EMAIL_1 | STRING | 128 | — | Email address 1 |
| 30 | BKAR_EMAIL_2 | STRING | 128 | — | Email address 2 |
| 31 | BKAR_EMAIL_3 | STRING | 128 | — | Email address 3 |
| 32 | BKAR_EMAIL_4 | STRING | 128 | — | Email address 4 |
| 33 | BKAR_EMAIL_5 | STRING | 128 | — | Email address 5 |
| 34 | BKAR_EXTRA | STRING | 30 | — | Extra |
| 35 | BKAR_FAX_PHONE | STRING | 25 | — | Fax Number |
| 36 | BKAR_FOB | STRING | 15 | — | Ship FOB |
| 37 | BKAR_FOLUPDTE | DATE | 4 | — | Follow-Up Date |
| 38 | BKAR_FORECAST | STRING | 12 | — | Forecast |
| 39 | BKAR_GLACCT | STRING | 10 | — | GL Account |
| 40 | BKAR_GLDPT | STRING | 4 | — | GL Department |
| 41 | BKAR_GROSS_LYR | NUMERIC | 8 | 2 | Gross Sales Last Year |
| 42 | BKAR_GROSS_MTD | NUMERIC | 8 | 2 | Gross Sales Month To Date |
| 43 | BKAR_GROSS_PVAR | NUMERIC | 8 | 4 | Gross Sales Percent Variance |
| 44 | BKAR_GROSS_YTD | NUMERIC | 8 | 2 | Gross Sales Year To Date |
| 45 | BKAR_HIST_YN | STRING | 1 | — | History Y/N |
| 46 | BKAR_IS_MCCODE | STRING | 3 | — | Multi-Currency Code |
| 47 | BKAR_IS_REP | STRING | 5 | — | Sales rep code (FK → rep master) |
| 48 | BKAR_IS_TAXGRP | STRING | 10 | — | Tax Group (FK → ISTAXGRP) |
| 49 | BKAR_IS_TAXIN | STRING | 1 | — | Excise Tax-In flag |
| 50 | BKAR_LASTPMT | DATE | 4 | — | Last Payment Date |
| 51 | BKAR_LASTSALE | DATE | 4 | — | Last Sale Date |
| 52 | BKAR_LEAD_SRC | STRING | 5 | — | Lead Source code |
| 53 | BKAR_LEAD_SRC2 | STRING | 5 | — | Lead source 2 (secondary lead source code) |
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
| 70 | BKAR_NUM_INVCS | NUMERIC | 8 | — | Number of open invoices |
| 71 | BKAR_OUT_CREDIT_1 | NUMERIC | 8 | 2 | Outstanding / unapplied credit amount 1 |
| 72 | BKAR_OUT_CREDIT_2 | NUMERIC | 8 | 2 | Outstanding / unapplied credit amount 2 |
| 73 | BKAR_OUTINV | NUMERIC | 8 | 2 | Outstanding Invoices total |
| 74 | BKAR_PNET_LYR | NUMERIC | 8 | 4 | Percent Profit Last Year |
| 75 | BKAR_PNET_MTD | NUMERIC | 8 | 4 | Percent Profit Month To Date |
| 76 | BKAR_PNET_PVAR | NUMERIC | 8 | 4 | Percent Profit Percent Variance |
| 77 | BKAR_PNET_YTD | NUMERIC | 8 | 4 | Percent Profit Year To Date |
| 78 | BKAR_PRICE_MAT | INTEGER | 2 | — | Price matrix code |
| 79 | BKAR_PURCH_AGMT | STRING | 1 | — | Purchasing agreement flag |
| 80 | BKAR_QC_INFO | STRING | 30 | — | QC Data / requirements |
| 81 | BKAR_RECV_HOURS | STRING | 30 | — | Receiving Hours |
| 82 | BKAR_REMAINCRD | NUMERIC | 8 | 2 | Credit Remaining (credit limit − outstanding balance) |
| 83 | BKAR_REQD_CERTS | STRING | 10 | — | Required certifications code |
| 84 | BKAR_RESALE_NO | STRING | 15 | — | Resale / tax-exempt certificate number |
| 85 | BKAR_SHIPTO | STRING | 10 | — | Default Ship-To Code |
| 86 | BKAR_SHIPVIA | STRING | 15 | — | Default Ship Via carrier |
| 87 | BKAR_SHP_TOLRNC | STRING | 10 | — | Ship tolerance code (acceptable over/under-shipment tolerance) |
| 88 | BKAR_SHP_WINDOW | STRING | 30 | — | Shipping Window (delivery window spec) |
| 89 | BKAR_SIC_CODE | STRING | 7 | — | SIC Code (Standard Industry Classification) |
| 90 | BKAR_SLSP_NUM_1 | INTEGER | 2 | — | Salesperson 1 number (FK → salesperson master) |
| 91 | BKAR_SLSP_NUM_2 | INTEGER | 2 | — | Salesperson 2 number (secondary salesperson) |
| 92 | BKAR_SORT | STRING | 6 | — | Sort Field |
| 93 | BKAR_START_DATE | DATE | 4 | — | Customer Start Date |
| 94 | BKAR_STATE | STRING | 2 | — | State |
| 95 | BKAR_STATEMENT | STRING | 1 | — | Send Statement Y/N |
| 96 | BKAR_TAX_LOCAL | STRING | 2 | — | Local Tax code |
| 97 | BKAR_TAX_STATE | STRING | 2 | — | State Tax code |
| 98 | BKAR_TAX_YN | STRING | 1 | — | Taxable Y/N |
| 99 | BKAR_TELEPHONE_1 | STRING | 25 | — | Phone number 1 |
| 100 | BKAR_TELEPHONE_2 | STRING | 25 | — | Phone number 2 |
| 101 | BKAR_TELEPHONE_3 | STRING | 25 | — | Phone number 3 |
| 102 | BKAR_TELEPHONE_4 | STRING | 25 | — | Phone number 4 |
| 103 | BKAR_TELEPHONE_5 | STRING | 25 | — | Phone number 5 |
| 104 | BKAR_TERMS_NUM | INTEGER | 2 | — | Payment Terms Number (FK → BKAPTERMS) |
| 105 | BKAR_TERRITORY | STRING | 4 | — | Sales Territory code |
| 106 | BKAR_ZIP | STRING | 10 | — | ZIP Code |

## BKARDEP
**CUSTOMER DEPOSITS**

Fields: 6 | Key: BKAR_DEP_DEPNO

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAR_DEP_CUST | STRING | 10 | — | Customer Code (FK → BKARCUST) |
| 2 | BKAR_DEP_DATE | DATE | 4 | — | Deposit Date |
| 3 | BKAR_DEP_DEPNO | NUMERIC | 8 | — | Deposit Number (PK) |
| 4 | BKAR_DEP_EXTRA | STRING | 50 | — | Extra data |
| 5 | BKAR_DEP_SO | NUMERIC | 8 | — | SO Number (FK → open SO this deposit applies to) |
| 6 | BKAR_DEP_SR | STRING | 1 | — | Deposit applied/status flag |

## BKARDESC
**CUSTOMER WEBSITE & DBA CUSTOMER & SO NOTES**

Fields: 5 | Key: BK_DESC_NUM + BK_DESC_LINE

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BK_DESC_CODE | STRING | 15 | — | not used |
| 2 | BK_DESC_DESC | STRING | 25 | — | not used |
| 3 | BK_DESC_LINE | INTEGER | 2 | — | Notes line number |
| 4 | BK_DESC_NOTES | STRING | 70 | — | Notes text |
| 5 | BK_DESC_NUM | NUMERIC | 8 | — | Document number (SO/customer reference) |

## BKARHDSC
**DBA INVOICE NOTES**

Fields: 5 | Key: BK_DESC_NUM + BK_DESC_LINE

Identical schema to BKARDESC above. See that table for all field definitions.

## BKARHTAX
**SALES TAX**

Fields: 5 | Key: BKAR_TAX_INVNO + BKAR_TAX_CODE

Identical 5-field BKAR_TAX_* schema to ISARAHTX.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAR_TAX_AMOUNT | NUMERIC | 8 | 2 | Tax Amount |
| 2 | BKAR_TAX_CODE | STRING | 10 | — | Tax Group Code (FK → ISTAXGRP) |
| 3 | BKAR_TAX_ID | STRING | 15 | — | Tax ID / registration number |
| 4 | BKAR_TAX_INVNO | NUMERIC | 8 | — | Invoice Number |
| 5 | BKAR_TAX_PID | STRING | 1 | — | Percent-included flag (`Y`=tax included in price) |

## BKARINVT
**AR AGING INVOICE**

Fields: 23 | Key: BKAR_INVT_NUM + BKAR_INVT_CODE

Identical 23-field BKAR_INVT_* schema to ISARAINT.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAR_INVT_AMT | NUMERIC | 8 | 2 | Original invoice amount |
| 2 | BKAR_INVT_AMTRM | NUMERIC | 8 | 2 | Amount remaining (unpaid balance) |
| 3 | BKAR_INVT_CHKAC | INTEGER | 2 | — | Checking Account number |
| 4 | BKAR_INVT_CHKNO | NUMERIC | 8 | — | Check Number (payment applied) |
| 5 | BKAR_INVT_CLOSD | DATE | 4 | — | Date the invoice was closed / fully paid |
| 6 | BKAR_INVT_CODE | STRING | 10 | — | Customer Code (FK → BKARCUST) |
| 7 | BKAR_INVT_DATE | DATE | 4 | — | Invoice / transaction date |
| 8 | BKAR_INVT_DEPNO | NUMERIC | 8 | — | Deposit number (if this invoice has a deposit applied) |
| 9 | BKAR_INVT_DEPST | STRING | 1 | — | Deposit status flag |
| 10 | BKAR_INVT_DESC | STRING | 25 | — | Description |
| 11 | BKAR_INVT_EXTRA | STRING | 50 | — | Extra |
| 12 | BKAR_INVT_GLDPT | STRING | 4 | — | GL Department |
| 13 | BKAR_INVT_MCCOD | STRING | 3 | — | Multi-currency code |
| 14 | BKAR_INVT_MCRAT | NUMERIC | 8 | 6 | Multi-currency exchange rate |
| 15 | BKAR_INVT_NORMP | STRING | 1 | — | Normal payment flag (`Y`=standard payment flow) |
| 16 | BKAR_INVT_NUM | NUMERIC | 8 | — | Invoice Number (PK) |
| 17 | BKAR_INVT_OPEND | DATE | 4 | — | Date invoice was opened / entered |
| 18 | BKAR_INVT_PDATE | DATE | 4 | — | Due date / payment due date |
| 19 | BKAR_INVT_SLSP | INTEGER | 2 | — | Salesperson 1 (FK → salesperson master) |
| 20 | BKAR_INVT_SLSP2 | INTEGER | 2 | — | Salesperson 2 |
| 21 | BKAR_INVT_TERMN | INTEGER | 2 | — | Terms Number |
| 22 | BKAR_INVT_TRXN | NUMERIC | 8 | — | AR transaction number (FK → BKART.BKART_TRXN) |
| 23 | BKAR_INVT_TYPE | STRING | 1 | — | Transaction type (`I`=invoice, `C`=credit, `P`=payment) |

## BKARINVV
**AR VOUCHER**

Fields: 77 | Key: BKAR_INVV_NUM

Identical 77-field BKAR_INVV_* schema to ISARAIVV.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAR_INVV_ARDPT | STRING | 4 | — | AR department code |
| 2 | BKAR_INVV_CHK | INTEGER | 2 | — | Manual Check Number |
| 3 | BKAR_INVV_CODE | STRING | 10 | — | Customer Code (FK → BKARCUST) |
| 4 | BKAR_INVV_COGS | NUMERIC | 8 | 2 | COGS |
| 5 | BKAR_INVV_COMPR_1 | NUMERIC | 8 | 4 | Commission percent for salesperson 1 |
| 6 | BKAR_INVV_COMPR_2 | NUMERIC | 8 | 4 | Commission percent for salesperson 2 |
| 7 | BKAR_INVV_COOP | NUMERIC | 8 | 2 | Co-op advertising amount |
| 8 | BKAR_INVV_DAMT_1 | NUMERIC | 8 | 2 | GL distribution dollar amount for line 1 |
| 9 | BKAR_INVV_DAMT_10 | NUMERIC | 8 | 2 | GL distribution dollar amount for line 10 |
| 10 | BKAR_INVV_DAMT_2 | NUMERIC | 8 | 2 | GL distribution dollar amount for line 2 |
| 11 | BKAR_INVV_DAMT_3 | NUMERIC | 8 | 2 | GL distribution dollar amount for line 3 |
| 12 | BKAR_INVV_DAMT_4 | NUMERIC | 8 | 2 | GL distribution dollar amount for line 4 |
| 13 | BKAR_INVV_DAMT_5 | NUMERIC | 8 | 2 | GL distribution dollar amount for line 5 |
| 14 | BKAR_INVV_DAMT_6 | NUMERIC | 8 | 2 | GL distribution dollar amount for line 6 |
| 15 | BKAR_INVV_DAMT_7 | NUMERIC | 8 | 2 | GL distribution dollar amount for line 7 |
| 16 | BKAR_INVV_DAMT_8 | NUMERIC | 8 | 2 | GL distribution dollar amount for line 8 |
| 17 | BKAR_INVV_DAMT_9 | NUMERIC | 8 | 2 | GL distribution dollar amount for line 9 |
| 18 | BKAR_INVV_DATE | DATE | 4 | — | Voucher date |
| 19 | BKAR_INVV_DC_1 | STRING | 1 | — | Debit/Credit code for GL distribution line 1 (`D` or `C`) |
| 20 | BKAR_INVV_DC_10 | STRING | 1 | — | Debit/Credit code for GL distribution line 10 |
| 21 | BKAR_INVV_DC_2 | STRING | 1 | — | Debit/Credit code for GL distribution line 2 |
| 22 | BKAR_INVV_DC_3 | STRING | 1 | — | Debit/Credit code for GL distribution line 3 |
| 23 | BKAR_INVV_DC_4 | STRING | 1 | — | Debit/Credit code for GL distribution line 4 |
| 24 | BKAR_INVV_DC_5 | STRING | 1 | — | Debit/Credit code for GL distribution line 5 |
| 25 | BKAR_INVV_DC_6 | STRING | 1 | — | Debit/Credit code for GL distribution line 6 |
| 26 | BKAR_INVV_DC_7 | STRING | 1 | — | Debit/Credit code for GL distribution line 7 |
| 27 | BKAR_INVV_DC_8 | STRING | 1 | — | Debit/Credit code for GL distribution line 8 |
| 28 | BKAR_INVV_DC_9 | STRING | 1 | — | Debit/Credit code for GL distribution line 9 |
| 29 | BKAR_INVV_DESC | STRING | 24 | — | Voucher description |
| 30 | BKAR_INVV_EXTRA | STRING | 50 | — | Extra |
| 31 | BKAR_INVV_FLAG_1 | STRING | 1 | — | User-defined flag 1 |
| 32 | BKAR_INVV_FLAG_2 | STRING | 1 | — | User-defined flag 2 |
| 33 | BKAR_INVV_FLAG_3 | STRING | 1 | — | User-defined flag 3 |
| 34 | BKAR_INVV_FLAG_4 | STRING | 1 | — | User-defined flag 4 |
| 35 | BKAR_INVV_FLAG_5 | STRING | 1 | — | User-defined flag 5 |
| 36 | BKAR_INVV_FRGHT | NUMERIC | 8 | 2 | Freight amount |
| 37 | BKAR_INVV_GLACT_1 | STRING | 10 | — | GL account for distribution line 1 |
| 38 | BKAR_INVV_GLACT_10 | STRING | 10 | — | GL account for distribution line 10 |
| 39 | BKAR_INVV_GLACT_2 | STRING | 10 | — | GL account for distribution line 2 |
| 40 | BKAR_INVV_GLACT_3 | STRING | 10 | — | GL account for distribution line 3 |
| 41 | BKAR_INVV_GLACT_4 | STRING | 10 | — | GL account for distribution line 4 |
| 42 | BKAR_INVV_GLACT_5 | STRING | 10 | — | GL account for distribution line 5 |
| 43 | BKAR_INVV_GLACT_6 | STRING | 10 | — | GL account for distribution line 6 |
| 44 | BKAR_INVV_GLACT_7 | STRING | 10 | — | GL account for distribution line 7 |
| 45 | BKAR_INVV_GLACT_8 | STRING | 10 | — | GL account for distribution line 8 |
| 46 | BKAR_INVV_GLACT_9 | STRING | 10 | — | GL account for distribution line 9 |
| 47 | BKAR_INVV_GLD_1 | STRING | 25 | — | GL department description for distribution line 1 |
| 48 | BKAR_INVV_GLD_10 | STRING | 25 | — | GL department description for distribution line 10 |
| 49 | BKAR_INVV_GLD_2 | STRING | 25 | — | GL department description for distribution line 2 |
| 50 | BKAR_INVV_GLD_3 | STRING | 25 | — | GL department description for distribution line 3 |
| 51 | BKAR_INVV_GLD_4 | STRING | 25 | — | GL department description for distribution line 4 |
| 52 | BKAR_INVV_GLD_5 | STRING | 25 | — | GL department description for distribution line 5 |
| 53 | BKAR_INVV_GLD_6 | STRING | 25 | — | GL department description for distribution line 6 |
| 54 | BKAR_INVV_GLD_7 | STRING | 25 | — | GL department description for distribution line 7 |
| 55 | BKAR_INVV_GLD_8 | STRING | 25 | — | GL department description for distribution line 8 |
| 56 | BKAR_INVV_GLD_9 | STRING | 25 | — | GL department description for distribution line 9 |
| 57 | BKAR_INVV_GLDPT_1 | STRING | 4 | — | GL department code for distribution line 1 |
| 58 | BKAR_INVV_GLDPT_10 | STRING | 4 | — | GL department code for distribution line 10 |
| 59 | BKAR_INVV_GLDPT_2 | STRING | 4 | — | GL department code for distribution line 2 |
| 60 | BKAR_INVV_GLDPT_3 | STRING | 4 | — | GL department code for distribution line 3 |
| 61 | BKAR_INVV_GLDPT_4 | STRING | 4 | — | GL department code for distribution line 4 |
| 62 | BKAR_INVV_GLDPT_5 | STRING | 4 | — | GL department code for distribution line 5 |
| 63 | BKAR_INVV_GLDPT_6 | STRING | 4 | — | GL department code for distribution line 6 |
| 64 | BKAR_INVV_GLDPT_7 | STRING | 4 | — | GL department code for distribution line 7 |
| 65 | BKAR_INVV_GLDPT_8 | STRING | 4 | — | GL department code for distribution line 8 |
| 66 | BKAR_INVV_GLDPT_9 | STRING | 4 | — | GL department code for distribution line 9 |
| 67 | BKAR_INVV_ISCUR | STRING | 3 | — | Currency code |
| 68 | BKAR_INVV_NUM | STRING | 6 | — | Voucher Number (PK) |
| 69 | BKAR_INVV_SLSP_1 | INTEGER | 2 | — | Salesperson 1 number (FK → salesperson master) |
| 70 | BKAR_INVV_SLSP_2 | INTEGER | 2 | — | Salesperson 2 number |
| 71 | BKAR_INVV_TAMT | NUMERIC | 8 | 2 | Total amount |
| 72 | BKAR_INVV_TAX | NUMERIC | 8 | 2 | Tax amount |
| 73 | BKAR_INVV_TDC | STRING | 1 | — | Total Debit/Credit indicator (`D` or `C`) |
| 74 | BKAR_INVV_TERMD | STRING | 10 | — | Terms Description |
| 75 | BKAR_INVV_TERMN | INTEGER | 2 | — | Terms Number |
| 76 | BKAR_INVV_TYPED | STRING | 10 | — | Transaction type description |
| 77 | BKAR_INVV_TYPEN | INTEGER | 2 | — | Transaction type number |

## BKARSHIP
**SHIP-TO CUSTOMER MASTER (NOT USED)**

Fields: 106 | Key: BKAR_CUSTCODE

Identical schema to BKARCUST above. See that table for all field definitions. Not used in
current EvoERP — ship-to addresses are stored via BKSOSHIP in the SO module.

## BKART
**AGING TRANSACTION DETAIL**

Fields: 12 | Key: BKART_TRXN + BKART_CNTR

Identical 12-field BKART_* schema to ISARAT.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKART_AMOUNT | NUMERIC | 8 | 2 | Amount |
| 2 | BKART_CHECK | NUMERIC | 8 | — | Check Number |
| 3 | BKART_CNTR | INTEGER | 2 | — | Transaction counter (tied to transaction number) |
| 4 | BKART_CUST | STRING | 10 | — | Customer Code |
| 5 | BKART_DISC | NUMERIC | 8 | 2 | Discount |
| 6 | BKART_ENTDATE | DATE | 4 | — | Date Entered |
| 7 | BKART_INVC | NUMERIC | 8 | — | Not used |
| 8 | BKART_NOTE | STRING | 1 | — | Note `Y` or blank |
| 9 | BKART_POSTDATE | DATE | 4 | — | Post Date |
| 10 | BKART_TRXN | NUMERIC | 8 | — | Transaction Number (PK) |
| 11 | BKART_TRXNLINK | NUMERIC | 8 | — | Transaction number — link to BKARINVT |
| 12 | BKART_TYPE | STRING | 1 | — | Transaction type (`O`=open, `P`=payment, `A`=adjustment) |

## BKARTNOT
**AGING TRANSACTION NOTES**

Fields: 3 | Key: BKART_NOT_TRXN + BKART_NOT_CNTR

Identical 3-field BKART_NOT_* schema to ISARATNT.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKART_NOT_CNTR | INTEGER | 2 | — | Line counter |
| 2 | BKART_NOT_DESC | STRING | 30 | — | Description / note text |
| 3 | BKART_NOT_TRXN | NUMERIC | 8 | — | Transaction number (FK → BKART) |

## BKCMDUN
**DUN LETTER HEADER**

Fields: 36 | Key: (single-row config table)

Dunning letter configuration — up to 10 age brackets, each with a form letter and trigger.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKCM_DUN_AGE_1 | INTEGER | 2 | — | Age bracket 1: days-past-due threshold |
| 2 | BKCM_DUN_AGE_10 | INTEGER | 2 | — | Age bracket 10: days-past-due threshold |
| 3 | BKCM_DUN_AGE_2 | INTEGER | 2 | — | Age bracket 2: days-past-due threshold |
| 4 | BKCM_DUN_AGE_3 | INTEGER | 2 | — | Age bracket 3: days-past-due threshold |
| 5 | BKCM_DUN_AGE_4 | INTEGER | 2 | — | Age bracket 4: days-past-due threshold |
| 6 | BKCM_DUN_AGE_5 | INTEGER | 2 | — | Age bracket 5: days-past-due threshold |
| 7 | BKCM_DUN_AGE_6 | INTEGER | 2 | — | Age bracket 6: days-past-due threshold |
| 8 | BKCM_DUN_AGE_7 | INTEGER | 2 | — | Age bracket 7: days-past-due threshold |
| 9 | BKCM_DUN_AGE_8 | INTEGER | 2 | — | Age bracket 8: days-past-due threshold |
| 10 | BKCM_DUN_AGE_9 | INTEGER | 2 | — | Age bracket 9: days-past-due threshold |
| 11 | BKCM_DUN_CNUM | INTEGER | 2 | — | Number of dunning brackets configured |
| 12 | BKCM_DUN_DESC_1 | STRING | 30 | — | Description / label for age bracket 1 |
| 13 | BKCM_DUN_DESC_10 | STRING | 30 | — | Description / label for age bracket 10 |
| 14 | BKCM_DUN_DESC_2 | STRING | 30 | — | Description / label for age bracket 2 |
| 15 | BKCM_DUN_DESC_3 | STRING | 30 | — | Description / label for age bracket 3 |
| 16 | BKCM_DUN_DESC_4 | STRING | 30 | — | Description / label for age bracket 4 |
| 17 | BKCM_DUN_DESC_5 | STRING | 30 | — | Description / label for age bracket 5 |
| 18 | BKCM_DUN_DESC_6 | STRING | 30 | — | Description / label for age bracket 6 |
| 19 | BKCM_DUN_DESC_7 | STRING | 30 | — | Description / label for age bracket 7 |
| 20 | BKCM_DUN_DESC_8 | STRING | 30 | — | Description / label for age bracket 8 |
| 21 | BKCM_DUN_DESC_9 | STRING | 30 | — | Description / label for age bracket 9 |
| 22 | BKCM_DUN_DORL | STRING | 1 | — | Trigger mode: `D`=dollar amount or `L`=letter age |
| 23 | BKCM_DUN_FORM_1 | STRING | 15 | — | Form letter template code for bracket 1 (FK → BKCMFORM) |
| 24 | BKCM_DUN_FORM_10 | STRING | 15 | — | Form letter template code for bracket 10 |
| 25 | BKCM_DUN_FORM_2 | STRING | 15 | — | Form letter template code for bracket 2 |
| 26 | BKCM_DUN_FORM_3 | STRING | 15 | — | Form letter template code for bracket 3 |
| 27 | BKCM_DUN_FORM_4 | STRING | 15 | — | Form letter template code for bracket 4 |
| 28 | BKCM_DUN_FORM_5 | STRING | 15 | — | Form letter template code for bracket 5 |
| 29 | BKCM_DUN_FORM_6 | STRING | 15 | — | Form letter template code for bracket 6 |
| 30 | BKCM_DUN_FORM_7 | STRING | 15 | — | Form letter template code for bracket 7 |
| 31 | BKCM_DUN_FORM_8 | STRING | 15 | — | Form letter template code for bracket 8 |
| 32 | BKCM_DUN_FORM_9 | STRING | 15 | — | Form letter template code for bracket 9 |
| 33 | BKCM_DUN_NUMUP | INTEGER | 2 | — | Number of aging periods / buckets |
| 34 | BKCM_DUN_PCONT | STRING | 1 | — | Print continuation flag |
| 35 | BKCM_DUN_REP | STRING | 5 | — | Rep Code (default rep for dunning run) |
| 36 | BKCM_DUN_SORT | STRING | 1 | — | Sort order flag |

## BKCMDUNH
**DUN LETTER HISTORY**

Fields: 6 | Key: BKCM_DUNH_ACCT + BKCM_DUNH_DATE

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKCM_DUNH_ACCT | STRING | 10 | — | Customer Account Code |
| 2 | BKCM_DUNH_AGE | INTEGER | 2 | — | Age bracket number sent |
| 3 | BKCM_DUNH_AMT | NUMERIC | 8 | 2 | Amount past-due when letter sent |
| 4 | BKCM_DUNH_DATE | DATE | 4 | — | Date letter was sent |
| 5 | BKCM_DUNH_FORM | STRING | 15 | — | Form template used |
| 6 | BKCM_DUNH_TOT | NUMERIC | 8 | 2 | Total balance when letter sent |

## BKCMFORM
**FORM & DUN LETTER TEMPLATE**

Fields: 8 | Key: BKCM_FORM_CODE + BKCM_FORM_LINE

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKCM_FORM_CODE | STRING | 15 | — | Form template code (PK) |
| 2 | BKCM_FORM_DESC | STRING | 30 | — | Template description |
| 3 | BKCM_FORM_DUN | STRING | 1 | — | Dunning Letter flag (`Y`=dunning letter) |
| 4 | BKCM_FORM_LEFT | INTEGER | 2 | — | Left justification position |
| 5 | BKCM_FORM_LINE | INTEGER | 2 | — | Line number within template (PK) |
| 6 | BKCM_FORM_LNSPG | INTEGER | 2 | — | Lines per page |
| 7 | BKCM_FORM_NOTE | STRING | 78 | — | Note / body text for this line of the letter |
| 8 | BKCM_FORM_START | INTEGER | 2 | — | Starting line number |

## BKISHTAX
**PAID SALES TAX DETAIL**

Fields: 13 | Key: BKIS_TAX_INVNO + BKIS_TAX_CODE

Identical 13-field BKIS_TAX_* schema to BKISTAX (open) and ISISATAX (archive).

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKIS_TAX_APINV | STRING | 10 | — | AP/AR invoice number cross-reference |
| 2 | BKIS_TAX_CODE | STRING | 10 | — | Tax code (FK → ISTAXFIL) |
| 3 | BKIS_TAX_CUST | STRING | 10 | — | Customer code (FK → BKARCUST) |
| 4 | BKIS_TAX_DATE | DATE | 4 | — | Tax transaction date |
| 5 | BKIS_TAX_INVNO | NUMERIC | 8 | — | Invoice number (FK → BKARINVT) |
| 6 | BKIS_TAX_ISCUR | STRING | 3 | — | Currency code |
| 7 | BKIS_TAX_NONTAX | NUMERIC | 8 | 2 | Non-taxable amount on this transaction |
| 8 | BKIS_TAX_PONO | NUMERIC | 8 | — | PO number (if associated with a sales invoice) |
| 9 | BKIS_TAX_TAG | STRING | 1 | — | Tax paid/remitted tag (`P`=paid) |
| 10 | BKIS_TAX_TAXABL | NUMERIC | 8 | 2 | Taxable amount |
| 11 | BKIS_TAX_TAXAMT | NUMERIC | 8 | 2 | Tax amount charged |
| 12 | BKIS_TAX_TRFLAG | STRING | 1 | — | Tax remitted/transferred flag |
| 13 | BKIS_TAX_VEND | STRING | 10 | — | Tax authority vendor code (FK → BKAPVEND) |

## BKISTAX
**SALES TAX DETAIL (OPEN)**

Fields: 13 | Key: BKIS_TAX_INVNO + BKIS_TAX_CODE

Identical schema to BKISHTAX above. See that table for all field definitions.

## BKSYAR
**AR DEFAULT MASTER**

Fields: 2 | Key: (single-row sequence counter table)

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKSY_AR_DEPNO | NUMERIC | 8 | — | Last deposit sequence number (auto-increment PK counter) |
| 2 | BKSY_AR_TRXN | NUMERIC | 8 | — | Last AR transaction sequence number (auto-increment counter) |

## CUSTCLAS
**CUSTOMER CLASS MASTER**

Fields: 2 | Key: MTCLASS_M_CLASS

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTCLASS_M_CLASS | STRING | 4 | — | Customer class code (PK) |
| 2 | MTCLASS_M_DESC | STRING | 30 | — | Customer class description |

## IS2DBAR
**2D BARCODE PARAMETERS**

Fields: 109 | Key: IS2D_BAR_CODE

Configuration for 2D barcode (e.g. QR/DataMatrix) printing on AR documents. Each record
defines one barcode profile; DOCPR_1..100 flags control which of up to 100 data elements
are included in the barcode payload.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS2D_BAR_ASCII | INTEGER | 2 | — | ASCII code of the barcode character |
| 2 | IS2D_BAR_CHAR | STRING | 5 | — | Character representation |
| 3 | IS2D_BAR_CODE | STRING | 10 | — | Barcode configuration code (PK) |
| 4 | IS2D_BAR_DESC | STRING | 60 | — | Configuration description |
| 5 | IS2D_BAR_DOCPR_1 | STRING | 1 | — | Include document data element 1 in barcode (`Y`=include) |
| 6 | IS2D_BAR_DOCPR_10 | STRING | 1 | — | Include document data element 10 |
| 7 | IS2D_BAR_DOCPR_100 | STRING | 1 | — | Include document data element 100 |
| 8 | IS2D_BAR_DOCPR_11 | STRING | 1 | — | Include document data element 11 |
| 9 | IS2D_BAR_DOCPR_12 | STRING | 1 | — | Include document data element 12 |
| 10 | IS2D_BAR_DOCPR_13 | STRING | 1 | — | Include document data element 13 |
| 11 | IS2D_BAR_DOCPR_14 | STRING | 1 | — | Include document data element 14 |
| 12 | IS2D_BAR_DOCPR_15 | STRING | 1 | — | Include document data element 15 |
| 13 | IS2D_BAR_DOCPR_16 | STRING | 1 | — | Include document data element 16 |
| 14 | IS2D_BAR_DOCPR_17 | STRING | 1 | — | Include document data element 17 |
| 15 | IS2D_BAR_DOCPR_18 | STRING | 1 | — | Include document data element 18 |
| 16 | IS2D_BAR_DOCPR_19 | STRING | 1 | — | Include document data element 19 |
| 17 | IS2D_BAR_DOCPR_2 | STRING | 1 | — | Include document data element 2 |
| 18 | IS2D_BAR_DOCPR_20 | STRING | 1 | — | Include document data element 20 |
| 19 | IS2D_BAR_DOCPR_21 | STRING | 1 | — | Include document data element 21 |
| 20 | IS2D_BAR_DOCPR_22 | STRING | 1 | — | Include document data element 22 |
| 21 | IS2D_BAR_DOCPR_23 | STRING | 1 | — | Include document data element 23 |
| 22 | IS2D_BAR_DOCPR_24 | STRING | 1 | — | Include document data element 24 |
| 23 | IS2D_BAR_DOCPR_25 | STRING | 1 | — | Include document data element 25 |
| 24 | IS2D_BAR_DOCPR_26 | STRING | 1 | — | Include document data element 26 |
| 25 | IS2D_BAR_DOCPR_27 | STRING | 1 | — | Include document data element 27 |
| 26 | IS2D_BAR_DOCPR_28 | STRING | 1 | — | Include document data element 28 |
| 27 | IS2D_BAR_DOCPR_29 | STRING | 1 | — | Include document data element 29 |
| 28 | IS2D_BAR_DOCPR_3 | STRING | 1 | — | Include document data element 3 |
| 29 | IS2D_BAR_DOCPR_30 | STRING | 1 | — | Include document data element 30 |
| 30 | IS2D_BAR_DOCPR_31 | STRING | 1 | — | Include document data element 31 |
| 31 | IS2D_BAR_DOCPR_32 | STRING | 1 | — | Include document data element 32 |
| 32 | IS2D_BAR_DOCPR_33 | STRING | 1 | — | Include document data element 33 |
| 33 | IS2D_BAR_DOCPR_34 | STRING | 1 | — | Include document data element 34 |
| 34 | IS2D_BAR_DOCPR_35 | STRING | 1 | — | Include document data element 35 |
| 35 | IS2D_BAR_DOCPR_36 | STRING | 1 | — | Include document data element 36 |
| 36 | IS2D_BAR_DOCPR_37 | STRING | 1 | — | Include document data element 37 |
| 37 | IS2D_BAR_DOCPR_38 | STRING | 1 | — | Include document data element 38 |
| 38 | IS2D_BAR_DOCPR_39 | STRING | 1 | — | Include document data element 39 |
| 39 | IS2D_BAR_DOCPR_4 | STRING | 1 | — | Include document data element 4 |
| 40 | IS2D_BAR_DOCPR_40 | STRING | 1 | — | Include document data element 40 |
| 41 | IS2D_BAR_DOCPR_41 | STRING | 1 | — | Include document data element 41 |
| 42 | IS2D_BAR_DOCPR_42 | STRING | 1 | — | Include document data element 42 |
| 43 | IS2D_BAR_DOCPR_43 | STRING | 1 | — | Include document data element 43 |
| 44 | IS2D_BAR_DOCPR_44 | STRING | 1 | — | Include document data element 44 |
| 45 | IS2D_BAR_DOCPR_45 | STRING | 1 | — | Include document data element 45 |
| 46 | IS2D_BAR_DOCPR_46 | STRING | 1 | — | Include document data element 46 |
| 47 | IS2D_BAR_DOCPR_47 | STRING | 1 | — | Include document data element 47 |
| 48 | IS2D_BAR_DOCPR_48 | STRING | 1 | — | Include document data element 48 |
| 49 | IS2D_BAR_DOCPR_49 | STRING | 1 | — | Include document data element 49 |
| 50 | IS2D_BAR_DOCPR_5 | STRING | 1 | — | Include document data element 5 |
| 51 | IS2D_BAR_DOCPR_50 | STRING | 1 | — | Include document data element 50 |
| 52 | IS2D_BAR_DOCPR_51 | STRING | 1 | — | Include document data element 51 |
| 53 | IS2D_BAR_DOCPR_52 | STRING | 1 | — | Include document data element 52 |
| 54 | IS2D_BAR_DOCPR_53 | STRING | 1 | — | Include document data element 53 |
| 55 | IS2D_BAR_DOCPR_54 | STRING | 1 | — | Include document data element 54 |
| 56 | IS2D_BAR_DOCPR_55 | STRING | 1 | — | Include document data element 55 |
| 57 | IS2D_BAR_DOCPR_56 | STRING | 1 | — | Include document data element 56 |
| 58 | IS2D_BAR_DOCPR_57 | STRING | 1 | — | Include document data element 57 |
| 59 | IS2D_BAR_DOCPR_58 | STRING | 1 | — | Include document data element 58 |
| 60 | IS2D_BAR_DOCPR_59 | STRING | 1 | — | Include document data element 59 |
| 61 | IS2D_BAR_DOCPR_6 | STRING | 1 | — | Include document data element 6 |
| 62 | IS2D_BAR_DOCPR_60 | STRING | 1 | — | Include document data element 60 |
| 63 | IS2D_BAR_DOCPR_61 | STRING | 1 | — | Include document data element 61 |
| 64 | IS2D_BAR_DOCPR_62 | STRING | 1 | — | Include document data element 62 |
| 65 | IS2D_BAR_DOCPR_63 | STRING | 1 | — | Include document data element 63 |
| 66 | IS2D_BAR_DOCPR_64 | STRING | 1 | — | Include document data element 64 |
| 67 | IS2D_BAR_DOCPR_65 | STRING | 1 | — | Include document data element 65 |
| 68 | IS2D_BAR_DOCPR_66 | STRING | 1 | — | Include document data element 66 |
| 69 | IS2D_BAR_DOCPR_67 | STRING | 1 | — | Include document data element 67 |
| 70 | IS2D_BAR_DOCPR_68 | STRING | 1 | — | Include document data element 68 |
| 71 | IS2D_BAR_DOCPR_69 | STRING | 1 | — | Include document data element 69 |
| 72 | IS2D_BAR_DOCPR_7 | STRING | 1 | — | Include document data element 7 |
| 73 | IS2D_BAR_DOCPR_70 | STRING | 1 | — | Include document data element 70 |
| 74 | IS2D_BAR_DOCPR_71 | STRING | 1 | — | Include document data element 71 |
| 75 | IS2D_BAR_DOCPR_72 | STRING | 1 | — | Include document data element 72 |
| 76 | IS2D_BAR_DOCPR_73 | STRING | 1 | — | Include document data element 73 |
| 77 | IS2D_BAR_DOCPR_74 | STRING | 1 | — | Include document data element 74 |
| 78 | IS2D_BAR_DOCPR_75 | STRING | 1 | — | Include document data element 75 |
| 79 | IS2D_BAR_DOCPR_76 | STRING | 1 | — | Include document data element 76 |
| 80 | IS2D_BAR_DOCPR_77 | STRING | 1 | — | Include document data element 77 |
| 81 | IS2D_BAR_DOCPR_78 | STRING | 1 | — | Include document data element 78 |
| 82 | IS2D_BAR_DOCPR_79 | STRING | 1 | — | Include document data element 79 |
| 83 | IS2D_BAR_DOCPR_8 | STRING | 1 | — | Include document data element 8 |
| 84 | IS2D_BAR_DOCPR_80 | STRING | 1 | — | Include document data element 80 |
| 85 | IS2D_BAR_DOCPR_81 | STRING | 1 | — | Include document data element 81 |
| 86 | IS2D_BAR_DOCPR_82 | STRING | 1 | — | Include document data element 82 |
| 87 | IS2D_BAR_DOCPR_83 | STRING | 1 | — | Include document data element 83 |
| 88 | IS2D_BAR_DOCPR_84 | STRING | 1 | — | Include document data element 84 |
| 89 | IS2D_BAR_DOCPR_85 | STRING | 1 | — | Include document data element 85 |
| 90 | IS2D_BAR_DOCPR_86 | STRING | 1 | — | Include document data element 86 |
| 91 | IS2D_BAR_DOCPR_87 | STRING | 1 | — | Include document data element 87 |
| 92 | IS2D_BAR_DOCPR_88 | STRING | 1 | — | Include document data element 88 |
| 93 | IS2D_BAR_DOCPR_89 | STRING | 1 | — | Include document data element 89 |
| 94 | IS2D_BAR_DOCPR_9 | STRING | 1 | — | Include document data element 9 |
| 95 | IS2D_BAR_DOCPR_90 | STRING | 1 | — | Include document data element 90 |
| 96 | IS2D_BAR_DOCPR_91 | STRING | 1 | — | Include document data element 91 |
| 97 | IS2D_BAR_DOCPR_92 | STRING | 1 | — | Include document data element 92 |
| 98 | IS2D_BAR_DOCPR_93 | STRING | 1 | — | Include document data element 93 |
| 99 | IS2D_BAR_DOCPR_94 | STRING | 1 | — | Include document data element 94 |
| 100 | IS2D_BAR_DOCPR_95 | STRING | 1 | — | Include document data element 95 |
| 101 | IS2D_BAR_DOCPR_96 | STRING | 1 | — | Include document data element 96 |
| 102 | IS2D_BAR_DOCPR_97 | STRING | 1 | — | Include document data element 97 |
| 103 | IS2D_BAR_DOCPR_98 | STRING | 1 | — | Include document data element 98 |
| 104 | IS2D_BAR_DOCPR_99 | STRING | 1 | — | Include document data element 99 |
| 105 | IS2D_BAR_EXTRA | STRING | 100 | — | Extra data |
| 106 | IS2D_BAR_FIELD | STRING | 25 | — | Source field name mapped to this barcode element |
| 107 | IS2D_BAR_ITEM | STRING | 15 | — | Item / part code association |
| 108 | IS2D_BAR_ORDER | INTEGER | 2 | — | Print sequence order |
| 109 | IS2D_BAR_TYPE | STRING | 10 | — | Barcode type (e.g. Code128, QR, DataMatrix) |

## ISARACHK
**ARCHIVED CUSTOMER PAYMENT HISTORY**

Fields: 12 | Key: BKAP_CHK_NUM + BKAP_CHK_INVNUM

Identical schema to BKARCHKF above. See that table for all field definitions.

## ISARACST
**ARCHIVED CUSTOMER MASTER**

Fields: 106 | Key: BKAR_CUSTCODE

Identical schema to BKARCUST above. See that table for all field definitions.

## ISARAHTX
**ARCHIVED SALES TAX**

Fields: 5 | Key: BKAR_TAX_INVNO + BKAR_TAX_CODE

Identical schema to BKARHTAX above. See that table for all field definitions.

## ISARAINT
**ARCHIVED CUSTOMER INVOICES**

Fields: 23 | Key: BKAR_INVT_NUM + BKAR_INVT_CODE

Identical schema to BKARINVT above. See that table for all field definitions.

## ISARAIVV
**ARCHIVED AR VOUCHERS**

Fields: 77 | Key: BKAR_INVV_NUM

Identical schema to BKARINVV above. See that table for all field definitions.

## ISARAT
**ARCHIVED TRANSACTION DETAIL**

Fields: 12 | Key: BKART_TRXN + BKART_CNTR

Identical schema to BKART above. See that table for all field definitions.

## ISARATNT
**ARCHIVED TRANSACTION NOTES**

Fields: 3 | Key: BKART_NOT_TRXN + BKART_NOT_CNTR

Identical schema to BKARTNOT above. See that table for all field definitions.

## ISAREX
**CUSTOMER EXTENSION**

Fields: 51 | Key: ISAREX_CUST

UDF extension record for BKARCUST — one record per customer, keyed by customer code.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISAREX_ALPHA_1 | STRING | 30 | — | User-defined alpha field 1 |
| 2 | ISAREX_ALPHA_2 | STRING | 30 | — | User-defined alpha field 2 |
| 3 | ISAREX_ALPHA_3 | STRING | 30 | — | User-defined alpha field 3 |
| 4 | ISAREX_ALPHA_4 | STRING | 30 | — | User-defined alpha field 4 |
| 5 | ISAREX_ALPHA_5 | STRING | 30 | — | User-defined alpha field 5 |
| 6 | ISAREX_CRT_FORM | STRING | 60 | — | Credit report form template name |
| 7 | ISAREX_CUST | STRING | 10 | — | Customer code (PK; FK → BKARCUST) |
| 8 | ISAREX_DATE_1 | DATE | 4 | — | User-defined date field 1 |
| 9 | ISAREX_DATE_2 | DATE | 4 | — | User-defined date field 2 |
| 10 | ISAREX_DATE_3 | DATE | 4 | — | User-defined date field 3 |
| 11 | ISAREX_DATE_4 | DATE | 4 | — | User-defined date field 4 |
| 12 | ISAREX_DATE_5 | DATE | 4 | — | User-defined date field 5 |
| 13 | ISAREX_EXTRA | STRING | 100 | — | Extra data |
| 14 | ISAREX_FLAG_1 | STRING | 1 | — | User-defined flag 1 |
| 15 | ISAREX_FLAG_10 | STRING | 1 | — | User-defined flag 10 |
| 16 | ISAREX_FLAG_2 | STRING | 1 | — | User-defined flag 2 |
| 17 | ISAREX_FLAG_3 | STRING | 1 | — | User-defined flag 3 |
| 18 | ISAREX_FLAG_4 | STRING | 1 | — | User-defined flag 4 |
| 19 | ISAREX_FLAG_5 | STRING | 1 | — | User-defined flag 5 |
| 20 | ISAREX_FLAG_6 | STRING | 1 | — | User-defined flag 6 |
| 21 | ISAREX_FLAG_7 | STRING | 1 | — | User-defined flag 7 |
| 22 | ISAREX_FLAG_8 | STRING | 1 | — | User-defined flag 8 |
| 23 | ISAREX_FLAG_9 | STRING | 1 | — | User-defined flag 9 |
| 24 | ISAREX_LONGNAME | STRING | 60 | — | Customer long name (extended 60-char name) |
| 25 | ISAREX_NUM2_1 | NUMERIC | 8 | — | User-defined integer field 1 |
| 26 | ISAREX_NUM2_2 | NUMERIC | 8 | — | User-defined integer field 2 |
| 27 | ISAREX_NUM2_3 | NUMERIC | 8 | — | User-defined integer field 3 |
| 28 | ISAREX_NUM2_4 | NUMERIC | 8 | — | User-defined integer field 4 |
| 29 | ISAREX_NUM2_5 | NUMERIC | 8 | — | User-defined integer field 5 |
| 30 | ISAREX_NUM_1 | NUMERIC | 8 | 2 | User-defined numeric field 1 |
| 31 | ISAREX_NUM_2 | NUMERIC | 8 | 2 | User-defined numeric field 2 |
| 32 | ISAREX_NUM_3 | NUMERIC | 8 | 2 | User-defined numeric field 3 |
| 33 | ISAREX_NUM_4 | NUMERIC | 8 | 2 | User-defined numeric field 4 |
| 34 | ISAREX_NUM_5 | NUMERIC | 8 | 2 | User-defined numeric field 5 |
| 35 | ISAREX_RS_EXPDT | DATE | 4 | — | Resale certificate expiration date |
| 36 | ISAREX_RS_FORM | STRING | 60 | — | Resale certificate form number / reference |
| 37 | ISAREX_RS_SGNDT | DATE | 4 | — | Resale certificate signed date |
| 38 | ISAREX_RS_UPDT | DATE | 4 | — | Resale certificate last updated date |
| 39 | ISAREX_RS_WHO | STRING | 15 | — | User who last updated the resale certificate |
| 40 | ISAREX_SLS_GOAL_1 | NUMERIC | 8 | 2 | Monthly sales goal — January |
| 41 | ISAREX_SLS_GOAL_10 | NUMERIC | 8 | 2 | Monthly sales goal — October |
| 42 | ISAREX_SLS_GOAL_11 | NUMERIC | 8 | 2 | Monthly sales goal — November |
| 43 | ISAREX_SLS_GOAL_12 | NUMERIC | 8 | 2 | Monthly sales goal — December |
| 44 | ISAREX_SLS_GOAL_2 | NUMERIC | 8 | 2 | Monthly sales goal — February |
| 45 | ISAREX_SLS_GOAL_3 | NUMERIC | 8 | 2 | Monthly sales goal — March |
| 46 | ISAREX_SLS_GOAL_4 | NUMERIC | 8 | 2 | Monthly sales goal — April |
| 47 | ISAREX_SLS_GOAL_5 | NUMERIC | 8 | 2 | Monthly sales goal — May |
| 48 | ISAREX_SLS_GOAL_6 | NUMERIC | 8 | 2 | Monthly sales goal — June |
| 49 | ISAREX_SLS_GOAL_7 | NUMERIC | 8 | 2 | Monthly sales goal — July |
| 50 | ISAREX_SLS_GOAL_8 | NUMERIC | 8 | 2 | Monthly sales goal — August |
| 51 | ISAREX_SLS_GOAL_9 | NUMERIC | 8 | 2 | Monthly sales goal — September |

## ISCC
**CREDIT CARD LISTING**

Fields: 13 | Key: IS_CC_CODE

Tokenized credit card records for customer accounts (PCI-compliant — actual card number not stored).

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_CC_ADDRESS | STRING | 40 | — | Billing address for card verification |
| 2 | IS_CC_CARDNAME | STRING | 25 | — | Cardholder name as it appears on card |
| 3 | IS_CC_CARDTYPE | STRING | 15 | — | Card type (Visa, MC, Amex, etc.) |
| 4 | IS_CC_CODE | STRING | 10 | — | Credit card record code (PK; often customer code) |
| 5 | IS_CC_EXP | STRING | 4 | — | Expiration date in MMYY format |
| 6 | IS_CC_EXTRA | STRING | 100 | — | Extra data |
| 7 | IS_CC_MASKED | STRING | 24 | — | Masked card number (PCI-compliant truncated display) |
| 8 | IS_CC_SORT | NUMERIC | 8 | — | Display sort order |
| 9 | IS_CC_STATUS | STRING | 25 | — | Card status (active, expired, declined, etc.) |
| 10 | IS_CC_STDATE | DATE | 4 | — | Card start date |
| 11 | IS_CC_TOLKEN | STRING | 20 | — | Payment processor token (note: TOLKEN = typo for TOKEN) |
| 12 | IS_CC_XCTRAN | STRING | 10 | — | Cross-reference to last payment transaction record |
| 13 | IS_CC_ZIP | STRING | 10 | — | Billing ZIP code for card verification |

## ISISATAX
**ARCHIVE SALES TAX**

Fields: 13 | Key: BKIS_TAX_INVNO + BKIS_TAX_CODE

Identical schema to BKISHTAX above. See that table for all field definitions.

## ISTAXFIL
**TAX CODES**

Fields: 84 | Key: ISIS_TXF_CODE

Tax code master — up to 9 tiered tax brackets each for PO (purchase/AP) and SO (sales/AR) sides.
POHRNG/POLRNG define bracket bounds; POPERC defines rate for each bracket.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISIS_TXF_CODE | STRING | 10 | — | Tax code (PK) |
| 2 | ISIS_TXF_DESC | STRING | 30 | — | Tax code description |
| 3 | ISIS_TXF_GLAPO | STRING | 10 | — | GL account for AP/PO tax postings |
| 4 | ISIS_TXF_GLASO | STRING | 10 | — | GL account for AR/SO tax postings |
| 5 | ISIS_TXF_GLDPO | STRING | 4 | — | GL department for PO tax |
| 6 | ISIS_TXF_GLDSO | STRING | 4 | — | GL department for SO tax |
| 7 | ISIS_TXF_IDNUM | STRING | 15 | — | Tax authority registration / ID number |
| 8 | ISIS_TXF_ISCUR | STRING | 3 | — | Currency code |
| 9 | ISIS_TXF_POHRNG_1 | NUMERIC | 8 | 2 | PO bracket 1: taxable amount upper bound |
| 10 | ISIS_TXF_POHRNG_2 | NUMERIC | 8 | 2 | PO bracket 2: taxable amount upper bound |
| 11 | ISIS_TXF_POHRNG_3 | NUMERIC | 8 | 2 | PO bracket 3: taxable amount upper bound |
| 12 | ISIS_TXF_POHRNG_4 | NUMERIC | 8 | 2 | PO bracket 4: taxable amount upper bound |
| 13 | ISIS_TXF_POHRNG_5 | NUMERIC | 8 | 2 | PO bracket 5: taxable amount upper bound |
| 14 | ISIS_TXF_POHRNG_6 | NUMERIC | 8 | 2 | PO bracket 6: taxable amount upper bound |
| 15 | ISIS_TXF_POHRNG_7 | NUMERIC | 8 | 2 | PO bracket 7: taxable amount upper bound |
| 16 | ISIS_TXF_POHRNG_8 | NUMERIC | 8 | 2 | PO bracket 8: taxable amount upper bound |
| 17 | ISIS_TXF_POHRNG_9 | NUMERIC | 8 | 2 | PO bracket 9: taxable amount upper bound |
| 18 | ISIS_TXF_POLRNG_1 | NUMERIC | 8 | 2 | PO bracket 1: taxable amount lower bound |
| 19 | ISIS_TXF_POLRNG_2 | NUMERIC | 8 | 2 | PO bracket 2: taxable amount lower bound |
| 20 | ISIS_TXF_POLRNG_3 | NUMERIC | 8 | 2 | PO bracket 3: taxable amount lower bound |
| 21 | ISIS_TXF_POLRNG_4 | NUMERIC | 8 | 2 | PO bracket 4: taxable amount lower bound |
| 22 | ISIS_TXF_POLRNG_5 | NUMERIC | 8 | 2 | PO bracket 5: taxable amount lower bound |
| 23 | ISIS_TXF_POLRNG_6 | NUMERIC | 8 | 2 | PO bracket 6: taxable amount lower bound |
| 24 | ISIS_TXF_POLRNG_7 | NUMERIC | 8 | 2 | PO bracket 7: taxable amount lower bound |
| 25 | ISIS_TXF_POLRNG_8 | NUMERIC | 8 | 2 | PO bracket 8: taxable amount lower bound |
| 26 | ISIS_TXF_POLRNG_9 | NUMERIC | 8 | 2 | PO bracket 9: taxable amount lower bound |
| 27 | ISIS_TXF_POMAX | NUMERIC | 8 | 2 | PO maximum taxable amount cap |
| 28 | ISIS_TXF_POPERC_1 | NUMERIC | 8 | 3 | PO tax rate percentage for bracket 1 |
| 29 | ISIS_TXF_POPERC_2 | NUMERIC | 8 | 3 | PO tax rate percentage for bracket 2 |
| 30 | ISIS_TXF_POPERC_3 | NUMERIC | 8 | 3 | PO tax rate percentage for bracket 3 |
| 31 | ISIS_TXF_POPERC_4 | NUMERIC | 8 | 3 | PO tax rate percentage for bracket 4 |
| 32 | ISIS_TXF_POPERC_5 | NUMERIC | 8 | 3 | PO tax rate percentage for bracket 5 |
| 33 | ISIS_TXF_POPERC_6 | NUMERIC | 8 | 3 | PO tax rate percentage for bracket 6 |
| 34 | ISIS_TXF_POPERC_7 | NUMERIC | 8 | 3 | PO tax rate percentage for bracket 7 |
| 35 | ISIS_TXF_POPERC_8 | NUMERIC | 8 | 3 | PO tax rate percentage for bracket 8 |
| 36 | ISIS_TXF_POPERC_9 | NUMERIC | 8 | 3 | PO tax rate percentage for bracket 9 |
| 37 | ISIS_TXF_PTICD_1 | STRING | 1 | — | PO tier code for bracket 1 (compound/included indicator) |
| 38 | ISIS_TXF_PTICD_2 | STRING | 1 | — | PO tier code for bracket 2 |
| 39 | ISIS_TXF_PTICD_3 | STRING | 1 | — | PO tier code for bracket 3 |
| 40 | ISIS_TXF_PTICD_4 | STRING | 1 | — | PO tier code for bracket 4 |
| 41 | ISIS_TXF_PTICD_5 | STRING | 1 | — | PO tier code for bracket 5 |
| 42 | ISIS_TXF_PTICD_6 | STRING | 1 | — | PO tier code for bracket 6 |
| 43 | ISIS_TXF_PTICD_7 | STRING | 1 | — | PO tier code for bracket 7 |
| 44 | ISIS_TXF_PTICD_8 | STRING | 1 | — | PO tier code for bracket 8 |
| 45 | ISIS_TXF_PTICD_9 | STRING | 1 | — | PO tier code for bracket 9 |
| 46 | ISIS_TXF_SOHRNG_1 | NUMERIC | 8 | 2 | SO bracket 1: taxable amount upper bound |
| 47 | ISIS_TXF_SOHRNG_2 | NUMERIC | 8 | 2 | SO bracket 2: taxable amount upper bound |
| 48 | ISIS_TXF_SOHRNG_3 | NUMERIC | 8 | 2 | SO bracket 3: taxable amount upper bound |
| 49 | ISIS_TXF_SOHRNG_4 | NUMERIC | 8 | 2 | SO bracket 4: taxable amount upper bound |
| 50 | ISIS_TXF_SOHRNG_5 | NUMERIC | 8 | 2 | SO bracket 5: taxable amount upper bound |
| 51 | ISIS_TXF_SOHRNG_6 | NUMERIC | 8 | 2 | SO bracket 6: taxable amount upper bound |
| 52 | ISIS_TXF_SOHRNG_7 | NUMERIC | 8 | 2 | SO bracket 7: taxable amount upper bound |
| 53 | ISIS_TXF_SOHRNG_8 | NUMERIC | 8 | 2 | SO bracket 8: taxable amount upper bound |
| 54 | ISIS_TXF_SOHRNG_9 | NUMERIC | 8 | 2 | SO bracket 9: taxable amount upper bound |
| 55 | ISIS_TXF_SOLRNG_1 | NUMERIC | 8 | 2 | SO bracket 1: taxable amount lower bound |
| 56 | ISIS_TXF_SOLRNG_2 | NUMERIC | 8 | 2 | SO bracket 2: taxable amount lower bound |
| 57 | ISIS_TXF_SOLRNG_3 | NUMERIC | 8 | 2 | SO bracket 3: taxable amount lower bound |
| 58 | ISIS_TXF_SOLRNG_4 | NUMERIC | 8 | 2 | SO bracket 4: taxable amount lower bound |
| 59 | ISIS_TXF_SOLRNG_5 | NUMERIC | 8 | 2 | SO bracket 5: taxable amount lower bound |
| 60 | ISIS_TXF_SOLRNG_6 | NUMERIC | 8 | 2 | SO bracket 6: taxable amount lower bound |
| 61 | ISIS_TXF_SOLRNG_7 | NUMERIC | 8 | 2 | SO bracket 7: taxable amount lower bound |
| 62 | ISIS_TXF_SOLRNG_8 | NUMERIC | 8 | 2 | SO bracket 8: taxable amount lower bound |
| 63 | ISIS_TXF_SOLRNG_9 | NUMERIC | 8 | 2 | SO bracket 9: taxable amount lower bound |
| 64 | ISIS_TXF_SOMAX | NUMERIC | 8 | 2 | SO maximum taxable amount cap |
| 65 | ISIS_TXF_SOPERC_1 | NUMERIC | 8 | 3 | SO tax rate percentage for bracket 1 |
| 66 | ISIS_TXF_SOPERC_2 | NUMERIC | 8 | 3 | SO tax rate percentage for bracket 2 |
| 67 | ISIS_TXF_SOPERC_3 | NUMERIC | 8 | 3 | SO tax rate percentage for bracket 3 |
| 68 | ISIS_TXF_SOPERC_4 | NUMERIC | 8 | 3 | SO tax rate percentage for bracket 4 |
| 69 | ISIS_TXF_SOPERC_5 | NUMERIC | 8 | 3 | SO tax rate percentage for bracket 5 |
| 70 | ISIS_TXF_SOPERC_6 | NUMERIC | 8 | 3 | SO tax rate percentage for bracket 6 |
| 71 | ISIS_TXF_SOPERC_7 | NUMERIC | 8 | 3 | SO tax rate percentage for bracket 7 |
| 72 | ISIS_TXF_SOPERC_8 | NUMERIC | 8 | 3 | SO tax rate percentage for bracket 8 |
| 73 | ISIS_TXF_SOPERC_9 | NUMERIC | 8 | 3 | SO tax rate percentage for bracket 9 |
| 74 | ISIS_TXF_TAXIN | STRING | 1 | — | Tax-included flag (`Y`=price includes tax) |
| 75 | ISIS_TXF_TICD_1 | STRING | 1 | — | SO tier code for bracket 1 (compound/included indicator) |
| 76 | ISIS_TXF_TICD_2 | STRING | 1 | — | SO tier code for bracket 2 |
| 77 | ISIS_TXF_TICD_3 | STRING | 1 | — | SO tier code for bracket 3 |
| 78 | ISIS_TXF_TICD_4 | STRING | 1 | — | SO tier code for bracket 4 |
| 79 | ISIS_TXF_TICD_5 | STRING | 1 | — | SO tier code for bracket 5 |
| 80 | ISIS_TXF_TICD_6 | STRING | 1 | — | SO tier code for bracket 6 |
| 81 | ISIS_TXF_TICD_7 | STRING | 1 | — | SO tier code for bracket 7 |
| 82 | ISIS_TXF_TICD_8 | STRING | 1 | — | SO tier code for bracket 8 |
| 83 | ISIS_TXF_TICD_9 | STRING | 1 | — | SO tier code for bracket 9 |
| 84 | ISIS_TXF_VNDCD | STRING | 10 | — | Tax authority vendor code (FK → BKAPVEND) |

## ISTAXGRP
**TAX GROUPS**

Fields: 105 | Key: ISIS_TXG_NAME

Tax group — assigns up to 9 tax jurisdiction codes to a named group; accumulates monthly
collected/taxable/non-taxable amounts. Referenced by customer and order tax group fields.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISIS_TXG_CODE_1 | STRING | 10 | — | Tax code for jurisdiction slot 1 (FK → ISTAXFIL) |
| 2 | ISIS_TXG_CODE_2 | STRING | 10 | — | Tax code for jurisdiction slot 2 |
| 3 | ISIS_TXG_CODE_3 | STRING | 10 | — | Tax code for jurisdiction slot 3 |
| 4 | ISIS_TXG_CODE_4 | STRING | 10 | — | Tax code for jurisdiction slot 4 |
| 5 | ISIS_TXG_CODE_5 | STRING | 10 | — | Tax code for jurisdiction slot 5 |
| 6 | ISIS_TXG_CODE_6 | STRING | 10 | — | Tax code for jurisdiction slot 6 |
| 7 | ISIS_TXG_CODE_7 | STRING | 10 | — | Tax code for jurisdiction slot 7 |
| 8 | ISIS_TXG_CODE_8 | STRING | 10 | — | Tax code for jurisdiction slot 8 |
| 9 | ISIS_TXG_CODE_9 | STRING | 10 | — | Tax code for jurisdiction slot 9 |
| 10 | ISIS_TXG_COLECT_1 | NUMERIC | 8 | 2 | Tax collected in January |
| 11 | ISIS_TXG_COLECT_10 | NUMERIC | 8 | 2 | Tax collected in October |
| 12 | ISIS_TXG_COLECT_11 | NUMERIC | 8 | 2 | Tax collected in November |
| 13 | ISIS_TXG_COLECT_12 | NUMERIC | 8 | 2 | Tax collected in December |
| 14 | ISIS_TXG_COLECT_2 | NUMERIC | 8 | 2 | Tax collected in February |
| 15 | ISIS_TXG_COLECT_3 | NUMERIC | 8 | 2 | Tax collected in March |
| 16 | ISIS_TXG_COLECT_4 | NUMERIC | 8 | 2 | Tax collected in April |
| 17 | ISIS_TXG_COLECT_5 | NUMERIC | 8 | 2 | Tax collected in May |
| 18 | ISIS_TXG_COLECT_6 | NUMERIC | 8 | 2 | Tax collected in June |
| 19 | ISIS_TXG_COLECT_7 | NUMERIC | 8 | 2 | Tax collected in July |
| 20 | ISIS_TXG_COLECT_8 | NUMERIC | 8 | 2 | Tax collected in August |
| 21 | ISIS_TXG_COLECT_9 | NUMERIC | 8 | 2 | Tax collected in September |
| 22 | ISIS_TXG_DESC | STRING | 30 | — | Tax group description |
| 23 | ISIS_TXG_DESCF_1 | STRING | 20 | — | Description label for jurisdiction slot 1 |
| 24 | ISIS_TXG_DESCF_2 | STRING | 20 | — | Description label for jurisdiction slot 2 |
| 25 | ISIS_TXG_DESCF_3 | STRING | 20 | — | Description label for jurisdiction slot 3 |
| 26 | ISIS_TXG_DESCF_4 | STRING | 20 | — | Description label for jurisdiction slot 4 |
| 27 | ISIS_TXG_DESCF_5 | STRING | 20 | — | Description label for jurisdiction slot 5 |
| 28 | ISIS_TXG_DESCF_6 | STRING | 20 | — | Description label for jurisdiction slot 6 |
| 29 | ISIS_TXG_DESCF_7 | STRING | 20 | — | Description label for jurisdiction slot 7 |
| 30 | ISIS_TXG_DESCF_8 | STRING | 20 | — | Description label for jurisdiction slot 8 |
| 31 | ISIS_TXG_DESCF_9 | STRING | 20 | — | Description label for jurisdiction slot 9 |
| 32 | ISIS_TXG_FREIGT | STRING | 1 | — | Apply this tax group to freight (global flag; `Y`=taxable freight) |
| 33 | ISIS_TXG_FRGT_1 | STRING | 1 | — | Apply freight tax for jurisdiction slot 1 |
| 34 | ISIS_TXG_FRGT_2 | STRING | 1 | — | Apply freight tax for jurisdiction slot 2 |
| 35 | ISIS_TXG_FRGT_3 | STRING | 1 | — | Apply freight tax for jurisdiction slot 3 |
| 36 | ISIS_TXG_FRGT_4 | STRING | 1 | — | Apply freight tax for jurisdiction slot 4 |
| 37 | ISIS_TXG_FRGT_5 | STRING | 1 | — | Apply freight tax for jurisdiction slot 5 |
| 38 | ISIS_TXG_FRGT_6 | STRING | 1 | — | Apply freight tax for jurisdiction slot 6 |
| 39 | ISIS_TXG_FRGT_7 | STRING | 1 | — | Apply freight tax for jurisdiction slot 7 |
| 40 | ISIS_TXG_FRGT_8 | STRING | 1 | — | Apply freight tax for jurisdiction slot 8 |
| 41 | ISIS_TXG_FRGT_9 | STRING | 1 | — | Apply freight tax for jurisdiction slot 9 |
| 42 | ISIS_TXG_IDC_1 | STRING | 15 | — | Tax ID code for jurisdiction slot 1 |
| 43 | ISIS_TXG_IDC_2 | STRING | 15 | — | Tax ID code for jurisdiction slot 2 |
| 44 | ISIS_TXG_IDC_3 | STRING | 15 | — | Tax ID code for jurisdiction slot 3 |
| 45 | ISIS_TXG_IDC_4 | STRING | 15 | — | Tax ID code for jurisdiction slot 4 |
| 46 | ISIS_TXG_IDC_5 | STRING | 15 | — | Tax ID code for jurisdiction slot 5 |
| 47 | ISIS_TXG_IDC_6 | STRING | 15 | — | Tax ID code for jurisdiction slot 6 |
| 48 | ISIS_TXG_IDC_7 | STRING | 15 | — | Tax ID code for jurisdiction slot 7 |
| 49 | ISIS_TXG_IDC_8 | STRING | 15 | — | Tax ID code for jurisdiction slot 8 |
| 50 | ISIS_TXG_IDC_9 | STRING | 15 | — | Tax ID code for jurisdiction slot 9 |
| 51 | ISIS_TXG_NAME | STRING | 10 | — | Tax group name / code (PK) |
| 52 | ISIS_TXG_NONTAX_1 | NUMERIC | 8 | 2 | Non-taxable amount accumulated in January |
| 53 | ISIS_TXG_NONTAX_10 | NUMERIC | 8 | 2 | Non-taxable amount accumulated in October |
| 54 | ISIS_TXG_NONTAX_11 | NUMERIC | 8 | 2 | Non-taxable amount accumulated in November |
| 55 | ISIS_TXG_NONTAX_12 | NUMERIC | 8 | 2 | Non-taxable amount accumulated in December |
| 56 | ISIS_TXG_NONTAX_2 | NUMERIC | 8 | 2 | Non-taxable amount accumulated in February |
| 57 | ISIS_TXG_NONTAX_3 | NUMERIC | 8 | 2 | Non-taxable amount accumulated in March |
| 58 | ISIS_TXG_NONTAX_4 | NUMERIC | 8 | 2 | Non-taxable amount accumulated in April |
| 59 | ISIS_TXG_NONTAX_5 | NUMERIC | 8 | 2 | Non-taxable amount accumulated in May |
| 60 | ISIS_TXG_NONTAX_6 | NUMERIC | 8 | 2 | Non-taxable amount accumulated in June |
| 61 | ISIS_TXG_NONTAX_7 | NUMERIC | 8 | 2 | Non-taxable amount accumulated in July |
| 62 | ISIS_TXG_NONTAX_8 | NUMERIC | 8 | 2 | Non-taxable amount accumulated in August |
| 63 | ISIS_TXG_NONTAX_9 | NUMERIC | 8 | 2 | Non-taxable amount accumulated in September |
| 64 | ISIS_TXG_OUTSTD | NUMERIC | 8 | 2 | Outstanding (unremitted) tax total |
| 65 | ISIS_TXG_PERCC_1 | NUMERIC | 8 | 3 | Tax percent collected for jurisdiction slot 1 |
| 66 | ISIS_TXG_PERCC_2 | NUMERIC | 8 | 3 | Tax percent collected for jurisdiction slot 2 |
| 67 | ISIS_TXG_PERCC_3 | NUMERIC | 8 | 3 | Tax percent collected for jurisdiction slot 3 |
| 68 | ISIS_TXG_PERCC_4 | NUMERIC | 8 | 3 | Tax percent collected for jurisdiction slot 4 |
| 69 | ISIS_TXG_PERCC_5 | NUMERIC | 8 | 3 | Tax percent collected for jurisdiction slot 5 |
| 70 | ISIS_TXG_PERCC_6 | NUMERIC | 8 | 3 | Tax percent collected for jurisdiction slot 6 |
| 71 | ISIS_TXG_PERCC_7 | NUMERIC | 8 | 3 | Tax percent collected for jurisdiction slot 7 |
| 72 | ISIS_TXG_PERCC_8 | NUMERIC | 8 | 3 | Tax percent collected for jurisdiction slot 8 |
| 73 | ISIS_TXG_PERCC_9 | NUMERIC | 8 | 3 | Tax percent collected for jurisdiction slot 9 |
| 74 | ISIS_TXG_PID_1 | STRING | 1 | — | Percent-included/compound flag for slot 1 |
| 75 | ISIS_TXG_PID_2 | STRING | 1 | — | Percent-included/compound flag for slot 2 |
| 76 | ISIS_TXG_PID_3 | STRING | 1 | — | Percent-included/compound flag for slot 3 |
| 77 | ISIS_TXG_PID_4 | STRING | 1 | — | Percent-included/compound flag for slot 4 |
| 78 | ISIS_TXG_PID_5 | STRING | 1 | — | Percent-included/compound flag for slot 5 |
| 79 | ISIS_TXG_PID_6 | STRING | 1 | — | Percent-included/compound flag for slot 6 |
| 80 | ISIS_TXG_PID_7 | STRING | 1 | — | Percent-included/compound flag for slot 7 |
| 81 | ISIS_TXG_PID_8 | STRING | 1 | — | Percent-included/compound flag for slot 8 |
| 82 | ISIS_TXG_PID_9 | STRING | 1 | — | Percent-included/compound flag for slot 9 |
| 83 | ISIS_TXG_TAXBLE_1 | NUMERIC | 8 | 2 | Taxable amount accumulated in January |
| 84 | ISIS_TXG_TAXBLE_10 | NUMERIC | 8 | 2 | Taxable amount accumulated in October |
| 85 | ISIS_TXG_TAXBLE_11 | NUMERIC | 8 | 2 | Taxable amount accumulated in November |
| 86 | ISIS_TXG_TAXBLE_12 | NUMERIC | 8 | 2 | Taxable amount accumulated in December |
| 87 | ISIS_TXG_TAXBLE_2 | NUMERIC | 8 | 2 | Taxable amount accumulated in February |
| 88 | ISIS_TXG_TAXBLE_3 | NUMERIC | 8 | 2 | Taxable amount accumulated in March |
| 89 | ISIS_TXG_TAXBLE_4 | NUMERIC | 8 | 2 | Taxable amount accumulated in April |
| 90 | ISIS_TXG_TAXBLE_5 | NUMERIC | 8 | 2 | Taxable amount accumulated in May |
| 91 | ISIS_TXG_TAXBLE_6 | NUMERIC | 8 | 2 | Taxable amount accumulated in June |
| 92 | ISIS_TXG_TAXBLE_7 | NUMERIC | 8 | 2 | Taxable amount accumulated in July |
| 93 | ISIS_TXG_TAXBLE_8 | NUMERIC | 8 | 2 | Taxable amount accumulated in August |
| 94 | ISIS_TXG_TAXBLE_9 | NUMERIC | 8 | 2 | Taxable amount accumulated in September |
| 95 | ISIS_TXG_TAXON_1 | STRING | 1 | — | Taxable indicator for slot 1 (`Y`=taxable) |
| 96 | ISIS_TXG_TAXON_2 | STRING | 1 | — | Taxable indicator for slot 2 |
| 97 | ISIS_TXG_TAXON_3 | STRING | 1 | — | Taxable indicator for slot 3 |
| 98 | ISIS_TXG_TAXON_4 | STRING | 1 | — | Taxable indicator for slot 4 |
| 99 | ISIS_TXG_TAXON_5 | STRING | 1 | — | Taxable indicator for slot 5 |
| 100 | ISIS_TXG_TAXON_6 | STRING | 1 | — | Taxable indicator for slot 6 |
| 101 | ISIS_TXG_TAXON_7 | STRING | 1 | — | Taxable indicator for slot 7 |
| 102 | ISIS_TXG_TAXON_8 | STRING | 1 | — | Taxable indicator for slot 8 |
| 103 | ISIS_TXG_TAXON_9 | STRING | 1 | — | Taxable indicator for slot 9 |
| 104 | ISIS_TXG_TOFPER | NUMERIC | 8 | 3 | Total of percentages from all active jurisdictions |
| 105 | ISIS_TXG_TOTPER | NUMERIC | 8 | 3 | Effective combined tax rate percentage |

## MKECLASS
**AR CUSTOMER CHECK CROSS REFERENCE**

Fields: 3 | Key: MKECLASS_NUM

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MKECLASS_ACTIVE | STRING | 1 | — | Active flag (`Y`=class is active) |
| 2 | MKECLASS_DESC | STRING | 45 | — | Class description |
| 3 | MKECLASS_NUM | NUMERIC | 8 | — | Class number (PK) |

**Confidence: 75/100** — Customer master core fields (address, contacts, terms, tax group,
salesperson, sales figures) confirmed from standard AR context; BKARINVT transaction type codes
O/P/A and CLOSD/OPEND date semantics inferred from AR aging conventions; BKARINVV GL
distribution arrays (DAMT/DC/GLACT/GLDPT/GLD × 10) confirmed from pattern; ISTAXFIL 9-bracket
tiered tax logic confirmed from field-name structure (HRNG/LRNG/PERC per PO/SO side); ISTAXGRP
12-month accumulator arrays confirmed from pattern; IS2DBAR DOCPR_1..100 element-selection
flags inferred from array pattern; exact type codes and flag values require RWN decryption.
