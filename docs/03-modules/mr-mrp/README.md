# MRP (Material Requirements Planning) (MR)

Status: verified (auto-generated from the extracted schema, menu-code dump, and DFM inventory).

- **Module code**: `MR`
- **Tables**: 4 (prefixes `BKMR`, `MTMR`)
- **UI forms**: 18 (prefixes `T7MR`, `T6MR`, `BKMR`)
- **Menu operations**: 12

## Narrative / vendor help

**→ [help-content.md](help-content.md)** — consolidated write-up of
all 14 help topics from `EvoHELP.CHM` (overview + MR-A through MR-N,
13 programs). Hoists the Buffer / Sensitivity / Action-message model
into a shared "Core concepts" section, then walks through forecasts
(MR-A/B/C), parameters (MR-D/E), the MR-F generation engine, the MR-G
/ MR-H / MR-L reporting trio, and the MR-I / MR-J / MR-K / MR-N
conversion programs. Includes MR-J's lead-time-batching worked
example. Cross-linked to WO, PO, SO, IN, BM, SH modules.

## Menu operations

| Code | Operation | Legacy module file(s) |
| ---- | --------- | --------------------- |
| `MR-A` | Enter Forecast | BKMRA;BKMRADE |
| `MR-B` | Print Forecast | BKMRB |
| `MR-C` | Reset Forecast | BKMRC |
| `MR-D` | Enter MRP Parameters | BKMRD |
| `MR-E` | Print MRP Parameters | BKMRE |
| `MR-F` | Generate Material Requirements | AUTOMRF;BKMRF |
| `MR-G` | Print Material Requirements | BKMRG |
| `MR-H` | Print Order Action Report | BKMRH |
| `MR-I` | Generate Work Orders | BKMRI |
| `MR-J` | Generate Purchase Orders | BKMRJ;BKMRK |
| `MR-K` | Generate RFQ's | BKMRJ;BKMRK |
| `MR-L` | Print Planned Orders Report | BKMRL |

## UI forms (18)

| DFM file | Caption | fields | controls | tabs |
| -------- | ------- | -----: | -------: | ---: |
| `T7MRA.DFM` |  | 0 | 1 | 0 |
| `T7MRADE.DFM` | New Screen | 9 | 33 | 0 |
| `T7MRB.DFM` | MR-B | 13 | 42 | 0 |
| `T7MRC.DFM` | New Screen | 16 | 45 | 0 |
| `T7MRD.DFM` | New Screen | 52 | 134 | 0 |
| `T7MRE.DFM` | New Screen | 10 | 35 | 0 |
| `T7MRF.DFM` | MR-F | 41 | 91 | 0 |
| `T7MRG.DFM` | MR-G | 25 | 61 | 0 |
| `T7MRH.DFM` | MR-H | 32 | 91 | 0 |
| `T7MRI.DFM` | MR-I | 24 | 58 | 0 |
| `T7MRIR.DFM` | Review QTY'#39's | 5 | 13 | 0 |
| `T7MRIX.DFM` | New Screen | 18 | 52 | 0 |
| `T7MRJ.DFM` | MR-J | 29 | 77 | 0 |
| `T7MRJR.DFM` | MR-J Review | 10 | 24 | 0 |
| `T7MRJX.DFM` |  | 0 | 1 | 0 |
| `T7MRL.DFM` | MR-L | 3 | 22 | 0 |
| `T7MRN.DFM` | MR-N | 5 | 23 | 0 |
| `T7MRO.DFM` | MR-O | 1 | 17 | 0 |

## Database tables (4)

Full field details are in `../../../samples/ddf/schema.md` (see per-table heading).

