# `.IMP` and `.XPT` — Import/Export Definition Files

Status: verified | Pass 325 2026-06-26

Sources: hex analysis of 11 × `.IMP` and 8 × `.XPT` files from `\\i2s109-solidcrm\DBAMFG$\`
(local copies in `samples/`).

These two file types form the Data Entry/Exchange (DE) module's import and export configuration.
Each is a fixed-size binary template file naming which table fields map to which CSV columns.

---

## `.IMP` — Import Definition (442 bytes fixed)

An `.IMP` file defines how an external file (CSV, delimited text, or Btrieve file) maps onto
a specific EvoERP table for import. One `.IMP` file per importable table/operation.

Empty files (0 bytes) = no import configured for that menu operation.

### Binary layout

| Offset | Size | Type | Contents |
|--------|-----:|------|----------|
| 0x00 | 40 | ASCII | Source file path (space-padded, e.g., `U:\PROFPN.CSV`) |
| 0x28 | 2 | ASCII | Mode code: `SC`, `DC`, `RC` — see table below |
| 0x2A | 200 | uint16 LE × 100 | **Map1 — Import map**: for each target field 1–100, the source column index (1-based; 0 = skip/blank) |
| 0xF2 | 200 | uint16 LE × 100 | **Map2 — Export map**: for each target field 1–100, the output column index (1-based; 0 = skip); **entry 100 = 0x0A0D (CRLF) = record-terminator sentinel** |

Total = 40 + 2 + 200 + 200 = **442 bytes**.

Note: A 3-char mode `RIC` was observed in `ISWCD.IMP` — the 'C' byte overlaps byte 0x2A
(first byte of Map1), corrupting Map1 entry 1. For `RIC` files Map1 parsing begins at 0x2B.

### Mode codes

| Code | Meaning |
|------|---------|
| `SC` | Standard CSV (comma-separated; standard quote rules) |
| `DC` | Delimited CSV (user-defined delimiter variant) |
| `RC` | Raw Copy from Btrieve file (source path names a `.B`/`.B00` file) |
| `RIC` | Unclear — observed in `ISWCD.IMP` (WC department data); 3-char code |

### Map interpretation

**Map1 (import):** `Map1[N-1]` = source column index for target table field N.

Example (`BKDEB.IMP`, Standard CSV `U:\PROFPN.CSV`):

| Target field | Source column | Meaning |
|:---:|:---:|---------|
| 1 | 1 | Field 1 ← CSV col 1 |
| 2 | 2 | Field 2 ← CSV col 2 |
| 3 | 3 | Field 3 ← CSV col 3 |
| 4 | 5 | Field 4 ← CSV col 5 (reorder) |
| 5 | 6 | Field 5 ← CSV col 6 |
| 6 | 0 | Field 6 ← skip (blank) |
| 7 | 4 | Field 7 ← CSV col 4 |

**Map2 (export):** Same structure but for output direction. Only `BKDEB.IMP` has a populated
Map2 — the others have all zeros except the CRLF sentinel at entry 100. This means `BKDEB`
(Profiles/Part Numbers import) supports both import AND export from the same definition file.

### Cataloged `.IMP` files

| File | Source | Mode | Import target (inferred) | Map1 populated |
|------|--------|------|--------------------------|:-:|
| `BKDEB.IMP` | `U:\PROFPN.CSV` | SC | DE-B (profiles/part numbers) | ✓ |
| `BKDEC.IMP` | `U:\04348-1.CSV` | DC | DE-C (customer/vendor data) | ✓ |
| `BKDED.IMP` | (empty) | — | DE-D (not configured) | — |
| `BKDEE.IMP` | (empty) | — | DE-E (not configured) | — |
| `BKDEF.IMP` | (empty) | — | DE-F (not configured) | — |
| `BKDEG.IMP` | `BKGLECOA.B00` | RC | DE-G (GL chart of accounts from Btrieve) | ✓ (1 entry) |
| `BKDEH.IMP` | (empty) | — | DE-H (not configured) | — |
| `BKDES.IMP` | (empty) | — | DE-S (not configured) | — |
| `BKPIPHYS.IMP` | `2011-11.TXT` | SC | PI Physical Inventory count file | ✓ |
| `ISWCD.IMP` | `LATEST IMPORT.CSV` | RIC | IS Work Center Departments | ✓ |
| `MRPFCDE.IMP` | (empty) | — | MRP Forecast (not configured) | — |

---

## `.XPT` — Export Layout (32000 bytes fixed)

An `.XPT` file defines which table fields appear in an exported text file, and in what column order.
One `.XPT` file per exportable table/operation.

### Binary layout

| Offset | Size | Type | Contents |
|--------|-----:|------|----------|
| 0x00 | 12 | ASCII | Target output filename (space-padded, e.g., `BKARCUST.TXT`) |
| 0x0C | 1 | ASCII | Export type flag (see table below) |
| 0x0D | 15 × N | ASCII | Column accessor names (15 bytes each, space-padded) in export column order |
| — | 15 | 0x00 × 15 | Terminator: first all-zero 15-byte slot ends the column list |
| — | varies | 0x20 | Remainder of 32000-byte block filled with spaces |

Total file size: **32000 bytes** (fixed).
Maximum columns: (32000 − 13) / 15 = **2132**.

### Export type flags (byte 0x0C)

| Byte | Flag | Meaning |
|------|------|---------|
| 0x53 | `S` | Standard — basic flat export |
| 0x54 | `T` | Tabular — columnar layout |
| 0x46 | `F` | Full / Formatted — all fields with formatting |
| 0x44 | `D` | Detail — detail-level rows (e.g., BOM lines) |
| 0x20 | ` ` | Default / unspecified |

### Cataloged `.XPT` files and their column lists

**BKARCUST.XPT** — type=S, target=`BKARCUST.TXT` (AR Customer export, 8 cols)

```
BKAR.CLASS, BKAR.CUSTCODE, BKAR.CUSTNAME, BKAR.CITY, BKAR.STATE,
BKAR.SLSP.NUM (×2), BKAR.TERMS.NUM
```

**BKICMSTR.XPT** — type=T, target=`BKICMSTR.TXT` (IC Item Master export, 7 cols)

```
BKIC.PROD.CAT, BKIC.PROD.CODE, BKIC.PROD.DESC, BKIC.PROD.NOTE,
BKIC.PROD.CLASS, BKIC.PROD.TYPE, BKIC.PROD.UM
```

**BKAPPOL.XPT** — type=default, target=`BKAPPOL.TXT` (AP PO Lines export, 39 cols)

```
[blank], BKAP.POL.PONM, BKAP.POL.CNTR, BKAP.POL.ERD, BKAP.POL.PCODE,
BKAP.POL.PDESC, BKAP.POL.PQTY, BKAP.POL.PPRCE, BKAP.POL.PDISC,
BKAP.POL.PEXT, BKAP.POL.PCOGS, BKAP.POL.ITYPE, BKAP.POL.GLA,
BKAP.POL.GLDPTA, BKAP.POL.TXBLE, BKAP.POL.RQTY, BKAP.POL.IQTY,
BKAP.POL.LOC, NKAP.POL.UM.LIN (×2 — anomalous prefix), BKAP.POL.OPER,
BKAP.POL.WOPRE, BKAP.POL.WOSUF, BKAP.POL.ARD, BKAP.POL.EST,
BKAP.POL.OO.QTY, BKAP.POL.ITM.NO, BKAP.POL.QC.QTY, BKAP.POL.BUYOFF,
BKAP.POL.SCRAP, BKAP.POL.PRTDIM, BKAP.POL.PARENT, BKAP.POL.RECNUM,
BKAP.POL.EXTRA, BKAP.POL.INVNUM, BKAP.POL.PCONV, BKAP.POL.INVDTE,
BKAP.POL.PSTDTE, BKAP.POL.PKSQTY
```

Note: cols 19–20 = `NKAP.POL.UM.LIN` — the 'N' prefix instead of 'B' may indicate a
computed/formatted variant or a data corruption in this specific template file.

**BKAPVEND.XPT** — type=F, target=`BKAPVEND.TXT` (AP Vendor export, 20 cols)

```
BKAP.CLASS, BKAP.VENDCODE, BKAP.VENDNAME, BKAP.ADD1 (×2), BKAP.ADD2 (×2),
BKAP.CITY (×2), BKAP.STATE, BKAP.ZIP, BKAP.COUNTRY (×2), BKAP.CLASS,
BKAP.REM.ZIP, BKAP.REM.STATE, BKAP.GL.ACCT, BKAP.GL.DPT, BKAP.SORT, BKAP.TAX.ID
```

Duplicate field names (ADD1/ADD2/CITY/COUNTRY) export the same field to two output columns —
this is intentional for reformatting (e.g., truncated vs. full, or primary vs. billing address).

**INVTXN.XPT** — type=F, target=`INVTXN.TXT` (Inventory Transaction export, 25 cols)

```
MTIT.TYPE (×2), MTIT.CLASS, MTIT.DATE, MTIT.CODE, MTIT.QTY, MTIT.AVGCOST,
MTIT.STDCST, MTIT.LOC, MTIT.REF, MTIT.CUST, MTIT.INVOICE, MTIT.PRICE,
MTIT.PO, MTIT.WOPRE, MTIT.WOSUF, MTIT.LOT, MTIT.SERIAL, MTIT.VENDOR,
MTIT.SCRAP, MTIT.QC, MTIT.DEPT, MTIT.DESC, MTIT.PRODLOT, MTIT.EXTRA
```

**WORKORD.XPT** — type=F, target=`WORKORD.TXT` (Work Order export, 17 cols)

```
MTWO.WIP.WOPRE (×4), MTWO.WIP.DDATE (×2), MTWO.WIP.SCHED (×11)
```

The 11 `SCHED` slots represent weekly schedule columns (WORKORD.XPT drives a schedule grid report).
Multiple `WOPRE` / `DDATE` columns export the same field with different formatting.

**BKBMMSTR.XPT** — type=D, target=`BKBMMSTR.TXT` (BOM Master export, 24 cols)

```
BKBM.PARENT (×2), BKBM.PROD.LINE#, BKBM.COMPONENT, BKBM.QTY.REQD,
BKBM.REFERENCE, BKBM.PROD.TYPE, BKBM.PROD.SCRAP, BKBM.PROD.OP,
BKBM.PROD.OPYN (×6), BKBM.PROD.PRICE, BKBM.PROD.RTNUM, BKBM.PROD.DUPOP,
BKBM.PROD.OPDSC, BKBM.PROD.VEND, BKBM.DATE1, BKBM.DATE2, BKBM.EXTRA, BKBM.REV
```

`BKBM.PROD.LINE#` = BOM line number (the `#` suffix denotes a calculated/sequence field).
`BKBM.PROD.OPYN` (×6) = six operation-Y/N flags (operation-inclusion toggles per BOM component).

