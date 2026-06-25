# Routings (RO)

Status: verified | Pass 265 (2026-06-25)

- **Module code**: `RO`
- **Tables**: 9 core (ROUTING, WORKCTR, MACHINE, TOOL, DPTMENT, WOROUT, BKRTCST, BKRTTEMP, BKMATRIM) + QCCODES, SCRAP
- **Programs**: 21 (T7ROA–T7ROQ + T7ROJ-series)
- **UI forms**: 19 (T7RO*.DFM)
- **Menu operations**: 19

→ See **[help-content.md](help-content.md)** for user-facing routing setup procedures (22 CHM topics: RO-A through RO-N).

Routings define the manufacturing sequence (operations) for each finished good or subassembly.
Routing operations are copied to Work Order routing records when a WO is released (firmed).
The routing drives the shop traveler, scheduling, capacity planning, and standard cost rollup.

---

## Menu operations

| Code | Operation | Program | Tables |
|------|-----------|---------|--------|
| `RO-A` | Enter Routings | T7ROA | ROUTING + BKRTCST + MTICMSTR |
| `RO-B` | Print/Rollup Routing Costs | T7ROB | BKSYMSTR + MTICMSTR |
| `RO-C` | Enter Work Centers | T7ROC | WORKCTR + DPTMENT + ROUTING |
| `RO-D` | Enter Machines | T7ROD | MACHINE + BKMATRIM + WORKCTR |
| `RO-E` | Enter Tools | T7ROE | TOOL + MACHINE |
| `RO-F` | Enter QC Codes | T7ROF | QCCODES |
| `RO-G` | Enter Scrap Codes | T7ROG | SCRAP + BKGLCOA |
| `RO-H` | Enter Departments | T7ROH | DPTMENT |
| `RO-I` | Enter Operation Templates | T7ROI | ROUTING + WORKCTR + BKAPVEND |
| `RO-J-A` | Print Routings | T7ROJA | WORKORD + WOROUT |
| `RO-J-B` | Print Work Centers | T7ROJB | WORKCTR |
| `RO-J-C` | Print Machines | T7ROJC | MACHINE |
| `RO-J-D` | Print Tools | T7ROJD | TOOL |
| `RO-J-E` | Print QC Codes | T7ROJE | QCCODES |
| `RO-J-F` | Print Scrap Codes | T7ROJF | SCRAP |
| `RO-J-G` | Print Departments | T7ROJG | DPTMENT |
| `RO-J-H` | Print Operation Templates | T7ROJH | WORKCTR + ROUTING |
| `RO-K` | Enter Specification Templates | T7ROK | BKRTTEMP |
| `RO-L` | Enter Sequence Print Control | T7ROL | ROUTING |
| `RO-P` | Update Processing Cost Standard | T7ROP | ROUTING + BKAPPOL + BKAPPO |
| `RO-Q` | Routing inquiry | T7ROQ | WORKCTR + ROUTING + WOROUT |

---

## Programs (21 total, Pass 265 2026-06-25)

Data extracted from rwn_symbols.json.

| Program | Procs | Lib | DBs | Role / key tables |
|---------|------:|-----|----:|-------------------|
| `T7ROA.RWN` | 226 | LISTG60 | 30 | **RO-A Enter Routings** — main routing editor; ROUTING + BKRTCST + MTICMSTR; IS.EST 58-var (estimating integration) |
| `T7ROC.RWN` | 139 | LISTG60 | 26 | **RO-C Enter Work Centers** — WORKCTR + DPTMENT + ROUTING |
| `T7ROB.RWN` | 123 | LISTG60 | 20 | **RO-B Print/Rollup Routing Costs** — BKSYMSTR + MTICMSTR |
| `T7ROJA.RWN` | 106 | LISTG60 | 40 | **RO-J-A Print Routings** — WORKORD + WOROUT; BKPR.EMP 103-var + MTWO.WIP 71-var |
| `T7ROJD.RWN` | 102 | LISTG60 | 40 | **RO-J-D Print Tools** — TOOL + BKARCUST |
| `T7ROI.RWN` | 98 | LISTG60 | 40 | **RO-I Enter Operation Templates** — ROUTING + WORKCTR + BKAPVEND |
| `T7ROE.RWN` | 97 | LISTG60 | 40 | **RO-E Enter Tools** — TOOL + MACHINE |
| `T7ROJH.RWN` | 90 | LISTG60 | 40 | **RO-J-H Print Operation Templates** — WORKCTR + ROUTING |
| `T7ROJB.RWN` | 89 | LISTG60 | 40 | **RO-J-B Print Work Centers** — WORKCTR |
| `T7ROJC.RWN` | 89 | LISTG60 | 40 | **RO-J-C Print Machines** — MACHINE |
| `T7ROJE.RWN` | 86 | LISTG60 | 40 | **RO-J-E Print QC Codes** — QCCODES |
| `T7ROJF.RWN` | 85 | LISTG60 | 40 | **RO-J-F Print Scrap Codes** — SCRAP |
| `T7ROP.RWN` | 82 | LISTG60 | 40 | **RO-P Update Processing Cost Standard** — ROUTING + BKAPPOL + BKAPPO (outside process PO link); BKAP.PO 57-var + BKAP.POL 38-var |
| `T7ROJG.RWN` | 80 | EVO.LIB | 40 | **RO-J-G Print Departments** — DPTMENT |
| `T7ROQ.RWN` | 77 | LISTG60 | 40 | **RO-Q Routing inquiry** — WORKCTR + ROUTING + WOROUT |
| `T7ROK.RWN` | 68 | LISTG60 | 40 | **RO-K Enter Specification Templates** — BKRTTEMP |
| `T7ROD.RWN` | 65 | LISTG60 | 40 | **RO-D Enter Machines** — MACHINE + BKMATRIM + WORKCTR |
| `T7ROG.RWN` | 64 | LISTG60 | 40 | **RO-G Enter Scrap Codes** — SCRAP + BKGLCOA |
| `T7ROL.RWN` | 56 | LISTG60 | 40 | **RO-L Enter Sequence Print Control** — ROUTING |
| `T7ROF.RWN` | 54 | EVO.LIB | 40 | **RO-F Enter QC Codes** — QCCODES |
| `T7ROH.RWN` | 54 | EVO.LIB | 40 | **RO-H Enter Departments** — DPTMENT |

