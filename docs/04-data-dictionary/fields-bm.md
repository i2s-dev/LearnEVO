# BM — Bill of Materials: Field Reference

Status: verified-schema

Source: `Evo-DBA_File_Fields 052421.xlsx`, sheet "Fields".
Field descriptions where provided by source; otherwise name-inferred.

---

## BKBMAMTR
**ARCHIVED BOM**

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

## BKBMAVAL
**TEMP FILE USED BY BOM AVAILABILITY REPORT**

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

## BKBMMSTR
**BOM  MASTER**

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

## BKBMNOTE
**BOM NOTES**

Fields: 16

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKBM_NT_NOTE_1 | STRING | 64 | — | — |
| 2 | BKBM_NT_NOTE_10 | STRING | 64 | — | — |
| 3 | BKBM_NT_NOTE_11 | STRING | 64 | — | — |
| 4 | BKBM_NT_NOTE_12 | STRING | 64 | — | — |
| 5 | BKBM_NT_NOTE_13 | STRING | 64 | — | — |
| 6 | BKBM_NT_NOTE_14 | STRING | 64 | — | — |
| 7 | BKBM_NT_NOTE_15 | STRING | 64 | — | — |
| 8 | BKBM_NT_NOTE_2 | STRING | 64 | — | — |
| 9 | BKBM_NT_NOTE_3 | STRING | 64 | — | — |
| 10 | BKBM_NT_NOTE_4 | STRING | 64 | — | — |
| 11 | BKBM_NT_NOTE_5 | STRING | 64 | — | — |
| 12 | BKBM_NT_NOTE_6 | STRING | 64 | — | — |
| 13 | BKBM_NT_NOTE_7 | STRING | 64 | — | — |
| 14 | BKBM_NT_NOTE_8 | STRING | 64 | — | — |
| 15 | BKBM_NT_NOTE_9 | STRING | 64 | — | — |
| 16 | BKBM_NT_PARENT | STRING | 15 | — | Parent Part Code |

## BKBMREMK
**BOM REMARKS**

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

## BKBMSUMM
**TEMP FILE FOR SUMMARIZED BOM**

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

## BKSBMFG
**APPROVED MANUFACTURERS**

Fields: 6

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKSB_MFG_CUST | STRING | 10 | — | — |
| 2 | BKSB_MFG_EXTRA | STRING | 50 | — | — |
| 3 | BKSB_MFG_MANUF | STRING | 25 | — | — |
| 4 | BKSB_MFG_MPART | STRING | 25 | — | — |
| 5 | BKSB_MFG_PARNT | STRING | 15 | — | — |
| 6 | BKSB_MFG_PROD | STRING | 15 | — | — |

## BKSBPART
**APPROVED SUBSTITUTE PARTS**

Fields: 5

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKSB_PART_CUST | STRING | 10 | — | — |
| 2 | BKSB_PART_EXTRA | STRING | 50 | — | — |
| 3 | BKSB_PART_PARNT | STRING | 15 | — | — |
| 4 | BKSB_PART_PROD | STRING | 15 | — | — |
| 5 | BKSB_PART_SUBST | STRING | 15 | — | — |

## BKSBVEND
**APPROVED VENDORS**

Fields: 6

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKSB_VEND_CUST | STRING | 10 | — | — |
| 2 | BKSB_VEND_EXTRA | STRING | 50 | — | — |
| 3 | BKSB_VEND_PARNT | STRING | 15 | — | — |
| 4 | BKSB_VEND_PROD | STRING | 15 | — | — |
| 5 | BKSB_VEND_VEND | STRING | 10 | — | — |
| 6 | BKSB_VEND_VPART | STRING | 25 | — | — |
