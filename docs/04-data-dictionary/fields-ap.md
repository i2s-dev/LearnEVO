# AP — Accounts Payable: Field Reference

Status: verified-schema

Source: `Evo-DBA_File_Fields 052421.xlsx`, sheet "Fields".
Field descriptions where provided by source; otherwise name-inferred.

---

## BKAPADSC
**ARCHIVED DBA VENDOR & PO NOTES**

Fields: 5

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BK_DESC_CODE | STRING | 15 | — | not used |
| 2 | BK_DESC_DESC | STRING | 25 | — | not used |
| 3 | BK_DESC_LINE | INTEGER | 2 | — | Notes line number |
| 4 | BK_DESC_NOTES | STRING | 70 | — | Notes - text |
| 5 | BK_DESC_NUM | NUMERIC | 8 | — | PO Number |

## BKAPCHKF
**PRO-FORMA CHECK REGITER**

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

## BKAPCHKH
**AP PAYMENT HISTORY**

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

## BKAPDEP
**AP DEPOSIT**

Fields: 6

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAR_DEP_CUST | STRING | 10 | — | Customer Code |
| 2 | BKAR_DEP_DATE | DATE | 4 | — | Deposit Date |
| 3 | BKAR_DEP_DEPNO | NUMERIC | 8 | — | Deposit Number |
| 4 | BKAR_DEP_EXTRA | STRING | 50 | — | Extra data field |
| 5 | BKAR_DEP_SO | NUMERIC | 8 | — | SO Number |
| 6 | BKAR_DEP_SR | STRING | 1 | — | Sales receipt flag Y/N |

## BKAPDESC
**VENDOR WEBSITE & DBA VENDOR & PO NOTES**

Fields: 5

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BK_DESC_CODE | STRING | 15 | — | not used |
| 2 | BK_DESC_DESC | STRING | 25 | — | not used |
| 3 | BK_DESC_LINE | INTEGER | 2 | — | Notes line number |
| 4 | BK_DESC_NOTES | STRING | 70 | — | Notes - text |
| 5 | BK_DESC_NUM | NUMERIC | 8 | — | PO Number |

## BKAPINVL
**AP VOUCHER**

