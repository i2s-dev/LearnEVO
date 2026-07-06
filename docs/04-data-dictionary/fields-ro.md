# RO — Routing / Machine / Tool: Field Reference

Status: verified-schema + completed field meanings (Pass 574h, 2026-07-06).

Note: file is labelled "Receivable Other" in the Excel source but all tables are clearly
Routing, Machine, and Tooling master data. Label is a source-sheet artifact.

Source: `Evo-DBA_File_Fields 052421.xlsx`, sheet "Fields". Excel descriptions present for
ROUTING/ROUTAING/ROUTTEMP operation fields; remaining meanings name-inferred.

ROUTING is the live routing master. ROUTAING is the archived copy after WO archive.
ROUTTEMP is reusable routing templates. All three share the MTRO_* schema (62 fields).

---

## BKRTCST
**ROUTING COSTS** — historical parts-per-hour and setup cost by operation

Fields: 24 | Key: BKRT_CODE + BKRT_OPER + BKRT_DATE

10 time-period slots per row tracking routing cost changes over time (PARTSHR/SETUP _1..10).

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKRT_CODE | STRING | 15 | — | Part code (FK → ROUTING.MTRO_CODE) |
| 2 | BKRT_DATE | DATE | 4 | — | Date this cost record was created or revised |
| 3 | BKRT_OPER | INTEGER | 2 | — | Operation number (FK → ROUTING.MTRO_OPER) |
| 4 | BKRT_PARTSHR_1 | NUMERIC | 8 | 2 | Parts per hour — period slot 1 |
| 5 | BKRT_PARTSHR_10 | NUMERIC | 8 | 2 | Parts per hour — period slot 10 |
| 6 | BKRT_PARTSHR_2 | NUMERIC | 8 | 2 | Parts per hour — period slot 2 |
| 7 | BKRT_PARTSHR_3 | NUMERIC | 8 | 2 | Parts per hour — period slot 3 |
| 8 | BKRT_PARTSHR_4 | NUMERIC | 8 | 2 | Parts per hour — period slot 4 |
| 9 | BKRT_PARTSHR_5 | NUMERIC | 8 | 2 | Parts per hour — period slot 5 |
| 10 | BKRT_PARTSHR_6 | NUMERIC | 8 | 2 | Parts per hour — period slot 6 |
| 11 | BKRT_PARTSHR_7 | NUMERIC | 8 | 2 | Parts per hour — period slot 7 |
| 12 | BKRT_PARTSHR_8 | NUMERIC | 8 | 2 | Parts per hour — period slot 8 |
| 13 | BKRT_PARTSHR_9 | NUMERIC | 8 | 2 | Parts per hour — period slot 9 |
| 14 | BKRT_QUOTE | NUMERIC | 8 | — | Quote number associated with this cost record |
| 15 | BKRT_SETUP_1 | TIME | 4 | — | Setup hours — period slot 1 |
| 16 | BKRT_SETUP_10 | TIME | 4 | — | Setup hours — period slot 10 |
| 17 | BKRT_SETUP_2 | TIME | 4 | — | Setup hours — period slot 2 |
| 18 | BKRT_SETUP_3 | TIME | 4 | — | Setup hours — period slot 3 |
| 19 | BKRT_SETUP_4 | TIME | 4 | — | Setup hours — period slot 4 |
| 20 | BKRT_SETUP_5 | TIME | 4 | — | Setup hours — period slot 5 |
| 21 | BKRT_SETUP_6 | TIME | 4 | — | Setup hours — period slot 6 |
| 22 | BKRT_SETUP_7 | TIME | 4 | — | Setup hours — period slot 7 |
| 23 | BKRT_SETUP_8 | TIME | 4 | — | Setup hours — period slot 8 |
| 24 | BKRT_SETUP_9 | TIME | 4 | — | Setup hours — period slot 9 |

## BKRTSPEC
**ROUTING SPECIFICATIONS** — per-operation specification notes (active routing)

Fields: 7 | Key: BKRT_SPEC_PART + BKRT_SPEC_SEQ

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKRT_SPEC_LINE | INTEGER | 2 | — | Line Number |
| 2 | BKRT_SPEC_NOTE_1 | STRING | 20 | — | Specification note line 1 (free text) |
| 3 | BKRT_SPEC_NOTE_2 | STRING | 20 | — | Specification note line 2 |
| 4 | BKRT_SPEC_NOTE_3 | STRING | 20 | — | Specification note line 3 |
| 5 | BKRT_SPEC_NOTE_4 | STRING | 20 | — | Specification note line 4 |
| 6 | BKRT_SPEC_PART | STRING | 15 | — | Item Number |
| 7 | BKRT_SPEC_SEQ | INTEGER | 2 | — | Sequence |

