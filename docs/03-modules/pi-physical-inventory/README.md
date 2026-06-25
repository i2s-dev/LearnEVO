# Physical Inventory (PI)

Status: verified | Pass 260 (2026-06-25)

- **Module code**: `PI`
- **Tables**: 10 (7 BKPI* core + 3 IS-prefix auxiliary: ISCYCLCD, PIBINLOC, ISBNMSTR)
- **Programs**: 9 (T7PIA–T7PIH + T7PICA)
- **UI forms**: 10 (T7PIA–T7PIH + T7PICA + T7PILOC)
- **Menu operations**: 9

Source: `samples/rwn_symbols.json` (T7PI* entries); DDF schemas from `samples/ddf/schema.md`.

---

## Programs (9 total)

| Program | Procs | Lib | DB Files | Role |
|---------|-------|-----|----------|------|
| T7PIA.RWN | 159 | LISTG60.LIB | 33 | PI-A: Capture Frozen Inventory — creates BKPIMSTR session, snapshots BKICMSTR→BKPIFROZ; opens ISCYCLCD (cycle count codes) |
| T7PIG.RWN | 155 | LISTG60.LIB | 45 | PI-G: Update Actual Inventory — posts INVTXN adjustments; opens PIBINLOC+ISBNMSTR for bin-level updates |
| T7PIC.RWN | 152 | LISTG60.LIB | 29 | PI-C: Enter Tag Counts — inserts BKPIPHYS tags; BKPRMSTR validates counter employee |
| T7PIF.RWN | 137 | LISTG60.LIB | 28 | PI-F: Physical Inventory Report — variance preview before posting; opens ISBUILD for kit item handling |
| T7PIB.RWN | 114 | LISTG60.LIB | 49 | PI-B: Print Count Sheets — prints BKPIFROZ contents for counters; opens PIBINLOC |
| T7PID.RWN | 98  | EVO.LIB     | 49 | PI-D: Missing Tags Report — reports BKPIFROZ rows with no BKPIPHYS count; BEGTAG = beginning tag number filter |
| T7PICA.RWN | 97 | LISTG60.LIB | 49 | PI-C-A: Alternate Tag Count Entry — same DB scope as T7PIC; grid-only variant |
| T7PIE.RWN | 76  | LISTG60.LIB | 49 | PI-E: Variance Summary (LISTG60 grid; reads BKPH.INFO.PADJ/PCOST/QTR/UOH from BKPIFROZ) |
| T7PIH.RWN | 68  | LISTG60.LIB | 49 | PI-H: Purge Physical Inventory — removes all BKPI* rows for the session |

Note: T7PIF opens ISBUILD — kit/carton assemblies require special handling during the PI report because kit components may be in ISBUILD rather than BKICMSTR inventory.

---

## Menu Operations

| Code | Operation | Program | DFM Caption |
|------|-----------|---------|------------|
| PI-A | Capture Frozen Inventory | T7PIA | PI-A Capture Frozen Inventory |
| PI-B | Print Count Sheets | T7PIB | PI-B Frozen Inventory Report |
| PI-C | Enter Tag Counts | T7PIC | (grid-only, no DFM caption) |
| PI-C-A | Alternate Tag Entry / Exception Report | T7PICA | PI-C-A Physical Inventory Exception Report |
| PI-D | Missing Tags Report | T7PID | PI-D Missing Tags Report |
| PI-E | Variance Summary | T7PIE | (grid-only, no DFM caption) |
| PI-F | Physical Inventory Report | T7PIF | PI-F Phisical Inventory Report (typo in DFM) |
| PI-G | Update Actual Inventory | T7PIG | PI-G Update Actual Inventory |
| PI-H | Purge Physical Inventory | T7PIH | PI-H Purge Physical Inventory |

---

## UI Forms (10)

