# SH — Shipping: Field Reference

Status: verified-schema

Source: `Evo-DBA_File_Fields 052421.xlsx`, sheet "Fields".
Field descriptions where provided by source; otherwise name-inferred.

---

## BUCKETS
**FINITE SCHEDULE BUCKETS**

Fields: 14

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BUK_CNTN | NUMERIC | 8 | — | — |
| 2 | BUK_CRATIO | NUMERIC | 8 | 5 | — |
| 3 | BUK_FDATE | DATE | 4 | — | — |
| 4 | BUK_FDATE_SHOP | NUMERIC | 8 | 4 | — |
| 5 | BUK_LOCKED | STRING | 1 | — | — |
| 6 | BUK_NUM_SUNITS | NUMERIC | 8 | — | — |
| 7 | BUK_OPER | INTEGER | 2 | — | — |
| 8 | BUK_PART | STRING | 15 | — | — |
| 9 | BUK_SDATE | DATE | 4 | — | — |
| 10 | BUK_SDATE_SHOP | NUMERIC | 8 | 4 | — |
| 11 | BUK_WC | STRING | 12 | — | — |
| 12 | BUK_WCTYPE | STRING | 1 | — | — |
| 13 | BUK_WOPRE | NUMERIC | 8 | — | — |
| 14 | BUK_WOSUF | INTEGER | 2 | — | — |

## CALENDAR
**SHOP CALENDAR**

Fields: 5

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTCAL_DATE | DATE | 4 | — | — |
| 2 | MTCAL_DESC | STRING | 25 | — | — |
| 3 | MTCAL_SAT | STRING | 1 | — | — |
| 4 | MTCAL_SUN | STRING | 1 | — | — |
| 5 | MTCAL_YEAR | INTEGER | 2 | — | — |

## SCHEDCAL
**SCHEDULING SHOP CALENDAR**

Fields: 6

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | SCH_BACK_DATE | NUMERIC | 8 | — | If Holiday/WE Date is backed off one day |
| 2 | SCH_BACK_SLASH | DATE | 4 | — | Shop Back Date // back off WE/H |
| 3 | SCH_CAL_DATE | DATE | 4 | — | Date |
| 4 | SCH_SHOP_DATE | NUMERIC | 8 | — | Shop Date Julian Floating Point Date |
| 5 | SCH_SHOP_SLASH | DATE | 4 | — | Shop Date     // |
| 6 | SCH_WH_FLAG | STRING | 1 | — | Flag  H/W Holiday/Weekend |

## SCHWO
**FINITE SCHEDULING TEMP FILE**

Fields: 10

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | SWO_CONTENTION | NUMERIC | 8 | — | — |
| 2 | SWO_CRATIO | NUMERIC | 8 | 5 | Critcal Ratio |
| 3 | SWO_DAYS_TOGO | NUMERIC | 8 | — | Days Remaining |
| 4 | SWO_OPCOUNT | INTEGER | 2 | — | Operation Count |
| 5 | SWO_RUN_DAYS | NUMERIC | 8 | 4 | Run Days |
| 6 | SWO_SHOP_DUE | NUMERIC | 8 | — | — |
| 7 | SWO_SHOP_FINISH | NUMERIC | 8 | — | — |
| 8 | SWO_SHOP_START | NUMERIC | 8 | — | — |
| 9 | SWO_WOPRE | NUMERIC | 8 | — | Work Order Prefix |
| 10 | SWO_WOSUF | INTEGER | 2 | — | Work Order Suffix |

## WCCTL
**FINITE SCHEDULING TEMP FILE**

Fields: 5

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | WCTL_COUNT | NUMERIC | 8 | — | — |
| 2 | WCTL_FLAG | STRING | 1 | — | — |
| 3 | WCTL_START | NUMERIC | 8 | — | — |
| 4 | WCTL_STOP | NUMERIC | 8 | — | — |
| 5 | WCTL_WC | STRING | 12 | — | — |

