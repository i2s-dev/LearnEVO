# PI — Physical Inventory

Status: verified (text distilled from the vendor's help file).

*Source: EvoHELP.CHM → Items → Physical Inventory (8 topics).*
*Extracted HTML in [samples/chm/extracted/](../../../samples/chm/extracted/).*

---

## Contents

- [PI-A — Capture Frozen Inventory](#pi-a--capture-frozen-inventory)
- [PI-B — Frozen Inventory Report](#pi-b--frozen-inventory-report)
- [PI-C — Enter Tag Counts](#pi-c--enter-tag-counts)
- [PI-D — Print Missing Tags](#pi-d--print-missing-tags)
- [PI-E — Edit Frozen Inventory Costs](#pi-e--edit-frozen-inventory-costs)
- [PI-F — Physical Inventory Report](#pi-f--physical-inventory-report)
- [PI-G — Update Actual Inventory](#pi-g--update-actual-inventory)
- [PI-H — Purge Physical Inventory](#pi-h--purge-physical-inventory)
- [Cross-references](#cross-references)

---

## Overview: The Physical Inventory Workflow

The PI module supports both full physical inventory counts and partial/cycle counts. The overall workflow is:

1. **Freeze** — run PI-A to snapshot current quantities and costs into a holding file. Halt operations.
2. **Report** — run PI-B to print count sheets (optional).
3. **Count** — physically count items and record on pre-numbered tags (or count sheets).
4. **Enter counts** — run PI-C to key in tag data (or import from a file).
5. **Check tags** — run PI-D to identify any missing tag numbers.
6. **Correct costs** (if needed) — run PI-E to assign costs to newly-discovered items.
7. **Review** — run PI-F (Physical Inventory Report) to verify counts and totals before posting.
8. **Post** — run PI-G to update on-hand quantities and optionally post GL adjustments.
9. **Purge** (when ready) — run PI-H to remove old physical inventory records from the file.

---

## PI-A — Capture Frozen Inventory

*Source: [pi-a_capture_frozen_inventory.htm](../../../samples/chm/extracted/pi-a_capture_frozen_inventory.htm)*

**Purpose.** Use this program to capture current inventory counts and costs into a separate holding file. This holding file is later compared with the physical inventory counts; the actual inventory and General Ledger are corrected for any discrepancies. Once this program is run, operations should cease until all physical counts are completed.

You can freeze the entire inventory (full physical) or limit the items frozen to support a partial inventory or cycle counting. Each physical inventory record stays on file indefinitely until purged through PI-H.

### Pre-capture checklist

When the program starts it displays an information screen that recommends running certain programs and reports before capturing. These programs can identify potential inventory problem areas that are best resolved prior to conducting a physical count.

### Creating a New Physical Inventory

Enter the **Year** and the **Physical Inventory No** to identify the new record.

The **Freeze Date** defaults to today's date but can be overridden. Regardless of the date entered, the costs and quantities frozen are a snapshot of inventory as it exists at the moment the capture executes. The program does not back out transactions to arrive at a prior-date on-hand quantity.

**Count Type** controls how uncounted items are treated:

| Value | Meaning |
|---|---|
| `Type 1` | Partial/cycle count. Items within the selected ranges that are not counted are ignored; no adjustment is made for them. |
| `Type 2` | Full count. All items with on-hand quantity within the selected ranges will be counted. Any item not counted will be zeroed out by the update. |

You can limit the items frozen by specifying a **Cycle Code** or by entering from/thru ranges for:

- Item numbers
- Item classes
- Category
- GL asset accounts

Once the filter fields are complete (or after clicking **Process**), a Location selection screen appears. Tag individual locations by double-clicking or by highlighting and clicking **Tag One**. To include all locations click **Tag All**.

After tagging, click **Go**. Confirm with **Yes** (or press Enter) to begin capturing. When finished you are prompted to print the Frozen Inventory Report; you can print immediately or defer to PI-B.

### Changing an Existing Physical Inventory

Enter the year and number of the physical inventory to change, or select from a lookup. Modify any filter ranges as needed, then click **Process**. The program informs you this is an existing physical inventory.

On the Location tagging screen, tag or untag locations as desired. If you tag a location that already has tag records entered through PI-C, you will be given the option to delete those tag records or leave them intact to avoid re-entry.

After tagging, click **Go** and confirm. The inventory will be re-frozen with completely new records replacing the existing ones.

---

## PI-B — Frozen Inventory Report

*Source: [pi-b_frozen_inventory_report.htm](../../../samples/chm/extracted/pi-b_frozen_inventory_report.htm)*

**Purpose.** This report lists the items captured by PI-A. It serves two purposes: as a reference listing of the frozen snapshot, and as a count sheet alternative to pre-numbered inventory tags. Each report line is assigned a unique line number that can be used as a tag number when entering counts in PI-C.

### Parameters

| Field | Options | Notes |
|---|---|---|
| **Year / Physical Inventory No** | Entered or selected from lookup | Identifies which frozen inventory to report. |
| **Print lot/serial detail** | `Y` / `N` | Whether to print current lot and serial number detail lines for items coded for lot or serial control. |
| **Print 2nd description line** | `Y` / `N` | Whether the second line of item description is included. |
| **Print current on-hand quantity** | `Y` / `N` | Generally not recommended when used as a count sheet — personnel should not know the current on-hand amount, as this leads to more accurate independent counts. |
| **Sort order** | `P` = by item number; `B` = by bin location | Choose based on how your warehouse is organized for counting. |
| **Print frozen cost** | `Y` / `N` | Whether the frozen inventory cost is shown on the report. |

After completing selection criteria, a **Locations** tagging screen appears. Tag or untag the locations to include, then click **Go** to print.

---

## PI-C — Enter Tag Counts

*Source: [pi-c_enter_tag_counts.htm](../../../samples/chm/extracted/pi-c_enter_tag_counts.htm)*

**Purpose.** Use this program to enter the information collected on physical inventory tags. Tags are not supplied with the system; any all-purpose pre-numbered inventory tags are suitable. Tags are normally attached in advance to items, bins, shelves, and pallets. Counts are made, item numbers and quantities written on tags, and tags collected. All collected tags are then entered into the system here.

If PI-B was used as a count sheet, the unique line numbers on that report serve as tag numbers. Counts can also be imported from a barcode data collection device output file.

**Important:** Do not tag items already issued to work-in-process. The PI module covers on-hand inventory only. For WIP inventory use JC-P (Print Materials in WIP); WIP adjustments must go through WO-G (Issue Materials).

### Lot and Serial Number Items

For items coded for lot control or serial control, one tag entry is required per lot number or serial number.

### Entering New Tag Records

1. Enter **Year** and **Phys Inv No**, or select from lookup.
2. A scrolling list of existing tags is displayed. Click **Add** to enter a new tag.
3. Enter **Tag Number**. After the first entry the number auto-increments by one; you can accept or override it. Tag numbers must be unique.
4. Enter **Location** (factory or warehouse).
5. Enter **Item number** or select from lookup. **Description** and **Unit of Measure** display automatically. Multiple tags for the same item are allowed; on-hand quantity will be the sum of all tags. Lot/serial controlled items require a separate tag per lot or serial number.
6. If an item number is not found in the inventory master file, the program prompts: "This part number does not exist. Would you like to set it up as a new part number?" Answer `Y` and create the part from this screen. Do not go to IN-B (Enter Inventory) to set it up.
7. Enter **Count Qty**. A quantity of zero is accepted to satisfy audit accountability requirements.
8. Enter **Bin Loc** (bin location) if applicable.
9. If the item requires lot or serial control, enter the **Lot Number** or **Serial Number**.
10. Enter **Bin Location** if applicable (defaults to the item's default bin location; can be overridden).
11. Enter **Count Date**. Defaults to today's date. The date entered persists for all subsequent entries until changed.
12. Enter **Employee No** (optional). If entered, the **Name** is displayed from the employee file. Non-employee personnel can also be tracked; the program issues a warning and allows a non-employee name to be entered.
13. Enter optional **Comment** for reference notes.
14. Save the record when the last field is completed (prompted automatically), or click **Save** (or press F10) at any point.

### Editing Tag Records

From the opening screen, highlight the tag record in the scrolling list and click **Edit**. Make changes and save. You are returned to the list to continue editing or take other actions.

### Deleting Tag Records

From the opening screen, highlight the tag record and click **Delete**. Confirm with **Yes** (or press Enter).

### Importing Tag Records

Counts collected with a barcode device can be imported from a comma-delimited or fixed-length ASCII file.

**Required file fields:** Tag Number (or incremental line counter), Location, Part number, Quantity counted, and Lot Number (for lot-controlled items). Employee number and Bin Location are optional. Serial-controlled items cannot be imported at this time.

**Import procedure:**

1. Click **Import** on the opening screen.
2. Enter the **file name**. The file name and path must conform to 8.3 naming convention (no names longer than 8 characters plus 3-character extension, no spaces in file or path names). Easiest to save the file in the application folder so no path prefix is needed.
3. Indicate whether existing tag numbers should be **skipped** or **replaced**.
4. Indicate whether the file is **comma delimited** or **fixed length**.
5. Enter the **Year** and **Quarter** of the physical inventory and the **count date**.
6. Specify the position of data fields in the text file:
   - Comma delimited: enter the column number in the first position; leave the second position at `0`.
   - Fixed length: enter the beginning position in the first column and the field length in the second.
7. Press Enter/Tab through all fields or press F10 to process.

A report listing imported items and exceptions (e.g. serial-controlled items requiring manual entry) is produced.

---

## PI-D — Print Missing Tags

*Source: [pi-d_print_missing_tags.htm](../../../samples/chm/extracted/pi-d_print_missing_tags.htm)*

**Purpose.** Use this report to identify any missing tags — specifically any tag numbers or ranges of tag numbers that are absent from the sequence of tags already entered in PI-C. This is a control report to ensure all pre-numbered tags are accounted for before posting.

### Parameters

| Field | Notes |
|---|---|
| **Year / Phys/Inv No** | Defaults to the latest physical inventory on file. |
| **Locations** | Optional filter; select specific factories or warehouses to limit the report scope. |
| **Starting Tag Number** | Enter a specific number to start the report at that point, or press Enter to get a listing of all missing tags in the full sequence. |

---

## PI-E — Edit Frozen Inventory Costs

*Source: [pi-e_edit_frozen_inventory_costs.htm](../../../samples/chm/extracted/pi-e_edit_frozen_inventory_costs.htm)*

**Purpose.** This program is for a narrow, specific use case: assigning a cost to an item that was discovered during counting, was not previously in the inventory database, and was entered as a new part number during PI-C. Because the item did not exist at freeze time, its Frozen Cost and on-hand quantity are both zero. This program allows a cost to be entered for that item.

**Restriction:** Companies on FIFO or LIFO costing cannot use this program.

### Operation

1. Enter **Year** and **Phys/Inv No** (defaults to latest on file).
2. A listing of frozen inventory items is displayed.
3. Double-click the item whose cost is to be set.
4. Enter the new cost on the detail screen.
5. You are returned to the list to make additional entries or click **Exit** to return to the Physical Inventory menu.

---

## PI-F — Physical Inventory Report

*Source: [pi-f_physical_inventory_report.htm](../../../samples/chm/extracted/pi-f_physical_inventory_report.htm)*

**Purpose.** Use this report to review the physical inventory results before posting via PI-G. The report can run in summary (count and cost summary per item), in detail (information from each numbered tag), or as an uncounted parts exception report. The report footer shows totals for current inventory value, physical inventory value, and the difference between the two.

This report is the normal final review step before PI-G is run.

### Parameters

| Field | Options | Notes |
|---|---|---|
| **Year / Phys Inv No** | Entered or selected from lookup | Defaults to latest on file. |
| **Report Type** | Standard report or uncounted parts exception | Uncounted parts are items frozen with on-hand quantity that have received no tag record. For Type 1 inventories, zero-quantity tag records must be entered for these in PI-C. The Physical Inventory Value report includes total value of counted items, frozen items, and the adjustment value. |
| **Sort order** | `P` = by item number; `C` = by item class | |
| **Cost basis for unposted parts** | `F` = frozen cost; `C` = current average cost | Items already posted through PI-G always print at frozen cost. On FIFO or LIFO costing, items always print and post at current average cost to avoid discrepancies with FIFO/LIFO cost buckets. |
| **Tag detail** | `Y` = print all tag detail; `N` = no tag detail; `L` = tag detail for lot/serial items only | |
| **Print lot/serial correction detail** | `Y` / `N` | Whether to print detail of corrections made to lot and serial items. |
| **Include uncounted parts** | `Y` / `N` | If uncounted items have no on-hand quantity, zero-quantity tag records should be entered in PI-C before including them. |

After completing selection criteria, a **Locations** tagging screen appears. Tag the appropriate locations and click **Go** to print.

---

## PI-G — Update Actual Inventory

*Source: [pi-g_update_actual_inventory.htm](../../../samples/chm/extracted/pi-g_update_actual_inventory.htm)*

**Purpose.** Use this program to post the physical inventory results. The program replaces on-hand quantities and average costs in the inventory files with the counts and costs from the physical inventory, and creates adjusting transactions for any differences between frozen quantities and counted quantities. Optionally, the General Ledger is updated to record the cost impact.

### Parameters

| Field | Options | Notes |
|---|---|---|
| **Year / Phys/Inv No** | Entered or selected from lookup | Defaults to latest on file. |
| **Adjustment cost basis** | `F` = frozen cost; `C` = current average cost | Little practical difference unless considerable time has passed since the freeze. Accountants generally prefer frozen cost because it was in effect at freeze time. On FIFO or LIFO costing, adjustments are always made at current average cost. |
| **Update General Ledger?** | `Y` / `N` | See GL impact section below. |

### GL Impact (when Update General Ledger = Y)

An entry is made to the GL **Other** journal for each item number where quantity changed:

| Direction | Asset (Inventory) Account | Cost of Goods Sold Account |
|---|---|---|
| Inventory value **increased** | Debit | Credit |
| Inventory value **decreased** | Credit | Debit |

The Asset account and COGS account used are those defined for the item's **item class**.

**Alternative — manual GL entry:** If you prefer a single consolidated manual journal entry rather than per-item automated postings, answer `N` to the Update General Ledger prompt. Then make a manual journal entry for the **Difference** total found at the end of the Physical Inventory Value report (PI-F).

### Processing

After completing selection criteria, a **Locations** tagging screen appears. Tag the appropriate locations and click **Go** to begin processing. When finished, the program optionally prints the **Physical Inventory Detail** report listing the items that were updated.

---

## PI-H — Purge Physical Inventory

*Source: [pi-h_purge_physical_inventory.htm](../../../samples/chm/extracted/pi-h_purge_physical_inventory.htm)*

**Purpose.** Use this program to remove physical inventory records from the file. Each physical inventory stays on file indefinitely until purged. Old physical inventories can be retained for reference as long as desired.

**Restriction:** An item number cannot be deleted in IN-B (Enter Inventory) while it remains in a physical inventory that has not yet been purged.

### Operation

1. Enter **Year** and **Phys/Inv No** to purge, or select from lookup.
2. A **Locations** tagging screen appears. Tag the locations to include in the purge, then click **Go**.
3. Before purging, you are given one last opportunity to print the **Physical Inventory Detail** report, which lists the items about to be purged.
4. The program deletes each record in the file one by one until complete.

---

## Cross-references

| Module | Relationship |
|---|---|
| **IN — Inventory** | PI operates on the inventory master file. On-hand quantities and average costs written back by PI-G go directly into the inventory records. New part numbers discovered during counting are created via PI-C and become IN records. Item numbers cannot be deleted from IN-B while they exist in an unprocessed physical inventory (PI-H must be run first). |
| **GL — General Ledger** | PI-G optionally posts adjusting entries to the GL Other journal, debiting/crediting the Asset (Inventory) account and Cost of Goods Sold account defined on the item's item class. |
| **JC / WO — Job Costing / Work Orders** | WIP inventory is outside PI scope. Use JC-P (Print Materials in WIP) for WIP counts; use WO-G (Issue Materials) for WIP adjustments. |
| **Cycle Codes** | PI-A supports filtering by Cycle Code, enabling cycle counting (partial, rotating counts) as an alternative to full physical inventory shutdowns. |
