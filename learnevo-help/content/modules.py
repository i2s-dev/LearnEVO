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
"BM": "## What it does\n\nBill of Materials defines what components go into what assemblies. 10 menu ops. Centered on `BKBMMSTR` (parent-child relationships) and `BKBMAMTR` (alternate parts) / `BKBMEMTR` (engineering BOM).\n\nKey operations: `BM-C` Print Where-Used, `BM-D` Availability, `BM-E` Global Replace, `BM-F` Global Delete, `BM-H` Print BOM at Average Cost, `BM-J` Approved Substitutes.\n",

"MR": "## What it does\n\nMaterial Requirements Planning. Reads open demand (SO, forecast), open supply (PO, WO), current on-hand, and BOMs to compute net requirements. See [[recipe-run-mrp]] for a detailed walkthrough. The core program is `BKMRF.SRC` (readable plaintext).\n",

"DC": "## What it does\n\nShop-floor Data Collection — labor, issues, scrap, receipts captured at the point of work. Handhelds / barcode stations integrate here. See [[recipe-dc-labor]].\n\nFeeds [[module-WO|WO]] (labor, material issues) and [[module-PR|PR]] (time totals).\n",

"QC": "## What it does\n\nQuality Control — inspection plans, deviation tracking, certificate of compliance. Tables `BKQCMSTR` (plans) and `BKQCTRAN` (inspections).\n",

"JC": "## What it does\n\nJob Costing — reports actual cost vs. planned for work orders and cost centers. Pulls from `WOLABOR`, `WOMAT`, `WORECV`. Key report: `JC-A` Job Cost Report.\n",

"CS": "## What it does\n\nCommission System — tracks salesperson commissions from AR/SO activity. 16 tables, 16 menu ops. Includes multi-tier comp (primary + secondary salesperson), team splits, override rates.\n",

"ES": "## What it does\n\nEstimating — pre-sale quote builder with material, labor, and markup rolled into price. `ES-A Enter Estimates`. Feeds into [[module-SO|SO]] and [[module-WO|WO]].\n",

"SR": "## What it does\n\nService / Repair — tracks in-bound service orders (customer equipment), labor, parts consumed, and warranty. Adjacent to RMA flow in SO.\n",

"PI": "## What it does\n\nPhysical Inventory — full-count or cycle-count cycles. See [[recipe-physical-inventory]] for the full process.\n",

"SH": "## What it does\n\nShipping — pack, ship, label, track. Integrates with UPS/FedEx/USPS APIs. Labels via `J7DCMatLabels` and handheld flows.\n",

"ED": "## What it does\n\nElectronic Data Interchange — trading-partner integration for PO/invoice/ASN. Uses `BKEDH`/`BKEDL` headers/lines and `BKEDNOTE` notes. Processing via `BKEDPOST`.\n",

"SM": "## What it does\n\nSystem Manager — company setup, users, defaults, backup/restore, updates. The **largest module by form count** (109 forms). Most admin-only.\n\nSee [[security-model]] for user admin.\n",

"AM": "## What it does\n\nArchive / Maintenance — period-end close, fiscal year-end, data purges. The **critical-timing** module: what you run at month-end. See [[recipe-month-end-close]].\n",

"AD": "## What it does\n\nAdmin Defaults — three screens that configure module-wide defaults:\n\n- `AD-A` General Ledger Defaults\n- `AD-B` Checking Account Defaults\n- `AD-C` Accounts Payable Defaults\n- `AD-D` Accounts Receivable Defaults (actually `AR-S`)\n\nValues stored in `BKSYMSTR` / `BKYSMSTR`.\n",

# ── Modules added Pass 310 (2026-06-25) to eliminate all 45 module stubs ──

"LC": "## What it does\n\nLot Control — assigns, tracks, and archives lot numbers for lot-controlled inventory items. Each lot has its own on-hand quantity, receipt date, expiration date, and cost. Full suite: `LC-A` Edit Lots, `LC-B` Assign Lot Control (per-item flag), `LC-C`/`LC-C2` Lot Listings, `LC-E` Lot Expiration, `LC-F` Lot Summary, `LC-G` Archive Lots.\n\nKey tables: `BKLCMSTR` (lot master), `BKLCLOC` (lot per-bin). See also [[module-SC|SC]] for the parallel serial-number module.\n",

"SC": "## What it does\n\nSerial Control — assigns and tracks unique serial numbers for serial-controlled items. Symmetric structure to [[module-LC|LC]]: `SC-A` Edit, `SC-B` Assign, `SC-C`/`SC-D` Listings, `SC-E` Archive. Serial numbers tie to specific customer shipments (SO allocations) for traceability.\n\nKey tables: `BKSCMSTR`, `BKSCLOC`.\n",