Fields: 390

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAP_INVL_APDPT | STRING | 4 | — | Recurring Invoice |
| 2 | BKAP_INVL_CHK | INTEGER | 2 | — | Manual Check Number |
| 3 | BKAP_INVL_CODE | STRING | 10 | — | Vendor Code |
| 4 | BKAP_INVL_DAMT_1 | NUMERIC | 8 | 2 | GL distribution amount for line 1 |
| 5 | BKAP_INVL_DAMT_10 | NUMERIC | 8 | 2 | GL distribution amount for line 10 |
| 6 | BKAP_INVL_DAMT_11 | NUMERIC | 8 | 2 | GL distribution amount for line 11 |
| 7 | BKAP_INVL_DAMT_12 | NUMERIC | 8 | 2 | GL distribution amount for line 12 |
| 8 | BKAP_INVL_DAMT_13 | NUMERIC | 8 | 2 | GL distribution amount for line 13 |
| 9 | BKAP_INVL_DAMT_14 | NUMERIC | 8 | 2 | GL distribution amount for line 14 |
| 10 | BKAP_INVL_DAMT_15 | NUMERIC | 8 | 2 | GL distribution amount for line 15 |
| 11 | BKAP_INVL_DAMT_16 | NUMERIC | 8 | 2 | GL distribution amount for line 16 |
| 12 | BKAP_INVL_DAMT_17 | NUMERIC | 8 | 2 | GL distribution amount for line 17 |
| 13 | BKAP_INVL_DAMT_18 | NUMERIC | 8 | 2 | GL distribution amount for line 18 |
| 14 | BKAP_INVL_DAMT_19 | NUMERIC | 8 | 2 | GL distribution amount for line 19 |
| 15 | BKAP_INVL_DAMT_2 | NUMERIC | 8 | 2 | GL distribution amount for line 2 |
| 16 | BKAP_INVL_DAMT_20 | NUMERIC | 8 | 2 | GL distribution amount for line 20 |
| 17 | BKAP_INVL_DAMT_21 | NUMERIC | 8 | 2 | GL distribution amount for line 21 |
| 18 | BKAP_INVL_DAMT_22 | NUMERIC | 8 | 2 | GL distribution amount for line 22 |
| 19 | BKAP_INVL_DAMT_23 | NUMERIC | 8 | 2 | GL distribution amount for line 23 |
| 20 | BKAP_INVL_DAMT_24 | NUMERIC | 8 | 2 | GL distribution amount for line 24 |
| 21 | BKAP_INVL_DAMT_25 | NUMERIC | 8 | 2 | GL distribution amount for line 25 |
| 22 | BKAP_INVL_DAMT_26 | NUMERIC | 8 | 2 | GL distribution amount for line 26 |
| 23 | BKAP_INVL_DAMT_27 | NUMERIC | 8 | 2 | GL distribution amount for line 27 |
| 24 | BKAP_INVL_DAMT_28 | NUMERIC | 8 | 2 | GL distribution amount for line 28 |
| 25 | BKAP_INVL_DAMT_29 | NUMERIC | 8 | 2 | GL distribution amount for line 29 |
| 26 | BKAP_INVL_DAMT_3 | NUMERIC | 8 | 2 | GL distribution amount for line 3 |
| 27 | BKAP_INVL_DAMT_30 | NUMERIC | 8 | 2 | GL distribution amount for line 30 |
| 28 | BKAP_INVL_DAMT_31 | NUMERIC | 8 | 2 | GL distribution amount for line 31 |
| 29 | BKAP_INVL_DAMT_32 | NUMERIC | 8 | 2 | GL distribution amount for line 32 |
| 30 | BKAP_INVL_DAMT_33 | NUMERIC | 8 | 2 | GL distribution amount for line 33 |
| 31 | BKAP_INVL_DAMT_34 | NUMERIC | 8 | 2 | GL distribution amount for line 34 |
| 32 | BKAP_INVL_DAMT_35 | NUMERIC | 8 | 2 | GL distribution amount for line 35 |
| 33 | BKAP_INVL_DAMT_36 | NUMERIC | 8 | 2 | GL distribution amount for line 36 |
| 34 | BKAP_INVL_DAMT_37 | NUMERIC | 8 | 2 | GL distribution amount for line 37 |
| 35 | BKAP_INVL_DAMT_38 | NUMERIC | 8 | 2 | GL distribution amount for line 38 |
| 36 | BKAP_INVL_DAMT_39 | NUMERIC | 8 | 2 | GL distribution amount for line 39 |
| 37 | BKAP_INVL_DAMT_4 | NUMERIC | 8 | 2 | GL distribution amount for line 4 |
| 38 | BKAP_INVL_DAMT_40 | NUMERIC | 8 | 2 | GL distribution amount for line 40 |
| 39 | BKAP_INVL_DAMT_41 | NUMERIC | 8 | 2 | GL distribution amount for line 41 |
| 40 | BKAP_INVL_DAMT_42 | NUMERIC | 8 | 2 | GL distribution amount for line 42 |
| 41 | BKAP_INVL_DAMT_43 | NUMERIC | 8 | 2 | GL distribution amount for line 43 |
| 42 | BKAP_INVL_DAMT_44 | NUMERIC | 8 | 2 | GL distribution amount for line 44 |
| 43 | BKAP_INVL_DAMT_45 | NUMERIC | 8 | 2 | GL distribution amount for line 45 |
| 44 | BKAP_INVL_DAMT_46 | NUMERIC | 8 | 2 | GL distribution amount for line 46 |
| 45 | BKAP_INVL_DAMT_47 | NUMERIC | 8 | 2 | GL distribution amount for line 47 |
| 46 | BKAP_INVL_DAMT_48 | NUMERIC | 8 | 2 | GL distribution amount for line 48 |
| 47 | BKAP_INVL_DAMT_49 | NUMERIC | 8 | 2 | GL distribution amount for line 49 |
| 48 | BKAP_INVL_DAMT_5 | NUMERIC | 8 | 2 | GL distribution amount for line 5 |
| 49 | BKAP_INVL_DAMT_50 | NUMERIC | 8 | 2 | GL distribution amount for line 50 |
| 50 | BKAP_INVL_DAMT_51 | NUMERIC | 8 | 2 | GL distribution amount for line 51 |
| 51 | BKAP_INVL_DAMT_52 | NUMERIC | 8 | 2 | GL distribution amount for line 52 |
| 52 | BKAP_INVL_DAMT_53 | NUMERIC | 8 | 2 | GL distribution amount for line 53 |
| 53 | BKAP_INVL_DAMT_54 | NUMERIC | 8 | 2 | GL distribution amount for line 54 |
| 54 | BKAP_INVL_DAMT_55 | NUMERIC | 8 | 2 | GL distribution amount for line 55 |
| 55 | BKAP_INVL_DAMT_56 | NUMERIC | 8 | 2 | GL distribution amount for line 56 |
| 56 | BKAP_INVL_DAMT_57 | NUMERIC | 8 | 2 | GL distribution amount for line 57 |
| 57 | BKAP_INVL_DAMT_58 | NUMERIC | 8 | 2 | GL distribution amount for line 58 |
| 58 | BKAP_INVL_DAMT_59 | NUMERIC | 8 | 2 | GL distribution amount for line 59 |
| 59 | BKAP_INVL_DAMT_6 | NUMERIC | 8 | 2 | GL distribution amount for line 6 |
| 60 | BKAP_INVL_DAMT_60 | NUMERIC | 8 | 2 | GL distribution amount for line 60 |
| 61 | BKAP_INVL_DAMT_61 | NUMERIC | 8 | 2 | GL distribution amount for line 61 |
| 62 | BKAP_INVL_DAMT_62 | NUMERIC | 8 | 2 | GL distribution amount for line 62 |
| 63 | BKAP_INVL_DAMT_63 | NUMERIC | 8 | 2 | GL distribution amount for line 63 |
| 64 | BKAP_INVL_DAMT_64 | NUMERIC | 8 | 2 | GL distribution amount for line 64 |
| 65 | BKAP_INVL_DAMT_65 | NUMERIC | 8 | 2 | GL distribution amount for line 65 |
| 66 | BKAP_INVL_DAMT_66 | NUMERIC | 8 | 2 | GL distribution amount for line 66 |
| 67 | BKAP_INVL_DAMT_67 | NUMERIC | 8 | 2 | GL distribution amount for line 67 |
| 68 | BKAP_INVL_DAMT_68 | NUMERIC | 8 | 2 | GL distribution amount for line 68 |
| 69 | BKAP_INVL_DAMT_69 | NUMERIC | 8 | 2 | GL distribution amount for line 69 |
| 70 | BKAP_INVL_DAMT_7 | NUMERIC | 8 | 2 | GL distribution amount for line 7 |
| 71 | BKAP_INVL_DAMT_70 | NUMERIC | 8 | 2 | GL distribution amount for line 70 |
| 72 | BKAP_INVL_DAMT_71 | NUMERIC | 8 | 2 | GL distribution amount for line 71 |
| 73 | BKAP_INVL_DAMT_72 | NUMERIC | 8 | 2 | GL distribution amount for line 72 |
| 74 | BKAP_INVL_DAMT_73 | NUMERIC | 8 | 2 | GL distribution amount for line 73 |
| 75 | BKAP_INVL_DAMT_74 | NUMERIC | 8 | 2 | GL distribution amount for line 74 |
| 76 | BKAP_INVL_DAMT_75 | NUMERIC | 8 | 2 | GL distribution amount for line 75 |
| 77 | BKAP_INVL_DAMT_8 | NUMERIC | 8 | 2 | GL distribution amount for line 8 |
| 78 | BKAP_INVL_DAMT_9 | NUMERIC | 8 | 2 | GL distribution amount for line 9 |
| 79 | BKAP_INVL_DATE | DATE | 4 | — | Invoice Date |
| 80 | BKAP_INVL_DC_1 | STRING | 1 | — | Debit/Credit flag for GL line 1 (D=Debit, C=Credit) |
| 81 | BKAP_INVL_DC_10 | STRING | 1 | — | Debit/Credit flag for GL line 10 (D=Debit, C=Credit) |
| 82 | BKAP_INVL_DC_11 | STRING | 1 | — | Debit/Credit flag for GL line 11 (D=Debit, C=Credit) |
| 83 | BKAP_INVL_DC_12 | STRING | 1 | — | Debit/Credit flag for GL line 12 (D=Debit, C=Credit) |
| 84 | BKAP_INVL_DC_13 | STRING | 1 | — | Debit/Credit flag for GL line 13 (D=Debit, C=Credit) |
| 85 | BKAP_INVL_DC_14 | STRING | 1 | — | Debit/Credit flag for GL line 14 (D=Debit, C=Credit) |
| 86 | BKAP_INVL_DC_15 | STRING | 1 | — | Debit/Credit flag for GL line 15 (D=Debit, C=Credit) |
| 87 | BKAP_INVL_DC_16 | STRING | 1 | — | Debit/Credit flag for GL line 16 (D=Debit, C=Credit) |
| 88 | BKAP_INVL_DC_17 | STRING | 1 | — | Debit/Credit flag for GL line 17 (D=Debit, C=Credit) |
| 89 | BKAP_INVL_DC_18 | STRING | 1 | — | Debit/Credit flag for GL line 18 (D=Debit, C=Credit) |
| 90 | BKAP_INVL_DC_19 | STRING | 1 | — | Debit/Credit flag for GL line 19 (D=Debit, C=Credit) |
| 91 | BKAP_INVL_DC_2 | STRING | 1 | — | Debit/Credit flag for GL line 2 (D=Debit, C=Credit) |
| 92 | BKAP_INVL_DC_20 | STRING | 1 | — | Debit/Credit flag for GL line 20 (D=Debit, C=Credit) |
| 93 | BKAP_INVL_DC_21 | STRING | 1 | — | Debit/Credit flag for GL line 21 (D=Debit, C=Credit) |
| 94 | BKAP_INVL_DC_22 | STRING | 1 | — | Debit/Credit flag for GL line 22 (D=Debit, C=Credit) |
| 95 | BKAP_INVL_DC_23 | STRING | 1 | — | Debit/Credit flag for GL line 23 (D=Debit, C=Credit) |
| 96 | BKAP_INVL_DC_24 | STRING | 1 | — | Debit/Credit flag for GL line 24 (D=Debit, C=Credit) |
| 97 | BKAP_INVL_DC_25 | STRING | 1 | — | Debit/Credit flag for GL line 25 (D=Debit, C=Credit) |
| 98 | BKAP_INVL_DC_26 | STRING | 1 | — | Debit/Credit flag for GL line 26 (D=Debit, C=Credit) |
| 99 | BKAP_INVL_DC_27 | STRING | 1 | — | Debit/Credit flag for GL line 27 (D=Debit, C=Credit) |
| 100 | BKAP_INVL_DC_28 | STRING | 1 | — | Debit/Credit flag for GL line 28 (D=Debit, C=Credit) |
| 101 | BKAP_INVL_DC_29 | STRING | 1 | — | Debit/Credit flag for GL line 29 (D=Debit, C=Credit) |
| 102 | BKAP_INVL_DC_3 | STRING | 1 | — | Debit/Credit flag for GL line 3 (D=Debit, C=Credit) |
| 103 | BKAP_INVL_DC_30 | STRING | 1 | — | Debit/Credit flag for GL line 30 (D=Debit, C=Credit) |
| 104 | BKAP_INVL_DC_31 | STRING | 1 | — | Debit/Credit flag for GL line 31 (D=Debit, C=Credit) |
| 105 | BKAP_INVL_DC_32 | STRING | 1 | — | Debit/Credit flag for GL line 32 (D=Debit, C=Credit) |
| 106 | BKAP_INVL_DC_33 | STRING | 1 | — | Debit/Credit flag for GL line 33 (D=Debit, C=Credit) |
| 107 | BKAP_INVL_DC_34 | STRING | 1 | — | Debit/Credit flag for GL line 34 (D=Debit, C=Credit) |
| 108 | BKAP_INVL_DC_35 | STRING | 1 | — | Debit/Credit flag for GL line 35 (D=Debit, C=Credit) |
| 109 | BKAP_INVL_DC_36 | STRING | 1 | — | Debit/Credit flag for GL line 36 (D=Debit, C=Credit) |
| 110 | BKAP_INVL_DC_37 | STRING | 1 | — | Debit/Credit flag for GL line 37 (D=Debit, C=Credit) |
| 111 | BKAP_INVL_DC_38 | STRING | 1 | — | Debit/Credit flag for GL line 38 (D=Debit, C=Credit) |
| 112 | BKAP_INVL_DC_39 | STRING | 1 | — | Debit/Credit flag for GL line 39 (D=Debit, C=Credit) |
| 113 | BKAP_INVL_DC_4 | STRING | 1 | — | Debit/Credit flag for GL line 4 (D=Debit, C=Credit) |
| 114 | BKAP_INVL_DC_40 | STRING | 1 | — | Debit/Credit flag for GL line 40 (D=Debit, C=Credit) |
| 115 | BKAP_INVL_DC_41 | STRING | 1 | — | Debit/Credit flag for GL line 41 (D=Debit, C=Credit) |
| 116 | BKAP_INVL_DC_42 | STRING | 1 | — | Debit/Credit flag for GL line 42 (D=Debit, C=Credit) |
| 117 | BKAP_INVL_DC_43 | STRING | 1 | — | Debit/Credit flag for GL line 43 (D=Debit, C=Credit) |
| 118 | BKAP_INVL_DC_44 | STRING | 1 | — | Debit/Credit flag for GL line 44 (D=Debit, C=Credit) |
| 119 | BKAP_INVL_DC_45 | STRING | 1 | — | Debit/Credit flag for GL line 45 (D=Debit, C=Credit) |
| 120 | BKAP_INVL_DC_46 | STRING | 1 | — | Debit/Credit flag for GL line 46 (D=Debit, C=Credit) |
| 121 | BKAP_INVL_DC_47 | STRING | 1 | — | Debit/Credit flag for GL line 47 (D=Debit, C=Credit) |
| 122 | BKAP_INVL_DC_48 | STRING | 1 | — | Debit/Credit flag for GL line 48 (D=Debit, C=Credit) |
| 123 | BKAP_INVL_DC_49 | STRING | 1 | — | Debit/Credit flag for GL line 49 (D=Debit, C=Credit) |
| 124 | BKAP_INVL_DC_5 | STRING | 1 | — | Debit/Credit flag for GL line 5 (D=Debit, C=Credit) |
| 125 | BKAP_INVL_DC_50 | STRING | 1 | — | Debit/Credit flag for GL line 50 (D=Debit, C=Credit) |
| 126 | BKAP_INVL_DC_51 | STRING | 1 | — | Debit/Credit flag for GL line 51 (D=Debit, C=Credit) |
| 127 | BKAP_INVL_DC_52 | STRING | 1 | — | Debit/Credit flag for GL line 52 (D=Debit, C=Credit) |
| 128 | BKAP_INVL_DC_53 | STRING | 1 | — | Debit/Credit flag for GL line 53 (D=Debit, C=Credit) |
| 129 | BKAP_INVL_DC_54 | STRING | 1 | — | Debit/Credit flag for GL line 54 (D=Debit, C=Credit) |
| 130 | BKAP_INVL_DC_55 | STRING | 1 | — | Debit/Credit flag for GL line 55 (D=Debit, C=Credit) |
| 131 | BKAP_INVL_DC_56 | STRING | 1 | — | Debit/Credit flag for GL line 56 (D=Debit, C=Credit) |
| 132 | BKAP_INVL_DC_57 | STRING | 1 | — | Debit/Credit flag for GL line 57 (D=Debit, C=Credit) |
| 133 | BKAP_INVL_DC_58 | STRING | 1 | — | Debit/Credit flag for GL line 58 (D=Debit, C=Credit) |
| 134 | BKAP_INVL_DC_59 | STRING | 1 | — | Debit/Credit flag for GL line 59 (D=Debit, C=Credit) |
| 135 | BKAP_INVL_DC_6 | STRING | 1 | — | Debit/Credit flag for GL line 6 (D=Debit, C=Credit) |
| 136 | BKAP_INVL_DC_60 | STRING | 1 | — | Debit/Credit flag for GL line 60 (D=Debit, C=Credit) |
| 137 | BKAP_INVL_DC_61 | STRING | 1 | — | Debit/Credit flag for GL line 61 (D=Debit, C=Credit) |
| 138 | BKAP_INVL_DC_62 | STRING | 1 | — | Debit/Credit flag for GL line 62 (D=Debit, C=Credit) |
| 139 | BKAP_INVL_DC_63 | STRING | 1 | — | Debit/Credit flag for GL line 63 (D=Debit, C=Credit) |
| 140 | BKAP_INVL_DC_64 | STRING | 1 | — | Debit/Credit flag for GL line 64 (D=Debit, C=Credit) |
| 141 | BKAP_INVL_DC_65 | STRING | 1 | — | Debit/Credit flag for GL line 65 (D=Debit, C=Credit) |
| 142 | BKAP_INVL_DC_66 | STRING | 1 | — | Debit/Credit flag for GL line 66 (D=Debit, C=Credit) |
| 143 | BKAP_INVL_DC_67 | STRING | 1 | — | Debit/Credit flag for GL line 67 (D=Debit, C=Credit) |
| 144 | BKAP_INVL_DC_68 | STRING | 1 | — | Debit/Credit flag for GL line 68 (D=Debit, C=Credit) |
| 145 | BKAP_INVL_DC_69 | STRING | 1 | — | Debit/Credit flag for GL line 69 (D=Debit, C=Credit) |
| 146 | BKAP_INVL_DC_7 | STRING | 1 | — | Debit/Credit flag for GL line 7 (D=Debit, C=Credit) |
| 147 | BKAP_INVL_DC_70 | STRING | 1 | — | Debit/Credit flag for GL line 70 (D=Debit, C=Credit) |
| 148 | BKAP_INVL_DC_71 | STRING | 1 | — | Debit/Credit flag for GL line 71 (D=Debit, C=Credit) |
| 149 | BKAP_INVL_DC_72 | STRING | 1 | — | Debit/Credit flag for GL line 72 (D=Debit, C=Credit) |
| 150 | BKAP_INVL_DC_73 | STRING | 1 | — | Debit/Credit flag for GL line 73 (D=Debit, C=Credit) |
| 151 | BKAP_INVL_DC_74 | STRING | 1 | — | Debit/Credit flag for GL line 74 (D=Debit, C=Credit) |
| 152 | BKAP_INVL_DC_75 | STRING | 1 | — | Debit/Credit flag for GL line 75 (D=Debit, C=Credit) |
| 153 | BKAP_INVL_DC_8 | STRING | 1 | — | Debit/Credit flag for GL line 8 (D=Debit, C=Credit) |
| 154 | BKAP_INVL_DC_9 | STRING | 1 | — | Debit/Credit flag for GL line 9 (D=Debit, C=Credit) |
| 155 | BKAP_INVL_DESC | STRING | 25 | — | Description |
| 156 | BKAP_INVL_EXTRA | STRING | 50 | — | Extra |
| 157 | BKAP_INVL_GLACT_1 | STRING | 10 | — | GL account code for distribution line 1 |
| 158 | BKAP_INVL_GLACT_10 | STRING | 10 | — | GL account code for distribution line 10 |
| 159 | BKAP_INVL_GLACT_11 | STRING | 10 | — | GL account code for distribution line 11 |
| 160 | BKAP_INVL_GLACT_12 | STRING | 10 | — | GL account code for distribution line 12 |
| 161 | BKAP_INVL_GLACT_13 | STRING | 10 | — | GL account code for distribution line 13 |
| 162 | BKAP_INVL_GLACT_14 | STRING | 10 | — | GL account code for distribution line 14 |
| 163 | BKAP_INVL_GLACT_15 | STRING | 10 | — | GL account code for distribution line 15 |
| 164 | BKAP_INVL_GLACT_16 | STRING | 10 | — | GL account code for distribution line 16 |
| 165 | BKAP_INVL_GLACT_17 | STRING | 10 | — | GL account code for distribution line 17 |
| 166 | BKAP_INVL_GLACT_18 | STRING | 10 | — | GL account code for distribution line 18 |
| 167 | BKAP_INVL_GLACT_19 | STRING | 10 | — | GL account code for distribution line 19 |
| 168 | BKAP_INVL_GLACT_2 | STRING | 10 | — | GL account code for distribution line 2 |
| 169 | BKAP_INVL_GLACT_20 | STRING | 10 | — | GL account code for distribution line 20 |
| 170 | BKAP_INVL_GLACT_21 | STRING | 10 | — | GL account code for distribution line 21 |
| 171 | BKAP_INVL_GLACT_22 | STRING | 10 | — | GL account code for distribution line 22 |
| 172 | BKAP_INVL_GLACT_23 | STRING | 10 | — | GL account code for distribution line 23 |
| 173 | BKAP_INVL_GLACT_24 | STRING | 10 | — | GL account code for distribution line 24 |
| 174 | BKAP_INVL_GLACT_25 | STRING | 10 | — | GL account code for distribution line 25 |
| 175 | BKAP_INVL_GLACT_26 | STRING | 10 | — | GL account code for distribution line 26 |
| 176 | BKAP_INVL_GLACT_27 | STRING | 10 | — | GL account code for distribution line 27 |
| 177 | BKAP_INVL_GLACT_28 | STRING | 10 | — | GL account code for distribution line 28 |
| 178 | BKAP_INVL_GLACT_29 | STRING | 10 | — | GL account code for distribution line 29 |
| 179 | BKAP_INVL_GLACT_3 | STRING | 10 | — | GL account code for distribution line 3 |
| 180 | BKAP_INVL_GLACT_30 | STRING | 10 | — | GL account code for distribution line 30 |
| 181 | BKAP_INVL_GLACT_31 | STRING | 10 | — | GL account code for distribution line 31 |
| 182 | BKAP_INVL_GLACT_32 | STRING | 10 | — | GL account code for distribution line 32 |
| 183 | BKAP_INVL_GLACT_33 | STRING | 10 | — | GL account code for distribution line 33 |
| 184 | BKAP_INVL_GLACT_34 | STRING | 10 | — | GL account code for distribution line 34 |
| 185 | BKAP_INVL_GLACT_35 | STRING | 10 | — | GL account code for distribution line 35 |
| 186 | BKAP_INVL_GLACT_36 | STRING | 10 | — | GL account code for distribution line 36 |
| 187 | BKAP_INVL_GLACT_37 | STRING | 10 | — | GL account code for distribution line 37 |
| 188 | BKAP_INVL_GLACT_38 | STRING | 10 | — | GL account code for distribution line 38 |
| 189 | BKAP_INVL_GLACT_39 | STRING | 10 | — | GL account code for distribution line 39 |
| 190 | BKAP_INVL_GLACT_4 | STRING | 10 | — | GL account code for distribution line 4 |
| 191 | BKAP_INVL_GLACT_40 | STRING | 10 | — | GL account code for distribution line 40 |
| 192 | BKAP_INVL_GLACT_41 | STRING | 10 | — | GL account code for distribution line 41 |
| 193 | BKAP_INVL_GLACT_42 | STRING | 10 | — | GL account code for distribution line 42 |
| 194 | BKAP_INVL_GLACT_43 | STRING | 10 | — | GL account code for distribution line 43 |
| 195 | BKAP_INVL_GLACT_44 | STRING | 10 | — | GL account code for distribution line 44 |
| 196 | BKAP_INVL_GLACT_45 | STRING | 10 | — | GL account code for distribution line 45 |
| 197 | BKAP_INVL_GLACT_46 | STRING | 10 | — | GL account code for distribution line 46 |
| 198 | BKAP_INVL_GLACT_47 | STRING | 10 | — | GL account code for distribution line 47 |
| 199 | BKAP_INVL_GLACT_48 | STRING | 10 | — | GL account code for distribution line 48 |
| 200 | BKAP_INVL_GLACT_49 | STRING | 10 | — | GL account code for distribution line 49 |
| 201 | BKAP_INVL_GLACT_5 | STRING | 10 | — | GL account code for distribution line 5 |
| 202 | BKAP_INVL_GLACT_50 | STRING | 10 | — | GL account code for distribution line 50 |
| 203 | BKAP_INVL_GLACT_51 | STRING | 10 | — | GL account code for distribution line 51 |
| 204 | BKAP_INVL_GLACT_52 | STRING | 10 | — | GL account code for distribution line 52 |
| 205 | BKAP_INVL_GLACT_53 | STRING | 10 | — | GL account code for distribution line 53 |
| 206 | BKAP_INVL_GLACT_54 | STRING | 10 | — | GL account code for distribution line 54 |
| 207 | BKAP_INVL_GLACT_55 | STRING | 10 | — | GL account code for distribution line 55 |
| 208 | BKAP_INVL_GLACT_56 | STRING | 10 | — | GL account code for distribution line 56 |
| 209 | BKAP_INVL_GLACT_57 | STRING | 10 | — | GL account code for distribution line 57 |
| 210 | BKAP_INVL_GLACT_58 | STRING | 10 | — | GL account code for distribution line 58 |
| 211 | BKAP_INVL_GLACT_59 | STRING | 10 | — | GL account code for distribution line 59 |
| 212 | BKAP_INVL_GLACT_6 | STRING | 10 | — | GL account code for distribution line 6 |
| 213 | BKAP_INVL_GLACT_60 | STRING | 10 | — | GL account code for distribution line 60 |
| 214 | BKAP_INVL_GLACT_61 | STRING | 10 | — | GL account code for distribution line 61 |
| 215 | BKAP_INVL_GLACT_62 | STRING | 10 | — | GL account code for distribution line 62 |
| 216 | BKAP_INVL_GLACT_63 | STRING | 10 | — | GL account code for distribution line 63 |
| 217 | BKAP_INVL_GLACT_64 | STRING | 10 | — | GL account code for distribution line 64 |
| 218 | BKAP_INVL_GLACT_65 | STRING | 10 | — | GL account code for distribution line 65 |
| 219 | BKAP_INVL_GLACT_66 | STRING | 10 | — | GL account code for distribution line 66 |
| 220 | BKAP_INVL_GLACT_67 | STRING | 10 | — | GL account code for distribution line 67 |
| 221 | BKAP_INVL_GLACT_68 | STRING | 10 | — | GL account code for distribution line 68 |
| 222 | BKAP_INVL_GLACT_69 | STRING | 10 | — | GL account code for distribution line 69 |
| 223 | BKAP_INVL_GLACT_7 | STRING | 10 | — | GL account code for distribution line 7 |
| 224 | BKAP_INVL_GLACT_70 | STRING | 10 | — | GL account code for distribution line 70 |
| 225 | BKAP_INVL_GLACT_71 | STRING | 10 | — | GL account code for distribution line 71 |
| 226 | BKAP_INVL_GLACT_72 | STRING | 10 | — | GL account code for distribution line 72 |
| 227 | BKAP_INVL_GLACT_73 | STRING | 10 | — | GL account code for distribution line 73 |
| 228 | BKAP_INVL_GLACT_74 | STRING | 10 | — | GL account code for distribution line 74 |
| 229 | BKAP_INVL_GLACT_75 | STRING | 10 | — | GL account code for distribution line 75 |
| 230 | BKAP_INVL_GLACT_8 | STRING | 10 | — | GL account code for distribution line 8 |
| 231 | BKAP_INVL_GLACT_9 | STRING | 10 | — | GL account code for distribution line 9 |
| 232 | BKAP_INVL_GLD_1 | STRING | 25 | — | GL account description for distribution line 1 |
| 233 | BKAP_INVL_GLD_10 | STRING | 25 | — | GL account description for distribution line 10 |
| 234 | BKAP_INVL_GLD_11 | STRING | 25 | — | GL account description for distribution line 11 |
| 235 | BKAP_INVL_GLD_12 | STRING | 25 | — | GL account description for distribution line 12 |
| 236 | BKAP_INVL_GLD_13 | STRING | 25 | — | GL account description for distribution line 13 |
| 237 | BKAP_INVL_GLD_14 | STRING | 25 | — | GL account description for distribution line 14 |
| 238 | BKAP_INVL_GLD_15 | STRING | 25 | — | GL account description for distribution line 15 |
| 239 | BKAP_INVL_GLD_16 | STRING | 25 | — | GL account description for distribution line 16 |
| 240 | BKAP_INVL_GLD_17 | STRING | 25 | — | GL account description for distribution line 17 |
| 241 | BKAP_INVL_GLD_18 | STRING | 25 | — | GL account description for distribution line 18 |
| 242 | BKAP_INVL_GLD_19 | STRING | 25 | — | GL account description for distribution line 19 |
| 243 | BKAP_INVL_GLD_2 | STRING | 25 | — | GL account description for distribution line 2 |
| 244 | BKAP_INVL_GLD_20 | STRING | 25 | — | GL account description for distribution line 20 |
| 245 | BKAP_INVL_GLD_21 | STRING | 25 | — | GL account description for distribution line 21 |
| 246 | BKAP_INVL_GLD_22 | STRING | 25 | — | GL account description for distribution line 22 |
| 247 | BKAP_INVL_GLD_23 | STRING | 25 | — | GL account description for distribution line 23 |
| 248 | BKAP_INVL_GLD_24 | STRING | 25 | — | GL account description for distribution line 24 |
| 249 | BKAP_INVL_GLD_25 | STRING | 25 | — | GL account description for distribution line 25 |
| 250 | BKAP_INVL_GLD_26 | STRING | 25 | — | GL account description for distribution line 26 |
| 251 | BKAP_INVL_GLD_27 | STRING | 25 | — | GL account description for distribution line 27 |
| 252 | BKAP_INVL_GLD_28 | STRING | 25 | — | GL account description for distribution line 28 |
| 253 | BKAP_INVL_GLD_29 | STRING | 25 | — | GL account description for distribution line 29 |
| 254 | BKAP_INVL_GLD_3 | STRING | 25 | — | GL account description for distribution line 3 |
| 255 | BKAP_INVL_GLD_30 | STRING | 25 | — | GL account description for distribution line 30 |
| 256 | BKAP_INVL_GLD_31 | STRING | 25 | — | GL account description for distribution line 31 |
| 257 | BKAP_INVL_GLD_32 | STRING | 25 | — | GL account description for distribution line 32 |
| 258 | BKAP_INVL_GLD_33 | STRING | 25 | — | GL account description for distribution line 33 |
| 259 | BKAP_INVL_GLD_34 | STRING | 25 | — | GL account description for distribution line 34 |
| 260 | BKAP_INVL_GLD_35 | STRING | 25 | — | GL account description for distribution line 35 |
| 261 | BKAP_INVL_GLD_36 | STRING | 25 | — | GL account description for distribution line 36 |
| 262 | BKAP_INVL_GLD_37 | STRING | 25 | — | GL account description for distribution line 37 |
| 263 | BKAP_INVL_GLD_38 | STRING | 25 | — | GL account description for distribution line 38 |
| 264 | BKAP_INVL_GLD_39 | STRING | 25 | — | GL account description for distribution line 39 |
| 265 | BKAP_INVL_GLD_4 | STRING | 25 | — | GL account description for distribution line 4 |
| 266 | BKAP_INVL_GLD_40 | STRING | 25 | — | GL account description for distribution line 40 |
| 267 | BKAP_INVL_GLD_41 | STRING | 25 | — | GL account description for distribution line 41 |
| 268 | BKAP_INVL_GLD_42 | STRING | 25 | — | GL account description for distribution line 42 |
| 269 | BKAP_INVL_GLD_43 | STRING | 25 | — | GL account description for distribution line 43 |
| 270 | BKAP_INVL_GLD_44 | STRING | 25 | — | GL account description for distribution line 44 |
| 271 | BKAP_INVL_GLD_45 | STRING | 25 | — | GL account description for distribution line 45 |
| 272 | BKAP_INVL_GLD_46 | STRING | 25 | — | GL account description for distribution line 46 |
| 273 | BKAP_INVL_GLD_47 | STRING | 25 | — | GL account description for distribution line 47 |
| 274 | BKAP_INVL_GLD_48 | STRING | 25 | — | GL account description for distribution line 48 |
| 275 | BKAP_INVL_GLD_49 | STRING | 25 | — | GL account description for distribution line 49 |
| 276 | BKAP_INVL_GLD_5 | STRING | 25 | — | GL account description for distribution line 5 |
| 277 | BKAP_INVL_GLD_50 | STRING | 25 | — | GL account description for distribution line 50 |
| 278 | BKAP_INVL_GLD_51 | STRING | 25 | — | GL account description for distribution line 51 |
| 279 | BKAP_INVL_GLD_52 | STRING | 25 | — | GL account description for distribution line 52 |
| 280 | BKAP_INVL_GLD_53 | STRING | 25 | — | GL account description for distribution line 53 |
| 281 | BKAP_INVL_GLD_54 | STRING | 25 | — | GL account description for distribution line 54 |
| 282 | BKAP_INVL_GLD_55 | STRING | 25 | — | GL account description for distribution line 55 |
| 283 | BKAP_INVL_GLD_56 | STRING | 25 | — | GL account description for distribution line 56 |
| 284 | BKAP_INVL_GLD_57 | STRING | 25 | — | GL account description for distribution line 57 |
| 285 | BKAP_INVL_GLD_58 | STRING | 25 | — | GL account description for distribution line 58 |
| 286 | BKAP_INVL_GLD_59 | STRING | 25 | — | GL account description for distribution line 59 |
| 287 | BKAP_INVL_GLD_6 | STRING | 25 | — | GL account description for distribution line 6 |
| 288 | BKAP_INVL_GLD_60 | STRING | 25 | — | GL account description for distribution line 60 |
| 289 | BKAP_INVL_GLD_61 | STRING | 25 | — | GL account description for distribution line 61 |
| 290 | BKAP_INVL_GLD_62 | STRING | 25 | — | GL account description for distribution line 62 |
| 291 | BKAP_INVL_GLD_63 | STRING | 25 | — | GL account description for distribution line 63 |
| 292 | BKAP_INVL_GLD_64 | STRING | 25 | — | GL account description for distribution line 64 |
| 293 | BKAP_INVL_GLD_65 | STRING | 25 | — | GL account description for distribution line 65 |
| 294 | BKAP_INVL_GLD_66 | STRING | 25 | — | GL account description for distribution line 66 |
| 295 | BKAP_INVL_GLD_67 | STRING | 25 | — | GL account description for distribution line 67 |
| 296 | BKAP_INVL_GLD_68 | STRING | 25 | — | GL account description for distribution line 68 |
| 297 | BKAP_INVL_GLD_69 | STRING | 25 | — | GL account description for distribution line 69 |
| 298 | BKAP_INVL_GLD_7 | STRING | 25 | — | GL account description for distribution line 7 |
| 299 | BKAP_INVL_GLD_70 | STRING | 25 | — | GL account description for distribution line 70 |
| 300 | BKAP_INVL_GLD_71 | STRING | 25 | — | GL account description for distribution line 71 |
| 301 | BKAP_INVL_GLD_72 | STRING | 25 | — | GL account description for distribution line 72 |
| 302 | BKAP_INVL_GLD_73 | STRING | 25 | — | GL account description for distribution line 73 |
| 303 | BKAP_INVL_GLD_74 | STRING | 25 | — | GL account description for distribution line 74 |
| 304 | BKAP_INVL_GLD_75 | STRING | 25 | — | GL account description for distribution line 75 |
| 305 | BKAP_INVL_GLD_8 | STRING | 25 | — | GL account description for distribution line 8 |
| 306 | BKAP_INVL_GLD_9 | STRING | 25 | — | GL account description for distribution line 9 |
| 307 | BKAP_INVL_GLDPT_1 | STRING | 4 | — | GL department for distribution line 1 |
| 308 | BKAP_INVL_GLDPT_10 | STRING | 4 | — | GL department for distribution line 10 |
| 309 | BKAP_INVL_GLDPT_11 | STRING | 4 | — | GL department for distribution line 11 |
| 310 | BKAP_INVL_GLDPT_12 | STRING | 4 | — | GL department for distribution line 12 |
| 311 | BKAP_INVL_GLDPT_13 | STRING | 4 | — | GL department for distribution line 13 |
| 312 | BKAP_INVL_GLDPT_14 | STRING | 4 | — | GL department for distribution line 14 |
| 313 | BKAP_INVL_GLDPT_15 | STRING | 4 | — | GL department for distribution line 15 |
| 314 | BKAP_INVL_GLDPT_16 | STRING | 4 | — | GL department for distribution line 16 |
| 315 | BKAP_INVL_GLDPT_17 | STRING | 4 | — | GL department for distribution line 17 |
| 316 | BKAP_INVL_GLDPT_18 | STRING | 4 | — | GL department for distribution line 18 |
| 317 | BKAP_INVL_GLDPT_19 | STRING | 4 | — | GL department for distribution line 19 |
| 318 | BKAP_INVL_GLDPT_2 | STRING | 4 | — | GL department for distribution line 2 |
| 319 | BKAP_INVL_GLDPT_20 | STRING | 4 | — | GL department for distribution line 20 |
| 320 | BKAP_INVL_GLDPT_21 | STRING | 4 | — | GL department for distribution line 21 |
| 321 | BKAP_INVL_GLDPT_22 | STRING | 4 | — | GL department for distribution line 22 |
| 322 | BKAP_INVL_GLDPT_23 | STRING | 4 | — | GL department for distribution line 23 |
| 323 | BKAP_INVL_GLDPT_24 | STRING | 4 | — | GL department for distribution line 24 |
| 324 | BKAP_INVL_GLDPT_25 | STRING | 4 | — | GL department for distribution line 25 |
| 325 | BKAP_INVL_GLDPT_26 | STRING | 4 | — | GL department for distribution line 26 |
| 326 | BKAP_INVL_GLDPT_27 | STRING | 4 | — | GL department for distribution line 27 |
| 327 | BKAP_INVL_GLDPT_28 | STRING | 4 | — | GL department for distribution line 28 |
| 328 | BKAP_INVL_GLDPT_29 | STRING | 4 | — | GL department for distribution line 29 |
| 329 | BKAP_INVL_GLDPT_3 | STRING | 4 | — | GL department for distribution line 3 |
| 330 | BKAP_INVL_GLDPT_30 | STRING | 4 | — | GL department for distribution line 30 |
| 331 | BKAP_INVL_GLDPT_31 | STRING | 4 | — | GL department for distribution line 31 |
| 332 | BKAP_INVL_GLDPT_32 | STRING | 4 | — | GL department for distribution line 32 |
| 333 | BKAP_INVL_GLDPT_33 | STRING | 4 | — | GL department for distribution line 33 |
| 334 | BKAP_INVL_GLDPT_34 | STRING | 4 | — | GL department for distribution line 34 |
| 335 | BKAP_INVL_GLDPT_35 | STRING | 4 | — | GL department for distribution line 35 |
| 336 | BKAP_INVL_GLDPT_36 | STRING | 4 | — | GL department for distribution line 36 |
| 337 | BKAP_INVL_GLDPT_37 | STRING | 4 | — | GL department for distribution line 37 |
| 338 | BKAP_INVL_GLDPT_38 | STRING | 4 | — | GL department for distribution line 38 |
| 339 | BKAP_INVL_GLDPT_39 | STRING | 4 | — | GL department for distribution line 39 |
| 340 | BKAP_INVL_GLDPT_4 | STRING | 4 | — | GL department for distribution line 4 |
| 341 | BKAP_INVL_GLDPT_40 | STRING | 4 | — | GL department for distribution line 40 |
| 342 | BKAP_INVL_GLDPT_41 | STRING | 4 | — | GL department for distribution line 41 |
| 343 | BKAP_INVL_GLDPT_42 | STRING | 4 | — | GL department for distribution line 42 |
| 344 | BKAP_INVL_GLDPT_43 | STRING | 4 | — | GL department for distribution line 43 |
| 345 | BKAP_INVL_GLDPT_44 | STRING | 4 | — | GL department for distribution line 44 |
| 346 | BKAP_INVL_GLDPT_45 | STRING | 4 | — | GL department for distribution line 45 |
| 347 | BKAP_INVL_GLDPT_46 | STRING | 4 | — | GL department for distribution line 46 |
| 348 | BKAP_INVL_GLDPT_47 | STRING | 4 | — | GL department for distribution line 47 |
| 349 | BKAP_INVL_GLDPT_48 | STRING | 4 | — | GL department for distribution line 48 |
| 350 | BKAP_INVL_GLDPT_49 | STRING | 4 | — | GL department for distribution line 49 |
| 351 | BKAP_INVL_GLDPT_5 | STRING | 4 | — | GL department for distribution line 5 |
| 352 | BKAP_INVL_GLDPT_50 | STRING | 4 | — | GL department for distribution line 50 |
| 353 | BKAP_INVL_GLDPT_51 | STRING | 4 | — | GL department for distribution line 51 |
| 354 | BKAP_INVL_GLDPT_52 | STRING | 4 | — | GL department for distribution line 52 |
| 355 | BKAP_INVL_GLDPT_53 | STRING | 4 | — | GL department for distribution line 53 |
| 356 | BKAP_INVL_GLDPT_54 | STRING | 4 | — | GL department for distribution line 54 |
| 357 | BKAP_INVL_GLDPT_55 | STRING | 4 | — | GL department for distribution line 55 |
| 358 | BKAP_INVL_GLDPT_56 | STRING | 4 | — | GL department for distribution line 56 |
| 359 | BKAP_INVL_GLDPT_57 | STRING | 4 | — | GL department for distribution line 57 |
| 360 | BKAP_INVL_GLDPT_58 | STRING | 4 | — | GL department for distribution line 58 |
| 361 | BKAP_INVL_GLDPT_59 | STRING | 4 | — | GL department for distribution line 59 |
| 362 | BKAP_INVL_GLDPT_6 | STRING | 4 | — | GL department for distribution line 6 |
| 363 | BKAP_INVL_GLDPT_60 | STRING | 4 | — | GL department for distribution line 60 |
| 364 | BKAP_INVL_GLDPT_61 | STRING | 4 | — | GL department for distribution line 61 |
| 365 | BKAP_INVL_GLDPT_62 | STRING | 4 | — | GL department for distribution line 62 |
| 366 | BKAP_INVL_GLDPT_63 | STRING | 4 | — | GL department for distribution line 63 |
| 367 | BKAP_INVL_GLDPT_64 | STRING | 4 | — | GL department for distribution line 64 |
| 368 | BKAP_INVL_GLDPT_65 | STRING | 4 | — | GL department for distribution line 65 |
| 369 | BKAP_INVL_GLDPT_66 | STRING | 4 | — | GL department for distribution line 66 |
| 370 | BKAP_INVL_GLDPT_67 | STRING | 4 | — | GL department for distribution line 67 |
| 371 | BKAP_INVL_GLDPT_68 | STRING | 4 | — | GL department for distribution line 68 |
| 372 | BKAP_INVL_GLDPT_69 | STRING | 4 | — | GL department for distribution line 69 |
| 373 | BKAP_INVL_GLDPT_7 | STRING | 4 | — | GL department for distribution line 7 |
| 374 | BKAP_INVL_GLDPT_70 | STRING | 4 | — | GL department for distribution line 70 |
| 375 | BKAP_INVL_GLDPT_71 | STRING | 4 | — | GL department for distribution line 71 |
| 376 | BKAP_INVL_GLDPT_72 | STRING | 4 | — | GL department for distribution line 72 |
| 377 | BKAP_INVL_GLDPT_73 | STRING | 4 | — | GL department for distribution line 73 |
| 378 | BKAP_INVL_GLDPT_74 | STRING | 4 | — | GL department for distribution line 74 |
| 379 | BKAP_INVL_GLDPT_75 | STRING | 4 | — | GL department for distribution line 75 |
| 380 | BKAP_INVL_GLDPT_8 | STRING | 4 | — | GL department for distribution line 8 |
| 381 | BKAP_INVL_GLDPT_9 | STRING | 4 | — | GL department for distribution line 9 |
| 382 | BKAP_INVL_ISCUR | STRING | 3 | — | Currency |
| 383 | BKAP_INVL_JOB | STRING | 15 | — | Job number linked to this voucher |
| 384 | BKAP_INVL_NUM | STRING | 10 | — | Invoice Number |
| 385 | BKAP_INVL_TAMT | NUMERIC | 8 | 2 | Tran Amount |
| 386 | BKAP_INVL_TDC | STRING | 1 | — | Tran Debit/Credit D/C |
| 387 | BKAP_INVL_TERMD | STRING | 10 | — | Terms Description |
| 388 | BKAP_INVL_TERMN | INTEGER | 2 | — | Terms Number |
| 389 | BKAP_INVL_TYPED | STRING | 10 | — | Tran.Type Description |
| 390 | BKAP_INVL_TYPEN | INTEGER | 2 | — | Tran. Type Number |

