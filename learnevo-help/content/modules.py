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

"TC": """
## What it does

Treasury Control — AR receipt batch processing module. TC handles the
batch-level control of cash receipts: batching incoming payments by terms
or bank account, cross-balancing batch totals, posting commissions on
receipt, and AP check cross-reference. Functions as the "outer wrapper"
for AR-B (Enter Cash Receipts) batch workflow.

## Menu operations (DFM-confirmed)

| Code | Program | Description |
|------|---------|-------------|
| TC-C | T7TCC | **Batch Payment by Terms** — Enter Terms to Pay / Bank Account / Process (select a payment terms code to process all due invoices meeting that term) |

**T7DETC** (T7DE-T-C) is a separate stub dispatcher that routes to TC programs from the DE module, not a TC menu program.

## Key workflow

```
TC-A: Open receipt batch (batch# / date / limits)
TC-B: Enter receipts (calls AR-B per transaction)
TC-C: Pay-by-terms (T7TCC: select Terms / Bank Account → process)
TC-X: Cross-balance and post batch (XBAL cross-balance check)
```

**Batch controls (from var analysis):** MAX_BATCH, NUM_NEG/POS (negative/positive record counters), NEGRECNUM/POSRECNUM, XBAL cross-balance; SOP_INV = system-of-payment invoice link.

## Integration

- **[[module-AR|AR]]** — AR-B cash receipt entry is invoked within TC batches
- **[[module-AP|AP]]** — BKAP.CHK.*(14) AP check cross-reference in TC
- **[[module-CS|CS]]** — BKPR.COMM.*(48)/BKPR.SLS.*(17) commissions calculated on-receipt within TC
- **[[module-IS|IS]]** — ISIS.MCF.*(49-var) multi-currency conversion in TC for foreign currency receipts
""",

"AR": """
## What it does

Accounts Receivable manages everything related to **what customers owe
you** and **how they pay**: customer master records, invoices, statements,
aging, interest, sales taxes, deposits, and dunning.

## Key tables

| Table | Records | Fields | Purpose |
|-------|--------:|-------:|---------|
| `BKARCUST` | 4,405 | 106 | Customer master (ODBC confirmed) |
| `BKARINV` | 3,709 | 104 | Open invoice headers (ODBC confirmed) |
| `BKARINVL` | 78,025 | 29 | Invoice line items (ODBC confirmed) |
| `BKARHINV` | 95,998 | 104 | Archived invoice headers (ODBC confirmed) |
| `BKARCHKF` | 43,700 | 12 | Customer payments (checks/EFT, ODBC confirmed) |
| `BKARTXN` | 2 | 14 | AR transaction ledger (sparse — most history in GL) |
| `BKARCR` | N/A | — | Cash receipts staging — Btrieve-only |

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

## Key tables

| Table | Records | Fields | Notes |
|-------|--------:|-------:|-------|
| `BKAPVEND` | 3,166 | 72 | Vendor master — **ODBC confirmed** |
| `BKAPINVT` | N/A | — | AP invoice (voucher) header — Btrieve-only |
| `BKAPINVL` | N/A | — | AP invoice line items — Btrieve-only |
| `BKAPCHKF` | N/A | — | Checks current — Btrieve-only |
| `BKAPCHKH` | N/A | — | Check history — Btrieve-only |
| `BKAPPAY` | N/A | — | AP payments scheduled — Btrieve-only |
| `BKAP1099` | N/A | — | 1099 records — Btrieve-only |

**BKAPVEND key fields (72 total):** `BKAP_VENDCODE(10,PK)`, `BKAP_VENDNAME(30)`,
address (ADD1_1/ADD2_1/CITY_1/STATE/ZIP/COUNTRY_1 — dual-address capable),
4 contacts + 5 phone numbers, `BKAP_OUTINV(52)` outstanding balance,
purchase stats (MTD/YTD/LYR), `BKAP_GL_ACCT(10)` default GL account,
`BKAP_TERMS_NUM(5)` payment terms, `BKAP_TAX_ID(20)` for 1099,
10 notes lines (60 chars each), 2 email fields (128 chars each),
`BKAP_CUST_CODE(15)` cross-ref to AR customer,
`BKAP_IS_MCCODE(3)` multi-currency code.

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

**Scale:** 208,703 BOM lines (BKBMMSTR, ODBC confirmed) — linking parent
assemblies to components with avg ~7 components per parent.

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

## Menu operations (16 DFMs confirmed)

| Code | DFM | Operation | Key fields |
|------|-----|-----------|-----------|
| BM-A | T7BMA | Enter BOM | List: Add/Edit/Copy/Delete/Options; sub-form T7BMAx: Line No, Component, Qty Per, Scrap%, Sequence, Routing#, Reference, Scrap Type [Q/%], Include When BackFlushing For Scrap Assembly, Manufactured or Kit type [M/K] |
| BM-B | T7BMB | Print BOM | Parent Item Number From/Thru, Number of decimals in Qty required, Print up to this many levels |
| BM-C | T7BMC | Print Where Used | Component From/Thru, Print up to levels, Print for inactive Parent? |
| BM-D | T7BMD | Print Availability | Print For Location, Quantity to Project, Incl ROHS Compliant items [Y/N/O]; note: shortages indicated by * |
| BM-E | T7BME | Replace Component | Search for Component, Replace with Component, Copy old BOM Remarks to new Component |
| BM-F | T7BMF | Remove Component | Remove this Component (global delete from all BOMs) |
| BM-G | T7BMG | Print by Item Type/Class | Item Type [RFAMNLBTKO], Class From/Thru, Category From/Thru |
| BM-H | T7BMH | Print BOM Costs | Parent Item Number From/Thru, Number of decimals, For (P)arent or (C)omponent? |
| BM-I | T7BMI | Print BOM at Cost | Parent Item Number From/Thru, Number of decimals, Print Avg/Std/Last Cost [A/L/S] |
| BM-J | T7BMJ | Approved Substitutes | Std Item Number/Parent/Customer Code/Substitute Item ranges → columns: Std Item, Parent, Customer Code, Line Number, Substitute Part |
| BM-K | T7BMK | Vendor BOM | Standard Item/Parent/Customer/Vendor Code ranges → columns: Vendor Code, Vendor Part Number; Sort By Vendor; Auto Print Folder |
| BM-L | T7BML | Manufacturer BOM | Std Item/Parent/Customer/Manufacturer Item ranges → columns: Manufacturer Name, Manufacturer Part Number |
| BM-P | T7BMP | BOM Pick List | Assembly Item Number, Item Number From, Item Type [RFAMNLBTKO], Component Types |
| BM-Q | T7BMQ | BOM Roll Up | Component From/Thru (cost roll-up) |
| BM-R | T7BMR | Requirements Projection | Parent Item Number, Quantity(s) to Project, Item Class From/Category From/Thru |

## BOM line entry (T7BMAx sub-form)

Key fields on each BOM component line:
- **Scrap Type [Q/%]** — Q=fixed quantity scrap loss, %=percentage scrap factor applied to Qty Per
- **Manufactured or Kit type [M/K]** — M=sub-assembly to manufacture; K=kit (phantom, explodes through to raw components)
- **Include When BackFlushing For Scrap Assembly** — controls whether component is consumed when parent is reported as scrap
- **Routing#** — operation routing step that consumes this component
- **Sequence** — BOM line sort order within the parent

## Cross-reference reports (BM-J / BM-K / BM-L)

EvoERP tracks three types of alternate/cross-reference items in the BOM:
- **BM-J Approved Substitutes** (BKSBPART table): customer-specific approved substitute parts (Std Item + Customer Code → Substitute Part)
- **BM-K Vendor BOM** (BKBMVEND): which vendor supplies which component, with vendor part numbers; Sort By Vendor output for purchasing
- **BM-L Manufacturer BOM** (BKBMMFR): manufacturer name + manufacturer part number cross-reference

## Integration

- **[[module-WO|WO]]** — when a WO is released, its BOM is copied from
  BKBMMSTR into `WOBOM` (per-WO snapshot). Changes to master BOM do
  not affect in-progress WOs.
- **[[module-MR|MR]]** — MRP explodes BOMs to compute component demand;
  BOM structure determines how far MRP pushes planned orders down.
- **[[module-ES|ES]]** — Estimating pulls BOM for cost roll-up.
- **[[module-HH|HH]]** — HH-C Issue Materials and HH-D Finish Production
  read WOBOM (the WO snapshot of the BOM), not BKBMMSTR directly.
""",

"MR": """
## What it does

Material Requirements Planning (MRP) closes the loop between demand and
supply. It reads every open Sales Order, WO demand, and safety stock
requirement, nets them against open POs and WOs plus on-hand inventory,
explodes the BOMs, and generates a recommended action list.

**Scale:** 37,137 records in `MTMRP` (13f, ODBC confirmed). i2 Systems
runs in pure-demand mode (no forecasting, BKMRPFC=0/10f confirmed).

## Key tables

| Table | Records | Fields | Notes |
|-------|--------:|-------:|-------|
| `MTMRP` | 37,137 | 13 | Live MRP planning rows — ODBC confirmed |
| `BKMRPFC` | 0 | 10 | Forecast — ODBC confirmed, not used at i2 |
| `BKMRPSW` | 4,717 | 2 | Suggested WOs (BKMRP_SW_PART, BKMRP_SW_SW) |
| `BKMRPPO` | 0 | 16 | Suggested POs — ODBC confirmed, currently empty |
| `BKMRPCA` | N/A | — | MRP calendar adjustments — Btrieve-only |

MTMRP schema (13f): `MTMRP_PARTNO(15)`, `MTMRP_DATE(10)`, `MTMRP_QTY(52)`,
`MTMRP_ONHAND(52)`, `MTMRP_PEGTO(10)`, `MTMRP_ORDER(10)`, `MTMRP_STARTDT(10)`,
`MTMRP_ACTION(10)`, `MTMRP_PG_SDATE(10)`, `MTMRP_PG_FDATE(10)`,
`MTMRP_PG_QTY(52)`, `MTMRP_EXTRA(50)`, `MTMRP_LOC(10)`.

## MTMRP action codes (MTMRP_ACTION field)

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

## Menu operations (18 DFMs confirmed)

| DFM | Operation | Confirmed from |
|-----|-----------|----------------|
| T7MRA | MR-A Enter/review demand — Item#, Qty, Due Date, Consumed/Original/Projected Qty | DFM |
| T7MRADE | MR-A Import — CSV or fixed-length: Item Number, Date (YYYYMMDD), Qty | DFM |
| T7MRB | MR-B — Item/Type [RFAMNLBTKO]/Class range report | DFM |
| T7MRC | MR-C — Date/Item/Class/Category range report | DFM |
| T7MRD | MR-D — Item/Type [RFAM]/Category/Class range | DFM |
| T7MRE | MR-E — Item/Type [RFAMNLT]/Category/Class range | DFM |
| T7MRF | **MR-F Run MRP** — 4-stage progress (Stage 1–4 + BOM Analysis + Generating Material Requirements) | DFM |
| T7MRG | MR-G — Item/Date/Type [FAMRNLT]/Class range report | DFM |
| T7MRH | MR-H — Color-coded report: "Req Date − Lead Time is Prior to Today" and "+ X Days" thresholds | DFM |
| T7MRI | MR-I — Item/Class/Category range filter | DFM |
| T7MRIR | MR-I Review Qty dialog — Item#, Description, Start Date, Finish Date, Quantity | DFM |
| T7MRIX | MR-I Execute — WO Qty per part; multi-part grid (Part1–Part4, Tool) | DFM |
| T7MRJ | **MR-J Planned PO Suggestions** — Qty/Item range/Due Date range/Category/Vendor/Start Date | DFM |
| T7MRJR | MR-J Review — Item#, Description, MRP Start Date, MRP Finish Date, RFQ Date, Exp Recv Date, Quantity | DFM |
| T7MRJX | MR-J Execute — Vendor, Est. Rcp Date, Qty, Price, Confirmed Y/N, Show Blank Vendors | DFM |
| T7MRL | MR-L Print Plan — PL Number (1 thru LAST.PLND), Reverse Lookup flag | DFM |
| T7MRN | MR-N — Vendor range, PO $ Value threshold, Report Only flag | DFM |
| T7MRO | MR-O — Item/Type [FRAM]/Class/Category/Planner range | DFM |

**MR-F is the core MRP computation:** T7MRF.DFM shows a 4-stage progress
sequence followed by "BOM Analysis" and "Generating Material Requirements" —
this is the UI wrapper for the BKMRF.SRC engine described below.

**MR-J is the PO suggestion workflow:** T7MRJR shows the suggested PO review
screen (MRP dates, RFQ date, exp. receipt date, qty); T7MRJX is the
confirmation/edit screen with vendor, price, Confirmed Y/N flag. When confirmed,
MR-J converts BKMRPPO rows into real BKAPPO/BKAPPOL records.

## Typical workflow

```
MR-F  Run MRP (4-stage BKMRF engine, T7MRF.DFM progress display)
MR-B  Review suggested POs    → BKMRPPO
MR-C  Review suggested WOs    → BKMRPSW
MR-J  Confirm planned PO      → T7MRJR review → T7MRJX execute → BKAPPO/BKAPPOL
MR-K  Confirm planned WO      → creates WORKORD
MR-L  Print plan (PL Number)
MR-L/clear  Purge MTMRP output
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

## Menu operations (DFM-confirmed, 22 DFMs)

| Code | Program | Description |
|------|---------|-------------|
| DC-A | T7DCA / T7DCA2 | **Real-time labor entry** (touchscreen/barcode terminal) — Employee / Action / Work Order / WO Item / Sequence / Machine / Work Center / Total Parts Made / Hrs; Notes required if cycle time exceeded. T7DCA2 adds Start Shift / Stop Shift buttons |
| DC-A-Label | T7DCALabel | **Print Transfer Label** — Item#/Desc/Bin Location/Sequence (printed when transferring WIP between operations) |
| DC-A-Notes | T7DCANotes | **WO Notes panel** — links: WO Item / WO Routing / WO / Routing (note viewer for DC-A context) |
| DC-B | t7dcb | **Production quantity entry** — Parts Made / Parts Scrapped / Total Parts Made / Scrap Code + Desc / Prev Seq Made; sub-form T7DCBSERIAL for serial number assignment (Serial# / Total Qty / Remaining Qty) |
| DC-D | T7DCD | **Supervisor inquiry / timecard review** — Employee# / Password; WO From/Thru filter (supervisor-level access to DC records) |
| DC-E | T7DCE | **Print Labor Tickets** (per operation) — WO# range / Number to Print per Operation / Include Outside Processing / Include Alternate Operations |
| DC-E-F | T7DCF | **Print Employee Tickets** (per employee) — Employee From/Thru / Number to Print per Employee |
| DC-G | T7DCG | **Edit Labor Transactions** (grid editor) — Date range / Include Shift Records [Y/N/Only]; columns: Date/WO/Employee/Sequence/Run+Setup Hrs/Time Start+Finish/Parts/Scrapped |
| DC-H | T7DCH | **Batch post labor** — Employee range / Shifts [1/2/3] / WO# range; Post button (commits staged BKDCLAB to WO labor/material) |
| DC-K | T7DCK | **Shift record archive/purge/restore** — Employee range / Shifts [123] / Date range / [A/R/P] |
| DC-L | T7DCL | **Employee timecard display** — Employee# / Password; shows Current Status / Hours Today / Hours Pay Period / Reg/OT/Hol/DT/Vac/Sick breakdown; Start Shift button |
| DC-M | T7DCM | **Labor summary board** — Sort by Employee Name / Include Run Hours / Include Salary Employees / Include Labor Type / Show Current Date Only (real-time shop floor view) |
| DC-N | T7DCN | **Holiday/vacation posting** — Employee From/Thru / Date range / **Holiday Hours** (payroll-linked time-off entry) |
| DC-PSF | T7DCPSF | **Paperless Shop Floor** (also accessible as HH-L) — WO#/Sequence/Item/Desc/Job/Drawing/Rev; sub-forms: Issue Components (All Comps/Issue Comps/Shortages), ECO viewer (Drawing/Rev/ECO#/ECO Date), Notes (QC Specifications/WO Item/Routing), SO Lookup |

**Shift codes [1/2/3]:** DC tracks three shifts per day. BKDCSHFT holds 3 shift names + 3 buffer codes (e.g. Day/Evening/Night).

**DC-PSF / HH-L dual access:** The Paperless Shop Floor form (`T7DCPSF.DFM` caption "HH-L Paperless Shop Floor") is accessible both from the DC menu and from the HH (HandHeld) module. The ECO sub-form (`T7DCPSFECO.DFM`) provides a read-only Engineering Change Order view during production.

**t7DCina.DFM** (caption "T7INA") — a cross-module navigation panel showing buttons for SO/SH/PO/RC/WO/AL/LO/BM/TR/VN/MF/RO/SR, embedded within the DC environment to allow rapid jumps to related modules.

## Integration

- **[[module-WO|WO]]** — BKDCLAB posts to WOLABOR and WOMAT when processed (DC-H)
- **[[module-PR|PR]]** — LAB_RUNHRS + LAB_SETUPHRS feed BKPRCURP for payroll (DC-N holiday hours also post to PR)
- **[[module-HH|HH]]** — HH-L Paperless Shop Floor = T7DCPSF (same program, dual-access)
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

## Menu operations (DFM-confirmed, 15 DFMs)

| Code | Program | Description |
|------|---------|-------------|
| QC-A | T7QCA | Scrap/QC report — date range / item / item class / vendor / QC-Scrap code; toggle Use QC Codes vs Use Scrap Codes |
| QC-B | T7QCB | Component scrap report — parent item / parent class / scrap code / WO# / component item; A/Archived filter |
| QC-C | T7QCC | CoC (Certificate of Compliance) report — same filter set as QC-B; A/Archived filter |
| QC-D | T7QCD | Detail scrap report — by employee, sequence number, QC/Scrap code; A/Archived filter |
| QC-F | T7QCFA/FB/FD/FF | NCR sub-menu (see below) |
| QC-G | T7QCGA/GB/GD | CAR sub-menu (see below) |
| QC-M | T7QCMTHD | Enter Testing Method — Description/Revision/Test Code/Date/Notes/Links |
| QC-R | T7QCRESULTS / T7QCRSLT | Enter/report Testing Results — Sequence No / Test Quantity / Clear button |
| QC-S | T7QCSPEC | Enter Testing Requirements — Test No / Test Code / Seq# / Individual or Batch [I/B] / Min / Max / Units / Pass-Only flag |

## NCR workflow (QC-F sub-menu)

| Sub | Program | Description |
|-----|---------|-------------|
| QC-F-A | T7QCFA | **Enter NCR** — NCR# / Created / Item / Component / Qty / Defect / Description of Nonconformity / Who |
| QC-F-B | T7QCFB | **Print NCR** — NCR# range; Print Linked Documents / Print Notes / Print Serial Numbers; Open or Closed NCR filter |
| QC-F-D | T7QCFD | **Close NCR** — NCR# range / NCR Date range / Force Close NCR |
| QC-F-F | T7QCFF | **NCR List** — Item / Component / NCR# / Location / Origin (I/V/R) / Sort by Part or Date (P/D) / Status (O/D/C) |

Origin (I/V/R) = Internal / Vendor / Rework (inferred from manufacturing QC context).

## CAR workflow (QC-G sub-menu)

| Sub | Program | Description |
|-----|---------|-------------|
| QC-G-A | T7QCGA | **Enter CAR** — CAR# / Created / Item / Component / Qty / Defect / Description of Nonconformity / Initiator |
| QC-G-B | T7QCGB | **Print CAR** — CAR# range / Print Linked Documents / Print Notes / Print Open Only |
| QC-G-D | T7QCGD | **CAR List** — Item / Component / CAR# / Location / Origin (I/V/R) / Open-Review-Closed status / Filter Owner |

CAR (Corrective Action Report) has a 3-state status (Open / Review / Closed) vs. NCR's 2-state (Open / Closed).
The "Filter Owner" field in QC-G-D allows filtering CARs by assigned owner — not present in the NCR list.

## Workflow

```
PO receipt arrives  ->  QC-A: Scrap/QC report (BKQCMSTR)
                    ->  QC-B/C/D: Component scrap / CoC / detail reports
                    ->  QC-F-A: Enter NCR if rejection (ISNCR created)
                    ->  QC-F-D: Force-close NCR when resolved
                    ->  QC-G-A: Escalate to CAR if corrective action required (ISCAR)
For in-process testing:
  QC-M: Define test method  ->  QC-S: Set specifications  ->  QC-R: Record results
```

## Integration

- **[[module-PO|PO]]** — QC inspection triggers on PO receipt (QC-J intercept on PO-E)
- **[[module-IN|IN]]** — items under QC hold are unavailable for issue until released
- **[[module-WO|WO]]** — in-process QC can trigger per routing operation (OPQCDESC table)
- NCR/CAR tables (ISNCR, ISCAR) are IS* custom tables; 74 NCRs live at i2, 0 CARs
""",

