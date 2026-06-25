# EX — SQL Export / Business Intelligence Export (SQLEXPORT.RWN)

Status: verified | Pass 315 2026-06-25

Sources: variable extraction from `samples/rwn_decrypted/SQLEXPORT.RWN.dec` +
DFM read from Pass 156 + SQLExport.jar analysis from Pass 156 +
EvoPVT.jar class file analysis from Pass 315.

---

## Overview

`SQLEXPORT.RWN` is the **EX module** launcher — a **TAS Pro 7 → Java bridge** that
starts the `SQLExport.jar` Java Swing application. The TAS component contains no
business logic; it passes session parameters to the Java app and exits.

- **Module code:** EX (SQL Export)
- **Program:** SQLEXPORT.RWN (23 procs, 709 vars)
- **DFM:** T7JTemp template (Caption: "Loading....") — generic Java loader; no EX-specific UI
- **Java application:** `SQLExport.jar` (`com.evoerp.*`, v1.5.0 build 2014-03-19)
- **Architecture pattern:** identical to QUERYEXECUTE, CASHFLOW, CRMDASHBOARD,
  COMMISSIONRPT, PURCHITEM, PURCHVEND, VSCHED (7 confirmed Java bridges)

---

## What It Does

1. TAS Pro opens SQLEXPORT.RWN, displays "Loading...." dialog
2. Passes session parameters (HOST/NAME/PORT/COMP/JAVA.PATH/JAVA.NAME) to JVM
3. Java app `SQLExport.jar` launches — full Swing UI with SQL query selection
4. User selects a predefined SQL query against **EVOBI2** (separate BI database, NOT DBAMFG$)
5. Export runs via `TextExportingWorker`; results written to `\\I2S109-SOLIDCRM\DBAMFG$\REPORTS\` as CSV

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

## Java Application Details (from Pass 156)

**SQLExport.jar** (`com.evoerp.*`):

| Class | Purpose |
|-------|---------|
| `com.evoerp.sql.PervasiveDatabase` | Pervasive JDBC v2 connection manager |
| `com.evoerp.ui.util.TextExportingWorker` | CSV export Swing background task |
| `com.evoerp.ui.util.FileOpeningWorker` | File open/save dialog worker |

**Database connection:**
- Target: **EVOBI2** (separate BI database — NOT operational DBAMFG$)
- Host: i2s109-solidcrm, Port: 1583
- The EVOBI2 schema contains views or denormalized tables for reporting

**Output:**
- Path: `\\I2S109-SOLIDCRM\DBAMFG$\REPORTS\` (historical: `\\I2S109-SOLIDCRM\EVOREPORTS\`)
- Format: CSV
- Log: `\\I2S109-SOLIDCRM\DBAMFG$\logs\SQL Export.log`

**Known bug:** path separators in filenames (e.g., `7\18 thru 8-4.csv`) cause
`FileNotFoundException` — the backslash is treated as a path separator.

---

## Java Bridge Architecture (confirmed across 8 programs)

All EvoERP Java bridges share the same TAS-side var pattern at offset vars[60]:
`HOST / NAME / PORT / TREEDEST / COMP / NOPE / DUMMY_L / DFM / RVAL / ISTS.EDATE / JAVA.PATH / JAVA.NAME`

Confirmed programs: SQLEXPORT, QUERYEXECUTE, CASHFLOW, CRMDASHBOARD, COMMISSIONRPT,
PURCHITEM, PURCHVEND, VSCHED. Each uses a different `.jar` and class name in
`JAVA.PATH` / `JAVA.NAME`.

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

The `DatabaseSettings.class` reads `jdbc.ini` from the local `auto/` directory (path `auto\EvoSettings.ini`
in TAS var, but the Java side uses `jdbc.ini`). File format — line-by-line scanner, section-based:

```
Company <code>
Host    <hostname>
Port    <port>
Name    <database_name>
Tree Destination <code>
Report Destination <folder>
```

One `Company` block per company. `defaultCompanyCode` sets the fallback.
TAS passes the current `COMP` var to select the correct section at runtime.

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

- "How do I export EvoERP data to Excel/CSV?" → EX module → SQL Export — runs
  predefined SQL against EVOBI2, exports results to CSV on the network share.
- The EVOBI2 database is a reporting/BI database separate from the operational tables.
  SQL Export lets users run these queries and download results without ERP access.
- Shop calendar integration: the Java app uses PervasiveDatabase.getShopCalendar()
  which queries the CALENDAR table (MTCAL_DATE field) to load holiday dates for
  date calculations in reports.
- Shipping tracking: PervasiveDatabase.getTrackingUrl() queries ISSHIPCO.IS_SHIP_WEB_2
  for the carrier's tracking URL template, substituting %%TRACK%% with the tracking number.

---

## Remaining Gap (blocked)

The specific SQL queries for each EX export report are defined in `SQLExport.jar` (not in EvoPVT.jar).
That JAR is not present locally and is not decompilable without it. The EVOBI2 database schema
is also inaccessible (separate Pervasive server, DDFs not extracted). These two items cap the
confidence ceiling at approximately 85/100.

**Confidence: 85/100** — TAS-side var block fully confirmed; Java bridge architecture fully
mapped; EvoPVT.jar framework classes analyzed (Pass 315): JDBC.ini format, SQL query builder
framework, ShopCalendar/tracking SQL, multi-company architecture, UI framework all confirmed.
Remaining gap: specific EX export query set and EVOBI2 schema are in SQLExport.jar (not locally available).
