# RO — Receivable Other: Field Reference

Status: verified-schema

Source: `Evo-DBA_File_Fields 052421.xlsx`, sheet "Fields".
Field descriptions where provided by source; otherwise name-inferred.

---

## BKRTCST
**ROUTING COSTS**

Fields: 24

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKRT_CODE | STRING | 15 | — | — |
| 2 | BKRT_DATE | DATE | 4 | — | — |
| 3 | BKRT_OPER | INTEGER | 2 | — | — |
| 4 | BKRT_PARTSHR_1 | NUMERIC | 8 | 2 | — |
| 5 | BKRT_PARTSHR_10 | NUMERIC | 8 | 2 | — |
| 6 | BKRT_PARTSHR_2 | NUMERIC | 8 | 2 | — |
| 7 | BKRT_PARTSHR_3 | NUMERIC | 8 | 2 | — |
| 8 | BKRT_PARTSHR_4 | NUMERIC | 8 | 2 | — |
| 9 | BKRT_PARTSHR_5 | NUMERIC | 8 | 2 | — |
| 10 | BKRT_PARTSHR_6 | NUMERIC | 8 | 2 | — |
| 11 | BKRT_PARTSHR_7 | NUMERIC | 8 | 2 | — |
| 12 | BKRT_PARTSHR_8 | NUMERIC | 8 | 2 | — |
| 13 | BKRT_PARTSHR_9 | NUMERIC | 8 | 2 | — |
| 14 | BKRT_QUOTE | NUMERIC | 8 | — | — |
| 15 | BKRT_SETUP_1 | TIME | 4 | — | — |
| 16 | BKRT_SETUP_10 | TIME | 4 | — | — |
| 17 | BKRT_SETUP_2 | TIME | 4 | — | — |
| 18 | BKRT_SETUP_3 | TIME | 4 | — | — |
| 19 | BKRT_SETUP_4 | TIME | 4 | — | — |
| 20 | BKRT_SETUP_5 | TIME | 4 | — | — |
| 21 | BKRT_SETUP_6 | TIME | 4 | — | — |
| 22 | BKRT_SETUP_7 | TIME | 4 | — | — |
| 23 | BKRT_SETUP_8 | TIME | 4 | — | — |
| 24 | BKRT_SETUP_9 | TIME | 4 | — | — |

## BKRTSPEC
**ROUTING SPECIFICATIONS**

Fields: 7

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKRT_SPEC_LINE | INTEGER | 2 | — | Line Number |
| 2 | BKRT_SPEC_NOTE_1 | STRING | 20 | — | — |
| 3 | BKRT_SPEC_NOTE_2 | STRING | 20 | — | — |
| 4 | BKRT_SPEC_NOTE_3 | STRING | 20 | — | — |
| 5 | BKRT_SPEC_NOTE_4 | STRING | 20 | — | — |
| 6 | BKRT_SPEC_PART | STRING | 15 | — | Item Number |
| 7 | BKRT_SPEC_SEQ | INTEGER | 2 | — | Sequence |

## BKRTTEMP
**SPECIFICATION TEMPLATES**

Fields: 6

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKRT_TEMP_CODE | STRING | 15 | — | Item Number |
| 2 | BKRT_TEMP_LINE | INTEGER | 2 | — | Line Number |
| 3 | BKRT_TEMP_NOTE_1 | STRING | 20 | — | — |
| 4 | BKRT_TEMP_NOTE_2 | STRING | 20 | — | — |
| 5 | BKRT_TEMP_NOTE_3 | STRING | 20 | — | — |
| 6 | BKRT_TEMP_NOTE_4 | STRING | 20 | — | — |

## DPTMENT
**DEPARTMENTS**

Fields: 2

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | DPT_CODE | STRING | 4 | — | — |
| 2 | DPT_DESC | STRING | 30 | — | — |

## MACHINE
**MACHINES**

