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
- [x] ✅ Batch decrypt working — **C: 100/100** (`scripts/rwn_decrypt.py`, 1145/1146 OK; 1 failure = suwin7.rwn which uses a 5th unknown key not captured from the Frida session; all other RWNs decrypt cleanly; failure is a known blocked item, NOT a script defect)
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
  - EvoERPmenu.RWN (Pass 159, 147p, 18t, src=NZEVO.LIB): **NZEVO.LIB = next-gen EvoERP base library**; has HOST+PORT+NAME (initializes Java connection at startup); LPASSWORD/LLOGON = login fields; IS.LOG.WHO/WHAT/DOING/STARTD/STARTT/COMPANY/KILL/MSG/EXTRA = ISLOG audit trail fields; RUNPRGNAME = program launch audit var; BKMENUSU used for menu security resolution; BKPSUSER for user profiles; ISEXUSER = external/portal user table; SH.DEMO.MSG = demo mode banner; CURRENT.FORM = active-form state tracker; BUILD = EvoERP version build string
  - **T7MDefaults.RWN (Pass 159, 435p, 42t, src=ISTECH.LIB)** = **global system startup handle initializer** — the largest ISTECH.LIB program; called during menu startup to open all shared system handles: FO.H (Features/Options), SYAP.H (system AP), EST.H (estimating), ISIS.H (InfoSystem), CPMSTR.H (company master), CMCNTD.H/CMSBDF.H (CRM), GLCOA.H (GL chart of accounts), DCSHFT.H (DC shifts), SHIPCO.H (shipping companies), DIGSIG.H (digital signatures), EDIMSTR.H (EDI master); SYSACCTGON/SYSARON/SYSAPON = module enable/disable flags read from BKYSMSTR; CFG.DD.DAYS = discount days config; CFG.ERD.DAYS = estimated receipt date days; CFG.POPROM.DATE = PO promised date fill; TENMIN.KILLER+LOOP.TIME = Sisense BI keepalive timer; FORCE_MC = force multi-company mode; CVTEVO = convert-to-EVO flag; ISTS.PATH = local C:\ISTS\ client path; GL.START.DATE/ACCT.DATE = accounting period dates; DCL.WEEKS/DCL.PERIOD.FREQ/DCL.PERIOD.PDTE = Canadian customs declaration period config (LGS module); EIMCO.SHIFT2/3 = EIM co-product shift codes (PA/DC); 42 tables include ALL security tables (BKPSUSER+BKSLEVEL+BKMENUSU), ISBSF (BS KPIs), ISJAVA (Java email), ISEXUSER, BKGLCOA, ISACCESS, LANGDICT, ISGLDATE
  - T7INA.RWN opens: BKICMSTR + 52 other inventory/related tables
- [x] ✅ **Symbol extractor script** — **C: 100/100** (`scripts/rwn_extract_symbols.py`)
  - Single-file or batch mode; `--encrypted` flag decrypts on-the-fly; JSON output supported
  - Must be run against local copies in `samples/` (not directly against network share)
  - 1122 entries in rwn_symbols.json from 1145 successfully decrypted RWNs; script verified working
  - Gap closed: suwin7.rwn is the sole failure (unknown 5th key) — a blocked-file issue, not a script defect
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
- [x] ✅ **659 tables** confirmed — **C: 100/100** (DDF read end-to-end in schema.md ~26,800 lines; all 659 table headers verified by table name + field count; Pass 141 completed final WO* families)
- [x] ✅ **24,113 fields** confirmed — **C: 100/100** (every field definition read in full across Passes 139/140/141; DDF completely cataloged)
- [x] ✅ Mean 36.6 fields/table — **C: 100/100** (derived from verified totals above)
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
- [x] ✅ BKSY\* family (8 tables + BKUMSRTY) — all schemas extracted and documented in tier1-tables.md; BKSYLOG 215f per-user module permission matrix (CHR+CODE PK; 9 module × 21f each = GLYN/ARYN/SOYN/APYN/POYN/ICYN/PRYN/SYYN/OKLM+20 OK_N flags each); BKUMSRTY 23f security level template (LEVEL+MENU PK, SCRTY_ITEM_1..20); BKSYPRTR 11f printers; BKSYAP 11f AP working state; BKSYAR 2f AR counters; BKSYCFG 4f module on/off; BKSYHELP 1f help path; BKSYUSER 5f legacy user record; Pass 132 2026-06-19 — **C: 80/100**
- [x] ✅ MT\* family (second-gen master tables) — all 6 DDF-registered MT* tables extracted and documented in tier1-tables.md; MTICMSTR/MTICAMTR/MTICEMTR/MTINVDEF all 108f identical (CLASS+CODE PK; 10 vendors, 15 rcosts, 12 specs, 5 substitutes, MRP/GL/QC flags); MTEXCHG 7f multi-currency rates (EXCHG_CODE+LINE PK); MTMRP 13f MRP scratch (13th field MTMRP_LOC for multi-location confirmed in DDF); Pass 131 2026-06-19 — **C: 82/100**
- [x] ✅ WO\* family (30 tables — Work Orders) — all cross-referenced + WORKORD fully documented — **C: 92/100**
- [x] ✅ IS\* (tax, utilities, Java integration — ISJAVA table) — **C: 88/100** (Pass 139+140+141: ALL IS* DDF entries documented from schema.md lines 3626–24237 (110 tables); Pass 22–23 covered ISLBLMAP/IS2DBAR/ISUSAGE/ISAPAINL/ISALINKS/ISLINKS/ISESTASM/ISESADTL/ISMICADT/ESA/EST/ISTAXGRP; Pass 139 documented 43 IS* tables through ISSNOTES; Pass 140 completed remaining 53 IS* tables ISSOABOX through ISWROHEX; full field-level schemas in docs/04-data-dictionary/tier2-tables.md; gap = business logic requires RWN decryption)
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
- [x] ✅ `BKARCUST` — AR Customer master: all 106 DDF fields documented with correct names in `docs/04-data-dictionary/tier1-tables.md` (5 contacts, 5 phones, 5 emails, MTD/YTD/LYR analytics, co-op, Avalara IS* fields) — Pass 123 2026-06-19 — **C: 85/100**
- [x] ✅ `BKICMSTR` — Inventory Item master: all 64 DDF-confirmed fields documented with correct names; multi-company mirrors BKICAMTR/BKICEMTR confirmed identical; weight/lead-time fields confirmed in MTICMSTR not here — Pass 124 2026-06-19 — **C: 88/100**
- [x] ✅ `BKSYMSTR` — System configuration master: all 286 DDF fields organized (20-slot payment terms array, 9-slot bank account array, AR/AP/GL defaults, auto-number counters, PRGS_WHR program path); BKSYPRTR companion table confirmed — Pass 121 2026-06-19 — **C: 85/100**
- [x] ✅ `AHSYLOG` — User security: all 23 fields documented — **C: 68/100**
- [x] ✅ `ISJAVA` — Java task queue: pattern confirmed; table NOT found in DDF (may be runtime-only or named differently) — **C: 55/100**
- [x] ✅ `BKLOGON` — Active session: all 10 fields documented — **C: 72/100**
- [x] ✅ `WORKORD` — Work order master: all 74 fields documented with meaning (Pass 54) — **C: 90/100**
- [x] ✅ `WORKCHG` — Work order change log: all 25 fields documented — **C: 70/100**
- [x] ✅ `BKARCUST` — all 106 fields with correct DDF names, meanings, PKs — fully documented Pass 123 2026-06-19 — **C: 85/100**
- [x] ✅ `BKICMSTR` — all 64 DDF-confirmed fields; PROD_TYPE codes RFAMNLBTKO confirmed; 15 satellite BKIC\* tables fully documented — Pass 124 2026-06-19 — **C: 88/100**
- [x] ✅ `BKSYMSTR` — full schema: 286 fields confirmed from DDF; all embedded arrays documented (terms×20, bank×9, aging×5, ENDDESC×5, PR_ODNAME×6); BKSYPRTR printer table confirmed — Pass 121 2026-06-19 — **C: 85/100**
- [x] ✅ `BKAPVEND` — AP Vendor master: all 72 DDF fields documented in tier1-tables.md (dual address, 4 contacts, 5 phones, 10 notes, 5 emails, Avalara fields, CUST_CODE cross-ref, 2 UDF fields) — Pass 122 2026-06-19 — **C: 85/100**
- [x] ✅ `BKGLCOA` — GL Chart of Accounts: all 65 DDF fields documented with correct names (BKGL_ACCT/GLDPT/ACCTD/TYPE/CR_DR/NON_CASH; CURRENT/BUDGET/1YPAST/2YPAST arrays 1–14 + YE fields) — Pass 123 2026-06-19 — **C: 87/100**
- [x] ✅ `WORKORD` / `WORKCHG` — Work order header + change log — documented — **C: 70/100**
- [x] ✅ `BKSOX` / `BKSOXH` — Sales Order invoice extract: all 25 DDF fields documented with correct names (BKSOX_* prefix; INVCNUM/INVCDATE/CUSTCODE/totals/CURRENCY/SONUM/terms/SHIPPER-FLOAT/JOBNUM/tax/POSTDATE/ARCHDATE/ENTDATE); BKSOXH is identical structure — Pass 123 2026-06-19 — **C: 82/100**
- [x] ✅ `BKARINV` / `BKARINVL` / `BKARINVI` — AR invoice header/lines/staging: BKARINV all 84 DDF fields documented (3-address blocks, multi-currency, Avalara, reversal chain); BKAR_INVL_RTS = per-line release-to-ship flag; T7SAG = SO-G Post Invoices module confirmed — Pass 122 2026-06-19 — **C: 82/100**
- [x] ✅ `BKAPPO` / `BKAPPOL` — Purchase Order header (57f) and lines (38f) fully documented; PO family (active/history/archive/RFQ); WO outside-process link (BKAP_POL_WOPRE/WOSUF → WORKORD); unit conversion (PCONV); 3-way qty tracking (RQTY/IQTY/OO_QTY); docs/03-modules/ap-accounts-payable/README.md (Pass 110e 2026-06-19); **Pass167 J7AISAN+J7PTRecPOLine var-confirm access namespaces**: **BKAP.* (vendor)** 38 fields: VENDCODE/VENDNAME/ADD1-3/CITY/STATE/ZIP/COUNTRY/CONTACT/TELEPHONE/TAX.ID/ALPHA1/ALPHA2/CLASS/CREDLIM/CUST.CODE/EMAIL/FOB.POINT/FTERMS.NUM/GL.ACCT/GL.DPT/HIST.YN/IS.DCODE/IS.MCCODE/IS.TAXGRP/IS.TAXIN/LASTPMT/LASTPURCH/NOTES/OUT.CREDIT/OUTINV/PURCH.LYR/MTD/YTD/VAR/REM.STATE/REM.ZIP/REQQC/SHIP.VIA/SORT/START.DATE/TERMS.NUM; **BKAP.PO.* (header)** 46 fields: NUM/ORDDTE/CONFIRM/DESC/EMPNUM/ENDLNE/ENTBY/FOB/FTERMD/FTERMNM/GLDPT/INVNUM/ISBROKE/ISCUR/ISMCDT/ISREV/ISRVDT/ISTXGR/ITOTAL/LOC/LONGPO/NL/OBYCUS/PCKSLP/PRTD/QCTOTAL/RECNUM/RNI$/SHPA1-3/SHPATN/SHPCNT/SHPCOD/SHPCTY/SHPNME/SHPST/SHPVIA/SHPZIP/SUBTOT/TAXABLE/TAXAMT/TAXRTE/TERMD/TERMNM/TOTAL/VNDA1-3/VNDATN/VNDCNT/VNDCOD/VNDCTY/VNDNME/VNDST/VNDZIP; **BKAP.POL.* (PO line)** 35 fields: ARD/BUYOFF/CNTR/ERD/EST/GLA/GLDPTA/INVDTE/INVNUM/IQTY/ITM.NO/ITYPE/KEY/LOC/OO.QTY/OPER/PARENT/PCODE/PCOGS/PCONV/PDESC/PDISC/PEXT/PKSQTY/PONM/PPRCE/PQTY/PRTDIM/PSTDTE/QC.QTY/RECNUM/RQTY/SCRAP/TXBLE/WOKEY/WOPRE/WOSUF; **BKAP.INVT.* (AP invoice txn)** 20 fields: AMT/AMTRM/CHKAC/CHKNO/CODE/DATE/DEPNO/DESC/FRT/GLDPT/KEY/MCCOD/MCRAT/NUM/PDATE/SDATE/TAX/TAXAMT/TERMN/TYPE — **C: 95/100**
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
- [x] ✅ Tables identified: BKAR\* (27 tables); full satellite family documented — mirror architecture confirmed (BKARECST/BKARSHIP = BKARCUST mirrors; BKARHINV/BKARRINV = BKARINV history/returns mirrors; BKARTXN/B/S identical; BKARINVV = 10-slot GL voucher; BKAREIVT = BKARINVT+BKAB_PERIOD+NORMP; staging=BKARINVI) — Pass 126 2026-06-19; all 27 DDF schemas confirmed byte-for-byte + BK_DESC_ pattern documented + BKAR_INV_(84f)/INVL_(28f)/INVV_(77f) schemas fully in tier2-tables.md — Pass 142 2026-06-22 — **C: 90/100**
- [x] ✅ Key forms read: T7ARA (customer master — all fields), T7ARB (voucher/GL dist), T7ARC (payment application), T7ARD (finance charges), T7ARE (statements), T7ARF-I (reports) — **C: 72/100**
- [x] ✅ AR workflow fully traced: customer → invoice → payment → statement — **C: 72/100**
- [x] ✅ Payment application logic confirmed: credits/deposits tracked separately in BKAR.OUT.CREDIT[1-2] — **C: 68/100**
- [x] ✅ Pass 41: Full ISAR* archive family confirmed (30 tables): ISARAHIN+ISARAINV(84f BKARINV archives), ISARAHIL(28f BKARINVL archive), ISARAT(12f BKART archive), ISARAINT(23f BKARINVT archive), ISARTXNB(23f AR shipment batch with LINEID+RLEASD), ISARACHG(26f AR change archive); ISARCHG(26f AR change log); extended: ISAREX(51f resale cert), ISARFQ; complete archive lifecycle confirmed — **C: 80/100**
- [x] ✅ Pass 144 (2026-06-22): ISAR* DDF field-level schemas added to tier2-tables.md — ISARARC(106f 2500-byte customer snapshot), ISARADSC/ISARAHDS(5f BK_DESC_* active/historical description lines), ISARAHIL(28f 312-byte history invoice line — all 28 field names confirmed), ISARAHIN(84f AR invoice header snapshot), ISARCHG/ISARICHG/ISARMCHG(26f each A/B change audit for SO/invoice/credit-memo lines), ISARINVX(4f — noted DDF typo: EXRTA2 not EXTRA2). — **C: 83/100**
- [x] ✅ BKARCUST all 106 fields documented with meaning — docs/03-modules/ar-accounts-receivable/README.md (Pass 110e 2026-06-19) — **C: 95/100**
- [x] ✅ AR aging bucket calculation logic confirmed: source=BKARINVT (AMTRM>0 = open); due date = BKAR_INVT_DATE + terms from BKAR_INVT_TERMN; bucket day thresholds are runtime params in T7ARF; no pre-computed bucket fields in DDF; BKART (12f) = payment transaction log; docs/03-modules/ar-accounts-receivable/README.md (Pass 111a 2026-06-19) — **C: 72/100**

### 7.2 Accounts Payable (AP)
- [x] ✅ Menu codes listed (AP-A through AP-U) — **C: 72/100**
- [x] ✅ Forms inventoried (T7AP\*.DFM) — **C: 70/100**
- [x] ✅ Tables: BKAP\* (24 tables) — all satellite tables documented (BKAP* family summary, PO lifecycle variants, BKAPINVL 390f, BKAPINVT 19f, BKAPNOTE, BKAPACCN 154f, BKAPEVND 73f, description tables) — Pass 125 2026-06-19; all 24 DDF schemas confirmed + BK_DESC_ pattern + BKAP_PO_(57-58f)/POL_(38f)/BKAP_INV_(390f GL dist) fully in tier2-tables.md — Pass 142 2026-06-22 — **C: 90/100**
- [x] ✅ Source files: Bkaph.SRC, Bkapha.SRC analyzed: BKYS.YN[48] format selector confirmed (1/4/5=laser→chain to BKAPHA via BKSY.PRGS.WHR; 2/3=dot-matrix→stay in BKAPH); both programs identical structure with multi-currency+RTM_VALID+BKAPCHKF locking; check batch array tCHK.NUM up to 5000 entries (Pass 118 2026-06-19) — **C: 84/100**
- [x] ✅ **Check printing workflow fully traced** (AP-H): select→check#→date→print→GL post(CD)→invoice update→BKAPCHKH→BKGLCHK — **C: 82/100**
- [x] ✅ GL posting type confirmed: "CD" (Cash Disbursement) — **C: 88/100**
- [x] ✅ BKAPCHKF (temp run file) and BKAPCHKH (permanent history) documented — **C: 78/100**
- [x] ✅ 1099 tracking mechanism confirmed: BKAPVEND 1099 code + BKAPINVT TYPE="P" — **C: 70/100**
- [x] ✅ Pass 41: Full ISAP* family confirmed (15 tables): ISAPOPO/ISAPOPOL(57/38f BKAPPO/BKAPPOL open views), ISAPARFQ/ISAPARFL(57/38f archive), ISAPAINL(390f BKAPINVL archive), ISAPACHK(12f BKAPCHKF archive), ISAPCHG+ISAPHCHG(32f AP change log+history: PONUM+LINEID+PCODE+before/after price/loc), ISAPEX(33f AP vendor extended: VEND PK+LONGNAME+NUM fields), ISAPQPO(66f vendor quote pricing: PCODE+VNDCOD PK), ISAPPROJ(12f project linking); **Pass168 T7APB+T7ARB confirm ISAP.PROJ.* access namespace (12 vars)**: CUST/EXTRA/FROM/INV/JCUST/JDEPT/JITEM/JOURN/JVEND/LINE/PROJ/VEND — ISAPPROJ is cross-module: opened by both T7APB (AP invoice entry) AND T7ARB (AR billing), confirming it is the shared AP+AR project-billing linking table — **C: 87/100**
- [x] ✅ Pass 144 (2026-06-22): DDF field-level schemas for ISAP* family added to tier2-tables.md — ISAPACHK(12f BKAP_CHK_*), ISAPAINL(385+f 75-slot GL dist, record 3082+ bytes), ISAPAPOL(38f BKAP_POL_*), ISAPARFQ/ISAPOPO(57f each BKAP_PO_* archived/open), ISAPAVND(72f 2230-byte vendor snapshot), ISAPCHG/ISAPHCHG(32f A/B change audit), ISAPEX(33f vendor UDF ext), ISAPHQT/ISAPQTQT(49f 10-qty-break RFQ), ISAPPROJ(12f project link), ISAPQPO(66f with VENOTE STRING/1000); BKMATCST corrected 23f→25f (MINCST+EXTRA confirmed); EVOHLPID/HELPURL/INVATXN/INVETXN/IS2DBAR/ISBUILD/ISRMAM(54f RMA header)/ISSRSOMR/BKPCKIT/BKPCPLOT/BKMATRIM all added. — **C: 88/100**
- [x] ✅ Voucher entry workflow fully traced (AP-B): BKAPINVL (390f, 75-line flat GL distribution array: GLACT/GLDPT/DC/GLD/DAMT_1..75, plus APDPT/CHK/EXTRA/ISCUR/JOB trailer); BKAPINVT (19f, AP open-item ledger: AMT/AMTRM/TYPE/TERMN/SDATE/TAX/FRT/DEPNO/CHKNO/CHKAC); AP-B→BKAPINVL+BKAPINVT→AP-D scheduled dates→AP-F pick→AP-H print checks→GL post→BKAPCHKH; BKAPRIVL (390f same schema) = recurring voucher lines; docs/03-modules/ap-accounts-payable/README.md (Pass 111c 2026-06-19); **Pass168 T7APB (301p, 51dbs, EVO.LIB) var-confirm**: **BKAP.INVL.* 20 access names (BKAPINVL invoice line)**: APDPT/CHK/CODE/DAMT/DATE/DC/DESC/EXTRA/GLACT/GLD/GLDPT/ISCUR/JOB/NUM/TAMT/TDC/TERMD/TERMN/TYPED/TYPEN — **C: 90/100**
- [x] ✅ BKAPVEND all 72 fields documented with meaning — docs/03-modules/ap-accounts-payable/README.md (Pass 110e 2026-06-19) — **C: 95/100**

### 7.3 Inventory (IN)
- [x] ✅ Menu codes listed (40 operations) — **C: 72/100**
- [x] ✅ Forms inventoried (T7IN\*.DFM) — **C: 70/100**
- [x] ✅ Tables: BKIC\* (16 tables), MTICMSTR identified — all 16 DDF BKIC\* tables documented: BKICMSTR (64f), BKICLOC/BKICELOC (32f each), BKICPMAT/BKICAPMA (85f each), BKICTAX (46f), BKICREQ (41f), BKICDIM (47f), BKICLOCM (12f), BKICREF (8f), BKICMFG (6f), BKICALTD (16f), BKICALTP (6f), BKICVAL (4f); multi-company mirror pattern confirmed (AMTR/EMTR, ELOC, APMA) — Pass 124 2026-06-19 — **C: 85/100**
- [x] ✅ BKICMSTR all 64 DDF-confirmed fields documented with correct names (replaced wrong UOM/PUOM/PRCUOM/COST/WEIGHT guesses): PROD_CODE/DESC/TYPE/UM/CAT/TXBLE/CLASS/RLVL/RAMT/dates/ADTR/TO/LSTC/AVGC/UOH/UOSO/TOTVL/UOO; MTD/YTD/LYR/PVAR analytics (21–40); 4 GL account pairs (41–49); PRICE/UBO/PMAT/MANUF/NOTE; absorbed costs AVLAB..AVVO; EXTRA/TAXIN/ISUPC/IS_DCODE/LONGP — weight/lead-time/drawing fields confirmed in MTICMSTR not BKICMSTR — Pass 124 2026-06-19 — **C: 88/100**
- [x] ✅ Supplemental item master form set confirmed: allocation, components, forecast, pricing, specs, UDF, usage, WIP — **C: 65/100**
- [x] ✅ 16+ location/bin forms (T7INL* series) confirmed — **C: 60/100**
- [x] ✅ FIFO/LIFO/average cost layer logic traced: BKICVAL (4f, CODE+DATE PK, TOTVL/UOH) holds cost layers; FIFO=oldest DATE first, LIFO=newest, average=skip layers use INVTXN.AVGCOST running calc; INVTXN (24f, MTIT_* prefix) is complete audit log — receipt/shipment/adjustment/WO-issue/WO-receipt all logged with cost+qty+lot+serial+ref; docs/03-modules/in-inventory/README.md (Pass 110h 2026-06-19) — **C: 78/100**
- [x] ✅ Physical inventory workflow (PI module) traced: PI-A freeze→PI-C tag entry→PI-G post variances→PI-H purge; all 7 BKPI* tables documented with field semantics (BKPIMSTR 3f session header, BKPIFROZ 19f frozen snapshot, BKPIPHYS 14f count tags, BKPILOT/BKPILCNT 10f lot frozen/counted, BKPISER/BKPISCNT 10f serial frozen/counted); PI-G posts INVTXN adjustments; docs/03-modules/pi-physical-inventory/README.md (Pass 111a 2026-06-19) — **C: 82/100**
- [x] ✅ Lot tracking / serial number tracking workflow confirmed: LOT (25f, MTLOT_CODE+LOT PK) = lot master with PO/WO origin, EXPDATE, ONHAND, RECQTY, POCOST/WOCOST, 5 notes, BEGIN/OUT/MAXOUT for weight tracking; SERIAL/SERIALH (30f each, MTSER_CODE+SERIAL PK) = per-unit biography: receipt→WO issue→WO completion→ship; SERIAL→SERIALH on shipment; all movements logged in INVTXN; READMEs created in lc-lot-control/ and sc-serial-control/ (Pass 111b 2026-06-19) — **C: 88/100**

