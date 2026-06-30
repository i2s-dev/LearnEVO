# FO — Fixed Orders: Field Reference

Status: verified-schema

Source: `Evo-DBA_File_Fields 052421.xlsx`, sheet "Fields".
Field descriptions where provided by source; otherwise name-inferred.

---

## BKFOCFG
**FEATURES & OPTIONS CONFIGURATION**

Fields: 18

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKFO_CFG_EXTRA | STRING | 50 | — | — |
| 2 | BKFO_CFG_MANFET | STRING | 1 | — | — |
| 3 | BKFO_CFG_OPCODE | STRING | 5 | — | — |
| 4 | BKFO_CFG_YN_1 | STRING | 1 | — | — |
| 5 | BKFO_CFG_YN_10 | STRING | 1 | — | — |
| 6 | BKFO_CFG_YN_11 | STRING | 1 | — | — |
| 7 | BKFO_CFG_YN_12 | STRING | 1 | — | — |
| 8 | BKFO_CFG_YN_13 | STRING | 1 | — | — |
| 9 | BKFO_CFG_YN_14 | STRING | 1 | — | — |
| 10 | BKFO_CFG_YN_15 | STRING | 1 | — | — |
| 11 | BKFO_CFG_YN_2 | STRING | 1 | — | — |
| 12 | BKFO_CFG_YN_3 | STRING | 1 | — | — |
| 13 | BKFO_CFG_YN_4 | STRING | 1 | — | — |
| 14 | BKFO_CFG_YN_5 | STRING | 1 | — | — |
| 15 | BKFO_CFG_YN_6 | STRING | 1 | — | — |
| 16 | BKFO_CFG_YN_7 | STRING | 1 | — | — |
| 17 | BKFO_CFG_YN_8 | STRING | 1 | — | — |
| 18 | BKFO_CFG_YN_9 | STRING | 1 | — | — |

## ISFOBMRM
**CONFIGURATION LINE REMARKS**

Fields: 20

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISFO_BRM_COMP | STRING | 15 | — | — |
| 2 | ISFO_BRM_EXTRA | STRING | 100 | — | — |
| 3 | ISFO_BRM_LINE | INTEGER | 2 | — | — |
| 4 | ISFO_BRM_PARENT | STRING | 15 | — | — |
| 5 | ISFO_BRM_REMARK_1 | STRING | 64 | — | — |
| 6 | ISFO_BRM_REMARK_10 | STRING | 64 | — | — |
| 7 | ISFO_BRM_REMARK_11 | STRING | 64 | — | — |
| 8 | ISFO_BRM_REMARK_12 | STRING | 64 | — | — |
| 9 | ISFO_BRM_REMARK_13 | STRING | 64 | — | — |
| 10 | ISFO_BRM_REMARK_14 | STRING | 64 | — | — |
| 11 | ISFO_BRM_REMARK_15 | STRING | 64 | — | — |
| 12 | ISFO_BRM_REMARK_2 | STRING | 64 | — | — |
| 13 | ISFO_BRM_REMARK_3 | STRING | 64 | — | — |
| 14 | ISFO_BRM_REMARK_4 | STRING | 64 | — | — |
| 15 | ISFO_BRM_REMARK_5 | STRING | 64 | — | — |
| 16 | ISFO_BRM_REMARK_6 | STRING | 64 | — | — |
| 17 | ISFO_BRM_REMARK_7 | STRING | 64 | — | — |
| 18 | ISFO_BRM_REMARK_8 | STRING | 64 | — | — |
| 19 | ISFO_BRM_REMARK_9 | STRING | 64 | — | — |
| 20 | ISFO_BRM_UID | STRING | 40 | — | — |

## ISFOHEAD
**CONGIGURATON HEADER**

Fields: 16

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISFO_HDR_CUST | STRING | 10 | — | — |
| 2 | ISFO_HDR_DATE | DATE | 4 | — | — |
| 3 | ISFO_HDR_DESC | STRING | 30 | — | — |
| 4 | ISFO_HDR_EXTRA | STRING | 150 | — | — |
| 5 | ISFO_HDR_MDATES_1 | DATE | 4 | — | — |
| 6 | ISFO_HDR_MDATES_2 | DATE | 4 | — | — |
| 7 | ISFO_HDR_MDATES_3 | DATE | 4 | — | — |
| 8 | ISFO_HDR_MDATES_4 | DATE | 4 | — | — |
| 9 | ISFO_HDR_MDATES_5 | DATE | 4 | — | — |
| 10 | ISFO_HDR_PARENT | STRING | 15 | — | — |
| 11 | ISFO_HDR_PERM | STRING | 1 | — | — |
| 12 | ISFO_HDR_REV | STRING | 5 | — | — |
| 13 | ISFO_HDR_RFQ | STRING | 20 | — | — |
| 14 | ISFO_HDR_STATUS | STRING | 15 | — | — |
| 15 | ISFO_HDR_UID | STRING | 40 | — | — |
| 16 | ISFO_HDR_VEND | STRING | 10 | — | — |

