# Bill of Materials (BM)

Status: verified | Pass 332 (2026-06-26)

- **Module code**: `BM`
- **Tables**: 13 (10 BKBM* + 3 BKSB* approved-list tables)
- **Programs**: 17 (T7BMA–T7BMR + T7BMGNC + T7BMKPRINT stubs)
- **UI forms**: 16 (T7BMA–T7BMR DFMs)
- **Menu operations**: 10

---

## Programs (17 total)

Source: `samples/rwn_symbols.json` — all entries keyed to T7BM* path.

| Program | Procs | Lib | Role |
|---------|-------|-----|------|
| T7BMA.RWN | 218 | LISTG60.LIB | BOM editor — main CRUD interface for BKBMMSTR |
| T7BMB.RWN | 194 | DBA.LIB | BOM print (basic): PRT.2ND.DESC / PRT.DWG.PAR / PRT.VENDS / PRT.SPECS |
| T7BMC.RWN | 178 | DBA.LIB | Where-used multi-level: X_LEVEL/LEVEL/LVL_QTY/LVL_TOTAL + MEM_CODE/MEM_COMPONENT/MEM_PRNT_COST |
| T7BMD.RWN | 284 | DBA.LIB | BOM shortage/availability calculator — posts to GL via BKGLTRAN+DBAFIFO |
| T7BME.RWN | 119 | LISTG60.LIB | Remark copy: COPY.REMARKS = copies all remarks from one BOM to another |
| T7BMF.RWN | 86 | LISTG60.LIB | Simple item browser (FROM.ITEM only — minimal filter, pure browse) |
| T7BMG.RWN | 177 | LISTG60.LIB | Multi-level BOM explosion + cost rollup: ROLLUP flag, opens ROUTING+WORKCTR |
| T7BMH.RWN | 122 | LISTG60.LIB | Where-used browser: CHG.TIME/CHG.DATE + STDDAYS/STDMONTH/STDYEAR (lead time) |
| T7BMI.RWN | 202 | DBA.LIB | BOM print with routings: PRT.ROUTINGS flag adds routing op costs to printout |
| T7BMJ.RWN | 118 | LISTG60.LIB | Approved substitute parts browser: FROM.SUBST filter, BKARCUST + BKSBPART |
| T7BMK.RWN | 130 | LISTG60.LIB | Approved vendor BOM browser: FROM.VEND/SORT.BY.VEND, BKAPVEND + BKSBVEND |
| T7BML.RWN | 143 | LISTG60.LIB | Approved manufacturer BOM browser: FROM.MFG filter, BKSBMFG |
| T7BMP.RWN | 101 | LISTG60.LIB | Item + bin location browser: BKICMSTR + ISBINLOC (bin location pick list) |
| T7BMQ.RWN | 110 | LISTG60.LIB | BOM cost summary: MEM.QTY / TOT.COMP / SUB.TOT / COMP.EXT |
| T7BMR.RWN | 132 | LISTG60.LIB | BOM-to-order / ASN: BKARINVL + ISBUILD + QUOTE.NUMBER / COMP.QTY1-3 |
| T7BMGNC.RWN | 5 | T7BMGNC.SRC | Stub (GNC customization — no business logic) |
| T7BMKPRINT.RWN | 5 | T7BMKPrint.SRC | Stub (kit print — no business logic) |

---

## Program Details

### T7BMA — BOM Editor

218 procs, LISTG60.LIB, 41 DB files. The main BOM CRUD editor.

Key var namespaces confirmed from rwn_symbols.json:
- **BKBM.*** — 20-var BKBMMSTR field accessor: KEY/PARENT/PROD.LINE#/COMPONENT/QTY.REQD/REFERENCE/PROD.TYPE/SCRAP/OP/OPYN/PRICE/RTNUM/DUPOP/OPDSC/VEND/DATE1/DATE2/EXTRA/REV/P.TYPE/C.TYPE/EST.LINE/UID
  - PROD.TYPE = component type code
  - SCRAP = scrap percentage
  - OP = assigned routing operation
  - OPYN = operation flag
  - PRICE = standard price at BOM line level
  - RTNUM = routing number link
  - DUPOP = duplicate operation
  - OPDSC = operation description
  - P.TYPE / C.TYPE = parent/component type codes
  - EST.LINE = estimate line link