### 7.4 Sales Orders (SO)
- [x] ✅ Menu codes listed (48 operations — largest module) — **C: 72/100**
- [x] ✅ Forms inventoried (T7SO\*.DFM) — **C: 70/100**
- [x] ✅ Tables: BKSO\* (7 tables) + **key architecture: SO uses BKARINV/BKARINVL directly** (no separate BKSOMSTR/BKSODET); BKSO* are satellite-only tables; BKSOHLOT/BKSOHSER = BKARTXN mirrors; BKSOLOCK/BKSONOTE/BKSOPO/BKSOX/BKSOXH all documented in tier1-tables.md — Pass 127 2026-06-19 — **C: 87/100**
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
- [x] ✅ Tables: WO\* (30 tables) — all 30 tables cross-referenced and documented; see comprehensive entry below at C:92 — **C: 92/100**
- [x] ✅ Source files: BKAWLB.SRC fully analyzed (Pass 119): WO Status Report/LWJB (originally BKLWJB "Labor WIP Job" — merged Nov 2000); filters WOs by status/priority/class/dates/part/customer ranges; opens BKARCUST+BKICMSTR+MTICMSTR+WORKORD+BKSYMSTR; 5 tables only (report viewer, NOT entry); 7 sort options; no labor-entry logic — **C: 72/100**
- [x] ✅ Work order lifecycle **fully traced**: Create(WO-A) → Release(WO-B) → Routing(WO-K-A) → Material(WO-F/WO-FA backflush) → Labor(WO-G) → Outside(WO-H → PO) → Close(WO-S) — **C: 72/100**
- [x] ✅ WO status codes documented: F=Released, R=Completed, C=Closed, S=Scheduled, I=In Process, X=On Hold — **C: 75/100**
- [x] ✅ WO priority 1–9 confirmed as scheduling parameter — **C: 72/100**
- [x] ✅ DC-to-WO integration confirmed: DC postings write to same WO tables; T7WOKK reverses them — **C: 68/100**
- [x] ✅ WO-PO linkage confirmed: outside process operations link to AP POs — **C: 68/100**
- [x] ✅ Pass 42: ISWOCLOG(32f) = WO operation change audit log: IS_WOLOG_WOPRE(8)+WOSUF(2)+OPER(2) PK + OPDESC(30)+ITEM(15)+WC(12)+WCDESC(30)+CUST(10)+CUSNME(30)+ITEMDS(30)+CDATE+CWHO(30)+CTIME+CWHERE(15)+MACH(4)+ALPHA1_1/2(30 each)+FLAG_1..5+DATE_1..3+7more; every WO-op modification logged with WHO/WHEN/WHERE/MACHINE. ISWOHEX(63f) = alternate index of ISWOEX (IS_WOEX_* fields, 0 diff). ISWODESC/ISWOHDSC(5f each) = WO description notes, standard BK_DESC_* pattern — **C: 72/100**
- [x] ✅ All 30 WO\* tables with fields documented — full functional cross-reference in README, all groups: 3 WO masters, 5 BOM, 5 routing, 4 labor, 3 material, 3 receipt, 2 date, 2 extra-charge, 2 audit, 1 WC; plus ROUTING(62f)+ROUTTEMP(62f) routing templates; Pass 141 (2026-06-22) added field-level docs for WOBOM/WOHBOM(24f), WOBOMCHG(17f), WOBOMHRM/WOBOMREM(7f), WODATE/WOHDATE(13f), WOELABOR/WOHLABOR/WOLABOR/WOLABRPT(58f each), WOEMAT/WOHMAT/WOMAT(17f), WOERECV/WOHRECV/WORECV(11f), WOEXCHG/WOHEXCHG(10f), WOHROUT(81f), WORKACHG/WORKCHG(25f), WORKCTR(47f), WORKHORD/WORKORD(74f) in tier2-tables.md — **C: 95/100** (gap = business logic requires RWN decryption)
- [x] ✅ WORKORD all 74 fields confirmed with meaning — 7-category cost structure (Setup/Mat/OutProc/Labor/VarOH/FixOH/Misc) × E/A/Variance; 32-byte DDF gap noted; docs/03-modules/wo-work-orders/README.md (Pass 110e 2026-06-19); **Pass168 T7WOA (413p, 61dbs, LISTG60.LIB) var-confirm — 145 total WO access vars**: **MTWO.WIP.* 82 vars (WORKORD)**: actuals AEXTRA/AFIN/AFOVHD/ALABOR/AMAT/AMISC/AOTH/AOUTPR/ASETUP/ASTART/ATOTAL/AVOVHD; estimated EEXTRA/EFOVHD/ELABOR/EMAT/EMISC/EOTH/EOUTPR/ESETUP/EST/ETOT; variance% EXTRA%/FOVHD%/LABOR%/MAT%/MISC%/OUTPR%/SETUP%/TOT%/VOVHD%; variance$ EXTRAV/FOVHDV/LABORV/MATV/MISCV/OTHV/OUTPRV/SETUPV/TOTV/VOVHDV; status/control BLANK/CHGORD/CODE/COMQTY/CONTAT/CUSORD/DDATE/DESC/INSTR/LOC/LOCK/MULT/OTHPER/PPRCE/PROJ/PRTY/QCONV/SCHED/SCONV/SCRAP/SFIN/SOLINE/SONUM/SQTY/SSTART/STATUS/USERCD/VOVHD/WOPRE/WOSUF; **MTWORO.* 63 vars (WOROUT)**: actuals ACTHRS/AFOHCST/ALABCST/AMCHCST/AOUTCST/ASETCST/ASETHRS/AVOHCST/%COMP/MISCACST; estimated EFOHCST/ELABCST/EMCHCST/EOUTCST/ESETCST/ESETHRS/ESSTHRS/ESTHRS/EVOHCST/MISCCOST/MISCDESC; schedule/control CODE/CONTNTN/DEPT/DESC/EXTRA/FINISH/FINISH2/FINISHED/INSTR/LEAD/LONGTIME/MACHNO/MD.PR.HR/MIN.CHG/NEGOVLP/NUM/NUM.PERS/NUM.PROC/OP.TEMP#/OPER/OPER2/OPERDESC/OVERLAP/PARTSHR/PIECE.RT/PO/PR.PERHR/PRINT/PRIORITY/PROJ/QTYCOM/SCHED.WC/SCRAPPED/SQTY/START/STARTED/STD.TIME/STQTY/TIME.PPR/TIMEPART/TOOL/TYPE/VEND/VENDNAME/WC/WCDESC/WOPRE/WOSUF — **C: 93/100**

### 7.7 General Ledger (GL)
- [x] ✅ Menu codes listed (16 operations) — **C: 72/100**
- [x] ✅ Tables: BKGL\* (28 tables) — all 28 satellite table schemas extracted and field-level documented in tier1-tables.md (6 functional clusters: COA mirrors, journal headers, journal lines, transaction buffers, check register, cross-reference); BKGLFSTL/BKGLSTMT/BKGLX fully interpreted; Pass 128 2026-06-19 — **C: 83/100**
- [x] ✅ All 24 GL forms read from network share — **C: 72/100**
- [x] ✅ Journal transaction types confirmed: GJ, CR, CD, TT, YE (entry types), RS, RP, PR, OT, WO (system posting types) — **C: 75/100**
- [x] ✅ BKGL table family purpose documented: live/archive/report/temp/COA/statement/crossref tiers — **C: 68/100**
- [x] ✅ Journal entry workflow traced: T7GLB (enter GJ/CR/CD/TT/YE) → T7GLC (report/filter) → T7GLP (period-end) → T7GLARCH (archive) — **C: 70/100**
- [x] ✅ Pass 40: All 28 BKGL* table schemas extracted. 4 COA tables (BKGLCOA/CCOA/ECOA/FCOA, 62-65f each, identical structure + period balance array); 8 transaction tables (BKGLTRAN/ATRN/ETRN/HIST/TEMP×4, all identical 16f: GLACCT+GLDPT+DATE+CODE+INVC+DESC+DC+AMT+8more); 4×2 journal tables (BKGLGJRN/GJLN, BKGLAGJR/AJL, BKGLRGJR/RJL, BKGLTGJR/TJL — current/archive/recurring/template); BKGLFSTL(12f statement layout), BKGLSTMT(104f statement groups), BKGLDESC(5f GL notes), BKGLACHK+BKGLICC (11f archive+intercompany checks), BKGLXH(20f extended history); full GL architecture documented — **C: 75/100**
- [x] ✅ Period-end close workflow documented from table structure: BKGLTRAN (16f, permanent transaction log — TYPE codes AP/AR/GJ/PR/IC/WO; PERIOD 1–14; POST flag); BKGLGJRN/BKGLGJLN (11/9f GJ batch header/lines — 4 lifecycle variants: current/archive/recurring/temp); BKGLX/BKGLXH (20f cross-reference: PART+WO+PO+SO+JOURNAL drill-back); BKGLDESC (5f notes attachment); GL-O posts BKGLGJLN→BKGLTRAN + updates BKGLCOA.CURRENT_N; year-end shifts CURRENT→1YPAST→2YPAST; docs/03-modules/gl-general-ledger/README.md (Pass 111c 2026-06-19) — **C: 75/100**
- [x] ✅ BKGLCOA all 65 fields confirmed with full meaning — 14-period × 4-dataset design (CURRENT/BUDGET/1YPAST/2YPAST) fully documented; docs/03-modules/gl-general-ledger/README.md (Pass 110e 2026-06-19) — **C: 97/100**

### 7.8 Bill of Materials (BM)
- [x] ✅ Menu codes listed — **C: 65/100**
- [x] ✅ Tables: BKBM\* (10 tables) — all 10 schemas extracted and field-level documented in tier1-tables.md; 5-table core schema cluster (BKBMMSTR/AMTR/EMTR/AVAL/SUMM all 26f identical), remarks/notes/dim/cnfg satellites fully interpreted; BKBMDIM (sheet cut dimensions) confirmed; BKBMCNFG flags documented; Pass 129 2026-06-19; all 10 DDF schemas confirmed byte-for-byte + BKBM_ line schema (26f) + BKBMERMK/REMK (20f, 15-remark pattern) documented in tier2-tables.md — Pass 142 2026-06-22 — **C: 88/100**
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
- [x] ✅ Source file: BKMRF.SRC fully re-analyzed (Pass 119): DO.SO/DO.PO/DO.WO/DO.WOBOM/DO.FC/DO.RLEVEL demand loading procedures confirmed; 4-stage MRP engine (START.MRP 1-4) confirmed; MTMRP 12 field names confirmed from SRC (PARTNO/DATE/KEY/ORDER/ACTION/PEGTO/QTY/PG.SDATE/PG.FDATE/STARTDT/PG.QTY/ONHAND); DDF confirms 13f — MTMRP_LOC(10) is the 13th (multi-location MRP, Pass 131); MTIC.PROD.MRP/TYPE/MRPSW flags confirmed; BKMRPSW 2f confirmed (PART+SW='Z'); BKICLOC opened for reorder level check — **C: 78/100**
- [x] ✅ Pass 45: All 17 T7MR* programs mapped (T7MRA through T7MRO). Full demand-to-release lifecycle: MR-A(forecast entry) → MR-F(explosion engine→MTMRP) → MR-G(firm, BKSBVEND/BKSBMFG select vendor) → MR-H(release→WORKORD+BKAPPO) → MR-I/IX(capacity scheduling with ROUTING+CALENDAR) → MR-J(PO/RFQ via BKRFQ 49f). MTMRP(13f) extracted: PARTNO+DATE PK, PEGTO(demand tracing), ACTION lifecycle. BKRFQ(49f): 10 qty/cost breakpoints, shared by both RF (estimates) and MR (MRP). CALENDAR(5f): SAT+SUN work flags. BKSBVEND(6f)/BKSBMFG(6f)/BKSBPART(5f): approved-source tables used by MR-G vendor selection — **C: 80/100**
- [x] ✅ Full MRP calculation cycle traced (T7MRF explosion → MTMRP → firm/release)
- [x] ✅ All core BKMR\*/MTMRP/support tables documented with fields; full field tables + MRP data flow diagram added to docs/03-modules/mr-mrp/README.md (Pass 110h 2026-06-19) — **C: 88/100**

### 7.10 Routing (RO)
- [x] ✅ Menu codes listed (19 operations) — **C: 65/100**
- [x] ✅ Source file: BKROA.SRC fully re-analyzed (Pass 119): ROUTING table opened + ~20 field names confirmed from entry procedures (DESC/LOTSZ/TYPE/ROUTNM/VEND/VNDCST/MCHCST/NUMPRC/TMPRC/PRTSHR/SETUP/POVLP/NOVLP/STDTIM/LOTSIZ/PERSON/TMACH/TOOL); BKRTEMTR confirmed (EDI import routing staging — used instead of ROUTING when cfrom='BKDEJC'); G.COPY.SPEC confirms routing spec copy path — **C: 75/100**
- [x] ✅ Pass 57: ROUTING/MTRO_(62f) fully extracted: CODE+OPER PK, TYPE/LEAD/PARTSHR/TIMEPART/SETUPHRS/LOTSIZE, 15×INSTR, WC+WCDESC, VENDCODE+VENDNAME, LABOR/MACHINE/FOVHD/VOVHD/SETUP costs, TMACHINE/TOOL, NUM/NUM_PERSON, OVERLAP/NEGOVLP, PIECE_RATE, LONGTIME, PRINT, CLASS, EXTRA(150), DEF_TIME, R_TYPE, EST_LINE/EST_TAG; BKRTCST(24f)=routing cost snapshot 10-break; BKRFQ(49f)=vendor RFQ per operation (subcontract quotes); 13 T7RO* programs mapped — **C: 85/100**
- [x] ✅ Pass 143 (2026-06-22): All 4 BKRT* DDF schemas confirmed byte-for-byte: BKRTEMTR(62f — routing estimate/template operation master: CODE+OPER PK, 15 instruction lines 900-byte, 5 cost categories LABOR/MACHINE/FOVHD/VOVHD/SETUP, WC+tool+vendor refs, EXTRA 150-byte blob; MTWO_ prefix typo on MISC_COST noted), BKRTSPEC(7f — routing spec notes: PART+SEQ+LINE PK, NOTE_1..4 STRING/20), BKRTTEMP(6f — routing template notes: CODE+LINE PK, NOTE_1..4), BKRTCST(24f previously confirmed); all documented in tier2-tables.md — **C: 88/100**
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
- [x] ✅ Tables: BKDC\* (7 tables) — all 7 schemas extracted and field-level documented in tier1-tables.md; 5-table identical 50-field LAB_* cluster (BKDCCLAB/BKDCLAB/BKDCPLAB/BKDCHLAB/BKDCTLAB); BKDCSHFT 34f (3-shift × 10 time boundaries); BKDCCFG 7f (timeouts + paths); full pipeline lifecycle documented; Pass 130 2026-06-19 — **C: 82/100**
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
- [x] ✅ Tables: BKPI\* (7 tables) — all 7 schemas extracted and field-level documented in tier1-tables.md; BKPIMSTR 3f session header; BKPIFROZ 19f frozen snapshot (dual GL account pairs for adj/clearing, LOT/SER tracking flags); BKPIPHYS 14f count tags; BKPILOT/BKPILCNT 10f identical lot mirror pair; BKPISER/BKPISCNT 10f identical serial mirror pair; variance post flow documented; Pass 130 2026-06-19 — **C: 82/100**
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
- [x] ✅ Pass 143 (2026-06-22): Full EST* family (estimating module) DDF schemas confirmed: ESTSUM(213f — quote header, PK=QUOTE FLOAT/8, 10-qty-break cost matrix × 14 cost types = 140 cost fields, 10 note lines, record=2465 bytes), ESTROUT(48f — quote routing op: QUOTE+OPER PK, 15 instruction lines STRING/60, 5-slot LAB/MACH/OVER/SETUP cost types, record=1219 bytes), ESTMAT(18f — quote BOM material: QUOTE+CODE PK, 8-decimal QTYPER, 5 cost types, 5 remark lines), ESTCHGS(3f — surcharges: QUOTE+AMT+DESC); all use MTE* field prefix (not BK*); BKMATCST(23f — 10-break material cost table) confirmed; DPTMENT(2f — DPT_CODE+DPT_DESC) confirmed; all documented in tier2-tables.md — **C: 82/100**
- [x] ✅ Pass 106: All BKES* tables fully documented in tier4-tables.md; BKESTQT/BKESTQTL = byte-for-byte BKARINV/BKARINVL clones confirmed from DDF; BKESTCFG 13f field semantics documented; ESTSUM 213f structure confirmed (MTESUM_ prefix, 10-qty-break cost matrix); full ES-A..M pipeline documented — **C: 78/100**
- [x] ✅ Pass 155 (2026-06-22): All 6 ES sub-form DFMs confirmed. T7ESB=Print Estimates (SO/cust/class/job ranges; ISPRT.NOTES/KIT/ECO/xref; PLDTYPE=YES/NO/PARENT/COMPONENT). T7ESC=Print Estimate Detail (quote range; PRINT.REPORT[1..10] qty-level selectors; Summary Only; BOM/routing/extras). T7ESD=Print Customer Quotes (quote/cust/expiry ranges; qt.status AICXD; ais.dec price precision; PLDTYPE Y/N/P/C). T7ESE=Convert Estimates (sFROM.QUOTE; ISTO.SO/ISTO.WO; lines grid APART/AQTY/APRICE/AESD/AWSD/AWFD; ISUPD.CONTRACT; per-line ORD.QTY/SELL.PRICE/START.DATE/FINISH.DATE/ESD.DATE; btnConvert Visible=False). T7ESH=Enter Material Costs (BKMC.CODE; BKMC.QTY[1..5]/BKMC.COST[1..5]; MTIC.PROD.VEND[1] vendor ref). T7ESI=Print Material Costs (from/thru item + from/thru date). AICXD status codes confirmed from AllowedChrs field — **C: 78/100**
- [x] ✅ Pass 42: Full ISES\* family (10 tables) extracted. ISESTHDR(84f)/ISESTLNE(28f) = BKARINV/BKARINVL ES current views. ISESAHDR/ISESALNE + ISESTAQT/ISESTAQL = archive alternate indexes (same structures). ISESTDTL/ISESADTL(203f, identical) = estimate detail: IS_EST_NUM+PART+LINE PK; 10 qty-break × material/labor/overhead cost columns. ISESTASM(213f) = DBA/MT-era estimate assembly summary: MTESUM_QUOTE(8) PK + DATE/EXPDATE/STATUS/CLASS/CODE/DESC/UM/CUSTCODE+NAME+ATTN+RFQ/REV/PROJ + QTY_1..10 + MAT_1..N (213 fields total, MTESUM_ prefix confirms MT generation — predecessor to BKESTQT). ISESTPO(16f) = ES→PO link: BKMRP_PO_* fields (same as BKSOPO). Unified architecture confirmed end-to-end: ES quotes through archive through estimate detail — **C: 72/100**
- [x] 🔄 Pass 50: T7ESA (15p) FOUND — opens BKBMMSTR+BKICMSTR+BKMRPFC+DBAFIFO; T7ESB(213p)/ESC(124p)/ESD(162p)/ESE(194p)/ESH(60p)/ESI(94p)/EST(163p) all mapped; BKMATCST(25f: CODE PK, 10×QTY_N+10×COST_N+MIN+MINCST+DATE) material cost; BKRTCST(24f: QUOTE+CODE+OPER PK, 10×PARTSHR_N+10×SETUP_N) routing cost; BKMRPFC(9f: PART+DATE PK, QTY+OQTY+CQTY+FLAG) MRP forecast demand; ESTSUM = DDF table name for ISESTASM(213f); ES-C uses BKRFQ for vendor cost — **C: 72/100**

### 7.18 Remaining Modules (not yet deeply documented)
The following modules have menu codes and forms inventoried but no deep logic documentation:

- [ ] ⬜ **AB** — no T7 RWN/DFM files found (DBA-era legacy code, unimplemented in TAS Pro 7)
- [x] 🔄 **AC** — Activity Control / NCR tracking — 3 DFMs + 5 RWN modules (T7ACTION/ACRDTYPE/T7ACDET/T7ACDATE/T7ACCNFIX); WODATE(13f) all fields var-confirmed (Pass 116): WOPRE+WOSUF PK, START/FINISH/QTY/PARPRE/PARSUF/TOPPRE/TOPSUF/DELPRE/DELSUF/PRIO/EXTRA; **ACDETAIL 17-field schema extracted from T7ACDET vars (Pass 116, 2026-06-19):** ID+LINE+PART+QPERF+QPERT+OPER+UM+ACTION+REFDES+LNOTE+LQTCOST+LQTDATE+ACTCOST+TOTBUY+CNEED+CUSTPART+TYPE (Btrieve-only, not in DDF); ISACTION(3f: TYPE+DESC+MISC) extracted; T7ACTION (53p, 14 tables): ISACTION+BKARCUST+BKAPVEND+BKCMACCN+BKICMSTR+ISLINKS — action master with entity cross-ref; T7ACDATE (64p, 16 tables): WODATE+WORKORD+MTICMSTR confirms WO hierarchy traversal; T7ACCNFIX (28p, 6 tables): BKCMACCN-only fixer (BKCM.ACCN.* vars: CODE/CONT/TITLE/PHONE/EMAIL/DATE1/DATE2/ALPH1/ALPH2/CON/PRIM/PHLBL/EMLBL/MSLBL/DTLBL/M2LBL/D2LBL) — **C: 75/100**
- [x] 🔄 **AM** — Accounting Maintenance (NOT Asset Management — CORRECTED) — 5 forms read (GL period control, account history, account entry, dept copy/delete, financial statement format) — **C: 75/100**
- [x] 🔄 **AD** — Accounting Defaults — CHM fully documented (AD-A GL defaults with 20 accounts + 5 posting flags + 6 period-date controls, AD-B checking account setup with 16 fields, AD-C AP defaults with 11 behavioral flags); RWN programs: T7MDEFAULTS (435 procs, main — opens BKSYMSTR+BKYSMSTR+ISBANKS+42 more tables), T7MDEFBANKS (79 procs, AD-B bank setup — BKGLCOA+ISBANKS), T7MDEFNDC (252 procs, extended module defaults — BKSYAP+BKESTCFG+BKFOCFG+BKCPMSTR+BKCMCNTD); primary tables: BKSYMSTR(286f full schema extracted Pass63: auto-numbers/company/20terms×6arrays/9banks×6arrays/all GL accounts/aging buckets/feature flags/173 EXTRA), BKYSMSTR (YN flags), ISBANKS (checking accounts); **Pass165 T7MDefNDC: 73 unique BKSY.* field-access vars** = complete BKSYMSTR namespace confirmed: auto-numbers (ARINV.NUM/APINV.NUM/APPO.NUM/GJ.NUM/ARSO.NUM/CHK.NUM/AR.RECNUM/AP.RECNUM/GJ.RECNUM/AP.RECVNUM), company (COMP.NAME/ADD1/ADD2/CSZ), terms (TERMS/TRM.AMT/TYP/DAY/EOM/MAX/DISC), GL clearing (GL.CLRING/GLDPT.CLR), GL retained-earnings (GL.RETEARN/GLDPT.RET), GL related-year (GL.RELYR/GLDPT.RELY), GL AR-interest (GL.ARINTR/GLDPT.ARIN), AR GL (AR.GLACT/GLDPT/DISCGL/DISCDPT/FREIGHT/FRGTDPT/CHKACT/AGING/INT.RTE/INT.DAY), AR defaults (AR.SHP.VIA/SLSP/ENTBY/TAXABL/ENDDESC/TURNOFF/PEL), AP GL (AP.GLACT/GLDPT/DISCGL/DISCDPT/CHKACT/AGING), AP defaults (AP.SHP.VIA/ENTBY/PEL/ENDDESC/REOPEN/RQSCRAP/RQREWRK/RECVFLG/PONUM/QCRECV/RFQNUM/VPRICE/PERCOVR/CONVDTE), PO GL (PO.TAXGL/TAXDPT/FREIGHT/FRGTDPT/RNI/RNIDPT/INR/INRDPT), TAX GL (TAX.GLACT/GLDPT/RATE), check/banking (CHK.BAL/NAME/CHKACT/CHKDPT/CHKCUR), PR (PR.CHKACT/PR.ODNAME), flags (AUTO.BO/RTS.DEF/PLAIN.INV/PO/STMT/CHKS/FORM.CMPNY/TAL/EXTRA), fiscal/path (FISCAL.YR/PRGS.WHR/HELP.PATH); IS.* module flag set (IS.TAX/MULTI.CURR/LANDED.COST/UPC/RETAIL.PRICE/COMM.PRICE/IMAGING/EZPAY/RMA/SPEC.SUP etc.); BKEST.CFG.NUM/STAT/CLASS = estimating config; BKCMCNTD/BKCMSBDF/BKCMREP = CRM companion tables — **C: 83/100**
- [x] 🔄 **CM** — CRM/Contact Manager — T7CMA + 4 sub-forms read; CRM-AR bridge confirmed; 9 emails/contact (BKCM.ACCN.EMAIL[1-9]); contact title/primary flag; key dates (BKCM.ACTD.*); account classes; territory/SIC/lead-source; BKCM.* (46 tables); detailed findings at Pass 53 entry below; 41/46 BKCM* DDF schemas confirmed + all documented in tier2-tables.md (BKCMACCN 154f, BKCMACTH 21f, BKCMMHST 72f, BKCMDUN 36f + 36 more tables) — Pass 142 2026-06-22 — **C: 85/100**
- [x] 🔄 Pass 53: All 37 BKCM* tables field-extracted; 6 T7CM* programs fully mapped; 3-entity architecture confirmed (BKARCUST customers + BKCMACCT prospects + BKCMPCNT contacts); BKCMACCT(41f: CODE+NAME+ADDR+REP+SICCD+CUST+LEAD+TERR+CCARD+EMAIL+EMPS)+BKCMACCN(154f: 10×CONT/TITLE/PHONE/DEAR/EMAIL+labels+UDF dates/alpha)+BKCMACTH(21f: history with start/stop/MIN/BMIN/RATE/AMT/BALNC billing)+BKCMACTF(11f: follow-up+SO link)+BKCMHCOD(9f: event codes+rate+BPART billing parts)+BKCMREP(14f: VIEW/CHANGE/GWARN/AADD flags)+BKCMTERR(11f)+BKCMMHST(72f: campaign with 20-class include+20-class exclude+9 range filters)+BKCMDUN(36f: 10-level dunning ladder)+BKCMDUNH(6f)+ISREMIND(22f: system-wide calendar with cust/vend/item links+email+FILE attachment)+MKAHIST(9f) all extracted; BKCMDE+BKCMEACT confirmed as DDF alt-key views of BKCMACCT (not separate tables) — **C: 82/100**
- [ ] ⬜ **CP** — no T7 RWN/DFM files found (DBA-era legacy)
- [x] 🔄 **CR** — Contract Review / SO Approval — T7CTREVU(96p, 35t); Pass164 vars: SFROM/STHRU.SONUM + FROM/THRU.ORDDTE = SO number + date filter; CT.DEPT/CT.ADMIN/CT.EMPNAME/CT.LEVEL = approver credentials (confirm ISCTREVU DEPT/ADMIN/LEVEL/EMPNME fields); CT.PASSWORD/ENTER.PSWD/CONF.PSWD/DISP.PSWD/OLD.PSWD/PSWD.ATTEMPT = password authentication; OLDPASS/NEWPASS/REENTPASS/OKTOSAVE = password change workflow; RESET.PSWD/FIRST.SAVE/NEW.EMP = admin reset path; HOLD.AMT = the SO dollar amount being reviewed; PRMSTR.H = permission master handle (BKPSUSER lookup); ISCTREVU(17f) schema confirmed; ISSOREVU(12f); password rotation fully documented — **C: 80/100**
- [x] 🔄 **CC** — Credit Card Processing ⚠️ (NOT Cycle Count — CORRECTED) — all 6 DFMs read; CC-P (IS.CC.MASKED/CARDNAME/EXP/ZIP — masked card storage with expiry flag), CC-PO (CC charges on POs: ccnum/ccamount/CCYY/CCMM), ccr1 (Credit Card Invoice List report by date/terms), CC-DE (CSV import); WO and item range filters confirm cost allocation to jobs; Pass 44: ISCC(14f) fully documented: CODE(10) PK + TOLKEN(20, vault token, NOT raw PAN = PCI-compliant)+MASKED(24)+EXP(4)+ADDRESS(40)+ZIP(10)+CARDTYPE(15)+CARDNAME(25)+STATUS(25)+STDATE+XCTRAN(10)+EXTRA(100)+PROCESS(10, processor code e.g. "AUTHORIZE") — **C: 72/100**
- [x] 🔄 **CS** — Commission/Salesperson Management — all 12 DFMs read; CS-A (BKPR.SLS.* fields: rate/HOW/WHEN/class/GL/agent-vendor), CS-B (quota/COGS/comm-due/paid[1-7]), CS-D (transfer commissions: BKPR.COMM.SLSP/CCODE/INVNM/INVDT), CS-E/F (detail+summary reports); outside agents linked to AP vendor — Pass 57: 17 T7CS* programs fully mapped; BKPRSALE(87f)+BKPRCOMM(12f, fully extracted)+BKPRAGNT(4f)+BKPRMSTR(384f employee/payroll master)+BKPRCURP(127f current payroll period)+ISREPLNK(11f rep-to-customer link) all extracted; HOW (`S`=sales%, `G`=gross margin) and WHEN (`I`=invoice, `P`=payment) logic confirmed from field names; **Pass165 T7CSO (168p, LISTG60.LIB)** = Commission SO report: SFROM/STHRU.SLSP+FROM/THRU.SLSP salesperson range filters; 3 independent date-range filters: FROM/THRU.CDATE (close date)/DDATE (delivery date)/TDATE (transaction date); 3-tier color-coded class display: COLOR.CL1/2/3+CLASSCL1/2/3; commission summary vars: OT.COMM/ARC.COMM (on-target vs. actual commission), TOT.AMT.PD/TOT.FRT.AMT/TOT.COMM.DUE/RPT.COMM.DUE/RPT.FRT.AMT; uses BKPRSALE+BKPRCOMM+BKPRAGNT (agent table) — **C: 84/100**
- [x] 🔄 **DE** — Data Entry / EDI / Imports (20 DFMs, 33 ops); Pass 116 ASN family confirmed: T7DEP860 (82p, EDI 860 PO changes — BKGLX+DBAFIFO+BKGLTRAN), T7DEPB (111p, EDI 856 ASN shipment build — BKARINV+BKYSMSTR+BKEDMSTR+BKEDIDUN+BKARCUST+BKARINVL+ISSRINFO), T7DEPC (15p, ASN cost post — BKGLX+DBAFIFO+BKGLTRAN+TASCOLOR+ISGLDATE), T7DEPD (132p, ASN pack/carton build — ISBUILD+BKICLOC+BKICLOCM+ISACCESS), T7DEPE (114p, ASN dispatch/compliance — ISBUILD+ISAREX+BKARCUST), T7DEPF (104p, ASN box confirmation — ISSOBOX+ISAREX), T7DEPH (116p, EDI receipt/PO match — BKAPPOL+BKICPMAT); **ISBUILD (new table, Pass 116):** opened by T7DEPD+T7DEPE — carton/pallet build assembly for ASN; not in DDF; T7DEP860 also opens BKGLX (GL extended — also seen in CU module); full BOM component/PI/WO/AR import programs + 33 original ops unchanged; BKEDIH(84f)+BKEDIL(28f)+BKEDMSTR(3f)+BKEDNOTE(3f)+BKEDIDUN(7f)+CCEDIXRF(6f)+ISEDINFO(54f)+ISDEFECT(3f) all extracted — **C: 82/100**
- [x] 🔄 **DI** — Digital Signatures — T7DIGSIG.DFM (131KB) confirmed: Caption='Enter Digital Signatures'; T7DIGSIG.RWN (128p, 27 tables, Pass 116): BKAPPO+BKAPPOL+ISDIGSIG+BKPRMSTR+ISTRIGRS+BKPSUSER+ISTERMS+ISREMIND+LOT+SERIAL+ISNCR+BKSYMSTR+FILELOC; far larger than the 3-program estimate — full PO approval workflow; EMAIL.TAG/NAME/LEVEL/ADDRESS vars confirm email routing; BKAP.PO.* vars (NUM/VNDCOD/VNDNME/SUBTOT/TAXAMT/TOTAL/ORDDTE etc.) = full PO header displayed in signature form; LOT+SERIAL+ISNCR = digital signatures extend beyond PO to lot/serial and nonconformance records; ISREMIND = approval reminders created; ISDIGSIG(89f fully documented): 10 approval slots × ACTIVE/TYPE/SDATE/FDATE/TDATE/AMT/FLAG/DATE + MOTCACH/POENTBY/SOENTBY/FILE/ATIME/ADATE; T7DigSigChgPSWD = password change utility; ISTRIGRS(25f) = email notification triggers — **C: 75/100**
- [x] 🔄 Pass 55: ISDIGSIG(89f) all fields confirmed; approval workflow traced (BKAPPO→ISDIGSIG slot→ISTRIGRS email→BKGLTRAN on approve); 10-slot structure fully understood (TYPE=approval class, SDATE/FDATE=valid period, AMT=dollar limit, TDATE=last-used date, FLAG=current status) — **C: 72/100**
- [x] 🔄 **EX** — SQL Export / BI Export — Pass 156 (2026-06-22): SQLEXPORT.RWN + SQLEXPORT.DFM (T7JTemp Java loader, Caption='Loading....', SourceFile='T7JTemp') + SQLExport.jar (com.evoerp package, v1.5.0 build 2014-03-19); Java Swing app connects via Pervasive JDBC to EVOBI2 database (separate BI DB, NOT operational DBAMFG$); Pervasive port 1583; exports CSV to \\I2S109-SOLIDCRM\DBAMFG$\REPORTS\; key classes: PervasiveDatabase+TextExportingWorker+FileOpeningWorker; logs to DBAMFG$\logs\SQL Export.log; same T7JTemp launcher architecture as QU-F (EvoPVT.jar); EVOBI2 schema/SQL queries not decompiled — **C: 45/100**
- [x] 🔄 **FA** — Fixed Assets — all 3 DFMs read; FA-A (IS.FXA.* asset master: cost/residual/life/method/GL accounts), FA-B (IS.FXT.* depreciation: post with Ready-to-Post flag), FA-E (export); Pass 65: ISFXASST(23f fully extracted: NUMBER PK+TYPE+DESC/DESC2+CSTBAS+RESVAL+LIFE+METH+GLA/D+ACDEPA/D+DEPEXPA/D+SDATE/EDATE+SOLD+ACCUMDEP+SERIAL+LDEPAMT/LDEPPERC/LDEPDATE+EXTRA), ISFXATRN(12f: NUMBER+DATE PK+AMOUNT+PERC+AUDIT+POSTED+ACDEPA/D+DEPEXPA/D+NETAVAL+EXTRA); depreciation GL flow confirmed (ISFXATRN.POSTED→BKGLTRAN); IS.FXA.*=ISFXASST, IS.FXT.*=ISFXATRN confirmed — **C: 82/100**
- [ ] ⬜ **FL** — no T7 RWN/DFM files found (DBA-era legacy)
- [x] 🔄 **FO** — Features & Options — 5 programs: T7FOA/B(5p stubs), T7FOC(60p BKBMMSTR+BKICMSTR — option entry), T7FOD(103p item+class range filter), T7FOE(86p item filter); BKFOCFG(18f: MANFET+YN_1..15+OPCODE) is the FO config table; BKBMMSTR(26f Pass 64: PROD_OPYN_1..6 decoded); Pass 65: ISFOHEAD(16f: UID PK+PARENT+DATE+DESC+CUST+VEND+RFQ+STATUS+REV+MDATES_1..5+PERM+EXTRA)+ISFOLINE(78f: UID+LEVEL+50×OPFLAG+PARENT+COMP+QTYREQ+OPYN_1..6+PRICE+PBRANC/CBRANC)+ISFOORDL(18f: UID+TYPE+PCODE+PQTY/PPRCE/PDISC/PEXT+ESD+LOC+TXBLE+UM+LN+DRAW+REV+LINE+OUID) — FO order lifecycle confirmed: customer config→ISFOHEAD+ISFOLINE→ISFOORDL output→BKARINV SO; BKLUGRID fingerprint includes ISFOHEAD+ISFOORDL+ISFOLINE confirming they're queryable in the lookup framework; Pass 154: T7FOC DFM fully read — OPYN[4]="Use STD Customer Pricing?", OPYN[5]="Add Price to Parent?" exact label names confirmed; BKBM.PROD.PRICE=$,0.0000 format; from.item=Feature item (not range-start), thru.item=Option item (not range-end) — naming quirk confirmed — **C: 80/100**
- [x] 🔄 **FP** — Features & Options Print — CHM confirmed: FP-B='Print Features and Options'; zero T7FP* programs (FP uses T7FO-labeled programs for printing); Pass 156 (2026-06-22): T7FOD (103p, EVO.LIB) + T7FOE (86p, EVO.LIB) DECRYPTED + SYMBOLS EXTRACTED; identical 18-table DB fingerprint: BKICMSTR+MTICMSTR+BKBMMSTR+BKICLOCM+CLASMSTR+BKSYHELP+DBAHLPID+ISIS+MKAHIST+ISLOG+ISDRILL+BKAPVEND+BKARCUST+BKCMACCN+ISLINKS+BKAPDESC+LANGDICT+FILELOC; key vars: CFG.RTM.NAME / RTM_NAME / RTM.NUMBER — RTM is runtime-configurable (not hardcoded); both are FULL print programs, not stubs; T7FOD=item+category+class range, T7FOE=single item; MTICMSTR confirms FP can print from both production and estimating inventory — **C: 72/100**
- [x] 🔄 **HH** — Handheld / Shop-Floor Data Collection (44 forms) — 20 key DFMs read; 9 sub-areas: PO Receiving (hhpoc/POCBIN/POCLot/POCSER), WO ops (wog=issue, wop=finish, WOSCRAP, WOLabel, woser), SO shipping (SSOE 5-form verification chain, SOLookup, SODD), Inventory (ItemLU/INGA labels/hhinlj transfer/INLJLot/INLJSer), DC labor scan (HHDCA=scan.wo/scan.emp/OPER), PI tag count (HHPIC/hhpictags with lot/serial), alerts, batch process; large.lookups dual-mode; item type filter RFAMNLBTKO; Pass 48: 30+ T7HH* programs fully mapped across 9 sub-areas; BKDCLAB(50f) complete: DATE+EMP+WOPRE+OPER PK, START/FINISH+PARTS+SCRAP+RUNHRS+5 scrap codes+LAB_JCNUM(12)→JC link; BKDCSHFT(34f): 3-shift schedule with 2 breaks+lunch per shift; BKDCCFG(7f); ISSOBOX(22f): SONUM+LINE+BOX PK, UCC+TRACK+dimensions; BKARTXN(14f): AR shipment with LOT+SERIAL+LOC+BIN; BKICREF(8f): customer part xref; ISAREX(51f): AR compliance/certifications — **C: 80/100**
- [x] 🔄 **IC** — Inventory Control utility — T7IC2EST (6 procs, BKICMSTR+MTICMSTR): one-way bridge copies production inventory to ES estimating module; accessed as IC-A "Copy Production to Estimate Inventory"; MTICMSTR(108f) fully extracted: 10 vendor sources (VEND_1..10+VNAM+VPC vendor part codes), RCOST_1..15 received cost slots, 5 substitutes, LOTSZ, option flags, UIQC/UIWIP; **Pass166 J7TMCKanban (232p, 59dbs)** = Kanban replenishment hub: triggers on below-reorder-level signal → opens BKRFQ (creates vendor RFQ) + BKQCMSTR (incoming inspection) + BKPRMSTR (contact); **BKIC.PROD.* 65-field access namespace confirmed**: CODE/DESC/TYPE/UM/CAT/CLASS/TXBLE/TAXIN/ISUPC/PRICE/LONGP + costs: LSTC/AVGC/PMAT/AVMAT/AVLAB/AVOP/AVSET/AVVO/AVFO + quantities: UOH/UOO/UOSO/UBO/TOTVL/TO + reorder: RLVL/RAMT + dates: LSALE/LORD/LRCPT + sales MTD/YTD/LYR/VAR: USMTD/USYTD/USLYR/USVAR + GSMTD/GSYTD/GSLYR/GSVAR + NSMTD/NSYTD/NSLYR/NSVAR + CMTD/CYTD/CVAR + NGMTD/NGYTD/NGLYR/NGVAR + GL: GLA/GLC/GLS/GLSNT + DPTA/DPTC/DPTS/DPTNT + misc: EXTRA/NOTE/MANUF/ADTR/CLYR/CVAR; **BKIC.LOC.* 22-field access namespace** (BKICLOC): KEY/CODE/PROD + quantities: UOH/UOO/UOSO/UBO/UOWO/UWIP/UALLOC/UIQC + GL per location: GLA/GLC/GLS/GLSNT/GLWIP + dept: DPTA/DPTC/DPTS/DPTSNT/DPTWIP; **BKIC.LOCM.* 13-field access namespace** (BKICLOCM): CODE/NAME/ADDR1/ADDR2/ADDR3/CITY/STATE/ZIP/TAX#/CNTCT/PHONE/FAX + TAX# (13); **BKIC.IS.DCODE** = item-specific detail code link — **C: 79/100**
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
- [x] ✅ Pass 143 (2026-06-22): Menu-level security tables confirmed from DDF: BKSLEVEL(422f — PK=MENU UBINARY/2+LEVEL STRING/2; 20 menu groups × 21 flags each = 420 flags + 2 PK = 422 fields, record 424 bytes; flag pattern MENU_K_YN + MENU_K_1..20 for 400 individual menu-item access control points per level), BKSLMSTR(2f — LEVEL+DESC, one record per defined security level); BKLOGON(10f — active session: CODE+PSWD plaintext+CMPY+PROG+PRINTER+INUSE+SCRTY→BKSLMSTR+MENU+SUBMENU+CURPRT; INUSE flag prevents duplicate logins); two-tier security: BKLOGON links session to BKSLEVEL for menu access, BKPSUSER for program-level access; all documented in tier2-tables.md — **C: 78/100**
- [x] 🔄 **QC** — Quality Control — 18 programs across 4 sub-areas: (1) QC-A/B/C/D inspection (T7QCA 106p incoming, T7QCB 120p WO material, T7QCC 108p WO receipt, T7QCD 117p WO routing); (2) QC-F NCR (T7QCFA 178p entry, QCFB 108p supplier quality, QCFD 53p inquiry, QCFF 131p closeout); (3) QC-G CAPA (T7QCGA 212p corrective action entry, QCGB 122p team approval, QCGD 110p report); (4) Support (T7QCMTHD 65p methods, QCRESULTS 104p results, QCRSLT 87p tray results, QCSPEC 82p spec def); key tables: ISNCR(35f), ISQCSPEC(57f), ISQCMTHD(44f), SCRAP(21f), ISWOTRAY(52f), QCCODES(2f), ISCACT/ISCARDTE/ISCTEAM (not in DDF); Pass 47: ISNCR(35f) fully extracted all 35 fields (PART+COMP+LOT+SERIAL+DCODE+DISP+CAR+VEND+WO/PO/RMA links), BKQCMSTR(14f receiving master) + BKQCTRAN(21f transaction log) both extracted; **Pass166 T7POJC (323p, 59dbs) = J7/J-era PO receiving + QC inspection hub**: **BKQCMSTR 20 access-var names confirmed**: VKEY/DKEY/PKEY/RKEY/IKEY (composite key parts); VEND.CODE/RECV.DATE/PO.NUM/RECVR.NUM/POL.ITM.NO (vendor/date/PO/receiver/item keys); PKSLIP.NUM/PKSLIP.QTY (packing slip); QTY.RECVD/QTY.BUYOFF/QTY.REJECT/QTY.NCR (receipt qty breakdown); PROD.CODE/UNIT.COST/OUT.DATE/EXTRA; **BKQCTRAN 26 access-var names confirmed**: BKQC.TRN.PO/VEND/CODE/RECNUM/RECVNM (PO/vendor/receipt keys); BKQC.TRN.BQTY/NQTY/GQTY/UQTY/POQTY (bad/no-action/good/usable/PO qtys); BKQC.TRN.SCRAP/REWORK/FIXQTY (disposition qtys); BKQC.TRN.FAULT/NCR (NCR link); BKQC.TRN.FLAG/GEN/BROKEN/INVCD (flags); BKQC.TRN.ARDTE/BODTE/PODTE/DATES (arrival/buyoff/PO/txn dates); BKQC.TRN.EMPNUM/NUMS/EXTRA; BUYOFF.REMAIN/EMPNUM = inspection session vars; AC.MST.* vars (AEGIS/AINTERNA/AIQ/APROD/APROG/APURCH/AQUAL etc.) = ISCACT/ISCCAR corrective action master approvals — **C: 84/100**
- [x] 🔄 **QT** — Service Quote extended info (linked to SR module) — T7QTINFO (42 procs): opens ISSRINFO+BKYSMSTR+BKARINVL+ISTERMS+BKICPMAT+LANGDICT+BKICREF+BKPRSALE; service quotes are SR orders in quote status (BKARINV); T7QTINFO = extended info entry analogous to T7SRINFO; LANGDICT(5f)=translation: ECAPT+LANG PK → LCAPT(80)+FONT(30)+EXTRA(150); BKICREF(8f)=customer part xref: CUST+CODE PK → CUSNME(30)+CUSCOD(25 customer part number)+DESC/DESC2; ISTERMS(13f)=payment terms: NUM PK+NAME(20)+DESC(50)+AMT+TYP(P/%/$)+DAY+EOM+MAX+COD+ARAP+CC+SRT+EXTRA — all schemas extracted — **C: 72/100**
- [x] 🔄 **QU** — Query / Inquiry Tools — CHM fully documented (6 ops); RWN programs: WBKLOOKUP (413 procs, QU-A universal lookup grid — opens BKLUGRID+ISDRILL+ISDRILLM+FILEKEY+FILEDICT), CALDRILLBT (94 procs, QU-B calendar drill-down — same date vars as CALREM: ISTS.EDATE/ENTRY.DATE/DATE_TYPE/MM/DD/YY/START.DATE; bridges CALREM↔EvoDrillDown; opens ISDRILL for drill-down config, Pass 114), EVOBS (128 procs, QU-D Business Status — opens ISBSF+BKGLTRAN+MTICMSTR), T7QGRID (62 procs, QU-E Quick Grid Lookup — opens BKLUGRID+ISDRILL), QUERYEXECUTE (26 procs, QU-F — confirmed EvoPVT.jar launcher stub (Pass 114, 2026-06-19): same HOST/NAME/PORT/TREEDEST/COMP/NOPE/DUMMY_L/DFM vars as CashFlow/CommissionRpt; QU-F SQL execution happens entirely inside EvoPVT.jar Java layer; ISDRILL+BKPSUSER = drill config + access gate); ISDRILL(46f) full schema extracted: LOOKUP_FROM(30)+GRID(15)+REC(4)+KEY(2)+FILE(15)+FILTERS_1..20(80×20)+WHILE_1..20(80×20)+COMM(150); ISDRILLM(17f): PARENT+CHILD+MENU+FILE+SFIELD_1..5→TFIELD_1..5+KEY+PFILE+EXTAR(150); **BKLUGRID 14-field schema extracted from EvoERPDrillM LUGRID_* vars (Pass 115, 2026-06-19):** LUGRID_NAME+LUGRID_FDNAME+LUGRID_FORM+LUGRID_KEYFLD+LUGRID_KDATA+LUGRID_DATA+LUGRID_TEXT+LUGRID_EXTPARM+LUGRID_EXTRA+LUGRID_EXTUDF+LUGRID_END+LUGRID_PROT+LUGRID_DELFLAG+LUGRID_HNDL — grid layout config table (column defs + key field + display text + UDF extensions); resolves the last "runtime-only table" gap for WBKLOOKUP fingerprint; WBKLOOKUP total DB fingerprint=76 tables (70 in DDF; 6 runtime: BKLUGRID✓+FILEKEY+FILEDICT+FILEDFLD+FILEKNUM+FILELOC); **Pass165 FILEDICT API field-access vars confirmed**: FD_FIELDNAME/KD_FIELDNAME/KD_KEYNAME = field+key names; FD_COLHEADER/KD_COLHEADER = column display headers; FD_TOT/FD_SSSFD/FD_FUNC/FD_TYPE/FD_SIZE/FD_EDIT = field attributes (total flag, sub-sort field, sort function, data type, size, edit mask); control vars: FINDVAL/LU_EDIT_SCRN/CBINDEXNAME/CURRENTFASTSRCH/LU_CONTROL_FLD/LUGRID_HNDL; result/data: LK.WHO/LK.EMPTY/LU_RESULT/KEY.REC/DREC (record handles); resource handles: NOTES.H/LINKS.H/DRILL.H/DRILLM.H (notes/links/drill-down/drill-master); path/session: ISTS.PATH/DD/DU/BLANK — WBKLOOKUP dynamically reads any Btrieve table schema via FILEDICT/FILEKEY and presents in grid (FD_* = column defs, KD_* = key defs) — **C: 88/100**
- [x] 🔄 **RF** — Request for Quote (T7RFQ: 103 procs); opens ISESTDTL+MTICMSTR+BKBMMSTR+BKICMSTR+BKMRPPO+BKAPPOL+BKAPVEND+BKAPPO; ISESTDTL(203f) fully decoded: IS_EST_NUM+PART+LINE PK; 10 qty breaks × 18 cost types (MAT/MATMU/LAB/LABMU/SETUP/OP/OPMU/OH/OHMU/MISC/EXTRA/MEMU/OVALL/TOTAL/PRICE/COST/VOVHD each ×10) + SETMU + scalars (STATUS/DRAW/REV/CUST/ORDDESC/ORDDTE/EXPDTE/LOSTDTE/SO/WOPRE/WOSUF); bridges ES estimate to vendor RFQ to PO; BKMRPPO→BKAPPO link confirmed — **C: 75/100**
- [x] 🔄 **RM** — Return Material Authorization (RMA) — all 5 DFMs read; Pass 66: 4 programs confirmed: T7RMD(216p main entry: BKARINVL+ISRMAI+ISRMAC+BKARINV+ISNOTES+ISLINKS+ISNCR+SCRAP), T7RMG(132p report: BKARINV+ISRMAI+BKICMSTR+BKARCUST), T7RME(54p reason code master: ISRMAC), T7RMB/C(5p stubs); ISRMAI(54f Pass 66: NUM+PART+LINEID PK+DATE/RCPT/CLOSDATE+STATUS+REASON+DISP+OSONUM/OINVNUM+SONUM/INVNUM+CMNUM+REORDER+WOPRE/WOSUF+WARRANTY+WO/CR/SO/STOCK/SCRAP/SR/REFUND flags+FLAGS_1..20)+ISRMAC(3f: CODE+DESC+EXTRA); complete disposition flag set fully decoded — **C: 78/100**
- [x] 🔄 **RT** — **CORRECTED Pass164**: NOT a Report Template Validator — T7RTMVALID is the **EvoERP Runtime License Validator** (src=NZLICE.LIB = NZ License library); 4 own DB files: BKSYHELP+DBAHLPID+ISIS+MKAHIST; license vars: SERIAL/PRODUCT/APROD (license serial#, product code, active product), SDATE/EDATE (license start/expiry dates), SMM/SDD/SYY+EMM/EDD/EYY+XMM/XDD/XYY (start/expire/current date components), USERS (max licensed user count), SER5/SER6/SCBUFF/LIC/XDBUFF/USBUFF (license key buffers); EVOONLY (EvoERP-only license flag); CHKSUM/BIGSTR (checksum verification); SF.H (SysFile handle = license file); reads ISIS and sets 12 module license flags: ISIS.TAX/ISIS.TAX.IN/ISIS.TAX.FRM/ISIS.TAX.PO/ISIS.MULTI.CURR/ISIS.MULTI.CPAY/ISIS.LANDED.COS/ISIS.UPC/ISIS.RETAIL.PRI/ISIS.COMM.PRICE/ISIS.IMAGING/ISIS.AUTO.TAX; working copies: IS.TAX/IS.MULTI.CURR/IS.LANDED.COST/IS.UPC/IS.RETAIL.PRICE/IS.COMM.PRICE/IS.IMAGING/IS.UPC.1/IS.DEMO/IS.UPC.2/IS.MULTI.CPAY/IS.PIC.PATH/IS.TAX.FRM/IS.PO.TAX/IS.TAX.IN/IS.TAX.CVT/IS.CUR.CVT/IS.AUTO.TAX.CAL; module gates: IS.EZPAY/IS.RMA/IS.SPEC.SUP/IS.SPEC.SUPF/IS.SPEC.SUPT; MK.H/MKAHIST.* = license event logging; OVL_HNDL/OVL_PATH = overlay/module loading; NZCT/ALEN = NZ lib return codes; 8 tax/currency handles from T7MDefaults session (same pattern as all modules) — **C: 82/100**
- [x] 🔄 **SA** — Sales Analysis (13 ops) — 13 RWN programs fully identified: T7SAA(212p main engine: BKARINV+BKARINVL+BKARCUST+BKICMSTR+ISARCHG+ISSOBOX+BKPRSALE+ISJOB+CLASS+ISAREX); T7SAB/C/D/E/G/H/I/J/L (all 5p, range filter stubs, same table set as SAA); T7SAM(238p: BKSAREPT+BKACTRPT+ISBUILD+BKARINVL+BKARINV+BKICMSTR+ISRMAI+ISSRINFO+WORKORD+BKCMLEAD+BKCMTERR); T7SAN(220p: same as SAM excluding ISRMAI); T7SAO(169p Top N: BKCMACCL+BKCMACCC+ISAREX); T7SAP(131p class range: CLASMSTR+ISCATMST); T7SAQ(95p actual margin: WORKORD+WOMAT+WOBOM — uses actual WO costs); dedicated tables: BKSAREPT(57f full schema extracted: TYPE+NAME PK, RTM + 26 FROM/THRU range pairs covering inv#/dates/ship dates/amounts/salesperson/customer/class/category/part/lot/territory/currency), BKACTRPT(53f full schema extracted: TYPE+NAME PK, RTM + named FROM/THRU pairs for PART/CLASS/CAT/DATE/LOC/WO/CUST/INV/QC/LOT/SERIAL/PRICE/AVGC/STDC/DESC/REF/DEPT/QTY/SCRAP/VEND/PO/TYPE), ISJOB(9f job tracking: NUM/DESC/CUST/VEND/STATUS/OPENDT/CLOSEDT), ISAREX(51f AR extended: resale cert fields), ISRMAI(54f RMA invoice: NUM+PART+LINEID, STATUS/REASON/DISP/OSONUM/OINVNUM), BKCMACCL(2f account level), BKCMLEAD(2f lead source); Pass 157: 5 Java JARs confirmed in com.evoerp.salesanalysis.* namespace: SalesRepSummary.jar(srs)+ProfitByInvoice.jar(pbi)+ItemClass.jar(ic)+CustomerClass.jar(cc)+MultiYearSales.jar(multiyear) — SA analysis views are Java-backed; **Pass167 J7AISAN (201p, 32dbs, EVO.LIB)**: BKSA.TYPE/NAME/RTM/TITLE/BASE + BKSA.FROM1..26/THRU1..26 = **57 BKSA.* vars confirm full BKSAREPT access namespace** (matches 57f DDF schema exactly: TYPE+NAME PK+RTM+TITLE+BASE+26 FROM/THRU range pairs); **BKAP.* 105 = BKAPVEND** access namespace (SA does vendor analysis — BKAP.ADD1/VENDNAME/TELEPHONE/PURCH.MTD/YTD/LYR/VAR etc.); BKAP.PO.* = PO header access (open PO context in SA); J7AISAN also opens WORKORD+WOMAT+WOLABOR+OUTPROC+WORECV+WOEXCHG = SA module includes WO actual-cost dimension (labor, material, outside processing, receipts) — **C: 84/100**
- [ ] ⬜ **SB** — no T7 RWN/DFM files found (DBA-era legacy)
- [x] 🔄 **SD** — Standard Detail Codes (T7SDET: 58 procs, 32 tables, src=EVO.LIB); **ISSDET confirmed 4 fields** (not 2f — Pass 117): IS.SDET.TYPE+DETAIL+SUB+WHO; ISSTYPE(3f) confirmed: IS.STYPE.TYPE+ASSET+WHO; ISNCR+ISMCR+ISDRILL+FILELOC in DB set confirms SD codes link to NCR defects and multi-currency; maintains cross-module service/detail code lookup; purpose: CRUD editor for ISSDET detail codes + ISSTYPE type master; Pass 159: REPLNK_REC_HOLD = record hold during link-replacement operations (ensures consistent cross-table code references); ADD.NEW = add-new mode flag; WHOAMI = current user identity; ISDRILL in 32t set = standard detail codes ARE searchable via the query/drill-down system; SDET + STYPE vars confirm single program manages both ISSDET code records AND their ISSTYPE category assignments — **C: 78/100**
- [x] 🔄 **SH** — Shop Scheduling ⚠️ (NOT Shipping) (16 ops) — all 15 DFM files read; SH-A/B (WO WIP scheduling grid + operation scheduling), SH-C (work center capacity), SH-E (due date change), SH-I (dispatch report with color coding), SH-P (color config); primary tables MTWO.WIP.*, MTWORO.*, MTWC.* — **C: 72/100**
- [x] 🔄 Pass 54: All 17 T7SH* programs mapped; WORKORD(74f: MTWO_WIP_* all fields — WOPRE/WOSUF/CODE/SQTY/COMQTY/STATUS/PRTY/dates/costs×8-types×est+act+var)+WOROUT(81f: MTWORO_* all fields — WC/SCHED_WC/dates/ESTHRS/ACTHRS/ESETHRS/ASETHRS/QTYCOM/CONTNTN/OVERLAP/NEGOVLP/costs×6+misc/15×INSTR)+WORKCTR(47f: MTWC_* — HRSWEEK/rates/OH/AVGQTIME/LEAD/OUTPROC/PARENT/CYCLE_TIMES×10/FLAGS×5/ALPHA×5)+BUCKETS(14f: WC+WO+OP per time bucket with CRATIO+LOCKED+CNTN)+SCHWO(10f: WO scheduler summary with shop-day numbers+CRATIO+CONTENTION)+SCHEDCAL(6f: calendar↔shop-day mapping forward+backward)+CALENDAR(5f)+MACHINE(20f: HRSUSED+HRSMAINT+parent WC+deactivation log)+ISWOPRIO(4f: priority 1-9 with color)+ISARCHG(26f: SO line before/after change audit)+MTMRP(13f: MRP pegged demand)+ISWOEX(63f: fully extracted — 10-date+7-float+alpha+10-flag UDF)+WCCTL(5f)+ISBUILD(15f)+ISDROP(4f) all extracted; TASCOLOR confirmed not in DDF (TAS runtime color config) — **C: 82/100**
- [x] 🔄 **SL** — Shop Loading (T7SLSFC: 5 procs, 53,987 bytes); full DB fingerprint confirmed (Pass 117, 22 tables): BKARINVL+BKDCLAB+BKARCUST+ISWOPRIO+WORKCTR+ROUTING+BKYSMSTR+BKICMSTR+BKCMACCN+BKAPVEND+ISDRILL+ISIS+BKSYHELP+DBAHLPID+MKAHIST+ISLOG+ISLINKS+BKAPDESC+LANGDICT+TASCOLOR+ISMCR+FILELOC; source_file=ISTS.SRC; JAVA.PATH/JAVA.PATH2 vars confirmed (Pass 157 decryption); PLDN/PTDN = production-line/tool-down flags; WEBLINK/XCPATH = cross-platform display path; ISWOPRIO(4f: PRIO+DESC+EXTRA+COLOR); BKDCLAB(50f fully extracted); **Java-backed confirmed**: candidate JARs = WCScheduler.jar(com.evoerp.wcsched), WOScheduler.jar, WorkCenterLoad.jar(com.evoerp.wcload.javafx.App=VSCHED), MachineView.jar(com.evoerp.machineview.jfx.App), Scheduler.jar; ISTS.CFG.AUTOSL+AUTOPL = auto-scheduling flags — **C: 73/100**
- [x] 🔄 **SM** — System Maintenance (34 ops, 3rd largest) — 23+ forms + full T7SM* sub-module family decoded; SM-K (user prefs→EvoSettings.INI/ISNUMBER), SM-E/F (tax ISIS.TXF+ISIS.TXG), SM-O (ship-via ISSHPVIA with tracking URL), SM-D (payment terms IS.TERMS), SM-PF (ISJOB job#), SM-PH (IS.CYCLE), SM-JM/JN (merge), SM-JC (JC setup), SM-SD (AP doc link); T7SMI* (CRM masters: BKCMLEAD/BKCMTERR/BKCMACFC/BKCMACCC/BKCMDTCD), T7SMP* (ISCATMST/ISUDMSTR/ISJOB), T7SMT/SMU (ISSHPVIA), T7SMTEND/SMTSET (SMT/PCB: ISSMTCFG/MACHINE); BKSYMSTR/BKYSMSTR not fully decoded; Pass 51: T7SMJA-V rebuild family (14 programs) + T7SMPA-J variants (10 programs) fully mapped; BKCMHCOD(9f: HCODE(2) PK+RATE+BPART billing part+WINDW+ABILL)+BKCMACFC(3f)+BKCMACCC(2f)+BKCMDTCD(2f)+ISCATMST(3f)+CLASMSTR(2f)+CLASS(24f: CLASS+LOC PK, full GL set per location)+ISNUMBER(52f: CODE PK+51 counter slots)+BKSYAP(11f: next RECVNUM+PONUM+QCRECV+RFQNUM+flags)+CALTEMP(2f) all extracted — **C: 82/100**
- [x] 🔄 **SP** — Statistical Process Control (SPC) ⚠️ (NOT Ship Packing — CORRECTED) — Pass 67: 7 programs confirmed: T7SPC(148p main: ISSERR+ISSTRACK+ISSPC+ISSTYPE+ISSDET+ISSETYPE+ISSEPROC+WORKORD+WOBOM), T7SPCREP/SPCREP2(105p each), T7SPCLIVEREP(50p), T7SPCREPPPM(104p), T7SPCLIVEGRID(5p), T7SPCMEMO2ALPHA(25p); ISSERR(14f fully decoded: WOPRE+WOSUF+OPER+TIME+DATE+ERROR+PROCESS+COUNT+REF+EXTRA+SERIAL+ADOF(1000)+ADIAG(1000)+AREWORK(1000) — AOI integration confirmed by 3×1000-char AOI text fields), ISSPC(20f: WO+OPER+EMP+DATE+TIME+GOOD+REWORK+SIDE+TYPE+DETAIL+TESTR/T/E_1..3+ANOTES+CUST+PART), ISSTRACK(13f: WOPRE+WOSUF+OPER+PROC+PSER+COMP+CSER+NOTE(1000)+AR+CLOT — component traceability), ISSTYPE/ISSETYPE/ISSEPROC/ISSDET all decoded; AOI+PCB traceability architecture confirmed — **C: 80/100**
- [x] 🔄 **SR** — Service / Repair — 16 RWN programs confirmed (T7SRA-T7SRK + SRDISPACH/SRBK/SRGA/SRINFO); SR Orders ARE BKARINV records (same as SO/AR); 5 ISSR*INV views = BKARINV (0 diff), 5 ISSR*IVL views = BKARINVL (0 diff); key tables: ISSRMMS (equipment 12f), ISSRINFO (configurable 54f), ISSOREVU (approval workflow 12f), ISARINVX (AR ext 4f); T7SRGA (157 procs) is full posting to BKGLTRAN+BKGLX+BKARHTAX+BKISTAX+ISTAXGRP — **C: 72/100**
- [x] 🔄 **SU** — Setup / UI Configuration — CHM confirmed 4 ops (SU-A=Maintain Grid Lookups, SU-B=Maintain Drill Down Menus, SU-C=Forms Editor, SU-D=Grid Maintenance); RWN programs: WBKLUGRID(68p Pass 65: 79-table fingerprint = admin+lookup sources in one program; admin role confirmed as QU framework configurator), EVOERPDRILLM(31p: ISDRILLM+BKLUGRID+ISLOG audit), T7GDM(31p: Grid Display Manager BKLUGRID+ISDRILLM); SU-C Forms Editor not yet matched to RWN; key tables: BKLUGRID+ISDRILLM — **C: 72/100**
- [ ] ⬜ **SY** — no T7 RWN/DFM files found; BKSY* tables are System config (documented)
- [x] 🔄 **TA** — TAS / System Administration — CHM confirmed 9 ops: TA-D=Maintain Database, TA-G=Maintain Menu Access Records, TA-H=Maintain Menu End User, TA-M=Forms Editor, TA-N=Program Scheduler, TA-O=Backup Utility, TA-Q=Change Logo Image, TA-R=SQL Editor, TA-S=Data Dictionary Check; ALL 9 programs now matched (Pass 112 2026-06-19): TA-S=T7DDCHECK(92p, FILEDICT+FILEKEY+FILELOC), TA-N=EVOSCHEDULER(65p, ISSCHED)+EVOSCHEDSETUP(37p), TA-O=EVOERPBACKUP(76p, zipdll), TA-R=QUERYEXECUTE(26p, ISDRILL); TA-G=WBKMENUSETUP.RWN(98p: BKPSUSER+BKMENUSU; vars MI_MENU_LVL/MI_CAPTION/MI_FASTSELECT/MI_PROGRAMNAME/MI_IMAGE/GA_* menu item+group editors; ACCESS_CODE+USERNAME for user access control); TA-H=wbkmenusueu.rwn(143KB: BKMENUSU+50+ tables = end-user view of menu access records; source=NZLICE.LIB NZ-licensed variant); TA-M=Forms Editor=EXTERNAL program (no dedicated RWN found in all 1,122 programs — invokes RBDsgnr.exe or TAS Pro built-in form-design command); TA-Q=evologo.RWN(23p: CO.LOGO field in BKSYMSTR, LOGOFILE var — changes company logo image stored in BKSYMSTR.CO.LOGO); Pass 63: 8 WTAS* admin programs confirmed; ISSCHED(24f) fully extracted — **C: 88/100**
- [x] 🔄 **TC** — Treasury Control — AR Cash Receipts Entry; T7TCC(119p, src=LISTG60.LIB, 37 unique tables); ETBCOMBOVAL = LISTG60.LIB grid confirmed; full DB: ISTERMS+ISBANKS+BKARINVT+BKARCUST+BKARINV+BKGLCOA+BKSYMSTR+BKYSMSTR+ISMCF+BKART+BKAPCHKF+BKARDEP+BKGLCHK+BKARINVI+BKPRSALE+BKPRCOMM+ISREPORD+BKARINVL+BKICMSTR+CLASS+BKSYHELP+DBAHLPID+ISIS+MKAHIST+ISLOG+ISDRILL+BKAPVEND+BKCMACCN+ISLINKS+BKAPDESC+LANGDICT+BKSYAR+MKECLASS+BKGLTRAN+ISMCR+BKGLX+WORKORD; Pass 65: ISREPORD(17f: REPNM+REPWH+SONUM+INVNM+INVDT+ULID+COMPR+CMAMT+AMT+AMTRM+CBK+PCODE+CUST+PAYDT+GLA/GLD), MKECLASS(3f: NUM+DESC+ACTIVE); Pass 162 vars: TERMS.NUM=payment terms; CHK_NAME[1]=check payee; CHECK_AMT/CHECK_NUM/CHKACT=payment amount/number/bank account; OP_INV=open invoice list; NUM_INVOICES=batch count; INV_NUM/INV_DATE/INV_AMTRM/INV_DISC/INV_APPLIED/INV_DESC/INV_TERMSN/INV_TERMSD/INV_DEPOSITS/INV_PS=per-invoice apply vars; DINV_*=deposit-invoice parallel vars; TOT_CREDITS/TOT_DEPOSITS/TOT_CHARGES/TOT_DISC=batch totals; OUT.INV/OUT.CRD/OUT.DEP=outstanding counters; ENT_DISC/ENT_APPLIED/HOLD_APPLIED=user-entered amounts; DISC_DATE/DAYS.TOPAY=discount deadline+terms; DEPOSIT_NUM=deposit record; AMOUNT_REM=unapplied remaining; ARC_TTLA/B/1=archive totals; INVC.NETCHG/CRED.NETCHG/DEP.NETCHG=net change calcs; workflow: BKART=payment txn; BKGLCHK=check register; BKGLTRAN=GL; BKARDEP=deposits; BKPRSALE/BKPRCOMM=commission on receipt; WORKORD=WO milestone billing payments — **C: 76/100**
- [ ] ⬜ **UM** — no T7 RWN/DFM files found (DBA-era legacy)
- [ ] ⬜ **UP** — no T7 RWN/DFM files found (DBA-era legacy)
- [x] 🔄 **US** — User Services / Trigger Notifications — T7USG (90 procs, 24 tables); full DB fingerprint (Pass 117): ISTRIGRS+BKARCUST+BKAPVEND+WORKORD+BKARINV+BKAPDESC+BKCMACCN+BKICMSTR+BKICREF+BKPSUSER+BKSYHELP+BKSYUSER+CLASMSTR+DBAHLPID+ISDRILL+ISIS+ISBNMSTR+ISCATMST+ISITP+ISLINKS+ISLOG+ISNCR+MKAHIST; new tables vs prior: BKSYUSER (system user config), CLASMSTR (class master), ISBNMSTR (bin name master), ISCATMST (category master), ISITP (item type/issue type), BKICREF (customer part xref), BKPSUSER (user access check); ISTRIGRS(25f) fully documented; ISREMIND(22f) fully documented; EvoRemind (46 procs) polls ISTRIGRS → creates ISREMIND; broad module: trigger maintenance + category/class/item-type master — **C: 70/100**
- [x] 🔄 **UT** — Utilities (admin/data maintenance) — 8 programs; Pass164 symbol vars: UTKA clears: CLR.COA/CUST/VEND/INVN/EMP/CM/GLDATES (7 targets — CORRECTED: also EMP, CM, GLDATES) + DONE.GL/AR/AP/INV/PR/CM/DT completion flags + WARNBANKACCT; UTKD: FYCUR+FY1YP..FY6YP (6 prior years — CORRECTED from 3) + SUSP.GLACCT/SUSP.GLDPT (suspense account for year-end posting) + POST.AMT/POST.FAIL; UTKE (location rename): **GL arrays confirmed** — AGLA/AGLC/AGLS/AGLSNT/AGLW = 5 inventory GL account types per location (A=Asset, C=COGS, S=Sales, SNT=Sales-net-tax, W=WIP) + ADPTA/ADPTC/ADPTS/ADPTNT/ADPTW = corresponding dept codes — confirms EvoERP maintains location-specific 5-account GL sets; UTKF (cost revalue): OLD.TOTVL/NEW.TOTVL delta + PRT.GLACT/PRT.GLAMT GL output + PART.GLA/PART.DPTA per-part GL; UTKH: INC.TYPE + FROM/THRU ITEM/CLASS/GLACCT/GLDPT; T7UTH: LOC_* FILELOC vars + DICT_BUFF_NAME/DICT_FIELD_NAME; T7UTI: BKSYAP(11f) + DONE flags; T7UTKH: CLASS(24f CLASS+LOC GL sets) — **C: 82/100**
- [x] 🔄 **WC** — Warehouse Control ⚠️ (11 programs: T7WCA/B/BinLot/BK/C/D/E/F/G/H/WCLOCFIX); Pass164 symbol vars: **BKIC.LOCM.* 14-field location master** cross-validated (CODE/NAME/ADDR1/ADDR2/ADDR3/CITY/STATE/ZIP/TAX#/CNTCT/PHONE/FAX/TAXGR/CITY2 — in WCA+WCH); **ISBINLOC 9 fields from WCLOCFIX** (ITEM/LOC/BIN/UOH/CDATE/VDATE/DFLT/EXTRA/RVLVL; DDF=11f, 2 unknown); program roles: WCA=location+bin master CRUD; WCB=WH.CONTROL bin assignment review (LIST.*WC vars); WCBinLot=ISTECH.LIB integrity fix (ARTXN+BINLOC+LOT+SERIAL+PI handles); WCBK=capacity report (TOT.HOURS/CAPACITY/BALANCE/HRS.REMAIN, ISE.STATUS.2/.3 WO ops); WCC=serial by location (MTSER.* 25 fields); WCD=CSV bin import (IMP.LOC/BIN/ITEM/DFLT/QTY/LOT/SERIAL); WCE=bin/lot/serial inventory report (INCL.LOT/INCL.SER/COMBINE.DUPES/CYCLE); WCF=simpler inventory+RTM_NAME/EXCEPT.CODES; WCG=bin assignment (MAKE.DEFAULT/DFLT.LOC); WCH=location browser (full BKIC.LOCM); WCLOCFIX=ISBINLOC repair — **C: 88/100**
- [x] 🔄 **YS** — Y/N System Flags Editor (T7YSYN: 52 procs, 14 DB files, src=EVO.LIB+LISTG60.LIB(ETBCOMBOVAL)); Pass164: BKYS.* typed field access confirmed — BKYSMSTR holds typed parameters beyond YN array: BKYS.WONUM/YN/GLNUM/GLDPT/NUM/DESC/VNUM/DATE/QCNUM/REQNUM/INVNUM/RBNUM (12 named typed fields); 14 DB tables include BKARCUST/BKAPVEND/BKCMACCN/BKICMSTR (entity lookup for default values), LANGDICT (multi-language descriptions), ISDRILL+ISLOG+ISLINKS (audit+drill); EVO.CFG.OL*A vars (OLWOA/OLPOA/OLINA/OLINB/OLSOA/OLARA/OLAPA) = per-module OnLine mode toggles stored in BKYSMSTR; CFG.START/CFG.BUFFER = startup config buffer vars (T7YSYN manages numeric config parameters, not just YN flags); ARRAY/YSYN/ARRAY.DESC = display arrays; T7YSYN is the system-wide parameters editor covering GL defaults, vendor defaults, WO/invoice auto-numbers, QC codes, dates, descriptions — not just binary Y/N flags — **C: 80/100**

**Subsystems (not menu modules — discovered via RWN analysis):**
- [x] 🔄 **PI** — Physical Inventory (9 files, 1,056 procs) — Pass 38: 8 programs fully mapped: T7PIA(159p freeze: BKPIMSTR+BKICMSTR+BKICLOC+ISCYCLCD→creates BKPIFROZ), T7PIB(114p print sheets: BKPIFROZ+BKPILOT+BKPISER), T7PIC(152p tag entry: writes BKPIPHYS, reads ISBINLOC+BKPRMSTR), T7PID(98p discrepancy: BKPIPHYS vs BKPIFROZ), T7PIE(76p adjust: BKPIFROZ+BKICMSTR), T7PICA(97p count adj variant), T7PIF(137p post: ISBUILD+MTICMSTR+BKPIPHYS+ISBINLOC→BKGLTRAN), T7PIG(155p report: BKPIMSTR+BKPIPHYS+BKPIFROZ+BKICLOC); all 7 BKPI* schemas extracted: BKPIMSTR(3f YEAR+QTR+DESC), BKPIFROZ(19f UOH+COST+GLPST/INPST+ACCTA/C+TAGS), BKPIPHYS(14f TAGNUM+ACTQTY+EMPNAME+LOT+SERIAL+BIN), BKPILOT(10f), BKPISER(10f), PIBINLOC(14f ITEM+LOC+BIN UOH+DFLT), PIBINLOT(14f with LOT+SER); freeze→count→variance→post cycle fully confirmed — **C: 72/100**
- [x] 🔄 **BO** — Bill of Lading; T7BOL (178p, src=LISTG60.LIB, 26t) + T7BOLMSO (174p, 25t); full DB fingerprints confirmed (Pass 117); T7BOL opens ISAREX+ISICMSTR+ISSRINFO+ISSOBOX+BKAPPO+ISACCESS+FILELOC+BKSYMSTR; T7BOLMSO drops BKAPPO/ISAREX/ISSRINFO, adds BKPRMSTR+BKPSUSER (driver/employee for LTL); both open BKARINV+BKARCUST+BKARINVL+BKCMACCN+BKICMSTR+ISSHIPCO+ISSHPVIA+MTICMSTR; ISAREX = AR compliance certifications; Pass 162 vars: carrier/load: LOAD.NUMBER/SEAL.NUMBER/TRAILER.NUMBER/AUTHOR.NUMBER/CONTROL.NUMBER = 5 carrier reference numbers; PICKUP.TIME/PICKUP.DATE = scheduled pickup; DRIVER.ARRIVED/LOADING.START/LOADING.END/DRIVER.DEPARTED = 4 logistics timestamps; BOL content list: LIST.DESC/QTY/CASES/WT/PALLET/DUEDATE/SHIPINFO = display grid fields; BOL entry: EDIT.DESC/QTY/ITEM.WT/CASES/PALLET.WT/INFO = basic edit vars; **EDIT.HTYPE/HQTY** = hazardous material type/quantity; **EDIT.NMFC** = NMFC freight classification code (LTL carrier tariff); **EDIT.CLASS** = freight class (30/50/70/85/100/etc.); EDIT.PQTY/PTYPE = package quantity/type; EDIT.HM = hazmat flag; pallet: TOT.CARR.HTYPE/PTYPE/ONE.PALLET.WT/ADD.PALLETS/ADD.PALLET.WT/EDIT.PALLET/EDIT.PWEIGHT = pallet detail entry; COMMODITY/DEPARTMENT = freight commodity + billing dept — **C: 76/100**
- [x] 🔄 Pass 55: ISSOBOX(22f: SONUM+LINE+BOX PK, CODE+QTY+LOT+SERIAL+INVNUM+SHIPPR+SHPCOD+WEIGHT+SKID+DATE+WO link+UCC+HT+LG+WD+TRACK+EXTRA)+ISSHIPCO(16f: SHPCOD PK+NAME+DESC+VNDCOD+5×NOTES+SHIPVIA+EXTRA+5×WEB(120 tracking URL templates)) fully extracted; no dedicated BOL table confirmed; workflow traced; BOL assembles from BKARINV+ISSOBOX+ISSHIPCO at print time — **C: 72/100**
- [x] 🔄 **DS** — Data Sync (25 programs: T7DSAP/AR/BOM/CK/CM/CO/CS/DC/EST/FO/GEN/GL/HH/IC/IM/MRP/PO/PR/QC/RMA/RO/SH/SO/WC/WO); **T7DSGEN stub confirmed from symbol data (Pass 117):** 7,271 bytes, 5 procs, 36 db_files, only 1 named var = STUB; source_file=T7DSGEN.SRC (one of 7 readable SRC files); all 24 active T7DS* programs identical 36-table fingerprints (T7DSQC=0 anomaly); identical fingerprint: BKAPDESC+BKAPPO+BKAPVEND+BKARCUST+BKARINV+BKCMACCN+BKGLTRAN+BKGLX+BKICMSTR+BKSYAR+BKSYHELP+CLASS+DBAFIFO+DBAHLPID+FILELOC+ISDRILL+ISDROP+ISGLDATE+ISICMSTR+ISIS+ISLINKS+ISLOG+ISMCR+ISNCR+ISNOTES+ISNTYPE+ISNUMBER+ISREMIND+ISTAXGRP+ISTRIGRS+LANGDICT+LOT+MKAHIST+MKECLASS+SERIAL+WORKORD; DS architecture confirmed: 7KB stubs → central sync engine (the STUB var is the dispatch token); all 36 fingerprint tables fully field-decoded; sync field-level logic remains blocked by RWN encryption — **C: 72/100**
- [x] 🔄 **AU** — Automation modules; Pass164 symbol vars: **T7AUTOFX** = Java-backed FX rate updater (HOST/PORT/JAVA.PATH); FRMCUR/TOCUR currency pair; **ISIS.MCF.* schema confirmed**: CODE(currency code)/BASE(base flag)/GLABK(GL account bank-foreign)/GLDBK(GL dept bank-foreign)/GLABS(GL account bank-base)/GLDBS(GL dept bank-base); **T7AUTOMRF** additional MTMRP fields: ACTION(MRP action code)/PG.SDATE/PG.FDATE(planning dates)/PG.QTY(planned qty)/LOC; **T7AUTOREBSS** BKIC.PROD.* adds: TXBLE(taxable)/RLVL/RAMT(reorder level/amount)/LSALE/LORD/LRCPT(last sale/order/receipt dates); **T7AutoDCH** filters: SFROM/STHRU.EMP + FROM/THRU WONUM/LABDATE/LABTIME + BACKFLUSH flag; BKDCLAB(50f) fully extracted; 8 programs total (4 active + 4 stubs) — **C: 80/100**
- [x] 🔄 **FS** — Field Information Base (FIB) (T7FSCLASS: 62 procs, ISFSCLAS+ISPRINFO; T7FSINFO: 61 procs, ISFSINFO+BKCMACCN; T7FSEMP: 59 procs, ISFSCLAS+BKPRSALE); field prefixes IS_FIB_* confirm "Field Information Base" not general field service; ISFSCLAS(3f: CLASS/GROUP/EXTRA), ISFSINFO(4f: PROGRAM/CONTRACT/MISC/WHO), ISPRINFO(4f: PROG/DESC/MISC/TYPE) all extracted; BKCMACCN(154f) fully extracted: 10 contacts × (name+title+phone+email+salutation) + 2×10 date+alpha configurable slots + labels; FIB links service records to CRM account contacts — **C: 72/100**
- [x] 🔄 **GF** — Global Finance / AR Charges (T7GFPRICE: 116 procs, customer+item pricing/charge entry; T7GFV/GFVS: 82/81 procs, invoice charge viewer; T7GFR: 46 procs, report); ISARCHG (26f) fully documented; BKICPMAT(85f) fully extracted; Pass164: **BKARCUST 13 fields confirmed from T7GFPRICE vars** (BKAR.*: CUSTCODE/CUSTNAME/ADD1/ADD2/CITY/STATE/ZIP/CONTACT/TELEPHONE/COUNTRY/CREDITLMT/CHG.INTRST/REMAINCRD); T7GFV: TODAY/SO/ORDDATE/ESD/SHIPTO — SO header context for charge entry; JOB_NUM/SORTJ/SORTG — job+sort vars; GCNTR/LCNTR — group+line counters; ARCUST.H = AR customer handle; NEWGROUP = new charge group flag; 5 programs confirmed — **C: 80/100**
- [x] 🔄 **RE** — Reminders + Rebuild Utilities (T7RemindRpt: 125 procs, ISREMIND+BKARCUST+BKCMACCN; T7REPLNK: 67 procs, ISREPLNK+BKPRSALE; T7REPDEF: 52 procs, ISREPDEF; T7REINDEX: 36 procs, FILELOC; T7REBQC: 62 procs, BKICMSTR; T7REBWO: 123 procs, WORKORD+WOBOM+WORECV+WOROUT+MTICMSTR+WOMAT+WOLABOR; T7REDINDEXDD: 5 procs stub); ISREPDEF(3f: LABEL(5 PK)+TITLE+EXTRA); ISREPLNK(11f: REPNM+CUST+ITEM PK, CLASS+SDATE+EDATE+LABEL+GLA+GLD+EXTRA) fully extracted; WOLABOR(58f) fully extracted: DATE+EMP+WOPRE+WOSUF+OPER+TRXN PK, RUNHRS/SETUPHRS/LABRATE/LABCOST/SETCOST/MACHCOST/FOHCOST/VOHCOST/WC/TOOL/MACH/START/STOP/DEDUCT + cycle time + 5flags+3alpha UDF; WORECV(11f): WOPRE+WOSUF+DATE PK, ASSY+QTY+AVGC+LOT+SERIAL — all 7 programs and 4 key schemas confirmed — **C: 75/100**
- [x] 🔄 **SE/ST** — Service Code Tables; T7STEQUIP (52p, 90t, src=EVO.LIB — Pass 117 "46t" was post-dedup; symbol extractor count=90): opens BKEDIDUN+BKEDPOST (EDI tables), BKISTAX (item tax), BKSYAR (AR system settings), BKGLX (GL extended), DBAFIFO, ISARCHG (AR charge extension), ISARTXNB (AR txn by num), ISBINLOT, ISBSF, ISCHAINM (chain master), ISNOTES, ISSOBOX, MKECLASS, LOT, SERIAL; BKEDPOST = EDI posting table; ISARCHG = AR charge extended; T7SEPROC (52p, 32t, src=EVO.LIB): ISSEPROC 2f (IS.SEPROC.PROC+WHO = service procedure codes); T7SETYPE (52p, 32t, src=EVO.LIB): ISSETYPE 2f (IS.SETYPE.ERR+WHO = service entry error/type codes); T7STYPE (52p, 90t, src=EVO.LIB): ISSTYPE 3f (IS.STYPE.TYPE+WHO+ASSET = equipment type with ASSET flag for fixed-asset linkage); **t7sttype.RWN** (52p, 90t, src=EVO.LIB) = lowercase alias of T7STYPE — same vars/tables, kept for backward-compatibility; T7STOCK (53p, 90t, src=EVO.LIB): BKCMACCC (BKCM.ACCC.CCODE+DESC = CRM account category code editor — NOT an equipment table); ISSEQUIP(2f)+ISSERIAL(11f) both extracted; T7STEQUIP is the most complex SE/ST program (52p, 90t = full operational scope for service equipment lifecycle); Pass 159: all 6 SE/ST programs confirmed src=EVO.LIB; program roles fully mapped — **C: 77/100**
- [x] 🔄 **PU** — Warehouse Put-Away (T7PUTAWAY: 105 procs, 34 unique tables/63 raw, src=LISTG60.LIB): BKAPINVL+BKAPPO+BKGLTRAN+DBAFIFO+LOT+SERIAL+ISORDECO+BKCMACCT+BKCMACCN+ISTRIGRS+ISREMIND+ISNCR+ISNUMBER+ISMCR+ISLINKS+ISNTYPE+BKARINV+MKAHIST+ISGLDATE+MKECLASS+MTICMSTR+TASCOLOR+BKICMSTR+BKPSUSER+BKAPVEND+BKARCUST+BKAPDESC+BKSYHELP+DBAHLPID+FILELOC+ISDRILL+ISIS+LANGDICT; NO PU-specific tables — uses shared infrastructure; MKECLASS+TASCOLOR = class-based put-away rules with color coding; ISORDECO = ECO-linked put-away; ISGLDATE = GL-date-controlled posting; BKCMACCT = CRM account context for customer-owned stock; workflow: AP receipt (BKAPINVL/BKAPPO)→bin assignment→lot/serial (LOT/SERIAL)→GL (BKGLTRAN/DBAFIFO)→notifications (ISTRIGRS/ISREMIND); Pass 160: **LISTG60.LIB confirmed** (grid/list UI framework); SCAN.ITEM = barcode scan input; ENTERBIN = operator bin entry; ACTION = put-away action code; PABBL = put-away compound state var (bin/box/lot); BKIC.IS.DCODE = item discontinued flag (checked before put-away); MTIC.PROD.CUBFT = cubic feet (warehouse space); MTIC.PROD.ABC = ABC cycle-count class; MTIC.PROD.STDPK = standard pack (unit of put-away) — **C: 78/100**
- [x] 🔄 **MU** — Multi-Yield Work Orders (T7MULTIYIELD: 150 procs, 43 tables, src=LISTG60.LIB); records multiple co-product output part numbers from single WO; full DB set confirmed: WORKORD+WOROUT+WOBOM+WORECV+INVTXN+ISBINLOC+BKARINVL+MTICMSTR+BKICLOC+WOMAT+ISWOEX+LOT+ISBINLOT+SERIAL+BKGLTRAN+BKGLX+DBAFIFO+ISTRIGRS; ISWOEX (WO extended) holds multi-yield state; workflow confirmed (input WO→multiple WORECV+INVTXN outputs→FIFO/LOT/SERIAL tracking); Pass 43: 43-table DB fingerprint re-confirmed; Pass 160: **E.PART/DESC/QTY/BIN** = expected output co-product fields (per yield output line); **M.PART/DESC/QTY/PER/BIN** = material input fields (component consumed); **PROPORTION** = yield split ratio between co-products; **SCAN.WONUM** = barcode scan for WO number entry; MTWO.WIP.MULT = multiple-yield flag on WORKORD; MTWO.WIP.PRTY/SSTART/SFIN = WO scheduling fields; LISTG60.LIB = grid/list display framework (item grid for yield output selection) — **C: 77/100**
- [x] 🔄 **AL** — Audit Log + Alternate Parts (T7ALOGSETUP: 43 procs — configures audit monitoring, writes to ISLOG+BKSYMSTR+BKPSUSER; T7ALTPART: 104 procs, BKSBPART+BKICMSTR+ISLINKS — alternate/substitute part maintenance; Pass 65: ISLOG(9f fully extracted: WHO+WHAT+DOING+STARTD/T+COMPANY+KILL+MSG+EXTRA — KILL flag allows admin session termination)); BKSBPART(5f)=PARNT+PROD+CUST+SUBST; ISLINKS(311f)=global doc/URL store; T7ALOGSETUP opens FILELOC (enumerate all tables to configure monitoring); Pass 157: T7ALOGSETUP vars confirmed: USER/PASSWORD/PASS.OK/EUSER/UPSK = password-gated setup; LOC_BUFF_NAME/LOC_FILE_NAME/LOC_COMP_CODE/LOC_REC_SIZE/LOC_REC_TYPE = FILELOC record iteration; CNTR = table counter; NEW_GROUP/NEW_GROUP_NUM = audit group config; writes BKSYMSTR; T7ALTPART vars: FROM.ITEM/THRU.ITEM range filter; BKSB.PART.PARNT/KEY/KEY2/PROD/CUST/SUBST/EXTRA = direct BKSBPART field access; **SAVE.BOTH.WAYS** = creates bidirectional A→B AND B→A substitution records; ALTPART.H/RLPART.H/ALPART.H = 3 record handles; ISACCESS = license gate — **C: 74/100**
- [x] 🔄 **LI** — License / Module Access (T7LIMACC: 42 procs, 4 tables: ISACCESS+BKSYHELP+DBAHLPID+MKAHIST, src=NZLICE.LIB); **ISACCESS 8-field schema extracted from IS.ACC.* vars (Pass 117):** NAME+OBJ+OBJTYPE+DFM+FIELD+STATUS+TEXT+EXTRA (not in DDF); AGROUP/AOBJ = access group and object identifier vars; ACC.REC/ACCESS.H = record and handle; OBJ_TYPE/OTYPE = object type codes; FPOPVLD1-5 = field-level pop-up validation (licensed module gate fields); ISACCESS controls per-DFM/per-field access restrictions for licensed modules; Pass 160: **T7LIMACC scans actual DFM files** to enumerate UI components: DFMNAME = form file being inspected; DFM.H = DFM file handle; DFM_OBJNAME/CAPTION/TEXT/HINT = DFM component property vars (reads object names + captions from DFM binary); LAGROUP/LGNUM = language group number for multi-language access control; workflow: open DFM→iterate components→match to ISACCESS by object name→apply STATUS restriction per field — **C: 77/100**
- [x] 🔄 **ML** — Multi-Language Invoice Support (T7MLC: 50 procs, source=NZLICE.LIB, 40t); DB fingerprint confirmed (Pass 117, 40t not 27); conversion vars: IS.CF/CFF (currency flags/fields), IS.CVT.MTH (conversion method), IS.LND.RTE (landed rate), IS.OEXC/RTE/RTE2 (orig/new exchange rates), IS.SYMBOL/SYMDESC/SYMPOS (currency symbol display), IS.FRGTPER (freight percentage); full tax+landed cost handle set: ISTXG.HNDL+ISTXF.HNDL+ISTAX.HNDL+ISHTX.HNDL+HTAX.HNDL+ISMCF.HNDL+ISMCR.HNDL+ISDUTY.HNDL+ISBRK.HNDL+ISLDF.HNDL; DCL.PERIOD.FREQ/PDTE = customs declaration period; EIMCO.SHIFT2/3 = EIM invoice shift codes; Pass 162 vars: **DFMNAME/DFM_NAME** = DFM file name being translated; **ADDLANG** = add language action flag; **LANGUAGE** = 3-char language code; **LANG.H** = LANGDICT handle; **LGNUM** = language group number; **LANGS** = total language count; **LANG.DICT.ECAPT/LANG/LCAPT/FONT/EXTRA** = all 5 LANGDICT fields (English caption, lang code, local caption, font, extra — font field was NOT in prior documentation); **PRE.LANGCAPT** = previous caption value before edit; **EVO.CFG.LANG** = system-wide default language from BKYSMSTR; ISCTR/ISCT/ISLP/IS.DEC = multi-currency counters (decimal precision handling); TAXC/TAMT/IS.TAX.FIX = tax code/amount/fixed-tax flag; T7MLC = multi-currency invoice printer with LANGDICT translation layer + landed cost apportionment + tax; T7LANG = LANGDICT maintenance — **C: 82/100**
- [x] 🔄 **MH** — Shipping Order (T7MHOPE: 98 procs, source=ISTECH2.LIB, 39t); **ISTECH2.LIB** = SO/shipping framework library (superset of LISTG60.LIB — all ISTECH2 programs have ETBCOMBOVAL grid); confirmed: T7SOE/T7SOS/T7MHOPE/T7SRE/T7INS/t7hhssoe/J7HHRTSSOE all use ISTECH2.LIB; full DB (39t): BKCMTERR+BKARCUST+ISSHPVIA+ISSHIPCO+BKARINV+BKARINVL+BKICLOC+BKGLTRAN+ISREPLNK+BKPRSALE+BKICPMAT+ISJAVA+ISBSF+BKYSMSTR+BKAPDESC+BKICMSTR+BKCMACCN+BKAPVEND+ISGLDATE+ISIS+ISNUMBER+ISREPORD+ISDRILL+MKAHIST+DBAHLPID+ISLINKS+ISLOG+BKSYHELP+MTICMSTR+LANGDICT (full match to Pass 117); Pass 162 vars: FROM.CUST/FROM.ORDDTE/THRU.ORDDTE/TERRITORY/SHIP.DATE/SHIPVIA = filter range vars; REL.ALL/AUTO.BO/AUTO.RCOMM/DSP.COMMENTS/DSP.SHIPPED = operational mode flags (release-all, auto back-order, auto recommit, show comments, show shipped); TOT_UOH/TOT_UOSO/TOT_UBO/TOT_ORD = inventory totals (on-hand/on-SO/back-ordered/ordered); LOT_YN/SER_YN = lot/serial flags; NUM.LINES = order line count; FACTOR/FACTOR2 = pricing adjustment factors; ISBSF = KPI update on shipment; ISJAVA = Java email notification; ISREPLNK+ISREPORD = rep commission; ISGLDATE = GL-date posting control; ISSHPVIA(23f)+BKCMTERR(11f) extracted — **C: 76/100**
- [x] 🔄 **ED (EDII)** — EDI Invoice Import (T7EDII: 183 procs, src=LISTG60.LIB, 43t); ETBCOMBOVAL = LISTG60.LIB grid confirmed; full inbound EDI→AR invoice pipeline: 42 of 43 tables in DDF (only FILELOC unregistered); EDII uses identical code path as manual SO entry — customer/item lookup, BKICPMAT pricing, ISTAXGRP taxes, BKGLTRAN GL, WORKORD WO link, LOT/SERIAL tracking; complete AR invoice creation without human interaction; Pass 162 vars: **IMP.FILENAME** = EDI import file path; DATE.FORMAT/DATE.FORM.ARRAY/DATE.CNTR/DATE.POS1/DATE.POS2 = multi-format EDI date parser (position-based date extraction from EDI records); FROM.CUST/FROM_PROD/FROM_LOC = customer/product/location filters; INCL.ROHS = include RoHS compliance flag; REBUILD = reprocess/rebuild flag; SELECT.LOCS = multi-location selector; ITEM.LIST/QTY.LIST/ESD.LIST/CUSORD.LIST/FS.FLAG.LIST/CUSCOD.LIST/REBSS.LIST/SKIP.LIST = parallel import arrays (item/qty/ESD/customer-order/flag/custcode/rebill/skip per line); SO.LIST/NEW.SO.LIST/SO.LINE.LIST = SO creation arrays (existing SO mapping + new SO assignment + line assignment); PRT.MULTI/PRT_SHORT = print options (multiple/shortages); HOLD.FPATH/FPATH = import file path hold var — **C: 76/100**
- [x] 🔄 **BR** — Brand / CRM Classification; T7BRANDS (53p, **40 tables** — CORRECTED from 27, Pass 157): BKCMACCC+BKAPPOL+BKGLTRAN+BKMRPFC+DBAFIFO+LOT+SERIAL+ISNCR+ISREMIND+ISTRIGRS+ISICMSTR+BKAPDESC+BKAPVEND+BKARCUST+BKCMACCN+BKICMSTR+BKSYHELP+DBAHLPID+FILELOC+ISDRILL+ISIS+ISLINKS+ISLOG+LANGDICT+MKAHIST+BKARINV+BKAPPO+TASCOLOR(+full tax+multi-currency handle set opened at session init); T7BRANDS is NOT just a brand code editor; IS.* feature flag vars from BKYSMSTR: IS.AUTO.TAX.CAL/IS.CC.*/IS.DEMO/IS.EZPAY/IS.IMAGING/IS.LANDED.COST/IS.MULTI.CPAY/IS.MULTI.CURR/IS.PO.TAX/IS.RETAIL.PRICE/IS.RMA/IS.UPC/IS.UPC.1/IS.UPC.2 — T7BRANDS manages system-wide feature flag configuration; TOLKEN = credit card token binding; ISPOSI.H = POS handle (confirms point-of-sale module integration); T7BROWSER (4p, src=t7browser.SRC) = CRM contact viewer; 55 tables opened (session init overhead — business tables: BKCMACCN+BKCMACCC); BKCMACCN(154f) + BKCMACCC(2f: CCODE+DESC) = brand category codes — **C: 72/100**
- [x] 🔄 **NE** — New Company Initialization (T7NEWINIT: 49 procs, 15 tables); FILELOC+FILEDES+BKAPVEND+BKARCUST+BKCMACCN+BKICMSTR confirmed; **FILEDES schema inferred from vars (Pass 117):** LOC_BUFF_NAME+COMP_CODE+DESCRIPTION+FILE_NAME+LOCATION+REC_SIZE+REC_TYPE = file template definition (file name + path + record size + type); BKYS.DATE/DESC/GLDPT/GLNUM/INVNUM/NUM/QCNUM/RBNUM/REQNUM/VNUM/WONUM/YN = BKYSMSTR initial auto-number values for new company; ESETTINGS = initial settings seed; PPARAMS = program params; FILLVAL = fill value for initial field values; purpose: creates all Btrieve .B data files for a new company from FILEDES templates, optionally seeds from existing company; Pass 157 symbols: DBN = company number (numeric identifier); LFN = logical file name being created; SEC.OK = security authorization result; FILE.OK = per-file creation success flag; MCNTR = file count iterator; LOC_H = FILELOC handle; DES_H = FILEDES handle; BKICLOCMHNDL = item-location master created; BKYSMSTRHNDL = system master seeded from source company; BKPSUSER_HNDL2/BKSYUSER_HNDL2 = user auth handles — workflow: auth→iterate FILELOC→read FILEDES→create .B file at LOC_LOCATION→seed BKYSMSTR — **C: 73/100**
- [x] 🔄 **CU** — WO Material Cut Sheet; 2 programs (T7CUTSHEET2: 75 procs, 56t, lot-enabled) + T7CUTSHEET2b (60 procs, 56t, no-lot variant); Pass164 symbol vars: WOMAT.* = full material issue schema (DATE/WOPRE/WOSUF/QTYISSUED/QTYSCRAP/SCRAPCD/LOT/SERIAL/PRODCODE/PRODDESC/KIT/PCODE/PDESC/SCDESC/COST/REF/EXTRA — 17 fields cross-validated vs WOMAT DDF); MTLOT.* = full lot tracking (CODE/KEY/LOT/EXPDATE/ONHAND/PO/RECDOC/VENDOR/RECDATE/RECQTY/POCOST/WO/INRECDATE/WOQTY/WOCOST/NOTES/LOC/WOSUF/EXTRA/BEGIN/OUT/MAXOUT — 22 fields); MTWO.WIP.* = WO production status (WOPRE/WOSUF/BLANK/MULT/SQTY/PRTY/SSTART/SFIN/ASTART/AFIN/COMQTY/STATUS/LOCK/ESETUP — 14 fields same as PA module); filters: EJOB/ELOT/EQTY/EPART + EUSER/EPASS authentication gate; summary vars: WOTOTQTY/ABIQTY/LEFTQTY/GT.MAT/GT.ISS/FABQTY; DB handles: WOEMAT.H/ICMSTR.H/WORKORD.H/LOT.H/WOBOM.H/BINLOT.H; ISBINLOT+ISDUTY+ISBROKER+BKGLTRAN; lot-enabled variant adds MTLOT.* traversal for lot-assigned components — **C: 82/100**
- [x] 🔄 Pass 55: WOBOM(24f: OPER+WOPRE+WOSUF PK, ASSY+COMPCODE, QTYPER+SCRAPQTY+TOTQTY+ASSYQTY+QTYISSUED, UM, EMATCST+AMATCST, REF+OPTION+VEND+BINLOC+UID+REV+SEQ)+WOMAT(17f: DATE+WOPRE+WOSUF PK, PRODCODE/DESC+PCODE/DESC, QTYISSUED+QTYSCRAP+SCRAPCD, LOT+SERIAL+KIT+COST+REF) fully extracted; cut sheet = WOBOM(required) vs WOMAT(issued) shortfall with ISBINLOT bin locations — **C: 72/100**
- [x] 🔄 **JO** — Jobs and Departments (T7JOBS: 21 procs, ISDEPT+WOEXCHG+ISCATMST+BKICLOCM+BKARCUST+BKAPVEND+ISBNMSTR+ISREMIND+ISNOTES+ISLINKS+WORKCTR+BKGLTRAN+BKMRPFC+DBAFIFO; ISDEPT(3f)=dept master, WOEXCHG(10f)=WO change orders with GL posting; T7JODPSALES(52 procs, IS2DBAR+ISCYCLCD+BKSBPART+BKAPDESC+ISUDFINV — 64 tables) = SM/item-inquiry drill-down panel; Pass 65: ISDEPT(3f: IS_GF_DEPT PK+DESC+MISC; GF_=GL Finance prefix), DBAFIFO(5f: PARTNO+QTY+COST+RECVDATE+REMAIN — FIFO costing queue), BKMRPFC(9f: PART+DATE PK+QTY/OQTY/CQTY+FLAG+DATE1+NUM+EXTRA — MRP firm commitments), BKAPDESC(5f); Pass 157: T7JOBS vars confirm: JCUST/JVEND/JDEPT/JITEM = per-job entity links; JARCUST.H/JAPVEND.H/JISDEPT.H/JICMSTR.H = 4 entity record handles; T7JODPSALES **Java-backed** (HOST/PORT/NAME/TREEDEST/COMP vars = EvoPVT.jar jdbc.ini pattern); ISUDFINV = new table (inventory UDF — not previously documented); 2 programs confirmed — **C: 73/100**
- [x] 🔄 **FN** — File Navigator / Btrieve Find+Replace (T7FNR: 104 procs, 15 tables, src=EVO.LIB+LISTG60.LIB); Pass164 additional vars: type-specific search arrays — DFIND_FIELD1..4 (date), NFIND_FIELD1..6 (numeric), AFIND_FIELD1..6 (alpha); DREPL_FIELD/NREPL_FIELD/AREPL_FIELD = type-specific replace targets; FILENAME/DNAME/ELEMENT = target file + field name; ACTION = replace action; FLNAME/FELEMENT = filter field+element; OPER = comparison operator; POS/SPOS/SLENGTH = position-based substring search; supports 3 data type search modes (date/numeric/alpha) with up to 6 simultaneous search fields; test-mode dry-run; admin TA-D tool — **C: 80/100**
- [x] 🔄 **XC** — Credit Card Cross-Reference (T7XCUTIL: 29 procs, 8 tables: BKCMACCT+BKYSMSTR+ISCC+LANGDICT+FILELOC+BKSYHELP+DBAHLPID+MKAHIST); ISCC(14f) fully documented; BKYS.DATE/DESC/GLDPT/GLNUM/INVNUM/NUM/QCNUM/RBNUM/REQNUM/VNUM/WONUM/YN = BKYSMSTR auto-number read (XC checks transaction numbering); BKCMACCT (CRM account type master — maps account to CC token via TOLKEN); TOLKEN = credit card vault token; XC maps CRM accounts to ISCC payment tokens; RVALF = return value float (token lookup result); Pass 157: T7XCUTIL vars confirm BKCMACCT access via BKCM.ACCT.* (35 field vars: CODE/OLDCD/ALPHA/NAME/ADD1-3/CITY/STATE/ZIP/CNTRY/CONT1/TITLE/PHONE/FAX/REP/DLOAD/SICCD/CUST/LEAD/START/TERR/REM/FONE/FTWO/FTHRE/FTIME/CCARD/CNUM/CEXP/CMPNM/PNAME/EXTRA/EMAIL/EMPS) — all 35 match DDF tier2 BKCMACCT(41f) schema — **C: 74/100**
- [x] 🔄 **LG** — LGS Customer Module — Canadian customs processing; SOE=Statement of Entry (Canadian customs declaration); **t7lgssoe.RWN** (170p, **src=LISTG60.LIB**, 42t, Pass 162): grid/list UI framework (ETBCOMBOVAL=embedded tree/combo nav; PROGRAM.HEADER=module panel wrapper); full 42-table DB: BKARINV+BKARCUST+BKARINVL+BKYSMSTR+BKICMSTR+MTICMSTR+BKARTXN+BKSYMSTR+BKICTAX+BKICLOC+BKSYHELP+DBAHLPID+ISIS+MKAHIST+ISLOG+ISDRILL+BKAPVEND+BKCMACCN+ISLINKS+BKAPDESC+**ISTAXGRP**+BKICLOCM+BKAPPOL+BKAPPO+WORKORD+WOBOM+INVTXN+BKBMMSTR+BKMRPFC+ISNUMBER+BKARINVT+ISICMSTR+BKGLTRAN+DBAFIFO+ISTRIGRS+ISREMIND+LOT+SERIAL+ISNCR (CORRECTION: ISTAXGRP IS used alongside BKICTAX; BKAPPOL/BKAPPO = import PO link; WORKORD/WOBOM = WO integration; DBAFIFO = FIFO cost layer; LOT/SERIAL/ISNCR = lot+serial+NCR); full tax handle set: ISTXG.HNDL/ISTXF.HNDL/ISTAX.HNDL/ISHTX.HNDL/HTAX.HNDL/ISMCF.HNDL/ISMCR.HNDL/ISDUTY.HNDL/ISBRK.HNDL/ISLDF.HNDL; domain vars: **RETEN.PER** = customs retention period; **BKAR.INV.RETEN** = invoice-level retention flag; **ISTS.EDATE** = SOE effective date; **ISTS.CFG.TRACK** = Canadian customs tracking mode; **ISTS.CFG.SOEDTE** = Statement of Entry date config; **ISTS.CFG.POEDTE** = Port of Entry date config; **ISTS.PATH/ISTS.CFROM** = customs file path and from-date; SCAN.QTY.CHAR/SONUM.CHAR = barcode scan input (touchscreen-enabled); LOT_YN/SER_YN = lot/serial control flags; FACTOR/FACTOR2 = customs duty calculation factors; UBO_FLAG/TOT_UBO = units back-ordered flags; LINE.PART/LINE.PQTY/LINE.UBO/LINE.TXAMT/LINE.RELEASE = per-line customs declaration fields; BKICTAX(46f): STATE+LOCAL PK, TAX/TAXY/STATE_AMOUNT/LOCAL_AMOUNT, TAXBLE_1..12/NONTAX_1..12/COLECT_1..12 12-month history, OUTSTD, EXTRA(100); **T7LGSSOEVerify.RWN** (41p, EVO.LIB, 14t): VERIFYFORM + SBVEND.H/SBMFG.H (sub-vendor/manufacturer handles for origin compliance) + MCLASS.H (material class) — pre-submission validation with vendor/manufacturer origin check — **C: 76/100**
- [x] 🔄 **JS** — JS Integration / Reporting Bridges; Pass 44: 9+ programs identified: T7JSETTINGS(70p, FILELOC config)+T7JUPD(27p, deploy)+T7JSACC(50p, AR accounts)+T7JSAIC(50p, item-customer)+T7JSAPBI(50p, AP BI)+T7JSASRS(50p, AR sales)+T7JSOI(50p, SO invoice)+T7JSQL(52p, SQL query)+T7JTREE(52p, tree view)+T7JTEMP(27p stub); all share 64-table ISDRILL-based DB set; export EvoERP data to JS-based BI layer (Sisense/similar); T7JSETTINGS configures connection, T7JUPD deploys; Pass 157 sym extract: **all JS programs Java-backed** (HOST+PORT+NAME+TREEDEST+COMP vars = EvoPVT.jar jdbc.ini pattern — same as QU-F); T7JSETTINGS additionally has TENMIN.KILLER+TENMIN.TIME = 10-minute BI connection session keepalive/timeout; T7JSQL has DICT_HNDL+KNUM_HNDL+KEY_HNDL = reads Btrieve table schemas via FILEDICT/FILELOC API to dynamically generate SQL; T7JSOI has JAVA.PATH = Java launcher; VS/INIT/POST/CO.LOC/NO.POST = display state vars shared by all JS programs; architecture: T7JS* TAS stub → EvoPVT.jar Java layer → EVOBI2 BI database → Sisense dashboards; Pass 159: **T7JAVASET.RWN (57p, EVO.LIB, 9t)** is a DISTINCT program from T7JSETTINGS — T7JAVASET configures the basic Java connection URL/HOST/PORT/NAME values in BKYSMSTR for all modules; T7JSETTINGS (70p) is Sisense BI-specific (adds SERIAL7+CDEF.BUFF+SERVER_PATH+CDEF.STOP = Sisense connection license and serialization params); T7JAVARUN.RWN (11p, NZEVO.LIB) = minimal Java runner shim from the NZ framework library — **C: 80/100**
- [x] 🔄 **BS** — Business Score/Summary Dashboard; writer/viewer split confirmed (Pass 114, 2026-06-19): T7BS.RWN (162 procs) = KPI writer — populates ISBSF from 40+ tables; EVOBS.RWN (128 procs, QU-D) = KPI viewer — reads ISBSF + live BKGLTRAN/MTICMSTR; ISBSF (143f) PK=STARTDATE+ENDDATE; var-confirmed fields: ISBSF.STARTDATE/ENDDATE (date range), ISBSF.AR.BAL/BILL/RECP/DISC/COGS (AR KPIs), ISBSF.AP.BAL/PAYA/PAYM (AP KPIs), CASH_TOTA+ACT1..9+CASH_ACTS_1..100 (100-period GL history), WOS_SETUP/LAB/OUTP/MAT/FOH/VOH/MEXT/FP/WIPV (WO cost breakdown); T7BS opens ISBANKS (cash balance from bank accounts), ISGLDATE (7-year period-date nav); ISBSF+ISGLDATE+ISBANKS+GL set fully explains KPI calculation; Pass 159: **t7jbs.RWN (63p, LISTG60.LIB, 64t)** confirmed — LISTG60 drill-down panel framework (same as T7JCRM/T7JODPSALES); ETBCOMBOVAL = embedded tree/combo selector; 64-table session init = ISDRILL-based set; t7jbs = Java Business Score embedded panel (in-session drill-down into BS KPI data without leaving current module); **Pass166 T7BS.RWN var query: 45 ISBSF.* field-access vars confirmed** — complete field set: AR: BAL/BILL/RECP/DISC/COGS/DEPO; AP: BAL/PAYA/PAYM/DISC/**ATP** (available-to-pay); SO: OPEN/BOOK/SHIP; PO: OPEN/BOOK/RECP/**PORNI** (received-not-invoiced); WO: WIPBAL/ISSU/FPVAR; WOS (WO cost components 9x): FOH/FP/LAB/MAT/MEXT/OUTP/SETUP/VOH/WIPV; CASH: TOTA + ACT1..ACT9 (9 bank accounts) + ACTS (sum); **IC.VALUE** (inventory value); STARTDATE/ENDDATE/EXTRA — AP.ATP+AR.DEPO+IC.VALUE+PO.PORNI all new; ISBSF has 143f DDF total; 45 var-confirmed access field names; cash is 9 bank accounts (not 100 periods as previously noted — correction to prior doc) — **C: 88/100**
- [x] 🔄 **AD (ADCA)** — Advanced Data Collection (T7ADCA: 290 procs, 55 unique tables, src=ISTECH.LIB); full auto shop floor DC: BKDCLAB+WORKORD+BKPRMSTR+BKDCSHFT(34f, 3-shift config)+ISWOEX(63f Pass 64 confirmed in DDF: WOPRE+WOSUF PK, 5 dates+5 ints+2 floats+5 alphas(30)+5 descs+10 flags+5 gnums+5 alphas+5 notes(100))+ISROUTEX(100f Pass 64: CODE+OPER PK, 10 machine cycle-time slots, 45+ configurable fields)+ISWOROEX(60f Pass 64: WOPRE+WOSUF+OPER PK, per-WO-op routing extension)+OPQCDESC(10f Pass 64: WOPRE+WOSUF+OPER PK, per-op QC result desc)+ISWOTRAY(52f Pass 64: TRAY_NUM PK, WO/oper/qty/QC/4 bins+37 fields)+EIMCOLST(not in DDF); operator scans→posts BKDCLAB→updates WOLABOR/WOROUT; Pass 109: T7ADA/B/C confirmed non-existent (only T7ADCA); BKDCSHFT all 34 fields decoded (3 names + 30 time fields per shift + EXTRA); ADCA vs PA functional distinction documented; Pass 160: **BKDCLAB full field schema from LAB.* vars**: LAB.DATE/EMP/WOPRE/WOKEY/WOSUF/OPER/POSTED/SHIFT/START/FINISH/PARTS/SCRAPPED/NOJOBS/RUNHRS/SETUPHRS/REGOVER/EXTRA/APPROVAL/SCRAPCD/SCRAPQTY = 20 fields confirmed; **LAB.JCNUM** = Job Cost number (BKDCLAB integrates with JC module — shop floor labor charged to job!); LAB.ADT.SUPER/IN/OUT = supervisor + timeclock punch in/out (attendance tracking); LAB.ESSDATE = ESS date (Employee Self-Service web submission date); LAB.CYCLE.HR/MIN/SEC = machine cycle time capture (3-part: hours/minutes/seconds for SPC analysis); LAB.REGOVER = regular/overtime classification; LAB.APPROVAL = supervisor approval flag for labor records — **C: 78/100**
- [x] 🔄 **IT** — Item Serial/Barcode/Cycle Config (T7ITMCFG: 66 procs, src=LISTG60.LIB, 64t); ETBCOMBOVAL=LISTG60.LIB confirmed; opens ISSERCNT+BKICMSTR+BKGLCOA+SERIAL+ISNCR+IS2DBAR+ISCYCLCD; ISSERCNT(9f): IS_SERC_ITEM(15)+CLASS(4)+SPOS+LENG+TOTAL+NUMBER(counter)+LAST(25)+EXTRA+L2; IS2DBAR(109f): barcode format config; ISCYCLCD(7f): IS_CYCLE_CODE(4)+DESC(30)+FREQ+DATE+ALPHA(15)+NUM+EXTRA(50); Pass 162 vars: **IS.SERC.ITEM/CLASS/SPOS/LENG/TOTAL/NUMBER/LAST/EXTRA/L2** = all 9 ISSERCNT fields accessed via IS.SERC.* = cross-validates DDF schema exactly; **SER.FORMAT** = serial number format template string; **SSIZE/SPOS/ANUM** = serial format components: size/position/alphanumeric flag; **TOT.LOCS** = total location count; **ITMCFG.H** = ISSERCNT record handle; REC.NUM = serial record navigator; XRETFLD = extended return field; full tax handle set (ISTXG/ISTXF/ISTAX/ISHTX/HTAX/ISMCF/ISMCR/ISDUTY/ISBRK/ISLDF); 64 tables (far more than 7 previously noted — includes full session init overhead) — **C: 76/100**
- [x] 🔄 **CH** — Multi-Location Chain (T7CHAIN: 62 procs, ISCHAINM+BKPSUSER+BKSYMSTR+LANGDICT; T7CHAINM: 40 procs, ISCHAINM+FILEDICT); ISCHAIN/ISCHAINM(17f identical)=USER(15)+PARENT(12)+CHILD(12) PK + PARAM_1..10(15 each)+AUTO(1)+DATE+DESC(100)+EXTRA(100); Pass 135 (2026-06-19): confirms both ISCHAIN+ISCHAINM exist (active dispatch + master/template pair); Pass 153 (2026-06-22): T7CHAIN.DFM+T7CHAINM.DFM fully read; IS.CHAIN field bindings confirmed (USER/PARENT/CHILD/AUTO/DESC/PARAM[1-5]); 19 parent programs + 30+ child programs confirmed from combo Items.Strings; AUTO Y/N/A semantics confirmed — **C: 82/100**
- [x] 🔄 **PA** — Paperless DC / Shop Floor Control (T7Paperless: 205 procs, 50 unique tables, src=LISTG60.LIB; T7PACKMENU: 5 procs stub; T7PASS: 3 procs password sub); ISBINLOC(9f)=bin-level inventory without lot (ITEM+LOC+BIN PK, UOH, DFLT, RVLVL); opens WORKORD+ROUTING+WOROUT+BKICLOC+ISBINLOC+ISWOEX+WORECV+BKAPPOL+ISWOTRAY+BKDCLAB; Pass 43: 50-table DB fingerprint re-confirmed; BKDCLAB+ISWOTRAY confirm PA=touchscreen DC identical function to ADCA; BKAPPOL confirms outside process PO receiving from floor; Pass 109: PA vs ADCA distinction: PA opens WOMAT+INVTXN+ISBINLOT+WOBOM+ISACCESS (material issues + bin-lot + license gate); ADCA opens BKPRMSTR+BKDCSHFT (payroll + shift); T7PASS=password sub with 45-table session init; Pass 160: **SCAN.WO + SCAN.OPER** = dual barcode scan workflow (WO number + operation barcode); MTWO.WIP.LOCK = concurrent-entry lock (prevents duplicate posting); MTWO.WIP.ASTART/AFIN = actual start/finish timestamps (vs MTWO.WIP.SSTART/SFIN scheduled); MTWO.WIP.ESETUP/EMAT/EOUTPR/ELABOR = estimated cost breakdown (setup/material/output/labor); MTWO.WIP.ASETUP = actual setup cost (estimate vs actual comparison); MTWO.WIP.COMQTY = completed quantity; MTWO.WIP.STATUS = WO routing status; LISTG60.LIB = touchscreen-optimized grid/list UI framework — **C: 78/100**
- [x] 🔄 **TE** — NACHA/ACH Electronic Payments (T7TESTNACHA: 103 procs, 18t, src=LISTG60.LIB); BKGLCHK(11f)=check register: CHKACT+NUM PK, DATE+TYPE+NAME+AMT+FLAG+DATER+VEND+CUST; ISBANKS(23f) fully extracted: NUM(2)+SRT PK, DESC(40)+GLA/GLD(GL account+dept)+NXTNUM(next check#)+BAL+ROUT(15 ABA routing)+ACCT(15 bank acct)+CURR(3)+TYPE(2)+VEND(10)+ACTIVE+INC_BS+AR/AP/PR flags+RTM_1..5(12, report templates)+EXTRA; generates NACHA ACH files from ISBANKS routing/account + BKAPVEND payment data; Pass 160: **WELLS.ID** = Wells Fargo bank company ID (hardcoded field for WF ACH format); ACH.FILENAME = output ACH file path; BATCH.CNTR = NACHA batch counter (tracks batch header/trailer); FROM.CHKNUM/THRU.CHKNUM = check number range filter; FROM.CHKDATE/THRU.CHKDATE = date range filter; FROM.VEND/THRU.VEND = vendor range; EFF.DATE = ACH effective date; WHICH = include-all/filter selector; CHK.D1/D2/M1/M2/Y1/Y2 = date component parsing (day/month/year 2-char each → NACHA 6-char YYMMDD format); LISTG60.LIB = grid/list framework — **C: 77/100**
- [x] 🔄 **KI** — Kit Assembly (T7KIT: 153 procs, src=EVO.LIB, 26t); opens BKICMSTR+MTICMSTR+WOBOM+BKICLOC+BKYSMSTR+ISLINKS+WOMAT+WORKORD+WOROUT+BKPRMSTR+ISBINLOC+LOT; assembles kits from BOM components using simplified WO without routing/labor; lot+bin location tracking; Pass 43: DB fingerprint re-confirmed; ISLINKS confirms document attachments; Pass 162 vars: **MTIC.PROD.*** = full MTICMSTR field access for kit components: CLASS/CODE/DESC/SUM/PUM/PCONV/CYCLE/ABC/LOT/SER/ACTIV/STDPK/WT/CUBFT/LEAD/LOC/DRAW/REV/COST/ESTCD/MRP/GLINV/INVDP/GLWIP/WIPDP/SPECS/UOWO/UOA/COMM/STDC/TYPE/SUBST/FRT/MRPSW/UIWIP/AVAIL/OPTPR/CUST/CUSNM = 40 MTICMSTR fields accessed by T7KIT; MTIC.PROD.UIWIP = units in WIP (checked before kit issue); MTIC.PROD.AVAIL = available qty; MTIC.PROD.MRPSW = MRP switch on component; MTIC.PROD.CUSNM/CUST = customer-specific kit component; BKIC.IS.DCODE = discontinued flag checked before kit assembly — **C: 76/100**
- [x] 🔄 **EM** — Emergency GL Maintenance (T7EMGL: 62 procs, 33 unique tables); full DB fingerprint confirmed (Pass 115): BKGLCOA+BKSYHELP+DBAHLPID+ISIS+MKAHIST+ISLOG+ISDRILL+BKAPVEND+BKARCUST+BKCMACCN+BKICMSTR+ISLINKS+BKAPDESC+LANGDICT+ISTAXGRP+ISNUMBER+BKICLOCM+BKAPPOL+BKAPPO+WORKORD+WOBOM+INVTXN+BKBMMSTR+BKMRPFC+FILELOC+ISICMSTR+BKGLTRAN+DBAFIFO+ISTRIGRS+ISREMIND+LOT+SERIAL+ISNCR; BKGLCOA(65f) fully extracted: ACCT(10)+GLDPT(4) PK, ACCTD(25)+TYPE(1)+CR_DR(1)+NON_CASH(1), CURRENT_1..14+BUDGET_1..14+1YPAST_1..14+1YPAST_YE+2YPAST_1..14+2YPAST_YE+EXTRA(50); new finds: BKMRPFC (MRP forecast table, opens for cost reference), DBAFIFO (FIFO cost layers), ISTRIGRS+ISREMIND (trigger+reminder system), LOT+SERIAL+ISNCR (lot/serial/nonconformance — deep override capability); EM = most privileged maintenance tool: can touch GL accounts, AP/PO transactions, WO/BOM, inventory txns, FIFO cost layers, lot/serial records; Pass 153 (2026-06-22): T7EMGL.DFM fully read; BKGL.ACCT/GLDPT/EXTRA field bindings confirmed; EXTRA=GL Account Link; Add/Delete/Save toolbar confirmed; from.glacct+from.gldpt filter confirmed — **C: 78/100**
- [x] 🔄 **QS** — Quick Sales Order / Web Order Staging (T7QSOA: 72 procs, 39t, src=EVO.LIB + T7QSOALines: 70 procs, 18t, src=LISTG60.LIB); ISQSOA(12f) schema all confirmed; Pass164: **T7QSOA adds ICPMAT.H** (BKICPMAT customer pricing matrix handle) + **PRSALE.H** (price/sale handle) = confirms QS entry checks customer-specific pricing matrix before creating SO; GETTING.CUST/SHIPTO = customer lookup + ship-to mode; CHK.QTY = available qty check; SYMSTR.H/ICREF.H/BMMSTR.H = system master/item cross-ref/BOM handles; **T7QSOALines accesses BKARINV (invoice header) for prior-order line history** via BKAR.INV.* vars: NUM/SONUM/INVCD/INVDTE/CUSCOD/CUSA1/CUSNME/CUSA2/CUSCTY/CUSST/CUSZIP/CUSCNT/CUSATT/SHPCTY/SHPST/SHPZIP/SHPCOD/SHPNME/SHPA1/SHPA2/SHPATN/SHPVIA/SHPCNT (23 BKARINV field names confirmed); workflow: ISQSOA staging → pricing matrix check → QTY check → create BKARINV/BKARINVL; **Pass166 J7SyncWOtoSO (153p, 54dbs): 86 BKAR.INV.* + 28 BKAR.INVL.* access vars confirmed** — most complete BKARINV/BKARINVL namespace to date: BKAR.INV.* 86 unique fields: key (NUM/SONUM/INVCD/INVDTE/ORDDTE/SHIPDT/INDATE/MDATE/DATES), customer addr (CUSCOD/CUSNME/CUSA1/CUSA2/CUSCTY/CUSST/CUSZIP/CUSATT/CUSCNT/CUSORD), ship-to (SHPCOD/SHPNME/SHPA1/SHPA2/SHPCTY/SHPST/SHPZIP/SHPATN/SHPCNT/SHPVIA), **bill-to** (BILCOD/BILNME/BILA1/BILA2/BILA3/BILCTY/BILST/BILZIP/BILATN/BILCNT — 10 new fields!), financials (SUBTOT/TAXAMT/FRGHT/TOTAL/COGS/DEPAMT/COMAMT/CCOAMT/CHKNUM), sales (SLSP/SLSP2/ENTBY/PCODE/DCODE/COMMPR), tax (TAXABL/TAXRTE/TAXKEY/ISTXKY/ITMZTX/AVATAX), multi-currency (ISCUR/ISMCDT/ISREV/ISRVDT), misc (LOC/GLDPT/NL/ENDLNE/JOBNUM/RELNUM/RETEN/RTS/SCCOGS/TRACK/FOB/QSTAT/DROP/ALPHAS/DESC/MISC/FLAGS/EXTRA/SHIPPR/LINV#P); BKAR.INVL.* 28 unique fields: INVNM/KEY/CNTR/PCODE/PDESC/PQTY/PPRCE/PDISC/PEXT/PCOGS/ITYPE/TXBLE/TXAMT/ESD/ASD/UBO/USTD/ABQTY/OOQTY/LOC/UM.LN/FRGHT/COMPR/COOP/JOB#/RTS/SCCOG/EXTRA — matches DDF BKARINVL(28f) exactly — **C: 87/100**
- [x] 🔄 **VSCHED** — Visual Work Center Capacity Scheduler (T7VSCHED: 94 procs, src=EVO.LIB, 22t); WCTRLOAD(8f: WC+DATE PK, TOTHRS+UDATE+CAP+UTIL+LOAD+EXTRA(100)); full DB fingerprint: WORKORD+WOROUT+WCTRLOAD+BKICMSTR+FILELOC+BKYSMSTR+BKARINV+BKARINVL+BKSYHELP+DBAHLPID+ISIS+MKAHIST+ISLOG+ISDRILL+BKAPVEND+BKARCUST+BKCMACCN+ISLINKS+BKAPDESC+ISACCESS+LANGDICT+BKSYMSTR; WCTRLOAD = pre-computed daily WC capacity snapshot; BKARCUST+BKARINV+BKARINVL = customer demand overlay; ISDRILL+ISLINKS+BKAPDESC = drill-through; ISACCESS = license gate; Pass 157: WorkCenterLoad.jar (com.evoerp.wcload.javafx.App) = Java-side visual scheduler; Pass 162 vars: **HOST/PORT/NAME/JAVA.PATH** = Java-backed (EvoPVT.jar, same pattern as other Java programs — VSCHED is a TAS stub for WorkCenterLoad.jar); **VS/INIT/POST/COMP/CO.LOC/NO.POST** = EVO.LIB Java bridge state vars; **ETBCOMBOVAL** = LISTG60.LIB grid (EVO.LIB can embed LISTG60 components); **ADD.ITEM/ADD.QTY/ADD.WONUM/ADD.WOPRE/ADD.WOSUF/ADD.SSTART/ADD.SFIN/ADD.STATUS** = WO addition vars (user adds WO to schedule from within VSCHED); **SADD.ESTNUM/ADD.ESTNUM** = estimate number (VSCHED links to ES estimating!); **ESTHDR.H/ESTLNE.H/ICEST.H** = estimate header/line/IC-estimate handles (shows estimated workload alongside actual WOs!); WOSROUT.H/WOROUT.H/WORKORD.H/WORKSORD.H/WOSBOM.H = WO+routing+BOM handles; DICT_HNDL/LOC_HNDL/LOC_* = FILEDICT API (dynamic table navigation for export); **OK.TO.ADD.WOS** = validation gate; WOS/WCS = WO/WC state machines; START.WOPRE = WO range start — **C: 79/100**
- [x] 🔄 **TPOA** — PO Processing Approval Hub (TPOA: 499 procs, src=LISTG60.LIB, 61t); ETBCOMBOVAL = LISTG60.LIB grid confirmed; DB fingerprint (Pass 115): BKAPPO+BKAPVEND+BKAPDESC+BKAPPOL+MTICMSTR+BKYSMSTR+ISTERMS+ISNOTES+ISLINKS+ISAPEX+BKSYMSTR+BKARCUST+BKICMSTR+BKICLOCM+WORKORD+WOBOM+WOROUT+BKRFQ+ISECO+ISORDDSC+ISORDECO+ISJOB+BKSBVEND+BKSBMFG+ISAPCHG+ISDIGSIG+WORKCHG+CALENDAR+ISMCF+ISMCR+BKARINV+BKARINVL+BKARINVV+BKAPINVL+ISTAXFIL+LOT+SERIAL+ISNCR+BKGLTRAN+MKAHIST; ISAPEX(33f) = approval gate engine; ISNOTES(13f) extracted; ISAPCHG = approval audit log; ISDIGSIG = digital signatures on PO; BKSBVEND/BKSBMFG = subcontracting vendor/mfg; WORKCHG = WO engineering changes; BKRFQ = RFQ link; ISECO = ECO integration; ISJOB = job costing link; CALENDAR = PO due date; 499 procs = largest standalone program; Pass 162 vars: **DIGSIG.H** = digital signature handle (ISDIGSIG); **USING.DIGSIG/NEW.DIGSIG.REQD/PRE.DIGSIG** = signature workflow flags; **APCHG.H** = ISAPCHG approval audit handle; **SEC.LEVEL** = security level for approval gate (links BKSLEVEL); **SCAN.QTY/SCAN.QTY.CHAR/SCAN.WO** = barcode scan on PO receipt (WO+qty barcode input); **BKAP.VENDCODE/NAME/ADD1-3/CITY/STATE/ZIP/CONTACT/TELEPHONE/COUNTRY** = vendor address vars; **BKAP.OUTINV/LASTPURCH/LASTPMT/PURCH.MTD/YTD/LYR/VAR/OUT.CREDIT** = vendor purchase history; **BKAP.CUST.CODE** = vendor's customer code (vendor↔customer cross-link!); **BKAP.GL.ACCT/DPT** = vendor default GL; **BKAP.IS.TAXGRP/TAXIN/MCCODE/DCODE/CREDLIM/REQQC** = vendor feature flags; **SCREEN.LOCKED/PONUM.LOCKED** = concurrent editing protection; USE.ACTIVE.PO = draft→active state; SCREEN.PO/SCREEN.POTEMP = PO vs temp-PO mode — **C: 76/100**

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
- [x] ✅ Files: EvoLinks.RWN, EvoLinkCVT.RWN — **C: 82/100**
- [x] ✅ Attachment storage table = **ISLINKS** — confirmed 2026-06-17 (EvoLinks.RWN opens ISLINKS as primary; ISLINKS = record-key → document filename cross-reference)
- [x] ✅ DB table for link mapping identified and all fields documented — IS.LNK.UID/LINK/APP/TYPES/PCB/DEF/GLOBAL/OPENWITH/DATE/NOTE/WHO/ATYPE/EXTRA/PRIVATE/SORT/ALPHA + FILELINK/LEXIST/GEN.ID/INVENTORY.LINK + E/PG thumbnail/component vars (Pass 110e, 2026-06-19) — **C: 75/100**
- [x] ✅ Attach / view / delete workflow traced — GEN.ID=owning record key; IS.LNK.PCB[100]=multi-record attach; BKAPVEND/BKARCUST/BKCMACCN/BKAPDESC entity lookups; BKYSMSTR/BKICMSTR for parts; FILELOC for path translation; two-tier doc system (E.*=engineering, PG.*=purchasing) with thumbnail support; **Pass165 EvoLinks.RWN (156p, 16 dbs)**: app launchers: WFA/OFA/XOAPP/OTHERAPP (open linked file with Word for Windows, other app, or external); GLOBALPATH = global base path for file links; alert vars: ALERTS/LINKS.ALERT/LINKS.ITM.ALERT = link notification triggers; IS.LNK.* 16 ISLINKS field access confirmed end-to-end (UID/LINK/APP/TYPES/PCB/DEF/GLOBAL/OPENWITH/DATE/NOTE/WHO/ATYPE/EXTRA/PRIVATE/SORT/ALPHA); DB fingerprint=16 tables: ISLINKS+ISSOBOX+BKICMSTR+MTICMSTR+FILELOC+BKYSMSTR+BKARCUST+BKAPVEND+BKCMACCN+BKAPDESC+ISIS+MKAHIST+ISLOG+ISDRILL+BKSYHELP+DBAHLPID — **C: 82/100**

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
- [x] ✅ Calendar sync logic confirmed from DB fingerprint (Pass 113 2026-06-19) — **C: 68/100**
  - CALREM.RWN (142 procs): opens BKYSMSTR+ISREMIND+BKARCUST+BKAPVEND+BKICMSTR+BKCMACFC+BKCMACCN+BKPSUSER+ISLOG
  - ISREMIND = primary data source (syncs EvoERP reminders → Google Calendar events)
  - Date handling vars: ISTS.EDATE/ENTRY.DATE/DATE_TYPE/MM/DD/YY/START.DATE/CHK.DATE (calendar date construction)
  - BKARCUST+BKAPVEND+BKCMACCN = entity context for event subject/description
  - CALREMGC.DFM = Google Calendar sync dialog (no separate CALREMGC.RWN; sync runs inside CALREM.RWN)
  - BKYSMSTR flag controls whether Google Calendar sync is enabled globally
  - Pass 157: **EvoToOutlookAppt.jar** (com.evoerp.outlook.appointments.main.Main) confirmed — CALREM also supports Outlook appointment sync (separate path from Google Calendar)
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
- [x] 🔄 **Full Java JAR inventory** (Pass 157, 2026-06-22): 37 application JARs enumerated on DBAMFG$; all Main-Class values confirmed; module assignments confirmed via com.evoerp.* package names; see HELP-RESOURCES.md "Java Application Inventory" section for complete table. Key new finds: WCScheduler.jar(SL), WorkCenterLoad.jar(VSCHED), FOTree.jar(FO), BOMTREE.JAR+EditBOMTree.jar+BomUtility.jar(BM), BusinessStatus.jar(QU-D), EvoToOutlookAppt.jar(CALREM), 5×salesanalysis.*(SA), EVOAVATAX.JAR(AvaTax), EvoScreenshot.jar, SMTPCLIENT.JAR — **C: 72/100** (Main-Class confirmed for all; TAS stub→JAR dispatch mapping not yet traced for most modules)

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
- [x] ✅ **New company creation** — UT → company add, NE module (T7NEWINIT: 49 procs) — see Recipe 16; Pass 153 (2026-06-22): T7NEWINIT.DFM fully read; "check and create missing data files" confirmed from form label; Go+Exit+fileslabel(progress) confirmed — **C: 78/100**
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
- [x] ✅ All remaining BKAP\* (24 tables) — Pass 142 (2026-06-22): full AP family documented at schema level in tier2-tables.md — BKAPACCN(154f 10-contact), BKAPDESC/BKAPADSC/BKAPHDSC(5f each BK_DESC_*), BKAPDEP(6f dept code), BKAPEIVT(19f entry ivt), BKAPEVND(73f entry vendor), BKAPCHKF/BKAPCHKH(12f check file/history), BKAPACCN(154f), BKAPRIVL(390f reversed invoice GL dist), BKAPAPO/BKAPAPOL/BKAPHPO/BKAPHPOL/BKAPRFQ/BKAPRFQL/BKAPPO/BKAPPOL(PO family 57-38f), BKAPQUOT(49f), BKAPVND2(63f), BKAPNOTE(8f) — **C: 82/100**
- [x] ✅ All remaining BKAR\* (27 tables) — Pass 42/142 (2026-06-22): full AR family documented — BKARCUST(106f), BKARECST/BKARSHIP(106f identical), BKARDEP(6f), BKARDESC/BKARDPST/BKARHDSC/BKARRDSC(5f BK_DESC_*), BKARDPST(5f), BKARECST, BKAREIVT(invoice temp), BKARHINV/BKARHIVL/BKARHTAX (history), BKARINV(84f header), BKARINVI/BKARINVV(AR variants), BKARINVL(28f lines), BKARINVT(19f open-item), BKARRINV/BKARRIVL(recurring), BKARSHIP, BKARSIVL(ship lines), BKART(12f payment), BKARTNOT(notes), BKARTXN/BKARTXNB/BKARTXNS(lot/serial txn) — **C: 80/100**
- [x] ✅ All remaining BKGL\* (28 tables) — Pass 40 (2026-06-19): full GL family documented in module docs: 4 COA tables (BKGLCOA/CCOA/ECOA/FCOA 62-65f), 8 transaction tables (16f each), 4×2 journal tables, BKGLFSTL(12f), BKGLSTMT(104f), BKGLDESC(5f), BKGLACHK+BKGLICC(11f each), BKGLXH(20f) — **C: 75/100**
- [x] ✅ All remaining BKIC\* (16 tables) — Pass 124 (2026-06-19): all 16 BKIC* entries fully field-documented in tier1-tables.md — BKICMSTR(64f item master), BKICAMTR/BKICEMTR(64f identical multi-company mirrors), BKICLOCM(12f warehouse/location address), BKICLOC(32f item×location qty+GL), BKICELOC(32f identical "E" mirror), BKICPMAT(85f price matrix 10-tier), BKICAPMA(85f identical "A" mirror), BKICTAX(46f jurisdiction+12-period accumulators), BKICREQ(41f requisition+WO/PO links), BKICDIM(47f material dimensions/metallurgy), BKICREF(8f customer part cross-ref), BKICMFG(6f manufacturer cross-ref), BKICALTD(16f alternate item detail+specs), BKICALTP(6f alternate item pricing link), BKICVAL(4f periodic valuation snapshot) — **C: 90/100**
- [x] ✅ All remaining WO\* (30 tables) — Pass 141 (2026-06-22): all 30 WO* tables documented; WORKORD(74f WO header), WORKIP(74f WIP), WORKCTR(13+f work center), MTWORO(81f routing operation), WOLABOR(17f labor), WORECEIPT(11f receipt), WORKACHG/WORKCHG(25f each change audit), WOE/WOH/WOM/WOR* families (estimated/history/material/routing); see docs/03-modules/wo-work-orders/README.md — **C: 92/100**
- [x] ✅ All MT\* tables — Pass 146 (2026-06-22): all 6 MT* + 3 adjacent tables documented in tier2-tables.md — MTICMSTR/MTICAMTR/MTICEMTR/MTINVDEF (108f × 4 identical MTIC_PROD_* schema: 10 vendor arrays, 12 spec lines, 15 replacement costs, CLASS+CODE PK); MTEXCHG (7f exchange rate, 6-decimal); MTMRP (13f MRP planning, PEGTO+ACTION); MWOPTEMP (8f WO completion temp); NOTETEMP (5f BK_DESC_* note staging); NZITPRE (15f WO prefix auto-number). Pass 152 (2026-06-22) updates: NZITPRE corrected to 54f (18×PREFIX+18×NXTNUM+18×DESC); MTEXCHG PK confirmed as CODE+LINE — **C: 85/100**
- [x] 🔄 All remaining BKPR\* (16 tables) — BKPRMSTR (384f fully grouped), BKPRCURP/BKPRHIST (127f each), BKPRINFO (128f), BKPRSALE/BKPRBOOK (87f each), BKPRTC (7f), BKPRTCFG (205f) documented; BKPRFTAX (47f), BKPRGLFL (664f), BKPRACOM/BKPRCOMM/BKPRHCOM (12f each), BKPRAGNT (4f), BKPRSTFL (2f) summarized — **C: 88/100**
- [x] ✅ All remaining BKBM\* (10 tables) — Pass 129 (2026-06-19): all 10 schemas extracted and field-level documented in tier1-tables.md; 5-table core cluster (BKBMMSTR/AMTR/EMTR/AVAL/SUMM all 26f identical), remarks/notes/dim/cnfg satellites fully interpreted — **C: 80/100**
- [x] 🔄 All remaining BKCM\* (46 tables) — Pass 133 (2026-06-19): all 46 tables field-documented in tier2-tables.md; full cluster architecture (account/contact/activity/prospect/vendor/dunning/mail/locks/temps); BKCMACCT(41f)/BKCMACCN(154f)/BKCMACTH(21f)/BKCMCUST(106f)/BKCMPCNT(24f)/BKCMREP(14f)/BKCMTERR(11f)/BKCMMHST(72f)/BKCMDUN(36f)/BKCMHCOD(9f) all field-level docs; mirror architecture (BKCMDE/BKCMEACT/E-mirrors) confirmed; BKCPEC(10f)+BKCPMSTR(9f) Checkmark Payroll tables also documented — **C: 82/100**
- [x] ✅ All remaining BKSO\* (7 tables) — Pass 110e/127 (2026-06-19): all 7 documented; BKSOHLOT/BKSOHSER (lot/serial ship tracking, 14f each), BKSOLOCK (5f edit lock), BKSONOTE (5f notes), BKSOPO (16f MRP planned PO), BKSOX/BKSOXH (25f SO supplemental + archive); SO uses BKARINV/BKARINVL directly (no separate SO master) — **C: 93/100**
- [x] ✅ All remaining BKDC\* (7 tables) — Pass 130 (2026-06-19): all 7 documented in tier1-tables.md; 5-table identical LAB_* pipeline cluster (50f each, DATE+EMP+WO+OPER PK), BKDCSHFT (34f, 3-shift schedule), BKDCCFG (7f, data collection config) — **C: 82/100**
- [x] ✅ All remaining IS\* tables — Pass 135 (2026-06-19) adds: ISCAR(35f: CAPA/NCR CA report, IS_NCR_* prefix clone), ISCARFUP(13f: CAR follow-up 5 milestone dates), ISCHAIN/ISCHAINM(17f identical: USER+PARENT+CHILD PK, 10 PARAM slots, multi-company chain dispatch), ISBMESA/ISBMEST/ISBMTMP(26f identical: BKBM_* BOM estimating mirrors), ISCRISLS(24f: CR/SO approval sales tracking per CUST+ITEM), ISCTREVU(17f: contract review employee+MOTPAS signature), ISCONVRT(9f: item UOM conversion SCONV/PCONV/WTCONV), ISCATMST(3f: category master), ISCYCLCD(7f: cycle count frequency), ISBOLMS(22f: ISSO_BOX_* BOL manifest clone), ISBRANDC/ISBRANDS(2f each: brand category/class, BKCM_ACCC/ACCL prefix), ISCCBTXN(16f: i2 custom corrugated-cut txn), ISCCICM(10f: i2 custom fabric/cover item master), ISCCMTF/ISCMGRP(2f each: CC MTF mapping); Pass 134 adds: ISIS(23f)/ISBANKS(23f)/ISBSF(143f)/ISBTCSB(54f)/ISBILLSH/ISBINLOC/ISBINLOT/MK* family; prior passes: ISLBLMAP/IS2DBAR/ISSCHED/ISNOTES/ISSRMMS/ISSRINFO/ISSOREVU/ISARINVX/ISSDET/ISORDECO/ISNTYPE/ISUDFINV/ISARTXNB; Pass 137 adds: ISFOHIST(15f FO history+conversion), ISFOLINE(78f FO BOM line 50 op-flags), ISFOORDL(18f order line from FO), ISFXASST(23f fixed asset: cost/dep/3 GL pairs), ISFXATRN(12f fixed asset dep transactions), ISGLCOA/ISGLBDGT/ISGLFCOA(67f identical: years 3-6 GL history extension), ISGLDATE/ISGLHDAT(86f identical: 7-year fiscal calendar), ISGLNBGT(35f: 2 budget sets per GL account), ISFSCLAS/ISFSEMP/ISFSINFO(3f/3f/4f i2 fiber custom), ISFUTYPE(3f follow-up type), ISHLOTS/ISHSERIA(11f identical: serial assembly genealogy PSERIAL→CSERIAL), ISICADT(18f+ BKIC_PROD_* IC audit snapshot); Pass 136 adds: ISDCSER/ISDEFECT/ISDEPT/ISDIV/ISDLCK1-2/ISDRILL/ISDRILLM/ISDROP/ISDUTY/ISEAB/ISECO/ISEDINFO/ISFIELDS/ISFOHEAD/ISFOBMRM; Pass 138 (2026-06-19) adds: ISICADT(64f confirmed), ISICAMTR/ISICMSTR(41f identical IS_PROD_* extension), ISICESA/ISICEST(64f identical snapshots), ISIS(23f config singleton), ISISATAX(13f tax audit), ISITMCFG(9f serial# config), ISITP(3f), ISJBSF(143f business scorecard), ISJOB(9f), ISLANDF(6f landed-cost GL), ISLBLMAP(102f label template), ISLINKS(311f document attachment), ISLOCCST(7f per-location cost), ISLOG(9f activity log), ISLOTS/ISLSMAP(11f/31f tray map), ISLTYPE(4f), ISMACS(11f machine scheduling), ISMCF(49f multi-currency config), ISMCR(22f exchange rates), ISMICADT/ISMICESA/ISMICEST(108f identical multi-company IC snapshots), ISMRPFC(9f MRP forecast), ISNCR(35f NCR), ISNOTES(13f notes; field-13 DDF metadata corruption noted), ISNTYPE(4f), ISNUMBER(52f next-number 50-slot), ISORDDSC/ISPODESC(1f each), ISORDECO(13f order-ECO XR; field-13 DDF corruption), ISPOBOX(22f), ISPOHTRK/ISPOTRK(7f identical shipment tracking), ISPOLOG(9f PO log), ISPOS/ISPOSC(2f each), ISPREQ(25f production requisition), ISPRESN(1f), ISPRINFO(4f), ISPRMSTR(384f payroll employee — largest table in ERP), ISPRSALE(87f sales rep commission), ISPRTEMP(15f payroll GL staging), ISPRUDF(31f UDF deduction/earning def), ISQCAMST(14f QC receiving), ISQCATRN(20f QC detail); Pass 139 (2026-06-19) adds: ISREPDEF(3f)/ISREPLNK(11f)/ISREPORD(17f report support), ISRFQADS(5f BK_DESC_* RFQ addr), ISRMAAI/ISRMAI(54f identical RMA lines arch+current), ISRMAC(3f RMA reason), ISRMADSC/ISRMDESC(5f each BK_DESC_*), ISRMAINF/ISRMHINF/ISRMINFO(54f identical ISSR_INFO_* UDF ext), ISRMAINV/ISRMINV(84f identical BKAR_INV_* invoice clone), ISRMAIVL/ISRMINVL(28f identical BKAR_INVL_* line clone), ISRMTXN/ISRMTXNS(14f identical BKAR_TXN_* txn), ISROUTEX(100f routing extended: 5-cycle arrays with notes×255/emp/WO/date/machine), ISRTESA/ISRTEST(62f identical MTRO_* routing estimate+test clones), ISRTLOAD(21f load manifest), ISRTMS(29f RTM label mapping 10 printers), ISSCHED(24f job scheduler 10 params), ISSCOMP/ISSDET(5f/4f compound+service detail), ISSEDH/ISSESH(84f identical BKAR_INV_* SE doc header), ISSEDL/ISSESL(28f identical BKAR_INVL_* SE lines), ISSEPROC/ISSEQUIP/ISSETYPE(2f each SE access/equip/error-type), ISSERCNT(9f serial counter), ISSERIAL(11f serial BOM tree; IS_SER_EXRA typo confirmed), ISSERR(14f shop error log: ADOF+ADIAG+AREWORK 1KB each), ISSHIPA(5f carrier API creds), ISSHIPCO(16f ship co extended+web URLs), ISSHPVIA(23f customer ship-via acct), ISSIGN(16f digital sig with JPEG path), ISSLSFC(9f BKMRP_FC_* sales forecast), ISSMTCFG(15f SMT reel config), ISSNOTES(9f structured notes); Pass 144 (2026-06-22) adds DDF field-level schemas for ISAP*/ISAR* families + EVOHLPID/HELPURL/INVATXN/INVETXN/IS2DBAR/ISBUILD/ISRMAM/ISSRSOMR. Pass 145 (2026-06-22) adds final 8 IS* tables: ISQCMTHD(44f QC method lib, 3367-byte record, 25 method text lines + 10 note lines), ISQCRSLT/ISQCSPEC(57f identical QC result/spec — ISQC_SPC_* prefix, min/max as STRING/15, test+approval note arrays), ISQRYSQL(2f SQL query store, QUERY STRING/1000), ISQSOA(12f quote/SO analysis line), ISQTCODE(3f IS_CATM_* quote type code), ISQTINFO(54f ISSR_INFO_* UDF clone for quotes), ISREMIND(12f reminder with TIME key + FILE/256 attachment). IS* documentation now COMPLETE — all 659 DDF tables have schema entries in tier2-tables.md. — **C: 90/100**
- [x] ✅ BKSLEVEL (422 fields) — 20-menu × 20-op security matrix; PK=BKSL_MENU+BKSL_LEVEL; MENU{N}_YN = quick access flag; MENU{N}_1..20 = per-op flags — **C: 82/100**
- [x] ✅ BKPRGLFL (664 fields) — payroll GL posting config; PK=STCODE+DEPT; standard taxes (FIT/FICA/FUTA/SUTA/SIT/SDI/WC/Medicare) each with GL acct+dept+rate+limit; 20 user-defined deductions × 13 sub-fields; 20 user-defined earnings; 46 tax-output/vendor slots — **C: 82/100**

### Priority Tier 3 — Remaining 365 misc tables
- [x] ✅ All MT\* tables — Pass 146 (2026-06-22): see entry in Priority Tier 2 above — **C: 82/100**
- [x] ✅ All ED\* (EDI) tables — Pass 147 (2026-06-22): EDI tables are named BKEDI* not ED*; all 6 documented — BKEDIDUN(7f DUNS XRF), BKEDIH(84f BKARINV clone staging), BKEDIL(28f BKARINVL clone staging), BKEDMSTR(3f config), BKEDNOTE(3f notes), BKEDPOST(2f post status); plus CCEDIXRF(6f CC ship-to routing) + ISEDINFO(54f ISSR_INFO_* UDF clone) — **C: 82/100**
- [x] ✅ All PI\* (Physical Inventory) tables — Pass 147 (2026-06-22): 2 DDF PI* tables — PIBINLOC(14f item+loc+bin PK, UOH+count dates+YEAR/QTR cycle, LOT/SER), PIBINLOT(14f period+item+loc+lot+bin+ser PK, SQTY vs UOH count comparison, PSTD posted flag) — **C: 85/100**
- [x] ✅ All ES\* (Estimating) tables — Pass 136 (2026-06-19): ISESTASM(213f: quote master MTESUM_* prefix, 10-qty-break cost summary), ISESADTL/ISESTDTL(203f identical: IS_EST_* per-component cost breakdown, 10-qty-break MAT/LAB/SETUP/OP/OH/MISC/PRICE), ISESAHDR/ISESTHDR/ISESTAQT(84f identical BKAR_INV_* schema), ISESALNE/ISESTLNE/ISESTAQL(28f identical BKAR_INVL_* schema), ISESTPO(16f BKMRP_PO_* bridge to MRP PO); all in tier2-tables.md — **C: 82/100**
- [x] ✅ All remaining tables not covered above — Pass 149 (2026-06-22): AHSYLOG(23f), ARTTEMP(12f), BKABCUST(5f), BKABVEND(2f), BKACTRPT(53f), BKFLDHLP(3f), BKFOCFG(18f), BKISHTAX+BKISTAX(13f×2), BKMATRIM(3f); plus DDF reinforcement of BKGLACHK/BKGLCHK/BKGLAGJL/BKGLAGJR/BKGLATRN/BKGLCCOA/BKGLCOA/BKLOGON/BKMATCST/BKMRPFC/BKMRPPO/BKMRPSW/BKESTQT/BKESTQTL. Pass 151 (2026-06-22): BKPSUSER(11f alt-session user), BKQCMSTR(14f QC inspection), BKQCTRAN(21f QC detail), BKQTNOTE+BKQTTEMP+BKRFQDES(5f each BK_DESC note lines), BKRFQ(49f RFQ header 10-break cost matrix), BKRTCST(24f routing cost for quoting), BKRTEMTR(62f E-routing mirror), BKRTSPEC(7f routing spec notes), BKRTTEMP(6f routing template notes), BKPCKIT(6f PC kit — offset-15 anomaly), BKPCPLOT(10f PC production plot — offset-15 anomaly), BKSAREPT(57f SA report filter 26-dim), BKSBMFG(6f)+BKSBPART(5f)+BKSBVEND(6f approved sources), BKSHORT(9f shortage log), BKSLEVEL(422f security level×menu access matrix), BKSLMSTR(2f level lookup), BKSOHLOT(14f)+BKSOHSER(14f SO lot/serial), BKSOLOCK(5f SO lock), BKSONOTE(5f SO notes), BKSOPO(16f)+BKWOPO(16f MRP suggested PO), BKSOX(25f)+BKSOXH(25f SOX archive), BKSYAP(11f)+BKSYAR(2f system links), BKSYCFG(4f)+BKSYHELP(1f)+BKSYPRTR(11f)+BKSYUSER(5f system config), BKSYLOG(215f per-user module access), BKSYMSTR(286f global system singleton), BKYSMSTR(355f WO/mfg system singleton), BKUMSRTY(23f UM security), BKUPDATE(4f version tracking); non-BK: BOMCHG(15f BOM audit), BUCKETS(14f capacity scheduling), CALENDAR(5f shop calendar), CALTEMP(2f), CCEDIXRF(6f EDI xref), CLASMSTR(2f)+CUSTCLAS(2f class lookups), CLASS(24f GL accounts per class), DBACNAME(3f multi-company name), DBAFIFO(5f FIFO layers), DBAHLPID(2f help map), DISCOUNT(85f pricing/commission matrix), DPTMENT(2f GL dept). **Pass 152 (2026-06-22) — DDF schema FULLY EXHAUSTED:** EMERSNGL(65f GL single-company COA+2 YE floats), INVATXN/INVATXN/INVETXN(24f×3 MTIT_* txn log — 3 company mirrors), IS2DBAR(109f 2D barcode 100×DOCPR), LANGDICT(5f translation dictionary), LOT(25f MTLOT_* lot master), MACHINE(20f TMACH_* machine with inactivation audit), MENUFILE(108f MENU_* TAS Pro menu definition: 20 items×LINES/OPTIONS/TYPES/NAMES/PROG), MK* marketing module 11 tables (MKAHIST/MKASSIGN/MKDEF/MKECLASS/MKEVENT/MKFORM/MKICLASS/MKTCLASS/MKTNOTE/MKTRACK/MKTROUT), MTEXCHG(7f exchange rate), MTICMSTR/MTICAMTR/MTICEMTR/MTINVDEF(108f×4 identical item master), MTMRP(13f MRP work), MWOPTEMP(8f), NOTETEMP(5f), NZITPRE(54f item# prefix), OPQCDESC(10f per-op QC), OUTPROC/OUTHPROC(15f×2 outside processing), PIBINLOC/PIBINLOT(14f×2 PI bin), QCCODES(2f), ROCHG(22f routing change audit), ROUTING/ROUTAING/ROUTTEMP(62f×3 identical MTRO_* routing op), SCHEDCAL(6f shop calendar), SCHWO(10f scheduled WO), SCRAP(21f scrap codes), SERIAL/SERIALH(30f×2 serial lifecycle), SUMCUST/SUMINV/SUMPNCUS/SUMWC(5f/19f/6f/7f summary stats), TEMPOLD(4f), TESTARRA/TESTFILE(dev artifacts noted only), TOOL(57f MTOOL_* mold/tool master), WBTRVMEM/WBTRVMEMO(5f×2 Btrieve memory buffers), WCCTL(5f)/WCTRLOAD/WCTRSLOD(8f×2 WC load), WOBOM/WOHBOM(24f×2), WOBOMCHG(17f), WOBOMHRM/WOBOMREM(7f×2), WODATE/WOHDATE(13f×2), WOELABOR/WOHLABOR/WOLABOR/WOLABRPT(58f×4 identical MTWOLA_* labor), WOEMAT/WOHMAT/WOMAT(17f×3 material issue), WOERECV/WOHRECV/WORECV(11f×3 WO receipt), WOEXCHG/WOHEXCHG(10f×2 WO extra charges), WORKACHG/WORKCHG(25f×2 WO change audit), WORKCTR(47f MTWC_* WC master with 10×CYCLE_TIME), WORKHORD/WORKORD/WORKSORD(74f×3 identical MTWO_WIP_* WO master), WOROCHG(24f WO routing change audit), WOHROUT/WOROUT/WOROUTMP/WOSROUT(81f×4 identical MTWORO_* WO routing op), XXICMSTR(64f BKIC_PROD_* cross-company IC summary), X$* Pervasive DDF catalog system tables (10 tables — Attrib/Field/File/Index/Occurs/Proc/Relate/Trigger/Variant/View). **All 659 DDF tables now have schema entries in tier2-tables.md.** — **C: 93/100** (every table from schema.md field-documented; remaining gap is functional/logic interpretation for tables not touched by SRC analysis)

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
| Module: AP | **97** | 96 | **0** ✅ Pass168 BKAP.INVL.* 20 access vars (BKAPINVL invoice line) + ISAP.PROJ.* 12 vars cross-module (AP+AR); ISAPPROJ confirmed shared AP/AR project-billing table | 2026-06-22 |
| Module: IN/Inventory | **95** | 85 | **0** ✅ ↑+2 Pass91 T6-IN-B 10-tab: IS.ECO/BKSB.MFG/BKSB.VEND/SPECS[12]/RCOST[14] confirmed | 2026-06-18 |
| Module: SO | **96** | 85 | **0** ✅ ↑+2 Pass95 FRGHT/SUBTOT/TOTAL/sobookdate/ASD/rts/recurring-SO/SOAXCOM/ISSR.INFO header+line confirmed | 2026-06-18 |
| Module: PO | **93** | 85 | **0** ✅ ↑+3 Pass89 ISAP.CHG POS-module vendor-master T7POQ delivery | 2026-06-18 |
| Module: WO | **97** | 90 | **0** ✅ Pass168 T7WOA(413p) MTWO.WIP.* 82 vars + MTWORO.* 63 vars = 145 WO access vars confirmed; WORKORD C:90→93 | 2026-06-22 |
| Module: GL | **95** | 92 | **0** ✅ ↑+2 Pass90 14-period confirmed BKGL.STC/STI fin-stmt config | 2026-06-18 |
| Module: BM/MRP | **90** | 88 | **0** ✅ ↑+2 Pass85 MTIC.PROD MRP fields confirmed | 2026-06-18 |
| Module: RO/Routing | **88** | 88 | **0** ✅ ↑+3 Pass72 | 2026-06-17 |
| Module: DC/Data Collection | **89** | 85 | **0** ✅ ↑+2 Pass86 EvoDCmenu/ht6 confirmed | 2026-06-18 |
| Module: PR/Payroll | **92** | 92 | **0** ✅ ↑+2 Pass84 W-4/CURP/PRLA DFMs | 2026-06-18 |
| Module: AM (Accounting Maint.) | **93** | 85 | **0** ✅ ↑+10 Pass90 14-period GL BKGL.STC/STI fin-stmt archive | 2026-06-18 |
| Module: CM/CRM | **90** | 85 | **0** ✅ ↑+4 Pass95 BKCM.LEAD/TERR/ACFC/DTCD/CATM 5 code tables fully confirmed | 2026-06-18 |
| Module: MK/Marketing Automation | **85** | 78 | **0** ✅ ↑+7 Pass134 all 11 MK* tables (MKAHIST/ASSIGN/DEF/ECLASS/ICLASS/TCLASS/EVENT/FORM/TRACK/TNOTE/TROUT) field-documented; campaign flow confirmed; + ISIS(23f feature flags)+ISBANKS(23f)+ISBSF(143f KPI) | 2026-06-19 |
| Module: DE/EDI/Imports | **86** | 80 | **0** ✅ ↑+8 Pass86 T7DE* full suite IS.DEF/ISAP.QPO confirmed | 2026-06-18 |
| Module: CS/Commission+Salesperson | **87** | 85 | **0** ✅ ↑+2 Pass165 T7CSO 3-date-range filters (close/delivery/txn) + 3-tier color-class + OT.COMM/ARC.COMM totals; C:80→84 | 2026-06-22 |
| Module: JC/Job Costing | **87** | 82 | **0** ✅ ↑+9 Pass85 JCA-JCS+JCENG full menu | 2026-06-18 |
| Module: SC/Serial Control ⚠️ | **80** | 80 | **0** ✅ | 2026-06-17 |
| Module: QC/Quality Control | **92** | 90 | **0** ✅ ↑+2 Pass166 T7POJC: BKQCMSTR 20 field-access names confirmed (VKEY/DKEY/PKEY/RKEY/IKEY + qty breakdown); BKQCTRAN 26 field names; AC.MST.* CAPA vars; C:78→84 | 2026-06-22 |
| Module: QT/Service Quote | **82** | 75 | **0** ✅ ↑+8 Pass93 ISSR.INFO.DATE[5]+AL[20] confirmed | 2026-06-18 |
| Module: IC/Inventory Utility | **83** | 80 | **0** ✅ ↑+3 Pass166 J7TMCKanban: BKIC.PROD.* 65f + BKIC.LOC.* 22f + BKIC.LOCM.* 13f access vars; Kanban replenishment → RFQ flow confirmed; C:68→79 | 2026-06-22 |
| Module: WC/Warehouse Control ⚠️ | **90** | 80 | **0** ✅ ↑+4 Pass164 BKIC.LOCM.* 14-field schema(CODE/NAME/ADDR1-3/CITY/STATE/ZIP/TAX#/CNTCT/PHONE/FAX/TAXGR/CITY2); ISBINLOC 9f; all 11 programs mapped; WCBK capacity vars | 2026-06-22 |
| Module: SH/Shop Scheduling ⚠️ | **88** | 88 | **0** ✅ ↑+5 Pass84 SHA-SHP full menu DFMs | 2026-06-18 |
| Module: LC/Lot Control | **88** | 78 | **0** ✅ ↑+7 Pass85 MTLOT.* LC-A/G DFMs | 2026-06-18 |
| Module: SR/Service Repair | **88** | 82 | **0** ✅ ↑+6 Pass90 SRB/D/E/F/G/I/S full invoice+release | 2026-06-18 |
| Module: FA/Fixed Assets | **86** | 86 | **0** ✅ ↑+4 Pass84 IS.FXA/FXT full field layout | 2026-06-18 |
| Module: PI/Physical Inventory | **88** | 80 | **0** ✅ ↑+12 Pass85 BKPH.* PI-A/H confirmed | 2026-06-18 |
| Module: MA/AR Deposits | **82** | 75 | **0** ✅ ↑+6 Pass92 ISAR.DEPL.SO/AMT/GLACT BKAR.DEP.DEPNO/CUST confirmed | 2026-06-18 |
| Module: ES/Estimating | **88** | 88 | **0** ✅ ↑+3 Pass84 IS.EST 10-qty+convert DFMs | 2026-06-18 |
| Module: SA/Sales Analysis | **88** | 84 | **0** ✅ ↑+4 Pass167 J7AISAN: BKSA.* 57-var full BKSAREPT access namespace (TYPE/NAME/RTM/TITLE/BASE + FROM1-26/THRU1-26); WO actual-cost dimension (WOLABOR/WOMAT/OUTPROC); C:77→84 | 2026-06-22 |
| Module: AC/Activity Control | **83** | 78 | **0** ✅ ↑+5 Pass92 WODATE/AC.RD/IS.ACTION all fields confirmed | 2026-06-18 |
| Module: CC/Credit Card ⚠️ | **87** | 85 | **0** ✅ ↑+3 Pass92 IS.CC.* all 8 fields + CCYY/CCMM/CVV confirmed | 2026-06-18 |
| Module: SP/SPC ⚠️ | **92** | 92 | **0** ✅ ↑+5 Pass84 SPCLIVEGRID/LIVEREP/REP2/REPPPM | 2026-06-18 |
| Module: HH/Handheld | **93** | 85 | **0** ✅ ↑+13 Pass87 43 DFMs WO/SO/PO/PI/INV full handheld system | 2026-06-18 |
| Module: UT/Utilities | **84** | 75 | **0** ✅ ↑+7 Pass164 UTKE GL arrays AGLA/AGLC/AGLS/AGLSNT/AGLW (5 GL types per location); UTKA 7 clear targets+DONE flags; UTKD 6 prior FY+SUSP.GLACCT; UTKF OLD/NEW.TOTVL cost revalue; C:72→82 | 2026-06-22 |
| Module: RM/RMA | **85** | 82 | **0** ✅ ↑+7 Pass86 SRMA/IS.RMA RMD disposition confirmed | 2026-06-18 |
| Module: FO/Features Options | **87** | 83 | **0** ✅ ↑+4 Pass86 ISFO.HDR.* EvoFNO confirmed | 2026-06-18 |
| Module: IS/InfoSystem | **80** | 72 | **0** ✅ ↑+5 Pass153 T7ISMCC.DFM fully read; MCC=Convert Source→Base Currency (AP/AR/PORNI/Bank); is.cvt.mth+is.date+ISGL.CYDATE[1-12] confirmed; F/E gain-loss posting confirmed | 2026-06-22 |
| Module: IM/Landed Cost | **88** | 82 | **0** ✅ ↑+10 Pass86 ISIS.MCF/MCR multi-currency + landed confirmed | 2026-06-18 |
| Module: PS/Program Security | **88** | 88 | **0** ✅ ↑+6 Pass83 ISEXUSER+max.chk.amt | 2026-06-18 |
| Module: QU/Query Tools | **88** | 82 | **0** ✅ ↑+6 Pass165 WBKLOOKUP FILEDICT API fully mapped: FD_FIELDNAME/KD_FIELDNAME/FD_TYPE/FD_SIZE/FD_EDIT/FD_COLHEADER/FD_TOT/FD_FUNC; LU_RESULT/LU_EDIT_SCRN/LUGRID_HNDL; NOTES.H/LINKS.H/DRILL.H/DRILLM.H handles; C:82→88 | 2026-06-22 |
| Module: SU/Setup UI | **80** | 78 | **0** ✅ ↑+2 Pass119 11 YN flags confirmed from source (YN[20/36/37/38/48/59/66/228/229/290]+YN[1]); YN[228] doc corrected | 2026-06-19 |
| Module: TA/TAS Admin | **91** | 80 | **0** ✅ ↑+3 Pass91 WTASDATAM/DMGR/INIT DFMs: FLD/KEY/FILE descriptors confirmed | 2026-06-18 |
| Module: DI/Digital Signatures | **90** | 80 | **0** ✅ ↑+12 Pass87 T7DIGSIG PO approval 5-level emp.signoff | 2026-06-18 |
| Module: AD/Accounting Defaults | **85** | 82 | **0** ✅ ↑+3 Pass165 T7MDefNDC 73 unique BKSY.* = full BKSYMSTR namespace: all GL accts + AR/AP/PO/PR defaults + auto-numbers + terms + company info; IS.* module flag set; C:75→83 | 2026-06-22 |
| Module: CR/SO Approvals | **80** | 78 | **0** ✅ ↑+2 Pass164 SFROM/STHRU.SONUM+ORDDTE filters; HOLD.AMT; PRMSTR.H; full password rotation workflow vars; CT.DEPT/ADMIN/LEVEL/EMPNAME confirmed | 2026-06-22 |
| Module: US/Triggers | **85** | 75 | **0** ✅ ↑+11 Pass93 IS.TRIG.* all 23 fields confirmed | 2026-06-18 |
| Subsystem: BO/Bill of Lading | **80** | 80 | **0** ✅ ↑+6 Pass163 NMFC/freight CLASS/hazmat(HTYPE/HM/HQTY); 5 carrier#s; 4 logistics timestamps; pallet entry; COMMODITY; LISTG60.LIB | 2026-06-22 |
| Subsystem: DS/Data Sync stubs | **65** | 65 | **0** ✅ ↑+3 Pass109 all 36 fingerprint tables field-decoded; ISLOG kill-flag mechanism; DBAFIFO=FIFO cost layers; HH/IM codes confirmed | 2026-06-18 |
| Subsystem: AU/Automation | **78** | 78 | **0** ✅ ↑+6 Pass82 DFM confirmed | 2026-06-18 |
| Subsystem: FS/Field Information Base | **78** | 78 | **0** ✅ ↑+6 Pass82 3 DFMs FIB prefix | 2026-06-18 |
| Subsystem: GF/AR Charges | **82** | 80 | **0** ✅ ↑+5 Pass164 BKAR.* 13 BKARCUST fields from T7GFPRICE(CUSTCODE/NAME/ADD1-2/CITY/STATE/ZIP/CONTACT/TELEPHONE/COUNTRY/CREDITLMT/CHG.INTRST/REMAINCRD); T7GFV SO/JOB charge context | 2026-06-22 |
| Subsystem: RE/Reminders+Rebuild | **83** | 78 | **0** ✅ ↑+8 Pass86 IS.REM.* Google Calendar export | 2026-06-18 |
| Subsystem: SE+ST/Service Code Tables | **77** | 74 | **0** ✅ ↑+3 Pass160 all 6 programs src=EVO.LIB; t7sttype=lowercase alias of T7STYPE; T7STOCK=CRM account category editor; program roles fully mapped | 2026-06-22 |
| Subsystem: PU/Put-Away | **78** | 76 | **0** ✅ ↑+2 Pass160 LISTG60.LIB confirmed; SCAN.ITEM/ENTERBIN/ACTION/PABBL/MTIC.PROD.CUBFT/ABC/STDPK vars; BKIC.IS.DCODE | 2026-06-22 |
| Subsystem: MU/Multi-Yield WO | **79** | 78 | **0** ✅ ↑+1 Pass160 E.*/M.* output/input var pattern; PROPORTION yield split; SCAN.WONUM; LISTG60.LIB framework | 2026-06-22 |
| Subsystem: LI/License Access | **77** | 72 | **0** ✅ ↑+5 Pass160 T7LIMACC scans DFM files; DFM_OBJNAME/CAPTION/TEXT/HINT; LAGROUP/LGNUM; workflow: DFM→components→ISACCESS match | 2026-06-22 |
| Subsystem: EDII/EDI Invoice Import | **76** | 76 | **0** ✅ ↑+4 Pass162 IMP.FILENAME; date format parser(DATE.POS1/2); parallel import arrays(ITEM/QTY/ESD/CUSORD.LIST); INCL.ROHS; src=LISTG60.LIB(ETBCOMBOVAL) | 2026-06-22 |
| Subsystem: LG/LGS Custom | **76** | 70 | **0** ✅ ↑+6 Pass162 src=LISTG60.LIB(ETBCOMBOVAL), 42t(CORRECTED from 10), ISTAXGRP+BKICTAX both used, RETEN.PER/BKAR.INV.RETEN/ISTS.EDATE customs retention; T7LGSSOEVerify adds SBVEND/SBMFG origin compliance | 2026-06-22 |
| Subsystem: JS/Reporting Bridges | **80** | 78 | **0** ✅ ↑+2 Pass159 T7JAVASET distinct from T7JSETTINGS; T7JAVARUN confirmed | 2026-06-22 |
| Subsystem: BS/Business Score | **88** | 84 | **0** ✅ ↑+4 Pass166 T7BS 45 ISBSF.* access vars: AP.ATP/AR.DEPO/IC.VALUE/PO.PORNI new; cash=9 bank accounts (not 100-period, prior note corrected); WOS 9-component cost breakdown confirmed; C:84→88 | 2026-06-22 |
| Subsystem: AD/Advanced DC | **78** | 72 | **0** ✅ ↑+6 Pass161 BKDCLAB full schema: LAB.JCNUM(JC integration!), LAB.ADT.SUPER/IN/OUT(timeclock), LAB.ESSDATE, LAB.CYCLE.HR/MIN/SEC(SPC), LAB.REGOVER, LAB.APPROVAL, LAB.SCRAPCD/SCRAPQTY | 2026-06-22 |
| Subsystem: IT/Item Serial Config | **78** | 78 | **0** ✅ ↑+6 Pass163 IS.SERC.ITEM/CLASS/SPOS/LENG/TOTAL/NUMBER/LAST/EXTRA/L2 all 9 fields from vars; SER.FORMAT template; SSIZE/SPOS/ANUM format params; 64t(CORRECTED from 7); src=LISTG60.LIB | 2026-06-22 |
| Module: SD/Standard Detail | **78** | 74 | **0** ✅ ↑+4 Pass160 T7SDET (58p, 32t, EVO.LIB); REPLNK_REC_HOLD purpose confirmed; ISSDET→ISSTYPE relationship confirmed; ISDRILL in set | 2026-06-22 |
| Module: SL/Shop Loading | **85** | 70 | **0** ✅ ↑+20 Pass93 T7SHA-SHP MTWC.*/MTWORO.*/SWO.CRATIO/RUN.DAYS fully confirmed | 2026-06-18 |
| Module: AL/Audit Log+AltPart | **79** | 76 | **0** ✅ ↑+3 Pass158 SAVE.BOTH.WAYS bidirectional sub; UPSK/EUSER/PASS.OK gate; FILELOC→BKSYMSTR audit group write confirmed | 2026-06-22 |
| Module: ML/Multi-Language | **82** | 76 | **0** ✅ ↑+6 Pass162 LANG.DICT.FONT(5th field); EVO.CFG.LANG; PRE.LANGCAPT; 40t(CORRECTED from 27); DFMNAME scanner + AddLang/Edit/Delete workflow from Pass153 | 2026-06-22 |
| Module: MH/Shipping Order | **80** | 72 | **0** ✅ ↑+8 Pass162 ISTECH2.LIB=SO/shipping framework(superset of LISTG60); FROM.CUST/ORDDTE/TERRITORY filters; REL.ALL/AUTO.BO/AUTO.RCOMM flags; TOT_UOH/UBO/ORD totals; Pass94 T7BOL+BOLMSO BOL structure | 2026-06-22 |
| Module: BR/Brands | **76** | 72 | **0** ✅ ↑+4 Pass158 DB corrected to 40t; ISPOSI.H=POS handle; T7BROWSER 55t session overhead; IS.* feature flag vars from BKYSMSTR | 2026-06-22 |
| Module: NE/New Company Init | **78** | 68 | **0** ✅ ↑+10 Pass153 T7NEWINIT.DFM fully read; purpose confirmed ("check/create missing data files"); Go+Exit+fileslabel confirmed | 2026-06-22 |
| Module: JO/Jobs+Departments | **79** | 76 | **0** ✅ ↑+3 Pass158 T7JODPSALES Java-backed (EvoPVT jdbc.ini); ISUDFINV new table; JCUST/JVEND/JDEPT/JITEM entity handle vars | 2026-06-22 |
| Module: FN/File Navigator | **80** | 72 | **0** ✅ ↑+8 Pass164 DFIND/NFIND/AFIND_FIELD1..6 typed search arrays; DREPL/NREPL/AREPL replace targets; FILENAME/ELEMENT navigation; OPER+POS/SPOS/SLENGTH substring; 3-type search(date/numeric/alpha); C:72→80 | 2026-06-22 |
| Module: XC/CC Cross-Ref | **78** | 74 | **0** ✅ ↑+4 Pass158 BKCMACCT 35-field var set confirmed (cross-validates DDF); TOLKEN credit card vault; RVALF token lookup result | 2026-06-22 |
| Module: IT/Item Config | **78** | 78 | **0** ✅ ↑+6 Pass82 IS.SERC DFM | 2026-06-18 |
| Module: EM/Emergency GL | **78** | 72 | **0** ✅ ↑+6 Pass153 T7EMGL.DFM fully read; BKGL.ACCT/GLDPT/EXTRA field bindings confirmed; EXTRA=GL Account Link; Add/Delete/Save toolbar confirmed | 2026-06-22 |
| Module: RT/RTM Validator | **82** | 55 | **0** ✅ ↑+12 Pass164 CORRECTED: T7RTMVALID=Runtime License Validator(NOT RTM template validator); SERIAL/PRODUCT/APROD license vars; ISIS.TAX+MULTI.CURR+IMAGING+RMA+EZPAY etc module gates; IS.DEMO flag; NZLICE.LIB | 2026-06-22 |
| Module: FP/FO Print | **55** | 55 | **0** ✅ ↑+0 Pass154: T7FOD/T7FOE confirmed as FP-B filter DFMs; zero T7FP* RWNs confirmed; RTM-only; BKBM.PROD.OPYN[4]="Use STD Customer Pricing?", OPYN[5]="Add Price to Parent?" exact semantics confirmed from T7FOC DFM | 2026-06-22 |
| Module: RF/RFQ | **84** | 78 | **0** ✅ ↑+9 Pass93 BKRFQ.EXP/ISSUE/QTY/COST/PROD/LCDATE confirmed | 2026-06-18 |
| Platform Subsystems | **85** | 82 | **0** ✅ ↑+3 Pass165 EvoLinks.RWN 16-db fingerprint + IS.LNK.* 16 ISLINKS fields all confirmed; WFA/OFA/XOAPP/OTHERAPP app launchers; ALERTS/LINKS.ALERT/LINKS.ITM.ALERT alert vars; GLOBALPATH; EvoLinks C:72→82 | 2026-06-22 |
| Subsystem: PI/Physical Inventory | **88** | 80 | **0** ✅ (dup — see primary) | 2026-06-18 |
| Module: SA/Sales Analysis | **84** | 84 | **0** ✅ (dup row — see primary entry) | 2026-06-18 |
| Module: JC/Job Cost | **87** | 82 | **0** ✅ (dup — see primary) | 2026-06-18 |
| Module: ES/Estimating | **88** | 88 | **0** ✅ (dup row — see primary entry) | 2026-06-18 |
| Platform: WBKLOOKUP/Lookup Framework | **88** | 76 | **0** ✅ ↑+12 Pass165 FILEDICT API fully mapped: FD_*/KD_* field+key attrs (col headers, type, size, edit mask, sort fn); LU_RESULT/LU_EDIT_SCRN; NOTES.H/LINKS.H/DRILL.H/DRILLM.H; dynamic any-table schema reader confirmed | 2026-06-22 |
| Module: DE/DC stubs+EDI processing | **86** | 75 | **0** ✅ (dup of DE/EDI -- see primary) | 2026-06-18 |
| Module: SM/System Maintenance+Item Inquiry | **94** | 86 | **0** ✅ ↑+3 Pass95 SM-I BKCM.LEAD/TERR/ACFC/DTCD/CATM + SM-J SMJA-SMJH 8 archive-purge programs | 2026-06-18 |
| Module: MR/MRP Engine | **90** | 85 | **0** ✅ ↑+10 Pass90 BKMRP.FC/PO MTMRP 4-stage-run MBEDORC WO/PO gen | 2026-06-18 |
| Tables: BKMR*/MRP Support | **78** | 78 | **0** ✅ ↑+6 Pass106e: BKMRPFC/BKMRPPO/BKMRPSW/MTMRP full field tables+semantics; 14-op pipeline; MTMRP action codes; BKMRPPO→BKAPPO flow | 2026-06-18 |
| Tables: BKED*/EDI | **78** | 72 | **0** ✅ ↑+13 Pass106 full family documented: BKEDIH/IL=BKARINV clones; BKEDIDUN/MSTR/NOTE/POST semantics; DEP-B/C/D/E/F/H pipeline | 2026-06-18 |
| Tables: BKES*/Estimating | **78** | 72 | **0** ✅ ↑+13 Pass106 full family documented: BKESTQT/QTL=BKARINV clones; BKESTCFG 13f; ESTSUM 213f 10-qty-break cost summary; ES-A..M pipeline | 2026-06-18 |
| Module: YS/YN Flags Editor | **80** | 75 | **0** ✅ ↑+5 Pass164 BKYS.WONUM/YN/GLNUM/GLDPT/NUM/DESC/VNUM/DATE/QCNUM/REQNUM/INVNUM/RBNUM (12 typed BKYSMSTR fields); 14 DB tables(BKARCUST/BKAPVEND/BKCMACCN/BKICMSTR entity lookups); LANGDICT multi-lang; CFG.START/CFG.BUFFER params editor | 2026-06-22 |
| Module: CU/WO Cut Sheet | **82** | 75 | **0** ✅ ↑+7 Pass164 WOMAT.*(17f)+MTLOT.*(22f)+MTWO.WIP.*(14f) all cross-validated from vars; EJOB/EPART/EUSER/EPASS auth gate; WOTOTQTY/ABIQTY/LEFTQTY/GT.MAT/GT.ISS/FABQTY qty summaries | 2026-06-22 |
| Subsystem: ADCA/Advanced DC | **78** | 72 | **0** ✅ ↑+6 Pass161 (same entry as AD/Advanced DC above) | 2026-06-22 |
| Module: TC/Treasury Control | **76** | 75 | **0** ✅ CORRECTED from 80 (prior was over-estimated) Pass162 LISTG60.LIB(ETBCOMBOVAL) confirmed; CHECK_AMT/INV_APPLIED/DINV_*/TOT_CREDITS/TOT_DISC/ARC_TTLA/INVC.NETCHG; AR cash receipts workflow vars fully confirmed | 2026-06-22 |
| Module: SC/Serial Control ⚠️ (dup) | **80** | 80 | **0** ✅ ↑+2 Pass109 MTSER all 30 fields decoded; lifecycle PO→WO→SO traced; ISSERIAL genealogy documented | 2026-06-18 |
| Module: CH/Multi-Location Chain | **82** | 72 | **0** ✅ ↑+10 Pass153 T7CHAIN+T7CHAINM DFMs fully read; IS.CHAIN fields+AUTO Y/N/A+PARAM[1-5]+19 parent+30 child programs confirmed | 2026-06-22 |
| Module: KI/Kit Assembly | **83** | 72 | **0** ✅ ↑+4 Pass163 MTIC.PROD.* 40 MTICMSTR fields confirmed; MTIC.PROD.UIWIP/AVAIL/MRPSW/CUSNM; BKIC.IS.DCODE; Pass94 BOM-component arrays | 2026-06-22 |
| Module: MA/AR Deposit Apply | **82** | 75 | **0** ✅ (merged with MA/AR Deposits — see primary) | 2026-06-18 |
| Module: TE/NACHA+ACH | **78** | 75 | **0** ✅ ↑+3 Pass160 BATCH.CNTR; CHK.D1/D2/M1/M2/Y1/Y2 NACHA date parsing; LISTG60.LIB; WHICH selector; FROM/THRU VEND filter | 2026-06-22 |
| Module: PA/Paperless DC | **78** | 72 | **0** ✅ ↑+6 Pass160 SCAN.WO+OPER dual scan; MTWO.WIP.LOCK; ASTART/AFIN timestamps; ESETUP/EMAT/EOUTPR/ELABOR vs ASETUP cost; COMQTY; LISTG60.LIB | 2026-06-22 |
| Module: TPOA/PO Processing Hub | **84** | 75 | **0** ✅ ↑+9 Pass162 TPOA.RWN(499p, LISTG60.LIB): DIGSIG.H/USING.DIGSIG/APCHG.H sig+audit; SEC.LEVEL; SCAN.WO+QTY barcode; BKAP.CUST.CODE vendor↔customer link; SCREEN.LOCKED; Pass93 T7POA* BKAP.PO header+RITEC | 2026-06-22 |
| Module: QS/Quick SO | **87** | 81 | **0** ✅ ↑+6 Pass166 J7SyncWOtoSO: BKAR.INV.* 86 fields (adds bill-to block BILA1-3/BILCTY/BILNME etc.); BKAR.INVL.* 28f = full line schema; C:81→87 | 2026-06-22 |
| Subsystem: VSCHED/Visual Scheduler | **79** | 78 | **0** ✅ ↑+1 Pass162 Java-backed(HOST/PORT/NAME/WorkCenterLoad.jar); ADD.WONUM vars(WO entry from scheduler); ESTHDR/ESTLNE handles(estimate load overlay!); FILEDICT API(export); C:75→79 | 2026-06-22 |
| System: AUTO/Batch Automation | **82** | 78 | **0** ✅ ↑+4 Pass164 T7AUTOFX ISIS.MCF.* schema(CODE/BASE/GLABK/GLDBK/GLABS/GLDBS)+Java HOST/PORT; t7automrf MTMRP.ACTION/PG.SDATE/PG.FDATE/PG.QTY; AUTOREBSS BKIC.PROD.TXBLE/RLVL/RAMT/LSALE/LORD/LRCPT | 2026-06-22 |
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
| Per-Table Narrative Docs | **93** | 88 | **+5** ✅ ↑+5 Pass152 (2026-06-22): DDF schema FULLY exhausted — all 659 tables now have schema entries in tier2-tables.md (8285 lines). Pass152 adds final ~80 tables: EMERSNGL/INVTXN-family/IS2DBAR/LANGDICT/LOT/MACHINE/MENUFILE/MK-11-tables/MTEXCHG/MTICMSTR-family×4/MTMRP/MWOPTEMP/NOTETEMP/NZITPRE/OPQCDESC/OUTPROC×2/PIBINLOC×2/QCCODES/ROCHG/ROUTING×3/SCHEDCAL/SCHWO/SCRAP/SERIAL×2/SUM×4/TEMPOLD/TOOL/WBTRVMEM×2/WCCTL/WCTRLOAD×2/WOBOM×2/WOBOMCHG/WOBOMHRM×2/WODATE×2/WOLABOR×4/WOMAT×3/WORECV×3/WOEXCHG×2/WORKCHG×2/WORKCTR/WORKORD×3/WOROCHG/WOROUT×4/XXICMSTR/X$-system×10. Prior: INVTXN(24f) narrative + WOLABOR(58f) narrative (Pass108) | 2026-06-22 |
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