"JC": """
## What it does

Job Costing cross-references manufacturing costs (from Work Orders) against
Job Codes — allowing management reporting by project, contract, or
cost-center that spans multiple WOs.

**Scale:** 45,863 job codes in `ISJOB` (all blank STATUS — passive reference
data, not actively managed via menu). 142 business scorecard records in
`ISJBSF`.

## Core concept

A Job Code (`ISJOB`) is a free-form grouping label attached to WOs. When
a WO is assigned a job code, its costs roll up to that job. JC-A generates
the summary by job showing planned vs. actual labor, material, and overhead.

## Tables

| Table | Records | Purpose |
|-------|--------:|---------|
| `ISJOB` | 45,863 | Job master (9 fields: IS_JOB_CODE/IS_JOB_DESC/IS_JOB_STATUS + extras) |
| `ISJBSF` | 142 | Business scorecard — key metrics per job/period (144 fields) |

ISJOB has only 3 meaningful fields: `IS_JOB_CODE`, `IS_JOB_DESC`, and
`IS_JOB_STATUS`. All 45,863 rows have blank STATUS — the codes are a
historical reference list rather than actively managed records.

## Menu operations (DFM-confirmed)

| Code | Program | Description |
|------|---------|-------------|
| JC-A | T7JCA.RWN | Job Cost Report — WO# / item / customer / job ranges; status [CXFRSI] |
| JC-B | T7JCB.RWN | Job Cost by Job — summary or detail; composite report option |
| JC-E | T7JCE.RWN | WO Cost with date range filter + act finish date |
| JC-F | T7JCF.RWN | Job Cost by WO with date range |
| JC-H | T7JCH.RWN | Operation efficiency — work center / sequence / scheduled finish date |
| JC-L | T7JCL.RWN | Labor report — act start/finish date ranges |
| JC-M | T7JCM.RWN | Material report — transaction date / customer / act finish date |
| JC-N | T7JCN.RWN | Month-end cost report — ISCALC.HOW_C/H/P costing method; ISCOST.BREAKOUT |
| JC-P | T7JCP.RWN | Print Materials in WIP — component / zero-issue / rebuild WO options |
| JC-Q | T7JCQ.RWN | WO Variance — fin product / WIP var / scrap code ranges |
| JC-R | T7JCR.RWN | WO cost as-of-date — same as Q with prior-date snapshot option |
| JC-S | T7JCS.RWN | WO cost summary by act start/finish + customer/job ranges |
| JC-RM | T7JCRM.RWN | Java BI Report Manager — same JDBC architecture as SQLEXPORT |

WO Status codes used in JC reports: C=Complete, X=Closed, F=Finished,
R=Released, S=Started, I=In-Process (combined set from T7JCA/JCN/JCP DFMs).

**T7JCENG.RWN** is the shared calculation engine invoked by most JC reports
(displayed as "JC Engine / Processing Data / Please Wait" while computing).
Its DFM shows: Report Type, Sort/Subtotal By, Level of Detail, WO Status
(5-state filter), WO Source, Labor Type — all parameterized per calling report.

**T7JCRM** — like SQLEXPORT, this is a Java JDBC-backed BI export tool:
Host/Port/Name/Destination settings (T7JCRM.DFM confirmed), connects to
Pervasive PSQL for custom JC queries and exports.

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

## DFM-confirmed operation details (9 DFMs)

| DFM | Caption / Confirmed |
|-----|---------------------|
| T7CSA | **CS-A Enter Salespersons** — Salesperson Number, Type/Class, Vendor Code, Rate, First Name/MI, Last Name |
| T7CSB | **CS-B View Salesperson Info** — Quota, COGS, Comm Due, Comm Paid, Receipts (read-only dashboard) |
| T7CSC | **CS-C Print Salesperson Info** — Which Month? (0 = YTD), Salesperson# range, Include Monthly Detail toggle |
| T7CSD | **CS-D Transfer Sales Commissions** — Tag All/Untag All/Tag/Untag/Transfer Tagged (batch transfer UI) |
| T7CSE | **CS-E Print Commission Detail** — Item# range, Salesperson# range, Invoice Date range |
| T7CSF | **CS-F Print Commission Summary** — Salesperson# range, Invoice Date range |
| T7CSI | EvoCSI Master Inquiry — Customer/Item/SO/Invoice/Vendor (shared cross-module lookup, not CS-specific) |
| T7CSO | **CS-O Print Commissions Earned Detail** — Color options: Class 1, Color 1/2, Background colors |
| T7CSP | **CS-P Print Commissions Due Summary** — Salesperson# range, Invoice Date range (separate from CS-F) |

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

**Scale:** 6,897 active quotes with 462,837 line items (~67 lines/quote, ODBC confirmed).
An additional 5,816 archived quotes in ISESTAQT + 130,792 lines in ISESTAQL
(IS-era tables, same BKAR_INV_* field layout as BKESTQT/BKESTQTL).
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

| Table | Records | Fields | Purpose |
|-------|--------:|-------:|---------|
| `BKESTQT` | 6,897 | 104 | Quote header — BKAR_INV_* field layout (ODBC confirmed) |
| `BKESTQTL` | 462,837 | 29 | Quote lines — BKAR_INVL_* field layout (ODBC confirmed) |
| `BKESTCFG` | 1 | 18 | Quote configuration singleton (ODBC confirmed) |
| `ISESTAQT` | 5,816 | 104 | IS-era archived quote headers — same BKAR_INV_* layout |
| `ISESTAQL` | 130,792 | 29 | IS-era archived quote lines — same BKAR_INVL_* layout |
| `ISESTDTL` | 0 | 220 | Detailed cost breakdown per component (legacy path) |
| `ESTSUM` | 0 | 228 | Legacy DBA estimate summary — unused in T7 era |
| `ISESTLBR` | N/A | — | Labor cost detail — Btrieve-only |
| `ISESTMTL` | N/A | — | Material cost detail — Btrieve-only |

BKESTQT and ISESTAQT share the same 104-field BKAR_INV_* schema (mirroring
the AR invoice header). Key fields: BKAR_INV_NUM (quote number), BKAR_INV_INVCD
(status: Y=open/X=cancelled), BKAR_INV_CUSCOD (customer), BKAR_INV_INVDTE
(date), BKAR_INV_TOTAL (quote total), BKAR_INV_JOBNUM (linked job).

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

## DFM-confirmed details

**T7SRINFO (S&R Misc. Information):** UDF panel attached to SR orders —
5 date fields (Date1–5) and 17 alpha fields (Alpha1–17) for user-defined
data. Stored in a companion record keyed by SRNUM.

**T7SRBK (Live Work Center Schedule):** Real-time WC queue view filtered
by Location, with Firmed/Released/Complete status checkboxes and a
configurable refresh timer. Confirms SR-C work orders appear in the shop
scheduling queue like regular WOs.

**T7SRF caption is "SO-F":** Confirmed that SR-F Print Invoices reuses the
SO invoice print form directly — SR invoice printing is handled by the
same program as SO-F. This makes sense given the shared BKAR_INV_* schema.

**T7SRI (SR-I Void Invoice) DFM-confirmed fields:** BKAR_INV_INVDTE,
BKAR_INV_ORDDTE, BKAR_INV_SHIPDT, BKAR_INV_SONUM, BKAR_INV_SUBTOT,
BKAR_INV_TAXAMT, BKAR_INV_FRGHT — the void screen is a full AR invoice
display, confirming SR invoices share the BKARINV schema byte-for-byte.

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

**Scale:** Live ODBC: 31,248 frozen inventory records (`BKPIFROZ`) and 51 lot
records (`BKPILOT`) — confirms PI was run and data remains. Session headers
(`BKPIMSTR`) and count tags (`BKPIPHYS`) are Btrieve-only. PI is actively
used at i2 Systems.

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
| `BKPIFROZ` | 31,248 | Frozen snapshot of on-hand at count start (19f, ODBC confirmed) |
| `BKPILOT` | 51 | Lot frozen/counted records (10f, ODBC confirmed) |
| `BKPISER` | 0 | Serial frozen/counted — not used at i2 (10f) |
| `BKPIMSTR` | Btrieve-only | PI session header (YEAR + QTR + DESC) |
| `BKPIPHYS` | Btrieve-only | Count tag entry (actual count per item) |
| `PIBINLOC` | Btrieve-only | Bin-location count records |
| `BKPISER` / `BKPISCNT` | — | Serial frozen/counted (10f each) |

## Cycle count support

PIBINLOC has `YEAR`/`QTR` cycle fields and last-count dates — supporting
partial (cycle) counts in addition to full physical inventory.

## DFM-confirmed operation details (10 DFMs)

| DFM | Caption / confirmed |
|-----|---------------------|
| T7PIA | **PI-A Capture Frozen Inventory** — Year, Physical Inventory Number, Freeze Date, Process button |
| T7PIB | **PI-B Frozen Inventory Report** — Year, PI#, Sort by Part or Bin, **Export FileName** (can export to flat file) |
| T7PIC | **PI-C Enter Tag Counts** — Part Number, Tag Number, Location, Count Qty (barcode-entry workflow) |
| T7PICA | **PI-C-A Exception Report** — Year, PI#, Sort by, Print button |
| T7PID | **PI-D Missing Tags Report** — Year, PI#, Starting Tag Number |
| T7PIE | **PI-E Enter Tag Counts (alternate)** — shows Frozen Cost; Part Number, Location, Frozen Cost, Edit (review mode vs. blind-count mode in PI-C) |
| T7PIF | **PI-F Physical Inventory Report** — Year, PI#, Sort by Item Number or Class (I/C), Include Tag Details (Y/N/L) |
| T7PIG | **PI-G Update Actual Inventory** — Year, PI#, note: "FIFO/LIFO always uses Current cost"; Post button |
| T7PIH | **PI-H Purge Physical Inventory** — Year, PI# (cleanup after posting) |
| T7HHPIC | **HH PI-C Entry** (handheld variant) — Phys Inv No, Count Date, Year, Name (operator name) |

**Note on PI-C vs PI-E:** T7PIC is the blind-count entry (operator enters qty without seeing frozen), T7PIE shows the frozen cost (supervisor review mode).

## Integration

- **[[module-IN|IN]]** — PI variances post as `INVTXN` type A adjustments,
  updating BKICLOC on-hand
- **[[module-GL|GL]]** — PI adjustments generate GL journal entries via the
  inventory variance accounts in BKSYMSTR
- **[[module-HH|HH]]** — T7HHPIC provides handheld scanner PI count entry
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

| Table | Records | Fields | Notes |
|-------|--------:|-------:|-------|
| `WORKORD` | 28,078 | 83 | WO headers — ODBC confirmed |
| `WOBOM` | 505,943 | 39 | WO BOM lines — ODBC confirmed |
| `WOROUT` | 8,239 | 83 | WO routing operations (per-op schedule) — ODBC confirmed |
| `SCHWO` | 0 | 10 | Finite schedule WO queue — ODBC confirmed (empty = not used at i2) |
| `SCHEDCAL` | 0 | 6 | Shop calendar — ODBC confirmed (empty = default M–F used) |
| `WORKCTR` | — | 47 | Work center master (`MTWC.*` namespace) — Btrieve-only |
| `ISWOPRIO` | — | 4 | WO priority codes with Gantt color — Btrieve-only |

**SH-A DFM-confirmed fields** written to WORKORD: `MTWO_WIP_SSTART` (scheduled
start), `MTWO_WIP_SFIN` (scheduled finish), `MTWO_WIP_PRTY` (priority code),
`MTWO_WIP_DDATE` (due date). The `AUTO_TEXT` combo enables auto-entry mode.

**SH-C DFM-confirmed fields** written to WOROUT (routing operations): `MTWORO_START`
(op start date), `MTWORO_FINISH` (op finish date); also captures total hours/day,
% utilization, shift hours, and outside-processing flag per work center.

## DFM-confirmed operation details

| DFM | Confirmed purpose |
|-----|-------------------|
| T7SHE | Reschedule / reprocess: sets new due date for priority change; "Labor Data Posted up Thru" field and "Incl Last/Curr WO Seq?" flag confirm this is the labor-driven reschedule, not a full finite schedule run |
| T7SHF | Print filtered schedule: Status Codes [FR], WO range, Start/Finish date range, Job Number range |
| T7SHG/J | Print WO Schedule report: WO Status/Class/Included Classes/Priority checkboxes; Sort by; Customer/Start/Finish/Planner ranges |
| T7SHI | Color-coded WC Schedule: per-WC page layout, elapsed-start-date color, same WO Status/Class/Priority filters as SH-G |
| T7SHM | Lead Time Estimator: item number (PART_NO), start date (SDATE), 4 priority date fields (PR0_DATE–PR3_DATE) |
| T7SHN | Generate Lead Times range: Part Types [RFAMNLBTKO], Item/Class/Category/Planner From–Thru |
| T7SHO | Work Center range report: WC From–Thru, page break between work centers option |
| T7SHP | Color priority report: 3-zone thresholds (X days, X–Y days, >Y days) for priority change, elapsed start, WO finish vs. est. ship date |

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
| `BKEDIH` | 0 | Inbound order staging header (**104f** ODBC confirmed, BKARINV clone) |
| `BKEDIL` | 0 | Inbound order staging lines (**29f** ODBC confirmed, BKARINVL clone) |
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
| Job codes | SM-P | Enter job codes for job-cost cross-reference (T7SMJL.RWN) |

## Key tables — ODBC-accessible

| Table | Records | Fields | Purpose |
|-------|--------:|-------:|---------|
| `BKYSMSTR` | 1 | 355 | Manufacturing system parameters (WO numbering, YN flags, ISTS.CFG.*) |
| `BKSYMSTR` | 1 | 286 | Global system parameters (company name, terms, GL defaults) |
| `BKICLOC` | 136,501 | 32 | Item/location stock positions (inventory by item × location) |
| `ISJOB` | 45,863 | 9 | Job code master (IS_JOB_CODE/DESC/STATUS) |
| `ISJBSF` | 142 | 144 | Business scorecard metrics per job/period |
| `BKICPMAT` | 32 | 137 | Customer price matrix (tier-based pricing rules) |
| `BKICREF` | 1,674 | 19 | Item cross-references (customer part#, vendor part#) |
| `WORKCTR` | 27 | 48 | Work center master (name, dept, WC code, capacity) |
| `BKICLOCM` | 16 | 15 | Location/warehouse master (CODE/NAME/ADDR/TAX) |
| `ISBANKS` | 12 | 36 | Bank account definitions (GL acct, routing) |
| `ISSHIPCO` | 11 | 16 | Shipping company codes (carrier definitions) |
| `ISNCR` | 74 | 63 | Non-conformance reports |
| `ISCATMST` | 35 | 3 | Category master codes |
| `ISTERMS` | 18 | 13 | Payment terms (NUM/NAME/DESC/AMT/TYP/DAY/EOM/MAX/COD/ARAP/CC/SRT/EXTRA) |
| `ISNTYPE` | 16 | 4 | Note type codes |
| `ISTAXGRP` | 2 | 105 | Tax group definitions |
| `ISTAXFIL` | 2 | 84 | Tax filing configuration |
| `ISTRIGRS` | 7 | 27 | Trigger condition rules |
| `ISNUMBER` | 9 | 52 | Auto-number configuration by document type |
| `CLASS` | 40 | 24 | Item class master |
| `CLASMSTR` | 185 | 2 | Class/subclass name table |
| `BKDCSHFT` | 1 | 34 | Data collection shift singleton |

**Btrieve-only (not in Pervasive DDF):** `BKEMP` (employee master), `BKTERM`
(payment terms legacy), `BKTAX` (tax code legacy), `BKSMSHIP` (ship-via legacy),
`CALT` (calendar), `CALSHIFT`, `BKSCHEDULE`, `BKUOM`, `BKUOMCON`

## System parameter singletons

Both `BKYSMSTR` (355f) and `BKSYMSTR` (286f) are single-row singletons storing
hundreds of system flags, GL account defaults, company info, and module-enable
switches. They are read at session start and cached. The full 355-field
`BKYSMSTR` schema includes 250 YN* flag slots (YN[1]..YN[250]) plus 40 GL account
pairs, 4 auto-numbers (WONUM/QCNUM/REQNUM/INVNUM), and the ISTS.CFG.* namespace.

## Integration

- **[[module-SY|SY]]** — SY handles user password and access security; SM handles master data
- **[[module-AM|AM]]** — AM handles GL/accounting period-end; SM-J handles operational archive/purge
- **[[module-GL|GL]]** — SM-C/D enter GL accounts and departments (cross-listed as AM-C/D)
- **[[module-WO|WO]]** — WORKCTR and BKICLOCM are read constantly by WO for routing/location lookup
- **[[module-IN|IN]]** — BKICLOC (136,501 rows) is the heart of inventory: per-item per-location stock
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

## Key AM operations (DFM-confirmed, 15 DFMs)

| Code | Program | DFM-confirmed detail |
|------|---------|----------------------|
| AM-A | T7AMA | **Period setup** — Current Fiscal Year Start Date / Today / Open Period Start Date / Open Period End Date / **Accounting Open Period Start Date** (two separate open-period boundaries) |
| AM-B | T7AMB | **GL balance editor** — Working on GL Account; columns: Current / Beginning / Total Year / 1 Year / 2 Year / … 6 Year |
| AM-C | T7AMC | **COA maintenance** — Account Code / Dept / Description / Account Type / (E Type Only) / (GL-O Posting Only) / Budget Amounts / Period / Beginning Balance / Ending Balance / New Account / Non-Cash flag / Inactive flag |
| AM-D | T7AMD | **Dept create/delete** — use existing dept as TEMPLATE → code of NEW dept; filter by account types (Asset/Liability/Expense/Income/Owner); Clear Budget Values; Department to be Deleted |
| AM-E | T7AME | **Financial statements** — Income Statement / Balance Sheet / Cash Flow / Statement of Changes in Financial Position; GL From/Thru; Report Title / section titles |
| AM-G | T7AMG | **Multi-company consolidation setup** — Consolidation Name / Last Consolidation Date / **Base Currency** |
| AM-H | T7AMH | **GL account code change** (CSV import) — Import Filename; Old GL Code/Dept → New GL Code/Dept; Start Time / Current Time progress display |
| AM-I | T7AMI | **Journal inquiry** — Date Range From/Thru / GL Account From / Journal Type filter; Go button |
| AM-J | T7AMJ | **AP history purge/archive/restore** — Vendor From/Thru / Process Thru Date / [P/A/R] |
| AM-K | T7AMK | **AR history purge/archive/restore** — Customer From/Thru / Process Thru Date / [P/A/R] |
| AM-N | T7AMN | **Fiscal period dates** — Period 1–12 end dates + "4 Years Ago" row (multi-year period boundary editor) |
| AM-O | T7AMO | **AP/PO data purge** — Vendor From/Thru / Last Activity Date / Vendor Class / **Delete PO Orphans [L/H/B/N]** (Lines/Header/Both/None) |
| AM-P | T7AMP | **AR/SO data purge** — Customer From/Thru / Last Activity Date / **Delete SO Orphans [L/H/B/N]** / **Include Ship To Customers [Y/N]** / Customer Class |
| AM-Q | T7AMQ | **Budget entry/copy** — GL Account From/Thru / GL Dept / Use One Year Past Amounts / Factor / Use Annual Budget / Use Current for Next Year / Use Annual for Next Year Budget |
| AM-S | T7AMS | **GL journal purge/archive/restore** — Journal Date range / Journal Number range / Journal Type / [Archive/Purge/Restore] |

**Delete Orphan codes [L/H/B/N]:** L=Lines only, H=Header only, B=Both, N=None — controls whether the purge removes only line items, only the header record, or both when the parent document has no remaining lines.

- **AM-A Reset Period-End Close Date** — updates ISGLDATE to advance the fiscal period gate (two boundaries: "Open Period" for transactions, "Accounting Open Period" for close process)
- **AM-B Fiscal Year End** — rolls BKGLCOA CURRENT→1YPAST→2YPAST balance fields; zeroes income statement; creates opening entry; populates ISGLHDAT with completed year's period dates
- **AM-Q Enter Budget Amounts** — writes budget figures to ISGLBDGT per account/period; copy-from-prior-year with multiplier factor supported
- **AM-T Archive GL Detail** — moves BKGLTRAN rows older than N years to offline archive (no DFM — may use inline filter only)

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

## Database tables (live counts, 2026-07-01)

| Table | Records | Fields | Purpose |
|-------|--------:|--------|---------|
| `LOT` | 11 | 25 | Active lot master (`MTLOT_*` prefix, `CODE+LOT` PK) |
| `BKLCMSTR` | Btrieve-only | — | Lot master (legacy; not in PSQL DDF) |
| `BKLCLOC` | Btrieve-only | — | Per-bin lot quantities (not in PSQL DDF) |

**At i2 Systems, lot control is minimally used — only 11 active lot records.** The LOT
table (DDF name `LOT`, TAS access prefix `MTLOT.*`) is the only ODBC-accessible lot table.

**MTLOT.* 22-var namespace** (confirmed from T7LCA/LCG): CODE/LOT/EXPDATE/ONHAND/
LOC/VENDOR/RECDATE/RECQTY/POCOST/WO/WOCOST/NOTES_1..5/WOSUF/BEGIN/OUT/MAXOUT.

Full 25-field LOT schema (from DDF): MTLOT_CODE, MTLOT_LOT, MTLOT_EXPDATE, MTLOT_ONHAND,
MTLOT_PO, MTLOT_RECDOC, MTLOT_VENDOR, MTLOT_RECDATE, MTLOT_RECQTY, MTLOT_POCOST,
MTLOT_WO, MTLOT_INRECDATE, MTLOT_WOQTY, MTLOT_WOCOST, MTLOT_NOTES_1..5, MTLOT_LOC,
MTLOT_WOSUF, MTLOT_EXTRA, MTLOT_BEGIN, MTLOT_OUT, MTLOT_MAXOUT.

Fields of note:
- `MTLOT_EXPDATE` — expiry date (food/pharma compliance)
- `MTLOT_POCOST` — landed cost at PO receipt
- `MTLOT_WOCOST` — cost when assembled into a WO
- `MTLOT_NOTES_1..5` — 5 free-text note lines per lot
- `MTLOT_BEGIN/OUT/MAXOUT` — initial qty, total out, max quantity ever issued

## Integration

- **[[module-PO|PO]]** — lot assigned at PO receipt (POCOST/RECDATE/VENDOR)
- **[[module-WO|WO]]** — lot linked to WO material issue and assembly
- **[[module-SO|SO]]** — lot linked to SO shipment line for customer traceability
- **[[module-PI|PI]]** — PIBINLOT (14f) tracks lot quantities during physical count
- **[[module-SC|SC]]** — parallel serial module; an item can be both lot and serial controlled

## DFM-confirmed operation details (7 DFMs)

| DFM | Caption | Key fields |
|-----|---------|-----------|
| T7LCA | LC-A Edit Lot Numbers | Lot Number, On-Hand, Date Rcvd |
| T7LCB | LC-B Assign Lot Control | Item Number, Product Type, Lot Control? toggle |
| T7LCC | LC-C | From/Thru filter, print |
| T7LCC2 | LC-C Print Lot Availability | Serial Number From/Thru (note: serial-aware variant of LC-C) |
| T7LCE | lot on-hand report | Item Number/Class/Category, Item Type [RFAMNLBTKO], Summary or Detail, Sub Sort by Lot/Exp Date, Exceptions Only, Negative Lot UOH |
| T7LCF | lot traceability | Item Number, Lot Number, Summary/Details/All |
| T7LCG | archive/unarchive | Archive/Unarchive [A/U], Item/Exp/Rcvd/Lot Date ranges, Include Zero UOH Only |
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

| Table | Records | Fields | Purpose |
|-------|--------:|-------:|---------|
| `SERIAL` | Btrieve-only | 30 | Active serial master (`MTSER_*`) — PO cost, SO ship, WO codes |
| `SERIALH` | Btrieve-only | 30 | Archived serial numbers (identical structure) |
| `INVTXN` | 3,269,208 | 40 | **Inventory transaction log** — every receipt, issue, transfer, and return |
| `WORECV` | 53,502 | 11 | WO completions/receipts linked to serial assignments |
| `ISBINLOC` | 31,844 | 9 | Bin-location stock positions (serial-aware) |
| `ISCATMST` | 35 | 3 | Category master codes |
| `ISSERCNT` | 0 | 9 | Serial counter — not used at i2 |
| `ISSCOMP` | 0 | 5 | Serial compound tracking — not used at i2 |
| `ISSTYPE` | 0 | 3 | Serial type codes — not used at i2 |

**MTSER.* 27-var namespace** in T7SCA: CODE/SERIAL/LOT/PO/RECDOC/VENDOR/RECDATE/POCOST/SO/CUSTCODE/SHIPDATE/SELLPRICE/WO/ISSDATE/ISSCOST/INRECDATE/INRECCOST/EXPDATE/WOCODE/NOTES/ONHAND/LOC/WOSUF/EXTRA/BIN/INV — full PO→WO→SO lifecycle per serial.

**At i2 Systems**, serial tracking is minimal — ISSERCNT=0 and ISSTYPE=0
confirm serial number generation is not configured. The INVTXN table
(3.27M rows) is the primary active table accessed by SC programs.

## Audit and fix (SC-F)

T7SCF performs 9 audit checks (orphans, duplicates, control changes, invalid
locations, unbalanced on-hand, unbalanced transactions, expired materials,
item type mismatches, negative on-hand) with 4 auto-fix modes.

## Serial number generation (SC-G — T7SCG.DFM confirmed)

T7SCG configures auto-generation of serial numbers per item:
- **Item Number** — per-item configuration
- **Item Class** — class-level default
- **Total Length of Serial Number** — fixed-width format
- **Starting Position of Numeric Portion** — prefix chars before number
- **Length of Numeric Portion** — auto-increment digit count
- **Last Number / Last Serial Number** — current auto-increment state
- **Format type [NISJ]:** N=Normal, I=UCC Item barcode, S=UCC Skid barcode,
  J=John Deere # — EVO supports John Deere-specific serial numbering format

The John Deere [J] format confirms i2 Systems ships to or works with John
Deere as a customer, requiring their barcode/serial specification.

## DFM-confirmed operation details

| DFM | Caption | Key fields |
|-----|---------|-----------|
| T7SCA | SC-A Edit Serial Numbers | Serial Number, On-Hand, Date Rcvd |
| T7SCB | SC-B Assign Serial Control | Item Number, Product Type, Serial Control? toggle |
| T7SCC | SC-C | From/Thru filter, print |
| T7SCC2 | SC-C Print Serial Availability | Serial Number From/Thru |
| T7SCE | archive/unarchive | Archive/Unarchive [A/U], Item/Serial/Exp/Rcvd/Ship Date From, Include Zero UOH Only |
| T7SCF | SC-F Serial Control Exceptions | print/settings |
| T7SCG | (SC-G generator config) | Total Length/Start Pos/Numeric Length/Last#/Format [NISJ] |
| T7SCH | SC-H | print/settings |
| T7SCOMP | compound serial management | Detail, Compound, Visible — compound serial/component tracking |

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
| `ISBINLOC` | Item-bin-location record (9 fields): item, location, bin, UOH, created/updated dates, default-bin flag, extra, reorder level | 31,848 records |
| `BKICLOC` | Per-location on-hand quantities per item (32 fields): UOH/UOO/UOSO/UBO, lot/serial tracked qtys | per item per location |
| `ISBINLOT` | Bin + lot cross-reference | lot-tracked items |
| `PIBINLOC` | Bin-level count records during physical inventory | PI cycle only |

`ISBINLOC` key fields: `ISBIN_LOC_ITEM` (part#), `ISBIN_LOC_LOC` (location code),
`ISBIN_LOC_BIN` (bin code), `ISBIN_LOC_UOH` (units on hand at this bin),
`ISBIN_LOC_DFLT` (Y = default bin for this item).

**Live scale at i2 Systems:** 31,848 item-bin records across 10 locations and 1,272
distinct bin addresses.

## Warehouse Control concept

Without WC enabled, inventory is tracked per-location only (BKICLOC). With WC
enabled, inventory is additionally tracked per bin within a location. This
enables warehouse picking by bin address, and bin-level counts during PI.

A single item can have multiple bins within one location (primary + overflow).
The default bin (`ISBIN_LOC_DFLT = Y`) is used when picking for SOs or issuing
to WOs unless the user specifies otherwise.

## DFM-confirmed operation details

| DFM | Confirmed purpose |
|-----|-------------------|
| T7WCBK | **Live Work Center Schedule** real-time dashboard: work center filter, configurable refresh timer (seconds), WO Status checkboxes, Operation#, Category, Customer filter — gives shop-floor visibility into what's queued per work center |
| T7WCD | **WC-D Bin Location Import**: CSV or fixed-length import; required fields: Warehouse (Location), Bin, Item Number; optional: Default Bin Y/N, Lot#, Serial#, Bin Qty; S/R/I flag controls skip/replace/ignore for existing records |
| T7WCE/F | **WC-E/F** item listing/exception reports: Active Status [YNODEPSQR], Item Type [RFAMNLBTKO], Class/Category ranges |
| T7WCG | **WC-G** Defaults: item/class/category range, Location, Bin range, Default Bin checkbox |
| T7WCH | **WC-H** Bin Master browse: Location, Name, Bin From–Thru |
| T7WCLOCFIX | **LOC SYNCH UTILITY** (maintenance tool, not a menu item): updates `MTIC.PROD.LOC` with the Default WC Bin — runs as a batch process showing File/Start Time/Current Time/Current Item/Default Loc |

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
counting, and bin-to-bin transfers. 52 T7HH*/J7HH* DFMs across 7 functional
groups. Shares BKDCLAB with the desktop [[module-DC|DC]] module.
All HH data files are Btrieve-only (none visible via ODBC/DDF).

## Menu operations

| Code | Operation | DFM(s) | Key fields |
|------|-----------|--------|-----------|
| HH-A | Scan & Ship (SSOE) | t7hhssoe + T7HHSSOE* | Item Num, Last Scan, Qty, &Rel SO, Reset |
| HH-B | Print Inventory Labels | t7hhINGA | Item No, Qty, Lot No, Serial No, Print Linked docs option |
| HH-C | Issue Materials | t7hhwog | WO#, Item, Qty, Print Labels Y/N/Ask, Use Large Screen Lookups |
| HH-D | Enter Finished Production | t7hhwop | WO#, Item, Qty, Lookup WO Status [FRXI], Prompt for Issue Date [YNOnce] |
| HH-E | Enter Physical Counts | T7HHPIC + t7hhpictags | Phys Inv No, Count Date, Emp Name (HHPIC) / Item No, Count Qty, Lot No, Serial No (tags) |
| HH-F | Enter Labor (DC) | T7HHDCA + t7hhdcb/c | Work Order, Sequence, Work Order Item, Emp Name |
| HH-G | Receive PO | t7hhpoc + T7HHPOC* | Vendor, Item, Qty, PO Type, Enable Vendor/Item Alerts, Use Large Screen Lookups |
| HH-H | Enter Shipping Info | J7HHLITN / T7HHH | SO Number, Customer Name, Track #, Ship Co |
| HH-I | Paperless Shop Floor | t7dcpsf | (Paperless Manufacturing sub-system) |
| HH-J | Print WO Label | T7HHWOLabel | Fin/Semi-Fin Seq From/Thru, Item Class, Hour remaining Filters, Ship Box RTM |
| HH-K | Transfer Inventory | t7hhinlj + T7HHINLJLot/Ser | From WC/Bin → To, Qty to Transfer, Transfer Date; sub-forms for Lot/Serial capture |
| HH-L | Multi-User Paperless | t7paperless | (Paperless Manufacturing, multi-user variant) |
| HH-M | Issue Scrap Component | T7HHWOSCRAP | Item No, Lot, Qty, Serial, Label Qty, RTM, Print Labels Y/N/Ask |
| HH-N | SO Shipping Queue | T7HHN/N2/NREL | (see Shipping Queue section) |
| HH-O | Bin-to-Bin Transfer | T7HHO | Item, Qty, Bin Qty, FROM BIN, TO BIN, Location, Transfer Date |

## HH-N: SO Shipping Queue / Dashboard

T7HHN (settings), T7HHN2 (list + action), T7HHNREL (alternate filter) form the
HH-N shipping queue. Settings fields:
- Limit Shipments to within X Working Days
- On or before: (date)
- Item Type [RFAMNLBTKO]  (R=Regular, F=?, A=?, M=Misc, N=Non-stock, etc.)
- Refresh Timer (Seconds)
- Include Customers on Credit Hold (Y/N)
- Include Released SO Lines
- Include SO Lines with 00/00/00 Dates
- Include Kit Components
- Include Back Order in SO Quantity
- Show Only Ship Early SO
- Incl Ship Early SOs with Limited Shipments
- Display SO-O-I when Printing SOs

T7HHN2 action buttons: &Lot, S&erial, Release SOs, &Print.
T7HHNDTE captures final shipping details: Ship Date, Ship Via, Tracking #, SO#, Customer, Freight.

## HH-A: SSOE and SODD variants

Two scan-ship variants:
- **T7HHSSOE** (standard) — Item Num, Qty, Last Scan, &Rel SO, Reset. Post-scan
  verify in T7HHSSOEVerify (Exit/Label/List/All) and T7HHSSOESVerify (Exit/Label/List).
  Print Box Content Labels in t7hhssoeLabels (Misc/RTM/Box/Printer/Print Lot Numbers).
- **T7HHSODD** (Direct Delivery) — SO Number, Reprint Invoice button. Separate
  workflow for direct customer shipments.
- **J7HHSSOE variants** (i2 custom): J7HHPTSSOE (PTS variant for PTS orders),
  J7HHRTSSOE (&Rel SO + Reset buttons, Reset capability for corrections).

## PO Receiving sub-forms

T7HHPOC (main) → spawns:
- T7HHPOCBin — WC Bin Selection (processing wait screen)
- T7HHPOCLot — Receive Lot Numbers (Lot Number, Last Lot Scanned, Item)
- T7HHPOCSER — Receive Serial Numbers (Serial Num, Last Serial Scanned, Item)
- T7HHPOCNotes — Notes category chooser (PO / PO Line Item / Item / Vendor)

## WO sub-forms

Finish Production (HH-D) sub-forms: T7HHWOIBin (WC Bin Selection: Component,
WO Num, Qty), T7HHWOIProcess (background PROCESS DATA wait screen),
T7HHWOLOT (Release Lot Number: Lot#, Last Lot Scanned, Qty On Hand, Bin),
t7hhwoser (Enter Serial Number: Serial Num, Last Serial Scanned, Qty).

## WO Label configuration (T7HHWOLabel)

- Finished item classification: Fin Seq From/Thru, Fin Item Class
- Semi-finished item classification: Semi-Fin Item Class, Semi-Fin Seq From/Thru
- Hour remaining Filters
- Ship Box RTM (report template for box label)
- Always Default Label Qty = 1
- Show Print Dialog box
- Use Full screen lookups

## SO Lot/Serial capture sub-forms

T7HHSOBIN — WC Bin Selection (for SO pick); T7HHSOLOT — Release Lot Number
(Lot#, Last Lot Scanned, Item, Qty, On Hand, Bin); T7HHSOSER — captioned
"Print Mattress Labels" (Serial Num, Last Serial Scanned, Item) — i2-specific
label for mattress serial tracking on SO release.

## i2 Systems extensions (J7HH*)

| Program | Caption | Purpose |
|---------|---------|---------|
| J7HHEBINC | Inventory Adjustment | Mattress serial # adjustment (Mattress Number/Desc/Serial Num) |
| J7HHEBXFER | Transfer Inventory | Mattress serial transfer (same fields as EBINC) |
| J7HHEBXferVerify | Verify Transfer | Confirm mattress transfer (Exit/List/Label) |
| J7HHLITN / T7HHH | Enter Tracking Numbers | Carrier tracking # entry: SO#, Customer, Track#, Ship Co |
| J7HHPTSSOE | Shipping | PTS order scan-ship variant |
| J7HHPTSSOELABELS | Print Box Content Labels | Box labels for PTS shipments |
| J7HHPTSSOEVerify | Sales Orders | PTS shipping verify |
| J7HHRTSSOE | Shipping | Release+Reset variant of SSOE |

## Utility forms

- **T7HHALERTMSG** — "ALERT NOTIFICATION" popup (vendor alert / item alert,
  shown when triggered by t7hhpoc settings)
- **T7HHProcess / T7HHWOIProcess** — "PROCESS DATA / Please Wait" spinners
- **T7HHItemLU** — Inventory item search (Search field, Desc column)
- **t7hhinbins** — "WC Item Lookup" (bins by WC)
- **T7HHSOLookup / T7HHWOLookup** — SO/WO lookup forms (for scan or manual entry)

## Integration

- **[[module-DC|DC]]** — HH-F Enter Labor writes to BKDCLAB (same table as desktop DC)
- **[[module-PO|PO]]** — HH-G Receive PO writes to same BKQCMSTR/BKQCTRAN as T7POJC
- **[[module-WO|WO]]** — HH-C/D/M read WORKORD, WOBOM; write INVTXN / WORECV
- **[[module-PI|PI]]** — HH-E writes to BKPIPHYS / PIBINLOC (same PI count tables)
- **[[module-SO|SO]]** — HH-A/N release SO lines; T7HHSOSER prints mattress labels
- **J7 customs** — HH-H (J7HHLITN) and J7HHEB* bridge HH to mattress serial tracking
""",

