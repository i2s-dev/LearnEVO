# CM — Contact Management: Field Reference

Status: verified-schema + completed field meanings (Pass 574k, 2026-07-06).

Source: `Evo-DBA_File_Fields 052421.xlsx`, sheet "Fields".

CM is the DBA Contact Manager module — a CRM layer on top of EvoERP. BKCMCUST is the
EVO-linked customer view (BKAR_* prefix). Export tables (BKCMEACC/BKCMEACD/BKCMEACF/
BKCMEACH/BKCMEACT) are identical to their live counterparts and share all field definitions.

---

## BKCMACCC
**ACCOUNT CLASS CODES**

Fields: 2 | Key: BKCM_ACCC_CCODE

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKCM_ACCC_CCODE | STRING | 5 | — | Code for Type of Entry |
| 2 | BKCM_ACCC_DESC | STRING | 25 | — | Description of Code |

## BKCMACCL
**ACCOUNT CLASSES**

Fields: 2 | Key: BKCM_ACCL_CODE + BKCM_ACCL_CLASS

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKCM_ACCL_CLASS | STRING | 5 | — | Class |
| 2 | BKCM_ACCL_CODE | STRING | 10 | — | Account Code |

## BKCMACCN
**ACCOUNT CONTACTS** — up to 10 contact persons per account

Fields: 154 | Key: BKCM_ACCN_CODE

