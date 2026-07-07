# SM — System Management: Field Reference

Status: verified-schema

Source: `Evo-DBA_File_Fields 052421.xlsx`, sheet "Fields".
Field descriptions where provided by source; otherwise name-inferred.

---

## BKFLDHLP
**FIELD SPECIFIC HELP**

Fields: 3

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | HLP_CODE | STRING | 17 | — | Help topic code identifier |
| 2 | HLP_INDEX | INTEGER | 2 | — | Index position within help topic |
| 3 | HLP_LINE | STRING | 60 | — | Help text line content |

## BKSYMSTR
**SYSTEM MASTER FILE**

Fields: 286

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKSY_AP_AGING_1 | INTEGER | 2 | — | AP aging bucket 1 threshold (days) |
| 2 | BKSY_AP_AGING_2 | INTEGER | 2 | — | AP aging bucket 2 threshold (days) |
| 3 | BKSY_AP_AGING_3 | INTEGER | 2 | — | AP aging bucket 3 threshold (days) |
| 4 | BKSY_AP_AGING_4 | INTEGER | 2 | — | AP aging bucket 4 threshold (days) |
| 5 | BKSY_AP_AGING_5 | INTEGER | 2 | — | AP aging bucket 5 threshold (days) |
| 6 | BKSY_AP_CHKACT | INTEGER | 2 | — | AP default check bank account slot number |
| 7 | BKSY_AP_DISCDPT | STRING | 4 | — | AP purchase discount GL department |
| 8 | BKSY_AP_DISCGL | STRING | 10 | — | AP purchase discount GL account |
| 9 | BKSY_AP_ENDDESC_1 | STRING | 30 | — | AP invoice end-of-document description line 1 |
| 10 | BKSY_AP_ENDDESC_2 | STRING | 30 | — | AP invoice end-of-document description line 2 |
| 11 | BKSY_AP_ENDDESC_3 | STRING | 30 | — | AP invoice end-of-document description line 3 |
| 12 | BKSY_AP_ENDDESC_4 | STRING | 30 | — | AP invoice end-of-document description line 4 |
| 13 | BKSY_AP_ENDDESC_5 | STRING | 30 | — | AP invoice end-of-document description line 5 |
| 14 | BKSY_AP_ENTBY | STRING | 2 | — | AP default entry-by operator code |
| 15 | BKSY_AP_GLACT | STRING | 10 | — | AP default accounts payable GL account |
| 16 | BKSY_AP_GLDPT | STRING | 4 | — | AP default GL department |
| 17 | BKSY_AP_PEL | STRING | 1 | — | AP price/exchange lock flag |
| 18 | BKSY_AP_RECNUM | NUMERIC | 8 | — | AP last record number (auto-increment) |
| 19 | BKSY_AP_SHP_VIA | STRING | 15 | — | AP default ship-via code |
| 20 | BKSY_APINV_NUM | NUMERIC | 8 | — | Last AP invoice number issued |
| 21 | BKSY_APPO_NUM | NUMERIC | 8 | — | Last AP purchase order number issued |
| 22 | BKSY_AR_AGING_1 | INTEGER | 2 | — | AR aging bucket 1 threshold (days) |
| 23 | BKSY_AR_AGING_2 | INTEGER | 2 | — | AR aging bucket 2 threshold (days) |
| 24 | BKSY_AR_AGING_3 | INTEGER | 2 | — | AR aging bucket 3 threshold (days) |
| 25 | BKSY_AR_AGING_4 | INTEGER | 2 | — | AR aging bucket 4 threshold (days) |
| 26 | BKSY_AR_AGING_5 | INTEGER | 2 | — | AR aging bucket 5 threshold (days) |
| 27 | BKSY_AR_CHKACT | INTEGER | 2 | — | AR default check bank account slot number |
| 28 | BKSY_AR_DISCDPT | STRING | 4 | — | AR sales discount GL department |
| 29 | BKSY_AR_DISCGL | STRING | 10 | — | AR sales discount GL account |
| 30 | BKSY_AR_ENDDESC_1 | STRING | 30 | — | AR invoice end-of-document description line 1 |
| 31 | BKSY_AR_ENDDESC_2 | STRING | 30 | — | AR invoice end-of-document description line 2 |
| 32 | BKSY_AR_ENDDESC_3 | STRING | 30 | — | AR invoice end-of-document description line 3 |
| 33 | BKSY_AR_ENDDESC_4 | STRING | 30 | — | AR invoice end-of-document description line 4 |
| 34 | BKSY_AR_ENDDESC_5 | STRING | 30 | — | AR invoice end-of-document description line 5 |
| 35 | BKSY_AR_ENTBY | STRING | 5 | — | AR default entry-by operator code |
| 36 | BKSY_AR_FREIGHT | STRING | 10 | — | AR freight GL account |
| 37 | BKSY_AR_FRGTDPT | STRING | 4 | — | AR freight GL department |
| 38 | BKSY_AR_GLACT | STRING | 10 | — | AR default accounts receivable GL account |
| 39 | BKSY_AR_GLDPT | STRING | 4 | — | AR default GL department |
| 40 | BKSY_AR_INT_DAY | INTEGER | 2 | — | AR finance charge grace period (days) |
| 41 | BKSY_AR_INT_RTE | NUMERIC | 8 | 2 | AR finance charge interest rate (%) |
| 42 | BKSY_AR_PEL | STRING | 1 | — | AR price/exchange lock flag |
| 43 | BKSY_AR_RECNUM | NUMERIC | 8 | — | AR last record number (auto-increment) |
| 44 | BKSY_AR_SHP_VIA | STRING | 15 | — | AR default ship-via code |
| 45 | BKSY_AR_SLSP | INTEGER | 2 | — | AR default salesperson code |
| 46 | BKSY_AR_TAXABL | STRING | 1 | — | AR default taxable flag (Y/N) |
| 47 | BKSY_AR_TURNOFF | STRING | 1 | — | AR module disable flag (Y=off) |
| 48 | BKSY_ARINV_NUM | NUMERIC | 8 | — | Last AR invoice number issued |
| 49 | BKSY_ARSO_NUM | NUMERIC | 8 | — | Last AR/SO order number issued |
| 50 | BKSY_AUTO_BO | STRING | 1 | — | Auto backorder creation flag (Y/N) |
| 51 | BKSY_CHK_BAL_1 | NUMERIC | 8 | 2 | Current balance for bank account 1 |
| 52 | BKSY_CHK_BAL_2 | NUMERIC | 8 | 2 | Current balance for bank account 2 |
| 53 | BKSY_CHK_BAL_3 | NUMERIC | 8 | 2 | Current balance for bank account 3 |
| 54 | BKSY_CHK_BAL_4 | NUMERIC | 8 | 2 | Current balance for bank account 4 |
| 55 | BKSY_CHK_BAL_5 | NUMERIC | 8 | 2 | Current balance for bank account 5 |
| 56 | BKSY_CHK_BAL_6 | NUMERIC | 8 | 2 | Current balance for bank account 6 |
| 57 | BKSY_CHK_BAL_7 | NUMERIC | 8 | 2 | Current balance for bank account 7 |
| 58 | BKSY_CHK_BAL_8 | NUMERIC | 8 | 2 | Current balance for bank account 8 |
| 59 | BKSY_CHK_BAL_9 | NUMERIC | 8 | 2 | Current balance for bank account 9 |
| 60 | BKSY_CHK_CHKACT_1 | STRING | 10 | — | GL account number for bank account 1 |
| 61 | BKSY_CHK_CHKACT_2 | STRING | 10 | — | GL account number for bank account 2 |
| 62 | BKSY_CHK_CHKACT_3 | STRING | 10 | — | GL account number for bank account 3 |
| 63 | BKSY_CHK_CHKACT_4 | STRING | 10 | — | GL account number for bank account 4 |
| 64 | BKSY_CHK_CHKACT_5 | STRING | 10 | — | GL account number for bank account 5 |
| 65 | BKSY_CHK_CHKACT_6 | STRING | 10 | — | GL account number for bank account 6 |
| 66 | BKSY_CHK_CHKACT_7 | STRING | 10 | — | GL account number for bank account 7 |
| 67 | BKSY_CHK_CHKACT_8 | STRING | 10 | — | GL account number for bank account 8 |
| 68 | BKSY_CHK_CHKACT_9 | STRING | 10 | — | GL account number for bank account 9 |
| 69 | BKSY_CHK_CHKCUR_1 | STRING | 3 | — | Currency code for bank account 1 |
| 70 | BKSY_CHK_CHKCUR_2 | STRING | 3 | — | Currency code for bank account 2 |
| 71 | BKSY_CHK_CHKCUR_3 | STRING | 3 | — | Currency code for bank account 3 |
| 72 | BKSY_CHK_CHKCUR_4 | STRING | 3 | — | Currency code for bank account 4 |
| 73 | BKSY_CHK_CHKCUR_5 | STRING | 3 | — | Currency code for bank account 5 |
| 74 | BKSY_CHK_CHKCUR_6 | STRING | 3 | — | Currency code for bank account 6 |
| 75 | BKSY_CHK_CHKCUR_7 | STRING | 3 | — | Currency code for bank account 7 |
| 76 | BKSY_CHK_CHKCUR_8 | STRING | 3 | — | Currency code for bank account 8 |
| 77 | BKSY_CHK_CHKCUR_9 | STRING | 3 | — | Currency code for bank account 9 |
| 78 | BKSY_CHK_CHKDPT_1 | STRING | 4 | — | Department code for bank account 1 |
| 79 | BKSY_CHK_CHKDPT_2 | STRING | 4 | — | Department code for bank account 2 |
| 80 | BKSY_CHK_CHKDPT_3 | STRING | 4 | — | Department code for bank account 3 |
| 81 | BKSY_CHK_CHKDPT_4 | STRING | 4 | — | Department code for bank account 4 |
| 82 | BKSY_CHK_CHKDPT_5 | STRING | 4 | — | Department code for bank account 5 |
| 83 | BKSY_CHK_CHKDPT_6 | STRING | 4 | — | Department code for bank account 6 |
| 84 | BKSY_CHK_CHKDPT_7 | STRING | 4 | — | Department code for bank account 7 |
| 85 | BKSY_CHK_CHKDPT_8 | STRING | 4 | — | Department code for bank account 8 |
| 86 | BKSY_CHK_CHKDPT_9 | STRING | 4 | — | Department code for bank account 9 |
| 87 | BKSY_CHK_NAME_1 | STRING | 30 | — | Bank account 1 name/description |
| 88 | BKSY_CHK_NAME_2 | STRING | 30 | — | Bank account 2 name/description |
| 89 | BKSY_CHK_NAME_3 | STRING | 30 | — | Bank account 3 name/description |
| 90 | BKSY_CHK_NAME_4 | STRING | 30 | — | Bank account 4 name/description |
| 91 | BKSY_CHK_NAME_5 | STRING | 30 | — | Bank account 5 name/description |
| 92 | BKSY_CHK_NAME_6 | STRING | 30 | — | Bank account 6 name/description |
| 93 | BKSY_CHK_NAME_7 | STRING | 30 | — | Bank account 7 name/description |
| 94 | BKSY_CHK_NAME_8 | STRING | 30 | — | Bank account 8 name/description |
| 95 | BKSY_CHK_NAME_9 | STRING | 30 | — | Bank account 9 name/description |
| 96 | BKSY_CHK_NUM_1 | NUMERIC | 8 | — | Last check number issued from bank account 1 |
| 97 | BKSY_CHK_NUM_2 | NUMERIC | 8 | — | Last check number issued from bank account 2 |
| 98 | BKSY_CHK_NUM_3 | NUMERIC | 8 | — | Last check number issued from bank account 3 |
| 99 | BKSY_CHK_NUM_4 | NUMERIC | 8 | — | Last check number issued from bank account 4 |
| 100 | BKSY_CHK_NUM_5 | NUMERIC | 8 | — | Last check number issued from bank account 5 |
| 101 | BKSY_CHK_NUM_6 | NUMERIC | 8 | — | Last check number issued from bank account 6 |
| 102 | BKSY_CHK_NUM_7 | NUMERIC | 8 | — | Last check number issued from bank account 7 |
| 103 | BKSY_CHK_NUM_8 | NUMERIC | 8 | — | Last check number issued from bank account 8 |
| 104 | BKSY_CHK_NUM_9 | NUMERIC | 8 | — | Last check number issued from bank account 9 |
| 105 | BKSY_COMP_ADD1 | STRING | 25 | — | Company address line 1 |
| 106 | BKSY_COMP_ADD2 | STRING | 25 | — | Company address line 2 |
| 107 | BKSY_COMP_CSZ | STRING | 25 | — | Company city, state, and zip |
| 108 | BKSY_COMP_NAME | STRING | 25 | — | Company name |
| 109 | BKSY_EXTRA | STRING | 173 | — | Reserved/overflow extra field |
| 110 | BKSY_FISCAL_YR | DATE | 4 | — | Current fiscal year start date |
| 111 | BKSY_FORM_CMPNY | STRING | 1 | — | Print company name on forms flag (Y/N) |
| 112 | BKSY_GJ_NUM | NUMERIC | 8 | — | Last general journal entry number |
| 113 | BKSY_GJ_RECNUM | NUMERIC | 8 | — | GL general journal last record number |
| 114 | BKSY_GL_ARINTR | STRING | 10 | — | GL AR interest/finance charge account |
| 115 | BKSY_GL_CLRING | STRING | 10 | — | GL clearing account |
| 116 | BKSY_GL_RELYR | STRING | 10 | — | GL retained earnings prior year account |
| 117 | BKSY_GL_RETEARN | STRING | 10 | — | GL retained earnings account |
| 118 | BKSY_GLDPT_ARIN | STRING | 4 | — | GL department for AR interest account |
| 119 | BKSY_GLDPT_CLR | STRING | 4 | — | GL department for clearing account |
| 120 | BKSY_GLDPT_RELY | STRING | 4 | — | GL department for prior year retained earnings |
| 121 | BKSY_GLDPT_RET | STRING | 4 | — | GL department for retained earnings |
| 122 | BKSY_PLAIN_CHKS | STRING | 1 | — | Use plain paper for checks flag (Y/N) |
| 123 | BKSY_PLAIN_INV | STRING | 1 | — | Use plain paper for invoices flag (Y/N) |
| 124 | BKSY_PLAIN_PO | STRING | 1 | — | Use plain paper for purchase orders flag (Y/N) |
| 125 | BKSY_PLAIN_STMT | STRING | 1 | — | Use plain paper for statements flag (Y/N) |
| 126 | BKSY_PO_FREIGHT | STRING | 10 | — | PO freight GL account |
| 127 | BKSY_PO_FRGTDPT | STRING | 4 | — | PO freight GL department |
| 128 | BKSY_PO_INR | STRING | 10 | — | PO inventory receipt GL account |
| 129 | BKSY_PO_INRDPT | STRING | 4 | — | PO inventory receipt GL department |
| 130 | BKSY_PO_RNI | STRING | 10 | — | PO received-not-invoiced GL account |
| 131 | BKSY_PO_RNIDPT | STRING | 4 | — | PO received-not-invoiced GL department |
| 132 | BKSY_PO_TAXDPT | STRING | 4 | — | PO tax GL department |
| 133 | BKSY_PO_TAXGL | STRING | 10 | — | PO tax GL account |
| 134 | BKSY_PR_CHKACT | INTEGER | 2 | — | Payroll check bank account slot number |
| 135 | BKSY_PR_ODNAME_1 | STRING | 12 | — | Payroll other deduction name 1 |
| 136 | BKSY_PR_ODNAME_2 | STRING | 12 | — | Payroll other deduction name 2 |
| 137 | BKSY_PR_ODNAME_3 | STRING | 12 | — | Payroll other deduction name 3 |
| 138 | BKSY_PR_ODNAME_4 | STRING | 12 | — | Payroll other deduction name 4 |
| 139 | BKSY_PR_ODNAME_5 | STRING | 12 | — | Payroll other deduction name 5 |
| 140 | BKSY_PR_ODNAME_6 | STRING | 12 | — | Payroll other deduction name 6 |
| 141 | BKSY_PRGS_WHR | STRING | 40 | — | Progress/status display text |
| 142 | BKSY_RTS_DEF | STRING | 1 | — | Default routing flag |
| 143 | BKSY_TAL | STRING | 1 | — | Transaction audit log enabled flag (Y/N) |
| 144 | BKSY_TAX_GLACT | STRING | 10 | — | Sales tax GL account |
| 145 | BKSY_TAX_GLDPT | STRING | 4 | — | Sales tax GL department |
| 146 | BKSY_TAX_RATE | NUMERIC | 8 | 2 | Default sales tax rate (%) |
| 147 | BKSY_TERMS_1 | STRING | 20 | — | Payment terms code 1 |
| 148 | BKSY_TERMS_10 | STRING | 20 | — | Payment terms code 10 |
| 149 | BKSY_TERMS_11 | STRING | 20 | — | Payment terms code 11 |
| 150 | BKSY_TERMS_12 | STRING | 20 | — | Payment terms code 12 |
| 151 | BKSY_TERMS_13 | STRING | 20 | — | Payment terms code 13 |
| 152 | BKSY_TERMS_14 | STRING | 20 | — | Payment terms code 14 |
| 153 | BKSY_TERMS_15 | STRING | 20 | — | Payment terms code 15 |
| 154 | BKSY_TERMS_16 | STRING | 20 | — | Payment terms code 16 |
| 155 | BKSY_TERMS_17 | STRING | 20 | — | Payment terms code 17 |
| 156 | BKSY_TERMS_18 | STRING | 20 | — | Payment terms code 18 |
| 157 | BKSY_TERMS_19 | STRING | 20 | — | Payment terms code 19 |
| 158 | BKSY_TERMS_2 | STRING | 20 | — | Payment terms code 2 |
| 159 | BKSY_TERMS_20 | STRING | 20 | — | Payment terms code 20 |
| 160 | BKSY_TERMS_3 | STRING | 20 | — | Payment terms code 3 |
| 161 | BKSY_TERMS_4 | STRING | 20 | — | Payment terms code 4 |
| 162 | BKSY_TERMS_5 | STRING | 20 | — | Payment terms code 5 |
| 163 | BKSY_TERMS_6 | STRING | 20 | — | Payment terms code 6 |
| 164 | BKSY_TERMS_7 | STRING | 20 | — | Payment terms code 7 |
| 165 | BKSY_TERMS_8 | STRING | 20 | — | Payment terms code 8 |
| 166 | BKSY_TERMS_9 | STRING | 20 | — | Payment terms code 9 |
| 167 | BKSY_TRM_AMT_1 | INTEGER | 2 | — | Minimum invoice amount threshold for terms slot 1 |
| 168 | BKSY_TRM_AMT_10 | INTEGER | 2 | — | Minimum invoice amount threshold for terms slot 10 |
| 169 | BKSY_TRM_AMT_11 | INTEGER | 2 | — | Minimum invoice amount threshold for terms slot 11 |
| 170 | BKSY_TRM_AMT_12 | INTEGER | 2 | — | Minimum invoice amount threshold for terms slot 12 |
| 171 | BKSY_TRM_AMT_13 | INTEGER | 2 | — | Minimum invoice amount threshold for terms slot 13 |
| 172 | BKSY_TRM_AMT_14 | INTEGER | 2 | — | Minimum invoice amount threshold for terms slot 14 |
| 173 | BKSY_TRM_AMT_15 | INTEGER | 2 | — | Minimum invoice amount threshold for terms slot 15 |
| 174 | BKSY_TRM_AMT_16 | INTEGER | 2 | — | Minimum invoice amount threshold for terms slot 16 |
| 175 | BKSY_TRM_AMT_17 | INTEGER | 2 | — | Minimum invoice amount threshold for terms slot 17 |
| 176 | BKSY_TRM_AMT_18 | INTEGER | 2 | — | Minimum invoice amount threshold for terms slot 18 |
| 177 | BKSY_TRM_AMT_19 | INTEGER | 2 | — | Minimum invoice amount threshold for terms slot 19 |
| 178 | BKSY_TRM_AMT_2 | INTEGER | 2 | — | Minimum invoice amount threshold for terms slot 2 |
| 179 | BKSY_TRM_AMT_20 | INTEGER | 2 | — | Minimum invoice amount threshold for terms slot 20 |
| 180 | BKSY_TRM_AMT_3 | INTEGER | 2 | — | Minimum invoice amount threshold for terms slot 3 |
| 181 | BKSY_TRM_AMT_4 | INTEGER | 2 | — | Minimum invoice amount threshold for terms slot 4 |
| 182 | BKSY_TRM_AMT_5 | INTEGER | 2 | — | Minimum invoice amount threshold for terms slot 5 |
| 183 | BKSY_TRM_AMT_6 | INTEGER | 2 | — | Minimum invoice amount threshold for terms slot 6 |
| 184 | BKSY_TRM_AMT_7 | INTEGER | 2 | — | Minimum invoice amount threshold for terms slot 7 |
| 185 | BKSY_TRM_AMT_8 | INTEGER | 2 | — | Minimum invoice amount threshold for terms slot 8 |
| 186 | BKSY_TRM_AMT_9 | INTEGER | 2 | — | Minimum invoice amount threshold for terms slot 9 |
| 187 | BKSY_TRM_DAY_1 | INTEGER | 2 | — | Net due days for payment terms slot 1 |
| 188 | BKSY_TRM_DAY_10 | INTEGER | 2 | — | Net due days for payment terms slot 10 |
| 189 | BKSY_TRM_DAY_11 | INTEGER | 2 | — | Net due days for payment terms slot 11 |
| 190 | BKSY_TRM_DAY_12 | INTEGER | 2 | — | Net due days for payment terms slot 12 |
| 191 | BKSY_TRM_DAY_13 | INTEGER | 2 | — | Net due days for payment terms slot 13 |
| 192 | BKSY_TRM_DAY_14 | INTEGER | 2 | — | Net due days for payment terms slot 14 |
| 193 | BKSY_TRM_DAY_15 | INTEGER | 2 | — | Net due days for payment terms slot 15 |
| 194 | BKSY_TRM_DAY_16 | INTEGER | 2 | — | Net due days for payment terms slot 16 |
| 195 | BKSY_TRM_DAY_17 | INTEGER | 2 | — | Net due days for payment terms slot 17 |
| 196 | BKSY_TRM_DAY_18 | INTEGER | 2 | — | Net due days for payment terms slot 18 |
| 197 | BKSY_TRM_DAY_19 | INTEGER | 2 | — | Net due days for payment terms slot 19 |
| 198 | BKSY_TRM_DAY_2 | INTEGER | 2 | — | Net due days for payment terms slot 2 |
| 199 | BKSY_TRM_DAY_20 | INTEGER | 2 | — | Net due days for payment terms slot 20 |
| 200 | BKSY_TRM_DAY_3 | INTEGER | 2 | — | Net due days for payment terms slot 3 |
| 201 | BKSY_TRM_DAY_4 | INTEGER | 2 | — | Net due days for payment terms slot 4 |
| 202 | BKSY_TRM_DAY_5 | INTEGER | 2 | — | Net due days for payment terms slot 5 |
| 203 | BKSY_TRM_DAY_6 | INTEGER | 2 | — | Net due days for payment terms slot 6 |
| 204 | BKSY_TRM_DAY_7 | INTEGER | 2 | — | Net due days for payment terms slot 7 |
| 205 | BKSY_TRM_DAY_8 | INTEGER | 2 | — | Net due days for payment terms slot 8 |
| 206 | BKSY_TRM_DAY_9 | INTEGER | 2 | — | Net due days for payment terms slot 9 |
| 207 | BKSY_TRM_DISC_1 | NUMERIC | 8 | 2 | Discount percentage for payment terms 1 |
| 208 | BKSY_TRM_DISC_10 | NUMERIC | 8 | 2 | Discount percentage for payment terms 10 |
| 209 | BKSY_TRM_DISC_11 | NUMERIC | 8 | 2 | Discount percentage for payment terms 11 |
| 210 | BKSY_TRM_DISC_12 | NUMERIC | 8 | 2 | Discount percentage for payment terms 12 |
| 211 | BKSY_TRM_DISC_13 | NUMERIC | 8 | 2 | Discount percentage for payment terms 13 |
| 212 | BKSY_TRM_DISC_14 | NUMERIC | 8 | 2 | Discount percentage for payment terms 14 |
| 213 | BKSY_TRM_DISC_15 | NUMERIC | 8 | 2 | Discount percentage for payment terms 15 |
| 214 | BKSY_TRM_DISC_16 | NUMERIC | 8 | 2 | Discount percentage for payment terms 16 |
| 215 | BKSY_TRM_DISC_17 | NUMERIC | 8 | 2 | Discount percentage for payment terms 17 |
| 216 | BKSY_TRM_DISC_18 | NUMERIC | 8 | 2 | Discount percentage for payment terms 18 |
| 217 | BKSY_TRM_DISC_19 | NUMERIC | 8 | 2 | Discount percentage for payment terms 19 |
| 218 | BKSY_TRM_DISC_2 | NUMERIC | 8 | 2 | Discount percentage for payment terms 2 |
| 219 | BKSY_TRM_DISC_20 | NUMERIC | 8 | 2 | Discount percentage for payment terms 20 |
| 220 | BKSY_TRM_DISC_3 | NUMERIC | 8 | 2 | Discount percentage for payment terms 3 |
| 221 | BKSY_TRM_DISC_4 | NUMERIC | 8 | 2 | Discount percentage for payment terms 4 |
| 222 | BKSY_TRM_DISC_5 | NUMERIC | 8 | 2 | Discount percentage for payment terms 5 |
| 223 | BKSY_TRM_DISC_6 | NUMERIC | 8 | 2 | Discount percentage for payment terms 6 |
| 224 | BKSY_TRM_DISC_7 | NUMERIC | 8 | 2 | Discount percentage for payment terms 7 |
| 225 | BKSY_TRM_DISC_8 | NUMERIC | 8 | 2 | Discount percentage for payment terms 8 |
| 226 | BKSY_TRM_DISC_9 | NUMERIC | 8 | 2 | Discount percentage for payment terms 9 |
| 227 | BKSY_TRM_EOM_1 | STRING | 1 | — | End-of-month flag for payment terms 1 (Y/N) |
| 228 | BKSY_TRM_EOM_10 | STRING | 1 | — | End-of-month flag for payment terms 10 (Y/N) |
| 229 | BKSY_TRM_EOM_11 | STRING | 1 | — | End-of-month flag for payment terms 11 (Y/N) |
| 230 | BKSY_TRM_EOM_12 | STRING | 1 | — | End-of-month flag for payment terms 12 (Y/N) |
| 231 | BKSY_TRM_EOM_13 | STRING | 1 | — | End-of-month flag for payment terms 13 (Y/N) |
| 232 | BKSY_TRM_EOM_14 | STRING | 1 | — | End-of-month flag for payment terms 14 (Y/N) |
| 233 | BKSY_TRM_EOM_15 | STRING | 1 | — | End-of-month flag for payment terms 15 (Y/N) |
| 234 | BKSY_TRM_EOM_16 | STRING | 1 | — | End-of-month flag for payment terms 16 (Y/N) |
| 235 | BKSY_TRM_EOM_17 | STRING | 1 | — | End-of-month flag for payment terms 17 (Y/N) |
| 236 | BKSY_TRM_EOM_18 | STRING | 1 | — | End-of-month flag for payment terms 18 (Y/N) |
| 237 | BKSY_TRM_EOM_19 | STRING | 1 | — | End-of-month flag for payment terms 19 (Y/N) |
| 238 | BKSY_TRM_EOM_2 | STRING | 1 | — | End-of-month flag for payment terms 2 (Y/N) |
| 239 | BKSY_TRM_EOM_20 | STRING | 1 | — | End-of-month flag for payment terms 20 (Y/N) |
| 240 | BKSY_TRM_EOM_3 | STRING | 1 | — | End-of-month flag for payment terms 3 (Y/N) |
| 241 | BKSY_TRM_EOM_4 | STRING | 1 | — | End-of-month flag for payment terms 4 (Y/N) |
| 242 | BKSY_TRM_EOM_5 | STRING | 1 | — | End-of-month flag for payment terms 5 (Y/N) |
| 243 | BKSY_TRM_EOM_6 | STRING | 1 | — | End-of-month flag for payment terms 6 (Y/N) |
| 244 | BKSY_TRM_EOM_7 | STRING | 1 | — | End-of-month flag for payment terms 7 (Y/N) |
| 245 | BKSY_TRM_EOM_8 | STRING | 1 | — | End-of-month flag for payment terms 8 (Y/N) |
| 246 | BKSY_TRM_EOM_9 | STRING | 1 | — | End-of-month flag for payment terms 9 (Y/N) |
| 247 | BKSY_TRM_MAX_1 | INTEGER | 2 | — | Discount cutoff days for payment terms slot 1 |
| 248 | BKSY_TRM_MAX_10 | INTEGER | 2 | — | Discount cutoff days for payment terms slot 10 |
| 249 | BKSY_TRM_MAX_11 | INTEGER | 2 | — | Discount cutoff days for payment terms slot 11 |
| 250 | BKSY_TRM_MAX_12 | INTEGER | 2 | — | Discount cutoff days for payment terms slot 12 |
| 251 | BKSY_TRM_MAX_13 | INTEGER | 2 | — | Discount cutoff days for payment terms slot 13 |
| 252 | BKSY_TRM_MAX_14 | INTEGER | 2 | — | Discount cutoff days for payment terms slot 14 |
| 253 | BKSY_TRM_MAX_15 | INTEGER | 2 | — | Discount cutoff days for payment terms slot 15 |
| 254 | BKSY_TRM_MAX_16 | INTEGER | 2 | — | Discount cutoff days for payment terms slot 16 |
| 255 | BKSY_TRM_MAX_17 | INTEGER | 2 | — | Discount cutoff days for payment terms slot 17 |
| 256 | BKSY_TRM_MAX_18 | INTEGER | 2 | — | Discount cutoff days for payment terms slot 18 |
| 257 | BKSY_TRM_MAX_19 | INTEGER | 2 | — | Discount cutoff days for payment terms slot 19 |
| 258 | BKSY_TRM_MAX_2 | INTEGER | 2 | — | Discount cutoff days for payment terms slot 2 |
| 259 | BKSY_TRM_MAX_20 | INTEGER | 2 | — | Discount cutoff days for payment terms slot 20 |
| 260 | BKSY_TRM_MAX_3 | INTEGER | 2 | — | Discount cutoff days for payment terms slot 3 |
| 261 | BKSY_TRM_MAX_4 | INTEGER | 2 | — | Discount cutoff days for payment terms slot 4 |
| 262 | BKSY_TRM_MAX_5 | INTEGER | 2 | — | Discount cutoff days for payment terms slot 5 |
| 263 | BKSY_TRM_MAX_6 | INTEGER | 2 | — | Discount cutoff days for payment terms slot 6 |
| 264 | BKSY_TRM_MAX_7 | INTEGER | 2 | — | Discount cutoff days for payment terms slot 7 |
| 265 | BKSY_TRM_MAX_8 | INTEGER | 2 | — | Discount cutoff days for payment terms slot 8 |
| 266 | BKSY_TRM_MAX_9 | INTEGER | 2 | — | Discount cutoff days for payment terms slot 9 |
| 267 | BKSY_TRM_TYP_1 | STRING | 1 | — | Terms type code 1 (e.g. N=Net, D=Discount) |
| 268 | BKSY_TRM_TYP_10 | STRING | 1 | — | Terms type code 10 (e.g. N=Net, D=Discount) |
| 269 | BKSY_TRM_TYP_11 | STRING | 1 | — | Terms type code 11 (e.g. N=Net, D=Discount) |
| 270 | BKSY_TRM_TYP_12 | STRING | 1 | — | Terms type code 12 (e.g. N=Net, D=Discount) |
| 271 | BKSY_TRM_TYP_13 | STRING | 1 | — | Terms type code 13 (e.g. N=Net, D=Discount) |
| 272 | BKSY_TRM_TYP_14 | STRING | 1 | — | Terms type code 14 (e.g. N=Net, D=Discount) |
| 273 | BKSY_TRM_TYP_15 | STRING | 1 | — | Terms type code 15 (e.g. N=Net, D=Discount) |
| 274 | BKSY_TRM_TYP_16 | STRING | 1 | — | Terms type code 16 (e.g. N=Net, D=Discount) |
| 275 | BKSY_TRM_TYP_17 | STRING | 1 | — | Terms type code 17 (e.g. N=Net, D=Discount) |
| 276 | BKSY_TRM_TYP_18 | STRING | 1 | — | Terms type code 18 (e.g. N=Net, D=Discount) |
| 277 | BKSY_TRM_TYP_19 | STRING | 1 | — | Terms type code 19 (e.g. N=Net, D=Discount) |
| 278 | BKSY_TRM_TYP_2 | STRING | 1 | — | Terms type code 2 (e.g. N=Net, D=Discount) |
| 279 | BKSY_TRM_TYP_20 | STRING | 1 | — | Terms type code 20 (e.g. N=Net, D=Discount) |
| 280 | BKSY_TRM_TYP_3 | STRING | 1 | — | Terms type code 3 (e.g. N=Net, D=Discount) |
| 281 | BKSY_TRM_TYP_4 | STRING | 1 | — | Terms type code 4 (e.g. N=Net, D=Discount) |
| 282 | BKSY_TRM_TYP_5 | STRING | 1 | — | Terms type code 5 (e.g. N=Net, D=Discount) |
| 283 | BKSY_TRM_TYP_6 | STRING | 1 | — | Terms type code 6 (e.g. N=Net, D=Discount) |
| 284 | BKSY_TRM_TYP_7 | STRING | 1 | — | Terms type code 7 (e.g. N=Net, D=Discount) |
| 285 | BKSY_TRM_TYP_8 | STRING | 1 | — | Terms type code 8 (e.g. N=Net, D=Discount) |
| 286 | BKSY_TRM_TYP_9 | STRING | 1 | — | Terms type code 9 (e.g. N=Net, D=Discount) |

