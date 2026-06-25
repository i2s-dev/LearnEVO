"""
Step-by-step task recipes — "how do I do X in EVO".

Each RECIPE is (id, title, module, menu_route, body_markdown, keywords).
`menu_route` is a list that becomes breadcrumb navigation.
"""

RECIPES = [

("recipes-index", "All Recipes (A-Z)", None, [],
"""
Every step-by-step walkthrough, grouped by workflow.

## Getting started

- [[recipe-login]] — First-time login
- [[recipe-add-user]] — Add a new user (admin)
- [[recipe-switch-company]] — Switch between companies

## Customer / A/R

- [[recipe-enter-customer]] — Add a new customer
- [[recipe-record-payment]] — Apply a customer payment
- [[recipe-print-statements]] — Month-end statements
- [[recipe-credit-memo]] — Issue a credit
- [[recipe-ar-aging]] — Run the aging report

## Vendor / A/P

- [[recipe-enter-vendor]] — Add a new vendor
- [[recipe-enter-voucher]] — Enter an AP invoice / voucher
- [[recipe-pick-invoices]] — Select vouchers to pay
- [[recipe-print-checks]] — AP check run
- [[recipe-void-check]] — Void a printed check
- [[recipe-1099]] — Year-end 1099 forms

## Inventory

- [[recipe-enter-item]] — Add a new item
- [[recipe-receive-stock]] — Receive inventory (PO-C or IN-E)
- [[recipe-adjust-inventory]] — Quantity adjustment
- [[recipe-transfer-stock]] — Bin-to-bin transfer
- [[recipe-physical-inventory]] — Full physical count cycle

## Sales orders

- [[recipe-enter-so]] — Create a sales order
- [[recipe-so-pick-ship]] — Pick and ship an order
- [[recipe-print-invoice]] — Generate the invoice
- [[recipe-rma]] — Return Merchandise Authorization

## Purchase orders

- [[recipe-enter-po]] — Create a purchase order
- [[recipe-receive-po]] — Receive against a PO
- [[recipe-rfq]] — Request for Quote
- [[recipe-close-po]] — Close a PO early

## Manufacturing

- [[recipe-enter-bom]] — Build a bill of materials
- [[recipe-enter-routing]] — Define a routing
- [[recipe-estimate]] — Build an estimate
- [[recipe-work-order]] — Full WO lifecycle (release → close)
- [[recipe-dc-labor]] — Enter labor via Data Collection
- [[recipe-run-mrp]] — Run MRP

## Reporting

- [[recipe-custom-report]] — Modify an RTM in ReportBuilder
- [[recipe-financial-statements]] — Run balance sheet / income statement
- [[recipe-export-csv]] — Export a grid to CSV

## Close

- [[recipe-month-end-close]] — Monthly close checklist
- [[recipe-year-end-close]] — Fiscal year end

## Admin / maintenance

- [[recipe-backup]] — Run a database backup
- [[recipe-add-company]] — Create a new company
- [[recipe-update-evo]] — Apply software update
- [[recipe-purge-history]] — Archive old data

## Workflow end-to-end

- [[recipe-po-to-payment]] — Full procurement cycle
- [[recipe-so-to-cash]] — Full sales cycle
""",
["recipes", "how to", "howto", "walkthrough", "task"]),

# ----- Starter recipes -----

("recipe-enter-customer", "How to Enter a New Customer", "AR",
["Main Menu", "Accounts Receivable", "AR-A Enter Customers"],
"""
Add a new customer record to [[table-BKARCUST|BKARCUST]].

## Prerequisite

- You need `AHSY_USER_ACCES_1 = Y` permission (AR module). If your menu
  doesn't show AR, talk to your admin.

## Menu route

```
Main Menu → AR (Accounts Receivable) → AR-A (Enter Customers)
```

Or type `AR-A` at the menu prompt and press Enter.

## Step-by-step

1. On the AR-A browse screen, press **INS** (Insert) to start a new
   customer.
2. **Customer code** — up to 10 chars, uppercase. Convention: use a
   readable short code, e.g. `ACMECORP` or `0000100`.
3. **Name** (30 chars) — legal name, used on invoices.
4. **Address, city, state, zip, country** — standard. Two `BKAR_ADD2`
   slots allow a 2-line street address.
5. **Contacts** — up to 5 contacts (`BKAR_CONTACT_1..5`), with
   matching phone numbers (`BKAR_TELEPHONE_1..5`).
6. **Credit Limit** — dollar amount. Used by SO-A to warn if a new
   order would exceed.
7. **Charge Interest** — `Y`/`N` flag. If Y, the monthly interest job
   (AR-D) will charge overdue invoices.
8. **Tax info tab** (`PgDn`) — tax code from [[table-BKISTAX|BKISTAX]],
   exempt flag, tax ID.
9. **Pricing tab** — sales level (`BKAR_SAL_LVL`) and default
   discount (`BKAR_DISC`).
10. **Credit tab** — terms (Net 30 / 2%10/N30 / etc.), COD flag, hold
    flag.
11. When done, press **F10 Save**.

## Field limits to know

| Field | Max | Notes |
| ----- | --- | ----- |
| Code | 10 | Uppercase alpha-numeric |
| Name | 30 | — |
| Address | 30 each line | — |
| City | 26 | — |
| State | 2 | USPS 2-char |
| Zip | 10 | Supports ZIP+4 with dash |
| Credit Limit | 12-digit numeric | 2 dec |
| Out Invoice balance (read-only) | 12-digit numeric | — |

## What happens behind the scenes

- INSERT writes to `BKARCUST.B<company>`.
- The customer shows up immediately in F2 lookups throughout the app.
- No GL entries are created — customers don't post.

## Common mistakes

- Using a customer code with spaces. Spaces can work but make lookups
  awkward — avoid.
- Forgetting to set the tax code (causes incorrect invoicing).
- Leaving "Charge Interest" on for accounts that shouldn't be charged.

## Related

- [[module-AR]]
- [[table-BKARCUST]]
- [[recipe-enter-so]] — creating their first order
- [[recipe-record-payment]] — when they pay
""",
["enter customer", "new customer", "add customer", "ar-a", "bkarcust"]),

("recipe-record-payment", "How to Record a Customer Payment", "AR",
["Main Menu", "Accounts Receivable", "AR-C Record Payments"],
"""
Apply a customer check (or ACH, wire, credit card) to open invoices.

## Menu route

```
AR-C Record Payments
```

## Step-by-step

1. From the main menu, select `AR-C`.
2. Enter the **customer code** or F2 Lookup to find them. EVO
   displays their open invoices.
3. Enter the **deposit amount** (the check total).
4. EVO shows each open invoice for that customer with its aging bucket.
5. Apply the payment across invoices:
   - **F10 Auto-apply** — apply oldest-first until deposit is used up.
   - Or manually: arrow to each invoice, type the amount to apply.
6. If there's a short-pay or overpay, EVO prompts for:
   - **Write-off** — leave as bad debt (posts to GL write-off account)
   - **Leave open** — remaining balance stays on the invoice
   - **Customer credit** — overpay becomes a credit memo
7. Enter the **check number** or ACH reference.
8. Enter the **deposit date** (or leave as today).
9. Press **F10 Post**.

## What posts to GL

Each payment entry triggers GL entries:

| Debit | Credit |
| ----- | ------ |
| Cash (BKAR_CUST_CASHACC from BKARCUST or default) | Accounts Receivable |

Write-offs post to the bad-debt account (`BKSY_AR_BADDEBTACCT`).

Entries go through [[table-BKGLTEMP|BKGLTEMP]] → [[table-BKGLACHK|BKGLACHK]].

## Tables touched

- `BKARCHKF` — Check file (inserted)
- `BKARCHKH` — Check history (copied on close)
- `BKARINV` — Invoice (balance decremented, status updated)
- `BKARCUST` — Customer (last-pay date, YTD totals updated)
- `BKGLTEMP` / `BKGLACHK` — GL entries

## Common problems

- **"Invoice not found"** — probably from a different company; make
  sure you logged into the right company.
- **"Deposit amount is zero"** — must enter at least $0.01.
- **"Check number already used"** — duplicate-check validation is on
  by default; you'll get warned.

## Related

- [[recipe-enter-customer]]
- [[recipe-ar-aging]]
- [[recipe-credit-memo]]
""",
["record payment", "ar-c", "customer payment", "check", "deposit", "apply payment"]),

("recipe-enter-voucher", "How to Enter an A/P Voucher (Invoice)", "AP",
["Main Menu", "Accounts Payable", "AP-B Enter Vouchers"],
"""
Record a vendor invoice so it can be paid later.

## Menu route

```
AP-B Enter Vouchers
```

## Step-by-step

1. Select `AP-B`.
2. **Vendor code** — F2 Lookup or type directly.
3. **Invoice number** — vendor's invoice #. Max 15 chars.
4. **Invoice date** — the date on the vendor's invoice.
5. **Due date** — defaults from vendor terms (`BKAP_VEND_TERMS`).
6. **PO reference** (optional) — if this invoice is for a receipt on
   an existing PO, enter the PO number. EVO will auto-populate the
   GL accounts from the PO lines.
7. **Line items** — per-line GL account and amount. You can split one
   invoice across multiple accounts.
8. **Tax / freight / discount** — optional adjustment lines.
9. **Total** — must match the vendor invoice total.
10. **F10** to post.

## Variations

### Voucher against a PO
If you entered a PO number, EVO shows received-but-unvouchered lines.
Check off what this invoice covers; EVO handles the accrual reversal.

### Recurring voucher
Use `AP-O (Enter Recurring)` instead — EVO templates it for future
auto-generation.

### Credit memo / return to vendor
Enter a negative-amount voucher. The system will generate a credit on
the vendor's account.

## GL posting

| Debit | Credit |
| ----- | ------ |
| Expense / Inventory GL account (per line) | Accounts Payable |

Plus any sales-tax liability and freight breakouts.

## Tables touched

- `BKAPINVT` — Invoice (header)
- `BKAPINVL` — Invoice lines
- `BKAPVEND` — Vendor (YTD totals, last-purchase date)
- `BKAPPO`, `BKAPPOL` — PO (if referenced, received→vouchered flag)
- `BKGLTEMP` / `BKGLACHK` — GL entries

## Related

- [[recipe-enter-vendor]]
- [[recipe-pick-invoices]] — what to do next
- [[recipe-print-checks]] — pay it
""",
["enter voucher", "ap-b", "vendor invoice", "bill", "ap invoice", "voucher"]),

("recipe-print-checks", "How to Run an A/P Check Run", "AP",
["Main Menu", "Accounts Payable", "AP-F → AP-G → AP-H"],
"""
The full AP check-run process: pick invoices, proof, print.

## Menu route

Three steps:
```
AP-F Pick Vouchers/Invoices to Pay
AP-G Print Pro Forma Check Register   (review before printing)
AP-H Print Checks                      (commits and prints)
```

## Phase 1: Pick (AP-F)

1. Select `AP-F`.
2. Enter **check date** — the pay date you want printed on checks.
3. Enter **vendor range** — all vendors, or a specific subset.
4. Enter **due-date cutoff** — invoices due on or before this date
   will be selected.
5. EVO shows each eligible invoice; you can:
   - **Accept** (pay full)
   - **Skip** (this run)
   - **Partial** (pay part; remainder stays open)
   - **Hold** (flag for special handling)
6. F10 to commit the pick list.

## Phase 2: Proof (AP-G)

Print the pro-forma check register. Review:
- Total disbursement
- Bank account being used
- Any rows you didn't intend to include

If wrong, go back to `AP-F` and un-pick.

## Phase 3: Print (AP-H)

The actual check printing:

1. Select `AP-H`.
2. Choose **check format**:
   - Format 1 — Classic dot-matrix
   - Format 2 — Laser 3-part (check on top)
   - Format 3 — Laser 3-part (check on bottom)
   - Format 4 — Laser 3-part (check in middle)
3. Enter **starting check number**.
4. Place check stock in the printer.
5. EVO runs the print job, using RTM `banks.rtm` (or
   `I2SCHK1.rtm` for the i2Systems custom format).
6. After printing, EVO asks **"Did all checks print correctly?"**:
   - **Yes** — EVO commits. Posts to [[table-BKAPCHKF|BKAPCHKF]] and
     rolls the disbursement to GL.
   - **No** — EVO asks which check number failed; lets you void the
     bad ones and reprint.
7. **F10 Post**.

## What posts to GL

For each check:

| Debit | Credit |
| ----- | ------ |
| Accounts Payable | Bank account (BKSY_AP_DISBACCT) |

Any discounts taken post to the Discount Earned account.

## Key source reference

The AP check printing logic is actually one of the 7 plaintext `.SRC`
files on the share — see `samples/src/Bkaph.src` (dot-matrix) and
`Bkapha.src` (laser). Reading those sources is instructive if you're
debugging a print problem.

## Common problems

- **Check alignment** — fix by running `AP-H` with a test-check
  option and adjusting the RTM margins.
- **"Invalid format setting"** — the check format flag in
  `BKYSMSTR.bkys.yn[48]` is wrong. Fix in `AD-C (AP Defaults)`.
- **Duplicate check number** — check-number sequence is in
  `BKSYMSTR.BKSY_AP_NXTCHK`; an admin can reset it.

## Related

- [[recipe-enter-voucher]] — creating vouchers
- [[recipe-pick-invoices]] — AP-F detail
- [[recipe-void-check]]
- [[table-BKAPCHKF]] — the check file
""",
["ap check", "print checks", "ap-h", "ap-f", "ap-g", "check run", "disbursement",
 "pay vendors", "check printing"]),

("recipe-run-mrp", "How to Run MRP", "MR",
["Main Menu", "MRP", "MR-F Generate MRP Suggestions"],
"""
Run Material Requirements Planning to compute what to buy and make.

## When to run

- Weekly, or whenever there's a material change (new SO, PO delay,
  BOM change)
- After a physical count
- Before a large production run

## Menu route

```
MR-F Generate MRP Suggestions
```

Or use `AUTOT7MRF` (auto-run variant, called from the scheduler).

## Prerequisites

- Current inventory on-hand (`BKICMSTR.BKIC_PROD_UOH`)
- Open POs (`BKAPPO`, `BKAPPOL`) — expected receipts
- Open SOs (`BKARINV`, `BKARINVL`) — committed demand
- Open WOs (`WORKORD`) — in-process supply
- Forecast (`BKMRPFC`) — optional extrapolated demand
- BOM (`BKBMMSTR`) — to explode parent demand
- Calendar (`CALENDAR`) — working days

## Step-by-step

1. Select `MR-F`.
2. Enter **horizon** — how far forward to plan (default 90 days,
   configurable).
3. Enter **item range** (or all).
4. Enter **location range** (if you use multi-loc).
5. Choose **include forecast** — Y/N.
6. EVO runs. This can take minutes for large inventories.
7. Report prints to screen/printer showing, per item:
   - Current on-hand
   - Net demand (SO + forecast)
   - Scheduled supply (PO + WO)
   - Net requirement by week
   - Suggested action: **Buy** (make PO) or **Make** (make WO)
8. Optionally, auto-generate POs from buy-suggestions (`BKMRPPO`
   table captures these).

## Tables touched

The MRP algorithm reads a wide set (see `samples/src/BKMRF.SRC`):

- `BKARINV` / `BKARINVL` — demand from SOs
- `BKAPPO` / `BKAPPOL` — supply from POs
- `BKBMMSTR` — BOM (to explode to components)
- `BKICMSTR` / `BKICLOC` — inventory & locations
- `BKMRPFC` — forecast
- `BKMRPSW` — safe-work (buffer) data
- `CALENDAR` — workday calendar
- `MTICMSTR` — second-gen item master (if used)
- `WORKORD` — work orders

Writes suggestions to `BKMRPPO` (buy recommendations).

## Common problems

- **MRP takes hours** — too much history; run `AM-S (Purge old
  transactions)` first.
- **Suggestions look wrong** — check lead times on items
  (`BKIC_PROD_LTIME`) and safety stock levels.
- **Calendar gap** — ensure CALENDAR has future workdays defined.

## Related

- [[module-MR]]
- [[table-BKBMMSTR]] — BOM
- [[recipe-enter-po]] — turn suggestions into POs
""",
["mrp", "material requirements", "mr-f", "production planning", "run mrp", "bkmrf"]),

("recipe-month-end-close", "Month-End Close Checklist", "AM",
["Main Menu", "Archive / Maintenance", "AM-*"],
"""
The standard monthly close sequence. Assumes you've been posting all
month.

## The checklist

Before starting, **everyone must be logged out** of the modules being
closed.

### 1. AR cleanup (if needed)

- `AR-B` Post any remaining invoices.
- `AR-C` Apply any remaining receipts.
- `AR-D` Charge interest on overdue invoices (optional but typical).
- `AR-F` Run aging — print for records.

### 2. AP cleanup

- `AP-B` Enter any remaining vendor invoices.
- `AP-F / AP-G / AP-H` Run checks for anything due.
- `AP-I` Run aging — print for records.

### 3. Inventory

- `PI-C` Post any remaining physical count results.
- `IN-I` Print inventory valuation — keep a copy.

### 4. Work orders

- `WO-L-A` Work order status report.
- `WO-C` Close any WOs that finished this month.
- `WO-F` Print WIP report.

### 5. GL consolidation

- `AM-I` Consolidate GL detail — rolls posted transactions from temp
  files into the permanent GL.
- `AM-R` Out-of-Balance Report — **must be zero**. If not, back out
  and investigate.
- `GL-X` Print financial statements (balance sheet, income statement).

### 6. Lock the period

- `AM-A` Reset Period-End Close Date.
  - Pushes the `BKSY_AR_PEDTE` / `BKSY_AP_PEDTE` / `BKSY_GL_PEDTE`
    pointers forward.
  - Prior periods become read-only for posting.

### 7. Backup

- `AM-?` Backup (or `EvoERPbackup.RWN`) — zip current state.
  Output goes to `\\\\i2s109-solidcrm\\Bak Up\\`.

### 8. Archive

At quarter- or year-end, run:
- `AM-J` Archive/Purge AP History
- `AM-K` Archive/Purge AR History
- `AM-T` Archive GL Transaction Detail

These move old data out of hot tables into archive tables
(`BKAPHPO`, `BKAPHPOL`, `BKARHINV`, `BKARHIVL`, etc.).

## Red-flag signals

- **Out-of-balance non-zero** — stop. Something posted only partially
  (crashed?). Find it before closing.
- **Negative on-hand** — someone sold what wasn't received.
- **Trial balance doesn't match balance sheet** — posting error.
  Re-run `AM-I`.

## Related

- [[module-AM]]
- [[recipe-year-end-close]]
""",
["close", "month end", "month-end", "am-i", "am-a", "consolidate", "period end",
 "monthly close", "checklist"]),

("recipe-enter-so", "How to Create a Sales Order", "SO",
["Main Menu", "Sales Orders", "SO-A Enter Sales Orders"],
"""
Build a sales order from quote or scratch.

## Menu route

```
SO-A Enter Sales Orders
```

(For a quote rather than a firm order, use `SO-P-A Enter Quotes`.)

## Step-by-step

1. Select `SO-A`.
2. **Customer code** — F2 Lookup. If new, cancel out and run `AR-A`
   first.
3. **Ship-to** — if different from billing, override here.
4. **Order date / required date** — shipping dates.
5. **Ship-via / freight terms / PO number (theirs)** — header info.
6. **Salesperson** — from `BKCSA` (commission master).
7. **Line items** — for each:
   - **Item code** (F2 Lookup or enter)
   - **Quantity**
   - **Unit price** (defaults from price level; manual override OK)
   - **Requested date** (per line, for partial ship)
   - **Location** (bin/warehouse, if multi-loc)
8. If customer has **credit hold**, EVO warns. Admin can override.
9. F10 Post.

## What's reserved

Each line reduces `BKICMSTR.BKIC_PROD_UOSO` (units on sales order)
and increments `BKIC_PROD_COMMIT`. Doesn't ship stock until `SO-C`
picks it.

## Variations

- **Drop-ship** — quantity comes directly from vendor, doesn't touch
  inventory. Check the drop-ship flag per line.
- **Features and Options** — if the item is configurable
  ([[subsystem-evofno]]), EVO launches the F/O dialog for that line.
- **Lot/serial tracked** — at ship time you'll be prompted for lot or
  serial numbers.

## Tables touched

- `BKARINV` — SO header
- `BKARINVL` — SO lines
- `BKARCUST` — Customer (outstanding/committed updates)
- `BKICMSTR` — Item (committed qty)
- `BKSONOTE` — Order notes
- `BKSOPO` — SO-to-PO linkage for drop-ships

## Related

- [[recipe-enter-customer]]
- [[recipe-enter-item]]
- [[recipe-so-pick-ship]] — next step
- [[recipe-rma]] — returns
""",
["enter so", "sales order", "so-a", "new order", "customer order"]),

("recipe-work-order", "Work Order Lifecycle (End-to-End)", "WO",
["Main Menu", "Work Orders", "WO-A"],
"""
The complete manufacturing order flow: release → issue → labor →
receive → close.

## Prerequisites

- An item in `BKICMSTR` flagged as "Make" (`BKIC_PROD_TYPE = M`).
- A BOM in `BKBMMSTR` (plus `BKBMAMTR` for alt parts).
- A routing in `ROUTING` (plus `BKRTEMTR` for ops).

## Lifecycle

### 1. Create — WO-A

```
WO-A Enter Work Orders
```

1. Enter item to make, quantity, due date.
2. EVO copies the BOM to `WOBOM` (the WO-specific BOM, so you can
   modify just this order).
3. Copies the routing to `WOROUT`.
4. Status = Open.

### 2. Release — WO-B

```
WO-B Release Work Orders
```

Changes status from Open to Released. This:
- Locks the BOM/routing against BOM-level edits
- Allocates component inventory (reserves on-hand for this WO)
- Prints the shop packet (pick list + routing sheet)

### 3. Issue components — DC-B or IN-E

Components leave raw inventory, go to WIP (`BKIC_PROD_UOH` decreases
for components, increases for WIP of parent at standard cost).

### 4. Report labor — DC-A

```
DC-A Enter Labor (Data Collection)
```

Workers clock in/out per operation. Each labor record:
- Writes to `WOLABOR`
- Updates `WORKORD` actual-labor fields
- Posts to GL: WIP Labor ↔ Labor Applied

### 5. Report scrap — DC-B

If parts are scrapped, record them here. Scrap cost goes to the
scrap GL account.

### 6. Report receipts — WO-C

```
WO-C Receive Finished Goods
```

Counts as finished good going into inventory:
- `BKICMSTR.BKIC_PROD_UOH` increases for parent
- WIP clears out
- Variance goes to PPV (purchase price variance) or scrap

### 7. Close — WO-D

```
WO-D Close Work Orders
```

When WO is complete:
- Cost summary posted to JC (Job Costing)
- Variances posted to GL
- Status = Closed
- WO locked against future postings

## Reports along the way

- `WO-L-A` — Work order status (how are things going?)
- `WO-L-F` — Work order shortage (what components are we missing?)
- `WO-L-B` — Print WO schedule
- `JC-A` — Job cost report (profit/loss for this WO)

## Variance tracking

At close, EVO compares:
- Planned cost (from BOM × quantity, plus planned labor from routing)
- Actual cost (from issues + labor + scrap)
- Variance = planned − actual

Posts to:
- `BKSY_MAT_VARACCT` (material variance)
- `BKSY_LAB_VARACCT` (labor variance)
- `BKSY_OVR_VARACCT` (overhead variance)

## Tables touched (the whole 30-table WO family)

See [[module-WO]] for the full list; key ones:

- `WORKORD` — header
- `WOBOM` — component list for this WO
- `WOROUT` — operations for this WO
- `WOLABOR` — labor time records
- `WOMAT` — material issues
- `WORECV` — receipts of finished goods
- `WOHLABOR`, `WOHMAT`, `WOHRECV`, `WOHROUT` — history (after close)

## Related

- [[module-WO]]
- [[module-BM]]
- [[module-RO|RO - Routings]]
- [[module-DC]]
- [[recipe-dc-labor]]
- [[recipe-run-mrp]]
""",
["work order", "wo", "manufacturing", "release", "issue", "labor", "wip",
 "receive finished", "close", "wo-a", "wo-b", "wo-c", "wo-d"]),

("recipe-physical-inventory", "Physical Inventory Cycle", "PI",
["Main Menu", "Physical Inventory", "PI-*"],
"""
A complete physical count — freeze, count, reconcile, post.

## When

- Annually (fiscal) at minimum
- More often for cycle counts (partial items)
- After any major event that could have lost track of stock

## Cycle steps

### 1. PI-A — Setup count

```
PI-A Print Count Sheets
```

EVO "freezes" on-hand quantities at the moment you run this, writing
them to `BKPIFROZ` (frozen on-hand). Prints count sheets with blank
columns for the counters to fill in.

While frozen:
- Normal stock moves continue, recorded in `BKPILOT`
- Cycle-counting can overlap; don't block other ops

### 2. Count

Physical counters walk the warehouse, writing actual counts on sheets
or scanning into handheld devices.

### 3. PI-B — Enter counts

```
PI-B Enter Physical Counts
```

Key in actuals to `BKPIPHYS`. EVO compares to frozen values and shows
variances per item.

### 4. PI-D — Variance report

```
PI-D Print Variance Report
```

Review big variances — investigate before posting. A common mistake is
counting units instead of cases, or vice versa.

### 5. PI-E — Update inventory

```
PI-E Post Physical Counts
```

Commits. EVO:
- Sets `BKIC_PROD_UOH` to counted value (plus any transactions in
  `BKPILOT` during freeze)
- Posts adjustment to GL: Inventory ↔ Inventory Adjustment
- Clears `BKPIFROZ` and `BKPIPHYS`

### 6. Print updated reports

- `IN-I` Inventory valuation (post-count)
- `JC-?` Job cost if WIP involved

## Cycle counting (partial physical)

Same menus, but `PI-A` only "freezes" selected items (e.g., ABC
class A).

## Tables touched

- `BKPIMSTR` — PI master
- `BKPIFROZ` — frozen-at-start snapshot
- `BKPIPHYS` — actual counts
- `BKPILOT` — intervening transactions during freeze
- `BKPILCNT` — cycle count schedule
- `BKICMSTR` — updated at post

## GL posting

| Debit | Credit |
| ----- | ------ |
| Inventory Shrinkage (from `BKSY_INV_SHRACC`) | Inventory |

Or reversed if net positive.

## Related

- [[module-PI]]
- [[module-IN]]
- [[table-BKICMSTR]]
""",
["physical inventory", "pi-a", "pi-b", "pi-e", "count", "cycle count", "shrink"]),

("recipe-enter-item", "Add a New Item (Item Master)", "IN",
["Main Menu", "Inventory", "IN-B Enter Items"],
"""
Create or update an item record in the Inventory master. Every part,
raw material, assembly, finished good, or labor code tracked by EVO
must have a record here.

## Prerequisites

- Know the item number you want to assign (or let EVO assign the next
  sequential number if auto-numbering is on).
- Know the product type (see table below).
- Have the default GL accounts set up in System Defaults.

## Steps

1. `Main Menu → Inventory → IN-B Enter Items`
2. **Item#** — enter the item number (up to 15 chars, typically
   all-caps alphanumeric with no spaces).
3. **Description** — free-text, max 30 chars. This is what prints on
   pick tickets, invoices, and POs.
4. **Product Type** — single-letter code:

   | Code | Meaning |
   |------|---------|
   | R | Raw Material |
   | F | Finished Good |
   | A | Assembly |
   | M | Make (manufactured in-house) |
   | N | Non-inventory (expense, service) |
   | L | Labor (time charge) |
   | B | Bought (purchased part, no stock) |
   | T | Tooling |
   | K | Kit |
   | O | Other |

5. **UOM** — unit of measure (EA, LB, FT, BOX, etc.).
6. **Cost method** — Standard (`S`), Average (`A`), or FIFO (`F`).
7. **Reorder point** / **Reorder qty** — triggers MRP and min/max
   replenishment.
8. **GL accounts** — Inventory, COGS, Sales, Variance. Usually
   defaulted from `T7MDefaults.DFM` (Master Defaults) by product type.
9. **Bin / Location** — default bin for this item.
10. F10 Post.

## Key fields (BKICMSTR)

| Field | Meaning |
|-------|---------|
| `BKIC_PROD_ITEM` | Item number (PK) |
| `BKIC_PROD_DESC` | Description |
| `BKIC_PROD_TYPE` | Product type (R/F/A/M/N/L/B/T/K/O) |
| `BKIC_PROD_UOM` | Unit of measure |
| `BKIC_PROD_UOH` | Units on hand |
| `BKIC_PROD_UOSO` | Units on sales order |
| `BKIC_PROD_UOPO` | Units on purchase order |
| `BKIC_PROD_UOWO` | Units on work order |
| `BKIC_PROD_COMMIT` | Committed qty |
| `BKIC_PROD_COST` | Standard/avg cost |
| `BKIC_PROD_REORD` | Reorder point |
| `BKIC_PROD_EOQTY` | Economic order quantity |

## Tables touched

- `BKICMSTR` — item master record
- `BKICLOC` — per-bin location records (multi-location)
- `BKICSUP` — default supplier link

## Related

- [[recipe-enter-bom]] — add a bill of materials for this item
- [[recipe-enter-routing]] — add a routing (if manufactured)
- [[recipe-enter-po]] — buy this item
- [[module-IN]]
- [[table-BKICMSTR]]
""",
["enter item", "new item", "in-b", "item master", "add part", "product type",
 "raw material", "finished good", "assembly", "inventory item"]),

("recipe-enter-vendor", "Add or Edit a Vendor", "AP",
["Main Menu", "Accounts Payable", "AP-A Enter Vendors"],
"""
Create or update an Accounts Payable vendor (supplier) record.

## Prerequisites

- Vendor name and remit-to address.
- Payment terms code (must exist in Terms table; AP-G).
- GL expense account for this vendor's purchases.

## Steps

1. `Main Menu → Accounts Payable → AP-A Enter Vendors`
2. **Vendor#** — up to 6 chars. Convention: first two letters of
   company name + sequential digits (e.g., `AC0001`).
3. **Name** — full company name (prints on checks).
4. **Address** lines, **City**, **State**, **Zip**, **Country**.
5. **Phone**, **Fax**, **Contact** name.
6. **Terms** — code from AP-G (e.g., `NET30`, `2/10`).
7. **1099 type** — blank = not a 1099 vendor. Set to `7` (Non-employee
   compensation) for contractors.
8. **GL accounts** — AP clearing account (defaults from system), COGS
   or expense account for this vendor's invoices.
9. **Currency** — if multi-currency is enabled. Defaults to base.
10. F10 Post.

## Key fields (BKAPVEND)

| Field | Meaning |
|-------|---------|
| `BKAP_VEN_VEND` | Vendor number (PK) |
| `BKAP_VEN_NAME` | Vendor name |
| `BKAP_VEN_ADDR1–3` | Address lines |
| `BKAP_VEN_CITY` | City |
| `BKAP_VEN_STATE` | State |
| `BKAP_VEN_ZIP` | Zip |
| `BKAP_VEN_TERMS` | Payment terms code |
| `BKAP_VEN_1099` | 1099 type code |
| `BKAP_VEN_YTDPURCH` | Year-to-date purchases |
| `BKAP_VEN_YTDPAY` | Year-to-date payments |
| `BKAP_VEN_BAL` | Current balance |

## Tables touched

- `BKAPVEND` — vendor master

## Related

- [[recipe-enter-po]] — create a PO for this vendor
- [[recipe-enter-voucher]] — enter an invoice from this vendor
- [[module-AP]]
""",
["enter vendor", "new vendor", "ap-a", "vendor master", "supplier", "add vendor",
 "1099", "payment terms"]),

("recipe-enter-po", "Create a Purchase Order", "PO",
["Main Menu", "Purchase Orders", "PO-A Enter Purchase Orders"],
"""
Create a purchase order to a vendor. EVO tracks open POs against
on-order inventory quantities and drives receipt and voucher flows.

## Prerequisites

- Vendor exists in `BKAPVEND` ([[recipe-enter-vendor]]).
- Items exist in `BKICMSTR` ([[recipe-enter-item]]).
- Ship-to location and buyer code set up.

## Steps

1. `Main Menu → Purchase Orders → PO-A Enter Purchase Orders`
2. **PO#** — EVO assigns next sequential PO number automatically, or
   enter a manual PO number if your site uses pre-printed forms.
3. **Vendor#** — enter or F2 lookup. EVO fills name, address, terms.
4. **Order date** — defaults to today.
5. **Expected receipt date** — used for scheduling and MRP.
6. **Ship via** — carrier code (optional).
7. **Buyer** — buyer/buyer code (prints on PO form).
8. **For each line:**
   - **Item#** — part number to order.
   - **Description** — auto-filled from item master; editable.
   - **Qty ordered** — quantity to buy.
   - **Unit cost** — defaults from last cost in item master; editable.
   - **Expected date** — per-line (can differ from header date).
   - **Job / WO#** — link to a work order if direct-to-WO purchase.
9. F10 Post.

## What posting does

- Creates header in `BKPOMSTR` and lines in `BKPOLINE`.
- Increments `BKICMSTR.BKIC_PROD_UOPO` (units on PO) for each item.
- PO status = `O` (Open).

## Receiving

After goods arrive, use **PO-B Receive Purchase Order** to enter
receipts. See [[recipe-receive-po]].

## Key tables

| Table | Contents |
|-------|---------|
| `BKPOMSTR` | PO header — vendor, date, status, totals |
| `BKPOLINE` | PO line items — item, qty, cost, received |
| `BKPORECV` | Receipt history |
| `BKICMSTR` | Updated: UOPO (units on PO) |

## Related

- [[recipe-receive-po]] — next step after creating a PO
- [[recipe-enter-voucher]] — enter the vendor invoice when it arrives
- [[recipe-enter-vendor]]
- [[module-PO]]
""",
["create po", "purchase order", "po-a", "enter po", "order from vendor",
 "buy parts", "procurement", "vendor order"]),

("recipe-receive-po", "Receive a Purchase Order", "PO",
["Main Menu", "Purchase Orders", "PO-B Receive Purchase Orders"],
"""
Record the arrival of goods against an open purchase order.
Receiving increases on-hand inventory and creates a receipt record
that the AP voucher will reference.

## Prerequisites

- An open PO exists ([[recipe-enter-po]]).
- Items are physically in the warehouse (or at least in-transit for a
  3-way match shop).

## Steps

1. `Main Menu → Purchase Orders → PO-B Receive Purchase Orders`
2. **PO#** — enter the PO number. EVO loads header and open lines.
3. **Receipt date** — defaults to today; change if backdating.
4. **Receiver#** — your internal receiver or packing slip number
   (for traceability).
5. For each line being received:
   - **Qty received** — enter actual quantity; can be partial.
   - **Unit cost** — confirm or override (triggers cost variance if
     different from PO cost).
   - **Location / bin** — where to put this stock.
   - **Lot#** — if item is lot-controlled, EVO prompts for a lot
     number ([[recipe-enter-item]] lot flag).
6. F10 Post.

## What posting does

- Writes records to `BKPORECV`.
- Increments `BKICMSTR.BKIC_PROD_UOH` by qty received.
- Decrements `BKICMSTR.BKIC_PROD_UOPO` by qty received.
- Posts a debit to the Inventory account and a credit to the AP
  Clearing (Accrued Liability) account — awaiting the vendor invoice.
- If full receipt: PO line status → `R` (Received); header → `R`
  when all lines received.

## Partial receipts

EVO leaves the PO open with the remaining qty still on order.
Receive again with PO-B to bring in the remainder, or manually
close with PO-E if you're not expecting the balance.

## Lot / serial at receiving

If the item has lot control enabled (`BKIC_PROD_LOTCTL = Y`), the
Lot Assignment dialog ([[module-LC]]) launches automatically.

## Related

- [[recipe-enter-po]]
- [[recipe-enter-voucher]] — after receiving, enter the vendor invoice
- [[module-PO]]
- [[module-LC]]
""",
["receive po", "po-b", "receiving", "receipt", "goods receipt", "packing slip",
 "receive inventory", "po receipt"]),

("recipe-enter-bom", "Build a Bill of Materials", "BM",
["Main Menu", "Bill of Materials", "BM-A Enter Bill of Materials"],
"""
Define the component list for a manufactured item. The BOM tells EVO
(and MRP) what raw materials and sub-assemblies are needed to build
one unit of the parent item.

## Prerequisites

- Parent item (finished good or assembly) exists in `BKICMSTR`
  with product type `A`, `M`, or `F`.
- All component items exist in `BKICMSTR`.

## Steps

1. `Main Menu → Bill of Materials → BM-A Enter Bill of Materials`
2. **Parent Item#** — the item you're building.
3. **BOM revision** — EVO supports multiple revisions (A, B, C…).
   Defaults to active revision.
4. **For each component:**
   - **Sequence#** — line order (10, 20, 30…).
   - **Component Item#** — raw material or sub-assembly.
   - **Quantity per** — qty needed per *one* parent unit.
   - **UOM** — component unit of measure.
   - **Scrap %** — expected yield loss; EVO inflates qty needed.
   - **Reference designator** — (electronics only) board position
     (e.g., R1, C3).
   - **Operation seq** — if using routings, which routing step uses
     this component (for WIP staging).
5. F10 Post.

## Phantom assemblies

Set a component's BOM type to `P` (Phantom) to explode through it at
WO creation — EVO substitutes the phantom's components directly
rather than ordering the phantom as a separate item.

## BM-D Where-Used

Use `BM-D Where-Used Report` to find every parent that uses a given
component — useful for engineering changes.

## BM-E Component Replace

Global substitution — replace one component with another across all
BOMs in one pass (`BM-E Component Replace`).

## Key tables

| Table | Contents |
|-------|---------|
| `BKBMMSTR` | BOM header — parent item, revision, effectivity |
| `BKBMAMTR` | BOM lines — components, qty-per, scrap%, op-seq |

## Related

- [[recipe-work-order]] — WO pulls the BOM at creation
- [[recipe-run-mrp]] — MRP explodes the BOM
- [[recipe-enter-routing]] — pair with a routing for full WO
- [[module-BM]]
""",
["bom", "bill of materials", "bm-a", "component list", "enter bom",
 "materials", "parent item", "sub-assembly", "explosion", "qty per"]),

("recipe-enter-routing", "Define a Routing (Operations)", "RO",
["Main Menu", "Routings", "RO-A Enter Routings"],
"""
A routing is the sequence of manufacturing operations (steps) for a
parent item. Each operation defines which work center performs it,
how long it takes, and how labor cost is captured.

## Prerequisites

- Parent item exists in `BKICMSTR` (type M, F, or A).
- Work centers exist (WC-A; [[module-WC]]).

## Steps

1. `Main Menu → Routings → RO-A Enter Routings`
2. **Item#** — the item being manufactured.
3. **Revision** — routing revision letter (typically matches BOM rev).
4. **For each operation (step):**
   - **Sequence#** — op order (10, 20, 30…).
   - **Work Center** — the WC code where this op runs.
   - **Operation description** — e.g., "Cut", "Drill", "Inspect".
   - **Setup hours** — one-time setup per run.
   - **Run hours/unit** — labor hours to complete one unit.
   - **Machine hours/unit** — separate from labor if machine-paced.
   - **Queue time** — days to wait before this op can start (for
     scheduling lead-time calculations).
   - **Move time** — days to move from this WC to the next.
   - **Instructions** — free-form text (prints on traveler / router).
   - **Tools** — list of tooling required (linked to RO-I Tool
     Maintenance).
5. F10 Post.

## Lead time calculation

EVO uses routing ops to compute item lead time:

```
lead_time = sum(setup + (run × lot_size) + queue + move) for all ops
```

This drives MRP's planned order start dates and scheduling.

## Key tables

| Table | Contents |
|-------|---------|
| `ROUTING` | Routing header — item, revision |
| `BKRTEMTR` | Routing operations — seq, WC, hours, times |
| `BKRTTOOL` | Tooling per operation |
| `BKRTINST` | Instructions per operation |

## Related

- [[recipe-enter-bom]] — companion to the BOM
- [[recipe-work-order]] — WO copies routing ops at creation
- [[recipe-dc-labor]] — operators clock labor against routing ops
- [[module-RO]]
- [[module-WC]]
""",
["routing", "ro-a", "enter routing", "operations", "work center", "setup hours",
 "run hours", "lead time", "traveler", "op sequence"]),

("recipe-dc-labor", "Clock Labor on a Work Order (DC)", "DC",
["Main Menu", "Data Collection", "DC-A Enter Labor"],
"""
Record operator labor hours against a work order operation.
DC (Data Collection) is how shop-floor time gets into EVO —
either through the DC-A keyboard entry screen or a handheld scanner.

## Prerequisites

- An open Work Order with a routing ([[recipe-work-order]]).
- Employee record exists (DC employee table).
- Work center exists ([[module-WC]]).

## Steps

1. `Main Menu → Data Collection → DC-A Enter Labor`
2. **Employee#** — operator ID.
3. **WO#** — the work order number.
4. **Sequence#** — the routing operation being worked (10, 20, …).
5. **Machine#** — (optional) specific machine within the WC.
6. **Date** — defaults to today.
7. **Start time / Stop time** — or enter **Elapsed hours** directly.
8. **Qty complete** — units finished this session.
9. **Qty scrap** — units scrapped (triggers scrap GL posting).
10. **Action** — `E` Enter new record; `C` Close operation when done.
11. F10 Post.

## What posting does

- Writes to `WOLABOR` (active WO labor).
- Accumulates actual hours and actual cost on the WO.
- If `Action = C`, marks the routing operation complete; EVO moves
  to the next op in the traveler.
- Scrap quantity posts to the Scrap account defined in System
  Defaults (`BKSY_SCRAP_ACCT`).

## WO Priority

Use `WO-PRIO` (t7woprio.DFM) to assign color-coded priorities to
open WOs — visible in `DC-A` and `WCS` (Work Center Schedule) to
help operators pick what to work on next.

## Key tables

| Table | Contents |
|-------|---------|
| `WOLABOR` | Active WO labor records |
| `WOHLAB` | History (after WO close) |
| `BKDCEMPL` | DC employee master |
| `BKDCMACH` | Machine codes |

## Related

- [[recipe-work-order]]
- [[recipe-enter-routing]]
- [[module-DC]]
- [[module-WC]]
""",
["labor", "dc-a", "data collection", "clock in", "time entry", "work order labor",
 "shop floor", "dc labor", "operator hours", "scrap"]),

("recipe-so-pick-ship", "Pick, Pack, and Ship a Sales Order", "SO",
["Main Menu", "Sales Orders", "SO-C Pick/Ship"],
"""
Once a sales order is entered ([[recipe-enter-so]]), use the
pick-ship flow to pull stock from inventory, create a packing slip,
and record the shipment.

## Prerequisites

- An open SO with sufficient on-hand stock (or allow backorder).
- Shipping carrier and freight terms set.

## Steps

### 1. SO-B — Print Pick Tickets

```
Main Menu → Sales Orders → SO-B Print Pick Tickets
```

Prints a warehouse pick list per SO (or by item/location for wave
picking). Items are staged but inventory isn't deducted yet.

### 2. SO-C — Ship the Order

```
Main Menu → Sales Orders → SO-C Enter Shipments
```

1. **SO#** — enter or scan the SO number.
2. EVO shows open lines. Enter **qty shipped** per line.
   - Partial ship leaves remainder as a backorder.
   - Enter `0` to skip a line entirely this shipment.
3. **Ship date** — defaults to today.
4. **Carrier / tracking** — enter carrier and tracking number.
5. **Packing slip#** — EVO assigns or you enter a manual number.
6. F10 Post.

### 3. SO-D — Print Invoice

After posting the shipment, print the customer invoice:

```
Main Menu → Sales Orders → SO-D Print Invoices
```

Or batch-print all unprinted invoices for the day.

## What posting does

- Deducts shipped qty from `BKICMSTR.BKIC_PROD_UOH`.
- Reduces `BKIC_PROD_UOSO` and `BKIC_PROD_COMMIT` by shipped qty.
- Creates an AR open item in `BKARINV` / `BKARINVL`.
- Posts to GL: Debit AR, Credit Revenue; Debit COGS, Credit Inventory.

## Lot / serial at ship

If the item is lot- or serial-tracked, EVO prompts to select which
lot numbers (LC) or serial numbers (SC) are being shipped.

## Backorders

If qty shipped < qty ordered, EVO creates a backorder line. The
original SO remains open for the balance.

## Tables touched

- `BKARINV` — AR invoice / shipment header
- `BKARINVL` — invoice lines
- `BKICMSTR` — on-hand decremented
- `BKSOSHIP` — shipment record

## Related

- [[recipe-enter-so]]
- [[recipe-record-payment]]
- [[module-SO]]
- [[module-AR]]
""",
["ship order", "so-c", "pick ship", "packing slip", "shipment", "invoice so",
 "so-b", "pick ticket", "so-d", "ship sales order"]),

("recipe-adjust-inventory", "Adjust Inventory On-Hand", "IN",
["Main Menu", "Inventory", "IN-F Inventory Adjustments"],
"""
Make a direct positive or negative adjustment to on-hand quantity
for any item — used for cycle count corrections, damage write-offs,
or initial stock loads.

## When to use

- Fixing a count discrepancy outside of a full physical inventory.
- Writing off damaged or obsolete stock.
- Loading initial on-hand quantities for a new company.
- Transferring stock between bins within the same location.

## Steps

1. `Main Menu → Inventory → IN-F Inventory Adjustments`
2. **Item#** — the item to adjust.
3. **Adj date** — defaults to today (must be in open period).
4. **Qty** — positive number to increase on-hand; negative to
   decrease. EVO shows current on-hand for reference.
5. **Unit cost** — for positive adjustments, the cost of the units
   being added. For negative, current average/standard cost.
6. **Reason code** — select or enter a reason (cycle count, damage,
   theft, etc.). Reason codes are user-defined in system tables.
7. **GL account override** — optional. If blank, posts to the
   default Inventory Adjustment account (`BKSY_INV_ADJACC`).
8. **Lot#** — required if item is lot-controlled.
9. F10 Post.

## What posting does

- Changes `BKICMSTR.BKIC_PROD_UOH` by the qty entered.
- If cost-method is Average, recalculates average cost.
- Posts GL: Inventory ↔ Inventory Adjustment account.
- Writes to `BKICADJ` history table.

## Bin transfer (multi-location)

To move stock from Bin A to Bin B with no net change in total on-hand,
use `IN-G Transfer Inventory` rather than two adjustments.

## Tables touched

- `BKICMSTR` — on-hand updated
- `BKICLOC` — per-bin balance updated
- `BKICADJ` — adjustment history
- `BKICTRN` — transaction log

## Related

- [[recipe-physical-inventory]] — full-cycle approach
- [[module-IN]]
- [[table-BKICMSTR]]
""",
["adjust inventory", "in-f", "inventory adjustment", "cycle count correction",
 "write off", "on-hand", "stock adjustment", "damage write-off"]),

("recipe-ar-aging", "Run an AR Aging Report", "AR",
["Main Menu", "Accounts Receivable", "AR-L-A AR Aging"],
"""
The AR Aging shows how old your open customer balances are —
organized into current, 30, 60, 90, and 90+ day buckets.
Run it to prioritize collections and review credit exposure.

## Steps

1. `Main Menu → Accounts Receivable → AR-L-A AR Aging`
2. **As-of date** — EVO ages balances relative to this date.
   Use today for current AR; use a prior period-end for historical.
3. **Sort by** — Customer# or Customer Name.
4. **Customer range** — leave blank for all; enter from/thru for
   a subset.
5. **Detail or summary** — Summary shows one line per customer;
   Detail shows every open invoice.
6. **Include on credit hold?** — Y to flag credit-hold customers.
7. Print or export.

## Reading the report

Each row shows:
- Customer# and Name
- Current (invoices not yet due)
- 1–30 days past due
- 31–60 days past due
- 61–90 days past due
- 91+ days past due
- Total balance

Totals at the bottom reconcile to the AR control account in GL.

## Collections workflow

- Sort by 91+ column descending to find worst-aged balances.
- Use `AR-A Enter Customers` to view the customer's credit terms
  and put on credit hold if needed.
- Use `AR-H Enter AR Notes` to log call notes per customer.

## Reconciliation

The grand total of AR Aging **must match** the GL AR control account
balance as of the same date. If they differ, run `AR-L-B AR
Reconciliation` to find the discrepancy.

## Tables touched (read only — this is a report)

- `BKARCUST` — customer master (name, terms)
- `BKARINV` — open invoices
- `BKARPAY` — applied payments

## Related

- [[recipe-record-payment]] — apply a payment to reduce aging
- [[recipe-print-statements]] — send statements to customers
- [[module-AR]]
""",
["ar aging", "ar-l-a", "aging report", "accounts receivable aging",
 "past due", "collections", "30 60 90", "open invoices"]),

("recipe-financial-statements", "Print Financial Statements", "AM",
["Main Menu", "Accounting Manager", "AM-F Financial Statements"],
"""
Generate the Balance Sheet, Income Statement (P&L), and (optionally)
Statement of Cash Flows from EVO's General Ledger.

## Prerequisites

- All journals posted and period closed for the reporting period.
- Financial statement formats defined in `AM-D Statement Format`
  (groups GL accounts into line items like "Total Revenue",
  "Cost of Goods Sold", etc.).

## Steps

1. `Main Menu → Accounting Manager → AM-F Financial Statements`
2. **Statement type** — Balance Sheet, Income Statement, or both.
3. **Period** — select the accounting period (or date range for
   mid-period interim).
4. **Comparison** — optional prior period or budget columns.
   - **Prior period** — same period last year (year-over-year).
   - **Budget** — requires budget entries in `AM-C Budget Entry`.
5. **Consolidated?** — if multi-company, roll up subsidiaries.
6. **Detail level** — Summary (by account group) or Detail
   (every account code).
7. Print or export to Excel.

## Statement format setup (AM-D)

If statements look wrong or missing accounts, the format definition
needs updating:

1. `AM-D Enter Statement Format`
2. Each format line maps a GL account range to a label and section
   (Assets, Liabilities, Equity, Revenue, Expense).
3. Add new account ranges after creating new GL accounts.

## Period-end checklist before printing

- All AP vouchers entered and posted.
- All AR cash receipts posted.
- Bank reconciliation complete (`GL-F Bank Reconciliation`).
- Payroll posted (if EVO handles payroll).
- Depreciation posted (if EVO handles fixed assets).
- All WO receipts and issues posted.
- Inventory adjustments posted.

## Tables touched (read only — this is a report)

- `BKGLMSTR` — GL account master
- `BKGLHIST` — posted GL transaction detail
- `BKAMFMT` — financial statement format definitions
- `BKAMBUDG` — budget amounts (if comparison used)

## Related

- [[recipe-month-end-close]]
- [[module-AM]]
- [[module-GL]]
""",
["financial statements", "balance sheet", "income statement", "p&l",
 "profit and loss", "am-f", "financial report", "gl report",
 "accounting manager", "period end report"]),

("recipe-login", "Start EVO and Sign In", "SY",
["Desktop shortcut or C:\\ISTS\\StartEvo.exe"],
"""
How to launch EvoERP and log into a company.

## Steps

1. Double-click the **EvoERP** shortcut on your desktop, or run
   `C:\\ISTS\\StartEvo.exe`.
2. `StartEvo.exe` checks the local install, reads `taspro7.ini`, and
   launches `tp7runtime.exe` against the main menu program
   (`EvoERPmenu.RWN` on the network share).
3. The **Login** screen appears. Enter:
   - **Company code** — 1- or 2-character company identifier (e.g.,
     `01`). If there is only one company, this may default.
   - **User ID** — your EVO user code (case-insensitive).
   - **Password** — your EVO password.
4. Press Enter or click **Login**.
5. On success, the EvoERP main menu appears, showing all modules
   your user profile permits.

## Single Sign-On (SSO)

If your site has Windows Domain Authentication enabled
(`ISTS.CFG.SSO = Y`), EVO may fill the User ID from your Windows
login automatically. Confirm and press Enter.

## First login / forced password change

On first login or after an admin password reset, EVO forces you to
choose a new password before proceeding.

## Remember Me

Check **Remember Me** (`REMEMBER.ME` flag) to save your company and
user ID for the next login — password is never saved.

## Idle timeout

EVO automatically logs out after 10 minutes of inactivity
(`TENMIN.KILLER` timer). Any keypress resets the clock.

## Troubleshooting

| Symptom | Likely cause |
|---------|-------------|
| "Cannot connect to server" | Network share `\\\\server\\DBAMFG$` unreachable |
| "Invalid user" | User code doesn't exist in `BKSYUSER` |
| "Invalid password" | Password mismatch; see admin for reset |
| Blank screen / crash | `tp7runtime.exe` or `qtintf70.dll` version mismatch |
| "License exceeded" | Too many concurrent users (TAS Pro 7 seat count) |

## Related

- [[module-SY]] — system administration including user setup
- [[recipe-add-user]] — create a new user account
""",
["login", "sign in", "start evo", "launch evo", "startevo", "password",
 "company code", "user id", "sso", "single sign-on"]),

("recipe-rma", "Process a Customer Return (RMA)", "SO",
["Main Menu", "Sales Orders", "SO-J Enter RMAs"],
"""
Record goods returned by a customer. EVO creates a Return Material
Authorization (RMA) to track the return, restores inventory, and
generates a credit memo to reduce the customer's balance.

## Prerequisites

- Original SO or invoice number (helpful but not required).
- Customer exists in `BKARCUST`.
- Returned items exist in `BKICMSTR`.

## Steps

### 1. Create the RMA — SO-J

1. `Main Menu → Sales Orders → SO-J Enter RMAs`
2. **RMA#** — EVO assigns next sequential number.
3. **Customer#** — the customer returning goods.
4. **Original SO#** — enter if known; links return to original sale.
5. **RMA date** — date customer notified / shipped return.
6. **For each returned line:**
   - **Item#** — what they're returning.
   - **Qty returned** — units coming back.
   - **Reason code** — defective, wrong item, overshipment, etc.
   - **Disposition** — `R` Restock, `S` Scrap, `R` Repair/Rework.
7. F10 Post. EVO prints an RMA acknowledgment to send to the customer.

### 2. Receive the Return — SO-K

When goods physically arrive:

1. `Main Menu → Sales Orders → SO-K Receive RMAs`
2. Enter the **RMA#**. Confirm quantities received.
3. EVO puts stock back into inventory (if disposition = Restock):
   increments `BKICMSTR.BKIC_PROD_UOH`.
4. F10 Post.

### 3. Credit Memo — SO-L (or AR-D)

After receiving the return, issue the customer a credit:

1. `Main Menu → Sales Orders → SO-L Enter Credit Memos`
2. Reference the **RMA#**. EVO fills customer, items, and amounts.
3. Adjust amount if partial credit (restocking fee, etc.).
4. F10 Post — creates a credit in `BKARINV` with negative amount.
   Customer balance decreases. GL: Credit AR, Debit Revenue (reversal).

## Tables touched

- `BKSORMA` — RMA header
- `BKSORMAD` — RMA detail lines
- `BKARINV` — credit memo record
- `BKICMSTR` — on-hand restored (Restock disposition)

## Related

- [[recipe-enter-so]]
- [[recipe-so-pick-ship]]
- [[recipe-record-payment]]
- [[module-SO]]
- [[module-AR]]
""",
["rma", "return", "so-j", "customer return", "credit memo", "return material",
 "refund", "return goods", "so-k", "receive return"]),

("recipe-so-to-cash", "SO-to-Cash End-to-End", "SO",
["Main Menu", "Sales Orders / Accounts Receivable"],
"""
The complete order-to-cash cycle: enter an order, ship it, invoice
the customer, and collect payment.

## Overview

```
SO-A Enter Order
  ↓
SO-B Print Pick Tickets
  ↓
SO-C Ship / Create Invoice
  ↓
SO-D Print Invoice
  ↓
(Customer pays)
  ↓
AR-C Enter Cash Receipts
```

## Step 1 — Enter the Order (SO-A)

See [[recipe-enter-so]] for full detail. Key: confirm pricing,
customer credit limit, and requested ship date before posting.

## Step 2 — Pick the Order (SO-B)

Print pick tickets for the warehouse. Stock is still in inventory;
no GL entry yet.

## Step 3 — Ship and Invoice (SO-C)

Enter shipped quantities. EVO:
- Deducts stock from `BKICMSTR`
- Creates the invoice in `BKARINV` / `BKARINVL`
- Posts GL: **DR** AR, **CR** Revenue; **DR** COGS, **CR** Inventory

If the SO is only partially filled, the remainder stays as an open
backorder. Run SO-C again when the rest ships.

## Step 4 — Print the Invoice (SO-D)

Print and mail (or email) the invoice to the customer. EVO marks the
invoice as printed. Some sites also email a PDF from the report
printer driver.

## Step 5 — Collect Payment (AR-C)

When the customer's check (or EFT) arrives:
1. `Main Menu → AR → AR-C Enter Cash Receipts`
2. Enter **Customer#**, **Payment amount**, **Check#**, **Date**.
3. EVO shows open invoices. Apply payment to specific invoices
   (full or partial). Unapplied balance goes to a suspense bucket.
4. F10 Post — closes the matched invoices.

## Typical GL flow

| Event | Debit | Credit |
|-------|-------|--------|
| Ship | AR | Revenue |
| Ship | COGS | Inventory |
| Cash receipt | Cash | AR |

## Discounts

If the customer pays within terms (e.g., 2/10), enter the discount
amount at AR-C. EVO posts the difference to a Sales Discount account.

## Related

- [[recipe-enter-so]]
- [[recipe-so-pick-ship]]
- [[recipe-record-payment]]
- [[recipe-ar-aging]]
- [[module-SO]]
- [[module-AR]]
""",
["order to cash", "so to cash", "otc", "ship invoice collect",
 "sales cycle", "end to end so", "ar cash receipt"]),

("recipe-transfer-stock", "Transfer Stock Between Bins or Locations", "IN",
["Main Menu", "Inventory", "IN-G Transfer Inventory"],
"""
Move on-hand inventory from one bin or warehouse location to another
without changing the total quantity on hand.

## When to use

- Reorganizing warehouse storage.
- Moving finished goods from production floor to finished-goods
  bin after a work order receipt.
- Consolidating partial bins.
- Moving slow items to overflow or off-site storage.

## Steps

1. `Main Menu → Inventory → IN-G Transfer Inventory`
2. **Item#** — the item to move.
3. **From Location / Bin** — current storage location.
4. **To Location / Bin** — destination.
5. **Qty to transfer** — how many units to move. EVO validates that
   the From location has at least this quantity.
6. **Transfer date** — defaults to today.
7. **Lot#** — if lot-controlled, specify which lot is moving.
8. F10 Post.

## What posting does

- Decrements `BKICLOC` at the From location.
- Increments `BKICLOC` at the To location.
- `BKICMSTR.BKIC_PROD_UOH` total is unchanged.
- No GL entry — this is a physical move, not a cost event.
- Writes to `BKICTRN` (transaction log).

## Multi-warehouse transfers

If moving between separate warehouse codes (not just bins within
the same warehouse), EVO may require both a **Transfer Out** and a
**Transfer In** step depending on your site's multi-location
configuration. Check `T7MDefaults` for `MULTI_WH` flag.

## Tables touched

- `BKICLOC` — per-bin balance updated (both from and to)
- `BKICTRN` — transaction log entry

## Related

- [[recipe-adjust-inventory]]
- [[recipe-physical-inventory]]
- [[module-IN]]
- [[table-BKICMSTR]]
""",
["transfer stock", "move inventory", "in-g", "bin transfer", "location transfer",
 "warehouse transfer", "move stock", "relocate inventory"]),

("recipe-close-po", "Close or Cancel a Purchase Order", "PO",
["Main Menu", "Purchase Orders", "PO-E Close/Cancel POs"],
"""
Close a PO that is fully received, or cancel lines/POs you no longer
need. Closing removes the open quantity from on-order balances.

## When to use

- Vendor delivered the full order → PO should auto-close at final
  receipt, but use PO-E if it stays open.
- You are canceling an order the vendor can no longer fill.
- Clearing old unreceived POs to clean up the open PO report.

## Steps

### Close (fully received)

1. `Main Menu → Purchase Orders → PO-E Close Purchase Orders`
2. Enter the **PO#**.
3. EVO shows header and any lines with remaining open qty.
4. Select **Close All** to close the entire PO, or close individual
   lines selectively.
5. F10 Post.

### Cancel (not yet received)

Same path as Close. Set close reason to **Cancel** (or the
site-defined cancel code). EVO:
- Sets PO line status to `C` (Cancelled).
- Decrements `BKICMSTR.BKIC_PROD_UOPO` by the cancelled qty.
- No receiving entry is created.
- No cost is posted to GL (nothing was received).

## Impact on MRP

Cancelled PO lines no longer count as supply in MRP. If MRP
previously relied on this PO to cover demand, the next MRP run
will generate a new planned order to cover the gap.

## Partial close

Close only specific lines (e.g., items delivered; remove balance
you know won't ship). Leave other lines open.

## Tables touched

- `BKPOMSTR` — PO status updated
- `BKPOLINE` — line status updated
- `BKICMSTR` — UOPO decremented by cancelled qty

## Related

- [[recipe-enter-po]]
- [[recipe-receive-po]]
- [[module-PO]]
""",
["close po", "cancel po", "po-e", "cancel purchase order",
 "close purchase order", "cancel order", "po closeout"]),

("recipe-year-end-close", "Year-End Close", "AM",
["Main Menu", "Accounting Manager", "AM-M Year-End Close"],
"""
Close the fiscal year in EvoERP's General Ledger. This zeroes
out income and expense accounts and carries the net income
into Retained Earnings.

## Prerequisites

- All 12 (or 13) accounting periods for the fiscal year are closed
  ([[recipe-month-end-close]]).
- Audited financials signed off.
- Backup created ([[recipe-backup]]) — year-end is not easily reversed.
- No open journals or unposted batches.

## Steps

1. `Main Menu → Accounting Manager → AM-M Year-End Close`
2. EVO displays the **fiscal year** to be closed (confirm it's the
   right year).
3. **Retained Earnings account** — confirm the GL account that will
   receive the net income/loss transfer.
4. EVO shows a pre-close checklist summary:
   - All periods closed? ✓/✗
   - Unposted batches? ✓/✗
5. Type `YES` to confirm (or equivalent confirmation prompt).
6. EVO performs the close:
   - Zeros all Revenue and Expense accounts.
   - Transfers net income to Retained Earnings.
   - Rolls forward opening balances for Balance Sheet accounts.
   - Archives prior-year GL history to `BKGLHIST` with year-end
     flag.
7. After close, the new fiscal year is set as current.

## What changes after close

- P&L accounts (Revenue, Expense) start the new year at zero.
- Balance Sheet accounts (Assets, Liabilities, Equity) carry forward
  their ending balances.
- Prior-year comparatives remain accessible in AM-F with
  "Prior Year" comparison option.
- `BKAMFPRD` period table is updated: old year's periods locked,
  new year's first period opened.

## Cannot undo

Year-end close is permanent. If you must reopen a prior year:
- Restore from backup and re-close — or —
- Manually post a correcting journal in the new year.

## Tables touched

- `BKGLMSTR` — account balances zeroed (P&L) or carried forward
- `BKGLHIST` — year-end archive entries
- `BKAMFPRD` — period table updated

## Related

- [[recipe-month-end-close]]
- [[recipe-financial-statements]]
- [[module-AM]]
- [[module-GL]]
""",
["year end close", "fiscal year close", "year-end", "am-m",
 "close fiscal year", "year end", "retained earnings close"]),

("recipe-void-check", "Void a Check", "AP",
["Main Menu", "Accounts Payable", "AP-J Void Checks"],
"""
Void a printed check — either because it was lost, misprinted,
or issued in error. Voiding reverses the payment and reopens
the vendor invoice.

## Prerequisites

- Know the check number and check date.
- The period the check was in must be open, OR you have override
  authority to post into a closed period.

## Steps

1. `Main Menu → Accounts Payable → AP-J Void Checks`
2. **Check#** — enter the check number to void.
3. **Check date** — EVO looks up the check and confirms vendor and
   amount.
4. **Void date** — the date the void is posted (defaults to today).
   This determines which period absorbs the reversal.
5. **Reason** — optional text note (for audit trail).
6. F10 Post.

## What posting does

- Marks the check as `VOID` in `BKAPCHKS`.
- Reverses the GL cash entry: **DR** AP, **CR** Cash.
- Reopens the original vouchers (invoices) that the check paid;
  they return to `BKAPOPEN` as unpaid.
- The vendor's balance increases by the voided amount.

## Re-issuing

After voiding, re-issue a replacement check through the normal
`AP-I Print Checks` flow ([[recipe-print-checks]]).

## Partial void

EVO does not support partial check voids. If a check covered
multiple invoices and only some are wrong, void the entire check
and re-issue for the correct invoices only.

## Tables touched

- `BKAPCHKS` — check record marked VOID
- `BKAPOPEN` — voided invoices returned to open status
- `BKGLHIST` — reversal GL entries posted

## Related

- [[recipe-print-checks]]
- [[recipe-enter-voucher]]
- [[module-AP]]
""",
["void check", "ap-j", "void payment", "cancel check",
 "lost check", "check reversal", "voided check"]),

("recipe-add-user", "Add a New EVO User", "SY",
["Main Menu", "System", "SY-A Enter Users"],
"""
Create a new user account so someone can log into EvoERP.

## Prerequisites

- You must be logged in as an admin-level user (or have SY module access).
- Know what modules and functions the new user needs.

## Steps

1. `Main Menu → System → SY-A Enter Users`
2. **User ID** — 1–8 char code, typically the person's initials or
   first name (e.g., `JSMITH`). This is what they type at login.
3. **Full name** — displayed in menus and reports.
4. **Password** — temporary password; user will be prompted to change
   on first login if `Force Password Change = Y`.
5. **Access level** — numeric level (1–9 typically). Higher = more
   authority. Affects which menus and overrides are available.
6. **Module access** — list of module codes this user can access.
   Blank/all = full access (admin). Restrict sensitive modules
   (e.g., AP, GL, SY) for non-admin users.
7. **Default company** — which company this user logs into by default.
8. **Windows login** (SSO) — if Single Sign-On is enabled, enter the
   user's Windows domain username to link accounts.
9. F10 Post.

## Restrict menu items

Beyond module-level access, use `SY-B Menu Restrictions` to hide
specific sub-menu items from a user or group.

## Password policy

- Passwords are stored hashed in `BKSYUSER`.
- Admins can reset (but not view) passwords via SY-A.
- Minimum length and complexity rules are set in `T7MDefaults`.

## Tables touched

- `BKSYUSER` — user master record

## Related

- [[recipe-login]]
- [[recipe-add-company]]
- [[module-SY]]
""",
["add user", "new user", "sy-a", "create user", "user account",
 "user setup", "user id", "password reset", "user access"]),

("recipe-backup", "Back Up EVO Data", "TA",
["Main Menu", "Utilities / Admin", "TA-O Evo Backups"],
"""
Create a backup of EvoERP company data. EVO supports local ZIP
backups and (with the cloud module) automatic upload to i2 tech
support servers.

## When to back up

- Before any major operation: year-end close, large data imports,
  system updates.
- On a regular scheduled basis (daily recommended for production
  data).
- Before running a Physical Inventory post.

## Steps (manual backup)

1. `Main Menu → Utilities → TA-O Evo Backups`
2. **Backup type** — select:
   - **Full** — all company data files.
   - **Company** — specific company(ies) only.
   - **Custom** — user-defined file list.
3. **Zip file name / path** — where to save the `.zip` file.
   Default is usually a network backup folder.
4. For **Company** type, check the companies to include.
5. Click **Start Backup** (or equivalent action button).
6. EVO creates a ZIP archive using the TZipMaster VCL component.
   Progress is shown in the status area.

## Cloud backup (GS_BACKUP flag)

If your site has cloud backup enabled, EVO automatically:
1. Creates the local ZIP.
2. Uploads to `https://login.istechsupport.com/api/v1/evo/backups/`
   in multi-part chunks with SHA-256 integrity verification.
3. Shows upload progress and confirms success.

## Scheduled backups

Click **Schedule** to configure recurring automatic backups.
Requires the EVO scheduler service to be running.

## Restore

Restore is handled by i2 technical support for production data.
For test/dev, extract the ZIP and place files back in the
appropriate company folder on the network share.

## What's in the ZIP

- All `.B` (Btrieve) data files for the selected companies.
- `*.DFM`, `*.DCY` dictionary files (if a Full backup).
- Does NOT include `.RWN` program files (those are the application,
  not data).

## Related

- [[recipe-add-company]]
- [[recipe-update-evo]]
- [[module-TA]]
""",
["backup", "ta-o", "evo backup", "zip backup", "cloud backup",
 "data backup", "backup company", "schedule backup"]),

("recipe-add-company", "Add a New Company in EVO", "SY",
["Main Menu", "System", "SY-C Add Company"],
"""
Create a new company code in EvoERP. Each company has its own set
of data files and GL chart of accounts.

## When to add a company

- New legal entity or subsidiary.
- Setting up a test/training company (common prefix: `TS`, `TEST`).
- Creating a new fiscal year rollover copy for experimentation.

## Prerequisites

- Admin access (SY module).
- Know the 1–2 character company code (e.g., `02`, `AB`).
- Have a template company to copy from, OR plan to set up from scratch.

## Steps

1. `Main Menu → System → SY-C Add Company` (or equivalent admin utility)
2. **Company code** — 1–2 alphanumeric chars. This becomes the
   suffix on all data files (e.g., `BKICMSTR.B02` for company `02`).
3. **Company name** — full legal name; appears on reports and invoices.
4. **Copy from** — select an existing company to copy GL accounts,
   system defaults, and user-defined tables from. Or select NONE
   to start empty.
5. **Create data files** — EVO creates blank Btrieve files for every
   required table in the new company's folder.
6. Confirm.

## After adding

- Set up System Defaults in `T7MDefaults` for the new company.
- Define the fiscal calendar in `AM-A Accounting Periods`.
- Assign the default GL accounts for AR, AP, Inventory, etc.
- Grant user access to the new company code ([[recipe-add-user]]).

## Multi-company data isolation

Each company's files are physically separate on the network share
(separate directory or separate file-suffix convention). There is
no data bleed between companies unless you explicitly use
inter-company GL transfers.

## Related

- [[recipe-add-user]]
- [[recipe-backup]]
- [[module-SY]]
- [[module-AM]]
""",
["add company", "new company", "sy-c", "create company",
 "company setup", "multi-company", "company code"]),

]
