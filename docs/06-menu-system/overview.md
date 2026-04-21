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
| **DE** | Delivery (or "Demand Est"?) | 33  | *To confirm* — possibly Delivery planning |
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
| **MM** | Multi-Module?               | 4   | *To confirm* |
| **RM** | RMA (Return Merch Auth)     | 4   | |
| **IS** | Information System?         | 4   | *To confirm* — shows up in many `IS*` files |
| **AD** | Admin Defaults              | 3   | System-wide default toggles |
| **FO** | Form Output                 | 3   | |
| **LM** | Label Management            | 2   | |
| **PL** | Plotting?                   | 2   | |
| **DI** | Dispatch?                   | 1   | |

Total: **554 menu codes** across 38 identified modules.

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

## Where this maps onto the UI

The user sees an EVO-branded hierarchical menu rendered by
`EvoERPmenu.RWN` (encrypted T7) — the menu leaf selects a `T7XXY.RWN`
module to run. The menu **tree itself** is stored in either
`\\I2S109-SOLIDCRM\DBAMFG$\EVOERPMENU.DCY` (encrypted) or in a
Pervasive DB table — cannot yet confirm without a running instance.

## Open

- [ ] Confirm the menu tree lives in a DB table or in `EVOERPMENU.DCY`.
  If the former, we can dump it. If the latter, only the decrypted
  runtime can read it — and we saw the encryption warning in
  `tp7runtime.exe` strings. Deferred.
- [ ] Map each menu code to the form captured in
  `samples/dfm_parsed/dfm_summary.csv` (T7XXY.DFM pair) — a join
  between `menu_codes.csv` and `dfm_summary.csv`.
- [ ] Confirm the `DE`, `MM`, `IS`, `PL`, `DI` module meanings by
  reading their SRC/RUN samples.