## BKYSMSTR
**SYSTEM MASTER FILE 2**

Fields: 355

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKYS_DATE_1 | DATE | 4 | — | User-defined date value 1 |
| 2 | BKYS_DATE_2 | DATE | 4 | — | User-defined date value 2 |
| 3 | BKYS_DATE_3 | DATE | 4 | — | User-defined date value 3 |
| 4 | BKYS_DATE_4 | DATE | 4 | — | User-defined date value 4 |
| 5 | BKYS_DATE_5 | DATE | 4 | — | User-defined date value 5 |
| 6 | BKYS_DESC_1 | STRING | 25 | — | User-defined description 1 |
| 7 | BKYS_DESC_2 | STRING | 25 | — | User-defined description 2 |
| 8 | BKYS_DESC_3 | STRING | 25 | — | User-defined description 3 |
| 9 | BKYS_DESC_4 | STRING | 25 | — | User-defined description 4 |
| 10 | BKYS_DESC_5 | STRING | 25 | — | User-defined description 5 |
| 11 | BKYS_GLDPT_1 | STRING | 4 | — | GL department code 1 |
| 12 | BKYS_GLDPT_10 | STRING | 4 | — | GL department code 10 |
| 13 | BKYS_GLDPT_11 | STRING | 4 | — | GL department code 11 |
| 14 | BKYS_GLDPT_12 | STRING | 4 | — | GL department code 12 |
| 15 | BKYS_GLDPT_13 | STRING | 4 | — | GL department code 13 |
| 16 | BKYS_GLDPT_14 | STRING | 4 | — | GL department code 14 |
| 17 | BKYS_GLDPT_15 | STRING | 4 | — | GL department code 15 |
| 18 | BKYS_GLDPT_16 | STRING | 4 | — | GL department code 16 |
| 19 | BKYS_GLDPT_17 | STRING | 4 | — | GL department code 17 |
| 20 | BKYS_GLDPT_18 | STRING | 4 | — | GL department code 18 |
| 21 | BKYS_GLDPT_19 | STRING | 4 | — | GL department code 19 |
| 22 | BKYS_GLDPT_2 | STRING | 4 | — | GL department code 2 |
| 23 | BKYS_GLDPT_20 | STRING | 4 | — | GL department code 20 |
| 24 | BKYS_GLDPT_21 | STRING | 4 | — | GL department code 21 |
| 25 | BKYS_GLDPT_22 | STRING | 4 | — | GL department code 22 |
| 26 | BKYS_GLDPT_23 | STRING | 4 | — | GL department code 23 |
| 27 | BKYS_GLDPT_24 | STRING | 4 | — | GL department code 24 |
| 28 | BKYS_GLDPT_25 | STRING | 4 | — | GL department code 25 |
| 29 | BKYS_GLDPT_26 | STRING | 4 | — | GL department code 26 |
| 30 | BKYS_GLDPT_27 | STRING | 4 | — | GL department code 27 |
| 31 | BKYS_GLDPT_28 | STRING | 4 | — | GL department code 28 |
| 32 | BKYS_GLDPT_29 | STRING | 4 | — | GL department code 29 |
| 33 | BKYS_GLDPT_3 | STRING | 4 | — | GL department code 3 |
| 34 | BKYS_GLDPT_30 | STRING | 4 | — | GL department code 30 |
| 35 | BKYS_GLDPT_31 | STRING | 4 | — | GL department code 31 |
| 36 | BKYS_GLDPT_32 | STRING | 4 | — | GL department code 32 |
| 37 | BKYS_GLDPT_33 | STRING | 4 | — | GL department code 33 |
| 38 | BKYS_GLDPT_34 | STRING | 4 | — | GL department code 34 |
| 39 | BKYS_GLDPT_35 | STRING | 4 | — | GL department code 35 |
| 40 | BKYS_GLDPT_36 | STRING | 4 | — | GL department code 36 |
| 41 | BKYS_GLDPT_37 | STRING | 4 | — | GL department code 37 |
| 42 | BKYS_GLDPT_38 | STRING | 4 | — | GL department code 38 |
| 43 | BKYS_GLDPT_39 | STRING | 4 | — | GL department code 39 |
| 44 | BKYS_GLDPT_4 | STRING | 4 | — | GL department code 4 |
| 45 | BKYS_GLDPT_40 | STRING | 4 | — | GL department code 40 |
| 46 | BKYS_GLDPT_5 | STRING | 4 | — | GL department code 5 |
| 47 | BKYS_GLDPT_6 | STRING | 4 | — | GL department code 6 |
| 48 | BKYS_GLDPT_7 | STRING | 4 | — | GL department code 7 |
| 49 | BKYS_GLDPT_8 | STRING | 4 | — | GL department code 8 |
| 50 | BKYS_GLDPT_9 | STRING | 4 | — | GL department code 9 |
| 51 | BKYS_GLNUM_1 | STRING | 10 | — | GL account number 1 |
| 52 | BKYS_GLNUM_10 | STRING | 10 | — | GL account number 10 |
| 53 | BKYS_GLNUM_11 | STRING | 10 | — | GL account number 11 |
| 54 | BKYS_GLNUM_12 | STRING | 10 | — | GL account number 12 |
| 55 | BKYS_GLNUM_13 | STRING | 10 | — | GL account number 13 |
| 56 | BKYS_GLNUM_14 | STRING | 10 | — | GL account number 14 |
| 57 | BKYS_GLNUM_15 | STRING | 10 | — | GL account number 15 |
| 58 | BKYS_GLNUM_16 | STRING | 10 | — | GL account number 16 |
| 59 | BKYS_GLNUM_17 | STRING | 10 | — | GL account number 17 |
| 60 | BKYS_GLNUM_18 | STRING | 10 | — | GL account number 18 |
| 61 | BKYS_GLNUM_19 | STRING | 10 | — | GL account number 19 |
| 62 | BKYS_GLNUM_2 | STRING | 10 | — | GL account number 2 |
| 63 | BKYS_GLNUM_20 | STRING | 10 | — | GL account number 20 |
| 64 | BKYS_GLNUM_21 | STRING | 10 | — | GL account number 21 |
| 65 | BKYS_GLNUM_22 | STRING | 10 | — | GL account number 22 |
| 66 | BKYS_GLNUM_23 | STRING | 10 | — | GL account number 23 |
| 67 | BKYS_GLNUM_24 | STRING | 10 | — | GL account number 24 |
| 68 | BKYS_GLNUM_25 | STRING | 10 | — | GL account number 25 |
| 69 | BKYS_GLNUM_26 | STRING | 10 | — | GL account number 26 |
| 70 | BKYS_GLNUM_27 | STRING | 10 | — | GL account number 27 |
| 71 | BKYS_GLNUM_28 | STRING | 10 | — | GL account number 28 |
| 72 | BKYS_GLNUM_29 | STRING | 10 | — | GL account number 29 |
| 73 | BKYS_GLNUM_3 | STRING | 10 | — | GL account number 3 |
| 74 | BKYS_GLNUM_30 | STRING | 10 | — | GL account number 30 |
| 75 | BKYS_GLNUM_31 | STRING | 10 | — | GL account number 31 |
| 76 | BKYS_GLNUM_32 | STRING | 10 | — | GL account number 32 |
| 77 | BKYS_GLNUM_33 | STRING | 10 | — | GL account number 33 |
| 78 | BKYS_GLNUM_34 | STRING | 10 | — | GL account number 34 |
| 79 | BKYS_GLNUM_35 | STRING | 10 | — | GL account number 35 |
| 80 | BKYS_GLNUM_36 | STRING | 10 | — | GL account number 36 |
| 81 | BKYS_GLNUM_37 | STRING | 10 | — | GL account number 37 |
| 82 | BKYS_GLNUM_38 | STRING | 10 | — | GL account number 38 |
| 83 | BKYS_GLNUM_39 | STRING | 10 | — | GL account number 39 |
| 84 | BKYS_GLNUM_4 | STRING | 10 | — | GL account number 4 |
| 85 | BKYS_GLNUM_40 | STRING | 10 | — | GL account number 40 |
| 86 | BKYS_GLNUM_5 | STRING | 10 | — | GL account number 5 |
| 87 | BKYS_GLNUM_6 | STRING | 10 | — | GL account number 6 |
| 88 | BKYS_GLNUM_7 | STRING | 10 | — | GL account number 7 |
| 89 | BKYS_GLNUM_8 | STRING | 10 | — | GL account number 8 |
| 90 | BKYS_GLNUM_9 | STRING | 10 | — | GL account number 9 |
| 91 | BKYS_INVNUM | NUMERIC | 8 | — | Last inventory transaction number |
| 92 | BKYS_NUM_1 | NUMERIC | 8 | — | User-defined numeric value 1 |
| 93 | BKYS_NUM_2 | NUMERIC | 8 | — | User-defined numeric value 2 |
| 94 | BKYS_NUM_3 | NUMERIC | 8 | — | User-defined numeric value 3 |
| 95 | BKYS_NUM_4 | NUMERIC | 8 | — | User-defined numeric value 4 |
| 96 | BKYS_NUM_5 | NUMERIC | 8 | — | User-defined numeric value 5 |
| 97 | BKYS_QCNUM | NUMERIC | 8 | — | Last quality control number |
| 98 | BKYS_RBNUM | NUMERIC | 8 | — | Last ReportBuilder report number |
| 99 | BKYS_REQNUM | NUMERIC | 8 | — | Last requisition number |
| 100 | BKYS_VNUM_1 | INTEGER | 2 | — | User-defined integer value 1 |
| 101 | BKYS_VNUM_2 | INTEGER | 2 | — | User-defined integer value 2 |
| 102 | BKYS_VNUM_3 | INTEGER | 2 | — | User-defined integer value 3 |
| 103 | BKYS_VNUM_4 | INTEGER | 2 | — | User-defined integer value 4 |
| 104 | BKYS_VNUM_5 | INTEGER | 2 | — | User-defined integer value 5 |
| 105 | BKYS_WONUM | NUMERIC | 8 | — | Last work order number |
| 106 | BKYS_YN_1 | STRING | 1 | — | System option flag 1 (Y/N) mapped to ISTS.CFG slot |
| 107 | BKYS_YN_10 | STRING | 1 | — | System option flag 10 (Y/N) mapped to ISTS.CFG slot |
| 108 | BKYS_YN_100 | STRING | 1 | — | System option flag 100 (Y/N) mapped to ISTS.CFG slot |
| 109 | BKYS_YN_101 | STRING | 1 | — | System option flag 101 (Y/N) mapped to ISTS.CFG slot |
| 110 | BKYS_YN_102 | STRING | 1 | — | System option flag 102 (Y/N) mapped to ISTS.CFG slot |
| 111 | BKYS_YN_103 | STRING | 1 | — | System option flag 103 (Y/N) mapped to ISTS.CFG slot |
| 112 | BKYS_YN_104 | STRING | 1 | — | System option flag 104 (Y/N) mapped to ISTS.CFG slot |
| 113 | BKYS_YN_105 | STRING | 1 | — | System option flag 105 (Y/N) mapped to ISTS.CFG slot |
| 114 | BKYS_YN_106 | STRING | 1 | — | System option flag 106 (Y/N) mapped to ISTS.CFG slot |
| 115 | BKYS_YN_107 | STRING | 1 | — | System option flag 107 (Y/N) mapped to ISTS.CFG slot |
| 116 | BKYS_YN_108 | STRING | 1 | — | System option flag 108 (Y/N) mapped to ISTS.CFG slot |
| 117 | BKYS_YN_109 | STRING | 1 | — | System option flag 109 (Y/N) mapped to ISTS.CFG slot |
| 118 | BKYS_YN_11 | STRING | 1 | — | System option flag 11 (Y/N) mapped to ISTS.CFG slot |
| 119 | BKYS_YN_110 | STRING | 1 | — | System option flag 110 (Y/N) mapped to ISTS.CFG slot |
| 120 | BKYS_YN_111 | STRING | 1 | — | System option flag 111 (Y/N) mapped to ISTS.CFG slot |
| 121 | BKYS_YN_112 | STRING | 1 | — | System option flag 112 (Y/N) mapped to ISTS.CFG slot |
| 122 | BKYS_YN_113 | STRING | 1 | — | System option flag 113 (Y/N) mapped to ISTS.CFG slot |
| 123 | BKYS_YN_114 | STRING | 1 | — | System option flag 114 (Y/N) mapped to ISTS.CFG slot |
| 124 | BKYS_YN_115 | STRING | 1 | — | System option flag 115 (Y/N) mapped to ISTS.CFG slot |
| 125 | BKYS_YN_116 | STRING | 1 | — | System option flag 116 (Y/N) mapped to ISTS.CFG slot |
| 126 | BKYS_YN_117 | STRING | 1 | — | System option flag 117 (Y/N) mapped to ISTS.CFG slot |
| 127 | BKYS_YN_118 | STRING | 1 | — | System option flag 118 (Y/N) mapped to ISTS.CFG slot |
| 128 | BKYS_YN_119 | STRING | 1 | — | System option flag 119 (Y/N) mapped to ISTS.CFG slot |
| 129 | BKYS_YN_12 | STRING | 1 | — | System option flag 12 (Y/N) mapped to ISTS.CFG slot |
| 130 | BKYS_YN_120 | STRING | 1 | — | System option flag 120 (Y/N) mapped to ISTS.CFG slot |
| 131 | BKYS_YN_121 | STRING | 1 | — | System option flag 121 (Y/N) mapped to ISTS.CFG slot |
| 132 | BKYS_YN_122 | STRING | 1 | — | System option flag 122 (Y/N) mapped to ISTS.CFG slot |
| 133 | BKYS_YN_123 | STRING | 1 | — | System option flag 123 (Y/N) mapped to ISTS.CFG slot |
| 134 | BKYS_YN_124 | STRING | 1 | — | System option flag 124 (Y/N) mapped to ISTS.CFG slot |
| 135 | BKYS_YN_125 | STRING | 1 | — | System option flag 125 (Y/N) mapped to ISTS.CFG slot |
| 136 | BKYS_YN_126 | STRING | 1 | — | System option flag 126 (Y/N) mapped to ISTS.CFG slot |
| 137 | BKYS_YN_127 | STRING | 1 | — | System option flag 127 (Y/N) mapped to ISTS.CFG slot |
| 138 | BKYS_YN_128 | STRING | 1 | — | System option flag 128 (Y/N) mapped to ISTS.CFG slot |
| 139 | BKYS_YN_129 | STRING | 1 | — | System option flag 129 (Y/N) mapped to ISTS.CFG slot |
| 140 | BKYS_YN_13 | STRING | 1 | — | System option flag 13 (Y/N) mapped to ISTS.CFG slot |
| 141 | BKYS_YN_130 | STRING | 1 | — | System option flag 130 (Y/N) mapped to ISTS.CFG slot |
| 142 | BKYS_YN_131 | STRING | 1 | — | System option flag 131 (Y/N) mapped to ISTS.CFG slot |
| 143 | BKYS_YN_132 | STRING | 1 | — | System option flag 132 (Y/N) mapped to ISTS.CFG slot |
| 144 | BKYS_YN_133 | STRING | 1 | — | System option flag 133 (Y/N) mapped to ISTS.CFG slot |
| 145 | BKYS_YN_134 | STRING | 1 | — | System option flag 134 (Y/N) mapped to ISTS.CFG slot |
| 146 | BKYS_YN_135 | STRING | 1 | — | System option flag 135 (Y/N) mapped to ISTS.CFG slot |
| 147 | BKYS_YN_136 | STRING | 1 | — | System option flag 136 (Y/N) mapped to ISTS.CFG slot |
| 148 | BKYS_YN_137 | STRING | 1 | — | System option flag 137 (Y/N) mapped to ISTS.CFG slot |
| 149 | BKYS_YN_138 | STRING | 1 | — | System option flag 138 (Y/N) mapped to ISTS.CFG slot |
| 150 | BKYS_YN_139 | STRING | 1 | — | System option flag 139 (Y/N) mapped to ISTS.CFG slot |
| 151 | BKYS_YN_14 | STRING | 1 | — | System option flag 14 (Y/N) mapped to ISTS.CFG slot |
| 152 | BKYS_YN_140 | STRING | 1 | — | System option flag 140 (Y/N) mapped to ISTS.CFG slot |
| 153 | BKYS_YN_141 | STRING | 1 | — | System option flag 141 (Y/N) mapped to ISTS.CFG slot |
| 154 | BKYS_YN_142 | STRING | 1 | — | System option flag 142 (Y/N) mapped to ISTS.CFG slot |
| 155 | BKYS_YN_143 | STRING | 1 | — | System option flag 143 (Y/N) mapped to ISTS.CFG slot |
| 156 | BKYS_YN_144 | STRING | 1 | — | System option flag 144 (Y/N) mapped to ISTS.CFG slot |
| 157 | BKYS_YN_145 | STRING | 1 | — | System option flag 145 (Y/N) mapped to ISTS.CFG slot |
| 158 | BKYS_YN_146 | STRING | 1 | — | System option flag 146 (Y/N) mapped to ISTS.CFG slot |
| 159 | BKYS_YN_147 | STRING | 1 | — | System option flag 147 (Y/N) mapped to ISTS.CFG slot |
| 160 | BKYS_YN_148 | STRING | 1 | — | System option flag 148 (Y/N) mapped to ISTS.CFG slot |
| 161 | BKYS_YN_149 | STRING | 1 | — | System option flag 149 (Y/N) mapped to ISTS.CFG slot |
| 162 | BKYS_YN_15 | STRING | 1 | — | System option flag 15 (Y/N) mapped to ISTS.CFG slot |
| 163 | BKYS_YN_150 | STRING | 1 | — | System option flag 150 (Y/N) mapped to ISTS.CFG slot |
| 164 | BKYS_YN_151 | STRING | 1 | — | System option flag 151 (Y/N) mapped to ISTS.CFG slot |
| 165 | BKYS_YN_152 | STRING | 1 | — | System option flag 152 (Y/N) mapped to ISTS.CFG slot |
| 166 | BKYS_YN_153 | STRING | 1 | — | System option flag 153 (Y/N) mapped to ISTS.CFG slot |
| 167 | BKYS_YN_154 | STRING | 1 | — | System option flag 154 (Y/N) mapped to ISTS.CFG slot |
| 168 | BKYS_YN_155 | STRING | 1 | — | System option flag 155 (Y/N) mapped to ISTS.CFG slot |
| 169 | BKYS_YN_156 | STRING | 1 | — | System option flag 156 (Y/N) mapped to ISTS.CFG slot |
| 170 | BKYS_YN_157 | STRING | 1 | — | System option flag 157 (Y/N) mapped to ISTS.CFG slot |
| 171 | BKYS_YN_158 | STRING | 1 | — | System option flag 158 (Y/N) mapped to ISTS.CFG slot |
| 172 | BKYS_YN_159 | STRING | 1 | — | System option flag 159 (Y/N) mapped to ISTS.CFG slot |
| 173 | BKYS_YN_16 | STRING | 1 | — | System option flag 16 (Y/N) mapped to ISTS.CFG slot |
| 174 | BKYS_YN_160 | STRING | 1 | — | System option flag 160 (Y/N) mapped to ISTS.CFG slot |
| 175 | BKYS_YN_161 | STRING | 1 | — | System option flag 161 (Y/N) mapped to ISTS.CFG slot |
| 176 | BKYS_YN_162 | STRING | 1 | — | System option flag 162 (Y/N) mapped to ISTS.CFG slot |
| 177 | BKYS_YN_163 | STRING | 1 | — | System option flag 163 (Y/N) mapped to ISTS.CFG slot |
| 178 | BKYS_YN_164 | STRING | 1 | — | System option flag 164 (Y/N) mapped to ISTS.CFG slot |
| 179 | BKYS_YN_165 | STRING | 1 | — | System option flag 165 (Y/N) mapped to ISTS.CFG slot |
| 180 | BKYS_YN_166 | STRING | 1 | — | System option flag 166 (Y/N) mapped to ISTS.CFG slot |
| 181 | BKYS_YN_167 | STRING | 1 | — | System option flag 167 (Y/N) mapped to ISTS.CFG slot |
| 182 | BKYS_YN_168 | STRING | 1 | — | System option flag 168 (Y/N) mapped to ISTS.CFG slot |
| 183 | BKYS_YN_169 | STRING | 1 | — | System option flag 169 (Y/N) mapped to ISTS.CFG slot |
| 184 | BKYS_YN_17 | STRING | 1 | — | System option flag 17 (Y/N) mapped to ISTS.CFG slot |
| 185 | BKYS_YN_170 | STRING | 1 | — | System option flag 170 (Y/N) mapped to ISTS.CFG slot |
| 186 | BKYS_YN_171 | STRING | 1 | — | System option flag 171 (Y/N) mapped to ISTS.CFG slot |
| 187 | BKYS_YN_172 | STRING | 1 | — | System option flag 172 (Y/N) mapped to ISTS.CFG slot |
| 188 | BKYS_YN_173 | STRING | 1 | — | System option flag 173 (Y/N) mapped to ISTS.CFG slot |
| 189 | BKYS_YN_174 | STRING | 1 | — | System option flag 174 (Y/N) mapped to ISTS.CFG slot |
| 190 | BKYS_YN_175 | STRING | 1 | — | System option flag 175 (Y/N) mapped to ISTS.CFG slot |
| 191 | BKYS_YN_176 | STRING | 1 | — | System option flag 176 (Y/N) mapped to ISTS.CFG slot |
| 192 | BKYS_YN_177 | STRING | 1 | — | System option flag 177 (Y/N) mapped to ISTS.CFG slot |
| 193 | BKYS_YN_178 | STRING | 1 | — | System option flag 178 (Y/N) mapped to ISTS.CFG slot |
| 194 | BKYS_YN_179 | STRING | 1 | — | System option flag 179 (Y/N) mapped to ISTS.CFG slot |
| 195 | BKYS_YN_18 | STRING | 1 | — | System option flag 18 (Y/N) mapped to ISTS.CFG slot |
| 196 | BKYS_YN_180 | STRING | 1 | — | System option flag 180 (Y/N) mapped to ISTS.CFG slot |
| 197 | BKYS_YN_181 | STRING | 1 | — | System option flag 181 (Y/N) mapped to ISTS.CFG slot |
| 198 | BKYS_YN_182 | STRING | 1 | — | System option flag 182 (Y/N) mapped to ISTS.CFG slot |
| 199 | BKYS_YN_183 | STRING | 1 | — | System option flag 183 (Y/N) mapped to ISTS.CFG slot |
| 200 | BKYS_YN_184 | STRING | 1 | — | System option flag 184 (Y/N) mapped to ISTS.CFG slot |
| 201 | BKYS_YN_185 | STRING | 1 | — | System option flag 185 (Y/N) mapped to ISTS.CFG slot |
| 202 | BKYS_YN_186 | STRING | 1 | — | System option flag 186 (Y/N) mapped to ISTS.CFG slot |
| 203 | BKYS_YN_187 | STRING | 1 | — | System option flag 187 (Y/N) mapped to ISTS.CFG slot |
| 204 | BKYS_YN_188 | STRING | 1 | — | System option flag 188 (Y/N) mapped to ISTS.CFG slot |
| 205 | BKYS_YN_189 | STRING | 1 | — | System option flag 189 (Y/N) mapped to ISTS.CFG slot |
| 206 | BKYS_YN_19 | STRING | 1 | — | System option flag 19 (Y/N) mapped to ISTS.CFG slot |
| 207 | BKYS_YN_190 | STRING | 1 | — | System option flag 190 (Y/N) mapped to ISTS.CFG slot |
| 208 | BKYS_YN_191 | STRING | 1 | — | System option flag 191 (Y/N) mapped to ISTS.CFG slot |
| 209 | BKYS_YN_192 | STRING | 1 | — | System option flag 192 (Y/N) mapped to ISTS.CFG slot |
| 210 | BKYS_YN_193 | STRING | 1 | — | System option flag 193 (Y/N) mapped to ISTS.CFG slot |
| 211 | BKYS_YN_194 | STRING | 1 | — | System option flag 194 (Y/N) mapped to ISTS.CFG slot |
| 212 | BKYS_YN_195 | STRING | 1 | — | System option flag 195 (Y/N) mapped to ISTS.CFG slot |
| 213 | BKYS_YN_196 | STRING | 1 | — | System option flag 196 (Y/N) mapped to ISTS.CFG slot |
| 214 | BKYS_YN_197 | STRING | 1 | — | System option flag 197 (Y/N) mapped to ISTS.CFG slot |
| 215 | BKYS_YN_198 | STRING | 1 | — | System option flag 198 (Y/N) mapped to ISTS.CFG slot |
| 216 | BKYS_YN_199 | STRING | 1 | — | System option flag 199 (Y/N) mapped to ISTS.CFG slot |
| 217 | BKYS_YN_2 | STRING | 1 | — | System option flag 2 (Y/N) mapped to ISTS.CFG slot |
| 218 | BKYS_YN_20 | STRING | 1 | — | System option flag 20 (Y/N) mapped to ISTS.CFG slot |
| 219 | BKYS_YN_200 | STRING | 1 | — | System option flag 200 (Y/N) mapped to ISTS.CFG slot |
| 220 | BKYS_YN_201 | STRING | 1 | — | System option flag 201 (Y/N) mapped to ISTS.CFG slot |
| 221 | BKYS_YN_202 | STRING | 1 | — | System option flag 202 (Y/N) mapped to ISTS.CFG slot |
| 222 | BKYS_YN_203 | STRING | 1 | — | System option flag 203 (Y/N) mapped to ISTS.CFG slot |
| 223 | BKYS_YN_204 | STRING | 1 | — | System option flag 204 (Y/N) mapped to ISTS.CFG slot |
| 224 | BKYS_YN_205 | STRING | 1 | — | System option flag 205 (Y/N) mapped to ISTS.CFG slot |
| 225 | BKYS_YN_206 | STRING | 1 | — | System option flag 206 (Y/N) mapped to ISTS.CFG slot |
| 226 | BKYS_YN_207 | STRING | 1 | — | System option flag 207 (Y/N) mapped to ISTS.CFG slot |
| 227 | BKYS_YN_208 | STRING | 1 | — | System option flag 208 (Y/N) mapped to ISTS.CFG slot |
| 228 | BKYS_YN_209 | STRING | 1 | — | System option flag 209 (Y/N) mapped to ISTS.CFG slot |
| 229 | BKYS_YN_21 | STRING | 1 | — | System option flag 21 (Y/N) mapped to ISTS.CFG slot |
| 230 | BKYS_YN_210 | STRING | 1 | — | System option flag 210 (Y/N) mapped to ISTS.CFG slot |
| 231 | BKYS_YN_211 | STRING | 1 | — | System option flag 211 (Y/N) mapped to ISTS.CFG slot |
| 232 | BKYS_YN_212 | STRING | 1 | — | System option flag 212 (Y/N) mapped to ISTS.CFG slot |
| 233 | BKYS_YN_213 | STRING | 1 | — | System option flag 213 (Y/N) mapped to ISTS.CFG slot |
| 234 | BKYS_YN_214 | STRING | 1 | — | System option flag 214 (Y/N) mapped to ISTS.CFG slot |
| 235 | BKYS_YN_215 | STRING | 1 | — | System option flag 215 (Y/N) mapped to ISTS.CFG slot |
| 236 | BKYS_YN_216 | STRING | 1 | — | System option flag 216 (Y/N) mapped to ISTS.CFG slot |
| 237 | BKYS_YN_217 | STRING | 1 | — | System option flag 217 (Y/N) mapped to ISTS.CFG slot |
| 238 | BKYS_YN_218 | STRING | 1 | — | System option flag 218 (Y/N) mapped to ISTS.CFG slot |
| 239 | BKYS_YN_219 | STRING | 1 | — | System option flag 219 (Y/N) mapped to ISTS.CFG slot |
| 240 | BKYS_YN_22 | STRING | 1 | — | System option flag 22 (Y/N) mapped to ISTS.CFG slot |
| 241 | BKYS_YN_220 | STRING | 1 | — | System option flag 220 (Y/N) mapped to ISTS.CFG slot |
| 242 | BKYS_YN_221 | STRING | 1 | — | System option flag 221 (Y/N) mapped to ISTS.CFG slot |
| 243 | BKYS_YN_222 | STRING | 1 | — | System option flag 222 (Y/N) mapped to ISTS.CFG slot |
| 244 | BKYS_YN_223 | STRING | 1 | — | System option flag 223 (Y/N) mapped to ISTS.CFG slot |
| 245 | BKYS_YN_224 | STRING | 1 | — | System option flag 224 (Y/N) mapped to ISTS.CFG slot |
| 246 | BKYS_YN_225 | STRING | 1 | — | System option flag 225 (Y/N) mapped to ISTS.CFG slot |
| 247 | BKYS_YN_226 | STRING | 1 | — | System option flag 226 (Y/N) mapped to ISTS.CFG slot |
| 248 | BKYS_YN_227 | STRING | 1 | — | System option flag 227 (Y/N) mapped to ISTS.CFG slot |
| 249 | BKYS_YN_228 | STRING | 1 | — | System option flag 228 (Y/N) mapped to ISTS.CFG slot |
| 250 | BKYS_YN_229 | STRING | 1 | — | System option flag 229 (Y/N) mapped to ISTS.CFG slot |
| 251 | BKYS_YN_23 | STRING | 1 | — | System option flag 23 (Y/N) mapped to ISTS.CFG slot |
| 252 | BKYS_YN_230 | STRING | 1 | — | System option flag 230 (Y/N) mapped to ISTS.CFG slot |
| 253 | BKYS_YN_231 | STRING | 1 | — | System option flag 231 (Y/N) mapped to ISTS.CFG slot |
| 254 | BKYS_YN_232 | STRING | 1 | — | System option flag 232 (Y/N) mapped to ISTS.CFG slot |
| 255 | BKYS_YN_233 | STRING | 1 | — | System option flag 233 (Y/N) mapped to ISTS.CFG slot |
| 256 | BKYS_YN_234 | STRING | 1 | — | System option flag 234 (Y/N) mapped to ISTS.CFG slot |
| 257 | BKYS_YN_235 | STRING | 1 | — | System option flag 235 (Y/N) mapped to ISTS.CFG slot |
| 258 | BKYS_YN_236 | STRING | 1 | — | System option flag 236 (Y/N) mapped to ISTS.CFG slot |
| 259 | BKYS_YN_237 | STRING | 1 | — | System option flag 237 (Y/N) mapped to ISTS.CFG slot |
| 260 | BKYS_YN_238 | STRING | 1 | — | System option flag 238 (Y/N) mapped to ISTS.CFG slot |
| 261 | BKYS_YN_239 | STRING | 1 | — | System option flag 239 (Y/N) mapped to ISTS.CFG slot |
| 262 | BKYS_YN_24 | STRING | 1 | — | System option flag 24 (Y/N) mapped to ISTS.CFG slot |
| 263 | BKYS_YN_240 | STRING | 1 | — | System option flag 240 (Y/N) mapped to ISTS.CFG slot |
| 264 | BKYS_YN_241 | STRING | 1 | — | System option flag 241 (Y/N) mapped to ISTS.CFG slot |
| 265 | BKYS_YN_242 | STRING | 1 | — | System option flag 242 (Y/N) mapped to ISTS.CFG slot |
| 266 | BKYS_YN_243 | STRING | 1 | — | System option flag 243 (Y/N) mapped to ISTS.CFG slot |
| 267 | BKYS_YN_244 | STRING | 1 | — | System option flag 244 (Y/N) mapped to ISTS.CFG slot |
| 268 | BKYS_YN_245 | STRING | 1 | — | System option flag 245 (Y/N) mapped to ISTS.CFG slot |
| 269 | BKYS_YN_246 | STRING | 1 | — | System option flag 246 (Y/N) mapped to ISTS.CFG slot |
| 270 | BKYS_YN_247 | STRING | 1 | — | System option flag 247 (Y/N) mapped to ISTS.CFG slot |
| 271 | BKYS_YN_248 | STRING | 1 | — | System option flag 248 (Y/N) mapped to ISTS.CFG slot |
| 272 | BKYS_YN_249 | STRING | 1 | — | System option flag 249 (Y/N) mapped to ISTS.CFG slot |
| 273 | BKYS_YN_25 | STRING | 1 | — | System option flag 25 (Y/N) mapped to ISTS.CFG slot |
| 274 | BKYS_YN_250 | STRING | 1 | — | System option flag 250 (Y/N) mapped to ISTS.CFG slot |
| 275 | BKYS_YN_26 | STRING | 1 | — | System option flag 26 (Y/N) mapped to ISTS.CFG slot |
| 276 | BKYS_YN_27 | STRING | 1 | — | System option flag 27 (Y/N) mapped to ISTS.CFG slot |
| 277 | BKYS_YN_28 | STRING | 1 | — | System option flag 28 (Y/N) mapped to ISTS.CFG slot |
| 278 | BKYS_YN_29 | STRING | 1 | — | System option flag 29 (Y/N) mapped to ISTS.CFG slot |
| 279 | BKYS_YN_3 | STRING | 1 | — | System option flag 3 (Y/N) mapped to ISTS.CFG slot |
| 280 | BKYS_YN_30 | STRING | 1 | — | System option flag 30 (Y/N) mapped to ISTS.CFG slot |
| 281 | BKYS_YN_31 | STRING | 1 | — | System option flag 31 (Y/N) mapped to ISTS.CFG slot |
| 282 | BKYS_YN_32 | STRING | 1 | — | System option flag 32 (Y/N) mapped to ISTS.CFG slot |
| 283 | BKYS_YN_33 | STRING | 1 | — | System option flag 33 (Y/N) mapped to ISTS.CFG slot |
| 284 | BKYS_YN_34 | STRING | 1 | — | System option flag 34 (Y/N) mapped to ISTS.CFG slot |
| 285 | BKYS_YN_35 | STRING | 1 | — | System option flag 35 (Y/N) mapped to ISTS.CFG slot |
| 286 | BKYS_YN_36 | STRING | 1 | — | System option flag 36 (Y/N) mapped to ISTS.CFG slot |
| 287 | BKYS_YN_37 | STRING | 1 | — | System option flag 37 (Y/N) mapped to ISTS.CFG slot |
| 288 | BKYS_YN_38 | STRING | 1 | — | System option flag 38 (Y/N) mapped to ISTS.CFG slot |
| 289 | BKYS_YN_39 | STRING | 1 | — | System option flag 39 (Y/N) mapped to ISTS.CFG slot |
| 290 | BKYS_YN_4 | STRING | 1 | — | System option flag 4 (Y/N) mapped to ISTS.CFG slot |
| 291 | BKYS_YN_40 | STRING | 1 | — | System option flag 40 (Y/N) mapped to ISTS.CFG slot |
| 292 | BKYS_YN_41 | STRING | 1 | — | System option flag 41 (Y/N) mapped to ISTS.CFG slot |
| 293 | BKYS_YN_42 | STRING | 1 | — | System option flag 42 (Y/N) mapped to ISTS.CFG slot |
| 294 | BKYS_YN_43 | STRING | 1 | — | System option flag 43 (Y/N) mapped to ISTS.CFG slot |
| 295 | BKYS_YN_44 | STRING | 1 | — | System option flag 44 (Y/N) mapped to ISTS.CFG slot |
| 296 | BKYS_YN_45 | STRING | 1 | — | System option flag 45 (Y/N) mapped to ISTS.CFG slot |
| 297 | BKYS_YN_46 | STRING | 1 | — | System option flag 46 (Y/N) mapped to ISTS.CFG slot |
| 298 | BKYS_YN_47 | STRING | 1 | — | System option flag 47 (Y/N) mapped to ISTS.CFG slot |
| 299 | BKYS_YN_48 | STRING | 1 | — | System option flag 48 (Y/N) mapped to ISTS.CFG slot |
| 300 | BKYS_YN_49 | STRING | 1 | — | System option flag 49 (Y/N) mapped to ISTS.CFG slot |
| 301 | BKYS_YN_5 | STRING | 1 | — | System option flag 5 (Y/N) mapped to ISTS.CFG slot |
| 302 | BKYS_YN_50 | STRING | 1 | — | System option flag 50 (Y/N) mapped to ISTS.CFG slot |
| 303 | BKYS_YN_51 | STRING | 1 | — | System option flag 51 (Y/N) mapped to ISTS.CFG slot |
| 304 | BKYS_YN_52 | STRING | 1 | — | System option flag 52 (Y/N) mapped to ISTS.CFG slot |
| 305 | BKYS_YN_53 | STRING | 1 | — | System option flag 53 (Y/N) mapped to ISTS.CFG slot |
| 306 | BKYS_YN_54 | STRING | 1 | — | System option flag 54 (Y/N) mapped to ISTS.CFG slot |
| 307 | BKYS_YN_55 | STRING | 1 | — | System option flag 55 (Y/N) mapped to ISTS.CFG slot |
| 308 | BKYS_YN_56 | STRING | 1 | — | System option flag 56 (Y/N) mapped to ISTS.CFG slot |
| 309 | BKYS_YN_57 | STRING | 1 | — | System option flag 57 (Y/N) mapped to ISTS.CFG slot |
| 310 | BKYS_YN_58 | STRING | 1 | — | System option flag 58 (Y/N) mapped to ISTS.CFG slot |
| 311 | BKYS_YN_59 | STRING | 1 | — | System option flag 59 (Y/N) mapped to ISTS.CFG slot |
| 312 | BKYS_YN_6 | STRING | 1 | — | System option flag 6 (Y/N) mapped to ISTS.CFG slot |
| 313 | BKYS_YN_60 | STRING | 1 | — | System option flag 60 (Y/N) mapped to ISTS.CFG slot |
| 314 | BKYS_YN_61 | STRING | 1 | — | System option flag 61 (Y/N) mapped to ISTS.CFG slot |
| 315 | BKYS_YN_62 | STRING | 1 | — | System option flag 62 (Y/N) mapped to ISTS.CFG slot |
| 316 | BKYS_YN_63 | STRING | 1 | — | System option flag 63 (Y/N) mapped to ISTS.CFG slot |
| 317 | BKYS_YN_64 | STRING | 1 | — | System option flag 64 (Y/N) mapped to ISTS.CFG slot |
| 318 | BKYS_YN_65 | STRING | 1 | — | System option flag 65 (Y/N) mapped to ISTS.CFG slot |
| 319 | BKYS_YN_66 | STRING | 1 | — | System option flag 66 (Y/N) mapped to ISTS.CFG slot |
| 320 | BKYS_YN_67 | STRING | 1 | — | System option flag 67 (Y/N) mapped to ISTS.CFG slot |
| 321 | BKYS_YN_68 | STRING | 1 | — | System option flag 68 (Y/N) mapped to ISTS.CFG slot |
| 322 | BKYS_YN_69 | STRING | 1 | — | System option flag 69 (Y/N) mapped to ISTS.CFG slot |
| 323 | BKYS_YN_7 | STRING | 1 | — | System option flag 7 (Y/N) mapped to ISTS.CFG slot |
| 324 | BKYS_YN_70 | STRING | 1 | — | System option flag 70 (Y/N) mapped to ISTS.CFG slot |
| 325 | BKYS_YN_71 | STRING | 1 | — | System option flag 71 (Y/N) mapped to ISTS.CFG slot |
| 326 | BKYS_YN_72 | STRING | 1 | — | System option flag 72 (Y/N) mapped to ISTS.CFG slot |
| 327 | BKYS_YN_73 | STRING | 1 | — | System option flag 73 (Y/N) mapped to ISTS.CFG slot |
| 328 | BKYS_YN_74 | STRING | 1 | — | System option flag 74 (Y/N) mapped to ISTS.CFG slot |
| 329 | BKYS_YN_75 | STRING | 1 | — | System option flag 75 (Y/N) mapped to ISTS.CFG slot |
| 330 | BKYS_YN_76 | STRING | 1 | — | System option flag 76 (Y/N) mapped to ISTS.CFG slot |
| 331 | BKYS_YN_77 | STRING | 1 | — | System option flag 77 (Y/N) mapped to ISTS.CFG slot |
| 332 | BKYS_YN_78 | STRING | 1 | — | System option flag 78 (Y/N) mapped to ISTS.CFG slot |
| 333 | BKYS_YN_79 | STRING | 1 | — | System option flag 79 (Y/N) mapped to ISTS.CFG slot |
| 334 | BKYS_YN_8 | STRING | 1 | — | System option flag 8 (Y/N) mapped to ISTS.CFG slot |
| 335 | BKYS_YN_80 | STRING | 1 | — | System option flag 80 (Y/N) mapped to ISTS.CFG slot |
| 336 | BKYS_YN_81 | STRING | 1 | — | System option flag 81 (Y/N) mapped to ISTS.CFG slot |
| 337 | BKYS_YN_82 | STRING | 1 | — | System option flag 82 (Y/N) mapped to ISTS.CFG slot |
| 338 | BKYS_YN_83 | STRING | 1 | — | System option flag 83 (Y/N) mapped to ISTS.CFG slot |
| 339 | BKYS_YN_84 | STRING | 1 | — | System option flag 84 (Y/N) mapped to ISTS.CFG slot |
| 340 | BKYS_YN_85 | STRING | 1 | — | System option flag 85 (Y/N) mapped to ISTS.CFG slot |
| 341 | BKYS_YN_86 | STRING | 1 | — | System option flag 86 (Y/N) mapped to ISTS.CFG slot |
| 342 | BKYS_YN_87 | STRING | 1 | — | System option flag 87 (Y/N) mapped to ISTS.CFG slot |
| 343 | BKYS_YN_88 | STRING | 1 | — | System option flag 88 (Y/N) mapped to ISTS.CFG slot |
| 344 | BKYS_YN_89 | STRING | 1 | — | System option flag 89 (Y/N) mapped to ISTS.CFG slot |
| 345 | BKYS_YN_9 | STRING | 1 | — | System option flag 9 (Y/N) mapped to ISTS.CFG slot |
| 346 | BKYS_YN_90 | STRING | 1 | — | System option flag 90 (Y/N) mapped to ISTS.CFG slot |
| 347 | BKYS_YN_91 | STRING | 1 | — | System option flag 91 (Y/N) mapped to ISTS.CFG slot |
| 348 | BKYS_YN_92 | STRING | 1 | — | System option flag 92 (Y/N) mapped to ISTS.CFG slot |
| 349 | BKYS_YN_93 | STRING | 1 | — | System option flag 93 (Y/N) mapped to ISTS.CFG slot |
| 350 | BKYS_YN_94 | STRING | 1 | — | System option flag 94 (Y/N) mapped to ISTS.CFG slot |
| 351 | BKYS_YN_95 | STRING | 1 | — | System option flag 95 (Y/N) mapped to ISTS.CFG slot |
| 352 | BKYS_YN_96 | STRING | 1 | — | System option flag 96 (Y/N) mapped to ISTS.CFG slot |
| 353 | BKYS_YN_97 | STRING | 1 | — | System option flag 97 (Y/N) mapped to ISTS.CFG slot |
| 354 | BKYS_YN_98 | STRING | 1 | — | System option flag 98 (Y/N) mapped to ISTS.CFG slot |
| 355 | BKYS_YN_99 | STRING | 1 | — | System option flag 99 (Y/N) mapped to ISTS.CFG slot |

