# TAS Pro 7 Data Infrastructure Modules
Status: verified | C:90/100 — procedure names from SRC-compiled RWN files, 2026-06-16

These modules are part of the TAS Pro 7 runtime's data management layer — not EvoERP
business logic, but the tooling that EvoERP uses to manage its Btrieve file dictionary
and perform low-level database administration.

All data is from `scripts/rwn_extract_symbols.py` applied to locally-copied RWN files.

---

## Module inventory

| Module file | Source | Procs | Vars | Purpose |
|-------------|--------|-------|------|---------|
| `wtasdmgr.RWN` | wtasdmgr.SRC | 68 | 229 | Data dictionary manager — define/edit file schemas |
| `wtasdatam.RWN` | wtasdatam.SRC | 59 | 176 | Generic record browser/editor for any TAS-managed file |
| `wtasinit.RWN` | wtasinit.SRC | 21 | 153 | File creation and initialization |
| `winit.RWN` | winit.SRC | 21 | 152 | Older file initialization (pre-WTASINIT) |
| `wtascvtdict.RWN` | wtascvtdict.SRC | 13 | 244 | Dictionary format conversion utility |
| `wtascvtdictpr.RWN` | wtascvtdictpr.SRC | 12 | 243 | Dictionary conversion — print/report variant |
| `wtaschkint.RWN` | wtaschkint.SRC | 8 | 128 | Dictionary integrity checker |
| `wtasmerge.RWN` | Wtasmerge.SRC | 16 | 182 | Dictionary merge (combine two dict sets) |
| `wtasfloc.RWN` | wtasfloc.SRC | 22 | 99 | File location manager |

---

## TAS-internal meta-tables (FILEDICT system)

These five tables are the TAS Pro 7 internal data dictionary — they describe every
Btrieve `.B` file that TAS manages. They appear as DB files in all the infrastructure
modules above and are distinct from the EvoERP business tables.

| Table name | Purpose |
|-----------|---------|
| `FILELOC` | File locations — maps logical file names to physical paths and company codes |
| `FILEDICT` | Field dictionary — one record per field per file; stores name, type, size, decimals |
| `FILEKEY` | Key definitions — which fields make up each index key |
| `FILEKNUM` | Key number index — counts and ordering of keys per file |
| `FILEDES` | File description / extended metadata |
| `FILEDFLD` | DBF-era field definitions (older format, used by wtascvtdict during conversion) |
| `FILEDBF` | DBF file registry (older format) |

---

## WTASDMGR — Data Dictionary Manager

**File:** `wtasdmgr.RWN` (wtasdmgr.SRC, 68 procedures)

The admin UI for creating and editing the TAS Pro file dictionary. This is how a TAS
developer defines new `.B` file schemas or modifies existing ones.

**Procedure groups:**

| Category | Procedures |
|----------|-----------|
| Init | `OPENFILES`, `START`, `FDSTART`, `RFSTART` |
| Navigation | `PCMAIN.CHANGE`, `SETUP_GRIDS`, `SETUPDROPDOWN`, `SET_LIST_ARYS` |
| Field entry | `TYPE.POST`, `SIZE.PRE`, `ARRAYELEMENTS.PRE`, `UPPERCASE.PRE`, `DECCHRS.PRE` |
| Key management | `SETUP_SEGMENTFIELDNAME`, `SETUPKEYSPEC`, `SETUPKEYSEG`, `CBKEYNAME.PRE/VALID`, `DGKEYSPEC.MOVE`, `BTNKEYSAVE/EDIT/NEW/DELETE/REFRESH.CLICK` |
| Grid events | `DGFIELDS.INSERT`, `DGFIELDS.ADD` |
| Toolbar CRUD | `TBEDIT/NEW/SAVE/CLOSE/DELETE.CLICK` |
| Menu actions | `MLEDIT/SAVE/CLOSE/DELETE.CLICK`, `MLEDITFILELOCS/CREATFILE/REINDEXFILE/REINDEXCBFILE/RESTRUCFILE.CLICK` |
| Validation | `LONGNAMEVLD`, `SHORTNAMEVLD`, `VLDCBFILELAYOUT`, `VLDCBKEYNAME`, `SNCHKFORDUP` |
| Restructure | `RESETRESTRUCT`, `BTNRFPROCEED.CLICK` |
| Print/Export | `MLPRINT/PRINTFILELOCS.CLICK`, `BTNEXPORT.CLICK`, `GET_PATHS` |
| Help | `SET_HELPFILE`, `TBHELP.CLICK`, `BTNMOREHELP.CLICK` |

**Key variable names:** `FLD_LIST`, `FLD_LNAME/SNAME/TYPE/SIZE/DEC/ARRAY/UPCASE/DESC`,
`AKEY_LIST`, `AKEY_NAME`, `SEG_FLD_NAME`, `KORD/KMOD/KDUP/KIGNORE`, `NUMSEG`,
`AFILE_NAME/EXT/TYPE/PATH/DESC`, `LAYOUT_NAME`, `RESTRUCTFDNAME`, `DPATH_RPT`

