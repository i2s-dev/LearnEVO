# EvoERP Module Code Reference

Status: verified — derived directly from `BKMENUSU.TXT` (GROUPS + BUTTONS sections,
Pass 410, 2026-06-30). 786 menu items confirmed. 42 module codes cataloged.

## Complete Module Table

Confirmed from `\\i2s109-solidcrm\DBAMFG$\BKMENUSU.TXT` GROUPS + BUTTONS sections.
Menu item counts from `samples/menu_catalog.csv`.

| Code | Full Name | Group | Items | Notes |
|------|-----------|-------|------:|-------|
| **AD** | Accounting Defaults | Accounting | 3 | Setup defaults for GL/AP/Checking |
| **AM** | Accounting Maintenance | Accounting | 18 | Period-close, fiscal year-end, GL accounts, purge/archive |
| **AP** | Accounts Payable | Accounting | 30 | Vouchers, vendor payments, 1099s |
| **AR** | Accounts Receivable | Sales | 18 | Customer invoicing, cash receipts, statements |
| **BM** | Bill of Materials | Items | 18 | BOM structure, where-used, rollup |
| **CM** | Contact Master | Sales | 9 | CRM / contact accounts, reminders, notes |
| **CR** | Contract Review | Sales | 2 | Contract review and approval workflow |
| **CS** | Commissions | Sales | 16 | Sales rep commission tracking and payout |
| **DC** | Data Collection | Mfg | 14 | Shop-floor data collection / barcode scanning |
| **DE** | Data Exchange | System Mgr | 62 | Import/export data (SQL export, inventory import, etc.) |
| **ES** | Estimates | Mfg | 11 | Job/project estimation |
| **FA** | Fixed Assets | Accounting | 5 | Asset register, depreciation |
| **FO** | Features and Options | Items | 7 | Configurable item features and options |
| **GL** | General Ledger | Accounting | 19 | Chart of accounts, journal entries, financial statements |
| **HH** | Hand Held Programs | Hand Held | 13 | Mobile/handheld terminal functions |
| **IM** | International Module | System Mgr | 7 | Multi-currency, international settings |
| **IN** | Inventory | Items | 41 | Item master, transactions, adjustments, reports |
| **JC** | Job Costing | Mfg | 20 | Job cost tracking, labor/material allocation |
| **LC** | Lot Control | Items | 6 | Lot tracking for serialized/lot-controlled inventory |
| **MR** | MRP | Mfg | 14 | Material Requirements Planning — demand/supply netting |
| **PI** | Physical Inventory | Items | 8 | Cycle count and physical inventory count |
| **PL** | Pay Link | Pay Link | 4 | Payroll data link/export |
| **PO** | Purchase Orders | Mfg | 35 | PO entry, receiving, vendor invoicing |
| **PR** | Payroll | Payroll | 36 | Payroll processing, checks, tax filings |
| **PS** | Password Security | System Mgr | 11 | User/menu security setup |
| **QC** | Quality Control | Mfg | 18 | Inspection, non-conformance, corrective action |
| **QU** | Queries & Reports | Queries | 6 | Ad-hoc queries and report run/schedule |
| **RM** | RMA | Sales | 7 | Return Merchandise Authorization |
| **RO** | Routings | Items | 24 | Manufacturing routing operations and work centers |
| **SA** | Sales Analysis | Sales | 19 | Sales performance analysis, commission reports |
| **SC** | Serial Control | Items | 8 | Serial number tracking |
| **SD** | System Defaults | System Mgr | 21 | System-wide configuration defaults |
| **SH** | Scheduling | Mfg | 18 | Production scheduling |
| **SM** | System Maintenance | System Mgr | 69 | Master data maintenance shortcuts (customers, vendors, classes, etc.) |
| **SO** | Sales Orders | Sales | 57 | Order entry, shipping, invoicing |
| **SR** | Service and Repair | Sales | 9 | Service tickets, repair orders |
| **SU** | Query & Report Setup | Queries | 4 | Query/report template configuration |
| **TA** | System Configuration | System Mgr | 16 | TAS Pro system configuration (display code "TAS" in menus) |
| **US** | User Settings | Settings | 8 | Per-user preferences and settings |
| **UT** | Utilities | System Mgr | 15 | System maintenance utilities |
| **WC** | Warehouse Control | Items | 6 | Multi-warehouse / warehouse control |
| **WO** | Work Orders | Mfg | 54 | Shop order entry, travelers, pick lists, labor entry |