## CALTEMP
**TEMP FILE FOR GENERATING SHOP CALENDAR**

Fields: 2

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | SHP_DATE | NUMERIC | 8 | — | Ship date stored as numeric YYYYMMDD |
| 2 | SLSH_DATE | DATE | 4 | — | Slash/delimiter date temp value |

## DBAHLPID
**PROGRAM SPECIFIC HELP REFERENCE**

Fields: 2

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | DBA_HELP_MAP | INTEGER | 2 | — | Help topic ID mapping number |
| 2 | DBA_HELP_REF | STRING | 8 | — | Help file reference key |

## ISALINKS
**ARCHIVED LINKS**

Fields: 312

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_LNK_ALPHA | STRING | 6000 | — | Full text/blob content for this link |
| 2 | IS_LNK_APP | STRING | 10 | — | Application module this link belongs to |
| 3 | IS_LNK_ATYPE | STRING | 3 | — | Archive type code |
| 4 | IS_LNK_DATE | DATE | 4 | — | Date link was created |
| 5 | IS_LNK_DEF_1 | STRING | 1 | — | Default flag 1 for this link definition |
| 6 | IS_LNK_DEF_10 | STRING | 1 | — | Default flag 10 for this link definition |
| 7 | IS_LNK_DEF_100 | STRING | 1 | — | Default flag 100 for this link definition |
| 8 | IS_LNK_DEF_11 | STRING | 1 | — | Default flag 11 for this link definition |
| 9 | IS_LNK_DEF_12 | STRING | 1 | — | Default flag 12 for this link definition |
| 10 | IS_LNK_DEF_13 | STRING | 1 | — | Default flag 13 for this link definition |
| 11 | IS_LNK_DEF_14 | STRING | 1 | — | Default flag 14 for this link definition |
| 12 | IS_LNK_DEF_15 | STRING | 1 | — | Default flag 15 for this link definition |
| 13 | IS_LNK_DEF_16 | STRING | 1 | — | Default flag 16 for this link definition |
| 14 | IS_LNK_DEF_17 | STRING | 1 | — | Default flag 17 for this link definition |
| 15 | IS_LNK_DEF_18 | STRING | 1 | — | Default flag 18 for this link definition |
| 16 | IS_LNK_DEF_19 | STRING | 1 | — | Default flag 19 for this link definition |
| 17 | IS_LNK_DEF_2 | STRING | 1 | — | Default flag 2 for this link definition |
| 18 | IS_LNK_DEF_20 | STRING | 1 | — | Default flag 20 for this link definition |
| 19 | IS_LNK_DEF_21 | STRING | 1 | — | Default flag 21 for this link definition |
| 20 | IS_LNK_DEF_22 | STRING | 1 | — | Default flag 22 for this link definition |
| 21 | IS_LNK_DEF_23 | STRING | 1 | — | Default flag 23 for this link definition |
| 22 | IS_LNK_DEF_24 | STRING | 1 | — | Default flag 24 for this link definition |
| 23 | IS_LNK_DEF_25 | STRING | 1 | — | Default flag 25 for this link definition |
| 24 | IS_LNK_DEF_26 | STRING | 1 | — | Default flag 26 for this link definition |
| 25 | IS_LNK_DEF_27 | STRING | 1 | — | Default flag 27 for this link definition |
| 26 | IS_LNK_DEF_28 | STRING | 1 | — | Default flag 28 for this link definition |
| 27 | IS_LNK_DEF_29 | STRING | 1 | — | Default flag 29 for this link definition |
| 28 | IS_LNK_DEF_3 | STRING | 1 | — | Default flag 3 for this link definition |
| 29 | IS_LNK_DEF_30 | STRING | 1 | — | Default flag 30 for this link definition |
| 30 | IS_LNK_DEF_31 | STRING | 1 | — | Default flag 31 for this link definition |
| 31 | IS_LNK_DEF_32 | STRING | 1 | — | Default flag 32 for this link definition |
| 32 | IS_LNK_DEF_33 | STRING | 1 | — | Default flag 33 for this link definition |
| 33 | IS_LNK_DEF_34 | STRING | 1 | — | Default flag 34 for this link definition |
| 34 | IS_LNK_DEF_35 | STRING | 1 | — | Default flag 35 for this link definition |
| 35 | IS_LNK_DEF_36 | STRING | 1 | — | Default flag 36 for this link definition |
| 36 | IS_LNK_DEF_37 | STRING | 1 | — | Default flag 37 for this link definition |
| 37 | IS_LNK_DEF_38 | STRING | 1 | — | Default flag 38 for this link definition |
| 38 | IS_LNK_DEF_39 | STRING | 1 | — | Default flag 39 for this link definition |
| 39 | IS_LNK_DEF_4 | STRING | 1 | — | Default flag 4 for this link definition |
| 40 | IS_LNK_DEF_40 | STRING | 1 | — | Default flag 40 for this link definition |
| 41 | IS_LNK_DEF_41 | STRING | 1 | — | Default flag 41 for this link definition |
| 42 | IS_LNK_DEF_42 | STRING | 1 | — | Default flag 42 for this link definition |
| 43 | IS_LNK_DEF_43 | STRING | 1 | — | Default flag 43 for this link definition |
| 44 | IS_LNK_DEF_44 | STRING | 1 | — | Default flag 44 for this link definition |
| 45 | IS_LNK_DEF_45 | STRING | 1 | — | Default flag 45 for this link definition |
| 46 | IS_LNK_DEF_46 | STRING | 1 | — | Default flag 46 for this link definition |
| 47 | IS_LNK_DEF_47 | STRING | 1 | — | Default flag 47 for this link definition |
| 48 | IS_LNK_DEF_48 | STRING | 1 | — | Default flag 48 for this link definition |
| 49 | IS_LNK_DEF_49 | STRING | 1 | — | Default flag 49 for this link definition |
| 50 | IS_LNK_DEF_5 | STRING | 1 | — | Default flag 5 for this link definition |
| 51 | IS_LNK_DEF_50 | STRING | 1 | — | Default flag 50 for this link definition |
| 52 | IS_LNK_DEF_51 | STRING | 1 | — | Default flag 51 for this link definition |
| 53 | IS_LNK_DEF_52 | STRING | 1 | — | Default flag 52 for this link definition |
| 54 | IS_LNK_DEF_53 | STRING | 1 | — | Default flag 53 for this link definition |
| 55 | IS_LNK_DEF_54 | STRING | 1 | — | Default flag 54 for this link definition |
| 56 | IS_LNK_DEF_55 | STRING | 1 | — | Default flag 55 for this link definition |
| 57 | IS_LNK_DEF_56 | STRING | 1 | — | Default flag 56 for this link definition |
| 58 | IS_LNK_DEF_57 | STRING | 1 | — | Default flag 57 for this link definition |
| 59 | IS_LNK_DEF_58 | STRING | 1 | — | Default flag 58 for this link definition |
| 60 | IS_LNK_DEF_59 | STRING | 1 | — | Default flag 59 for this link definition |
| 61 | IS_LNK_DEF_6 | STRING | 1 | — | Default flag 6 for this link definition |
| 62 | IS_LNK_DEF_60 | STRING | 1 | — | Default flag 60 for this link definition |
| 63 | IS_LNK_DEF_61 | STRING | 1 | — | Default flag 61 for this link definition |
| 64 | IS_LNK_DEF_62 | STRING | 1 | — | Default flag 62 for this link definition |
| 65 | IS_LNK_DEF_63 | STRING | 1 | — | Default flag 63 for this link definition |
| 66 | IS_LNK_DEF_64 | STRING | 1 | — | Default flag 64 for this link definition |
| 67 | IS_LNK_DEF_65 | STRING | 1 | — | Default flag 65 for this link definition |
| 68 | IS_LNK_DEF_66 | STRING | 1 | — | Default flag 66 for this link definition |
| 69 | IS_LNK_DEF_67 | STRING | 1 | — | Default flag 67 for this link definition |
| 70 | IS_LNK_DEF_68 | STRING | 1 | — | Default flag 68 for this link definition |
| 71 | IS_LNK_DEF_69 | STRING | 1 | — | Default flag 69 for this link definition |
| 72 | IS_LNK_DEF_7 | STRING | 1 | — | Default flag 7 for this link definition |
| 73 | IS_LNK_DEF_70 | STRING | 1 | — | Default flag 70 for this link definition |
| 74 | IS_LNK_DEF_71 | STRING | 1 | — | Default flag 71 for this link definition |
| 75 | IS_LNK_DEF_72 | STRING | 1 | — | Default flag 72 for this link definition |
| 76 | IS_LNK_DEF_73 | STRING | 1 | — | Default flag 73 for this link definition |
| 77 | IS_LNK_DEF_74 | STRING | 1 | — | Default flag 74 for this link definition |
| 78 | IS_LNK_DEF_75 | STRING | 1 | — | Default flag 75 for this link definition |
| 79 | IS_LNK_DEF_76 | STRING | 1 | — | Default flag 76 for this link definition |
| 80 | IS_LNK_DEF_77 | STRING | 1 | — | Default flag 77 for this link definition |
| 81 | IS_LNK_DEF_78 | STRING | 1 | — | Default flag 78 for this link definition |
| 82 | IS_LNK_DEF_79 | STRING | 1 | — | Default flag 79 for this link definition |
| 83 | IS_LNK_DEF_8 | STRING | 1 | — | Default flag 8 for this link definition |
| 84 | IS_LNK_DEF_80 | STRING | 1 | — | Default flag 80 for this link definition |
| 85 | IS_LNK_DEF_81 | STRING | 1 | — | Default flag 81 for this link definition |
| 86 | IS_LNK_DEF_82 | STRING | 1 | — | Default flag 82 for this link definition |
| 87 | IS_LNK_DEF_83 | STRING | 1 | — | Default flag 83 for this link definition |
| 88 | IS_LNK_DEF_84 | STRING | 1 | — | Default flag 84 for this link definition |
| 89 | IS_LNK_DEF_85 | STRING | 1 | — | Default flag 85 for this link definition |
| 90 | IS_LNK_DEF_86 | STRING | 1 | — | Default flag 86 for this link definition |
| 91 | IS_LNK_DEF_87 | STRING | 1 | — | Default flag 87 for this link definition |
| 92 | IS_LNK_DEF_88 | STRING | 1 | — | Default flag 88 for this link definition |
| 93 | IS_LNK_DEF_89 | STRING | 1 | — | Default flag 89 for this link definition |
| 94 | IS_LNK_DEF_9 | STRING | 1 | — | Default flag 9 for this link definition |
| 95 | IS_LNK_DEF_90 | STRING | 1 | — | Default flag 90 for this link definition |
| 96 | IS_LNK_DEF_91 | STRING | 1 | — | Default flag 91 for this link definition |
| 97 | IS_LNK_DEF_92 | STRING | 1 | — | Default flag 92 for this link definition |
| 98 | IS_LNK_DEF_93 | STRING | 1 | — | Default flag 93 for this link definition |
| 99 | IS_LNK_DEF_94 | STRING | 1 | — | Default flag 94 for this link definition |
| 100 | IS_LNK_DEF_95 | STRING | 1 | — | Default flag 95 for this link definition |
| 101 | IS_LNK_DEF_96 | STRING | 1 | — | Default flag 96 for this link definition |
| 102 | IS_LNK_DEF_97 | STRING | 1 | — | Default flag 97 for this link definition |
| 103 | IS_LNK_DEF_98 | STRING | 1 | — | Default flag 98 for this link definition |
| 104 | IS_LNK_DEF_99 | STRING | 1 | — | Default flag 99 for this link definition |
| 105 | IS_LNK_EXTRA | STRING | 100 | — | Reserved extra field |
| 106 | IS_LNK_GLOBAL | STRING | 1 | — | Global (company-wide) link flag (Y/N) |
| 107 | IS_LNK_LINK | STRING | 256 | — | File path or URL for this link |
| 108 | IS_LNK_NOTE | STRING | 0 | — | Memo/blob note field |
| 109 | IS_LNK_OPENWITH | STRING | 1 | — | Open-with application preference flag |
| 110 | IS_LNK_PCB_1 | STRING | 1 | — | PCB permission flag 1 for this link |
| 111 | IS_LNK_PCB_10 | STRING | 1 | — | PCB permission flag 10 for this link |
| 112 | IS_LNK_PCB_100 | STRING | 1 | — | PCB permission flag 100 for this link |
| 113 | IS_LNK_PCB_11 | STRING | 1 | — | PCB permission flag 11 for this link |
| 114 | IS_LNK_PCB_12 | STRING | 1 | — | PCB permission flag 12 for this link |
| 115 | IS_LNK_PCB_13 | STRING | 1 | — | PCB permission flag 13 for this link |
| 116 | IS_LNK_PCB_14 | STRING | 1 | — | PCB permission flag 14 for this link |
| 117 | IS_LNK_PCB_15 | STRING | 1 | — | PCB permission flag 15 for this link |
| 118 | IS_LNK_PCB_16 | STRING | 1 | — | PCB permission flag 16 for this link |
| 119 | IS_LNK_PCB_17 | STRING | 1 | — | PCB permission flag 17 for this link |
| 120 | IS_LNK_PCB_18 | STRING | 1 | — | PCB permission flag 18 for this link |
| 121 | IS_LNK_PCB_19 | STRING | 1 | — | PCB permission flag 19 for this link |
| 122 | IS_LNK_PCB_2 | STRING | 1 | — | PCB permission flag 2 for this link |
| 123 | IS_LNK_PCB_20 | STRING | 1 | — | PCB permission flag 20 for this link |
| 124 | IS_LNK_PCB_21 | STRING | 1 | — | PCB permission flag 21 for this link |
| 125 | IS_LNK_PCB_22 | STRING | 1 | — | PCB permission flag 22 for this link |
| 126 | IS_LNK_PCB_23 | STRING | 1 | — | PCB permission flag 23 for this link |
| 127 | IS_LNK_PCB_24 | STRING | 1 | — | PCB permission flag 24 for this link |
| 128 | IS_LNK_PCB_25 | STRING | 1 | — | PCB permission flag 25 for this link |
| 129 | IS_LNK_PCB_26 | STRING | 1 | — | PCB permission flag 26 for this link |
| 130 | IS_LNK_PCB_27 | STRING | 1 | — | PCB permission flag 27 for this link |
| 131 | IS_LNK_PCB_28 | STRING | 1 | — | PCB permission flag 28 for this link |
| 132 | IS_LNK_PCB_29 | STRING | 1 | — | PCB permission flag 29 for this link |
| 133 | IS_LNK_PCB_3 | STRING | 1 | — | PCB permission flag 3 for this link |
| 134 | IS_LNK_PCB_30 | STRING | 1 | — | PCB permission flag 30 for this link |
| 135 | IS_LNK_PCB_31 | STRING | 1 | — | PCB permission flag 31 for this link |
| 136 | IS_LNK_PCB_32 | STRING | 1 | — | PCB permission flag 32 for this link |
| 137 | IS_LNK_PCB_33 | STRING | 1 | — | PCB permission flag 33 for this link |
| 138 | IS_LNK_PCB_34 | STRING | 1 | — | PCB permission flag 34 for this link |
| 139 | IS_LNK_PCB_35 | STRING | 1 | — | PCB permission flag 35 for this link |
| 140 | IS_LNK_PCB_36 | STRING | 1 | — | PCB permission flag 36 for this link |
| 141 | IS_LNK_PCB_37 | STRING | 1 | — | PCB permission flag 37 for this link |
| 142 | IS_LNK_PCB_38 | STRING | 1 | — | PCB permission flag 38 for this link |
| 143 | IS_LNK_PCB_39 | STRING | 1 | — | PCB permission flag 39 for this link |
| 144 | IS_LNK_PCB_4 | STRING | 1 | — | PCB permission flag 4 for this link |
| 145 | IS_LNK_PCB_40 | STRING | 1 | — | PCB permission flag 40 for this link |
| 146 | IS_LNK_PCB_41 | STRING | 1 | — | PCB permission flag 41 for this link |
| 147 | IS_LNK_PCB_42 | STRING | 1 | — | PCB permission flag 42 for this link |
| 148 | IS_LNK_PCB_43 | STRING | 1 | — | PCB permission flag 43 for this link |
| 149 | IS_LNK_PCB_44 | STRING | 1 | — | PCB permission flag 44 for this link |
| 150 | IS_LNK_PCB_45 | STRING | 1 | — | PCB permission flag 45 for this link |
| 151 | IS_LNK_PCB_46 | STRING | 1 | — | PCB permission flag 46 for this link |
| 152 | IS_LNK_PCB_47 | STRING | 1 | — | PCB permission flag 47 for this link |
| 153 | IS_LNK_PCB_48 | STRING | 1 | — | PCB permission flag 48 for this link |
| 154 | IS_LNK_PCB_49 | STRING | 1 | — | PCB permission flag 49 for this link |
| 155 | IS_LNK_PCB_5 | STRING | 1 | — | PCB permission flag 5 for this link |
| 156 | IS_LNK_PCB_50 | STRING | 1 | — | PCB permission flag 50 for this link |
| 157 | IS_LNK_PCB_51 | STRING | 1 | — | PCB permission flag 51 for this link |
| 158 | IS_LNK_PCB_52 | STRING | 1 | — | PCB permission flag 52 for this link |
| 159 | IS_LNK_PCB_53 | STRING | 1 | — | PCB permission flag 53 for this link |
| 160 | IS_LNK_PCB_54 | STRING | 1 | — | PCB permission flag 54 for this link |
| 161 | IS_LNK_PCB_55 | STRING | 1 | — | PCB permission flag 55 for this link |
| 162 | IS_LNK_PCB_56 | STRING | 1 | — | PCB permission flag 56 for this link |
| 163 | IS_LNK_PCB_57 | STRING | 1 | — | PCB permission flag 57 for this link |
| 164 | IS_LNK_PCB_58 | STRING | 1 | — | PCB permission flag 58 for this link |
| 165 | IS_LNK_PCB_59 | STRING | 1 | — | PCB permission flag 59 for this link |
| 166 | IS_LNK_PCB_6 | STRING | 1 | — | PCB permission flag 6 for this link |
| 167 | IS_LNK_PCB_60 | STRING | 1 | — | PCB permission flag 60 for this link |
| 168 | IS_LNK_PCB_61 | STRING | 1 | — | PCB permission flag 61 for this link |
| 169 | IS_LNK_PCB_62 | STRING | 1 | — | PCB permission flag 62 for this link |
| 170 | IS_LNK_PCB_63 | STRING | 1 | — | PCB permission flag 63 for this link |
| 171 | IS_LNK_PCB_64 | STRING | 1 | — | PCB permission flag 64 for this link |
| 172 | IS_LNK_PCB_65 | STRING | 1 | — | PCB permission flag 65 for this link |
| 173 | IS_LNK_PCB_66 | STRING | 1 | — | PCB permission flag 66 for this link |
| 174 | IS_LNK_PCB_67 | STRING | 1 | — | PCB permission flag 67 for this link |
| 175 | IS_LNK_PCB_68 | STRING | 1 | — | PCB permission flag 68 for this link |
| 176 | IS_LNK_PCB_69 | STRING | 1 | — | PCB permission flag 69 for this link |
| 177 | IS_LNK_PCB_7 | STRING | 1 | — | PCB permission flag 7 for this link |
| 178 | IS_LNK_PCB_70 | STRING | 1 | — | PCB permission flag 70 for this link |
| 179 | IS_LNK_PCB_71 | STRING | 1 | — | PCB permission flag 71 for this link |
| 180 | IS_LNK_PCB_72 | STRING | 1 | — | PCB permission flag 72 for this link |
| 181 | IS_LNK_PCB_73 | STRING | 1 | — | PCB permission flag 73 for this link |
| 182 | IS_LNK_PCB_74 | STRING | 1 | — | PCB permission flag 74 for this link |
| 183 | IS_LNK_PCB_75 | STRING | 1 | — | PCB permission flag 75 for this link |
| 184 | IS_LNK_PCB_76 | STRING | 1 | — | PCB permission flag 76 for this link |
| 185 | IS_LNK_PCB_77 | STRING | 1 | — | PCB permission flag 77 for this link |
| 186 | IS_LNK_PCB_78 | STRING | 1 | — | PCB permission flag 78 for this link |
| 187 | IS_LNK_PCB_79 | STRING | 1 | — | PCB permission flag 79 for this link |
| 188 | IS_LNK_PCB_8 | STRING | 1 | — | PCB permission flag 8 for this link |
| 189 | IS_LNK_PCB_80 | STRING | 1 | — | PCB permission flag 80 for this link |
| 190 | IS_LNK_PCB_81 | STRING | 1 | — | PCB permission flag 81 for this link |
| 191 | IS_LNK_PCB_82 | STRING | 1 | — | PCB permission flag 82 for this link |
| 192 | IS_LNK_PCB_83 | STRING | 1 | — | PCB permission flag 83 for this link |
| 193 | IS_LNK_PCB_84 | STRING | 1 | — | PCB permission flag 84 for this link |
| 194 | IS_LNK_PCB_85 | STRING | 1 | — | PCB permission flag 85 for this link |
| 195 | IS_LNK_PCB_86 | STRING | 1 | — | PCB permission flag 86 for this link |
| 196 | IS_LNK_PCB_87 | STRING | 1 | — | PCB permission flag 87 for this link |
| 197 | IS_LNK_PCB_88 | STRING | 1 | — | PCB permission flag 88 for this link |
| 198 | IS_LNK_PCB_89 | STRING | 1 | — | PCB permission flag 89 for this link |
| 199 | IS_LNK_PCB_9 | STRING | 1 | — | PCB permission flag 9 for this link |
| 200 | IS_LNK_PCB_90 | STRING | 1 | — | PCB permission flag 90 for this link |
| 201 | IS_LNK_PCB_91 | STRING | 1 | — | PCB permission flag 91 for this link |
| 202 | IS_LNK_PCB_92 | STRING | 1 | — | PCB permission flag 92 for this link |
| 203 | IS_LNK_PCB_93 | STRING | 1 | — | PCB permission flag 93 for this link |
| 204 | IS_LNK_PCB_94 | STRING | 1 | — | PCB permission flag 94 for this link |
| 205 | IS_LNK_PCB_95 | STRING | 1 | — | PCB permission flag 95 for this link |
| 206 | IS_LNK_PCB_96 | STRING | 1 | — | PCB permission flag 96 for this link |
| 207 | IS_LNK_PCB_97 | STRING | 1 | — | PCB permission flag 97 for this link |
| 208 | IS_LNK_PCB_98 | STRING | 1 | — | PCB permission flag 98 for this link |
| 209 | IS_LNK_PCB_99 | STRING | 1 | — | PCB permission flag 99 for this link |
| 210 | IS_LNK_PRIVATE | STRING | 1 | — | Private (user-only) link flag (Y/N) |
| 211 | IS_LNK_TYPES_1 | STRING | 1 | — | Link type flag 1 |
| 212 | IS_LNK_TYPES_10 | STRING | 1 | — | Link type flag 10 |
| 213 | IS_LNK_TYPES_100 | STRING | 1 | — | Link type flag 100 |
| 214 | IS_LNK_TYPES_11 | STRING | 1 | — | Link type flag 11 |
| 215 | IS_LNK_TYPES_12 | STRING | 1 | — | Link type flag 12 |
| 216 | IS_LNK_TYPES_13 | STRING | 1 | — | Link type flag 13 |
| 217 | IS_LNK_TYPES_14 | STRING | 1 | — | Link type flag 14 |
| 218 | IS_LNK_TYPES_15 | STRING | 1 | — | Link type flag 15 |
| 219 | IS_LNK_TYPES_16 | STRING | 1 | — | Link type flag 16 |
| 220 | IS_LNK_TYPES_17 | STRING | 1 | — | Link type flag 17 |
| 221 | IS_LNK_TYPES_18 | STRING | 1 | — | Link type flag 18 |
| 222 | IS_LNK_TYPES_19 | STRING | 1 | — | Link type flag 19 |
| 223 | IS_LNK_TYPES_2 | STRING | 1 | — | Link type flag 2 |
| 224 | IS_LNK_TYPES_20 | STRING | 1 | — | Link type flag 20 |
| 225 | IS_LNK_TYPES_21 | STRING | 1 | — | Link type flag 21 |
| 226 | IS_LNK_TYPES_22 | STRING | 1 | — | Link type flag 22 |
| 227 | IS_LNK_TYPES_23 | STRING | 1 | — | Link type flag 23 |
| 228 | IS_LNK_TYPES_24 | STRING | 1 | — | Link type flag 24 |
| 229 | IS_LNK_TYPES_25 | STRING | 1 | — | Link type flag 25 |
| 230 | IS_LNK_TYPES_26 | STRING | 1 | — | Link type flag 26 |
| 231 | IS_LNK_TYPES_27 | STRING | 1 | — | Link type flag 27 |
| 232 | IS_LNK_TYPES_28 | STRING | 1 | — | Link type flag 28 |
| 233 | IS_LNK_TYPES_29 | STRING | 1 | — | Link type flag 29 |
| 234 | IS_LNK_TYPES_3 | STRING | 1 | — | Link type flag 3 |
| 235 | IS_LNK_TYPES_30 | STRING | 1 | — | Link type flag 30 |
| 236 | IS_LNK_TYPES_31 | STRING | 1 | — | Link type flag 31 |
| 237 | IS_LNK_TYPES_32 | STRING | 1 | — | Link type flag 32 |
| 238 | IS_LNK_TYPES_33 | STRING | 1 | — | Link type flag 33 |
| 239 | IS_LNK_TYPES_34 | STRING | 1 | — | Link type flag 34 |
| 240 | IS_LNK_TYPES_35 | STRING | 1 | — | Link type flag 35 |
| 241 | IS_LNK_TYPES_36 | STRING | 1 | — | Link type flag 36 |
| 242 | IS_LNK_TYPES_37 | STRING | 1 | — | Link type flag 37 |
| 243 | IS_LNK_TYPES_38 | STRING | 1 | — | Link type flag 38 |
| 244 | IS_LNK_TYPES_39 | STRING | 1 | — | Link type flag 39 |
| 245 | IS_LNK_TYPES_4 | STRING | 1 | — | Link type flag 4 |
| 246 | IS_LNK_TYPES_40 | STRING | 1 | — | Link type flag 40 |
| 247 | IS_LNK_TYPES_41 | STRING | 1 | — | Link type flag 41 |
| 248 | IS_LNK_TYPES_42 | STRING | 1 | — | Link type flag 42 |
| 249 | IS_LNK_TYPES_43 | STRING | 1 | — | Link type flag 43 |
| 250 | IS_LNK_TYPES_44 | STRING | 1 | — | Link type flag 44 |
| 251 | IS_LNK_TYPES_45 | STRING | 1 | — | Link type flag 45 |
| 252 | IS_LNK_TYPES_46 | STRING | 1 | — | Link type flag 46 |
| 253 | IS_LNK_TYPES_47 | STRING | 1 | — | Link type flag 47 |
| 254 | IS_LNK_TYPES_48 | STRING | 1 | — | Link type flag 48 |
| 255 | IS_LNK_TYPES_49 | STRING | 1 | — | Link type flag 49 |
| 256 | IS_LNK_TYPES_5 | STRING | 1 | — | Link type flag 5 |
| 257 | IS_LNK_TYPES_50 | STRING | 1 | — | Link type flag 50 |
| 258 | IS_LNK_TYPES_51 | STRING | 1 | — | Link type flag 51 |
| 259 | IS_LNK_TYPES_52 | STRING | 1 | — | Link type flag 52 |
| 260 | IS_LNK_TYPES_53 | STRING | 1 | — | Link type flag 53 |
| 261 | IS_LNK_TYPES_54 | STRING | 1 | — | Link type flag 54 |
| 262 | IS_LNK_TYPES_55 | STRING | 1 | — | Link type flag 55 |
| 263 | IS_LNK_TYPES_56 | STRING | 1 | — | Link type flag 56 |
| 264 | IS_LNK_TYPES_57 | STRING | 1 | — | Link type flag 57 |
| 265 | IS_LNK_TYPES_58 | STRING | 1 | — | Link type flag 58 |
| 266 | IS_LNK_TYPES_59 | STRING | 1 | — | Link type flag 59 |
| 267 | IS_LNK_TYPES_6 | STRING | 1 | — | Link type flag 6 |
| 268 | IS_LNK_TYPES_60 | STRING | 1 | — | Link type flag 60 |
| 269 | IS_LNK_TYPES_61 | STRING | 1 | — | Link type flag 61 |
| 270 | IS_LNK_TYPES_62 | STRING | 1 | — | Link type flag 62 |
| 271 | IS_LNK_TYPES_63 | STRING | 1 | — | Link type flag 63 |
| 272 | IS_LNK_TYPES_64 | STRING | 1 | — | Link type flag 64 |
| 273 | IS_LNK_TYPES_65 | STRING | 1 | — | Link type flag 65 |
| 274 | IS_LNK_TYPES_66 | STRING | 1 | — | Link type flag 66 |
| 275 | IS_LNK_TYPES_67 | STRING | 1 | — | Link type flag 67 |
| 276 | IS_LNK_TYPES_68 | STRING | 1 | — | Link type flag 68 |
| 277 | IS_LNK_TYPES_69 | STRING | 1 | — | Link type flag 69 |
| 278 | IS_LNK_TYPES_7 | STRING | 1 | — | Link type flag 7 |
| 279 | IS_LNK_TYPES_70 | STRING | 1 | — | Link type flag 70 |
| 280 | IS_LNK_TYPES_71 | STRING | 1 | — | Link type flag 71 |
| 281 | IS_LNK_TYPES_72 | STRING | 1 | — | Link type flag 72 |
| 282 | IS_LNK_TYPES_73 | STRING | 1 | — | Link type flag 73 |
| 283 | IS_LNK_TYPES_74 | STRING | 1 | — | Link type flag 74 |
| 284 | IS_LNK_TYPES_75 | STRING | 1 | — | Link type flag 75 |
| 285 | IS_LNK_TYPES_76 | STRING | 1 | — | Link type flag 76 |
| 286 | IS_LNK_TYPES_77 | STRING | 1 | — | Link type flag 77 |
| 287 | IS_LNK_TYPES_78 | STRING | 1 | — | Link type flag 78 |
| 288 | IS_LNK_TYPES_79 | STRING | 1 | — | Link type flag 79 |
| 289 | IS_LNK_TYPES_8 | STRING | 1 | — | Link type flag 8 |
| 290 | IS_LNK_TYPES_80 | STRING | 1 | — | Link type flag 80 |
| 291 | IS_LNK_TYPES_81 | STRING | 1 | — | Link type flag 81 |
| 292 | IS_LNK_TYPES_82 | STRING | 1 | — | Link type flag 82 |
| 293 | IS_LNK_TYPES_83 | STRING | 1 | — | Link type flag 83 |
| 294 | IS_LNK_TYPES_84 | STRING | 1 | — | Link type flag 84 |
| 295 | IS_LNK_TYPES_85 | STRING | 1 | — | Link type flag 85 |
| 296 | IS_LNK_TYPES_86 | STRING | 1 | — | Link type flag 86 |
| 297 | IS_LNK_TYPES_87 | STRING | 1 | — | Link type flag 87 |
| 298 | IS_LNK_TYPES_88 | STRING | 1 | — | Link type flag 88 |
| 299 | IS_LNK_TYPES_89 | STRING | 1 | — | Link type flag 89 |
| 300 | IS_LNK_TYPES_9 | STRING | 1 | — | Link type flag 9 |
| 301 | IS_LNK_TYPES_90 | STRING | 1 | — | Link type flag 90 |
| 302 | IS_LNK_TYPES_91 | STRING | 1 | — | Link type flag 91 |
| 303 | IS_LNK_TYPES_92 | STRING | 1 | — | Link type flag 92 |
| 304 | IS_LNK_TYPES_93 | STRING | 1 | — | Link type flag 93 |
| 305 | IS_LNK_TYPES_94 | STRING | 1 | — | Link type flag 94 |
| 306 | IS_LNK_TYPES_95 | STRING | 1 | — | Link type flag 95 |
| 307 | IS_LNK_TYPES_96 | STRING | 1 | — | Link type flag 96 |
| 308 | IS_LNK_TYPES_97 | STRING | 1 | — | Link type flag 97 |
| 309 | IS_LNK_TYPES_98 | STRING | 1 | — | Link type flag 98 |
| 310 | IS_LNK_TYPES_99 | STRING | 1 | — | Link type flag 99 |
| 311 | IS_LNK_UID | STRING | 48 | — | Unique identifier of the parent record |
| 312 | IS_LNK_WHO | STRING | 15 | — | User who created or owns this link |

