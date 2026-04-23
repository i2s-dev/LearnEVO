# Purchase Orders — Vendor Help Content

Status: verified (summarized from the vendor's help file).

Source CHM: `\\i2s109-solidcrm\DBAMFG$\EVOHELP.CHM` →
[samples/chm/EvoHELP.CHM](../../../samples/chm/EvoHELP.CHM) →
decompiled to [samples/chm/extracted/](../../../samples/chm/extracted/).
Extracted via [scripts/chm_to_md.py](../../../scripts/chm_to_md.py).

This doc consolidates the **27 help topics** under the CHM's
*Manufacturing → Purchase Orders* category (overview + PO-A through
PO-T, covering 26 programs). Each program gets its purpose, key
fields / behaviors, and cross-links. The full verbatim source is one
click away via the `Source:` link on each section.

For the companion schema + menu + form view of this module, see
[README.md](README.md) in this folder.

---

## Contents

- [Overview — what Purchase Orders does](#overview--what-purchase-orders-does)
- [Key concepts that recur across programs](#key-concepts-that-recur-across-programs)

**Life-cycle programs**
- [PO-A Enter Purchase Orders](#po-a-enter-purchase-orders)
- [PO-B Print Purchase Orders](#po-b-print-purchase-orders)
- [PO-C Receive Purchase Orders](#po-c-receive-purchase-orders)
- [PO-D View PO Receivers](#po-d-view-po-receivers)
- [PO-K Close Purchase Orders](#po-k-close-purchase-orders)

**RFQ system**
- [PO-E Enter / Print RFQs](#po-e-enter--print-rfqs)
- [PO-F Enter Verbal RFQs](#po-f-enter-verbal-rfqs)
- [PO-G Convert RFQs](#po-g-convert-rfqs)

**Vendor data**
- [PO-H Enter Vendor Prices](#po-h-enter-vendor-prices)
- [PO-L Assign Vendors to Items](#po-l-assign-vendors-to-items)
- [PO-P View Vendor Information](#po-p-view-vendor-information)

**PO-I-\* reports**
- [PO-I-A Print Open Purchase Orders Listing](#po-i-a-print-open-purchase-orders-listing)
- [PO-I-B Print Closed Purchase Orders Listing](#po-i-b-print-closed-purchase-orders-listing)
- [PO-I-C Print RFQ Status](#po-i-c-print-rfq-status)
- [PO-I-D Print Vendor Prices](#po-i-d-print-vendor-prices)
- [PO-I-E Print Receiving Report](#po-i-e-print-receiving-report)
- [PO-I-F Print Received not Invoiced](#po-i-f-print-received-not-invoiced)
- [PO-I-G Print Purch Order Items by Due Date](#po-i-g-print-purch-order-items-by-due-date)
- [PO-I-H Vendor Performance Report](#po-i-h-vendor-performance-report)

**QC inspection flow (PO-J-\*)**
- [PO-J-A Print Receipt Travelers](#po-j-a-print-receipt-travelers)
- [PO-J-B Print Inventory in QC](#po-j-b-print-inventory-in-qc)
- [PO-J-C Enter Inspection Buyoffs](#po-j-c-enter-inspection-buyoffs)

**Inquiry / scheduling / receiving slip / e-sign**
- [PO-M Purchase Order Inquiry](#po-m-purchase-order-inquiry)
- [PO-Q Maintain PO Delivery Dates](#po-q-maintain-po-delivery-dates)
- [PO-R Print Receiving Slip](#po-r-print-receiving-slip)
- [PO-T Digitally Sign Purchase Order](#po-t-digitally-sign-purchase-order)

---

## Overview — what Purchase Orders does

*Source: [purchase_orders.htm](../../../samples/chm/extracted/purchase_orders.htm)*

The PO module covers: entering / editing / deleting / reviewing
purchase orders, recording receipts (including partial receipts),
printing POs (preprinted forms, plain paper, or PDF-by-email). It's
**fully integrated** with Work Orders, Job Costing, Lot Control,
Serial Control, and (through AP-C) Accounts Payable.

### Two document types from the same screen

- **Type P — Purchase Order** for **tangible items**.
- **Type S — Service Order** for **services** like plating, painting.
  Type S lines **must** carry a valid Work Order number + outside-
  processing sequence. Type S costs post to WIP, not inventory.

### The RFQ sub-system

Request-for-Quote is a separate numbering sequence that parallels PO
entry. Two styles exist:
- **[PO-E](#po-e-enter--print-rfqs)** — full multi-item RFQ, same UI
  as PO-A but prices are empty.
- **[PO-F](#po-f-enter-verbal-rfqs)** — one-off verbal RFQ for a
  single item / service; ties to an estimate or work order.

Either style feeds **[PO-G Convert RFQs](#po-g-convert-rfqs)** when
the quote is accepted.

### The QC-inspection side-path

`[PO-C]` can receive **to inventory** (default) or **to QC inspection**
— the latter holds the goods until they're bought off in
`[PO-J-C]`, at which point they transfer to inventory/WIP or get
rejected back to the vendor. Receipt travelers for QC are produced
by `[PO-J-A]`, and `[PO-J-B]` reports what's still in QC.

### Prerequisites to set up before using the module

Per the vendor:
1. **[SD-C Purchase Orders Defaults](../../../samples/chm/extracted/sd-c_purchase_order_defaults.htm)**
   — the behavior-control file for this whole module.
2. **[AP-A Enter Vendors](../../../samples/chm/extracted/ap-j_print_vendor_code_and_name.htm)**
   — or add vendors inline from PO-A.

---

## Key concepts that recur across programs

These four concepts show up in multiple programs; documenting them
once here so the per-program sections can stay short.

### 1. Make-From items (type M)

A **Make-From** is an item number that *is the result* of an outside
process applied to a raw part — e.g. a plated version of a raw part.
Defined as **type M** in [IN-B](../../../samples/chm/extracted/in-b_enter_inventory.htm)
with a BOM in [BM-A](../../../samples/chm/extracted/bm-a_ener_bills_of_material.htm)
consisting of the raw input(s).

**The trick:** Make-Froms are bought on **type P POs** (not Service
Orders), because they're items in their own right with their own
item number — not tied to a WO sequence.

When entered on a PO, the BOM components pull in as **negative-
quantity lines** → creates a negative On-PO, which signals MRP /
reorder report that those components are already committed and not
available for other uses. On receipt, the parent is received
positively and the components are deducted (reversing the negative
quantities); the Make-From picks up the component costs **plus** the
service fee (the PO price) as its inventory value.

**Location flexibility:** the Make-From's components can be assigned
to a **different Location** than the parent — so [IN-L-J Transfer
Inventory](../../../samples/chm/extracted/in-l-j_transfer_inventory.htm)
can transfer components to a **vendor location as consignment**, and
the Make-From receipt both deducts consigned components and
increases finished stock at the main warehouse in one transaction.

### 2. Phantom (type B) purchases

Buying a **type B phantom** on a PO = buying a single item and
receiving **multiple items** (the phantom's components) into stock.
On receipt, PO price for the phantom parent is distributed across
components proportionally by their standard cost.

### 3. Unit-of-measure codes and how they affect pricing

PO lines accept a **Purchase UM** that drives automatic price
arithmetic. Common codes (listable on-screen via F1):

| UM code | Calculation |
|---|---|
| `M` | `(PO qty / 1000) × PO price` — per thousand |
| `H` / `C` | `(PO qty / 100) × PO price` — per hundred |
| `LOT` | flat lot charge, regardless of qty |
| `LB` | qty × inventory `Weight` × PO price |
| `CWT` | qty × `Weight` / 100 × PO price |
| `SF` / `BF` / `LF` | qty × inventory `Foot Factor` × PO price |
| `MSF` / `MBF` / `MLF` | `.../ 1000` variants |
| `CLF` | `.../ 100` — linear feet |

**Conversion Factor** is separate from this — it converts the
**purchase UM to the stock UM** on receipt. Example from the vendor:
a reel of 5000 resistors is a PO of `1 REL @ $50` with conversion
`5000`; inventory receives `5000 EA @ $0.01`.

### 4. The seven ways a PO life cycle ends

1. **Full receipt** — PO closes automatically when fully received
   **AND** fully invoiced via [AP-C](../../../samples/chm/extracted/ap-c_enter_purchase_order_invoices.htm).
2. **Full receipt without AP** — auto-closes on full PO-C receipt.
3. **Manual close** via [PO-K](#po-k-close-purchase-orders) for
   cancellation or short-close.
4. **Direct-to-WO** — tangible PO lines with a WO # bypass inventory
   entirely; units / costs go straight to WIP via [PO-C](#po-c-receive-purchase-orders).
5. **Service order (type S)** — costs go to WIP; no inventory effect.
6. **QC-inspection path** — received items land in QC via [PO-C](#po-c-receive-purchase-orders),
   transferred to inventory/WIP (or rejected back to vendor) via
   [PO-J-C](#po-j-c-enter-inspection-buyoffs).
7. **Negative-qty receipt** — return to vendor; reverses inventory /
   WO / GL, puts items back on PO.

---

## PO-A Enter Purchase Orders

*Source: [po-a_enter_purchase_orders.htm](../../../samples/chm/extracted/po-a_enter_purchase_orders.htm)*

The big one — creating / editing POs and Service Orders.

### Header fields worth highlighting

- **PO No** — default sequence counter at
  [SD-R Assign Next Numbers](../../../samples/chm/extracted/sd-r_assign_next_numbers.htm).
  If you type your own, you're prompted to reset the counter — the
  vendor recommends accepting the auto-assigned number.
- **Vend Cd** — unknown code? Program jumps you to
  [AP-A Enter Vendors](../../../samples/chm/extracted/ap-j_print_vendor_code_and_name.htm)
  to add inline. **Alt-P** on blank vendor → enter item number, pulls
  in the item's primary vendor.
- **Type P vs S** — see the module overview above.
- **Ship To V/C** — direct-ship from vendor to another vendor or
  customer; blank = your IN-L-B location address.
- **Ord Desc** — prints on PO *and* on the vendor's check when the
  PO is invoiced/paid; blank falls back to PO-number cross-ref.
- **Ship Via / Terms Cd / FOB** — all default from the vendor master.
- **Taxable? + Tax Group + Tax Rate** — driven by
  [SD-C](../../../samples/chm/extracted/sd-c_purchase_order_defaults.htm)
  `Track PO taxes using Tax Groups?` flag. Tax Rate not overridable
  when using groups.
- **GL Dept** — header-level override; blank = fall back to each item
  class's department. Applied to **all GL postings** from the PO
  except PO/RNI, AP, cash (COD), and FX exchange postings.
- **Location** — must be a valid location.
- **Rework PO** — checkbox; filters on [PO-B](#po-b-print-purchase-orders)
  and [PO-I-G](#po-i-g-print-purch-order-items-by-due-date).
- **Import Lines** — green-circle button between header and lines;
  imports a CSV with item/description/quantity/price/receipt-date.
  Missing price & description fall back to item master + vendor price.

### Line-item fields worth highlighting

- **Comment-only lines** — blank Item, text in Description; no qty /
  price / dates asked for.
- **Due Date** — first line default = today + lead time (from
  vendor-price file, falling back to inventory lead time). Non-work
  days per [SM-H](../../../samples/chm/extracted/sm-h_enter_shop_calendar.htm)
  get skipped. Subsequent lines default to previous line's date;
  warning fires if today + lead > previous line's date.
- **Price** — for type P, defaults from vendor-price file then
  inventory Last Cost. For type S with no vendor price entered,
  price stays 0 until WO+seq entered, then offers the routing
  outside-processing cost.
- **UM + Conv. Fact.** — see [Key concepts §3](#3-unit-of-measure-codes-and-how-they-affect-pricing).
- **Work Order + Seq** — type P: optional (qty/cost bypasses
  inventory → WIP if set). Type S: **required**, and seq must be a
  valid outside-processing sequence.
- **GL Acct / GL Dept** — editable per-line only if SD-C's "edit GL
  Account/Dept by Item type" flag is Y and the line type matches.
- **Confirmed checkbox** — flag for price/delivery vendor-confirmed.
- **Promise Date** — defaults to Due Date; later editable in
  [PO-Q](#po-q-maintain-po-delivery-dates). Vendor-performance
  reports rate against the **original promise**.
- **ECO Info button** — active if [SD-H](../../../samples/chm/extracted/sd-h_inventory_defaults.htm)
  `Use ECO = Y`; lets you specify the revision level.

### Auto-inserted comment lines (in this order)

If an item has these records, they pull in as comment-only lines
immediately after the line:
1. Vendor-specific item number from [BM-K](../../../samples/chm/extracted/bm-k_enter_approved_vendors.htm).
2. Manufacturer + manufacturer's item number from [BM-L](../../../samples/chm/extracted/bm-l_enter_approved_manufacturers.htm).
3. Inventory Specifications (up to 12 lines) — prompted Y/N.
4. For type S: Routing Notes.

### Dupe / Insert / Notes / Copy

- **Dupe Line** — click after saving a line; repeats all the line's
  data (optionally including comments) so you just edit the due date.
  Classic use: **scheduled / blanket orders** (same item, multiple
  dates, each its own line).
- **Ins Line** — move the anchor line into the entry area, click
  Ins; everything below shifts down one.
- **Notes** — Notes button → free-form; also **Copy Notes** to pull
  notes from another PO (template pattern).
- **Copy PO** — on the opening list, highlight → Copy PO → prompts
  for PO# (blank = next sequential) and receipt date (blank = lead
  time on first line).

### Reversing a PO (credit/return)

Enter a **new PO** mirroring the original but with **negative line
quantities**. On receipt, the second PO reverses the first's ledger /
inventory / vendor activity. Also known as a **Credit PO**.

### Deleting an Existing PO

Opening list → highlight → Delete. **Not allowed** if:
- Any item is Received-Not-Invoiced.
- Any item is in QC.

### Approved vendors / manufacturers

This program honors approved-vendor and approved-manufacturer rules
per [How to Use Approved Vendors and Manufacturers](../../../samples/chm/extracted/how_to_use_approved_vendors_and_manufacturers.htm).

---

## PO-B Print Purchase Orders

*Source: [po-b_print_purchase_orders.htm](../../../samples/chm/extracted/po-b_print_purchase_orders.htm)*

Prints POs to preview / printer / email / file.

**Key behaviors:**
- **First print** is titled "Purchase Order"; subsequent prints are
  **"Original Purchase Order"** or **"Current Purchase Order"**
  (selected at print time).
- **Print all unprinted?** flag controls batch-print-the-queue.
- Options: include Make-From components / exclude zero-balance lines /
  print original vs remaining-to-receive amounts / include linked docs.
- Post-print prompt: **"Were they printed correctly?"** — the PO is
  only marked printed when you answer Y. Answering N preserves the
  unprinted flag for a reprint.

---

## PO-C Receive Purchase Orders

*Source: [po-c_receive_purchase_orders.htm](../../../samples/chm/extracted/po-c_receive_purchase_orders.htm)*

The **high-traffic** program for recording receipts.

### Receiving modes

| Line has WO? | Line is type S? | Effect |
|---|---|---|
| No | No | Adds to on-hand inventory. |
| Yes (type P) | — | Bypasses inventory → posts units + cost straight to WIP. |
| — | Yes (type S) | Bypasses on-hand and WIP qty; costs go to WIP against the WO's sequence. |

### Receive Into: I (Inventory) vs Q (QC)

Header-level choice that sets the default for all lines; **each line
can override**. QC-routed lines sit in QC until [PO-J-C](#po-j-c-enter-inspection-buyoffs)
buys them off.

### Full vs partial receipt

- **Receive All Lines? Y** — marks every line fully received with
  one click. Exceptions can be tweaked after by highlighting the
  line from the pop-up display.
- **Recv thru Due Date** — limits the "receive all" to lines up to
  that date (scheduled/blanket-order scenario).
- **Receive All Lines? N** — all lines default qty 0; highlight each
  line you want to receive.

### Unit Cost editability

Controlled by [SD-C](../../../samples/chm/extracted/sd-c_purchase_order_defaults.htm):
**no access / view only / editable**. When editable, changing the
price at receipt time updates the PO line in place.

### Over-receipts + returns

- **Over-receipt percentage** is set in SD-C. Beyond that → warning.
- **Negative qty** = return to vendor. Removes stock / WIP qty, puts
  items back on PO, reverses GL postings.

### Side-effects on the inventory file

A full receipt updates: on-hand, on-purchase-order, **average cost**,
**last cost**, **last receipt date**, **average days to receive**.
Location file gets its own on-hand / on-PO updates for the
designated location.

### Vendor-price auto-update

If `SD-C → update vendor prices on receipt` is set, the
[PO-H Enter Vendor Prices](#po-h-enter-vendor-prices) file for this
vendor+item also gets updated with the actual PO price.

### Multi-currency

Foreign-currency POs convert each line's cost from source currency
to **base currency** at the **closest historical exchange rate**
when posting to inventory/WIP. PO/RNI posts **in source currency**.
FX delta goes to the **F/E Transactions account** from [IM-C](../../../samples/chm/extracted/im-c_enter_currenct_exchange_rates.htm).

### Landed cost

**Customs Broker** field at receipt triggers brokerage fees from
[IM-F](../../../samples/chm/extracted/im-f_enter_landed_cost_customs_fees.htm).
Duty = vendor's duty code (AP-A) × item's duty code (IN-B). Both get
added to inventory cost **in base currency**.

### Reopening a closed PO

If `SD-C → allow reopen closed POs = Y`, reopen from
[PO-D](#po-d-view-po-receivers).

---

## PO-D View PO Receivers

*Source: [po-d_view_po_receivers.htm](../../../samples/chm/extracted/po-d_view_po_receivers.htm)*

Browse the receiver file + **reopen closed POs**.

- Opening list: sorted by PO, sub-sorted by date. Re-sortable by
  Vendor Code / Vendor Name / Job Number.
- Closed POs: last receipt marked **"C"**.
- **Reopen PO** button on the last receipt of a closed PO → moves it
  back to the open-PO file for [PO-A](#po-a-enter-purchase-orders)
  editing.
- **Copy PO** on a closed PO's last receipt → creates a new PO from
  it (open POs use Copy PO in PO-A instead).

---

## PO-E Enter / Print RFQs

*Source: [po-e_enter_print_rfqs.htm](../../../samples/chm/extracted/po-e_enter_print_rfqs.htm)*

Full-screen RFQ — **identical to PO-A except prices are omitted**.
Separate numbering sequence.

**Uses:**
- Standard quote request.
- **Template PO** — keep a stock RFQ of typical items; enter
  quantities only when you want to buy; convert via
  [PO-G](#po-g-convert-rfqs) so only the items-with-quantities
  become a live PO.

**Copy RFQ** — sends the same RFQ to a different vendor (new RFQ #).
Also copyable from the opening list (copies to same vendor).

Prints same way as POs (marked-printed state handled identically).

---

## PO-F Enter Verbal RFQs

*Source: [po-f_enter_verbal_rfqs.htm](../../../samples/chm/extracted/po-f_enter_verbal_rfqs.htm)*

Single-item (or single-service) verbal-RFQ form — alternative to the
full-screen PO-E. Intended for shops with lots of one-off vendor
quote calls.

### Estimating tie-in

- **Estimate No** field can tie an RFQ to an estimate.
- Multiple RFQs can target the same estimate; one can be flagged
  **Use in Est? = Y** (the program enforces "only one").
- The flagged RFQ's prices are what the estimate uses for cost calcs.

### Sequence field

If populated, the cursor skips the item-number block — services tied
to a routing operation don't need an item number.

### Open vs answered

- **Open** — no prices entered.
- **Answered / closed** — prices filled in.

### Quantity/Cost quantity-break grid

Five (qty, cost) pairs. `99, $10.00` + `199, $7.50` → $10 for qty 1-99,
$7.50 for 100-199.

### Exp Date

**Required.** Distinguishes current vs expired RFQs — no "never
expires" sentinel, so use a far-future date like `12/31/28`.

### Lookup helpers

- Standard F2 lookup on vendor / item / WO / estimate.
- **Home key** (or Display RFQs by Est button) → list all RFQs for
  the currently-referenced estimate.

Status tracking → [PO-I-C Print RFQ Status](#po-i-c-print-rfq-status).

---

## PO-G Convert RFQs

*Source: [po-g_convert_rfqs.htm](../../../samples/chm/extracted/po-g_convert_rfqs.htm)*

Turn an RFQ (PO-E or PO-F) into a live PO.

**Inputs:**
- Convert Quote Number.
- P/O Number (blank = next sequential).
- Order Date (default today).
- Estimated Receipt Date — **applies to every line**; different dates
  must be edited on the PO afterward.
- Work Order # (optional; only if not already on the RFQ).
- Transfer Notes? (Y/N).
- **Purge RFQ after convert?** — N leaves the RFQ on file (reusable
  template). Additional option: when acting as a template, convert
  **only items with quantities** and then **clear the quantities**
  — resets the template.

---

## PO-H Enter Vendor Prices

*Source: [po-h_enter_vendor_prices.htm](../../../samples/chm/extracted/po-h_enter_vendor_prices.htm)*

Per (item, vendor) pricing record — used automatically on PO entry.

### Fields

- **Item** + **Vendor** (key).
- **Purch UM / Conv Factor / Lead Time** — default from inventory
  master, overridable.
- **Expiration date** — **required**; use far-future date if there's
  no real expiry.
- **Quantity / Cost** — five quantity-break pairs. Quantities higher
  than the last break use the last break's cost.
- **Last Update** — auto-stamped on save.

### Editing the existing record (not creating a duplicate)

Naive flow — item + vendor entry — **creates a duplicate**. To edit
the existing record: from the Item Number field, **Alt-P** (or
Display Pricing button), select from the list that comes up. This is
a common gotcha.

Reporting: [PO-I-D Print Vendor Prices](#po-i-d-print-vendor-prices).

---

## PO-I-A Print Open Purchase Orders Listing

*Source: [po-i-a_print_open_purchase_orders_listing.htm](../../../samples/chm/extracted/po-i-a_print_open_purchase_orders_listing.htm)*

Listing of not-yet-closed POs. **Short form** or **Long form**.

- **Short form columns:** vendor name/code, PO #, item #, qty
  ordered / received to inventory / in QC, unit cost, UM, due date,
  WO + sequence, currency + subtotals.
- **Long form adds:** 2 description lines, Job #, PO type, PO
  description, ordered-by.

**Multi-currency option** — `Print in Base/Source Currency?` Base
converts via historical rates from the first receipt (or today if
never received).

**Filters:** sort (vendor / item / PO), from-thru ranges for vendor,
item, job #, PO #, order date, due date, detail-vs-summary.

---

## PO-I-B Print Closed Purchase Orders Listing

*Source: [po-i-b_print_closed_purchase_orders_listing.htm](../../../samples/chm/extracted/po-i-b_print_closed_purchase_orders_listing.htm)*

Closed-PO history. Alternative for purchasing-history questions:
[IN-E Print Inventory Transactions](../../../samples/chm/extracted/in-l-e_update_materoal_standard_costs.htm).

Same multi-currency option as PO-I-A. Sort by vendor / item / PO.
Filters: vendor, item, PO, date range, summary vs detail.

---

## PO-I-C Print RFQ Status

*Source: [po-i-c_print_rfq_status.htm](../../../samples/chm/extracted/po-i-c_print_rfq_status.htm)*

Open and answered RFQs. Columns: item, RFQ #, estimate #, WO #,
vendor, RFQ date, qtys, prices.

**"Open only?" flag** restricts to not-yet-priced RFQs — the queue
of "still waiting on the vendor to respond".

Filters: item, RFQ #, estimate #, WO #, vendor.

---

## PO-I-D Print Vendor Prices

*Source: [po-i-d_print_vendor_prices.htm](../../../samples/chm/extracted/po-i-d_print_vendor_prices.htm)*

Listing of [PO-H](#po-h-enter-vendor-prices) records.

**Key filter:** `Limit to expired prices only?` — produces a cleanup
worklist for the vendor-price file.

---

## PO-I-E Print Receiving Report

*Source: [po-i-e_print_receiving_report.htm](../../../samples/chm/extracted/po-i-e_print_receiving_report.htm)*

Receipts for a day / date range. Used by the receiving clerk to
route incoming goods to the open WOs that need them.

**Key feature:** when sorted **by item**, the report can include
**open allocations** (WOs waiting on each item). Allocations can be
filtered to WOs within a start-date range to exclude far-future WOs.

**Filters:** sort (item / vendor / PO), date range, PO #, vendor,
Ship To, item, job, WO, due date, entered-by, received date,
purchase / service / both.

**Vendor-order variant:** select `T6POIE1V.RTM` as the print format →
one summary line per vendor.

Multi-currency base/source option as elsewhere.

---

## PO-I-F Print Received not Invoiced

*Source: [po-i-f_print_received_not_invoiced.htm](../../../samples/chm/extracted/po-i-f_print_received_not_invoiced.htm)*

**The control report for the PO/RNI GL account.**

> The report should reconcile to the PO's Received not Invoiced GL
> account. It **does not include items in QC** — combine with
> [PO-J-B Print Inventory in QC](#po-j-b-print-inventory-in-qc) for
> GL reconciliation.

### Multi-currency caveats

- PO/RNI per currency is maintained in **source currency**.
- Running in source + including multiple currencies → the grand
  total is meaningless.
- Running in **base** for reconciliation: first run the **Convert to
  Base Currency routine** in [IM-B](../../../samples/chm/extracted/im-b_enter_multiple_currencies.htm)
  so the source-currency PORNI accounts reflect current exchange rates.

### As-of-prior-date logic

Leave all filters blank except received date `0/0/00` through
as-of-date. Report has two parts:
1. PO RNI items with subtotals + grand total.
2. **Price changes** from [AP-C](../../../samples/chm/extracted/ap-c_enter_purchase_order_invoices.htm)
   for items that were uninvoiced on the as-of date but have since
   been invoiced. The net PO/RNI backs these out to arrive at a true
   backdated balance.

### Underlying filter logic (for anyone querying the data directly)

A PO line is included if **`BKAP.POL.ARD ≤ as-of`** AND either
**`BKAP.POL.INVNM` is empty** OR **`BKAP.POL.PSTDTE > as-of`** (i.e.
invoice existed later but hadn't been posted yet as of the as-of date).

This report is part of the
[System Overview § Month End Accounting](../../00-overview/system-overview.md#9-month-end-accounting--detail)
checklist.

---

## PO-I-G Print Purch Order Items by Due Date

*Source: [po-i-g_print_purch_order_items.htm](../../../samples/chm/extracted/po-i-g_print_purch_order_items.htm)*

Projected PO receipts in due-date order. Alternate sorts: item,
vendor, promise-date.

**Filters:** item, PO, due date, Rework-PO flag, vendor-copy toggle,
WO priority (when lines are tied to work orders).

---

## PO-I-H Vendor Performance Report

*Source: [po-i-h_vendor_performance_report.htm](../../../samples/chm/extracted/po-i-h_vendor_performance_report.htm)*

On-time-delivery rating per vendor.

### Inputs

- **Receipt-date range** — basis of the rating.
- **Actual vs Estimated dates** within the range.
- **On-Time Window** — days early + days late that still count as
  on-time.
- **Vendor Code** / **Vendor Class** ranges.
- **Skip POs entered before <date>** — performance knob for speed
  (skips old data instead of scanning it).
- **Save rating to vendor history file?** — only available if a Rep
  Code is set in [SD-C](../../../samples/chm/extracted/sd-c_purchase_order_defaults.htm).
- **Summary vs line-item detail.**

### Three rating methods (one or more)

- On-time % by **number of lines received**.
- On-time % by **number of items received**.
- On-time % by **dollar value received**.

**Important:** rating is always against the **original Promise Date**,
not the edited Due Date — that's why [PO-Q](#po-q-maintain-po-delivery-dates)
intentionally preserves the original.

---

## PO-J-A Print Receipt Travelers

*Source: [po-j-a_print_receipt_travelers.htm](../../../samples/chm/extracted/po-j-a_print_receipt_travelers.htm)*

Print a QC traveler per **line item** that came in with "Receive
Into = Q" in [PO-C](#po-c-receive-purchase-orders). Receipt travelers
get a unique auto-assigned identifying number at receipt time.

Used by QC to mark accepted / rejected / remarks; then fed into
[PO-J-C](#po-j-c-enter-inspection-buyoffs).

**Filters:** receiver # range, receipt date range, PO # range.
`Print PO comment lines after line items on a receiver?` — Y prints
all the line's comment lines for reference.

---

## PO-J-B Print Inventory in QC

*Source: [po-j-b_printinventory_in_qc.htm](../../../samples/chm/extracted/po-j-b_printinventory_in_qc.htm)*

Listing of line items in QC that haven't been bought off yet.
Sort by vendor / item / PO; filter by vendor, item, job, PO, order
date. **Can run as of a prior date** — for month-end reconciliation.

**Critical tie-in:** **PO/RNI GL reconciliation = [PO-I-F](#po-i-f-print-received-not-invoiced) total + PO-J-B total.** See
[System Overview § Month End Accounting](../../00-overview/system-overview.md#9-month-end-accounting--detail).

---

## PO-J-C Enter Inspection Buyoffs

*Source: [po-j-c_enter_inspection_buyoffs.htm](../../../samples/chm/extracted/po-j-c_enter_inspection_buyoffs.htm)*

The **closer** for the QC-inspection path — transfers (or rejects)
what was received to QC.

### Three qty columns

- **Accepted** — transfer to inventory (or WIP if WO-tied).
- **Rejected** — return to vendor; requires a **Scrap Code**.
- **Use As Is** — transfers to inventory/WIP with the Accepted, but
  requires a **QC Code** to record less-than-perfect vendor work.

### What happens to rejected parts

Posted to the inventory transaction file as a **Q-type transaction,
negative quantity**. Parts placed on NCR go to
[QC-F-C Disposition NCR](../../../samples/chm/extracted/qc-f-c_disposition_ncr.htm).

### What happens to accepted parts (the bookkeeping trick)

Positive **P-type** transaction **and** an offsetting **negative
Q-type** — so the dollar value isn't double-counted in
[IN-N-A Print Month End Inventory Costing](../../../samples/chm/extracted/in-n-a_print_month_end_inventory_costing.htm).

### Returns back to PO

Rejected parts are put **back on the PO** against the line they were
originally received against — assumption is the vendor replaces them.

---

## PO-K Close Purchase Orders

*Source: [po-k_close_purchase_orders.htm](../../../samples/chm/extracted/po-k_close_purchase_orders.htm)*

Manual close for POs that won't naturally close via full receipt +
full invoice.

### Guard rails

- Items **Received-Not-Invoiced** on a line → **warning**, but close
  allowed.
- Items in **QC inspection** → **blocked** (must come out of QC first).

### Effective close date

Either "use latest Actual Received Date" or an explicit date. This
is **the date the receipt drops off [PO-I-F](#po-i-f-print-received-not-invoiced)**.

### The GL catch

> "Closing a PO makes no GL or Inventory transactions."

So when cleaning up old orphan POs off the RNI report, expect to
follow up with a **Journal Entry** against the PO/RNI GL account.

Reopen via [PO-D](#po-d-view-po-receivers).

---

## PO-L Assign Vendors to Items

*Source: [po-l_assign_vendors_to_items.htm](../../../samples/chm/extracted/po-l_assign_vendors_to_items.htm)*

Per-item list of vendors (and optionally **vendor item numbers** for
cross-reference).

**Effect:** when a PO line is entered for an item that has a vendor
item number here, the vendor item number pulls in as a comment-only
line under the PO line (see the auto-comment ordering in PO-A).

Also feeds the **approved-vendors** feature — see
[How to Use Approved Vendors and Manufacturers](../../../samples/chm/extracted/how_to_use_approved_vendors_and_manufacturers.htm).

---

## PO-M Purchase Order Inquiry

*Source: [po-m_purchase_order_inquiry.htm](../../../samples/chm/extracted/po-m_purchase_order_inquiry.htm)*

**Per-vendor inquiry hub.** One filter set; eight inquiry buttons
down the bottom to pivot on different views:
- **Purchase Orders** — open POs within the selection.
- **Receipts (F3)** — receipts within the selection.
- **Work Orders (F4)** — open WOs within the selection.
- Remaining 5 buttons — stock-status views for the entered item.

**Filters:** vendor (primary), item, PO #, job #, WO #, date range.

---

## PO-P View Vendor Information

*Source: [po-p_view_vendor_information.htm](../../../samples/chm/extracted/po-p_view_vendor_information.htm)*

Read-only / non-locking version of
[AP-A Enter Vendors](../../../samples/chm/extracted/ap-j_print_vendor_code_and_name.htm).
Identical screen; save / edit disabled.

---

## PO-Q Maintain PO Delivery Dates

*Source: [po-q_print_receiving_slip.htm](../../../samples/chm/extracted/po-q_print_receiving_slip.htm)*

Per-line date editor. The point of the program is the **two-field
separation**:

- **Estimated Receipt Date** — editable; **MRP uses this**.
- **Original Promise Date** — normally NOT edited;
  [PO-I-H Vendor Performance Report](#po-i-h-vendor-performance-report)
  rates against this.

So: delivery slipped? Update ERD. Vendor's still on the hook against
their original promise.

*Gotcha on the filename:* source htm is `po-q_print_receiving_slip.htm`
even though the program is **not** a receiving-slip print — the
vendor recycled the htm name.

---

## PO-R Print Receiving Slip

*Source: [po-r_print_receiving_slip_evo_erp_.htm](../../../samples/chm/extracted/po-r_print_receiving_slip_evo_erp_.htm)*

Prints a PO-shaped form **without prices** and with space for the
receiver to write in received-date / quantity. Same operation and
fields as [PO-B](#po-b-print-purchase-orders); different RTM.

---

## PO-T Digitally Sign Purchase Order

*Source: [po-t_digitally_sign_purchase_order.htm](../../../samples/chm/extracted/po-t_digitally_sign_purchase_order.htm)*

Electronic approval with signature-block printing on the PO.

**Operation:** signer's employee ID + password + PO #. PO total is
compared to the signer's **approval limit**. Authorized signers
defined in [PS-I Enter Digital Signers for PO](../../../samples/chm/extracted/ps-i_enter_digital_signers_for_po.htm).

---

## Cross-references

### Data tables this module writes

Primary tables per
[file-names-index · Purchase Orders](../../04-data-dictionary/file-names-index.md#purchase-orders):

| Table | Purpose |
|---|---|
| `BKAPPO` / `BKAPPOL` | Open PO header + lines |
| `BKAPHPO` / `BKAPHPOL` | Receiver header + lines (history) |
| `BKAPRFQ` / `BKAPRFQL` | RFQ header + lines |
| `BKAPQUOT` | Vendor pricing (PO-H) |
| `BKRFQ` | Verbal RFQs (PO-F) |
| `BKQCMSTR` / `BKQCTRAN` | QC master + transaction |
| `ISDIGSIG` | Digital signature records (PO-T) |
| `ISAPCHG` | Changes to POs (audit) |
| `BKAPAPO` / `BKAPAPOL` | Archived PO header/lines |
| `BKWOPO` | Temp file for WO-to-PO conversion |

### Related modules (LearnEVO)

- [WO — Work Orders](../wo-work-orders/README.md) —
  [help-content](../wo-work-orders/help-content.md). Direct-to-WO
  receipts (type P with WO), type-S service orders on routing
  sequences, [WO-K-Q Convert WO to PO](../wo-work-orders/help-content.md#wo-k-q-convert-wo-to-po).
- [JC — Job Costing](../jc-job-costing/README.md) —
  [help-content](../jc-job-costing/help-content.md).
  [JC-F Print Outside Purchases](../jc-job-costing/help-content.md#jc-f-print-outside-purchases)
  reads what PO-C wrote to WIP.
- [AP — Accounts Payable](../ap-accounts-payable/README.md) — where
  [AP-C Enter Purchase Order Invoices](../../../samples/chm/extracted/ap-c_enter_purchase_order_invoices.htm)
  closes the loop on receiving → invoicing → payment.
- [IN — Inventory](../in-inventory/README.md) — average-cost / Last
  Cost updates on receipt; on-PO qty maintenance.
- [MR — MRP](../mr-mrp/README.md) — uses PO-Q's Estimated Receipt
  Date for time-phased planning.

### Related CHM overview sections

- [System Overview § Sequence of Events — Purchase Orders](../../00-overview/system-overview.md#7d-purchase-orders)
  — the canonical seven-step PO flow.
- [System Overview § Month End Accounting](../../00-overview/system-overview.md#9-month-end-accounting--detail)
  — PO-I-F + PO-J-B tie-out to PO/RNI GL.
- [System Overview § Archiving](../../00-overview/system-overview.md#10-archiving-or-purging-old-data)
  — [SM-J-R Archive Purchase Orders](../../../samples/chm/extracted/sm-j-r-archive_purchase_orders.htm)
  moves BKAPPO / BKAPPOL data to archive tables.