"QT": """
## What it does

Quotations / Estimating — **not a separate top-level menu module.** This code is
an alias for the [[module-ES|ES]] Estimates module. Quotes (estimates) are entered
and managed via the ES menu (ES-A through ES-E).

Key tables: `BKESTQT` (6,897 active quotes), `BKESTQTL` (462,837 lines). These
are byte-for-byte clones of `BKARINV`/`BKARINVL` (ODBC confirmed).

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

## Database tables (live counts, 2026-07-01)

| Table | Records | Fields | Purpose |
|-------|--------:|--------|---------|
| `BKRFQ` | 0 | 49 | RFQ header — 10 qty/cost breakpoints per vendor quote |
| `BKRFQDES` | 427 | 5 | RFQ vendor address lines (5 address lines per RFQ vendor) |
| `ISESTDTL` | 0 | 203 | Estimate detail tied to RFQ (cost breakdown per component) |

**At i2 Systems: RFQ is configured but currently idle** — BKRFQ has 0 active records.
BKRFQDES has 427 records (historical vendor addresses from past RFQ sessions).
BKRFQ (49 fields): RFQ#/PART/VENDOR/ITEM/QUOTE PK; then QTY_1..10 + COST_1..10
(10-break price matrix) + VENDCODE/VENDNAME/PHONE/DATE/EXPDATE/NOTES/ENTBY/EXTRA fields.

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
| `T7RTMVALID.RWN` | RTM format name validator / license checker |
| `FILELOC.B` | Maps EVO config keys to RTM filenames on disk |
| `EVOReports\\*.RTM` | All report templates (~300+ files) |
| `T6WOL*.RTM` | Work order listing reports (T6 era) |
| `T7*.RTM` | Current-era report templates |

## T7RTMVALID — report format name dialog

`T7RTMVALID.DFM` caption: **"Select Report Format Name"** (DFM confirmed).
Single field: `rtmvld_name` — the RTM file name to validate.
Buttons: Ok / Cancel / Settings.
This is invoked when a TAS program needs the user to confirm or select a
report format before printing, and validates that the named RTM file exists
and is licensed.

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

## DFM-confirmed tools (WTAS* family)

The TA module uses `WTAS*` program prefixes (not `T7TA*`) for its core tools:

| DFM | Caption / Confirmed |
|-----|---------------------|
| WTASDMGR | **"Addsum TAS Premier 7i Maintain Data Dictionary"** — full DDD manager; fields/keys tabs, Export visible rows; Key Name editor |
| WTASDATAM | **"Maintain Database"** — Sort by, file name, "Search for dates in YYYYMMDD format", Sequential (no key) mode |
| WTASINIT | **"Addsum TAS Professional 7 Create/Initialize File Program"** — File Name, Extension, FD Name, Rec Type |
| WTASCHKINT | **"DataScanIntegrity utility"** — Total Progress, Current Scan Progress, Scan Type, Records Scanned (company selector sub-dialog: All/Current company) |
| WTASCVTDICT | **"Convert Existing Dictionary"** — Working On, Next (DDF conversion tool) |
| WTASDMGR3 | **"Restructure a file"** — FD to restructure, Number of files/records remaining, Working on file |
| WTASFLOC | **"Maintain File Names and Locations"** — File Name, Extension, FD Name, Rec Type (this is the FL module) |
| WTASINIT | File Create/Initialize with same fields as WTASFLOC |

**Key finding:** WTASDMGR is the full Addsum TAS data dictionary editor — it confirms
the runtime is "TAS Premier 7i" (not just "TAS Pro 7"), and that the DDD is maintained
via a GUI tool with Fields/Keys tabs and export capability.

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

## Key tables (ODBC confirmed)

| Table | Records | Fields | Purpose |
|-------|--------:|-------:|---------|
| `BKEDIH` | 0 | 104 | Inbound EDI order staging header — identical layout to BKARINV (104f) |
| `BKEDIL` | 0 | 29 | Inbound EDI order staging lines — identical layout to BKARINVL (29f) |
| `BKEDMSTR` | 1 | 3 | EDI config (CandoEDI path, our DUNS, counter) |
| `BKEDNOTE` | 0 | 3 | EDI notes |
| `BKEDPOST` | 0 | 2 | EDI export posting log |
| `BKEDIDUN` | 0 | 7 | Trading partner DUNS↔customer mapping |

All other DE staging tables (BKDEITEM, BKDEBOM, BKDECUST, BKDEVEND, etc.)
are **Btrieve-only** (not in ODBC DDF) — they are temporary import staging
tables purged after DE-X-E Transfer.

## DFM-confirmed operation details

| DFM | Operation | Confirmed |
|-----|-----------|-----------|
| T7DEK | **DE-H Global Field Change** — File selector, Field to Change, Replace all Values toggle, search-value + replace-value pair | DFM |
| T7DEL | **DE-I Erase Files** — 7 checkboxes: Inventory / Bill of Materials / Customers / Routings / Vendors / Chart of Accounts / **Labor** | DFM |
| T7DEER | **BOM import error report** — "Only print for records that have Errors?", "Validate against Estimating or Production?", "Allow Importing Comps with 0 Qty Per" | DFM |
| T7DEFECT | **Defect Code maintenance** — Defect Code / Description / Add / Edit / Delete / Back (shared lookup table used by QC and DE) | DFM |
| T7DEM | **DE-M Import BOM** — "Import BOM Components to Estimating or Production?" toggle, "Allow Importing BOM Components with 0 Qty Per" flag, Transfer button | DFM |
| T7DEJH | DE-J-H Issue Materials sub-screen — Thru (date), Print, Add, Edit, Issue Materials buttons | DFM |
| T7DEHD | **PI-C Import Tags** (Physical Inventory count-tag import) — Skip/Replace existing tags [S/R], Count Date, Tag#, Location, Actual Qty, Item#, Employee#, Bin, Lot, Serial, Comma/Fixed Length [C/F], Import Filename | DFM |
| T7DEQ | **DE-Q Customer Invoice import** — Filename, CSV/Fixed, Skip/Replace [S/R]; columns: Invoice#/Customer/Date(YYYYMMDD)/Amount/Exchange Rate/Currency Code/Description/Terms# | DFM |
| T7DER | **DE-R Vendor Invoice import** — same layout as DEQ but with Vendor instead of Customer | DFM |
| T7DET | **DE-T Web Order Import (header)** — Rec Designator Type=H; confirmed fields: Customer Code, Order Number, Ship-To Name/Address/City/State/Postal/Country/Contact/Phone, Tax Group | DFM |
| T7DETB | **DE-T-B** — "Import to EDI Module or to Open SO File [E,S]", Date Format, Customer, Bank Account, Drop Shipment Default [Y/N/G], Include Second Description, Include Specifications, Import Comment Lines, Order ID | DFM |
| T7DEU | **DE-U Web Item Export** — CSV file name, Item Number From/Thru, Item Type [RFAMNLBTKO], Class From, Settings | DFM |
| T7DEV | **DE-V POA Import** (PO Acknowledgement) — PO#, Item#, Description, Qty, Vendor Code, Line#, Import Filename, Receipt Date, Packing Slip#, Employee# | DFM |
| T7DEPB / T7DEP860 | **DE-P-B EDI orders / DE-P-B EDI 860 PO Change** — EDI#, Customer, Release#, Customer Order; T7DEP860 adds "Import EDI 860" button; T7DEPB adds Line# | DFM |
| T7DEPD | **DE-P-D Convert EDI to SO** — New Sales Order Date, New Sales Order Number, Default Est Ship Date | DFM |
| T7DEPE | **DE-P-E Export EDI Invoice/ASN** — SO#, Customer, Invoice#, BOL#, PSV/Fixed file, Orders Entered By, Distribution Center, Create By Customer | DFM |
| T7DEPF | **DE-P-F Invoice export** — Invoice#, PSV or Fixed Length, Include Header Information, SO/Invoice toggle | DFM |
| T7DEPH | **DE-P-H Standard Pack / EDI list** — EDI# range, STANDARD PACK / CUSTOMER PO# columns | DFM |
| T7DEX | Tag-selection panel (Tag All / Untag All / Tag / Untag) — shared utility for multi-record selection | DFM |

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

## Database tables (live counts, 2026-07-01)

| Table | Records | Fields | Purpose |
|-------|--------:|--------|---------|
| `ISRMAI` | 6,986 | 84 | Active RMA lines (IS_RMA_* prefix) |
| `ISRMAAI` | 4,279 | 84 | Archived RMA lines (identical 84-field structure) |
| `ISRMAINV` | 2,194 | 104 | RMA invoice/credit memo (BKAR_INV_* clone) |
| `ISRMINV` | 3,220 | 104 | RMA invoice history (second credit memo archive) |
| `ISRMAINF` | 0 | 54 | RMA UDF extension (ISSR_INFO_* 54 user-defined fields) |
| `ISRMAC` | 12 | 3 | RMA reason codes |
| `ISRMTXN` | 0 | 14 | RMA transaction log (BKAR_TXN_* clone) |

**ISRMAI 84-field schema highlights (IS_RMA_* prefix):**
NUM(PK), PART, LINEID, DATE, RCPTDATE, CLOSDATE, STATUS(30), REASON(30), DISP(40),
OSONUM/OINVNUM (original SO/invoice), SONUM/INVNUM/CMNUM (new documents),
REORDER, WOPRE/WOSUF (repair WO), WARRANTY, FLAGS_1..20 (disposition bits:
WO/CR/SO/STOCK/SCRAP/SR/REFUND), OQTY/RQTY/IQTY (ordered/received/issued qty),
WHO, NCR#, CONTACT, PHONE, EMAIL, VNDRMA, TRACK, RETVIA, FREIGHT.

**ISRMAINV** is a full 104-field BKAR_INV_* clone — same schema as BKARINV (AR invoice
master). Stores the credit memo issued to the customer when the RMA is closed.

**Total active RMA history at i2:** 6,986 active + 4,279 archived = 11,265 RMA records.

## Integration

- **[[module-AR|AR]]** — credit memo posts to AR as negative open item via ISRMAINV
- **[[module-SO|SO]]** — original SO invoice traced via OSONUM/OINVNUM on ISRMAI
- **[[module-SR|SR]]** — Repair disposition can create a service order in SR
- **[[module-IN|IN]]** — Restock disposition triggers INVTXN adjustment

## DFM-confirmed operation details (5 DFMs)

| DFM | Caption | Key fields |
|-----|---------|-----------|
| T7RMAWHY | RMA Why | RMA Number, Line #, Status, Item, Desc., Original Invoice #, Original SO #, Reason, Description |
| T7RMD | RM-D (receive line) | Item Number, Original Inv Num/SO Num, Warranty [NLPB], Reason for Return, RMA Line Status, RMA Quantity, Received Qty, Quantity to Receive |
| T7RMDASK | Change Location | Pass RMA# to Desc/Job/None [D/J/N], Location, Enter Restock Charge, Enter SO Number, Estimated Ship Date, Original Inv/Price, RMA Item Price |
| T7RME | reason code maint. | (code/description list) |
| T7RMG | BASE Blank T7 SCREEN | (template/print base) |

**Warranty [NLPB]** — warranty status codes confirmed:
N=No warranty, L=Limited warranty, P=Parts only, B=Both/Full warranty.

**Pass RMA# to [D/J/N]** — when restocking an RMA item, controls where the RMA
number is passed: D=to Description field, J=to Job# field, N=None (not passed).
This allows GL/job-costing traceability for returned goods.
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

## Program detail — UT-K sub-suite

| Program | Procs | DB tables | Purpose |
|---------|------:|----------:|---------|
| T7UTH | 109 | 18 | File registry manager: reads FILELOC/FILEDICT/FILEKEY — the TAS7 internal Btrieve schema. Outputs file layout reports. Vars: LOC_BUFF_NAME/LOC_FILE_NAME/LOC_COMP_CODE/LOC_REC_SIZE/LOC_REC_TYPE/LOC_LOCATION/LOC_DESCRIPTION/FILEFAST |
| T7UTKD | 91 | 19 | GL fiscal-year-period recalc: FYCUR + FY1YP–FY6YP = 7-year period boundary recalculation; FROM/THRU GL account range |
| T7UTKE | 238 | 55 | Location-code mass-change: NEW.CODE + LOCATION; **55-table DB = broadest UT access** — touches every location-linked record across all modules |
| T7UTKF | 116 | 53 | Item book-value change: CHG.BOOK/BV.CHANGE/ZRET; updates standard cost fields across 53 tables |
| T7UTKG | 145 | 23 | Item status change: ACT.STATUS + FROM/THRU item/class/cat range + GL account range |
| T7UTKH | 135 | 21 | Item notes and inactive filter: INC.TYPE/INCL.INACTIVE/PRT.NOTE |
| T7UTKA | — | — | Payroll GL config (documented under [[module-PR|PR]]) |

The 55-table DB of T7UTKE is the largest in the UT suite — consolidating
inventory locations requires touching every table that records a location code
(WO, PO, SO, IN, SC, LC, PI, SH, etc.).

## Integration

UT-I (Create/Delete Company) is the mechanism for adding a new company code;
it creates the FILELOC routing records and `.B<code>` file structure.
UT-K utilities are bulk data correction tools run after data migrations or errors.

## DFM-confirmed operation details (8 DFMs)

| DFM | Caption | Key fields |
|-----|---------|-----------|
| T7UTH | file layout report | File Layout From/Thru (print FILELOC/FILEDICT layouts) |
| t7uti | company create/delete | Company Code, Company Name, Company Path, Delete Company, Create Company, Copy from another Company? |
| T7UTKA | **DATA PURGE** | D=Delete ALL data / C=Clear transaction data only; modules: GL/BKSYMSTR, AR/SO, AP/PO, Manufacturing/Inventory, Payroll, Contact Manager |
| T7UTKD | GL fiscal year | Current / Last Year / 2–6 Years Ago; GL Account From/Thru (period management) |
| T7UTKE | location code change | IMPORTANT WARNING; New master location code — mass-replaces location codes across all 55 tables |
| T7UTKF | UT-K-F item book value | process/settings |
| T7UTKG | UT-K-G item status | process/settings |
| T7UTKH | inventory type filter | INVENTORY TYPES: Item Number/Class, GL Account, Purchased Parts/Make From/Subassembly/Finished Goods item type filters |

**T7UTKA** is the most destructive utility in EVO — it can permanently delete all
records from an entire module. The DFM warning text: "To Delete ALL data in the
specified module, enter D" / "To clear transaction related data only, enter C."
This is administrator-only; running it on the production database is irreversible.
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

## DFM-confirmed operation details (6 DFMs)

**T7PSA — PS-A System Users/Passwords (confirmed fields):**
- User Name, Default Start Company, Security Level, Security Code [A/P/1/2/C/V/U/E]
- Employee / Rep., Group, Windows Username, Allow Auto Login, **Velocitrack Admin**

**Security Code [A/P/1/2/C/V/U/E]** — 8 security tier flags:
A=Administrator, P=Power User, 1=Level 1, 2=Level 2, C=Controller,
V=View Only, U=User, E=Employee. Controls module/field access rights.

**Velocitrack Admin** — Velocitrack is the barcode/mobile scanning system used
at i2 Systems for shop-floor data collection. Users with this flag have admin
access to Velocitrack device management within EVO.

**T7PSE/T7PSF — Report DFMs:**
- T7PSE "User Security Report" — User Name From/Thru, Printing Items/Groups
- T7PSF "Access to Program Report" — Program Name filter (shows all users with access to a given program)

**T7PSK — Approve Vendor (DFM confirmed):**
Caption "Approve Vendor" — vendor approval workflow requiring PS-level authorization
before a new vendor can be used in purchasing. Integrates with [[module-PO|PO]].

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

**Scale at i2 Systems:** SA reads from 462,837+ posted invoice lines (BKESTQTL, ODBC confirmed).

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

## SA-M/SA-N filter ranges (T7SAM.DFM confirmed)

The 26 FROM/THRU range pairs (BKSA.FROM1..26 / BKSA.THRU1..26) map to:
Invoice Date, Ship Date, Invoice#, SO#, Bill Cust, Ship Cust, Bill State,
Ship State, Bill Zip, Ship Zip, Bill Country, Ship Country, Cust Start Date,
Lead Source, Bill Territory, Cust Class, Sales Rep 1, Sales Rep 2, Currency,
Location, Job Num, Cust Ord#, Invoice Total, Ship Territory, plus
**line-item filters**: Item#, Item Class, Product Category, Item Desc,
SO Desc, Est Ship Date, Ship Qty, Ship Cost, Cust Ref, % Margin Range.
Quote status filter supports codes Y/L/N/A/S/D/W/B.
User-defined sort/break with up to 10 sort/break field indexes (udbrk.array[1..10]).

## Integration

- **[[module-AR|AR]]** — all SA reports draw from posted AR invoice history
- **[[module-SO|SO]]** — SA-A includes bookings (open SO) from BKSOX
- **[[module-WO|WO]]** — SA-Q uses actual WO labor+material costs for margin
- **[[module-CS|CS]]** — salesperson links via ISPRSALE / BKPRSALE

## DFM-confirmed operation details (6 DFMs)

| DFM | Caption | Notes |
|-----|---------|-------|
| T7SAA | SA-A | print/settings (standard sales report) |
| T7SAM | SA-M | From/Thru ranges, print (multi-filter sales analysis) |
| T7SAN | SA-N | From/Thru ranges, print (alternate multi-filter variant) |
| T7SAO | SA-O Top N Sales Report | Top-N customer/item ranking report |
| T7SAP | SA-P | print/settings |
| T7SAQ | Actual Margin Report | Ship Date From filter; uses actual WO costs for margin |

SA-O ("Top N Sales Report") provides ranked listing of top N customers or items
by sales volume — management summary report.
SA-Q ("Actual Margin Report") calculates true margin using actual WO
labor+material costs, not standard cost — key profitability analysis tool.
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

## Key tables (live ODBC)

| Table | Records | Fields | Purpose |
|-------|--------:|-------:|---------|
| `ISARCHG` | 211,748 | 26 | SO change audit trail — before/after field values for every SO line edit |
| `WORKCTR` | 27 | 48 | Work center master — capacity, rates, dept |
| `ISWOPRIO` | 40 | 4 | WO priority codes for Gantt color coding (PRIO/DESC/EXTRA/COLOR) |
| `BKDCLAB` | 22 | 51 | DC labor data feed to Gantt (DATE/EMP/WOPRE/WOSUF/OPER/SHIFT/HRS) |
| `ISBUILD` | 0 | 15 | WO build/staging queue — not used at i2 |

**ISARCHG** is the SO change history — 211,748 rows confirm heavy SO editing
activity at i2. Structure: `IS_CHGNO`, `IS_CHG_SONUM`, `IS_CHG_INVNUM`,
`IS_CHG_LINEID`, and 20 paired A*/B* before/after value fields covering
price, quantity, date, location, and GL fields.

## Integration

- **[[module-SH|SH]]** — SL programs are the implementation of SH scheduling menu items
- **[[module-WO|WO]]** — reads WORKORD + WOROUT + BKDCLAB for schedule inputs
- **[[module-DC|DC]]** — BKDCLAB time-clock feed drives Gantt actual vs scheduled
""",