One record per account with 10 parallel contact slots. Each slot N (1–10) stores a
complete contact record: name, title, salutation, phones, emails, dates, and UDF fields.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKCM_ACCN_ALPH1_1 | STRING | 25 | — | Alpha UDF 1 for contact slot 1 |
| 2 | BKCM_ACCN_ALPH1_10 | STRING | 25 | — | Alpha UDF 1 for contact slot 10 |
| 3 | BKCM_ACCN_ALPH1_2 | STRING | 25 | — | Alpha UDF 1 for contact slot 2 |
| 4 | BKCM_ACCN_ALPH1_3 | STRING | 25 | — | Alpha UDF 1 for contact slot 3 |
| 5 | BKCM_ACCN_ALPH1_4 | STRING | 25 | — | Alpha UDF 1 for contact slot 4 |
| 6 | BKCM_ACCN_ALPH1_5 | STRING | 25 | — | Alpha UDF 1 for contact slot 5 |
| 7 | BKCM_ACCN_ALPH1_6 | STRING | 25 | — | Alpha UDF 1 for contact slot 6 |
| 8 | BKCM_ACCN_ALPH1_7 | STRING | 25 | — | Alpha UDF 1 for contact slot 7 |
| 9 | BKCM_ACCN_ALPH1_8 | STRING | 25 | — | Alpha UDF 1 for contact slot 8 |
| 10 | BKCM_ACCN_ALPH1_9 | STRING | 25 | — | Alpha UDF 1 for contact slot 9 |
| 11 | BKCM_ACCN_ALPH2_1 | STRING | 25 | — | Alpha UDF 2 for contact slot 1 |
| 12 | BKCM_ACCN_ALPH2_10 | STRING | 25 | — | Alpha UDF 2 for contact slot 10 |
| 13 | BKCM_ACCN_ALPH2_2 | STRING | 25 | — | Alpha UDF 2 for contact slot 2 |
| 14 | BKCM_ACCN_ALPH2_3 | STRING | 25 | — | Alpha UDF 2 for contact slot 3 |
| 15 | BKCM_ACCN_ALPH2_4 | STRING | 25 | — | Alpha UDF 2 for contact slot 4 |
| 16 | BKCM_ACCN_ALPH2_5 | STRING | 25 | — | Alpha UDF 2 for contact slot 5 |
| 17 | BKCM_ACCN_ALPH2_6 | STRING | 25 | — | Alpha UDF 2 for contact slot 6 |
| 18 | BKCM_ACCN_ALPH2_7 | STRING | 25 | — | Alpha UDF 2 for contact slot 7 |
| 19 | BKCM_ACCN_ALPH2_8 | STRING | 25 | — | Alpha UDF 2 for contact slot 8 |
| 20 | BKCM_ACCN_ALPH2_9 | STRING | 25 | — | Alpha UDF 2 for contact slot 9 |
| 21 | BKCM_ACCN_CODE | STRING | 10 | — | Contact Code |
| 22 | BKCM_ACCN_CON | STRING | 30 | — | Primary contact name (overrides slot 1) |
| 23 | BKCM_ACCN_CONT_1 | STRING | 30 | — | Contact name for slot 1 |
| 24 | BKCM_ACCN_CONT_10 | STRING | 30 | — | Contact name for slot 10 |
| 25 | BKCM_ACCN_CONT_2 | STRING | 30 | — | Contact name for slot 2 |
| 26 | BKCM_ACCN_CONT_3 | STRING | 30 | — | Contact name for slot 3 |
| 27 | BKCM_ACCN_CONT_4 | STRING | 30 | — | Contact name for slot 4 |
| 28 | BKCM_ACCN_CONT_5 | STRING | 30 | — | Contact name for slot 5 |
| 29 | BKCM_ACCN_CONT_6 | STRING | 30 | — | Contact name for slot 6 |
| 30 | BKCM_ACCN_CONT_7 | STRING | 30 | — | Contact name for slot 7 |
| 31 | BKCM_ACCN_CONT_8 | STRING | 30 | — | Contact name for slot 8 |
| 32 | BKCM_ACCN_CONT_9 | STRING | 30 | — | Contact name for slot 9 |
| 33 | BKCM_ACCN_D2LBL_1 | STRING | 20 | — | User-defined label for DATE2 field, slot 1 |
| 34 | BKCM_ACCN_D2LBL_10 | STRING | 20 | — | User-defined label for DATE2 field, slot 10 |
| 35 | BKCM_ACCN_D2LBL_2 | STRING | 20 | — | User-defined label for DATE2 field, slot 2 |
| 36 | BKCM_ACCN_D2LBL_3 | STRING | 20 | — | User-defined label for DATE2 field, slot 3 |
| 37 | BKCM_ACCN_D2LBL_4 | STRING | 20 | — | User-defined label for DATE2 field, slot 4 |
| 38 | BKCM_ACCN_D2LBL_5 | STRING | 20 | — | User-defined label for DATE2 field, slot 5 |
| 39 | BKCM_ACCN_D2LBL_6 | STRING | 20 | — | User-defined label for DATE2 field, slot 6 |
| 40 | BKCM_ACCN_D2LBL_7 | STRING | 20 | — | User-defined label for DATE2 field, slot 7 |
| 41 | BKCM_ACCN_D2LBL_8 | STRING | 20 | — | User-defined label for DATE2 field, slot 8 |
| 42 | BKCM_ACCN_D2LBL_9 | STRING | 20 | — | User-defined label for DATE2 field, slot 9 |
| 43 | BKCM_ACCN_DATE2_1 | DATE | 4 | — | Date UDF 2 for contact slot 1 |
| 44 | BKCM_ACCN_DATE2_10 | DATE | 4 | — | Date UDF 2 for contact slot 10 |
| 45 | BKCM_ACCN_DATE2_2 | DATE | 4 | — | Date UDF 2 for contact slot 2 |
| 46 | BKCM_ACCN_DATE2_3 | DATE | 4 | — | Date UDF 2 for contact slot 3 |
| 47 | BKCM_ACCN_DATE2_4 | DATE | 4 | — | Date UDF 2 for contact slot 4 |
| 48 | BKCM_ACCN_DATE2_5 | DATE | 4 | — | Date UDF 2 for contact slot 5 |
| 49 | BKCM_ACCN_DATE2_6 | DATE | 4 | — | Date UDF 2 for contact slot 6 |
| 50 | BKCM_ACCN_DATE2_7 | DATE | 4 | — | Date UDF 2 for contact slot 7 |
| 51 | BKCM_ACCN_DATE2_8 | DATE | 4 | — | Date UDF 2 for contact slot 8 |
| 52 | BKCM_ACCN_DATE2_9 | DATE | 4 | — | Date UDF 2 for contact slot 9 |
| 53 | BKCM_ACCN_DEAR_1 | STRING | 25 | — | Salutation / Dear line for contact slot 1 (e.g. "Dear John") |
| 54 | BKCM_ACCN_DEAR_10 | STRING | 25 | — | Salutation / Dear line for contact slot 10 |
| 55 | BKCM_ACCN_DEAR_2 | STRING | 25 | — | Salutation / Dear line for contact slot 2 |
| 56 | BKCM_ACCN_DEAR_3 | STRING | 25 | — | Salutation / Dear line for contact slot 3 |
| 57 | BKCM_ACCN_DEAR_4 | STRING | 25 | — | Salutation / Dear line for contact slot 4 |
| 58 | BKCM_ACCN_DEAR_5 | STRING | 25 | — | Salutation / Dear line for contact slot 5 |
| 59 | BKCM_ACCN_DEAR_6 | STRING | 25 | — | Salutation / Dear line for contact slot 6 |
| 60 | BKCM_ACCN_DEAR_7 | STRING | 25 | — | Salutation / Dear line for contact slot 7 |
| 61 | BKCM_ACCN_DEAR_8 | STRING | 25 | — | Salutation / Dear line for contact slot 8 |
| 62 | BKCM_ACCN_DEAR_9 | STRING | 25 | — | Salutation / Dear line for contact slot 9 |
| 63 | BKCM_ACCN_DTLBL_1 | STRING | 20 | — | User-defined label for DATE1 field, slot 1 |
| 64 | BKCM_ACCN_DTLBL_10 | STRING | 20 | — | User-defined label for DATE1 field, slot 10 |
| 65 | BKCM_ACCN_DTLBL_2 | STRING | 20 | — | User-defined label for DATE1 field, slot 2 |
| 66 | BKCM_ACCN_DTLBL_3 | STRING | 20 | — | User-defined label for DATE1 field, slot 3 |
| 67 | BKCM_ACCN_DTLBL_4 | STRING | 20 | — | User-defined label for DATE1 field, slot 4 |
| 68 | BKCM_ACCN_DTLBL_5 | STRING | 20 | — | User-defined label for DATE1 field, slot 5 |
| 69 | BKCM_ACCN_DTLBL_6 | STRING | 20 | — | User-defined label for DATE1 field, slot 6 |
| 70 | BKCM_ACCN_DTLBL_7 | STRING | 20 | — | User-defined label for DATE1 field, slot 7 |
| 71 | BKCM_ACCN_DTLBL_8 | STRING | 20 | — | User-defined label for DATE1 field, slot 8 |
| 72 | BKCM_ACCN_DTLBL_9 | STRING | 20 | — | User-defined label for DATE1 field, slot 9 |
| 73 | BKCM_ACCN_EMAIL_1 | STRING | 128 | — | Email address for contact slot 1 |
| 74 | BKCM_ACCN_EMAIL_10 | STRING | 128 | — | Email address for contact slot 10 |
| 75 | BKCM_ACCN_EMAIL_2 | STRING | 128 | — | Email address for contact slot 2 |
| 76 | BKCM_ACCN_EMAIL_3 | STRING | 128 | — | Email address for contact slot 3 |
| 77 | BKCM_ACCN_EMAIL_4 | STRING | 128 | — | Email address for contact slot 4 |
| 78 | BKCM_ACCN_EMAIL_5 | STRING | 128 | — | Email address for contact slot 5 |
| 79 | BKCM_ACCN_EMAIL_6 | STRING | 128 | — | Email address for contact slot 6 |
| 80 | BKCM_ACCN_EMAIL_7 | STRING | 128 | — | Email address for contact slot 7 |
| 81 | BKCM_ACCN_EMAIL_8 | STRING | 128 | — | Email address for contact slot 8 |
| 82 | BKCM_ACCN_EMAIL_9 | STRING | 128 | — | Email address for contact slot 9 |
| 83 | BKCM_ACCN_EMLBL_1 | STRING | 20 | — | User-defined email label for slot 1 (e.g. "Work", "Personal") |
| 84 | BKCM_ACCN_EMLBL_10 | STRING | 20 | — | User-defined email label for slot 10 |
| 85 | BKCM_ACCN_EMLBL_2 | STRING | 20 | — | User-defined email label for slot 2 |
| 86 | BKCM_ACCN_EMLBL_3 | STRING | 20 | — | User-defined email label for slot 3 |
| 87 | BKCM_ACCN_EMLBL_4 | STRING | 20 | — | User-defined email label for slot 4 |
| 88 | BKCM_ACCN_EMLBL_5 | STRING | 20 | — | User-defined email label for slot 5 |
| 89 | BKCM_ACCN_EMLBL_6 | STRING | 20 | — | User-defined email label for slot 6 |
| 90 | BKCM_ACCN_EMLBL_7 | STRING | 20 | — | User-defined email label for slot 7 |
| 91 | BKCM_ACCN_EMLBL_8 | STRING | 20 | — | User-defined email label for slot 8 |
| 92 | BKCM_ACCN_EMLBL_9 | STRING | 20 | — | User-defined email label for slot 9 |
| 93 | BKCM_ACCN_EXTRA | STRING | 50 | — | Extra |
| 94 | BKCM_ACCN_M2LBL_1 | STRING | 20 | — | User-defined label for misc UDF 2, slot 1 |
| 95 | BKCM_ACCN_M2LBL_10 | STRING | 20 | — | User-defined label for misc UDF 2, slot 10 |
| 96 | BKCM_ACCN_M2LBL_2 | STRING | 20 | — | User-defined label for misc UDF 2, slot 2 |
| 97 | BKCM_ACCN_M2LBL_3 | STRING | 20 | — | User-defined label for misc UDF 2, slot 3 |
| 98 | BKCM_ACCN_M2LBL_4 | STRING | 20 | — | User-defined label for misc UDF 2, slot 4 |
| 99 | BKCM_ACCN_M2LBL_5 | STRING | 20 | — | User-defined label for misc UDF 2, slot 5 |
| 100 | BKCM_ACCN_M2LBL_6 | STRING | 20 | — | User-defined label for misc UDF 2, slot 6 |
| 101 | BKCM_ACCN_M2LBL_7 | STRING | 20 | — | User-defined label for misc UDF 2, slot 7 |
| 102 | BKCM_ACCN_M2LBL_8 | STRING | 20 | — | User-defined label for misc UDF 2, slot 8 |
| 103 | BKCM_ACCN_M2LBL_9 | STRING | 20 | — | User-defined label for misc UDF 2, slot 9 |
| 104 | BKCM_ACCN_MSLBL_1 | STRING | 20 | — | User-defined label for misc UDF 1, slot 1 |
| 105 | BKCM_ACCN_MSLBL_10 | STRING | 20 | — | User-defined label for misc UDF 1, slot 10 |
| 106 | BKCM_ACCN_MSLBL_2 | STRING | 20 | — | User-defined label for misc UDF 1, slot 2 |
| 107 | BKCM_ACCN_MSLBL_3 | STRING | 20 | — | User-defined label for misc UDF 1, slot 3 |
| 108 | BKCM_ACCN_MSLBL_4 | STRING | 20 | — | User-defined label for misc UDF 1, slot 4 |
| 109 | BKCM_ACCN_MSLBL_5 | STRING | 20 | — | User-defined label for misc UDF 1, slot 5 |
| 110 | BKCM_ACCN_MSLBL_6 | STRING | 20 | — | User-defined label for misc UDF 1, slot 6 |
| 111 | BKCM_ACCN_MSLBL_7 | STRING | 20 | — | User-defined label for misc UDF 1, slot 7 |
| 112 | BKCM_ACCN_MSLBL_8 | STRING | 20 | — | User-defined label for misc UDF 1, slot 8 |
| 113 | BKCM_ACCN_MSLBL_9 | STRING | 20 | — | User-defined label for misc UDF 1, slot 9 |
| 114 | BKCM_ACCN_PHLBL_1 | STRING | 20 | — | User-defined phone label for slot 1 (e.g. "Direct", "Mobile") |
| 115 | BKCM_ACCN_PHLBL_10 | STRING | 20 | — | User-defined phone label for slot 10 |
| 116 | BKCM_ACCN_PHLBL_2 | STRING | 20 | — | User-defined phone label for slot 2 |
| 117 | BKCM_ACCN_PHLBL_3 | STRING | 20 | — | User-defined phone label for slot 3 |
| 118 | BKCM_ACCN_PHLBL_4 | STRING | 20 | — | User-defined phone label for slot 4 |
| 119 | BKCM_ACCN_PHLBL_5 | STRING | 20 | — | User-defined phone label for slot 5 |
| 120 | BKCM_ACCN_PHLBL_6 | STRING | 20 | — | User-defined phone label for slot 6 |
| 121 | BKCM_ACCN_PHLBL_7 | STRING | 20 | — | User-defined phone label for slot 7 |
| 122 | BKCM_ACCN_PHLBL_8 | STRING | 20 | — | User-defined phone label for slot 8 |
| 123 | BKCM_ACCN_PHLBL_9 | STRING | 20 | — | User-defined phone label for slot 9 |
| 124 | BKCM_ACCN_PHONE_1 | STRING | 25 | — | Phone number for contact slot 1 |
| 125 | BKCM_ACCN_PHONE_10 | STRING | 25 | — | Phone number for contact slot 10 |
| 126 | BKCM_ACCN_PHONE_2 | STRING | 25 | — | Phone number for contact slot 2 |
| 127 | BKCM_ACCN_PHONE_3 | STRING | 25 | — | Phone number for contact slot 3 |
| 128 | BKCM_ACCN_PHONE_4 | STRING | 25 | — | Phone number for contact slot 4 |
| 129 | BKCM_ACCN_PHONE_5 | STRING | 25 | — | Phone number for contact slot 5 |
| 130 | BKCM_ACCN_PHONE_6 | STRING | 25 | — | Phone number for contact slot 6 |
| 131 | BKCM_ACCN_PHONE_7 | STRING | 25 | — | Phone number for contact slot 7 |
| 132 | BKCM_ACCN_PHONE_8 | STRING | 25 | — | Phone number for contact slot 8 |
| 133 | BKCM_ACCN_PHONE_9 | STRING | 25 | — | Phone number for contact slot 9 |
| 134 | BKCM_ACCN_PRIM | STRING | 1 | — | Primary contact slot number (1–10) |
| 135 | BKCM_ACCN_TITLE_1 | STRING | 30 | — | Job title for contact slot 1 |
| 136 | BKCM_ACCN_TITLE_10 | STRING | 30 | — | Job title for contact slot 10 |
| 137 | BKCM_ACCN_TITLE_2 | STRING | 30 | — | Job title for contact slot 2 |
| 138 | BKCM_ACCN_TITLE_3 | STRING | 30 | — | Job title for contact slot 3 |
| 139 | BKCM_ACCN_TITLE_4 | STRING | 30 | — | Job title for contact slot 4 |
| 140 | BKCM_ACCN_TITLE_5 | STRING | 30 | — | Job title for contact slot 5 |
| 141 | BKCM_ACCN_TITLE_6 | STRING | 30 | — | Job title for contact slot 6 |
| 142 | BKCM_ACCN_TITLE_7 | STRING | 30 | — | Job title for contact slot 7 |
| 143 | BKCM_ACCN_TITLE_8 | STRING | 30 | — | Job title for contact slot 8 |
| 144 | BKCM_ACCN_TITLE_9 | STRING | 30 | — | Job title for contact slot 9 |
| 145 | BMCM_ACCN_DATE1_1 | DATE | 4 | — | Date UDF 1 for contact slot 1 (note: BMCM_ prefix = typo in source data) |
| 146 | BMCM_ACCN_DATE1_10 | DATE | 4 | — | Date UDF 1 for contact slot 10 |
| 147 | BMCM_ACCN_DATE1_2 | DATE | 4 | — | Date UDF 1 for contact slot 2 |
| 148 | BMCM_ACCN_DATE1_3 | DATE | 4 | — | Date UDF 1 for contact slot 3 |
| 149 | BMCM_ACCN_DATE1_4 | DATE | 4 | — | Date UDF 1 for contact slot 4 |
| 150 | BMCM_ACCN_DATE1_5 | DATE | 4 | — | Date UDF 1 for contact slot 5 |
| 151 | BMCM_ACCN_DATE1_6 | DATE | 4 | — | Date UDF 1 for contact slot 6 |
| 152 | BMCM_ACCN_DATE1_7 | DATE | 4 | — | Date UDF 1 for contact slot 7 |
| 153 | BMCM_ACCN_DATE1_8 | DATE | 4 | — | Date UDF 1 for contact slot 8 |
| 154 | BMCM_ACCN_DATE1_9 | DATE | 4 | — | Date UDF 1 for contact slot 9 |

