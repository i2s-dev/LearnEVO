# Java Integration via `EvoPVT.jar`

Status: verified (from extracted `EvoPVT.jar` classes + strings).

## The tool

`C:\ISTS\EvoPVT.jar` — 1.8 MB JavaFX application. Jar manifest:

```
Manifest-Version: 1.0
Main-Class: com.evoerp.TASKS.sql.Main$WindowsUtils
Class-Path: .
```

Packaged classes are organized as:

```
com.evoerp
├── Evo                             // JavaFX Application class
├── EvoException
├── TASKS.sql.Main                  // entry-point shell
├── TASKS.sql.PervasiveDatabase     // DB connection wrapper
├── javafx.{EvoApp, SplashScreen, TabularView, CalendarView, …}
├── help.EvoHelp
├── localization.Localization
├── log.{DialogHandler, EvoFormatter}
├── mail                            // SMTP sender
├── res
├── sql                             // SQL clause builders (Field, Clause, …)
└── util.{CsvConverter, FileUtils, WinRegistry, Tabular, …}

com.pervasive.jdbc                   // Pervasive/Actian JDBC driver
org.apache.commons.{codec, logging}
```

## Primary role — SQL over Pervasive, for TAS programs

`com.evoerp.TASKS.sql.PervasiveDatabase` establishes a JDBC connection
through `com.pervasive.jdbc.v2.ConnectionPoolDataSource`, pointed at
the EVO company database.

## Integration pattern — the `ISJAVA` task queue

Extracted bytecode string reveals this SQL fragment:

```
INSERT INTO ISJAVA (IS_JAVA_UID, IS_JAVA_DATE, IS_JAVA_PARAM_ ... ) VALUES (?, ?, ...)
```

`ISJAVA` is a **dispatch table**: the Java side writes parameter rows
for a job, and the TAS programs (or the scheduler) pick them up.

The pattern is:

1. A TAS program (or scheduled job) needs a piece of work done that is
   easier to do in Java (e.g. CSV export, Excel write, HTTP/SMTP).
2. TAS calls out to `EvoPVT.jar` (directly via
   `EXEC_TOP_WAIT "java -jar ...\EvoPVT.jar <task> <args>"`, or
   implicitly via the scheduler).
3. EvoPVT writes an **audit row** into `ISJAVA` with a UID, timestamp,
   and the per-parameter columns.
4. The TAS program correlates on the UID to see the result.

Consequence: **`ISJAVA` is the audit trail for every Java-initiated
action against the database**. If someone is hunting for "what did
EvoPVT do to my data", that's where to look.

## JavaFX UI capabilities included

`EvoApp` gives this jar a full JavaFX UI when invoked interactively:

- `SplashScreen` — startup splash.
- `TabularView` (+ `ExportTask`) — grid view with CSV export.
- `CalendarView` / `CalendarCell` — calendar widget.
- `LookupPane` / `LookupTableView` — database lookups (identical
  purpose to the TAS `F2 Lookup` but in Java).
- `ConfirmDialog`, `MessageDialog`, `AboutWindow`, `EvoHelp` — basic
  dialog infra.
- `ProgressSwitchLabel` / `ProgressSwitchList` / `ProgressSwitchTable`
  — progress-indicator widgets wrapping long `ExecuteTask` and
  `WaitTask` runs.

So: the same jar is both a **library** used by TAS out-calls AND a
stand-alone utility a user can run.

## Data-access layer

Under `com.evoerp.sql` there's a hand-rolled SQL builder:

- `Expression`, `Field`, `IntegerField`, `BigDecimalField`,
  `LocalDateField`, `LocalTimeField`, `WStringField` — typed field
  wrappers.
- `Clause`, `AndClause`, `OrClause`, `BinaryClause`, `NullClause` —
  WHERE-tree nodes.
- `ConstantExpression`, `NumberConstantExpression`,
  `LocalDateConstantExpression`, `LocalTimeConstantExpression` —
  right-hand sides.
- `DistinctFieldExpression`, `AliasFieldExpression`, `AliasTable` —
  SELECT shape.
- `DatabaseWorkerService`, `ThreadLocalConnection`,
  `ConnectionClosingThreadFactory` — a small thread-per-query executor.

