# EvoERP Data Dictionary — Tier 3 Tables

Status: partial — extracted from Pervasive DDF schema 2026-06-17.
Purpose: document the next tier of important tables not yet covered in tier1/tier2.

---

## MTICMSTR — MT-generation Inventory Master

**Purpose:** The MT (second-generation) inventory master. Replaces/extends BKICMSTR
in newer code. Opened as MTICMSTR by T7* modules; BKICMSTR used by older BK* modules.
Both tables store item master data, but MTICMSTR has more fields.

Primary key: MTIC_PROD_CODE (inferred from usage)
Record size: 1,533 bytes, 108 fields

| Offset | Field | Type | Size | Meaning |
|---|---|---|---|---|
| 0 | MTIC_PROD_CLASS | STRING | 4 | Item class code |
| 4 | MTIC_PROD_CODE | STRING | 15 | **Part number** (primary key) |
| 19 | MTIC_PROD_DESC | STRING | 30 | Item description |
| 49 | MTIC_PROD_SUM | STRING | 3 | Stock UOM |
| 52 | MTIC_PROD_PUM | STRING | 3 | Purchase UOM |
| 55 | MTIC_PROD_PCONV | FLOAT | 8 | Purchase-to-stock UOM conversion factor |
| 63 | MTIC_PROD_CYCLE | STRING | 1 | Cycle count flag |
| 64 | MTIC_PROD_ABC | STRING | 1 | ABC classification (A/B/C) |
| 65 | MTIC_PROD_LOT | STRING | 1 | Lot tracking Y/N |
| 66 | MTIC_PROD_SER | STRING | 1 | Serial tracking Y/N |
| 67 | MTIC_PROD_ACTIV | STRING | 1 | Active flag (Y/N) |
| 68 | MTIC_PROD_STDPK | FLOAT | 8 | Standard pack quantity |
| 76 | MTIC_PROD_WT | FLOAT | 8 | Weight |
| 84 | MTIC_PROD_CUBFT | FLOAT | 8 | Cubic feet (volume) |
| 92 | MTIC_PROD_LEAD | UBINARY | 2 | Lead time (days) |
| 94 | MTIC_PROD_LOC | STRING | 10 | Primary stock location |
| 104 | MTIC_PROD_DRAW | STRING | 15 | Drawing number |
| 119 | MTIC_PROD_REV | STRING | 5 | Revision level |
| 124 | MTIC_PROD_COST | STRING | 1 | Cost method (S=standard, A=average, L=LIFO, F=FIFO) |
| 125 | MTIC_PROD_ESTCD | STRING | 1 | Estimating code |
| 126 | MTIC_PROD_MRP | STRING | 1 | MRP flag (include in MRP or not) |
| 127 | MTIC_PROD_GLINV | STRING | 10 | GL inventory account |
| 137 | MTIC_PROD_INVDP | STRING | 4 | Inventory department |
| 141 | MTIC_PROD_GLWIP | STRING | 10 | GL WIP account |
| 151 | MTIC_PROD_WIPDP | STRING | 4 | WIP department |
| 155–484 | MTIC_PROD_SPECS_1..12 | STRING | 30 each | 12 specification text lines |
| 515 | MTIC_PROD_UOWO | FLOAT | 8 | Units on open work orders |
| 523 | MTIC_PROD_UOA | FLOAT | 8 | Units on allocation |
| 531 | MTIC_PROD_COMM | FLOAT | 8 | Committed quantity |
| 539 | MTIC_PROD_STDC | FLOAT | 8 | Standard cost (current) |
| 547 | MTIC_PROD_TYPE | STRING | 1 | **Item type** — same codes as BKIC_PROD_TYPE (R/F/A/M/N/L/K/B/T/O) |
| 548–672 | MTIC_PROD_SUBST_1..5 | STRING | 25 each | Up to 5 substitute part numbers |
| 673 | MTIC_PROD_FRT | FLOAT | 8 | Freight cost per unit |
| 681 | MTIC_PROD_MRPSW | STRING | 1 | MRP switch (additional flag) |
| 682 | MTIC_PROD_UIWIP | FLOAT | 8 | Units in WIP |
| 690 | MTIC_PROD_AVAIL | FLOAT | 8 | Available quantity (UOH - allocated) |
| 698 | MTIC_PROD_OPTPR | UBINARY | 2 | Options/pricing flag |
| 700 | MTIC_PROD_CUST | STRING | 10 | Customer code (for customer-specific items) |
| 710 | MTIC_PROD_CUSNM | STRING | 30 | Customer name |
| 740 | MTIC_PROD_CLDES | STRING | 30 | Class description |
| 770–869 | MTIC_PROD_VEND_1..10 | STRING | 10 each | Up to 10 preferred vendor codes |
| 870–1169 | MTIC_PROD_VNAM_1..10 | STRING | 30 each | Vendor names |
| 1170–1349 | MTIC_PROD_VPC_1..9 | STRING | 20 each | Vendor part codes |
| 1350–1469 | MTIC_PROD_RCOST_1..15 | FLOAT | 8 each | 15-slot rolling cost history |
| 1470 | MTIC_PROD_OPT | STRING | 1 | Options flag |
| 1471 | MTIC_PROD_LOTSZ | FLOAT | 8 | Lot/order size |
| 1479 | MTIC_PROD_OPTCS | STRING | 1 | Options cost flag |
| 1480 | MTIC_PROD_OPTCD | STRING | 5 | Options code |
| 1485 | MTIC_PROD_UIQC | FLOAT | 8 | Units in QC |
| 1501 | MTIC_PROD_EXPBF | UBINARY | 2 | Expire before (days) — lot expiry warning threshold |
| 1503 | MTIC_PROD_DELBF | UBINARY | 2 | Delete before (days) — lot deletion threshold |
| 1505 | MTIC_PROD_CUM | STRING | 3 | Customer UOM |
| 1508 | MTIC_PROD_LONGP | STRING | 25 | Long part description |