## BKCMACCT
**DBA ACCOUNT MASTER**

Fields: 41 | Key: BKCM_ACCT_CODE

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKCM_ACCT_ADD1 | STRING | 30 | — | Address Line 1 |
| 2 | BKCM_ACCT_ADD2 | STRING | 30 | — | Address Line 2 |
| 3 | BKCM_ACCT_ADD3 | STRING | 30 | — | Address Line 3 |
| 4 | BKCM_ACCT_ALPHA | STRING | 6 | — | Alpha Search |
| 5 | BKCM_ACCT_CCARD | STRING | 25 | — | Credit Card Company |
| 6 | BKCM_ACCT_CEXP | DATE | 4 | — | CC Exp. Date |
| 7 | BKCM_ACCT_CITY | STRING | 26 | — | City |
| 8 | BKCM_ACCT_CMPNM | STRING | 25 | — | Company Name |
| 9 | BKCM_ACCT_CNTRY | STRING | 30 | — | Country |
| 10 | BKCM_ACCT_CNUM | STRING | 25 | — | Credit Card Number |
| 11 | BKCM_ACCT_CODE | STRING | 10 | — | Account Code |
| 12 | BKCM_ACCT_CONT1 | STRING | 30 | — | Contact 1 |
| 13 | BKCM_ACCT_CUST | STRING | 1 | — | Y/N |
| 14 | BKCM_ACCT_DLOAD | STRING | 1 | — | Y/N |
| 15 | BKCM_ACCT_EMAIL | STRING | 128 | — | Email Address |
| 16 | BKCM_ACCT_EMPS | NUMERIC | 8 | — | Number  Employees |
| 17 | BKCM_ACCT_EXTRA | STRING | 200 | — | Extra |
| 18 | BKCM_ACCT_FAX | STRING | 25 | — | Fax Number |
| 19 | BKCM_ACCT_FONE_1 | STRING | 15 | — | Additional phone number 1 |
| 20 | BKCM_ACCT_FONE_2 | STRING | 15 | — | Additional phone number 2 |
| 21 | BKCM_ACCT_FONE_3 | STRING | 15 | — | Additional phone number 3 |
| 22 | BKCM_ACCT_FTHRE_1 | STRING | 25 | — | Phone extension / third phone field 1 |
| 23 | BKCM_ACCT_FTHRE_2 | STRING | 25 | — | Phone extension / third phone field 2 |
| 24 | BKCM_ACCT_FTIME | INTEGER | 2 | — | not used |
| 25 | BKCM_ACCT_FTWO_1 | STRING | 2 | — | Phone type code 1 (2-char type code for FONE_1) |
| 26 | BKCM_ACCT_FTWO_2 | STRING | 2 | — | Phone type code 2 (2-char type code for FONE_2) |
| 27 | BKCM_ACCT_FTWO_3 | STRING | 2 | — | Phone type code 3 (2-char type code for FONE_3) |
| 28 | BKCM_ACCT_LEAD | STRING | 5 | — | Lead Source |
| 29 | BKCM_ACCT_NAME | STRING | 30 | — | Name |
| 30 | BKCM_ACCT_OLDCD | STRING | 10 | — | Old Account Code |
| 31 | BKCM_ACCT_PHONE | STRING | 25 | — | Phone Number |
| 32 | BKCM_ACCT_PNAME | STRING | 25 | — | Prospect Name |
| 33 | BKCM_ACCT_REM_1 | STRING | 60 | — | Remarks line 1 |
| 34 | BKCM_ACCT_REM_2 | STRING | 60 | — | Remarks line 2 |
| 35 | BKCM_ACCT_REP | STRING | 5 | — | Rep Num. |
| 36 | BKCM_ACCT_SICCD | STRING | 7 | — | SIC Code |
| 37 | BKCM_ACCT_START | DATE | 4 | — | Start Date |
| 38 | BKCM_ACCT_STATE | STRING | 2 | — | State |
| 39 | BKCM_ACCT_TERR | STRING | 4 | — | Territory |
| 40 | BKCM_ACCT_TITLE | STRING | 30 | — | Title |
| 41 | BKCM_ACCT_ZIP | STRING | 10 | — | Zip Code |

