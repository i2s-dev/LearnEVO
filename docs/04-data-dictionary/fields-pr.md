# PR — Payroll: Field Reference

Status: verified-schema

Source: `Evo-DBA_File_Fields 052421.xlsx`, sheet "Fields".
Field descriptions where provided by source; otherwise name-inferred.

---

## BKPRCURP
**CURRENT PAYROLL INFORMATION (Temporary)**

Fields: 127

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKPR_CURP_ACTNM | INTEGER | 2 | — | Bank account slot number for this paycheck |
| 2 | BKPR_CURP_CHKNM | STRING | 6 | — | Check number |
| 3 | BKPR_CURP_EIC | NUMERIC | 8 | 2 | Earned income credit advance payment |
| 4 | BKPR_CURP_EMPNM | INTEGER | 2 | — | Employee number |
| 5 | BKPR_CURP_FICEX_1 | NUMERIC | 8 | 2 | FICA excess contribution (slot 1) for current pay period |
| 6 | BKPR_CURP_FICEX_2 | NUMERIC | 8 | 2 | FICA excess contribution (slot 2) for current pay period |
| 7 | BKPR_CURP_FICWH_1 | NUMERIC | 8 | 2 | FICA withheld (SS=1/Medicare=2) for current pay period |
| 8 | BKPR_CURP_FICWH_2 | NUMERIC | 8 | 2 | FICA withheld (SS=1/Medicare=2) for current pay period |
| 9 | BKPR_CURP_FITWH | NUMERIC | 8 | 2 | Federal income tax withheld |
| 10 | BKPR_CURP_FUTEX | NUMERIC | 8 | 2 | FUTA (federal unemployment) tax expense |
| 11 | BKPR_CURP_MDACT | STRING | 10 | — | Medical deduction GL account |
| 12 | BKPR_CURP_MDAMT | NUMERIC | 8 | 2 | Medical deduction amount |
| 13 | BKPR_CURP_MDDPT | STRING | 4 | — | Medical deduction GL department |
| 14 | BKPR_CURP_MDNME | STRING | 12 | — | Medical deduction name |
| 15 | BKPR_CURP_NTPAY | NUMERIC | 8 | 2 | Net pay amount |
| 16 | BKPR_CURP_ODACT | STRING | 10 | — | Other deduction GL account |
| 17 | BKPR_CURP_ODAMT | NUMERIC | 8 | 2 | Other deduction amount |
| 18 | BKPR_CURP_ODDPT | STRING | 4 | — | Other deduction GL department |
| 19 | BKPR_CURP_ODNME | STRING | 12 | — | Other deduction name |
| 20 | BKPR_CURP_OPACT_1 | STRING | 10 | — | Other pay type 1 GL account for current pay period |
| 21 | BKPR_CURP_OPACT_2 | STRING | 10 | — | Other pay type 2 GL account for current pay period |
| 22 | BKPR_CURP_OPACT_3 | STRING | 10 | — | Other pay type 3 GL account for current pay period |
| 23 | BKPR_CURP_OPACT_4 | STRING | 10 | — | Other pay type 4 GL account for current pay period |
| 24 | BKPR_CURP_OPACT_5 | STRING | 10 | — | Other pay type 5 GL account for current pay period |
| 25 | BKPR_CURP_OPAMT_1 | NUMERIC | 8 | 2 | Other pay type 1 amount for current pay period |
| 26 | BKPR_CURP_OPAMT_10 | NUMERIC | 8 | 2 | Other pay type 10 amount for current pay period |
| 27 | BKPR_CURP_OPAMT_11 | NUMERIC | 8 | 2 | Other pay type 11 amount for current pay period |
| 28 | BKPR_CURP_OPAMT_12 | NUMERIC | 8 | 2 | Other pay type 12 amount for current pay period |
| 29 | BKPR_CURP_OPAMT_2 | NUMERIC | 8 | 2 | Other pay type 2 amount for current pay period |
| 30 | BKPR_CURP_OPAMT_3 | NUMERIC | 8 | 2 | Other pay type 3 amount for current pay period |
| 31 | BKPR_CURP_OPAMT_4 | NUMERIC | 8 | 2 | Other pay type 4 amount for current pay period |
| 32 | BKPR_CURP_OPAMT_5 | NUMERIC | 8 | 2 | Other pay type 5 amount for current pay period |
| 33 | BKPR_CURP_OPAMT_6 | NUMERIC | 8 | 2 | Other pay type 6 amount for current pay period |
| 34 | BKPR_CURP_OPAMT_7 | NUMERIC | 8 | 2 | Other pay type 7 amount for current pay period |
| 35 | BKPR_CURP_OPAMT_8 | NUMERIC | 8 | 2 | Other pay type 8 amount for current pay period |
| 36 | BKPR_CURP_OPAMT_9 | NUMERIC | 8 | 2 | Other pay type 9 amount for current pay period |
| 37 | BKPR_CURP_OPDPT_1 | STRING | 4 | — | Other pay type 1 GL department for current pay period |
| 38 | BKPR_CURP_OPDPT_2 | STRING | 4 | — | Other pay type 2 GL department for current pay period |
| 39 | BKPR_CURP_OPDPT_3 | STRING | 4 | — | Other pay type 3 GL department for current pay period |
| 40 | BKPR_CURP_OPDPT_4 | STRING | 4 | — | Other pay type 4 GL department for current pay period |
| 41 | BKPR_CURP_OPDPT_5 | STRING | 4 | — | Other pay type 5 GL department for current pay period |
| 42 | BKPR_CURP_OPHRS_1 | NUMERIC | 8 | 2 | Other pay type 1 hours for current pay period |
| 43 | BKPR_CURP_OPHRS_10 | NUMERIC | 8 | 2 | Other pay type 10 hours for current pay period |
| 44 | BKPR_CURP_OPHRS_11 | NUMERIC | 8 | 2 | Other pay type 11 hours for current pay period |
| 45 | BKPR_CURP_OPHRS_12 | NUMERIC | 8 | 2 | Other pay type 12 hours for current pay period |
| 46 | BKPR_CURP_OPHRS_2 | NUMERIC | 8 | 2 | Other pay type 2 hours for current pay period |
| 47 | BKPR_CURP_OPHRS_3 | NUMERIC | 8 | 2 | Other pay type 3 hours for current pay period |
| 48 | BKPR_CURP_OPHRS_4 | NUMERIC | 8 | 2 | Other pay type 4 hours for current pay period |
| 49 | BKPR_CURP_OPHRS_5 | NUMERIC | 8 | 2 | Other pay type 5 hours for current pay period |
| 50 | BKPR_CURP_OPHRS_6 | NUMERIC | 8 | 2 | Other pay type 6 hours for current pay period |
| 51 | BKPR_CURP_OPHRS_7 | NUMERIC | 8 | 2 | Other pay type 7 hours for current pay period |
| 52 | BKPR_CURP_OPHRS_8 | NUMERIC | 8 | 2 | Other pay type 8 hours for current pay period |
| 53 | BKPR_CURP_OPHRS_9 | NUMERIC | 8 | 2 | Other pay type 9 hours for current pay period |
| 54 | BKPR_CURP_OPNME_1 | STRING | 10 | — | Other pay type 1 name for current pay period |
| 55 | BKPR_CURP_OPNME_2 | STRING | 10 | — | Other pay type 2 name for current pay period |
| 56 | BKPR_CURP_OPNME_3 | STRING | 10 | — | Other pay type 3 name for current pay period |
| 57 | BKPR_CURP_OPNME_4 | STRING | 10 | — | Other pay type 4 name for current pay period |
| 58 | BKPR_CURP_OPNME_5 | STRING | 10 | — | Other pay type 5 name for current pay period |
| 59 | BKPR_CURP_OPRTE_1 | NUMERIC | 8 | 4 | Other pay type 1 pay rate for current pay period |
| 60 | BKPR_CURP_OPRTE_10 | NUMERIC | 8 | 4 | Other pay type 10 pay rate for current pay period |
| 61 | BKPR_CURP_OPRTE_11 | NUMERIC | 8 | 4 | Other pay type 11 pay rate for current pay period |
| 62 | BKPR_CURP_OPRTE_12 | NUMERIC | 8 | 4 | Other pay type 12 pay rate for current pay period |
| 63 | BKPR_CURP_OPRTE_2 | NUMERIC | 8 | 4 | Other pay type 2 pay rate for current pay period |
| 64 | BKPR_CURP_OPRTE_3 | NUMERIC | 8 | 4 | Other pay type 3 pay rate for current pay period |
| 65 | BKPR_CURP_OPRTE_4 | NUMERIC | 8 | 4 | Other pay type 4 pay rate for current pay period |
| 66 | BKPR_CURP_OPRTE_5 | NUMERIC | 8 | 4 | Other pay type 5 pay rate for current pay period |
| 67 | BKPR_CURP_OPRTE_6 | NUMERIC | 8 | 4 | Other pay type 6 pay rate for current pay period |
| 68 | BKPR_CURP_OPRTE_7 | NUMERIC | 8 | 4 | Other pay type 7 pay rate for current pay period |
| 69 | BKPR_CURP_OPRTE_8 | NUMERIC | 8 | 4 | Other pay type 8 pay rate for current pay period |
| 70 | BKPR_CURP_OPRTE_9 | NUMERIC | 8 | 4 | Other pay type 9 pay rate for current pay period |
| 71 | BKPR_CURP_PRDTE | DATE | 4 | — | Payroll period date |
| 72 | BKPR_CURP_RPAMT | NUMERIC | 8 | 2 | Regular pay amount |
| 73 | BKPR_CURP_RPHRS | NUMERIC | 8 | 2 | Regular pay hours |
| 74 | BKPR_CURP_RPRTE | NUMERIC | 8 | 4 | Regular pay rate |
| 75 | BKPR_CURP_SDIWH | NUMERIC | 8 | 2 | SDI (state disability) withheld |
| 76 | BKPR_CURP_SITWH | NUMERIC | 8 | 2 | SIT (state income tax) withheld |
| 77 | BKPR_CURP_SPAMT | NUMERIC | 8 | 2 | Special pay amount |
| 78 | BKPR_CURP_SPHRS | NUMERIC | 8 | 2 | Special pay hours |
| 79 | BKPR_CURP_SPRTE | NUMERIC | 8 | 4 | Special pay rate |
| 80 | BKPR_CURP_SUTEX | NUMERIC | 8 | 2 | SUTA (state unemployment) tax expense |
| 81 | BKPR_CURP_TOTHR | NUMERIC | 8 | 2 | Total hours for this pay period |
| 82 | BKPR_CURP_TOTPY | NUMERIC | 8 | 2 | Total gross pay for this pay period |
| 83 | BKPR_CURP_UOD_1 | NUMERIC | 8 | 2 | User other deduction 1 amount for current pay period |
| 84 | BKPR_CURP_UOD_10 | NUMERIC | 8 | 2 | User other deduction 10 amount for current pay period |
| 85 | BKPR_CURP_UOD_11 | NUMERIC | 8 | 2 | User other deduction 11 amount for current pay period |
| 86 | BKPR_CURP_UOD_12 | NUMERIC | 8 | 2 | User other deduction 12 amount for current pay period |
| 87 | BKPR_CURP_UOD_13 | NUMERIC | 8 | 2 | User other deduction 13 amount for current pay period |
| 88 | BKPR_CURP_UOD_14 | NUMERIC | 8 | 2 | User other deduction 14 amount for current pay period |
| 89 | BKPR_CURP_UOD_15 | NUMERIC | 8 | 2 | User other deduction 15 amount for current pay period |
| 90 | BKPR_CURP_UOD_16 | NUMERIC | 8 | 2 | User other deduction 16 amount for current pay period |
| 91 | BKPR_CURP_UOD_17 | NUMERIC | 8 | 2 | User other deduction 17 amount for current pay period |
| 92 | BKPR_CURP_UOD_18 | NUMERIC | 8 | 2 | User other deduction 18 amount for current pay period |
| 93 | BKPR_CURP_UOD_19 | NUMERIC | 8 | 2 | User other deduction 19 amount for current pay period |
| 94 | BKPR_CURP_UOD_2 | NUMERIC | 8 | 2 | User other deduction 2 amount for current pay period |
| 95 | BKPR_CURP_UOD_20 | NUMERIC | 8 | 2 | User other deduction 20 amount for current pay period |
| 96 | BKPR_CURP_UOD_3 | NUMERIC | 8 | 2 | User other deduction 3 amount for current pay period |
| 97 | BKPR_CURP_UOD_4 | NUMERIC | 8 | 2 | User other deduction 4 amount for current pay period |
| 98 | BKPR_CURP_UOD_5 | NUMERIC | 8 | 2 | User other deduction 5 amount for current pay period |
| 99 | BKPR_CURP_UOD_6 | NUMERIC | 8 | 2 | User other deduction 6 amount for current pay period |
| 100 | BKPR_CURP_UOD_7 | NUMERIC | 8 | 2 | User other deduction 7 amount for current pay period |
| 101 | BKPR_CURP_UOD_8 | NUMERIC | 8 | 2 | User other deduction 8 amount for current pay period |
| 102 | BKPR_CURP_UOD_9 | NUMERIC | 8 | 2 | User other deduction 9 amount for current pay period |
| 103 | BKPR_CURP_UODEC_1 | NUMERIC | 8 | 2 | User other deduction 1 employee contribution for current pay period |
| 104 | BKPR_CURP_UODEC_10 | NUMERIC | 8 | 2 | User other deduction 10 employee contribution for current pay period |
| 105 | BKPR_CURP_UODEC_11 | NUMERIC | 8 | 2 | User other deduction 11 employee contribution for current pay period |
| 106 | BKPR_CURP_UODEC_12 | NUMERIC | 8 | 2 | User other deduction 12 employee contribution for current pay period |
| 107 | BKPR_CURP_UODEC_13 | NUMERIC | 8 | 2 | User other deduction 13 employee contribution for current pay period |
| 108 | BKPR_CURP_UODEC_14 | NUMERIC | 8 | 2 | User other deduction 14 employee contribution for current pay period |
| 109 | BKPR_CURP_UODEC_15 | NUMERIC | 8 | 2 | User other deduction 15 employee contribution for current pay period |
| 110 | BKPR_CURP_UODEC_16 | NUMERIC | 8 | 2 | User other deduction 16 employee contribution for current pay period |
| 111 | BKPR_CURP_UODEC_17 | NUMERIC | 8 | 2 | User other deduction 17 employee contribution for current pay period |
| 112 | BKPR_CURP_UODEC_18 | NUMERIC | 8 | 2 | User other deduction 18 employee contribution for current pay period |
| 113 | BKPR_CURP_UODEC_19 | NUMERIC | 8 | 2 | User other deduction 19 employee contribution for current pay period |
| 114 | BKPR_CURP_UODEC_2 | NUMERIC | 8 | 2 | User other deduction 2 employee contribution for current pay period |
| 115 | BKPR_CURP_UODEC_20 | NUMERIC | 8 | 2 | User other deduction 20 employee contribution for current pay period |
| 116 | BKPR_CURP_UODEC_3 | NUMERIC | 8 | 2 | User other deduction 3 employee contribution for current pay period |
| 117 | BKPR_CURP_UODEC_4 | NUMERIC | 8 | 2 | User other deduction 4 employee contribution for current pay period |
| 118 | BKPR_CURP_UODEC_5 | NUMERIC | 8 | 2 | User other deduction 5 employee contribution for current pay period |
| 119 | BKPR_CURP_UODEC_6 | NUMERIC | 8 | 2 | User other deduction 6 employee contribution for current pay period |
| 120 | BKPR_CURP_UODEC_7 | NUMERIC | 8 | 2 | User other deduction 7 employee contribution for current pay period |
| 121 | BKPR_CURP_UODEC_8 | NUMERIC | 8 | 2 | User other deduction 8 employee contribution for current pay period |
| 122 | BKPR_CURP_UODEC_9 | NUMERIC | 8 | 2 | User other deduction 9 employee contribution for current pay period |
| 123 | BKPR_CURP_VPAMT | NUMERIC | 8 | 2 | Vacation pay amount |
| 124 | BKPR_CURP_VPHRS | NUMERIC | 8 | 2 | Vacation pay hours |
| 125 | BKPR_CURP_VPRTE | NUMERIC | 8 | 4 | Vacation pay rate |
| 126 | BKPR_CURP_WCEXP | NUMERIC | 8 | 2 | Workers compensation expense |
| 127 | BKPR_CURP_WCWH | NUMERIC | 8 | 2 | Workers compensation withheld |

## BKPRFTAX
**PAYROLL TAX TABLES**

Fields: 46

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKPR_TAX_ALLOW | NUMERIC | 8 | 2 | Withholding allowance amount per exemption |
| 2 | BKPR_TAX_AMT_1 | NUMERIC | 8 | 2 | Base tax amount for bracket 1 |
| 3 | BKPR_TAX_AMT_10 | NUMERIC | 8 | 2 | Base tax amount for bracket 10 |
| 4 | BKPR_TAX_AMT_11 | NUMERIC | 8 | 2 | Base tax amount for bracket 11 |
| 5 | BKPR_TAX_AMT_2 | NUMERIC | 8 | 2 | Base tax amount for bracket 2 |
| 6 | BKPR_TAX_AMT_3 | NUMERIC | 8 | 2 | Base tax amount for bracket 3 |
| 7 | BKPR_TAX_AMT_4 | NUMERIC | 8 | 2 | Base tax amount for bracket 4 |
| 8 | BKPR_TAX_AMT_5 | NUMERIC | 8 | 2 | Base tax amount for bracket 5 |
| 9 | BKPR_TAX_AMT_6 | NUMERIC | 8 | 2 | Base tax amount for bracket 6 |
| 10 | BKPR_TAX_AMT_7 | NUMERIC | 8 | 2 | Base tax amount for bracket 7 |
| 11 | BKPR_TAX_AMT_8 | NUMERIC | 8 | 2 | Base tax amount for bracket 8 |
| 12 | BKPR_TAX_AMT_9 | NUMERIC | 8 | 2 | Base tax amount for bracket 9 |
| 13 | BKPR_TAX_CODE | STRING | 3 | — | Tax table code (e.g. S=Single, M=Married) |
| 14 | BKPR_TAX_DESC | STRING | 20 | — | Tax table description |
| 15 | BKPR_TAX_PERC_1 | NUMERIC | 8 | 2 | Marginal tax rate for bracket 1 (%) |
| 16 | BKPR_TAX_PERC_10 | NUMERIC | 8 | 2 | Marginal tax rate for bracket 10 (%) |
| 17 | BKPR_TAX_PERC_11 | NUMERIC | 8 | 2 | Marginal tax rate for bracket 11 (%) |
| 18 | BKPR_TAX_PERC_2 | NUMERIC | 8 | 2 | Marginal tax rate for bracket 2 (%) |
| 19 | BKPR_TAX_PERC_3 | NUMERIC | 8 | 2 | Marginal tax rate for bracket 3 (%) |
| 20 | BKPR_TAX_PERC_4 | NUMERIC | 8 | 2 | Marginal tax rate for bracket 4 (%) |
| 21 | BKPR_TAX_PERC_5 | NUMERIC | 8 | 2 | Marginal tax rate for bracket 5 (%) |
| 22 | BKPR_TAX_PERC_6 | NUMERIC | 8 | 2 | Marginal tax rate for bracket 6 (%) |
| 23 | BKPR_TAX_PERC_7 | NUMERIC | 8 | 2 | Marginal tax rate for bracket 7 (%) |
| 24 | BKPR_TAX_PERC_8 | NUMERIC | 8 | 2 | Marginal tax rate for bracket 8 (%) |
| 25 | BKPR_TAX_PERC_9 | NUMERIC | 8 | 2 | Marginal tax rate for bracket 9 (%) |
| 26 | BKPR_TAX_START_1 | NUMERIC | 8 | — | Income start threshold for tax bracket 1 |
| 27 | BKPR_TAX_START_10 | NUMERIC | 8 | — | Income start threshold for tax bracket 10 |
| 28 | BKPR_TAX_START_11 | NUMERIC | 8 | — | Income start threshold for tax bracket 11 |
| 29 | BKPR_TAX_START_2 | NUMERIC | 8 | — | Income start threshold for tax bracket 2 |
| 30 | BKPR_TAX_START_3 | NUMERIC | 8 | — | Income start threshold for tax bracket 3 |
| 31 | BKPR_TAX_START_4 | NUMERIC | 8 | — | Income start threshold for tax bracket 4 |
| 32 | BKPR_TAX_START_5 | NUMERIC | 8 | — | Income start threshold for tax bracket 5 |
| 33 | BKPR_TAX_START_6 | NUMERIC | 8 | — | Income start threshold for tax bracket 6 |
| 34 | BKPR_TAX_START_7 | NUMERIC | 8 | — | Income start threshold for tax bracket 7 |
| 35 | BKPR_TAX_START_8 | NUMERIC | 8 | — | Income start threshold for tax bracket 8 |
| 36 | BKPR_TAX_START_9 | NUMERIC | 8 | — | Income start threshold for tax bracket 9 |
| 37 | BKPR_TAX_THRU_1 | NUMERIC | 8 | — | Income end threshold for tax bracket 1 |
| 38 | BKPR_TAX_THRU_10 | NUMERIC | 8 | — | Income end threshold for tax bracket 10 |
| 39 | BKPR_TAX_THRU_2 | NUMERIC | 8 | — | Income end threshold for tax bracket 2 |
| 40 | BKPR_TAX_THRU_3 | NUMERIC | 8 | — | Income end threshold for tax bracket 3 |
| 41 | BKPR_TAX_THRU_4 | NUMERIC | 8 | — | Income end threshold for tax bracket 4 |
| 42 | BKPR_TAX_THRU_5 | NUMERIC | 8 | — | Income end threshold for tax bracket 5 |
| 43 | BKPR_TAX_THRU_6 | NUMERIC | 8 | — | Income end threshold for tax bracket 6 |
| 44 | BKPR_TAX_THRU_7 | NUMERIC | 8 | — | Income end threshold for tax bracket 7 |
| 45 | BKPR_TAX_THRU_8 | NUMERIC | 8 | — | Income end threshold for tax bracket 8 |
| 46 | BKPR_TAX_THRU_9 | NUMERIC | 8 | — | Income end threshold for tax bracket 9 |

## BKPRGLFL
**PAYROLL DIVISION MASTER**

