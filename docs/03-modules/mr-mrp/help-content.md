# Material Requirements (MRP) — Vendor Help Content

Status: verified (summarized from the vendor's help file).

Source CHM: `\\i2s109-solidcrm\DBAMFG$\EVOHELP.CHM` →
[samples/chm/EvoHELP.CHM](../../../samples/chm/EvoHELP.CHM) →
decompiled to [samples/chm/extracted/](../../../samples/chm/extracted/).
Extracted via [scripts/chm_to_md.py](../../../scripts/chm_to_md.py).

This doc consolidates the **14 help topics** under the CHM's
*Manufacturing → Material Requirements* category (overview + MR-A
through MR-N — 13 programs, no MR-M). Each program gets its purpose,
key inputs / behaviors, and cross-links. The full verbatim source is
one click away via the `Source:` link on each section.

For the companion schema + menu + form view of this module, see
[README.md](README.md) in this folder.

---

## Contents

- [Overview — what MRP does](#overview--what-mrp-does)
- [Core concepts — buffers, sensitivity, action messages](#core-concepts--buffers-sensitivity-action-messages)

**Forecasts**
- [MR-A Enter Forecast](#mr-a-enter-forecast)
- [MR-B Print Forecast](#mr-b-print-forecast)
- [MR-C Reset Forecast](#mr-c-reset-forecast)

**Parameters**
- [MR-D Enter MRP Parameters](#mr-d-enter-mrp-parameters)
- [MR-E Print MRP Parameters](#mr-e-print-mrp-parameters)

**The MRP run**
- [MR-F Generate Material Requirements](#mr-f-generate-material-requirements)

**Reports**
- [MR-G Print Material Requirements](#mr-g-print-material-requirements)
- [MR-H Print Order Action Report](#mr-h-print-order-action-report)
- [MR-L Print Planned Orders Report](#mr-l-print-planned-orders-report)

**Conversion to live orders**
- [MR-I Generate Work Orders](#mr-i-generate-work-orders)
- [MR-J Generate Purchase Orders](#mr-j-generate-purchase-orders)
- [MR-K Generate RFQs](#mr-k-generate-rfqs)
- [MR-N Apply Delay Action to POs](#mr-n-apply-delay-action-to-pos)

---

## Overview — what MRP does

*Source: [material_requirements.htm](../../../samples/chm/extracted/material_requirements.htm)*

MRP plans purchasing and production to fit shipping schedules and
stocking levels — making sure materials + subassemblies are
available all the way down the BOM.

### Inputs → Outputs

**Demand side inputs:**
- **Forecasts** of finished-good demand ([MR-A](#mr-a-enter-forecast)).
- **Sales orders** (actual customer demand).
- **Work-order BOMs** (existing allocations).

**Supply side data:**
- Existing **purchase orders**.
- Existing **work orders**.
- Current **on-hand inventory**.

**Outputs from [MR-F](#mr-f-generate-material-requirements):**
- **MAKE** — suggested (planned) work orders.
- **BUY** — suggested purchase orders.
- **EXPEDITE / DELAY / REVIEW** action messages on existing orders.

### The "MRP explosion"

When a planned WO gets suggested, its BOM creates **new demand** for
the next level of components → more planned WOs and POs → down
through every level of the BOM. Start dates back off by each level's
lead time.

### Integration

- **[Scheduling (SH)](../../../samples/chm/extracted/scheduling.htm)**
  translates the MRP plan into work-center schedules vs capacity.
- **[MR-I](#mr-i-generate-work-orders) / [MR-J](#mr-j-generate-purchase-orders) / [MR-K](#mr-k-generate-rfqs)**
  convert planned orders into live ones with no manual re-entry.

---

## Core concepts — buffers, sensitivity, action messages

These come up across MR-D, MR-G, and MR-H. Hoisting them once keeps
per-program sections short.

### Per-item MRP parameters ([MR-D](#mr-d-enter-mrp-parameters))

| Parameter | What it controls |
|---|---|
| **Include in MRP Generation?** | `N` → item is skipped entirely. Good for bulk items like rivets/oil/labels bought in bulk. |
| **Reorder Level** | Safety-stock minimum on-hand. MRP suggests orders to maintain it. Set to `0` if you only want to order on demand. |
| **Reorder Amount** | Minimum order quantity when MRP suggests an order. Set to `0` to order exactly what's needed. |
| **Lead Time** | Manufactured: days to run the WO start-to-finish. Purchased: days from vendor order to receipt. MRP uses this to back-date WO start dates / PO order dates. |
| **Planner Code** | Filter key so each planner can run reports for their own items. |
| **Round to whole number?** | For items that physically can't be fractional (e.g. sheet steel). |

### Buffers vs Sensitivity — the two-knob filter

For **both** late (Expedite) and early (Delay) arrivals there are
two knobs:

1. **Buffer** — defines the window within which an arriving order is
   assumed to be "pegged to" (fulfilling) the current requirement
   rather than a future one.
2. **Sensitivity** — defines the number of days of slip that are
   tolerable before the action message even shows up on reports.

**EXPEDITE scenario.** Requirement on March 1, Expedite Buffer = 20
days:
- PO arrives March 19 → **inside buffer** → treated as fulfilling
  the March 1 requirement, just late → **EXPEDITE** message.
- PO arrives March 21 → **outside buffer** → assumed to be for some
  later requirement → **BUY** message generated to cover March 1.

**DELAY scenario.** Same idea, in reverse, for early arrivals. Order
inside the Delay Buffer prior to a requirement → **DELAY**. Order
earlier than the Delay Buffer → **REVIEW** (no known requirement).

**Sensitivity** suppresses messages below the tolerable-slip
threshold. Expedite Sensitivity = 10 → a 9-day-late arrival doesn't
bother you.

**Vendor guidance:** start at 30–60 days on both buffers; tune from
experience. Longer buffer = fewer planned orders. Shorter Delay
Buffer = more REVIEW messages.

### Action messages (from MR-G / MR-H)

| Action | Meaning |
|---|---|
| **MAKE** | Suggested (planned) work order. |
| **BUY** | Suggested purchase order. |
| **EXPEDITE** | Existing order sufficient in qty but arrives late and **within the Expedite Buffer** of the requirement — pull it in. |
| **DELAY** | Existing order arriving earlier than needed, **within the Delay Buffer** — push it out. |
| **REVIEW** | Order arrives earlier than the Delay Buffer — not pegged to any known requirement. Often means a prior EXPEDITE was too late and MAKE/BUY got suggested in its place, leaving the original order orphaned. |
| **NONE** | Order qty + requirement fall on the same date. |

### Planned-order identifiers

Regenerated **from scratch** every MR-F run:
- **Planned work orders** — `PL` + up to 5-digit sequential number.
- **Planned purchase orders** — shown as `BUY` in the Order No column.

The `PL` number is a short-lived planning handle — don't depend on
it between MR-F runs.

### "Pegged to" column logic

| What appears | Meaning |
|---|---|
| WO-shaped number (prefix + suffix) | Existing WO BOM is allocating this component. |
| Single number without suffix | Sales order. |
| `FORECAST` | Forecast requirement. |
| `PL` + number | Planned (not-yet-live) WO. Lots of these = MR-F hasn't generated yet; run [MR-I](#mr-i-generate-work-orders) to convert. |

---

## MR-A Enter Forecast

*Source: [mr-a_enter_forecast.htm](../../../samples/chm/extracted/mr-a_enter_forecast.htm)*

Forecasts are future demand without firm sales orders. MRP treats
them the same as sales orders.

### Key points

- **Unlimited entries per item** as far into the future as you want
  — most users enter one per month per finished good.
- **No calculation is done by the program** — you develop forecasts
  externally. [SA-M Print User-Defined Detail](../../../samples/chm/extracted/sa-m_print_user_defined_detail.htm)
  is the vendor-recommended tool for building a historical file you
  can import.
- Typically entered on **finished goods only**; MRP generates the
  component demand automatically.
- Each entry = **item + qty + due date**. Due date is the MRP target
  for completion.

### Import path

Comma-delimited or fixed-length ASCII file with three columns:
**Item / Date / Quantity**. Date **must** be `YYYYMMDD` (ISO).

> In Excel: Format → Cells → Custom → type `YYYYMMDD` → OK.

---

## MR-B Print Forecast

*Source: [mr-b_print_forecast.htm](../../../samples/chm/extracted/mr-b_print_forecast.htm)*

Listing of current forecasts. Filters: item range, inventory types
(F/A/M/R), category, item class, date range. Output: screen /
printer / file.

---

## MR-C Reset Forecast

*Source: [mr-c_reset_forecast.htm](../../../samples/chm/extracted/mr-c_reset_forecast.htm)*

Three **mutually exclusive** maintenance actions — pick one per run:

| Action | What it does |
|---|---|
| **Consume** | Deducts actual sales / shipments from the forecast (within a date range) so requirements aren't double-counted. |
| **Erase** | Deletes forecasts within a date range. Typical monthly pattern: erase the earliest month, append a new far-future month. |
| **Rollover** | Moves every forecast date forward **one month**. Useful for stable / non-seasonal forecasts. No date range — it's all-or-nothing. |

---

## MR-D Enter MRP Parameters

*Source: [mr-d_enter_mrp_parameters.htm](../../../samples/chm/extracted/mr-d_enter_mrp_parameters.htm)*

Per-item MRP tuning. See [Core concepts](#core-concepts--buffers-sensitivity-action-messages)
above for what each parameter does.

### Defaults + backfill

- New parameters come from [SD-D Material Requirements Defaults](../../../samples/chm/extracted/sd-d_material_requirements_defaults.htm)
  when items are created in [IN-B](../../../samples/chm/extracted/in-b_enter_inventory.htm).
- **Existing items do NOT get retroactive defaults.** You have to
  edit them (single-item mode or range mode).

### Two entry modes

**Single item** — standard F2 lookup, F8/Next button walks through
item numbers sequentially without re-entering.

**Range** — two-screen flow:
1. Select range: item / category / class / planner code + inventory
   type filter.
2. Parameter screen with a **Change?** flag per field — `N` leaves
   untouched.

**Range-mode trick for Reorder Level / Reorder Amount:** enter
**`C`** instead of a value → you're prompted for months-of-usage →
program takes the **last 365 days' usage**, divides by 12, and
multiplies by the months specified. Useful for resetting reorder
points from actual usage.

### Access angle

Same fields are editable in [IN-B](../../../samples/chm/extracted/in-b_enter_inventory.htm),
but MR-D lets a planner edit parameters **without** rights to
create new part numbers.

---

## MR-E Print MRP Parameters

*Source: [mr-e_print_mrp_parameters.htm](../../../samples/chm/extracted/mr-e_print_mrp_parameters.htm)*

Listing of items + their MRP parameters, sorted by item. Filters:
item, inventory type (F/A/M/R), category, item class.

Final flag: `Print MRP Parts only?` — limits to items with
`Include in MRP Generation? = Y`.

---

## MR-F Generate Material Requirements

*Source: [mr-f_generate_mrp_requirements.htm](../../../samples/chm/extracted/mr-f_generate_mrp_requirements.htm)*

**The heart of the module.** Builds the whole MRP plan from scratch.
Can take **hours** to run — the vendor recommends off-hours.

### Phases (shown to the user as status messages)

1. Initialize MRP files.
2. Reset MRP flags.
3. Scan **sales orders**.
4. Scan **purchase orders**.
5. Scan **work orders**.
6. Scan **work-order BOMs**.
7. Scan **forecasts**.
8. Generate MRP — the explosion, top-down through every BOM level.

ESC / Exit aborts mid-run.

### Scope controls (all optional, all reduce run time)

- **Include forecasts?** Y/N.
- **Include sales orders?** Y/N, plus an optional `Estimated Ship
  Date` cutoff to ignore far-future SOs.
- **Include S-type (scheduled) WOs?** Y/N.
- **Inventory type toggles** — R/F/A/M always included; N/L/T
  optional.
- **Locations** — one or many.

### Performance guidance

> "If you have not set up any reorder levels or reorder amounts on
> your inventory items, many more MRP records will be created as the
> program responds to each individual requirement."

Good defaults for job shops that buy to order; bad for make-to-stock
or shops with common raw materials across products — set reorder
level / amount on those items to shrink the output.

### Frequency

Depends on how fast demand changes — some shops daily, some weekly.
The whole thing is regenerated each time.

---

## MR-G Print Material Requirements

*Source: [mr-g_print_material_requirements.htm](../../../samples/chm/extracted/mr-g_print_material_requirements.htm)*

**Time-phased inventory projection per item.** The main MRP inquiry
screen — can be huge if printed for the entire inventory.

### The running-on-hand pattern

Every row = one transaction (SO / forecast / WO / WO-allocation / PO
/ planned WO / planned PO) in date order, with a running projected
on-hand balance. Demand rows (negative quantities) reduce; supply
rows increase.

### Column semantics

- **Req Date** — source-specific: SO's estimated ship date, PO
  receiving due date, WO finish date, WO-allocation start date,
  forecast due date.
- **Quantity** — the transaction's quantity (combined ship +
  backorder for SOs).
- **On-Hand** — projected running balance.
- **Pegged to** — the transaction driving demand (see
  [Core concepts](#core-concepts--buffers-sensitivity-action-messages)).
- **Prod Code** — parent item for the pegged-to record.
- **Order No** — supply side: real WO (prefix + suffix), real PO
  (single number), planned PO (`BUY`), or planned WO (`PL` + number).
- **St Date** — scheduled/suggested start date for WOs; order date
  for POs.
- **Action** — MAKE / BUY / EXPEDITE / DELAY / REVIEW / NONE.

### Filters

- **BOM-wide option:** `Print BOM Components? = Y` + one top-level
  item → traverses the assembly and prints requirements for every
  component.
- Otherwise: item range, date range, inventory type, category,
  class, primary vendor.
- `New page for each Item number?` controls page breaks.

### When to use this vs MR-H

> "If you wish to identify MAKE, BUY, EXPEDITE, and DELAY actions to
> be performed, an alternative to this report is [MR-H Print Order
> Action Report](#mr-h-print-order-action-report), which is limited
> strictly to MRP transactions with action messages."

Use MR-G as **single-item inquiry on screen**; use MR-H as the
actionable worklist.

---

## MR-H Print Order Action Report

*Source: [mr-h_print_order_action_report.htm](../../../samples/chm/extracted/mr-h_print_order_action_report.htm)*

**The actionable worklist.** Everything that needs a human decision
(MAKE / BUY / EXPEDITE / DELAY / REVIEW) plus what drove each.

### Action filter flags

- **M** = Make, **B** = Buy, **E** = Expedite, **D** = Delay.
  Blank = all.
- (REVIEW always appears alongside D.)

### Column semantics (specific to this report)

- **Start Dt** — existing WO scheduled start / planned WO suggested
  start / existing PO order date / planned PO suggested order date.
- **Due Dt** — existing WO finish / planned WO suggested finish /
  existing PO receiving due date / planned PO suggested receipt.
- **Vendor** — existing PO vendor OR item's **primary vendor** for
  planned POs.
- **Req Dt + Quantity** — the pegged-to item's date + quantity (what
  created the demand).

### Filters

BOM-wide option same as MR-G. Also: item, start date, finish date,
class, category, **vendor range** (useful for batching purchases).

---

## MR-I Generate Work Orders

*Source: [mr-i_generate_work_orders.htm](../../../samples/chm/extracted/mr-i_generate_work_orders.htm)*

Convert planned WOs to real ones.

### Filters

Item, start date, finish date, item class, category. Location target
(for multi-plant).

### Two conversion modes

- **A — Automatic** — batch-create with MRP-suggested qty / start /
  finish, no review.
- **R — Review** — pop-up per suggested WO; edit start, finish, qty.
  Set qty to **0** to skip one. Enter through accepted fields to
  proceed to the next.

---

## MR-J Generate Purchase Orders

*Source: [mr-j_generate_purchase_orders.htm](../../../samples/chm/extracted/mr-j_generate_purchase_orders.htm)*

Convert planned POs to real ones. **The most complex conversion
program in MRP** — requires planning around **batching by lead time**.

### The batching problem

POs can have **multiple line items per vendor**, but within a run
this program **groups everything into one PO per vendor** and gives
them **one shared due date** — overriding the per-item MRP
requirement dates. Therefore: select items for each run by tight
date windows.

### The lead-time batching pattern (vendor's worked example)

Goal: order everything needed between **Feb 1 and Feb 8**.

| Run | Lead time | MRP Start Date range | MRP Due Date range | PO Date Default | Due Date Default |
|---|---|---|---|---|---|
| 1 | 4 weeks | 12/28 – 1/3 | 2/1 – 2/8 | 12/28 | 2/1 |
| 2 | 3 weeks | 1/4 – 1/11 | 2/1 – 2/8 | 1/4 | 2/1 |
| 3 | 2 weeks | (the 2-week window) | 2/1 – 2/8 | (PO send date) | 2/1 |
| 4 | 1 week | (the 1-week window) | 2/1 – 2/8 | (PO send date) | 2/1 |

The pattern: keep **Due Date Default = earliest requirement date in
the window** so nothing arrives late, step the **Start Date range**
back by lead-time tier, step the **PO Date Default** to the send
date for each tier.

**Not for scheduled / blanket orders** — those should be entered
manually in [PO-A](../po-purchase-orders/help-content.md#po-a-enter-purchase-orders).

### Report-only mode

`Generate a Report Only? = Y` → produces the suggested-PO list
**without creating POs**. Useful for evaluating different batching
schemes.

### Review mode

Per-item pop-up showing MRP start date + MRP requirement date side
by side with the PO Date / Due Date defaults. Editable: qty,
**vendor** (override the primary-vendor suggestion here — that's
often why you'd use review mode).

### Rounding to Standard Pack

If the default is set in [SD-D Material Requirements Defaults](../../../samples/chm/extracted/sd-d_material_requirements_defaults.htm),
qtys round up to the next `Standard Pack` increment from
[IN-B](../../../samples/chm/extracted/in-b_enter_inventory.htm).

---

## MR-K Generate RFQs

*Source: [mr-k_generare_rfqs.htm](../../../samples/chm/extracted/mr-k_generare_rfqs.htm)*

Same engine as [MR-J](#mr-j-generate-purchase-orders), but produces
**RFQs instead of POs** and can fan out **multiple RFQs per item**
to different vendors.

### The multi-vendor loop

After generating one RFQ, the screen reopens with vendor #2 (from
[IN-B](../../../samples/chm/extracted/in-b_enter_inventory.htm))
prefilled and asks `Generate same RFQ for another Vendor?`. Answer
Y → generates #2 → prompts again with vendor #3 → repeat as needed.

RFQs feed [PO-G Convert RFQs](../po-purchase-orders/help-content.md#po-g-convert-rfqs).

---

## MR-L Print Planned Orders Report

*Source: [mr-l_print_planned_orders_report.htm](../../../samples/chm/extracted/mr-l_print_planned_orders_report.htm)*

Tracks the **dependency chain** around planned orders — what drove a
planned order and what further demand it creates.

**Single PL-number mode** — enter a `PL` number, see all requirements
generated below it. **`Reverse Lookup? = Y`** shows the chain **above**
the planned order (what drove it). Run both to see the full chain.

**All mode** — blank PL-number → reports every planned order.

Since `PL` numbers are regenerated every [MR-F](#mr-f-generate-material-requirements)
run, the screen displays the currently valid range.

---

## MR-N Apply Delay Action to POs

*Source: [mr-n_apply_delay_action_to_pos.htm](../../../samples/chm/extracted/mr-n_apply_delay_action_to_pos.htm)*

**Automated execution of DELAY actions** on PO Estimated Receipt
Dates, for PO lines above a minimum dollar value.

### Inputs

- Vendor code range.
- Minimum PO line value threshold.

### Behavior

Every PO line with a **DELAY action** over the value threshold gets
its **Estimated Receipt Date** changed to the MRP recommended date —
same field that [PO-Q Maintain PO Delivery Dates](../po-purchase-orders/help-content.md#po-q-maintain-po-delivery-dates)
edits manually, and same field MRP uses going forward. The
**Original Promise Date** stays untouched, so vendor on-time
performance is still judged against the vendor's original commitment.

---

## Cross-references

### Data tables this module writes / reads

Per
[file-names-index · Material Requirements](../../04-data-dictionary/file-names-index.md#material-requirements):

| Table | Purpose |
|---|---|
| `MTMRP` | MRP master (output of MR-F) |
| `SUMPNCUS` | MRP temp file |
| `BKMRPPO` | MRP-to-PO conversion (temporary — used by MR-J/MR-K) |
| `BKMRPSW` | Temp file used by MRP |

Input data comes from WO (`WORKORD`, `WOBOM`), PO (`BKAPPO`,
`BKAPPOL`), SO (`BKARINV`, `BKARINVL`), inventory (`BKICMSTR`), and
forecasts (unnamed dedicated table).

### Related modules (LearnEVO)

- [WO — Work Orders](../wo-work-orders/README.md) — [help-content](../wo-work-orders/help-content.md).
  [MR-I](#mr-i-generate-work-orders) writes into `WORKORD`; WO BOM is a
  source of demand for MR-F.
- [PO — Purchase Orders](../po-purchase-orders/README.md) — [help-content](../po-purchase-orders/help-content.md).
  [MR-J](#mr-j-generate-purchase-orders) writes into `BKAPPO` / `BKAPPOL`;
  existing POs are a source of supply for MR-F.
- [SO — Sales Orders](../so-sales-orders/README.md) — primary source
  of real demand.
- [IN — Inventory](../in-inventory/README.md) — on-hand starting
  point; reorder level / amount / lead time live on the inventory
  record.
- [BM — Bills of Material](../bm-bill-of-materials/README.md) —
  what gets "exploded" when planned WOs generate lower-level demand.
- [SH — Scheduling](../../../samples/chm/extracted/scheduling.htm) —
  consumes the MRP plan; [SH-N Generate Lead Times](../../../samples/chm/extracted/sh-n_generate_lead_times.htm)
  keeps manufacturing lead times honest in MR-D.

### Related CHM overview sections

- [System Overview § Sequence of Events — Manufacturing Planning](../../00-overview/system-overview.md#7a-manufacturing-planning)
  — where MR-A → MR-F → MR-H → MR-I/J/K sit in the big picture.
- [System Overview § Sequence of Events — Work Orders / Purchase Orders](../../00-overview/system-overview.md#7c-work-orders)
  — downstream of MRP.