## BKCMACFC
**REMINDER CODES**

Fields: 3 | Key: BKCM_ACFC_FCODE

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKCM_ACFC_DESC | STRING | 25 | — | Description |
| 2 | BKCM_ACFC_FCODE | STRING | 3 | — | Type Code |
| 3 | BKCM_ACFC_REP | STRING | 5 | — | Rep. Code |

## BKCMACTD
**KEY DATES** — important dates per contact account

Fields: 4 | Key: BKCM_ACTD_CODE + BKCM_ACTD_DCODE

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKCM_ACTD_CODE | STRING | 10 | — | Contact Code |
| 2 | BKCM_ACTD_DATE | DATE | 4 | — | Date |
| 3 | BKCM_ACTD_DCODE | STRING | 2 | — | Date Code |
| 4 | BKCM_ACTD_EXTRA | STRING | 100 | — | Extra data / notes for this key date |

## BKCMACTF
**DBA ACCOUNT FOLLOW-UPS**

Fields: 11 | Key: BKCM_ACTF_CODE + BKCM_ACTF_DATE

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKCM_ACTF_CODE | STRING | 10 | — | Contact Code |
| 2 | BKCM_ACTF_DATE | DATE | 4 | — | Date |
| 3 | BKCM_ACTF_DLOAD | STRING | 1 | — | Download Y/N |
| 4 | BKCM_ACTF_REM_1 | STRING | 60 | — | Remarks line 1 |
| 5 | BKCM_ACTF_REM_2 | STRING | 60 | — | Remarks line 2 |
| 6 | BKCM_ACTF_REM_3 | STRING | 60 | — | Remarks line 3 |
| 7 | BKCM_ACTF_REM_4 | STRING | 60 | — | Remarks line 4 |
| 8 | BKCM_ACTF_REM_5 | STRING | 60 | — | Remarks line 5 |
| 9 | BKCM_ACTF_REP | STRING | 5 | — | Rep Code |
| 10 | BKCM_ACTF_SO | NUMERIC | 8 | — | SO Number |
| 11 | BKCM_ACTF_TYPE | STRING | 3 | — | Type Code |

## BKCMACTH
**DBA ACCOUNT HISTORY**

Fields: 21 | Key: BKCM_ACTH_CODE + BKCM_ACTH_DATE + BKCM_ACTH_EVENT + BKCM_ACTH_LINE

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKCM_ACTH_AMT | NUMERIC | 8 | 2 | Amount |
| 2 | BKCM_ACTH_BALNC | NUMERIC | 8 | 2 | Balance |
| 3 | BKCM_ACTH_BILLD | STRING | 1 | — | Billed Y/N |
| 4 | BKCM_ACTH_BMIN | INTEGER | 2 | — | Billable Minutes |
| 5 | BKCM_ACTH_CD | STRING | 2 | — | Contact Desc. |
| 6 | BKCM_ACTH_CNTCT | STRING | 25 | — | Contact |
| 7 | BKCM_ACTH_CODE | STRING | 10 | — | Contact Code |
| 8 | BKCM_ACTH_DATE | DATE | 4 | — | Date |
| 9 | BKCM_ACTH_DLOAD | STRING | 1 | — | Download Y/N |
| 10 | BKCM_ACTH_EVENT | INTEGER | 2 | — | Event Number |
| 11 | BKCM_ACTH_EXTRA | STRING | 50 | — | Extra |
| 12 | BKCM_ACTH_FLINE | STRING | 1 | — | Y/N |
| 13 | BKCM_ACTH_LINE | INTEGER | 2 | — | Line Number |
| 14 | BKCM_ACTH_MIN | INTEGER | 2 | — | Number Minutes |
| 15 | BKCM_ACTH_PHONE | STRING | 1 | — | Phone Number |
| 16 | BKCM_ACTH_RATE | NUMERIC | 8 | 2 | Rate |
| 17 | BKCM_ACTH_RECVD | TIME | 4 | — | Time Received |
| 18 | BKCM_ACTH_REM | STRING | 57 | — | Remarks |
| 19 | BKCM_ACTH_REP | STRING | 5 | — | Rep. Code |
| 20 | BKCM_ACTH_START | TIME | 4 | — | Time Call Start |
| 21 | BKCM_ACTH_STOP | TIME | 4 | — | Time Call Stop |

## BKCMCNTD
**CONTACT MANAGER DEFAULTS**