## BKAPINVT
**AP INVOICE**

Fields: 19

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAP_INVT_AMT | NUMERIC | 8 | 2 | Amount |
| 2 | BKAP_INVT_AMTRM | NUMERIC | 8 | 2 | Amount Remaining |
| 3 | BKAP_INVT_CHKAC | INTEGER | 2 | — | Bank account number used for this check |
| 4 | BKAP_INVT_CHKNO | NUMERIC | 8 | — | Check number issued for payment |
| 5 | BKAP_INVT_CODE | STRING | 10 | — | Vendor Code |
| 6 | BKAP_INVT_DATE | DATE | 4 | — | Transaction Date |
| 7 | BKAP_INVT_DEPNO | NUMERIC | 8 | — | Deposit number |
| 8 | BKAP_INVT_DESC | STRING | 25 | — | Transaction Description |
| 9 | BKAP_INVT_EXTRA | STRING | 50 | — | Extra |
| 10 | BKAP_INVT_FRT | NUMERIC | 8 | 2 | Freight amount |
| 11 | BKAP_INVT_GLDPT | STRING | 4 | — | GL Department |
| 12 | BKAP_INVT_MCCOD | STRING | 3 | — | Currency Code |
| 13 | BKAP_INVT_MCRAT | NUMERIC | 8 | 6 | Currency Rate |
| 14 | BKAP_INVT_NUM | STRING | 10 | — | Invoice/Voucher Reference No. |
| 15 | BKAP_INVT_PDATE | DATE | 4 | — | Post Date |
| 16 | BKAP_INVT_SDATE | DATE | 4 | — | Start Date |
| 17 | BKAP_INVT_TAX | NUMERIC | 8 | 2 | Tax amount |
| 18 | BKAP_INVT_TERMN | INTEGER | 2 | — | Terms Number |
| 19 | BKAP_INVT_TYPE | STRING | 1 | — | transaction Type (IPCM) |

## BKAPRIVL
**VOUCHER TEMPLATE/RECURRING VOUCHER**

