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

## ISJAVA table schema (confirmed from bytecode + TAS named_vars, Pass 110d, 2026-06-19)

ISJAVA is a **TAS runtime-only table** (not registered in the Pervasive DDF). It serves as the
task-queue and audit trail for all Java-initiated database operations.

| TAS field name | DB column | Type | Purpose |
|----------------|-----------|------|---------|
| `IS.JAVA.UID` | `IS_JAVA_UID` | STRING | Unique task ID (PK) — correlation key between TAS call and Java result |
| `IS.JAVA.DATE` | `IS_JAVA_DATE` | DATE | Task execution date |
| `IS.JAVA.PARAM` | `IS_JAVA_PARAM_1`, `IS_JAVA_PARAM_2`, … | STRING (×N) | Command-line parameters passed to EvoPVT.jar (array; column count = max args) |

Additional TAS variables (not DB columns):
- `JAVA.PATH` — path to `EvoPVT.jar` (from config or taspro7.ini)
- `JAVA.H` — TAS file handle for the ISJAVA Btrieve table

The INSERT is built dynamically: `INSERT INTO ISJAVA (IS_JAVA_UID, IS_JAVA_DATE, IS_JAVA_PARAM_1, IS_JAVA_PARAM_2, ...) VALUES (?, ?, ?, ?, ...)`
The count of PARAM columns equals the number of args the calling TAS program passes.

## Resolved open questions (Pass 106l)

- EvoPVT.jar sub-tasks: CsvExportTask + TextFileWriteTask + FileOpenTask + TabularView.ExportTask ✅
- JDBC driver source: PSQL 13.20 bundled in JAR (no external driver needed) ✅
- PSQL version: 13.20.023.000 (backward-compatible with 8.x .B files) ✅

## Resolved open questions (Pass 110d, 2026-06-19)

- Java connection parameters source: **`jdbc.ini`** text file (not Windows registry) ✅
- ISJAVA table schema: IS_JAVA_UID + IS_JAVA_DATE + IS_JAVA_PARAM_N (dynamic N) ✅
- ISJAVA is TAS runtime-only (not in Pervasive DDF) ✅