| DFM File | Caption | Fields | Controls |
|----------|---------|--------|----------|
| T7PIA.DFM | PI-A Capture Frozen Inventory | 31 | 65 |
| T7PIB.DFM | PI-B Frozen Inventory Report | 10 | 34 |
| T7PIC.DFM | (empty — grid only) | 0 | 1 |
| T7PICA.DFM | PI-C-A Physical Inventory Exception Report | 6 | 26 |
| T7PID.DFM | PI-D Missing Tags Report | 4 | 28 |
| T7PIE.DFM | (empty — grid only) | 0 | 1 |
| T7PIF.DFM | PI-F Phisical Inventory Report | 13 | 44 |
| T7PIG.DFM | PI-G Update Actual Inventory | 11 | 40 |
| T7PIH.DFM | PI-H Purge Physical Inventory | 3 | 21 |
| T7PILOC.DFM | (empty — location selector helper) | 0 | 3 |

---

## Key Variable Namespaces

### BKPH.INFO.* — BKPIFROZ field accessor (18 vars confirmed)

Used by T7PIA/B/E/F/G to read BKPIFROZ frozen snapshot fields:

| Var | BKPIFROZ Field | Meaning |
|-----|---------------|---------|
| BKPH.INFO.ACCTA | BKPH_INFO_ACCTA | GL adjustment account |
| BKPH.INFO.ACCTC | BKPH_INFO_ACCTC | GL clearing account |
| BKPH.INFO.COST | BKPH_INFO_COST | Frozen unit cost |
| BKPH.INFO.DEPTA | BKPH_INFO_DEPTA | GL adjustment department |
| BKPH.INFO.DEPTC | BKPH_INFO_DEPTC | GL clearing department |
| BKPH.INFO.FDATE | BKPH_INFO_FDATE | Freeze date |
| BKPH.INFO.GLPST | BKPH_INFO_GLPST | GL posted flag (Y/N) |
| BKPH.INFO.INPST | BKPH_INFO_INPST | Inventory posted flag (Y/N) |
| BKPH.INFO.LOC | BKPH_INFO_LOC | Warehouse location |
| BKPH.INFO.LOT | BKPH_INFO_LOT | Lot-tracked flag |
| BKPH.INFO.PADJ | BKPH_INFO_PADJ | Prior adjustment quantity |
| BKPH.INFO.PCOST | BKPH_INFO_PCOST | Prior period cost |
| BKPH.INFO.PROD | BKPH_INFO_PROD | Part number |
| BKPH.INFO.PUNIT | BKPH_INFO_PUNIT | Prior period unit |
| BKPH.INFO.QTR | BKPH_INFO_QTR | Count period/quarter |
| BKPH.INFO.SER | BKPH_INFO_SER | Serial-tracked flag |
| BKPH.INFO.TAGS | BKPH_INFO_TAGS | Number of count tags for this item |
| BKPH.INFO.UOH | BKPH_INFO_UOH | Units on hand at freeze |

Note: T7PIB uses the extended set (PADJ/PCOST/PROD/PUNIT/QTR/SER/TAGS/UOH) for print-time batch summary fields — these are batch-level summary computations, not additional BKPIFROZ fields.

### BKPH.* — BKPIPHYS field accessor (tag-level vars)

Used by T7PIC/D/F/G to access individual count tag records:

| Var | Meaning |
|-----|---------|
| BKPH.ACTQTY | Actual counted quantity |
| BKPH.BIN | Bin location |
| BKPH.CODE | Part number |
| BKPH.COMMENT | Count comment |
| BKPH.COUNTDATE | Date counted |
| BKPH.EMPNAME | Counter employee name |
| BKPH.EMPNUM | Counter employee number |
| BKPH.FDATE | Freeze date |
| BKPH.LOC | Warehouse location |
| BKPH.LOT | Lot number |
| BKPH.TAGNUM | Sequential tag number (PK) |

---

## Database Tables (10 total)

### Core PI Tables (7 — BKPI*)

Full field details in `../../../samples/ddf/schema.md`.

