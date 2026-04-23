# Job Costing — Vendor Help Content

Status: verified (summarized from the vendor's help file).

Source CHM: `\\i2s109-solidcrm\DBAMFG$\EVOHELP.CHM` →
[samples/chm/EvoHELP.CHM](../../../samples/chm/EvoHELP.CHM) →
decompiled to [samples/chm/extracted/](../../../samples/chm/extracted/).
Extracted via [scripts/chm_to_md.py](../../../scripts/chm_to_md.py).

This doc consolidates the **20 help topics** under the CHM's
*Manufacturing → Job Costing* category. Each program gets its purpose,
what's being compared, filters, and cross-links. Full verbatim source
is one click away via the `Source:` link on each section.

For the companion schema + menu + form view of this module, see
[README.md](README.md) in this folder.

---

## Contents

- [Overview — what Job Costing is](#overview--what-job-costing-is)
- [Design pattern — the common selection ribbon](#design-pattern--the-common-selection-ribbon)

**Cost analysis**
- [JC-A Print Job Cost Report](#jc-a-print-job-cost-report)
- [JC-B Print Profit Projection](#jc-b-print-profit-projection)
- [JC-L Print Job Cost Summary](#jc-l-print-job-cost-summary)
- [JC-R Print Multi-Level Job Cost](#jc-r-print-multi-level-job-cost)
- [JC-S Work Order Detail Report](#jc-s-work-order-detail-report)

**Transaction listings**
- [JC-C Print Labor Transactions](#jc-c-print-labor-transactions)
- [JC-D Print Overhead Transactions](#jc-d-print-overhead-transactions)
- [JC-E Print Material Issues](#jc-e-print-material-issues)
- [JC-F Print Outside Purchases](#jc-f-print-outside-purchases)
- [JC-Q Print Work Order Receipts](#jc-q-print-work-order-receipts)

**Efficiency & standards**
- [JC-G Print Labor Efficiency](#jc-g-print-labor-efficiency)
- [JC-H Print Work Order History](#jc-h-print-work-order-history)
- [JC-O Print Standard Labor Hours](#jc-o-print-standard-labor-hours)

**Production output**
- [JC-I Print Production by Work Center](#jc-i-print-production-by-work-center)
- [JC-J Print Production by Machine](#jc-j-print-production-by-machine)
- [JC-K Print Production by Tool](#jc-k-print-production-by-tool)

**Work-in-process**
- [JC-M Print WIP Summary](#jc-m-print-wip-summary)
- [JC-N Print WIP Percent Completion](#jc-n-print-wip-percent-completion)
- [JC-P Print Materials in WIP](#jc-p-print-materials-in-wip)

---

## Overview — what Job Costing is

*Source: [job_costing.htm](../../../samples/chm/extracted/job_costing.htm)*

Job Costing is a **reporting-only module** — not a transactional one.
It reads the data already created by the Work Orders and Purchasing
modules and produces analytical reports across four themes:
- **Job cost and profit** per work order.
- **Labor, overhead, material, and outside-purchase** transaction lists.
- **Efficiency, standards, and work-order history**.
- **Work-in-process** summaries and percent-completion.

The module's value is in **contrast** — actual vs estimate, actual vs
standard, one period vs a prior period. Every report here is driven
by data the user produced elsewhere in EvoERP, so the reports are
only as good as the discipline in [WO-F / WO-M / DC](../../../samples/chm/extracted/data_collection.htm),
[WO-G](../../../samples/chm/extracted/wo-g_issue_materials.htm),
[WO-I](../../../samples/chm/extracted/wo-i_enter_finished_production.htm),
and [PO-C](../../../samples/chm/extracted/po-c_receive_purchase_orders.htm).

### The three WIP totals to balance

Most month-end GL reconciliation flows through:
1. **[JC-M Print WIP Summary](#jc-m-print-wip-summary)** — the canonical
   control total against the GL WIP account.
2. **[JC-N Print WIP Percent Completion](#jc-n-print-wip-percent-completion)**
   — period-over-period progress (used for progress billings).
3. **[JC-P Print Materials in WIP](#jc-p-print-materials-in-wip)** —
   floor-status detail, **not** for GL reconciliation (use JC-M).

### Filtering by Active vs Archived

Most JC reports offer an Active / Archived toggle. Archive is driven
by [SM-J-B Archive Work Orders](../../../samples/chm/extracted/sm-j-b_archive_work_orders.htm)
— see [System Overview § Archiving](../../00-overview/system-overview.md#10-archiving-or-purging-old-data).

---

## Design pattern — the common selection ribbon

Seven of the 20 JC programs (JC-C, JC-D, JC-G, JC-I, JC-J, JC-K, JC-O)
share an **identical selection screen**. Rather than repeat it in each
section below, here's the template:

1. **Sort / subtotal field** — Labor Date, Work Order, Employee,
   Work Center, Parent Part, Machine, Tool, or Sequence.
   - Sort by **Labor Date** → subsorts by employee within each date.
   - All other sorts → subsort by date within the sort field.
2. **Output mode** — Detail only / Detail + subtotals / Subtotals only.
3. **Work Order Status** filter.
4. **Active vs Archived** work orders.
5. **Labor Type** + **Shift** filters.
6. **Free-form filters** — Labor Date, WO, WC, Parent Part, Tool,
   Employee, Job #, Sequence, Scrap Code, Rework Code, QC Code,
   Machine, Department.

> **Performance tip from the vendor:** the labor-transaction table
> gets very large; **always bracket the date range** even when date
> isn't your primary filter, or the report crawls.

Sections below only note deviations from this pattern.

---

## JC-A Print Job Cost Report

*Source: [jc-a_print_job_cost_report.htm](../../../samples/chm/extracted/jc-a_print_job_cost_report.htm)*

**Purpose.** Full cost + profit analysis per work order. Summary-only
or detail-and-summary. Estimated vs actual, totals and per-part, with
variance % and (if the WO has a price) profit comparison.

**Detail section costs** come from:
- **Labor** — per-sequence total ÷ qty completed from [WO-F](../../../samples/chm/extracted/wo-f_enter_labor.htm).
- **Outside processing** — per-sequence total ÷ qty received from [PO-C](../../../samples/chm/extracted/po-c_receive_purchase_orders.htm).
- **Materials** — per-component total ÷ qty issued from [WO-G](../../../samples/chm/extracted/wo-g_issue_materials.htm) + PO-C.

**Summary section per-part** = total actual ÷ parts completed from
[WO-I](../../../samples/chm/extracted/wo-i_enter_finished_production.htm).
**Only meaningful after the WO is fully finished** — during the WO, the
actual-cost-accumulated doesn't line up with parts-completed-so-far.

**Estimate source mismatch gotcha.** If the user enters summary totals
manually in [WO-A](../../../samples/chm/extracted/wo-a_enter_work_orders.htm),
the summary estimate **won't agree** with the detail-section rollup
because the latter recomputes from WO BOM + routing.

**Key filters / options:**
- WO range, status, customer, job #, active/archived.
- **Composite Report** (Y) — merges multiple WOs' costs. Header =
  first WO; no detail section; price for profit = first WO's price.
  Only meaningful when all selected WOs are for the same item.
- Summary-only vs full.
- Toggle component descriptions (extra line per component).

---

## JC-B Print Profit Projection

*Source: [jc-b_print_profit_projection.htm](../../../samples/chm/extracted/jc-b_print_profit_projection.htm)*

**Purpose.** Projected total cost + profit **mid-WO** (complement to
[JC-A](#jc-a-print-job-cost-report), which is best after completion).

**Projection formula.** For each operation and BOM component:
`actual to date ÷ % complete = projected total`. All projected costs
sum to projected WO total and projected profit.

Same filter set as JC-A (range, status, customer, job #).
Composite-report option behaves the same.

---

## JC-C Print Labor Transactions

*Source: [jc-c_print_labor_transactions.htm](../../../samples/chm/extracted/jc-c_print_labor_transactions.htm)*

**Purpose.** Transaction listing of labor entries from
[WO-F](../../../samples/chm/extracted/wo-f_enter_labor.htm) /
[WO-M](../../../samples/chm/extracted/wo-m_batch_labor_entry.htm) /
Data Collection. Detail or subtotal-only.

Uses the [common selection ribbon](#design-pattern--the-common-selection-ribbon).

**Works as both** an overall period report AND a narrow
transaction-hunting report — just depends on how tight the filters are.

---

## JC-D Print Overhead Transactions

*Source: [jc-d_print_overhead_transactions.htm](../../../samples/chm/extracted/jc-d_print_overhead_transactions.htm)*

**Purpose.** Same-shaped report as JC-C, but for the **overhead**
cost posted alongside each labor transaction. Use it to reconcile
job-costed overhead against actual overhead in the GL.

Uses the [common selection ribbon](#design-pattern--the-common-selection-ribbon).

---

## JC-E Print Material Issues

*Source: [jc-e_print_material_issues.htm](../../../samples/chm/extracted/jc-e_print_material_issues.htm)*

**Purpose.** Transaction listing of material issues — via
[WO-G](../../../samples/chm/extracted/wo-g_issue_materials.htm) directly,
backflushed at [WO-I](../../../samples/chm/extracted/wo-i_enter_finished_production.htm),
or backflushed-by-sequence at labor entry (WO-F / WO-M / DC).

**Filters:** active/archived, dates, WO, status, parent item,
component, job #, scrap code.

---

## JC-F Print Outside Purchases

*Source: [jc-f_print_outside_purchase.htm](../../../samples/chm/extracted/jc-f_print_outside_purchase.htm)*

**Purpose.** Transaction listing of purchase receipts relevant to
work orders — both components purchased direct-to-WO and outside
processing (service POs) assigned to routing sequences.

**Filters:** active/archived, sort (WO # or date), dates, WO, status,
vendor, PO, PO type (purchase vs service), item, sequence, job #.

---

## JC-G Print Labor Efficiency

*Source: [jc-g_print_labor_efficiency.htm](../../../samples/chm/extracted/jc-g_print_labor_efficiency.htm)*

**Purpose.** Actual labor vs **routing standards**, as a percentage.

**Convention flipped.** Below 100% = better than standard; above 100%
= worse than standard. (Confirm with the vendor's own wording in the
source if surprised — this is opposite of the usual "efficiency
above 100% = good" reading.)

Auto-subtotaled by employee. Uses the
[common selection ribbon](#design-pattern--the-common-selection-ribbon).

**Precondition that's easy to miss:** *"efficiency can only be
calculated based on the quantity of items produced so you must be
reporting quantity complete as well as labor hours for this report
to be meaningful."* — vendor.

---

## JC-H Print Work Order History

*Source: [jc-h_print_work_order_history.htm](../../../samples/chm/extracted/jc-h_print_work_order_history.htm)*

**Purpose.** Historical sequence-level comparison across WOs — e.g.
"the last several times sequence 10 was performed for item X".
Primary use: **setting / refining routing labor standards**.

**Key feature:** the report can **write back** to the Routings
master.
- First run with `Update Master Routing = N` and `Update Setup = N`
  to review results.
- If satisfied, re-run with the Update flags set to **Y** — routing
  labor and setup standards get overwritten with the averages from
  the report.
- **After a write-back, run [BM-G Print/Rollup Standard Costs](../../../samples/chm/extracted/bm-g_print_rollup_standard_costs.htm)**
  so item standard costs reflect the new times.

**Filters:** active/archived, item range, dates, sequences, detail
vs summary-only.

---

## JC-I Print Production by Work Center

*Source: [jc-i_print_production_by_work_center.htm](../../../samples/chm/extracted/jc-i_print_production_by_work_center.htm)*

**Purpose.** Parts completed + production hours **per work center**.

**Primary filters:** dates, departments, work centers, active/archived.
Uses the [common selection ribbon](#design-pattern--the-common-selection-ribbon).

---

## JC-J Print Production by Machine

*Source: [jc-j_print_production_by_machine.htm](../../../samples/chm/extracted/jc-j_print_production_by_machine.htm)*

**Purpose.** Parts completed + scrapped + setup + labor hours **per
machine**. Dates, machines, work centers, active/archived.

Uses the [common selection ribbon](#design-pattern--the-common-selection-ribbon).

---

## JC-K Print Production by Tool

*Source: [jc-k_print_production_by_tool.htm](../../../samples/chm/extracted/jc-k_print_production_by_tool.htm)*

**Purpose.** Parts completed + scrapped **per tool**. Dates, tools,
active/archived.

Uses the [common selection ribbon](#design-pattern--the-common-selection-ribbon).

---

## JC-L Print Job Cost Summary

*Source: [jc-l_print_job_cost_summary.htm](../../../samples/chm/extracted/jc-l_print_job_cost_summary.htm)*

**Purpose.** One-line-per-WO summary comparing actual-to-date vs
estimated costs.

**Filters:** active/archived, WO range, parent item, actual start
date, actual finish date, status. Vendor suggests **R (Released) +
C (Closed)** as the most useful status combination.

---

## JC-M Print WIP Summary

*Source: [jc-m_print_wip_summary.htm](../../../samples/chm/extracted/jc-m_print_wip_summary.htm)*

**Purpose.** The **canonical WIP control total** — one-line-per-WO
summary of period activity.

> "The difference between total actual costs and finished production
> gives you the net work-in-process for the period, which can be used
> as a control total to balance with your GL WIP account."

**Cost columns:** setup, labor, outside processing, material, fixed
OH, variable OH, actual total, **finished production**, **net WIP**.

**Performance note from the vendor:** *"The costs shown on this
report are calculated from scratch via the detail transaction files,
so it may take some time to process."*

Totals should tie out to the detail-transaction reports
([JC-C](#jc-c-print-labor-transactions), [JC-D](#jc-d-print-overhead-transactions),
[JC-E](#jc-e-print-material-issues), [JC-F](#jc-f-print-outside-purchases),
[JC-Q](#jc-q-print-work-order-receipts)).

**As-of-date behavior:** can be run as-of a prior date — includes all
transactions through that date for WOs that were **open at that
date**, even if currently closed/cancelled. **WO status shown = live
status at report time**, not as-of.

**Filters:** transaction date range, WO range, status, item, job #,
customer. Options: print customer names (extra line), include WOs
with no activity in the range.

This is the report called for in the
[System Overview § Month End Accounting](../../00-overview/system-overview.md#9-month-end-accounting--detail)
checklist.

---

## JC-N Print WIP Percent Completion

*Source: [jc-n_print_wip_percent_completion.htm](../../../samples/chm/extracted/jc-n_print_wip_percent_completion.htm)*

**Purpose.** Period-over-period % completion. Common use: **progress
billing** on project-type WOs.

**Three calculation modes** (picked via a single-letter flag at the
final prompt):
- **P** — material costs: materials-issued-to-date ÷ estimated materials.
- **C** — total costs: all-costs-to-date ÷ estimated total costs.
- **H** — hours: actual hours ÷ estimated hours.

**Operation:** enter the **prior-period end date** (through which
last % was calculated), then the **current-period end date**. Report
shows delta in dollars and percentage.

**Filters:** WO range, status, item, customer.

---

## JC-O Print Standard Labor Hours

*Source: [jc-o_print_standard_labor_hours.htm](../../../samples/chm/extracted/jc-o_print_standard_labor_hours.htm)*

**Purpose.** Two simultaneous comparisons:
1. **Actual hours** vs **hours at routing standard rate** — validates
   routing production-rate accuracy.
2. **Actual labor cost** vs **cost at work-center standard rate** —
   validates WC standard-labor-rate accuracy.

**Precondition for #2:** `Use Actual Costs in Labor Entry? = Y` in
[SD-B Work Orders Defaults](../../../samples/chm/extracted/sd-b_work_order_defaults.htm).
Without that, the cost comparison is noise.

Uses the [common selection ribbon](#design-pattern--the-common-selection-ribbon).

---

## JC-P Print Materials in WIP

*Source: [jc-p_print_materials_in_wip.htm](../../../samples/chm/extracted/jc-p_print_materials_in_wip.htm)*

**Purpose.** Components issued to WIP but not yet removed via
finished production. Use for **floor status tracking**.

> "This report is not recommended for reconciling your GL balance
> for work-in-process inventory. [JC-M](#jc-m-print-wip-summary)
> should be the report used for reconciliation of the WIP Balance
> to the General Ledger."

Sorted by component item #, broken out by work order.
**Filters:** WO range, component range.

---

## JC-Q Print Work Order Receipts

*Source: [jc-q_print_work_order_receipts.htm](../../../samples/chm/extracted/jc-q_print_work_order_receipts.htm)*

**Purpose.** Transaction listing for **Finished Production**, **Scrap**,
and **WIP Variance** postings.

**Filters:** active/archived, dates, WO, status, parent item, job #,
customer, close dates. **Transaction-type toggles**: include FP
receipts / scrap / WIP variance (any combination).

---

## JC-R Print Multi-Level Job Cost

*Source: [jc-r_print_multi_level_job_cost.htm](../../../samples/chm/extracted/jc-r_print_multi_level_job_cost.htm)*

**Purpose.** Job cost for a **multi-level assembly** — a group of WOs
building up to a top-level item — broken out into Labor, Material,
Overhead, Outside Processing, Extra.

**Accuracy rules that are easy to violate:**
- The **Material column only includes type R (purchased) and type M
  (make-from) items**. Type A (subassembly) and F (finished) items
  are excluded because their unit cost already includes labor +
  overhead — including them would double-count.
- **All** the WOs used to manufacture the multi-level assembly must
  be in the selected range.
- If any type-M part issued has type-A or type-F components beneath
  it, results are incorrect.

**Filters:** transaction dates, WO range, status, item, job #,
customer. Customer-names toggle. `Include WOs with no activity` flag.
Skipping the first date field = "all costs to date" (not a period).

**WO Status** = live status at report time (not as-of).

---

## JC-S Work Order Detail Report

*Source: [jc-s_work_order_detail_report.htm](../../../samples/chm/extracted/jc-s_work_order_detail_report.htm)*

**Purpose.** Detailed per-WO report with transaction-level listings
of Material, Labor, Overhead, Outside Processing, Extra — each with
its own subtotal and a grand total per WO.

**Operation:** WO filters + page-break-between-WOs toggle.

---

## Cross-references

### Data read by JC reports

| Report bucket | Source of actuals |
|---|---|
| Labor / overhead / efficiency | [WOLABOR / WOHLABOR](../../04-data-dictionary/file-names-index.md#work-orders) via [WO-F](../../../samples/chm/extracted/wo-f_enter_labor.htm) / [WO-M](../../../samples/chm/extracted/wo-m_batch_labor_entry.htm) / DC |
| Materials | [WOMAT / WOHMAT](../../04-data-dictionary/file-names-index.md#work-orders) via [WO-G](../../../samples/chm/extracted/wo-g_issue_materials.htm) / backflush at [WO-I](../../../samples/chm/extracted/wo-i_enter_finished_production.htm) |
| Outside purchases | [OUTPROC / OUTHPROC](../../04-data-dictionary/file-names-index.md#work-orders) via [PO-C](../../../samples/chm/extracted/po-c_receive_purchase_orders.htm) |
| WO receipts / scrap / variance | [WORECV / WOHRECV](../../04-data-dictionary/file-names-index.md#work-orders) via [WO-I](../../../samples/chm/extracted/wo-i_enter_finished_production.htm) + close processing |

### Related LearnEVO docs

- [WO — Work Orders module help content](../wo-work-orders/help-content.md)
  — where every JC report's underlying transactions are created.
- [System Overview § Month End Accounting](../../00-overview/system-overview.md#9-month-end-accounting--detail)
  — JC-M is part of the recommended close checklist.
- [System Overview § Sequence of Events — Work Orders flow](../../00-overview/system-overview.md#7c-work-orders).
- [file-names-index · Work Orders](../../04-data-dictionary/file-names-index.md#work-orders)
  — the actual tables these reports query.

### Related modules
- [WO — Work Orders](../wo-work-orders/README.md) — upstream producer of JC data
- [GL — General Ledger](../gl-general-ledger/README.md) — JC-M reconciliation target
- [BM — Bills of Material](../bm-bill-of-materials/README.md) — JC-H rollup dependency
- [PR — Payroll](../pr-payroll/README.md) — actual-rate source when `Use Actual Costs = Y`
- [PO — Purchase Orders](../po-purchase-orders/README.md) — source of outside-purchase data for JC-F
- [SH — Scheduling](../../../samples/chm/extracted/scheduling.htm) — uses standards that JC-H can update
