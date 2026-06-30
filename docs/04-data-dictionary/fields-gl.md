# GL — General Ledger: Field Reference

Status: verified-schema

Source: `Evo-DBA_File_Fields 052421.xlsx`, sheet "Fields".
Field descriptions where provided by source; otherwise name-inferred.

---

## BKGLACHK
**ARCHIVED CHECK REGISTER**

Fields: 11

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKGL_CHK_AMT | NUMERIC | 8 | 2 | Amount |
| 2 | BKGL_CHK_CHKACT | INTEGER | 2 | — | Checking Accoun Num |
| 3 | BKGL_CHK_CUST | STRING | 10 | — | — |
| 4 | BKGL_CHK_DATE | DATE | 4 | — | Date |
| 5 | BKGL_CHK_DATER | DATE | 4 | — | — |
| 6 | BKGL_CHK_EXTRA | STRING | 100 | — | — |
| 7 | BKGL_CHK_FLAG | STRING | 1 | — | Reconciled Y/N |
| 8 | BKGL_CHK_NAME | STRING | 25 | — | Pay to Name |
| 9 | BKGL_CHK_NUM | NUMERIC | 8 | — | Check Number |
| 10 | BKGL_CHK_TYPE | STRING | 1 | — | Type |
| 11 | BKGL_CHK_VEND | STRING | 10 | — | — |

## BKGLAGJL
**ARCHIVED GJ LINES**

Fields: 9

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKGL_GJL_ACCTNM | STRING | 10 | — | GL Account Number |
| 2 | BKGL_GJL_AMOUNT | NUMERIC | 8 | 2 | Amount |
| 3 | BKGL_GJL_DC | STRING | 1 | — | Debit/Credit |
| 4 | BKGL_GJL_DESC | STRING | 25 | — | GL Description |
| 5 | BKGL_GJL_EXTRA | STRING | 50 | — | — |
| 6 | BKGL_GJL_GLDPT | STRING | 4 | — | GL Department |
| 7 | BKGL_GJL_JOB | STRING | 15 | — | — |
| 8 | BKGL_GJL_LINE | INTEGER | 2 | — | — |
| 9 | BKGL_GJL_TRANSN | NUMERIC | 8 | — | Gen Journal Transaction Number |

## BKGLAGJR
**ARCHIVED GJ HEADER**

Fields: 11

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKGL_GJ_CHKACT | INTEGER | 2 | — | Checking Account |
| 2 | BKGL_GJ_CVCODE | STRING | 10 | — | GJ Transaction Code |
| 3 | BKGL_GJ_EXTRA | STRING | 50 | — | — |
| 4 | BKGL_GJ_INVCHKN | NUMERIC | 8 | — | Check Number |
| 5 | BKGL_GJ_JOB | STRING | 15 | — | — |
| 6 | BKGL_GJ_NUMLNES | INTEGER | 2 | — | Number of Lines |
| 7 | BKGL_GJ_POSTED | STRING | 1 | — | Posted Y/N |
| 8 | BKGL_GJ_TRANSDT | DATE | 4 | — | Transaction Date |
| 9 | BKGL_GJ_TRANSNM | NUMERIC | 8 | — | Transaction Number |
| 10 | BKGL_GJ_TYPE | STRING | 2 | — | Type |
| 11 | BKGL_GJ_TYPEN | INTEGER | 2 | — | Type Number |

## BKGLATRN
**ARCHIVED GL TXT (NOT USED)**

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

## BKGLCCOA
**CONSOLIDATED CHART OF ACCOUNTS (Temporary)**

Fields: 62

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKGLC_1YPAST_1 | NUMERIC | 8 | 2 | — |
| 2 | BKGLC_1YPAST_10 | NUMERIC | 8 | 2 | — |
| 3 | BKGLC_1YPAST_11 | NUMERIC | 8 | 2 | — |
| 4 | BKGLC_1YPAST_12 | NUMERIC | 8 | 2 | — |
| 5 | BKGLC_1YPAST_13 | NUMERIC | 8 | 2 | — |
| 6 | BKGLC_1YPAST_14 | NUMERIC | 8 | 2 | — |
| 7 | BKGLC_1YPAST_2 | NUMERIC | 8 | 2 | — |
| 8 | BKGLC_1YPAST_3 | NUMERIC | 8 | 2 | — |
| 9 | BKGLC_1YPAST_4 | NUMERIC | 8 | 2 | — |
| 10 | BKGLC_1YPAST_5 | NUMERIC | 8 | 2 | — |
| 11 | BKGLC_1YPAST_6 | NUMERIC | 8 | 2 | — |
| 12 | BKGLC_1YPAST_7 | NUMERIC | 8 | 2 | — |
| 13 | BKGLC_1YPAST_8 | NUMERIC | 8 | 2 | — |
| 14 | BKGLC_1YPAST_9 | NUMERIC | 8 | 2 | — |
| 15 | BKGLC_2YPAST_1 | NUMERIC | 8 | 2 | — |
| 16 | BKGLC_2YPAST_10 | NUMERIC | 8 | 2 | — |
| 17 | BKGLC_2YPAST_11 | NUMERIC | 8 | 2 | — |
| 18 | BKGLC_2YPAST_12 | NUMERIC | 8 | 2 | — |
| 19 | BKGLC_2YPAST_13 | NUMERIC | 8 | 2 | — |
| 20 | BKGLC_2YPAST_14 | NUMERIC | 8 | 2 | — |
| 21 | BKGLC_2YPAST_2 | NUMERIC | 8 | 2 | — |
| 22 | BKGLC_2YPAST_3 | NUMERIC | 8 | 2 | — |
| 23 | BKGLC_2YPAST_4 | NUMERIC | 8 | 2 | — |
| 24 | BKGLC_2YPAST_5 | NUMERIC | 8 | 2 | — |
| 25 | BKGLC_2YPAST_6 | NUMERIC | 8 | 2 | — |
| 26 | BKGLC_2YPAST_7 | NUMERIC | 8 | 2 | — |
| 27 | BKGLC_2YPAST_8 | NUMERIC | 8 | 2 | — |
| 28 | BKGLC_2YPAST_9 | NUMERIC | 8 | 2 | — |
| 29 | BKGLC_ACCT | STRING | 10 | — | GL Account Code |
| 30 | BKGLC_ACCTD | STRING | 25 | — | Account Description |
| 31 | BKGLC_BUDGET_1 | NUMERIC | 8 | 2 | — |
| 32 | BKGLC_BUDGET_10 | NUMERIC | 8 | 2 | — |
| 33 | BKGLC_BUDGET_11 | NUMERIC | 8 | 2 | — |
| 34 | BKGLC_BUDGET_12 | NUMERIC | 8 | 2 | — |
| 35 | BKGLC_BUDGET_13 | NUMERIC | 8 | 2 | — |
| 36 | BKGLC_BUDGET_14 | NUMERIC | 8 | 2 | — |
| 37 | BKGLC_BUDGET_2 | NUMERIC | 8 | 2 | — |
| 38 | BKGLC_BUDGET_3 | NUMERIC | 8 | 2 | — |
| 39 | BKGLC_BUDGET_4 | NUMERIC | 8 | 2 | — |
| 40 | BKGLC_BUDGET_5 | NUMERIC | 8 | 2 | — |
| 41 | BKGLC_BUDGET_6 | NUMERIC | 8 | 2 | — |
| 42 | BKGLC_BUDGET_7 | NUMERIC | 8 | 2 | — |
| 43 | BKGLC_BUDGET_8 | NUMERIC | 8 | 2 | — |
| 44 | BKGLC_BUDGET_9 | NUMERIC | 8 | 2 | — |
| 45 | BKGLC_CR_DR | STRING | 1 | — | Normal Credit/Debit |
| 46 | BKGLC_CURRENT_1 | NUMERIC | 8 | 2 | — |
| 47 | BKGLC_CURRENT_10 | NUMERIC | 8 | 2 | — |
| 48 | BKGLC_CURRENT_11 | NUMERIC | 8 | 2 | — |
| 49 | BKGLC_CURRENT_12 | NUMERIC | 8 | 2 | — |
| 50 | BKGLC_CURRENT_13 | NUMERIC | 8 | 2 | — |
| 51 | BKGLC_CURRENT_14 | NUMERIC | 8 | 2 | — |
| 52 | BKGLC_CURRENT_2 | NUMERIC | 8 | 2 | — |
| 53 | BKGLC_CURRENT_3 | NUMERIC | 8 | 2 | — |
| 54 | BKGLC_CURRENT_4 | NUMERIC | 8 | 2 | — |
| 55 | BKGLC_CURRENT_5 | NUMERIC | 8 | 2 | — |
| 56 | BKGLC_CURRENT_6 | NUMERIC | 8 | 2 | — |
| 57 | BKGLC_CURRENT_7 | NUMERIC | 8 | 2 | — |
| 58 | BKGLC_CURRENT_8 | NUMERIC | 8 | 2 | — |
| 59 | BKGLC_CURRENT_9 | NUMERIC | 8 | 2 | — |
| 60 | BKGLC_GLDPT | STRING | 4 | — | GL Department |
| 61 | BKGLC_NON_CASH | STRING | 1 | — | Non Cash Y/N |
| 62 | BKGLC_TYPE | STRING | 1 | — | Account Type (ALOIE) |

## BKGLCHK
**CHECKING ACCOUNT REGISTER**

Fields: 11

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKGL_CHK_AMT | NUMERIC | 8 | 2 | Amount |
| 2 | BKGL_CHK_CHKACT | INTEGER | 2 | — | Checking Accoun Num |
| 3 | BKGL_CHK_CUST | STRING | 10 | — | — |
| 4 | BKGL_CHK_DATE | DATE | 4 | — | Date |
| 5 | BKGL_CHK_DATER | DATE | 4 | — | — |
| 6 | BKGL_CHK_EXTRA | STRING | 100 | — | — |
| 7 | BKGL_CHK_FLAG | STRING | 1 | — | Reconciled Y/N |
| 8 | BKGL_CHK_NAME | STRING | 25 | — | Pay to Name |
| 9 | BKGL_CHK_NUM | NUMERIC | 8 | — | Check Number |
| 10 | BKGL_CHK_TYPE | STRING | 1 | — | Type |
| 11 | BKGL_CHK_VEND | STRING | 10 | — | — |

## BKGLCOA
**CHART OF ACCOUNTS**

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

## BKGLDESC
**DBA GL JOURNAL NOTES**

Fields: 5

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BK_DESC_CODE | STRING | 15 | — | not used |
| 2 | BK_DESC_DESC | STRING | 25 | — | not used |
| 3 | BK_DESC_LINE | INTEGER | 2 | — | Notes line number |
| 4 | BK_DESC_NOTES | STRING | 70 | — | Notes - text |
| 5 | BK_DESC_NUM | NUMERIC | 8 | — | PO Number |