**Notes:**
- `NE` ("New Programs") — appears as a BUTTONS entry, 0 items, placeholder for new functionality.
- `AI` — 4 operations appear in `DBAHLPID.B` help system but has no GROUPS/BUTTONS entry (hidden/internal module).
- `TA` — menu items use 2-char prefix "TA"; BKMENUSU.TXT shows display name "TAS" (System Configuration).

## Module Groups

From `BKMENUSU.TXT` GROUPS section — groups correspond to the main navigation tabs in EvoERP:

| Group | Modules | Total Items |
|-------|---------|------------:|
| **Mfg** | WO, JC, PO, MR, SH, DC, ES, QC | 184 |
| **System Mgr** | UT, SM, SD, IM, PS, DE, TA | 185 |
| **Sales** | SO, SR, RM, SA, CS, CM, AR, CR | 137 |
| **Items** | IN, RO, BM, LC, SC, FO, PI, WC | 118 |
| **Accounting** | GL, AP, FA, AM, AD | 75 |
| **Payroll** | PR | 36 |
| **Hand Held** | HH | 13 |
| **Queries** | QU, SU | 10 |
| **Settings** | US | 8 |
| **Pay Link** | PL | 4 |
| **Total** | 42 modules | 786 items |

## Menu Code Format

Menu item codes follow one of two formats:

**3-char codes** (most items): `[2-char module][1-char operation]`
```
WOA = Work Orders, operation A = "Enter Work Orders" -> t7woa.rwn
APB = Accounts Payable, operation B = "Enter Vouchers" -> t7apb.rwn
GLN = General Ledger, operation N
```

**4-char codes** (sub-menu items): `[2-char module][1-char parent-op][1-char sub-op]`
```
CMBB = Contact Master, parent-B, sub-B = "Print Accounts Listing & Labels" -> t7cmbb.rwn
DEBA = Data Exchange, parent-B, sub-A = "Generate Import Header" -> T7DEBA.RWN
SMCA = System Maintenance, parent-C, sub-A = "Enter Item Classes" -> T7SMCA.RWN
```

Parent-op codes with no `.rwn` file are sub-menu headers (e.g. `CMB` = "Contact Account Reports" = no program, just a sub-menu).

## Program File Naming

| Prefix | Count | Meaning |
|--------|------:|---------|
| `T7xxx.rwn` | 699 | TAS Pro 7 compiled program (current) |
| `T6xxx.run` | 2 | TAS Pro 6 legacy program (t6amf.run, t6wola1.rtm) |
| `BK*.run` | 6 | Btrieve-era legacy programs |
| Other | 79 | Non-standard names (e.g. `sqlexport.rwn`, `evonotesrpt.rwn`) |

## Key Module Program Starters (Sample)

| Code | First Operation | Program |
|------|----------------|---------|
| WO-A | Enter Work Orders | `t7woa.rwn` |
| WO-B | Release Work Orders | `t7wob.rwn` |
| AP-A | Enter Vendors | `t7apa.rwn` |
| AP-B | Enter Vouchers | `t7apb.rwn` |
| SO-A | Enter Sales Orders | `t7soa.rwn` |
| IN-A | Enter Items | `t7ina.rwn` |
| GL-A | Enter G/L Journal Entries | `t7gla.rwn` |
| PO-A | Enter Purchase Orders | `t7poa.rwn` |
| SM-A | Enter Customers (shortcut) | `t7ara.rwn` |
| SM-B | Enter Vendors (shortcut) | `t7apa.rwn` |
| DE-A | Export Data | `sqlexport.rwn` |

See `samples/menu_catalog.csv` for the full 786-item catalog.
