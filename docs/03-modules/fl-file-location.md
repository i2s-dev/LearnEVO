# FL — File Location Manager (WTASFLOC.RWN)

Status: verified | Pass 231 2026-06-23

Source: variable extraction from `samples/rwn_decrypted/WTASFLOC.RWN.dec` +
DFM read of `samples/dfm/WTASFLOC.DFM`

---

## Overview

`WTASFLOC.RWN` is the **FL module** — the TAS Pro 7 runtime **File Location Manager**.
It provides the "Maintain File Names and Locations" form used by system administrators to
manage the FILELOC routing table, which maps logical Btrieve file codes to physical disk
paths on the server.

- **Module code:** FL (File Location)
- **Program:** WTASFLOC.RWN (22 procs, 99 vars)
- **DFM caption:** "Maintain File Names and Locations"
- **Source library:** ISTS.SRC (ISTS custom extension)
- **Tables opened:** FILELOC + FILEDICT + FILEKEY + FILEKNUM + FILEDES + FILEDFLD +
  ERRMSG + FILEDBF + BKAPPOL + BKAPPO

---

## What It Does

Every time TAS Pro opens a Btrieve `.B` file, it consults the **FILELOC** table to
resolve the logical file code to a physical server path (and company-specific subfolder).
WTASFLOC is the administrative UI for managing that routing table — adding new files,
updating paths, and viewing the field dictionary (FILEDICT) for any registered file.

The program also exposes the **FILEDICT** field dictionary to the administrator,
allowing inspection of field names, offsets, types, and array dimensions for any
registered Btrieve table.

---

## UI Form (WTASFLOC.DFM)

| Control | Type | Purpose |
|---------|------|---------|
| `ceFileName` | TASComboEnter | File name selector (combo with lookup) |
| `entExt` | entry | Extension / file code input |
| `cbRecType` | combo | Record type selector |
| `entDesc` | entry | Description field |
| `cePath` | TASComboEnter | Physical path selector |
| `cbFDName` | combo | FD Name selector (field dictionary link) |
| `btnSave` | button | Save current record |
| `btnUpdate` | button | Update all (refresh all paths) |
| `btnDelete` | button | Delete current FILELOC entry |
| `btnExit` | button | Close form |

---

## Key Variable Namespaces

### CF_* — Current-File Selection (6 vars)

Used to identify which file is currently selected in the form. Read/write by any
program that presents a file-picker or navigates FILELOC.

| Variable | Meaning |
|----------|---------|
| `CF_FLNAME` | File name (logical name, e.g., `BKICMSTR`) |
| `CF_FLCODE` | Extension / file code (e.g., `.B`) |
| `CF_RTYPE` | Record type code |
| `CF_DESC` | Human-readable description |
| `CF_PATH` | Physical server path |
| `CF_FDNAME` | FD name — which FILEDICT definition to use |

### LOC_* — FILELOC Table Fields

Direct field access for the FILELOC routing table.

| Variable | Meaning |
|----------|---------|
| `LOC_BUFF_NAME` | Buffer/logical name |
| `LOC_FILE_NAME` | Actual filename on disk |
| `LOC_COMP_CODE` | Company code (multi-company routing) |
| `LOC_REC_SIZE` | Btrieve record size |
| `LOC_REC_TYPE` | Record type |
| `LOC_LOCATION` | Full physical path |
| `LOC_DESCRIPTION` | Description |
| `LOC_HNDL` | Open file handle |

### DICT_* — FILEDICT Field Dictionary (13 vars)

Mirrors the FILEDICT table — field-level metadata for any registered Btrieve file.

| Variable | Meaning |
|----------|---------|
| `DICT_BUFF_NAME` | Buffer/file this field belongs to |
| `DICT_FIELD_NAME` | Field name |
| `DICT_OFFSET` | Byte offset within the Btrieve record |
| `DICT_TYPE` | Field data type |
| `DICT_SIZE` | Field size in bytes |
| `DICT_DEC` | Decimal places (for numeric) |
| `DICT_ARRAY_ELE` | Array element count (for array fields) |
| `DICT_UPCASE` | Uppercase flag |
| `DICT_DESC` | Human-readable field description |
| `DICT_PICTURE` | Display picture/mask |
| `DICT_HOFFSET` | Header offset (display positioning) |
| `DICT_HTYPE` | Header type |
| `DICT_HSIZE` | Header size |
| `DICT_HDEC` | Header decimal places |
| `DICT_HARRAY` | Header array count |

