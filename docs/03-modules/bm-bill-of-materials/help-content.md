# BM — Bills of Material

Status: verified (text distilled from the vendor's help file).

*Source: EvoHELP.CHM → Items → Bills of Material (16 topics).*
*Extracted HTML in [samples/chm/extracted/](../../../samples/chm/extracted/).*

---

## Contents

1. [BM-A — Enter Bills of Material](#bm-a--enter-bills-of-material)
2. [BM-B — Print Bills of Material](#bm-b--print-bills-of-material)
3. [BM-C — Print Where Used](#bm-c--print-where-used)
4. [BM-D — Print BOM Availability](#bm-d--print-bom-availability)
5. [BM-E — Global Replace](#bm-e--global-replace)
6. [BM-F — Global Delete](#bm-f--global-delete)
7. [BM-G — Print/Rollup Standard Costs](#bm-g--printrollup-standard-costs)
8. [BM-H — Print BOM at Average Cost](#bm-h--print-bom-at-average-cost)
9. [BM-I — Print Summarized BOM](#bm-i--print-summarized-bom)
10. [BM-J — Enter Approved Substitutes](#bm-j--enter-approved-substitutes)
11. [BM-K — Enter Approved Vendors](#bm-k--enter-approved-vendors)
12. [BM-L — Enter Approved Manufacturers](#bm-l--enter-approved-manufacturers)
13. [BM-N — BOM Availability Tree](#bm-n--bom-availability-tree)
14. [BM-P — Print BOM Pick List](#bm-p--print-bom-pick-list)
15. [BM-Q — Roll Up Where Used](#bm-q--roll-up-where-used)
16. [BM-R — Print BOM for Quoting](#bm-r--print-bom-for-quoting)

---

## BM-A — Enter Bills of Material

*Source: [bm-a_ener_bills_of_material.htm](../../../samples/chm/extracted/bm-a_ener_bills_of_material.htm)*

**Purpose.** Use this program to enter your bills of material. Inventory items created in IN-B (Enter Inventory) are used here to define parent and component parts. Each bill of materials must have a parent part — the inventory item number used to reference this BOM. Below the parent are components: the individual elements of the bill of material. Components may be purchased parts, subassemblies, phantom assemblies, non-inventory items, make-from parts, labor, and outside processing. Subassemblies and phantom assemblies are defined with their own bills of material.

### Field Explanations

| Field | Description |
|---|---|
| **Parent Part** | The item number in the inventory file for this finished good, subassembly, phantom assembly, make-from, or selling kit. The inventory type, product description, and total standard cost display automatically. |
| **Lin** | Optional line number that determines the sort order of components on the shop traveler or screen. Duplicate line numbers are allowed; within the same group the components sort in item number order. Three character, numeric field. Use the *Auto Assign Lin Nums* button (F7) to assign numbers automatically after entry, preserving the order components were entered. |
| **Component** | The item number from the inventory file for a component in the bill of materials. |
| **T** | The inventory type of each component, displayed automatically when the component is entered. Valid types: `N` = non-inventory, `R` = regular, `F` = finished good, `A` = subassembly, `M` = make-from, `L` = labor, `T` = outside processing, `B` = phantom assembly, `O` = option. |
| **Description** | The inventory description for the component; filled in automatically. |
| **Quantity Per** | How many units of each component are required to make one unit of the parent part. Default is `1.00000000`. |
| **Scrap** | Optional. Specifies a scrap percentage or fixed quantity (`Q`). Ten percent scrap is entered as `10.00`. Scrap is added to the quantity required when Print/Rollup Standard Costs is run. When a work order is firmed, the component's quantity required is increased by the scrap amount. Note: the scrap calculation does not round up to the nearest whole number, so fractional on-hand quantities can result — the scrap percentage is not well suited to discrete components. |
| **Seq** | Optional sequence number in the parent part's routing at which this component is needed. If specified, material optionally prints on the shop traveler within that sequence. Supports backflushing by sequence: components tied to a sequence are automatically relieved from on-hand inventory when completed parts are reported for that sequence in WO-F (Enter Labor). |
| **Rt#** | Optional routing number. The system supports multiple printed routings for the same work order so that particular departments only see the sequences and components pertaining to their work. |
| **Reference** | Memo field for additional information about the component, such as a drawing bubble number. Twenty character, alphanumeric field. |
| **Include when backflushing parent assembly** | Enter `N` to exclude this component from backflushing at WO-I (Enter Finished Production) for a scrapped parent item — for example, packaging materials that would not be used on a scrapped item. Default is `Y`. |

### General Program Operation

#### New Bill of Material Entry

Enter a parent item number by typing it or using the Lookup button (F2). Only `F`, `A`, `B`, `K`, or `M` type items are allowed as parents. `R`, `L`, or `T` type inventory items cannot have bills of material. If the item cannot be found, create it first in IN-B.

If the item exists, the inventory type and product description are displayed automatically. If a bill of material already exists for the item number, its components are displayed.

To add a component, click *Add*. Enter a line number or press Enter to skip. Type in the component item number or use F2/Lookup. Enter the quantity per (default 1.00000000), an optional scrap percentage, an optional sequence number, an optional routing number, and an optional reference. Indicate whether the item is to be included when backflushing scrap assemblies (default Yes).

The same component can be entered twice within a bill of material. The program will issue a warning but will allow the entry.

You remain on the entry screen until you click *Exit*, which returns you to the components list from which you can add, edit, or exit to enter another parent part.

To limit changes to items released for production, assign users Security Code `E` (Engineer) in PS-A (System Users/Passwords). Users with Security Code E can only create and edit Bills of Material for parent items with Active Status `E`.

#### Entering Remarks

While a component is highlighted in the components listing, click the *Line Remarks* button to enter up to 15 lines of remarks on each component. Remarks optionally print on the shop traveler and bill of material reports.

#### Entering BOM Notes

Click the *Notes* button while on the components listing or editing screen to enter unlimited notes against the parent part of any bill of material. BOM notes optionally print on the shop traveler and bill of material reports.

#### Copy Feature

A copy feature allows you to copy all or selected components from another bill of material. While on the components listing screen, click the *Copy* button, enter the parent part from which to copy, and choose whether to copy the BOM notes, all or selective components, and whether accompanying remarks are to be copied. Multiple copy operations can be performed in sequence to merge several bills of material into one.

#### Automatic Line Numbering

Enter components in the desired order and click *Auto Assign Lin Nums* (F7) to automatically assign line numbers that preserve the entry order. Useful when a specific sequence other than item number order is required.

#### Deleting a Bill of Material Component

Highlight the component in the components listing screen and click the *Delete* button at the bottom of the screen.

#### Deleting a Complete Bill of Materials

Click the *Delete* button at the upper left of the components listing screen to delete an entire bill of materials.

---

## BM-B — Print Bills of Material

*Source: [bm-b_print_bills_of_materials.htm](../../../samples/chm/extracted/bm-b_print_bills_of_materials.htm)*

**Purpose.** This program prints a list of your bills of material. The report includes the parent item number, description and type, component item numbers, descriptions, types, quantity pers, scrap percentages, sequences, routing numbers, and reference fields. If sub-assemblies are selected, the bill of materials for each assembly or phantom assembly is included. For a listing with standard costs, use BM-G (Print/Rollup Standard Costs), which produces a multi-level, costed bill of material.

### General Program Operation

Enter a range of parent item numbers or select via Lookup (F2). Options include:

- **Second description line:** indicate whether to print for `P` (Parent only), `C` (Components only), or `A` (both).
- **Specifications, BOM remarks, BOM notes:** indicate whether each is to print.
- **Multiple levels:** if Yes, components are included for every subassembly and phantom assembly down through up to 35 levels of the product structure. Each component is identified by its level in the product structure. Specify the number of levels to print.
- **Features and Options module:** optionally print features (not the actual options; use FO-B for options).
- **Approved substitutes, approved vendors, approved manufacturers:** indicate whether each is to print.
- **Quantity per decimals:** specify the number of decimal places (shortens from the standard eight decimal places for printing purposes).

---

## BM-C — Print Where Used

*Source: [bm-c_print_where_used.htm](../../../samples/chm/extracted/bm-c_print_where_used.htm)*

**Purpose.** Use this program to list all bills of material in which a specific component part appears. The report includes the component item number and description, and all parent parts, descriptions, quantities required, and reference fields. The report can be confined to a single level (only parent parts in which the component is in the first level of the bill) or can be run as a multi-level or limited-level inquiry where parent parts using the component two or more levels down in the product structure are also shown.

### General Program Operation

Enter the item number of the component part you are inquiring about, or select via Lookup (F2). Indicate the number of levels to include (up to 35) and whether or not to print for inactive parent parts.

---

## BM-D — Print BOM Availability

*Source: [bm-d_print_bom_availability.htm](../../../samples/chm/extracted/bm-d_print_bom_availability.htm)*

**Purpose.** This program lists up-to-date information on how much inventory is available for each component within a bill of material. It is useful for expediting orders, allowing a quick survey of all materials required to produce a particular assembly. The report can be run for a single level or for multiple levels (showing the status of the entire product structure).

The report includes:
- Parent item number, description, type, and quantity on hand at the selected location.
- Calculated quantity to pull from stock and quantity to assemble, based on the quantity requested.
- For each component: item number, quantity needed, quantity on hand, combined quantity on sales order and backorder, quantity allocated (required) for existing work orders, and quantity on work order or purchase order.
- An asterisk (`*`) is printed next to any component that does not have enough on-hand inventory to build the quantity requested.
- At the end of the report: a calculation of the maximum number of units that can be built based on current inventory at the selected location.

### General Program Operation

Enter the parent item number or select via Lookup (F2). Indicate whether to view multiple levels or a single level structure. Enter the inventory **Location** (use F2/Lookup for multi-location setups).

**Quantity to Project** works with the "print shortages only?" option. For example, to find out if you have enough inventory to build 10 units, enter `10` in the quantity to project field. Enter `Y` at the *Print shortages only?* field to list only components with insufficient inventory.

---

## BM-E — Global Replace

*Source: [bm-e_global_replace.htm](../../../samples/chm/extracted/bm-e_global_replace.htm)*

**Purpose.** Use this program to replace a component with another component throughout all bills of material that contain that component. For example, replacing an aluminum washer with a stainless steel washer used in hundreds of products. Rather than changing each bill of material individually, the global replace program automatically replaces the component everywhere it is used.

**Warning:** This program changes the master bill of material only and has no effect on any work orders that may already exist.

### General Program Operation

Enter the component to replace in the **Search For** field (or use F2/Lookup). Enter the replacement component in the **Replace With** field (or use F2/Lookup). Press Enter and all affected bills of material are updated automatically.

---

## BM-F — Global Delete

*Source: [bm-f_global_delete.htm](../../../samples/chm/extracted/bm-f_global_delete.htm)*

**Purpose.** Use this program to delete a component across all bills of material that contain that component. This eliminates the task of having to change each bill individually.

**Warning:** This program changes the master bill of material only and has no effect on any work orders that may already exist.

### General Program Operation

Enter the component item number in the **Delete** field (or use F2/Lookup). Press Enter and the component is deleted from all bills of material that contain it.

---

## BM-G — Print/Rollup Standard Costs

*Source: [bm-g_print_rollup_standard_costs.htm](../../../samples/chm/extracted/bm-g_print_rollup_standard_costs.htm)*

**Purpose.** Use this program to calculate and print standard costs for material, setup, labor, outside processing, fixed overhead, and variable overhead up through all levels of the bill of material. The report will optionally update these costs for the parent item number and all its related components, subassemblies, and their components in the inventory file.

This program is extremely valuable for manufacturers. It performs complex cost calculations that are difficult to maintain manually. Products can be recosted instantly to reflect changes in material or labor rates. For example, if a component used throughout many products has a changed cost, simply update the standard cost on the component, run a cost rollup, and all products that use that component are recosted.

### Two-Step Rollup Process

The cost rollup is a two-step process:

1. **Routings cost rollup** — run Print/Rollup Routings Costs first. This goes through all manufacturing sequences and calculates the values in the inventory file for setup, labor, outside processing, fixed overhead, and variable overhead.
2. **BOM cost rollup** — once the routings rollup has updated the inventory file for all assembly-type items, the BOM rollup rolls those costs, along with all costs for materials and non-inventory items, up through all levels in the product structure to arrive at a total standard cost for the top-level parent product.

This two-step process gives precise control over how and when products are recosted.

### General Program Operation

Enter a from/through range of parent item numbers or select via Lookup (F2).

- **Print Remarks and Notes?** — answer Yes to include notes and remarks on the report.
- **Save Rollup Std Cost Changes?** — answer No to calculate costs without saving to the inventory file (report only). Answer Yes to pass the updated rolled-up costs for material, setup, labor, outside processing, fixed overhead, variable overhead, and total standard cost to the inventory file record for the parent item number.
- **Print Product Descriptions?** — answer `N` to suppress component product descriptions, cutting the report length in half.

---

## BM-H — Print BOM at Average Cost

*Source: [bm-h_print_bom_at_average_cost.htm](../../../samples/chm/extracted/bm-h_print_bom_at_average_cost.htm)*

**Purpose.** Use this program to get a rolled-up cost for a parent part at current average or last cost, rather than at standard cost. This is useful for assessing a product's cost based on already-incurred inventory costs of its components, as opposed to fixed standard costs that represent what a product should cost.

This report includes only a single level of the BOM because the average and last cost of the components are already inclusive of lower-level component costs.

### General Program Operation

Select bills of material by entering a range of parent item numbers or via Lookup (F2). Options include:

- **Second description line and specifications:** `P` for Parent only, `C` for Components only, `A` for both.
- **Remarks and notes:** indicate whether to print.
- **Cost to use:** average cost or last cost.
- **Decimal places:** desired number of decimal places for quantities.

---

## BM-I — Print Summarized BOM

*Source: [bm-d_print_summarized_bom.htm](../../../samples/chm/extracted/bm-d_print_summarized_bom.htm)*

**Purpose.** Use this program to get a single-level bill of material listing where each component — no matter how many times it is separately listed within a bill of material — is summarized into a single quantity. The report can be limited to a single level or can include all levels of the product structure.

### General Program Operation

Enter a range of parent item numbers or select via Lookup (F2). Indicate whether to print the second description line.

- **Single level or multi-level:** if multi-level, all instances of each component through all levels of the product structure are rolled into a single quantity. Remarks, approved substitutes, approved vendors, and approved manufacturers cannot be printed on the multi-level version.
- **Specifications, BOM remarks, BOM notes:** available on single-level reports only.
- **Features and Options module:** optionally print features (not the actual options; use FO-B for options).
- **Approved substitutes, approved vendors, approved manufacturers:** available on single-level reports only.
- **Quantity per decimals:** specify the number of decimal places (shortens from the standard eight for printing purposes).

---

## BM-J — Enter Approved Substitutes

*Source: [bm-j_enter_approved_substitutes.htm](../../../samples/chm/extracted/bm-j_enter_approved_substitutes.htm)*

**Purpose.** Use this program to enter approved substitute parts on any bill of material component. A substitute part is another inventory item that can be used in place of a particular component when no stock is available for that component.

Substitute parts can be defined at three levels of scope:

| Scope | How to configure |
|---|---|
| **Global** | Applies within any bill of material. Leave *Parent Part No* and *Customer Code* blank. |
| **By parent item number** | Applies only within a particular assembly. Enter a *Parent Item number*. |
| **By customer** | Applies only within a particular customer's products (job shop use). Enter a *Customer Code*. |

These substitute parts can optionally print within BM-B (Print Bills of Material), BM-I (Print Summarized Bill of Material), and WO-D (Print Pick Lists). During production, substitute parts can be swapped into the work order BOM through WO-K-E (Swap Substitute Parts).

### General Program Operation

Enter the **Std Item number** (the standard component item number within the bill of material). Set the scope by leaving *Parent Part No* and *Customer Code* blank for global substitutes, or filling in the appropriate field for assembly- or customer-specific substitutes. Each unique combination of *Std Item number*, *Parent Part No*, and *Customer Code* defines a separate substitute record — you can define many such combinations for the same standard component.

#### Entering Substitutes

After defining the key combination, enter substitute item numbers in the entry area at the bottom of the screen. Use F2/Lookup to select. Substitutes must be pre-defined in IN-B (Enter Inventory). Save each record. Multiple substitutes can be entered for the same record.

To delete an existing substitute: with the cursor in the *Substitute Part* field, click *Display Lines* to get a listing, highlight the substitute, press Enter to bring it into the entry area, then click *Delete* (F4).

---

## BM-K — Enter Approved Vendors

*Source: [bm-k_enter_approved_vendors.htm](../../../samples/chm/extracted/bm-k_enter_approved_vendors.htm)*

**Purpose.** Use this program to enter approved vendors on any bill of material component, with sophisticated control at the customer and/or bill of material level. If all you need is approved vendors by item (without BOM-level or customer-level control), use PO-L (Assign Vendors to Items) instead. For more information on using approved vendors, see the help topic "How to Use Approved Vendors and Manufacturers."

Approved vendors can be designated at three levels:

| Scope | How to configure |
|---|---|
| **Global** | Applicable within any bill of material. Leave *Parent Part No* and *Customer Code* blank. |
| **By parent item number** | Designated only within a particular assembly. Enter a *Parent Item number*. |
| **By customer** | Approved only for a particular customer's products (job shop use). Enter a *Customer Code*. |

You can also enter the vendor's item number as a cross-reference to your item number. When entering a purchase order for that vendor, the vendor item number will appear as a comment line following entry of your item number.

Approved vendors can optionally print within BM-B (Print Bills of Material) and BM-I (Print Summarized Bill of Material).

### General Program Operation

Enter the **Std Item number**. Set scope by leaving *Parent Part No* and *Customer Code* blank for global, or filling in the appropriate field. Each unique combination of *Std Item number*, *Parent Part No*, and *Customer Code* defines a separate approved vendor record.

#### Entering Vendors and Vendor Item Numbers

After defining the key combination, enter vendor codes in the entry area at the bottom of the screen. Use F2/Lookup to select. Vendors must be pre-defined in AP-A (Enter Vendors). The vendor name is displayed automatically. Enter the vendor's item number for the component if applicable (25 character alphanumeric field). Save each record.

To delete an existing approved vendor: with the cursor in the *Vend Code* field, click *Display Lines*, highlight the vendor, press Enter, then click *Delete* (F4). Alternatively, navigate using the standard search keys: *First* (F5), *Last* (F6), *Previous* (F7), *Next* (F8).

---

## BM-L — Enter Approved Manufacturers

*Source: [bm-l_enter_approved_manufacturers.htm](../../../samples/chm/extracted/bm-l_enter_approved_manufacturers.htm)*

**Purpose.** Use this program to specify approved manufacturers in the purchasing process. Use this program to enter approved manufacturers on any bill of material component. For more information on using approved manufacturers, see the help topic "How to Use Approved Vendors and Manufacturers."

Approved manufacturers can be designated at three levels:

| Scope | How to configure |
|---|---|
| **Global** | Applicable within any bill of material. Leave *Parent Part No* and *Customer Code* blank. |
| **By parent item number** | Designated only within a particular assembly. Enter a *Parent Item number*. |
| **By customer** | Approved only for a particular customer's products (job shop use). Enter a *Customer Code*. |

You can also enter the manufacturer's item number as a cross-reference to your item number. When entering a purchase order, the manufacturer item number will appear as a comment line following entry of your item number.

Approved manufacturers can optionally print within BM-B (Print Bills of Material) and BM-I (Print Summarized Bill of Material).

### General Program Operation

Enter the **Std Item number**. Set scope as described above. Each unique combination of *Std Item number*, *Parent Part No*, and *Customer Code* defines a separate approved manufacturer record.

#### Entering Manufacturers and Manufacturer Item Numbers

After defining the key combination, enter manufacturer names in the entry area at the bottom of the screen. Unlike vendors, manufacturers do not have to be set up in the vendor file — enter the name directly. If the manufacturer has their own item number for the standard component, enter it (25 character alphanumeric field). Save each record. Multiple manufacturers can be entered for the same record.

To delete an existing manufacturer: with the cursor in the *Manufacturer's Name* field, click *Display Lines*, highlight the manufacturer, press Enter, then click *Delete* (F4). Alternatively, navigate using: *First* (F5), *Last* (F6), *Previous* (F7), *Next* (F8).

---

## BM-N — BOM Availability Tree

*Source: [bm-n_bom_availability_tree.htm](../../../samples/chm/extracted/bm-n_bom_availability_tree.htm)*

**Purpose.** Use this program to view an item's bill of materials in a tree view with visual indications of component stock status and availability. This is a Java-based graphical program requiring an ODBC data connection.

### General Program Operation

The program loads with a list of potential parent items. Select the top-level parent to view — searchable by either Item Code or Description. Identify the Location(s) to consider. If checking availability of components to manufacture additional units beyond current requirements, enter a quantity.

The BOM displays in a tree view:
- **Green** — component has available stock.
- **Red** — component has a shortage.
- **Blue** — component is not on-hand but has been ordered (only when *Display Future Supply* is selected).

**Future supply options:**
- *Include Future Supply* — items on purchase order and work order are included as available supply when calculating shortages.
- *Ignore Future Supply* — only on-hand quantity is considered.
- *Display Future Supply* — items ordered but not on hand display as blue.

The right side of the screen displays each component's stock status and the detail of open orders.

**Setup requirement:** See the ODBC Data Connection help topic for information on setting up the database for the Java programs.

---

## BM-P — Print BOM Pick List

*Source: [bm-p_print_bom_pick_list.htm](../../../samples/chm/extracted/bm-p_print_bom_pick_list.htm)*

**Purpose.** Use this program to create a pick list for some quantity of an assembly without specifying a work order number. Use this when building multiple assemblies together where the range of work order numbers is not consecutive, making the work-order combined pick list in WO-D unsuitable.

### General Program Operation

Enter the assembly number, quantity, component types to include, and whether to consolidate quantities of common components.

---

## BM-Q — Roll Up Where Used

*Source: [bm-q_roll_up_where_used.htm](../../../samples/chm/extracted/bm-q_roll_up_where_used.htm)*

**Purpose.** Use this program to roll up the standard cost of all parent parts that use a specified component or range of components whose standard cost has changed. This is a targeted cost rollup that propagates a component cost change upstream through all assemblies that use it, without requiring a full BOM-G rollup of all items.

### General Program Operation

Enter the range of component parts and process.

---

## BM-R — Print BOM for Quoting

*Source: [bm-r_print_bom_for_quoting.htm](../../../samples/chm/extracted/bm-r_print_bom_for_quoting.htm)*

**Purpose.** Use this program to generate a list of components for a given top-level assembly and the total quantity of each needed for up to six quantity breaks. The report includes on-hand quantity, manufacturer, manufacturer part number, and any approved substitutes. For purchased items, the last PO number, cost, quantity, date, and vendor are listed. This report is designed to support the quoting process by presenting BOM cost data at multiple volume levels.

### General Program Operation

Enter the parent part, quantity breaks desired, an optional quote number, and filters for Component Item Class, Category, and Type.

---

## Cross-references

The Bills of Material module is central to manufacturing operations in EvoERP. It is tightly linked to:

- **IN — Inventory** (`docs/03-modules/in-inventory/`): All parent and component items must first be created in IN-B (Enter Inventory). Inventory type codes (`F`, `A`, `B`, `M`, `K` for parents; `R`, `N`, `L`, `T` etc. for components) are defined there. Standard costs are stored in the inventory master and updated by BM-G.

- **WO — Work Orders** (`docs/03-modules/wo-work-orders/`): Work orders are created from the master BOM. BOM components drive pick lists (WO-D), backflushing in WO-F (Enter Labor) and WO-I (Enter Finished Production), and the work order traveler. Approved substitutes defined in BM-J can be swapped into work order BOMs via WO-K-E.

- **MR — Material Requirements Planning** (`docs/03-modules/mr-mrp/`): MRP explodes the BOM to calculate component requirements based on planned production. The accuracy of BOM quantity-per and scrap fields directly drives MRP demand quantities.

- **ES — Estimating** (`docs/03-modules/es-estimating/`): BOM structures are used in estimating to price out assemblies. BM-R (Print BOM for Quoting) bridges the BOM module directly to quoting workflows.

- **RO — Routings** (`docs/03-modules/ro-routings/`): BOM sequence fields (the *Seq* column) tie components to routing operation sequences, enabling backflushing by sequence and component placement on the shop traveler at the correct operation. The routings cost rollup (Step 1 of BM-G) must precede the BOM cost rollup (Step 2).

- **PO — Purchase Orders** (`docs/03-modules/po-purchase-orders/`): Approved vendor cross-references entered in BM-K appear as comment lines on purchase orders. PO-L (Assign Vendors to Items) is the simpler alternative when BOM-level vendor control is not needed.

- **FO — Features and Options** (`docs/03-modules/fo-features-options/`): BM-B and BM-I can optionally print feature definitions within BOM reports. Full options listings require FO-B.

### Global Maintenance Utilities

Two programs — **BM-E (Global Replace)** and **BM-F (Global Delete)** — operate across all master BOMs in one pass. Both affect the master BOM file only; existing work orders are not changed. These are powerful and irreversible operations: use with care.
