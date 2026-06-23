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

| Table | Purpose |
|-------|---------|
| `FILELOC` | Maps logical file codes → physical paths (per company) |
| `FILEDICT` | Field dictionary: name/offset/type/size for every field |
| `FILEKEY` | Key definitions for each registered Btrieve file |
| `FILEKNUM` | Key number assignments |
| `FILEDES` | File descriptor — template for creating new `.B` files |
| `FILEDFLD` | File default field values |
| `FILEDBF` | dBASE format file registry |
| `ERRMSG` | TAS runtime error messages |

These 8 tables appear in hundreds of EvoERP programs because every program that performs
dynamic record navigation or file-open calls links to the FILELOC routing layer.

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

**Confidence: 80/100** — DFM fully read; var-level confirmed from decrypted RWN. Proc
names extracted but not analyzed individually. BKAPPOL/BKAPPO cross-link purpose inferred.
