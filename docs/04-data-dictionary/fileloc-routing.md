# FILELOC — File Routing Table

Status: verified (Pass 388, 2026-06-29 — live fileloc.dbf parsed; FILELOC.B binary confirmed)

Source: `samples/FILELOC.B` (Btrieve, 2,793,472 bytes, copied from `\\i2s109-solidcrm\DBAMFG$\FILELOC.B`)
Also: `samples/fileloc.dbf` (dBASE III+ equivalent, 972 KB, 4,461 records including deleted/temp)

---

## Purpose

FILELOC is EvoERP's **file routing table** — the central registry that tells `tp7runtime.exe`
where each Btrieve data file lives on disk and how logical buffer names map to physical
filenames. It is opened by **831 of 1,122 programs** (74%).

When a TAS Pro 7 program executes `open BKAPCHKF lock W`, the runtime looks up `BKAPCHKF` in
FILELOC to find:
- Which physical file to open (may differ from the buffer name)
- Which company-specific extension/subdirectory to use
- Whether the file is Btrieve (`.B*`) or CodeBase/dBASE

**Important:** FILELOC does NOT contain RTM report paths. RTM files are located directly
via hardcoded paths or ISTS.CFG configuration keys.

---

## Schema (fileloc.dbf / FILELOC.B)

