# Data Collection (DC) — Vendor Help Content

Status: verified (summarized from the vendor's help file).

Source CHM: `\\i2s109-solidcrm\DBAMFG$\EVOHELP.CHM` →
[samples/chm/EvoHELP.CHM](../../../samples/chm/EvoHELP.CHM) →
decompiled to [samples/chm/extracted/](../../../samples/chm/extracted/).
Extracted via [scripts/chm_to_md.py](../../../scripts/chm_to_md.py).

This doc consolidates the **14 help topics** under the CHM's
*Manufacturing → Data Collection* category (overview + 13 programs,
DC-A through DC-N — no DC-J). Each program gets its purpose, key
behaviors, and cross-links. Full verbatim source is one click away
via each `Source:` link.

For the companion schema + menu + form view of this module, see
[README.md](README.md) in this folder.

---

## Contents

- [Overview — shop-floor labor entry, live vs batch](#overview--shop-floor-labor-entry-live-vs-batch)
- [Design model — modes, shifts, multi-WO policy](#design-model--modes-shifts-multi-wo-policy)

**Daily entry**
- [DC-A Enter Labor / Production](#dc-a-enter-labor--production)
- [DC-B Enter Production Only](#dc-b-enter-production-only)
- [DC-C Enter Labor Only](#dc-c-enter-labor-only)
- [DC-L Shift Clock In / Out](#dc-l-shift-clock-in--out)

**Barcode printing**
- [DC-E Print Labor Tickets](#dc-e-print-labor-tickets)
- [DC-F Print Employee Tickets](#dc-f-print-employee-tickets)

**Review / correction / posting**
- [DC-D Print Labor Status](#dc-d-print-labor-status)
- [DC-G Edit Labor Transactions](#dc-g-edit-labor-transactions)
- [DC-H Post Labor Transactions](#dc-h-post-labor-transactions)

**Inquiry / admin**
- [DC-I Work Order Inquiry](#dc-i-work-order-inquiry)
- [DC-M Employee Dashboard](#dc-m-employee-dashboard)
- [DC-K Archive or Purge Shift Records](#dc-k-archive-or-purge-shift-records)
- [DC-N Enter Holiday Shift Records](#dc-n-enter-holiday-shift-records)

---

## Overview — shop-floor labor entry, live vs batch

*Source: [data_collection.htm](../../../samples/chm/extracted/data_collection.htm)*

DC replaces after-the-fact labor entry from paper time cards /
tickets. Employees enter labor **directly on shop-floor computers**,
via numeric keypad or barcode scanner. The entry program is normally
left running all day as a makeshift time clock.

### Transaction flow

1. Employee makes entries in [DC-A](#dc-a-enter-labor--production) /
   [DC-B](#dc-b-enter-production-only) / [DC-C](#dc-c-enter-labor-only).
2. Transactions land in the DC transactions file (`BKDCPLAB` —
   unposted per
   [file-names-index](../../04-data-dictionary/file-names-index.md#data-collection)).
3. Review / correct via [DC-D](#dc-d-print-labor-status) +
   [DC-G](#dc-g-edit-labor-transactions).
4. Post to the permanent WO files via [DC-H](#dc-h-post-labor-transactions)
   — or configure **real-time posting** in
   [SD-F Data Collection Defaults](../../../samples/chm/extracted/sd-f_data_collection_defaults.htm).
5. After posting, edits require [WO-K-K Edit Posted DC Labor](../wo-work-orders/help-content.md#wo-k-k-edit-posted-dc-labor).

### Hardware

Standard PCs with USB or Bluetooth "wedge" barcode readers.
**Requirement:** readers must handle **3-character barcodes** (some
devices have a 4-character minimum and can't read the 3-character WO
suffix).

---

## Design model — modes, shifts, multi-WO policy

Three recurring concepts that show up across DC programs.

### Three modes of data collection

Pick based on whether you care about time, parts, or both:

| Mode | Program | Records |
|---|---|---|
| **Labor + Production** | [DC-A](#dc-a-enter-labor--production) | Time + parts made + parts scrapped |
| **Production Only** | [DC-B](#dc-b-enter-production-only) | Parts made + parts scrapped |
| **Labor Only** | [DC-C](#dc-c-enter-labor-only) | Time |

"Production Only" is for scheduling-driven shops: sequence completion
updates what the Work Center Backlog report and Scheduling module
read, which is what they actually care about. Can be combined with
`Use Standard Time? = Y` in [SD-I Routings Defaults](../../../samples/chm/extracted/sd-i_routings_defaults.htm)
to charge standard time × parts to the WO without collecting actual
time.

"Labor Only" is for job-costing-driven shops where sequence
completion state isn't important.

### Shifts and buffer periods

Shifts are defined in [SD-F Data Collection Defaults](../../../samples/chm/extracted/sd-f_data_collection_defaults.htm).
Each employee is **assigned** to a shift in
[SM-G Enter Employees](../../../samples/chm/extracted/sm-g_enter_employees.htm)
— **not** chosen at entry time.

Three time-management features on the shift:
- **Pre/post buffers** — employees can clock in before the shift
  starts and after it ends (avoids terminal queue pileups at shift
  boundaries). **Job costing only runs between the official shift
  start and end** — buffer time doesn't bill to WOs.
- **Lunches / breaks** — defined on the shift; job costing pauses
  automatically without requiring clock-out.
- **Employee Shift Start/Stop** — optional feature. When on, the
  employee must clock into their shift before clocking into any WO;
  clocking out of the shift clocks out all open WOs. Produces a
  single per-day shift record for payroll (eliminates the Indirect-WO
  workaround for non-productive time). Shift data can be pushed to
  Payroll via [PR-K Print/Post Time Cards](../../../samples/chm/extracted/pr-k_print_post_time_cards.htm).

### Multi-WO clocking policy

Whether an employee can be clocked into two or more sequences
simultaneously is controlled in two places:
1. **System default:** [SD-F Data Collection Defaults](../../../samples/chm/extracted/sd-f_data_collection_defaults.htm)
   → `Allow clocking in/out on multiple jobs?`.
2. **Per-employee override:** [SM-G Enter Employees](../../../samples/chm/extracted/sm-g_enter_employees.htm).

When multi-WO is enabled, **every clock-in or clock-out event
auto-closes and auto-reopens all currently-open sequences** so that
the labor cost for each time segment gets distributed proportionally
across what the employee was doing during that segment.

**Consequence:** a single employee-sequence-session may produce
**multiple transaction records**. Parts produced are reported on the
**last transaction** only. This matters in [DC-G Edit Labor
Transactions](#dc-g-edit-labor-transactions) — you may see more rows
than you expect, and edits have to account for it.

### Auto-close on last operation

A default flag controls whether reporting qty complete against the
**last routing sequence** automatically processes
[WO-I Enter Finished Production](../wo-work-orders/help-content.md#wo-i--enter-finished-production)
— placing the items into stock without a separate step.

---

## DC-A Enter Labor / Production

*Source: [dc-a_enter_labor_production.htm](../../../samples/chm/extracted/dc-a_enter_labor_production.htm)*

The full-featured entry program. Runs all day as a shop-floor time
clock. Each entry captures: employee, WO, sequence, clock-in vs
clock-out (Run or Setup), parts made, parts scrapped + scrap code,
rework qty + QC code.

### Inputs

- **Employee number** — typed on the keypad, or scan a barcoded
  employee ticket from [DC-F](#dc-f-print-employee-tickets).
- **Work Order** — typed, or scan barcode from a traveler
  ([WO-C](../wo-work-orders/help-content.md#wo-c--print-travelers))
  or labor ticket ([DC-E](#dc-e-print-labor-tickets)). Must be status
  **R (Released)** or **I (Indirect)**.
- **Sequence** — typed or scanned. Shows the sequence description as
  confirmation.
- **Run vs Setup** — prompted at clock-in if the default is on.
- **Clock-out extras:** parts good, parts scrapped (+ scrap code),
  rework (+ QC code), NCR routing (feeds
  [QC-F-C Disposition NCR](../../../samples/chm/extracted/qc-f-c_disposition_ncr.htm)).

### Shift integration

If **Employee Shift Start/Stop** is on, the first WO clock-in of the
day automatically starts the shift. **Shift Start/Stop button** at
top lets you start/end the shift explicitly without needing a WO
(for payroll-only days).

### Setup requirements

Done in [SD-F Data Collection Defaults](../../../samples/chm/extracted/sd-f_data_collection_defaults.htm):
- Shifts defined.
- **Full-screen mode** recommended.
- Multi-WO clocking policy.
- Real-time vs batch posting flag.

---

## DC-B Enter Production Only

*Source: [dc-b_enter_production_only.htm](../../../samples/chm/extracted/dc-b_enter_production_only.htm)*

Just parts — employee / WO / sequence / parts made / parts scrapped.
Ideal for scheduling-focused shops; see
[Design model § Three modes](#three-modes-of-data-collection).

**Sequence completion isn't visible** to Work Center Backlog or
Scheduling until [DC-H](#dc-h-post-labor-transactions) runs — unless
real-time part posting is on in [SD-F](../../../samples/chm/extracted/sd-f_data_collection_defaults.htm).

> "The employee number provides a record as to who made the entry.
> If you don't wish to track entries to specific employees, you can
> always set up a dummy employee number in [SM-G] and use that
> number for all entries." — vendor

---

## DC-C Enter Labor Only

*Source: [dc-c_enter_labor_only.htm](../../../samples/chm/extracted/dc-c_enter_labor_only.htm)*

Same program flow as [DC-A](#dc-a-enter-labor--production) minus the
parts-made / parts-scrapped prompts.

> **Trade-off:** job costing works, but without parts counts you
> won't know which routing sequences are actually complete. If you
> need sequence-completion tracking (for Scheduling or Work Center
> Backlog), use DC-A or DC-B instead.

---

## DC-D Print Labor Status

*Source: [dc-d_print_labor_status.htm](../../../samples/chm/extracted/dc-d_print_labor_status.htm)*

Listing / on-screen view of DC transactions. Columns: employee,
name, date, WO, sequence, shift, time-in, time-out.

### Three states, each with their own filter toggle

- **Open** — clocked in, not yet clocked out.
- **Pending** — clocked out, not yet posted via
  [DC-H](#dc-h-post-labor-transactions).
- **Posted** — already live on WO files. Active vs archived WOs
  selectable here.

### Shift data export

**"Print the Shift data only"** option, plus CSV export — used to
drive payroll import via
[PR-K Print/Post Time Cards](../../../samples/chm/extracted/pr-k_print_post_time_cards.htm).

### Performance note

> "The posted data collection transaction file gets very large, so
> we recommend that you enter some filters" — vendor.

Periodic cleanup:
[SM-J-H Purge Data Collection File](../../../samples/chm/extracted/sm-j-h_purge_data_collection_file.htm).

---

## DC-E Print Labor Tickets

*Source: [dc-e_print_labor_tickets.htm](../../../samples/chm/extracted/dc-e_print_labor_tickets.htm)*

Per-sequence barcoded tickets — alternative to
[WO-E Print Labor Cards/Labels](../wo-work-orders/help-content.md#wo-e--print-labor-cards--labels).

Two barcodes per ticket: WO number + sequence number. Used at
clock-in / clock-out.

### Why labor tickets beat scanning the traveler

> "With labor tickets there is no danger that the wrong sequence
> gets accidentally scanned, which could happen with a bar coded
> shop traveler." — vendor

Typical workflow: print labor tickets alongside the traveler; insert
everything into a plastic shop-packet jacket; print extras so the
shop doesn't run short.

**Filters:** WO number range (prefix-only = all suffixes) and
tickets-per-operation count.

---

## DC-F Print Employee Tickets

*Source: [dc-f_print_employee_tickets.htm](../../../samples/chm/extracted/dc-f_print_employee_tickets.htm)*

Barcoded employee-number tickets. Commonly laminated and used as
employee ID badges.

**Filters:** employee number range + tickets-per-employee count.

---

## DC-G Edit Labor Transactions

*Source: [dc-g_edit_labor_transactions.htm](../../../samples/chm/extracted/dc-g_edit_labor_transactions.htm)*

Pre-posting corrections. Once
[DC-H](#dc-h-post-labor-transactions) runs, records are locked here
— edit via [WO-K-K Edit Posted DC Labor](../wo-work-orders/help-content.md#wo-k-k-edit-posted-dc-labor)
instead.

### Multi-WO gotcha (revisited)

See [Design model § Multi-WO policy](#multi-wo-clocking-policy). When
multi-WO is on, a single sequence-session can produce multiple
records. Parts produced only appear on the **last** record — keep
this in mind when editing.

### Operation

Date-range filter on the opening screen → transaction list → Edit
(modify + save) or Delete.

---

## DC-H Post Labor Transactions

*Source: [dc-h_post_labor_transactions.htm](../../../samples/chm/extracted/dc-h_post_labor_transactions.htm)*

Batch-post unposted DC transactions to the permanent WO files
(`WOLABOR` etc., from
[file-names-index](../../04-data-dictionary/file-names-index.md#work-orders)).

**Filters:** employee range, WO range, time range, date range. Enter
through all = post everything. **Tip:** filter by time / date so you
don't post records saved in the last few minutes that haven't been
reviewed yet in [DC-D](#dc-d-print-labor-status).

### Backflush-by-sequence support

Identical to [WO-N Post Labor Batches](../wo-work-orders/help-content.md#wo-n-post-labor-batches)
— BOM components tied to routing sequences get auto-issued to the
WO when the sequence is posted. **Lot- and serial-required
components are skipped** and listed on a discrepancy report; the
shop has to manually issue those via
[WO-G Issue Materials](../wo-work-orders/help-content.md#wo-g--issue-materials).

### Frequency choice

- Daily batch → lag between shop and reports, but review opportunity.
- Multiple-times-a-day batch → shorter lag.
- Real-time posting (flag in [SD-F](../../../samples/chm/extracted/sd-f_data_collection_defaults.htm))
  → zero lag; corrections done through [WO-K-K](../wo-work-orders/help-content.md#wo-k-k-edit-posted-dc-labor).

---

## DC-I Work Order Inquiry

*Source: [dc-i_work_order_inquiry.htm](../../../samples/chm/extracted/dc-i_work_order_inquiry.htm)*

Read-only, non-locking clone of
[WO-A Enter Work Orders](../wo-work-orders/help-content.md#wo-a--enter-work-orders).
Use this instead of WO-A for inquiry — WO-A locks records, which can
block [DC-H](#dc-h-post-labor-transactions) and other processing.

Buttons on the screen surface labor / materials / outside-processing
status panes without leaving the inquiry.

---

## DC-K Archive or Purge Shift Records

*Source: [dc-k_archive_or_purge_shift_re.htm](../../../samples/chm/extracted/dc-k_archive_or_purge_shift_re.htm)*

Archive / purge / **restore** Shift Start/Stop records from the
unposted labor file.

**Inputs:** action (archive / purge / restore) + date range + shift
+ employee number.

---

## DC-L Shift Clock In / Out

*Source: [dc-l_shift_clock_in_out.htm](../../../samples/chm/extracted/dc-l_shift_clock_in_out.htm)*

Per-employee shift-clock UI — **time-clock only**, no WO needed. For
payroll-accurate shift tracking when there's no productive WO to
clock into.

### Operation

Employee enters number + password. Screen displays:
- Current status (in / out).
- Period-to-date hours.
- Available vacation + sick time.

Single button toggles clock-in ↔ clock-out.

### vs DC-A shift start

[DC-A](#dc-a-enter-labor--production) can also start the shift (via
its dedicated button) when Employee Shift Start/Stop is enabled.
DC-L is the lighter-weight, standalone alternative for sites where
DC-A isn't running as a public terminal.

---

## DC-M Employee Dashboard

*Source: [dc-m_employee_dashboard.htm](../../../samples/chm/extracted/dc-m_employee_dashboard.htm)*

One-screen status board: who's clocked in right now, and for those
who aren't, when they last clocked out. Purely informational.

---

## DC-N Enter Holiday Shift Records

*Source: [dc-n_enter_holiday_shift_recor.htm](../../../samples/chm/extracted/dc-n_enter_holiday_shift_recor.htm)*

Bulk-generate **future** holiday shift records driven by the
Holiday list in
[SM-H Enter Shop Calendar](../../../samples/chm/extracted/sm-h_enter_shop_calendar.htm).

**Inputs:** employee range, how-far-in-future, hours-per-day to
generate.

Removes the need to manually create a holiday shift record per
employee per holiday — the shop calendar's holiday definitions drive
the generation.

---

## Cross-references

### Data tables

Per
[file-names-index · Data Collection](../../04-data-dictionary/file-names-index.md#data-collection):

| Table | Purpose |
|---|---|
| `BKDCPLAB` | Unposted DC labor transactions (edited by DC-G, posted by DC-H) |
| `BKDCLAB` | Posted DC labor transactions |
| `BKDCSHFT` | DC shifts |
| `BKDCHLAB` | Archived DC labor (per [file-names-index · Work Orders](../../04-data-dictionary/file-names-index.md#work-orders)) |

### Related LearnEVO modules

- [WO — Work Orders](../wo-work-orders/README.md) —
  [help-content](../wo-work-orders/help-content.md). DC posts into
  `WOLABOR`; [WO-F](../wo-work-orders/help-content.md#wo-f--enter-labor)
  is the non-DC alternative;
  [WO-K-K](../wo-work-orders/help-content.md#wo-k-k-edit-posted-dc-labor)
  is where posted DC transactions get edited.
- [SH — Scheduling](../sh-shipping/README.md) —
  [help-content](../sh-shipping/help-content.md).
  [SH-K View Work Center Load](../sh-shipping/help-content.md#sh-k-view-work-center-load)
  depends on real-time DC data for the "currently running" pane.
- [JC — Job Costing](../jc-job-costing/README.md) —
  [help-content](../jc-job-costing/help-content.md). Every JC report
  that cites labor / overhead derives from data entered here.
- [PR — Payroll](../pr-payroll/README.md). Shift data from DC flows
  to [PR-K Print/Post Time Cards](../../../samples/chm/extracted/pr-k_print_post_time_cards.htm)
  via [DC-D](#dc-d-print-labor-status)'s shift-only / CSV export.

### Related CHM overview sections

- [System Overview § Sequence of Events — Work Orders](../../00-overview/system-overview.md#7c-work-orders)
  — DC as the alternative to the WO-F / WO-M labor-entry path.
- [System Overview § Archiving](../../00-overview/system-overview.md#10-archiving-or-purging-old-data)
  — DC shift records are archived through this module via DC-K and
  the posted-labor file via SM-J-H.