Fields: 20

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | TMACH_ACTIVE | STRING | 1 | — | — |
| 2 | TMACH_DATE | DATE | 4 | — | — |
| 3 | TMACH_DESC | STRING | 30 | — | — |
| 4 | TMACH_EXTRA | STRING | 100 | — | — |
| 5 | TMACH_HRSMAINT | NUMERIC | 8 | — | — |
| 6 | TMACH_HRSUSED | NUMERIC | 8 | — | — |
| 7 | TMACH_INACTDATE | DATE | 4 | — | — |
| 8 | TMACH_INACTWHO | STRING | 30 | — | — |
| 9 | TMACH_INACTWHY | STRING | 60 | — | — |
| 10 | TMACH_MACHINE | STRING | 4 | — | — |
| 11 | TMACH_NOTES_1 | STRING | 45 | — | — |
| 12 | TMACH_NOTES_2 | STRING | 45 | — | — |
| 13 | TMACH_NOTES_3 | STRING | 45 | — | — |
| 14 | TMACH_NOTES_4 | STRING | 45 | — | — |
| 15 | TMACH_NOTES_5 | STRING | 45 | — | — |
| 16 | TMACH_NOTES_6 | STRING | 45 | — | — |
| 17 | TMACH_NOTES_7 | STRING | 45 | — | — |
| 18 | TMACH_NOTES_8 | STRING | 45 | — | — |
| 19 | TMACH_WC | STRING | 12 | — | — |
| 20 | TMACH_WCDESC | STRING | 30 | — | — |

## ROCHG
**ROUTING CHANGES (NOT USED)**

Fields: 22

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | RO_CHG_AEXTRA | STRING | 100 | — | — |
| 2 | RO_CHG_ALONG | NUMERIC | 8 | 7 | — |
| 3 | RO_CHG_ANUMPERS | NUMERIC | 8 | 2 | — |
| 4 | RO_CHG_AOPER | STRING | 1 | — | — |
| 5 | RO_CHG_ASETUP | TIME | 4 | — | — |
| 6 | RO_CHG_ASTDT | STRING | 1 | — | — |
| 7 | RO_CHG_ATMACH | STRING | 4 | — | — |
| 8 | RO_CHG_ATOOL | STRING | 15 | — | — |
| 9 | RO_CHG_AWC | STRING | 12 | — | — |
| 10 | RO_CHG_BEXTRA | STRING | 100 | — | — |
| 11 | RO_CHG_BLONG | NUMERIC | 8 | 7 | — |
| 12 | RO_CHG_BMATCH | STRING | 4 | — | — |
| 13 | RO_CHG_BNUMPERS | NUMERIC | 8 | 2 | — |
| 14 | RO_CHG_BSETUP | TIME | 4 | — | — |
| 15 | RO_CHG_BSTDT | STRING | 1 | — | — |
| 16 | RO_CHG_BTOOL | STRING | 15 | — | — |
| 17 | RO_CHG_BWC | STRING | 12 | — | — |
| 18 | RO_CHG_CDATE | DATE | 4 | — | — |
| 19 | RO_CHG_DOPER | STRING | 1 | — | — |
| 20 | RO_CHG_OPER | INTEGER | 2 | — | — |
| 21 | RO_CHG_PART | STRING | 15 | — | — |
| 22 | RO_CHG_USER | STRING | 15 | — | — |

## ROUTAING
**ARCHIVED ROUTING MASTER**