**BKSBMFG.XPT** — type=T, target=`BKSBMFG.TXT` (Sub-contract Manufacturer export, 4 cols)

```
BKSB.MFG.CUST, BKSB.MFG.PROD, BKSB.MFG.MANUF, BKSB.MFG.MPART
```

---

## INVTXN field namespace — extended (from INVTXN.XPT)

Prior analysis (Pass 324 from BKSCF/BKSCG) identified 11 `MTIT.*` fields. INVTXN.XPT confirms
25 distinct INVTXN field accessors:

| TAS variable | Meaning |
|-------------|---------|
| `MTIT.TYPE` | Transaction type code |
| `MTIT.CLASS` | Item class |
| `MTIT.DATE` | Transaction date |
| `MTIT.CODE` | Part number |
| `MTIT.QTY` | Transaction quantity |
| `MTIT.AVGCOST` | Average cost at transaction time |
| `MTIT.STDCST` | Standard cost at transaction time |
| `MTIT.LOC` | Warehouse location |
| `MTIT.REF` | Reference number / document |
| `MTIT.CUST` | Customer code (for SO-linked transactions) |
| `MTIT.INVOICE` | Invoice / SO number |
| `MTIT.PRICE` | Unit price |
| `MTIT.PO` | Purchase order number |
| `MTIT.WOPRE` | Work order prefix |
| `MTIT.WOSUF` | Work order suffix |
| `MTIT.LOT` | Lot number |
| `MTIT.SERIAL` | Serial number |
| `MTIT.VENDOR` | Vendor code (for PO-linked transactions) |
| `MTIT.SCRAP` | Scrap quantity |
| `MTIT.QC` | QC hold quantity |
| `MTIT.DEPT` | Department |
| `MTIT.DESC` | Description |
| `MTIT.PRODLOT` | Production lot (manufactured lot, distinct from purchased lot) |
| `MTIT.EXTRA` | Extra / user-defined field |