## ISANOTES
**ARCHIVED NOTES**

Fields: 14

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_NOTE_ALPHA | STRING | 6000 | — | Full text/blob content for this note |
| 2 | IS_NOTE_CDATE | DATE | 4 | — | Note creation date |
| 3 | IS_NOTE_CONTACT | STRING | 30 | — | Contact name associated with note |
| 4 | IS_NOTE_CTIME | STRING | 10 | — | Note creation time (HH:MM:SS) |
| 5 | IS_NOTE_CWHO | STRING | 15 | — | User who created the note |
| 6 | IS_NOTE_EDATE | DATE | 4 | — | Note last-edited date |
| 7 | IS_NOTE_ETIME | STRING | 10 | — | Note last-edited time (HH:MM:SS) |
| 8 | IS_NOTE_EWHO | STRING | 15 | — | User who last edited the note |
| 9 | IS_NOTE_EXTRA | STRING | 100 | — | Reserved extra field |
| 10 | IS_NOTE_GROUP | STRING | 4 | — | Note category/group code |
| 11 | IS_NOTE_ID | STRING | 48 | — | Unique identifier of the parent record |
| 12 | IS_NOTE_NOTE | STRING | 0 | — | Memo/blob note body |
| 13 | IS_NOTE_PRIVATE | STRING | 1 | — | Private note flag (Y/N) |
| 14 | IS_NOTE_TYPE | STRING | 3 | — | Note type code |