Fields: 664

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKPR_GL_DEPT | STRING | 4 | — | Default payroll GL department |
| 2 | BKPR_GL_DPTNME | STRING | 20 | — | Default payroll GL department name |
| 3 | BKPR_GL_EXPACT_1 | STRING | 10 | — | Payroll expense GL account 1 |
| 4 | BKPR_GL_EXPACT_10 | STRING | 10 | — | Payroll expense GL account 10 |
| 5 | BKPR_GL_EXPACT_11 | STRING | 10 | — | Payroll expense GL account 11 |
| 6 | BKPR_GL_EXPACT_12 | STRING | 10 | — | Payroll expense GL account 12 |
| 7 | BKPR_GL_EXPACT_13 | STRING | 10 | — | Payroll expense GL account 13 |
| 8 | BKPR_GL_EXPACT_14 | STRING | 10 | — | Payroll expense GL account 14 |
| 9 | BKPR_GL_EXPACT_15 | STRING | 10 | — | Payroll expense GL account 15 |
| 10 | BKPR_GL_EXPACT_2 | STRING | 10 | — | Payroll expense GL account 2 |
| 11 | BKPR_GL_EXPACT_3 | STRING | 10 | — | Payroll expense GL account 3 |
| 12 | BKPR_GL_EXPACT_4 | STRING | 10 | — | Payroll expense GL account 4 |
| 13 | BKPR_GL_EXPACT_5 | STRING | 10 | — | Payroll expense GL account 5 |
| 14 | BKPR_GL_EXPACT_6 | STRING | 10 | — | Payroll expense GL account 6 |
| 15 | BKPR_GL_EXPACT_7 | STRING | 10 | — | Payroll expense GL account 7 |
| 16 | BKPR_GL_EXPACT_8 | STRING | 10 | — | Payroll expense GL account 8 |
| 17 | BKPR_GL_EXPACT_9 | STRING | 10 | — | Payroll expense GL account 9 |
| 18 | BKPR_GL_EXPDPT_1 | STRING | 4 | — | Payroll expense GL department 1 |
| 19 | BKPR_GL_EXPDPT_10 | STRING | 4 | — | Payroll expense GL department 10 |
| 20 | BKPR_GL_EXPDPT_11 | STRING | 4 | — | Payroll expense GL department 11 |
| 21 | BKPR_GL_EXPDPT_12 | STRING | 4 | — | Payroll expense GL department 12 |
| 22 | BKPR_GL_EXPDPT_13 | STRING | 4 | — | Payroll expense GL department 13 |
| 23 | BKPR_GL_EXPDPT_14 | STRING | 4 | — | Payroll expense GL department 14 |
| 24 | BKPR_GL_EXPDPT_15 | STRING | 4 | — | Payroll expense GL department 15 |
| 25 | BKPR_GL_EXPDPT_2 | STRING | 4 | — | Payroll expense GL department 2 |
| 26 | BKPR_GL_EXPDPT_3 | STRING | 4 | — | Payroll expense GL department 3 |
| 27 | BKPR_GL_EXPDPT_4 | STRING | 4 | — | Payroll expense GL department 4 |
| 28 | BKPR_GL_EXPDPT_5 | STRING | 4 | — | Payroll expense GL department 5 |
| 29 | BKPR_GL_EXPDPT_6 | STRING | 4 | — | Payroll expense GL department 6 |
| 30 | BKPR_GL_EXPDPT_7 | STRING | 4 | — | Payroll expense GL department 7 |
| 31 | BKPR_GL_EXPDPT_8 | STRING | 4 | — | Payroll expense GL department 8 |
| 32 | BKPR_GL_EXPDPT_9 | STRING | 4 | — | Payroll expense GL department 9 |
| 33 | BKPR_GL_EXTRA | STRING | 200 | — | Reserved extra field |
| 34 | BKPR_GL_FICACCT_1 | STRING | 10 | — | FICA liability GL account 1 |
| 35 | BKPR_GL_FICACCT_2 | STRING | 10 | — | FICA liability GL account 2 |
| 36 | BKPR_GL_FICAEMP | NUMERIC | 8 | 4 | Employee FICA rate (SS 6.2%) |
| 37 | BKPR_GL_FICAEPL | NUMERIC | 8 | 4 | Employee Medicare rate (1.45%) |
| 38 | BKPR_GL_FICAEXD_1 | STRING | 4 | — | FICA expense GL department 1 |
| 39 | BKPR_GL_FICAEXD_2 | STRING | 4 | — | FICA expense GL department 2 |
| 40 | BKPR_GL_FICAEXP_1 | STRING | 10 | — | FICA expense GL account 1 |
| 41 | BKPR_GL_FICAEXP_2 | STRING | 10 | — | FICA expense GL account 2 |
| 42 | BKPR_GL_FICALMT | NUMERIC | 8 | — | Social Security wage base limit |
| 43 | BKPR_GL_FICAMEE | NUMERIC | 8 | 4 | Employer Medicare rate (1.45%) |
| 44 | BKPR_GL_FICAMER | NUMERIC | 8 | 4 | Employer FICA rate (SS 6.2%) |
| 45 | BKPR_GL_FICAMLM | NUMERIC | 8 | — | Medicare additional wage threshold |
| 46 | BKPR_GL_FICDPT_1 | STRING | 4 | — | FICA liability GL department 1 |
| 47 | BKPR_GL_FICDPT_2 | STRING | 4 | — | FICA liability GL department 2 |
| 48 | BKPR_GL_FITACCT | STRING | 10 | — | Federal income tax (FIT) liability GL account |
| 49 | BKPR_GL_FITDPT | STRING | 4 | — | FIT liability GL department |
| 50 | BKPR_GL_FUTACCT | STRING | 10 | — | FUTA liability GL account |
| 51 | BKPR_GL_FUTACRD | NUMERIC | 8 | 2 | FUTA credit rate |
| 52 | BKPR_GL_FUTAEXD | STRING | 4 | — | FUTA expense GL department |
| 53 | BKPR_GL_FUTAEXP | STRING | 10 | — | FUTA expense GL account |
| 54 | BKPR_GL_FUTALMT | NUMERIC | 8 | — | FUTA wage base limit |
| 55 | BKPR_GL_FUTART | NUMERIC | 8 | 4 | FUTA tax rate |
| 56 | BKPR_GL_FUTDPT | STRING | 4 | — | FUTA liability GL department |
| 57 | BKPR_GL_MDACCT | STRING | 10 | — | Medical deduction GL account |
| 58 | BKPR_GL_MDDPT | STRING | 4 | — | Medical deduction GL department |
| 59 | BKPR_GL_ODACCT | STRING | 10 | — | Other deduction GL account |
| 60 | BKPR_GL_ODDPT | STRING | 4 | — | Other deduction GL department |
| 61 | BKPR_GL_OPAYNME_1 | STRING | 10 | — | Other pay type 1 name label |
| 62 | BKPR_GL_OPAYNME_2 | STRING | 10 | — | Other pay type 2 name label |
| 63 | BKPR_GL_OPAYNME_3 | STRING | 10 | — | Other pay type 3 name label |
| 64 | BKPR_GL_OPAYNME_4 | STRING | 10 | — | Other pay type 4 name label |
| 65 | BKPR_GL_OPAYNME_5 | STRING | 10 | — | Other pay type 5 name label |
| 66 | BKPR_GL_PAYPER | STRING | 1 | — | Pay period type (W=Weekly, B=Bi-weekly, S=Semi-monthly, M=Monthly) |
| 67 | BKPR_GL_SDI_LMT | NUMERIC | 8 | — | SDI wage base limit |
| 68 | BKPR_GL_SDI_RTE | NUMERIC | 8 | 4 | SDI employee rate |
| 69 | BKPR_GL_SDIACCT | STRING | 10 | — | SDI liability GL account |
| 70 | BKPR_GL_SDIDPT | STRING | 4 | — | SDI liability GL department |
| 71 | BKPR_GL_SDIEXP | STRING | 10 | — | SDI expense GL account |
| 72 | BKPR_GL_SDIEXPD | STRING | 4 | — | SDI expense GL department |
| 73 | BKPR_GL_SITACCT | STRING | 10 | — | SIT (state income tax) liability GL account |
| 74 | BKPR_GL_SITDPT | STRING | 4 | — | SIT liability GL department |
| 75 | BKPR_GL_SRTE | NUMERIC | 8 | 4 | Standard pay rate |
| 76 | BKPR_GL_STCODE | STRING | 2 | — | State code for tax withholding |
| 77 | BKPR_GL_SUTACCT | STRING | 10 | — | SUTA liability GL account |
| 78 | BKPR_GL_SUTAEXD | STRING | 4 | — | SUTA expense GL department |
| 79 | BKPR_GL_SUTAEXP | STRING | 10 | — | SUTA expense GL account |
| 80 | BKPR_GL_SUTALMT | NUMERIC | 8 | — | SUTA wage base limit |
| 81 | BKPR_GL_SUTART | NUMERIC | 8 | 4 | SUTA tax rate |
| 82 | BKPR_GL_SUTDPT | STRING | 4 | — | SUTA liability GL department |
| 83 | BKPR_GL_TAXOUT1_1 | NUMERIC | 8 | 2 | Tax table 1 output amount slot 1 |
| 84 | BKPR_GL_TAXOUT1_10 | NUMERIC | 8 | 2 | Tax table 1 output amount slot 10 |
| 85 | BKPR_GL_TAXOUT1_11 | NUMERIC | 8 | 2 | Tax table 1 output amount slot 11 |
| 86 | BKPR_GL_TAXOUT1_12 | NUMERIC | 8 | 2 | Tax table 1 output amount slot 12 |
| 87 | BKPR_GL_TAXOUT1_13 | NUMERIC | 8 | 2 | Tax table 1 output amount slot 13 |
| 88 | BKPR_GL_TAXOUT1_14 | NUMERIC | 8 | 2 | Tax table 1 output amount slot 14 |
| 89 | BKPR_GL_TAXOUT1_15 | NUMERIC | 8 | 2 | Tax table 1 output amount slot 15 |
| 90 | BKPR_GL_TAXOUT1_16 | NUMERIC | 8 | 2 | Tax table 1 output amount slot 16 |
| 91 | BKPR_GL_TAXOUT1_2 | NUMERIC | 8 | 2 | Tax table 1 output amount slot 2 |
| 92 | BKPR_GL_TAXOUT1_3 | NUMERIC | 8 | 2 | Tax table 1 output amount slot 3 |
| 93 | BKPR_GL_TAXOUT1_4 | NUMERIC | 8 | 2 | Tax table 1 output amount slot 4 |
| 94 | BKPR_GL_TAXOUT1_5 | NUMERIC | 8 | 2 | Tax table 1 output amount slot 5 |
| 95 | BKPR_GL_TAXOUT1_6 | NUMERIC | 8 | 2 | Tax table 1 output amount slot 6 |
| 96 | BKPR_GL_TAXOUT1_7 | NUMERIC | 8 | 2 | Tax table 1 output amount slot 7 |
| 97 | BKPR_GL_TAXOUT1_8 | NUMERIC | 8 | 2 | Tax table 1 output amount slot 8 |
| 98 | BKPR_GL_TAXOUT1_9 | NUMERIC | 8 | 2 | Tax table 1 output amount slot 9 |
| 99 | BKPR_GL_TAXOUTS_1 | NUMERIC | 8 | 2 | Tax table summary output slot 1 |
| 100 | BKPR_GL_TAXOUTS_10 | NUMERIC | 8 | 2 | Tax table summary output slot 10 |
| 101 | BKPR_GL_TAXOUTS_11 | NUMERIC | 8 | 2 | Tax table summary output slot 11 |
| 102 | BKPR_GL_TAXOUTS_12 | NUMERIC | 8 | 2 | Tax table summary output slot 12 |
| 103 | BKPR_GL_TAXOUTS_13 | NUMERIC | 8 | 2 | Tax table summary output slot 13 |
| 104 | BKPR_GL_TAXOUTS_14 | NUMERIC | 8 | 2 | Tax table summary output slot 14 |
| 105 | BKPR_GL_TAXOUTS_15 | NUMERIC | 8 | 2 | Tax table summary output slot 15 |
| 106 | BKPR_GL_TAXOUTS_16 | NUMERIC | 8 | 2 | Tax table summary output slot 16 |
| 107 | BKPR_GL_TAXOUTS_17 | NUMERIC | 8 | 2 | Tax table summary output slot 17 |
| 108 | BKPR_GL_TAXOUTS_18 | NUMERIC | 8 | 2 | Tax table summary output slot 18 |
| 109 | BKPR_GL_TAXOUTS_19 | NUMERIC | 8 | 2 | Tax table summary output slot 19 |
| 110 | BKPR_GL_TAXOUTS_2 | NUMERIC | 8 | 2 | Tax table summary output slot 2 |
| 111 | BKPR_GL_TAXOUTS_20 | NUMERIC | 8 | 2 | Tax table summary output slot 20 |
| 112 | BKPR_GL_TAXOUTS_21 | NUMERIC | 8 | 2 | Tax table summary output slot 21 |
| 113 | BKPR_GL_TAXOUTS_22 | NUMERIC | 8 | 2 | Tax table summary output slot 22 |
| 114 | BKPR_GL_TAXOUTS_23 | NUMERIC | 8 | 2 | Tax table summary output slot 23 |
| 115 | BKPR_GL_TAXOUTS_24 | NUMERIC | 8 | 2 | Tax table summary output slot 24 |
| 116 | BKPR_GL_TAXOUTS_25 | NUMERIC | 8 | 2 | Tax table summary output slot 25 |
| 117 | BKPR_GL_TAXOUTS_26 | NUMERIC | 8 | 2 | Tax table summary output slot 26 |
| 118 | BKPR_GL_TAXOUTS_27 | NUMERIC | 8 | 2 | Tax table summary output slot 27 |
| 119 | BKPR_GL_TAXOUTS_28 | NUMERIC | 8 | 2 | Tax table summary output slot 28 |
| 120 | BKPR_GL_TAXOUTS_29 | NUMERIC | 8 | 2 | Tax table summary output slot 29 |
| 121 | BKPR_GL_TAXOUTS_3 | NUMERIC | 8 | 2 | Tax table summary output slot 3 |
| 122 | BKPR_GL_TAXOUTS_30 | NUMERIC | 8 | 2 | Tax table summary output slot 30 |
| 123 | BKPR_GL_TAXOUTS_4 | NUMERIC | 8 | 2 | Tax table summary output slot 4 |
| 124 | BKPR_GL_TAXOUTS_5 | NUMERIC | 8 | 2 | Tax table summary output slot 5 |
| 125 | BKPR_GL_TAXOUTS_6 | NUMERIC | 8 | 2 | Tax table summary output slot 6 |
| 126 | BKPR_GL_TAXOUTS_7 | NUMERIC | 8 | 2 | Tax table summary output slot 7 |
| 127 | BKPR_GL_TAXOUTS_8 | NUMERIC | 8 | 2 | Tax table summary output slot 8 |
| 128 | BKPR_GL_TAXOUTS_9 | NUMERIC | 8 | 2 | Tax table summary output slot 9 |
| 129 | BKPR_GL_TAXVEND_1 | STRING | 10 | — | Tax vendor code slot 1 |
| 130 | BKPR_GL_TAXVEND_10 | STRING | 10 | — | Tax vendor code slot 10 |
| 131 | BKPR_GL_TAXVEND_11 | STRING | 10 | — | Tax vendor code slot 11 |
| 132 | BKPR_GL_TAXVEND_12 | STRING | 10 | — | Tax vendor code slot 12 |
| 133 | BKPR_GL_TAXVEND_13 | STRING | 10 | — | Tax vendor code slot 13 |
| 134 | BKPR_GL_TAXVEND_14 | STRING | 10 | — | Tax vendor code slot 14 |
| 135 | BKPR_GL_TAXVEND_15 | STRING | 10 | — | Tax vendor code slot 15 |
| 136 | BKPR_GL_TAXVEND_16 | STRING | 10 | — | Tax vendor code slot 16 |
| 137 | BKPR_GL_TAXVEND_17 | STRING | 10 | — | Tax vendor code slot 17 |
| 138 | BKPR_GL_TAXVEND_18 | STRING | 10 | — | Tax vendor code slot 18 |
| 139 | BKPR_GL_TAXVEND_19 | STRING | 10 | — | Tax vendor code slot 19 |
| 140 | BKPR_GL_TAXVEND_2 | STRING | 10 | — | Tax vendor code slot 2 |
| 141 | BKPR_GL_TAXVEND_20 | STRING | 10 | — | Tax vendor code slot 20 |
| 142 | BKPR_GL_TAXVEND_21 | STRING | 10 | — | Tax vendor code slot 21 |
| 143 | BKPR_GL_TAXVEND_22 | STRING | 10 | — | Tax vendor code slot 22 |
| 144 | BKPR_GL_TAXVEND_23 | STRING | 10 | — | Tax vendor code slot 23 |
| 145 | BKPR_GL_TAXVEND_24 | STRING | 10 | — | Tax vendor code slot 24 |
| 146 | BKPR_GL_TAXVEND_25 | STRING | 10 | — | Tax vendor code slot 25 |
| 147 | BKPR_GL_TAXVEND_26 | STRING | 10 | — | Tax vendor code slot 26 |
| 148 | BKPR_GL_TAXVEND_27 | STRING | 10 | — | Tax vendor code slot 27 |
| 149 | BKPR_GL_TAXVEND_28 | STRING | 10 | — | Tax vendor code slot 28 |
| 150 | BKPR_GL_TAXVEND_29 | STRING | 10 | — | Tax vendor code slot 29 |
| 151 | BKPR_GL_TAXVEND_3 | STRING | 10 | — | Tax vendor code slot 3 |
| 152 | BKPR_GL_TAXVEND_30 | STRING | 10 | — | Tax vendor code slot 30 |
| 153 | BKPR_GL_TAXVEND_4 | STRING | 10 | — | Tax vendor code slot 4 |
| 154 | BKPR_GL_TAXVEND_5 | STRING | 10 | — | Tax vendor code slot 5 |
| 155 | BKPR_GL_TAXVEND_6 | STRING | 10 | — | Tax vendor code slot 6 |
| 156 | BKPR_GL_TAXVEND_7 | STRING | 10 | — | Tax vendor code slot 7 |
| 157 | BKPR_GL_TAXVEND_8 | STRING | 10 | — | Tax vendor code slot 8 |
| 158 | BKPR_GL_TAXVEND_9 | STRING | 10 | — | Tax vendor code slot 9 |
| 159 | BKPR_GL_TAXVND1_1 | STRING | 10 | — | Tax table 1 vendor code slot 1 |
| 160 | BKPR_GL_TAXVND1_10 | STRING | 10 | — | Tax table 1 vendor code slot 10 |
| 161 | BKPR_GL_TAXVND1_11 | STRING | 10 | — | Tax table 1 vendor code slot 11 |
| 162 | BKPR_GL_TAXVND1_12 | STRING | 10 | — | Tax table 1 vendor code slot 12 |
| 163 | BKPR_GL_TAXVND1_13 | STRING | 10 | — | Tax table 1 vendor code slot 13 |
| 164 | BKPR_GL_TAXVND1_14 | STRING | 10 | — | Tax table 1 vendor code slot 14 |
| 165 | BKPR_GL_TAXVND1_15 | STRING | 10 | — | Tax table 1 vendor code slot 15 |
| 166 | BKPR_GL_TAXVND1_16 | STRING | 10 | — | Tax table 1 vendor code slot 16 |
| 167 | BKPR_GL_TAXVND1_2 | STRING | 10 | — | Tax table 1 vendor code slot 2 |
| 168 | BKPR_GL_TAXVND1_3 | STRING | 10 | — | Tax table 1 vendor code slot 3 |
| 169 | BKPR_GL_TAXVND1_4 | STRING | 10 | — | Tax table 1 vendor code slot 4 |
| 170 | BKPR_GL_TAXVND1_5 | STRING | 10 | — | Tax table 1 vendor code slot 5 |
| 171 | BKPR_GL_TAXVND1_6 | STRING | 10 | — | Tax table 1 vendor code slot 6 |
| 172 | BKPR_GL_TAXVND1_7 | STRING | 10 | — | Tax table 1 vendor code slot 7 |
| 173 | BKPR_GL_TAXVND1_8 | STRING | 10 | — | Tax table 1 vendor code slot 8 |
| 174 | BKPR_GL_TAXVND1_9 | STRING | 10 | — | Tax table 1 vendor code slot 9 |
| 175 | BKPR_GL_UODACT1_1 | STRING | 10 | — | User OD (type 1) liability GL account 1 |
| 176 | BKPR_GL_UODACT1_2 | STRING | 10 | — | User OD (type 1) liability GL account 2 |
| 177 | BKPR_GL_UODACT1_3 | STRING | 10 | — | User OD (type 1) liability GL account 3 |
| 178 | BKPR_GL_UODACT1_4 | STRING | 10 | — | User OD (type 1) liability GL account 4 |
| 179 | BKPR_GL_UODACT1_5 | STRING | 10 | — | User OD (type 1) liability GL account 5 |
| 180 | BKPR_GL_UODACT1_6 | STRING | 10 | — | User OD (type 1) liability GL account 6 |
| 181 | BKPR_GL_UODACT_1 | STRING | 10 | — | User OD liability GL account 1 |
| 182 | BKPR_GL_UODACT_10 | STRING | 10 | — | User OD liability GL account 10 |
| 183 | BKPR_GL_UODACT_11 | STRING | 10 | — | User OD liability GL account 11 |
| 184 | BKPR_GL_UODACT_12 | STRING | 10 | — | User OD liability GL account 12 |
| 185 | BKPR_GL_UODACT_13 | STRING | 10 | — | User OD liability GL account 13 |
| 186 | BKPR_GL_UODACT_14 | STRING | 10 | — | User OD liability GL account 14 |
| 187 | BKPR_GL_UODACT_15 | STRING | 10 | — | User OD liability GL account 15 |
| 188 | BKPR_GL_UODACT_16 | STRING | 10 | — | User OD liability GL account 16 |
| 189 | BKPR_GL_UODACT_17 | STRING | 10 | — | User OD liability GL account 17 |
| 190 | BKPR_GL_UODACT_18 | STRING | 10 | — | User OD liability GL account 18 |
| 191 | BKPR_GL_UODACT_19 | STRING | 10 | — | User OD liability GL account 19 |
| 192 | BKPR_GL_UODACT_2 | STRING | 10 | — | User OD liability GL account 2 |
| 193 | BKPR_GL_UODACT_20 | STRING | 10 | — | User OD liability GL account 20 |
| 194 | BKPR_GL_UODACT_3 | STRING | 10 | — | User OD liability GL account 3 |
| 195 | BKPR_GL_UODACT_4 | STRING | 10 | — | User OD liability GL account 4 |
| 196 | BKPR_GL_UODACT_5 | STRING | 10 | — | User OD liability GL account 5 |
| 197 | BKPR_GL_UODACT_6 | STRING | 10 | — | User OD liability GL account 6 |
| 198 | BKPR_GL_UODACT_7 | STRING | 10 | — | User OD liability GL account 7 |
| 199 | BKPR_GL_UODACT_8 | STRING | 10 | — | User OD liability GL account 8 |
| 200 | BKPR_GL_UODACT_9 | STRING | 10 | — | User OD liability GL account 9 |
| 201 | BKPR_GL_UODAMT1_1 | NUMERIC | 8 | 4 | User OD (type 1) allocation amount 1 |
| 202 | BKPR_GL_UODAMT1_2 | NUMERIC | 8 | 4 | User OD (type 1) allocation amount 2 |
| 203 | BKPR_GL_UODAMT1_3 | NUMERIC | 8 | 4 | User OD (type 1) allocation amount 3 |
| 204 | BKPR_GL_UODAMT1_4 | NUMERIC | 8 | 4 | User OD (type 1) allocation amount 4 |
| 205 | BKPR_GL_UODAMT1_5 | NUMERIC | 8 | 4 | User OD (type 1) allocation amount 5 |
| 206 | BKPR_GL_UODAMT1_6 | NUMERIC | 8 | 4 | User OD (type 1) allocation amount 6 |
| 207 | BKPR_GL_UODAMT_1 | NUMERIC | 8 | 4 | User OD allocation amount 1 |
| 208 | BKPR_GL_UODAMT_10 | NUMERIC | 8 | 4 | User OD allocation amount 10 |
| 209 | BKPR_GL_UODAMT_11 | NUMERIC | 8 | 4 | User OD allocation amount 11 |
| 210 | BKPR_GL_UODAMT_12 | NUMERIC | 8 | 4 | User OD allocation amount 12 |
| 211 | BKPR_GL_UODAMT_13 | NUMERIC | 8 | 4 | User OD allocation amount 13 |
| 212 | BKPR_GL_UODAMT_14 | NUMERIC | 8 | 4 | User OD allocation amount 14 |
| 213 | BKPR_GL_UODAMT_15 | NUMERIC | 8 | 4 | User OD allocation amount 15 |
| 214 | BKPR_GL_UODAMT_16 | NUMERIC | 8 | 4 | User OD allocation amount 16 |
| 215 | BKPR_GL_UODAMT_17 | NUMERIC | 8 | 4 | User OD allocation amount 17 |
| 216 | BKPR_GL_UODAMT_18 | NUMERIC | 8 | 4 | User OD allocation amount 18 |
| 217 | BKPR_GL_UODAMT_19 | NUMERIC | 8 | 4 | User OD allocation amount 19 |
| 218 | BKPR_GL_UODAMT_2 | NUMERIC | 8 | 4 | User OD allocation amount 2 |
| 219 | BKPR_GL_UODAMT_20 | NUMERIC | 8 | 4 | User OD allocation amount 20 |
| 220 | BKPR_GL_UODAMT_3 | NUMERIC | 8 | 4 | User OD allocation amount 3 |
| 221 | BKPR_GL_UODAMT_4 | NUMERIC | 8 | 4 | User OD allocation amount 4 |
| 222 | BKPR_GL_UODAMT_5 | NUMERIC | 8 | 4 | User OD allocation amount 5 |
| 223 | BKPR_GL_UODAMT_6 | NUMERIC | 8 | 4 | User OD allocation amount 6 |
| 224 | BKPR_GL_UODAMT_7 | NUMERIC | 8 | 4 | User OD allocation amount 7 |
| 225 | BKPR_GL_UODAMT_8 | NUMERIC | 8 | 4 | User OD allocation amount 8 |
| 226 | BKPR_GL_UODAMT_9 | NUMERIC | 8 | 4 | User OD allocation amount 9 |
| 227 | BKPR_GL_UODCALC_1 | STRING | 1 | — | User OD 1 calculation type flag |
| 228 | BKPR_GL_UODCALC_10 | STRING | 1 | — | User OD 10 calculation type flag |
| 229 | BKPR_GL_UODCALC_11 | STRING | 1 | — | User OD 11 calculation type flag |
| 230 | BKPR_GL_UODCALC_12 | STRING | 1 | — | User OD 12 calculation type flag |
| 231 | BKPR_GL_UODCALC_13 | STRING | 1 | — | User OD 13 calculation type flag |
| 232 | BKPR_GL_UODCALC_14 | STRING | 1 | — | User OD 14 calculation type flag |
| 233 | BKPR_GL_UODCALC_15 | STRING | 1 | — | User OD 15 calculation type flag |
| 234 | BKPR_GL_UODCALC_16 | STRING | 1 | — | User OD 16 calculation type flag |
| 235 | BKPR_GL_UODCALC_17 | STRING | 1 | — | User OD 17 calculation type flag |
| 236 | BKPR_GL_UODCALC_18 | STRING | 1 | — | User OD 18 calculation type flag |
| 237 | BKPR_GL_UODCALC_19 | STRING | 1 | — | User OD 19 calculation type flag |
| 238 | BKPR_GL_UODCALC_2 | STRING | 1 | — | User OD 2 calculation type flag |
| 239 | BKPR_GL_UODCALC_20 | STRING | 1 | — | User OD 20 calculation type flag |
| 240 | BKPR_GL_UODCALC_3 | STRING | 1 | — | User OD 3 calculation type flag |
| 241 | BKPR_GL_UODCALC_4 | STRING | 1 | — | User OD 4 calculation type flag |
| 242 | BKPR_GL_UODCALC_5 | STRING | 1 | — | User OD 5 calculation type flag |
| 243 | BKPR_GL_UODCALC_6 | STRING | 1 | — | User OD 6 calculation type flag |
| 244 | BKPR_GL_UODCALC_7 | STRING | 1 | — | User OD 7 calculation type flag |
| 245 | BKPR_GL_UODCALC_8 | STRING | 1 | — | User OD 8 calculation type flag |
| 246 | BKPR_GL_UODCALC_9 | STRING | 1 | — | User OD 9 calculation type flag |
| 247 | BKPR_GL_UODCLC1_1 | STRING | 1 | — | User OD (type 1) 1 calculation type flag |
| 248 | BKPR_GL_UODCLC1_2 | STRING | 1 | — | User OD (type 1) 2 calculation type flag |
| 249 | BKPR_GL_UODCLC1_3 | STRING | 1 | — | User OD (type 1) 3 calculation type flag |
| 250 | BKPR_GL_UODCLC1_4 | STRING | 1 | — | User OD (type 1) 4 calculation type flag |
| 251 | BKPR_GL_UODCLC1_5 | STRING | 1 | — | User OD (type 1) 5 calculation type flag |
| 252 | BKPR_GL_UODCLC1_6 | STRING | 1 | — | User OD (type 1) 6 calculation type flag |
| 253 | BKPR_GL_UODDPT1_1 | STRING | 4 | — | User OD (type 1) liability GL department 1 |
| 254 | BKPR_GL_UODDPT1_2 | STRING | 4 | — | User OD (type 1) liability GL department 2 |
| 255 | BKPR_GL_UODDPT1_3 | STRING | 4 | — | User OD (type 1) liability GL department 3 |
| 256 | BKPR_GL_UODDPT1_4 | STRING | 4 | — | User OD (type 1) liability GL department 4 |
| 257 | BKPR_GL_UODDPT1_5 | STRING | 4 | — | User OD (type 1) liability GL department 5 |
| 258 | BKPR_GL_UODDPT1_6 | STRING | 4 | — | User OD (type 1) liability GL department 6 |
| 259 | BKPR_GL_UODDPT_1 | STRING | 4 | — | User OD liability GL department 1 |
| 260 | BKPR_GL_UODDPT_10 | STRING | 4 | — | User OD liability GL department 10 |
| 261 | BKPR_GL_UODDPT_11 | STRING | 4 | — | User OD liability GL department 11 |
| 262 | BKPR_GL_UODDPT_12 | STRING | 4 | — | User OD liability GL department 12 |
| 263 | BKPR_GL_UODDPT_13 | STRING | 4 | — | User OD liability GL department 13 |
| 264 | BKPR_GL_UODDPT_14 | STRING | 4 | — | User OD liability GL department 14 |
| 265 | BKPR_GL_UODDPT_15 | STRING | 4 | — | User OD liability GL department 15 |
| 266 | BKPR_GL_UODDPT_16 | STRING | 4 | — | User OD liability GL department 16 |
| 267 | BKPR_GL_UODDPT_17 | STRING | 4 | — | User OD liability GL department 17 |
| 268 | BKPR_GL_UODDPT_18 | STRING | 4 | — | User OD liability GL department 18 |
| 269 | BKPR_GL_UODDPT_19 | STRING | 4 | — | User OD liability GL department 19 |
| 270 | BKPR_GL_UODDPT_2 | STRING | 4 | — | User OD liability GL department 2 |
| 271 | BKPR_GL_UODDPT_20 | STRING | 4 | — | User OD liability GL department 20 |
| 272 | BKPR_GL_UODDPT_3 | STRING | 4 | — | User OD liability GL department 3 |
| 273 | BKPR_GL_UODDPT_4 | STRING | 4 | — | User OD liability GL department 4 |
| 274 | BKPR_GL_UODDPT_5 | STRING | 4 | — | User OD liability GL department 5 |
| 275 | BKPR_GL_UODDPT_6 | STRING | 4 | — | User OD liability GL department 6 |
| 276 | BKPR_GL_UODDPT_7 | STRING | 4 | — | User OD liability GL department 7 |
| 277 | BKPR_GL_UODDPT_8 | STRING | 4 | — | User OD liability GL department 8 |
| 278 | BKPR_GL_UODDPT_9 | STRING | 4 | — | User OD liability GL department 9 |
| 279 | BKPR_GL_UODEACT_1 | STRING | 10 | — | User OD expense GL account 1 |
| 280 | BKPR_GL_UODEACT_10 | STRING | 10 | — | User OD expense GL account 10 |
| 281 | BKPR_GL_UODEACT_11 | STRING | 10 | — | User OD expense GL account 11 |
| 282 | BKPR_GL_UODEACT_12 | STRING | 10 | — | User OD expense GL account 12 |
| 283 | BKPR_GL_UODEACT_13 | STRING | 10 | — | User OD expense GL account 13 |
| 284 | BKPR_GL_UODEACT_14 | STRING | 10 | — | User OD expense GL account 14 |
| 285 | BKPR_GL_UODEACT_15 | STRING | 10 | — | User OD expense GL account 15 |
| 286 | BKPR_GL_UODEACT_16 | STRING | 10 | — | User OD expense GL account 16 |
| 287 | BKPR_GL_UODEACT_17 | STRING | 10 | — | User OD expense GL account 17 |
| 288 | BKPR_GL_UODEACT_18 | STRING | 10 | — | User OD expense GL account 18 |
| 289 | BKPR_GL_UODEACT_19 | STRING | 10 | — | User OD expense GL account 19 |
| 290 | BKPR_GL_UODEACT_2 | STRING | 10 | — | User OD expense GL account 2 |
| 291 | BKPR_GL_UODEACT_20 | STRING | 10 | — | User OD expense GL account 20 |
| 292 | BKPR_GL_UODEACT_3 | STRING | 10 | — | User OD expense GL account 3 |
| 293 | BKPR_GL_UODEACT_4 | STRING | 10 | — | User OD expense GL account 4 |
| 294 | BKPR_GL_UODEACT_5 | STRING | 10 | — | User OD expense GL account 5 |
| 295 | BKPR_GL_UODEACT_6 | STRING | 10 | — | User OD expense GL account 6 |
| 296 | BKPR_GL_UODEACT_7 | STRING | 10 | — | User OD expense GL account 7 |
| 297 | BKPR_GL_UODEACT_8 | STRING | 10 | — | User OD expense GL account 8 |
| 298 | BKPR_GL_UODEACT_9 | STRING | 10 | — | User OD expense GL account 9 |
| 299 | BKPR_GL_UODEAMT_1 | NUMERIC | 8 | 4 | User OD expense GL amount 1 |
| 300 | BKPR_GL_UODEAMT_10 | NUMERIC | 8 | 4 | User OD expense GL amount 10 |
| 301 | BKPR_GL_UODEAMT_11 | NUMERIC | 8 | 4 | User OD expense GL amount 11 |
| 302 | BKPR_GL_UODEAMT_12 | NUMERIC | 8 | 4 | User OD expense GL amount 12 |
| 303 | BKPR_GL_UODEAMT_13 | NUMERIC | 8 | 4 | User OD expense GL amount 13 |
| 304 | BKPR_GL_UODEAMT_14 | NUMERIC | 8 | 4 | User OD expense GL amount 14 |
| 305 | BKPR_GL_UODEAMT_15 | NUMERIC | 8 | 4 | User OD expense GL amount 15 |
| 306 | BKPR_GL_UODEAMT_16 | NUMERIC | 8 | 4 | User OD expense GL amount 16 |
| 307 | BKPR_GL_UODEAMT_17 | NUMERIC | 8 | 4 | User OD expense GL amount 17 |
| 308 | BKPR_GL_UODEAMT_18 | NUMERIC | 8 | 4 | User OD expense GL amount 18 |
| 309 | BKPR_GL_UODEAMT_19 | NUMERIC | 8 | 4 | User OD expense GL amount 19 |
| 310 | BKPR_GL_UODEAMT_2 | NUMERIC | 8 | 4 | User OD expense GL amount 2 |
| 311 | BKPR_GL_UODEAMT_20 | NUMERIC | 8 | 4 | User OD expense GL amount 20 |
| 312 | BKPR_GL_UODEAMT_3 | NUMERIC | 8 | 4 | User OD expense GL amount 3 |
| 313 | BKPR_GL_UODEAMT_4 | NUMERIC | 8 | 4 | User OD expense GL amount 4 |
| 314 | BKPR_GL_UODEAMT_5 | NUMERIC | 8 | 4 | User OD expense GL amount 5 |
| 315 | BKPR_GL_UODEAMT_6 | NUMERIC | 8 | 4 | User OD expense GL amount 6 |
| 316 | BKPR_GL_UODEAMT_7 | NUMERIC | 8 | 4 | User OD expense GL amount 7 |
| 317 | BKPR_GL_UODEAMT_8 | NUMERIC | 8 | 4 | User OD expense GL amount 8 |
| 318 | BKPR_GL_UODEAMT_9 | NUMERIC | 8 | 4 | User OD expense GL amount 9 |
| 319 | BKPR_GL_UODECLC_1 | STRING | 1 | — | User OD expense 1 calculation type flag |
| 320 | BKPR_GL_UODECLC_10 | STRING | 1 | — | User OD expense 10 calculation type flag |
| 321 | BKPR_GL_UODECLC_11 | STRING | 1 | — | User OD expense 11 calculation type flag |
| 322 | BKPR_GL_UODECLC_12 | STRING | 1 | — | User OD expense 12 calculation type flag |
| 323 | BKPR_GL_UODECLC_13 | STRING | 1 | — | User OD expense 13 calculation type flag |
| 324 | BKPR_GL_UODECLC_14 | STRING | 1 | — | User OD expense 14 calculation type flag |
| 325 | BKPR_GL_UODECLC_15 | STRING | 1 | — | User OD expense 15 calculation type flag |
| 326 | BKPR_GL_UODECLC_16 | STRING | 1 | — | User OD expense 16 calculation type flag |
| 327 | BKPR_GL_UODECLC_17 | STRING | 1 | — | User OD expense 17 calculation type flag |
| 328 | BKPR_GL_UODECLC_18 | STRING | 1 | — | User OD expense 18 calculation type flag |
| 329 | BKPR_GL_UODECLC_19 | STRING | 1 | — | User OD expense 19 calculation type flag |
| 330 | BKPR_GL_UODECLC_2 | STRING | 1 | — | User OD expense 2 calculation type flag |
| 331 | BKPR_GL_UODECLC_20 | STRING | 1 | — | User OD expense 20 calculation type flag |
| 332 | BKPR_GL_UODECLC_3 | STRING | 1 | — | User OD expense 3 calculation type flag |
| 333 | BKPR_GL_UODECLC_4 | STRING | 1 | — | User OD expense 4 calculation type flag |
| 334 | BKPR_GL_UODECLC_5 | STRING | 1 | — | User OD expense 5 calculation type flag |
| 335 | BKPR_GL_UODECLC_6 | STRING | 1 | — | User OD expense 6 calculation type flag |
| 336 | BKPR_GL_UODECLC_7 | STRING | 1 | — | User OD expense 7 calculation type flag |
| 337 | BKPR_GL_UODECLC_8 | STRING | 1 | — | User OD expense 8 calculation type flag |
| 338 | BKPR_GL_UODECLC_9 | STRING | 1 | — | User OD expense 9 calculation type flag |
| 339 | BKPR_GL_UODEDPT_1 | STRING | 4 | — | User OD expense GL department 1 |
| 340 | BKPR_GL_UODEDPT_10 | STRING | 4 | — | User OD expense GL department 10 |
| 341 | BKPR_GL_UODEDPT_11 | STRING | 4 | — | User OD expense GL department 11 |
| 342 | BKPR_GL_UODEDPT_12 | STRING | 4 | — | User OD expense GL department 12 |
| 343 | BKPR_GL_UODEDPT_13 | STRING | 4 | — | User OD expense GL department 13 |
| 344 | BKPR_GL_UODEDPT_14 | STRING | 4 | — | User OD expense GL department 14 |
| 345 | BKPR_GL_UODEDPT_15 | STRING | 4 | — | User OD expense GL department 15 |
| 346 | BKPR_GL_UODEDPT_16 | STRING | 4 | — | User OD expense GL department 16 |
| 347 | BKPR_GL_UODEDPT_17 | STRING | 4 | — | User OD expense GL department 17 |
| 348 | BKPR_GL_UODEDPT_18 | STRING | 4 | — | User OD expense GL department 18 |
| 349 | BKPR_GL_UODEDPT_19 | STRING | 4 | — | User OD expense GL department 19 |
| 350 | BKPR_GL_UODEDPT_2 | STRING | 4 | — | User OD expense GL department 2 |
| 351 | BKPR_GL_UODEDPT_20 | STRING | 4 | — | User OD expense GL department 20 |
| 352 | BKPR_GL_UODEDPT_3 | STRING | 4 | — | User OD expense GL department 3 |
| 353 | BKPR_GL_UODEDPT_4 | STRING | 4 | — | User OD expense GL department 4 |
| 354 | BKPR_GL_UODEDPT_5 | STRING | 4 | — | User OD expense GL department 5 |
| 355 | BKPR_GL_UODEDPT_6 | STRING | 4 | — | User OD expense GL department 6 |
| 356 | BKPR_GL_UODEDPT_7 | STRING | 4 | — | User OD expense GL department 7 |
| 357 | BKPR_GL_UODEDPT_8 | STRING | 4 | — | User OD expense GL department 8 |
| 358 | BKPR_GL_UODEDPT_9 | STRING | 4 | — | User OD expense GL department 9 |
| 359 | BKPR_GL_UODELMT_1 | NUMERIC | 8 | 4 | User OD 1 employee per-period limit |
| 360 | BKPR_GL_UODELMT_10 | NUMERIC | 8 | 4 | User OD 10 employee per-period limit |
| 361 | BKPR_GL_UODELMT_11 | NUMERIC | 8 | 4 | User OD 11 employee per-period limit |
| 362 | BKPR_GL_UODELMT_12 | NUMERIC | 8 | 4 | User OD 12 employee per-period limit |
| 363 | BKPR_GL_UODELMT_13 | NUMERIC | 8 | 4 | User OD 13 employee per-period limit |
| 364 | BKPR_GL_UODELMT_14 | NUMERIC | 8 | 4 | User OD 14 employee per-period limit |
| 365 | BKPR_GL_UODELMT_15 | NUMERIC | 8 | 4 | User OD 15 employee per-period limit |
| 366 | BKPR_GL_UODELMT_16 | NUMERIC | 8 | 4 | User OD 16 employee per-period limit |
| 367 | BKPR_GL_UODELMT_17 | NUMERIC | 8 | 4 | User OD 17 employee per-period limit |
| 368 | BKPR_GL_UODELMT_18 | NUMERIC | 8 | 4 | User OD 18 employee per-period limit |
| 369 | BKPR_GL_UODELMT_19 | NUMERIC | 8 | 4 | User OD 19 employee per-period limit |
| 370 | BKPR_GL_UODELMT_2 | NUMERIC | 8 | 4 | User OD 2 employee per-period limit |
| 371 | BKPR_GL_UODELMT_20 | NUMERIC | 8 | 4 | User OD 20 employee per-period limit |
| 372 | BKPR_GL_UODELMT_3 | NUMERIC | 8 | 4 | User OD 3 employee per-period limit |
| 373 | BKPR_GL_UODELMT_4 | NUMERIC | 8 | 4 | User OD 4 employee per-period limit |
| 374 | BKPR_GL_UODELMT_5 | NUMERIC | 8 | 4 | User OD 5 employee per-period limit |
| 375 | BKPR_GL_UODELMT_6 | NUMERIC | 8 | 4 | User OD 6 employee per-period limit |
| 376 | BKPR_GL_UODELMT_7 | NUMERIC | 8 | 4 | User OD 7 employee per-period limit |
| 377 | BKPR_GL_UODELMT_8 | NUMERIC | 8 | 4 | User OD 8 employee per-period limit |
| 378 | BKPR_GL_UODELMT_9 | NUMERIC | 8 | 4 | User OD 9 employee per-period limit |
| 379 | BKPR_GL_UODEYLM_1 | NUMERIC | 8 | 2 | User OD 1 employee annual limit |
| 380 | BKPR_GL_UODEYLM_10 | NUMERIC | 8 | 2 | User OD 10 employee annual limit |
| 381 | BKPR_GL_UODEYLM_11 | NUMERIC | 8 | 2 | User OD 11 employee annual limit |
| 382 | BKPR_GL_UODEYLM_12 | NUMERIC | 8 | 2 | User OD 12 employee annual limit |
| 383 | BKPR_GL_UODEYLM_13 | NUMERIC | 8 | 2 | User OD 13 employee annual limit |
| 384 | BKPR_GL_UODEYLM_14 | NUMERIC | 8 | 2 | User OD 14 employee annual limit |
| 385 | BKPR_GL_UODEYLM_15 | NUMERIC | 8 | 2 | User OD 15 employee annual limit |
| 386 | BKPR_GL_UODEYLM_16 | NUMERIC | 8 | 2 | User OD 16 employee annual limit |
| 387 | BKPR_GL_UODEYLM_17 | NUMERIC | 8 | 2 | User OD 17 employee annual limit |
| 388 | BKPR_GL_UODEYLM_18 | NUMERIC | 8 | 2 | User OD 18 employee annual limit |
| 389 | BKPR_GL_UODEYLM_19 | NUMERIC | 8 | 2 | User OD 19 employee annual limit |
| 390 | BKPR_GL_UODEYLM_2 | NUMERIC | 8 | 2 | User OD 2 employee annual limit |
| 391 | BKPR_GL_UODEYLM_20 | NUMERIC | 8 | 2 | User OD 20 employee annual limit |
| 392 | BKPR_GL_UODEYLM_3 | NUMERIC | 8 | 2 | User OD 3 employee annual limit |
| 393 | BKPR_GL_UODEYLM_4 | NUMERIC | 8 | 2 | User OD 4 employee annual limit |
| 394 | BKPR_GL_UODEYLM_5 | NUMERIC | 8 | 2 | User OD 5 employee annual limit |
| 395 | BKPR_GL_UODEYLM_6 | NUMERIC | 8 | 2 | User OD 6 employee annual limit |
| 396 | BKPR_GL_UODEYLM_7 | NUMERIC | 8 | 2 | User OD 7 employee annual limit |
| 397 | BKPR_GL_UODEYLM_8 | NUMERIC | 8 | 2 | User OD 8 employee annual limit |
| 398 | BKPR_GL_UODEYLM_9 | NUMERIC | 8 | 2 | User OD 9 employee annual limit |
| 399 | BKPR_GL_UODFICA_1 | STRING | 1 | — | User OD 1 FICA-applicable flag (Y/N) |
| 400 | BKPR_GL_UODFICA_10 | STRING | 1 | — | User OD 10 FICA-applicable flag (Y/N) |
| 401 | BKPR_GL_UODFICA_11 | STRING | 1 | — | User OD 11 FICA-applicable flag (Y/N) |
| 402 | BKPR_GL_UODFICA_12 | STRING | 1 | — | User OD 12 FICA-applicable flag (Y/N) |
| 403 | BKPR_GL_UODFICA_13 | STRING | 1 | — | User OD 13 FICA-applicable flag (Y/N) |
| 404 | BKPR_GL_UODFICA_14 | STRING | 1 | — | User OD 14 FICA-applicable flag (Y/N) |
| 405 | BKPR_GL_UODFICA_15 | STRING | 1 | — | User OD 15 FICA-applicable flag (Y/N) |
| 406 | BKPR_GL_UODFICA_16 | STRING | 1 | — | User OD 16 FICA-applicable flag (Y/N) |
| 407 | BKPR_GL_UODFICA_17 | STRING | 1 | — | User OD 17 FICA-applicable flag (Y/N) |
| 408 | BKPR_GL_UODFICA_18 | STRING | 1 | — | User OD 18 FICA-applicable flag (Y/N) |
| 409 | BKPR_GL_UODFICA_19 | STRING | 1 | — | User OD 19 FICA-applicable flag (Y/N) |
| 410 | BKPR_GL_UODFICA_2 | STRING | 1 | — | User OD 2 FICA-applicable flag (Y/N) |
| 411 | BKPR_GL_UODFICA_20 | STRING | 1 | — | User OD 20 FICA-applicable flag (Y/N) |
| 412 | BKPR_GL_UODFICA_3 | STRING | 1 | — | User OD 3 FICA-applicable flag (Y/N) |
| 413 | BKPR_GL_UODFICA_4 | STRING | 1 | — | User OD 4 FICA-applicable flag (Y/N) |
| 414 | BKPR_GL_UODFICA_5 | STRING | 1 | — | User OD 5 FICA-applicable flag (Y/N) |
| 415 | BKPR_GL_UODFICA_6 | STRING | 1 | — | User OD 6 FICA-applicable flag (Y/N) |
| 416 | BKPR_GL_UODFICA_7 | STRING | 1 | — | User OD 7 FICA-applicable flag (Y/N) |
| 417 | BKPR_GL_UODFICA_8 | STRING | 1 | — | User OD 8 FICA-applicable flag (Y/N) |
| 418 | BKPR_GL_UODFICA_9 | STRING | 1 | — | User OD 9 FICA-applicable flag (Y/N) |
| 419 | BKPR_GL_UODFIT_1 | STRING | 1 | — | User OD 1 FIT-applicable flag (Y/N) |
| 420 | BKPR_GL_UODFIT_10 | STRING | 1 | — | User OD 10 FIT-applicable flag (Y/N) |
| 421 | BKPR_GL_UODFIT_11 | STRING | 1 | — | User OD 11 FIT-applicable flag (Y/N) |
| 422 | BKPR_GL_UODFIT_12 | STRING | 1 | — | User OD 12 FIT-applicable flag (Y/N) |
| 423 | BKPR_GL_UODFIT_13 | STRING | 1 | — | User OD 13 FIT-applicable flag (Y/N) |
| 424 | BKPR_GL_UODFIT_14 | STRING | 1 | — | User OD 14 FIT-applicable flag (Y/N) |
| 425 | BKPR_GL_UODFIT_15 | STRING | 1 | — | User OD 15 FIT-applicable flag (Y/N) |
| 426 | BKPR_GL_UODFIT_16 | STRING | 1 | — | User OD 16 FIT-applicable flag (Y/N) |
| 427 | BKPR_GL_UODFIT_17 | STRING | 1 | — | User OD 17 FIT-applicable flag (Y/N) |
| 428 | BKPR_GL_UODFIT_18 | STRING | 1 | — | User OD 18 FIT-applicable flag (Y/N) |
| 429 | BKPR_GL_UODFIT_19 | STRING | 1 | — | User OD 19 FIT-applicable flag (Y/N) |
| 430 | BKPR_GL_UODFIT_2 | STRING | 1 | — | User OD 2 FIT-applicable flag (Y/N) |
| 431 | BKPR_GL_UODFIT_20 | STRING | 1 | — | User OD 20 FIT-applicable flag (Y/N) |
| 432 | BKPR_GL_UODFIT_3 | STRING | 1 | — | User OD 3 FIT-applicable flag (Y/N) |
| 433 | BKPR_GL_UODFIT_4 | STRING | 1 | — | User OD 4 FIT-applicable flag (Y/N) |
| 434 | BKPR_GL_UODFIT_5 | STRING | 1 | — | User OD 5 FIT-applicable flag (Y/N) |
| 435 | BKPR_GL_UODFIT_6 | STRING | 1 | — | User OD 6 FIT-applicable flag (Y/N) |
| 436 | BKPR_GL_UODFIT_7 | STRING | 1 | — | User OD 7 FIT-applicable flag (Y/N) |
| 437 | BKPR_GL_UODFIT_8 | STRING | 1 | — | User OD 8 FIT-applicable flag (Y/N) |
| 438 | BKPR_GL_UODFIT_9 | STRING | 1 | — | User OD 9 FIT-applicable flag (Y/N) |
| 439 | BKPR_GL_UODFUTA_1 | STRING | 1 | — | User OD 1 FUTA-applicable flag (Y/N) |
| 440 | BKPR_GL_UODFUTA_10 | STRING | 1 | — | User OD 10 FUTA-applicable flag (Y/N) |
| 441 | BKPR_GL_UODFUTA_11 | STRING | 1 | — | User OD 11 FUTA-applicable flag (Y/N) |
| 442 | BKPR_GL_UODFUTA_12 | STRING | 1 | — | User OD 12 FUTA-applicable flag (Y/N) |
| 443 | BKPR_GL_UODFUTA_13 | STRING | 1 | — | User OD 13 FUTA-applicable flag (Y/N) |
| 444 | BKPR_GL_UODFUTA_14 | STRING | 1 | — | User OD 14 FUTA-applicable flag (Y/N) |
| 445 | BKPR_GL_UODFUTA_15 | STRING | 1 | — | User OD 15 FUTA-applicable flag (Y/N) |
| 446 | BKPR_GL_UODFUTA_16 | STRING | 1 | — | User OD 16 FUTA-applicable flag (Y/N) |
| 447 | BKPR_GL_UODFUTA_17 | STRING | 1 | — | User OD 17 FUTA-applicable flag (Y/N) |
| 448 | BKPR_GL_UODFUTA_18 | STRING | 1 | — | User OD 18 FUTA-applicable flag (Y/N) |
| 449 | BKPR_GL_UODFUTA_19 | STRING | 1 | — | User OD 19 FUTA-applicable flag (Y/N) |
| 450 | BKPR_GL_UODFUTA_2 | STRING | 1 | — | User OD 2 FUTA-applicable flag (Y/N) |
| 451 | BKPR_GL_UODFUTA_20 | STRING | 1 | — | User OD 20 FUTA-applicable flag (Y/N) |
| 452 | BKPR_GL_UODFUTA_3 | STRING | 1 | — | User OD 3 FUTA-applicable flag (Y/N) |
| 453 | BKPR_GL_UODFUTA_4 | STRING | 1 | — | User OD 4 FUTA-applicable flag (Y/N) |
| 454 | BKPR_GL_UODFUTA_5 | STRING | 1 | — | User OD 5 FUTA-applicable flag (Y/N) |
| 455 | BKPR_GL_UODFUTA_6 | STRING | 1 | — | User OD 6 FUTA-applicable flag (Y/N) |
| 456 | BKPR_GL_UODFUTA_7 | STRING | 1 | — | User OD 7 FUTA-applicable flag (Y/N) |
| 457 | BKPR_GL_UODFUTA_8 | STRING | 1 | — | User OD 8 FUTA-applicable flag (Y/N) |
| 458 | BKPR_GL_UODFUTA_9 | STRING | 1 | — | User OD 9 FUTA-applicable flag (Y/N) |
| 459 | BKPR_GL_UODLMT_1 | NUMERIC | 8 | 4 | User OD 1 per-period limit |
| 460 | BKPR_GL_UODLMT_10 | NUMERIC | 8 | 4 | User OD 10 per-period limit |
| 461 | BKPR_GL_UODLMT_11 | NUMERIC | 8 | 4 | User OD 11 per-period limit |
| 462 | BKPR_GL_UODLMT_12 | NUMERIC | 8 | 4 | User OD 12 per-period limit |
| 463 | BKPR_GL_UODLMT_13 | NUMERIC | 8 | 4 | User OD 13 per-period limit |
| 464 | BKPR_GL_UODLMT_14 | NUMERIC | 8 | 4 | User OD 14 per-period limit |
| 465 | BKPR_GL_UODLMT_15 | NUMERIC | 8 | 4 | User OD 15 per-period limit |
| 466 | BKPR_GL_UODLMT_16 | NUMERIC | 8 | 4 | User OD 16 per-period limit |
| 467 | BKPR_GL_UODLMT_17 | NUMERIC | 8 | 4 | User OD 17 per-period limit |
| 468 | BKPR_GL_UODLMT_18 | NUMERIC | 8 | 4 | User OD 18 per-period limit |
| 469 | BKPR_GL_UODLMT_19 | NUMERIC | 8 | 4 | User OD 19 per-period limit |
| 470 | BKPR_GL_UODLMT_2 | NUMERIC | 8 | 4 | User OD 2 per-period limit |
| 471 | BKPR_GL_UODLMT_20 | NUMERIC | 8 | 4 | User OD 20 per-period limit |
| 472 | BKPR_GL_UODLMT_3 | NUMERIC | 8 | 4 | User OD 3 per-period limit |
| 473 | BKPR_GL_UODLMT_4 | NUMERIC | 8 | 4 | User OD 4 per-period limit |
| 474 | BKPR_GL_UODLMT_5 | NUMERIC | 8 | 4 | User OD 5 per-period limit |
| 475 | BKPR_GL_UODLMT_6 | NUMERIC | 8 | 4 | User OD 6 per-period limit |
| 476 | BKPR_GL_UODLMT_7 | NUMERIC | 8 | 4 | User OD 7 per-period limit |
| 477 | BKPR_GL_UODLMT_8 | NUMERIC | 8 | 4 | User OD 8 per-period limit |
| 478 | BKPR_GL_UODLMT_9 | NUMERIC | 8 | 4 | User OD 9 per-period limit |
| 479 | BKPR_GL_UODLOC1_1 | STRING | 1 | — | User OD 1 local tax 1 applicable flag (Y/N) |
| 480 | BKPR_GL_UODLOC1_10 | STRING | 1 | — | User OD 10 local tax 1 applicable flag (Y/N) |
| 481 | BKPR_GL_UODLOC1_11 | STRING | 1 | — | User OD 11 local tax 1 applicable flag (Y/N) |
| 482 | BKPR_GL_UODLOC1_12 | STRING | 1 | — | User OD 12 local tax 1 applicable flag (Y/N) |
| 483 | BKPR_GL_UODLOC1_13 | STRING | 1 | — | User OD 13 local tax 1 applicable flag (Y/N) |
| 484 | BKPR_GL_UODLOC1_14 | STRING | 1 | — | User OD 14 local tax 1 applicable flag (Y/N) |
| 485 | BKPR_GL_UODLOC1_15 | STRING | 1 | — | User OD 15 local tax 1 applicable flag (Y/N) |
| 486 | BKPR_GL_UODLOC1_16 | STRING | 1 | — | User OD 16 local tax 1 applicable flag (Y/N) |
| 487 | BKPR_GL_UODLOC1_17 | STRING | 1 | — | User OD 17 local tax 1 applicable flag (Y/N) |
| 488 | BKPR_GL_UODLOC1_18 | STRING | 1 | — | User OD 18 local tax 1 applicable flag (Y/N) |
| 489 | BKPR_GL_UODLOC1_19 | STRING | 1 | — | User OD 19 local tax 1 applicable flag (Y/N) |
| 490 | BKPR_GL_UODLOC1_2 | STRING | 1 | — | User OD 2 local tax 1 applicable flag (Y/N) |
| 491 | BKPR_GL_UODLOC1_20 | STRING | 1 | — | User OD 20 local tax 1 applicable flag (Y/N) |
| 492 | BKPR_GL_UODLOC1_3 | STRING | 1 | — | User OD 3 local tax 1 applicable flag (Y/N) |
| 493 | BKPR_GL_UODLOC1_4 | STRING | 1 | — | User OD 4 local tax 1 applicable flag (Y/N) |
| 494 | BKPR_GL_UODLOC1_5 | STRING | 1 | — | User OD 5 local tax 1 applicable flag (Y/N) |
| 495 | BKPR_GL_UODLOC1_6 | STRING | 1 | — | User OD 6 local tax 1 applicable flag (Y/N) |
| 496 | BKPR_GL_UODLOC1_7 | STRING | 1 | — | User OD 7 local tax 1 applicable flag (Y/N) |
| 497 | BKPR_GL_UODLOC1_8 | STRING | 1 | — | User OD 8 local tax 1 applicable flag (Y/N) |
| 498 | BKPR_GL_UODLOC1_9 | STRING | 1 | — | User OD 9 local tax 1 applicable flag (Y/N) |
| 499 | BKPR_GL_UODMED_1 | STRING | 1 | — | User OD 1 Medicare-applicable flag (Y/N) |
| 500 | BKPR_GL_UODMED_10 | STRING | 1 | — | User OD 10 Medicare-applicable flag (Y/N) |
| 501 | BKPR_GL_UODMED_11 | STRING | 1 | — | User OD 11 Medicare-applicable flag (Y/N) |
| 502 | BKPR_GL_UODMED_12 | STRING | 1 | — | User OD 12 Medicare-applicable flag (Y/N) |
| 503 | BKPR_GL_UODMED_13 | STRING | 1 | — | User OD 13 Medicare-applicable flag (Y/N) |
| 504 | BKPR_GL_UODMED_14 | STRING | 1 | — | User OD 14 Medicare-applicable flag (Y/N) |
| 505 | BKPR_GL_UODMED_15 | STRING | 1 | — | User OD 15 Medicare-applicable flag (Y/N) |
| 506 | BKPR_GL_UODMED_16 | STRING | 1 | — | User OD 16 Medicare-applicable flag (Y/N) |
| 507 | BKPR_GL_UODMED_17 | STRING | 1 | — | User OD 17 Medicare-applicable flag (Y/N) |
| 508 | BKPR_GL_UODMED_18 | STRING | 1 | — | User OD 18 Medicare-applicable flag (Y/N) |
| 509 | BKPR_GL_UODMED_19 | STRING | 1 | — | User OD 19 Medicare-applicable flag (Y/N) |
| 510 | BKPR_GL_UODMED_2 | STRING | 1 | — | User OD 2 Medicare-applicable flag (Y/N) |
| 511 | BKPR_GL_UODMED_20 | STRING | 1 | — | User OD 20 Medicare-applicable flag (Y/N) |
| 512 | BKPR_GL_UODMED_3 | STRING | 1 | — | User OD 3 Medicare-applicable flag (Y/N) |
| 513 | BKPR_GL_UODMED_4 | STRING | 1 | — | User OD 4 Medicare-applicable flag (Y/N) |
| 514 | BKPR_GL_UODMED_5 | STRING | 1 | — | User OD 5 Medicare-applicable flag (Y/N) |
| 515 | BKPR_GL_UODMED_6 | STRING | 1 | — | User OD 6 Medicare-applicable flag (Y/N) |
| 516 | BKPR_GL_UODMED_7 | STRING | 1 | — | User OD 7 Medicare-applicable flag (Y/N) |
| 517 | BKPR_GL_UODMED_8 | STRING | 1 | — | User OD 8 Medicare-applicable flag (Y/N) |
| 518 | BKPR_GL_UODMED_9 | STRING | 1 | — | User OD 9 Medicare-applicable flag (Y/N) |
| 519 | BKPR_GL_UODNAME_1 | STRING | 12 | — | User OD 1 name/description |
| 520 | BKPR_GL_UODNAME_10 | STRING | 12 | — | User OD 10 name/description |
| 521 | BKPR_GL_UODNAME_11 | STRING | 12 | — | User OD 11 name/description |
| 522 | BKPR_GL_UODNAME_12 | STRING | 12 | — | User OD 12 name/description |
| 523 | BKPR_GL_UODNAME_13 | STRING | 12 | — | User OD 13 name/description |
| 524 | BKPR_GL_UODNAME_14 | STRING | 12 | — | User OD 14 name/description |
| 525 | BKPR_GL_UODNAME_15 | STRING | 12 | — | User OD 15 name/description |
| 526 | BKPR_GL_UODNAME_16 | STRING | 12 | — | User OD 16 name/description |
| 527 | BKPR_GL_UODNAME_17 | STRING | 12 | — | User OD 17 name/description |
| 528 | BKPR_GL_UODNAME_18 | STRING | 12 | — | User OD 18 name/description |
| 529 | BKPR_GL_UODNAME_19 | STRING | 12 | — | User OD 19 name/description |
| 530 | BKPR_GL_UODNAME_2 | STRING | 12 | — | User OD 2 name/description |
| 531 | BKPR_GL_UODNAME_20 | STRING | 12 | — | User OD 20 name/description |
| 532 | BKPR_GL_UODNAME_3 | STRING | 12 | — | User OD 3 name/description |
| 533 | BKPR_GL_UODNAME_4 | STRING | 12 | — | User OD 4 name/description |
| 534 | BKPR_GL_UODNAME_5 | STRING | 12 | — | User OD 5 name/description |
| 535 | BKPR_GL_UODNAME_6 | STRING | 12 | — | User OD 6 name/description |
| 536 | BKPR_GL_UODNAME_7 | STRING | 12 | — | User OD 7 name/description |
| 537 | BKPR_GL_UODNAME_8 | STRING | 12 | — | User OD 8 name/description |
| 538 | BKPR_GL_UODNAME_9 | STRING | 12 | — | User OD 9 name/description |
| 539 | BKPR_GL_UODPTX_1 | STRING | 1 | — | User OD 1 pre-tax flag (Y/N) |
| 540 | BKPR_GL_UODPTX_10 | STRING | 1 | — | User OD 10 pre-tax flag (Y/N) |
| 541 | BKPR_GL_UODPTX_11 | STRING | 1 | — | User OD 11 pre-tax flag (Y/N) |
| 542 | BKPR_GL_UODPTX_12 | STRING | 1 | — | User OD 12 pre-tax flag (Y/N) |
| 543 | BKPR_GL_UODPTX_13 | STRING | 1 | — | User OD 13 pre-tax flag (Y/N) |
| 544 | BKPR_GL_UODPTX_14 | STRING | 1 | — | User OD 14 pre-tax flag (Y/N) |
| 545 | BKPR_GL_UODPTX_15 | STRING | 1 | — | User OD 15 pre-tax flag (Y/N) |
| 546 | BKPR_GL_UODPTX_16 | STRING | 1 | — | User OD 16 pre-tax flag (Y/N) |
| 547 | BKPR_GL_UODPTX_17 | STRING | 1 | — | User OD 17 pre-tax flag (Y/N) |
| 548 | BKPR_GL_UODPTX_18 | STRING | 1 | — | User OD 18 pre-tax flag (Y/N) |
| 549 | BKPR_GL_UODPTX_19 | STRING | 1 | — | User OD 19 pre-tax flag (Y/N) |
| 550 | BKPR_GL_UODPTX_2 | STRING | 1 | — | User OD 2 pre-tax flag (Y/N) |
| 551 | BKPR_GL_UODPTX_20 | STRING | 1 | — | User OD 20 pre-tax flag (Y/N) |
| 552 | BKPR_GL_UODPTX_3 | STRING | 1 | — | User OD 3 pre-tax flag (Y/N) |
| 553 | BKPR_GL_UODPTX_4 | STRING | 1 | — | User OD 4 pre-tax flag (Y/N) |
| 554 | BKPR_GL_UODPTX_5 | STRING | 1 | — | User OD 5 pre-tax flag (Y/N) |
| 555 | BKPR_GL_UODPTX_6 | STRING | 1 | — | User OD 6 pre-tax flag (Y/N) |
| 556 | BKPR_GL_UODPTX_7 | STRING | 1 | — | User OD 7 pre-tax flag (Y/N) |
| 557 | BKPR_GL_UODPTX_8 | STRING | 1 | — | User OD 8 pre-tax flag (Y/N) |
| 558 | BKPR_GL_UODPTX_9 | STRING | 1 | — | User OD 9 pre-tax flag (Y/N) |
| 559 | BKPR_GL_UODSDI_1 | STRING | 1 | — | User OD 1 SDI-applicable flag (Y/N) |
| 560 | BKPR_GL_UODSDI_10 | STRING | 1 | — | User OD 10 SDI-applicable flag (Y/N) |
| 561 | BKPR_GL_UODSDI_11 | STRING | 1 | — | User OD 11 SDI-applicable flag (Y/N) |
| 562 | BKPR_GL_UODSDI_12 | STRING | 1 | — | User OD 12 SDI-applicable flag (Y/N) |
| 563 | BKPR_GL_UODSDI_13 | STRING | 1 | — | User OD 13 SDI-applicable flag (Y/N) |
| 564 | BKPR_GL_UODSDI_14 | STRING | 1 | — | User OD 14 SDI-applicable flag (Y/N) |
| 565 | BKPR_GL_UODSDI_15 | STRING | 1 | — | User OD 15 SDI-applicable flag (Y/N) |
| 566 | BKPR_GL_UODSDI_16 | STRING | 1 | — | User OD 16 SDI-applicable flag (Y/N) |
| 567 | BKPR_GL_UODSDI_17 | STRING | 1 | — | User OD 17 SDI-applicable flag (Y/N) |
| 568 | BKPR_GL_UODSDI_18 | STRING | 1 | — | User OD 18 SDI-applicable flag (Y/N) |
| 569 | BKPR_GL_UODSDI_19 | STRING | 1 | — | User OD 19 SDI-applicable flag (Y/N) |
| 570 | BKPR_GL_UODSDI_2 | STRING | 1 | — | User OD 2 SDI-applicable flag (Y/N) |
| 571 | BKPR_GL_UODSDI_20 | STRING | 1 | — | User OD 20 SDI-applicable flag (Y/N) |
| 572 | BKPR_GL_UODSDI_3 | STRING | 1 | — | User OD 3 SDI-applicable flag (Y/N) |
| 573 | BKPR_GL_UODSDI_4 | STRING | 1 | — | User OD 4 SDI-applicable flag (Y/N) |
| 574 | BKPR_GL_UODSDI_5 | STRING | 1 | — | User OD 5 SDI-applicable flag (Y/N) |
| 575 | BKPR_GL_UODSDI_6 | STRING | 1 | — | User OD 6 SDI-applicable flag (Y/N) |
| 576 | BKPR_GL_UODSDI_7 | STRING | 1 | — | User OD 7 SDI-applicable flag (Y/N) |
| 577 | BKPR_GL_UODSDI_8 | STRING | 1 | — | User OD 8 SDI-applicable flag (Y/N) |
| 578 | BKPR_GL_UODSDI_9 | STRING | 1 | — | User OD 9 SDI-applicable flag (Y/N) |
| 579 | BKPR_GL_UODSIT_1 | STRING | 1 | — | User OD 1 SIT-applicable flag (Y/N) |
| 580 | BKPR_GL_UODSIT_10 | STRING | 1 | — | User OD 10 SIT-applicable flag (Y/N) |
| 581 | BKPR_GL_UODSIT_11 | STRING | 1 | — | User OD 11 SIT-applicable flag (Y/N) |
| 582 | BKPR_GL_UODSIT_12 | STRING | 1 | — | User OD 12 SIT-applicable flag (Y/N) |
| 583 | BKPR_GL_UODSIT_13 | STRING | 1 | — | User OD 13 SIT-applicable flag (Y/N) |
| 584 | BKPR_GL_UODSIT_14 | STRING | 1 | — | User OD 14 SIT-applicable flag (Y/N) |
| 585 | BKPR_GL_UODSIT_15 | STRING | 1 | — | User OD 15 SIT-applicable flag (Y/N) |
| 586 | BKPR_GL_UODSIT_16 | STRING | 1 | — | User OD 16 SIT-applicable flag (Y/N) |
| 587 | BKPR_GL_UODSIT_17 | STRING | 1 | — | User OD 17 SIT-applicable flag (Y/N) |
| 588 | BKPR_GL_UODSIT_18 | STRING | 1 | — | User OD 18 SIT-applicable flag (Y/N) |
| 589 | BKPR_GL_UODSIT_19 | STRING | 1 | — | User OD 19 SIT-applicable flag (Y/N) |
| 590 | BKPR_GL_UODSIT_2 | STRING | 1 | — | User OD 2 SIT-applicable flag (Y/N) |
| 591 | BKPR_GL_UODSIT_20 | STRING | 1 | — | User OD 20 SIT-applicable flag (Y/N) |
| 592 | BKPR_GL_UODSIT_3 | STRING | 1 | — | User OD 3 SIT-applicable flag (Y/N) |
| 593 | BKPR_GL_UODSIT_4 | STRING | 1 | — | User OD 4 SIT-applicable flag (Y/N) |
| 594 | BKPR_GL_UODSIT_5 | STRING | 1 | — | User OD 5 SIT-applicable flag (Y/N) |
| 595 | BKPR_GL_UODSIT_6 | STRING | 1 | — | User OD 6 SIT-applicable flag (Y/N) |
| 596 | BKPR_GL_UODSIT_7 | STRING | 1 | — | User OD 7 SIT-applicable flag (Y/N) |
| 597 | BKPR_GL_UODSIT_8 | STRING | 1 | — | User OD 8 SIT-applicable flag (Y/N) |
| 598 | BKPR_GL_UODSIT_9 | STRING | 1 | — | User OD 9 SIT-applicable flag (Y/N) |
| 599 | BKPR_GL_UODSUTA_1 | STRING | 1 | — | User OD 1 SUTA-applicable flag (Y/N) |
| 600 | BKPR_GL_UODSUTA_10 | STRING | 1 | — | User OD 10 SUTA-applicable flag (Y/N) |
| 601 | BKPR_GL_UODSUTA_11 | STRING | 1 | — | User OD 11 SUTA-applicable flag (Y/N) |
| 602 | BKPR_GL_UODSUTA_12 | STRING | 1 | — | User OD 12 SUTA-applicable flag (Y/N) |
| 603 | BKPR_GL_UODSUTA_13 | STRING | 1 | — | User OD 13 SUTA-applicable flag (Y/N) |
| 604 | BKPR_GL_UODSUTA_14 | STRING | 1 | — | User OD 14 SUTA-applicable flag (Y/N) |
| 605 | BKPR_GL_UODSUTA_15 | STRING | 1 | — | User OD 15 SUTA-applicable flag (Y/N) |
| 606 | BKPR_GL_UODSUTA_16 | STRING | 1 | — | User OD 16 SUTA-applicable flag (Y/N) |
| 607 | BKPR_GL_UODSUTA_17 | STRING | 1 | — | User OD 17 SUTA-applicable flag (Y/N) |
| 608 | BKPR_GL_UODSUTA_18 | STRING | 1 | — | User OD 18 SUTA-applicable flag (Y/N) |
| 609 | BKPR_GL_UODSUTA_19 | STRING | 1 | — | User OD 19 SUTA-applicable flag (Y/N) |
| 610 | BKPR_GL_UODSUTA_2 | STRING | 1 | — | User OD 2 SUTA-applicable flag (Y/N) |
| 611 | BKPR_GL_UODSUTA_20 | STRING | 1 | — | User OD 20 SUTA-applicable flag (Y/N) |
| 612 | BKPR_GL_UODSUTA_3 | STRING | 1 | — | User OD 3 SUTA-applicable flag (Y/N) |
| 613 | BKPR_GL_UODSUTA_4 | STRING | 1 | — | User OD 4 SUTA-applicable flag (Y/N) |
| 614 | BKPR_GL_UODSUTA_5 | STRING | 1 | — | User OD 5 SUTA-applicable flag (Y/N) |
| 615 | BKPR_GL_UODSUTA_6 | STRING | 1 | — | User OD 6 SUTA-applicable flag (Y/N) |
| 616 | BKPR_GL_UODSUTA_7 | STRING | 1 | — | User OD 7 SUTA-applicable flag (Y/N) |
| 617 | BKPR_GL_UODSUTA_8 | STRING | 1 | — | User OD 8 SUTA-applicable flag (Y/N) |
| 618 | BKPR_GL_UODSUTA_9 | STRING | 1 | — | User OD 9 SUTA-applicable flag (Y/N) |
| 619 | BKPR_GL_UODWC_1 | STRING | 1 | — | User OD 1 workers comp applicable flag (Y/N) |
| 620 | BKPR_GL_UODWC_10 | STRING | 1 | — | User OD 10 workers comp applicable flag (Y/N) |
| 621 | BKPR_GL_UODWC_11 | STRING | 1 | — | User OD 11 workers comp applicable flag (Y/N) |
| 622 | BKPR_GL_UODWC_12 | STRING | 1 | — | User OD 12 workers comp applicable flag (Y/N) |
| 623 | BKPR_GL_UODWC_13 | STRING | 1 | — | User OD 13 workers comp applicable flag (Y/N) |
| 624 | BKPR_GL_UODWC_14 | STRING | 1 | — | User OD 14 workers comp applicable flag (Y/N) |
| 625 | BKPR_GL_UODWC_15 | STRING | 1 | — | User OD 15 workers comp applicable flag (Y/N) |
| 626 | BKPR_GL_UODWC_16 | STRING | 1 | — | User OD 16 workers comp applicable flag (Y/N) |
| 627 | BKPR_GL_UODWC_17 | STRING | 1 | — | User OD 17 workers comp applicable flag (Y/N) |
| 628 | BKPR_GL_UODWC_18 | STRING | 1 | — | User OD 18 workers comp applicable flag (Y/N) |
| 629 | BKPR_GL_UODWC_19 | STRING | 1 | — | User OD 19 workers comp applicable flag (Y/N) |
| 630 | BKPR_GL_UODWC_2 | STRING | 1 | — | User OD 2 workers comp applicable flag (Y/N) |
| 631 | BKPR_GL_UODWC_20 | STRING | 1 | — | User OD 20 workers comp applicable flag (Y/N) |
| 632 | BKPR_GL_UODWC_3 | STRING | 1 | — | User OD 3 workers comp applicable flag (Y/N) |
| 633 | BKPR_GL_UODWC_4 | STRING | 1 | — | User OD 4 workers comp applicable flag (Y/N) |
| 634 | BKPR_GL_UODWC_5 | STRING | 1 | — | User OD 5 workers comp applicable flag (Y/N) |
| 635 | BKPR_GL_UODWC_6 | STRING | 1 | — | User OD 6 workers comp applicable flag (Y/N) |
| 636 | BKPR_GL_UODWC_7 | STRING | 1 | — | User OD 7 workers comp applicable flag (Y/N) |
| 637 | BKPR_GL_UODWC_8 | STRING | 1 | — | User OD 8 workers comp applicable flag (Y/N) |
| 638 | BKPR_GL_UODWC_9 | STRING | 1 | — | User OD 9 workers comp applicable flag (Y/N) |
| 639 | BKPR_GL_UODYLMT_1 | NUMERIC | 8 | 2 | User OD 1 annual limit |
| 640 | BKPR_GL_UODYLMT_10 | NUMERIC | 8 | 2 | User OD 10 annual limit |
| 641 | BKPR_GL_UODYLMT_11 | NUMERIC | 8 | 2 | User OD 11 annual limit |
| 642 | BKPR_GL_UODYLMT_12 | NUMERIC | 8 | 2 | User OD 12 annual limit |
| 643 | BKPR_GL_UODYLMT_13 | NUMERIC | 8 | 2 | User OD 13 annual limit |
| 644 | BKPR_GL_UODYLMT_14 | NUMERIC | 8 | 2 | User OD 14 annual limit |
| 645 | BKPR_GL_UODYLMT_15 | NUMERIC | 8 | 2 | User OD 15 annual limit |
| 646 | BKPR_GL_UODYLMT_16 | NUMERIC | 8 | 2 | User OD 16 annual limit |
| 647 | BKPR_GL_UODYLMT_17 | NUMERIC | 8 | 2 | User OD 17 annual limit |
| 648 | BKPR_GL_UODYLMT_18 | NUMERIC | 8 | 2 | User OD 18 annual limit |
| 649 | BKPR_GL_UODYLMT_19 | NUMERIC | 8 | 2 | User OD 19 annual limit |
| 650 | BKPR_GL_UODYLMT_2 | NUMERIC | 8 | 2 | User OD 2 annual limit |
| 651 | BKPR_GL_UODYLMT_20 | NUMERIC | 8 | 2 | User OD 20 annual limit |
| 652 | BKPR_GL_UODYLMT_3 | NUMERIC | 8 | 2 | User OD 3 annual limit |
| 653 | BKPR_GL_UODYLMT_4 | NUMERIC | 8 | 2 | User OD 4 annual limit |
| 654 | BKPR_GL_UODYLMT_5 | NUMERIC | 8 | 2 | User OD 5 annual limit |
| 655 | BKPR_GL_UODYLMT_6 | NUMERIC | 8 | 2 | User OD 6 annual limit |
| 656 | BKPR_GL_UODYLMT_7 | NUMERIC | 8 | 2 | User OD 7 annual limit |
| 657 | BKPR_GL_UODYLMT_8 | NUMERIC | 8 | 2 | User OD 8 annual limit |
| 658 | BKPR_GL_UODYLMT_9 | NUMERIC | 8 | 2 | User OD 9 annual limit |
| 659 | BKPR_GL_VRTE | NUMERIC | 8 | 4 | Vacation pay rate |
| 660 | BKPR_GL_WCACCT | STRING | 10 | — | Workers comp liability GL account |
| 661 | BKPR_GL_WCDPT | STRING | 4 | — | Workers comp liability GL department |
| 662 | BKPR_GL_WCEXD | STRING | 4 | — | Workers comp expense GL department |
| 663 | BKPR_GL_WCEXP | STRING | 10 | — | Workers comp expense GL account |
| 664 | BKPR_GL_WCHOW | STRING | 1 | — | Workers comp calculation method flag |