- **BKBM.RM.*** — 7-var BKBMREMK field accessor: PARENT/KEY/LINE/COMP/REMARK/UID/EXTRA
- **Feature/Option integration**: BKFOCFG + ISFOHEAD + ISFOLINE in DB list — product configurator BOM variants managed from T7BMA
- **Dimensional BOM**: BKBMDIM + BKICDIM — sheet-metal dimensional BOM co-managed
- **Material cost**: BKMATCST in DB list — material cost for BOM costing
- **ECO**: ISECO in T7BMB DB list — engineering change orders referenced in BOM prints

### T7BMD — Shortage/Availability Calculator

284 procs, DBA.LIB, 41 DB files. Most complex BM program.

Quantity variables (7 quantity types):
| Var | Meaning |
|-----|---------|
| UOSO | Units on Sales Orders |
| UBO | Units Backordered |
| UOO | Units on Open Orders |
| UIQC | Units in QC hold |
| UOWO | Units on Work Orders |
| UOA | Units on Allocations |
| UIWIP | Units in WIP |

Decision flags:
| Var | Meaning |
|-----|---------|
| SO.BO | SO backorder flag |
| PO.WO | PO/WO shortage flag |
| SHORT_FLAG | Shortage detected |
| REBUILD | Rebuild shortage list from scratch |

Math vars: QTY_TO_USE / QTY_TO_BUILD / QTY_REQUIRED

**GL posting**: Opens BKGLTRAN + DBAFIFO — T7BMD CAN POST to GL (shortage resolution writes financial entries when inventory is committed to meet shortage). This is the only BM program with GL write access.

### T7BMG — Multi-Level BOM Explosion + Cost Rollup

177 procs, LISTG60.LIB. Multi-level traversal with cost rollup:

| Var | Meaning |
|-----|---------|
| X_LEVEL | Current explosion depth |
| LEVEL | Node level in tree |
| LVL_QTY | Quantity at current level |
| LVL_TOTAL | Accumulated quantity through all parent levels |
| ROLLUP | Cost rollup flag — rolls unit costs up through all BOM levels |

Opens ROUTING + WORKCTR DB files: routing operation costs are included in the cost rollup computation. ROLLUP calculates MTIC.PROD.COST (rolled-up standard cost) from all BOM levels + routing operations.

### T7BMH — Where-Used Browser

122 procs, LISTG60.LIB. Where-used with lead time analysis:
- CHG.TIME / CHG.DATE — change timestamp tracking
- STDDAYS / STDMONTH / STDYEAR — standard lead time components

### T7BMI — BOM Print With Routings

202 procs, DBA.LIB. BOM print variant: **PRT.ROUTINGS** flag enables printing of routing operation costs alongside component lines.

### T7BMJ — Approved Substitutes

118 procs, LISTG60.LIB. Browse/manage approved substitute parts:
- FROM.SUBST — filter by substitute part number
- Tables: BKARCUST + BKSBPART

### T7BMK — Approved Vendor List

130 procs, LISTG60.LIB. Browse/manage approved vendor sourcing:
- FROM.VEND — filter by vendor
- SORT.BY.VEND — sort mode
- Tables: BKAPVEND + BKSBVEND

### T7BML — Approved Manufacturer List

143 procs, LISTG60.LIB. Browse/manage approved manufacturers:
- FROM.MFG — filter by manufacturer
- Tables: BKSBMFG

### T7BMQ — BOM Cost Summary

110 procs, LISTG60.LIB. Component cost calculation:
| Var | Meaning |
|-----|---------|
| MEM.QTY | Memory quantity (accumulated during traversal) |
| TOT.COMP | Total component count |
| SUB.TOT | Subtotal cost |
| COMP.EXT | Component extended cost |

### T7BMR — BOM-to-Order / ASN

132 procs, LISTG60.LIB. Generates orders or ASNs from BOM:
- QUOTE.NUMBER — links to a Sales Quote (make-to-order configured product path)
- COMP.QTY1 / COMP.QTY2 / COMP.QTY3 — component quantity tiers
- Tables: BKARINVL + ISBUILD

ISBUILD = carton/kit build table (also used by DE-D carton build module) — T7BMR bridges BOM component lists into kit assembly orders.

### T7BMP — Item + Bin Location Browser

101 procs, LISTG60.LIB. Browse items with bin location assignment:
- Tables: BKICMSTR + ISBINLOC (bin location per item)
- DFM caption: "BOM Pick List"

---

## Menu Operations