**Summary:** Provides the full CRUD UI for file/field/key definitions stored in
FILELOC + FILEDICT + FILEKEY + FILEKNUM. The "Restructure File" workflow
(`RFSTART` → `RESETRESTRUCT` → `BTNRFPROCEED.CLICK`) handles schema changes
that require Btrieve file reconstruction.

---

## WTASDATAM — Generic Record Browser

**File:** `wtasdatam.RWN` (wtasdatam.SRC, 59 procedures)

A universal data browsing and editing tool. Given any file name registered in FILELOC,
it opens that `.B` file and displays its records in a data grid. Used by EVO developers
for direct table inspection and ad-hoc editing.

**Procedure groups:**

| Category | Procedures |
|----------|-----------|
| Lifecycle | `ONOPEN`, `ONCLOSE`, `FILEOPEN`, `MNIEXIT/BTNEXIT.CLICK` |
| Display | `SETUPTEMPLATE`, `SETUPFASTSEARCH`, `TESTLASTCOL`, `DISPLAYARRAY`, `DISPARRAYFORM`, `DISPLAYMEMO` |
| Navigation | `CBKEYS.CHANGE`, `FASTNUM.CHANGE`, `DGRECORDS.MOVE` |
| Edit mode | `CBEDIT.CLICK`, `SWITCH_EDIT`, `SWITCH_EDIT2`, `MNIEDITMODE.CLICK`, `CBNOKEY.CLICK` |
| Grid CRUD | `DGRECORDS.SAVE/INSERT/ADD/DISPLAY/DELETE`, `NAVRECORDS.SAVE/DELETE` |
| Row actions | `BTNADDROW/SAVEROW/DELREC.CLICK` |
| Filter | `MNIFILTER.CLICK`, `ENTER_FILTER`, `CHKFILTER`, `MNIREDISPLAY/REDISPLAYCURRENT/REFRESH.CLICK` |
| Find | `MNIFIND.CLICK`, `FINDFILTER` |
| File lookup | `CEFILENAME.CLICK/PRE/POST`, `VLDCEFILENAME`, `FLLKUPSTART`, `DGFILELOCLU.SELECT` |
| Memo | `SETUPMEMOFORM`, `DISPMEMOFORM` |
| Export | `BTNEXPORT/EXPORTALL.CLICK` |
| Lock handling | `REC_LOCKED` |

**Key variable names:** `CBINDEXNAME`, `NOKEY`, `GOEDITING`, `REC_NUM`, `CURR_REC_NUM`,
`ENTFILENAME`, `PATH_NAME`, `DEL_NUM`, `ARRAYCNTR`, `FILTEREXPR`, `FINDFILTEREXPR`,
`FILE_HNDL`, `LOC_HNDL`, `DICT_HNDL`, `KNUM_HNDL`, `KEY_HNDL`,
`MEMOFLDARRAY`, `MEMOFLD`, `MEMOFLDCNTR`, `USEFILTER`, `FILTEREXPRPTR`

**Summary:** Essentially a database browser for any TAS-managed file. Supports multiple
index keys (CBKEYS dropdown), filter expressions (MNIFILTER), fast numeric search
(FASTNUM), memo field display, array field display, and export. The `REC_LOCKED`
handler deals with Btrieve record locking for concurrent users.

---

## WTASINIT / WINIT — File Creation

**Files:** `wtasinit.RWN` (wtasinit.SRC), `winit.RWN` (winit.SRC) — nearly identical

Creates new Btrieve `.B` files from dictionary definitions. `WTASINIT` is the
current-generation version; `WINIT` is the older predecessor (one fewer variable).

**Procedures:** `OPENFILES`, `OPEN_FILES`, `AUTOCREATE`, `CREATE_FILE1`, `CREATE_FINI`,
`CF_FLNAME_VALID`, `CF_FDNAME_VALID`, `CEPATH.CLICK/POST`, `CBRECTYPE.CHANGE`,
`CBFDNAME.DROPDOWN`, `CLEARBUFFER`, `BTNINIT.CLICK`, `GIS`, `CALC_BCD_INT`,
`CEFILENAME.CLICK`, `FLLKUPSTART`, `DGFILELOCLU.SELECT`, `ENTEXT.POST/CHANGE`

**Key workflow:** User selects a file definition from FILEDICT (`CBFDNAME.DROPDOWN`),
picks a location path (`CEPATH`), chooses record type (`CBRECTYPE`), then clicks
`BTNINIT` → `CREATE_FILE1` → `CREATE_FINI`. `CALC_BCD_INT` converts integer sizes
to BCD format required by Btrieve.

**Key variables:** `CF_FLNAME`, `CF_FLCODE`, `CF_RTYPE`, `CF_DESC`, `CF_PATH`,
`CF_FDNAME`, `LOC_BUFF_NAME/FILE_NAME/COMP_CODE/REC_SIZE/REC_TYPE/LOCATION/DESCRIPTION`