Fields: 12 | Key: singleton

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKCM_CNTD_LTYPE | STRING | 1 | — | Label Printer Type  L/I/D |
| 2 | BKCM_CNTD_MREP | STRING | 1 | — | Rep Code Required? Y/N |
| 3 | BKCM_CNTD_TITLE_1 | STRING | 25 | — | Default contact title option 1 (user-configurable dropdown) |
| 4 | BKCM_CNTD_TITLE_2 | STRING | 25 | — | Default contact title option 2 |
| 5 | BKCM_CNTD_TITLE_3 | STRING | 25 | — | Default contact title option 3 |
| 6 | BKCM_CNTD_TITLE_4 | STRING | 25 | — | Default contact title option 4 |
| 7 | BKCM_CNTD_TITLE_5 | STRING | 25 | — | Default contact title option 5 |
| 8 | BKCM_CNTD_TITLE_6 | STRING | 25 | — | Default contact title option 6 |
| 9 | BKCM_CNTD_TITLE_7 | STRING | 25 | — | Default contact title option 7 |
| 10 | BKCM_CNTD_TITLE_8 | STRING | 25 | — | Default contact title option 8 |
| 11 | BKCM_CNTD_TITLE_9 | STRING | 25 | — | Default contact title option 9 |
| 12 | BKCM_CNTD_TTLE1 | STRING | 25 | — | Title 1 |

## BKCMCUST
**EVO CONTACT ACCOUNT MASTER** — EvoERP customer master linked to CM (BKAR_* prefix)

Fields: 106 | Key: BKAR_CUSTCODE

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAR_ADD1 | STRING | 30 | — | Address Line 1 |
| 2 | BKAR_ADD2_1 | STRING | 30 | — | Address Line 2 (line 1 of secondary address block) |
| 3 | BKAR_ADD2_2 | STRING | 30 | — | Address Line 2 (line 2 of secondary address block) |
| 4 | BKAR_CARRIER | STRING | 15 | — | Carrier |
| 5 | BKAR_CHG_INTRST | STRING | 1 | — | Charge Interst Y/N |
| 6 | BKAR_CITY | STRING | 26 | — | City |
| 7 | BKAR_CLASS | STRING | 4 | — | Customer Class |
| 8 | BKAR_COGS_LYR | NUMERIC | 8 | 2 | COGS Last Year |
| 9 | BKAR_COGS_MTD | NUMERIC | 8 | 2 | COGS Month To Date |
| 10 | BKAR_COGS_PVAR | NUMERIC | 8 | 4 | COGS Percent Variance |
| 11 | BKAR_COGS_YTD | NUMERIC | 8 | 2 | COGS Year To Date |
| 12 | BKAR_COMM_1 | NUMERIC | 8 | 4 | Commission rate for salesperson 1 |
| 13 | BKAR_COMM_2 | NUMERIC | 8 | 4 | Commission rate for salesperson 2 |
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
| 24 | BKAR_CUST_YEAR | STRING | 12 | — | Customer fiscal year code |
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
| 47 | BKAR_IS_REP | STRING | 5 | — | Inside sales rep code (EvoERP rep assigned to customer) |
| 48 | BKAR_IS_TAXGRP | STRING | 10 | — | Tax Group |
| 49 | BKAR_IS_TAXIN | STRING | 1 | — | Excise Tax-In |
| 50 | BKAR_LASTPMT | DATE | 4 | — | Last Payment Date |
| 51 | BKAR_LASTSALE | DATE | 4 | — | Last Sale Date |
| 52 | BKAR_LEAD_SRC | STRING | 5 | — | Lead Source |
| 53 | BKAR_LEAD_SRC2 | STRING | 5 | — | Secondary lead source code |
| 54 | BKAR_MAIL_LIST | STRING | 1 | — | Mail List Y/N |
| 55 | BKAR_NET_LYR | NUMERIC | 8 | 2 | Net Profit Last Year |
| 56 | BKAR_NET_MTD | NUMERIC | 8 | 2 | Net Profit Month To Date |
| 57 | BKAR_NET_PVAR | NUMERIC | 8 | 4 | Net Profit Percent Variance |
| 58 | BKAR_NET_YTD | NUMERIC | 8 | 2 | Net Profit Year To Date |
| 59 | BKAR_NEW_CUST | STRING | 1 | — | New Customer Y/N |
| 60 | BKAR_NOTES_1 | STRING | 80 | — | Account notes line 1 |
| 61 | BKAR_NOTES_10 | STRING | 80 | — | Account notes line 10 |
| 62 | BKAR_NOTES_2 | STRING | 80 | — | Account notes line 2 |
| 63 | BKAR_NOTES_3 | STRING | 80 | — | Account notes line 3 |
| 64 | BKAR_NOTES_4 | STRING | 80 | — | Account notes line 4 |
| 65 | BKAR_NOTES_5 | STRING | 80 | — | Account notes line 5 |
| 66 | BKAR_NOTES_6 | STRING | 80 | — | Account notes line 6 |
| 67 | BKAR_NOTES_7 | STRING | 80 | — | Account notes line 7 |
| 68 | BKAR_NOTES_8 | STRING | 80 | — | Account notes line 8 |
| 69 | BKAR_NOTES_9 | STRING | 80 | — | Account notes line 9 |
| 70 | BKAR_NUM_INVCS | NUMERIC | 8 | — | Number Invoices |
| 71 | BKAR_OUT_CREDIT_1 | NUMERIC | 8 | 2 | Outstanding credit balance type 1 |
| 72 | BKAR_OUT_CREDIT_2 | NUMERIC | 8 | 2 | Outstanding credit balance type 2 |
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
| 87 | BKAR_SHP_TOLRNC | STRING | 10 | — | Ship tolerance percentage or code |
| 88 | BKAR_SHP_WINDOW | STRING | 30 | — | Shipping Window |
| 89 | BKAR_SIC_CODE | STRING | 7 | — | SIC Code |
| 90 | BKAR_SLSP_NUM_1 | INTEGER | 2 | — | Salesperson number 1 (FK → salesperson master) |
| 91 | BKAR_SLSP_NUM_2 | INTEGER | 2 | — | Salesperson number 2 (secondary salesperson) |
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

## BKCMDTCD
**DATE CODES**

Fields: 2 | Key: BKCM_DTCD_DCODE

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKCM_DTCD_DCODE | STRING | 2 | — | Date Code |
| 2 | BKCM_DTCD_DESC | STRING | 25 | — | Description |

## BKCMEACC
**DBA ACCOUNT CLASSES EXPORT FILE**

Fields: 2 — Identical schema to BKCMACCL. See that table.

## BKCMEACD
**DBA ACCOUNT DATES EXPORT FILE**

Fields: 4 — Identical schema to BKCMACTD. See that table.

## BKCMEACF
**DBA ACCOUNT FOLLOW-UPS EXPORT FILE**

Fields: 11 — Identical schema to BKCMACTF. See that table.

## BKCMEACH
**DBA ACCOUNT HISTORY EXPORT FILE**

Fields: 21 — Identical schema to BKCMACTH. See that table.

## BKCMEACT
**DBA ACCOUNT MASTER EXPORT FILE**

Fields: 41 — Identical schema to BKCMACCT. See that table.

## BKCMFTME
**DBA NO CHARGE TIME** — pre-paid / complimentary support time balance per account

Fields: 7 | Key: BKCM_FTME_CODE

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKCM_FTME_ATIME | INTEGER | 2 | — | Allocated time (total no-charge minutes granted to this account) |
| 2 | BKCM_FTME_BALNC | NUMERIC | 8 | 2 | Balance of no-charge time remaining |
| 3 | BKCM_FTME_CODE | STRING | 10 | — | Contact Code |
| 4 | BKCM_FTME_DESC | STRING | 25 | — | Description |
| 5 | BKCM_FTME_FTIME | INTEGER | 2 | — | Free time (no-charge minutes used this period) |
| 6 | BKCM_FTME_LASTP | DATE | 4 | — | Last Payment |
| 7 | BKCM_FTME_NTIME | INTEGER | 2 | — | Next scheduled no-charge time allocation (minutes) |