| Code | Operation | Program | Notes |
|------|-----------|---------|-------|
| BM-C | Print Where Used | T7BMC | Multi-level where-used print |
| BM-D | Print BOM Availability | T7BMD | Shortage/availability + GL posting |
| BM-E | Global Replace | T7BME | Remark copy utility |
| BM-F | Global Delete | T7BMF | Item browse / global delete |
| BM-G | Multi-level explosion | T7BMG | Explosion + cost rollup (ROLLUP) |
| BM-H | Print BOM at Average Cost | T7BMH | Where-used + lead time |
| BM-I | Print Summarized BOM | T7BMI | BOM print + routing costs |
| BM-J | Enter Approved Substitutes | T7BMJ | BKSBPART management |
| BM-J-C | Enter Approved Manufacturers | T7BML | BKSBMFG management |
| BM-X | BOM report | T7BMR | BOM-to-order / ASN (ISBUILD) |

Additional programs (T7BMK, T7BMP, T7BMQ, T7BMGNC, T7BMKPRINT) are accessed via submenu or subsystem, not direct menu codes.

---

## Database Tables (13 total)

### Core BOM Tables (10 — BKBM*)

Full field details in `../../../samples/ddf/schema.md`.

| Table | Fields | Key Fields | Purpose |
|-------|--------|-----------|---------|
| BKBMMSTR | 26 | PARENT + COMPONENT | Current/active BOM lines |
| BKBMAMTR | 26 | PARENT + COMPONENT | Actual-cost BOM snapshot |
| BKBMAVAL | 26 | PARENT + COMPONENT | Actual-value BOM snapshot |
| BKBMEMTR | 26 | PARENT + COMPONENT | Estimated BOM snapshot |
| BKBMSUMM | 26 | PARENT + COMPONENT | BOM summary snapshot |
| BKBMCNFG | 7 | NUM + GLACT + GLDPT | BOM configuration / GL account linkage |
| BKBMDIM | 11 | DIM_PARENT + LINE + COMP | Sheet-metal dimensional BOM |
| BKBMERMK | 20 | RM_PARENT + LINE + COMP | Engineering remarks (10×64 lines) |
| BKBMREMK | 20 | RM_PARENT + LINE + COMP | Regular remarks (10×64 lines) |
| BKBMNOTE | 16 | NT_PARENT | Parent-level notes (15×64 lines) |

The 5 main BOM data tables (BKBMMSTR/AMTR/AVAL/EMTR/SUMM) share an identical 26-field schema — parallel-snapshot architecture preserving current, actual, estimated, and summary states.

### Approved List Tables (3 — BKSB*) — Pass 317 DDF-confirmed

These tables are managed by T7BMJ/K/L and are also read by MRP planning programs.

#### BKSBPART — Approved Substitute Parts (5 fields)

| Field | Type | Size | Meaning |
|-------|------|------|---------|
| `BKSB_PART_PARNT` | STRING | 15 | Parent assembly part number (PK) |
| `BKSB_PART_PROD` | STRING | 15 | Component/product code (PK) |
| `BKSB_PART_CUST` | STRING | 10 | Customer code (PK — customer-specific substitutes) |
| `BKSB_PART_SUBST` | STRING | 15 | Approved substitute part number |
| `BKSB_PART_EXTRA` | STRING | 50 | Spare/notes field |

#### BKSBVEND — Approved Vendors (6 fields)

| Field | Type | Size | Meaning |
|-------|------|------|---------|
| `BKSB_VEND_PARNT` | STRING | 15 | Parent assembly part number (PK) |
| `BKSB_VEND_PROD` | STRING | 15 | Component/product code (PK) |
| `BKSB_VEND_CUST` | STRING | 10 | Customer code (PK — customer-specific sourcing) |
| `BKSB_VEND_VEND` | STRING | 10 | Approved vendor code (FK → BKAPVEND) |
| `BKSB_VEND_VPART` | STRING | 25 | Vendor's part number for this component |
| `BKSB_VEND_EXTRA` | STRING | 50 | Spare/notes field |

#### BKSBMFG — Approved Manufacturers (16 fields)