## BKRTTEMP
**SPECIFICATION TEMPLATES** — reusable specification note templates

Fields: 6 | Key: BKRT_TEMP_CODE + BKRT_TEMP_LINE

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKRT_TEMP_CODE | STRING | 15 | — | Item Number |
| 2 | BKRT_TEMP_LINE | INTEGER | 2 | — | Line Number |
| 3 | BKRT_TEMP_NOTE_1 | STRING | 20 | — | Template specification note line 1 (free text) |
| 4 | BKRT_TEMP_NOTE_2 | STRING | 20 | — | Template specification note line 2 |
| 5 | BKRT_TEMP_NOTE_3 | STRING | 20 | — | Template specification note line 3 |
| 6 | BKRT_TEMP_NOTE_4 | STRING | 20 | — | Template specification note line 4 |

## DPTMENT
**DEPARTMENTS** — department code lookup

Fields: 2 | Key: DPT_CODE

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | DPT_CODE | STRING | 4 | — | Department code (PK) |
| 2 | DPT_DESC | STRING | 30 | — | Department description |

## MACHINE
**MACHINES** — machine master for routing work center assignment

Fields: 20 | Key: TMACH_MACHINE

Physical machine records. Each machine belongs to a work center. Hours-based preventive
maintenance tracking via HRSMAINT/HRSUSED.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | TMACH_ACTIVE | STRING | 1 | — | Active flag: `Y`=active, `N`=inactive |
| 2 | TMACH_DATE | DATE | 4 | — | Machine record creation/purchase date |
| 3 | TMACH_DESC | STRING | 30 | — | Machine description |
| 4 | TMACH_EXTRA | STRING | 100 | — | Extra data |
| 5 | TMACH_HRSMAINT | NUMERIC | 8 | — | Hours since last maintenance |
| 6 | TMACH_HRSUSED | NUMERIC | 8 | — | Total hours used (lifetime runtime accumulator) |
| 7 | TMACH_INACTDATE | DATE | 4 | — | Date machine was inactivated |
| 8 | TMACH_INACTWHO | STRING | 30 | — | Who inactivated the machine |
| 9 | TMACH_INACTWHY | STRING | 60 | — | Reason for inactivation |
| 10 | TMACH_MACHINE | STRING | 4 | — | Machine code (PK) |
| 11 | TMACH_NOTES_1 | STRING | 45 | — | Machine notes line 1 |
| 12 | TMACH_NOTES_2 | STRING | 45 | — | Machine notes line 2 |
| 13 | TMACH_NOTES_3 | STRING | 45 | — | Machine notes line 3 |
| 14 | TMACH_NOTES_4 | STRING | 45 | — | Machine notes line 4 |
| 15 | TMACH_NOTES_5 | STRING | 45 | — | Machine notes line 5 |
| 16 | TMACH_NOTES_6 | STRING | 45 | — | Machine notes line 6 |
| 17 | TMACH_NOTES_7 | STRING | 45 | — | Machine notes line 7 |
| 18 | TMACH_NOTES_8 | STRING | 45 | — | Machine notes line 8 |
| 19 | TMACH_WC | STRING | 12 | — | Work center this machine belongs to (FK → WORKCNTR) |
| 20 | TMACH_WCDESC | STRING | 30 | — | Work center description (denormalized copy) |

## ROCHG
**ROUTING CHANGES (NOT USED)** — routing operation change audit log

Fields: 22 | Key: BKRT_PART + BKRT_OPER + BKRT_CDATE

