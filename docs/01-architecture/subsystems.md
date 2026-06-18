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

## EvoNotes — note tables (Pass 106k)

EvoNotes is NOT a single table — each module has its own `*NOTE` table:

| Table | Module | Purpose |
|-------|--------|---------|
| `BKAPNOTE` | AP | AP vendor/transaction notes |
| `BKBMNOTE` | BM | Bill-of-materials notes |
| `BKEDNOTE` | ED | EDI notes |
| `BKQTNOTE` | QT | Quote notes |
| `BKSONOTE` | SO | Sales-order notes |
| `ISANOTES` | IS | General IS notes |
| `ISNOTES` | IS | General notes store |
| `ISSNOTES` | IS | System notes |
| `MKTNOTE` | MKT | Marketing notes |

Standard schema pattern (from `BKAPNOTE` DDF):
```
BKAP_NOTE_SRCH1   STRING  10   — first search key (e.g., vendor code)
BKAP_NOTE_SRCH2   STRING  10   — second search key (e.g., document number)
BKAP_NOTE_DATE    DATE     4   — note date
BKAP_NOTE_ENTBY   STRING  10   — entered-by user
BKAP_NOTE_NOTES_1 STRING  76   — note text line 1
... (additional _NOTES_N lines for continuation)
```
Primary key = SRCH1 + SRCH2 + DATE (composite — allows multiple notes per document).

## EvoScheduler — ISSCHED (confirmed Pass 106f)

Schedule table: `ISSCHED.B` (confirmed in Pass 106f). 24-field schema:
`NAME` (PK) + `DESC` + `PROG` + `CO` + `TYPE` (O/D/W/M) + `DATE` + `TIME` +
`RECUR` + `LOG` + `EXTRA` + `LDATE/LTIME` + `WHO` + `EMAIL` + `PARAM1..9` + `PARAM0`
See `HELP-RESOURCES.md` §AUTO/Batch for the full details.

## EvoLinks — ISLINKS schema (confirmed Pass 106k)

`ISLINKS.B` — 311-field schema (DDF confirmed):

| Field | Size | Meaning |
|-------|------|---------|
| `IS_LNK_UID` | 48 | Parent record key — the EvoERP record this document is attached to |
| `IS_LNK_LINK` | 256 | File path / URL of the linked document |
| `IS_LNK_APP` | 10 | Module code (e.g., `AR`, `PO`, `SO`) that owns this link |
| `IS_LNK_TYPES_1..100` | 1×100 | Array: which of 100 document type codes apply |
| `IS_LNK_PCB_1..100` | 1×100 | Array: "print check box" flags per type code |
| `IS_LNK_DEF_1..100` | 1×100 | Array: default-include flags per type code |
| `IS_LNK_GLOBAL` | 1 | Global flag: `Y` = visible to all companies |
| `IS_LNK_OPENWITH` | 1 | Open-with behavior flag |
| `IS_LNK_DATE` | 4 | Date document was attached |
| `IS_LNK_WHO` | 15 | User who attached it |
| `IS_LNK_ATYPE` | 3 | Attachment type code |
| `IS_LNK_EXTRA` | 100 | Supplemental metadata |
| `IS_LNK_PRIVATE` | 1 | Private flag: hides from other users |
| `IS_LNK_SORT` | 8 (FLOAT) | Sort order within attachment list |

The 100-element arrays (TYPES/PCB/DEF) are TAS `array 100` occurrences — each index
position maps to one of up to 100 configurable document-type categories (e.g., "quote",
"drawing", "PO confirmation"). EvoLinks stores ONE record per attached file, with the
bitmask of applicable types in the array columns.
