# DFM Form Inventory — the UI Layer

Status: verified (from bulk parse of 1109 DFM files, 2026-04-17).

Every DFM was parsed with `scripts/parse_dfm.py` +
`scripts/bulk_parse_dfm.py`. Raw outputs in
`../../samples/dfm_parsed/dfm_summary.csv` (CSV, per-form stats) and
`../../samples/dfm_parsed/by_prefix.txt` (index).

## Top-level breakdown

| Module group | Form count | Role |
| ------------ | ---------- | ---- |
| **T7-SO**    | 69 | Sales Orders |
| **T7-WO**    | 68 | Work Orders |
| **T7-IN**    | 67 | Inventory |
| **T7-SM**    | 56 | System Manager / Setup |
| **T7-HH**    | 44 | Hand-Held (barcode / shop-floor data collection) |
| **T7-PO**    | 41 | Purchase Orders |
| **T7-PR**    | 40 | Payroll (`BKPR*` tables) |
| **T7-AP**    | 33 | Accounts Payable |
| **T7-RO**    | 25 | Routing |
| **T7-AR**    | 24 | Accounts Receivable |
| **T7-GL**    | 24 | General Ledger |
| **T7-DC**    | 22 | Data Collection (ERP shop-floor) |
| **T7-DE**    | 20 | Delivery / EDI |
| **T7-MR**    | 18 | MRP (Material Requirements Planning) |
| **T7-BM**    | 16 | Bill of Materials |
| **T7-AM**    | 15 | Asset Management / Alt Master |
| **T7-QC**    | 15 | Quality Control |
| **T7-SH**    | 15 | Shipping |
| **T7-JC**    | 14 | Job Costing |
| **T7-WC**    | 13 | Work Centers |
| **T7-CM**    | 12 | Customer Master / Config |
| **T7-CS**    | 12 | Cost System |
| **T7-SR**    | 12 | Sales Reports |
| **T7-PI**    | 10 | Physical Inventory |
| **T7-RE**    | 10 | Reports |
| **T7-EV**    | 9  | Evolution utilities |
| **T7-SC**    | 9  | Scheduler? |
| **T7-ES**    | 7  | Estimating |
| **T7-JS**    | 7  | Job Shop |
| **T7-LC**    | 7  | Labor Capture? |
| **T7-CC**    | 6  | Cycle Count |
| **T7-PS**    | 6  | Payroll Setup? |
| **T7-SA**    | 6  | Sales Analysis |
| **T7-SP**    | 6  | Ship Packing? |
| **T6-IS**    | 9  | Information System (TAS 6 era remnants) |
| **PLATFORM-EVO**  | 53 | Platform (EvoMenu, EvoFilters, EvoNotes, EvoService…) |
| **PLATFORM-WTAS** | 14 | Generic TAS-shipped windows |
| **PLATFORM-WBK**  | 11 | Wrapper-Bookkeeping scaffolds |
| **PLATFORM-HT**   | 4  | HT6-era handheld (legacy) |
| **J7-\***         | 20+ | Customer-specific customizations |
| **OTHER**         | 49 | Utility/tool forms (Chart, Calendar, Drill, BOMTree, CashFlow, CRMDashboard, etc.) |

## How this was extracted

`scripts/parse_dfm.py` is a small Delphi-text-DFM parser (~100 lines of
Python). It walks the `object ... end` tree and captures:
- Every object's name and VCL class.
- Every property = value pair on every object.
- Binary blobs collapsed to `<HEX N bytes>`.

The bulk script (`bulk_parse_dfm.py`) runs it across both the network
share and the local cache, deduping by filename, and writes per-form
statistics + a prefix-grouped index.

### What the stats tell us

- **Field count** = number of child controls declaring a `FieldName`
  property (i.e. bound to a program variable).
- **Control counts** (TTASENTER, TTASNumEnter, TTASDateEdit, etc.) show
  how data-entry heavy each form is.
- **Tab count** (TTabSheet) shows multi-pane forms. `T7ARA` has 7 tabs;
  `EVOFILTERS` has 11.

### Biggest forms (by total control count)

From a quick pass of `dfm_summary.csv`, the heaviest forms are typically:
- `EVOFILTERS.DFM` — filter/query builder (270 controls, 11 tabs, 106 fields)
- `T7INA.DFM` — inventory item master (several hundred controls)
- `T7ARA.DFM` — AR customer master (275 controls, 57 TASENTERs, 7 tabs)
- `T7SOA.DFM` — Sales Order master
- `T7WOA.DFM` — Work Order master

These five forms alone are the heart of the user-facing ERP.

## Parsing errors (25 files)

All 25 failures are **zero-byte placeholder `.DFM` files** on the
share (e.g. `EVOLOGO.DFM`, `EVOCHANGEPASS.DFM`, `T7APACH.DFM`). They
are real files on disk but contain nothing. Safe to treat as "form
referenced by name but layout not yet implemented / dormant".
Log: `../../samples/dfm_parsed/errors.txt`.

## Notable non-obvious findings

- **`EVOFILTERS.DFM`** is a filter-builder with 11 tab sheets and 106
  bound fields — a generic grid-filter UI that every list screen
  probably calls into.
- **`CHART*` family** (4 forms) — `chartBarModal`, `chartLineModal`,
  `chartPieModal`, `ChartDemo` — a built-in charting surface available
  to any program. Paired with runtime keywords `SET_CHARTCOLOR`,
  `SET_CHARTDATA`, `SET_CHARTIMAGE`, etc.
- **`calDDsel.DFM`**, **`CALDRILL.DFM`**, **`CALGRIDDRILL.DFM`** — the
  calendar drill-down module (matches `CALENDARS\` folder on the share).
- **`DFMALTS.DFM`** — "Set ALT Keys for DFMs" — lets users rebind
  keyboard accelerators in forms at runtime. Not something I would have
  guessed existed.
- **`classic2evonts.DFM`** — migration screen to pull "Classic"
  (DBA Manufacturing-era) notes into the `EvoNotes` subsystem.
- **`chartDemo.DFM`** has caption "Addsum TAS 7i Chart Demo Program"
  — more confirmation that the runtime is Addsum TAS Pro 7i.

## Open follow-ups

- Build per-module sub-pages (AR / AP / IN / SO / PO / WO / GL) that
  list each form, its caption, the program variables it binds to, and
  which tables those map onto. That's the long tail.
- Decode and document the `EVOFILTERS` generic filter — one
  understanding of that will explain most list-screen behavior.