| Table | File on disk | Fields | Key fields (first 3) |
| ----- | ------------ | -----: | -------------------- |
| **BKMRPFC** | `BKMRPFC.B` | 9 | `BKMRP_FC_PART`, `BKMRP_FC_DATE`, `BKMRP_FC_QTY` |
| **BKMRPPO** | `BKMRPPO.B` | 16 | `BKMRP_PO_UID`, `BKMRP_PO_VEND`, `BKMRP_PO_DATE` |
| **BKMRPSW** | `BKMRPSW.B` | 2 | `BKMRP_SW_PART`, `BKMRP_SW_SW` |
| **MTMRP** | `MTMRP.B` | 13 | `MTMRP_PARTNO`, `MTMRP_DATE`, `MTMRP_QTY` |

## Table documentation (confirmed from DDF schema.md, Pass 110h 2026-06-19)

### BKMRPFC — Forecast (9 fields)

Primary key: `BKMRP_FC_PART` (STRING 15) + `BKMRP_FC_DATE` (DATE)

| Field | Type | Meaning |
|-------|------|---------|
| `BKMRP_FC_PART` | STRING 15 | Part number (PK 1) |
| `BKMRP_FC_DATE` | DATE | Forecast period start date (PK 2) |
| `BKMRP_FC_QTY` | FLOAT | Forecasted demand quantity |
| `BKMRP_FC_EXTRA` | STRING 25 | Extra / notes |
| `BKMRP_FC_OQTY` | FLOAT | Original forecast quantity (before any edits) |
| `BKMRP_FC_CQTY` | FLOAT | Consumed quantity (actual demand that has consumed the forecast) |
| `BKMRP_FC_FLAG` | STRING 1 | Status flag |
| `BKMRP_FC_DATE1` | DATE | Alternate date |
| `BKMRP_FC_NUM` | FLOAT | Sequence number |

Populated by MR-A (Enter Forecast). Consumed by MR-F (Generate MRP) — forecast demand reduces OQTY as actual sales orders are booked against it.

---

### BKMRPPO — MRP Planned Purchase Orders (16 fields)

Primary key: `BKMRP_PO_UID` (STRING 20)

| Field | Type | Meaning |
|-------|------|---------|
| `BKMRP_PO_UID` | STRING 20 | Unique planned PO ID (PK) |
| `BKMRP_PO_VEND` | STRING 10 | Suggested vendor (from MTICMSTR preferred vendor list) |
| `BKMRP_PO_DATE` | DATE | Suggested order date |
| `BKMRP_PO_ERD` | DATE | Expected receipt date (order date + lead time) |
| `BKMRP_PO_PART` | STRING 15 | Part number |
| `BKMRP_PO_QTY` | FLOAT | Suggested order quantity |
| `BKMRP_PO_PRICE` | FLOAT | Suggested price (from vendor price file) |
| `BKMRP_PO_WOPRE` | FLOAT | Work order prefix (pegged-to WO demand) |
| `BKMRP_PO_WOSUF` | UBINARY | Work order suffix |
| `BKMRP_PO_PLANR` | STRING 4 | Planner/buyer code |
| `BKMRP_PO_CONF` | STRING 1 | Confirmed flag (Y = user confirmed, proceed to create real PO) |
| `BKMRP_PO_DONE` | STRING 10 | Done/released marker |
| `BKMRP_PO_MTREC` | UBINARY 4 | Master record reference |
| `BKMRP_PO_EXTRA` | STRING 50 | Extra |
| `BKMRP_PO_EST` | STRING 10 | Estimate reference |
| `BKMRP_PO_ESTLNE` | FLOAT | Estimate line number |

Populated by MR-F. Released to actual POs via MR-J (Generate Purchase Orders) when CONF = Y.

---

### BKMRPSW — MRP Item Switch (2 fields)

Primary key: `BKMRP_SW_PART` (STRING 15)

| Field | Type | Meaning |
|-------|------|---------|
| `BKMRP_SW_PART` | STRING 15 | Part number (PK) |
| `BKMRP_SW_SW` | STRING 1 | MRP switch: Y = include this part in MRP run, N = exclude |

One row per part. Overrides the `MTIC_PROD_MRPSW` flag on the item master for the current MRP run. Allows temporary exclusion of items without changing the item master.

