# Physical Inventory (PI)

Status: verified (auto-generated from the extracted schema, menu-code dump, and DFM inventory).

- **Module code**: `PI`
- **Tables**: 7 (prefixes `BKPI`)
- **UI forms**: 10 (prefixes `T7PI`, `T6PI`)
- **Menu operations**: 9

## Menu operations

| Code | Operation | Legacy module file(s) |
| ---- | --------- | --------------------- |
| `PI-A` | Frozen Inventory Report | BKPIA;BKPIB |
| `PI-B` | Frozen Inventory Report | BKPIB |
| `PI-C` | Enter Tag Counts | BKPIC |
| `PI-C-A` | Physical Inventory Exception Report | BKPICA;T6PICA |
| `PI-D` | Missing Tags Report | BKPID |
| `PI-E` | Edit Frozen Inventory Costs | BKPIE |
| `PI-F` | Physical Inventory Report | BKPIF;T6PIF |
| `PI-G` | Update Actual Inventory | BKPIF;BKPIG;T6PIF |
| `PI-H` | Purge Physical Inventory | BKPIF;BKPIH;T6PIF |

## UI forms (10)

| DFM file | Caption | fields | controls | tabs |
| -------- | ------- | -----: | -------: | ---: |
| `T7PIA.DFM` | PI-A Capture Frozen Inventory | 31 | 65 | 0 |
| `T7PIB.DFM` | PI-B Frozen Inventory Report | 10 | 34 | 0 |
| `T7PIC.DFM` |  | 0 | 1 | 0 |
| `T7PICA.DFM` | PI-C-A  Physical Inventory Exception Report | 6 | 26 | 0 |
| `T7PID.DFM` | PI-D  Missing Tags Report | 4 | 28 | 0 |
| `T7PIE.DFM` |  | 0 | 1 | 0 |
| `T7PIF.DFM` | PI-F Phisical Inventory Report | 13 | 44 | 0 |
| `T7PIG.DFM` | PI-G Update Actual Inventory | 11 | 40 | 0 |
| `T7PIH.DFM` | PI-H Purge Physical Inventory | 3 | 21 | 0 |
| `T7PILOC.DFM` |  | 0 | 3 | 0 |

## Database tables (7)

Full field details are in `../../../samples/ddf/schema.md` (see per-table heading).

| Table | File on disk | Fields | Key fields (first 3) |
| ----- | ------------ | -----: | -------------------- |
| **BKPIFROZ** | `BKPIFROZ.B` | 19 | `BKPH_INFO_UOH`, `BKPH_INFO_YEAR`, `BKPH_INFO_QTR` |
| **BKPILCNT** | `BKPILCNT.B` | 10 | `BKPI_LOT_YEAR`, `BKPI_LOT_QTR`, `BKPI_LOT_CODE` |
| **BKPILOT** | `BKPILOT.B` | 10 | `BKPI_LOT_YEAR`, `BKPI_LOT_QTR`, `BKPI_LOT_CODE` |
| **BKPIMSTR** | `BKPIMSTR.B` | 3 | `BKPI_MSTR_YEAR`, `BKPI_MSTR_QTR`, `BKPI_MSTR_DESC` |
| **BKPIPHYS** | `BKPIPHYS.B` | 14 | `BKPH_TAGNUM`, `BKPH_ACTQTY`, `BKPH_EMPNUM` |
| **BKPISCNT** | `BKPISCNT.B` | 10 | `BKPI_SER_YEAR`, `BKPI_SER_QTR`, `BKPI_SER_CODE` |
| **BKPISER** | `BKPISER.B` | 10 | `BKPI_SER_YEAR`, `BKPI_SER_QTR`, `BKPI_SER_CODE` |

## Table documentation (confirmed from DDF schema.md, Pass 111a 2026-06-19)

Physical inventory runs as a periodic "count and reconcile" process. Each count cycle is identified by a YEAR+QTR pair. The workflow is: PI-A freezes current inventory → PI-B prints count sheets → PI-C enters tag counts → PI-G reconciles and posts adjustments → PI-H purges the count session.

### BKPIMSTR — Physical Inventory Session Master (3 fields)

Primary key: `BKPI_MSTR_YEAR` (STRING 4) + `BKPI_MSTR_QTR` (STRING 2)

| Field | Type | Meaning |
|-------|------|---------|
| `BKPI_MSTR_YEAR` | STRING 4 | Count year (PK 1) |
| `BKPI_MSTR_QTR` | STRING 2 | Count quarter/period code (PK 2) |
| `BKPI_MSTR_DESC` | STRING 30 | Description of this count session |

Session header. One row per count cycle. Created by PI-A (Capture Frozen Inventory).

---

### BKPIFROZ — Frozen Inventory Snapshot (19 fields)

Primary key: `BKPH_INFO_YEAR` + `BKPH_INFO_QTR` + `BKPH_INFO_PROD` (part code) + `BKPH_INFO_LOC`

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
| `BKPH_INFO_PCOST` | FLOAT | Prior period cost (for variance comparison) |
| `BKPH_INFO_PADJ` | FLOAT | Prior adjustment quantity |
| `BKPH_INFO_ACCTA` | STRING 10 | GL account (adjustment) |
| `BKPH_INFO_DEPTA` | STRING 4 | GL department (adjustment) |
| `BKPH_INFO_ACCTC` | STRING 10 | GL account (cost) |
| `BKPH_INFO_DEPTC` | STRING 4 | GL department (cost) |
| `BKPH_INFO_PUNIT` | FLOAT | Prior period unit cost |
| `BKPH_INFO_TAGS` | UBINARY | Tag count for this item/location |