| Field | Type | Size | Meaning |
|-------|------|------|---------|
| `BKSB_MFG_PARNT` | STRING | 15 | Parent assembly part number (PK) |
| `BKSB_MFG_PROD` | STRING | 15 | Component/product code (PK) |
| `BKSB_MFG_CUS` | STRING | 10 | Customer code (PK) |
| `BKSB_MFG_MANUF` | STRING | 25 | Manufacturer name (PK) |
| `BKSB_MFG_MPART` | STRING | 25 | Manufacturer's part number |
| `BKSB_MFG_EXTRA` | STRING | 50 | Spare/notes field |
| `BKSB_MFG_MAKING` | STRING | 10 | "Making" status code (assembly process flag) |
| `BKSB_MFG_ALPHA_1` | STRING | 30 | Alpha field 1 (user-defined) |
| `BKSB_MFG_ALPHA_2` | STRING | 30 | Alpha field 2 (user-defined) |
| `BKSB_MFG_GDATES_1` | DATE | 4 | Generic date 1 (e.g., approval/expiry date) |
| `BKSB_MFG_GDATES_2` | DATE | 4 | Generic date 2 |
| `BKSB_MFG_FLAGS_1` | STRING | 1 | Flag 1 (Y/N status flag) |
| `BKSB_MFG_FLAGS_2` | STRING | 1 | Flag 2 |
| `BKSB_MFG_FLAGS_3` | STRING | 1 | Flag 3 |
| `BKSB_MFG_FLAGS_4` | STRING | 1 | Flag 4 |
| `BKSB_MFG_FLAGS_5` | STRING | 1 | Flag 5 |

BKSBMFG is the richest of the three — 16 fields vs 5–6 for the other two, with manufacturer-specific dates (approval/certification dates) and 5 status flags. This supports approval workflows (e.g., `GDATES_1` = approval date, `FLAGS_1` = approved/pending flag).

---

## UI Forms (16)

| DFM File | Caption | Fields | Controls |
|----------|---------|--------|----------|
| T7BMA.DFM | New Screen | 44 | 105 |
| T7BMAx.DFM | New Screen | 42 | 77 |
| T7BMB.DFM | BM-B | 28 | 58 |
| T7BMC.DFM | BM-C | 6 | 27 |
| T7BMD.DFM | Print Availability | 18 | 46 |
| T7BME.DFM | BM-E | 6 | 24 |
| T7BMF.DFM | BM-F | 2 | 18 |
| T7BMG.DFM | BM-G | 18 | 48 |
| T7BMH.DFM | BM-H | 11 | 33 |
| T7BMI.DFM | BM-I | 16 | 40 |
| T7BMJ.DFM | (empty caption) | 0 | 1 |
| T7BMK.DFM | (empty caption) | 0 | 1 |
| T7BML.DFM | (empty caption) | 0 | 1 |
| T7BMP.DFM | BOM Pick List | 7 | 29 |
| T7BMQ.DFM | BM-Q | 3 | 21 |
| T7BMR.DFM | BM-R | 16 | 43 |

T7BMJ/K/L DFMs have 0 fields + 1 control each — grid-only launch screens (the grid is the entire UI).

---

## TAS6-era programs (BKBM*.RUN) — complete binary inventory (Pass 323, 2026-06-26)

17 TAS Pro 6 `.RUN` programs confirmed from binary string extraction. All files in `samples/`.