## ISBUILD
**REPORT SORT FILE**

Fields: 8

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_BUILD_DSORT | DATE | 4 | — | Date sort key for index building |
| 2 | IS_BUILD_EXTRA | STRING | 50 | — | Reserved extra field |
| 3 | IS_BUILD_FILE | STRING | 8 | — | Source file name for index build record |
| 4 | IS_BUILD_NSORT | NUMERIC | 8 | 4 | Numeric sort key (4 decimal places) |
| 5 | IS_BUILD_REC | INTEGER | 4 | — | Primary record number |
| 6 | IS_BUILD_REC2 | INTEGER | 4 | — | Secondary record number |
| 7 | IS_BUILD_SORT | STRING | 215 | — | Composite sort key string |
| 8 | IS_BUILD_UID | STRING | 40 | — | UID of the record being indexed |

## ISCHAIN
**AUTO CHAIN PROGRAMS**

Fields: 17

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_CHAIN_AUTO | STRING | 1 | — | Auto-launch chain on trigger flag (Y/N) |
| 2 | IS_CHAIN_CHILD | STRING | 12 | — | Child program name in chain |
| 3 | IS_CHAIN_DATE | DATE | 4 | — | Chain definition date |
| 4 | IS_CHAIN_DESC | STRING | 100 | — | Chain description |
| 5 | IS_CHAIN_EXTRA | STRING | 100 | — | Reserved extra field |
| 6 | IS_CHAIN_PARAM_1 | STRING | 15 | — | Parameter 1 passed to chained program |
| 7 | IS_CHAIN_PARAM_10 | STRING | 15 | — | Parameter 10 passed to chained program |
| 8 | IS_CHAIN_PARAM_2 | STRING | 15 | — | Parameter 2 passed to chained program |
| 9 | IS_CHAIN_PARAM_3 | STRING | 15 | — | Parameter 3 passed to chained program |
| 10 | IS_CHAIN_PARAM_4 | STRING | 15 | — | Parameter 4 passed to chained program |
| 11 | IS_CHAIN_PARAM_5 | STRING | 15 | — | Parameter 5 passed to chained program |
| 12 | IS_CHAIN_PARAM_6 | STRING | 15 | — | Parameter 6 passed to chained program |
| 13 | IS_CHAIN_PARAM_7 | STRING | 15 | — | Parameter 7 passed to chained program |
| 14 | IS_CHAIN_PARAM_8 | STRING | 15 | — | Parameter 8 passed to chained program |
| 15 | IS_CHAIN_PARAM_9 | STRING | 15 | — | Parameter 9 passed to chained program |
| 16 | IS_CHAIN_PARENT | STRING | 12 | — | Parent program name in chain |
| 17 | IS_CHAIN_USER | STRING | 15 | — | User who defined the chain |