## BKGLFCOA
**CONSOLIDATED FINANCIALS**

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

## BKGLFSTL
**CUSTOM FINANCIAL STATEMENTS**

Fields: 12

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKFS_CALC_BASE | INTEGER | 2 | — | Base Code |
| 2 | BKFS_DESC | STRING | 25 | — | Description |
| 3 | BKFS_EGL_ACCT | STRING | 10 | — | GL Acct Through |
| 4 | BKFS_LINE_NUM | INTEGER | 2 | — | — |
| 5 | BKFS_NAME | STRING | 10 | — | Report  Name |
| 6 | BKFS_NDC | STRING | 1 | — | Normal Debit/Credit (D/C) |
| 7 | BKFS_OP | STRING | 2 | — | Operator Code (T, B,P,L…) |
| 8 | BKFS_PRT_AMT | STRING | 1 | — | Print Amount Y/N |
| 9 | BKFS_PRT_DOL | STRING | 1 | — | Dolllar Y/N |
| 10 | BKFS_PRT_LOC | INTEGER | 2 | — | Location  Where Total Will Print |
| 11 | BKFS_SGL_ACCT | STRING | 10 | — | GL Acct From |
| 12 | BKFS_TOTAL_FLD | INTEGER | 2 | — | Total Field Type |

## BKGLGJLN
**GENERAL JOURNAL LINE ITEMS**

Fields: 9

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKGL_GJL_ACCTNM | STRING | 10 | — | GL Account Number |
| 2 | BKGL_GJL_AMOUNT | NUMERIC | 8 | 2 | Amount |
| 3 | BKGL_GJL_DC | STRING | 1 | — | Debit/Credit |
| 4 | BKGL_GJL_DESC | STRING | 25 | — | GL Description |
| 5 | BKGL_GJL_EXTRA | STRING | 50 | — | — |
| 6 | BKGL_GJL_GLDPT | STRING | 4 | — | GL Department |
| 7 | BKGL_GJL_JOB | STRING | 15 | — | — |
| 8 | BKGL_GJL_LINE | INTEGER | 2 | — | — |
| 9 | BKGL_GJL_TRANSN | NUMERIC | 8 | — | Gen Journal Transaction Number |

## BKGLGJRN
**GENERAL JOURNAL HEADER**

Fields: 11

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKGL_GJ_CHKACT | INTEGER | 2 | — | Checking Account |
| 2 | BKGL_GJ_CVCODE | STRING | 10 | — | GJ Transaction Code |
| 3 | BKGL_GJ_EXTRA | STRING | 50 | — | — |
| 4 | BKGL_GJ_INVCHKN | NUMERIC | 8 | — | Check Number |
| 5 | BKGL_GJ_JOB | STRING | 15 | — | — |
| 6 | BKGL_GJ_NUMLNES | INTEGER | 2 | — | Number of Lines |
| 7 | BKGL_GJ_POSTED | STRING | 1 | — | Posted Y/N |
| 8 | BKGL_GJ_TRANSDT | DATE | 4 | — | Transaction Date |
| 9 | BKGL_GJ_TRANSNM | NUMERIC | 8 | — | Transaction Number |
| 10 | BKGL_GJ_TYPE | STRING | 2 | — | Type |
| 11 | BKGL_GJ_TYPEN | INTEGER | 2 | — | Type Number |

## BKGLRGJL
**RECURRING GENERAL JOURNAL LINES**

Fields: 9

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKGL_GJL_ACCTNM | STRING | 10 | — | GL Account Number |
| 2 | BKGL_GJL_AMOUNT | NUMERIC | 8 | 2 | Amount |
| 3 | BKGL_GJL_DC | STRING | 1 | — | Debit/Credit |
| 4 | BKGL_GJL_DESC | STRING | 25 | — | GL Description |
| 5 | BKGL_GJL_EXTRA | STRING | 50 | — | — |
| 6 | BKGL_GJL_GLDPT | STRING | 4 | — | GL Department |
| 7 | BKGL_GJL_JOB | STRING | 15 | — | — |
| 8 | BKGL_GJL_LINE | INTEGER | 2 | — | — |
| 9 | BKGL_GJL_TRANSN | NUMERIC | 8 | — | Gen Journal Transaction Number |

## BKGLRGJR
**RECURRING GENERAL JOURNAL HEADER**

Fields: 11

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKGL_GJ_CHKACT | INTEGER | 2 | — | Checking Account |
| 2 | BKGL_GJ_CVCODE | STRING | 10 | — | GJ Transaction Code |
| 3 | BKGL_GJ_EXTRA | STRING | 50 | — | — |
| 4 | BKGL_GJ_INVCHKN | NUMERIC | 8 | — | Check Number |
| 5 | BKGL_GJ_JOB | STRING | 15 | — | — |
| 6 | BKGL_GJ_NUMLNES | INTEGER | 2 | — | Number of Lines |
| 7 | BKGL_GJ_POSTED | STRING | 1 | — | Posted Y/N |
| 8 | BKGL_GJ_TRANSDT | DATE | 4 | — | Transaction Date |
| 9 | BKGL_GJ_TRANSNM | NUMERIC | 8 | — | Transaction Number |
| 10 | BKGL_GJ_TYPE | STRING | 2 | — | Type |
| 11 | BKGL_GJ_TYPEN | INTEGER | 2 | — | Type Number |

## BKGLSTMT
**FINANCIAL STATEMENT SETUP**

Fields: 104

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKGL_STB_GLA_F_1 | STRING | 10 | — | — |
| 2 | BKGL_STB_GLA_F_2 | STRING | 10 | — | — |
| 3 | BKGL_STB_GLA_F_3 | STRING | 10 | — | — |
| 4 | BKGL_STB_GLA_F_4 | STRING | 10 | — | — |
| 5 | BKGL_STB_GLA_MT | STRING | 25 | — | Assets Main Title |
| 6 | BKGL_STB_GLA_T_1 | STRING | 10 | — | — |
| 7 | BKGL_STB_GLA_T_2 | STRING | 10 | — | — |
| 8 | BKGL_STB_GLA_T_3 | STRING | 10 | — | — |
| 9 | BKGL_STB_GLA_T_4 | STRING | 10 | — | — |
| 10 | BKGL_STB_GLATTL_1 | STRING | 25 | — | — |
| 11 | BKGL_STB_GLATTL_2 | STRING | 25 | — | — |
| 12 | BKGL_STB_GLATTL_3 | STRING | 25 | — | — |
| 13 | BKGL_STB_GLATTL_4 | STRING | 25 | — | — |
| 14 | BKGL_STB_GLL_F_1 | STRING | 10 | — | — |
| 15 | BKGL_STB_GLL_F_2 | STRING | 10 | — | — |
| 16 | BKGL_STB_GLL_F_3 | STRING | 10 | — | — |
| 17 | BKGL_STB_GLL_F_4 | STRING | 10 | — | — |
| 18 | BKGL_STB_GLL_MT | STRING | 25 | — | Liabilities Main Title |
| 19 | BKGL_STB_GLL_T_1 | STRING | 10 | — | — |
| 20 | BKGL_STB_GLL_T_2 | STRING | 10 | — | — |
| 21 | BKGL_STB_GLL_T_3 | STRING | 10 | — | — |
| 22 | BKGL_STB_GLL_T_4 | STRING | 10 | — | — |
| 23 | BKGL_STB_GLLTTL_1 | STRING | 25 | — | — |
| 24 | BKGL_STB_GLLTTL_2 | STRING | 25 | — | — |
| 25 | BKGL_STB_GLLTTL_3 | STRING | 25 | — | — |
| 26 | BKGL_STB_GLLTTL_4 | STRING | 25 | — | — |
| 27 | BKGL_STB_GLO_F_1 | STRING | 10 | — | — |
| 28 | BKGL_STB_GLO_F_2 | STRING | 10 | — | — |
| 29 | BKGL_STB_GLO_MT | STRING | 25 | — | Owners Equity Main Title |
| 30 | BKGL_STB_GLO_T_1 | STRING | 10 | — | — |
| 31 | BKGL_STB_GLO_T_2 | STRING | 10 | — | — |
| 32 | BKGL_STB_GLOTTL_1 | STRING | 25 | — | — |
| 33 | BKGL_STB_GLOTTL_2 | STRING | 25 | — | — |
| 34 | BKGL_STB_MN_TTL | STRING | 25 | — | Balance Sheet Report Title |
| 35 | BKGL_STC_GLA_F_1 | STRING | 10 | — | — |
| 36 | BKGL_STC_GLA_F_2 | STRING | 10 | — | — |
| 37 | BKGL_STC_GLA_F_3 | STRING | 10 | — | — |
| 38 | BKGL_STC_GLA_F_4 | STRING | 10 | — | — |
| 39 | BKGL_STC_GLA_MT | STRING | 25 | — | SofC Assets Main  Title |
| 40 | BKGL_STC_GLA_T_1 | STRING | 10 | — | — |
| 41 | BKGL_STC_GLA_T_2 | STRING | 10 | — | — |
| 42 | BKGL_STC_GLA_T_3 | STRING | 10 | — | — |
| 43 | BKGL_STC_GLA_T_4 | STRING | 10 | — | — |
| 44 | BKGL_STC_GLATTL_1 | STRING | 25 | — | — |
| 45 | BKGL_STC_GLATTL_2 | STRING | 25 | — | — |
| 46 | BKGL_STC_GLATTL_3 | STRING | 25 | — | — |
| 47 | BKGL_STC_GLATTL_4 | STRING | 25 | — | — |
| 48 | BKGL_STC_GLI_F | STRING | 10 | — | Net Income Acct From Range |
| 49 | BKGL_STC_GLI_T | STRING | 10 | — | Net Income To Range |
| 50 | BKGL_STC_GLITTL | STRING | 25 | — | Net Income Tittle |
| 51 | BKGL_STC_GLL_F_1 | STRING | 10 | — | — |
| 52 | BKGL_STC_GLL_F_2 | STRING | 10 | — | — |
| 53 | BKGL_STC_GLL_F_3 | STRING | 10 | — | — |
| 54 | BKGL_STC_GLL_F_4 | STRING | 10 | — | — |
| 55 | BKGL_STC_GLL_MT | STRING | 25 | — | SofC Liabilities Main Title |
| 56 | BKGL_STC_GLL_T_1 | STRING | 10 | — | — |
| 57 | BKGL_STC_GLL_T_2 | STRING | 10 | — | — |
| 58 | BKGL_STC_GLL_T_3 | STRING | 10 | — | — |
| 59 | BKGL_STC_GLL_T_4 | STRING | 10 | — | — |
| 60 | BKGL_STC_GLLTTL_1 | STRING | 25 | — | — |
| 61 | BKGL_STC_GLLTTL_2 | STRING | 25 | — | — |
| 62 | BKGL_STC_GLLTTL_3 | STRING | 25 | — | — |
| 63 | BKGL_STC_GLLTTL_4 | STRING | 25 | — | — |
| 64 | BKGL_STC_GLN_F | STRING | 10 | — | Non-Cash Acct From Range |
| 65 | BKGL_STC_GLN_T | STRING | 10 | — | Non-Cash Acct To Range |
| 66 | BKGL_STC_GLNTTL | STRING | 25 | — | Non-Cash Expense Title |
| 67 | BKGL_STC_MN_TTL | STRING | 25 | — | Statement of Change Main Title |
| 68 | BKGL_STI_GLC_F_1 | STRING | 10 | — | — |
| 69 | BKGL_STI_GLC_F_2 | STRING | 10 | — | — |
| 70 | BKGL_STI_GLC_MT | STRING | 25 | — | Cost of Goods Sold Main Title |
| 71 | BKGL_STI_GLC_T_1 | STRING | 10 | — | — |
| 72 | BKGL_STI_GLC_T_2 | STRING | 10 | — | — |
| 73 | BKGL_STI_GLCTTL_1 | STRING | 25 | — | — |
| 74 | BKGL_STI_GLCTTL_2 | STRING | 25 | — | — |
| 75 | BKGL_STI_GLE_F_1 | STRING | 10 | — | — |
| 76 | BKGL_STI_GLE_F_2 | STRING | 10 | — | — |
| 77 | BKGL_STI_GLE_F_3 | STRING | 10 | — | — |
| 78 | BKGL_STI_GLE_F_4 | STRING | 10 | — | — |
| 79 | BKGL_STI_GLE_MT | STRING | 25 | — | Expenses Main Title |
| 80 | BKGL_STI_GLE_T_1 | STRING | 10 | — | — |
| 81 | BKGL_STI_GLE_T_2 | STRING | 10 | — | — |
| 82 | BKGL_STI_GLE_T_3 | STRING | 10 | — | — |
| 83 | BKGL_STI_GLE_T_4 | STRING | 10 | — | — |
| 84 | BKGL_STI_GLETTL_1 | STRING | 25 | — | — |
| 85 | BKGL_STI_GLETTL_2 | STRING | 25 | — | — |
| 86 | BKGL_STI_GLETTL_3 | STRING | 25 | — | — |
| 87 | BKGL_STI_GLETTL_4 | STRING | 25 | — | — |
| 88 | BKGL_STI_GLI_F_1 | STRING | 10 | — | — |
| 89 | BKGL_STI_GLI_F_2 | STRING | 10 | — | — |
| 90 | BKGL_STI_GLI_MT | STRING | 25 | — | Income Statement Main Title |
| 91 | BKGL_STI_GLI_T_1 | STRING | 10 | — | — |
| 92 | BKGL_STI_GLI_T_2 | STRING | 10 | — | — |
| 93 | BKGL_STI_GLITTL_1 | STRING | 25 | — | — |
| 94 | BKGL_STI_GLITTL_2 | STRING | 25 | — | — |
| 95 | BKGL_STI_GLOE_F | STRING | 10 | — | Other Expense From |
| 96 | BKGL_STI_GLOE_T | STRING | 10 | — | Other Expense To |
| 97 | BKGL_STI_GLOETT | STRING | 25 | — | Other Expense Title |
| 98 | BKGL_STI_GLOI_F | STRING | 10 | — | Other Income From |
| 99 | BKGL_STI_GLOI_T | STRING | 10 | — | Other Income To |
| 100 | BKGL_STI_GLOITT | STRING | 25 | — | Other Income Title |
| 101 | BKGL_STI_GLT_F | STRING | 10 | — | — |
| 102 | BKGL_STI_GLT_T | STRING | 10 | — | — |
| 103 | BKGL_STI_GLTTTL | STRING | 25 | — | — |
| 104 | BKGL_STI_MN_TTL | STRING | 25 | — | Income Report Main Title |

