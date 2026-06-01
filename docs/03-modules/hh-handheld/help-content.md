# HH — Hand Held Data Collection

Status: verified (text distilled from the vendor's help file).

*Source: EvoHELP.CHM → Hand Held Data Collection (15 CHM topics).*
*Extracted HTML in [samples/chm/extracted/](../../../samples/chm/extracted/).*

The Hand Held module is a suite of programs scaled for use on portable wireless hand held bar code devices such as Symbol 9000 scanners or Pocket PC with bar code reader. These programs provide real-time data regarding part movement within the facility: HH-C Issue Materials and HH-D Enter Finished Production track materials into and out of work orders; HH-A Scan & Ship validates shipments as orders are packed; HH-B Print Bar Code Labels prints bar coded labels for completed items (also called automatically from HH-D). The module also includes a full Paperless Shop Floor Tracking system (HH-I and HH-L) designed to eliminate printed Shop Travelers, Pick Lists, potentially outdated engineering drawings and test requirements, and paper labor tickets or time sheets.

---

## How to Use Paperless Shop Floor Tracking

*Source: [how_to_use_paperless_shop_floor_tracking.htm](../../../samples/chm/extracted/how_to_use_paperless_shop_floor_tracking.htm)*

The Paperless Shop Floor Tracking programs are designed to eliminate printed Shop Travelers, Pick Lists, potentially outdated engineering drawings and test requirements, and labor tickets or time sheets. There are two versions of the paperless shop floor program.

**HH-I Paperless Shop Floor Tracking** requires a computer workstation at each shop floor station. Each workstation links to all work order information based on the Work Order Number, which would be bar coded to a label or sticker applied to the pallet, box, or other container used to transport parts from station to station. Lot and Serial controlled components and assemblies are supported. At this time, only Average and Standard Costing methods are supported for material issues and Finished Production reporting — FIFO and LIFO costing are not supported.

**HH-L Multi-user Paperless Shop Floor** does not require a dedicated computer workstation at each shop floor work location. When the program is loaded, the workstation can be assigned to a work order and optionally a sequence. Once assigned, any user can view documents such as drawings linked to the work order and/or sequence. Clicking the Data Collection buttons allows multiple workers to clock in or out of labor, and transfer labels can be printed to move parts to the next sequence.

### Setting up Paperless Shop Floor Tracking

The Paperless Shop Floor system uses the standard Work Centers and Routings already assigned to parts and consequently to Work Orders, so no special setup is required. You can use Evo Links to link drawings and other engineering documents to parts or a work order so that they are accessible from the Links button on the screen.

If you have specific testing requirements and minimum results required for acceptance, you can:

- Enter the testing method at **RO-M Enter Testing Method**.
- Enter the required results linked to a given Item's Routing Sequence (where the testing is to be performed) at **RO-N Enter Test Requirements**.

---

## Contents

- [HH-A — Scan & Ship](#hh-a--scan--ship)
- [HH-B — Print Bar Code Labels](#hh-b--print-bar-code-labels)
- [HH-C — Issue Materials](#hh-c--issue-materials)
- [HH-D — Enter Finished Production](#hh-d--enter-finished-production)
- [HH-E — Enter PI Tag Counts](#hh-e--enter-pi-tag-counts)
- [HH-F — Enter Labor](#hh-f--enter-labor)
- [HH-G — Receive Purchase Order](#hh-g--receive-purchase-order)
- [HH-H — Enter Shipping Information](#hh-h--enter-shipping-information)
- [HH-I — Paperless Shop Floor Tracking](#hh-i--paperless-shop-floor-tracking)
- [HH-J — Print Work Order Label](#hh-j--print-work-order-label)
- [HH-K — Transfer Inventory](#hh-k--transfer-inventory)
- [HH-L — Multi-user Paperless Shop Floor](#hh-l--multi-user-paperless-shop-floor)
- [HH-M — Issue Scrap Component](#hh-m--issue-scrap-component)

---

## HH-A — Scan & Ship

*Source: [hh-a_scan_ship.htm](../../../samples/chm/extracted/hh-a_scan_ship.htm)*

**Purpose.** Use this program to replace SO-E Release Sales Orders as orders are packed for shipment. It validates that the items being packed are in fact on the order and that quantities are correct. Lot and/or Serial Control information can also be collected via bar code to ensure accuracy.

### General Program Operation

1. Enter the **Sales Order number** to be packed — either manually or by scanning the bar code from the packing slip or other document.
2. Indicate whether quantities packed will be counted as **Standard Pack** or **Each**.
3. As items are packed, scan each **item number**. The item number scanned can be either the Evo item number or the **UPC number** if UPC numbers are assigned to the item.
4. If applicable, you will also be prompted for **Lot** and/or **Serial numbers**.
5. Once a box has been filled, click **Verify** to confirm the box contents, print a box label, and move to the next box in the shipment.
6. The **Clear** button can either clear the current box or clear the entire order and start over.
7. Click **Save** when the order is done. The order is released and ready for invoicing.

### Behavior and Warnings

- If an item scanned is **not on the order** or the **quantity is exceeded**, a warning is given so incorrect orders are not shipped.
- The **Ship Date** saved to the order will be today based on the system clock of the terminal.
- Any items on the order not released are set to **backorder**.

### Cross-module links

- Replaces: SO-E Release Sales Orders
- Related: IN-B Enter Inventory (for UPC number assignment)

---

## HH-B — Print Bar Code Labels

*Source: [hh-b_print_bar_code_labels.htm](../../../samples/chm/extracted/hh-b_print_bar_code_labels.htm)*

**Purpose.** Use this program to print bar coded labels for items, including Lot and/or Serial number as applicable, so that the labels can be used with other scanning programs.

### Label Format Selection

This program uses the **RTM Print Group** assigned to items in IN-B Enter Inventory. You can develop variations of the standard `T7ING1.RTM` label template for different types of parts:

- Save the customized RTM as (for example) `T7ING1A.RTM`.
- Designate the parts that should use that label format as **RTM Print Group A**.
- The program will automatically use that label for those parts.

### General Program Operation

1. Enter the **quantity of labels** to print.
2. Enter the **Item Number**.
3. Enter **Lot** and **Serial Number** as applicable.
4. Click **Print**.

The Hand Held version of the program prints directly to the **default printer** without prompting for any settings.

### Related Program

There is also a full-screen variation at **IN-Q Print Labels With Lot/Serial Info** that can print a batch of labels from a list of items and Lot/Serial information imported from a text file.

### Cross-module links

- Related: IN-B Enter Inventory (RTM Print Group assignment)
- Related: IN-Q Print Labels With Lot/Serial Info (full-screen batch version)
- Called automatically from: HH-D Enter Finished Production (optionally, after production is reported)

---

## HH-C — Issue Materials

*Source: [hh-c_issue_materials.htm](../../../samples/chm/extracted/hh-c_issue_materials.htm)*

**Purpose.** Use this program to replace WO-G Issue Materials as parts are issued to Work Orders from the stockroom. Lot and/or Serial Control information can also be collected via bar code to ensure accuracy.

### General Program Operation

1. Enter or scan the **Work Order number**.
2. Scan each **component** as it is issued and enter the **quantity issued**.
3. The **transaction date** used will be today based on the system clock of the terminal.
4. If the component is **Lot** or **Serial controlled**, you will be prompted to enter or scan the Lot/Serial information.
5. Scan the next component for the same Work Order.
6. When ready to move to a new Work Order, click **Clear** and begin with a new Work Order number.

### Cross-module links

- Replaces: WO-G Issue Materials
- Related: WO (Work Orders) module for work order setup and status

---

## HH-D — Enter Finished Production

*Source: [hh-d_enter_finished_production.htm](../../../samples/chm/extracted/hh-d_enter_finished_production.htm)*

**Purpose.** Use this program to replace WO-I Enter Finished Production or WO-P Batch Finished Production to indicate completion of parts on a Work Order.

### Automated Defaults

Several behaviors are automatically driven by system defaults configured in **SD-B Work Orders Defaults** (also referred to as SD-Q IS Tech Support Defaults in some contexts) without prompting the operator:

- **Lot Control automation**: Lot Control of finished items can be automated to use the Work Order number as the Lot Number based on a default setting.
- **Backflushing of components**: whether components are backflushed automatically on production reporting.
- **Costing method**: whether Standard or Actual cost is used.
- **Work Order close logic**: whether to close the work order if the quantity complete meets the Work Order quantity.

Ensure those default settings are correct before using this program, as the operator will not be prompted to respond to questions about these behaviors.

### General Program Operation

1. Enter or scan the **Work Order number**.
2. Enter the **quantity complete**.
3. Click **Save**. The program processes the order.
4. You will then be prompted for **Lot** and/or **Serial numbers** as appropriate.
5. Based on default settings, the program will either:
   - **Prompt** for label printing, or
   - **Go directly** to the label printing program (HH-B) without prompting.

### Cross-module links

- Replaces: WO-I Enter Finished Production; WO-P Batch Finished Production
- Defaults controlled by: SD-B Work Orders Defaults / SD-Q IS Tech Support Defaults
- Triggers: HH-B Print Bar Code Labels (for label printing after production)

---

## HH-E — Enter PI Tag Counts

*Source: [hh-e_enter_pi_tag_counts.htm](../../../samples/chm/extracted/hh-e_enter_pi_tag_counts.htm)*

**Purpose.** Use this program to replace PI-C Enter Tag Counts when performing a Physical Inventory. This is the hand held equivalent of the standard Physical Inventory tag count entry program.

### General Program Operation

1. Enter **Employee Number**.
2. Confirm or change the **PI Number**, **date**, and **Location**.
3. Click **Tags** to begin entering tag counts.
4. Enter a **beginning Tag number**.
5. Then enter or scan:
   - **Item number**
   - **Quantity**
   - **Lot** and **Serial** numbers (as applicable)
   - **Bin Location** (as applicable)

### Cross-module links

- Replaces: PI-C Enter Tag Counts
- Related: PI (Physical Inventory) module

---

## HH-F — Enter Labor

*Source: [hh-f_enter_labor.htm](../../../samples/chm/extracted/hh-f_enter_labor.htm)*

**Purpose.** Use this program to replace DC-A Enter Labor Production when entering labor and production or clocking into or out of a shift.

### General Program Operation

**Clocking in:**

1. Enter or scan **Employee number**.
2. Enter **Work Order number**.
3. Enter **Sequence**.

**Clocking out:**

1. You will also be prompted for:
   - **Quantity good** completed
   - **Quantity scrapped**

**Shift clock-in/clock-out:**

- If the **Shift Start/Stop** feature is enabled, this program can also be used to clock into and out of the shift.

### Cross-module links

- Replaces: DC-A Enter Labor Production
- Related: DC (Data Collection) module
- Related: WO (Work Orders) module for work order and sequence setup

---

## HH-G — Receive Purchase Order

*Source: [hh-g_receive_purchase_order.htm](../../../samples/chm/extracted/hh-g_receive_purchase_order.htm)*

**Purpose.** Use this program to replace PO-C Receive Purchase Order. It provides a bar code-driven interface for receiving goods against an open purchase order.

### General Program Operation

1. Enter or scan the **PO Number**.
2. Enter the **receipt date**.
3. Select whether to receive to **Inventory** or **QC** (Quality Control).
4. Enter the **Packing Slip** number and **Employee number**.
5. Enter or scan the **item number**.
6. Confirm the receipt destination (Inventory vs. QC).
7. Enter the **quantity received**.
8. If the item is **Lot and/or Serial controlled** and you are receiving to **Inventory** (not QC), you will be prompted to enter or scan the Lot and/or Serial information.
9. Enter the next part number to handle multi-line PO receipts.
10. When all lines have been received, click **Save**.

### Notes

- Lot/Serial prompting only occurs when receiving directly to Inventory, not when receiving to QC.
- Multiple line receipts on a single PO are handled by continuing to enter part numbers before saving.

### Cross-module links

- Replaces: PO-C Receive Purchase Orders
- Related: PO (Purchase Orders) module
- Related: IN (Inventory) module for Lot/Serial control settings

---

## HH-H — Enter Shipping Information

*Source: [hh-h_enter_shipping_information.htm](../../../samples/chm/extracted/hh-h_enter_shipping_information.htm)*

**Purpose.** Use this program to replace SO-P-I Enter Freight & Tracking #. It provides a hand held interface for recording freight carrier and tracking number information against a shipped sales order.

### General Program Operation

1. Enter or scan the **Box ID** or **Sales Order Number**.
2. Enter or scan the **tracking number**.
3. Enter the **freight company**.
4. Enter the **freight charge**.

**Multiple boxes on a single shipment:**

- Enter the tracking number for each box individually.
- Enter the total freight charge on the **last box** only.

### Cross-module links

- Replaces: SO-P-I Enter Freight & Tracking #
- Related: SO (Sales Orders) module; SH (Scheduling/Shipping) module

---

## HH-I — Paperless Shop Floor Tracking

*Source: [hh-i_paperless_shop_floor_tracking.htm](../../../samples/chm/extracted/hh-i_paperless_shop_floor_tracking.htm)*

**Purpose.** Use this program to enable fully electronic tracking of work orders, including labor entry and material issue, links to drawings and test requirements and specifications, job status, and entry of test results, lot and serial numbers. This is the single-workstation-per-station version of the Paperless Shop Floor system.

### General Program Operation

1. If the default is **not** set to automatically use the Evo Login as the Paperless Login, log in your **Employee Number** first.
2. Scan or enter the **Work Order** and **Sequence** you will be working on.
3. The screen displays general information for the Work Order and Sequence, similar to what would be printed on a Shop Traveler.

### Available Screen Buttons

| Button | Function |
|---|---|
| **Links** | Access documents linked to the work order or parts (drawings, engineering docs via Evo Links) |
| **Notes** | View or add notes related to the work order or sequence |
| **QC Tests** | View testing requirements or report test results |
| **Issue Components** | Issue component materials to the work order |
| **Report Parts Complete** | Report finished production quantity |
| **Clock Out / Labor** | Clock out of the sequence and report labor hours |

### Costing Limitations

Only **Average** and **Standard** Costing methods are supported for material issues and Finished Production reporting. FIFO and LIFO costing are not supported.

### Lot and Serial Control

Lot and Serial controlled components and assemblies are supported.

### Cross-module links

- Related: HH-L Multi-user Paperless Shop Floor (alternative version for shared stations)
- Setup: RO-M Enter Testing Method; RO-N Enter Test Requirements
- Related: WO (Work Orders) module; DC (Data Collection) module
- See also: How to Use Paperless Shop Floor Tracking (setup overview)

---

## HH-J — Print Work Order Label

*Source: [hh-j_print_work_order_label.htm](../../../samples/chm/extracted/hh-j_print_work_order_label.htm)*

**Purpose.** Use this program to replace WO-S Print Work Order Labels. It provides a simple hand held interface to print a bar coded label for a specific work order, which can then be applied to pallets, boxes, or containers to enable scanning at subsequent shop floor stations.

### General Program Operation

1. Enter or scan the **WO Number**.
2. Enter the **quantity of labels** to print.

### Cross-module links

- Replaces: WO-S Print Work Order Labels
- Related: WO (Work Orders) module
- Used with: HH-I Paperless Shop Floor Tracking; HH-L Multi-user Paperless Shop Floor (labels printed to move parts to next sequence)

---

## HH-K — Transfer Inventory

*Source: [hh-k_transfer_inventory.htm](../../../samples/chm/extracted/hh-k_transfer_inventory.htm)*

**Purpose.** Use this program to replace IN-L-J Transfer Inventory. It provides a bar code-driven interface for transferring inventory between warehouse locations or bins.

### General Program Operation

1. Enter or scan the **Item Number**.
2. Enter the **From Warehouse Location**.
3. Enter the **To Warehouse Location**.
4. Enter the **quantity** to transfer.
5. Enter the **transaction date** (defaults to the current date).
6. If **Warehouse Control** is enabled:
   - Enter the **From Bin Location**.
   - Enter the **To Bin Location**.
7. If **Lot or Serial control** applies, enter or scan the appropriate **Lot/Serial** information.

### Cross-module links

- Replaces: IN-L-J Transfer Inventory
- Related: IN (Inventory) module for warehouse and bin location setup and Lot/Serial control settings

---

## HH-L — Multi-user Paperless Shop Floor

*Source: [hh-l_multi-user_paperless_shop_floor.htm](../../../samples/chm/extracted/hh-l_multi-user_paperless_shop_floor.htm)*

**Purpose.** Use this program to enable fully electronic tracking of work orders including labor entry and material issue, links to drawings and specifications, and job status. This version does **not** require a dedicated computer workstation at each shop floor work location — a single shared workstation can be assigned to different work orders as needed.

### General Program Operation

1. Enter a **Work Order number** and **sequence**.
2. The work order and sequence information displays on the screen.
3. Use the buttons across the top of the screen to perform actions:

| Button | Function |
|---|---|
| **Clock In** | Clock a worker into the work order/sequence |
| **Clock Out** | Clock a worker out and record labor |
| **Report Parts Completed** | Enter quantity of finished production |
| **Issue Components** | Issue component materials to the work order |
| **Print Labels** | Print transfer labels to move parts to the next sequence |
| **Enter Inspection Results** | Record inspection or QC results |

### Key Difference from HH-I

In HH-L, multiple workers can share a single workstation — any user can clock in or out against the currently displayed work order/sequence without each worker having their own dedicated station. This is the recommended approach when a dedicated workstation at every shop floor position is not practical.

### Cross-module links

- Related: HH-I Paperless Shop Floor Tracking (single-user, dedicated-workstation version)
- Related: WO (Work Orders) module; DC (Data Collection) module
- See also: How to Use Paperless Shop Floor Tracking (setup overview)

---

## HH-M — Issue Scrap Component

*Source: [hh-m_issue_scrap_component.htm](../../../samples/chm/extracted/hh-m_issue_scrap_component.htm)*

**Purpose.** Use this program to document the scrapping of a component previously issued to a work order when that component cannot be immediately replaced via a Scrap Replacement in WO-G Issue Materials. By recording the scrap here, the open allocation is recreated and purchasing is alerted to purchase a replacement.

### Important Distinction

This program does **NOT** actually issue material to the work order. It moves the quantity entered to a **Scrap quantity**, resetting the open allocation for the replacement component.

### General Program Operation

1. Enter the **Work Order Number**.
2. Enter the **Component** (item number of the component being scrapped).
3. Enter the **Scrap quantity**.
4. Enter the **Scrap Code**.

The system recreates the open allocation for the scrapped component so that purchasing can identify the need for a replacement.

### Cross-module links

- Related: WO-G Issue Materials (full-screen program; also handles Scrap Replacement on the same transaction)
- Related: WO (Work Orders) module for work order and component setup
- Related: PO (Purchase Orders) module — purchasing is alerted to buy a replacement

---

## Cross-references

| Module | Relationship to HH programs |
|---|---|
| **DC — Data Collection** | HH-F Enter Labor replaces DC-A Enter Labor Production |
| **WO — Work Orders** | HH-C replaces WO-G Issue Materials; HH-D replaces WO-I/WO-P Finished Production; HH-J replaces WO-S Print Work Order Labels; HH-M documents component scrap for WO-G |
| **IN — Inventory** | HH-B uses IN-B RTM Print Group for label formats; HH-K replaces IN-L-J Transfer Inventory; IN-Q is the full-screen batch label alternative to HH-B |
| **PO — Purchase Orders** | HH-G replaces PO-C Receive Purchase Orders; HH-M triggers purchasing alert for scrap replacement |
| **PI — Physical Inventory** | HH-E replaces PI-C Enter Tag Counts |
| **SO — Sales Orders / SH — Shipping** | HH-A replaces SO-E Release Sales Orders; HH-H replaces SO-P-I Enter Freight & Tracking # |
| **RO — Routings** | RO-M Enter Testing Method and RO-N Enter Test Requirements are used to set up QC test data accessible via HH-I Paperless Shop Floor |
| **SD — System Defaults** | SD-B Work Orders Defaults controls backflushing, costing, auto-close, and Lot automation behavior for HH-D |