This is a **lightweight ORM / DSL** specifically for the EVO Pervasive
schema. Matches the **24k-field, 659-table** landscape without
requiring JPA.

## Mail + localization

Separate packages handle SMTP (`com.evoerp.mail`) and resource-bundle
localization (`com.evoerp.localization.Localization`). These are
invoked when the Java side needs to email reports or render localized
labels.

## EvoPVT.jar is a JavaFX application (Pass 106l)

Confirmed from class inventory of `samples/jar/EvoPVT.jar` (886 files):

**EvoPVT.jar is a full JavaFX GUI application**, not just a command-line tool. It contains:

| Package/Class | Role |
|--------------|------|
| `com.evoerp.javafx.EvoApp` | JavaFX Application entry point (splash + main window) |
| `com.evoerp.javafx.TabularView` | Tabular data grid — the primary report/data display |
| `com.evoerp.javafx.calendar.CalendarView` | Date picker widget |
| `com.evoerp.javafx.util.LookupPane` | Lookup/search dialog |
| `com.evoerp.javafx.SplashScreen` | Startup splash screen |
| `com.evoerp.TASKS.sql.Main` | CLI entry point (headless mode) |
| `com.evoerp.TASKS.sql.Main$WindowsUtils` | Windows registry + OS utilities |
| `com.evoerp.TASKS.sql.PervasiveDatabase` | JDBC connection manager |

**Main dispatch tasks** (confirmed from class names):
- `CsvExportTask` — export tabular data to CSV file
- `TextFileWriteTask` — write results to text file
- `FileOpenTask` — open a file from disk (Windows shell open)
- `TabularView$ExportTask` — export from grid view

When launched via `ISJAVA` (from TAS programs), EvoPVT.jar runs in headless/task mode.
When launched directly (e.g., from a user shortcut), it shows the JavaFX GUI.

## JDBC driver bundled (Pass 106l)

`EvoPVT.jar` bundles the Pervasive JDBC driver **inside the JAR itself**:
- Driver: **Pervasive JDBC 2.0 Driver**
- PSQL version: **13.20.023.000** (from `com/pervasive/jdbc/common/Version.properties`)

This means no separate JDBC driver installation is needed on client machines — the driver
ships with EvoPVT.jar. PSQL 13.x is backward-compatible with PSQL 8.x data files (the `.B`
files created by the older EvoERP runtime remain accessible).

**JDBC connection parameters — confirmed from DatabaseSettings.class (Pass 110d, 2026-06-19):**
`DatabaseSettings.class` reads a **`jdbc.ini`** text file (NOT the Windows registry as previously
hypothesized). The file is parsed line-by-line; recognized keys:

| Key | Purpose |
|-----|---------|
| `Host` | Database server hostname (e.g. `i2s109-solidcrm`) |
| `Name` | Database name (e.g. `@DBA` for Pervasive ODBC path) |
| `Port` | Port number (default Pervasive port: 1583) |
| `Company` | Default company code (e.g. `I2`) |
| `Tree Destination` | Report/BOM tree output destination path |

The `DEFAULT_FILE` constant points to `jdbc.ini`. The `WinRegistry` class is used for
other purposes (e.g., finding the Java installation path for `JAVA.PATH`), not for DB connection.

## ISJAVA table schema (confirmed from DDF + TAS named_vars, Pass 390 2026-06-30)

**CORRECTION (Pass 362 2026-06-26):** ISJAVA IS registered in the Pervasive DDF (file_id=437).
The prior "not in DDF" claim was wrong — the DDF parser filtered brackets in field names.

Confirmed DDF schema (27 fields, record = 2,054 bytes):

| TAS field name | DB column | Type | Size | Offset | Purpose |
|----------------|-----------|------|------|--------|---------|
| `IS.JAVA.UID` | `IS_JAVA_UID` | STRING | 40 | 0 | Unique task ID (PK) |
| `IS.JAVA.PARAM` | `IS_JAVA_PARAM[1..25]` | STRING | 80 each | 40–2039 | 25 parameter slots (80 chars each = up to 2,000 chars total) |
| `IS.JAVA.DATE` | `IS_JAVA_DATE` | DATE | 4 | 2040 | Queue/execution date |