"SP": """
## What it does

Statistical Process Control (SPC) — in-process quality measurement module
that captures inspection data at the work order / operation level. Tracks
accepted, rework, and scrap quantities per operation with Drawing/Revision
references. Provides real-time live dashboard and PPM (Parts Per Million)
defect reporting.

## Menu operations (DFM-confirmed, 6 DFMs)

| Code | Program | Description |
|------|---------|-------------|
| SP-A | T7SPC | **SPC Entry** — Inspector# / Employee / Work Order / WO Item / WO Qty / Customer / Drawing / Revision / Sequence / Accepted Qty / Rework Qty / General Notes; Sort By field |
| SP-B | T7SPCLIVEGRID | **Top Real Time Errors** — live grid display of current SPC errors (auto-refresh) |
| SP-C | T7SPCLIVEREP | **Live SPC Report** — Types/Details From/Thru / Date range / Show Top N / **Refresh Every X Mins** (auto-refreshing live report) |
| SP-D | T7SPCREP | **SPC Report** — WO#/Parent Part/Employee/Date/Sequence/**Sides**/Types/Details/Test Types/Serial#/**Test Reason [P/R/B]**/Customer |
| SP-E | T7SPCREP2 | **SPC Report (variant 2)** — same filter set as SP-D |
| SP-F | T7SPCREPPPM | **PPM Report** — WO#/Parent/Date/Sides/Types/Details/Customer/**Include S/R** (scrap/rework toggle) |

**Sides From/Thru** — mattress and foam products have inspectable "sides" (top/bottom/border/handle); this filter enables side-specific SPC tracking.

**Test Reason [P/R/B]** — P=Pass-test/Production, R=Rework, B=Both. Filters SPC records by why the inspection was performed.

**PPM** = Parts Per Million defect rate — standard manufacturing quality metric for defect frequency across large production runs.

## Database (via ISQC.SPC.* namespace)

SPC data is stored in ISQC.SPC.* tables (41-variable namespace confirmed from
T7DCPSF(290p) analysis). Live SPC data is also accessible from T7DCPSF (DC-PSF /
HH-L Paperless Shop Floor), making it visible on the shop floor without running
the SP module separately.

## Integration

- **[[module-DC|DC]]** — DC-PSF (Paperless Shop Floor) accesses the same SPC
  data; ISQC.SPC.*(41-var) namespace shared between DC and SP
- **[[module-QC|QC]]** — QC tracks incoming inspection; SP tracks in-process operation-level inspection
- **[[module-WO|WO]]** — WO# / Sequence are the primary keys on SPC records
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

| Code | Operation | DFM | Key fields |
|------|-----------|-----|-----------|
| CM-A | Enter Contact Accounts | T7CMA | Account, Name, Address, City/State/Zip, Country, Contact, Phone, Fax, Currency, Group, SIC, Sls Rep 1 |
| CM-B-B | Print Accounts Listing & Labels | T7CMBB | Report Code, Description, Date, Primary Sort, Filters, SIC Code |
| CM-B-C | Print Reminders | T7REMINDRPT | (reminder print) |
| CM-B-F | Print Notes | evonotesrpt | (notes print) |
| CM-C | CRM Dashboard | t7jcrm | (Java CRM dashboard) |
| CM-J | Change Account Codes | t7cmj | (code renumber) |
| CM-K | Add Customers to Account File | T7CMK | Customer From/Thru, Customer Class From, Skip or Replace Existing, Include Ship To |
| CM-M | Contact Manager Defaults | T7DSCM | (defaults maintenance) |

## DFM-confirmed sub-forms

**T7CMACON / T7CMCON — Customer Contact Information**
Two contact sub-forms (CMACON = full; CMCON = simplified).
CMACON fields: Customer, Contact Name, Position, Primary Contact flag,
Phone Numbers (phone1..phone10), and **E-mail include flags**:
Ack (acknowledgement), PkSlip (packing slip), Invoice, Quote, Statement,
RFQ, PO, E-Pay. These flags control which transaction types send e-mail
to each contact automatically.

**T7CMABCL / T7CMABCLB / T7CMABCLP / T7CMACL — Class Management**
Account class code maintenance (Class + Description). Variants ABCLB/P are
alternate views. T7CMACL is the global classes list editor (all classes).
DFM caption is hardcoded "BellTec Industries" — inherited from the
system integrator's dev/test company; the caption is the form title, not
a module name.

**T7CMAKD — Key Dates**
Per-account key date tracking: Key Date Code, Description, Key Date value.
Used for anniversary dates, contract renewals, or follow-up milestones.

**T7CMfocvt / T7CMnfcvt — Conversion Filters**
T7CMfocvt: "From Rep Number → To Evo User Name" (converts legacy rep-number
assignments to named EVO user IDs); filter: Transaction Date From/Thru.
T7CMnfcvt: "Customer From/Thru" with Transaction Date From filter.
These are data-migration utilities for rep-code upgrades.

## Database tables (live counts, 2026-07-01)

BKCM* tables are **in the PSQL DDF and ODBC-accessible** at i2 Systems.

| Table | Records | Fields | Purpose |
|-------|--------:|--------|---------|
| `BKCMCUST` | 1,267 | 106 | Customer CRM account (links to BKARCUST by customer code) |
| `BKCMACCT` | 1,264 | 41 | Prospect / non-customer CRM account |
| `BKCMACCN` | 5,754 | 154 | Account notes + up to 10 contacts per account (avg 4.5 contacts) |
| `BKCMACTH` | 3,446 | 21 | Activity history: START/STOP timestamps, billing flag, rep |
| `BKCMACTF` | 468 | 11 | Follow-up records: due-date, SO link, status |
| `BKCMMHST` | 2 | 72 | Campaign / mailing history (20-class filter) — barely used |
| `BKCMREP` | 4 | 14 | Sales rep access flags — 4 reps configured |
| `BKCMTERR` | 7 | 11 | Territory codes — 7 sales territories |
| `BKCMDUN` | 0 | 36 | 10-level dunning ladder (not configured at i2) |
| `MKAHIST` | 12 | 9 | System activity history log (audit, used by 158 programs) |
| `CLASMSTR` | 185 | 2 | Account class codes (CLASS + DESCRIPTION) |

**Scale at i2:** 1,267 CRM customers + 1,264 prospect accounts = 2,531 total CRM accounts;
5,754 account notes/contacts; 3,446 activity history records; 4 sales reps; 7 territories.
CRM is **actively used** at i2 Systems for managing both customers and prospects.

**BKCMACCN** (154 fields) is the account notes hub: each account record holds
10 inline contact slots (CONTACT_1..10 with name/title/phone/email/fax each),
plus note text fields, lead source, classification, territory, rep assignment,
and up to 20 category flags (BKCM.CLASS_1..20).

## Integration

- **[[module-AR|AR]]** — BKCMCUST links to BKARCUST; CM-K imports AR customers into CRM
- **[[module-SO|SO]]** — SO module reads BKCMACTH for quote-to-order history
- **[[module-SA|SA]]** — SA reports can filter by BKCMTERR (territory) and BKCMLEAD (lead source)
""",