## BKGLTEMP
**UNPOSTED GL TRANSACTIONS**

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

## BKGLTGJL
**JOURNAL TEMPLATE LINE**

Fields: 9

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKGL_GJL_ACCTNM | STRING | 10 | — | GL Account Number |
| 2 | BKGL_GJL_AMOUNT | NUMERIC | 8 | 2 | Amount |
| 3 | BKGL_GJL_DC | STRING | 1 | — | Debit/Credit |
| 4 | BKGL_GJL_DESC | STRING | 25 | — | GL Description |
| 5 | BKGL_GJL_EXTRA | STRING | 50 | — | — |
| 6 | BKGL_GJL_GLDPT | STRING | 4 | — | GL Department |
| 7 | BKGL_GJL_JOB | STRING | 15 | — | — |
| 8 | BKGL_GJL_LINE | INTEGER | 2 | — | — |
| 9 | BKGL_GJL_TRANSN | NUMERIC | 8 | — | Gen Journal Transaction Number |

## BKGLTGJR
**JOURNAL TEMPLATE HEADER**

Fields: 11

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKGL_GJ_CHKACT | INTEGER | 2 | — | Checking Account |
| 2 | BKGL_GJ_CVCODE | STRING | 10 | — | GJ Transaction Code |
| 3 | BKGL_GJ_EXTRA | STRING | 50 | — | — |
| 4 | BKGL_GJ_INVCHKN | NUMERIC | 8 | — | Check Number |
| 5 | BKGL_GJ_JOB | STRING | 15 | — | — |
| 6 | BKGL_GJ_NUMLNES | INTEGER | 2 | — | Number of Lines |
| 7 | BKGL_GJ_POSTED | STRING | 1 | — | Posted Y/N |
| 8 | BKGL_GJ_TRANSDT | DATE | 4 | — | Transaction Date |
| 9 | BKGL_GJ_TRANSNM | NUMERIC | 8 | — | Transaction Number |
| 10 | BKGL_GJ_TYPE | STRING | 2 | — | Type |
| 11 | BKGL_GJ_TYPEN | INTEGER | 2 | — | Type Number |

## BKGLTMP3
**DBA BUSINESS STATUS DETAIL**

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

## BKGLTRAN
**POSTED GL TRANSACTIONS**

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

## BKGLX
**TRANSACTION DETAIL**

Fields: 20

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKGLX_AMOUNT | NUMERIC | 8 | 2 | — |
| 2 | BKGLX_ARCHDATE | DATE | 4 | — | — |
| 3 | BKGLX_BATCH | NUMERIC | 8 | — | — |
| 4 | BKGLX_CCLASS | STRING | 4 | — | — |
| 5 | BKGLX_COMPANY | STRING | 2 | — | — |
| 6 | BKGLX_DESC | STRING | 30 | — | — |
| 7 | BKGLX_ENTDATE | DATE | 4 | — | — |
| 8 | BKGLX_ICLASS | STRING | 4 | — | — |
| 9 | BKGLX_JOURNAL | STRING | 2 | — | — |
| 10 | BKGLX_PART | STRING | 15 | — | — |
| 11 | BKGLX_POINVC | STRING | 10 | — | — |
| 12 | BKGLX_PONUM | NUMERIC | 8 | — | — |
| 13 | BKGLX_POST | STRING | 1 | — | — |
| 14 | BKGLX_POSTDATE | DATE | 4 | — | — |
| 15 | BKGLX_QUANTITY | NUMERIC | 8 | 2 | — |
| 16 | BKGLX_SOINVC | NUMERIC | 8 | — | — |
| 17 | BKGLX_TRXN | NUMERIC | 8 | — | — |
| 18 | BKGLX_TRXNTYPE | STRING | 1 | — | — |
| 19 | BKGLX_WOPRE | NUMERIC | 8 | — | — |
| 20 | BKGLX_WOSUF | INTEGER | 2 | — | — |

## BKGLXH
**TRANSACTION DETAIL HISTORY**

Fields: 20

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKGLX_AMOUNT | NUMERIC | 8 | 2 | — |
| 2 | BKGLX_ARCHDATE | DATE | 4 | — | — |
| 3 | BKGLX_BATCH | NUMERIC | 8 | — | — |
| 4 | BKGLX_CCLASS | STRING | 4 | — | — |
| 5 | BKGLX_COMPANY | STRING | 2 | — | — |
| 6 | BKGLX_DESC | STRING | 30 | — | — |
| 7 | BKGLX_ENTDATE | DATE | 4 | — | — |
| 8 | BKGLX_ICLASS | STRING | 4 | — | — |
| 9 | BKGLX_JOURNAL | STRING | 2 | — | — |
| 10 | BKGLX_PART | STRING | 15 | — | — |
| 11 | BKGLX_POINVC | STRING | 10 | — | — |
| 12 | BKGLX_PONUM | NUMERIC | 8 | — | — |
| 13 | BKGLX_POST | STRING | 1 | — | — |
| 14 | BKGLX_POSTDATE | DATE | 4 | — | — |
| 15 | BKGLX_QUANTITY | NUMERIC | 8 | 2 | — |
| 16 | BKGLX_SOINVC | NUMERIC | 8 | — | — |
| 17 | BKGLX_TRXN | NUMERIC | 8 | — | — |
| 18 | BKGLX_TRXNTYPE | STRING | 1 | — | — |
| 19 | BKGLX_WOPRE | NUMERIC | 8 | — | — |
| 20 | BKGLX_WOSUF | INTEGER | 2 | — | — |

## ISBANKS
**BANK MASTER**

Fields: 23

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_BANKS_ACCT | STRING | 15 | — | — |
| 2 | IS_BANKS_ACTIVE | STRING | 1 | — | — |
| 3 | IS_BANKS_AP | STRING | 1 | — | — |
| 4 | IS_BANKS_AR | STRING | 1 | — | — |
| 5 | IS_BANKS_BAL | NUMERIC | 8 | 2 | — |
| 6 | IS_BANKS_CURR | STRING | 3 | — | — |
| 7 | IS_BANKS_DESC | STRING | 40 | — | — |
| 8 | IS_BANKS_EXTRA | STRING | 100 | — | — |
| 9 | IS_BANKS_GLA | STRING | 10 | — | — |
| 10 | IS_BANKS_GLD | STRING | 4 | — | — |
| 11 | IS_BANKS_INC_BS | STRING | 1 | — | — |
| 12 | IS_BANKS_NUM | INTEGER | 2 | — | — |
| 13 | IS_BANKS_NXTNUM | NUMERIC | 8 | — | — |
| 14 | IS_BANKS_PR | STRING | 1 | — | — |
| 15 | IS_BANKS_ROUT | STRING | 15 | — | — |
| 16 | IS_BANKS_RTM_1 | STRING | 12 | — | — |
| 17 | IS_BANKS_RTM_2 | STRING | 12 | — | — |
| 18 | IS_BANKS_RTM_3 | STRING | 12 | — | — |
| 19 | IS_BANKS_RTM_4 | STRING | 12 | — | — |
| 20 | IS_BANKS_RTM_5 | STRING | 12 | — | — |
| 21 | IS_BANKS_SRT | INTEGER | 2 | — | — |
| 22 | IS_BANKS_TYPE | STRING | 2 | — | — |
| 23 | IS_BANKS_VEND | STRING | 10 | — | — |