Additional TAS variables (not DB columns):
- `JAVA.PATH` — path to `EvoPVT.jar` (read from ISTS.CFG or taspro7.ini)
- `JAVA.PATH2` — secondary Java path (fallback or alternate version)
- `JAVA.H` — TAS file handle for the open ISJAVA Btrieve table
- `JAVA.NAME` — Java class/program name (used by QUERYEXECUTE.RWN)

## ISJAVA two-tier usage pattern (Pass 390 2026-06-30)

Of 23 programs that open ISJAVA, two distinct access tiers exist:

**Tier A — Full queue access (9 programs, have JAVA.H + IS.JAVA.UID/PARAM/DATE):**

| Program | Module | Task type |
|---------|--------|-----------|
| `EVOERPMENU.RWN` | Menu | Queue monitor — polls ISJAVA, dispatches to EvoPVT.jar |
| `T7AUTOFX.RWN` | System | FX rate fetch daemon (queues Oanda API calls) |
| `T7MDEFAULTS.RWN` | System | System defaults (config update notifications) |
| `T7SOA.RWN` | SO | Sales order entry — queues SO confirmation emails |
| `T7SOE.RWN` | SO | SO release/ship — queues shipping notifications |
| `T7SOGA.RWN` | SO | SO invoice posting — queues invoice emails |
| `T7SOR.RWN` | SO | SO returns — queues return/RMA notifications |

**Tier B — Path-only reference (14 programs, have JAVA.PATH/PATH2 only):**
These programs only reference the Java path (T7MRA/B/C/E MRP suite, T7SOH/SOLOT/SOLINFO, T7SOGCOGS, T7SOHINFO/SOINFO/SOJ/SOK/MEMO2ALPHA, T7MHOPE/MLC) — they check Java availability or display Java-related info but do not queue tasks themselves.

**T7jsql.RWN** (SQL bridge, 52 procs) has `JAVA.PATH + JAVA.PATH2` only — it calls Java directly rather than using the ISJAVA queue.  
**QUERYEXECUTE.RWN** (26 procs) has `JAVA.PATH + JAVA.NAME` — interactive query launcher.

## ISJOB — separate job/project tracking table (Pass 390 2026-06-30)

`ISJOB` is entirely distinct from `ISJAVA`. It is a job/project cross-reference table used to link transactions to job numbers.

DDF schema (9 fields, record = 175 bytes, file_id=416, location=ISJOB.B):

| Field | Type | Size | Purpose |
|-------|------|------|---------|
| `IS_JOB_NUMB` | STRING | 15 | Job number (primary key) |
| `IS_JOB_DESC` | STRING | 30 | Job description |
| `IS_JOB_CUST` | STRING | 10 | Customer code link |
| `IS_JOB_VEND` | STRING | 10 | Vendor code link |
| `IS_JOB_RSVD` | STRING | 1 | Reserved |
| `IS_JOB_STATUS` | STRING | 1 | Status code |
| `IS_JOB_OPENDT` | DATE | 4 | Open date |
| `IS_JOB_CLOSEDT` | DATE | 4 | Close date |
| `IS_JOB_EXTRA` | STRING | 100 | Extra data |

TAS namespace: `IS.JOB.*` (9 vars matching the DDF fields).  
Primary editor: `T7SMPF.RWN` (SM module, 64 procs, 1,292 vars — also opens JOB.H handle).  
Enable flag: `ISTS.CFG.JOB`; config variants: `ISTS.CFG.JOBDEC`, `ISTS.CFG.JOBCUS`.  
Accessed by 15 programs: SO (T7SOA/SOPK), AP (T7APB), AR (T7ARB), GL (T7GLB), PO (T7POA/TPOA),
WO (T7WOA/OLD), SA (T7SAA), MRP (T7MRIX), and J7* customizations.

## EVOReports network share (Pass 390 2026-06-30)

