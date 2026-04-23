# Scheduling (SH) — Vendor Help Content

Status: verified (summarized from the vendor's help file).

Source CHM: `\\i2s109-solidcrm\DBAMFG$\EVOHELP.CHM` →
[samples/chm/EvoHELP.CHM](../../../samples/chm/EvoHELP.CHM) →
decompiled to [samples/chm/extracted/](../../../samples/chm/extracted/).
Extracted via [scripts/chm_to_md.py](../../../scripts/chm_to_md.py).

This doc consolidates the **22 help topics** under the CHM's
*Manufacturing → Scheduling* category (overview + 4 method
explanations + SH-A through SH-R, 17 programs — no SH-Q in the
lineup). Each program gets its purpose, key behaviors, and
cross-links.

> **Module classification fix.** [README.md](README.md) in this
> folder was originally labeled "Shipping (SH)" because the SH prefix
> was auto-classified that way. The CHM and all the menu ops
> (Edit WO dates, Finite / Infinite / Lead Time / Manual Scheduling,
> Work Center Load, Lead Time Estimator, Machine Schedule) make it
> clear this is **Scheduling, not Shipping**. The README title is
> corrected in the same commit that adds this help content; the
> folder name is kept as `sh-shipping/` so existing URLs don't break.

For the companion schema + menu + form view of this module, see
[README.md](README.md) in this folder.

---

## Contents

- [Overview — four methods, one goal](#overview--four-methods-one-goal)
- [Shared vocabulary — calendar, critical ratio, contention, buckets, parent-child](#shared-vocabulary--calendar-critical-ratio-contention-buckets-parent-child)
- [Method: Finite Scheduling](#method-finite-scheduling)
- [Method: Infinite Scheduling](#method-infinite-scheduling)
- [Method: Lead Time Scheduling](#method-lead-time-scheduling)
- [Method: Manual Scheduling](#method-manual-scheduling)

**Per-program reference**

- Editors — [SH-A](#sh-a-edit-wo-startfinishdue-dates) · [SH-B](#sh-b-manually-schedule-work-orders) · [SH-C](#sh-c-manually-schedule-work-centers) · [SH-D](#sh-d-manually-schedule-machines)
- Automatic schedulers — [SH-E](#sh-e-finite-scheduling) · [SH-F](#sh-f-infinite-scheduling) · [SH-P](#sh-p-lead-time-scheduling) · [SH-R](#sh-r-work-center-scheduler)
- Reports — [SH-G](#sh-g-print-work-order-schedule) · [SH-H](#sh-h-print-work-order-status) · [SH-I](#sh-i-print-work-center-schedule) · [SH-J](#sh-j-print-machine-schedule) · [SH-O](#sh-o-finite-schedule-bucket-report)
- Load inquiry — [SH-K](#sh-k-view-work-center-load) · [SH-L](#sh-l-view-or-calculate-work-center-load)
- Lead-time tools — [SH-M](#sh-m-lead-time-estimator) · [SH-N](#sh-n-generate-lead-times)

---

## Overview — four methods, one goal

*Source: [scheduling.htm](../../../samples/chm/extracted/scheduling.htm)*

The SH module translates work orders into factory schedules — work
center dates, machine assignments, sequence start/finish dates.

### Prerequisites

> "To use the Scheduling module you must use routings and collect
> and report labor." — vendor

### The four scheduling methods (pick one, system-wide)

| Method | Who sets WO start/finish? | Who sets sequence dates? | Work center capacity respected? | Best for |
|---|---|---|---|---|
| **Finite** ([SH-E](#sh-e-finite-scheduling)) | You set Start Date; program calculates Finish Date | Program | **Yes** — contends with other WOs | Complex products, high order volume, realistic due dates needed |
| **Infinite** ([SH-F](#sh-f-infinite-scheduling)) | You set both | Program | **No** — infinite capacity assumed | Inflexible due dates; you adapt capacity (OT, temps) to meet them |
| **Lead Time** ([SH-P](#sh-p-lead-time-scheduling)) | One of them; program calculates the other from routing time + queue | Program | Implicit via Queue Time | Establishing realistic dates at WO creation; rescheduling when queue times change |
| **Manual** | You | You (optional — otherwise WO dates roll down) | N/A | Few WOs, simple products |

> "You cannot mix scheduling methods — you must use one method
> system-wide." — vendor

The choice drives which programs in this module get used and drives
defaults in [SD-B Work Orders Defaults](../../../samples/chm/extracted/sd-b_work_order_defaults.htm)
(`Use Lead Time Scheduling?` flag: F / B / N).

### Everything that schedules WOs works alongside MRP

All four methods schedule **work orders only**. Purchase orders are
scheduled by
[MR-F Generate Material Requirements](../../../samples/chm/extracted/mr-f_generate_mrp_requirements.htm).
The normal operational loop is:
1. (Re)schedule WOs via the chosen SH method.
2. Review PO-side impacts via [MR-H Print Order Action Report](../../../samples/chm/extracted/mr-h_print_order_action_report.htm)
   for EXPEDITE / DELAY messages.
3. Adjust WO due dates based on MRP feedback.
4. Go back to step 1.

See [MR — MRP module help content](../mr-mrp/help-content.md) for the
other half of the cycle.

---

## Shared vocabulary — calendar, critical ratio, contention, buckets, parent-child

These terms show up across multiple methods and programs. Hoisted
here once.

### Scheduling Calendar + Shop Date

Built via [SM-H Enter Shop Calendar](../../../samples/chm/extracted/sm-h_enter_shop_calendar.htm)
for each company. You mark weekends, holidays, plant shutdowns as
non-workdays; calendar generation assigns each work day a
**sequential shop date**.

A **shop date** is an integer day number plus a decimal portion for
time-of-day. The decimal × 100 = zero-based hour (excluding breaks).
Example: `1101.0200` = the 1101st work day, 2 hours into that day.

Vendor guidance: generate the calendar **6 months prior to today
through ~5 years in the future**. Re-generate after any change to
weekend / holiday marks.

### Start / Finish / Due Dates on a WO

| Date | Who sets it | Meaning |
|---|---|---|
| **Start Date** | You (manually at WO creation; editable) | Earliest day the WO can start |
| **Finish Date** | Finite: program. Infinite/Lead Time/Manual: depends | Scheduled completion |
| **Due Date** | You (always manual; MRP can suggest) | When the item is actually needed |

**Due Date semantics:**
- Customer WO → SO Estimated Ship Date.
- Stock WO → manually entered or MRP-suggested from forecasts / SOs.
- Subassembly → start date of the earliest WO that needs it.

**Due Date is never changed automatically by any scheduling
program.** The rhythm of scheduling is: programs set Finish Dates;
you set Due Dates; the relationship between the two tells you if
the WO is on time.

### Critical Ratio (finite scheduling only)

```
critical ratio = (work days until due date) / (run days to complete)
```

- **Example 1:** due in 21 days, needs 5 days → ratio = 4.2.
- **Example 2:** due in 10 days, needs 5 days → ratio = 2.0 (higher
  priority — scheduled first).
- **Negative ratio** = past-due work order. Bigger negative = higher
  priority still.

Finite scheduling sorts all work orders **ascending by critical
ratio** and schedules in that order.

### Contention

The gap between the **ideal** start date for a routing sequence (the
day after the prior sequence finishes) and the **actual** start date
the finite scheduler could fit it in. Roughly: **waiting time** in
work-center queues, caused by higher-priority WOs taking the slot.

Total WO contention is printed on the finite schedule report; per-
sequence contention is visible in [SH-B](#sh-b-manually-schedule-work-orders).

### Scheduling Units

Per-sequence hours, **rounded up to the next whole hour**, adjusted
by the work center's `% Utilization` from [RO-C Enter Work Centers](../../../samples/chm/extracted/ro-c_enter_work_centers.htm).

Example: 5 run hours × 80% utilization = 6.25 hrs → **7** scheduling
units. Use `% Utilization` per work center to loosen scheduling on
unpredictable stations while keeping tight elsewhere.

### Forward / Backward Overlap

Both entered on routing sequences in [RO-A Enter Routings](../../../samples/chm/extracted/ro-a_enter_routings.htm):

- **Forward Overlap (hours)** — delay before the *next* sequence can
  start even after this one finishes. Classic use: paint drying time.
- **Backward Overlap (parts)** — once this many parts have been
  produced in the current sequence, the *next* sequence can start
  using them while the current one continues. Enables parallel
  sequences.

### Buckets

A **work-center bucket** = the available hours in one work center on
one work day. Finite scheduling fills buckets left-to-right in time
as it schedules sequences.

### Unlimited-Capacity Work Centers

Some work centers don't have meaningful capacity limits:
- **Outside processing** work centers (vendor capacity, not ours).
- In-house work centers where capacity is effectively unlimited (e.g.
  inspection).

Set `Finite Scheduling? = N` in [RO-C](../../../samples/chm/extracted/ro-c_enter_work_centers.htm)
to tell SH-E to skip bucket creation and allow unlimited contention-
free scheduling.

### Parent-Child Work Centers (finite only)

Common pattern: a work center has **several identical machines or
workstations**. Model:
- Each **machine/workstation** = its own (**child**) work center.
- The group = a **parent** work center.
- Routings reference the **parent**; the finite scheduler assigns
  each sequence to the child with the **lowest contention**.

Once production starts on a child, the assignment **locks in** — the
next finite-schedule run won't reshuffle it. Labor reporting via
[WO-F](../../../samples/chm/extracted/wo-f_enter_labor.htm) /
[WO-M](../../../samples/chm/extracted/wo-m_batch_labor_entry.htm) /
Data Collection defaults to the most-recently-assigned child.

**Important:** parent-child is **finite-scheduling only**. Infinite
and Lead Time don't support it; for those methods, combine capacity
on a single work center and use [SH-D](#sh-d-manually-schedule-machines)
+ [SH-J](#sh-j-print-machine-schedule) to dispatch to specific
machines.

### Sequence Completion Flag

Scheduling programs don't know a sequence is done until a **Finish
Date** lives on the work-order-routing record. Set automatically
when [WO-F](../../../samples/chm/extracted/wo-f_enter_labor.htm) or
[DC-A](../../../samples/chm/extracted/dc-a_enter_labor_production.htm)
is answered Y to "Is this sequence now complete?" After-the-fact
fix: [WO-K-F Edit Sequence Started/Finished Dates](../../../samples/chm/extracted/wo-k-f_edit_sequence_started_finished_dates.htm).

Forgotten completion flags are a classic cause of sequences that
keep re-scheduling after they're actually finished.

---

## Method: Finite Scheduling

*Source: [how_finite_scheduling_works.htm](../../../samples/chm/extracted/how_finite_scheduling_works.htm)*

The most automatic method. **You set Start Date only**; SH-E
calculates everything else, respecting work-center capacity.

### The four phases

| Phase | What happens |
|---|---|
| 1. Build buckets | Create empty daily buckets for every **schedulable** work center. Skipped: outside-processing, parents, `Finite Scheduling? = N`, `Total Hours/Day = 0`, `> 24 hrs/day`. |
| 2. Load + rank | Load active sequences into buckets; calculate each WO's critical ratio; display sortable list for due-date edits + recalc. |
| 3. Schedule | Process WOs in ascending-critical-ratio order; for each sequence, drop into the earliest fitting bucket; record contention. |
| 4. Report | Print the finite schedule report (sortable by WO # or Due Date) + warnings for WOs without routings. |

### First-time setup — the 5-step dance

Done **in order**, once before relying on SH-E:

1. **Run `SCHUPD`** via [UT-A Run a TAS Program](../../../samples/chm/extracted/ut-a_run_a_tas_program.htm)
   — initializes `Finite Scheduling? = Y` on non-outside WCs, sets
   `Parent? = N` everywhere, backfills Started Dates on already-
   reported sequences.
2. **Generate shop calendar** in [SM-H](../../../samples/chm/extracted/sm-h_enter_shop_calendar.htm).
3. **Review work centers** in [RO-C](../../../samples/chm/extracted/ro-c_enter_work_centers.htm)
   — no more than 24 hrs/day, `Total Hours/Day` = `Total Shift Hours`.
   Identify parent-child groupings.
4. **Run SH-E to find 00/00/00 Due Dates** — Due Date is now
   required. Any WOs pre-dating that requirement will show up at the
   top; fix via [WO-A](../../../samples/chm/extracted/wo-a_enter_work_orders.htm)
   or the SH-E opening list.
5. **Run [WO-K-F](../../../samples/chm/extracted/wo-k-f_edit_sequence_started_finished_dates.htm)
   to close already-done sequences** — use [SH-O](#sh-o-finite-schedule-bucket-report)
   to find candidates (sequences marked `==>> Running <<==`) and
   [WO-L-A Print Work Order Status](../../../samples/chm/extracted/wo-l-a_print_work_order_status.htm)
   to confirm actual state. Use today's date for expediency. Also
   enter started dates for outside-processing sequences via
   [SH-I](#sh-i-print-work-center-schedule)'s PO Date column.

### Accuracy of the schedule depends on routings

> "Whenever you close a work order... you should review work order
> performance and see if any of your routing sequences should be
> adjusted so that they will be more accurate the next time the item
> is run again." — vendor

Tools for this feedback loop:
- [JC-A Print Job Cost Report](../jc-job-costing/help-content.md#jc-a-print-job-cost-report) — estimated vs actual per WO.
- [JC-H Print Work Order History](../jc-job-costing/help-content.md#jc-h-print-work-order-history) — average times per sequence across WOs; can write back to routing masters.

### Expanding / shrinking capacity

When SH-O shows one bottleneck work center dominating contention:
- **Per-WC `% Utilization`** in RO-C loosens scheduling for that WC
  (multiplies all its time allocations by 1/utilization).
- Move due dates out on the problem WO → frees the WC for others.
- Add OT / personnel / machine to that WC.
- Farm out some work (outside processing).

---

## Method: Infinite Scheduling

*Source: [how_infinite_scheduling_works.htm](../../../samples/chm/extracted/how_infinite_scheduling_works.htm)*

Semi-manual. **You set both Start Date and Finish Date** on every WO;
[SH-F](#sh-f-infinite-scheduling) distributes sequence dates across
that window ignoring capacity.

### The date-distribution formula

```
available days = finish - max(start, today) - non-workdays - outside-proc lead times

seq % = remaining production time (this seq) / total remaining production time

seq share = available days × seq %
```

Direct-labor sequences get `seq share` of available days added to
the previous sequence's finish date. Outside-processing sequences
get their routing `Lead Time` (in days) added instead.

Each sequence's Finish = the next sequence's Start (no gaps).

### Why it's called "infinite"

Work center capacity is ignored during the scheduling pass — the
program assumes you have unlimited capacity. In practice capacity
very much matters; the workflow is:
1. Assign realistic WO dates based on what you think you can deliver.
2. Run SH-F.
3. Review work-center load via [SH-I](#sh-i-print-work-center-schedule)
   and [SH-R](#sh-r-work-center-scheduler).
4. Where overloaded → add OT / personnel, or push WO finish dates out.

### Sequence dates are time windows

Since finish = next start exactly, the dates form **tight windows**
rather than hard deadlines. Production foremen have leeway on which
WO to run day-to-day as long as each sequence completes within its
window.

### Due Date is basically unused

The WO **Finish Date** serves as the effective due date (since SH-F
doesn't move it). Convention: enter Finish Date = Due Date; treat
Due Date as reference.

### Parent-child NOT supported

Model interchangeable machines/stations as a **single** WC with
combined `Total Hours/Day`, then use [SH-D](#sh-d-manually-schedule-machines)
for specific machine dispatch.

---

## Method: Lead Time Scheduling

*Source: [how_lead_time_scheduling_works.htm](../../../samples/chm/extracted/how_lead_time_scheduling_works.htm)*

Calculates total process time from routing + queue + outside lead
time, then generates the missing end of the start/finish pair.

### The production-days formula

```
days required = Σ (seq qty × time-per-part)
              + Σ setup time
              + Σ positive overlap
              + Σ work-center queue time             (labor sequences)
              + Σ outside-processing lead time       (outside-proc sequences)
```

Each labor-sequence piece accounts for the work center's shift hours
and `% Utilization`.

### Forward vs Backward vs Backward-from-Due

At WO save / SH-P run, you pick:
- **Forward** — enter Start, program calculates Finish.
- **Backward (from Finish)** — enter Finish, program calculates Start.
- **Backward (from Due)** — program uses Due Date as the target
  Finish; if that doesn't fit, it falls back to "earliest-possible
  Finish Date with Start = today".

### Queue time = estimated contention

Set in [RO-C](../../../samples/chm/extracted/ro-c_enter_work_centers.htm)
per work center, **per WO Priority (1 / 2 / 3)**. Lead Time
Scheduling uses the one matching the WO's priority. Only **Average
Queue Time** is used by [SH-N Generate Lead Times](#sh-n-generate-lead-times).

This is the key difference vs finite: contention is **modeled as a
number you enter** rather than computed from actual bucket contention.

### Default opt-in

Set `Use Lead Time Scheduling?` to `F` or `B` in
[SD-B Work Orders Defaults](../../../samples/chm/extracted/sd-b_work_order_defaults.htm)
to make [WO-A](../../../samples/chm/extracted/wo-a_enter_work_orders.htm) /
[SO-N](../../../samples/chm/extracted/so-n_convers_sales_orders_to_work_orders.htm) /
[ES-E](../../../samples/chm/extracted/es-e_convert_estimates.htm)
use this logic instead of the fixed inventory lead time when
creating WOs.

**Precondition:** the shop calendar MUST exist before toggling this
on. The program depends on non-workday skipping.

### Finish ≠ Due when scheduling forward

If forward scheduling and Finish > Due, the WO is already late at
creation time — visible on [SH-G](#sh-g-print-work-order-schedule) /
[SH-H](#sh-h-print-work-order-status). Decide: move Due, add
capacity, or split the WO.

### Parent-child NOT supported

Same limitation as Infinite — combine stations into one WC.

---

## Method: Manual Scheduling

*Source: [how_manual_scheduling_works.htm](../../../samples/chm/extracted/how_manual_scheduling_works.htm)*

You type every date. Best for shops with few WOs and simple products.

### Sequence dates are optional

If you **don't** enter sequence dates, WO Start Date and Finish Date
get used as the sequence start and finish. That means
[SH-H Print Work Order Status](#sh-h-print-work-order-status) shows
overall WO dates, not per-sequence detail — sufficient for most
manual-scheduling shops.

If you **do** want per-sequence dates, enter via
[SH-B](#sh-b-manually-schedule-work-orders) or
[SH-C](#sh-c-manually-schedule-work-centers). If it gets tedious,
switch to [SH-F Infinite Scheduling](#sh-f-infinite-scheduling).

### Common programs

Same as Infinite + Lead Time: [SM-H](../../../samples/chm/extracted/sm-h_enter_shop_calendar.htm),
[RO-C](../../../samples/chm/extracted/ro-c_enter_work_centers.htm),
[WO-A](../../../samples/chm/extracted/wo-a_enter_work_orders.htm),
SH-A / SH-B / SH-C / SH-D (editors), SH-G / SH-H / SH-I / SH-J
(reports), plus [MR-F](../../../samples/chm/extracted/mr-f_generate_mrp_requirements.htm) /
[MR-H](../../../samples/chm/extracted/mr-h_print_order_action_report.htm)
for the MRP feedback loop.

---

## SH-A Edit WO Start/Finish/Due Dates

*Source: [sh-a_edit_wo_start_finish_dates.htm](../../../samples/chm/extracted/sh-a_edit_wo_start_finish_dates.htm)*

Fast bulk editor for WO header dates. Faster than using [WO-A](../../../samples/chm/extracted/wo-a_enter_work_orders.htm)
when many date changes are needed.

### Behavior

- **Filter screen** — Start Date floor, Status Codes, Priority Codes
  (X = include).
- **List + auto-entry mode** — after saving one WO's date edits, the
  next WO in the filtered list pops in automatically. Toggle off
  with **Disable Auto-Entry Mode** to return to the list after each.

### Finite-scheduling gotcha

> "If you are using finite scheduling, do not waste time changing
> the Finish Date because it changes each time [SH-E] is run." —
> vendor

---

## SH-B Manually Schedule Work Orders

*Source: [sh-b_manually_schedule_work_orders.htm](../../../samples/chm/extracted/sh-b_manually_schedule_work_orders.htm)*

Per-WO date editor with routing-sequence drilldown. Also doubles as
a sequence inquiry for any scheduling method.

### Two sections per WO

1. **Header** — Start Date, Finish Date, Due Date, Priority, Lead Time.
2. **Sequence list** — per-sequence Start Date / Finish Date with
   auto-entry mode. Reference columns: sequence description, overlap
   days, work center + description, queue time.

### When to enter sequence dates

**Manual only.** Under finite / infinite / lead time the scheduling
programs overwrite them.

---

## SH-C Manually Schedule Work Centers

*Source: [sh-c_manually_schedile_work_centers.htm](../../../samples/chm/extracted/sh-c_manually_schedile_work_centers.htm)*

Per-work-center editor — the mirror of [SH-B](#sh-b-manually-schedule-work-orders)
(which is per-WO).

### Two functions in one screen

1. **Work-center parameters** — alternative to [RO-C](../../../samples/chm/extracted/ro-c_enter_work_centers.htm)
   for `Total Hours/Day`, `% Utilization`, `Total Shift Hrs`.
2. **Sequence dates for all WOs in this WC** — per-sequence Start
   Date / Finish Date edits with auto-entry mode. Manual scheduling
   only.

---

## SH-D Manually Schedule Machines

*Source: [sh-d_manually_schedule_machines.htm](../../../samples/chm/extracted/sh-d_manually_schedule_machines.htm)*

Assign sequences to specific machines within a WC. Usable with
**manual, lead time, or infinite** scheduling. Finite users should
use parent-child WCs instead.

Machines come from [RO-D Enter Machines](../../../samples/chm/extracted/ro-j-b_print_work_centers.htm).

### Two UIs documented in the same help topic

The help page actually covers **two views** with the same name:

**1. Machine View (graphical, Java-based)**
- Create named **layouts** that group machines (by WC or any other
  criterion). Machines can appear in multiple layouts.
- Right-click canvas → Add Machine; arrange as list or factory-floor
  layout. Linked images on machines show up (don't resize — provide
  small ones).
- Dropdowns: planning horizon date, work center. Pick a WC → its
  open operations appear on the left.
- **Drag an operation to a machine** to assign; drag across
  machines to reassign. Operations under each machine sort by
  execution order — drag up/down to reorder.
- **Color coding:** green = running (open DC labor record OR hours/
  parts already charged), blue = assigned but unstarted, black =
  unstarted + unassigned.
- Needs ODBC — see [external-odbc-connections.md](../../01-architecture/external-odbc-connections.md).

**2. Classic Entry-Area View**
- Filter WC + machine range → list of sequences for that WC.
- Highlight a sequence → change Mach, Start Date, Finish Date in the
  entry area. Auto-entry advances to next.

### Machine prompt on labor entry

Controlled by `Display Machine Prompt in Enter Labor?` in
[SD-E Scheduling Defaults](../../../samples/chm/extracted/sd-e_scheduling_defaults.htm).
When Y, [WO-F](../../../samples/chm/extracted/wo-f_enter_labor.htm)
shows the assigned machine; you can change it if the actual run
happened elsewhere.

To **require** a machine entry (not blank), set `Prevent Blank
Machine at DC-A` to Y in
[SD-F Data Collection Defaults](../../../samples/chm/extracted/sd-f_data_collection_defaults.htm).

---

## SH-E Finite Scheduling

*Source: [sh-e_finite_scheduling.htm](../../../samples/chm/extracted/sh-e_finite_scheduling.htm)*

The finite scheduler. See [Method: Finite Scheduling](#method-finite-scheduling)
above for the how/why.

### Operation

1. Enter **date through which labor/production has been posted** —
   schedule begins from the next day.
2. `Generate new schedule` vs `Reprint existing schedule`.
3. Report sort: `Due Date` or `Work Order number`.
4. **Opening list** displays all WOs in critical-ratio order; Due
   Dates can be edited here. Click **Re Process** to recalc ratios
   based on the edits.
5. Click **Go** → scheduling runs.
6. Standard List / Printer / Disk output prompt.

### Report columns (for reference)

WO #, item #, order qty, critical ratio, due date, scheduled start,
scheduled finish, remaining run days, days-until-due, **days late**,
**days contention**.

---

## SH-F Infinite Scheduling

*Source: [sh-f_infinte_scheduling.htm](../../../samples/chm/extracted/sh-f_infinte_scheduling.htm)*

Runs the infinite-scheduling pass. See
[Method: Infinite Scheduling](#method-infinite-scheduling) for
the distribution formula.

### Operation

- Filters: Status Codes, Priority Codes, WO range, Start Date range,
  Finish Date range, WO Class range.
- Each WO number displays as it's scheduled.
- **Exception report at the end** lists any WOs that couldn't be
  scheduled.

---

## SH-G Print Work Order Schedule

*Source: [sh-g_print_work_order_schedule.htm](../../../samples/chm/extracted/sh-g_print_work_order_schedule.htm)*

Listing of all open WOs with Start Date, Finish Date, remaining
quantity, and days late (if Finish Date > Due Date).

**Filters:** sort (Start or Finish), Status codes, Priority codes,
WO Class, **`Late`** toggle under Priority codes (for late-only
filter), WO range, item range, customer range.

---

## SH-H Print Work Order Status

*Source: [sh-h_print_work_order_status.htm](../../../samples/chm/extracted/sh-h_print_work_order_status.htm)*

Per-WO, per-sequence status: current Start / Finish Date per
sequence, remaining qty, estimated hours remaining, days late.

Late sequences get an **asterisk** to visually highlight behind-
schedule WOs.

**Filters:** WO, Start Date, Finish Date, item, customer.

---

## SH-I Print Work Center Schedule

*Source: [sh-i_prnt_work_center_schedule.htm](../../../samples/chm/extracted/sh-i_prnt_work_center_schedule.htm)*

The **daily dispatch report** — per-work-center list of uncompleted
sequences.

### Backlog-in-days

Total hours of backlog in the date range ÷ hours/day in the WC =
**backlog in days**. Lets you compare load across WCs of different
sizes.

**Filters:** sort (Start or Finish), Status / Priority / Class
toggles, WO / item / customer / Start Date / Finish Date ranges,
`Skip sequences with 0 quantity?` toggle.

---

## SH-J Print Machine Schedule

*Source: [sh-j_print_machine_schedule.htm](../../../samples/chm/extracted/sh-j_print_machine_schedule.htm)*

Per-machine version of SH-I. Sequences must have been assigned to
machines via the product's routing or [SH-D](#sh-d-manually-schedule-machines).

**Not for finite scheduling** — the vendor recommends parent-child
WCs for finite. Same filter set as SH-I.

---

## SH-K View Work Center Load

*Source: [sh-k_view_work_center_load.htm](../../../samples/chm/extracted/sh-k_view_work_center_load.htm)*

**Real-time dashboard** of a single work center: currently-running
WOs (top pane) + queued WOs (bottom pane).

### Precondition

Requires [Data Collection](../../../samples/chm/extracted/data_collection.htm)
or [HH-I Paperless Shop Floor Tracking](../../../samples/chm/extracted/hh-i_paperless_shop_floor_tracking.htm)
for clock-in/clock-out — otherwise only the queue is meaningful (no
data for "currently running").

### Behavior

- Pick WC + refresh interval + `Include F-status WOs?` flag.
- Top pane: clocked-in WOs sorted by WO #, with employee name.
- Bottom pane: queue sorted by Priority + scheduled start.
- Highlighting a line highlights the corresponding entry in the
  other pane (if any).
- Auto-refreshes per the timer.

---

## SH-L View or Calculate Work Center Load

*Source: [sh-l_view_or_calculate_work_ce.htm](../../../samples/chm/extracted/sh-l_view_or_calculate_work_ce.htm)*

**Historical / projected % load** per WC per day — numeric + graph.

### Tools menu

- **Recalculate** — rebuild load from today forward based on open
  WOs. **Important:** all open operations with past dates get moved
  to "today".
- **Get History / Hide History** — toggle display of prior periods.
- **Export to CSV** — dumps to CSV and opens in Excel.

---

## SH-M Lead Time Estimator

*Source: [sh-m_lead_time_estimator.htm](../../../samples/chm/extracted/sh-m_lead_time_estimator.htm)*

**What-if calculator** for realistic delivery dates on any item +
quantity. Primary use: quoting to customers.

### Output

Given item + qty + Start Date, the program calculates:
- Projected total run-time days (setup + run + outside lead + WC
  queue).
- Estimated Finish Date for **each of the three priorities (1/2/3)**
  — higher-priority WOs have shorter queue waits.
- A "no queue time" finish date as a baseline for comparison.

Skips non-working days from the shop calendar.

### Scope limit

Single-level only. Does NOT factor in subassembly manufacturing time
— if the item has multi-level BOMs, the actual lead time is longer.

---

## SH-N Generate Lead Times

*Source: [sh-n_generate_lead_times.htm](../../../samples/chm/extracted/sh-n_generate_lead_times.htm)*

Bulk recalculation of the inventory `Lead Time` field for
manufactured items. MRP uses this Lead Time to set suggested-WO
start dates.

### What gets recomputed

Same formula as [SH-M](#sh-m-lead-time-estimator) but run for **every
manufactured item** in the filter range, using each item's **Lot
Size** as the quantity. Lot Size lives in [IN-B](../../../samples/chm/extracted/in-b_enter_inventory.htm) /
[IN-L-A](../../../samples/chm/extracted/in-l-a_enter_standard_costs.htm) /
[RO-A](../../../samples/chm/extracted/ro-a_enter_routings.htm).

Uses **Average Queue Time** per WC (not the per-priority queue
times).

### Filters

Item range, types (F/A/M), class, category, cycle code, report
option. Final report lists every lead time that changed, with old
vs new values.

### The cycle

1. Update WC queue times / hours in [RO-C](../../../samples/chm/extracted/ro-c_enter_work_centers.htm)
   as conditions change.
2. Run SH-N to push those changes into inventory lead times.
3. Next MRP run picks up the new lead times for suggested WO start
   dates.

---

## SH-O Finite Schedule Bucket Report

*Source: [sh-o_finite_schedule_bucket_report.htm](../../../samples/chm/extracted/sh-o_finite_schedule_bucket_report.htm)*

**Finite-scheduling only.** Per-work-center bucket analysis — the
tool for spotting bottlenecks.

### Columns

work center, work order, sequence, start date, finish date, shop
start date, shop finish date, scheduling units, days, critical
ratio, **contention**.

Total contention per WC = the bottleneck indicator. Dominant
contention in one WC → that's where you add capacity / push out WOs /
farm out work.

Also used during finite-scheduling initial setup (step 5 in the
[5-step dance](#first-time-setup--the-5-step-dance)) to find
sequences marked as still running that are actually complete — look
for `==>> Running <<==` in the critical-ratio column.

---

## SH-P Lead Time Scheduling

*Source: [sh-p_lead_time_scheduling.htm](../../../samples/chm/extracted/sh-p_lead_time_scheduling.htm)*

Re-scheduler for existing WOs under the Lead Time method. [WO-A](../../../samples/chm/extracted/wo-a_enter_work_orders.htm) /
[SO-N](../../../samples/chm/extracted/so-n_convers_sales_orders_to_work_orders.htm) /
[ES-E](../../../samples/chm/extracted/es-e_convert_estimates.htm) use
the same logic at WO creation; SH-P is for when conditions change
(queue times, shift hours) after creation.

### Operation

- Filters: Status Codes, Priority Codes, WO range, Start Date,
  Finish Date, WO Class.
- **Forward / Backward** prompt — default from [SD-B](../../../samples/chm/extracted/sd-b_work_order_defaults.htm).
- **Backward** also prompts: reschedule based on current Finish Date
  or Due Date.
- If not enough days → forward-schedules from today, warns that
  some finish dates couldn't be met.

### Dependent Scheduling

Backward scheduling optionally **cascades** — subassembly WOs are
rescheduled to finish when the higher-level WO starts, **provided**
the subassembly WOs were generated via
[SO-N Convert Sales Orders to Work Orders](../../../samples/chm/extracted/so-n_convers_sales_orders_to_work_orders.htm)
with the multi-assembly option, or via
[WO-K-D Create Multi-Assy Work Orders](../wo-work-orders/help-content.md#wo-k-d-create-multi-assy-work-orders).

---

## SH-R Work Center Scheduler

*Source: [sh-r_work_center_scheduler.htm](../../../samples/chm/extracted/sh-r_work_center_scheduler.htm)*

**Visual Gantt-chart-style scheduler** — Java-based. Drag-and-drop
WOs or operations across time.

### Working copy pattern

Loads into **copies** of the WO + WO routing files. No other
programs see changes until you explicitly post.

Three entry actions at load:
- **Initialize** the scheduling files and start the scheduler.
- **Continue editing** a prior session.
- **Post changes** to the live WO files.

### Two views

**1. Work Order Scheduler** (macro view)
- Filters: priorities, locations, list order, include R/F statuses,
  planning horizon.
- **First run suggestion:** run [SH-P](#sh-p-lead-time-scheduling)
  first if WOs have past dates.
- WO list on the left, timeline bars on the right. Color per status
  (R = red, F = black) + per-priority bar colors from [SM-P-G Enter
  WO Priority Codes](../../../samples/chm/extracted/sm-p-g_enter_wo_priority_codes.htm).
- Drag WOs forward/backward in time.
- **Options toggle: move vs stretch/squeeze**. Stretching/squeezing
  prompts for new per-operation dates within the new WO window.

**2. Work Center Scheduler** (micro view)
- Pick a WC; displays all scheduled operations on a timeline.
- Drag operations forward/backward — prior + subsequent operations on
  the **same WO** follow (push out / pull back).
- Same move vs stretch/squeeze toggle.
- Save per WC, then Close → Post Visual Scheduler Dates when done.

### Precondition

Requires ODBC for the Java side. See
[external-odbc-connections.md](../../01-architecture/external-odbc-connections.md)
and the help topic [ODBC Data Connection](../../../samples/chm/extracted/odbc_data_connection.htm).

---

## Cross-references

### Data consumed / produced

Per
[file-names-index · Scheduling](../../04-data-dictionary/file-names-index.md#scheduling):

| Table | Purpose |
|---|---|
| `CALENDAR` / `SCHEDCAL` | Shop calendar (general + scheduling variant) |
| `BUCKETS` | Finite-scheduling buckets |
| `SCHWO` / `WCCTL` | Finite-scheduling temp files |
| `WCTRSLOD` | Temp WC load % (Visual Scheduler) |
| `WORKSORD` / `WOSROUT` | Temp WO header + routing (Visual Scheduler) |
| `CALTEMP` | Temp file for calendar generation |

Input data: `WORKORD` / `WOROUT` (WO), `WORKCTR` (work centers),
`MACHINE` (machines), all via
[file-names-index · Work Orders](../../04-data-dictionary/file-names-index.md#work-orders) /
[Routings](../../04-data-dictionary/file-names-index.md#routings).

### Related LearnEVO modules

- [WO — Work Orders](../wo-work-orders/README.md) —
  [help-content](../wo-work-orders/help-content.md). Dates SH
  programs edit live on `WORKORD` / `WOROUT`. See also
  [WO-K-F Edit Sequence Started/Finished Dates](../wo-work-orders/help-content.md#wo-k-f-edit-sequence-started--finished-dates)
  for the sequence-completion fix-up.
- [MR — MRP](../mr-mrp/README.md) —
  [help-content](../mr-mrp/help-content.md). Half of the scheduling/
  MRP feedback loop; see also [MR-F](../mr-mrp/help-content.md#mr-f-generate-material-requirements) and
  [MR-H](../mr-mrp/help-content.md#mr-h-print-order-action-report).
- Routings module (no LearnEVO help doc yet) — [RO-A / RO-C / RO-D](../../../samples/chm/extracted/ro-a_enter_routings.htm)
  are where the times, queue times, and machines that SH consumes
  get defined.
- [JC — Job Costing](../jc-job-costing/README.md) —
  [help-content](../jc-job-costing/help-content.md).
  [JC-A](../jc-job-costing/help-content.md#jc-a-print-job-cost-report) and
  [JC-H](../jc-job-costing/help-content.md#jc-h-print-work-order-history)
  feed the routing-accuracy feedback loop.
- [DC — Data Collection](../dc-data-collection/README.md) — powers
  real-time data in [SH-K](#sh-k-view-work-center-load) and the
  "currently running" coloring in [SH-D Machine View](#sh-d-manually-schedule-machines).

### Related CHM overview sections

- [System Overview § Sequence of Events — Manufacturing Planning](../../00-overview/system-overview.md#7a-manufacturing-planning)
  — where SH sits in the big picture.
- [External ODBC connections](../../01-architecture/external-odbc-connections.md)
  — for SH-D Machine View and SH-R Work Center Scheduler.
