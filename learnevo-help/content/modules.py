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

## Key tables

| Table | Purpose | Live count (i2) |
|-------|---------|----------------|
| `BKARCUST` | Customer master (106 fields) | 4,404 customers |
| `BKARINV` | Open invoice headers (104 fields) | 3,708 open invoices |
| `BKARINVL` | Invoice line items | ~47,000 lines |
| `BKARHINV` | Archived invoice headers | 95,982 paid/archived |
| `BKARCHKF` | Customer payments (checks/EFT) | 43,698 payments |
| `BKARTXN` | AR transaction ledger | multi-year history |
| `BKARCR` | Cash receipts staging | current period |

`BKARCUST` is 106 fields: name, bill-to/ship-to address, credit limit,
terms code, tax code, salesperson, pricing code, GL receivable account,
balance forward, last payment date.

`BKARINV` is 104 fields: invoice#, SO#, customer, bill/ship address,
terms, total, tax, salesperson, freight, all detail for statement and
aging. Status code: Y=active, X=voided, N=returned.

## Core concept

Each customer exists as one row in BKARCUST. An invoice is a BKARINV
header + one-or-more BKARINVL lines. A payment is a BKARCHKF check
that links back to one or more invoices. When an invoice is fully paid
it moves from BKARINV to BKARHINV (history) during AM-K Archive AR.

## Typical workflow

```
AR-A Enter Customer → BKARCUST
  ↓
SO-A Create Sales Order → shipped → SO-F Print Invoice
  ↓  (invoice creation crosses into SO module)
AR-B Post Invoice to AR → BKARINV / BKARINVL / BKGLTRAN
  ↓
AR-E Print Statement (monthly) → mailed to customer
  ↓
AR-C Record Payment → BKARCHKF / BKARTXN / updates BKARCUST.balance
  ↓
AR-D Charge Interest (optional, if overdue) → posts interest voucher
  ↓
AM-K Archive → closed invoices move BKARINV → BKARHINV
```

## Common reports

| Code | Report |
|------|--------|
| `AR-F` | Customer Aging (current/30/60/90/over 90 days) |
| `AR-E` | Monthly Statements |
| `AR-G/H/I/J` | Customer name/info/labels/tax listings |
| `AR-K` | Sales Tax Report |
| `AR-N` | Customer Deposits |
| `AR-R` | AR Payment History |

## Integration

| Module | Relationship |
|--------|-------------|
| `SO` | SO-F creates BKARINV invoices; AR records the payment |
| `GL` | Every AR transaction posts to BKGLTRAN (2.97M GL entries total) |
| `CS` | Commission System reads BKARINV to compute earned commissions |
| `AM` | AM-K archives paid invoices; AM-H posts period-end AR summary |

## Admin defaults

`AD-E (Accounts Receivable Defaults)` configures:
default receivable GL account, interest rate and grace period,
statement format, taxable/non-taxable defaults, and aging bucket
thresholds.
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
RMAs. 48 menu operations, 69 UI forms — the largest module by UI surface.

## Key tables

| Table | Purpose | Live count (i2) |
|-------|---------|----------------|
| `BKARINV` | SO / invoice headers (104 fields) | 3,708 open; 95,982 archived |
| `BKARINVL` | SO / invoice line items (38 fields) | 78,023 lines |
| `BKARINVI` | Invoice shipping detail | per invoice |
| `BKSOHLOT` | Lot shipping records | lot-tracked shipments |
| `BKSOHSER` | Serial shipping records | serial-tracked shipments |
| `BKSONOTE` | Order notes | per-line notes |
| `BKSOPO` | SO-to-PO link for drop-ship | 0 if no drop-ships |

**Note:** EvoERP reuses `BKARINV` for both Sales Orders and Invoices.
The status code `BKAR_INV_INVCD` distinguishes them:
- `Y` = active SO / active invoice (2,896 at i2)
- `X` = voided (421)
- `N` = returned/credit memo (179)
- ` ` = draft / in-progress (202)

## Document lifecycle

```
SO-P-A Enter Quote
  ↓ customer accepts
SO-A Enter Sales Order → BKARINV (INVCD=' ') + BKARINVL
  ↓
CR-B Contract Review (if required by customer/item)
  ↓ approved
SO-C Print Pick Ticket → pickers pull from warehouse
  ↓ physically picked and confirmed
SO-C Print Packing Slip → shipped with goods
  ↓
SO-F Print Invoice → BKARINV (INVCD='Y') + posts to BKGLTRAN
  ↓ payment received
AR-C Record Payment → BKARCHKF closes the invoice
```

## SO screen variants

| Code | Variant | Use case |
|------|---------|----------|
| `SO-A` | Standard SO | Normal sales order entry |
| `SO-P-A` | Quote | Price quote before order is confirmed |
| `SO-P-F` | RMA Return | Return Material Authorization |
| `SO-J` | Recurring SO | Auto-create repeat orders on schedule |
| `SO-Q` | Quick Entry | Fast single-line SO entry |
| `SO-T` | In-house | Internal transfer orders |

## Sales pricing

Multiple price levels supported per item in `BKSLEVEL` (422 fields).
Each customer has a default price level (`BKARCUST.BKAR_SAL_LVL`),
with per-item overrides. Discounts apply by customer price code or
quantity break.

## Features & Options configurator

If an item has `BKIC_PROD_FNO_FLAG = Y`, entering it on an SO launches
a modal F/O dialog. User selects from Feature categories (e.g. "Color")
and Options (e.g. "Red"). The configuration builds a custom part# and
BKARINVL line. See [[module-FO|FO]] for configuration setup.

## Invoice formats

Four RTM variants: `bksof1.rtm` through `bksof4.rtm`. Selected per
customer based on their requirements (customer PO# display, line-item
detail level, price visibility, etc.).

## Integration

| Module | Relationship |
|--------|-------------|
| `AR` | SO-F posts to BKARINV; AR records payment |
| `IN` | Shipment decrements BKINVLOC on-hand |
| `WO` | Make-to-order: releasing an SO can trigger WO creation |
| `PO` | Drop-ship SOs auto-create linked PO via BKSOPO |
| `CS` | Commission System reads posted invoices for commission calc |
| `CR` | Contract Review module can block SO until approved |
| `ES` | ES-E Convert Estimates creates new SOs from quotes |
""",

"PO": """
## What it does

Purchase Orders manages procurement — creating POs, receiving against
them, and feeding AP for payment. 29 menu operations covering the full
procurement lifecycle: RFQ → quote → PO → receipt → AP voucher → check.

## PO lifecycle

```
RF-A / PO-E-A Request for Quote (optional)
  ↓ vendor responds
PO-G Convert RFQs → Purchase Order
  ↓ (or PO-A Enter PO directly)
PO-A Purchase Order created
  ↓ approved (if approval limits configured)
PO-C Receive Purchase Orders → inventory on-hand incremented
  ↓ PO-J-A Print Receipt Traveler (for QC inspection path)
PO-J-C Enter Inspection Buyoffs (QC accepts/rejects received qty)
  ↓ QC release
AP-B Enter AP Voucher → linked to PO via BKAP_POL_PONM
  ↓ approved & checked
AP-H Print Checks → posted to GL
```

## Key tables

| Table | Contents | Live count (i2) |
|-------|----------|----------------|
| `BKAPPO` | Open PO headers (58 fields) | 2,814 |
| `BKAPPOL` | Open PO lines (38 fields) | 25,022 |
| `BKAPAPO` | Archived PO headers | 66,098 |
| `BKAPAPOL` | Archived PO lines | 278,089 |
| `BKAPHPO` | Historical PO headers | 77,780 |
| `BKAPHPOL` | Historical PO lines (has .XLB blob file) | 325,518 |

Total POs ever created at i2: ~146,700 (open + archived + historical).

