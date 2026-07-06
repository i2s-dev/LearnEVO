# GL — General Ledger: Field Reference

Status: verified-schema

Source: `Evo-DBA_File_Fields 052421.xlsx`, sheet "Fields".
Field descriptions where provided by source; otherwise name-inferred.

Pass 574k-7: all blanks filled. Identical-schema tables collapsed to cross-references.

---

## BKGLACHK
**ARCHIVED CHECK REGISTER**

Fields: 11

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKGL_CHK_AMT | NUMERIC | 8 | 2 | Amount |
| 2 | BKGL_CHK_CHKACT | INTEGER | 2 | — | Checking Accoun Num |
| 3 | BKGL_CHK_CUST | STRING | 10 | — | Customer code (check issued to customer, e.g. refund) |
| 4 | BKGL_CHK_DATE | DATE | 4 | — | Date |
| 5 | BKGL_CHK_DATER | DATE | 4 | — | Reconciliation / return date |
| 6 | BKGL_CHK_EXTRA | STRING | 100 | — | Extra/custom data |
| 7 | BKGL_CHK_FLAG | STRING | 1 | — | Reconciled Y/N |
| 8 | BKGL_CHK_NAME | STRING | 25 | — | Pay to Name |
| 9 | BKGL_CHK_NUM | NUMERIC | 8 | — | Check Number |
| 10 | BKGL_CHK_TYPE | STRING | 1 | — | Type |
| 11 | BKGL_CHK_VEND | STRING | 10 | — | Vendor code (check issued to vendor) |

## BKGLAGJL
**ARCHIVED GJ LINES**

Fields: 9

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKGL_GJL_ACCTNM | STRING | 10 | — | GL Account Number |
| 2 | BKGL_GJL_AMOUNT | NUMERIC | 8 | 2 | Amount |
| 3 | BKGL_GJL_DC | STRING | 1 | — | Debit/Credit |
| 4 | BKGL_GJL_DESC | STRING | 25 | — | GL Description |
| 5 | BKGL_GJL_EXTRA | STRING | 50 | — | Extra/custom data |
| 6 | BKGL_GJL_GLDPT | STRING | 4 | — | GL Department |
| 7 | BKGL_GJL_JOB | STRING | 15 | — | Job number cross-reference |
| 8 | BKGL_GJL_LINE | INTEGER | 2 | — | Line number within journal entry |
| 9 | BKGL_GJL_TRANSN | NUMERIC | 8 | — | Gen Journal Transaction Number |

## BKGLAGJR
**ARCHIVED GJ HEADER**

Fields: 11

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKGL_GJ_AMT | NUMERIC | 8 | 2 | Amount |
| 2 | BKGL_GJ_DATE | DATE | 4 | — | Date |
| 3 | BKGL_GJ_DESC | STRING | 25 | — | Description |
| 4 | BKGL_GJ_DRCR | STRING | 1 | — | Debit/Credit Indicator |
| 5 | BKGL_GJ_EXTRA | STRING | 25 | — | Extra/custom data |
| 6 | BKGL_GJ_JOB | STRING | 15 | — | Job number cross-reference |
| 7 | BKGL_GJ_LINES | INTEGER | 2 | — | Number of Lines |
| 8 | BKGL_GJ_PERIOD | INTEGER | 2 | — | Period |
| 9 | BKGL_GJ_POSTDT | DATE | 4 | — | Post Date |
| 10 | BKGL_GJ_SOURCE | STRING | 10 | — | Source |
| 11 | BKGL_GJ_TRXN | NUMERIC | 8 | — | Transaction Number |

## BKGLATRN
**ARCHIVED GL TRANSACTIONS**

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
| 12 | BKGL_TRN_PART | STRING | 15 | — | Part number on GL transaction |
| 13 | BKGL_TRN_PERIOD | INTEGER | 2 | — | Period |
| 14 | BKGL_TRN_POSTDT | DATE | 4 | — | Post Date |
| 15 | BKGL_TRN_TRXN | NUMERIC | 8 | — | Transaction Number |
| 16 | BKGL_TRN_YEAR | INTEGER | 2 | — | Year |

## BKGLCCOA
**CONSOLIDATED CHART OF ACCOUNTS (Temporary)**

Fields: 62 | Prefix: BKGLC_