**Key differences from BKICMSTR (617 bytes):**
- 10 preferred vendors + names + vendor part codes (vs. fewer in BKICMSTR)
- 15 rolling cost history slots
- 12 spec lines (vs. fewer)
- 5 substitute parts
- UOWO, AVAIL, UIWIP quantity fields
- LOTSZ, EXPBF, DELBF for lot management
- LONGP, CUM additional description fields

---

## BKBMMSTR — Bill of Materials Component Record

**Purpose:** Each row is one BOM component line. A finished product's BOM is the set of
all rows where BKBM_PARENT = the product's part code.

Identical structure to BKBMAVAL (alternate BOM) and BKBMAMTR (auto-calculated BOM).

Primary key: BKBM_PARENT + BKBM_COMPONENT
Record size: ~215 bytes, 26 fields

| Offset | Field | Type | Size | Meaning |
|---|---|---|---|---|
| 0 | BKBM_PARENT | STRING | 15 | Parent item (finished/assembly part number) |
| 17 | BKBM_COMPONENT | STRING | 15 | Component part number |
| 32 | BKBM_QTY_REQD | FLOAT | 8 | Quantity of component per unit of parent |
| 40 | BKBM_REFERENCE | STRING | 20 | Reference designator (e.g., R1, C4 in PCBs) |
| 60 | BKBM_PROD_TYPE | STRING | 1 | Component type (mirrors BKIC_PROD_TYPE) |
| 61 | BKBM_PROD_SCRAP | FLOAT | 8 | Scrap rate (% extra to order) |
| 69 | BKBM_PROD_OP | STRING | 3 | Routing operation where this component is consumed |
| 72–77 | BKBM_PROD_OPYN_1..6 | STRING | 1 each | 6 per-operation Y/N flags |
| 78 | BKBM_PROD_PRICE | FLOAT | 8 | Component price (for estimating) |
| 86 | BKBM_PROD_RTNUM | UBINARY | 2 | Routing number |
| 88 | BKBM_PROD_DUPOP | STRING | 1 | Duplicate operation flag |
| 89 | BKBM_PROD_OPDSC | STRING | 5 | Operation description code |
| 94 | BKBM_PROD_VEND | STRING | 10 | Vendor (for outside process components) |
| 104 | BKBM_DATE1 | DATE | 4 | Effectivity start date |
| 108 | BKBM_DATE2 | DATE | 4 | Effectivity end date |
| 112 | BKBM_EXTRA | STRING | 50 | Extra notes |
| 162 | BKBM_REV | STRING | 5 | BOM revision |
| 167 | BKBM_P_TYPE | STRING | 10 | Parent item type description |
| 177 | BKBM_C_TYPE | STRING | 10 | Component item type description |
| 187 | BKBM_EST_LINE | FLOAT | 8 | Estimating line cost |
| 195 | BKBM_UID | STRING | 20 | Unique identifier |

**BOM variant tables** (same structure):
- `BKBMMSTR` — active production BOM
- `BKBMAVAL` — alternate/validation BOM
- `BKBMAMTR` — auto-calculated/master BOM

---

## BKRTEMTR — MT-Generation Routing Master

**Purpose:** Each row is one routing operation for one part. A part's full routing is all
rows where MTRO_CODE = the part number, ordered by MTRO_OPER.

Primary key: MTRO_CODE + MTRO_OPER
Record size: ~1,514 bytes, 62 fields