| Table | Fields | Key Fields | Purpose |
|-------|--------|-----------|---------|
| BKPIMSTR | 3 | YEAR + QTR | Session header (one row per count cycle) |
| BKPIFROZ | 19 | YEAR + QTR + PROD + LOC | Frozen inventory snapshot per part/location |
| BKPIPHYS | 14 | TAGNUM | Count tags (one row per physical count entry) |
| BKPILOT | 10 | YEAR + QTR + CODE + LOT | Frozen lot quantities |
| BKPILCNT | 10 | YEAR + QTR + CODE + LOT | Counted lot quantities (vs BKPILOT) |
| BKPISER | 10 | YEAR + QTR + CODE + SERIAL | Frozen serial numbers |
| BKPISCNT | 10 | YEAR + QTR + CODE + SERIAL | Counted serial numbers (vs BKPISER) |

### Auxiliary IS-Prefix Tables (3 — confirmed Pass 260)

These tables are accessed by PI programs but are not prefixed BKPI*:

| Table | Program | Purpose |
|-------|---------|---------|
| ISCYCLCD | T7PIA | Cycle count code table — defines cycle count categories/modes used during PI-A freeze setup |
| PIBINLOC | T7PIB, T7PIG | Physical inventory bin location — PI-specific snapshot of bin-level inventory, distinct from ISBINLOC |
| ISBNMSTR | T7PIG | Bin name master — warehouse bin definitions; used during PI-G update to resolve bin names for INVTXN posts |

Note: ISCYCLCD schema is unconfirmed from DDF (not registered at install time or not in extracted DDF). PIBINLOC and ISBNMSTR are inferred from DB file list names.

---

## Table Field Documentation (confirmed from DDF, Pass 111a 2026-06-19)

Physical inventory runs as a periodic "count and reconcile" process. Each count cycle is identified by a YEAR+QTR pair. The workflow is:
PI-A freezes → PI-B prints sheets → PI-C enters tags → PI-D checks missing → PI-F previews variances → PI-G posts adjustments → PI-H purges session.

### BKPIMSTR — Physical Inventory Session Master (3 fields)

Primary key: `BKPI_MSTR_YEAR` + `BKPI_MSTR_QTR`

| Field | Type | Meaning |
|-------|------|---------|
| `BKPI_MSTR_YEAR` | STRING 4 | Count year (PK 1) |
| `BKPI_MSTR_QTR` | STRING 2 | Count quarter/period code (PK 2) |
| `BKPI_MSTR_DESC` | STRING 30 | Description of this count session |

Session header. One row per count cycle. Created by PI-A. ISCYCLCD provides the cycle count code options shown in T7PIA at freeze setup.

---

### BKPIFROZ — Frozen Inventory Snapshot (19 fields)

Primary key: `BKPH_INFO_YEAR` + `BKPH_INFO_QTR` + `BKPH_INFO_PROD` + `BKPH_INFO_LOC`

| Field | Type | Meaning |
|-------|------|---------|
| `BKPH_INFO_UOH` | FLOAT | Units on hand at freeze time |
| `BKPH_INFO_YEAR` | STRING 4 | Count year (PK 1) |
| `BKPH_INFO_QTR` | STRING 2 | Count quarter/period (PK 2) |
| `BKPH_INFO_LOC` | STRING 10 | Warehouse location (PK 3) |
| `BKPH_INFO_PROD` | STRING 15 | Part number (PK 4) |
| `BKPH_INFO_COST` | FLOAT | Unit cost at freeze time |
| `BKPH_INFO_GLPST` | STRING 1 | GL posted flag (Y after PI-G posts) |
| `BKPH_INFO_INPST` | STRING 1 | Inventory posted flag |
| `BKPH_INFO_FDATE` | DATE | Freeze date (when PI-A ran) |
| `BKPH_INFO_LOT` | STRING 1 | Lot-tracked flag (Y/N) |
| `BKPH_INFO_SER` | STRING 1 | Serial-tracked flag (Y/N) |
| `BKPH_INFO_PCOST` | FLOAT | Prior period cost |
| `BKPH_INFO_PADJ` | FLOAT | Prior adjustment quantity |
| `BKPH_INFO_ACCTA` | STRING 10 | GL account (adjustment debit) |
| `BKPH_INFO_DEPTA` | STRING 4 | GL department (adjustment) |
| `BKPH_INFO_ACCTC` | STRING 10 | GL account (cost clearing) |
| `BKPH_INFO_DEPTC` | STRING 4 | GL department (cost clearing) |
| `BKPH_INFO_PUNIT` | FLOAT | Prior period unit cost |
| `BKPH_INFO_TAGS` | UBINARY | Tag count for this item/location |

