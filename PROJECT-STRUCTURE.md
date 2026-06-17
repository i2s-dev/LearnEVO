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
| BKARINV | BKARINV.B | AR Invoice header (46+ fields: invoice#, SO#, INVCD type flag, date, customer, shipping, terms, totals, NL line count, RTS release flag, GL) — unposted and posted records |
| BKARINVL | BKARINVL.B | AR Invoice lines (28 fields: invoice#, counter, ESD, PCODE, PDESC, qty, price, disc, ext, COGS, ITYPE item type copy, TXBLE, UBO, USTD, RTS release-to-ship flag, LOC, ABQTY) |
| BKARINVI | BKARINVI.B | SO→invoice staging cross-ref (16 fields: SONUM+INVNM key, ESD, PCODE, qty, price, disc, ext, COGS, ITYPE, extr margin, commissions, freight, coop, tax) |
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
| BKICMSTR | BKICMSTR.B | Item master (64 fields, 617-byte records): PROD_CODE (key,15), PROD_DESC (30), PROD_TYPE (1 char at offset 45: R=raw/purchased, N=non-stock, F=finished, A=assembly, M=misc, K=kit, B=phantom, L=labor, T=tool, O=outside-svc), UM, CAT, CLASS, costs, pricing, GL accounts, UOH, MRP switch, reorder levels. Binary Btrieve format. Located at Default\BKICMSTR.B (71680 bytes) |
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
| BKPIMSTR | BKPIMSTR.B | PI Master — Physical Inventory freeze/count control record |
| BKSBPART | BKSBPART.B | Substitute/alternate part master — maps primary item to substitutes |
| BKSBMFG | BKSBMFG.B | Sub-manufacturing — outsourced/subcontracted job tracking |
| BKPRCOMM | BKPRCOMM.B | PR Commissions — sales commission records |
| BKPRCURP | BKPRCURP.B | PR Current Payroll batch — active payroll run data |
| BKPRINFO | BKPRINFO.B | PR Employee Info — extended employee demographics |
| BKICREF | BKICREF.B | IC Item Cross-Reference — alternate item codes / vendor part numbers |
| BKICLOCM | BKICLOCM.B | IC Location Master — warehouse location definitions |
| BKCMACCL | BKCMACCL.B | CM Account Links — CRM account relationship links |
| BKCMVNDH | BKCMVNDH.B | CM Vendor History — CRM activity history for vendors |
| BKCMVNDF | BKCMVNDF.B | CM Vendor Footer — CRM vendor detail footer |
| BKCPEC | BKCPEC.B | Compliance/customs data (customs entry / import compliance) |
| BKRFQ | BKRFQ.B | Request for Quote master — vendor RFQ records |
| ISICMSTR | ISICMSTR.B | IS IC Master — extended inventory item data beyond BKICMSTR |
| ISCATMST | ISCATMST.B | IS Category Master — item category definitions |
| ISORDECO | ISORDECO.B | IS Order Decoration — custom decoration/processing instructions per SO line |
| ISWOROEX | ISWOROEX.B | IS WO Routing Operations Extensions — per-operation extra data |
| ISWOEX | ISWOEX.B | IS WO Extensions — WO dispatch status + operator notes (Paperless SF) |
| ISWOEX (= ISWOROEX) | | See above |
| ISQSOA | ISQSOA.B | IS Quick SO — staging table for Quick Sales Order entry |
| ISUDFINV | ISUDFINV.B | IS UDF Invoice — user-defined fields on AR invoices |
| ISESTDTL | ISESTDTL.B | IS Estimating Detail — estimate line detail records |
| ISSOBOX | ISSOBOX.B | IS SO Box/Packing — packing/boxing instructions per SO |
| ISSOREVU | ISSOREVU.B | IS SO Review — SO approval/review staging |
| ISAREX | ISAREX.B | IS AR Export — AR invoice export staging |
| ISAPEX | ISAPEX.B | IS AP Export — AP check/payment file export staging |
| ISCONVRT | ISCONVRT.B | IS Conversion Rate — unit-of-measure conversion table |
| ISRTMS | ISRTMS.B | IS RTM Summary — report template routing/printing rules |
| ISTAXGRP | ISTAXGRP.B | IS Tax Group — customer/item tax group assignments |
| ISFUTYPE | ISFUTYPE.B | IS Follow-Up Type — CAR follow-up type codes |
| ISSPC | ISSPC.B | IS SPC — routing operation to SPC data feed link |
| ISCCICM | ISCCICM.B | IS CC IC Master — CC customer item configuration |
| ISCHAINM | ISCHAINM.B | IS Chain Master — multi-company chain definition |
| ISQSOA | ISQSOA.B | IS Quick SO staging |
| WCTRLOAD | WCTRLOAD.B | Work Center Load — capacity loading by date bucket |
| WOEXCHG | WOEXCHG.B | WO Exchange — inter-company WO transfer records |
| DBAFIFO | DBAFIFO.B | DBA FIFO cost layers — inventory costing layers (DBA-era) |
| QCCODES | QCCODES.B | QC Codes master — defect classification codes |
| BKRTSPEC | BKRTSPEC.B | Routing Spec — routing operation specification detail |
| MKECLASS | MKECLASS.B | Make Class — manufacturing/purchasing class codes |
| BKCPMSTR | BKCPMSTR.B | Cost Period Master — labor cost period tracking |
| BKESTCFG | BKESTCFG.B | Estimating Config — module-level estimating defaults |
| BKFOCFG | BKFOCFG.B | FO Config — Features & Options module defaults |
| BKLUGRID | BKLUGRID.B | Lookup Grid — grid column layout definitions |
| ISDRILLM | ISDRILLM.B | IS Drill-Down Master — drill-down menu definitions |
| ISDROP | ISDROP.B | IS Dropdown — dropdown list definitions |
| ISREPDEF | ISREPDEF.B | IS Report Def — report parameter defaults |
| ISREPLNK | ISREPLNK.B | IS Report Link — report-to-menu action links |
| ISBROKER | ISBROKER.B | IS Broker — customs/freight broker records |
| BKPRSALE | BKPRSALE.B | PR Sale — sales commission by period (payroll) |
| BKARHTAX | BKARHTAX.B | AR Head Tax — AR invoice head/body tax |
| ISSRMMS | ISSRMMS.B | IS SR MMS — Service Repair maintenance management system data |
| BKCPEC | BKCPEC.B | Compliance/customs data |
| ESTSUM | ESTSUM.B | Estimate Summary — estimating rollup records |
| CLASS | CLASS.B | Class master (short alias of CLASMSTR) |
| ISSMTCFG | ISSMTCFG.B | IS SMT Config — surface mount technology machine config (PCB assembly) |
| ISSERIAL | ISSERIAL.B | IS Serial — active serial number tracking (complement to SERIAL master) |
| ISUDMSTR | ISUDMSTR.B | IS UD Master — user-defined field type definitions |
| ISJOB | ISJOB.B | IS Job master — job cost number master |
| ISORDDSC | ISORDDSC.B | IS Order Discount codes |
| ISSHPVIA | ISSHPVIA.B | IS Ship Via — freight carrier/shipping method codes |
| BKCMLEAD | BKCMLEAD.B | CRM Lead Source codes |
| BKCMTERR | BKCMTERR.B | CRM Territory codes |
| BKCMACFC | BKCMACFC.B | CRM Account Financial Category |
| BKCMDTCD | BKCMDTCD.B | CRM Document Type codes |
| ISGLCOA | ISGLCOA.B | IS GL COA — extension to chart of accounts (multi-year history/budget) |
| ISGLDATE | ISGLDATE.B | IS GL Date — current GL period dates per company/module |
| BKGLTRAN | BKGLTRAN.B | GL transaction register — all posted GL entries |
| MACHINE | MACHINE.B | Machine master — specific machines within work centers |
| TOOL | TOOL.B | Tool master — cutting tools, fixtures, jigs per routing operation |
| ISFSCLAS | ISFSCLAS.B | IS Field Service Class — service class master (Field Service module) |
| ISFSINFO | ISFSINFO.B | IS Field Service Info — field service information/call records |
| ISPRINFO | ISPRINFO.B | IS PR Info — payroll employee profile/info records |
| ISARCHG | ISARCHG.B | IS AR Charge — extra charges added to AR invoices beyond line items |
| ISAPCHG | ISAPCHG.B | IS AP Charge — extra charges on AP side (parallel to ISARCHG) |
| ISICMSTR | ISICMSTR.B | IS IC Master — secondary/extension item master (alternate item config) |
| ISREMIND | ISREMIND.B | IS Remind — reminder/follow-up records (date + contact + trigger type) |
| ISREPLNK | ISREPLNK.B | IS Replace Link — record-link replacement tracking |
| ISREPDEF | ISREPDEF.B | IS Report Defaults — saved report parameter defaults per user/report |
| ISSTYPE | ISSTYPE.B | IS Service Type — shared service/storage/equipment type code table |
| ISSEPROC | ISSEPROC.B | IS SE Process — service error process codes (SR module support) |
| ISSETYPE | ISSETYPE.B | IS SE Type — service error category type codes |
| ISBINLOC | ISBINLOC.B | IS Bin Location — bin location master (distinct from BKICLOC item locations) |
| ISBINLOT | ISBINLOT.B | IS Bin Lot — bin + lot cross-reference (which lots are in which bins) |
| ISACCESS | ISACCESS.B | IS Access — module access/license control (which modules are enabled) |
| ISSHIPCO | ISSHIPCO.B | IS Ship Company — shipping company/carrier master (codes, names, contacts) |
| ISREPORD | ISREPORD.B | IS Repeat Order — standing/recurring AR order records |
| ISDEPT | ISDEPT.B | IS Department — department master (dept codes, names, GL accounts) |
| ISMCF | ISMCF.B | IS Multi-Currency Foreign — foreign exchange configuration (base currency, conversion) |
| ISBUILD | ISBUILD.B | IS Build — build/kit operation record (BOM build tracking) |
| BKICTAX | BKICTAX.B | BK IC Tax — item-level tax classification codes |
| BKARTXN | BKARTXN.B | BK AR Transaction — AR transaction/activity log |
| FILEDES | FILEDES.B | File Descriptions — purpose strings for each registered DB file |
| LOT | LOT.B | Lot master — lot records (distinct from MTLOT which is multi-company variant) |
| ISSCHED | ISSCHED.B | IS Scheduler — EvoScheduler job table (confirmed by EvoSched.RWN + EvoScheduler.RWN + EVOSERVICE.RWN) |
| SCHEDCAL | SCHEDCAL.B | Schedule Calendar — calendar used by shop scheduling due-date changes (T7SHE) |
| ISLINKS | ISLINKS.B | IS Links — document attachment cross-reference: maps record keys to linked document filenames |
| ISBSF | ISBSF.B | IS Business Score File — cross-module KPI/business performance aggregation |
| EIMCOLST | EIMCOLST.B | EIM Column List — column configuration for EIM/DC integration |
| ISESTDTL | ISESTDTL.B | IS Estimate Detail — line items from estimate records |
| BKMRPPO | BKMRPPO.B | BK MRP PO — MRP-generated purchase order recommendations |
| BKSBVEND | BKSBVEND.B | BK Sub-contract Vendor — sub-contracting vendor table |
| ISSERCNT | ISSERCNT.B | IS Serial Count — serial number counter/sequence control per item |
| ISSDET | ISSDET.B | IS Standard Detail — type/detail code pairs (used with ISSTYPE) |
| BKSYUSER | BKSYUSER.B | BK SY User — additional session/user tracking table |
| ISTRIGRS | ISTRIGRS.B | IS Trigger Results — automated trigger execution/result log |
| BKLUGRID | BKLUGRID.B | BK Lookup Grid — lookup grid column layout configuration |
| BKPIMSTR | BKPIMSTR.B | BK PI Master — physical inventory run master (one record per PI session) |
| BKPILOT | BKPILOT.B | BK PI Lot — PI lot count records (lot, location, counted qty) |
| BKPIPHYS | BKPIPHYS.B | BK PI Physical — PI physical count records (item, location, count qty) |
| BKPISER | BKPISER.B | BK PI Serial — PI serial count records (serial#, item, found/missing) |
| BKPIFROZ | BKPIFROZ.B | BK PI Frozen — PI inventory snapshot at freeze time (baseline for variance) |
| PIBINLOC | PIBINLOC.B | PI Bin Location — frozen bin-location records at PI start |
| PIBINLOT | PIBINLOT.B | PI Bin Lot — frozen bin-lot records at PI start |
| BKESTCFG | BKESTCFG.B | BK Estimate Config — estimate module settings (method, markup, numbering) |
| BKMATCST | BKMATCST.B | BK Material Cost — estimate line-level material cost + pricing detail |
| BKRFQ | BKRFQ.B | BK RFQ — Request for Quote master (vendor RFQ records tied to estimates) |
| BKRTCST | BKRTCST.B | BK Routing Cost — routing cost detail (labor/machine cost per estimate operation) |
| BKICPMAT | BKICPMAT.B | BK IC Purchase Material — item-level purchase material category/config |
| BKICREF | BKICREF.B | BK IC Reference — item cross-reference (alt part numbers, customer/vendor part#) |
| BKICVAL | BKICVAL.B | BK IC Values — item valuation extension (additional costing/pricing data) |
| BKICDIM | BKICDIM.B | BK IC Dimension — item physical dimensions (size, weight for shipping) |
| BKBMDIM | BKBMDIM.B | BK BOM Dimension — BOM component dimension overrides |
| BKBMNOTE | BKBMNOTE.B | BK BOM Note — text notes attached to BOM components |
| BKBMREMK | BKBMREMK.B | BK BOM Remark — structured remarks on BOM components |
| BKSBPART | BKSBPART.B | BK Sub-contract Part — components sourced from outside process/subcontract vendors |
| BKSBMFG | BKSBMFG.B | BK Sub-contract Mfg — subcontracted manufacturing operation records |
| BKMENUSU | BKMENUSU.B | BK Menu User — per-user menu/toolbar layout settings |
| BKPSUSER | BKPSUSER.B | BK PS User — per-user personal settings (printer, column, preference records) |
| BKSAREPT | BKSAREPT.B | BK SA Report — sales analysis saved report template definitions |
| BKDCCFG | BKDCCFG.B | BK DC Config — data collection terminal/station configuration |
| BKDCLAB | BKDCLAB.B | BK DC Labor — data collection labor entry records (raw labor from DC terminals) |
| BKEDMSTR | BKEDMSTR.B | BK EDI Master — EDI trading partner / transaction set master |
| BKEDIDUN | BKEDIDUN.B | BK EDI Data Element — EDI data element definitions and mappings |
| BKEDNOTE | BKEDNOTE.B | BK EDI Note — EDI transaction notes / audit comments |
| BKEDPOST | BKEDPOST.B | BK EDI Post — EDI posting log (transaction transmission history) |
| BKGLX | BKGLX.B | BK GL Extended — GL extended transaction data (supplemental GL fields) |
| BKGLGJRN | BKGLGJRN.B | BK GL GJ Journal — GL general journal header records |
| BKGLGJLN | BKGLGJLN.B | BK GL GJ Line — GL general journal line entries |
| BKGLFSTL | BKGLFSTL.B | BK GL Financial Statement Layout — user-defined financial statement layouts |
| ISGLNBGT | ISGLNBGT.B | IS GL New Budget — new/revised GL budget entries (separate from BKGLCOA budgets) |
| ISAREX | ISAREX.B | IS AR Extra — extended AR customer/invoice additional data |
| ISARINVX | ISARINVX.B | IS AR Invoice Extra — invoice-level extra fields and overrides |
| BKARDEP | BKARDEP.B | BK AR Deposit — AR customer deposit records |
| BKARDEP | BKARDEP.B | BK AR Deposit — AR customer deposit records |
| BKARINVT | BKARINVT.B | BK AR Invoice Transaction — AR invoice transaction/posting history |
| BKART | BKART.B | BK AR Transaction — short-form AR transaction records |
| ISRMAC | ISRMAC.B | IS RMA Credit — RMA credit note records (return merchandise credit authorization) |
| ISRMAI | ISRMAI.B | IS RMA Invoice — RMA auto-invoice records (return material invoice generation) |
| ISFOHEAD | ISFOHEAD.B | IS FO Header — field order header (order#, customer, dates, status) |
| ISFOLINE | ISFOLINE.B | IS FO Line — field order line items (product, qty, price) |
| ISFOORDL | ISFOORDL.B | IS FO Order List — multi-field order management list |
| ISBANKS | ISBANKS.B | IS Banks — bank account master (account codes, bank names, GL accounts) |
| ISBNMSTR | ISBNMSTR.B | IS Bank Name Master — bank name/routing reference |
| ISNUMBER | ISNUMBER.B | IS Number — auto-increment number sequence definitions (counters per entity type) |
| BKFOCFG | BKFOCFG.B | BK FO Config — field order module configuration settings |
| BKSYAP | BKSYAP.B | BK SY AP — system-level AP configuration (AP defaults, aging, terms defaults) |
| QCCODES | QCCODES.B | QC Codes — quality control code master (defect codes, disposition codes) |
| BKQCMSTR | BKQCMSTR.B | BK QC Master — QC test/inspection master records |
| BKQCTRAN | BKQCTRAN.B | BK QC Transaction — QC inspection transaction records (pass/fail per inspection) |
| ISQCMTHD | ISQCMTHD.B | IS QC Method — QC inspection method definitions |
| ISQCSPEC | ISQCSPEC.B | IS QC Specification — QC product specification records |
| WORECV | WORECV.B | WO Receive — WO production receipt records (parts received/completed per op) |
| WOBOMREM | WOBOMREM.B | WO BOM Remark — remarks attached to WO BOM components |
| WOEXCHG | WOEXCHG.B | WO Exchange — WO part/material exchange/substitution records |
| ISNCR | ISNCR.B | IS NCR — non-conformance report records (linked to QC/AC module) |
| ISDEFECT | ISDEFECT.B | IS Defect — defect tracking records |
| OUTPROC | OUTPROC.B | Outside Process — outside processing operation records (WO ops sent to external vendors) |
| SCHWO | SCHWO.B | Scheduled WO — scheduled work order records (linked to shop scheduling) |
| WCCTL | WCCTL.B | WC Control — warehouse control operation control records |
| WCTRLOAD | WCTRLOAD.B | WC TR Load — warehouse control transaction loading records |
| ISTERMS | ISTERMS.B | IS Terms — payment terms definitions (net-days, discount %, EOM flag) |
| ISTAXGRP | ISTAXGRP.B | IS Tax Group — tax group/nexus definitions (state, county, city tax combos) |
| ISTAXFIL | ISTAXFIL.B | IS Tax File — tax filing records |
| ISSHPVIA | ISSHPVIA.B | IS Ship Via — shipping via/method codes (UPS, FedEx, common carrier, etc.) |
| ISSOBOX | ISSOBOX.B | IS SO Box — SO packing/box assignments for multi-box shipments |
| ISRTLOAD | ISRTLOAD.B | IS Routing Load — routing load balancing data |
| ISORDECO | ISORDECO.B | IS Order ECO — engineering change orders linked to specific customer orders |
| ISECO | ISECO.B | IS ECO — engineering change order master |
| ISUSAGE | ISUSAGE.B | IS Usage — item usage tracking (consumption history by customer/period) |
| BKSHORT | BKSHORT.B | BK Short — short supply records (items short on WO/SO orders) |
| MKECLASS | MKECLASS.B | MK/Mkt E-Class — marketing/external classification codes |
| LANGDICT | LANGDICT.B | Language Dictionary — multi-language label translations for UI fields |
| TASCOLOR | TASCOLOR.B | TAS Color — user-defined color scheme settings |

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

---

## Pass 12 — New Tables (2026-06-17)

| Table | Module | Purpose | Status |
|-------|--------|---------|--------|
| BKGLSTMT | GL-F (T7GLF) | GL statement templates — named financial report layouts (P&L, Balance Sheet, etc.) | inferred |
| BKGLFSTL | GL-N (T7GLN) | GL financial statement line definitions — user-defined row format for BKGLSTMT reports | inferred |
| BKGLGJRN | GL-B (T7GLB) | GL general journal headers — batch/journal header records for manual journal entries | inferred |
| BKGLGJLN | GL-B (T7GLB) | GL general journal lines — individual debit/credit lines within a journal entry | inferred |
| BKPRCURP | PR (T7PRB) | PR current period data — YTD and period-to-date amounts per employee | inferred |
| BKPRFTAX | PR (T7PRA) | PR federal tax tables — federal and state withholding rate schedules | inferred |
| BKPRGLFL | PR (T7PRB) | PR GL flags/accounts — maps each payroll expense type to its GL account code | inferred |
| BKPRINFO | PR (T7PRB) | PR employee additional info — supplemental employee fields beyond BKPRMSTR | inferred |
| BKPRTC | PR (T7PRK) | PR time card records — individual time entries per employee per job/operation | inferred |
| BKARINVI | TC (T7TCC) | AR invoice inventory — links AR invoices to inventory transaction records | inferred |
| BKART | TC (T7TCC) | AR transaction short log — condensed transaction record for AP/AR quick lookup | inferred |
| ISCHAINM | CH (T7CHAIN) | Chain/multi-location master — location codes, names, relationships for multi-site EVO | inferred |
| ISDROP | DR (T7DROPDOWN) | Dropdown list master — user-configurable picklist options for configurable fields | inferred |
| ISCTREVU | CR (T7CTREVU) | Contract review — SO approval workflow state (department, password, status) | confirmed |

---

---

## Pass 13 — New Tables (2026-06-17)

| Table | Module | Purpose | Status |
|-------|--------|---------|--------|
| MTMRP | MR (T7MRG) | MRP planned orders — calculated buy/make recommendations with qty + due date | inferred |
| MTICMSTR | MR (T7MRD) | MRP shadow item master — snapshot of BKICMSTR used during MRP calculation run | inferred |
| BKMRPFC | MR (T7MRADE) | MRP firm changes — user overrides to planned orders that survive regeneration | inferred |
| BKMRPPO | MR (T7MRJ) | MRP planned purchase orders — unconfirmed buy suggestions before PO release | inferred |
| ISBUILD | MR (T7MRH) | Build schedule — manually-entered production targets that feed MRP demand | inferred |
| ISICMSTR | MR (T7MRI) | IS item configuration master — extended item config for multi-location MRP | inferred |
| ISARDEPL | AR (T7ARN) | AR deposit lines — line-level payment application detail within a deposit record | inferred |
| MKAHIST | ISTECH.LIB (infra) | MKA audit history — system-wide change/event log opened by nearly every module | inferred |
| ISLOG | ISTECH.LIB (infra) | IS activity log — user action audit trail opened by nearly every module | inferred |
| ISIS | ISTECH.LIB (infra) | IS image/icon system — UI icon or image lookup table (universal) | inferred |
| BKCMACCN | ISTECH.LIB (infra) | CM account number lookup — shared account code cross-reference (universal) | inferred |
| BKAPDESC | ISTECH.LIB (infra) | AP/AR description lookup — shared description text table (universal) | inferred |

---

---

## Pass 14 — New Tables (2026-06-17)

| Table | Module | Purpose | Status |
|-------|--------|---------|--------|
| ISMCR | SM (T7SMCA) | IS Master Category Reference — item category master code lookup | inferred |
| ISSMTCFG | SM (T7SMTEND) | IS Smart Terminal config — machine-to-terminal binding for DC/WO entry | inferred |
| ISNTYPE | SM (T7SMN) | IS Note type — note category master (defines valid note types) | inferred |
| ISNOTES | SM (T7SMN) | IS Notes — cross-module note text records (all entity types) | inferred |
| ISSHPVIA | SM (T7SMT) | IS Ship Via — shipping method codes (UPS, FedEx, truck, etc.) | confirmed |
| ISSHIPCO | SM (T7SMO) | IS Ship Company — carrier/shipping company master | inferred |
| ISORDDSC | SM (T7SMW) | IS Order Description — order description/reference code master | inferred |
| ISJOB | SM (T7SMPF) | IS Job — GL job code master for job-costing sub-accounts | inferred |
| ISCYCLCD | SM (T7SMPH) | IS Cycle Code — cycle count frequency codes assigned per item class | inferred |
| ISUDMSTR | SM (T7SMPB) | IS User-Defined Master — user-defined field set master | inferred |
| ISICUL | SM (T7SMPJ) | IS IC Unit Level — item count unit-level (multi-UOM hierarchy) | inferred |
| ISPRCONS | SM (T7SMG) | IS PR Constants — PR employee constants/payroll config table | inferred |
| BKCMVNDH | SM (T7SMJN) | BK CM Vendor Header — CRM vendor notes header | inferred |
| BKCMVNDF | SM (T7SMJN) | BK CM Vendor Footer — CRM vendor notes detail | inferred |
| ISBROKER | SM (T7SMJN) | IS Broker — freight broker master records | inferred |
| BKCPEC | SM (T7SMJN) | BK CP EC — CRM prospect/contact extended codes | inferred |
| BKISTAX | SM (T7SME) | BK IS Tax — item-level tax override records | inferred |

---

---

## Pass 16 — New Tables (2026-06-17)

| Table | Module | Purpose | Status |
|-------|--------|---------|--------|
| ISAPEX | TPOA | AP extended fields — supplemental per-line AP/PO data | inferred |
| ISMCF | TPOA | IS Manufacturing Config Flags — per-company manufacturing settings | inferred |
| WORKCHG | EVONOTESARCH | Work Order Change log — field-level audit trail of every WO modification | inferred |
| SUMPNCUS | AUTOT7MRF | Summary by customer — MRP demand aggregation table | inferred |
| BKMRPSW | AUTOT7MRF | MRP switch/run control — settings and state for MRP batch execution | inferred |
| ISBINLOT | AUTOT7POJC | Bin lot assignments — bin-level lot location records | inferred |
| ISGLDATE | AUTOT7POJC | GL date control — open/closed period flags per GL period | inferred |
| SCRAP | AUTOT7POJC | Scrap records — WO scrap transaction log | inferred |
| ISFOHIST | EVONOTESARCH | F/O history — archived Features & Options selections | inferred |
| ISFOBMRM | EVOFNO | F/O BOM remarks — notes on Features & Options BOM components | inferred |
| ISREPDEF | EXCOM | Report Definition master — named external report templates | inferred |
| ISREPORD | EXCOM | Report Order/queue — scheduled report run records | inferred |
| FILEDBF | WTASDMGR | Pervasive DDF column definitions (file DBF schema) | confirmed |
| FILEDFLD | WBKLUGRID | Pervasive DDF default field settings | confirmed |
| FILEKNUM | WTASDMGR | Pervasive DDF key number index | confirmed |
| BKCMACCT | NZEMAILTLL | BK CRM Account — CRM customer/vendor account records | inferred |

---

---

## Pass 17 — Cross-Module Framework Tables (2026-06-17)

| Table | File | Module scope | Purpose | Status |
|-------|------|-------------|---------|--------|
| SERIAL | SERIAL.B | 460 modules | Serial number master — one record per tracked serial; location, status, history | confirmed |
| ISNCR | ISNCR.B | 420 modules | Non-Conformance Report — QC flag raised on any failing transaction | confirmed |
| DBAFIFO | DBAFIFO.B | 382 modules | DBA FIFO cost layers — FIFO inventory costing bucket per item/receipt | confirmed |
| BKGLX | BKGLX.B | 297 modules | GL extended transaction — extended posting data per BKGLTRAN line | inferred |
| BKICLOCM | BKICLOCM.B | 294 modules | Inventory location master — on-hand quantity per item × location | confirmed |
| CLASS | CLASS.B | 259 modules | Item class code — current class code record (joined for filtering) | confirmed |
| BKARINVL | BKARINVL.B | 272 modules | AR invoice lines — SO/invoice line items; most-joined transactional table | confirmed |
| BKAPPOL | BKAPPOL.B | 266 modules | AP PO lines — PO/AP invoice line items | confirmed |
| MKECLASS | MKECLASS.B | 202 modules | MKE class — manufacturing/engineering item class master | inferred |
| WORKCTR | WORKCTR.B | 208 modules | Work center master — production work center definitions with capacity | confirmed |
| BKICLOC | BKICLOC.B | 215 modules | Inventory by location — on-hand quantity per item × location | confirmed |
| CLASMSTR | CLASMSTR.B | 136 modules | Class master — class code master with descriptions and GL accounts | confirmed |
| BKPRMSTR | BKPRMSTR.B | 161 modules | PR employee master — one record per employee | confirmed |
| ISTAXGRP | ISTAXGRP.B | 154 modules | Tax group master — tax group codes for tax calculation | confirmed |
| BKGLCOA | BKGLCOA.B | 109 modules | GL Chart of Accounts — account number master | confirmed |
| LOT | LOT.B | 119 modules | Lot master — lot number master records with quantity and status | confirmed |
| MACHINE | MACHINE.B | 87 modules | Machine master — individual machines within a work center | confirmed |
| TOOL | TOOL.B | 83 modules | Tool master — tooling definitions used in routing operations | inferred |
| ISSOBOX | ISSOBOX.B | 68 modules | SO box/packing — packing box assignments for multi-box shipments | confirmed |
| BKGLCHK | BKGLCHK.B | 41 modules | GL check — AP checks that have posted to GL | confirmed |
| CALENDAR | CALENDAR.B | 17 modules | Shop calendar — work days and shifts per work center | confirmed |
| IS2DBAR | IS2DBAR.B | 51 modules | 2D barcode — 2D barcode scan data for receiving and DC | inferred |
| BKSYAR | BKSYAR.B | 115 modules | System AR config — company-level AR settings and defaults | inferred |
| ISUDFINV | ISUDFINV.B | 83 modules | User-defined invoice fields — custom fields on AR invoices | inferred |
| BKICREF | BKICREF.B | 63 modules | Item cross-reference — customer/vendor part # ↔ internal part # | confirmed |
| ISDUTY | ISDUTY.B | 56 modules | Duty — import duty records for landed cost | inferred |
| ISORDECO | ISORDECO.B | 120 modules | IS Order ECO — engineering change orders linked to orders | confirmed |
| ISECO | ISECO.B | 49 modules | ECO master — engineering change order master records | confirmed |
| OUTPROC | OUTPROC.B | 60 modules | Outside process — WO operations sent to external vendors | confirmed |
| BUCKETS | BUCKETS.B | 18 modules | FIFO cost buckets — detailed FIFO bucket per item/receipt | confirmed |
| WOBOM | WOBOM.B | WO | WO BOM — component list for a specific work order | confirmed |
| WOLABOR | WOLABOR.B | WO | WO labor — actual labor recorded against a WO operation | confirmed |
| WOMAT | WOMAT.B | WO | WO materials — actual material issued to a WO | confirmed |
| WOROUT | WOROUT.B | WO | WO routing — routing operations attached to a WO | confirmed |
| WORECV | WORECV.B | WO | WO receipts — completed assemblies received from a WO | confirmed |
| WODATE | WODATE.B | WO | WO dates — planned/actual start, finish, and due dates per WO | confirmed |
| WOEXCHG | WOEXCHG.B | WO | WO exchange — WO-level transfer records | inferred |
| WOBOMREM | WOBOMREM.B | WO | WO BOM remarks — notes on WO BOM lines | inferred |

## Pass 18 — SO posting tables, infrastructure lookups, shop-floor tray (2026-06-17)

| Table | File | Modules | Purpose | Status |
|-------|------|---------|---------|--------|
| DBAHLPID | DBAHLPID.B | 1389 | DBA Help ID — maps 8-char ref code → help topic number. Opened by every module for F1 context help. Infrastructure only; not a fingerprint table. | confirmed |
| BKSYHELP | BKSYHELP.B | 1344 | System Help Path — single record: BKSY_HELP_PATH (70 chars) = path to EvoHELP.CHM. Infrastructure. | confirmed |
| BKSYPRTR | BKSYPRTR.B | 35 | System Printer config — keyed by PRTR_NAME (30). Fields: EXEC (print cmd), TAS flag, LPTNM (port), TYPE, PWDT (page width), PMAX, PPLNE, LASER. Maps logical printer names to physical device commands. | confirmed |
| BKARTNOT | BKARTNOT.B | 22 | AR Transaction Notes — keyed by TRXN#(8)+CNTR(2). Single text field DESC(30). Free-text memo lines attached to AR/SO transactions. | confirmed |
| BKARINVV | BKARINVV.B | 44 | AR Invoice V — keyed by INVV_CODE(10)+INVV_NUM(6)+DATE. 78 fields. INVV_CHK = check#, TERMD/TERMN = terms, TYPED/TYPEN = payment type. Likely AR cash receipts / payment voucher records. | inferred |
| ISARTXNB | ISARTXNB.B | 35 | IS AR Transaction B — keyed by SONUM+PART_CODE+LINEID. 24 fields: BIN(15), LOC(10), QTY, LOT(15), SERIAL(25), DATE, TIME. Tracks which bin/lot/serial was picked for each SO line during shipping. | confirmed |
| ISSRINFO | ISSRINFO.B | 82 | IS SR Info — keyed by SRNUM(8)+UID(8). 55 fields: CODE(15), 5 DATE fields, multiple ALPHA/NUM generic fields. Generic service-request or shipper extended data bag. | inferred |
| ISWOTRAY | ISWOTRAY.B | 46 | IS WO Tray — keyed by TRAY_NUM(25). 53 fields: WOPRE+WOSUF (WO), OPER, OPDESC(30), CODE(15), SQTY/COMQTY/SCRPQTY. Shop-floor tray/container tracking: which production tray is at which WO operation, with scheduled/completed/scrap qty. | confirmed |
| ISLOCCST | ISLOCCST.B | 17 | IS Location Cost — keyed by PART(15)+LOC(10). 7 fields: AVGC (avg cost), BOOKVAL, LDATE/LTIME (last updated), EXTRA(150). Per-item-per-location average cost and book value for multi-location costing. | confirmed |
| BKCMHCOD | BKCMHCOD.B | 16 | CM History Code — keyed by HCODE(2). 9 fields: DESC(25), WINDW, RATE, UM(3), ABILL (billable flag), BPART/NPART/FPART (base/next/final part#). Billable service/labor rate codes with associated part numbers. | inferred |
| BKCMACCC | BKCMACCC.B | 20 | CM Account Cost Center — keyed by CCODE(5). 2 fields: DESC(25). Simple cost center code + description lookup table. | confirmed |

---

*Last updated: 2026-06-17 — built from menu_to_form.csv, master_index.csv, tables.txt,
schema.md, SRC analysis, catalog.md, and rwn_symbols.json DB fingerprint passes 1–18. Confidence varies by section — see EVO-DECOMPILE-TODO.md.*
