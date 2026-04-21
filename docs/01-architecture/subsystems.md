# Supporting Subsystems

Status: draft — assembled from filename inventory, JAR contents, help
topics, and string dumps.

These are the EVO features that **aren't modules** but run alongside
them.

## EvoNotes — in-app notes / CRM

| Component | File |
| --------- | ---- |
| Main      | `EvoNotes.RWN` |
| Archive   | `EvoNotesARCH.RWN` |
| Search    | `EvoNoteSearch.RWN` |
| Print     | `EvoNotesPrt.RWN` |
| Report    | `EvoNotesRpt.RWN` |
| Migration | `classic2evonts.DFM` — migrate old "Classic" notes in |
| Entry form | `EVOENOTES.DFM` ("Entering Notes") |
| Context   | `ENPM.DFM` ("Evo Notes:") |
| Per-customer entry | accessible from `T7ARA*` customer forms |

EvoNotes is a per-record, append-only note log. Any master record
(customer, vendor, item, work order, etc.) has an **Evo Notes button**
available — a TAS program call wires the current record's key into
EvoNotes before opening it. The CHM section `using_evo_notes` +
`evo_notes_search` is the user-facing doc.

## EvoScheduler — cron-like scheduler

| Component | File |
| --------- | ---- |
| Main      | `EvoScheduler.RWN` |
| Lightweight | `EvoSched.RWN` |
| Setup     | `EvoSchedSetup.RWN` |
| Auto-MRP  | `AUTOT7MRF.RWN` — scheduler variant of `MR-F` |

The scheduler reads a job table (schedule name, program to run,
start time / interval, next-run date) and invokes target RWN files.
Likely backed by a `BKSCHED*` or similar table. Paired with
`EvoService.RWN` for unattended execution.

## EvoService — Windows service harness

| Component | File |
| --------- | ---- |
| Install   | `EvoServiceSetup.RWN` |
| Uninstall | `EvoServiceRemove.RWN` |
| Runner    | `EvoService.RWN` |

Runs EVO programs as a Windows service so that `EvoScheduler` jobs fire
whether or not a user is logged in. The `SERVICE\` folder on the share
likely contains the service's configuration.

## EvoBackup — built-in backup

| Component | File |
| --------- | ---- |
| Main      | `EvoERPbackup.RWN` (and `EvoERPBACKUP.DCY`) |

Zips the company folders using `zipdll.dll`/`unzdll.dll` and stores
snapshots in `\\i2s109-solidcrm\Bak Up\` or `\\…\Recovered\`.

## EvoDC — Data Collection (shop-floor / handheld)

Distinct subsystem from the DC module docs — these are the *runtime*
infrastructure files:

| Component | File |
| --------- | ---- |
| Main      | `EvoDC.RWN` |
| Main menu | `EvoDCmenu.RWN` / `EvoDCmenu2.RWN` |
| Setup     | `EvoDCsetup.RWN` |
| Demo workstations | `EvoDemoWks.RWN` |
| Mobile setup | `EvoMobilSetup.RWN` / `EvoMobileSetup.RWN` |
| Label tables | `BKDC*` (7 tables, see
  [../03-modules/dc-data-collection/README.md](../03-modules/dc-data-collection/README.md)) |
| Handheld forms | `T7HH*` (44 forms) |

Paired `BKDCLAB` / `BKDCHLAB` / `BKDCPLAB` / `BKDCCLAB` tables store
label designs for wave labels / palette labels / carton labels.
`EvoMobileSetup` is the PDA / RF-barcode-gun client.

## EvoLinks — document attachments

| Component | File |
| --------- | ---- |
| Main      | `EvoLinks.RWN` |
| Converter | `EvoLinkCVT.RWN` |

"Links" are **document attachments** on any record — PDFs, emails,
photos associated with a customer, vendor, order, etc. Stored in
`\\…\LinkDoc\` on the share. Help topic `using_evo_links`.

## EvoFNO — "Features & Options"

| Component | File |
| --------- | ---- |
| Main      | `EvoFNO.RWN` |
| SO tie-in | `EvoFNOSO.RWN` |
| PO tie-in | `EvoFNOPO.RWN` |
| WO tie-in | `EvoFNOWO.RWN` |

"Features and Options" is EVO's **option-configurator** — the Dell-laptop
"choose your CPU / RAM / screen" style. Help topic
`using_features_and_options_in_sales_orders` + `setting_up_features_and_options`.

## EvoUpdate — in-app updates

| Component | File |
| --------- | ---- |
| Main      | `EvoUpdate.RWN` / `EvoERPupd.RWN` / `EvoPRupd.RWN` |
| Setup     | `EvoUPDSetup.RWN` |
| Runtime update | `UPDTP7.EXE` (shipped in `C:\ISTS`) |

Pulls new `.RWN`/`.DFM`/`.DCY`/`.RTM` releases from Addsum and applies
them to the share. `.UPD` files (see
[../02-file-formats/other-formats.md](../02-file-formats/other-formats.md))
carry the DDF schema migrations that accompany a release.

## Evo Notes Search (`EvoNoteSearch`) + Drill-Down (`EvoERPDrillM`)

Cross-record search and drill-down navigation. `EvoERPDrillM.RWN`
provides the "drill into source" feature where you can click a GL
entry and jump back to the originating AP check or AR invoice.
Tables: likely `BKDRILL*` / drill-map tables.

## Calendar + reminders

Help topic `google_calendar`. Files:

- `CALREM.RWN` / `calrem.DFM` — calendar reminder core
- `CALREMGC.DFM` — Google Calendar sync form
- `CALDRILL.DFM` / `CALGRIDDRILL.DFM` / `calDDsel.DFM` — calendar drill-down
- `CALENDARS\` folder on the share — calendar data

## Chart demo / reusable charts

- `ChartDemo.DFM`, `chartBarModal.DFM`, `chartLineModal.DFM`,
  `chartPieModal.DFM` — modal chart surfaces callable from any
  program. Wired to the runtime keywords `SET_CHARTDATA`,
  `SET_CHARTCOLOR`, `SET_CHARTSERIESLABEL`, etc.

## CRM Dashboard

`CRMDASHBOARD.RWN` + `CRMDASHBOARD.DFM` — consolidated customer view.

## CashFlow / CommissionRpt / BOMTree / EditBOMTree

Standalone "analysis" utilities:

- `CASHFLOW.RWN` / `CashFlowReport.DFM` — cash-flow forecast
- `COMMISSIONRPT.RWN` — commission reporter
- `BOMTREE.RWN` / `EDITBOMTREE.RWN` — visual BOM tree explorer

## FNO / MRP helpers

- `AUTOT7MRF.RWN` — auto MRP (scheduled)
- `EvoEMTrns.RWN` — email transmissions
- `EvoCSI` — "Check Settings & Info" (likely diagnostic)
- `EvoBS` / `EvoVIEW` — business-status / generic viewer

## Things still to document

- The exact fields/tables used by EvoNotes (presumably `BKNOTE*` or
  similar, but it's not in the `BKNOTE*` prefix we catalogued — might
  use a dedicated `NOTES*` table, need to check the schema for it).
- EvoScheduler's schedule table.
- EvoLinks' attachment-storage schema (where the document path lives
  vs. where the file lives).