### File Handle Variables

| Variable | Meaning |
|----------|---------|
| `KEY_HNDL` | Open handle to FILEKEY table |
| `KNUM_HNDL` | Open handle to FILEKNUM table |
| `ARET` | Return value from sub-form calls |
| `FLLKUPFORMNAME` | Form name for the file-lookup result display |
| `UPDFORMNAME` | Form name for update sub-dialog |
| `RECCNTR` | Record counter |

---

## TAS Pro 7 Internal File Tables

WTASFLOC manages tables that are **TAS runtime internals** — not in the Pervasive DDF:

| Table | Physical file | Purpose |
|-------|--------------|---------|
| `FILELOC` | `FILELOC.UPD` | Maps logical file codes → physical paths (per company + location) |
| `FILEDICT` | `FILEDICT.UPD` | Field dictionary: name/offset/type/size for every registered field |
| `FILEKEY` | `FILEKEY.UPD` | Key definitions for each registered Btrieve file |
| `FILEKNUM` | `FILEKNUM.UPD` | Key number assignments |
| `FILEDES` | `FILEDES.UPD` | File descriptor — record-level metadata for creating `.B` files |
| `FILEDFLD` | `FILEDFLD.UPD` | File default field values |
| `FILEDBF` | — | dBASE format file registry |
| `ERRMSG` | `errmsg.dbf` | TAS runtime error messages (dBASE format) |
| `FILES` | `FILES.UPD` | Master list of registered Btrieve tables |
| `FILEREL` | `FILEREL.UPD` | FK relationships within the FILE* system |
| `FILEDEF` | `FILEDEF.UPD` | File definitions / character-set validation data |
| `FILECHSP` | `FILECHSP.UPD` | Character set page mapping (printer type codes) |

These tables are **live runtime lookup tables** (not just migration artifacts). Every TAS Pro
program that opens a Btrieve file calls FILELOC at runtime to resolve the physical path.
EvoUpdate also reads/writes them during schema migrations.

---

## Binary Analysis of FILE*.UPD (Pass 409, 2026-06-30)