Period arrays (1YPAST/2YPAST/BUDGET/CURRENT × 14 periods each = 56 fields):
14 periods = 12 accounting months + 2 year-end adjusting entry slots.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1–14 | BKGLC_1YPAST_1..14 | NUMERIC | 8 | 2 | Prior year period amounts, periods 1–14 |
| 15–28 | BKGLC_2YPAST_1..14 | NUMERIC | 8 | 2 | 2-years-prior period amounts, periods 1–14 |
| 29 | BKGLC_ACCT | STRING | 10 | — | GL Account Code |
| 30 | BKGLC_ACCTD | STRING | 25 | — | Account Description |
| 31–44 | BKGLC_BUDGET_1..14 | NUMERIC | 8 | 2 | Budget amounts by period, periods 1–14 |
| 45 | BKGLC_CR_DR | STRING | 1 | — | Normal Credit/Debit |
| 46–59 | BKGLC_CURRENT_1..14 | NUMERIC | 8 | 2 | Current year period amounts, periods 1–14 |
| 60 | BKGLC_GLDPT | STRING | 4 | — | GL Department |
| 61 | BKGLC_NON_CASH | STRING | 1 | — | Non Cash Y/N |
| 62 | BKGLC_TYPE | STRING | 1 | — | Account Type (ALOIE) |

## BKGLCHK
**CHECKING ACCOUNT REGISTER**

