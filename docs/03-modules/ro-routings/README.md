# Routings (RO)

Status: verified | Pass 328 (2026-06-26)

- **Module code**: `RO`
- **Tables**: 9 core (ROUTING/BKROMA, WORKCTR, MACHINE/TMACH, TOOL/MTOOL, DPTMENT, WOROUT, BKRTCST, BKRTTEMP/BKRTSPEC, BKMATRIM) + QCCODES, SCRAP
- **Programs**: 21 T7 programs (T7ROA–T7ROQ + T7ROJ-series) + 19 TAS6 BKRO*.RUN programs
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
- `T7ROC` is the **only** program that writes WORKCTR — work center setup; parent/child WC hierarchy enforced in software (MTWC.PARENT.WC, MTWC.PARENT.YN)
- `T7ROP` bridges **type-P (outside process) routing ops → AP purchase orders** — when a routing operation is type P, T7ROP generates or updates BKAPPOL/BKAPPO records; these same POs appear in the WO-LA (T7WOLA) outside-process flow
- `T7ROJA` accesses both ROUTING and WORKORD/WOROUT — it prints routing-level data **including currently open WO load** (capacity analysis)
- `IS.EST 58-var` in T7ROA confirms **routing data feeds the ES (Estimating) module** — estimated routings use the same ROUTING table
- When a WO is released (firmed via WO-B), the routing lines from ROUTING are **copied** to WOROUT (WO routing output) — subsequent DC labor postings update WOROUT, not the ROUTING master
- `MTRO.PRINT` flag controls which sequences appear on the printed shop traveler — managed via RO-L (BKROL.RUN)
- Work center rates flow into routing ops at print/cost time: MTWC.SETUP → MTRO.SETUP, MTWC.LABOR → MTRO.LABOR (confirmed from BKROB costed routing print)
- `BKRTEMTRA` = routing template copy/transfer table (confirmed from BKROA allcap IDs — used during operation template sync)

---

## Pass 328 — TAS6 BKRO*.RUN binary analysis (2026-06-26)

Extracted string data from all 19 BKRO*.RUN files. These are the TAS Pro 6 generation of the RO module (pre-T7ROA/T7ROC etc), still shipping on the network share.

### TAS6 program inventory

| File | Size | Menu Code | Title |
|------|-----:|-----------|-------|
| `BKROA.RUN` | 281KB | RO-A | Enter Routings (+ DE-J-C Edit Imported Routings) |
| `BKROB.RUN` | 156KB | RO-B | Print Costed Routing |
| `BKROC.RUN` | 160KB | RO-C | Work Centers |
| `BKROD.RUN` | 46KB | RO-D | Enter Machines (+ Trim Sizes variant) |
| `BKROE.RUN` | 106KB | RO-E | Enter Tools |
| `BKROF.RUN` | 27KB | RO-F | Enter QC Codes |
| `BKROG.RUN` | 26KB | RO-G | Enter Scrap Codes |
| `BKROH.RUN` | 100KB | RO-H | Enter Departments |
| `BKROI.RUN` | 152KB | RO-I | Enter Operation Templates |
| `BKROJA.RUN` | 130KB | RO-J-A | Print Routings |
| `BKROJB.RUN` | 124KB | RO-J-B | Print Work Centers |
| `BKROJC.RUN` | 42KB | RO-J-C | Print Machines |
| `BKROJD.RUN` | 38KB | RO-J-D | Print Tools |
| `BKROJE.RUN` | 37KB | RO-J-E | Print QC Codes |
| `BKROJF.RUN` | 37KB | RO-J-F | Print Scrap Codes |
| `BKROJG.RUN` | 37KB | RO-J-G | Print Departments |
| `BKROJH.RUN` | 52KB | RO-J-H | Print Operation Templates |
| `BKROK.RUN` | 114KB | RO-K | Enter Specs Templates |
| `BKROL.RUN` | 38KB | RO-L | Sequence Print Control |

**BKROA.RUN** also dispatches to "DE-J-C Edit Imported Routings" — it handles the import path
for routings coming from the DE (Data Entry) module import.

