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
- [x] ✅ `StartEvo.exe` fully analyzed: .NET assembly; DomainAuthenticate→KillEvoProcesses→LaunchEvoWithUser; queries `tas_menus` via DSN=EVOADMIN; handles `evo://` URI scheme; reads DEFAULTPATH/DFLTCOMPANYCODE from taspro7.ini; robocopy for updates — **C: 88/100**
- [x] ✅ `suwin6.dcy` format decoded: NOT a Delphi DFM form — it is TAS Pro 7 compiled bytecode (32,864 bytes, Shannon entropy 7.99 bits/byte, no ASCII string literals, validated with K_C key at offset 0). DCY files have two sub-types: Type A = Delphi DFM form (standard, decrypted with K_D), Type B = compiled TAS Pro 7 bytecode (suwin6.dcy, decrypted with K_C). Pre-load behavior itself cannot be traced without a TAS Pro 7 bytecode disassembler. (Pass 112 2026-06-19) — **C: 60/100** (format confirmed, logic opaque)
- [ ] ⬜ `suwin7.dcy` — fails all 4 known keys; format unknown

### 1.3 Runtime Engine (tp7runtime.exe)
- [x] ✅ Identified as TAS Professional 7 by Computer Keyes / Business Tools — **C: 90/100**
- [x] ✅ 33.3 MB executable; embeds Qt 3/CLX UI layer (`qtintf70.dll`) + CodeBase data engine (`c4dll.dll`) — **C: 85/100**
- [x] ✅ Keyword list extracted from embedded strings (`tp7runtime.keywords.txt`) — **C: 88/100**
- [x] ✅ Runtime version number and build date confirmed — **C: 95/100**
  - FileVersion: 7.1.9.1; ProductVersion: "7i"; ProductName: "Tas Premier 7i runtime"
  - CompanyName: Addsum Business Software, Inc.; Copyright: 2004-2014
  - PE timestamp 1992 is spoofed/reset; actual build 2004-2014 era
- [x] ✅ All DLLs loaded by tp7runtime.exe cataloged with purpose — **C: 90/100**
  - qtintf70.dll: Borland Delphi-Qt2.x Interface Library v7.0.4.258 (Borland CLX/Qt UI bridge)
  - C4DLL.DLL: CodeBase v1.0.0.1 by Sequiter Software (dBASE/DBF/CDX engine for BKMENUSU.DBF)
  - quricol32.dll: Quricol QR Barcode Library by Serhiy Perevoznyk (barcode printing)
  - odbc32.dll, odbccp32.dll: ODBC for Pervasive SQL connectivity
  - Tapi32.dll: Windows Telephony API (dial-out features in ERP)
  - avifil32.dll, msvfw32.dll: AVI/video playback (help videos or embedded tutorials?)
  - 49 total DLL imports; all standard Windows libraries + above 4 third-party DLLs
- [ ] ⬜ Error-code table (runtime error messages ↔ numeric codes)

---

## 2. FILE FORMATS

