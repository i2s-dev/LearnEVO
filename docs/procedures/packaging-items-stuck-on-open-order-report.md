# IT Case Study: Packaging Items Stuck on Open Order Report

**Status:** Resolved — 2026-06-18  
**Reported by:** Casey  
**Customer affected:** Albertsons (customer code 2B13)  
**Resolved by:** SD-M flag change (one setting, no data edits)

---

## Symptom

12 part numbers — all packaging components and install guides — appeared permanently on the
Open Sales Order Listing (SO-O-A) with Qty To Ship > 0 but Qty Shipped = 0. They never
cleared no matter how many times SO-G was run. Albertsons complained about apparent short
shipments because these lines showed as unfulfilled on every order.

The 12 items:

| Part Number | Description | Class | Cat |
|-------------|-------------|-------|-----|
| 730-54200 | BOX,CDBD,ACCESSORY,ALBERTSONS | BOX | HRC |
| 730-54117 | BOX,CDBD,50INCH,ALBERTSONS | BOX | HRC |
| 730-54201 | INSERT,CDBD,5 LIGHT,ALBERTSONS | BOX | HRC |
| 730-54116 | BOX,CDBD,60INCH,ALBERTSONS | BOX | HRC |
| 090-05233 | QUICKSTART GUIDE,COMPOSE | DOC | COVE |
| 090-52716 | INSTR,INSTALL,CP ACT | DOC | CPSE |
| 090-05230 | QUICKSTART GUIDE,COMPOSE | DOC | COVE |
| 090-52711 | (install guide) | DOC | CPSE |
| 090-05234 | (install guide) | DOC | COVE |
| 090-52713 | (install guide) | DOC | CPSE |
| 090-53118 | (install guide) | DOC | CPSE |
| 090-52715 | (install guide) | DOC | CPSE |

---

## Root Cause

These items are **packaging and documentation that ship inside the product box**. They are
added to sales orders with a quantity, but warehouse staff never individually scan or release
them through **SO-E** (Release Sales Orders) — they go out physically with the finished goods.

This means when **SO-G** (Post Invoices) runs, these lines always have **Qty Shipped = 0**.

The system default **SD-M → Processing Tab → "Create 0 Qty SO Lines during post"** was set
to **N**. With this flag set to N, SO-G skips every line with Qty Shipped = 0 entirely — it
neither posts them nor closes them. They accumulate as permanently open lines.

Confirmed by SO-O-A: 730-54200 alone had **28 open SOs** spanning 06/29/26–01/04/27,
totaling 475 units, all with Qty Shipped = 0.00 on every line.

---

## Dead Ends Investigated

These were checked and ruled out before the root cause was found:

| Hypothesis | What was checked | Result |
|------------|-----------------|--------|
| Item Type prevents posting | IN-A → Type field | All items Type=R (Regular). Not the cause. |
| Item Class has posting flag | CLASS table schema | CLASS table only contains GL accounts. No posting flag exists. |
| Lot/Serial Control blocking release | IN-B Controls tab, ADTR bitmask | Lot Control=N, Serial Control=N on all items. Not the cause. |
| 730 items had different item flags than 090 items | BKICMSTR binary scan (ADTR field) | 730 items had ADTR=0x000E vs. 090 items ADTR=0x0000, but this bit pattern did not map to any IN-B visible field and was not the cause. |

---

## Fix — Step by Step

### Step 1: Change the SD-M flag

1. Launch EvoERP, go to the **SD** menu → **SD-M** (Sales Order Defaults)
2. On the screen that opens, click the **Processing** tab
3. Find the field: **"Create 0 Qty SO Lines during post"**
4. Check the box (set to **Y**)
5. Save

This is a system-wide setting. It takes effect for all future SO-G runs company-wide.

> **Side effect warning:** With this flag Y, SO-G will now post every 0-ship-qty line
> company-wide — not just these 12 items. This is the correct behavior for packaging items.
> Alert accounting or operations before the next batch SO-G run if other items may be
> affected.

### Step 2: Clear the backlog with SO-G

The fix only affects future SO-G runs. All the existing open lines from before the change
must be manually cleared by running SO-G:

1. Go to **SO-G** (Post Invoices) — under the SO menu
2. Set **SO Number From** and **Thru** to the range covering affected orders
   - For a test: enter a single known SO number in both From and Thru (e.g., `74632` / `74632`)
   - For a full clearance: use the range covering all open SOs for these items
3. Click **Post**
4. SO-G will process all lines on those SOs, including the 0-ship-qty packaging lines
5. Verify with **SO-O-A**: filter to the item number and confirm it no longer appears

> **What SO-G does internally:** It creates GL entries (COGS, Sales, AR), updates inventory
> transaction history, and marks lines as posted. It does NOT send anything to the customer.
> It is purely an internal financial posting operation.

---

## Why the 090 Items Appeared to "Fix Themselves"

At some point prior to this ticket being filed, the 090-series items went through SO-G
successfully (their BKICMSTR audit trail showed SO-G and SO-E activity). This means their
orders had ship qty > 0 at some point — someone had individually released them through SO-E,
or they were on a separate order that was properly released. They were not permanently fixed
by a configuration difference; they just happened to catch a release cycle the 730 items
never did.

---

## Relevant EVO Screens

| Screen | Menu Code | Purpose in this case |
|--------|-----------|----------------------|
| Open Sales Order Listing | SO-O-A | Diagnose: shows Qty Shipped = 0 on affected lines |
| Sales Order Defaults | SD-M | Fix: "Create 0 Qty SO Lines during post" flag |
| Post Invoices | SO-G | Clearance: posts the 0-qty lines and removes from open report |
| Release Sales Orders | SO-E | Context: packaging items are NOT released here (that's why qty stays 0) |
| Inventory Inquiry | IN-A | Checked item type (Type=R, not the cause) |
| Enter Inventory | IN-B | Checked Controls tab (Lot/Serial = N, not the cause) |
| Master Default Settings | DEF-M (via SD-M) | The screen where the fix lives |

---

## Key Field Reference

| Table | Field | Offset | Notes |
|-------|-------|--------|-------|
| BKICMSTR.BI2 | BKIC_PROD_TYPE | 45 | Item type — all affected items are R (Regular) |
| BKICMSTR.BI2 | BKIC_PROD_CLASS | 54 | BOX (730 items) or DOC (090 items) |
| BKICMSTR.BI2 | BKIC_PROD_ADTR | 86 | UBINARY 2 bytes — bitmask, not directly mapped to visible IN-B posting flags |
| SD-M setting | "Create 0 Qty SO Lines during post" | — | The fix; stored in the SD-M system defaults |

**Confidence: 95/100** — Root cause confirmed by SO-O-A verification showing 0 ship qty;
fix confirmed working by end user (Casey, 2026-06-18).