### MTRO.* — ROUTING table field accessor map (40 fields, confirmed from binary)

The TAS6 accessor prefix `MTRO.` maps to the ROUTING/BKROMA Btrieve file.

| Accessor | Meaning |
|----------|---------|
| `MTRO.NUM` | Routing number |
| `MTRO.CODE` | Part/item code (routing parent item) |
| `MTRO.CLASS` | Item class |
| `MTRO.DESC` | Routing description |
| `MTRO.OPER` | Operation sequence number |
| `MTRO.OPERDESC` | Operation description |
| `MTRO.TYPE` | Operation type (L=Labor, P=Outside Process, A=Alternate) |
| `MTRO.WC` | Work center code |
| `MTRO.WCDESC` | Work center description (denormalized) |
| `MTRO.STD.TIME` | Standard time |
| `MTRO.DEF.TIME` | Default time |
| `MTRO.TIME.PERPR` | Time per part/process |
| `MTRO.TIMEPART` | Time per part (alt field) |
| `MTRO.MD.PROC.HR` | Minutes per process-hour |
| `MTRO.PROC.PERHR` | Processes per hour |
| `MTRO.PARTSHR` | Parts per hour |
| `MTRO.SETUP` | Setup cost |
| `MTRO.SETUPHRS` | Setup hours |
| `MTRO.LEAD` | Lead time |
| `MTRO.LOTSIZE` | Lot size |
| `MTRO.LONGTIME` | Long-cycle time |
| `MTRO.OVERLAP` | Overlap (forward, hours) |
| `MTRO.NEGOVLP` | Negative overlap (backward, parts); value 0.02 = concurrent flag |
| `MTRO.LABOR` | Labor cost |
| `MTRO.FOVHD` | Fixed overhead |
| `MTRO.VOVHD` | Variable overhead |
| `MTRO.MIN.CHG` | Minimum charge |
| `MTRO.NUM.PERSON` | Number of persons |
| `MTRO.NUM.PROCES` | Number of processes |
| `MTRO.MACHINE` | Machine code |
| `MTRO.TMACHINE` | Machine (template reference) |
| `MTRO.TMACHDESC` | Machine description (denormalized) |
| `MTRO.TOOL` | Tool code |
| `MTRO.TOOLDESC` | Tool description (denormalized) |
| `MTRO.VENDCODE` | Vendor code (outside processing vendor) |
| `MTRO.VENDNAME` | Vendor name (denormalized) |
| `MTRO.VENDCOST` | Vendor cost (outside process unit cost) |
| `MTRO.OP.TEMP.NO` | Operation template number (link to BKRTTEMP) |
| `MTRO.INSTR` | Instructions / notes |
| `MTRO.PRINT` | Print flag — controls traveler sequence print (managed by RO-L) |
| `MTRO.EXTRA` | Extra / user-defined |

**Operation type codes** (confirmed from BKROA string "L Labor / P Outside Process / A Alternate"):
- `L` = Labor — standard shop floor operation; billed at work center labor + overhead rates
- `P` = Outside Processing — vendor performs the operation; MTRO.VENDCODE/VENDCOST apply; T7ROP generates AP POs
- `A` = Alternate Operation — parallel path that can be selected at WO time

**Overlap note** (confirmed from BKROA): Negative Overlap of 0.02 is a special Scheduling flag meaning "run next operation concurrently."

### MTWC.* — WORKCTR table field accessor map (24 fields, confirmed from binary)