| Offset | Field | Type | Size | Meaning |
|---|---|---|---|---|
| 0 | MTRO_CODE | STRING | 15 | Part number |
| 15 | MTRO_OPER | UBINARY | 2 | Operation sequence number |
| 17 | MTRO_DESC | STRING | 30 | Operation description |
| 47 | MTRO_OPERDESC | STRING | 30 | Alternate operation description |
| 77 | MTRO_TYPE | STRING | 1 | Operation type (L=labor, S=standard, O=outside process) |
| 78 | MTRO_LEAD | UBINARY | 2 | Lead time for this operation |
| 80 | MTRO_VENDCOST | FLOAT | 8 | Outside process vendor cost |
| 88 | MTRO_PARTSHR | FLOAT | 8 | Parts per hour (throughput rate) |
| 96 | MTRO_TIMEPART | TIME | 4 | Time per part |
| 100 | MTRO_SETUPHRS | TIME | 4 | Setup time per run |
| 104 | MTRO_LOTSIZE | FLOAT | 8 | Lot size for this operation |
| 112–891 | MTRO_INSTR_1..14 | STRING | 60 each | 14 work instruction lines |

**Note:** Work centers are linked to routing operations via a separate relationship
table, not directly in BKRTEMTR. The routing record references a work center code.

Related tables: `BKRTCST` (routing cost/quote snapshots), `BKRTSPEC` (special notes, 4 lines per op).

---

## WORKCTR — Work Center Master

**Purpose:** Defines production resources (machines, labor groups) used in routings.
Also used for capacity planning in scheduling.

Primary key: MTWC_WC
Record size: ~468 bytes, 47 fields

| Offset | Field | Type | Size | Meaning |
|---|---|---|---|---|
| 0 | MTWC_WC | STRING | 12 | Work center code (primary key) |
| 12 | MTWC_WCDESC | STRING | 30 | Work center description |
| 42 | MTWC_DEPT | STRING | 4 | Department code |
| 46 | MTWC_DEPTDESC | STRING | 30 | Department description |
| 76 | MTWC_HRSWEEK | UBINARY | 2 | Available hours per week |
| 86 | MTWC_SETUP | FLOAT | 8 | Setup rate ($/hr) |
| 94 | MTWC_LABOR | FLOAT | 8 | Labor rate ($/hr) |
| 102 | MTWC_MACHINE | FLOAT | 8 | Machine rate ($/hr) |
| 110 | MTWC_AVGQTIME | UBINARY | 2 | Average queue time (days) |
| 112–117 | MTWC_QPR1..3 | UBINARY | 2 each | Queue priority ratios |
| 118 | MTWC_VOVHD | FLOAT | 8 | Variable overhead rate |
| 126 | MTWC_FOVHD | FLOAT | 8 | Fixed overhead rate |
| 134 | MTWC_LEAD | UBINARY | 2 | Lead time |
| 136 | MTWC_OUTPROC | STRING | 1 | Outside process flag (Y/N) |
| 137 | MTWC_EST_VOVHD | FLOAT | 8 | Estimated variable overhead rate |
| 145 | MTWC_HRS_SHIFT | UBINARY | 2 | Hours per shift |
| 147 | MTWC_MIN_CHG | FLOAT | 8 | Minimum charge |
| 155 | MTWC_COST_LB | FLOAT | 8 | Cost per labor unit |
| 163 | MTWC_EXTRA | STRING | 100 | Extra notes |
| 263 | MTWC_PARENT_YN | STRING | 1 | Has parent work center (Y/N) |
| 264 | MTWC_PARENT_WC | STRING | 12 | Parent work center (for hierarchy) |
| 276 | MTWC_LEVEL_YN | STRING | 1 | Level flag |
| 277–295 | MTWC_CYCLE_TIME_1..10 | UBINARY | 2 each | 10 cycle time slots |
| 297–304 | MTWC_GDATE_1..2 | DATE | 4 each | Gate/milestone dates |
| 305–309 | MTWC_FLAGS_1..5 | STRING | 1 each | 5 user-defined flags |
| 310 | MTWC_GNUM | FLOAT | 8 | Gate number |
| 318–467 | MTWC_ALPHA_1..5 | STRING | 30 each | 5 user-defined text fields |

---

## ISNOTES — Notes / EvoNotes Table

**Purpose:** Stores all internal notes entered via EvoNotes. Notes attach to any
EvoERP record via a 48-character composite key (IS_NOTE_ID).

Primary key: IS_NOTE_ID
Record size: 685 bytes (note: anomalous `BKAP_INVL_GLACT_48` field at offset 429 = DDF artifact, not a real field)