Fields: 390

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAP_INVL_APDPT | STRING | 4 | — | Recurring Invoice |
| 2 | BKAP_INVL_CHK | INTEGER | 2 | — | Manual Check Number |
| 3 | BKAP_INVL_CODE | STRING | 10 | — | Vendor Code |
| 4 | BKAP_INVL_DAMT_1 | NUMERIC | 8 | 2 | GL distribution amount for line 1 |
| 5 | BKAP_INVL_DAMT_10 | NUMERIC | 8 | 2 | GL distribution amount for line 10 |
| 6 | BKAP_INVL_DAMT_11 | NUMERIC | 8 | 2 | GL distribution amount for line 11 |
| 7 | BKAP_INVL_DAMT_12 | NUMERIC | 8 | 2 | GL distribution amount for line 12 |
| 8 | BKAP_INVL_DAMT_13 | NUMERIC | 8 | 2 | GL distribution amount for line 13 |
| 9 | BKAP_INVL_DAMT_14 | NUMERIC | 8 | 2 | GL distribution amount for line 14 |
| 10 | BKAP_INVL_DAMT_15 | NUMERIC | 8 | 2 | GL distribution amount for line 15 |
| 11 | BKAP_INVL_DAMT_16 | NUMERIC | 8 | 2 | GL distribution amount for line 16 |
| 12 | BKAP_INVL_DAMT_17 | NUMERIC | 8 | 2 | GL distribution amount for line 17 |
| 13 | BKAP_INVL_DAMT_18 | NUMERIC | 8 | 2 | GL distribution amount for line 18 |
| 14 | BKAP_INVL_DAMT_19 | NUMERIC | 8 | 2 | GL distribution amount for line 19 |
| 15 | BKAP_INVL_DAMT_2 | NUMERIC | 8 | 2 | GL distribution amount for line 2 |
| 16 | BKAP_INVL_DAMT_20 | NUMERIC | 8 | 2 | GL distribution amount for line 20 |
| 17 | BKAP_INVL_DAMT_21 | NUMERIC | 8 | 2 | GL distribution amount for line 21 |
| 18 | BKAP_INVL_DAMT_22 | NUMERIC | 8 | 2 | GL distribution amount for line 22 |
| 19 | BKAP_INVL_DAMT_23 | NUMERIC | 8 | 2 | GL distribution amount for line 23 |
| 20 | BKAP_INVL_DAMT_24 | NUMERIC | 8 | 2 | GL distribution amount for line 24 |
| 21 | BKAP_INVL_DAMT_25 | NUMERIC | 8 | 2 | GL distribution amount for line 25 |
| 22 | BKAP_INVL_DAMT_26 | NUMERIC | 8 | 2 | GL distribution amount for line 26 |
| 23 | BKAP_INVL_DAMT_27 | NUMERIC | 8 | 2 | GL distribution amount for line 27 |
| 24 | BKAP_INVL_DAMT_28 | NUMERIC | 8 | 2 | GL distribution amount for line 28 |
| 25 | BKAP_INVL_DAMT_29 | NUMERIC | 8 | 2 | GL distribution amount for line 29 |
| 26 | BKAP_INVL_DAMT_3 | NUMERIC | 8 | 2 | GL distribution amount for line 3 |
| 27 | BKAP_INVL_DAMT_30 | NUMERIC | 8 | 2 | GL distribution amount for line 30 |
| 28 | BKAP_INVL_DAMT_31 | NUMERIC | 8 | 2 | GL distribution amount for line 31 |
| 29 | BKAP_INVL_DAMT_32 | NUMERIC | 8 | 2 | GL distribution amount for line 32 |
| 30 | BKAP_INVL_DAMT_33 | NUMERIC | 8 | 2 | GL distribution amount for line 33 |
| 31 | BKAP_INVL_DAMT_34 | NUMERIC | 8 | 2 | GL distribution amount for line 34 |
| 32 | BKAP_INVL_DAMT_35 | NUMERIC | 8 | 2 | GL distribution amount for line 35 |
| 33 | BKAP_INVL_DAMT_36 | NUMERIC | 8 | 2 | GL distribution amount for line 36 |
| 34 | BKAP_INVL_DAMT_37 | NUMERIC | 8 | 2 | GL distribution amount for line 37 |
| 35 | BKAP_INVL_DAMT_38 | NUMERIC | 8 | 2 | GL distribution amount for line 38 |
| 36 | BKAP_INVL_DAMT_39 | NUMERIC | 8 | 2 | GL distribution amount for line 39 |
| 37 | BKAP_INVL_DAMT_4 | NUMERIC | 8 | 2 | GL distribution amount for line 4 |
| 38 | BKAP_INVL_DAMT_40 | NUMERIC | 8 | 2 | GL distribution amount for line 40 |
| 39 | BKAP_INVL_DAMT_41 | NUMERIC | 8 | 2 | GL distribution amount for line 41 |
| 40 | BKAP_INVL_DAMT_42 | NUMERIC | 8 | 2 | GL distribution amount for line 42 |
| 41 | BKAP_INVL_DAMT_43 | NUMERIC | 8 | 2 | GL distribution amount for line 43 |
| 42 | BKAP_INVL_DAMT_44 | NUMERIC | 8 | 2 | GL distribution amount for line 44 |
| 43 | BKAP_INVL_DAMT_45 | NUMERIC | 8 | 2 | GL distribution amount for line 45 |
| 44 | BKAP_INVL_DAMT_46 | NUMERIC | 8 | 2 | GL distribution amount for line 46 |
| 45 | BKAP_INVL_DAMT_47 | NUMERIC | 8 | 2 | GL distribution amount for line 47 |
| 46 | BKAP_INVL_DAMT_48 | NUMERIC | 8 | 2 | GL distribution amount for line 48 |
| 47 | BKAP_INVL_DAMT_49 | NUMERIC | 8 | 2 | GL distribution amount for line 49 |
| 48 | BKAP_INVL_DAMT_5 | NUMERIC | 8 | 2 | GL distribution amount for line 5 |
| 49 | BKAP_INVL_DAMT_50 | NUMERIC | 8 | 2 | GL distribution amount for line 50 |
| 50 | BKAP_INVL_DAMT_51 | NUMERIC | 8 | 2 | GL distribution amount for line 51 |
| 51 | BKAP_INVL_DAMT_52 | NUMERIC | 8 | 2 | GL distribution amount for line 52 |
| 52 | BKAP_INVL_DAMT_53 | NUMERIC | 8 | 2 | GL distribution amount for line 53 |
| 53 | BKAP_INVL_DAMT_54 | NUMERIC | 8 | 2 | GL distribution amount for line 54 |
| 54 | BKAP_INVL_DAMT_55 | NUMERIC | 8 | 2 | GL distribution amount for line 55 |
| 55 | BKAP_INVL_DAMT_56 | NUMERIC | 8 | 2 | GL distribution amount for line 56 |
| 56 | BKAP_INVL_DAMT_57 | NUMERIC | 8 | 2 | GL distribution amount for line 57 |
| 57 | BKAP_INVL_DAMT_58 | NUMERIC | 8 | 2 | GL distribution amount for line 58 |
| 58 | BKAP_INVL_DAMT_59 | NUMERIC | 8 | 2 | GL distribution amount for line 59 |
| 59 | BKAP_INVL_DAMT_6 | NUMERIC | 8 | 2 | GL distribution amount for line 6 |
| 60 | BKAP_INVL_DAMT_60 | NUMERIC | 8 | 2 | GL distribution amount for line 60 |
| 61 | BKAP_INVL_DAMT_61 | NUMERIC | 8 | 2 | GL distribution amount for line 61 |
| 62 | BKAP_INVL_DAMT_62 | NUMERIC | 8 | 2 | GL distribution amount for line 62 |
| 63 | BKAP_INVL_DAMT_63 | NUMERIC | 8 | 2 | GL distribution amount for line 63 |
| 64 | BKAP_INVL_DAMT_64 | NUMERIC | 8 | 2 | GL distribution amount for line 64 |
| 65 | BKAP_INVL_DAMT_65 | NUMERIC | 8 | 2 | GL distribution amount for line 65 |
| 66 | BKAP_INVL_DAMT_66 | NUMERIC | 8 | 2 | GL distribution amount for line 66 |
| 67 | BKAP_INVL_DAMT_67 | NUMERIC | 8 | 2 | GL distribution amount for line 67 |
| 68 | BKAP_INVL_DAMT_68 | NUMERIC | 8 | 2 | GL distribution amount for line 68 |
| 69 | BKAP_INVL_DAMT_69 | NUMERIC | 8 | 2 | GL distribution amount for line 69 |
| 70 | BKAP_INVL_DAMT_7 | NUMERIC | 8 | 2 | GL distribution amount for line 7 |
| 71 | BKAP_INVL_DAMT_70 | NUMERIC | 8 | 2 | GL distribution amount for line 70 |
| 72 | BKAP_INVL_DAMT_71 | NUMERIC | 8 | 2 | GL distribution amount for line 71 |
| 73 | BKAP_INVL_DAMT_72 | NUMERIC | 8 | 2 | GL distribution amount for line 72 |
| 74 | BKAP_INVL_DAMT_73 | NUMERIC | 8 | 2 | GL distribution amount for line 73 |
| 75 | BKAP_INVL_DAMT_74 | NUMERIC | 8 | 2 | GL distribution amount for line 74 |
| 76 | BKAP_INVL_DAMT_75 | NUMERIC | 8 | 2 | GL distribution amount for line 75 |
| 77 | BKAP_INVL_DAMT_8 | NUMERIC | 8 | 2 | GL distribution amount for line 8 |
| 78 | BKAP_INVL_DAMT_9 | NUMERIC | 8 | 2 | GL distribution amount for line 9 |
| 79 | BKAP_INVL_DATE | DATE | 4 | — | Invoice Date |
| 80 | BKAP_INVL_DC_1 | STRING | 1 | — | Debit/Credit flag for GL line 1 (D=Debit, C=Credit) |
| 81 | BKAP_INVL_DC_10 | STRING | 1 | — | Debit/Credit flag for GL line 10 (D=Debit, C=Credit) |
| 82 | BKAP_INVL_DC_11 | STRING | 1 | — | Debit/Credit flag for GL line 11 (D=Debit, C=Credit) |
| 83 | BKAP_INVL_DC_12 | STRING | 1 | — | Debit/Credit flag for GL line 12 (D=Debit, C=Credit) |
| 84 | BKAP_INVL_DC_13 | STRING | 1 | — | Debit/Credit flag for GL line 13 (D=Debit, C=Credit) |
| 85 | BKAP_INVL_DC_14 | STRING | 1 | — | Debit/Credit flag for GL line 14 (D=Debit, C=Credit) |
| 86 | BKAP_INVL_DC_15 | STRING | 1 | — | Debit/Credit flag for GL line 15 (D=Debit, C=Credit) |
| 87 | BKAP_INVL_DC_16 | STRING | 1 | — | Debit/Credit flag for GL line 16 (D=Debit, C=Credit) |
| 88 | BKAP_INVL_DC_17 | STRING | 1 | — | Debit/Credit flag for GL line 17 (D=Debit, C=Credit) |
| 89 | BKAP_INVL_DC_18 | STRING | 1 | — | Debit/Credit flag for GL line 18 (D=Debit, C=Credit) |
| 90 | BKAP_INVL_DC_19 | STRING | 1 | — | Debit/Credit flag for GL line 19 (D=Debit, C=Credit) |
| 91 | BKAP_INVL_DC_2 | STRING | 1 | — | Debit/Credit flag for GL line 2 (D=Debit, C=Credit) |
| 92 | BKAP_INVL_DC_20 | STRING | 1 | — | Debit/Credit flag for GL line 20 (D=Debit, C=Credit) |
| 93 | BKAP_INVL_DC_21 | STRING | 1 | — | Debit/Credit flag for GL line 21 (D=Debit, C=Credit) |
| 94 | BKAP_INVL_DC_22 | STRING | 1 | — | Debit/Credit flag for GL line 22 (D=Debit, C=Credit) |
| 95 | BKAP_INVL_DC_23 | STRING | 1 | — | Debit/Credit flag for GL line 23 (D=Debit, C=Credit) |
| 96 | BKAP_INVL_DC_24 | STRING | 1 | — | Debit/Credit flag for GL line 24 (D=Debit, C=Credit) |
| 97 | BKAP_INVL_DC_25 | STRING | 1 | — | Debit/Credit flag for GL line 25 (D=Debit, C=Credit) |
| 98 | BKAP_INVL_DC_26 | STRING | 1 | — | Debit/Credit flag for GL line 26 (D=Debit, C=Credit) |
| 99 | BKAP_INVL_DC_27 | STRING | 1 | — | Debit/Credit flag for GL line 27 (D=Debit, C=Credit) |
| 100 | BKAP_INVL_DC_28 | STRING | 1 | — | Debit/Credit flag for GL line 28 (D=Debit, C=Credit) |
| 101 | BKAP_INVL_DC_29 | STRING | 1 | — | Debit/Credit flag for GL line 29 (D=Debit, C=Credit) |
| 102 | BKAP_INVL_DC_3 | STRING | 1 | — | Debit/Credit flag for GL line 3 (D=Debit, C=Credit) |
| 103 | BKAP_INVL_DC_30 | STRING | 1 | — | Debit/Credit flag for GL line 30 (D=Debit, C=Credit) |
| 104 | BKAP_INVL_DC_31 | STRING | 1 | — | Debit/Credit flag for GL line 31 (D=Debit, C=Credit) |
| 105 | BKAP_INVL_DC_32 | STRING | 1 | — | Debit/Credit flag for GL line 32 (D=Debit, C=Credit) |
| 106 | BKAP_INVL_DC_33 | STRING | 1 | — | Debit/Credit flag for GL line 33 (D=Debit, C=Credit) |
| 107 | BKAP_INVL_DC_34 | STRING | 1 | — | Debit/Credit flag for GL line 34 (D=Debit, C=Credit) |
| 108 | BKAP_INVL_DC_35 | STRING | 1 | — | Debit/Credit flag for GL line 35 (D=Debit, C=Credit) |
| 109 | BKAP_INVL_DC_36 | STRING | 1 | — | Debit/Credit flag for GL line 36 (D=Debit, C=Credit) |
| 110 | BKAP_INVL_DC_37 | STRING | 1 | — | Debit/Credit flag for GL line 37 (D=Debit, C=Credit) |
| 111 | BKAP_INVL_DC_38 | STRING | 1 | — | Debit/Credit flag for GL line 38 (D=Debit, C=Credit) |
| 112 | BKAP_INVL_DC_39 | STRING | 1 | — | Debit/Credit flag for GL line 39 (D=Debit, C=Credit) |
| 113 | BKAP_INVL_DC_4 | STRING | 1 | — | Debit/Credit flag for GL line 4 (D=Debit, C=Credit) |
| 114 | BKAP_INVL_DC_40 | STRING | 1 | — | Debit/Credit flag for GL line 40 (D=Debit, C=Credit) |
| 115 | BKAP_INVL_DC_41 | STRING | 1 | — | Debit/Credit flag for GL line 41 (D=Debit, C=Credit) |
| 116 | BKAP_INVL_DC_42 | STRING | 1 | — | Debit/Credit flag for GL line 42 (D=Debit, C=Credit) |
| 117 | BKAP_INVL_DC_43 | STRING | 1 | — | Debit/Credit flag for GL line 43 (D=Debit, C=Credit) |
| 118 | BKAP_INVL_DC_44 | STRING | 1 | — | Debit/Credit flag for GL line 44 (D=Debit, C=Credit) |
| 119 | BKAP_INVL_DC_45 | STRING | 1 | — | Debit/Credit flag for GL line 45 (D=Debit, C=Credit) |
| 120 | BKAP_INVL_DC_46 | STRING | 1 | — | Debit/Credit flag for GL line 46 (D=Debit, C=Credit) |
| 121 | BKAP_INVL_DC_47 | STRING | 1 | — | Debit/Credit flag for GL line 47 (D=Debit, C=Credit) |
| 122 | BKAP_INVL_DC_48 | STRING | 1 | — | Debit/Credit flag for GL line 48 (D=Debit, C=Credit) |
| 123 | BKAP_INVL_DC_49 | STRING | 1 | — | Debit/Credit flag for GL line 49 (D=Debit, C=Credit) |
| 124 | BKAP_INVL_DC_5 | STRING | 1 | — | Debit/Credit flag for GL line 5 (D=Debit, C=Credit) |
| 125 | BKAP_INVL_DC_50 | STRING | 1 | — | Debit/Credit flag for GL line 50 (D=Debit, C=Credit) |
| 126 | BKAP_INVL_DC_51 | STRING | 1 | — | Debit/Credit flag for GL line 51 (D=Debit, C=Credit) |
| 127 | BKAP_INVL_DC_52 | STRING | 1 | — | Debit/Credit flag for GL line 52 (D=Debit, C=Credit) |
| 128 | BKAP_INVL_DC_53 | STRING | 1 | — | Debit/Credit flag for GL line 53 (D=Debit, C=Credit) |
| 129 | BKAP_INVL_DC_54 | STRING | 1 | — | Debit/Credit flag for GL line 54 (D=Debit, C=Credit) |
| 130 | BKAP_INVL_DC_55 | STRING | 1 | — | Debit/Credit flag for GL line 55 (D=Debit, C=Credit) |
| 131 | BKAP_INVL_DC_56 | STRING | 1 | — | Debit/Credit flag for GL line 56 (D=Debit, C=Credit) |
| 132 | BKAP_INVL_DC_57 | STRING | 1 | — | Debit/Credit flag for GL line 57 (D=Debit, C=Credit) |
| 133 | BKAP_INVL_DC_58 | STRING | 1 | — | Debit/Credit flag for GL line 58 (D=Debit, C=Credit) |
| 134 | BKAP_INVL_DC_59 | STRING | 1 | — | Debit/Credit flag for GL line 59 (D=Debit, C=Credit) |
| 135 | BKAP_INVL_DC_6 | STRING | 1 | — | Debit/Credit flag for GL line 6 (D=Debit, C=Credit) |
| 136 | BKAP_INVL_DC_60 | STRING | 1 | — | Debit/Credit flag for GL line 60 (D=Debit, C=Credit) |
| 137 | BKAP_INVL_DC_61 | STRING | 1 | — | Debit/Credit flag for GL line 61 (D=Debit, C=Credit) |
| 138 | BKAP_INVL_DC_62 | STRING | 1 | — | Debit/Credit flag for GL line 62 (D=Debit, C=Credit) |
| 139 | BKAP_INVL_DC_63 | STRING | 1 | — | Debit/Credit flag for GL line 63 (D=Debit, C=Credit) |
| 140 | BKAP_INVL_DC_64 | STRING | 1 | — | Debit/Credit flag for GL line 64 (D=Debit, C=Credit) |
| 141 | BKAP_INVL_DC_65 | STRING | 1 | — | Debit/Credit flag for GL line 65 (D=Debit, C=Credit) |
| 142 | BKAP_INVL_DC_66 | STRING | 1 | — | Debit/Credit flag for GL line 66 (D=Debit, C=Credit) |
| 143 | BKAP_INVL_DC_67 | STRING | 1 | — | Debit/Credit flag for GL line 67 (D=Debit, C=Credit) |
| 144 | BKAP_INVL_DC_68 | STRING | 1 | — | Debit/Credit flag for GL line 68 (D=Debit, C=Credit) |
| 145 | BKAP_INVL_DC_69 | STRING | 1 | — | Debit/Credit flag for GL line 69 (D=Debit, C=Credit) |
| 146 | BKAP_INVL_DC_7 | STRING | 1 | — | Debit/Credit flag for GL line 7 (D=Debit, C=Credit) |
| 147 | BKAP_INVL_DC_70 | STRING | 1 | — | Debit/Credit flag for GL line 70 (D=Debit, C=Credit) |
| 148 | BKAP_INVL_DC_71 | STRING | 1 | — | Debit/Credit flag for GL line 71 (D=Debit, C=Credit) |
| 149 | BKAP_INVL_DC_72 | STRING | 1 | — | Debit/Credit flag for GL line 72 (D=Debit, C=Credit) |
| 150 | BKAP_INVL_DC_73 | STRING | 1 | — | Debit/Credit flag for GL line 73 (D=Debit, C=Credit) |
| 151 | BKAP_INVL_DC_74 | STRING | 1 | — | Debit/Credit flag for GL line 74 (D=Debit, C=Credit) |
| 152 | BKAP_INVL_DC_75 | STRING | 1 | — | Debit/Credit flag for GL line 75 (D=Debit, C=Credit) |
| 153 | BKAP_INVL_DC_8 | STRING | 1 | — | Debit/Credit flag for GL line 8 (D=Debit, C=Credit) |
| 154 | BKAP_INVL_DC_9 | STRING | 1 | — | Debit/Credit flag for GL line 9 (D=Debit, C=Credit) |
| 155 | BKAP_INVL_DESC | STRING | 25 | — | Description |
| 156 | BKAP_INVL_EXTRA | STRING | 50 | — | Extra |
| 157 | BKAP_INVL_GLACT_1 | STRING | 10 | — | GL account code for distribution line 1 |
| 158 | BKAP_INVL_GLACT_10 | STRING | 10 | — | GL account code for distribution line 10 |
| 159 | BKAP_INVL_GLACT_11 | STRING | 10 | — | GL account code for distribution line 11 |
| 160 | BKAP_INVL_GLACT_12 | STRING | 10 | — | GL account code for distribution line 12 |
| 161 | BKAP_INVL_GLACT_13 | STRING | 10 | — | GL account code for distribution line 13 |
| 162 | BKAP_INVL_GLACT_14 | STRING | 10 | — | GL account code for distribution line 14 |
| 163 | BKAP_INVL_GLACT_15 | STRING | 10 | — | GL account code for distribution line 15 |
| 164 | BKAP_INVL_GLACT_16 | STRING | 10 | — | GL account code for distribution line 16 |
| 165 | BKAP_INVL_GLACT_17 | STRING | 10 | — | GL account code for distribution line 17 |
| 166 | BKAP_INVL_GLACT_18 | STRING | 10 | — | GL account code for distribution line 18 |
| 167 | BKAP_INVL_GLACT_19 | STRING | 10 | — | GL account code for distribution line 19 |
| 168 | BKAP_INVL_GLACT_2 | STRING | 10 | — | GL account code for distribution line 2 |
| 169 | BKAP_INVL_GLACT_20 | STRING | 10 | — | GL account code for distribution line 20 |
| 170 | BKAP_INVL_GLACT_21 | STRING | 10 | — | GL account code for distribution line 21 |
| 171 | BKAP_INVL_GLACT_22 | STRING | 10 | — | GL account code for distribution line 22 |
| 172 | BKAP_INVL_GLACT_23 | STRING | 10 | — | GL account code for distribution line 23 |
| 173 | BKAP_INVL_GLACT_24 | STRING | 10 | — | GL account code for distribution line 24 |
| 174 | BKAP_INVL_GLACT_25 | STRING | 10 | — | GL account code for distribution line 25 |
| 175 | BKAP_INVL_GLACT_26 | STRING | 10 | — | GL account code for distribution line 26 |
| 176 | BKAP_INVL_GLACT_27 | STRING | 10 | — | GL account code for distribution line 27 |
| 177 | BKAP_INVL_GLACT_28 | STRING | 10 | — | GL account code for distribution line 28 |
| 178 | BKAP_INVL_GLACT_29 | STRING | 10 | — | GL account code for distribution line 29 |
| 179 | BKAP_INVL_GLACT_3 | STRING | 10 | — | GL account code for distribution line 3 |
| 180 | BKAP_INVL_GLACT_30 | STRING | 10 | — | GL account code for distribution line 30 |
| 181 | BKAP_INVL_GLACT_31 | STRING | 10 | — | GL account code for distribution line 31 |
| 182 | BKAP_INVL_GLACT_32 | STRING | 10 | — | GL account code for distribution line 32 |
| 183 | BKAP_INVL_GLACT_33 | STRING | 10 | — | GL account code for distribution line 33 |
| 184 | BKAP_INVL_GLACT_34 | STRING | 10 | — | GL account code for distribution line 34 |
| 185 | BKAP_INVL_GLACT_35 | STRING | 10 | — | GL account code for distribution line 35 |
| 186 | BKAP_INVL_GLACT_36 | STRING | 10 | — | GL account code for distribution line 36 |
| 187 | BKAP_INVL_GLACT_37 | STRING | 10 | — | GL account code for distribution line 37 |
| 188 | BKAP_INVL_GLACT_38 | STRING | 10 | — | GL account code for distribution line 38 |
| 189 | BKAP_INVL_GLACT_39 | STRING | 10 | — | GL account code for distribution line 39 |
| 190 | BKAP_INVL_GLACT_4 | STRING | 10 | — | GL account code for distribution line 4 |
| 191 | BKAP_INVL_GLACT_40 | STRING | 10 | — | GL account code for distribution line 40 |
| 192 | BKAP_INVL_GLACT_41 | STRING | 10 | — | GL account code for distribution line 41 |
| 193 | BKAP_INVL_GLACT_42 | STRING | 10 | — | GL account code for distribution line 42 |
| 194 | BKAP_INVL_GLACT_43 | STRING | 10 | — | GL account code for distribution line 43 |
| 195 | BKAP_INVL_GLACT_44 | STRING | 10 | — | GL account code for distribution line 44 |
| 196 | BKAP_INVL_GLACT_45 | STRING | 10 | — | GL account code for distribution line 45 |
| 197 | BKAP_INVL_GLACT_46 | STRING | 10 | — | GL account code for distribution line 46 |
| 198 | BKAP_INVL_GLACT_47 | STRING | 10 | — | GL account code for distribution line 47 |
| 199 | BKAP_INVL_GLACT_48 | STRING | 10 | — | GL account code for distribution line 48 |
| 200 | BKAP_INVL_GLACT_49 | STRING | 10 | — | GL account code for distribution line 49 |
| 201 | BKAP_INVL_GLACT_5 | STRING | 10 | — | GL account code for distribution line 5 |
| 202 | BKAP_INVL_GLACT_50 | STRING | 10 | — | GL account code for distribution line 50 |
| 203 | BKAP_INVL_GLACT_51 | STRING | 10 | — | GL account code for distribution line 51 |
| 204 | BKAP_INVL_GLACT_52 | STRING | 10 | — | GL account code for distribution line 52 |
| 205 | BKAP_INVL_GLACT_53 | STRING | 10 | — | GL account code for distribution line 53 |
| 206 | BKAP_INVL_GLACT_54 | STRING | 10 | — | GL account code for distribution line 54 |
| 207 | BKAP_INVL_GLACT_55 | STRING | 10 | — | GL account code for distribution line 55 |
| 208 | BKAP_INVL_GLACT_56 | STRING | 10 | — | GL account code for distribution line 56 |
| 209 | BKAP_INVL_GLACT_57 | STRING | 10 | — | GL account code for distribution line 57 |
| 210 | BKAP_INVL_GLACT_58 | STRING | 10 | — | GL account code for distribution line 58 |
| 211 | BKAP_INVL_GLACT_59 | STRING | 10 | — | GL account code for distribution line 59 |
| 212 | BKAP_INVL_GLACT_6 | STRING | 10 | — | GL account code for distribution line 6 |
| 213 | BKAP_INVL_GLACT_60 | STRING | 10 | — | GL account code for distribution line 60 |
| 214 | BKAP_INVL_GLACT_61 | STRING | 10 | — | GL account code for distribution line 61 |
| 215 | BKAP_INVL_GLACT_62 | STRING | 10 | — | GL account code for distribution line 62 |
| 216 | BKAP_INVL_GLACT_63 | STRING | 10 | — | GL account code for distribution line 63 |
| 217 | BKAP_INVL_GLACT_64 | STRING | 10 | — | GL account code for distribution line 64 |
| 218 | BKAP_INVL_GLACT_65 | STRING | 10 | — | GL account code for distribution line 65 |
| 219 | BKAP_INVL_GLACT_66 | STRING | 10 | — | GL account code for distribution line 66 |
| 220 | BKAP_INVL_GLACT_67 | STRING | 10 | — | GL account code for distribution line 67 |
| 221 | BKAP_INVL_GLACT_68 | STRING | 10 | — | GL account code for distribution line 68 |
| 222 | BKAP_INVL_GLACT_69 | STRING | 10 | — | GL account code for distribution line 69 |
| 223 | BKAP_INVL_GLACT_7 | STRING | 10 | — | GL account code for distribution line 7 |
| 224 | BKAP_INVL_GLACT_70 | STRING | 10 | — | GL account code for distribution line 70 |
| 225 | BKAP_INVL_GLACT_71 | STRING | 10 | — | GL account code for distribution line 71 |
| 226 | BKAP_INVL_GLACT_72 | STRING | 10 | — | GL account code for distribution line 72 |
| 227 | BKAP_INVL_GLACT_73 | STRING | 10 | — | GL account code for distribution line 73 |
| 228 | BKAP_INVL_GLACT_74 | STRING | 10 | — | GL account code for distribution line 74 |
| 229 | BKAP_INVL_GLACT_75 | STRING | 10 | — | GL account code for distribution line 75 |
| 230 | BKAP_INVL_GLACT_8 | STRING | 10 | — | GL account code for distribution line 8 |
| 231 | BKAP_INVL_GLACT_9 | STRING | 10 | — | GL account code for distribution line 9 |
| 232 | BKAP_INVL_GLD_1 | STRING | 25 | — | GL account description for distribution line 1 |
| 233 | BKAP_INVL_GLD_10 | STRING | 25 | — | GL account description for distribution line 10 |
| 234 | BKAP_INVL_GLD_11 | STRING | 25 | — | GL account description for distribution line 11 |
| 235 | BKAP_INVL_GLD_12 | STRING | 25 | — | GL account description for distribution line 12 |
| 236 | BKAP_INVL_GLD_13 | STRING | 25 | — | GL account description for distribution line 13 |
| 237 | BKAP_INVL_GLD_14 | STRING | 25 | — | GL account description for distribution line 14 |
| 238 | BKAP_INVL_GLD_15 | STRING | 25 | — | GL account description for distribution line 15 |
| 239 | BKAP_INVL_GLD_16 | STRING | 25 | — | GL account description for distribution line 16 |
| 240 | BKAP_INVL_GLD_17 | STRING | 25 | — | GL account description for distribution line 17 |
| 241 | BKAP_INVL_GLD_18 | STRING | 25 | — | GL account description for distribution line 18 |
| 242 | BKAP_INVL_GLD_19 | STRING | 25 | — | GL account description for distribution line 19 |
| 243 | BKAP_INVL_GLD_2 | STRING | 25 | — | GL account description for distribution line 2 |
| 244 | BKAP_INVL_GLD_20 | STRING | 25 | — | GL account description for distribution line 20 |
| 245 | BKAP_INVL_GLD_21 | STRING | 25 | — | GL account description for distribution line 21 |
| 246 | BKAP_INVL_GLD_22 | STRING | 25 | — | GL account description for distribution line 22 |
| 247 | BKAP_INVL_GLD_23 | STRING | 25 | — | GL account description for distribution line 23 |
| 248 | BKAP_INVL_GLD_24 | STRING | 25 | — | GL account description for distribution line 24 |
| 249 | BKAP_INVL_GLD_25 | STRING | 25 | — | GL account description for distribution line 25 |
| 250 | BKAP_INVL_GLD_26 | STRING | 25 | — | GL account description for distribution line 26 |
| 251 | BKAP_INVL_GLD_27 | STRING | 25 | — | GL account description for distribution line 27 |
| 252 | BKAP_INVL_GLD_28 | STRING | 25 | — | GL account description for distribution line 28 |
| 253 | BKAP_INVL_GLD_29 | STRING | 25 | — | GL account description for distribution line 29 |
| 254 | BKAP_INVL_GLD_3 | STRING | 25 | — | GL account description for distribution line 3 |
| 255 | BKAP_INVL_GLD_30 | STRING | 25 | — | GL account description for distribution line 30 |
| 256 | BKAP_INVL_GLD_31 | STRING | 25 | — | GL account description for distribution line 31 |
| 257 | BKAP_INVL_GLD_32 | STRING | 25 | — | GL account description for distribution line 32 |
| 258 | BKAP_INVL_GLD_33 | STRING | 25 | — | GL account description for distribution line 33 |
| 259 | BKAP_INVL_GLD_34 | STRING | 25 | — | GL account description for distribution line 34 |
| 260 | BKAP_INVL_GLD_35 | STRING | 25 | — | GL account description for distribution line 35 |
| 261 | BKAP_INVL_GLD_36 | STRING | 25 | — | GL account description for distribution line 36 |
| 262 | BKAP_INVL_GLD_37 | STRING | 25 | — | GL account description for distribution line 37 |
| 263 | BKAP_INVL_GLD_38 | STRING | 25 | — | GL account description for distribution line 38 |
| 264 | BKAP_INVL_GLD_39 | STRING | 25 | — | GL account description for distribution line 39 |
| 265 | BKAP_INVL_GLD_4 | STRING | 25 | — | GL account description for distribution line 4 |
| 266 | BKAP_INVL_GLD_40 | STRING | 25 | — | GL account description for distribution line 40 |
| 267 | BKAP_INVL_GLD_41 | STRING | 25 | — | GL account description for distribution line 41 |
| 268 | BKAP_INVL_GLD_42 | STRING | 25 | — | GL account description for distribution line 42 |
| 269 | BKAP_INVL_GLD_43 | STRING | 25 | — | GL account description for distribution line 43 |
| 270 | BKAP_INVL_GLD_44 | STRING | 25 | — | GL account description for distribution line 44 |
| 271 | BKAP_INVL_GLD_45 | STRING | 25 | — | GL account description for distribution line 45 |
| 272 | BKAP_INVL_GLD_46 | STRING | 25 | — | GL account description for distribution line 46 |
| 273 | BKAP_INVL_GLD_47 | STRING | 25 | — | GL account description for distribution line 47 |
| 274 | BKAP_INVL_GLD_48 | STRING | 25 | — | GL account description for distribution line 48 |
| 275 | BKAP_INVL_GLD_49 | STRING | 25 | — | GL account description for distribution line 49 |
| 276 | BKAP_INVL_GLD_5 | STRING | 25 | — | GL account description for distribution line 5 |
| 277 | BKAP_INVL_GLD_50 | STRING | 25 | — | GL account description for distribution line 50 |
| 278 | BKAP_INVL_GLD_51 | STRING | 25 | — | GL account description for distribution line 51 |
| 279 | BKAP_INVL_GLD_52 | STRING | 25 | — | GL account description for distribution line 52 |
| 280 | BKAP_INVL_GLD_53 | STRING | 25 | — | GL account description for distribution line 53 |
| 281 | BKAP_INVL_GLD_54 | STRING | 25 | — | GL account description for distribution line 54 |
| 282 | BKAP_INVL_GLD_55 | STRING | 25 | — | GL account description for distribution line 55 |
| 283 | BKAP_INVL_GLD_56 | STRING | 25 | — | GL account description for distribution line 56 |
| 284 | BKAP_INVL_GLD_57 | STRING | 25 | — | GL account description for distribution line 57 |
| 285 | BKAP_INVL_GLD_58 | STRING | 25 | — | GL account description for distribution line 58 |
| 286 | BKAP_INVL_GLD_59 | STRING | 25 | — | GL account description for distribution line 59 |
| 287 | BKAP_INVL_GLD_6 | STRING | 25 | — | GL account description for distribution line 6 |
| 288 | BKAP_INVL_GLD_60 | STRING | 25 | — | GL account description for distribution line 60 |
| 289 | BKAP_INVL_GLD_61 | STRING | 25 | — | GL account description for distribution line 61 |
| 290 | BKAP_INVL_GLD_62 | STRING | 25 | — | GL account description for distribution line 62 |
| 291 | BKAP_INVL_GLD_63 | STRING | 25 | — | GL account description for distribution line 63 |
| 292 | BKAP_INVL_GLD_64 | STRING | 25 | — | GL account description for distribution line 64 |
| 293 | BKAP_INVL_GLD_65 | STRING | 25 | — | GL account description for distribution line 65 |
| 294 | BKAP_INVL_GLD_66 | STRING | 25 | — | GL account description for distribution line 66 |
| 295 | BKAP_INVL_GLD_67 | STRING | 25 | — | GL account description for distribution line 67 |
| 296 | BKAP_INVL_GLD_68 | STRING | 25 | — | GL account description for distribution line 68 |
| 297 | BKAP_INVL_GLD_69 | STRING | 25 | — | GL account description for distribution line 69 |
| 298 | BKAP_INVL_GLD_7 | STRING | 25 | — | GL account description for distribution line 7 |
| 299 | BKAP_INVL_GLD_70 | STRING | 25 | — | GL account description for distribution line 70 |
| 300 | BKAP_INVL_GLD_71 | STRING | 25 | — | GL account description for distribution line 71 |
| 301 | BKAP_INVL_GLD_72 | STRING | 25 | — | GL account description for distribution line 72 |
| 302 | BKAP_INVL_GLD_73 | STRING | 25 | — | GL account description for distribution line 73 |
| 303 | BKAP_INVL_GLD_74 | STRING | 25 | — | GL account description for distribution line 74 |
| 304 | BKAP_INVL_GLD_75 | STRING | 25 | — | GL account description for distribution line 75 |
| 305 | BKAP_INVL_GLD_8 | STRING | 25 | — | GL account description for distribution line 8 |
| 306 | BKAP_INVL_GLD_9 | STRING | 25 | — | GL account description for distribution line 9 |
| 307 | BKAP_INVL_GLDPT_1 | STRING | 4 | — | GL department for distribution line 1 |
| 308 | BKAP_INVL_GLDPT_10 | STRING | 4 | — | GL department for distribution line 10 |
| 309 | BKAP_INVL_GLDPT_11 | STRING | 4 | — | GL department for distribution line 11 |
| 310 | BKAP_INVL_GLDPT_12 | STRING | 4 | — | GL department for distribution line 12 |
| 311 | BKAP_INVL_GLDPT_13 | STRING | 4 | — | GL department for distribution line 13 |
| 312 | BKAP_INVL_GLDPT_14 | STRING | 4 | — | GL department for distribution line 14 |
| 313 | BKAP_INVL_GLDPT_15 | STRING | 4 | — | GL department for distribution line 15 |
| 314 | BKAP_INVL_GLDPT_16 | STRING | 4 | — | GL department for distribution line 16 |
| 315 | BKAP_INVL_GLDPT_17 | STRING | 4 | — | GL department for distribution line 17 |
| 316 | BKAP_INVL_GLDPT_18 | STRING | 4 | — | GL department for distribution line 18 |
| 317 | BKAP_INVL_GLDPT_19 | STRING | 4 | — | GL department for distribution line 19 |
| 318 | BKAP_INVL_GLDPT_2 | STRING | 4 | — | GL department for distribution line 2 |
| 319 | BKAP_INVL_GLDPT_20 | STRING | 4 | — | GL department for distribution line 20 |
| 320 | BKAP_INVL_GLDPT_21 | STRING | 4 | — | GL department for distribution line 21 |
| 321 | BKAP_INVL_GLDPT_22 | STRING | 4 | — | GL department for distribution line 22 |
| 322 | BKAP_INVL_GLDPT_23 | STRING | 4 | — | GL department for distribution line 23 |
| 323 | BKAP_INVL_GLDPT_24 | STRING | 4 | — | GL department for distribution line 24 |
| 324 | BKAP_INVL_GLDPT_25 | STRING | 4 | — | GL department for distribution line 25 |
| 325 | BKAP_INVL_GLDPT_26 | STRING | 4 | — | GL department for distribution line 26 |
| 326 | BKAP_INVL_GLDPT_27 | STRING | 4 | — | GL department for distribution line 27 |
| 327 | BKAP_INVL_GLDPT_28 | STRING | 4 | — | GL department for distribution line 28 |
| 328 | BKAP_INVL_GLDPT_29 | STRING | 4 | — | GL department for distribution line 29 |
| 329 | BKAP_INVL_GLDPT_3 | STRING | 4 | — | GL department for distribution line 3 |
| 330 | BKAP_INVL_GLDPT_30 | STRING | 4 | — | GL department for distribution line 30 |
| 331 | BKAP_INVL_GLDPT_31 | STRING | 4 | — | GL department for distribution line 31 |
| 332 | BKAP_INVL_GLDPT_32 | STRING | 4 | — | GL department for distribution line 32 |
| 333 | BKAP_INVL_GLDPT_33 | STRING | 4 | — | GL department for distribution line 33 |
| 334 | BKAP_INVL_GLDPT_34 | STRING | 4 | — | GL department for distribution line 34 |
| 335 | BKAP_INVL_GLDPT_35 | STRING | 4 | — | GL department for distribution line 35 |
| 336 | BKAP_INVL_GLDPT_36 | STRING | 4 | — | GL department for distribution line 36 |
| 337 | BKAP_INVL_GLDPT_37 | STRING | 4 | — | GL department for distribution line 37 |
| 338 | BKAP_INVL_GLDPT_38 | STRING | 4 | — | GL department for distribution line 38 |
| 339 | BKAP_INVL_GLDPT_39 | STRING | 4 | — | GL department for distribution line 39 |
| 340 | BKAP_INVL_GLDPT_4 | STRING | 4 | — | GL department for distribution line 4 |
| 341 | BKAP_INVL_GLDPT_40 | STRING | 4 | — | GL department for distribution line 40 |
| 342 | BKAP_INVL_GLDPT_41 | STRING | 4 | — | GL department for distribution line 41 |
| 343 | BKAP_INVL_GLDPT_42 | STRING | 4 | — | GL department for distribution line 42 |
| 344 | BKAP_INVL_GLDPT_43 | STRING | 4 | — | GL department for distribution line 43 |
| 345 | BKAP_INVL_GLDPT_44 | STRING | 4 | — | GL department for distribution line 44 |
| 346 | BKAP_INVL_GLDPT_45 | STRING | 4 | — | GL department for distribution line 45 |
| 347 | BKAP_INVL_GLDPT_46 | STRING | 4 | — | GL department for distribution line 46 |
| 348 | BKAP_INVL_GLDPT_47 | STRING | 4 | — | GL department for distribution line 47 |
| 349 | BKAP_INVL_GLDPT_48 | STRING | 4 | — | GL department for distribution line 48 |
| 350 | BKAP_INVL_GLDPT_49 | STRING | 4 | — | GL department for distribution line 49 |
| 351 | BKAP_INVL_GLDPT_5 | STRING | 4 | — | GL department for distribution line 5 |
| 352 | BKAP_INVL_GLDPT_50 | STRING | 4 | — | GL department for distribution line 50 |
| 353 | BKAP_INVL_GLDPT_51 | STRING | 4 | — | GL department for distribution line 51 |
| 354 | BKAP_INVL_GLDPT_52 | STRING | 4 | — | GL department for distribution line 52 |
| 355 | BKAP_INVL_GLDPT_53 | STRING | 4 | — | GL department for distribution line 53 |
| 356 | BKAP_INVL_GLDPT_54 | STRING | 4 | — | GL department for distribution line 54 |
| 357 | BKAP_INVL_GLDPT_55 | STRING | 4 | — | GL department for distribution line 55 |
| 358 | BKAP_INVL_GLDPT_56 | STRING | 4 | — | GL department for distribution line 56 |
| 359 | BKAP_INVL_GLDPT_57 | STRING | 4 | — | GL department for distribution line 57 |
| 360 | BKAP_INVL_GLDPT_58 | STRING | 4 | — | GL department for distribution line 58 |
| 361 | BKAP_INVL_GLDPT_59 | STRING | 4 | — | GL department for distribution line 59 |
| 362 | BKAP_INVL_GLDPT_6 | STRING | 4 | — | GL department for distribution line 6 |
| 363 | BKAP_INVL_GLDPT_60 | STRING | 4 | — | GL department for distribution line 60 |
| 364 | BKAP_INVL_GLDPT_61 | STRING | 4 | — | GL department for distribution line 61 |
| 365 | BKAP_INVL_GLDPT_62 | STRING | 4 | — | GL department for distribution line 62 |
| 366 | BKAP_INVL_GLDPT_63 | STRING | 4 | — | GL department for distribution line 63 |
| 367 | BKAP_INVL_GLDPT_64 | STRING | 4 | — | GL department for distribution line 64 |
| 368 | BKAP_INVL_GLDPT_65 | STRING | 4 | — | GL department for distribution line 65 |
| 369 | BKAP_INVL_GLDPT_66 | STRING | 4 | — | GL department for distribution line 66 |
| 370 | BKAP_INVL_GLDPT_67 | STRING | 4 | — | GL department for distribution line 67 |
| 371 | BKAP_INVL_GLDPT_68 | STRING | 4 | — | GL department for distribution line 68 |
| 372 | BKAP_INVL_GLDPT_69 | STRING | 4 | — | GL department for distribution line 69 |
| 373 | BKAP_INVL_GLDPT_7 | STRING | 4 | — | GL department for distribution line 7 |
| 374 | BKAP_INVL_GLDPT_70 | STRING | 4 | — | GL department for distribution line 70 |
| 375 | BKAP_INVL_GLDPT_71 | STRING | 4 | — | GL department for distribution line 71 |
| 376 | BKAP_INVL_GLDPT_72 | STRING | 4 | — | GL department for distribution line 72 |
| 377 | BKAP_INVL_GLDPT_73 | STRING | 4 | — | GL department for distribution line 73 |
| 378 | BKAP_INVL_GLDPT_74 | STRING | 4 | — | GL department for distribution line 74 |
| 379 | BKAP_INVL_GLDPT_75 | STRING | 4 | — | GL department for distribution line 75 |
| 380 | BKAP_INVL_GLDPT_8 | STRING | 4 | — | GL department for distribution line 8 |
| 381 | BKAP_INVL_GLDPT_9 | STRING | 4 | — | GL department for distribution line 9 |
| 382 | BKAP_INVL_ISCUR | STRING | 3 | — | Currency |
| 383 | BKAP_INVL_JOB | STRING | 15 | — | Job number linked to this voucher |
| 384 | BKAP_INVL_NUM | STRING | 10 | — | Invoice Number |
| 385 | BKAP_INVL_TAMT | NUMERIC | 8 | 2 | Tran Amount |
| 386 | BKAP_INVL_TDC | STRING | 1 | — | Tran Debit/Credit D/C |
| 387 | BKAP_INVL_TERMD | STRING | 10 | — | Terms Description |
| 388 | BKAP_INVL_TERMN | INTEGER | 2 | — | Terms Number |
| 389 | BKAP_INVL_TYPED | STRING | 10 | — | Tran.Type Description |
| 390 | BKAP_INVL_TYPEN | INTEGER | 2 | — | Tran. Type Number |