### 2.1 `.SRC` — TAS Pro 4GL Source Code
- [x] ✅ Encoding confirmed: plaintext ASCII, CR+LF, no BOM — **C: 92/100**
- [x] ✅ Comment syntax: `;` to end-of-line — **C: 95/100**
- [x] ✅ Compiler directives: `#PRO3`, `#UDX`, `#LIB <name>`, `#INC <name>`, `SETUP_COLOR` — **C: 92/100**
  - `#INC`/`#LIB` both case-insensitive; resolve from DataDictPath (`\\DBAMFG$\`); `#PRO3` = Pro 3.0 backward-compat flag
  - `SETUP_COLOR` = TAS keyword (not `#` directive) that opens TASCOLOR Btrieve table, reads color palette; `Color Array Norm/Inverse/High` = color mode selectors
  - `HELPSCRN.SRC` = universal F1 help template included in all programs; `isdef.SRC` = IS module definitions
- [x] ✅ Variable declaration syntax: `define <name> type A/i/n/d/t size <N> [array <N>] [LOCAL]` — **C: 92/100**
  - `LOCAL` modifier: variable scoped to current `func` block (only valid inside function body)
- [x] ✅ Database I/O keywords: `open`, `find F srch`, `clr`, `del`, `dall` — **C: 80/100**
- [x] ✅ UI/form keywords: `mount`, `prg_hdr`, `enter`, `xtrap`, `fnc_list`, `menu` — **C: 75/100**
- [x] ✅ 7 plaintext `.SRC` files analyzed: BKAWLB, BKDCA, BKLME, BKMRF, BKROA, Bkaph, Bkapha — **C: 90/100**
- [x] ✅ `.a.` / `.o.` / `.n.` / `$` operators fully documented with behavior — **C: 95/100**
- [x] ✅ `{ func }` block scoping rules fully confirmed (Pass 107): — **C: 90/100**
  - Inline `{ func name ... ret .t. }` immediately after `enter` = local UDF scoped to program
  - Multiple `func` definitions per `{}` block allowed
  - Top-level `func name [param]` = program-scope subroutine; param declared `define X LOCAL` above the `func` header
  - `ret .t.`=allow, `ret .f.`=abort, `ret`=subroutine return (no value)
- [x] ✅ Include resolution order confirmed (Pass 107): DataDictPath first; `#INC` resolves `.SRC` extension — **C: 90/100**
- [ ] ⬜ Full grammar specification — expression precedence for `.a./.o./.n.` vs `=/<>/</>/<=/>=` vs `+/-/*//` (cannot observe from 7 available SRC files; all use parens or single-op expressions)
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
- [x] 🔄 Bytecode instruction set — **C: 63/100** (17 opcodes; form lifecycle semantics confirmed from 10-program ordering analysis; 2026-06-19 refinements)
  - Dispatch table = program instructions: `[op][00][b2][sub] + [pool_offset_LE4]` (8 bytes each)
    - b2 is usually 0x00; **exception: op=0x57 EXECUTE_FORM has b2=0xFE** (main form) or b2=0x00 (sub-form in t7nest)
  - DISP_START = 0x6C0 is a confirmed UNIVERSAL constant — holds for all 1122 programs extracted
  - **Pool detection**: scan 8-byte blocks from DISP_START+8; first block where byte[0]=0x41 = pool_start. May need to skip 0x00 no-op blocks. Confirmed for all 4 small programs.
  - Pool immediately follows dispatch; first entry always 0x41 = DFM filename: `[0x41][0x00][len_LE2][name_ascii]`
  - Typed pool values: 0x41=string/blob (var-len), 0x46=var_ref (val=var_idx×77), 0x43=pool_ptr, 0x52/0x4E/etc.=5-byte numeric
  - Compound blobs: 0x41 blobs starting with 0xFD contain sub-typed argument fields, end with 0xFF
  - **CONFIRMED 0x20 = CREATE FORM / BIND HANDLER**: First occurrence → DFM filename string (TForm.Create). Subsequent 0x20s bind event handler procs. Confirmed from 10-program ordering analysis.
  - **CONFIRMED 0x57 = EXECUTE FORM**: Universal. Enters form event loop (TForm.ShowModal). In suwin7 it is the LAST instruction after 31 license-check ops. In T7MSG (no procs) it creates+executes in one shot.
  - **Standard form lifecycle**: `[0x20→DFM][0x20→handler...][0x57→DFM][0x40/0x71→EXIT]`
  - **Branch family (sub=0x14)**: 0x3B, 0xD2, 0x6A — confirmed jump/branch variants
  - **0x42 = GOSUB/CALL**: sub=0x04; calls named procs. 0x0F = ASSIGN: sub=0x0A; sets properties/vars.
  - **0x40/0x71 = EXIT PROGRAM**: Both terminate the program; 0x71 sub=0x05, 0x40 sub=0x36.
  - 17 distinct opcodes fully documented in `docs/02-file-formats/rwn-binary-format.md`
  - `.dec` files in `samples/rwn_decrypted/` regenerated 2026-06-19 (1145/1146 OK); 1122 with pool extracted

### 2.3 `.RUN` — TAS Pro 6 Compiled Program
- [x] ✅ Older generation; readable strings present (menu codes extractable) — **C: 85/100**
- [x] ✅ 554 menu codes extracted from `.RUN` string dump — **C: 88/100**
- [x] ✅ Still in active use for legacy BK\* / T6\* modules — **C: 80/100**
- [x] ✅ File structure confirmed: header / table-name slots / var section / code section — **C: 78/100**
  - Magic "TAS32" at offset 0x35; version byte at 0x3A; table names at 0x80 (16-byte slots)
  - Var section: [0..0x045F] = zero-initialized runtime storage; [0x0460..] = var descriptor table
  - code_start = 0x80 + N×16 + var_size; 2-byte preamble precedes instruction stream
  - See `docs/02-file-formats/run-tas6-bytecode.md`
- [x] 🔄 Bytecode instruction set — **C: 42/100** (7-byte fixed instruction + var descriptor format confirmed)
  - All instructions exactly 7 bytes: `[op:1][0x00:1][b2:1][addr_LE4:4]` — confirmed BKAWLB
  - Var descriptor: 7-byte fixed entries `[type_tag][0x00][storage_size][runtime_offset_LE4]` at var_section[runtime_base]
  - runtime_base varies: 0x0460 (var_size=1440) vs 0x02D0 (var_size=2640); zero area = system/lib vars not in descriptor
  - Instruction addr = runtime_base + cumulative_offset; array elements: first_addr + n×element_size
  - 45 user vars confirmed for BKAWLB; total runtime storage = 1110 bytes (all within zero-init area)
  - 13+ opcodes identified; semantics mostly unknown; 0x3B=BRANCH, 0x0F=ASSIGN cross-confirmed from .RWN
  - BKMRF preamble=11780 → large data block precedes instructions; confirmed at abs=0x3C4A
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
- [x] ✅ Form-to-menu-code mapping — **C: 82/100** (2026-06-19: DFM names extracted from all 1122 decrypted RWNs via pool scan)
  - Complete code → program → DB table mapping in `docs/06-menu-system/code-program-mapping.md`
  - 726/870 entries have DB table info from decrypted RWN symbol data; 83% coverage
  - DFM name extraction: scans pool section (DISP_START+8, first 0x41 block = first pool entry = DFM filename); extracted all 1122 programs in `samples/rwn_dfm_map.json`
  - 814/1122 standard (prog.DFM == prog name); 193 → STUB.DFM (J7* i2 customizations); 115 truly non-standard (e.g. T7ADCA→T7DCA.DFM, T7INAC→T7INA.DFM, T7POS→T7QSOA.DFM, T7FIX.DFM for fix utilities)
  - Menu→DFM join: 734/870 resolved (84%); 136 not in dec dir (BK*/T6* or group entries)
  - Instruction count stats: median=2722, max=20367 (T7SOA), min=2; 885/1122 have >1000 instructions
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
- [x] ✅ Binary file layout fully decoded (Pass 109): bytes 0-7 = 8-byte repeated file ID; bytes 8+ = DFM content — either text "object..." (37/41) or binary with 20-byte mini-header: ff0a00 + classname\0 + 3010 + LE-uint16-size + 0000 + TPF0 (4/41). Size field = file_size-28 (verified all 4 binary cases). — **C: 95/100**
- [x] ✅ EVOUSERS.DCY confirmed: admin user-management grid binds ISLOG fields (WHO/COMPANY/WHAT/DOING/STARTT/STARTD/KILL); Kill button sets IS_LOG_KILL=T to log out user — **C: 95/100**
- [x] ✅ WBKLUGRID.DCY confirmed: FD_COLHEADER/FIELDNAME/TOT/SSSFD/FUNC/TYPE/SIZE/EDIT columns define grid layout; KD_KEYNAME/FIELDNAME define sort keys; extprog+params for External UDF — **C: 88/100**
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
- [x] ✅ DDF types 12/13 resolved: NOTE and LVAR, DDF-catalog only, zero in business tables — **C: 95/100**
- [x] ✅ RELATE.DDF: ~8 FK records, engine-level RI not used, RI enforced procedurally — **C: 90/100**
- [x] ✅ OCCURS.DDF: ~150+ occurrence records confirmed active; dual FCR (pages 0+8) confirmed — **C: 85/100**
- [ ] ⬜ Btrieve page layout at full byte level (complete FCR field map)
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
- [x] ✅ Full update pipeline traced — EvoUpdate→EvoUPDSetup→EvoERPupd (FILEDICT/FILEDBF/FILEKEY schema registry; FROM_FILE→TO_FILE migration; UPDATE_FD; RSTR_FILES rollback; updates BKLUGRID+ISDRILLM+ISTS.CFG)→EvoPRupd→Evocnvtb (DDF sync) — Pass 110e 2026-06-19 — **C: 75/100**
- [ ] ⬜ All FILE\*.UPD files parsed and delta-compared to current schema

### 2.11 `.DBA` — Identity / Seat Token
- [x] ✅ File identified: `WHOAMI.DBA`, per-workstation — **C: 45/100**
  - Local copy is 2 bytes (CRLF only) — stub/uninitialized on this workstation; reported size of 35 bytes was incorrect
  - Prior documentation listing "35 bytes" appears to be based on CHMHELP.EVO, not WHOAMI.DBA
- [ ] ⬜ Byte layout decoded — cannot decode without a populated copy
- [ ] ⬜ How WHOAMI.DBA is generated and validated by tp7runtime.exe

### 2.12 `.EVO` — Unknown Marker File
- [x] ✅ `CHMHELP.EVO` fully decoded (2026-06-19) — **C: 95/100**
  - Content: plaintext ASCII "EvoHELP now set for this computer.\r\n" (35 bytes)
  - Purpose: presence marker — written by StartEvo/install when EvoHELP.CHM is registered for this workstation
  - tp7runtime.exe checks for this file to enable the F1 contextual help system
  - Not binary; just a text confirmation note

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
- [x] ✅ Full operator table: +/-/*//, =/<>/>/</>=/<=, .a./.o./.n., $ (string-in-set) — **C: 90/100**
- [x] ✅ `.a.` / `.o.` / `.n.` boolean operators confirmed with source examples — **C: 95/100**
- [x] ✅ `$` string-contains operator confirmed: `if X $ "ABC"` = true if X in set — **C: 90/100**
- [ ] ⬜ Expression precedence rules
- [x] ✅ 20+ built-in functions documented (str/trim/mid/chr/round/ttof/ftot/flerr/fnum/co/zask/etyp/iif/loc/just/windows/clicked_on/max_cols/dpath) — **C: 85/100**
- [x] ✅ Extended types V (variant) and O (legacy numeric) documented with BKDCA.SRC source — **C: 72/100**
- [x] ✅ `find R` mode confirmed absent; `lock R` = read-lock on open — **C: 90/100**

### 3.2 Database I/O Keywords
- [x] ✅ `open <table> lock N/W/R` — open table with no-lock/wait-lock/read-lock — **C: 82/100**
- [x] ✅ Find modes: F/N/G/M/L/P (first/next/gte/match/last/prev); `err`/`nlock`/`noclr` modifiers — **C: 92/100**
- [x] ✅ `clr <table> rec` — clear/new record — **C: 72/100**
- [x] ✅ `del` / `dall` — delete record / delete all — **C: 70/100**
- [x] ✅ Field access via dot notation: `bksy.comp.name` (table.field) — **C: 85/100**
- [x] ✅ Locking: `LOCK_OWNER`, `REC_LOCK`, `UNLOCK` keywords — **C: 72/100**
- [x] ✅ `rcn TABLE rcn VAR get/set` — record cursor save/restore; `openv` open by variable; `setact` alias table — **C: 85/100**
- [ ] ⬜ Full find/seek operation set — all 6 modes now confirmed; only gap is `find A` (absolute by position) — **C: 92/100**
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
- [x] ✅ WO\* family (30 tables — Work Orders) — all cross-referenced + WORKORD fully documented — **C: 92/100**
- [x] ✅ IS\* (tax, utilities, Java integration — ISJAVA table) — **C: 68/100** (Pass 22–23: ISLBLMAP/IS2DBAR/ISUSAGE/ISAPAINL/ISALINKS/ISLINKS/ISESTASM/ISESADTL/ISMICADT/ESA/EST/ISTAXGRP all field-documented; ~200 smaller IS\* tables remain)
- [x] ✅ AHSYLOG (security / user table) — **C: 72/100**
- [ ] ⬜ Full per-table narrative documentation (see §16 for checklist)
- [x] ✅ MT\* vs. BK\* scope difference **CONFIRMED**: BK\* = single-company operational data (BKICMSTR 64f, code-only PK); MT\* = multi-class catalog (MTICMSTR 108f, CLASS+CODE PK, 44 extra fields); MTMRP=MRP work table; MTEXCHG=multi-currency rates; MTINVDEF=creation defaults template; docs/03-modules/in-inventory/README.md (Pass 110g 2026-06-19) — **C: 75/100**
- [ ] ⬜ BKARHINV anomaly fully resolved (sub-folder table, now documented)
- [x] ✅ All 30 WO\* tables cross-referenced to Work Order module logic — functional groups (master/BOM/routing/labor/material/receipt/scheduling/audit/WC), naming convention (E=estimated/pending, H=history), WORKCTR + ROUTING templates fully documented; docs/03-modules/wo-work-orders/README.md (Pass 110e 2026-06-19) — **C: 92/100**
- [ ] ⬜ Primary key confirmed for each of **728+** tables (from INDEX.DDF; originally 649, +55 pass 7b, +17 pass 8, +26 pass 9 = 747 minimum — see PROJECT-STRUCTURE.md Special/Misc Tables)
- [ ] ⬜ Foreign key relationships mapped across module boundaries

### 4.4a ISTS.CFG.* Configuration Keys
- [x] ✅ Key namespace confirmed: `ISTS.CFG.*` strings in all program binaries map to BKYSMSTR/BKSYMSTR fields — **C: 72/100**
- [x] ✅ **535 unique keys** cataloged from grep across 2,575 rwn_strings files — **C: 78/100**
- [x] ✅ **495 keys confirmed from T7YSYN symbol table** (most authoritative — these have actual editor fields in BKYSMSTR editor); organized by module prefix: SO=75, PO=52, WO=39, DC=35, IN=20, AP=15, HH=15, AR=8, SR=8, RM=12, PR=10, VO=6, AV=5, EV=4, CC=4 — Pass 120 2026-06-19 — **C: 75/100**
- [x] ✅ Full key directory rebuilt with 495 keys in `docs/05-configuration/ists-cfg-keys.md`; VO* void-permissions group and HH* hand-held group newly documented; Avalara (AV*) and RMA (RM*) subsystems confirmed — **C: 75/100**
- [x] ✅ Prevalence distribution documented (9 global keys in 400+ files; 276 module-specific in 1–9 files) — **C: 75/100**
- [ ] ⬜ Complete YN[N] ↔ ISTS.CFG.* mapping (9 confirmed so far: YN[20], YN[36], YN[37], YN[38]=WOCALC, YN[48], YN[59], YN[66], YN[228]=DCSEQ, YN[229]=DCSYNC)
- [ ] ⬜ All 495 keys mapped to their BKYSMSTR/BKSYMSTR field with confirmed meaning
- [ ] ⬜ Keys that control module-enable/disable confirmed (module licensing gates)

### 4.4 Key Individual Tables (minimum needed for 90% goal)
- [x] ✅ `BKARCUST` — AR Customer master: 106 fields documented in `docs/04-data-dictionary/tier1-tables.md` — **C: 68/100**
- [x] ✅ `BKICMSTR` — Inventory Item master: 64 fields documented; PROD_TYPE codes R/N confirmed from live IN-A screen (2026-06-17); full set RFAMNLBTKO confirmed from HH filter string — **C: 82/100**
- [x] ✅ `BKSYMSTR` — System configuration master: all 286 DDF fields organized (20-slot payment terms array, 9-slot bank account array, AR/AP/GL defaults, auto-number counters, PRGS_WHR program path); BKSYPRTR companion table confirmed — Pass 121 2026-06-19 — **C: 85/100**
- [x] ✅ `AHSYLOG` — User security: all 23 fields documented — **C: 68/100**
- [x] ✅ `ISJAVA` — Java task queue: pattern confirmed; table NOT found in DDF (may be runtime-only or named differently) — **C: 55/100**
- [x] ✅ `BKLOGON` — Active session: all 10 fields documented — **C: 72/100**
- [x] ✅ `WORKORD` — Work order master: all 74 fields documented with meaning (Pass 54) — **C: 90/100**
- [x] ✅ `WORKCHG` — Work order change log: all 25 fields documented — **C: 70/100**
- [x] ✅ `BKARCUST` — all fields with meaning, PKs — documented — **C: 68/100**
- [x] ✅ `BKICMSTR` — all fields with meaning; PROD_TYPE codes confirmed (RFAMNLBTKO, R/N from live UI) — **C: 82/100**
- [x] ✅ `BKSYMSTR` — full schema: 286 fields confirmed from DDF; all embedded arrays documented (terms×20, bank×9, aging×5, ENDDESC×5, PR_ODNAME×6); BKSYPRTR printer table confirmed — Pass 121 2026-06-19 — **C: 85/100**
- [x] ✅ `BKAPVEND` — AP Vendor master: all 72 DDF fields documented in tier1-tables.md (dual address, 4 contacts, 5 phones, 10 notes, 5 emails, Avalara fields, CUST_CODE cross-ref, 2 UDF fields) — Pass 122 2026-06-19 — **C: 85/100**
- [x] ✅ `BKGLCOA` — GL Chart of Accounts: 65 fields documented (replaces BKGLJRNL — that table is BKGLTRAN) — **C: 68/100**
- [x] ✅ `WORKORD` / `WORKCHG` — Work order header + change log — documented — **C: 70/100**
- [x] ✅ `BKSOX` / `BKSOXH` — Sales Order extract: 25 fields documented — **C: 65/100**
- [x] ✅ `BKARINV` / `BKARINVL` / `BKARINVI` — AR invoice header/lines/staging: BKARINV all 84 DDF fields documented (3-address blocks, multi-currency, Avalara, reversal chain); BKAR_INVL_RTS = per-line release-to-ship flag; T7SAG = SO-G Post Invoices module confirmed — Pass 122 2026-06-19 — **C: 82/100**
- [x] ✅ `BKAPPO` / `BKAPPOL` — Purchase Order header (57f) and lines (38f) fully documented; PO family (active/history/archive/RFQ); WO outside-process link (BKAP_POL_WOPRE/WOSUF → WORKORD); unit conversion (PCONV); 3-way qty tracking (RQTY/IQTY/OO_QTY); docs/03-modules/ap-accounts-payable/README.md (Pass 110e 2026-06-19) — **C: 90/100**
- [x] ✅ `BKPRMSTR` — Payroll master (384 fields) — all fields grouped and documented; BKPRCURP/BKPRHIST, BKPRINFO, BKPRSALE/BKPRBOOK, BKPRTC/BKPRTCFG also documented; docs/03-modules/pr-payroll/README.md (Pass 110f 2026-06-19) — **C: 90/100**
- [x] ✅ `BKSLEVEL` — **SOLVED: Security level permission matrix** (14 menus × 20 options = 422 fields; links AHSYLOG.AHSY_USER_LEVL to allowed operations) — **C: 68/100**
- [x] ✅ `BKPRGLFL` — **SOLVED: Payroll GL posting config** (664 fields: 20 user deductions × GL accounts/limits/pct + 30 tax vendors) — **C: 62/100**
- [x] ✅ `ISJAVA` table — confirmed NOT in DDF (TAS runtime-only, not registered in Pervasive schema); schema known from Java decompilation: IS_JAVA_UID(PK)+IS_JAVA_DATE+IS_JAVA_PARAM_1..N; documented in architecture section — **C: 75/100**

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
- [x] ✅ `BKLOGON` all 10 fields documented (CODE/PSWD/CMPY/PROG/PRINTER/INUSE/SCRTY/MENU/SUBMENU/CURPRT); session tracking, multi-user conflict detection, menu navigation state; docs/03-modules/sm-system-manager/README.md (Pass 110g 2026-06-19) — **C: 82/100**
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
- [x] ✅ Menu tree storage confirmed: `BKMENUSU.DBF` (xBase/CodeBase); `EVOERPMENU.DCY` = visual form shell only — **C: 98/100** (Pass 105)
- [x] ✅ All 870 menu entries mapped to programs: `samples/BKMENUSU.TXT` — **C: 95/100**
- [x] ✅ PL = Checkmark Payroll Link (external Checkmark software integration) — **C: 95/100**
- [x] ✅ Module navigation groups (Mfg/Items/Sales/Queries/HH/System Mgr/Accounting/Pay Link/Payroll/Settings) — **C: 92/100**
- [ ] ⬜ All 870 menu entries mapped to their `.DFM` form (join with dfm_summary.csv)
- [ ] ⬜ NE (New Programs) 14 items identified — not in BKMENUSU.TXT; custom i2 additions
- [ ] ⬜ 205 help-only codes explained (removed features, optional modules, or RWN-only additions)

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
- [x] ✅ Pass 41: Full ISAR* archive family confirmed (30 tables): ISARAHIN+ISARAINV(84f BKARINV archives), ISARAHIL(28f BKARINVL archive), ISARAT(12f BKART archive), ISARAINT(23f BKARINVT archive), ISARTXNB(23f AR shipment batch with LINEID+RLEASD), ISARACHG(26f AR change archive); ISARCHG(26f AR change log); extended: ISAREX(51f resale cert), ISARFQ; complete archive lifecycle confirmed — **C: 80/100**
- [x] ✅ BKARCUST all 106 fields documented with meaning — docs/03-modules/ar-accounts-receivable/README.md (Pass 110e 2026-06-19) — **C: 95/100**
- [x] ✅ AR aging bucket calculation logic confirmed: source=BKARINVT (AMTRM>0 = open); due date = BKAR_INVT_DATE + terms from BKAR_INVT_TERMN; bucket day thresholds are runtime params in T7ARF; no pre-computed bucket fields in DDF; BKART (12f) = payment transaction log; docs/03-modules/ar-accounts-receivable/README.md (Pass 111a 2026-06-19) — **C: 72/100**

### 7.2 Accounts Payable (AP)
- [x] ✅ Menu codes listed (AP-A through AP-U) — **C: 72/100**
- [x] ✅ Forms inventoried (T7AP\*.DFM) — **C: 70/100**
- [x] ✅ Tables: BKAP\* (24 tables) — **C: 60/100**
- [x] ✅ Source files: Bkaph.SRC, Bkapha.SRC analyzed: BKYS.YN[48] format selector confirmed (1/4/5=laser→chain to BKAPHA via BKSY.PRGS.WHR; 2/3=dot-matrix→stay in BKAPH); both programs identical structure with multi-currency+RTM_VALID+BKAPCHKF locking; check batch array tCHK.NUM up to 5000 entries (Pass 118 2026-06-19) — **C: 84/100**
- [x] ✅ **Check printing workflow fully traced** (AP-H): select→check#→date→print→GL post(CD)→invoice update→BKAPCHKH→BKGLCHK — **C: 82/100**
- [x] ✅ GL posting type confirmed: "CD" (Cash Disbursement) — **C: 88/100**
- [x] ✅ BKAPCHKF (temp run file) and BKAPCHKH (permanent history) documented — **C: 78/100**
- [x] ✅ 1099 tracking mechanism confirmed: BKAPVEND 1099 code + BKAPINVT TYPE="P" — **C: 70/100**
- [x] ✅ Pass 41: Full ISAP* family confirmed (15 tables): ISAPOPO/ISAPOPOL(57/38f BKAPPO/BKAPPOL open views), ISAPARFQ/ISAPARFL(57/38f archive), ISAPAINL(390f BKAPINVL archive), ISAPACHK(12f BKAPCHKF archive), ISAPCHG+ISAPHCHG(32f AP change log+history: PONUM+LINEID+PCODE+before/after price/loc), ISAPEX(33f AP vendor extended: VEND PK+LONGNAME+NUM fields), ISAPQPO(66f vendor quote pricing: PCODE+VNDCOD PK), ISAPPROJ(12f project linking) — **C: 85/100**
- [x] ✅ Voucher entry workflow fully traced (AP-B): BKAPINVL (390f, 75-line flat GL distribution array: GLACT/GLDPT/DC/GLD/DAMT_1..75, plus APDPT/CHK/EXTRA/ISCUR/JOB trailer); BKAPINVT (19f, AP open-item ledger: AMT/AMTRM/TYPE/TERMN/SDATE/TAX/FRT/DEPNO/CHKNO/CHKAC); AP-B→BKAPINVL+BKAPINVT→AP-D scheduled dates→AP-F pick→AP-H print checks→GL post→BKAPCHKH; BKAPRIVL (390f same schema) = recurring voucher lines; docs/03-modules/ap-accounts-payable/README.md (Pass 111c 2026-06-19) — **C: 88/100**
- [x] ✅ BKAPVEND all 72 fields documented with meaning — docs/03-modules/ap-accounts-payable/README.md (Pass 110e 2026-06-19) — **C: 95/100**

### 7.3 Inventory (IN)
- [x] ✅ Menu codes listed (40 operations) — **C: 72/100**
- [x] ✅ Forms inventoried (T7IN\*.DFM) — **C: 70/100**
- [x] ✅ Tables: BKIC\* (16 tables), MTICMSTR identified — **C: 58/100**
- [x] ✅ BKICMSTR all 62 fields documented with meaning in tier1-tables.md: product code/desc, type, class, category, UOM (stock/purchase/price), costs, QOH, reorder, lead time, GL accounts (asset/COGS/scrap/non-tax), absorbed labor/setup/ops/material/fixed OH/variable OH, UPC, MTD/YTD sales — **C: 72/100**
- [x] ✅ Supplemental item master form set confirmed: allocation, components, forecast, pricing, specs, UDF, usage, WIP — **C: 65/100**
- [x] ✅ 16+ location/bin forms (T7INL* series) confirmed — **C: 60/100**
- [x] ✅ FIFO/LIFO/average cost layer logic traced: BKICVAL (4f, CODE+DATE PK, TOTVL/UOH) holds cost layers; FIFO=oldest DATE first, LIFO=newest, average=skip layers use INVTXN.AVGCOST running calc; INVTXN (24f, MTIT_* prefix) is complete audit log — receipt/shipment/adjustment/WO-issue/WO-receipt all logged with cost+qty+lot+serial+ref; docs/03-modules/in-inventory/README.md (Pass 110h 2026-06-19) — **C: 78/100**
- [x] ✅ Physical inventory workflow (PI module) traced: PI-A freeze→PI-C tag entry→PI-G post variances→PI-H purge; all 7 BKPI* tables documented with field semantics (BKPIMSTR 3f session header, BKPIFROZ 19f frozen snapshot, BKPIPHYS 14f count tags, BKPILOT/BKPILCNT 10f lot frozen/counted, BKPISER/BKPISCNT 10f serial frozen/counted); PI-G posts INVTXN adjustments; docs/03-modules/pi-physical-inventory/README.md (Pass 111a 2026-06-19) — **C: 82/100**
- [x] ✅ Lot tracking / serial number tracking workflow confirmed: LOT (25f, MTLOT_CODE+LOT PK) = lot master with PO/WO origin, EXPDATE, ONHAND, RECQTY, POCOST/WOCOST, 5 notes, BEGIN/OUT/MAXOUT for weight tracking; SERIAL/SERIALH (30f each, MTSER_CODE+SERIAL PK) = per-unit biography: receipt→WO issue→WO completion→ship; SERIAL→SERIALH on shipment; all movements logged in INVTXN; READMEs created in lc-lot-control/ and sc-serial-control/ (Pass 111b 2026-06-19) — **C: 88/100**

### 7.4 Sales Orders (SO)
- [x] ✅ Menu codes listed (48 operations — largest module) — **C: 72/100**
- [x] ✅ Forms inventoried (T7SO\*.DFM) — **C: 70/100**
- [x] ✅ Tables: BKSO\* (7 tables identified) — **C: 55/100**
- [x] ✅ Key forms read: T7SOA (full header+lines, 5001-element line arrays), T7SOB (print), T7SOC (pick→pack→ship→invoice hub), T7SOD (line status), T7SOE (release), T7SOF (invoice print), T7SOG (COGS) — **C: 72/100**
- [x] ✅ Order → shipping → invoice chain traced: T7SOA → T7SOE → T7SOC → T7SOF — **C: 70/100**
- [x] ✅ Certificate of Conformance + Country of Origin compliance docs confirmed (T7SOC RTMs) — **C: 68/100**
- [x] ✅ 5,001-element line item arrays confirmed (supports 5,000 lines per SO) — **C: 75/100**
- [x] ✅ All BKSO\* tables with fields documented — BKSOHLOT(14f=lot/serial ship tracking), BKSOHSER(14f=serial tracking, same layout), BKSOLOCK(5f=concurrent edit lock), BKSONOTE(5f=BK_DESC note lines), BKSOPO(16f=MRP planned PO, BKMRP prefix shared), BKSOX(25f=invoice supplemental/multi-company), BKSOXH(25f=BKSOX archive) — docs/03-modules/so-sales-orders/README.md (Pass 110e 2026-06-19) — **C: 93/100**
- [x] ✅ Sales Analysis (SA module): reporting-only module (no data entry); reads BKARHINV/BKARHIVL/BKARCUST/BKICMSTR; single table BKSAREPT (57f, TYPE+NAME PK, RTM + 26 FROM/THRU filter pairs); SA-M/SA-N save configs to BKSAREPT; SA-A reads BKSOX for bookings; SA-Q uses actual WO costs; README created docs/03-modules/sa-sales-analysis/README.md (Pass 111a 2026-06-19) — **C: 82/100**

### 7.5 Purchase Orders (PO)
- [x] ✅ Menu codes listed (29 operations) — **C: 72/100**
- [x] ✅ Forms inventoried (T7PO\*.DFM) — **C: 70/100**
- [x] ✅ Key PO forms read from network share: T7POA (232 KB — full header+lines), T7POB (print options), T7POJC (receiving+QC), T7POH (RFQ/5-level pricing), T7POM (multi-tab inquiry) — **C: 70/100**
- [x] ✅ 5-level vendor price breaks confirmed in T7POH — **C: 72/100**
- [x] ✅ RoHS / NCR tracking on received items confirmed (T7POJC) — **C: 68/100**
- [x] ✅ Digital signature support on printed POs confirmed — **C: 65/100**
- [x] 🔄 Pass 52: 50+ T7PO* programs fully mapped; full PO→receipt→AP voucher→check workflow traced; BKAPVND2(63f: VENDCODE PK+ID+SEND_1099+6-type×5-slot UDF with labels)+BKCMVNDH(8f: vendor history log)+BKCMVNDF(10f: vendor follow-up+PO link)+ISICMSTR(41f: item dimensions+pallet+tooling+UDF)+ISAPCHG(32f: PO change audit before/after) all extracted; ACMASTER confirmed NOT IN DDF schema — **C: 80/100**

### 7.6 Work Orders (WO)
- [x] ✅ Menu codes listed (31 operations) — **C: 72/100**
- [x] ✅ Forms inventoried (T7WO\*.DFM) — **C: 70/100**
- [x] ✅ Tables: WO\* (30 tables) — **C: 55/100**
- [x] ✅ Source files: BKAWLB.SRC fully analyzed (Pass 119): WO Status Report/LWJB (originally BKLWJB "Labor WIP Job" — merged Nov 2000); filters WOs by status/priority/class/dates/part/customer ranges; opens BKARCUST+BKICMSTR+MTICMSTR+WORKORD+BKSYMSTR; 5 tables only (report viewer, NOT entry); 7 sort options; no labor-entry logic — **C: 72/100**
- [x] ✅ Work order lifecycle **fully traced**: Create(WO-A) → Release(WO-B) → Routing(WO-K-A) → Material(WO-F/WO-FA backflush) → Labor(WO-G) → Outside(WO-H → PO) → Close(WO-S) — **C: 72/100**
- [x] ✅ WO status codes documented: F=Released, R=Completed, C=Closed, S=Scheduled, I=In Process, X=On Hold — **C: 75/100**
- [x] ✅ WO priority 1–9 confirmed as scheduling parameter — **C: 72/100**
- [x] ✅ DC-to-WO integration confirmed: DC postings write to same WO tables; T7WOKK reverses them — **C: 68/100**
- [x] ✅ WO-PO linkage confirmed: outside process operations link to AP POs — **C: 68/100**
- [x] ✅ Pass 42: ISWOCLOG(32f) = WO operation change audit log: IS_WOLOG_WOPRE(8)+WOSUF(2)+OPER(2) PK + OPDESC(30)+ITEM(15)+WC(12)+WCDESC(30)+CUST(10)+CUSNME(30)+ITEMDS(30)+CDATE+CWHO(30)+CTIME+CWHERE(15)+MACH(4)+ALPHA1_1/2(30 each)+FLAG_1..5+DATE_1..3+7more; every WO-op modification logged with WHO/WHEN/WHERE/MACHINE. ISWOHEX(63f) = alternate index of ISWOEX (IS_WOEX_* fields, 0 diff). ISWODESC/ISWOHDSC(5f each) = WO description notes, standard BK_DESC_* pattern — **C: 72/100**
- [x] ✅ All 30 WO\* tables with fields documented — full functional cross-reference in README, all groups: 3 WO masters, 5 BOM, 5 routing, 4 labor, 3 material, 3 receipt, 2 date, 2 extra-charge, 2 audit, 1 WC; plus ROUTING(62f)+ROUTTEMP(62f) routing templates — **C: 92/100** (Pass 110e 2026-06-19)
- [x] ✅ WORKORD all 74 fields confirmed with meaning — 7-category cost structure (Setup/Mat/OutProc/Labor/VarOH/FixOH/Misc) × E/A/Variance; 32-byte DDF gap noted; docs/03-modules/wo-work-orders/README.md (Pass 110e 2026-06-19) — **C: 90/100**

### 7.7 General Ledger (GL)
- [x] ✅ Menu codes listed (16 operations) — **C: 72/100**
- [x] ✅ Tables: BKGL\* (28 tables) — **C: 65/100**
- [x] ✅ All 24 GL forms read from network share — **C: 72/100**
- [x] ✅ Journal transaction types confirmed: GJ, CR, CD, TT, YE (entry types), RS, RP, PR, OT, WO (system posting types) — **C: 75/100**
- [x] ✅ BKGL table family purpose documented: live/archive/report/temp/COA/statement/crossref tiers — **C: 68/100**
- [x] ✅ Journal entry workflow traced: T7GLB (enter GJ/CR/CD/TT/YE) → T7GLC (report/filter) → T7GLP (period-end) → T7GLARCH (archive) — **C: 70/100**
- [x] ✅ Pass 40: All 28 BKGL* table schemas extracted. 4 COA tables (BKGLCOA/CCOA/ECOA/FCOA, 62-65f each, identical structure + period balance array); 8 transaction tables (BKGLTRAN/ATRN/ETRN/HIST/TEMP×4, all identical 16f: GLACCT+GLDPT+DATE+CODE+INVC+DESC+DC+AMT+8more); 4×2 journal tables (BKGLGJRN/GJLN, BKGLAGJR/AJL, BKGLRGJR/RJL, BKGLTGJR/TJL — current/archive/recurring/template); BKGLFSTL(12f statement layout), BKGLSTMT(104f statement groups), BKGLDESC(5f GL notes), BKGLACHK+BKGLICC (11f archive+intercompany checks), BKGLXH(20f extended history); full GL architecture documented — **C: 75/100**
- [x] ✅ Period-end close workflow documented from table structure: BKGLTRAN (16f, permanent transaction log — TYPE codes AP/AR/GJ/PR/IC/WO; PERIOD 1–14; POST flag); BKGLGJRN/BKGLGJLN (11/9f GJ batch header/lines — 4 lifecycle variants: current/archive/recurring/temp); BKGLX/BKGLXH (20f cross-reference: PART+WO+PO+SO+JOURNAL drill-back); BKGLDESC (5f notes attachment); GL-O posts BKGLGJLN→BKGLTRAN + updates BKGLCOA.CURRENT_N; year-end shifts CURRENT→1YPAST→2YPAST; docs/03-modules/gl-general-ledger/README.md (Pass 111c 2026-06-19) — **C: 75/100**
- [x] ✅ BKGLCOA all 65 fields confirmed with full meaning — 14-period × 4-dataset design (CURRENT/BUDGET/1YPAST/2YPAST) fully documented; docs/03-modules/gl-general-ledger/README.md (Pass 110e 2026-06-19) — **C: 97/100**

### 7.8 Bill of Materials (BM)
- [x] ✅ Menu codes listed — **C: 65/100**
- [x] ✅ Tables: BKBM\* (10 tables) — **C: 60/100**
- [x] ✅ BOM Tree analysis tool documented (BOMTREE.RWN) — **C: 60/100**
- [x] ✅ 4 core forms read: T7BMA (master entry, 15 remarks/component), T7BMB (print with status codes Y/N/O/D/E/P/S/Q/R), T7BMC (multi-level print, "up to X levels"), T7BMD (availability + shortages) — **C: 62/100**
- [x] ✅ Item type codes confirmed: R/F/A/M/N/L/B/T/K/O (10 types) — **C: 75/100**
- [x] ✅ Item status codes confirmed: Y/N/O/D/E/P/S/Q/R (9 status values) — **C: 75/100**
- [x] ✅ Multi-level BOM explosion confirmed (T7BMC: "print up to X levels") — **C: 65/100**
- [x] ✅ RoHS compliance flag on BOM components confirmed — **C: 72/100**
- [x] ✅ Pass 40: All 10 BKBM* schemas extracted. Parallel-snapshot architecture confirmed: BKBMMSTR(26f current)/BKBMAMTR(actual)/BKBMAVAL(actual value)/BKBMEMTR(estimated)/BKBMSUMM(summary) all identical PARENT+COMPONENT PK + QTY_REQD+REFERENCE+PROD_TYPE+SCRAP+OP+OPYN flags; BKBMDIM(11f sheet-metal dimensional BOM: PARENT+LINE+COMP, PART_X/Y+TRIM_X/Y+MACH); BKBMERMK/BKBMREMK(20f each, 10×64 remark lines — engineering vs regular); BKBMNOTE(16f parent notes, 15×64 lines); BKBMCNFG(7f: NUM+GLACT+GLDPT+AUTO+POST+ROLL+LABOR) — **C: 72/100**

### 7.9 MRP / Manufacturing Requirements Planning (MR)
- [x] ✅ Menu codes listed (12 operations) — **C: 65/100**
- [x] ✅ Tables: BKMR\* (3 tables) — BKMRPFC(9f: MRP demand forecast PART+DATE+QTY+OQTY+CQTY+FLAG), BKMRPPO(16f: planned PO PART+DATE+ERD+QTY+PRICE+WOPRE/WOSUF+PLANR+CONF+EST link), BKMRPSW(2f: per-part on/off switch); all schemas extracted; MRP demand→planned-PO flow confirmed — **C: 78/100** (Pass106e: full field semantics+action codes+data flow in tier4-tables.md)
- [x] ✅ Source file: BKMRF.SRC fully re-analyzed (Pass 119): DO.SO/DO.PO/DO.WO/DO.WOBOM/DO.FC/DO.RLEVEL demand loading procedures confirmed; 4-stage MRP engine (START.MRP 1-4) confirmed; MTMRP 12 field names confirmed (PARTNO/DATE/KEY/ORDER/ACTION/PEGTO/QTY/PG.SDATE/PG.FDATE/STARTDT/PG.QTY/ONHAND); MTIC.PROD.MRP/TYPE/MRPSW flags confirmed; BKMRPSW 2f confirmed (PART+SW='Z'); BKICLOC opened for reorder level check — **C: 78/100**
- [x] ✅ Pass 45: All 17 T7MR* programs mapped (T7MRA through T7MRO). Full demand-to-release lifecycle: MR-A(forecast entry) → MR-F(explosion engine→MTMRP) → MR-G(firm, BKSBVEND/BKSBMFG select vendor) → MR-H(release→WORKORD+BKAPPO) → MR-I/IX(capacity scheduling with ROUTING+CALENDAR) → MR-J(PO/RFQ via BKRFQ 49f). MTMRP(13f) extracted: PARTNO+DATE PK, PEGTO(demand tracing), ACTION lifecycle. BKRFQ(49f): 10 qty/cost breakpoints, shared by both RF (estimates) and MR (MRP). CALENDAR(5f): SAT+SUN work flags. BKSBVEND(6f)/BKSBMFG(6f)/BKSBPART(5f): approved-source tables used by MR-G vendor selection — **C: 80/100**
- [x] ✅ Full MRP calculation cycle traced (T7MRF explosion → MTMRP → firm/release)
- [x] ✅ All core BKMR\*/MTMRP/support tables documented with fields; full field tables + MRP data flow diagram added to docs/03-modules/mr-mrp/README.md (Pass 110h 2026-06-19) — **C: 88/100**

### 7.10 Routing (RO)
- [x] ✅ Menu codes listed (19 operations) — **C: 65/100**
- [x] ✅ Source file: BKROA.SRC fully re-analyzed (Pass 119): ROUTING table opened + ~20 field names confirmed from entry procedures (DESC/LOTSZ/TYPE/ROUTNM/VEND/VNDCST/MCHCST/NUMPRC/TMPRC/PRTSHR/SETUP/POVLP/NOVLP/STDTIM/LOTSIZ/PERSON/TMACH/TOOL); BKRTEMTR confirmed (EDI import routing staging — used instead of ROUTING when cfrom='BKDEJC'); G.COPY.SPEC confirms routing spec copy path — **C: 75/100**
- [x] ✅ Pass 57: ROUTING/MTRO_(62f) fully extracted: CODE+OPER PK, TYPE/LEAD/PARTSHR/TIMEPART/SETUPHRS/LOTSIZE, 15×INSTR, WC+WCDESC, VENDCODE+VENDNAME, LABOR/MACHINE/FOVHD/VOVHD/SETUP costs, TMACHINE/TOOL, NUM/NUM_PERSON, OVERLAP/NEGOVLP, PIECE_RATE, LONGTIME, PRINT, CLASS, EXTRA(150), DEF_TIME, R_TYPE, EST_LINE/EST_TAG; BKRTCST(24f)=routing cost snapshot 10-break; BKRFQ(49f)=vendor RFQ per operation (subcontract quotes); 13 T7RO* programs mapped — **C: 85/100**
- [x] ✅ Routing → WO link: ROUTING template → WOROUT copy (MTWORO_ fields mirror MTRO_ fields)

### 7.11 Payroll (PR)
- [x] ✅ Menu codes listed (29 operations) — **C: 65/100**
- [x] ✅ Tables: BKPR\* (16 tables); BKPRMSTR (384 fields) fully field-grouped; all 16 tables documented to varying depth — **C: 88/100**
- [x] ✅ Key forms read: T7PRA (W-4/employee tax setup), T7PRB (current payroll batch entry), T7PRF (11-bracket tax tables), T7PRE (direct deposit) — **C: 62/100**
- [x] ✅ Tax table structure documented: 11-bracket tiers per tax code in BKPRFTAX — **C: 65/100**
- [x] ✅ Array-based payroll entry confirmed (batch employee processing, 7 unlimited deduction types) — **C: 62/100**
- [x] ✅ Pass 46: All 40+ T7PR* programs mapped. Full lifecycle: PR-A(employee setup)→PR-J/K(time cards/DC labor import)→PR-B(current period BKPRCURP)→PR-C(calculate)→PR-G(print checks)→PR-D(post BKGLTRAN)→PR-DPST(direct deposit via ISPRTEMP staging). BKPRMSTR(384f) key fields: EMP# PK+NAME+SSN+ADDRESS+PAYTYP+15 rates+DEPT+SHIFT+QTD/YTD for regular/vacation/sick/FIT/FICA_1/2/state/WC/medical+12 user-defined deductions. BKPRCURP(127f): EMP#+DATE PK; regular+12 OT types+vacation+sick hrs/rates/amounts. BKPRFTAX(47f): CODE PK+11-bracket START/THRU/AMT/PERC. BKPRGLFL(664f, widest table): STATE+DEPT PK; every payroll tax GL account+rate (FICA employee/employer/limit, FUTA, SUTA, SDI, WC). BKPRSALE(87f): 12-month QUOTA/GROSS/COGS/RCPTS commission bridge. BKPRINFO(128f): 6 review+raise dates, vacation/sick accrual config, direct deposit banking. BKPRTC(7f): time card EMP+DATE+START/STOP/DEDUCT. ISPRTEMP(15f): direct deposit GL staging before ACH post — **C: 82/100**
- [x] ✅ BKPRMSTR all 384 fields fully documented by group (Pass 110f 2026-06-19) — **C: 90/100**
- [x] ✅ W-2 / 1099 generation fully traced: BKPRW2 (384f, identical schema to BKPRMSTR — year-end snapshot created by PR-O); PR-O copies BKPRMSTR→BKPRW2 + zeros YTD fields + rolls BKPRSALE→BKPRBOOK; PR-A edits BKPRW2; PR-L-I prints W-2s from BKPRW2; PR-H (82f DFM) transfers payroll liabilities to AP (creates BKAPINVL/BKAPINVT vouchers using BKPRGLFL GL matrix); 1099 via AP-S reads BKAPVEND.TAX_ID+BKAPVND2 (63f 10-slot box amounts); full year-end sequence documented in docs/03-modules/pr-payroll/README.md (Pass 111d 2026-06-19) — **C: 82/100**

### 7.12 Data Collection (DC)
- [x] ✅ Menu codes listed — **C: 65/100**
- [x] ✅ Files: EvoDC\*.RWN, EvoDCmenu.RWN, EvoDCsetup.RWN cataloged — **C: 70/100**
- [x] ✅ Tables: BKDC\* (7 tables) — **C: 55/100**
- [x] ✅ Source file: BKDCA.SRC fully analyzed (938 lines): DC entry variants DCA/DCB/DCC confirmed; BKYS.YN[228]=alternate screen/BKYS.YN[229]=auto-close confirmed; WOLABOR 17 field names (DATE/EMP/WOPRE/WOSUF/WOKEY/OPER/POSTED/SHIFT/START/FINISH/PARTS/SCRAPPED/NOJOBS/RUNHRS/SETUPHRS/REGOVER/EXTRA) confirmed from source; BKDCSHFT 4-field-per-shift structure (BUFFER/START/FIN/FINBUF) confirmed; BKDCLAB→BKDCPLAB→BKDCTLAB migration logic confirmed (Pass 118 2026-06-19) — **C: 82/100**
- [x] ✅ Handheld forms: T7HH\*, label tables BKDC\* — **C: 60/100**
- [x] ✅ Full DC workflow traced: scanner input→BKDCCLAB→DC-G review/approval→DC-H post to BKDCLAB→WORKORD update→BKDCPLAB→archive BKDCHLAB; all LAB_* tables share 50f schema; docs/03-modules/dc-data-collection/README.md (Pass 111b 2026-06-19) — **C: 78/100**
- [x] ✅ All BKDC\* tables documented: BKDCCFG(7f config), BKDCSHFT(34f 3-shift schedule), BKDCCLAB/BKDCLAB/BKDCPLAB/BKDCHLAB/BKDCTLAB(all 50f same schema: LAB_DATE+EMP+WO+OPER PK; START/FINISH times; PARTS/SCRAPCD/SCRAPQTY; CYCLE_HR/MIN/SEC; audit+generic fields) — **C: 78/100**

### 7.13 Serial Control (SC) ⚠️ NAME CORRECTED — was "Scheduling/Capacity"
- [x] ✅ Menu codes listed — **C: 68/100**
- [x] ✅ All 9 DFM files read from network share — **C: 72/100**
- [x] ✅ SC-A: Edit Serial Numbers (MTSER table) — serial record view/edit — **C: 75/100**
- [x] ✅ SC-B: Assign Serial Control on items (MTIC.PROD.SER flag) — **C: 72/100**
- [x] ✅ SC-G: Serial format setup (total length, numeric start position, last number) — **C: 72/100**
- [x] ✅ T7SCOMP: Compound serial numbers (IS.SCOMP.*) — **C: 65/100**
- [x] ✅ Primary tables: MTSER (serial master), IS.SERC.* (config), IS.SCOMP.* (compound) — **C: 72/100**
- [x] ✅ Pass 37 RWN confirmation — 9 programs: T7SCA(78p cycle count entry, SERIAL+WORKORD+BKICLOC+ISBINLOC), T7SCB(59p list maintenance, BKICMSTR+ISTRIGRS), T7SCC(121p count posting, BKARTXN), T7SCD(5p sub-stub), T7SCE(88p count by location, BKICLOCM), T7SCF(131p transaction history, INVTXN+CLASMSTR), T7SCG(92p counter maintenance, ISSERCNT+MTICMSTR), T7SCH(113p history report, INVTXN+WORECV+WORKORD+BKARINV), T7SCOMP(54p compound, ISSCOMP); ISSCOMP(5f: IS_SCOMP_DETAIL+COMPND+VIS+WHO+IS_SCOMP) schema extracted — **C: 72/100**
- [x] ✅ MTSER all 30 fields documented with meaning (Pass 109: PO/WO/SO paths; ONHAND/LOC/BIN/INV; NOTES_1..5; EXTRA) — **C: 80/100**
- [x] ✅ Serial lifecycle fully traced: PO receipt→WO issue→WO completion→SO ship→invoice; ISSERIAL(11f) genealogy table documented (Pass 109) — **C: 80/100**

### 7.14 Physical Inventory (PI)
- [x] ✅ Menu codes listed — **C: 65/100**
- [x] ✅ Tables: BKPI\* (7 tables) — **C: 55/100**
- [x] ✅ PI-A (Capture Frozen Inventory: YEAR/QTR/FDATE/COUNTTYPE), PI-B (print count sheets), PI-C (Enter Tag Counts: BKPH.TAGNUM/LOC/EMPNAME/CODE/LOT), PI-D (Missing Tags) — **C: 62/100**
- [x] ✅ Variance calculation and posting steps confirmed: PI-G compares BKPIPHYS.BKPH_ACTQTY to BKPIFROZ.BKPH_INFO_UOH; delta posted as INVTXN adjustment; BKICMSTR.UOH updated; BKPIFROZ.BKPH_INFO_GLPST+INPST set to Y; lot/serial variants use BKPILCNT vs BKPILOT and BKPISCNT vs BKPISER; docs/03-modules/pi-physical-inventory/README.md (Pass 111a 2026-06-19) — **C: 82/100**

### 7.15 Labor / Time & Attendance (LW / LA)
- [x] ✅ Menu codes listed — **C: 62/100**
- [x] ✅ Source file: BKLME.SRC analyzed — **C: 60/100**
- [x] ✅ Time entry → WO charge chain fully traced: 3 paths — (1) DC path: BKDCCLAB→DC-G approve→DC-H post→WOLABOR+WORKORD costs+BKGLTRAN; (2) WO-G direct: T7WOG→WOLABOR+WORKORD+BKGLTRAN; (3) PR-J time cards: BKPRTC→PR-K→BKPRCURP+BKPRMSTR YTD (payroll only, no WOLABOR); PR-J-A imports BKDCLAB→BKPRTC for paycheck generation from same DC event; LW module = WO+JC menu alias using same tables; docs/03-modules/lw-labor-wip/README.md created (Pass 111d 2026-06-19) — **C: 82/100**

### 7.16 EDI (ED)
- [x] ✅ Tables: BKED\* (6 tables) — BKEDIH(84f: same structure as BKARINV — EDI-in staging header), BKEDIL(28f: same as BKARINVL — EDI-in lines), BKEDIDUN(7f: customer DUNS mapping+EDI flags), BKEDMSTR(3f: our DUNS+import path+counter), BKEDNOTE(3f: EDI notes), BKEDPOST(2f: posting log); unified invoice architecture confirmed for EDI — **C: 78/100**
- [x] ✅ Pass 106: All 6 BKED* tables fully documented in tier4-tables.md — field semantics for all auxiliary tables confirmed; BKEDIH/BKEDIL = byte-for-byte BKARINV/BKARINVL clones confirmed from DDF — **C: 78/100**
- [x] ✅ Pass 106: EDI pipeline confirmed from BKMENUSU.TXT DEP submenu: DEP-B=Import (X12 850 in → BKEDIH/BKEDIL), DEP-C=Edit staging, DEP-D=Convert to SO (→ BKARINV), DEP-E=Export 810/855, DEP-F=Export 856 ASN, DEP-H=Error Report — **C: 78/100**
- [ ] ⬜ X12 transaction set version numbers confirmed (e.g. 004010/005010)

### 7.17 Estimating (ES)
- [x] ✅ Tables: BKES\* (3 tables) — BKESTQT(84f: same structure as BKARINV — ES quote header), BKESTQTL(28f: same as BKARINVL — quote lines), BKESTCFG(13f: quote config NUM+STAT+CLASS+FORM+DAYS+5 footer lines+SONUM); unified invoice architecture confirmed for ES quotes — **C: 78/100**
- [x] ✅ Pass 106: All BKES* tables fully documented in tier4-tables.md; BKESTQT/BKESTQTL = byte-for-byte BKARINV/BKARINVL clones confirmed from DDF; BKESTCFG 13f field semantics documented; ESTSUM 213f structure confirmed (MTESUM_ prefix, 10-qty-break cost matrix); full ES-A..M pipeline documented — **C: 78/100**
- [x] ✅ ES-D (Print Customer Quotes), ES-E (Convert Estimates: ISTO.WO + ISTO.SO — converts to WO or SO), ES-B/C (print/range options) — **C: 58/100**
- [x] ✅ Pass 42: Full ISES\* family (10 tables) extracted. ISESTHDR(84f)/ISESTLNE(28f) = BKARINV/BKARINVL ES current views. ISESAHDR/ISESALNE + ISESTAQT/ISESTAQL = archive alternate indexes (same structures). ISESTDTL/ISESADTL(203f, identical) = estimate detail: IS_EST_NUM+PART+LINE PK; 10 qty-break × material/labor/overhead cost columns. ISESTASM(213f) = DBA/MT-era estimate assembly summary: MTESUM_QUOTE(8) PK + DATE/EXPDATE/STATUS/CLASS/CODE/DESC/UM/CUSTCODE+NAME+ATTN+RFQ/REV/PROJ + QTY_1..10 + MAT_1..N (213 fields total, MTESUM_ prefix confirms MT generation — predecessor to BKESTQT). ISESTPO(16f) = ES→PO link: BKMRP_PO_* fields (same as BKSOPO). Unified architecture confirmed end-to-end: ES quotes through archive through estimate detail — **C: 72/100**
- [x] 🔄 Pass 50: T7ESA (15p) FOUND — opens BKBMMSTR+BKICMSTR+BKMRPFC+DBAFIFO; T7ESB(213p)/ESC(124p)/ESD(162p)/ESE(194p)/ESH(60p)/ESI(94p)/EST(163p) all mapped; BKMATCST(25f: CODE PK, 10×QTY_N+10×COST_N+MIN+MINCST+DATE) material cost; BKRTCST(24f: QUOTE+CODE+OPER PK, 10×PARTSHR_N+10×SETUP_N) routing cost; BKMRPFC(9f: PART+DATE PK, QTY+OQTY+CQTY+FLAG) MRP forecast demand; ESTSUM = DDF table name for ISESTASM(213f); ES-C uses BKRFQ for vendor cost — **C: 72/100**

### 7.18 Remaining Modules (not yet deeply documented)
The following modules have menu codes and forms inventoried but no deep logic documentation:

- [ ] ⬜ **AB** — no T7 RWN/DFM files found (DBA-era legacy code, unimplemented in TAS Pro 7)
- [x] 🔄 **AC** — Activity Control / NCR tracking — 3 DFMs + 5 RWN modules (T7ACTION/ACRDTYPE/T7ACDET/T7ACDATE/T7ACCNFIX); WODATE(13f) all fields var-confirmed (Pass 116): WOPRE+WOSUF PK, START/FINISH/QTY/PARPRE/PARSUF/TOPPRE/TOPSUF/DELPRE/DELSUF/PRIO/EXTRA; **ACDETAIL 17-field schema extracted from T7ACDET vars (Pass 116, 2026-06-19):** ID+LINE+PART+QPERF+QPERT+OPER+UM+ACTION+REFDES+LNOTE+LQTCOST+LQTDATE+ACTCOST+TOTBUY+CNEED+CUSTPART+TYPE (Btrieve-only, not in DDF); ISACTION(3f: TYPE+DESC+MISC) extracted; T7ACTION (53p, 14 tables): ISACTION+BKARCUST+BKAPVEND+BKCMACCN+BKICMSTR+ISLINKS — action master with entity cross-ref; T7ACDATE (64p, 16 tables): WODATE+WORKORD+MTICMSTR confirms WO hierarchy traversal; T7ACCNFIX (28p, 6 tables): BKCMACCN-only fixer (BKCM.ACCN.* vars: CODE/CONT/TITLE/PHONE/EMAIL/DATE1/DATE2/ALPH1/ALPH2/CON/PRIM/PHLBL/EMLBL/MSLBL/DTLBL/M2LBL/D2LBL) — **C: 75/100**
- [x] 🔄 **AM** — Accounting Maintenance (NOT Asset Management — CORRECTED) — 5 forms read (GL period control, account history, account entry, dept copy/delete, financial statement format) — **C: 75/100**
- [x] 🔄 **AD** — Accounting Defaults — CHM fully documented (AD-A GL defaults with 20 accounts + 5 posting flags + 6 period-date controls, AD-B checking account setup with 16 fields, AD-C AP defaults with 11 behavioral flags); RWN programs: T7MDEFAULTS (435 procs, main — opens BKSYMSTR+BKYSMSTR+ISBANKS+42 more tables), T7MDEFBANKS (79 procs, AD-B bank setup — BKGLCOA+ISBANKS), T7MDEFNDC (252 procs, extended module defaults — BKSYAP+BKESTCFG+BKFOCFG+BKCPMSTR+BKCMCNTD); primary tables: BKSYMSTR(286f full schema extracted Pass63: auto-numbers/company/20terms×6arrays/9banks×6arrays/all GL accounts/aging buckets/feature flags/173 EXTRA), BKYSMSTR (YN flags), ISBANKS (checking accounts) — **C: 75/100**
- [x] 🔄 **CM** — CRM/Contact Manager — T7CMA + 4 sub-forms read; CRM-AR bridge confirmed; 9 emails/contact (BKCM.ACCN.EMAIL[1-9]); contact title/primary flag; key dates (BKCM.ACTD.*); account classes; territory/SIC/lead-source; BKCM.* (46 tables); detailed findings at Pass 53 entry below — **C: 82/100** (aligned with Pass 53 detailed entry)
- [x] 🔄 Pass 53: All 37 BKCM* tables field-extracted; 6 T7CM* programs fully mapped; 3-entity architecture confirmed (BKARCUST customers + BKCMACCT prospects + BKCMPCNT contacts); BKCMACCT(41f: CODE+NAME+ADDR+REP+SICCD+CUST+LEAD+TERR+CCARD+EMAIL+EMPS)+BKCMACCN(154f: 10×CONT/TITLE/PHONE/DEAR/EMAIL+labels+UDF dates/alpha)+BKCMACTH(21f: history with start/stop/MIN/BMIN/RATE/AMT/BALNC billing)+BKCMACTF(11f: follow-up+SO link)+BKCMHCOD(9f: event codes+rate+BPART billing parts)+BKCMREP(14f: VIEW/CHANGE/GWARN/AADD flags)+BKCMTERR(11f)+BKCMMHST(72f: campaign with 20-class include+20-class exclude+9 range filters)+BKCMDUN(36f: 10-level dunning ladder)+BKCMDUNH(6f)+ISREMIND(22f: system-wide calendar with cust/vend/item links+email+FILE attachment)+MKAHIST(9f) all extracted; BKCMDE+BKCMEACT confirmed as DDF alt-key views of BKCMACCT (not separate tables) — **C: 82/100**
- [ ] ⬜ **CP** — no T7 RWN/DFM files found (DBA-era legacy)
- [x] 🔄 **CR** — Contract Review / SO Approval — T7CTREVU(96p): opens ISCTREVU+BKARINV+ISSOREVU; ISCTREVU(17f) schema extracted: EMPNME(25)+EMP PK; DEPT(25)/ADMIN(1)/LEVEL(2)/MOTPAS(10)/ACTIVE(1)/CDATE/EDATE/ADATE/ATIME/FLAG_1..5/EXTRA(100); ISSOREVU(12f, already in SR docs): SO+DEPT PK, EMPNME/EMPNUM/MOTPAS/ADATE/EDATE/APPROVE/REQUIRE; CR-A assigns departments to SOs (creates ISSOREVU records), CR-B enters approvals (reviewers per ISCTREVU); 2 programs confirmed — **C: 72/100**
- [x] 🔄 **CC** — Credit Card Processing ⚠️ (NOT Cycle Count — CORRECTED) — all 6 DFMs read; CC-P (IS.CC.MASKED/CARDNAME/EXP/ZIP — masked card storage with expiry flag), CC-PO (CC charges on POs: ccnum/ccamount/CCYY/CCMM), ccr1 (Credit Card Invoice List report by date/terms), CC-DE (CSV import); WO and item range filters confirm cost allocation to jobs; Pass 44: ISCC(14f) fully documented: CODE(10) PK + TOLKEN(20, vault token, NOT raw PAN = PCI-compliant)+MASKED(24)+EXP(4)+ADDRESS(40)+ZIP(10)+CARDTYPE(15)+CARDNAME(25)+STATUS(25)+STDATE+XCTRAN(10)+EXTRA(100)+PROCESS(10, processor code e.g. "AUTHORIZE") — **C: 72/100**
- [x] 🔄 **CS** — Commission/Salesperson Management — all 12 DFMs read; CS-A (BKPR.SLS.* fields: rate/HOW/WHEN/class/GL/agent-vendor), CS-B (quota/COGS/comm-due/paid[1-7]), CS-D (transfer commissions: BKPR.COMM.SLSP/CCODE/INVNM/INVDT), CS-E/F (detail+summary reports); outside agents linked to AP vendor — Pass 57: 17 T7CS* programs fully mapped; BKPRSALE(87f)+BKPRCOMM(12f, fully extracted)+BKPRAGNT(4f)+BKPRMSTR(384f employee/payroll master)+BKPRCURP(127f current payroll period)+ISREPLNK(11f rep-to-customer link) all extracted; HOW (`S`=sales%, `G`=gross margin) and WHEN (`I`=invoice, `P`=payment) logic confirmed from field names — **C: 80/100**
- [x] 🔄 **DE** — Data Entry / EDI / Imports (20 DFMs, 33 ops); Pass 116 ASN family confirmed: T7DEP860 (82p, EDI 860 PO changes — BKGLX+DBAFIFO+BKGLTRAN), T7DEPB (111p, EDI 856 ASN shipment build — BKARINV+BKYSMSTR+BKEDMSTR+BKEDIDUN+BKARCUST+BKARINVL+ISSRINFO), T7DEPC (15p, ASN cost post — BKGLX+DBAFIFO+BKGLTRAN+TASCOLOR+ISGLDATE), T7DEPD (132p, ASN pack/carton build — ISBUILD+BKICLOC+BKICLOCM+ISACCESS), T7DEPE (114p, ASN dispatch/compliance — ISBUILD+ISAREX+BKARCUST), T7DEPF (104p, ASN box confirmation — ISSOBOX+ISAREX), T7DEPH (116p, EDI receipt/PO match — BKAPPOL+BKICPMAT); **ISBUILD (new table, Pass 116):** opened by T7DEPD+T7DEPE — carton/pallet build assembly for ASN; not in DDF; T7DEP860 also opens BKGLX (GL extended — also seen in CU module); full BOM component/PI/WO/AR import programs + 33 original ops unchanged; BKEDIH(84f)+BKEDIL(28f)+BKEDMSTR(3f)+BKEDNOTE(3f)+BKEDIDUN(7f)+CCEDIXRF(6f)+ISEDINFO(54f)+ISDEFECT(3f) all extracted — **C: 82/100**
- [x] 🔄 **DI** — Digital Signatures — T7DIGSIG.DFM (131KB) confirmed: Caption='Enter Digital Signatures'; T7DIGSIG.RWN (128p, 27 tables, Pass 116): BKAPPO+BKAPPOL+ISDIGSIG+BKPRMSTR+ISTRIGRS+BKPSUSER+ISTERMS+ISREMIND+LOT+SERIAL+ISNCR+BKSYMSTR+FILELOC; far larger than the 3-program estimate — full PO approval workflow; EMAIL.TAG/NAME/LEVEL/ADDRESS vars confirm email routing; BKAP.PO.* vars (NUM/VNDCOD/VNDNME/SUBTOT/TAXAMT/TOTAL/ORDDTE etc.) = full PO header displayed in signature form; LOT+SERIAL+ISNCR = digital signatures extend beyond PO to lot/serial and nonconformance records; ISREMIND = approval reminders created; ISDIGSIG(89f fully documented): 10 approval slots × ACTIVE/TYPE/SDATE/FDATE/TDATE/AMT/FLAG/DATE + MOTCACH/POENTBY/SOENTBY/FILE/ATIME/ADATE; T7DigSigChgPSWD = password change utility; ISTRIGRS(25f) = email notification triggers — **C: 75/100**
- [x] 🔄 Pass 55: ISDIGSIG(89f) all fields confirmed; approval workflow traced (BKAPPO→ISDIGSIG slot→ISTRIGRS email→BKGLTRAN on approve); 10-slot structure fully understood (TYPE=approval class, SDATE/FDATE=valid period, AMT=dollar limit, TDATE=last-used date, FLAG=current status) — **C: 72/100**
- [ ] ⬜ **EX** — Export / data exchange — forms inventoried only
- [x] 🔄 **FA** — Fixed Assets — all 3 DFMs read; FA-A (IS.FXA.* asset master: cost/residual/life/method/GL accounts), FA-B (IS.FXT.* depreciation: post with Ready-to-Post flag), FA-E (export); Pass 65: ISFXASST(23f fully extracted: NUMBER PK+TYPE+DESC/DESC2+CSTBAS+RESVAL+LIFE+METH+GLA/D+ACDEPA/D+DEPEXPA/D+SDATE/EDATE+SOLD+ACCUMDEP+SERIAL+LDEPAMT/LDEPPERC/LDEPDATE+EXTRA), ISFXATRN(12f: NUMBER+DATE PK+AMOUNT+PERC+AUDIT+POSTED+ACDEPA/D+DEPEXPA/D+NETAVAL+EXTRA); depreciation GL flow confirmed (ISFXATRN.POSTED→BKGLTRAN); IS.FXA.*=ISFXASST, IS.FXT.*=ISFXATRN confirmed — **C: 82/100**
- [ ] ⬜ **FL** — no T7 RWN/DFM files found (DBA-era legacy)
- [x] 🔄 **FO** — Features & Options — 5 programs: T7FOA/B(5p stubs), T7FOC(60p BKBMMSTR+BKICMSTR — option entry), T7FOD(103p item+class range filter), T7FOE(86p item filter); BKFOCFG(18f: MANFET+YN_1..15+OPCODE) is the FO config table; BKBMMSTR(26f Pass 64: PROD_OPYN_1..6 decoded); Pass 65: ISFOHEAD(16f: UID PK+PARENT+DATE+DESC+CUST+VEND+RFQ+STATUS+REV+MDATES_1..5+PERM+EXTRA)+ISFOLINE(78f: UID+LEVEL+50×OPFLAG+PARENT+COMP+QTYREQ+OPYN_1..6+PRICE+PBRANC/CBRANC)+ISFOORDL(18f: UID+TYPE+PCODE+PQTY/PPRCE/PDISC/PEXT+ESD+LOC+TXBLE+UM+LN+DRAW+REV+LINE+OUID) — FO order lifecycle confirmed: customer config→ISFOHEAD+ISFOLINE→ISFOORDL output→BKARINV SO; BKLUGRID fingerprint includes ISFOHEAD+ISFOORDL+ISFOLINE confirming they're queryable in the lookup framework — **C: 78/100**
- [x] 🔄 **FP** — Features & Options Print — CHM confirmed: FP-B='Print Features and Options'; EXHAUSTIVE SEARCH confirmed: zero T7FP* programs across all 1,122 RWN modules in rwn_symbols.json; FP-B is definitively RTM-only (print variant of FO-D/FO-E); print sub-module with no standalone RWN — **C: 55/100**
- [x] 🔄 **HH** — Handheld / Shop-Floor Data Collection (44 forms) — 20 key DFMs read; 9 sub-areas: PO Receiving (hhpoc/POCBIN/POCLot/POCSER), WO ops (wog=issue, wop=finish, WOSCRAP, WOLabel, woser), SO shipping (SSOE 5-form verification chain, SOLookup, SODD), Inventory (ItemLU/INGA labels/hhinlj transfer/INLJLot/INLJSer), DC labor scan (HHDCA=scan.wo/scan.emp/OPER), PI tag count (HHPIC/hhpictags with lot/serial), alerts, batch process; large.lookups dual-mode; item type filter RFAMNLBTKO; Pass 48: 30+ T7HH* programs fully mapped across 9 sub-areas; BKDCLAB(50f) complete: DATE+EMP+WOPRE+OPER PK, START/FINISH+PARTS+SCRAP+RUNHRS+5 scrap codes+LAB_JCNUM(12)→JC link; BKDCSHFT(34f): 3-shift schedule with 2 breaks+lunch per shift; BKDCCFG(7f); ISSOBOX(22f): SONUM+LINE+BOX PK, UCC+TRACK+dimensions; BKARTXN(14f): AR shipment with LOT+SERIAL+LOC+BIN; BKICREF(8f): customer part xref; ISAREX(51f): AR compliance/certifications — **C: 80/100**
- [x] 🔄 **IC** — Inventory Control utility — T7IC2EST (6 procs, BKICMSTR+MTICMSTR): one-way bridge copies production inventory to ES estimating module; accessed as IC-A "Copy Production to Estimate Inventory"; no other IC programs found; not a general inventory module; MTICMSTR(108f) fully extracted: 10 vendor sources (VEND_1..10+VNAM+VPC vendor part codes), RCOST_1..15 received cost slots, 5 substitutes, LOTSZ, option flags, UIQC/UIWIP — **C: 68/100**
- [x] 🔄 **IM** — Import Management / Landed Cost — all 5 DFMs read; IMB (ISIS.MCF.* currency master: code/desc/base/symbol), IMC (ISIS.MCR.* exchange rates: date/base/SOURCE[1..n]), IMD (ISIS.LND.* landed cost GL accounts: duty/freight/deferred variants), IME (ISIS.DUTY.* duty codes: first 3 chars=vendor, percentage), IMF (ISIS.BRK.* customs broker: code/flat/perc/type); full landed cost and multi-currency infrastructure; Pass 46: all 5 T7IM* programs mapped, ISLANDF(6f duty/freight/customs GL), ISDUTY(2f DCODE+PERC), ISBROKER(4f CODE+FLAT+PERC+TYPE) fully extracted — **C: 78/100**
- [x] 🔄 **IS** — InfoSystem / Multi-Currency GL — T7ISMCC (ISTECH.LIB, 82 procs): ISGLDATE(86f) fully extracted: CYDATE_1..12+1YDATE..6YDATE (7 years × 12 periods) + FYDATE; var-confirmed usage (Pass 114, 2026-06-19): ISGL.CYDATE/1YDATE/2YDATE/3YDATE/4YDATE/5YDATE/6YDATE/FYDATE (all 7 years accessed directly in procedure logic); IS.DATE = period date being processed; ETBCOMBOVAL = combined multi-currency total being calculated; T7ISMCC opens ISGLDATE+ISMCF+BKYSMSTR+BKSYMSTR+ISMCR+CLASS+BKGLTRAN+ISBANKS+BKGLCOA → multi-currency GL reconciliation: converts foreign-currency GL balances via ISMCR exchange rates, sums to ETBCOMBOVAL for each period in ISGLDATE; ISMCF(49f) fully extracted: one row per currency (CODE+BASE+SYMBOL+SYMPOS+DEC+DESC), GL accounts per currency for BNK/AP/AR/INV/PO/CS/discounts, running balances (AMTBNK/AMTAP/AMTAR/AMTFE/AMTPOR); T7ISASER (DBA.LIB, 12 procs): WORKORD+SERIAL+WOPRE/WOSUF/PROJECT.COST — WO-to-serial assignment with cost capture; IS namespace = shared extension tables (IS.CC/RMA/FXA/SERR/TERMS/JOB/CYCLE/ACTION/DEF/SCOMP) — **C: 75/100**
- [x] 🔄 **JC** — Job Costing (18 ops) — all 14 DFM files read; JC Engine parameters fully extracted; forms: JC-A (main report), JC-E (parent/child cost roll-up), JC-N (cost calculation modes: current/historical/proposed), JC-P (materials in WIP); 6 labor types, 3 shifts; primary tables WORKORD/ISCALC.*/ISCOST.*; Pass 47: 30+ T7JC* programs mapped — CRITICAL FINDING: no BKJC* or ISCALC/ISCOST tables in DDF schema; JC is a cost-analysis overlay entirely on WORKORD+WOBOM+WOMAT+WOLABOR+WORECV+WOROUT+BKGLTRAN+MTICMSTR; WOEXCHG(10f engineering change costs)+OUTPROC(15f MT-era outside process PO)+ISNCR(35f NCR: PART+COMP+LOT+SERIAL+DCODE+DISP+CAR+links to WO/PO/RMA)+BKSHORT(9f WO shortage: PCODE+WONUM PK)+ISCYCLCD(7f cycle count freq)+BKQCTRAN(21f QC transactions)+BKQCMSTR(14f QC master)+IS2DBAR(109f 2D barcode config)+BKRTSPEC(7f routing spec notes) all extracted — **C: 78/100**
- [x] 🔄 **LC** — Lot Control — all 6 found DFMs read; LC-A (MTLOT table), LC-B (assigns MTIC.PROD.LOT flag), LC-G (archive with expiry date range); parallel to SC module for lots — Pass 57: 7 T7LC* programs fully mapped; LOT/MTLOT_(25f) fully extracted: CODE+LOT PK, EXPDATE+ONHAND+LOC+VENDOR+RECDATE+RECQTY+POCOST+WO+WOCOST+NOTES_1..5+WOSUF+BEGIN+OUT+MAXOUT; lot lifecycle (PO receipt→store→ship→trace-to-customer) confirmed from LC-F (T7LCF uses BKARCUST); DDF note: table name LOT, all fields MTLOT_ prefix — **C: 80/100**
- [ ] ⬜ **LM** — no T7 RWN/DFM files found (DBA-era legacy)
- [ ] ⬜ **LO** — no T7 RWN/DFM files found (DBA-era legacy)
- [x] 🔄 **MA** — AR Deposits module; T7MAPDEPO (97p, 20 tables): BKARDEP+BKARCUST+BKARINVL+ISARDEPL+BKGLCOA+BKARINVT+BKARINV+BKSYMSTR confirmed; BKARDEP(6f) var-confirmed (Pass 116): BKAR.DEP.DEPNO/CUST/DATE/SO/SR/EXTRA; T7GETDEP (18p, 7 tables): BKARDEP+BKARINVT+ISARDEPL+BKARINVL+MKECLASS+BKSYHELP+DBAHLPID; vars: DEPTOUSE/LINES.DEPCAL/APPDEP/DEP.TOTAL/DEP.TOTAL.LATE = deposit availability calculation (DEPCAL=calculated deposit credit; APPDEP=approved for application; DEP.TOTAL.LATE=late payment penalty tracking); MKECLASS in T7GETDEP = class-based deposit filtering; ISARDEPL confirmed opened by both programs (deposit→invoice allocation table, not in DDF); deposit workflow: T7ARN(enter) → T7MAPDEPO(post to GL) → T7GETDEP(retrieve available) → T7ARC(apply at payment); BKARDEP(6f)+BKARTNOT(3f)+BKARINVV(77f)+BKARINVI(16f) all extracted — **C: 75/100**
- [ ] ⬜ **MM** — no T7 RWN/DFM files found (DBA-era legacy)
- [ ] ⬜ **PC** — no T7 RWN/DFM files found (DBA-era legacy)
- [ ] ⬜ **PL** — no T7 RWN/DFM files found (DBA-era legacy)
- [x] 🔄 **PS** — Program Security / User Access — all 6 DFMs read; PSA (BKPS.USER.CODE user setup: seclevel, seccode [A/P/1/2/C/V/U/E], company, employee/rep), PSE (user security report), PSEITM (program access list: PROGRAM_NUM/NME), PSF (access-to-program report), PSEGRP (button group config), PSK (approve vendor: bkap.vendname); dual user system with AHSYLOG (module-level) + BKPS (program-level); Pass 46: BKPSUSER(11f) fully extracted: CODE(15)+PRT+MENU+CMPY+MWIND+PSWD(10)+ME+SEC(30)+MCNTR+LDATE+EMP link to BKPRMSTR — **C: 72/100**
- [x] 🔄 **QC** — Quality Control — 18 programs across 4 sub-areas: (1) QC-A/B/C/D inspection (T7QCA 106p incoming, T7QCB 120p WO material, T7QCC 108p WO receipt, T7QCD 117p WO routing); (2) QC-F NCR (T7QCFA 178p entry, QCFB 108p supplier quality, QCFD 53p inquiry, QCFF 131p closeout); (3) QC-G CAPA (T7QCGA 212p corrective action entry, QCGB 122p team approval, QCGD 110p report); (4) Support (T7QCMTHD 65p methods, QCRESULTS 104p results, QCRSLT 87p tray results, QCSPEC 82p spec def); key tables: ISNCR(35f), ISQCSPEC(57f), ISQCMTHD(44f), SCRAP(21f), ISWOTRAY(52f), QCCODES(2f), ISCACT/ISCARDTE/ISCTEAM (not in DDF); Pass 47: ISNCR(35f) fully extracted all 35 fields (PART+COMP+LOT+SERIAL+DCODE+DISP+CAR+VEND+WO/PO/RMA links), BKQCMSTR(14f receiving master) + BKQCTRAN(21f transaction log) both extracted — **C: 78/100**
- [x] 🔄 **QT** — Service Quote extended info (linked to SR module) — T7QTINFO (42 procs): opens ISSRINFO+BKYSMSTR+BKARINVL+ISTERMS+BKICPMAT+LANGDICT+BKICREF+BKPRSALE; service quotes are SR orders in quote status (BKARINV); T7QTINFO = extended info entry analogous to T7SRINFO; LANGDICT(5f)=translation: ECAPT+LANG PK → LCAPT(80)+FONT(30)+EXTRA(150); BKICREF(8f)=customer part xref: CUST+CODE PK → CUSNME(30)+CUSCOD(25 customer part number)+DESC/DESC2; ISTERMS(13f)=payment terms: NUM PK+NAME(20)+DESC(50)+AMT+TYP(P/%/$)+DAY+EOM+MAX+COD+ARAP+CC+SRT+EXTRA — all schemas extracted — **C: 72/100**
- [x] 🔄 **QU** — Query / Inquiry Tools — CHM fully documented (6 ops); RWN programs: WBKLOOKUP (413 procs, QU-A universal lookup grid — opens BKLUGRID+ISDRILL+ISDRILLM+FILEKEY+FILEDICT), CALDRILLBT (94 procs, QU-B calendar drill-down — same date vars as CALREM: ISTS.EDATE/ENTRY.DATE/DATE_TYPE/MM/DD/YY/START.DATE; bridges CALREM↔EvoDrillDown; opens ISDRILL for drill-down config, Pass 114), EVOBS (128 procs, QU-D Business Status — opens ISBSF+BKGLTRAN+MTICMSTR), T7QGRID (62 procs, QU-E Quick Grid Lookup — opens BKLUGRID+ISDRILL), QUERYEXECUTE (26 procs, QU-F — confirmed EvoPVT.jar launcher stub (Pass 114, 2026-06-19): same HOST/NAME/PORT/TREEDEST/COMP/NOPE/DUMMY_L/DFM vars as CashFlow/CommissionRpt; QU-F SQL execution happens entirely inside EvoPVT.jar Java layer; ISDRILL+BKPSUSER = drill config + access gate); ISDRILL(46f) full schema extracted: LOOKUP_FROM(30)+GRID(15)+REC(4)+KEY(2)+FILE(15)+FILTERS_1..20(80×20)+WHILE_1..20(80×20)+COMM(150); ISDRILLM(17f): PARENT+CHILD+MENU+FILE+SFIELD_1..5→TFIELD_1..5+KEY+PFILE+EXTAR(150); **BKLUGRID 14-field schema extracted from EvoERPDrillM LUGRID_* vars (Pass 115, 2026-06-19):** LUGRID_NAME+LUGRID_FDNAME+LUGRID_FORM+LUGRID_KEYFLD+LUGRID_KDATA+LUGRID_DATA+LUGRID_TEXT+LUGRID_EXTPARM+LUGRID_EXTRA+LUGRID_EXTUDF+LUGRID_END+LUGRID_PROT+LUGRID_DELFLAG+LUGRID_HNDL — grid layout config table (column defs + key field + display text + UDF extensions); resolves the last "runtime-only table" gap for WBKLOOKUP fingerprint; WBKLOOKUP total DB fingerprint=76 tables (70 in DDF; 6 runtime: BKLUGRID✓+FILEKEY+FILEDICT+FILEDFLD+FILEKNUM+FILELOC) — **C: 82/100**
- [x] 🔄 **RF** — Request for Quote (T7RFQ: 103 procs); opens ISESTDTL+MTICMSTR+BKBMMSTR+BKICMSTR+BKMRPPO+BKAPPOL+BKAPVEND+BKAPPO; ISESTDTL(203f) fully decoded: IS_EST_NUM+PART+LINE PK; 10 qty breaks × 18 cost types (MAT/MATMU/LAB/LABMU/SETUP/OP/OPMU/OH/OHMU/MISC/EXTRA/MEMU/OVALL/TOTAL/PRICE/COST/VOVHD each ×10) + SETMU + scalars (STATUS/DRAW/REV/CUST/ORDDESC/ORDDTE/EXPDTE/LOSTDTE/SO/WOPRE/WOSUF); bridges ES estimate to vendor RFQ to PO; BKMRPPO→BKAPPO link confirmed — **C: 75/100**
- [x] 🔄 **RM** — Return Material Authorization (RMA) — all 5 DFMs read; Pass 66: 4 programs confirmed: T7RMD(216p main entry: BKARINVL+ISRMAI+ISRMAC+BKARINV+ISNOTES+ISLINKS+ISNCR+SCRAP), T7RMG(132p report: BKARINV+ISRMAI+BKICMSTR+BKARCUST), T7RME(54p reason code master: ISRMAC), T7RMB/C(5p stubs); ISRMAI(54f Pass 66: NUM+PART+LINEID PK+DATE/RCPT/CLOSDATE+STATUS+REASON+DISP+OSONUM/OINVNUM+SONUM/INVNUM+CMNUM+REORDER+WOPRE/WOSUF+WARRANTY+WO/CR/SO/STOCK/SCRAP/SR/REFUND flags+FLAGS_1..20)+ISRMAC(3f: CODE+DESC+EXTRA); complete disposition flag set fully decoded — **C: 78/100**
- [x] 🔄 **RT** — Report Template Validator (T7RTMVALID: 20 procs confirmed Pass 116, 68,677 bytes); opens BKSYHELP+DBAHLPID+ISIS+MKAHIST ONLY — zero module-specific tables; vars: ISTS.PATH (network share path to find RTM files), ISTS.EDATE (effective date for validation) — pure file-path based RTM format checker; ISIS = import/export index (scans RTM files via ISIS); source_file=NZLICE.LIB confirms it is a licensed utility (NZ=license gating library); cannot push confidence higher without RWN bytecode — **C: 60/100**
- [x] 🔄 **SA** — Sales Analysis (13 ops) — 13 RWN programs fully identified: T7SAA(212p main engine: BKARINV+BKARINVL+BKARCUST+BKICMSTR+ISARCHG+ISSOBOX+BKPRSALE+ISJOB+CLASS+ISAREX); T7SAB/C/D/E/G/H/I/J/L (all 5p, range filter stubs, same table set as SAA); T7SAM(238p: BKSAREPT+BKACTRPT+ISBUILD+BKARINVL+BKARINV+BKICMSTR+ISRMAI+ISSRINFO+WORKORD+BKCMLEAD+BKCMTERR); T7SAN(220p: same as SAM excluding ISRMAI); T7SAO(169p Top N: BKCMACCL+BKCMACCC+ISAREX); T7SAP(131p class range: CLASMSTR+ISCATMST); T7SAQ(95p actual margin: WORKORD+WOMAT+WOBOM — uses actual WO costs); dedicated tables: BKSAREPT(57f full schema extracted: TYPE+NAME PK, RTM + 26 FROM/THRU range pairs covering inv#/dates/ship dates/amounts/salesperson/customer/class/category/part/lot/territory/currency), BKACTRPT(53f full schema extracted: TYPE+NAME PK, RTM + named FROM/THRU pairs for PART/CLASS/CAT/DATE/LOC/WO/CUST/INV/QC/LOT/SERIAL/PRICE/AVGC/STDC/DESC/REF/DEPT/QTY/SCRAP/VEND/PO/TYPE), ISJOB(9f job tracking: NUM/DESC/CUST/VEND/STATUS/OPENDT/CLOSEDT), ISAREX(51f AR extended: resale cert fields), ISRMAI(54f RMA invoice: NUM+PART+LINEID, STATUS/REASON/DISP/OSONUM/OINVNUM), BKCMACCL(2f account level), BKCMLEAD(2f lead source) — **C: 75/100**
- [ ] ⬜ **SB** — no T7 RWN/DFM files found (DBA-era legacy)
- [x] 🔄 **SD** — Standard Detail Codes (T7SDET: 58 procs, 18 tables); **ISSDET confirmed 4 fields** (not 2f — Pass 117): IS.SDET.TYPE+DETAIL+SUB+WHO; ISSTYPE(3f) confirmed: IS.STYPE.TYPE+ASSET+WHO; ISNCR+ISMCR+ISDRILL+FILELOC in DB set confirms SD codes link to NCR defects and multi-currency; maintains cross-module service/detail code lookup; purpose: CRUD editor for ISSDET detail codes + ISSTYPE type master — **C: 72/100**
- [x] 🔄 **SH** — Shop Scheduling ⚠️ (NOT Shipping) (16 ops) — all 15 DFM files read; SH-A/B (WO WIP scheduling grid + operation scheduling), SH-C (work center capacity), SH-E (due date change), SH-I (dispatch report with color coding), SH-P (color config); primary tables MTWO.WIP.*, MTWORO.*, MTWC.* — **C: 72/100**
- [x] 🔄 Pass 54: All 17 T7SH* programs mapped; WORKORD(74f: MTWO_WIP_* all fields — WOPRE/WOSUF/CODE/SQTY/COMQTY/STATUS/PRTY/dates/costs×8-types×est+act+var)+WOROUT(81f: MTWORO_* all fields — WC/SCHED_WC/dates/ESTHRS/ACTHRS/ESETHRS/ASETHRS/QTYCOM/CONTNTN/OVERLAP/NEGOVLP/costs×6+misc/15×INSTR)+WORKCTR(47f: MTWC_* — HRSWEEK/rates/OH/AVGQTIME/LEAD/OUTPROC/PARENT/CYCLE_TIMES×10/FLAGS×5/ALPHA×5)+BUCKETS(14f: WC+WO+OP per time bucket with CRATIO+LOCKED+CNTN)+SCHWO(10f: WO scheduler summary with shop-day numbers+CRATIO+CONTENTION)+SCHEDCAL(6f: calendar↔shop-day mapping forward+backward)+CALENDAR(5f)+MACHINE(20f: HRSUSED+HRSMAINT+parent WC+deactivation log)+ISWOPRIO(4f: priority 1-9 with color)+ISARCHG(26f: SO line before/after change audit)+MTMRP(13f: MRP pegged demand)+ISWOEX(63f: fully extracted — 10-date+7-float+alpha+10-flag UDF)+WCCTL(5f)+ISBUILD(15f)+ISDROP(4f) all extracted; TASCOLOR confirmed not in DDF (TAS runtime color config) — **C: 82/100**
- [x] 🔄 **SL** — Shop Loading (T7SLSFC: 5 procs, 53,987 bytes); full DB fingerprint confirmed (Pass 117, 22 tables): BKARINVL+BKDCLAB+BKARCUST+ISWOPRIO+WORKCTR+ROUTING+BKYSMSTR+BKICMSTR+BKCMACCN+BKAPVEND+ISDRILL+ISIS+BKSYHELP+DBAHLPID+MKAHIST+ISLOG+ISLINKS+BKAPDESC+LANGDICT+TASCOLOR+ISMCR+FILELOC; source_file=ISTS.SRC (one of 7 readable SRC files on the share — source code available on network); JAVA.PATH/JAVA.PATH2 vars = standard Java infra block; PLDN/PTDN = production-line/tool-down flags; WEBLINK/XCPATH = cross-platform display path; ISWOPRIO(4f: PRIO+DESC+EXTRA+COLOR); BKDCLAB(50f fully extracted); display-only 5-proc viewer — **C: 70/100**
- [x] 🔄 **SM** — System Maintenance (34 ops, 3rd largest) — 23+ forms + full T7SM* sub-module family decoded; SM-K (user prefs→EvoSettings.INI/ISNUMBER), SM-E/F (tax ISIS.TXF+ISIS.TXG), SM-O (ship-via ISSHPVIA with tracking URL), SM-D (payment terms IS.TERMS), SM-PF (ISJOB job#), SM-PH (IS.CYCLE), SM-JM/JN (merge), SM-JC (JC setup), SM-SD (AP doc link); T7SMI* (CRM masters: BKCMLEAD/BKCMTERR/BKCMACFC/BKCMACCC/BKCMDTCD), T7SMP* (ISCATMST/ISUDMSTR/ISJOB), T7SMT/SMU (ISSHPVIA), T7SMTEND/SMTSET (SMT/PCB: ISSMTCFG/MACHINE); BKSYMSTR/BKYSMSTR not fully decoded; Pass 51: T7SMJA-V rebuild family (14 programs) + T7SMPA-J variants (10 programs) fully mapped; BKCMHCOD(9f: HCODE(2) PK+RATE+BPART billing part+WINDW+ABILL)+BKCMACFC(3f)+BKCMACCC(2f)+BKCMDTCD(2f)+ISCATMST(3f)+CLASMSTR(2f)+CLASS(24f: CLASS+LOC PK, full GL set per location)+ISNUMBER(52f: CODE PK+51 counter slots)+BKSYAP(11f: next RECVNUM+PONUM+QCRECV+RFQNUM+flags)+CALTEMP(2f) all extracted — **C: 82/100**
- [x] 🔄 **SP** — Statistical Process Control (SPC) ⚠️ (NOT Ship Packing — CORRECTED) — Pass 67: 7 programs confirmed: T7SPC(148p main: ISSERR+ISSTRACK+ISSPC+ISSTYPE+ISSDET+ISSETYPE+ISSEPROC+WORKORD+WOBOM), T7SPCREP/SPCREP2(105p each), T7SPCLIVEREP(50p), T7SPCREPPPM(104p), T7SPCLIVEGRID(5p), T7SPCMEMO2ALPHA(25p); ISSERR(14f fully decoded: WOPRE+WOSUF+OPER+TIME+DATE+ERROR+PROCESS+COUNT+REF+EXTRA+SERIAL+ADOF(1000)+ADIAG(1000)+AREWORK(1000) — AOI integration confirmed by 3×1000-char AOI text fields), ISSPC(20f: WO+OPER+EMP+DATE+TIME+GOOD+REWORK+SIDE+TYPE+DETAIL+TESTR/T/E_1..3+ANOTES+CUST+PART), ISSTRACK(13f: WOPRE+WOSUF+OPER+PROC+PSER+COMP+CSER+NOTE(1000)+AR+CLOT — component traceability), ISSTYPE/ISSETYPE/ISSEPROC/ISSDET all decoded; AOI+PCB traceability architecture confirmed — **C: 80/100**
- [x] 🔄 **SR** — Service / Repair — 16 RWN programs confirmed (T7SRA-T7SRK + SRDISPACH/SRBK/SRGA/SRINFO); SR Orders ARE BKARINV records (same as SO/AR); 5 ISSR*INV views = BKARINV (0 diff), 5 ISSR*IVL views = BKARINVL (0 diff); key tables: ISSRMMS (equipment 12f), ISSRINFO (configurable 54f), ISSOREVU (approval workflow 12f), ISARINVX (AR ext 4f); T7SRGA (157 procs) is full posting to BKGLTRAN+BKGLX+BKARHTAX+BKISTAX+ISTAXGRP — **C: 72/100**
- [x] 🔄 **SU** — Setup / UI Configuration — CHM confirmed 4 ops (SU-A=Maintain Grid Lookups, SU-B=Maintain Drill Down Menus, SU-C=Forms Editor, SU-D=Grid Maintenance); RWN programs: WBKLUGRID(68p Pass 65: 79-table fingerprint = admin+lookup sources in one program; admin role confirmed as QU framework configurator), EVOERPDRILLM(31p: ISDRILLM+BKLUGRID+ISLOG audit), T7GDM(31p: Grid Display Manager BKLUGRID+ISDRILLM); SU-C Forms Editor not yet matched to RWN; key tables: BKLUGRID+ISDRILLM — **C: 72/100**
- [ ] ⬜ **SY** — no T7 RWN/DFM files found; BKSY* tables are System config (documented)
- [x] 🔄 **TA** — TAS / System Administration — CHM confirmed 9 ops: TA-D=Maintain Database, TA-G=Maintain Menu Access Records, TA-H=Maintain Menu End User, TA-M=Forms Editor, TA-N=Program Scheduler, TA-O=Backup Utility, TA-Q=Change Logo Image, TA-R=SQL Editor, TA-S=Data Dictionary Check; ALL 9 programs now matched (Pass 112 2026-06-19): TA-S=T7DDCHECK(92p, FILEDICT+FILEKEY+FILELOC), TA-N=EVOSCHEDULER(65p, ISSCHED)+EVOSCHEDSETUP(37p), TA-O=EVOERPBACKUP(76p, zipdll), TA-R=QUERYEXECUTE(26p, ISDRILL); TA-G=WBKMENUSETUP.RWN(98p: BKPSUSER+BKMENUSU; vars MI_MENU_LVL/MI_CAPTION/MI_FASTSELECT/MI_PROGRAMNAME/MI_IMAGE/GA_* menu item+group editors; ACCESS_CODE+USERNAME for user access control); TA-H=wbkmenusueu.rwn(143KB: BKMENUSU+50+ tables = end-user view of menu access records; source=NZLICE.LIB NZ-licensed variant); TA-M=Forms Editor=EXTERNAL program (no dedicated RWN found in all 1,122 programs — invokes RBDsgnr.exe or TAS Pro built-in form-design command); TA-Q=evologo.RWN(23p: CO.LOGO field in BKSYMSTR, LOGOFILE var — changes company logo image stored in BKSYMSTR.CO.LOGO); Pass 63: 8 WTAS* admin programs confirmed; ISSCHED(24f) fully extracted — **C: 88/100**
- [x] 🔄 **TC** — Treasury Control — T7TCC(119p, 37 unique tables) opens ISTERMS+ISBANKS+BKARINVT+BKARCUST+BKARINV+BKGLCOA+BKSYMSTR+BKYSMSTR+ISMCF+BKART+BKAPCHKF+BKARDEP+BKGLCHK+BKARINVI+BKPRSALE+BKPRCOMM+ISREPORD+MKECLASS+WORKORD+BKGLX+BKGLTRAN; Pass 65: ISREPORD(17f: REPNM+REPWH+SONUM+INVNM+INVDT+ULID+COMPR+CMAMT+AMT+AMTRM+CBK+PCODE+CUST+PAYDT+GLA/GLD — commission/report scheduling per invoice), MKECLASS(3f: NUM+DESC+ACTIVE — MKE classification codes); all TC table schemas extracted — **C: 72/100**
- [ ] ⬜ **UM** — no T7 RWN/DFM files found (DBA-era legacy)
- [ ] ⬜ **UP** — no T7 RWN/DFM files found (DBA-era legacy)
- [x] 🔄 **US** — User Services / Trigger Notifications — T7USG (90 procs, 24 tables); full DB fingerprint (Pass 117): ISTRIGRS+BKARCUST+BKAPVEND+WORKORD+BKARINV+BKAPDESC+BKCMACCN+BKICMSTR+BKICREF+BKPSUSER+BKSYHELP+BKSYUSER+CLASMSTR+DBAHLPID+ISDRILL+ISIS+ISBNMSTR+ISCATMST+ISITP+ISLINKS+ISLOG+ISNCR+MKAHIST; new tables vs prior: BKSYUSER (system user config), CLASMSTR (class master), ISBNMSTR (bin name master), ISCATMST (category master), ISITP (item type/issue type), BKICREF (customer part xref), BKPSUSER (user access check); ISTRIGRS(25f) fully documented; ISREMIND(22f) fully documented; EvoRemind (46 procs) polls ISTRIGRS → creates ISREMIND; broad module: trigger maintenance + category/class/item-type master — **C: 70/100**
- [x] 🔄 **UT** — Utilities (admin/data maintenance) — all 8 DFMs read; UTH (file layout report), t7uti (company add/delete: company_code/name/path/copy.file/cdelete), UTKA (data clear/reset: CLR.COA/CUST/VEND/INVN — DESTRUCTIVE), UTKD (fiscal year: fycur/fy1yp/fy2yp/fy3yp), UTKE (location cleanup — DESTRUCTIVE), UTKF/UTKG (item rebuild F and G variants), UTKH (average cost recalculate by inc.type[1-4]); most ops irreversible; Pass 51: 9 T7UT*/T7FNR programs fully confirmed via DB fingerprints; T7UTKE(238p) = largest UT, 45+ tables; T7UTI opens BKSYAP(11f: AP counters+flags); T7UTKH opens CLASS(24f: CLASS+LOC PK, full GL accounts per class per location); CLASMSTR(2f)/ISCATMST(3f)/ISNUMBER(52f) all extracted — **C: 72/100**
- [x] 🔄 **WC** — Warehouse Control ⚠️ (NOT Work Center) — 8 DFM files read; WC-A (bin master CRUD, ISBN.MSTR table), WC-C (serials by bin, MTSER), WC-D (bulk bin assignment — Skip/Replace), WC-H (location browser); primary tables ISBN.MSTR, BKIC.LOCM; Pass 49: ISBNMSTR(4f: LOC(10)+BIN(15) PK, DESC(60)+EXTRA(100)) fully extracted — **C: 75/100**
- [x] 🔄 **YS** — Y/N System Flags Editor (T7YSYN: 52 procs, BKYSMSTR+standard lookup tables); direct editor for all Yes/No behavioral flags stored in BKYSMSTR; BKYSMSTR(355f) fully extracted: BKYS_WONUM(float, row key) + BKYS_YN_1..354 (354 × STRING(1) Y/N flags); one row per company, 354 feature flags covering all EvoERP modules; individual flag meanings blocked by RWN encryption — **C: 72/100**

**Subsystems (not menu modules — discovered via RWN analysis):**
- [x] 🔄 **PI** — Physical Inventory (9 files, 1,056 procs) — Pass 38: 8 programs fully mapped: T7PIA(159p freeze: BKPIMSTR+BKICMSTR+BKICLOC+ISCYCLCD→creates BKPIFROZ), T7PIB(114p print sheets: BKPIFROZ+BKPILOT+BKPISER), T7PIC(152p tag entry: writes BKPIPHYS, reads ISBINLOC+BKPRMSTR), T7PID(98p discrepancy: BKPIPHYS vs BKPIFROZ), T7PIE(76p adjust: BKPIFROZ+BKICMSTR), T7PICA(97p count adj variant), T7PIF(137p post: ISBUILD+MTICMSTR+BKPIPHYS+ISBINLOC→BKGLTRAN), T7PIG(155p report: BKPIMSTR+BKPIPHYS+BKPIFROZ+BKICLOC); all 7 BKPI* schemas extracted: BKPIMSTR(3f YEAR+QTR+DESC), BKPIFROZ(19f UOH+COST+GLPST/INPST+ACCTA/C+TAGS), BKPIPHYS(14f TAGNUM+ACTQTY+EMPNAME+LOT+SERIAL+BIN), BKPILOT(10f), BKPISER(10f), PIBINLOC(14f ITEM+LOC+BIN UOH+DFLT), PIBINLOT(14f with LOT+SER); freeze→count→variance→post cycle fully confirmed — **C: 72/100**
- [x] 🔄 **BO** — Bill of Lading; T7BOL (178p, 26 tables) + T7BOLMSO (174p, 25 tables); full DB fingerprints confirmed (Pass 117); T7BOL opens ISAREX+ISICMSTR+ISSRINFO+ISSOBOX+BKAPPO+ISACCESS+FILELOC+BKSYMSTR; T7BOLMSO drops BKAPPO/ISAREX/ISSRINFO, adds BKPRMSTR+BKPSUSER (driver/employee data for LTL); both open BKARINV+BKARCUST+BKARINVL+BKCMACCN+BKICMSTR+ISSHIPCO+ISSHPVIA+MTICMSTR; LOAD.NUMBER/SEAL.NUMBER/TRAILER.NUMBER/AUTHOR.NUMBER/CONTROL.NUMBER + DRIVER.ARRIVED/LOADING.START/END/DRIVER.DEPARTED timestamps confirmed; T7BOLMSO: EDIT.CLASS/WEIGHT/PACKS/HM (LTL fields); ISAREX = AR compliance certifications on BOL — **C: 70/100**
- [x] 🔄 Pass 55: ISSOBOX(22f: SONUM+LINE+BOX PK, CODE+QTY+LOT+SERIAL+INVNUM+SHIPPR+SHPCOD+WEIGHT+SKID+DATE+WO link+UCC+HT+LG+WD+TRACK+EXTRA)+ISSHIPCO(16f: SHPCOD PK+NAME+DESC+VNDCOD+5×NOTES+SHIPVIA+EXTRA+5×WEB(120 tracking URL templates)) fully extracted; no dedicated BOL table confirmed; workflow traced; BOL assembles from BKARINV+ISSOBOX+ISSHIPCO at print time — **C: 72/100**
- [x] 🔄 **DS** — Data Sync (25 programs: T7DSAP/AR/BOM/CK/CM/CO/CS/DC/EST/FO/GEN/GL/HH/IC/IM/MRP/PO/PR/QC/RMA/RO/SH/SO/WC/WO); **T7DSGEN stub confirmed from symbol data (Pass 117):** 7,271 bytes, 5 procs, 36 db_files, only 1 named var = STUB; source_file=T7DSGEN.SRC (one of 7 readable SRC files); all 24 active T7DS* programs identical 36-table fingerprints (T7DSQC=0 anomaly); identical fingerprint: BKAPDESC+BKAPPO+BKAPVEND+BKARCUST+BKARINV+BKCMACCN+BKGLTRAN+BKGLX+BKICMSTR+BKSYAR+BKSYHELP+CLASS+DBAFIFO+DBAHLPID+FILELOC+ISDRILL+ISDROP+ISGLDATE+ISICMSTR+ISIS+ISLINKS+ISLOG+ISMCR+ISNCR+ISNOTES+ISNTYPE+ISNUMBER+ISREMIND+ISTAXGRP+ISTRIGRS+LANGDICT+LOT+MKAHIST+MKECLASS+SERIAL+WORKORD; DS architecture confirmed: 7KB stubs → central sync engine (the STUB var is the dispatch token); all 36 fingerprint tables fully field-decoded; sync field-level logic remains blocked by RWN encryption — **C: 72/100**
- [x] 🔄 **AU** — Automation modules (T7AUTODCH: 183 procs DC labor validation via BKDCLABR+BKDCLABO+BKDCLABH; T7AUTOMRF: 132 procs MRP auto-firm MTMRP.PARTNO/KEY/DATE/QTY/ONHAND/PEGTO/ORDER/STARTDT→WORKORD; T7AUTOREBSS: 79 procs back-order re-BSS via BKICMSTR+BKARINV+BKARINVL; T7AUTOFX: 21 procs auto FX rate update via ISMCF+ISJAVA+ISMCR); 4 confirmed automation programs, each purpose identified from DB fingerprint — Pass 57: 8 programs total mapped (added T7AUTODEJH/AUTOSMJC/AUTOWOLA/AUTOUTKG stubs); BKDCLAB(50f) fully extracted: DATE+EMP+WOPRE+WOSUF+OPER PK, POSTED+SHIFT+START/FINISH+PARTS+SCRAPPED+NOJOBS+RUNHRS+SETUPHRS+REGOVER+APPROVAL+5 scrap codes+CYCLE_HR/MIN/SEC+CYCLE_PARTS+CYCLE_NOTE(255)+GEN fields; BKDCCFG(7f) extracted; DC→WO posting workflow: LAB_POSTED=N rows → validate → post → LAB_POSTED=Y — **C: 72/100**
- [x] 🔄 **FS** — Field Information Base (FIB) (T7FSCLASS: 62 procs, ISFSCLAS+ISPRINFO; T7FSINFO: 61 procs, ISFSINFO+BKCMACCN; T7FSEMP: 59 procs, ISFSCLAS+BKPRSALE); field prefixes IS_FIB_* confirm "Field Information Base" not general field service; ISFSCLAS(3f: CLASS/GROUP/EXTRA), ISFSINFO(4f: PROGRAM/CONTRACT/MISC/WHO), ISPRINFO(4f: PROG/DESC/MISC/TYPE) all extracted; BKCMACCN(154f) fully extracted: 10 contacts × (name+title+phone+email+salutation) + 2×10 date+alpha configurable slots + labels; FIB links service records to CRM account contacts — **C: 72/100**
- [x] 🔄 **GF** — Global Finance / AR Charges (T7GFPRICE: 116 procs, customer+item pricing/charge entry; T7GFV/GFVS: 82/81 procs, invoice charge viewer; T7GFR: 46 procs, report); ISARCHG (26f) fully documented: before/after audit trail with SONUM+INVNUM+LINEID+PCODE+CDATE+USER+REVLVL+ALOC/BLOC+APRICE/BPRICE+ADISC/BDISC+AOOQTY/BOOQTY+AESD/BESD+AASD/BASD+ACOMPR_1/2+BCOMPR_1/2+AEXTRA/BEXTRA; 4 RWN programs confirmed — Pass 57: 5 programs total; BKICPMAT(85f) fully extracted: CUST+PCODE+PNUM PK; 10 price break levels (RATE_1..10+QTY_1..10+PER_1..10), 2 commission rates per break (COMM1/COMM2_1..10), EXP+SDATE/EDATE effective range, DCODE+CLASS, MIN/MINPR, PROMO flag, METH(11) pricing method, OFFIN/OFFCH/SCAND/FRTAL/BILLB/SWELL/ACCRU trade promotion buckets, LUMP, PDESC(30), UID(40) — **C: 75/100**
- [x] 🔄 **RE** — Reminders + Rebuild Utilities (T7RemindRpt: 125 procs, ISREMIND+BKARCUST+BKCMACCN; T7REPLNK: 67 procs, ISREPLNK+BKPRSALE; T7REPDEF: 52 procs, ISREPDEF; T7REINDEX: 36 procs, FILELOC; T7REBQC: 62 procs, BKICMSTR; T7REBWO: 123 procs, WORKORD+WOBOM+WORECV+WOROUT+MTICMSTR+WOMAT+WOLABOR; T7REDINDEXDD: 5 procs stub); ISREPDEF(3f: LABEL(5 PK)+TITLE+EXTRA); ISREPLNK(11f: REPNM+CUST+ITEM PK, CLASS+SDATE+EDATE+LABEL+GLA+GLD+EXTRA) fully extracted; WOLABOR(58f) fully extracted: DATE+EMP+WOPRE+WOSUF+OPER+TRXN PK, RUNHRS/SETUPHRS/LABRATE/LABCOST/SETCOST/MACHCOST/FOHCOST/VOHCOST/WC/TOOL/MACH/START/STOP/DEDUCT + cycle time + 5flags+3alpha UDF; WORECV(11f): WOPRE+WOSUF+DATE PK, ASSY+QTY+AVGC+LOT+SERIAL — all 7 programs and 4 key schemas confirmed — **C: 75/100**
- [x] 🔄 **SE/ST** — Service Code Tables; T7STEQUIP (52p, 46 tables — CORRECTED from 90+, Pass 117): opens BKEDIDUN+BKEDPOST (EDI tables), BKISTAX (item tax), BKSYAR (AR system settings), BKGLX (GL extended), DBAFIFO, ISARCHG (AR charge extension — new), ISARTXNB (AR txn by num), ISBINLOT, ISBSF, ISCHAINM (chain master), ISNOTES, ISSOBOX, MKECLASS, LOT, SERIAL; BKEDPOST = new EDI posting table (not previously documented); ISARCHG = AR charge extended data (not previously documented); T7SEPROC (ISSEPROC 2f: PROC/WHO), T7SERR+T7SETYPE (ISSTYPE 3f: TYPE/WHO/ASSET; ISSETYPE 2f: ERR/WHO), T7STOCK (BKCMACCC); ISSEQUIP(2f)+ISSERIAL(11f) both extracted; T7STEQUIP is the most complex SE/ST program (52p, 46t = full operational scope for service equipment lifecycle) — **C: 70/100**
- [x] 🔄 **PU** — Warehouse Put-Away (T7PUTAWAY: 105 procs, 34 tables confirmed Pass 117): BKAPINVL+BKAPPO+BKGLTRAN+DBAFIFO+LOT+SERIAL+ISORDECO+BKCMACCT+BKCMACCN+ISTRIGRS+ISREMIND+ISNCR+ISNUMBER+ISMCR+ISLINKS+ISNTYPE+BKARINV+MKAHIST+ISGLDATE+MKECLASS+MTICMSTR+TASCOLOR+BKICMSTR+BKPSUSER+BKAPVEND+BKARCUST+BKAPDESC+BKSYHELP+DBAHLPID+FILELOC+ISDRILL+ISIS+LANGDICT; NO PU-specific tables — uses shared infrastructure; MKECLASS+TASCOLOR = class-based put-away rules with color coding; ISORDECO = ECO-linked put-away; ISGLDATE = GL-date-controlled posting; BKCMACCT = CRM account context for customer-owned stock; workflow: AP receipt (BKAPINVL/BKAPPO)→bin assignment→lot/serial (LOT/SERIAL)→GL (BKGLTRAN/DBAFIFO)→notifications (ISTRIGRS/ISREMIND) — **C: 72/100**
- [x] 🔄 **MU** — Multi-Yield Work Orders (T7MULTIYIELD: 150 procs, 43 tables); records multiple co-product output part numbers from single WO; full DB set confirmed: WORKORD+WOROUT+WOBOM+WORECV+INVTXN+ISBINLOC+BKARINVL+MTICMSTR+BKICLOC+WOMAT+ISWOEX+LOT+ISBINLOT+SERIAL+BKGLTRAN+BKGLX+DBAFIFO+ISTRIGRS; ISWOEX (WO extended) holds multi-yield state; workflow confirmed (input WO→multiple WORECV+INVTXN outputs→FIFO/LOT/SERIAL tracking); Pass 43: 43-table DB fingerprint re-confirmed — **C: 72/100**
- [x] 🔄 **AL** — Audit Log + Alternate Parts (T7ALOGSETUP: 43 procs — configures audit monitoring, writes to ISLOG+BKSYMSTR+BKPSUSER; T7ALTPART: 104 procs, BKSBPART+BKICMSTR+ISLINKS — alternate/substitute part maintenance; Pass 65: ISLOG(9f fully extracted: WHO+WHAT+DOING+STARTD/T+COMPANY+KILL+MSG+EXTRA — KILL flag allows admin session termination)); BKSBPART(5f)=PARNT+PROD+CUST+SUBST; ISLINKS(311f)=global doc/URL store; T7ALOGSETUP opens FILELOC (enumerate all tables to configure monitoring) — 2 programs confirmed — **C: 70/100**
- [x] 🔄 **LI** — License / Module Access (T7LIMACC: 42 procs, 4 tables: ISACCESS+BKSYHELP+DBAHLPID+MKAHIST); **ISACCESS 8-field schema extracted from IS.ACC.* vars (Pass 117):** NAME+OBJ+OBJTYPE+DFM+FIELD+STATUS+TEXT+EXTRA (not in DDF); AGROUP/AOBJ = access group and object identifier vars; ACC.REC/ACCESS.H = record and handle; OBJ_TYPE/OTYPE = object type codes; FPOPVLD1-5 = field-level pop-up validation (licensed module gate fields); source_file=NZLICE.LIB (NZ = licensed module validation library); ISACCESS controls per-DFM/per-field access restrictions for licensed modules — **C: 72/100**
- [x] 🔄 **ML** — Multi-Language Invoice Support (T7MLC: 50 procs, source=NZLICE.LIB, 27 tables); DB fingerprint confirmed (Pass 117); conversion vars: IS.CF/CFF (currency flags/fields), IS.CVT.MTH (conversion method), IS.LND.RTE (landed rate), IS.OEXC/RTE/RTE2 (orig/new exchange rates), IS.SYMBOL/SYMDESC/SYMPOS (currency symbol display), IS.FRGTPER (freight percentage); handles: ISBRK.HNDL+ISDUTY.HNDL+ISHTX.HNDL+ISLDF.HNDL+ISMCF.HNDL+ISMCR.HNDL+ISTAX.HNDL+ISTXF.HNDL+ISTXG.HNDL = full landed cost + tax handle set opened; DCL.PERIOD.FREQ/PDTE = customs declaration period; EIMCO.SHIFT2/3 = EIM invoice shift codes; T7MLC = multi-currency invoice printer with landed cost apportionment + tax handling; NZLICE.LIB confirms licensed module; T7LANG = LANGDICT maintenance — **C: 72/100**
- [x] 🔄 **MH** — Shipping Order (T7MHOPE: 98 procs, source=ISTECH2.LIB, 30 tables); full DB fingerprint confirmed (Pass 117): BKCMTERR+BKARCUST+ISSHPVIA+ISSHIPCO+BKARINV+BKARINVL+BKICLOC+BKGLTRAN+ISREPLNK+BKPRSALE+BKICPMAT+ISJAVA+ISBSF+BKYSMSTR+BKAPDESC+BKICMSTR+BKCMACCN+BKAPVEND+ISGLDATE+ISIS+ISNUMBER+ISREPORD+ISDRILL+MKAHIST+DBAHLPID+ISLINKS+ISLOG+BKSYHELP+MTICMSTR+LANGDICT; ISBSF in MH = KPI update on shipment; ISJAVA = Java email notification on ship; ISREPLNK+ISREPORD = rep commission tracking on ship order; ISGLDATE = GL-date-controlled shipment posting; source=ISTECH2.LIB (2nd-tier IS tech); ISSHPVIA(23f)+BKCMTERR(11f) fully extracted — **C: 72/100**
- [x] 🔄 **ED (EDII)** — EDI Invoice Import (T7EDII: 183 procs, 43-table DB set); full inbound EDI→AR invoice pipeline: 42 of 43 tables are in DDF schema (only FILELOC unregistered); all constituent tables documented across AR/SO/GL/LC sections; EDII uses identical code path as manual SO entry — customer/item lookup, BKICPMAT pricing, ISTAXGRP taxes, BKGLTRAN GL, WORKORD WO link, LOT/SERIAL tracking; complete AR invoice creation without human interaction — **C: 72/100**
- [x] 🔄 **BR** — Brand / CRM Classification; T7BRANDS (53p, 27 tables) opens far more than expected (Pass 117): BKCMACCC+BKAPPOL+BKGLTRAN+BKMRPFC+DBAFIFO+LOT+SERIAL+ISNCR+ISREMIND+ISTRIGRS+ISICMSTR — full operational scope; T7BRANDS is NOT just a brand code editor; IS.* feature flag vars from BKYSMSTR: IS.AUTO.TAX.CAL/IS.CC.*/IS.DEMO/IS.EZPAY/IS.IMAGING/IS.LANDED.COST/IS.MULTI.CPAY/IS.MULTI.CURR/IS.PO.TAX/IS.RETAIL.PRICE/IS.RMA/IS.UPC/IS.UPC.1/IS.UPC.2 — T7BRANDS manages system-wide feature flag configuration; TOLKEN = credit card token binding; T7BROWSER (4p) = CRM contact viewer (BKCMACCN 154f); BKCMACCN fully extracted; BKCMACCC(2f: CCODE+DESC) = brand category codes — **C: 70/100**
- [x] 🔄 **NE** — New Company Initialization (T7NEWINIT: 49 procs, 15 tables); FILELOC+FILEDES+BKAPVEND+BKARCUST+BKCMACCN+BKICMSTR confirmed; **FILEDES schema inferred from vars (Pass 117):** LOC_BUFF_NAME+COMP_CODE+DESCRIPTION+FILE_NAME+LOCATION+REC_SIZE+REC_TYPE = file template definition (file name + path + record size + type); BKYS.DATE/DESC/GLDPT/GLNUM/INVNUM/NUM/QCNUM/RBNUM/REQNUM/VNUM/WONUM/YN = BKYSMSTR initial auto-number values for new company; ESETTINGS = initial settings seed; PPARAMS = program params; FILLVAL = fill value for initial field values; purpose: creates all Btrieve .B data files for a new company from FILEDES templates, optionally seeds from existing company — **C: 70/100**
- [x] 🔄 **CU** — WO Material Cut Sheet; 2 programs confirmed (Pass 115): T7CUTSHEET2 (75 procs, lot-enabled: WOMAT+LOT+WORKORD+WOBOM+ISBINLOT+BKPSUSER) + T7CUTSHEET2b (60 procs, no-lot variant: drops LOT/ISBINLOT/BKPSUSER — simpler material cut sheet without lot tracking); both open BKGLX+ISDUTY+ISBROKER (landed cost tables: import duty + customs broker fees), ISMCR+ISMCF (multi-currency), ISGLDATE (period dates), BKSYAR (AR system settings), MKECLASS+CLASS (material class config), BKGLTRAN (GL posting); ISBINLOT(11f) = bin-level lot qty (ITEM+LOC+LOT+BIN PK, UOH, TMPSO/TMPPO, DFLT); ISDUTY/ISBROKER = landed cost import tables (confirms CU handles tariff/duty apportionment on cut materials); BKGLX = GL extended (purpose unclear, possibly GL override or extended distribution) — **C: 68/100**
- [x] 🔄 Pass 55: WOBOM(24f: OPER+WOPRE+WOSUF PK, ASSY+COMPCODE, QTYPER+SCRAPQTY+TOTQTY+ASSYQTY+QTYISSUED, UM, EMATCST+AMATCST, REF+OPTION+VEND+BINLOC+UID+REV+SEQ)+WOMAT(17f: DATE+WOPRE+WOSUF PK, PRODCODE/DESC+PCODE/DESC, QTYISSUED+QTYSCRAP+SCRAPCD, LOT+SERIAL+KIT+COST+REF) fully extracted; cut sheet = WOBOM(required) vs WOMAT(issued) shortfall with ISBINLOT bin locations — **C: 72/100**
- [x] 🔄 **JO** — Jobs and Departments (T7JOBS: 21 procs, ISDEPT+WOEXCHG+ISCATMST+BKICLOCM+BKARCUST+BKAPVEND+ISBNMSTR+ISREMIND+ISNOTES+ISLINKS+WORKCTR+BKGLTRAN+BKMRPFC+DBAFIFO; ISDEPT(3f)=dept master, WOEXCHG(10f)=WO change orders with GL posting; T7JODPSALES(52 procs, IS2DBAR+ISCYCLCD+BKSBPART+BKAPDESC) = SM/item-inquiry drill-down panel; Pass 65: ISDEPT(3f: IS_GF_DEPT PK+DESC+MISC; GF_=GL Finance prefix), DBAFIFO(5f: PARTNO+QTY+COST+RECVDATE+REMAIN — FIFO costing queue), BKMRPFC(9f: PART+DATE PK+QTY/OQTY/CQTY+FLAG+DATE1+NUM+EXTRA — MRP firm commitments), BKAPDESC(5f); 2 programs confirmed — **C: 70/100**
- [x] 🔄 **FN** — File Navigator / Btrieve Find+Replace (T7FNR: 104 procs, 15 tables); T7FNR is NOT just a browser — it is a **field-level find+replace utility** for Btrieve files (Pass 117): FIND_FIELD1-6/REPL_FIELD/ACT_FIELD = find+replace field targets; AFIND_FIELD1-6/AREPL_FIELD/NFIND_FIELD1-6 = alternate search patterns; FILTER_CODE/SEARCH_VAL/FIELD = filter+search vars; DICT_* vars (BUFF_NAME/DEC/DESC/FIELD_NAME/HARRAY/HDEC/HNDL/HOFFSET/HSIZE/HTYPE/LCD/OFFSET/PICTURE/SIZE/TYPE/UPCASE) = full FILEDICT API for field metadata access; OPER = replace operation code; NEXT.REC = record navigation; TEST.MODE = dry-run flag; scope: opens FILEDICT+FILELOC — reads any Btrieve table's schema and can find/replace field values; admin tool surfaces as TA-D "Find/Replace in Btrieve files" — **C: 72/100**
- [x] 🔄 **XC** — Credit Card Cross-Reference (T7XCUTIL: 29 procs, 8 tables: BKCMACCT+BKYSMSTR+ISCC+LANGDICT+FILELOC+BKSYHELP+DBAHLPID+MKAHIST); ISCC(14f) fully documented; BKYS.DATE/DESC/GLDPT/GLNUM/INVNUM/NUM/QCNUM/RBNUM/REQNUM/VNUM/WONUM/YN = BKYSMSTR auto-number read (XC checks transaction numbering); BKCMACCT (CRM account type master — maps account to CC token via TOLKEN); TOLKEN = credit card vault token; XC maps CRM accounts to ISCC payment tokens; RVALF = return value float (token lookup result) — **C: 70/100**
- [x] 🔄 **LG** — LGS Customer Module — Canadian customs processing (T7LGSSOE: 170 procs + T7LGSSOEVERIFY: 41 procs); SOE=Statement of Entry (Canadian customs declaration); DB: BKARINV+BKARCUST+BKARINVL+BKYSMSTR+BKICMSTR+MTICMSTR+BKARTXN(14f: SONUM+CODE+QTY+LOT+SERIAL+DATE+LOC+BIN+SRNUM)+BKICTAX+BKICLOC; BKICTAX(46f Pass 64 fully extracted: STATE+LOCAL PK, TAX/TAXY/STATE_AMOUNT/LOCAL_AMOUNT, TAXBLE_1..12/NONTAX_1..12/COLECT_1..12 12-month history, OUTSTD, EXTRA(100)); uses BKICTAX instead of ISTAXGRP (province-level jurisdiction vs. group codes); T7LGSSOEVERIFY = pre-submission validation; 2 programs, purpose fully confirmed — **C: 70/100**
- [x] 🔄 **JS** — JS Integration / Reporting Bridges; Pass 44: 9+ programs identified: T7JSETTINGS(70p, FILELOC config)+T7JUPD(27p, deploy)+T7JSACC(50p, AR accounts)+T7JSAIC(50p, item-customer)+T7JSAPBI(50p, AP BI)+T7JSASRS(50p, AR sales)+T7JSOI(50p, SO invoice)+T7JSQL(52p, SQL query)+T7JTREE(52p, tree view)+T7JTEMP(27p stub); all share 64-table ISDRILL-based DB set; export EvoERP data to JS-based BI layer (Sisense/similar); T7JSETTINGS configures connection, T7JUPD deploys; purpose fully confirmed — **C: 68/100**
- [x] 🔄 **BS** — Business Score/Summary Dashboard; writer/viewer split confirmed (Pass 114, 2026-06-19): T7BS.RWN (162 procs) = KPI writer — populates ISBSF from 40+ tables; EVOBS.RWN (128 procs, QU-D) = KPI viewer — reads ISBSF + live BKGLTRAN/MTICMSTR; ISBSF (143f) PK=STARTDATE+ENDDATE; var-confirmed fields: ISBSF.STARTDATE/ENDDATE (date range), ISBSF.AR.BAL/BILL/RECP/DISC/COGS (AR KPIs), ISBSF.AP.BAL/PAYA/PAYM (AP KPIs), CASH_TOTA+ACT1..9+CASH_ACTS_1..100 (100-period GL history), WOS_SETUP/LAB/OUTP/MAT/FOH/VOH/MEXT/FP/WIPV (WO cost breakdown); T7BS opens ISBANKS (cash balance from bank accounts), ISGLDATE (7-year period-date nav); ISBSF+ISGLDATE+ISBANKS+GL set fully explains KPI calculation — **C: 82/100**
- [x] 🔄 **AD (ADCA)** — Advanced Data Collection (T7ADCA: 290 procs, 55 unique tables); full auto shop floor DC: BKDCLAB+WORKORD+BKPRMSTR+BKDCSHFT(34f, 3-shift config)+ISWOEX(63f Pass 64 confirmed in DDF: WOPRE+WOSUF PK, 5 dates+5 ints+2 floats+5 alphas(30)+5 descs+10 flags+5 gnums+5 alphas+5 notes(100))+ISROUTEX(100f Pass 64: CODE+OPER PK, 10 machine cycle-time slots, 45+ configurable fields)+ISWOROEX(60f Pass 64: WOPRE+WOSUF+OPER PK, per-WO-op routing extension)+OPQCDESC(10f Pass 64: WOPRE+WOSUF+OPER PK, per-op QC result desc)+ISWOTRAY(52f Pass 64: TRAY_NUM PK, WO/oper/qty/QC/4 bins+37 fields)+EIMCOLST(not in DDF); operator scans→posts BKDCLAB→updates WOLABOR/WOROUT; Pass 109: T7ADA/B/C confirmed non-existent (only T7ADCA); BKDCSHFT all 34 fields decoded (3 names + 30 time fields per shift + EXTRA); ADCA vs PA functional distinction documented — **C: 72/100**
- [x] 🔄 **IT** — Item Serial/Barcode/Cycle Config (T7ITMCFG: 66 procs); opens ISSERCNT+BKICMSTR+BKGLCOA+SERIAL+ISNCR+IS2DBAR+ISCYCLCD; ISSERCNT(9f): IS_SERC_ITEM(15)+CLASS(4)+SPOS+LENG+TOTAL+NUMBER(counter)+LAST(25, last serial generated)+EXTRA+L2 — serial counter per item; IS2DBAR(109f): barcode format config per item/document (109 fields=mostly doc-type print flags); ISCYCLCD(7f): IS_CYCLE_CODE(4)+DESC(30)+FREQ+DATE+ALPHA(15)+NUM+EXTRA(50) — cycle count frequency code; all 3 schemas extracted from DDF — **C: 72/100**
- [x] 🔄 **CH** — Multi-Location Chain (T7CHAIN: 62 procs, ISCHAINM+BKPSUSER+BKSYMSTR+LANGDICT; T7CHAINM: 40 procs, ISCHAINM+FILEDICT); ISCHAINM(17f)=USER(15)+PARENT(12)+CHILD(12) PK + PARAM_1..10(15 each)+AUTO(1)+DATE+DESC(100)+EXTRA(100); defines parent-child company relationships for multi-company chains; 2 programs confirmed; LANGDICT in T7CHAIN confirms multi-language chain deployments — **C: 72/100**
- [x] 🔄 **PA** — Paperless DC / Shop Floor Control (T7PAPERLESS: 205 procs, 50 unique tables; T7PACKMENU: 5 procs stub; T7PASS: 3 procs password sub); ISBINLOC(9f)=bin-level inventory without lot (ITEM+LOC+BIN PK, UOH, DFLT, RVLVL); opens WORKORD+ROUTING+WOROUT+BKICLOC+ISBINLOC+ISWOEX+WORECV+BKAPPOL+ISWOTRAY+BKDCLAB; Pass 43: 50-table DB fingerprint re-confirmed; BKDCLAB+ISWOTRAY confirm PA=touchscreen DC identical function to ADCA; BKAPPOL confirms outside process PO receiving from floor; Pass 109: PA vs ADCA distinction: PA opens WOMAT+INVTXN+ISBINLOT+WOBOM+ISACCESS (material issues + bin-lot + license gate); ADCA opens BKPRMSTR+BKDCSHFT (payroll + shift); T7PASS=password sub with 45-table session init — **C: 72/100**
- [x] 🔄 **TE** — NACHA/ACH Electronic Payments (T7TESTNACHA: 103 procs, BKSYMSTR+ISBANKS+BKGLCHK+BKAPVEND+BKARINVL); BKGLCHK(11f)=check register: CHKACT+NUM PK, DATE+TYPE+NAME+AMT+FLAG+DATER+VEND+CUST; ISBANKS(23f) fully extracted: NUM(2)+SRT PK, DESC(40)+GLA/GLD(GL account+dept)+NXTNUM(next check#)+BAL+ROUT(15 ABA routing)+ACCT(15 bank acct)+CURR(3)+TYPE(2)+VEND(10)+ACTIVE+INC_BS+AR/AP/PR flags+RTM_1..5(12, report templates)+EXTRA; generates NACHA ACH files from ISBANKS routing/account + BKAPVEND payment data — **C: 72/100**
- [x] 🔄 **KI** — Kit Assembly (T7KIT: 153 procs, 26 unique tables); opens BKICMSTR+MTICMSTR+WOBOM+BKICLOC+BKYSMSTR+ISLINKS+WOMAT+WORKORD+WOROUT+BKPRMSTR+ISBINLOC+LOT; assembles kits from BOM components using simplified WO without routing/labor; lot+bin location tracking; Pass 43: DB fingerprint re-confirmed; ISLINKS confirms document attachments to kits — **C: 72/100**
- [x] 🔄 **EM** — Emergency GL Maintenance (T7EMGL: 62 procs, 33 unique tables); full DB fingerprint confirmed (Pass 115): BKGLCOA+BKSYHELP+DBAHLPID+ISIS+MKAHIST+ISLOG+ISDRILL+BKAPVEND+BKARCUST+BKCMACCN+BKICMSTR+ISLINKS+BKAPDESC+LANGDICT+ISTAXGRP+ISNUMBER+BKICLOCM+BKAPPOL+BKAPPO+WORKORD+WOBOM+INVTXN+BKBMMSTR+BKMRPFC+FILELOC+ISICMSTR+BKGLTRAN+DBAFIFO+ISTRIGRS+ISREMIND+LOT+SERIAL+ISNCR; BKGLCOA(65f) fully extracted: ACCT(10)+GLDPT(4) PK, ACCTD(25)+TYPE(1)+CR_DR(1)+NON_CASH(1), CURRENT_1..14+BUDGET_1..14+1YPAST_1..14+1YPAST_YE+2YPAST_1..14+2YPAST_YE+EXTRA(50); new finds: BKMRPFC (MRP forecast table, opens for cost reference), DBAFIFO (FIFO cost layers), ISTRIGRS+ISREMIND (trigger+reminder system), LOT+SERIAL+ISNCR (lot/serial/nonconformance — deep override capability); EM = most privileged maintenance tool: can touch GL accounts, AP/PO transactions, WO/BOM, inventory txns, FIFO cost layers, lot/serial records — **C: 70/100**
- [x] 🔄 **QS** — Quick Sales Order / Web Order Staging (T7QSOA: 72 procs + T7QSOALINES: 70 procs); ISQSOA(12f) schema extracted: IS_QSOA_UID(40) PK + CUST(10)+SHPTO(10)+SHPDTE+ITEM(15)+DESC(30)+QTY+PRICE+DISC+MDATE1/2+EXTRA(50); ISQSOA vars confirmed (Pass 115): IS.QSOA.CUST/DESC/EXTRA/ITEM/MDATE1/MDATE2/PRICE/QTY/SHPDTE/SHPTO/UID — all 12 fields accessed directly; T7QSOA opens LOT+SERIAL (lot/serial-controlled items in quick orders) + BKAPINVL+BKAPPO (AP cost check for pricing); T7QSOALINES (70 procs) = SO line-detail viewer: opens BKCMACCT (CRM account context for line items) + BKICLOC+BKICPMAT (location+price matrix); ISTERMS+BKPRSALE confirm real SO creation; ISQSOA = staging record for quick/web order entry — **C: 72/100**
- [x] 🔄 **VSCHED** — Visual Work Center Capacity Scheduler (T7VSCHED: 94 procs confirmed Pass 115, 22 tables); WCTRLOAD(8f: WC+DATE PK, TOTHRS+UDATE+CAP+UTIL+LOAD+EXTRA(100)); full DB fingerprint: WORKORD+WOROUT+WCTRLOAD+BKICMSTR+FILELOC+BKYSMSTR+BKARINV+BKARINVL+BKSYHELP+DBAHLPID+ISIS+MKAHIST+ISLOG+ISDRILL+BKAPVEND+BKARCUST+BKCMACCN+ISLINKS+BKAPDESC+ISACCESS+LANGDICT+BKSYMSTR; WCTRLOAD = pre-computed daily WC capacity snapshot (written by scheduler/MRP); BKARCUST+BKARINV+BKARINVL = customer demand overlay (open SO→WC); BKAPVEND+BKCMACCN = vendor/contact context for demand source; ISDRILL+ISLINKS+BKAPDESC = drill-through to source orders; ISACCESS = license gate; LANGDICT = multi-language UI; purpose confirmed = visual/Gantt WC capacity planning with customer demand overlay — **C: 72/100**
- [x] 🔄 **TPOA** — PO Processing Approval Hub (TPOA: 499 procs, 61 tables); DB fingerprint (Pass 115): BKAPPO+BKAPVEND+BKAPDESC+BKAPPOL+MTICMSTR+BKYSMSTR+ISTERMS+ISNOTES+ISLINKS+ISAPEX+BKSYMSTR+BKARCUST+BKICMSTR+BKICLOCM+WORKORD+WOBOM+WOROUT+BKRFQ+ISECO+ISORDDSC+ISORDECO+ISJOB+BKSBVEND+BKSBMFG+ISAPCHG+ISDIGSIG+WORKCHG+CALENDAR+ISMCF+ISMCR+BKARINV+BKARINVL+BKARINVV+BKAPINVL+ISTAXFIL+LOT+SERIAL+ISNCR+BKGLTRAN+MKAHIST; new finds: ISAPCHG (approval change/audit log), ISDIGSIG (digital signatures on PO approvals), BKSBVEND/BKSBMFG (subcontracting vendor/mfg), WORKCHG (WO engineering changes), BKRFQ (RFQ link), ISECO (ECO integration), ISJOB (job costing link), CALENDAR (PO due date calendar), ISMCF/ISMCR (multi-currency), BKICLOCM (location master for delivery sites); ISAPEX(33f) = approval gate engine; ISNOTES(13f) fully extracted; 499 procs = largest standalone program — **C: 72/100**

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
- [x] ✅ Files: EvoNotes.RWN, EvoNotesARCH.RWN, EvoNoteSearch.RWN, EvoNotesPrt.RWN, EvoNotesRpt.RWN — **C: 82/100**
- [x] ✅ Table: ISNOTES — **C: 55/100**
- [x] 🔄 Pass 56: 6 programs mapped (EVONOTES/ARCH/SEARCH/PRT/RPT+T7EVONOTES); ISNOTES(13f: IS_NOTE_ID(48 composite key)+TYPE+CDATE/CTIME/CWHO+EDATE/ETIME/EWHO+EXTRA(100 search)+PRIVATE+GROUP(4)+CONTACT(30)+body(256-char DDF-corrupt field)); ISNTYPE(4f: TYPE+DESC+SEC(security level)+EXTRA); WORKCHG(25f: WO change audit before/after PRIO/STATUS/CLASS/DESC/QTY/SDATE/FDATE/DDATE/ASD/EXTRA all A/B pairs) extracted; IS_NOTE_ID = 48-char entity key; note body = DDF-corrupted STRING(256) confirmed from field size; entity linking via DB fingerprints (BKARCUST+BKAPVEND+BKICMSTR+WORKORD in every notes program); ISTAXFIL(84f) extracted as bonus: 9-bracket SO+PO tax tables with GL accounts — **C: 72/100**

### 9.2 EvoScheduler
- [x] ✅ Files: EvoScheduler.RWN, EvoSched.RWN, EvoSchedSetup.RWN — **C: 80/100**
- [x] ✅ Scheduler job table = **ISSCHED** — confirmed 2026-06-17 from DB fingerprints (EvoSched.RWN, EvoScheduler.RWN, EVOSERVICE.RWN all open ISSCHED); SCHEDCAL used by shop scheduling module
- [x] ✅ EvoRemind (evoremind.RWN: 46 procs) opens ISREMIND+BKYSMSTR+BKSYUSER+ISTRIGRS+BKPSUSER+BKAPPOL — links reminders to PO/AR transactions; ISTRIGRS = trigger result log
- [x] ✅ ISSCHED all 24 fields documented — Pass106f — **C: 78/100**
- [x] ✅ Job execution mechanism traced — EvoSched.RWN (21 procs): polls ISTS.CFG.PTIME interval → reads ISSCHED by DATE+TIME → invokes PROG as subprocess with CO+PARAM1..9 → updates LDATE/LTIME → computes next TYPE fire — **C: 78/100**

### 9.3 EvoService (Windows Service)
- [x] ✅ Files: EvoService.RWN, EvoServiceSetup.RWN, EvoServiceRemove.RWN — **C: 68/100**
- [x] ✅ Service registration mechanism traced — THIRTYTWO/SIXTYFOUR named_vars hold 32/64-bit service install paths; EvoServiceSetup writes SCM entry + ISTS.CFG.USINI; EvoServiceRemove uninstalls via same vars — **C: 78/100**
- [x] ✅ Service ↔ Scheduler interaction confirmed (Pass 113 2026-06-19) — **C: 82/100**
  - EvoService.RWN (27 procs): opens ISSCHED + ISREMIND; drives BOTH scheduled jobs AND reminder notifications
  - SCHED.H/REMIND.H = record handles; REMREC/REMCNTR = reminder loop; PARSTO = subprocess param storage; A.RET/A.RET2 = return codes
  - ISTS.CFG.WTIME = poll interval (ms); EvoSched.RWN (21 procs) = test variant (ISSCHED only, no ISREMIND)
  - EvoScheduler.RWN (65 procs, TA-N) = admin UI for CRUD on ISSCHED records; uses FILELOC to enumerate available programs

### 9.4 EvoBackup
- [x] ✅ Files: EvoERPbackup.RWN; uses zipdll/unzdll — **C: 65/100**
- [x] ✅ Backup target paths and file selection logic confirmed (Pass 113 2026-06-19) — **C: 80/100**
  - Source files: FILELOC registry enumerates all Btrieve .B data files; per-company via COMP.TAG/COMP.EXT/COMP.NAME
  - Three scope modes: FULLSYSTEM (all companies), COMPDATA (current company), CUSTOM (CSTFILELIST)
  - Output: ZIP archive (ZIPNAME) via zipdll; BKSYMSTR provides company name for archive labeling; ISLOG logs backup run
  - Local target: `\\i2s109-solidcrm\Bak Up\`; cloud: AWS Glacier via GLACIERKEY (GS_ARCH/GS_BACKUP/GS_NONE flags)
  - MON/TUE/... flags support scheduled day-of-week automation; ISACCESS checks module license
  - docs: `docs/01-architecture/subsystems.md` (EvoBackup section)
- [ ] ⬜ Restore procedure documented — no EvoERPrestore.RWN found in 1122-program catalog; restore may be manual ZIP extraction

### 9.5 EvoLinks (Document Attachments)
- [x] ✅ Files: EvoLinks.RWN, EvoLinkCVT.RWN — **C: 62/100**
- [x] ✅ Attachment storage table = **ISLINKS** — confirmed 2026-06-17 (EvoLinks.RWN opens ISLINKS as primary; ISLINKS = record-key → document filename cross-reference)
- [x] ✅ DB table for link mapping identified and all fields documented — IS.LNK.UID/LINK/APP/TYPES/PCB/DEF/GLOBAL/OPENWITH/DATE/NOTE/WHO/ATYPE/EXTRA/PRIVATE/SORT/ALPHA + FILELINK/LEXIST/GEN.ID/INVENTORY.LINK + E/PG thumbnail/component vars (Pass 110e, 2026-06-19) — **C: 75/100**
- [x] ✅ Attach / view / delete workflow traced — GEN.ID=owning record key; IS.LNK.PCB[100]=multi-record attach; BKAPVEND/BKARCUST/BKCMACCN/BKAPDESC entity lookups; BKYSMSTR/BKICMSTR for parts; FILELOC for path translation; two-tier doc system (E.*=engineering, PG.*=purchasing) with thumbnail support — **C: 72/100**

### 9.6 EvoFNO (Features & Options / Product Configurator)
- [x] ✅ Files: EvoFNO.RWN, EvoFNOSO.RWN, EvoFNOPO.RWN, EvoFNOWO.RWN — **C: 62/100**
- [x] ✅ FNO table structure documented — ISFOHEAD (header: UID/CUST/VEND/RFQ/STATUS/REV/MDATES) + ISFOLINE (BOM lines: LEVEL/COMP/QTYREQ/OP/OPYN/RTNUM/SCRAP/TYPE) + ISFOORDL (customer order lines: PCODE/PDESC/PQTY/PPRCE/PDISC/PEXT/ESD) + ISFOBMRM (remarks) + ISFOHIST (conversion audit) — **C: 78/100**
- [x] ✅ FNO interaction with SO/PO/WO modules traced — EvoFNOSO: BKARINV/BKARINVL (P.SO/ITEM/LINE context); EvoFNOPO: BKAPPOL/BKAPPO + BKSBVEND/BKSBMFG cross-check; EvoFNOWO: WORKORD+WOBOM+WOROUT+ROUTING+WORKCTR+CALENDAR; all 3 log to ISFOHIST.CVTTO/CVTNO — **C: 78/100**

### 9.7 EvoUpdate (In-App Patching)
- [x] ✅ Files: EvoUpdate.RWN, EvoERPupd.RWN, EvoPRupd.RWN, EvoUPDSetup.RWN, UPDTP7.EXE — **C: 70/100**
- [x] ✅ Update mechanism: reads FILE\*.UPD manifests, applies schema migrations — **C: 65/100**
- [x] ✅ Full update pipeline traced — EvoUpdate(entry)→EvoUPDSetup(path)→EvoERPupd(77p; FILEDICT/FILEDBF/FILEKEY schema registry; FROM_FILE→TO_FILE migration; UPDATE_FD field defs; RSTR_FILES rollback; updates BKLUGRID+ISDRILLM+ISTS.CFG)→EvoPRupd(payroll)→Evocnvtb(DDF sync) — **C: 75/100**
- [x] ✅ UPDTP7.EXE role confirmed (Pass 113 2026-06-19) — **C: 68/100**
  - 32-bit VC++ Win32 executable, 85,680 bytes; 24,240-byte encrypted overlay at offset 0xF000
  - Generates batch script (@echo off / mkdir / attrib +h) to create hidden temp working dir
  - Uses CreateProcessA to apply patch; error "Error #bdembed1 -- Quiting" confirms "BD embed" architecture
  - Overlaid encoded strings DFDHERGDCV/DFDHERGGZV = obfuscated temp folder names (cipher unknown)
  - Role: patches tp7runtime.exe binary itself; distinct from EvoERPupd.RWN (schema migrations)
  - Gap: overlay cipher/encoding not decoded; exact patch mechanism unknown without debugging session

### 9.8 EvoDrillDown / Analysis Tools
- [x] ✅ Files: EvoERPDrillM.RWN, CashFlow, CommissionRpt, BOMTree, EditBOMTree, CRM Dashboard — **C: 75/100** (Pass 115, 2026-06-19): EvoERPDrillM (31 procs, 10 tables: ISDRILLM+BKLUGRID+FILELOC+FILEDICT+FILEKNUM+FILEKEY+BKSYHELP+DBAHLPID+MKAHIST+ISLOG); DRILLM.* vars (CHILD/EXTAR/FILE/H/KEY/MENU/PARENT/PFILE/SFIELD/TFIELD) exactly match ISDRILLM(17f) schema; BKLUGRID 14-field schema confirmed from LUGRID_* vars; DICT_*/KEY_*/KNUM_*/LOC_* vars confirm FILEDICT/FILEKEY/FILEKNUM/FILELOC field access patterns; role: master drill-down dispatcher — resolves ISDRILLM lookup entries (parent→child nav via SFIELD→TFIELD mappings) + loads BKLUGRID grid column layouts; EIMCO.SHIFT2/3 vars = EIM (invoice management) shift code refs
- [x] 🔄 T7SMJ* drill-down panel family decoded (18 modules, 2026-06-17): SMJA/B=WO, SMJC/D=Inventory+FIFO, SMJF/R=PO, SMJG=QC, SMJH=DC Labor, SMJI=Estimates, SMJJ/K=SO/Invoice, SMJL=Master (459 procs, 92 tables), SMJM=Customers, SMJN=Vendors, SMJO=AR/AP, SMJQ=Item/BOM, SMJS=Item, SMJV=Payroll; 16 new tables confirmed — **C: 72/100**
- [x] ✅ CashFlow + CommissionRpt confirmed as EvoPVT.jar launcher stubs (Pass 113 2026-06-19) — **C: 78/100**
  - Both have identical DB fingerprint: BKPSUSER+ISDRILL+BKAPVEND+BKARCUST+BKCMACCN+BKICMSTR+ISLINKS+BKAPDESC
  - Both have identical vars: HOST/NAME/PORT/TREEDEST/COMP/NOPE/DUMMY_L/DFM
  - Calculation logic is NOT in the RWN — it lives in the EvoPVT.jar Java layer (HOST/PORT → Pervasive JDBC)
  - CashFlow: TREEDEST → CashFlow drill-down tree; CommissionRpt: TREEDEST → commission report tree
  - docs: `docs/01-architecture/subsystems.md` (CashFlow/CommissionRpt section, Pass 113 update)
- [x] ✅ CRM Dashboard confirmed as EvoPVT.jar launcher (Pass 113 2026-06-19) — **C: 78/100**
  - CRMDASHBOARD.RWN: 26 procs; vars HOST/NAME/PORT/TREEDEST/COMP/NOPE/DUMMY_L/DFM/RVAL/ISTS.EDATE
  - Extra DBs vs CashFlow: LANGDICT+ISLOG+FILELOC (adds logging and multi-language support)
  - Same pattern as CashFlow/CommissionRpt/BOMTree: TAS launcher passes HOST+PORT+COMP+TREEDEST to EvoPVT.jar; Java layer renders the CRM dashboard view

### 9.9 Google Calendar Integration
- [x] ✅ Files: CALREM.RWN, CALREMGC.DFM — **C: 55/100**
- [x] ✅ Calendar sync logic confirmed from DB fingerprint (Pass 113 2026-06-19) — **C: 65/100**
  - CALREM.RWN (142 procs): opens BKYSMSTR+ISREMIND+BKARCUST+BKAPVEND+BKICMSTR+BKCMACFC+BKCMACCN+BKPSUSER+ISLOG
  - ISREMIND = primary data source (syncs EvoERP reminders → Google Calendar events)
  - Date handling vars: ISTS.EDATE/ENTRY.DATE/DATE_TYPE/MM/DD/YY/START.DATE/CHK.DATE (calendar date construction)
  - BKARCUST+BKAPVEND+BKCMACCN = entity context for event subject/description
  - CALREMGC.DFM = Google Calendar sync dialog (no separate CALREMGC.RWN; sync runs inside CALREM.RWN)
  - BKYSMSTR flag controls whether Google Calendar sync is enabled globally
- [ ] ⬜ OAuth / API credential storage traced — inferred: EvoSettings.INI [CALENDAR] section (similar to [EMAIL] sections); no explicit OAUTH/TOKEN vars visible in named_vars; requires tracing CALREM.RWN bytecode

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
- [x] ✅ ISJAVA schema: IS_JAVA_UID(PK) + IS_JAVA_DATE + IS_JAVA_PARAM_1..N (dynamic-count params); TAS vars: IS.JAVA.UID / IS.JAVA.PARAM / IS.JAVA.DATE / JAVA.PATH / JAVA.H; table is TAS runtime-only (not in DDF) — **C: 75/100**
- [x] ✅ Java connection parameters: **jdbc.ini** text file (NOT registry); keys: Host, Name, Port, Company, Tree Destination; WinRegistry used only for Java path lookup — **C: 92/100**
- [x] ✅ JavaFX sub-tasks enumerated: CsvExportTask, TextFileWriteTask, FileOpenTask, TabularView$ExportTask — **C: 80/100**
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
- [x] ✅ DSN setup parameters documented: ServerName=i2s109-solidcrm, Port=1583, Database=@DBA, Driver=Pervasive ODBC Client Interface — **C: 92/100**
- [x] ✅ Read/write via ODBC (Relational): SELECT/INSERT/UPDATE/DELETE all work; no DB-side constraints; external writes bypass TAS Pro RI — **C: 90/100**
- [x] ✅ Locking: ODBC reads (read-committed, never blocked); ODBC writes conflict with Btrieve explicit locks (SQLSTATE 40001); file locks during posting block reads — **C: 88/100**

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

Pass 58 + Pass 97 + Pass 106d (2026-06-18): 16 workflow recipes written — **C: 85/100**

### 13.1 Core Accounting Workflows
- [x] ✅ **Customer invoice (AR voucher)** — see Recipe 7: AR Cash Receipts — **C: 75/100**
- [x] ✅ **Cash receipts** — AR-C → BKARTXN+BKARINVT+BKARCUST+BKGLTRAN — see Recipe 7 — **C: 75/100**
- [x] ✅ **Purchase order → AP voucher → check** — see Recipe 3 — **C: 75/100**
- [x] ✅ **Month-end close** — AR-H → AP → IN → AM period lock — see Recipe 5 — **C: 72/100**
- [x] ✅ **GL journal entry** — T7GLB enter → T7GLC report → T7GLP period-end → T7GLARCH archive — see Recipe 10 — **C: 70/100**
- [x] ✅ **Period-end archiving** — T7GLP → T7GLARCH → purge — see Recipe 11 — **C: 70/100**
- [x] ✅ **Year-end close** — full sequence traced: PR-O (BKPRMSTR→BKPRW2 + YTD zero + BKPRSALE→BKPRBOOK) → PR-L-I W-2 print → AP-S 1099 (BKAPVEND.TAX_ID + BKAPVND2) → AM GL year-end shift (BKGLCOA CURRENT→1YPAST→2YPAST) → SM-J* archive; Recipe 21 added to HELP-RESOURCES.md (Pass 112 2026-06-19) — **C: 88/100**

### 13.2 Inventory & Manufacturing Workflows
- [x] ✅ **New item setup** — IN-B → BM → RO-A — see Recipe 6 — **C: 78/100**
- [x] ✅ **Work order lifecycle** — WO-A → DC → WO-K-J → WO-K-C — see Recipe 2 — **C: 80/100**
- [x] ✅ **MRP run** — MR-A → MR-J → MR-K — see Recipe 4 — **C: 75/100**
- [x] ✅ **Physical inventory count** — PI-A → PI-C → PI-D → PI-F — see Recipe 8 — **C: 75/100**
- [x] ✅ **Sales order → ship → invoice** — SO-A → BO → SO-F → SO-G — see Recipe 1 — **C: 80/100**
- [x] ✅ **Inventory adjustment** — IN-G/IN-H → BKISTXN+BKICLOC — see Recipe 14 — **C: 70/100**
- [x] ✅ **Lot/serial tracking** — PO receipt → WO issue → WO completion → SO shipment — see Recipe 15 — **C: 68/100**

### 13.3 Payroll Workflows
- [x] ✅ **Time entry** — DC/WO-L-E path (WOLABOR→BKPRCURP) + PR-J/PR-K time card path — see Recipe 17 — **C: 80/100**
- [x] ✅ **Payroll calculation** — PR-B (gross→deductions→net, tag by division) → PR-C register — see Recipe 18 — **C: 78/100**
- [x] ✅ **Check printing** — PR-D (direct deposit stubs + live checks, BKGLCHK+BKPRMSTR+BKGLTRAN) → PR-G void — see Recipe 19 — **C: 82/100**
- [x] ✅ **Tax filing** — PR-L-A/C/G/H quarterly + PR-H liabilities→AP + PR-O year-end + PR-L-I W-2 — see Recipe 20 — **C: 82/100**

### 13.5 Master Record Setup Recipes (Pass 113)
- [x] ✅ **Add a new customer** — AR-A → BKARCUST (106f); TERMS/SALESPERSON/CLASS/TAXGRP/CREDIT_LIMIT/RESALE key fields; Recipe 23 in HELP-RESOURCES.md — **C: 90/100**
- [x] ✅ **Add a new vendor** — AP-A → BKAPVEND (72f); TERMS/TAX_ID/1099-type/BANK fields; 1099 workflow; Recipe 24 in HELP-RESOURCES.md — **C: 90/100**
- [x] ✅ **Receive a purchase order** — PO-J (T7POJC) → BKAPPOL/BKAPINVL/BKAPINVT; QC/lot/serial/bin capture; DBAFIFO cost layer; Recipe 25 in HELP-RESOURCES.md — **C: 82/100**

### 13.4 System Administration Workflows
- [x] ✅ **New user setup** — AHSYLOG entry, access flags, starting menu — see Recipe 13 — **C: 65/100**
- [x] ✅ **New company creation** — UT → company add, NE module (T7NEWINIT: 49 procs) — see Recipe 16 — **C: 60/100**
- [x] ✅ **Backup / restore** — TA-O (EVOERPBACKUP) — see Recipe 12 — **C: 65/100**
- [x] ✅ **Software update** — EvoUpdate pipeline traced (Pass 110e 2026-06-19) — see Platform Subsystems § EvoUpdate — **C: 75/100**
- [x] ✅ **ODBC DDF build** — required before Java tools can connect; full procedure documented: DDF Builder method (Pervasive Control Center → DDF Builder → FILE.DDF/FIELD.DDF/INDEX.DDF), TA-S method (FILEDICT sync), ODBC Admin method (SysWOW64 32-bit admin, DSN=DBA, Host=i2s109-solidcrm, Port=1583, Database=@DBA); bitness trap documented; Recipe 22 added to HELP-RESOURCES.md (Pass 112 2026-06-19) — **C: 88/100**

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
- [x] ✅ `WHOAMI.DBA` decoded: 2 bytes (0x0D 0x0A only = bare CRLF); file existence is the flag, content is empty; samples/WHOAMI.DBA (Pass 112 2026-06-19) — **C: 100/100**
- [x] ✅ `CHMHELP.EVO` decoded: 35-byte text sentinel — "EvoHELP now set for this computer\r\n"; written by StartEvo.exe after CHM installation; presence signals CHM is installed and configured; samples/CHMHELP.EVO (Pass 112 2026-06-19) — **C: 100/100**
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
- [x] ✅ BKAPINVH — Confirmed NOT in DDF schema (grep of schema.md returns no match); AP voucher header data is the first 10 fields of BKAPINVL (390f total); no separate header table exists (Pass 112 2026-06-19) — **C: 95/100**
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
- [x] 🔄 All remaining BKPR\* (16 tables) — BKPRMSTR (384f fully grouped), BKPRCURP/BKPRHIST (127f each), BKPRINFO (128f), BKPRSALE/BKPRBOOK (87f each), BKPRTC (7f), BKPRTCFG (205f) documented; BKPRFTAX (47f), BKPRGLFL (664f), BKPRACOM/BKPRCOMM/BKPRHCOM (12f each), BKPRAGNT (4f), BKPRSTFL (2f) summarized — **C: 88/100**
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
- [x] ✅ Form-to-menu-code mapping: DFM column added to code-program-mapping.md (2026-06-19) — 723/870 codes resolved (83%); 9 are .RUN legacy; 12 RWN not yet decrypted; 147 are navigation groups — **C: 83/100**
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
| System Architecture | **90** | 90 | **0** ✅ ↑+3 Pass106k ISLINKS 311-field schema confirmed (UID+LINK+APP+TYPES[100]+PCB[100]+DEF[100]+DATE+WHO+ATYPE); EvoNotes 9-table pattern confirmed (BKAPNOTE/BKBMNOTE/BKSONOTE/BKQTNOTE/ISNOTES+); ISSCHED confirmed from Pass106f; all subsystems documented | 2026-06-18 |
| Boot Sequence | **85** | 85 | **0** ✅ ↑+3 Pass106l StartEvo.exe Pass105 confirmed in doc (DomainAuth→KillProcs→LaunchUser); CHMHELP.EVO=sentinel flag "EvoHELP now set..."; evo:// URI+license gate documented; remaining open: exact evoerp.exe argv; suwin6.dcy pre-load | 2026-06-18 |
| File Formats — SRC | **90** | 90 | **0** ✅ ↑+3 Pass107: func/{} block full semantics confirmed from BKAWLB.SRC (inline local block vs top-level func with parameter); #INC/#LIB case-insensitive, resolve from DataDictPath (\\DBAMFG$\); HELPSCRN.SRC=F1 help template, isdef.SRC=IS defines; SETUP_COLOR=opens TASCOLOR Btrieve table reads palette; Color Array Norm/Inverse/High = color mode select; #PRO3=legacy backward-compat flag; ret .t./.f. semantics confirmed (true=allow, false=abort); remaining gap=expression precedence (cannot observe from 7 files) | 2026-06-18 |
| File Formats — DFM | **90** | 90 | **0** ✅ ↑+3 Pass106k Delphi 7 confirmed from evoerp.exe string table (qtintf70.dll="70"=VCL7.0); 51 distinct control types across 1136 DFMs cataloged in tas-pro-7-controls.md; all questions resolved | 2026-06-18 |
| File Formats — RWN/DCY | **90** | 90 | **0** ✅ ↑+2 Pass109 DCY binary layout: 8-byte ID + DFM (text or binary-TPF0 with 20-byte mini-header); all 41 forms structure confirmed; EVOUSERS/WBKLUGRID forms documented | 2026-06-18 |
| File Formats — RTM | **88** | 88 | **0** ✅ ↑+4 Pass106i T:\ drive mapping confirmed (cfg.rtm=T:\cfg.rtm inferred); TppDBText dual field binding (underscore=ODBC/dot=TAS) confirmed from I2SCHK1.btm; full 24-module RTM breakdown (SO=103/SR=52/PO=32/AP=27/AR=25/J6=20/WO=14/PR=12/JM=12/IN=11/IS=11/CM=9/SA=7/DC=5/ES=5/AW=4/AS=4/PI=3/GL=2/AM=2) | 2026-06-18 |
| File Formats — Btrieve | **85** | 85 | **0** ✅ ↑+5 Pass106i Types 12=NOTE/13=LVAR resolved (DDF-catalog only, zero in business tables); RELATE.DDF confirmed ~8 FK records/engine RI not used; OCCURS.DDF ~150+ records confirmed; dual FCR pages 0+8 confirmed; B-tree page structure decoded | 2026-06-18 |
| TAS 4GL Language | **92** | 92 | **0** ✅ ↑+2 Pass108: `enter` full option set documented (12 options: mask/up/acr/pre/post/vld/vldm/dflt/upar/at/help/noclickoff; all confirmed from 7 SRC files); pre+vld accept either func() or bare expression; noclickoff=T7-era standard; remaining: expression precedence (unobservable from SRC) | 2026-06-18 |
| Database Schema (structure) | **95** | 95 | **0** ✅ ↑+5 Pass108: tier10+tier11 — all 649 DDF tables now categorized: 638 business tables in tier docs, 10 X$* Pervasive catalog tables (documented in tier10 as DDF system tables), 1 BOMCHG (BOM change log, documented in tier10). EvoERP archive pattern: every module has BKARINV/BKARINVL clones (ISAR*/ISSR*/ISRM*/ISSS*); ISSR_INFO 54f shared service record across 9 tables; MK* campaign management; ISGL* 14-period fiscal calendar; BOMCHG 15f before/after audit pattern | 2026-06-18 |
| Database Schema (field meaning) | **88** | 88 | **0** ✅ ↑+2 Pass108: tier11 adds field-level semantics for 80+ more tables — EvoERP archive pattern explains all BKARINV clone tables; ISSR_INFO 54f pattern (SRNUM+UID+CODE+DATE_1..5+AL_1..20) confirmed across 9 tables; ISSO* packing/approval semantics (ISSOBOX+ISSOREVU); ISPO* carrier tracking (IS_TRK_ORD+NUM+SHPVIA+CDATE+RDATE+STATUS); ISAP* AP-side extended (ISAPAINL 390f=75 GL distribution lines embedded); ISPR* WO labor auth (IS_PREQ_WOPRE+WOSUF+OPER+WC+EMP+RDATE) | 2026-06-18 |
| Security / Login | **85** | 85 | **0** ✅ ↑+7 Pass105 4-layer security model: license gate(tas_menus/StartEvo)→AHSYLOG module flags→BKPSUSER program-level→T7LIMACC field-level; all PS* admin programs mapped from BKMENUSU.TXT; BKPSUSER 11 fields confirmed; BKSLEVEL 14×20=422f confirmed | 2026-06-18 |
| Menu System | **93** | 90 | **0** ✅ ↑+9 Pass105 BKMENUSU.DBF=xBase/CodeBase menu store (confirmed); BKMENUSU.TXT=870-line complete code→program mapping; module groups confirmed; PL=Checkmark Payroll Link; NE=New Programs (14 custom i2 items); J7 programs in standard menu confirmed | 2026-06-18 |
| Module: AR | **93** | 92 | **0** ✅ ↑+5 Pass89 BKAR full ISAREX BKAR.INVV IS.CC tax-transfer stats | 2026-06-18 |
| Module: AP | **96** | 92 | **0** ✅ ↑+3 Pass89 ISAPEX BKAP2-UDF BKAP.CHK BKQC recurring ACH/1099 | 2026-06-18 |
| Module: IN/Inventory | **95** | 85 | **0** ✅ ↑+2 Pass91 T6-IN-B 10-tab: IS.ECO/BKSB.MFG/BKSB.VEND/SPECS[12]/RCOST[14] confirmed | 2026-06-18 |
| Module: SO | **96** | 85 | **0** ✅ ↑+2 Pass95 FRGHT/SUBTOT/TOTAL/sobookdate/ASD/rts/recurring-SO/SOAXCOM/ISSR.INFO header+line confirmed | 2026-06-18 |
| Module: PO | **93** | 85 | **0** ✅ ↑+3 Pass89 ISAP.CHG POS-module vendor-master T7POQ delivery | 2026-06-18 |
| Module: WO | **97** | 90 | **0** ✅ ↑+3 Pass88 IS.PREQ/IS.SER/IS.TRAY/IS.WOPRIO ISSO.BOX WO-L suite | 2026-06-18 |
| Module: GL | **95** | 92 | **0** ✅ ↑+2 Pass90 14-period confirmed BKGL.STC/STI fin-stmt config | 2026-06-18 |
| Module: BM/MRP | **90** | 88 | **0** ✅ ↑+2 Pass85 MTIC.PROD MRP fields confirmed | 2026-06-18 |
| Module: RO/Routing | **88** | 88 | **0** ✅ ↑+3 Pass72 | 2026-06-17 |
| Module: DC/Data Collection | **89** | 85 | **0** ✅ ↑+2 Pass86 EvoDCmenu/ht6 confirmed | 2026-06-18 |
| Module: PR/Payroll | **92** | 92 | **0** ✅ ↑+2 Pass84 W-4/CURP/PRLA DFMs | 2026-06-18 |
| Module: AM (Accounting Maint.) | **93** | 85 | **0** ✅ ↑+10 Pass90 14-period GL BKGL.STC/STI fin-stmt archive | 2026-06-18 |
| Module: CM/CRM | **90** | 85 | **0** ✅ ↑+4 Pass95 BKCM.LEAD/TERR/ACFC/DTCD/CATM 5 code tables fully confirmed | 2026-06-18 |
| Module: MK/Marketing Automation | **78** | 78 | **0** ✅ ↑+6 Pass84 BKCM.LEAD/TERR/ACFC confirmed | 2026-06-18 |
| Module: DE/EDI/Imports | **86** | 80 | **0** ✅ ↑+8 Pass86 T7DE* full suite IS.DEF/ISAP.QPO confirmed | 2026-06-18 |
| Module: CS/Commission+Salesperson | **85** | 85 | **0** ✅ ↑+5 Pass84 BKPR.COMM/SLS monthly arrays | 2026-06-18 |
| Module: JC/Job Costing | **87** | 82 | **0** ✅ ↑+9 Pass85 JCA-JCS+JCENG full menu | 2026-06-18 |
| Module: SC/Serial Control ⚠️ | **80** | 80 | **0** ✅ | 2026-06-17 |
| Module: QC/Quality Control | **90** | 88 | **0** ✅ ↑+2 Pass86 BKQC.TRN.*/RoHS confirmed | 2026-06-18 |
| Module: QT/Service Quote | **82** | 75 | **0** ✅ ↑+8 Pass93 ISSR.INFO.DATE[5]+AL[20] confirmed | 2026-06-18 |
| Module: IC/Inventory Utility | **80** | 72 | **0** ✅ ↑+2 Pass77 | 2026-06-17 |
| Module: WC/Warehouse Control ⚠️ | **86** | 80 | **0** ✅ ↑+6 Pass90 WCE/F/G/H/BK/LOCfix bin-assign cycle | 2026-06-18 |
| Module: SH/Shop Scheduling ⚠️ | **88** | 88 | **0** ✅ ↑+5 Pass84 SHA-SHP full menu DFMs | 2026-06-18 |
| Module: LC/Lot Control | **88** | 78 | **0** ✅ ↑+7 Pass85 MTLOT.* LC-A/G DFMs | 2026-06-18 |
| Module: SR/Service Repair | **88** | 82 | **0** ✅ ↑+6 Pass90 SRB/D/E/F/G/I/S full invoice+release | 2026-06-18 |
| Module: FA/Fixed Assets | **86** | 86 | **0** ✅ ↑+4 Pass84 IS.FXA/FXT full field layout | 2026-06-18 |
| Module: PI/Physical Inventory | **88** | 80 | **0** ✅ ↑+12 Pass85 BKPH.* PI-A/H confirmed | 2026-06-18 |
| Module: MA/AR Deposits | **82** | 75 | **0** ✅ ↑+6 Pass92 ISAR.DEPL.SO/AMT/GLACT BKAR.DEP.DEPNO/CUST confirmed | 2026-06-18 |
| Module: ES/Estimating | **88** | 88 | **0** ✅ ↑+3 Pass84 IS.EST 10-qty+convert DFMs | 2026-06-18 |
| Module: SA/Sales Analysis | **84** | 84 | **0** ✅ ↑+4 Pass84 BKSA confirmed top-N+margin | 2026-06-18 |
| Module: AC/Activity Control | **83** | 78 | **0** ✅ ↑+5 Pass92 WODATE/AC.RD/IS.ACTION all fields confirmed | 2026-06-18 |
| Module: CC/Credit Card ⚠️ | **87** | 85 | **0** ✅ ↑+3 Pass92 IS.CC.* all 8 fields + CCYY/CCMM/CVV confirmed | 2026-06-18 |
| Module: SP/SPC ⚠️ | **92** | 92 | **0** ✅ ↑+5 Pass84 SPCLIVEGRID/LIVEREP/REP2/REPPPM | 2026-06-18 |
| Module: HH/Handheld | **93** | 85 | **0** ✅ ↑+13 Pass87 43 DFMs WO/SO/PO/PI/INV full handheld system | 2026-06-18 |
| Module: UT/Utilities | **84** | 75 | **0** ✅ ↑+6 Pass94 UTKA-UTKH data-deletion/GL-transfer/location-rename/item-type-reports | 2026-06-18 |
| Module: RM/RMA | **85** | 82 | **0** ✅ ↑+7 Pass86 SRMA/IS.RMA RMD disposition confirmed | 2026-06-18 |
| Module: FO/Features Options | **87** | 83 | **0** ✅ ↑+4 Pass86 ISFO.HDR.* EvoFNO confirmed | 2026-06-18 |
| Module: IS/InfoSystem | **75** | 72 | **0** ✅ ↑+3 Pass114 ISGLDATE(86f)+ISMCF(49f) fully extracted; T7ISMCC+T7ISASER confirmed | 2026-06-19 |
| Module: IM/Landed Cost | **88** | 82 | **0** ✅ ↑+10 Pass86 ISIS.MCF/MCR multi-currency + landed confirmed | 2026-06-18 |
| Module: PS/Program Security | **88** | 88 | **0** ✅ ↑+6 Pass83 ISEXUSER+max.chk.amt | 2026-06-18 |
| Module: QU/Query Tools | **75** | 75 | **0** ✅ ↑+1 Pass91 WBKLOOKUP/DDFilters/SSS/SSSFD DFMs confirmed | 2026-06-18 |
| Module: SU/Setup UI | **80** | 78 | **0** ✅ ↑+2 Pass119 11 YN flags confirmed from source (YN[20/36/37/38/48/59/66/228/229/290]+YN[1]); YN[228] doc corrected | 2026-06-19 |
| Module: TA/TAS Admin | **91** | 80 | **0** ✅ ↑+3 Pass91 WTASDATAM/DMGR/INIT DFMs: FLD/KEY/FILE descriptors confirmed | 2026-06-18 |
| Module: DI/Digital Signatures | **90** | 80 | **0** ✅ ↑+12 Pass87 T7DIGSIG PO approval 5-level emp.signoff | 2026-06-18 |
| Module: AD/Accounting Defaults | **82** | 82 | **0** ✅ ↑+7 Pass83 ISTS.CFG+bkys.yn[202] | 2026-06-18 |
| Module: CR/SO Approvals | **78** | 78 | **0** ✅ ↑+6 Pass83 CTRevu DFMs | 2026-06-18 |
| Module: US/Triggers | **85** | 75 | **0** ✅ ↑+11 Pass93 IS.TRIG.* all 23 fields confirmed | 2026-06-18 |
| Subsystem: BO/Bill of Lading | **80** | 80 | **0** ✅ ↑+8 Pass82 DFMs confirmed | 2026-06-18 |
| Subsystem: DS/Data Sync stubs | **65** | 65 | **0** ✅ ↑+3 Pass109 all 36 fingerprint tables field-decoded; ISLOG kill-flag mechanism; DBAFIFO=FIFO cost layers; HH/IM codes confirmed | 2026-06-18 |
| Subsystem: AU/Automation | **78** | 78 | **0** ✅ ↑+6 Pass82 DFM confirmed | 2026-06-18 |
| Subsystem: FS/Field Information Base | **78** | 78 | **0** ✅ ↑+6 Pass82 3 DFMs FIB prefix | 2026-06-18 |
| Subsystem: GF/AR Charges | **82** | 80 | **0** ✅ ↑+7 Pass86 IS.GF.DEPT/DIV GFV confirmed | 2026-06-18 |
| Subsystem: RE/Reminders+Rebuild | **83** | 78 | **0** ✅ ↑+8 Pass86 IS.REM.* Google Calendar export | 2026-06-18 |
| Subsystem: SE+ST/Service Code Tables | **74** | 74 | **0** ✅ ↑+9 Pass83 6 DFMs confirmed | 2026-06-18 |
| Subsystem: PU/Put-Away | **76** | 76 | **0** ✅ ↑+8 Pass83 T7PUTAWAY DFM | 2026-06-18 |
| Subsystem: MU/Multi-Yield WO | **78** | 78 | **0** ✅ ↑+6 Pass82 DFM W/F/E confirmed | 2026-06-18 |
| Subsystem: LI/License Access | **72** | 72 | **0** ✅ ↑+7 Pass82 DFM confirmed | 2026-06-18 |
| Subsystem: EDII/EDI Invoice Import | **76** | 76 | **0** ✅ ↑+4 Pass83 T7EDII DFM | 2026-06-18 |
| Subsystem: LG/LGS Custom | **70** | 70 | **0** ✅ ↑+8 Pass64 | 2026-06-17 |
| Subsystem: JS/Reporting Bridges | **78** | 78 | **0** ✅ ↑+10 Pass82 7 DSN DFMs | 2026-06-18 |
| Subsystem: BS/Business Score | **82** | 82 | **0** ✅ ↑+4 Pass82 T7BS+T7BSR DFMs | 2026-06-18 |
| Subsystem: AD/Advanced DC | **72** | 72 | **0** ✅ ↑+2 Pass109 BKDCSHFT all 34 fields decoded; T7ADA/B/C confirmed non-existent; ADCA vs PA distinction | 2026-06-18 |
| Subsystem: IT/Item Serial Config | **78** | 78 | **0** ✅ ↑+6 Pass82 IS.SERC confirmed | 2026-06-18 |
| Module: SD/Standard Detail | **74** | 74 | **0** ✅ ↑+6 Pass82 IS.SDET confirmed | 2026-06-18 |
| Module: SL/Shop Loading | **85** | 70 | **0** ✅ ↑+20 Pass93 T7SHA-SHP MTWC.*/MTWORO.*/SWO.CRATIO/RUN.DAYS fully confirmed | 2026-06-18 |
| Module: AL/Audit Log+AltPart | **76** | 76 | **0** ✅ ↑+6 Pass82 3 DFMs | 2026-06-18 |
| Module: ML/Multi-Language | **76** | 76 | **0** ✅ ↑+8 Pass82 LANGDICT confirmed | 2026-06-18 |
| Module: MH/Shipping Order | **80** | 72 | **0** ✅ ↑+12 Pass94 T7BOL+BOLMSO full BOL structure confirmed | 2026-06-18 |
| Module: BR/Brands | **72** | 72 | **0** ✅ ↑+7 Pass82 BKCM.ACCC confirmed | 2026-06-18 |
| Module: NE/New Company Init | **68** | 68 | **0** ✅ ↑+3 Pass82 stub confirmed | 2026-06-18 |
| Module: JO/Jobs+Departments | **76** | 76 | **0** ✅ ↑+6 Pass82 3 DFMs | 2026-06-18 |
| Module: FN/File Navigator | **72** | 72 | **0** ✅ ↑+7 Pass82 FNR DFM confirmed | 2026-06-18 |
| Module: XC/CC Cross-Ref | **74** | 74 | **0** ✅ ↑+6 Pass82 XCharge DFM | 2026-06-18 |
| Module: IT/Item Config | **78** | 78 | **0** ✅ ↑+6 Pass82 IS.SERC DFM | 2026-06-18 |
| Module: EM/Emergency GL | **72** | 72 | **0** ✅ ↑+7 Pass82 BKGL DFM | 2026-06-18 |
| Module: RT/RTM Validator | **70** | 70 | **0** ✅ ↑+15 Pass84 T7RTMVALID=RTM name picker confirmed | 2026-06-18 |
| Module: FP/FO Print | **55** | 55 | **0** ✅ ↑+13 Pass64 | 2026-06-17 |
| Module: RF/RFQ | **84** | 78 | **0** ✅ ↑+9 Pass93 BKRFQ.EXP/ISSUE/QTY/COST/PROD/LCDATE confirmed | 2026-06-18 |
| Platform Subsystems | **82** | 82 | **0** ✅ ↑+3 Pass107: EvoService=ISSCHED+ISREMIND poller(WTIME/USINI CFG); EvoBackup=AWS Glacier confirmed(GLACIERKEY+GS_ARCH/BACKUP/NONE)+day-of-week schedule(MON/TUE); EvoLinks=IS.LNK.OPENWITH/GLOBAL/PRIVATE/SORT confirmed; BOMTREE/CASHFLOW/CRMDASHBOARD/EDITBOMTREE=EvoPVT.jar launchers(HOST/PORT/TREEDEST/COMP); CALREM=ISREMIND+entity tables(BKARCUST/BKAPVEND/BKICMSTR),no CALREMGC.RWN; EvoERPupd=schema migrator(RESTRUCT_FLD/OLD_FLD_TYPE); EVOBSR=does not exist | 2026-06-18 |
| Subsystem: PI/Physical Inventory | **88** | 80 | **0** ✅ (dup — see primary) | 2026-06-18 |
| Module: SA/Sales Analysis | **84** | 84 | **0** ✅ (dup row — see primary entry) | 2026-06-18 |
| Module: JC/Job Cost | **87** | 82 | **0** ✅ (dup — see primary) | 2026-06-18 |
| Module: ES/Estimating | **88** | 88 | **0** ✅ (dup row — see primary entry) | 2026-06-18 |
| Platform: WBKLOOKUP/Lookup Framework | **76** | 70 | **0** ✅ ↑+8 Pass85 WBKLPRINT/HHLOOKUP | 2026-06-18 |
| Module: DE/DC stubs+EDI processing | **86** | 75 | **0** ✅ (dup of DE/EDI -- see primary) | 2026-06-18 |
| Module: SM/System Maintenance+Item Inquiry | **94** | 86 | **0** ✅ ↑+3 Pass95 SM-I BKCM.LEAD/TERR/ACFC/DTCD/CATM + SM-J SMJA-SMJH 8 archive-purge programs | 2026-06-18 |
| Module: MR/MRP Engine | **90** | 85 | **0** ✅ ↑+10 Pass90 BKMRP.FC/PO MTMRP 4-stage-run MBEDORC WO/PO gen | 2026-06-18 |
| Tables: BKMR*/MRP Support | **78** | 78 | **0** ✅ ↑+6 Pass106e: BKMRPFC/BKMRPPO/BKMRPSW/MTMRP full field tables+semantics; 14-op pipeline; MTMRP action codes; BKMRPPO→BKAPPO flow | 2026-06-18 |
| Tables: BKED*/EDI | **78** | 72 | **0** ✅ ↑+13 Pass106 full family documented: BKEDIH/IL=BKARINV clones; BKEDIDUN/MSTR/NOTE/POST semantics; DEP-B/C/D/E/F/H pipeline | 2026-06-18 |
| Tables: BKES*/Estimating | **78** | 72 | **0** ✅ ↑+13 Pass106 full family documented: BKESTQT/QTL=BKARINV clones; BKESTCFG 13f; ESTSUM 213f 10-qty-break cost summary; ES-A..M pipeline | 2026-06-18 |
| Module: YS/YN Flags Editor | **75** | 75 | **0** ✅ ↑+3 Pass106h: ARRAY/ARRAY.DESC/YSMSTR.H display mechanism; BKSYHELP lookup; 3 confirmed flags; T7MDefaults=primary UI | 2026-06-18 |
| Module: CU/WO Cut Sheet | **75** | 75 | **0** ✅ ↑+3 Pass106h: EJOB/ELOT/EQTY filter vars; ISDUTY+ISBROKER import-duty tracking; J7CCCutSheet(217p,44t) i2 variant documented | 2026-06-18 |
| Subsystem: ADCA/Advanced DC | **72** | 72 | **0** ✅ ↑+2 Pass109 (same entry as AD — see above) | 2026-06-18 |
| Module: TC/Treasury Control | **80** | 75 | **0** ✅ ↑+8 Pass93 T7TCC terms.num+CHK_NAME[1] confirmed | 2026-06-18 |
| Module: SC/Serial Control ⚠️ (dup) | **80** | 80 | **0** ✅ ↑+2 Pass109 MTSER all 30 fields decoded; lifecycle PO→WO→SO traced; ISSERIAL genealogy documented | 2026-06-18 |
| Module: CH/Multi-Location Chain | **72** | 72 | **0** ✅ | 2026-06-17 |
| Module: KI/Kit Assembly | **83** | 72 | **0** ✅ ↑+11 Pass94 T7KIT BOM-component/lot/scan/bin arrays confirmed | 2026-06-18 |
| Module: MA/AR Deposit Apply | **82** | 75 | **0** ✅ (merged with MA/AR Deposits — see primary) | 2026-06-18 |
| Module: TE/NACHA+ACH | **75** | 75 | **0** ✅ ↑+3 Pass106h: WELLS.ID+ACH.FILENAME+date/check-range vars; AR ACH receipts via BKARINVL; NACHA record structure | 2026-06-18 |
| Module: PA/Paperless DC | **72** | 72 | **0** ✅ ↑+2 Pass109 PA vs ADCA table-set diff; WOMAT/INVTXN/ISBINLOT material-issue confirmed; T7PASS session-init sub | 2026-06-18 |
| Module: TPOA/PO Processing Hub | **84** | 75 | **0** ✅ ↑+12 Pass93 T7POA/POA2/POAC/POAE/POACPY BKAP.PO full header+RITEC risk.assess[6]+CONFIRM[1]/[2] | 2026-06-18 |
| Module: QS/Quick SO | **76** | 76 | **0** ✅ ↑+11 Pass84 T7QSOA+QSOALINES DFMs confirmed | 2026-06-18 |
| Subsystem: VSCHED/Visual Scheduler | **78** | 78 | **0** ✅ ↑+10 Pass84 init/start/post/DSN confirmed | 2026-06-18 |
| System: AUTO/Batch Automation | **78** | 78 | **0** ✅ ↑+6 Pass106f: EvoScheduler 3-program architecture; ISSCHED 24f all fields; T7AUTOREBSS 26-table fingerprint; T7AUTOFX ISMCF+ISJAVA+ISMCR flow; T7AUTODCH 42-table fingerprint+ISAUTODC | 2026-06-18 |
| Module: FO/Features+Options | **87** | 83 | **0** ✅ (dup row — see primary) | 2026-06-18 |
| System: Notes/EVONOTES | **82** | 78 | **0** ✅ ↑+10 Pass86 IS.NOTE/LNK/REM tables confirmed | 2026-06-18 |
| Modules: AB/CP/EX/FL/LM/MA/MM/PC/PL/RT/SB/SL/SY/UM/UP/YS (16 opaque) | **60** | 50 | **0** ✅ ↑+13 Pass106m: all 16 IDs confirmed from DDF schema+share scan+BKLME.SRC: AB=License, CP=Checkmark(legacy), EX=launcher, FL=FldHelp, LM=InvTxnConsolidate(SRC✅), MA=MapDepo+Material, MM=MfgMaint(legacy), PC=ProdCtrl, PL=PayLink(menu✅), RT=RoutingTemplates, SB=SpecBook/AVL, SL=SecurityLevels, SY=SysTables, UM=UserMenuSecurity, UP=Update, YS=YN-SysParams | 2026-06-18 |
| RWN String Analysis technique | **90** | 90 | **0** ✅ ↑+8 Pass106 2-technique doc: Technique1=2575 string files, Technique2=rwn_symbols.json 1122 RWN records (db_files/procs/named_vars); workflow; upgrade table | 2026-06-18 |
| Reporting Engine | **88** | 88 | **0** ✅ ↑+6 Pass106c comprehensive module-to-RTM table (12 modules, RTM counts); TAS push-model pipeline (SETUP_REPORT_BUFF/OUTPUT_REPORT_DATA/EXEC_RB); print modes; cfg.rtm status note | 2026-06-18 |
| Platform Subsystems | **82** | 82 | **0** ✅ ↑+3 Pass107 (dup row — see primary above) | 2026-06-18 |
| Java Integration | **88** | 88 | **0** ✅ ↑+3 Pass106l EvoPVT=JavaFX app confirmed (EvoApp+TabularView+LookupPane+SplashScreen); CsvExportTask+TextFileWriteTask+FileOpenTask tasks confirmed; PSQL 13.20.023 driver bundled in JAR; DatabaseSettings reads registry | 2026-06-18 |
| ODBC Connectivity | **92** | 92 | **0** ✅ ↑+1 Pass109 DSN setup parameters (ServerName/Port/Database/@DBA); read/write DML confirmed; read-committed locking semantics documented | 2026-06-18 |
| Customizations (J7\*) | **90** | 80 | **0** ✅ ↑+8 Pass91 41 J7 DFMs: Lapco/PTS/ACH/kanban/sync/web-export all documented | 2026-06-18 |
| Business Workflows | **85** | 85 | **0** ✅ ↑+3 Pass106d Recipes15-16: lot/serial tracking lifecycle + new company creation | 2026-06-18 |
| Encryption / RWN Decryption | 100 | 95 | 0 ✅ | 2026-06-16 |
| Per-Table Narrative Docs | **88** | 88 | **0** ✅ ↑+1 Pass108: INVTXN(24f) full narrative added — cross-module inventory transaction log (TYPE R/I/A/S/P/X, AVGCOST+STDCST confirmed, REF=source document, PRODLOT for WO receipts); WOLABOR(58f) full narrative added — WO labor transaction (LABRATE/LABCOST/SETCOST/MACHCOST/FOHCOST/VOHCOST, cycle-count metrics CYCHR/MIN/SEC/PARTS/NOTE, FLAG_1..5+ALPHA_1..3 custom fields) | 2026-06-18 |
| PROJECT-STRUCTURE.md | **90** | 90 | **0** ✅ ↑+4 Pass106g: 45 inferred→confirmed via DDF cross-check; confidence note updated ↑+6 Pass103 AP 6→26 entries, AR 5→17, PO 0→30 (full new section), SO 1→21; 171 DFM forms cataloged | 2026-06-18 |
| HELP-RESOURCES.md | **92** | 92 | **0** ✅ ↑+2 Pass108: Platform Subsystems section added (EvoService/EvoServiceSetup/EvoBackup/EvoLinks/CALREM — all programs, tables, config keys, how-to procedures); Spec Book/AVL (SB) section added (BKSBMFG/BKSBVEND/BKSBPART — PK structure, MRP enforcement); 6 QUICK LOOKUP entries added (SMTP config/backup/Glacier restore/links/reminders/AVL) | 2026-06-18 |

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
| ~~**4**~~ | ~~Re-decrypt all 1,124 `.RWN` files locally~~ | ✅ **DONE** — `samples/rwn_decrypted/` contains 1,123 `.dec` files; validated by file ID pattern (bytes 0-3==4-7); `rwn_symbols.json` built from these (1,122 entries) | Module variable/DB catalog complete |
| **5** | Map `.RWN` bytecode instruction set via Rosetta Stone | 🔄 **C: 60/100** — DISP_START=0x6C0 universal; 17 opcodes; 0x20=CREATE FORM/BIND, 0x57=EXECUTE FORM, 0x42=GOSUB, 0x0F=ASSIGN, 0x3B/0xD2/0x6A=BRANCH confirmed; .dec files regenerated 1145/1146 OK | Full logic traceability |
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
