# LC — Lot Control

Status: verified (text distilled from the vendor's help file).

*Source: EvoHELP.CHM → Items → Lot Control (6 topics).*
*Extracted HTML in [samples/chm/extracted/](../../../samples/chm/extracted/).*

---

## Contents

- [LC-A — Edit Lot File](#lc-a--edit-lot-file)
- [LC-B — Assign Lot Control](#lc-b--assign-lot-control)
- [LC-C — Print Lot Availability](#lc-c--print-lot-availability)
- [LC-D — Print Lot History](#lc-d--print-lot-history)
- [LC-E — Lot Control On Hand Report](#lc-e--lot-control-on-hand-report)
- [LC-F — Lot Traceability Report](#lc-f--lot-traceability-report)
- [Cross-references](#cross-references)

---

## LC-A — Edit Lot File

*Source: [lc-a_edit_lot_file.htm](../../../samples/chm/extracted/lc-a_edit_lot_file.htm)*

**Purpose.** Use this program to view information pertaining to a specific lot number, or to add or change lot number information. Typical edits include entering an expiration date or notes against an existing lot record.

### Lot File Contents

The lot file stores the following information per lot number:

- Current on-hand quantity, broken down by **warehouse location**
- The **date the lot originated**
- The **purchase order number** or **work order number** the lot was created from

For full transaction-level history of a lot, use [LC-D Print Lot History](#lc-d--print-lot-history).

### How Lot Records Are Created

Lot file records are normally created automatically through one of two processes:

1. **Purchase order receiving** — a receipt in the Purchase Orders module creates the lot record.
2. **Finished production entry** — entering a work order completion in the Work Orders module creates the lot record.

You can create a lot record manually inside LC-A, but doing so **will not update the inventory transaction file or the general ledger detail file**. Manual creation is therefore not recommended. All corrections to lot quantities, dates, and order numbers should be made through standard transactions in the Purchase Orders, Inventory, Work Orders, and Sales Orders modules so that all related transaction files remain consistent.

### General Operation

1. Enter an **Item number** or press **F2** (or click **Lookup**) to select one from a pop-up window.
2. Enter the **Lot Number** or press **F2** (or click **Lookup**) to display all lot numbers associated with the selected item. Highlight the desired lot and press **Enter**.
3. The current information for the lot is displayed. Advance through fields with **Enter**.
4. Make any changes or additions.
5. Press **F10** (or click **Save**) to save the record.

### Safe vs. Unsafe Edits

| Field | Safe to edit here? | Notes |
|---|---|---|
| **Exp Date** | Yes | Expiration date — a primary use case for this screen |
| **Notes** | Yes | Free-text notes attached to the lot |
| **On-Hand** quantity | No — use module transactions | Direct edit bypasses inventory transaction and GL detail files |
| Origin dates | No — use module transactions | Same bypass risk |
| PO / WO number | No — use module transactions | Same bypass risk |

---

## LC-B — Assign Lot Control

*Source: [lc-b_assign_lot_control.htm](../../../samples/chm/extracted/lc-b_assign_lot_control.htm)*

**Purpose.** Use this program to designate which inventory items require lot-number tracking. Once an item is flagged for lot control, a lot number becomes mandatory whenever inventory moves for that item — in any module.

### Effect of the Lot Control Flag

When an item's **Lot Control** field is set to `Y`, a lot number is required in every transaction that affects inventory for that item, including:

- Purchase order receiving
- Inventory adjustments
- Work order issues and receipts
- Sales order shipments

Setting the field to `N` removes the requirement (but does not delete existing lot records).

### Alternative Entry Point

The same **Lot Control** flag can also be set directly on the item record via **IN-B Enter Inventory**. LC-B is a focused shortcut for updating this flag without navigating through the full item maintenance screen.

### General Operation

1. Enter the **Item number** of the item that will require lot control, or press **F2** (or click **Lookup**) to select from a pop-up window.
2. The item's **Product Type** (purchase part, finished good, subassembly, etc.) is automatically displayed for confirmation.
3. Enter `Y` to enable lot control for the item, or `N` to disable it.
4. Press **Enter** when prompted to confirm. The record is saved.

---

## LC-C — Print Lot Availability

*Source: [lc-c_print_lot_availability.htm](../../../samples/chm/extracted/lc-c_print_lot_availability.htm)*

**Purpose.** Use this program to produce a listing of current on-hand inventory quantities broken down by lot number. The report is sorted by item number, then by lot number within item number.

### Report Filters

| Filter | Description |
|---|---|
| **Item Number from/thru** | Limits the report to a range of item numbers. Press F2 or click Lookup to select from a pop-up window. |
| **Lot Number from/thru** | Further narrows output to a specific range of lot numbers. |
| **Include allocated items** | Controls whether units already allocated to sales orders (and therefore not freely available) are included in the report. |

### Use Case

This report answers the question "how much of each lot do I have on hand right now?" It is the primary snapshot report for lot-controlled inventory availability. The allocation filter lets you distinguish between gross on-hand and net-available quantities when open sales order commitments exist.

---

## LC-D — Print Lot History

*Source: [lc-d_print_lot_history.htm](../../../samples/chm/extracted/lc-d_print_lot_history.htm)*

**Purpose.** Use this report to obtain a full transaction listing for specific lot numbers. The report provides end-to-end traceability — from the inception of a lot through every transaction in which that lot was consumed or moved.

### Transaction Types

The report can be filtered to include only selected transaction types. The available types are:

| Code | Transaction Type |
|---|---|
| `A` | Adjustments (IN-C, IN-K, or Physical Inventory) |
| `B` | Bin Location Transfers |
| `C` | PO Price Change entered in AP-C *(not tracked by Lot Number)* |
| `G` | Scrap |
| `I` | Stock issues to work-in-process |
| `J` | Purchase order receipts to work-in-process |
| `M` | Make-From Component Issue |
| `O` | Outside Processing (Service) PO Receipt to Work Order *(not tracked by Lot Number)* |
| `P` | Purchase order receipts to stock |
| `Q` | Purchase Receipt to QC |
| `R` | Service and Repair |
| `S` | Shipments |
| `T` | Warehouse Transfer |
| `W` | Work order receipts to stock |

Note: transaction types `C` (PO Price Change) and `O` (Outside Processing PO Receipt to WO) are listed but are **not tracked by Lot Number**.

### Report Definition Names

The program supports named report definitions. You can save a combination of selection filters under a report name and reuse it in future sessions. This allows multiple predefined report configurations (e.g., one for purchase receipts only, one for shipments only) without re-entering filters each time.

### Sort Orders

Select a sort order before running the report. The recommended default is **Item Number / Lot Number**. Sort order directly affects report speed because it controls which database indexes are used to select and sequence the data.

### Filter Options — Screen 1

- **Item number** or range of items
- **Transaction date range**
- Additional filters (customer, vendor, and others)
- **Filter printing option**: print the active filter list on every page, the first page only, at the end only, or not at all

### Filter Options — Screen 2 (Next Screen)

Clicking **Next Screen** exposes additional filters, including filtering by **Lot Number** directly.

### General Operation

1. Enter an existing report name or type a new one to create it.
2. Select the desired sort order.
3. Use the spacebar to toggle the `X` marker on each transaction type to include or exclude.
4. Choose where to print the filter list.
5. Enter the item number or range, transaction date range, and any additional filters.
6. Click **Print** at any time to run the report with the current filter set.
7. Optionally click **Next Screen** to add lot number and other secondary filters before printing.

---

## LC-E — Lot Control On Hand Report

*Source: [lc-e-lot_control_on_hand_report.htm](../../../samples/chm/extracted/lc-e-lot_control_on_hand_report.htm)*

**Purpose.** *(Available in Evo-ERP only — not in the older DBA Manufacturing baseline.)* Use this program to produce a listing of current on-hand inventory by lot number compared against total inventory on hand, and to manage exceptions where the lot totals do not reconcile with the inventory balance.

### Report Filters and Options

| Filter / Option | Description |
|---|---|
| **Item Number from/thru** | Limits report to a range of item numbers |
| **Class** | Filter by item class |
| **Category** | Filter by item category |
| **Item Types** | Select which item types to include |
| **Exceptions only** | Include only items where total inventory on hand does not equal the sum of all lot quantities |
| **Negative Lot UOH** | Include lots with a negative unit on-hand quantity |
| **Orphan Lots** | Include lots assigned to item numbers that have since been deleted |
| **Summary only / Lot detail** | Toggle between a summary line per item and a full lot-by-lot breakdown |
| **Sort by** | Sort within item number by **Lot** number or by **Expiration Date** |

### Primary Use Case

This report is the diagnostic tool for lot control integrity. Running it with **Exceptions only** enabled will surface any items where the sum of lot quantities has drifted from the inventory on-hand balance — a condition that requires investigation and correction through standard module transactions.

---

## LC-F — Lot Traceability Report

*Source: [lc-f-lot_traceability_report.htm](../../../samples/chm/extracted/lc-f-lot_traceability_report.htm)*

**Purpose.** Use this program to obtain a complete activity listing for a given part and lot number — showing where the lot came from, where it went, and confirming that all units are accounted for.

### Report Scope

The report covers:

- **Inbound activity** — the origin of the lot (purchase receipt, work order completion, etc.)
- **Outbound activity** — every transaction in which units of the lot were consumed or shipped
- **Unit reconciliation** — confirmation that all units are accounted for across inbound and outbound transactions

### General Operation

1. Enter the **Item number** and **Lot number** to report on.
2. Choose the output level:
   - **Summary** — totals only
   - **Details** — individual transaction lines
   - **All** — both summary and detail

### Relationship to LC-D

LC-F is focused: one item, one lot, full picture. LC-D is the broader history report that can span many items and lots filtered by transaction type, date range, customer, vendor, and other criteria. For a targeted lot investigation (e.g., a quality recall on a specific lot), LC-F is the appropriate tool. For cross-lot or cross-item trend analysis, use LC-D.

---

## Cross-references

| Module | Relationship |
|---|---|
| **IN — Inventory** | The **Lot Control** flag on each item is also maintained in IN-B (Enter Inventory). Inventory adjustments (IN-C, IN-K) and physical inventory counts generate lot transaction type `A`. Lot records are visible and maintainable via LC-A. |
| **PO — Purchase Orders** | Purchase order receiving creates lot records automatically (transaction types `P` = receipt to stock, `J` = receipt to WIP, `Q` = receipt to QC). The originating PO number is stored on the lot record. |
| **WO — Work Orders** | Work order completions create lot records automatically (transaction type `W` = receipt to stock). Work order component issues consume lot-controlled items (transaction type `I`). The originating WO number is stored on the lot record. |
| **SO — Sales Orders** | Sales order shipments consume lot-controlled items (transaction type `S`). Allocated units appear in the LC-C availability report when the allocation filter is active. |
| **AP — Accounts Payable** | PO price changes entered in AP-C generate transaction type `C` but are not tracked by lot number. |
