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
- [x] ✅ Full boot chain traced: `EvoERP.lnk → StartEvo.exe → tp7runtime.exe → EvoERPmenu.rwn → EVOMENU_LOGIN → EVOMENU_SELCOMP → EvoERPmenu.RWN builds module tree → EVOMENU_RUNPRG dispatches to module` — **C: 90/100**
- [x] ✅ `StartEvo.exe` role: checks runtime, reads `taspro7.ini`, spawns tp7runtime.exe — **C: 60/100**
  - Gap: exact command-line arguments passed to tp7runtime.exe not confirmed
- [x] ✅ `taspro7.ini` keys documented: `DataDictPath`, `DfltRunPrg`, `MultiUser`, `DefaultPath`, `Titlebar`, `HelpFileName` — **C: 80/100**
- [x] ✅ Bootstrap RWNs identified: `suwin6.dcy`, `suwin7.dcy`, `suwin6t.rwn`, `suwin7t.rwn` — **C: 55/100**
  - Gap: what these actually do before EvoERPmenu.rwn loads is not confirmed
- [x] ✅ Per-workstation state files cataloged: `taspro7.ini`, `EvoSettings.INI`, `WHOAMI.DBA`, `CHMHELP.EVO`, `RBuilder.ini`, `DFM/`, `PDFS/` — **C: 68/100**
- [x] ✅ `EvoSettings.INI` fully decoded (2026-06-17) — **C: 88/100**
  - Sections: [Users] global prefs, [User:NAME] per-user, [EMAIL CO# X User:Y] email SMTP+templates, per-module [ARA]/[SOA] etc., [HOT BUTTONS] × 6
  - Key flags: SAVE ACCESS, EvoorClassicScreen, Converted, OpenListXXX, Reminder, CheckForUpdates, TopMost
  - Email creds stored in plaintext; booleans use `.T.`/`.F.` TAS Pro syntax in plain INI
  - Full detail in `docs/01-architecture/overview.md`
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
- [x] ✅ Format: Twofish-CFB encrypted binary; decoder in tp7runtime.exe — **C: 80/100**
- [x] ✅ High entropy from offset 0; no readable strings in first 4 KB — **C: 90/100**
- [x] ✅ Paired with same-basename `.DFM` (layout ↔ logic) — **C: 90/100**
- [x] ✅ Encryption algorithm: Twofish-192-CFB; key K_B = `a898d21e2fd6ca294026e5d633d9047f91f7ed35` — **C: 100/100**
  - Key derivation: SHA1(runtime_passphrase)[0:20] + 4 zeros; passphrase "mabufoju" was WRONG
  - IV param always 0; P_initial = Encrypt_K(zeros); body P_start = K0 = Encrypt_K(P_initial)
  - Q-box tables verified to match NIST Twofish spec exactly (file offsets 0x7740A8, 0x7741A8)
  - Validation block: first 8 bytes of .RWN; pass when decrypted pt[0:4] == pt[4:8]
  - Confirmed 2026-06-16 via live Frida capture + Python verification
- [x] ✅ Batch decrypt working — **C: 99/100** (`scripts/rwn_decrypt.py`, 5/5 samples verified ✓)
- [x] ✅ **Decrypted binary structure fully mapped** — **C: 90/100** (2026-06-16, see `docs/02-file-formats/rwn-binary-format.md`)
  - Format marker `TWINB` at decrypted offset 0x35 (vs. `TAS32` at same offset in .RUN files)
  - Header: 128 bytes (32 DWORDs); key fields: [0x0C]=proc table size, [0x14]=var count, [0x20]=var table size
  - File reference table: starts at 0x80, 16-byte null-padded entries, all-zero terminator
  - Dispatch/jump table: starts at 0x6C0, 8-byte entries [type_DWORD + offset_DWORD]
  - String constant pool: `[0x41][0x00][uint16_LE length][ASCII chars]` per entry
  - Procedure symbol table (end-of-file): 53-byte records, Pascal length-prefix name at byte 0
    - SRC-compiled modules: procedure names present; LIB-compiled (LISTG60.LIB etc.): byte 0 = 0x00 (no name)
  - Source filename: 60-byte space-padded ASCII field before variable table (e.g. "suwin7.src", "LISTG60.LIB")
  - Variable symbol table (end-of-file): 77-byte records; name at bytes 0–14 (or 1–14 if byte 0 < 0x20)
    - Byte 0 < 0x20: compiler type code (0x05 = temp var), name at bytes 1–14
    - Byte 0 >= 0x20: printable = first char of user-declared variable name, name spans bytes 0–14
- [x] ✅ **Variable names extractable from ALL RWN files** — **C: 100/100**
  - T7INA.RWN: 3,917 variables including full buffer access patterns (BKIC.PROD.CODE, BKIC.PROD.DESC, …)
  - EvoERPmenu.RWN: 1,635 variables (LPASSWORD, USER_WHO, IS.LOG.*, COMPANY_NAME, BKMENUSU.*, …)
  - suwin7.rwn: 68 variables (TEMP0–TEMP59 + CURR_TIME, WAIT_SECS, SERIALNUMBER, LICTYPE, …)
- [x] ✅ **DB file names extractable (all modules)** — **C: 100/100**
  - EvoERPmenu.RWN opens: ISLOG, FILELOC, BKSYAP, BKSYMSTR, BKMENUSU, BKAPDESC, BKPSUSER, BKARINVL, ISEXUSER, BKYSMSTR, ISJAVA, MKAHIST, ISTRIGRS, BKICMSTR, ISREMIND, LOT, SERIAL, ISNCR
  - T7INA.RWN opens: BKICMSTR + 52 other inventory/related tables
- [x] ✅ **Symbol extractor script** — **C: 99/100** (`scripts/rwn_extract_symbols.py`)
  - Single-file or batch mode; `--encrypted` flag decrypts on-the-fly; JSON output supported
  - Must be run against local copies in `samples/` (not directly against network share)
  - Note: all existing `samples/rwn_decrypted/*.dec` files were made with wrong key — re-decrypt needed
- [x] 🔄 Bytecode instruction set — **C: 15/100** (TAS Pro 6 opcodes partially mapped; TAS Pro 7 encoding different)
  - Confirmed: TAS Pro 7 decrypted body is correct (uniform bytes = no embedded strings, no padding)
  - TAS Pro 7 uses a different opcode format — no inline `41 00` string pushes found
  - See `docs/02-file-formats/run-tas6-bytecode.md` for TAS Pro 6 findings; TAS Pro 7 analysis pending

### 2.3 `.RUN` — TAS Pro 6 Compiled Program
- [x] ✅ Older generation; readable strings present (menu codes extractable) — **C: 85/100**
- [x] ✅ 554 menu codes extracted from `.RUN` string dump — **C: 88/100**
- [x] ✅ Still in active use for legacy BK\* / T6\* modules — **C: 80/100**
- [x] ✅ File structure confirmed: header / table-name slots / variable storage / code+string pool — **C: 72/100**
  - Magic "TAS32" at offset 0x35; version byte at 0x3A; table names at 0x80 (16-byte slots)
  - Variable storage: zero-initialized block, size = header[0x18]
  - See `docs/02-file-formats/run-tas6-bytecode.md`
- [x] 🔄 Bytecode instruction set — **C: 22/100** (partial; key opcodes 0x41/0x46/0x4E identified)
  - Opcode `41 00 LL LL data` = PUSH_VALUE (string literal or compiled expression)
  - Table names embedded as inline strings (runtime does string-based table lookup, not slot index)
  - 7 SRC+RUN Rosetta Stone pairs ready; BKMRF 3-way compile diff planned
- [ ] ⬜ All readable logic extracted from `.RUN` string sections

### 2.4 `.DFM` — Delphi Form Layout
- [x] ✅ Format confirmed: plaintext Borland Delphi VCL textual form representation — **C: 92/100**
- [x] ✅ Structure: `object ClassName ... property = value ... object Child ... end ... end` — **C: 90/100**
- [x] ✅ 1,109 forms successfully parsed; 25 failures are zero-byte placeholders — **C: 90/100**
- [x] ✅ Key properties documented: Left/Top, BorderStyle, Font, Caption, Hint (dev path hint) — **C: 85/100**
- [x] ✅ Child controls identified: TLabel, TEdit, TButton, TPanel, TGroupBox, TDBGrid — **C: 78/100**
- [x] ✅ DFM ↔ RWN pairing rule confirmed (same basename) — **C: 92/100**
- [x] ✅ DFM summary CSV generated (`samples/dfm_parsed/dfm_summary.csv`) — **C: 88/100**
- [x] ✅ TAS-specific control types fully cataloged (2026-06-17) — **C: 92/100**
  - 51 unique control types across 1,136 DFM files — full catalog in `docs/02-file-formats/tas-pro-7-controls.md`
  - 16 TEditForm variants (TEditForm1 dominates: 857/1112 = 77%)
  - TTAS* controls: TTASENTER (7,504), TTASNumEnter (3,994), TTASComboEnter (3,622), TTASDateEdit (1,380), TTASComboBox (1,260), TTASDataGrid (423), TTASStrList (138), TTASCheckBox (1,948), TTASRadioButton (221)
  - TShellExe (850 occurrences!) = how EVO launches print/email/file-open
  - TRtnTimer (227) = auto-dismiss, polling, and timeout pattern throughout UI
- [ ] ⬜ All TAS-specific control properties documented with behavior
- [ ] ⬜ Form-to-menu-code mapping fully resolved (which DFM opens for each menu code)
- [ ] ⬜ Binary `.DFM` variant (the 25 TPF0-format forms) decoded

### 2.5 `.DCY` — Data Dictionary / Compiled Schema
- [x] ✅ Format: Twofish-192-CFB encrypted binary; key K_D; cipher solved 2026-06-16 — **C: 100/100**
- [x] ✅ All 41 standard DCY files decrypted and cataloged (Pass 19, 2026-06-17) — **C: 95/100**
  - Full catalog: `docs/02-file-formats/dcy-forms-catalog.md`
  - Every DCY decrypts to a Delphi VCL TEditForm DFM — they are encrypted UI form definitions, not schema files
  - Note: the term "data dictionary" in TAS Pro 7 means the compiled form+code bundle, NOT a database schema dictionary
- [x] ✅ Paired with `.RWN` of same basename — **C: 85/100**
- [x] ✅ Decryption working: `scripts/dcy_decrypt.py`; MDUMMY.DCY → DFM content confirmed — **C: 100/100**
- [x] ✅ 41/48 standard `.DCY` files decrypt OK; 7 suwin*.DCY use different format — **C: 95/100**
- [x] ✅ Login/company DCY files decoded: EVOMENU_LOGIN (login), EVOMENU_SELCOMP (company select), EVORESETPASS (admin reset), EVOCHANGEPASS (user change) — **C: 92/100**
- [x] ✅ Full EvoERP startup flow confirmed from DCY content: ISSPLASH → EVOMENU_LOGIN → EVOMENU_SELCOMP → EvoERPmenu.RWN builds menu → EVOMENU_RUNPRG dispatches modules — **C: 90/100**
- [x] ✅ All shared system dialogs identified: PRINTTLL (print), NZEMAILTLL (email), WBKLOOKUP (list-picker), WBKLUGRID (grid admin), GETALPHAGEN (1-field input), T7POPGET (5-field popup), EVOMESSAGE (modal), EVOUSERS (user mgmt) — **C: 92/100**
- [x] ✅ License model confirmed as annual subscription from EVOEXPIRE.DCY — **C: 90/100**
- [ ] ⬜ suwin7.dcy decryption — still fails all known keys (K_A/K_B/K_C/K_D); 5th key unknown

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
- [x] ✅ INDEX.DDF parsed → primary keys for ~200+ tables documented in `docs/04-data-dictionary/primary-keys.md` — **C: 72/100**
- [x] ✅ RELATE.DDF / TRIGGER.DDF / PROC.DDF / VIEW.DDF / ATTRIB.DDF / OCCURS.DDF — all confirmed EMPTY (2026-06-17) — **C: 100/100**
  - Zero foreign keys, zero triggers, zero stored procedures, zero views
  - All data integrity enforced at the TAS Pro application layer only
  - Btrieve is used as a pure key-value B-tree store with no database-level constraints

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
- [x] ✅ IS\* (tax, utilities, Java integration — ISJAVA table) — **C: 68/100** (Pass 22–23: ISLBLMAP/IS2DBAR/ISUSAGE/ISAPAINL/ISALINKS/ISLINKS/ISESTASM/ISESADTL/ISMICADT/ESA/EST/ISTAXGRP all field-documented; ~200 smaller IS\* tables remain)
- [x] ✅ AHSYLOG (security / user table) — **C: 72/100**
- [ ] ⬜ Full per-table narrative documentation (see §16 for checklist)
- [ ] ⬜ MT\* vs. BK\* scope difference confirmed (which company, which generation)
- [ ] ⬜ BKARHINV anomaly fully resolved (sub-folder table, now documented)
- [ ] ⬜ All 30 WO\* tables cross-referenced to Work Order module logic
- [ ] ⬜ Primary key confirmed for each of **728+** tables (from INDEX.DDF; originally 649, +55 pass 7b, +17 pass 8, +26 pass 9 = 747 minimum — see PROJECT-STRUCTURE.md Special/Misc Tables)
- [ ] ⬜ Foreign key relationships mapped across module boundaries

### 4.4a ISTS.CFG.* Configuration Keys
- [x] ✅ Key namespace confirmed: `ISTS.CFG.*` strings in all program binaries map to BKYSMSTR/BKSYMSTR fields — **C: 72/100**
- [x] ✅ **535 unique keys** cataloged from grep across 2,575 rwn_strings files — **C: 78/100**
- [x] ✅ Functional categories identified: Access/Security, AP, AR, SO (70+ keys), PO (80+ keys), WO (44+ keys), DC, Inventory/Costing, Reporting, EDI, Credit Card, EvoNotes, Ship-Via — **C: 68/100**
- [x] ✅ Prevalence distribution documented (9 global keys in 400+ files; 276 module-specific in 1–9 files) — **C: 75/100**
- [x] ✅ Full key directory documented in `docs/05-configuration/ists-cfg-keys.md` — **C: 68/100**
- [ ] ⬜ Complete YN[N] ↔ ISTS.CFG.* mapping (only 3 confirmed so far: YN[38], YN[228], YN[229])
- [ ] ⬜ All 535 keys mapped to their BKYSMSTR/BKSYMSTR field with confirmed meaning
- [ ] ⬜ Keys that control module-enable/disable confirmed (module licensing gates)

### 4.4 Key Individual Tables (minimum needed for 90% goal)
- [x] ✅ `BKARCUST` — AR Customer master: 106 fields documented in `docs/04-data-dictionary/tier1-tables.md` — **C: 68/100**
- [x] ✅ `BKICMSTR` — Inventory Item master: 64 fields documented; PROD_TYPE codes R/N confirmed from live IN-A screen (2026-06-17); full set RFAMNLBTKO confirmed from HH filter string — **C: 82/100**
- [x] ✅ `BKSYMSTR` — System configuration master: 286 fields, key categories documented — **C: 62/100**
- [x] ✅ `AHSYLOG` — User security: all 23 fields documented — **C: 68/100**
- [x] ✅ `ISJAVA` — Java task queue: pattern confirmed; table NOT found in DDF (may be runtime-only or named differently) — **C: 55/100**
- [x] ✅ `BKLOGON` — Active session: all 10 fields documented — **C: 72/100**
- [x] ✅ `WORKORD` — Work order master: all 74 fields documented — **C: 72/100**
- [x] ✅ `WORKCHG` — Work order change log: all 25 fields documented — **C: 70/100**
- [x] ✅ `BKARCUST` — all fields with meaning, PKs — documented — **C: 68/100**
- [x] ✅ `BKICMSTR` — all fields with meaning; PROD_TYPE codes confirmed (RFAMNLBTKO, R/N from live UI) — **C: 82/100**
- [x] ✅ `BKSYMSTR` — major categories documented — **C: 62/100**
- [x] ✅ `BKAPVEND` — AP Vendor master: 26+ fields documented — **C: 65/100**
- [x] ✅ `BKGLCOA` — GL Chart of Accounts: 65 fields documented (replaces BKGLJRNL — that table is BKGLTRAN) — **C: 68/100**
- [x] ✅ `WORKORD` / `WORKCHG` — Work order header + change log — documented — **C: 70/100**
- [x] ✅ `BKSOX` / `BKSOXH` — Sales Order extract: 25 fields documented — **C: 65/100**
- [x] ✅ `BKARINV` / `BKARINVL` / `BKARINVI` — AR invoice header/lines/staging: fields and posting flow documented; BKAR_INVL_RTS = per-line release-to-ship flag; T7SAG = SO-G Post Invoices module confirmed — **C: 68/100**
- [ ] ⬜ `BKPO????` — Purchase Order tables — all fields (BKAPPO + BKAPPOL identified but not field-level documented)
- [ ] ⬜ `BKPRMSTR` — Payroll master (384 fields) — all fields
- [x] ✅ `BKSLEVEL` — **SOLVED: Security level permission matrix** (14 menus × 20 options = 422 fields; links AHSYLOG.AHSY_USER_LEVL to allowed operations) — **C: 68/100**
- [x] ✅ `BKPRGLFL` — **SOLVED: Payroll GL posting config** (664 fields: 20 user deductions × GL accounts/limits/pct + 30 tax vendors) — **C: 62/100**
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
- [x] ✅ Tables identified: BKAR\* (27 tables); primary keys documented — **C: 65/100**
- [x] ✅ Key forms read: T7ARA (customer master — all fields), T7ARB (voucher/GL dist), T7ARC (payment application), T7ARD (finance charges), T7ARE (statements), T7ARF-I (reports) — **C: 72/100**
- [x] ✅ AR workflow fully traced: customer → invoice → payment → statement — **C: 72/100**
- [x] ✅ Payment application logic confirmed: credits/deposits tracked separately in BKAR.OUT.CREDIT[1-2] — **C: 68/100**
- [ ] ⬜ BKARCUST all 106 fields documented with meaning
- [ ] ⬜ AR aging bucket calculation logic confirmed (how 30/60/90 boundaries computed)

### 7.2 Accounts Payable (AP)
- [x] ✅ Menu codes listed (AP-A through AP-U) — **C: 72/100**
- [x] ✅ Forms inventoried (T7AP\*.DFM) — **C: 70/100**
- [x] ✅ Tables: BKAP\* (24 tables) — **C: 60/100**
- [x] ✅ Source files: Bkaph.SRC, Bkapha.SRC analyzed — **C: 82/100**
- [x] ✅ **Check printing workflow fully traced** (AP-H): select→check#→date→print→GL post(CD)→invoice update→BKAPCHKH→BKGLCHK — **C: 82/100**
- [x] ✅ GL posting type confirmed: "CD" (Cash Disbursement) — **C: 88/100**
- [x] ✅ BKAPCHKF (temp run file) and BKAPCHKH (permanent history) documented — **C: 78/100**
- [x] ✅ 1099 tracking mechanism confirmed: BKAPVEND 1099 code + BKAPINVT TYPE="P" — **C: 70/100**
- [ ] ⬜ Voucher entry workflow fully traced (AP-B main form logic)
- [ ] ⬜ BKAPVEND all fields documented with meaning

### 7.3 Inventory (IN)
- [x] ✅ Menu codes listed (40 operations) — **C: 72/100**
- [x] ✅ Forms inventoried (T7IN\*.DFM) — **C: 70/100**
- [x] ✅ Tables: BKIC\* (16 tables), MTICMSTR identified — **C: 58/100**
- [x] ✅ BKICMSTR all 62 fields documented with meaning in tier1-tables.md: product code/desc, type, class, category, UOM (stock/purchase/price), costs, QOH, reorder, lead time, GL accounts (asset/COGS/scrap/non-tax), absorbed labor/setup/ops/material/fixed OH/variable OH, UPC, MTD/YTD sales — **C: 72/100**
- [x] ✅ Supplemental item master form set confirmed: allocation, components, forecast, pricing, specs, UDF, usage, WIP — **C: 65/100**
- [x] ✅ 16+ location/bin forms (T7INL* series) confirmed — **C: 60/100**
- [ ] ⬜ FIFO/LIFO/average cost layer logic traced (INVTXN / BKICVAL tables)
- [ ] ⬜ Physical inventory workflow (PI module) traced end-to-end
- [ ] ⬜ Lot tracking / serial number tracking workflow confirmed

### 7.4 Sales Orders (SO)
- [x] ✅ Menu codes listed (48 operations — largest module) — **C: 72/100**
- [x] ✅ Forms inventoried (T7SO\*.DFM) — **C: 70/100**
- [x] ✅ Tables: BKSO\* (7 tables identified) — **C: 55/100**
- [x] ✅ Key forms read: T7SOA (full header+lines, 5001-element line arrays), T7SOB (print), T7SOC (pick→pack→ship→invoice hub), T7SOD (line status), T7SOE (release), T7SOF (invoice print), T7SOG (COGS) — **C: 72/100**
- [x] ✅ Order → shipping → invoice chain traced: T7SOA → T7SOE → T7SOC → T7SOF — **C: 70/100**
- [x] ✅ Certificate of Conformance + Country of Origin compliance docs confirmed (T7SOC RTMs) — **C: 68/100**
- [x] ✅ 5,001-element line item arrays confirmed (supports 5,000 lines per SO) — **C: 75/100**
- [ ] ⬜ All BKSO\* tables with fields documented (BKSO, BKSOL, BKSOSH, BKSOHLOT, BKSOHSER, BKSOLOCK, BKSONOTE)
- [ ] ⬜ Sales Analysis (SA module) tables and calculations

### 7.5 Purchase Orders (PO)
- [x] ✅ Menu codes listed (29 operations) — **C: 72/100**
- [x] ✅ Forms inventoried (T7PO\*.DFM) — **C: 70/100**
- [x] ✅ Key PO forms read from network share: T7POA (232 KB — full header+lines), T7POB (print options), T7POJC (receiving+QC), T7POH (RFQ/5-level pricing), T7POM (multi-tab inquiry) — **C: 70/100**
- [x] ✅ 5-level vendor price breaks confirmed in T7POH — **C: 72/100**
- [x] ✅ RoHS / NCR tracking on received items confirmed (T7POJC) — **C: 68/100**
- [x] ✅ Digital signature support on printed POs confirmed — **C: 65/100**
- [ ] ⬜ PO entry → receipt → AP voucher chain traced end-to-end
- [ ] ⬜ All BKPO\*/BKAP\* tables with fields documented

### 7.6 Work Orders (WO)
- [x] ✅ Menu codes listed (31 operations) — **C: 72/100**
- [x] ✅ Forms inventoried (T7WO\*.DFM) — **C: 70/100**
- [x] ✅ Tables: WO\* (30 tables) — **C: 55/100**
- [x] ✅ Source files: BKAWLB.SRC (Work Order labor logic analyzed) — **C: 62/100**
- [x] ✅ Work order lifecycle **fully traced**: Create(WO-A) → Release(WO-B) → Routing(WO-K-A) → Material(WO-F/WO-FA backflush) → Labor(WO-G) → Outside(WO-H → PO) → Close(WO-S) — **C: 72/100**
- [x] ✅ WO status codes documented: F=Released, R=Completed, C=Closed, S=Scheduled, I=In Process, X=On Hold — **C: 75/100**
- [x] ✅ WO priority 1–9 confirmed as scheduling parameter — **C: 72/100**
- [x] ✅ DC-to-WO integration confirmed: DC postings write to same WO tables; T7WOKK reverses them — **C: 68/100**
- [x] ✅ WO-PO linkage confirmed: outside process operations link to AP POs — **C: 68/100**
- [ ] ⬜ All 30 WO\* tables with fields documented
- [ ] ⬜ WORKORD all 74 fields confirmed with meaning

### 7.7 General Ledger (GL)
- [x] ✅ Menu codes listed (16 operations) — **C: 72/100**
- [x] ✅ Tables: BKGL\* (28 tables) — **C: 65/100**
- [x] ✅ All 24 GL forms read from network share — **C: 72/100**
- [x] ✅ Journal transaction types confirmed: GJ, CR, CD, TT, YE (entry types), RS, RP, PR, OT, WO (system posting types) — **C: 75/100**
- [x] ✅ BKGL table family purpose documented: live/archive/report/temp/COA/statement/crossref tiers — **C: 68/100**
- [x] ✅ Journal entry workflow traced: T7GLB (enter GJ/CR/CD/TT/YE) → T7GLC (report/filter) → T7GLP (period-end) → T7GLARCH (archive) — **C: 70/100**
- [ ] ⬜ Period-end close process traced step-by-step (T7GLH/T7GLP sequence)
- [ ] ⬜ BKGLCOA all 65 fields confirmed with full meaning
- [ ] ⬜ BKGLTRAN all 16 fields confirmed with full meaning

### 7.8 Bill of Materials (BM)
- [x] ✅ Menu codes listed — **C: 65/100**
- [x] ✅ Tables: BKBM\* (10 tables) — **C: 60/100**
- [x] ✅ BOM Tree analysis tool documented (BOMTREE.RWN) — **C: 60/100**
- [x] ✅ 4 core forms read: T7BMA (master entry, 15 remarks/component), T7BMB (print with status codes Y/N/O/D/E/P/S/Q/R), T7BMC (multi-level print, "up to X levels"), T7BMD (availability + shortages) — **C: 62/100**
- [x] ✅ Item type codes confirmed: R/F/A/M/N/L/B/T/K/O (10 types) — **C: 75/100**
- [x] ✅ Item status codes confirmed: Y/N/O/D/E/P/S/Q/R (9 status values) — **C: 75/100**
- [x] ✅ Multi-level BOM explosion confirmed (T7BMC: "print up to X levels") — **C: 65/100**
- [x] ✅ RoHS compliance flag on BOM components confirmed — **C: 72/100**
- [ ] ⬜ All BKBM\* tables with fields documented
- [ ] ⬜ Phantom assembly logic confirmed (BKBMAMTR purpose)

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
- [x] ✅ Tables: BKPR\* (16 tables); BKPRMSTR (384 fields — largest practical table) — **C: 55/100**
- [x] ✅ Key forms read: T7PRA (W-4/employee tax setup), T7PRB (current payroll batch entry), T7PRF (11-bracket tax tables), T7PRE (direct deposit) — **C: 62/100**
- [x] ✅ Tax table structure documented: 11-bracket tiers per tax code in BKPRFTAX — **C: 65/100**
- [x] ✅ Array-based payroll entry confirmed (batch employee processing, 7 unlimited deduction types) — **C: 62/100**
- [ ] ⬜ BKPRMSTR all 384 fields documented with meaning
- [ ] ⬜ Payroll calculation cycle traced (T7PRB → check run → BKPRHIST)
- [ ] ⬜ W-2 / 1099 generation traced (T7PRS identified)

### 7.12 Data Collection (DC)
- [x] ✅ Menu codes listed — **C: 65/100**
- [x] ✅ Files: EvoDC\*.RWN, EvoDCmenu.RWN, EvoDCsetup.RWN cataloged — **C: 70/100**
- [x] ✅ Tables: BKDC\* (7 tables) — **C: 55/100**
- [x] ✅ Source file: BKDCA.SRC analyzed — **C: 65/100**
- [x] ✅ Handheld forms: T7HH\*, label tables BKDC\* — **C: 60/100**
- [ ] ⬜ Full DC workflow (scanner → table entry → WO update) traced
- [ ] ⬜ All BKDC\* tables with fields documented

### 7.13 Serial Control (SC) ⚠️ NAME CORRECTED — was "Scheduling/Capacity"
- [x] ✅ Menu codes listed — **C: 68/100**
- [x] ✅ All 9 DFM files read from network share — **C: 72/100**
- [x] ✅ SC-A: Edit Serial Numbers (MTSER table) — serial record view/edit — **C: 75/100**
- [x] ✅ SC-B: Assign Serial Control on items (MTIC.PROD.SER flag) — **C: 72/100**
- [x] ✅ SC-G: Serial format setup (total length, numeric start position, last number) — **C: 72/100**
- [x] ✅ T7SCOMP: Compound serial numbers (IS.SCOMP.*) — **C: 65/100**
- [x] ✅ Primary tables: MTSER (serial master), IS.SERC.* (config), IS.SCOMP.* (compound) — **C: 72/100**
- [ ] ⬜ MTSER all fields documented with meaning
- [ ] ⬜ Serial number lifecycle (receive → track → ship → close) fully traced

### 7.14 Physical Inventory (PI)
- [x] ✅ Menu codes listed — **C: 65/100**
- [x] ✅ Tables: BKPI\* (7 tables) — **C: 55/100**
- [x] ✅ PI-A (Capture Frozen Inventory: YEAR/QTR/FDATE/COUNTTYPE), PI-B (print count sheets), PI-C (Enter Tag Counts: BKPH.TAGNUM/LOC/EMPNAME/CODE/LOT), PI-D (Missing Tags) — **C: 62/100**
- [ ] ⬜ Variance calculation and posting steps (remaining PI forms)

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
- [x] ✅ ES-D (Print Customer Quotes), ES-E (Convert Estimates: ISTO.WO + ISTO.SO — converts to WO or SO), ES-B/C (print/range options) — **C: 58/100**
- [ ] ⬜ ES-A (main entry form) not found on share; BKES.* table fields not yet extracted

### 7.18 Remaining Modules (not yet deeply documented)
The following modules have menu codes and forms inventoried but no deep logic documentation:

- [ ] ⬜ **AB** — no T7 RWN/DFM files found (DBA-era legacy code, unimplemented in TAS Pro 7)
- [x] 🔄 **AC** — Activity Control / NCR tracking — 3 DFMs + 4 RWN modules (T7ACTION/ACRDTYPE/ACDET/ACDATE); ACDATE (WODATE.START/FINISH/QTY, PARPRE/PARSUF/TOPPRE/TOPSUF WO hierarchy, DELPRE cascade delete); ACRDTYPE (AC.RD.TYPE/REASON/DISPO disposition codes: rework/scrap/use-as-is); T7ACTION (IS.ACTION.TYPE/DESC/MISC action items); T7ACDET (AC.DET.ID/LINE/PART detail records); primary tables WODATE/ISACTION/ACRDTYPE/ACDETAIL — **C: 60/100**
- [x] 🔄 **AM** — Accounting Maintenance (NOT Asset Management — CORRECTED) — 5 forms read (GL period control, account history, account entry, dept copy/delete, financial statement format) — **C: 75/100**
- [x] 🔄 **AD** — Accounting Defaults — CHM fully documented (AD-A GL defaults with 20 accounts + 5 posting flags + 6 period-date controls, AD-B checking account setup with 16 fields, AD-C AP defaults with 11 behavioral flags); RWN programs: T7MDEFAULTS (435 procs, main — opens BKSYMSTR+BKYSMSTR+ISBANKS+42 more tables), T7MDEFBANKS (79 procs, AD-B bank setup — BKGLCOA+ISBANKS), T7MDEFNDC (252 procs, extended module defaults — BKSYAP+BKESTCFG+BKFOCFG+BKCPMSTR+BKCMCNTD); primary tables: BKSYMSTR (system config), BKYSMSTR (YN flags), ISBANKS (checking accounts); gap: specific BKSYMSTR field offsets for each setting — **C: 70/100**
- [x] 🔄 **CM** — CRM/Contact Manager — T7CMA + 4 sub-forms read; CRM-AR bridge confirmed; 9 emails/contact (BKCM.ACCN.EMAIL[1-9]); contact title/primary flag; key dates (BKCM.ACTD.*); account classes; territory/SIC/lead-source; BKCM.* (46 tables) — **C: 65/100**
- [ ] ⬜ **CP** — no T7 RWN/DFM files found (DBA-era legacy)
- [x] 🔄 **CR** — Contract Review / SO Approval — CHM confirmed: CR-A='Assign Departments to Sales Orders', CR-B='View/Enter SO Approvals'; T7CTREVU (96 procs): ENTER.PSWD/CONF.PSWD password entry, CT.DEPT/CT.ADMIN department+admin flags, CT.EMPNAME approving employee, SFROM.SONUM/STHRU.SONUM SO range, FROM/THRU.ORDDTE date range; T7CTREVUADMIN = admin variant stub; password-protected SO approval — **C: 55/100**
- [x] 🔄 **CC** — Credit Card Processing ⚠️ (NOT Cycle Count — CORRECTED) — all 6 DFMs read; CC-P (IS.CC.MASKED/CARDNAME/EXP/ZIP — masked card storage with expiry flag), CC-PO (CC charges on POs: ccnum/ccamount/CCYY/CCMM), ccr1 (Credit Card Invoice List report by date/terms), CC-DE (CSV import); WO and item range filters confirm cost allocation to jobs; primary tables IS.CC.* — **C: 65/100**
- [x] 🔄 **CS** — Commission/Salesperson Management — all 12 DFMs read; CS-A (BKPR.SLS.* fields: rate/HOW/WHEN/class/GL/agent-vendor), CS-B (quota/COGS/comm-due/paid[1-7]), CS-D (transfer commissions: BKPR.COMM.SLSP/CCODE/INVNM/INVDT), CS-E/F (detail+summary reports); outside agents linked to AP vendor — **C: 70/100**
- [x] 🔄 **DE** — Data Entry / EDI / Imports (20 DFMs, 33 ops) — all 20 DFMs read; BOM component import (DEM=import, DEER=error report), PI tag import (DEHD), WO material import (DEJH), AR invoice import (DEQ/DER), web order import (DET/DETB: import.to.edi flag), vendor POA 855 (DEV: SKIP.PONUM/PCODE/PQTY), EDI-860 PO changes (DEP860), customer releases (DEPB: RELEASE_NUM), web item FTP export (DEU), defect code setup (DEFECT: IS.DEF.*); DEK=global field replace DESTRUCTIVE, DEL=selective file erase DESTRUCTIVE — **C: 68/100**
- [x] 🔄 **DI** — Digital Signatures — T7DIGSIG.DFM (131KB) confirmed: Caption='Enter Digital Signatures'; PO#/Vendor/Name/Description/Terms + EMAIL.TAG/NAME/LEVEL/ADDRESS for email routing of PO approvals; T7DigSigChgPSWD = change digital signature password; ISDIGSIG (89f, fully documented): 10 approval slots per employee with ACTIVE/TYPE/SDATE/FDATE/TDATE/AMT/FLAG/DATE per slot + MOTCACH/POENTBY/SOENTBY/FILE/ATIME/ADATE; ISTRIGRS (25f) used for email notifications; 3 RWN programs identified — **C: 65/100**
- [ ] ⬜ **EX** — Export / data exchange — forms inventoried only
- [x] 🔄 **FA** — Fixed Assets — all 3 DFMs read; FA-A (IS.FXA.* asset master: cost/residual/life/method/GL accounts), FA-B (IS.FXT.* depreciation: post with Ready-to-Post flag), FA-E (export); IS.FXA.*/IS.FXT.* tables — **C: 75/100**
- [ ] ⬜ **FL** — no T7 RWN/DFM files found (DBA-era legacy)
- [x] 🔄 **FO** — Features & Options — all 3 DFMs read; FO-C (BKBM.PROD.OPYN[5] option flags, PAR.DESC+COMP.DESC parent-component option pairing), FO-D (item/class/category range), FO-E (item filter); BOM sub-module — options set OPYN[1..N] per product; SO triggers option selection driving BOM inclusions — **C: 50/100**
- [x] 🔄 **FP** — Features & Options Print — CHM confirmed: FP-B='Print Features and Options'; print sub-module for FO (Features & Options) — **C: 35/100**
- [x] 🔄 **HH** — Handheld / Shop-Floor Data Collection (44 forms) — 20 key DFMs read; 9 sub-areas: PO Receiving (hhpoc/POCBIN/POCLot/POCSER), WO ops (wog=issue, wop=finish, WOSCRAP, WOLabel, woser), SO shipping (SSOE 5-form verification chain, SOLookup, SODD), Inventory (ItemLU/INGA labels/hhinlj transfer/INLJLot/INLJSer), DC labor scan (HHDCA=scan.wo/scan.emp/OPER), PI tag count (HHPIC/hhpictags with lot/serial), alerts, batch process; large.lookups dual-mode; item type filter RFAMNLBTKO — **C: 68/100**
- [x] 🔄 **IC** — Inventory Control utility — 1 DFM read (IC2EST: Caption='Copy Production to Estimate Inventory' — one-way bridge copies production BOM data into ES estimating module); IC broader scope in RWN — **C: 35/100**
- [x] 🔄 **IM** — Import Management / Landed Cost — all 5 DFMs read; IMB (ISIS.MCF.* currency master: code/desc/base/symbol), IMC (ISIS.MCR.* exchange rates: date/base/SOURCE[1..n]), IMD (ISIS.LND.* landed cost GL accounts: duty/freight/deferred variants), IME (ISIS.DUTY.* duty codes: first 3 chars=vendor, percentage), IMF (ISIS.BRK.* customs broker: code/flat/perc/type); full landed cost and multi-currency infrastructure — **C: 70/100**
- [x] 🔄 **IS** — InfoSystem / Multi-Currency GL — T7ISMCC (ISTECH.LIB, 82 procs): ISGL.CYDATE (current year GL date), ISGL.1YDATE–6YDATE (6 years back), ISGL.FYDATE (fiscal year date) — multi-company GL fiscal date synchronization; T7ISASER (DBA.LIB, 12 procs): WOPRE/WOSUF + MTWO.WIP.* — old-era WO serial number assignment; IS namespace = shared extension tables (IS.CC/RMA/FXA/SERR/TERMS/JOB/CYCLE/ACTION/DEF/SCOMP) — **C: 60/100**
- [x] 🔄 **JC** — Job Costing (18 ops) — all 14 DFM files read; JC Engine parameters fully extracted; forms: JC-A (main report), JC-E (parent/child cost roll-up), JC-N (cost calculation modes: current/historical/proposed), JC-P (materials in WIP); 6 labor types, 3 shifts; primary tables WORKORD/ISCALC.*/ISCOST.* — **C: 68/100**
- [x] 🔄 **LC** — Lot Control — all 6 found DFMs read; LC-A (MTLOT table), LC-B (assigns MTIC.PROD.LOT flag), LC-G (archive with expiry date range); parallel to SC module for lots; MTLOT primary table — **C: 72/100**
- [ ] ⬜ **LM** — no T7 RWN/DFM files found (DBA-era legacy)
- [ ] ⬜ **LO** — no T7 RWN/DFM files found (DBA-era legacy)
- [x] 🔄 **MA** — T7MAPDEPO.RWN (97 procs): BKARDEP+BKARCUST+BKARINVL+ISARDEPL+BKGLCOA+BKARINVT — AR Deposits module; handles customer deposit posting to GL; helper programs: T7GETDEP (18 procs, retrieves available deposit balance), T7GETWEB (6 procs, web-order deposits), T7ARN (enter SO deposits), T7ARC (apply deposits at payment); ISARDEPL confirmed in use but not in DDF schema; deposit workflow fully traced (enter→apply→clear) — **C: 62/100**
- [ ] ⬜ **MM** — no T7 RWN/DFM files found (DBA-era legacy)
- [ ] ⬜ **PC** — no T7 RWN/DFM files found (DBA-era legacy)
- [ ] ⬜ **PL** — no T7 RWN/DFM files found (DBA-era legacy)
- [x] 🔄 **PS** — Program Security / User Access — all 6 DFMs read; PSA (BKPS.USER.CODE user setup: seclevel, seccode [A/P/1/2/C/V/U/E], company, employee/rep), PSE (user security report), PSEITM (program access list: PROGRAM_NUM/NME), PSF (access-to-program report), PSEGRP (button group config), PSK (approve vendor: bkap.vendname); dual user system with AHSYLOG (module-level) + BKPS (program-level) — **C: 60/100**
- [x] 🔄 **QC** — Quality Control — 4 DFM files read; QC-A confirms QC/Scrap dual-code classification + vendor range; parent item roll-up in QC-B/C/D; tables BKQCMSTR/BKQCTRAN/BKQC confirmed in DDF — **C: 52/100**
- [x] 🔄 **QT** — Service Quote (linked to SR module) — 1 DFM read (QTINFO: 'Quote Misc. Information'; ISSR.INFO.DATE[1..5] indexed dates — ISSR prefix confirms SR module linkage; service quotes track multiple date milestones) — **C: 35/100**
- [x] 🔄 **QU** — Query / Inquiry Tools — CHM fully documented (6 ops); RWN programs: WBKLOOKUP (413 procs, QU-A universal lookup grid — opens BKLUGRID+ISDRILL+ISDRILLM+FILEKEY+FILEDICT), CALDRILLBT (94 procs, QU-B calendar drill-down), EVOBS (128 procs, QU-D Business Status — opens ISBSF+BKGLTRAN+MTICMSTR), T7QGRID (62 procs, QU-E Quick Grid Lookup — opens BKLUGRID+ISDRILL), QUERYEXECUTE (26 procs, QU-F SQL executor — opens ISDRILL+BKPSUSER); key tables: ISDRILL (46f, query definitions with 20 FILTER + 20 WHILE condition slots), ISDRILLM (17f, drill navigation: PARENT→CHILD with SFIELD/TFIELD mappings) — **C: 70/100**
- [x] 🔄 **RF** — Request for Quote (from Estimating) — 1 DFM read; T7RFQ: 103 procs, ISESTDTL+BKMRPPO+BKBMMSTR+BKICMSTR+BKAPVEND+BKAPPO+BKSBVEND; generates vendor RFQs from estimate data; bridges ES (Estimating) and PO — **C: 50/100**
- [x] 🔄 **RM** — Return Material Authorization (RMA) — all 5 DFMs read; RMD=main entry (bkar.inv/invl links, is.rma.warranty NLPB codes, reason for return), RMAWHY=detail popup (is.rma.status), RMDASK=disposition (pass.rma.num [D/J/N], restock.charge, so.location), RME=reason code master (IS.RMA.CODE/DESC), RMG=report; RMA→WO bridge via "Pass to Job" — **C: 68/100**
- [x] 🔄 **RT** — T7RTMVALID.RWN (20 procs): BKSYHELP+DBAHLPID+ISIS+MKAHIST — Report Template Validation utility (validates RTM files, reads help system) — **C: 30/100**
- [x] 🔄 **SA** — Sales Analysis (13 ops) — all 6 DFMs read; SA-A (currency filter: from_cur/thru_cur/inc.change), SA-M/N (BKSA.NAME/TITLE/BASE — dedicated BKSA.* aggregation table, not just BKARINV), SA-O (Top N Sales Report), SA-P (class/category range), SA-Q (Actual Margin Report: from.shipdt/thru.shipdt/thru.afin); multi-currency and WO actual-finish date integration confirmed; primary table BKSA.* — **C: 55/100**
- [ ] ⬜ **SB** — no T7 RWN/DFM files found (DBA-era legacy)
- [x] 🔄 **SD** — Standard Data — 1 DFM read (SDET: IS.SDET.DETAIL + IS.SDET.TYPE); T7SDET: 58 procs, ISSDET+ISSTYPE — type/detail code pair maintenance for cross-module lookup codes — **C: 42/100**
- [x] 🔄 **SH** — Shop Scheduling ⚠️ (NOT Shipping) (16 ops) — all 15 DFM files read; SH-A/B (WO WIP scheduling grid + operation scheduling), SH-C (work center capacity), SH-E (due date change), SH-I (dispatch report with color coding), SH-P (color config); primary tables MTWO.WIP.*, MTWORO.*, MTWC.* — **C: 72/100**
- [x] 🔄 **SL** — t7slsfc.RWN (5 procs): BKARINVL+BKYSMSTR — Sales Forecast utility; accesses AR invoice lines for demand calc — **C: 30/100**
- [x] 🔄 **SM** — System Maintenance (34 ops, 3rd largest) — 23+ forms + full T7SM* sub-module family decoded; SM-K (user prefs→EvoSettings.INI/ISNUMBER), SM-E/F (tax ISIS.TXF+ISIS.TXG), SM-O (ship-via ISSHPVIA with tracking URL), SM-D (payment terms IS.TERMS), SM-PF (ISJOB job#), SM-PH (IS.CYCLE), SM-JM/JN (merge), SM-JC (JC setup), SM-SD (AP doc link); T7SMI* (CRM masters: BKCMLEAD/BKCMTERR/BKCMACFC/BKCMACCC/BKCMDTCD), T7SMP* (ISCATMST/ISUDMSTR/ISJOB), T7SMT/SMU (ISSHPVIA), T7SMTEND/SMTSET (SMT/PCB: ISSMTCFG/MACHINE); BKSYMSTR/BKYSMSTR not fully decoded — **C: 80/100**
- [x] 🔄 **SP** — Statistical Process Control (SPC) ⚠️ (NOT Ship Packing — CORRECTED) — all 6 DFMs read; SPC main entry (Inspector #/Employee/WO/Item/Qty/Customer/Drawing → IS.SERR.ERROR/PROCESS), SPCLIVEGRID (Caption='Top Real Time Errors'; ATYPE/ADETAIL/ACODE/ACOUNT), SPCLIVEREP (auto-refresh live report), SPCREP/SPCREP2 (WO/Part/Employee/Date range reports), SPCREPPPM (PPM defect rate with Sides range — PCB/electronics context); primary table IS.SERR.* — **C: 60/100**
- [x] 🔄 **SR** — Service / Repair — 16 RWN programs confirmed (T7SRA-T7SRK + SRDISPACH/SRBK/SRGA/SRINFO); SR Orders ARE BKARINV records (same as SO/AR); 5 ISSR*INV views = BKARINV (0 diff), 5 ISSR*IVL views = BKARINVL (0 diff); key tables: ISSRMMS (equipment 12f), ISSRINFO (configurable 54f), ISSOREVU (approval workflow 12f), ISARINVX (AR ext 4f); T7SRGA (157 procs) is full posting to BKGLTRAN+BKGLX+BKARHTAX+BKISTAX+ISTAXGRP — **C: 72/100**
- [x] 🔄 **SU** — Setup / UI Configuration — CHM confirmed 4 ops (SU-A=Maintain Grid Lookups, SU-B=Maintain Drill Down Menus, SU-C=Forms Editor, SU-D=Grid Maintenance); RWN programs: WBKLUGRID (68 procs, SU-A — opens BKLUGRID+FILELOC+FILEKNUM+FILEDICT), EVOERPDRILLM (31 procs, SU-B — opens ISDRILLM+BKLUGRID+FILELOC), T7GDM (31 procs, Grid Display Manager — opens BKLUGRID+ISDRILLM); key tables: BKLUGRID (per-user column layout saves), ISDRILLM (drill navigation map, 17f) — **C: 65/100**
- [ ] ⬜ **SY** — no T7 RWN/DFM files found; BKSY* tables are System config (documented)
- [x] 🔄 **TA** — TAS / System Administration — CHM confirmed 9 ops: TA-D=Maintain Database, TA-G=Maintain Menu Access Records, TA-H=Maintain Menu End User, TA-M=Forms Editor, TA-N=Program Scheduler, TA-O=Backup Utility, TA-Q=Change Logo Image, TA-R=SQL Editor, TA-S=Data Dictionary Check; the most powerful admin module — direct DB/menu/scheduler/backup/SQL access — **C: 55/100**
- [ ] ⬜ **UM** — no T7 RWN/DFM files found (DBA-era legacy)
- [ ] ⬜ **UP** — no T7 RWN/DFM files found (DBA-era legacy)
- [x] 🔄 **US** — User Services / Trigger Notifications — T7USG (90 procs): ISTRIGRS primary table (25f, fully documented: CODE/TRIGR/CONTACT/DAYS/EMAIL/ONCE/LDATE/LTIME/WO-PO-SO-CUST-VEND refs + ITYPE/CLASS/CAT/PLANNER); ISREMIND (22f, fully documented: DATE/TIME/WHO/SUBJECT/CUST/VEND/ITEM/FILE/EMAIL/SENT); EvoRemind (46 procs) polls ISTRIGRS and creates ISREMIND calendar entries; US program also opens BKARCUST+BKAPVEND+WORKORD+BKARINV+BKAPPO for entity lookups — **C: 65/100**
- [x] 🔄 **UT** — Utilities (admin/data maintenance) — all 8 DFMs read; UTH (file layout report), t7uti (company add/delete: company_code/name/path/copy.file/cdelete), UTKA (data clear/reset: CLR.COA/CUST/VEND/INVN — DESTRUCTIVE), UTKD (fiscal year: fycur/fy1yp/fy2yp/fy3yp), UTKE (location cleanup — DESTRUCTIVE), UTKF/UTKG (item rebuild F and G variants), UTKH (average cost recalculate by inc.type[1-4]); most ops irreversible — **C: 60/100**
- [x] 🔄 **WC** — Warehouse Control ⚠️ (NOT Work Center) — 8 DFM files read; WC-A (bin master CRUD, ISBN.MSTR table), WC-C (serials by bin, MTSER), WC-D (bulk bin assignment — Skip/Replace), WC-H (location browser); primary tables ISBN.MSTR, BKIC.LOCM — **C: 72/100**
- [x] 🔄 **YS** — T7YSYN.RWN (52 procs): BKYSMSTR+BKSYHELP+DBAHLPID+ISIS+MKAHIST+ISLOG — Y/N system flags editor (BKYSMSTR maintenance) — **C: 45/100**

**Subsystems (not menu modules — discovered via RWN analysis):**
- [x] 🔄 **PI** — Physical Inventory (9 files, 1,056 procs) — **NEWLY DOCUMENTED Pass 11** — T7PIA/T7PIC/T7PIF = main count entry; T7PIB/T7PICA = PI posting to GL (uses BKGLTRAN+BKGLX); T7PID/T7PIE = discrepancy entry; T7PIG = report; T7DEHD = handheld PI entry; PI tables confirmed: BKPIMSTR (run master), BKPILOT (lot counts), BKPIPHYS (physical counts), BKPISER (serial counts), BKPIFROZ (frozen snapshot), PIBINLOC/PIBINLOT (frozen bin records); freeze→count→post cycle inferred — **C: 52/100**
- [x] 🔄 **BO** — Bill of Lading (T7BOL: 178 procs, T7BOLMSO: 174 procs); LOAD.NUMBER/SEAL.NUMBER/TRAILER.NUMBER/AUTHOR.NUMBER/CONTROL.NUMBER; DRIVER.ARRIVED/LOADING.START/END/DRIVER.DEPARTED timestamps; T7BOLMSO: EDIT.CLASS/WEIGHT/PACKS/HM (LTL freight fields); integrated with BKARINV/SO for outbound shipments — **C: 58/100**
- [x] 🔄 **DS** — Data Sync stubs (25 files: T7DSAP/AR/BOM/CK/CM/CO/CS/DC/EST/FO/GEN/GL/HH/IC/IM/MRP/PO/PR/QC/RMA/RO/SH/SO/WC/WO); all are SRC stubs with single STUB variable; all share same core DB set + BKSYAR; one stub per module for multi-company data synchronization — **C: 42/100** (architecture known; sync logic is in RWN, blocked)
- [x] 🔄 **AU** — Automation modules (T7AUTODCH: 183 procs DC labor validation; T7AUTOMRF: 132 procs MRP auto-firm, MTMRP.PARTNO/KEY/DATE/QTY/ONHAND/PEGTO/ORDER/STARTDT; T7AUTOREBSS: 79 procs back-order re-BSS; T7AUTOFX: 21 procs auto foreign-exchange rate update via ISMCF+ISJAVA+ISMCR); automation/batch layer for background ERP operations — **C: 52/100**
- [x] 🔄 **FS** — Field Service (T7FSCLASS: 62 procs, ISFSCLAS+ISPRINFO; T7FSINFO: 61 procs, ISFSINFO; T7FSEMP: 59 procs, ISFSCLAS+BKPRSALE); tracks service classes, field service info records, and employee-to-class assignments; ISFSCLAS (3f: CLASS/GROUP/EXTRA), ISFSINFO (4f: PROGRAM/CONTRACT/MISC/WHO), ISPRINFO (4f: PROG/DESC/MISC/TYPE) all fully documented; optional add-on module — **C: 62/100**
- [x] 🔄 **GF** — Global Finance / AR Charges (T7GFPRICE: 116 procs, customer+item pricing/charge entry; T7GFV/GFVS: 82/81 procs, invoice charge viewer; T7GFR: 46 procs, report); ISARCHG (26f) fully documented: before/after audit trail with SONUM+INVNUM+LINEID+PCODE+CDATE+USER+REVLVL+ALOC/BLOC+APRICE/BPRICE+ADISC/BDISC+AOOQTY/BOOQTY+AESD/BESD+AASD/BASD+ACOMPR_1/2+BCOMPR_1/2+AEXTRA/BEXTRA; 4 RWN programs confirmed — **C: 62/100**
- [x] 🔄 **RE** — Reminders + Rebuild Utilities (T7RemindRpt: 125 procs, ISREMIND+BKARCUST — CRM/AR reminder report; T7REPLNK: 67 procs, ISREPLNK — replace links; T7REPDEF: 52 procs, ISREPDEF — saved report defaults; T7REINDEX: 36 procs, Btrieve reindex; T7REBQC/REBWO: QC+WO rebuild utilities) — **C: 48/100**
- [x] 🔄 **SE/ST** — Service Code Tables (T7SEPROC: ISSEPROC; T7SERR+T7SETYPE: ISSTYPE/ISSETYPE; T7STEQUIP/T7sttype/T7STYPE: ISSTYPE; T7STOCK: BKCMACCC); code maintenance tables for SR Service/Repair module; ISSEPROC (2f: PROC/WHO), ISSTYPE (3f: TYPE/WHO/ASSET), ISSETYPE (2f: ERR/WHO) all fully documented; 7 RWN programs identified; T7STEQUIP opens 90+ tables including BKARINV/BKISTAX/BKARDEP confirming cross-module use — **C: 60/100**
- [x] 🔄 **PU** — Warehouse Put-Away (T7PUTAWAY: 105 procs); places received PO items into bin locations; updates BKICMSTR/MTICMSTR; full DB set: BKICMSTR+MTICMSTR+BKAPINVL+BKAPPO+BKGLTRAN+DBAFIFO+LOT+SERIAL+ISORDECO+BKCMACCT+60 more; workflow confirmed: AP receiving→bin assignment→lot/serial tracking→GL posting; single-program module — **C: 62/100**
- [x] 🔄 **MU** — Multi-Yield Work Orders (T7MULTIYIELD: 150 procs); records multiple co-product output part numbers from single WO; full DB set confirmed: WORKORD+WOROUT+WOBOM+WORECV+INVTXN+ISBINLOC+BKARINVL+MTICMSTR+BKICLOC+WOMAT+ISWOEX+LOT+ISBINLOT+SERIAL+BKGLTRAN+BKGLX+DBAFIFO+ISTRIGRS; ISWOEX (WO extended, not in DDF) holds multi-yield state; workflow confirmed (input WO→multiple WORECV+INVTXN outputs→FIFO/LOT/SERIAL tracking) — **C: 62/100**
- [x] 🔄 **AL** — Audit Log Setup (T7ALOGSETUP: 43 procs, FILELOC+BKSYMSTR+BKPSUSER); configures which tables/events are written to system audit log — **C: 40/100**
- [x] 🔄 **LI** — License / Module Access (T7LIMACC: 42 procs, ISACCESS); controls which EvoERP modules are licensed/enabled; ISACCESS confirmed used across 20+ programs as module gate; not in DDF (not registered in Pervasive schema) — single-table maintenance program — **C: 52/100**
- [x] 🔄 **ML** — Multi-Language (T7MLC: 50 procs, LANGDICT+BKARINV+BKARINVL+ISREPORD); multilingual AR invoice support — **C: 38/100**
- [x] 🔄 **MH** — Shipping Configuration (T7MHOPE: 98 procs, ISSHIPCO+ISSHPVIA+BKCMTERR+BKARINV+ISREPORD); carrier–territory–ship-via relationship config — **C: 42/100**
- [x] 🔄 **ED (EDII)** — EDI Invoice Import (T7EDII: 183 procs); creates AR invoices from inbound EDI with pricing+charges; opens BKARINV+BKARINVL+ISARCHG+BKARCUST+ISTERMS+BKICPMAT+BKICLOC+CLASMSTR — **C: 45/100**
- [x] 🔄 **BR** — Brands Master (T7BRANDS: 53 procs, BKCMACCC); product brand master linked to CRM account classifications; T7BROWSER: HTML browser wrapper — **C: 40/100**
- [x] 🔄 **NE** — New Company Init (T7NEWINIT: 49 procs, FILELOC+FILEDES); creates all Btrieve data files for a new company — **C: 42/100**
- [x] 🔄 **CU** — WO Cut Sheet (T7CUTSHEET2: 75 procs, WOMAT+LOT+WORKORD+WOBOM+ISBINLOT+BKPSUSER); material cut sheet for shop floor with lot+bin tracking — **C: 45/100**
- [x] 🔄 **JO** — Jobs / Departments (t7jobs: 21 procs, ISDEPT+BKARCUST+BKAPVEND+WOEXCHG+CLASMSTR+ISCATMST); HR job positions and department master — **C: 38/100**
- [x] 🔄 **FN** — File Navigator (T7FNR: 104 procs, FILELOC+FILEDICT); Btrieve file/data-dictionary browser and report — admin tool — **C: 42/100**
- [x] 🔄 **XC** — CC Cross-Reference Utility (T7XCUTIL: 29 procs, BKCMACCT+ISCC+LANGDICT); credit card record reconciliation across CRM and billing — **C: 38/100**
- [x] 🔄 **LG** — LGS Customer Module (t7lgssoe: 170 procs + T7LGSSOEVerify: 41 procs); customer-specific customization (similar to J7* but LGS prefix); processes AR invoices with tax/customs via BKARTXN+BKICTAX; "SOE" likely = Statement of Entry — **C: 35/100**
- [x] 🔄 **JS** — JS Integration / Reporting Bridges (7 modules: jsettings, jsql, jsacc, jsaIc, jsaPBI, jsaSRS, jsoi); settings + SQL tool + data bridges for Power BI and SQL Reporting Services external reporting — **C: 42/100**
- [x] 🔄 **BS** — Business Score/Summary Dashboard (T7BS: 162 procs); ISBSF (143f, fully documented): PK=STARTDATE+ENDDATE; AR/AP/SO/PO/WO/IC KPIs + CASH_TOTA+ACT1..9 + CASH_ACTS_1..100 (100-period GL history) + WOS_SETUP/LAB/OUTP/MAT/FOH/VOH/MEXT/FP/WIPV (WO cost breakdown) + EXTRA; opens 40+ tables including all major modules; also surfaced as QU-D Business Status (EVOBS) — **C: 65/100**
- [x] 🔄 **AD (ADCA)** — Advanced Data Collection (T7ADCA: 290 procs — largest DC module; BKDCLAB+WORKORD+BKPRMSTR+BKDCSHFT+ISWOEX+EIMCOLST); full automatic DC entry for shop floor — **C: 48/100**
- [x] 🔄 **IT** — Item Serial Counter Config (T7ITMCFG: 66 procs, ISSERCNT+BKICMSTR); configures serial number generation counters per item — **C: 40/100**
- [x] 🔄 **EM** — Emergency GL Maintenance (T7EMGL: 62 procs, BKGLCOA); raw GL account edit mode — **C: 38/100**

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
- [x] ✅ Scheduler job table = **ISSCHED** — confirmed 2026-06-17 from DB fingerprints (EvoSched.RWN, EvoScheduler.RWN, EVOSERVICE.RWN all open ISSCHED); SCHEDCAL used by shop scheduling module
- [x] ✅ EvoRemind (evoremind.RWN: 46 procs) opens ISREMIND+BKYSMSTR+BKSYUSER+ISTRIGRS+BKPSUSER+BKAPPOL — links reminders to PO/AR transactions; ISTRIGRS = trigger result log
- [ ] ⬜ ISSCHED all fields documented
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
- [x] ✅ Attachment storage table = **ISLINKS** — confirmed 2026-06-17 (EvoLinks.RWN opens ISLINKS as primary; ISLINKS = record-key → document filename cross-reference)
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
- [x] 🔄 T7SMJ* drill-down panel family decoded (18 modules, 2026-06-17): SMJA/B=WO, SMJC/D=Inventory+FIFO, SMJF/R=PO, SMJG=QC, SMJH=DC Labor, SMJI=Estimates, SMJJ/K=SO/Invoice, SMJL=Master (459 procs, 92 tables), SMJM=Customers, SMJN=Vendors, SMJO=AR/AP, SMJQ=Item/BOM, SMJS=Item, SMJV=Payroll; 16 new tables confirmed — **C: 72/100**
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

- [x] ✅ All 50 J7\* RWN modules inventoried (Pass 18, 2026-06-17) — **C: 88/100**
- [x] ✅ 16 DFM files read; form titles and field labels extracted — **C: 88/100**
- [x] ✅ J7\* prefix = i2 Systems customization namespace (confirmed from J7i2SystemSOOE, J7I2SACH) — **C: 90/100**
- [x] ✅ Business context confirmed: i2 Systems = corrugated packaging + mattress components manufacturer; customers include Lapco, Albertsons — **C: 90/100**
- [x] ✅ All 50 modules categorized by functional area (CC=corrugated, HH=handheld, DC=data collection, customer integrations) — **C: 85/100**
- [x] ✅ Core tables used by J7 modules confirmed: BKICMSTR, BKARINV/L, BKAPPOL, ISARTXNB, ISWOTRAY — **C: 80/100**
- [ ] ⬜ J7 RWN internal logic (blocked by encryption — see §14)
- [ ] ⬜ Custom J7-specific tables (if any) — not yet confirmed to exist

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

- [x] ✅ `.RWN` / `.DCY` encryption — **FULLY SOLVED C: 100/100** (2026-06-16)
  - [x] ✅ Encryption algorithm: Twofish-192, CFB-128 mode — **C: 100/100**
  - [x] ✅ Key derivation: SHA1(runtime_passphrase)[0:20] + 4 zeros → 192-bit key — **C: 100/100**
  - [x] ✅ RWN key K_B = `a898d21e2fd6ca294026e5d633d9047f91f7ed35` (live Frida capture) — **C: 100/100**
  - [x] ✅ DCY key K_D = `691e8041ab265b4e6ee052ccc946dba4caac60da` (live Frida capture) — **C: 100/100**
  - [x] ✅ "mabufoju" passphrase was WRONG — actual passphrase unknown but not needed — **C: 100/100**
  - [x] ✅ IV param always 0; P_initial = Encrypt_K(zeros); body P_start = K0 = Encrypt_K(P_initial) — **C: 100/100**
  - [x] ✅ Validation: first 8 bytes; pt[0:4]==pt[4:8] — **C: 100/100**
  - [x] ✅ Q-box tables (q0 at file 0x7740A8, q1 at 0x7741A8) verified against NIST Twofish spec — **C: 95/100**
  - [x] ✅ `twofish_pure.py` passes NIST 192-bit test vector — **C: 95/100**
  - [x] ✅ `scripts/rwn_decrypt.py` — batch RWN decryptor, correct K_B key, P_start=K0 — **C: 100/100**
  - [x] ✅ `scripts/dcy_decrypt.py` — batch DCY decryptor, correct K_D key, P_start=K0 — **C: 100/100**
  - [x] ✅ MDUMMY.DCY decrypts to `object EditForm1: TEditForm1...` (DFM content) — **C: 100/100**
  - [x] ✅ 5/5 sample RWN files decrypt successfully — **C: 100/100**
  - [x] 🔄 K_C = **suwin6.dcy** encryption key (confirmed 2026-06-17 — validation PASS; content is binary, not Delphi VCL text)
  - [ ] ⬜ K_A purpose still unknown (tried against all suwin files — none pass)
  - [ ] ⬜ suwin7.dcy — fails all 4 known keys; 5th key or different format
  - Note: See `docs/02-file-formats/decryption-findings.md` for complete algorithm spec
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

**Status:** Many tier-1 tables now documented in tier1–tier5-tables.md.

### Priority Tier 1 — Core Transaction Tables (must reach C: 80+ to hit 90% goal)
- [x] ✅ BKARCUST — AR Customer master — tier1-tables.md **C: 82/100**
- [x] ✅ BKARINV — AR Invoice header — tier1-tables.md **C: 78/100**
- [x] ✅ BKARINVL — AR Invoice detail — tier1-tables.md **C: 78/100**
- [x] ✅ BKARINVT — AR Payment application (= "BKARPMT") — tier1-tables.md **C: 78/100**
- [x] ✅ BKARDEP — AR Customer deposits — tier1-tables.md **C: 72/100**
- [x] ✅ BKARCHKH/F — AP Check history — tier1-tables.md **C: 78/100**
- [x] ✅ BKAPVEND — AP Vendor master — tier1-tables.md **C: 80/100**
- [ ] ⬜ BKAPINVH — AP Invoice header (not yet found in schema — may be BKAPINV)
- [x] ✅ BKAPINVL — AP Invoice detail — tier1-tables.md **C: 78/100**
- [x] ✅ BKAPCHKH — AP Check header — tier1-tables.md **C: 78/100**
- [x] ✅ BKICMSTR — Inventory Item master — tier1-tables.md **C: 75/100**
- [x] ✅ BKGLCOA — GL Chart of Accounts — tier1-tables.md **C: 80/100**
- [x] ✅ BKGLTRAN — GL Journal transactions — tier1-tables.md **C: 80/100**
- [x] ✅ WORKORD — Work Order header — tier1-tables.md **C: 80/100**
- [x] ✅ WORKCHG — Work Order detail / charges — tier1-tables.md **C: 78/100**
- [x] ✅ BKBMMSTR — BOM master — tier3-tables.md **C: 78/100**
- [x] ✅ BKBMAVAL/BKBMAMTR — BOM components — tier3-tables.md **C: 75/100**
- [x] ✅ AHSYLOG — User security — tier1-tables.md **C: 82/100**
- [ ] ⬜ ISJAVA — Java task queue — documented in architecture but not schema-page
- [x] ✅ BKLOGON — Active sessions — tier1-tables.md **C: 78/100**
- [x] ✅ BKSYMSTR — System configuration — tier1-tables.md **C: 72/100**

### Priority Tier 2 — Supporting Tables
- [ ] ⬜ All remaining BKAP\* (24 tables)
- [ ] ⬜ All remaining BKAR\* (27 tables)
- [ ] ⬜ All remaining BKGL\* (28 tables)
- [x] 🔄 All remaining BKIC\* (16 tables) — BKICLOC (32f, per-location quantities + GL accounts), BKICLOCM (12f, location master with TAXGR), BKICPMAT (85f, customer price matrix 10-break), BKICDIM (47f, dimensions/alloy/temper/finish/tolerances), BKICTAX (46f, state tax with 12-month collection), BKICREQ (41f, requisitions + 10 notes); BKICAMTR/BKICEMTR + MTICAMTR/MTICEMTR confirmed as 108-field MTICMSTR clones (actual/estimated cost snapshots); ~10 tables not yet extracted — **C: 60/100**
- [ ] ⬜ All remaining WO\* (30 tables)
- [ ] ⬜ All remaining BKPR\* (16 tables) including BKPRMSTR (384 fields)
- [ ] ⬜ All remaining BKBM\* (10 tables)
- [x] 🔄 All remaining BKCM\* (46 tables) — top 5 field-documented (BKCMACCN 154, BKCMCUST 106, BKCMMHST 72, BKCMACCT 41, BKCMREP 14); 41 smaller tables identified but not field-extracted — **C: 55/100**
- [ ] ⬜ All remaining BKSO\* (7 tables)
- [ ] ⬜ All remaining BKDC\* (7 tables)
- [x] 🔄 All remaining IS\* tables — ISLBLMAP (102f), IS2DBAR (109f), ISSCHED (24f), ISNOTES (13f); ISSRMMS (12f, SR equip), ISSRINFO (54f, SR ext), ISSOREVU (12f, approval), ISARINVX (4f, AR ext), ISSDET (4f), ISORDECO (13f), ISNTYPE (4f), ISUDFINV (8f), BKISTAX (13f), BKARHTAX (5f), ISARTXNB (23f) fully field-documented; ~220 IS\* remaining — **C: 52/100**
- [x] ✅ BKSLEVEL (422 fields) — 20-menu × 20-op security matrix; PK=BKSL_MENU+BKSL_LEVEL; MENU{N}_YN = quick access flag; MENU{N}_1..20 = per-op flags — **C: 82/100**
- [x] ✅ BKPRGLFL (664 fields) — payroll GL posting config; PK=STCODE+DEPT; standard taxes (FIT/FICA/FUTA/SUTA/SIT/SDI/WC/Medicare) each with GL acct+dept+rate+limit; 20 user-defined deductions × 13 sub-fields; 20 user-defined earnings; 46 tax-output/vendor slots — **C: 82/100**

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
| File Formats — RWN/DCY | 88 | 90 | 2 | 2026-06-16 |
| File Formats — RTM | 78 | 88 | 10 | 2026-06-11 |
| File Formats — Btrieve | 72 | 85 | 13 | 2026-06-11 |
| TAS 4GL Language | 75 | 92 | 17 | 2026-06-11 |
| Database Schema (structure) | 90 | 95 | 5 | 2026-06-11 |
| Database Schema (field meaning) | **78** | 88 | **10** ↑ | 2026-06-17 |
| Security / Login | **78** | 85 | **7** ↑ | 2026-06-17 |
| Menu System | 78 | 90 | 12 | 2026-06-11 |
| Module: AR | **80** | 85 | **5** ↑ | 2026-06-17 |
| Module: AP | **82** | 85 | **3** ↑ | 2026-06-16 |
| Module: IN/Inventory | **77** | 85 | **8** ↑ | 2026-06-17 |
| Module: SO | **75** | 85 | **10** ↑ | 2026-06-17 |
| Module: PO | **72** | 85 | **13** ↑ | 2026-06-16 |
| Module: WO | **83** | 85 | **2** ↑ +3 | 2026-06-17 |
| Module: GL | **87** | 88 | **1** ↑ | 2026-06-17 |
| Module: BM/MRP | **78** | 80 | **2** ↑ | 2026-06-17 |
| Module: RO/Routing | **82** | 85 | **3** ↑ | 2026-06-17 |
| Module: DC/Data Collection | **82** | 82 | **0** ✅ | 2026-06-17 |
| Module: PR/Payroll | **70** | 80 | **10** ↑ | 2026-06-17 |
| Module: AM (Accounting Maint.) | **75** | 85 | **10** ↑ NEW | 2026-06-11 |
| Module: CM/CRM | **72** | 80 | **8** ↑ | 2026-06-17 |
| Module: DE/EDI/Imports | **68** | 80 | **12** ↑ | 2026-06-15 |
| Module: CS/Commission+Salesperson | **78** | 80 | **2** ↑ | 2026-06-17 |
| Module: JC/Job Costing | **72** | 75 | **3** ↑ | 2026-06-17 |
| Module: SC/Serial Control ⚠️ | **80** | 80 | **0** ✅ | 2026-06-17 |
| Module: QC/Quality Control | **65** | 75 | **10** ↑ | 2026-06-17 |
| Module: WC/Warehouse Control ⚠️ | **72** | 80 | **8** ↑ +17 | 2026-06-15 |
| Module: SH/Shop Scheduling ⚠️ | **72** | 80 | **8** ↑ +27 | 2026-06-15 |
| Module: LC/Lot Control | **80** | 78 | **0** ✅ | 2026-06-17 |
| Module: SR/Service Repair | **72** | 75 | **3** ↑ | 2026-06-17 |
| Module: FA/Fixed Assets | **75** | 80 | **5** ↑ +27 | 2026-06-15 |
| Module: PI/Physical Inventory | **75** | 78 | **3** ↑ | 2026-06-17 |
| Module: MA/AR Deposits | **62** | 65 | **3** ↑+22 | 2026-06-17 |
| Module: ES/Estimating | **65** | 75 | **10** ↑ | 2026-06-17 |
| Module: SA/Sales Analysis | **68** | 75 | **7** ↑ | 2026-06-17 |
| Module: AC/Activity Control | **60** | 70 | **10** ↑ +15 | 2026-06-17 |
| Module: CC/Credit Card ⚠️ | **65** | 78 | **13** NEW | 2026-06-15 |
| Module: SP/SPC ⚠️ | **60** | 75 | **15** NEW | 2026-06-15 |
| Module: HH/Handheld | **68** | 80 | **12** NEW | 2026-06-15 |
| Module: UT/Utilities | **60** | 75 | **15** NEW | 2026-06-15 |
| Module: RM/RMA | **68** | 78 | **10** NEW | 2026-06-15 |
| Module: FO/Features Options | **65** | 70 | **5** ↑ | 2026-06-17 |
| Module: IS/InfoSystem | **60** | 65 | **5** ↑ +15 | 2026-06-17 |
| Module: IM/Landed Cost | **70** | 80 | **10** NEW | 2026-06-15 |
| Module: PS/Program Security | **60** | 75 | **15** NEW | 2026-06-15 |
| Module: QU/Query Tools | **70** | 75 | **5** ↑ | 2026-06-17 |
| Module: SU/Setup UI | **65** | 70 | **5** ↑ | 2026-06-17 |
| Module: TA/TAS Admin | **55** | 72 | **17** NEW | 2026-06-15 |
| Module: DI/Digital Signatures | **65** | 70 | **5** ↑+15 | 2026-06-17 |
| Module: AD/Accounting Defaults | **70** | 75 | **5** ↑ | 2026-06-17 |
| Module: CR/SO Approvals | **55** | 65 | **10** ↑ +15 | 2026-06-17 |
| Module: US/Triggers | **65** | 65 | **0** ✅+20 | 2026-06-17 |
| Subsystem: BO/Bill of Lading | **58** | 72 | **14** NEW | 2026-06-17 |
| Subsystem: DS/Data Sync stubs | **42** | 65 | **23** NEW | 2026-06-17 |
| Subsystem: AU/Automation | **52** | 68 | **16** ↑ +4 | 2026-06-17 |
| Subsystem: FS/Field Service | **62** | 65 | **3** ↑+17 | 2026-06-17 |
| Subsystem: GF/AR Charges | **62** | 65 | **3** ↑+17 | 2026-06-17 |
| Subsystem: RE/Reminders+Rebuild | **48** | 65 | **17** NEW | 2026-06-17 |
| Subsystem: SE+ST/Service Code Tables | **60** | 60 | **0** ✅+18 | 2026-06-17 |
| Subsystem: PU/Put-Away | **62** | 65 | **3** ↑+20 | 2026-06-17 |
| Subsystem: MU/Multi-Yield WO | **62** | 68 | **6** ↑+17 | 2026-06-17 |
| Subsystem: LI/License Access | **52** | 65 | **13** ↑+12 | 2026-06-17 |
| Subsystem: EDII/EDI Invoice Import | **45** | 65 | **20** NEW | 2026-06-17 |
| Subsystem: LG/LGS Custom | **35** | 55 | **20** NEW | 2026-06-17 |
| Subsystem: JS/Reporting Bridges | **42** | 60 | **18** NEW | 2026-06-17 |
| Subsystem: BS/Business Score | **65** | 65 | **0** ✅+23 | 2026-06-17 |
| Subsystem: AD/Advanced DC | **48** | 65 | **17** NEW | 2026-06-17 |
| Subsystem: IT/Item Serial Config | **40** | 60 | **20** NEW | 2026-06-17 |
| Module: SD/Standard Detail | **42** | 60 | **18** ↑ +12 | 2026-06-17 |
| Module: RF/RFQ | **50** | 68 | **18** ↑ +10 | 2026-06-17 |
| Platform Subsystems | **75** | 82 | **7** ↑ +3 | 2026-06-17 |
| Subsystem: PI/Physical Inventory | **52** | 68 | **16** NEW | 2026-06-17 |
| Module: SA/Sales Analysis | **58** | 72 | **14** ↑ +3 | 2026-06-17 |
| Module: JC/Job Cost | **68** | 78 | **10** ↑ | 2026-06-17 |
| Module: ES/Estimating | **58** | 72 | **14** ↑ | 2026-06-17 |
| Platform: WBKLOOKUP/Lookup Framework | **55** | 70 | **15** NEW | 2026-06-17 |
| Module: DE/DC stubs+EDI processing | **65** | 75 | **10** ↑ +5 | 2026-06-17 |
| Module: SM/System Maintenance+Item Inquiry | **65** | 80 | **15** NEW | 2026-06-17 |
| Module: MR/MRP Engine | **62** | 78 | **16** NEW | 2026-06-17 |
| Module: TC/Treasury Control | **52** | 70 | **18** NEW | 2026-06-17 |
| Module: SC/Cycle Count | **58** | 72 | **14** NEW | 2026-06-17 |
| Module: CH/Multi-Location Chain | **45** | 65 | **20** NEW | 2026-06-17 |
| Module: KI/Kit Assembly | **50** | 70 | **20** NEW | 2026-06-17 |
| Module: MA/AR Deposit Apply | **52** | 68 | **16** NEW | 2026-06-17 |
| Module: TE/NACHA+ACH | **48** | 65 | **17** NEW | 2026-06-17 |
| Module: PA/Paperless DC | **45** | 68 | **23** NEW | 2026-06-17 |
| Module: TPOA/PO Processing Hub | **58** | 72 | **14** NEW | 2026-06-17 |
| System: AUTO/Batch Automation | **52** | 68 | **16** NEW | 2026-06-17 |
| Module: FO/Features+Options | **60** | 72 | **12** ↑ +10 | 2026-06-17 |
| System: Notes/EVONOTES | **58** | 70 | **12** NEW | 2026-06-17 |
| Modules: AB/CP/EX/FL/LM/MA/MM/PC/PL/RT/SB/SL/SY/UM/UP/YS (16 opaque) | 15 | 50 | 35 | 2026-06-15 |
| RWN String Analysis technique | **82** | 90 | **8** NEW | 2026-06-11 |
| Reporting Engine | 75 | 88 | 13 | 2026-06-11 |
| Platform Subsystems | **72** | 82 | **10** ↑ +7 | 2026-06-17 |
| Java Integration | 73 | 85 | 12 | 2026-06-11 |
| ODBC Connectivity | 85 | 92 | 7 | 2026-06-11 |
| Customizations (J7\*) | **72** | 80 | **8** ↑ +7 | 2026-06-17 |
| Business Workflows | **62** | 85 | **23** ↑ | 2026-06-11 |
| Encryption / RWN Decryption | 100 | 95 | 0 ✅ | 2026-06-16 |
| Per-Table Narrative Docs | **68** | 88 | **20** ↑ +10 | 2026-06-17 |
| PROJECT-STRUCTURE.md | **72** | 90 | **18** ↑ | 2026-06-11 |
| HELP-RESOURCES.md | **75** | 90 | **15** ↑ +10 | 2026-06-15 |

### Critical Path to 90% Goal

**Key finding (2026-06-12):** Only **7 `.SRC` files** exist on the network share — all are TAS
Pro 6 era holdovers already analyzed. The entire TAS Pro 7 program logic (1,124 `.RWN` files)
exists only as encrypted binary. There is no plaintext source code for any current module.
This makes `.RWN` decryption the **single highest-leverage unlock** in the project.

Priority order — in sequence, each unblocks the next:

| # | Task | Status | Impact |
|---|------|--------|--------|
| ~~**1**~~ | ~~Debugger session to recover IV~~ | ✅ **DONE 2026-06-16** — K_B and K_D captured live via Frida; IV derivation proven deterministic | Unlocked #2/#3 |
| ~~**2**~~ | ~~Write `rwn_decrypt.py` and decrypt all 1,124 `.RWN` files~~ | ✅ **DONE 2026-06-16** — `scripts/rwn_decrypt.py` with K_B; batch run against share completed; symbol extractor `scripts/rwn_extract_symbols.py` created | Variable names + DB files from all modules now extractable |
| ~~**3**~~ | ~~Decode `.DCY` files~~ | ✅ **DONE 2026-06-16** — `scripts/dcy_decrypt.py` with K_D; 41/48 files OK; format = Delphi VCL forms | Menu form and login forms decryptable |
| **4** | Re-decrypt all 1,124 `.RWN` files locally (existing `rwn_decrypted/` used wrong key) | ⬜ **NOT STARTED** — copy files to `samples/` then run `rwn_decrypt.py`; batch extractor will produce symbol catalog | Full module variable/DB catalog |
| **5** | Map `.RWN` bytecode instruction set via Rosetta Stone | 🔄 **C: 15/100** — dispatch table mapped; 7 opcode DWORDs in suwin7.rwn; full mapping needs BKMRF 3-way compile diff | Full logic traceability |
| **6** | Per-table field meaning documentation (659 tables) | 🔄 **C: 48/100** — Tier 1 tables partially done; 659 × full semantic docs needed | Database understanding |
| **7** | Module-by-module logic from decoded `.RWN` variable patterns | 🔄 **started** — T7INA variables confirm buffer field names; EvoERPmenu confirms menu tables | Module confidence to 85+ |
| **7** | Business workflow recipes (end-to-end traces: SO→ship→invoice, WO lifecycle, AP check run, etc.) | #6 | Me | Operational understanding |
| **8** | Analyze 1,273 `.RUN` files (TAS Pro 6, unencrypted compiled format — partial window into legacy logic) | None — unblocked now | Me | Legacy module coverage |
| **9** | Reverse-engineer `ENCRYPTSTR`/`DECRYPTSTR` (password hashing + string crypto in `tp7runtime.exe`) | None — unblocked | Me | Security model complete |
| **10** | Decode `WHOAMI.DBA` (35 bytes), `CHMHELP.EVO` (35 bytes), fill remaining `.INI` keys | None — unblocked | Me | Infrastructure gaps |
| **11** | Map all 554 menu codes → implementing file → `.DFM` form → tables | #2 (for RWN-backed codes) | Me | Navigation complete |
| **12** | TAS 4GL language gaps (full grammar, operators, scope rules, all built-ins) | #2 | Me | Language spec complete |
| **13** | Security model detail (AHSY_USER_ACCES mapping, password algorithm, WHOAMI validation) | #2, #9 | Me | Security complete |
| **14** | Per-form narrative docs (1,109 forms × field labels, purpose, linked tables) | None — unblocked | Me | UI reference complete |
| **15** | Per-report docs (899 RTM files × data fields, parameters, output columns) | None — unblocked | Me | Reporting reference |

**Biggest gaps blocking the 90% target, by area:**

1. **RWN decryption** — 1,124 programs with zero readable logic until IV is solved
2. **Per-table field meaning** — 659 tables × semantics = largest volume task
3. **Business workflow recipes** — no end-to-end processes yet documented
4. **~16 still-opaque modules** — AB, CP, EX, FL, LM, MA, MM, PC, PL, RT, SB, SL, SY, UM, UP, YS — no DFMs, no CHM; require RWN decryption or live instance access. (35+ others now documented via DFM analysis.)
5. **Bytecode format** — needed to interpret decrypted `.RWN` content
6. **Security model detail** — access flags, password algorithm, WHOAMI validation

---

*Last updated: 2026-06-17 (pass 4)*
*Document location: `EVO-DECOMPILE-TODO.md` at workspace root*