## WCTRSLOD
**TEMP WORK CENTER LOAD % FOR VISUAL SCHEDULER**

Fields: 8

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | WC_LOAD_CAP | NUMERIC | 8 | 2 | — |
| 2 | WC_LOAD_DATE | DATE | 4 | — | — |
| 3 | WC_LOAD_EXTRA | STRING | 100 | — | — |
| 4 | WC_LOAD_LOAD | NUMERIC | 8 | 2 | — |
| 5 | WC_LOAD_TOTHRS | NUMERIC | 8 | 2 | — |
| 6 | WC_LOAD_UDATE | DATE | 4 | — | — |
| 7 | WC_LOAD_UTIL | NUMERIC | 8 | 2 | — |
| 8 | WC_LOAD_WC | STRING | 12 | — | — |

## WORKSORD
**TEMP WORK ORDER HEADER FOR VISUAL SCHEDULER**

Fields: 82

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTWO_CUSTCODE | STRING | 10 | — | Customer Code |
| 2 | MTWO_CUSTNAME | STRING | 25 | — | Customer Name |
| 3 | MTWO_WIP_AEXTRA | NUMERIC | 8 | 2 | — |
| 4 | MTWO_WIP_AFIN | DATE | 4 | — | Actual Finish Date |
| 5 | MTWO_WIP_AFOVHD | NUMERIC | 8 | 2 | — |
| 6 | MTWO_WIP_ALABOR | NUMERIC | 8 | 2 | Actual Labor Cost |
| 7 | MTWO_WIP_AMAT | NUMERIC | 8 | 2 | Actual Material Cost |
| 8 | MTWO_WIP_AMISC | NUMERIC | 8 | 2 | — |
| 9 | MTWO_WIP_AOTH | NUMERIC | 8 | 2 | — |
| 10 | MTWO_WIP_AOUTPR | NUMERIC | 8 | 2 | Actual Outside Process Cost |
| 11 | MTWO_WIP_ASETUP | NUMERIC | 8 | 2 | Actual Setup Cost |
| 12 | MTWO_WIP_ASTART | DATE | 4 | — | Acual Start Date |
| 13 | MTWO_WIP_ATOTAL | NUMERIC | 8 | 2 | Actaul Total Cost |
| 14 | MTWO_WIP_AVOVHD | NUMERIC | 8 | 2 | — |
| 15 | MTWO_WIP_BLANK | STRING | 1 | — | — |
| 16 | MTWO_WIP_CHGORD | INTEGER | 2 | — | — |
| 17 | MTWO_WIP_CODE | STRING | 15 | — | — |
| 18 | MTWO_WIP_COMQTY | NUMERIC | 8 | 2 | — |
| 19 | MTWO_WIP_CONTAT | STRING | 25 | — | — |
| 20 | MTWO_WIP_CUSORD | STRING | 25 | — | — |
| 21 | MTWO_WIP_DDATE | DATE | 4 | — | — |
| 22 | MTWO_WIP_DESC | STRING | 30 | — | — |
| 23 | MTWO_WIP_EEXTRA | NUMERIC | 8 | 2 | — |
| 24 | MTWO_WIP_EFOVHD | NUMERIC | 8 | 2 | — |
| 25 | MTWO_WIP_ELABOR | NUMERIC | 8 | 2 | Est. Labor Cost |
| 26 | MTWO_WIP_EMAT | NUMERIC | 8 | 2 | Est. Material Cost |
| 27 | MTWO_WIP_EMISC | NUMERIC | 8 | 2 | — |
| 28 | MTWO_WIP_EOTH | NUMERIC | 8 | 2 | — |
| 29 | MTWO_WIP_EOUTPR | NUMERIC | 8 | 2 | Est. Outside Process Cost |
| 30 | MTWO_WIP_ESETUP | NUMERIC | 8 | 2 | Est. Setup Cost |
| 31 | MTWO_WIP_EST | NUMERIC | 8 | — | — |
| 32 | MTWO_WIP_ETOT | NUMERIC | 8 | 2 | Est. Toatal Cost |
| 33 | MTWO_WIP_EXTRA^ | NUMERIC | 8 | 2 | — |
| 34 | MTWO_WIP_EXTRAV | NUMERIC | 8 | 2 | — |
| 35 | MTWO_WIP_FOVHD^ | NUMERIC | 8 | 2 | — |
| 36 | MTWO_WIP_FOVHDV | NUMERIC | 8 | 2 | — |
| 37 | MTWO_WIP_INSTR_1 | STRING | 60 | — | — |
| 38 | MTWO_WIP_INSTR_10 | STRING | 60 | — | — |
| 39 | MTWO_WIP_INSTR_2 | STRING | 60 | — | — |
| 40 | MTWO_WIP_INSTR_3 | STRING | 60 | — | — |
| 41 | MTWO_WIP_INSTR_4 | STRING | 60 | — | — |
| 42 | MTWO_WIP_INSTR_5 | STRING | 60 | — | — |
| 43 | MTWO_WIP_INSTR_6 | STRING | 60 | — | — |
| 44 | MTWO_WIP_INSTR_7 | STRING | 60 | — | — |
| 45 | MTWO_WIP_INSTR_8 | STRING | 60 | — | — |
| 46 | MTWO_WIP_INSTR_9 | STRING | 60 | — | — |
| 47 | MTWO_WIP_LABOR^ | NUMERIC | 8 | 2 | — |
| 48 | MTWO_WIP_LABORV | NUMERIC | 8 | 2 | — |
| 49 | MTWO_WIP_LOC | STRING | 10 | — | — |
| 50 | MTWO_WIP_LOCK | STRING | 1 | — | — |
| 51 | MTWO_WIP_MAT^ | NUMERIC | 8 | 2 | — |
| 52 | MTWO_WIP_MATV | NUMERIC | 8 | 2 | — |
| 53 | MTWO_WIP_MISC^ | NUMERIC | 8 | 2 | — |
| 54 | MTWO_WIP_MISCV | NUMERIC | 8 | 2 | — |
| 55 | MTWO_WIP_MULT | STRING | 1 | — | — |
| 56 | MTWO_WIP_OTHPER | NUMERIC | 8 | 2 | — |
| 57 | MTWO_WIP_OTHV | NUMERIC | 8 | 2 | — |
| 58 | MTWO_WIP_OUTPR^ | NUMERIC | 8 | 2 | — |
| 59 | MTWO_WIP_OUTPRV | NUMERIC | 8 | 2 | — |
| 60 | MTWO_WIP_PPRCE | NUMERIC | 8 | 4 | — |
| 61 | MTWO_WIP_PROJ | STRING | 15 | — | — |
| 62 | MTWO_WIP_PRTY | STRING | 1 | — | Priority |
| 63 | MTWO_WIP_QCONV | STRING | 1 | — | — |
| 64 | MTWO_WIP_SCHED_1 | STRING | 1 | — | — |
| 65 | MTWO_WIP_SCHED_2 | STRING | 1 | — | — |
| 66 | MTWO_WIP_SCONV | STRING | 1 | — | — |
| 67 | MTWO_WIP_SETUP^ | NUMERIC | 8 | 2 | — |
| 68 | MTWO_WIP_SETUPV | NUMERIC | 8 | 2 | — |
| 69 | MTWO_WIP_SFIN | DATE | 4 | — | Scheduled Finish Date |
| 70 | MTWO_WIP_SOLINE | NUMERIC | 8 | — | — |
| 71 | MTWO_WIP_SONUM | NUMERIC | 8 | — | SO Number |
| 72 | MTWO_WIP_SQTY | NUMERIC | 8 | 2 | Start Quantity |
| 73 | MTWO_WIP_SSTART | DATE | 4 | — | Scheduled Start Date |
| 74 | MTWO_WIP_STATUS | STRING | 1 | — | Status |
| 75 | MTWO_WIP_TOT^ | NUMERIC | 8 | 2 | — |
| 76 | MTWO_WIP_TOTV | NUMERIC | 8 | 2 | — |
| 77 | MTWO_WIP_USERCD | STRING | 1 | — | — |
| 78 | MTWO_WIP_VOVHD | NUMERIC | 8 | 2 | — |
| 79 | MTWO_WIP_VOVHD^ | NUMERIC | 8 | 2 | — |
| 80 | MTWO_WIP_VOVHDV | NUMERIC | 8 | 2 | — |
| 81 | MTWO_WIP_WOPRE | NUMERIC | 8 | — | WO Prefix |
| 82 | MTWO_WIP_WOSUF | INTEGER | 2 | — | WO Suffix |

