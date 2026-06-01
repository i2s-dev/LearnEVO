# SR — Service and Repair

Status: verified (text distilled from the vendor's help file).

*Source: EvoHELP.CHM → Sales → Service and Repair (8 topics).*
*Extracted HTML in [samples/chm/extracted/](../../../samples/chm/extracted/).*

The Service and Repair (SR) module manages service orders and repair orders as a distinct workflow from standard sales orders. Items received from customers for repair are tracked through quotation, order entry, optional work-order-backed repair production, invoicing, and posting. The module re-uses the SO (Sales Order) program framework throughout but applies service-specific rules: no standard pricing pull-in on production parts, a dedicated Service/Repair inventory location, support for Make/Model/Serial Number traceability on type-N service items, and COGS driven by user-entered values rather than average inventory cost. The transaction type recorded in the ledger is `R` (repair) rather than `S` (sale), and inventory on-hand for the repaired item is not affected by invoice posting.

---

## Contents

- [SR-A — Enter Service/Repair Order](#sr-a--enter-servicerepair-order)
- [SR-B — Print Service/Repair Order](#sr-b--print-servicerepair-order)
- [SR-C — Convert S/R Order to Work Order](#sr-c--convert-sr-order-to-work-order)
- [SR-D — Print S/R Packing Slip](#sr-d--print-sr-packing-slip)
- [SR-E — Release S/R Order](#sr-e--release-sr-order)
- [SR-F — Print S/R Invoice](#sr-f--print-sr-invoice)
- [SR-G — Post S/R Invoice](#sr-g--post-sr-invoice)
- [SR-I — Void S/R Invoice](#sr-i--void-sr-invoice)
- [Cross-references](#cross-references)

---

## SR-A — Enter Service/Repair Order

*Source: [sr-a_enter_service_repair_order.htm](../../../samples/chm/extracted/sr-a_enter_service_repair_order.htm)*

**Purpose.** Use this program to enter a Service and Repair Order or Quotation. The program is modeled on SO-A Enter Sales Orders, with the service-specific differences described below.

### General Operation

Order entry follows the same field-by-field flow as SO-A Enter Sales Orders. The notable differences are:

- **Order or Quote prompt.** On opening a new record the program asks whether you are entering an **Order** or a **Quote**. A quote carries a `Quote` status; once the customer approves it, clicking the **Convert** button on the opening list promotes the quote to an order using the same number but changing the status to `Order`.

- **Default Location.** The **Location** field defaults to the Service/Repair Location configured as the default in SD-T Service Repair & RMA Defaults, rather than to the standard sales location. This lets service orders draw from a dedicated service stocking location.

- **No standard pricing pull-in.** When a production part number is entered on a line, the system does **not** pull in the standard selling price. Pricing must be entered manually for service work.

- **Make / Model / Serial Number traceability.** If the line item is an inventory type `N` item that has been designated as a Service/Repair item in IN-B Enter Inventory, the program presents additional fields for **Make**, **Model**, and **Serial Number**. These fields provide item-level traceability throughout the service lifecycle.

- **Line Number codes for component handling.** When itemizing components under a service line, the **Line Number** field controls how the component is processed:

  | Line Number | Meaning |
  |---|---|
  | `S/R` | Component will be processed via a work order (costs collected on the WO, not deducted from inventory at order time). |
  | `K` | Component should be deducted directly from inventory during invoice posting (use when **not** using a work order). |

- **Inventory Location per line.** Each component line can carry its own inventory **Location**, so the parent service order can reference the Service Location while component lines pull stock from the primary stock location during invoice posting.

### Quote-to-Order Conversion

To convert a Service Quote to a Service Order: open the order list in SR-A, locate the quote, and click the **Convert** button. The quote number becomes the order number; the status changes from `Quote` to `Order`. No new number is assigned.

### Next Step

To print the service order document, proceed to SR-B Print Service/Repair Order.

---

## SR-B — Print Service/Repair Order

*Source: [sr-b_print_service_repair_order.htm](../../../samples/chm/extracted/sr-b_print_service_repair_order.htm)*

**Purpose.** Use this program to print a Service Order or Quote for a customer — either to send to the customer or for internal use by the Service department.

### General Operation

Basic operation is identical to SO-B Print Acknowledgements. All print options, destination selections (printer, preview, file), and reprint behavior available in SO-B apply equally here. The printed document will reflect the SR order header and lines rather than a standard sales acknowledgement.

---

## SR-C — Convert S/R Order to Work Order

*Source: [sr-c_convert_s_r_order_to_work_order.htm](../../../samples/chm/extracted/sr-c_convert_s_r_order_to_work_order.htm)*

**Purpose.** Use this program to generate a Work Order from a Service/Repair Order so that labor and material costs can be collected against the repair job.

### General Operation

Basic operation is the same as SO-N Convert Sales Orders to Work Orders, with one critical difference:

- **No standard BOM or Routing pull.** For production items, the system does **not** automatically pull the standard Bill of Materials or Routing into the generated work order. This reflects the reality that service/repair work is not standard production — the actual operations needed depend on the condition of the item received, not on a fixed manufacturing process.

### Entering Labor on the Work Order

Because no routing is pulled automatically, labor sequences must be established by one of two methods:

1. **Manual routing entry.** Use WO-K-A Enter Work Order Routings to create sequences directly on the work order after it is generated.

2. **Service/Repair template item.** Define a template item with a routing in the inventory master, then configure both the template item and the **S/R Generic Item Number** in SD-T Service Repair & RMA Defaults. When the conversion runs, the system will use the template routing instead of the production routing.

---

## SR-D — Print S/R Packing Slip

*Source: [sr-d_print_s_r_packing_slip.htm](../../../samples/chm/extracted/sr-d_print_s_r_packing_slip.htm)*

**Purpose.** Use this program to print a Service Order Packing Slip for shipping the repaired items back to the customer.

### General Operation

Basic operation is identical to SO-C Print Packing Slips. All print options and destination selections available in SO-C apply here. The packing slip will be formatted for the service/repair context and will reflect the SR order rather than a standard shipment.

---

## SR-E — Release S/R Order

*Source: [sr-e_release_s_r_order.htm](../../../samples/chm/extracted/sr-e_release_s_r_order.htm)*

**Purpose.** Use this program to release a Service Order for invoicing. During release you specify which components to itemize on the invoice, the selling price for each, and the Cost of Goods Sold (COGS) to apply to each line.

### General Operation

1. Select the Order from the opening list.
2. Select the line item to be shipped/invoiced.
3. Click **BOM** to view the Bill of Materials of the Work Order that collected costs for the Service Order.
4. Select any components you want itemized on the invoice.

### Component and Pricing Options

- **Itemized components.** Components can appear as individual invoice lines with their own prices, or they can be listed at `$0` while the parent (top assembly) line carries the total price charged to the customer.
- **Labor and Misc items.** Labor and miscellaneous cost items can also be selected for itemization on the invoice.
- **Standard selling price reference.** The standard selling price for each component is displayed on screen for reference when deciding how to price service work.
- **Component release requirement.** Component lines that were designated as `K` (on-order) lines in SR-A **must** be released here in order for the invoice posting program (SR-G) to process them and pull the stock from inventory.
- **COGS entry.** The **COGS** value entered in this program for each line is the exact Cost of Goods Sold that SR-G Post S/R Invoice will use. It is not derived from average inventory cost — it is the value you enter here, reflecting the actual cost of the repair work.

### Key Distinction

Unlike standard SO processing where COGS is pulled from the inventory average cost, SR releases require explicit COGS entry because the cost of a repair job is not captured in the inventory master; it is accumulated on the work order and evaluated here during release.

---

## SR-F — Print S/R Invoice

*Source: [sr-f_print_s_r_invoice.htm](../../../samples/chm/extracted/sr-f_print_s_r_invoice.htm)*

**Purpose.** Use this program to print the invoice generated from a Service Order.

### General Operation

Basic operation is identical to SO-F Print Invoices. All print options, destination selections, and reprint behavior available in SO-F apply equally here. The printed invoice will reflect the SR order lines, the pricing established during SR-E release, and the service/repair transaction context.

---

## SR-G — Post S/R Invoice

*Source: [sr-g_post_s_r_invoice.htm](../../../samples/chm/extracted/sr-g_post_s_r_invoice.htm)*

**Purpose.** Use this program to post the Service/Repair invoice, recording the sale in Accounts Receivable, updating General Ledger, closing the associated work order, and completing finished production processing.

### General Operation

Basic operation is identical to SO-G Post Invoices, with the following SR-specific behaviors:

- **COGS source.** Instead of pulling average cost from the inventory master, the program uses the **COGS value entered per line in SR-E Release S/R Order**.
- **On-hand inventory not affected.** The on-hand quantity of the item being repaired is **not** changed. A repair is not a sale of inventory; the item was received from the customer and is being returned.
- **Transaction type.** The inventory/ledger transaction generated is type `R` (repair), not `S` (sale).
- **GL posting.** The GL entry posts between the **WIP (Work In Process) account** and the **COGS account**, rather than between the inventory asset account and COGS. This reflects that repair costs accumulated on the work order sit in WIP until the invoice is posted.
- **Work Order closure.** Posting automatically performs the **Enter Finished Production** processing on the associated work order and then closes the work order. No separate WO closure step is required after SR-G runs.

### Summary of GL Impact

| Debit | Credit | Condition |
|---|---|---|
| COGS account | WIP account | Invoice posting for each S/R line |
| Accounts Receivable | Sales/Revenue account | Invoice posted to AR (standard AR posting) |

Inventory asset accounts are **not** touched by SR-G.

---

## SR-I — Void S/R Invoice

*Source: [sr-i_void_s_r_invoice.htm](../../../samples/chm/extracted/sr-i_void_s_r_invoice.htm)*

**Purpose.** Use this program to reverse a Service/Repair invoice that has already been posted.

### General Operation

Basic operation is identical to SO-R Void Invoice, with one additional SR-specific action:

- **Finished Production reversal.** The program reverses the Finished Production posting that was performed by the original SR-G invoice posting. The repaired item is returned onto the work order, restoring the WO to its pre-posting state so the order can be corrected and re-invoiced if needed.

### Effect of Voiding

| What is reversed | Result |
|---|---|
| AR invoice | AR balance reduced / credit memo created |
| GL WIP-to-COGS entry | WIP re-debited, COGS reversed |
| Finished Production posting | Work order re-opened; repaired item back on WO |
| Inventory on-hand | Not affected (was not affected by original posting either) |

---

## Cross-references

The SR module sits within the Sales area of EvoERP and integrates closely with the following modules:

| Module | Relationship |
|---|---|
| **SO — Sales Orders** | SR-A/B/D/F/G/I mirror the SO-A/B/C/F/G/R programs. SR orders are distinct order types but share the same data entry framework. |
| **WO — Work Orders** | SR-C converts S/R orders to work orders. SR-E reads the WO BOM for component selection. SR-G closes the WO on invoice posting. SR-I re-opens the WO on void. |
| **IN — Inventory** | Service/Repair item designation is set in IN-B. Component `K` lines pull inventory on posting. Type-N items support Make/Model/Serial traceability. |
| **AR — Accounts Receivable** | SR-G posts invoices to AR in the same way as SO-G; SR-I voids follow the same AR reversal path as SO-R. |
| **GL — General Ledger** | SR-G posts WIP-to-COGS rather than Inventory-to-COGS. The WIP and COGS accounts used are configured in company/module defaults. |
| **SD-T — Service Repair & RMA Defaults** | Configures the default Service/Repair Location (used by SR-A), the S/R Generic Item Number, and the service/repair template item with routing (used by SR-C). |
| **WO-K-A — Enter Work Order Routings** | Used to manually add labor sequences to a work order generated by SR-C when no template routing is defined. |
