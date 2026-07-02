# EX — SQL Export / Business Intelligence Export (SQLEXPORT.RWN)

Status: verified | Pass 556 2026-07-02

Sources: variable extraction from `samples/rwn_decrypted/SQLEXPORT.RWN.dec` +
DFM read from Pass 156 + SQLExport.jar class string analysis (Pass 556) +
EvoPVT.jar class file analysis from Pass 315 + JDBC.INI read (Pass 556) +
all 19 DefaultSQL query files read (Pass 556).

---

## Overview

`SQLEXPORT.RWN` is the **EX module** launcher — a **TAS Pro 7 → Java bridge** that
starts the `SQLExport.jar` Java Swing application. The TAS component contains no
business logic; it passes session parameters to the Java app and exits.

- **Module code:** EX (SQL Export)
- **Program:** SQLEXPORT.RWN (23 procs, 709 vars)
- **DFM:** T7JTemp template (Caption: "Loading....") — generic Java loader; no EX-specific UI
- **Java application:** `SQLExport.jar` (`com.evoerp.*`, v1.8.6 build 2021-09-11)
- **Architecture pattern:** identical to QUERYEXECUTE, CASHFLOW, CRMDASHBOARD,
  COMMISSIONRPT, PURCHITEM, PURCHVEND, VSCHED (7 confirmed Java bridges)

---

## What It Does