Populated by PI-A. One row per part/location combination. GLPST and INPST cleared to N at creation, set to Y when PI-G posts.

---

### BKPIPHYS — Physical Count Tag (14 fields)

Primary key: `BKPH_TAGNUM` (FLOAT — sequential tag number)

| Field | Type | Meaning |
|-------|------|---------|
| `BKPH_TAGNUM` | FLOAT | Tag number (PK) |
| `BKPH_ACTQTY` | FLOAT | Actual counted quantity |
| `BKPH_EMPNUM` | UBINARY | Counter employee number |
| `BKPH_EMPNAME` | STRING 15 | Counter employee name |
| `BKPH_COMMENT` | STRING 30 | Count comment |
| `BKPH_COUNTDATE` | DATE | Date counted |
| `BKPH_YEAR` | STRING 4 | Count session year |
| `BKPH_QTR` | STRING 2 | Count session quarter |
| `BKPH_LOC` | STRING 10 | Warehouse location |
| `BKPH_CODE` | STRING 15 | Part number |
| `BKPH_FDATE` | DATE | Freeze date |
| `BKPH_LOT` | STRING 15 | Lot number (if lot-tracked) |
| `BKPH_SERIAL` | STRING 25 | Serial number (if serial-tracked) |
| `BKPH_BIN` | STRING 10 | Bin location within warehouse |

One row per count tag entered via PI-C. PI-G compares BKPH_ACTQTY to BKPIFROZ.BKPH_INFO_UOH and posts INVTXN adjustments for variances.

---

### BKPILOT — Frozen Lot Snapshot (10 fields)

Primary key: `BKPI_LOT_YEAR` + `BKPI_LOT_QTR` + `BKPI_LOT_CODE` + `BKPI_LOT_LOT`

| Field | Type | Meaning |
|-------|------|---------|
| `BKPI_LOT_YEAR` | STRING 4 | Count session year |
| `BKPI_LOT_QTR` | STRING 2 | Count session quarter |
| `BKPI_LOT_CODE` | STRING 15 | Part number |
| `BKPI_LOT_LOT` | STRING 15 | Lot number |
| `BKPI_LOT_QTY` | FLOAT | Frozen quantity for this lot |
| `BKPI_LOT_TAG` | FLOAT | Tag number (link to BKPIPHYS) |
| `BKPI_LOT_LOC` | STRING 10 | Warehouse location |
| `BKPI_LOT_SERQTY` | FLOAT | Serial-tracked quantity within this lot |
| `BKPI_LOT_PSTD` | STRING 1 | Posted flag |
| `BKPI_LOT_BIN` | STRING 10 | Bin location |

Frozen lot breakdown. Created by PI-A for each lot present at freeze time.

---

### BKPILCNT — Counted Lot Entry (10 fields)

Identical schema to BKPILOT. The **counted** lot table (entered via PI-C) — PI-G compares BKPILCNT to BKPILOT for lot-level variances.

---

### BKPISER — Frozen Serial Snapshot (10 fields)

Primary key: `BKPI_SER_YEAR` + `BKPI_SER_QTR` + `BKPI_SER_CODE` + `BKPI_SER_SERIAL`

| Field | Type | Meaning |
|-------|------|---------|
| `BKPI_SER_YEAR` | STRING 4 | Count session year |
| `BKPI_SER_QTR` | STRING 2 | Count session quarter |
| `BKPI_SER_CODE` | STRING 15 | Part number |
| `BKPI_SER_SERIAL` | STRING 25 | Serial number |
| `BKPI_SER_QTY` | FLOAT | Quantity (normally 1 for serialized items) |
| `BKPI_SER_TAG` | FLOAT | Tag number (link to BKPIPHYS) |
| `BKPI_SER_LOC` | STRING 10 | Warehouse location |
| `BKPI_SER_LOTNO` | STRING 15 | Lot number (if also lot-tracked) |
| `BKPI_SER_PSTD` | STRING 1 | Posted flag |
| `BKPI_SER_BIN` | STRING 10 | Bin location |

