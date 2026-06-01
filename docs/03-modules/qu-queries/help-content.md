# QU — Queries & Reports

Status: verified (text distilled from the vendor's help file).

*Source: EvoHELP.CHM → Queries & Reports (7 CHM topics).*
*Extracted HTML in [samples/chm/extracted/](../../../samples/chm/extracted/).*

The Queries & Reports menu provides cross-module inquiry tools, calendar-based
order activity views, a financial snapshot dashboard, standalone grid lookups,
and an SQL query execution facility. Because the information these tools surface
spans many different data files simultaneously, the programs do not belong to any
single module and are collected here under the QU prefix.

---

## Contents

- [QU-A — Master Inquiry](#qu-a--master-inquiry)
- [QU-B — Calendar Drill Down](#qu-b--calendar-drill-down)
- [QU-C — Calendar Summary Report](#qu-c--calendar-summary-report)
- [QU-D — Business Status](#qu-d--business-status)
- [QU-E — Quick Grid Lookup](#qu-e--quick-grid-lookup)
- [QU-F — Query Executor](#qu-f--query-executor)
- [Cross-references](#cross-references)

---

## Queries Overview

*Source: [queries_and_reports.htm](../../../samples/chm/extracted/queries_and_reports.htm)*

The Queries menu contains reports and drill-down queries that do not belong to
any specific module because the information they display can jump across many
different data files. The same drill-down functionality also appears inside
lookup screens embedded in other programs — for example, IN-A Inventory Inquiry
and IN-B Enter Inventory.

### Drill Down button

The Drill Down function appears in programs as a button with a **green circle
containing a white arrow pointing downward**. Pressing it displays a list of
destination options. The system uses the data from the currently highlighted
record to link into and filter the destination file. Drill links only appear if
they have been established and if the user has a security level that permits
access.

Once inside drill-down data the user can continue drilling deeper or navigate
back up by clicking the **red circle with a white arrow pointing upward** — this
back-up button appears only when the user has drilled into a lookup.

### Lookup grid anatomy

Every lookup grid is divided into two areas:

| Area | Contents |
|---|---|
| Top (navigation bar) | Move-to-top, Previous, Next, Move-to-last; **Select**, **Edit**, **Add**, **Delete**, **Exit** buttons; **Fast Find** field; sort-selection dropdown; toolbar buttons |
| Bottom | Data rows |

**Navigation bar behavior:**

- **Select** (or Enter, or double-click) — returns the highlighted value to the
  calling program.
- **Exit** (or Esc) — returns to the calling program without returning a value.
- **Fast Find** — incremental search field; searches the current index as the
  user types. Changing the sort order is done via the dropdown on the right side
  of the sort list.

### Toolbar buttons

The toolbars are dynamic — what is displayed depends on the context:

| Button / Icon | Availability | Function |
|---|---|---|
| Camera | Inventory lookups | Display image/document links attached to the record |
| Drill Down (green arrow down) | When drill links are established and permitted | Open drill-down destination menu |
| Drill Up (red arrow up) | After drilling into a lookup | Navigate back to the previous level |
| Funnel with equals sign (substring search) | All grids | Filter the grid by a substring; search is case-insensitive and finds all matches; the resulting grid is treated as a drill-down (can drill back up or continue drilling down); up to 6 user-configurable search fields |
| Print Grid | All grids | Dump the current drill-down results to an RTM report |
| Print associated documents | Sales and Purchases contexts | Prompts whether to print Acknowledgements, Packing Lists, or Invoices (Sales) or Purchase Orders (Purchases) |

---

## QU-A — Master Inquiry

*Source: [qu-a_master_inquiry.htm](../../../samples/chm/extracted/qu-a_master_inquiry.htm)*

**Purpose.** Use this program to drill down from any of the available starting
points, using the Lookup Grids and drill-down menus available throughout EvoERP.
It is the top-level entry point to the system's cross-module drill-down
capability.

### Operation

QU-A does not itself define the drill-down destinations — those are determined by
the Lookup Grids and the drill links that have been configured for each grid. The
program launches the generic drill-down framework so a user can begin from any
lookup and follow data relationships across modules without starting from a
specific module program.

See the **Drill Down general information** in the [Queries Overview](#queries-overview)
section above for the full description of navigation controls, toolbar buttons,
Fast Find, substring search, Print Grid, and Print Associated Documents.

---

## QU-B — Calendar Drill Down

*Source: [qu-b_calendar_drill_down.htm](../../../samples/chm/extracted/qu-b_calendar_drill_down.htm)*

**Purpose.** Use this program to display a calendar of the current (or any)
month with dates that have order activity highlighted. Clicking a highlighted
date shows the list of orders due on that date, and from there the user can
continue drilling into related information.

### Operation

- The calendar defaults to the current month but can be navigated to any month.
- Dates with order activity (Sales Orders, Purchase Orders, or Work Orders) are
  visually highlighted.
- Clicking a highlighted date opens a list of the orders scheduled for that date.
- From the order list the user can apply standard drill-down navigation to reach
  further related records.

### Order types surfaced

| Order type | Module |
|---|---|
| Sales Orders | SO |
| Purchase Orders | PO |
| Work Orders | WO |

---

## QU-C — Calendar Summary Report

*Source: [qu-c_calendar_summary_report.htm](../../../samples/chm/extracted/qu-c_calendar_summary_report.htm)*

**Purpose.** Use this program to display or print summary shipment information
organized by date in a calendar-style layout.

### Operation

- Each date cell contains summary shipment lines scheduled for that date.
- If more lines are due to ship on a given date than will fit in the date cell,
  the report uses additional pages to accommodate the overflow.
- The report can be displayed on screen or sent to a printer.

---

## QU-D — Business Status

*Source: [qu-d_business_status.htm](../../../samples/chm/extracted/qu-d_business_status.htm)*

**Purpose.** Use this program for a financial snapshot of the company, with
limited drill-down capability into some of the displayed fields.

### Operation

QU-D is the Queries-menu entry point to the Business Status dashboard. The full
detail of the fields and drill-down options for this screen is documented at
**GL-R Business Status** (General Ledger module). Refer to that topic for the
complete field-by-field description.

Key characteristics:

- Provides a high-level, at-a-glance view of company financial health.
- Selected fields support limited drill-down to underlying detail.
- Because it shows GL-sourced financial data it requires access permissions
  consistent with GL reporting.

---

## QU-E — Quick Grid Lookup

*Source: [qu-e_quick_grid_lookup.htm](../../../samples/chm/extracted/qu-e_quick_grid_lookup.htm)*

**Purpose.** Use this program to launch a lookup grid for any EvoERP data file
without being called from another program.

### Operation

- Normally, lookup grids are invoked from within data-entry programs (e.g., when
  pressing F2 or clicking a lookup button on a field). QU-E makes the same grids
  available as a standalone tool.
- The user selects which file's lookup grid to open.
- Once open, all standard grid features are available: Fast Find, sort selection,
  drill-down, substring search, Print Grid, and Print Associated Documents (where
  applicable).
- This is useful for ad-hoc browsing of any EvoERP table without navigating into
  a data-entry program.

---

## QU-F — Query Executor

*Source: [qu-f_query_executor.htm](../../../samples/chm/extracted/qu-f_query_executor.htm)*

**Purpose.** Use this program to execute pre-defined SQL queries that accept
user-supplied variables (such as a date range). It allows regular users to run
administrator-prepared queries without having access to the full query-design
wizard.

### Prerequisites

- SQL queries with variables must first be defined by an administrator in
  **DE-A SQL Query/Export**.
- JDBC connection settings must be configured at **SM-T Enter Java Settings**
  before this program will function.

### General program operation

1. Click the **dropdown** to see the list of available queries.
2. Enter values for the prompted **variables** (e.g., start date, end date,
   customer code).
3. Click **Execute**.
4. Results appear in a results window.
5. Click **Export to CSV** to open the results in the system's default CSV
   application (typically Microsoft Excel).

### Design intent

The separation between query definition (DE-A) and query execution (QU-F) is
deliberate. Administrators can craft complex SQL with parameters in DE-A and then
publish only QU-F access to end users, keeping the underlying SQL hidden while
still giving users self-service reporting capability.

### Dependencies

| Dependency | Location |
|---|---|
| Query definitions (SQL with variables) | DE-A SQL Query/Export |
| JDBC connection configuration | SM-T Enter Java Settings |

---

## Cross-references

| Related module / program | Relationship |
|---|---|
| **IN-A Inventory Inquiry** | Drill-down capability is embedded in this program's lookup screens |
| **IN-B Enter Inventory** | Drill-down capability is embedded in this program's lookup screens |
| **SO — Sales Orders** | Calendar drill-down (QU-B) surfaces SO activity; Print Associated Documents shows acknowledgements, packing lists, invoices |
| **PO — Purchase Orders** | Calendar drill-down (QU-B) surfaces PO activity; Print Associated Documents shows POs |
| **WO — Work Orders** | Calendar drill-down (QU-B) surfaces WO activity |
| **GL-R Business Status** | QU-D is the Queries-menu alias for this GL program; see GL for full field documentation |
| **DE-A SQL Query/Export** | Defines the parameterised SQL queries that QU-F executes |
| **SM-T Enter Java Settings** | Required JDBC configuration for QU-F |
| **SU — Setup (grid lookups)** | SU-A Maintain Grid Lookups configures which drill links and search fields appear in the lookup grids used by QU-A and QU-E |