## WOSROUT
**TEMP WORK ORDER ROUTING FOR VISUAL SCHEDULER**

Fields: 83

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTWORO_^COMP | INTEGER | 2 | — | — |
| 2 | MTWORO_ACTHRS | NUMERIC | 8 | 4 | — |
| 3 | MTWORO_AFOHCST | NUMERIC | 8 | 4 | — |
| 4 | MTWORO_ALABCST | NUMERIC | 8 | 4 | — |
| 5 | MTWORO_AMCHCST | NUMERIC | 8 | 4 | — |
| 6 | MTWORO_AOUTCST | NUMERIC | 8 | 4 | — |
| 7 | MTWORO_ASETCST | NUMERIC | 8 | 4 | — |
| 8 | MTWORO_ASETHRS | NUMERIC | 8 | 4 | — |
| 9 | MTWORO_AVOHCST | NUMERIC | 8 | 4 | — |
| 10 | MTWORO_CODE | STRING | 15 | — | — |
| 11 | MTWORO_CONTNTN | NUMERIC | 8 | — | — |
| 12 | MTWORO_DEPT | STRING | 3 | — | — |
| 13 | MTWORO_DESC | STRING | 30 | — | — |
| 14 | MTWORO_EFOHCST | NUMERIC | 8 | 4 | — |
| 15 | MTWORO_ELABCST | NUMERIC | 8 | 4 | — |
| 16 | MTWORO_EMCHCST | NUMERIC | 8 | 4 | — |
| 17 | MTWORO_EOUTCST | NUMERIC | 8 | 4 | — |
| 18 | MTWORO_ESETCST | NUMERIC | 8 | 4 | — |
| 19 | MTWORO_ESETHRS | NUMERIC | 8 | 4 | — |
| 20 | MTWORO_ESSTHRS | TIME | 4 | — | — |
| 21 | MTWORO_ESTHRS | NUMERIC | 8 | 4 | — |
| 22 | MTWORO_EVOHCST | NUMERIC | 8 | 4 | — |
| 23 | MTWORO_EXTRA | STRING | 150 | — | — |
| 24 | MTWORO_FINISH | DATE | 4 | — | — |
| 25 | MTWORO_FINISH2 | DATE | 4 | — | — |
| 26 | MTWORO_FINISHED | DATE | 4 | — | — |
| 27 | MTWORO_INSTR_1 | STRING | 60 | — | — |
| 28 | MTWORO_INSTR_10 | STRING | 60 | — | — |
| 29 | MTWORO_INSTR_11 | STRING | 60 | — | — |
| 30 | MTWORO_INSTR_12 | STRING | 60 | — | — |
| 31 | MTWORO_INSTR_13 | STRING | 60 | — | — |
| 32 | MTWORO_INSTR_14 | STRING | 60 | — | — |
| 33 | MTWORO_INSTR_15 | STRING | 60 | — | — |
| 34 | MTWORO_INSTR_2 | STRING | 60 | — | — |
| 35 | MTWORO_INSTR_3 | STRING | 60 | — | — |
| 36 | MTWORO_INSTR_4 | STRING | 60 | — | — |
| 37 | MTWORO_INSTR_5 | STRING | 60 | — | — |
| 38 | MTWORO_INSTR_6 | STRING | 60 | — | — |
| 39 | MTWORO_INSTR_7 | STRING | 60 | — | — |
| 40 | MTWORO_INSTR_8 | STRING | 60 | — | — |
| 41 | MTWORO_INSTR_9 | STRING | 60 | — | — |
| 42 | MTWORO_LEAD | INTEGER | 2 | — | — |
| 43 | MTWORO_LONGTIME | NUMERIC | 8 | 7 | — |
| 44 | MTWORO_MACHNO | STRING | 4 | — | — |
| 45 | MTWORO_MD_PR_HR | STRING | 1 | — | — |
| 46 | MTWORO_MIN_CHG | NUMERIC | 8 | 2 | — |
| 47 | MTWORO_MISCACST | NUMERIC | 8 | 2 | — |
| 48 | MTWORO_MISCCOST | NUMERIC | 8 | 2 | — |
| 49 | MTWORO_MISCDESC | STRING | 30 | — | — |
| 50 | MTWORO_NEGOVLP | NUMERIC | 8 | 2 | — |
| 51 | MTWORO_NUM | INTEGER | 2 | — | — |
| 52 | MTWORO_NUM_PERS | NUMERIC | 8 | 2 | — |
| 53 | MTWORO_NUM_PROC | INTEGER | 2 | — | — |
| 54 | MTWORO_OP_TEMP^ | INTEGER | 2 | — | — |
| 55 | MTWORO_OPER | INTEGER | 2 | — | — |
| 56 | MTWORO_OPER2 | INTEGER | 2 | — | — |
| 57 | MTWORO_OPERDESC | STRING | 30 | — | — |
| 58 | MTWORO_OVERLAP | INTEGER | 2 | — | — |
| 59 | MTWORO_PARTSHR | NUMERIC | 8 | 2 | — |
| 60 | MTWORO_PIECE_RT | NUMERIC | 8 | 2 | — |
| 61 | MTWORO_PO | NUMERIC | 8 | — | — |
| 62 | MTWORO_PR_PERHR | NUMERIC | 8 | 2 | — |
| 63 | MTWORO_PRINT | STRING | 1 | — | — |
| 64 | MTWORO_PRIORITY | STRING | 1 | — | — |
| 65 | MTWORO_PROJ | NUMERIC | 8 | — | — |
| 66 | MTWORO_QTYCOM | NUMERIC | 8 | 2 | — |
| 67 | MTWORO_SCHED_WC | STRING | 12 | — | — |
| 68 | MTWORO_SCRAPPED | NUMERIC | 8 | 2 | — |
| 69 | MTWORO_SQTY | NUMERIC | 8 | 2 | — |
| 70 | MTWORO_START | DATE | 4 | — | — |
| 71 | MTWORO_STARTED | DATE | 4 | — | — |
| 72 | MTWORO_STD_TIME | STRING | 1 | — | — |
| 73 | MTWORO_STQTY | NUMERIC | 8 | 2 | — |
| 74 | MTWORO_TIME_PPR | TIME | 4 | — | — |
| 75 | MTWORO_TIMEPART | TIME | 4 | — | — |
| 76 | MTWORO_TOOL | STRING | 15 | — | — |
| 77 | MTWORO_TYPE | STRING | 1 | — | — |
| 78 | MTWORO_VEND | STRING | 10 | — | — |
| 79 | MTWORO_VENDNAME | STRING | 30 | — | — |
| 80 | MTWORO_WC | STRING | 12 | — | — |
| 81 | MTWORO_WCDESC | STRING | 30 | — | — |
| 82 | MTWORO_WOPRE | NUMERIC | 8 | — | WO Prefix |
| 83 | MTWORO_WOSUF | INTEGER | 2 | — | WO Suffix |