| Offset | Field | Type | Size | Meaning |
|---|---|---|---|---|
| 0 | IS_NOTE_ID | STRING | 48 | Composite key: identifies the parent record (e.g., customer code + note sequence) |
| 48 | IS_NOTE_TYPE | STRING | 3 | Note type / module code (identifies which module's note this is) |
| 63 | IS_NOTE_CDATE | DATE | 4 | Created date |
| 67 | IS_NOTE_CTIME | STRING | 10 | Created time |
| 77 | IS_NOTE_CWHO | STRING | 15 | Created by (user name) |
| 92 | IS_NOTE_EDATE | DATE | 4 | Last edited date |
| 96 | IS_NOTE_ETIME | STRING | 10 | Last edited time |
| 106 | IS_NOTE_EWHO | STRING | 15 | Last edited by |
| 121 | IS_NOTE_EXTRA | STRING | 100 | Note body / extra text |
| 221 | IS_NOTE_PRIVATE | STRING | 1 | Private note flag (Y = only visible to creator) |
| 222 | IS_NOTE_GROUP | STRING | 4 | Note group / category code |
| 226 | IS_NOTE_CONTACT | STRING | 30 | Contact name associated with this note |

**Note format:** The note body itself ("IS_NOTE_EXTRA") is only 100 chars — long notes
are likely stored as multiple records with sequential IS_NOTE_ID values.

---

## ISSCHED — Scheduler Task Table

**Purpose:** Stores configured scheduled tasks for the EvoERP Scheduler.
Each row is one scheduled task definition.

Primary key: IS_SCHED_NAME
Record size: 3,649 bytes, 24 fields

| Offset | Field | Type | Size | Meaning |
|---|---|---|---|---|
| 0 | IS_SCHED_NAME | STRING | 50 | **Task name** (primary key) |
| 50 | IS_SCHED_DESC | STRING | 256 | Task description |
| 306 | IS_SCHED_PROG | STRING | 256 | **Program to run** (.RWN file path) |
| 562 | IS_SCHED_CO | STRING | 3 | Company code to run the task as |
| 565 | IS_SCHED_TYPE | STRING | 1 | Schedule type (O=once, R=recurring?, etc.) |
| 566 | IS_SCHED_DATE | DATE | 4 | Next scheduled run date |
| 570 | IS_SCHED_TIME | TIME | 4 | Next scheduled run time |
| 574 | IS_SCHED_RECUR | FLOAT | 8 | Recurrence interval (days or minutes) |
| 582 | IS_SCHED_LOG | STRING | 256 | Log output from last run |
| 838 | IS_SCHED_EXTRA | STRING | 100 | Additional notes |
| 938 | IS_SCHED_LDATE | DATE | 4 | Last run date |
| 942 | IS_SCHED_LTIME | TIME | 4 | Last run time |
| 946 | IS_SCHED_WHO | STRING | 15 | Last run by (user) |
| 961 | IS_SCHED_EMAIL | STRING | 128 | Email address for task completion notification |
| 1089–3392 | IS_SCHED_PARAM1..9 | STRING | 256 each | Up to 9 parameter slots passed to the scheduled program |
| 3393 | IS_SCHED_PARAM0 | STRING | 256 | Parameter slot 0 (10th parameter — note naming: 1-9, then 0) |

**Key insight:** The scheduler can run any `.RWN` program with up to 10 parameters
and email a notification to IS_SCHED_EMAIL on completion. The IS_SCHED_LOG field
stores the last run output for troubleshooting.

---

## BKRTCST — Routing Cost / Quote Snapshot

**Purpose:** Stores routing cost data for quotes and estimates.
One row per quote + part + operation combination.

Primary key: BKRT_QUOTE + BKRT_CODE + BKRT_OPER (inferred)

| Offset | Field | Type | Size | Meaning |
|---|---|---|---|---|
| 0 | BKRT_QUOTE | FLOAT | 8 | Quote/estimate number |
| 8 | BKRT_CODE | STRING | 15 | Part number |
| 23 | BKRT_OPER | UBINARY | 2 | Operation sequence number |
| 25–96 | BKRT_PARTSHR_1..10 | FLOAT | 8 each | Parts-per-hour by work center slot |
| 105–144 | BKRT_SETUP_1..10 | TIME | 4 each | Setup time by work center slot |
| 145 | BKRT_DATE | DATE | 4 | Date of this cost snapshot |

---

## BKRTSPEC — Routing Special Notes

**Purpose:** Up to 4 special instruction notes per routing operation line.

Primary key: BKRT_SPEC_PART + BKRT_SPEC_SEQ + BKRT_SPEC_LINE

| Offset | Field | Type | Size | Meaning |
|---|---|---|---|---|
| 0 | BKRT_SPEC_PART | STRING | 15 | Part number |
| 15 | BKRT_SPEC_SEQ | UBINARY | 2 | Routing operation sequence |
| 17 | BKRT_SPEC_LINE | UBINARY | 2 | Note line number (1–4) |
| 19–79 | BKRT_SPEC_NOTE_1..4 | STRING | 20 each | 4 note lines × 20 chars |