## BKPRHIST
**PAYROLL HISTORY**

Fields: 127

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKPR_CURP_ACTNM | INTEGER | 2 | — | Bank account slot number for this paycheck |
| 2 | BKPR_CURP_CHKNM | STRING | 6 | — | Check number |
| 3 | BKPR_CURP_EIC | NUMERIC | 8 | 2 | Earned income credit advance payment |
| 4 | BKPR_CURP_EMPNM | INTEGER | 2 | — | Employee number |
| 5 | BKPR_CURP_FICEX_1 | NUMERIC | 8 | 2 | FICA excess contribution (slot 1) for current pay period |
| 6 | BKPR_CURP_FICEX_2 | NUMERIC | 8 | 2 | FICA excess contribution (slot 2) for current pay period |
| 7 | BKPR_CURP_FICWH_1 | NUMERIC | 8 | 2 | FICA withheld (SS=1/Medicare=2) for current pay period |
| 8 | BKPR_CURP_FICWH_2 | NUMERIC | 8 | 2 | FICA withheld (SS=1/Medicare=2) for current pay period |
| 9 | BKPR_CURP_FITWH | NUMERIC | 8 | 2 | Federal income tax withheld |
| 10 | BKPR_CURP_FUTEX | NUMERIC | 8 | 2 | FUTA (federal unemployment) tax expense |
| 11 | BKPR_CURP_MDACT | STRING | 10 | — | Medical deduction GL account |
| 12 | BKPR_CURP_MDAMT | NUMERIC | 8 | 2 | Medical deduction amount |
| 13 | BKPR_CURP_MDDPT | STRING | 4 | — | Medical deduction GL department |
| 14 | BKPR_CURP_MDNME | STRING | 12 | — | Medical deduction name |
| 15 | BKPR_CURP_NTPAY | NUMERIC | 8 | 2 | Net pay amount |
| 16 | BKPR_CURP_ODACT | STRING | 10 | — | Other deduction GL account |
| 17 | BKPR_CURP_ODAMT | NUMERIC | 8 | 2 | Other deduction amount |
| 18 | BKPR_CURP_ODDPT | STRING | 4 | — | Other deduction GL department |
| 19 | BKPR_CURP_ODNME | STRING | 12 | — | Other deduction name |
| 20 | BKPR_CURP_OPACT_1 | STRING | 10 | — | Other pay type 1 GL account for current pay period |
| 21 | BKPR_CURP_OPACT_2 | STRING | 10 | — | Other pay type 2 GL account for current pay period |
| 22 | BKPR_CURP_OPACT_3 | STRING | 10 | — | Other pay type 3 GL account for current pay period |
| 23 | BKPR_CURP_OPACT_4 | STRING | 10 | — | Other pay type 4 GL account for current pay period |
| 24 | BKPR_CURP_OPACT_5 | STRING | 10 | — | Other pay type 5 GL account for current pay period |
| 25 | BKPR_CURP_OPAMT_1 | NUMERIC | 8 | 2 | Other pay type 1 amount for current pay period |
| 26 | BKPR_CURP_OPAMT_10 | NUMERIC | 8 | 2 | Other pay type 10 amount for current pay period |
| 27 | BKPR_CURP_OPAMT_11 | NUMERIC | 8 | 2 | Other pay type 11 amount for current pay period |
| 28 | BKPR_CURP_OPAMT_12 | NUMERIC | 8 | 2 | Other pay type 12 amount for current pay period |
| 29 | BKPR_CURP_OPAMT_2 | NUMERIC | 8 | 2 | Other pay type 2 amount for current pay period |
| 30 | BKPR_CURP_OPAMT_3 | NUMERIC | 8 | 2 | Other pay type 3 amount for current pay period |
| 31 | BKPR_CURP_OPAMT_4 | NUMERIC | 8 | 2 | Other pay type 4 amount for current pay period |
| 32 | BKPR_CURP_OPAMT_5 | NUMERIC | 8 | 2 | Other pay type 5 amount for current pay period |
| 33 | BKPR_CURP_OPAMT_6 | NUMERIC | 8 | 2 | Other pay type 6 amount for current pay period |
| 34 | BKPR_CURP_OPAMT_7 | NUMERIC | 8 | 2 | Other pay type 7 amount for current pay period |
| 35 | BKPR_CURP_OPAMT_8 | NUMERIC | 8 | 2 | Other pay type 8 amount for current pay period |
| 36 | BKPR_CURP_OPAMT_9 | NUMERIC | 8 | 2 | Other pay type 9 amount for current pay period |
| 37 | BKPR_CURP_OPDPT_1 | STRING | 4 | — | Other pay type 1 GL department for current pay period |
| 38 | BKPR_CURP_OPDPT_2 | STRING | 4 | — | Other pay type 2 GL department for current pay period |
| 39 | BKPR_CURP_OPDPT_3 | STRING | 4 | — | Other pay type 3 GL department for current pay period |
| 40 | BKPR_CURP_OPDPT_4 | STRING | 4 | — | Other pay type 4 GL department for current pay period |
| 41 | BKPR_CURP_OPDPT_5 | STRING | 4 | — | Other pay type 5 GL department for current pay period |
| 42 | BKPR_CURP_OPHRS_1 | NUMERIC | 8 | 2 | Other pay type 1 hours for current pay period |
| 43 | BKPR_CURP_OPHRS_10 | NUMERIC | 8 | 2 | Other pay type 10 hours for current pay period |
| 44 | BKPR_CURP_OPHRS_11 | NUMERIC | 8 | 2 | Other pay type 11 hours for current pay period |
| 45 | BKPR_CURP_OPHRS_12 | NUMERIC | 8 | 2 | Other pay type 12 hours for current pay period |
| 46 | BKPR_CURP_OPHRS_2 | NUMERIC | 8 | 2 | Other pay type 2 hours for current pay period |
| 47 | BKPR_CURP_OPHRS_3 | NUMERIC | 8 | 2 | Other pay type 3 hours for current pay period |
| 48 | BKPR_CURP_OPHRS_4 | NUMERIC | 8 | 2 | Other pay type 4 hours for current pay period |
| 49 | BKPR_CURP_OPHRS_5 | NUMERIC | 8 | 2 | Other pay type 5 hours for current pay period |
| 50 | BKPR_CURP_OPHRS_6 | NUMERIC | 8 | 2 | Other pay type 6 hours for current pay period |
| 51 | BKPR_CURP_OPHRS_7 | NUMERIC | 8 | 2 | Other pay type 7 hours for current pay period |
| 52 | BKPR_CURP_OPHRS_8 | NUMERIC | 8 | 2 | Other pay type 8 hours for current pay period |
| 53 | BKPR_CURP_OPHRS_9 | NUMERIC | 8 | 2 | Other pay type 9 hours for current pay period |
| 54 | BKPR_CURP_OPNME_1 | STRING | 10 | — | Other pay type 1 name for current pay period |
| 55 | BKPR_CURP_OPNME_2 | STRING | 10 | — | Other pay type 2 name for current pay period |
| 56 | BKPR_CURP_OPNME_3 | STRING | 10 | — | Other pay type 3 name for current pay period |
| 57 | BKPR_CURP_OPNME_4 | STRING | 10 | — | Other pay type 4 name for current pay period |
| 58 | BKPR_CURP_OPNME_5 | STRING | 10 | — | Other pay type 5 name for current pay period |
| 59 | BKPR_CURP_OPRTE_1 | NUMERIC | 8 | 4 | Other pay type 1 pay rate for current pay period |
| 60 | BKPR_CURP_OPRTE_10 | NUMERIC | 8 | 4 | Other pay type 10 pay rate for current pay period |
| 61 | BKPR_CURP_OPRTE_11 | NUMERIC | 8 | 4 | Other pay type 11 pay rate for current pay period |
| 62 | BKPR_CURP_OPRTE_12 | NUMERIC | 8 | 4 | Other pay type 12 pay rate for current pay period |
| 63 | BKPR_CURP_OPRTE_2 | NUMERIC | 8 | 4 | Other pay type 2 pay rate for current pay period |
| 64 | BKPR_CURP_OPRTE_3 | NUMERIC | 8 | 4 | Other pay type 3 pay rate for current pay period |
| 65 | BKPR_CURP_OPRTE_4 | NUMERIC | 8 | 4 | Other pay type 4 pay rate for current pay period |
| 66 | BKPR_CURP_OPRTE_5 | NUMERIC | 8 | 4 | Other pay type 5 pay rate for current pay period |
| 67 | BKPR_CURP_OPRTE_6 | NUMERIC | 8 | 4 | Other pay type 6 pay rate for current pay period |
| 68 | BKPR_CURP_OPRTE_7 | NUMERIC | 8 | 4 | Other pay type 7 pay rate for current pay period |
| 69 | BKPR_CURP_OPRTE_8 | NUMERIC | 8 | 4 | Other pay type 8 pay rate for current pay period |
| 70 | BKPR_CURP_OPRTE_9 | NUMERIC | 8 | 4 | Other pay type 9 pay rate for current pay period |
| 71 | BKPR_CURP_PRDTE | DATE | 4 | — | Payroll period date |
| 72 | BKPR_CURP_RPAMT | NUMERIC | 8 | 2 | Regular pay amount |
| 73 | BKPR_CURP_RPHRS | NUMERIC | 8 | 2 | Regular pay hours |
| 74 | BKPR_CURP_RPRTE | NUMERIC | 8 | 4 | Regular pay rate |
| 75 | BKPR_CURP_SDIWH | NUMERIC | 8 | 2 | SDI (state disability) withheld |
| 76 | BKPR_CURP_SITWH | NUMERIC | 8 | 2 | SIT (state income tax) withheld |
| 77 | BKPR_CURP_SPAMT | NUMERIC | 8 | 2 | Special pay amount |
| 78 | BKPR_CURP_SPHRS | NUMERIC | 8 | 2 | Special pay hours |
| 79 | BKPR_CURP_SPRTE | NUMERIC | 8 | 4 | Special pay rate |
| 80 | BKPR_CURP_SUTEX | NUMERIC | 8 | 2 | SUTA (state unemployment) tax expense |
| 81 | BKPR_CURP_TOTHR | NUMERIC | 8 | 2 | Total hours for this pay period |
| 82 | BKPR_CURP_TOTPY | NUMERIC | 8 | 2 | Total gross pay for this pay period |
| 83 | BKPR_CURP_UOD_1 | NUMERIC | 8 | 2 | User other deduction 1 amount for current pay period |
| 84 | BKPR_CURP_UOD_10 | NUMERIC | 8 | 2 | User other deduction 10 amount for current pay period |
| 85 | BKPR_CURP_UOD_11 | NUMERIC | 8 | 2 | User other deduction 11 amount for current pay period |
| 86 | BKPR_CURP_UOD_12 | NUMERIC | 8 | 2 | User other deduction 12 amount for current pay period |
| 87 | BKPR_CURP_UOD_13 | NUMERIC | 8 | 2 | User other deduction 13 amount for current pay period |
| 88 | BKPR_CURP_UOD_14 | NUMERIC | 8 | 2 | User other deduction 14 amount for current pay period |
| 89 | BKPR_CURP_UOD_15 | NUMERIC | 8 | 2 | User other deduction 15 amount for current pay period |
| 90 | BKPR_CURP_UOD_16 | NUMERIC | 8 | 2 | User other deduction 16 amount for current pay period |
| 91 | BKPR_CURP_UOD_17 | NUMERIC | 8 | 2 | User other deduction 17 amount for current pay period |
| 92 | BKPR_CURP_UOD_18 | NUMERIC | 8 | 2 | User other deduction 18 amount for current pay period |
| 93 | BKPR_CURP_UOD_19 | NUMERIC | 8 | 2 | User other deduction 19 amount for current pay period |
| 94 | BKPR_CURP_UOD_2 | NUMERIC | 8 | 2 | User other deduction 2 amount for current pay period |
| 95 | BKPR_CURP_UOD_20 | NUMERIC | 8 | 2 | User other deduction 20 amount for current pay period |
| 96 | BKPR_CURP_UOD_3 | NUMERIC | 8 | 2 | User other deduction 3 amount for current pay period |
| 97 | BKPR_CURP_UOD_4 | NUMERIC | 8 | 2 | User other deduction 4 amount for current pay period |
| 98 | BKPR_CURP_UOD_5 | NUMERIC | 8 | 2 | User other deduction 5 amount for current pay period |
| 99 | BKPR_CURP_UOD_6 | NUMERIC | 8 | 2 | User other deduction 6 amount for current pay period |
| 100 | BKPR_CURP_UOD_7 | NUMERIC | 8 | 2 | User other deduction 7 amount for current pay period |
| 101 | BKPR_CURP_UOD_8 | NUMERIC | 8 | 2 | User other deduction 8 amount for current pay period |
| 102 | BKPR_CURP_UOD_9 | NUMERIC | 8 | 2 | User other deduction 9 amount for current pay period |
| 103 | BKPR_CURP_UODEC_1 | NUMERIC | 8 | 2 | User other deduction 1 employee contribution for current pay period |
| 104 | BKPR_CURP_UODEC_10 | NUMERIC | 8 | 2 | User other deduction 10 employee contribution for current pay period |
| 105 | BKPR_CURP_UODEC_11 | NUMERIC | 8 | 2 | User other deduction 11 employee contribution for current pay period |
| 106 | BKPR_CURP_UODEC_12 | NUMERIC | 8 | 2 | User other deduction 12 employee contribution for current pay period |
| 107 | BKPR_CURP_UODEC_13 | NUMERIC | 8 | 2 | User other deduction 13 employee contribution for current pay period |
| 108 | BKPR_CURP_UODEC_14 | NUMERIC | 8 | 2 | User other deduction 14 employee contribution for current pay period |
| 109 | BKPR_CURP_UODEC_15 | NUMERIC | 8 | 2 | User other deduction 15 employee contribution for current pay period |
| 110 | BKPR_CURP_UODEC_16 | NUMERIC | 8 | 2 | User other deduction 16 employee contribution for current pay period |
| 111 | BKPR_CURP_UODEC_17 | NUMERIC | 8 | 2 | User other deduction 17 employee contribution for current pay period |
| 112 | BKPR_CURP_UODEC_18 | NUMERIC | 8 | 2 | User other deduction 18 employee contribution for current pay period |
| 113 | BKPR_CURP_UODEC_19 | NUMERIC | 8 | 2 | User other deduction 19 employee contribution for current pay period |
| 114 | BKPR_CURP_UODEC_2 | NUMERIC | 8 | 2 | User other deduction 2 employee contribution for current pay period |
| 115 | BKPR_CURP_UODEC_20 | NUMERIC | 8 | 2 | User other deduction 20 employee contribution for current pay period |
| 116 | BKPR_CURP_UODEC_3 | NUMERIC | 8 | 2 | User other deduction 3 employee contribution for current pay period |
| 117 | BKPR_CURP_UODEC_4 | NUMERIC | 8 | 2 | User other deduction 4 employee contribution for current pay period |
| 118 | BKPR_CURP_UODEC_5 | NUMERIC | 8 | 2 | User other deduction 5 employee contribution for current pay period |
| 119 | BKPR_CURP_UODEC_6 | NUMERIC | 8 | 2 | User other deduction 6 employee contribution for current pay period |
| 120 | BKPR_CURP_UODEC_7 | NUMERIC | 8 | 2 | User other deduction 7 employee contribution for current pay period |
| 121 | BKPR_CURP_UODEC_8 | NUMERIC | 8 | 2 | User other deduction 8 employee contribution for current pay period |
| 122 | BKPR_CURP_UODEC_9 | NUMERIC | 8 | 2 | User other deduction 9 employee contribution for current pay period |
| 123 | BKPR_CURP_VPAMT | NUMERIC | 8 | 2 | Vacation pay amount |
| 124 | BKPR_CURP_VPHRS | NUMERIC | 8 | 2 | Vacation pay hours |
| 125 | BKPR_CURP_VPRTE | NUMERIC | 8 | 4 | Vacation pay rate |
| 126 | BKPR_CURP_WCEXP | NUMERIC | 8 | 2 | Workers compensation expense |
| 127 | BKPR_CURP_WCWH | NUMERIC | 8 | 2 | Workers compensation withheld |

