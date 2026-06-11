# PROJECT-STRUCTURE.md
# EvoERP — Complete File & Path Structure

**Purpose:** Every known file in the EvoERP system, its format, owner module, purpose, and
relationships to other files. Updated each ANALYZE session.

**Status legend:** `confirmed` | `inferred` | `unknown`

---

## QUICK STATS

| File Type | Count | Readable | Notes |
|-----------|-------|----------|-------|
| `.RUN` | 1,265 | Partial (strings only) | TAS Pro 6 compiled programs |
| `.RWN` | 1,115+ | No (encrypted) | TAS Pro 7 compiled programs |
| `.DFM` | 1,120+ | Yes (plaintext) | Delphi VCL form layouts |
| `.RTM` | 899+ | Partial (TPF0 binary) | Nevrona ReportBuilder templates |
| `.SRC` | 7 | Yes (plaintext) | TAS Pro 4GL source (partial deploy) |
| `.DCY` | 41 | No (encrypted) | TAS data dictionaries / schemas |
| `.B` | 649 | No (Btrieve binary) | Database table files |
| `.TXT` | 4,088 | Yes (ASCII) | Report output / data exports |
| `.pdf` | ~700 | Yes | Generated report PDFs |
| `.XLS` | 195 | Yes | Excel exports |
| `.csv` | 11 | Yes | Import/export delimited data |

---

## TOP-LEVEL DIRECTORY LAYOUT

### Client Install — `C:\ISTS\` (READ-ONLY)

```
C:\ISTS\
├── StartEvo.exe          [37 KB] Launcher — checks runtime, reads taspro7.ini, spawns tp7runtime.exe
├── tp7runtime.exe        [33.3 MB] TAS Professional 7 engine (the interpreter)
├── taspro7.ini           Config: DataDictPath, DfltRunPrg, MultiUser, DefaultPath, Titlebar, HelpFileName
├── EvoSettings.INI       Per-workstation module access flags
├── WHOAMI.DBA            [35 bytes] Workstation seat identity token (format: unknown)
├── CHMHELP.EVO           [35 bytes] CHM presence marker (format: unknown)
├── RBuilder.ini          Nevrona ReportBuilder preferences
├── EvoHELP.CHM           Windows HTML Help — 779 topics
├── EvoPVT.jar            [1.8 MB] JavaFX SQL helper app
├── qtintf70.dll          Qt 3/CLX UI layer (used by tp7runtime.exe)
├── c4dll.dll             CodeBase data engine DLL
├── zipdll.dll            ZIP compression (used by EvoBackup)
├── unzdll.dll            ZIP decompression
├── RBDsgnr.exe           [6.2 MB] Nevrona ReportBuilder stand-alone designer
├── DFM\                  Form cache directory (runtime-written)
└── PDFS\                 PDF output directory (runtime-written)
```

**Status:** confirmed for named files; directory listing inferred from catalog.

---

### Network Share — `\\I2S109-SOLIDCRM\DBAMFG$\` (READ-ONLY)

This is the primary program and data share. All companies share program files; data files
are per-company (see Company Layout below).

```
DBAMFG$/
├── [Program files — .RWN, .RUN, .DFM, .RTM, .SRC, .DCY]
├── [Database files — *.B (649 tables, Default company)]
├── Default\              Default company data (*.B files)
├── 22\                   Company "22" data (*.B22 files or subdirectory)
├── AB\                   Company "AB"
├── AT\                   Company "AT"
├── CA\                   Company "CA"
├── Goldstar\             Company "Goldstar"
├── I2\                   Company "I2"
├── IT\                   Company "IT"
├── UU\                   Company "UU"
├── DefaultSQL\           Company "DefaultSQL" (ODBC/SQL variant)
├── Testdata\             Test data company
├── DEV\                  Development company
├── Bak Up\               Backup company
├── Menu Backup\          Menu backup company
├── Recovered\            Recovered data
├── LinkDoc\              Document attachment files (EvoLinks storage)
├── FILE.DDF              Pervasive data dictionary — table names + file IDs
├── FIELD.DDF             Pervasive data dictionary — field definitions
├── INDEX.DDF             Pervasive data dictionary — index definitions
├── ATTRIB.DDF            Pervasive data dictionary — attributes
├── OCCURS.DDF            Pervasive repeating groups
├── RELATE.DDF            Pervasive relationships (foreign keys)
├── TRIGGER.DDF           Pervasive triggers
├── VIEW.DDF              Pervasive views
└── PROC.DDF              Pervasive stored procedures
```