## BKAPVEND
**VENDOR MASTER**

Fields: 72

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAP_ADD1_1 | STRING | 30 | — | Address line 1 (primary/shipping) |
| 2 | BKAP_ADD1_2 | STRING | 30 | — | Address line 1 (remit-to) |
| 3 | BKAP_ADD2_1 | STRING | 30 | — | Address line 2 (primary/shipping) |
| 4 | BKAP_ADD2_2 | STRING | 30 | — | Address line 2 (remit-to) |
| 5 | BKAP_ADD3 | STRING | 30 | — | Address line 3 |
| 6 | BKAP_ALPHA1 | STRING | 25 | — | Alpha sort key 1 |
| 7 | BKAP_ALPHA2 | STRING | 25 | — | Alpha sort key 2 |
| 8 | BKAP_CITY_1 | STRING | 26 | — | City (primary/shipping) |
| 9 | BKAP_CITY_2 | STRING | 26 | — | City (remit-to) |
| 10 | BKAP_CLASS | STRING | 4 | — | Vendor Class - user defined |
| 11 | BKAP_CONTACT_1 | STRING | 30 | — | Contact name 1 |
| 12 | BKAP_CONTACT_2 | STRING | 30 | — | Contact name 2 |
| 13 | BKAP_CONTACT_3 | STRING | 30 | — | Contact name 3 |
| 14 | BKAP_CONTACT_4 | STRING | 30 | — | Contact name 4 |
| 15 | BKAP_COUNTRY_1 | STRING | 30 | — | Country (primary/shipping) |
| 16 | BKAP_COUNTRY_2 | STRING | 30 | — | Country (remit-to) |
| 17 | BKAP_CREDLIM | NUMERIC | 8 | 2 | Credit limit amount |
| 18 | BKAP_CUST_CODE | STRING | 15 | — | Cross-reference customer code (AR) |
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
| 58 | BKAP_REQQC | STRING | 1 | — | Require QC inspection Y/N |
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

## BKAPVND2
**VENDOR TAX ID**

