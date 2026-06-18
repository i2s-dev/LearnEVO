"""
Pass 102 — Java Integration full documentation.
Appends comprehensive EvoPVT.jar / Java layer analysis to HELP-RESOURCES.md.
Sources:
  - samples/jar/extracted/com/evoerp/TASKS/sql/Main.class (constant pool)
  - samples/jar/extracted/com/evoerp/TASKS/sql/PervasiveDatabase.class
  - samples/jar/extracted/com/evoerp/TASKS/sql/Main$WindowsUtils.class
  - samples/jar/extracted/com/evoerp/sql/PervasiveDatabase.class
  - samples/jar/extracted/com/evoerp/sql/DatabaseSettings.class
  - samples/jar/extracted/com/evoerp/util/WinRegistry.class
  - samples/jar/extracted/com/evoerp/sql/tables/*.class (field schemas)
  - samples/jar/extracted/com/evoerp/Evo.class
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

OUT = r'C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\HELP-RESOURCES.md'

BLOCK = '''

---

## Pass 102 — Java Integration: EvoPVT.jar Architecture (2026-06-18)

**Source:** `samples/jar/extracted/` — constant-pool string extraction from 881 class files.
**Confidence:** 85/100 — all strings confirmed from class file constant pools; runtime
dispatch logic inferred from class structure since bytecode not fully decompiled.

---

### EvoPVT.jar Overview

`EvoPVT.jar` (lib version 0.4.7) is EvoERP's Java bridge layer. It operates in two modes:

| Mode | Entry Point | Purpose |
|------|-------------|---------|
| **GUI** | `com.evoerp.javafx.EvoApp` | JavaFX desktop UI (calendar, tabular views, CRM dashboard) |
| **Task runner** | `com.evoerp.TASKS.sql.Main` | CLI task executor — invoked by TAS Pro, writes results to ISJAVA |

TAS Pro 7 (tp7runtime) launches the task runner via command line, passing `host port name`
as arguments (confirmed from `Main$WindowsUtils.main()` argument dispatch to
`PervasiveDatabase.writeParams()`).

---

### ISJAVA Table (TAS Pro ↔ Java bridge)

**Confirmed from:** `TASKS/sql/PervasiveDatabase.class` constant pool.

```
INSERT INTO ISJAVA (IS_JAVA_UID, IS_JAVA_DATE, IS_JAVA_PARAM_1, IS_JAVA_PARAM_2, ...) VALUES (?, ?, ...)
```

- Table is **not** a Java model class — it lives on the TAS Pro / Pervasive side only.
- TAS Pro writes a task request row; Java reads and processes it; Java writes result params back.
- Field pattern:
  - `IS_JAVA_UID` — unique task identifier (string, used as `setString` param 1)
  - `IS_JAVA_DATE` — task date (`setDate` param 2, java.sql.Date)
  - `IS_JAVA_PARAM_N` — variable number of string parameters (dynamically constructed
    loop: `, IS_JAVA_PARAM_` + suffix + `) VALUES (?, ?` + `, ?` × N)
- `writeParams(params, maxLength)` — the Java method that performs the INSERT.
- The parameter count (N) is runtime-determined by `maxLength`.

---

### Connection Configuration: jdbc.ini

**Confirmed from:** `DatabaseSettings.class` constant pool — file name `jdbc.ini` literal.

`DatabaseSettings` reads a plain-text configuration file (`jdbc.ini`) with this format:

```ini
Company=<company-code>
Host=<server-hostname>
Port=<port-number>
Name=<database-name>
Tree Destination=<report-tree-path>
```

Key facts:
- Default file path resolved at runtime from process working directory or a known config path.
- Multiple company instances are supported via `DatabaseSettings.getInstance(code)` —
  one instance per company code, keyed in a `HashMap<String, DatabaseSettings>`.
- `getDefault()` returns the default company instance.
- `isInitialized()` guards against unread configurations.

---

### Database Connection: Pervasive JDBC

**Confirmed from:** `sql/PervasiveDatabase.class` constant pool.

- JDBC URL prefix: `jdbc:pervasive://`
- Driver class: `com.pervasive.jdbc.v2.ConnectionPoolDataSource`
- Connection parameters: host, port, name (from `jdbc.ini`)
- Connection pool managed by `DatabaseWorkerService` (thread-local connection model)
- SQL queries confirmed in this class:

```sql
-- Shop calendar holiday/weekend dates
SELECT MTCAL_DATE FROM CALENDAR WHERE MTCAL_DATE IS NOT NULL

-- Carrier tracking URL template
SELECT IS_SHIP_WEB_2 FROM ISSHIPCO WHERE IS_SHIP_SHIPVIA = ?
```

The tracking URL uses `%%TRACK%%` as a placeholder, replaced with the actual tracking
number at runtime via `String.replace("%%TRACK%%", trackingNumber)`.

---

### WinRegistry Utility

**Confirmed from:** `com/evoerp/util/WinRegistry.class` constant pool.

EvoERP Java reads/writes Windows registry using the `reg` command-line tool. Methods:
- `read(path, key)` — runs `reg query <path> /v <key>`, parses `REG_\S+` type + value
- `addKey(path, key)` / `addKey(path, key, value)` — runs `reg add`
- `deleteKey(path, key)` — runs `reg delete`

Uses `COMPLETED SUCCESSFULLY` output to detect success.
Registry paths are not embedded in this class — they are passed as arguments from callers.

---

### Process Monitor (Main$WindowsUtils)

**Confirmed from:** `TASKS/sql/Main$WindowsUtils.class` constant pool.

When the task runner starts, it monitors these three EvoERP-related processes:
```
PV.EXE  Evoerp.exe  TP7Runtime.exe
```
The `listRunningProcesses(istsPath)` method checks which of these are active.
This is likely used to determine whether TAS Pro is still alive before committing results.

---

### EvoPVT.jar GUI Architecture

**Confirmed from:** `com/evoerp/Evo.class` and javafx/* classes.

Command-line arguments accepted by the main Evo application:
| Arg | Purpose |
|-----|---------|
| `-log <level>` | Set log level (SEVERE/WARNING/INFO/CONFIG/FINE/FINER/FINEST/ALL/OFF) |
| `-nodialog` | Suppress error dialog boxes (runs in server mode) |
| `-lang <locale>` | Set locale (default: `en_US`, format: `language_country_variant`) |

Property keys read/written by `Evo.getProperty()` / `Evo.setProperty()`:
| Key | Purpose |
|-----|---------|
| `app.version` | Application version string |
| `lib.version` | Library version (confirmed: `0.4.7`) |
| `app.date` | Application build date |
| `app.name` | Application name |
| `evo.version` | EVO version (read from `EVO.VER` file) |
| `pervasive.version` | Pervasive SQL engine version |
| `company.id` | Active company code |
| `user.name` | Logged-in user name |

Logs directory: `logs/` relative to working directory. Log file: `<classname>.log`.

---

### Java SQL Layer (com.evoerp.sql)

The `sql` package is a fluent query-builder over Pervasive JDBC. Key classes:

| Class | Role |
|-------|------|
| `Query` | SELECT builder — `Query.selecting(fields).from(table).where(clause)` |
| `Table` | Table descriptor |
| `Field` | Typed field reference (`StringField`, `IntegerField`, `BigDecimalField`, `LocalDateField`, `LocalTimeField`) |
| `Clause` | WHERE condition builder (`AndClause`, `OrClause`, `BinaryClause`, `NullClause`) |
| `Ordering` | ORDER BY builder |
| `Sql` | Utility class with static SQL helpers |
| `ShopCalendar` | Wraps CALENDAR table; returns `Set<LocalDate>` of holidays/weekends |
| `DatabaseWorkerService` | Thread pool with thread-local connections for concurrent queries |

---

### Complete Java-Side Table Model

The `com.evoerp.sql.tables` package contains **~260+ Java model classes**, one per
Pervasive table. These are the tables EvoPVT.jar can query. Full inventory by module:

**AP (Accounts Payable):**
BKAPADSC, BKAPAPO, BKAPAPOL, BKAPCHKF, BKAPCHKH, BKAPDEP, BKAPDESC, BKAPEIVT,
BKAPEVND, BKAPHDSC, BKAPHPO, BKAPHPOL, BKAPINVL, BKAPINVT, BKAPNOTE, BKAPPO, BKAPPOL,
BKAPQUOT, BKAPRFQ, BKAPRFQL, BKAPRIVL, BKAPVEND, BKAPVND2

**AR (Accounts Receivable):**
BKARCHKF, BKARCHKH, BKARCUST, BKARDEP, BKARDESC, BKARDPST, BKARECST, BKAREIVT,
BKARHDSC, BKARHINV, BKARHIVL, BKARHTAX, BKARINV, BKARINVI, BKARINVL, BKARINVT, BKARINVV,
BKARRDSC, BKARRINV, BKARRIVL, BKARSHIP, BKARSIVL, BKART, BKARTNOT, BKARTXN, BKARTXNB, BKARTXNS

**BM (Bill of Materials):**
BKBMAMTR, BKBMAVAL, BKBMCNFG, BKBMDIM, BKBMEMTR, BKBMERMK, BKBMMSTR, BKBMNOTE, BKBMREMK, BKBMSUMM

**CM (CRM / Customer Management):**
BKCMACCC, BKCMACCL, BKCMACCN, BKCMACCT, BKCMACFC, BKCMACTD, BKCMACTF, BKCMACTH,
BKCMCNTD, BKCMCTL1..4, BKCMCTRL, BKCMCUST, BKCMDE, BKCMDTCD, BKCMDUN, BKCMDUNH,
BKCMEACC, BKCMEACD, BKCMEACF, BKCMEACH, BKCMEACT, BKCMEFTM, BKCMFORM, BKCMFTME,
BKCMHCD2, BKCMHCOD, BKCMLEAD, BKCMMHST, BKCMPCFC, BKCMPCNT, BKCMPCTF, BKCMPCTH,
BKCMREP, BKCMSBDF, BKCMTEMP, BKCMTERR, BKCMTMP1..4, BKCMVNDF, BKCMVNDH, BKCMVNFC

**DC (Data Collection):**
BKDCCFG, BKDCCLAB, BKDCHLAB, BKDCLAB, BKDCPLAB, BKDCSHFT, BKDCTLAB

**EDI:**
BKEDIDUN, BKEDIH, BKEDIL, BKEDMSTR, BKEDNOTE, BKEDPOST

**Estimating:**
BKESTCFG, BKESTQT, BKESTQTL

**GL (General Ledger):**
BKGLACHK, BKGLCCOA, BKGLCHK, BKGLCOA, BKGLDESC, BKGLECOA, BKGLETRN, BKGLFCOA, BKGLFSTL,
BKGLGJLN, BKGLGJRN, BKGLHIST, BKGLRGJL, BKGLRGJR, BKGLSTMT, BKGLTEMP, BKGLTGJL, BKGLTGJR,
BKGLTMP, BKGLTMP2, BKGLTMP3, BKGLTRAN, BKGLX, BKGLXH

**IC (Inventory / Items):**
BKICALTD, BKICALTP, BKICAMTR, BKICAPMA, BKICDIM, BKICELOC, BKICEMTR, BKICLOC, BKICLOCM,
BKICMFG, BKICMSTR, BKICPMAT, BKICREF, BKICREQ, BKICTAX, BKICVAL

**MRP/Other:**
BKISHTAX, BKISTAX, BKLOGON, BKMATCST, BKMATRIM, BKMRPFC, BKMRPPO, BKMRPSW

**Packing/PI (Physical Inventory):**
BKPCKIT, BKPCPLOT, BKPIFROZ, BKPILCNT, BKPILOT, BKPIMSTR, BKPIPHYS, BKPISCNT, BKPISER

**PO (Purchase Orders):**
BKPOX, BKPOXH

**PR (Payroll):**
BKPRACOM, BKPRAGNT, BKPRBOOK, BKPRCOMM, BKPRCURP, BKPRFTAX, BKPRGLFL, BKPRHCOM,
BKPRHIST, BKPRINFO, BKPRMSTR, BKPRSALE, BKPRSTFL, BKPRTC, BKPRTCFG, BKPRW2

**QC (Quality Control):**
BKPSUSER, BKQCMSTR, BKQCTRAN, BKQTNOTE, BKQTTEMP

**RFQ / Routing:**
BKRFQ, BKRFQDES, BKRTCST, BKRTEMTR, BKRTSPEC, BKRTTEMP

**SA (Sales Analysis):**
BKSAREPT, BKSBMFG, BKSBPART, BKSBVEND, BKSHORT

**Security/Users:**
BKSLEVEL, BKSLMSTR, BKSYAP, BKSYAR, BKSYCFG, BKSYHELP, BKSYLOG, BKSYMSTR, BKSYPRTR, BKSYUSER

**SO (Sales Orders):**
BKSOHLOT, BKSOHSER, BKSOLOCK, BKSONOTE, BKSOPO

**Update/History:**
BKUMSRTY, BKUPDATE, BKWOPO, BKYSMSTR

**IS-prefix tables (EVO extensions):**
IS2DBAR, ISANOTES, ISAPACHK, ISAPAINL, ISAPAINT, ISAPARFL, ISAPARFQ, ISAPAVND, ISAPCHG,
ISAPHCHG, ISAPHQT, ISAPPROJ, ISAPQTQT, ISARACHK, ISARACST, ISARADSC, ISARAHDS, ISARAHIL,
ISARAHIN, ISARAHTX, ISARAINT, ISARAINV, ISARAIVI, ISARAIVL, ISARAIVV, ISARAT, ISARATNT,
ISARATXN, ISARATXS, ISARCHG, ISAREMND, ISARFQ, ISARHCHG, ISARINVX, ISARTXNB, ISAUTODC,
ISBANKS, ISBILLSH, ISBINLOC, ISBINLOT, ISBMEST, ISBMTMP, ISBNMSTR, ISBRANDC, ISBRANDS,
ISBROKER, ISBSF, ISBTCSB, ISBUILD, ISCATMST, ISCC, ISCHAIN, ISCHAINM, ISCONVRT, ISCTREVU,
ISCYCLCD, ISDEPT, ISDIGSIG, ISDIV, ISDLCK1, ISDLCK2, ISDRILL, ISDRILLM, ISDUTY, ISEAB,
ISECO, ISEDINFO, ISESTAQL, ISESTAQT, ISESTASM, ISESTDTL, ISESTHDR, ISESTLNE, ISESTPO,
ISFIELDS, ISFOBMRM, ISFOHEAD, ISFOHIST, ISFOLINE, ISFOORDL, ISFXASST, ISFXATRN, ISGLBDGT,
ISGLCOA, ISGLDATE, ISGLFCOA, ISGLHDAT, ISGLNBGT, ISICADT, ISICAMTR, ISICEST, ISICMSTR,
ISIS, ISISATAX, ISITMCFG, ISITP, ISJBSF, ISJOB, ISLANDF, ISLBLMAP, ISLINKS, ISLOCCST,
ISLOG, ISLSMAP, ISLTYPE, ISMACS, ISMCF, ISMCR, ISMICADT, ISMICEST, ISMRPFC, ISNOTES,
ISNTYPE, ISNUMBER, ISORDDSC, ISORDECO, ISPODESC, ISPOHTRK, ISPOS, ISPOSC, ISPOTRK,
ISPREQ, ISPRESN, ISPRMSTR, ISPRSALE, ISPRTEMP, ISQCMTHD, ISQCRSLT, ISQCSPEC, ISQSOA,
ISQTINFO, ISREMIND, ISREPDEF, ISREPLNK, ISREPORD, ISRFQADS, ISRMAAI, ISRMAC, ISRMAI,
ISRTEST, ISRTLOAD, ISSCHED, ISSDET, ISSEPROC, ISSEQUIP, ISSERCNT, ISSERR, ISSETYPE,
ISSHIPCO, ISSHPVIA, ISSLSFC, ISSOABOX, ISSOAHBX, ISSOALOT, ISSOASER, ISSOBOX, ISSOHBOX,
ISSOHNFO, ISSOINFO, ISSOREVU, ISSPC, ISSRADSC, ISSRAINF, ISSRAINV, ISSRAIVL, ISSRAMMS,
ISSRDESC, ISSRINFO, ISSRINV, ISSRINVL, ISSRMMS, ISSTEQUI, ISSTTYPE, ISSTYPE, ISTAXFIL,
ISTAXGRP, ISTERMS, ISTRIGRS, ISUDFINV, ISUDMSTR, ISUSAGE, ISVAR, ISVNDADT, ISWODESC,
ISWOEX, ISWOHDSC, ISWOPRIO, ISWOROEX, ISWOTRAY

**Misc / Other:**
ARTTEMP, BKABCUST, BKABVEND, BKACTRPT, BKCPEC, BKCPMSTR, BUCKETS, CALTEMP, CCEDIXRF,
CLASMSTR, CLASS, CUSTCLAS, DBACNAME, DBAFIFO, DBAHLPID, DISCOUNT, DPTMENT, ESTCHGS,
ESTMAT, ESTROUT, ESTSUM, EVOHLPID, HELPURL, INVATXN, INVETXN, INVTXN, JSPCNLCD, JSPCNLSO,
LANGDICT, LOT, MACHINE, MENUFILE, MKAHIST, MKASSIGN, MKDEF, MKECLASS, MKEVENT, MKFORM,
MKICLASS, MKTCLASS, MKTNOTE, MKTRACK, MKTROUT, MTEXCHG, MTICAMTR, MTICEMTR, MTICMSTR,
MTINVDEF, MTMRP, MWOPTEMP, NOTETEMP, NZITPRE, OUTHPROC, OUTPROC, PIBINLOC, PIBINLOT,
QCCODES, ROUTAING, ROUTING, ROUTTEMP, SCHEDCAL, SCHWO, SCRAP, SERIAL, SERIALH, SUMCUST,
SUMINV, SUMPNCUS, SUMWC, TEMPOLD, TESTFILE, TOOL, WBTRVMEM, WBTRVMEMO, WCCTL, WCTRLOAD,
WCTRSLOD, WOBOM, WOBOMHRM, WOBOMREM, WODATE, WOELABOR, WOEMAT, WOERECV, WOEXCHG, WOHBOM,
WOHDATE, WOHEXCHG, WOHLABOR, WOHMAT, WOHRECV, WOHROUT, WOLABOR, WOLABRPT, WOMAT, WORECV,
WORKCHG, WORKCTR, WORKHORD, WORKORD, WORKSORD, WOROUT, WOROUTMP, WOSROUT, XXICMSTR

---

### Key Table Field Schemas (Java-confirmed)

#### ISLINKS — 311 fields
EvoLinks document attachment table. Full schema:
- `IS_LNK_UID` — unique link ID
- `IS_LNK_LINK` — file/URL path being linked
- `IS_LNK_APP` — application type for linked file
- `IS_LNK_ATYPE` — attachment type code
- `IS_LNK_DATE` — link creation date
- `IS_LNK_WHO` — user who created the link
- `IS_LNK_NOTE` — description note
- `IS_LNK_OPENWITH` — open-with application override
- `IS_LNK_GLOBAL` — global link flag (visible to all users)
- `IS_LNK_ALPHA` — additional alpha field
- `IS_LNK_EXTRA` — extra/overflow field
- `IS_LNK_PCB_1..100` — 100 parent-context-block fields (entity key fields)
- `IS_LNK_DEF_1..100` — 100 definition/descriptor fields
- `IS_LNK_TYPES_1..100` — 100 type classification fields

The PCB/DEF/TYPES arrays (100 each) store context keys linking a document to specific
records across all modules — enabling the same document to be attached to multiple entities.

#### ISREMIND — 24 fields
Reminders and calendar events:
IS_REM_WHO, IS_REM_DATE, IS_REM_TIME, IS_REM_ENDDT, IS_REM_ENDTM, IS_REM_ETIME,
IS_REM_SUBJECT, IS_REM_TYPE, IS_REM_CO, IS_REM_DISP, IS_REM_CUST, IS_REM_VEND, IS_REM_ITEM,
IS_REM_FILE, IS_REM_MEMO, IS_REM_NOTE, IS_REM_EMAIL, IS_REM_NOTIFY, IS_REM_SENT,
IS_REM_TRANS, IS_REM_BEFTXT, IS_REM_COUNTER, IS_REM_EDATE, IS_REM_EXTRA

#### ISSHIPCO — 16 fields
Shipping carrier master:
IS_SHIP_SHIPVIA (PK), IS_SHIP_SHPCOD, IS_SHIP_SHPDESC, IS_SHIP_SHPNME, IS_SHIP_VNDCOD,
IS_SHIP_WEB_1..5 (5 tracking URL templates — WEB_2 confirmed used for parcel tracking),
IS_SHIP_NOTES_1..5 (5 note lines), IS_SHIP_EXTRA

#### CALENDAR — 5 fields
Shop calendar:
MTCAL_DATE, MTCAL_DESC, MTCAL_SAT, MTCAL_SUN, MTCAL_YEAR

#### BKLOGON — 10 fields
Active login session record (one row per active EVO session):
BKLOGON_CODE (user code), BKLOGON_PSWD, BKLOGON_SCRTY (security level), BKLOGON_MENU,
BKLOGON_SUBMENU, BKLOGON_CMPY (company), BKLOGON_PRINTER, BKLOGON_CURPRT (current printer),
BKLOGON_INUSE (Y/N in-use flag), BKLOGON_PROG (current program code)

#### BKSYUSER — 5 fields
System user table (simple login credentials):
BKSY_USER_CODE (user code), BKSY_USER_PSWD, BKSY_USER_SCTY (security level),
BKSY_USER_COMP (company), BKSY_USER_CHR

#### BKSLEVEL — 422 fields
Security level permission table. Pattern: BKSL_MENU{1..20}_{1..20} + BKSL_MENU{1..20}_YN.
For 20 menus × 21 fields each = 420 + BKSL_LEVEL + BKSL_MENU = 422 total.
Each menu section has 20 item permissions (Y/N) plus a master YN flag for that menu.

#### BKSYCFG — 4 fields
System module configuration flags:
BKSY_CFG_ACCTG (accounting mode), BKSY_CFG_ADVWO (advanced WO), BKSY_CFG_LITEWO (lite WO),
BKSY_CFG_SALES (sales configuration)

#### BKUPDATE — 4 fields
Update history record:
BKUPDATE_VER, BKUP_COMPANY, BKUP_DATE, BKUP_UPDATE

#### BKBMMSTR — 26 fields
Bill of Materials component record:
BKBM_UID, BKBM_PARENT (parent item code), BKBM_COMPONENT (child item code),
BKBM_P_TYPE, BKBM_C_TYPE, BKBM_QTY_REQD, BKBM_REFERENCE, BKBM_REV, BKBM_EXTRA,
BKBM_DATE1, BKBM_DATE2, BKBM_EST_LINE, BKBM_PROD_OP, BKBM_PROD_OPDSC, BKBM_PROD_DUPOP,
BKBM_PROD_TYPE, BKBM_PROD_SCRAP, BKBM_PROD_PRICE, BKBM_PROD_VEND, BKBM_PROD_RTNUM,
BKBM_PROD_OPYN_1..6

#### ISFOHEAD — 16 fields
Features & Options header (F&O master):
ISFO_HDR_UID, ISFO_HDR_PARENT (item code), ISFO_HDR_DESC, ISFO_HDR_STATUS, ISFO_HDR_DATE,
ISFO_HDR_CUST, ISFO_HDR_VEND, ISFO_HDR_RFQ, ISFO_HDR_REV, ISFO_HDR_PERM,
ISFO_HDR_MDATES_1..5 (5 milestone dates), ISFO_HDR_EXTRA

#### ISFOLINE — 78 fields
Features & Options line (F&O component):
ISFO_LIN_UID, ISFO_LIN_PARENT, ISFO_LIN_COMP, ISFO_LIN_TYPE, ISFO_LIN_LEVEL, ISFO_LIN_LINEN,
ISFO_LIN_OP, ISFO_LIN_OPDSC, ISFO_LIN_DUPOP, ISFO_LIN_RTNUM, ISFO_LIN_QTYREQ, ISFO_LIN_PRICE,
ISFO_LIN_SCRAP, ISFO_LIN_REV, ISFO_LIN_REF, ISFO_LIN_VEND, ISFO_LIN_DATE1, ISFO_LIN_DATE2,
ISFO_LIN_CBRANC, ISFO_LIN_PBRANC, ISFO_LIN_BEXTRA, ISFO_LIN_EXTRA,
ISFO_LIN_OPFLAG_1..50 (50 operation flags), ISFO_LIN_OPYN_1..6

#### AHSYLOG — 23 fields
Security access log / user session:
AHSY_USER_CTRL, AHSY_USER_LEVL, AHSY_USER_MENU, AHSY_USER_ACCES_1..20

#### MACHINE — 16 fields
Machine master (work center machine):
TMACH_MACHINE (PK), TMACH_WC (work center), TMACH_WCDESC, TMACH_DESC, TMACH_DATE,
TMACH_HRSUSED, TMACH_HRSMAINT, TMACH_EXTRA, TMACH_NOTES_1..8

#### ROUTING — 62 fields
Routing operation master (MTRO_* prefix — full schema):
MTRO_NUM (routing number), MTRO_CODE (product code), MTRO_OPER (operation), MTRO_OPERDESC,
MTRO_DESC, MTRO_WC, MTRO_WCDESC, MTRO_TYPE, MTRO_R_TYPE, MTRO_CLASS, MTRO_LABOR,
MTRO_SETUP, MTRO_SETUPHRS, MTRO_STD_TIME, MTRO_DEF_TIME, MTRO_OVERTIME, MTRO_LEAD,
MTRO_LONGTIME, MTRO_LOTSIZE, MTRO_OVERLAP, MTRO_NEGOVLP, MTRO_PRINT, MTRO_PARTSHR,
MTRO_MACHINE, MTRO_TMACHINE, MTRO_TMACHDESC, MTRO_TOOL, MTRO_TOOLDESC, MTRO_MIN_CHG,
MTRO_PIECE_RATE, MTRO_NUM_PERSON, MTRO_NUM_PROCES, MTRO_MD_PROC_HR, MTRO_PROC_PERHR,
MTRO_TIME_PERPR, MTRO_TIMEPART, MTRO_FOVHD, MTRO_VOVHD, MTRO_EST_LINE, MTRO_EST_TAG,
MTRO_MISC_ACOST, MTRO_OP_TEMP_NO, MTRO_VENDCODE, MTRO_VENDCOST, MTRO_VENDNAME,
MTRO_INSTR_1..15 (15 instruction lines), MTRO_EXTRA,
MTWO_MISC_COST, MTWO_MISC_DESC (WO misc cost fields stored in routing record)

#### WORKCTR — 24 fields
Work center master (MTWC_* prefix — full schema):
MTWC_WC (PK), MTWC_WCDESC, MTWC_DEPT, MTWC_DEPTDESC, MTWC_LABOR, MTWC_SETUP, MTWC_FOVHD,
MTWC_VOVHD, MTWC_EST_VOVHD, MTWC_LEAD, MTWC_HRSWEEK, MTWC_HRS_SHIFT, MTWC_AVGQTIME,
MTWC_COST_LB, MTWC_MACHINE, MTWC_MIN_CHG, MTWC_OUTPROC, MTWC_PARENT_WC, MTWC_PARENT_YN,
MTWC_LEVEL_YN, MTWC_QPR1, MTWC_QPR2, MTWC_QPR3, MTWC_EXTRA

#### ISBSF — 143 fields
Business Score File (ISBSF_* prefix — rebuilt by EVOBSR):
Key summary fields: AP_ATP, AP_BAL, AP_DISC, AP_PAYA, AP_PAYM, AR_BAL, AR_BILL, AR_COGS,
AR_DEPO, AR_DISC, AR_RECP, IC_VALUE, SO_BOOK, SO_OPEN, SO_SHIP, PO_BOOK, PO_OPEN, PO_RECP,
WOS_FOH/FP/LAB/MAT/MEXT/OUTP/SETUP/VOH/WIPV, WO_FPVAR, WO_ISSU, WO_WIPBAL,
CASH_ACT1..9 (9 manual cash accounts), CASH_ACTS_1..100 (100 G/L cash accounts),
CASH_TOTA, STARTDATE, ENDDATE, EXTRA

#### BKSYMSTR — 286 fields
System master (company settings, terms, GL accounts):
Key groups: AP setup (APINV_NUM, APPO_NUM, AP_AGING_1..5, AP_CHKACT, AP_DISCGL, AP_GLACT),
AR setup (ARINV_NUM, ARSO_NUM, AR_AGING_1..5, AR_CHKACT, AR_FREIGHT, AR_INT_DAY/RTE, AR_TAXABL),
Company info (COMP_ADD1/ADD2/CSZ/NAME), Check accounts (CHK_NAME/NUM/ACT/CUR/DPT_1..9),
GL accounts (GL_ARINTR, GL_CLRING, GL_RELYR, GL_RETEARN + GLDPT equivalents),
Terms (TERMS_1..20 names + TRM_AMT/DAY/DISC/EOM/MAX/TYP_1..20 = 120 term detail fields),
PO setup (PO_FREIGHT, PO_INR, PO_RNI, PO_TAXGL), PR setup (PR_ODNAME_1..6),
Fiscal year (FISCAL_YR), Extra fields (EXTRA)

---

*Java Integration documentation auto-generated Pass 102 from EvoPVT.jar class file constant pool extraction.*
'''

with open(OUT, encoding='utf-8') as f:
    existing = f.read()

with open(OUT, 'w', encoding='utf-8') as f:
    f.write(existing + BLOCK)

print(f'Appended {len(BLOCK):,} chars to HELP-RESOURCES.md')