| File | Size | Menu code | Operation | Key tables |
|------|-----:|-----------|-----------|------------|
| `BKBMA.RUN` | 307 KB | BM-A | Enter Bills of Material (also: "Edit Imported BOMs", "Enter Estimates [BOM]") | BKBMMSTR, BKBMDIM, BKBMREMK, BKBMNOTE, BKFOCFG, BKICDIM, BKESHA |
| `BKBMB.RUN` | 223 KB | BM-B | Print Bills of Material (+ Print Features and Options) | BKBMMSTR, BKBMREMK, BKBMNOTE, BKBMMSTRFP |
| `BKBMC.RUN` | 206 KB | BM-C | Print Where Used (multi-level) | BKBMMSTR, BKBMMSTRF, BKICREF |
| `BKBMD.RUN` | 331 KB | BM-D | Print BOM Availability (shortage + demand calc; largest BM file) | BKBMMSTR, BKARINVL, BKAPPOL, BKAPPO, BKBMAVAL |
| `BKBME.RUN` | 94 KB | BM-E | Global Replace (replace one component across all BOMs) | BKBMMSTR, BKSBMFG, BKSBVEND |
| `BKBMF.RUN` | 94 KB | BM-F | Global Delete | BKBMMSTR, BKSBMFG, BKSBVEND |
| `BKBMG.RUN` | 252 KB | BM-G | Print/Rollup Standard Costs (multi-level cost explosion up BOM tree) | BKBMMSTR, BKBMREMK, BKBMNOTE, BKICMSTR |
| `BKBMH.RUN` | 213 KB | BM-H | Print BOM at Average Cost | BKBMMSTR, BKBMREMK, BKBMNOTE, BKICMSTR |
| `BKBMH1.RUN` | 147 KB | BM-H | (older variant of BM-H — Print BOM at Average Cost) | same tables as BKBMH |
| `BKBMH2.RUN` | 205 KB | BM-B-A | Print Features and Options variant (accesses AP history PO lines) | BKBMMSTR, BKAPPOL, BKAPHPOL |
| `BKBMI.RUN` | 229 KB | BM-I | Print Summarized BOM / Pick List (uses temp file lock; one user at a time) | BKBMMSTR, BKBMSUMM, BKICREF |
| `BKBMJ.RUN` | 195 KB | BM-J | Enter Approved Substitutes | BKSBMFG, BKSBVEND, BKSBPART, BKICREF |
| `BKBMJC.RUN` | 99 KB | BM-J-C | Enter Approved Manufacturers | BKSBMFG, BKSBVEND |
| `BKBMK.RUN` | 4 KB | BM-K-A | (stub) | BKPOLA, BKSYMSTR |
| `BKBML.RUN` | 196 KB | BM-L-A | Enter Approved Manufacturers (older variant of BM-J-C) | BKSBMFG |
| `BKBMM.RUN` | 196 KB | (SM-J-Q) | BOM Recursion Utility — title says "SM-J-Q" (Service Management), not BM | BKBMMSTR, BKICMSTR |
| `BKBMX.RUN` | 192 KB | BM-X | Change Item Class utility (binary: "New Item Class" / "Change Item Class?") | BKBMMSTR, BKICMSTR |

### Key findings from binary analysis

**Multi-level BOM explosion confirmed:**
- `BKBMC.RUN` (BM-C) = multi-level **Where Used** — uses `BKBMMSTRF` (filter variant) and `BKICREF` (cross-reference index) to traverse the BOM tree upward
- `BKBMG.RUN` (BM-G) = multi-level **cost rollup** — rolls standard costs up through all BOM levels via `BKBMMSTRF0` (filter variant with 0 suffix); writes to MTIC.PROD.COST
- `BKBMI.RUN` (BM-I) = summarized/multi-level **pick list** — uses `BKBMSUMM` to accumulate summarized quantities across BOM levels (one line per part across all BOM levels)
- `BKBMD.RUN` (BM-D) = multi-level **availability** — also reads `BKARINVL` (SO demand) and `BKAPPOL` (PO supply) for shortage calculation

**BKICREF — Where Used cross-reference index:**
Appears in BKBMC (Where Used), BKBMI (pick list), BKBMJ (substitutes), BKBME (global replace). `BKICREF` is the reverse BOM index: given a component part, look up which parents use it. This accelerates the "where used" search without scanning all BKBMMSTR records.

**BKBMMSTR filter variants discovered:**
| Variant | Seen in | Likely role |
|---------|---------|-------------|
| `BKBMMSTR` | all programs | Live BOM lines |
| `BKBMMSTRF` | BKBMC, BKBMH, BKBMJ | Filter/find variant (alternate key by parent) |
| `BKBMMSTRF0` | BKBMG | F0 variant — perhaps "first component" key for cost rollup |
| `BKBMMSTRFP` | BKBMB | FP variant — Features and Products BOM line? |
| `BKBMMSTRL` | BKBMH | L variant — "last" key |
| `BKBMMSTRI` | BKBME/F/G | I variant — index (alternate-key open) |

**BKBMA.RUN dual-module integration:**
Opens `BKESHA` (Estimating Spec Header Archive) — confirming BM-A is the BOM entry point for the Estimating module as well. Also opens `BKICDIM` (item dimension master) alongside `BKBMDIM` (BOM-specific dimensions) — the two dimension tables are managed together during BOM entry.

**BKBMM.RUN — SM module recursion utility:**
Title string "SM-J-Q  Bill of Material Recursion Utility" indicates this program belongs to the **Service Management (SM)** module, not BM. It detects and resolves circular/recursive BOM references (a part that is a component of itself). Registered as SM-J-Q.

---

## Key Relationships

- T7BMA is the only program that writes BKBMMSTR — all other BM programs read it
- T7BMD is the only BM program with GL write access (BKGLTRAN + DBAFIFO)
- T7BMG ROLLUP computes MTIC.PROD.COST — the result feeds into IC standard costing
- T7BMR ISBUILD bridges BOM component lists → kit/carton assembly orders (also used by DE module)
- T7BMR QUOTE.NUMBER links BOM-to-order through Sales Quotes (SO module)
- BKFOCFG + ISFOHEAD + ISFOLINE in T7BMA DB list = Features/Options product configurator variants are managed as BOM branches
- BKSBPART/VEND/MFG are also read by MRP programs (procurement planning uses approved sourcing lists)