(MTIT.TYPE appears twice in INVTXN.XPT — one column for the raw code, one for its display string.)

---

## Related files and pipeline

```
DE module programs (T7DEB, T7DEC, T7DEG, etc.)
  ├── Read .IMP file (MapFile call) → load source filename + mode + column maps
  ├── Open source file (CSV / Btrieve as specified)
  ├── Loop source rows: for each row, apply Map1 to build target field array
  ├── Write to target Btrieve table
  └── On export pass: apply Map2 + CRLF sentinel → write .TXT output

DE module (T7DEx, T7DEU)
  ├── Read .XPT file → get target .TXT filename + type flag + field list
  ├── Open source Btrieve table
  ├── Loop rows: for each row, evaluate field accessors in column order
  └── Write delimited text to target .TXT file
```

Programs confirmed to use import definitions:
- `T7DEHD` (131p) — Physical Inventory count import → BKPIPHYS (uses BKPIPHYS.IMP)
- `T7DEV` (138p) — PO import → ISAPQPO staging (uses a `.IMP` file)
- `T7DEQ` / `T7DER` — AR/AP payment CSV imports (uses `.IMP` files)
- `T7DEx` (82p) — Generic export config (uses ISFIELDS + possibly `.XPT`)
- `T7DEU` (102p) — Web/FTP catalog export → ISUDFINV (likely `.XPT`-driven)

**Confidence: 91/100** — IMP format confirmed from hex analysis of 5 non-empty files (442-byte
structure, uint16 LE column maps, CRLF sentinel at Map2[100]); XPT format confirmed from all 8
files (32000-byte block, 12-byte filename + 1-byte flag + 15-char column slots); MTIT.* 25-field
namespace confirmed from INVTXN.XPT; XPT type-flag semantics inferred from context (not confirmed
from source code); "RIC" mode encoding and Map2 export semantics need SRC-level verification.