Fields: 62

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTRO_CLASS | STRING | 15 | — | not used |
| 2 | MTRO_CODE | STRING | 15 | — | Part Code |
| 3 | MTRO_DEF_TIME | TIME | 4 | — | — |
| 4 | MTRO_DESC | STRING | 30 | — | Description |
| 5 | MTRO_EST_LINE | NUMERIC | 8 | — | — |
| 6 | MTRO_EST_TAG | STRING | 10 | — | — |
| 7 | MTRO_EXTRA | STRING | 150 | — | Extra |
| 8 | MTRO_FOVHD | NUMERIC | 8 | 4 | Fixed Overhead Rate |
| 9 | MTRO_INSTR_1 | STRING | 60 | — | — |
| 10 | MTRO_INSTR_10 | STRING | 60 | — | — |
| 11 | MTRO_INSTR_11 | STRING | 60 | — | — |
| 12 | MTRO_INSTR_12 | STRING | 60 | — | — |
| 13 | MTRO_INSTR_13 | STRING | 60 | — | — |
| 14 | MTRO_INSTR_14 | STRING | 60 | — | — |
| 15 | MTRO_INSTR_15 | STRING | 60 | — | — |
| 16 | MTRO_INSTR_2 | STRING | 60 | — | — |
| 17 | MTRO_INSTR_3 | STRING | 60 | — | — |
| 18 | MTRO_INSTR_4 | STRING | 60 | — | — |
| 19 | MTRO_INSTR_5 | STRING | 60 | — | — |
| 20 | MTRO_INSTR_6 | STRING | 60 | — | — |
| 21 | MTRO_INSTR_7 | STRING | 60 | — | — |
| 22 | MTRO_INSTR_8 | STRING | 60 | — | — |
| 23 | MTRO_INSTR_9 | STRING | 60 | — | — |
| 24 | MTRO_LABOR | NUMERIC | 8 | 4 | Labor Rate |
| 25 | MTRO_LEAD | INTEGER | 2 | — | Lead Time |
| 26 | MTRO_LONGTIME | NUMERIC | 8 | 7 | Longtime - Decimal Hrs. |
| 27 | MTRO_LOTSIZE | NUMERIC | 8 | — | Lot Size |
| 28 | MTRO_MACHINE | NUMERIC | 8 | 4 | Machine Rate |
| 29 | MTRO_MD_PROC_HR | STRING | 1 | — | — |
| 30 | MTRO_MIN_CHG | NUMERIC | 8 | 2 | Minimum Charge (Outside Process) |
| 31 | MTRO_MISC_ACOST | NUMERIC | 8 | 2 | — |
| 32 | MTRO_NEGOVLP | NUMERIC | 8 | 2 | Negative Overlap |
| 33 | MTRO_NUM | INTEGER | 2 | — | Routing Number |
| 34 | MTRO_NUM_PERSON | NUMERIC | 8 | 2 | Number of Persons |
| 35 | MTRO_NUM_PROCES | INTEGER | 2 | — | Number of Processes |
| 36 | MTRO_OP_TEMP_NO | INTEGER | 2 | — | Template Number |
| 37 | MTRO_OPER | INTEGER | 2 | — | Operation |
| 38 | MTRO_OPERDESC | STRING | 30 | — | Operation Desciption |
| 39 | MTRO_OVERLAP | INTEGER | 2 | — | Overlap Hrs. |
| 40 | MTRO_PARTSHR | NUMERIC | 8 | 2 | Parts/Hour |
| 41 | MTRO_PIECE_RATE | NUMERIC | 8 | 2 | Piece Rate |
| 42 | MTRO_PRINT | STRING | 1 | — | not used |
| 43 | MTRO_PROC_PERHR | NUMERIC | 8 | 2 | Processes Per Hour |
| 44 | MTRO_R_TYPE | STRING | 10 | — | — |
| 45 | MTRO_SETUP | NUMERIC | 8 | 4 | Setup Rate |
| 46 | MTRO_SETUPHRS | TIME | 4 | — | Setup Hours |
| 47 | MTRO_STD_TIME | STRING | 1 | — | Standard Time Y/N |
| 48 | MTRO_TIME_PERPR | TIME | 4 | — | — |
| 49 | MTRO_TIMEPART | TIME | 4 | — | Time/Part |
| 50 | MTRO_TMACHDESC | STRING | 30 | — | Machine Description |
| 51 | MTRO_TMACHINE | STRING | 4 | — | Machine Code |
| 52 | MTRO_TOOL | STRING | 15 | — | Tool Code |
| 53 | MTRO_TOOLDESC | STRING | 30 | — | Tool Description |
| 54 | MTRO_TYPE | STRING | 1 | — | Type |
| 55 | MTRO_VENDCODE | STRING | 10 | — | Vendor Code |
| 56 | MTRO_VENDCOST | NUMERIC | 8 | 6 | Vendor Cost |
| 57 | MTRO_VENDNAME | STRING | 25 | — | Vendor Name |
| 58 | MTRO_VOVHD | NUMERIC | 8 | 4 | Variable Overhead Rate |
| 59 | MTRO_WC | STRING | 12 | — | Work Center |
| 60 | MTRO_WCDESC | STRING | 30 | — | Work Center Description |
| 61 | MTWO_MISC_COST | NUMERIC | 8 | 2 | Misc. Cost |
| 62 | MTWO_MISC_DESC | STRING | 30 | — | Misc. Description |