## ISFOHIST
**CONFIGURATION HISTORY**

Fields: 15

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISFO_HIST_CITEM | STRING | 15 | — | — |
| 2 | ISFO_HIST_CV | STRING | 10 | — | — |
| 3 | ISFO_HIST_CVTNO | NUMERIC | 8 | — | — |
| 4 | ISFO_HIST_CVTTO | STRING | 4 | — | — |
| 5 | ISFO_HIST_DATE | DATE | 4 | — | — |
| 6 | ISFO_HIST_DDATE | DATE | 4 | — | — |
| 7 | ISFO_HIST_EXTRA | STRING | 100 | — | — |
| 8 | ISFO_HIST_LOC | STRING | 10 | — | — |
| 9 | ISFO_HIST_PART | STRING | 15 | — | — |
| 10 | ISFO_HIST_PRICE | NUMERIC | 8 | 2 | — |
| 11 | ISFO_HIST_QTY | NUMERIC | 8 | 4 | — |
| 12 | ISFO_HIST_STATU | STRING | 40 | — | — |
| 13 | ISFO_HIST_TIME | TIME | 4 | — | — |
| 14 | ISFO_HIST_UID | STRING | 40 | — | — |
| 15 | ISFO_HIST_WHO | STRING | 20 | — | — |

## ISFOLINE
**CONFIGURATION LINES**

Fields: 78

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISFO_LIN_BEXTRA | STRING | 50 | — | — |
| 2 | ISFO_LIN_CBRANC | INTEGER | 2 | — | — |
| 3 | ISFO_LIN_COMP | STRING | 15 | — | — |
| 4 | ISFO_LIN_DATE1 | DATE | 4 | — | — |
| 5 | ISFO_LIN_DATE2 | DATE | 4 | — | — |
| 6 | ISFO_LIN_DUPOP | STRING | 1 | — | — |
| 7 | ISFO_LIN_EXTRA | STRING | 150 | — | — |
| 8 | ISFO_LIN_LEVEL | INTEGER | 2 | — | — |
| 9 | ISFO_LIN_LINEN | INTEGER | 2 | — | — |
| 10 | ISFO_LIN_OP | STRING | 3 | — | — |
| 11 | ISFO_LIN_OPDSC | STRING | 5 | — | — |
| 12 | ISFO_LIN_OPFLAG_1 | STRING | 1 | — | — |
| 13 | ISFO_LIN_OPFLAG_10 | STRING | 1 | — | — |
| 14 | ISFO_LIN_OPFLAG_11 | STRING | 1 | — | — |
| 15 | ISFO_LIN_OPFLAG_12 | STRING | 1 | — | — |
| 16 | ISFO_LIN_OPFLAG_13 | STRING | 1 | — | — |
| 17 | ISFO_LIN_OPFLAG_14 | STRING | 1 | — | — |
| 18 | ISFO_LIN_OPFLAG_15 | STRING | 1 | — | — |
| 19 | ISFO_LIN_OPFLAG_16 | STRING | 1 | — | — |
| 20 | ISFO_LIN_OPFLAG_17 | STRING | 1 | — | — |
| 21 | ISFO_LIN_OPFLAG_18 | STRING | 1 | — | — |
| 22 | ISFO_LIN_OPFLAG_19 | STRING | 1 | — | — |
| 23 | ISFO_LIN_OPFLAG_2 | STRING | 1 | — | — |
| 24 | ISFO_LIN_OPFLAG_20 | STRING | 1 | — | — |
| 25 | ISFO_LIN_OPFLAG_21 | STRING | 1 | — | — |
| 26 | ISFO_LIN_OPFLAG_22 | STRING | 1 | — | — |
| 27 | ISFO_LIN_OPFLAG_23 | STRING | 1 | — | — |
| 28 | ISFO_LIN_OPFLAG_24 | STRING | 1 | — | — |
| 29 | ISFO_LIN_OPFLAG_25 | STRING | 1 | — | — |
| 30 | ISFO_LIN_OPFLAG_26 | STRING | 1 | — | — |
| 31 | ISFO_LIN_OPFLAG_27 | STRING | 1 | — | — |
| 32 | ISFO_LIN_OPFLAG_28 | STRING | 1 | — | — |
| 33 | ISFO_LIN_OPFLAG_29 | STRING | 1 | — | — |
| 34 | ISFO_LIN_OPFLAG_3 | STRING | 1 | — | — |
| 35 | ISFO_LIN_OPFLAG_30 | STRING | 1 | — | — |
| 36 | ISFO_LIN_OPFLAG_31 | STRING | 1 | — | — |
| 37 | ISFO_LIN_OPFLAG_32 | STRING | 1 | — | — |
| 38 | ISFO_LIN_OPFLAG_33 | STRING | 1 | — | — |
| 39 | ISFO_LIN_OPFLAG_34 | STRING | 1 | — | — |
| 40 | ISFO_LIN_OPFLAG_35 | STRING | 1 | — | — |
| 41 | ISFO_LIN_OPFLAG_36 | STRING | 1 | — | — |
| 42 | ISFO_LIN_OPFLAG_37 | STRING | 1 | — | — |
| 43 | ISFO_LIN_OPFLAG_38 | STRING | 1 | — | — |
| 44 | ISFO_LIN_OPFLAG_39 | STRING | 1 | — | — |
| 45 | ISFO_LIN_OPFLAG_4 | STRING | 1 | — | — |
| 46 | ISFO_LIN_OPFLAG_40 | STRING | 1 | — | — |
| 47 | ISFO_LIN_OPFLAG_41 | STRING | 1 | — | — |
| 48 | ISFO_LIN_OPFLAG_42 | STRING | 1 | — | — |
| 49 | ISFO_LIN_OPFLAG_43 | STRING | 1 | — | — |
| 50 | ISFO_LIN_OPFLAG_44 | STRING | 1 | — | — |
| 51 | ISFO_LIN_OPFLAG_45 | STRING | 1 | — | — |
| 52 | ISFO_LIN_OPFLAG_46 | STRING | 1 | — | — |
| 53 | ISFO_LIN_OPFLAG_47 | STRING | 1 | — | — |
| 54 | ISFO_LIN_OPFLAG_48 | STRING | 1 | — | — |
| 55 | ISFO_LIN_OPFLAG_49 | STRING | 1 | — | — |
| 56 | ISFO_LIN_OPFLAG_5 | STRING | 1 | — | — |
| 57 | ISFO_LIN_OPFLAG_50 | STRING | 1 | — | — |
| 58 | ISFO_LIN_OPFLAG_6 | STRING | 1 | — | — |
| 59 | ISFO_LIN_OPFLAG_7 | STRING | 1 | — | — |
| 60 | ISFO_LIN_OPFLAG_8 | STRING | 1 | — | — |
| 61 | ISFO_LIN_OPFLAG_9 | STRING | 1 | — | — |
| 62 | ISFO_LIN_OPYN_1 | STRING | 1 | — | — |
| 63 | ISFO_LIN_OPYN_2 | STRING | 1 | — | — |
| 64 | ISFO_LIN_OPYN_3 | STRING | 1 | — | — |
| 65 | ISFO_LIN_OPYN_4 | STRING | 1 | — | — |
| 66 | ISFO_LIN_OPYN_5 | STRING | 1 | — | — |
| 67 | ISFO_LIN_OPYN_6 | STRING | 1 | — | — |
| 68 | ISFO_LIN_PARENT | STRING | 15 | — | — |
| 69 | ISFO_LIN_PBRANC | INTEGER | 2 | — | — |
| 70 | ISFO_LIN_PRICE | NUMERIC | 8 | 4 | — |
| 71 | ISFO_LIN_QTYREQ | NUMERIC | 8 | 8 | — |
| 72 | ISFO_LIN_REF | STRING | 20 | — | — |
| 73 | ISFO_LIN_REV | STRING | 5 | — | — |
| 74 | ISFO_LIN_RTNUM | INTEGER | 2 | — | — |
| 75 | ISFO_LIN_SCRAP | NUMERIC | 8 | 2 | — |
| 76 | ISFO_LIN_TYPE | STRING | 1 | — | — |
| 77 | ISFO_LIN_UID | STRING | 40 | — | — |
| 78 | ISFO_LIN_VEND | STRING | 10 | — | — |