---

### MTMRP — MRP Explosion Work Table (13 fields)

Primary key: `MTMRP_PARTNO` (STRING 15) + `MTMRP_DATE` (DATE)

| Field | Type | Meaning |
|-------|------|---------|
| `MTMRP_PARTNO` | STRING 15 | Part number |
| `MTMRP_DATE` | DATE | Need date (when the demand is required) |
| `MTMRP_QTY` | FLOAT | Net requirement quantity |
| `MTMRP_ONHAND` | FLOAT | Projected on-hand at need date |
| `MTMRP_PEGTO` | STRING 10 | Pegged-to demand source (SO#, WO#, forecast) |
| `MTMRP_ORDER` | STRING 10 | Supply order number (planned WO or planned PO) |
| `MTMRP_STARTDT` | DATE | Planned order start date (need date minus lead time) |
| `MTMRP_ACTION` | STRING 10 | Action message: NEW, CANCEL, EXPEDITE, DEFER, etc. |
| `MTMRP_PG_SDATE` | DATE | Peg start date |
| `MTMRP_PG_FDATE` | DATE | Peg finish date |
| `MTMRP_PG_QTY` | FLOAT | Pegged quantity |
| `MTMRP_EXTRA` | STRING 50 | Extra |
| `MTMRP_LOC` | STRING 10 | Warehouse location |

Populated by MR-F (Generate Material Requirements). Cleared and rebuilt each MRP run. Drives MR-G (Print MRP), MR-H (Order Action Report), MR-L (Planned Orders Report). Row is consumed by MR-I (Generate Work Orders) and MR-J (Generate Purchase Orders).

---

## Additional runtime tables (confirmed from BKMRF.RUN binary, Pass 246 2026-06-24)

These strings appear in the BKMRF.RUN data channel, indicating the MRP engine opens or
reads these tables during a run. They are supplementary to the 4 permanent BKMRP* tables.

| String in binary | Role / interpretation | Confidence |
|------------------|-----------------------|-----------|
| `BKBMMSTR` | BM (Bills of Material) master — BOM explosion input | confirmed table |
| `CALENDAR` | Shop calendar — working days for lead time calc | confirmed table |
| `BKAPPO` / `BKAPPOL` | AP purchase order header + line — existing PO supply | confirmed tables |
| `WOBOM` | WO BOM (material requirements on open WOs) | confirmed table |
| `WORKORD` | Work order header — open WO demand input | confirmed table |
| `BKICLOC` / `BKICLOCM` | IC warehouse location — on-hand quantity per location | confirmed tables |
| `BKICMSTR` / `MTICMSTR` | IC item master (single/multi-class) | confirmed tables |
| `BKARINVL` / `BKARINV` | AR invoice line + header — sales order linkage | confirmed tables |
| `WOROUT` | WO routing — routing steps on open WOs | confirmed table |
| `SUMPNCUS` | 6-field summary stats table (DDF confirmed); used in BOM Analysis pass | confirmed table |
| `REORDLVL` | Reorder level — Stage 3 input; likely a field string or MTICMSTR field | inferred |
| `EXPSENS` | Expedite sensitivity threshold — Stage 4 action messages | inferred (field/constant) |
| `NLT` | Net lead time accumulator — BOM Analysis pass | inferred (field/variable) |
| `RFAM` / `RFAMB` | 4/5-char identifiers in Stage 2 / BOM Analysis section | role unclear |
| `FAMNB` | Family "NB" code — appears near BOM Analysis strings | role unclear |

**Stage source order strings confirmed in binary:** "Sales Orders", "Purchase Orders",
"Work Orders", "WO BOMs", "S-Type WO BOMs", "Forecasts".

**Stage progress strings confirmed in binary:** "Stage 1:", "Stage 2:", "Stage 3:",
"Stage 4:", "BOM Analysis:".

**File init messages confirmed in binary:**
- `Initializing MRP output file...`
- `Initializing BOM Analysis file...`
- `Initializing BKMRPSW file...`

---

## MRP data flow summary

```
BKMRPFC (forecasts) ──┐
WORKORD (WO demand)  ──┤
BKSOX   (SO demand)  ──┤──► MR-F generates ──► MTMRP (planned orders)
BKAPPOL (PO supply)  ──┤
BKICLOC (on-hand)    ──┘
                                                  │
                                    ┌─────────────┴──────────────┐
                                    ▼                             ▼
                               MR-I → WORKORD           MR-J → BKMRPPO
                                (planned WOs)           (planned POs)
```

## Programs (17 total, Pass 265 2026-06-25)

Data extracted from rwn_symbols.json.

| Program | Procs | Lib | DBs | Role / key tables |
|---------|------:|-----|----:|-------------------|
| `T7MRJ.RWN` | 206 | LISTG60 | 39 | **MR-J Generate Purchase Orders** — BKMRPPO → BKAPPO; IS.NCR 58-var + BKAP.PO 57-var |
| `T7MRH.RWN` | 193 | DBA.LIB | 29 | **MR-H Print Order Action Report** — BKICMSTR + ISBUILD; BKAR.INV 86-var + MTWO.WIP 71-var |
| `T7MRG.RWN` | 188 | DBA.LIB | 34 | **MR-G Print Material Requirements** — MTMRP + BKICMSTR; BKAR.INV 86-var + MTWO.WIP 71-var |
| `T7MRF.RWN` | 172 | LISTG60 | 35 | **MR-F Generate Material Requirements** — reads BKMRPFC + BKARINVL → writes MTMRP; BKAR.INV 86-var |
| `T7MRI.RWN` | 171 | LISTG60 | 31 | **MR-I Generate Work Orders** — MTMRP → WORKORD; MTWO.WIP 71-var |
| `T7MRIX.RWN` | 130 | LISTG60 | 40 | **MR-I-X WO expansion drill-down** — WORKORD + ISICMSTR; MTWO.WIP **213-var** (highest WIP namespace in system) |
| `T7MRJX.RWN` | 123 | LISTG60 | 40 | **MR-J-X PO expansion drill-down** — BKMRPPO + BKAPPO; BKAP.PO 57-var |
| `T7MRD.RWN` | 121 | LISTG60 | 21 | **MR-D Enter MRP Parameters** — 52-field form; BKICMSTR + MTICMSTR |
| `T7MRE.RWN` | 120 | LISTG60 | 40 | **MR-E Print MRP Parameters** — BKICLOCM + BKICMSTR |
| `T7MRB.RWN` | 117 | LISTG60 | 40 | **MR-B Print Forecast** — BKMRPFC + BKICMSTR |
| `T7MRO.RWN` | 113 | LISTG60 | 40 | **MR-O planned orders browser** — ISBUILD + MTMRP |
| `T7MRC.RWN` | 108 | LISTG60 | 40 | **MR-C Reset Forecast** — BKMRPFC + MTICMSTR |
| `T7MRN.RWN` | 95 | LISTG60 | 40 | **MR-N Print Planned Orders Report** — ISBUILD + MTMRP |
| `T7MRL.RWN` | 85 | EVO.LIB | 40 | **MR-L Print Planned Orders** — MTMRP |
| `T7MRADE.RWN` | 75 | EVO.LIB | 40 | **MR-A-D-E demand forecast editor** — BKMRPFC + BKICMSTR |
| `T7MRA.RWN` | 65 | LISTG60 | 40 | **MR-A Enter Forecast** — BKMRPFC + BKICMSTR |
| `T7MRK.RWN` | 5 | stub | 40 | Stub — RFQ generation (no business logic) |

**T7MRIX** has MTWO.WIP **213-var** — the highest WIP namespace count in the entire rwn_symbols dataset. This is the MRP→WO expansion view that drills into every open work order's detailed material and capacity consumption. When MR-I generates WOs, T7MRIX shows the exploded view of what those WOs will consume.

**T7MRF** is the MRP generation engine (the only program that writes MTMRP). It reads 6 demand/supply sources → writes MTMRP planned orders. The **4-stage engine** is fully SRC-confirmed (Pass 283): Stage 1 = make-item planning, Stage 2 = multi-pass BOM explosion, Stage 3 = buy-item planning, Stage 4 = action code assignment (EXPEDITE/DELAY/REVIEW). See "MRP Engine Architecture" section below.

**T7MRH and T7MRG** (the two main report programs) both use DBA.LIB rather than the usual LISTG60.LIB — this suggests they do complex processing (posting or multi-pass calculations) rather than simple browse/display.

---

---

## MRP Engine Architecture — BKMRF.SRC fully decoded (Pass 283, 2026-06-25)

All the following is **SRC-confirmed** from `samples/src/BKMRF.SRC`.

### Demand loading (pre-stage)

MR-F first clears MTMRP and rebuilds from all 6 demand/supply sources:

| Section | Source table | Field used | Notes |
|---------|-------------|-----------|-------|
| `DO.SO` | `BKARINVL` | ESD (estimated ship date) | QTY = PQTY + UBO (ordered + backordered) × -1; skips UM.LN[1]='M' (BOM explosion handles those); skips closed SO (INVCD='Y') |
| `DO.PO` | `BKAPPOL` | ERD (estimated receipt date) | QTY = PQTY × PCONV (or QC.QTY × PCONV if in QC); EXTRA="PURCHASE ORDER"; ORDER = PO#; QC orders tagged "/QC" suffix; STARTDT = BKAP.PO.ORDDTE |
| `DO.WO` | `WORKORD` | WO due date | QTY = SQTY - COMQTY; skips STATUS $ "CXI" (closed/cancelled/issued-complete) |
| `DO.WOBOM` | `WOBOM` | WO BOM required dates | BOM component demand from open WOs |
| `DO.WSBOM` | `WORKORD` | S-type WO BOMs | S-type work order BOM explosion |
| `DO.FC` | `BKMRPFC` | FC_DATE | Forecast demand (if INC.FORECAST='Y') |
| `DO.RLEVEL` | `BKICLOC` | — | Reorder level check — seeds stage 1 |

All demand records: MTMRP.QTY is **negative** (demand) or **positive** (supply).

### 4-Stage MRP engine

```
Stage 1: Make items (FAMNB types) ─► CREATE.PLN() ─► MTMRP planned orders
           └─► BOM explosion (GET.BOM) seeds MTMRP component demand
           └─► BKMRPSW records created for each part

Stage 2: Multi-pass BOM explosion (FAMNB types)
           Scans BKMRPSW, runs CHK.PLAND / CREATE.PLN for each
           Loops until ctl.recs = 0 (no new planned orders)

Stage 3: Buy items (R, L, T types) ─► CREATE.PLNB() ─► MTMRP "BUY" orders

Stage 4: Action code assignment (all types, 3 passes)
           Pass 1: EXPEDITE / EXPSENS — supply arriving too late
           Pass 2: Update PG.FDATE with GET.RQ.DATE()
           Pass 3: DELAY / DELSENS / REVIEW — supply arriving too early
```

**Stage 1/2 item type filter:** `inc.types2 = 'FAMNB' + opt.types` where opt.types (default 'NLT') is user-configurable from the MR-F run parameters (INC.FORECAST, STYPE, OPT.TYPES).

**Stage 3 filter:** `MTIC.PROD.TYPE $ 'RLT'` — raw/purchased/outside-process items.

### Planned order numbering

| Order type | ORDER field format | Counter |
|-----------|-------------------|---------|
| Make (F/A/N) planned | `PL1`, `PL2`, … | `plnum` |
| Phantom (B) planned | `PLP1`, `PLP2`, … | `plpnum` |
| Buy (R/L/T) planned | `BUY` | `buynum` counter displayed |
| Reorder level trigger | `REORDLVL` | — |

After Stage 4, PLP records are renumbered via `RENUM.PHN` subroutine.

Initial `MTMRP.ACTION` on newly created planned orders:
- M-type items → `'BUY'` (make-from items purchase raw material)
- All other make types (F/A/N/B) → `'MAKE'`
- R/L/T types (CREATE.PLNB) → `'BUY'`

### Action code assignment (Stage 4)

Stage 4 scans **all** BKMRPSW entries (all item types).

**EXPEDITE / EXPSENS logic (MRK.EXPDTE):**
```
lookahead = order.DATE + MTIC.PROD.EXPBF     ; days forward to scan
scan MTMRP reverse while PARTNO matches
  if supply found with QTY > 0 within lookahead:
    if order.DATE - demand.DATE > int(BKIC.PROD.AVFO):
      ACTION = "EXPEDITE"          ; supply is late by more than threshold
    else:
      ACTION = "EXPSENS"           ; supply is late but within sensitivity range
```

**DELAY / DELSENS / REVIEW logic (MRK.DELAY):**
```
lookahead = order.DATE + MTIC.PROD.DELBF     ; days forward to scan
scan MTMRP reverse while PARTNO matches
  if demand found with QTY < 0 within lookahead:
    if demand.DATE - order.DATE > int(BKIC.PROD.AVVO):
      ACTION = "DELAY"             ; supply arrives too early by more than threshold
    else:
      ACTION = "DELSENS"           ; supply is early but within sensitivity range
  if no demand found in window:
    ACTION = "REVIEW"              ; supply with no demand — review needed
```

### Key item master fields used by MRP (SRC-confirmed)

| Field | Type | MRP role |
|-------|------|---------|
| `MTIC.PROD.MRP` | STRING 1 | 'Y' = include in MRP run (the real MRP on/off flag) |
| `MTIC.PROD.MRPSW` | STRING 1 | Quantity rounding flag: 'N'=no rounding, else round planned QTY to whole number |
| `MTIC.PROD.TYPE` | STRING 1 | Item type — governs which stage processes the part |
| `MTIC.PROD.LEAD` | UBINARY | Lead time (days) — STARTDT = required_date − LEAD |
| `MTIC.PROD.EXPBF` | UBINARY | Expedite buffer (days) — lookahead window for EXPEDITE scan |
| `MTIC.PROD.DELBF` | UBINARY | Delay buffer (days) — lookahead window for DELAY scan |
| `MTIC.PROD.PCONV` | FLOAT | Purchase UOM conversion factor (applied to PO quantities) |
| `BKIC.PROD.RLVL` | FLOAT | Reorder level — planned order triggered when ONHAND < RLVL |
| `BKIC.PROD.RAMT` | FLOAT | Reorder amount — minimum planned order quantity (non-phantoms) |
| `BKIC.PROD.UOH` | FLOAT | Units on hand — initial ONHAND seed for MRP balance calc |
| `BKIC.PROD.AVFO` | FLOAT | **EXPEDITE threshold (days)** — if late_days > AVFO → EXPEDITE (previously mislabelled "avg fixed overhead") |
| `BKIC.PROD.AVVO` | FLOAT | **DELAY sensitivity (days)** — if early_days > AVVO → DELAY (previously mislabelled "avg variable overhead") |

### BKMRPSW role (corrected)

BKMRPSW is a **stage-control scratch file**, not a per-part MRP enable/disable switch:
- Initialized in Stage 1: `BKMRP.SW.SW = 'Z'` for each part that gets MTMRP records
- During Stage 2: SW is updated to `MTIC.PROD.TYPE` when a planned order is created
- Stage 4 scans BKMRPSW (scope A = all records) to process every part that appeared in the run
- Cleared at the start of each MRP run via `casinit`

### MTMRP.ACTION codes (SRC-confirmed)

| Code | Meaning | Set by |
|------|---------|--------|
| `MAKE` | Planned order to manufacture | CREATE.PLN — F/A/N/B types |
| `BUY` | Planned order to purchase | CREATE.PLN (M-type) + CREATE.PLNB |
| `EXPEDITE` | Existing supply arriving late (> AVFO days) | Stage 4 MRK.EXPDTE |
| `EXPSENS` | Existing supply arriving late (≤ AVFO days) | Stage 4 MRK.EXPDTE |
| `DELAY` | Existing supply arriving too early (> AVVO days) | Stage 4 MRK.DELAY |
| `DELSENS` | Existing supply arriving too early (≤ AVVO days) | Stage 4 MRK.DELAY |
| `REVIEW` | Supply with no demand within delay buffer | Stage 4 MRK.DELAY |
| `REORDLVL` | Order triggered by reorder level rule | Stage 1/3 — seeded by DO.RLEVEL |

### CALENDAR table usage (SRC-confirmed)

`CREATE.PLN` and `CREATE.PLNB` both use `CALENDAR` (the shop calendar) to adjust the planned STARTDT:
```
STARTDT = DATE - LEAD
; if any day in [STARTDT..DATE] is a non-working day (ifdup MTCAL.DATE):
;   shift STARTDT back one day and recheck
```
The `ifdup MTCAL.DATE` check detects calendar blocking days. Working days = days NOT in the CALENDAR table.

---

## Live Data Analysis (Pass 420, 2026-06-30)

Queried via DSN=DBA ODBC against the live i2 Systems database.

### MTMRP — MRP output table

| Action Code | Count | Meaning |
|-------------|------:|---------|
| *(blank)* | 31,437 | Pending — demand loaded, not yet actioned |
| BUY | 2,559 | Planned purchase order (outside buy) |
| REVIEW | 2,311 | Action required — user review needed |
| MAKE | 772 | Planned work order (make in-house) |
| DELSENS | 45 | Delay-sensitive — supply behind demand |
| EXPSENS | 13 | Expedite-sensitive — demand urgent |
| **Total** | **37,137** | |

Key observations:
- 85% of MTMRP records are blank-action (demand loaded, awaiting MRP run processing)
- BUY >> MAKE (2,559 vs 772): i2 Systems buys far more than it makes in the current MRP snapshot
- 2,311 REVIEW items = significant manual MRP workload outstanding
- Date range: 2001-01-01 to 2044-05-12 (MTMRP accumulates demand history and future planning horizon)

### Supporting tables

| Table | Records | Notes |
|-------|--------:|-------|
| MTMRP | 37,137 | Full MRP output — action codes confirmed |
| BKMRPFC | 0 | No forecasts loaded in MRP at this time |
| BKMRPPO | 0 | No planned POs outstanding (all released or cleared) |

**Interpretation:** BKMRPFC=0 confirms i2 Systems runs MRP in pure-demand mode (actual SO/WO demand only, no forecasting). BKMRPPO=0 means all planned POs from last MRP run have been confirmed/released to BKAPPO/BKAPPOL.

---

## Notes & open questions (updated Pass 283)

- BKMRPPO CONF field: once confirmed by user in MR-J, creates a real BKAPPO/BKAPPOL record. The BKMRPPO row is likely then deleted or marked DONE (not confirmed in SRC).
- `BKAP.PO.PRTD $ "CR"` in DO.PO — C and R are excluded PO statuses. C likely = Cancelled, R likely = Received. Awaiting UI label confirmation.
- `BKAP.PO.CONFIRM[2]='S'` — PO status flag at position 2 = 'S' is skipped. Meaning of 'S' not confirmed.
- `MTWO.WIP.STATUS $ "CXI"` — WO statuses C/X/I excluded from MRP demand. Likely Complete/Cancelled/Issued-complete. SRC-level confirmed as exclusion filter; label confirmation pending.