## ISBSF
**DBA BUSINESS STATUS**

Fields: 143

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISBSF_AP_ATP | NUMERIC | 8 | 2 | — |
| 2 | ISBSF_AP_BAL | NUMERIC | 8 | 2 | — |
| 3 | ISBSF_AP_DISC | NUMERIC | 8 | 2 | — |
| 4 | ISBSF_AP_PAYA | NUMERIC | 8 | 2 | — |
| 5 | ISBSF_AP_PAYM | NUMERIC | 8 | 2 | — |
| 6 | ISBSF_AR_BAL | NUMERIC | 8 | 2 | — |
| 7 | ISBSF_AR_BILL | NUMERIC | 8 | 2 | — |
| 8 | ISBSF_AR_COGS | NUMERIC | 8 | 2 | — |
| 9 | ISBSF_AR_DEPO | NUMERIC | 8 | 2 | — |
| 10 | ISBSF_AR_DISC | NUMERIC | 8 | 2 | — |
| 11 | ISBSF_AR_RECP | NUMERIC | 8 | 2 | — |
| 12 | ISBSF_CASH_ACT1 | NUMERIC | 8 | 2 | — |
| 13 | ISBSF_CASH_ACT2 | NUMERIC | 8 | 2 | — |
| 14 | ISBSF_CASH_ACT3 | NUMERIC | 8 | 2 | — |
| 15 | ISBSF_CASH_ACT4 | NUMERIC | 8 | 2 | — |
| 16 | ISBSF_CASH_ACT5 | NUMERIC | 8 | 2 | — |
| 17 | ISBSF_CASH_ACT6 | NUMERIC | 8 | 2 | — |
| 18 | ISBSF_CASH_ACT7 | NUMERIC | 8 | 2 | — |
| 19 | ISBSF_CASH_ACT8 | NUMERIC | 8 | 2 | — |
| 20 | ISBSF_CASH_ACT9 | NUMERIC | 8 | 2 | — |
| 21 | ISBSF_CASH_ACTS_1 | NUMERIC | 8 | 2 | — |
| 22 | ISBSF_CASH_ACTS_10 | NUMERIC | 8 | 2 | — |
| 23 | ISBSF_CASH_ACTS_100 | NUMERIC | 8 | 2 | — |
| 24 | ISBSF_CASH_ACTS_11 | NUMERIC | 8 | 2 | — |
| 25 | ISBSF_CASH_ACTS_12 | NUMERIC | 8 | 2 | — |
| 26 | ISBSF_CASH_ACTS_13 | NUMERIC | 8 | 2 | — |
| 27 | ISBSF_CASH_ACTS_14 | NUMERIC | 8 | 2 | — |
| 28 | ISBSF_CASH_ACTS_15 | NUMERIC | 8 | 2 | — |
| 29 | ISBSF_CASH_ACTS_16 | NUMERIC | 8 | 2 | — |
| 30 | ISBSF_CASH_ACTS_17 | NUMERIC | 8 | 2 | — |
| 31 | ISBSF_CASH_ACTS_18 | NUMERIC | 8 | 2 | — |
| 32 | ISBSF_CASH_ACTS_19 | NUMERIC | 8 | 2 | — |
| 33 | ISBSF_CASH_ACTS_2 | NUMERIC | 8 | 2 | — |
| 34 | ISBSF_CASH_ACTS_20 | NUMERIC | 8 | 2 | — |
| 35 | ISBSF_CASH_ACTS_21 | NUMERIC | 8 | 2 | — |
| 36 | ISBSF_CASH_ACTS_22 | NUMERIC | 8 | 2 | — |
| 37 | ISBSF_CASH_ACTS_23 | NUMERIC | 8 | 2 | — |
| 38 | ISBSF_CASH_ACTS_24 | NUMERIC | 8 | 2 | — |
| 39 | ISBSF_CASH_ACTS_25 | NUMERIC | 8 | 2 | — |
| 40 | ISBSF_CASH_ACTS_26 | NUMERIC | 8 | 2 | — |
| 41 | ISBSF_CASH_ACTS_27 | NUMERIC | 8 | 2 | — |
| 42 | ISBSF_CASH_ACTS_28 | NUMERIC | 8 | 2 | — |
| 43 | ISBSF_CASH_ACTS_29 | NUMERIC | 8 | 2 | — |
| 44 | ISBSF_CASH_ACTS_3 | NUMERIC | 8 | 2 | — |
| 45 | ISBSF_CASH_ACTS_30 | NUMERIC | 8 | 2 | — |
| 46 | ISBSF_CASH_ACTS_31 | NUMERIC | 8 | 2 | — |
| 47 | ISBSF_CASH_ACTS_32 | NUMERIC | 8 | 2 | — |
| 48 | ISBSF_CASH_ACTS_33 | NUMERIC | 8 | 2 | — |
| 49 | ISBSF_CASH_ACTS_34 | NUMERIC | 8 | 2 | — |
| 50 | ISBSF_CASH_ACTS_35 | NUMERIC | 8 | 2 | — |
| 51 | ISBSF_CASH_ACTS_36 | NUMERIC | 8 | 2 | — |
| 52 | ISBSF_CASH_ACTS_37 | NUMERIC | 8 | 2 | — |
| 53 | ISBSF_CASH_ACTS_38 | NUMERIC | 8 | 2 | — |
| 54 | ISBSF_CASH_ACTS_39 | NUMERIC | 8 | 2 | — |
| 55 | ISBSF_CASH_ACTS_4 | NUMERIC | 8 | 2 | — |
| 56 | ISBSF_CASH_ACTS_40 | NUMERIC | 8 | 2 | — |
| 57 | ISBSF_CASH_ACTS_41 | NUMERIC | 8 | 2 | — |
| 58 | ISBSF_CASH_ACTS_42 | NUMERIC | 8 | 2 | — |
| 59 | ISBSF_CASH_ACTS_43 | NUMERIC | 8 | 2 | — |
| 60 | ISBSF_CASH_ACTS_44 | NUMERIC | 8 | 2 | — |
| 61 | ISBSF_CASH_ACTS_45 | NUMERIC | 8 | 2 | — |
| 62 | ISBSF_CASH_ACTS_46 | NUMERIC | 8 | 2 | — |
| 63 | ISBSF_CASH_ACTS_47 | NUMERIC | 8 | 2 | — |
| 64 | ISBSF_CASH_ACTS_48 | NUMERIC | 8 | 2 | — |
| 65 | ISBSF_CASH_ACTS_49 | NUMERIC | 8 | 2 | — |
| 66 | ISBSF_CASH_ACTS_5 | NUMERIC | 8 | 2 | — |
| 67 | ISBSF_CASH_ACTS_50 | NUMERIC | 8 | 2 | — |
| 68 | ISBSF_CASH_ACTS_51 | NUMERIC | 8 | 2 | — |
| 69 | ISBSF_CASH_ACTS_52 | NUMERIC | 8 | 2 | — |
| 70 | ISBSF_CASH_ACTS_53 | NUMERIC | 8 | 2 | — |
| 71 | ISBSF_CASH_ACTS_54 | NUMERIC | 8 | 2 | — |
| 72 | ISBSF_CASH_ACTS_55 | NUMERIC | 8 | 2 | — |
| 73 | ISBSF_CASH_ACTS_56 | NUMERIC | 8 | 2 | — |
| 74 | ISBSF_CASH_ACTS_57 | NUMERIC | 8 | 2 | — |
| 75 | ISBSF_CASH_ACTS_58 | NUMERIC | 8 | 2 | — |
| 76 | ISBSF_CASH_ACTS_59 | NUMERIC | 8 | 2 | — |
| 77 | ISBSF_CASH_ACTS_6 | NUMERIC | 8 | 2 | — |
| 78 | ISBSF_CASH_ACTS_60 | NUMERIC | 8 | 2 | — |
| 79 | ISBSF_CASH_ACTS_61 | NUMERIC | 8 | 2 | — |
| 80 | ISBSF_CASH_ACTS_62 | NUMERIC | 8 | 2 | — |
| 81 | ISBSF_CASH_ACTS_63 | NUMERIC | 8 | 2 | — |
| 82 | ISBSF_CASH_ACTS_64 | NUMERIC | 8 | 2 | — |
| 83 | ISBSF_CASH_ACTS_65 | NUMERIC | 8 | 2 | — |
| 84 | ISBSF_CASH_ACTS_66 | NUMERIC | 8 | 2 | — |
| 85 | ISBSF_CASH_ACTS_67 | NUMERIC | 8 | 2 | — |
| 86 | ISBSF_CASH_ACTS_68 | NUMERIC | 8 | 2 | — |
| 87 | ISBSF_CASH_ACTS_69 | NUMERIC | 8 | 2 | — |
| 88 | ISBSF_CASH_ACTS_7 | NUMERIC | 8 | 2 | — |
| 89 | ISBSF_CASH_ACTS_70 | NUMERIC | 8 | 2 | — |
| 90 | ISBSF_CASH_ACTS_71 | NUMERIC | 8 | 2 | — |
| 91 | ISBSF_CASH_ACTS_72 | NUMERIC | 8 | 2 | — |
| 92 | ISBSF_CASH_ACTS_73 | NUMERIC | 8 | 2 | — |
| 93 | ISBSF_CASH_ACTS_74 | NUMERIC | 8 | 2 | — |
| 94 | ISBSF_CASH_ACTS_75 | NUMERIC | 8 | 2 | — |
| 95 | ISBSF_CASH_ACTS_76 | NUMERIC | 8 | 2 | — |
| 96 | ISBSF_CASH_ACTS_77 | NUMERIC | 8 | 2 | — |
| 97 | ISBSF_CASH_ACTS_78 | NUMERIC | 8 | 2 | — |
| 98 | ISBSF_CASH_ACTS_79 | NUMERIC | 8 | 2 | — |
| 99 | ISBSF_CASH_ACTS_8 | NUMERIC | 8 | 2 | — |
| 100 | ISBSF_CASH_ACTS_80 | NUMERIC | 8 | 2 | — |
| 101 | ISBSF_CASH_ACTS_81 | NUMERIC | 8 | 2 | — |
| 102 | ISBSF_CASH_ACTS_82 | NUMERIC | 8 | 2 | — |
| 103 | ISBSF_CASH_ACTS_83 | NUMERIC | 8 | 2 | — |
| 104 | ISBSF_CASH_ACTS_84 | NUMERIC | 8 | 2 | — |
| 105 | ISBSF_CASH_ACTS_85 | NUMERIC | 8 | 2 | — |
| 106 | ISBSF_CASH_ACTS_86 | NUMERIC | 8 | 2 | — |
| 107 | ISBSF_CASH_ACTS_87 | NUMERIC | 8 | 2 | — |
| 108 | ISBSF_CASH_ACTS_88 | NUMERIC | 8 | 2 | — |
| 109 | ISBSF_CASH_ACTS_89 | NUMERIC | 8 | 2 | — |
| 110 | ISBSF_CASH_ACTS_9 | NUMERIC | 8 | 2 | — |
| 111 | ISBSF_CASH_ACTS_90 | NUMERIC | 8 | 2 | — |
| 112 | ISBSF_CASH_ACTS_91 | NUMERIC | 8 | 2 | — |
| 113 | ISBSF_CASH_ACTS_92 | NUMERIC | 8 | 2 | — |
| 114 | ISBSF_CASH_ACTS_93 | NUMERIC | 8 | 2 | — |
| 115 | ISBSF_CASH_ACTS_94 | NUMERIC | 8 | 2 | — |
| 116 | ISBSF_CASH_ACTS_95 | NUMERIC | 8 | 2 | — |
| 117 | ISBSF_CASH_ACTS_96 | NUMERIC | 8 | 2 | — |
| 118 | ISBSF_CASH_ACTS_97 | NUMERIC | 8 | 2 | — |
| 119 | ISBSF_CASH_ACTS_98 | NUMERIC | 8 | 2 | — |
| 120 | ISBSF_CASH_ACTS_99 | NUMERIC | 8 | 2 | — |
| 121 | ISBSF_CASH_TOTA | NUMERIC | 8 | 2 | — |
| 122 | ISBSF_ENDDATE | DATE | 4 | — | — |
| 123 | ISBSF_EXTRA | STRING | 100 | — | — |
| 124 | ISBSF_IC_VALUE | NUMERIC | 8 | 2 | — |
| 125 | ISBSF_PO_BOOK | NUMERIC | 8 | 2 | — |
| 126 | ISBSF_PO_OPEN | NUMERIC | 8 | 2 | — |
| 127 | ISBSF_PO_RECP | NUMERIC | 8 | 2 | — |
| 128 | ISBSF_SO_BOOK | NUMERIC | 8 | 2 | — |
| 129 | ISBSF_SO_OPEN | NUMERIC | 8 | 2 | — |
| 130 | ISBSF_SO_SHIP | NUMERIC | 8 | 2 | — |
| 131 | ISBSF_STARTDATE | DATE | 4 | — | — |
| 132 | ISBSF_WO_FPVAR | NUMERIC | 8 | 2 | — |
| 133 | ISBSF_WO_ISSU | NUMERIC | 8 | 2 | — |
| 134 | ISBSF_WO_WIPBAL | NUMERIC | 8 | 2 | — |
| 135 | ISBSF_WOS_FOH | NUMERIC | 8 | 2 | — |
| 136 | ISBSF_WOS_FP | NUMERIC | 8 | 2 | — |
| 137 | ISBSF_WOS_LAB | NUMERIC | 8 | 2 | — |
| 138 | ISBSF_WOS_MAT | NUMERIC | 8 | 2 | — |
| 139 | ISBSF_WOS_MEXT | NUMERIC | 8 | 2 | — |
| 140 | ISBSF_WOS_OUTP | NUMERIC | 8 | 2 | — |
| 141 | ISBSF_WOS_SETUP | NUMERIC | 8 | 2 | — |
| 142 | ISBSF_WOS_VOH | NUMERIC | 8 | 2 | — |
| 143 | ISBSF_WOS_WIPV | NUMERIC | 8 | 2 | — |