| Field | Type | Size | Description |
|-------|------|------|-------------|
| `LOC_BUFF_N` | C | 8 | Logical buffer name — what TAS programs name in `open TABLE` |
| `LOC_FILE_N` | C | 32 | Physical filename — actual file opened (often = LOC_BUFF_N) |
| `LOC_COMP_C` | C | 3 | Company/context code (see table below) |
| `LOC_REC_SI` | N | 5 | Record size in bytes |
| `LOC_REC_TY` | C | 1 | Record type: `B`=Btrieve, `C`=CodeBase/dBASE, `F`=Overlay |
| `LOC_LOCATI` | C | 128 | Subdirectory path within `DBAMFG$\` (e.g., `I2\`, `DEFAULT\`) |
| `LOC_DESCRI` | C | 40 | Description (usually blank in live data) |

---

## Company Codes (LOC_COMP_C)

| Code | Meaning |
|------|---------|
| `B` | Default company (no suffix; uses `DEFAULT\` directory) |
| `BI2` | Company I2 — i2 Systems main data (directory `I2\`) |
| `BAT` | Company AT (directory `AT\`) |
| `BAB` | Company AB (directory `AB\`) |
| `BCA` | Company CA (directory `CA\`) |
| `B99` | Company 99 — test data (directory `TESTDATA\`) |
| `TMP` | Temporary migration tables (timestamped names like `TBKAPPOL20251217085516`) |
| `OVL` | Overlay file (type F; used only for TASCOLOR.OVL) |
| `C` | CodeBase/dBASE format (DDF infrastructure files + BKMENUSU + ERRMSG) |
| `DDF` | DDF-specific routing entries |
| `XFR` | Transfer/migration source files |

---

## Record Type Codes (LOC_REC_TY)

| Type | Count | Meaning |
|------|-------|---------|
| `B` | 4,419 | Btrieve `.B*` file (main data engine) |
| `C` | 15 | CodeBase/dBASE `.DBF` file (DDF tables + menu + errmsg) |
| `F` | 1 | Overlay file (TASCOLOR.OVL only) |

---

## Directory Locations

All paths are relative to `\\i2s109-solidcrm\DBAMFG$\`.

| LOC_LOCATI | Full path | Usage |
|------------|-----------|-------|
| `DEFAULT\` | `DBAMFG$\DEFAULT\` | Non-company-specific files |
| `I2\` | `DBAMFG$\I2\` | Company I2 (active) |
| `AT\` | `DBAMFG$\AT\` | Company AT (active) |
| `AB\` | `DBAMFG$\AB\` | Company AB (active) |
| `CA\` | `DBAMFG$\CA\` | Company CA (active) |
| `TESTDATA\` | `DBAMFG$\TESTDATA\` | Company 99 test data |
| `DRILL\` | `DBAMFG$\DRILL\` | Drill/demo data |
| *(blank)* | `DBAMFG$\` | Root-level DDF/infrastructure files |

---

## Statistics

- **401 unique logical buffer names** (primary table handles)
- **863 unique physical file names** (including all aliases)
- **4,419 Btrieve records** (401 tables × ~6 companies + aliases per company)
- **123 buffer names** have at least one physical alias different from the buffer name
- **T* temp files**: ~100+ timestamped migration temp tables visible (e.g., `TINVTXN20261015023916`)

---

## Key Buffer-to-Alias Mappings

The most important alias groups — each shows a logical buffer name and all the
physical files it can route to:

### BKAPDESC (21 aliases — shared "description lines" buffer)
TAS programs open `BKAPDESC` and FILELOC routes them to the correct BK_DESC table:
`BKAPADSC`, `BKAPHDSC`, `BKARDESC`, `BKARDPST`, `BKARHDSC`, `BKARRDSC`,
`BKGLDESC`, `BKQTNOTE`, `BKQTTEMP`, `BKRFQDES`, `BKSONOTE`, `ISARADSC`,
`ISARAHDS`, `ISRFQADS`, `ISRMADSC`, `ISRMDESC`, `ISSRADSC`, `ISSRDESC`,
`ISWODESC`, `ISWOHDSC`, `NOTETEMP`

### BKARINV (26 aliases — invoice header, polymorphic)
`BKARHINV`, `BKARRINV`, `BKEDIH`, `BKESTQT`, `ISARAHIN`, `ISARAINV`,
`ISECIH`, `ISESAHDR`, `ISESTAQT`, `ISESTHDR`, `ISRMAINV`, `ISRMINV`,
`ISSEDH`, `ISSESH`, `ISSNINV`, `ISSQTH`, `ISSRAINV`, `ISSRCH`, `ISSRINV`,
`ISSRMH`, `ISSRMINV`, `ISSSOH`, `ISSSRH`, (+ 3 migration temps)

### BKARINVL (30 aliases — invoice lines)
`BKARHIVL`, `BKARRIVL`, `BKARSIVL`, `BKEDIL`, `BKESTQTL`, `ISARAHIL`,
`ISARAIVL`, `ISECIL`, `ISESALNE`, `ISESTAQL`, `ISESTLNE`, `ISRMAIVL`,
`ISRMINVL`, `ISSEDL`, `ISSESL`, `ISSNINVL`, `ISSQTL`, `ISSRAIVL`,
`ISSRCL`, `ISSRINVL`, `ISSRMIVL`, `ISSRML`, `ISSSOL`, `ISSSRL`,
(+ 6 migration temps)

### BKARTXN (18 aliases — AR transaction/lot/serial)
Routes to: `BKARTXNB`, `BKARTXNS`, `BKSOHLOT`, `BKSOHSER`, `ISARATXN`,
`ISARATXS`, `ISRMATXN`, `ISRMATXS`, `ISRMTXN`, `ISRMTXNS`, `ISSNTXN`,
`ISSNTXNS`, `ISSOALOT`, `ISSOASER`, `ISSRATXN`, `ISSRATXS`, `ISSRTXN`, `ISSRTXNS`

### INVTXN (28 aliases — inventory transactions, heavily migrated)
`INVATXN`, `INVETXN`, `ISBTXFER`, (+ 25 migration temp tables from 2024–2026)

### BKBMMSTR (39 aliases — BOM master, most-migrated table)
`BKBMAMTR`, `BKBMARC`, `BKBMAVAL`, `BKBMEMTR`, `BKBMSUMM`,
`ISBMESA`, `ISBMEST`, `ISBMTMP`, `ISMYBOM`, (+ 30 migration temps)

### ISSRINFO (15 aliases — service record info, polymorphic)
`ISBTCSB`, `ISECINFO`, `ISEDINFO`, `ISESINFO`, `ISICINFO`, `ISQTINFO`,
`ISRMAINF`, `ISRMHINF`, `ISRMINFO`, `ISSOAINF`, `ISSOHINF`, `ISSOINFO`,
`ISSRAINF`, `ISSRHINF` (all are context-specific views of the same record structure)

### Other notable alias groups
- `BKAPCHKF` → `BKAPCHKH` (history), `BKARCHKF/H` (AR version), `ISAPACHK/ISARACHK` (archived)
- `BKCMTEMP` → `BKCMTMP1/2/3/4` (4 parallel company-merge temp slots)
- `BKCMCTRL` → `BKCMCTL1/2/3/4` (company control, 4 slots)
- `CLASMSTR` → `CUSTCLAS`, `VENDCLAS`, `ISFSMARK` (same table, 3 logical uses)
- `ROUTING` → `BKRTEMTR`, `ISRTESA`, `ISRTEST`, `ROUTAING`, `ROUTTEMP`
- `WORKORD` → `WORKHORD`, `WORKSORD`, (+ 4 migration temps)
- `MTICMSTR` → `MTICAMTR`, `MTICEMTR`, `MTINVDEF`, `ISMICADT`, `ISMICESA`, `ISMICEST`, `ISMICSTD`
- `LOT` → `ISALOT` (archived lots)
- `SERIAL` → `SERIALH` (serial history)
- `ISSERIAL` → `ISHLOTS`, `ISHSERIA`, `ISLOTS` (lot/serial by handle context)
- `ISNCR` → `ISACAR`, `ISANCR`, `ISCAR` (NCR context aliases)

---

## CodeBase (dBASE) Entries

The 15 type-C entries are the DDF infrastructure files and shared utilities:

| Buffer Name | Physical File | Purpose |
|-------------|--------------|---------|
| FILEDBF | FILEDBF / XFR_FILEDBF | DDF file registry |
| FILEDES | FILEDES | DDF file descriptions |
| FILEDFLD | FILEDFLD | DDF field definitions |
| FILEDICT | FILEDICT / XFR_FILEDICT | DDF file dictionary |
| FILEKEY | FILEKEY / XFR_FILEKEY | DDF key definitions |
| FILEKNUM | FILEKNUM | DDF key numbering |
| FILELOC | FILELOC / XFR_FILELOC | Routing table (self-referential) |
| ERRMSG | ERRMSG | TAS runtime error messages |
| BKMENUSU | BKMENUSU | EvoERP menu structure |
| WTASFMGR | WTASFMGR | TAS file manager |

---

## TAS Variable Names for FILELOC

```
FILELOC.H     — FILELOC file handle (in startup/menu programs)
SFILELOC.H    — shared FILELOC handle (passed between programs)
FILELOC_HNDL  — alternate handle name
FILELOC.NAMES — comma-delimited file name list
FL.FILE       — current buffer name field value
FL.ITEM       — current physical file name field value
FL.NEXTOK     — flag: next sequential record available
FL.CNTR       — iteration counter
FL.PCT        — progress percentage
```

---

## How RTM Files Are Located (corrects earlier assumption)

**FILELOC does NOT contain RTM report file paths.** RTM file location works via:
1. **ISRTMS table** (29 fields, per-customer/vendor/item label routing) — routes label RTMs per printer
2. **RTMVLD_\* library** (used by 327 programs) — validates RTM file existence; RTM paths come from ISTS.CFG keys or are hardcoded
3. **ISTS.CFG.RTM.\*** config keys in BKYSMSTR — store default RTM paths per module/report type
4. **Direct pool strings** in RWN bytecode — many programs have the RTM filename embedded as a string constant in the pool section

---

## See Also

- [overview.md](overview.md) — Btrieve/DDF architecture overview
- [primary-keys.md](primary-keys.md) — primary key definitions for all 659 tables
- [file-names-index.md](file-names-index.md) — logical table name index
- [docs/01-architecture/system-overview.md](../01-architecture/overview.md) — multi-company architecture