"CC": """
## What it does

Credit Card processing — a separate T7CC* module that handles real-time credit
card charges, CC data import, and CC-linked transaction lookup. Works alongside
the [[module-AR|AR]] and [[module-PO|PO]] modules to process both customer
(AR) and vendor (PO/AP) credit card payments.

## Menu operations (DFM-confirmed, 6 DFMs)

| Code | Program | Description |
|------|---------|-------------|
| CC-C-ITM | T7CCCITM | **Charge by Item Number** — Item# lookup; Process button (lookup CC charge associated with an item) |
| CC-C-WOT | T7CCCWOT | **Charge by Work Order** — WO# / Location / Go button |
| CC-D/DE | T7CCDE | **CC Data Import** — bulk CSV/fixed CSV: Customer Code / CC Number / Expiry Date / Sort; import customer CC info on file |
| CC-P | T7CCP | **Process Customer CC Payment** (AR-linked) — CC Number / Expiry (MMYY) / Zip Code / Address / Name on Card / Amount / CC Type / CC Processor / Use a Different Card |
| CC-PO | T7CCPO | **PO/AP Credit Card Charge** (PO-linked) — CC Number / Expiry (YYYY) / Amount / Zip / CVV / Address |
| CC-R1 | T7ccr1 | **Credit Card Invoice List** — Terms From / Date range (report of CC-linked invoices) |

**T7CCP vs T7CCPO:** CCP handles customer AR payments (has CC Type, CC Processor, Name on Card, MMYY expiry), while CCPO handles PO/AP vendor payments (adds CVV field, YYYY expiry format — different form of the card entry).

**T7CCDE CC Import:** allows bulk import of customer CC data (card-on-file) from an external file with column mapping for Number/Expiry/Customer.

**At i2 Systems:** IS.CC.* (8 fields) confirmed in prior passes; CC processing is active for customer SO/AR transactions; BKCC* tables are Btrieve-only (not in ODBC DDF).

## Integration

- **[[module-AR|AR]]** — CC-P charges appear as cash receipt entries in BKARINV
- **[[module-PO|PO]]** — CC-PO charges linked to PO/AP payment; CC-C-WOT links CC charges to WO cost
- **[[module-CP|CP]]** — see also CP stub for general credit/payment overview
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

## Database tables (live counts, 2026-07-01)

| Table | Records | Fields | Purpose |
|-------|--------:|--------|---------|
| `ISCRISLS` | 0 | 10 | Contract sales compliance tracking (ISCR_SLS_CUST/ITEM/dates/qty) |
| `ISSOREVU` | 0 | 12 | SO review staging — one row per department per SO pending |
| `ISCTREVU` | 0 | 17 | Approver master — who can sign off on CR approvals |

**All CR tables have 0 records at i2 Systems — the CR module is configured but not
actively used.** Tables exist in the DDF and ODBC schema but contain no data.

**ISSOREVU** (12 fields): IS_SOVU_SONUM, DEPT(25), EMPNME(25), EMPNUM(5), MOTPAS(10),
ADATE, EDATE, APPROVE(1), REQUIRE(1), ENTBY(25), ENTMOT(10), EXTRA(100).
One row per department assigned to review a SO. APPROVE='Y' when signed off.
REQUIRE='Y' forces the department to approve before SO proceeds.

**ISCTREVU** (17 fields): IS_CREVU_EMPNME, EMP(5), DEPT(25), ADMIN(1), LEVEL(2),
MOTPAS(10), ACTIVE(1), CDATE, EDATE, ADATE, ATIME, FLAG_1..5, EXTRA(100).
This is the approver master — lists who is authorized to sign CRs. MOTPAS is the
one-time-password used as the approval PIN (same mechanism as PS-J electronic signers).

**ISCRISLS** (10 fields): IS_CR_SLS_CUST(10), ITEM(15), SDATE, SUOH, SHPQTY,
SHPDTE, INVNUM, FDATE, FUOH, SOLDTE — tracks contract compliance by customer+item.

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
| `ISFXASST` | 589 | Asset master (48 fields, ODBC confirmed) |
| `ISFXATRN` | 22,568 | Depreciation transactions (12 fields, ODBC confirmed) |
| `ISFXBOOK` | Btrieve-only | Depreciation book definitions |
| `ISFXDEP` | Btrieve-only | Depreciation schedule per asset |
| `ISFXCLS` | Btrieve-only | Asset class codes |
| `ISFXLOC` | Btrieve-only | Asset location codes |

Key note: `ISFXATRN` stores **redundant copies** of the 4 GL account fields
from ISFXASST. This means changing the GL accounts on an asset after posting
does not corrupt historical transaction records.

## DFM-confirmed details (3 DFMs)

| DFM | Caption / Confirmed |
|-----|---------------------|
| T7FAA | **FA-A Enter Asset** — Asset Number, Type, Description, Cost Basis, Residual Value, Life (depreciation life in years) |
| T7FAB | **FA-B Post Depreciation** — Asset Number, Amount, Percent, Post date, Net Asset Value, Accumulated Dep Acct; confirms GL accounts visible on posting screen |
| T7FAE | **FA-E Export Assets** — File Name (with path), Length or Delimited import format, Asset Number; `* = Basic Fields` note for simplified export |

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

- DFM caption: **"Maintain File Names and Locations"** — full CRUD (Create/Update/Delete),
  not just browse (WTASFLOC.DFM confirmed)
- Opens `FILELOC.B` (the runtime file-location registry) which maps 386+ logical
  table names to their physical `.B` file paths
- From FILELOC, the user selects any table entry and can create, edit, or delete it
- **Update All** button regenerates all path mappings from the canonical registry
- 74-table database fingerprint: FL reads all FILELOC-registered tables
- Programs: `WTASFLOC.RWN` (22 procs, source: `wtasfloc.SRC`) + `WTASFLOCUPD.RWN`
  (update sub-form) — one of the few readable `.SRC` files on the network share

## DFM form fields (WTASFLOC.DFM confirmed)

| Field | Label | Purpose |
|-------|-------|---------|
| `CF_FLNAME` | File Name | Logical table name (key into FILELOC) |
| `CF_FLCODE` | Extension | File extension (e.g. `.B`) |
| `CF_RTYPE` | Rec Type | Record type code (combo) |
| `CF_DESC` | Description | Human-readable description |
| `CF_PATH` | Path | Physical file path |
| `CF_FDNAME` | FD Name | Field dictionary name (links to FILEDICT) |

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
- Writes to `ISICMSTR` (IS-era item extension) + `ISICEST` (estimating IC mirror)
- `TNOR` / `TPR` flags select which cost tier (normal vs. prime) to transfer

## Database tables (live counts, 2026-07-01)

| Table | Records | Fields | Purpose |
|-------|--------:|--------|---------|
| `BKICMSTR` | ~51,938 | 176 | Production item master (source of truth) |
| `ISICMSTR` | 51,938 | 93 | IS* item extension: weight/dims/tool/lead/flags/alphas/numerics |
| `ISICEST` | 51,408 | 64 | Estimating IC mirror: full BKICMSTR clone (BKIC_PROD_* prefix) |
| `MTICMSTR` | 50,990 | ~60 | Multi-company IC mirror (MTIC_PROD_* prefix) |
| `ISCYCLCD` | 0 | 7 | Cycle count frequency codes (not configured at i2) |
| `ISCYCLE` | 0 | — | Cycle count schedule (not in use) |

**ISICMSTR** (IS* item extension, keyed on IS_PROD_CODE):
Extends each BKICMSTR record with additional i2-specific attributes:
IS_PROD_WT (weight), IS_PROD_ITP (item type), IS_PROD_HI/WD/LG (dimensions),
IS_PROD_FOBPAL/FOBFULL (FOB pallet/full), IS_PROD_TOOL (tooling ref), IS_PROD_SLEAD (supplier lead),
IS_PROD_FLAG_1..10, IS_PROD_FLAGS_1..25 (35 flag fields), IS_PROD_ALPHA_1..5, IS_PROD_ALPHA2_1..10,
IS_PROD_NUM_1..5, IS_PROD_NUM2_1..10, IS_PROD_GDATES/GDATES2 (10 date slots), IS_PROD_RCODE.

**ISICEST** (estimating mirror, keyed on BKIC_PROD_CODE):
Near-complete clone of BKICMSTR: BKIC_PROD_DESC/TYPE/UM/CAT/TXBLE/CLASS/RLVL/RAMT/LSALE/etc.
(64 of BKICMSTR's 176 fields). IC-A keeps this synchronized for the ES Estimating module.

Count divergence: ISICMSTR=51,938 vs MTICMSTR=50,990 vs ISICEST=51,408 — minor lag from
IC-A not having been run for all records equally, but all are near-complete mirrors.

**Cycle count** scheduling (ISCYCLCD/ISCYCLE) is managed through [[module-PI|PI]] Physical
Inventory, not through the IC utility. These tables are empty at i2 Systems.

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

## Database tables (live counts, 2026-07-01)

| Table | Records | Fields | Purpose |
|-------|--------:|--------|---------|
| `ISMCF` | 1 | 49 | Multi-currency config singleton (ISIS_MCF_CODE/BASE/GL pairs) |
| `ISLANDF` | 1 | 6 | Landed cost GL account mapping (duty/freight/customs fee GL pairs) |
| `MTEXCHG` | 0 | 7 | Exchange rate master (EXCHG_QUOTE/AMT/DESC/COST/EXTRA/CODE) |
| `ISMCR` | 0 | 22 | Exchange rate history (ISIS_MCR_BASE/DATE/SOURCE_1..4/RATE_1..4 etc.) |

**At i2 Systems: IM is configured but not actively used.** ISMCF=1 (module is set up) and
ISLANDF=1 (one landed cost GL mapping exists) but MTEXCHG=0 and ISMCR=0 — no foreign
currencies are in use and no exchange rates are being tracked.

**ISLANDF** (6 fields): ISIS_LND_GLADT/GLDDT (duty GL account+dept), ISIS_LND_GLAFR/GLDFR
(freight GL account+dept), ISIS_LND_GLACF/GLDCF (customs fees GL account+dept).
One row holds the default GL posting targets for landed cost components on POs.

**ISMCF** (49 fields): ISIS_MCF_CODE (base currency code), ISIS_MCF_BASE (base currency name),
ISIS_MCF_GLABK/GLDBK (bank account/dept), ISIS_MCF_GLABS/GLDBS (balance-sheet FX account),
plus 44 more configuration flags for multi-currency AR/AP/GL behavior.

**T7AUTOFX.RWN** — automatic exchange rate update program: reads OANDA API key from
ISTS.CFG.FXKEY in BKYSMSTR, calls OANDA REST API, and populates MTEXCHG + ISMCR.
This program exists but is not scheduled at i2 (MTEXCHG remains empty).

## Integration

- **[[module-AP|AP]]** — foreign currency POs converted using IM exchange rates
- **[[module-AR|AR]]** — multi-currency AR invoices use MTEXCHG rates
- **[[module-GL|GL]]** — currency gain/loss posts to GL on settlement
- Auto FX rate update: `T7AUTOFX.RWN` uses OANDA API (key in ISTS.CFG.FXKEY) to
  update MTEXCHG rates automatically via ISJAVA task queue

## DFM-confirmed operation details (5 DFMs)

| DFM | Operation | Key fields |
|-----|-----------|-----------|
| T7IMB | IM-B Currency Codes | Code, Description, Base, Symbol, Text, Pos (position), Decimals, Accounts Payable GL, Control Account |
| T7IMC | IM-C Exchange Rates | Date, Base currency, Source, Rate (manual rate entry table) |
| T7IMD | IM-D Landed Cost GL Accounts | Duty Account, Freight Account, Customs Fees Account |
| T7IME | IM-E Duty Rate Codes | Code, Percentage; "first 3 chars of Duty Code represent the Vendor" |
| T7IMF | IM-F Broker/Customs Fees | Broker, Percentage, Type, Flat Fee |

T7IMD confirms that landed costs (duty/freight/customs) post to separate GL accounts.
T7IME's note that the first 3 chars of Duty Code = Vendor code means duty rates are
per-vendor — different suppliers have different tariff classifications.
""",