## ISGLBDGT
**MULTI-YEAR BUDGET**

Fields: 67

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISGL_3YPAST_1 | NUMERIC | 8 | 2 | — |
| 2 | ISGL_3YPAST_10 | NUMERIC | 8 | 2 | — |
| 3 | ISGL_3YPAST_11 | NUMERIC | 8 | 2 | — |
| 4 | ISGL_3YPAST_12 | NUMERIC | 8 | 2 | — |
| 5 | ISGL_3YPAST_13 | NUMERIC | 8 | 2 | — |
| 6 | ISGL_3YPAST_14 | NUMERIC | 8 | 2 | — |
| 7 | ISGL_3YPAST_2 | NUMERIC | 8 | 2 | — |
| 8 | ISGL_3YPAST_3 | NUMERIC | 8 | 2 | — |
| 9 | ISGL_3YPAST_4 | NUMERIC | 8 | 2 | — |
| 10 | ISGL_3YPAST_5 | NUMERIC | 8 | 2 | — |
| 11 | ISGL_3YPAST_6 | NUMERIC | 8 | 2 | — |
| 12 | ISGL_3YPAST_7 | NUMERIC | 8 | 2 | — |
| 13 | ISGL_3YPAST_8 | NUMERIC | 8 | 2 | — |
| 14 | ISGL_3YPAST_9 | NUMERIC | 8 | 2 | — |
| 15 | ISGL_3YPAST_YE | NUMERIC | 8 | 2 | — |
| 16 | ISGL_4YPAST_1 | NUMERIC | 8 | 2 | — |
| 17 | ISGL_4YPAST_10 | NUMERIC | 8 | 2 | — |
| 18 | ISGL_4YPAST_11 | NUMERIC | 8 | 2 | — |
| 19 | ISGL_4YPAST_12 | NUMERIC | 8 | 2 | — |
| 20 | ISGL_4YPAST_13 | NUMERIC | 8 | 2 | — |
| 21 | ISGL_4YPAST_14 | NUMERIC | 8 | 2 | — |
| 22 | ISGL_4YPAST_2 | NUMERIC | 8 | 2 | — |
| 23 | ISGL_4YPAST_3 | NUMERIC | 8 | 2 | — |
| 24 | ISGL_4YPAST_4 | NUMERIC | 8 | 2 | — |
| 25 | ISGL_4YPAST_5 | NUMERIC | 8 | 2 | — |
| 26 | ISGL_4YPAST_6 | NUMERIC | 8 | 2 | — |
| 27 | ISGL_4YPAST_7 | NUMERIC | 8 | 2 | — |
| 28 | ISGL_4YPAST_8 | NUMERIC | 8 | 2 | — |
| 29 | ISGL_4YPAST_9 | NUMERIC | 8 | 2 | — |
| 30 | ISGL_4YPAST_YE | NUMERIC | 8 | 2 | — |
| 31 | ISGL_5YPAST_1 | NUMERIC | 8 | 2 | — |
| 32 | ISGL_5YPAST_10 | NUMERIC | 8 | 2 | — |
| 33 | ISGL_5YPAST_11 | NUMERIC | 8 | 2 | — |
| 34 | ISGL_5YPAST_12 | NUMERIC | 8 | 2 | — |
| 35 | ISGL_5YPAST_13 | NUMERIC | 8 | 2 | — |
| 36 | ISGL_5YPAST_14 | NUMERIC | 8 | 2 | — |
| 37 | ISGL_5YPAST_2 | NUMERIC | 8 | 2 | — |
| 38 | ISGL_5YPAST_3 | NUMERIC | 8 | 2 | — |
| 39 | ISGL_5YPAST_4 | NUMERIC | 8 | 2 | — |
| 40 | ISGL_5YPAST_5 | NUMERIC | 8 | 2 | — |
| 41 | ISGL_5YPAST_6 | NUMERIC | 8 | 2 | — |
| 42 | ISGL_5YPAST_7 | NUMERIC | 8 | 2 | — |
| 43 | ISGL_5YPAST_8 | NUMERIC | 8 | 2 | — |
| 44 | ISGL_5YPAST_9 | NUMERIC | 8 | 2 | — |
| 45 | ISGL_5YPAST_YE | NUMERIC | 8 | 2 | — |
| 46 | ISGL_6YPAST_1 | NUMERIC | 8 | 2 | — |
| 47 | ISGL_6YPAST_10 | NUMERIC | 8 | 2 | — |
| 48 | ISGL_6YPAST_11 | NUMERIC | 8 | 2 | — |
| 49 | ISGL_6YPAST_12 | NUMERIC | 8 | 2 | — |
| 50 | ISGL_6YPAST_13 | NUMERIC | 8 | 2 | — |
| 51 | ISGL_6YPAST_14 | NUMERIC | 8 | 2 | — |
| 52 | ISGL_6YPAST_2 | NUMERIC | 8 | 2 | — |
| 53 | ISGL_6YPAST_3 | NUMERIC | 8 | 2 | — |
| 54 | ISGL_6YPAST_4 | NUMERIC | 8 | 2 | — |
| 55 | ISGL_6YPAST_5 | NUMERIC | 8 | 2 | — |
| 56 | ISGL_6YPAST_6 | NUMERIC | 8 | 2 | — |
| 57 | ISGL_6YPAST_7 | NUMERIC | 8 | 2 | — |
| 58 | ISGL_6YPAST_8 | NUMERIC | 8 | 2 | — |
| 59 | ISGL_6YPAST_9 | NUMERIC | 8 | 2 | — |
| 60 | ISGL_6YPAST_YE | NUMERIC | 8 | 2 | — |
| 61 | ISGL_ACCT | STRING | 10 | — | — |
| 62 | ISGL_ACCTD | STRING | 25 | — | — |
| 63 | ISGL_CEXTRA | STRING | 100 | — | — |
| 64 | ISGL_CR_DR | STRING | 1 | — | — |
| 65 | ISGL_GLDPT | STRING | 4 | — | — |
| 66 | ISGL_NON_CASH | STRING | 1 | — | — |
| 67 | ISGL_TYPE | STRING | 1 | — | — |

## ISGLCOA
**CHART OF ACCOUNTS 3-6 YR PAST**