Fields: 63

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAP2_A10_1 | STRING | 10 | — | User-defined 10-char attribute 1 |
| 2 | BKAP2_A10_2 | STRING | 10 | — | User-defined 10-char attribute 2 |
| 3 | BKAP2_A10_3 | STRING | 10 | — | User-defined 10-char attribute 3 |
| 4 | BKAP2_A10_4 | STRING | 10 | — | User-defined 10-char attribute 4 |
| 5 | BKAP2_A10_5 | STRING | 10 | — | User-defined 10-char attribute 5 |
| 6 | BKAP2_A10L_1 | STRING | 50 | — | Label for 10-char attribute 1 |
| 7 | BKAP2_A10L_2 | STRING | 50 | — | Label for 10-char attribute 2 |
| 8 | BKAP2_A10L_3 | STRING | 50 | — | Label for 10-char attribute 3 |
| 9 | BKAP2_A10L_4 | STRING | 50 | — | Label for 10-char attribute 4 |
| 10 | BKAP2_A10L_5 | STRING | 50 | — | Label for 10-char attribute 5 |
| 11 | BKAP2_A1_1 | STRING | 1 | — | User-defined 1-char flag 1 |
| 12 | BKAP2_A1_2 | STRING | 1 | — | User-defined 1-char flag 2 |
| 13 | BKAP2_A1_3 | STRING | 1 | — | User-defined 1-char flag 3 |
| 14 | BKAP2_A1_4 | STRING | 1 | — | User-defined 1-char flag 4 |
| 15 | BKAP2_A1_5 | STRING | 1 | — | User-defined 1-char flag 5 |
| 16 | BKAP2_A1L_1 | STRING | 50 | — | Label for 1-char flag 1 |
| 17 | BKAP2_A1L_2 | STRING | 50 | — | Label for 1-char flag 2 |
| 18 | BKAP2_A1L_3 | STRING | 50 | — | Label for 1-char flag 3 |
| 19 | BKAP2_A1L_4 | STRING | 50 | — | Label for 1-char flag 4 |
| 20 | BKAP2_A1L_5 | STRING | 50 | — | Label for 1-char flag 5 |
| 21 | BKAP2_A30_1 | STRING | 30 | — | User-defined 30-char attribute 1 |
| 22 | BKAP2_A30_2 | STRING | 30 | — | User-defined 30-char attribute 2 |
| 23 | BKAP2_A30_3 | STRING | 30 | — | User-defined 30-char attribute 3 |
| 24 | BKAP2_A30_4 | STRING | 30 | — | User-defined 30-char attribute 4 |
| 25 | BKAP2_A30_5 | STRING | 30 | — | User-defined 30-char attribute 5 |
| 26 | BKAP2_A30L_1 | STRING | 50 | — | Label for 30-char attribute 1 |
| 27 | BKAP2_A30L_2 | STRING | 50 | — | Label for 30-char attribute 2 |
| 28 | BKAP2_A30L_3 | STRING | 50 | — | Label for 30-char attribute 3 |
| 29 | BKAP2_A30L_4 | STRING | 50 | — | Label for 30-char attribute 4 |
| 30 | BKAP2_A30L_5 | STRING | 50 | — | Label for 30-char attribute 5 |
| 31 | BKAP2_D8_1 | DATE | 4 | — | User-defined date attribute 1 |
| 32 | BKAP2_D8_2 | DATE | 4 | — | User-defined date attribute 2 |
| 33 | BKAP2_D8_3 | DATE | 4 | — | User-defined date attribute 3 |
| 34 | BKAP2_D8_4 | DATE | 4 | — | User-defined date attribute 4 |
| 35 | BKAP2_D8_5 | DATE | 4 | — | User-defined date attribute 5 |
| 36 | BKAP2_D8L_1 | STRING | 50 | — | Label for date attribute 1 |
| 37 | BKAP2_D8L_2 | STRING | 50 | — | Label for date attribute 2 |
| 38 | BKAP2_D8L_3 | STRING | 50 | — | Label for date attribute 3 |
| 39 | BKAP2_D8L_4 | STRING | 50 | — | Label for date attribute 4 |
| 40 | BKAP2_D8L_5 | STRING | 50 | — | Label for date attribute 5 |
| 41 | BKAP2_ID | STRING | 15 | — | Tax ID Number |
| 42 | BKAP2_N12_1 | NUMERIC | 8 | 2 | User-defined amount attribute 1 |
| 43 | BKAP2_N12_2 | NUMERIC | 8 | 2 | User-defined amount attribute 2 |
| 44 | BKAP2_N12_3 | NUMERIC | 8 | 2 | User-defined amount attribute 3 |
| 45 | BKAP2_N12_4 | NUMERIC | 8 | 2 | User-defined amount attribute 4 |
| 46 | BKAP2_N12_5 | NUMERIC | 8 | 2 | User-defined amount attribute 5 |
| 47 | BKAP2_N12L_1 | STRING | 50 | — | Label for amount attribute 1 |
| 48 | BKAP2_N12L_2 | STRING | 50 | — | Label for amount attribute 2 |
| 49 | BKAP2_N12L_3 | STRING | 50 | — | Label for amount attribute 3 |
| 50 | BKAP2_N12L_4 | STRING | 50 | — | Label for amount attribute 4 |
| 51 | BKAP2_N12L_5 | STRING | 50 | — | Label for amount attribute 5 |
| 52 | BKAP2_N6_1 | NUMERIC | 8 | — | User-defined integer attribute 1 |
| 53 | BKAP2_N6_2 | NUMERIC | 8 | — | User-defined integer attribute 2 |
| 54 | BKAP2_N6_3 | NUMERIC | 8 | — | User-defined integer attribute 3 |
| 55 | BKAP2_N6_4 | NUMERIC | 8 | — | User-defined integer attribute 4 |
| 56 | BKAP2_N6_5 | NUMERIC | 8 | — | User-defined integer attribute 5 |
| 57 | BKAP2_N6L_1 | STRING | 50 | — | Label for integer attribute 1 |
| 58 | BKAP2_N6L_2 | STRING | 50 | — | Label for integer attribute 2 |
| 59 | BKAP2_N6L_3 | STRING | 50 | — | Label for integer attribute 3 |
| 60 | BKAP2_N6L_4 | STRING | 50 | — | Label for integer attribute 4 |
| 61 | BKAP2_N6L_5 | STRING | 50 | — | Label for integer attribute 5 |
| 62 | BKAP2_SEND_1099 | STRING | 1 | — | Send 199 Y/N |
| 63 | BKAP2_VENDCODE | STRING | 10 | — | Vendor Code |

## BKSYAP
**AP DEFAULT MASTER**

Fields: 11

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKSY_AP_CONVDTE | DATE | 4 | — | AP module conversion/go-live date |
| 2 | BKSY_AP_PERCOVR | NUMERIC | 8 | 3 | Percent override for discount/terms calculation |
| 3 | BKSY_AP_PONUM | NUMERIC | 8 | — | Next PO number auto-increment counter |
| 4 | BKSY_AP_QCRECV | NUMERIC | 8 | — | QC receive quantity threshold |
| 5 | BKSY_AP_RECVFLG | STRING | 1 | — | PO receipt required flag Y/N |
| 6 | BKSY_AP_RECVNUM | NUMERIC | 8 | — | Next receipt number auto-increment counter |
| 7 | BKSY_AP_REOPEN | STRING | 1 | — | Allow reopening closed vouchers Y/N |
| 8 | BKSY_AP_RFQNUM | NUMERIC | 8 | — | Next RFQ number auto-increment counter |
| 9 | BKSY_AP_RQREWRK | STRING | 1 | — | Require rework disposition Y/N |
| 10 | BKSY_AP_RQSCRAP | STRING | 1 | — | Require scrap disposition Y/N |
| 11 | BKSY_AP_VPRICE | INTEGER | 2 | — | Default vendor pricing method |

## ISAPACHK
**ARCHIVED CHECK HISTORY**

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

## ISAPAINL
**ARCHIVED AP VOUCHERS**

