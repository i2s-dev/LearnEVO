# EvoERP Menu System

Status: verified — extracted from the readable strings in every RUN/RWN
file on the share (2026-04-17, 2,439 modules scanned).

## The find

The **TAS Pro 6 `.RUN` files are _not_ encrypted** the way the TAS
Pro 7 `.RWN` files are. The strings inside them are fully readable.
Bulk-dumping them (see `scripts/bulk_strings_rwn.py`) and mining for
`XX-Y[-Z]  <description>` patterns (see `scripts/extract_menu_codes.py`)
yielded **554 unique menu codes** belonging to ~60 functional modules.

Full list: `../../samples/menu_tree.md` (human-readable, per-module),
CSV: `../../samples/menu_codes.csv` (machine-readable, with source module
references).

## Menu-code format

```
<MODULE>-<LEVEL1>[-<LEVEL2>]
```

- `<MODULE>` — 2-letter functional area code (see "Module map" below).
- `<LEVEL1>` — single letter indicating the operation within the module.
- `<LEVEL2>` — optional sub-operation letter (for drilled-down menus).

Examples:
- `AR-A` — Enter Customers
- `AR-C` — Record Payments
- `SO-F` — Print/Reprint Invoices
- `WO-L-A` — Print Work Order Status
- `IN-L-A` — (inventory sub-screen — referenced from BM-G)

The **first letter (LEVEL1)** is conventionally:
- `A` = enter/maintain master data (add/edit records)
- `B` through `Z` = activity screens, inquiries, reports, utilities —
  in roughly alphabetical order of typical business workflow.

The pattern is legible even without docs: `AP-A` enters vendors, `AP-B`
enters vouchers, `AP-C`… wait, missing. `AP-D` enters scheduled
payments, `AP-E` prints due vouchers, `AP-F` picks what to pay,
`AP-G` prints proforma register, `AP-H` prints checks, `AP-I` prints
aging. So the LEVEL1 letters track a business process from master-data
entry through transaction entry through printing/reporting.

## Module map (by number of operations)

### Top modules
| Module | Name                        | Ops | Notes |
| ------ | --------------------------- | --- | ----- |
| **SO** | Sales Orders                | 48  | Largest — SO-A through SO-Z with many sub-menus |
| **IN** | Inventory                   | 40  | Item maintenance, receipts, transfers, reports |
| **SM** | System Manager              | 34  | Setup & administration of everything |
| **DE** | Data Exchange               | 33  | Import/export: inventory, BOM, routings, customers, vendors, COA, labor, QB GL export |
| **WO** | Work Orders                 | 31  | Manufacturing order lifecycle |
| **PO** | Purchase Orders             | 29  | |
| **PR** | Payroll                     | 29  | Payroll processing |
| **UT** | Utilities                   | 20  | General-purpose utilities |
| **AP** | Accounts Payable            | 19  | |
| **RO** | Routing                     | 19  | Manufacturing routings |
| **LW** | Labor / Work Schedule       | 18  | Shop-floor labor reporting |
| **JC** | Job Costing                 | 18  | Project/job profitability |
| **AR** | Accounts Receivable         | 17  | |
| **AM** | Archive / Maintenance       | 17  | Period-end close, purge, fiscal, rebuild |
| **CS** | Commission System           | 16  | |
| **GL** | General Ledger              | 16  | |
| **SH** | Shipping                    | 16  | |
| **SA** | Sales Analysis              | 13  | |
| **MR** | MRP                         | 12  | Material requirements planning |
| **SD** | System Defaults             | 12  | |
| **BM** | Bill of Materials           | 10  | |
| **PI** | Physical Inventory          | 9   | |
| **SR** | Service / Repair            | 9   | |
| **ES** | Estimating                  | 8   | |
| **DC** | Data Collection             | 7   | Shop-floor barcode |
| **LC** | Lot Control                 | 7   | |
| **SC** | Serial Control              | 7   | |
| **ED** | EDI                         | 6   | |
| **WC** | Work Centers                | 6   | |
| **PS** | Payroll Setup               | 5   | |
| **MM** | Manufacturing Mgmt Reporting | 4  | Cross-module mfg reports; menu entries share BKAPJ/BKARG/BKAPA programs |
| **RM** | Return Material Authorization | 4 | RM-A Enter RMA, RM-C Receive, RM-D Process, RM-E Reason Maint. Current name for legacy AB module. |
| **IS** | i2 Systems Custom Reports   | 4   | Uses J5/J6/JM-prefix programs (i2 custom): Item Recap, Production Report, Top-N Ships, New Customer |
| **AD** | Admin Defaults              | 3   | System-wide default toggles |
| **FO** | Form Output                 | 3   | |
| **LM** | Lot Management              | 2   | LM-B Item Generator Templates; LM-H Purge QC Receipts |
| **PL** | Checkmark Payroll Link      | 4   | PL-A Run Checkmark Payroll; PL-B/C Import Checks/Vouchers; PL-D Setup |
| **DI** | Data Import (Labor)         | 1   | DI-G Import Labor (BKDIG); single-operation import sub-module |