"IS": """
## What it does

ISTS Custom Enhancements — **not a standard EVO top-level module.**
`IS` is the prefix used for i2 Systems (ISTS) database enhancements and
custom programs added on top of the standard EVO install.

## What lives under IS* (live counts, 2026-07-01)

| Family | Key tables + record counts | Description |
|--------|---------------------------|-------------|
| `ISAP*` | (11 tables) | AP enhancements |
| `ISAR*` | (22 tables) | AR enhancements |
| `ISES*` | ISESTAQT=5,816 / ISESTAQL=130,792 | Estimating: archived quotes (BKAR_INV_* clone, 104f) + quote lines (BKAR_INVL_* clone, 29f) |
| `ISSO*` | ISSSOH=37 / ISSSOL=1,177 | Service orders (BKAR_INV_* clone, 104f) |
| `ISRMA*` | ISRMAI=6,986 / ISRMAAI=4,279 / ISRMAINV=2,194 / ISRMINV=3,220 | RMA: active+archived records, credit memos (BKAR_INV_* clone, 104f) |
| `ISWO*` | (6 tables) | WO enhancements |
| `ISGL*` | ISGLDATE=1 / ISGLHDAT=18 / ISGLBDGT=2,173 / ISGLCOA=2,181 | GL period/budget/COA extensions |
| `ISPR*` | ISPRSALE=0 | Payroll/sales enhancements (not active at i2) |
| `ISPO*` | ISSPOH=34 / ISSPOL=182 | PO enhancements |
| `ISFO*` | ISFOHEAD=10,842 / ISFOLINE=934,922 / ISFOHIST=25,338 | Features/Options product configurator |
| `ISQC*` | ISNCR=74 / ISCAR=0 | QC NCR/CAR extensions |
| `ISIC*` | ISICMSTR=51,938 / ISICEST=51,408 | Item master + estimating IC extensions |
| `ISFA*` | ISFXASST=589 / ISFXATRN=22,568 | Fixed Assets |
| `ISSS*` | (same as ISSO*, re-used prefix) | Service/Repair order tables |
| `ISCR*` | ISCRISLS=0 / ISSOREVU=0 / ISCTREVU=0 | Contract Review (configured, not active) |
| `ISJOB` | ISJOB=45,863 / ISJBSF=142 | Job Costing codes |
| `ISBINLOC` | (WC bin locations) | Warehouse bin locations (used by [[module-WC|WC]]) |

**Key architectural pattern:** IS* tables that store document headers use the same
`BKAR_INV_*` 104-field schema as BKARINV (AR invoice master). This applies to:
ISSSOH (service orders), ISRMAINV/ISRMINV (RMA credit memos), ISESTAQT (archived quotes).
Document lines use the `BKAR_INVL_*` 29-field schema. This one-schema-fits-all approach
means all IS* document types can use the same posting and printing infrastructure as AR.

## Custom programs

Programs with `J7` prefix or `ASSIGN(" - ISTS Enhancement MM/DD/YY")` in source
are i2 Systems customizations. Example: `T7GFPRICE.DFM` (Golding Farms pricing).

The IS table family is fully accessible via Pervasive PSQL ODBC (unlike BKCM* tables).

## Utility: T7ISMCC — Multi-Currency Conversion

Caption: "Convert Source to Base Currency". Fields:
- GL Period, Beginning Date
- Convert/Post as of What Date?
- Convert as of What GL Period?

T7ISMCC is the multi-currency revaluation utility — converts foreign-currency
balances to the base currency as of a specific GL period. Writes to GL. This is
the only confirmed IS-prefix DFM in the EVO install (T7ISMCC.DFM + T7ISMCC.RWN).
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

Activity Control — WO date management, action/reason code maintenance, and
account-number fix utilities. 5 programs sharing a 16-table database (WORKORD,
WOBOM, WORO, INVTXN, BKICMSTR, ISTRIGRS core).

**Note on GL consolidation:** Multi-company GL consolidation ("AC" in some
older ERP parlance) is in [[module-AM|AM]] AM-G Consolidate Financials — not
in this AC module.

## Menu operations (3 DFMs confirmed)

| Code | DFM | Operation | Key fields |
|------|-----|-----------|-----------|
| AC-A | T7ACRDTYPE | Enter Return/Defect Types | Doc Type, Reason, Disposition (ISACTION-like table) |
| AC-B | T7ACTION | Enter Action Codes | Action Type, Description (ISACTION: TYPE/DESC/MISC) |
| AC-C | T7ACDATE | WO Date Recalculation | Start Date, Finish Date, Quantity, Parent WO, Top WO, Deleted WO, Total Qty |
| AC-D | T7ACDET | Activity Detail Fixer | (no DFM — RWN-only utility) |
| AC-E | T7ACCNFIX | Account Number Fix | (no DFM — RWN-only, updates BKCM.ACCN.* account numbers) |

## Key tables

| Table | Purpose |
|-------|---------|
| `ISACTION` | Action type codes: TYPE/DESC/MISC |
| `WODATE` | WO actual-vs-planned dates: WOPRE/WOSUF/START/FINISH/QTY/PARPRE/PARSUF/TOPPRE/TOPSUF/DELPRE/DELSUF/EXTRA/PRIO/H (14 fields, parent/top/delivery WO hierarchy + priority) |
| `BKARDTYPE` | Return/defect type codes (T7ACRDTYPE AC.RD.* vars: TYPE/REASON/DISPO/EXTRA1/EXTRA2) |

## Integration

- **[[module-WO|WO]]** — T7ACDATE recalculates WODATE records after WO changes;
  T7ACDET fixes orphaned activity detail records; all 5 programs share the 16-table WO DB
- **[[module-CM|CM]]** — T7ACCNFIX updates BKCM.ACCN.* account numbers after renumbering
- **[[module-RM|RM]]** — T7ACRDTYPE manages the return/defect type codes used by RMA workflows
""",