## BKCMHCD2
**DBA HISTORY CODES, 2ND DATABASE**

Fields: 7 | Key: BKCM_HCD2_HCODE

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKCM_HCD2_CCODE | STRING | 1 | — | Category code (type classification of this history code) |
| 2 | BKCM_HCD2_CPART | STRING | 15 | — | Category part code (catalog number for this type) |
| 3 | BKCM_HCD2_HCODE | STRING | 2 | — | History Code |
| 4 | BKCM_HCD2_PCODE | STRING | 1 | — | Primary type code |
| 5 | BKCM_HCD2_PPART | STRING | 15 | — | Primary part code |
| 6 | BKCM_HCD2_RCODE | STRING | 1 | — | Related type code |
| 7 | BKCM_HCD2_RPART | STRING | 15 | — | Related part code |

## BKCMHCOD
**DBA HISTORY CODES**

Fields: 9 | Key: BKCM_HCOD_HCODE

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKCM_HCOD_ABILL | STRING | 1 | — | Auto-billable flag (`Y`=time is billable when this code is used) |
| 2 | BKCM_HCOD_BPART | STRING | 15 | — | Billable part code (service item to charge when auto-billing) |
| 3 | BKCM_HCOD_DESC | STRING | 25 | — | Description |
| 4 | BKCM_HCOD_FPART | STRING | 15 | — | Flat-rate part code (item used for fixed-fee billing) |
| 5 | BKCM_HCOD_HCODE | STRING | 2 | — | History Code |
| 6 | BKCM_HCOD_NPART | STRING | 15 | — | No-charge part code (item for non-billable / free service) |
| 7 | BKCM_HCOD_RATE | NUMERIC | 8 | 2 | Hourly billing rate |
| 8 | BKCM_HCOD_UM | STRING | 3 | — | Unit of measure (for billing line items) |
| 9 | BKCM_HCOD_WINDW | STRING | 1 | — | Time window flag (limits allowed entry window for this history type) |

## BKCMLEAD
**LEAD SOURCE CODES**

Fields: 2 | Key: BKCM_LEAD_SCODE

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKCM_LEAD_DESC | STRING | 25 | — | Description |
| 2 | BKCM_LEAD_SCODE | STRING | 5 | — | Lead Source Code |

## BKCMMHST
**DBA MAILING HISTORY** — mail merge session history with filter criteria used

Fields: 72 | Key: BKCM_MHST_MCODE + BKCM_MHST_MDATE

Filter fields use F* = from (start of range) and T* = to (end of range).
CLASS_1..20 = classes included; OCLAS_1..20 = classes excluded from mailing.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKCM_MHST_CLASS_1 | STRING | 5 | — | Account class included in mailing 1 (up to 20 class codes) |
| 2 | BKCM_MHST_CLASS_10 | STRING | 5 | — | Account class included 10 |
| 3 | BKCM_MHST_CLASS_11 | STRING | 5 | — | Account class included 11 |
| 4 | BKCM_MHST_CLASS_12 | STRING | 5 | — | Account class included 12 |
| 5 | BKCM_MHST_CLASS_13 | STRING | 5 | — | Account class included 13 |
| 6 | BKCM_MHST_CLASS_14 | STRING | 5 | — | Account class included 14 |
| 7 | BKCM_MHST_CLASS_15 | STRING | 5 | — | Account class included 15 |
| 8 | BKCM_MHST_CLASS_16 | STRING | 5 | — | Account class included 16 |
| 9 | BKCM_MHST_CLASS_17 | STRING | 5 | — | Account class included 17 |
| 10 | BKCM_MHST_CLASS_18 | STRING | 5 | — | Account class included 18 |
| 11 | BKCM_MHST_CLASS_19 | STRING | 5 | — | Account class included 19 |
| 12 | BKCM_MHST_CLASS_2 | STRING | 5 | — | Account class included 2 |
| 13 | BKCM_MHST_CLASS_20 | STRING | 5 | — | Account class included 20 |
| 14 | BKCM_MHST_CLASS_3 | STRING | 5 | — | Account class included 3 |
| 15 | BKCM_MHST_CLASS_4 | STRING | 5 | — | Account class included 4 |
| 16 | BKCM_MHST_CLASS_5 | STRING | 5 | — | Account class included 5 |
| 17 | BKCM_MHST_CLASS_6 | STRING | 5 | — | Account class included 6 |
| 18 | BKCM_MHST_CLASS_7 | STRING | 5 | — | Account class included 7 |
| 19 | BKCM_MHST_CLASS_8 | STRING | 5 | — | Account class included 8 |
| 20 | BKCM_MHST_CLASS_9 | STRING | 5 | — | Account class included 9 |
| 21 | BKCM_MHST_CNUM | INTEGER | 2 | — | Count of accounts mailed in this session |
| 22 | BKCM_MHST_CUSTO | STRING | 1 | — | Customers only filter (`Y`=only mail to EvoERP customers) |
| 23 | BKCM_MHST_DESC | STRING | 25 | — | Mailing session description |
| 24 | BKCM_MHST_DORL | STRING | 1 | — | Download or Local flag (`D`=download list / `L`=use local) |
| 25 | BKCM_MHST_FACD | STRING | 10 | — | Filter account code — from (range start) |
| 26 | BKCM_MHST_FKDAT | DATE | 4 | — | Filter key date — from |
| 27 | BKCM_MHST_FLEAD | STRING | 5 | — | Filter lead source — from |
| 28 | BKCM_MHST_FORM | STRING | 15 | — | Form / letter name used for this mailing |
| 29 | BKCM_MHST_FREP | STRING | 5 | — | Filter rep — from |
| 30 | BKCM_MHST_FSDT | DATE | 4 | — | Filter start date — from |
| 31 | BKCM_MHST_FSIC | STRING | 7 | — | Filter SIC code — from |
| 32 | BKCM_MHST_FST | STRING | 2 | — | Filter state — from |
| 33 | BKCM_MHST_FTERR | STRING | 4 | — | Filter territory — from |
| 34 | BKCM_MHST_FZIP | STRING | 10 | — | Filter zip code — from |
| 35 | BKCM_MHST_KDCD | STRING | 2 | — | Key date code used as filter criterion |
| 36 | BKCM_MHST_MCODE | STRING | 15 | — | Contact Code |
| 37 | BKCM_MHST_MDATE | DATE | 4 | — | Mailing date |
| 38 | BKCM_MHST_NOCUS | STRING | 1 | — | No customers flag (`Y`=exclude EvoERP customers from this mailing) |
| 39 | BKCM_MHST_NUMUP | INTEGER | 2 | — | Number of records updated / labels printed |
| 40 | BKCM_MHST_OCLAS_1 | STRING | 5 | — | Account class excluded from mailing 1 (up to 20) |
| 41 | BKCM_MHST_OCLAS_10 | STRING | 5 | — | Account class excluded 10 |
| 42 | BKCM_MHST_OCLAS_11 | STRING | 5 | — | Account class excluded 11 |
| 43 | BKCM_MHST_OCLAS_12 | STRING | 5 | — | Account class excluded 12 |
| 44 | BKCM_MHST_OCLAS_13 | STRING | 5 | — | Account class excluded 13 |
| 45 | BKCM_MHST_OCLAS_14 | STRING | 5 | — | Account class excluded 14 |
| 46 | BKCM_MHST_OCLAS_15 | STRING | 5 | — | Account class excluded 15 |
| 47 | BKCM_MHST_OCLAS_16 | STRING | 5 | — | Account class excluded 16 |
| 48 | BKCM_MHST_OCLAS_17 | STRING | 5 | — | Account class excluded 17 |
| 49 | BKCM_MHST_OCLAS_18 | STRING | 5 | — | Account class excluded 18 |
| 50 | BKCM_MHST_OCLAS_19 | STRING | 5 | — | Account class excluded 19 |
| 51 | BKCM_MHST_OCLAS_2 | STRING | 5 | — | Account class excluded 2 |
| 52 | BKCM_MHST_OCLAS_20 | STRING | 5 | — | Account class excluded 20 |
| 53 | BKCM_MHST_OCLAS_3 | STRING | 5 | — | Account class excluded 3 |
| 54 | BKCM_MHST_OCLAS_4 | STRING | 5 | — | Account class excluded 4 |
| 55 | BKCM_MHST_OCLAS_5 | STRING | 5 | — | Account class excluded 5 |
| 56 | BKCM_MHST_OCLAS_6 | STRING | 5 | — | Account class excluded 6 |
| 57 | BKCM_MHST_OCLAS_7 | STRING | 5 | — | Account class excluded 7 |
| 58 | BKCM_MHST_OCLAS_8 | STRING | 5 | — | Account class excluded 8 |
| 59 | BKCM_MHST_OCLAS_9 | STRING | 5 | — | Account class excluded 9 |
| 60 | BKCM_MHST_PCONT | STRING | 1 | — | Print contacts flag (`Y`=include contact names on labels/letters) |
| 61 | BKCM_MHST_REM | STRING | 1 | — | Remarks flag (`Y`=remarks exist for this mailing session) |
| 62 | BKCM_MHST_SORT | STRING | 1 | — | Sort option code (e.g. `Z`=by zip, `N`=by name) |
| 63 | BKCM_MHST_STAT | STRING | 11 | — | Status (mailing session status code) |
| 64 | BKCM_MHST_TACD | STRING | 10 | — | Filter account code — to (range end) |
| 65 | BKCM_MHST_TKDAT | DATE | 4 | — | Filter key date — to |
| 66 | BKCM_MHST_TLEAD | STRING | 5 | — | Filter lead source — to |
| 67 | BKCM_MHST_TREP | STRING | 5 | — | Filter rep — to |
| 68 | BKCM_MHST_TSDT | DATE | 4 | — | Filter start date — to |
| 69 | BKCM_MHST_TSIC | STRING | 7 | — | Filter SIC code — to |
| 70 | BKCM_MHST_TST | STRING | 2 | — | Filter state — to |
| 71 | BKCM_MHST_TTERR | STRING | 4 | — | Filter territory — to |
| 72 | BKCM_MHST_TZIP | STRING | 10 | — | Filter zip code — to |

