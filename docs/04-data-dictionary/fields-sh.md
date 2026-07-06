# SH — Finite Scheduling: Field Reference

Status: verified-schema + completed field meanings (Pass 574e, 2026-07-06).

Source: `Evo-DBA_File_Fields 052421.xlsx`, sheet "Fields". Excel descriptions present
for SCHEDCAL and partial WORKSORD/WOSROUT; remaining fields inferred from naming + WO
module parallels (MTWO_WIP_* = WORKORD/WORKIP schema, MTWORO_* = MTWORO routing schema).

The SH module is the finite scheduling / visual scheduler subsystem. It uses temp tables
(BUCKETS, SCHWO, WCCTL, WCTRSLOD, WORKSORD, WOSROUT) to hold the current scheduling
state for display. CALENDAR and SCHEDCAL define working days for scheduling calculations.

---

## BUCKETS
**FINITE SCHEDULE BUCKETS** — one bucket per WO operation × scheduled time slot

Fields: 14 | Key: BUK_WOPRE + BUK_WOSUF + BUK_OPER + BUK_SDATE

The visual scheduler breaks WO operations into time buckets. Each bucket represents one
scheduling slot (WO × operation × work center × start/finish window).

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BUK_CNTN | NUMERIC | 8 | — | Contention count — number of WOs competing for the same WC slot |
| 2 | BUK_CRATIO | NUMERIC | 8 | 5 | Critical ratio (scheduling priority: lower = more overdue/urgent) |
| 3 | BUK_FDATE | DATE | 4 | — | Bucket finish date |
| 4 | BUK_FDATE_SHOP | NUMERIC | 8 | 4 | Finish date as shop day (floating-point shop calendar value) |
| 5 | BUK_LOCKED | STRING | 1 | — | Manually locked flag: `Y`=this bucket is pinned/not reschedulable |
| 6 | BUK_NUM_SUNITS | NUMERIC | 8 | — | Number of scheduling units (run time expressed in scheduler units) |
| 7 | BUK_OPER | INTEGER | 2 | — | Operation sequence number |
| 8 | BUK_PART | STRING | 15 | — | Item code being manufactured |
| 9 | BUK_SDATE | DATE | 4 | — | Bucket start date |
| 10 | BUK_SDATE_SHOP | NUMERIC | 8 | 4 | Start date as shop day (floating-point) |
| 11 | BUK_WC | STRING | 12 | — | Work center code (FK → WORKCTR) |
| 12 | BUK_WCTYPE | STRING | 1 | — | Work center type flag (M=machine, L=labor, O=outside) |
| 13 | BUK_WOPRE | NUMERIC | 8 | — | WO prefix |
| 14 | BUK_WOSUF | INTEGER | 2 | — | WO suffix |

## CALENDAR
**SHOP CALENDAR** — working day / holiday calendar

Fields: 5 | Key: MTCAL_DATE

One row per calendar date. Defines which days are working vs. weekend/holiday for
scheduling date calculations.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTCAL_DATE | DATE | 4 | — | Calendar date |
| 2 | MTCAL_DESC | STRING | 25 | — | Description (holiday name, special day note) |
| 3 | MTCAL_SAT | STRING | 1 | — | Saturday working flag: `Y`=Saturday is a working day |
| 4 | MTCAL_SUN | STRING | 1 | — | Sunday working flag: `Y`=Sunday is a working day |
| 5 | MTCAL_YEAR | INTEGER | 2 | — | Year (2-digit) |

## SCHEDCAL
**SCHEDULING SHOP CALENDAR** — pre-computed shop-day calendar

Fields: 6 | Key: SCH_CAL_DATE

