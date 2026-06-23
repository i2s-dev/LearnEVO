# SU — Setup / UI Configuration

Status: partial | Pass 232

EvoERP module code: **SU**

CHM-confirmed operations:
- SU-A: Maintain Grid Lookups (`WBKLUGRID.RWN`)
- SU-B: Maintain Drill Down Menus (`EvoERPDrillM.RWN`)
- SU-C: Forms Editor (RWN not yet matched)
- SU-D: Grid Maintenance (`T7gdm.RWN`)

---

## SU-A: Maintain Grid Lookups — WBKLUGRID.RWN

**68 procs | ISTECH.LIB | 75 DB tables**

WBKLUGRID is the configuration manager for the grid lookup system used throughout EvoERP. It manages records in the `BKLUGRID` table, which defines which columns appear in every lookup/browse grid and how they behave.

### LUGRID_* Namespace — BKLUGRID field access (13 vars)

| Var | Field | Notes |
|-----|-------|-------|
| LUGRID_NAME | NAME | Grid config name (primary key) |
| LUGRID_DATA | DATA | Serialized column data |
| LUGRID_FDNAME | FDNAME | Field definition name reference |
| LUGRID_KDATA | KDATA | Key data block |
| LUGRID_END | END | End marker / record delimiter |
| LUGRID_FORM | FORM | Associated form program |
| LUGRID_PROT | PROT | Protected (read-only) flag |
| LUGRID_DELFLAG | DELFLAG | Deletion flag |
| LUGRID_TEXT | TEXT | Display label / description |
| LUGRID_KEYFLD | KEYFLD | Key field reference |
| LUGRID_EXTRA | EXTRA | Extra/overflow data |
| LUGRID_EXTUDF | EXTUDF | Extended UDF data |
| LUGRID_EXTPARM | EXTPARM | Extended parameters |

### FD_* — Column field definition vars (per-column metadata)

| Var | Meaning |
|-----|---------|
| FD_COLHEADER | Column header label |
| FD_FIELDNAME | Source field name (from FILEDICT) |
| FD_TOT | Totaling flag (Y/N) |
| FD_SSSFD | Sub-sort/sub-select field |
| FD_FUNC | Aggregate function |
| FD_TYPE | Data type code |
| FD_SIZE | Display width |
| FD_EDIT | Edit mask |

### KD_* — Key definition vars

| Var | Meaning |
|-----|---------|
| KD_COLHEADER | Key column header |
| KD_KEYNAME | Key name (from FILEKNUM) |
| KD_FIELDNAME | Key field name |

### Supporting vars

| Var | Meaning |
|-----|---------|
| KEYFLD1 / KEYFLD2 / KEYFLD3 | Up to 3-part compound key support |
| EXTPARAM1-4 | Extended parameter slots |
| SEC.LEVEL | Security level filter |
| NUM_FIELDS | Field count |
| FD_CNTR / FD_ACTIVE | Field iterator counter / active column |
| KD_CNTR / KD_ACTIVE | Key iterator counter / active key |
| ACTIVE_RECORD / ACTIVE_COPY / NEW_RECORD | Record operation flags |
| GET_KEY_NAME | Key name lookup var |
| ONDISP | On-display trigger |
| EVOPRG | Calling program name |

### Handles

- `LUGRID_HNDL` — BKLUGRID file handle
- `DICT_HNDL` — FILEDICT (field dictionary) handle
- `KNUM_HNDL` — FILEKNUM (key definition) handle

### Database tables (75 total)

