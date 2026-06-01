# WC — Warehouse Control

Status: verified (text distilled from the vendor's help file).

*Source: EvoHELP.CHM → Items → Warehouse Control (5 topics).*
*Extracted HTML in [samples/chm/extracted/](../../../samples/chm/extracted/).*

---

## Contents

- [WC-A — Enter Warehouse Bin Locations](#wc-a--enter-warehouse-bin-locations)
- [WC-B — Assign Warehouse Control](#wc-b--assign-warehouse-control)
- [WC-C — Assign Bin Locations to Items](#wc-c--assign-bin-locations-to-items)
- [WC-E — Print Bin Inventory Listing](#wc-e--print-bin-inventory-listing)
- [WC-F — Warehouse Control Exceptions Report](#wc-f--warehouse-control-exceptions-report)
- [Cross-references](#cross-references)

---

## WC-A — Enter Warehouse Bin Locations

*Source: [wc-a_enter_warehouse_bin_locations.htm](../../../samples/chm/extracted/wc-a_enter_warehouse_bin_locations.htm)*

**Purpose.** Use this program to enter the master list of Bins and Shelves that will be assigned to items in each Warehouse. This is the setup step that defines all valid bin/shelf identifiers before they can be linked to inventory items.

### General Program Operation

Bin Location records are the master table of physical bin and shelf designators within each warehouse. They must exist before they can be assigned to items, though they can also be created on-the-fly within WC-C.

#### Adding a record

Click **ADD** and enter the following:

| Field | Description |
|---|---|
| **Warehouse Location** | The warehouse to which this bin belongs. |
| **Bin or Shelf** | The bin or shelf identifier (the physical location label). |
| **Description** | Optional free-text description of the bin or shelf. |

Note: Bin Locations can also be created inline as they are assigned to items in [WC-C Assign Bin Locations to Items](#wc-c--assign-bin-locations-to-items). It is not necessary to pre-populate this master list before using WC-C, but doing so is useful for larger warehouses where consistent bin naming is important.

#### Editing a record

Click **EDIT**, enter the desired changes, and click **Save** or press **F10**.

#### Deleting a record

Click **DELETE** or press **F4** and confirm the deletion. Deleting a master Bin record removes it from the bin master table. Note that deleting here removes the master record; to remove only the assignment of a bin to a specific item without deleting the master, use WC-C instead.

---

## WC-B — Assign Warehouse Control

*Source: [wc-b_assign_warehouse_control.htm](../../../samples/chm/extracted/wc-b_assign_warehouse_control.htm)*

**Purpose.** Use this program to turn Warehouse Control on or off by part number and Warehouse Location. This is the switch that determines whether bin-level tracking is enforced for a given item at a given warehouse.

### General Program Operation

Warehouse Control can be enabled, enabled with quantity-only tracking, or disabled on a per-item, per-warehouse basis. Two assignment methods are provided.

#### Assigning Individual Items

Enter an **Item Number** and set the **Warehouse Control** flag to one of the following values:

| Value | Meaning |
|---|---|
| `Y` | Warehouse Control is on — bin-level tracking is required for this item. |
| `Q` | Warehouse Control is on in quantity-only mode. |
| `N` | Warehouse Control is off for this item. |

When the value is `Y` or `Q`, an additional prompt allows you to indicate whether Warehouse Control applies to **all Warehouse Locations** or only **specific Location(s)**. If specific locations are chosen, a selection screen allows you to pick which location(s) will require Warehouse Control for this item.

#### Assigning Ranges of Items

To assign Warehouse Control to many items at once, click the **Ranges** button and enter selection criteria:

| Filter | Description |
|---|---|
| **Item Number range** | First and last item number in the range to update. |
| **Class** | Filter by item class. |
| **Category** | Filter by item category. |
| **Type** | Filter by item type. |
| **Warehouse Locations** | Which warehouse locations the assignment applies to. |

The range operation sets Warehouse Control on or off for all items matching the specified criteria in a single pass, which is useful during initial setup when enabling Warehouse Control across an existing item catalog.

---

## WC-C — Assign Bin Locations to Items

*Source: [wc-c_assign_bin_locations_to_items.htm](../../../samples/chm/extracted/wc-c_assign_bin_locations_to_items.htm)*

**Purpose.** Use this program to assign specific Bins to items by Warehouse Location. This is the operational step that maps a physical bin to an inventory item within a given warehouse, including designating a default bin.

### General Program Operation

Each item can have multiple bin assignments within a warehouse. One bin is designated the **Default Bin** for that item. When Warehouse Control is first turned on for an item, the existing Bin Location previously entered in **IN-B** (Inventory item setup) is automatically assigned as the Default Bin for that item.

#### Assigning a Bin

Click **Add** and enter the following:

| Field | Description |
|---|---|
| **Warehouse Location** | The warehouse where the bin is located. Use the Lookup to select from previously entered warehouses. |
| **Bin** | The bin identifier within that warehouse. Use the Lookup to select from previously entered bins. |
| **Item Number** | The inventory item to assign to this bin. |
| **Default Bin** | Indicate `Y` or `N` — whether this bin is the default bin for the item. |

New Bins can also be created on this screen as they are assigned to items; it is not required to pre-define all bins in WC-A first.

#### Editing an Existing Bin

Click **Edit**, make the desired changes, and save.

#### Deleting a record

Click **DELETE** or press **F4** and confirm the deletion. This operation deletes the **assignment** of the item to the bin — it does not delete the master Bin record itself. To delete the master Bin record (the bin definition that appears in lookups), use [WC-A Enter Warehouse Bin Locations](#wc-a--enter-warehouse-bin-locations).

#### Importing Bin Assignments

Bin assignments can be loaded in bulk from an external file:

1. Click **Import**.
2. Enter the name of the import file (comma-delimited or fixed-length format accepted).
3. Specify the conflict behavior:
   - **Skip** — leave existing bin assignments unchanged if a matching record is found.
   - **Replace** — overwrite existing bin assignments with the imported data.
4. Indicate the file format: **comma delimited** or **fixed length**.
5. Enter column/field position information as prompted. Required fields are marked on screen.

This import facility is intended for initial data load or bulk updates from a spreadsheet or warehouse management extract.

---

## WC-E — Print Bin Inventory Listing

*Source: [wc-e_print_bin_inventory_listing.htm](../../../samples/chm/extracted/wc-e_print_bin_inventory_listing.htm)*

**Purpose.** Use this program to list the quantity on hand for items broken down by Bin within each Warehouse Location. This is the primary operational report showing where inventory physically sits within the warehouse at the bin level.

### General Program Operation

Before printing, configure the following options:

**Sort order** — choose one of three sequences:

| Sort Option | Description |
|---|---|
| `Warehouse / Bin / Item` | Groups output by warehouse, then by bin within each warehouse, then by item within each bin. Useful for physical warehouse walks. |
| `Warehouse / Item` | Groups output by warehouse, then by item. Useful for item-centric lookups without bin detail grouping. |
| `Item / Warehouse / Bin` | Groups output by item first, then warehouse, then bin. Useful for cross-warehouse item inquiries. |

**Filters** — apply desired criteria to limit the report output (specific items, classes, categories, etc. — exact filter fields are set on the report parameters screen).

**Warehouse scope** — choose to include **all Warehouses** or select only **specific warehouses** to include in the report.

The report shows on-hand quantity at the bin level, giving warehouse staff a bin-by-bin picture of inventory for picking, receiving, and cycle count purposes.

---

## WC-F — Warehouse Control Exceptions Report

*Source: [wc-f_warehouse_control_exceptions_report.htm](../../../samples/chm/extracted/wc-f_warehouse_control_exceptions_report.htm)*

**Purpose.** Use this program to identify items where the inventory on-hand quantity (as recorded in the inventory master) does not match the total of all bin quantities for that item. Discrepancies indicate that bin-level records and the inventory master are out of sync and require reconciliation.

### General Program Operation

This is a data-integrity report. It surfaces exceptions only — items where the sum of all bin quantities differs from the item's total on-hand quantity. Items where the two figures agree are not listed.

Configure the following before printing:

**Filters** — apply desired criteria to limit which items are checked (specific item ranges, classes, categories, etc.).

**Warehouse scope** — choose to include **all Warehouses** or select only **specific warehouses**.

### Usage Notes

- Run this report after any bulk import of bin assignments, after physical inventory adjustments, or any time bin counts are manually updated outside of normal transaction flow.
- Exceptions on this report typically require either a bin quantity adjustment in WC-C or an inventory adjustment in the Inventory module to bring the two figures back into agreement.
- This report is a companion to the WC-E Bin Inventory Listing; WC-E shows what the bins contain, while WC-F shows where bins and inventory totals disagree.

---

## Cross-references

| Module | Relationship |
|---|---|
| **IN — Inventory** | Inventory items are defined in IN. The existing Bin Location field in IN-B (item setup) is used as the seed Default Bin when Warehouse Control is first enabled for an item via WC-B. Inventory on-hand quantities compared in WC-F originate from the IN module. |
| **HH — Hand Held Data Collection** | The HH module uses Warehouse Control bin assignments when performing handheld-driven inventory transactions. Bin data set up in WC-A through WC-C drives the location prompts in handheld workflows. |
| **PI — Physical Inventory** | Physical inventory counts can be taken at the bin level when Warehouse Control is active. Discrepancies found in WC-F after a physical inventory pass indicate records needing adjustment. |
| **SO — Sales Orders** | When filling sales orders, Warehouse Control bin assignments guide pick-list generation, directing warehouse staff to the correct bin location for each line item. |
| **WO — Work Orders** | Work order material issues can reference bin locations when Warehouse Control is enabled for the issued items. |
