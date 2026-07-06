# JC — Job Costing: Field Reference

Status: verified-schema + completed field meanings (Pass 574k, 2026-07-06).

Source: `Evo-DBA_File_Fields 052421.xlsx`, sheet "Fields".

WOLABRPT shares the MTWOLA_* prefix with WOELABOR in the DI module (fields-di.md).
BKPRMSTR is the payroll employee master with standard payroll accumulators:
QTD = quarter-to-date, YTD = year-to-date. RA=regular amount, RH=regular hours,
SA=sick amount, SH=sick hours, VA=vacation amount, VH=vacation hours,
OA_1..12/OH_1..12 = user-defined other pay types.
UDE_1..20 = user-defined earnings; UOD_1..20 = user-defined other deductions.

---

## BKPRMSTR
**JOB COST EMPLOYEE MASTER** — employee payroll master for job costing and payroll processing

Fields: 384 | Key: BKPR_EMP_NUM

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKPR_EMP_ADD | STRING | 30 | — | Street address |
| 2 | BKPR_EMP_ADDIT_1 | NUMERIC | 8 | 2 | Additional flat deduction amount 1 |
| 3 | BKPR_EMP_ADDIT_2 | NUMERIC | 8 | 2 | Additional flat deduction amount 2 |
| 4 | BKPR_EMP_ADDIT_3 | NUMERIC | 8 | 2 | Additional flat deduction amount 3 |
| 5 | BKPR_EMP_BANKA | STRING | 17 | — | Bank account number (ACH direct deposit) |
| 6 | BKPR_EMP_BANKR | STRING | 9 | — | Bank routing number (ABA) |
| 7 | BKPR_EMP_BDAY | DATE | 4 | — | Birth date |
| 8 | BKPR_EMP_BENDTE | DATE | 4 | — | Benefits end date |
| 9 | BKPR_EMP_CNTRY | STRING | 30 | — | Country |
| 10 | BKPR_EMP_CSZ | STRING | 25 | — | City, state, zip (combined) |
| 11 | BKPR_EMP_DEPT | STRING | 4 | — | Department code |
| 12 | BKPR_EMP_EIC | NUMERIC | 8 | 2 | Earned Income Credit (EIC) refund amount |
| 13 | BKPR_EMP_EICAMT | NUMERIC | 8 | 2 | EIC advance amount per pay period |
| 14 | BKPR_EMP_EMAIL | STRING | 128 | — | Email address |
| 15 | BKPR_EMP_EXPACT_1 | STRING | 10 | — | Expense allocation GL account 1 (labor cost posting account) |
| 16 | BKPR_EMP_EXPACT_10 | STRING | 10 | — | Expense allocation GL account 10 |
| 17 | BKPR_EMP_EXPACT_11 | STRING | 10 | — | Expense allocation GL account 11 |
| 18 | BKPR_EMP_EXPACT_12 | STRING | 10 | — | Expense allocation GL account 12 |
| 19 | BKPR_EMP_EXPACT_13 | STRING | 10 | — | Expense allocation GL account 13 |
| 20 | BKPR_EMP_EXPACT_14 | STRING | 10 | — | Expense allocation GL account 14 |
| 21 | BKPR_EMP_EXPACT_15 | STRING | 10 | — | Expense allocation GL account 15 |
| 22 | BKPR_EMP_EXPACT_2 | STRING | 10 | — | Expense allocation GL account 2 |
| 23 | BKPR_EMP_EXPACT_3 | STRING | 10 | — | Expense allocation GL account 3 |
| 24 | BKPR_EMP_EXPACT_4 | STRING | 10 | — | Expense allocation GL account 4 |
| 25 | BKPR_EMP_EXPACT_5 | STRING | 10 | — | Expense allocation GL account 5 |
| 26 | BKPR_EMP_EXPACT_6 | STRING | 10 | — | Expense allocation GL account 6 |
| 27 | BKPR_EMP_EXPACT_7 | STRING | 10 | — | Expense allocation GL account 7 |
| 28 | BKPR_EMP_EXPACT_8 | STRING | 10 | — | Expense allocation GL account 8 |
| 29 | BKPR_EMP_EXPACT_9 | STRING | 10 | — | Expense allocation GL account 9 |
| 30 | BKPR_EMP_EXPDPT_1 | STRING | 4 | — | Expense allocation GL department 1 |
| 31 | BKPR_EMP_EXPDPT_10 | STRING | 4 | — | Expense allocation GL department 10 |
| 32 | BKPR_EMP_EXPDPT_11 | STRING | 4 | — | Expense allocation GL department 11 |
| 33 | BKPR_EMP_EXPDPT_12 | STRING | 4 | — | Expense allocation GL department 12 |
| 34 | BKPR_EMP_EXPDPT_13 | STRING | 4 | — | Expense allocation GL department 13 |
| 35 | BKPR_EMP_EXPDPT_14 | STRING | 4 | — | Expense allocation GL department 14 |
| 36 | BKPR_EMP_EXPDPT_15 | STRING | 4 | — | Expense allocation GL department 15 |
| 37 | BKPR_EMP_EXPDPT_2 | STRING | 4 | — | Expense allocation GL department 2 |
| 38 | BKPR_EMP_EXPDPT_3 | STRING | 4 | — | Expense allocation GL department 3 |
| 39 | BKPR_EMP_EXPDPT_4 | STRING | 4 | — | Expense allocation GL department 4 |
| 40 | BKPR_EMP_EXPDPT_5 | STRING | 4 | — | Expense allocation GL department 5 |
| 41 | BKPR_EMP_EXPDPT_6 | STRING | 4 | — | Expense allocation GL department 6 |
| 42 | BKPR_EMP_EXPDPT_7 | STRING | 4 | — | Expense allocation GL department 7 |
| 43 | BKPR_EMP_EXPDPT_8 | STRING | 4 | — | Expense allocation GL department 8 |
| 44 | BKPR_EMP_EXPDPT_9 | STRING | 4 | — | Expense allocation GL department 9 |
| 45 | BKPR_EMP_EXTRA | STRING | 200 | — | Extra data |
| 46 | BKPR_EMP_FEDEXM | INTEGER | 2 | — | Federal tax exemptions / W-4 allowances |
| 47 | BKPR_EMP_FICQTD_1 | NUMERIC | 8 | 2 | FICA employee share — quarter-to-date |
| 48 | BKPR_EMP_FICQTD_2 | NUMERIC | 8 | 2 | FICA employer share — quarter-to-date |
| 49 | BKPR_EMP_FICYTD_1 | NUMERIC | 8 | 2 | FICA employee share — year-to-date |
| 50 | BKPR_EMP_FICYTD_2 | NUMERIC | 8 | 2 | FICA employer share — year-to-date |
| 51 | BKPR_EMP_FITQTD | NUMERIC | 8 | 2 | Federal income tax withheld — quarter-to-date |
| 52 | BKPR_EMP_FITYTD | NUMERIC | 8 | 2 | Federal income tax withheld — year-to-date |
| 53 | BKPR_EMP_FNMI | STRING | 25 | — | First name and middle initial |
| 54 | BKPR_EMP_LNME | STRING | 25 | — | Last name |
| 55 | BKPR_EMP_LOCCOD | STRING | 2 | — | Locality code (for local income tax) |
| 56 | BKPR_EMP_LSTPR | DATE | 4 | — | Last payroll date |
| 57 | BKPR_EMP_MDACT | STRING | 10 | — | Medicare GL account code |
| 58 | BKPR_EMP_MDAMT | NUMERIC | 8 | 2 | Medicare withholding amount per period |
| 59 | BKPR_EMP_MDDPT | STRING | 4 | — | Medicare GL department code |
| 60 | BKPR_EMP_MDNME | STRING | 12 | — | Medicare deduction name (label) |
| 61 | BKPR_EMP_MDQTD | NUMERIC | 8 | 2 | Medicare withheld — quarter-to-date |
| 62 | BKPR_EMP_MDYTD | NUMERIC | 8 | 2 | Medicare withheld — year-to-date |
| 63 | BKPR_EMP_MS | STRING | 1 | — | Marital status (`S`=single / `M`=married) |
| 64 | BKPR_EMP_NUM | INTEGER | 2 | — | Employee number (PK) |
| 65 | BKPR_EMP_OAQTD_1 | NUMERIC | 8 | 2 | Other pay type 1 — amount quarter-to-date |
| 66 | BKPR_EMP_OAQTD_10 | NUMERIC | 8 | 2 | Other pay type 10 — amount quarter-to-date |
| 67 | BKPR_EMP_OAQTD_11 | NUMERIC | 8 | 2 | Other pay type 11 — amount quarter-to-date |
| 68 | BKPR_EMP_OAQTD_12 | NUMERIC | 8 | 2 | Other pay type 12 — amount quarter-to-date |
| 69 | BKPR_EMP_OAQTD_2 | NUMERIC | 8 | 2 | Other pay type 2 — amount quarter-to-date |
| 70 | BKPR_EMP_OAQTD_3 | NUMERIC | 8 | 2 | Other pay type 3 — amount quarter-to-date |
| 71 | BKPR_EMP_OAQTD_4 | NUMERIC | 8 | 2 | Other pay type 4 — amount quarter-to-date |
| 72 | BKPR_EMP_OAQTD_5 | NUMERIC | 8 | 2 | Other pay type 5 — amount quarter-to-date |
| 73 | BKPR_EMP_OAQTD_6 | NUMERIC | 8 | 2 | Other pay type 6 — amount quarter-to-date |
| 74 | BKPR_EMP_OAQTD_7 | NUMERIC | 8 | 2 | Other pay type 7 — amount quarter-to-date |
| 75 | BKPR_EMP_OAQTD_8 | NUMERIC | 8 | 2 | Other pay type 8 — amount quarter-to-date |
| 76 | BKPR_EMP_OAQTD_9 | NUMERIC | 8 | 2 | Other pay type 9 — amount quarter-to-date |
| 77 | BKPR_EMP_OAYTD_1 | NUMERIC | 8 | 2 | Other pay type 1 — amount year-to-date |
| 78 | BKPR_EMP_OAYTD_10 | NUMERIC | 8 | 2 | Other pay type 10 — amount year-to-date |
| 79 | BKPR_EMP_OAYTD_11 | NUMERIC | 8 | 2 | Other pay type 11 — amount year-to-date |
| 80 | BKPR_EMP_OAYTD_12 | NUMERIC | 8 | 2 | Other pay type 12 — amount year-to-date |
| 81 | BKPR_EMP_OAYTD_2 | NUMERIC | 8 | 2 | Other pay type 2 — amount year-to-date |
| 82 | BKPR_EMP_OAYTD_3 | NUMERIC | 8 | 2 | Other pay type 3 — amount year-to-date |
| 83 | BKPR_EMP_OAYTD_4 | NUMERIC | 8 | 2 | Other pay type 4 — amount year-to-date |
| 84 | BKPR_EMP_OAYTD_5 | NUMERIC | 8 | 2 | Other pay type 5 — amount year-to-date |
| 85 | BKPR_EMP_OAYTD_6 | NUMERIC | 8 | 2 | Other pay type 6 — amount year-to-date |
| 86 | BKPR_EMP_OAYTD_7 | NUMERIC | 8 | 2 | Other pay type 7 — amount year-to-date |
| 87 | BKPR_EMP_OAYTD_8 | NUMERIC | 8 | 2 | Other pay type 8 — amount year-to-date |
| 88 | BKPR_EMP_OAYTD_9 | NUMERIC | 8 | 2 | Other pay type 9 — amount year-to-date |
| 89 | BKPR_EMP_OHQTD_1 | NUMERIC | 8 | 2 | Other pay type 1 — hours quarter-to-date |
| 90 | BKPR_EMP_OHQTD_10 | NUMERIC | 8 | 2 | Other pay type 10 — hours quarter-to-date |
| 91 | BKPR_EMP_OHQTD_11 | NUMERIC | 8 | 2 | Other pay type 11 — hours quarter-to-date |
| 92 | BKPR_EMP_OHQTD_12 | NUMERIC | 8 | 2 | Other pay type 12 — hours quarter-to-date |
| 93 | BKPR_EMP_OHQTD_2 | NUMERIC | 8 | 2 | Other pay type 2 — hours quarter-to-date |
| 94 | BKPR_EMP_OHQTD_3 | NUMERIC | 8 | 2 | Other pay type 3 — hours quarter-to-date |
| 95 | BKPR_EMP_OHQTD_4 | NUMERIC | 8 | 2 | Other pay type 4 — hours quarter-to-date |
| 96 | BKPR_EMP_OHQTD_5 | NUMERIC | 8 | 2 | Other pay type 5 — hours quarter-to-date |
| 97 | BKPR_EMP_OHQTD_6 | NUMERIC | 8 | 2 | Other pay type 6 — hours quarter-to-date |
| 98 | BKPR_EMP_OHQTD_7 | NUMERIC | 8 | 2 | Other pay type 7 — hours quarter-to-date |
| 99 | BKPR_EMP_OHQTD_8 | NUMERIC | 8 | 2 | Other pay type 8 — hours quarter-to-date |
| 100 | BKPR_EMP_OHQTD_9 | NUMERIC | 8 | 2 | Other pay type 9 — hours quarter-to-date |
| 101 | BKPR_EMP_OHYTD_1 | NUMERIC | 8 | 2 | Other pay type 1 — hours year-to-date |
| 102 | BKPR_EMP_OHYTD_10 | NUMERIC | 8 | 2 | Other pay type 10 — hours year-to-date |
| 103 | BKPR_EMP_OHYTD_11 | NUMERIC | 8 | 2 | Other pay type 11 — hours year-to-date |
| 104 | BKPR_EMP_OHYTD_12 | NUMERIC | 8 | 2 | Other pay type 12 — hours year-to-date |
| 105 | BKPR_EMP_OHYTD_2 | NUMERIC | 8 | 2 | Other pay type 2 — hours year-to-date |
| 106 | BKPR_EMP_OHYTD_3 | NUMERIC | 8 | 2 | Other pay type 3 — hours year-to-date |
| 107 | BKPR_EMP_OHYTD_4 | NUMERIC | 8 | 2 | Other pay type 4 — hours year-to-date |
| 108 | BKPR_EMP_OHYTD_5 | NUMERIC | 8 | 2 | Other pay type 5 — hours year-to-date |
| 109 | BKPR_EMP_OHYTD_6 | NUMERIC | 8 | 2 | Other pay type 6 — hours year-to-date |
| 110 | BKPR_EMP_OHYTD_7 | NUMERIC | 8 | 2 | Other pay type 7 — hours year-to-date |
| 111 | BKPR_EMP_OHYTD_8 | NUMERIC | 8 | 2 | Other pay type 8 — hours year-to-date |
| 112 | BKPR_EMP_OHYTD_9 | NUMERIC | 8 | 2 | Other pay type 9 — hours year-to-date |
| 113 | BKPR_EMP_OPNAME_1 | STRING | 10 | — | User-defined other pay type name 1 (e.g. "Holiday") |
| 114 | BKPR_EMP_OPNAME_2 | STRING | 10 | — | User-defined other pay type name 2 |
| 115 | BKPR_EMP_OPNAME_3 | STRING | 10 | — | User-defined other pay type name 3 |
| 116 | BKPR_EMP_OPNAME_4 | STRING | 10 | — | User-defined other pay type name 4 |
| 117 | BKPR_EMP_OPNAME_5 | STRING | 10 | — | User-defined other pay type name 5 |
| 118 | BKPR_EMP_OTHACT | STRING | 10 | — | Other deduction GL account code |
| 119 | BKPR_EMP_OTHAMT | NUMERIC | 8 | 2 | Other deduction flat amount per period |
| 120 | BKPR_EMP_OTHDPT | STRING | 4 | — | Other deduction GL department code |
| 121 | BKPR_EMP_OTHNME | STRING | 12 | — | Other deduction name (label) |
| 122 | BKPR_EMP_OTHQTD | NUMERIC | 8 | 2 | Other deduction — quarter-to-date |
| 123 | BKPR_EMP_OTHYTD | NUMERIC | 8 | 2 | Other deduction — year-to-date |
| 124 | BKPR_EMP_PAYAMT_1 | NUMERIC | 8 | 4 | Pay rate / amount for pay type 1 |
| 125 | BKPR_EMP_PAYAMT_10 | NUMERIC | 8 | 4 | Pay rate / amount for pay type 10 |
| 126 | BKPR_EMP_PAYAMT_11 | NUMERIC | 8 | 4 | Pay rate / amount for pay type 11 |
| 127 | BKPR_EMP_PAYAMT_12 | NUMERIC | 8 | 4 | Pay rate / amount for pay type 12 |
| 128 | BKPR_EMP_PAYAMT_13 | NUMERIC | 8 | 4 | Pay rate / amount for pay type 13 |
| 129 | BKPR_EMP_PAYAMT_14 | NUMERIC | 8 | 4 | Pay rate / amount for pay type 14 |
| 130 | BKPR_EMP_PAYAMT_15 | NUMERIC | 8 | 4 | Pay rate / amount for pay type 15 |
| 131 | BKPR_EMP_PAYAMT_2 | NUMERIC | 8 | 4 | Pay rate / amount for pay type 2 |
| 132 | BKPR_EMP_PAYAMT_3 | NUMERIC | 8 | 4 | Pay rate / amount for pay type 3 |
| 133 | BKPR_EMP_PAYAMT_4 | NUMERIC | 8 | 4 | Pay rate / amount for pay type 4 |
| 134 | BKPR_EMP_PAYAMT_5 | NUMERIC | 8 | 4 | Pay rate / amount for pay type 5 |
| 135 | BKPR_EMP_PAYAMT_6 | NUMERIC | 8 | 4 | Pay rate / amount for pay type 6 |
| 136 | BKPR_EMP_PAYAMT_7 | NUMERIC | 8 | 4 | Pay rate / amount for pay type 7 |
| 137 | BKPR_EMP_PAYAMT_8 | NUMERIC | 8 | 4 | Pay rate / amount for pay type 8 |
| 138 | BKPR_EMP_PAYAMT_9 | NUMERIC | 8 | 4 | Pay rate / amount for pay type 9 |
| 139 | BKPR_EMP_PAYTYP | STRING | 1 | — | Pay type code (`H`=hourly / `S`=salaried) |
| 140 | BKPR_EMP_PHONE | STRING | 15 | — | Phone number |
| 141 | BKPR_EMP_QTR | INTEGER | 2 | — | Current quarter number (1–4) |
| 142 | BKPR_EMP_RAQTD | NUMERIC | 8 | 2 | Regular pay amount — quarter-to-date |
| 143 | BKPR_EMP_RAYTD | NUMERIC | 8 | 2 | Regular pay amount — year-to-date |
| 144 | BKPR_EMP_RHQTD | NUMERIC | 8 | 2 | Regular hours — quarter-to-date |
| 145 | BKPR_EMP_RHYTD | NUMERIC | 8 | 2 | Regular hours — year-to-date |
| 146 | BKPR_EMP_SAQTD | NUMERIC | 8 | 2 | Sick pay amount — quarter-to-date |
| 147 | BKPR_EMP_SAYTD | NUMERIC | 8 | 2 | Sick pay amount — year-to-date |
| 148 | BKPR_EMP_SCAP | NUMERIC | 8 | 2 | Sick hours accrual cap (maximum hours) |
| 149 | BKPR_EMP_SDATE | DATE | 4 | — | Start / hire date |
| 150 | BKPR_EMP_SDIEXM | STRING | 1 | — | SDI exempt flag (`Y`=exempt from state disability insurance) |
| 151 | BKPR_EMP_SDIQTD | NUMERIC | 8 | 2 | State Disability Insurance withheld — quarter-to-date |
| 152 | BKPR_EMP_SDIYTD | NUMERIC | 8 | 2 | State Disability Insurance withheld — year-to-date |
| 153 | BKPR_EMP_SDUE | NUMERIC | 8 | 2 | Sick hours accrued / due |
| 154 | BKPR_EMP_SHIFT | INTEGER | 2 | — | Default shift assignment (1/2/3) |
| 155 | BKPR_EMP_SHQTD | NUMERIC | 8 | 2 | Sick hours used — quarter-to-date |
| 156 | BKPR_EMP_SHYTD | NUMERIC | 8 | 2 | Sick hours used — year-to-date |
| 157 | BKPR_EMP_SRTE | NUMERIC | 8 | 4 | Sick pay hourly rate |
| 158 | BKPR_EMP_SSN | STRING | 11 | — | Social Security Number |
| 159 | BKPR_EMP_ST | STRING | 2 | — | State code (for state income tax) |
| 160 | BKPR_EMP_STEXM | INTEGER | 2 | — | State tax exemptions (number of allowances) |
| 161 | BKPR_EMP_STEXMA | NUMERIC | 8 | — | State tax additional exemption amount |
| 162 | BKPR_EMP_STEXMN | INTEGER | 2 | — | Number of state exemption dependents |
| 163 | BKPR_EMP_STQTD | NUMERIC | 8 | 2 | State income tax withheld — quarter-to-date |
| 164 | BKPR_EMP_STYTD | NUMERIC | 8 | 2 | State income tax withheld — year-to-date |
| 165 | BKPR_EMP_TERM | STRING | 1 | — | Terminated flag (`Y`=no longer active) |
| 166 | BKPR_EMP_UDAMT1_1 | NUMERIC | 8 | 2 | User-defined amount set 1, field 1 |
| 167 | BKPR_EMP_UDAMT1_2 | NUMERIC | 8 | 2 | User-defined amount set 1, field 2 |
| 168 | BKPR_EMP_UDAMT1_3 | NUMERIC | 8 | 2 | User-defined amount set 1, field 3 |
| 169 | BKPR_EMP_UDAMT1_4 | NUMERIC | 8 | 2 | User-defined amount set 1, field 4 |
| 170 | BKPR_EMP_UDAMT1_5 | NUMERIC | 8 | 2 | User-defined amount set 1, field 5 |
| 171 | BKPR_EMP_UDAMT1_6 | NUMERIC | 8 | 2 | User-defined amount set 1, field 6 |
| 172 | BKPR_EMP_UDEAMT_1 | NUMERIC | 8 | 4 | User-defined earnings type 1 — rate / amount per period |
| 173 | BKPR_EMP_UDEAMT_10 | NUMERIC | 8 | 4 | User-defined earnings type 10 — rate |
| 174 | BKPR_EMP_UDEAMT_11 | NUMERIC | 8 | 4 | User-defined earnings type 11 — rate |
| 175 | BKPR_EMP_UDEAMT_12 | NUMERIC | 8 | 4 | User-defined earnings type 12 — rate |
| 176 | BKPR_EMP_UDEAMT_13 | NUMERIC | 8 | 4 | User-defined earnings type 13 — rate |
| 177 | BKPR_EMP_UDEAMT_14 | NUMERIC | 8 | 4 | User-defined earnings type 14 — rate |
| 178 | BKPR_EMP_UDEAMT_15 | NUMERIC | 8 | 4 | User-defined earnings type 15 — rate |
| 179 | BKPR_EMP_UDEAMT_16 | NUMERIC | 8 | 4 | User-defined earnings type 16 — rate |
| 180 | BKPR_EMP_UDEAMT_17 | NUMERIC | 8 | 4 | User-defined earnings type 17 — rate |
| 181 | BKPR_EMP_UDEAMT_18 | NUMERIC | 8 | 4 | User-defined earnings type 18 — rate |
| 182 | BKPR_EMP_UDEAMT_19 | NUMERIC | 8 | 4 | User-defined earnings type 19 — rate |
| 183 | BKPR_EMP_UDEAMT_2 | NUMERIC | 8 | 4 | User-defined earnings type 2 — rate |
| 184 | BKPR_EMP_UDEAMT_20 | NUMERIC | 8 | 4 | User-defined earnings type 20 — rate |
| 185 | BKPR_EMP_UDEAMT_3 | NUMERIC | 8 | 4 | User-defined earnings type 3 — rate |
| 186 | BKPR_EMP_UDEAMT_4 | NUMERIC | 8 | 4 | User-defined earnings type 4 — rate |
| 187 | BKPR_EMP_UDEAMT_5 | NUMERIC | 8 | 4 | User-defined earnings type 5 — rate |
| 188 | BKPR_EMP_UDEAMT_6 | NUMERIC | 8 | 4 | User-defined earnings type 6 — rate |
| 189 | BKPR_EMP_UDEAMT_7 | NUMERIC | 8 | 4 | User-defined earnings type 7 — rate |
| 190 | BKPR_EMP_UDEAMT_8 | NUMERIC | 8 | 4 | User-defined earnings type 8 — rate |
| 191 | BKPR_EMP_UDEAMT_9 | NUMERIC | 8 | 4 | User-defined earnings type 9 — rate |
| 192 | BKPR_EMP_UDELMT_1 | NUMERIC | 8 | 4 | User-defined earnings type 1 — per-period limit |
| 193 | BKPR_EMP_UDELMT_10 | NUMERIC | 8 | 4 | User-defined earnings type 10 — per-period limit |
| 194 | BKPR_EMP_UDELMT_11 | NUMERIC | 8 | 4 | User-defined earnings type 11 — per-period limit |
| 195 | BKPR_EMP_UDELMT_12 | NUMERIC | 8 | 4 | User-defined earnings type 12 — per-period limit |
| 196 | BKPR_EMP_UDELMT_13 | NUMERIC | 8 | 4 | User-defined earnings type 13 — per-period limit |
| 197 | BKPR_EMP_UDELMT_14 | NUMERIC | 8 | 4 | User-defined earnings type 14 — per-period limit |
| 198 | BKPR_EMP_UDELMT_15 | NUMERIC | 8 | 4 | User-defined earnings type 15 — per-period limit |
| 199 | BKPR_EMP_UDELMT_16 | NUMERIC | 8 | 4 | User-defined earnings type 16 — per-period limit |
| 200 | BKPR_EMP_UDELMT_17 | NUMERIC | 8 | 4 | User-defined earnings type 17 — per-period limit |
| 201 | BKPR_EMP_UDELMT_18 | NUMERIC | 8 | 4 | User-defined earnings type 18 — per-period limit |
| 202 | BKPR_EMP_UDELMT_19 | NUMERIC | 8 | 4 | User-defined earnings type 19 — per-period limit |
| 203 | BKPR_EMP_UDELMT_2 | NUMERIC | 8 | 4 | User-defined earnings type 2 — per-period limit |
| 204 | BKPR_EMP_UDELMT_20 | NUMERIC | 8 | 4 | User-defined earnings type 20 — per-period limit |
| 205 | BKPR_EMP_UDELMT_3 | NUMERIC | 8 | 4 | User-defined earnings type 3 — per-period limit |
| 206 | BKPR_EMP_UDELMT_4 | NUMERIC | 8 | 4 | User-defined earnings type 4 — per-period limit |
| 207 | BKPR_EMP_UDELMT_5 | NUMERIC | 8 | 4 | User-defined earnings type 5 — per-period limit |
| 208 | BKPR_EMP_UDELMT_6 | NUMERIC | 8 | 4 | User-defined earnings type 6 — per-period limit |
| 209 | BKPR_EMP_UDELMT_7 | NUMERIC | 8 | 4 | User-defined earnings type 7 — per-period limit |
| 210 | BKPR_EMP_UDELMT_8 | NUMERIC | 8 | 4 | User-defined earnings type 8 — per-period limit |
| 211 | BKPR_EMP_UDELMT_9 | NUMERIC | 8 | 4 | User-defined earnings type 9 — per-period limit |
| 212 | BKPR_EMP_UDEQTD_1 | NUMERIC | 8 | 2 | User-defined earnings type 1 — quarter-to-date |
| 213 | BKPR_EMP_UDEQTD_10 | NUMERIC | 8 | 2 | User-defined earnings type 10 — quarter-to-date |
| 214 | BKPR_EMP_UDEQTD_11 | NUMERIC | 8 | 2 | User-defined earnings type 11 — quarter-to-date |
| 215 | BKPR_EMP_UDEQTD_12 | NUMERIC | 8 | 2 | User-defined earnings type 12 — quarter-to-date |
| 216 | BKPR_EMP_UDEQTD_13 | NUMERIC | 8 | 2 | User-defined earnings type 13 — quarter-to-date |
| 217 | BKPR_EMP_UDEQTD_14 | NUMERIC | 8 | 2 | User-defined earnings type 14 — quarter-to-date |
| 218 | BKPR_EMP_UDEQTD_15 | NUMERIC | 8 | 2 | User-defined earnings type 15 — quarter-to-date |
| 219 | BKPR_EMP_UDEQTD_16 | NUMERIC | 8 | 2 | User-defined earnings type 16 — quarter-to-date |
| 220 | BKPR_EMP_UDEQTD_17 | NUMERIC | 8 | 2 | User-defined earnings type 17 — quarter-to-date |
| 221 | BKPR_EMP_UDEQTD_18 | NUMERIC | 8 | 2 | User-defined earnings type 18 — quarter-to-date |
| 222 | BKPR_EMP_UDEQTD_19 | NUMERIC | 8 | 2 | User-defined earnings type 19 — quarter-to-date |
| 223 | BKPR_EMP_UDEQTD_2 | NUMERIC | 8 | 2 | User-defined earnings type 2 — quarter-to-date |
| 224 | BKPR_EMP_UDEQTD_20 | NUMERIC | 8 | 2 | User-defined earnings type 20 — quarter-to-date |
| 225 | BKPR_EMP_UDEQTD_3 | NUMERIC | 8 | 2 | User-defined earnings type 3 — quarter-to-date |
| 226 | BKPR_EMP_UDEQTD_4 | NUMERIC | 8 | 2 | User-defined earnings type 4 — quarter-to-date |
| 227 | BKPR_EMP_UDEQTD_5 | NUMERIC | 8 | 2 | User-defined earnings type 5 — quarter-to-date |
| 228 | BKPR_EMP_UDEQTD_6 | NUMERIC | 8 | 2 | User-defined earnings type 6 — quarter-to-date |
| 229 | BKPR_EMP_UDEQTD_7 | NUMERIC | 8 | 2 | User-defined earnings type 7 — quarter-to-date |
| 230 | BKPR_EMP_UDEQTD_8 | NUMERIC | 8 | 2 | User-defined earnings type 8 — quarter-to-date |
| 231 | BKPR_EMP_UDEQTD_9 | NUMERIC | 8 | 2 | User-defined earnings type 9 — quarter-to-date |
| 232 | BKPR_EMP_UDEYLM_1 | NUMERIC | 8 | 2 | User-defined earnings type 1 — annual limit (cap) |
| 233 | BKPR_EMP_UDEYLM_10 | NUMERIC | 8 | 2 | User-defined earnings type 10 — annual limit |
| 234 | BKPR_EMP_UDEYLM_11 | NUMERIC | 8 | 2 | User-defined earnings type 11 — annual limit |
| 235 | BKPR_EMP_UDEYLM_12 | NUMERIC | 8 | 2 | User-defined earnings type 12 — annual limit |
| 236 | BKPR_EMP_UDEYLM_13 | NUMERIC | 8 | 2 | User-defined earnings type 13 — annual limit |
| 237 | BKPR_EMP_UDEYLM_14 | NUMERIC | 8 | 2 | User-defined earnings type 14 — annual limit |
| 238 | BKPR_EMP_UDEYLM_15 | NUMERIC | 8 | 2 | User-defined earnings type 15 — annual limit |
| 239 | BKPR_EMP_UDEYLM_16 | NUMERIC | 8 | 2 | User-defined earnings type 16 — annual limit |
| 240 | BKPR_EMP_UDEYLM_17 | NUMERIC | 8 | 2 | User-defined earnings type 17 — annual limit |
| 241 | BKPR_EMP_UDEYLM_18 | NUMERIC | 8 | 2 | User-defined earnings type 18 — annual limit |
| 242 | BKPR_EMP_UDEYLM_19 | NUMERIC | 8 | 2 | User-defined earnings type 19 — annual limit |
| 243 | BKPR_EMP_UDEYLM_2 | NUMERIC | 8 | 2 | User-defined earnings type 2 — annual limit |
| 244 | BKPR_EMP_UDEYLM_20 | NUMERIC | 8 | 2 | User-defined earnings type 20 — annual limit |
| 245 | BKPR_EMP_UDEYLM_3 | NUMERIC | 8 | 2 | User-defined earnings type 3 — annual limit |
| 246 | BKPR_EMP_UDEYLM_4 | NUMERIC | 8 | 2 | User-defined earnings type 4 — annual limit |
| 247 | BKPR_EMP_UDEYLM_5 | NUMERIC | 8 | 2 | User-defined earnings type 5 — annual limit |
| 248 | BKPR_EMP_UDEYLM_6 | NUMERIC | 8 | 2 | User-defined earnings type 6 — annual limit |
| 249 | BKPR_EMP_UDEYLM_7 | NUMERIC | 8 | 2 | User-defined earnings type 7 — annual limit |
| 250 | BKPR_EMP_UDEYLM_8 | NUMERIC | 8 | 2 | User-defined earnings type 8 — annual limit |
| 251 | BKPR_EMP_UDEYLM_9 | NUMERIC | 8 | 2 | User-defined earnings type 9 — annual limit |
| 252 | BKPR_EMP_UDEYTD_1 | NUMERIC | 8 | 2 | User-defined earnings type 1 — year-to-date |
| 253 | BKPR_EMP_UDEYTD_10 | NUMERIC | 8 | 2 | User-defined earnings type 10 — year-to-date |
| 254 | BKPR_EMP_UDEYTD_11 | NUMERIC | 8 | 2 | User-defined earnings type 11 — year-to-date |
| 255 | BKPR_EMP_UDEYTD_12 | NUMERIC | 8 | 2 | User-defined earnings type 12 — year-to-date |
| 256 | BKPR_EMP_UDEYTD_13 | NUMERIC | 8 | 2 | User-defined earnings type 13 — year-to-date |
| 257 | BKPR_EMP_UDEYTD_14 | NUMERIC | 8 | 2 | User-defined earnings type 14 — year-to-date |
| 258 | BKPR_EMP_UDEYTD_15 | NUMERIC | 8 | 2 | User-defined earnings type 15 — year-to-date |
| 259 | BKPR_EMP_UDEYTD_16 | NUMERIC | 8 | 2 | User-defined earnings type 16 — year-to-date |
| 260 | BKPR_EMP_UDEYTD_17 | NUMERIC | 8 | 2 | User-defined earnings type 17 — year-to-date |
| 261 | BKPR_EMP_UDEYTD_18 | NUMERIC | 8 | 2 | User-defined earnings type 18 — year-to-date |
| 262 | BKPR_EMP_UDEYTD_19 | NUMERIC | 8 | 2 | User-defined earnings type 19 — year-to-date |
| 263 | BKPR_EMP_UDEYTD_2 | NUMERIC | 8 | 2 | User-defined earnings type 2 — year-to-date |
| 264 | BKPR_EMP_UDEYTD_20 | NUMERIC | 8 | 2 | User-defined earnings type 20 — year-to-date |
| 265 | BKPR_EMP_UDEYTD_3 | NUMERIC | 8 | 2 | User-defined earnings type 3 — year-to-date |
| 266 | BKPR_EMP_UDEYTD_4 | NUMERIC | 8 | 2 | User-defined earnings type 4 — year-to-date |
| 267 | BKPR_EMP_UDEYTD_5 | NUMERIC | 8 | 2 | User-defined earnings type 5 — year-to-date |
| 268 | BKPR_EMP_UDEYTD_6 | NUMERIC | 8 | 2 | User-defined earnings type 6 — year-to-date |
| 269 | BKPR_EMP_UDEYTD_7 | NUMERIC | 8 | 2 | User-defined earnings type 7 — year-to-date |
| 270 | BKPR_EMP_UDEYTD_8 | NUMERIC | 8 | 2 | User-defined earnings type 8 — year-to-date |
| 271 | BKPR_EMP_UDEYTD_9 | NUMERIC | 8 | 2 | User-defined earnings type 9 — year-to-date |
| 272 | BKPR_EMP_UODAMT_1 | NUMERIC | 8 | 4 | User-defined other deduction type 1 — per-period amount |
| 273 | BKPR_EMP_UODAMT_10 | NUMERIC | 8 | 4 | User-defined other deduction type 10 — per-period amount |
| 274 | BKPR_EMP_UODAMT_11 | NUMERIC | 8 | 4 | User-defined other deduction type 11 — per-period amount |
| 275 | BKPR_EMP_UODAMT_12 | NUMERIC | 8 | 4 | User-defined other deduction type 12 — per-period amount |
| 276 | BKPR_EMP_UODAMT_13 | NUMERIC | 8 | 4 | User-defined other deduction type 13 — per-period amount |
| 277 | BKPR_EMP_UODAMT_14 | NUMERIC | 8 | 4 | User-defined other deduction type 14 — per-period amount |
| 278 | BKPR_EMP_UODAMT_15 | NUMERIC | 8 | 4 | User-defined other deduction type 15 — per-period amount |
| 279 | BKPR_EMP_UODAMT_16 | NUMERIC | 8 | 4 | User-defined other deduction type 16 — per-period amount |
| 280 | BKPR_EMP_UODAMT_17 | NUMERIC | 8 | 4 | User-defined other deduction type 17 — per-period amount |
| 281 | BKPR_EMP_UODAMT_18 | NUMERIC | 8 | 4 | User-defined other deduction type 18 — per-period amount |
| 282 | BKPR_EMP_UODAMT_19 | NUMERIC | 8 | 4 | User-defined other deduction type 19 — per-period amount |
| 283 | BKPR_EMP_UODAMT_2 | NUMERIC | 8 | 4 | User-defined other deduction type 2 — per-period amount |
| 284 | BKPR_EMP_UODAMT_20 | NUMERIC | 8 | 4 | User-defined other deduction type 20 — per-period amount |
| 285 | BKPR_EMP_UODAMT_3 | NUMERIC | 8 | 4 | User-defined other deduction type 3 — per-period amount |
| 286 | BKPR_EMP_UODAMT_4 | NUMERIC | 8 | 4 | User-defined other deduction type 4 — per-period amount |
| 287 | BKPR_EMP_UODAMT_5 | NUMERIC | 8 | 4 | User-defined other deduction type 5 — per-period amount |
| 288 | BKPR_EMP_UODAMT_6 | NUMERIC | 8 | 4 | User-defined other deduction type 6 — per-period amount |
| 289 | BKPR_EMP_UODAMT_7 | NUMERIC | 8 | 4 | User-defined other deduction type 7 — per-period amount |
| 290 | BKPR_EMP_UODAMT_8 | NUMERIC | 8 | 4 | User-defined other deduction type 8 — per-period amount |
| 291 | BKPR_EMP_UODAMT_9 | NUMERIC | 8 | 4 | User-defined other deduction type 9 — per-period amount |
| 292 | BKPR_EMP_UODLMT_1 | NUMERIC | 8 | 4 | User-defined other deduction type 1 — per-period limit |
| 293 | BKPR_EMP_UODLMT_10 | NUMERIC | 8 | 4 | User-defined other deduction type 10 — per-period limit |
| 294 | BKPR_EMP_UODLMT_11 | NUMERIC | 8 | 4 | User-defined other deduction type 11 — per-period limit |
| 295 | BKPR_EMP_UODLMT_12 | NUMERIC | 8 | 4 | User-defined other deduction type 12 — per-period limit |
| 296 | BKPR_EMP_UODLMT_13 | NUMERIC | 8 | 4 | User-defined other deduction type 13 — per-period limit |
| 297 | BKPR_EMP_UODLMT_14 | NUMERIC | 8 | 4 | User-defined other deduction type 14 — per-period limit |
| 298 | BKPR_EMP_UODLMT_15 | NUMERIC | 8 | 4 | User-defined other deduction type 15 — per-period limit |
| 299 | BKPR_EMP_UODLMT_16 | NUMERIC | 8 | 4 | User-defined other deduction type 16 — per-period limit |
| 300 | BKPR_EMP_UODLMT_17 | NUMERIC | 8 | 4 | User-defined other deduction type 17 — per-period limit |
| 301 | BKPR_EMP_UODLMT_18 | NUMERIC | 8 | 4 | User-defined other deduction type 18 — per-period limit |
| 302 | BKPR_EMP_UODLMT_19 | NUMERIC | 8 | 4 | User-defined other deduction type 19 — per-period limit |
| 303 | BKPR_EMP_UODLMT_2 | NUMERIC | 8 | 4 | User-defined other deduction type 2 — per-period limit |
| 304 | BKPR_EMP_UODLMT_20 | NUMERIC | 8 | 4 | User-defined other deduction type 20 — per-period limit |
| 305 | BKPR_EMP_UODLMT_3 | NUMERIC | 8 | 4 | User-defined other deduction type 3 — per-period limit |
| 306 | BKPR_EMP_UODLMT_4 | NUMERIC | 8 | 4 | User-defined other deduction type 4 — per-period limit |
| 307 | BKPR_EMP_UODLMT_5 | NUMERIC | 8 | 4 | User-defined other deduction type 5 — per-period limit |
| 308 | BKPR_EMP_UODLMT_6 | NUMERIC | 8 | 4 | User-defined other deduction type 6 — per-period limit |
| 309 | BKPR_EMP_UODLMT_7 | NUMERIC | 8 | 4 | User-defined other deduction type 7 — per-period limit |
| 310 | BKPR_EMP_UODLMT_8 | NUMERIC | 8 | 4 | User-defined other deduction type 8 — per-period limit |
| 311 | BKPR_EMP_UODLMT_9 | NUMERIC | 8 | 4 | User-defined other deduction type 9 — per-period limit |
| 312 | BKPR_EMP_UODQTD_1 | NUMERIC | 8 | 2 | User-defined other deduction type 1 — quarter-to-date |
| 313 | BKPR_EMP_UODQTD_10 | NUMERIC | 8 | 2 | User-defined other deduction type 10 — quarter-to-date |
| 314 | BKPR_EMP_UODQTD_11 | NUMERIC | 8 | 2 | User-defined other deduction type 11 — quarter-to-date |
| 315 | BKPR_EMP_UODQTD_12 | NUMERIC | 8 | 2 | User-defined other deduction type 12 — quarter-to-date |
| 316 | BKPR_EMP_UODQTD_13 | NUMERIC | 8 | 2 | User-defined other deduction type 13 — quarter-to-date |
| 317 | BKPR_EMP_UODQTD_14 | NUMERIC | 8 | 2 | User-defined other deduction type 14 — quarter-to-date |
| 318 | BKPR_EMP_UODQTD_15 | NUMERIC | 8 | 2 | User-defined other deduction type 15 — quarter-to-date |
| 319 | BKPR_EMP_UODQTD_16 | NUMERIC | 8 | 2 | User-defined other deduction type 16 — quarter-to-date |
| 320 | BKPR_EMP_UODQTD_17 | NUMERIC | 8 | 2 | User-defined other deduction type 17 — quarter-to-date |
| 321 | BKPR_EMP_UODQTD_18 | NUMERIC | 8 | 2 | User-defined other deduction type 18 — quarter-to-date |
| 322 | BKPR_EMP_UODQTD_19 | NUMERIC | 8 | 2 | User-defined other deduction type 19 — quarter-to-date |
| 323 | BKPR_EMP_UODQTD_2 | NUMERIC | 8 | 2 | User-defined other deduction type 2 — quarter-to-date |
| 324 | BKPR_EMP_UODQTD_20 | NUMERIC | 8 | 2 | User-defined other deduction type 20 — quarter-to-date |
| 325 | BKPR_EMP_UODQTD_3 | NUMERIC | 8 | 2 | User-defined other deduction type 3 — quarter-to-date |
| 326 | BKPR_EMP_UODQTD_4 | NUMERIC | 8 | 2 | User-defined other deduction type 4 — quarter-to-date |
| 327 | BKPR_EMP_UODQTD_5 | NUMERIC | 8 | 2 | User-defined other deduction type 5 — quarter-to-date |
| 328 | BKPR_EMP_UODQTD_6 | NUMERIC | 8 | 2 | User-defined other deduction type 6 — quarter-to-date |
| 329 | BKPR_EMP_UODQTD_7 | NUMERIC | 8 | 2 | User-defined other deduction type 7 — quarter-to-date |
| 330 | BKPR_EMP_UODQTD_8 | NUMERIC | 8 | 2 | User-defined other deduction type 8 — quarter-to-date |
| 331 | BKPR_EMP_UODQTD_9 | NUMERIC | 8 | 2 | User-defined other deduction type 9 — quarter-to-date |
| 332 | BKPR_EMP_UODYLM_1 | NUMERIC | 8 | 2 | User-defined other deduction type 1 — annual limit |
| 333 | BKPR_EMP_UODYLM_10 | NUMERIC | 8 | 2 | User-defined other deduction type 10 — annual limit |
| 334 | BKPR_EMP_UODYLM_11 | NUMERIC | 8 | 2 | User-defined other deduction type 11 — annual limit |
| 335 | BKPR_EMP_UODYLM_12 | NUMERIC | 8 | 2 | User-defined other deduction type 12 — annual limit |
| 336 | BKPR_EMP_UODYLM_13 | NUMERIC | 8 | 2 | User-defined other deduction type 13 — annual limit |
| 337 | BKPR_EMP_UODYLM_14 | NUMERIC | 8 | 2 | User-defined other deduction type 14 — annual limit |
| 338 | BKPR_EMP_UODYLM_15 | NUMERIC | 8 | 2 | User-defined other deduction type 15 — annual limit |
| 339 | BKPR_EMP_UODYLM_16 | NUMERIC | 8 | 2 | User-defined other deduction type 16 — annual limit |
| 340 | BKPR_EMP_UODYLM_17 | NUMERIC | 8 | 2 | User-defined other deduction type 17 — annual limit |
| 341 | BKPR_EMP_UODYLM_18 | NUMERIC | 8 | 2 | User-defined other deduction type 18 — annual limit |
| 342 | BKPR_EMP_UODYLM_19 | NUMERIC | 8 | 2 | User-defined other deduction type 19 — annual limit |
| 343 | BKPR_EMP_UODYLM_2 | NUMERIC | 8 | 2 | User-defined other deduction type 2 — annual limit |
| 344 | BKPR_EMP_UODYLM_20 | NUMERIC | 8 | 2 | User-defined other deduction type 20 — annual limit |
| 345 | BKPR_EMP_UODYLM_3 | NUMERIC | 8 | 2 | User-defined other deduction type 3 — annual limit |
| 346 | BKPR_EMP_UODYLM_4 | NUMERIC | 8 | 2 | User-defined other deduction type 4 — annual limit |
| 347 | BKPR_EMP_UODYLM_5 | NUMERIC | 8 | 2 | User-defined other deduction type 5 — annual limit |
| 348 | BKPR_EMP_UODYLM_6 | NUMERIC | 8 | 2 | User-defined other deduction type 6 — annual limit |
| 349 | BKPR_EMP_UODYLM_7 | NUMERIC | 8 | 2 | User-defined other deduction type 7 — annual limit |
| 350 | BKPR_EMP_UODYLM_8 | NUMERIC | 8 | 2 | User-defined other deduction type 8 — annual limit |
| 351 | BKPR_EMP_UODYLM_9 | NUMERIC | 8 | 2 | User-defined other deduction type 9 — annual limit |
| 352 | BKPR_EMP_UODYTD_1 | NUMERIC | 8 | 2 | User-defined other deduction type 1 — year-to-date |
| 353 | BKPR_EMP_UODYTD_10 | NUMERIC | 8 | 2 | User-defined other deduction type 10 — year-to-date |
| 354 | BKPR_EMP_UODYTD_11 | NUMERIC | 8 | 2 | User-defined other deduction type 11 — year-to-date |
| 355 | BKPR_EMP_UODYTD_12 | NUMERIC | 8 | 2 | User-defined other deduction type 12 — year-to-date |
| 356 | BKPR_EMP_UODYTD_13 | NUMERIC | 8 | 2 | User-defined other deduction type 13 — year-to-date |
| 357 | BKPR_EMP_UODYTD_14 | NUMERIC | 8 | 2 | User-defined other deduction type 14 — year-to-date |
| 358 | BKPR_EMP_UODYTD_15 | NUMERIC | 8 | 2 | User-defined other deduction type 15 — year-to-date |
| 359 | BKPR_EMP_UODYTD_16 | NUMERIC | 8 | 2 | User-defined other deduction type 16 — year-to-date |
| 360 | BKPR_EMP_UODYTD_17 | NUMERIC | 8 | 2 | User-defined other deduction type 17 — year-to-date |
| 361 | BKPR_EMP_UODYTD_18 | NUMERIC | 8 | 2 | User-defined other deduction type 18 — year-to-date |
| 362 | BKPR_EMP_UODYTD_19 | NUMERIC | 8 | 2 | User-defined other deduction type 19 — year-to-date |
| 363 | BKPR_EMP_UODYTD_2 | NUMERIC | 8 | 2 | User-defined other deduction type 2 — year-to-date |
| 364 | BKPR_EMP_UODYTD_20 | NUMERIC | 8 | 2 | User-defined other deduction type 20 — year-to-date |
| 365 | BKPR_EMP_UODYTD_3 | NUMERIC | 8 | 2 | User-defined other deduction type 3 — year-to-date |
| 366 | BKPR_EMP_UODYTD_4 | NUMERIC | 8 | 2 | User-defined other deduction type 4 — year-to-date |
| 367 | BKPR_EMP_UODYTD_5 | NUMERIC | 8 | 2 | User-defined other deduction type 5 — year-to-date |
| 368 | BKPR_EMP_UODYTD_6 | NUMERIC | 8 | 2 | User-defined other deduction type 6 — year-to-date |
| 369 | BKPR_EMP_UODYTD_7 | NUMERIC | 8 | 2 | User-defined other deduction type 7 — year-to-date |
| 370 | BKPR_EMP_UODYTD_8 | NUMERIC | 8 | 2 | User-defined other deduction type 8 — year-to-date |
| 371 | BKPR_EMP_UODYTD_9 | NUMERIC | 8 | 2 | User-defined other deduction type 9 — year-to-date |
| 372 | BKPR_EMP_VAQTD | NUMERIC | 8 | 2 | Vacation pay amount — quarter-to-date |
| 373 | BKPR_EMP_VAYTD | NUMERIC | 8 | 2 | Vacation pay amount — year-to-date |
| 374 | BKPR_EMP_VCAP | NUMERIC | 8 | 2 | Vacation hours accrual cap (maximum hours) |
| 375 | BKPR_EMP_VDUE | NUMERIC | 8 | 2 | Vacation hours accrued / due |
| 376 | BKPR_EMP_VHQTD | NUMERIC | 8 | 2 | Vacation hours used — quarter-to-date |
| 377 | BKPR_EMP_VHYTD | NUMERIC | 8 | 2 | Vacation hours used — year-to-date |
| 378 | BKPR_EMP_VRTE | NUMERIC | 8 | 4 | Vacation pay hourly rate |
| 379 | BKPR_EMP_WCEE | NUMERIC | 8 | 4 | Workers' compensation employee rate |
| 380 | BKPR_EMP_WCER | NUMERIC | 8 | 4 | Workers' compensation employer rate |
| 381 | BKPR_EMP_WKQTD | NUMERIC | 8 | 2 | Weeks worked — quarter-to-date |
| 382 | BKPR_EMP_WKYTD | NUMERIC | 8 | 2 | Weeks worked — year-to-date |
| 383 | BKPR_EMP_YEAR | NUMERIC | 8 | — | Current payroll year |
| 384 | BKPR_EMP_ZIP | STRING | 10 | — | ZIP code |