`\\i2s109-solidcrm\EVOReports\` is **not** a systematic print-to-file output folder.
Actual contents: ad-hoc SQL queries (.sql), CSV exports (.csv), screenshot PNGs, an empty subfolder.
Files are irregularly dated (2015–2023) and user-created. Purpose: informal workspace for sharing
queries and data extracts across users.  Print-to-file report output goes elsewhere (PDFs likely
stored per-user or per-workstation, not on this share).

## Resolved open questions (Pass 106l)

- EvoPVT.jar sub-tasks: CsvExportTask + TextFileWriteTask + FileOpenTask + TabularView.ExportTask ✅
- JDBC driver source: PSQL 13.20 bundled in JAR (no external driver needed) ✅
- PSQL version: 13.20.023.000 (backward-compatible with 8.x .B files) ✅

## Resolved open questions (Pass 110d, 2026-06-19)

- Java connection parameters source: **`jdbc.ini`** text file (not Windows registry) ✅
- ISJAVA table schema: IS_JAVA_UID + IS_JAVA_DATE + IS_JAVA_PARAM[1..25] ✅

## ISJAVA live data analysis (Pass 412, 2026-06-30)

Live ISJAVA records queried via ODBC (DSN=DBA). Results:

**Record count:** 1,774 records spanning 2021-12-10 to 2025-02-03.
Records are **retained permanently** — this is an audit log, not a cleared queue.

**PARAM_1 distribution** (only parameter actually used — PARAM_2..25 are all empty):

| PARAM_1 | Count | Likely task type |
|---------|------:|-----------------|
| `1` | 1,407 | Most common SA analysis (likely SalesRepSummary) |
| `2` | 345 | Second SA analysis type (likely ProfitByInvoice) |
| `3` | 14 | Rare SA type (ItemClass?) |
| `0` | 5 | Internal/cleanup sentinel (UID=`-i`) |
| `4` | 2 | Very rare (CustomerClass?) |
| `5` | 1 | Very rare (MultiYearSales?) |

**UID format:** `<USERNAME><HHMMSS><A|P><YYYYMMDD>`
- `USERNAME` = EvoERP user code (up to ~10 chars)
- `HHMMSS` = time in 12-hour HH:MM:SS format
- `A` or `P` = AM or PM
- `YYYYMMDD` = date

Examples:
- `BSCHIBI010308P20240523` = user BSCHIBI, 1:03:08 PM, 2024-05-23
- `ASTEMPIEN015256P20230403` = user ASTEMPIEN, 1:52:56 PM, 2023-04-03
- `-i` = internal record (startup/cleanup sentinel written by EvoPVT.jar itself)

**Top 5 users by task count:**
DFRENETTE(201), BSCHIBI(189), STEVESP(176), JCHARETTE(171), RONEILL(160)

**Key insight:** Since PARAM_2..25 are always empty, each Java task submission uses
only `PARAM_1` as the task type discriminator. EvoPVT.jar reads `PARAM_1` and dispatches
to the appropriate SA JAR. The task type → JAR mapping (1=SalesRepSummary, 2=ProfitByInvoice,
3=ItemClass, 4=CustomerClass, 5=MultiYearSales) is confirmed by the JAR inventory but
the exact number-to-JAR assignment requires reading the TAS program that writes `PARAM_1`.

## Resolved open questions (Pass 390 2026-06-30)

- ISJAVA IS in DDF (file_id=437) — prior "not in DDF" was wrong ✅
- ISJAVA schema: 27 fields — UID (40) + 25×PARAM (80 each) + DATE (4) ✅
- Two-tier TAS access: 9 programs queue tasks (JAVA.H + IS.JAVA.*), 14 programs path-only ✅
- ISJOB = separate job/project table (9f, file_id=416, T7SMPF primary editor) ✅
- EVOReports folder = informal user workspace, not print-to-file output ✅

## Resolved open questions (Pass 412, 2026-06-30)

- ISJAVA has 1,774 live records (permanent audit log, not a cleared queue) ✅
- UID format: `<USER><HHMMSS><A|P><YYYYMMDD>` (12-hour AM/PM encoded) ✅
- PARAM_1 = task type (1-5); PARAM_2..25 always empty in this installation ✅
- 5 internal `-i` records with PARAM_1=`0` = EvoPVT.jar startup sentinel ✅
