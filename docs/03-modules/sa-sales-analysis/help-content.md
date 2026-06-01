# SA — Sales Analysis

Status: verified (text distilled from the vendor's help file).

*Source: EvoHELP.CHM → Sales → Sales Analysis (18 topics).*
*Extracted HTML in [samples/chm/extracted/](../../../samples/chm/extracted/).*

The Sales Analysis (SA) module is a reporting-only module — it contains no data-entry programs. All reports read from the posted invoice history file and (for the bookings report in SA-A) from the open sales order file. The module provides a complete suite of printed reports, graphical charts, and CSV export programs that allow management to analyze sales volume, gross profit, cost of goods sold (COGS), and profit margin across every meaningful dimension: by invoice, customer, customer class, salesperson, inventory item, item class, user-defined grouping, and a top-customer ranking. Four sub-programs (SA-F-A through SA-F-D) produce charts or CSV exports instead of traditional printed reports. The two user-defined programs (SA-M and SA-N) support saved named report definitions with custom sort and subtotal combinations. Multi-currency processing is available throughout the module where enabled.

---

## Contents

- [SA-A — Print Daily Sales/Bookings](#sa-a--print-daily-salesbookings)
- [SA-B — Print Profit by Invoice](#sa-b--print-profit-by-invoice)
- [SA-C — Print Customer Detail](#sa-c--print-customer-detail)
- [SA-D — Print Customer Summary](#sa-d--print-customer-summary)
- [SA-E — Print Customer Class Detail](#sa-e--print-customer-class-detail)
- [SA-F-A — Chart/Export Profit by Invoice](#sa-f-a--chartexport-profit-by-invoice)
- [SA-F-B — Chart/Export Customer Detail/Summary](#sa-f-b--chartexport-customer-detailsummary)
- [SA-F-C — Chart/Export Salesperson Summary](#sa-f-c--chartexport-salesperson-summary)
- [SA-F-D — Chart/Export Item Sales Analysis](#sa-f-d--chartexport-item-sales-analysis)
- [SA-G — Print Customer Class Summary](#sa-g--print-customer-class-summary)
- [SA-H — Print Salesperson Detail](#sa-h--print-salesperson-detail)
- [SA-I — Print Salesperson Summary](#sa-i--print-salesperson-summary)
- [SA-J — Print Inventory Detail](#sa-j--print-inventory-detail)
- [SA-L — Print Product Class (Item Class)](#sa-l--print-product-class-item-class)
- [SA-M — Print User-Defined Detail](#sa-m--print-user-defined-detail)
- [SA-N — Print User-Defined Summary](#sa-n--print-user-defined-summary)
- [SA-O — Top Customer Report](#sa-o--top-customer-report)
- [SA-P — Print Sales Report](#sa-p--print-sales-report)
- [Cross-references](#cross-references)

---

## SA-A — Print Daily Sales/Bookings

*Source: [sa-a_print_daily_sales_bookings.htm](../../../samples/chm/extracted/sa-a_print_daily_sales_bookings.htm)*

**Purpose.** Produces a daily (or any date-range) summary report of either invoiced shipments (sales) or new/changed sales orders (bookings). Each line represents one invoice or sales order, showing sales amount, cost, gross profit, and profit percentage. The report subtotals by salesman and accumulates month-to-date totals.

### Report type selection

The user chooses either a **Sales** report or a **Bookings** report.

**Sales report** — draws from posted invoices. Cost of goods sold is the inventory average cost at the time of invoice posting.

**Bookings report** — divided into three sections that together represent total net bookings for the selected date range:

| Section | Description |
|---|---|
| *Closed Bookings* | Invoiced sales orders that have already shipped within the date range. Uses average cost at invoice posting. |
| *Open Bookings* | Open sales orders, or open portions of sales orders, that have not yet shipped. Uses inventory standard cost at the time the order was entered or updated. |
| *Changed Bookings* | Changes entered within the date range to sales orders that were booked prior to the date range. |

The Bookings report can also include line-item detail.

### Filters and options

| Parameter | Description |
|---|---|
| **Customer range** | From/thru customer code to restrict the report to selected customers. |
| **Salesperson range** | From/thru salesperson to restrict the report. |
| **Date range** | From/thru date (invoice date for sales; booking date for bookings). |
| **Include sales tax and freight** | Whether to add tax and freight to the sales totals. Default: `N`. |

### Multi-currency processing

Available when multi-currency is enabled in IM-A International Configuration.

**Currency [Base/Src]** — enter `B` to print in *base currency*. The program converts:
- Newly booked orders: using current exchange rates.
- Sales (invoiced) portion: using the closest historical exchange rate to the invoice date.

Enter `S` (or leave blank) to report in source currency as originally entered.

---

## SA-B — Print Profit by Invoice

*Source: [sa-b_print_profiy_by_invoice.htm](../../../samples/chm/extracted/sa-b_print_profiy_by_invoice.htm)*

**Purpose.** Provides a line-item detail analysis of gross profit organized by invoice. For each invoice, every line item is listed showing item number, quantity, price, cost, gross profit, and profit percentage. The report subtotals by invoice.

### Filters and options

| Parameter | Description |
|---|---|
| **Invoice range** | From/thru invoice number. |
| **Date range** | From/thru invoice date. |
| **Include sales tax and freight** | Whether to add tax and freight to the totals. Default: `N`. |

### Multi-currency processing

Available when multi-currency is enabled in IM-A International Configuration.

**Currency [Base/Src]** — enter `B` to print in *base currency*. All orders are converted using the closest historical exchange rate to each invoice date.

---

## SA-C — Print Customer Detail

*Source: [sa-c_print_customer_detail.htm](../../../samples/chm/extracted/sa-c_print_customer_detail.htm)*

**Purpose.** Produces a line-item detail report of sales and gross profit organized by customer. For each customer, the report lists every invoice line item with its extended amounts. Customer monthly totals are listed for each of the past 12 months.

### Filters and options

| Parameter | Description |
|---|---|
| **Customer range** | From/thru customer code. |
| **Salesperson range** | From/thru salesperson. |
| **Invoice date range** | From/thru invoice date. |
| **Item number range** | From/thru item number to restrict which line items appear. |
| **Include sales tax and freight** | Whether to add tax and freight to the extended amounts. Default: `N`. |
| **Sort order** | Choose to sort customers by **customer code**, **customer name**, or **alpha sort code**. |

---

## SA-D — Print Customer Summary

*Source: [sa-d_print_customer_summary.htm](../../../samples/chm/extracted/sa-d_print_customer_summary.htm)*

**Purpose.** Produces an invoice-level summary of sales and gross profit organized by customer. Rather than line-item detail, each invoice is represented by a single summary row. The report subtotals by customer.

### Filters and options

| Parameter | Description |
|---|---|
| **Customer range** | From/thru customer code. |
| **Salesperson range** | From/thru salesperson. |
| **Invoice date range** | From/thru invoice date. |
| **Include sales tax and freight** | Whether to add tax and freight to the totals. Default: `N`. |
| **Print monthly totals** | Option to print a monthly subtotal break after each customer, covering each of the last 12 months. |
| **Sort order** | Choose to sort by **customer code**, **customer name**, or **alpha sort code**. |

---

## SA-E — Print Customer Class Detail

*Source: [sa-e_print_customer_class_detail.htm](../../../samples/chm/extracted/sa-e_print_customer_class_detail.htm)*

**Purpose.** Produces a line-item level detail report of sales and profits organized by customer class. The **customer class** is a user-defined field assigned to each customer record in AR-A (Enter Customers). The report subtotals by customer class.

### Filters and options

| Parameter | Description |
|---|---|
| **Customer class range** | From/thru customer class code. |
| **Customer range** | From/thru customer code within each class. |
| **Invoice date range** | From/thru invoice date. |
| **Include sales tax and freight** | Whether to add tax and freight to the extended amounts. Default: `N`. |
| **Print monthly totals** | Option to print a monthly subtotal after each customer, covering each of the last 12 months. |

---

## SA-F-A — Chart/Export Profit by Invoice

*Source: [sa-f-a_chart_export_profit_by_invoice.htm](../../../samples/chm/extracted/sa-f-a_chart_export_profit_by_invoice.htm)*

**Purpose.** Provides a graphical analysis of gross profit by invoice, or extracts the underlying data to a CSV file. This is one of four Chart/Export programs in the SA module (SA-F-A through SA-F-D).

### Graphical option

- Chart type: **line chart**.
- Summarized by **day**, **week**, or **month**.
- Option to also include the **COGS** for each period as a second series.
- Option for a **year-to-year comparison** when the selected date range exceeds one year.
- Output: the chart opens in the default Windows image viewer, where the user can save or print it.

### Export (CSV) option

- One row per invoice.
- Columns: **Invoice Number**, **Date**, **Customer code**, **Invoice total**, **COGS**, **Margin**, **Margin %**.
- Output: a CSV file is generated and opened in the Windows default application (typically Excel or equivalent), where the user can save or print it.

---

## SA-F-B — Chart/Export Customer Detail/Summary

*Source: [sa-f-b_chart_export_customer_detail_summary.htm](../../../samples/chm/extracted/sa-f-b_chart_export_customer_detail_summary.htm)*

**Purpose.** Provides a graphical analysis of gross profit by invoice (customer view) or an extraction of the data to CSV. Functionally mirrors SA-F-A but is oriented toward customer-level analysis.

### Graphical option

- Chart type: **line chart**.
- Summarized by **day**, **week**, or **month**.
- Option to also include **COGS** for the period.
- Option for a **year-to-year comparison** when the date range exceeds one year.
- Output: opens in the default Windows image viewer.

### Export (CSV) option

- One row per invoice.
- Columns: **Invoice Number**, **Date**, **Customer code**, **Invoice total**, **COGS**, **Margin**, **Margin %**.
- Output: CSV file opened in the Windows default application.

---

## SA-F-C — Chart/Export Salesperson Summary

*Source: [sa-f-c_chart_export_salesperson_summary.htm](../../../samples/chm/extracted/sa-f-c_chart_export_salesperson_summary.htm)*

**Purpose.** Provides a graphical analysis of gross profit summarized by salesperson, or exports the underlying data to CSV.

### Graphical option

- Chart type: **pie chart** or **bar chart**, summarized by **Sales Rep**.
- Output: opens in the default Windows image viewer.

### Export (CSV) option

- One row per invoice.
- Columns: **Invoice Number**, **Date**, **Bill To Customer**, **Ship To Customer**, **Invoice Number**, **Invoice Subtotal**, **Invoice Total**, **COGS**, **Margin**, **Margin %**.
- Output: CSV file opened in the Windows default application.

---

## SA-F-D — Chart/Export Item Sales Analysis

*Source: [sa-f-d_chart_export_item_sales_analysis.htm](../../../samples/chm/extracted/sa-f-d_chart_export_item_sales_analysis.htm)*

**Purpose.** Provides a graphical analysis of gross profit at the item or item-class level, or exports detailed item-level data to CSV.

### Graphical option

- Chart type: **pie chart** or **bar chart** by **item class**.
- When the *Top N Items* option is selected, the chart is by individual **item** rather than item class.
- Output: opens in the default Windows image viewer.

### Export (CSV) option

- One row per invoice line.
- Columns: **Item Class**, **Item Number**, **Item Description**, **Invoice Number**, **Invoice Date**, **Customer**, **Quantity**, **Extension**, **Unit Cost**, **Category**, **Extended COGS**, **Margin**, **Margin %**.
- Output: CSV file opened in the Windows default application.

---

## SA-G — Print Customer Class Summary

*Source: [sa-g_print_customer_class_summary.htm](../../../samples/chm/extracted/sa-g_print_customer_class_summary.htm)*

**Purpose.** Produces an invoice-level summary report of sales and profits organized by customer class. The **customer class** is a user-defined field assigned to customers in AR-A (Enter Customers). The report subtotals by customer class.

### Filters and options

| Parameter | Description |
|---|---|
| **Customer class range** | From/thru customer class code. |
| **Customer range** | From/thru customer code within each class. |
| **Invoice date range** | From/thru invoice date. |
| **Include sales tax and freight** | Whether to add tax and freight to the totals. Default: `N`. |
| **Print monthly totals** | Option to print a monthly subtotal after each customer, covering each of the last 12 months. |

---

## SA-H — Print Salesperson Detail

*Source: [sa-h_print_salesperson_detail.htm](../../../samples/chm/extracted/sa-h_print_salesperson_detail.htm)*

**Purpose.** Produces a line-item level detailed report of sales organized by salesperson. The report subtotals by salesperson.

### Filters and options

| Parameter | Description |
|---|---|
| **Salesperson range** | From/thru salesperson code. |
| **Invoice date range** | From/thru invoice date. |
| **Item number range** | From/thru item number to restrict which line items appear. |
| **Include sales tax and freight** | Whether to add tax and freight to the extended amounts. Default: `N`. |
| **Print monthly totals** | Option to print a monthly subtotal after each salesperson, covering each of the last 12 months. |

---

## SA-I — Print Salesperson Summary

*Source: [sa-i_print_salesperson_summary.htm](../../../samples/chm/extracted/sa-i_print_salesperson_summary.htm)*

**Purpose.** Produces an invoice-level summary report of sales and profits organized by salesperson. Rather than line-item detail, each invoice appears as a single summary row. The report subtotals by salesperson.

### Filters and options

| Parameter | Description |
|---|---|
| **Salesperson range** | From/thru salesperson code. |
| **Invoice date range** | From/thru invoice date. |
| **Include sales tax and freight** | Whether to add tax and freight to the totals. Default: `N`. |
| **Print monthly totals** | Option to print a monthly subtotal after each salesperson, covering each of the last 12 months. |

---

## SA-J — Print Inventory Detail

*Source: [sa-j_print_inventory_detail.htm](../../../samples/chm/extracted/sa-j_print_inventory_detail.htm)*

**Purpose.** Produces a line-item detail report of sales and profits organized by inventory item number. For each item, every invoice line for that item is listed. The report subtotals by inventory item.

### Filters and options

| Parameter | Description |
|---|---|
| **Item number range** | From/thru item number. |
| **Invoice date range** | From/thru invoice date. |
| **Include sales tax and freight** | Whether to add tax and freight to the extended amounts. Default: `N`. |
| **Print monthly totals** | Option to print a monthly subtotal after each item number, covering each of the last 12 months. |

---

## SA-L — Print Product Class (Item Class)

*Source: [sa-l_print_product_class.htm](../../../samples/chm/extracted/sa-l_print_product_class.htm)*

**Purpose.** Produces a detail report of sales and profits organized by inventory item class. The report subtotals by item class. (Note: the CHM page title says "SA-L Print Product Class" but the body heading reads "SA-L Print Item class" — both names refer to the same program.)

### Filters and options

| Parameter | Description |
|---|---|
| **Item class range** | From/thru item class code. |
| **Category range** | From/thru item category within each class. |
| **Item number range** | From/thru item number within each class. |
| **Invoice date range** | From/thru invoice date. |
| **Include sales tax and freight** | Whether to add tax and freight to the extended amounts. Default: `N`. |

---

## SA-M — Print User-Defined Detail

*Source: [sa-m_print_user_defined_detail.htm](../../../samples/chm/extracted/sa-m_print_user_defined_detail.htm)*

**Purpose.** A user-defined report generator providing flexible filtering and sorting options for viewing sales analysis data in any combination. This version produces **detail data** (one row per invoice line item), similar to the dedicated detail reports elsewhere in the SA module. For invoice-level summary output, use SA-N Print User-Defined Summary.

### Multi-currency processing

Available when multi-currency is enabled in IM-A International Configuration.

**Currency [Base/Src]** — enter `B` to print in *base currency*, converting all orders using the closest historical exchange rate to each invoice date.

### General operation

**Report Name** — when creating a report for the first time, assign it a name. All filtering, sorting, and layout selections are saved under this name. To rerun a previously defined report, perform a lookup to select the report name; all settings reload automatically.

**Report Format** — defaults to `T6SAM1`, which is the standard graphical RTM (ReportBuilder) layout for this program. The user can:
- Copy `T6SAM1.RTM` to a new name.
- Modify the copy using the *Modify Forms* program (accessible from the main menu's *File* menu).
- Specify the custom layout name in the *Report Format* field, allowing each saved *Report Name* to use a unique layout.
- Use format `T6OPSALE.RTM` to produce a single summary line per item when sorting by item rather than listing all invoice detail.

**Sort / subtotal parameter** — choose from pre-defined fields or *User Defined*:

| Pre-defined sort options |
|---|
| Customer |
| Customer Class |
| Salesperson |
| Item |
| Item Class |
| User Defined |

When *User Defined* is selected, click the **User Defined** tab to define:
- **Indexes** — the sort order fields.
- **Breaks** — the subtotal grouping fields.

This allows combinations such as item numbers subtotaled within item class subtotaled within customer.

**Filter fields** — two screens of from/thru selection criteria are available. Because the posted invoice file can become large, the program's **primary sort is Ship Date**. Even when filtering by invoice number range, specifying a Ship Date range that encompasses those invoices is strongly recommended to avoid scanning the entire file.

Click **Print** after all fields are completed to run the report.

### Performance tip

The posted invoice file can be very large. Always supply a **Ship Date range** in addition to any other filters to minimize file-scan time.

---

## SA-N — Print User-Defined Summary

*Source: [sa-n_print_user_defined_summary.htm](../../../samples/chm/extracted/sa-n_print_user_defined_summary.htm)*

**Purpose.** A user-defined report generator providing flexible filtering and sorting options for viewing sales analysis data. This version produces **summary data with one line per invoice**. For line-item detail output listing each individual shipment, use SA-M Print User-Defined Detail.

### Multi-currency processing

Available when multi-currency is enabled in IM-A International Configuration.

**Currency [Base/Src]** — enter `B` to print in *base currency*, converting all orders using the closest historical exchange rate to each invoice date.

### General operation

**Report Name** — assign a name when first creating a report. All filtering, sorting, and layout selections save under this name and reload automatically on subsequent runs.

**Output format options:**

| Option | Behavior |
|---|---|
| Text Format | Print to text format. |
| Export | Output to ASCII file without headers or page breaks (for downstream processing). |
| Report Format | Available when both Text and Export are answered `N`. Defaults to `T6SAN1` (standard graphical RTM layout). |

The **Report Format** field allows specifying a custom RTM layout name. The user can copy `T6SAN1.RTM` to a new name, modify it with the *Modify Forms* program, and reference the custom name here. Using format `T6OPSALE.RTM` produces a single summary line per customer when sorting by customer.

**Sort / subtotal parameter** — identical options to SA-M:

| Pre-defined sort options |
|---|
| Customer |
| Customer Class |
| Salesperson |
| Item |
| Item Class |
| User Defined |

When *User Defined* is selected, click the **User Defined** button (lower right) to define index (sort order) and break (subtotal) fields.

**Filter fields** — two screens of from/thru selection criteria. The **primary sort is Ship Date**; always specify a Ship Date range to limit file-scan time even when filtering by other fields.

After completing all fields the program asks:
1. Whether to save the entries.
2. Whether to print the report now.
3. Whether to include taxes and freight in the price.

### Performance tip

Same as SA-M: the posted invoice file can be very large. Always supply a **Ship Date range** to avoid scanning the entire file.

---

## SA-O — Top Customer Report

*Source: [sa-o_top_customer_report.htm](../../../samples/chm/extracted/sa-o_top_customer_report.htm)*

**Purpose.** Ranks and reports the top customers by sales volume within any combination of filters, and provides a side-by-side sales comparison for two date ranges.

### General operation

**Filter fields available:**

| Filter | Description |
|---|---|
| **Salesperson range** | From/thru salesperson code. |
| **Customer code range** | From/thru customer code. |
| **Customer class** | Filter to a specific class. |
| **State** | Filter by customer state. |
| **Territory** | Filter by customer territory. |
| **Include Vouchers** | Whether to include voucher-type transactions. |
| **Contact Manager Class** | Additional filter via the Contact Manager classification. |
| **Top N customers** | How many customers to include in the ranking. |

**Date ranges** — two date ranges are entered for comparison. Default is year-to-date for the current year as the first range, and the same period in the prior year as the second range. Custom ranges may be entered.

The report ranks the top X customers (as specified) that meet all filters based on sales during the **first date range**, then shows their sales figures for both date ranges side by side.

---

## SA-P — Print Sales Report

*Source: [sa-p_print_sales_report.htm](../../../samples/chm/extracted/sa-p_print_sales_report.htm)*

**Purpose.** Produces a profit-by-item report that adds **surcharge revenue** to item revenue so that accurate profitability by item can be determined. This distinguishes it from other item-level SA reports: surcharge amounts that are typically treated as separate line items are rolled into the preceding line item's revenue figure.

### General operation

**Filter fields available:**

| Filter | Description |
|---|---|
| **Invoice number range** | From/thru invoice number. |
| **Ship date range** | From/thru ship date. |
| **Customer code range** | From/thru customer code. |
| **Item number range** | From/thru item number. |
| **Item class** | Filter by item class. |
| **Item category** | Filter by item category. |
| **Item type** | Filter by item type. |
| **Active status** | Filter by item active/inactive status. |

**Output columns** — the report shows: **item**, **quantity**, **price**, **cost**, and **margin**. Surcharge revenue is added to the preceding line item's figures.

---

## Cross-references

The SA module is **read-only**. It does not post, update, or delete any data. All analysis draws from the posted invoice history file and (for SA-A bookings) from the open sales order file.

| Related module | Relationship |
|---|---|
| **SO — Sales Orders** | Source of open booking data used by SA-A (Bookings report). Sales order entry, order changes, and shipments feed the SA data. |
| **AR — Accounts Receivable** | Invoice posting (via AR invoice processing) feeds the posted invoice history file that all SA reports read from. AR-A (Enter Customers) defines the customer class field used by SA-E and SA-G. |
| **CS — Contact Manager** | SA-O (Top Customer Report) accepts a Contact Manager Class as an additional filter, linking customer ranking to CRM classifications. |
| **IM — International/Multi-currency** | IM-A (International Configuration) controls whether multi-currency fields appear in SA-A, SA-B, SA-M, and SA-N. |
| **IN — Inventory** | Item numbers, item classes, item categories, and product classes referenced throughout SA filter fields originate in the Inventory master. Average cost and standard cost used for COGS calculations are maintained in Inventory. |

### Chart/Export programs summary

Four programs in the SA-F group produce charts or CSV exports rather than printed reports:

| Program | Chart type | Export columns |
|---|---|---|
| SA-F-A | Line chart (by day/week/month) | Invoice No, Date, Customer, Invoice total, COGS, Margin, Margin % |
| SA-F-B | Line chart (by day/week/month) | Invoice No, Date, Customer, Invoice total, COGS, Margin, Margin % |
| SA-F-C | Pie or bar chart (by Sales Rep) | Invoice No, Date, Bill To, Ship To, Invoice No, Subtotal, Total, COGS, Margin, Margin % |
| SA-F-D | Pie or bar chart (by item class or Top N items) | Item Class, Item No, Description, Invoice No, Date, Customer, Qty, Extension, Unit Cost, Category, Extended COGS, Margin, Margin % |

All chart outputs open in the Windows default image viewer. All CSV exports open in the Windows default application (typically Excel).

### Cost basis used in SA reports

| Context | Cost used |
|---|---|
| Sales reports (invoiced) | Inventory **average cost** at the time of invoice posting |
| Closed bookings | Inventory **average cost** at the time of invoice posting |
| Open bookings | Inventory **standard cost** at the time the order was entered or updated |