Total: **554 menu codes** across 38 identified modules — all module names now confirmed.

## Module name confirmations (Pass 104)

| Code | Confirmed Name | Evidence |
|------|---------------|---------|
| DE | Data Exchange | DE-A=Export Data; DE-B..H=Import various (Inventory/BOM/Routings/Customers/Vendors/COA/Labor); DE-O=Export to QuickBooks |
| IS | i2 Systems Custom Reports | IS-A..D use J5/J6/JM-prefix programs — i2 Systems custom Java-based tools |
| MM | Mfg Mgmt Reporting | MM menu entries reuse BKAPJ (print vendor), BKARG (print customer), BKAPA (enter vendors) — a reporting shortcut hub |
| PL | Payroll Link | PL-E description = "Payroll Software Link Setup" (BKPLE source confirmed) |
| RM | Return Material Authorization | RM-A Enter RMA; supersedes legacy AB module naming |
| LM | Lot Management | LM-B Item Generator Templates; LM-H Purge QC Receipts |
| DI | Data Import (Labor) | DI-G Import Labor (BKDIG); possibly "Direct Import" variant |

## Example — AP (Accounts Payable) full menu

| Code | Operation |
| ---- | --------- |
| AP-A | Enter Vendors |
| AP-B | Enter Vouchers |
| AP-D | Enter Scheduled Payment Dates |
| AP-E | Print Vouchers/Invoices Due by Date |
| AP-F | Pick Vouchers/Invoices to Pay |
| AP-G | Print Pro Forma Check Register |
| AP-H | Print Checks |
| AP-I | Print Aging |
| AP-J | Print Vendor Code and Name |
| AP-K | Print Vendor General Info |
| AP-L | Print Vendor Purchase Info |
| AP-M | Print Vendor Labels |
| AP-N | Print Vendor Rolodex |
| AP-O | Enter Recurring Vouchers |
| AP-P | Generate Recurring Vouchers |
| AP-Q | Void AP Check |
| AP-R | Print AP Payment History |
| AP-S | Print 1099 Forms |
| AP-U | Archive/Purge Vendor |

## Example — AR (Accounts Receivable) full menu

| Code | Operation |
| ---- | --------- |
| AR-A | Enter Customers |
| AR-B | Enter Vouchers |
| AR-C | Record Payments |
| AR-D | Charge Interest on Invoices |
| AR-E | Print Statements |
| AR-F | Print Aging |
| AR-G | Print Customer Code and Name |
| AR-H | Print Customer General Info |
| AR-I | Print Customer Mail Labels |
| AR-J | Print Customer Rolodex |
| AR-K | Print Sales Tax Report |
| AR-L | Transfer Sales Taxes |
| AR-M | Enter Customer Refund |
| AR-N | Print Customer Deposits |
| AR-P | Generate Dun Letters |
| AR-Q | View Customers |
| AR-S | Accounts Receivable Defaults |

## Naming → file mapping (rule of thumb)

An `XX-Y` operation typically has three parallel implementations:

1. `BKXXY.SRC`  / `BKXXY.RUN`  — TAS Pro 5/6 compiled (legacy).
2. `T6XXY.RUN`  — TAS Pro 6 Windows-ish.
3. `T7XXY.RWN`  + `T7XXY.DFM` — TAS Pro 7 current (the one users see).

Example: **AR-C (Record Payments)** is `BKARC.RUN`, `T6ARC.RUN`, and
(implicitly) `T7ARC.RWN` / `T7ARC.DFM`.

## Where the menu tree lives — CONFIRMED (Pass 105, 2026-06-18)