## ROUTING
**ROUTING MASTER**

Fields: 62

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTRO_CLASS | STRING | 15 | — | not used |
| 2 | MTRO_CODE | STRING | 15 | — | Part Code |
| 3 | MTRO_DEF_TIME | TIME | 4 | — | — |
| 4 | MTRO_DESC | STRING | 30 | — | Description |
| 5 | MTRO_EST_LINE | NUMERIC | 8 | — | — |
| 6 | MTRO_EST_TAG | STRING | 10 | — | — |
| 7 | MTRO_EXTRA | STRING | 150 | — | Extra |
| 8 | MTRO_FOVHD | NUMERIC | 8 | 4 | Fixed Overhead Rate |
| 9 | MTRO_INSTR_1 | STRING | 60 | — | — |
| 10 | MTRO_INSTR_10 | STRING | 60 | — | — |
| 11 | MTRO_INSTR_11 | STRING | 60 | — | — |
| 12 | MTRO_INSTR_12 | STRING | 60 | — | — |
| 13 | MTRO_INSTR_13 | STRING | 60 | — | — |
| 14 | MTRO_INSTR_14 | STRING | 60 | — | — |
| 15 | MTRO_INSTR_15 | STRING | 60 | — | — |
| 16 | MTRO_INSTR_2 | STRING | 60 | — | — |
| 17 | MTRO_INSTR_3 | STRING | 60 | — | — |
| 18 | MTRO_INSTR_4 | STRING | 60 | — | — |
| 19 | MTRO_INSTR_5 | STRING | 60 | — | — |
| 20 | MTRO_INSTR_6 | STRING | 60 | — | — |
| 21 | MTRO_INSTR_7 | STRING | 60 | — | — |
| 22 | MTRO_INSTR_8 | STRING | 60 | — | — |
| 23 | MTRO_INSTR_9 | STRING | 60 | — | — |
| 24 | MTRO_LABOR | NUMERIC | 8 | 4 | Labor Rate |
| 25 | MTRO_LEAD | INTEGER | 2 | — | Lead Time |
| 26 | MTRO_LONGTIME | NUMERIC | 8 | 7 | Longtime - Decimal Hrs. |
| 27 | MTRO_LOTSIZE | NUMERIC | 8 | — | Lot Size |
| 28 | MTRO_MACHINE | NUMERIC | 8 | 4 | Machine Rate |
| 29 | MTRO_MD_PROC_HR | STRING | 1 | — | — |
| 30 | MTRO_MIN_CHG | NUMERIC | 8 | 2 | Minimum Charge (Outside Process) |
| 31 | MTRO_MISC_ACOST | NUMERIC | 8 | 2 | — |
| 32 | MTRO_NEGOVLP | NUMERIC | 8 | 2 | Negative Overlap |
| 33 | MTRO_NUM | INTEGER | 2 | — | Routing Number |
| 34 | MTRO_NUM_PERSON | NUMERIC | 8 | 2 | Number of Persons |
| 35 | MTRO_NUM_PROCES | INTEGER | 2 | — | Number of Processes |
| 36 | MTRO_OP_TEMP_NO | INTEGER | 2 | — | Template Number |
| 37 | MTRO_OPER | INTEGER | 2 | — | Operation |
| 38 | MTRO_OPERDESC | STRING | 30 | — | Operation Desciption |
| 39 | MTRO_OVERLAP | INTEGER | 2 | — | Overlap Hrs. |
| 40 | MTRO_PARTSHR | NUMERIC | 8 | 2 | Parts/Hour |
| 41 | MTRO_PIECE_RATE | NUMERIC | 8 | 2 | Piece Rate |
| 42 | MTRO_PRINT | STRING | 1 | — | not used |
| 43 | MTRO_PROC_PERHR | NUMERIC | 8 | 2 | Processes Per Hour |
| 44 | MTRO_R_TYPE | STRING | 10 | — | — |
| 45 | MTRO_SETUP | NUMERIC | 8 | 4 | Setup Rate |
| 46 | MTRO_SETUPHRS | TIME | 4 | — | Setup Hours |
| 47 | MTRO_STD_TIME | STRING | 1 | — | Standard Time Y/N |
| 48 | MTRO_TIME_PERPR | TIME | 4 | — | — |
| 49 | MTRO_TIMEPART | TIME | 4 | — | Time/Part |
| 50 | MTRO_TMACHDESC | STRING | 30 | — | Machine Description |
| 51 | MTRO_TMACHINE | STRING | 4 | — | Machine Code |
| 52 | MTRO_TOOL | STRING | 15 | — | Tool Code |
| 53 | MTRO_TOOLDESC | STRING | 30 | — | Tool Description |
| 54 | MTRO_TYPE | STRING | 1 | — | Type |
| 55 | MTRO_VENDCODE | STRING | 10 | — | Vendor Code |
| 56 | MTRO_VENDCOST | NUMERIC | 8 | 6 | Vendor Cost |
| 57 | MTRO_VENDNAME | STRING | 25 | — | Vendor Name |
| 58 | MTRO_VOVHD | NUMERIC | 8 | 4 | Variable Overhead Rate |
| 59 | MTRO_WC | STRING | 12 | — | Work Center |
| 60 | MTRO_WCDESC | STRING | 30 | — | Work Center Description |
| 61 | MTWO_MISC_COST | NUMERIC | 8 | 2 | Misc. Cost |
| 62 | MTWO_MISC_DESC | STRING | 30 | — | Misc. Description |

