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
| `BKARTXN` | 2 | 14 | Unposted lot allocation to order lines — staging buffer for lot-tracked items pending AR post (EVOHELP.PDF canonical; 2 live records = currently empty/temp) |
| `BKARTXNS` | — | — | Unposted serial allocation to order lines — staging buffer for serial-tracked items pending AR post (EVOHELP.PDF §File Names, Pass 505) |
| `BKARCR` | N/A | — | Cash receipts staging — Btrieve-only |

`BKARCUST` is 106 fields (EVOHELP.PDF §AR-A confirms key fields, Pass 506):
- **Cust Cd** — 10-char alphanumeric PK
- **Alpha Sort** — sort key (default = first 6 chars of company name); used by alpha-sort reports
- **Ship to Customer? (SHIPTO)** — Y = this code is a warehouse/ship-to address only; cannot be used on bill-to side
- **Bill** — for SHIPTO=Y records, this is the associated bill-to customer code
- **Ship-to Cd** — default ship-to address code for SO entry; ship-to's salesperson/tax takes precedence over bill-to
- **FOB** — prints on SO documents; no lookup constraint
- **Ship Via** — defaults into SO header ship-via field
- **Default GL Sales** — overrides item-class GL account; used when SO module not in use (AR-B vouchers)
- **Class** — 4-char classification for report grouping
- **Start Date** — first-sale date or record creation date
- **Slsp 1/2** — two salespersons; each has own Comm field; ship-to salesperson overrides bill-to
- **Territory** — 4-char; must exist in SM-I-B Enter Territory Codes
- **Lead Source 1/2** — must exist in SM-I-A Enter Lead Source Codes
- **Resale Number** — 15-char tax-exemption resale certificate number
- **RTM Print Group** — SINGLE CHAR suffix for customer-specific RTM variants: if customer is group "A" and standard RTM is "ENSOF4.RTM", program tries "ENSOF4A.RTM" first. Allows custom invoice/SO layouts per customer group.
- **Ship Time** — transit days; SO-A uses this to auto-calc ship date = customer due date − Ship Time
- credit limit, terms code, tax code, pricing code, GL receivable account, balance forward, last payment date

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
| `AR-N` | Customer Deposits — **T7MAPDEPO.DFM confirmed**: SO# / Description / Qty / Amount / Deposit Amount / Item# / GL Account / Deposit# / Customer / Amount Remaining (maps a deposit to specific SO lines with GL account override) |
| `AR-R` | AR Payment History |

## Integration

| Module | Relationship |
|--------|-------------|
| `SO` | SO-F creates BKARINV invoices; AR records the payment |
| `GL` | Every AR transaction posts to BKGLTRAN (2.97M GL entries total) |
| `CS` | Commission System reads BKARINV to compute earned commissions |
| `AM` | AM-K archives paid invoices; AM-H posts period-end AR summary |

## AR-B voucher types (EVOHELP.PDF §AR-B, Pass 506)

| Code | Type | GL behavior |
|------|------|-------------|
| (blank/standard) | Invoice | Debit AR account; distribution must be net credits |
| Credit Memo | Credit memo | Credit AR account; distribution must be net debits |
| Cash Transaction | Direct cash, no formal invoice | Debit cash/bank account; AR account bypassed; appears on statement/aging as paid invoice if full; distribution = credits |
| D | Beginning balance invoice | Posts to aging/voucher files; does NOT post to GL (used when cutting over from prior system) |
| E | Beginning balance credit memo | Posts to aging/voucher files; does NOT post to GL |

**Distribution**: Up to 10 GL accounts; debits must equal credits for save. Default distribution amount = amount needed to balance.

## AR-C payment capabilities (EVOHELP.PDF §AR-C, Pass 506)

- **Prepayments**: Record customer deposits before invoicing (applies as credit later)
- **Early payment discounts**: Take discounts on invoices during payment application
- **Apply credits**: Apply outstanding credits without cash (Check Amount = $0)
- **NSF checks**: Enter as negative amount to reverse a prior payment
- **Partial payments**: Apply portion of check to one invoice; balance stays open
- **Split across customers**: Spread one payment across multiple customer accounts
- **X-Charge credit card**: Approval code prefix V/M/A/D (Visa/MasterCard/AmEx/Discover) stored as Check Number (must be unique); requires SD-P config
- **Multi-currency** (IM module): If IM-A Pay=N → post in source currency; Pay=Y → two GL transactions (source + conversion to base currency at IM-C exchange rate; F/E Gain/Loss recognized at payment time)
- **Check Number field**: 20-char alphanumeric; used as unique transaction ID; reusing same number can cause lookup confusion

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
| `BKAPHPOL` | N/A | — | PO receiver lines (Pass 493, DefaultSQL-confirmed) |
| `BKAPHPO` | N/A | — | PO headers (Pass 493, DefaultSQL-confirmed) |

**BKAPHPOL fields (DefaultSQL-confirmed):**

| Field | Meaning |
|-------|---------|
| `BKAP_POL_PCODE` | Part code |
| `BKAP_POL_PONM` | PO number (FK to BKAPHPO.BKAP_PO_NUM) |
| `BKAP_POL_PSTDTE` | Post date (date invoice was posted) |
| `BKAP_POL_ARD` | Actual received date |
| `BKAP_POL_INVNUM` | Invoice/voucher number |
| `BKAP_POL_PQTY` | Purchase quantity |
| `BKAP_POL_PPRCE` | Purchase price |

**BKAPHPO fields (DefaultSQL-confirmed):**

| Field | Meaning |
|-------|---------|
| `BKAP_PO_NUM` | PO number (PK) |
| `BKAP_PO_VNDCOD` | Vendor code (FK to BKAPVEND) |

**RNI (Received-Not-Invoiced) concept:** When PO-C receives goods, EVO
debits Inventory and credits a PO/RNI GL account (description =
`'RECEIVED/NOT INVOICED'`). When AP-C vouchers the invoice, EVO reverses
the RNI credit and posts the AP liability (description = `'RNI/INVOICED'`).
The two DE-A preset queries `RNI Received` and `RNI Invoiced` audit for
orphaned GL entries in this two-step process.

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

## AP-A Enter Vendors — field semantics (EVOHELP.PDF §AP-A, Pass 507)

| Field | Size | Notes |
|-------|------|-------|
| Vend Code | 10-char alphanumeric | PK; common format = first 3 letters of name 1 + first 3 of name 2 |
| Alpha Sort | 6-char | Sort key; defaults to first 6 chars of vendor name |
| Vend Name | 30-char | |
| Address 1/2 | 30-char each | Two address lines |
| City | 26-char | |
| State | 2-char | |
| Zip | 10-char | |
| Country | 30-char | |
| Contact 1 | 30-char | Three additional contacts via "Other Contacts" button |
| Telephone/Fax | 25-char each | |
| Remittance Address | — | Used on printed checks (AP-H); if blank, standard address used |
| Tax ID No | 15-char | For 1099 reporting (AP-S Print 1099 Forms) |
| Tax Group | — | PO tax authority (only if SD-C "Track PO Taxes using Tax Groups" = Y) |
| Send 1099? | checkbox | Controls which vendors get 1099 forms printed by AP-S |
| Customer at This Vendor | — | Your customer code in their accounting system |
| Class Cd | 4-char | Groups vendors for reports (e.g., out-of-state, wholesale) |
| Terms Cd | Required | Payment terms; default for PO-A and AP-B/AP-C entry |
| Default GL Exp Acct | — | Default GL account for AP-B voucher entry; overridden by item class GL on PO-based vouchers |
| Start Dt | — | First purchase date / record creation date |
| Ship Via | — | Default shipping method; defaults into POs |
| FOB | — | Default FOB point; defaults into POs |
| Print File Lbls | checkbox | Include in AP-M Print Vendor Mail Labels (file label mode) |
| Web Site | — | URL field |

**International fields** (only visible when IM-A enabled): Currency (default for POs), Duty Code (3-char, used with IN-B duty code to calculate landed cost fee), Tax-In Code (excise tax code from IM-G).

**Auto-filled status fields**: Outstanding Inv Amts (total owed), Outstanding Credits (unapplied credits), Last Purch (date of last PO receipt), Last Payment (date of last check).

**Deletion restrictions**: Outstanding Inv Amts and Outstanding Credits must both be $0.00; no open POs allowed. Archived via AM-O Archive/Purge Vendor Data rather than deleted if purchase/payment history exists.

## AP-B Enter Vouchers — voucher types (EVOHELP.PDF §AP-B, Pass 507)

| Type | Name | GL behavior |
|------|------|-------------|
| A | AP Voucher | Credits default AP account; debit distribution must balance |
| B | Credit Memo | Debits AP account; credit distribution must balance |
| C | Manual Check | Posts directly to Cash Disbursements; also optionally prints a check |
| D | Beg Balance | Populates open aging only — does NOT post to GL (system cutover use) |
| E | Beg Bal Credit | Populates open aging only — does NOT post to GL (system cutover use) |
| F | Template | Pulls predefined % distribution to multiple GL accounts; saved as A or B |

Key AP-B fields: **Inv Num** (20-char, Required), **Voucher Date** (invoice date = aging date), **GL Post Date** (defaults to today; controls GL period and aging inclusion separately from invoice date), **Desc** (25-char, prints on check stub), **Terms** (from AP-A default), **Total Amt** (12-digit), **Schedule Date** (override payment due date), **Job Number** (optional; can be Required via SM-P-F). Distribution: up to **75 GL accounts**; debits must equal credits.

## AP-C Enter Purchase Order Invoices — key behaviors (EVOHELP.PDF §AP-C, Pass 507)

- **COD vs Invoice**: COD bypasses AP, creates a manual check entry, optionally prints check. Invoice goes to AP for future payment via AP-F/AP-H.
- **Invoice Date vs GL Post Date**: Invoice date = aging date (always enter as-received). GL Post Date = accounting period (can differ for late-arriving invoices). Aging age based on Invoice Date; aging *inclusion* as-of a date controlled by GL Post Date.
- **Price override**: If unit cost differs from PO, overriding it corrects inventory last cost, average cost, and any job costing.
- **Partial invoicing**: Cannot invoice more than the received quantity. Full receipt + invoicing triggers prompt to close PO (deletes from open PO file, marks receivers as closed in history).
- **Multi-PO invoice**: One vendor invoice can cover multiple POs. Only one currency (if IM-A multi-currency) per invoice.
- **Freight / Tax / Misc Charges**: Separate fields on the invoice total; freight defaults blank; tax auto-calculated if PO had sales tax, or can be manual override.
- **RNI reversal**: AP-C posts debit to PO/RNI (Received-Not-Invoiced) account and credit to AP — completing the two-step RNI cycle started by PO-C.
- **PO-C Receive Into**: I=Inventory (items update stock immediately); Q=QC Inspection (items held in QC, must be released via PO-J-C Enter Inspection Buyoffs before they enter inventory).

## AP-F Pick Vouchers — workflow (EVOHELP.PDF §AP-F, Pass 507)

- Pick per vendor; one vendor at a time.
- Auto-apply oldest-first (answering Y to "apply against all outstanding invoices" option).
- Partial payment: enter any amount up to the invoice balance in the Applied field.
- Outstanding credits can be auto-applied (Y) or applied manually after choosing an invoice.
- **ePay button**: records electronic payments (wire transfer, credit card) without printing a check; prompts for bank account + reference number; posts immediately to check register and payment history; optionally prints a receipt.
- All picks are provisional until AP-H Print Checks is run. Can re-run AP-F to change picks by re-entering the vendor code.

## AP-H Print Checks — GL posting (EVOHELP.PDF §AP-H, Pass 507)

AP-H is the **commit step**: prints checks, then:
1. Empties the AP check register (BKAPCHKF).
2. Updates AP Payment History.
3. Posts to GL Cash Disbursements journal.
4. Adds checks to GL check register file (BKGLCHK, used for bank reconciliation).
5. Updates next check number in AD-B Checking Accounts Defaults.

## AP-I Print Aging — three report types (EVOHELP.PDF §AP-I, Pass 507)

| Type | Content | Paid items included? |
|------|---------|---------------------|
| AP Aging | Open invoices by age columns (default or custom periods); totals-only or detail | No |
| AP Listing | Transaction detail, oldest first; invoice date/number/vendor/description/original amount/remaining/age | Yes (open and paid, with start date) |
| AP Past Due | Open invoices by age based on payment terms (not invoice date) | No |

Aging is run as-of any prior date; the program recreates the aging as it was on that date. Multi-currency: run in source currency (per-currency totals) or base currency (reconcile with GL AP balances).
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

## IN-B Enter Inventory — item master sub-tabs (T6ISINB*.DFM confirmed)

The "Enter Inventory" form has at least 7 sub-tabs:

| Tab | Key fields |
|-----|-----------|
| **Main** | Item#, Description, Class, Category, Type, Act Status, Taxable, Tax In, Stock UM, Price UM, Purch UM, Duty Code, User Defined Sort Field, Characteristics |
| **ECO** | Drawing Number, Revision Level, Internal Date, Entered By, ECO Number (Add/Edit/Delete/Print) |
| **Item Links** | Order, Link, Use Global Path, File Associations vs Other, Printing, Image Thumbnail |
| **Manufacturer** | Manufacturer, Vendor Item Number |
| **MRP Settings** | Include in MRP, Reorder Level, Reorder Amount, Lead Time, Planner Code, Round MRP Quantities, Expedite Buffer (Days), Delay Buffer (Days) |
| **Specifications** | (item spec text, exact fields dynamic) |
| **Vendor** | Vendor, Vendor Item Number |

The MRP Settings tab drives MRP generation: only items with Include in MRP = Y appear in
MR runs. Reorder Level and Reorder Amount also drive IN-D (Reorder Report) independently
of MRP. ECO tab records engineering change history against the item.

**Mandatory fields for new item** (EVOHELP.PDF §IN-B): Item#, Class, Part Type, Stock UM, Price UM, Purch UM — program will not save without all 6.

**Item deletion restrictions** (EVOHELP.PDF §IN-B): Cannot delete if any of: on-hand qty > 0, open orders, in any BOM, has a routing, in active or non-purged physical inventory. Program shows list of blocking reasons.

**Specifications sub-tab**: Free-format text notepad; automatically prints on shop travelers; optionally prints on order acknowledgments, packing lists, invoices, and POs.

**Primary Vendor** (EVOHELP.PDF §IN-B): When a vendor code is entered, EvoERP automatically creates a record in the approved vendor file (PO-L). The primary vendor is the default for MR-J Generate Purchase Orders.

**Lead Time semantics** (EVOHELP.PDF §IN-B): For purchased items = calendar days order-to-receive. For manufactured items = shop days (per SM-H shop calendar) to make a typical run — does not include lower-level BOM procurement time.

**PO Conv Mult**: Purchase-to-stock UOM conversion factor. Only enter if Stock UM ≠ Purch UM AND Purch UM is not a pre-defined EVO value. Example: Purch UM=YD, Stock UM=FT → Mult=3.0.

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

## Standard Cost view (T6ISSTDCST.DFM)

`T6ISSTDCST.DFM` — "Standard Cost" — shows a two-tier cost summary for any item:

| Section | Fields |
|---------|--------|
| **This Level Costs** | Material, Freight, Labor, Setup, Outside Proc, Fixed Overhead, Var. Overhead |
| **Rolled-up Costs (All Levels)** | Material & Frt., Standard Cost, Lot Size, Item Number, Description |

This matches the standard cost rollup concept: "This Level" shows costs at this
assembly level only; "Rolled-up" includes all sub-components recursively. The Standard
Cost final value lives in `BKICMSTR.BKIC_PROD_STDC`.

## GL impact

Inventory moves always post to GL:

- Receipt: Inventory ↔ AP/PPV
- Issue to WO: Inventory ↔ WIP
- Finished receipt: WIP ↔ Inventory
- Adjustment: Inventory ↔ Adjustment account
- Sale: COGS ↔ Inventory

## T7ITMCFG — Item Number Auto-Format Configuration (DFM-confirmed)

`T7ITMCFG.DFM` (66 procs, LISTG60.LIB, 30 tables) — the "Item Configuration"
utility. The DFM shows the item number auto-format panel:

| Field | Meaning |
|-------|---------|
| Item Group | Code identifying a group of auto-numbered items |
| Total Length of Item Number | Total character length of generated item codes |
| Starting Position of Numeric Portion | Where the numeric sequence begins |
| Length of Numeric Portion | How many digits in the auto-increment |
| Last Number | Last used auto-number in this group |
| Formatted Last Number | Display-formatted version of Last Number |

Add / Edit / Delete / Save / Exit toolbar with Search. This is EVO's item number
auto-generation system: each Item Group has its own format template, and the system
increments "Last Number" each time a new item is added.

**T7ITMCFG is also the broadest item-config program (30 tables):** Opens
ISSERCNT / ISCYCLCD / ISUDFINV / IS2DBAR / WORKCTR / BKGLCOA / BKGLTRAN /
BKSBPART / BKMRPFC / DBAFIFO / ISNCR / ISNTYPE / CLASS / SERIAL / BKAPPOL /
BKAPPO and more — confirming T7ITMCFG is the master item-level configuration
editor (serial codes, cycle count codes, UDF fields, 2D barcode settings,
work center links, MRP forecast, alt-parts, FIFO layers, NCR links).

## INVTXN — Inventory transaction ledger (Pass 493, DefaultSQL-confirmed)

Every inventory movement writes a row to `INVTXN`. This table is the
mirror of `BKGLTRAN` for inventory-side entries; the two tables are
reconciled by GL↔IN audit queries in DE-A (SQL Export).

| Field | Meaning |
|-------|---------|
| `MTIT_CODE` | Part number |
| `MTIT_DATE` | Transaction date |
| `MTIT_TYPE` | Transaction type code — see table below |
| `MTIT_QTY` | Quantity moved (positive or negative) |
| `MTIT_AVGCOST` | Average cost at time of transaction |
| `MTIT_EXTRA` | Binary extra data — contains entry date at offsets 26-33 (MMDDYY format as chars: `SUBSTRING(MTIT_EXTRA,26,2)`=MM, `29,2`=DD, `32,2`=YY; century assumed '20') |
| `MTIT_CLASS` | Item class |
| `MTIT_CUST` | Customer code (for customer-specific transactions) |
| `MTIT_DEPT` | Department code |
| `MTIT_DESC` | Transaction description |
| `MTIT_INVOICE` | Invoice number |
| `MTIT_LOC` | Location/bin |
| `MTIT_LOT` | Lot number |
| `MTIT_PO` | PO number |
| `MTIT_PRICE` | Price at time of transaction |
| `MTIT_PRODLOT` | Production lot |
| `MTIT_QC` | QC code |
| `MTIT_REF` | Reference field |
| `MTIT_SCRAP` | Scrap quantity |
| `MTIT_SERIAL` | Serial number |
| `MTIT_STDCST` | Standard cost at time of transaction |
| `MTIT_VENDOR` | Vendor code |
| `MTIT_WOPRE` | Work order prefix |
| `MTIT_WOSUF` | Work order suffix |

All 24 fields confirmed from EVO3.JAR INVTXN.class (Pass 495, 2026-07-01).

**MTIT_TYPE codes (all 12 confirmed from DefaultSQL GL↔IN query):**

| Code | Meaning | GL type |
|------|---------|---------|
| A | Adjustment | OT |
| C | Credit receipt | RP |
| I | Issue to WO | WO |
| J | Journal | RP |
| M | Misc purchase | RP |
| O | Order-related | RP |
| P | Purchase receipt | RP |
| Q | Quote/misc | RP |
| R | Return sale | RS |
| S | Sale (shipment) | RS |
| T | Transfer | OT |
| W | WO completion | WO |

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

## SO-A line item field semantics (EVOHELP.PDF §SO-A, Pass 506)

| Field | Meaning |
|-------|---------|
| Ready to Invoice? | Y = auto-backorder excess over on-hand; N = use SO-E Release Sales Orders to designate ship qty |
| Backord Qty | Auto-filled when Ready to Invoice? = Y and qty > on-hand; also filled by SO-E for unshipped items |
| Price | Sourced from: price code file, base inventory price, contract price, or manual; SD-M can prohibit manual price change |
| UM | Unit of measure; M = per-thousand pricing, C or H = per-hundred; LOT or MIN = lot charge (price not multiplied by qty) |
| Disc | Discount % from customer's discount code (class × dollar amount); NOT applied to contract prices; negative = upcharge/surcharge; surcharge >9.99% requires SD-M "Enable Up Charges in Discounts" = Y |
| Tax? | Per-line taxability; defaults from IN-B item master; can be overridden; always N if order-header Taxable? = N |
| Release? | Ready-to-ship flag per line; Y = released for invoicing; set by SO-E Release Sales Orders; reset to N after invoice post |
| Est Shp | Estimated ship date per line (default = today); F7 duplicates the item to a new line for blanket orders with multiple ship dates |

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
- `PO-J-C Enter Inspection Buyoffs` (`autoT7POJC.DFM`) records accepted/rejected qty into
  `BKQCMSTR` (receive event) + `BKQCTRAN` (per-item QC detail). Form fields:
  Receiver Number, To Date, Receiver Line Qty, Bought Off to Date, Rejected to Date,
  Qty Remaining — cumulative tracking of what has been inspected against each receipt.
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

## PO types (EVOHELP.PDF §PO-A, Pass 507)

| Type | Name | Description |
|------|------|-------------|
| P | Purchase | Tangible items; received to inventory (or WO if Work Order field specified) |
| S | Service | Outside processing; Work Order and Seq fields **required**; price defaults from routing outside-processing cost; receipt posts to WO job cost, not inventory |

## PO-A line item fields (EVOHELP.PDF §PO-A, Pass 507)

| Field | Notes |
|-------|-------|
| REF | Optional line reference number; auto-assign in SD-C |
| Item Number | From IN-B; blank = comment line (no qty/price/date) |
| Location | Per-line override of header location; defaults from header |
| Job Number | Associates line item with a job for cost tracking |
| Description | Defaults from IN-B; customizable on PO without changing master; 2nd description + Specifications auto-add as comment lines |
| Quantity | 11-char numeric, 2 decimals |
| Due Date | Required; first line defaults from vendor lead time (PO-H) or item lead time (IN-B), adjusted past non-working days per SM-H calendar; subsequent lines default from prior line |
| Price | Type P: defaults from PO-H vendor price file, else IN-B Last Cost; Type S: defaults from RO-A routing outside-processing cost |
| UM pricing codes | M=per-thousand; H or C=per-hundred; LOT=flat lot charge; LB=per pound; CWT=per 100 weight; SF=per sq ft; MSF=per 1000 sq ft; BF=per board foot; MBF=per 1000 board foot; LF=per linear foot; CLF=per 100 linear feet; MLF=per 1000 linear feet |
| Conv. Fact. | PO UM → Stock UM conversion multiplier; built-in for M/H/C/LOT/LB/etc.; manual entry only for non-standard UMs (e.g., 1 REL of 5000 resistors → Conv=5000) |
| Taxable? | Per-line; defaults from IN-B; always N if order header Taxable? = N |
| Disc% | 4-digit, 2 decimal; discount off gross unit price |
| Work Order | Optional for type P; **required** for type S; received units/costs bypass inventory and post directly to WO job costing |
| Seq | Routing sequence; required for type S (must match outside-processing seq in WO routing) |

## PO-C Receive — key behaviors (EVOHELP.PDF §PO-C, Pass 507)

**Receive Into options** (pop-up at start of receipt):
- **I — Inventory**: items go directly to stock; on-hand incremented immediately.
- **Q — QC Inspection**: items held in QC; must be released via PO-J-C Enter Inspection Buyoffs before entering inventory.

**Header fields**: Receipt Date (defaults today), Packing Slip (optional; required if SD-C "Require Pack Slip Info?" = Y), Employee Number (optional receiving clerk).

**Receive All Lines? Y/N**: Y marks all remaining lines as fully received; can restrict via "Recv thru Due Date" to receive only lines through a specified date (useful for blanket/scheduled POs). Individual line exceptions can still be changed after answering Y.