Fields: 390

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAP_INVL_APDPT | STRING | 4 | — | Recurring Invoice |
| 2 | BKAP_INVL_CHK | INTEGER | 2 | — | Manual Check Number |
| 3 | BKAP_INVL_CODE | STRING | 10 | — | Vendor Code |
| 4 | BKAP_INVL_DAMT_1 | NUMERIC | 8 | 2 | GL distribution amount for line 1 |
| 5 | BKAP_INVL_DAMT_10 | NUMERIC | 8 | 2 | GL distribution amount for line 10 |
| 6 | BKAP_INVL_DAMT_11 | NUMERIC | 8 | 2 | GL distribution amount for line 11 |
| 7 | BKAP_INVL_DAMT_12 | NUMERIC | 8 | 2 | GL distribution amount for line 12 |
| 8 | BKAP_INVL_DAMT_13 | NUMERIC | 8 | 2 | GL distribution amount for line 13 |
| 9 | BKAP_INVL_DAMT_14 | NUMERIC | 8 | 2 | GL distribution amount for line 14 |
| 10 | BKAP_INVL_DAMT_15 | NUMERIC | 8 | 2 | GL distribution amount for line 15 |
| 11 | BKAP_INVL_DAMT_16 | NUMERIC | 8 | 2 | GL distribution amount for line 16 |
| 12 | BKAP_INVL_DAMT_17 | NUMERIC | 8 | 2 | GL distribution amount for line 17 |
| 13 | BKAP_INVL_DAMT_18 | NUMERIC | 8 | 2 | GL distribution amount for line 18 |
| 14 | BKAP_INVL_DAMT_19 | NUMERIC | 8 | 2 | GL distribution amount for line 19 |
| 15 | BKAP_INVL_DAMT_2 | NUMERIC | 8 | 2 | GL distribution amount for line 2 |
| 16 | BKAP_INVL_DAMT_20 | NUMERIC | 8 | 2 | GL distribution amount for line 20 |
| 17 | BKAP_INVL_DAMT_21 | NUMERIC | 8 | 2 | GL distribution amount for line 21 |
| 18 | BKAP_INVL_DAMT_22 | NUMERIC | 8 | 2 | GL distribution amount for line 22 |
| 19 | BKAP_INVL_DAMT_23 | NUMERIC | 8 | 2 | GL distribution amount for line 23 |
| 20 | BKAP_INVL_DAMT_24 | NUMERIC | 8 | 2 | GL distribution amount for line 24 |
| 21 | BKAP_INVL_DAMT_25 | NUMERIC | 8 | 2 | GL distribution amount for line 25 |
| 22 | BKAP_INVL_DAMT_26 | NUMERIC | 8 | 2 | GL distribution amount for line 26 |
| 23 | BKAP_INVL_DAMT_27 | NUMERIC | 8 | 2 | GL distribution amount for line 27 |
| 24 | BKAP_INVL_DAMT_28 | NUMERIC | 8 | 2 | GL distribution amount for line 28 |
| 25 | BKAP_INVL_DAMT_29 | NUMERIC | 8 | 2 | GL distribution amount for line 29 |
| 26 | BKAP_INVL_DAMT_3 | NUMERIC | 8 | 2 | GL distribution amount for line 3 |
| 27 | BKAP_INVL_DAMT_30 | NUMERIC | 8 | 2 | GL distribution amount for line 30 |
| 28 | BKAP_INVL_DAMT_31 | NUMERIC | 8 | 2 | GL distribution amount for line 31 |
| 29 | BKAP_INVL_DAMT_32 | NUMERIC | 8 | 2 | GL distribution amount for line 32 |
| 30 | BKAP_INVL_DAMT_33 | NUMERIC | 8 | 2 | GL distribution amount for line 33 |
| 31 | BKAP_INVL_DAMT_34 | NUMERIC | 8 | 2 | GL distribution amount for line 34 |
| 32 | BKAP_INVL_DAMT_35 | NUMERIC | 8 | 2 | GL distribution amount for line 35 |
| 33 | BKAP_INVL_DAMT_36 | NUMERIC | 8 | 2 | GL distribution amount for line 36 |
| 34 | BKAP_INVL_DAMT_37 | NUMERIC | 8 | 2 | GL distribution amount for line 37 |
| 35 | BKAP_INVL_DAMT_38 | NUMERIC | 8 | 2 | GL distribution amount for line 38 |
| 36 | BKAP_INVL_DAMT_39 | NUMERIC | 8 | 2 | GL distribution amount for line 39 |
| 37 | BKAP_INVL_DAMT_4 | NUMERIC | 8 | 2 | GL distribution amount for line 4 |
| 38 | BKAP_INVL_DAMT_40 | NUMERIC | 8 | 2 | GL distribution amount for line 40 |
| 39 | BKAP_INVL_DAMT_41 | NUMERIC | 8 | 2 | GL distribution amount for line 41 |
| 40 | BKAP_INVL_DAMT_42 | NUMERIC | 8 | 2 | GL distribution amount for line 42 |
| 41 | BKAP_INVL_DAMT_43 | NUMERIC | 8 | 2 | GL distribution amount for line 43 |
| 42 | BKAP_INVL_DAMT_44 | NUMERIC | 8 | 2 | GL distribution amount for line 44 |
| 43 | BKAP_INVL_DAMT_45 | NUMERIC | 8 | 2 | GL distribution amount for line 45 |
| 44 | BKAP_INVL_DAMT_46 | NUMERIC | 8 | 2 | GL distribution amount for line 46 |
| 45 | BKAP_INVL_DAMT_47 | NUMERIC | 8 | 2 | GL distribution amount for line 47 |
| 46 | BKAP_INVL_DAMT_48 | NUMERIC | 8 | 2 | GL distribution amount for line 48 |
| 47 | BKAP_INVL_DAMT_49 | NUMERIC | 8 | 2 | GL distribution amount for line 49 |
| 48 | BKAP_INVL_DAMT_5 | NUMERIC | 8 | 2 | GL distribution amount for line 5 |
| 49 | BKAP_INVL_DAMT_50 | NUMERIC | 8 | 2 | GL distribution amount for line 50 |
| 50 | BKAP_INVL_DAMT_51 | NUMERIC | 8 | 2 | GL distribution amount for line 51 |
| 51 | BKAP_INVL_DAMT_52 | NUMERIC | 8 | 2 | GL distribution amount for line 52 |
| 52 | BKAP_INVL_DAMT_53 | NUMERIC | 8 | 2 | GL distribution amount for line 53 |
| 53 | BKAP_INVL_DAMT_54 | NUMERIC | 8 | 2 | GL distribution amount for line 54 |
| 54 | BKAP_INVL_DAMT_55 | NUMERIC | 8 | 2 | GL distribution amount for line 55 |
| 55 | BKAP_INVL_DAMT_56 | NUMERIC | 8 | 2 | GL distribution amount for line 56 |
| 56 | BKAP_INVL_DAMT_57 | NUMERIC | 8 | 2 | GL distribution amount for line 57 |
| 57 | BKAP_INVL_DAMT_58 | NUMERIC | 8 | 2 | GL distribution amount for line 58 |
| 58 | BKAP_INVL_DAMT_59 | NUMERIC | 8 | 2 | GL distribution amount for line 59 |
| 59 | BKAP_INVL_DAMT_6 | NUMERIC | 8 | 2 | GL distribution amount for line 6 |
| 60 | BKAP_INVL_DAMT_60 | NUMERIC | 8 | 2 | GL distribution amount for line 60 |
| 61 | BKAP_INVL_DAMT_61 | NUMERIC | 8 | 2 | GL distribution amount for line 61 |
| 62 | BKAP_INVL_DAMT_62 | NUMERIC | 8 | 2 | GL distribution amount for line 62 |
| 63 | BKAP_INVL_DAMT_63 | NUMERIC | 8 | 2 | GL distribution amount for line 63 |
| 64 | BKAP_INVL_DAMT_64 | NUMERIC | 8 | 2 | GL distribution amount for line 64 |
| 65 | BKAP_INVL_DAMT_65 | NUMERIC | 8 | 2 | GL distribution amount for line 65 |
| 66 | BKAP_INVL_DAMT_66 | NUMERIC | 8 | 2 | GL distribution amount for line 66 |
| 67 | BKAP_INVL_DAMT_67 | NUMERIC | 8 | 2 | GL distribution amount for line 67 |
| 68 | BKAP_INVL_DAMT_68 | NUMERIC | 8 | 2 | GL distribution amount for line 68 |
| 69 | BKAP_INVL_DAMT_69 | NUMERIC | 8 | 2 | GL distribution amount for line 69 |
| 70 | BKAP_INVL_DAMT_7 | NUMERIC | 8 | 2 | GL distribution amount for line 7 |
| 71 | BKAP_INVL_DAMT_70 | NUMERIC | 8 | 2 | GL distribution amount for line 70 |
| 72 | BKAP_INVL_DAMT_71 | NUMERIC | 8 | 2 | GL distribution amount for line 71 |
| 73 | BKAP_INVL_DAMT_72 | NUMERIC | 8 | 2 | GL distribution amount for line 72 |
| 74 | BKAP_INVL_DAMT_73 | NUMERIC | 8 | 2 | GL distribution amount for line 73 |
| 75 | BKAP_INVL_DAMT_74 | NUMERIC | 8 | 2 | GL distribution amount for line 74 |
| 76 | BKAP_INVL_DAMT_75 | NUMERIC | 8 | 2 | GL distribution amount for line 75 |
| 77 | BKAP_INVL_DAMT_8 | NUMERIC | 8 | 2 | GL distribution amount for line 8 |
| 78 | BKAP_INVL_DAMT_9 | NUMERIC | 8 | 2 | GL distribution amount for line 9 |
| 79 | BKAP_INVL_DATE | DATE | 4 | — | Invoice Date |
| 80 | BKAP_INVL_DC_1 | STRING | 1 | — | Debit/Credit flag for GL line 1 (D=Debit, C=Credit) |
| 81 | BKAP_INVL_DC_10 | STRING | 1 | — | Debit/Credit flag for GL line 10 (D=Debit, C=Credit) |
| 82 | BKAP_INVL_DC_11 | STRING | 1 | — | Debit/Credit flag for GL line 11 (D=Debit, C=Credit) |
| 83 | BKAP_INVL_DC_12 | STRING | 1 | — | Debit/Credit flag for GL line 12 (D=Debit, C=Credit) |
| 84 | BKAP_INVL_DC_13 | STRING | 1 | — | Debit/Credit flag for GL line 13 (D=Debit, C=Credit) |
| 85 | BKAP_INVL_DC_14 | STRING | 1 | — | Debit/Credit flag for GL line 14 (D=Debit, C=Credit) |
| 86 | BKAP_INVL_DC_15 | STRING | 1 | — | Debit/Credit flag for GL line 15 (D=Debit, C=Credit) |
| 87 | BKAP_INVL_DC_16 | STRING | 1 | — | Debit/Credit flag for GL line 16 (D=Debit, C=Credit) |
| 88 | BKAP_INVL_DC_17 | STRING | 1 | — | Debit/Credit flag for GL line 17 (D=Debit, C=Credit) |
| 89 | BKAP_INVL_DC_18 | STRING | 1 | — | Debit/Credit flag for GL line 18 (D=Debit, C=Credit) |
| 90 | BKAP_INVL_DC_19 | STRING | 1 | — | Debit/Credit flag for GL line 19 (D=Debit, C=Credit) |
| 91 | BKAP_INVL_DC_2 | STRING | 1 | — | Debit/Credit flag for GL line 2 (D=Debit, C=Credit) |
| 92 | BKAP_INVL_DC_20 | STRING | 1 | — | Debit/Credit flag for GL line 20 (D=Debit, C=Credit) |
| 93 | BKAP_INVL_DC_21 | STRING | 1 | — | Debit/Credit flag for GL line 21 (D=Debit, C=Credit) |
| 94 | BKAP_INVL_DC_22 | STRING | 1 | — | Debit/Credit flag for GL line 22 (D=Debit, C=Credit) |
| 95 | BKAP_INVL_DC_23 | STRING | 1 | — | Debit/Credit flag for GL line 23 (D=Debit, C=Credit) |
| 96 | BKAP_INVL_DC_24 | STRING | 1 | — | Debit/Credit flag for GL line 24 (D=Debit, C=Credit) |
| 97 | BKAP_INVL_DC_25 | STRING | 1 | — | Debit/Credit flag for GL line 25 (D=Debit, C=Credit) |
| 98 | BKAP_INVL_DC_26 | STRING | 1 | — | Debit/Credit flag for GL line 26 (D=Debit, C=Credit) |
| 99 | BKAP_INVL_DC_27 | STRING | 1 | — | Debit/Credit flag for GL line 27 (D=Debit, C=Credit) |
| 100 | BKAP_INVL_DC_28 | STRING | 1 | — | Debit/Credit flag for GL line 28 (D=Debit, C=Credit) |
| 101 | BKAP_INVL_DC_29 | STRING | 1 | — | Debit/Credit flag for GL line 29 (D=Debit, C=Credit) |
| 102 | BKAP_INVL_DC_3 | STRING | 1 | — | Debit/Credit flag for GL line 3 (D=Debit, C=Credit) |
| 103 | BKAP_INVL_DC_30 | STRING | 1 | — | Debit/Credit flag for GL line 30 (D=Debit, C=Credit) |
| 104 | BKAP_INVL_DC_31 | STRING | 1 | — | Debit/Credit flag for GL line 31 (D=Debit, C=Credit) |
| 105 | BKAP_INVL_DC_32 | STRING | 1 | — | Debit/Credit flag for GL line 32 (D=Debit, C=Credit) |
| 106 | BKAP_INVL_DC_33 | STRING | 1 | — | Debit/Credit flag for GL line 33 (D=Debit, C=Credit) |
| 107 | BKAP_INVL_DC_34 | STRING | 1 | — | Debit/Credit flag for GL line 34 (D=Debit, C=Credit) |
| 108 | BKAP_INVL_DC_35 | STRING | 1 | — | Debit/Credit flag for GL line 35 (D=Debit, C=Credit) |
| 109 | BKAP_INVL_DC_36 | STRING | 1 | — | Debit/Credit flag for GL line 36 (D=Debit, C=Credit) |
| 110 | BKAP_INVL_DC_37 | STRING | 1 | — | Debit/Credit flag for GL line 37 (D=Debit, C=Credit) |
| 111 | BKAP_INVL_DC_38 | STRING | 1 | — | Debit/Credit flag for GL line 38 (D=Debit, C=Credit) |
| 112 | BKAP_INVL_DC_39 | STRING | 1 | — | Debit/Credit flag for GL line 39 (D=Debit, C=Credit) |
| 113 | BKAP_INVL_DC_4 | STRING | 1 | — | Debit/Credit flag for GL line 4 (D=Debit, C=Credit) |
| 114 | BKAP_INVL_DC_40 | STRING | 1 | — | Debit/Credit flag for GL line 40 (D=Debit, C=Credit) |
| 115 | BKAP_INVL_DC_41 | STRING | 1 | — | Debit/Credit flag for GL line 41 (D=Debit, C=Credit) |
| 116 | BKAP_INVL_DC_42 | STRING | 1 | — | Debit/Credit flag for GL line 42 (D=Debit, C=Credit) |
| 117 | BKAP_INVL_DC_43 | STRING | 1 | — | Debit/Credit flag for GL line 43 (D=Debit, C=Credit) |
| 118 | BKAP_INVL_DC_44 | STRING | 1 | — | Debit/Credit flag for GL line 44 (D=Debit, C=Credit) |
| 119 | BKAP_INVL_DC_45 | STRING | 1 | — | Debit/Credit flag for GL line 45 (D=Debit, C=Credit) |
| 120 | BKAP_INVL_DC_46 | STRING | 1 | — | Debit/Credit flag for GL line 46 (D=Debit, C=Credit) |
| 121 | BKAP_INVL_DC_47 | STRING | 1 | — | Debit/Credit flag for GL line 47 (D=Debit, C=Credit) |
| 122 | BKAP_INVL_DC_48 | STRING | 1 | — | Debit/Credit flag for GL line 48 (D=Debit, C=Credit) |
| 123 | BKAP_INVL_DC_49 | STRING | 1 | — | Debit/Credit flag for GL line 49 (D=Debit, C=Credit) |
| 124 | BKAP_INVL_DC_5 | STRING | 1 | — | Debit/Credit flag for GL line 5 (D=Debit, C=Credit) |
| 125 | BKAP_INVL_DC_50 | STRING | 1 | — | Debit/Credit flag for GL line 50 (D=Debit, C=Credit) |
| 126 | BKAP_INVL_DC_51 | STRING | 1 | — | Debit/Credit flag for GL line 51 (D=Debit, C=Credit) |
| 127 | BKAP_INVL_DC_52 | STRING | 1 | — | Debit/Credit flag for GL line 52 (D=Debit, C=Credit) |
| 128 | BKAP_INVL_DC_53 | STRING | 1 | — | Debit/Credit flag for GL line 53 (D=Debit, C=Credit) |
| 129 | BKAP_INVL_DC_54 | STRING | 1 | — | Debit/Credit flag for GL line 54 (D=Debit, C=Credit) |
| 130 | BKAP_INVL_DC_55 | STRING | 1 | — | Debit/Credit flag for GL line 55 (D=Debit, C=Credit) |
| 131 | BKAP_INVL_DC_56 | STRING | 1 | — | Debit/Credit flag for GL line 56 (D=Debit, C=Credit) |
| 132 | BKAP_INVL_DC_57 | STRING | 1 | — | Debit/Credit flag for GL line 57 (D=Debit, C=Credit) |
| 133 | BKAP_INVL_DC_58 | STRING | 1 | — | Debit/Credit flag for GL line 58 (D=Debit, C=Credit) |
| 134 | BKAP_INVL_DC_59 | STRING | 1 | — | Debit/Credit flag for GL line 59 (D=Debit, C=Credit) |
| 135 | BKAP_INVL_DC_6 | STRING | 1 | — | Debit/Credit flag for GL line 6 (D=Debit, C=Credit) |
| 136 | BKAP_INVL_DC_60 | STRING | 1 | — | Debit/Credit flag for GL line 60 (D=Debit, C=Credit) |
| 137 | BKAP_INVL_DC_61 | STRING | 1 | — | Debit/Credit flag for GL line 61 (D=Debit, C=Credit) |
| 138 | BKAP_INVL_DC_62 | STRING | 1 | — | Debit/Credit flag for GL line 62 (D=Debit, C=Credit) |
| 139 | BKAP_INVL_DC_63 | STRING | 1 | — | Debit/Credit flag for GL line 63 (D=Debit, C=Credit) |
| 140 | BKAP_INVL_DC_64 | STRING | 1 | — | Debit/Credit flag for GL line 64 (D=Debit, C=Credit) |
| 141 | BKAP_INVL_DC_65 | STRING | 1 | — | Debit/Credit flag for GL line 65 (D=Debit, C=Credit) |
| 142 | BKAP_INVL_DC_66 | STRING | 1 | — | Debit/Credit flag for GL line 66 (D=Debit, C=Credit) |
| 143 | BKAP_INVL_DC_67 | STRING | 1 | — | Debit/Credit flag for GL line 67 (D=Debit, C=Credit) |
| 144 | BKAP_INVL_DC_68 | STRING | 1 | — | Debit/Credit flag for GL line 68 (D=Debit, C=Credit) |
| 145 | BKAP_INVL_DC_69 | STRING | 1 | — | Debit/Credit flag for GL line 69 (D=Debit, C=Credit) |
| 146 | BKAP_INVL_DC_7 | STRING | 1 | — | Debit/Credit flag for GL line 7 (D=Debit, C=Credit) |
| 147 | BKAP_INVL_DC_70 | STRING | 1 | — | Debit/Credit flag for GL line 70 (D=Debit, C=Credit) |
| 148 | BKAP_INVL_DC_71 | STRING | 1 | — | Debit/Credit flag for GL line 71 (D=Debit, C=Credit) |
| 149 | BKAP_INVL_DC_72 | STRING | 1 | — | Debit/Credit flag for GL line 72 (D=Debit, C=Credit) |
| 150 | BKAP_INVL_DC_73 | STRING | 1 | — | Debit/Credit flag for GL line 73 (D=Debit, C=Credit) |
| 151 | BKAP_INVL_DC_74 | STRING | 1 | — | Debit/Credit flag for GL line 74 (D=Debit, C=Credit) |
| 152 | BKAP_INVL_DC_75 | STRING | 1 | — | Debit/Credit flag for GL line 75 (D=Debit, C=Credit) |
| 153 | BKAP_INVL_DC_8 | STRING | 1 | — | Debit/Credit flag for GL line 8 (D=Debit, C=Credit) |
| 154 | BKAP_INVL_DC_9 | STRING | 1 | — | Debit/Credit flag for GL line 9 (D=Debit, C=Credit) |
| 155 | BKAP_INVL_DESC | STRING | 25 | — | Description |
| 156 | BKAP_INVL_EXTRA | STRING | 50 | — | Extra |
| 157 | BKAP_INVL_GLACT_1 | STRING | 10 | — | GL account code for distribution line 1 |
| 158 | BKAP_INVL_GLACT_10 | STRING | 10 | — | GL account code for distribution line 10 |
| 159 | BKAP_INVL_GLACT_11 | STRING | 10 | — | GL account code for distribution line 11 |
| 160 | BKAP_INVL_GLACT_12 | STRING | 10 | — | GL account code for distribution line 12 |
| 161 | BKAP_INVL_GLACT_13 | STRING | 10 | — | GL account code for distribution line 13 |
| 162 | BKAP_INVL_GLACT_14 | STRING | 10 | — | GL account code for distribution line 14 |
| 163 | BKAP_INVL_GLACT_15 | STRING | 10 | — | GL account code for distribution line 15 |
| 164 | BKAP_INVL_GLACT_16 | STRING | 10 | — | GL account code for distribution line 16 |
| 165 | BKAP_INVL_GLACT_17 | STRING | 10 | — | GL account code for distribution line 17 |
| 166 | BKAP_INVL_GLACT_18 | STRING | 10 | — | GL account code for distribution line 18 |
| 167 | BKAP_INVL_GLACT_19 | STRING | 10 | — | GL account code for distribution line 19 |
| 168 | BKAP_INVL_GLACT_2 | STRING | 10 | — | GL account code for distribution line 2 |
| 169 | BKAP_INVL_GLACT_20 | STRING | 10 | — | GL account code for distribution line 20 |
| 170 | BKAP_INVL_GLACT_21 | STRING | 10 | — | GL account code for distribution line 21 |
| 171 | BKAP_INVL_GLACT_22 | STRING | 10 | — | GL account code for distribution line 22 |
| 172 | BKAP_INVL_GLACT_23 | STRING | 10 | — | GL account code for distribution line 23 |
| 173 | BKAP_INVL_GLACT_24 | STRING | 10 | — | GL account code for distribution line 24 |
| 174 | BKAP_INVL_GLACT_25 | STRING | 10 | — | GL account code for distribution line 25 |
| 175 | BKAP_INVL_GLACT_26 | STRING | 10 | — | GL account code for distribution line 26 |
| 176 | BKAP_INVL_GLACT_27 | STRING | 10 | — | GL account code for distribution line 27 |
| 177 | BKAP_INVL_GLACT_28 | STRING | 10 | — | GL account code for distribution line 28 |
| 178 | BKAP_INVL_GLACT_29 | STRING | 10 | — | GL account code for distribution line 29 |
| 179 | BKAP_INVL_GLACT_3 | STRING | 10 | — | GL account code for distribution line 3 |
| 180 | BKAP_INVL_GLACT_30 | STRING | 10 | — | GL account code for distribution line 30 |
| 181 | BKAP_INVL_GLACT_31 | STRING | 10 | — | GL account code for distribution line 31 |
| 182 | BKAP_INVL_GLACT_32 | STRING | 10 | — | GL account code for distribution line 32 |
| 183 | BKAP_INVL_GLACT_33 | STRING | 10 | — | GL account code for distribution line 33 |
| 184 | BKAP_INVL_GLACT_34 | STRING | 10 | — | GL account code for distribution line 34 |
| 185 | BKAP_INVL_GLACT_35 | STRING | 10 | — | GL account code for distribution line 35 |
| 186 | BKAP_INVL_GLACT_36 | STRING | 10 | — | GL account code for distribution line 36 |
| 187 | BKAP_INVL_GLACT_37 | STRING | 10 | — | GL account code for distribution line 37 |
| 188 | BKAP_INVL_GLACT_38 | STRING | 10 | — | GL account code for distribution line 38 |
| 189 | BKAP_INVL_GLACT_39 | STRING | 10 | — | GL account code for distribution line 39 |
| 190 | BKAP_INVL_GLACT_4 | STRING | 10 | — | GL account code for distribution line 4 |
| 191 | BKAP_INVL_GLACT_40 | STRING | 10 | — | GL account code for distribution line 40 |
| 192 | BKAP_INVL_GLACT_41 | STRING | 10 | — | GL account code for distribution line 41 |
| 193 | BKAP_INVL_GLACT_42 | STRING | 10 | — | GL account code for distribution line 42 |
| 194 | BKAP_INVL_GLACT_43 | STRING | 10 | — | GL account code for distribution line 43 |
| 195 | BKAP_INVL_GLACT_44 | STRING | 10 | — | GL account code for distribution line 44 |
| 196 | BKAP_INVL_GLACT_45 | STRING | 10 | — | GL account code for distribution line 45 |
| 197 | BKAP_INVL_GLACT_46 | STRING | 10 | — | GL account code for distribution line 46 |
| 198 | BKAP_INVL_GLACT_47 | STRING | 10 | — | GL account code for distribution line 47 |
| 199 | BKAP_INVL_GLACT_48 | STRING | 10 | — | GL account code for distribution line 48 |
| 200 | BKAP_INVL_GLACT_49 | STRING | 10 | — | GL account code for distribution line 49 |
| 201 | BKAP_INVL_GLACT_5 | STRING | 10 | — | GL account code for distribution line 5 |
| 202 | BKAP_INVL_GLACT_50 | STRING | 10 | — | GL account code for distribution line 50 |
| 203 | BKAP_INVL_GLACT_51 | STRING | 10 | — | GL account code for distribution line 51 |
| 204 | BKAP_INVL_GLACT_52 | STRING | 10 | — | GL account code for distribution line 52 |
| 205 | BKAP_INVL_GLACT_53 | STRING | 10 | — | GL account code for distribution line 53 |
| 206 | BKAP_INVL_GLACT_54 | STRING | 10 | — | GL account code for distribution line 54 |
| 207 | BKAP_INVL_GLACT_55 | STRING | 10 | — | GL account code for distribution line 55 |
| 208 | BKAP_INVL_GLACT_56 | STRING | 10 | — | GL account code for distribution line 56 |
| 209 | BKAP_INVL_GLACT_57 | STRING | 10 | — | GL account code for distribution line 57 |
| 210 | BKAP_INVL_GLACT_58 | STRING | 10 | — | GL account code for distribution line 58 |
| 211 | BKAP_INVL_GLACT_59 | STRING | 10 | — | GL account code for distribution line 59 |
| 212 | BKAP_INVL_GLACT_6 | STRING | 10 | — | GL account code for distribution line 6 |
| 213 | BKAP_INVL_GLACT_60 | STRING | 10 | — | GL account code for distribution line 60 |
| 214 | BKAP_INVL_GLACT_61 | STRING | 10 | — | GL account code for distribution line 61 |
| 215 | BKAP_INVL_GLACT_62 | STRING | 10 | — | GL account code for distribution line 62 |
| 216 | BKAP_INVL_GLACT_63 | STRING | 10 | — | GL account code for distribution line 63 |
| 217 | BKAP_INVL_GLACT_64 | STRING | 10 | — | GL account code for distribution line 64 |
| 218 | BKAP_INVL_GLACT_65 | STRING | 10 | — | GL account code for distribution line 65 |
| 219 | BKAP_INVL_GLACT_66 | STRING | 10 | — | GL account code for distribution line 66 |
| 220 | BKAP_INVL_GLACT_67 | STRING | 10 | — | GL account code for distribution line 67 |
| 221 | BKAP_INVL_GLACT_68 | STRING | 10 | — | GL account code for distribution line 68 |
| 222 | BKAP_INVL_GLACT_69 | STRING | 10 | — | GL account code for distribution line 69 |
| 223 | BKAP_INVL_GLACT_7 | STRING | 10 | — | GL account code for distribution line 7 |
| 224 | BKAP_INVL_GLACT_70 | STRING | 10 | — | GL account code for distribution line 70 |
| 225 | BKAP_INVL_GLACT_71 | STRING | 10 | — | GL account code for distribution line 71 |
| 226 | BKAP_INVL_GLACT_72 | STRING | 10 | — | GL account code for distribution line 72 |
| 227 | BKAP_INVL_GLACT_73 | STRING | 10 | — | GL account code for distribution line 73 |
| 228 | BKAP_INVL_GLACT_74 | STRING | 10 | — | GL account code for distribution line 74 |
| 229 | BKAP_INVL_GLACT_75 | STRING | 10 | — | GL account code for distribution line 75 |
| 230 | BKAP_INVL_GLACT_8 | STRING | 10 | — | GL account code for distribution line 8 |
| 231 | BKAP_INVL_GLACT_9 | STRING | 10 | — | GL account code for distribution line 9 |
| 232 | BKAP_INVL_GLD_1 | STRING | 25 | — | GL account description for distribution line 1 |
| 233 | BKAP_INVL_GLD_10 | STRING | 25 | — | GL account description for distribution line 10 |
| 234 | BKAP_INVL_GLD_11 | STRING | 25 | — | GL account description for distribution line 11 |
| 235 | BKAP_INVL_GLD_12 | STRING | 25 | — | GL account description for distribution line 12 |
| 236 | BKAP_INVL_GLD_13 | STRING | 25 | — | GL account description for distribution line 13 |
| 237 | BKAP_INVL_GLD_14 | STRING | 25 | — | GL account description for distribution line 14 |
| 238 | BKAP_INVL_GLD_15 | STRING | 25 | — | GL account description for distribution line 15 |
| 239 | BKAP_INVL_GLD_16 | STRING | 25 | — | GL account description for distribution line 16 |
| 240 | BKAP_INVL_GLD_17 | STRING | 25 | — | GL account description for distribution line 17 |
| 241 | BKAP_INVL_GLD_18 | STRING | 25 | — | GL account description for distribution line 18 |
| 242 | BKAP_INVL_GLD_19 | STRING | 25 | — | GL account description for distribution line 19 |
| 243 | BKAP_INVL_GLD_2 | STRING | 25 | — | GL account description for distribution line 2 |
| 244 | BKAP_INVL_GLD_20 | STRING | 25 | — | GL account description for distribution line 20 |
| 245 | BKAP_INVL_GLD_21 | STRING | 25 | — | GL account description for distribution line 21 |
| 246 | BKAP_INVL_GLD_22 | STRING | 25 | — | GL account description for distribution line 22 |
| 247 | BKAP_INVL_GLD_23 | STRING | 25 | — | GL account description for distribution line 23 |
| 248 | BKAP_INVL_GLD_24 | STRING | 25 | — | GL account description for distribution line 24 |
| 249 | BKAP_INVL_GLD_25 | STRING | 25 | — | GL account description for distribution line 25 |
| 250 | BKAP_INVL_GLD_26 | STRING | 25 | — | GL account description for distribution line 26 |
| 251 | BKAP_INVL_GLD_27 | STRING | 25 | — | GL account description for distribution line 27 |
| 252 | BKAP_INVL_GLD_28 | STRING | 25 | — | GL account description for distribution line 28 |
| 253 | BKAP_INVL_GLD_29 | STRING | 25 | — | GL account description for distribution line 29 |
| 254 | BKAP_INVL_GLD_3 | STRING | 25 | — | GL account description for distribution line 3 |
| 255 | BKAP_INVL_GLD_30 | STRING | 25 | — | GL account description for distribution line 30 |
| 256 | BKAP_INVL_GLD_31 | STRING | 25 | — | GL account description for distribution line 31 |
| 257 | BKAP_INVL_GLD_32 | STRING | 25 | — | GL account description for distribution line 32 |
| 258 | BKAP_INVL_GLD_33 | STRING | 25 | — | GL account description for distribution line 33 |
| 259 | BKAP_INVL_GLD_34 | STRING | 25 | — | GL account description for distribution line 34 |
| 260 | BKAP_INVL_GLD_35 | STRING | 25 | — | GL account description for distribution line 35 |
| 261 | BKAP_INVL_GLD_36 | STRING | 25 | — | GL account description for distribution line 36 |
| 262 | BKAP_INVL_GLD_37 | STRING | 25 | — | GL account description for distribution line 37 |
| 263 | BKAP_INVL_GLD_38 | STRING | 25 | — | GL account description for distribution line 38 |
| 264 | BKAP_INVL_GLD_39 | STRING | 25 | — | GL account description for distribution line 39 |
| 265 | BKAP_INVL_GLD_4 | STRING | 25 | — | GL account description for distribution line 4 |
| 266 | BKAP_INVL_GLD_40 | STRING | 25 | — | GL account description for distribution line 40 |
| 267 | BKAP_INVL_GLD_41 | STRING | 25 | — | GL account description for distribution line 41 |
| 268 | BKAP_INVL_GLD_42 | STRING | 25 | — | GL account description for distribution line 42 |
| 269 | BKAP_INVL_GLD_43 | STRING | 25 | — | GL account description for distribution line 43 |
| 270 | BKAP_INVL_GLD_44 | STRING | 25 | — | GL account description for distribution line 44 |
| 271 | BKAP_INVL_GLD_45 | STRING | 25 | — | GL account description for distribution line 45 |
| 272 | BKAP_INVL_GLD_46 | STRING | 25 | — | GL account description for distribution line 46 |
| 273 | BKAP_INVL_GLD_47 | STRING | 25 | — | GL account description for distribution line 47 |
| 274 | BKAP_INVL_GLD_48 | STRING | 25 | — | GL account description for distribution line 48 |
| 275 | BKAP_INVL_GLD_49 | STRING | 25 | — | GL account description for distribution line 49 |
| 276 | BKAP_INVL_GLD_5 | STRING | 25 | — | GL account description for distribution line 5 |
| 277 | BKAP_INVL_GLD_50 | STRING | 25 | — | GL account description for distribution line 50 |
| 278 | BKAP_INVL_GLD_51 | STRING | 25 | — | GL account description for distribution line 51 |
| 279 | BKAP_INVL_GLD_52 | STRING | 25 | — | GL account description for distribution line 52 |
| 280 | BKAP_INVL_GLD_53 | STRING | 25 | — | GL account description for distribution line 53 |
| 281 | BKAP_INVL_GLD_54 | STRING | 25 | — | GL account description for distribution line 54 |
| 282 | BKAP_INVL_GLD_55 | STRING | 25 | — | GL account description for distribution line 55 |
| 283 | BKAP_INVL_GLD_56 | STRING | 25 | — | GL account description for distribution line 56 |
| 284 | BKAP_INVL_GLD_57 | STRING | 25 | — | GL account description for distribution line 57 |
| 285 | BKAP_INVL_GLD_58 | STRING | 25 | — | GL account description for distribution line 58 |
| 286 | BKAP_INVL_GLD_59 | STRING | 25 | — | GL account description for distribution line 59 |
| 287 | BKAP_INVL_GLD_6 | STRING | 25 | — | GL account description for distribution line 6 |
| 288 | BKAP_INVL_GLD_60 | STRING | 25 | — | GL account description for distribution line 60 |
| 289 | BKAP_INVL_GLD_61 | STRING | 25 | — | GL account description for distribution line 61 |
| 290 | BKAP_INVL_GLD_62 | STRING | 25 | — | GL account description for distribution line 62 |
| 291 | BKAP_INVL_GLD_63 | STRING | 25 | — | GL account description for distribution line 63 |
| 292 | BKAP_INVL_GLD_64 | STRING | 25 | — | GL account description for distribution line 64 |
| 293 | BKAP_INVL_GLD_65 | STRING | 25 | — | GL account description for distribution line 65 |
| 294 | BKAP_INVL_GLD_66 | STRING | 25 | — | GL account description for distribution line 66 |
| 295 | BKAP_INVL_GLD_67 | STRING | 25 | — | GL account description for distribution line 67 |
| 296 | BKAP_INVL_GLD_68 | STRING | 25 | — | GL account description for distribution line 68 |
| 297 | BKAP_INVL_GLD_69 | STRING | 25 | — | GL account description for distribution line 69 |
| 298 | BKAP_INVL_GLD_7 | STRING | 25 | — | GL account description for distribution line 7 |
| 299 | BKAP_INVL_GLD_70 | STRING | 25 | — | GL account description for distribution line 70 |
| 300 | BKAP_INVL_GLD_71 | STRING | 25 | — | GL account description for distribution line 71 |
| 301 | BKAP_INVL_GLD_72 | STRING | 25 | — | GL account description for distribution line 72 |
| 302 | BKAP_INVL_GLD_73 | STRING | 25 | — | GL account description for distribution line 73 |
| 303 | BKAP_INVL_GLD_74 | STRING | 25 | — | GL account description for distribution line 74 |
| 304 | BKAP_INVL_GLD_75 | STRING | 25 | — | GL account description for distribution line 75 |
| 305 | BKAP_INVL_GLD_8 | STRING | 25 | — | GL account description for distribution line 8 |
| 306 | BKAP_INVL_GLD_9 | STRING | 25 | — | GL account description for distribution line 9 |
| 307 | BKAP_INVL_GLDPT_1 | STRING | 4 | — | GL department for distribution line 1 |
| 308 | BKAP_INVL_GLDPT_10 | STRING | 4 | — | GL department for distribution line 10 |
| 309 | BKAP_INVL_GLDPT_11 | STRING | 4 | — | GL department for distribution line 11 |
| 310 | BKAP_INVL_GLDPT_12 | STRING | 4 | — | GL department for distribution line 12 |
| 311 | BKAP_INVL_GLDPT_13 | STRING | 4 | — | GL department for distribution line 13 |
| 312 | BKAP_INVL_GLDPT_14 | STRING | 4 | — | GL department for distribution line 14 |
| 313 | BKAP_INVL_GLDPT_15 | STRING | 4 | — | GL department for distribution line 15 |
| 314 | BKAP_INVL_GLDPT_16 | STRING | 4 | — | GL department for distribution line 16 |
| 315 | BKAP_INVL_GLDPT_17 | STRING | 4 | — | GL department for distribution line 17 |
| 316 | BKAP_INVL_GLDPT_18 | STRING | 4 | — | GL department for distribution line 18 |
| 317 | BKAP_INVL_GLDPT_19 | STRING | 4 | — | GL department for distribution line 19 |
| 318 | BKAP_INVL_GLDPT_2 | STRING | 4 | — | GL department for distribution line 2 |
| 319 | BKAP_INVL_GLDPT_20 | STRING | 4 | — | GL department for distribution line 20 |
| 320 | BKAP_INVL_GLDPT_21 | STRING | 4 | — | GL department for distribution line 21 |
| 321 | BKAP_INVL_GLDPT_22 | STRING | 4 | — | GL department for distribution line 22 |
| 322 | BKAP_INVL_GLDPT_23 | STRING | 4 | — | GL department for distribution line 23 |
| 323 | BKAP_INVL_GLDPT_24 | STRING | 4 | — | GL department for distribution line 24 |
| 324 | BKAP_INVL_GLDPT_25 | STRING | 4 | — | GL department for distribution line 25 |
| 325 | BKAP_INVL_GLDPT_26 | STRING | 4 | — | GL department for distribution line 26 |
| 326 | BKAP_INVL_GLDPT_27 | STRING | 4 | — | GL department for distribution line 27 |
| 327 | BKAP_INVL_GLDPT_28 | STRING | 4 | — | GL department for distribution line 28 |
| 328 | BKAP_INVL_GLDPT_29 | STRING | 4 | — | GL department for distribution line 29 |
| 329 | BKAP_INVL_GLDPT_3 | STRING | 4 | — | GL department for distribution line 3 |
| 330 | BKAP_INVL_GLDPT_30 | STRING | 4 | — | GL department for distribution line 30 |
| 331 | BKAP_INVL_GLDPT_31 | STRING | 4 | — | GL department for distribution line 31 |
| 332 | BKAP_INVL_GLDPT_32 | STRING | 4 | — | GL department for distribution line 32 |
| 333 | BKAP_INVL_GLDPT_33 | STRING | 4 | — | GL department for distribution line 33 |
| 334 | BKAP_INVL_GLDPT_34 | STRING | 4 | — | GL department for distribution line 34 |
| 335 | BKAP_INVL_GLDPT_35 | STRING | 4 | — | GL department for distribution line 35 |
| 336 | BKAP_INVL_GLDPT_36 | STRING | 4 | — | GL department for distribution line 36 |
| 337 | BKAP_INVL_GLDPT_37 | STRING | 4 | — | GL department for distribution line 37 |
| 338 | BKAP_INVL_GLDPT_38 | STRING | 4 | — | GL department for distribution line 38 |
| 339 | BKAP_INVL_GLDPT_39 | STRING | 4 | — | GL department for distribution line 39 |
| 340 | BKAP_INVL_GLDPT_4 | STRING | 4 | — | GL department for distribution line 4 |
| 341 | BKAP_INVL_GLDPT_40 | STRING | 4 | — | GL department for distribution line 40 |
| 342 | BKAP_INVL_GLDPT_41 | STRING | 4 | — | GL department for distribution line 41 |
| 343 | BKAP_INVL_GLDPT_42 | STRING | 4 | — | GL department for distribution line 42 |
| 344 | BKAP_INVL_GLDPT_43 | STRING | 4 | — | GL department for distribution line 43 |
| 345 | BKAP_INVL_GLDPT_44 | STRING | 4 | — | GL department for distribution line 44 |
| 346 | BKAP_INVL_GLDPT_45 | STRING | 4 | — | GL department for distribution line 45 |
| 347 | BKAP_INVL_GLDPT_46 | STRING | 4 | — | GL department for distribution line 46 |
| 348 | BKAP_INVL_GLDPT_47 | STRING | 4 | — | GL department for distribution line 47 |
| 349 | BKAP_INVL_GLDPT_48 | STRING | 4 | — | GL department for distribution line 48 |
| 350 | BKAP_INVL_GLDPT_49 | STRING | 4 | — | GL department for distribution line 49 |
| 351 | BKAP_INVL_GLDPT_5 | STRING | 4 | — | GL department for distribution line 5 |
| 352 | BKAP_INVL_GLDPT_50 | STRING | 4 | — | GL department for distribution line 50 |
| 353 | BKAP_INVL_GLDPT_51 | STRING | 4 | — | GL department for distribution line 51 |
| 354 | BKAP_INVL_GLDPT_52 | STRING | 4 | — | GL department for distribution line 52 |
| 355 | BKAP_INVL_GLDPT_53 | STRING | 4 | — | GL department for distribution line 53 |
| 356 | BKAP_INVL_GLDPT_54 | STRING | 4 | — | GL department for distribution line 54 |
| 357 | BKAP_INVL_GLDPT_55 | STRING | 4 | — | GL department for distribution line 55 |
| 358 | BKAP_INVL_GLDPT_56 | STRING | 4 | — | GL department for distribution line 56 |
| 359 | BKAP_INVL_GLDPT_57 | STRING | 4 | — | GL department for distribution line 57 |
| 360 | BKAP_INVL_GLDPT_58 | STRING | 4 | — | GL department for distribution line 58 |
| 361 | BKAP_INVL_GLDPT_59 | STRING | 4 | — | GL department for distribution line 59 |
| 362 | BKAP_INVL_GLDPT_6 | STRING | 4 | — | GL department for distribution line 6 |
| 363 | BKAP_INVL_GLDPT_60 | STRING | 4 | — | GL department for distribution line 60 |
| 364 | BKAP_INVL_GLDPT_61 | STRING | 4 | — | GL department for distribution line 61 |
| 365 | BKAP_INVL_GLDPT_62 | STRING | 4 | — | GL department for distribution line 62 |
| 366 | BKAP_INVL_GLDPT_63 | STRING | 4 | — | GL department for distribution line 63 |
| 367 | BKAP_INVL_GLDPT_64 | STRING | 4 | — | GL department for distribution line 64 |
| 368 | BKAP_INVL_GLDPT_65 | STRING | 4 | — | GL department for distribution line 65 |
| 369 | BKAP_INVL_GLDPT_66 | STRING | 4 | — | GL department for distribution line 66 |
| 370 | BKAP_INVL_GLDPT_67 | STRING | 4 | — | GL department for distribution line 67 |
| 371 | BKAP_INVL_GLDPT_68 | STRING | 4 | — | GL department for distribution line 68 |
| 372 | BKAP_INVL_GLDPT_69 | STRING | 4 | — | GL department for distribution line 69 |
| 373 | BKAP_INVL_GLDPT_7 | STRING | 4 | — | GL department for distribution line 7 |
| 374 | BKAP_INVL_GLDPT_70 | STRING | 4 | — | GL department for distribution line 70 |
| 375 | BKAP_INVL_GLDPT_71 | STRING | 4 | — | GL department for distribution line 71 |
| 376 | BKAP_INVL_GLDPT_72 | STRING | 4 | — | GL department for distribution line 72 |
| 377 | BKAP_INVL_GLDPT_73 | STRING | 4 | — | GL department for distribution line 73 |
| 378 | BKAP_INVL_GLDPT_74 | STRING | 4 | — | GL department for distribution line 74 |
| 379 | BKAP_INVL_GLDPT_75 | STRING | 4 | — | GL department for distribution line 75 |
| 380 | BKAP_INVL_GLDPT_8 | STRING | 4 | — | GL department for distribution line 8 |
| 381 | BKAP_INVL_GLDPT_9 | STRING | 4 | — | GL department for distribution line 9 |
| 382 | BKAP_INVL_ISCUR | STRING | 3 | — | Currency |
| 383 | BKAP_INVL_JOB | STRING | 15 | — | Job number linked to this voucher |
| 384 | BKAP_INVL_NUM | STRING | 10 | — | Invoice Number |
| 385 | BKAP_INVL_TAMT | NUMERIC | 8 | 2 | Tran Amount |
| 386 | BKAP_INVL_TDC | STRING | 1 | — | Tran Debit/Credit D/C |
| 387 | BKAP_INVL_TERMD | STRING | 10 | — | Terms Description |
| 388 | BKAP_INVL_TERMN | INTEGER | 2 | — | Terms Number |
| 389 | BKAP_INVL_TYPED | STRING | 10 | — | Tran.Type Description |
| 390 | BKAP_INVL_TYPEN | INTEGER | 2 | — | Tran. Type Number |