## ROUTTEMP
**ROUTING TEMPLATES**

Fields: 62

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTRO_CLASS | STRING | 15 | — | not used |
| 2 | MTRO_CODE | STRING | 15 | — | Part Code |
| 3 | MTRO_DEF_TIME | TIME | 4 | — | — |
| 4 | MTRO_DESC | STRING | 30 | — | Description |
| 5 | MTRO_EST_LINE | NUMERIC | 8 | — | — |
| 6 | MTRO_EST_TAG | STRING | 10 | — | — |
| 7 | MTRO_EXTRA | STRING | 150 | — | Extra |
| 8 | MTRO_FOVHD | NUMERIC | 8 | 4 | Fixed Overhead Rate |
| 9 | MTRO_INSTR_1 | STRING | 60 | — | — |
| 10 | MTRO_INSTR_10 | STRING | 60 | — | — |
| 11 | MTRO_INSTR_11 | STRING | 60 | — | — |
| 12 | MTRO_INSTR_12 | STRING | 60 | — | — |
| 13 | MTRO_INSTR_13 | STRING | 60 | — | — |
| 14 | MTRO_INSTR_14 | STRING | 60 | — | — |
| 15 | MTRO_INSTR_15 | STRING | 60 | — | — |
| 16 | MTRO_INSTR_2 | STRING | 60 | — | — |
| 17 | MTRO_INSTR_3 | STRING | 60 | — | — |
| 18 | MTRO_INSTR_4 | STRING | 60 | — | — |
| 19 | MTRO_INSTR_5 | STRING | 60 | — | — |
| 20 | MTRO_INSTR_6 | STRING | 60 | — | — |
| 21 | MTRO_INSTR_7 | STRING | 60 | — | — |
| 22 | MTRO_INSTR_8 | STRING | 60 | — | — |
| 23 | MTRO_INSTR_9 | STRING | 60 | — | — |
| 24 | MTRO_LABOR | NUMERIC | 8 | 4 | Labor Rate |
| 25 | MTRO_LEAD | INTEGER | 2 | — | Lead Time |
| 26 | MTRO_LONGTIME | NUMERIC | 8 | 7 | Longtime - Decimal Hrs. |
| 27 | MTRO_LOTSIZE | NUMERIC | 8 | — | Lot Size |
| 28 | MTRO_MACHINE | NUMERIC | 8 | 4 | Machine Rate |
| 29 | MTRO_MD_PROC_HR | STRING | 1 | — | — |
| 30 | MTRO_MIN_CHG | NUMERIC | 8 | 2 | Minimum Charge (Outside Process) |
| 31 | MTRO_MISC_ACOST | NUMERIC | 8 | 2 | — |
| 32 | MTRO_NEGOVLP | NUMERIC | 8 | 2 | Negative Overlap |
| 33 | MTRO_NUM | INTEGER | 2 | — | Routing Number |
| 34 | MTRO_NUM_PERSON | NUMERIC | 8 | 2 | Number of Persons |
| 35 | MTRO_NUM_PROCES | INTEGER | 2 | — | Number of Processes |
| 36 | MTRO_OP_TEMP_NO | INTEGER | 2 | — | Template Number |
| 37 | MTRO_OPER | INTEGER | 2 | — | Operation |
| 38 | MTRO_OPERDESC | STRING | 30 | — | Operation Desciption |
| 39 | MTRO_OVERLAP | INTEGER | 2 | — | Overlap Hrs. |
| 40 | MTRO_PARTSHR | NUMERIC | 8 | 2 | Parts/Hour |
| 41 | MTRO_PIECE_RATE | NUMERIC | 8 | 2 | Piece Rate |
| 42 | MTRO_PRINT | STRING | 1 | — | not used |
| 43 | MTRO_PROC_PERHR | NUMERIC | 8 | 2 | Processes Per Hour |
| 44 | MTRO_R_TYPE | STRING | 10 | — | — |
| 45 | MTRO_SETUP | NUMERIC | 8 | 4 | Setup Rate |
| 46 | MTRO_SETUPHRS | TIME | 4 | — | Setup Hours |
| 47 | MTRO_STD_TIME | STRING | 1 | — | Standard Time Y/N |
| 48 | MTRO_TIME_PERPR | TIME | 4 | — | — |
| 49 | MTRO_TIMEPART | TIME | 4 | — | Time/Part |
| 50 | MTRO_TMACHDESC | STRING | 30 | — | Machine Description |
| 51 | MTRO_TMACHINE | STRING | 4 | — | Machine Code |
| 52 | MTRO_TOOL | STRING | 15 | — | Tool Code |
| 53 | MTRO_TOOLDESC | STRING | 30 | — | Tool Description |
| 54 | MTRO_TYPE | STRING | 1 | — | Type |
| 55 | MTRO_VENDCODE | STRING | 10 | — | Vendor Code |
| 56 | MTRO_VENDCOST | NUMERIC | 8 | 6 | Vendor Cost |
| 57 | MTRO_VENDNAME | STRING | 25 | — | Vendor Name |
| 58 | MTRO_VOVHD | NUMERIC | 8 | 4 | Variable Overhead Rate |
| 59 | MTRO_WC | STRING | 12 | — | Work Center |
| 60 | MTRO_WCDESC | STRING | 30 | — | Work Center Description |
| 61 | MTWO_MISC_COST | NUMERIC | 8 | 2 | Misc. Cost |
| 62 | MTWO_MISC_DESC | STRING | 30 | — | Misc. Description |