Pre-computed mapping of calendar dates to shop day numbers. Used by the scheduler to
perform shop-day arithmetic without re-walking the calendar on each calculation.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | SCH_BACK_DATE | NUMERIC | 8 | — | If Holiday/WE Date is backed off one day |
| 2 | SCH_BACK_SLASH | DATE | 4 | — | Shop Back Date — calendar date after backing off weekend/holiday |
| 3 | SCH_CAL_DATE | DATE | 4 | — | Calendar date |
| 4 | SCH_SHOP_DATE | NUMERIC | 8 | — | Shop Date — Julian floating-point shop day number |
| 5 | SCH_SHOP_SLASH | DATE | 4 | — | Shop date display format (// = formatted date) |
| 6 | SCH_WH_FLAG | STRING | 1 | — | Weekend/Holiday flag: `H`=holiday, `W`=weekend |

## SCHWO
**FINITE SCHEDULING TEMP FILE** — per-WO scheduling summary

Fields: 10 | Key: SWO_WOPRE + SWO_WOSUF

One record per WO during a scheduling run. Holds aggregate scheduling values used by the
scheduler to sort and assign WOs to time buckets.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | SWO_CONTENTION | NUMERIC | 8 | — | Contention count (total number of WOs competing for same WC windows) |
| 2 | SWO_CRATIO | NUMERIC | 8 | 5 | Critical ratio (due date priority) |
| 3 | SWO_DAYS_TOGO | NUMERIC | 8 | — | Days Remaining (calendar days until WO due date) |
| 4 | SWO_OPCOUNT | INTEGER | 2 | — | Operation Count (number of routing operations) |
| 5 | SWO_RUN_DAYS | NUMERIC | 8 | 4 | Run Days (total scheduled run time in shop days) |
| 6 | SWO_SHOP_DUE | NUMERIC | 8 | — | Due date expressed as shop day number |
| 7 | SWO_SHOP_FINISH | NUMERIC | 8 | — | Calculated scheduled finish as shop day number |
| 8 | SWO_SHOP_START | NUMERIC | 8 | — | Calculated scheduled start as shop day number |
| 9 | SWO_WOPRE | NUMERIC | 8 | — | Work Order Prefix |
| 10 | SWO_WOSUF | INTEGER | 2 | — | Work Order Suffix |

## WCCTL
**FINITE SCHEDULING TEMP FILE** — work center control state during scheduling run

Fields: 5 | Key: WCTL_WC

One record per work center. Tracks the current scheduled load window during the
scheduling engine's forward-pass calculation.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | WCTL_COUNT | NUMERIC | 8 | — | Count of WOs/buckets currently scheduled to this WC |
| 2 | WCTL_FLAG | STRING | 1 | — | Processing flag (marks WC as processed in current pass) |
| 3 | WCTL_START | NUMERIC | 8 | — | Current earliest available start time (shop day float) |
| 4 | WCTL_STOP | NUMERIC | 8 | — | Current latest available stop time (shop day float) |
| 5 | WCTL_WC | STRING | 12 | — | Work center code (PK, FK → WORKCTR) |

## WCTRSLOD
**TEMP WORK CENTER LOAD % FOR VISUAL SCHEDULER** — WC load summary by date

Fields: 8 | Key: WCTL_WC + WC_LOAD_DATE

One record per work center × date. Used by the visual scheduler Gantt chart to display
load/utilization bars.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | WC_LOAD_CAP | NUMERIC | 8 | 2 | Work center capacity in hours for this date |
| 2 | WC_LOAD_DATE | DATE | 4 | — | Load date |
| 3 | WC_LOAD_EXTRA | STRING | 100 | — | Extra data |
| 4 | WC_LOAD_LOAD | NUMERIC | 8 | 2 | Scheduled load hours for this date |
| 5 | WC_LOAD_TOTHRS | NUMERIC | 8 | 2 | Total hours scheduled across all WOs for this WC+date |
| 6 | WC_LOAD_UDATE | DATE | 4 | — | Last update date (when this row was recalculated) |
| 7 | WC_LOAD_UTIL | NUMERIC | 8 | 2 | Utilization percentage (LOAD / CAP × 100) |
| 8 | WC_LOAD_WC | STRING | 12 | — | Work center code (FK → WORKCTR) |

## WORKSORD
**TEMP WORK ORDER HEADER FOR VISUAL SCHEDULER** — WO master clone for scheduling display

Fields: 82 | Key: MTWO_WIP_WOPRE + MTWO_WIP_WOSUF

Copy of WORKORD/WORKIP fields populated for the visual scheduler. Same MTWO_WIP_* schema.
See docs/03-modules/wo-work-orders/README.md for full WORKORD/WORKIP field documentation.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTWO_CUSTCODE | STRING | 10 | — | Customer Code |
| 2 | MTWO_CUSTNAME | STRING | 25 | — | Customer Name |
| 3 | MTWO_WIP_AEXTRA | NUMERIC | 8 | 2 | Actual extra/miscellaneous overhead cost |
| 4 | MTWO_WIP_AFIN | DATE | 4 | — | Actual Finish Date |
| 5 | MTWO_WIP_AFOVHD | NUMERIC | 8 | 2 | Actual fixed overhead cost |
| 6 | MTWO_WIP_ALABOR | NUMERIC | 8 | 2 | Actual Labor Cost |
| 7 | MTWO_WIP_AMAT | NUMERIC | 8 | 2 | Actual Material Cost |
| 8 | MTWO_WIP_AMISC | NUMERIC | 8 | 2 | Actual miscellaneous cost |
| 9 | MTWO_WIP_AOTH | NUMERIC | 8 | 2 | Actual other cost |
| 10 | MTWO_WIP_AOUTPR | NUMERIC | 8 | 2 | Actual Outside Process Cost |
| 11 | MTWO_WIP_ASETUP | NUMERIC | 8 | 2 | Actual Setup Cost |
| 12 | MTWO_WIP_ASTART | DATE | 4 | — | Actual Start Date |
| 13 | MTWO_WIP_ATOTAL | NUMERIC | 8 | 2 | Actual Total Cost |
| 14 | MTWO_WIP_AVOVHD | NUMERIC | 8 | 2 | Actual variable overhead cost |
| 15 | MTWO_WIP_BLANK | STRING | 1 | — | Reserved/blank placeholder field |
| 16 | MTWO_WIP_CHGORD | INTEGER | 2 | — | Change order number |
| 17 | MTWO_WIP_CODE | STRING | 15 | — | WO item code (part number being manufactured) |
| 18 | MTWO_WIP_COMQTY | NUMERIC | 8 | 2 | Completed quantity (receipts to date) |
| 19 | MTWO_WIP_CONTAT | STRING | 25 | — | Customer contact name |
| 20 | MTWO_WIP_CUSORD | STRING | 25 | — | Customer purchase order number |
| 21 | MTWO_WIP_DDATE | DATE | 4 | — | Due date (WO required completion date) |
| 22 | MTWO_WIP_DESC | STRING | 30 | — | WO description (item description) |
| 23 | MTWO_WIP_EEXTRA | NUMERIC | 8 | 2 | Estimated extra overhead cost |
| 24 | MTWO_WIP_EFOVHD | NUMERIC | 8 | 2 | Estimated fixed overhead cost |
| 25 | MTWO_WIP_ELABOR | NUMERIC | 8 | 2 | Est. Labor Cost |
| 26 | MTWO_WIP_EMAT | NUMERIC | 8 | 2 | Est. Material Cost |
| 27 | MTWO_WIP_EMISC | NUMERIC | 8 | 2 | Estimated miscellaneous cost |
| 28 | MTWO_WIP_EOTH | NUMERIC | 8 | 2 | Estimated other cost |
| 29 | MTWO_WIP_EOUTPR | NUMERIC | 8 | 2 | Est. Outside Process Cost |
| 30 | MTWO_WIP_ESETUP | NUMERIC | 8 | 2 | Est. Setup Cost |
| 31 | MTWO_WIP_EST | NUMERIC | 8 | — | Estimate number (source estimate/quote for this WO) |
| 32 | MTWO_WIP_ETOT | NUMERIC | 8 | 2 | Estimated Total Cost |
| 33 | MTWO_WIP_EXTRA^ | NUMERIC | 8 | 2 | Extra cost variance (actual vs. estimated) |
| 34 | MTWO_WIP_EXTRAV | NUMERIC | 8 | 2 | Extra cost variance detail |
| 35 | MTWO_WIP_FOVHD^ | NUMERIC | 8 | 2 | Fixed overhead variance |
| 36 | MTWO_WIP_FOVHDV | NUMERIC | 8 | 2 | Fixed overhead variance detail |
| 37 | MTWO_WIP_INSTR_1 | STRING | 60 | — | WO instruction line 1 |
| 38 | MTWO_WIP_INSTR_10 | STRING | 60 | — | WO instruction line 10 |
| 39 | MTWO_WIP_INSTR_2 | STRING | 60 | — | WO instruction line 2 |
| 40 | MTWO_WIP_INSTR_3 | STRING | 60 | — | WO instruction line 3 |
| 41 | MTWO_WIP_INSTR_4 | STRING | 60 | — | WO instruction line 4 |
| 42 | MTWO_WIP_INSTR_5 | STRING | 60 | — | WO instruction line 5 |
| 43 | MTWO_WIP_INSTR_6 | STRING | 60 | — | WO instruction line 6 |
| 44 | MTWO_WIP_INSTR_7 | STRING | 60 | — | WO instruction line 7 |
| 45 | MTWO_WIP_INSTR_8 | STRING | 60 | — | WO instruction line 8 |
| 46 | MTWO_WIP_INSTR_9 | STRING | 60 | — | WO instruction line 9 |
| 47 | MTWO_WIP_LABOR^ | NUMERIC | 8 | 2 | Labor cost total (^=actual+variance combined) |
| 48 | MTWO_WIP_LABORV | NUMERIC | 8 | 2 | Labor cost variance |
| 49 | MTWO_WIP_LOC | STRING | 10 | — | Warehouse location for WO output |
| 50 | MTWO_WIP_LOCK | STRING | 1 | — | Concurrent edit lock flag |
| 51 | MTWO_WIP_MAT^ | NUMERIC | 8 | 2 | Material cost total |
| 52 | MTWO_WIP_MATV | NUMERIC | 8 | 2 | Material cost variance |
| 53 | MTWO_WIP_MISC^ | NUMERIC | 8 | 2 | Miscellaneous cost total |
| 54 | MTWO_WIP_MISCV | NUMERIC | 8 | 2 | Miscellaneous cost variance |
| 55 | MTWO_WIP_MULT | STRING | 1 | — | Multiple WO flag: `Y`=this is part of a multi-WO release |
| 56 | MTWO_WIP_OTHPER | NUMERIC | 8 | 2 | Other period cost |
| 57 | MTWO_WIP_OTHV | NUMERIC | 8 | 2 | Other cost variance |
| 58 | MTWO_WIP_OUTPR^ | NUMERIC | 8 | 2 | Outside process cost total |
| 59 | MTWO_WIP_OUTPRV | NUMERIC | 8 | 2 | Outside process variance |
| 60 | MTWO_WIP_PPRCE | NUMERIC | 8 | 4 | Planned unit price |
| 61 | MTWO_WIP_PROJ | STRING | 15 | — | Project code |
| 62 | MTWO_WIP_PRTY | STRING | 1 | — | Priority |
| 63 | MTWO_WIP_QCONV | STRING | 1 | — | Quantity conversion flag |
| 64 | MTWO_WIP_SCHED_1 | STRING | 1 | — | Scheduling flag 1 (used by visual scheduler state machine) |
| 65 | MTWO_WIP_SCHED_2 | STRING | 1 | — | Scheduling flag 2 |
| 66 | MTWO_WIP_SCONV | STRING | 1 | — | Scheduling conversion flag |
| 67 | MTWO_WIP_SETUP^ | NUMERIC | 8 | 2 | Setup cost total |
| 68 | MTWO_WIP_SETUPV | NUMERIC | 8 | 2 | Setup cost variance |
| 69 | MTWO_WIP_SFIN | DATE | 4 | — | Scheduled Finish Date |
| 70 | MTWO_WIP_SOLINE | NUMERIC | 8 | — | SO line number linked to this WO |
| 71 | MTWO_WIP_SONUM | NUMERIC | 8 | — | SO Number |
| 72 | MTWO_WIP_SQTY | NUMERIC | 8 | 2 | Start Quantity (original WO quantity) |
| 73 | MTWO_WIP_SSTART | DATE | 4 | — | Scheduled Start Date |
| 74 | MTWO_WIP_STATUS | STRING | 1 | — | Status (E=Estimate, O=Open, H=Hold, C=Closed, X=Cancelled) |
| 75 | MTWO_WIP_TOT^ | NUMERIC | 8 | 2 | Total cost (actual) |
| 76 | MTWO_WIP_TOTV | NUMERIC | 8 | 2 | Total cost variance |
| 77 | MTWO_WIP_USERCD | STRING | 1 | — | User-defined category code |
| 78 | MTWO_WIP_VOVHD | NUMERIC | 8 | 2 | Variable overhead cost |
| 79 | MTWO_WIP_VOVHD^ | NUMERIC | 8 | 2 | Variable overhead cost total |
| 80 | MTWO_WIP_VOVHDV | NUMERIC | 8 | 2 | Variable overhead variance |
| 81 | MTWO_WIP_WOPRE | NUMERIC | 8 | — | WO Prefix |
| 82 | MTWO_WIP_WOSUF | INTEGER | 2 | — | WO Suffix |

## WOSROUT
**TEMP WORK ORDER ROUTING FOR VISUAL SCHEDULER** — WO routing clone for scheduling

Fields: 83 | Key: MTWORO_WOPRE + MTWORO_WOSUF + MTWORO_OPER

Copy of WOHROUT/WOROUT routing fields for the visual scheduler. Same MTWORO_* schema.
See docs/03-modules/wo-work-orders/README.md for full routing field documentation.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTWORO_^COMP | INTEGER | 2 | — | Completion flag (internal scheduling state) |
| 2 | MTWORO_ACTHRS | NUMERIC | 8 | 4 | Actual run hours charged |
| 3 | MTWORO_AFOHCST | NUMERIC | 8 | 4 | Actual fixed overhead cost |
| 4 | MTWORO_ALABCST | NUMERIC | 8 | 4 | Actual labor cost |
| 5 | MTWORO_AMCHCST | NUMERIC | 8 | 4 | Actual machine cost |
| 6 | MTWORO_AOUTCST | NUMERIC | 8 | 4 | Actual outside process cost |
| 7 | MTWORO_ASETCST | NUMERIC | 8 | 4 | Actual setup cost |
| 8 | MTWORO_ASETHRS | NUMERIC | 8 | 4 | Actual setup hours |
| 9 | MTWORO_AVOHCST | NUMERIC | 8 | 4 | Actual variable overhead cost |
| 10 | MTWORO_CODE | STRING | 15 | — | Item code being processed on this operation |
| 11 | MTWORO_CONTNTN | NUMERIC | 8 | — | Contention count for this operation's work center |
| 12 | MTWORO_DEPT | STRING | 3 | — | Department code |
| 13 | MTWORO_DESC | STRING | 30 | — | Operation description |
| 14 | MTWORO_EFOHCST | NUMERIC | 8 | 4 | Estimated fixed overhead cost |
| 15 | MTWORO_ELABCST | NUMERIC | 8 | 4 | Estimated labor cost |
| 16 | MTWORO_EMCHCST | NUMERIC | 8 | 4 | Estimated machine cost |
| 17 | MTWORO_EOUTCST | NUMERIC | 8 | 4 | Estimated outside process cost |
| 18 | MTWORO_ESETCST | NUMERIC | 8 | 4 | Estimated setup cost |
| 19 | MTWORO_ESETHRS | NUMERIC | 8 | 4 | Estimated setup hours |
| 20 | MTWORO_ESSTHRS | TIME | 4 | — | Estimated standard time per piece (time-per-piece format) |
| 21 | MTWORO_ESTHRS | NUMERIC | 8 | 4 | Estimated run hours total |
| 22 | MTWORO_EVOHCST | NUMERIC | 8 | 4 | Estimated variable overhead cost |
| 23 | MTWORO_EXTRA | STRING | 150 | — | Extra data |
| 24 | MTWORO_FINISH | DATE | 4 | — | Planned finish date |
| 25 | MTWORO_FINISH2 | DATE | 4 | — | Alternate/secondary finish date |
| 26 | MTWORO_FINISHED | DATE | 4 | — | Actual finish date |
| 27 | MTWORO_INSTR_1 | STRING | 60 | — | Operation instruction line 1 |
| 28 | MTWORO_INSTR_10 | STRING | 60 | — | Operation instruction line 10 |
| 29 | MTWORO_INSTR_11 | STRING | 60 | — | Operation instruction line 11 |
| 30 | MTWORO_INSTR_12 | STRING | 60 | — | Operation instruction line 12 |
| 31 | MTWORO_INSTR_13 | STRING | 60 | — | Operation instruction line 13 |
| 32 | MTWORO_INSTR_14 | STRING | 60 | — | Operation instruction line 14 |
| 33 | MTWORO_INSTR_15 | STRING | 60 | — | Operation instruction line 15 |
| 34 | MTWORO_INSTR_2 | STRING | 60 | — | Operation instruction line 2 |
| 35 | MTWORO_INSTR_3 | STRING | 60 | — | Operation instruction line 3 |
| 36 | MTWORO_INSTR_4 | STRING | 60 | — | Operation instruction line 4 |
| 37 | MTWORO_INSTR_5 | STRING | 60 | — | Operation instruction line 5 |
| 38 | MTWORO_INSTR_6 | STRING | 60 | — | Operation instruction line 6 |
| 39 | MTWORO_INSTR_7 | STRING | 60 | — | Operation instruction line 7 |
| 40 | MTWORO_INSTR_8 | STRING | 60 | — | Operation instruction line 8 |
| 41 | MTWORO_INSTR_9 | STRING | 60 | — | Operation instruction line 9 |
| 42 | MTWORO_LEAD | INTEGER | 2 | — | Lead time (days before this operation can start after prior one) |
| 43 | MTWORO_LONGTIME | NUMERIC | 8 | 7 | Long-run time (extended run hours for run-time items) |
| 44 | MTWORO_MACHNO | STRING | 4 | — | Machine number/ID assigned to this operation |
| 45 | MTWORO_MD_PR_HR | STRING | 1 | — | Mode: `P`=price per piece, `H`=price per hour |
| 46 | MTWORO_MIN_CHG | NUMERIC | 8 | 2 | Minimum charge hours (even if actual < this amount) |
| 47 | MTWORO_MISCACST | NUMERIC | 8 | 2 | Actual miscellaneous cost |
| 48 | MTWORO_MISCCOST | NUMERIC | 8 | 2 | Estimated miscellaneous cost |
| 49 | MTWORO_MISCDESC | STRING | 30 | — | Miscellaneous cost description |
| 50 | MTWORO_NEGOVLP | NUMERIC | 8 | 2 | Negative overlap (schedule prior ops later to start this one sooner) |
| 51 | MTWORO_NUM | INTEGER | 2 | — | Internal operation sequence number |
| 52 | MTWORO_NUM_PERS | NUMERIC | 8 | 2 | Number of persons required for this operation |
| 53 | MTWORO_NUM_PROC | INTEGER | 2 | — | Number of processes/machines running in parallel |
| 54 | MTWORO_OP_TEMP^ | INTEGER | 2 | — | Operation template reference flag |
| 55 | MTWORO_OPER | INTEGER | 2 | — | Operation sequence number (PK component) |
| 56 | MTWORO_OPER2 | INTEGER | 2 | — | Secondary operation number (for split operations) |
| 57 | MTWORO_OPERDESC | STRING | 30 | — | Operation description (from routing master) |
| 58 | MTWORO_OVERLAP | INTEGER | 2 | — | Overlap quantity (units to release before prior op completes) |
| 59 | MTWORO_PARTSHR | NUMERIC | 8 | 2 | Parts per hour rate |
| 60 | MTWORO_PIECE_RT | NUMERIC | 8 | 2 | Piece rate (labor cost per unit) |
| 61 | MTWORO_PO | NUMERIC | 8 | — | PO number (for outside process operations) |
| 62 | MTWORO_PR_PERHR | NUMERIC | 8 | 2 | Price per hour (outside process billing rate) |
| 63 | MTWORO_PRINT | STRING | 1 | — | Print flag: `Y`=include this operation on shop traveler |
| 64 | MTWORO_PRIORITY | STRING | 1 | — | Priority override for this operation |
| 65 | MTWORO_PROJ | NUMERIC | 8 | — | Project number |
| 66 | MTWORO_QTYCOM | NUMERIC | 8 | 2 | Quantity completed at this operation |
| 67 | MTWORO_SCHED_WC | STRING | 12 | — | Scheduled work center (may differ from assigned WC during scheduling) |
| 68 | MTWORO_SCRAPPED | NUMERIC | 8 | 2 | Quantity scrapped at this operation |
| 69 | MTWORO_SQTY | NUMERIC | 8 | 2 | Starting quantity entering this operation |
| 70 | MTWORO_START | DATE | 4 | — | Planned start date |
| 71 | MTWORO_STARTED | DATE | 4 | — | Actual start date |
| 72 | MTWORO_STD_TIME | STRING | 1 | — | Standard time flag: `Y`=use standard time, `N`=use actual |
| 73 | MTWORO_STQTY | NUMERIC | 8 | 2 | Remaining quantity at this operation |
| 74 | MTWORO_TIME_PPR | TIME | 4 | — | Time per piece (for piece-rate operations) |
| 75 | MTWORO_TIMEPART | TIME | 4 | — | Partial operation time remaining |
| 76 | MTWORO_TOOL | STRING | 15 | — | Tool or mold ID required for this operation |
| 77 | MTWORO_TYPE | STRING | 1 | — | Operation type: `M`=machine, `L`=labor, `O`=outside process |
| 78 | MTWORO_VEND | STRING | 10 | — | Vendor code (for outside process operations, FK → BKAPVEND) |
| 79 | MTWORO_VENDNAME | STRING | 30 | — | Vendor name (denormalized) |
| 80 | MTWORO_WC | STRING | 12 | — | Work center code |
| 81 | MTWORO_WCDESC | STRING | 30 | — | Work center description (denormalized) |
| 82 | MTWORO_WOPRE | NUMERIC | 8 | — | WO Prefix |
| 83 | MTWORO_WOSUF | INTEGER | 2 | — | WO Suffix |

**Confidence: 82/100** — BUCKETS/SCHWO/WCCTL/WCTRSLOD scheduling semantics inferred from
finite scheduling workflow context; WORKSORD/WOSROUT field meanings derived from WORKORD/MTWORO
parallels (same MTWO_WIP_*/MTWORO_* schemas); CALENDAR/SCHEDCAL descriptions from Excel confirmed;
scheduling-engine internals (CRATIO exact formula, shop-day float encoding, contention algorithm)
require RWN decryption.
