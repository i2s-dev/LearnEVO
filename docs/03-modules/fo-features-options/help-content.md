# FO — Features & Options

Status: verified (text distilled from the vendor's help file).

*Source: EvoHELP.CHM → Items → Features & Options (5 topics).*
*Extracted HTML in [samples/chm/extracted/](../../../samples/chm/extracted/).*

---

## Contents

- [FO-A — Enter Features and Options](#fo-a--enter-features-and-options)
- [FO-C — Enter Option Prices](#fo-c--enter-option-prices)
- [FO-D — Print Option Prices](#fo-d--print-option-prices)
- [FO-E — Print Option Where Used](#fo-e--print-option-where-used)
- [FO-G — Configure Item](#fo-g--configure-item)
- [Cross-references](#cross-references)

---

## FO-A — Enter Features and Options

*Source: [fo-a_enter_features_and_options.htm](../../../samples/chm/extracted/fo-a_enter_features_and_options.htm)*

**Purpose.** Use this program to enter features within bills of material and to enter option bills of material for features. The program can also be used for general bills of material maintenance unrelated to features and options.

### General Program Operation

This program is identical to BM-A Enter Bills of Material and in fact Feature and Option bills can be entered using either program. There are additional pop-up windows that are presented to further define features and options when a type `O` part is either a parent or component; those windows are specific to Features and Options and are described below. See BM-A for specific instructions on entering bills of material.

### Defining Options within Features

Before entering option bills of material to define specific features, you must have features (`O` type items) already created in inventory. Enter the `O` type feature as the **Parent Product**.

For option bills only, a special **Option Settings** button is available. After clicking on this button you are asked the following questions. Defaults for these prompts can be set up in SD-L Features and Options Defaults.

#### Option Settings fields

| Field | Values | Description |
|---|---|---|
| **Manufactured or Kit type** | `M` / `K` | `M` — option is passed over to a work order bill of materials. `K` — option remains only as a sales order line item. |
| **Include in cost rollup?** | `Y` / `N` | `Y` — the standard cost of this component is included in the cost rollup of the parent product as performed via BM-G Print/Rollup Standard Costs. Generally only one component within an option bill will be included in the cost rollup; including all components would overstate the parent product's cost. |
| **Use std customer pricing?** | `Y` / `N` | `Y` — sales order entry uses whatever pricing the customer is assigned (price code, contract price, or the option's base price from the inventory file if no price code is assigned). `N` — a specific price or percentage entered in the following field applies equally to all customers regardless of price lists or contract prices. If the option carries no price, enter `N` and leave the **Option Price** field blank. |
| **Percentage pricing** | `Y` / `N` | `Y` — the price for this option is a percentage add-on to the parent product's price. |
| **Option price/percent** | Numeric | A specific flat price for this option that applies to all customers, regardless of price list or contract price. This price is feature-specific — the same option can carry a different price within a different feature. The price is multiplied by the **Quantity Per** for this component defined in the option bill, which is then multiplied by the order quantity of each parent product up through all levels of the option structure. If **Percentage pricing** was set to `Y`, this field holds the actual percentage (e.g., enter `10.0000` to boost the parent's price by 10%). |
| **Add price to parent?** | `Y` / `N` | `Y` — this option's price or percentage is added to the price of the parent product. `N` — this option's price or percentage is itemized as a separate charge on the sales order. |

### Defining Features within Parent Products

Wherever a finished good or subassembly parent product has optional components in its bill of material, enter the appropriate **Feature** (`O` type item) that represents that set of options as a bill of material component. Whenever a feature is entered in a bill of material, a **Features Settings** button is presented, after which you can answer the following questions.

- **Mandatory Feature** — select this if you require selection of an **Option** within this feature during sales order entry.
- **Feature not required** — select this if the feature is not required and it is up to the order entry operator's discretion whether to make a selection or not.
- **Allow multiple selections** — if selected, the user can choose more than one of the available options within this feature.

---

## FO-C — Enter Option Prices

*Source: [fo-c_enter_option_prince.htm](../../../samples/chm/extracted/fo-c_enter_option_prince.htm)*

**Purpose.** Use this program to update option prices that were originally entered via FO-A Enter Features and Options. This provides a faster and more convenient means of maintaining option prices than navigating back through the option bills of material.

Pricing for options that are designated to use standard pricing (base prices, price codes, contract prices) is performed from within the Pricing submenu in the Inventory module, not here.

### General Program Operation

1. Enter the **Feature** item number, or select one using the **Lookup** icon (F2). The lookup window is confined to features only. The feature description is displayed automatically.
2. Enter the **Option** item number in the **Option** field. Pressing F2 (or clicking **Lookup**) displays all options defined for this feature. Highlight the desired option and press Enter or click to select it.
3. Before reaching the **Option Price** field, the current settings for **Add price to Parent?** and **Use std customer pricing?** (established in FO-A) are shown. Press Enter through these fields unless you wish to change them.
4. Enter the option price.
5. Confirm the save prompt (press Enter or click **Save**). The **Feature** remains on the screen so you can proceed to the next option without re-entering the feature number.

---

## FO-D — Print Option Prices

*Source: [fo-d_print_option_price.htm](../../../samples/chm/extracted/fo-d_print_option_price.htm)*

**Purpose.** Use this program to get a listing of the option prices entered through either FO-A Enter Features and Options or FO-C Enter Option Prices.

### General Program Operation

The report can be filtered to a from/through range of:

- **Features** (item number range)
- **Categories** (from the inventory file)
- **Item classes**

---

## FO-E — Print Option Where Used

*Source: [fo-e_print_option_where_used.htm](../../../samples/chm/extracted/fo-e_print_option_where_used.htm)*

**Purpose.** Use this program to get a listing of all the features within which an **Option** is defined, or, in the case of a **Feature**, all the parent products that contain that feature.

### General Program Operation

Enter either the feature or the option for which you want a where-used listing. You may select one from a pop-up window by pressing F2 (or clicking the **Lookup** button).

- If the item entered is an **Option**, the report shows every feature in which that option appears.
- If the item entered is a **Feature**, the report shows every parent product (finished good or subassembly) whose bill of material contains that feature.

---

## FO-G — Configure Item

*Source: [fo-g_configure_item.htm](../../../samples/chm/extracted/fo-g_configure_item.htm)*

**Purpose.** Use this program to define the configuration of a specific item by selecting specific options from an assembly that has been defined with Features and Options choices. Once the configuration has been defined, the item can be converted to a Sales Order, Work Order, Sales Quotation, Vendor RFQ, or Purchase Order — or copied to a new configuration that can then be modified.

### Configuring an Item

1. Click the **Add New** button (plus sign on the green circle on the top toolbar) to start a new configuration.
2. Enter the **top assembly item number**.
3. Enter a **Description** of this particular configuration.
4. Enter the **Customer**, **Vendor**, and **RFQ number** as applicable.
5. Leave the **Status** field blank.
6. Click the **Options** button in the lower left. You will get the message "BOM Template copied." The program has copied the complete bill of materials for this assembly at all levels to a template file to be used for configuration selection.
7. Click **Options** again to open a **tree view** of the options in the BOM. Traverse the tree and make the desired selections by clicking the appropriate checkboxes.

#### Tree view display modes

| Button | Description |
|---|---|
| **Display Options** | Default opening view — shows only option-choice nodes. |
| **Display All** | Shows the entire BOM including all components. |
| **Display Selections** | Shows only items that have already been selected. |
| **Display Open Options** | Shows only entries that have not yet been selected. |
| **Reset** | Clears all choices so you can start over. |

At any time you can click **Save and Exit** to partially configure an item and return later to finish it. The exception is when this configurator is called by SO-A Enter Sales Orders — in that context the **Save and Exit** button is not enabled until all mandatory selections have been made.

### Converting a Configured Item

Click the **Convert** button to choose a conversion target. Available targets are:

- Sales Quote
- Sales Order
- Work Order
- Vendor RFQ
- Purchase Order

A future release will also support conversion to a permanent part number, so that a popular configuration can become a firm part number without Feature and Option choices.

Select one or more conversion types and click **Go**. Multiple types are processed sequentially.

The **Convert** button is only available when the configuration status is **Completed** (all selections made) or **Cvt to** (previously converted). If option selection has not been completed, the Convert button is not available.

#### Converting to Sales Quote or Sales Order

You are prompted for:

- **Quantity**
- **Warehouse Location**
- **Customer Code**
- **Ship date**

Click **Go** and you are prompted whether to create a new order/quote or add lines to an existing one. If adding to an existing order, a list of Sales Orders for that customer is presented. You are then shown a list of line items that will be passed to the order, which can be edited for price, description, and quantity. Click **Exit** when the lines are correct; you are then prompted to generate the order/quote or save the choices for later.

#### Converting to a Work Order

You are prompted for:

- **Quantity**
- **Warehouse Location**
- **Customer**
- **Due Date**

Click **Go** and the program creates work orders for the appropriate quantities of all levels of subassemblies with the appropriate feature and option selections.

#### Converting to Vendor RFQ or Purchase Order

You are prompted for:

- **Quantity**
- **Warehouse Location**
- **Vendor Code**
- **Due date**

Click **Go** and you are prompted whether to create a new order/RFQ or add lines to an existing one. If adding to an existing order, a list of Purchase Orders for that vendor is presented. You are then shown a list of line items that can be edited for price, description, and quantity. Click **Exit** when the lines are correct; you are prompted to generate the order/RFQ or save the choices for later.

---

## Cross-references

| Module | Relationship |
|---|---|
| **BM — Bills of Material** | FO-A is functionally identical to BM-A; features and options are stored as `O`-type items within the BOM structure. BM-G Print/Rollup Standard Costs is affected by the "Include in cost rollup?" flag on each option. |
| **SO — Sales Orders** | SO-A Enter Sales Orders invokes the FO-G configurator when a configurable item is placed on an order; mandatory features enforce complete option selection before the configurator can be saved. Option prices feed directly into SO line item pricing. |
| **WO — Work Orders** | FO-G can convert a completed configuration directly to work orders at all BOM levels, carrying the selected features and options into the work order BOM. |
| **ES — Estimating** | The estimating module works alongside Features & Options to produce quotes for configurable/make-to-order items; FO-G can convert a configuration to a Sales Quotation. |
| **IN — Inventory** | `O`-type items (features) must be created in Inventory before they can be used in FO-A. Standard pricing (price codes, contract prices) for options is maintained in the Inventory module's Pricing submenu, not in FO-C. |
| **SD — System Defaults** | SD-L Features and Options Defaults sets system-wide defaults for the option-settings prompts in FO-A. |
| **PO — Purchase Orders** | FO-G can convert a completed configuration to a Vendor RFQ or Purchase Order for outsourced/purchased assemblies. |