Fields: 67

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISGL_3YPAST_1 | NUMERIC | 8 | 2 | — |
| 2 | ISGL_3YPAST_10 | NUMERIC | 8 | 2 | — |
| 3 | ISGL_3YPAST_11 | NUMERIC | 8 | 2 | — |
| 4 | ISGL_3YPAST_12 | NUMERIC | 8 | 2 | — |
| 5 | ISGL_3YPAST_13 | NUMERIC | 8 | 2 | — |
| 6 | ISGL_3YPAST_14 | NUMERIC | 8 | 2 | — |
| 7 | ISGL_3YPAST_2 | NUMERIC | 8 | 2 | — |
| 8 | ISGL_3YPAST_3 | NUMERIC | 8 | 2 | — |
| 9 | ISGL_3YPAST_4 | NUMERIC | 8 | 2 | — |
| 10 | ISGL_3YPAST_5 | NUMERIC | 8 | 2 | — |
| 11 | ISGL_3YPAST_6 | NUMERIC | 8 | 2 | — |
| 12 | ISGL_3YPAST_7 | NUMERIC | 8 | 2 | — |
| 13 | ISGL_3YPAST_8 | NUMERIC | 8 | 2 | — |
| 14 | ISGL_3YPAST_9 | NUMERIC | 8 | 2 | — |
| 15 | ISGL_3YPAST_YE | NUMERIC | 8 | 2 | — |
| 16 | ISGL_4YPAST_1 | NUMERIC | 8 | 2 | — |
| 17 | ISGL_4YPAST_10 | NUMERIC | 8 | 2 | — |
| 18 | ISGL_4YPAST_11 | NUMERIC | 8 | 2 | — |
| 19 | ISGL_4YPAST_12 | NUMERIC | 8 | 2 | — |
| 20 | ISGL_4YPAST_13 | NUMERIC | 8 | 2 | — |
| 21 | ISGL_4YPAST_14 | NUMERIC | 8 | 2 | — |
| 22 | ISGL_4YPAST_2 | NUMERIC | 8 | 2 | — |
| 23 | ISGL_4YPAST_3 | NUMERIC | 8 | 2 | — |
| 24 | ISGL_4YPAST_4 | NUMERIC | 8 | 2 | — |
| 25 | ISGL_4YPAST_5 | NUMERIC | 8 | 2 | — |
| 26 | ISGL_4YPAST_6 | NUMERIC | 8 | 2 | — |
| 27 | ISGL_4YPAST_7 | NUMERIC | 8 | 2 | — |
| 28 | ISGL_4YPAST_8 | NUMERIC | 8 | 2 | — |
| 29 | ISGL_4YPAST_9 | NUMERIC | 8 | 2 | — |
| 30 | ISGL_4YPAST_YE | NUMERIC | 8 | 2 | — |
| 31 | ISGL_5YPAST_1 | NUMERIC | 8 | 2 | — |
| 32 | ISGL_5YPAST_10 | NUMERIC | 8 | 2 | — |
| 33 | ISGL_5YPAST_11 | NUMERIC | 8 | 2 | — |
| 34 | ISGL_5YPAST_12 | NUMERIC | 8 | 2 | — |
| 35 | ISGL_5YPAST_13 | NUMERIC | 8 | 2 | — |
| 36 | ISGL_5YPAST_14 | NUMERIC | 8 | 2 | — |
| 37 | ISGL_5YPAST_2 | NUMERIC | 8 | 2 | — |
| 38 | ISGL_5YPAST_3 | NUMERIC | 8 | 2 | — |
| 39 | ISGL_5YPAST_4 | NUMERIC | 8 | 2 | — |
| 40 | ISGL_5YPAST_5 | NUMERIC | 8 | 2 | — |
| 41 | ISGL_5YPAST_6 | NUMERIC | 8 | 2 | — |
| 42 | ISGL_5YPAST_7 | NUMERIC | 8 | 2 | — |
| 43 | ISGL_5YPAST_8 | NUMERIC | 8 | 2 | — |
| 44 | ISGL_5YPAST_9 | NUMERIC | 8 | 2 | — |
| 45 | ISGL_5YPAST_YE | NUMERIC | 8 | 2 | — |
| 46 | ISGL_6YPAST_1 | NUMERIC | 8 | 2 | — |
| 47 | ISGL_6YPAST_10 | NUMERIC | 8 | 2 | — |
| 48 | ISGL_6YPAST_11 | NUMERIC | 8 | 2 | — |
| 49 | ISGL_6YPAST_12 | NUMERIC | 8 | 2 | — |
| 50 | ISGL_6YPAST_13 | NUMERIC | 8 | 2 | — |
| 51 | ISGL_6YPAST_14 | NUMERIC | 8 | 2 | — |
| 52 | ISGL_6YPAST_2 | NUMERIC | 8 | 2 | — |
| 53 | ISGL_6YPAST_3 | NUMERIC | 8 | 2 | — |
| 54 | ISGL_6YPAST_4 | NUMERIC | 8 | 2 | — |
| 55 | ISGL_6YPAST_5 | NUMERIC | 8 | 2 | — |
| 56 | ISGL_6YPAST_6 | NUMERIC | 8 | 2 | — |
| 57 | ISGL_6YPAST_7 | NUMERIC | 8 | 2 | — |
| 58 | ISGL_6YPAST_8 | NUMERIC | 8 | 2 | — |
| 59 | ISGL_6YPAST_9 | NUMERIC | 8 | 2 | — |
| 60 | ISGL_6YPAST_YE | NUMERIC | 8 | 2 | — |
| 61 | ISGL_ACCT | STRING | 10 | — | — |
| 62 | ISGL_ACCTD | STRING | 25 | — | — |
| 63 | ISGL_CEXTRA | STRING | 100 | — | — |
| 64 | ISGL_CR_DR | STRING | 1 | — | — |
| 65 | ISGL_GLDPT | STRING | 4 | — | — |
| 66 | ISGL_NON_CASH | STRING | 1 | — | — |
| 67 | ISGL_TYPE | STRING | 1 | — | — |

## ISGLDATE
**FISCAL PERIOD DATES**

Fields: 86

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISGL_1YDATE_1 | DATE | 4 | — | — |
| 2 | ISGL_1YDATE_10 | DATE | 4 | — | — |
| 3 | ISGL_1YDATE_11 | DATE | 4 | — | — |
| 4 | ISGL_1YDATE_12 | DATE | 4 | — | — |
| 5 | ISGL_1YDATE_2 | DATE | 4 | — | — |
| 6 | ISGL_1YDATE_3 | DATE | 4 | — | — |
| 7 | ISGL_1YDATE_4 | DATE | 4 | — | — |
| 8 | ISGL_1YDATE_5 | DATE | 4 | — | — |
| 9 | ISGL_1YDATE_6 | DATE | 4 | — | — |
| 10 | ISGL_1YDATE_7 | DATE | 4 | — | — |
| 11 | ISGL_1YDATE_8 | DATE | 4 | — | — |
| 12 | ISGL_1YDATE_9 | DATE | 4 | — | — |
| 13 | ISGL_2YDATE_1 | DATE | 4 | — | — |
| 14 | ISGL_2YDATE_10 | DATE | 4 | — | — |
| 15 | ISGL_2YDATE_11 | DATE | 4 | — | — |
| 16 | ISGL_2YDATE_12 | DATE | 4 | — | — |
| 17 | ISGL_2YDATE_2 | DATE | 4 | — | — |
| 18 | ISGL_2YDATE_3 | DATE | 4 | — | — |
| 19 | ISGL_2YDATE_4 | DATE | 4 | — | — |
| 20 | ISGL_2YDATE_5 | DATE | 4 | — | — |
| 21 | ISGL_2YDATE_6 | DATE | 4 | — | — |
| 22 | ISGL_2YDATE_7 | DATE | 4 | — | — |
| 23 | ISGL_2YDATE_8 | DATE | 4 | — | — |
| 24 | ISGL_2YDATE_9 | DATE | 4 | — | — |
| 25 | ISGL_3YDATE_1 | DATE | 4 | — | — |
| 26 | ISGL_3YDATE_10 | DATE | 4 | — | — |
| 27 | ISGL_3YDATE_11 | DATE | 4 | — | — |
| 28 | ISGL_3YDATE_12 | DATE | 4 | — | — |
| 29 | ISGL_3YDATE_2 | DATE | 4 | — | — |
| 30 | ISGL_3YDATE_3 | DATE | 4 | — | — |
| 31 | ISGL_3YDATE_4 | DATE | 4 | — | — |
| 32 | ISGL_3YDATE_5 | DATE | 4 | — | — |
| 33 | ISGL_3YDATE_6 | DATE | 4 | — | — |
| 34 | ISGL_3YDATE_7 | DATE | 4 | — | — |
| 35 | ISGL_3YDATE_8 | DATE | 4 | — | — |
| 36 | ISGL_3YDATE_9 | DATE | 4 | — | — |
| 37 | ISGL_4YDATE_1 | DATE | 4 | — | — |
| 38 | ISGL_4YDATE_10 | DATE | 4 | — | — |
| 39 | ISGL_4YDATE_11 | DATE | 4 | — | — |
| 40 | ISGL_4YDATE_12 | DATE | 4 | — | — |
| 41 | ISGL_4YDATE_2 | DATE | 4 | — | — |
| 42 | ISGL_4YDATE_3 | DATE | 4 | — | — |
| 43 | ISGL_4YDATE_4 | DATE | 4 | — | — |
| 44 | ISGL_4YDATE_5 | DATE | 4 | — | — |
| 45 | ISGL_4YDATE_6 | DATE | 4 | — | — |
| 46 | ISGL_4YDATE_7 | DATE | 4 | — | — |
| 47 | ISGL_4YDATE_8 | DATE | 4 | — | — |
| 48 | ISGL_4YDATE_9 | DATE | 4 | — | — |
| 49 | ISGL_5YDATE_1 | DATE | 4 | — | — |
| 50 | ISGL_5YDATE_10 | DATE | 4 | — | — |
| 51 | ISGL_5YDATE_11 | DATE | 4 | — | — |
| 52 | ISGL_5YDATE_12 | DATE | 4 | — | — |
| 53 | ISGL_5YDATE_2 | DATE | 4 | — | — |
| 54 | ISGL_5YDATE_3 | DATE | 4 | — | — |
| 55 | ISGL_5YDATE_4 | DATE | 4 | — | — |
| 56 | ISGL_5YDATE_5 | DATE | 4 | — | — |
| 57 | ISGL_5YDATE_6 | DATE | 4 | — | — |
| 58 | ISGL_5YDATE_7 | DATE | 4 | — | — |
| 59 | ISGL_5YDATE_8 | DATE | 4 | — | — |
| 60 | ISGL_5YDATE_9 | DATE | 4 | — | — |
| 61 | ISGL_6YDATE_1 | DATE | 4 | — | — |
| 62 | ISGL_6YDATE_10 | DATE | 4 | — | — |
| 63 | ISGL_6YDATE_11 | DATE | 4 | — | — |
| 64 | ISGL_6YDATE_12 | DATE | 4 | — | — |
| 65 | ISGL_6YDATE_2 | DATE | 4 | — | — |
| 66 | ISGL_6YDATE_3 | DATE | 4 | — | — |
| 67 | ISGL_6YDATE_4 | DATE | 4 | — | — |
| 68 | ISGL_6YDATE_5 | DATE | 4 | — | — |
| 69 | ISGL_6YDATE_6 | DATE | 4 | — | — |
| 70 | ISGL_6YDATE_7 | DATE | 4 | — | — |
| 71 | ISGL_6YDATE_8 | DATE | 4 | — | — |
| 72 | ISGL_6YDATE_9 | DATE | 4 | — | — |
| 73 | ISGL_CYDATE_1 | DATE | 4 | — | — |
| 74 | ISGL_CYDATE_10 | DATE | 4 | — | — |
| 75 | ISGL_CYDATE_11 | DATE | 4 | — | — |
| 76 | ISGL_CYDATE_12 | DATE | 4 | — | — |
| 77 | ISGL_CYDATE_2 | DATE | 4 | — | — |
| 78 | ISGL_CYDATE_3 | DATE | 4 | — | — |
| 79 | ISGL_CYDATE_4 | DATE | 4 | — | — |
| 80 | ISGL_CYDATE_5 | DATE | 4 | — | — |
| 81 | ISGL_CYDATE_6 | DATE | 4 | — | — |
| 82 | ISGL_CYDATE_7 | DATE | 4 | — | — |
| 83 | ISGL_CYDATE_8 | DATE | 4 | — | — |
| 84 | ISGL_CYDATE_9 | DATE | 4 | — | — |
| 85 | ISGL_EXTRA | STRING | 50 | — | — |
| 86 | ISGL_FYDATE | DATE | 4 | — | — |