The 75-table fingerprint reflects all tables that WBKLUGRID can configure grid lookups for (including every module's browseable table). The program reads FILELOC (via LOC_*) to enumerate all configured file locations.

LOC_* vars mirror the WTASFLOC/T7ALOGSETUP pattern: `LOC_BUFF_NAME`, `LOC_FILE_NAME`, `LOC_COMP_CODE`, `LOC_REC_SIZE`, `LOC_REC_TYPE`, `LOC_LOCATION`.

---

## SU-B: Maintain Drill Down Menus — EvoERPDrillM.RWN

**31 procs | ISTECH.LIB | 10 DB tables**

EvoERPDrillM manages records in `ISDRILLM`, the drill-down menu configuration table. Each record defines a parent→child relationship: when a user "drills down" from a record in one program, EVO looks up the ISDRILLM entry to find which child program to launch and how to pass the key.

### DRILLM.* Namespace — ISDRILLM field access (9 vars)

| Var | Field | Meaning |
|-----|-------|---------|
| DRILLM.PARENT | PARENT | Parent program/menu code |
| DRILLM.CHILD | CHILD | Child program/menu code to launch |
| DRILLM.MENU | MENU | Menu entry identifier |
| DRILLM.FILE | FILE | Source table name |
| DRILLM.SFIELD | SFIELD | Source key field (from parent) |
| DRILLM.TFIELD | TFIELD | Target key field (in child) |
| DRILLM.KEY | KEY | Key value to pass |
| DRILLM.PFILE | PFILE | Parent file reference |
| DRILLM.EXTAR | EXTAR | Extra/extended arguments |

### Supporting handles

- `LUGRID_HNDL` — grid display handle (BKLUGRID)
- `DICT_HNDL` — FILEDICT handle (confirms LOC_*/DICT_* pattern shared with WTASFLOC)
- `KNUM_HNDL` — FILEKNUM handle
- `KEY_HNDL` — FILEKEY handle
- `DRILLM.H` — ISDRILLM record handle

### DICT_* vars (FILEDICT field dictionary — 13 vars)

Same namespace as WTASFLOC and WBKLUGRID:
`DICT_BUFF_NAME/FIELD_NAME/OFFSET/TYPE/SIZE/DEC/ARRAY_ELE/UPCASE/DESC/PICTURE/LCD` + 2 additional metadata vars.

These cross-confirm that SU-B reads the full data dictionary at runtime to resolve field names for drill-down key mapping.

---

## SU-D: Grid Maintenance — T7gdm.RWN

**31 procs | NZLICE.LIB | 7 DB tables**

T7gdm is the Grid Data Maintenance utility — it copies, imports, and exports grid lookup configurations between workstations or datasets. It is the admin tool for bulk grid config management.

### Operation mode flags

| Var | Meaning |
|-----|---------|
| SKIP | Skip existing records (no overwrite) |
| REPLACE | Replace/update existing records |
| OVERWRITE | Overwrite all (unconditional) |

These three flags control how T7gdm handles conflicts when copying grid configs between sources.

### Grid record identifiers

| Var | Meaning |
|-----|---------|
| GNAME | Grid config name |
| GDATE | Grid config date |
| CDATE | Copy date |
| GBUFF | Grid config record buffer |

### Drill-down record identifiers

| Var | Meaning |
|-----|---------|
| DPNAME | Drill-down parent name |
| DCNAME | Drill-down child name |
| DDATE | Drill-down record date |
| DBUFF | Drill-down record buffer |

### Count vars

| Var | Meaning |
|-----|---------|
| TNOR | Total count — normal records |
| TPR | Total count — preferred records |

### Handles

- `ISTECHLUG.H` / `LUG.H` — BKLUGRID handles (source / target)
- `ISTECHDM.H` / `DM.H` — ISDRILLM handles (source / target)

The dual handle pattern confirms T7gdm works with two open connections simultaneously (source dataset and target dataset) during copy operations.

---

## SU-C: Forms Editor — RWN not matched

The CHM documents SU-C as "Forms Editor" but no RWN file for this operation has been identified yet. Candidate: `WEVOFORMS.RWN` or similar. Open question in `research/OPEN_QUESTIONS.md`.

---

## Key tables

| Table | Purpose |
|-------|---------|
| BKLUGRID | Grid lookup configuration — one record per named grid (NAME = key) |
| ISDRILLM | Drill-down menu configuration — parent→child launch mappings |
| FILELOC | File location routing — enumerated by WBKLUGRID to find all tables |
| FILEDICT | Field dictionary — resolved at runtime by WBKLUGRID/EvoERPDrillM |
| FILEKNUM | Key number definitions — resolved by WBKLUGRID |

---

## Confidence notes

- LUGRID_* 13-var namespace: **confirmed** from WBKLUGRID var extraction (Pass 232)
- DRILLM.* 9-var namespace: **confirmed** from EvoERPDrillM var extraction (Pass 232)
- T7gdm SKIP/REPLACE/OVERWRITE: **confirmed** from var extraction (Pass 232)
- SU-C Forms Editor RWN: **unknown** — CHM-confirmed operation, RWN not yet matched
- 75-table fingerprint in WBKLUGRID: **confirmed** from DB file table (Pass 65 + Pass 232)
