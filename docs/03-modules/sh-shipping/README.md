# Scheduling (SH)

Status: verified | Pass 437 (2026-07-01)

> **Note:** folder name `sh-shipping/` is a legacy auto-classification
> artifact — the SH module is actually **Scheduling** (per the vendor
> help file's *Manufacturing → Scheduling* category and every one of
> the menu operations below). Folder name retained to avoid breaking
> URLs; contents and title corrected.

- **Module code**: `SH`
- **Tables**: 4 primary (`WORKORD`, `WOROUT`, `WORKCTR`, `BKSHORT`)
- **UI forms**: 14 (T7SHA through T7SHP + T7SHIPRTM)
- **Menu operations**: 16 (SH-A through SH-P)

→ See **[help-content.md](help-content.md)** for consolidated vendor help
(22 topics from `EvoHELP.CHM` covering all 4 scheduling methods, setup walkthrough,
shared vocabulary, and per-operation descriptions).

---

## What Scheduling does

SH assigns and adjusts **scheduled start/finish dates** on Work Order routing operations.
Each WO has a routing (a list of operations in WOROUT), each operation assigned to a
Work Center (WORKCTR). Scheduling fills in dates based on one of four methods:

1. **Finite** (SH-F) — forward from WO start; respects WC capacity (hours/day × % utilization)
2. **Infinite** (SH-F) — same logic but ignores capacity; all WCs effectively unlimited
3. **Lead Time** (SH-N/SH-P) — backward from WO due date using routing setup+run times + WC lead days
4. **Manual** (SH-A/SH-B) — user edits start/finish/due dates directly on each WO

The module does **not** issue, receive, or post inventory — it only fills in date fields
on WORKORD and WOROUT records. Actual production activity is recorded by WO and DC modules.

---

## Menu operations (16)

| Code | Operation | Program | DFM filters / notes |
|------|-----------|---------|---------------------|
| `SH-A` | Edit WO Start/Finish/Due Dates | T7SHA | WO# grid with Item/Desc/Customer; auto-entry mode toggle; edits Sched Start/Finish, Due Date, Priority, Class |
| `SH-B` | Manually Schedule Work Orders | T7SHB | WO drag-and-schedule UI; Auto-Entry OFF mode |
| `SH-C` | Manually Schedule Work Centers | T7SHC | WC/Dept/Total Hours/Day/% Utilization grid |
| `SH-D` | Manually Schedule Machines | — | Machine-level scheduling (no DFM in samples) |
| `SH-E` | Finite Scheduling — Due Date Change | T7SHE | "Enter a New Due Date to change Priority"; triggers reprocess |
| `SH-F` | Finite / Infinite Scheduling Engine | T7SHF | Filters: Status [FR], WO#/WO Start/WO Finish/Job#/WO Class/WO Priority/Planner Code ranges; "Process" button runs algorithm |
| `SH-G` | Print Work Order Schedule | T7SHG | WO Status/Class/Priority + Customer/Date ranges; sort options; Excluded Classes list |
| `SH-H` | Print Work Order Status | T7SHH | Same as SH-G + Status Codes filter |
| `SH-I` | Print Work Center Schedule (color) | T7SHI | Color-coded WC dispatch; configurable colors for Elapsed/Background + "Only show color for WOs Not Started on Time"; WC range + WO filters |
| `SH-J` | Print Machine Schedule | T7SHJ | Machine-based schedule report; WO Status/Class/Priority/Sort |
| `SH-K` | View Work Center Load | Java (WorkCenterLoad.jar) | Graphical Java view of WC capacity vs. demand (VSCHED) |
| `SH-L` | Print Work Center Load | T7SHL | Printed WC load report |
| `SH-M` | Lead Time Estimator | T7SHM | Item#/Desc/Qty/Start Date entry → estimates lead time from routing |
| `SH-N` | Generate Lead Times (batch) | T7SHN | Part Types filter + Item#/Item Class From/Thru → batch-updates MTWC_LEAD on WORKCTR |
| `SH-O` | Finite Schedule Bucket Report | T7SHO | Work Center From/Thru → shows capacity buckets from finite scheduling run |
| `SH-P` | Lead Time Scheduling (color) | T7SHP | Color threshold config (X/Y days from start date); WO Class/Start/Finish date ranges; uses MTWORO.FINISH for due-date comparison |

---

## Database tables

SH reads WORKORD and WOROUT (owned by WO module) and WORKCTR (owned by RO module).
The only table unique to SH is **BKSHORT** (shortage list).

### WORKORD — Work Order Master (74 fields)

Primary source: `docs/03-modules/wo-work-orders/README.md`
Key scheduling fields: `MTWO_WIP_SSTART` / `MTWO_WIP_SFIN` (scheduled start/finish),
`MTWO_WIP_ASTART` / `MTWO_WIP_AFIN` (actual), `MTWO_WIP_DDATE` (due date),
`MTWO_WIP_PRTY` (priority), `MTWO_WIP_STATUS` (status code), `MTWO_WIP_PRTY` (priority 1-9).

**Live data (i2 Systems):** 27 work centers active; 8,238 open WO routing operations.

### WOROUT — WO Routing Operations