The menu data is stored in **`BKMENUSU.DBF`** on the network share — an xBase/dBASE
format file accessed by `tp7runtime.exe` via the embedded CodeBase 4 engine (`c4dll.dll`).
`EVOERPMENU.DCY` is the *visual form shell* (an 8-TTASStrList UI form); the *content* comes
from BKMENUSU.DBF at runtime.

A plain-text CSV export of the full menu tree is available at:
`\\i2s109-solidcrm\DBAMFG$\BKMENUSU.TXT` (870 lines — full menu) and
`\\i2s109-solidcrm\DBAMFG$\BKMENUST.TXT` (109 lines — Setup Wizard only).
Copies in `samples/BKMENUSU.TXT` and `samples/BKMENUST.TXT`.

### BKMENUSU.TXT record format

Three record types, all CSV with quoted fields:

```
"GROUPS","Group label","MODULE"          -- navigation tab assignment
"BUTTONS","Module full name","MODULE",N  -- module button (N = button index)
"CODE","&Label","program.rwn"            -- menu item → program mapping
```

### Module navigation groups

| Nav tab | Modules |
|---------|---------|
| Mfg | WO, JC, PO, MR, SH, DC, ES, QC |
| Items | IN, RO, BM, LC, SC, FO, PI, WC |
| Sales | SO, SR, RM, SA, CS, CM, AR, CR |
| Queries | QU, SU |
| Hand Held | HH |
| System Mgr | UT, SM, SD, IM, PS, DE, TAS |
| Accounting | GL, AP, FA, AM, AD |
| Pay Link | PL |
| Payroll | PR |
| Settings | US |

### Complete menu code → program mapping

The full list is in `samples/BKMENUSU.TXT`. Highlights that resolve prior unknowns:

| Code | Label | Program | Note |
|------|-------|---------|------|
| PL-A | Run Checkmark Payroll | T6PLA.RUN | PL = **Checkmark Payroll** integration |
| PL-B | Import Employee Checks | BKPLB.RUN | |
| PL-C | Import Employer Vouchers | BKPLC.RUN | |
| PL-D | Payroll Link Setup | BKPLD.RUN | |
| DE-U | Upload Stock to Web | J7BEFWEBINV.RWN | J7 custom |
| HH-H | Shipping Info | J7HHLITN.RWN | J7 custom |
| WO-K-J | Synch WO BOM/Routing | j7ptwoki.rwn | J7 custom |
| WO-L-L | WO BOM Component Labels | j7woll.rwn | J7 custom |
| PS-K | Enter Vendor Approval | J7appvend.rwn | J7 custom |
| TA-A | Run TAS Program | RUNPRG.INT | System menu |
| TA-B | Change Company Code | GETCO.INT | System menu |
| TA-C | Set Configuration | CONFIG.INT | System menu |
| TA-S | Data Dictionary Check | T7DDCHECK.RWN | System menu |
| NE | New Programs (14 buttons) | — | Custom i2 additions; not in TXT export |

**PL = Checkmark Payroll Link** — integrates with an external payroll application
called "Checkmark Payroll" (not EvoERP's own PR module). T6PLA.RUN launches Checkmark;
BKPLB/C.RUN import the resulting check and voucher data back into EvoERP.

### StartEvo.exe access control

Before `tp7runtime.exe` starts, `StartEvo.exe` (.NET assembly) queries:
```sql
SELECT count(*) FROM tas_menus WHERE menu_name = ? AND program_name = ?
```
via DSN `EVOADMIN` (Pervasive Server DSN). `tas_menus` is the PSQL SQL-engine view of
`BKMENUSU.DBF`. This is the license/access gate — if a program is not in `tas_menus`, it
cannot be launched.

## Open

- [x] Confirm the menu tree storage — **RESOLVED**: `BKMENUSU.DBF` (xBase/CodeBase format); `EVOERPMENU.DCY` is the form shell only.
- [x] Confirm the `DE`, `MM`, `IS`, `PL`, `DI`, `RM`, `LM` module meanings — all resolved (Pass 104–105, 2026-06-18).
- [ ] Map each menu code to the form captured in `samples/dfm_parsed/dfm_summary.csv` (T7XXY.DFM pair) — join between `BKMENUSU.TXT` and `dfm_summary.csv`.
- [ ] Identify NE (New Programs) 14 items — not in BKMENUSU.TXT export; likely i2-specific additions.