Frozen serial list at PI-A. Each serial item in inventory at freeze gets one row.

---

### BKPISCNT — Counted Serial Entry (10 fields)

Identical schema to BKPISER. The **counted** serial table (entered via PI-C) — PI-G compares BKPISCNT to BKPISER to find missing/extra serial numbers.

---

## Physical Inventory Workflow

```
PI-A: Capture Frozen Inventory (T7PIA)
  → ISCYCLCD: select cycle count mode
  → Snapshot BKICMSTR on-hand qtys into BKPIFROZ (one row per part/location)
  → Snapshot LOT table into BKPILOT (one row per lot)
  → Snapshot SERIAL table into BKPISER (one row per serial#)
  → Create BKPIMSTR session header

PI-B: Print Count Sheets (T7PIB)
  → Read BKPIFROZ, consult PIBINLOC for bin detail
  → Prints count sheets showing what should be counted per item/location/bin

PI-C: Enter Tag Counts (T7PIC)
  → BKPRMSTR validates counter employee ID
  → Insert BKPIPHYS rows (one tag per count entry)
  → For lot-tracked: update BKPILCNT
  → For serial-tracked: update BKPISCNT

PI-C-A: Alternate Tag Count Entry (T7PICA)
  → Same DB scope as PI-C; grid-only interface variant

PI-D: Missing Tags Report (T7PID)
  → BEGTAG filter for starting tag range
  → Reports BKPIFROZ rows with no matching BKPIPHYS tag

PI-E: Variance Summary (T7PIE)
  → Reads BKPH.INFO.PADJ/PCOST/QTR/UOH from BKPIFROZ
  → Grid display of variance summary before posting

PI-F: Physical Inventory Report (T7PIF)
  → Compares BKPIPHYS counts to BKPIFROZ frozen qtys
  → Opens ISBUILD for kit/carton items (components in kit assembly)
  → Variance preview report — use before PI-G to confirm numbers

PI-G: Update Actual Inventory (T7PIG)
  → For each BKPIPHYS tag: delta = BKPH_ACTQTY − BKPIFROZ.BKPH_INFO_UOH
  → Post adjustment to INVTXN
  → Update BKICMSTR on-hand quantity
  → Set BKPIFROZ.BKPH_INFO_GLPST = Y and INPST = Y
  → Uses PIBINLOC + ISBNMSTR for bin-level inventory update

PI-H: Purge Physical Inventory (T7PIH)
  → Removes all BKPI* rows for the completed session
```

---

## Key Relationships

- T7PIA is the only program that writes BKPIMSTR and BKPIFROZ — all other programs read them
- T7PIG is the only program that posts to INVTXN (makes the inventory correction permanent)
- T7PIF opens ISBUILD — kit assemblies managed by the DE (carton build) module need special handling in the PI report because their components live in ISBUILD, not direct BKICMSTR inventory
- BKPILOT/BKPILCNT are the frozen/counted mirrors for lot items; BKPISER/BKPISCNT for serial items
- ISCYCLCD (cycle count codes) links PI to the cycle-count mode in T7PIA — allows partial counts by item class or cycle code rather than a full count
- PIBINLOC is distinct from ISBINLOC — PI uses a PI-specific bin location snapshot to avoid race conditions during counting
- BKPRMSTR (employee master) is used by T7PIC to authenticate/validate counter employee entries

---

**Confidence: 85/100** — All 9 programs confirmed from rwn_symbols.json with proc counts, lib assignments, and DB file lists; 7 BKPI* schemas confirmed from DDF; BKPH.INFO.* 18-var namespace confirmed from named-var extraction; workflow steps confirmed from program roles and DB file analysis; ISCYCLCD/PIBINLOC/ISBNMSTR existence confirmed from DB file lists but schemas not confirmed from DDF. Gap: ISCYCLCD field layout unknown; exact PIBINLOC structure vs ISBINLOC not compared.