## BKPRINFO
**SUPPLEMENTAL EMPLOYEE MASTER**

Fields: 128

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKPR_INFO_AHOW_1 | STRING | 1 | — | Accrual calculation method 1 (H=hours-based, etc.) |
| 2 | BKPR_INFO_AHOW_2 | STRING | 1 | — | Accrual calculation method 2 (H=hours-based, etc.) |
| 3 | BKPR_INFO_AHRS_1 | NUMERIC | 8 | 2 | Accrual 1 hours balance |
| 4 | BKPR_INFO_AHRS_2 | NUMERIC | 8 | 2 | Accrual 2 hours balance |
| 5 | BKPR_INFO_ALPHA_1 | STRING | 25 | — | User-defined alpha field 1 |
| 6 | BKPR_INFO_ALPHA_2 | STRING | 25 | — | User-defined alpha field 2 |
| 7 | BKPR_INFO_ALPHA_3 | STRING | 25 | — | User-defined alpha field 3 |
| 8 | BKPR_INFO_ALPHA_4 | STRING | 25 | — | User-defined alpha field 4 |
| 9 | BKPR_INFO_ALPHA_5 | STRING | 25 | — | User-defined alpha field 5 |
| 10 | BKPR_INFO_AMT_1 | NUMERIC | 8 | 2 | Employee payroll amount field 1 (YTD/QTD totals) |
| 11 | BKPR_INFO_AMT_10 | NUMERIC | 8 | 2 | Employee payroll amount field 10 (YTD/QTD totals) |
| 12 | BKPR_INFO_AMT_11 | NUMERIC | 8 | 2 | Employee payroll amount field 11 (YTD/QTD totals) |
| 13 | BKPR_INFO_AMT_12 | NUMERIC | 8 | 2 | Employee payroll amount field 12 (YTD/QTD totals) |
| 14 | BKPR_INFO_AMT_13 | NUMERIC | 8 | 2 | Employee payroll amount field 13 (YTD/QTD totals) |
| 15 | BKPR_INFO_AMT_14 | NUMERIC | 8 | 2 | Employee payroll amount field 14 (YTD/QTD totals) |
| 16 | BKPR_INFO_AMT_15 | NUMERIC | 8 | 2 | Employee payroll amount field 15 (YTD/QTD totals) |
| 17 | BKPR_INFO_AMT_2 | NUMERIC | 8 | 2 | Employee payroll amount field 2 (YTD/QTD totals) |
| 18 | BKPR_INFO_AMT_3 | NUMERIC | 8 | 2 | Employee payroll amount field 3 (YTD/QTD totals) |
| 19 | BKPR_INFO_AMT_4 | NUMERIC | 8 | 2 | Employee payroll amount field 4 (YTD/QTD totals) |
| 20 | BKPR_INFO_AMT_5 | NUMERIC | 8 | 2 | Employee payroll amount field 5 (YTD/QTD totals) |
| 21 | BKPR_INFO_AMT_6 | NUMERIC | 8 | 2 | Employee payroll amount field 6 (YTD/QTD totals) |
| 22 | BKPR_INFO_AMT_7 | NUMERIC | 8 | 2 | Employee payroll amount field 7 (YTD/QTD totals) |
| 23 | BKPR_INFO_AMT_8 | NUMERIC | 8 | 2 | Employee payroll amount field 8 (YTD/QTD totals) |
| 24 | BKPR_INFO_AMT_9 | NUMERIC | 8 | 2 | Employee payroll amount field 9 (YTD/QTD totals) |
| 25 | BKPR_INFO_ASICK | STRING | 1 | — | Sick time accrual method (H=per-hour, P=per-period) |
| 26 | BKPR_INFO_AVAC | STRING | 1 | — | Vacation time accrual method (H=per-hour, P=per-period) |
| 27 | BKPR_INFO_BINFO_1 | STRING | 30 | — | Banking info line 1 |
| 28 | BKPR_INFO_BINFO_2 | STRING | 30 | — | Banking info line 2 |
| 29 | BKPR_INFO_CTACT_1 | STRING | 30 | — | Emergency contact 1 |
| 30 | BKPR_INFO_CTACT_2 | STRING | 30 | — | Emergency contact 2 |
| 31 | BKPR_INFO_CTACT_3 | STRING | 30 | — | Emergency contact 3 |
| 32 | BKPR_INFO_CTACT_4 | STRING | 30 | — | Emergency contact 4 |
| 33 | BKPR_INFO_CTACT_5 | STRING | 30 | — | Emergency contact 5 |
| 34 | BKPR_INFO_DATE_1 | DATE | 4 | — | User-defined date field 1 |
| 35 | BKPR_INFO_DATE_10 | DATE | 4 | — | User-defined date field 10 |
| 36 | BKPR_INFO_DATE_11 | DATE | 4 | — | User-defined date field 11 |
| 37 | BKPR_INFO_DATE_12 | DATE | 4 | — | User-defined date field 12 |
| 38 | BKPR_INFO_DATE_2 | DATE | 4 | — | User-defined date field 2 |
| 39 | BKPR_INFO_DATE_3 | DATE | 4 | — | User-defined date field 3 |
| 40 | BKPR_INFO_DATE_4 | DATE | 4 | — | User-defined date field 4 |
| 41 | BKPR_INFO_DATE_5 | DATE | 4 | — | User-defined date field 5 |
| 42 | BKPR_INFO_DATE_6 | DATE | 4 | — | User-defined date field 6 |
| 43 | BKPR_INFO_DATE_7 | DATE | 4 | — | User-defined date field 7 |
| 44 | BKPR_INFO_DATE_8 | DATE | 4 | — | User-defined date field 8 |
| 45 | BKPR_INFO_DATE_9 | DATE | 4 | — | User-defined date field 9 |
| 46 | BKPR_INFO_DDEP | STRING | 1 | — | Direct deposit enabled flag (Y/N) |
| 47 | BKPR_INFO_DEDS_1 | NUMERIC | 8 | 2 | Deduction 1 amount |
| 48 | BKPR_INFO_DEDS_2 | NUMERIC | 8 | 2 | Deduction 2 amount |
| 49 | BKPR_INFO_DEDS_3 | NUMERIC | 8 | 2 | Deduction 3 amount |
| 50 | BKPR_INFO_DEDS_4 | NUMERIC | 8 | 2 | Deduction 4 amount |
| 51 | BKPR_INFO_DEDS_5 | NUMERIC | 8 | 2 | Deduction 5 amount |
| 52 | BKPR_INFO_EXTRA | STRING | 50 | — | Reserved extra field |
| 53 | BKPR_INFO_FLAGS_1 | STRING | 1 | — | User-defined flag 1 (Y/N) |
| 54 | BKPR_INFO_FLAGS_2 | STRING | 1 | — | User-defined flag 2 (Y/N) |
| 55 | BKPR_INFO_FLAGS_3 | STRING | 1 | — | User-defined flag 3 (Y/N) |
| 56 | BKPR_INFO_FLAGS_4 | STRING | 1 | — | User-defined flag 4 (Y/N) |
| 57 | BKPR_INFO_FLAGS_5 | STRING | 1 | — | User-defined flag 5 (Y/N) |
| 58 | BKPR_INFO_NOTE_1 | STRING | 60 | — | Employee note line 1 |
| 59 | BKPR_INFO_NOTE_10 | STRING | 60 | — | Employee note line 10 |
| 60 | BKPR_INFO_NOTE_11 | STRING | 60 | — | Employee note line 11 |
| 61 | BKPR_INFO_NOTE_12 | STRING | 60 | — | Employee note line 12 |
| 62 | BKPR_INFO_NOTE_13 | STRING | 60 | — | Employee note line 13 |
| 63 | BKPR_INFO_NOTE_14 | STRING | 60 | — | Employee note line 14 |
| 64 | BKPR_INFO_NOTE_15 | STRING | 60 | — | Employee note line 15 |
| 65 | BKPR_INFO_NOTE_16 | STRING | 60 | — | Employee note line 16 |
| 66 | BKPR_INFO_NOTE_17 | STRING | 60 | — | Employee note line 17 |
| 67 | BKPR_INFO_NOTE_18 | STRING | 60 | — | Employee note line 18 |
| 68 | BKPR_INFO_NOTE_19 | STRING | 60 | — | Employee note line 19 |
| 69 | BKPR_INFO_NOTE_2 | STRING | 60 | — | Employee note line 2 |
| 70 | BKPR_INFO_NOTE_20 | STRING | 60 | — | Employee note line 20 |
| 71 | BKPR_INFO_NOTE_21 | STRING | 60 | — | Employee note line 21 |
| 72 | BKPR_INFO_NOTE_22 | STRING | 60 | — | Employee note line 22 |
| 73 | BKPR_INFO_NOTE_23 | STRING | 60 | — | Employee note line 23 |
| 74 | BKPR_INFO_NOTE_24 | STRING | 60 | — | Employee note line 24 |
| 75 | BKPR_INFO_NOTE_3 | STRING | 60 | — | Employee note line 3 |
| 76 | BKPR_INFO_NOTE_4 | STRING | 60 | — | Employee note line 4 |
| 77 | BKPR_INFO_NOTE_5 | STRING | 60 | — | Employee note line 5 |
| 78 | BKPR_INFO_NOTE_6 | STRING | 60 | — | Employee note line 6 |
| 79 | BKPR_INFO_NOTE_7 | STRING | 60 | — | Employee note line 7 |
| 80 | BKPR_INFO_NOTE_8 | STRING | 60 | — | Employee note line 8 |
| 81 | BKPR_INFO_NOTE_9 | STRING | 60 | — | Employee note line 9 |
| 82 | BKPR_INFO_NUM | INTEGER | 2 | — | Employee number |
| 83 | BKPR_INFO_PHONE_1 | STRING | 15 | — | Employee phone number 1 |
| 84 | BKPR_INFO_PHONE_2 | STRING | 15 | — | Employee phone number 2 |
| 85 | BKPR_INFO_PHONE_3 | STRING | 15 | — | Employee phone number 3 |
| 86 | BKPR_INFO_PHONE_4 | STRING | 15 | — | Employee phone number 4 |
| 87 | BKPR_INFO_PHONE_5 | STRING | 15 | — | Employee phone number 5 |
| 88 | BKPR_INFO_RASDT_1 | DATE | 4 | — | Raise/review 1 actual date |
| 89 | BKPR_INFO_RASDT_2 | DATE | 4 | — | Raise/review 2 actual date |
| 90 | BKPR_INFO_RASDT_3 | DATE | 4 | — | Raise/review 3 actual date |
| 91 | BKPR_INFO_RASDT_4 | DATE | 4 | — | Raise/review 4 actual date |
| 92 | BKPR_INFO_RASDT_5 | DATE | 4 | — | Raise/review 5 actual date |
| 93 | BKPR_INFO_RASDT_6 | DATE | 4 | — | Raise/review 6 actual date |
| 94 | BKPR_INFO_RASNT_1 | STRING | 60 | — | Raise/review 1 note |
| 95 | BKPR_INFO_RASNT_10 | STRING | 60 | — | Raise/review 10 note |
| 96 | BKPR_INFO_RASNT_11 | STRING | 60 | — | Raise/review 11 note |
| 97 | BKPR_INFO_RASNT_12 | STRING | 60 | — | Raise/review 12 note |
| 98 | BKPR_INFO_RASNT_2 | STRING | 60 | — | Raise/review 2 note |
| 99 | BKPR_INFO_RASNT_3 | STRING | 60 | — | Raise/review 3 note |
| 100 | BKPR_INFO_RASNT_4 | STRING | 60 | — | Raise/review 4 note |
| 101 | BKPR_INFO_RASNT_5 | STRING | 60 | — | Raise/review 5 note |
| 102 | BKPR_INFO_RASNT_6 | STRING | 60 | — | Raise/review 6 note |
| 103 | BKPR_INFO_RASNT_7 | STRING | 60 | — | Raise/review 7 note |
| 104 | BKPR_INFO_RASNT_8 | STRING | 60 | — | Raise/review 8 note |
| 105 | BKPR_INFO_RASNT_9 | STRING | 60 | — | Raise/review 9 note |
| 106 | BKPR_INFO_REVDT_1 | DATE | 4 | — | Review date 1 |
| 107 | BKPR_INFO_REVDT_2 | DATE | 4 | — | Review date 2 |
| 108 | BKPR_INFO_REVDT_3 | DATE | 4 | — | Review date 3 |
| 109 | BKPR_INFO_REVDT_4 | DATE | 4 | — | Review date 4 |
| 110 | BKPR_INFO_REVDT_5 | DATE | 4 | — | Review date 5 |
| 111 | BKPR_INFO_REVDT_6 | DATE | 4 | — | Review date 6 |
| 112 | BKPR_INFO_REVNT_1 | STRING | 60 | — | Review note 1 |
| 113 | BKPR_INFO_REVNT_10 | STRING | 60 | — | Review note 10 |
| 114 | BKPR_INFO_REVNT_11 | STRING | 60 | — | Review note 11 |
| 115 | BKPR_INFO_REVNT_12 | STRING | 60 | — | Review note 12 |
| 116 | BKPR_INFO_REVNT_2 | STRING | 60 | — | Review note 2 |
| 117 | BKPR_INFO_REVNT_3 | STRING | 60 | — | Review note 3 |
| 118 | BKPR_INFO_REVNT_4 | STRING | 60 | — | Review note 4 |
| 119 | BKPR_INFO_REVNT_5 | STRING | 60 | — | Review note 5 |
| 120 | BKPR_INFO_REVNT_6 | STRING | 60 | — | Review note 6 |
| 121 | BKPR_INFO_REVNT_7 | STRING | 60 | — | Review note 7 |
| 122 | BKPR_INFO_REVNT_8 | STRING | 60 | — | Review note 8 |
| 123 | BKPR_INFO_REVNT_9 | STRING | 60 | — | Review note 9 |
| 124 | BKPR_INFO_SHRS | NUMERIC | 8 | 2 | Sick time hours balance |
| 125 | BKPR_INFO_SICKA | DATE | 4 | — | Sick time accrual anniversary date |
| 126 | BKPR_INFO_SYNC | STRING | 1 | — | Sync/export flag for external payroll interface |
| 127 | BKPR_INFO_VACAC | DATE | 4 | — | Vacation accrual anniversary date |
| 128 | BKPR_INFO_VHRS | NUMERIC | 8 | 2 | Vacation hours balance |

