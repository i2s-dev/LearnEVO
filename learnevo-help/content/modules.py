"""
Per-module deep-dive pages. Each module gets:
- Purpose / scope
- Menu codes (with links)
- Database tables (with links)
- Forms (with links)
- Workflows
- Related modules
- Key files and programs

Most of this is auto-filled by the build script; this file holds the
HAND-WRITTEN narrative for each.
"""

MODULE_NARRATIVES = {

"AR": """
## What it does

Accounts Receivable manages everything related to **what customers owe
you** and **how they pay**: customer master records, invoices, statements,
aging, interest, sales taxes, deposits, and dunning.

## Core concept

Each customer exists as a single row in [[table-BKARCUST|BKARCUST]] with
106 fields. An invoice is a `BKARINV` header + one-or-more `BKARINVL`
lines. A payment is a `BKARCHKF` check that links back to one or more
invoices. When an invoice is fully paid, it moves from `BKARINV` to
`BKARHINV` (history) during `AM-K (Archive AR)`.

## Typical workflow

```
AR-A Enter Customer
  ↓
SO-A Create Sales Order
  ↓
SO-F Print Invoice           ← crosses the module boundary into SO
  ↓
AR-B Post Invoice to AR
  ↓
AR-E Print Statement (monthly)
  ↓
AR-C Record Payment (when received)
  ↓
AR-D Charge Interest (if overdue)
  ↓
AM-K Archive after N years
```

## Common reports

- `AR-F` Aging (current/30/60/90/over)
- `AR-E` Statements
- `AR-G`/`AR-H`/`AR-I`/`AR-J` Customer listings
- `AR-K` Sales tax report
- `AR-N` Deposits

## Integration with other modules

- **[[module-SO|SO]]** creates the invoices that AR posts.
- **[[module-GL|GL]]** receives every AR transaction (AR ↔ Cash, AR ↔
  Sales Rev, AR ↔ Tax, AR ↔ Bad Debt).
- **[[module-CS|CS]]** (Commission System) reads AR invoices to compute
  commissions earned by salespeople.

## Admin defaults

See `AD-E (Accounts Receivable Defaults)` to configure:
- Default receivable GL account
- Interest rate and grace period
- Statement format preferences
- Taxable/non-taxable defaults
""",

"AP": """
## What it does

Accounts Payable manages **what you owe vendors** and **how you pay
them**: vendor master, invoices (vouchers), scheduled payment dates,
pro-forma registers, check runs, 1099s, aging, and history.

## Core concept

Each vendor is a row in [[table-BKAPVEND|BKAPVEND]]. An AP invoice is
called a **voucher** (tradition from older accounting) and is stored in
`BKAPINVT` + `BKAPINVL`. Checks live in `BKAPCHKF` (current) and
`BKAPCHKH` (history).

## Typical workflow

```
AP-A Enter Vendor
  ↓
PO-A Create PO (optional)
  ↓
PO-C Receive
  ↓
AP-B Enter Voucher (references PO or stand-alone)
  ↓
AP-F Pick Vouchers to Pay
  ↓
AP-G Print Pro Forma Register
  ↓
AP-H Print Checks (the commit step)
  ↓
AP-R Payment History
  ↓
AP-S 1099 Forms (year end)
```

## Key reports

- `AP-I` Aging
- `AP-E` Due by date
- `AP-G` Pro-forma register
- `AP-R` Payment history
- `AP-S` 1099 forms

## Check formats

EVO supports four check formats (stored in `BKYSMSTR.bkys.yn[48]`):
- `1` Classic dot-matrix
- `2` Laser 3-part (check on top)
- `3` Laser 3-part (check on bottom)
- `4` Laser 3-part (check in middle)

Each format uses a different RTM (`banks.rtm`, `bkaph1.rtm`, etc.).
Custom formats like `I2SCHK1.rtm` override the default.

## Integration

- **[[module-PO|PO]]** supplies the received-but-unvouchered list.
- **[[module-GL|GL]]** receives AP postings (Expense ↔ AP at voucher
  entry; AP ↔ Cash at check).
- **[[module-IN|IN]]** — received inventory vouchers bump `BKIC_PROD_LSTC`
  (last cost).

## Check-printing deep dive

The AP check printer is one of the few programs we have in plaintext:
`Bkaph.src` (dot-matrix) and `Bkapha.src` (laser). Key logic:

- Reads the AP check format flag from `BKYSMSTR.bkys.yn[48]`.
- Chains to the correct sub-program based on format.
- Writes MICR check data + reference stubs for each voucher paid.
- Calls `EXEC_RB` with the appropriate RTM.
- Updates `BKAPCHKF` → `BKAPCHKH` after successful print.

See [[recipe-print-checks]] for the user-facing walk-through.
""",

"IN": """
## What it does

Inventory manages **what you have, where it is, and what it's worth**.
This is the largest module by menu count (40 ops) and one of the most
intricately integrated.

## Item classification

Each item in [[table-BKICMSTR|BKICMSTR]] has a **Type** (`BKIC_PROD_TYPE`):

| Code | Meaning |
| ---- | ------- |
| R | **Raw / Purchased** — bought outright |
| M | **Make** / Manufacturing — produced via WO |
| F | **Finished** — end product |
| A | **Sub-assembly** — intermediate assembly |
| N | **Non-inventory** — service, labor, etc. |
| S | **Service** — billable service item |

The Type drives most business logic elsewhere: only M/A items can be
WO parents; only R/F can receive POs; N items skip inventory tracking.

## Costing methods

Item-level cost method (`BKIC_PROD_CST_METH`):

| Code | Method | Cost updated by |
| ---- | ------ | --------------- |
| S | Standard | Manual (IN-Q) |
| A | Average | PO receipts auto-adjust |
| F | FIFO | Layer tracking in BKICLOT |
| L | LIFO | Layer tracking |
| T | Last | Every receipt overwrites |

The active cost lives in `BKIC_PROD_AVGC`, `BKIC_PROD_STDC`,
`BKIC_PROD_LSTC`.

## Key tables

- [[table-BKICMSTR|BKICMSTR]] — item master (16 BKIC* tables total)
- `BKICLOC` — per-location quantities
- `BKICDIM` — size/dimension variants
- `BKICALTD` / `BKICALTP` — alternate part numbers
- `BKICLOT` — lot tracking layers
- `MTICMSTR` — second-generation master (co-exists with BKICMSTR)

## Multi-location

Enable multi-location in `AD-D (Inventory Defaults)`. Each location has
its own quantities in `BKICLOC`, and the item master just shows summed.

## Typical workflow

```
IN-A Enter Items (master data)
  ↓
PO-C Receive (adds to inventory)
  ↓
SO-C Ship (removes from inventory)
  ↓
IN-E Transfer (move between bins)
  ↓
PI-* Physical count (verify)
  ↓
IN-G Adjust (correct discrepancies)
```

## Reports

- `IN-D` Reorder report (below ROP)
- `IN-I` Valuation (current worth)
- `IN-O` User-defined inventory transactions
- `IN-L-A` Print location summary

## GL impact

Inventory moves always post to GL:

- Receipt: Inventory ↔ AP/PPV
- Issue to WO: Inventory ↔ WIP
- Finished receipt: WIP ↔ Inventory
- Adjustment: Inventory ↔ Adjustment account
- Sale: COGS ↔ Inventory

## Related

- [[module-PI|PI - Physical Inventory]]
- [[module-PO|PO - Purchase Orders]]
- [[module-WO|WO - Work Orders]]
- [[recipe-enter-item]]
- [[recipe-adjust-inventory]]
""",

"SO": """
## What it does

Sales Orders covers the **customer-facing order lifecycle** — from
quotation through order entry, picking, shipping, invoicing, and
RMAs. 48 menu ops, 69 forms — the largest module by UI surface.

## Document lifecycle

```
Quote (SO-P-A)
  ↓ accepted
Sales Order (SO-A)
  ↓ produced/picked
Pick Ticket (SO-C)
  ↓ physically picked
Packing Slip (SO-C)
  ↓ shipped
Invoice (SO-F)
  ↓ posted to AR
(AR module takes over)
```

## Sales levels

Multiple price levels supported per item, in `BKSLEVEL` (422 fields!).
Each customer has a default level (`BKARCUST.BKAR_SAL_LVL`), plus per-
item overrides.

## Features & Options configurator

See [[subsystem-evofno]]. If an item has `BKIC_PROD_FNO_FLAG = Y`,
entering it on an SO launches a modal dialog that walks through
Feature (category, e.g. "Color") and Options (choice, e.g. "Red"),
building a configured line.

## Variant screens

- `SO-A` base
- `SO-P-A` quote variant
- `SO-P-F` RMA (return) variant
- `SO-J` recurring SO
- `SO-Q` quick-entry
- `SO-T` in-house

## Multiple invoice formats

Four SO invoice formats stored in RTM variants: `bksof1.rtm` through
`bksof4.rtm`. Pick based on customer requirements (their PO number,
line-item detail, price display, etc.).

## Tables

- `BKARINV` — SO header (same table is reused for invoices — status
  field distinguishes)
- `BKARINVL` — SO lines
- `BKARINVI` — Invoice shipping detail
- `BKARINVV` — Invoice variants
- `BKSOHLOT` / `BKSOHSER` — Lot / serial shipping records
- `BKSONOTE` — order notes
- `BKSOPO` — links SO to drop-ship PO

## Integration

- **AR** — posted invoices land here
- **IN** — ship events decrement on-hand
- **CS** — commissions earned
- **PO** — drop-ships auto-generate POs
- **WO** — make-to-order triggers a WO
""",

"PO": """
## What it does

Purchase Orders manages procurement — creating POs, receiving against
them, and feeding `AP` for payment. 29 menu ops.

## PO lifecycle

```
RFQ (optional, RF-A)
  ↓ quoted
Quote (PO-E)
  ↓ accepted
Purchase Order (PO-A)
  ↓ approved
Expected receipt (PO-C)
  ↓ received physically
Receipt (PO-C) → inventory
  ↓ invoiced by vendor
Voucher (AP-B) linked to PO
  ↓ approved & paid
Check (AP-H)
```

## Drop-ship POs

POs created from a drop-ship SO line link back to `BKSOPO`. When
vendor ships direct to customer, the PO receipt simultaneously closes
the SO line.

## Approval workflow

If approval limits are configured (`BKAPAPO.BKAP_APO_APRV_*`), POs
over a threshold need approval before receipt.

## Key tables

- `BKAPPO` — PO header
- `BKAPPOL` — PO lines
- `BKAPAPO` — APo (approved POs)
- `BKAPAPOL` — APo lines
- `BKAPHPO` / `BKAPHPOL` — History

## Receiving

`PO-C` walks the receiver through:
1. Select PO or blanket
2. Pick lines being received
3. Enter actual quantity (defaults to ordered, override for partial)
4. Enter lot / serial if applicable
5. Post → inventory increment + accrual GL entry

## Integration

- **AP** — picks up received-unvouchered for payment
- **IN** — receipt increments on-hand
- **GL** — receipt: Inventory ↔ Accrued AP; Voucher: Accrued AP ↔ AP
""",

"WO": """
## What it does

Work Orders (manufacturing orders) is the **core production module** —
it's what makes EVO an ERP not just accounting. 31 menu ops, 68 forms,
30 dedicated tables.

## Why WO is special

A work order is a **snapshot** of how a specific unit of production
will be built. When you release a WO:

- The **BOM is copied** from the master into `WOBOM` (per-WO).
- The **routing is copied** into `WOROUT` (per-WO).

This means a WO, once released, is **locked to its plan**. Changes to
the master BOM won't retroactively change in-progress WOs.

## WO status lifecycle

```
Open (WO-A entered)
  ↓
Released (WO-B; BOM/routing locked)
  ↓
In Production
  ↓ labor entered (DC-A, WO-E)
  ↓ materials issued (DC-B, WO-G)
Complete (WO-C; finished qty received)
  ↓
Closed (WO-D; variances posted, costs locked)
```

## Cost tracking

As the WO progresses, costs accumulate:

- **Material** — component issues at their item cost
- **Labor** — hours × labor rate (from operation)
- **Overhead** — applied at absorption rate (from cost center)

Actual vs. planned:

- Planned = BOM cost × qty + sum(routing ops × labor rate)
- Actual = actual issues + actual labor + actual overhead
- **Variance** posts to GL at close

## Tables (the 30-table family)

```
WORKORD         WO header
WOBOM           Per-WO BOM
WOBOMCHG        BOM changes within WO
WOBOMHRM        BOM hierarchy (multi-level)
WOBOMREM        BOM removed items
WODATE          Date tracking
WOHBOMR/WOHBOMM WO BOM history
WOHLABOR        WO labor history
WOHMAT          WO material issue history
WOHRECV         WO receipt history
WOHROUT         WO routing history
WOLABOR         Current labor
WOLABRPT        Labor reports
WOMAT           Current material issues
WORECV          Receipts
WORKACHG        Actual changes
WORKCHG         Changes
WORKCTR         Work centers
WORKHORD        Hold orders
WORKORD         Main WO table
WORKSORD        Sub-orders (sub-WOs)
WOROCHG         Routing operation changes
WOROUT          Per-WO routing
WOROUTMP        Routing temp
WOSROUT         Sub-routing
```

## Reports

- `WO-L-A` Status report (critical!)
- `WO-L-F` Shortage report (what components are short)
- `WO-L-B` Schedule report
- `JC-A` Job cost (profitability per WO)

## Scheduling

Four scheduling modes, help topics documented:

- **Finite** — fully constrained by work-center capacity
- **Infinite** — no capacity constraint (plan as if unlimited)
- **Lead-time** — based on fixed lead times per op
- **Manual** — user-entered dates

## Related

- [[module-BM|BM - Bill of Materials]]
- [[module-RO|RO - Routings]]
- [[module-DC|DC - Data Collection]]
- [[module-JC|JC - Job Costing]]
- [[recipe-work-order]]
""",

"GL": """
## What it does

General Ledger is **the accounting book of record** — the chart of
accounts, journal entries (both auto-generated by sub-ledgers and
manual), trial balance, financial statements, and fiscal period
control.

## The six GL master tables

- `BKGLCCOA` — **Chart of Accounts** (account numbers, names, types)
- `BKGLACHK` — Accounts and current balances
- `BKGLAGJL` — General journal (auto-posted from sub-ledgers)
- `BKGLAGJR` — General journal recurring templates
- `BKGLATRN` — **All GL transactions** (the detail)
- `BKGLCHK` — Check register

## The two posting patterns

**Automatic (from sub-ledgers):** AR/AP/IN/SO/PO/WO/PR — each of these
modules writes GL entries as part of its normal workflow. The entries
flow through `BKGLTEMP` (staging) and get consolidated by `AM-I`.

**Manual (GL-B):** typed journal entries. Admin-only. Used for
adjustments, accruals, corrections.

## Account structure

Typical chart:
- 1xxxx — Assets
- 2xxxx — Liabilities
- 3xxxx — Equity
- 4xxxx — Revenue
- 5xxxx — COGS
- 6xxxx — Expenses

Sub-accounts (departments) add a dash-suffix:
- `12000-00` — Cash, corporate
- `12000-10` — Cash, division 10

## Fiscal periods

Set up in `AM-N (Maintain GL Fiscal Periods)`. Each period has:
- Start / end dates
- Open/closed flag
- Period number within fiscal year

Trial balance must balance to zero in every period.

## Financial statements

- `AM-E` Standard financial statement layout (header/detail/total
  style)
- `AM-F` Custom statement builder

Layouts stored in `BKGLxxxx` config tables. Running a statement reads
the layout + executes SELECTs against `BKGLATRN` summed by account.

## Consolidation

- `AM-G` Consolidate financials across companies (when you have
  multiple companies in the same org)
- `AM-I` Consolidate GL detail (pulls sub-ledger transactions into
  the permanent ledger)

## Reports

- `GL-X` Trial balance
- `GL-Y` Balance sheet
- `GL-Z` Income statement (custom format)
- `AM-R` Out-of-balance report (finds broken entries)

## Key dates

- **Fiscal year start** — set in `BKSYMSTR.BKSY_GL_FYRBGN`
- **Current period** — `BKSY_GL_PERIOD`
- **Period-end close date** — `BKSY_GL_PEDTE`

Posts AFTER the close date aren't allowed; admins can temporarily
reopen a period via `AM-A`.

## Related

- [[module-AM|AM - Archive/Maintenance]]
- [[module-AD|AD - Admin Defaults]]
- [[recipe-month-end-close]]
""",

"PR": """
## What it does

Payroll. 29 menu ops, 16 tables, and the table with the **most
fields of any** (`BKPRGLFL` has 664 fields for payroll GL mapping).

## Scope

Full US-based payroll:

- Employee master (`BKPRMSTR`, 384 fields)
- Time & attendance integration (from DC or external)
- Federal / state / local tax calc (`BKPRTCFG`, `BKPRW2`)
- Deductions (health, 401k, garnishments)
- Direct deposit
- Check printing
- Quarterly 941, year-end W-2
- GL distribution per employee / per cost center

## Workflow

```
PR-A Enter Employees
  ↓
PR-B Enter Time (or import from DC)
  ↓
PR-C Calculate Payroll
  ↓
PR-D Print Pre-check Register (proof)
  ↓
PR-E Print Checks / DD advices
  ↓
PR-F Post to GL
  ↓ quarterly
PR-G Print 941
  ↓ annually
PR-H Print W-2
```

## Tax calc

Uses the `BKPRTCFG` table (205 fields) plus federal tax tables
(shipped with updates) to compute per-paycheck:
- Federal withholding
- Social Security (6.2%)
- Medicare (1.45%)
- State income tax (per state rules)
- Local tax (where applicable)
- SUTA, FUTA employer portions

Rates are updated via `EvoPRupd.RWN` when the IRS / state changes
them.

## Direct deposit

Bank info per employee in `BKPRMSTR.BKPR_DD_*`. ACH file generation
format via `J7ADTNACHA` or custom variants.

## Related

- [[module-GL]]
- [[module-CS|CS - Commissions]] — posts to PR for payout
- [[module-DC|DC]] — labor data source
""",

# Short stubs for remaining modules - filled in by build script via schema/menu data
"BM": """
## What it does

Bill of Materials defines what components go into what assemblies. It is
the structural backbone of manufacturing at i2 Systems — every Work Order
and MRP run depends on BOM data.

**Scale:** 208,686 BOM lines linking 29,714 parent assemblies to 27,415
unique components (average 7.0 components per parent).

## Core table: BKBMMSTR

Each row is one parent-child relationship:

| Field | Meaning |
|-------|---------|
| `BKBM_PART_PARENT` | Assembly item code (FK to BKICMSTR) |
| `BKBM_PART_COMP` | Component item code (FK to BKICMSTR) |
| `BKBM_PART_SEQ` | Line sequence within the parent BOM |
| `BKBM_PART_QTYPER` | Quantity per parent (8-decimal precision) |
| `BKBM_PART_UM` | Unit of measure for quantity |
| `BKBM_PART_REFDES` | Reference designator (PCB/electronics use) |
| `BKBM_PART_SCRAP` | Scrap allowance percentage |
| `BKBM_PART_PHTYPE` | Phantom flag — phantom assemblies explode through |
| `BKBM_PART_ECO` | Engineering change order reference |

## Engineering vs Production BOM

EvoERP maintains separate engineering (`BKBMAVAL`) and production (`BKBMMSTR`)
BOMs. At i2 Systems, BKBMAVAL and BKBMAMTR are empty — the production BOM
is the only active one.

`BKBMEMTR` (engineering mirror, 0 rows) would hold an in-progress ECO copy
that gets approved and promoted to BKBMMSTR.

## Menu operations

| Code | Operation | Notes |
|------|-----------|-------|
| `BM-A` | Enter BOM | Main entry — add/edit component lines |
| `BM-C` | Print Where-Used | "Which assemblies use this component?" |
| `BM-D` | Availability | "Can I build N units with current stock?" |
| `BM-E` | Global Replace | Swap one component for another across all BOMs |
| `BM-F` | Global Delete | Remove component from all BOMs |
| `BM-H` | Print BOM at Average Cost | Explosion with current costs |
| `BM-J` | Approved Substitutes | Alternate parts (BKSBPART table) |

## Integration

- **[[module-WO|WO]]** — when a WO is released, its BOM is copied from
  BKBMMSTR into `WOBOM` (per-WO snapshot). Changes to the master BOM do
  not affect in-progress WOs.
- **[[module-MR|MR]]** — MRP explodes BOMs to compute component demand.
- **[[module-ES|ES]]** — Estimating can pull BOM for cost roll-up.
""",

"MR": """
## What it does

Material Requirements Planning (MRP) closes the loop between demand and
supply. It reads every open Sales Order, WO demand, and safety stock
requirement, nets them against open POs and WOs plus on-hand inventory,
explodes the BOMs, and generates a recommended action list.

**Scale:** 37,137 records in `MTMRP` — the live planning table. i2 Systems
runs in pure-demand mode (no forecasting, BKMRPFC=0).

## MTMRP action codes

| Code | Count | Meaning |
|------|------:|---------|
| *(blank)* | 31,437 | Demand loaded, awaiting action |
| `BUY` | 2,559 | Planned purchase order |
| `REVIEW` | 2,311 | Requires manual review |
| `MAKE` | 772 | Planned work order |
| `DELSENS` | 45 | Delay-sensitive — supply behind demand |
| `EXPSENS` | 13 | Expedite-sensitive — demand urgent |

BUY >> MAKE (2,559 vs 772): i2 Systems buys more than it makes, consistent
with a value-added assembly/kitting operation.

## The core program: BKMRF.SRC

Unusually, the MRP calculation engine is in plaintext source (`BKMRF.SRC`
on the network share). It is a TAS Pro 6-era program still in active use.
Key logic:
- Reads BKSYMSTR for fiscal calendar and settings
- Explodes BOM levels top-down via BKBMMSTR
- Reads BKICLOC for on-hand, BKAPPO for open POs, WORKORD for open WOs
- Writes action rows to MTMRP

## Typical workflow

```
MR-A  Run MRP (triggers BKMRF or BKMRP)
MR-B  Review suggested POs    → BKMRPPO
MR-C  Review suggested WOs    → BKMRPSW
MR-J  Confirm planned PO      → creates BKAPPO/BKAPPOL
MR-K  Confirm planned WO      → creates WORKORD
MR-L  Clear MRP output        → purges MTMRP
```

## Integration

- **[[module-BM|BM]]** — BOM explosion is the heart of MRP
- **[[module-PO|PO]]** — confirmed planned POs become real POs
- **[[module-WO|WO]]** — confirmed planned WOs become real WOs
- **[[module-SO|SO]]** — SO demand drives MRP demand horizon
""",

"DC": """
## What it does

Shop-floor Data Collection (DC) captures labor, material issues, scrap, and
WO receipts at the point of work — from handheld scanners or barcode
terminals — so the system stays current without manual data entry.

**At i2 Systems:** DC is installed but not actively used (BKDCCFG=0 — no
data collection configuration). Shop floor data is entered via WO module
menus instead.

## Architecture

DC has 7 database tables:

| Table | Purpose |
|-------|---------|
| `BKDCLAB1`–`BKDCLAB5` | 5 identical pipeline stages for labor capture (50f each) — Btrieve-only, not in PSQL layer |
| `BKDCSHFT` | Shift schedule master (34f, 3 shift slots) — 1 record |
| `BKDCCFG` | Data collection configuration (7f) — empty |

The 5 `BKDCLAB*` tables form a pipeline: data flows through stages 1→5 as
it is validated and posted to WO labor records. Each stage is identical in
schema (`DATE+EMP+WO+OPER` primary key) — the stage number is the
differentiator.

The tables use **Btrieve direct-access only** — they don't appear in the
PSQL ODBC relational layer (`SELECT COUNT(*) FROM BKDCLAB1` returns ERR).
This is deliberate: real-time handheld data collection bypasses the SQL
engine for speed.

## Integration

- **[[module-WO|WO]]** — labor entries and material issues post directly to
  `WOLABOR` and `WOMAT`
- **[[module-PR|PR]]** — time totals from DC feed payroll hours
""",

"QC": """
## What it does

Quality Control tracks incoming and in-process inspections — from setting
up inspection plans per item to recording results and issuing certificates
of compliance (CoC).

**Scale:** 53,300 receive events in `BKQCMSTR` with a 1.73% rejection rate.
i2 Systems actively uses QC for incoming inspection on purchased components.

## Core tables

| Table | Fields | Purpose |
|-------|--------|---------|
| `BKQCMSTR` | 14 | QC inspection event record (one per receive + inspection) |
| `BKQCTRAN` | 21 | Per-line inspection detail with pass/fail and quantities |
| `ISQCMTHD` | 44 | QC method library (test procedures, 3,367-byte record) |
| `ISQCRSLT` | 57 | QC result/specification per method (min/max as strings) |
| `ISQCSPEC` | 57 | QC specification master (identical schema to ISQCRSLT) |
| `ISQCAMST` | 14 | QC receiving master (alternate inspection table) |
| `ISQCATRN` | 20 | QC receiving transaction detail |
| `OPQCDESC` | 10 | Per-operation QC descriptions |
| `QCCODES` | 2 | Inspection result codes |

## Workflow

```
PO receipt arrives  →  QC-A: Create inspection record (BKQCMSTR)
                    →  QC-B: Enter results line-by-line (BKQCTRAN)
                    →  QC-C: Print certificate of compliance
```

The QC module hooks into the PO receiving process: when a PO line is
received, it can trigger QC inspection before the inventory is released.
Items on hold pending QC show up separately in the inventory availability
picture.

## Integration

- **[[module-PO|PO]]** — QC inspection triggers on PO receipt
- **[[module-IN|IN]]** — items under QC hold are not available for issue
- **[[module-WO|WO]]** — in-process QC can be triggered per routing operation
""",

"JC": """
## What it does

Job Costing cross-references manufacturing costs (from Work Orders) against
Job Codes — allowing management reporting by project, contract, or
cost-center that spans multiple WOs.

**Scale:** 45,862 job codes in `ISJOB` (all blank STATUS — passive reference
data, not actively managed via menu). 142 business scorecard records in
`ISJBSF`.

## Core concept

A Job Code (`ISJOB`) is a free-form grouping label attached to WOs. When
a WO is assigned a job code, its costs roll up to that job. JC-A generates
the summary by job showing planned vs. actual labor, material, and overhead.

## Tables

| Table | Records | Purpose |
|-------|--------:|---------|
| `ISJOB` | 45,862 | Job master — code + description + status |
| `ISJBSF` | 142 | Business scorecard — key metrics per job/period |

ISJOB has only 3 meaningful fields: `IS_JOB_CODE`, `IS_JOB_DESC`, and
`IS_JOB_STATUS`. All 45,862 rows have blank STATUS — the codes are a
historical reference list rather than actively managed records.

## Key report

**JC-A** (Job Cost Report) — for a range of job codes, lists each WO
assigned, then shows:
- Planned labor hours and cost (from `WOROUT` routing)
- Actual labor hours and cost (from `WOLABOR`)
- Planned material cost (from `WOBOM`)
- Actual material cost (from `WOMAT` issues)
- Variance

## Integration

- **[[module-WO|WO]]** — WO header has a Job Code field; all WO cost
  transactions carry the job code forward
- **[[module-GL|GL]]** — job costs can post to job-specific GL accounts
""",

"CS": """
## What it does

Commissions — calculates and reports salesperson commissions derived from posted
AR/SO invoices. Supports multiple commission structures: flat rates, price-code
commissions, and contract commissions. Handles primary + secondary salesperson
splits and year-end commission transfer.

## Menu operations

| Code | Operation |
|------|-----------|
| CS-A | Enter Salespersons |
| CS-B | View Salesperson Info |
| CS-C | Print Salesperson Info |
| CS-D | Transfer Sales Commissions |
| CS-E | Print Commission Detail |
| CS-F | Print Commission Summary |
| CS-G | Enter Sales Rep Links |
| CS-H | Import Sales Rep Links |
| CS-K | Enter Price Code Commissions |
| CS-L | Print Price Code Commissions |
| CS-M | Enter Contract Commissions |
| CS-N | Print Contract Commissions |
| CS-O | Print Commissions Earned Detail |
| CS-P | Print Commissions Due Summary |
| CS-Q | Commission Year End Routine |
| CS-R | Sales Commission Defaults |

## Key table

`ISPRSALE` (87 fields, IS_PR_SALE_* prefix) — sales rep commission master:
commission rate, commission type, pay period, earned/paid totals.
Stores commission amounts per salesperson per period derived from AR/SO activity.

## Integration

- **[[module-AR|AR]]** — commissions sourced from posted invoices (BKARINV)
- **[[module-SO|SO]]** — salesperson code on SO header drives commission assignment
- **[[module-PR|PR]]** — commission earned amounts feed payroll (CS-D Transfer)
""",

"ES": """
## What it does

Estimating builds pre-sale quotes with full BOM/routing cost roll-up —
material, labor, overhead, and markup — before committing to a Sales Order
or Work Order.

**Scale:** 6,894 active quotes with 462,727 line items (~67 lines per quote).
An additional 5,816 archived quotes exist in the IS-era ISESTAQT table.
i2 Systems uses ES heavily as the primary pre-sale tool.

## Quote lifecycle

```
ES-A  Enter Estimate  →  BKESTQT (header) + BKESTQTL (lines)
                         same schema as BKARINV/BKARINVL
ES-E  Convert          →  creates SO (BKARINV) or WO (WORKORD)
ES-B  Print Estimate   →  customer-facing quote document
```

## Quote status codes (BKESTQT.BKAR_INV_INVCD)

| Code | Meaning | Count |
|------|---------|------:|
| `Y` | Active / open quote | 5,909 |
| `X` | Cancelled | 366 |
| *(blank)* | Unset / draft | 618 |

## Key tables

| Table | Records | Purpose |
|-------|--------:|---------|
| `BKESTQT` | 6,894 | Quote header — byte-for-byte BKARINV clone |
| `BKESTQTL` | 462,727 | Quote lines — byte-for-byte BKARINVL clone |
| `BKESTCFG` | 1 | Quote configuration singleton |
| `ISESTDTL` | 0 | Detailed cost breakdown per component (legacy path) |
| `ESTSUM` | 0 | Legacy DBA estimate summary — unused in T7 era |

## Cost structure

Each quote line can carry 10 quantity breaks with separate material, labor,
overhead, setup, op, and misc costs per break. The `ISESTDTL` table (when
used) holds 10 qty-break × 7 cost types = 70 cost fields per component.

At i2 Systems, ISESTDTL=0 — quotes are stored as simple BKESTQT/BKESTQTL
records without the detailed cost breakdown, consistent with quote-document
mode (pricing set manually rather than cost-rolled-up).

## Integration

- **[[module-SO|SO]]** — ES-E converts a quote to a Sales Order
- **[[module-WO|WO]]** — ES-E can also convert directly to a WO
- **[[module-BM|BM]]** — BOM pull populates the component list
- **[[module-PO|PO]]** — vendor RFQ support via BKRFQ table
""",

"SR": "## What it does\n\nService / Repair — tracks in-bound service orders (customer equipment), labor, parts consumed, and warranty. Adjacent to RMA flow in SO.\n",

"PI": """
## What it does

Physical Inventory (PI) manages the process of counting actual on-hand
inventory and reconciling the system quantities. Supports both full physical
counts and cycle counting.

**Scale:** 250 PI sessions on record. Current snapshot: 22,279 bin-location
count records (PIBINLOC) and 40 lot records (PIBINLOT) — PI is actively used
at i2 Systems.

## Workflow

```
PI-A  Capture Frozen Inventory
      → snapshots BKICMSTR on-hand quantities into BKPIFROZ
      → creates a BKPIMSTR session record (YEAR+QTR+DESC)

PI-C  Enter Count Tags
      → count tags entered in BKPIPHYS (one per item+location+bin)
      → PIBINLOC tracks the bin-level count

PI-G  Update Actual Inventory (post variances)
      → compares BKPIPHYS count vs BKPIFROZ freeze
      → posts INVTXN adjustment transactions (type A)
      → updates BKICLOC on-hand quantities

PI-H  Purge Physical Inventory
      → clears BKPIFROZ and BKPIPHYS for the session
```

## Tables

| Table | Records | Purpose |
|-------|--------:|---------|
| `BKPIMSTR` | 250 | PI session header (YEAR + QTR + DESC) |
| `BKPIFROZ` | — | Frozen snapshot of on-hand at count start |
| `BKPIPHYS` | — | Count tag entry (actual count per item) |
| `PIBINLOC` | 22,279 | Bin-location count records |
| `PIBINLOT` | 40 | Lot-tracked items in current count |
| `BKPILOT` / `BKPILCNT` | — | Lot frozen/counted (10f each) |
| `BKPISER` / `BKPISCNT` | — | Serial frozen/counted (10f each) |

## Cycle count support

PIBINLOC has `YEAR`/`QTR` cycle fields and last-count dates — supporting
partial (cycle) counts in addition to full physical inventory.

## Integration

- **[[module-IN|IN]]** — PI variances post as `INVTXN` type A adjustments,
  updating BKICLOC on-hand
- **[[module-GL|GL]]** — PI adjustments generate GL journal entries via the
  inventory variance accounts in BKSYMSTR
""",

"SH": "## What it does\n\nShipping — pack, ship, label, track. Integrates with UPS/FedEx/USPS APIs. Labels via `J7DCMatLabels` and handheld flows.\n",

"ED": """
## What it does

Electronic Data Interchange (EDI) handles X12 electronic order exchange with
trading partners. EvoERP does **not** parse X12 directly — all translation
is handled by the external **CandoEDI** middleware.

**At i2 Systems:** ED is licensed but completely idle (BKEDIH=0, BKEDIL=0,
BKEDIDUN=0, BKEDMSTR has 1 config record). No electronic orders are being
received or sent.

## Architecture: CandoEDI middleware

```
Trading partner  →  X12 850 PO   →  CandoEDI  →  DBASO.IN (flat)
DBASO.IN  →  ED-B (import)  →  BKEDIH + BKEDIL (staging)
BKEDIH/BKEDIL  →  ED-C (review)  →  ED-D (convert)  →  BKARINV/BKARINVL
```

Outbound:
```
BKARINV/BKARINVL  →  ED-E (export)  →  DBASO.OUT → CandoEDI → X12 810/855
WO shipment  →  DEP module  →  DBASHIP.OUT → CandoEDI → X12 856 ASN
```

## X12 transaction sets

| Set | Type | Direction |
|-----|------|-----------|
| 850 | Purchase Order (customer PO) | Inbound |
| 860 | PO Change | Inbound |
| 810 | Invoice | Outbound |
| 855 | PO Acknowledgement | Outbound |
| 856 | ASN (DEP module) | Outbound |

X12 version numbers (004010, 005010, etc.) are **not** in EvoERP binaries —
they are configured entirely within CandoEDI.

## Tables

| Table | Records | Purpose |
|-------|--------:|---------|
| `BKEDIH` | 0 | Inbound order staging header (84f, BKARINV clone) |
| `BKEDIL` | 0 | Inbound order staging lines (28f, BKARINVL clone) |
| `BKEDIDUN` | 0 | Trading partner DUNS ↔ customer mapping |
| `BKEDMSTR` | 1 | Config: CandoEDI path + our DUNS + counter |
| `BKEDNOTE` | 0 | Order notes |
| `BKEDPOST` | 0 | Export posting log |

## Integration

- **[[module-SO|SO]]** — converted EDI orders become SO records in BKARINV
- **[[module-DE|DE]]** — 856 ASN (advance ship notice) is generated by the
  DEP outbound compliance module, not by ED directly
""",

"SM": """
## What it does

System Maintenance — the broadest administrative module in EVO. Contains master
file setup (customers, vendors, classes, terms, tax codes, employees, shop
calendar), file maintenance / archive / purge operations, and miscellaneous
utilities. **Largest module by program count** (34 top-level buttons, 109+ forms).

## Key operation groups

| Group | Codes | Purpose |
|-------|-------|---------|
| Master file setup | SM-A–SM-H | Enter customers (t7ara), vendors (t7apa), classes, terms, taxes, employees, shop calendar |
| Contact master setup | SM-I (A–F) | Lead sources, territory codes, reminder types, class codes, date codes, quote-loss reasons |
| File maintenance | SM-J (A–V) | Archive/purge: WOs, PO history, QC, DC, estimates, SOs, invoices, GL journals; reconcile inventory; merge item/customer/vendor codes |
| User / system admin | SM-K | Evo User Settings (T7SMK.RWN) — user profile customization |
| Notes maintenance | SM-N | Note types, system notes, Classic↔Evo sync |
| Ship-via codes | SM-O | Enter ship-via codes (T7SMO.RWN) |

## Key tables

- `BKLOGON` — user login + access level master
- `ISJOB` (9f) — job/project cross-reference (SM-PF primary editor, 64 procs)
- `BKSYMSTR` (286f) — global system parameter singleton (company name, terms, defaults)
- `BKYSMSTR` (355f) — manufacturing system parameters (WO numbering, ISTS.CFG.*, YN slots)

## Integration

- **[[module-SY|SY]]** — SY handles user password and access security; SM handles master data
- **[[module-AM|AM]]** — AM handles GL/accounting period-end; SM-J handles operational archive/purge
- **[[module-GL|GL]]** — SM-C/D enter GL accounts and departments (cross-listed as AM-C/D)
""",

"AM": """
## What it does

Accounting Maintenance — period-end, fiscal year-end, GL setup, financial
statement formatting, and AP/AR/GL archive/purge operations. The critical-timing
module: these programs must be run in the correct order at month-end and year-end.
See [[recipe-month-end-close]] and [[recipe-year-end-close]].

## Menu operations

| Code | Operation |
|------|-----------|
| AM-A | Reset Period-End Close Date |
| AM-B | Fiscal Year End Routines |
| AM-C | Enter General Ledger Accounts |
| AM-D | Enter General Ledger Departments |
| AM-E | Format Standard Financial Statement |
| AM-F | Format Custom Financial Statements |
| AM-G | Consolidate Financials (multi-company) |
| AM-H | Change GL Account Codes |
| AM-I | Consolidate General Ledger Detail |
| AM-J | Purge/Archive AP History |
| AM-K | Purge/Archive AR History |
| AM-N | Maintain GL Fiscal Periods |
| AM-O | Purge/Archive Vendor Data |
| AM-P | Purge/Archive Customer Data |
| AM-Q | Enter Budget Amounts |
| AM-R | Out of Balance Report |
| AM-S | Purge/Archive GL Journals |
| AM-T | Archive GL Transaction Detail |

## Key tables

- `BKGLPER` — GL fiscal period master (open/close flags)
- `BKGLCOA` (65f) — chart of accounts
- `BKGLTRAN` — GL journal detail (source of all financial reports)

## Integration

- **[[module-GL|GL]]** — AM-A/B control the period locks that GL enforces on posting
- **[[module-AP|AP]]** — AM-J purges AP invoice and check history
- **[[module-AR|AR]]** — AM-K purges AR invoice history (complement to SA aging reports)
- **[[module-SM|SM]]** — SM-J handles operational archive (WO, PO, QC); AM handles accounting archive
""",

"AD": "## What it does\n\nAdmin Defaults — three screens that configure module-wide defaults:\n\n- `AD-A` General Ledger Defaults\n- `AD-B` Checking Account Defaults\n- `AD-C` Accounts Payable Defaults\n- `AD-D` Accounts Receivable Defaults (actually `AR-S`)\n\nValues stored in `BKSYMSTR` / `BKYSMSTR`.\n",

# ── Modules added Pass 310 (2026-06-25) to eliminate all 45 module stubs ──

"LC": "## What it does\n\nLot Control — assigns, tracks, and archives lot numbers for lot-controlled inventory items. Each lot has its own on-hand quantity, receipt date, expiration date, and cost. Full suite: `LC-A` Edit Lots, `LC-B` Assign Lot Control (per-item flag), `LC-C`/`LC-C2` Lot Listings, `LC-E` Lot Expiration, `LC-F` Lot Summary, `LC-G` Archive Lots.\n\nKey tables: `BKLCMSTR` (lot master), `BKLCLOC` (lot per-bin). See also [[module-SC|SC]] for the parallel serial-number module.\n",

"SC": "## What it does\n\nSerial Control — assigns and tracks unique serial numbers for serial-controlled items. Symmetric structure to [[module-LC|LC]]: `SC-A` Edit, `SC-B` Assign, `SC-C`/`SC-D` Listings, `SC-E` Archive. Serial numbers tie to specific customer shipments (SO allocations) for traceability.\n\nKey tables: `BKSCMSTR`, `BKSCLOC`.\n",

"RO": "## What it does\n\nRoutings — defines the sequence of manufacturing operations (steps) for an item. Each operation links to a work center, setup hours, run hours, queue time, and move time. Drives WO scheduling and lead-time calculation. See [[recipe-enter-routing]].\n\nKey tables: `ROUTING` (header), `BKRTEMTR` (operations), `BKRTTOOL` (tooling), `BKRTINST` (instructions).\n",

"WC": """
## What it does

Warehouse Control — manages warehouse bin addresses for multi-location inventory.
Defines physical bin locations within each stock location, assigns items to bins,
and tracks bin-level on-hand quantities separately from total on-hand.

Not to be confused with **work centers** (production stations) — those are set up
under [[module-RO|RO]] routing option `RO-C Enter Work Centers`.

## Menu operations

| Code | Operation |
|------|-----------|
| WC-A | Enter Warehouse Bin Locations |
| WC-B | Assign Warehouse Control (per-location flag) |
| WC-C | Assign Bins to Items |
| WC-E | Print Bin Inventory Listing |
| WC-F | Print Bin Inventory Exceptions |
| WC-G | Warehouse Control Defaults |

## Key tables

| Table | Purpose |
|-------|---------|
| `ISBINLOC` (22 fields) | Bin master — bin code + location + on-hand per lot |
| `BKICLOC` (32 fields) | Per-location on-hand quantities (UOH/UOO/UOSO/UBO per location) |
| `ISBINLOT` (14 fields) | Bin + lot cross-reference |
| `PIBINLOC` (14 fields) | Bin-level count records during physical inventory |

## Integration

- **[[module-IN|IN]]** — items can have a default bin; BKICMSTR links to bin
- **[[module-PI|PI]]** — bin counts feed Physical Inventory via PIBINLOC
- **[[module-HH|HH]]** — handheld scanners use BKIC.LOC.* 297-var namespace for bin scanning
- **[[module-LO|LO]]** — LO module also manages location-level inventory
""",

"HH": "## What it does\n\nHandheld / Mobile — barcode scanner and mobile device integration for shop-floor data collection, receiving, and inventory. `HH-N` is the handheld item lookup (filters by Item Type [RFAMNLBTKO], Refresh Timer, credit-hold flag). Integrates with [[module-DC|DC]] for labor and [[module-PO|PO]] for receiving.\n\nKey forms: `T7HHN.DFM`, `T7HHWRC.DFM`.\n",

"PL": "## What it does\n\nPaperless Manufacturing — displays work order routing, BOM components, QC specs, and notes on screen at the workstation, eliminating printed travelers. Key forms: `T7PLessComps.DFM` (Issue Components — All/Shortages), `T7PLessNotes.DFM` (QC Specs/WO Item/Routing/Customer/Vendor), `T7PLessWODates.DFM` (WO Dates/Qty).\n",

"QT": "## What it does\n\nQuotations / Estimating — builds pre-sale cost estimates with material, labor, and markup. See [[recipe-estimate]] for a full walkthrough. Key tables: `BKQTMSTR` (estimate header), `BKQTLINE` (lines). `QT-B Convert to SO` turns an accepted estimate into a live sales order.\n",

"RF": "## What it does\n\nRFQ (Request for Quotation) — sends quote requests to multiple vendors and tracks their responses before issuing a PO. See [[recipe-rfq]]. Key tables: `BKPORFQH` (header), `BKPORFQL` (lines/responses). `PO-J Accept RFQ` creates a PO from the winning quote.\n",

"RT": "## What it does\n\nReport Templates — the ReportBuilder `.RTM` file engine. All EVO reports are `.RTM` files on the network share under `EVOReports\\`. Reports are designed in `RBDsgnr.exe` (Nevrona ReportBuilder). `FILELOC.B` maps configuration names to `.RTM` filenames. See [[recipe-custom-report]].\n",

"TA": "## What it does\n\nTools / Admin Utilities — backup, restore, software updates, company setup, and purge operations. Key forms: `TA-O Evo Backups` (local ZIP + optional cloud upload), `TA-P Apply Updates` (.UPD file processor). See [[recipe-backup]] and [[recipe-update-evo]].\n",

"SY": "## What it does\n\nSystem — user administration, access control, and company switching. `SY-A Enter Users` manages login IDs, passwords, access levels, and module restrictions. `SY-B Menu Restrictions` hides specific menu items. `SY-C Add Company` creates a new company. See [[recipe-add-user]], [[recipe-add-company]], [[recipe-switch-company]].\n\nKey table: `BKSYUSER`.\n",

"DE": "## What it does\n\nEDI / Data Exchange — Electronic Data Interchange for trading-partner document exchange (PO, invoice, ASN). Key forms in the `T7DEP*` and `T7DE*` family. Tables: `BKEDH`/`BKEDL` (EDI transaction headers/lines), `BKEDNOTE` (notes), `BKEDPOST` (posting queue). Also handles generic import/export via `T7GENIMP.DFM` (Import DBA — Skip/Replace/Append modes).\n",

"RM": """
## What it does

RMA (Return Material Authorization) — manages the full lifecycle of customer
returns: authorization, print/ship instructions, physical receipt, disposition
(Restock / Scrap / Repair), and credit memo generation.

## Workflow

```
RM-A  Enter RMA (t7rma.rwn)
      → creates RMA authorization record
      → assigns RMA number, return codes, disposition

RM-B  Print RMA (T7RMB.RWN)
      → generates packing slip / return instructions for customer

RM-C  Receive RMA (T7RMC.RWN)
      → records physical receipt of returned goods
      → updates inventory (Restock path) or scrap / repair routing

RM-D  Disposition RMA (T7RMD.RWN)
      → final disposition: Restock → INVTXN adjustment
                           Scrap   → INVTXN scrap transaction
                           Repair  → creates WO or SR service order

RM-E  Enter RMA Return Codes (T7RME.RWN)
RM-F  RMA / Service & Repair Defaults (T7DSRMA.RWN)
RM-G  Reason Codes Report (t7rmg.rwn)
```

## Key tables

| Table | Fields | Purpose |
|-------|--------|---------|
| `ISRMAI` | 54 | Active RMA lines (IS_RMA_* prefix) |
| `ISRMAAI` | 54 | Archived RMA lines (identical structure) |
| `ISRMAINV` | 84 | RMA invoice record (BKAR_INV_* clone — credit memo) |
| `ISRMINV` | 84 | RMA invoice (alternate/current path) |
| `ISRMAINF` | 54 | RMA UDF extension (ISSR_INFO_* 54 user-defined fields) |
| `ISRMAC` | 3 | RMA reason codes |
| `ISRMTXN` | 14 | RMA transaction log (BKAR_TXN_* clone) |

## Integration

- **[[module-AR|AR]]** — credit memo posts to AR as negative open item via ISRMAINV
- **[[module-SO|SO]]** — original SO invoice traced via OSONUM/OINVNUM on ISRMAI
- **[[module-SR|SR]]** — Repair disposition can create a service order in SR
- **[[module-IN|IN]]** — Restock disposition triggers INVTXN adjustment
""",

"SU": "## What it does\n\nSystem Utilities — low-level maintenance tools: index rebuild, file restructure, data verification, and diagnostic utilities. Typically accessed by administrators only. Includes table repair functions for Btrieve/Pervasive data files.\n",

"UT": "## What it does\n\nUtilities — general-purpose tools including data export, CSV import/export, and miscellaneous administrative functions. See [[recipe-export-csv]] and [[recipe-purge-history]].\n",

"LM": "## What it does\n\nLabel Management / Label Printing — prints barcoded labels for inventory items, lot numbers, serial numbers, and shipping. Uses `t7lottag.DFM` (Evo Lot Tagging — Label1/2/3 fields) for lot label printing. Integrates with [[module-LC|LC]] and [[module-HH|HH]].\n",

"LO": "## What it does\n\nLocations / Bin Management — manages warehouse bin addresses for multi-location inventory. Each bin is a slot in `BKICLOC`. Items can have a default bin in [[module-IN|IN]], and per-bin on-hand is tracked separately from total on-hand.\n",

"MA": "## What it does\n\nMachine / Asset tracking — records production machinery, maintenance schedules, and downtime in relation to [[module-WC|WC]] work centers. Each machine belongs to a work center and can be targeted in [[module-DC|DC]] labor entries.\n",

"MM": "## What it does\n\nMaintenance Management — preventive and corrective maintenance scheduling for production equipment. Tracks maintenance orders, labor, and parts used on machines in [[module-WC|WC]].\n",

"PL": "## What it does\n\nPaperless Manufacturing — electronic traveler / work-order packet displayed at the workstation. Eliminates printed travelers. Forms: `T7PLessComps.DFM` (issue components), `T7PLessNotes.DFM` (QC specs, routing notes), `T7PLessWODates.DFM` (WO dates and qty).\n",

"PS": "## What it does\n\nPlanning / Scheduling — finite capacity scheduling complement to [[module-MR|MR]] (MRP). Uses routing operation times, work center calendars, and WO priority to schedule production. Forms in the `T7SHA*` family (13 scheduling forms).\n",

"SA": """
## What it does

Sales Analysis — reporting-only module (no data entry) that produces detailed
and summary sales reports from posted AR/SO invoice history. Supports 26
user-configurable FROM/THRU range filters per report type (invoice date,
customer, item, salesperson, class, category, territory, lot, job, etc.).
Four Java-backed analysis views provide interactive charts.

**Scale at i2 Systems:** SA reads from 462,727+ posted invoice lines.

## Menu operations

| Code | Operation | Engine |
|------|-----------|--------|
| SA-A | Print Daily Sales/Bookings | T7SAA.RWN |
| SA-B | Print Profit by Invoice | T7SAB.RWN |
| SA-C | Print Customer Detail | T7SAC.RWN |
| SA-D | Print Customer Summary | T7SAD.RWN |
| SA-E | Print Customer Class Detail | T7SAE.RWN |
| SA-F → A | Profit by Invoice (chart) | ProfitByInvoice.jar |
| SA-F → B | Sales by Customer | CustomerClass.jar |
| SA-F → C | Sales by Salesperson | SalesRepSummary.jar |
| SA-F → D | Sales by Item/Class | ItemClass.jar |
| SA-G | Print Customer Class Summary | T7SAG.RWN |
| SA-H | Print Salesperson Detail | T7SAH.RWN |
| SA-I | Print Salesperson Summary | T7SAI.RWN |
| SA-J | Print Inventory Detail | T7SAJ.RWN |
| SA-L | Print Product Class | T7SAL.RWN |
| SA-M | Print User-Defined Detail | T7SAM.RWN |
| SA-N | Print User-Defined Summary | T7SAN.RWN |
| SA-O | Top Customer Report | T7SAO.RWN |
| SA-P | Print Sales With Surcharge Rolled Up | T7SAP.RWN |
| SA-Q | Print Actual Margin (uses WO actual costs) | T7SAQ.RWN |

## Key tables

| Table | Fields | Purpose |
|-------|--------|---------|
| `BKSAREPT` | 57 | Saved report configurations (TYPE+NAME PK, RTM + 26 FROM/THRU range pairs) |
| `BKACTRPT` | 53 | Activity report configurations (same structure, for SA-M/SA-N) |

SA reads (but does not write) `BKARINV`/`BKARINVL` (AR invoices), `BKARCUST`,
`BKICMSTR`, and for actual-cost analysis: `WORKORD`/`WOMAT`/`WOBOM`.

## Integration

- **[[module-AR|AR]]** — all SA reports draw from posted AR invoice history
- **[[module-SO|SO]]** — SA-A includes bookings (open SO) from BKSOX
- **[[module-WO|WO]]** — SA-Q uses actual WO labor+material costs for margin
- **[[module-CS|CS]]** — salesperson links via ISPRSALE / BKPRSALE
""",

"SB": """
## What it does

Spec Book / Approved Vendor List (AVL) — enforces approved sourcing for purchased
components. Defines which manufacturers, vendors, and manufacturer part numbers
are approved for each item. During purchasing and receiving, the system validates
that the selected source is on the approved list.

**SB has no standalone top-level menu.** The approved sourcing data is accessed
through the BM (BOM) module sub-menus and is enforced automatically by PO and
IN module transactions.

## Tables

| Table | Fields | Purpose |
|-------|--------|---------|
| `BKSBPART` | 5 | Approved substitute parts (FROM.SUBST cross-reference) |
| `BKSBVEND` | 6 | Approved vendor sources (VENDOR + MFGNM + VPART + REV + EXTRA + UID) |
| `BKSBMFG` | 16 | Approved manufacturer master (MFG code + name + address + contact) |

## Access points

| Location | Program | What it does |
|----------|---------|-------------|
| BM-J | T7BMJ.RWN | Enter approved substitutes (BKSBPART) |
| BM-K | T7BMK.RWN | Enter approved vendors (BKSBVEND) |
| BM-L | T7BML.RWN | Enter approved manufacturers (BKSBMFG) |
| PO receive | T7POENG.RWN | Validates BKSBVEND on engineering receipts |
| MRP | T7MRG.RWN | Uses BKSBVEND / BKSBMFG to select vendor at planned-order release |

## Integration

- **[[module-BM|BM]]** — AVL data is managed from BM browse/entry screens
- **[[module-PO|PO]]** — PO receipt programs check BKSBVEND / BKSBMFG compliance
- **[[module-MR|MR]]** — MR-G auto-selects first approved vendor from BKSBVEND
- **[[module-WO|WO]]** — T7WOLA (outside process) reads BKSBVEND for subcontract sourcing
""",

"SL": """
## What it does

Shop Loading — the ISTS-enhanced scheduling and work center load subsystem.
SL programs integrate with the [[module-SH|SH]] scheduling module and provide
Java-backed interactive visualizations for work center capacity, WO priority,
and finite scheduling.

The main SL component is `T7SLSFC` — the **ISTS global session config loader**
that reads ~250 `ISTS.CFG.*` flags from BKYSMSTR into memory at session start.
The scheduling views (T7SHA/SHC/SHP) and Java JARs are accessible from the
SH module menu (SHA–SHR).

**SL has no standalone top-level menu entry.** All SL functionality is reached
through the [[module-SH|SH]] Scheduling menu.

## Programs

| Program | Procs | Purpose |
|---------|------:|---------|
| `T7SLSFC` | 5 | ISTS session config loader — reads ISTS.CFG.* flags at startup |
| `T7SHA` | 94 | WO schedule / Gantt chart (SH-A) |
| `T7SHC` | 70 | Work center capacity scheduler (SH-C) |
| `T7SHP` | 179 | Priority-based lead time scheduler (SH-P) |

## Java-backed load views (launched from SH-K / SH-L / SH-R)

| JAR | Entry point | View |
|-----|------------|------|
| `WCScheduler.jar` | `com.evoerp.wcsched` | Work center scheduler (SH-R) |
| `WorkCenterLoad.jar` | `com.evoerp.wcload.javafx.App` (VSCHED) | WC load visualization (SH-L) |
| `WOScheduler.jar` | — | Work order scheduler |
| `MachineView.jar` | `com.evoerp.machineview.jfx.App` | Machine schedule (SH-D) |

## Key namespace

`MTWC.*` 30-var namespace from `WORKCTR` (47f): WC/%UTIL/HRSWEEK/LABOR/SETUP/
MACHINE/AVGQTIME/VOVHD/QPR1-3/PARENT.WC/OUTPROC — work center capacity and
cost rates used by all SL scheduling calculations.

## Integration

- **[[module-SH|SH]]** — SL programs are the implementation of SH scheduling menu items
- **[[module-WO|WO]]** — reads WORKORD + WOROUT + BKDCLAB for schedule inputs
- **[[module-DC|DC]]** — BKDCLAB time-clock feed drives Gantt actual vs scheduled
""",

"SD": "## What it does\n\nSales / Shipping Detail — shipment detail tracking, carrier assignments, and freight billing. Related to [[module-SH|SH]] (Shipping) and SO module.\n",

"CM": "## What it does\n\nCredit Memo — processing of customer credit memos. Handles price adjustments, allowances, and return credits outside of the RMA flow. See [[recipe-credit-memo]]. Posts to AR as negative open items.\n",

"CP": "## What it does\n\nCredit and Payment processing — handles credit card and alternative payment method processing for customer accounts. Integrates with [[module-AR|AR]] cash receipts.\n",

"CR": "## What it does\n\nCredit — customer credit limit management, credit hold processing, and credit approval workflows. AR-A Enter Customers includes the credit limit and credit hold fields tracked by this module.\n",

"FA": """
## What it does

Fixed Assets manages the full lifecycle of capital equipment: acquisition,
periodic depreciation calculation, GL posting, and disposal.

**Scale:** 589 assets with 22,568 depreciation transaction records (~38
transactions per asset on average). Regular depreciation has been posted
over many years.

## Asset lifecycle

```
FA-A  Enter Asset
      → ISFXASST record with cost, life, method, 3 GL account pairs

FA-B  Post Depreciation
      → reviews ISFXATRN where IS_FXT_POSTED = 'N'
      → writes 2 GL lines per entry to BKGLTRAN:
          DR: Depreciation Expense (IS_FXT_DEPEXPA/D)
          CR: Accumulated Depreciation (IS_FXT_ACDEPA/D)
      → flips IS_FXT_POSTED = 'Y'

FA-C  List Depreciation Transactions (ISFXATRN)
FA-D  List Assets (ISFXASST)
FA-E  Export Assets to CSV/fixed-width
```

## GL account pairs per asset

Each asset carries **three** GL account pairs (account + department):

| Pair | Balance Sheet or P&L | Purpose |
|------|---------------------|---------|
| Asset (GLA/GLD) | Balance Sheet | Asset at cost |
| Accum Dep (ACDEPA/ACDEPD) | Balance Sheet | Contra-asset |
| Dep Expense (DEPEXPA/DEPEXPD) | P&L | Periodic charge |

This allows different assets to post depreciation to different cost centers.

## Tables

| Table | Records | Purpose |
|-------|--------:|---------|
| `ISFXASST` | 589 | Asset master (23 fields) |
| `ISFXATRN` | 22,568 | Depreciation transactions (12 fields) |

Key note: `ISFXATRN` stores **redundant copies** of the 4 GL account fields
from ISFXASST. This means changing the GL accounts on an asset after posting
does not corrupt historical transaction records.

## Integration

- **[[module-GL|GL]]** — depreciation posts to BKGLTRAN; BKSYMSTR validates
  the open accounting period before posting
""",

"FL": "## What it does\n\nFloor Control — shop-floor scheduling and sequencing at the work center level. Bridges [[module-DC|DC]] (labor capture) and [[module-SH|SH]] (scheduling) with real-time WO status on the floor.\n",

"FO": "## What it does\n\nForecasting — demand forecasting engine. Creates item-level forecasts based on sales history, seasonality, and trend analysis. Feeds planned demand into [[module-MR|MR]] (MRP) as independent demand.\n",

"FP": "## What it does\n\nForecast / Planning — planning horizon management for MRP and scheduling. Defines planning buckets (weekly, monthly) and forecast periods.\n",

"IC": """
## What it does

Inventory Copy utility — a single-operation utility that copies production
inventory master data (BKICMSTR) into the estimating inventory mirror (ISICMSTR /
MTICMSTR). Accessed as **IC-A Copy Production to Estimate Inventory**.

This is a one-way bridge: it ensures the estimating module (ES) has current
standard costs, UOM, and item descriptions when building estimates.

**IC has no standalone menu group.** It is a small utility invoked from within
the IN or ES module workflow.

## Program

`T7IC2EST` (6 procs, 2 tables) from EVOCFG.SRC:
- Reads `BKICMSTR` (production item master) + `MTICMSTR` (multi-company IC)
- Writes to `ISICMSTR` (IS-era estimating IC mirror) + `ISICEST` (estimating IC test)
- `TNOR` / `TPR` flags select which cost tier (normal vs. prime) to transfer

**Cycle count** scheduling and ABC classification are tracked in `ISCYCLCD` (7 fields:
cycle count frequency codes) and managed through the [[module-PI|PI]] Physical Inventory
module, not through the IC utility.

## Integration

- **[[module-ES|ES]]** — IC-A populates the IC mirror used by Estimating for standard costs
- **[[module-IN|IN]]** — source data is BKICMSTR (production inventory master)
- **[[module-PI|PI]]** — cycle count frequency (ISCYCLCD) is a PI-adjacent feature, not IC
""",

"IM": "## What it does\n\nImport Management — handles data imports from external sources (CSV, tab-delimited, legacy system exports). Uses `T7GENIMP.DFM` (Import DBA) with Skip/Replace/Append modes. See [[recipe-export-csv]].\n",

"IS": "## What it does\n\nISTS Custom — modules and enhancements specific to i2 Systems installations. Forms prefixed with `J7*` or carrying the ISTS enhancement marker (`ASSIGN(\" - ISTS Enhancement MM/DD/YY\")` in the source). Examples include Golding Farms pricing (`T7GFPRICE.DFM`).\n",

"LW": "## What it does\n\nLottery / Weighted Allocation — specialty module for allocating items across multiple orders using weighted or lottery logic. Used in specific industries (e.g., agricultural distribution) when demand exceeds supply and fair allocation is required.\n",

"PC": "## What it does\n\nProduct Configuration — Features and Options (F/O) engine. Allows configurable items where the customer selects options at order entry time. The F/O dialog launches from SO-A when an item has a configuration. See `T7FO*.DFM` forms.\n",

"QU": "## What it does\n\nQueue Management — tracks work queues at work centers, including setup, run, and move times for scheduling. Relates to [[module-WC|WC]] queue-time fields in routing operations.\n",

"AB": "## What it does\n\nAddress Book — shared contact management for customers, vendors, and other entities. Provides a centralized repository of addresses, phone numbers, and contacts referenced by AR, AP, and SO modules.\n",

"AC": "## What it does\n\nAccounting Consolidation — multi-company GL consolidation. Rolls up subsidiary company financials into a parent company for consolidated financial statements. Works with [[module-AM|AM]] period-end processing.\n",

"DI": "## What it does\n\nDistribution / Drop-Ship — manages drop-ship order flows where PO quantities ship directly from vendor to customer without passing through your warehouse. Links SO lines to PO lines via `BKSOPO`.\n",

"EX": "## What it does\n\nExport / Exchange — data export utilities for sending EVO data to external systems (accounting interfaces, warehouse management, etc.). Produces formatted output files. See [[recipe-export-csv]].\n",

"MM": "## What it does\n\nMaterial Management — broader material planning and control functions extending MRP. Manages safety stock, reorder points, and min/max replenishment outside of the full MRP engine.\n",

"UM": "## What it does\n\nUnit of Measure Conversion — manages UOM conversion factors between purchasing UOM, stocking UOM, and selling UOM. Ensures quantities are correctly translated when a vendor sells in cases but you stock in each.\n",

"UP": "## What it does\n\nUpdates / Patches — the software update distribution and application subsystem. `.UPD` files are Btrieve-format patch packages applied by `TA-P`. See [[recipe-update-evo]].\n",

"US": """
## What it does

User Settings — per-user personal preferences for the EVO interface. Each logged-in
user can customize their own menu layout, screen positions, password, reminders,
and workflow triggers without affecting other users.

## Menu operations

| Code | Operation | Program |
|------|-----------|---------|
| US-A | Customize Settings (toolbar, colors, screen mode) | T7SMK.RWN |
| US-B | Customize Menu (add/remove/reorder menu items) | WBKMENUSUEU.RWN |
| US-C | Reset Screen Size / Locations | t7resetdfm.RWN |
| US-D | Change Password | PASSWORD.INT |
| US-E | Update PO Electronic Signature Info | T7DIGSIG.RWN |
| US-F | Enter Reminders (calendar reminders) | calrem.rwn |
| US-G | Enter Triggers (automation triggers) | T7USG.RWN |
| US-H | Update Contract Review Password | T7CTREVU.RWN |

These settings are stored per-user in EvoSettings.INI (`[User:NAME]` sections) and
in `BKLOGON` / `BKSYUSER`. US-B customizations are stored in `BKMENUSU` (the menu
definition table) per-user.

## Integration

- **[[module-SM|SM]]** — SM-K is the same as US-A (Evo User Settings, T7SMK.RWN)
- **[[module-SY|SY]]** — SY-A manages security levels and module access; US manages personal prefs
""",

"YS": "## What it does\n\nYear-end / System — year-end processing utilities beyond [[module-AM|AM]]. Handles special year-end tasks: 1099 generation, W-2 reporting (if EVO handles payroll), and fiscal-year archive operations. See [[recipe-year-end-close]] and [[recipe-1099]].\n",

}