"RO": "## What it does\n\nRoutings — defines the sequence of manufacturing operations (steps) for an item. Each operation links to a work center, setup hours, run hours, queue time, and move time. Drives WO scheduling and lead-time calculation. See [[recipe-enter-routing]].\n\nKey tables: `ROUTING` (header), `BKRTEMTR` (operations), `BKRTTOOL` (tooling), `BKRTINST` (instructions).\n",

"WC": "## What it does\n\nWork Centers — defines physical or logical production stations (machines, assembly areas, test benches). Each WC has a labor rate, overhead rate, capacity, and scheduling calendar. Referenced by [[module-RO|RO]] routings and [[module-DC|DC]] labor entries. Key menu: `WC-A Enter Work Centers`.\n\nKey tables: `BKWCMSTR`, `BKWCCAL` (capacity calendar).\n",

"HH": "## What it does\n\nHandheld / Mobile — barcode scanner and mobile device integration for shop-floor data collection, receiving, and inventory. `HH-N` is the handheld item lookup (filters by Item Type [RFAMNLBTKO], Refresh Timer, credit-hold flag). Integrates with [[module-DC|DC]] for labor and [[module-PO|PO]] for receiving.\n\nKey forms: `T7HHN.DFM`, `T7HHWRC.DFM`.\n",

"PL": "## What it does\n\nPaperless Manufacturing — displays work order routing, BOM components, QC specs, and notes on screen at the workstation, eliminating printed travelers. Key forms: `T7PLessComps.DFM` (Issue Components — All/Shortages), `T7PLessNotes.DFM` (QC Specs/WO Item/Routing/Customer/Vendor), `T7PLessWODates.DFM` (WO Dates/Qty).\n",

"QT": "## What it does\n\nQuotations / Estimating — builds pre-sale cost estimates with material, labor, and markup. See [[recipe-estimate]] for a full walkthrough. Key tables: `BKQTMSTR` (estimate header), `BKQTLINE` (lines). `QT-B Convert to SO` turns an accepted estimate into a live sales order.\n",

"RF": "## What it does\n\nRFQ (Request for Quotation) — sends quote requests to multiple vendors and tracks their responses before issuing a PO. See [[recipe-rfq]]. Key tables: `BKPORFQH` (header), `BKPORFQL` (lines/responses). `PO-J Accept RFQ` creates a PO from the winning quote.\n",

"RT": "## What it does\n\nReport Templates — the ReportBuilder `.RTM` file engine. All EVO reports are `.RTM` files on the network share under `EVOReports\\`. Reports are designed in `RBDsgnr.exe` (Nevrona ReportBuilder). `FILELOC.B` maps configuration names to `.RTM` filenames. See [[recipe-custom-report]].\n",

"TA": "## What it does\n\nTools / Admin Utilities — backup, restore, software updates, company setup, and purge operations. Key forms: `TA-O Evo Backups` (local ZIP + optional cloud upload), `TA-P Apply Updates` (.UPD file processor). See [[recipe-backup]] and [[recipe-update-evo]].\n",

"SY": "## What it does\n\nSystem — user administration, access control, and company switching. `SY-A Enter Users` manages login IDs, passwords, access levels, and module restrictions. `SY-B Menu Restrictions` hides specific menu items. `SY-C Add Company` creates a new company. See [[recipe-add-user]], [[recipe-add-company]], [[recipe-switch-company]].\n\nKey table: `BKSYUSER`.\n",

"DE": "## What it does\n\nEDI / Data Exchange — Electronic Data Interchange for trading-partner document exchange (PO, invoice, ASN). Key forms in the `T7DEP*` and `T7DE*` family. Tables: `BKEDH`/`BKEDL` (EDI transaction headers/lines), `BKEDNOTE` (notes), `BKEDPOST` (posting queue). Also handles generic import/export via `T7GENIMP.DFM` (Import DBA — Skip/Replace/Append modes).\n",

"RM": "## What it does\n\nReturn Material — RMA tracking from customer return authorization through physical receipt, disposition (Restock/Scrap/Repair), and credit memo issuance. See [[recipe-rma]]. Key tables: `BKSORMA` (RMA header), `BKSORMAD` (detail lines).\n",

"SU": "## What it does\n\nSystem Utilities — low-level maintenance tools: index rebuild, file restructure, data verification, and diagnostic utilities. Typically accessed by administrators only. Includes table repair functions for Btrieve/Pervasive data files.\n",

"UT": "## What it does\n\nUtilities — general-purpose tools including data export, CSV import/export, and miscellaneous administrative functions. See [[recipe-export-csv]] and [[recipe-purge-history]].\n",