"DI": """
## What it does

Digital Signatures — electronic signature approval workflow for Purchase Orders.
T7DIGSIG.DFM / T7DIGSIG.RWN: requires an authorized user's password and (optionally)
a signature file before a PO above a dollar threshold can be approved or printed.

**Note on the "DI" prefix:** earlier stubs incorrectly described this as Distribution/
Drop-Ship. Drop-ship is handled within [[module-SO|SO]] (SO-A drop-ship flag) and
[[module-PO|PO]] (BKSOPO SO/PO link table), not as a standalone DI module.

## DFM-confirmed operation (T7DIGSIG.DFM)

**Caption: "Enter Digital Signatures"**

Fields:
- PO # — the purchase order requiring signature
- Vendor — vendor name (read-only display)
- Name / Description / Terms — PO summary (display)
- Entered By — user who entered the PO (display)
- Job # — job/cost code linked to PO
- Date — PO date
- Notes — free-text approval notes
- Password — authorizing user's password (required to sign)
- Signature File — path to a signature image file (optional)
- PO Threshold — dollar amount above which signature is required
- PO-A Ent By ID — tracks which PO-A entry user ID entered the PO

**T7DigSigChgPSWD.DFM** — "Change Password": Old Password, New Password,
Reenter Password (self-service password change for the DI signing authority).

## Integration

- **[[module-PO|PO]]** — T7DIGSIG is invoked from within the PO approval
  workflow when a PO exceeds the configured PO Threshold
- Signature records written to ISDIGSIG or similar IS* table (not yet ODBC-confirmed)
""",