## ISCHAINM
**AUTO CHAIN PROGRAM MASTER**

Fields: 17

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_CHAIN_AUTO | STRING | 1 | — | Auto-launch chain on trigger flag (Y/N) |
| 2 | IS_CHAIN_CHILD | STRING | 12 | — | Child program name in chain |
| 3 | IS_CHAIN_DATE | DATE | 4 | — | Chain definition date |
| 4 | IS_CHAIN_DESC | STRING | 100 | — | Chain description |
| 5 | IS_CHAIN_EXTRA | STRING | 100 | — | Reserved extra field |
| 6 | IS_CHAIN_PARAM_1 | STRING | 15 | — | Parameter 1 passed to chained program |
| 7 | IS_CHAIN_PARAM_10 | STRING | 15 | — | Parameter 10 passed to chained program |
| 8 | IS_CHAIN_PARAM_2 | STRING | 15 | — | Parameter 2 passed to chained program |
| 9 | IS_CHAIN_PARAM_3 | STRING | 15 | — | Parameter 3 passed to chained program |
| 10 | IS_CHAIN_PARAM_4 | STRING | 15 | — | Parameter 4 passed to chained program |
| 11 | IS_CHAIN_PARAM_5 | STRING | 15 | — | Parameter 5 passed to chained program |
| 12 | IS_CHAIN_PARAM_6 | STRING | 15 | — | Parameter 6 passed to chained program |
| 13 | IS_CHAIN_PARAM_7 | STRING | 15 | — | Parameter 7 passed to chained program |
| 14 | IS_CHAIN_PARAM_8 | STRING | 15 | — | Parameter 8 passed to chained program |
| 15 | IS_CHAIN_PARAM_9 | STRING | 15 | — | Parameter 9 passed to chained program |
| 16 | IS_CHAIN_PARENT | STRING | 12 | — | Parent program name in chain |
| 17 | IS_CHAIN_USER | STRING | 15 | — | User who defined the chain |

## ISDLCK1
**LOCK FILE FOR NEXT NUMBER PROGRAM**

Fields: 1

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BUBBA | STRING | 10 | — | Lock record placeholder field (no functional data) |

## ISDLCK2
**LOCK FILE FOR MASTER DEFAULT PROGRAM**

Fields: 1

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BUBBA | STRING | 10 | — | Lock record placeholder field (no functional data) |

## ISDRILLM
**MASTER DRILL DOWN FILE**

Fields: 17

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | DRILLM_CHILD | STRING | 15 | — | Child program for drill-down navigation |
| 2 | DRILLM_EXTAR | STRING | 150 | — | Extra/reserved field |
| 3 | DRILLM_FILE | STRING | 15 | — | Data file for drill-down source |
| 4 | DRILLM_KEY | STRING | 15 | — | Key field for drill-down lookup |
| 5 | DRILLM_MENU | STRING | 25 | — | Menu entry text for drill-down option |
| 6 | DRILLM_PARENT | STRING | 15 | — | Parent program that launches drill-down |
| 7 | DRILLM_PFILE | STRING | 15 | — | Parent data file for drill-down |
| 8 | DRILLM_SFIELD_1 | STRING | 15 | — | Source field 1 for drill-down key mapping |
| 9 | DRILLM_SFIELD_2 | STRING | 15 | — | Source field 2 for drill-down key mapping |
| 10 | DRILLM_SFIELD_3 | STRING | 15 | — | Source field 3 for drill-down key mapping |
| 11 | DRILLM_SFIELD_4 | STRING | 15 | — | Source field 4 for drill-down key mapping |
| 12 | DRILLM_SFIELD_5 | STRING | 15 | — | Source field 5 for drill-down key mapping |
| 13 | DRILLM_TFIELD_1 | STRING | 15 | — | Target field 1 for drill-down key mapping |
| 14 | DRILLM_TFIELD_2 | STRING | 15 | — | Target field 2 for drill-down key mapping |
| 15 | DRILLM_TFIELD_3 | STRING | 15 | — | Target field 3 for drill-down key mapping |
| 16 | DRILLM_TFIELD_4 | STRING | 15 | — | Target field 4 for drill-down key mapping |
| 17 | DRILLM_TFIELD_5 | STRING | 15 | — | Target field 5 for drill-down key mapping |

## ISFIELDS
**IMPORT FIELD LISTING**

Fields: 7

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_FLDS_ANUM | INTEGER | 2 | — | Field attribute number |
| 2 | IS_FLDS_DESC | STRING | 40 | — | Field description/label |
| 3 | IS_FLDS_EXTRA | STRING | 50 | — | Reserved extra field |
| 4 | IS_FLDS_FD | STRING | 8 | — | File/dictionary name this field belongs to |
| 5 | IS_FLDS_FIELD | STRING | 15 | — | Field name |
| 6 | IS_FLDS_NUM | INTEGER | 2 | — | Field sequence number |
| 7 | IS_FLDS_REQUIRE | STRING | 1 | — | Required field flag (Y/N) |

## ISJOB
**JOB MASTER LISTING**

Fields: 9

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_JOB_CLOSEDT | DATE | 4 | — | Job close date |
| 2 | IS_JOB_CUST | STRING | 10 | — | Customer code for this job |
| 3 | IS_JOB_DESC | STRING | 30 | — | Job description |
| 4 | IS_JOB_EXTRA | STRING | 100 | — | Reserved extra field |
| 5 | IS_JOB_NUMB | STRING | 15 | — | Job number |
| 6 | IS_JOB_OPENDT | DATE | 4 | — | Job open/start date |
| 7 | IS_JOB_RSVD | STRING | 1 | — | Reserved flag |
| 8 | IS_JOB_STATUS | STRING | 1 | — | Job status code (O=Open, C=Closed) |
| 9 | IS_JOB_VEND | STRING | 10 | — | Vendor code for this job |

## ISLINKS
**EVO LINKS**