"LM": "## What it does\n\nLabel Management / Label Printing — prints barcoded labels for inventory items, lot numbers, serial numbers, and shipping. Uses `t7lottag.DFM` (Evo Lot Tagging — Label1/2/3 fields) for lot label printing. Integrates with [[module-LC|LC]] and [[module-HH|HH]].\n",

"LO": "## What it does\n\nLocations / Bin Management — manages warehouse bin addresses for multi-location inventory. Each bin is a slot in `BKICLOC`. Items can have a default bin in [[module-IN|IN]], and per-bin on-hand is tracked separately from total on-hand.\n",

"MA": "## What it does\n\nMachine / Asset tracking — records production machinery, maintenance schedules, and downtime in relation to [[module-WC|WC]] work centers. Each machine belongs to a work center and can be targeted in [[module-DC|DC]] labor entries.\n",

"MM": "## What it does\n\nMaintenance Management — preventive and corrective maintenance scheduling for production equipment. Tracks maintenance orders, labor, and parts used on machines in [[module-WC|WC]].\n",

"PL": "## What it does\n\nPaperless Manufacturing — electronic traveler / work-order packet displayed at the workstation. Eliminates printed travelers. Forms: `T7PLessComps.DFM` (issue components), `T7PLessNotes.DFM` (QC specs, routing notes), `T7PLessWODates.DFM` (WO dates and qty).\n",

"PS": "## What it does\n\nPlanning / Scheduling — finite capacity scheduling complement to [[module-MR|MR]] (MRP). Uses routing operation times, work center calendars, and WO priority to schedule production. Forms in the `T7SHA*` family (13 scheduling forms).\n",

"SA": "## What it does\n\nSales Analysis — provides sales history reporting and trend analysis by customer, item, salesperson, and time period. Pulls from AR/SO posted history tables. Common reports: sales by customer, sales by item, sales trend year-over-year.\n",

"SB": "## What it does\n\nSales Budget / Forecast — entry and tracking of sales budgets and demand forecasts. Budget figures feed [[module-MR|MR]] (MRP) as independent demand when actual orders are not sufficient to plan against.\n",

"SL": "## What it does\n\nSales Analysis Listings — detailed listing reports for sales data by customer, item, region, or rep. Companion to [[module-SA|SA]]. Provides the detail-level drill-down that SA summarizes.\n",

"SD": "## What it does\n\nSales / Shipping Detail — shipment detail tracking, carrier assignments, and freight billing. Related to [[module-SH|SH]] (Shipping) and SO module.\n",

"CM": "## What it does\n\nCredit Memo — processing of customer credit memos. Handles price adjustments, allowances, and return credits outside of the RMA flow. See [[recipe-credit-memo]]. Posts to AR as negative open items.\n",

"CP": "## What it does\n\nCredit and Payment processing — handles credit card and alternative payment method processing for customer accounts. Integrates with [[module-AR|AR]] cash receipts.\n",

"CR": "## What it does\n\nCredit — customer credit limit management, credit hold processing, and credit approval workflows. AR-A Enter Customers includes the credit limit and credit hold fields tracked by this module.\n",

"FA": "## What it does\n\nFixed Assets — depreciation schedules and asset register for capital equipment. Tracks acquisition cost, accumulated depreciation, book value, and disposal. Posts depreciation journal entries to [[module-GL|GL]].\n",

"FL": "## What it does\n\nFloor Control — shop-floor scheduling and sequencing at the work center level. Bridges [[module-DC|DC]] (labor capture) and [[module-SH|SH]] (scheduling) with real-time WO status on the floor.\n",

"FO": "## What it does\n\nForecasting — demand forecasting engine. Creates item-level forecasts based on sales history, seasonality, and trend analysis. Feeds planned demand into [[module-MR|MR]] (MRP) as independent demand.\n",

"FP": "## What it does\n\nForecast / Planning — planning horizon management for MRP and scheduling. Defines planning buckets (weekly, monthly) and forecast periods.\n",

"IC": "## What it does\n\nInventory Control / Cycle Count — manages cycle count schedules, assigns ABC classifications to items, and drives the cycle counting portion of [[module-PI|PI]] (Physical Inventory).\n",

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

"US": "## What it does\n\nUser-defined Settings — custom fields, user-defined codes, and site-specific configuration tables. Allows EVO to be tailored without source code changes by defining additional codes in lookup tables.\n",

"YS": "## What it does\n\nYear-end / System — year-end processing utilities beyond [[module-AM|AM]]. Handles special year-end tasks: 1099 generation, W-2 reporting (if EVO handles payroll), and fiscal-year archive operations. See [[recipe-year-end-close]] and [[recipe-1099]].\n",

}