## ISGLHDAT
**HISTORICAL FISCAL PERIOD DATES**

Fields: 86

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISGL_1YDATE_1 | DATE | 4 | — | — |
| 2 | ISGL_1YDATE_10 | DATE | 4 | — | — |
| 3 | ISGL_1YDATE_11 | DATE | 4 | — | — |
| 4 | ISGL_1YDATE_12 | DATE | 4 | — | — |
| 5 | ISGL_1YDATE_2 | DATE | 4 | — | — |
| 6 | ISGL_1YDATE_3 | DATE | 4 | — | — |
| 7 | ISGL_1YDATE_4 | DATE | 4 | — | — |
| 8 | ISGL_1YDATE_5 | DATE | 4 | — | — |
| 9 | ISGL_1YDATE_6 | DATE | 4 | — | — |
| 10 | ISGL_1YDATE_7 | DATE | 4 | — | — |
| 11 | ISGL_1YDATE_8 | DATE | 4 | — | — |
| 12 | ISGL_1YDATE_9 | DATE | 4 | — | — |
| 13 | ISGL_2YDATE_1 | DATE | 4 | — | — |
| 14 | ISGL_2YDATE_10 | DATE | 4 | — | — |
| 15 | ISGL_2YDATE_11 | DATE | 4 | — | — |
| 16 | ISGL_2YDATE_12 | DATE | 4 | — | — |
| 17 | ISGL_2YDATE_2 | DATE | 4 | — | — |
| 18 | ISGL_2YDATE_3 | DATE | 4 | — | — |
| 19 | ISGL_2YDATE_4 | DATE | 4 | — | — |
| 20 | ISGL_2YDATE_5 | DATE | 4 | — | — |
| 21 | ISGL_2YDATE_6 | DATE | 4 | — | — |
| 22 | ISGL_2YDATE_7 | DATE | 4 | — | — |
| 23 | ISGL_2YDATE_8 | DATE | 4 | — | — |
| 24 | ISGL_2YDATE_9 | DATE | 4 | — | — |
| 25 | ISGL_3YDATE_1 | DATE | 4 | — | — |
| 26 | ISGL_3YDATE_10 | DATE | 4 | — | — |
| 27 | ISGL_3YDATE_11 | DATE | 4 | — | — |
| 28 | ISGL_3YDATE_12 | DATE | 4 | — | — |
| 29 | ISGL_3YDATE_2 | DATE | 4 | — | — |
| 30 | ISGL_3YDATE_3 | DATE | 4 | — | — |
| 31 | ISGL_3YDATE_4 | DATE | 4 | — | — |
| 32 | ISGL_3YDATE_5 | DATE | 4 | — | — |
| 33 | ISGL_3YDATE_6 | DATE | 4 | — | — |
| 34 | ISGL_3YDATE_7 | DATE | 4 | — | — |
| 35 | ISGL_3YDATE_8 | DATE | 4 | — | — |
| 36 | ISGL_3YDATE_9 | DATE | 4 | — | — |
| 37 | ISGL_4YDATE_1 | DATE | 4 | — | — |
| 38 | ISGL_4YDATE_10 | DATE | 4 | — | — |
| 39 | ISGL_4YDATE_11 | DATE | 4 | — | — |
| 40 | ISGL_4YDATE_12 | DATE | 4 | — | — |
| 41 | ISGL_4YDATE_2 | DATE | 4 | — | — |
| 42 | ISGL_4YDATE_3 | DATE | 4 | — | — |
| 43 | ISGL_4YDATE_4 | DATE | 4 | — | — |
| 44 | ISGL_4YDATE_5 | DATE | 4 | — | — |
| 45 | ISGL_4YDATE_6 | DATE | 4 | — | — |
| 46 | ISGL_4YDATE_7 | DATE | 4 | — | — |
| 47 | ISGL_4YDATE_8 | DATE | 4 | — | — |
| 48 | ISGL_4YDATE_9 | DATE | 4 | — | — |
| 49 | ISGL_5YDATE_1 | DATE | 4 | — | — |
| 50 | ISGL_5YDATE_10 | DATE | 4 | — | — |
| 51 | ISGL_5YDATE_11 | DATE | 4 | — | — |
| 52 | ISGL_5YDATE_12 | DATE | 4 | — | — |
| 53 | ISGL_5YDATE_2 | DATE | 4 | — | — |
| 54 | ISGL_5YDATE_3 | DATE | 4 | — | — |
| 55 | ISGL_5YDATE_4 | DATE | 4 | — | — |
| 56 | ISGL_5YDATE_5 | DATE | 4 | — | — |
| 57 | ISGL_5YDATE_6 | DATE | 4 | — | — |
| 58 | ISGL_5YDATE_7 | DATE | 4 | — | — |
| 59 | ISGL_5YDATE_8 | DATE | 4 | — | — |
| 60 | ISGL_5YDATE_9 | DATE | 4 | — | — |
| 61 | ISGL_6YDATE_1 | DATE | 4 | — | — |
| 62 | ISGL_6YDATE_10 | DATE | 4 | — | — |
| 63 | ISGL_6YDATE_11 | DATE | 4 | — | — |
| 64 | ISGL_6YDATE_12 | DATE | 4 | — | — |
| 65 | ISGL_6YDATE_2 | DATE | 4 | — | — |
| 66 | ISGL_6YDATE_3 | DATE | 4 | — | — |
| 67 | ISGL_6YDATE_4 | DATE | 4 | — | — |
| 68 | ISGL_6YDATE_5 | DATE | 4 | — | — |
| 69 | ISGL_6YDATE_6 | DATE | 4 | — | — |
| 70 | ISGL_6YDATE_7 | DATE | 4 | — | — |
| 71 | ISGL_6YDATE_8 | DATE | 4 | — | — |
| 72 | ISGL_6YDATE_9 | DATE | 4 | — | — |
| 73 | ISGL_CYDATE_1 | DATE | 4 | — | — |
| 74 | ISGL_CYDATE_10 | DATE | 4 | — | — |
| 75 | ISGL_CYDATE_11 | DATE | 4 | — | — |
| 76 | ISGL_CYDATE_12 | DATE | 4 | — | — |
| 77 | ISGL_CYDATE_2 | DATE | 4 | — | — |
| 78 | ISGL_CYDATE_3 | DATE | 4 | — | — |
| 79 | ISGL_CYDATE_4 | DATE | 4 | — | — |
| 80 | ISGL_CYDATE_5 | DATE | 4 | — | — |
| 81 | ISGL_CYDATE_6 | DATE | 4 | — | — |
| 82 | ISGL_CYDATE_7 | DATE | 4 | — | — |
| 83 | ISGL_CYDATE_8 | DATE | 4 | — | — |
| 84 | ISGL_CYDATE_9 | DATE | 4 | — | — |
| 85 | ISGL_EXTRA | STRING | 50 | — | — |
| 86 | ISGL_FYDATE | DATE | 4 | — | — |

## ISJBSF
**EVO BUSINESS STATUS**