Fields: 312

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_LNK_ALPHA | STRING | 6000 | — | Full text/blob content for this link |
| 2 | IS_LNK_APP | STRING | 10 | — | Application module this link belongs to |
| 3 | IS_LNK_ATYPE | STRING | 3 | — | Archive type code |
| 4 | IS_LNK_DATE | DATE | 4 | — | Date link was created |
| 5 | IS_LNK_DEF_1 | STRING | 1 | — | Default flag 1 for this link definition |
| 6 | IS_LNK_DEF_10 | STRING | 1 | — | Default flag 10 for this link definition |
| 7 | IS_LNK_DEF_100 | STRING | 1 | — | Default flag 100 for this link definition |
| 8 | IS_LNK_DEF_11 | STRING | 1 | — | Default flag 11 for this link definition |
| 9 | IS_LNK_DEF_12 | STRING | 1 | — | Default flag 12 for this link definition |
| 10 | IS_LNK_DEF_13 | STRING | 1 | — | Default flag 13 for this link definition |
| 11 | IS_LNK_DEF_14 | STRING | 1 | — | Default flag 14 for this link definition |
| 12 | IS_LNK_DEF_15 | STRING | 1 | — | Default flag 15 for this link definition |
| 13 | IS_LNK_DEF_16 | STRING | 1 | — | Default flag 16 for this link definition |
| 14 | IS_LNK_DEF_17 | STRING | 1 | — | Default flag 17 for this link definition |
| 15 | IS_LNK_DEF_18 | STRING | 1 | — | Default flag 18 for this link definition |
| 16 | IS_LNK_DEF_19 | STRING | 1 | — | Default flag 19 for this link definition |
| 17 | IS_LNK_DEF_2 | STRING | 1 | — | Default flag 2 for this link definition |
| 18 | IS_LNK_DEF_20 | STRING | 1 | — | Default flag 20 for this link definition |
| 19 | IS_LNK_DEF_21 | STRING | 1 | — | Default flag 21 for this link definition |
| 20 | IS_LNK_DEF_22 | STRING | 1 | — | Default flag 22 for this link definition |
| 21 | IS_LNK_DEF_23 | STRING | 1 | — | Default flag 23 for this link definition |
| 22 | IS_LNK_DEF_24 | STRING | 1 | — | Default flag 24 for this link definition |
| 23 | IS_LNK_DEF_25 | STRING | 1 | — | Default flag 25 for this link definition |
| 24 | IS_LNK_DEF_26 | STRING | 1 | — | Default flag 26 for this link definition |
| 25 | IS_LNK_DEF_27 | STRING | 1 | — | Default flag 27 for this link definition |
| 26 | IS_LNK_DEF_28 | STRING | 1 | — | Default flag 28 for this link definition |
| 27 | IS_LNK_DEF_29 | STRING | 1 | — | Default flag 29 for this link definition |
| 28 | IS_LNK_DEF_3 | STRING | 1 | — | Default flag 3 for this link definition |
| 29 | IS_LNK_DEF_30 | STRING | 1 | — | Default flag 30 for this link definition |
| 30 | IS_LNK_DEF_31 | STRING | 1 | — | Default flag 31 for this link definition |
| 31 | IS_LNK_DEF_32 | STRING | 1 | — | Default flag 32 for this link definition |
| 32 | IS_LNK_DEF_33 | STRING | 1 | — | Default flag 33 for this link definition |
| 33 | IS_LNK_DEF_34 | STRING | 1 | — | Default flag 34 for this link definition |
| 34 | IS_LNK_DEF_35 | STRING | 1 | — | Default flag 35 for this link definition |
| 35 | IS_LNK_DEF_36 | STRING | 1 | — | Default flag 36 for this link definition |
| 36 | IS_LNK_DEF_37 | STRING | 1 | — | Default flag 37 for this link definition |
| 37 | IS_LNK_DEF_38 | STRING | 1 | — | Default flag 38 for this link definition |
| 38 | IS_LNK_DEF_39 | STRING | 1 | — | Default flag 39 for this link definition |
| 39 | IS_LNK_DEF_4 | STRING | 1 | — | Default flag 4 for this link definition |
| 40 | IS_LNK_DEF_40 | STRING | 1 | — | Default flag 40 for this link definition |
| 41 | IS_LNK_DEF_41 | STRING | 1 | — | Default flag 41 for this link definition |
| 42 | IS_LNK_DEF_42 | STRING | 1 | — | Default flag 42 for this link definition |
| 43 | IS_LNK_DEF_43 | STRING | 1 | — | Default flag 43 for this link definition |
| 44 | IS_LNK_DEF_44 | STRING | 1 | — | Default flag 44 for this link definition |
| 45 | IS_LNK_DEF_45 | STRING | 1 | — | Default flag 45 for this link definition |
| 46 | IS_LNK_DEF_46 | STRING | 1 | — | Default flag 46 for this link definition |
| 47 | IS_LNK_DEF_47 | STRING | 1 | — | Default flag 47 for this link definition |
| 48 | IS_LNK_DEF_48 | STRING | 1 | — | Default flag 48 for this link definition |
| 49 | IS_LNK_DEF_49 | STRING | 1 | — | Default flag 49 for this link definition |
| 50 | IS_LNK_DEF_5 | STRING | 1 | — | Default flag 5 for this link definition |
| 51 | IS_LNK_DEF_50 | STRING | 1 | — | Default flag 50 for this link definition |
| 52 | IS_LNK_DEF_51 | STRING | 1 | — | Default flag 51 for this link definition |
| 53 | IS_LNK_DEF_52 | STRING | 1 | — | Default flag 52 for this link definition |
| 54 | IS_LNK_DEF_53 | STRING | 1 | — | Default flag 53 for this link definition |
| 55 | IS_LNK_DEF_54 | STRING | 1 | — | Default flag 54 for this link definition |
| 56 | IS_LNK_DEF_55 | STRING | 1 | — | Default flag 55 for this link definition |
| 57 | IS_LNK_DEF_56 | STRING | 1 | — | Default flag 56 for this link definition |
| 58 | IS_LNK_DEF_57 | STRING | 1 | — | Default flag 57 for this link definition |
| 59 | IS_LNK_DEF_58 | STRING | 1 | — | Default flag 58 for this link definition |
| 60 | IS_LNK_DEF_59 | STRING | 1 | — | Default flag 59 for this link definition |
| 61 | IS_LNK_DEF_6 | STRING | 1 | — | Default flag 6 for this link definition |
| 62 | IS_LNK_DEF_60 | STRING | 1 | — | Default flag 60 for this link definition |
| 63 | IS_LNK_DEF_61 | STRING | 1 | — | Default flag 61 for this link definition |
| 64 | IS_LNK_DEF_62 | STRING | 1 | — | Default flag 62 for this link definition |
| 65 | IS_LNK_DEF_63 | STRING | 1 | — | Default flag 63 for this link definition |
| 66 | IS_LNK_DEF_64 | STRING | 1 | — | Default flag 64 for this link definition |
| 67 | IS_LNK_DEF_65 | STRING | 1 | — | Default flag 65 for this link definition |
| 68 | IS_LNK_DEF_66 | STRING | 1 | — | Default flag 66 for this link definition |
| 69 | IS_LNK_DEF_67 | STRING | 1 | — | Default flag 67 for this link definition |
| 70 | IS_LNK_DEF_68 | STRING | 1 | — | Default flag 68 for this link definition |
| 71 | IS_LNK_DEF_69 | STRING | 1 | — | Default flag 69 for this link definition |
| 72 | IS_LNK_DEF_7 | STRING | 1 | — | Default flag 7 for this link definition |
| 73 | IS_LNK_DEF_70 | STRING | 1 | — | Default flag 70 for this link definition |
| 74 | IS_LNK_DEF_71 | STRING | 1 | — | Default flag 71 for this link definition |
| 75 | IS_LNK_DEF_72 | STRING | 1 | — | Default flag 72 for this link definition |
| 76 | IS_LNK_DEF_73 | STRING | 1 | — | Default flag 73 for this link definition |
| 77 | IS_LNK_DEF_74 | STRING | 1 | — | Default flag 74 for this link definition |
| 78 | IS_LNK_DEF_75 | STRING | 1 | — | Default flag 75 for this link definition |
| 79 | IS_LNK_DEF_76 | STRING | 1 | — | Default flag 76 for this link definition |
| 80 | IS_LNK_DEF_77 | STRING | 1 | — | Default flag 77 for this link definition |
| 81 | IS_LNK_DEF_78 | STRING | 1 | — | Default flag 78 for this link definition |
| 82 | IS_LNK_DEF_79 | STRING | 1 | — | Default flag 79 for this link definition |
| 83 | IS_LNK_DEF_8 | STRING | 1 | — | Default flag 8 for this link definition |
| 84 | IS_LNK_DEF_80 | STRING | 1 | — | Default flag 80 for this link definition |
| 85 | IS_LNK_DEF_81 | STRING | 1 | — | Default flag 81 for this link definition |
| 86 | IS_LNK_DEF_82 | STRING | 1 | — | Default flag 82 for this link definition |
| 87 | IS_LNK_DEF_83 | STRING | 1 | — | Default flag 83 for this link definition |
| 88 | IS_LNK_DEF_84 | STRING | 1 | — | Default flag 84 for this link definition |
| 89 | IS_LNK_DEF_85 | STRING | 1 | — | Default flag 85 for this link definition |
| 90 | IS_LNK_DEF_86 | STRING | 1 | — | Default flag 86 for this link definition |
| 91 | IS_LNK_DEF_87 | STRING | 1 | — | Default flag 87 for this link definition |
| 92 | IS_LNK_DEF_88 | STRING | 1 | — | Default flag 88 for this link definition |
| 93 | IS_LNK_DEF_89 | STRING | 1 | — | Default flag 89 for this link definition |
| 94 | IS_LNK_DEF_9 | STRING | 1 | — | Default flag 9 for this link definition |
| 95 | IS_LNK_DEF_90 | STRING | 1 | — | Default flag 90 for this link definition |
| 96 | IS_LNK_DEF_91 | STRING | 1 | — | Default flag 91 for this link definition |
| 97 | IS_LNK_DEF_92 | STRING | 1 | — | Default flag 92 for this link definition |
| 98 | IS_LNK_DEF_93 | STRING | 1 | — | Default flag 93 for this link definition |
| 99 | IS_LNK_DEF_94 | STRING | 1 | — | Default flag 94 for this link definition |
| 100 | IS_LNK_DEF_95 | STRING | 1 | — | Default flag 95 for this link definition |
| 101 | IS_LNK_DEF_96 | STRING | 1 | — | Default flag 96 for this link definition |
| 102 | IS_LNK_DEF_97 | STRING | 1 | — | Default flag 97 for this link definition |
| 103 | IS_LNK_DEF_98 | STRING | 1 | — | Default flag 98 for this link definition |
| 104 | IS_LNK_DEF_99 | STRING | 1 | — | Default flag 99 for this link definition |
| 105 | IS_LNK_EXTRA | STRING | 100 | — | Reserved extra field |
| 106 | IS_LNK_GLOBAL | STRING | 1 | — | Global (company-wide) link flag (Y/N) |
| 107 | IS_LNK_LINK | STRING | 256 | — | File path or URL for this link |
| 108 | IS_LNK_NOTE | STRING | 0 | — | Memo/blob note field |
| 109 | IS_LNK_OPENWITH | STRING | 1 | — | Open-with application preference flag |
| 110 | IS_LNK_PCB_1 | STRING | 1 | — | PCB permission flag 1 for this link |
| 111 | IS_LNK_PCB_10 | STRING | 1 | — | PCB permission flag 10 for this link |
| 112 | IS_LNK_PCB_100 | STRING | 1 | — | PCB permission flag 100 for this link |
| 113 | IS_LNK_PCB_11 | STRING | 1 | — | PCB permission flag 11 for this link |
| 114 | IS_LNK_PCB_12 | STRING | 1 | — | PCB permission flag 12 for this link |
| 115 | IS_LNK_PCB_13 | STRING | 1 | — | PCB permission flag 13 for this link |
| 116 | IS_LNK_PCB_14 | STRING | 1 | — | PCB permission flag 14 for this link |
| 117 | IS_LNK_PCB_15 | STRING | 1 | — | PCB permission flag 15 for this link |
| 118 | IS_LNK_PCB_16 | STRING | 1 | — | PCB permission flag 16 for this link |
| 119 | IS_LNK_PCB_17 | STRING | 1 | — | PCB permission flag 17 for this link |
| 120 | IS_LNK_PCB_18 | STRING | 1 | — | PCB permission flag 18 for this link |
| 121 | IS_LNK_PCB_19 | STRING | 1 | — | PCB permission flag 19 for this link |
| 122 | IS_LNK_PCB_2 | STRING | 1 | — | PCB permission flag 2 for this link |
| 123 | IS_LNK_PCB_20 | STRING | 1 | — | PCB permission flag 20 for this link |
| 124 | IS_LNK_PCB_21 | STRING | 1 | — | PCB permission flag 21 for this link |
| 125 | IS_LNK_PCB_22 | STRING | 1 | — | PCB permission flag 22 for this link |
| 126 | IS_LNK_PCB_23 | STRING | 1 | — | PCB permission flag 23 for this link |
| 127 | IS_LNK_PCB_24 | STRING | 1 | — | PCB permission flag 24 for this link |
| 128 | IS_LNK_PCB_25 | STRING | 1 | — | PCB permission flag 25 for this link |
| 129 | IS_LNK_PCB_26 | STRING | 1 | — | PCB permission flag 26 for this link |
| 130 | IS_LNK_PCB_27 | STRING | 1 | — | PCB permission flag 27 for this link |
| 131 | IS_LNK_PCB_28 | STRING | 1 | — | PCB permission flag 28 for this link |
| 132 | IS_LNK_PCB_29 | STRING | 1 | — | PCB permission flag 29 for this link |
| 133 | IS_LNK_PCB_3 | STRING | 1 | — | PCB permission flag 3 for this link |
| 134 | IS_LNK_PCB_30 | STRING | 1 | — | PCB permission flag 30 for this link |
| 135 | IS_LNK_PCB_31 | STRING | 1 | — | PCB permission flag 31 for this link |
| 136 | IS_LNK_PCB_32 | STRING | 1 | — | PCB permission flag 32 for this link |
| 137 | IS_LNK_PCB_33 | STRING | 1 | — | PCB permission flag 33 for this link |
| 138 | IS_LNK_PCB_34 | STRING | 1 | — | PCB permission flag 34 for this link |
| 139 | IS_LNK_PCB_35 | STRING | 1 | — | PCB permission flag 35 for this link |
| 140 | IS_LNK_PCB_36 | STRING | 1 | — | PCB permission flag 36 for this link |
| 141 | IS_LNK_PCB_37 | STRING | 1 | — | PCB permission flag 37 for this link |
| 142 | IS_LNK_PCB_38 | STRING | 1 | — | PCB permission flag 38 for this link |
| 143 | IS_LNK_PCB_39 | STRING | 1 | — | PCB permission flag 39 for this link |
| 144 | IS_LNK_PCB_4 | STRING | 1 | — | PCB permission flag 4 for this link |
| 145 | IS_LNK_PCB_40 | STRING | 1 | — | PCB permission flag 40 for this link |
| 146 | IS_LNK_PCB_41 | STRING | 1 | — | PCB permission flag 41 for this link |
| 147 | IS_LNK_PCB_42 | STRING | 1 | — | PCB permission flag 42 for this link |
| 148 | IS_LNK_PCB_43 | STRING | 1 | — | PCB permission flag 43 for this link |
| 149 | IS_LNK_PCB_44 | STRING | 1 | — | PCB permission flag 44 for this link |
| 150 | IS_LNK_PCB_45 | STRING | 1 | — | PCB permission flag 45 for this link |
| 151 | IS_LNK_PCB_46 | STRING | 1 | — | PCB permission flag 46 for this link |
| 152 | IS_LNK_PCB_47 | STRING | 1 | — | PCB permission flag 47 for this link |
| 153 | IS_LNK_PCB_48 | STRING | 1 | — | PCB permission flag 48 for this link |
| 154 | IS_LNK_PCB_49 | STRING | 1 | — | PCB permission flag 49 for this link |
| 155 | IS_LNK_PCB_5 | STRING | 1 | — | PCB permission flag 5 for this link |
| 156 | IS_LNK_PCB_50 | STRING | 1 | — | PCB permission flag 50 for this link |
| 157 | IS_LNK_PCB_51 | STRING | 1 | — | PCB permission flag 51 for this link |
| 158 | IS_LNK_PCB_52 | STRING | 1 | — | PCB permission flag 52 for this link |
| 159 | IS_LNK_PCB_53 | STRING | 1 | — | PCB permission flag 53 for this link |
| 160 | IS_LNK_PCB_54 | STRING | 1 | — | PCB permission flag 54 for this link |
| 161 | IS_LNK_PCB_55 | STRING | 1 | — | PCB permission flag 55 for this link |
| 162 | IS_LNK_PCB_56 | STRING | 1 | — | PCB permission flag 56 for this link |
| 163 | IS_LNK_PCB_57 | STRING | 1 | — | PCB permission flag 57 for this link |
| 164 | IS_LNK_PCB_58 | STRING | 1 | — | PCB permission flag 58 for this link |
| 165 | IS_LNK_PCB_59 | STRING | 1 | — | PCB permission flag 59 for this link |
| 166 | IS_LNK_PCB_6 | STRING | 1 | — | PCB permission flag 6 for this link |
| 167 | IS_LNK_PCB_60 | STRING | 1 | — | PCB permission flag 60 for this link |
| 168 | IS_LNK_PCB_61 | STRING | 1 | — | PCB permission flag 61 for this link |
| 169 | IS_LNK_PCB_62 | STRING | 1 | — | PCB permission flag 62 for this link |
| 170 | IS_LNK_PCB_63 | STRING | 1 | — | PCB permission flag 63 for this link |
| 171 | IS_LNK_PCB_64 | STRING | 1 | — | PCB permission flag 64 for this link |
| 172 | IS_LNK_PCB_65 | STRING | 1 | — | PCB permission flag 65 for this link |
| 173 | IS_LNK_PCB_66 | STRING | 1 | — | PCB permission flag 66 for this link |
| 174 | IS_LNK_PCB_67 | STRING | 1 | — | PCB permission flag 67 for this link |
| 175 | IS_LNK_PCB_68 | STRING | 1 | — | PCB permission flag 68 for this link |
| 176 | IS_LNK_PCB_69 | STRING | 1 | — | PCB permission flag 69 for this link |
| 177 | IS_LNK_PCB_7 | STRING | 1 | — | PCB permission flag 7 for this link |
| 178 | IS_LNK_PCB_70 | STRING | 1 | — | PCB permission flag 70 for this link |
| 179 | IS_LNK_PCB_71 | STRING | 1 | — | PCB permission flag 71 for this link |
| 180 | IS_LNK_PCB_72 | STRING | 1 | — | PCB permission flag 72 for this link |
| 181 | IS_LNK_PCB_73 | STRING | 1 | — | PCB permission flag 73 for this link |
| 182 | IS_LNK_PCB_74 | STRING | 1 | — | PCB permission flag 74 for this link |
| 183 | IS_LNK_PCB_75 | STRING | 1 | — | PCB permission flag 75 for this link |
| 184 | IS_LNK_PCB_76 | STRING | 1 | — | PCB permission flag 76 for this link |
| 185 | IS_LNK_PCB_77 | STRING | 1 | — | PCB permission flag 77 for this link |
| 186 | IS_LNK_PCB_78 | STRING | 1 | — | PCB permission flag 78 for this link |
| 187 | IS_LNK_PCB_79 | STRING | 1 | — | PCB permission flag 79 for this link |
| 188 | IS_LNK_PCB_8 | STRING | 1 | — | PCB permission flag 8 for this link |
| 189 | IS_LNK_PCB_80 | STRING | 1 | — | PCB permission flag 80 for this link |
| 190 | IS_LNK_PCB_81 | STRING | 1 | — | PCB permission flag 81 for this link |
| 191 | IS_LNK_PCB_82 | STRING | 1 | — | PCB permission flag 82 for this link |
| 192 | IS_LNK_PCB_83 | STRING | 1 | — | PCB permission flag 83 for this link |
| 193 | IS_LNK_PCB_84 | STRING | 1 | — | PCB permission flag 84 for this link |
| 194 | IS_LNK_PCB_85 | STRING | 1 | — | PCB permission flag 85 for this link |
| 195 | IS_LNK_PCB_86 | STRING | 1 | — | PCB permission flag 86 for this link |
| 196 | IS_LNK_PCB_87 | STRING | 1 | — | PCB permission flag 87 for this link |
| 197 | IS_LNK_PCB_88 | STRING | 1 | — | PCB permission flag 88 for this link |
| 198 | IS_LNK_PCB_89 | STRING | 1 | — | PCB permission flag 89 for this link |
| 199 | IS_LNK_PCB_9 | STRING | 1 | — | PCB permission flag 9 for this link |
| 200 | IS_LNK_PCB_90 | STRING | 1 | — | PCB permission flag 90 for this link |
| 201 | IS_LNK_PCB_91 | STRING | 1 | — | PCB permission flag 91 for this link |
| 202 | IS_LNK_PCB_92 | STRING | 1 | — | PCB permission flag 92 for this link |
| 203 | IS_LNK_PCB_93 | STRING | 1 | — | PCB permission flag 93 for this link |
| 204 | IS_LNK_PCB_94 | STRING | 1 | — | PCB permission flag 94 for this link |
| 205 | IS_LNK_PCB_95 | STRING | 1 | — | PCB permission flag 95 for this link |
| 206 | IS_LNK_PCB_96 | STRING | 1 | — | PCB permission flag 96 for this link |
| 207 | IS_LNK_PCB_97 | STRING | 1 | — | PCB permission flag 97 for this link |
| 208 | IS_LNK_PCB_98 | STRING | 1 | — | PCB permission flag 98 for this link |
| 209 | IS_LNK_PCB_99 | STRING | 1 | — | PCB permission flag 99 for this link |
| 210 | IS_LNK_PRIVATE | STRING | 1 | — | Private (user-only) link flag (Y/N) |
| 211 | IS_LNK_TYPES_1 | STRING | 1 | — | Link type flag 1 |
| 212 | IS_LNK_TYPES_10 | STRING | 1 | — | Link type flag 10 |
| 213 | IS_LNK_TYPES_100 | STRING | 1 | — | Link type flag 100 |
| 214 | IS_LNK_TYPES_11 | STRING | 1 | — | Link type flag 11 |
| 215 | IS_LNK_TYPES_12 | STRING | 1 | — | Link type flag 12 |
| 216 | IS_LNK_TYPES_13 | STRING | 1 | — | Link type flag 13 |
| 217 | IS_LNK_TYPES_14 | STRING | 1 | — | Link type flag 14 |
| 218 | IS_LNK_TYPES_15 | STRING | 1 | — | Link type flag 15 |
| 219 | IS_LNK_TYPES_16 | STRING | 1 | — | Link type flag 16 |
| 220 | IS_LNK_TYPES_17 | STRING | 1 | — | Link type flag 17 |
| 221 | IS_LNK_TYPES_18 | STRING | 1 | — | Link type flag 18 |
| 222 | IS_LNK_TYPES_19 | STRING | 1 | — | Link type flag 19 |
| 223 | IS_LNK_TYPES_2 | STRING | 1 | — | Link type flag 2 |
| 224 | IS_LNK_TYPES_20 | STRING | 1 | — | Link type flag 20 |
| 225 | IS_LNK_TYPES_21 | STRING | 1 | — | Link type flag 21 |
| 226 | IS_LNK_TYPES_22 | STRING | 1 | — | Link type flag 22 |
| 227 | IS_LNK_TYPES_23 | STRING | 1 | — | Link type flag 23 |
| 228 | IS_LNK_TYPES_24 | STRING | 1 | — | Link type flag 24 |
| 229 | IS_LNK_TYPES_25 | STRING | 1 | — | Link type flag 25 |
| 230 | IS_LNK_TYPES_26 | STRING | 1 | — | Link type flag 26 |
| 231 | IS_LNK_TYPES_27 | STRING | 1 | — | Link type flag 27 |
| 232 | IS_LNK_TYPES_28 | STRING | 1 | — | Link type flag 28 |
| 233 | IS_LNK_TYPES_29 | STRING | 1 | — | Link type flag 29 |
| 234 | IS_LNK_TYPES_3 | STRING | 1 | — | Link type flag 3 |
| 235 | IS_LNK_TYPES_30 | STRING | 1 | — | Link type flag 30 |
| 236 | IS_LNK_TYPES_31 | STRING | 1 | — | Link type flag 31 |
| 237 | IS_LNK_TYPES_32 | STRING | 1 | — | Link type flag 32 |
| 238 | IS_LNK_TYPES_33 | STRING | 1 | — | Link type flag 33 |
| 239 | IS_LNK_TYPES_34 | STRING | 1 | — | Link type flag 34 |
| 240 | IS_LNK_TYPES_35 | STRING | 1 | — | Link type flag 35 |
| 241 | IS_LNK_TYPES_36 | STRING | 1 | — | Link type flag 36 |
| 242 | IS_LNK_TYPES_37 | STRING | 1 | — | Link type flag 37 |
| 243 | IS_LNK_TYPES_38 | STRING | 1 | — | Link type flag 38 |
| 244 | IS_LNK_TYPES_39 | STRING | 1 | — | Link type flag 39 |
| 245 | IS_LNK_TYPES_4 | STRING | 1 | — | Link type flag 4 |
| 246 | IS_LNK_TYPES_40 | STRING | 1 | — | Link type flag 40 |
| 247 | IS_LNK_TYPES_41 | STRING | 1 | — | Link type flag 41 |
| 248 | IS_LNK_TYPES_42 | STRING | 1 | — | Link type flag 42 |
| 249 | IS_LNK_TYPES_43 | STRING | 1 | — | Link type flag 43 |
| 250 | IS_LNK_TYPES_44 | STRING | 1 | — | Link type flag 44 |
| 251 | IS_LNK_TYPES_45 | STRING | 1 | — | Link type flag 45 |
| 252 | IS_LNK_TYPES_46 | STRING | 1 | — | Link type flag 46 |
| 253 | IS_LNK_TYPES_47 | STRING | 1 | — | Link type flag 47 |
| 254 | IS_LNK_TYPES_48 | STRING | 1 | — | Link type flag 48 |
| 255 | IS_LNK_TYPES_49 | STRING | 1 | — | Link type flag 49 |
| 256 | IS_LNK_TYPES_5 | STRING | 1 | — | Link type flag 5 |
| 257 | IS_LNK_TYPES_50 | STRING | 1 | — | Link type flag 50 |
| 258 | IS_LNK_TYPES_51 | STRING | 1 | — | Link type flag 51 |
| 259 | IS_LNK_TYPES_52 | STRING | 1 | — | Link type flag 52 |
| 260 | IS_LNK_TYPES_53 | STRING | 1 | — | Link type flag 53 |
| 261 | IS_LNK_TYPES_54 | STRING | 1 | — | Link type flag 54 |
| 262 | IS_LNK_TYPES_55 | STRING | 1 | — | Link type flag 55 |
| 263 | IS_LNK_TYPES_56 | STRING | 1 | — | Link type flag 56 |
| 264 | IS_LNK_TYPES_57 | STRING | 1 | — | Link type flag 57 |
| 265 | IS_LNK_TYPES_58 | STRING | 1 | — | Link type flag 58 |
| 266 | IS_LNK_TYPES_59 | STRING | 1 | — | Link type flag 59 |
| 267 | IS_LNK_TYPES_6 | STRING | 1 | — | Link type flag 6 |
| 268 | IS_LNK_TYPES_60 | STRING | 1 | — | Link type flag 60 |
| 269 | IS_LNK_TYPES_61 | STRING | 1 | — | Link type flag 61 |
| 270 | IS_LNK_TYPES_62 | STRING | 1 | — | Link type flag 62 |
| 271 | IS_LNK_TYPES_63 | STRING | 1 | — | Link type flag 63 |
| 272 | IS_LNK_TYPES_64 | STRING | 1 | — | Link type flag 64 |
| 273 | IS_LNK_TYPES_65 | STRING | 1 | — | Link type flag 65 |
| 274 | IS_LNK_TYPES_66 | STRING | 1 | — | Link type flag 66 |
| 275 | IS_LNK_TYPES_67 | STRING | 1 | — | Link type flag 67 |
| 276 | IS_LNK_TYPES_68 | STRING | 1 | — | Link type flag 68 |
| 277 | IS_LNK_TYPES_69 | STRING | 1 | — | Link type flag 69 |
| 278 | IS_LNK_TYPES_7 | STRING | 1 | — | Link type flag 7 |
| 279 | IS_LNK_TYPES_70 | STRING | 1 | — | Link type flag 70 |
| 280 | IS_LNK_TYPES_71 | STRING | 1 | — | Link type flag 71 |
| 281 | IS_LNK_TYPES_72 | STRING | 1 | — | Link type flag 72 |
| 282 | IS_LNK_TYPES_73 | STRING | 1 | — | Link type flag 73 |
| 283 | IS_LNK_TYPES_74 | STRING | 1 | — | Link type flag 74 |
| 284 | IS_LNK_TYPES_75 | STRING | 1 | — | Link type flag 75 |
| 285 | IS_LNK_TYPES_76 | STRING | 1 | — | Link type flag 76 |
| 286 | IS_LNK_TYPES_77 | STRING | 1 | — | Link type flag 77 |
| 287 | IS_LNK_TYPES_78 | STRING | 1 | — | Link type flag 78 |
| 288 | IS_LNK_TYPES_79 | STRING | 1 | — | Link type flag 79 |
| 289 | IS_LNK_TYPES_8 | STRING | 1 | — | Link type flag 8 |
| 290 | IS_LNK_TYPES_80 | STRING | 1 | — | Link type flag 80 |
| 291 | IS_LNK_TYPES_81 | STRING | 1 | — | Link type flag 81 |
| 292 | IS_LNK_TYPES_82 | STRING | 1 | — | Link type flag 82 |
| 293 | IS_LNK_TYPES_83 | STRING | 1 | — | Link type flag 83 |
| 294 | IS_LNK_TYPES_84 | STRING | 1 | — | Link type flag 84 |
| 295 | IS_LNK_TYPES_85 | STRING | 1 | — | Link type flag 85 |
| 296 | IS_LNK_TYPES_86 | STRING | 1 | — | Link type flag 86 |
| 297 | IS_LNK_TYPES_87 | STRING | 1 | — | Link type flag 87 |
| 298 | IS_LNK_TYPES_88 | STRING | 1 | — | Link type flag 88 |
| 299 | IS_LNK_TYPES_89 | STRING | 1 | — | Link type flag 89 |
| 300 | IS_LNK_TYPES_9 | STRING | 1 | — | Link type flag 9 |
| 301 | IS_LNK_TYPES_90 | STRING | 1 | — | Link type flag 90 |
| 302 | IS_LNK_TYPES_91 | STRING | 1 | — | Link type flag 91 |
| 303 | IS_LNK_TYPES_92 | STRING | 1 | — | Link type flag 92 |
| 304 | IS_LNK_TYPES_93 | STRING | 1 | — | Link type flag 93 |
| 305 | IS_LNK_TYPES_94 | STRING | 1 | — | Link type flag 94 |
| 306 | IS_LNK_TYPES_95 | STRING | 1 | — | Link type flag 95 |
| 307 | IS_LNK_TYPES_96 | STRING | 1 | — | Link type flag 96 |
| 308 | IS_LNK_TYPES_97 | STRING | 1 | — | Link type flag 97 |
| 309 | IS_LNK_TYPES_98 | STRING | 1 | — | Link type flag 98 |
| 310 | IS_LNK_TYPES_99 | STRING | 1 | — | Link type flag 99 |
| 311 | IS_LNK_UID | STRING | 48 | — | Unique identifier of the parent record |
| 312 | IS_LNK_WHO | STRING | 15 | — | User who created or owns this link |

## ISLOG
**ACTIVE USER LIST**

Fields: 9

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_LOG_COMPANY | STRING | 3 | — | Company ID for this log entry |
| 2 | IS_LOG_DOING | STRING | 60 | — | Description of current operation |
| 3 | IS_LOG_EXTRA | STRING | 100 | — | Reserved extra field |
| 4 | IS_LOG_KILL | STRING | 1 | — | Kill/abort flag for running process |
| 5 | IS_LOG_MSG | STRING | 200 | — | Log message text |
| 6 | IS_LOG_STARTD | DATE | 4 | — | Process start date |
| 7 | IS_LOG_STARTT | STRING | 12 | — | Process start time |
| 8 | IS_LOG_WHAT | STRING | 15 | — | Program name being logged |
| 9 | IS_LOG_WHO | STRING | 35 | — | User running the process |

## ISNOTES
**EVO NOTES**