1. TAS Pro opens SQLEXPORT.RWN, displays "Loading...." dialog
2. Passes session parameters (HOST/NAME/PORT/COMP/JAVA.PATH/JAVA.NAME) to JVM
3. Java app `SQLExport.jar` launches — full Swing UI with SQL query editor
4. User selects a query from the **Default Queries** menu (loaded from `DefaultSQL\` directory) or writes ad-hoc SQL
5. Export runs; results written as CSV to the `Tree Destination` for the active company code
6. **Company code** (COMP var) selects which Pervasive database to query (see `jdbc.ini` section below)

The `DefaultSQL\` queries all target **operational EvoERP tables** in the main `abi` database — they query
BKARHINV, BKICMSTR, BKGLTRAN, WOBOM, BKAPHPO, etc. directly. EVOBI2 is an additional reporting database
available via the BI2 company code; it is not required by the DefaultSQL queries.

---

## Java Bridge Var Block (vars[60–71])

These 12 vars follow immediately after the LISTG60.LIB TEMP0–TEMP59 scratch block.
Same structure in every Java bridge program:

| Var | Meaning |
|-----|---------|
| `HOST` | Java server hostname |
| `NAME` | Java application name / service name |
| `PORT` | Java service port |
| `TREEDEST` | Tree destination code |
| `COMP` | Company code (passed to Java app) |
| `NOPE` | Unused/placeholder flag |
| `DUMMY_L` | Dummy local variable |
| `DFM` | DFM form name to display during loading |
| `RVAL` | Return value from Java app |
| `ISTS.EDATE` | EvoERP session end date |
| `JAVA.PATH` | Full filesystem path to `.jar` file |
| `JAVA.NAME` | Main class name within the JAR |

---

## Workstation Config Var Block (vars[72–87])

Immediately after the Java bridge vars — standard workstation settings from
EVO.CFG.* namespace (same 18-var block as t7slsfc.RWN):

| Var | Meaning |
|-----|---------|
| `TOOLBAR` | Toolbar visible flag |
| `OLWOA` | WO-A online flag |
| `OLPOA` | PO-A online flag |
| `OLINA` | IN-A online flag |
| `OLINB` | IN-B online flag |
| `OLSOA` | SO-A online flag |
| `OLARA` | AR-A online flag |
| `OLAPA` | AP-A online flag |
| `LANG` | UI language code |
| `SOUNDS` | Sound effects flag |
| `REMIND` | Reminder flag |
| `EREMIND` | Email reminder flag |
| `REMSEC` | Reminder seconds |
| `RSNOOZE` | Reminder snooze interval |
| `QPRINT` | Quick print flag |

---

## Per-Module Screen Config Vars

After the workstation block, SQLEXPORT.RWN carries per-module screen selector vars
(same pattern as QUERYEXECUTE, used to route to the correct sub-module screen):

| Var | Meaning |
|-----|---------|
| `ARA.SAVE` | AR-A save flag |
| `APA.SAVE` | AP-A save flag |
| `DEFPRINTPATH` | Default printer path |
| `ARA.CFG.ECSCRN` | AR-A EC screen selector |
| `ARA.CFG.CVTSCRN` | AR-A convert screen selector |
| `APA.CFG.ECSCRN` | AP-A EC screen selector |
| `APA.CFG.CVTSCRN` | AP-A convert screen selector |
| `INA.CFG.ECSCRN` | IN-A EC screen selector |
| `INB.CFG.ECSCRN` | IN-B EC screen selector |
| `POA.CFG.ECSCRN` | PO-A EC screen selector |
| `SOA.CFG.ECSCRN` | SO-A EC screen selector |
| `WOA.CFG.ECSCRN` | WO-A EC screen selector |
| `WOA.CFG.CVTSCRN` | WO-A convert screen selector |

---

## Java Application Details (Pass 556 class analysis)

**SQLExport.jar** (`com.evoerp.sqlexport.*`, v1.8.6):

| Class | Purpose |
|-------|---------|
| `com.evoerp.sqlexport.ui.QueryFrame` | Main window — query editor (JEditorPane, text/sql), toolbar (New/Execute/Export), Default Queries menu |
| `QueryFrame$QueryWorker` | Background SwingWorker that executes SQL via `Database.executeQuery()` |
| `QueryFrame$DirectExportWorker` | Background SwingWorker for direct-to-CSV export |
| `QueryFrame$StoredQueryLoader` | Loads `StoredQuery` objects from DefaultSQL .sql files for the menu |
| `com.evoerp.sqlexport.sql.Database` | Wraps a `PervasiveDatabase` connection; executes queries; saves/loads from ISQRYSQL/ISVARSQL |
| `com.evoerp.sqlexport.sql.StoredQuery` | Holds one .sql file's text; `loadFromFile(File)` reads from disk |
| `com.evoerp.sqlexport.sql.Permission` | SELECT permission type; `check()` enforces read-only access |
| `com.evoerp.sqlexport.ui.QueryResultFrame` | Displays result set; supports CSV export with "Format for Excel" checkbox |

**JDBC.INI** (`\\I2S109-SOLIDCRM\DBAMFG$\JDBC.INI`, copied to `samples/jar/JDBC.INI`):

```ini
[BAB]          ; Main production company
Host=i2s109-solidcrm
Port=1583
Name=abi                              ; operational DBAMFG$ database
Tree Destination=\\I2S109-SOLIDCRM\EVOREPORTS\

[BI2]          ; BI/reporting company
Host=I2S109-SOLIDCRM
Port=1583
Name=EVOBI2                           ; separate BI reporting database
Tree Destination=\\I2S109-SOLIDCRM\DBAMFG$\REPORTS

[B22]          ; Second company (testing / alternate)
Host=i2s109-solidcrm
Port=1583
Name=evob22
Tree Destination=\\I2S109-SOLIDCRM\EVOREPORTS\

[BAT]          ; Batch processing company
Host=I2S109-SOLIDCRM
Port=1583
Name=EVOBAT
Tree Destination=\\I2S109-SOLIDCRM\DBAMFG$\REPORTS
```

All four databases share the same Pervasive PSQL server on port 1583.
`DatabaseSettings` reads this file; TAS passes the `COMP` var to select the section.

**Output:**
- Path: `Tree Destination` from jdbc.ini for the active company code
  - BAB: `\\I2S109-SOLIDCRM\EVOREPORTS\`
  - BI2/BAT: `\\I2S109-SOLIDCRM\DBAMFG$\REPORTS\`
- Format: CSV; "Format for Excel" option adds Excel-compatible quoting
- Log: `\\I2S109-SOLIDCRM\DBAMFG$\logs\SQL Export.log`

**Saved Queries** — two additional tables in the database store user-saved queries:

| Table | Columns | Purpose |
|-------|---------|---------|
| `ISQRYSQL` | `IS_QRY_NAME`, `IS_QRY_QUERY` | Named saved SQL queries (full query text) |
| `ISVARSQL` | `IS_VAR_QNAME`, `IS_VAR_TYPE`, `IS_VAR_VNAME`, `IS_VAR_ORDER` | Variable definitions for parameterized queries |

**Variable Query Wizard** — "Variable Query Wizard" menu item uses `com.evoerp.sql.wizard.QueryConstructor`
(shared with EvoPVT Query builder) to build parameterized queries. Variables are saved to ISVARSQL.

**Known bug (historical):** path separators in filenames (e.g., `7\18 thru 8-4.csv`) cause
`FileNotFoundException` — the backslash is treated as a path separator.

---

## Java Bridge Architecture (confirmed across 8 programs)

All EvoERP Java bridges share the same TAS-side var pattern at offset vars[60]:
`HOST / NAME / PORT / TREEDEST / COMP / NOPE / DUMMY_L / DFM / RVAL / ISTS.EDATE / JAVA.PATH / JAVA.NAME`

Confirmed programs: SQLEXPORT, QUERYEXECUTE, CASHFLOW, CRMDASHBOARD, COMMISSIONRPT,
PURCHITEM, PURCHVEND, VSCHED. Each uses a different `.jar` and class name in
`JAVA.PATH` / `JAVA.NAME`.

---

## DefaultSQL Query Catalog (Pass 556 — all 19 queries read)

Copied from `\\I2S109-SOLIDCRM\DBAMFG$\DefaultSQL\` → `samples/jar/DefaultSQL/`.
All queries target the main `abi` production database (company BAB).

| File | Purpose | Key Tables |
|------|---------|-----------|
| `ACH Vendor.sql` | List vendors with ACH flag | BKAPVEND + ISAPEX (ISAPEX_FLAG_1) |
| `AP Count.sql` | Count AP GL txns by entry date | BKGLTRAN (type RP, acct 2110) |
| `AP Daily Invoicing.sql` | Count AP invoices by posting date | BKAPINVT (type I) |
| `Closed WO.sql` | Closed WOs with under-issued BOM components | WOBOM + WORKORD + ISWOEX + BKICMSTR |
| `EandO.sql` | Excess-and-obsolete inventory analysis | BKICMSTR + INVTXN + MTICMSTR |
| `GL no Inv Txn.sql` | GL txns to inventory account with no matching INVTXN | BKGLTRAN + INVTXN (date in MTIT_EXTRA) |
| `Inventory Non Asset.sql` | Inventory items posting to non-Asset GL accounts | BKGLCOA + BKICMSTR + CLASS |
| `Inventory txn no GL Post.sql` | INVTXN entries with no matching GL transaction | INVTXN + BKGLTRAN |
| `Non-Inventory Asset.sql` | Non-tangible items posting to Asset GL accounts | BKGLCOA + BKICMSTR + CLASS |
| `overstock.sql` | Inventory items with excess available qty × avg cost | BKICMSTR + MTICMSTR |
| `Released WO.sql` | Released WOs with under-issued BOM components | WOBOM + WORKORD + ISWOEX |
| `RNI.sql` | Received-not-invoiced PO lines (rqty>0, no invoice) | BKAPHPO + BKAPHPOL |
| `RNI Invoiced.sql` | GL RNI/Invoiced txns with no matching AP PO receiver | BKGLTRAN + BKAPHPOL + BKAPHPO |
| `RNI Received.sql` | GL Received/Not-Invoiced txns with no matching PO receiver | BKGLTRAN + BKAPHPOL |
| `RNI-INVOICED.SQL` | AP invoices flagged as RNI (BKAP_INVT_EXTRA[49]=R) | BKAPINVT |
| `Royalty.sql` | Sales invoices with royalty field | BKARHINV + BKARHIVL + BKICMSTR + MTICMSTR |
| `SALES.sql` | Sales invoice line items with ASD date | BKARHINV + BKARHIVL |
| `Shipping Info.sql` | Full BKARHINV record dump (all columns) | BKARHINV |
| `VoucherPO.sql` | AP vouchers for PO vendors | BKAPHPO + BKAPINVL |

**New table relationships confirmed from these queries:**

| Table | Key Fields Found | Notes |
|-------|----------------|-------|
| `ISAPEX` | `ISAPEX_VEND` → BKAPVEND PK, `ISAPEX_FLAG_1` | AP extension; ISAPEX_FLAG_1=ACH enabled flag |
| `ISWOEX` | `IS_WOEX_WOPRE`, `IS_WOEX_WOSUF` → WORKORD PK, `IS_WOEX_CDATE` | WO extension table |
| `CLASS` | `MTCLASS_CLASS` → BKICMSTR.BKIC_PROD_CLASS, `CLASS_GLA` = GL account | Item class → GL account mapping |
| `MTICMSTR` | `MTIC_PROD_CODE` FK→ BKICMSTR, `MTIC_PROD_AVAIL`, `MTIC_PROD_UOA`, `MTIC_PROD_UOWO`, `MTIC_PROD_VEND_1`, `MTIC_PROD_SPECS_5` | MT-prefixed inventory extension |

**INVTXN.MTIT_EXTRA date encoding** (confirmed from GL no Inv Txn.sql):
- `SUBSTRING(MTIT_EXTRA, 26, 2)` = month (MM)
- `SUBSTRING(MTIT_EXTRA, 29, 2)` = day (DD)
- `SUBSTRING(MTIT_EXTRA, 32, 2)` = year (YY, prepend '20')

**INVTXN.MTIT_TYPE codes** (confirmed from GL no Inv Txn):
A=adjustment, P=PO receipt, S=sale/shipment, I=WO issue, W=WO completion, Q=?, M=?, T=transfer, C=?, R=return, J=journal, O=?

**BKGLTRAN.BKGL_TRN_DESC values** (confirmed from RNI queries):
- `'RECEIVED/NOT INVOICED'` — PO receiving (PO-C) posts
- `'RNI/INVOICED'` — PO invoicing (AP-C) posts

---

## EvoPVT.jar — Shared Java Library (Pass 315 analysis)

**EvoPVT.jar** (`samples/jar/EvoPVT.jar`) is the shared framework library used by all EvoERP Java bridge programs
(SQLExport, CASHFLOW, CRMDASHBOARD, COMMISSIONRPT, PURCHITEM, PURCHVEND, VSCHED, etc.).
It provides the infrastructure SQLExport.jar builds on:

### SQL Framework (`com.evoerp.sql.*`)

| Class | Purpose |
|-------|---------|
| `PervasiveDatabase` | Pervasive JDBC v2 connection pool; instance-per-company-code |
| `DatabaseSettings` | Reads `jdbc.ini` config; maps company → host/port/name/reportDest |
| `Query` | SQL query builder (SELECT + FROM + WHERE clauses) |
| `Field` / `AliasFieldExpression` / `DistinctFieldExpression` | Column expression types |
| `BinaryClause` / `AndClause` / `OrClause` / `NullClause` | WHERE clause builders |
| `ShopCalendar` | Shop-day calendar loaded from CALENDAR table; supports holidays, moveDate, shopDaysBetween |

**Two hardcoded SQL queries** in `PervasiveDatabase.class`:
```sql
SELECT MTCAL_DATE FROM CALENDAR WHERE MTCAL_DATE IS NOT NULL
-- used by getShopCalendar() to load holiday dates

SELECT IS_SHIP_WEB_2 FROM ISSHIPCO WHERE IS_SHIP_SHIPVIA = ?
-- used by getTrackingUrl(shipVia, trackingNumber): %%TRACK%% placeholder replaced with tracking#
```

### jdbc.ini Config Format

`DatabaseSettings.class` reads `\\I2S109-SOLIDCRM\DBAMFG$\JDBC.INI`. Format — INI-style,
line-by-line scanner with `startsWith` checks. Each section starts with `[COMPANY_CODE]`:

```ini
[CODE]
Host=<hostname>
Port=<port_number>
Name=<pervasive_database_name>
Tree Destination=<UNC_path_for_report_output>
```

Keys are: `Host`, `Port`, `Name`, `Tree Destination` (= `REPORT_DEST_KEY`).
`DatabaseSettings.getDefault()` returns the instance for `defaultCompanyCode`.
TAS passes the current `COMP` var to select the correct section at runtime via `getInstance(companyCode)`.
The `INSTANCE_MAP` caches instances keyed by company code.

### UI Framework (`com.evoerp.javafx.*`)

| Class | Feature |
|-------|---------|
| `TabularView` | Main grid/table display; supports Export to CSV, Format for Excel, Create Chart |
| `CsvExportTask` | Background CSV export task |
| `DateRangePrompt` | Date range input dialog (used by reports with from/thru date filters) |
| `LookupPane` | F2-style lookup popup |
| `MessageDialog` / `ConfirmDialog` | Standard OK/Cancel dialogs |
| `CalendarView` | Date picker calendar |

### Other (`com.evoerp.*`)

| Class | Purpose |
|-------|---------|
| `Localization` | XML-based string localization; reads `*.xml` files from a `localization/` directory |
| `Email` / `SmtpClient` | Email client (mirrors EvoERP email config) |
| `WinRegistry` | Windows registry access (reads Java path for `JAVA.EXE` lookup) |
| `CsvConverter` | CSV encoding utility |
| `SingleInstanceService` | Prevents duplicate app instances |

### Multi-Company Architecture

`DatabaseSettings` supports multiple company codes via `INSTANCE_MAP` (company→settings) and
a `defaultCompanyCode`. Each company code maps to its own Pervasive DBMS connection. The active
company is passed from TAS via the `COMP` var in the Java bridge vars block.

---

## Use Cases

- "How do I export EvoERP data to Excel/CSV?" → EX module → SQL Export — select from Default Queries
  menu or write ad-hoc SQL; results export to CSV on the network share. "Format for Excel" option
  adds Excel-compatible quoting.
- The Default Queries target the main `abi` operational database. EVOBI2 (company BI2) is a
  separate BI reporting database accessible by switching company code.
- Shop calendar integration: `PervasiveDatabase.getShopCalendar()` queries `CALENDAR.MTCAL_DATE`
  to load holiday dates for date calculations in reports.
- Shipping tracking: `PervasiveDatabase.getTrackingUrl()` queries `ISSHIPCO.IS_SHIP_WEB_2`
  for the carrier's tracking URL template, substituting `%%TRACK%%` with the tracking number.
- Saved queries (Variable Query Wizard): queries with parameters are built via the wizard,
  stored in `ISQRYSQL` (query text) and `ISVARSQL` (variable definitions).

---

## Remaining Gap

EVOBI2 database DDF schema not extracted — the internal table structure of the BI reporting
database is unknown. EVOBAT and evob22 databases also undocumented.

**Confidence: 93/100** — TAS-side var block fully confirmed; Java app fully analyzed
(QueryFrame/Database/StoredQuery/Permission all class-string-extracted, Pass 556); JDBC.INI
read (4 companies: BAB=abi, BI2=EVOBI2, B22=evob22, BAT=EVOBAT); all 19 DefaultSQL queries
read with tables and field references documented. Remaining gap: EVOBI2/evob22/EVOBAT database
schemas not extracted. — **C: 93/100**
