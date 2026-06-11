# EVO-DECOMPILE-TODO.md
# EvoERP Full Decompile & Documentation Master Checklist

**Goal:** Reach 90–95% understanding of every module, table, data flow, and behavior so that
EVO code or tables can be accurately explained, modified, or reproduced.

**Confidence Scale:**
- **90–100** — Fully verified, zero meaningful unknowns, could write a spec from memory
- **70–89** — Well understood, minor gaps or unverified edge cases
- **50–69** — Solid foundation, several confirmed facts, but significant unknowns remain
- **30–49** — Partial — key facts confirmed but core logic or schema incomplete
- **10–29** — Surface-level only — structure identified, content still opaque
- **0–9** — Essentially unknown

**Status Legend:**
- ✅ Done — documented, confidence rated
- 🔄 In Progress — started but incomplete
- ⬜ Not Started — not yet touched

---

## TABLE OF CONTENTS

1. [System Architecture & Runtime](#1-system-architecture--runtime)
2. [File Formats](#2-file-formats)
3. [TAS Pro 4GL Language](#3-tas-pro-4gl-language)
4. [Data Dictionary & Database Schema](#4-data-dictionary--database-schema)
5. [Security & Login System](#5-security--login-system)
6. [Menu System & Navigation](#6-menu-system--navigation)
7. [Modules — Functional Documentation](#7-modules--functional-documentation)
8. [Reporting Engine (ReportBuilder / RTM)](#8-reporting-engine-reportbuilder--rtm)
9. [Platform Subsystems](#9-platform-subsystems)
10. [Java Integration (EvoPVT.jar)](#10-java-integration-evopvtjar)
11. [ODBC / External Connectivity](#11-odbc--external-connectivity)
12. [Customization Modules (J7\*)](#12-customization-modules-j7)
13. [Business Workflows / Recipes](#13-business-workflows--recipes)
14. [Encryption & Reverse Engineering Blockers](#14-encryption--reverse-engineering-blockers)
15. [Help System (EvoHELP.CHM)](#15-help-system-evohelpchm)
16. [Per-Table Schema Pages](#16-per-table-schema-pages)
17. [Per-Form Documentation](#17-per-form-documentation)
18. [Per-Report Documentation](#18-per-report-documentation)
19. [Infrastructure & Deployment](#19-infrastructure--deployment)
20. [Master Confidence Summary](#20-master-confidence-summary)

---

## 1. SYSTEM ARCHITECTURE & RUNTIME

### 1.1 High-Level Architecture
- [x] ✅ Three-tier model identified (Client thin install / Network share / tp7runtime.exe stateless) — **C: 78/100**
  - Confirmed: `C:\ISTS\` = thin client, `\\i2s109-solidcrm\DBAMFG$\` = program/data share
  - Gap: exact IPC between client and share not fully traced; StartEvo.exe internals not decoded
- [x] ✅ Network share layout mapped (`DBAMFG$\`, `evo-ERP\`, `ISTS\`, `EVOReports\`, `2004.1\`) — **C: 85/100**
- [x] ✅ Multi-company layout understood (per-company subdirs + `.B<code>` file suffixes) — **C: 82/100**
  - Known company codes: Default, 22, AB, AT, CA, Goldstar, I2, IT, UU, DefaultSQL, Testdata, DEV, Bak Up, Menu Backup, Recovered
- [x] ✅ Company count ceiling (~1,200 possible; 2-char alphanumeric codes) — **C: 70/100**
- [ ] ⬜ Full network topology diagram (workstations ↔ server ↔ Pervasive service ↔ share paths)
- [ ] ⬜ Pervasive SQL server role vs. workgroup mode documented with actual config on i2s109-solidcrm

### 1.2 Boot Sequence
- [x] ✅ Full boot chain traced: `EvoERP.lnk → StartEvo.exe → tp7runtime.exe → EvoERPmenu.rwn → login → company → module` — **C: 72/100**
- [x] ✅ `StartEvo.exe` role: checks runtime, reads `taspro7.ini`, spawns tp7runtime.exe — **C: 60/100**
  - Gap: exact command-line arguments passed to tp7runtime.exe not confirmed
- [x] ✅ `taspro7.ini` keys documented: `DataDictPath`, `DfltRunPrg`, `MultiUser`, `DefaultPath`, `Titlebar`, `HelpFileName` — **C: 80/100**
- [x] ✅ Bootstrap RWNs identified: `suwin6.dcy`, `suwin7.dcy`, `suwin6t.rwn`, `suwin7t.rwn` — **C: 55/100**
  - Gap: what these actually do before EvoERPmenu.rwn loads is not confirmed
- [x] ✅ Per-workstation state files cataloged: `taspro7.ini`, `EvoSettings.INI`, `WHOAMI.DBA`, `CHMHELP.EVO`, `RBuilder.ini`, `DFM/`, `PDFS/` — **C: 68/100**
- [ ] ⬜ `EvoSettings.INI` fully decoded (which modules it gates, format, all keys)
- [ ] ⬜ `StartEvo.exe` binary analyzed (exact command line, version check logic, error handling)
- [ ] ⬜ `suwin6/7.dcy` pre-load behavior traced

### 1.3 Runtime Engine (tp7runtime.exe)
- [x] ✅ Identified as TAS Professional 7 by Computer Keyes / Business Tools — **C: 90/100**
- [x] ✅ 33.3 MB executable; embeds Qt 3/CLX UI layer (`qtintf70.dll`) + CodeBase data engine (`c4dll.dll`) — **C: 85/100**
- [x] ✅ Keyword list extracted from embedded strings (`tp7runtime.keywords.txt`) — **C: 88/100**
- [ ] ⬜ Runtime version number and build date confirmed
- [ ] ⬜ All DLLs loaded by tp7runtime.exe cataloged with purpose
- [ ] ⬜ Error-code table (runtime error messages ↔ numeric codes)

---

## 2. FILE FORMATS

### 2.1 `.SRC` — TAS Pro 4GL Source Code
- [x] ✅ Encoding confirmed: plaintext ASCII, CR+LF, no BOM — **C: 92/100**
- [x] ✅ Comment syntax: `;` to end-of-line — **C: 95/100**
- [x] ✅ Compiler directives: `#PRO3`, `#UDX`, `#LIB <name>`, `#INC <name>`, `SETUP_COLOR` — **C: 85/100**
- [x] ✅ Variable declaration syntax: `define <name> type A/i/n/d/t size <N> [array <N>]` — **C: 88/100**
- [x] ✅ Database I/O keywords: `open`, `find F srch`, `clr`, `del`, `dall` — **C: 80/100**
- [x] ✅ UI/form keywords: `mount`, `prg_hdr`, `enter`, `xtrap`, `fnc_list`, `menu` — **C: 75/100**
- [x] ✅ 7 plaintext `.SRC` files analyzed: BKAWLB, BKDCA, BKLME, BKMRF, BKROA, Bkaph, Bkapha — **C: 70/100**
- [ ] ⬜ Full grammar specification (all operators, expression types, precedence)
- [ ] ⬜ `.a.` / `.o.` / `.n.` / `$` operators fully documented with behavior
- [ ] ⬜ Include resolution order (`#INC` / `#LIB` search paths)
- [ ] ⬜ `SETUP_COLOR` macro fully expanded
- [ ] ⬜ Variable scope rules inside `{ func ... ret ... }` blocks
- [ ] ⬜ All 1,265 `.RUN` + 1,115 `.RWN` source files (logic content — blocked by encryption; see §14)

### 2.2 `.RWN` — TAS Pro 7 Compiled Program
- [x] ✅ Format: encrypted/compressed binary; license-bound decoder in tp7runtime.exe — **C: 65/100**
- [x] ✅ High entropy from offset 0; no readable strings in first 4 KB — **C: 90/100**
- [x] ✅ Paired with same-basename `.DFM` (layout ↔ logic) — **C: 90/100**
- [ ] ⬜ Encryption algorithm identified (suspected Twofish-CFB, not confirmed — see §14)
- [ ] ⬜ Any `.RWN` successfully decrypted and read as bytecode
- [ ] ⬜ Bytecode instruction set documented

### 2.3 `.RUN` — TAS Pro 6 Compiled Program
- [x] ✅ Older generation; readable strings present (menu codes extractable) — **C: 85/100**
- [x] ✅ 554 menu codes extracted from `.RUN` string dump — **C: 88/100**
- [x] ✅ Still in active use for legacy BK\* / T6\* modules — **C: 80/100**
- [ ] ⬜ Binary structure fully documented (header, offset table, bytecode section, string pool)
- [ ] ⬜ All readable logic extracted from `.RUN` string sections

### 2.4 `.DFM` — Delphi Form Layout
- [x] ✅ Format confirmed: plaintext Borland Delphi VCL textual form representation — **C: 92/100**
- [x] ✅ Structure: `object ClassName ... property = value ... object Child ... end ... end` — **C: 90/100**
- [x] ✅ 1,109 forms successfully parsed; 25 failures are zero-byte placeholders — **C: 90/100**
- [x] ✅ Key properties documented: Left/Top, BorderStyle, Font, Caption, Hint (dev path hint) — **C: 85/100**
- [x] ✅ Child controls identified: TLabel, TEdit, TButton, TPanel, TGroupBox, TDBGrid — **C: 78/100**
- [x] ✅ DFM ↔ RWN pairing rule confirmed (same basename) — **C: 92/100**
- [x] ✅ DFM summary CSV generated (`samples/dfm_parsed/dfm_summary.csv`) — **C: 88/100**
- [ ] ⬜ TAS-specific control types fully cataloged (TTASEdit, TTASGrid, T7\* custom controls)
- [ ] ⬜ All TAS-specific control properties documented with behavior
- [ ] ⬜ Form-to-menu-code mapping fully resolved (which DFM opens for each menu code)
- [ ] ⬜ Binary `.DFM` variant (the 25 TPF0-format forms) decoded

### 2.5 `.DCY` — Data Dictionary / Compiled Schema
- [x] ✅ Format: encrypted binary; same encryption model as `.RWN` — **C: 60/100**
- [x] ✅ 6 samples cataloged: EVOERPMENU.DCY (1.4 MB), EVODC.DCY (746 KB), EVOUSERS.DCY (27 KB), + others — **C: 80/100**
- [x] ✅ Paired with `.RWN` of same basename — **C: 85/100**
- [ ] ⬜ Any `.DCY` successfully decrypted / structure read
- [ ] ⬜ Login/company DCY files decoded: EVOMENU_LOGIN.DCY, EVOMENU_SELCOMP.DCY, EVORESETPASS.DCY, EVOCHANGEPASS.DCY

### 2.6 `.RTM` / `.btm` — ReportBuilder Templates
- [x] ✅ Format confirmed: TPF0 binary (Delphi binary stream, Nevrona TppReport component tree) — **C: 85/100**
- [x] ✅ Magic bytes: `54 50 46 30` ('TPF0') — **C: 95/100**
- [x] ✅ Key classes: TppReport, TppDetailBand, TppSubReport, TppChildReport, TppShape, TppLabel, TppDBText — **C: 80/100**
- [x] ✅ Data pipeline binding: TAS sets up "TASFile" pipeline; fields bound by name (e.g., BKAP_CHK_INVNUM) — **C: 75/100**
- [x] ✅ TAS keywords for reporting: EXEC_RB, RTM_FN, REPORTNAME, USE_PRINTER, PRINT_TO_FILE — **C: 80/100**
- [x] ✅ `.btm` confirmed as backup/snapshot of `.RTM` in same format — **C: 72/100**
- [x] ✅ 899+ RTM files inventoried; 60 `.btm` files cataloged — **C: 88/100**
- [ ] ⬜ Complete TPF0 property table (every TppComponent property type + offset)
- [ ] ⬜ Full RTM ↔ module cross-reference (which report is called from which SRC function)
- [ ] ⬜ All 899 RTM files parsed for data-field bindings

### 2.7 `.B` / Btrieve Data Files
- [x] ✅ Format: Pervasive/Btrieve B-tree paged file; FC magic header — **C: 72/100**
- [x] ✅ Schema queryable via Pervasive ODBC (SELECT from X$File, X$Field) — **C: 88/100**
- [x] ✅ Companion files: `.mdx` (index), `.XLB` (extended attributes) — **C: 65/100**
- [x] ✅ Per-company suffix: default = `.B`, others = `.B22`, `.BAB`, etc. — **C: 85/100**
- [ ] ⬜ Btrieve page layout at byte level (header, page size, record format)
- [ ] ⬜ Index structure decoded from `.mdx` companion
- [ ] ⬜ Low-level I/O operations (Btrieve status codes, operation codes) documented

### 2.8 `.IMP` — Import Definition
- [x] ✅ Format: plaintext; source filename + mode (e.g., `U:\PROFPN.CSV SC`) — **C: 80/100**
- [x] ✅ 11 files cataloged — **C: 85/100**
- [ ] ⬜ All import definition keywords/flags documented
- [ ] ⬜ Import pipeline traced end-to-end (which SRC calls the import, which table it populates)

### 2.9 `.XPT` — Export Layout
- [x] ✅ Format: plaintext; `output.TXT flag FIELD1 FIELD2…` — **C: 78/100**
- [x] ✅ 20 files cataloged; cover BKAP/BKAR/BKSO exports — **C: 80/100**
- [ ] ⬜ All export flags documented
- [ ] ⬜ Export pipeline traced (SRC → .XPT → .TXT output flow)

### 2.10 `.UPD` — Schema Migration Manifest
- [x] ✅ Format: Btrieve DDF; mirrors Pervasive system catalog tables (FILE\*.UPD) — **C: 75/100**
- [x] ✅ Purpose: schema-migration snapshots used by EvoUpdate subsystem — **C: 70/100**
- [ ] ⬜ Full update pipeline traced (how EvoUpdate applies .UPD patches to live tables)
- [ ] ⬜ All FILE\*.UPD files parsed and delta-compared to current schema

### 2.11 `.DBA` — Identity / Seat Token
- [x] ✅ File identified: `WHOAMI.DBA` (35 bytes, per-workstation) — **C: 65/100**
- [ ] ⬜ Byte layout decoded (what each of the 35 bytes means)
- [ ] ⬜ How WHOAMI.DBA is generated (install-time? first-run? server-assigned?)
- [ ] ⬜ How tp7runtime.exe reads/validates WHOAMI.DBA

### 2.12 `.EVO` — Unknown Marker File
- [x] ✅ File identified: `CHMHELP.EVO` (35 bytes); same size as WHOAMI.DBA — **C: 40/100**
- [ ] ⬜ Purpose confirmed (hypothesis: "CHM help present" presence marker)
- [ ] ⬜ Byte content decoded

### 2.13 `.CHM` — Windows HTML Help
- [x] ✅ `EvoHELP.CHM` successfully decompiled with `hh.exe -decompile` — **C: 92/100**
- [x] ✅ 779 topics extracted to `samples/chm/extracted/` — **C: 95/100**
- [x] ✅ Topic categories: 636 per-menu-code + 90 conceptual chapters + 53 meta — **C: 90/100**

---

## 3. TAS PRO 4GL LANGUAGE

### 3.1 Language Fundamentals
- [x] ✅ Language family: xBase-style 4GL; interpreted by tp7runtime.exe — **C: 85/100**
- [x] ✅ Keyword list extracted from runtime embedded data (~300+ keywords) — **C: 88/100**
- [x] ✅ Variable types: A (alphanumeric), i (integer), n/d (numeric/decimal), t (date), time — **C: 85/100**
- [x] ✅ Comment syntax: `;` to end-of-line — **C: 95/100**
- [x] ✅ Control flow: `if/else/endif`, `for(...)/next`, `select/endselect`, `while/loop_if/exit_if`, `goto/gosub/return` — **C: 82/100**
- [x] ✅ Trap mechanism: `trap <key>`, `xtrap`, `fnc_list` — **C: 70/100**
- [ ] ⬜ Full operator table (arithmetic, string, logical, comparison, date)
- [ ] ⬜ `.a.` / `.o.` / `.n.` boolean operators confirmed with examples
- [ ] ⬜ `$` string operator behavior confirmed
- [ ] ⬜ Expression precedence rules
- [ ] ⬜ All built-in functions documented (string, date, math, I/O, UI, crypto)

### 3.2 Database I/O Keywords
- [x] ✅ `open <table> lock N/W` — open table with no-lock or wait-lock — **C: 78/100**
- [x] ✅ `find F srch <key>` — keyed find — **C: 75/100**
- [x] ✅ `clr <table> rec` — clear/new record — **C: 72/100**
- [x] ✅ `del` / `dall` — delete record / delete all — **C: 70/100**
- [x] ✅ Field access via dot notation: `bksy.comp.name` (table.field) — **C: 85/100**
- [x] ✅ Locking: `LOCK_OWNER`, `REC_LOCK`, `UNLOCK` keywords — **C: 72/100**
- [ ] ⬜ Full find/seek operation set (first, last, next, prev, range)
- [ ] ⬜ Transaction keywords (BEGIN_TRAN, COMMIT, ROLLBACK — if they exist)
- [ ] ⬜ `USECODEBASE` vs. Btrieve mode switching fully documented
- [ ] ⬜ `REINDEX_DBF` behavior and when it's called

### 3.3 UI / Forms Keywords
- [x] ✅ `mount <screen> type S` — load and show form — **C: 75/100**
- [x] ✅ `wmount` / `load_form` / `set_focus` — windowed form loading — **C: 68/100**
- [x] ✅ `enter <field> [mask] [up] [acr] [pre/post <expr>] [upar <label>]` — field input with hooks — **C: 72/100**
- [x] ✅ `prg_hdr "..."` — program header/title — **C: 80/100**
- [x] ✅ `menu` — pop-up selection list — **C: 70/100**
- [ ] ⬜ Full `enter` keyword option set documented
- [ ] ⬜ All window management keywords (resize, move, close, modal/modeless)
- [ ] ⬜ Event model (how keystrokes, mouse events, and form events are handled)
- [ ] ⬜ `#WINFORM` pragma behavior vs. legacy mount

### 3.4 Reporting & Integration Keywords
- [x] ✅ `EXEC_RB`, `RTM_FN`, `REPORTNAME`, `USE_PRINTER`, `PRINT_TO_FILE` — **C: 78/100**
- [x] ✅ `OUTPUT_REPORT_DATA`, `UPDATE_REPORT_DATA`, `SETUP_REPORT_BUFF` — data pipeline setup — **C: 70/100**
- [x] ✅ `ENCRYPTSTR` / `DECRYPTSTR` — crypto keywords present — **C: 72/100**
- [x] ✅ `OLECALL` — COM/OLE integration — **C: 55/100**
- [x] ✅ `SQLCALL` — SQL execution keyword — **C: 55/100**
- [x] ✅ `GET_WEBSOURCE` — HTTP fetch — **C: 50/100**
- [x] ✅ `EXEC_TOP_WAIT` — shell execute with wait — **C: 60/100**
- [x] ✅ `PLAYWAV` — audio playback — **C: 65/100**
- [ ] ⬜ `SQLCALL` parameter format and connection target fully documented
- [ ] ⬜ `OLECALL` parameter format and COM object binding documented
- [ ] ⬜ `ENCRYPTSTR` algorithm reverse-engineered (see §14)
- [ ] ⬜ `ISJAVA` task queue interaction fully traced from TAS side

---

## 4. DATA DICTIONARY & DATABASE SCHEMA

### 4.1 Pervasive / Btrieve Infrastructure
- [x] ✅ Database engine: Pervasive PSQL (Btrieve) — **C: 92/100**
- [x] ✅ DDF files confirmed: FILE.DDF, FIELD.DDF, INDEX.DDF, ATTRIB.DDF, OCCURS.DDF, RELATE.DDF, TRIGGER.DDF, VIEW.DDF, PROC.DDF — **C: 90/100**
- [x] ✅ Workgroup (≤5 users) vs. Client/Server (6+) licensing — **C: 82/100**
- [x] ✅ Two ODBC engines: Transactional (EVO native) vs. Relational (external tools) — **C: 80/100**
- [ ] ⬜ INDEX.DDF fully parsed → primary keys for all 659 tables
- [ ] ⬜ RELATE.DDF fully parsed → foreign key relationships mapped
- [ ] ⬜ TRIGGER.DDF content extracted (any server-side triggers in use?)
- [ ] ⬜ PROC.DDF content extracted (any stored procedures in use?)

### 4.2 Schema Coverage
- [x] ✅ **659 tables** confirmed — **C: 95/100**
- [x] ✅ **24,113 fields** confirmed — **C: 95/100**
- [x] ✅ Mean 36.6 fields/table — **C: 95/100**
- [x] ✅ Largest tables: BKPRGLFL (664 fields), BKSLEVEL (422), BKAPINVL (390), BKPRMSTR (384) — **C: 90/100**
- [x] ✅ Full schema extracted to `samples/ddf/schema.md` (27k lines) and `schema.json` — **C: 92/100**
- [x] ✅ Field type codes documented: STRING, INTEGER, FLOAT, DATE, TIME, DECIMAL, MONEY, LOGICAL, NUMERIC, UBINARY — **C: 88/100**

### 4.3 Table Family Inventory
- [x] ✅ BK\* family (legacy backbone, largest group) — **C: 80/100**
  - BKAP\* (24 tables — Accounts Payable)
  - BKAR\* (27 tables — Accounts Receivable)
  - BKBM\* (10 tables — Bill of Materials)
  - BKCM\* (46 tables — Company Master)
  - BKDC\* (7 tables — Data Collection)
  - BKED\* (6 tables — EDI)
  - BKES\* (3 tables — Estimating)
  - BKGL\* (28 tables — General Ledger)
  - BKIC\* (16 tables — Inventory / Item Master)
  - BKMR\* (3 tables — MRP)
  - BKPI\* (7 tables — Physical Inventory)
  - BKPR\* (16 tables — Payroll)
  - BKSO\* (7 tables — Sales Orders)
  - BKSY\* (8 tables — System / Configuration)
- [x] ✅ MT\* family (second-gen master tables) — **C: 55/100**
- [x] ✅ WO\* family (30 tables — Work Orders) — **C: 65/100**
- [x] ✅ IS\* (tax, utilities, Java integration — ISJAVA table) — **C: 60/100**
- [x] ✅ AHSYLOG (security / user table) — **C: 72/100**
- [ ] ⬜ Full per-table narrative documentation (see §16 for checklist)
- [ ] ⬜ MT\* vs. BK\* scope difference confirmed (which company, which generation)
- [ ] ⬜ BKARHINV anomaly fully resolved (sub-folder table, now documented)
- [ ] ⬜ All 30 WO\* tables cross-referenced to Work Order module logic
- [ ] ⬜ Primary key confirmed for each of 659 tables (from INDEX.DDF)
- [ ] ⬜ Foreign key relationships mapped across module boundaries

### 4.4 Key Individual Tables (minimum needed for 90% goal)
- [x] ✅ `BKARCUST` — AR Customer master: 106 fields documented in `docs/04-data-dictionary/tier1-tables.md` — **C: 68/100**
- [x] ✅ `BKICMSTR` — Inventory Item master: 64 fields documented — **C: 68/100**
- [x] ✅ `BKSYMSTR` — System configuration master: 286 fields, key categories documented — **C: 62/100**
- [x] ✅ `AHSYLOG` — User security: all 23 fields documented — **C: 68/100**
- [x] ✅ `ISJAVA` — Java task queue: pattern confirmed; table NOT found in DDF (may be runtime-only or named differently) — **C: 55/100**
- [x] ✅ `BKLOGON` — Active session: all 10 fields documented — **C: 72/100**
- [x] ✅ `WORKORD` — Work order master: all 74 fields documented — **C: 72/100**
- [x] ✅ `WORKCHG` — Work order change log: all 25 fields documented — **C: 70/100**
- [x] ✅ `BKARCUST` — all fields with meaning, PKs — documented — **C: 68/100**
- [x] ✅ `BKICMSTR` — all fields with meaning — documented — **C: 68/100**
- [x] ✅ `BKSYMSTR` — major categories documented — **C: 62/100**
- [x] ✅ `BKAPVEND` — AP Vendor master: 26+ fields documented — **C: 65/100**
- [x] ✅ `BKGLCOA` — GL Chart of Accounts: 65 fields documented (replaces BKGLJRNL — that table is BKGLTRAN) — **C: 68/100**
- [x] ✅ `WORKORD` / `WORKCHG` — Work order header + change log — documented — **C: 70/100**
- [x] ✅ `BKSOX` / `BKSOXH` — Sales Order extract: 25 fields documented — **C: 65/100**
- [ ] ⬜ `BKPO????` — Purchase Order tables — all fields (BKAPPO + BKAPPOL identified but not field-level documented)
- [ ] ⬜ `BKPRMSTR` — Payroll master (384 fields) — all fields
- [ ] ⬜ `BKSLEVEL` — (422 fields, second-largest) — purpose and all fields
- [ ] ⬜ `BKPRGLFL` — (664 fields, largest) — purpose and all fields
- [ ] ⬜ `ISJAVA` table — locate actual table name in DDF and document all fields

---

## 5. SECURITY & LOGIN SYSTEM

- [x] ✅ Login form identified: `EVOMENU_LOGIN.DCY` (encrypted) — **C: 65/100**
- [x] ✅ `AHSYLOG` table structure: AHSY_USER_LEVL (role), AHSY_USER_MENU (starting menu 4-char), AHSY_USER_CTRL (control flag), AHSY_USER_ACCES_1..20 (20 module permission flags) — **C: 72/100**
- [x] ✅ Password storage: encrypted via `ENCRYPTSTR` TAS keyword; algorithm not decoded — **C: 55/100**
- [x] ✅ Session tracking via `BKLOGON` table — **C: 55/100**
- [x] ✅ Locking keywords: `LOCK_OWNER`, `REC_LOCK`, `UNLOCK` — **C: 65/100**
- [x] ✅ Password reset/change forms identified: `EVORESETPASS.DCY`, `EVOCHANGEPASS.DCY` — **C: 60/100**
- [x] ✅ Company selection form: `EVOMENU_SELCOMP.DCY` — **C: 60/100**
- [ ] ⬜ `AHSY_USER_ACCES_1..20` — exact index → module mapping (which flag controls which module)
- [ ] ⬜ `AHSY_USER_LEVL` — all role values and what each allows/denies
- [ ] ⬜ Password hashing algorithm reverse-engineered
- [ ] ⬜ `AHSY_USER_CTRL` flag values and their meaning
- [ ] ⬜ Multi-user locking: exact lock contention behavior (wait vs. skip vs. error)
- [ ] ⬜ `BKLOGON` all fields documented (session start time, workstation ID, etc.)
- [ ] ⬜ How WHOAMI.DBA ties into session/license validation

---

## 6. MENU SYSTEM & NAVIGATION

- [x] ✅ 554 menu codes extracted from `.RUN` string dump — **C: 88/100**
- [x] ✅ Menu code format: `XX-Y[-Z]` (MODULE-LEVEL1[-LEVEL2]) — **C: 85/100**
- [x] ✅ LEVEL1 convention: A = master data, B–Z = activities/inquiries/reports — **C: 78/100**
- [x] ✅ 38 modules with menu codes identified — **C: 85/100**
- [x] ✅ Top modules by operation count: SO(48), IN(40), SM(34), DE(33), WO(31), PO(29), PR(29), UT(20), AP(19), RO(19) — **C: 88/100**
- [x] ✅ Full AP menu codes listed (AP-A through AP-U, with descriptions) — **C: 82/100**
- [x] ✅ Full AR menu codes listed (AR-A through AR-S, with descriptions) — **C: 82/100**
- [x] ✅ 636 help topics per menu code extracted from CHM — **C: 90/100**
- [x] ✅ 205 "help-only" codes identified (CHM but not in RUN dump) — **C: 80/100**
- [x] ✅ Master index CSV joining menu codes ↔ help topics ↔ forms — **C: 82/100**
- [ ] ⬜ Menu tree storage location confirmed (EVOERPMENU.DCY vs. DB table — currently unknown)
- [ ] ⬜ All 554 menu codes mapped to their implementing `.RWN`/`.RUN` file
- [ ] ⬜ All 554 menu codes mapped to their `.DFM` form
- [ ] ⬜ 205 help-only codes explained (removed features, optional modules, or RWN-only additions)
- [ ] ⬜ Menu code → module → table chain fully traced for all 38 modules
- [ ] ⬜ Module meanings confirmed for: DE, MM, IS, PL, DI, AB, AC, FO, HH (some ambiguous)

---

## 7. MODULES — FUNCTIONAL DOCUMENTATION

Each module needs: menu codes, implementing files, UI forms, database tables, business logic summary.
Target for "understood" = C: 75+ on all items below.

### 7.1 Accounts Receivable (AR)
- [x] ✅ Menu codes listed (AR-A through AR-S) — **C: 72/100**
- [x] ✅ Forms inventoried (T7AR\*.DFM) — **C: 70/100**
- [x] ✅ Tables identified: BKAR\* (27 tables) — **C: 55/100**
- [ ] ⬜ Business logic for each AR-\* operation documented
- [ ] ⬜ BKARCUST all fields with meaning
- [ ] ⬜ AR aging calculation logic traced
- [ ] ⬜ Payment application workflow fully traced

### 7.2 Accounts Payable (AP)
- [x] ✅ Menu codes listed (AP-A through AP-U) — **C: 72/100**
- [x] ✅ Forms inventoried (T7AP\*.DFM) — **C: 70/100**
- [x] ✅ Tables: BKAP\* (24 tables) — **C: 55/100**
- [x] ✅ Source files: Bkaph.SRC, Bkapha.SRC analyzed — **C: 65/100**
- [ ] ⬜ Voucher entry workflow fully traced
- [ ] ⬜ Check printing workflow traced (AP-M through AP-P)
- [ ] ⬜ BKAPCUST all fields with meaning

### 7.3 Inventory (IN)
- [x] ✅ Menu codes listed (40 operations) — **C: 72/100**
- [x] ✅ Forms inventoried (T7IN\*.DFM) — **C: 70/100**
- [x] ✅ Tables: BKIC\* (16 tables), MTICMSTR identified — **C: 55/100**
- [ ] ⬜ Item master (BKICMSTR) all fields documented
- [ ] ⬜ FIFO/LIFO/average cost layer logic traced
- [ ] ⬜ Physical inventory workflow (PI module) traced end-to-end
- [ ] ⬜ Lot tracking / serial number tracking documented (if present)

### 7.4 Sales Orders (SO)
- [x] ✅ Menu codes listed (48 operations — largest module) — **C: 72/100**
- [x] ✅ Forms inventoried (T7SO\*.DFM) — **C: 70/100**
- [x] ✅ Tables: BKSO\* (7 tables identified) — **C: 50/100**
- [ ] ⬜ Order entry workflow (SO-B) fully traced
- [ ] ⬜ Order → shipping → invoice chain traced
- [ ] ⬜ All BKSO\* tables with fields documented
- [ ] ⬜ Sales Analysis (SA module) tables and calculations

### 7.5 Purchase Orders (PO)
- [x] ✅ Menu codes listed (29 operations) — **C: 72/100**
- [x] ✅ Forms inventoried (T7PO\*.DFM) — **C: 70/100**
- [ ] ⬜ PO entry → receipt → AP voucher chain traced
- [ ] ⬜ All BKPO\* tables with fields documented

### 7.6 Work Orders (WO)
- [x] ✅ Menu codes listed (31 operations) — **C: 72/100**
- [x] ✅ Forms inventoried (T7WO\*.DFM) — **C: 70/100**
- [x] ✅ Tables: WO\* (30 tables) — **C: 50/100**
- [x] ✅ Source files: BKAWLB.SRC (Work Order labor logic analyzed) — **C: 62/100**
- [ ] ⬜ Work order life cycle (create → release → labor entry → close) fully traced
- [ ] ⬜ All 30 WO\* tables with fields documented
- [ ] ⬜ WORKORD + WORKCHG relationship and key fields

### 7.7 General Ledger (GL)
- [x] ✅ Menu codes listed (16 operations) — **C: 72/100**
- [x] ✅ Tables: BKGL\* (28 tables) — **C: 50/100**
- [ ] ⬜ Journal entry creation workflow traced
- [ ] ⬜ Period-end close process traced
- [ ] ⬜ All BKGL\* tables with fields documented
- [ ] ⬜ Chart of accounts structure documented

### 7.8 Bill of Materials (BM)
- [x] ✅ Menu codes listed — **C: 65/100**
- [x] ✅ Tables: BKBM\* (10 tables) — **C: 50/100**
- [x] ✅ BOM Tree analysis tool documented (BOMTREE.RWN) — **C: 60/100**
- [ ] ⬜ Multi-level BOM explosion logic traced
- [ ] ⬜ All BKBM\* tables with fields documented

### 7.9 MRP / Manufacturing Requirements Planning (MR)
- [x] ✅ Menu codes listed (12 operations) — **C: 65/100**
- [x] ✅ Tables: BKMR\* (3 tables) — **C: 45/100**
- [x] ✅ Source file: BKMRF.SRC (MRP logic analyzed) — **C: 62/100**
- [ ] ⬜ Full MRP calculation cycle traced
- [ ] ⬜ All BKMR\* tables with fields documented

### 7.10 Routing (RO)
- [x] ✅ Menu codes listed (19 operations) — **C: 65/100**
- [x] ✅ Source file: BKROA.SRC analyzed — **C: 60/100**
- [ ] ⬜ Routing record structure documented
- [ ] ⬜ Routing → Work Order link traced

### 7.11 Payroll (PR)
- [x] ✅ Menu codes listed (29 operations) — **C: 65/100**
- [x] ✅ Tables: BKPR\* (16 tables); BKPRMSTR (384 fields — largest practical table) — **C: 50/100**
- [ ] ⬜ BKPRMSTR all 384 fields documented with meaning
- [ ] ⬜ Payroll calculation cycle traced
- [ ] ⬜ W-2 / 1099 generation traced
- [ ] ⬜ Tax table structure documented

### 7.12 Data Collection (DC)
- [x] ✅ Menu codes listed — **C: 65/100**
- [x] ✅ Files: EvoDC\*.RWN, EvoDCmenu.RWN, EvoDCsetup.RWN cataloged — **C: 70/100**
- [x] ✅ Tables: BKDC\* (7 tables) — **C: 55/100**
- [x] ✅ Source file: BKDCA.SRC analyzed — **C: 65/100**
- [x] ✅ Handheld forms: T7HH\*, label tables BKDC\* — **C: 60/100**
- [ ] ⬜ Full DC workflow (scanner → table entry → WO update) traced
- [ ] ⬜ All BKDC\* tables with fields documented

### 7.13 Scheduling / Capacity (SC)
- [x] ✅ Menu codes listed — **C: 60/100**
- [ ] ⬜ Full scheduling algorithm documented
- [ ] ⬜ Capacity planning tables identified and fields documented

### 7.14 Physical Inventory (PI)
- [x] ✅ Menu codes listed — **C: 65/100**
- [x] ✅ Tables: BKPI\* (7 tables) — **C: 55/100**
- [ ] ⬜ PI count cycle (freeze → count → reconcile) fully traced

### 7.15 Labor / Time & Attendance (LW / LA)
- [x] ✅ Menu codes listed — **C: 62/100**
- [x] ✅ Source file: BKLME.SRC analyzed — **C: 60/100**
- [ ] ⬜ Time entry → work order charge chain fully traced

### 7.16 EDI (ED)
- [x] ✅ Tables: BKED\* (6 tables) — **C: 45/100**
- [ ] ⬜ EDI transaction set support confirmed
- [ ] ⬜ Inbound/outbound EDI pipeline traced

### 7.17 Estimating (ES)
- [x] ✅ Tables: BKES\* (3 tables) — **C: 45/100**
- [ ] ⬜ Estimating-to-quote-to-order workflow traced

### 7.18 Remaining Modules (not yet deeply documented)
The following modules have menu codes and forms inventoried but no deep logic documentation:

- [ ] ⬜ **AB** — purpose unclear; no deep doc
- [ ] ⬜ **AC** — purpose unclear; no deep doc
- [ ] ⬜ **AM** — Asset Management (17 ops) — forms inventoried only
- [ ] ⬜ **AD** — purpose unclear; no deep doc
- [ ] ⬜ **CM** — Customer Management / CRM — forms inventoried only
- [ ] ⬜ **CP** — purpose unclear; no deep doc
- [ ] ⬜ **CR** — Credit / Collections — forms inventoried only
- [ ] ⬜ **CS** — Customer Service (16 ops) — forms inventoried only
- [ ] ⬜ **DE** — Data Entry (33 ops, 2nd largest) — forms inventoried only
- [ ] ⬜ **DI** — purpose unclear; no deep doc
- [ ] ⬜ **EX** — Export / data exchange — forms inventoried only
- [ ] ⬜ **FA** — Fixed Assets — forms inventoried only
- [ ] ⬜ **FL** — purpose unclear; no deep doc
- [ ] ⬜ **FO** — Features & Options (EvoFNO) — forms inventoried only
- [ ] ⬜ **FP** — purpose unclear; no deep doc
- [ ] ⬜ **HH** — Handheld / Data Collection terminals — forms inventoried only
- [ ] ⬜ **IC** — Inventory Control (sub-area of IN?) — forms inventoried only
- [ ] ⬜ **IM** — Import / data loading — forms inventoried only
- [ ] ⬜ **IS** — purpose unclear; no deep doc
- [ ] ⬜ **JC** — Job Costing (18 ops) — forms inventoried only
- [ ] ⬜ **LC** — Lot Control — forms inventoried only
- [ ] ⬜ **LM** — Labor Management — forms inventoried only
- [ ] ⬜ **LO** — purpose unclear; no deep doc
- [ ] ⬜ **MA** — purpose unclear; no deep doc
- [ ] ⬜ **MM** — Main Menu / Master Maintenance — forms inventoried only
- [ ] ⬜ **PC** — Production Control — forms inventoried only
- [ ] ⬜ **PL** — Planning — forms inventoried only
- [ ] ⬜ **PS** — Product Structure / BOM variant — forms inventoried only
- [ ] ⬜ **QC** — Quality Control — forms inventoried only
- [ ] ⬜ **QT** / **QU** — Quoting — forms inventoried only
- [ ] ⬜ **RF** — purpose unclear; no deep doc
- [ ] ⬜ **RM** — Return Material — forms inventoried only
- [ ] ⬜ **RT** — purpose unclear; no deep doc
- [ ] ⬜ **SA** — Sales Analysis (13 ops) — forms inventoried only
- [ ] ⬜ **SB** — purpose unclear; no deep doc
- [ ] ⬜ **SD** — Standard Data (12 ops) — forms inventoried only
- [ ] ⬜ **SH** — Shipping (16 ops) — forms inventoried only
- [ ] ⬜ **SL** — purpose unclear; no deep doc
- [ ] ⬜ **SM** — System Maintenance (34 ops, 3rd largest) — forms inventoried only
- [ ] ⬜ **SR** — Service / Repair — forms inventoried only
- [ ] ⬜ **SU** — Setup — forms inventoried only
- [ ] ⬜ **SY** — System — forms inventoried only
- [ ] ⬜ **TA** — purpose unclear; no deep doc
- [ ] ⬜ **UM** — User Maintenance — forms inventoried only
- [ ] ⬜ **UP** — Update / patch — forms inventoried only
- [ ] ⬜ **US** — User Settings — forms inventoried only
- [ ] ⬜ **UT** — Utilities (20 ops) — forms inventoried only
- [ ] ⬜ **WC** — Work Center — forms inventoried only
- [ ] ⬜ **YS** — purpose unclear; no deep doc

---

## 8. REPORTING ENGINE (REPORTBUILDER / RTM)

- [x] ✅ Engine identified: Nevrona ReportBuilder (stand-alone: `RBDsgnr.exe`) — **C: 88/100**
- [x] ✅ TPF0 binary format documented (magic, component tree, key classes) — **C: 80/100**
- [x] ✅ TAS-to-report data pipeline: SETUP_REPORT_BUFF → OUTPUT_REPORT_DATA → EXEC_RB — **C: 72/100**
- [x] ✅ 899+ RTM files inventoried — **C: 85/100**
- [x] ✅ `rtm_callers.csv` cross-reference generated — **C: 70/100**
- [x] ✅ PDF output path: `C:\ISTS\PDFS\` — **C: 75/100**
- [ ] ⬜ All 899 RTM files parsed to extract data-field bindings
- [ ] ⬜ RTM ↔ module call mapping complete (which SRC function calls which RTM)
- [ ] ⬜ Report parameter passing fully documented (how TAS passes filters/date ranges to RTM)
- [ ] ⬜ Print-to-file vs. print-to-screen vs. print-to-printer mode switching documented
- [ ] ⬜ Email/PDF archiving workflow traced
- [ ] ⬜ `EVOReports\` share folder purpose confirmed (stored report output?)
- [ ] ⬜ All report templates for each module listed by name + purpose

---

## 9. PLATFORM SUBSYSTEMS

### 9.1 EvoNotes (CRM / Notes)
- [x] ✅ Files: EvoNotes.RWN, EvoNotesARCH.RWN, EvoNoteSearch.RWN, EvoNotesPrt.RWN, EvoNotesRpt.RWN — **C: 72/100**
- [x] ✅ Table: ISNOTES — **C: 55/100**
- [ ] ⬜ ISNOTES all fields documented
- [ ] ⬜ Note creation / search workflow fully traced
- [ ] ⬜ Note archiving logic traced

### 9.2 EvoScheduler
- [x] ✅ Files: EvoScheduler.RWN, EvoSched.RWN, EvoSchedSetup.RWN — **C: 70/100**
- [ ] ⬜ Scheduler job table name confirmed (not found in 659-table inventory)
- [ ] ⬜ Schedule table all fields documented
- [ ] ⬜ Job execution mechanism traced (how scheduler triggers a program)

### 9.3 EvoService (Windows Service)
- [x] ✅ Files: EvoService.RWN, EvoServiceSetup.RWN, EvoServiceRemove.RWN — **C: 68/100**
- [ ] ⬜ Service registration mechanism traced
- [ ] ⬜ Service ↔ Scheduler interaction documented

### 9.4 EvoBackup
- [x] ✅ Files: EvoERPbackup.RWN; uses zipdll/unzdll — **C: 65/100**
- [ ] ⬜ Backup target paths and file selection logic documented
- [ ] ⬜ Restore procedure documented

### 9.5 EvoLinks (Document Attachments)
- [x] ✅ Files: EvoLinks.RWN, EvoLinkCVT.RWN — **C: 62/100**
- [ ] ⬜ Attachment storage schema (DB table + LinkDoc\ folder) confirmed
- [ ] ⬜ DB table for link mapping identified and all fields documented
- [ ] ⬜ Attach / view / delete workflow traced

### 9.6 EvoFNO (Features & Options Configurator)
- [x] ✅ Files: EvoFNO.RWN, EvoFNOSO.RWN, EvoFNOPO.RWN, EvoFNOWO.RWN — **C: 62/100**
- [ ] ⬜ FNO table structure documented
- [ ] ⬜ FNO interaction with SO/PO/WO modules traced

### 9.7 EvoUpdate (In-App Patching)
- [x] ✅ Files: EvoUpdate.RWN, EvoERPupd.RWN, EvoPRupd.RWN, EvoUPDSetup.RWN, UPDTP7.EXE — **C: 70/100**
- [x] ✅ Update mechanism: reads FILE\*.UPD manifests, applies schema migrations — **C: 65/100**
- [ ] ⬜ Full update pipeline traced step-by-step
- [ ] ⬜ UPDTP7.EXE role (binary patcher?) documented

### 9.8 EvoDrillDown / Analysis Tools
- [x] ✅ Files: EvoERPDrillM.RWN, CashFlow, CommissionRpt, BOMTree, EditBOMTree, CRM Dashboard — **C: 60/100**
- [ ] ⬜ CashFlow calculation logic documented
- [ ] ⬜ CRM Dashboard data sources traced
- [ ] ⬜ Commission calculation logic traced

### 9.9 Google Calendar Integration
- [x] ✅ Files: CALREM.RWN, CALREMGC.DFM — **C: 55/100**
- [ ] ⬜ OAuth / API credential storage traced
- [ ] ⬜ Calendar sync logic documented

---

## 10. JAVA INTEGRATION (EvoPVT.jar)

- [x] ✅ JAR analyzed: 1.8 MB JavaFX application — **C: 78/100**
- [x] ✅ Main-Class: `com.evoerp.TASKS.sql.Main$WindowsUtils` — **C: 90/100**
- [x] ✅ Connection: Pervasive JDBC driver; SQL over Btrieve — **C: 75/100**
- [x] ✅ Integration pattern: ISJAVA task-queue table; TAS writes params, Java reads and executes — **C: 75/100**
- [x] ✅ JavaFX UI components: SplashScreen, TabularView (CSV export), CalendarView, LookupPane — **C: 72/100**
- [x] ✅ Data layer: hand-rolled SQL builder (Expression, Field, Clause, etc.) — **C: 70/100**
- [x] ✅ Mail & localization: SMTP sender + resource-bundle i18n — **C: 65/100**
- [x] ✅ `ISJAVA` table: TAS writes task ID + params; Java polls, executes, writes result — **C: 72/100**
- [ ] ⬜ All ISJAVA task command IDs documented with their action
- [ ] ⬜ ISJAVA all fields documented
- [ ] ⬜ Java connection parameters source confirmed (taspro7.ini vs. registry vs. .properties file)
- [ ] ⬜ All JavaFX command-line sub-tasks enumerated
- [ ] ⬜ CSV export logic fully traced (which data pipelines, column mapping)

---

## 11. ODBC / EXTERNAL CONNECTIVITY

- [x] ✅ DSN-based connection: `DSN=DBA;` (preferred) — **C: 88/100**
- [x] ✅ Prerequisites: Pervasive client runtime + 32-bit ODBC DSN — **C: 88/100**
- [x] ✅ Bitness trap: 32-bit and 64-bit ODBC have separate registry hives; EVO is 32-bit — **C: 90/100**
- [x] ✅ ODBC admin paths documented (System32 = 64-bit, SysWOW64 = 32-bit) — **C: 90/100**
- [x] ✅ Working C# example confirmed (`System.Data.Odbc`, SELECT from WORKCHG) — **C: 85/100**
- [x] ✅ Two ODBC engines: Transactional (Btrieve native) vs. Relational (SQL joins) — **C: 80/100**
- [x] ✅ Schema queryable via X$File / X$Field Pervasive system views — **C: 85/100**
- [ ] ⬜ DSN connection string all parameters documented
- [ ] ⬜ Read/write capability confirmed via Transactional engine (can you INSERT/UPDATE via ODBC?)
- [ ] ⬜ Table locking behavior when reading via ODBC while EVO has records open

---

## 12. CUSTOMIZATION MODULES (J7\*)

- [x] ✅ 37 J7\* customer-specific modules inventoried — **C: 78/100**
- [x] ✅ 109 files cataloged (DFM + RWN pairs) — **C: 78/100**
- [x] ✅ Examples: J7AIJCG, J7BEFWebInv, J7CCCutSheet, J7CRSOW, J7DCMatLabels, J7EIMDCRev, J7HH\* — **C: 72/100**
- [x] ✅ DFM forms analyzed (UI layouts visible) — **C: 65/100**
- [ ] ⬜ J7\* prefix meaning confirmed (customer initials? i2 Systems internal?)
- [ ] ⬜ Each J7 module's business purpose fully documented
- [ ] ⬜ J7\* database tables identified (any custom tables created by J7 modules?)
- [ ] ⬜ J7 RWN logic (blocked by encryption — see §14)
- [ ] ⬜ J7\* modules' interaction with core EVO tables documented

---

## 13. BUSINESS WORKFLOWS / RECIPES

These are end-to-end process traces. Currently 0 workflow recipes are fully documented.

### 13.1 Core Accounting Workflows
- [ ] ⬜ **Customer invoice creation** — AR entry to GL posting
- [ ] ⬜ **Cash receipts** — payment entry, application, bank deposit
- [ ] ⬜ **Vendor invoice entry** — AP voucher through GL posting
- [ ] ⬜ **Check run** — AP selection through check printing
- [ ] ⬜ **Month-end close** — AR/AP/GL reconciliation and period lock
- [ ] ⬜ **Year-end close** — payroll, 1099, W-2, purge cycle
- [ ] ⬜ **GL journal entry** — manual entry, posting, reversal

### 13.2 Inventory & Manufacturing Workflows
- [ ] ⬜ **New item setup** — item master entry, BOM, routing
- [ ] ⬜ **Purchase order** — creation, receipt, AP matching
- [ ] ⬜ **Work order lifecycle** — creation, material release, labor entry, close
- [ ] ⬜ **MRP run** — planning input, calculation, WO/PO suggestions
- [ ] ⬜ **Physical inventory count** — freeze, count entry, variance approval
- [ ] ⬜ **Inventory adjustment** — manual quantity/cost adjustment
- [ ] ⬜ **Sales order** — entry, pick, ship, invoice

### 13.3 Payroll Workflows
- [ ] ⬜ **Time entry** — labor hours entry through pay period
- [ ] ⬜ **Payroll calculation** — gross to net, deductions
- [ ] ⬜ **Check printing** — direct deposit, live checks
- [ ] ⬜ **Tax filing** — quarterly 941, W-2, 1099 generation

### 13.4 System Administration Workflows
- [ ] ⬜ **New user setup** — AHSYLOG entry, access flags, starting menu
- [ ] ⬜ **New company creation** — directory setup, DDF copy, initialization
- [ ] ⬜ **Backup / restore** — EvoBackup operation and restore path
- [ ] ⬜ **Software update** — EvoUpdate apply process
- [ ] ⬜ **Period-end archiving** — archive + purge old transaction tables
- [ ] ⬜ **ODBC DDF build** — required before Java tools can connect

---

## 14. ENCRYPTION & REVERSE ENGINEERING BLOCKERS

These are the primary obstacles to reaching 90%+ confidence on module logic.

- [x] 🔄 `.RWN` / `.DCY` encryption investigated — **C: 25/100**
  - High entropy from offset 0; no magic bytes; license-bound key suspected
  - Twofish-CFB suspected but not confirmed
  - Block-0 partially analyzed; key not recovered
  - [ ] ⬜ Identify encryption algorithm (static analysis of tp7runtime.exe decrypt routine)
  - [ ] ⬜ Locate key derivation code in tp7runtime.exe (filename-based? license-serial-based? fixed?)
  - [ ] ⬜ Decrypt one `.DCY` file and confirm structure
  - [ ] ⬜ Decrypt one `.RWN` file and read bytecode
  - [ ] ⬜ Build automated decryptor for all `.RWN` files
  - [ ] ⬜ Build automated decryptor for all `.DCY` files
- [ ] ⬜ `ENCRYPTSTR` algorithm reverse-engineered (password hashing, string crypto in TAS)
- [ ] ⬜ `WHOAMI.DBA` 35-byte format decoded
- [ ] ⬜ `CHMHELP.EVO` 35-byte format decoded
- [ ] ⬜ Menu tree format inside `EVOERPMENU.DCY` decoded (once decryption solved)
- [ ] ⬜ `.RUN` (TAS Pro 6) binary structure fully decoded (bytecode, not just strings)

---

## 15. HELP SYSTEM (EvoHELP.CHM)

- [x] ✅ CHM decompiled: 779 topics extracted — **C: 95/100**
- [x] ✅ 636 per-menu-code topics — **C: 92/100**
- [x] ✅ 90 conceptual chapter topics — **C: 88/100**
- [x] ✅ 53 meta topics — **C: 85/100**
- [x] ✅ All 14 CHM categories processed — **C: 90/100**
- [x] ✅ Menu-to-help mapping CSV generated — **C: 88/100**
- [ ] ⬜ 35 recipe stubs — daily workflow pages (login, AR/AP/PO workflows, manufacturing, month-end, admin)
- [ ] ⬜ 45 module stubs — less-documented modules (full list in `research/TODO_help_pages.md` Section C)
- [ ] ⬜ 8 cross-cutting topic stubs (encryption overview, DCY/RWN decryption, SRC deep-dive, INI reference, reporting pipeline, field-search feature)
- [ ] ⬜ Per-table schema pages (one page per table with all fields and meaning)
- [ ] ⬜ Per-form pages (one page per DFM with field labels, purpose, and linked table)
- [ ] ⬜ Per-report pages (one page per RTM with data sources, parameters, output columns)

---

## 16. PER-TABLE SCHEMA PAGES

One documentation page needed per table with: all fields, types, meanings, PK, FKs, which module uses it.

**Status:** Schema extracted (field names + types) but narrative documentation = 0 tables complete.

### Priority Tier 1 — Core Transaction Tables (must reach C: 80+ to hit 90% goal)
- [ ] ⬜ BKARCUST — AR Customer master
- [ ] ⬜ BKARINVH — AR Invoice header
- [ ] ⬜ BKARINVL — AR Invoice detail
- [ ] ⬜ BKARPMT — AR Payment
- [ ] ⬜ BKAPCUST — AP Vendor master
- [ ] ⬜ BKAPINVH — AP Invoice header
- [ ] ⬜ BKAPINVL — AP Invoice detail (390 fields)
- [ ] ⬜ BKAPCHKH — AP Check header
- [ ] ⬜ BKICMSTR — Inventory Item master
- [ ] ⬜ BKGLACCT — GL Account master
- [ ] ⬜ BKGLJRNL — GL Journal entry
- [ ] ⬜ WORKORD — Work Order header
- [ ] ⬜ WORKCHG — Work Order detail / charges
- [ ] ⬜ BKBMMSTR — BOM master
- [ ] ⬜ BKBMCOMP — BOM components
- [ ] ⬜ AHSYLOG — User security
- [ ] ⬜ ISJAVA — Java task queue
- [ ] ⬜ BKLOGON — Active sessions
- [ ] ⬜ BKSYMSTR — System configuration

### Priority Tier 2 — Supporting Tables
- [ ] ⬜ All remaining BKAP\* (24 tables)
- [ ] ⬜ All remaining BKAR\* (27 tables)
- [ ] ⬜ All remaining BKGL\* (28 tables)
- [ ] ⬜ All remaining BKIC\* (16 tables)
- [ ] ⬜ All remaining WO\* (30 tables)
- [ ] ⬜ All remaining BKPR\* (16 tables) including BKPRMSTR (384 fields)
- [ ] ⬜ All remaining BKBM\* (10 tables)
- [ ] ⬜ All remaining BKCM\* (46 tables)
- [ ] ⬜ All remaining BKSO\* (7 tables)
- [ ] ⬜ All remaining BKDC\* (7 tables)
- [ ] ⬜ All remaining IS\* tables
- [ ] ⬜ BKSLEVEL (422 fields — second largest)
- [ ] ⬜ BKPRGLFL (664 fields — largest)

### Priority Tier 3 — Remaining 365 misc tables
- [ ] ⬜ All MT\* tables
- [ ] ⬜ All ED\* (EDI) tables
- [ ] ⬜ All PI\* (Physical Inventory) tables
- [ ] ⬜ All ES\* (Estimating) tables
- [ ] ⬜ All remaining tables not covered above

---

## 17. PER-FORM DOCUMENTATION

One page per DFM: field labels, control types, linked table(s), menu code(s) that open it.

- [x] ✅ All 1,109 forms inventoried (name, size, control count) — **C: 85/100**
- [x] ✅ DFM summary CSV (`samples/dfm_parsed/dfm_summary.csv`) — **C: 82/100**
- [ ] ⬜ Form-to-menu-code mapping complete (which DFM opens for each menu code)
- [ ] ⬜ Form-to-table mapping (which tables does each form read/write)
- [ ] ⬜ Per-form narrative documentation (field labels + purpose) for all 1,109 forms

---

## 18. PER-REPORT DOCUMENTATION

- [x] ✅ 899+ RTM files inventoried — **C: 85/100**
- [x] ✅ `rtm_callers.csv` cross-reference generated — **C: 70/100**
- [ ] ⬜ All 899 RTM files parsed for: data pipeline fields, sub-report structure, label texts
- [ ] ⬜ Each report mapped to: calling SRC function + module + menu code
- [ ] ⬜ Report parameter documentation (what filters/date ranges each report accepts)

---

## 19. INFRASTRUCTURE & DEPLOYMENT

- [x] ✅ Server: `i2s109-solidcrm` — **C: 90/100**
- [x] ✅ Client install path: `C:\ISTS\` — **C: 90/100**
- [x] ✅ Data share: `\\i2s109-solidcrm\DBAMFG$\` — **C: 90/100**
- [x] ✅ Pervasive license types: Workgroup (≤5) vs. Client/Server (6+) — **C: 80/100**
- [x] ✅ Update/deployment: EvoUpdate in-app + Robocopy possible — **C: 68/100**
- [ ] ⬜ Full server topology: which services run on i2s109-solidcrm, ports, Pervasive engine config
- [ ] ⬜ Workstation setup procedure fully documented (what gets installed, what's configured)
- [ ] ⬜ Multi-site / Terminal Server / Citrix deployment variants documented
- [ ] ⬜ Pervasive License Administrator utility operation documented
- [ ] ⬜ Robocopy deployment procedure fully traced

---

## 20. MASTER CONFIDENCE SUMMARY

| Area | Current C: | Target C: | Gap | Last Updated |
|---|---|---|---|---|
| System Architecture | 75 | 90 | 15 | 2026-06-11 |
| Boot Sequence | 68 | 85 | 17 | 2026-06-11 |
| File Formats — SRC | 80 | 90 | 10 | 2026-06-11 |
| File Formats — DFM | 87 | 90 | 3 | 2026-06-11 |
| File Formats — RWN/DCY | 25 | 70 | 45 ⚠️ | 2026-06-11 |
| File Formats — RTM | 78 | 88 | 10 | 2026-06-11 |
| File Formats — Btrieve | 72 | 85 | 13 | 2026-06-11 |
| TAS 4GL Language | 75 | 92 | 17 | 2026-06-11 |
| Database Schema (structure) | 90 | 95 | 5 | 2026-06-11 |
| Database Schema (field meaning) | **48** | 88 | **40** ↑ | 2026-06-11 |
| Security / Login | 65 | 85 | 20 | 2026-06-11 |
| Menu System | 78 | 90 | 12 | 2026-06-11 |
| Module: AR | **72** | 85 | **13** ↑ | 2026-06-11 |
| Module: AP | **78** | 85 | **7** ↑ | 2026-06-11 |
| Module: IN/Inventory | **68** | 85 | **17** ↑ | 2026-06-11 |
| Module: SO | **65** | 85 | **20** ↑ | 2026-06-11 |
| Module: PO | 60 | 85 | 25 | 2026-06-11 |
| Module: WO | **72** | 85 | **13** ↑ | 2026-06-11 |
| Module: GL | **65** | 85 | **20** ↑ | 2026-06-11 |
| Module: BM/MRP | **72** | 80 | **8** ↑ | 2026-06-11 |
| Module: RO/Routing | **75** | 85 | **10** ↑ | 2026-06-11 |
| Module: DC/Data Collection | **78** | 82 | **4** ↑ | 2026-06-11 |
| Module: PR/Payroll | 50 | 80 | 30 | 2026-06-11 |
| Modules: Remaining ~35 | 35 | 75 | 40 ⚠️ | 2026-06-11 |
| Reporting Engine | 75 | 88 | 13 | 2026-06-11 |
| Platform Subsystems | 65 | 82 | 17 | 2026-06-11 |
| Java Integration | 73 | 85 | 12 | 2026-06-11 |
| ODBC Connectivity | 85 | 92 | 7 | 2026-06-11 |
| Customizations (J7\*) | 65 | 80 | 15 | 2026-06-11 |
| Business Workflows | **62** | 85 | **23** ↑ | 2026-06-11 |
| Encryption / RWN Decryption | 20 | 60 | 40 ⚠️ | 2026-06-11 |
| Per-Table Narrative Docs | **48** | 88 | **40** ↑ | 2026-06-11 |
| PROJECT-STRUCTURE.md | **72** | 90 | **18** ↑ | 2026-06-11 |
| HELP-RESOURCES.md | **65** | 90 | **25** ↑ | 2026-06-11 |

### Critical Path to 90% Goal

The biggest gaps blocking the 90% target, in order of impact:

1. **Per-table field meaning documentation** (gap: 73) — 659 tables × full field semantics
2. **Business workflow recipes** (gap: 80) — no end-to-end processes yet documented
3. **RWN/DCY decryption** (gap: 45) — blocks all module logic; highest leverage single unlock
4. **Remaining ~35 modules** (gap: 40) — DE, SM, AM, FA, JC, SA, SH, CS, etc.
5. **TAS 4GL language gaps** (gap: 17) — operators, full grammar, scope rules
6. **Security model detail** (gap: 23) — access flag mapping, password algorithm
7. **Module logic for core 7** (gaps: 20–30 each) — AR, AP, IN, SO, PO, WO, GL

---

*Last updated: 2026-06-11*
*Document location: `EVO-DECOMPILE-TODO.md` at workspace root*