## BKPRTC
**TIME CARDS**

Fields: 7

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKPR_TC_DATE | DATE | 4 | — | Time clock punch date |
| 2 | BKPR_TC_DEDUCT | TIME | 4 | — | Time deduction (e.g. meal break) |
| 3 | BKPR_TC_EMP | INTEGER | 2 | — | Employee number |
| 4 | BKPR_TC_EXTRA | STRING | 25 | — | Reserved extra field |
| 5 | BKPR_TC_START | TIME | 4 | — | Punch-in start time |
| 6 | BKPR_TC_STOP | TIME | 4 | — | Punch-out stop time |
| 7 | BKPR_TC_TYPE | STRING | 1 | — | Punch type code (R=Regular, O=Overtime, etc.) |

## BKPRW2
**PAYROLL W-2 FILE**

Fields: 384

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKPR_EMP_ADD | STRING | 30 | — | Employee street address |
| 2 | BKPR_EMP_ADDIT_1 | NUMERIC | 8 | 2 | Additional withholding amount 1 |
| 3 | BKPR_EMP_ADDIT_2 | NUMERIC | 8 | 2 | Additional withholding amount 2 |
| 4 | BKPR_EMP_ADDIT_3 | NUMERIC | 8 | 2 | Additional withholding amount 3 |
| 5 | BKPR_EMP_BANKA | STRING | 17 | — | Bank account number for direct deposit |
| 6 | BKPR_EMP_BANKR | STRING | 9 | — | Bank routing number for direct deposit |
| 7 | BKPR_EMP_BDAY | DATE | 4 | — | Employee birth date |
| 8 | BKPR_EMP_BENDTE | DATE | 4 | — | Benefits effective date |
| 9 | BKPR_EMP_CNTRY | STRING | 30 | — | Employee country |
| 10 | BKPR_EMP_CSZ | STRING | 25 | — | Employee city, state, and zip |
| 11 | BKPR_EMP_DEPT | STRING | 4 | — | Employee department code |
| 12 | BKPR_EMP_EIC | NUMERIC | 8 | 2 | Earned income credit advance per period |
| 13 | BKPR_EMP_EICAMT | NUMERIC | 8 | 2 | Total EIC paid to date |
| 14 | BKPR_EMP_EMAIL | STRING | 128 | — | Employee email address |
| 15 | BKPR_EMP_EXPACT_1 | STRING | 10 | — | Employee expense GL account 1 |
| 16 | BKPR_EMP_EXPACT_10 | STRING | 10 | — | Employee expense GL account 10 |
| 17 | BKPR_EMP_EXPACT_11 | STRING | 10 | — | Employee expense GL account 11 |
| 18 | BKPR_EMP_EXPACT_12 | STRING | 10 | — | Employee expense GL account 12 |
| 19 | BKPR_EMP_EXPACT_13 | STRING | 10 | — | Employee expense GL account 13 |
| 20 | BKPR_EMP_EXPACT_14 | STRING | 10 | — | Employee expense GL account 14 |
| 21 | BKPR_EMP_EXPACT_15 | STRING | 10 | — | Employee expense GL account 15 |
| 22 | BKPR_EMP_EXPACT_2 | STRING | 10 | — | Employee expense GL account 2 |
| 23 | BKPR_EMP_EXPACT_3 | STRING | 10 | — | Employee expense GL account 3 |
| 24 | BKPR_EMP_EXPACT_4 | STRING | 10 | — | Employee expense GL account 4 |
| 25 | BKPR_EMP_EXPACT_5 | STRING | 10 | — | Employee expense GL account 5 |
| 26 | BKPR_EMP_EXPACT_6 | STRING | 10 | — | Employee expense GL account 6 |
| 27 | BKPR_EMP_EXPACT_7 | STRING | 10 | — | Employee expense GL account 7 |
| 28 | BKPR_EMP_EXPACT_8 | STRING | 10 | — | Employee expense GL account 8 |
| 29 | BKPR_EMP_EXPACT_9 | STRING | 10 | — | Employee expense GL account 9 |
| 30 | BKPR_EMP_EXPDPT_1 | STRING | 4 | — | Employee expense GL department 1 |
| 31 | BKPR_EMP_EXPDPT_10 | STRING | 4 | — | Employee expense GL department 10 |
| 32 | BKPR_EMP_EXPDPT_11 | STRING | 4 | — | Employee expense GL department 11 |
| 33 | BKPR_EMP_EXPDPT_12 | STRING | 4 | — | Employee expense GL department 12 |
| 34 | BKPR_EMP_EXPDPT_13 | STRING | 4 | — | Employee expense GL department 13 |
| 35 | BKPR_EMP_EXPDPT_14 | STRING | 4 | — | Employee expense GL department 14 |
| 36 | BKPR_EMP_EXPDPT_15 | STRING | 4 | — | Employee expense GL department 15 |
| 37 | BKPR_EMP_EXPDPT_2 | STRING | 4 | — | Employee expense GL department 2 |
| 38 | BKPR_EMP_EXPDPT_3 | STRING | 4 | — | Employee expense GL department 3 |
| 39 | BKPR_EMP_EXPDPT_4 | STRING | 4 | — | Employee expense GL department 4 |
| 40 | BKPR_EMP_EXPDPT_5 | STRING | 4 | — | Employee expense GL department 5 |
| 41 | BKPR_EMP_EXPDPT_6 | STRING | 4 | — | Employee expense GL department 6 |
| 42 | BKPR_EMP_EXPDPT_7 | STRING | 4 | — | Employee expense GL department 7 |
| 43 | BKPR_EMP_EXPDPT_8 | STRING | 4 | — | Employee expense GL department 8 |
| 44 | BKPR_EMP_EXPDPT_9 | STRING | 4 | — | Employee expense GL department 9 |
| 45 | BKPR_EMP_EXTRA | STRING | 200 | — | Reserved extra field |
| 46 | BKPR_EMP_FEDEXM | INTEGER | 2 | — | Number of federal withholding exemptions |
| 47 | BKPR_EMP_FICQTD_1 | NUMERIC | 8 | 2 | FICA QTD (1=SS, 2=Medicare) |
| 48 | BKPR_EMP_FICQTD_2 | NUMERIC | 8 | 2 | FICA QTD (1=SS, 2=Medicare) |
| 49 | BKPR_EMP_FICYTD_1 | NUMERIC | 8 | 2 | FICA YTD (1=SS, 2=Medicare) |
| 50 | BKPR_EMP_FICYTD_2 | NUMERIC | 8 | 2 | FICA YTD (1=SS, 2=Medicare) |
| 51 | BKPR_EMP_FITQTD | NUMERIC | 8 | 2 | Federal income tax withheld QTD |
| 52 | BKPR_EMP_FITYTD | NUMERIC | 8 | 2 | Federal income tax withheld YTD |
| 53 | BKPR_EMP_FNMI | STRING | 25 | — | Employee first name and middle initial |
| 54 | BKPR_EMP_LNME | STRING | 25 | — | Employee last name |
| 55 | BKPR_EMP_LOCCOD | STRING | 2 | — | Local tax code |
| 56 | BKPR_EMP_LSTPR | DATE | 4 | — | Last payroll date |
| 57 | BKPR_EMP_MDACT | STRING | 10 | — | Medical deduction GL account |
| 58 | BKPR_EMP_MDAMT | NUMERIC | 8 | 2 | Medical deduction per-period amount |
| 59 | BKPR_EMP_MDDPT | STRING | 4 | — | Medical deduction GL department |
| 60 | BKPR_EMP_MDNME | STRING | 12 | — | Medical deduction name |
| 61 | BKPR_EMP_MDQTD | NUMERIC | 8 | 2 | Medical deduction QTD amount |
| 62 | BKPR_EMP_MDYTD | NUMERIC | 8 | 2 | Medical deduction YTD amount |
| 63 | BKPR_EMP_MS | STRING | 1 | — | Marital status (S=Single, M=Married) |
| 64 | BKPR_EMP_NUM | INTEGER | 2 | — | Employee number |
| 65 | BKPR_EMP_OAQTD_1 | NUMERIC | 8 | 2 | Other pay type 1 QTD amount |
| 66 | BKPR_EMP_OAQTD_10 | NUMERIC | 8 | 2 | Other pay type 10 QTD amount |
| 67 | BKPR_EMP_OAQTD_11 | NUMERIC | 8 | 2 | Other pay type 11 QTD amount |
| 68 | BKPR_EMP_OAQTD_12 | NUMERIC | 8 | 2 | Other pay type 12 QTD amount |
| 69 | BKPR_EMP_OAQTD_2 | NUMERIC | 8 | 2 | Other pay type 2 QTD amount |
| 70 | BKPR_EMP_OAQTD_3 | NUMERIC | 8 | 2 | Other pay type 3 QTD amount |
| 71 | BKPR_EMP_OAQTD_4 | NUMERIC | 8 | 2 | Other pay type 4 QTD amount |
| 72 | BKPR_EMP_OAQTD_5 | NUMERIC | 8 | 2 | Other pay type 5 QTD amount |
| 73 | BKPR_EMP_OAQTD_6 | NUMERIC | 8 | 2 | Other pay type 6 QTD amount |
| 74 | BKPR_EMP_OAQTD_7 | NUMERIC | 8 | 2 | Other pay type 7 QTD amount |
| 75 | BKPR_EMP_OAQTD_8 | NUMERIC | 8 | 2 | Other pay type 8 QTD amount |
| 76 | BKPR_EMP_OAQTD_9 | NUMERIC | 8 | 2 | Other pay type 9 QTD amount |
| 77 | BKPR_EMP_OAYTD_1 | NUMERIC | 8 | 2 | Other pay type 1 YTD amount |
| 78 | BKPR_EMP_OAYTD_10 | NUMERIC | 8 | 2 | Other pay type 10 YTD amount |
| 79 | BKPR_EMP_OAYTD_11 | NUMERIC | 8 | 2 | Other pay type 11 YTD amount |
| 80 | BKPR_EMP_OAYTD_12 | NUMERIC | 8 | 2 | Other pay type 12 YTD amount |
| 81 | BKPR_EMP_OAYTD_2 | NUMERIC | 8 | 2 | Other pay type 2 YTD amount |
| 82 | BKPR_EMP_OAYTD_3 | NUMERIC | 8 | 2 | Other pay type 3 YTD amount |
| 83 | BKPR_EMP_OAYTD_4 | NUMERIC | 8 | 2 | Other pay type 4 YTD amount |
| 84 | BKPR_EMP_OAYTD_5 | NUMERIC | 8 | 2 | Other pay type 5 YTD amount |
| 85 | BKPR_EMP_OAYTD_6 | NUMERIC | 8 | 2 | Other pay type 6 YTD amount |
| 86 | BKPR_EMP_OAYTD_7 | NUMERIC | 8 | 2 | Other pay type 7 YTD amount |
| 87 | BKPR_EMP_OAYTD_8 | NUMERIC | 8 | 2 | Other pay type 8 YTD amount |
| 88 | BKPR_EMP_OAYTD_9 | NUMERIC | 8 | 2 | Other pay type 9 YTD amount |
| 89 | BKPR_EMP_OHQTD_1 | NUMERIC | 8 | 2 | Other pay type 1 QTD hours |
| 90 | BKPR_EMP_OHQTD_10 | NUMERIC | 8 | 2 | Other pay type 10 QTD hours |
| 91 | BKPR_EMP_OHQTD_11 | NUMERIC | 8 | 2 | Other pay type 11 QTD hours |
| 92 | BKPR_EMP_OHQTD_12 | NUMERIC | 8 | 2 | Other pay type 12 QTD hours |
| 93 | BKPR_EMP_OHQTD_2 | NUMERIC | 8 | 2 | Other pay type 2 QTD hours |
| 94 | BKPR_EMP_OHQTD_3 | NUMERIC | 8 | 2 | Other pay type 3 QTD hours |
| 95 | BKPR_EMP_OHQTD_4 | NUMERIC | 8 | 2 | Other pay type 4 QTD hours |
| 96 | BKPR_EMP_OHQTD_5 | NUMERIC | 8 | 2 | Other pay type 5 QTD hours |
| 97 | BKPR_EMP_OHQTD_6 | NUMERIC | 8 | 2 | Other pay type 6 QTD hours |
| 98 | BKPR_EMP_OHQTD_7 | NUMERIC | 8 | 2 | Other pay type 7 QTD hours |
| 99 | BKPR_EMP_OHQTD_8 | NUMERIC | 8 | 2 | Other pay type 8 QTD hours |
| 100 | BKPR_EMP_OHQTD_9 | NUMERIC | 8 | 2 | Other pay type 9 QTD hours |
| 101 | BKPR_EMP_OHYTD_1 | NUMERIC | 8 | 2 | Other pay type 1 YTD hours |
| 102 | BKPR_EMP_OHYTD_10 | NUMERIC | 8 | 2 | Other pay type 10 YTD hours |
| 103 | BKPR_EMP_OHYTD_11 | NUMERIC | 8 | 2 | Other pay type 11 YTD hours |
| 104 | BKPR_EMP_OHYTD_12 | NUMERIC | 8 | 2 | Other pay type 12 YTD hours |
| 105 | BKPR_EMP_OHYTD_2 | NUMERIC | 8 | 2 | Other pay type 2 YTD hours |
| 106 | BKPR_EMP_OHYTD_3 | NUMERIC | 8 | 2 | Other pay type 3 YTD hours |
| 107 | BKPR_EMP_OHYTD_4 | NUMERIC | 8 | 2 | Other pay type 4 YTD hours |
| 108 | BKPR_EMP_OHYTD_5 | NUMERIC | 8 | 2 | Other pay type 5 YTD hours |
| 109 | BKPR_EMP_OHYTD_6 | NUMERIC | 8 | 2 | Other pay type 6 YTD hours |
| 110 | BKPR_EMP_OHYTD_7 | NUMERIC | 8 | 2 | Other pay type 7 YTD hours |
| 111 | BKPR_EMP_OHYTD_8 | NUMERIC | 8 | 2 | Other pay type 8 YTD hours |
| 112 | BKPR_EMP_OHYTD_9 | NUMERIC | 8 | 2 | Other pay type 9 YTD hours |
| 113 | BKPR_EMP_OPNAME_1 | STRING | 10 | — | Other pay type 1 name |
| 114 | BKPR_EMP_OPNAME_2 | STRING | 10 | — | Other pay type 2 name |
| 115 | BKPR_EMP_OPNAME_3 | STRING | 10 | — | Other pay type 3 name |
| 116 | BKPR_EMP_OPNAME_4 | STRING | 10 | — | Other pay type 4 name |
| 117 | BKPR_EMP_OPNAME_5 | STRING | 10 | — | Other pay type 5 name |
| 118 | BKPR_EMP_OTHACT | STRING | 10 | — | Other deduction GL account |
| 119 | BKPR_EMP_OTHAMT | NUMERIC | 8 | 2 | Other deduction per-period amount |
| 120 | BKPR_EMP_OTHDPT | STRING | 4 | — | Other deduction GL department |
| 121 | BKPR_EMP_OTHNME | STRING | 12 | — | Other deduction name |
| 122 | BKPR_EMP_OTHQTD | NUMERIC | 8 | 2 | Other deduction QTD amount |
| 123 | BKPR_EMP_OTHYTD | NUMERIC | 8 | 2 | Other deduction YTD amount |
| 124 | BKPR_EMP_PAYAMT_1 | NUMERIC | 8 | 4 | Pay rate 1 amount |
| 125 | BKPR_EMP_PAYAMT_10 | NUMERIC | 8 | 4 | Pay rate 10 amount |
| 126 | BKPR_EMP_PAYAMT_11 | NUMERIC | 8 | 4 | Pay rate 11 amount |
| 127 | BKPR_EMP_PAYAMT_12 | NUMERIC | 8 | 4 | Pay rate 12 amount |
| 128 | BKPR_EMP_PAYAMT_13 | NUMERIC | 8 | 4 | Pay rate 13 amount |
| 129 | BKPR_EMP_PAYAMT_14 | NUMERIC | 8 | 4 | Pay rate 14 amount |
| 130 | BKPR_EMP_PAYAMT_15 | NUMERIC | 8 | 4 | Pay rate 15 amount |
| 131 | BKPR_EMP_PAYAMT_2 | NUMERIC | 8 | 4 | Pay rate 2 amount |
| 132 | BKPR_EMP_PAYAMT_3 | NUMERIC | 8 | 4 | Pay rate 3 amount |
| 133 | BKPR_EMP_PAYAMT_4 | NUMERIC | 8 | 4 | Pay rate 4 amount |
| 134 | BKPR_EMP_PAYAMT_5 | NUMERIC | 8 | 4 | Pay rate 5 amount |
| 135 | BKPR_EMP_PAYAMT_6 | NUMERIC | 8 | 4 | Pay rate 6 amount |
| 136 | BKPR_EMP_PAYAMT_7 | NUMERIC | 8 | 4 | Pay rate 7 amount |
| 137 | BKPR_EMP_PAYAMT_8 | NUMERIC | 8 | 4 | Pay rate 8 amount |
| 138 | BKPR_EMP_PAYAMT_9 | NUMERIC | 8 | 4 | Pay rate 9 amount |
| 139 | BKPR_EMP_PAYTYP | STRING | 1 | — | Pay type (H=Hourly, S=Salary) |
| 140 | BKPR_EMP_PHONE | STRING | 15 | — | Employee phone number |
| 141 | BKPR_EMP_QTR | INTEGER | 2 | — | Current quarter number (1-4) |
| 142 | BKPR_EMP_RAQTD | NUMERIC | 8 | 2 | Regular pay QTD amount |
| 143 | BKPR_EMP_RAYTD | NUMERIC | 8 | 2 | Regular pay YTD amount |
| 144 | BKPR_EMP_RHQTD | NUMERIC | 8 | 2 | Regular pay QTD hours |
| 145 | BKPR_EMP_RHYTD | NUMERIC | 8 | 2 | Regular pay YTD hours |
| 146 | BKPR_EMP_SAQTD | NUMERIC | 8 | 2 | Special pay QTD amount |
| 147 | BKPR_EMP_SAYTD | NUMERIC | 8 | 2 | Special pay YTD amount |
| 148 | BKPR_EMP_SCAP | NUMERIC | 8 | 2 | Salary cap amount |
| 149 | BKPR_EMP_SDATE | DATE | 4 | — | Employee start/hire date |
| 150 | BKPR_EMP_SDIEXM | STRING | 1 | — | SDI exempt flag (Y/N) |
| 151 | BKPR_EMP_SDIQTD | NUMERIC | 8 | 2 | SDI withheld QTD |
| 152 | BKPR_EMP_SDIYTD | NUMERIC | 8 | 2 | SDI withheld YTD |
| 153 | BKPR_EMP_SDUE | NUMERIC | 8 | 2 | Salary due/accrued amount |
| 154 | BKPR_EMP_SHIFT | INTEGER | 2 | — | Default shift number |
| 155 | BKPR_EMP_SHQTD | NUMERIC | 8 | 2 | Special pay QTD hours |
| 156 | BKPR_EMP_SHYTD | NUMERIC | 8 | 2 | Special pay YTD hours |
| 157 | BKPR_EMP_SRTE | NUMERIC | 8 | 4 | Salary pay rate |
| 158 | BKPR_EMP_SSN | STRING | 11 | — | Social security number (XXX-XX-XXXX) |
| 159 | BKPR_EMP_ST | STRING | 2 | — | State code for tax withholding |
| 160 | BKPR_EMP_STEXM | INTEGER | 2 | — | Number of state withholding exemptions |
| 161 | BKPR_EMP_STEXMA | NUMERIC | 8 | — | State exemption additional amount |
| 162 | BKPR_EMP_STEXMN | INTEGER | 2 | — | Number of additional state exemptions |
| 163 | BKPR_EMP_STQTD | NUMERIC | 8 | 2 | State income tax withheld QTD |
| 164 | BKPR_EMP_STYTD | NUMERIC | 8 | 2 | State income tax withheld YTD |
| 165 | BKPR_EMP_TERM | STRING | 1 | — | Terminated flag (Y/N) |
| 166 | BKPR_EMP_UDAMT1_1 | NUMERIC | 8 | 2 | User deduction (type 1) slot 1 amount |
| 167 | BKPR_EMP_UDAMT1_2 | NUMERIC | 8 | 2 | User deduction (type 1) slot 2 amount |
| 168 | BKPR_EMP_UDAMT1_3 | NUMERIC | 8 | 2 | User deduction (type 1) slot 3 amount |
| 169 | BKPR_EMP_UDAMT1_4 | NUMERIC | 8 | 2 | User deduction (type 1) slot 4 amount |
| 170 | BKPR_EMP_UDAMT1_5 | NUMERIC | 8 | 2 | User deduction (type 1) slot 5 amount |
| 171 | BKPR_EMP_UDAMT1_6 | NUMERIC | 8 | 2 | User deduction (type 1) slot 6 amount |
| 172 | BKPR_EMP_UDEAMT_1 | NUMERIC | 8 | 4 | User other deduction 1 employee per-period amount |
| 173 | BKPR_EMP_UDEAMT_10 | NUMERIC | 8 | 4 | User other deduction 10 employee per-period amount |
| 174 | BKPR_EMP_UDEAMT_11 | NUMERIC | 8 | 4 | User other deduction 11 employee per-period amount |
| 175 | BKPR_EMP_UDEAMT_12 | NUMERIC | 8 | 4 | User other deduction 12 employee per-period amount |
| 176 | BKPR_EMP_UDEAMT_13 | NUMERIC | 8 | 4 | User other deduction 13 employee per-period amount |
| 177 | BKPR_EMP_UDEAMT_14 | NUMERIC | 8 | 4 | User other deduction 14 employee per-period amount |
| 178 | BKPR_EMP_UDEAMT_15 | NUMERIC | 8 | 4 | User other deduction 15 employee per-period amount |
| 179 | BKPR_EMP_UDEAMT_16 | NUMERIC | 8 | 4 | User other deduction 16 employee per-period amount |
| 180 | BKPR_EMP_UDEAMT_17 | NUMERIC | 8 | 4 | User other deduction 17 employee per-period amount |
| 181 | BKPR_EMP_UDEAMT_18 | NUMERIC | 8 | 4 | User other deduction 18 employee per-period amount |
| 182 | BKPR_EMP_UDEAMT_19 | NUMERIC | 8 | 4 | User other deduction 19 employee per-period amount |
| 183 | BKPR_EMP_UDEAMT_2 | NUMERIC | 8 | 4 | User other deduction 2 employee per-period amount |
| 184 | BKPR_EMP_UDEAMT_20 | NUMERIC | 8 | 4 | User other deduction 20 employee per-period amount |
| 185 | BKPR_EMP_UDEAMT_3 | NUMERIC | 8 | 4 | User other deduction 3 employee per-period amount |
| 186 | BKPR_EMP_UDEAMT_4 | NUMERIC | 8 | 4 | User other deduction 4 employee per-period amount |
| 187 | BKPR_EMP_UDEAMT_5 | NUMERIC | 8 | 4 | User other deduction 5 employee per-period amount |
| 188 | BKPR_EMP_UDEAMT_6 | NUMERIC | 8 | 4 | User other deduction 6 employee per-period amount |
| 189 | BKPR_EMP_UDEAMT_7 | NUMERIC | 8 | 4 | User other deduction 7 employee per-period amount |
| 190 | BKPR_EMP_UDEAMT_8 | NUMERIC | 8 | 4 | User other deduction 8 employee per-period amount |
| 191 | BKPR_EMP_UDEAMT_9 | NUMERIC | 8 | 4 | User other deduction 9 employee per-period amount |
| 192 | BKPR_EMP_UDELMT_1 | NUMERIC | 8 | 4 | User other deduction 1 employee per-period limit |
| 193 | BKPR_EMP_UDELMT_10 | NUMERIC | 8 | 4 | User other deduction 10 employee per-period limit |
| 194 | BKPR_EMP_UDELMT_11 | NUMERIC | 8 | 4 | User other deduction 11 employee per-period limit |
| 195 | BKPR_EMP_UDELMT_12 | NUMERIC | 8 | 4 | User other deduction 12 employee per-period limit |
| 196 | BKPR_EMP_UDELMT_13 | NUMERIC | 8 | 4 | User other deduction 13 employee per-period limit |
| 197 | BKPR_EMP_UDELMT_14 | NUMERIC | 8 | 4 | User other deduction 14 employee per-period limit |
| 198 | BKPR_EMP_UDELMT_15 | NUMERIC | 8 | 4 | User other deduction 15 employee per-period limit |
| 199 | BKPR_EMP_UDELMT_16 | NUMERIC | 8 | 4 | User other deduction 16 employee per-period limit |
| 200 | BKPR_EMP_UDELMT_17 | NUMERIC | 8 | 4 | User other deduction 17 employee per-period limit |
| 201 | BKPR_EMP_UDELMT_18 | NUMERIC | 8 | 4 | User other deduction 18 employee per-period limit |
| 202 | BKPR_EMP_UDELMT_19 | NUMERIC | 8 | 4 | User other deduction 19 employee per-period limit |
| 203 | BKPR_EMP_UDELMT_2 | NUMERIC | 8 | 4 | User other deduction 2 employee per-period limit |
| 204 | BKPR_EMP_UDELMT_20 | NUMERIC | 8 | 4 | User other deduction 20 employee per-period limit |
| 205 | BKPR_EMP_UDELMT_3 | NUMERIC | 8 | 4 | User other deduction 3 employee per-period limit |
| 206 | BKPR_EMP_UDELMT_4 | NUMERIC | 8 | 4 | User other deduction 4 employee per-period limit |
| 207 | BKPR_EMP_UDELMT_5 | NUMERIC | 8 | 4 | User other deduction 5 employee per-period limit |
| 208 | BKPR_EMP_UDELMT_6 | NUMERIC | 8 | 4 | User other deduction 6 employee per-period limit |
| 209 | BKPR_EMP_UDELMT_7 | NUMERIC | 8 | 4 | User other deduction 7 employee per-period limit |
| 210 | BKPR_EMP_UDELMT_8 | NUMERIC | 8 | 4 | User other deduction 8 employee per-period limit |
| 211 | BKPR_EMP_UDELMT_9 | NUMERIC | 8 | 4 | User other deduction 9 employee per-period limit |
| 212 | BKPR_EMP_UDEQTD_1 | NUMERIC | 8 | 2 | User other deduction 1 employee QTD amount |
| 213 | BKPR_EMP_UDEQTD_10 | NUMERIC | 8 | 2 | User other deduction 10 employee QTD amount |
| 214 | BKPR_EMP_UDEQTD_11 | NUMERIC | 8 | 2 | User other deduction 11 employee QTD amount |
| 215 | BKPR_EMP_UDEQTD_12 | NUMERIC | 8 | 2 | User other deduction 12 employee QTD amount |
| 216 | BKPR_EMP_UDEQTD_13 | NUMERIC | 8 | 2 | User other deduction 13 employee QTD amount |
| 217 | BKPR_EMP_UDEQTD_14 | NUMERIC | 8 | 2 | User other deduction 14 employee QTD amount |
| 218 | BKPR_EMP_UDEQTD_15 | NUMERIC | 8 | 2 | User other deduction 15 employee QTD amount |
| 219 | BKPR_EMP_UDEQTD_16 | NUMERIC | 8 | 2 | User other deduction 16 employee QTD amount |
| 220 | BKPR_EMP_UDEQTD_17 | NUMERIC | 8 | 2 | User other deduction 17 employee QTD amount |
| 221 | BKPR_EMP_UDEQTD_18 | NUMERIC | 8 | 2 | User other deduction 18 employee QTD amount |
| 222 | BKPR_EMP_UDEQTD_19 | NUMERIC | 8 | 2 | User other deduction 19 employee QTD amount |
| 223 | BKPR_EMP_UDEQTD_2 | NUMERIC | 8 | 2 | User other deduction 2 employee QTD amount |
| 224 | BKPR_EMP_UDEQTD_20 | NUMERIC | 8 | 2 | User other deduction 20 employee QTD amount |
| 225 | BKPR_EMP_UDEQTD_3 | NUMERIC | 8 | 2 | User other deduction 3 employee QTD amount |
| 226 | BKPR_EMP_UDEQTD_4 | NUMERIC | 8 | 2 | User other deduction 4 employee QTD amount |
| 227 | BKPR_EMP_UDEQTD_5 | NUMERIC | 8 | 2 | User other deduction 5 employee QTD amount |
| 228 | BKPR_EMP_UDEQTD_6 | NUMERIC | 8 | 2 | User other deduction 6 employee QTD amount |
| 229 | BKPR_EMP_UDEQTD_7 | NUMERIC | 8 | 2 | User other deduction 7 employee QTD amount |
| 230 | BKPR_EMP_UDEQTD_8 | NUMERIC | 8 | 2 | User other deduction 8 employee QTD amount |
| 231 | BKPR_EMP_UDEQTD_9 | NUMERIC | 8 | 2 | User other deduction 9 employee QTD amount |
| 232 | BKPR_EMP_UDEYLM_1 | NUMERIC | 8 | 2 | User other deduction 1 employee annual limit |
| 233 | BKPR_EMP_UDEYLM_10 | NUMERIC | 8 | 2 | User other deduction 10 employee annual limit |
| 234 | BKPR_EMP_UDEYLM_11 | NUMERIC | 8 | 2 | User other deduction 11 employee annual limit |
| 235 | BKPR_EMP_UDEYLM_12 | NUMERIC | 8 | 2 | User other deduction 12 employee annual limit |
| 236 | BKPR_EMP_UDEYLM_13 | NUMERIC | 8 | 2 | User other deduction 13 employee annual limit |
| 237 | BKPR_EMP_UDEYLM_14 | NUMERIC | 8 | 2 | User other deduction 14 employee annual limit |
| 238 | BKPR_EMP_UDEYLM_15 | NUMERIC | 8 | 2 | User other deduction 15 employee annual limit |
| 239 | BKPR_EMP_UDEYLM_16 | NUMERIC | 8 | 2 | User other deduction 16 employee annual limit |
| 240 | BKPR_EMP_UDEYLM_17 | NUMERIC | 8 | 2 | User other deduction 17 employee annual limit |
| 241 | BKPR_EMP_UDEYLM_18 | NUMERIC | 8 | 2 | User other deduction 18 employee annual limit |
| 242 | BKPR_EMP_UDEYLM_19 | NUMERIC | 8 | 2 | User other deduction 19 employee annual limit |
| 243 | BKPR_EMP_UDEYLM_2 | NUMERIC | 8 | 2 | User other deduction 2 employee annual limit |
| 244 | BKPR_EMP_UDEYLM_20 | NUMERIC | 8 | 2 | User other deduction 20 employee annual limit |
| 245 | BKPR_EMP_UDEYLM_3 | NUMERIC | 8 | 2 | User other deduction 3 employee annual limit |
| 246 | BKPR_EMP_UDEYLM_4 | NUMERIC | 8 | 2 | User other deduction 4 employee annual limit |
| 247 | BKPR_EMP_UDEYLM_5 | NUMERIC | 8 | 2 | User other deduction 5 employee annual limit |
| 248 | BKPR_EMP_UDEYLM_6 | NUMERIC | 8 | 2 | User other deduction 6 employee annual limit |
| 249 | BKPR_EMP_UDEYLM_7 | NUMERIC | 8 | 2 | User other deduction 7 employee annual limit |
| 250 | BKPR_EMP_UDEYLM_8 | NUMERIC | 8 | 2 | User other deduction 8 employee annual limit |
| 251 | BKPR_EMP_UDEYLM_9 | NUMERIC | 8 | 2 | User other deduction 9 employee annual limit |
| 252 | BKPR_EMP_UDEYTD_1 | NUMERIC | 8 | 2 | User other deduction 1 employee YTD amount |
| 253 | BKPR_EMP_UDEYTD_10 | NUMERIC | 8 | 2 | User other deduction 10 employee YTD amount |
| 254 | BKPR_EMP_UDEYTD_11 | NUMERIC | 8 | 2 | User other deduction 11 employee YTD amount |
| 255 | BKPR_EMP_UDEYTD_12 | NUMERIC | 8 | 2 | User other deduction 12 employee YTD amount |
| 256 | BKPR_EMP_UDEYTD_13 | NUMERIC | 8 | 2 | User other deduction 13 employee YTD amount |
| 257 | BKPR_EMP_UDEYTD_14 | NUMERIC | 8 | 2 | User other deduction 14 employee YTD amount |
| 258 | BKPR_EMP_UDEYTD_15 | NUMERIC | 8 | 2 | User other deduction 15 employee YTD amount |
| 259 | BKPR_EMP_UDEYTD_16 | NUMERIC | 8 | 2 | User other deduction 16 employee YTD amount |
| 260 | BKPR_EMP_UDEYTD_17 | NUMERIC | 8 | 2 | User other deduction 17 employee YTD amount |
| 261 | BKPR_EMP_UDEYTD_18 | NUMERIC | 8 | 2 | User other deduction 18 employee YTD amount |
| 262 | BKPR_EMP_UDEYTD_19 | NUMERIC | 8 | 2 | User other deduction 19 employee YTD amount |
| 263 | BKPR_EMP_UDEYTD_2 | NUMERIC | 8 | 2 | User other deduction 2 employee YTD amount |
| 264 | BKPR_EMP_UDEYTD_20 | NUMERIC | 8 | 2 | User other deduction 20 employee YTD amount |
| 265 | BKPR_EMP_UDEYTD_3 | NUMERIC | 8 | 2 | User other deduction 3 employee YTD amount |
| 266 | BKPR_EMP_UDEYTD_4 | NUMERIC | 8 | 2 | User other deduction 4 employee YTD amount |
| 267 | BKPR_EMP_UDEYTD_5 | NUMERIC | 8 | 2 | User other deduction 5 employee YTD amount |
| 268 | BKPR_EMP_UDEYTD_6 | NUMERIC | 8 | 2 | User other deduction 6 employee YTD amount |
| 269 | BKPR_EMP_UDEYTD_7 | NUMERIC | 8 | 2 | User other deduction 7 employee YTD amount |
| 270 | BKPR_EMP_UDEYTD_8 | NUMERIC | 8 | 2 | User other deduction 8 employee YTD amount |
| 271 | BKPR_EMP_UDEYTD_9 | NUMERIC | 8 | 2 | User other deduction 9 employee YTD amount |
| 272 | BKPR_EMP_UODAMT_1 | NUMERIC | 8 | 4 | User other deduction 1 per-period amount |
| 273 | BKPR_EMP_UODAMT_10 | NUMERIC | 8 | 4 | User other deduction 10 per-period amount |
| 274 | BKPR_EMP_UODAMT_11 | NUMERIC | 8 | 4 | User other deduction 11 per-period amount |
| 275 | BKPR_EMP_UODAMT_12 | NUMERIC | 8 | 4 | User other deduction 12 per-period amount |
| 276 | BKPR_EMP_UODAMT_13 | NUMERIC | 8 | 4 | User other deduction 13 per-period amount |
| 277 | BKPR_EMP_UODAMT_14 | NUMERIC | 8 | 4 | User other deduction 14 per-period amount |
| 278 | BKPR_EMP_UODAMT_15 | NUMERIC | 8 | 4 | User other deduction 15 per-period amount |
| 279 | BKPR_EMP_UODAMT_16 | NUMERIC | 8 | 4 | User other deduction 16 per-period amount |
| 280 | BKPR_EMP_UODAMT_17 | NUMERIC | 8 | 4 | User other deduction 17 per-period amount |
| 281 | BKPR_EMP_UODAMT_18 | NUMERIC | 8 | 4 | User other deduction 18 per-period amount |
| 282 | BKPR_EMP_UODAMT_19 | NUMERIC | 8 | 4 | User other deduction 19 per-period amount |
| 283 | BKPR_EMP_UODAMT_2 | NUMERIC | 8 | 4 | User other deduction 2 per-period amount |
| 284 | BKPR_EMP_UODAMT_20 | NUMERIC | 8 | 4 | User other deduction 20 per-period amount |
| 285 | BKPR_EMP_UODAMT_3 | NUMERIC | 8 | 4 | User other deduction 3 per-period amount |
| 286 | BKPR_EMP_UODAMT_4 | NUMERIC | 8 | 4 | User other deduction 4 per-period amount |
| 287 | BKPR_EMP_UODAMT_5 | NUMERIC | 8 | 4 | User other deduction 5 per-period amount |
| 288 | BKPR_EMP_UODAMT_6 | NUMERIC | 8 | 4 | User other deduction 6 per-period amount |
| 289 | BKPR_EMP_UODAMT_7 | NUMERIC | 8 | 4 | User other deduction 7 per-period amount |
| 290 | BKPR_EMP_UODAMT_8 | NUMERIC | 8 | 4 | User other deduction 8 per-period amount |
| 291 | BKPR_EMP_UODAMT_9 | NUMERIC | 8 | 4 | User other deduction 9 per-period amount |
| 292 | BKPR_EMP_UODLMT_1 | NUMERIC | 8 | 4 | User other deduction 1 per-period limit |
| 293 | BKPR_EMP_UODLMT_10 | NUMERIC | 8 | 4 | User other deduction 10 per-period limit |
| 294 | BKPR_EMP_UODLMT_11 | NUMERIC | 8 | 4 | User other deduction 11 per-period limit |
| 295 | BKPR_EMP_UODLMT_12 | NUMERIC | 8 | 4 | User other deduction 12 per-period limit |
| 296 | BKPR_EMP_UODLMT_13 | NUMERIC | 8 | 4 | User other deduction 13 per-period limit |
| 297 | BKPR_EMP_UODLMT_14 | NUMERIC | 8 | 4 | User other deduction 14 per-period limit |
| 298 | BKPR_EMP_UODLMT_15 | NUMERIC | 8 | 4 | User other deduction 15 per-period limit |
| 299 | BKPR_EMP_UODLMT_16 | NUMERIC | 8 | 4 | User other deduction 16 per-period limit |
| 300 | BKPR_EMP_UODLMT_17 | NUMERIC | 8 | 4 | User other deduction 17 per-period limit |
| 301 | BKPR_EMP_UODLMT_18 | NUMERIC | 8 | 4 | User other deduction 18 per-period limit |
| 302 | BKPR_EMP_UODLMT_19 | NUMERIC | 8 | 4 | User other deduction 19 per-period limit |
| 303 | BKPR_EMP_UODLMT_2 | NUMERIC | 8 | 4 | User other deduction 2 per-period limit |
| 304 | BKPR_EMP_UODLMT_20 | NUMERIC | 8 | 4 | User other deduction 20 per-period limit |
| 305 | BKPR_EMP_UODLMT_3 | NUMERIC | 8 | 4 | User other deduction 3 per-period limit |
| 306 | BKPR_EMP_UODLMT_4 | NUMERIC | 8 | 4 | User other deduction 4 per-period limit |
| 307 | BKPR_EMP_UODLMT_5 | NUMERIC | 8 | 4 | User other deduction 5 per-period limit |
| 308 | BKPR_EMP_UODLMT_6 | NUMERIC | 8 | 4 | User other deduction 6 per-period limit |
| 309 | BKPR_EMP_UODLMT_7 | NUMERIC | 8 | 4 | User other deduction 7 per-period limit |
| 310 | BKPR_EMP_UODLMT_8 | NUMERIC | 8 | 4 | User other deduction 8 per-period limit |
| 311 | BKPR_EMP_UODLMT_9 | NUMERIC | 8 | 4 | User other deduction 9 per-period limit |
| 312 | BKPR_EMP_UODQTD_1 | NUMERIC | 8 | 2 | User other deduction 1 QTD amount |
| 313 | BKPR_EMP_UODQTD_10 | NUMERIC | 8 | 2 | User other deduction 10 QTD amount |
| 314 | BKPR_EMP_UODQTD_11 | NUMERIC | 8 | 2 | User other deduction 11 QTD amount |
| 315 | BKPR_EMP_UODQTD_12 | NUMERIC | 8 | 2 | User other deduction 12 QTD amount |
| 316 | BKPR_EMP_UODQTD_13 | NUMERIC | 8 | 2 | User other deduction 13 QTD amount |
| 317 | BKPR_EMP_UODQTD_14 | NUMERIC | 8 | 2 | User other deduction 14 QTD amount |
| 318 | BKPR_EMP_UODQTD_15 | NUMERIC | 8 | 2 | User other deduction 15 QTD amount |
| 319 | BKPR_EMP_UODQTD_16 | NUMERIC | 8 | 2 | User other deduction 16 QTD amount |
| 320 | BKPR_EMP_UODQTD_17 | NUMERIC | 8 | 2 | User other deduction 17 QTD amount |
| 321 | BKPR_EMP_UODQTD_18 | NUMERIC | 8 | 2 | User other deduction 18 QTD amount |
| 322 | BKPR_EMP_UODQTD_19 | NUMERIC | 8 | 2 | User other deduction 19 QTD amount |
| 323 | BKPR_EMP_UODQTD_2 | NUMERIC | 8 | 2 | User other deduction 2 QTD amount |
| 324 | BKPR_EMP_UODQTD_20 | NUMERIC | 8 | 2 | User other deduction 20 QTD amount |
| 325 | BKPR_EMP_UODQTD_3 | NUMERIC | 8 | 2 | User other deduction 3 QTD amount |
| 326 | BKPR_EMP_UODQTD_4 | NUMERIC | 8 | 2 | User other deduction 4 QTD amount |
| 327 | BKPR_EMP_UODQTD_5 | NUMERIC | 8 | 2 | User other deduction 5 QTD amount |
| 328 | BKPR_EMP_UODQTD_6 | NUMERIC | 8 | 2 | User other deduction 6 QTD amount |
| 329 | BKPR_EMP_UODQTD_7 | NUMERIC | 8 | 2 | User other deduction 7 QTD amount |
| 330 | BKPR_EMP_UODQTD_8 | NUMERIC | 8 | 2 | User other deduction 8 QTD amount |
| 331 | BKPR_EMP_UODQTD_9 | NUMERIC | 8 | 2 | User other deduction 9 QTD amount |
| 332 | BKPR_EMP_UODYLM_1 | NUMERIC | 8 | 2 | User other deduction 1 annual limit |
| 333 | BKPR_EMP_UODYLM_10 | NUMERIC | 8 | 2 | User other deduction 10 annual limit |
| 334 | BKPR_EMP_UODYLM_11 | NUMERIC | 8 | 2 | User other deduction 11 annual limit |
| 335 | BKPR_EMP_UODYLM_12 | NUMERIC | 8 | 2 | User other deduction 12 annual limit |
| 336 | BKPR_EMP_UODYLM_13 | NUMERIC | 8 | 2 | User other deduction 13 annual limit |
| 337 | BKPR_EMP_UODYLM_14 | NUMERIC | 8 | 2 | User other deduction 14 annual limit |
| 338 | BKPR_EMP_UODYLM_15 | NUMERIC | 8 | 2 | User other deduction 15 annual limit |
| 339 | BKPR_EMP_UODYLM_16 | NUMERIC | 8 | 2 | User other deduction 16 annual limit |
| 340 | BKPR_EMP_UODYLM_17 | NUMERIC | 8 | 2 | User other deduction 17 annual limit |
| 341 | BKPR_EMP_UODYLM_18 | NUMERIC | 8 | 2 | User other deduction 18 annual limit |
| 342 | BKPR_EMP_UODYLM_19 | NUMERIC | 8 | 2 | User other deduction 19 annual limit |
| 343 | BKPR_EMP_UODYLM_2 | NUMERIC | 8 | 2 | User other deduction 2 annual limit |
| 344 | BKPR_EMP_UODYLM_20 | NUMERIC | 8 | 2 | User other deduction 20 annual limit |
| 345 | BKPR_EMP_UODYLM_3 | NUMERIC | 8 | 2 | User other deduction 3 annual limit |
| 346 | BKPR_EMP_UODYLM_4 | NUMERIC | 8 | 2 | User other deduction 4 annual limit |
| 347 | BKPR_EMP_UODYLM_5 | NUMERIC | 8 | 2 | User other deduction 5 annual limit |
| 348 | BKPR_EMP_UODYLM_6 | NUMERIC | 8 | 2 | User other deduction 6 annual limit |
| 349 | BKPR_EMP_UODYLM_7 | NUMERIC | 8 | 2 | User other deduction 7 annual limit |
| 350 | BKPR_EMP_UODYLM_8 | NUMERIC | 8 | 2 | User other deduction 8 annual limit |
| 351 | BKPR_EMP_UODYLM_9 | NUMERIC | 8 | 2 | User other deduction 9 annual limit |
| 352 | BKPR_EMP_UODYTD_1 | NUMERIC | 8 | 2 | User other deduction 1 YTD amount |
| 353 | BKPR_EMP_UODYTD_10 | NUMERIC | 8 | 2 | User other deduction 10 YTD amount |
| 354 | BKPR_EMP_UODYTD_11 | NUMERIC | 8 | 2 | User other deduction 11 YTD amount |
| 355 | BKPR_EMP_UODYTD_12 | NUMERIC | 8 | 2 | User other deduction 12 YTD amount |
| 356 | BKPR_EMP_UODYTD_13 | NUMERIC | 8 | 2 | User other deduction 13 YTD amount |
| 357 | BKPR_EMP_UODYTD_14 | NUMERIC | 8 | 2 | User other deduction 14 YTD amount |
| 358 | BKPR_EMP_UODYTD_15 | NUMERIC | 8 | 2 | User other deduction 15 YTD amount |
| 359 | BKPR_EMP_UODYTD_16 | NUMERIC | 8 | 2 | User other deduction 16 YTD amount |
| 360 | BKPR_EMP_UODYTD_17 | NUMERIC | 8 | 2 | User other deduction 17 YTD amount |
| 361 | BKPR_EMP_UODYTD_18 | NUMERIC | 8 | 2 | User other deduction 18 YTD amount |
| 362 | BKPR_EMP_UODYTD_19 | NUMERIC | 8 | 2 | User other deduction 19 YTD amount |
| 363 | BKPR_EMP_UODYTD_2 | NUMERIC | 8 | 2 | User other deduction 2 YTD amount |
| 364 | BKPR_EMP_UODYTD_20 | NUMERIC | 8 | 2 | User other deduction 20 YTD amount |
| 365 | BKPR_EMP_UODYTD_3 | NUMERIC | 8 | 2 | User other deduction 3 YTD amount |
| 366 | BKPR_EMP_UODYTD_4 | NUMERIC | 8 | 2 | User other deduction 4 YTD amount |
| 367 | BKPR_EMP_UODYTD_5 | NUMERIC | 8 | 2 | User other deduction 5 YTD amount |
| 368 | BKPR_EMP_UODYTD_6 | NUMERIC | 8 | 2 | User other deduction 6 YTD amount |
| 369 | BKPR_EMP_UODYTD_7 | NUMERIC | 8 | 2 | User other deduction 7 YTD amount |
| 370 | BKPR_EMP_UODYTD_8 | NUMERIC | 8 | 2 | User other deduction 8 YTD amount |
| 371 | BKPR_EMP_UODYTD_9 | NUMERIC | 8 | 2 | User other deduction 9 YTD amount |
| 372 | BKPR_EMP_VAQTD | NUMERIC | 8 | 2 | Vacation pay QTD amount |
| 373 | BKPR_EMP_VAYTD | NUMERIC | 8 | 2 | Vacation pay YTD amount |
| 374 | BKPR_EMP_VCAP | NUMERIC | 8 | 2 | Vacation time cap (maximum accrual) |
| 375 | BKPR_EMP_VDUE | NUMERIC | 8 | 2 | Vacation time due/accrued balance |
| 376 | BKPR_EMP_VHQTD | NUMERIC | 8 | 2 | Vacation pay QTD hours |
| 377 | BKPR_EMP_VHYTD | NUMERIC | 8 | 2 | Vacation pay YTD hours |
| 378 | BKPR_EMP_VRTE | NUMERIC | 8 | 4 | Vacation pay rate |
| 379 | BKPR_EMP_WCEE | NUMERIC | 8 | 4 | Workers comp employee rate |
| 380 | BKPR_EMP_WCER | NUMERIC | 8 | 4 | Workers comp employer rate |
| 381 | BKPR_EMP_WKQTD | NUMERIC | 8 | 2 | Total weeks worked QTD |
| 382 | BKPR_EMP_WKYTD | NUMERIC | 8 | 2 | Total weeks worked YTD |
| 383 | BKPR_EMP_YEAR | NUMERIC | 8 | — | Calendar year for this W2/payroll record |
| 384 | BKPR_EMP_ZIP | STRING | 10 | — | Employee ZIP code |