All FILE*.UPD files are **Btrieve data files** (FC magic `46 43`, 4096-byte pages), stored in
`\\i2s109-solidcrm\DBAMFG$\`. They are not in the Pervasive DDF — TAS Pro accesses them directly.

### FILELOC.UPD — Table-to-File Location Routing

- **1,352 records** = 340 unique logical tables × 2 location codes × duplicates
- **Location codes**: `DEFAULT` (production data) and `TESTDATA` (test/training mode)
- Every table has both a production and test path — EvoERP has built-in test-mode support
- **304 tables have a physical file name different from their logical name** (aliases)
- Example aliases:
  - `BKAPVEND` (logical) → `BKAPEVND` (production physical file)
  - `BKAPDESC` (logical) → maps to 16+ physical files: `BKARDESC`, `BKGLDESC`, `BKSONOTE`, `ISRMADSC`, etc.
- **Template tables**: `BKAPDESC`, `BKAPPOL`, etc. define a shared schema used by multiple
  physical files across modules (e.g., every module's notes/description table uses BKAPDESC's schema)
- Extracted CSV: `samples/fileloc_mappings.csv` (1,352 rows)

### FILEDICT.UPD — EvoERP Field Dictionary (4 MB)

- **3,265 unique (table, field_path) pairs** across **370 tables**
- Field paths use TAS Pro dot notation: `TABLE_ALIAS.FIELD_NAME` or `TABLE_ALIAS.SUB.FIELD` 
- Record format: `[table_name: 8 bytes, space-padded][field_path: variable-length ASCII]`
- Extracted CSV: `samples/filedict_fields.csv` (3,265 rows)

Top tables by field count:

| Table | Fields | Module |
|-------|--------|--------|
| BKPRMSTR | 47 | Payroll master |
| BKSYMSTR | 41 | System config master |
| BKICMSTR | 34 | Inventory item master |
| WOROUT | 33 | WO routing output |
| BKPRGLFL | 33 | Payroll GL files |
| BKAPPO | 32 | AP Purchase Order |
| WORKORD | 32 | Work Order header |
| BKARINV | 29 | AR Invoice header |
| BKARCUST | 27 | AR Customer master |
| ROUTING | 27 | WO Routing template |

Security fields (AHSYLOG table):
- `AHSY.USER.ACCES` — module access flags (AHSY_USER_ACCES)
- `AHSY.USER.CTRL` — control flags
- `AHSY.USER.KEY` — user record key
- `AHSY.USER.LEVL` — security level
- `AHSY.USER.MENU` — menu access mask
- `AHSY.USER.PKEYS` — password keys

Description template fields (BKAPDESC logical schema):
- `BK.DESC.CODE`, `BK.DESC.DESC`, `BK.DESC.KEY`, `BK.DESC.KEY2`, `BK.DESC.LINE`, `BK.DESC.NOTES`, `BK.DESC.NUM`

### FILES.UPD — Master Table Registry (72 KB)

Contains the master list of registered Btrieve tables. The BKCM* series tables are registered
here and are **not in the Pervasive DDF** — they form EvoERP's Company Master add-on module:
`BKCMACCC`, `BKCMACCL`, `BKCMACCN`, `BKCMACCT`, `BKCMACFC`, `BKCMACTD`, `BKCMACTF`,
`BKCMACTH`, `BKCMCNTD`, `BKCMDE`, `BKCMDTCD`, `BKCMDUN`, `BKCMDUNH`, `BKCMEACC`,
`BKCMEACD`, `BKCMEACF`, `BKCMEACH`, `BKCMEACT`, `BKCMFORM`, `BKCMHCOD`, `BKCMLEAD`,
`BKCMMHST`, `BKCMPCFC`, `BKCMPCNT`, `BKCMPCTF`, `BKCMPCTH`, `BKCMREP`, `BKCMSBDF`,
`BKCMTERR`, `BKCMVNDF`, `BKCMVNDH`, `BKCMVNFC`, `BKICPMAT`, `DISCOUNT`

### FILEREL.UPD — Table Relationships (72 KB)

Only 2 real relationship records — both link tables within the FILE* system itself:
- `FILEDICT.DICT_BUFF_NAME` → `FILELOC.LOC_BUFF_NAME`
- `FILEKNUM.KNUM_BUFF_NAME` → `FILELOC.LOC_BUFF_NAME`

Main EvoERP table FK relationships are **not** stored here — they are enforced procedurally
by TAS Pro program logic (confirmed: no FK data in FILEREL for production BK*/IS* tables).

### evo.upd (3 bytes)

Contains ASCII `"1\r\n"` — a version marker only.

---

## Access Entry Points

This program is reached via:
- Menu code: not yet confirmed (likely under TA — System Admin)
- Called from: WTASDATAM, WTASDMGR, WTASINIT, T7DDCHECK (all FILE* table management programs)
- From `FLLKUPFORMNAME` var: other programs can call WTASFLOC as a sub-picker dialog

---

## Notes

- The `BKAPPOL` + `BKAPPO` in the DB fingerprint shows FL can also navigate to
  PO-related records — likely for lookup integration (F3 drill-down).
- WTASFLOC is distinct from WTASINIT (which *creates* new FILELOC entries) and T7FNR
  (which *browses* FILEDICT for a specific file). WTASFLOC is the *maintenance* UI.
- The DFM `cePath` combo uses `TASComboEnter` — meaning it does a runtime FILELOC
  lookup to populate the path list (it reads FILELOC to show where files currently are).

**Confidence: 92/100** — DFM + RWN vars fully confirmed; binary analysis of all FILE*.UPD
files complete (Pass 409, 2026-06-30); 3,265 field-path pairs extracted from FILEDICT; 1,352
FILELOC routing records extracted; template-table architecture confirmed. Remaining gap:
FILEKEY/FILEKNUM record structure not fully decoded; FILEDFLD purpose unclear.