## WOLABRPT
**TEMP FILE FOR JC LABOR REPORTS** — work order labor report staging table

Fields: 45 | Key: MTWOLA_WOPRE + MTWOLA_WOSUF + MTWOLA_DATE + MTWOLA_TRXN

Identical schema to WOELABOR (DI module, MTWOLA_* prefix). See [fields-di.md](fields-di.md)
WOELABOR section for all field definitions.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTWOLA_ASSY | STRING | 15 | — | Assembly / component part number |
| 2 | MTWOLA_ASSYDESC | STRING | 30 | — | Assembly description |
| 3 | MTWOLA_AUDIT | STRING | 35 | — | Audit trail text |
| 4 | MTWOLA_COMPLETE | STRING | 1 | — | Operation complete flag (`Y`=complete) |
| 5 | MTWOLA_DATE | DATE | 4 | — | Labor entry date |
| 6 | MTWOLA_DATE2 | DATE | 4 | — | Secondary date (tool date or end date) |
| 7 | MTWOLA_DEDUCT | TIME | 4 | — | Deduct time (break deduction) |
| 8 | MTWOLA_EMP | INTEGER | 2 | — | Employee number (FK → BKPRMSTR) |
| 9 | MTWOLA_EMP2 | INTEGER | 2 | — | Second / team employee number |
| 10 | MTWOLA_EXTRA | STRING | 50 | — | Extra data |
| 11 | MTWOLA_FOHCOST | NUMERIC | 8 | 2 | Fixed overhead cost |
| 12 | MTWOLA_LABCOST | NUMERIC | 8 | 2 | Labor cost |
| 13 | MTWOLA_LABRATE | NUMERIC | 8 | 4 | Labor rate ($/hour) |
| 14 | MTWOLA_MACH | STRING | 4 | — | Machine code (FK → MACHINE) |
| 15 | MTWOLA_MACHCOST | NUMERIC | 8 | 2 | Machine cost |
| 16 | MTWOLA_MACHDATE | DATE | 4 | — | Machine entry date |
| 17 | MTWOLA_MISC | NUMERIC | 8 | 6 | Miscellaneous cost |
| 18 | MTWOLA_MISCDESC | STRING | 30 | — | Miscellaneous cost description |
| 19 | MTWOLA_NOJOBS | INTEGER | 2 | — | Number of jobs (concurrent operations) |
| 20 | MTWOLA_OPER | INTEGER | 2 | — | Routing operation number |
| 21 | MTWOLA_OTEAM | INTEGER | 2 | — | Overtime team member count |
| 22 | MTWOLA_PARTS | NUMERIC | 8 | 2 | Parts / material cost |
| 23 | MTWOLA_POSTED | STRING | 1 | — | Posted to GL flag (`Y`=posted) |
| 24 | MTWOLA_QCCODE | STRING | 2 | — | QC reject code |
| 25 | MTWOLA_QCDESC | STRING | 30 | — | QC reject description |
| 26 | MTWOLA_REGOVER | STRING | 1 | — | Regular/overtime flag (`R`=regular / `O`=overtime) |
| 27 | MTWOLA_REWORK | STRING | 1 | — | Rework flag (`Y`=this is rework labor) |
| 28 | MTWOLA_RUNHRS | NUMERIC | 8 | 2 | Run hours |
| 29 | MTWOLA_SCDESC | STRING | 30 | — | Scrap description |
| 30 | MTWOLA_SCRAPCD | STRING | 2 | — | Scrap code |
| 31 | MTWOLA_SCRAPPED | NUMERIC | 8 | 2 | Scrapped quantity |
| 32 | MTWOLA_SETCOST | NUMERIC | 8 | 2 | Setup cost |
| 33 | MTWOLA_SETUPHRS | NUMERIC | 8 | 2 | Setup hours |
| 34 | MTWOLA_SHIFT | INTEGER | 2 | — | Shift number (1/2/3) |
| 35 | MTWOLA_START | TIME | 4 | — | Start time |
| 36 | MTWOLA_STOP | TIME | 4 | — | Stop time |
| 37 | MTWOLA_TEAM | INTEGER | 2 | — | Regular team member count |
| 38 | MTWOLA_TOOL | STRING | 15 | — | Tool code (FK → TOOL) |
| 39 | MTWOLA_TOOLDATE | DATE | 4 | — | Tool entry date |
| 40 | MTWOLA_TRXN | INTEGER | 2 | — | Transaction number within WO |
| 41 | MTWOLA_VOHCOST | NUMERIC | 8 | 2 | Variable overhead cost |
| 42 | MTWOLA_WC | STRING | 12 | — | Work center code (FK → DPTMENT) |
| 43 | MTWOLA_WCDATE | DATE | 4 | — | Work center entry date |
| 44 | MTWOLA_WOPRE | NUMERIC | 8 | — | Work order number (FK → WO header) |
| 45 | MTWOLA_WOSUF | INTEGER | 2 | — | Work order suffix |

**Confidence: 80/100** — BKPRMSTR payroll accumulator structure (QTD/YTD, FICA/FIT/ST/SDI/WC,
vacation/sick/UDE/UOD patterns) confirmed from US payroll standards and abbreviation analysis;
EXPACT/EXPDPT multi-account labor allocation confirmed by manufacturing payroll context; specific
UDE/UOD slot assignments and OPNAME content require live data access to verify. WOLABRPT confirmed
by cross-reference to WOELABOR (fields-di.md).