**Note on T7ROJA:** Opens WORKORD + WOROUT alongside ROUTING — it's not just a routing print but also accesses **open work orders** (WORKORD = WO header, WOROUT = WO routing output). BKPR.EMP 103-var namespace confirms this program also accesses employee/labor data, likely for capacity-load analysis across active WOs.

**Note on T7ROP:** Directly links routing outside-process operations to AP purchase orders (BKAPPOL + BKAPPO). This is the mechanism that converts type-P (outside processing) routing operations into actual PO line items.

---

## Database tables

### Core routing tables

| Table | Fields (est.) | Purpose |
|-------|:-------------:|---------|
| `ROUTING` | ~25 | Routing header + operation lines — PARENT (item) + OP (sequence); per-operation: type (L/P/A), work center, setup/run time, cost |
| `WORKCTR` | ~20 | Work center master — center code, department, labor/overhead rates, capacity (hrs/week, shifts) |
| `DPTMENT` | ~10 | Department master — code + name + GL accounts |
| `MACHINE` | ~15 | Machine master — machine code, associated work center, setup/run rates |
| `TOOL` | ~15 | Tooling master — tool code, description, associated work center, customer/mfg owner |
| `WOROUT` | ~15 | Work order routing output — per-WO copy of routing operations; updated as DC posts labor |
| `BKRTCST` | ~10 | Routing cost standard — stores rolled-up cost per routing/item |
| `BKRTTEMP` | ~15 | Routing/specification template — re-usable operation definitions |
| `BKMATRIM` | ~10 | Material trim definition — used in sheet/roll material cutting operations |
| `QCCODES` | ~8 | QC operation codes — quality check steps that appear in routing ops |
| `SCRAP` | ~8 | Scrap codes — scrap reason codes with GL account linkage (BKGLCOA) |

**Field counts are estimated** — these tables are not in the standard DDF (they use the ROUTING/WORKCTR Btrieve DDF set, not the BKIC/BKAR standard DDF). Exact schemas require DDF inspection.

### Confirmed from BKROA.SRC analysis (Pass 119 2026-06-19)

The BKROA.SRC (TAS Pro 6 routing source) opened the **ROUTING table** alongside ~20 other files.
Key ROUTING fields confirmed from source: PARENT (item code), OP (operation seq), WC (work center),
SEQTYPE (R/S/blank), OPTYPE (L/P/A), DESC (30 char), SETUP/RUN time, VENDOR (for type P).

---

## Key relationships

- `T7ROA` is the **only** program that writes ROUTING master data — all other programs read it
- `T7ROC` is the **only** program that writes WORKCTR — work center setup
- `T7ROP` bridges **type-P (outside process) routing ops → AP purchase orders** — when a routing operation is type P, T7ROP generates or updates BKAPPOL/BKAPPO records; these same POs appear in the WO-LA (T7WOLA) outside-process flow
- `T7ROJA` accesses both ROUTING and WORKORD/WOROUT — it prints routing-level data **including currently open WO load** (capacity analysis)
- `IS.EST 58-var` in T7ROA confirms **routing data feeds the ES (Estimating) module** — estimated routings use the same ROUTING table
- When a WO is released (firmed via WO-B), the routing lines from ROUTING are **copied** to WOROUT (WO routing output) — subsequent DC labor postings update WOROUT, not the ROUTING master

---

**Confidence: 82/100** — All 21 programs confirmed from rwn_symbols.json with proc counts, libs, and DB fingerprints; menu code mapping confirmed from help-content.md; core table names confirmed from program DB lists and BKROA.SRC analysis (Pass 119). Field-level table schemas for ROUTING/WORKCTR/MACHINE/TOOL/DPTMENT are estimated (not from DDF) — these tables use a separate DDF set not yet extracted.