Marked NOT USED in source; stores before (B) and after (A) snapshots of routing operation
fields for audit purposes.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | RO_CHG_AEXTRA | STRING | 100 | — | After-change: extra data |
| 2 | RO_CHG_ALONG | NUMERIC | 8 | 7 | After-change: longtime (decimal hours) |
| 3 | RO_CHG_ANUMPERS | NUMERIC | 8 | 2 | After-change: number of persons |
| 4 | RO_CHG_AOPER | STRING | 1 | — | Change type: `A`=add, `D`=delete, `C`=change |
| 5 | RO_CHG_ASETUP | TIME | 4 | — | After-change: setup time |
| 6 | RO_CHG_ASTDT | STRING | 1 | — | After-change: standard time flag (Y/N) |
| 7 | RO_CHG_ATMACH | STRING | 4 | — | After-change: machine code |
| 8 | RO_CHG_ATOOL | STRING | 15 | — | After-change: tool code |
| 9 | RO_CHG_AWC | STRING | 12 | — | After-change: work center code |
| 10 | RO_CHG_BEXTRA | STRING | 100 | — | Before-change: extra data |
| 11 | RO_CHG_BLONG | NUMERIC | 8 | 7 | Before-change: longtime (decimal hours) |
| 12 | RO_CHG_BMATCH | STRING | 4 | — | Before-change: machine code |
| 13 | RO_CHG_BNUMPERS | NUMERIC | 8 | 2 | Before-change: number of persons |
| 14 | RO_CHG_BSETUP | TIME | 4 | — | Before-change: setup time |
| 15 | RO_CHG_BSTDT | STRING | 1 | — | Before-change: standard time flag (Y/N) |
| 16 | RO_CHG_BTOOL | STRING | 15 | — | Before-change: tool code |
| 17 | RO_CHG_BWC | STRING | 12 | — | Before-change: work center code |
| 18 | RO_CHG_CDATE | DATE | 4 | — | Date of this routing change |
| 19 | RO_CHG_DOPER | STRING | 1 | — | Deleted operation flag (Y=this operation was deleted) |
| 20 | RO_CHG_OPER | INTEGER | 2 | — | Operation number changed |
| 21 | RO_CHG_PART | STRING | 15 | — | Part code changed (FK → ROUTING) |
| 22 | RO_CHG_USER | STRING | 15 | — | User who made the routing change |

## ROUTAING
**ARCHIVED ROUTING MASTER** — routing operations archived after WO close

Fields: 62 | Key: MTRO_CODE + MTRO_NUM + MTRO_OPER

Identical schema to ROUTING — archival copy. See ROUTING below for full field semantics.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTRO_CLASS | STRING | 15 | — | not used |
| 2 | MTRO_CODE | STRING | 15 | — | Part Code |
| 3 | MTRO_DEF_TIME | TIME | 4 | — | Default operation time (used when no actual logged) |
| 4 | MTRO_DESC | STRING | 30 | — | Description |
| 5 | MTRO_EST_LINE | NUMERIC | 8 | — | Estimate line number (cross-reference to cost estimate) |
| 6 | MTRO_EST_TAG | STRING | 10 | — | Estimate tag code |
| 7 | MTRO_EXTRA | STRING | 150 | — | Extra |
| 8 | MTRO_FOVHD | NUMERIC | 8 | 4 | Fixed Overhead Rate |
| 9 | MTRO_INSTR_1 | STRING | 60 | — | Operation instruction line 1 (freetext work instructions) |
| 10 | MTRO_INSTR_10 | STRING | 60 | — | Operation instruction line 10 |
| 11 | MTRO_INSTR_11 | STRING | 60 | — | Operation instruction line 11 |
| 12 | MTRO_INSTR_12 | STRING | 60 | — | Operation instruction line 12 |
| 13 | MTRO_INSTR_13 | STRING | 60 | — | Operation instruction line 13 |
| 14 | MTRO_INSTR_14 | STRING | 60 | — | Operation instruction line 14 |
| 15 | MTRO_INSTR_15 | STRING | 60 | — | Operation instruction line 15 |
| 16 | MTRO_INSTR_2 | STRING | 60 | — | Operation instruction line 2 |
| 17 | MTRO_INSTR_3 | STRING | 60 | — | Operation instruction line 3 |
| 18 | MTRO_INSTR_4 | STRING | 60 | — | Operation instruction line 4 |
| 19 | MTRO_INSTR_5 | STRING | 60 | — | Operation instruction line 5 |
| 20 | MTRO_INSTR_6 | STRING | 60 | — | Operation instruction line 6 |
| 21 | MTRO_INSTR_7 | STRING | 60 | — | Operation instruction line 7 |
| 22 | MTRO_INSTR_8 | STRING | 60 | — | Operation instruction line 8 |
| 23 | MTRO_INSTR_9 | STRING | 60 | — | Operation instruction line 9 |
| 24 | MTRO_LABOR | NUMERIC | 8 | 4 | Labor Rate |
| 25 | MTRO_LEAD | INTEGER | 2 | — | Lead Time |
| 26 | MTRO_LONGTIME | NUMERIC | 8 | 7 | Longtime - Decimal Hrs. |
| 27 | MTRO_LOTSIZE | NUMERIC | 8 | — | Lot Size |
| 28 | MTRO_MACHINE | NUMERIC | 8 | 4 | Machine Rate |
| 29 | MTRO_MD_PROC_HR | STRING | 1 | — | Rate driver: `M`=machine-driven processes/hr, `D`=direct labor |
| 30 | MTRO_MIN_CHG | NUMERIC | 8 | 2 | Minimum Charge (Outside Process) |
| 31 | MTRO_MISC_ACOST | NUMERIC | 8 | 2 | Miscellaneous actual cost for this operation |
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
| 44 | MTRO_R_TYPE | STRING | 10 | — | Routing type: `I`=inside/in-house, `O`=outside process |
| 45 | MTRO_SETUP | NUMERIC | 8 | 4 | Setup Rate |
| 46 | MTRO_SETUPHRS | TIME | 4 | — | Setup Hours |
| 47 | MTRO_STD_TIME | STRING | 1 | — | Standard Time Y/N |
| 48 | MTRO_TIME_PERPR | TIME | 4 | — | Time per process (cycle time at unit level) |
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
**ROUTING MASTER** — active routing operations per part