Identical schema to [BKGLACHK](#bkglachk) (BKGL_CHK_ prefix). Live (non-archived) check register.

## BKGLCOA
**CHART OF ACCOUNTS**

Fields: 65 | Prefix: BKGL_

Same four period arrays as BKGLCCOA (BKGLC_ → BKGL_), plus three additional _YE fields.
14 periods = 12 months + 2 year-end adjusting entry slots.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1–14 | BKGL_1YPAST_1..14 | NUMERIC | 8 | 2 | Prior year period amounts, periods 1–14 |
| — | BKGL_1YPAST_YE | NUMERIC | 8 | 2 | Prior year year-end adjusting entry amount |
| 15–28 | BKGL_2YPAST_1..14 | NUMERIC | 8 | 2 | 2-years-prior period amounts, periods 1–14 |
| — | BKGL_2YPAST_YE | NUMERIC | 8 | 2 | 2-years-prior year-end adjusting entry amount |
| — | BKGL_ACCT | STRING | 10 | — | GL Account Number |
| — | BKGL_ACCTD | STRING | 25 | — | Account Description |
| 29–42 | BKGL_BUDGET_1..14 | NUMERIC | 8 | 2 | Budget amounts by period, periods 1–14 |
| — | BKGL_BUDGET_YE | NUMERIC | 8 | 2 | Budget year-end adjusting entry amount |
| — | BKGL_CR_DR | STRING | 1 | — | Normal Credit/Debit Balance |
| 43–56 | BKGL_CURRENT_1..14 | NUMERIC | 8 | 2 | Current year period amounts, periods 1–14 |
| — | BKGL_GLDPT | STRING | 4 | — | GL Department |
| — | BKGL_NON_CASH | STRING | 1 | — | Non Cash Y/N |
| — | BKGL_TYPE | STRING | 1 | — | Account Type (ALOIE) |

## BKGLDESC
**GL DESCRIPTION TABLE**

Fields: 5

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BK_DESC_EXTRA | STRING | 100 | — | Extra |
| 2 | BK_DESC_GLDPT | STRING | 4 | — | GL Department |
| 3 | BK_DESC_GLACCT | STRING | 10 | — | GL Account |
| 4 | BK_DESC_MODULE | STRING | 2 | — | Module |
| 5 | BK_DESC_TEXT | STRING | 25 | — | Description Text |

## BKGLFCOA
**FINANCIAL COA**

Identical schema to [BKGLCOA](#bkglcoa) (BKGL_ prefix). Alternate/financial company COA copy.

## BKGLFSTL
**FINANCIAL STATEMENT LINES**

Fields: 12

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKFS_ACCT_FROM | STRING | 10 | — | Account From |
| 2 | BKFS_ACCT_TO | STRING | 10 | — | Account To |
| 3 | BKFS_DEPT_FROM | STRING | 4 | — | Dept From |
| 4 | BKFS_DEPT_TO | STRING | 4 | — | Dept To |
| 5 | BKFS_EXTRA | STRING | 25 | — | Extra |
| 6 | BKFS_FMTCD | STRING | 1 | — | Format Code |
| 7 | BKFS_INDENT | INTEGER | 2 | — | Indent Level |
| 8 | BKFS_LINE_NUM | INTEGER | 2 | — | Line number in financial statement definition |
| 9 | BKFS_PRINT | STRING | 1 | — | Print Y/N |
| 10 | BKFS_RPTNUM | STRING | 10 | — | Report Number |
| 11 | BKFS_TITLE | STRING | 40 | — | Title |
| 12 | BKFS_TYPE | STRING | 1 | — | Line Type |

## BKGLGJLN
**GJ LINES**

Identical schema to [BKGLAGJL](#bkglagjl) (BKGL_GJL_ prefix). Live (non-archived) GJ lines.

## BKGLGJRN
**GJ HEADER**

Identical schema to [BKGLAGJR](#bkglagjr) (BKGL_GJ_ prefix). Live (non-archived) GJ headers.

## BKGLRGJL
**RECURRING GJ LINES**

Identical schema to [BKGLAGJL](#bkglagjl) (BKGL_GJL_ prefix). Recurring journal entry lines.

## BKGLRGJR
**RECURRING GJ HEADER**

Identical schema to [BKGLAGJR](#bkglagjr) (BKGL_GJ_ prefix). Recurring journal entry headers.

## BKGLSTMT
**FINANCIAL STATEMENT SETUP**

Fields: 104

Three sections define the three standard financial reports:
- **STB** = Balance Sheet (Assets/GLA, Liabilities/GLL, Owners Equity/GLO)
- **STC** = Statement of Changes (Assets/GLA, Liabilities/GLL, Net Income/GLI, Non-Cash/GLN)
- **STI** = Income Statement (Income/GLI, COGS/GLC, Expenses/GLE, Other Income/GLOI, Other Expense/GLOE, Tax/GLT)

Pattern: `_F_N` = account range "From" for group N; `_T_N` = account range "To" for group N; `_TTL_N` = subsection title string for group N; `_MT` = main section title.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKGL_STB_GLA_F_1 | STRING | 10 | — | Balance sheet assets: account range From, group 1 |
| 2 | BKGL_STB_GLA_F_2 | STRING | 10 | — | Balance sheet assets: account range From, group 2 |
| 3 | BKGL_STB_GLA_F_3 | STRING | 10 | — | Balance sheet assets: account range From, group 3 |
| 4 | BKGL_STB_GLA_F_4 | STRING | 10 | — | Balance sheet assets: account range From, group 4 |
| 5 | BKGL_STB_GLA_MT | STRING | 25 | — | Assets Main Title |
| 6 | BKGL_STB_GLA_T_1 | STRING | 10 | — | Balance sheet assets: account range To, group 1 |
| 7 | BKGL_STB_GLA_T_2 | STRING | 10 | — | Balance sheet assets: account range To, group 2 |
| 8 | BKGL_STB_GLA_T_3 | STRING | 10 | — | Balance sheet assets: account range To, group 3 |
| 9 | BKGL_STB_GLA_T_4 | STRING | 10 | — | Balance sheet assets: account range To, group 4 |
| 10 | BKGL_STB_GLATTL_1 | STRING | 25 | — | Balance sheet assets: subsection title, group 1 |
| 11 | BKGL_STB_GLATTL_2 | STRING | 25 | — | Balance sheet assets: subsection title, group 2 |
| 12 | BKGL_STB_GLATTL_3 | STRING | 25 | — | Balance sheet assets: subsection title, group 3 |
| 13 | BKGL_STB_GLATTL_4 | STRING | 25 | — | Balance sheet assets: subsection title, group 4 |
| 14 | BKGL_STB_GLL_F_1 | STRING | 10 | — | Balance sheet liabilities: account range From, group 1 |
| 15 | BKGL_STB_GLL_F_2 | STRING | 10 | — | Balance sheet liabilities: account range From, group 2 |
| 16 | BKGL_STB_GLL_F_3 | STRING | 10 | — | Balance sheet liabilities: account range From, group 3 |
| 17 | BKGL_STB_GLL_F_4 | STRING | 10 | — | Balance sheet liabilities: account range From, group 4 |
| 18 | BKGL_STB_GLL_MT | STRING | 25 | — | Liabilities Main Title |
| 19 | BKGL_STB_GLL_T_1 | STRING | 10 | — | Balance sheet liabilities: account range To, group 1 |
| 20 | BKGL_STB_GLL_T_2 | STRING | 10 | — | Balance sheet liabilities: account range To, group 2 |
| 21 | BKGL_STB_GLL_T_3 | STRING | 10 | — | Balance sheet liabilities: account range To, group 3 |
| 22 | BKGL_STB_GLL_T_4 | STRING | 10 | — | Balance sheet liabilities: account range To, group 4 |
| 23 | BKGL_STB_GLLTTL_1 | STRING | 25 | — | Balance sheet liabilities: subsection title, group 1 |
| 24 | BKGL_STB_GLLTTL_2 | STRING | 25 | — | Balance sheet liabilities: subsection title, group 2 |
| 25 | BKGL_STB_GLLTTL_3 | STRING | 25 | — | Balance sheet liabilities: subsection title, group 3 |
| 26 | BKGL_STB_GLLTTL_4 | STRING | 25 | — | Balance sheet liabilities: subsection title, group 4 |
| 27 | BKGL_STB_GLO_F_1 | STRING | 10 | — | Balance sheet owners equity: account range From, group 1 |
| 28 | BKGL_STB_GLO_F_2 | STRING | 10 | — | Balance sheet owners equity: account range From, group 2 |
| 29 | BKGL_STB_GLO_MT | STRING | 25 | — | Owners Equity Main Title |
| 30 | BKGL_STB_GLO_T_1 | STRING | 10 | — | Balance sheet owners equity: account range To, group 1 |
| 31 | BKGL_STB_GLO_T_2 | STRING | 10 | — | Balance sheet owners equity: account range To, group 2 |
| 32 | BKGL_STB_GLOTTL_1 | STRING | 25 | — | Balance sheet owners equity: subsection title, group 1 |
| 33 | BKGL_STB_GLOTTL_2 | STRING | 25 | — | Balance sheet owners equity: subsection title, group 2 |
| 34 | BKGL_STB_MN_TTL | STRING | 25 | — | Balance Sheet Report Title |
| 35 | BKGL_STC_GLA_F_1 | STRING | 10 | — | SOC assets: account range From, group 1 |
| 36 | BKGL_STC_GLA_F_2 | STRING | 10 | — | SOC assets: account range From, group 2 |
| 37 | BKGL_STC_GLA_F_3 | STRING | 10 | — | SOC assets: account range From, group 3 |
| 38 | BKGL_STC_GLA_F_4 | STRING | 10 | — | SOC assets: account range From, group 4 |
| 39 | BKGL_STC_GLA_MT | STRING | 25 | — | SofC Assets Main  Title |
| 40 | BKGL_STC_GLA_T_1 | STRING | 10 | — | SOC assets: account range To, group 1 |
| 41 | BKGL_STC_GLA_T_2 | STRING | 10 | — | SOC assets: account range To, group 2 |
| 42 | BKGL_STC_GLA_T_3 | STRING | 10 | — | SOC assets: account range To, group 3 |
| 43 | BKGL_STC_GLA_T_4 | STRING | 10 | — | SOC assets: account range To, group 4 |
| 44 | BKGL_STC_GLATTL_1 | STRING | 25 | — | SOC assets: subsection title, group 1 |
| 45 | BKGL_STC_GLATTL_2 | STRING | 25 | — | SOC assets: subsection title, group 2 |
| 46 | BKGL_STC_GLATTL_3 | STRING | 25 | — | SOC assets: subsection title, group 3 |
| 47 | BKGL_STC_GLATTL_4 | STRING | 25 | — | SOC assets: subsection title, group 4 |
| 48 | BKGL_STC_GLI_F | STRING | 10 | — | Net Income Acct From Range |
| 49 | BKGL_STC_GLI_T | STRING | 10 | — | Net Income To Range |
| 50 | BKGL_STC_GLITTL | STRING | 25 | — | Net Income Tittle |
| 51 | BKGL_STC_GLL_F_1 | STRING | 10 | — | SOC liabilities: account range From, group 1 |
| 52 | BKGL_STC_GLL_F_2 | STRING | 10 | — | SOC liabilities: account range From, group 2 |
| 53 | BKGL_STC_GLL_F_3 | STRING | 10 | — | SOC liabilities: account range From, group 3 |
| 54 | BKGL_STC_GLL_F_4 | STRING | 10 | — | SOC liabilities: account range From, group 4 |
| 55 | BKGL_STC_GLL_MT | STRING | 25 | — | SofC Liabilities Main Title |
| 56 | BKGL_STC_GLL_T_1 | STRING | 10 | — | SOC liabilities: account range To, group 1 |
| 57 | BKGL_STC_GLL_T_2 | STRING | 10 | — | SOC liabilities: account range To, group 2 |
| 58 | BKGL_STC_GLL_T_3 | STRING | 10 | — | SOC liabilities: account range To, group 3 |
| 59 | BKGL_STC_GLL_T_4 | STRING | 10 | — | SOC liabilities: account range To, group 4 |
| 60 | BKGL_STC_GLLTTL_1 | STRING | 25 | — | SOC liabilities: subsection title, group 1 |
| 61 | BKGL_STC_GLLTTL_2 | STRING | 25 | — | SOC liabilities: subsection title, group 2 |
| 62 | BKGL_STC_GLLTTL_3 | STRING | 25 | — | SOC liabilities: subsection title, group 3 |
| 63 | BKGL_STC_GLLTTL_4 | STRING | 25 | — | SOC liabilities: subsection title, group 4 |
| 64 | BKGL_STC_GLN_F | STRING | 10 | — | Non-Cash Acct From Range |
| 65 | BKGL_STC_GLN_T | STRING | 10 | — | Non-Cash Acct To Range |
| 66 | BKGL_STC_GLNTTL | STRING | 25 | — | Non-Cash Expense Title |
| 67 | BKGL_STC_MN_TTL | STRING | 25 | — | Statement of Change Main Title |
| 68 | BKGL_STI_GLC_F_1 | STRING | 10 | — | Income statement COGS: account range From, group 1 |
| 69 | BKGL_STI_GLC_F_2 | STRING | 10 | — | Income statement COGS: account range From, group 2 |
| 70 | BKGL_STI_GLC_MT | STRING | 25 | — | Cost of Goods Sold Main Title |
| 71 | BKGL_STI_GLC_T_1 | STRING | 10 | — | Income statement COGS: account range To, group 1 |
| 72 | BKGL_STI_GLC_T_2 | STRING | 10 | — | Income statement COGS: account range To, group 2 |
| 73 | BKGL_STI_GLCTTL_1 | STRING | 25 | — | Income statement COGS: subsection title, group 1 |
| 74 | BKGL_STI_GLCTTL_2 | STRING | 25 | — | Income statement COGS: subsection title, group 2 |
| 75 | BKGL_STI_GLE_F_1 | STRING | 10 | — | Income statement expenses: account range From, group 1 |
| 76 | BKGL_STI_GLE_F_2 | STRING | 10 | — | Income statement expenses: account range From, group 2 |
| 77 | BKGL_STI_GLE_F_3 | STRING | 10 | — | Income statement expenses: account range From, group 3 |
| 78 | BKGL_STI_GLE_F_4 | STRING | 10 | — | Income statement expenses: account range From, group 4 |
| 79 | BKGL_STI_GLE_MT | STRING | 25 | — | Expenses Main Title |
| 80 | BKGL_STI_GLE_T_1 | STRING | 10 | — | Income statement expenses: account range To, group 1 |
| 81 | BKGL_STI_GLE_T_2 | STRING | 10 | — | Income statement expenses: account range To, group 2 |
| 82 | BKGL_STI_GLE_T_3 | STRING | 10 | — | Income statement expenses: account range To, group 3 |
| 83 | BKGL_STI_GLE_T_4 | STRING | 10 | — | Income statement expenses: account range To, group 4 |
| 84 | BKGL_STI_GLETTL_1 | STRING | 25 | — | Income statement expenses: subsection title, group 1 |
| 85 | BKGL_STI_GLETTL_2 | STRING | 25 | — | Income statement expenses: subsection title, group 2 |
| 86 | BKGL_STI_GLETTL_3 | STRING | 25 | — | Income statement expenses: subsection title, group 3 |
| 87 | BKGL_STI_GLETTL_4 | STRING | 25 | — | Income statement expenses: subsection title, group 4 |
| 88 | BKGL_STI_GLI_F_1 | STRING | 10 | — | Income statement revenue: account range From, group 1 |
| 89 | BKGL_STI_GLI_F_2 | STRING | 10 | — | Income statement revenue: account range From, group 2 |
| 90 | BKGL_STI_GLI_MT | STRING | 25 | — | Income Statement Main Title |
| 91 | BKGL_STI_GLI_T_1 | STRING | 10 | — | Income statement revenue: account range To, group 1 |
| 92 | BKGL_STI_GLI_T_2 | STRING | 10 | — | Income statement revenue: account range To, group 2 |
| 93 | BKGL_STI_GLITTL_1 | STRING | 25 | — | Income statement revenue: subsection title, group 1 |
| 94 | BKGL_STI_GLITTL_2 | STRING | 25 | — | Income statement revenue: subsection title, group 2 |
| 95 | BKGL_STI_GLOE_F | STRING | 10 | — | Other Expense From |
| 96 | BKGL_STI_GLOE_T | STRING | 10 | — | Other Expense To |
| 97 | BKGL_STI_GLOETT | STRING | 25 | — | Other Expense Title |
| 98 | BKGL_STI_GLOI_F | STRING | 10 | — | Other Income From |
| 99 | BKGL_STI_GLOI_T | STRING | 10 | — | Other Income To |
| 100 | BKGL_STI_GLOITT | STRING | 25 | — | Other Income Title |
| 101 | BKGL_STI_GLT_F | STRING | 10 | — | Income statement tax: account range From |
| 102 | BKGL_STI_GLT_T | STRING | 10 | — | Income statement tax: account range To |
| 103 | BKGL_STI_GLTTTL | STRING | 25 | — | Income statement tax: section title |
| 104 | BKGL_STI_MN_TTL | STRING | 25 | — | Income Report Main Title |

## BKGLTEMP
**UNPOSTED GL TRANSACTIONS**

Identical schema to [BKGLATRN](#bkglatrn) (BKGL_TRN_ prefix). Unposted (pending) GL transactions.

## BKGLTGJL
**TEMPLATE GJ LINES**

Identical schema to [BKGLAGJL](#bkglagjl) (BKGL_GJL_ prefix). Template/model journal entry lines.

## BKGLTGJR
**TEMPLATE GJ HEADER**

Identical schema to [BKGLAGJR](#bkglagjr) (BKGL_GJ_ prefix). Template/model journal entry headers.

## BKGLTMP3
**GL TRANSACTIONS TEMP**

Identical schema to [BKGLATRN](#bkglatrn) (BKGL_TRN_ prefix). Secondary GL transaction temp table.

## BKGLTRAN
**GL TRANSACTIONS**

Identical schema to [BKGLATRN](#bkglatrn) (BKGL_TRN_ prefix). Live posted GL transaction ledger.

## BKGLX
**GL TRANSACTION DETAIL (Extended)**

Fields: 20 | Prefix: BKGLX_

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKGLX_AMOUNT | NUMERIC | 8 | 2 | Transaction amount |
| 2 | BKGLX_ARCHDATE | DATE | 4 | — | Archive date |
| 3 | BKGLX_BATCH | NUMERIC | 8 | — | Batch number |
| 4 | BKGLX_CCLASS | STRING | 5 | — | Customer class code |
| 5 | BKGLX_COMPANY | STRING | 10 | — | Company code |
| 6 | BKGLX_DESC | STRING | 25 | — | Description |
| 7 | BKGLX_ENTDATE | DATE | 4 | — | Entry date |
| 8 | BKGLX_ICLASS | STRING | 5 | — | Inventory class code |
| 9 | BKGLX_JOURNAL | STRING | 10 | — | Journal type code |
| 10 | BKGLX_PART | STRING | 15 | — | Part number |
| 11 | BKGLX_POINVC | STRING | 10 | — | PO invoice number |
| 12 | BKGLX_PONUM | STRING | 10 | — | PO number |
| 13 | BKGLX_POST | STRING | 1 | — | Posted flag |
| 14 | BKGLX_POSTDATE | DATE | 4 | — | GL post date |
| 15 | BKGLX_QUANTITY | NUMERIC | 8 | 2 | Quantity |
| 16 | BKGLX_SOINVC | STRING | 10 | — | SO invoice number |
| 17 | BKGLX_TRXN | NUMERIC | 8 | — | Transaction number |
| 18 | BKGLX_TRXNTYPE | STRING | 2 | — | Transaction type code |
| 19 | BKGLX_WOPRE | STRING | 2 | — | Work order prefix |
| 20 | BKGLX_WOSUF | NUMERIC | 8 | — | Work order suffix |

## BKGLXH
**GL TRANSACTION DETAIL HISTORY (Extended)**

Identical schema to [BKGLX](#bkglx) (BKGLX_ prefix). Archived/historical extended GL transaction detail.

## ISBANKS
**BANK MASTER**

Fields: 23 | Prefix: IS_BANKS_

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_BANKS_ACCT | STRING | 20 | — | Bank account number |
| 2 | IS_BANKS_ACTIVE | STRING | 1 | — | Active flag (Y/N) |
| 3 | IS_BANKS_AP | STRING | 1 | — | Used for AP payments (Y/N) |
| 4 | IS_BANKS_AR | STRING | 1 | — | Used for AR receipts (Y/N) |
| 5 | IS_BANKS_BAL | NUMERIC | 8 | 2 | Current balance |
| 6 | IS_BANKS_CURR | STRING | 3 | — | Currency code |
| 7 | IS_BANKS_DESC | STRING | 30 | — | Bank description |
| 8 | IS_BANKS_EXTRA | STRING | 50 | — | Extra/custom data |
| 9 | IS_BANKS_GLA | STRING | 10 | — | GL account code |
| 10 | IS_BANKS_GLD | STRING | 4 | — | GL department |
| 11 | IS_BANKS_INC_BS | STRING | 1 | — | Include on balance sheet (Y/N) |
| 12 | IS_BANKS_NUM | STRING | 5 | — | Bank number (PK) |
| 13 | IS_BANKS_NXTNUM | NUMERIC | 8 | — | Next check number |
| 14 | IS_BANKS_PR | STRING | 1 | — | Used for payroll (Y/N) |
| 15 | IS_BANKS_ROUT | STRING | 9 | — | Bank routing number |
| 16 | IS_BANKS_RTM_1 | STRING | 10 | — | Check print report template name, slot 1 |
| 17 | IS_BANKS_RTM_2 | STRING | 10 | — | Check print report template name, slot 2 |
| 18 | IS_BANKS_RTM_3 | STRING | 10 | — | Check print report template name, slot 3 |
| 19 | IS_BANKS_RTM_4 | STRING | 10 | — | Check print report template name, slot 4 |
| 20 | IS_BANKS_RTM_5 | STRING | 10 | — | Check print report template name, slot 5 |
| 21 | IS_BANKS_SRT | INTEGER | 2 | — | Sort order |
| 22 | IS_BANKS_TYPE | STRING | 1 | — | Bank account type (C=checking, S=savings) |
| 23 | IS_BANKS_VEND | STRING | 10 | — | Vendor code for bank (used in reconciliation) |

## ISBSF
**EVO BUSINESS STATUS SUMMARY**

Fields: 143 | Prefix: ISBSF_

Period-level financial summary across all modules (AP/AR/PO/SO/WO/IC/Cash).
CASH_ACT1..9 = legacy short-key slots; CASH_ACTS_1..100 = full 100-slot bank balance array.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISBSF_AP_ATP | NUMERIC | 8 | 2 | AP available-to-pay balance |
| 2 | ISBSF_AP_BAL | NUMERIC | 8 | 2 | AP outstanding balance |
| 3 | ISBSF_AP_DISC | NUMERIC | 8 | 2 | AP discounts taken this period |
| 4 | ISBSF_AP_PAYA | NUMERIC | 8 | 2 | AP payables total |
| 5 | ISBSF_AP_PAYM | NUMERIC | 8 | 2 | AP payments total |
| 6 | ISBSF_AR_BAL | NUMERIC | 8 | 2 | AR outstanding balance |
| 7 | ISBSF_AR_BILL | NUMERIC | 8 | 2 | AR billings total |
| 8 | ISBSF_AR_COGS | NUMERIC | 8 | 2 | AR cost of goods sold |
| 9 | ISBSF_AR_DEPO | NUMERIC | 8 | 2 | AR deposits total |
| 10 | ISBSF_AR_DISC | NUMERIC | 8 | 2 | AR discounts given this period |
| 11 | ISBSF_AR_RECP | NUMERIC | 8 | 2 | AR receipts total |
| 12 | ISBSF_CASH_ACT1 | NUMERIC | 8 | 2 | Cash balance for bank account slot 1 (legacy) |
| 13 | ISBSF_CASH_ACT2 | NUMERIC | 8 | 2 | Cash balance for bank account slot 2 (legacy) |
| 14 | ISBSF_CASH_ACT3 | NUMERIC | 8 | 2 | Cash balance for bank account slot 3 (legacy) |
| 15 | ISBSF_CASH_ACT4 | NUMERIC | 8 | 2 | Cash balance for bank account slot 4 (legacy) |
| 16 | ISBSF_CASH_ACT5 | NUMERIC | 8 | 2 | Cash balance for bank account slot 5 (legacy) |
| 17 | ISBSF_CASH_ACT6 | NUMERIC | 8 | 2 | Cash balance for bank account slot 6 (legacy) |
| 18 | ISBSF_CASH_ACT7 | NUMERIC | 8 | 2 | Cash balance for bank account slot 7 (legacy) |
| 19 | ISBSF_CASH_ACT8 | NUMERIC | 8 | 2 | Cash balance for bank account slot 8 (legacy) |
| 20 | ISBSF_CASH_ACT9 | NUMERIC | 8 | 2 | Cash balance for bank account slot 9 (legacy) |
| 21–120 | ISBSF_CASH_ACTS_1..100 | NUMERIC | 8 | 2 | Cash balance for bank account slot 1–100 (full array, FK→ISBANKS) |
| 121 | ISBSF_CASH_TOTA | NUMERIC | 8 | 2 | Total cash across all bank accounts |
| 122 | ISBSF_ENDDATE | DATE | 4 | — | Period end date |
| 123 | ISBSF_EXTRA | STRING | 100 | — | Extra/custom data |
| 124 | ISBSF_IC_VALUE | NUMERIC | 8 | 2 | Inventory carrying value |
| 125 | ISBSF_PO_BOOK | NUMERIC | 8 | 2 | PO booked value (open purchase orders) |
| 126 | ISBSF_PO_OPEN | NUMERIC | 8 | 2 | PO open value (unreceipted) |
| 127 | ISBSF_PO_RECP | NUMERIC | 8 | 2 | PO receipts value this period |
| 128 | ISBSF_SO_BOOK | NUMERIC | 8 | 2 | SO booked value (open sales orders) |
| 129 | ISBSF_SO_OPEN | NUMERIC | 8 | 2 | SO open value (unshipped) |
| 130 | ISBSF_SO_SHIP | NUMERIC | 8 | 2 | SO shipped value this period |
| 131 | ISBSF_STARTDATE | DATE | 4 | — | Period start date |
| 132 | ISBSF_WO_FPVAR | NUMERIC | 8 | 2 | WO finished product variance |
| 133 | ISBSF_WO_ISSU | NUMERIC | 8 | 2 | WO materials issued value |
| 134 | ISBSF_WO_WIPBAL | NUMERIC | 8 | 2 | WO WIP balance |
| 135 | ISBSF_WOS_FOH | NUMERIC | 8 | 2 | WO status: fixed overhead cost |
| 136 | ISBSF_WOS_FP | NUMERIC | 8 | 2 | WO status: finished product value |
| 137 | ISBSF_WOS_LAB | NUMERIC | 8 | 2 | WO status: labor cost |
| 138 | ISBSF_WOS_MAT | NUMERIC | 8 | 2 | WO status: material cost |
| 139 | ISBSF_WOS_MEXT | NUMERIC | 8 | 2 | WO status: material extra cost |
| 140 | ISBSF_WOS_OUTP | NUMERIC | 8 | 2 | WO status: output value |
| 141 | ISBSF_WOS_SETUP | NUMERIC | 8 | 2 | WO status: setup cost |
| 142 | ISBSF_WOS_VOH | NUMERIC | 8 | 2 | WO status: variable overhead cost |
| 143 | ISBSF_WOS_WIPV | NUMERIC | 8 | 2 | WO status: WIP variance |

## ISGLBDGT
**MULTI-YEAR BUDGET**

Fields: 67 | Prefix: ISGL_

Extended COA budget history for years 3–6 prior. Paired with BKGLCOA which holds years 1–2.
14 periods = 12 months + 2 year-end adjusting entry slots.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1–14 | ISGL_3YPAST_1..14 | NUMERIC | 8 | 2 | Budget amounts 3 years prior, periods 1–14 |
| 15 | ISGL_3YPAST_YE | NUMERIC | 8 | 2 | Budget amount 3 years prior, year-end adjusting entry |
| 16–29 | ISGL_4YPAST_1..14 | NUMERIC | 8 | 2 | Budget amounts 4 years prior, periods 1–14 |
| 30 | ISGL_4YPAST_YE | NUMERIC | 8 | 2 | Budget amount 4 years prior, year-end adjusting entry |
| 31–44 | ISGL_5YPAST_1..14 | NUMERIC | 8 | 2 | Budget amounts 5 years prior, periods 1–14 |
| 45 | ISGL_5YPAST_YE | NUMERIC | 8 | 2 | Budget amount 5 years prior, year-end adjusting entry |
| 46–59 | ISGL_6YPAST_1..14 | NUMERIC | 8 | 2 | Budget amounts 6 years prior, periods 1–14 |
| 60 | ISGL_6YPAST_YE | NUMERIC | 8 | 2 | Budget amount 6 years prior, year-end adjusting entry |
| 61 | ISGL_ACCT | STRING | 10 | — | GL account number (PK) |
| 62 | ISGL_ACCTD | STRING | 25 | — | Account description |
| 63 | ISGL_CEXTRA | STRING | 100 | — | Extra/custom data |
| 64 | ISGL_CR_DR | STRING | 1 | — | Normal credit/debit balance indicator |
| 65 | ISGL_GLDPT | STRING | 4 | — | GL department |
| 66 | ISGL_NON_CASH | STRING | 1 | — | Non-cash account flag (Y/N) |
| 67 | ISGL_TYPE | STRING | 1 | — | Account type (ALOIE) |

## ISGLCOA
**CHART OF ACCOUNTS 3-6 YR PAST**

Identical schema to [ISGLBDGT](#isglbdgt) (ISGL_ prefix). Actual period amounts for years 3–6 prior (vs. ISGLBDGT which holds budget).

## ISGLDATE
**FISCAL PERIOD DATES**

Fields: 86 | Prefix: ISGL_

Stores the period end dates for up to 7 fiscal years (current + 6 prior). 12 periods per year.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1–12 | ISGL_CYDATE_1..12 | DATE | 4 | — | Current year fiscal period end dates, periods 1–12 |
| 13–24 | ISGL_1YDATE_1..12 | DATE | 4 | — | 1-year-prior fiscal period end dates, periods 1–12 |
| 25–36 | ISGL_2YDATE_1..12 | DATE | 4 | — | 2-years-prior fiscal period end dates, periods 1–12 |
| 37–48 | ISGL_3YDATE_1..12 | DATE | 4 | — | 3-years-prior fiscal period end dates, periods 1–12 |
| 49–60 | ISGL_4YDATE_1..12 | DATE | 4 | — | 4-years-prior fiscal period end dates, periods 1–12 |
| 61–72 | ISGL_5YDATE_1..12 | DATE | 4 | — | 5-years-prior fiscal period end dates, periods 1–12 |
| 73–84 | ISGL_6YDATE_1..12 | DATE | 4 | — | 6-years-prior fiscal period end dates, periods 1–12 |
| 85 | ISGL_EXTRA | STRING | 50 | — | Extra/custom data |
| 86 | ISGL_FYDATE | DATE | 4 | — | Fiscal year start date |

## ISGLHDAT
**HISTORICAL FISCAL PERIOD DATES**

Identical schema to [ISGLDATE](#isgldate) (ISGL_ prefix). Historical archive of a prior year's period date configuration.

## ISJBSF
**EVO BUSINESS STATUS**

Identical schema to [ISBSF](#isbsf) (ISBSF_ prefix). Journal/working-set copy of the business status summary, accumulated before period close.