| Accessor | Meaning |
|----------|---------|
| `MTWC.WC` | Work center code (PK) |
| `MTWC.WCDESC` | Work center description |
| `MTWC.DEPT` | Department code |
| `MTWC.DEPTDESC` | Department description (denormalized) |
| `MTWC.SETUP` | Setup rate |
| `MTWC.LABOR` | Labor rate |
| `MTWC.FOVHD` | Fixed overhead rate |
| `MTWC.VOVHD` | Variable overhead rate |
| `MTWC.EST.VOVHD` | Estimated variable overhead |
| `MTWC.%UTIL` | Utilization % |
| `MTWC.HRS.SHIFT` | Hours per shift |
| `MTWC.HRSWEEK` | Hours per week |
| `MTWC.LEAD` | Lead time |
| `MTWC.AVGQTIME` | Average queue time |
| `MTWC.MACHINE` | Default machine code |
| `MTWC.OUTPROC` | Outside processing flag (Y/N) |
| `MTWC.PARENT.WC` | Parent work center (for WC hierarchy) |
| `MTWC.PARENT.YN` | Is this a parent WC? (Y/N) |
| `MTWC.LEVEL.YN` | Level-tracking Y/N |
| `MTWC.COST.LB` | Cost per lb (material cost basis) |
| `MTWC.MIN.CHG` | Minimum charge |
| `MTWC.QPR1` | Queue priority 1 |
| `MTWC.QPR2` | Queue priority 2 |
| `MTWC.QPR3` | Queue priority 3 |

**Work center hierarchy**: BKROC enforces parent/child WC relationships. A WC with MTWC.PARENT.YN=Y
can have child WCs pointing at it via MTWC.PARENT.WC. Deleting a parent WC is blocked if children exist.
When editing costs on a parent, the system offers to propagate to children ("Updating child Work Centers...").

### MTOOL.* — TOOL table field accessor map (confirmed from BKROE binary)

| Accessor | Meaning |
|----------|---------|
| `MTOOL.TOOL` | Tool code (PK) |
| `MTOOL.DESC` | Tool description |
| `MTOOL.PRTSMAINT` | Parts between maintenance |
| `MTOOL.NOPARTS` | Number of parts made to date |
| `MTOOL.DATE` | Last maintenance date |
| `MTOOL.NOTES` | Notes (up to note line 1+) |

### TMACH.* — MACHINE table field accessor map (confirmed from BKROD binary)

| Accessor | Meaning |
|----------|---------|
| `TMACH.MACHINE` | Machine code (PK) |
| `TMACH.HRSUSED` | Hours used to date |
| `TMACH.HRSMAINT` | Hours between maintenance |

BKROD prompt confirms additional fields: Machine No., Work Center, No. Hours between Service, No. Hours Used to Date.

### Additional tables confirmed from TAS6 binaries

| TAS6 handle | TAS7 table name | Purpose |
|-------------|-----------------|---------|
| `BKROMA` / `BKROMAA/I` | ROUTING | Routing header + operation lines |
| `BKRTSPEC` / `BKRTSPECA/I` | BKRTCST (part) | Routing specifications (notes/specs per routing) |
| `BKRTTEMP` / `BKRTTEMPA/I` | BKRTTEMP | Operation templates (re-usable ops) |
| `BKRTEMTRA` | (internal) | Template transfer/copy temp table (used during Sync with routing templates) |
| `WORKCTRA` / `WORKCTR` | WORKCTR | Work center master |
| `MACHINEA` / `MACHINEI` | MACHINE | Machine master |
| `TOOLA` / `TOOLF` | TOOL | Tool master |
| `QCCODESA` / `QCCODES` | QCCODES | QC operation codes |
| `SCRAPA` / `SCRAP` | SCRAP | Scrap reason codes |
| `DPTMENTA` / `DPTMENT` | DPTMENT | Department master |

---

**Confidence: 91/100** — All 21 T7 programs confirmed from rwn_symbols.json; all 19 TAS6 BKRO*.RUN programs binary-analyzed (Pass 328); MTRO.* 40-field accessor map confirmed from binary string extraction; MTWC.* 24-field accessor map confirmed; MTOOL.* and TMACH.* accessor maps confirmed; TAS6 table handles (BKROMA, BKRTSPEC, BKRTTEMP) confirmed from binary allcap IDs; work center hierarchy logic and operation-type codes confirmed from UI strings. Remaining gap: exact Btrieve field byte offsets and types for ROUTING/WORKCTR not yet extracted from DDF (tables use a separate DDF not yet fully inspected).