**Status:** directory names confirmed; file existence confirmed via DDF parsing.

---

## PROGRAM FILE NAMING CONVENTIONS

### Generation Prefixes

| Prefix | Era | Format | Example |
|--------|-----|--------|---------|
| `BK*` | TAS Pro 3–6 (legacy backbone) | `.RUN` or `.SRC` | `BKAPA`, `BKWOA` |
| `T6*` | TAS Pro 6 | `.RUN` | `T6APB`, `T6INA` |
| `T7*` | TAS Pro 7 (current) | `.RWN` + `.DFM` | `T7APA`, `T7INA` |
| `EVO*` | Platform infrastructure | `.RWN` + `.DFM` | `EvoERPmenu`, `EvoNotes` |
| `IS*` | IStech extensions | `.RWN` or `.RUN` | `ISSRA`, `ISTECH` |
| `J7*` | i2 Systems customizations | `.RWN` + `.DFM` | `J7AIJCG`, `J7BEFWebInv` |
| `MT*` | Master tables (second-gen) | `.RWN` | `MTICMSTR` |

### Module Codes

| Code | Module Name | Menu Count |
|------|-------------|-----------|
| AD | Administration / GL Defaults | — |
| AM | Period-End Close | — |
| AP | Accounts Payable | 19 |
| AR | Accounts Receivable | 17 |
| BM | Bill of Materials | — |
| CM | Company Master / CRM | — |
| CR | Credit / Collections | — |
| CS | Customer Service | 16 |
| DC | Data Collection | — |
| DE | Data Entry | 33 |
| DI | (purpose TBD) | — |
| ED | EDI | — |
| ES | Estimating | — |
| FA | Fixed Assets | — |
| FO | Features & Options | — |
| GL | General Ledger | 16 |
| HH | Handheld Terminals | — |
| IM | Import / Data Loading | — |
| IN | Inventory | 40 |
| IS | (purpose TBD) | — |
| JC | Job Costing | 18 |
| LC | Lot Control | — |
| LM | Labor Management | — |
| LW | Labor / Time & Attendance | 18 |
| MM | Main Menu / Master Maint. | — |
| MR | MRP / Material Requirements | 12 |
| PI | Physical Inventory | — |
| PL | Planning | — |
| PO | Purchase Orders | 29 |
| PR | Payroll | 29 |
| PS | Product Structure | — |
| QC | Quality Control | — |
| QU | Quoting | — |
| RM | Return Material | — |
| RO | Routing | 19 |
| SA | Sales Analysis | 13 |
| SC | Scheduling / Capacity | — |
| SD | Standard Data | 12 |
| SH | Shipping | 16 |
| SM | System Maintenance | 34 |
| SO | Sales Orders | 48 |
| SR | Service / Repair | — |
| SU | Setup | — |
| TA | (purpose TBD) | — |
| US | User Settings | — |
| UT | Utilities | 20 |
| WC | Work Center | — |
| WO | Work Orders | 31 |

---

## MODULE-BY-MODULE FILE MAP

Each module entry lists: program files (`.RWN`/`.RUN`), form files (`.DFM`), and tables (`.B`).
One RWN can have multiple DFM child forms (sub-dialogs, tabs, lookups).

### AP — Accounts Payable

**Program → Forms mapping (confirmed from menu_to_form.csv):**