**Per-line fields**: Qty this Receipt (actual count), Packing Slip Qty (vendor's count — discrepancy tracking only), Unit Cost (access controlled by SD-C: no access / view only / changeable).

**GL and inventory posting on save**: PO marked received; posts to GL and Purchases journal; updates inventory on-hand, on-PO/WIP, average cost, last cost, last receipt date, and average days to receive; per-location inventory updated too.

**Returning items**: To return items on a fully-received line, set Display Fully Recd Lines? = Y and enter a negative quantity against the line.
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

## Tables (confirmed from EVOHELP.PDF §File Names, Pass 505)

Active / live tables:
```
WORKORD         Work order header
WOBOM           Work order bill of material
WOBOMCHG        BOM changes within WO
WOBOMREM        WO bill of material remarks
WODATE          Work order dates
WOLABOR         Labor transactions
WOMAT           Material transactions
WORECV          Work order receipts
WOROUT          Work order routing
WOROUTMP        Aggregate WO routings (temporary)
WOROCHG         Routing operation changes
WORKCHG         Change audit log
WORKACHG        Actual changes
WORKCTR         Work centers
WCTRLOAD        Work center load %
ISMACS          Machine schedule
OUTPROC         Outside processing transactions
QCCODES         QC codes
SCRAP           Scrap codes
BKSHORT         Shortage tracking (temp — PCODE/WONUM/QTYREQ/SHORT)
ISWOEX          WO header 2 / UDF extensions (28f)
ISWOROEX        WO routing adjunct / op UDFs (51f)
ISWOTRAY        Paperless batch tracking (52f)
ISWOPRIO        WO priority master (4f — Gantt color coding)
ISQCMTHD        Paperless shop floor test methods (44f)
ISQCSPEC        Paperless shop floor test requirements
ISQCRSLT        Paperless shop floor test results (57f)
```

Archive (H = historical, written by SM-J-B Archive Work Orders):
```
WOHBOM          WO bill of material — archive
WOBOMHRM        WO bill of material remarks — archive
WOHDATE         WO dates — archive
WOHLABOR        Labor transactions — archive
WOHMAT          Material transactions — archive
WOHRECV         WO receipts — archive
WOHROUT         WO routing — archive
WORKHORD        WO header — archive
WOEXCHG         WO extra charges
WOHEXCHG        WO extra charges — archive
OUTHPROC        Outside processing transactions — archive
```

Visual Scheduler temp files (created by T7VSCHED/SH-R "Initialize Scheduling Files"):
```
WORKSORD        Temp WO header for Visual Scheduler
WOSROUT         Temp WO routing for Visual Scheduler
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

## Multi-Yield WO (T7MULTIYIELD.DFM confirmed)

Multi-Yield allows a single WO to produce multiple output items (co-products
or by-products from one production run). `T7MULTIYIELD.DFM` DFM-confirmed:

| Field | Meaning |
|-------|---------|
| Item Number | Output item code |
| Description | Output item description |
| Quantity | Expected yield quantity |
| Bin | Target bin location |
| Proportion Costs by [W/F/E] | Cost distribution method: **W**eight / **F**ixed / **E**qual |
| Use Standard Cost? | Use std cost instead of actual for the yield split |

The "Proportion Costs by [W/F/E]" selector confirms three co-product cost
allocation methods: by weight ratio, fixed amounts, or equal split. This is
the MU/Multi-Yield subsystem DFM form.

## WO scheduling tables (Pass 496, EVO3.JAR)

### SCHEDCAL — Shop calendar (6 fields)

Maps calendar dates to shop working days, excluding holidays and weekends.

| Field | Notes |
|-------|-------|
| SCH_CAL_DATE | Calendar date (the actual date) |
| SCH_SHOP_DATE | Corresponding shop working day number |
| SCH_SHOP_SLASH | Shop date display format (with slashes) |
| SCH_BACK_DATE | Back-scheduled date (for due-date → start-date calculation) |
| SCH_BACK_SLASH | Back-scheduled date display format |
| SCH_WH_FLAG | Warehouse/holiday flag — marks non-working days |

The WO scheduling engine uses SCHEDCAL to translate due dates to shop start dates
by counting backward through working days, skipping SCH_WH_FLAG days.

### SCHWO — Scheduled work order results (10 fields)

Stores the output of the WO scheduling run for each work order.

| Field | Notes |
|-------|-------|
| SWO_WOPRE | WO prefix (FK to BKWOMSTR) |
| SWO_WOSUF | WO suffix (FK to BKWOMSTR) |
| SWO_SHOP_START | Computed shop start date |
| SWO_SHOP_FINISH | Computed shop finish date |
| SWO_SHOP_DUE | Required ship/due date |
| SWO_DAYS_TOGO | Shop days remaining |
| SWO_RUN_DAYS | Total planned run days |
| SWO_CRATIO | Completion ratio (% complete, 0.0–1.0) |
| SWO_OPCOUNT | Number of routing operations |
| SWO_CONTENTION | Resource contention flag — set if WC is over-scheduled |

SCHWO is populated by the WO scheduling program and read by the WO schedule
view (WO-B "Print WO Schedule"). SWO_CONTENTION flags work centers that are
over-subscribed in the current schedule.

## WO extension tables (Pass 500, 2026-07-01)

Four extension/UDF tables linked to WO records:

### ISWOEX — WO user-defined fields (28 fields)
One row per WO (PK: WOPRE + WOSUF). Provides configurable extension slots for WO-level data.

| Field group | Fields | Purpose |
|-------------|--------|---------|
| PK | WOPRE, WOSUF | WO number + suffix (FK to WORKORD) |
| Text UDFs | ALPHA1..5 | 5 user-defined text fields |
| Description UDFs | DESC1, DESC2 | 2 longer description fields |
| Date UDFs | DATE1..5, CDATE | 5 date UDFs + creation date |
| Integer UDFs | INT1..5 | 5 integer UDFs |
| Numeric UDFs | NUM1, NUM2 | 2 numeric UDFs |
| Classification | ITP, ITPP | Item type pointer + parent |
| Material | MCLASS, MNUM | Material class + material number |
| Misc | EXTRA, RF | Reserved + reference field |

### ISWOROEX — WO routing operation UDFs (51 fields)
One row per WO routing operation (PK: WOPRE + WOSUF + OPER). Per-operation extension.

| Field group | Fields | Purpose |
|-------------|--------|---------|
| PK | WOPRE, WOSUF, OPER | WO + operation# |
| Text UDFs | ALPHA1, ALPHA2 | 2 text UDFs |
| Text array | ALPHA3_1..10 | 10-element text array UDF |
| Date UDFs | DATE1 | Single date UDF |
| Date array | DATE2_1..10 | 10-element date array |
| Description | DESC1 | Description UDF |
| Flag UDFs | FLAG_1..5 | 5 Y/N flag UDFs |
| Integer UDFs | INT_1..5 | 5 integer UDFs |
| Numeric UDF | NUM1 | Single numeric UDF |
| Numeric array | NUM2_1..5 | 5-element numeric array |
| Scheduling | SDAY, FDAY | Start day / Finish day (for DC tray scheduling) |
| Machine | PRMACH | Primary machine code (FK to MACHINE) |
| Qty | LQTY | Lot quantity |
| Misc | ITP, ITPP, FOI, EXTRA | Type pointers, first-op indicator, reserved |

### ISWOTRAY — WO tray tracking (52 fields)
Assembly tray system — tracks physical trays of sub-assemblies as they move through operations.

| Field group | Fields | Purpose |
|-------------|--------|---------|
| PK | CODE, OPER, WOPRE, WOSUF | Tray code + operation + WO |
| Tray ID | NUM | Tray number |
| Slots | ALPHA_1..20 | 20 text label/tag data slots |
| Bins | BIN_1..5, BINQTY_1..5 | Up to 5 bin locations + quantities |
| Locations | LOC_1..5 | 5 location codes |
| Dates | DATE_1..5 | 5 date stamps |
| Quantities | COMQTY, SQTY, QCQTY, SCRPQTY | Completed / start / QC / scrap qty |
| QC | QCREQD | QC required flag for this tray |
| Operation | OPDESC | Operation description |
| Misc | EXTRA | Reserved |

### ISORDECO — Order ECO linkage (12 fields)
Links Engineering Change Orders to specific orders (SO/PO/WO). Cross-reference for ECO impact tracking.

| Field | Purpose |
|-------|---------|
| IS_OECO_WOPRE + IS_OECO_WOSUF | Linked WO |
| IS_OECO_SONUM | Linked SO number |
| IS_OECO_PONUM | Linked PO number |
| IS_OECO_PART | Part number affected by this ECO |
| IS_OECO_ECO | ECO (Engineering Change Order) number |
| IS_OECO_REVLVL | Revision level at time of ECO application |
| IS_OECO_DRAW | Drawing number |
| IS_OECO_ENTDATE | Date ECO was applied to this order |
| IS_OECO_TMPO | Temporary operation code |
| IS_OECO_UNUM | Unique unit number |
| IS_OECO_EXTRA | Reserved |

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

## BKGLTRAN — GL transaction detail (Pass 493, DefaultSQL-confirmed)

`BKGLTRAN` is the sub-ledger GL posting table written by AR/AP/IN/PO/WO
automatically as transactions occur. **Distinct from `BKGLX`**
(the extended-GL cross-module table — see BKGLX section below).

## BKGLX — Extended GL cross-module table (Pass 495, EVO3.JAR-confirmed)

BKGLX stores richer GL posting information than BKGLTRAN, with explicit
cross-module links to WO, PO, and SO. BKGLXH is the history/archived version.

| Field | Meaning |
|-------|---------|
| `BKGLX_TRXNTYPE` | Journal/transaction type (16 confirmed codes: GLPOINV/GLSO/GLINV/etc.) |
| `BKGLX_JOURNAL` | Journal number |
| `BKGLX_TRXN` | Transaction number |
| `BKGLX_AMOUNT` | Dollar amount |
| `BKGLX_QUANTITY` | Quantity |
| `BKGLX_PART` | Part/item code |
| `BKGLX_WOPRE` | Work order prefix (FK to WORKORD) |
| `BKGLX_WOSUF` | Work order suffix (FK to WORKORD) |
| `BKGLX_PONUM` | PO number |
| `BKGLX_POINVC` | PO invoice number |
| `BKGLX_SOINVC` | SO invoice number |
| `BKGLX_CCLASS` | Customer class |
| `BKGLX_ICLASS` | Item class |
| `BKGLX_COMPANY` | Company code |
| `BKGLX_DESC` | Description |
| `BKGLX_ENTDATE` | Entry date |
| `BKGLX_POSTDATE` | Post date |
| `BKGLX_POST` | Posted flag |
| `BKGLX_ARCHDATE` | Archive date |
| `BKGLX_BATCH` | Batch number |

**Design contrast**: BKGLTRAN is GL-account focused (has BKGL_TRN_GLACCT);
BKGLX is cross-module linkage focused (has WOPRE/WOSUF/PONUM/SOINVC, no GL account).
Both tables are written for every posting event.

| Field | Type | Meaning |
|-------|------|---------|
| `BKGL_TRN_PART` | char | Part/vendor code linked to the transaction |
| `BKGL_TRN_DATE` | date | Transaction date (yyyy-mm-dd) |
| `BKGL_TRN_TYPE` | char(2) | Source type — see table below |
| `BKGL_TRN_AMT` | decimal | Dollar amount |
| `BKGL_TRN_ENTDTE` | date | Entry date (when posted) |
| `BKGL_TRN_CODE` | char | Secondary code (vendor code in AP context) |
| `BKGL_TRN_GLACCT` | char(10) | GL account number |
| `BKGL_TRN_INVC` | char | Invoice number (byte[0] is a flag; bytes[1-9] = invoice#) |
| `BKGL_TRN_DESC` | char | Description — e.g. `'RNI/INVOICED'`, `'RECEIVED/NOT INVOICED'` |
| `BKGL_TRN_BATCH` | char | Batch number (for batch-posted entries) |
| `BKGL_TRN_DC` | char | Debit/credit flag |
| `BKGL_TRN_EXTRA` | binary | Extra data |
| `BKGL_TRN_GLDPT` | char | GL department |
| `BKGL_TRN_PERIOD` | int | Fiscal period number |
| `BKGL_TRN_POST` | char | Posted flag |
| `BKGL_TRN_TRXN` | char | Transaction number |

All 16 fields confirmed from EVO3.JAR BKGLTRAN.class (Pass 495, 2026-07-01).

**BKGL_TRN_TYPE codes (confirmed from DefaultSQL cross-reference):**

| Code | Meaning | Source |
|------|---------|--------|
| `OT` | Other Transaction | Inventory Adjustments, Transfers |
| `RP` | Receipt/Purchase | PO Receipts, AP Credits, Misc |
| `RS` | Receipt/Sale | SO Shipments, Sales Returns |
| `WO` | Work Order | WO Issues and WO completions |

**INVTXN ↔ BKGLTRAN type mapping** (confirmed from GL↔IN audit queries):

| MTIT_TYPE | BKGL_TRN_TYPE | Description |
|-----------|--------------|-------------|
| A | OT | Adjustment |
| P | RP | Purchase receipt |
| S | RS | Sale (shipment) |
| I | WO | Issue to WO |
| W | WO | WO completion/return |
| Q | RP | Quote/misc |
| M | RP | Misc purchase |
| T | OT | Transfer |
| C | RP | Credit |
| R | RS | Return sale |
| J | RP | Journal |
| O | RP | Order-related |

## GL transaction variant family (Pass 496)

Three tables share the identical 16-field BKGL_TRN_* schema:

| Table | Role |
|-------|------|
| BKGLTRAN | Live GL sub-ledger postings (current period) |
| BKGLETRN | Extended GL transactions — same schema, separate physical file |
| BKGLHIST | GL transaction history archive |

`BKGLTRAN` is used by DefaultSQL cross-reference queries; `BKGLETRN` appears in
EVO3.JAR as a distinct class but all 16 fields are identical (BKGL_TRN_AMT through
BKGL_TRN_TYPE). `BKGLHIST` is the archive counterpart.

## GL journal entry tables (Pass 496, EVO3.JAR)

EVO maintains separate tables for manual journal entry batches:

### BKGLGJRN — GL general journal header (11 fields)

| Field | Notes |
|-------|-------|
| BKGL_GJ_CHKACT | Check account |
| BKGL_GJ_CVCODE | Conversion code |
| BKGL_GJ_EXTRA | Extra/binary data |
| BKGL_GJ_INVCHKN | Invoice/check number |
| BKGL_GJ_JOB | Job reference |
| BKGL_GJ_NUMLNES | Number of lines in this journal batch |
| BKGL_GJ_POSTED | Posted flag |
| BKGL_GJ_TRANSDT | Transaction date |
| BKGL_GJ_TRANSNM | Transaction/journal name (batch identifier) |
| BKGL_GJ_TYPE | Journal type |
| BKGL_GJ_TYPEN | Type number |

### BKGLGJLN — GL general journal lines (9 fields)

| Field | Notes |
|-------|-------|
| BKGL_GJL_ACCTNM | GL account number |
| BKGL_GJL_AMOUNT | Amount |
| BKGL_GJL_DC | Debit/Credit flag |
| BKGL_GJL_DESC | Line description |
| BKGL_GJL_EXTRA | Extra/binary data |
| BKGL_GJL_GLDPT | GL department |
| BKGL_GJL_JOB | Job reference |
| BKGL_GJL_LINE | Line number within batch |
| BKGL_GJL_TRANSN | Transaction/batch reference (FK to BKGLGJRN.BKGL_GJ_TRANSNM) |

**Recurring journal variants:** `BKGLRGJR` (header) and `BKGLRGJL` (lines) share
identical 11- and 9-field schemas with BKGLGJRN/BKGLGJLN. These hold template
recurring entries that auto-post on schedule (e.g., monthly depreciation).

### BKGLSTMT — GL financial statement layout (104 fields)

Three sub-groups by prefix (confirmed from Acctug.pdf AM-E program description,
Pass 497):
- `BKGL_STB_*` — Statement **B** = **Balance Sheet** (assets/liabilities/equity
  section; `GLA_F/T` = asset account ranges 1-4, `GLL_F/T` = liability ranges 1-4,
  `GLO_F/T` = owners equity ranges 1-2; `_MT` = merge/total flag; `_TTL` = section
  totals) — 34 fields
- `BKGL_STC_*` — Statement **C** = **P&L Income Statement** (Profit & Loss;
  income ranges 1-2, COGS ranges 1-2, expense ranges 1-4, other income/expense;
  `GLITTL` = income main title, `GLLTTL_1-4` = sub-group titles; `_MN_TTL` = net
  income total) — 36 fields
- `BKGL_STI_*` — Statement **I** = **Cash Flow** (Statement of Changes in
  Financial Position; `GLOETT/GLOITT` = other expense/income totals; asset/liability
  ranges; net income and non-cash expense sections) — 34 fields

The AM-E program writes this table (Format Standard Financial Statements). GL-F
reads it to print statements. Each row stores a complete statement format: 3
statement types in one 104-field record, each with account-range from/to pairs and
section title strings.

## Manufacturing GL accounting philosophy (Pass 497, Acctug.pdf)

EvoERP uses **absorption costing**:
- Labor, material, outside process, and overhead costs are **absorbed into WIP**
  (not directly expensed) as they are charged to work orders
- When WO is completed, costs transfer from WIP to Inventory (asset)
- Only when items are **invoiced** do costs become COGS (expense)

**GL accounts required per item class** (set up in IN/AD defaults):
| Account purpose | Type | When posted |
|----------------|------|-------------|
| Inventory | Asset | PO receipt / WO completion |
| WIP | Asset | Material issue / labor / OH charged to WO |
| Cost of Goods Sold | Expense | SO invoice posted |
| Sales | Income | SO invoice posted |

**Absorbed cost accounts** (set up in AD-A GL Defaults, expense section):
| Account | Posted when | Direction |
|---------|-------------|-----------|
| Absorbed Labor | Labor reported to WO | Credit (offsets actual labor) |
| Absorbed Fixed Overhead | Labor reported (% of labor) | Credit |
| Absorbed Variable Overhead | Labor reported (% of labor) | Credit |

Both fixed and variable OH are **calculated as % of direct labor** and posted
simultaneously with the labor entry. Month-end variance = actual OH − absorbed OH.

**GL account code structure**: 10-character alphanumeric code + optional
4-character department suffix (e.g., `5500-MKTG`). Departments apply to income
and expense accounts only — not balance sheet accounts.

## Related

- [[module-AM|AM - Archive/Maintenance]]
- [[module-AD|AD - Admin Defaults]]
- [[recipe-month-end-close]]

## GL-A View Chart of Accounts — field meanings (EVOHELP.PDF §GL-A, Pass 507)

**GL-A is read-only except for Budget amounts.** To create/change accounts, use AM-C.

| Field | Notes |
|-------|-------|
| Acct Code | 10-char alphanumeric GL account number |
| Dept | 4-char GL department code; blank if not using departments |
| Description | Account title |
| Type | A=Asset, L=Liability, O=Owner's Equity, I=Income, E=Expense |
| Norm Dr/Cr | D=normally Debit (asset/expense); C=normally Credit (equity/income/liability) — auto-set by Type |
| Non-Cash | Y = non-cash expense; used by GL-F Cash Flow statement to add back to net income (e.g., depreciation) |
| Current | Monthly posted amounts in current year |
| Budget | Monthly budget amounts (editable in GL-A; used for comparison in GL-F) |
| 1 Year Past | Posted amounts from prior year |
| 2 Years Past | Posted amounts from 2 years prior |
| Prior Years | Click Previous/Next buttons — up to 6 years past available |

Check AD-A GL Defaults before changing/deleting a GL account to avoid breaking system default accounts.

## GL-B Enter/Post General Journal Trxns — transaction types (EVOHELP.PDF §GL-B, Pass 507)

| Code | Type | Description |
|------|------|-------------|
| 1/GJ | General Journal | Manual adjusting entries; do NOT use for AR/AP adjustments (use AR-B/AP-B instead) |
| 2/CR | Cash Receipts | Requires Bank Account; updates check register |
| 3/CD | Cash Disbursements | Requires Bank Account; updates check register |
| 4/TT | Transaction Template | Saved recurring template; can be copied/reversed to create new entries |
| 5/BB | Beginning Balance | Initial GL balances when starting accounting on EVO |

**Other GL-B facts**:
- Up to 999 line items per transaction batch
- **Must balance (debits = credits) before posting**; can save out-of-balance and fix later
- Transactions are committed to a **temporary file** first; GL-O Print/Post General Ledger Batches does the final transfer to permanent GL
- Copy button: duplicates any transaction (including posted/template) to a new transaction
- Reverse button: copies with debits↔credits swapped (for month-end reversing accruals)
- Notes: can be attached to GJ/CR/CD transactions
- **CAUTION**: Entries here affect GL only — not AR aging or AP aging. Always use AR-B / AP-B for subsidiary ledger adjustments.

## GL-D Print Journals — journal types (EVOHELP.PDF §GL-D, Pass 507)

| Journal | What it records |
|---------|----------------|
| General Journal | GL-B General Journal type entries |
| Cash Receipts | GL-B CR entries + cash-terms SO-G invoices + AR-C payments + AR-N deposits |
| Cash Disbursements | AP-H checks, AP-F ePay, AP-B manual checks, AP-C COD payments, AR-M customer refunds, GL-B CD entries |
| Sales Journal | SO-G invoice postings + AR-B vouchers/credits + AR-D interest charges |
| Purchases Journal | AP non-cash transactions (vouchers, credits, sales tax, commissions, payroll tax transfers to AP) |
| Other Journal | Inventory value/qty changes, bank transfers, commissions, month-end currency conversions |
| Work Order Journal | All WO module transactions |
| Year End Journal | Income/expense account closure to Retained Earnings (AM-B Fiscal Year End + any prior-year income/expense posts via GL-O) |

## GL-F Print Financial Statements — options (EVOHELP.PDF §GL-F, Pass 507)

Three standard statement types (defined in AM-E Format Standard Financial Statements):
- **Income Statement** (Profit & Loss): Beg Month + End Month by fiscal period number
- **Balance Sheet**: "as of end of this Month" (one period-end snapshot)
- **Cash Flow** (Changes in Financial Position): Beg Month + End Month

Up to **4 comparison columns** per statement. Per column:

| Option | Meaning |
|--------|---------|
| C | Current year amounts |
| B | Budget amounts |
| 1–6 | 1–6 years past amounts |
| D | Column 1 minus Column 2 (difference; available for column 3 only) |

**Income statement only**: Print % (percentages beside amounts; wider output, may reduce column count).

Department filtering: Beg/End Dept Code to limit scope; Print Department Detail Y/N; Print Account Codes Y/N; Print Zero Amounts Y/N.

Consolidated report option available if AM-G Consolidate Financials has been run for multiple companies.

**Custom financial statements** (AM-I Format / AM-F Print) → use GL-N Print Custom Statements, not GL-F.
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
| `GL` | PR-F posts payroll journal entries; BKPRGLFL maps components to accounts |
| `DC` | Shop-floor time scans in BKDCLAB* feed PR-B time entry |
| `CS` | Commissions module can post to payroll for salesperson payout |
| `WO` | WO-F Enter Labor also writes time records used by PR |

## Nasco payroll export (i2-specific)

`NascoPAYex.DFM` — "Export Payroll Data" — prompts for Payroll date and exports
the period's payroll data for submission to **Nasco** (i2's external payroll service
processor). This supplements the internal PR module: i2 uses EVO for time/cost
tracking and Nasco for the actual payroll run / tax filing / check disbursement.
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

## BM-A field semantics (EVOHELP.PDF §BM-A, Pass 508)

**Allowed parent types:** F (Finished Good), A (Assembly), B (unknown), K (Kit), M (Make/Manufacturing) only. **R, L, or T type items cannot have BOMs.**

| Field | Notes |
|-------|-------|
| Lin (Line Number) | Optional; determines sort order on shop traveler and BOM reports; auto-assigned in entry order if skipped |
| Component | Item#; program auto-shows type and description; same component can appear twice (warning shown but allowed) |
| Qty Per | 8 decimal places; default 1.00000000 |
| Scrap | % = entered as value (10% = 10.00); Q = fixed quantity scrap loss; WO firming adds scrap to required qty; **% scrap does NOT round up to whole numbers — not suitable for discrete components** |
| Seq | Routing sequence; used for (1) shop traveler placement within operation, and (2) **backflushing by sequence** — components tied to a sequence are auto-relieved from inventory when that sequence is completed in WO-F Enter Labor |
| Rt# | Routing number for multi-routing work orders; components assigned to Rt# print only on that routing — departments see only their sequences and parts |
| Reference | 20-char memo field; common use: drawing bubble numbers |
| Include when backflushing parent assembly | N = exclude from scrap-assembly backflush (e.g., packaging materials not consumed on a scrapped assembly) |

**BOM line remarks**: Up to 15 lines per component (via "Line Remarks" button); optionally print on shop traveler and BOM reports.

**BOM notes**: Unlimited notes on the parent part (via "Notes" button); optionally print on shop traveler and BOM reports.

**Copy feature**: Copy all or selected components from another BOM, with or without remarks; can copy from multiple source BOMs to merge them into one target BOM.

**PS-A Security Code E (Engineer)**: Users with code E can only create/edit BOMs for parent items with Active Status = E. Prevents non-engineer users from modifying items that have been released to Production.

## BM-B / BM-C options (EVOHELP.PDF §BM-B/C, Pass 508)

BM-B Print BOM: Multi-level up to 35 levels; 2nd description line option (P=Parent/C=Component/A=Both); Specifications, BOM Remarks, BOM Notes print options; Approved Substitutes/Vendors/Manufacturers print option; qty decimal precision choice.

BM-C Print Where Used: Single-level or multi-level (up to 35); "Print for Inactive Parent?" option.
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

**T7AUTODCH.DFM (caption "AUTO DC-H"):** Automated batch-post variant of DC-H —
Employee From/Thru / Shifts [123] / WO Number From/Thru; Exit / Settings / Post
buttons; ETBcomboval = LISTG60.LIB grid. T7AUTODCH is the scheduled/automation
variant of T7DCH — same fields, designed to run unattended as part of
[[module-AU|AU]] batch automation.

**T7PUTAWAY.DFM (caption "New Screen"):** Bin-level inventory put-away form —
Part / Bin / Bin Location fields; Put Away / Print Label / Clear / Exit buttons;
ETBcomboval = LISTG60.LIB grid. Confirms the [[module-PU|PU]] Put-Away
workflow: scan/enter part number → assign to bin location → print bin label.

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
| QC-G-D | T7QCGD | **CAR List** — Item / Component / CAR# / Location / Origin (I/V/R) / Open-Review-Failed-Closed status / Filter Owner |

CAR (Corrective Action Report) has a **4-state** status (Open / Review / Failed / Closed) vs. NCR's 2-state (Open / Closed).
The "Failed" state was added in Pass 492 DFM confirmation (T7QCGA Items.Strings); prior doc said 3-state — now corrected.
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
| JC-H | T7JCH.RWN | Operation efficiency — work center / sequence / scheduled finish date; "A=Ask if Updating to a lower value" option |
| JC-L | T7JCL.RWN | Labor report — act start/finish date ranges; Y/N/L mode selector |
| JC-M | T7JCM.RWN | Material report — LAST.TXN.DATE (transaction date) / customer / act finish date (RTM field: LAST.TXN.DATE) |
| JC-N | T7JCN.RWN | Month-end cost report — WO Status [RCSF] (Released/Closed/Started/Finished); Thru-Last-Month-Date + Thru-Current-Month-Date boundary selectors; ISCALC.HOW_C/H/P costing method |
| JC-P | T7JCP.RWN | Print Materials in WIP — component / zero-issue / rebuild WO options |
| JC-Q | T7JCQ.RWN | WO Variance — fin product / WIP var / scrap code ranges |
| JC-R | T7JCR.RWN | WO cost as-of-date — same as Q with prior-date snapshot option |
| JC-S | T7JCS.RWN | WO cost summary by act start/finish + customer/job ranges; option "Print all Invoices for the SO associated with the WO" |
| JC-RM | T7JCRM.RWN | Java BI Report Manager — same JDBC architecture as SQLEXPORT |

WO Status codes used in JC reports: C=Complete, X=Closed, F=Finished,
R=Released, S=Started, I=In-Process (combined set from T7JCA/JCN/JCP DFMs).

**T7JCENG.RWN** is the shared calculation engine invoked by most JC reports
(displayed as "JC Engine / Processing Data / Please Wait" while computing).
Its DFM shows: Report Type, Sort/Subtotal By, Level of Detail, WO Status
(5-state filter), WO Source, Labor Type/Shift — all parameterized per calling report.

**T7JCENG DFM-confirmed Report Types** (Items.Strings): Labor Transactions /
Overhead Transactions / Labor Efficiency / Production by WC / Production by
Machine / Production by Tool / Standard Labor Hours — 7 distinct reports.
**Multiple Setup** option: Y=Include setup time once per WO/Operation (first page
only), N=include for every occurrence. Prevents double-counting setup hours
when a WO is split across pages.

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

"JO": """
## What it does

Jobs/Departments — cross-dimensional cost and revenue analytics. Unlike JC
(which groups WOs under a simple job code), JO allocates transactions across
a 4-way composite key: **Customer × Vendor × Department × Item**.

45,863 ISJOB records (all blank STATUS) serve as the reference dimension list.
T7JOANDA.RWN (1,456 KB) is the primary JO analytics program — a heavyweight
Java-integrated analytics engine (T7JOANDA.DFM caption "Java Response").

## 4-dimensional architecture (DFM-confirmed)

`t7jobs.DFM` (compact 163×278px `fsStayOnTop` filter form): vld_jcust() /
vld_jvend() / vld_jdept() / vld_jitem() — 4 dimension validators for:
- **jcust** — Customer dimension
- **jvend** — Vendor dimension
- **jdept** — Department dimension
- **jitem** — Product/Item dimension

A JO "job" is not a sequential number — it is the intersection of these four
dimensions. A transaction is assigned to JO by specifying which combination
of customer/vendor/department/item applies.

## Programs (DFM-confirmed)

| DFM | Caption | Purpose |
|-----|---------|---------|
| t7jobs.DFM | (compact filter) | Dimension filter selection — the JO selector sub-form |
| T7JOANDA.DFM | Java Response | Primary JO analytics engine (Java-integrated, 1,456 KB binary) |
| T7JODPSALES.DFM | New Screen | Java bridge launcher — Host/Port/Name/DSN settings; hint references T7Jtree.DFM (tree-based query layout) |

T7SMJO = SM KPI dashboard integration (shows JO summary in the SM module scorecard).
T7JODPSALES hint `C:\\TASPRO7\\DBA7\\T7Jtree.DFM` confirms it reuses the
T7JTREE Java tree-browsing form rather than having its own layout.

## Key tables

| Table | Records | Purpose |
|-------|--------:|---------|
| `ISJOB` | 45,863 | Job dimension master (IS_JOB_CODE/DESC/STATUS) |
| `ISJBSF` | 142 | Business scorecard metrics per job/period (143 fields) |

## Integration

- **[[module-JC|JC]]** — JC reports filter by job code; JO provides the dimensional
  analysis layer on top of JC cost data
- **[[module-SM|SM]]** — T7SMJO feeds JO summary metrics into the SM KPI dashboard

## SM-P-F — Job code maintenance (EVOHELP.PDF §SM-P-F page 491, Pass 518)
Job codes in the ISJOB table are maintained via SM-P-F Enter Jobs.
From SO-A, WO-A, and PO-A, the Job Number field supports F2 lookup into ISJOB.
Inline add: if an unknown job code is typed in any of those programs, EVO prompts
whether to add it to ISJOB immediately. Only the job code itself is required; description
and all other fields are optional.
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

## CS-A field semantics (EVOHELP.PDF §CS-A, Pass 509)

### Class (employee vs. agent)
| Code | Meaning |
|------|---------|
| E | Employee — commissions paid via internal Payroll module or ADP/CheckMark; salesperson# must match SM-G employee# |
| A | Agent (outside) — commissions paid via AP voucher to the vendor assigned in Vendor Code field; must be set up in AP-A first |

### How (commission basis)
| Code | Meaning |
|------|---------|
| G | Gross Sales — net invoice amount after line discount; excludes tax and freight |
| C | COGS — cost of goods sold at average cost at time of invoice posting |
| N | Net Profit / Gross Margin — gross sales minus COGS |
| F | FOB selling price — Bill To customer contract price (used when Ship To price includes embedded freight) |

Note: Extended Commissions only supports G or F.

### When (commission trigger)
| Code | Meaning |
|------|---------|
| I | Invoice posting — commission due immediately when SO-G posts the invoice |
| P | Customer payment — commission due when AR-C records the payment |
| A | Accrue — GL entry made at invoice post (debit Commission Expense, credit Commission Payable); but transfer to AP/Payroll not allowed until customer payment received |

### CS-D Transfer accounting
- Employee reps: updates payroll record with commission amount (or prints CheckMark manual report if using outside payroll)
- Agent reps: generates AP voucher to their vendor; converted to vendor's source currency if multi-currency
- GL treatment: commission expense is recognized at invoice post; CS-D transfer posts to Commission Payable (liability account), NOT expense — expense was already booked

### Extended Commissions (CS-G / SD-N setting)
When Extended Commissions is enabled in SD-N Sales Commission Defaults:
- Unlimited reps per order (vs. 2 in standard CS)
- Commissions assigned at line-item level by Rep + Customer + Item + Item Class combinations
- Start Date / End Date support for promotional commission periods
- CS-G stores the Rep Link records: Rep#/Customer/Item#/Item Class/Rate/Start Date/End Date

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
ES-K  Convert Production Inventory to Estimating
      → copies production item master into Estimating database (required first step)

ES-A  Enter Estimate  →  BKESTQT (header) + BKESTQTL (lines)
                         same schema as BKARINV/BKARINVL

ES-D  Quick Estimate  →  per-item cost detail entry; handles single-item or
                         edits lines of multi-line estimates from ES-A
      → 10 quantity breaks; margins from SD-G Estimating Defaults (editable per estimate)
      → RFQ optional: vendor pricing from PO RFQ system, else ES-H material costs, else Standard Cost

ES-B  Print Estimate   →  customer-facing quote (options: Notes / Hidden Notes / Kit Components /
                          Extensions / Linked Documents)
ES-C  Print Internal Estimate Sheet  →  internal cost+margin detail (BOM / Routing / Extra Charges /
                          Summary sections, multi-quantity)

ES-E  Convert          →  creates SO and/or WO
      → new items auto-added to production inventory
      → if converted to WO: uses Estimate BOM & Routing (NOT production standard)
      → if customer is a prospect only in CM, creates a customer record at conversion
```

**Estimating uses its own parallel inventory database.** Items in the Estimating DB can be production items (copied via ES-K) or new items that only exist in the Estimating DB until ES-E conversion adds them to production inventory.

**Multiple BOMs/Routings per item:** The Estimating module allows multiple BOMs and Routings for the same item number — enabling cost rollups for different configurations of the same product without affecting production standards.

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

## SR behavioral differences from SO (EVOHELP.PDF §SR, Pass 510)

### SR-A vs SO-A
- Prompts for Order or Quote at entry
- Location defaults to the Service/Repair Location defined in SD-T (IN-L-B sets Type=S for S/R locations — excludes from Available in IN-A)
- Standard pricing does NOT pull in for production part numbers
- Type N items with "Service/Repair item" flag in IN-B prompt for Make, Model, and Serial Number
- Line Number codes: **S/R** = processed via work order; **K** = deducted from inventory at invoice posting (no WO)
- Component lines can specify a different inventory Location than the S/R location

### SR-C vs SO-N (Convert to WO)
- Standard BOM and Routing do NOT pull for production items — sequences must be added manually via WO-K-A
- Alternative: define a Service/Repair template item with a routing and enter it in SD-T defaults

### SR-E Release (no equivalent in SO)
- Displays WO BOM; user selects which components to itemize on invoice
- Each component can be priced individually OR parent assembly reflects total price
- COGS entered here overrides average cost for invoice posting
- Components not flagged K are only deducted if released here

### SR-G vs SO-G
- Uses COGS entered in SR-E (not inventory average cost)
- On-hand of the repair item is NOT affected (no inventory deduction of the parent item)
- Transaction type generated = **R** (Service & Repair), not S (Shipment)
- GL posting: WIP → COGS account (not Inventory → COGS)
- Also performs WO-I Enter Finished Production and closes the associated work order in one step

## Standard Detail (T7SDET) — DFM-confirmed 2026-07-01

Service type/detail code maintenance (SD/Standard Detail subsystem).

**T7SDET.DFM** (caption "New Screen"): Type field (combo Items: **"Top"** / **"Bottom"** —
mattress-industry position codes); Add/Save/Delete/Exit toolbar.

| Table | Fields | Purpose |
|-------|--------|---------|
| `ISSDET` | 4 | Service detail codes — IS_SDET_TYPE str20 / DETAIL str20 / WHO str40 / SUB str1 |
| `ISSTYPE` | 3 | Service type master — IS_STYPE_TYPE str60 / WHO str40 / ASSET str25 |

**"Top"/"Bottom" Items:** confirm i2 Systems mattress manufacturing context — service
detail types are mattress surface positions. IS_STYPE.ASSET(str25) = asset category
link (equipment or product type being serviced). IS_SDET.SUB(str1) = sub-classification flag.

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

## PI Count Types — critical behavioral distinction (EVOHELP.PDF §PI, Pass 510)

| Type | Behavior for uncounted items |
|------|------------------------------|
| **Type 1** (partial/cycle) | Uncounted items are left unchanged — assumed to be items not in scope |
| **Type 2** (complete) | Uncounted items are zeroed out — assumes everything was counted; use for year-end |

**PI-A date caveat:** Entering a prior Freeze Date does NOT back-calculate inventory. The snapshot is always of inventory as-it-exists at the moment PI-A runs, regardless of the date field.

**PI does NOT include WIP.** PI module only counts on-hand inventory. Work-in-process inventory is obtained via JC-P Print Materials in WIP. Adjustments to WIP must be done through WO-G Issue Materials.

**PI-C new item:** If a counted item is not in the inventory master, PI-C prompts "Would you like to set it up as a new part number?" — answer Y and create it from PI-C (do NOT go to IN-B Enter Inventory instead).

**PI-C import:** Bar code scanner data can be imported as comma- or space-delimited text file. File and path must follow 8.3 naming convention (max 8-char names, no spaces). Comma-delimited: enter column number; space-delimited: enter start position + field length. Items requiring serial control cannot be imported and must be entered manually.

**PI-G cost choices:**
- **F** = Use frozen cost (cost at time of snapshot) — preferred by accountants for reconciliation
- **C** = Use current average cost — FIFO/LIFO costing always uses C (no choice)

**PI-H caveat:** Cannot delete an item in IN-B Enter Inventory while that item exists in an unposted physical inventory. Must either purge the PI or exclude the item and refreeze.

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
| `CALENDAR` | — | — | Shop calendar (alternate/older name — EVOHELP.PDF §File Names) |
| `WORKCTR` | — | 47 | Work center master (`MTWC.*` namespace) — Btrieve-only |
| `WCTRLOAD` | — | — | Work center load % (persistent; WCTRSLOD = temp for Visual Scheduler) |
| `ISWOPRIO` | — | 4 | WO priority codes with Gantt color — Btrieve-only |
| `BUCKETS` | — | — | Finite schedule buckets (capacity time-buckets for finite scheduling engine) |
| `WCCTL` | — | — | Finite scheduling temp file (cleared after each finite schedule run) |
| `WCTRSLOD` | — | — | Temp WC load % for Visual Scheduler (built by T7VSCHED Initialize step) |
| `WORKSORD` | — | — | Temp WO header for Visual Scheduler (see also WO section) |
| `WOSROUT` | — | — | Temp WO routing for Visual Scheduler (see also WO section) |
| `CALTEMP` | — | — | Temp file for generating shop calendar (SM utility) |

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
| T7VSCHED | **Visual Scheduler launcher** — WO filter: Item#/Desc/Qty/Start Date/Finish Date/WO Prefix #/WO Status [RF]/Estimate#; **Visual Scheduler Options** panel: (1) Initialize Scheduling Files and start Visual Scheduler, (2) Start Visual Scheduler to continue editing, (3) Post Visual Scheduler dates; "Creating Work Files" progress state; "Work Order Scheduler" + "Work Center Scheduler" dual views; WO Prefix# hint: "Enter the Starting WO Number with a Unique Prefix Number" |

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
| `ISLOG` | — | 9 | Active user list (WHO/WHAT/DOING/STARTD/STARTT/COMPANY/KILL/MSG/EXTRA; opened by 999 programs) |
| `ISNOTES` | 133,574 | 14 | Notes — universal note store for all EVO entities (EVOHELP.PDF: "NOTES") |
| `ISLINKS` | — | — | Links — entity-to-entity cross-reference (EVOHELP.PDF: "LINKS") |
| `ISNTYPE` | 16 | 4 | Note type codes (EVOHELP.PDF: "NOTE TYPES") |
| `ISREMIND` | — | 22 | Reminders / calendar entries (DATE/TIME/WHO/SUBJECT/CUST/VEND/ITEM/EMAIL/SENT) |
| `ISCHAINM` | 0 | 17 | Auto chain program master (EVOHELP.PDF: "AUTO CHAIN PROGRAM MASTER") |
| `ISCHAIN` | 0 | 17 | Auto chain programs (EVOHELP.PDF: "AUTO CHAIN PROGRAMS") |
| `ISSCHED` | — | — | EVO Scheduler program list (EVOHELP.PDF: "LIST OF PROGRAMS TO RUN BY EVO SCHEDULER") |
| `ISSHPVIA` | — | — | Ship via listing (EVOHELP.PDF: "SHIP VIA LISTING"; distinct from ISSHIPCO=company master) |
| `ISDLCK1` | — | — | Lock file for next-number program (prevents concurrent sequence increments) |
| `ISDLCK2` | — | — | Lock file for master default program |
| `ISDRILLM` | — | — | Master drill-down file (context-menu definitions for drill-down navigation) |
| `ISEREM` | — | — | EvoRemind notifications (system notification queue) |
| `DBAHLPID` | 2 | — | Program-specific help reference (maps program codes to help IDs) |
| `LANGDICT` | — | — | Translation master (multi-language label dictionary) |
| `MKAHIST` | 12 | 9 | System activity history log (EVOHELP.PDF: "SYSTEM DEFAULT MASTER FILE 3"; 158+ programs write audit events here — ACCT/DATE/EVENT/FORM/TRACK/SEQ/MEDIA/REM1/REM2; dual purpose: 12 config rows + audit log) |

**Btrieve-only (not in Pervasive DDF):** `BKEMP` (employee master), `BKTERM`
(payment terms legacy), `BKTAX` (tax code legacy), `BKSMSHIP` (ship-via legacy),
`CALT` (calendar), `CALSHIFT`, `BKSCHEDULE`, `BKUOM`, `BKUOMCON`

## Multi-jurisdiction sales tax (ISTAXGRP, Pass 502 2026-07-01)

`ISTAXGRP` (105 fields, 2 records at i2) defines tax groups used in AR, AP, SO, PO,
and QT. Each tax group bundles up to **9 jurisdictions** (federal, state, county, city,
special districts) with individual rates and freight rules, plus 12 taxable/non-taxable
category slots.

| Field group | Count | Meaning |
|-------------|-------|---------|
| ISIS_TXG_NAME | 1 | Tax group name (PK) |
| ISIS_TXG_DESC | 1 | Description |
| ISIS_TXG_FREIGT | 1 | Freight taxable flag (whole-group default) |
| ISIS_TXG_TOTPER | 1 | Combined tax % total (all jurisdictions) |
| ISIS_TXG_TOFPER | 1 | Combined freight tax % total |
| ISIS_TXG_OUTSTD | 1 | Outstanding balance |
| ISIS_TXG_CODE_1..9 | 9 | Jurisdiction codes (state/county/city/district slots) |
| ISIS_TXG_IDC_1..9 | 9 | Jurisdiction ID / lookup code |
| ISIS_TXG_DESCF_1..9 | 9 | Per-jurisdiction description |
| ISIS_TXG_PERCC_1..9 | 9 | Per-jurisdiction tax rate (%) |
| ISIS_TXG_PID_1..9 | 9 | Per-jurisdiction posting ID (GL account selector) |
| ISIS_TXG_TAXON_1..9 | 9 | Taxon flag per jurisdiction |
| ISIS_TXG_FRGT_1..9 | 9 | Freight taxable flag per jurisdiction |
| ISIS_TXG_COLECT_1..12 | 12 | Collection period flags |
| ISIS_TXG_TAXBLE_1..12 | 12 | Taxable-category flags (which item categories are taxable) |
| ISIS_TXG_NONTAX_1..12 | 12 | Non-taxable-category flags |

**Workflow:** Each customer and location is assigned a tax group code; when an invoice
is created the matching ISTAXGRP record is read to calculate and post the multi-line
tax breakout. The 12 TAXBLE/NONTAX slots allow category-level overrides (e.g., food
items non-taxable even in a state that taxes other goods).

**Companion table:** `ISTAXFIL` (2 records, 84 fields) — tax filing configuration
(maps each jurisdiction's collected taxes to the correct GL account for remittance).
Together ISTAXGRP+ISTAXFIL represent the full tax compliance subsystem embedded in EVO.

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

## SM-O / SM-P / SM-R–SM-U sub-programs (EVOHELP.PDF §7.2, Pass 518)

### SM-O Enter Ship Via Codes (page 489)
Code (≤15 chars) + optional company code / name / description / vendor code.
Carrier tracking: enter the carrier home page URL and a %%TRACK%% URL template
(replace the package tracking number with the literal string `%%TRACK%%`). UPS and
FedEx examples are provided. SO-I Customer Service Inquiry uses this to open a browser
and track a shipment directly from the shipments screen.

### SM-P-A Enter Categories (page 489–490)
4-char alphanumeric code + 25-char description. Used in IN-B Enter Inventory as a
user-defined filter for various reports.

### SM-P-B Enter User Defined (page 490)
25-char code + description. A second user-defined filter for IN-B / reports.

### SM-P-C / SM-P-D
SM-P-C is identical to RO-G Enter Scrap Codes.
SM-P-D is identical to RO-F Enter QC Codes.

### SM-P-E Define Inventory User Defined Fields (page 490–491)
Up to 30 UDF slots mapped to `MTIC.PROD.SUBST[2]`, `[3]`, `[4]`, or `[5]`
(each 25 chars = 100 chars total). Each UDF specifies: source field, start position,
length, label, and screen position (1–30; 3 columns of 10; 1=upper-left, 21=upper-right,
30=lower-right). Appear on IN-A/IN-B **User Defined Tab** (GUI Tab view only).
Default on first load: 4 auto-defined fields using first 10 chars of each SUBST field.
If all UDFs are deleted, the same 4 defaults reload on the next program launch.
Storage: `BKICPROD.MTIC_PROD_SUBST_2` through `_5`.

### SM-P-F Enter Jobs (page 491)
Maintains the `ISJOB` reference table used in SO-A, WO-A, and PO-A Job Number
fields. Only required field: the job code itself. All other fields optional.
Add/Edit/Delete/Print. Inline add: if an unknown job code is typed in SO-A/WO-A/PO-A,
EVO offers to add it to ISJOB on the spot.

### SM-P-G Enter WO Priority Codes (page 491)
Default codes: 1/2/3 = High/Medium/Low. Can define up to 9 numeric + 26 alpha codes.
Color assignment per code: used by SH-R Work Center Scheduler to visually differentiate
WO priorities on the schedule grid.

### SM-P-H Enter Cycle Codes (page 491)
4-char code + description + count frequency (days). Used by PI-A Capture Frozen
Inventory to filter which items are due for counting based on last-count date + frequency.

### SM-R Multi Language Maintenance (page 492)
Translation table for multi-language displays or terminology overrides. Workflow:
1. Create a language (3-char code, e.g., `SPA`).
2. Select a DFM screen to translate (e.g., `T7INAC.DFM` for IN-A Classic view).
3. Click Generate — loads all field description rows.
4. Enter translated values per language column.
Fields with no translation continue to display the original text. Storage: `LANGDICT`.

### SM-S Enter Evo Links (page 492–493)
Global Evo Links management. Types: SO / PP / Quotes / Inventory / etc. Print settings
control whether a link prints as a thumbnail on the document or as a linked page after it.
Conversion: the rightmost toolbar button (arrow icon) converts old Inventory Links to
Evo Links; after conversion it becomes an eyeglasses icon (view-only).

### SM-T Enter Java Settings (page 493–494)
JDBC connection for Java-integrated programs: SH-R Work Center Scheduler,
BM-N BOM Availability Tree, GL-R Business Status.
| Field | Notes |
|-------|-------|
| Host | Server IP or name |
| Port | Default 1583 (Pervasive Relational Engine port) |
| Name | Database name in Pervasive Control Center pointing to company subfolder |
| Destination | Folder for Java report output |
Test Settings: success shows first 10 inventory items; failure produces an error report.

### SM-U Customer Ship Via (page 494)
Per-customer carrier account numbers for third-party freight billing.
Fields: Customer Code, Ship To Code (must exist in SM-O), Priority (precedence when
multiple accounts exist), Billing Account Number, Notes, Active/Inactive, Insurance Required.

## SM-C / SM-D / SM-G / SM-H operational details (EVOHELP.PDF §7.2, Pass 521)

### SM-C Enter Item Classes (pages 463–465)
Item classes organize inventory for reports and GL posting. Every item must have a class.
**9 GL accounts per class:**
asset/expense | COGS | taxable sales | non-taxable sales | WIP |
absorbed labor | absorbed fixed OH | absorbed variable OH | absorbed material burden

If any GL account is left blank, the system uses the AD-A default. Classes only need
non-default GL accounts for exceptions. Material burden % is also per-class.
Multi-location: separate Class/Location records for per-location GL overrides.

### SM-D Enter Terms Table (pages 466–467)
Up to 99 terms types. Stored as a numbered sequence in `ISTERMS`.
**Critical rule:** The FIRST position term is the default for NSF checks, interest
charges, PR tax, and commission transfers — use a generic term like "NET 30".
**Warning:** Once orders are entered, do NOT reorder the terms table — existing records
store the terms number, not the description; reordering changes their meaning.
Fields: Term Num / Description (20 chars, prints on invoices+POs) / Disc Amt (%) /
Disc Days / Net Days / COD flag / AR/AP applicability.

### SM-G Enter Employees (pages 470–471)
4-char numeric employee number. Fields: First name / MI / Last name / Address / City /
State / Zip / Phone / Start Date / Regular Pay Rate / Overtime Pay Rate / Email / Division /
Shift / Multiple WO simultaneous clocking / Exempt from overhead burden / Photo image link.
Uses: WO labor tracking / JC job costing / DC data collection / PO receiving+inspection+approval /
email icc list / Sales Rep assignment.
Wage rates: employee rates can replace work center rates for job costing (Rate button).

### SM-H Enter Shop Calendar (pages 472–473)
Marks non-workdays (weekends, holidays, shutdowns) unlimited years forward.
**Two calendars:** (1) general system calendar (used by PO-A, WO-A date validation);
(2) SH-E finite scheduling calendar (must be generated separately from within SM-H).
Programs that use the calendar will not allow dates that fall on marked non-workdays.

## SM-J file maintenance programs (EVOHELP.PDF §7.2, Pass 521)

| Program | Purpose |
|---------|---------|
| SM-J-A | WO File Maintenance — delete blank/duplicate/orphan records; Report-only then For-real modes |
| SM-J-B | Archive Work Orders — move closed WOs to history |
| SM-J-C | Reconcile Inventory On-Hand — compare calculated vs. stored on-hand |
| SM-J-D | Consolidate Inventory Transactions — merge redundant INVTXN records |
| SM-J-E | Purge Work Orders — permanently delete old WO records |
| SM-J-F | Purge Purchase Order History |
| SM-J-G | Purge QC Receipts |
| SM-J-H | Purge Data Collection File |
| SM-J-I | Purge Estimates |
| SM-J-J | Archive or Purge Closed Sales Orders |
| SM-J-K | Purge or Archive Invoice History |
| SM-J-L | **Change Part Numbers** — renames an item number across ALL system files (including history); can merge two item numbers |
| SM-J-M | **Change Customer Codes** — renames a customer code across ALL files (including history); can merge |
| SM-J-N | **Change Vendor Codes** — renames a vendor code across ALL files (including history); can merge |
| SM-J-O | Rebuild Customer/Vendor Credit Info |
| SM-J-P | Purge/Archive Service/RMA Orders |
| SM-J-Q | BOM Recursion Utility — detect/fix circular BOM references |
| SM-J-R | Archive Purchase Orders |

**Key warning for SM-J-L/M/N:** These operations change HISTORY files as well as master
files. Use only during startup or under controlled renumbering projects.
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

## AD-A — General Ledger Defaults (Pass 498, Acctug.pdf ch. 11)

Controls system-wide GL behavior and supplies every module's default account codes.

**Control flags** (4 Y/N posting-on/off toggles):
| Field | Meaning |
|-------|---------|
| Post COGS Transactions? | N = suppress automatic SO invoice → COGS posting |
| Post PO Transactions? | N = suppress automatic PO receipt → Inventory posting |
| Post Inventory Adjustments? | N = suppress IN-A adj → GL posting |
| Post WO Transactions? | N = suppress WO cost → WIP/Inventory posting |
| Permit use of Item Class GLs? | Y = allow SM-C item-class level GL overrides |

**System counters:**
- `Fiscal Year Start Dt` — calendar start date; auto-updated by AM-B (never change manually)
- `Next Genl Journal No` — next GL-B batch number

**Accounting & Sales GL accounts** (first screen):
| Account | Type | Purpose |
|---------|------|---------|
| Current Earnings | O (OE) | Net income/loss for current fiscal year; zeroed to Retained Earnings at AM-B |
| Retained Earnings | O (OE) | Accumulated prior-year earnings |
| Clearing Account | O (OE) | Catch-all when GL code not found during posting; recommended 99999 |
| Accounts Payable | L | AP control account |
| AP Discounts Taken | E or I | Vendor early-pay discounts |
| Accounts Receivable | A | AR control account |
| AR Discounts Taken | I or E | Customer early-pay discounts |
| AR Interest Charged | I | Overdue invoice interest income |
| AR Customer Deposits | L | Prepayments (separate from AR; applied later via AR-C/AR-N) |
| Taxable Sales | I | Revenue from taxable items (can override per item class in SM-C) |
| Non-Taxable Sales | I | Revenue from non-taxable items (can override per item class in SM-C) |
| Invoice Freight Out | I or contra-E | Freight billed to customers on SO invoices |
| Sales Tax Withheld | L | Sales taxes collected; can use separate account per tax authority |
| Retention | A | Holds retention billing amounts until retention SO is posted |
| Agents Commissions Payable | L | Credited when invoices/payments include agent commissions; cleared by CS-D |
| Agents Commission Expense | E | Debited when agent commissions are recorded |

**Manufacturing GL accounts** (second screen — "Mfg GL Accounts" button):
| Account | Type | Posted when |
|---------|------|-------------|
| Inventory | A | PO receipt; WO completion transfer from WIP |
| Cost-of-Goods-Sold | E | SO invoice posted (can override per item class) |
| Absorbed Freight In | (contra-A) | IN-B Freight Pct absorption — credit side; debit → Inventory asset |
| POs Received not Invoiced | L | PO receipt (credit); cleared at AP invoice entry (debit) |
| PO Freight In | E | Vendor freight on PO invoices |
| PO Sales Tax Expense | E | Tax charged on PO invoices |
| Extra Costs (WO) | E | WO extra costs: credit Extra Costs, debit WIP; reversed at AP voucher |
| Miscellaneous Costs (WO) | E | WO routing misc costs (tooling etc.): same credit/debit pattern as Extra Costs |
| Absorbed Labor | E (credit) | Labor reported on WO: cancels actual direct labor expense; ideally nets to zero |
| Labor Variance | E | Difference between actual direct labor and absorbed labor; adjust at month-end |
| Absorbed Fixed Overhead | E (credit) | Fixed OH absorbed as % of labor: cancels actual fixed OH expense |
| Fixed Overhead Variance | E | Difference between actual fixed OH and absorbed fixed OH |
| Absorbed Variable Overhead | E (credit) | Variable OH absorbed as % of labor: cancels actual variable OH expense |
| Variable Overhead Variance | E | Difference between actual variable OH and absorbed variable OH |
| WIP Inventory | A | All WO costs (material/labor/OH) debited here; credited at WO completion |
| WIP Variance | E | Adjusted at month-end by variance entries; also posted when WOs close with residual |

## AD-B — Checking Accounts Defaults (Pass 498, Acctug.pdf ch. 11)

Up to 9 checking accounts. Three are designated as defaults for AR deposits, AP checks, and Payroll.

| Field | Meaning |
|-------|---------|
| AR (default bank #) | Which of the 9 accounts receives AR deposits |
| AP (default bank #) | Which of the 9 accounts issues AP checks |
| PR (default bank #) | Which of the 9 accounts issues payroll checks |
| AP Checks Print Format # | 1/2/4/5 = graphical laser/continuous; 3 = text dot-matrix |
| Account Name | Display label (appears in lookup windows throughout system) |
| GL Account-Dept | Cash account code for this checking account (usually asset, sometimes liability for CC) |
| Balance | Period-ending balance; auto-updated by GL-J (Reconcile Check Register) |
| Next Ck # | Next check number to be assigned; auto-increments each print run |

## AD-C — Accounts Payable Defaults (Pass 498, Acctug.pdf ch. 11)

| Field | Meaning |
|-------|---------|
| Next AP Invoice Number | Auto-assigned when payroll/sales taxes transferred to AP |
| Next Recurring AP Number | Incremented each time a new AP-O recurring voucher template is created |
| Aging Periods 1–5 | Day thresholds for AP-I aging report buckets; Period 1 should always be 0 |

## Integration

- **[[module-GL|GL]]** — AD-A sets the default posting period, account numbering, and COA structure
- **[[module-AP|AP]]** — AD-C sets terms, default vendor GL accounts, and check format
- **[[module-AR|AR]]** — AD-A AR accounts (deposits, discounts, interest) used by all AR posting
- **[[module-CS|CS]]** — AD-A Agents Commissions accounts used when CS-D transfers commissions
- **[[module-WO|WO]]** — AD-A manufacturing GL accounts (WIP/Absorbed Labor/OH) drive all WO cost postings
- **[[module-PO|PO]]** — AD-A PO GL accounts (Received-not-Invoiced, Freight In) used at receipt/invoice
- **[[module-SO|SO]]** — AD-A COGS/Sales accounts used at invoice posting
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

## Workflow triggers (EVOHELP.PDF §LC, Pass 509)

Lot numbers are required at these transaction points when an item has Lot Control = Y:
- **PO-C Receive POs** — lot assigned at receipt; if received to QC (Q), prompt deferred until PO-J-C buyoff
- **WO-G Issue Materials** — cursor stops at Qty field; prompted for lot number per component
- **WO-I Enter Finished Production** — parent assembly lot assigned here if parent is lot-controlled
- **IN-C Enter Inventory Adjustments** — one adjustment per lot (use instead of IN-K for lot items)
- **IN-K Adjust Physical Levels** — warns if changed; better to use IN-C for lot items
- **SO-A Enter Sales Orders** — optional pre-assignment (requires SD-M Setup II: "Ask for Lot info when adding SO Lines" = Y)
- **SO-E Release Sales Orders** — if not pre-assigned, prompts here
- **SO-G Post Invoices** — final check; if still unassigned, prompts during post

Creating a lot manually in LC-A is not recommended — it does not update INVTXN or GL detail.

## LC-D transaction type codes (EVOHELP.PDF §LC-D, Pass 509)

| Code | Transaction type |
|------|-----------------|
| A | Adjustments (IN-C, IN-K, or Physical Inventory) |
| B | Bin Location Transfers |
| C | PO Price Change entered in AP-C (**not tracked by Lot Number**) |
| G | Scrap |
| I | Stock issues to work-in-process |
| J | Purchase order receipts to work-in-process |
| M | Make-From Component Issue |
| O | Outside Processing (Service) PO Receipt to Work Order (**not tracked by Lot Number**) |
| P | Purchase order receipts to stock |
| Q | Purchase Receipt to QC |
| R | Service & Repair |
| S | Shipments |
| T | Warehouse Transfer |
| W | Work order receipts to stock |

Note: C and O are not tracked by lot number; they appear in inventory but cannot be filtered by lot in LC-D.

## LC-E exception filters (EVOHELP.PDF §LC-E, Pass 509)

| Filter | Meaning |
|--------|---------|
| Exceptions Only | Total inventory on-hand does not equal sum of all lot quantities |
| Negative Lot UOH | Individual lot records with negative on-hand |
| Orphan Lots | Lots assigned to item numbers that no longer exist |
| Summary or Detail | Print line per item vs. line per lot number |
| Sub Sort by Lot or Exp Date | Controls secondary sort within item |

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

## Workflow triggers (EVOHELP.PDF §SC, Pass 509)

Serial numbers are required (one per unit) at these transaction points when an item has Serial Control = Y:
- **PO-C Receive POs** — serial assigned per unit received; if received to QC, deferred until PO-J-C buyoff
- **WO-G Issue Materials** — serial required for each unit issued; Auto Generate button uses SC-G parameters
- **WO-I Enter Finished Production** — serial assigned per unit completed
- **IN-C Enter Inventory Adjustments** — one serial per unit adjusted
- **IN-K Adjust Physical Levels** — warns if changed; IN-C preferred for serial items
- **SO-A Enter Sales Orders** — optional pre-assignment (requires SD-M Setup II: "Ask for Serial info when adding SO Lines" = Y); F2 lookup shows available serial numbers for the item
- **SO-E Release Sales Orders** — prompts if not pre-assigned
- **SO-G Post Invoices** — final check; prompts if still unassigned during post

Creating a serial record manually in SC-A is not recommended — it does not update INVTXN or GL detail.

## SC-D transaction type codes (EVOHELP.PDF §SC-D, Pass 509)

Identical to LC-D codes: A=Adjustments / B=Bin Transfer / C=PO Price Change (not by serial) / G=Scrap / I=WIP issue / J=PO receipt to WIP / M=Make-From / O=Outside Processing (not by serial) / P=PO receipt to stock / Q=PO Receipt to QC / R=Service & Repair / S=Shipments / T=Warehouse Transfer / W=WO receipts to stock.

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
| RO-J-A | Print Routings — Item#/WO# range; **Master or WO Routing [M/W]** | T7ROJA |
| RO-J-B | Print Work Centers — WC range / Dept range | T7ROJB |
| RO-J-C | Print Machines — Machine range / Last Maintenance Date range | T7ROJC |
| RO-J-D | Print Tools — Tool range / Last Maintenance / **Active+Inactive+Both [AIB]** | T7ROJD |
| RO-J-E | Print QC Codes — QC Code From/Thru | T7ROJE |
| RO-J-F | Print Scrap Codes — Scrap Code From/Thru | T7ROJF |
| RO-J-G | Print Departments — Dept Code From/Thru | T7ROJG |
| RO-J-H | Print Operation Types — WC range / Operation range / **Type [A/L/P]** (All/Labor/Purchase) | T7ROJH |
| RO-K | Enter Routing Templates — Template Number / Add/Insert/Delete | T7ROK |
| RO-L | Enter Routing Specs / QC Link — Item#/Sequence#/**Print on Shop Traveler** flag | T7ROL |
| RO-M | Enter Testing Method | t7qcmthd.rwn |
| RO-N | Enter Testing Requirements | t7qcspec.rwn |
| RO-O | Routings Defaults | T7DSRO.RWN |
| RO-P | Update Routing Standard from Receipts — Received Date range / Item# range / **Update Vendor+Cost+Both [V/C/B]** / Limit to Sequence | T7ROP |
| RO-Q | Work Center Rename (CSV import) — Old WC → New WC / New Description | T7ROQ |

## DFM-confirmed operation details (25 DFMs)

**RO-A (T7ROA.DFM):** Cycle Time Threshold (In Seconds) — sets a threshold for flagging exceeded cycle times; columns: RUN/SETUP/Sequence/Oper/Type/Description/Work Center/Rout#/Line/Processes#/Time per Part. Sub-forms:
- **t7roacpy** — "Copy Existing Routing": Part/Desc/Est# + Copy From direction toggle (**Production ↔ Estimates**)
- **T7ROASpecs** — "Enter Routing Specs": Item#/Sequence/spec grid (Current Line/Total Lines)
- **T7ROAOpts** — column display toggle panel

**RO-C (T7ROC.DFM):** Global change to outside processing settings — selects which fields to change (Outside Processing WC / Lead Time / Min Charge / Vendor Cost / Unit Cost) across routing records. Batch update tool.

**RO-D (T7ROD.DFM):** Machine master: Machine/Work Center/Hours between Service/Last Service Date/Hours Used/Notes/Reason/Active flag; **Trim Size X/Trim Size Y** — confirms cutting machine support (foam/fabric material dimensions).

**RO-E (T7ROE.DFM):** Tool/mold master: Weight/Height/Width/Depth/Ejector Stroke/Nozzle Radius/Tool Type 1/Hot Runners Channel/#Water Ports/Water Temp Side A/Water Temp Side B/Shot Size/Min Tonnage Required — **injection mold tooling fields** confirm i2 Systems works with plastic injection molding or tooling components.

**T7ROUTWO.DFM** — "Select WOROUT/ROUTING" — shared sub-form that lets the user choose between a WO-specific routing (WOROUT) and the master routing (ROUTING) when both exist.

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

## RO-A Enter Routings — field semantics (EVOHELP.PDF §RO-A, Pass 508)

### Header fields
| Field | Notes |
|-------|-------|
| Item# | Part number being routed; must exist in item master |
| Rt# (Routing Number) | Default 1; each distinct Rt# prints a separate shop traveler on WO release |
| Description | Auto-filled from item master; read-only display |

### Line (operation) fields
| Field | Notes |
|-------|-------|
| Seq | Sequence number (e.g., 10, 20, 30); determines traveler print order |
| Oper | Operation code; must exist in RO-I operation templates if templates are used |
| Type | Sequence Type: **R** = always Run Time; **S** = always Setup; blank = either (most common) |
| Description | Free-text operation description; prints on shop traveler |
| Work Center | Must exist in RO-C work center master |
| Rout# | Routing number for this line; links to multi-routing travelers |
| Processes# | Number of simultaneous processes per operation; enables Time/Process, Processes/Hr, Multiply/Divide sub-fields |
| Time per Part | Run time per unit produced (HH:MM:SS or decimal hours); mutually calculated with Parts/Hr |
| Parts/Hr | Throughput rate; mutually calculated with Time per Part |
| Setup | Setup time in HH:MM:SS |
| Decimal Time | Use for >99 hours or sub-second precision |
| Forward Overlap | Hours after this sequence completes before parts move to the next (e.g., paint drying time) |
| Backward Overlap | Number of parts produced at this sequence before the next sequence can begin (enables parallel/simultaneous ops) |
| Std Time? | Y = auto-applies standard time when parts are reported — for operations impossible to track individually |
| #Persons | Number of people assigned; 2 decimal places; used in direct-labor cost calculations |
| Mach | Machine number; must exist in RO-D machine master |
| Tool | Tool number; must exist in RO-E tool master |
| Line | Optional sort key; determines order on shop traveler and routing reports |

### Time/Processes sub-fields (visible when Processes# > 1)
| Field | Notes |
|-------|-------|
| Time/Process | Time per individual process within the operation |
| Processes/Hr | Throughput in processes per hour |
| Multiply/Divide | Controls whether #Proc multiplies or divides the total time calculation |

### Lines/Components-driven time (Time Type field)
| Code | Meaning |
|------|---------|
| blank / F | Flat time — fixed time regardless of BOM complexity |
| L | BOM Lines-driven — time scales with number of BOM lines (e.g., assembly steps) |
| C | Components-driven — time scales with total component count |

### Outside processing fields (visible when Work Center is flagged as outside processing)
| Field | Notes |
|-------|-------|
| Vend | Vendor code; required for outside processing (or use a dummy vendor) |
| Cost | Per-unit outside processing cost; if WC has a Cost/lb default, prompts for weight × cost |
| Min Charge | Minimum charge for the operation; cost rollup uses max(qty x Cost, Min Charge) |
| LT | Outside processing lead time in days; auto-fills from work center default |

### Text fields
| Field | Notes |
|-------|-------|
| Notes | Free-form text, unlimited lines; prints on shop traveler; for outside processing, content also auto-populates the PO line notes |
| Specs | Structured specification fields with predetermined headings; for industry-specific process parameters (e.g., temperature, pressure, material grade) |
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

## SD-S master WC settings (EVOHELP.PDF §WC, Pass 510)

Three SD-S Warehouse Control Defaults settings control all WC behavior:

| Setting | Options |
|---------|---------|
| **Master WC switch** | N = 1 bin per item only; Y = multiple bins tracked but on-hand qty NOT maintained per bin; Q = qty by bin IS maintained per bin |
| **Use Controlled Bin Locations** | Y = bins must exist in master list (WC-A); N = users can create bins on-the-fly |
| **Allow Blank Bin Locations** | Y = items can be assigned to a blank bin; N = all bins must be named |

When WC is first enabled, each item's existing Bin field from IN-B Enter Inventory is automatically assigned as the default bin for that item.

Transaction behavior: For WC=Y transactions prompt for bin but do not control qty by bin. For WC=Q all transactions prompt for bin AND quantity split.

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

Quotations / Service Quotes — two separate sub-areas:

1. **Standard Quotes (alias for ES):** The QT code points to the
   [[module-ES|ES]] Estimates module. Quotes (estimates) are entered and managed
   via the ES menu (ES-A through ES-E). Tables: `BKESTQT` (6,897 active quotes),
   `BKESTQTL` (462,837 lines) — byte-for-byte clones of `BKARINV`/`BKARINVL`.

2. **Service Quote UDFs (T7QTINFO):** A dedicated UDF extension form for service
   quotes — "Quote Misc. Information" (note: caption has typo "Infromation"). Provides
   20 user-defined fields attached to a service quote record.

## DFM-confirmed details

**T7QTINFO (Quote Misc. Information):** UDF panel for service quote orders —
5 date fields (`qtDate1`–`qtDate5`) and 15 alpha fields (`qtAlpha1`–`qtAlpha15`),
plus Save/Exit toolbar. Stored in `ISQTINFO` (54 fields; mirrors the
`ISSR_INFO_*` UDF clone pattern used by SR orders). Program: 42 procs,
`LISTG60.LIB`, 39 tables (includes `BKBMMSTR`, `BKAPINVL`, `BKAPPO`,
`ISTAXGRP`, `BKARINVV` for GL distribution).

**ISSR.INFO.\* access namespace (30-var, from T7QTINFO var-confirm):**
SRNUM/UID/CODE/DATE/ALPHA/EXTRA + DATE1–5 (5 UDF date slots) +
AL1–20 (20 alpha UDF slots).

**Note:** The `qtDate`/`qtAlpha` DFM field names differ from the underlying
`ISSR.INFO.DATE*`/`AL*` namespace — the DFM labels are display-layer aliases.
The "BADGER.TRUCK" var in T7QTINFO confirms i2-specific customization
(Badger Truck is a customer with custom service quote fields).

## Integration

- **[[module-ES|ES]]** — standard quote entry and management
- **[[module-SR|SR]]** — T7SRINFO provides the same UDF pattern for S&R orders
  (5 date + 17 alpha); QT uses a parallel form for service quotes
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

## DFM-confirmed details

**T7RFQ.DFM (caption "New Screen"):** Two-panel view — Pending (items needing
quotes) and RFQ (items with active quotes). Grid columns: LIST.PART /
LIST.DESC / LIST.QTY / LIST.VEND / LIST.STDCST / LIST.STATUS / LIST.TAG.
Actions: Tag Individual / Tag Groups / Process / Exit. The tag-based workflow
lets buyers select items individually or by group before processing them into
RFQ requests.

## PO-E/F/G workflow details (EVOHELP.PDF §PO-E/F/G pages 127-132, Pass 514)

### PO-E — Enter/Print RFQ's

Identical entry flow to PO-A Enter Purchase Orders, **except prices are not entered**.
RFQ numbers use a **separate numbering sequence** from POs. Leave RFQ# blank → system assigns next available on save.

**As template PO:** Enter a standing RFQ with typical vendor items and no quantities. To order,
open the RFQ, enter quantities on specific items, then PO-G converts only items with quantities to a live PO, optionally clearing quantities afterward for reuse.

**Copy function:** From the header, press Home (or click Copy RFQ) → enter target vendor code.
System creates a new RFQ with a new number, identical content except vendor fields. Can chain: copy → copy → copy for mass multi-vendor RFQ distribution.

**Printing:** On save, prompted to print. Also available any time via F3 (Print button) on a blank screen — prints all unprinted RFQs or a specified range; can include linked documents.

### PO-F — Enter Verbal RFQ's

Single-item verbal quote recorder — used when dealing with frequent subcontractor price calls.

**Header fields:**
| Field | Notes |
|-------|-------|
| RFQ Number | Auto-assigned or manual |
| Issue Date | Defaults to today |
| Vendor | Must be valid in vendor file |
| Estimate# | Optional; ties quote to an ES estimate for cost calculation |
| WO# | Optional; associates with a specific work order |
| Sequence | Routing sequence if RFQ is for a service (skips item# entry) |
| Item# | Must be valid in inventory; pulls Desc/Purch UM/Conv Factor/Lead Time |
| Use in Est? | Y = use this RFQ's prices in the estimate's cost calculation (only one RFQ per item can have Y) |
| Exp Date | **Required** — marks when quote expires; used by PO-I-C RFQ Status to separate current from expired |
| Qty 1-5 / Cost 1-5 | Up to 5 quantity-break price tiers (e.g., 1-99 → $10.00; 100-199 → $7.50) |

### PO-G — Convert RFQ's

Converts an RFQ (either PO-E or PO-F style) to a live purchase order.

**Fields:**
| Field | Notes |
|-------|-------|
| Quote Number | RFQ to convert |
| P/O Number | Next available PO# displayed; can override |
| Order Date | Defaults to today |
| Est Receipt Date | Applied to all line items (individual dates must be changed in PO-A afterward) |
| WO# | Optional tie to a work order if not already on the RFQ |
| Transfer Notes | Y/N — copy RFQ notes to the new PO |
| Stay on File? | Keep RFQ after conversion (can convert again); or purge |
| Convert qty'd items only | Only lines with quantities are converted; optionally clears quantities for template reuse |

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

## T7RTMVALID — dual role: RTM selector AND license validator (Pass 520)

`T7RTMVALID.RWN` serves two entirely separate roles:

**Role 1 — RTM format name selector** (invoked before printing)
- DFM caption: "Select Report Format Name"
- Field: RTM file name input
- Buttons: Ok / Cancel / Settings
- Validates that the named RTM file exists before the report runs

**Role 2 — Runtime license validator** (invoked at EVO startup)
- Library: `NZLICE.LIB`
- Reads `ISIS` table (4-table DB: BKSYHELP / DBAHLPID / ISIS / MKAHIST)
- Reads 12 module gate flags from ISIS: TAX / TAX.IN / TAX.FRM / TAX.PO /
  MULTI.CURR / MULTI.CPAY / LANDED.COS / UPC / RETAIL.PRI / COMM.PRICE /
  IMAGING / AUTO.TAX
- Sets 21 system-wide IS.* license flags used by all other programs:
  IS.TAX / MULTI.CURR / LANDED.COST / UPC / RETAIL.PRICE / COMM.PRICE /
  IMAGING / UPC.1 / MULTI.CPAY / PIC.PATH / TAX.FRM / PO.TAX / TAX.IN /
  TAX.CVT / CUR.CVT / AUTO.TAX.CAL / EZPAY / RMA / SPEC.SUP / SPEC.SUPF / SPEC.SUPT
- Concurrent user enforcement: USERS / USBUFF
- Serial key obfuscation: SCBUFF / SER5 / SER6
- Logs validation to MKAHIST (activity audit trail)
- IS.DEMO flag: if set, all programs run in demo/evaluation mode
""",

"TA": """
## What it does

Tools / Admin Utilities — the EVO system maintenance and administration module.
Covers data backup/restore, software update application, data purging, company
setup, and system-wide configuration tasks.

## Menu operations (Pass 494, BKMENUSU.TXT-confirmed)

"TAS" group in BKMENUSU.DBF = System Configuration. `.INT` entries are TAS Pro
built-in intrinsic commands (part of tp7runtime.exe, not separate files).

| Code | Description | Program | Type |
|------|-------------|---------|------|
| TA-A | Run TAS Program | RUNPRG.INT | intrinsic |
| TA-B | Change Company Code | GETCO.INT | intrinsic |
| TA-C | Set Configuration | CONFIG.INT | intrinsic |
| TA-D | Maintain Database | WTASDATAM.RWN | RWN |
| TA-E | Initialize Database | WTASINIT.RWN | RWN |
| TA-F | Maintain Location File | WTASFLOC.RWN | RWN |
| TA-G | Maintain Menu Access Records | WBKMENUSETUP.RWN | RWN |
| TA-H | Maint Menu Access - End User | WBKMENUSUEU.RWN | RWN |
| TA-I | Update File Structures | WTASMERGE.RWN | RWN |
| TA-M | RTM Editor | REPORTS.INT | intrinsic |
| TA-N | Program Scheduler | evoscheduler.rwn | RWN |
| TA-O | Backup Utility | EvoERPbackup.rwn | RWN |
| TA-P | Change Password | PASSWORD.INT | intrinsic |
| TA-Q | Change Logo Image | Evologo.rwn | RWN |
| TA-R | SQL Editor | **T7JSQL.RWN** | RWN |
| TA-S | Data Dictionary Check | T7DDCHECK.RWN | RWN |

**Note on TA-R:** Prior documentation incorrectly identified TA-R as QUERYEXECUTE.
BKMENUSU.TXT confirms TA-R = T7JSQL.RWN ("SQL Editor"). QUERYEXECUTE is
QU-F ("Query Executor") under the Queries menu — a completely different program.

**Note on TA-M (RTM Editor):** Prior doc said this invokes an external program.
BKMENUSU.TXT confirms it is REPORTS.INT — a TAS Pro built-in intrinsic command,
not a separate file.

## Key concepts

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
| WTASFLOC | **"Maintain File Names and Locations"** — File Name, Extension, FD Name, Rec Type, Path, Description, Delete File, Update All (this is the FL module) |
| WTASINIT | **"Addsum TAS Professional 7 Create/Initialize File Program"** — File Name, Extension, FD Name, Rec Type, Path, Description, Initialize button |
| WTASDMGR2 | **"New FD"** — Enter the new FD Name (sub-dialog of WTASDMGR) |
| WTASDMGR3 | **"Restructure a file"** — FD to restructure, files/records remaining counter |
| WTASDMS2 | **"Enter Array Elements"** — array field value editor |
| WTASDMS3 | **"Edit Memo Field"** — memo text editor (generic popup for long fields) |
| WTASDMS4 | **"Enter Filter Expression"** — Btrieve filter expression entry |
| WTASDMS5 | **"Enter Find Next Expression"** — search within current record set |
| WTASCHKINT | **"DataScanIntegrity utility"** — Total/Current Scan Progress, Scan Type, Records Scanned, Current file/key, Start scan; sub-dialog: "Include which companies" (Current/All) |

WTASDATAM ("Maintain Database") fields: Sort by, file name, "Search for dates in the
format YYYYMMDD", Sequential (no key) mode, Edit, Save row, Add row, Delete, Choose
fields to display, Override file location path, Deleted records counter. This is a
general-purpose low-level Btrieve record editor — the TAS Pro admin power tool.

**Key finding:** WTASDMGR is the full Addsum TAS Premier 7i data dictionary editor —
confirms runtime is "TAS Premier 7i" (not just "TAS Pro 7"). DDD managed via GUI with
Fields/Keys tabs, key properties (Modifiable/Allow duplicates/Ignore Case/Clear segment
field num), Export visible rows, and New/Edit/Delete field capability.

## Security and session tables (Pass 496, EVO3.JAR)

### BKLOGON — Active user session (10 fields)

One row per currently logged-in user. Controls concurrent-login prevention and
stores the active session state.

| Field | Notes |
|-------|-------|
| BKLOGON_CODE | User login code (primary key) |
| BKLOGON_PSWD | Password (stored for session auth) |
| BKLOGON_CMPY | Company code currently active (set by TA-B Change Company) |
| BKLOGON_MENU | Current top-level menu group |
| BKLOGON_SUBMENU | Current submenu position |
| BKLOGON_PROG | Program file currently running |
| BKLOGON_PRINTER | Default printer for this session |
| BKLOGON_CURPRT | Currently active printer (may differ from default) |
| BKLOGON_SCRTY | Security level code (FK to BKSLEVEL.BKSL_LEVEL) |
| BKLOGON_INUSE | In-use flag — set on login, cleared on logout; prevents duplicate logins |

BKLOGON_INUSE is the concurrency lock. BKLOGON_SCRTY → BKSLEVEL determines which
menus the user can see.

### BKSLEVEL — Security access matrix (422 fields)

Stores per-security-level menu access control. One row per defined security level.
The 422 fields break down as:

- `BKSL_LEVEL` — the security level code (e.g., "ADMIN", "USER1")
- `BKSL_MENU` — associated menu group identifier
- `BKSL_MENU{n}_YN` (n = 1–20) — whether menu group n is accessible at all (Y/N)
- `BKSL_MENU{n}_{k}` (n = 1–20, k = 1–20) — whether item k within menu group n is
  accessible (Y/N)

Math: 2 + (20 × 21) = 2 + 420 = 422 fields exactly.

The 20 menu groups map to the MENUFILE/BKMENUSU menu group definitions. Each group
has up to 20 individual menu operations. This is EvoERP's entire menu-based access
control system stored as a single denormalized row per security level.

**Relationship:** BKLOGON.BKLOGON_SCRTY → BKSLEVEL.BKSL_LEVEL → 20 menu groups each
with up to 20 item flags → MENUFILE.MENU_CODE → MENUFILE.MENU_PROG_n (the .RWN to run)

### MENUFILE — Runtime menu definition (108 fields)

The in-memory/database representation of the EVO menu system, loaded from
BKMENUSU.DBF at runtime.

| Field group | Count | Notes |
|-------------|-------|-------|
| MENU_CODE | 1 | Menu group code (e.g., "AP", "SO") |
| MENU_TITLE | 1 | Display title for the menu group |
| MENU_ESCAPE | 1 | Escape key binding |
| MENU_LEFT, MENU_RIGHT | 2 | Horizontal boundaries |
| MENU_WIDTH | 1 | Menu window width |
| MENU_LL_COL, MENU_LL_ROW | 2 | Lower-left display position |
| MENU_NAMES_1-20 | 20 | Display label for each of up to 20 items |
| MENU_PROG_1-20 | 20 | Program file (.RWN/.INT) for each item |
| MENU_LINES_1-20 | 20 | Display line number for each item |
| MENU_OPTIONS_1-20 | 20 | Option flags for each item |
| MENU_TYPES_1-20 | 20 | Type code for each item |

108 = 8 header fields + 5 × 20 per-item arrays. The MENU_PROG_n fields are the exact
.RWN filenames that BKMENUSU.TXT confirms (e.g., `T7JSQL.RWN`, `queryexecute.rwn`).

MENUFILE ties the three security layers together:
`BKLOGON` (session) → `BKSLEVEL` (access matrix) → `MENUFILE` (menu definition) →
`MENU_PROG_n` (program to launch)

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

## Menu infrastructure — WBKMEN*.DFM (8 DFMs confirmed)

The EvoERP menu system is implemented via a "Workbook Menu" subsystem. Admin forms:

| DFM | Purpose |
|-----|---------|
| WBKMENU_LOGIN.DFM | Login form (dynamic, no static caption) |
| WBKMENUSETUP.DFM | **Menu Item Setup** — Groups/Buttons, Menu Lines, New Menu, Existing Menu Items; Add/Edit/Delete User; Add Group; Update to Latest Prg; Change Prg Name |
| WBKMENUSUCPRG.DFM | **Change Program Name** — old vs new program name mapping |
| wbkmenusueu.dfm | **Per-user access** — Menu Item Setup with Access Code field |
| WBKMENUSUMVEBTN.DFM | Move Button between groups |
| WBKMENUSUNEWAC.DFM | **Enter New Access Code** — New Menu Access Code, Copy From (inherit another user's menu) |
| WBKMENUBUTT.DFM | Button selector |
| WBKMENUPICS.DFM | Image/icon selector |

These allow SY/SM admins to customize which programs appear in which menu groups for
each user or access-code group, and to remap program names when RWN files are renamed.

## Key table: BKSYMSTR (286 fields, 1 row — global system defaults)

Set via SM (System Maintenance). One row stores all company-wide defaults:

| Field group | Examples | Purpose |
|-------------|----------|---------|
| **Company** | `BKSY_COMP_NAME`, `BKSY_COMP_ADD1/2/CSZ` | Company name and address |
| **AR GL** | `BKSY_AR_GLACT=1200`, `BKSY_AR_DISCGL=4004 dept1`, `BKSY_AR_FREIGHT=8517 dept4` | AR receivables, discount, freight GL defaults |
| **AP GL** | `BKSY_AP_GLACT=2110`, `BKSY_AP_DISCGL=5100 dept1` | AP payables, discount GL defaults |
| **PO GL** | `BKSY_PO_FREIGHT=5102 dept0250`, `BKSY_PO_RNI=2137`, `BKSY_PO_TAXGL=8805` | PO freight, received-not-invoiced, tax GL |
| **GL** | `BKSY_GL_CLRING=9999`, `BKSY_GL_RETEARN=9999`, `BKSY_GL_ARINTR=9999`, `BKSY_GL_RELYR=3200` | GL clearing, retained earnings, AR interest, prior-year |
| **Tax** | `BKSY_TAX_RATE=0`, `BKSY_TAX_GLACT=9999` | Default tax rate and GL account |
| **Aging** | `BKSY_AR_AGING_1-5=0/30/60/90/120`, `BKSY_AP_AGING_1-5=0/30/60/90/120` | AR/AP aging bucket day thresholds |
| **Terms** | `BKSY_TERMS_1-20`, `BKSY_TRM_AMT/DAY/TYP/EOM/MAX/DISC_1-20` | 20 payment terms slots (description + amount/day/type/EOM/max/disc) |
| **Check register** | `BKSY_CHK_NUM/BAL/NAME/CHKACT/CHKDPT/CHKCUR_1-9` | 9 bank accounts (next check#, balance, name, GL acct/dept, currency) |
| **Counters** | `BKSY_ARINV_NUM=0`, `BKSY_APINV_NUM=0`, `BKSY_APPO_NUM=0`, `BKSY_GJ_NUM=0` | Next AR invoice, AP invoice, AP PO, GJ number |
| **Fiscal** | `BKSY_FISCAL_YR=01/01/2026` | Fiscal year start date |
| **AR defaults** | `BKSY_AR_SLSP`, `BKSY_AR_ENTBY`, `BKSY_AR_TAXABL`, `BKSY_AR_PEL` | Default salesperson, entered-by, taxable flag |
| **AR interest** | `BKSY_AR_INT_RTE=1.5`, `BKSY_AR_INT_DAY=1` | Finance charge rate (1.5%), grace days (1) |
| **Print flags** | `BKSY_PLAIN_INV/PO/STMT/CHKS` | Y/N whether to use plain-paper forms |
| **AP end desc** | `BKSY_AP_ENDDESC_1-5` | Default AP invoice end-of-description lines |

Live values (i2 Systems, 2026-07-01): AR GL=1200, AP GL=2110, freight(AR)=8517/dept4,
freight(PO)=5102/dept0250, AR interest=1.5%/1-day, aging=0/30/60/90/120, fiscal=2026-01-01.
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

## SU-A UDF (User Defined Functions) mechanism (EVOHELP.PDF §SU-A, Pass 507)

SU-A grid columns can include **calculated or cross-file values** via UDF scripts:

- UDF scripts are TAS Pro source files named `UDF1.SRC`, `UDF2.SRC`, etc.
- Referenced on the grid column as data field name `UDF1()`, `UDF2()`, etc.
- Column type set to A (alphanumeric) or N (numeric); Size = display width.
- UDF template structure:
  ```
  func UDF1                              // must match file number
  define variablename type N size 9 dec 2  // optional work variable
  if filehandle.h = 0                    // open only once
    openv 'tablename' fnum filehandle.h lock N
  endif
  findv M fnum filehandle.h key indexname val fieldname  // find record
  variablename = calculation             // optional calc
  ret variablename                       // return result
  ```
- Grid name is shown in lower-left corner of lookup grid screen.
- Grid definitions are stored in WBKLUGRID.DCY (the grid config file).
- **Copy grid**: open existing grid, answer Y to "create a copy", blank FD name, then answer N to "does not exist" prompt, specify FD name and edit.
- **Security level**: 1 = full access, 999 = most restricted; sensitive grids (payroll) should use low numbers.
- **Start at end?**: Y = grid opens with cursor on last record.
- **Substring search**: alphanumeric fields only; max 6 per grid.

## SU-B Maintain Drill Down Menus — two-file system (EVOHELP.PDF §SU-B, Pass 507)

Two copies of `ISDRILLM.B` exist:
- `DBAMFG\ISDRILLM.B` — IS Tech master; **replaced on every IS Tech update**
- `DBAMFG\DRILL\ISDRILLM.B` — local working copy; user customizations go here

When editing in SU-B, choose "local" (DRILL\) to edit customizations, or "ISTECH" (DBAMFG\) to edit the master (will be overwritten by next update). A drill link record = parent grid + child grid + child index + display text + link field.

To receive an IS Tech update for drill links: copy `DBAMFG\ISDRILLM.B` → `DBAMFG\DRILL\ISDRILLM.B` (overwrites any local customizations).

## SU-D Grid Maintenance — three sync modes (EVOHELP.PDF §SU-D, Pass 507)

| Mode | Behavior |
|------|---------|
| Skip | New grids from IS Tech update appended; same-name grids not replaced (user edits preserved). **This mode runs automatically during IS Tech update install.** |
| Replace | New and existing same-name grids that are newer in the IS Tech version are replaced; user-unique named grids retained |
| Overwrite | Entire grid file replaced by IS Tech standard; all user edits lost |
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

## UT-C Re-Index File (EVOHELP.PDF §UT-C, Pass 516)

When to use: file key structure corrupted from static discharge, power failure, or disk damage.
Symptoms: wrong description returned for a valid code; missing data; Btrieve Status 2 Error.

**WARNING:** Do NOT re-index while other users are on the system — if interrupted, the file cannot be recovered.
**Always make a backup before re-indexing.**

## UT-D Edit Data Location File (EVOHELP.PDF §UT-D, Pass 516)

Manages the FILELOC routing records that tell EVO where each `.B` data file lives.

**Multi-company file extension scheme:**
- Default company: files in `DEFAULT\` folder, extension `.B`
- Company 99: files in `99\` folder (or custom path), extension `.B99`
- Data dictionary files (`FILE*.*`): always in the main EVOERP folder — shared across companies

**Schema files** share another file's layout. When editing, the Layout field = name of the primary file.
For non-schema files, File Name and Layout are the same.

**Chg All Locations** button: mass-reassigns all file paths for a given company code.

**NOTE:** Do not use without Technical Support guidance. Used at initial setup or when adding custom programs.

## UT-H Print File Layouts (EVOHELP.PDF §UT-H, Pass 516)

Prints field specifications for a FROM/THRU range of files. Primary use cases:
- Third-party report writers that need field names and sizes
- DE-A SQL Query Export (to know which fields to select)
- Technical Support and custom program development

## UT-I Create/Delete Company (EVOHELP.PDF §UT-I, Pass 516)

**Single company users:** No action needed — the default company files are pre-installed and ready.
Can also use UT-K-A Clear Data to initialize (empty) the default company files.

**IMPORTANT:** Always use EVO-ERP (not DBA Classic) to create/delete companies — both sets of data dictionaries (EVO and Classic) must be updated together. Using DBA alone leaves the EVO DDF out of sync.

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

## UT-I / UT-K-A through UT-K-G operational detail (EVOHELP.PDF pages 456–462, Pass 521)

### UT-I Create / Delete Company (page 456)
Creates a new company (copy of files from an existing company) or deletes an existing one.
Fields: Company Code / Company Name / Company Path / Delete flag / Create flag /
Copy from existing company? / Copy company code.
Special modes: F3=update data dictionary only (files already exist); F4=create missing files only.
Underlying action: copies Btrieve .B files from source company path to new company path,
then updates the company registry.

### UT-K-A Clear Data (pages 457–458)
Clears or purges all data in a selected module. **The most destructive utility in EVO.**
Entry D = delete ALL records in the module. Entry C = clear transaction data only (keeps masters).
Six selectable module groups: GL / AR+SO / AP+PO / Manufacturing+Inventory / Payroll / Contact Manager.
Always back up and get all users off system first.

### UT-K-B Global Field Replace (pages 458–459)
Mass-update a single field across all records of a Btrieve file.
Fields: File Name, Field to Change, Array# (for array fields), Action (Flat amount / Percentage),
3 filter conditions each with field name + operation (All / <> / > / < / >= / <= / $ / =$) +
comparison value. F10=Process. Test Filters button validates conditions before running.
Same functionality as T7FNR described in FN module.

### UT-K-D Recalculate GL Account Balances (page 460)
Rebuilds GL account balance buckets (BKGLCOA / ISGLCOA) by summing all BKGLTRAN entries.
Useful after data corruption or import. "Orphan" BKGLTRAN entries (account not in COA) are
posted to a configurable suspense account. Allows Current Year / Last Year / 2–6 Years Ago
to scope the recalculation. GL Account From/Thru filter for partial recalc.

### UT-K-E Consolidate Inventory Locations (pages 460–461)
Merges inventory from one location code into another across all 55 inventory-related tables.
Presents an important warning before running. New master location code = target code.
This is a mass-rename/merge — not a quantity transfer.

### UT-K-F Set Average/Last Cost to Standard Cost (page 461)
For each item in inventory, sets the Average Cost and Last Cost fields equal to the
current Standard Cost. Used when switching costing methods or after a cost roll-up.
Per-item or all-items. No undo — run reports first.

### UT-K-G Recalculate Inventory Book Value (page 461–462)
Recalculates the BKICMSTR.BKIC_BKVAL (book value) field for each inventory item
by multiplying on-hand quantity × unit cost. Use after cost corrections or data repair.
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

AR Deposit Apply — applies customer deposit payments to specific Sales Order
line items. Deposits were originally entered via AR-N (Enter/Print Deposits) or
AR-C (Record Payments); MA links those deposit balances to SO shipments/invoices.

**Confirmed from T7MAPDEPO.DFM** (Pass 499, 2026-07-01):

Form Caption: "New Screen" (placeholder) — SourceFile = T7mapdepo

## Form fields (T7MAPDEPO.DFM)

**Header area:**
- Deposit # — the AR deposit record number

**Detail area:**
| Field | Purpose |
|-------|---------|
| SO Number | Sales order being applied to |
| Item Number | Line item on the SO |
| Description | Item description |
| Qty | Quantity |
| Amount | Line amount |
| Deposit Amount | How much of the deposit to apply to this line |
| GL Account | Override GL account (leave blank for default accounts) |

Note: leaving GL Account blank uses the system default AR Customer Deposits account
(set in AD-A). Populated when deposits need to be applied to a specific GL instead.

## AR-N deposit entry workflow (EVOHELP.PDF §AR-N, Pass 517)

AR-N is where deposits are **entered** (the origin step). MA/T7MAPDEPO is where they are **applied** to SO lines.

**Purpose:** For job shops requiring advance deposits before running special orders.

**Two benefits:**
1. Deposit shown on SO acknowledgments and invoices — deducted from total
2. GL automatically handled: deposit → **Customer Deposits (liability)** account (from AD-A); when invoice posts → auto-debit Customer Deposits, auto-credit AR Receivables, auto-applies to correct invoice in aging

**Entry fields:**
| Field | Notes |
|-------|-------|
| Customer Code | Required; name auto-fills |
| Deposit Date | |
| Check Number | |
| Deposit Amount | |
| Currency | If multi-currency enabled |
| Bank Account | Which bank account receives the funds |
| SO Number | Optional link to a specific sales order |

**Editing restrictions:** Can only change SO link and Description. To change other fields: Delete (prompts for reversal date) → re-enter from scratch.

**Credit card processing:** If X-Charge installed and configured in SD-P, a Credit Card button appears after customer selection. Processes credit card; approval code prefixed with V/M/A/D (Visa/MC/Amex/Discover) stored as Check#.

**Report:** Print listing of open deposits, filtered by from/thru Customer Code or Deposit Date range.

## AR-M Customer Refund (EVOHELP.PDF §AR-M, Pass 517)

Processes refunds of customer credits or deposits not applied to sales orders.

- Payment method: AP Voucher / Credit Card (X-Charge) / Manual Check (immediate cash posting)
- AP Voucher: prompts for invoice#, date, description, payment terms; processed at AP payment run
- Manual Check: prompts for bank account, check#, date, description; can print check immediately
- Customer must have matching Vendor code (system prompts to reuse or create new one)

## Integration

- **[[module-AR|AR]]** — deposits originate in AR-N/AR-C; MA links them to SO lines
- **[[module-SO|SO]]** — MA applies deposits against SO orders before invoicing
- **[[module-GL|GL]]** — posts from AR Customer Deposits account to AR control when applied
- **[[module-AD|AD]]** — AD-A defines the default AR Customer Deposits GL account
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

## Shared Paperless sub-forms (T7PLess*.DFM confirmed)

The `T7PLess*` DFM files are shared sub-forms used by the Paperless Shop Floor
system (HH-L / DC-PSF) and are named with the "PLess" prefix:

| DFM | Caption | Fields |
|-----|---------|--------|
| T7PLessComps | Issue Components | All Comps / Issue Comps / Shortages / Item# / WO# |
| T7PLessNotes | Notes Caption | QC Specifications / WO Item / Routing / **Customer / Vendor** / Cancel |
| T7PLessWODates | WO Dates | Total Qty / Exit |

T7PLessNotes has Customer and Vendor links (in addition to QC Spec/WO Item/Routing) — slightly richer than T7DCPSFNotes which is DC-PSF-only. This suggests T7PLess forms are the shared base layer used by multiple contexts.

## Integration

- **[[module-PR|PR]]** — internal EVO payroll; PL is for sites that use an external payroll service instead
- **[[module-HH|HH]]** — T7PLess* sub-forms are called by HH-L (Paperless Shop Floor)
- **[[module-DC|DC]]** — DC-PSF uses T7DCPSFComps/Notes/ECO (DC-specific variants); T7PLess* is the shared base
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

## PS-A field semantics (EVOHELP.PDF §PS-A, Pass 513)

**Default users on a new system:** ADMIN and STARTUP.

**Security Level [1–999]:**
- Level 1 = administrator — can see and edit all lookup grid data
- Levels 1–5 allow editing of data in lookup grids (admin-only range)
- Level 999 = least privileged; blank = treated as 999
- Grid security: each SU-A grid has its own level; a user can only view grids where their level ≤ the grid's level

**Security Code [A/P/1/2/C/V/U/E] — detailed meanings:**
- A=Admin: always full menu even when new programs added (no PS-G record needed)
- P=Power User; 1=Sales Rep 1; 2=Sales Rep 2; C=Customer; V=Vendor; U=User; E=Engineer
- C/V codes: login name must match Customer or Vendor Code exactly
- 1/2 codes: login name must match Sales Rep number
- E=Engineer: restricted to Active Status "E" items in IN-B and BM-A only

**Password lifecycle:** Admin sets initial password at creation; user prompted to change at first login.
User can change own password via File → Change Password in the running EVO session.
Admin can Reset Password (admin cannot see current password, only overwrite it).

## PS-G field semantics (EVOHELP.PDF §PS-G, Pass 513)

**Built-in template menus:** Admin, PowerUser, User, SalesRep, Customer, Vendor.
- Admin menu: cannot be edited or deleted; always has full access; auto-updated on any ADMIN login after an update
- PowerUser/User/Customer/Vendor/SalesRep: can be edited but not deleted — serve as starting templates when creating user menus (copy-from)

**Key operations:**
- **Update to Latest Prg**: updates program .RWN names for programs a user already has (e.g., BKARA.RUN → T7ARA.RWN) without adding new programs
- **Change Prg Name**: updates a single program name across all user menus simultaneously
- **Add Group**: copies a menu group (e.g., "Mfg") from ADMIN or another user; add to one user or all users; skips users who already have the group
- **Menu Lines tab**: left side = what user has access to; right side = removed programs. New programs from updates appear on the right to be optionally added.
- **Drag reorder**: drag grey buttons to change menu group order (controls which group displays first)

## PS-H field semantics (EVOHELP.PDF §PS-H, Pass 513)

Auto-Chain programs — lets a program automatically call the next program (e.g., Print Invoice → Post Invoice).

- User Name: blank = chain applies to **all users**; specific name = that user only
- Chain combination: choose from dropdown of available program pairs
- Mode: **Y** = run next program automatically without prompting; **A** = ask before chaining
- Note: chaining bypasses PS-G menu access checks — the chained program runs even if not in the user's menu

## PS-I field semantics (EVOHELP.PDF §PS-I, Pass 513)

Digital Signers for PO (T7DIGSIGADMIN.RWN):
- Employee must be in SM-G Enter Employees first
- Fields: Employee Number / Password / Signature Image file path / Initials (printed as "Entered By" on PO) / Approval Threshold (dollar limit; 0 = unlimited authority)

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

## SA-A Bookings vs Sales (EVOHELP.PDF §SA-A, Pass 511)

SA-A offers two report modes:

**Sales report:** invoiced shipments only; uses inventory **average cost at time of invoice posting** for COGS.

**Bookings report:** three sections that together equal total net bookings for the period:
| Section | Content | Cost basis |
|---------|---------|-----------|
| Closed Bookings | Invoiced SO lines within the date range | Average cost at invoice posting |
| Open Bookings | Open SO lines not yet shipped | Standard cost at time of order entry/update |
| Changed Bookings | Changes made within the date range to SO lines booked before the range | — |

Multi-currency option: B=Base currency (converts source at current exchange rate for open, historical rate for closed).

## SA-F Chart/Export behaviors (EVOHELP.PDF §SA-F, Pass 511)

All SA-F-* programs produce either a **chart** or a **CSV export**:
- Chart opens in default Windows image viewer (can save or print from there)
- Export generates CSV, opens in default Windows app (typically Excel)

| Program | Chart type | Export columns |
|---------|-----------|----------------|
| SA-F-A | Line chart by day/week/month; optional COGS overlay; optional year-over-year | Invoice#, Date, Customer, Invoice total, COGS, Margin, Margin% |
| SA-F-B | Line chart (same options as A) | Invoice#, Date, Customer, Invoice total, COGS, Margin, Margin% |
| SA-F-C | Pie or bar chart by Sales Rep | Invoice#, Date, Bill To, Ship To, Invoice#, Subtotal, Total, COGS, Margin, Margin% |
| SA-F-D | Pie or bar chart by Item Class (or Top N items) | Item Class, Item#, Desc, Invoice#, Date, Customer, Qty, Extension, Unit Cost, Category, Extended COGS, Margin, Margin% |

## SA-M/SA-N performance note (EVOHELP.PDF §SA-M, Pass 511)

The BKARINV invoice file is large. SA-M/SA-N primary sort key = **Ship Date**. Even when filtering by invoice number range, also specify a Ship Date range to avoid scanning the entire file.

Named reports save all filter settings under a Report Name — reselect the name to reload all settings. RTM formats: T6SAM1 (default detail), T6SAN1 (default summary), T6OPSALE (single summary line per item/customer).

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

## DFM-confirmed details (Pass 489, 2026-07-01)

**T7SHA.DFM (SH-A WO Schedule Viewer):** WO header display — Work Order / Item Number /
Description / Customer / Sched Start / Sched Finish / Due Date / Priority / Class /
Lead Time. **Auto-entry mode [ON/OFF]** toggle (ON = auto-advances to next WO in sequence).
Priorities 1/2/3 in combo items.

**T7SHP.DFM (SH-P Priority Report):** Color-coded WO schedule report with configurable
thresholds. Background color assignments:
- Priority Change Color — when WO priority changes
- Elapsed Start Date Color — WO Start Date has elapsed
- Color for X Days < Start Date <= Y Days — approaching start (amber zone)
- Color for Start Date <= X Days — imminent start (red zone)
- Color for Start Date > Y Days — future/comfortable (green zone)
- WO Finish Date > Est Ship Date Color — finish date exceeds ship commitment
- WOs that Cannot Meet Assigned Finish Date Color — physically impossible finish

**Number of X Days / Number of Y Days** — configurable day thresholds for the color
bands. **"Only show color for WOs that do NOT have any Open, Posted or UnPosted labor"** —
limits color alerts to WOs not yet started. Filters: Start Date From/Thru,
Finish Date From/Thru, WO Class Code From. Items Y/N/P.

## DFM-confirmed SH program inventory (Pass 490, 2026-07-01)

The SL module has at least 13 programs (SH-A through SH-O, not all letters used):

| DFM | Caption | Function |
|-----|---------|----------|
| T7SHA.DFM | SH-A | WO Schedule Viewer: WO/Item/Auto-entry [ON/OFF]/Priorities 1-3 |
| T7SHB.DFM | SH-B | WO Schedule Viewer variant: WO/Start Date/Finish Date/Auto-Entry OFF/Back (same viewer pattern as SH-A) |
| T7SHC.DFM | SH-C | Work Center Capacity Entry: WC/Dept/Total Hours Per Day/% Utilization/Total Shift Hours/Outside Processing? |
| T7SHE.DFM | SH-E | WO Dispatch/Schedule Generation: Action [Generate New/Reprint Prior]; Sort by [Due Date/Work Order No/Critical Ratio]; "Labor Data has been Entered & Posted up Thru" status |
| T7SHF.DFM | SH-F | WO Filter Report: Status Codes [FR]/WO#/Start Date/Finish Date/Job#/WO Class/Priority [1-9]/Planner Code ranges |
| T7SHG.DFM | SH-G | WO Schedule Report: WO STATUS/CLASS/Included Classes/PRIORITY/Sort By/Customer/Start/Finish Date/Planner Code |
| T7SHH.DFM | New Screen | WO Filter Form: WO#/Start Date/Finish Date/Planner Code/Item#/Customer/Status Codes |
| T7SHI.DFM | SH-I | Color-Coded WC Schedule Report: Elapsed Start Date Color/Background Color/"Only show color for WOs Not Started on Time"; WC/Customer/Start/Finish Date ranges |
| T7SHJ.DFM | SH-J | WO Schedule Report: WO STATUS/CLASS/PRIORITY/Sort By/Customer/Start/Finish/Planner (similar to SH-G) |
| T7SHP.DFM | SH-P | Priority Color Report: 7 color zones/X-Y day thresholds (see details above) |
| T7SHM.DFM | SH-M | Item Schedule: Item#/Desc/Qty/Start Date/Lead Time/Est Finish/Priority 1/Queue Times |
| T7SHN.DFM | SH-N | Part Planning: PART TYPES/Item#/Item Class/Item Category/Planner Code/Cycle Code/Calculate using |
| T7SHO.DFM | SH-O | WC Report: Work Center From/Thru; Page Break between Work Centers? |
| T7SHIPRTM.DFM | New Screen | User RTM Assignment: User/RTM Name/Add/Delete/Back; "Back to the List of links" — assigns per-user RTM report templates for SH reports |

**Critical Ratio** sort order in SH-E = classic MRP dispatch rule: CR = (Time remaining) / (Work remaining),
where CR < 1 means late, CR = 1 means on-time, CR > 1 means slack.

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

## SD-B — Work Orders Defaults (field semantics, Mfgug.pdf Ch.23, Pass 504)

| Field | Values | Meaning |
|-------|--------|---------|
| Work Order Status Code | S/F/R | S=Scheduled (no allocation), F=Firmed (allocated), R=Released (on shop floor) |
| Default Priority Code | 1/2/3 | Sort order for scheduling; 2=most common default |
| Default Class Code | 1 char | User classification for WO reports/filters |
| Next Work Order Number | integer | Auto-increments each new WO |
| Labor Prompt in Kit Issues? | Y/N | Y=pop-up prompt to include labor in kit issues; N=always include |
| Backflush in Enter Finished Prod? | Y/N | Y=present backflush option in WO-I |
| Close WO in Enter Finished Prod? | Y/N | Y=present close-WO option at finish entry (WO-I) |
| View only in WO Bills of Mat? | Y/N | Y=read-only WOBOM after creation |
| Print BOM Remarks? - Traveler | Y/N | Print component BOM remarks on shop traveler |
| Print BOM Comments? - Traveler | Y/N | Print WO BOM comments on traveler |
| Print Job Schedule? - Traveler | Y/N | Print related WOs (same prefix) in traveler header |
| Print Short Form? - Traveler | Y/N | Y=short format, N=long format |
| Print Bill of Mat? - Traveler | Y/N | N=suppress BOM from traveler |
| Use Std Cost in Ent Fin Prod? | Y/N | Y=always receive finished goods at std cost; N=allow actual cost |
| Print Mat in Seqs? - Traveler | Y/N | Y=print BOM within routing sequences |
| Print Machine and Tool - Traveler | Y/N | Print machine/tool assignments on traveler |
| Print Inspection Fields - Traveler | Y/N | Print sign-off fields (qty/first-article/last-article/accepted/rejected) |
| Use Actual Costs in Labor Entry? | Y/N | Y=use employee file labor rates; N=use work center standard rates |
| Post Overhead as % of Labor? | Y/N | Y=OH rate is % of labor cost; N=OH rate is $/hr |
| Calculate Labor from Bills of Mat? | Y/N | Y=ES-E converts BOM type-L items to routing time |
| Delete Labor after BOM Calc? | Y/N | Y=delete type-L items from BOM after conversion |
| View only in Enter Routings? | Y/N | Y=read-only WORO after creation |
| Backflush by Sequence in Enter Labor? | Y/N | Y=prompt for sequence backflush in WO-F |
| Divide Labor Cost by # Jobs Worked | Y/N | Y=split labor cost equally among concurrent WOs |
| Print Multi Routings? - Traveler | Y/N | Y=multiple routing numbers on one WO print as separate routings |

## SD-C — Purchase Orders Defaults (field semantics, Mfgug.pdf Ch.23, Pass 504)

| Field | Values | Meaning |
|-------|--------|---------|
| Print Co. Name/Address on forms? | Y/N | Print company name/address on PO/RFQ forms |
| Force PO to use approved vendors? | X in slot | X=Do not check / X=Warn if unapproved / X=Prohibit unapproved |
| Next PO Number | integer | Auto-increments each new PO |
| Next RFQ Number | integer | Auto-increments each new RFQ |
| Track PO Taxes using Tax Groups | Y/N | Y=track incoming sales tax by tax group |
| Default PO Tax Rate | decimal | Tax rate for non-tax-group taxable POs |
| Require Pack Slip Info? | Y/N | Default in PO-C header: require packing slip info on receipt |
| Receive Into | I/Q | I=Inventory direct, Q=QC Inspection |
| Receive all Lines? | Y/N | Default for PO-C: receive all lines at once |
| Item Number for Job Cost Freight | item code | Freight-to-WO item number for AP-C |

## SD-D — Material Requirements Defaults (Mfgug.pdf Ch.23, Pass 504)

| Field | Meaning |
|-------|---------|
| Include in MRP Generation? | Default Y/N for new inventory items created in IN-B |
| Expedite Buffer (days) | Days within which a late arrival triggers EXPEDITE (not a new BUY) |
| Expedite Sensitivity (days) | Suppress EXPEDITE if days-late ≤ this value |
| Delay Buffer (days) | Days early that triggers DELAY (not REVIEW) for early arrivals |
| Delay Sensitivity (days) | Suppress DELAY if days-early ≤ this value |

## SD-E — Scheduling Defaults (Mfgug.pdf Ch.23, Pass 504)

| Field | Values | Meaning |
|-------|--------|---------|
| Update actual seq start/finish dates? | Y/N | Y=finite scheduling; ask "is sequence complete?" in PO-C/WO-F/DC |
| Allow overlap settings in routings? | Y/N | Y=show forward OVERLAP field in RO-A (finite scheduling) |
| Display Machine prompt in Enter Labor? | Y/N | Y=pop-up machine override in WO-F (infinite/manual scheduling) |

## SD-F — Data Collection Defaults (Mfgug.pdf Ch.23, Pass 504)

| Field | Values | Meaning |
|-------|--------|---------|
| Allow clocking in/out on multiple jobs? | Y/N | Y=concurrent WO sequences; auto-split labor across open seqs |
| Use full screen? | Y/N | Y=full transaction history display; N=two-line entry mode |
| Enable Employee Shift Start/Stop? | Y/N | Y=track shift records for payroll (DC-A/DC-C) |

## SD-G — Estimating Defaults (Mfgug.pdf Ch.23, Pass 504)

| Field | Meaning |
|-------|---------|
| Starting Quote Number | Next ES-A quote number |
| Default Status Code | A=Active / C=Converted / I=Inactive / X=Canceled |
| Default Class Code | 4-char estimate classification |
| Num Days to Expiration Date | Quote validity period (added to quotation date) |
| Material Margin | Default profit margin % for material cost |
| Labor Margin | Default profit margin % for labor+setup cost |
| Outs Proc Margin | Default profit margin % for outside processing |
| Overhead Margin | Default profit margin % for overhead |
| Total Margin | Applied to all costs above (not to misc/extra costs) |
| Default Machine for Trim Size | RO-D machine for Yield Calculator (sheet cutting) |
| Use Yield Calculator in BOM entry | Y/N |

## SD-H — Inventory Defaults (Mfgug.pdf Ch.23, Pass 504)

| Field | Values | Meaning |
|-------|--------|---------|
| Default Inventory Location | blank or code | Blank=no location required (single-warehouse); code=default location |
| Average, FIFO, LIFO Costing? | A/F/L | A=weighted running average; F=FIFO; L=LIFO; change via IN-L-I only |

## SD-I — Routings Defaults (Mfgug.pdf Ch.23, Pass 504)

| Field | Values | Meaning |
|-------|--------|---------|
| Multiply or Divide by Num Processes | M/D | M=multiply processes×rate; D=divide rate by process count |
| Use Standard Time | Y/N | Y=apply std time in WO-F; N=require actual time entry |

## SD-M — Sales Orders Defaults (Mfgug.pdf Ch.23, Pass 504) — key behavioral flags

| Field | Values | Meaning |
|-------|--------|---------|
| Next Sales Order Number | integer | Auto-increments each new SO |
| Next Invoice Number | integer | Auto-increments each new SO-F invoice |
| Next Packing Slip Number | integer | Sequential packing slip tracker |
| Next Recurring Sales Order No | integer | Recurring SO template counter |
| Next Sales Quote Number | integer | ES-A quote counter |
| Default Taxable | Y/N | Default taxable status for new SOs; overridden by SM-A customer flag |
| Ready to Ship Default | Y/N | Default Rdy? flag for instant invoicing without SO-E release |
| Release Qtys > On Hand | 0/1/2 | 0=no control; 1=warn but allow; 2=prohibit |
| Turn the Credit Limit Message off? | Y/N | Y=suppress credit limit warnings in SO-A |
| Prompt for Taxable Line Item Amt? | Y/N | Y=pop-up to override taxable amount per line (construction use) |
| Prompt for Itemized Sales Tax? | Y/N | Y=ask to itemize sales tax on each SO save |
| Prompt for Retention Billing? | Y/N | Y=offer retention % split at SO-E release |
| Print Discount Column on Forms? | Y/N | N=suppress discount column on SO forms |
| Decimalized Quantities on Forms? | Y/N | Y=suppress decimal places on order documents |

## Integration

All SD defaults are stored in `BKYSMSTR` (355f) and `BKSYMSTR` (286f). Every
module reads its operational defaults from those singletons at runtime. The
Mfgug.pdf Ch.23 field descriptions above directly explain the BKSY.WO.* / BKSY.PO.*
/ BKSY.SO.* / BKSY.MRP.* / BKSY.DC.* / BKSY.EST.* namespaces used in T7MDEFAULTS.

## SD-A Company Defaults (EVOHELP.PDF §7.3.2 pages 495–496, Pass 518)

| Field | Values | Effect |
|-------|--------|--------|
| Configuration Settings | 0 / 1 / 2 | 0=no form-default changes; 1=system-wide defaults; 2=system-wide + per-workstation user overrides |
| Password | string | Required to change system-wide config when setting is 1 or 2; blank = anyone can change |
| Alt. Drive for \ISTS\ | C or blank | Always C or blank unless using Terminal Services / Citrix |
| Multiple Print Dialog Box | Y / N / A | Y=reopen after print; N=no reopen; A=ask "Finished Printing?" |
| Remove EDI SO-IN file | Y / N | Prompt to clear ED-B import file after import |
| Enable Del/Make Obsolete in IN-L-O | Y / N | Allow IN-L-O to make items Obsolete or Delete |
| Enable Change/Save Default RTMs | Y / N | Prompt to set non-default RTM as new default |
| Maximize Evo Menu Screen on Start | Y / N / blank | N=remember last menu size; blank/Y=always maximize |
| Trace Evo File Name | string | Leave blank unless instructed by tech support for debugging |
| Enable Evo Notes System | Y / N | Enables Memo-style free-form Notes for printing |
| Enable Evo Links System | Y / N | 256-char path / Evo Links to all master files (not just inventory) |
| Enable/Disable/Hide BCC box | E / D / H | Controls BCC visibility in email dialogs |
| Control Ship Via Code | N / Y / R / A | N=no check; Y=list but optional; R=required from list; A=add-on-fly |
| Use Evo Login as Paperless Login | Y / N | Employee# (SM-G) = PS-A Logon ID; auto-clock-in on HH-I load |
| Permanently Disable DBA Classic | Y / N | Must disable Classic if passwords are encrypted (irreversible once encrypted) |
| Permanently Encrypt Passwords | Y / N | **Irreversible.** Requires ADMIN user + no blank passwords; DBA Classic must be disabled |
| Company name | 25 chars alphanumeric | Displayed at top of master menus and printed on forms |
| Address Line 1 / Line 2 | 25 chars each | Company address printed on forms |
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
| CC-R (alt) | ISCCREP.DFM | **Credit Card Report** — Sales Order From / Thru date range filter; prints CC activity by SO |

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

Company Paths — a single-row system configuration table (`BKCPMSTR`) that stores
custom file-path overrides for the EvoERP installation. Not a menu-accessible module;
the table is populated at install time if non-default paths are needed.

**CORRECTION (2026-07-01):** Previously mislabeled as "Credit and Payment." There is
no `CP` entry in `BKMENUSU.TXT`. Credit card and payment processing lives in
[[module-AR|AR]] (AR-B Enter Cash Receipts, BKARCUST.CRLIMIT). Credit hold release
is in [[module-CR|CR]] Contract Review. BKCPMSTR is a path-config table, not a
payment table.

## Key table: BKCPMSTR (9 fields, 1 row)

| Field | Meaning |
|-------|---------|
| `BKCP_MST_CMPATH` | Company master path (custom install location) |
| `BKCP_MST_IMPATH` | Image files path |
| `BKCP_MST_CFILE` | Company-specific config file |
| `BKCP_MST_VFILE` | Vendor file override |
| `BKCP_MST_EXPATH` | Executable path override |
| `BKCP_MST_HFILE` | Help file path |
| `BKCP_MST_LABEX` | Label file extension |
| `BKCP_MST_COMMEX` | Common files extension |
| `BKCP_MST_EFILE` | Executable file name override |

At i2 Systems all 9 fields are empty (default paths used). BKCPMSTR exists in the
ODBC DSN=DBA catalog but is not referenced by any menu group.
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

## DFM-confirmed details

**T7CTRevu (Setup Contract Review Departments):** Admin configuration form —
Password + Confirm Password + Department fields; Admin Level + Mass Approval
toggles; SO filter: SO Number From/Thru + Order Date From/Thru; actions:
Save / Reset / App SOs (bulk approve SOs in range) / Kill (delete record).

**T7CTRevuPSWD (Enter Contract Review ID and password):** Auth sub-form —
Contract Reviewer ID / Department / Password. Shared with T7SORevuPSWD.

**T7SORevu (SO Contract Review):** Live SO review display — SO Number /
Customer / Entered By / Entered Date; grid (ETBcomboval = LISTG60.LIB);
hints: "SO Notes" / "SO Evo Links" / "Clear Data" / "SO Department Evo Links" /
"SO Department Notes" — confirms the CR review screen has direct access to
SO-level and department-level notes and EvoLinks attachments.
Actions: Save / Exit / Kill.

## Conceptual model (EVOHELP.PDF §CR, Pass 513)

Contract Review replaces the physical "job folder" that circulates through departments for
approval. The electronic system links scanned PDFs, drawings, inspection sheets, packing
slips, and invoices to a contract record, replacing the paper folder lifecycle.

**Administrator requirements:**
- At least one Administrator is required — the admin enters the other approvers and departments.
- Every department that exists is a **required approval by default** for every contract.
- The Administrator determines, per contract, which approvals are actually required.
- Department names must match exactly — "Credit", "Accounts Receivable", and "A/R" are three separate departments.

**Enabling the module:**
- Once at least one approver exists, Approval Control is active.
- SOs cannot convert to WOs, print packing slips, or print invoices until approved.
- Use PS-J Enter Contract Review Signers → Mass Approval option to pre-approve all existing
  orders when first enabling, so only new orders require fresh approvals.

**CR-A — Assign Departments to Sales Order:**
- Requires Contract Review Admin ID + password.
- If no approvals exist for the SO, prompts to add them; else displays existing list.
- Select which departments are Required for this order vs. optional.
- Evo Links and Notes can attach at both SO level and per-department level.

**CR-B — View/Enter SO Approvals:**
- Displays departments assigned and current approval status (date if approved).
- Approver clicks the Approved field, enters Y, then provides their CR ID + password.
- System verifies authorization — only designated approvers for the department can sign.
- Evo Links and Notes accessible per department from CR-B.

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

## ISFXASST key fields (EVO3.JAR, 23 active out of 48 total)

| Field | Meaning |
|-------|---------|
| IS_FXA_NUMBER | Asset number (PK) |
| IS_FXA_TYPE | Asset type code |
| IS_FXA_DESC / DESC2 | Description (two lines) |
| IS_FXA_SERIAL | Asset serial number |
| IS_FXA_SDATE | Acquisition / in-service date |
| IS_FXA_EDATE | Disposal / retirement date |
| IS_FXA_CSTBAS | Cost basis (original acquisition cost) |
| IS_FXA_RESVAL | Residual / salvage value |
| IS_FXA_LIFE | Useful life (years) |
| IS_FXA_METH | Depreciation method code (SL=straight-line, DDB=double-declining, etc.) |
| IS_FXA_ACCUMDEP | Running accumulated depreciation total |
| IS_FXA_ACDEPA / ACDEPD | Accumulated depreciation GL account / dept |
| IS_FXA_DEPEXPA / DEPEXPD | Depreciation expense GL account / dept |
| IS_FXA_GLA / GLD | Asset at-cost GL account / dept |
| IS_FXA_LDEPAMT | Last depreciation amount posted |
| IS_FXA_LDEPDATE | Last depreciation date |
| IS_FXA_LDEPPERC | Last depreciation rate (%) |
| IS_FXA_SOLD | Disposal flag (Y = asset retired/sold) |
| IS_FXA_EXTRA | Spare / custom use |

## Asset disposal workflow

When an asset is retired or sold, the following fields record the event:
- `IS_FXA_SOLD = 'Y'` — marks the asset as disposed
- `IS_FXA_EDATE` — disposal date
- `IS_FXA_CSTBAS - IS_FXA_ACCUMDEP` = net book value at disposal
- GL entries required: **DR Accumulated Depreciation** + **DR Cash** (if sold) + **CR Asset at Cost** ± **CR/DR Gain/Loss on Disposal**

EVO generates these GL entries via FA-B (Post Depreciation) on the final depreciation period
before the disposal date. The actual disposal GL lines are posted through the GL module
journal entry (T7GLA) since there is no dedicated FA-Disposal program — the SOLD flag and
EDATE update are made directly in FA-A (Edit Asset).

## DFM-confirmed details (3 DFMs)

| DFM | Caption / Confirmed |
|-----|---------------------|
| T7FAA | **FA-A Enter Asset** — Asset Number, Type, Description, Cost Basis, Residual Value, Life (depreciation life in years) |
| T7FAB | **FA-B Post Depreciation** — Asset Number, Amount, Percent, Post date, Net Asset Value, Accumulated Dep Acct; confirms GL accounts visible on posting screen |
| T7FAE | **FA-E Export Assets** — File Name (with path), Length or Delimited import format, Asset Number; `* = Basic Fields` note for simplified export |

## Utility data browser forms (UT7G*.DFM)

`UT7GFAC.DFM` and `UT7GFAD.DFM` are FA-specific utility data browser panels used for
drilling into fixed assets data (FXATRN transactions and FXASSETS master) from within
module contexts. These are runtime-loaded forms (caption = "Loading....") — the actual
table name (FXATRN/FXASSETS) appears as the second caption field.

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

"GF": """
## What it does

Golding Farms — a **customer-specific customization module** built for a single
customer account. Not a standard EvoERP module; these programs exist only at
installations that serve Golding Farms. All 8 DFMs found on the i2 Systems network
share (T7GF prefix).

## Programs (8 DFMs confirmed, 2026-07-01)

| DFM | Caption / Type | Purpose |
|-----|----------------|---------|
| `T7GFPRICE.DFM` | **Golding Farms Pricing** | Delivered price management per bill-to customer: Add/Save/Archive Data/View Archive; Cust/Street/City address; Notes, Sales Orders, Shipments links |
| `T7GFCB.DFM` | New Screen (General + Order tabs) | Customer / Bill-To order entry with standard toolbar (Save/Exit/Delete) |
| `T7GFR.DFM` | New Screen (report range) | Report by Orders From/Thru date range |
| `T7GFV.DFM` | New Screen (view, Today button) | Today's orders viewer + Print |
| `T7GFVS.DFM` | New Screen ("Orders to ship on") | Ship-schedule viewer + Print |
| `t7GFdept.DFM` | New Screen | Golding Farms **department code** table (Dept Code + Description) |
| `t7GFdiv.DFM` | New Screen | Golding Farms **division code** table (Div Code + Description) |
| `T7GFTEST.DFM` | New Screen (test get file()) | Developer test form — not production |

## Key features (T7GFPRICE)

Delivered Prices screen for Golding Farms pricing:
- Bill-To Customer header (Cust + Street + City)
- **Delivered Prices** grid — customer-specific delivered pricing
- **Archive Data** / **View Archive** — price history archive workflow
- **Notes**, **Sales Orders**, **Shipments** sidebar buttons

## Scope

GF is invoked directly by program name (not via a standard BKMENUSU menu group).
T7GFdept/div provide lookup tables for the GF-specific department and division codes
used in Golding Farms order entry. No standard `BK*` tables found for GF — pricing
data likely stored in a custom `IS*` or standalone `.B` file.
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

## Setup workflow (EVOHELP.PDF §FO, Pass 512)

| Step | Action |
|------|--------|
| 1 | Create **Type O inventory items** for each feature (not stocked, not ordered; decision point in configurator) |
| 2 | Create **Option Bills of Material** via FO-A or BM-A: enter the Type O item as parent; each option is a component |
| 3 | Add **Feature items (Type O)** to the parent product's BOM wherever optional components exist |
| 4 | Review via FO-B Print Features and Options to verify structure |

**Unlimited nesting:** Features can contain Features (e.g., FABRIC → PATTERNS or SOLIDS → specific options). Options can also contain their own features. The configurator traverses the full tree.

### FO-A — Option Settings (5 fields per option in the option BOM)

| Field | Options | Meaning |
|-------|---------|---------|
| Manufactured or Kit type | **M** = passes to WO BOM; **K** = stays on SO line only (no WO) |
| Include in cost rollup? | Y/N | Whether this option's standard cost is included in parent rollup |
| Percentage pricing? | Y/N | If Y, option price is a % of the parent's price |
| Option price/percent | numeric | Flat price per unit (or % if Percentage=Y); multiplied by Qty Per × order qty through all nesting levels |
| Add price to parent? | **Y** = option price added to parent price; **N** = itemized as a separate line on the SO |

Defaults for these settings can be configured in SD-L Features and Options Defaults.

### FO-A — Feature Settings (when a Feature/Type O item is added to a parent BOM)

| Setting | Meaning |
|---------|---------|
| Mandatory Feature | Selection required during SO entry — operator cannot skip it |
| Feature not required | Selection optional at order entry operator's discretion |

### FO-G conversion targets

FO-G can convert a completed configuration to: **Sales Quote**, **Sales Order**, **Work Order**, **Vendor RFQ**, **Purchase Order**. Multiple targets can be processed sequentially in one operation. A future release would also support converting to a permanent part number.

FO-G status codes: blank = in-progress / Completed = all selections done (Convert button enabled) / "Cvt to" = previously converted.

## FO-G Configure Item UI (EvoFNO.DFM)

The main configurator form has two display modes and several actions:

- **Indented View** — shows BOM hierarchy with parent/child indentation
- **Edit View** — flat editable grid for changing option selections
- **Tag / All** — tag individual components or tag all for batch operations
- **Sort** — re-sort the displayed BOM by various criteria
- **Convert** — launch conversion dialog; three targets:
  - **Convert → PO** (`EvoFNOPO.DFM`): "Converting to Purchase Order" progress dialog
  - **Convert → SO** (`EvoFNOSO.DFM`): "Converting to Sales Order" progress dialog
  - **Convert → WO** (`EvoFNOWO.DFM`): "Converting to Work Order" progress dialog
- **Qty dialog** (`EvoFNOQty.DFM`): "F&O Qty" — prompts for QTY to be made, Location,
  Cust/Vend, Due Date before conversion

Conversion writes to ISFOHIST with CVTTO = 'SO', 'PO', or 'WO' and CVTNO = target document#.

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

## DFM-confirmed (T7IC2EST.DFM, Pass 519)
Caption: "Copy Production to Estimate Inventory"
Only user-input field: **Inventory** (item number). Go + Exit buttons.
Operation: enter one item number and click Go to copy that item's `BKICMSTR`
production record into the estimating inventory mirror (`ISICMSTR`/`MTICMSTR`).
This is a single-item sync, not a full-table copy. Useful after a new item is
set up in production and needs to be immediately available in ES Estimating.
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
| IM-G | Enter Tax-In Codes | t7img.rwn |
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

## Multi-currency GL accounts per currency (Pass 503, Acctug.pdf Chapter 9)

Each source currency configured in IM-B has its own set of GL accounts:

| Account | Purpose |
|---------|---------|
| AP Control | AP balances in source currency |
| AR Control | AR balances in source currency |
| AR Deposits | Customer deposits (AR-N) in this currency |
| PO's Rec'd Not Invoiced (PORNI) Control | Uninvoiced PO receipts in source currency |
| PORNI Conversions | Offset for Convert-to-Base routine |
| F/E Gain/Loss — Transactions | FX gain/loss on individual transactions |
| F/E Gain/Loss — Conversions | FX gain/loss on periodic conversion runs |
| Bank Account | Bank balance in source currency |
| Bank Account Conversions | Offset for Convert-to-Base routine |

## Currency conversion workflow (IM-B, confirmed from Acctug.pdf Chapter 9)

The "Convert to Base Currency" routine (IM-B) runs in **two transactions per account**:

1. **Reversal of last conversion**: Credits or debits the Conversions account for the
   amount stored in "Last Conversion Values" (cancels the previous period's FX entry).
   Offsetting entry goes to the F/E Gain/Loss-Conversions account.

2. **New conversion**: Formula: `(current rate − 1) × Control Account balance = Conversion amount`.
   The Conversion amount is posted to the Conversions account; offset to F/E Gain/Loss-Conversions.
   Net result: `Control Account + Conversions Account = total balance in base currency`.

This two-step reversal+rebook approach ensures prior-period FX entries do not accumulate;
only the most recent conversion value persists in the Conversions accounts.

## IM-G: Tax-In Codes (back-out embedded taxes)

IM-G defines **Tax-In** codes — used when the selling or purchase price already includes
taxes embedded in it. Each code specifies the rate and the GL accounts to which the
backed-out tax amount is posted. Tax-In amounts reduce the invoice price and post the
difference to the assigned tax GL accounts. Used in markets where prices are tax-inclusive
(e.g. GST/VAT models).

## IM-E: Duty Code structure (Acctug.pdf confirmed)

The 6-character Duty Code = vendor code first 3 chars (from AP-A) + item code last 3 chars
(from IN-B). Example: if vendor has Duty Code "CHN" and item has "ELE", the combined code
is "CHNELE". Duty percentage is assigned to this combined code in IM-E.
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

## Shared lookup engine (WBKLOOKUP)

`WBKLOOKUP.DFM` — "Evo Lookups" — the universal list-picker dialog used throughout
EvoERP to let users choose from any table. Buttons: Select, Edit, Add New, Delete,
Go, Exit, Print, SSSFD (saved searches/sort/filter), Change View, Drill_down, Drill_up,
Camera (image viewer). This is the backbone behind every "lookup" field in EVO.

`WMBKLOOKUP.DFM` — Mobile/web variant of the lookup: Lookup:, Select, Edit, Add New,
Delete, First, Previous navigation buttons — used in HH/mobile contexts.

`WBKHHLOOKUP.DFM` — HH-specific list picker: Search, Sort List by, Tag All/UnTag All,
Vendors Number / Manufacturers / Customers X-Ref sub-tabs — used in handheld item lookup.

`WBKLUGRID.DFM` — "Maintain Grid Lookup Data" admin tool: Grid Name, FD Name,
Form Name, Security Level, Start At End, Key Data, Sort Keys — configures which columns
appear in each lookup popup and how it sorts. Accessed by SU/SM admins.

`WBKLKPMEMO.DFM` — "Edit Memo Field": Save/Cancel — inline memo editor invoked when a
lookup field contains a long text value (e.g., note or description over one line).

`WBKLPRINT.DFM` — "Order Printing": Print Acknowledgements / Print Packing Slips /
Print Invoices / Go — quick batch-print dialog launched from the SO lookup to print
multiple document types for the selected order in one step.

`GetAlphaGen.DFM` — minimal 1-field text input (GAG Caption, GAGLABEL, Cancel) —
used wherever a single string prompt is needed without a full form.

`GetFileName.DFM` — "Enter File" — File Name, Local/Server path toggle, Cancel —
shared file-path picker for import/export dialogs.

## Drill-down UI mechanics (EVOHELP.PDF §QU, Pass 513)

The drill-down button (green circle with white downward arrow) appears in any program where
drill-links are established and the user has security level access.

**Navigation bar** (top of all lookup grids): First record / Previous / Next / Last + Select /
Edit / Add / Delete / Exit buttons + Fast Find field + Sort dropdown.

**Fast Find:** searches the current index as-you-type. Change sort order via the dropdown.

**Sub-string search** (funnel+equals icon): filter/search on a substring — not case-sensitive,
finds all matches. Configurable fields: up to 6 fields per grid. Result treated as a drill-down;
drill-back (red circle with white upward arrow) returns to prior level.

**Print Grid** toolbar button: dumps drill-down results to an RTM.

**Print Associated Documents** toolbar button (visible in SO/PO contexts): print
Acknowledgements / Packing Slips / Invoices (for SO) or POs — batch-print without leaving QU.

## SU-A Maintain Grid Lookups (EVOHELP.PDF §SU-A, Pass 513)

Grid Lookup admin program. Three parts:

**Grid Name section:** Grid Name (the name used by lookups/drill-downs), FD Name (the
Btrieve/PSQL file opened — select from dropdown of registered file names), Form Name
(always `WBKLOOKUP`), Security Level (1=full access, 999=most restricted; controls which
users see which grids).

**Field Data section:** Column Header / Field (from dropdown of file fields) / Sub-string search
flag (only alphanumeric fields; max 6 per grid).

**Key Data section:** Column Header (sort name) / Index Key Name (from dropdown) /
Match Field Name (first field of compound index; usually same as key name).

**Deleting:** Bring up a grid and press Delete.

**Copying:** Bring up existing grid → answer "yes" to copy → blank out Grid/FD names →
type new name (system says "not found, create new?" → answer No) → enter FD name →
edit fields/keys → save.

## User-Defined Functions (UDF) in SU-A

UDFs add calculated columns or cross-file columns to any Lookup Grid. A UDF is a `.SRC`
text file (e.g., `UDF1.SRC`) containing up to 5 sections: Define variables / Open file /
Find correct record / Perform calculation / Return results. Stored in the EVO program
directory. Referenced in the field data section of SU-A.

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

## DFM-confirmed additional details (Pass 519)

### T7ACRDTYPE.DFM — Document type codes
Doc Type dropdown contains 6 predefined values:
| Code | Meaning |
|------|---------|
| ECN | Engineering Change Notice |
| VAR | Variance |
| MIN | Minor (change) |
| COR | Corrective (action) |
| DR | Design Review |
| QUA | Quality |
Each record also carries: **Reason** (free-text) + **Disposition** (free-text).
The OR label suggests these can be combined/OR'd in filters.

### T7ACDATE.DFM — WO date span entry
Fields: Start Date, Finish Date, Quantity, Parent WO, Top WO, Deleted WO.
Total Qty shown in footer. Add/Save/Delete/Back toolbar.
"Top WO" and "Deleted WO" fields confirm this tracks WO hierarchy and handles
deleted-WO date records (orphan cleanup).
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

## Default preset queries (CHM-confirmed + Pass 493 DefaultSQL files)

Seven built-in reconciliation queries available via "Default Queries" button.
Six of the seven have SQL source files confirmed in `samples/2004share/DefaultSQL/`.

| Name | SQL file | Purpose |
|------|---------|---------|
| `GLPOINV` | `RNI Invoiced.sql` | GL txns to PO/RNI from AP-C with no matching BKAPHPOL line (BKGL_TRN_DESC=`'RNI/INVOICED'`) |
| `GLPORECPT` | `RNI Received.sql` | GL txns to PO/RNI from PO-C with no matching BKAPHPOL line (BKGL_TRN_DESC=`'RECEIVED/NOT INVOICED'`) |
| `Inv_Txn_no_GL` | `Inventory txn no GL Post.sql` | INVTXN rows with no matching BKGLTRAN entry |
| `INVGL` | `GL no Inv Txn.sql` | BKGLTRAN rows with no matching INVTXN entry |
| `Inventory_Non_Asset` | `Inventory Non Asset.sql` | Tangible inventory items (type R/F/A/M) posting to non-asset GL accounts |
| `Non_Inventory_Asset` | `Non-Inventory Asset.sql` | Non-tangible items (type N/L/K/T) posting to asset GL accounts |
| `INVGLACCT` | *(no SQL file found)* | Inventory transactions with incorrect GL accounts (wrong item class/location) |

The GL↔IN cross-reference queries both use the same MTIT_TYPE → BKGL_TRN_TYPE
12-code mapping table (see [[module-GL|GL]] and [[module-IN|IN]] for the full map).
The join also matches on `MTIT_EXTRA` binary date (offsets 26/29/32) against
`BKGL_TRN_ENTDTE` and on `ROUND(ABS(MTIT_QTY * MTIT_AVGCOST), 2)` = `BKGL_TRN_AMT`.

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

## US-A field semantics (EVOHELP.PDF §US-A, Pass 515)

**Settings are workstation-specific** except Email settings which are per-user + per-company.

**Tabs:** Misc / Mfg / Items / Sales / Queries / Sys Mgr / Accounting / Payroll / Email

**Misc Tab key settings:**
- **Enable Toolbar**: upper-right toolbar (calculator, camera, web link, etc.)
- **Notification Sounds**: "Ding" wav when lookup grid search completes
- **Language**: activates screen translation (ML tables must be created in SM-R first)
- **Enable Evo Reminders on Startup**: opens Reminders calendar on launch; also required for Triggers to function
- **Enable Evo Notifications**: receives IS Tech Support broadcast messages via FTP (needs internet)
- **Check for reminders**: frequency of reminder polling
- **Snooze All**: resets all open reminders by specified minutes
- **Enable Quick Printing**: bypasses RTM name/notes popup screens; uses defaults
- **Hot Buttons 1-6**: assigns programs to launch from main menu Hot Button slots; optional image per button

**Email Tab key settings:**
SMTP address / Login / Port / BCC address / Default subject+body+signature /
Attach path (folder for PDF generation; Windows user must have full write rights) /
Auto-email failure address (receives notices when batch items have no email — e.g., invoicing batches)

**Mfg/Items/Sales/Accounting Tabs:** Each tab controls: show opening list Y/N; load in Evo tabbed view vs. DBA Classic view.

## US-G Triggers — event codes (EVOHELP.PDF §US-G, Pass 515)

Triggers are **scheduled business event notifications** — EVO fires a trigger
(email or on-screen alert) when defined conditions are met. T7USG.RWN manages
the trigger list; data stored in a Btrieve-only IS_TRIG* table (not in DDF).

**16 trigger event codes:**

| Code | When fires |
|------|-----------|
| `REORDER` | Item stock on-hand hits reorder level |
| `REORDERA` | Item quantity **available** hits reorder level |
| `EFP` | Enter Finished Production |
| `RECEIPT` | Purchased item received |
| `RECEIPTQC` | Purchased item received to QC |
| `LOT` | Lot-controlled item within N days of expiration |
| `SERIAL` | Serial-controlled item within N days of expiration |
| `BASE PRICE` | Item base price changed in SO-Q-A or IN-B |
| `SO` | New SO entered or lines added (one trigger per line) |
| `SOEDIT` | Existing SO lines edited |
| `SODELETE` | Existing SO deleted |
| `PO` | New PO entered or lines added (one trigger per line) |
| `EPO` | PO edited (one trigger per line) |
| `NONPO` | PO receipt is past estimated receipt date |
| `NONSO` | Sales Order is past estimated ship date |
| `NONWO` | Work Order is past estimated completion date |

**LOT/SERIAL triggers:** enter "Days Pre" = days before expiry to warn.
**NON* triggers:** checked at each login, scanning back to last login date.
**Security Level 1-10:** can create triggers for other users; >10 = self only.
**Notification:** desktop popup (link to IN-A for item) + optional email to multiple addresses.
**At i2 Systems:** triggers are configured but status of active records is unknown (IS_TRIG* is Btrieve-only, not in ODBC).

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

## DFM-confirmed details (Pass 489, 2026-07-01)

| DFM | Caption | Key fields / purpose |
|-----|---------|---------------------|
| T7AMK.DFM | New Screen | MK-A Purge/Archive/Restore — **Purge, Archive or Restore [P/A/R]** selector; Process Thru Date; Customer From/Thru range; Go/Exit |
| T7BMK.DFM | BM-K | AVL/Spec-Book vendor cross-reference report — Standard Item# From/Thru, Parent Item# From, Customer Code From, Vendor Code From, Vendor Part#; **Sort By Vendor** toggle; **Auto Print Folder** path; dual role: BM-K (BOM Vendor BOM) AND MK-B (Marketing spec-book AVL report) |
| T7CMK.DFM | (bulk-copy) | Customer account bulk-copy — from.cust/thru.cust + class range; SHIPTO + SKIPR [S/R] (skip existing or replace) |
| T7SMK.DFM | **Evo User Settings** | **CORRECTION: T7SMK is NOT a campaign summary.** T7SMK = per-user preferences editor: Language selector, Default Print Path, Check for Reminders every X seconds, **Snooze All interval** (combo: 5 min / 10 min / 15 min / 30 min / 1 hr / 2 hr / 4 hr / 8 hr / 0.5 day / 1 day / 2 day / 3 day / 4 day / 1 week), Hot Button 1-3 (program + icon), Email Body + Signature; accessed from SM module settings |

**T7SMK correction:** Prior documentation identified T7SMK as "campaign summary."
The DFM confirms it is the **Evo User Settings** dialog — per-user preferences
for reminder intervals, hotkeys, email templates, and print paths. The actual
campaign summary is in T7MKA/MKTRACK territory.

## Integration

- **[[module-CM|CM]]** — Contact Master uses MK for campaign management and
  follow-up scheduling; BKCM* tables link to MKTRACK via the activity framework
- **[[module-GL|GL]]** — T7GLJ (bank reconciliation) opens MKTRACK
- **[[module-LI|LI]]** — LI logs access-grant events to MKAHIST (audit trail)
""",

"YS": """
## What it does

YN Flags Editor / One-Time Database Migration Utility — a privileged admin tool
that runs one-time data conversion and schema migration scripts against the live
Btrieve database. Program: `T7YSYN.RWN` (also `T7YSYN.DFM`).

**Confirmed from T7YSYN.RWN.dec strings** (Pass 499, 2026-07-01):
- Caption: `YS-YN  Utility to change settings`
- Author tag: `ISTS Enhancement 08/31/18` (last modified August 2018 by i2 Systems)

## Purpose

YS is a **run-once conversion utility** — each entry in its list is a one-time
database migration that should only be run once during system upgrades or data
repairs. Selecting an entry runs the corresponding conversion routine directly
against Btrieve (.B) files.

## Known conversion entries (from RWN strings)

| Entry label | What it does |
|-------------|--------------|
| Converted to Long Check # for AR | Migrates AR check numbers to long format |
| Direct Deposit Conversion | Converts payroll direct deposit data |
| Flag to clean ICLOC GLACCOUNTS | Cleans up item-class/location GL account fields |
| INIT ISBSF.Bxx Data | Initializes ISBSF (Business Scorecard) files |
| Bin Loc Util | Bin location data migration |
| SO line Loc Util | SO line location field migration |
| CC Encryption Util | Credit card number encryption conversion |
| ROHS Cleanup Util (IN-B) | Cleans RoHS compliance flags in IN-B |
| WO Materials (IN-B) | WO material reference migration in IN-B |
| Move POL GL Code to .GLA and .GLDPT | Migrates PO line GL code to new fields |
| Move next numbers to ISNUMB | Migrates auto-number sequences to ISNUMB table |
| Convert to Long Invoice # in AP | Migrates AP invoice numbers to long format |
| One time PR Encrypt Util | Payroll data encryption migration |
| BZ fix in update to BKBM.EXTRA | Fixes BZ (BOM) EXTRA field values |
| Convert Long Invoice 2 (missed BKISTAX) | Follow-up long invoice migration (tax table) |
| Left justify Invoice (AP) Numbers | Normalizes AP invoice number formatting |
| Sync ISPRMSTR with BKPRMSTR util | Synchronizes two PR master tables |
| SRINFO / SOINFO / QTINFO Util to move out of arrays | Migrates info fields from arrays to flat fields |
| SR Loc Util into MKAHIST | Moves SR location data to marketing history |
| Move Cycle code to .VEND[8] | Migrates cycle code into vendor array slot 8 |
| Util to move BANKS to ISBANKS | Migrates bank accounts to ISBANKS table |
| Move Invoiced to IType for SR/RMA | Sets IType flag on SR/RMA records |
| XCHARGE Conversion | X-Charge credit card processor conversion |
| PMAT Conversion to Start & End Dates | Migrates PMAT date fields |
| Convert CMACCT to CMCUST | Migrates CRM account to customer code |
| Update/Clean BKIC.PROD.GL | Cleans item-class product GL account fields |
| Cleanup BKIC.PROD.LONGP | Cleans long part number fields in BKIC |
| Flag to move Lot/Serial into BIN | Moves lot/serial data into BIN table structure |
| Notes/Links Format fix | Fixes EVONOTES format field |
| Convert EvoNotes to A6000 | Converts EvoNotes to new A6000 storage format |
| TERMS from EvoUTIL | Migrates payment terms from EvoUTIL |
| BKBMMSTR BZFix on PTYPE | Fixes PTYPE field on BOM master |
| EvoNOTES one CSN/CSH | EvoNotes CSN/CSH field consolidation |
| BKBMMSTR Unique ID fill | Fills unique IDs on BOM master records |
| WOBOM Unique ID Fill | Fills unique IDs on WO BOM records |
| Fill in APRIVL Blank Number | Populates blank AP Rivl (rival) numbers |
| Convert AP Contacts to APACCN | Migrates AP contacts to APACCN table |
| Fill in ISCC Processor with X Charge | Populates CC processor flag |
| Separate S/R and RMA data | Splits SR and RMA record types |
| SO Quote Status .Extra 96 | Sets quote status flags in Extra field byte 96 |
| PR Array to File | Converts payroll array data to file-based storage |

## Tables accessed

- `BKYSMSTR` (355f) — YS system master (flag storage for migration state)
- `BKSYHELP` / `DBAHLPID` — help system tables
- Most Btrieve tables (each conversion touches specific .B files)

## Integration

- **[[module-TA|TA]]** — YS accessed through admin/system maintenance area
- **[[module-SY|SY]]** — BKYSMSTR stores YS flags alongside SY system settings
- **[[module-AM|AM]]** — year-end processing is in AM-B, not YS

## CAUTION

Each entry runs once only. Running a conversion twice may corrupt data.
This tool is for ISTS/i2 Systems staff use only during system upgrades.
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

EvoNotes DFM suite fully confirmed (Pass 490, 2026-07-01):

| DFM | Caption | Function |
|-----|---------|----------|
| EvoNotes.DFM | Evo Notes | Main editor (LISTG60 grid): KILL(delete)/Contact/View Current/View Archive/Search toolbar; hints: Add New Note/Edit Note/Delete Note/Copy in a new Note/Select Note |
| EVOENOTES.DFM | Entering Notes | Per-entity popup entry: Date/Time/Who/Type/View/Alert/Notes for:/Contact/Save/Exit |
| EvoNoteSearch.DFM | Evo Notes Search | Full-text search: String to search for/Search Current-Archived-Both/Match Case |
| EvoNotesARCH.DFM | Evo Notes | Archive/Restore: Note Date From/Thru/Item# From/CM Customer From/Process/Settings |
| EvoNotesPrt.DFM | Evo Notes Selection | Print: Box 1–6 display areas/Note Types/Print Note Type(s)/Save Settings |
| EvoNotesRpt.DFM | Evo Notes | Report: Event Date From/Thru/Item#/CM Customer/Vendor/User Name ranges/Print/Settings |
| ENPM.DFM | Processing Memo… | Progress dialog during memo save |
| evoreminders.DFM | Evo Reminders | Reminder popup: ReminderMessage/Dismiss/Reschedule/Exit/Dismiss All/Snooze All |
| evorereminders.DFM | Reschedule | Snooze interval picker: "Remind me again in" + 14 items (5 min/10 min/15 min/30 min/1 hour/2 hours/4 hours/8 hours/0.5 days/1 day/2 days/3 days/4 days/1 week); matches T7SMK Snooze All interval list |
| classic2evonts.DFM | Classic 2 Evo Notes | Migration utility: converts pre-EvoNotes classic note records to new EvoNotes format |
| REMREM.DFM | Reminder... | Minimal reminder popup (legacy/alternate reminder dialog) |

## Links system (EvoLinks)

**ISLINKS — 4,196 records / 313 fields (ODBC confirmed)**

Attaches external files (PDFs, images, Office docs) to any EvoERP record.
The 313-field schema uses an `IS_LNK_TYPES_1..N` array for cross-module
type associations (one association field per module/record type pair).

Key fields: IS_LNK_UID, IS_LNK_LINK (file path/URL), IS_LNK_APP (open-with app),
IS_LNK_GLOBAL, IS_LNK_OPENWITH, IS_LNK_DATE, IS_LNK_NOTE (annotation),
IS_LNK_WHO, IS_LNK_ATYPE (attachment type), IS_LNK_PRIVATE, IS_LNK_SORT.

EvoLinks.DFM: viewer — KILL (delete), Image Preview, File, View Current/Archive, Links for:, ID2.
EvoELinks.DFM: entry form — Date, Who, Link, File, Sort#, **Use Global Path**, Image Preview,
Alert (per-link alert flag), Item Alert, View Only, **SDS** (Safety Data Sheet tag),
Printing (printable flag), Document Type — rich metadata per link.
EvoLinkCVT.DFM: "Evo Links CVT" — "Converting Image Links to Evo Links" migration progress.

`imageinfo.DFM` — attached image GPS viewer: File Name, Date, Time, **Latitude, Longitude**,
Get (reads EXIF GPS from file), Map button. Geotagged photos can be attached and mapped
directly from within EvoERP via EvoLinks.

## Reminders & Alerts

**ISREMIND — 0 records / 24 fields (not used at i2 Systems)**

evoreminders.DFM: pop-up panel — ReminderMessage, Dismiss, Reschedule,
Dismiss All, Snooze All. evorereminders.DFM: Snooze — "Remind me again in X [time unit]".
evoalerts.DFM: system broadcast alerts — AlertMessage, Ignore, View.
REMREM.DFM: minimal "Reminder..." popup (bare notification form).

`dayrem.DFM` — "Day Time Reminders" — full reminder entry form:
Time, Subject, Notes, Item, Cust, Vend, File/URL, Remind me X [unit] before this event,
Date, Type, Contact, Phone, Email Address, Add button.

**Calendar DFMs:**

| DFM | Caption / Purpose |
|-----|------------------|
| calDDsel.DFM | "Calendar Drill Down" — choose Drill Down Type: **Est. Receipt Date** or **Vendor Promise Date** — selects which PO date field the calendar drills on |
| caldrillbt.DFM | Calendar grid (Sun-Sat week view) with Previous/Next navigation |
| CALDRILL.DFM | Calendar grid variant (no navigation buttons) |
| calrem.DFM | Calendar with Previous/Next/Print/Today/**Export to Google Calendar**/Closed — the reminders calendar with Google Calendar integration |
| CALREMGC.DFM | Google Calendar export dialog: Event Date From/Thru, Export Reminders filter (All / Open Only / Dismissed Only), Export button |
| CALGRIDDRILL.DFM | "Calendar Drill Downs" — grid of scheduled items for the selected day |

The **Google Calendar export** (`calrem.DFM + CALREMGC.DFM`) allows EvoERP reminders
to be pushed to a user's Google Calendar as events. Filter: export all, only open, or
only dismissed reminders within a date range.

## ERP Scheduler

`EvoScheduler.DFM` — task configuration grid; each scheduled task has:
Name, Description, Program (RWN to run), Params, Log File, Company, E-Mail
(recipient for completion notification), Occuring (schedule type), Type,
Next Date, Next Time, Reoccur Every X Minutes, Last Date, Last Time.

`evoERPsched.DFM`: "Run at time" + "Schedule Every" + day-of-week checkboxes.

Service installation forms (all share same SMTP setup UI):
- `EvoSchedsetup.DFM` — "Create Evo Scheduler as a Service" (Windows service)
- `EVOSERVICESETUP.DFM` — "Create EvoService for your Server" (the EVO background service)
- `EVOSERVICEREMOVE.DFM` — "Remove EvoService from your Server"
- `EvoMobilesetup.DFM` — "Create Mobile Reminders Setup" (pushes reminders to mobile)

All service-install forms share: Server Path (g:\path), SMTP, User, Passwd, Port,
Email, Name, 32/64-bit OS selector, Continue and TestEmail buttons.

## Business Status dashboard (EvoBS)

Three-panel executive dashboard accessed from the main menu toolbar:

| DFM | Fields confirmed by scan |
|-----|--------------------------|
| T7BS.DFM (= EvoBS) | **Status** date; **AR:** Current Balance / Billings / Receipts / Discounts / COGS / Deposits; **AP:** Payables / Payments / Approved to Pay; **SO:** Open Orders / Booked Orders / **Shipments**; **PO** + **WO** drill-down sections (click-to-drill hints confirmed) |
| T7BSCash.DFM (= EvoBSCash) | Cash / Balance — bank account cash detail (drill-down from main BS) |
| T7BSWO.DFM (= EvoBSWO) | **Work Orders** section: FP/Variances (Finished Production / Variance) / Issues / WIP Balance / Labor / Materials & Process / Fixed Overhead / Variable Overhead / Misc. Extra; Back button |
| T7BSR.DFM (= EvoBSR) | **Business Status Rebuild** — "Initializing..." progress; rebuilds/recalculates BS aggregates |

**T7BS hint strings confirm 5 drill-down sections:** "Click to Drill Down to Accounts
Receivables" / "…Payables" / "…Sales Orders" / "…Purchase Orders" / "…Work Orders" —
the BS dashboard is fully clickable to module-level detail.

**Backing tables confirmed from EVO3.JAR class catalog (Pass 501, 2026-07-01):**

| Table | Fields | Role |
|-------|--------|------|
| ISBSF | 143 | Company-level Business Scorecard aggregates |
| ISJBSF | 143 | Job/division-level scorecard — same field structure as ISBSF |

ISBSF field groups (EVO3.JAR, 143 total):

| Group | Count | Fields |
|-------|-------|--------|
| Root | 3 | ISBSF_STARTDATE, ISBSF_ENDDATE, ISBSF_EXTRA |
| AP | 5 | ISBSF_AP_ATP (approved-to-pay), ISBSF_AP_BAL, ISBSF_AP_DISC, ISBSF_AP_PAYA, ISBSF_AP_PAYM |
| AR | 6 | ISBSF_AR_BAL, ISBSF_AR_BILL, ISBSF_AR_COGS, ISBSF_AR_DEPO, ISBSF_AR_DISC, ISBSF_AR_RECP |
| CASH | 110 | ISBSF_CASH_ACT1..9 (9 named accounts) + ISBSF_CASH_ACTS_1..100 (100-slot sub-account array) |
| IC | 1 | ISBSF_IC_VALUE (inventory value snapshot) |
| PO | 3 | ISBSF_PO_BOOK, ISBSF_PO_OPEN, ISBSF_PO_RECP |
| SO | 3 | ISBSF_SO_BOOK, ISBSF_SO_OPEN, ISBSF_SO_SHIP |
| WO | 3 | ISBSF_WO_FPVAR (FP variance), ISBSF_WO_ISSU (issues), ISBSF_WO_WIPBAL |
| WOS | 9 | ISBSF_WOS_FOH, ISBSF_WOS_FP, ISBSF_WOS_LAB, ISBSF_WOS_MAT, ISBSF_WOS_MEXT, ISBSF_WOS_OUTP, ISBSF_WOS_SETUP, ISBSF_WOS_VOH, ISBSF_WOS_WIPV |

T7BSR.DFM ("Business Status Rebuild") repopulates ISBSF/ISJBSF from live transactional tables
(BKARINV, BKARCUST, WORKORD, etc.); the dashboard reads the pre-computed aggregates, not live data.
The 100-slot CASH_ACTS array accommodates an unlimited number of GL cash accounts mapped to the
T7BSCash.DFM bank account drill-down.

## Master Inquiry (EvoCSI)

`EvoCSI.DFM` — "Evo Master Inquiry" — cross-module lookup by any of these key types:
Customer Code, Item Number, SO Number, Invoice Number, Vendor Code, PO Receipts,
PO Number, WO Number. Resolves "where does this number appear?" across all modules.
Eight lookup dimensions confirmed from DFM scan.

## Password management

| DFM | Purpose |
|-----|---------|
| Evopass.DFM | Login password prompt |
| EVOUPASS.DFM | User + password entry |
| EVOCHANGEPASS.DFM | Change password |
| EVORESETPASS.DFM | Reset password — User Name, New Password, Reenter Password |

## EvoERP Update System (Pass 491, 2026-07-01)

**Distribution staging**: `\\i2s109-solidcrm\evo-ERP\ISTS\` is the master workstation
install image. Robocopy deploys it to `C:\ISTS\` on each workstation. It contains all
client executables plus zip utilities and UPDTP7.EXE.

**Update workflow — 3 programs, DFM-confirmed:**

| DFM | Caption | Role |
|-----|---------|------|
| EvoUPDsetup.DFM | Create Update Setup | Developer: specify Server Path → builds update package |
| EvoERPupd.DFM | Evo ~ ERP Update | User: Initialize / Files-in-Update / Files-to-Force tabs / Update+Go |
| EvoForceUpd.DFM | Evo ~ ERP Force Update | Same as above with force-update as default |
| EVOERPUPDW.DFM | Archive Work Orders | WO archival utility (NOT an ERP update) — archive Closed WOs as-of date |

**Key binaries in distribution** (confirmed from `evo-ERP\ISTS\`):
- `UPDTP7.EXE` (86KB) — TAS Pro 7 file updater; called via `EXEC_TOP_WAIT` from EvoERPupd
- `unzdll.dll` + `zipdll.dll` — ZIP/UNZIP for in-app update package decompression
- `robocopy.exe` — bundled for workstation deployment
- `fileloc.zip` (1.7MB in `evo-ERP\`) — distributed FILELOC table update package

**EvoUPDsetup fields** (DFM): Server Path (placeholder `g:\path`) + Creating label + Continue.
**EvoERPupd fields** (DFM): Initialize checkbox → FD Name + FileName per file (FILELOC-style
registration) → "Files in this Update" tab + "Files to Force" tab → Update+Go.
**CheckForUpdates** in `EvoSettings.INI [Users]` section controls whether the client
auto-checks for an available update at startup (default `.F.` = disabled).

**Per-workstation config files** (`C:\ISTS\`):
- `EvoSettings.INI` — per-user EVO prefs: Toolbar/OpenList mode flags, Language, Sounds,
  DefPrintPath, Reminder/Notification/RemSeconds/RemSnoozeAll, QuickPrint,
  CheckForUpdates; per-module screen (EvoorClassicScreen E/C); HOT BUTTONS 1-6
- `taspro7.INI` (deployed: 127 bytes) — minimal: UseBtrvMemos=1, LimitRuntime=1,
  HelpFileName=`\\i2s109-solidcrm\DBAMFG$\EvoHELP.CHM`
- `WHOAMI.DBA` (9 bytes) — last login: "NON EVO" if no user logged in; otherwise
  `<user> <time> <date>` (e.g., "CWILLIAMS      11:00:53 A20171019")
- `BMB.CFG` (56 bytes) — Pervasive PSQL workstation license key (V2355B-28BBE pattern)
- `CHMHELP.EVO` (35 bytes) — marker file: "EvoHELP now set for this computer"

**Developer source layout** (from `taspro7.ini` in outer distribution):
- Source files: `F:\Projects\TAS\istech\` (developer machine, F: drive)
- Old server: `\\2kserver\c\DBAMFG\` (Windows 2000-era predecessor to i2s109-solidcrm)
- Dev DataDictPath: `E:\DBAMFG\` (developer's local drive mapping)

## Maintenance tools

| DFM | Purpose |
|-----|---------|
| Evocnvtb.DFM | Synchronize Data Dictionary with Btrieve — rebuilds DDF from live .B files |
| EvoERPbackup.DFM | Backup utility: file types, zip file name, Backup Type |
| EvoERPDrillM.DFM | Drill-down menu editor: Source Field, Target Field, Menu Text, Key |
| EVOFUP.DFM | Upload files to ISTS tech support: Select Tech, zip, Your Name |
| EVOSERVICESETUP.DFM | Create EvoService Windows service (SMTP, Server Path) |
| EvocfgSave.DFM | Save/Restore Evo Service Settings |
| EVOFILTERS.DFM | WO filter panel (WO#/Finished Date/Status) — shared across SH/WO/PA |

## Email system (NZE)

`nzemailtll.DFM` — "Evo ~ ERP email" — the universal email compose dialog:
To, Cc, Icc (internal CC), BCC Self toggle, Form (report template), Attachment (&Att:),
Subject, Send, Cancel. Used whenever EvoERP sends an email (invoices, packing slips,
acknowledgements, etc.).

`nzedefs.DFM` — "Evo Email Default Settings": Attach (default attachment flag),
Signature, Body Text, BCC Self, Subject, Subject Fields — configures the default
template for each outbound document type.

## Print dialog (shared across all modules)

`printtll.DFM` — "Print" — the standard EvoERP print routing dialog:
- Number of Copies
- Print Options: Printer / Preview / Email / File
- Printer: Name, Setup, Print to File, Type, Where
- Save Settings, Exit

All EvoERP reports and documents reach this dialog before output.

## Calendar Summary Report

`EvoCSR.DFM` — "Calendar Summary Report" — cross-order scheduling summary:
Month (to display), Customer From/Thru, Item From/Thru, ESD (Estimated Ship Date),
CDD (Customer Due Date), Report Fields (Customer and PO#; Qty and Backorder;
SO# and Customer). Used to view open SO delivery commitments by calendar period.

## UI customization tools

| DFM | Purpose |
|-----|---------|
| DFMALTS.DFM | "Set ALT Keys for DFMs" — maps keyboard shortcuts to form fields |
| DDFilters.DFM | "Drill Filters" — Apply/Edit/Delete/Save/Load/Clear/Sort; manages persistent drill-down filter sets |
| EvoERPDrillM.DFM | "Drill Down Menus" — Source Field, Target Field, Menu Text, Key, File, Child/Parent Grid; configures cross-record navigation |
| classic2evonts.DFM | "Classic 2 Evo Notes" — migrates legacy note records to the ISNOTES format |

## UDF (User Defined Field) editors

`udfedit.DFM` through `udfedit5.DFM` — six "Enter Value" dialogs, one per UDF
data type/length. When a user edits a UDF field in any EvoERP form, the appropriate
udfedit variant pops up based on the field's type. Caption is just "Enter Value" for
all six — the difference is in the underlying component type (text, numeric, date, memo).

## Saved Search/Sort/Filter (SSS)

`SSS.DFM` = "Drill Filters" — the persistent filter manager linked to the SSSFD button
in WBKLOOKUP. `SSSFD.DFM` = "Sub String Search" with Clear and Evo Notes buttons —
the free-text substring search panel within the lookup engine.

## Image/photo viewer

`imageinfo.DFM` — "New Screen" — displays photo metadata: File Name, Date, Time,
**Latitude, Longitude**, Get, Map button. EvoERP can display GPS coordinates from
geotagged images attached via EvoLinks. Map button presumably opens a map viewer.
`Imageprint.DFM` — "Printing Linked Documents" — progress dialog for printing linked files.

## TAS Premier 7i native charts (non-Java)

TAS Premier 7i has built-in chart rendering (not requiring the Java EvoPVT.jar):

| DFM | Caption | Series |
|-----|---------|--------|
| chartBarModal.DFM | "Bar Chart Values & Captions" | 3 series with color, Values/Label/Caption |
| chartLineModal.DFM | "Line Chart Values & Captions" | 2 series + Point Labels |
| ChartPieModal.DFM | "Pie Chart Values & Captions" | 1 series + Labels + Caption |
| ChartDemo.DFM | "Addsum TAS 7i Chart Demo Program" | Bar chart type / Format / Enter Values / Print |

These are TAS 7i's own VCL chart dialogs — independent of the Java BI layer.

## WO-related utilities

`ACT7SHKNOTE.DFM` — WO sequence note entry: WO Number, Sequence, Note, Save, Exit.
Used to attach free-text notes to individual WO operations (sequence steps).

`EVOERPUPDW.DFM` — "Archive Work Orders" — Archive Closed WO as of [date]. Despite
the EVOERPUPD prefix (suggesting an update), this is a WO archiving tool.

## T6 → T7 migration tools

| DFM | Purpose |
|-----|---------|
| T6MENUUTIL.DFM | "Evo ~ ERP T6 Program Names" — remap T6 program names to T7 equivalents |
| dbamenu_LOGIN.Dfm | DBA Manufacturing era login form (pre-EvoERP, no caption) |
| dbamenu_SELCOMP.Dfm | DBA Manufacturing company selector (pre-EvoERP, no caption) |
| ht6close.DFM | T6 WO close confirmation dialog |
| ht6inc.DFM | T6 receiving dialog (Item, Qty, Process) |
| ht6so.DFM | T6 Sales Order creation (PO#, Item, Desc, Qty) |
| ht6wo.DFM | T6 Work Orders viewer (Start, End) |

These T6-era forms are still present on the share but are not invoked in normal T7/EvoERP operation.

## Email server config

`EMAILREL4.DFM` — another SMTP configuration form (SMTP, Email, Name, Port, TestEmail) —
appears to be a legacy/alternate email setup path.

## Data Collection workstation menu

`EvoDCmenu.DFM` = "Data Collection Menu" with Prog1–9 + Main/Exit/Settings/Help buttons.
`EvoDCmenu2.DFM` = DC Menu with Main/Exit/Settings/Help/About.
`EvoDCsetup.DFM` / `Evowkssetup.DFM` = "Create Workstation Setup" — Server Path,
Date Format (dd/mm/yy or mm/dd/yy selector), Continue.
`EVODCS.DFM` = DC screen (dynamic, no caption).

## Brands (BR) — DFM-confirmed 2026-07-01

**T7BRANDS.DFM** (caption "New Screen"): Code / Description fields; Add/Save/Delete/Exit/
**Back** toolbar; Hint "Back to the List of links" (same hierarchy-navigation pattern as FIB).

| Table | Fields | Purpose |
|-------|--------|---------|
| `BKCMACCC` | 2 | Brand code master — CCODE str5 / DESC str25 |
| `BKCMACCN` | 154 | Account notes with up to 10 contacts per account |
| `ISBROKER` | 4 | Broker commission table — ISIS_BRK_CODE str10 / FLAT float / PERC float / TYPE str1 |

**T7BROWSER.RWN** (4 procs, 55-table session-init overhead, 0 named vars) = the main
brand browser; uses BKCMACCN+BKCMACCC as business tables; ISPOSI.H = POS terminal
integration confirms brands appear in point-of-sale context.

## Reporting Bridges (JS) — DFM-confirmed 2026-07-01

7 Java export bridge launchers (all LISTG60, all confirmed by DFM scan):

| DFM | Bridge | Purpose |
|-----|--------|---------|
| T7JSACC.DFM | ACC | Accounting data export to Java/BI |
| T7JSAIC.DFM | AIC | Inventory & Cost export |
| T7JSAPBI.DFM | APBI | **Power BI** export — confirms Power BI integration |
| T7JSASRS.DFM | ASRS | SRS (SQL Server Reporting Services?) export |
| T7JSOI.DFM | OI | Order Inquiry export |
| T7JSQL.DFM | SQL | SQL/generic export + Destination field |
| T7JSettings.DFM | (settings) | Java bridge settings utility: Host/Port/Name/DSN; **Detect Settings** (auto-discover); **Test Settings**; **Generate Program** (builds a new TAS bridge program from template) |

All launchers share identical UI: Host / Port / Name / Company DSN Settings / Save / Go.
T7JODPSALES.DFM reuses the T7Jtree.DFM layout (tree-based job sales query bridge).

## Rebuild Utilities (RE) — DFM-confirmed 2026-07-01

| DFM | Caption | Purpose |
|-----|---------|---------|
| T7REBQC.DFM | Recalculate QC Qty | Recalculates QC on-hand quantities — Tag Items; Item Range; From Through Range selection |
| T7REBSS.DFM | Rebuilding Stock Status | Rebuilds inventory stock status aggregate (progress display) |
| t7rebwo.DFM | New Screen | Rebuild Work Order data — WO#/Job#/Item#/Status [SFRICX]; Active(A) or Archive(D) |
| T7REINDEX.DFM | New Screen | Per-file reindex utility — Tag/Untag/Tag All/Untag All by File Name; Reindex Tagged |
| t7redindexDD.DFM | Reindex Data Dictionary | Reindexes DDF tables: File Dict / File Loc / File Key / File Key Num / File DBF / Menu tabs |
| t7ResetDFM.DFM | Reset DFM Settings | Resets user DFM customizations to defaults; "Resetting DFM" progress |
| T7RemindRpt.DFM | CM-B-D | Reminder report — Event Date / Item# / Customer / Type ranges; Open/Dismissed/Both filter |
| T7REPDEF.DFM | New Screen | Sales Rep definition maintenance — Label / Title; Add/Save/Delete |
| T7REPLNK.DFM | New Screen | Sales Rep item-customer link — Rep# / Item# / Customer / Item Class; Sort By |
| T7REPLNK1.DFM | New Screen | Rep link with Commission Rate — adds Commission Rate field to T7REPLNK |

**REPDEF/REPLNK/REPLNK1** are Sales Rep commission structure programs (not reminder-related
despite the T7RE* prefix). T7REPLNK1 confirms per-link commission rate overrides exist.

## Field Information Base (FS) — DFM-confirmed 2026-07-01

FIB is a 3-level hierarchy: Class → Program → Info+Employee.

| DFM | Caption | Fields | Purpose |
|-----|---------|--------|---------|
| T7FSCLASS.DFM | New Screen | Class / Description | Class maintenance — BKFIBCLASS or ISFIBCL table |
| T7FSEMP.DFM | New Screen | Rep # / Market Segment | Employee/Rep assignment — sales territory dimension |
| T7FSINFO.DFM | New Screen | Contract / Program / Who | Info record maintenance — the bottom-level FIB record |

All 3 DFMs share Add/Save/Delete/Exit/**Back** toolbar with "Back to the List of links" hint
(Back navigates up one level in the FIB hierarchy).
ISTS.EDATE = LGS integration confirmed (FIB connects to LGS garment shipping schedule).
FIB Class is also tied to DFM form names (T7FSCLASS reads DFM.H/DFM_CAPTION/DFM_NAME/DFM_OBJNAME)
suggesting FIB classes correspond to EvoERP form identifiers.
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

## T7LGS* — LGS Custom Shipping Programs (3 DFMs confirmed, 2026-07-01)

These T7LGS-prefixed programs are ISTS-authored customizations for a
garment/apparel industry customer (LGS = Lapco Garment Systems or similar).
They follow the same scan-based shipping workflow as the J7DCSSOE/J7HHPTSSOE
mattress variants, but for garment shipments.

| DFM | Caption | Key fields |
|-----|---------|-----------|
| T7LGSSOE.DFM | Shipping | Customer Name / Item Num / Item Code / Item Description / Last Item Scanned / Quantity / Qty / UM — scan-based shipment confirmation |
| T7LGSSOEVerify.DFM | Sales Orders | Grid (ETBcomboval); Exit / Label / List actions — verification step after scanning |
| t7LGssoeLabels.DFM | Print Box Content Labels | RTM template / Print Lot Numbers / Print Serial Numbers checkboxes / Label Qty / Print / Exit — box content label printing |

**Workflow:** Scan items via T7LGSSOE → verify SO lines via T7LGSSOEVerify
→ print box labels via t7LGssoeLabels. Parallel to J7DCSSOE/J7DCSSOEVERIFY/
J7HHPTSSOELABELS for mattress production.

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

"NE": """
## What it does

New Company / Data File Initializer — checks whether required Btrieve data files
are missing and creates them. Used when setting up a new company code or recovering
from missing-file errors. Single T7 program.

## DFM confirmed (T7NEWINIT.DFM, 2026-07-01)

- Caption: "This program will check and see if you are missing any data file"
- Buttons: **Go** (run the check/create) + **Exit**
- No input fields — reads FILELOC registry and creates missing `.B` files

## Context

`T7NEWINIT.RWN` — runs after `UT-I Create/Delete Company` (which sets up FILELOC
routing records) to ensure all blank data files exist. Also used as a repair tool
when a data file is accidentally deleted. One variable, zero DB tables (it creates
files, not records).

## Integration

- **[[module-UT|UT]]** — UT-I creates the company structure; NE initializes files
- **[[module-FL|FL]]** — reads FILELOC to know which files to check/create

## DFM-confirmed (T7NEWINIT.DFM, Pass 520)
Caption: "New Screen"
Fields: **Go** + **Exit** only — no user input required.
Single-operation utility. Clicking Go triggers the new company file initialization
sequence for the current company (creates required Btrieve files if missing).
The simplicity of the DFM confirms NE is a one-shot bootstrap, not an interactive
data entry form.
""",

"EM": """
## What it does

Emergency GL — a utility for creating or editing GL account link records when
normal GL posting fails or when emergency manual GL corrections are needed.
Not a standard transaction module — used by accountants/admins to fix GL mappings.

## DFM confirmed (T7EMGL.DFM, 2026-07-01)

Caption: **"GL Account Link"**

| Field/Button | Purpose |
|---|---|
| Account | GL account number |
| &Add | Add a new GL account link record |
| &Save | Save the current record |
| &Delete | Delete the current link |
| &Back | Back to the list of links |
| E&xit | Exit |

The "Back to the List of links" hint (from `hints`) confirms EM is a list/detail
editor for GL account link records (probably `BKGL.*` namespace).

## Key namespace (from variable analysis, Pass185)

`BKGL.*` 14-var namespace: ACCT/KEY/GLDPT/ACCTD/TYP + others — the GL account
master fields used by EM to build/repair GL account-to-department links.

## Integration

- **[[module-GL|GL]]** — EM repairs GL account links that SM or standard modules write
- **[[module-SM|SM]]** — SM-A Enter Chart of Accounts is the normal path; EM is the break-glass tool
""",

"PA": """
## What it does

Paperless DC — the shop-floor paperless manufacturing workstation. Displays WO
traveler, BOM components, routing notes, QC specs, and customer/vendor notes on a
touchscreen terminal without printing. The operator can enter production and labor
directly from the form. Separate from but related to DC-PSF (HH-L).

## DFMs confirmed (3 DFMs, 2026-07-01)

| DFM | Caption | Purpose |
|-----|---------|---------|
| `T7Paperless.DFM` | **Paperless Shop Floor** | Main workstation form — WO#/Sequence/Item No; keyboard shortcuts: F9=WO Login, F2=Production Only, F3=Labor Only, F4=Transfer Label, F7=Notes; **Item Alerts** + **Archives** + **Refresh** buttons |
| `t7packmenu.DFM` | **Pack Menu** | Pack workstation admin — **Menu** / **Grids** / **Reindex** / E&xit tabs |
| `T7PASS.DFM` | **Password** | Simple password entry dialog ("Password :") — used for workstation authentication |

## T7Paperless vs T7DCPSF

| Feature | T7Paperless (PA) | T7DCPSF (DC-PSF / HH-L) |
|---------|------------------|--------------------------|
| Caption | "Paperless Shop Floor" | "HH-L Paperless Shop Floor" |
| Item Alerts button | Yes | Not shown |
| Archives button | Yes | Not shown |
| Refresh button | Yes | Not shown |
| Context | PA standalone workstation | DC/HH module dual-access |

T7Paperless appears to be the independent PA-module variant; T7DCPSF is the version
accessed from both DC and HH menus.

## Integration

- **[[module-DC|DC]]** — DC-PSF (T7DCPSF) is a related but separate form; both display
  shop floor data
- **[[module-HH|HH]]** — HH-L uses T7DCPSF; PA module uses T7Paperless
- **[[module-WO|WO]]** — reads WORKORD/WOBOM/WORO for WO traveler display

## DFM-confirmed: T7Paperless.DFM WO queue columns (Pass 519)
The Paperless Shop Floor grid displays one row per open WO with these columns:
Sequence / WO Number / Item No / Desc / Job No / Drawing / Start Dt / Qty to Make /
Cust Code / Name / PO Number / Sales Order No / Contact / Priority / Change Ord No /
Rev / Fin Dt / UM / Operation

**Toolbar actions (keyboard shortcuts):**
| Action | Key |
|--------|-----|
| WO Login | F9 |
| Enter Production Only | F2 |
| Enter Labor Only | F3 |
| Enter Labor/Production | (both) |
| Print Transfer Label | F4 |
| Issue Components | — |
| Notes | F7 |
| Links | F8 |
| Item Alerts | button |
| Archives | button |
| Refresh | button |
""",

"AL": """
## What it does

Audit Log + Alt Part — a dual-purpose module covering:
1. **Alternate Part lookup/management** — maintains bidirectional alternate part
   number cross-references for inventory items
2. **Auto-Login setup** — configures workstation auto-login credentials (AL-Log)
3. **Alert notifications** — displays EvoERP system alert messages to users

## DFMs confirmed (3 DFMs, 2026-07-01)

| DFM | Caption | Purpose |
|-----|---------|---------|
| `T7ALTPART.DFM` | **Alternate Part** | Part Number entry + "Create the Inverse of this Part Number/Alternate Part Record" option + **Related Parts** button |
| `T7ALOGSETUP.DFM` | (New Screen) | **Enable/Disable Auto Login** — User Name / Password / Status / &Enable Auto Login / &Disable Auto Login buttons |
| `T7ALERTMSG.DFM` | **ALERT NOTIFICATION** | Simple popup: AlertMsgLabel + &OK |

## Key variable (SAVE.BOTH.WAYS, confirmed)

T7ALTPART uses a `SAVE.BOTH.WAYS` variable to control bidirectional alternate-part
creation: when enabled, creating Part A → Alt B automatically creates the inverse
record (Alt B → Part A). The DFM confirms: "Create the Inverse of this Part Number/
Alternate Part Record as" checkbox.

## Integration

- **[[module-IN|IN]]** — alternate parts feed BOM substitution lookup
- **[[module-PS|PS]]** — PS-A user management; AL auto-login stores workstation credentials
- **[[module-EVO|EVO]]** — Alert notifications (T7ALERTMSG) are dispatched system-wide
""",

"SE": """
## What it does

Service Events / Service Code Tables — maintains lookup codes for the service
quality tracking system (error codes, procedure codes, service types) and logs
service error events keyed to WO + operation. Related to QC/SR quality workflows.

## DFMs confirmed (4 DFMs, 2026-07-01)

| DFM | Caption | Fields |
|-----|---------|--------|
| `T7SETYPE.DFM` | New Screen | **Type** field + Add/Save/Delete toolbar |
| `T7SEPROC.DFM` | New Screen | **Type** field + Add/Save/Delete toolbar |
| `T7SERR.DFM` | New Screen | **Type** field + Add/Save/Delete toolbar |
| `T7SELLOC.DFM` | **Selection Locations** | Tag All / Untag All / **Include Segregated Locations** / Settings / Go |

The first three are simple code-table editors (one "Type" field = code + description).
T7SELLOC is a multi-select location picker used cross-module.

## Database tables (ODBC confirmed, 2026-07-01)

| Table | Fields | Records | Purpose |
|-------|--------|--------:|---------|
| `ISSETYPE` | 2 | 0 | Service type codes (IS_SETYPE_ERR / IS_SETYPE_WHO) |
| `ISSEPROC` | 2 | 0 | Procedure codes (IS_SEPROC_PROC / IS_SEPROC_WHO) |
| `ISSERR` | 17 | 0 | **Service error event log** — full WO event record |

### ISSERR — Service Error Event (17 fields)

| Field | Meaning |
|-------|---------|
| `IS_SERR_WOPRE` / `IS_SERR_WOSUF` | Work order prefix + suffix |
| `IS_SERR_OPER` | Routing operation number |
| `IS_SERR_TIME` / `IS_SERR_DATE` | Time/date of error event |
| `IS_SERR_ERROR` | Error type code (→ ISSETYPE) |
| `IS_SERR_PROCESS` | Procedure code (→ ISSEPROC) |
| `IS_SERR_COUNT` | Error count |
| `IS_SERR_REF` | Reference (ticket/batch#) |
| `IS_SERR_EXTRA` | Extra/free-text |
| `IS_SERR_DOF` | Date of failure |
| `IS_SERR_DIAG` | Diagnosis |
| `IS_SERR_REWORK` | Rework required |
| `IS_SERR_SERIAL` | Serial number |
| `IS_SERR_ADOF` | Actual date of failure |
| `IS_SERR_ADIAG` | Actual diagnosis |
| `IS_SERR_AREWORK` | Actual rework |

**At i2 Systems all SE tables have 0 records** — the SE service-error tracking
feature is not in active use.

## Integration

- **[[module-SR|SR]]** — SR Service Repair uses SE type/proc codes for service tickets
- **[[module-QC|QC]]** — QC quality events may reference SE error codes
""",

"CH": """
## What it does

Auto-Chain Configuration (also "Multi-Location Chain") — the PS-H utility for
defining program chains. A "chain" automatically launches a child program after
a parent program completes, allowing multi-step workflows to run without manual
navigation. Per-user chains are supported.

## DFMs confirmed (3 DFMs, 2026-07-01)

| DFM | Caption | Key fields |
|-----|---------|-----------|
| `T7Chain.DFM` | **Chain List** | User Name / Auto Chain [Y/N/Ask] / Add+Edit+Delete+Back+Save+Exit |
| `T7CHAINM.DFM` | **Chain Master** | **Child Program** / **Parent Program** / Auto Chain [Y/N/Ask] / Description; program list includes T6SOA/T7SOA/T6SOC/T7SOC... |
| `T7CHARGBK.DFM` | New Screen | Save / Exit (minimal — may be a charge-back form) |

T7CHAINM programs list confirms chains are set up for SO sub-programs (T6SOA/T7SOA,
T6SOC/T7SOC, T6SOD/T7SOD, T6SOE/T7SOE, T6SOF/T7SOF...) — both T6 and T7 variants
are chainable.

## Database tables (ODBC confirmed, 2026-07-01)

| Table | Fields | Records | Purpose |
|-------|--------|--------:|---------|
| `ISCHAIN` | 17 | 0 | Chain definitions |
| `ISCHAINM` | 17 | 0 | Chain master (same schema) |

**ISCHAIN / ISCHAINM — 17 fields:**
IS_CHAIN_USER / IS_CHAIN_PARENT / IS_CHAIN_CHILD / IS_CHAIN_PARAM_1..10 /
IS_CHAIN_AUTO / IS_CHAIN_DATE / IS_CHAIN_DESC / IS_CHAIN_EXTRA

- `USER` = user name (blank = applies to all users)
- `PARENT` = parent program code (e.g. "T7SOA")
- `CHILD` = child program code to launch after parent exits
- `PARAM_1..10` = up to 10 parameter strings passed to child program
- `AUTO` = Y/N/Ask (auto-launch without prompt, or ask first)

**At i2 Systems both tables have 0 records** — no auto-chains configured.

## Integration

- **[[module-PS|PS]]** — PS-H "Configure Auto-Chain Programs" is the menu entry for CH
- **[[module-SO|SO]]** — SO sub-programs are the most common chain target

## DFM-confirmed: T7CHAINM.DFM program list (Pass 519)
The Child Program and Parent Program dropdowns include these chainable programs:
`T6SOA` / `T7SOA` / `T6SOC` / `T7SOC` / `T6SOD` / `T7SOD` / `T6SOE` / `T7SOE` /
`T6SOF` / `T7SOF` / `T7WOA` / `*T6POA` / `*T7POA` / `*T6POB` / `*T6POR` /
`T7ARA` / `*T7APA` / `T7SON` / `ACHHSSOE`

The `*` prefix appears on PO and AP programs — possibly indicating optional/conditional
chain targets. `ACHHSSOE` is an i2-specific ACH/SSO entry point, confirming the chain
system is also used for ACH integration hooks.
""",

"ML": """
## What it does

Multi-Language — a DFM-based UI localization system that allows EvoERP forms to
be displayed in languages other than English. The ML module generates string
extraction files from DFMs and provides a caption editor for translators.

## DFMs confirmed (2 DFMs, 2026-07-01)

| DFM | Caption | Purpose |
|-----|---------|---------|
| `T7MLC.DFM` | **DFM Multi Language Generator / Editor** | DFM Name input / Generate (extract strings) / Edit / Add Lang / Delete / Select a Language to Delete |
| `T7MLE.DFM` | **Edit Captions** | Select a Language dropdown / Default Caption (original) / Translated Caption (localized); navigation: First/Prev/List/Next/Last |

## Workflow

```
T7MLC: DFM Name → Generate → creates string table for that DFM
T7MLC: Add Lang → registers a new language (e.g. "Español")
T7MLE: Select Language → Default Caption ↔ Translated Caption editor
       Navigate First/Prev/List/Next/Last through all strings
Runtime: EVO loads translated captions at startup per user's language setting
```

## Key table link

T7MLC is confirmed to use `BKEDMSTR` in its DB (from Pass181 analysis) — the same
EDI config table. This may be incidental (shared runtime library) or `BKEDMSTR`
holds a multi-language flag.

**At i2 Systems:** Multi-language is not in use — single-language (English) install.

## Integration

- **[[module-DE|DE]]** — DE/EDI shares `BKEDMSTR`; ML reads it for its own config
- **[[module-SM|SM]]** — SM-R Multi Language Maintenance is the user-accessible setup path: create language code → select DFM → Generate string table → edit translations in T7MLE. See SM-R documentation (Pass 518) for full workflow.
""",

"KI": """
## What it does

Kit Assembly (`T7KIT.RWN`) — a tablet-optimized stockroom picking tool that lets
a worker pull BOM components for a Work Order into a temporary holding file before
they are formally issued. A supervisor can review the kit before the final material
post reduces on-hand inventory.

Also accessible via the Work Orders menu as WO-K-I (Kitting System).

## Workflow (EVOHELP.PDF §WO-K-I, Pass 514)

```
Enter WO# + Employee ID
  → WO BOM displayed, first component highlighted
  → For each component:
      suggested qty = min(required qty, on-hand qty)
      Click Select → accept or override quantity
      If on-hand discrepancy detected → flag for physical count (sets Cycle Code = KIT)
  → Click Save → transactions staged to temporary file
  → On-hand NOT reduced yet; allocations NOT satisfied yet
  → Supervisor reviews kit
  → Edit/Post Material Issues → final post reduces on-hand
```

## Key fields and behavior

- **WO#**: work order to be kitted
- **Employee ID**: picker's employee ID (for audit trail)
- **Suggested Qty**: minimum of BOM required qty and current on-hand — helps picker know the shortfall immediately
- **Cycle Code = KIT**: set on items where a discrepancy is detected; flags item for inventory control to recount
- **Temporary holding file**: until "Edit/Post Material Issues" is run, on-hand qty and allocations are unchanged — the kit staging does not affect inventory balance

## Database tables (from Pass183/208)

| Table | Fields | Purpose |
|-------|--------|---------|
| `WOBOM` | 39 | WO bill-of-material — BOM snapshot for the WO being kitted |
| `WOMAT` | 21 | WO material issue staging — the "temporary holding file" |
| `MTLOT` | 22 | Lot transaction staging (for lot-controlled kitted items) |
| `ISBNMSTR` | — | Bin labels master — for multi-bin stockroom bin identification |
| `ISBIN.LOC.*` | 9 vars | Bin location namespace accessed during picking |

**WOBOM** (32-var namespace): WOPRE/WOSUF/SEQ/COMP/DESC/QTYREQ/QTYISS/UOM/TYPE/
LOT/SER/BIN + backflush/scrap flags.
**WOMAT** (21-var namespace): WO/SEQ/COMP/QTY/LOT/SER/BIN/DATE/EMP + staging status.
**SCAN.ITEM/SCAN.WO/SCAN.EMP**: barcode scan input variables used for tablet operation.

## Integration

- **[[module-WO|WO]]** — WO-K-I is the same program accessed from the WO menu; WO-G Post Material Issues is the final posting step after kit review
- **[[module-IN|IN]]** — on-hand is not reduced until WO-G posts; BKINVLOC updated then
- **[[module-LC|LC]]** / **[[module-SC|SC]]** — lot and serial control are applied at kit staging for lot/serial items
""",

"BR": """
## What it does

Brands — a simple brand code reference table for inventory items.
Maintained via T7BRANDS.RWN.

## DFM-confirmed (T7BRANDS.DFM, Pass 519)
Caption: "New Screen" (standard list-editor)
Fields: **Code** + **Description**. Add/Edit/Delete/Back toolbar.
The brand code is likely stored on inventory items as a user-defined
classifier (similar to Category and User Defined codes). No other EVO
tables reference BRANDS in the known schema, suggesting it is a report-
filter field on BKICPROD (likely MTIC.PROD.BRAND or similar).

## Integration

- **[[module-IN|IN]]** — brand code is a filter/classifier on inventory items in IN-B
""",

"XC": """
## What it does

XCharge Conversion Utility — a one-time migration tool to convert legacy
credit card data stored in EVO into the secure XCharge format.

## DFM-confirmed (T7XCUTIL.DFM, Pass 519)
Caption: "XCharge Conversion Utility"
Display label: "Converting data to Secure XCharge"
No user-input fields visible — the utility runs automatically when launched.
This is a one-shot conversion, not a recurring program.

## Context

XCharge is the credit card processing integration used throughout EVO
(AR-N deposits, SO credit card payments). Before the secure XCharge format
was adopted, card data was stored in a legacy format. T7XCUTIL converts
that legacy data in-place. After running once, the program is retired.

## Integration

- **[[module-AR|AR]]** — AR-N credit card deposits use XCharge after conversion
- **[[module-SO|SO]]** — SO credit card payments use XCharge
""",

"CU": """
## What it does

WO Cut Sheet — a material allocation/issue confirmation screen used in
textile or mattress manufacturing to record cutting quantities against
work orders.

## DFM-confirmed (T7CU programs, Pass 519)

### t7cutsheet2.DFM — Fabric/Material Cut Sheet (primary)
Fields: Job # / Lot # / Qty Left / Part / Tot (total) / Iss (issued) / Left
Warning line: "*Some Qtys already Allocated"
Footer: Total Qty display
Security: User + Password required to Post
Toolbar: Skip / Post / Exit

### t7cutsheet2b.DFM — Fabric Variant
Fields: Job # / Fabric / Req QTY / Tot / Iss / Left
No password gate — lighter-weight entry form.

## Workflow

1. Operator opens a WO cut sheet by Job # and Lot #.
2. System displays required vs. issued vs. remaining quantities per part/fabric.
3. Operator reviews allocations; if "*Some Qtys already Allocated" appears, partial
   issues already exist — care required to avoid over-issuing.
4. Operator enters User + Password and clicks Post to confirm the issue.
5. Alternatively, Skip bypasses the record.

## Integration

- **[[module-WO|WO]]** — cut sheet reads from WORKORD (Job#/Lot#) and posts to material issue tables
- **[[module-IN|IN]]** — inventory on-hand reduced at Post
""",

"TE": """
## What it does

NACHA / ACH — exports vendor payment files in NACHA format (National Automated
Clearing House Association) for ACH electronic funds transfer. T7TESTNACHA.RWN
generates the flat-file export from EVO AP check records.

## DFM-confirmed (T7TESTNACHA.DFM, Pass 519)
Caption: "NACHA"
Entry fields:
| Field | Notes |
|-------|-------|
| Bank Account Number | ACH originating bank account |
| Bank Account Name | Name of originating bank account |
| Check Number From / Thru | Filter by check number range |
| Check Date From / Thru | Filter by check date range |
| Export FileName | Output path, e.g., `C:\\EXPORT\\DATA\\Filename.TXT` |
| Company Tax ID | EIN for ACH Company ID field |
| Effective Date | ACH settlement date |

Toolbar: Settings / Process / Exit

## Workflow

1. Run AP check printing for the payment batch in AP.
2. Open TE-NACHA, enter bank account + date range matching the batch.
3. Enter export path and company Tax ID.
4. Click Process — generates the NACHA-formatted flat file.
5. Submit the flat file to the bank for ACH processing.

## Integration

- **[[module-AP|AP]]** — reads AP check records (BKAP.CHK.*) as the source data
- **[[module-AD|AD]]** — bank account defined in AD-B; account number used here must match
""",

"QS": """
## What it does

Quick Sales Entry — a simplified SO entry form for rapid order creation
without navigating the full SO-A screen. Designed for high-volume or
counter-sale environments.

## DFM-confirmed (t7qsoa.DFM + T7QSOALines.DFM, Pass 519)

### t7qsoa.DFM — Entry point
Caption: "Quick Sales Entry"
Button: **Create Sales Order** + Exit

### T7QSOALines.DFM — Line item entry
Caption: "New Screen"
Header: SO Number display
**Customer Info section:** Customer code
**New SO Line Item section:**
| Field | Notes |
|-------|-------|
| Item Number | Part number lookup |
| Quantity | |
| Discount | Discount % |
| Price | Unit price |

Toolbar: Lines grid / Save / Clear / Exit

## How it differs from SO-A

SO-A is the full sales order entry program with shipping, terms, tax,
approval workflow, etc. QS/t7qsoa is a stripped-down form: enter a customer,
add line items (item/qty/discount/price), Save. The resulting record is a
standard BKSO* Sales Order record — just created faster.

## Integration

- **[[module-SO|SO]]** — produces the same BKSO* tables as SO-A; QS is just a faster front-end
- **[[module-IN|IN]]** — item lookup reads BKICMSTR for valid item numbers
""",

"FN": """
## What it does

File Navigator (UT-K-B Search and Replace) — a mass field-value editor for Btrieve data
files. Allows searching for records matching filter conditions and replacing or adjusting
field values in bulk. Accessed from the UT Utilities menu as UT-K-B "Search and Replace."

## DFM-confirmed (T7FNR.DFM, Pass 475 + Pass 520)
Caption: "New Screen"

| Section | Fields |
|---------|--------|
| Target | File Name (Btrieve .B file), Field to Change, Array # |
| Filter conditions (up to 3) | Array #, Operation, Value, Pos, Start, Length |
| Operations | All / <> / > / < / >= / <= / = / $ ($ = substring contains) |
| Adjustment | Flat amount, Percentage |
| Buttons | Test Filters (preview matches), Process, Exit |

## Workflow

1. Enter Btrieve file name.
2. Specify which field to change (with optional array index for multi-value fields).
3. Define up to 3 filter conditions to limit which records get changed.
4. Click Test Filters to preview the match count before committing.
5. Enter flat amount or percentage adjustment value.
6. Click Process to apply changes across all matching records.

## Notes

- Break-glass mass-update tool intended for data corrections, price adjustments, or
  field repairs that would otherwise require custom SQL or Btrieve API code.
- Operates directly on Btrieve `.B` files — not SQL-level access.
- The `$` operation (substring contains) is unique to TAS Pro and not standard SQL.

## Integration

- **[[module-UT|UT]]** — FN is accessed as UT-K-B from the UT Utilities sub-menu
- **[[module-IN|IN]]** — common use case: bulk price adjustments on BKICPROD
""",

"MH": """
## What it does

Shipping Order — batch shipment release and outbound shipping document processing.
MH handles multi-bin picking, lot/serial assignment, backorder control, carrier
tracking, and per-user RTM assignment for shipping report templates.

## Programs

| Program | Description |
|---------|-------------|
| `T7MHOPE.RWN` | Main shipping order processing (98p, ISTECH2.LIB, 30-table DB) |
| `T7SHIPRTM.RWN` | Per-user RTM assignment for shipping order report templates |

## DFM-confirmed (T7SHIPRTM.DFM, Pass 520)
Caption: "New Screen"
Fields: **User** + **RTM Name** — maps each user to a specific .RTM report format
for their shipping order print output. Add/Edit/Delete/Back toolbar.
This allows different users or workstations to use different shipping order
layouts (e.g., different form designs for different carriers or customers).

## Key operational variables (from Pass 181/216)
| Variable | Purpose |
|----------|---------|
| MULTI.BIN / MULTI.BIN.QTY / MULTI.BIN.CNTR | Multi-bin pick quantities |
| DEFAULT.BIN | Default bin for single-bin operations |
| ALLOW.BO / ALLOW.BO.RCN / ALLOW.BO.CNTR | Backorder release control |
| TRACKING.NUM / SHIP.CO | Carrier tracking number + carrier code |
| SPECIAL / SPECIAL2 | Tariff codes for customs |
| RET.LOC | Return location for MH-handled SO returns |
| LOT_YN / SER_YN | Lot/serial tracking flags |
| FROM.CUST / THRU.CUST | Batch release customer range filter |
| TERRITORY | Territory filter |
| FROM.ORDDTE / THRU.ORDDTE | Order date range filter |
| AUTO.BO / AUTO.RCOMM | Automatic backorder release / recommit flags |
| IS.SHPVIA.* / IS.SHIP.* | Ship-via and carrier tables (ISSHPVIA + ISSHIPCO) |
| ISREP.ORD.* | Repeat-order staging (ISREPORD table) |

## 30-table DB
BKICLOC / MTICMSTR / BKGLTRAN / ISREPLNK / BKPRSALE / BKICPMAT / ISBSF
(plus standard BK* SO/AR tables)

## Integration

- **[[module-SO|SO]]** — MH processes released SO lines for shipment; reads SO header/lines
- **[[module-IN|IN]]** — inventory allocated and on-hand reduced at ship confirmation
- **[[module-LC|LC]]** / **[[module-SC|SC]]** — lot/serial tracking applied at ship
- **[[module-AR|AR]]** — invoice created on ship confirmation; BKARINV/BKARINVL written
- **[[module-RT|RT]]** — T7SHIPRTM assigns per-user RTM for shipping order prints
""",

}