## BKCMPCNT
**DBA PERSONAL CONTACT MASTER** — standalone individual contacts (not linked to an account)

Fields: 24 | Key: BKCM_PCNT_NAME (or BKCM_PCNT_CCODE)

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKCM_PCNT_ADD1 | STRING | 30 | — | Address line 1 |
| 2 | BKCM_PCNT_ADD2 | STRING | 30 | — | Address line 2 |
| 3 | BKCM_PCNT_ADD3 | STRING | 30 | — | Address line 3 |
| 4 | BKCM_PCNT_ALPHA | STRING | 6 | — | Alpha sort code |
| 5 | BKCM_PCNT_CCODE | STRING | 10 | — | Account code link (FK → BKCMACCT, optional — blank if no account) |
| 6 | BKCM_PCNT_CITY | STRING | 26 | — | City |
| 7 | BKCM_PCNT_CLASS | STRING | 5 | — | Contact class code |
| 8 | BKCM_PCNT_CNTRY | STRING | 30 | — | Country |
| 9 | BKCM_PCNT_CONT | STRING | 30 | — | Contact full name |
| 10 | BKCM_PCNT_EMAIL | STRING | 40 | — | Email address |
| 11 | BKCM_PCNT_EXTRA | STRING | 100 | — | Extra data |
| 12 | BKCM_PCNT_FAX | STRING | 25 | — | Fax number |
| 13 | BKCM_PCNT_NAME | STRING | 30 | — | Full name (sort/display name) |
| 14 | BKCM_PCNT_PHONE | STRING | 25 | — | Phone number |
| 15 | BKCM_PCNT_REM_1 | STRING | 60 | — | Remarks line 1 |
| 16 | BKCM_PCNT_REM_2 | STRING | 60 | — | Remarks line 2 |
| 17 | BKCM_PCNT_REM_3 | STRING | 60 | — | Remarks line 3 |
| 18 | BKCM_PCNT_REM_4 | STRING | 60 | — | Remarks line 4 |
| 19 | BKCM_PCNT_REP | STRING | 5 | — | Rep code (FK → BKCMREP) |
| 20 | BKCM_PCNT_SDATE | DATE | 4 | — | First contact date |
| 21 | BKCM_PCNT_STATE | STRING | 2 | — | State |
| 22 | BKCM_PCNT_TITLE | STRING | 30 | — | Job title |
| 23 | BKCM_PCNT_WPHON | STRING | 25 | — | Work phone number |
| 24 | BKCM_PCNT_ZIP | STRING | 10 | — | Zip code |

## BKCMPCTF
**DBA PERSONAL CONTACT FOLLOW-UPS**

Fields: 9 | Key: BKCM_PCTF_CCODE + BKCM_PCTF_DATE

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKCM_PCTF_CCODE | STRING | 10 | — | Personal contact code (FK → BKCMPCNT) |
| 2 | BKCM_PCTF_DATE | DATE | 4 | — | Follow-up date |
| 3 | BKCM_PCTF_REM_1 | STRING | 60 | — | Remarks line 1 |
| 4 | BKCM_PCTF_REM_2 | STRING | 60 | — | Remarks line 2 |
| 5 | BKCM_PCTF_REM_3 | STRING | 60 | — | Remarks line 3 |
| 6 | BKCM_PCTF_REM_4 | STRING | 60 | — | Remarks line 4 |
| 7 | BKCM_PCTF_REM_5 | STRING | 60 | — | Remarks line 5 |
| 8 | BKCM_PCTF_REP | STRING | 5 | — | Rep code (FK → BKCMREP) |
| 9 | BKCM_PCTF_TYPE | STRING | 3 | — | Follow-up type code |

## BKCMPCTH
**DBA PERSONAL CONTACT HISTORY**

Fields: 8 | Key: BKCM_PCTH_CCODE + BKCM_PCTH_DATE + BKCM_PCTH_EVENT + BKCM_PCTH_LINE

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKCM_PCTH_CCODE | STRING | 10 | — | Personal contact code (FK → BKCMPCNT) |
| 2 | BKCM_PCTH_DATE | DATE | 4 | — | Contact date |
| 3 | BKCM_PCTH_EVENT | INTEGER | 2 | — | Event number (groups multi-line history entries) |
| 4 | BKCM_PCTH_EXTRA | STRING | 50 | — | Extra data |
| 5 | BKCM_PCTH_FLINE | STRING | 1 | — | First line flag (`Y`=first line of this event) |
| 6 | BKCM_PCTH_LINE | INTEGER | 2 | — | Line number within event |
| 7 | BKCM_PCTH_REM | STRING | 60 | — | Remarks text for this history line |
| 8 | BKCM_PCTH_REP | STRING | 5 | — | Rep code who made this contact |

## BKCMREP
**DBA REP MASTER**

