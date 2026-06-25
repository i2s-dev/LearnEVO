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

**T7MRF** is the MRP generation engine (the only program that writes MTMRP). It reads 6 sources: BKMRPFC (forecasts), BKARINVL (SO demand), BKAPPOL (PO supply), WOBOM (WO material demand), BKICLOC (on-hand), BKICMSTR (item parameters) → writes MTMRP planned orders. The 5-stage engine is confirmed from BKMRF.RUN binary analysis (Pass 246).

**T7MRH and T7MRG** (the two main report programs) both use DBA.LIB rather than the usual LISTG60.LIB — this suggests they do complex processing (posting or multi-pass calculations) rather than simple browse/display.

---

## Notes & open questions

- MRP "buffer" sensitivity: T7MRD (52-field MRP parameters form) contains sensitivity settings — the exact buffer/sensitivity field names need extraction to confirm how MTMRP action messages (EXPEDITE/DEFER thresholds) are calculated.
- BKMRPSW per-part override: relationship to `MTIC_PROD_MRPSW` flag in the item master — unclear whether SW=Y means "run MRP" (include) or SW=Y means "switch off" (exclude). Context suggests SW=Y = include.
- BKMRPPO CONF field: once confirmed, MR-J creates a real BKAPPO/BKAPPOL record. The BKMRPPO row may then be deleted or marked DONE.