Populated by PI-A. One row per part/location combination at freeze time. GLPST and INPST are cleared to N at creation and set to Y when PI-G posts adjustments.

---

### BKPIPHYS — Physical Count Tag (14 fields)

Primary key: `BKPH_TAGNUM` (FLOAT — sequential tag number)

| Field | Type | Meaning |
|-------|------|---------|
| `BKPH_TAGNUM` | FLOAT | Tag number (PK — unique sequential number) |
| `BKPH_ACTQTY` | FLOAT | Actual counted quantity |
| `BKPH_EMPNUM` | UBINARY | Counter employee number |
| `BKPH_EMPNAME` | STRING 15 | Counter employee name |
| `BKPH_COMMENT` | STRING 30 | Count comment / note |
| `BKPH_COUNTDATE` | DATE | Date the count was performed |
| `BKPH_YEAR` | STRING 4 | Count session year |
| `BKPH_QTR` | STRING 2 | Count session quarter |
| `BKPH_LOC` | STRING 10 | Warehouse location counted |
| `BKPH_CODE` | STRING 15 | Part number counted |
| `BKPH_FDATE` | DATE | Freeze date (matches BKPIFROZ.BKPH_INFO_FDATE) |
| `BKPH_LOT` | STRING 15 | Lot number (if lot-tracked) |
| `BKPH_SERIAL` | STRING 25 | Serial number (if serial-tracked) |
| `BKPH_BIN` | STRING 10 | Bin location within warehouse |

One row per physical count tag entered via PI-C (Enter Tag Counts). PI-D (Missing Tags) reports BKPIFROZ rows with no matching BKPIPHYS tag. PI-G compares BKPIPHYS.BKPH_ACTQTY to BKPIFROZ.BKPH_INFO_UOH and posts adjustment transactions (INVTXN) for variances.

---

### BKPILOT — Physical Inventory Lot Snapshot (10 fields)

Primary key: `BKPI_LOT_YEAR` + `BKPI_LOT_QTR` + `BKPI_LOT_CODE` (part) + `BKPI_LOT_LOT`

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

Frozen lot breakdown for lot-tracked items. Created by PI-A for each lot present at freeze time.

---

### BKPILCNT — Physical Count Lot Entry (10 fields)

Identical schema to BKPILOT. Primary key: `BKPI_LOT_YEAR` + `BKPI_LOT_QTR` + `BKPI_LOT_CODE` + `BKPI_LOT_LOT`

This is the **counted** lot table (entered via PI-C), whereas BKPILOT is the **frozen** snapshot. PI-G compares BKPILCNT to BKPILOT to compute lot-level variances.

---

### BKPISER — Physical Inventory Serial Snapshot (10 fields)

Primary key: `BKPI_SER_YEAR` + `BKPI_SER_QTR` + `BKPI_SER_CODE` (part) + `BKPI_SER_SERIAL`

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

Frozen serial number list at PI-A time. Each serial item that was in inventory at freeze gets one row.

---

### BKPISCNT — Physical Count Serial Entry (10 fields)

Identical schema to BKPISER. Primary key: `BKPI_SER_YEAR` + `BKPI_SER_QTR` + `BKPI_SER_CODE` + `BKPI_SER_SERIAL`

The **counted** serial table (entered via PI-C), compared to BKPISER by PI-G to find missing/extra serial numbers.

---

## Physical inventory workflow (confirmed from menu operations + table structure)

```
PI-A: Capture Frozen Inventory
  → Snapshot BKICMSTR (on-hand qtys) into BKPIFROZ  (one row per part/location)
  → Snapshot LOT table into BKPILOT  (one row per lot)
  → Snapshot SERIAL table into BKPISER  (one row per serial#)
  → Create BKPIMSTR session header

PI-B: Print count sheets  (from BKPIFROZ — tells counters what to count)

PI-C: Enter Tag Counts
  → Insert rows into BKPIPHYS  (one tag per count)
  → For lot-tracked: update BKPILCNT
  → For serial-tracked: update BKPISCNT

PI-C-A: Exception Report  (tags entered vs. frozen items)

PI-D: Missing Tags Report  (BKPIFROZ rows with no BKPIPHYS match)

PI-E: Edit Frozen Costs  (update BKPH_INFO_COST in BKPIFROZ)

PI-F: Physical Inventory Report  (compare BKPIPHYS to BKPIFROZ — shows variances)

PI-G: Update Actual Inventory
  → For each BKPIPHYS tag: delta = BKPH_ACTQTY − BKPIFROZ.BKPH_INFO_UOH
  → Post adjustment transaction to INVTXN (TYPE = PI adjustment)
  → Update BKICMSTR on-hand quantity
  → Set BKPIFROZ.BKPH_INFO_GLPST = Y and INPST = Y

PI-H: Purge Physical Inventory  (remove all BKPI* rows for the session)
```

## Notes & open questions

- BKPILOT and BKPILCNT have identical field schemas — the distinction is "frozen" (PILOT) vs "counted" (PILCNT). Same pattern for BKPISER vs BKPISCNT.
- BKPH_INFO_TAGS in BKPIFROZ tracks how many tags were entered for the item — used by PI-D to detect zero-tag items.
- PI-C-A (Exception Report) is a sub-program of PI-C — the T6PICA form shows it's a legacy T6 form also available.
- The YEAR+QTR key structure allows multiple concurrent or historical count sessions — though in practice only one active session would make sense at a time to avoid data conflicts.