| Menu | Program | DFM Forms | Description |
|------|---------|-----------|-------------|
| AP-A | BKAPA | T7APA.DFM, T7APABANK.DFM, T7APACON.DFM, T7APAPRC.DFM, T7APASTA.DFM, t7apaC.DFM, t7apae.DFM | Enter Vendors |
| AP-B | BKAPB, T6APB | T7APB.DFM + sub-forms | Enter Vouchers |
| AP-E | BKAPE, t6ape | T7APE.DFM | Print Vouchers Due |
| AP-H | BKAPH (laser: BKAPHA) | T7APH.DFM | Print Checks |
| AP-P | BKAPP | T7APP.DFM | Generate Recurring Vouchers |
| AP-S | APS1999, APS2000, TAPS2000 | T7APS.DFM | 1099 Forms (year-specific programs) |

**Source files available:** `Bkaph.SRC` (continuous checks), `Bkapha.SRC` (laser checks)

**Database tables (BKAP\* family — 24 tables):**

| Table | File | Purpose |
|-------|------|---------|
| BKAPVEND | BKAPVEND.B | AP Vendor master (26+ fields: code, name, address, payment history) |
| BKAPINVL | BKAPINVL.B | AP Invoice / Voucher (36+ fields: vendor, invoice#, date, amounts, 26 GL accounts) |
| BKAPCHKH | BKAPCHKH.B | AP Check header (12 fields: vendor, invoice#, amounts, check date) |
| BKAPCHKF | BKAPCHKF.B | AP Check run file (in-progress check batch) |
| BKAPINVT | BKAPINVT.B | AP Invoice transactions (updated on check posting) |
| BKAPPO | BKAPPO.B | AP Purchase order header |
| BKAPPOL | BKAPPOL.B | AP Purchase order lines |
| BKAPNOTE | BKAPNOTE.B | AP Vendor notes |
| *(+16 more)* | | |

---

### AR — Accounts Receivable

**Program → Forms mapping:**

| Menu | Program | Key DFM | Description |
|------|---------|---------|-------------|
| AR-A | BKARA | T7ARA.DFM + sub-forms | Enter Customers |
| AR-B | BKARB | T7ARB.DFM | Enter Vouchers |
| AR-C | BKARC | T7ARC.DFM | Record Payments |
| AR-D | BKARD | T7ARD.DFM | Charge Interest |
| AR-E | BKARE | T7ARE.DFM | Print Statements |

**Database tables (BKAR\* family — 27 tables):**

| Table | File | Purpose |
|-------|------|---------|
| BKARCUST | BKARCUST.B | AR Customer master (106 fields: code, name, address, GL accounts, credit, terms, salesperson, commissions, discounts, tax, contact info) |
| BKARINV | BKARINV.B | AR Invoice header (84 fields: invoice#, customer, shipping, tax, totals, GL, COGS) |
| BKARINVL | BKARINVL.B | AR Invoice lines (28 fields: invoice#, counter, product code, qty, price, tax, GL) |
| BKARDESC | BKARDESC.B | AR Descriptions |
| BKARSHIP | BKARSHIP.B | AR Ship-to addresses |
| ARTTEMP | ARTTEMP.B | AR Temporary (12 fields: customer, transaction, type, amounts, dates) |
| *(+21 more)* | | |

---

### IN — Inventory

**Program → Forms mapping:**

| Menu | Program | Key DFM | Description |
|------|---------|---------|-------------|
| IN-A | BKINA, lbkina, t6INA, t6INAC | T7INA.DFM (+ 11 sub-forms) | Inventory Inquiry |
| IN-B | BKINB | T7INB.DFM | Enter Inventory |

**Database tables (BKIC\* family — 16 tables):**

| Table | File | Purpose |
|-------|------|---------|
| BKICMSTR | BKICMSTR.B | Item master (64 fields: product code, description, type, UOM, category, cost, pricing, GL accounts, dates, MRP settings, reorder levels) |
| BKICLOC | BKICLOC.B | Inventory locations |
| BKICVAL | BKICVAL.B | Inventory valuation |
| MTICMSTR | MTICMSTR.B | Inventory transaction master (second-gen) |
| INVTXN | INVTXN.B | Inventory transaction detail (types: A/S/P/J/W/I/Q/O/C) |
| BUCKETS | BUCKETS.B | FIFO/LIFO cost buckets |
| DBAFIFO | DBAFIFO.B | FIFO layer tracking |
| *(+9 more)* | | |

---

### SO — Sales Orders

**Program → Forms mapping:**

| Menu | Program | Key DFM | Description |
|------|---------|---------|-------------|
| SO-A | BKSOA, BKSOA2, ISSRA, ISTECH, JKSOS1S | T7SOABKD.DFM, T7SOAC.DFM (+ 9 sub-forms) | View/Enter Sales Orders |

**Database tables (BKSO\* family — 7 tables):**

| Table | File | Purpose |
|-------|------|---------|
| BKSOX | BKSOX.B | Sales order extract / invoice (25 fields: company, invoice#, date, customer, subtotal, tax, freight, total, SO#, terms, ship date) |
| BKSOXH | BKSOXH.B | Sales order header variant (same structure as BKSOX) |
| BKSONOTE | BKSONOTE.B | Sales order notes |
| BKSOPO | BKSOPO.B | SO → PO cross-reference |
| *(+3 more)* | | |

---

### PO — Purchase Orders

**Database tables:** BKAP\* family (shared with AP — BKAPPO, BKAPPOL for PO data)

---

### WO — Work Orders

**Program → Forms mapping:**

| Menu | Program | Key DFM | Description |
|------|---------|---------|-------------|
| WO-A | BKWOA, ISTECH, ISWORPT1 | T7WOA.DFM (+ sub-forms: T7WOAC.DFM, T7WOACFG.DFM, etc.) | Enter Work Orders |
| WO-K-F | (sub-function) | T7WOKF.DFM | Edit Sequence Dates |

**Source files:** `BKAWLB.SRC` (WO schedule report), `BKDCA.SRC` (DC labor/production entry)

**Database tables (WO\* family — 30 tables):**

| Table | File | Purpose |
|-------|------|---------|
| WORKORD | WORKORD.B | Work order master (74 fields: WO prefix/suffix, qty, priority, dates sched/actual, completed qty, status, estimated/actual costs, customer order, instructions, scrap) |
| WORKCHG | WORKCHG.B | Work order change log (25 fields: WO ref, change code, date, user, before/after values) |
| WORKCTR | WORKCTR.B | Work center master |
| WOBOM | WOBOM.B | WO bill of materials |
| WOMAT | WOMAT.B | WO material issues |
| WOLABOR | WOLABOR.B | WO labor entries |
| WOROUT | WOROUT.B | WO routing output / production |
| WOHBOM | WOHBOM.B | WO history BOM |
| MACHINE | MACHINE.B | Machine master |
| TOOL | TOOL.B | Tool master |
| *(+20 more)* | | |

---

### GL — General Ledger

**Database tables (BKGL\* family — 28 tables):**

| Table | File | Purpose |
|-------|------|---------|
| BKGLCOA | BKGLCOA.B | GL Chart of Accounts (65 fields: account code, dept, description, type, CR/DR, balances 1–14, budgets, prior-year, YE balances) |
| BKGLTRAN | BKGLTRAN.B | GL transactions / journal entries |
| BKGLTEMP | BKGLTEMP.B | GL temporary (used during posting) |
| BKGLCHK | BKGLCHK.B | GL check history records |
| BKGLX | BKGLX.B | GL cross-reference / extract |
| *(+23 more)* | | |

---

### BM — Bill of Materials

**Source files:** Referenced from `BKMRF.SRC` (MRP uses BKBMMSTR)

**Database tables (BKBM\* family — 10 tables):**

| Table | File | Purpose |
|-------|------|---------|
| BKBMMSTR | BKBMMSTR.B | BOM master (26 fields: parent product, component, qty required, scrap rate, operation, revision, routing, flags) |
| *(+9 more)* | | |

---

### RO — Routing

**Source files:** `BKROA.SRC` (routing entry program — fully analyzed)

**Database tables (BKRT\* family — 4 tables + shared):**

| Table | File | Purpose |
|-------|------|---------|
| ROUTING | ROUTING.B | Routing master (operations per part) |
| BKRTTEMP | BKRTTEMP.B | Routing operation templates |
| BKRTSPEC | BKRTSPEC.B | Routing specs / notes |
| BKRTCST | BKRTCST.B | Routing costs |
| BKRTEMTR | BKRTEMTR.B | Imported routing records |
| ROUTTEMP | ROUTTEMP.B | Routing template staging |

---

### MR — MRP / Material Requirements

**Source files:** `BKMRF.SRC` (MRP generation — fully analyzed)

**Database tables (BKMR\* family — 3 tables):**

| Table | File | Purpose |
|-------|------|---------|
| MTMRP | MTMRP.B | MRP output — planned order recommendations |
| BKMRPFC | BKMRPFC.B | MRP forecast input |
| BKMRPSW | BKMRPSW.B | MRP switch file (run state tracking) |

---

### PR — Payroll

**Database tables (BKPR\* family — 16 tables):**

| Table | File | Purpose |
|-------|------|---------|
| BKPRMSTR | BKPRMSTR.B | Payroll master (384 fields — largest practical table) |
| BKPRHIST | BKPRHIST.B | Payroll history |
| BKPRW2 | BKPRW2.B | W-2 data |
| *(+13 more)* | | |

---

### DC — Data Collection

**Source files:** `BKDCA.SRC` (DC labor/production entry — fully analyzed)

**Database tables (BKDC\* family — 7 tables):**

| Table | File | Purpose |
|-------|------|---------|
| BKDCSHFT | BKDCSHFT.B | Shift definitions (3 shifts, start/finish times) |
| BKDCTLAB | BKDCTLAB.B | DC temporary labor (in-progress entries) |
| BKDCPLAB | BKDCPLAB.B | DC pending labor (awaiting batch post) |
| *(+4 more)* | | |

---

### Security / System

| Table | File | Purpose |
|-------|------|---------|
| AHSYLOG | AHSYLOG.B | User security: AHSY_USER_LEVL (role, 2 chars), AHSY_USER_MENU (starting menu, 4 chars), AHSY_USER_CTRL (control flag, 1 char), AHSY_USER_ACCES_1..20 (20 × 1-char module permission flags) |
| BKLOGON | BKLOGON.B | Active sessions (10 fields: code, password, company, program, printer, in-use flag, security level, menu, submenu, current printer) |
| BKSYMSTR | BKSYMSTR.B | System master / global config (286 fields: AR/AP/PO invoice numbers, tax rate, 20 payment terms, check accounts, GL accounts, aging buckets, payroll deductions, currency codes) |
| BKYSMSTR | BKYSMSTR.B | System master variant (second config table) |
| ISNOTES | ISNOTES.B | EvoNotes append-only note records |
| CALENDAR | CALENDAR.B | Shop calendar (work days, holidays) |
| SCHEDCAL | SCHEDCAL.B | Schedule calendar variant |

---

### Java Integration

| Table | File | Purpose |
|-------|------|---------|
| ISJAVA | *(not found in DDF — may be runtime-only or different name)* | Java task queue: TAS writes task ID + params, Java reads and executes |

---

### Special / Misc Tables

| Table | File | Purpose |
|-------|------|---------|
| SERIAL | SERIAL.B | Serial number master |
| SERIALH | SERIALH.B | Serial number history |
| LOT | LOT.B | Lot master |
| SCRAP | SCRAP.B | Scrap codes |
| BKSLEVEL | BKSLEVEL.B | (422 fields — second largest table; purpose TBD) |
| BKPRGLFL | BKPRGLFL.B | (664 fields — largest table; purpose TBD) |
| BKABCUST | BKABCUST.B | AB module customer data (5 fields: start date, expiry, period, warning, standalone flag) |
| BKABVEND | BKABVEND.B | AB module vendor data (2 fields: serial, registered name) |
| BKACTRPT | BKACTRPT.B | AC activity reports (9 fields: type, name, RTM template, part/class/cat ranges) |

---

## PLATFORM INFRASTRUCTURE FILES

### Boot / Menu System

| File | Format | Purpose |
|------|--------|---------|
| EvoERPmenu.rwn | RWN (encrypted) | Main menu shell — login, company select, hierarchical menu |
| EVOERPMENU.DCY | DCY (encrypted) | Menu tree / data dictionary for main menu |
| EVOMENU_LOGIN.DCY | DCY (encrypted) | Login form data |
| EVOMENU_SELCOMP.DCY | DCY (encrypted) | Company selection form data |
| EVORESETPASS.DCY | DCY (encrypted) | Password reset form data |
| EVOCHANGEPASS.DCY | DCY (encrypted) | Password change form data |
| suwin6.dcy / suwin7.dcy | DCY (encrypted) | Bootstrap dictionary cache (pre-loads before menu) |
| suwin6t.rwn / suwin7t.rwn | RWN (encrypted) | Bootstrap program (pre-loads before menu) |

### Subsystem Files

| File | Purpose | Tables Used |
|------|---------|-------------|
| EvoNotes.RWN | Note entry / browse | ISNOTES |
| EvoNotesARCH.RWN | Note archiving | ISNOTES |
| EvoNoteSearch.RWN | Full-text note search | ISNOTES |
| EvoNotesPrt.RWN | Note printing | ISNOTES |
| EvoNotesRpt.RWN | Note reporting | ISNOTES |
| EvoScheduler.RWN | Job scheduler UI | BKSCHED\* (table name unconfirmed) |
| EvoSched.RWN | Schedule execution | — |
| EvoSchedSetup.RWN | Scheduler configuration | — |
| EvoService.RWN | Windows service harness | — |
| EvoServiceSetup.RWN | Service install | — |
| EvoServiceRemove.RWN | Service uninstall | — |
| EvoERPbackup.RWN | Backup (uses zipdll) | — |
| EvoLinks.RWN | Document attachment manager | LinkDoc\ folder + mapping table |
| EvoLinkCVT.RWN | Link format conversion | — |
| EvoFNO.RWN | Features & Options configurator | FNO tables |
| EvoFNOSO.RWN | FNO — Sales Orders | — |
| EvoFNOPO.RWN | FNO — Purchase Orders | — |
| EvoFNOWO.RWN | FNO — Work Orders | — |
| EvoUpdate.RWN | In-app software update | FILE\*.UPD manifests |
| EvoERPupd.RWN | Update engine | — |
| EvoPRupd.RWN | Payroll update | — |
| EvoUPDSetup.RWN | Update configuration | — |
| UPDTP7.EXE | Binary patcher (role unconfirmed) | — |
| EvoERPDrillM.RWN | Drill-down / analysis | — |
| CALREM.RWN | Calendar reminders | — |
| CALREMGC.DFM | Google Calendar sync form | — |
| EvoDC.RWN | Data collection main | BKDC\* |
| EvoDCmenu.RWN | Data collection menu | — |
| EvoDCsetup.RWN | Data collection setup | — |

### Platform DFM Forms

| File | Purpose |
|------|---------|
| EVOEMSG.DFM | System message dialog |
| EVOERROR.DFM | File open error dialog |
| EVOGETDATE.DFM | Date picker dialog |
| EVOMESSAGE.DFM | Generic message display |
| EVORESETPASS.DFM | Password reset form |

---

## REPORT FILES (RTM)

Nevrona ReportBuilder templates — 899+ files. Each is a TPF0 binary (Delphi stream).

**Naming pattern:** `[ProgramCode].RTM` or `t7[FunctionCode].RTM`

**Known specific reports:**
| File | Module | Purpose |
|------|--------|---------|
| BKAPHA1.RTM | AP | AP check — laser format 1 |
| BKAPHA2.RTM | AP | AP check — laser format 2 |
| BKAPHA3.RTM | AP | AP check — laser format 3 |
| ENARE4.RTM | AR | AR aged statement |
| t7ing1.rtm | IN | IN-G inventory labels |

All 899+ RTM files are in `DBAMFG$\` alongside their calling `.RWN` programs.

---

## J7\* CUSTOMIZATION FILES (i2 Systems)

37 customer-specific modules, 109 files (DFM + RWN pairs):

| Module Prefix | Example Files | Purpose |
|---------------|---------------|---------|
| J7AIJCG | J7AIJCG.RWN, J7AIJCG.DFM | (purpose TBD from DFM) |
| J7BEFWebInv | J7BEFWebInv.RWN, J7BEFWebInv.DFM | Web inventory (inferred) |
| J7CCCutSheet | J7CCCutSheet.RWN, J7CCCutSheet.DFM | Cut sheet printing |
| J7CRSOW | J7CRSOW.RWN, J7CRSOW.DFM | CR → SO workflow |
| J7DCMatLabels | J7DCMatLabels.RWN, J7DCMatLabels.DFM | DC material labels |
| J7EIMDCRev | J7EIMDCRev.RWN, J7EIMDCRev.DFM | EIM DC revision |
| J7HH\* | Multiple | Handheld terminal variants |

---

## FILE RELATIONSHIP MAP

```
StartEvo.exe
  └── tp7runtime.exe (reads taspro7.ini)
        ├── EvoERPmenu.rwn  ←→  EVOERPMENU.DCY  (menu tree)
        │     ├── EVOMENU_LOGIN.DCY  (login data)
        │     └── EVOMENU_SELCOMP.DCY  (company select)
        │
        └── [Module].RWN  ←→  [Module].DFM  (form layout)
              ├── Reads/writes  *.B  (Btrieve tables via c4dll.dll / Pervasive)
              ├── Calls  EXEC_RB → [Report].RTM  (ReportBuilder output)
              ├── Calls  ISJAVA task queue → EvoPVT.jar  (Java tasks)
              └── References  [Module].DCY  (encrypted data dictionary)
```

**DFM ↔ RWN pairing rule:** Same basename. One RWN typically has one main DFM plus
several child DFMs (sub-dialogs, lookups, tabs). Example: `BKAPA.RWN` ↔ `T7APA.DFM`
(main) + `T7APABANK.DFM` + `T7APACON.DFM` + `T7APAPRC.DFM` + `T7APASTA.DFM` +
`t7apaC.DFM` + `t7apae.DFM`.

Note: The form filename prefix shifts from `BK*` (program) to `T7*` (form) for TAS Pro 7
era modules. Example: program `BKAPA` uses forms `T7APA*`.

---

## PERVASIVE DDF FILE RELATIONSHIPS

```
FILE.DDF   → maps table names to file IDs
FIELD.DDF  → maps field names to file IDs + offsets + types
INDEX.DDF  → maps index definitions to file IDs (→ primary keys)
RELATE.DDF → defines foreign key relationships between tables
VIEW.DDF   → SQL views built over Btrieve tables
```

All queryable via Pervasive ODBC: `SELECT * FROM X$File`, `SELECT * FROM X$Field WHERE
Xf$File = (SELECT Xi$File FROM X$Index WHERE ...)`.

---

*Last updated: 2026-06-11 — built from menu_to_form.csv, master_index.csv, tables.txt,
schema.md, SRC analysis, and catalog.md. Confidence varies by section — see EVO-DECOMPILE-TODO.md.*