Fields: 14 | Key: BKCM_REP_REP

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKCM_REP_AADD | STRING | 1 | — | Auto-add new accounts flag (`Y`=automatically add new accounts to this rep) |
| 2 | BKCM_REP_CHANGE | STRING | 1 | — | Can change price flag (`Y`=rep allowed to override pricing) |
| 3 | BKCM_REP_DDCODE | STRING | 2 | — | Default date code (default history date type) |
| 4 | BKCM_REP_DFCODE | STRING | 3 | — | Default follow-up code |
| 5 | BKCM_REP_DHCODE | STRING | 2 | — | Default history code |
| 6 | BKCM_REP_EMP | INTEGER | 2 | — | Employee number (FK → employee master) |
| 7 | BKCM_REP_FNAME | STRING | 25 | — | First name |
| 8 | BKCM_REP_FNMEMI | STRING | 25 | — | First name and middle initial combined |
| 9 | BKCM_REP_FTITLE | STRING | 25 | — | Rep title / job title |
| 10 | BKCM_REP_GWARN | STRING | 1 | — | Give warning flag (`Y`=warn when entering activity for another rep's account) |
| 11 | BKCM_REP_LNAME | STRING | 25 | — | Last name |
| 12 | BKCM_REP_PSWD | STRING | 10 | — | Password |
| 13 | BKCM_REP_REP | STRING | 5 | — | Rep code (PK) |
| 14 | BKCM_REP_VIEW | STRING | 1 | — | View mode (`A`=see all accounts / `O`=see own accounts only) |

## BKCMTERR
**TERRITORY MASTER**

Fields: 2 | Key: BKCM_TERR_TCODE

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKCM_TERR_DESC | STRING | 25 | — | Territory description |
| 2 | BKCM_TERR_TCODE | STRING | 4 | — | Territory code (PK) |

## BKCMVNDF
**DBA VENDOR FOLLOW-UPS**

Fields: 10 | Key: BKCM_VNDF_VCODE + BKCM_VNDF_DATE

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKCM_VNDF_DATE | DATE | 4 | — | Follow-up date |
| 2 | BKCM_VNDF_PO | NUMERIC | 8 | — | PO number associated with this follow-up |
| 3 | BKCM_VNDF_REM_1 | STRING | 60 | — | Remarks line 1 |
| 4 | BKCM_VNDF_REM_2 | STRING | 60 | — | Remarks line 2 |
| 5 | BKCM_VNDF_REM_3 | STRING | 60 | — | Remarks line 3 |
| 6 | BKCM_VNDF_REM_4 | STRING | 60 | — | Remarks line 4 |
| 7 | BKCM_VNDF_REM_5 | STRING | 60 | — | Remarks line 5 |
| 8 | BKCM_VNDF_REP | STRING | 5 | — | Rep code (FK → BKCMREP) |
| 9 | BKCM_VNDF_TYPE | STRING | 3 | — | Follow-up type code |
| 10 | BKCM_VNDF_VCODE | STRING | 10 | — | Vendor code (FK → BKAPVEND) |

## BKCMVNDH
**DBA VENDOR HISTORY**

Fields: 8 | Key: BKCM_VNDH_VCODE + BKCM_VNDH_DATE + BKCM_VNDH_EVENT + BKCM_VNDH_LINE

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKCM_VNDH_DATE | DATE | 4 | — | Contact date |
| 2 | BKCM_VNDH_EVENT | INTEGER | 2 | — | Event number |
| 3 | BKCM_VNDH_EXTRA | STRING | 50 | — | Extra data |
| 4 | BKCM_VNDH_FLINE | STRING | 1 | — | First line flag (`Y`=first line of this event) |
| 5 | BKCM_VNDH_LINE | INTEGER | 2 | — | Line number within event |
| 6 | BKCM_VNDH_REM | STRING | 60 | — | Remarks text |
| 7 | BKCM_VNDH_REP | STRING | 5 | — | Rep code who made this contact |
| 8 | BKCM_VNDH_VCODE | STRING | 10 | — | Vendor code (FK → BKAPVEND) |

## BKCMVNFC
**DBA VENDOR FOLLOW-UP CODES**

Fields: 3 | Key: BKCM_VNFC_FCODE

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKCM_VNFC_DESC | STRING | 25 | — | Description |
| 2 | BKCM_VNFC_FCODE | STRING | 3 | — | Follow-up code (PK) |
| 3 | BKCM_VNFC_REP | STRING | 5 | — | Rep code (assigned rep or blank=all) |

## ISAREMND
**ARCHIVED REMINDERS** — completed/expired reminder records

Fields: 24 | Key: IS_REM_WHO + IS_REM_DATE + IS_REM_ITEM

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_REM_BEFTXT | STRING | 15 | — | Before-due text (e.g. "3 days before") |
| 2 | IS_REM_CO | STRING | 3 | — | Company code |
| 3 | IS_REM_COUNTER | INTEGER | 4 | — | Occurrence counter (how many times this reminder has fired) |
| 4 | IS_REM_CUST | STRING | 10 | — | Customer code (FK → AR customer if reminder is linked to a customer) |
| 5 | IS_REM_DATE | DATE | 4 | — | Reminder date |
| 6 | IS_REM_DISP | STRING | 1 | — | Displayed flag (`Y`=reminder has been shown to user) |
| 7 | IS_REM_EDATE | DATE | 4 | — | Expiry date |
| 8 | IS_REM_EMAIL | STRING | 400 | — | Email address(es) to notify (multiple addresses separated by delimiter) |
| 9 | IS_REM_ENDDT | DATE | 4 | — | Recurrence end date |
| 10 | IS_REM_ENDTM | TIME | 4 | — | Recurrence end time |
| 11 | IS_REM_ETIME | TIME | 4 | — | Event time |
| 12 | IS_REM_EXTRA | STRING | 50 | — | Extra data |
| 13 | IS_REM_FILE | STRING | 256 | — | Attached file path |
| 14 | IS_REM_ITEM | STRING | 15 | — | Item code / reference (linked SO, PO, or document number) |
| 15 | IS_REM_MEMO | STRING | 0 | — | Memo (blob reference — zero-length placeholder) |
| 16 | IS_REM_NOTE | STRING | 6000 | — | Full note / reminder body text (up to 6000 chars) |
| 17 | IS_REM_NOTIFY | STRING | 1 | — | Notify by email flag (`Y`=send email notification) |
| 18 | IS_REM_SENT | STRING | 25 | — | Sent-to info (email address or contact name notified) |
| 19 | IS_REM_SUBJECT | STRING | 100 | — | Reminder subject / title |
| 20 | IS_REM_TIME | TIME | 4 | — | Reminder time |
| 21 | IS_REM_TRANS | STRING | 1 | — | Transferred flag (`Y`=this reminder was forwarded/delegated) |
| 22 | IS_REM_TYPE | STRING | 3 | — | Reminder type code |
| 23 | IS_REM_VEND | STRING | 10 | — | Vendor code (FK → BKAPVEND if reminder linked to a vendor) |
| 24 | IS_REM_WHO | STRING | 20 | — | Created-by / assigned-to (rep or user code) |

**Confidence: 75/100** — BKCMACCN 10-slot structure, F*/T* filter pair pattern in BKCMMHST, BKCMREP
flags, and BKCMHCOD billing parts confirmed by field-name analysis and CRM conventions; IS_REM_* reminder
fields confirmed by naming; BKCMHCD2 part-code semantics and BKCMFTME time-unit interpretation are
inferred — verify exact codes via RWN decryption.
