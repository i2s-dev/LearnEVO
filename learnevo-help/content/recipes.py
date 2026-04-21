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

]