"EX": """
## What it does

SQL Export / BI Export — **DE-A SQL Query/Export (Java Version)**. A Java Swing
application embedded in EVO via the T7Jtemp loader pattern that allows ad-hoc
SQL queries against the live Pervasive PSQL database and exports results to CSV.

This is not a standalone top-level module — it is accessible as **DE-A** under
the Data Exchange menu.

## Architecture

```
EVO menu → DE-A
  → SQLEXPORT.RWN (TAS wrapper, 23p, ISTECH.LIB)
      passes vars[60-71]: HOST/NAME/PORT/TREEDEST/COMP/NOPE/DUMMY_L/DFM/RVAL/...
  → T7Jtemp (Java loader)
  → SQLExport.jar (com.evoerp, v1.5.0, built 2014-03-19)
      Java Swing UI defined in T7JSQL.DFM (SourceFile='T7Jsql')
```

## Connection settings (T7JSQL.DFM confirmed)

The Settings panel in the Java UI has three fields:
- **Host** — Pervasive PSQL server hostname
- **Port** — default **1583** (Pervasive PSQL JDBC port)
- **Name** — database/DSN name
- **Destination** (TreeDEST combo, validated by `vld_treeDEST()`) — output target

Connection goes directly to Pervasive PSQL via JDBC, bypassing the ODBC layer.

## Two query modes

**Mode 1: Direct SQL** — type any Pervasive SQL SELECT directly and click Go.
Results display in a grid with an option to save as CSV.

**Mode 2: Query Wizard** — guided UI to pick tables → select fields → define
JOIN conditions → add filters → click Finish to build the query automatically.

## Default preset queries (CHM-confirmed)

Seven built-in reconciliation queries available via "Default Queries" button:

| Name | Purpose |
|------|---------|
| `GLPOINV` | GL transactions to PO/RNI account from AP-C with no matching PO line |
| `GLPORECPT` | GL transactions to PO/RNI account from PO-C with no matching PO line |
| `Inv_Txn_no_GL` | Inventory transactions with no corresponding GL entries |
| `INVGL` | GL transactions to inventory account with no corresponding inventory transaction |
| `INVGLACCT` | Inventory transactions with incorrect GL accounts (wrong item class/location) |
| `Inventory_Non_Asset` | Tangible inventory items posting to non-asset GL accounts |
| `Non_Inventory_Asset` | Non-tangible inventory items posting to asset GL accounts |

## Related export mechanisms

- **[[module-TA|TA-K]]** Export Data — raw table → flat file dump (no SQL required)
- **[[module-QU|QU]]** Query Executor — alternative ad-hoc query tool via
  `queryexecute.rwn` (also Java JDBC-based)
- **[[module-DE|DE]]** Data Exchange — structured EDI / `.IMP`-format file exchange
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

## US-G Triggers (T7USG.DFM confirmed)

Triggers are **scheduled business event notifications** — EVO fires a trigger
(email or on-screen alert) when defined conditions are met. T7USG.RWN manages
the trigger list; data stored in a Btrieve-only IS_TRIG* table (not in DDF).

**Trigger definition fields (IS.TRIG.\* namespace):**
- `CODE` — trigger code (PK)
- `CONTACT` — contact name to notify
- `EMAIL` / `EFLAG` — email address + enable email reminder (Y/N)
- `DAYS` — days before trigger fires (pre-notification window)
- `TRIGR` — the trigger event code
- `ONCE` — fire once on next occurrence vs. recurring
- `LDATE` / `LTIME` — last triggered date/time
- `NOTE` — free-text notes on the trigger
- `ODEL` — delete after triggered

**Trigger filter scope** — each trigger can be scoped to:
Item number, Customer code, Vendor code, SO#, PO#, WO range (prefix+suffix),
Operation, Item Class, Item Category, Planner Code, Bin Location, Item Types.

**At i2 Systems:** triggers are configured but status of active records is
unknown (IS_TRIG* is Btrieve-only, not in ODBC).

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

## T7LIMACC.DFM — Limited Access Generator / Editor

Caption: "DFM Multi Limited Access Generator / Editor"
Fields: DFM Name, Access Group, Generate, Edit, Copy

The DFM form is a code-generation tool: given a DFM file name and an access
group, it generates the ISACCESS restriction records for all fields in that
DFM. Operators: Generate (create new access records for a DFM), Edit (modify
existing restrictions), Copy (duplicate an access group's restrictions to
another DFM).

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

"EVO": """
## What it does

EVO* is the **platform layer** of EvoERP — a set of cross-cutting features
shared by every module. These are not menu modules; they appear as toolbar
buttons, right-click context menus, and pop-up panels within existing module
screens.

## Notes system (EvoNotes)

**ISNOTES — 133,574 records / 14 fields (ODBC confirmed, 2026-07-01)**

The most actively used platform feature. Every record in EvoERP (customer,
vendor, item, WO, SO, PO, invoice, etc.) can have one or more attached text
notes.

| Field | Purpose |
|-------|---------|
| IS_NOTE_ID | Note unique ID |
| IS_NOTE_TYPE | Module/record type link (WO, SO, AR, etc.) |
| IS_NOTE_NOTE | Note text |
| IS_NOTE_CDATE / CTIME / CWHO | Created date/time/who |
| IS_NOTE_EDATE / ETIME / EWHO | Last edited date/time/who |
| IS_NOTE_PRIVATE | Private (Y = visible only to creator) |
| IS_NOTE_GROUP | Group tag |
| IS_NOTE_CONTACT | Contact reference |
| IS_NOTE_ALPHA / EXTRA | Extra fields |

EvoNotes.DFM confirms: "KILL" button (delete), Contact, View Current/Archive,
search (EvoNoteSearch.DFM: string search, Current/Archived/Both, Match Case).
EvoNotesARCH.DFM: archive/restore by date range. EvoNotesRpt.DFM: notes report
by Event Date + Item# range.

## Links system (EvoLinks)

**ISLINKS — 4,196 records / 313 fields (ODBC confirmed)**

Attaches external files (PDFs, images, Office docs) to any EvoERP record.
The 313-field schema uses an `IS_LNK_TYPES_1..N` array for cross-module
type associations (one association field per module/record type pair).

Key fields: IS_LNK_UID, IS_LNK_LINK (file path/URL), IS_LNK_APP (open-with app),
IS_LNK_GLOBAL, IS_LNK_OPENWITH, IS_LNK_DATE, IS_LNK_NOTE (annotation),
IS_LNK_WHO, IS_LNK_ATYPE (attachment type), IS_LNK_PRIVATE, IS_LNK_SORT.

EvoLinks.DFM confirms: Image Preview panel, File, View Current, KILL.
EvoELinks.DFM: "Entering Links" panel (Date, Who, Link, File).
EvoLinkCVT.DFM: utility to convert old image links to EvoLinks format.

## Reminders & Alerts

**ISREMIND — 0 records / 24 fields (not used at i2 Systems)**

evoreminders.DFM: pop-up panel — ReminderMessage, Dismiss, Reschedule,
Dismiss All. evorereminders.DFM: Snooze — "Remind me again in X [time unit]".
evoalerts.DFM: system broadcast alerts — AlertMessage, Ignore, View.

## ERP Scheduler

evoERPsched.DFM confirms: "Run at time", "Schedule Every", day-of-week
checkboxes (Monday, ...). EvoSchedsetup.DFM: "Create Evo Scheduler as a
Service" (installs as a Windows service). Drives background tasks like
US-G Triggers and scheduled report email.

## Business Status dashboard (EvoBS)

Three-panel executive dashboard accessed from the main menu toolbar:

| DFM | Content |
|-----|---------|
| EvoBS.DFM | Top-level: AR Current Balance, Billings |
| EvoBSCash.DFM | Cash detail: Cash Balance, Bank Accounts |
| EvoBSWO.DFM | Work Orders: FP/Variances, Issues, WIP Balance |
| EVOBSR.DFM | Rebuild: regenerates BS aggregates from live data |

No dedicated ODBC table found — likely reads directly from BKARINV, BKARCUST,
BKGLCOA, WORKORD for live aggregation.

## Master Inquiry (EvoCSI)

EvoCSI.DFM: "Evo Master Inquiry" — single entry point for cross-module
lookup by Customer Code, Item Number, SO Number, or Invoice Number.
Resolves the question "where does this number appear?" across all modules.

## Password management

| DFM | Purpose |
|-----|---------|
| Evopass.DFM | Login password prompt |
| EVOUPASS.DFM | User + password entry |
| EVOCHANGEPASS.DFM | Change password |
| EVORESETPASS.DFM | Reset password — User Name, New Password, Reenter Password |

## Maintenance tools

| DFM | Purpose |
|-----|---------|
| EvoERPupd.DFM | Online EVO update: Initialize, FileName, FD Name |
| EvoForceUpd.DFM | Force Update (bypass version check) |
| Evocnvtb.DFM | Synchronize Data Dictionary with Btrieve — rebuilds DDF from live .B files |
| EvoERPbackup.DFM | Backup utility: file types, zip file name, Backup Type |
| EvoERPDrillM.DFM | Drill-down menu editor: Source Field, Target Field, Menu Text, Key |
| EVOFUP.DFM | Upload files to ISTS tech support: Select Tech, zip, Your Name |
| EVOSERVICESETUP.DFM | Create EvoService Windows service (SMTP, Server Path) |
| EvocfgSave.DFM | Save/Restore Evo Service Settings |
| EVOFILTERS.DFM | WO filter panel (WO#/Finished Date/Status) — shared across SH/WO/PA |

## Data Collection workstation menu

EvoDCmenu.DFM: "Data Collection Menu" with Prog1–Prog4 configurable buttons.
EvoDCmenu2.DFM: DC Menu with Main/Exit/Settings/Help.
EvoDCsetup.DFM: "Create Workstation Setup" (Server Path, Date Format).
""",

"J7": """
## What it does

J7 is the namespace for **i2 Systems custom programs** written by ISTS (the EvoERP
vendor) specifically for i2 Systems. All J7 programs are add-ons that extend standard
EvoERP modules with business-specific functionality.

**i2 Systems business context (confirmed from DFMs):** i2 Systems is a
**mattress manufacturer**. Multiple J7 DFMs reference "Mattress Number",
"Mattress Description", "Print Mattress Labels", and "Serial Num:" in the
context of serialized mattress production and shipping. The standard EvoERP
WO/SO/HH modules are extended with mattress-specific serial tracking.

## J7 programs by category (41 DFMs confirmed)

### Mattress production & shipping (HH/DC)
| Program | Caption / Purpose |
|---------|------------------|
| J7DCMATLABELS | Print Mattress Labels — Mattress Number/Description/Serial# entry |
| J7DCSSOE | Shipping — Customer Name, Serial Num, Mattress Number (ship-confirm) |
| J7DCSSOEVERIFY | Sales Orders verification list |
| J7EBSERIAL | Enter Serial Number — Item Code, Item, Last Serial Scanned |
| J7HHEBINC | Inventory Adjustment (HH) — Mattress Number/Description/Serial# |
| J7HHEBXFER | Transfer Inventory (HH) — Mattress Number/Description/Serial# |
| J7HHEBXFERVERIFY | Verify Transfer — Exit/List/Label |
| J7HHLITN | Enter Tracking Numbers (HH) — Customer, Track#, Ship Co |
| J7HHPTSSOE | Shipping (HH) — Item Num/Code/Description |
| J7HHPTSSOELABELS | Print Box Content Labels — Misc/RTM/Box/Label Qty |
| J7HHPTSSOEVERIFY | Sales Orders verification (HH) — Label/List |
| J7HHRTSSOE | Shipping (HH) — Rel SO/Reset/Clear buttons |

### AP/Purchasing
| Program | Caption / Purpose |
|---------|------------------|
| J7APPVEND | Approve Vendor — Vendor Code, Name, Max Allowable Check Amount, Approved flag |
| J7AUTOAPC | Auto Enter PO Invoices — Received Date range, Vendor Class range |
| J7I2SACH | ACH Export — Bank Account Number, Bank Account Name |
| J7POAIMPLINES | Import PO Lines — Filename, PO#, Vend Code, Name |
| J7PTRECPOLINE | Receive PO Line — Item#, Receive Qty, Description, Price |

### Sales Orders / SO
| Program | Caption / Purpose |
|---------|------------------|
| J7CRSOW | SO-W custom — SO# range, Order Date range |
| J7I2SYSTEMSOOE | Custom SOOE — multi-range filter SOOE form |
| J7SOAIMPLINES | Import SO Lines — Company Code/Name/Path, PO# |
| J7SYNCWOTOSO | Synchronize WO to SO — SO Line#, WO#, Item#, Description |
| J7ABISHIPRPT | Lapco Fulfillment Report — Customer range, Order Date range |
| J7LAPCOSO | Print Inventory Usage — Item# range, Customer range (Lapco-specific) |

### Work Orders / Production
| Program | Caption / Purpose |
|---------|------------------|
| J7PEDCB | Production Status — WO#, Description, Parent Part, Department |
| J7PTWOKI | WO-K-J custom — Item# range, WO# range |
| J7WOLL | WO-L-L custom — Sequence# range, Component# range |
| J7TMCKANBAN | Kanban Orders — Item#, Receive Qty, Description, Price |

### Inventory / Warehouse
| Program | Caption / Purpose |
|---------|------------------|
| J7BEFWEBINV | Web Item Export — CSV file, Item# range, Item Type (same as DE-U) |
| J7CIWEBIMPORT | Web Import — E=EDI module or S=SO file, Date Format, Customer |
| J7CJBUSAGE | Print Inventory Usage — Product Class/Category range |
| J7EIMDCREV | IN-H Print Inventory Listing with DC List and Reverse option |
| J7NMBINS | Bin management — Item, Description, Save/Clear |

### Job Costing / Analysis
| Program | Caption / Purpose |
|---------|------------------|
| J7MCDSAREPORT | Sales Analysis Report — YTD Date range, Customer Code range |
| J7SMJCT | Closed Job Cost Report — SO#, Item#, Order Date range |
| J7MPIMPORTAR | Import AR — filename import tool |

### System
| Program | Caption / Purpose |
|---------|------------------|
| J7CCPIC | PI-C Enter Tag Counts — Phys Inv No, Count Date, Year, Name |
| J7NMRTMPRINTER | RTM Printer config — RTM Name, Printer, Program Name, Setup |

## Key observations

- **Serial tracking on all mattresses:** J7 programs confirm every mattress unit carries
  a serial number from production through shipping, using EvoERP's standard serial
  tracking infrastructure plus mattress-specific labels (J7DCMATLABELS).
- **Lapco is a major customer:** J7ABISHIPRPT ("Lapco Fulfillment Report") and J7LAPCOSO
  are dedicated to Lapco drop-ship reporting — Lapco is a branded product line or
  key customer with special fulfillment requirements.
- **Custom vendor approval:** J7APPVEND adds an "Approved Vendor" flag and a
  "Maximum Allowable Check Amount" to the standard vendor master — a finance control.
- **Kanban support:** J7TMCKANBAN suggests i2 uses lean pull-replenishment for some
  items alongside the standard MRP-driven purchasing.
- **ACH payments:** J7I2SACH exports ACH payment files (bank transfers) — not part
  of standard EvoERP AP.
""",

}