Key header fields (`BKAPPO`): `BKAP_PO_NUM` (PO#, PK), `BKAP_PO_VNDCOD`/`VNDNME`
(vendor), `BKAP_PO_SHPCOD`/`SHPNME` (ship-to location), `BKAP_PO_TERMD` (payment
terms), `BKAP_PO_ENTBY` (entered by user).

Key line fields (`BKAPPOL`): `BKAP_POL_PONM` (PO#, FK), `BKAP_POL_CNTR` (line#),
`BKAP_POL_PCODE`/`PDESC` (item/description), `BKAP_POL_PQTY` (ordered qty),
`BKAP_POL_PPRCE` (unit price), `BKAP_POL_PDISC` (discount %), `BKAP_POL_ERD`
(expected receipt date).

## Receiving (PO-C)

1. Select PO number (or scan barcode)
2. Pick lines being received (partial receipts supported)
3. Enter actual quantity received (defaults to ordered qty)
4. Enter lot # and/or serial # if item is lot/serial-tracked
5. Select bin location
6. Post → `BKINVLOC` on-hand incremented; accrual GL entry posted

## QC path (PO-J)

For items requiring incoming inspection:
- `PO-J-A` prints a receipt traveler (work order-style routing card)
- `PO-J-C Enter Inspection Buyoffs` records accepted/rejected qty into
  `BKQCMSTR` (receive event) + `BKQCTRAN` (per-item QC detail)
- `PO-J-B Print Inventory in QC` shows what is still awaiting inspection

## Drop-ship POs

POs created from a drop-ship SO line link back to `BKSOPO` via the
BKAP_PO_SONUM field. When vendor ships direct to customer, the PO
receipt simultaneously closes the SO line without touching inventory.

## Approval workflow

If approval limits are configured, POs over a dollar threshold require
approval (BKAP_PO_APRV flag) before they can be received. Configured
in PO or AP defaults.

## Integration

| Module | Relationship |
|--------|-------------|
| `AP` | AP-B picks up received-not-vouchered PO lines for payment |
| `IN` | PO-C receipt increments BKINVLOC on-hand |
| `GL` | Receipt: Inventory ↔ Accrued AP; Voucher: Accrued AP ↔ AP |
| `QC` | PO-J-C writes BKQCMSTR/BKQCTRAN; QC-A/QC-E report off PO receipts |
| `MR` | MRP creates PO suggestions; PO delivery dates feed MR due-date calc |
| `SO` | Drop-ship SOs generate linked POs via BKSOPO |
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

Payroll manages the full US payroll cycle: employee master, time entry,
tax calculation, check printing, GL posting, and year-end W-2/941 filing.
29 menu operations, 16 dedicated tables. Holds the **largest table in
EvoERP by field count** — `BKPRGLFL` has 664 fields mapping payroll
cost components to GL accounts.

## Key tables

| Table | Purpose | Live count (i2) |
|-------|---------|----------------|
| `BKPRMSTR` | Employee master (384 fields) | 305 employees |
| `BKPRCURP` | Current period payroll entries | 17 (current cycle) |
| `BKPRHISTP` | Payroll history | multi-year |
| `BKPRTCFG` | Tax configuration (205 fields) | 1 record |
| `BKPRW2` | W-2 staging | 0 (pre-year-end) |
| `BKPRGLFL` | GL distribution mapping (664 fields) | 1 record |
| `BKPRSTAB` | Tax rate tables | 1 record |

## Payroll cycle workflow

```
PR-A Enter Employees → BKPRMSTR (name, address, tax status, deductions,
  bank routing for direct deposit, GL cost center)
  ↓
PR-B Enter Time → BKPRCURP (hours per employee per period)
  (or import from DC shop-floor time scans, or from WO-F Enter Labor)
  ↓
PR-C Calculate Payroll → compute gross, taxes, deductions, net
  Federal withholding + SS (6.2%) + Medicare (1.45%) + state + local
  Deductions: health, 401k, garnishments
  ↓
PR-D Print Pre-Check Register → proof listing; verify before printing
  ↓
PR-E Print Checks / DD Advices → physical checks or ACH direct-deposit file
  (ACH via J7ADTNACHA or custom variant; bank routing in BKPRMSTR.BKPR_DD_*)
  ↓
PR-F Post to GL → BKPRGLFL maps each pay component to GL accounts
  ↓ quarterly
PR-G Print 941 → federal quarterly payroll tax return
  ↓ annually
PR-H Print W-2 → BKPRW2 staging → W-2 forms
```

## Tax calculation

`BKPRTCFG` (205 fields) + federal/state rate tables (`BKPRSTAB`) drive
withholding. Rates updated via `EvoPRupd.RWN` when IRS or state changes
them. Supports: federal, Social Security, Medicare, state income tax,
local tax, SUTA, FUTA (employer portions).

## Integration

| Module | Relationship |
|--------|-------------|
| `GL` | PR-F posts payroll journal entries; BKPRGLFL maps components to accounts |
| `DC` | Shop-floor time scans in BKDCLAB* feed PR-B time entry |
| `CS` | Commissions module can post to payroll for salesperson payout |
| `WO` | WO-F Enter Labor also writes time records used by PR |
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

**At i2 Systems:** BKDCCFG=0 (no DC configuration active). Shop floor labor
is entered via WO-F menus, not barcode terminals. However BKDCHLAB holds
96,421 historical DC labor records from prior active use.

## Database tables (live counts, 2026-07-01)

| Table | Records | Purpose |
|-------|--------:|---------|
| `BKDCLAB` | 22 | Active labor transactions not yet posted (pipeline staging) |
| `BKDCPLAB` | 1 | Posted-pending labor (cleared after full post cycle) |
| `BKDCCLAB` | 0 | Cleared/archived labor |
| `BKDCTLAB` | 0 | Temp labor staging |
| `BKDCHLAB` | 96,421 | Historical DC labor — all posted transactions (archive) |
| `BKDCSHFT` | 1 | Shift configuration (3 shift names + 3 buffer codes) |
| `BKDCCFG` | 0 | Data collection module configuration |

All BKDCLAB* tables share **identical 51-field LAB_* schema** and are accessible via ODBC.

## BKDCLAB / BKDCHLAB — Labor Transaction Schema (51 fields)

| Field | Meaning |
|-------|---------|
| `LAB_DATE` | Work date |
| `LAB_EMP` | Employee number |
| `LAB_WOPRE` + `LAB_WOSUF` | Work order number + suffix |
| `LAB_OPER` | Routing operation number |
| `LAB_POSTED` | Posted flag (Y/N) |
| `LAB_SHIFT` | Shift number |
| `LAB_START` / `LAB_FINISH` | Clock-in / clock-out time |
| `LAB_PARTS` / `LAB_SCRAPPED` | Parts completed / scrapped |
| `LAB_NOJOBS` | Number of jobs run |
| `LAB_RUNHRS` / `LAB_SETUPHRS` | Run time / setup time hours |
| `LAB_REGOVER` | R=Regular / O=Overtime |
| `LAB_SCRAPCD_1..5` / `LAB_SCRAPQTY_1..5` | Up to 5 scrap reason codes + qty |
| `LAB_JCNUM` | Job code (links to ISJOB) |
| `LAB_CYCLE_HR/MIN/SEC/PARTS/NOTE` | Cycle time tracking |
| `LAB_GEN_DATE_1..2`, `LAB_GEN_ALPHA_1..2`, `LAB_GEN_NUM_1..2`, `LAB_GEN_FLAG_1..5` | Generic extension fields |
| `LAB_UID` | Unique record ID (STRING 30) |
| `LAB_ADT_SUPER/IN/OUT` | Audit trail: supervisor + in/out (STRING 100 each) |

## Integration

- **[[module-WO|WO]]** — BKDCLAB posts to WOLABOR and WOMAT when processed
- **[[module-PR|PR]]** — LAB_RUNHRS + LAB_SETUPHRS feed BKPRCURP for payroll
- **[[module-HH|HH]]** — handheld device interface; HH-I Paperless Shop Floor uses DC tables
- **[[module-DE|DE]]** — DE-J batch import writes directly to BKDCLAB
""",

"QC": """
## What it does

Quality Control tracks incoming and in-process inspections — from setting
up inspection plans per item to recording results and issuing certificates
of compliance (CoC) and Non-Conformance Reports (NCRs).

**Scale (2026-07-01):** 53,304 inspection events in BKQCMSTR; 54,227 transaction
lines in BKQCTRAN (avg 1.02 trans/event); 74 NCRs in ISNCR.
Rejection rate: BKQCMSTR.QTY_REJECT / QTY_RECVD = ~1.7% historically.

## Database tables (live counts, 2026-07-01)

| Table | Records | Fields | Purpose |
|-------|--------:|--------|---------|
| `BKQCMSTR` | 53,304 | 15 | QC inspection event (one per PO receive lot) |
| `BKQCTRAN` | 54,227 | 38 | Per-line inspection detail with pass/fail quantities |
| `ISNCR` | 74 | — | Non-Conformance Reports |
| `ISCAR` | 0 | — | Corrective Action Reports |
| `ISQCMTHD` | 0 | 44 | QC method library (test procedures) |
| `ISQCRSLT` | 0 | 57 | QC result/specification per method |
| `ISQCSPEC` | 0 | 57 | QC specification master |
| `ISQCAMST` | 0 | 14 | Alternative QC receiving master |
| `ISQCATRN` | 0 | 20 | Alternative QC receiving transaction detail |

**At i2:** ISQCMTHD/ISQCRSLT/ISQCSPEC all empty — the method library feature
is not configured. i2 uses basic receive-inspect-pass/fail flow without
pre-defined test methods.

## BKQCMSTR — QC Inspection Event (15 fields)

| Field | Meaning |
|-------|---------|
| `BKQC_VEND_CODE` | Vendor code |
| `BKQC_RECV_DATE` | Receipt date |
| `BKQC_PO_NUM` | Purchase order number |
| `BKQC_RECVR_NUM` | Receiver (receipt transaction) number |
| `BKQC_POL_ITM_NO` | PO line item number (STRING 10) |
| `BKQC_PKSLIP_NUM` | Packing slip number |
| `BKQC_QTY_RECVD` | Quantity received |
| `BKQC_QTY_BUYOFF` | Quantity accepted (bought off) |
| `BKQC_QTY_REJECT` | Quantity rejected |
| `BKQC_PKSLIP_QTY` | Packing slip quantity |
| `BKQC_PROD_CODE` | Item/part code |
| `BKQC_UNIT_COST` | Unit cost at receipt |
| `BKQC_EXTRA` | Extra (STRING 25) |
| `BKQC_OUT_DATE` | Release/disposition date |
| `BKQC_QTY_NCR` | Quantity sent to NCR |

## BKQCTRAN — QC Transaction Detail (38 fields)

Key fields: TRN_PO, TRN_VEND, TRN_CODE (item#), TRN_RECNUM (receiver#),
TRN_GQTY (good qty), TRN_BQTY (buy-off qty), TRN_UQTY (unacceptable qty),
TRN_SCRAP (scrap code), TRN_REWORK (rework code), TRN_PODTE/ARDTE/BODTE
(PO/arrival/buy-off dates), TRN_EMPNUM (inspector), TRN_FAULT/BROKEN flags,
TRN_FIXQTY (fixed qty), TRN_NCR (NCR qty) + 5 date/num/alpha generic fields.

## Workflow

```
PO receipt arrives  ->  QC-A: Create inspection record (BKQCMSTR)
                    ->  QC-B: Enter inspection results (BKQCTRAN)
                    ->  QC-C: Print certificate of compliance
                    ->  QC-F: NCR workflow if rejection (ISNCR created)
```

## Integration

- **[[module-PO|PO]]** — QC inspection triggers on PO receipt (QC-J intercept on PO-E)
- **[[module-IN|IN]]** — items under QC hold are unavailable for issue until released
- **[[module-WO|WO]]** — in-process QC can trigger per routing operation (OPQCDESC table)
- **[[module-NCR|NCR/IS]]** — QC-F-A creates ISNCR; QC-F-B triggers ISCAR corrective action
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

**Key architectural note:** CS has no dedicated BKCS* commission tables. Commission
data is stored as fields within the core AR/SO tables: BKARCUST holds the rate,
BKARINV holds the per-invoice percentages, BKICPMAT holds per-price-code rates.
ISPRSALE (IS* custom, 0 records at i2) is the accumulation table for earned
commissions but is not actively used at i2 Systems.

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

## Where commission data lives

| Table | Field(s) | What it stores |
|-------|----------|----------------|
| `BKARCUST` | `BKAR_COMM_1`, `BKAR_COMM_2` | Customer commission % for primary/secondary rep |
| `BKARCUST` | `BKAR_IS_REP` | IS custom sales rep code (5 chars) |
| `BKARINV` | `BKAR_INV_COMMPR_1`, `BKAR_INV_COMMPR_2` | Per-invoice commission % at time of posting |
| `BKICPMAT` | `BKIC_PMAT_COMM1_1..10` | Per-price-code commission rates (10 price bands) |
| `ISPRSALE` | IS_PR_SALE_* (87 fields, 0 records) | IS custom accumulated commission totals |

**At i2 Systems:** Commission module is minimally used. ISPRSALE is empty (0 records).
Salesperson commissions are tracked manually outside EVO rather than through CS-D Transfer.

## Integration

- **[[module-AR|AR]]** — commissions sourced from BKARINV; BKARCUST drives rate defaults
- **[[module-SO|SO]]** — salesperson code on SO header (BKAR_INV_SALEP_1/2) drives assignment
- **[[module-PR|PR]]** — CS-D Transfer writes earned commissions to PR for payment
- **[[module-IN|IN]]** — BKICPMAT price-code commission matrix links back to item setup
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

"SR": """
## What it does

Service and Repair — tracks customer equipment sent in for service or repair.
Manages the full workflow from receipt through diagnosis, parts and labor
consumption, invoice generation, and return shipment. Adjacent to
[[module-RM|RM]] (RMA) — a repair disposition in RM can create an SR order.

## Menu operations

| Code | Operation | Program |
|------|-----------|---------|
| SR-A | Enter Service/Repair | T7SRA.RWN |
| SR-B | Print Service/Repair | T7SRB.RWN |
| SR-C | Convert S/R to Work Order | T7SRC.RWN |
| SR-D | Print S/R Packing Slips | T7SRD.RWN |
| SR-E | Release Service/Repairs | T7SRE.RWN |
| SR-F | Print S/R Invoices | T7SRF.RWN |
| SR-G | Post S/R Invoices | T7SRG.RWN |
| SR-H | RMA & Service & Repair Defaults | T7DSRMA.RWN |
| SR-I | Void S/R Invoice | T7SRI.RWN |

## Workflow

```
SR-A  Enter Service/Repair order
      → captures customer, equipment, reported problem
      → creates ISSR_INFO_* UDF record

SR-C  Convert to Work Order (optional)
      → creates WORKORD for complex repairs requiring WO routing

SR-E  Release
      → moves to billable status

SR-F  Print Invoice   →   SR-G Post Invoice
      → generates AR invoice for labor + parts
      → posts to BKARINV
```

## Key tables (ISSS* family, live 2026-07-01)

| Table | Records | Fields | Purpose |
|-------|--------:|--------|---------|
| `ISSSOH` | 37 | 104 | Service order header — BKAR_INV_* schema clone (same layout as BKARINV) |
| `ISSSOL` | 1,177 | — | Service order lines — BKAR_INVL_* schema clone (same layout as BKARINVL) |
| `ISSSRH` | 0 | — | Service/repair history headers |
| `ISSSRL` | 0 | — | Service/repair history lines |

**ISSSOH uses byte-for-byte BKAR_INV_* field naming (104 fields):** BKAR_INV_NUM,
BKAR_INV_SONUM, BKAR_INV_INVCD (status), BKAR_INV_INVDTE, BKAR_INV_CUSCOD, and
all customer/ship-to address fields — identical structure to BKARINV.
This means SR-F/SR-G can generate invoices using the same posting logic as SO-F/SO-G.

**Scale at i2:** 37 active service orders, 1,177 service order lines (avg 31.8 lines/order).

## Integration

- **[[module-RM|RM]]** — Repair disposition in RM creates an SR order
- **[[module-WO|WO]]** — SR-C converts complex repairs to full WO routing
- **[[module-AR|AR]]** — SR-G posts the service invoice to BKARINV (same posting path as SO)
- **[[module-SO|SO]]** — ISSSOH mirrors BKARINV schema; the posting path is identical
""",

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

"SH": """
## What it does

Scheduling — manages work order scheduling, work center capacity, and finite/infinite
scheduling runs. Includes both interactive Gantt-style views (Java-backed) and batch
scheduling engines. Drives lead time calculation and WO start/finish date assignment.

## Menu operations

| Code | Operation | Engine |
|------|-----------|--------|
| SH-A | Edit WO Start/Finish/Due Dates | T7SHA.RWN |
| SH-B | Manually Schedule Work Orders | T7SHB.RWN |
| SH-C | Manually Schedule Work Centers | T7SHC.RWN |
| SH-D | Manually Schedule Machines | MachineView.jar |
| SH-E | Finite Scheduling | T7SHE.RWN |
| SH-F | Infinite Scheduling | T7SHF.RWN |
| SH-G | Print Work Order Schedule | T7SHG.RWN |
| SH-H | Print Work Order Status | T7SHH.RWN |
| SH-I | Print Work Center Schedule | T7SHI.RWN |
| SH-J | Print Machine Schedule | T7SHJ.RWN |
| SH-K | View Work Center Load | T7SHK.RWN |
| SH-L | View or Calculate Work Center Load | WorkCenterLoad.jar |
| SH-M | Lead Time Estimator | T7SHM.RWN |
| SH-N | Generate Lead Times | T7SHN.RWN |
| SH-O | Finite Schedule Bucket Report | T7SHO.RWN |
| SH-P | Lead Time Scheduling | T7SHP.RWN |
| SH-Q | Scheduling Defaults | T7DSSH.RWN |
| SH-R | Work Center Scheduler | T7VSCHED.RWN (WCScheduler.jar) |

## Java-backed views

SH-D, SH-L, and SH-R launch Java JARs from the ISJAVA task queue:
- `MachineView.jar` — machine schedule Gantt
- `WorkCenterLoad.jar` — work center capacity load visualization
- `WCScheduler.jar` / `WOScheduler.jar` — interactive Gantt-style schedulers

## Key tables

- `WORKCTR` (47f, `MTWC.*` namespace) — work center capacity, labor/overhead rates
- `WORKORD` (74f) — WO headers with start/finish/due dates
- `WOROUT` (81f) — WO routing operations (per-operation schedule)
- `SCHEDCAL` / `CALENDAR` — shop business calendar (SH-Q configures)
- `ISWOPRIO` (4f) — WO priority codes with Gantt color assignments

## Integration

- **[[module-WO|WO]]** — all SH operations read WORKORD; SH-A writes start/finish dates
- **[[module-RO|RO]]** — routing operation times (ROUTING/WOROUT) drive scheduling math
- **[[module-DC|DC]]** — BKDCLAB actual labor feeds Gantt for actual-vs-planned comparison
""",

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

## Database tables (live counts, 2026-07-01)

| Table | Records | Purpose |
|-------|--------:|---------|
| `ISGLDATE` | 1 | Current fiscal period boundary dates (12 CY + 6 prior years x 12) |
| `ISGLHDAT` | 18 | Historical period date registry — 7 years x 12 periods per row (84 date fields) |
| `ISGLBDGT` | 2,173 | Historical GL balances per account/dept: 4 years x 14 periods + year-end total |
| `ISGLCOA` | 2,181 | IS* shadow of BKGLCOA — financial statement formatter working set |
| `BKGLCOA` | 2,185 | Chart of accounts master (65 fields, acct#/dept/type/balance fields) |
| `BKGLTRAN` | 2,965,096 | GL transaction detail — source of all financial reports (2016-2026) |

**ISGLBDGT structure:** keyed on ISGL_ACCT + ISGL_GLDPT; TYPE(A/L/E/I), CR_DR, NON_CASH
flags; then ISGL_3YPAST_1..14, ISGL_4YPAST_1..14, ISGL_5YPAST_1..14, ISGL_6YPAST_1..14
(14 periods each = 12 months + 2 adjustment periods) + year-end totals for each year.
One row per COA account matches BKGLCOA (2,173 vs 2,185 — slight divergence from deletions).

**ISGLHDAT structure:** 84+ fields — ISGL_CYDATE_1..12, ISGL_1YDATE_1..12, through
ISGL_6YDATE_1..12 + ISGL_FYDATE + ISGL_EXTRA — stores period cutoff date boundaries
for 7 fiscal years. 18 records (vs ISGLDATE's 1 record) suggests one row per historical year maintained.

## Key AM operations

- **AM-A Reset Period-End Close Date** — updates ISGLDATE to advance the fiscal period gate
- **AM-B Fiscal Year End** — rolls BKGLCOA CURRENT→1YPAST→2YPAST balance fields; zeroes income
  statement; creates opening entry; populates ISGLHDAT with completed year's period dates
- **AM-Q Enter Budget Amounts** — writes budget figures to ISGLBDGT per account/period
- **AM-T Archive GL Detail** — moves BKGLTRAN rows older than N years to offline archive

## Integration

- **[[module-GL|GL]]** — AM-A/B control the period boundary that GL enforces on posting dates
- **[[module-AP|AP]]** — AM-J purges AP invoice and check history
- **[[module-AR|AR]]** — AM-K purges AR invoice history (complement to SA aging reports)
- **[[module-SM|SM]]** — SM-J handles operational archive (WO, PO, QC); AM handles accounting archive
""",

"AD": """
## What it does

Accounting Defaults — three screens that configure GL, checking accounts,
and AP module defaults. Part of the [[module-SD|SD]] System Defaults family,
but grouped under Accounting in the navigation bar.

## Menu operations

| Code | Operation | Program |
|------|-----------|---------|
| AD-A | General Ledger Defaults | T7DSGL.rwn |
| AD-B | Checking Accounts Defaults | T7DSCK.rwn |
| AD-C | Accounts Payable Defaults | T7DSAP.rwn |

Note: `AD-D Accounts Receivable Defaults` in some older versions is the same
as `AR-S` (AR Defaults). In this installation it is accessed via SD-P.

## Key table

All accounting defaults are stored in `BKSYMSTR` (286f) and `BKYSMSTR` (355f)
— the same global singletons used by every module.

## Integration

- **[[module-GL|GL]]** — AD-A sets the default posting period, account numbering, and COA structure
- **[[module-AP|AP]]** — AD-C sets terms, default vendor GL accounts, and check format
""",

# ── Modules added Pass 310 (2026-06-25) to eliminate all 45 module stubs ──

"LC": """
## What it does

Lot Control — assigns and tracks lot numbers for lot-controlled inventory items.
Each lot has its own on-hand quantity, receipt date, expiration date, cost, and
vendor/PO reference. Supports full lot traceability: from PO receipt through
WO assembly through SO shipment to a specific customer lot.
Symmetric structure to [[module-SC|SC]] (Serial Control).

## Menu operations

| Code | Operation | Program |
|------|-----------|---------|
| LC-A | Edit Lot Numbers | t7lca.rwn |
| LC-B | Assign Lot Control (per-item flag) | t7lcb.rwn |
| LC-C | Print Lot Availability | t7lcc.rwn |
| LC-D | Print Lot History | T7LCD.RWN |
| LC-E | Lot Control On Hand Report | t7lce.rwn |
| LC-F | Lot Traceability Report | t7lcf.rwn |
| LC-G | Archive Lots (with expiry date range) | T7LCG.RWN |

## Key tables

| Table | Fields | Purpose |
|-------|--------|---------|
| `LOT` | 25 | Active lot master (`MTLOT_*` prefix) — CODE+LOT PK |
| `BKLCMSTR` / `BKLCLOC` | — | Lot master and per-bin lot quantities |

**MTLOT.* 22-var namespace** (confirmed from T7LCA/LCG): CODE/LOT/EXPDATE/ONHAND/
LOC/VENDOR/RECDATE/RECQTY/POCOST/WO/WOCOST/NOTES_1..5/WOSUF/BEGIN/OUT/MAXOUT.

Fields of note:
- `EXPDATE` — expiry date for food/pharma compliance
- `POCOST` — landed cost at receipt
- `WOCOST` — assembled-into-WO cost
- `NOTES_1..5` — 5 free-text note lines per lot

## Integration

- **[[module-PO|PO]]** — lot assigned at PO receipt (POCOST/RECDATE/VENDOR)
- **[[module-WO|WO]]** — lot linked to WO material issue and assembly
- **[[module-SO|SO]]** — lot linked to SO shipment line for customer traceability
- **[[module-PI|PI]]** — PIBINLOT (14f) tracks lot quantities during physical count
- **[[module-SC|SC]]** — parallel serial module; an item can be both lot and serial controlled
""",

"SC": """
## What it does

Serial Control — assigns and tracks unique serial numbers for serial-controlled
inventory items. Provides complete lifecycle traceability: from PO receipt through
WO issue/assembly through SO shipment to a specific customer. Symmetric
structure to [[module-LC|LC]] (Lot Control).

## Menu operations

| Code | Operation | Program |
|------|-----------|---------|
| SC-A | Edit Serial Numbers | t7sca.rwn |
| SC-B | Assign Serial Control (per-item flag) | t7scb.rwn |
| SC-C | Print Serial Availability | t7scc.rwn |
| SC-D | Print Serial History | T7SCD.RWN |
| SC-E | Archive Serial Numbers | t7sce.rwn |
| SC-F | Serial Control Exception Report | t7scf.rwn |
| SC-G | Enter Serial Generation Parameters | t7scg.rwn |
| SC-H | Serial Traceability Report | t7sch.rwn |

## Key tables

| Table | Fields | Purpose |
|-------|--------|---------|
| `SERIAL` | 30 | Active serial number master (`MTSER_*` prefix) — PO cost, SO ship, WO codes |
| `SERIALH` | 30 | Archived serial numbers (identical structure) |
| `BKSCMSTR` | varies | SC module configuration (generation parameters) |

**MTSER.* 27-var namespace** in T7SCA: CODE/SERIAL/LOT/PO/RECDOC/VENDOR/RECDATE/POCOST/SO/CUSTCODE/SHIPDATE/SELLPRICE/WO/ISSDATE/ISSCOST/INRECDATE/INRECCOST/EXPDATE/WOCODE/NOTES/ONHAND/LOC/WOSUF/EXTRA/BIN/INV — full PO→WO→SO lifecycle per serial.

## Audit and fix (SC-F)

T7SCF performs 9 audit checks (orphans, duplicates, control changes, invalid
locations, unbalanced on-hand, unbalanced transactions, expired materials,
item type mismatches, negative on-hand) with 4 auto-fix modes.

## Integration

- **[[module-PO|PO]]** — serial assigned at PO receipt (POCOST/RECDATE/VENDOR)
- **[[module-WO|WO]]** — serial linked to WO during issue and assembly
- **[[module-SO|SO]]** — serial linked to SO shipment for customer traceability
- **[[module-LC|LC]]** — parallel structure; an item can be both lot AND serial controlled
""",

"RO": """
## What it does

Routings — defines the sequence of manufacturing operations (steps) for a
manufactured item. Each routing step specifies a work center, setup hours,
run hours per unit, queue time, and move time. Drives WO scheduling
(SH module) and lead-time calculation (MR module).

Also manages the supporting master data: work centers, machines, tools,
departments, QC codes, scrap codes, and operation templates.

## Menu operations

| Code | Operation | Program |
|------|-----------|---------|
| RO-A | Enter Routings | t7roa.rwn |
| RO-B | Print / Rollup Routing Costs | t7rob.rwn |
| RO-C | Work Centers | t7roc.rwn |
| RO-D | Enter Machines | t7rod.rwn |
| RO-E | Enter Tools | t7roe.rwn |
| RO-F | Enter QC Codes | t7rof.rwn |
| RO-G | Enter Scrap Codes | T7ROG.RWN |
| RO-H | Enter Departments | t7roh.rwn |
| RO-I | Enter Operation Templates | t7roi.rwn |
| RO-J-A | Print Routings | t7roja.rwn |
| RO-J-B | Print Work Centers | t7rojb.rwn |
| RO-J-C | Print Machines | t7rojc.rwn |
| RO-J-D | Print Tools | T7ROJD.RWN |
| RO-K | Enter Specifications Templates | t7rok.rwn |
| RO-M | Enter Testing Method | t7qcmthd.rwn |
| RO-N | Enter Testing Requirements | t7qcspec.rwn |
| RO-O | Routings Defaults | T7DSRO.RWN |
| RO-P | Update Processing Cost Standards | t7rop.rwn |

## Key tables

| Table | Fields | Purpose |
|-------|--------|---------|
| `ROUTING` | 62 | Routing operation (`MTRO_*` prefix) — header per item+operation |
| `BKRTEMTR` | 62 | E-routing mirror (identical structure) |
| `WORKCTR` | 47 | Work center master (`MTWC_*` prefix) — capacity, rates, calendar |
| `MACHINE` | 20 | Machine master (`TMACH_*` prefix) |
| `TOOL` | 57 | Tool/mold master (`MTOOL_*` prefix) — injection mold tooling |
| `BKRTTOOL` | — | Routing-to-tool link |
| `BKRTSPEC` | 7 | Routing specification notes |
| `BKRTCST` | 24 | Routing cost for quoting |
| `ISROUTEX` | 100 | Routing extended: 5-cycle arrays (notes/emp/WO/date/machine) |

## Integration

- **[[module-WO|WO]]** — WO creates WOROUT (WO routing) from ROUTING template at release
- **[[module-SH|SH]]** — scheduling reads WORKCTR capacity + ROUTING times for scheduling math
- **[[module-BM|BM]]** — BOM entry (T7BMA) shows routing on the BOM line (RTNUM link)
- **[[module-MR|MR]]** — MRP uses routing lead times for planned order due date calculation
""",

"WC": """
## What it does

Warehouse Control manages warehouse bin addresses for multi-location inventory.
It defines physical bin locations within each stock location, assigns items to
bins, and tracks bin-level on-hand quantities separately from total on-hand.

**Not to be confused with work centers** (production stations) — those are set
up under [[module-RO|RO]] routing option `RO-C Enter Work Centers`.

## Menu operations

| Code | Operation | Program |
|------|-----------|---------|
| WC-A | Enter Warehouse Bin Locations | — |
| WC-B | Assign Warehouse Control (per-location flag) | — |
| WC-C | Assign Bins to Items | — |
| WC-E | Print Bin Inventory Listing | — |
| WC-F | Print Bin Inventory Exceptions | — |
| WC-G | Warehouse Control Defaults | — |

## Key tables

| Table | Purpose | Live count (i2) |
|-------|---------|----------------|
| `ISBINLOC` | Item-bin-location record (9 fields): item, location, bin, UOH, created/updated dates, default-bin flag, extra, reorder level | 31,843 records |
| `BKICLOC` | Per-location on-hand quantities per item (32 fields): UOH/UOO/UOSO/UBO, lot/serial tracked qtys | per item per location |
| `ISBINLOT` | Bin + lot cross-reference | lot-tracked items |
| `PIBINLOC` | Bin-level count records during physical inventory | PI cycle only |

`ISBINLOC` key fields: `ISBIN_LOC_ITEM` (part#), `ISBIN_LOC_LOC` (location code),
`ISBIN_LOC_BIN` (bin code), `ISBIN_LOC_UOH` (units on hand at this bin),
`ISBIN_LOC_DFLT` (Y = default bin for this item).

**Live scale at i2 Systems:** 31,843 item-bin records across 10 locations and 1,272
distinct bin addresses.

## Warehouse Control concept

Without WC enabled, inventory is tracked per-location only (BKICLOC). With WC
enabled, inventory is additionally tracked per bin within a location. This
enables warehouse picking by bin address, and bin-level counts during PI.

A single item can have multiple bins within one location (primary + overflow).
The default bin (`ISBIN_LOC_DFLT = Y`) is used when picking for SOs or issuing
to WOs unless the user specifies otherwise.

## Integration

| Module | Relationship |
|--------|-------------|
| `IN` | BKICMSTR stores the default bin per item per location; WC-C assigns bins |
| `PI` | Physical Inventory counts at bin level flow into PIBINLOC |
| `HH` | Handheld scanners look up and confirm bin addresses during pick/ship/receive |
| `WO` | WO-G Issue Materials can specify the source bin; WO-I receipt can specify put-away bin |
""",

"HH": """
## What it does

Hand Held Programs — barcode scanner and mobile device integration for
shop-floor data collection: SO scan-and-ship, WO labor entry, material
issues, finished production receipt, PO receiving, physical inventory
counting, and bin-to-bin transfers. 32 T7HH* programs across 6 functional
groups. Shares BKDCLAB with the desktop [[module-DC|DC]] module.

## Menu operations

| Code | Operation | Program |
|------|-----------|---------|
| HH-A | Scan & Ship | t7hhssoe.rwn |
| HH-B | Print Labels | T7HHinga.rwn |
| HH-C | Issue Materials | T7HHWOG.RWN |
| HH-D | Enter Finished Production | T7HHWOP.RWN |
| HH-E | Enter Physical Counts | T7HHPIC.RWN |
| HH-F | Enter Labor | T7HHDCA.RWN |
| HH-G | Receive PO | T7HHPOC.RWN |
| HH-H | Enter Shipping Information | J7HHLITN.RWN (ISTS custom) |
| HH-I | Paperless Shop Floor Tracking | t7dcpsf.rwn |
| HH-J | Print WO Label | t7hhwolabel.rwn |
| HH-K | Transfer Inventory | t7hhinlj.rwn |
| HH-L | Multi-User Paperless Shop Floor | t7paperless.rwn |
| HH-M | Issue Scrap Component | t7hhwoscrap.rwn |

**Paperless Manufacturing** (T7PLess*.DFM forms — WO routing, BOM, QC specs
on screen) is accessed via HH-I and HH-L.

## Key functional groups

| Group | Programs | Purpose |
|-------|---------|---------|
| SO / Shipping | t7hhssoe + J7HHLITN + 8 more | Scan orders, print labels, ship |
| WO / Production | T7HHWOG/WOP/woscrap + 5 more | Issue materials, report FP, scrap |
| PO Receiving | T7HHPOC + 4 more | Receive POs with QC |
| DC Labor | T7HHDCA + 3 more | Time-clock labor entry for WO operations |
| Bin/Location | t7hhinlj + 1 more | Bin transfer, bin lookup |
| Physical Inventory | T7HHPIC | Count entry for PI cycle |

## Integration

- **[[module-DC|DC]]** — HH-F Enter Labor writes to BKDCLAB (same table as desktop DC)
- **[[module-PO|PO]]** — HH-G Receive PO writes to same BKQCMSTR/BKQCTRAN as T7POJC
- **[[module-WO|WO]]** — HH-C/D/M read WORKORD, WOBOM, and write INVTXN / WORECV
- **[[module-PI|PI]]** — HH-E writes to BKPIPHYS / PIBINLOC (same PI count tables)
""",

"QT": """
## What it does

Quotations / Estimating — **not a separate top-level menu module.** This code is
an alias for the [[module-ES|ES]] Estimates module. Quotes (estimates) are entered
and managed via the ES menu (ES-A through ES-E).

Key tables: `BKESTQT` (6,894 active quotes), `BKESTQTL` (462,727 lines). These
are byte-for-byte clones of `BKARINV`/`BKARINVL`.

See [[module-ES|ES]] for the full description and workflow.
""",

"RF": """
## What it does

RFQ (Request for Quotation) — not a standalone top-level menu module, but a
significant program group (`T7RFQ.RWN`, 103 procs) invoked from within the
[[module-PO|PO]] and [[module-MR|MR]] modules when requesting vendor quotes
before issuing a purchase order.

## Workflow

```
MR-G or PO vendor selection
  → T7RFQ launched to send quote requests to multiple vendors
  → vendors respond with prices for one or more quantity breaks
  → prices recorded in BKRFQ (49f, 10-break cost matrix)
  → winning vendor selected → PO-J Accept RFQ creates the PO
```

## Key tables

| Table | Fields | Purpose |
|-------|--------|---------|
| `BKRFQ` | 49 | RFQ header — 10 qty/cost breakpoints per vendor quote |
| `BKRFQDES` | 5 | RFQ description/address lines |
| `ISESTDTL` | 203 | Estimate detail tied to RFQ (cost breakdown per component) |

## Integration

- **[[module-PO|PO]]** — PO-J Accept RFQ creates a PO from the winning quote
- **[[module-MR|MR]]** — MR-G releases planned orders using BKSBVEND + RFQ for sourcing
- **[[module-ES|ES]]** — ES estimates can trigger RFQ via BKRFQ for vendor pricing
""",

"RT": """
## What it does

Report Templates — **not a standalone top-level menu module.** `RT` refers to the
Nevrona ReportBuilder `.RTM` file format and report engine used throughout EVO.

All EVO reports are `.RTM` files stored on the network share under `EVOReports\\`
(confirmed path: `\\\\i2s109-solidcrm\\EVOReports\\`). Reports are designed in
`RBDsgnr.exe` (Nevrona ReportBuilder 5.x).

## How RTM files work

```
TAS Pro 7 program (.RWN)
  → RBDsgnr/RBRun engine loaded
  → FILELOC.B maps config key → RTM filename
  → RTM file loaded → merged with Btrieve data → printed/previewed
```

## RTM file anatomy

RTM files are binary Delphi-format streams containing:
- Report header: title, page size, margins, orientation
- Band definitions: page header, group header, detail, group footer, page footer, summary
- Component list: TRBText, TRBDBText, TRBLine, TRBShape, TRBImage (all Delphi class names)
- Data pipeline: table name, filters, sort order

## Key files

| File | Purpose |
|------|---------|
| `RBDsgnr.exe` | ReportBuilder designer (visual report editor) |
| `FILELOC.B` | Maps EVO config keys to RTM filenames on disk |
| `EVOReports\\*.RTM` | All report templates (~300+ files) |
| `T6WOL*.RTM` | Work order listing reports (T6 era) |
| `T7*.RTM` | Current-era report templates |

Reports are called from TAS Pro programs via `RUNREPORT(configkey)` or equivalent
procedure call in `.RWN` programs. See [[module-UT|UT]] for report management utilities.
""",

"TA": """
## What it does

Tools / Admin Utilities — the EVO system maintenance and administration module.
Covers data backup/restore, software update application, data purging, company
setup, and system-wide configuration tasks.

## Menu operations

| Code | Operation | Notes |
|------|-----------|-------|
| TA-A | Rebuild Indexes | Rebuilds Btrieve index files for a table (fixes corrupted indexes) |
| TA-B | Rebuild All Indexes | Bulk index rebuild across all tables |
| TA-C | Pack Tables | Removes deleted-record slots from Btrieve files |
| TA-D | Pack All Tables | Bulk pack operation |
| TA-E | Table Statistics | Counts records, reports file sizes |
| TA-F | File Conversion | Migrates Btrieve file format versions |
| TA-G | Initialize Tables | Resets a table to empty (CAUTION: destructive) |
| TA-H | Table Copy | Copies a table to a backup file |
| TA-I | Company Setup | Configures company name, address, fiscal year, license |
| TA-J | Import Data | Processes `.IMP` import definition files |
| TA-K | Export Data | Exports table data to flat files |
| TA-L | Purge Data | Deletes old transactions by date cutoff |
| TA-M | Archive Data | Moves old transactions to archive tables |
| TA-N | Restore Data | Restores data from backup |
| TA-O | EVO Backups | Creates ZIP snapshot of all Btrieve data files |
| TA-P | Apply Updates | Applies `.UPD` patch packages to the database |

## Key concepts

- **Btrieve file repair**: TA-A/B/C/D are the first-line response to any
  "file error" or "status 22" Btrieve error — index corruption is common.
- **`.UPD` update files**: binary Btrieve-format patch packages delivered by
  EVO Support; TA-P reads and applies them. See [[module-UP|UP]] for detail.
- **Backup strategy**: TA-O creates a local ZIP; for network backup, the
  `\\\\i2s109-solidcrm\\DBAMFG$` folder should be backed up at OS level.

## Integration

- **[[module-SD|SD]]** — System Defaults overlap with TA-I Company Setup
- **[[module-SM|SM]]** — System Maintenance overlaps with TA rebuild/pack tools
- **[[module-PS|PS]]** — Password Security controls who can run TA operations
""",

"SY": """
## What it does

System — **not a standalone top-level module in standard EVO.**
User administration, access control, and company switching are split between:

- **[[module-PS|PS]]** — Password Security: user logins, access levels, module
  restrictions (`BKSLEVEL`, 422 fields — 5 access levels × ~84 modules).
  `PS-A Enter Users`, `PS-B Security Levels`.
- **[[module-SM|SM]]** — System Maintenance: company setup, system-wide
  parameters, and menu customization.
- **[[module-SD|SD]]** — System Defaults: company defaults and configuration.

`SY` appears as a shorthand alias in some contexts (e.g., inter-program calls)
but is not listed as a GROUPS entry in `BKMENUSU.TXT`. When EVO documentation
or an error message references `SY`, it means the PS/SM/SD cluster.

## Key table

`BKSLEVEL` (422 fields) — security level matrix: each of the 5 access levels
has a Y/N flag for every function in every module.
""",

"DE": """
## What it does

Data Exchange — the comprehensive import/export and EDI module. Far broader
than just EDI: DE handles bulk CSV/flat-file import for inventory, BOM,
routings, customers, vendors, GL chart, labor, material issues, finished
production, physical inventory, and AR/AP open items. Also manages EDI
trading-partner document exchange and web storefront order integration
(FTP, Shopify, file-based).

## Menu operations

| Code | Operation | Key programs |
|------|-----------|-------------|
| DE-A | Export Data | sqlexport.rwn |
| DE-B | Import Inventory | T7DEBB.RWN (import + validate + transfer) |
| DE-C | Import Bills of Material | T7DECB/DECC/DECD/DECE |
| DE-D | Import Routings | T7DEDB/DEDC/DEDD/DEDE |
| DE-E | Import Customers | T7DEEB/DEEC/DEED/DEEE |
| DE-F | Import Vendors | T7DEFB/DEFC/DEFD/DEFE |
| DE-G | Import Chart of Accounts | T7DEGB/DEGC/DEGD/DEGE |
| DE-H | Global Field Change | T7DEK.RWN |
| DE-I | Erase Files | t7del.rwn |
| DE-J | Import and Post Labor | t7deja/dejb/dejc/dejd/deje |
| DE-K | Import and Post Material Issues | t7dejh.rwn |
| DE-L | Import and Post Finished Production | T7WOP.RWN |
| DE-M | Import Physical Inventory Count | T7PIC.RWN |
| DE-P | EDI Interface (sub-menu) | Import/Edit/Convert/Export EDI |
| DE-Q | Import open Accounts Receivable | t7deq.rwn |
| DE-R | Import open Accounts Payable | t7der.rwn |
| DE-T | Import Sales Orders | FTP / Shopify / file web storefronts |
| DE-U | Upload Stock Balance to Web Storefront | J7BEFWEBINV.RWN (ISTS custom) |

## Import workflow pattern (for each data type)

```
DE-X-A  Generate Import Header (template/format definition)
DE-X-B  Import [Data]          (read flat file into staging table)
DE-X-C  Error Report           (validate staged data, report problems)
DE-X-D  Edit Imported [Data]   (fix staging errors interactively)
DE-X-E  Transfer to Master     (commit to production tables)
```

## EDI sub-menu (DE-P)

| Code | Operation |
|------|-----------|
| DE-P-B | Import EDI Orders (X12 850 PO from trading partner) |
| DE-P-C | Edit EDI Orders |
| DE-P-D | Convert EDI Orders to Sales Orders |
| DE-P-E | Export EDI Invoice/Acknowledgement (X12 810/997) |
| DE-P-F | Export EDI ASN (X12 856 Advance Ship Notice) |
| DE-P-H | EDI Error Report |

## Key tables

- `BKEDH` / `BKEDL` — EDI transaction headers/lines (staging)
- `BKEDNOTE` — EDI notes
- `BKEDPOST` — EDI posting queue

## Integration

Every production module writes to DE's target tables — DE-B imports feed
BKICMSTR (IN), DE-C feeds BKBMMSTR (BM), DE-J feeds BKDCLAB (DC), etc.
DE-T (Shopify/FTP orders) feeds BKARINV/BKARINVL (SO pipeline).
""",

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

"SU": """
## What it does

Query & Report Setup — the administration module for configuring the
interactive query and reporting infrastructure used by [[module-QU|QU]].
SU is for **system administrators**, not end users. It defines grid column
layouts, drill-down menu trees, and provides access to the forms/report editor.

## Menu operations

| Code | Operation | Program | Notes |
|------|-----------|---------|-------|
| SU-A | Maintain Grid Lookups | `wbklugrid.rwn` | Edit WBKLUGRID.DCY — defines columns, field bindings, keys for all grid views |
| SU-B | Maintain Drill Down Menus | `evoerpdrillm.rwn` | Configure drill-down menu trees (context menus on browse grids) |
| SU-C | Forms Editor | `reports.int` | Launches ReportBuilder designer (`RBDsgnr.exe`) for editing `.RTM` report templates |
| SU-D | Grid Maintenance | `t7gdm.rwn` | Low-level grid column/layout maintenance |

## Key concepts

**Grid lookups (SU-A / WBKLUGRID.DCY):**
The grid lookup system is defined in `WBKLUGRID.DCY` — a DCY file with a
non-standard format encoding column headers, field names, totals flags, and
external UDF procedure calls per grid. There are dozens of grid definitions
covering every browse screen in EVO (SO browse, PO browse, WO browse, etc.).
When users click a column header to sort, the WBKLUGRID definition drives the
available sort keys.

**Drill-down menus (SU-B / evoerpdrillm.rwn):**
ISDRILLM (drill-down menu table) stores context-menu definitions. When a user
right-clicks on a grid row, the drill-down menu shows related operations (e.g.,
right-click on a SO → "View Invoice", "Open WO", "Print Packing Slip"). SU-B
allows administrators to add, remove, or modify these context actions.

**Forms editor (SU-C):**
`reports.int` is an internal TAS Pro integration that launches `RBDsgnr.exe`
(Nevrona ReportBuilder) for editing report templates. This is the user-facing
equivalent of directly opening `EVOReports/*.RTM` files in the designer.

## Integration

- **[[module-QU|QU]]** — QU-E (Quick Grid Lookup) and QU-A (Master Inquiry)
  use grid layouts defined in SU-A
- **[[module-RT|RT]]** — SU-C is the EVO menu entry for the ReportBuilder designer
- **[[module-SM|SM]]** — SM has some overlap with SU for system-level configuration
""",

"UT": """
## What it does

Utilities — low-level administrative and data maintenance tools. Includes running
arbitrary DBA/TAS programs by name, file index rebuild, data location file editing
(FILELOC), system configuration, file layout reports, company create/delete,
and data correction utilities (clear data, search-and-replace, cost recalculation).

## Menu operations

| Code | Operation | Program |
|------|-----------|---------|
| UT-A | Run a DBA Program | runprg.int |
| UT-C | Re-Index File | t7reindex.rwn |
| UT-D | Edit Data Location File | wtasfloc.rwn (same as [[module-FL|FL]]) |
| UT-E | Set System Configuration | config.int |
| UT-H | Print File Layouts | t7uth.rwn |
| UT-I | Create/Delete Company | t7uti.rwn |
| UT-K-A | Clear Data | t7utka.rwn |
| UT-K-B | Search and Replace | T7FNR.RWN |
| UT-K-D | Recalc GL Chart of Accounts | t7utkd.rwn |
| UT-K-E | Consolidate Inventory Locations | T7UTKE.RWN |
| UT-K-F | Set Avg and Last Cost to Std Cost | t7utkf.rwn |
| UT-K-G | Recalc Inventory Book Value | t7utkg.rwn |
| UT-K-H | Recalc Avg Cost from FIFO/LIFO Bucket | T7UTKH.RWN |
| UT-K-I | Fix Binary Zeroes | t7bzfix.rwn |

**UT-D** opens the same `wtasfloc.rwn` as the [[module-FL|FL]] File Location Browser.
**UT-A** allows running any TAS Pro program by code — a superuser escape hatch.

## Integration

UT-I (Create/Delete Company) is the mechanism for adding a new company code;
it creates the FILELOC routing records and `.B<code>` file structure.
UT-K utilities are bulk data correction tools run after data migrations or errors.
""",

"LM": """
## What it does

Label Management / Label Printing — prints barcoded labels for inventory
items, lot numbers, serial numbers, and shipping cartons.

**Note:** LM is not confirmed as a separate top-level BKMENUSU group.
Label printing is integrated into multiple modules rather than being
a standalone menu.

## Label types and sources

| Label type | Where printed | Form / Program |
|------------|---------------|----------------|
| Lot tags | LC or WO receive | `t7lottag.DFM` (Evo Lot Tagging) |
| Item labels | IN or WC | `t7itemlbl.DFM` (item barcode label) |
| Shipping labels | SH / SO | part of the SH ship-confirm workflow |
| Work order traveler | WO | `T6WOLB2.RTM` (WO listing / traveler) |

## Key form: t7lottag.DFM

The `t7lottag.DFM` form (`Evo Lot Tagging`) has three label lines:
`Label1`, `Label2`, `Label3` — configurable text printed on the lot tag.
Fields include lot number, item code, quantity, date, and reference.

## Integration

- **[[module-LC|LC]]** — Lot Control: lot labels printed at LC-B Assign Lot Control
- **[[module-HH|HH]]** — HandHeld: barcode scanning uses labels generated here
- **[[module-WO|WO]]** — Work Order: WO travelers are printed via ReportBuilder RTM
- **[[module-SH|SH]]** — Scheduling/Shipping: shipping labels at ship-confirm
""",

"LO": """
## What it does

Locations / Bin Management — **not a separate top-level module.** Warehouse bin
and location management is handled by the [[module-WC|WC]] Warehouse Control module.

`WC-A Enter Warehouse Bin Locations` defines bins in `ISBINLOC`.
Per-bin on-hand quantities and bin-to-bin transfers are also managed from WC.

See [[module-WC|WC]] for Warehouse Control documentation.
""",

"MA": """
## What it does

Machine / Asset tracking — **not a separate top-level module.** Machine master
records (equipment assigned to work centers) are managed from the
[[module-RO|RO]] Routing module.

`RO-D Enter Machines` defines machines: machine number, work center, description,
and capacity. The `MACHINE` table (16 fields) stores the machine master.
Machines are referenced in routing steps to specify which machine runs each
operation.

[[module-DC|DC]] Data Collection can log labor entries against specific machines.

See [[module-RO|RO]] for Routing module documentation.
""",

"PL": """
## What it does

Pay Link — connects EVO to an external payroll service (Checkmark Payroll).
Exports employee time and labor data from EVO and imports the resulting paycheck
records back. Runs on T6-era programs (BK prefix).

**Paperless Manufacturing** (shop-floor workstation display of WO traveler, BOM,
QC specs, and routing notes) is accessed from [[module-HH|HH]] menu items
HH-I (Paperless Shop Floor Tracking) and HH-L (Multi-User Paperless Shop Floor),
not from PL.

## Menu operations

| Code | Operation | Program |
|------|-----------|---------|
| PL-A | Run Checkmark Payroll | T6PLA.RUN (T6 era) |
| PL-B | Import Employee Checks | BKPLB.RUN (T6 era) |
| PL-C | Import Employer Vouchers | BKPLC.RUN (T6 era) |
| PL-D | Payroll Link Setup | BKPLD.RUN (T6 era) |

## Integration

- **[[module-PR|PR]]** — internal EVO payroll; PL is for sites that use an external payroll service instead
""",

"PS": """
## What it does

Password Security — manages user accounts, password policies, module access
restrictions, menu access control, electronic approval signers, and field-level
access restrictions. The security administration hub for the EVO system.

## Menu operations

| Code | Operation | Program |
|------|-----------|---------|
| PS-A | System Users / Passwords | t7psa.rwn |
| PS-B | DBA System Security Levels | bkpsb.run (T6 era) |
| PS-C | DBA Company Logon Access | bkpsc.run (T6 era) |
| PS-E | Evo Menu Access by User Report | t7pse.rwn |
| PS-F | Evo Menu Access by Program Report | t7psf.rwn |
| PS-G | Maintain Menu Access Records | WBKMENUSETUP.RWN |
| PS-H | Configure Auto-Chain Programs | T7CHAIN.RWN |
| PS-I | Enter Approved Signers for Purchase Orders | T7DIGSIGADMIN.RWN |
| PS-J | Enter Contract Review Signers | T7CTREVUADMIN.RWN |
| PS-K | Enter Vendor Approval | J7appvend.rwn (ISTS custom) |
| PS-L | Enter Field Specific Access | T7LIMACC.rwn |

## Database tables

| Table | DDF | ODBC | Purpose |
|-------|-----|------|---------|
| `BKPSUSER` | 11f | 0 records (DBA DSN) | User account: code, password, security level, company, printer, menu, emp# |
| `BKSLMSTR` | 2f | not in DBA DSN | Security level master: level code + description |
| `BKSLEVEL` | 422f | not in DBA DSN | Security level menu access matrix — 20 menus x 20+ ops x flags |
| `BKSYLOG` | — | 0 records | Module access audit log (empty at i2 Systems) |

**BKPSUSER fields (11):** BKPS_USER_CODE (user ID, PK), BKPS_USER_PRT (default printer),
BKPS_USER_MENU (default menu), BKPS_USER_CMPY (company code), BKPS_USER_MWIND (window mode),
BKPS_USER_PSWD (encrypted password), BKPS_USER_ME (multi-entity Y/N), BKPS_USER_SEC
(security level → FK to BKSLMSTR), BKPS_USER_MCNTR (menu counter), BKPS_USER_LDATE
(last login date), BKPS_USER_EMP (linked employee code → FK to BKPRMSTR).

**BKSLEVEL (422 fields):** Key = BKSL_MENU (menu# 1-20) + BKSL_LEVEL (2-char level code).
Then BKSL_MENU1_YN/BKSL_MENU1_1..N through BKSL_MENU20_* — one flag per menu operation
per security level. A security level with all YN=Y = unrestricted access to that menu.

**Why BKPSUSER shows 0 records via DBA DSN:** The DBA DSN is configured for the DBAMFG$
database on the network share. BKPSUSER.B lives there but may be registered under a
different logical name, or users are stored in a company-specific BKPSUSER.B variant
rather than a shared one.

## Integration

- **[[module-SY|SY]]** — SY-A Enter Users is the T7 user entry screen backed by BKPSUSER
- **[[module-US|US]]** — US-D Change Password is user-facing; PS-A is admin view of same data
- **[[module-CR|CR]]** — PS-J configures the contract review approvers (T7CTREVUADMIN)
- **[[module-PO|PO]]** — PS-I configures digital signature approvers for purchase orders
""",

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
components. Defines which manufacturers, vendors, and approved part numbers are
valid for each component, keyed by component + product assembly + customer.
During purchasing, the system validates that the selected source is on the AVL.

**SB has no standalone top-level menu.** AVL data is accessed from BM sub-menus
and enforced automatically by PO and IN module transactions.

**Scale (2026-07-01):** 8,271 approved manufacturer sources + 5,354 approved vendor
sources + 319 approved substitutes = 13,944 total AVL records at i2 Systems.

## Tables (live counts, 2026-07-01)

| Table | Records | Fields | Purpose |
|-------|--------:|--------|---------|
| `BKSBMFG` | 8,271 | 6 | Approved manufacturer source: component + assembly + customer + MFG code + MFG part# |
| `BKSBVEND` | 5,354 | 6 | Approved vendor source: component + assembly + customer + vendor + vendor part# |
| `BKSBPART` | 319 | 5 | Approved substitute parts: component + assembly + customer + substitute part# |

**AVL key structure (all three tables):**
- `BKSB_*_PARNT` (STRING 15) — component item code (the part being sourced)
- `BKSB_*_PROD` (STRING 15) — top-level product/assembly that uses this component
- `BKSB_*_CUST` (STRING 10) — customer code (blank = applies to all customers)

This 3-key design means AVL rules can be **customer-specific**: two customers can
require different approved manufacturers for the same component in the same assembly.

## BKSBMFG — Approved Manufacturer Source (6 fields)

| Field | Meaning |
|-------|---------|
| `BKSB_MFG_PARNT` | Component item code (PK part 1) |
| `BKSB_MFG_PROD` | Product assembly (PK part 2) |
| `BKSB_MFG_CUST` | Customer code (PK part 3, blank=any) |
| `BKSB_MFG_MANUF` | Approved manufacturer code |
| `BKSB_MFG_MPART` | Manufacturer's part number |
| `BKSB_MFG_EXTRA` | Extra / notes |

## BKSBVEND — Approved Vendor Source (6 fields)

| Field | Meaning |
|-------|---------|
| `BKSB_VEND_PARNT` | Component item code |
| `BKSB_VEND_PROD` | Product assembly |
| `BKSB_VEND_CUST` | Customer code |
| `BKSB_VEND_VEND` | Approved vendor code |
| `BKSB_VEND_VPART` | Vendor's part number |
| `BKSB_VEND_EXTRA` | Extra / notes |

## Access points

| Location | Program | What it does |
|----------|---------|-------------|
| BM-J | T7BMJ.RWN | Enter approved substitutes (BKSBPART) |
| BM-K | T7BMK.RWN | Enter approved vendors (BKSBVEND) |
| BM-L | T7BML.RWN | Enter approved manufacturers (BKSBMFG) |
| PO receive | T7POENG.RWN | Validates BKSBVEND on engineering receipts |
| MRP | T7MRG.RWN | Uses BKSBVEND / BKSBMFG to select vendor at planned-order release |

## Integration

- **[[module-BM|BM]]** — AVL data managed from BM browse/entry screens (BM-J/K/L)
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

"SD": """
## What it does

System Defaults — consolidated access to all module defaults screens. Each
SD sub-menu opens the defaults entry form for a specific EVO module. This is
where the system administrator configures default values, numbering sequences,
and behavioral flags for every module without needing to navigate into each
module's own menu.

## Menu operations (defaults screens)

| Code | Defaults screen | Key program |
|------|----------------|-------------|
| SD-A | Company Defaults | T7DSCO.rwn |
| SD-B | Work Order Defaults | t7dswo.rwn |
| SD-C | Purchase Order Defaults | t7dspo.rwn |
| SD-D | MRP Defaults | t7dsmrp.rwn |
| SD-E | Scheduling Defaults | t7dssh.rwn |
| SD-F | Data Collection Defaults | t7dsdc.rwn |
| SD-G | Estimating Defaults | t7dsest.rwn |
| SD-H | Inventory Defaults | t7dsic.rwn |
| SD-I | Routings Defaults | t7dsro.rwn |
| SD-J | Bills of Material Defaults | t7dsbom.rwn |
| SD-L | Features and Options Defaults | t7dsfo.rwn |
| SD-M | Sales Orders Defaults | t7dsso.rwn |
| SD-N | Sales Commissions Defaults | t7dscs.rwn |
| SD-O | Contact Manager Defaults | t7dscm.rwn |
| SD-P | Customer / AR Defaults | t7dsar.rwn |
| SD-Q | Master Default Settings | t7mdefaults.rwn (495-key BKYSMSTR editor) |
| SD-R | Assign Next Document Numbers | t7numdef.rwn |
| SD-S | Warehouse Control Defaults | t7dswc.rwn |
| SD-T | Service / RMA Defaults | t7dsrma.rwn |
| SD-U | Hand-Held Defaults | t7dshh.rwn |
| SD-V | International Settings Defaults | T7DSIM.RWN |

`SD-Q Master Default Settings` is the most powerful: it opens `T7MDefaults.rwn`,
the full 495-key BKYSMSTR editor with all ISTS.CFG.* flags, YN slots, numbering,
and module parameters. See [[recipe-configure-defaults]].

## Integration

All SD defaults are stored in `BKYSMSTR` (355f) and `BKSYMSTR` (286f). Every
module reads its operational defaults from those singletons at runtime.
""",

"CM": """
## What it does

Contact Master — the CRM (Customer Relationship Management) module. Manages
customer and prospect account records, contact history, reminders, campaigns,
and activity tracking. Closely integrated with AR (customer accounts) and SO.

## Menu operations

| Code | Operation | Program |
|------|-----------|---------|
| CM-A | Enter Contact Accounts | t7cma.rwn |
| CM-B-B | Print Accounts Listing & Labels | t7cmbb.rwn |
| CM-B-C | Print Reminders | T7REMINDRPT.RWN |
| CM-B-F | Print Notes | evonotesrpt.rwn |
| CM-C | CRM Dashboard | t7jcrm.rwn (Java) |
| CM-J | Change Account Codes | t7cmj.rwn |
| CM-K | Add Customers to Account File | t7cmk.rwn |
| CM-M | Contact Manager Defaults | T7DSCM.RWN |

## Key tables (BKCM* family — 46 tables)

Most BKCM* tables are **Btrieve-only** (not in Pervasive DDF) — cannot be
queried via SQL/ODBC; only accessible through TAS Pro or the Java CM bridge.

| Table | Fields | Purpose |
|-------|--------|---------|
| `BKCMCUST` | 106 | Customer CRM account (links to BKARCUST) |
| `BKCMACCT` | 41 | Prospect / non-customer account |
| `BKCMACCN` | 154 | Account notes + 10 contacts per account |
| `BKCMACTH` | 21 | Activity history (START/STOP/billing) |
| `BKCMACTF` | 11 | Follow-up + SO link |
| `BKCMMHST` | 72 | Campaign / mailing history (20-class filter) |
| `BKCMREP` | 14 | Sales rep access flags |
| `BKCMTERR` | 2 | Territory codes |
| `BKCMDUN` | 36 | 10-level dunning ladder |
| `MKAHIST` | 9 | Activity history log (used by 158 programs) |

## Integration

- **[[module-AR|AR]]** — BKCMCUST links to BKARCUST; CM-K imports AR customers into CRM
- **[[module-SO|SO]]** — SO module reads BKCMACTH for quote-to-order history
- **[[module-SA|SA]]** — SA reports can filter by BKCMTERR (territory) and BKCMLEAD (lead source)
""",

"CP": """
## What it does

Credit and Payment processing — **not a separate top-level module.** Credit card
and payment processing for customer accounts is handled within the
[[module-AR|AR]] Accounts Receivable module.

AR-B Enter Cash Receipts processes payments including credit card transactions.
Credit limit management is in the customer master (`AR-A Enter Customers`,
`BKARCUST.CRLIMIT`). Credit hold release is in [[module-CR|CR]] Contract Review.

See [[module-AR|AR]] for Accounts Receivable documentation.
""",

"CR": """
## What it does

Contract Review — an electronic approval workflow that requires designated
department managers to sign off on a Sales Order before it can proceed to
fulfillment. Prevents unapproved orders from shipping.

## Menu operations

| Code | Operation | Program |
|------|-----------|---------|
| CR-A | Assign Departments to SO | T7SOREVUADMIN.RWN |
| CR-B | Enter SO Approvals | T7SOREVU.RWN |

## Workflow

```
SO created → CR-A assigns review departments to the SO
           → CR-B displays pending SOs awaiting approval
           → each department approver signs off (ISCTREVU: employee + MOTPAS signature)
           → when all departments approve → SO released for fulfillment
```

## Key tables

- `ISSOREVU` (SR module, part of IS* family) — SO review pending records
- `ISCTREVU` (17f) — contract review sign-off: employee code + MOTPAS signature

## Integration

- **[[module-SO|SO]]** — SO header status blocked until CR approval clears
- **[[module-PS|PS]]** — PS-J Enter Contract Review Signers configures who can approve
- **[[module-US|US]]** — US-H Update Contract Review Password manages the approval PIN
""",

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

"FL": """
## What it does

File Location Browser — a TAS Pro 7 built-in administrative utility that allows
any registered Btrieve table to be browsed interactively at runtime. Accessed via
`WTASFLOC.RWN`. Not a business module — it is a low-level data inspection tool for
system administrators and developers.

**FL has no standalone top-level menu entry.** It is invoked directly by name
(FL) in the TAS Pro launcher or from the SU/SM admin areas.

## Key facts

- Opens `FILELOC.B` (the runtime file-location registry) which maps 386+ logical
  table names to their physical `.B` file paths
- From FILELOC, the user selects any table and FL opens it for browse/edit
- 74-table database fingerprint: FL reads all FILELOC-registered tables
- Programs: `WTASFLOC.RWN` (22 procs, source: `wtasfloc.SRC`) — one of the few
  readable `.SRC` files on the network share

## Key namespaces (confirmed from wtasfloc.SRC)

- `LOC_*` — FILELOC fields (LOC_BUFF_NAME / FILE_NAME / COMP_CODE / REC_SIZE / REC_TYPE / LOCATION / DESCRIPTION / HNDL)
- `DICT_*` — FILEDICT fields (13 vars: field name, offset, type, size, dec, array, etc.)
- `CF_*` — current file selection (CF_FLNAME / CF_FLCODE / CF_RTYPE / CF_DESC / CF_PATH / CF_FDNAME)

## Integration

- **[[module-SU|SU]]** — SU-related admin path for data inspection
- **[[module-SM|SM]]** — SM-J file maintenance context for Btrieve data verification
""",

"FO": """
## What it does

Features and Options — the product configurator module. Allows configurable
inventory items to be set up with selectable features (e.g., fabric, cushion
style, leg finish, welt color) that the customer picks at order entry time.
EVO explodes the correct BOM variant automatically from the selected options.

At i2 Systems, FO drives the **upholstery product line** (sofas, chairs, sectionals)
where each order specifies dozens of configurable attributes. The ISFO* custom
table family extends the standard EVO FO module with full workflow tracking
(Copied → Tagging → Completed → Cvt toSO). As of 2026-07-01: 10,842 configuration
sessions in ISFOHEAD with 934,922 BOM lines across those sessions.

## Menu operations

| Code | Operation | Program |
|------|-----------|---------|
| FO-A | Set up Features and Options | T7FOA.RWN |
| FO-B | Print Features and Options | T7FOB.RWN |
| FO-C | Enter Option Prices | T7FOC.RWN |
| FO-D | Print Option Prices | T7FOD.RWN |
| FO-E | Print Option Where Used | T7FOE.RWN |
| FO-F | Feature and Option Defaults | T7DSFO.RWN |
| FO-G | Configure Item | EvoFNO.RWN |

## Database tables (live counts, 2026-07-01)

| Table | Records | Purpose |
|-------|--------:|---------|
| `BKFOCFG` | 1 | F/O global config flags (MANFET + 15 YN flags, OPCODE) |
| `ISFOHEAD` | 10,842 | Configuration session header: parent item, customer, date, status |
| `ISFOLINE` | 934,922 | BOM lines per session: 50 OPFLAG bits + component, qty, op, price |
| `ISFOHIST` | 25,338 | Workflow history per session: status transitions with WHO/DATE/TIME |
| `ISFOBMRM` | 11,890 | BOM remarks: up to 15x64-char remark fields per component |
| `ISFOORDL` | 8 | Live order lines from active conversions (transient staging) |

## ISFOHEAD — Configuration Session Header (16 fields)

| Field | Type | Meaning |
|-------|------|---------|
| `ISFO_HDR_UID` | STRING 40 | Unique configuration ID (PK) |
| `ISFO_HDR_PARENT` | STRING 15 | Parent item# being configured |
| `ISFO_HDR_DATE` | DATE | Configuration date |
| `ISFO_HDR_DESC` | STRING 30 | Description / order ref |
| `ISFO_HDR_CUST` | STRING 10 | Customer# |
| `ISFO_HDR_VEND` | STRING 10 | Vendor# (if vendor-driven) |
| `ISFO_HDR_RFQ` | STRING 20 | RFQ reference# |
| `ISFO_HDR_STATUS` | STRING 15 | Workflow status (see below) |
| `ISFO_HDR_REV` | STRING 5 | Revision# |
| `ISFO_HDR_MDATES_1..5` | DATE x5 | 5 milestone dates |
| `ISFO_HDR_PERM` | STRING 1 | Permanent flag |
| `ISFO_HDR_EXTRA` | STRING 150 | Extra / user-defined |

**Status values (from live data):**

| Status | Count | Meaning |
|--------|------:|---------|
| Completed | 3,071 | Configuration finalized |
| Copied | 544 | Copied from another session |
| Cvt toSO XXXXX | ~700 total | Converted to SO# XXXXX |
| (blank) | 19 | In-progress / draft |

**Top configured parent items:** A3120Z-31HAE (869 sessions), E1150Z-11CAB (564),
A3120Z-11HAE (331), A3120Z-31HCE (299) — all upholstered seating SKUs at i2.

## ISFOLINE — BOM Lines per Session (78 fields)

50 ISFO_LIN_OPFLAG_N (STRING 1 each) encode which option flags apply to this
BOM component. Additional fields: LEVEL, PARENT, LINEN, COMP (part#), QTYREQ,
REF, TYPE, SCRAP, OP (operation code), 6 OPYN flags, PRICE, RTNUM, DUPOP, OPDSC,
VEND, DATE1/2, REV, PBRANC, CBRANC. 934,922 lines across 10,842 sessions = avg
86 BOM lines per configuration session.

## ISFOHIST — Workflow History (15 fields)

Records every status transition: WHO (user), DATE, TIME, STATU (new status),
PART (item changed), CVTTO (conversion type: SO/WO), CVTNO (target document#),
CITEM (converted item), QTY, LOC, CV, DDATE, PRICE.

**History status distribution:** Copied (10,806), Completed (7,231), Tagging (93),
Cvt toSO (various SO#s, ~700 total) — matches ISFOHEAD status lifecycle.

## Integration

- **[[module-SO|SO]]** — FO-G launches from SO-A when item has OPT flag set; ISFOHIST
  CVTTO='SO' records link configuration sessions to Sales Orders
- **[[module-BM|BM]]** — BKFOCFG and ISFOLINE are in T7BMA DB fingerprint; BOM variants
  stored as ISFOLINE OPFLAG bit patterns
- **[[module-IN|IN]]** — BKICMSTR OPT flag enables the FO dialog for that item
- **[[module-WO|WO]]** — ISFOHIST CVTTO='WO' records show direct WO conversions
""",

"FP": """
## What it does

Forecast / Planning — **not a separate top-level module.** Sales forecasting
and planning horizon management are functions within the [[module-MR|MR]]
MRP (Material Requirements Planning) module.

MR-A Enter MPS Forecast / MR-B Review MPS Forecast manage forecast demand
quantities by item and period. The planning horizon (buckets, periods) is
configured in [[module-SD|SD]] System Defaults.

See [[module-MR|MR]] for MRP and forecasting documentation.
""",

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

"IM": """
## What it does

International Module — multi-currency support and landed cost tracking.
Enables EVO to process transactions in foreign currencies, maintain exchange
rates, and capture landed costs (duties, customs fees, freight) on imported
purchase orders.

## Menu operations

| Code | Operation | Program |
|------|-----------|---------|
| IM-A | International Configuration | T7DSIM.RWN |
| IM-B | Enter Multiple Currencies | t7imb.rwn |
| IM-C | Enter Currency Exchange Rates | t7imc.rwn |
| IM-D | Enter Landed Cost Defaults | t7imd.rwn |
| IM-E | Enter Landed Cost Duty Codes | t7ime.rwn |
| IM-F | Enter Landed Cost Customs Fees | t7imf.rwn |
| IM-H | International Defaults | T7DSIM.RWN |

## Key tables

- `MTEXCHG` (7f) — multi-currency exchange rate master (Java entity class confirmed)
- `ISLANDF` (6f) — landed cost GL account mapping
- `ISMCF` (49f) — multi-currency configuration
- `ISMCR` (22f) — exchange rate history (ISTS multi-currency)

## Integration

- **[[module-AP|AP]]** — foreign currency POs converted using IM exchange rates
- **[[module-AR|AR]]** — multi-currency AR invoices use MTEXCHG rates
- **[[module-GL|GL]]** — currency gain/loss posts to GL on settlement
- Auto FX rate update: `T7AUTOFX.RWN` uses OANDA API (key in ISTS.CFG.FXKEY) to
  update MTEXCHG rates automatically via ISJAVA task queue
""",

"IS": """
## What it does

ISTS Custom Enhancements — **not a standard EVO top-level module.**
`IS` is the prefix used for i2 Systems (ISTS) database enhancements and
custom programs added on top of the standard EVO install.

## What lives under IS*

| Family | Description |
|--------|-------------|
| `ISAP*` | AP enhancements (11 tables) |
| `ISAR*` | AR enhancements (22 tables) |
| `ISES*` | Estimating enhancements (7 tables; ISESTAQT=5,816 archived quotes) |
| `ISSO*` | SO enhancements (9 tables) |
| `ISSR*` | Service/RMA (10 tables — ISRMAI, ISRMAINV, etc.) |
| `ISWO*` | WO enhancements (6 tables) |
| `ISGL*` | GL enhancements (6 tables) |
| `ISPR*` | Payroll enhancements (5 tables) |
| `ISPO*` | PO enhancements (5 tables) |
| `ISFO*` | Features/Options enhancements (5 tables) |
| `ISQC*` | QC enhancements (3 tables) |
| `ISIC*` | Inventory cycle enhancements (4 tables) |
| `ISBINLOC` | Warehouse bin locations (used by [[module-WC|WC]]) |

## Custom programs

Programs with `J7` prefix or `ASSIGN(" - ISTS Enhancement MM/DD/YY")` in source
are i2 Systems customizations. Example: `T7GFPRICE.DFM` (Golding Farms pricing).

The IS table family is fully accessible via Pervasive PSQL ODBC (unlike BKCM* tables).
""",

"LW": """
## What it does

Lottery / Weighted Allocation — specialty allocation module. When demand for
a lot-controlled or supply-constrained item exceeds available quantity, LW
provides a weighted or lottery-based fair-allocation mechanism across open
sales orders.

**Not confirmed as a top-level menu module in BKMENUSU.TXT.** This may be a
site-specific or optional module installed at select customers. Not observed
in the i2 Systems EVO instance.

If available, the LW module would integrate with [[module-SO|SO]] Sales Orders
and [[module-LC|LC]] Lot Control to allocate lot quantities across competing orders.

*Status: unverified — module presence at i2 is unknown.*
""",

"PC": """
## What it does

Product Configuration — **not a separate top-level module.** Product configuration
in EVO is the [[module-FO|FO]] Features and Options module.

`FO-A` defines features and option sets for configurable items. When a configured
item is entered on a Sales Order, the F/O dialog (launched from `SO-A`) presents
the option choices and builds the item's configuration record.

See [[module-FO|FO]] for the full Features and Options module documentation.
""",

"QU": """
## What it does

Queries & Reports is the interactive inquiry and cross-module reporting hub.
It contains master inquiry screens, calendar drill-downs, business status
dashboards, quick grid lookups, and a live SQL query executor. This is the
primary module for ad-hoc data lookup when a specific module's built-in
reports don't answer the question.

## Menu operations

| Code | Operation | Program | What it does |
|------|-----------|---------|-------------|
| QU-A | Master Inquiry | t7csi.rwn | Cross-module grid: search items, customers, vendors, WOs, SOs, POs by any key field |
| QU-B | Calendar Drill Down | caldrillbt.rwn | Click any date to see what WOs/SOs are scheduled for that day |
| QU-C | Calendar Summary Report | isshpcal2.rwn | Printable monthly calendar of scheduled shipments / WO completions |
| QU-D | Business Status (Java) | t7jbs.rwn | KPI dashboard: open orders, backlog value, inventory turns |
| QU-E | Quick Grid Lookup | t7qgrid.rwn | Configurable quick-search grids for common lookups |
| QU-F | Query Executor (live SQL) | queryexecute.rwn | Ad-hoc Pervasive SQL against any table via JDBC |

## QU-F: Live SQL Query Executor

The most powerful tool in the QU module. `QUERYEXECUTE.RWN` launches
`EvoPVT.jar` directly (via JAVA.NAME) to run arbitrary SQL against the
Pervasive database via JDBC. This is the **only user-facing ad-hoc SQL
interface** in EVO — all other reports are fixed RTM templates.

Use cases: custom data extracts, verifying table contents, building
one-off reports that don't exist in the standard menus.

Access restriction: typically limited to IT/admin users via PS-B security
levels because raw SQL can read any table.

## QU-D: Business Status Dashboard

`ISJBSF` table (143 fields) stores the KPI metrics displayed in the
Java Business Scorecard. The scorecard summarizes: open SO backlog,
WO work-in-progress value, inventory on-hand value, on-time delivery
%, and other business metrics. Updated on schedule or on-demand.

## QU-A: Master Inquiry Grid

`t7csi.rwn` provides a unified search grid across modules. You can look
up an item number and see: on-hand qty, open SOs, open POs, open WOs,
current BOM, and routing — all from a single inquiry. This is the
"where-is-my-stuff" tool for production and customer service.

## Integration

| Module | Relationship |
|--------|-------------|
| `SU` | SU-A/D configures the grid layouts and drill-down column sets |
| `RT` | QU-B/C calendar reports use RTM report templates |
| `All` | QU-F SQL executor can query any of the 659 registered tables |
""",

"AB": """
## What it does

Address Book — **not a separate top-level module.** A shared address and
contact repository is provided by the [[module-CM|CM]] Contact Master module
(BKCM* family, 46 tables).

Customer addresses are managed in [[module-AR|AR]] (`AR-A`, `BKARCUST`).
Vendor addresses are in [[module-AP|AP]] (`AP-A`, `BKAPVEND`).
Ship-to addresses for customers are sub-records under BKARCUST.

The Contact Master (CM) module provides the unified contact directory spanning
customers, prospects, and companies. See [[module-CM|CM]] for full documentation.
""",

"AC": """
## What it does

Accounting Consolidation — **not a separate top-level module.** Multi-company
GL consolidation is performed from the [[module-AM|AM]] Accounting Management
module.

`AM-G Consolidate Financials` rolls up subsidiary company trial balances into
a parent company for consolidated financial statements. The [[module-IM|IM]]
International Module handles multi-currency translation adjustments before
consolidation.

See [[module-AM|AM]] for Accounting Management documentation.
""",

"DI": """
## What it does

Distribution / Drop-Ship — **not a separate top-level module.** Drop-ship order
management (where a vendor ships directly to the customer) is handled within
[[module-SO|SO]] Sales Orders and [[module-PO|PO]] Purchase Orders.

When a SO line is flagged as drop-ship:
1. SO-A marks the line with the drop-ship flag
2. PO is generated linked to that SO line via `BKSOPO` (SO/PO link table)
3. The vendor ships to the customer address from the SO — goods never enter your warehouse
4. AP invoice closes the PO; AR invoice closes the SO

See [[module-SO|SO]] for drop-ship sales order entry and [[module-PO|PO]] for the
linked purchase order workflow.
""",

"EX": """
## What it does

Export / Exchange — **not a standalone top-level module.** Data export to
external systems is a function available across multiple EVO modules.

Key export mechanisms:
- **[[module-DE|DE]]** Data Exchange — the primary module for structured
  data interchange (EDI, flat-file import/export definitions using `.IMP` files)
- **[[module-TA|TA]]** Tools Admin — `TA-K Export Data` exports raw table
  contents to flat files
- **[[module-QU|QU]]** Queries & Reports — `QU-F Query Executor` allows
  ad-hoc SQL output via `queryexecute.rwn` (Java JDBC)

The DE module handles integration-oriented export (trading partner EDI,
formatted interfaces). Use TA-K for simple data dumps.
""",

"MM": """
## What it does

Material Management — **not a separate top-level module.** Safety stock,
reorder points, and min/max replenishment planning are managed within the
[[module-MR|MR]] MRP module and [[module-IN|IN]] Inventory.

- `IN-A Enter Items` stores `BKICMSTR.REORDER_PT` and `BKICMSTR.SAFETY_STK`
- MR-F runs MRP and generates planned orders based on reorder points when
  demand-driven MRP is not being used
- Min/max replenishment (order-up-to logic) uses `BKICMSTR.ORDER_QTY`

For full material requirements planning, see [[module-MR|MR]].
For item-level safety stock and reorder point setup, see [[module-IN|IN]].
""",

"UM": """
## What it does

Unit of Measure Conversion — **not a separate top-level module.** UOM
conversion factors are defined within the [[module-IN|IN]] Inventory module.

`IN-A Enter Items` stores `BKICMSTR.PURCH_UM` (purchasing UOM), `STOCK_UM`
(stocking UOM), and `SELL_UM` (selling UOM) plus the conversion factors
between them. System-wide UOM codes are defined in [[module-SD|SD]] System Defaults.

See [[module-IN|IN]] for Inventory and [[module-SD|SD]] for UOM code setup.
""",

"UP": """
## What it does

Updates / Patches — **not a separate top-level module.** EVO software update
application is handled by [[module-TA|TA]] Tools Admin, `TA-P Apply Updates`.

## How EVO updates work

EVO Support delivers patch packages as `.UPD` files — Btrieve-format files
containing table modifications, new records, or program replacements.

```
TA-P Apply Updates
  → browse to .UPD file on disk
  → TA-P reads Btrieve records from .UPD
  → applies each record to the target table
  → logs which updates were applied (prevents double-apply)
```

Network share programs (`.RWN`, `.RTM`, `.DFM`) are updated by Support directly
copying new versions to `\\\\i2s109-solidcrm\\DBAMFG$\\` — no `.UPD` needed for
program files, only for database-structure changes.

See [[module-TA|TA]] for the full Tools Admin module including TA-P.
""",

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

"TAS": """
## What it does

TAS (System Configuration) — the EVO system diagnostics and data-dictionary
integrity group, listed under "System Mgr" in the EVO menu.

There is currently only one item in this group:

| Code | Operation | Program |
|------|-----------|---------|
| TAS-S | Data Dictionary Check | T7DDCHECK.RWN |

## TAS-S Data Dictionary Check

`T7DDCHECK.RWN` scans the Pervasive PSQL DDF (Data Dictionary Files) and
verifies that every table listed in the DDF still exists on disk and that
all declared fields are present and sized correctly. Reports discrepancies
between the DDF schema and the physical `.B` files.

This is typically run after an EVO update or after a database recovery to
verify schema integrity before resuming production.

## Integration

- **[[module-TA|TA]]** — TA-A/B rebuild indexes; TAS-S checks schema validity
- **[[module-SM|SM]]** — SM tools also cover table maintenance
""",

"LI": """
## What it does

License / Module Access — controls which EVO modules are enabled for this
installation and provides field-level access restriction for licensed features.

`LI` is accessed via `T7LIMACC.RWN` (42 procedures, NZLICE.LIB library).

## What LI manages

**Module licensing gates** (ISTS.CFG flags read from BKYSMSTR):
EVO is modular — features like RMA, Features/Options, EDI, DC Barcoding, and
lot/serial control are separately licensed. `ISTS.CFG.*` flags in BKYSMSTR
(YN[102]–YN[143], one per BKMENUSU GROUP) control which modules are active.

T7LIMACC reads these flags at startup and selectively enables/disables menu
items and form fields depending on what is licensed.

**Field-level access control** (ISACCESS table):
Beyond module-level gating, LI provides per-form, per-field access restriction.
Each object in a DFM form can be marked as view-only, hidden, or restricted to
specific security levels. ISACCESS (8 fields: NAME/OBJ/OBJTYPE/DFM/FIELD/STATUS/TEXT/EXTRA)
stores these per-field restrictions.

## Key tables

| Table | Fields | Purpose |
|-------|--------|---------|
| `ISACCESS` | 8 | Per-DFM/per-field access restriction records |
| `BKSYHELP` | 1 | Help message text for restricted fields |
| `DBAHLPID` | 2 | Help ID cross-reference |
| `MKAHIST` | 9 | Activity history — access-grant events logged here |

## How field access works

```
T7LIMACC scans DFM form file
  → reads TAS form component names + captions
  → matches each to ISACCESS by form name + object name
  → applies STATUS restriction per field:
      0 = no restriction
      1 = view-only (gray out)
      2 = hidden
      3 = security-level restricted
```

## System configuration center

T7LIMACC also doubles as the **global EVO system configuration center** —
it reads and writes all ISTS.CFG.* flags (hundreds of behavior flags from
BKYSMSTR), EVO.CFG.* user preferences, EMAIL.CFG.* SMTP settings, and the
6 HOTBUTTON toolbar shortcuts. This makes it the primary tool for system
administrators configuring EVO behavior across all modules.

## Integration

- **[[module-PS|PS]]** — PS manages user-level security levels; LI manages
  field-level access and module licensing on top of security levels
- **[[module-SD|SD]]** — SD is the user-facing System Defaults; LI is the
  internal implementation of the config system behind it
""",

"MK": """
## What it does

Marketing / Activity Tracking — the CRM activity engine underlying EVO.
The MK module manages marketing campaigns, activity events, follow-up
tracks, and form templates for customer/prospect engagement.

MK is NOT a user-visible top-level menu group — its programs are invoked
from within CM (Contact Master) and other modules. However, MK tables appear
in virtually every EVO module because `MKAHIST` (activity history) serves as
a universal audit log across the entire system: 158+ programs write to MKAHIST
for event logging.

## Key tables (11 total)

| Table | Fields | Purpose |
|-------|--------|---------|
| `MKDEF` | 11 | Module config: ECNEXTID/ENEXTID/FNEXTID/TNEXTID auto-counters |
| `MKEVENT` | 12 | Event/activity type: class, description, form template, media |
| `MKECLASS` | 3 | Event classification codes |
| `MKICLASS` | 3 | Inbound activity classification codes |
| `MKTRACK` | 4 | Campaign/track definitions: NUM/CLASS/DESC/ACTIVE |
| `MKTCLASS` | 3 | Track classification codes |
| `MKTROUT` | 11 | Track routing: SEQ/EVENT/DAYSNXT/NEXTSEQ/JUMP/FIXED/PRICECD |
| `MKFORM` | 6 | Form templates: NUM/DESC/FILE/ATT/ACTIVE |
| `MKASSIGN` | 6 | Activity assignments: ACCT/NXTDAT/NXTSEQ/PRCODE |
| `MKTNOTE` | 3 | Track notes: TRACK/LINE/TEXT |
| `MKAHIST` | 9 | Activity history: ACCT/DATE/EVENT/FORM/TRACK/SEQ/MEDIA/REM1/REM2 |

## How it works

A **track** (MKTRACK) is a campaign sequence — a series of timed contact
events (MKTROUT) with defined intervals and next steps. Accounts (customers,
prospects) are **assigned** to tracks (MKASSIGN) and the track scheduler
advances them through events automatically.

Each completed event is logged to `MKAHIST` — which is why MKAHIST appears
in 158+ programs across all EVO modules as the universal activity audit trail.
The GL bank reconciliation (T7GLJ) also opens MKTRACK, confirming the marketing
engine is wired into non-CRM modules.

## Integration

- **[[module-CM|CM]]** — Contact Master uses MK for campaign management and
  follow-up scheduling; BKCM* tables link to MKTRACK via the activity framework
- **[[module-GL|GL]]** — T7GLJ (bank reconciliation) opens MKTRACK
- **[[module-LI|LI]]** — LI logs access-grant events to MKAHIST (audit trail)
""",

"YS": """
## What it does

Year-end / System — **not a separate top-level module.** Fiscal year-end
processing is handled by the [[module-AM|AM]] Accounting Management module.

`AM-B Fiscal Year End` closes the fiscal year: rolls forward retained earnings,
zeroes income statement accounts, creates the opening balance for the new year.

1099 generation (for vendor payments) is in [[module-AP|AP]].
W-2/payroll year-end (if using EVO payroll) is in [[module-PL|PL]].

See [[module-AM|AM]] for period-end and year-end procedures.
""",

}