One record per routing operation per WO. Key scheduling fields:
`MTWORO_FINISH` (scheduled finish), `MTWORO_START` (scheduled start), `MTWORO_WC` (work center),
`MTWORO_OPER` (operation code), `MTWORO_STD_TIME` / `MTWORO_ESTHRS` (standard/estimated hours).

**Live data:** 8,238 open operations across all active WOs.

### WORKCTR — Work Center Master (48 fields)

| Key field | Type | Meaning |
|-----------|------|---------|
| `MTWC_WC` | STRING 12 | Work center code (PK) |
| `MTWC_WCDESC` | STRING 30 | Description |
| `MTWC_DEPT` | STRING 4 | Department code |
| `MTWC_HRSWEEK` | UBINARY | Capacity hours per week (e.g. 2080 = 40h/wk × 52) |
| `MTWC_^UTIL` | FLOAT | % utilization rate (efficiency factor) |
| `MTWC_SETUP` | FLOAT/4dec | Setup cost rate ($/hr) |
| `MTWC_LABOR` | FLOAT/4dec | Labor cost rate ($/hr) |
| `MTWC_MACHINE` | FLOAT/4dec | Machine cost rate ($/hr) |
| `MTWC_AVGQTIME` | UBINARY | Average queue time (days) |
| `MTWC_QPR1/2/3` | UBINARY | Priority queue thresholds (days) |
| `MTWC_VOVHD` | FLOAT/4dec | Variable overhead rate |
| `MTWC_FOVHD` | FLOAT/4dec | Fixed overhead rate |
| `MTWC_LEAD` | UBINARY | Lead time days (used by Lead Time scheduling) |
| `MTWC_OUTPROC` | STRING 1 | Outside process flag (`Y` = subcontract WC) |
| `MTWC_PARENT_YN` | STRING 1 | `Y` = this WC is a parent of child WCs |
| `MTWC_PARENT_WC` | STRING 12 | Parent WC code (for hierarchical capacity) |
| `MTWC_LEVEL_YN` | STRING 1 | Level flag for dependent scheduling cascade |
| `MTWC_CYCLE_TIME_1..10` | UBINARY | 10-bucket cycle times (for finite scheduling buckets) |
| `MTWC_HRS_SHIFT` | UBINARY | Hours per shift |
| `MTWC_EST_VOVHD` | FLOAT/4dec | Estimated variable OH rate (for quoting) |
| `MTWC_EXTRA` | STRING 100 | Extra / user-defined |

**Live data (i2 Systems):** 27 work centers including SMT, QC Inspection, Conformal Coat,
Cable Assy, Apeiron (external/subcontract). Most have HRSWEEK=2080 (40h×52); utilization
and cost rates are set to 0 at i2 (rates managed outside EvoERP).

### BKSHORT — Shortage List (9 fields)

Tracks parts that are short (insufficient inventory) for scheduled WOs.

| Field | Type | Size | Meaning |
|-------|------|------|---------|
| `BK_SHORT_PCODE` | STRING | 15 | Part code (shortage item) |
| `BK_SHORT_DESC` | STRING | 25 | Part description |
| `BK_SHORT_WONUM` | FLOAT | 8 | Work Order number |
| `BK_SHORT_WO_SUF` | UBINARY | 2 | WO suffix |
| `BK_SHORT_QTYREQ` | FLOAT/2dec | 8 | Quantity required by the WO |
| `BK_SHORT_SHORT` | FLOAT/2dec | 8 | Shortage quantity (QTYREQ − available) |
| `BK_SHORT_DATE` | DATE | 4 | Date shortage identified |
| `BK_SHORT_PPCODE` | STRING | 15 | Parent part code (assembly the short part feeds into) |
| `BK_SHORT_PPDESC` | STRING | 25 | Parent part description |

**Live data:** 0 records — no current shortages at i2 Systems.

---

## Scheduling workflow

```
WO released (WO-B Release)
  → WORKORD.SSTART / SFIN populated from release date
  → WOROUT routing operations assigned to work centers

SH-F Finite / Infinite Scheduling
  → Filter: Status [FR], WO ranges, Planner Code
  → "Process" runs forward scheduling algorithm
  → Updates WOROUT.START / FINISH per-operation
  → Updates WORKORD.SSTART / SFIN / DDATE

SH-E Due Date Change
  → User enters new Due Date
  → Priority recalculated from due-date proximity

SH-A Manual Date Edit
  → Grid shows all WOs with Sched Start/Finish/Due Date
  → User types directly into grid

SH-N Generate Lead Times (batch)
  → Item# + Class filter → iterate WORKCTR
  → Updates MTWC_LEAD from routing standard times

SH-K View WC Load (Java)
  → WorkCenterLoad.jar reads WOROUT + WORKCTR
  → Graphical load chart per work center
```

---

## Related modules

| Module | Relationship |
|--------|-------------|
| `WO` | Owns WORKORD + WOROUT; SH reads and updates scheduling date fields |
| `RO` | Defines WORKCTR (routing master) and ROUTING (standard routing templates) |
| `DC` | Records actual start/finish times on WOROUT operations |
| `SL` | Shop Loading module — T7SHA/SHC/SHP read the same WORKORD/WORKCTR/WOROUT tables |
| `MR` | MRP creates WO release suggestions based on due dates; SH provides the dates MR needs |