## ISAPAINT
**ARCHIVED AP INVOICES**

Fields: 19

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAP_INVT_AMT | NUMERIC | 8 | 2 | Amount |
| 2 | BKAP_INVT_AMTRM | NUMERIC | 8 | 2 | Amount Remaining |
| 3 | BKAP_INVT_CHKAC | INTEGER | 2 | — | Bank account number used for this check |
| 4 | BKAP_INVT_CHKNO | NUMERIC | 8 | — | Check number issued for payment |
| 5 | BKAP_INVT_CODE | STRING | 10 | — | Vendor Code |
| 6 | BKAP_INVT_DATE | DATE | 4 | — | Transaction Date |
| 7 | BKAP_INVT_DEPNO | NUMERIC | 8 | — | Deposit number |
| 8 | BKAP_INVT_DESC | STRING | 25 | — | Transaction Description |
| 9 | BKAP_INVT_EXTRA | STRING | 50 | — | Extra |
| 10 | BKAP_INVT_FRT | NUMERIC | 8 | 2 | Freight amount |
| 11 | BKAP_INVT_GLDPT | STRING | 4 | — | GL Department |
| 12 | BKAP_INVT_MCCOD | STRING | 3 | — | Currency Code |
| 13 | BKAP_INVT_MCRAT | NUMERIC | 8 | 6 | Currency Rate |
| 14 | BKAP_INVT_NUM | STRING | 10 | — | Invoice/Voucher Reference No. |
| 15 | BKAP_INVT_PDATE | DATE | 4 | — | Post Date |
| 16 | BKAP_INVT_SDATE | DATE | 4 | — | Start Date |
| 17 | BKAP_INVT_TAX | NUMERIC | 8 | 2 | Tax amount |
| 18 | BKAP_INVT_TERMN | INTEGER | 2 | — | Terms Number |
| 19 | BKAP_INVT_TYPE | STRING | 1 | — | transaction Type (IPCM) |

## ISAPAVND
**ARCHIVED VENDOR MASTER**

Fields: 72

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAP_ADD1_1 | STRING | 30 | — | Address line 1 (primary/shipping) |
| 2 | BKAP_ADD1_2 | STRING | 30 | — | Address line 1 (remit-to) |
| 3 | BKAP_ADD2_1 | STRING | 30 | — | Address line 2 (primary/shipping) |
| 4 | BKAP_ADD2_2 | STRING | 30 | — | Address line 2 (remit-to) |
| 5 | BKAP_ADD3 | STRING | 30 | — | Address line 3 |
| 6 | BKAP_ALPHA1 | STRING | 25 | — | Alpha sort key 1 |
| 7 | BKAP_ALPHA2 | STRING | 25 | — | Alpha sort key 2 |
| 8 | BKAP_CITY_1 | STRING | 26 | — | City (primary/shipping) |
| 9 | BKAP_CITY_2 | STRING | 26 | — | City (remit-to) |
| 10 | BKAP_CLASS | STRING | 4 | — | Vendor Class - user defined |
| 11 | BKAP_CONTACT_1 | STRING | 30 | — | Contact name 1 |
| 12 | BKAP_CONTACT_2 | STRING | 30 | — | Contact name 2 |
| 13 | BKAP_CONTACT_3 | STRING | 30 | — | Contact name 3 |
| 14 | BKAP_CONTACT_4 | STRING | 30 | — | Contact name 4 |
| 15 | BKAP_COUNTRY_1 | STRING | 30 | — | Country (primary/shipping) |
| 16 | BKAP_COUNTRY_2 | STRING | 30 | — | Country (remit-to) |
| 17 | BKAP_CREDLIM | NUMERIC | 8 | 2 | Credit limit amount |
| 18 | BKAP_CUST_CODE | STRING | 15 | — | Cross-reference customer code (AR) |
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
| 58 | BKAP_REQQC | STRING | 1 | — | Require QC inspection Y/N |
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

## ISAPEX
**VENDOR MASTER EXTENSION**

Fields: 33

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISAPEX_ALPHA_1 | STRING | 30 | — | User-defined text attribute 1 (30 chars) |
| 2 | ISAPEX_ALPHA_2 | STRING | 30 | — | User-defined text attribute 2 (30 chars) |
| 3 | ISAPEX_ALPHA_3 | STRING | 30 | — | User-defined text attribute 3 (30 chars) |
| 4 | ISAPEX_ALPHA_4 | STRING | 30 | — | User-defined text attribute 4 (30 chars) |
| 5 | ISAPEX_ALPHA_5 | STRING | 30 | — | User-defined text attribute 5 (30 chars) |
| 6 | ISAPEX_DATE_1 | DATE | 4 | — | User-defined date attribute 1 |
| 7 | ISAPEX_DATE_2 | DATE | 4 | — | User-defined date attribute 2 |
| 8 | ISAPEX_DATE_3 | DATE | 4 | — | User-defined date attribute 3 |
| 9 | ISAPEX_DATE_4 | DATE | 4 | — | User-defined date attribute 4 |
| 10 | ISAPEX_DATE_5 | DATE | 4 | — | User-defined date attribute 5 |
| 11 | ISAPEX_EXTRA | STRING | 100 | — | Extra/overflow text field |
| 12 | ISAPEX_FLAG_1 | STRING | 1 | — | User-defined Y/N flag 1 |
| 13 | ISAPEX_FLAG_10 | STRING | 1 | — | User-defined Y/N flag 10 |
| 14 | ISAPEX_FLAG_2 | STRING | 1 | — | User-defined Y/N flag 2 |
| 15 | ISAPEX_FLAG_3 | STRING | 1 | — | User-defined Y/N flag 3 |
| 16 | ISAPEX_FLAG_4 | STRING | 1 | — | User-defined Y/N flag 4 |
| 17 | ISAPEX_FLAG_5 | STRING | 1 | — | User-defined Y/N flag 5 |
| 18 | ISAPEX_FLAG_6 | STRING | 1 | — | User-defined Y/N flag 6 |
| 19 | ISAPEX_FLAG_7 | STRING | 1 | — | User-defined Y/N flag 7 |
| 20 | ISAPEX_FLAG_8 | STRING | 1 | — | User-defined Y/N flag 8 |
| 21 | ISAPEX_FLAG_9 | STRING | 1 | — | User-defined Y/N flag 9 |
| 22 | ISAPEX_LONGNAME | STRING | 60 | — | Extended vendor name (60 chars) |
| 23 | ISAPEX_NUM2_1 | NUMERIC | 8 | — | User-defined integer attribute 1 |
| 24 | ISAPEX_NUM2_2 | NUMERIC | 8 | — | User-defined integer attribute 2 |
| 25 | ISAPEX_NUM2_3 | NUMERIC | 8 | — | User-defined integer attribute 3 |
| 26 | ISAPEX_NUM2_4 | NUMERIC | 8 | — | User-defined integer attribute 4 |
| 27 | ISAPEX_NUM2_5 | NUMERIC | 8 | — | User-defined integer attribute 5 |
| 28 | ISAPEX_NUM_1 | NUMERIC | 8 | 2 | User-defined numeric attribute 1 |
| 29 | ISAPEX_NUM_2 | NUMERIC | 8 | 2 | User-defined numeric attribute 2 |
| 30 | ISAPEX_NUM_3 | NUMERIC | 8 | 2 | User-defined numeric attribute 3 |
| 31 | ISAPEX_NUM_4 | NUMERIC | 8 | 2 | User-defined numeric attribute 4 |
| 32 | ISAPEX_NUM_5 | NUMERIC | 8 | 2 | User-defined numeric attribute 5 |
| 33 | ISAPEX_VEND | STRING | 10 | — | Vendor code (key link to BKAPVEND) |

## ISAPPROJ
**AP LINK TO JOB**

Fields: 12

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISAP_PROJ_CUST | STRING | 10 | — | Customer code |
| 2 | ISAP_PROJ_EXTRA | STRING | 100 | — | Extra/overflow text |
| 3 | ISAP_PROJ_FROM | STRING | 3 | — | Source module/table code (3-char) |
| 4 | ISAP_PROJ_INV | STRING | 10 | — | AP invoice/voucher number |
| 5 | ISAP_PROJ_JCUST | STRING | 10 | — | Job customer code |
| 6 | ISAP_PROJ_JDEPT | STRING | 10 | — | Job department code |
| 7 | ISAP_PROJ_JITEM | STRING | 15 | — | Job item/part number |
| 8 | ISAP_PROJ_JOURN | STRING | 10 | — | Journal/transaction reference |
| 9 | ISAP_PROJ_JVEND | STRING | 10 | — | Vendor code on the job |
| 10 | ISAP_PROJ_LINE | INTEGER | 2 | — | Distribution line number |
| 11 | ISAP_PROJ_PROJ | STRING | 15 | — | Project/job number |
| 12 | ISAP_PROJ_VEND | STRING | 10 | — | Vendor code |

## ISVNDADT
**APPROVED VENDOR CONTROL**

Fields: 11

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_VND_APPROVE | STRING | 1 | — | Approved status Y/N |
| 2 | IS_VND_CHGDESC | STRING | 30 | — | Description of change/approval action |
| 3 | IS_VND_DATE | DATE | 4 | — | Date of approval change |
| 4 | IS_VND_EXTRA | STRING | 100 | — | Extra/overflow text |
| 5 | IS_VND_NMAXAMT | NUMERIC | 8 | 2 | New approved maximum order amount |
| 6 | IS_VND_NNAME | STRING | 30 | — | New vendor name after change |
| 7 | IS_VND_OMAXAMT | NUMERIC | 8 | 2 | Previous approved maximum order amount |
| 8 | IS_VND_ONAME | STRING | 30 | — | Previous vendor name before change |
| 9 | IS_VND_TIME | TIME | 4 | — | Time of approval change |
| 10 | IS_VND_VEND | STRING | 10 | — | Vendor code |
| 11 | IS_VND_WHO | STRING | 20 | — | User who made the approval change |

## MKICLASS
**AP INVOICE CROSS REFERENCE**

Fields: 3

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MKECLASS_ACTIVE | STRING | 1 | — | Active flag Y/N |
| 2 | MKECLASS_DESC | STRING | 45 | — | Class description |
| 3 | MKECLASS_NUM | NUMERIC | 8 | — | Class number (key) |
