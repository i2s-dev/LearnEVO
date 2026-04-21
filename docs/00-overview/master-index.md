# EvoERP Master Index — Every Operation, One Table

Status: verified (auto-generated from the extracted evidence).

Source CSV: `../../samples/master_index.csv` (759 rows).

## What this file is

The single merged catalog of **every operation that EVO can perform**,
joining:

- The 554 menu codes extracted from the `.RUN`/`.RWN` string dumps
  (`samples/menu_codes.csv`).
- The 636 help-topic pages found in `EvoHELP.CHM` (one per menu code).
- The DFM form for each operation (when one exists), from the
  1,109-form DFM inventory.

## Coverage

| Source | Codes |
| ------ | ---: |
| In both menu-code dump and help file | **431** |
| In menu-code dump only (no help page found) | 123 |
| In help file only (no compiled `.RUN`/`.RWN` string found) | 205 |
| **Total distinct menu codes** | **759** |

### Why the discrepancy?

- **"Menu only"** = mostly legacy `T6/BK` utility programs whose help
  pages were either renamed or never shipped. Some are clearly
  internal / test operations.
- **"Help only"** = either (a) recently-added operations whose compiled
  module lives only in an encrypted `.RWN` (so our string dump found
  nothing readable), or (b) feature names documented in help but
  implemented inside a multi-operation program (no individual menu code
  shows up in strings).

## Big numbers, assembled

| Dimension | Count |
| --------- | ----: |
| **Total user-facing operations** | 759 (from menu codes + help pages) |
| **Database tables** | 659 |
| **Database fields** | 24,113 |
| **UI forms (DFM)** | 1,109 |
| **Compiled program modules** (RWN + RUN + DCY) | 2,439 |
| **Report templates** (RTM + btm) | 959 |
| **Help topics** (in EvoHELP.CHM) | 779 |
| **Data files per company** (Btrieve `.B`) | 649+ |
| **Companies seen in this install** | 9 active + 3 system + 3 backup |

## How to use this index

The master CSV is searchable in any spreadsheet or `grep`. Columns:

| Column | Meaning |
| ------ | ------- |
| `code` | `XX-Y[-Z]` menu code |
| `module` | 2-letter module (first component of `code`) |
| `description` | Short description (from menu-code match or help title) |
| `rwn/run_modules` | Programs that echo this code in their strings |
| `dfm_forms` | UI form filename(s) for this code |
| `help_title` | Help-page title from the CHM |

Example: to find the full picture of `AR-C` (Record Payments):

```
grep ^AR-C, samples/master_index.csv
```

Returns:
- `description` = Record Payments
- `rwn/run_modules` = `BKARC;T6ARC`
- `dfm_forms` = `T7ARC.DFM`
- `help_title` = Record Payments

## The 205 "help-only" codes worth exploring

Because these are documented in the help file but we couldn't find a
matching readable module, they're the best candidates for understanding
what **the current encrypted `.RWN` generation adds beyond the legacy
`.RUN` era**. Sampling from the index:

- `AM-R` Out Of Balance Report
- `AM-S` Purge Or Archive Gl Journ
- `AM-T` Archive Gl Transaction De
- `AP-C` Enter Purchase Order Invoices (but AP-C is missing from
  menu code dump — so AP-C is a T7-only addition)
- (full list in the CSV)

Knowing this lets us prioritize: if a business question is about any
of the 205 "help-only" codes, the answer lives only in the live system
plus the CHM content — we can't find it in the plaintext `.RUN`
string dump.
