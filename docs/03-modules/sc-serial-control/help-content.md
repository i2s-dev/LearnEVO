# SC — Serial Control

Status: verified (text distilled from the vendor's help file).

*Source: EvoHELP.CHM → Items → Serial Control (8 topics).*
*Extracted HTML in [samples/chm/extracted/](../../../samples/chm/extracted/).*

---

## Contents

- [SC-A — Edit Serial File](#sc-a--edit-serial-file)
- [SC-B — Assign Serial Control](#sc-b--assign-serial-control)
- [SC-C — Print Serial Availability](#sc-c--print-serial-availability)
- [SC-D — Print Serial History](#sc-d--print-serial-history)
- [SC-E — Archive Serial History](#sc-e--archive-serial-history)
- [SC-F — Serial Control Exception Report](#sc-f--serial-control-exception-report)
- [SC-G — Enter Serial Generation Parameters](#sc-g--enter-serial-generation-parameters)
- [SC-H — Serial Traceability Report](#sc-h--serial-traceability-report)
- [Cross-references](#cross-references)

---

## SC-A — Edit Serial File

*Source: [sc-a_edit_serial_file.htm](../../../samples/chm/extracted/sc-a_edit_serial_file.htm)*

**Purpose.** Use this program to view information pertaining to a specific serial number, or to add or change serial number information. Common uses include entering an expiration date or adding notes to a serial record.

### Serial File Contents

The serial file contains the date the serial number originated and the purchase order number or work order number the serial number originated from. For detailed transaction history, see [SC-D Print Serial History](#sc-d--print-serial-history) or [SC-H Serial Traceability Report](#sc-h--serial-traceability-report).

### How Serial Records Are Created

Normally, serial file records are created automatically through:

- Purchase order receiving
- Entering finished production in the Work Orders module

Manual creation of a serial record is possible, but it will **not** correctly update the inventory transaction file and general ledger detail file and is therefore not recommended. All corrections to the serial file should be made through standard transactions in the **Purchase Orders**, **Inventory**, **Work Orders**, and **Sales Orders** modules.

### General Program Operation

1. Enter an **Item number** or select one by clicking the **Lookup** icon (or press F2).
2. Enter the **Serial Number** or click the **Lookup** icon (or press F2) to display all serial numbers associated with the selected item. Highlight the desired one and press `<Enter>`.
3. The current information for this serial number will be displayed. Advance through fields by pressing `<Enter>`.
4. Make any changes or additions, then click the **Save** button (or press F10) to save the entry.

### Field Guidance

As a general rule, only the **Exp Date** (expiration date) and **Notes** fields should be updated directly in this screen. Changes to date fields and order number fields are best made through the **Purchase Orders**, **Inventory**, **Work Orders**, and **Sales Orders** modules so that all related transaction files are properly updated.

---

## SC-B — Assign Serial Control

*Source: [sc-b_assign_serial_control.htm](../../../samples/chm/extracted/sc-b_assign_serial_control.htm)*

**Purpose.** Use this program to determine which specific inventory items will require serial control. When an item's **Serial Control** field is set to `Y`, a serial number will be required whenever inventory is affected for that item, in any of the following contexts:

- Purchase receiving
- Inventory adjustments
- Work order issues or receipts
- Sales order shipments

### General Program Operation

1. Enter the **Item number** of the item to configure for serial control, or select an item from the pop-up window by pressing F2 (or clicking the **Lookup** button).
2. The item's **Product Type** (purchase part, finished good, subassembly, etc.) will be automatically displayed.
3. Enter `Y` to require serial control for this item, or `N` to remove the serial control requirement from an item previously coded for it.
4. You will be asked if you want to save the record. Press `<Enter>` to confirm and save.

---

## SC-C — Print Serial Availability

*Source: [sc-c_print_serial_availability.htm](../../../samples/chm/extracted/sc-c_print_serial_availability.htm)*

**Purpose.** Use this program to get a listing of current on-hand inventory by serial number. The report is sorted by item number, and by serial number within item number.

### General Program Operation

1. Enter a from/thru range of **Item numbers**. Item numbers can be selected from a pop-up window by pressing F2 (or clicking the **Lookup** button).
2. Optionally, further limit the report by entering a from/thru range of **Serial Numbers**.
3. Indicate whether items already **allocated to sales orders** (and therefore not truly available for other use) should be included in the report.

### Report Output

The report shows current on-hand inventory broken down by serial number, sorted first by item number and then by serial number within each item. The sales-order allocation filter allows users to see only genuinely uncommitted stock.

---

## SC-D — Print Serial History

*Source: [sc-d_print_serial_history.htm](../../../samples/chm/extracted/sc-d_print_serial_history.htm)*

**Purpose.** Use this report to get a listing of transactions associated with particular serial numbers. The report provides full traceability from the inception of a serial number through all uses of that serial number. The report can be limited to specific transaction types.

### General Program Operation

1. Enter an existing **report name** or create a new one. Multiple report names allow predefined combinations of selection filters to be saved and reused. Once reports are defined, you need only select the report name, adjust item number and/or date range, and click Print.
2. Select a **sort order** for the report. The suggested default is **Item Number / Serial Number**. The sort order directly affects report speed and which indexes are used to select and optimize the data.
3. Select the desired **transaction types** by accepting or removing the `X` next to each type using the space bar.

### Transaction Type Codes

| Code | Transaction Type |
|------|-----------------|
| `A` | Adjustments (IN-C, IN-K, or Physical Inventory) |
| `B` | Bin Location Transfers |
| `C` | PO Price Change entered in AP-C (not tracked by Lot Number) |
| `G` | Scrap |
| `I` | Stock issues to work-in-process |
| `J` | Purchase order receipts to work-in-process |
| `M` | Make-From Component Issue |
| `O` | Outside Processing (Service) PO Receipt to Work Order (not tracked by Lot Number) |
| `P` | Purchase order receipts to stock |
| `Q` | Purchase Receipt to QC |
| `R` | Service & Repair |
| `S` | Shipments |
| `T` | Warehouse Transfer |
| `W` | Work order receipts to stock |

### Filter and Print Options

- Select whether to print the list of filters on **the top of each page**, **first page only**, **at the end only**, or **not at all**.
- Select the **Item number** or range of items to report on.
- Select a **Transaction date range** and any additional filters desired.
- Click **Print** at any time to run the report based on current filters.
- Click **Next Screen** to access additional filters including a **Serial Number** filter.

---

## SC-E — Archive Serial History

*Source: [sc-e_archive_serial_history.htm](../../../samples/chm/extracted/sc-e_archive_serial_history.htm)*

**Purpose.** Use this program to archive or restore serial records based on various parameters. Archiving reduces the active working set of serial data, improving performance, while retaining the ability to restore records if needed.

### General Program Operation

1. Indicate whether to **Archive** or **Un-Archive (Restore)** items.
2. Enter the appropriate ranges:
   - **Item Numbers**
   - **Serial Numbers**
   - **Expiration dates** (as applicable)
   - **Received dates** (as applicable)
   - **Shipped dates** (as applicable)
3. Indicate whether to **only archive serial records with 0 on-hand quantity** — this defaults to `Y`.
4. Select the **Warehouse Location**.
5. Process the operation.

### Notes

The default behavior (archive only zero-quantity records) prevents accidentally archiving serial numbers that still represent on-hand stock.

---

## SC-F — Serial Control Exception Report

*Source: [sc-f_serial_control_exception_report.htm](../../../samples/chm/extracted/sc-f_serial_control_exception_report.htm)*

**Purpose.** Use this program to identify serial-numbered items with data discrepancies such as duplicate serial numbers, negative on-hand quantities, and other integrity issues.

### General Program Operation

1. Indicate the range of **Item number**, **Product Class**, and **Category**, and the **item types** to be included.
2. Indicate which **exception types** to include.
3. Click **Print**.

### Exception Types

| Exception | Description |
|-----------|-------------|
| **Negative Serial UOH** | Individual serial records with a negative on-hand quantity |
| **Orphan Serial** | A serial number assigned to an item number that no longer exists |
| **Serial Control Change** | Serial records for items that no longer require serial control |
| **Serial UOH <> Location UOH** | Total on-hand quantity of all serial numbers does not match the warehouse location on-hand quantity |
| **Duplicate Serials** | Multiple instances of the same serial number/item in a given warehouse location |
| **Invalid Serial Locations** | Serial records assigned to a warehouse location that the item is not assigned to |
| **Expired Serials [Y/N/Z]** | Check for expired serial numbers with on-hand quantity; enter `Z` to identify serial records with a `00/00/00` expiration date |
| **Unbalanced Serial Transactions** | Net of transactions for a serial number does not match the on-hand quantity |
| **Non-zero qty in multiple locations** | Serial records for the same serial number/item in different locations but more than one non-zero on-hand quantity |
| **Irregular On Hand Quantity** | Serial record with an on-hand quantity other than `1`, `0`, or `-1` |

### Notes

Serial quantities are expected to be binary (1 = in stock, 0 = not in stock, -1 = negative exception). Any other value is flagged as irregular. This report is the primary tool for diagnosing serial file integrity problems before they propagate to financial records.

---

## SC-G — Enter Serial Generation Parameters

*Source: [sc-g_enter_serial_generation_parameters.htm](../../../samples/chm/extracted/sc-g_enter_serial_generation_parameters.htm)*

**Purpose.** Use this program to define the parameters of your serial number configuration. These parameters are used in **WO-I Enter Finished Production** or **PO-C Receive Purchase Orders** when automatically generating a range of serial numbers.

### Scope of the Serial Number Range

The serial number generation parameters can be configured at three levels of granularity:

| Scope | Configuration |
|-------|---------------|
| Per part number | Enter a specific **part number** |
| Per item class | Leave item number blank; enter the **Class** |
| All parts (single range) | Leave both item number and class blank |

### Parameters to Define

- **Total length** of the serial number.
- **Start position** of the numeric portion (the counter that will be incremented).
- **Number of digits** in the counter.
- **Last counter value** used.
- **Complete Last Serial Number** used.

### How It Works

When a user receives a purchase order (PO-C) or enters finished production (WO-I) for a serial-controlled item, EvoERP can automatically generate a sequential range of serial numbers. SC-G defines the template and current counter state so that the system knows what the next serial number should be.

---

## SC-H — Serial Traceability Report

*Source: [sc-h_serial_traceability_report.htm](../../../samples/chm/extracted/sc-h_serial_traceability_report.htm)*

**Purpose.** Use this program to get a listing of all activity for a range of item and/or serial numbers. This report provides a consolidated view of the complete lifecycle of a serial number across all modules.

### General Program Operation

1. Enter the desired **item number** range and **serial number** range.
2. Click **Print**.

### Notes

SC-H is the simplified, focused traceability report. For a more configurable, transaction-type-filtered view, see [SC-D Print Serial History](#sc-d--print-serial-history). SC-H is cross-referenced from SC-A (Edit Serial File) as one of two options for looking up detailed history on a specific serial number.

---

## Cross-references

| Module | Relationship |
|--------|-------------|
| **IN — Inventory** | Serial control is enforced during inventory adjustments (IN-C, IN-K) and physical inventory. Serial records are created or consumed by inventory transactions. |
| **PO — Purchase Orders** | Serial numbers are assigned at PO receiving (PO-C Receive Purchase Orders). SC-G generation parameters feed into PO-C for automatic serial number generation. |
| **WO — Work Orders** | Serial numbers are assigned when entering finished production (WO-I). SC-G generation parameters feed into WO-I. Serial history transaction types `I`, `J`, `M`, `W` all originate in Work Orders. |
| **SO — Sales Orders** | Serial numbers are consumed at shipment. SC-C (Print Serial Availability) can filter out units already allocated to sales orders. |
| **SR — Service & Repair** | Service and repair transactions generate serial history type `R`, tracked through SC-D and SC-H. |
| **AP — Accounts Payable** | AP-C PO Price Change transactions appear in serial history as type `C` (not tracked by Lot Number). |