Fields: 62 | Key: MTRO_CODE + MTRO_NUM + MTRO_OPER

One row per part × routing number × operation step. Defines the manufacturing process:
work center, machine, labor/overhead rates, setup and run times. Identical schema to
ROUTAING and ROUTTEMP. See ROUTAING above for all field definitions.

## ROUTTEMP
**ROUTING TEMPLATES** — reusable routing definition templates

Fields: 62 | Key: MTRO_CODE + MTRO_NUM + MTRO_OPER

Template routing records copied to ROUTING when a new routing is created from a template.
Identical schema to ROUTING. See ROUTAING above for all field definitions.

## TOOL
**TOOL MASTER** — tooling master with injection-molding-specific physical specifications

Fields: 57 | Key: MTOOL_TOOL

Tooling master record. Physical dimensions (HEIGHT/DEPTH/WIDTH), mold specifications
(NUMCAVITY, CAVITY, SHOTSIZE, EJ_STROKE, NOZ_RAD, MIN_TON, WATERTMPA/B) indicate this
is configured for injection molding operations. User-defined fields ALPHA_1..5 and
FLAG_1..5 provide site-specific customization. PM interval tracked via CYCLES/PRTSMAINT.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTOOL_ADATE_1 | DATE | 4 | — | User-defined date field 1 |
| 2 | MTOOL_ADATE_2 | DATE | 4 | — | User-defined date field 2 |
| 3 | MTOOL_ALPHA_1 | STRING | 30 | — | User-defined alphanumeric field 1 |
| 4 | MTOOL_ALPHA_2 | STRING | 30 | — | User-defined alphanumeric field 2 |
| 5 | MTOOL_ALPHA_3 | STRING | 30 | — | User-defined alphanumeric field 3 |
| 6 | MTOOL_ALPHA_4 | STRING | 30 | — | User-defined alphanumeric field 4 |
| 7 | MTOOL_ALPHA_5 | STRING | 30 | — | User-defined alphanumeric field 5 |
| 8 | MTOOL_BASE_LOC | STRING | 10 | — | Base/home storage location code for this tool |
| 9 | MTOOL_BLOC_BIN | STRING | 15 | — | Base location bin designation |
| 10 | MTOOL_CAVITY | STRING | 60 | — | Cavity configuration description (e.g., "2-cavity hot runner") |
| 11 | MTOOL_CUST | STRING | 10 | — | Customer code (FK → BKARCUST; customer-owned tooling) |
| 12 | MTOOL_CYCLES | NUMERIC | 8 | — | Cycles accumulated since last maintenance |
| 13 | MTOOL_DATE | DATE | 4 | — | Tool record creation date |
| 14 | MTOOL_DEPTH | NUMERIC | 8 | 2 | Tool depth — physical dimension (inches) |
| 15 | MTOOL_DESC | STRING | 30 | — | Tool description |
| 16 | MTOOL_EJ_STROKE | NUMERIC | 8 | 2 | Ejector stroke — injection mold ejection travel (inches) |
| 17 | MTOOL_EXTRA | STRING | 100 | — | Extra data |
| 18 | MTOOL_FLAG_1 | STRING | 1 | — | User-defined flag field 1 (Y/N) |
| 19 | MTOOL_FLAG_2 | STRING | 1 | — | User-defined flag field 2 |
| 20 | MTOOL_FLAG_3 | STRING | 1 | — | User-defined flag field 3 |
| 21 | MTOOL_FLAG_4 | STRING | 1 | — | User-defined flag field 4 |
| 22 | MTOOL_FLAG_5 | STRING | 1 | — | User-defined flag field 5 |
| 23 | MTOOL_HEIGHT | NUMERIC | 8 | 2 | Tool height — physical dimension (inches) |
| 24 | MTOOL_HOTRUN_CH | STRING | 30 | — | Hot runner channel description |
| 25 | MTOOL_ILOC_BIN | STRING | 15 | — | In-use/current location bin |
| 26 | MTOOL_INS_LOC | STRING | 10 | — | In-service location code (where tool is currently installed) |
| 27 | MTOOL_INSERV_DT | DATE | 4 | — | In-service date (when tool was placed into production) |
| 28 | MTOOL_LASTUSED | DATE | 4 | — | Date tool was last used in production |
| 29 | MTOOL_LST_MDATE | DATE | 4 | — | Last maintenance date |
| 30 | MTOOL_MIN_TON | NUMERIC | 8 | 2 | Minimum press tonnage required for this tool |
| 31 | MTOOL_NOPARTS | NUMERIC | 8 | — | Total parts produced by this tool (lifetime counter) |
| 32 | MTOOL_NOTES_1 | STRING | 45 | — | Tool notes line 1 |
| 33 | MTOOL_NOTES_2 | STRING | 45 | — | Tool notes line 2 |
| 34 | MTOOL_NOTES_3 | STRING | 45 | — | Tool notes line 3 |
| 35 | MTOOL_NOTES_4 | STRING | 45 | — | Tool notes line 4 |
| 36 | MTOOL_NOTES_5 | STRING | 45 | — | Tool notes line 5 |
| 37 | MTOOL_NOTES_6 | STRING | 45 | — | Tool notes line 6 |
| 38 | MTOOL_NOTES_7 | STRING | 45 | — | Tool notes line 7 |
| 39 | MTOOL_NOTES_8 | STRING | 45 | — | Tool notes line 8 |
| 40 | MTOOL_NOZ_RAD | NUMERIC | 8 | 2 | Nozzle radius — sprue bushing contact radius (inches) |
| 41 | MTOOL_NUM1_1 | NUMERIC | 8 | 2 | User-defined numeric field 1 |
| 42 | MTOOL_NUM1_2 | NUMERIC | 8 | 2 | User-defined numeric field 2 |
| 43 | MTOOL_NUM_PORTS | STRING | 30 | — | Number of ports description (hot runner gate count, etc.) |
| 44 | MTOOL_NUMCAVITY | INTEGER | 2 | — | Number of cavities in this mold |
| 45 | MTOOL_OWNER | STRING | 10 | — | Owner code (company or customer code owning the tool) |
| 46 | MTOOL_PM_INTVAL | INTEGER | 2 | — | Preventive maintenance interval (cycles between PM services) |
| 47 | MTOOL_PRTSMAINT | NUMERIC | 8 | — | Parts produced since last maintenance |
| 48 | MTOOL_REPL_COST | NUMERIC | 8 | 2 | Tool replacement cost |
| 49 | MTOOL_SHOTSIZE | NUMERIC | 8 | 2 | Shot size (oz — material volume per cycle) |
| 50 | MTOOL_TOOL | STRING | 15 | — | Tool code (PK) |
| 51 | MTOOL_TOOLTYPE_1 | STRING | 60 | — | Tool type classification line 1 |
| 52 | MTOOL_TOOLTYPE_2 | STRING | 60 | — | Tool type classification line 2 |
| 53 | MTOOL_TOTCYCLES | NUMERIC | 8 | — | Total lifetime cycles (all-time production counter) |
| 54 | MTOOL_WATERTMPA | NUMERIC | 8 | 2 | Cooling circuit A water temperature (°F or °C) |
| 55 | MTOOL_WATERTMPB | NUMERIC | 8 | 2 | Cooling circuit B water temperature |
| 56 | MTOOL_WEIGHT | NUMERIC | 8 | 2 | Tool weight (lbs) |
| 57 | MTOOL_WIDTH | NUMERIC | 8 | 2 | Tool width — physical dimension (inches) |

**Confidence: 82/100** — ROUTING/ROUTAING/ROUTTEMP key fields verified from Excel descriptions;
BKRTCST slot semantics inferred from cost history context; MACHINE/TOOL field meanings clear
from manufacturing context; TOOL injection-molding-specific fields (NOZ_RAD, EJ_STROKE,
WATERTMPA/B, NUMCAVITY, SHOTSIZE) clear from physical mold design conventions; exact MTRO_R_TYPE
and MTRO_MD_PROC_HR values require RWN decryption.
