# Work Orders — Vendor Help Content

Status: verified (text distilled from the vendor's help file).

Source CHM: `\\i2s109-solidcrm\DBAMFG$\EVOHELP.CHM` →
[samples/chm/EvoHELP.CHM](../../../samples/chm/EvoHELP.CHM) →
decompiled to [samples/chm/extracted/](../../../samples/chm/extracted/).
Extracted via [scripts/chm_to_md.py](../../../scripts/chm_to_md.py).

This doc consolidates the **52 help topics** under the CHM's
*Manufacturing → Work Orders* category. Each program gets its
purpose, key fields / behaviors, and cross-links. The full verbatim
source is one click away via the `Source:` link on each section.

For the companion schema + menu + form view of this module, see
[README.md](README.md) in this folder.

---

## Contents

**Module overview**
- [Overview — the manufacturing sphere](#overview--the-manufacturing-sphere)

**Life-cycle programs (WO-A through WO-J)**
- [WO-A — Enter Work Orders](#wo-a--enter-work-orders)
- [WO-B — Release Work Orders](#wo-b--release-work-orders)
- [WO-C — Print Travelers](#wo-c--print-travelers)
- [WO-D — Print Pick Lists](#wo-d--print-pick-lists)
- [WO-E — Print Labor Cards / Labels](#wo-e--print-labor-cards--labels)
- [WO-F — Enter Labor](#wo-f--enter-labor)
- [WO-G — Issue Materials](#wo-g--issue-materials)
- [WO-H — Enter Misc / Extra Costs](#wo-h--enter-misc--extra-costs)
- [WO-I — Enter Finished Production](#wo-i--enter-finished-production)
- [WO-J — Close / Cancel Orders](#wo-j--close--cancel-orders)

**WO-K-\* — work-order modify / synchronize / tooling**
- [WO-K-A Enter Work Order Routings](#wo-k-a-enter-work-order-routings)
- [WO-K-B Enter Work Order Bills of Material](#wo-k-b-enter-work-order-bills-of-material)
- [WO-K-C Create Multi-Date Work Orders](#wo-k-c-create-multi-date-work-orders)
- [WO-K-D Create Multi-Assy Work Orders](#wo-k-d-create-multi-assy-work-orders)
- [WO-K-E Swap Substitute Parts](#wo-k-e-swap-substitute-parts)
- [WO-K-F Edit Sequence Started / Finished Dates](#wo-k-f-edit-sequence-started--finished-dates)
- [WO-K-G Recalculate Projected Hours](#wo-k-g-recalculate-projected-hours)
- [WO-K-H Recalculate Work Order Costs](#wo-k-h-recalculate-work-order-costs)
- [WO-K-I Kitting System](#wo-k-i-kitting-system)
- [WO-K-J Synchronize Work Order to Master BOM & Routing](#wo-k-j-synchronize-work-order-to-master-bom--routing)
- [WO-K-K Edit Posted DC Labor](#wo-k-k-edit-posted-dc-labor)
- [WO-K-L Quick Work Order](#wo-k-l-quick-work-order)
- [WO-K-M Parts Requester](#wo-k-m-parts-requester)
- [WO-K-N Stockroom Program](#wo-k-n-stockroom-program)
- [WO-K-O Enter Component Serial Numbers](#wo-k-o-enter-component-serial-numbers)
- [WO-K-P Enter Component Lot Information](#wo-k-p-enter-component-lot-information)
- [WO-K-Q Convert WO to PO](#wo-k-q-convert-wo-to-po)
- [WO-K-R Issue Scrap Component](#wo-k-r-issue-scrap-component)
- [WO-K-S Assign WO to Bin](#wo-k-s-assign-wo-to-bin)

**WO-L-\* — reports**
- [WO-L-A Print Work Order Status](#wo-l-a-print-work-order-status)
- [WO-L-B Print Work Order Schedule](#wo-l-b-print-work-order-schedule)
- [WO-L-C Print Work Center Backlog](#wo-l-c-print-work-center-backlog)
- [WO-L-D Print Projected Shipments](#wo-l-d-print-projected-shipments)
- [WO-L-E Print / Post Labor to Payroll](#wo-l-e-print--post-labor-to-payroll)
- [WO-L-F Print Work Order Shortages](#wo-l-f-print-work-order-shortages)
- [WO-L-G Print Work Center by Key Component](#wo-l-g-print-work-center-by-key-component)
- [WO-L-H Print Projected vs Estimated Hours](#wo-l-h-print-projected-vs-estimated-hours)
- [WO-L-I Print Allocations](#wo-l-i-print-allocations)
- [WO-L-J Print Work Order Completions](#wo-l-j-print-work-order-completions)
- [WO-L-K Print WO Bills of Material](#wo-l-k-print-wo-bills-of-material)
- [WO-L-L Print WO Component Labels](#wo-l-l-print-wo-component-labels)
- [WO-L-M Print Material Summary](#wo-l-m-print-material-summary)
- [WO-L-N WO BOM for Purchasing](#wo-l-n-wo-bom-for-purchasing)

**Batch / posting / inquiry / defaults**
- [WO-M Batch Labor Entry](#wo-m-batch-labor-entry)
- [WO-N Post Labor Batches](#wo-n-post-labor-batches)
- [WO-O Post Material Transactions](#wo-o-post-material-transactions)
- [WO-P Batch Finished Production](#wo-p-batch-finished-production)
- [WO-Q Work Order Inquiry](#wo-q-work-order-inquiry)
- [WO-R Work Order Defaults](#wo-r-work-order-defaults)
- [WO-S Print Work Order Labels](#wo-s-print-work-order-labels)
- [WO-T Enter Rework Work Order](#wo-t-enter-rework-work-order)

---

## Overview — the manufacturing sphere

*Source: [work_orders.htm](../../../samples/chm/extracted/work_orders.htm)*

> *"Actual manufacturing takes place in the Work Orders module."*
> — vendor, on the role this module plays in EvoERP.

Work orders can be:
- **Entered manually** via [WO-A](#wo-a--enter-work-orders).
- **Converted from a sales order** via [SO-N](../../../samples/chm/extracted/so-n_convers_sales_orders_to_work_orders.htm).
- **Converted from an estimate** via [ES-E](../../../samples/chm/extracted/es-e_convert_estimates.htm).
- **Generated by MRP** via [MR-I](../../../samples/chm/extracted/mr-i_generate_work_orders.htm).

They can be **for a specific customer** or **for stock**. They can
carry **multiple start / finish dates**, or you can split them into
separate orders via [WO-K-C](#wo-k-c-create-multi-date-work-orders).

### The standard life cycle

Every work order typically goes through this sequence (not every
shop uses every step):

1. **Enter** ([WO-A](#wo-a--enter-work-orders)) — the order header:
   who, what, how many, when, estimated cost rollup.
2. **Routing** (auto-copied on create; edit via [WO-K-A](#wo-k-a-enter-work-order-routings))
   — per-sequence run/setup times, work-center assignments.
3. **Bill of material** (auto-copied on create; edit via [WO-K-B](#wo-k-b-enter-work-order-bills-of-material))
   — components and quantities.
4. **Release** ([WO-B](#wo-b--release-work-orders)) — sets actual
   start date, optionally prints shortages. Labor cannot be charged
   until released.
5. **Print travelers & pick lists** ([WO-C](#wo-c--print-travelers),
   [WO-D](#wo-d--print-pick-lists)) — shop paper.
6. **Print labor cards / labels** ([WO-E](#wo-e--print-labor-cards--labels))
   — 3×5 cards or 1×3½ labels, one per sequence.
7. **Enter labor** ([WO-F](#wo-f--enter-labor), or batch via
   [WO-M](#wo-m-batch-labor-entry)+[WO-N](#wo-n-post-labor-batches),
   or Data Collection) — actual hours vs. standard.
8. **Issue materials** ([WO-G](#wo-g--issue-materials)) — from stock
   individually or as BOM kits.
9. **Misc / extra costs** ([WO-H](#wo-h--enter-misc--extra-costs))
   — tooling, engineering, etc.
10. **Finished production** ([WO-I](#wo-i--enter-finished-production))
    — post to inventory at standard or actual cost.
11. **Close / cancel** ([WO-J](#wo-j--close--cancel-orders)).
12. **Archive** via [SM-J-B](../../../samples/chm/extracted/sm-j-b_archive_work_orders.htm)
    (referenced in [System Overview — Archiving](../../00-overview/system-overview.md#10-archiving-or-purging-old-data)).

### Status codes at a glance

| Code | Meaning | Key effect |
|---|---|---|
| **S** | Scheduled | Future; no BOM/routing yet; nothing allocated, no WC backlog. |
| **F** | Firmed | BOM + routing created; components **allocated**; labor in WC backlog; material can be issued but **labor cannot be charged**. |
| **R** | Released | Live on the shop floor; actual start date set; labor can be charged. |
| **C** | Closed | Complete; no more transactions allowed. |
| **X** | Canceled | All transactions (except labor) reversed; no more transactions. |
| **I** | Indirect | Downtime / vacation / sick / R&D tracking. Usually in a separate number sequence. Materials can also be issued to type-I WOs. |

### Cross-module connections

- **Features & Options** — custom product options from SO flow
  automatically into WO BOMs via [SO-N](../../../samples/chm/extracted/so-n_convers_sales_orders_to_work_orders.htm).
- **Data Collection** — alternative to WO-F/WO-M for floor-entered labor.
- **Payroll** — hours can be pushed via [WO-L-E](#wo-l-e-print--post-labor-to-payroll).
- **Accounts Payable** — vendor invoices on PO-tied components via [AP-C](../../../samples/chm/extracted/ap-c_enter_purchase_order_invoices.htm)
  can affect WO cost after close; residual posts to **WIP Variance**
  defined at [AD-A](../../../samples/chm/extracted/ad-a_general_ledger_defaults.htm).

The module works equally well for **job shops, make-to-stock, and
custom (make-to-order)** — per the vendor's own positioning.

---

## WO-A — Enter Work Orders

*Source: [wo-a_enter_work_orders.htm](../../../samples/chm/extracted/wo-a_enter_work_orders.htm)*

**Purpose.** Create, edit, view, or copy work orders. Also serves as
an inquiry screen (read-only alternative: [WO-Q](#wo-q-work-order-inquiry) /
[DC-I](../../../samples/chm/extracted/dc-i_work_order_inquiry.htm), which
don't lock records).

### Key header fields

- **Work Order Number** — 6-char numeric **prefix** + 3-char numeric
  **suffix**. Prefix = "job"; suffix = "sub-job". Auto-assigned but
  overridable (manual override doesn't reset the counter). All WOs
  created from one SO share a prefix; multi-date / multi-assy WOs
  share a prefix.
- **Status** — S/F/R/C/X/I (see table in Overview).
- **Priority** — 1/2/3 default (high/med/low). Extendable via
  [SM-P-G](../../../samples/chm/extracted/sm-p-g_enter_wo_priority_codes.htm).
  Used by [WO-L-B](#wo-l-b-print-work-order-schedule), [WO-L-C](#wo-l-c-print-work-center-backlog),
  and [SH-P Lead Time Scheduling](../../../samples/chm/extracted/sh-p_lead_time_scheduling.htm)
  (priority → work-center queue time).
- **Class** — 1-char user-defined classifier, filterable on reports.
- **Location** — must already be a valid Location and the item must
  already be assigned there via [IN-L-B](../../../samples/chm/extracted/in-l-b_enter_assign_locations.htm).
- **Part #** — must exist in the inventory file. For non-stock or
  Indirect WOs, use a **dummy item number**.
- **Quantity to Make** / **Quantity Completed** (auto-updated by [WO-I](#wo-i--enter-finished-production)).
- **Multiple Dates** — unlimited start/finish/quantity triples;
  later split via [WO-K-C](#wo-k-c-create-multi-date-work-orders).
- **Start / Finish / Due dates**:
  - **Due Date** = when the items are needed (= SO Customer Due Date
    if customer order; = demand date if for stock).
  - **Finish Date** = when they're scheduled to be completed.
  - Forward vs backward scheduling flag lives in
    [SD-B Work Orders Defaults](../../../samples/chm/extracted/sd-b_work_order_defaults.htm).
  - Shop calendar ([SM-H](../../../samples/chm/extracted/sm-h_enter_shop_calendar.htm))
    is honored — non-work dates are skipped.
  - **WO start date can never be prior to today.**
- **Customer / Attn / PO / Job # / Quote # / SO #** — cross-link
  references. Pressing Enter twice on Cust auto-fills "STOCK".
- **Price / UM** — used by Job Cost reports; doesn't print on traveler.
- **Change Order Number** — user can increment on every save.

### Estimated vs Actual costs

Seven cost buckets: **material, labor, setup, outside processing,
fixed OH, variable OH, misc, extra** (+ total).
- **Estimated** — computed via cost rollup against WO BOM + routing,
  *or* pulled from the Estimating quote if the Quote # is populated,
  *or* entered manually.
- **Actual** — posted real-time by [WO-F](#wo-f--enter-labor) /
  [WO-G](#wo-g--issue-materials) / [WO-H](#wo-h--enter-misc--extra-costs) /
  [PO-C](../../../samples/chm/extracted/po-c_receive_purchase_orders.htm) /
  [WO-N](#wo-n-post-labor-batches) / [DC-H](../../../samples/chm/extracted/dc-h_post_labor_transactions.htm).
- **Variance** + **% variance** are displayed against estimate.

### Save-time processing

On save of a **new** F/R order:
1. Parent item's **On Work Order** field is incremented.
2. WO routing + WO BOM get created (unless status S).
3. Estimated labor/setup **hours** are added to the backlog of every
   work center used.
4. Each BOM component's **Allocated** field increases by its total
   required quantity.
5. If asked "recalculate estimated costs?" → roll up current standard
   rates × routing time + current standard costs × component quantity.

On **status transition S → F/R**: BOM + routing are created and
allocations made. Reverse transition **F/R → S** strips BOM/routing
and reverses all allocations — **only allowed if no transactions
have been processed** against the WO.

On **close (→ C)**:
- **On Work Order** reversed for uncompleted remainder.
- Remaining estimated labor/setup stripped from WC backlog.
- Remaining BOM allocations reversed; any excess In-WIP reversed.
- **Cannot close** a WO with unreceived POs or unposted labor.

On **cancel (→ X)**: same as close, plus any Allocated amounts for
non-issued materials are reversed. Same guard on unreceived POs /
unposted labor.

### Deleting a work order

Only path: change status to X through [WO-J](#wo-j--close--cancel-orders),
then **purge** via [SM-J-E Purge Work Orders](../../../samples/chm/extracted/sm-j-e_purge_work_orders.htm).
This is the only way to reverse material issues **and** remove the
WO's BOM, routing, and related files completely.

### Reopening a closed / canceled WO

Bring it up, change Status from C/X to F or R, save. The WO becomes
live again — On Work Order, WC backlog, and Allocated fields all get
restored for the remaining quantity.

### Copying

**Copy WO** button lets you clone the WO. If the source is a `-1`
WO, you can optionally copy all dash-numbered siblings. You have to
edit start/finish dates on the new copies manually.

### Phantom components

If a BOM entry is **type B (phantom)**, its first-level components
are copied into the WO BOM — the phantom parent itself is **not**.

### Inquiry buttons

While a WO is on screen: **Materials (F5)**, **Labor (F6)**,
**Out Proc (F7)** pop up status panes. The vendor recommends
[DC-I](../../../samples/chm/extracted/dc-i_work_order_inquiry.htm) for
inquiry because WO-A locks records.

---

## WO-B — Release Work Orders

*Source: [wo-b_release_work_orders.htm](../../../samples/chm/extracted/wo-b_release_work_orders.htm)*

**Purpose.** Change status S→F or F→R (or reverse) for a range of
WOs, with an optional shortage report.

**Behavior:**
- When released, an **actual start date** is automatically written.
- Only **Released** WOs accept labor charges.
- Filters: work order range, start-date range.
- Default target status is **R**.
- Final report lists the released WOs and (optionally) component
  shortages.
- Shortage columns: **Required** (this WO) vs **Allocated** (total
  across all open WOs). You can have enough inventory for this WO
  *but* be taking it from another WO that needs it.

---

## WO-C — Print Travelers

*Source: [wo-c_print_travelers.htm](../../../samples/chm/extracted/wo-c_print_travelers.htm)*

**Purpose.** Print the shop traveler — the paper document that
travels with the order around the shop floor.

**Traveler sections:**

| Section | Content |
|---|---|
| **Header** | WO #, item, start/finish, customer, SO, PO, etc. |
| **Specifications** | Inventory specs from [IN-B](../../../samples/chm/extracted/in-b_enter_inventory.htm). |
| **Instructions / Notes** | Notes tied to the item, WO, related SO, or customer, filtered by Note Type flagged to print on traveler. |
| **Work Order Schedule** | Multiple start/finish/qty if defined. |
| **Job Schedule** | Other WOs sharing the same prefix — for cross-ref. |
| **Routing** | All sequences with optional QC sign-off fields. Components can print within their sequence. |
| **Bill of Materials** | All components + total qty. Phantom assemblies broken out. BOM remarks included if flagged. |
| **Options Selected** | Features & Options selections, if present. |
| **Linked Documents** | Images print as thumbnails; PDF/DOC print after the traveler. |

**Key operation flags:**
- Active vs Archived.
- Unprinted-only.
- Status default: R & F (you rarely reprint C/X).
- Bar code (WO + sequence) for DC scanning.
- BOM remarks, F&O comments, job schedule, short form, drawing /
  revision / ECO, multi-routing page breaks, ascending/descending
  sequence order.
- Defaults: [SD-B Work Orders Defaults](../../../samples/chm/extracted/sd-b_work_order_defaults.htm).

---

## WO-D — Print Pick Lists

*Source: [wo-d_print_pick_lists.htm](../../../samples/chm/extracted/wo-d_print_pick_lists.htm)*

**Purpose.** List components to pull from stock.

**Key behaviors:**
- Repeated components are **consolidated** (unlike the traveler BOM).
- Prints **quantity remaining** to issue — run mid-WO and it only
  lists what's still needed.
- A range of WOs can be rolled into **one** consolidated pick list
  (which excludes parent parts within the range to avoid double-
  counting subassemblies).
- **"Parent Assemblies Outside the WO Selection Range"** section
  appears at the bottom for references to lower-level WOs not in
  the selected range.
- Can print approved substitutes below each standard component.
- Options: sort by item or bin, second description line, RoHS
  filter, on-hand column, blank lines for hand-writing, linked docs.

---

## WO-E — Print Labor Cards / Labels

*Source: [wo-e_print_labor_cards_labels.htm](../../../samples/chm/extracted/wo-e_print_labor_cards_labels.htm)*

**Purpose.** Print 3×5 labor cards (Avery 4167) or 1×3½ adhesive
labels — one per sequence. Workers log start/stop and pieces on
them; the shop gathers them daily and types them in via
[WO-F](#wo-f--enter-labor) or [WO-M](#wo-m-batch-labor-entry).

**Operation:** WO range, card ("L") or label ("A"), quantity per
operation. Printing extras is common practice.

---

## WO-F — Enter Labor

*Source: [wo-f_enter_labor.htm](../../../samples/chm/extracted/wo-f_enter_labor.htm)*

**Purpose.** Single-transaction labor entry with advanced options
(machine, rework, QC codes, team, scrap codes).
Alternative: [WO-M](#wo-m-batch-labor-entry) for fast entry of just
times + quantities.

### Fields

- **Work Date** — default today; sticks across entries.
- **Employee No** — sticks across entries.
- **Work Order / Sequence No**.
- **Machine** — only used with manual machine scheduling.
- **Reg / Over / Dbl** — R/O/D (default R). Plus H/S/V for Indirect WOs.
- **Shift** — default 1.
- **# Jobs Worked** — divides labor rate so WOs aren't overcharged
  when an employee runs multiple jobs simultaneously.
- **Setup? + Setup Hours** — Y bypasses run-hour fields.
- **Rework? + QC Code** — Rework triggers QC-code prompt.
- **Run Hours** (decimal).
- **% Complete** — current status (not delta); program calculates delta.
- **Qty Completed** — or derived from % Complete.
- **# Persons / Team** — divides quantity completed. **Important:**
  when a work center is team-operated, set its overhead rate at
  [RO-C](../../../samples/chm/extracted/ro-c_enter_work_centers.htm)
  on a machine/WC basis, not per-employee, since the overhead also
  gets divided by this field.
- **Qty Scrapped + Scrap Code** — unplanned scrap. If defaults say
  "close short by scrap quantity", the start qty from this sequence
  onward shrinks. To instead issue replacement material, use scrap
  qty in [WO-G](#wo-g--issue-materials).
- **Is this sequence now complete?** — flag that tells scheduling to
  stop considering it.

### Editing previous entries

`F2` in Work Date → list from that date forward → highlight → Enter
→ prompted to back out. Accept to fully reverse, then re-enter.
To delete: back out, then Esc without re-entering.

### Save-time processing

- Labor + setup hrs × rate (employee wage or WC standard, per
  [SD-B](../../../samples/chm/extracted/sd-b_work_order_defaults.htm)).
- Overhead = hourly rate OR % of labor.
- Hours + qty post to WO routing record for the sequence; % Complete
  recalculated.
- Costs post to WO header; variances recalculated.
- Machine run hours post to [MACHINE](../04-data-dictionary/file-names-index.md#routings)
  table; tool qty post to [TOOL](../04-data-dictionary/file-names-index.md#routings).
- GL: debit WIP, credit absorbed labor/overhead from item class.

### Common pitfall

*If you arrow-up past a blank Work Order field, the program blocks
you because blank isn't valid. Workaround: type any valid value
(without pressing Enter), then arrow up.* — vendor-documented gotcha.

---

## WO-G — Issue Materials

*Source: [wo-g_issue_materials.htm](../../../samples/chm/extracted/wo-g_issue_materials.htm)*

**Purpose.** Issue components from stock to a WO, individually or
as BOM kits. Not for PO-tied materials — those bypass inventory and
auto-issue on [PO-C](../../../samples/chm/extracted/po-c_receive_purchase_orders.htm).

### Three issue modes

| Mode | Behavior |
|---|---|
| **Individual** (N) | Screen opens with all issue qtys = 0; manual entry. |
| **Kit** (Y) | Suggests the full required qty regardless of on-hand; can drive stock negative. |
| **List** (L) | Suggests `min(required, on-hand)` — never drives stock negative. |

- If an item has a PO tied to this WO, the suggested issue accounts
  for the PO'd quantity.
- Entering **0 sets + Kit or List** issues enough to bring all
  components to 100% issued (useful after partial prior issues).
- **Add button** on the components screen lets you add a non-BOM
  component on the fly (with confirmation to also save to BOM).

### Lot / Serial control

- **Lot-required** component pauses for a lot number. If not on file,
  prompt to add.
- **Serial-required** component pauses once per unit. Unknown serials
  can be added on the fly.

### Component record locks

If another user holds a lock on a required file, that component's
issue goes to a **temp file** instead of aborting. Post later via
[WO-O](#wo-o-post-material-transactions). **Job costing isn't
correct and the WO can't close until WO-O is run.** The vendor
recommends running WO-O daily at end of day.

### Reversing / deleting

Click **Reverse** (lower left), choose WO issue vs PO receipt,
specify WO / Date / Component. Pick the transaction, confirm
back-out, re-enter or Esc to delete.

### GL impact

- Cost = current inventory **average cost** × qty.
- On-Hand decreased, **In-WIP increased**, Allocated decreased.
- Item-class asset account credited, WO parent's WIP account debited.
- Lot / serial master tables updated as applicable.

---

## WO-H — Enter Misc / Extra Costs

*Source: [wo-h_entermisc_extra_costs.htm](../../../samples/chm/extracted/wo-h_entermisc_extra_costs.htm)*

**Purpose.** Post actual misc or extra costs against a WO. Compared
to estimate in [JC-A](../../../samples/chm/extracted/jc-a_print_job_cost_report.htm).

- **Misc costs** are tied to specific routing sequences (e.g. tooling).
- **Extra costs** are tied to the estimate as a whole (engineering,
  letter of credit, packaging…).

Default GL accounts at [AD-A](../../../samples/chm/extracted/ad-a_general_ledger_defaults.htm)
(override on entry). **Processing:** debit WIP (item class), credit
the misc / extra GL account.

---

## WO-I — Enter Finished Production

*Source: [wo-i_enter_finished_production.htm](../../../samples/chm/extracted/wo-i_enter_finished_production.htm)*

**Purpose.** Receive finished goods (or subassemblies) back into
inventory. Partial completions allowed. Per transaction, you choose
whether to update inventory average cost at **standard** or **actual**.

### The "rebuild summarized actual costs" prompt

When saving a receipt you're asked:

> "Do you wish to rebuild the summarized actual costs in WO-A from
> the detail transaction files?"

The WO-A **Actual** column totals are used as the balancing basis
for the final-quantity calculation. Rebuild is only strictly needed
on the **final** quantity but doesn't hurt on interim.

### Over-production prompt

If total completed would exceed Quantity to Make:

> "Total quantity completed exceeds the 'Qty to Make' for the work
> order. Do you wish to make the 'Qty to Make' to be equal to the
> quantity completed?"

- **N** = keep the original target (useful if you track over-run %).
- **Y** = make the target match reality (useful if the original was
  rough anyway).

### Scrap during receipt

- Enter **Scrap Quantity / Code / Desc**.
- Per default settings, scrap cost is either amortized across good
  parts, posted separately, or prompted.
- Balance of parts still to be completed may be reduced by scrap,
  again per default.
- Scrapped parts can be routed to **NCR** for disposition in
  [QC-F-C](../../../samples/chm/extracted/qc-f-c_disposition_ncr.htm).

### The "is this the final quantity?" prompt

> "If YES, the program will calculate a unit cost that balances
> total work order actual costs with all previously reported
> finished production."

- **Y** → residual WIP is zeroed by fitting the unit cost. Safe even
  for non-final receipts *if* you know all cost already reported
  applies to the quantity being received.
- **N** → choose std cost or calc-from-actual.
  - **Standard cost** — often used for interim receipts where per-
    unit actual is unknowable.
  - **Calc-from-actual** — uses reported actual where available,
    falls back to estimated where not. Manually overridable.
- If neither is used and residual remains at close, it posts to
  **WIP Variance** at [AD-A](../../../samples/chm/extracted/ad-a_general_ledger_defaults.htm).
  List via [JC-Q](../../../samples/chm/extracted/jc-q_print_work_order_receipts.htm).

### Lot / Serial at receipt

- Lot-controlled item → must enter a lot number (add on the fly OK).
- Serial-controlled item → one per unit. Auto-generate per
  [SC-G](../../../samples/chm/extracted/sc-g_enter_serial_generation_parameters.htm).
  Skips collisions automatically.

### Backflushing — driven by SD-B default

| SD-B setting | Behavior |
|---|---|
| `Y` | Prompt to backflush. |
| `A` | Always backflush, no prompt. |
| `B` | Always backflush for total qty completed. Prompt only on negative (reverse-backflush) entries. |

Components flagged in [BM-A](../../../samples/chm/extracted/bm-a_ener_bills_of_material.htm)
as **"excluded from scrap backflush"** are backflushed only for good
parts. Backflushing handles record locks the same way as WO-G
(writes to temp file, post later via [WO-O](#wo-o-post-material-transactions)).

### Multi-yield work orders

For a type-N parent defined in [IN-B](../../../samples/chm/extracted/in-b_enter_inventory.htm)
as a **"Multi-yield placeholder"** (e.g. cutting one sheet of metal
into multiple parts):
1. Program detects placeholder and switches to multi-yield mode.
2. Choose allocation method: **Weight, Foot Factor, or Each** (W/F/E).
3. Choose standard vs actual cost.
4. Enter the list of parts + qtys.
5. Adjust labor percentages (material % doesn't always match labor %).
6. Process → separate receipt per item at proportional cost.
   - Delta vs standard posts to variance.

### Auto-close

If `Close Work Order at Enter Finished Production? = Y` in [SD-B](../../../samples/chm/extracted/sd-b_work_order_defaults.htm)
and total completed ≥ WO quantity, user is prompted to close.
Generally only do this if all costs are fully reported.

### Editing / deleting previous entries

F2 on Date Received → list sorted by WO + date. Highlight →
prompted to back out. Gotcha: **reversal only reverses the Finished
Production transaction**, not the backflush transactions — those
have to be corrected manually in [WO-G](#wo-g--issue-materials).

### Save-time processing

- Quantity completed → WO header.
- **On-Hand** ↑, **On Work Order** ↓.
- **In-WIP** ↓ proportionally for each component.
- If GL posting is on ([AD-A](../../../samples/chm/extracted/ad-a_general_ledger_defaults.htm)):
  debit item's asset account, credit WIP account.

---

## WO-J — Close / Cancel Orders

*Source: [wo-j_close_cancel_orders.htm](../../../samples/chm/extracted/wo-j_close_cancel_orders.htm)*

**Purpose.** Bulk close (C) or cancel (X) a range of WOs.

### Safety precaution

> *"If you select a range of work orders, this program will not
> close any work orders within the range that have open, unreceived,
> or uninvoiced purchase order items assigned to it."*

To **override** the safety: enter the **same WO number in both From
and Thru**. Even then, you cannot close a WO with **unreceived POs
or unposted labor**. You *can* force-close a WO with uninvoiced
receipts — any later PO price changes from [AP-C](../../../samples/chm/extracted/ap-c_enter_purchase_order_invoices.htm)
will post to **WIP Variance** ([AD-A](../../../samples/chm/extracted/ad-a_general_ledger_defaults.htm)).
Detail still posts to WO transaction files for reporting.

### Operation

- WO range (entire prefix works — it picks up every suffix).
- Or Job Number range.
- **Effective close date** — becomes the Actual Finish Date AND the
  GL posting date of any WIP Variance. Default = today for ranges;
  last-receipt-date for singletons.
- Close (**C**) or Cancel (**X**). Cannot cancel if any finished
  production has been reported.
- Prompt: rebuild summarized actual costs first? (Recommended for
  last-chance accuracy.)
- Output report lists WOs closed/canceled + WIP Variance postings.

### Closing — what happens

- On Work Order reversed for remaining uncompleted quantity.
- Remaining Allocated reversed for each component.
- Excess In-WIP reversed.
- Residual cost (actual issued − finished production removed) →
  WIP Variance, **unless** `SD-B process WIP Variance in WO-J = Y`,
  in which case the inventory value of on-hand stock of the parent
  is adjusted first and only the remainder posts to WIP Variance.

### Canceling — what happens

- On Work Order reversed by the full Quantity to Make.
- Any issued components **returned to inventory** (In-WIP ↓, On-Hand ↑).
- GL: WIP credited, component asset accounts debited.
- Any residual labor / outside-processing cost → WIP Variance.

### Reopening

Go to [WO-A](#wo-a--enter-work-orders), change status from C/X to F/R,
save. Everything reverses back — On Work Order, backlog, allocations.

---

## WO-K-A Enter Work Order Routings

*Source: [wo-k-a_enter_work_order_routings.htm](../../../samples/chm/extracted/wo-k-a_enter_work_order_routings.htm)*

Edit the WO-specific routing without touching the item's master
routing. Auto-copied from [RO-A](../../../samples/chm/extracted/ro-a_enter_routings.htm)
when the WO is created F/R (or on S→F). If no master routing
exists, enter from scratch. All sequences print on the traveler
unless suppressed via [RO-L](../../../samples/chm/extracted/ro-l_enter_sequence_print_control.htm).

Field definitions and operation are **identical** to RO-A — refer
there. If Lead Time scheduling is enabled, any change to production
run time prompts a reminder to run [SH-P](../../../samples/chm/extracted/sh-p_lead_time_scheduling.htm).

---

## WO-K-B Enter Work Order Bills of Material

*Source: [wo-k-b_enter_work_order_bills_of_material.htm](../../../samples/chm/extracted/wo-k-b_enter_work_order_bills_of_material.htm)*

Edit the WO-specific BOM without touching the item's master BOM.
Auto-copied on create F/R / on S→F. Phantoms (type B) are expanded
— the phantom parent itself is **not** a component in the WO BOM,
its first-level children are.

### Fields

**Lin** (sort key, dupes ok → sort by item within dupe group),
**Item number**, **T** (inventory type: R/A/F/N/M/T/L/B),
**Description**, **Quantity Per**, **UM**, **Seq** (tie to WO
routing sequence for backflush-by-seq), **Scrap Per**,
**Qty Req** = `(Quantity Per + Scrap Per) × WO Qty to Make`,
**Ref** (user field, e.g. bubble #), **Ph** (phantom flag),
**Assembly + Description** (if Ph = Y).

### Operation

- Modify: F2 for lookup, arrow through, edit Qty Per / UM / Seq /
  Scrap Per / Qty Req / Ref.
- Add: `End` or New Line → Lin → Item → Qty Per (or Qty Req; they
  auto-link) → Seq (optional) → Scrap Per → Ref → Ph/Assembly.
- Delete: **Delete button**. Not allowed if already issued; program
  will instead reduce Qty Req to match issued quantity (allocation → 0).
- **Free-form comments** tied to components (print on traveler) via
  `Home` / Comments. Distinct from standard BOM remarks.

---

## WO-K-C Create Multi-Date Work Orders

*Source: [wo-k-c_create_multi-date_work_orders.htm](../../../samples/chm/extracted/wo-k-c_create_multi-date_work_orders.htm)*

Splits a parent WO that has multiple date/qty triples into separate
suffixed WOs (-002, -003, …). Create the parent in [WO-A](#wo-a--enter-work-orders)
with Multiple Dates = Y first, then run WO-K-C. Resulting WOs all
share the parent's prefix.

---

## WO-K-D Create Multi-Assy Work Orders

*Source: [wo-k-d_create_multi-assy_work_orders.htm](../../../samples/chm/extracted/wo-k-d_create_multi-assy_work_orders.htm)*

Auto-generates WOs for all/selected subassemblies in a BOM.
Single-level or multi-level through the whole structure.

### Behaviors

- **WO range format controls depth:** specify prefix+suffix → single-
  level only; specify prefix only (or suffix 1-999) → all levels.
- **Offset lead times** — Y schedules subassembly WOs to finish
  before parent start. If Lead Time scheduling flag is F/B, always
  uses **backward** scheduling here per [How Lead Time Scheduling Works](../../../samples/chm/extracted/how_lead_time_scheduling_works.htm).
- **Reorder level filter** — Y only creates WOs for subassemblies
  below reorder level.
- **Prompt for qty** option lets you verify stock status level-by-level.
- **Balance required** — Y → subassembly WO qty = `available − reorder level − MOQ` (if those parameters are enabled); N → full parent qty.
- **Accidental re-run protection**: checks for existing lower-level
  WOs and warns.

---

## WO-K-E Swap Substitute Parts

*Source: [wo-k-e_swap_substitute_parts.htm](../../../samples/chm/extracted/wo-k-e_swap_substitute_parts.htm)*

Replace a BOM component with an approved substitute (from [BM-J](../../../samples/chm/extracted/bm-j_enter_approved_substitutes.htm)).
Optionally partial — specify qty to replace; the standard stays on
the BOM with reduced qty and the sub is added. Inventory
allocations move with it.

---

## WO-K-F Edit Sequence Started / Finished Dates

*Source: [wo-k-f_edit_sequence_started_finished_dates.htm](../../../samples/chm/extracted/wo-k-f_edit_sequence_started_finished_dates.htm)*

Manually set Started Date / Finished Date on any WO sequence.
Needed when a sequence is started or completed but lacks the
corresponding date that tells scheduling programs to (de)schedule
it. WO # sticks on screen for successive sequence edits.

---

## WO-K-G Recalculate Projected Hours

*Source: [wo-k-g_recalculate_projected_hours.htm](../../../samples/chm/extracted/wo-k-g_recalculate_projected_hours.htm)*

Recalculates per-sequence labor hours remaining based on `reported
hours` and `% complete`.

**Precondition:** `Use Projected or Estimate $ and Hours? = P` in
[SD-B](../../../samples/chm/extracted/sd-b_work_order_defaults.htm).

**Example (from the vendor):** sequence estimated 10h. 8h reported
at 50% complete → projected total = 16h, remaining = 8h.

Completed sequences and untouched sequences aren't changed.
Compare estimate vs projection via [WO-L-H](#wo-l-h-print-projected-vs-estimated-hours).

---

## WO-K-H Recalculate Work Order Costs

*Source: [wo-k-h_recalculate_work_order_costs.htm](../../../samples/chm/extracted/wo-k-h_recalculate_work_order_costs.htm)*

Rolls up total WO costs from transaction detail for a range of WOs.
Filters: WO, Job #, parent item #, status.

---

## WO-K-I Kitting System

*Source: [wo-k-i_kitting_system.htm](../../../samples/chm/extracted/wo-k-i_kitting_system.htm)*

**Purpose.** Pre-issue components to a **temporary holding file** as
the puller walks the stockroom (designed for tablet use). Final
posting via [DE-K-A Edit/Post Material Issues](../../../samples/chm/extracted/de-k-a_import_post_material_issues.htm).

### Operation

- Enter WO # + employee ID.
- Work through highlighted components; suggested qty =
  `min(required, on-hand)`.
- **Select → Enter** accepts suggested qty (or type a different one).
- On-hand discrepancy? Flag for physical count — sets **Cycle Code =
  KIT** as a signal to inventory control.
- Save → transactions go to temp file.
- **On-hand isn't reduced and allocations aren't cleared until final
  posting** via DE-K-A.

---

## WO-K-J Synchronize Work Order to Master BOM & Routing

*Source: [wo-k-j_synchronize_work_order_to_master_bom_and_routing.htm](../../../samples/chm/extracted/wo-k-j_synchronize_work_order_to_master_bom_and_routing.htm)*

Pushes master-level BOM/routing changes down to existing WOs. WOs
that already have materials or labor posted are **skipped**.
Operation: WO range + item range + report mode (all vs exceptions
only). For each eligible WO: delete BOM/routing, reapply master,
recalculate estimated costs.

---

## WO-K-K Edit Posted DC Labor

*Source: [wo-k-k_edit_posted_dc_labor.htm](../../../samples/chm/extracted/wo-k-k_edit_posted_dc_labor.htm)*

Reverse + correct labor posted through **Data Collection**.

### Gotcha — lot/serial backflush

Reversal also reverses any sequence-associated backflush
transactions, and re-posting backflushes again. **If the backflushed
components are Lot or Serial controlled and there are multiple
entries the same day**, the program can't tell which transactions
apply to the original — you'll be told to correct material issues
**manually in [WO-G](#wo-g--issue-materials)**.

---

## WO-K-L Quick Work Order

*Source: [wo-k-l_quick_work_order.htm](../../../samples/chm/extracted/wo-k-l_quick_work_order.htm)*

Bulk-create WOs from a list (typed or imported) of item + qty.

### Ending-status semantics

| Status | What the program does |
|---|---|
| **S** | WO header only — no BOM, no routing. |
| **F** | Header + BOM + routing, components allocated. |
| **R** | F + Actual Start Date populated. |
| **C** | R + components issued + finished production entered + closed. |

### Numbering

- **Suffix increment** → `12345-1, 12345-2, 12345-3, …`
- **Prefix increment** → `12345-1, 12346-1, 12347-1, …`

---

## WO-K-M Parts Requester

*Source: [wo-k-m_parts_requester.htm](../../../samples/chm/extracted/wo-k-m_parts_requester.htm)*

**Purpose.** Shop-floor request for replacement parts from the
stockroom. Pairs with [WO-K-N](#wo-k-n-stockroom-program).

Inputs: WO #, sequence, employee #, location (defaults to WO
location). Per requested item: qty, reference, **reason (Scrap Code
from [RO-G](../../../samples/chm/extracted/ro-g_enter_scrap_codes.htm))**,
optional notes. Request transmitted to the stockroom per location.

---

## WO-K-N Stockroom Program

*Source: [wo-k-n_stockroom_program.htm](../../../samples/chm/extracted/wo-k-n_stockroom_program.htm)*

**Purpose.** Stockroom side of [WO-K-M](#wo-k-m-parts-requester).

**Operation:**
- Runs continuously; refresh timer + optional audio cue.
- Pick a Location to monitor.
- When a request arrives: **Print Label → pull stock → tag the line
  → enter issue qty + lot/serial → save**.
- **Substitute button** swaps in a substitute if the requested item
  is unavailable.

---

## WO-K-O Enter Component Serial Numbers

*Source: [wo-k-o_enter_component_serial_.htm](../../../samples/chm/extracted/wo-k-o_enter_component_serial_.htm)*

Map component serial numbers → parent serial number they're installed
into. **Prerequisite:** run [WO-S](#wo-s-print-work-order-labels) first
to assign parent serial numbers. The mapping file gets pre-populated
with one row per (WO, parent item, parent serial, component item).
Enter per component serial → Post.

Enforcement: [WO-I](#wo-i--enter-finished-production) blocks completion
of a serialized parent until all required component serial numbers
are assigned.

---

## WO-K-P Enter Component Lot Information

*Source: [wo-k-p_enter_component_lot_inf.htm](../../../samples/chm/extracted/wo-k-p_enter_component_lot_inf.htm)*

Same pattern as [WO-K-O](#wo-k-o-enter-component-serial-numbers) but
for **Lot-controlled** components. Same prerequisite ([WO-S](#wo-s-print-work-order-labels)),
same enforcement on [WO-I](#wo-i--enter-finished-production).

---

## WO-K-Q Convert WO to PO

*Source: [wo-k-q_convert_wo_to_po.htm](../../../samples/chm/extracted/wo-k-q_convert_wo_to_po.htm)*

Generate POs for components needed on a WO range.

Inputs: WO range, Job # (optional), Warehouse Location, PO Date,
Est. Receipt Date, **Auto Generate vs Review**, policy flags
("issue on-hand first?", "reassign existing stock-POs to these
WOs?", "tie lines to work orders?").

**Precondition:** each item needs a **primary Vendor** to auto-
generate POs.

---

## WO-K-R Issue Scrap Component

*Source: [wo-k-r_issue_scrap_component.htm](../../../samples/chm/extracted/wo-k-r_issue_scrap_component.htm)*

Mark a component as scrapped (reopens allocation as replacement
demand). **Use this only if you have no on-hand replacement.** If
you do have replacement stock, use the **Scrap Quantity** option in
[WO-G](#wo-g--issue-materials) or [WO-K-M](#wo-k-m-parts-requester).

---

## WO-K-S Assign WO to Bin

*Source: [wo-k-s_assign_wo_to_bin.htm](../../../samples/chm/extracted/wo-k-s_assign_wo_to_bin.htm)*

Park a quantity of a WO's items in a **Bin** (on hold); remove to
put back in production. With **Warehouse Control + controlled bins**
enabled, bins are restricted to the master bin list. Add / Edit /
Remove operations.

---

## WO-L-A Print Work Order Status

*Source: [wo-l-a_print_work_order_status.htm](../../../samples/chm/extracted/wo-l-a_print_work_order_status.htm)*

**Purpose.** Completion status by WO, optionally with per-sequence
detail. Big selection ribbon: item #, date ranges, status, priority,
class, customer, PO, job.

**Key options:**
- **Print current status?** — Y limits to sequences with non-zero
  start qty AND qty complete < start qty.
- **Print an aggregate report format?** — aggregate by Part Number
  or Work Order Prefix. Combines header info across multiple WOs
  as if they were one. Ideal for multi-date WOs on the same item.
- **MAT column** (far right): Y=all issued, N=none, P=partial.
- Caveat: aggregating by prefix when suffixes are **different
  subassemblies** makes the routing aggregation meaningless.

---

## WO-L-B Print Work Order Schedule

*Source: [wo-l-b_print_work_order_schedule.htm](../../../samples/chm/extracted/wo-l-b_print_work_order_schedule.htm)*

Master production schedule, user-sortable. Filter by: start/finish
date ranges, WO range, status, priority, class, Job #, item,
customer.

---

## WO-L-C Print Work Center Backlog

*Source: [wo-l-c_print_work_center_backlog.htm](../../../samples/chm/extracted/wo-l-c_print_work_center_backlog.htm)*

Prioritized schedule per work center — usually run **daily**.
Different format for outside-processing WCs (shows whether a PO has
been issued).

**Key behavior:** all sequences after the first start at **start qty
= 0**; they only pick up qty when a preceding sequence completes. So
"sequences with zero start qty" = work the parts haven't arrived for
yet. Use `Include Sequences with no Start Qty? = N` to see only
sequences ready to work on. Sort: priority code, then finish date.

---

## WO-L-D Print Projected Shipments

*Source: [wo-l-d_print_projected_shipments.htm](../../../samples/chm/extracted/wo-l-d_print_projected_shipments.htm)*

Dollar projection of expected shipments based on current WOs.
`Sales price × Qty to Make`, scheduled finish date = projected ship
date. Subtotals by customer or by month (re-run with different date
ranges if you need finer than monthly).

---

## WO-L-E Print / Post Labor to Payroll

*Source: [wo-l-e_print_post_labor_to_payroll.htm](../../../samples/chm/extracted/wo-l-e_print_post_labor_to_payroll.htm)*

**Dual-purpose**: print hours report AND (optionally) push hours
into [PR-B Enter Pay Info](../../../samples/chm/extracted/pr-b_enter_pay_info.htm).

**Recommended flow:** run with `Post? = N` first → review → correct
errors → run with `Post? = Y`. Program tracks posted status; prompt
controls whether already-posted items appear.

**Report summary buckets:** regular, overtime, double, vacation,
holiday, sick, total.

---

## WO-L-F Print Work Order Shortages

*Source: [wo-l-f_print_work_order_shortages.htm](../../../samples/chm/extracted/wo-l-f_print_work_order_shortages.htm)*

Same report that prints at [WO-B](#wo-b--release-work-orders) release,
available on-demand.

**Semantics:**
- **Required** = this WO's need.
- **Allocated** = total need across all open WOs.
- **On Order** = POs / WOs not yet received / completed.
- *"You may technically have enough stock on hand for a component to
  satisfy this work order, but you could be taking the component from
  another work order that needs it."*

Leaving WO # and Parent blank + entering a component item → report
serves as **component-centric status** across all open WOs.

---

## WO-L-G Print Work Center by Key Component

*Source: [wo-l-g_print_work_center_by_key_component.htm](../../../samples/chm/extracted/wo-l-g_print_work_center_by_key_component.htm)*

Group open WOs sharing a **key component** for efficient batched
runs — e.g. "all WOs needing white paint at the paint center", or
"all WOs needing this alloy at the foundry".

**Critical operation note:** the "key component" filter is what makes
the report meaningful. If you don't specify components, all BOM
components are selected and the report **loses all meaning**.

**Performance warning:** *"This report has to do a lot of sorting
and could take awhile before printing."* — vendor.

---

## WO-L-H Print Projected vs Estimated Hours

*Source: [wo-l-h_print_projected_vs_estimated_hours.htm](../../../samples/chm/extracted/wo-l-h_print_projected_vs_estimated_hours.htm)*

Compare current projection vs original estimate. Same precondition
as [WO-K-G](#wo-k-g-recalculate-projected-hours) (`SD-B Use Projected?
= P`), and can optionally recalc before printing instead of running
WO-K-G separately.

**Calculation:**
- **Estimated remaining** = `(time/part × parts) − actual reported`.
  Clipped at 0 (no negatives).
- **Projected remaining** = recalculated estimated − actual reported.

---

## WO-L-I Print Allocations

*Source: [wo-l-i_print_allocations.htm](../../../samples/chm/extracted/wo-l-i_print_allocations.htm)*

Open-allocation listing. Sorts: **Component item, Class, or Primary
Vendor**. Filters: item #, type, class, category, primary vendor,
cycle code, planner code, active status. Options: second desc line,
vendor + last cost, order detail, rebuild stock status first.

---

## WO-L-J Print Work Order Completions

*Source: [wo-l-j_print_work_order_comple.htm](../../../samples/chm/extracted/wo-l-j_print_work_order_comple.htm)*

WO list with actual close date (if closed), due date, and
**estimated vs actual hours**. Filters: WO, completion date, item,
class, category (include/exclude), work-center filter (if routing
details are included).

---

## WO-L-K Print WO Bills of Material

*Source: [wo-l-k_print_wo_bills_of_mater.htm](../../../samples/chm/extracted/wo-l-k_print_wo_bills_of_mater.htm)*

Print WO BOMs in a format similar to [BM-B Print Bills of Material](../../../samples/chm/extracted/bm-b_print_bills_of_materials.htm).
Filter by parent item range + WO range.

---

## WO-L-L Print WO Component Labels

*Source: [wo-l-l_print_wo_component_labe.htm](../../../samples/chm/extracted/wo-l-l_print_wo_component_labe.htm)*

Labels for BOM components on a WO. Filter by associated sequence
and/or component number range. Label quantity either per-BOM qty
(for large parts needing individual labels) or a fixed qty per item.

---

## WO-L-M Print Material Summary

*Source: [wo-l-m_print_material_summary.htm](../../../samples/chm/extracted/wo-l-m_print_material_summary.htm)*

**Despite living in the WO menu, this report drives off Sales
Orders.** Summarizes total material needed to fulfill one or a range
(or non-sequential list) of SOs. Checkbox `Use WOs to determine
Required Material` switches the requirement source from master BOM
to WO BOMs. Columns: component, total required, total on-hand.

---

## WO-L-N WO BOM for Purchasing

*Source: [wo-l-n_wo_bom_for_purchasing.htm](../../../samples/chm/extracted/wo-l-n_wo_bom_for_purchasing.htm)*

Per-WO report of required qty, on-hand qty, existing POs, and other
WOs allocating the same item — for purchasing decisions.

---

## WO-M Batch Labor Entry

*Source: [wo-m_batch_labor_entry.htm](../../../samples/chm/extracted/wo-m_batch_labor_entry.htm)*

**Purpose.** Fast batch-mode labor entry from time cards. Unlike
[WO-F](#wo-f--enter-labor), this writes to a **temporary file** —
`BKDCPLAB` — until posted by [WO-N](#wo-n-post-labor-batches).
Entries can be freely edited or deleted pre-post.

### Operation

- Start / Finish time → program computes Run/Setup hours.
- Break adjustments per shift (defined in [SD-F Data Collection Defaults](../../../samples/chm/extracted/sd-f_data_collection_defaults.htm))
  are applied based on employee shift assignment in
  [SM-G Enter Employees](../../../samples/chm/extracted/sm-g_enter_employees.htm).
- Or enter decimal Run/Setup hours directly.
- Date + employee stick between saves.
- Edit list → Edit button. Delete list → Delete button.

---

## WO-N Post Labor Batches

*Source: [wo-n_post_labor_batches.htm](../../../samples/chm/extracted/wo-n_post_labor_batches.htm)*

**Purpose.** Batch-post [WO-M](#wo-m-batch-labor-entry) transactions
to the permanent WO files. Once posted, edits require
[WO-K-K](#wo-k-k-edit-posted-dc-labor).

### Backflush-by-sequence support

If any BOM components are tied to routing sequences (Seq field in
the WO BOM), this program issues those materials when that sequence
gets posted.

**Exception:** lot- or serial-controlled components are **not**
backflushed — they show up on a **discrepancy report** that tells
you to manually issue via [WO-G](#wo-g--issue-materials).

Filters: employee, WO, item, date (Enter through all = post everything).

---

## WO-O Post Material Transactions

*Source: [wo-o_post_material_transactions.htm](../../../samples/chm/extracted/wo-o_post_material_transactions.htm)*

**Purpose.** Post the temp-file transactions written by
[WO-G](#wo-g--issue-materials) / [WO-I](#wo-i--enter-finished-production)
when they hit component record locks.

**Important:** until WO-O is run:
- Job Cost reports are incomplete.
- The WO **cannot close**.

Vendor recommends running it **daily at end of day**. Lot- and
serial-required components prompt for info at post time.

---

## WO-P Batch Finished Production

*Source: [wo-p_batch_finished_production.htm](../../../samples/chm/extracted/wo-p_batch_finished_production.htm)*

Run [WO-I](#wo-i--enter-finished-production) for a batch of WOs.
Honors [SD-B](../../../samples/chm/extracted/sd-b_work_order_defaults.htm)
defaults for backflushing, `Use Standard Cost`, and auto-close.

### Multi-level assembly handling

If the range covers a multi-level structure built via
[WO-K-D](#wo-k-d-create-multi-assy-work-orders), the program
**starts from the highest dash number and works backward** so
components are generated and backflushed in the correct order.

### Qty inputs

- **Range mode** with multi-level parent — program prompts for parent
  qty and proportions components.
- **Range mode** without a single top-level parent — assumes all WOs
  in the range are fully complete (no qty prompt).
- **List mode** — specify qty per WO.

If `Close WO at Finished Production = Y` in SD-B, each WO can be
overridden to force-close-short or force-remain-open.

---

## WO-Q Work Order Inquiry

*Source: [wo-q_work_order_inquiry.htm](../../../samples/chm/extracted/wo-q_work_order_inquiry.htm)*

Identical to [WO-A](#wo-a--enter-work-orders) **but read-only and
non-locking**. Use for inquiry (or [DC-I](../../../samples/chm/extracted/dc-i_work_order_inquiry.htm))
— see WO-A's "Inquiry buttons" note.

---

## WO-R Work Order Defaults

*Source: [wo-r_work_order_defaults.htm](../../../samples/chm/extracted/wo-r_work_order_defaults.htm)*

Redirect only — points to [SD-B Work Order Defaults](../../../samples/chm/extracted/sd-b_work_order_defaults.htm).

---

## WO-S Print Work Order Labels

*Source: [wo-s_print_work_order_labels.htm](../../../samples/chm/extracted/wo-s_print_work_order_labels.htm)*

Labels for the items being manufactured on a WO. Can print **before
or after** production.

### Serial-number generation

If the item is serialized, this program can **generate** the needed
serial numbers per [SC-G Enter Serial Generation Parameters](../../../samples/chm/extracted/sc-g_enter_serial_generation_parameters.htm)
(if the parts aren't completed yet), or **print labels for the
already-assigned** serial numbers (if they are).

**Prerequisite** for [WO-K-O](#wo-k-o-enter-component-serial-numbers)
and [WO-K-P](#wo-k-p-enter-component-lot-information) mappings.

---

## WO-T Enter Rework Work Order

*Source: [wo-t_enter_rework_work_order.htm](../../../samples/chm/extracted/wo-t_enter_rework_work_order.htm)*

Create a WO to **rework** an item and return it to stock. Optionally
auto-issues the item to its own WO. **No standard BOM is pulled in
(it's a rework)** but there is a routing so operations are available
to charge labor against.

---

## Cross-references

### Related modules (LearnEVO docs)
- [AR — Accounts Receivable](../ar-accounts-receivable/README.md) — customer side
- [AP — Accounts Payable](../ap-accounts-payable/README.md) — PO-invoice side
- [IN — Inventory](../in-inventory/README.md) — item / location master
- [SO — Sales Orders](../so-sales-orders/README.md) — SO → WO conversion
- [PO — Purchase Orders](../po-purchase-orders/README.md) — PO tied to WO
- [BM — Bills of Material](../bm-bill-of-materials/README.md) — master BOM source
- [MR — MRP](../mr-mrp/README.md) — planned-WO generation
- [GL — General Ledger](../gl-general-ledger/README.md) — WIP / variance accounts
- [PR — Payroll](../pr-payroll/README.md) — [WO-L-E](#wo-l-e-print--post-labor-to-payroll) target
- [JC — Job Costing](../jc-job-costing/README.md) — reads all WO data

### Related tables (file-names-index)
All Work Order tables documented at
[04-data-dictionary/file-names-index.md · Work Orders](../../04-data-dictionary/file-names-index.md#work-orders).

### Related CHM content
- [System Overview § Sequence of Events — Work Orders flow](../../00-overview/system-overview.md#7c-work-orders)
- [System Overview § Archiving — SM-J-B](../../00-overview/system-overview.md#10-archiving-or-purging-old-data)