Fields: 14

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_NOTE_ALPHA | STRING | 6000 | — | Full text/blob content for this note |
| 2 | IS_NOTE_CDATE | DATE | 4 | — | Note creation date |
| 3 | IS_NOTE_CONTACT | STRING | 30 | — | Contact name associated with note |
| 4 | IS_NOTE_CTIME | STRING | 10 | — | Note creation time (HH:MM:SS) |
| 5 | IS_NOTE_CWHO | STRING | 15 | — | User who created the note |
| 6 | IS_NOTE_EDATE | DATE | 4 | — | Note last-edited date |
| 7 | IS_NOTE_ETIME | STRING | 10 | — | Note last-edited time (HH:MM:SS) |
| 8 | IS_NOTE_EWHO | STRING | 15 | — | User who last edited the note |
| 9 | IS_NOTE_EXTRA | STRING | 100 | — | Reserved extra field |
| 10 | IS_NOTE_GROUP | STRING | 4 | — | Note category/group code |
| 11 | IS_NOTE_ID | STRING | 48 | — | Unique identifier of the parent record |
| 12 | IS_NOTE_NOTE | STRING | 0 | — | Memo/blob note body |
| 13 | IS_NOTE_PRIVATE | STRING | 1 | — | Private note flag (Y/N) |
| 14 | IS_NOTE_TYPE | STRING | 3 | — | Note type code |

## ISNTYPE
**EVO NOTE TYPES**

Fields: 4

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_NT_DESC | STRING | 30 | — | Note type description |
| 2 | IS_NT_EXTRA | STRING | 100 | — | Reserved extra field |
| 3 | IS_NT_SEC | INTEGER | 2 | — | Security level for this note type |
| 4 | IS_NT_TYPE | STRING | 3 | — | Note type code |

## ISNUMBER
**DOCUMENT COUNTERS**

Fields: 52

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_NUM_CODE | STRING | 10 | — | Sequence name/code |
| 2 | IS_NUM_EXTRA | STRING | 100 | — | Reserved extra field |
| 3 | IS_NUM_NEXT_1 | NUMERIC | 8 | — | Next auto-number value for sequence 1 |
| 4 | IS_NUM_NEXT_10 | NUMERIC | 8 | — | Next auto-number value for sequence 10 |
| 5 | IS_NUM_NEXT_11 | NUMERIC | 8 | — | Next auto-number value for sequence 11 |
| 6 | IS_NUM_NEXT_12 | NUMERIC | 8 | — | Next auto-number value for sequence 12 |
| 7 | IS_NUM_NEXT_13 | NUMERIC | 8 | — | Next auto-number value for sequence 13 |
| 8 | IS_NUM_NEXT_14 | NUMERIC | 8 | — | Next auto-number value for sequence 14 |
| 9 | IS_NUM_NEXT_15 | NUMERIC | 8 | — | Next auto-number value for sequence 15 |
| 10 | IS_NUM_NEXT_16 | NUMERIC | 8 | — | Next auto-number value for sequence 16 |
| 11 | IS_NUM_NEXT_17 | NUMERIC | 8 | — | Next auto-number value for sequence 17 |
| 12 | IS_NUM_NEXT_18 | NUMERIC | 8 | — | Next auto-number value for sequence 18 |
| 13 | IS_NUM_NEXT_19 | NUMERIC | 8 | — | Next auto-number value for sequence 19 |
| 14 | IS_NUM_NEXT_2 | NUMERIC | 8 | — | Next auto-number value for sequence 2 |
| 15 | IS_NUM_NEXT_20 | NUMERIC | 8 | — | Next auto-number value for sequence 20 |
| 16 | IS_NUM_NEXT_21 | NUMERIC | 8 | — | Next auto-number value for sequence 21 |
| 17 | IS_NUM_NEXT_22 | NUMERIC | 8 | — | Next auto-number value for sequence 22 |
| 18 | IS_NUM_NEXT_23 | NUMERIC | 8 | — | Next auto-number value for sequence 23 |
| 19 | IS_NUM_NEXT_24 | NUMERIC | 8 | — | Next auto-number value for sequence 24 |
| 20 | IS_NUM_NEXT_25 | NUMERIC | 8 | — | Next auto-number value for sequence 25 |
| 21 | IS_NUM_NEXT_26 | NUMERIC | 8 | — | Next auto-number value for sequence 26 |
| 22 | IS_NUM_NEXT_27 | NUMERIC | 8 | — | Next auto-number value for sequence 27 |
| 23 | IS_NUM_NEXT_28 | NUMERIC | 8 | — | Next auto-number value for sequence 28 |
| 24 | IS_NUM_NEXT_29 | NUMERIC | 8 | — | Next auto-number value for sequence 29 |
| 25 | IS_NUM_NEXT_3 | NUMERIC | 8 | — | Next auto-number value for sequence 3 |
| 26 | IS_NUM_NEXT_30 | NUMERIC | 8 | — | Next auto-number value for sequence 30 |
| 27 | IS_NUM_NEXT_31 | NUMERIC | 8 | — | Next auto-number value for sequence 31 |
| 28 | IS_NUM_NEXT_32 | NUMERIC | 8 | — | Next auto-number value for sequence 32 |
| 29 | IS_NUM_NEXT_33 | NUMERIC | 8 | — | Next auto-number value for sequence 33 |
| 30 | IS_NUM_NEXT_34 | NUMERIC | 8 | — | Next auto-number value for sequence 34 |
| 31 | IS_NUM_NEXT_35 | NUMERIC | 8 | — | Next auto-number value for sequence 35 |
| 32 | IS_NUM_NEXT_36 | NUMERIC | 8 | — | Next auto-number value for sequence 36 |
| 33 | IS_NUM_NEXT_37 | NUMERIC | 8 | — | Next auto-number value for sequence 37 |
| 34 | IS_NUM_NEXT_38 | NUMERIC | 8 | — | Next auto-number value for sequence 38 |
| 35 | IS_NUM_NEXT_39 | NUMERIC | 8 | — | Next auto-number value for sequence 39 |
| 36 | IS_NUM_NEXT_4 | NUMERIC | 8 | — | Next auto-number value for sequence 4 |
| 37 | IS_NUM_NEXT_40 | NUMERIC | 8 | — | Next auto-number value for sequence 40 |
| 38 | IS_NUM_NEXT_41 | NUMERIC | 8 | — | Next auto-number value for sequence 41 |
| 39 | IS_NUM_NEXT_42 | NUMERIC | 8 | — | Next auto-number value for sequence 42 |
| 40 | IS_NUM_NEXT_43 | NUMERIC | 8 | — | Next auto-number value for sequence 43 |
| 41 | IS_NUM_NEXT_44 | NUMERIC | 8 | — | Next auto-number value for sequence 44 |
| 42 | IS_NUM_NEXT_45 | NUMERIC | 8 | — | Next auto-number value for sequence 45 |
| 43 | IS_NUM_NEXT_46 | NUMERIC | 8 | — | Next auto-number value for sequence 46 |
| 44 | IS_NUM_NEXT_47 | NUMERIC | 8 | — | Next auto-number value for sequence 47 |
| 45 | IS_NUM_NEXT_48 | NUMERIC | 8 | — | Next auto-number value for sequence 48 |
| 46 | IS_NUM_NEXT_49 | NUMERIC | 8 | — | Next auto-number value for sequence 49 |
| 47 | IS_NUM_NEXT_5 | NUMERIC | 8 | — | Next auto-number value for sequence 5 |
| 48 | IS_NUM_NEXT_50 | NUMERIC | 8 | — | Next auto-number value for sequence 50 |
| 49 | IS_NUM_NEXT_6 | NUMERIC | 8 | — | Next auto-number value for sequence 6 |
| 50 | IS_NUM_NEXT_7 | NUMERIC | 8 | — | Next auto-number value for sequence 7 |
| 51 | IS_NUM_NEXT_8 | NUMERIC | 8 | — | Next auto-number value for sequence 8 |
| 52 | IS_NUM_NEXT_9 | NUMERIC | 8 | — | Next auto-number value for sequence 9 |

## ISREMIND
**EVO REMINDERS**

Fields: 24

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_REM_BEFTXT | STRING | 15 | — | Before-due reminder text label |
| 2 | IS_REM_CO | STRING | 3 | — | Company ID for this reminder |
| 3 | IS_REM_COUNTER | INTEGER | 4 | — | Reminder recurrence counter |
| 4 | IS_REM_CUST | STRING | 10 | — | Customer code linked to reminder |
| 5 | IS_REM_DATE | DATE | 4 | — | Reminder due date |
| 6 | IS_REM_DISP | STRING | 1 | — | Display on dashboard flag (Y/N) |
| 7 | IS_REM_EDATE | DATE | 4 | — | Reminder expiry date |
| 8 | IS_REM_EMAIL | STRING | 400 | — | Email address(es) for reminder notification |
| 9 | IS_REM_ENDDT | DATE | 4 | — | Reminder end date (for recurring) |
| 10 | IS_REM_ENDTM | TIME | 4 | — | Reminder end time |
| 11 | IS_REM_ETIME | TIME | 4 | — | Event/appointment end time |
| 12 | IS_REM_EXTRA | STRING | 50 | — | Reserved extra field |
| 13 | IS_REM_FILE | STRING | 256 | — | File attachment path for reminder |
| 14 | IS_REM_ITEM | STRING | 15 | — | Item/part number linked to reminder |
| 15 | IS_REM_MEMO | STRING | 0 | — | Memo/blob body for reminder |
| 16 | IS_REM_NOTE | STRING | 6000 | — | Full text note for reminder |
| 17 | IS_REM_NOTIFY | STRING | 1 | — | Send notification flag (Y/N) |
| 18 | IS_REM_SENT | STRING | 25 | — | Notification sent-to address |
| 19 | IS_REM_SUBJECT | STRING | 100 | — | Reminder subject line |
| 20 | IS_REM_TIME | TIME | 4 | — | Reminder trigger time |
| 21 | IS_REM_TRANS | STRING | 1 | — | Transaction-linked flag (Y/N) |
| 22 | IS_REM_TYPE | STRING | 3 | — | Reminder type code |
| 23 | IS_REM_VEND | STRING | 10 | — | Vendor code linked to reminder |
| 24 | IS_REM_WHO | STRING | 20 | — | User who owns/created this reminder |

## ISSCHED
**LIST OF PROGRAMS TO RUN BY EVO SCHEDULER**

Fields: 24

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_SCHED_CO | STRING | 3 | — | Company ID for this scheduled task |
| 2 | IS_SCHED_DATE | DATE | 4 | — | Next scheduled run date |
| 3 | IS_SCHED_DESC | STRING | 256 | — | Scheduled task description |
| 4 | IS_SCHED_EMAIL | STRING | 128 | — | Email address for task completion notification |
| 5 | IS_SCHED_EXTRA | STRING | 100 | — | Reserved extra field |
| 6 | IS_SCHED_LDATE | DATE | 4 | — | Last run date |
| 7 | IS_SCHED_LOG | STRING | 256 | — | Last run log output |
| 8 | IS_SCHED_LTIME | TIME | 4 | — | Last run time |
| 9 | IS_SCHED_NAME | STRING | 50 | — | Scheduled task name |
| 10 | IS_SCHED_PARAM0 | STRING | 256 | — | Scheduled event parameter 0 |
| 11 | IS_SCHED_PARAM1 | STRING | 256 | — | Scheduled event parameter 1 |
| 12 | IS_SCHED_PARAM2 | STRING | 256 | — | Scheduled event parameter 2 |
| 13 | IS_SCHED_PARAM3 | STRING | 256 | — | Scheduled event parameter 3 |
| 14 | IS_SCHED_PARAM4 | STRING | 256 | — | Scheduled event parameter 4 |
| 15 | IS_SCHED_PARAM5 | STRING | 256 | — | Scheduled event parameter 5 |
| 16 | IS_SCHED_PARAM6 | STRING | 256 | — | Scheduled event parameter 6 |
| 17 | IS_SCHED_PARAM7 | STRING | 256 | — | Scheduled event parameter 7 |
| 18 | IS_SCHED_PARAM8 | STRING | 256 | — | Scheduled event parameter 8 |
| 19 | IS_SCHED_PARAM9 | STRING | 256 | — | Scheduled event parameter 9 |
| 20 | IS_SCHED_PROG | STRING | 256 | — | Program or script to run |
| 21 | IS_SCHED_RECUR | NUMERIC | 8 | — | Recurrence interval (days) |
| 22 | IS_SCHED_TIME | TIME | 4 | — | Scheduled run time |
| 23 | IS_SCHED_TYPE | STRING | 1 | — | Schedule type (D=Daily, W=Weekly, M=Monthly) |
| 24 | IS_SCHED_WHO | STRING | 15 | — | User who owns or created this schedule |

## ISSHIPCO
**SHIP VIA COMPANY**

Fields: 16

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_SHIP_EXTRA | STRING | 150 | — | Reserved extra field |
| 2 | IS_SHIP_NOTES_1 | STRING | 60 | — | Shipping company notes line 1 |
| 3 | IS_SHIP_NOTES_2 | STRING | 60 | — | Shipping company notes line 2 |
| 4 | IS_SHIP_NOTES_3 | STRING | 60 | — | Shipping company notes line 3 |
| 5 | IS_SHIP_NOTES_4 | STRING | 60 | — | Shipping company notes line 4 |
| 6 | IS_SHIP_NOTES_5 | STRING | 60 | — | Shipping company notes line 5 |
| 7 | IS_SHIP_SHIPVIA | STRING | 15 | — | Shipping carrier/ship-via code |
| 8 | IS_SHIP_SHPCOD | STRING | 10 | — | Shipping company code |
| 9 | IS_SHIP_SHPDESC | STRING | 60 | — | Shipping company description |
| 10 | IS_SHIP_SHPNME | STRING | 30 | — | Shipping company name |
| 11 | IS_SHIP_VNDCOD | STRING | 10 | — | Linked vendor code for this shipper |
| 12 | IS_SHIP_WEB_1 | STRING | 120 | — | Shipping company web tracking URL template 1 |
| 13 | IS_SHIP_WEB_2 | STRING | 120 | — | Shipping company web tracking URL template 2 |
| 14 | IS_SHIP_WEB_3 | STRING | 120 | — | Shipping company web tracking URL template 3 |
| 15 | IS_SHIP_WEB_4 | STRING | 120 | — | Shipping company web tracking URL template 4 |
| 16 | IS_SHIP_WEB_5 | STRING | 120 | — | Shipping company web tracking URL template 5 |

## ISSHPVIA
**SHIP VIA LISTING**

Fields: 23

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_SHPVIA_ACCT | STRING | 25 | — | Carrier account number |
| 2 | IS_SHPVIA_ALPH1 | STRING | 15 | — | Alpha sort key 1 |
| 3 | IS_SHPVIA_ALPH2 | STRING | 15 | — | Alpha sort key 2 |
| 4 | IS_SHPVIA_CNTCT | STRING | 25 | — | Carrier contact name |
| 5 | IS_SHPVIA_CODE | STRING | 15 | — | Ship-via carrier code |
| 6 | IS_SHPVIA_CUST | STRING | 10 | — | Default customer code for this carrier |
| 7 | IS_SHPVIA_DATE | DATE | 4 | — | Record date |
| 8 | IS_SHPVIA_EXTRA | STRING | 100 | — | Reserved extra field |
| 9 | IS_SHPVIA_FLAG | STRING | 1 | — | Carrier status/active flag |
| 10 | IS_SHPVIA_NOTES_1 | STRING | 60 | — | Ship-via carrier notes line 1 |
| 11 | IS_SHPVIA_NOTES_10 | STRING | 60 | — | Ship-via carrier notes line 10 |
| 12 | IS_SHPVIA_NOTES_2 | STRING | 60 | — | Ship-via carrier notes line 2 |
| 13 | IS_SHPVIA_NOTES_3 | STRING | 60 | — | Ship-via carrier notes line 3 |
| 14 | IS_SHPVIA_NOTES_4 | STRING | 60 | — | Ship-via carrier notes line 4 |
| 15 | IS_SHPVIA_NOTES_5 | STRING | 60 | — | Ship-via carrier notes line 5 |
| 16 | IS_SHPVIA_NOTES_6 | STRING | 60 | — | Ship-via carrier notes line 6 |
| 17 | IS_SHPVIA_NOTES_7 | STRING | 60 | — | Ship-via carrier notes line 7 |
| 18 | IS_SHPVIA_NOTES_8 | STRING | 60 | — | Ship-via carrier notes line 8 |
| 19 | IS_SHPVIA_NOTES_9 | STRING | 60 | — | Ship-via carrier notes line 9 |
| 20 | IS_SHPVIA_OBS | STRING | 1 | — | Obsolete/inactive flag (Y/N) |
| 21 | IS_SHPVIA_PHONE | STRING | 25 | — | Carrier phone number |
| 22 | IS_SHPVIA_PRTY | INTEGER | 2 | — | Carrier sort priority |
| 23 | IS_SHPVIA_VEND | STRING | 10 | — | Linked vendor code for this carrier |

## ISTERMS
**PAYMENT TERMS FOR GRID**

Fields: 13

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_TERMS_AMT | NUMERIC | 8 | 2 | Minimum invoice amount for terms |
| 2 | IS_TERMS_ARAP | STRING | 1 | — | Terms applicability flag (A=AR, P=AP, B=Both) |
| 3 | IS_TERMS_CC | STRING | 1 | — | Credit card terms flag (Y/N) |
| 4 | IS_TERMS_COD | STRING | 1 | — | Cash-on-delivery flag (Y/N) |
| 5 | IS_TERMS_DAY | INTEGER | 2 | — | Net due days |
| 6 | IS_TERMS_DESC | STRING | 50 | — | Terms description |
| 7 | IS_TERMS_EOM | STRING | 1 | — | End-of-month terms flag (Y/N) |
| 8 | IS_TERMS_EXTRA | STRING | 100 | — | Reserved extra field |
| 9 | IS_TERMS_MAX | INTEGER | 2 | — | Discount cutoff days |
| 10 | IS_TERMS_NAME | STRING | 20 | — | Payment terms name/code |
| 11 | IS_TERMS_NUM | INTEGER | 2 | — | Terms sequence number |
| 12 | IS_TERMS_SRT | INTEGER | 2 | — | Sort order |
| 13 | IS_TERMS_TYP | STRING | 1 | — | Terms type code (N=Net, D=Discount) |

## ISTRIGRS
**TRIGGERS**

Fields: 26

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_TRIG_CAT | STRING | 4 | — | Trigger category code |
| 2 | IS_TRIG_CLASS | STRING | 4 | — | Trigger class code |
| 3 | IS_TRIG_CODE | STRING | 15 | — | Trigger event code |
| 4 | IS_TRIG_CONTACT | STRING | 20 | — | Contact name for notification |
| 5 | IS_TRIG_CUST | STRING | 10 | — | Customer code linked to trigger |
| 6 | IS_TRIG_DAYS | INTEGER | 2 | — | Days offset for trigger timing |
| 7 | IS_TRIG_EFLAG | STRING | 1 | — | Email notification flag (Y/N) |
| 8 | IS_TRIG_EMAIL | STRING | 400 | — | Email address(es) for trigger notification |
| 9 | IS_TRIG_EXTRA | STRING | 100 | — | Reserved extra field |
| 10 | IS_TRIG_ITYPE | STRING | 10 | — | Item type filter for trigger |
| 11 | IS_TRIG_LDATE | DATE | 4 | — | Last trigger fire date |
| 12 | IS_TRIG_LOC | STRING | 10 | — | Location code filter for trigger |
| 13 | IS_TRIG_LTIME | TIME | 4 | — | Last trigger fire time |
| 14 | IS_TRIG_NOTE | STRING | 6000 | — | Trigger notes/memo |
| 15 | IS_TRIG_ODEL | STRING | 1 | — | On-delete trigger flag (Y/N) |
| 16 | IS_TRIG_ONCE | STRING | 1 | — | Fire once only flag (Y/N) |
| 17 | IS_TRIG_OPER | STRING | 3 | — | Operator code who owns trigger |
| 18 | IS_TRIG_PLANNER | STRING | 4 | — | Planner code filter |
| 19 | IS_TRIG_PO | NUMERIC | 8 | — | Purchase order number linked to trigger |
| 20 | IS_TRIG_SO | NUMERIC | 8 | — | Sales order number linked to trigger |
| 21 | IS_TRIG_TRIGR | STRING | 10 | — | Trigger rule code |
| 22 | IS_TRIG_VEND | STRING | 10 | — | Vendor code linked to trigger |
| 23 | IS_TRIG_WOPRE | NUMERIC | 8 | — | Work order prefix number linked to trigger |
| 24 | IS_TRIG_WOPRET | NUMERIC | 8 | — | Work order prefix type linked to trigger |
| 25 | IS_TRIG_WOSUF | INTEGER | 2 | — | Work order suffix number linked to trigger |
| 26 | IS_TRIG_WOSUFT | INTEGER | 2 | — | Work order suffix type linked to trigger |

## LANGDICT
**TRANSLATION MASTER**

Fields: 5

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | LANG_DICT_ECAPT | STRING | 80 | — | English (base) caption text |
| 2 | LANG_DICT_EXTRA | STRING | 150 | — | Reserved extra field |
| 3 | LANG_DICT_FONT | STRING | 30 | — | Font override for translated caption |
| 4 | LANG_DICT_LANG | STRING | 3 | — | Language code (ISO 3-letter) |
| 5 | LANG_DICT_LCAPT | STRING | 80 | — | Localized caption text in target language |

## MKAHIST
**SYSTEM DEFAULT MASTER FILE 3**

Fields: 9

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MKAHIST_ACCT | STRING | 10 | — | Account code for this marketing history entry |
| 2 | MKAHIST_DATE | DATE | 4 | — | Date of marketing activity |
| 3 | MKAHIST_EVENT | NUMERIC | 8 | — | Marketing event/activity code |
| 4 | MKAHIST_FORM | NUMERIC | 8 | — | Form/document number associated with activity |
| 5 | MKAHIST_MEDIA | STRING | 1 | — | Media type code for this activity |
| 6 | MKAHIST_REM1 | STRING | 60 | — | Remark line 1 |
| 7 | MKAHIST_REM2 | STRING | 60 | — | Remark line 2 |
| 8 | MKAHIST_SEQ | INTEGER | 2 | — | Sequence number within event |
| 9 | MKAHIST_TRACK | NUMERIC | 8 | — | Tracking number for this marketing activity |