## TOOL
**TOOL MASTER**

Fields: 57

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTOOL_ADATE_1 | DATE | 4 | — | — |
| 2 | MTOOL_ADATE_2 | DATE | 4 | — | — |
| 3 | MTOOL_ALPHA_1 | STRING | 30 | — | — |
| 4 | MTOOL_ALPHA_2 | STRING | 30 | — | — |
| 5 | MTOOL_ALPHA_3 | STRING | 30 | — | — |
| 6 | MTOOL_ALPHA_4 | STRING | 30 | — | — |
| 7 | MTOOL_ALPHA_5 | STRING | 30 | — | — |
| 8 | MTOOL_BASE_LOC | STRING | 10 | — | — |
| 9 | MTOOL_BLOC_BIN | STRING | 15 | — | — |
| 10 | MTOOL_CAVITY | STRING | 60 | — | — |
| 11 | MTOOL_CUST | STRING | 10 | — | — |
| 12 | MTOOL_CYCLES | NUMERIC | 8 | — | — |
| 13 | MTOOL_DATE | DATE | 4 | — | — |
| 14 | MTOOL_DEPTH | NUMERIC | 8 | 2 | — |
| 15 | MTOOL_DESC | STRING | 30 | — | — |
| 16 | MTOOL_EJ_STROKE | NUMERIC | 8 | 2 | — |
| 17 | MTOOL_EXTRA | STRING | 100 | — | — |
| 18 | MTOOL_FLAG_1 | STRING | 1 | — | — |
| 19 | MTOOL_FLAG_2 | STRING | 1 | — | — |
| 20 | MTOOL_FLAG_3 | STRING | 1 | — | — |
| 21 | MTOOL_FLAG_4 | STRING | 1 | — | — |
| 22 | MTOOL_FLAG_5 | STRING | 1 | — | — |
| 23 | MTOOL_HEIGHT | NUMERIC | 8 | 2 | — |
| 24 | MTOOL_HOTRUN_CH | STRING | 30 | — | — |
| 25 | MTOOL_ILOC_BIN | STRING | 15 | — | — |
| 26 | MTOOL_INS_LOC | STRING | 10 | — | — |
| 27 | MTOOL_INSERV_DT | DATE | 4 | — | — |
| 28 | MTOOL_LASTUSED | DATE | 4 | — | — |
| 29 | MTOOL_LST_MDATE | DATE | 4 | — | — |
| 30 | MTOOL_MIN_TON | NUMERIC | 8 | 2 | — |
| 31 | MTOOL_NOPARTS | NUMERIC | 8 | — | — |
| 32 | MTOOL_NOTES_1 | STRING | 45 | — | — |
| 33 | MTOOL_NOTES_2 | STRING | 45 | — | — |
| 34 | MTOOL_NOTES_3 | STRING | 45 | — | — |
| 35 | MTOOL_NOTES_4 | STRING | 45 | — | — |
| 36 | MTOOL_NOTES_5 | STRING | 45 | — | — |
| 37 | MTOOL_NOTES_6 | STRING | 45 | — | — |
| 38 | MTOOL_NOTES_7 | STRING | 45 | — | — |
| 39 | MTOOL_NOTES_8 | STRING | 45 | — | — |
| 40 | MTOOL_NOZ_RAD | NUMERIC | 8 | 2 | — |
| 41 | MTOOL_NUM1_1 | NUMERIC | 8 | 2 | — |
| 42 | MTOOL_NUM1_2 | NUMERIC | 8 | 2 | — |
| 43 | MTOOL_NUM_PORTS | STRING | 30 | — | — |
| 44 | MTOOL_NUMCAVITY | INTEGER | 2 | — | — |
| 45 | MTOOL_OWNER | STRING | 10 | — | — |
| 46 | MTOOL_PM_INTVAL | INTEGER | 2 | — | — |
| 47 | MTOOL_PRTSMAINT | NUMERIC | 8 | — | — |
| 48 | MTOOL_REPL_COST | NUMERIC | 8 | 2 | — |
| 49 | MTOOL_SHOTSIZE | NUMERIC | 8 | 2 | — |
| 50 | MTOOL_TOOL | STRING | 15 | — | — |
| 51 | MTOOL_TOOLTYPE_1 | STRING | 60 | — | — |
| 52 | MTOOL_TOOLTYPE_2 | STRING | 60 | — | — |
| 53 | MTOOL_TOTCYCLES | NUMERIC | 8 | — | — |
| 54 | MTOOL_WATERTMPA | NUMERIC | 8 | 2 | — |
| 55 | MTOOL_WATERTMPB | NUMERIC | 8 | 2 | — |
| 56 | MTOOL_WEIGHT | NUMERIC | 8 | 2 | — |
| 57 | MTOOL_WIDTH | NUMERIC | 8 | 2 | — |