## ISPRMSTR
**PAYROLL EMPLOYEE MASTER**

Fields: 384

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKPR_EMP_ADD | STRING | 30 | — | Employee street address |
| 2 | BKPR_EMP_ADDIT_1 | NUMERIC | 8 | 2 | Additional withholding amount 1 |
| 3 | BKPR_EMP_ADDIT_2 | NUMERIC | 8 | 2 | Additional withholding amount 2 |
| 4 | BKPR_EMP_ADDIT_3 | NUMERIC | 8 | 2 | Additional withholding amount 3 |
| 5 | BKPR_EMP_BANKA | STRING | 17 | — | Bank account number for direct deposit |
| 6 | BKPR_EMP_BANKR | STRING | 9 | — | Bank routing number for direct deposit |
| 7 | BKPR_EMP_BDAY | DATE | 4 | — | Employee birth date |
| 8 | BKPR_EMP_BENDTE | DATE | 4 | — | Benefits effective date |
| 9 | BKPR_EMP_CNTRY | STRING | 30 | — | Employee country |
| 10 | BKPR_EMP_CSZ | STRING | 25 | — | Employee city, state, and zip |
| 11 | BKPR_EMP_DEPT | STRING | 4 | — | Employee department code |
| 12 | BKPR_EMP_EIC | NUMERIC | 8 | 2 | Earned income credit advance per period |
| 13 | BKPR_EMP_EICAMT | NUMERIC | 8 | 2 | Total EIC paid to date |
| 14 | BKPR_EMP_EMAIL | STRING | 128 | — | Employee email address |
| 15 | BKPR_EMP_EXPACT_1 | STRING | 10 | — | Employee expense GL account 1 |
| 16 | BKPR_EMP_EXPACT_10 | STRING | 10 | — | Employee expense GL account 10 |
| 17 | BKPR_EMP_EXPACT_11 | STRING | 10 | — | Employee expense GL account 11 |
| 18 | BKPR_EMP_EXPACT_12 | STRING | 10 | — | Employee expense GL account 12 |
| 19 | BKPR_EMP_EXPACT_13 | STRING | 10 | — | Employee expense GL account 13 |
| 20 | BKPR_EMP_EXPACT_14 | STRING | 10 | — | Employee expense GL account 14 |
| 21 | BKPR_EMP_EXPACT_15 | STRING | 10 | — | Employee expense GL account 15 |
| 22 | BKPR_EMP_EXPACT_2 | STRING | 10 | — | Employee expense GL account 2 |
| 23 | BKPR_EMP_EXPACT_3 | STRING | 10 | — | Employee expense GL account 3 |
| 24 | BKPR_EMP_EXPACT_4 | STRING | 10 | — | Employee expense GL account 4 |
| 25 | BKPR_EMP_EXPACT_5 | STRING | 10 | — | Employee expense GL account 5 |
| 26 | BKPR_EMP_EXPACT_6 | STRING | 10 | — | Employee expense GL account 6 |
| 27 | BKPR_EMP_EXPACT_7 | STRING | 10 | — | Employee expense GL account 7 |
| 28 | BKPR_EMP_EXPACT_8 | STRING | 10 | — | Employee expense GL account 8 |
| 29 | BKPR_EMP_EXPACT_9 | STRING | 10 | — | Employee expense GL account 9 |
| 30 | BKPR_EMP_EXPDPT_1 | STRING | 4 | — | Employee expense GL department 1 |
| 31 | BKPR_EMP_EXPDPT_10 | STRING | 4 | — | Employee expense GL department 10 |
| 32 | BKPR_EMP_EXPDPT_11 | STRING | 4 | — | Employee expense GL department 11 |
| 33 | BKPR_EMP_EXPDPT_12 | STRING | 4 | — | Employee expense GL department 12 |
| 34 | BKPR_EMP_EXPDPT_13 | STRING | 4 | — | Employee expense GL department 13 |
| 35 | BKPR_EMP_EXPDPT_14 | STRING | 4 | — | Employee expense GL department 14 |
| 36 | BKPR_EMP_EXPDPT_15 | STRING | 4 | — | Employee expense GL department 15 |
| 37 | BKPR_EMP_EXPDPT_2 | STRING | 4 | — | Employee expense GL department 2 |
| 38 | BKPR_EMP_EXPDPT_3 | STRING | 4 | — | Employee expense GL department 3 |
| 39 | BKPR_EMP_EXPDPT_4 | STRING | 4 | — | Employee expense GL department 4 |
| 40 | BKPR_EMP_EXPDPT_5 | STRING | 4 | — | Employee expense GL department 5 |
| 41 | BKPR_EMP_EXPDPT_6 | STRING | 4 | — | Employee expense GL department 6 |
| 42 | BKPR_EMP_EXPDPT_7 | STRING | 4 | — | Employee expense GL department 7 |
| 43 | BKPR_EMP_EXPDPT_8 | STRING | 4 | — | Employee expense GL department 8 |
| 44 | BKPR_EMP_EXPDPT_9 | STRING | 4 | — | Employee expense GL department 9 |
| 45 | BKPR_EMP_EXTRA | STRING | 200 | — | Reserved extra field |
| 46 | BKPR_EMP_FEDEXM | INTEGER | 2 | — | Number of federal withholding exemptions |
| 47 | BKPR_EMP_FICQTD_1 | NUMERIC | 8 | 2 | FICA QTD (1=SS, 2=Medicare) |
| 48 | BKPR_EMP_FICQTD_2 | NUMERIC | 8 | 2 | FICA QTD (1=SS, 2=Medicare) |
| 49 | BKPR_EMP_FICYTD_1 | NUMERIC | 8 | 2 | FICA YTD (1=SS, 2=Medicare) |
| 50 | BKPR_EMP_FICYTD_2 | NUMERIC | 8 | 2 | FICA YTD (1=SS, 2=Medicare) |
| 51 | BKPR_EMP_FITQTD | NUMERIC | 8 | 2 | Federal income tax withheld QTD |
| 52 | BKPR_EMP_FITYTD | NUMERIC | 8 | 2 | Federal income tax withheld YTD |
| 53 | BKPR_EMP_FNMI | STRING | 25 | — | Employee first name and middle initial |
| 54 | BKPR_EMP_LNME | STRING | 25 | — | Employee last name |
| 55 | BKPR_EMP_LOCCOD | STRING | 2 | — | Local tax code |
| 56 | BKPR_EMP_LSTPR | DATE | 4 | — | Last payroll date |
| 57 | BKPR_EMP_MDACT | STRING | 10 | — | Medical deduction GL account |
| 58 | BKPR_EMP_MDAMT | NUMERIC | 8 | 2 | Medical deduction per-period amount |
| 59 | BKPR_EMP_MDDPT | STRING | 4 | — | Medical deduction GL department |
| 60 | BKPR_EMP_MDNME | STRING | 12 | — | Medical deduction name |
| 61 | BKPR_EMP_MDQTD | NUMERIC | 8 | 2 | Medical deduction QTD amount |
| 62 | BKPR_EMP_MDYTD | NUMERIC | 8 | 2 | Medical deduction YTD amount |
| 63 | BKPR_EMP_MS | STRING | 1 | — | Marital status (S=Single, M=Married) |
| 64 | BKPR_EMP_NUM | INTEGER | 2 | — | Employee number |
| 65 | BKPR_EMP_OAQTD_1 | NUMERIC | 8 | 2 | Other pay type 1 QTD amount |
| 66 | BKPR_EMP_OAQTD_10 | NUMERIC | 8 | 2 | Other pay type 10 QTD amount |
| 67 | BKPR_EMP_OAQTD_11 | NUMERIC | 8 | 2 | Other pay type 11 QTD amount |
| 68 | BKPR_EMP_OAQTD_12 | NUMERIC | 8 | 2 | Other pay type 12 QTD amount |
| 69 | BKPR_EMP_OAQTD_2 | NUMERIC | 8 | 2 | Other pay type 2 QTD amount |
| 70 | BKPR_EMP_OAQTD_3 | NUMERIC | 8 | 2 | Other pay type 3 QTD amount |
| 71 | BKPR_EMP_OAQTD_4 | NUMERIC | 8 | 2 | Other pay type 4 QTD amount |
| 72 | BKPR_EMP_OAQTD_5 | NUMERIC | 8 | 2 | Other pay type 5 QTD amount |
| 73 | BKPR_EMP_OAQTD_6 | NUMERIC | 8 | 2 | Other pay type 6 QTD amount |
| 74 | BKPR_EMP_OAQTD_7 | NUMERIC | 8 | 2 | Other pay type 7 QTD amount |
| 75 | BKPR_EMP_OAQTD_8 | NUMERIC | 8 | 2 | Other pay type 8 QTD amount |
| 76 | BKPR_EMP_OAQTD_9 | NUMERIC | 8 | 2 | Other pay type 9 QTD amount |
| 77 | BKPR_EMP_OAYTD_1 | NUMERIC | 8 | 2 | Other pay type 1 YTD amount |
| 78 | BKPR_EMP_OAYTD_10 | NUMERIC | 8 | 2 | Other pay type 10 YTD amount |
| 79 | BKPR_EMP_OAYTD_11 | NUMERIC | 8 | 2 | Other pay type 11 YTD amount |
| 80 | BKPR_EMP_OAYTD_12 | NUMERIC | 8 | 2 | Other pay type 12 YTD amount |
| 81 | BKPR_EMP_OAYTD_2 | NUMERIC | 8 | 2 | Other pay type 2 YTD amount |
| 82 | BKPR_EMP_OAYTD_3 | NUMERIC | 8 | 2 | Other pay type 3 YTD amount |
| 83 | BKPR_EMP_OAYTD_4 | NUMERIC | 8 | 2 | Other pay type 4 YTD amount |
| 84 | BKPR_EMP_OAYTD_5 | NUMERIC | 8 | 2 | Other pay type 5 YTD amount |
| 85 | BKPR_EMP_OAYTD_6 | NUMERIC | 8 | 2 | Other pay type 6 YTD amount |
| 86 | BKPR_EMP_OAYTD_7 | NUMERIC | 8 | 2 | Other pay type 7 YTD amount |
| 87 | BKPR_EMP_OAYTD_8 | NUMERIC | 8 | 2 | Other pay type 8 YTD amount |
| 88 | BKPR_EMP_OAYTD_9 | NUMERIC | 8 | 2 | Other pay type 9 YTD amount |
| 89 | BKPR_EMP_OHQTD_1 | NUMERIC | 8 | 2 | Other pay type 1 QTD hours |
| 90 | BKPR_EMP_OHQTD_10 | NUMERIC | 8 | 2 | Other pay type 10 QTD hours |
| 91 | BKPR_EMP_OHQTD_11 | NUMERIC | 8 | 2 | Other pay type 11 QTD hours |
| 92 | BKPR_EMP_OHQTD_12 | NUMERIC | 8 | 2 | Other pay type 12 QTD hours |
| 93 | BKPR_EMP_OHQTD_2 | NUMERIC | 8 | 2 | Other pay type 2 QTD hours |
| 94 | BKPR_EMP_OHQTD_3 | NUMERIC | 8 | 2 | Other pay type 3 QTD hours |
| 95 | BKPR_EMP_OHQTD_4 | NUMERIC | 8 | 2 | Other pay type 4 QTD hours |
| 96 | BKPR_EMP_OHQTD_5 | NUMERIC | 8 | 2 | Other pay type 5 QTD hours |
| 97 | BKPR_EMP_OHQTD_6 | NUMERIC | 8 | 2 | Other pay type 6 QTD hours |
| 98 | BKPR_EMP_OHQTD_7 | NUMERIC | 8 | 2 | Other pay type 7 QTD hours |
| 99 | BKPR_EMP_OHQTD_8 | NUMERIC | 8 | 2 | Other pay type 8 QTD hours |
| 100 | BKPR_EMP_OHQTD_9 | NUMERIC | 8 | 2 | Other pay type 9 QTD hours |
| 101 | BKPR_EMP_OHYTD_1 | NUMERIC | 8 | 2 | Other pay type 1 YTD hours |
| 102 | BKPR_EMP_OHYTD_10 | NUMERIC | 8 | 2 | Other pay type 10 YTD hours |
| 103 | BKPR_EMP_OHYTD_11 | NUMERIC | 8 | 2 | Other pay type 11 YTD hours |
| 104 | BKPR_EMP_OHYTD_12 | NUMERIC | 8 | 2 | Other pay type 12 YTD hours |
| 105 | BKPR_EMP_OHYTD_2 | NUMERIC | 8 | 2 | Other pay type 2 YTD hours |
| 106 | BKPR_EMP_OHYTD_3 | NUMERIC | 8 | 2 | Other pay type 3 YTD hours |
| 107 | BKPR_EMP_OHYTD_4 | NUMERIC | 8 | 2 | Other pay type 4 YTD hours |
| 108 | BKPR_EMP_OHYTD_5 | NUMERIC | 8 | 2 | Other pay type 5 YTD hours |
| 109 | BKPR_EMP_OHYTD_6 | NUMERIC | 8 | 2 | Other pay type 6 YTD hours |
| 110 | BKPR_EMP_OHYTD_7 | NUMERIC | 8 | 2 | Other pay type 7 YTD hours |
| 111 | BKPR_EMP_OHYTD_8 | NUMERIC | 8 | 2 | Other pay type 8 YTD hours |
| 112 | BKPR_EMP_OHYTD_9 | NUMERIC | 8 | 2 | Other pay type 9 YTD hours |
| 113 | BKPR_EMP_OPNAME_1 | STRING | 10 | — | Other pay type 1 name |
| 114 | BKPR_EMP_OPNAME_2 | STRING | 10 | — | Other pay type 2 name |
| 115 | BKPR_EMP_OPNAME_3 | STRING | 10 | — | Other pay type 3 name |
| 116 | BKPR_EMP_OPNAME_4 | STRING | 10 | — | Other pay type 4 name |
| 117 | BKPR_EMP_OPNAME_5 | STRING | 10 | — | Other pay type 5 name |
| 118 | BKPR_EMP_OTHACT | STRING | 10 | — | Other deduction GL account |
| 119 | BKPR_EMP_OTHAMT | NUMERIC | 8 | 2 | Other deduction per-period amount |
| 120 | BKPR_EMP_OTHDPT | STRING | 4 | — | Other deduction GL department |
| 121 | BKPR_EMP_OTHNME | STRING | 12 | — | Other deduction name |
| 122 | BKPR_EMP_OTHQTD | NUMERIC | 8 | 2 | Other deduction QTD amount |
| 123 | BKPR_EMP_OTHYTD | NUMERIC | 8 | 2 | Other deduction YTD amount |
| 124 | BKPR_EMP_PAYAMT_1 | NUMERIC | 8 | 4 | Pay rate 1 amount |
| 125 | BKPR_EMP_PAYAMT_10 | NUMERIC | 8 | 4 | Pay rate 10 amount |
| 126 | BKPR_EMP_PAYAMT_11 | NUMERIC | 8 | 4 | Pay rate 11 amount |
| 127 | BKPR_EMP_PAYAMT_12 | NUMERIC | 8 | 4 | Pay rate 12 amount |
| 128 | BKPR_EMP_PAYAMT_13 | NUMERIC | 8 | 4 | Pay rate 13 amount |
| 129 | BKPR_EMP_PAYAMT_14 | NUMERIC | 8 | 4 | Pay rate 14 amount |
| 130 | BKPR_EMP_PAYAMT_15 | NUMERIC | 8 | 4 | Pay rate 15 amount |
| 131 | BKPR_EMP_PAYAMT_2 | NUMERIC | 8 | 4 | Pay rate 2 amount |
| 132 | BKPR_EMP_PAYAMT_3 | NUMERIC | 8 | 4 | Pay rate 3 amount |
| 133 | BKPR_EMP_PAYAMT_4 | NUMERIC | 8 | 4 | Pay rate 4 amount |
| 134 | BKPR_EMP_PAYAMT_5 | NUMERIC | 8 | 4 | Pay rate 5 amount |
| 135 | BKPR_EMP_PAYAMT_6 | NUMERIC | 8 | 4 | Pay rate 6 amount |
| 136 | BKPR_EMP_PAYAMT_7 | NUMERIC | 8 | 4 | Pay rate 7 amount |
| 137 | BKPR_EMP_PAYAMT_8 | NUMERIC | 8 | 4 | Pay rate 8 amount |
| 138 | BKPR_EMP_PAYAMT_9 | NUMERIC | 8 | 4 | Pay rate 9 amount |
| 139 | BKPR_EMP_PAYTYP | STRING | 1 | — | Pay type (H=Hourly, S=Salary) |
| 140 | BKPR_EMP_PHONE | STRING | 15 | — | Employee phone number |
| 141 | BKPR_EMP_QTR | INTEGER | 2 | — | Current quarter number (1-4) |
| 142 | BKPR_EMP_RAQTD | NUMERIC | 8 | 2 | Regular pay QTD amount |
| 143 | BKPR_EMP_RAYTD | NUMERIC | 8 | 2 | Regular pay YTD amount |
| 144 | BKPR_EMP_RHQTD | NUMERIC | 8 | 2 | Regular pay QTD hours |
| 145 | BKPR_EMP_RHYTD | NUMERIC | 8 | 2 | Regular pay YTD hours |
| 146 | BKPR_EMP_SAQTD | NUMERIC | 8 | 2 | Special pay QTD amount |
| 147 | BKPR_EMP_SAYTD | NUMERIC | 8 | 2 | Special pay YTD amount |
| 148 | BKPR_EMP_SCAP | NUMERIC | 8 | 2 | Salary cap amount |
| 149 | BKPR_EMP_SDATE | DATE | 4 | — | Employee start/hire date |
| 150 | BKPR_EMP_SDIEXM | STRING | 1 | — | SDI exempt flag (Y/N) |
| 151 | BKPR_EMP_SDIQTD | NUMERIC | 8 | 2 | SDI withheld QTD |
| 152 | BKPR_EMP_SDIYTD | NUMERIC | 8 | 2 | SDI withheld YTD |
| 153 | BKPR_EMP_SDUE | NUMERIC | 8 | 2 | Salary due/accrued amount |
| 154 | BKPR_EMP_SHIFT | INTEGER | 2 | — | Default shift number |
| 155 | BKPR_EMP_SHQTD | NUMERIC | 8 | 2 | Special pay QTD hours |
| 156 | BKPR_EMP_SHYTD | NUMERIC | 8 | 2 | Special pay YTD hours |
| 157 | BKPR_EMP_SRTE | NUMERIC | 8 | 4 | Salary pay rate |
| 158 | BKPR_EMP_SSN | STRING | 11 | — | Social security number (XXX-XX-XXXX) |
| 159 | BKPR_EMP_ST | STRING | 2 | — | State code for tax withholding |
| 160 | BKPR_EMP_STEXM | INTEGER | 2 | — | Number of state withholding exemptions |
| 161 | BKPR_EMP_STEXMA | NUMERIC | 8 | — | State exemption additional amount |
| 162 | BKPR_EMP_STEXMN | INTEGER | 2 | — | Number of additional state exemptions |
| 163 | BKPR_EMP_STQTD | NUMERIC | 8 | 2 | State income tax withheld QTD |
| 164 | BKPR_EMP_STYTD | NUMERIC | 8 | 2 | State income tax withheld YTD |
| 165 | BKPR_EMP_TERM | STRING | 1 | — | Terminated flag (Y/N) |
| 166 | BKPR_EMP_UDAMT1_1 | NUMERIC | 8 | 2 | User deduction (type 1) slot 1 amount |
| 167 | BKPR_EMP_UDAMT1_2 | NUMERIC | 8 | 2 | User deduction (type 1) slot 2 amount |
| 168 | BKPR_EMP_UDAMT1_3 | NUMERIC | 8 | 2 | User deduction (type 1) slot 3 amount |
| 169 | BKPR_EMP_UDAMT1_4 | NUMERIC | 8 | 2 | User deduction (type 1) slot 4 amount |
| 170 | BKPR_EMP_UDAMT1_5 | NUMERIC | 8 | 2 | User deduction (type 1) slot 5 amount |
| 171 | BKPR_EMP_UDAMT1_6 | NUMERIC | 8 | 2 | User deduction (type 1) slot 6 amount |
| 172 | BKPR_EMP_UDEAMT_1 | NUMERIC | 8 | 4 | User other deduction 1 employee per-period amount |
| 173 | BKPR_EMP_UDEAMT_10 | NUMERIC | 8 | 4 | User other deduction 10 employee per-period amount |
| 174 | BKPR_EMP_UDEAMT_11 | NUMERIC | 8 | 4 | User other deduction 11 employee per-period amount |
| 175 | BKPR_EMP_UDEAMT_12 | NUMERIC | 8 | 4 | User other deduction 12 employee per-period amount |
| 176 | BKPR_EMP_UDEAMT_13 | NUMERIC | 8 | 4 | User other deduction 13 employee per-period amount |
| 177 | BKPR_EMP_UDEAMT_14 | NUMERIC | 8 | 4 | User other deduction 14 employee per-period amount |
| 178 | BKPR_EMP_UDEAMT_15 | NUMERIC | 8 | 4 | User other deduction 15 employee per-period amount |
| 179 | BKPR_EMP_UDEAMT_16 | NUMERIC | 8 | 4 | User other deduction 16 employee per-period amount |
| 180 | BKPR_EMP_UDEAMT_17 | NUMERIC | 8 | 4 | User other deduction 17 employee per-period amount |
| 181 | BKPR_EMP_UDEAMT_18 | NUMERIC | 8 | 4 | User other deduction 18 employee per-period amount |
| 182 | BKPR_EMP_UDEAMT_19 | NUMERIC | 8 | 4 | User other deduction 19 employee per-period amount |
| 183 | BKPR_EMP_UDEAMT_2 | NUMERIC | 8 | 4 | User other deduction 2 employee per-period amount |
| 184 | BKPR_EMP_UDEAMT_20 | NUMERIC | 8 | 4 | User other deduction 20 employee per-period amount |
| 185 | BKPR_EMP_UDEAMT_3 | NUMERIC | 8 | 4 | User other deduction 3 employee per-period amount |
| 186 | BKPR_EMP_UDEAMT_4 | NUMERIC | 8 | 4 | User other deduction 4 employee per-period amount |
| 187 | BKPR_EMP_UDEAMT_5 | NUMERIC | 8 | 4 | User other deduction 5 employee per-period amount |
| 188 | BKPR_EMP_UDEAMT_6 | NUMERIC | 8 | 4 | User other deduction 6 employee per-period amount |
| 189 | BKPR_EMP_UDEAMT_7 | NUMERIC | 8 | 4 | User other deduction 7 employee per-period amount |
| 190 | BKPR_EMP_UDEAMT_8 | NUMERIC | 8 | 4 | User other deduction 8 employee per-period amount |
| 191 | BKPR_EMP_UDEAMT_9 | NUMERIC | 8 | 4 | User other deduction 9 employee per-period amount |
| 192 | BKPR_EMP_UDELMT_1 | NUMERIC | 8 | 4 | User other deduction 1 employee per-period limit |
| 193 | BKPR_EMP_UDELMT_10 | NUMERIC | 8 | 4 | User other deduction 10 employee per-period limit |
| 194 | BKPR_EMP_UDELMT_11 | NUMERIC | 8 | 4 | User other deduction 11 employee per-period limit |
| 195 | BKPR_EMP_UDELMT_12 | NUMERIC | 8 | 4 | User other deduction 12 employee per-period limit |
| 196 | BKPR_EMP_UDELMT_13 | NUMERIC | 8 | 4 | User other deduction 13 employee per-period limit |
| 197 | BKPR_EMP_UDELMT_14 | NUMERIC | 8 | 4 | User other deduction 14 employee per-period limit |
| 198 | BKPR_EMP_UDELMT_15 | NUMERIC | 8 | 4 | User other deduction 15 employee per-period limit |
| 199 | BKPR_EMP_UDELMT_16 | NUMERIC | 8 | 4 | User other deduction 16 employee per-period limit |
| 200 | BKPR_EMP_UDELMT_17 | NUMERIC | 8 | 4 | User other deduction 17 employee per-period limit |
| 201 | BKPR_EMP_UDELMT_18 | NUMERIC | 8 | 4 | User other deduction 18 employee per-period limit |
| 202 | BKPR_EMP_UDELMT_19 | NUMERIC | 8 | 4 | User other deduction 19 employee per-period limit |
| 203 | BKPR_EMP_UDELMT_2 | NUMERIC | 8 | 4 | User other deduction 2 employee per-period limit |
| 204 | BKPR_EMP_UDELMT_20 | NUMERIC | 8 | 4 | User other deduction 20 employee per-period limit |
| 205 | BKPR_EMP_UDELMT_3 | NUMERIC | 8 | 4 | User other deduction 3 employee per-period limit |
| 206 | BKPR_EMP_UDELMT_4 | NUMERIC | 8 | 4 | User other deduction 4 employee per-period limit |
| 207 | BKPR_EMP_UDELMT_5 | NUMERIC | 8 | 4 | User other deduction 5 employee per-period limit |
| 208 | BKPR_EMP_UDELMT_6 | NUMERIC | 8 | 4 | User other deduction 6 employee per-period limit |
| 209 | BKPR_EMP_UDELMT_7 | NUMERIC | 8 | 4 | User other deduction 7 employee per-period limit |
| 210 | BKPR_EMP_UDELMT_8 | NUMERIC | 8 | 4 | User other deduction 8 employee per-period limit |
| 211 | BKPR_EMP_UDELMT_9 | NUMERIC | 8 | 4 | User other deduction 9 employee per-period limit |
| 212 | BKPR_EMP_UDEQTD_1 | NUMERIC | 8 | 2 | User other deduction 1 employee QTD amount |
| 213 | BKPR_EMP_UDEQTD_10 | NUMERIC | 8 | 2 | User other deduction 10 employee QTD amount |
| 214 | BKPR_EMP_UDEQTD_11 | NUMERIC | 8 | 2 | User other deduction 11 employee QTD amount |
| 215 | BKPR_EMP_UDEQTD_12 | NUMERIC | 8 | 2 | User other deduction 12 employee QTD amount |
| 216 | BKPR_EMP_UDEQTD_13 | NUMERIC | 8 | 2 | User other deduction 13 employee QTD amount |
| 217 | BKPR_EMP_UDEQTD_14 | NUMERIC | 8 | 2 | User other deduction 14 employee QTD amount |
| 218 | BKPR_EMP_UDEQTD_15 | NUMERIC | 8 | 2 | User other deduction 15 employee QTD amount |
| 219 | BKPR_EMP_UDEQTD_16 | NUMERIC | 8 | 2 | User other deduction 16 employee QTD amount |
| 220 | BKPR_EMP_UDEQTD_17 | NUMERIC | 8 | 2 | User other deduction 17 employee QTD amount |
| 221 | BKPR_EMP_UDEQTD_18 | NUMERIC | 8 | 2 | User other deduction 18 employee QTD amount |
| 222 | BKPR_EMP_UDEQTD_19 | NUMERIC | 8 | 2 | User other deduction 19 employee QTD amount |
| 223 | BKPR_EMP_UDEQTD_2 | NUMERIC | 8 | 2 | User other deduction 2 employee QTD amount |
| 224 | BKPR_EMP_UDEQTD_20 | NUMERIC | 8 | 2 | User other deduction 20 employee QTD amount |
| 225 | BKPR_EMP_UDEQTD_3 | NUMERIC | 8 | 2 | User other deduction 3 employee QTD amount |
| 226 | BKPR_EMP_UDEQTD_4 | NUMERIC | 8 | 2 | User other deduction 4 employee QTD amount |
| 227 | BKPR_EMP_UDEQTD_5 | NUMERIC | 8 | 2 | User other deduction 5 employee QTD amount |
| 228 | BKPR_EMP_UDEQTD_6 | NUMERIC | 8 | 2 | User other deduction 6 employee QTD amount |
| 229 | BKPR_EMP_UDEQTD_7 | NUMERIC | 8 | 2 | User other deduction 7 employee QTD amount |
| 230 | BKPR_EMP_UDEQTD_8 | NUMERIC | 8 | 2 | User other deduction 8 employee QTD amount |
| 231 | BKPR_EMP_UDEQTD_9 | NUMERIC | 8 | 2 | User other deduction 9 employee QTD amount |
| 232 | BKPR_EMP_UDEYLM_1 | NUMERIC | 8 | 2 | User other deduction 1 employee annual limit |
| 233 | BKPR_EMP_UDEYLM_10 | NUMERIC | 8 | 2 | User other deduction 10 employee annual limit |
| 234 | BKPR_EMP_UDEYLM_11 | NUMERIC | 8 | 2 | User other deduction 11 employee annual limit |
| 235 | BKPR_EMP_UDEYLM_12 | NUMERIC | 8 | 2 | User other deduction 12 employee annual limit |
| 236 | BKPR_EMP_UDEYLM_13 | NUMERIC | 8 | 2 | User other deduction 13 employee annual limit |
| 237 | BKPR_EMP_UDEYLM_14 | NUMERIC | 8 | 2 | User other deduction 14 employee annual limit |
| 238 | BKPR_EMP_UDEYLM_15 | NUMERIC | 8 | 2 | User other deduction 15 employee annual limit |
| 239 | BKPR_EMP_UDEYLM_16 | NUMERIC | 8 | 2 | User other deduction 16 employee annual limit |
| 240 | BKPR_EMP_UDEYLM_17 | NUMERIC | 8 | 2 | User other deduction 17 employee annual limit |
| 241 | BKPR_EMP_UDEYLM_18 | NUMERIC | 8 | 2 | User other deduction 18 employee annual limit |
| 242 | BKPR_EMP_UDEYLM_19 | NUMERIC | 8 | 2 | User other deduction 19 employee annual limit |
| 243 | BKPR_EMP_UDEYLM_2 | NUMERIC | 8 | 2 | User other deduction 2 employee annual limit |
| 244 | BKPR_EMP_UDEYLM_20 | NUMERIC | 8 | 2 | User other deduction 20 employee annual limit |
| 245 | BKPR_EMP_UDEYLM_3 | NUMERIC | 8 | 2 | User other deduction 3 employee annual limit |
| 246 | BKPR_EMP_UDEYLM_4 | NUMERIC | 8 | 2 | User other deduction 4 employee annual limit |
| 247 | BKPR_EMP_UDEYLM_5 | NUMERIC | 8 | 2 | User other deduction 5 employee annual limit |
| 248 | BKPR_EMP_UDEYLM_6 | NUMERIC | 8 | 2 | User other deduction 6 employee annual limit |
| 249 | BKPR_EMP_UDEYLM_7 | NUMERIC | 8 | 2 | User other deduction 7 employee annual limit |
| 250 | BKPR_EMP_UDEYLM_8 | NUMERIC | 8 | 2 | User other deduction 8 employee annual limit |
| 251 | BKPR_EMP_UDEYLM_9 | NUMERIC | 8 | 2 | User other deduction 9 employee annual limit |
| 252 | BKPR_EMP_UDEYTD_1 | NUMERIC | 8 | 2 | User other deduction 1 employee YTD amount |
| 253 | BKPR_EMP_UDEYTD_10 | NUMERIC | 8 | 2 | User other deduction 10 employee YTD amount |
| 254 | BKPR_EMP_UDEYTD_11 | NUMERIC | 8 | 2 | User other deduction 11 employee YTD amount |
| 255 | BKPR_EMP_UDEYTD_12 | NUMERIC | 8 | 2 | User other deduction 12 employee YTD amount |
| 256 | BKPR_EMP_UDEYTD_13 | NUMERIC | 8 | 2 | User other deduction 13 employee YTD amount |
| 257 | BKPR_EMP_UDEYTD_14 | NUMERIC | 8 | 2 | User other deduction 14 employee YTD amount |
| 258 | BKPR_EMP_UDEYTD_15 | NUMERIC | 8 | 2 | User other deduction 15 employee YTD amount |
| 259 | BKPR_EMP_UDEYTD_16 | NUMERIC | 8 | 2 | User other deduction 16 employee YTD amount |
| 260 | BKPR_EMP_UDEYTD_17 | NUMERIC | 8 | 2 | User other deduction 17 employee YTD amount |
| 261 | BKPR_EMP_UDEYTD_18 | NUMERIC | 8 | 2 | User other deduction 18 employee YTD amount |
| 262 | BKPR_EMP_UDEYTD_19 | NUMERIC | 8 | 2 | User other deduction 19 employee YTD amount |
| 263 | BKPR_EMP_UDEYTD_2 | NUMERIC | 8 | 2 | User other deduction 2 employee YTD amount |
| 264 | BKPR_EMP_UDEYTD_20 | NUMERIC | 8 | 2 | User other deduction 20 employee YTD amount |
| 265 | BKPR_EMP_UDEYTD_3 | NUMERIC | 8 | 2 | User other deduction 3 employee YTD amount |
| 266 | BKPR_EMP_UDEYTD_4 | NUMERIC | 8 | 2 | User other deduction 4 employee YTD amount |
| 267 | BKPR_EMP_UDEYTD_5 | NUMERIC | 8 | 2 | User other deduction 5 employee YTD amount |
| 268 | BKPR_EMP_UDEYTD_6 | NUMERIC | 8 | 2 | User other deduction 6 employee YTD amount |
| 269 | BKPR_EMP_UDEYTD_7 | NUMERIC | 8 | 2 | User other deduction 7 employee YTD amount |
| 270 | BKPR_EMP_UDEYTD_8 | NUMERIC | 8 | 2 | User other deduction 8 employee YTD amount |
| 271 | BKPR_EMP_UDEYTD_9 | NUMERIC | 8 | 2 | User other deduction 9 employee YTD amount |
| 272 | BKPR_EMP_UODAMT_1 | NUMERIC | 8 | 4 | User other deduction 1 per-period amount |
| 273 | BKPR_EMP_UODAMT_10 | NUMERIC | 8 | 4 | User other deduction 10 per-period amount |
| 274 | BKPR_EMP_UODAMT_11 | NUMERIC | 8 | 4 | User other deduction 11 per-period amount |
| 275 | BKPR_EMP_UODAMT_12 | NUMERIC | 8 | 4 | User other deduction 12 per-period amount |
| 276 | BKPR_EMP_UODAMT_13 | NUMERIC | 8 | 4 | User other deduction 13 per-period amount |
| 277 | BKPR_EMP_UODAMT_14 | NUMERIC | 8 | 4 | User other deduction 14 per-period amount |
| 278 | BKPR_EMP_UODAMT_15 | NUMERIC | 8 | 4 | User other deduction 15 per-period amount |
| 279 | BKPR_EMP_UODAMT_16 | NUMERIC | 8 | 4 | User other deduction 16 per-period amount |
| 280 | BKPR_EMP_UODAMT_17 | NUMERIC | 8 | 4 | User other deduction 17 per-period amount |
| 281 | BKPR_EMP_UODAMT_18 | NUMERIC | 8 | 4 | User other deduction 18 per-period amount |
| 282 | BKPR_EMP_UODAMT_19 | NUMERIC | 8 | 4 | User other deduction 19 per-period amount |
| 283 | BKPR_EMP_UODAMT_2 | NUMERIC | 8 | 4 | User other deduction 2 per-period amount |
| 284 | BKPR_EMP_UODAMT_20 | NUMERIC | 8 | 4 | User other deduction 20 per-period amount |
| 285 | BKPR_EMP_UODAMT_3 | NUMERIC | 8 | 4 | User other deduction 3 per-period amount |
| 286 | BKPR_EMP_UODAMT_4 | NUMERIC | 8 | 4 | User other deduction 4 per-period amount |
| 287 | BKPR_EMP_UODAMT_5 | NUMERIC | 8 | 4 | User other deduction 5 per-period amount |
| 288 | BKPR_EMP_UODAMT_6 | NUMERIC | 8 | 4 | User other deduction 6 per-period amount |
| 289 | BKPR_EMP_UODAMT_7 | NUMERIC | 8 | 4 | User other deduction 7 per-period amount |
| 290 | BKPR_EMP_UODAMT_8 | NUMERIC | 8 | 4 | User other deduction 8 per-period amount |
| 291 | BKPR_EMP_UODAMT_9 | NUMERIC | 8 | 4 | User other deduction 9 per-period amount |
| 292 | BKPR_EMP_UODLMT_1 | NUMERIC | 8 | 4 | User other deduction 1 per-period limit |
| 293 | BKPR_EMP_UODLMT_10 | NUMERIC | 8 | 4 | User other deduction 10 per-period limit |
| 294 | BKPR_EMP_UODLMT_11 | NUMERIC | 8 | 4 | User other deduction 11 per-period limit |
| 295 | BKPR_EMP_UODLMT_12 | NUMERIC | 8 | 4 | User other deduction 12 per-period limit |
| 296 | BKPR_EMP_UODLMT_13 | NUMERIC | 8 | 4 | User other deduction 13 per-period limit |
| 297 | BKPR_EMP_UODLMT_14 | NUMERIC | 8 | 4 | User other deduction 14 per-period limit |
| 298 | BKPR_EMP_UODLMT_15 | NUMERIC | 8 | 4 | User other deduction 15 per-period limit |
| 299 | BKPR_EMP_UODLMT_16 | NUMERIC | 8 | 4 | User other deduction 16 per-period limit |
| 300 | BKPR_EMP_UODLMT_17 | NUMERIC | 8 | 4 | User other deduction 17 per-period limit |
| 301 | BKPR_EMP_UODLMT_18 | NUMERIC | 8 | 4 | User other deduction 18 per-period limit |
| 302 | BKPR_EMP_UODLMT_19 | NUMERIC | 8 | 4 | User other deduction 19 per-period limit |
| 303 | BKPR_EMP_UODLMT_2 | NUMERIC | 8 | 4 | User other deduction 2 per-period limit |
| 304 | BKPR_EMP_UODLMT_20 | NUMERIC | 8 | 4 | User other deduction 20 per-period limit |
| 305 | BKPR_EMP_UODLMT_3 | NUMERIC | 8 | 4 | User other deduction 3 per-period limit |
| 306 | BKPR_EMP_UODLMT_4 | NUMERIC | 8 | 4 | User other deduction 4 per-period limit |
| 307 | BKPR_EMP_UODLMT_5 | NUMERIC | 8 | 4 | User other deduction 5 per-period limit |
| 308 | BKPR_EMP_UODLMT_6 | NUMERIC | 8 | 4 | User other deduction 6 per-period limit |
| 309 | BKPR_EMP_UODLMT_7 | NUMERIC | 8 | 4 | User other deduction 7 per-period limit |
| 310 | BKPR_EMP_UODLMT_8 | NUMERIC | 8 | 4 | User other deduction 8 per-period limit |
| 311 | BKPR_EMP_UODLMT_9 | NUMERIC | 8 | 4 | User other deduction 9 per-period limit |
| 312 | BKPR_EMP_UODQTD_1 | NUMERIC | 8 | 2 | User other deduction 1 QTD amount |
| 313 | BKPR_EMP_UODQTD_10 | NUMERIC | 8 | 2 | User other deduction 10 QTD amount |
| 314 | BKPR_EMP_UODQTD_11 | NUMERIC | 8 | 2 | User other deduction 11 QTD amount |
| 315 | BKPR_EMP_UODQTD_12 | NUMERIC | 8 | 2 | User other deduction 12 QTD amount |
| 316 | BKPR_EMP_UODQTD_13 | NUMERIC | 8 | 2 | User other deduction 13 QTD amount |
| 317 | BKPR_EMP_UODQTD_14 | NUMERIC | 8 | 2 | User other deduction 14 QTD amount |
| 318 | BKPR_EMP_UODQTD_15 | NUMERIC | 8 | 2 | User other deduction 15 QTD amount |
| 319 | BKPR_EMP_UODQTD_16 | NUMERIC | 8 | 2 | User other deduction 16 QTD amount |
| 320 | BKPR_EMP_UODQTD_17 | NUMERIC | 8 | 2 | User other deduction 17 QTD amount |
| 321 | BKPR_EMP_UODQTD_18 | NUMERIC | 8 | 2 | User other deduction 18 QTD amount |
| 322 | BKPR_EMP_UODQTD_19 | NUMERIC | 8 | 2 | User other deduction 19 QTD amount |
| 323 | BKPR_EMP_UODQTD_2 | NUMERIC | 8 | 2 | User other deduction 2 QTD amount |
| 324 | BKPR_EMP_UODQTD_20 | NUMERIC | 8 | 2 | User other deduction 20 QTD amount |
| 325 | BKPR_EMP_UODQTD_3 | NUMERIC | 8 | 2 | User other deduction 3 QTD amount |
| 326 | BKPR_EMP_UODQTD_4 | NUMERIC | 8 | 2 | User other deduction 4 QTD amount |
| 327 | BKPR_EMP_UODQTD_5 | NUMERIC | 8 | 2 | User other deduction 5 QTD amount |
| 328 | BKPR_EMP_UODQTD_6 | NUMERIC | 8 | 2 | User other deduction 6 QTD amount |
| 329 | BKPR_EMP_UODQTD_7 | NUMERIC | 8 | 2 | User other deduction 7 QTD amount |
| 330 | BKPR_EMP_UODQTD_8 | NUMERIC | 8 | 2 | User other deduction 8 QTD amount |
| 331 | BKPR_EMP_UODQTD_9 | NUMERIC | 8 | 2 | User other deduction 9 QTD amount |
| 332 | BKPR_EMP_UODYLM_1 | NUMERIC | 8 | 2 | User other deduction 1 annual limit |
| 333 | BKPR_EMP_UODYLM_10 | NUMERIC | 8 | 2 | User other deduction 10 annual limit |
| 334 | BKPR_EMP_UODYLM_11 | NUMERIC | 8 | 2 | User other deduction 11 annual limit |
| 335 | BKPR_EMP_UODYLM_12 | NUMERIC | 8 | 2 | User other deduction 12 annual limit |
| 336 | BKPR_EMP_UODYLM_13 | NUMERIC | 8 | 2 | User other deduction 13 annual limit |
| 337 | BKPR_EMP_UODYLM_14 | NUMERIC | 8 | 2 | User other deduction 14 annual limit |
| 338 | BKPR_EMP_UODYLM_15 | NUMERIC | 8 | 2 | User other deduction 15 annual limit |
| 339 | BKPR_EMP_UODYLM_16 | NUMERIC | 8 | 2 | User other deduction 16 annual limit |
| 340 | BKPR_EMP_UODYLM_17 | NUMERIC | 8 | 2 | User other deduction 17 annual limit |
| 341 | BKPR_EMP_UODYLM_18 | NUMERIC | 8 | 2 | User other deduction 18 annual limit |
| 342 | BKPR_EMP_UODYLM_19 | NUMERIC | 8 | 2 | User other deduction 19 annual limit |
| 343 | BKPR_EMP_UODYLM_2 | NUMERIC | 8 | 2 | User other deduction 2 annual limit |
| 344 | BKPR_EMP_UODYLM_20 | NUMERIC | 8 | 2 | User other deduction 20 annual limit |
| 345 | BKPR_EMP_UODYLM_3 | NUMERIC | 8 | 2 | User other deduction 3 annual limit |
| 346 | BKPR_EMP_UODYLM_4 | NUMERIC | 8 | 2 | User other deduction 4 annual limit |
| 347 | BKPR_EMP_UODYLM_5 | NUMERIC | 8 | 2 | User other deduction 5 annual limit |
| 348 | BKPR_EMP_UODYLM_6 | NUMERIC | 8 | 2 | User other deduction 6 annual limit |
| 349 | BKPR_EMP_UODYLM_7 | NUMERIC | 8 | 2 | User other deduction 7 annual limit |
| 350 | BKPR_EMP_UODYLM_8 | NUMERIC | 8 | 2 | User other deduction 8 annual limit |
| 351 | BKPR_EMP_UODYLM_9 | NUMERIC | 8 | 2 | User other deduction 9 annual limit |
| 352 | BKPR_EMP_UODYTD_1 | NUMERIC | 8 | 2 | User other deduction 1 YTD amount |
| 353 | BKPR_EMP_UODYTD_10 | NUMERIC | 8 | 2 | User other deduction 10 YTD amount |
| 354 | BKPR_EMP_UODYTD_11 | NUMERIC | 8 | 2 | User other deduction 11 YTD amount |
| 355 | BKPR_EMP_UODYTD_12 | NUMERIC | 8 | 2 | User other deduction 12 YTD amount |
| 356 | BKPR_EMP_UODYTD_13 | NUMERIC | 8 | 2 | User other deduction 13 YTD amount |
| 357 | BKPR_EMP_UODYTD_14 | NUMERIC | 8 | 2 | User other deduction 14 YTD amount |
| 358 | BKPR_EMP_UODYTD_15 | NUMERIC | 8 | 2 | User other deduction 15 YTD amount |
| 359 | BKPR_EMP_UODYTD_16 | NUMERIC | 8 | 2 | User other deduction 16 YTD amount |
| 360 | BKPR_EMP_UODYTD_17 | NUMERIC | 8 | 2 | User other deduction 17 YTD amount |
| 361 | BKPR_EMP_UODYTD_18 | NUMERIC | 8 | 2 | User other deduction 18 YTD amount |
| 362 | BKPR_EMP_UODYTD_19 | NUMERIC | 8 | 2 | User other deduction 19 YTD amount |
| 363 | BKPR_EMP_UODYTD_2 | NUMERIC | 8 | 2 | User other deduction 2 YTD amount |
| 364 | BKPR_EMP_UODYTD_20 | NUMERIC | 8 | 2 | User other deduction 20 YTD amount |
| 365 | BKPR_EMP_UODYTD_3 | NUMERIC | 8 | 2 | User other deduction 3 YTD amount |
| 366 | BKPR_EMP_UODYTD_4 | NUMERIC | 8 | 2 | User other deduction 4 YTD amount |
| 367 | BKPR_EMP_UODYTD_5 | NUMERIC | 8 | 2 | User other deduction 5 YTD amount |
| 368 | BKPR_EMP_UODYTD_6 | NUMERIC | 8 | 2 | User other deduction 6 YTD amount |
| 369 | BKPR_EMP_UODYTD_7 | NUMERIC | 8 | 2 | User other deduction 7 YTD amount |
| 370 | BKPR_EMP_UODYTD_8 | NUMERIC | 8 | 2 | User other deduction 8 YTD amount |
| 371 | BKPR_EMP_UODYTD_9 | NUMERIC | 8 | 2 | User other deduction 9 YTD amount |
| 372 | BKPR_EMP_VAQTD | NUMERIC | 8 | 2 | Vacation pay QTD amount |
| 373 | BKPR_EMP_VAYTD | NUMERIC | 8 | 2 | Vacation pay YTD amount |
| 374 | BKPR_EMP_VCAP | NUMERIC | 8 | 2 | Vacation time cap (maximum accrual) |
| 375 | BKPR_EMP_VDUE | NUMERIC | 8 | 2 | Vacation time due/accrued balance |
| 376 | BKPR_EMP_VHQTD | NUMERIC | 8 | 2 | Vacation pay QTD hours |
| 377 | BKPR_EMP_VHYTD | NUMERIC | 8 | 2 | Vacation pay YTD hours |
| 378 | BKPR_EMP_VRTE | NUMERIC | 8 | 4 | Vacation pay rate |
| 379 | BKPR_EMP_WCEE | NUMERIC | 8 | 4 | Workers comp employee rate |
| 380 | BKPR_EMP_WCER | NUMERIC | 8 | 4 | Workers comp employer rate |
| 381 | BKPR_EMP_WKQTD | NUMERIC | 8 | 2 | Total weeks worked QTD |
| 382 | BKPR_EMP_WKYTD | NUMERIC | 8 | 2 | Total weeks worked YTD |
| 383 | BKPR_EMP_YEAR | NUMERIC | 8 | — | Calendar year for this W2/payroll record |
| 384 | BKPR_EMP_ZIP | STRING | 10 | — | Employee ZIP code |