## ISFOORDL
**CONFIGURATION ORDER LINE CONVERSION**

Fields: 18

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISFO_ORDL_DRAW | STRING | 15 | — | — |
| 2 | ISFO_ORDL_ESD | DATE | 4 | — | — |
| 3 | ISFO_ORDL_EXTRA | STRING | 100 | — | — |
| 4 | ISFO_ORDL_LINE | INTEGER | 2 | — | — |
| 5 | ISFO_ORDL_LN | STRING | 3 | — | — |
| 6 | ISFO_ORDL_LOC | STRING | 10 | — | — |
| 7 | ISFO_ORDL_OUID | NUMERIC | 8 | 4 | — |
| 8 | ISFO_ORDL_PCODE | STRING | 15 | — | — |
| 9 | ISFO_ORDL_PDESC | STRING | 30 | — | — |
| 10 | ISFO_ORDL_PDISC | NUMERIC | 8 | 2 | — |
| 11 | ISFO_ORDL_PEXT | NUMERIC | 8 | 2 | — |
| 12 | ISFO_ORDL_PPRCE | NUMERIC | 8 | 4 | — |
| 13 | ISFO_ORDL_PQTY | NUMERIC | 8 | 2 | — |
| 14 | ISFO_ORDL_REV | STRING | 5 | — | — |
| 15 | ISFO_ORDL_TXBLE | STRING | 1 | — | — |
| 16 | ISFO_ORDL_TYPE | STRING | 6 | — | — |
| 17 | ISFO_ORDL_UID | STRING | 40 | — | — |
| 18 | ISFO_ORDL_UM | STRING | 3 | — | — |
