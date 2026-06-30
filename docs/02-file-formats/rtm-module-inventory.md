# RTM Report Template Inventory by Module

Status: verified — direct scan of `\\i2s109-solidcrm\DBAMFG$\` (Pass 410, 2026-06-30).
Source data: `samples/rtm_by_module.csv` (1,734 entries).

## Summary

| Generation | Count | Meaning |
|-----------|------:|---------|
| **T6** | 965 | TAS Pro 6 era `.RTM` (legacy, majority of reports) |
| **BK** | 245 | BK-prefix legacy reports (Btrieve-era format, still active) |
| **Other** | 480 | Custom/variant names (EN*, IEN*, IBK*, J6*, etc.) |
| **T7** | 23 | TAS Pro 7 era `.RTM` (only 23 — reporting mostly unchanged) |
| **J7** | 21 | J7 custom i2 Systems extensions |
| **Total** | 1,734 | |

**Key insight:** The reporting layer is overwhelmingly TAS Pro 6 era. Only 23 T7 RTMs exist,
confirming that EvoERP upgrades the TAS program layer (RWN) without rebuilding report templates.
ReportBuilder format (`TPF0`) is format-stable across TAS Pro 6 and 7.

## RTM Count by Module

From known module codes in BKMENUSU.TXT:

| Code | Module Name | Total | T6 | T7 | BK | J7 |
|------|-------------|------:|---:|---:|---:|---:|
| SO | Sales Orders | 253 | 181 | 0 | 72 | 0 |
| WO | Work Orders | 115 | 103 | 2 | 8 | 2 |
| IN | Inventory | 102 | 88 | 2 | 12 | 0 |
| AP | Accounts Payable | 95 | 58 | 9 | 27 | 1 |
| PO | Purchase Orders | 89 | 53 | 0 | 36 | 0 |
| PR | Payroll | 52 | 41 | 0 | 11 | 0 |
| GL | General Ledger | 42 | 42 | 0 | 0 | 0 |
| JC | Job Costing | 37 | 37 | 0 | 0 | 0 |
| SA | Sales Analysis | 34 | 27 | 0 | 7 | 0 |
| SR | Service and Repair | 30 | 16 | 0 | 14 | 0 |
| BM | Bill of Materials | 30 | 30 | 0 | 0 | 0 |
| SM | System Maintenance | 22 | 22 | 0 | 0 | 0 |
| AR | Accounts Receivable | 50 | 30 | 0 | 20 | 0 |
| RM | RMA | 12 | 11 | 0 | 1 | 0 |
| SH | Scheduling | 18 | 18 | 0 | 0 | 0 |
| QC | Quality Control | 19 | 19 | 0 | 0 | 0 |
| MR | MRP | 16 | 16 | 0 | 0 | 0 |
| CS | Commissions | 14 | 14 | 0 | 0 | 0 |
| DC | Data Collection | 20 | 11 | 0 | 8 | 1 |
| DE | Data Exchange | 11 | 11 | 0 | 0 | 0 |
| RO | Routings | 17 | 17 | 0 | 0 | 0 |
| CM | Contact Master | 16 | 8 | 0 | 8 | 0 |
| ES | Estimates | 16 | 8 | 0 | 8 | 0 |
| AM | Accounting Maintenance | 7 | 7 | 0 | 0 | 0 |
| PI | Physical Inventory | 7 | 6 | 0 | 1 | 0 |
| UT | Utilities | 6 | 6 | 0 | 0 | 0 |
| PS | Password Security | 2 | 0 | 2 | 0 | 0 |
| FA | Fixed Assets | 0 | — | — | — | — |
| HH | Hand Held Programs | 1 | 1 | 0 | 0 | 0 |
| IM | International Module | 0 | — | — | — | — |
| FO | Features and Options | 3 | 3 | 0 | 0 | 0 |
| LC | Lot Control | 1 | 1 | 0 | 0 | 0 |
| QU | Queries & Reports | 1 | 1 | 0 | 0 | 0 |
| SC | Serial Control | 3 | 3 | 0 | 0 | 0 |
| WC | Warehouse Control | 3 | 3 | 0 | 0 | 0 |

Modules with T7 reports: **AP** (9), **WO** (2), **IN** (2), **PS** (2). All other modules
use T6/BK-format report templates that pre-date the TAS Pro 7 migration.

## Custom RTM Prefixes (i2 Systems Specific)

Several non-standard naming prefixes appear in the RTM catalog:

| Prefix | Count | Meaning |
|--------|------:|---------|
| `EN*` (e.g. `enSOB3.rtm`) | ~200 | i2 Systems **enhanced/modified** versions of standard forms |
| `IEN*` (e.g. `ienSOB1.rtm`) | ~50 | **International English** variant of EN forms |
| `IBK*` (e.g. `IBKSOB1.RTM`) | ~50 | **International BK** variants |
| `IT6*` (e.g. `IT6SOB3.RTM`) | ~40 | **International T6** variants |
| `J6*` (e.g. `J6ARBMB1.RTM`) | 15 | **TAS6-era i2 custom** reports (older than J7) |
| `J7*` | 21 | **TAS7-era i2 custom** reports (current) |
| `T6I2*` (e.g. `T6I2SINV.RTM`) | ~20 | **i2 Systems** customer-specific reports (`I2` = i2 Systems company code) |
| `EN+I2S` (e.g. `ENI2SINV.rtm`) | ~5 | i2 Systems enhanced invoice forms |

The `EN*` pattern is the most common custom form family. Examples:
- `enSOB3.rtm`, `enSOB4.rtm` — enhanced Sales Order body reports (SO-B)
- `enPOB1.rtm` through `enPOB4.rtm` — enhanced PO body reports (PO-B)
- `enWOC1.RTM` through `enWOC5j.rtm` — enhanced Work Order traveler reports (WO-C)
- `enARE1.RTM` through `enARE4.RTM` — enhanced AR invoice reports (AR-E)
- `enSOPB1.RTM` through `enSOPB20.RTM` — enhanced SO packing list/pick reports (SO-P-B)

The large `ENSOC4` family (12 variants: base + `a`, `B`, `41`, `cr`, `ic`, `M`, `T`, etc.)
shows how a single core report (SO-C invoice template) gets modified for different:
- Paper sizes and formats
- International markets
- Special customer requirements
- Print preview vs. print modes

## Report Density Analysis

**Modules with excessive RTM counts relative to menu items:**
- SO: 253 RTMs / 57 menu items = 4.4 RTMs per operation
- WO: 115 RTMs / 54 menu items = 2.1 RTMs per operation
- AP: 95 RTMs / 30 menu items = 3.2 RTMs per operation

This reflects the "multiple format variants per report" pattern: a single menu operation
(e.g., SO-C "Print Sales Order Acknowledgement") may call one of many RTM files depending
on paper size, language, customer type, or company configuration.

The RTM selection logic is in the calling `.RWN` program (encrypted) and possibly in
`BKACTRPT.MKD` (user-saved report configuration records).

## AP T7 Reports (Most Upgraded Module)

AP has 9 T7 RTMs — more than any other module. These correspond to the T7 AP check
printing workflow (`t7apb.rwn`, `t7aph.rwn`):
- Check form templates with MICR encoding, signature line, amount-in-words, etc.
- T7 generation needed for new paper sizes or multi-company configurations

## Key Files

- `samples/rtm_by_module.csv` — complete 1,734-row RTM inventory with gen + module classification
- Script: `scripts/catalog_rtm_by_module.py`