## ISPRTEMP
**TEMP FILE FOR CONSOLIDATING PAYROLL DETAIL**

Fields: 15

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISPR_TRN_AMT | NUMERIC | 8 | 2 | Transaction amount |
| 2 | ISPR_TRN_BATCH | NUMERIC | 8 | — | Batch number for this transaction |
| 3 | ISPR_TRN_CODE | STRING | 10 | — | Transaction code |
| 4 | ISPR_TRN_DATE | DATE | 4 | — | Transaction date |
| 5 | ISPR_TRN_DC | STRING | 1 | — | Debit/Credit flag (D/C) |
| 6 | ISPR_TRN_DESC | STRING | 25 | — | Transaction description |
| 7 | ISPR_TRN_ENTDTE | DATE | 4 | — | Entry date |
| 8 | ISPR_TRN_EXTRA | STRING | 25 | — | Reserved extra field |
| 9 | ISPR_TRN_GLACCT | STRING | 10 | — | GL account for this transaction |
| 10 | ISPR_TRN_GLDPT | STRING | 4 | — | GL department for this transaction |
| 11 | ISPR_TRN_INVC | STRING | 10 | — | Invoice/reference number |
| 12 | ISPR_TRN_PERIOD | INTEGER | 2 | — | Accounting period number |
| 13 | ISPR_TRN_POST | STRING | 1 | — | Posted flag (Y/N) |
| 14 | ISPR_TRN_TRXN | NUMERIC | 8 | — | Transaction number |
| 15 | ISPR_TRN_TYPE | STRING | 2 | — | Transaction type code |