---

## Live Data Analysis (Pass 419, 2026-06-30)

All counts from live ODBC queries against DSN=DBA.

### BKBMMSTR — BOM Lines

208,686 active BOM lines. With BKICMSTR at 50,790 items, this averages **~4.1 BOM component lines per item** across the entire catalog — consistent with a mixed catalog of purchased parts (0 BOM lines), simple assemblies (1–3 lines), and complex multi-level sub-assemblies (10+ lines).

BOM depth depends on item type: R-type (Regular/purchased) items have no BOM; F/A/B-type manufactured items carry all the BOM volume. With F+A+B = 28,414 items in BKICMSTR, the manufacturing items average ~7.3 BOM lines each.

---

**Confidence: 90/100** — All 17 programs confirmed from rwn_symbols.json; BKBM* 10-table schemas + BKSB* 3-table schemas all confirmed from DDF (Pass 317); program roles and key vars confirmed from named-var extraction. Remaining gap: T7BMGNC and T7BMKPRINT stub purpose unconfirmed (minor — both are small programs with no business logic).

---

## Pass 332 — additional BKBM\*.RUN binary findings (2026-06-26)

Re-extraction of all 17 `samples/BKBM*.RUN` files for namespaces, table open patterns, and message strings.

### BKBMX.RUN — correction

Prior Pass 323 said "Inactive Bill of Material Utility". Binary string extraction shows the screen prompt is **"Change Item Class?"** with input field **"New Item Class"**. BKBMX.RUN is an item class reclassification utility — it updates `BKICMSTR` class for items across the BOM.

### RoHS binary confirmation

`BKBMH.RUN` contains the literal screen messages:
- `"All components are ROHS compliant"`
- `"Not all components are ROHS compliant"`

This is binary proof that RoHS compliance status is evaluated at BOM print time in the TAS6 generation. BKBMH iterates all BOM components and sets the compliance summary message. The check was already present before the T7 rewrite.

### BKARSIVLA — new table

`BKARSIVLA` appears in BKBMA, BKBMB, BKBMC, BKBMD, BKBMG, BKBMH, BKBMH1, BKBMH2, BKBMI. Inferred role: AR SI (Sales Invoice?) Variance / Level / Archive table — opened by most BOM programs as a session-context or currency table. Exact schema unknown; DDF lookup needed.

### New accessor namespaces confirmed

| Namespace | Seen in | Meaning |
|-----------|---------|---------|
| `BKIC.LOC.UALLOC` | BKBMA–BKBMM | IC location unallocated quantity |
| `BKIC.REF.CUSCODU` | BKBMA–BKBMX | IC reference customer code (uppercase variant) |
| `BKIC.PROD.UALLOC` | BKBMD | IC product unallocated quantity |
| `BKIC.PROD.TOTVL` | BKBMD | IC product total value |
| `BKIC.PROD.LRCPTR` | BKBMH2 | IC product last received cost pointer |
| `BKSB.PART.PARNT` | BKBMB, BKBMC, BKBMI | SB approved substitute parent field |
| `BKSB.VEND.PARNT` | BKBMB, BKBMC | SB approved vendor parent field |
| `ISFO.LIN.QTYREQ` | BKBMA | F/O option line quantity required |
| `BKBM.DIM.PARENT` | BKBMA | BM dimensional BOM parent field |
| `BKAP.PO.CONFIRMJ` | BKBMD | AP PO confirmed-job flag (demand side of shortage calc) |
| `BKAR.INVL.INVNM` | BKBMD | AR invoice line invoice number field |
| `BKIC.LOCM.STATE` | BKBMD | IC location-machine state (availability considers machine state) |

### BKBMM.RUN — additional confirmation

Binary strings from BKBMM.RUN include the report header `"BILL OF MATERIAL RECURSION ERROR REPORT"` and type-filter labels `"[B] Phantom Assembly"` / `"[O] Feature"`. This confirms the program detects circular BOM references specifically for Phantom Assembly (B) and Feature (O) type components, which are the types most likely to cause phantom recursion. The `BKWOAA` table open confirms WO archives are scanned for WIP with recursive BOM structures.