Fields: 143

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISBSF_AP_ATP | NUMERIC | 8 | 2 | — |
| 2 | ISBSF_AP_BAL | NUMERIC | 8 | 2 | — |
| 3 | ISBSF_AP_DISC | NUMERIC | 8 | 2 | — |
| 4 | ISBSF_AP_PAYA | NUMERIC | 8 | 2 | — |
| 5 | ISBSF_AP_PAYM | NUMERIC | 8 | 2 | — |
| 6 | ISBSF_AR_BAL | NUMERIC | 8 | 2 | — |
| 7 | ISBSF_AR_BILL | NUMERIC | 8 | 2 | — |
| 8 | ISBSF_AR_COGS | NUMERIC | 8 | 2 | — |
| 9 | ISBSF_AR_DEPO | NUMERIC | 8 | 2 | — |
| 10 | ISBSF_AR_DISC | NUMERIC | 8 | 2 | — |
| 11 | ISBSF_AR_RECP | NUMERIC | 8 | 2 | — |
| 12 | ISBSF_CASH_ACT1 | NUMERIC | 8 | 2 | — |
| 13 | ISBSF_CASH_ACT2 | NUMERIC | 8 | 2 | — |
| 14 | ISBSF_CASH_ACT3 | NUMERIC | 8 | 2 | — |
| 15 | ISBSF_CASH_ACT4 | NUMERIC | 8 | 2 | — |
| 16 | ISBSF_CASH_ACT5 | NUMERIC | 8 | 2 | — |
| 17 | ISBSF_CASH_ACT6 | NUMERIC | 8 | 2 | — |
| 18 | ISBSF_CASH_ACT7 | NUMERIC | 8 | 2 | — |
| 19 | ISBSF_CASH_ACT8 | NUMERIC | 8 | 2 | — |
| 20 | ISBSF_CASH_ACT9 | NUMERIC | 8 | 2 | — |
| 21 | ISBSF_CASH_ACTS_1 | NUMERIC | 8 | 2 | — |
| 22 | ISBSF_CASH_ACTS_10 | NUMERIC | 8 | 2 | — |
| 23 | ISBSF_CASH_ACTS_100 | NUMERIC | 8 | 2 | — |
| 24 | ISBSF_CASH_ACTS_11 | NUMERIC | 8 | 2 | — |
| 25 | ISBSF_CASH_ACTS_12 | NUMERIC | 8 | 2 | — |
| 26 | ISBSF_CASH_ACTS_13 | NUMERIC | 8 | 2 | — |
| 27 | ISBSF_CASH_ACTS_14 | NUMERIC | 8 | 2 | — |
| 28 | ISBSF_CASH_ACTS_15 | NUMERIC | 8 | 2 | — |
| 29 | ISBSF_CASH_ACTS_16 | NUMERIC | 8 | 2 | — |
| 30 | ISBSF_CASH_ACTS_17 | NUMERIC | 8 | 2 | — |
| 31 | ISBSF_CASH_ACTS_18 | NUMERIC | 8 | 2 | — |
| 32 | ISBSF_CASH_ACTS_19 | NUMERIC | 8 | 2 | — |
| 33 | ISBSF_CASH_ACTS_2 | NUMERIC | 8 | 2 | — |
| 34 | ISBSF_CASH_ACTS_20 | NUMERIC | 8 | 2 | — |
| 35 | ISBSF_CASH_ACTS_21 | NUMERIC | 8 | 2 | — |
| 36 | ISBSF_CASH_ACTS_22 | NUMERIC | 8 | 2 | — |
| 37 | ISBSF_CASH_ACTS_23 | NUMERIC | 8 | 2 | — |
| 38 | ISBSF_CASH_ACTS_24 | NUMERIC | 8 | 2 | — |
| 39 | ISBSF_CASH_ACTS_25 | NUMERIC | 8 | 2 | — |
| 40 | ISBSF_CASH_ACTS_26 | NUMERIC | 8 | 2 | — |
| 41 | ISBSF_CASH_ACTS_27 | NUMERIC | 8 | 2 | — |
| 42 | ISBSF_CASH_ACTS_28 | NUMERIC | 8 | 2 | — |
| 43 | ISBSF_CASH_ACTS_29 | NUMERIC | 8 | 2 | — |
| 44 | ISBSF_CASH_ACTS_3 | NUMERIC | 8 | 2 | — |
| 45 | ISBSF_CASH_ACTS_30 | NUMERIC | 8 | 2 | — |
| 46 | ISBSF_CASH_ACTS_31 | NUMERIC | 8 | 2 | — |
| 47 | ISBSF_CASH_ACTS_32 | NUMERIC | 8 | 2 | — |
| 48 | ISBSF_CASH_ACTS_33 | NUMERIC | 8 | 2 | — |
| 49 | ISBSF_CASH_ACTS_34 | NUMERIC | 8 | 2 | — |
| 50 | ISBSF_CASH_ACTS_35 | NUMERIC | 8 | 2 | — |
| 51 | ISBSF_CASH_ACTS_36 | NUMERIC | 8 | 2 | — |
| 52 | ISBSF_CASH_ACTS_37 | NUMERIC | 8 | 2 | — |
| 53 | ISBSF_CASH_ACTS_38 | NUMERIC | 8 | 2 | — |
| 54 | ISBSF_CASH_ACTS_39 | NUMERIC | 8 | 2 | — |
| 55 | ISBSF_CASH_ACTS_4 | NUMERIC | 8 | 2 | — |
| 56 | ISBSF_CASH_ACTS_40 | NUMERIC | 8 | 2 | — |
| 57 | ISBSF_CASH_ACTS_41 | NUMERIC | 8 | 2 | — |
| 58 | ISBSF_CASH_ACTS_42 | NUMERIC | 8 | 2 | — |
| 59 | ISBSF_CASH_ACTS_43 | NUMERIC | 8 | 2 | — |
| 60 | ISBSF_CASH_ACTS_44 | NUMERIC | 8 | 2 | — |
| 61 | ISBSF_CASH_ACTS_45 | NUMERIC | 8 | 2 | — |
| 62 | ISBSF_CASH_ACTS_46 | NUMERIC | 8 | 2 | — |
| 63 | ISBSF_CASH_ACTS_47 | NUMERIC | 8 | 2 | — |
| 64 | ISBSF_CASH_ACTS_48 | NUMERIC | 8 | 2 | — |
| 65 | ISBSF_CASH_ACTS_49 | NUMERIC | 8 | 2 | — |
| 66 | ISBSF_CASH_ACTS_5 | NUMERIC | 8 | 2 | — |
| 67 | ISBSF_CASH_ACTS_50 | NUMERIC | 8 | 2 | — |
| 68 | ISBSF_CASH_ACTS_51 | NUMERIC | 8 | 2 | — |
| 69 | ISBSF_CASH_ACTS_52 | NUMERIC | 8 | 2 | — |
| 70 | ISBSF_CASH_ACTS_53 | NUMERIC | 8 | 2 | — |
| 71 | ISBSF_CASH_ACTS_54 | NUMERIC | 8 | 2 | — |
| 72 | ISBSF_CASH_ACTS_55 | NUMERIC | 8 | 2 | — |
| 73 | ISBSF_CASH_ACTS_56 | NUMERIC | 8 | 2 | — |
| 74 | ISBSF_CASH_ACTS_57 | NUMERIC | 8 | 2 | — |
| 75 | ISBSF_CASH_ACTS_58 | NUMERIC | 8 | 2 | — |
| 76 | ISBSF_CASH_ACTS_59 | NUMERIC | 8 | 2 | — |
| 77 | ISBSF_CASH_ACTS_6 | NUMERIC | 8 | 2 | — |
| 78 | ISBSF_CASH_ACTS_60 | NUMERIC | 8 | 2 | — |
| 79 | ISBSF_CASH_ACTS_61 | NUMERIC | 8 | 2 | — |
| 80 | ISBSF_CASH_ACTS_62 | NUMERIC | 8 | 2 | — |
| 81 | ISBSF_CASH_ACTS_63 | NUMERIC | 8 | 2 | — |
| 82 | ISBSF_CASH_ACTS_64 | NUMERIC | 8 | 2 | — |
| 83 | ISBSF_CASH_ACTS_65 | NUMERIC | 8 | 2 | — |
| 84 | ISBSF_CASH_ACTS_66 | NUMERIC | 8 | 2 | — |
| 85 | ISBSF_CASH_ACTS_67 | NUMERIC | 8 | 2 | — |
| 86 | ISBSF_CASH_ACTS_68 | NUMERIC | 8 | 2 | — |
| 87 | ISBSF_CASH_ACTS_69 | NUMERIC | 8 | 2 | — |
| 88 | ISBSF_CASH_ACTS_7 | NUMERIC | 8 | 2 | — |
| 89 | ISBSF_CASH_ACTS_70 | NUMERIC | 8 | 2 | — |
| 90 | ISBSF_CASH_ACTS_71 | NUMERIC | 8 | 2 | — |
| 91 | ISBSF_CASH_ACTS_72 | NUMERIC | 8 | 2 | — |
| 92 | ISBSF_CASH_ACTS_73 | NUMERIC | 8 | 2 | — |
| 93 | ISBSF_CASH_ACTS_74 | NUMERIC | 8 | 2 | — |
| 94 | ISBSF_CASH_ACTS_75 | NUMERIC | 8 | 2 | — |
| 95 | ISBSF_CASH_ACTS_76 | NUMERIC | 8 | 2 | — |
| 96 | ISBSF_CASH_ACTS_77 | NUMERIC | 8 | 2 | — |
| 97 | ISBSF_CASH_ACTS_78 | NUMERIC | 8 | 2 | — |
| 98 | ISBSF_CASH_ACTS_79 | NUMERIC | 8 | 2 | — |
| 99 | ISBSF_CASH_ACTS_8 | NUMERIC | 8 | 2 | — |
| 100 | ISBSF_CASH_ACTS_80 | NUMERIC | 8 | 2 | — |
| 101 | ISBSF_CASH_ACTS_81 | NUMERIC | 8 | 2 | — |
| 102 | ISBSF_CASH_ACTS_82 | NUMERIC | 8 | 2 | — |
| 103 | ISBSF_CASH_ACTS_83 | NUMERIC | 8 | 2 | — |
| 104 | ISBSF_CASH_ACTS_84 | NUMERIC | 8 | 2 | — |
| 105 | ISBSF_CASH_ACTS_85 | NUMERIC | 8 | 2 | — |
| 106 | ISBSF_CASH_ACTS_86 | NUMERIC | 8 | 2 | — |
| 107 | ISBSF_CASH_ACTS_87 | NUMERIC | 8 | 2 | — |
| 108 | ISBSF_CASH_ACTS_88 | NUMERIC | 8 | 2 | — |
| 109 | ISBSF_CASH_ACTS_89 | NUMERIC | 8 | 2 | — |
| 110 | ISBSF_CASH_ACTS_9 | NUMERIC | 8 | 2 | — |
| 111 | ISBSF_CASH_ACTS_90 | NUMERIC | 8 | 2 | — |
| 112 | ISBSF_CASH_ACTS_91 | NUMERIC | 8 | 2 | — |
| 113 | ISBSF_CASH_ACTS_92 | NUMERIC | 8 | 2 | — |
| 114 | ISBSF_CASH_ACTS_93 | NUMERIC | 8 | 2 | — |
| 115 | ISBSF_CASH_ACTS_94 | NUMERIC | 8 | 2 | — |
| 116 | ISBSF_CASH_ACTS_95 | NUMERIC | 8 | 2 | — |
| 117 | ISBSF_CASH_ACTS_96 | NUMERIC | 8 | 2 | — |
| 118 | ISBSF_CASH_ACTS_97 | NUMERIC | 8 | 2 | — |
| 119 | ISBSF_CASH_ACTS_98 | NUMERIC | 8 | 2 | — |
| 120 | ISBSF_CASH_ACTS_99 | NUMERIC | 8 | 2 | — |
| 121 | ISBSF_CASH_TOTA | NUMERIC | 8 | 2 | — |
| 122 | ISBSF_ENDDATE | DATE | 4 | — | — |
| 123 | ISBSF_EXTRA | STRING | 100 | — | — |
| 124 | ISBSF_IC_VALUE | NUMERIC | 8 | 2 | — |
| 125 | ISBSF_PO_BOOK | NUMERIC | 8 | 2 | — |
| 126 | ISBSF_PO_OPEN | NUMERIC | 8 | 2 | — |
| 127 | ISBSF_PO_RECP | NUMERIC | 8 | 2 | — |
| 128 | ISBSF_SO_BOOK | NUMERIC | 8 | 2 | — |
| 129 | ISBSF_SO_OPEN | NUMERIC | 8 | 2 | — |
| 130 | ISBSF_SO_SHIP | NUMERIC | 8 | 2 | — |
| 131 | ISBSF_STARTDATE | DATE | 4 | — | — |
| 132 | ISBSF_WO_FPVAR | NUMERIC | 8 | 2 | — |
| 133 | ISBSF_WO_ISSU | NUMERIC | 8 | 2 | — |
| 134 | ISBSF_WO_WIPBAL | NUMERIC | 8 | 2 | — |
| 135 | ISBSF_WOS_FOH | NUMERIC | 8 | 2 | — |
| 136 | ISBSF_WOS_FP | NUMERIC | 8 | 2 | — |
| 137 | ISBSF_WOS_LAB | NUMERIC | 8 | 2 | — |
| 138 | ISBSF_WOS_MAT | NUMERIC | 8 | 2 | — |
| 139 | ISBSF_WOS_MEXT | NUMERIC | 8 | 2 | — |
| 140 | ISBSF_WOS_OUTP | NUMERIC | 8 | 2 | — |
| 141 | ISBSF_WOS_SETUP | NUMERIC | 8 | 2 | — |
| 142 | ISBSF_WOS_VOH | NUMERIC | 8 | 2 | — |
| 143 | ISBSF_WOS_WIPV | NUMERIC | 8 | 2 | — |