## ISPRUDF
**USER DEFINED DEDUCTIONS**

Fields: 31

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISPR_UDF_CALCEE | STRING | 1 | — | Employee deduction calculation method flag |
| 2 | ISPR_UDF_CALCRE | STRING | 1 | — | Employer contribution calculation method flag |
| 3 | ISPR_UDF_DESC | STRING | 12 | — | User-defined deduction description |
| 4 | ISPR_UDF_DIV | STRING | 4 | — | Division code |
| 5 | ISPR_UDF_DIVNAM | STRING | 20 | — | Division name |
| 6 | ISPR_UDF_EACCT | STRING | 10 | — | Employee deduction expense GL account |
| 7 | ISPR_UDF_EDEPT | STRING | 4 | — | Employee deduction expense GL department |
| 8 | ISPR_UDF_EEAMT | NUMERIC | 8 | 4 | Employee deduction per-period amount |
| 9 | ISPR_UDF_EETYPE | STRING | 17 | — | Employee deduction type code |
| 10 | ISPR_UDF_ERAMT | NUMERIC | 8 | 4 | Employer contribution per-period amount |
| 11 | ISPR_UDF_ERTYPE | STRING | 17 | — | Employer contribution type code |
| 12 | ISPR_UDF_EXTRA | STRING | 100 | — | Reserved extra field |
| 13 | ISPR_UDF_FIT | STRING | 1 | — | FIT-applicable flag (Y/N) |
| 14 | ISPR_UDF_FUTA | STRING | 1 | — | FUTA-applicable flag (Y/N) |
| 15 | ISPR_UDF_LACCT | STRING | 10 | — | Liability GL account |
| 16 | ISPR_UDF_LDEPT | STRING | 4 | — | Liability GL department |
| 17 | ISPR_UDF_LOCAL | STRING | 1 | — | Local tax applicable flag (Y/N) |
| 18 | ISPR_UDF_MED | STRING | 1 | — | Medicare-applicable flag (Y/N) |
| 19 | ISPR_UDF_NUM | NUMERIC | 8 | — | User-defined deduction record number |
| 20 | ISPR_UDF_PTAX | STRING | 1 | — | Pre-tax deduction flag (Y/N) |
| 21 | ISPR_UDF_SDI | STRING | 1 | — | SDI-applicable flag (Y/N) |
| 22 | ISPR_UDF_SIT | STRING | 1 | — | SIT-applicable flag (Y/N) |
| 23 | ISPR_UDF_SS | STRING | 1 | — | Social Security applicable flag (Y/N) |
| 24 | ISPR_UDF_SUTA | STRING | 1 | — | SUTA-applicable flag (Y/N) |
| 25 | ISPR_UDF_TAXOUT | NUMERIC | 8 | 2 | Tax output amount |
| 26 | ISPR_UDF_UDELMT | NUMERIC | 8 | 4 | Employee per-period deduction limit |
| 27 | ISPR_UDF_UDEYLM | NUMERIC | 8 | 2 | Employee annual deduction limit |
| 28 | ISPR_UDF_UODLMT | NUMERIC | 8 | 4 | Deduction per-period limit |
| 29 | ISPR_UDF_UODYLM | NUMERIC | 8 | 2 | Deduction annual limit |
| 30 | ISPR_UDF_VEND | STRING | 10 | — | Vendor code for deduction payments |
| 31 | ISPR_UDF_WC | STRING | 1 | — | Workers comp applicable flag (Y/N) |