---

## WTASCVTDICT — Dictionary Conversion

**File:** `wtascvtdict.RWN` (wtascvtdict.SRC, 13 procedures)

Converts from an older TAS dictionary format (FILEDFLD + FILEDBF tables) to the current
format (WCREATEDES table used by newer TAS versions).

**Procedures:** `OPENFILES`, `CHECKHANDLE`, `SCAN_DBFS`, `DO_DBF_FLDS`,
`DO_WCREATEDES`, `CREATEDESREC`, `CHG_INI_FILE`, `GETNETARRAYSIZE`,
`GIS`, `CALC_BCD_INT`, `BTNSTART.CLICK`, `BTNEXIT.CLICK`, `RTNTIMER1.CALL`

**Key variables:** `OLDLOC/DICT/DBF/KNUM/KEY/DFLD/ERR/DES_HNDL` (handles to old tables),
`DBF_HNDL`, `ERR_HNDL`, `OLD_BUFF_NAME`, `OLD_FILE_NAME`, `OLD_COMP_CODE`,
`OLD_DICT_BNAME/FNAME/OFFSET/TYPE/SIZE/DEC/ARRAY/UPCASE/DESC/PICT/LCD/HOFFS`

**Summary:** `SCAN_DBFS` walks the old FILEDBF registry, `DO_DBF_FLDS` reads each
field from FILEDFLD, `DO_WCREATEDES`/`CREATEDESREC` writes new-format records,
`CHG_INI_FILE` updates path references in an .INI file. Timer (`RTNTIMER1.CALL`)
drives progress display during batch conversion.

---

## EVOMENU_SELCOMP — Company Selection Dialog

**File:** `EVOMENU_SELCOMP.RWN` (EVOMENU_SELCOMP.SRC, 5 procedures)

The dialog shown at login when the user must select a company (multi-company
installations). Opens FILELOC to find company definitions, reads BKSYMSTR for
company metadata, then sets the global company context.

**Procedures:** `SEL_NEW_COMP`, `SELECTCOMPANY.START`, `SELECTCOMPANY.DISP`,
`BTNCANCEL.CLICK`, `BTNSELECTCOMPANY.CLICK`

**DB files opened (39 unique):** FILELOC, BKSYMSTR, BKPSUSER, BKARCUST, BKAPVEND,
BKICMSTR, BKCMACCN, BKAPDESC, BKYSMSTR, DBAHLPID, LANGDICT, MKAHIST, ISLOG,
ISNUMBER, TASCOLOR, WORKCHG, ISFOHIST, ISTAXFIL, BKARINVV, BKAPINVL, BKAPPO,
ISDRILL, BKCMACCN, ISLINKS, BKSYHELP, ISNOTES, ISNTYPE

**Company parameter variables:** `COMPCODE`, `COMPANY`, `BKSY.COMP.NAME`,
`BKSY.COMP.ADD1/ADD2/CSZ` — confirming BKSYMSTR holds company name/address.

**Other BKSY.* vars:** `BKSY.ARINV.NUM`, `BKSY.APINV.NUM`, `BKSY.APPO.NUM`,
`BKSY.GJ.NUM` (auto-number counters), `BKSY.TAX.RATE`, `BKSY.TERMS`,
`BKSY.TRM.AMT/TYP/DAY/EOM/MAX` (terms settings), `BKSY.AR.SHP.VIA`, `BKSY.AR.SLSP`,
`BKSY.AR.ENTBY` — these are BKSYMSTR fields accessed at company init.

**Note:** The long DB file list is the pre-open for the full EVO session — the company
selection module opens all tables that will be used throughout the session so they remain
open and cached.

---

## T7AUTOWOLA — i2 Systems WO Automation (ISTS.SRC)

**File:** `T7AUTOWOLA.RWN` (ISTS.SRC, 5 procs stub, 663 vars)

Custom module from i2 Systems (J7/ISTS era). Procedure names are not available
(compiled from ISTS.SRC which is not on the share), but variable names reveal the
ISTS.CFG configuration keys it reads:

**EVO.CFG.* configuration keys used:**
`TOOLBAR`, `OLWOA/OLPOA/OLINA/OLSOB/OLSOA/OLARA/OLAPA` (module "On Load" settings),
`LANG` (language), `SOUNDS`, `REMIND/EREMIND/REMSEC/RSNOOZE` (reminder settings),
`QPRINT`, `CFU` (check-for-updates), `TOPMOST`, `AREN`

**Module save-state vars:** `ARA.SAVE`, `APA.SAVE`, `DEFPRINTPATH`, `DEFPRINTER`,
`ARA/APA/INA/INB/POA/SOA/WOA.CFG.ECSCRN` (E-commerce screen flags per module)

**DB files touched (57):** Spans inventory, WO, BOM, MRP, AR, AP, GL, Lot/Serial,
NCR, DC, Classification — this is a broad automation engine that monitors and triggers
work order lifecycle events across many subsystems.
