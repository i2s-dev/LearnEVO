# CS — Sales Commissions

Status: verified (text distilled from the vendor's help file).

*Source: EvoHELP.CHM → Sales → Sales Commissions (15 topics).*
*Extracted HTML in [samples/chm/extracted/](../../../samples/chm/extracted/).*

The CS module manages the full lifecycle of sales commissions in EvoERP. It supports both employee salespersons (paid through Payroll) and outside agents (paid through Accounts Payable). Commission rates can be set at the salesperson level, overridden per customer or item via price codes or contracts, or driven by the Extended Commissions system using granular rep-level links. Commissions can be recognized on invoice posting, on customer payment receipt, or accrued at posting and transferred only after payment. The module tracks monthly totals for quotas, gross sales, COGS, receipts, commissions due, and commissions paid, and provides a year-end routine to roll unpaid balances into the new year.

---

## Contents

- [CS-A — Enter Salespersons](#cs-a--enter-salespersons)
- [CS-B — View Salesperson Info](#cs-b--view-salesperson-info)
- [CS-C — Print Salespersons Info](#cs-c--print-salespersons-info)
- [CS-D — Transfer Sales Commissions](#cs-d--transfer-sales-commissions)
- [CS-E — Print Commission Detail](#cs-e--print-commission-detail)
- [CS-F — Print Commission Summary](#cs-f--print-commission-summary)
- [CS-G — Enter Sales Rep Links](#cs-g--enter-sales-rep-links)
- [CS-H — Import Sales Rep Links](#cs-h--import-sales-rep-links)
- [CS-K — Enter Price Code Commissions](#cs-k--enter-price-code-commissions)
- [CS-L — Print Price Code Commissions](#cs-l--print-price-code-commissions)
- [CS-M — Enter Contract Commissions](#cs-m--enter-contract-commissions)
- [CS-N — Print Contract Commissions](#cs-n--print-contract-commissions)
- [CS-O — Print Commissions Earned Detail](#cs-o--print-commissions-earned-detail)
- [CS-P — Print Commissions Due Summary](#cs-p--print-commissions-due-summary)
- [CS-Q — Commission Year End Routine](#cs-q--commission-year-end-routine)
- [Cross-references](#cross-references)

---

## CS-A — Enter Salespersons

*Source: [cs-a_enter_salespersons.htm](../../../samples/chm/extracted/cs-a_enter_salespersons.htm)*

**Purpose.** Use this program to set up a new salesperson or to make changes to an existing salesperson's master record. A salesperson may be an employee or an outside agent. Employee salespersons must first be set up in SM-G Enter Employees; the salesperson number must match the employee number. Outside agents must first be set up as vendors in AP-A Enter Vendors; their salesperson number can be any number not already used as an employee number.

### Field Explanations

| Field | Notes |
|---|---|
| **Salesperson Num** | The number used in SO-A Enter Sales Orders and throughout the system. For employees it must equal the SM-G employee number. For outside agents it can be any unused number. |
| **Class** | `E` = employee whose commissions are paid through Payroll (internal module or third-party such as ADP). `A` = outside agent whose commissions are paid through Accounts Payable. |
| **Vendor Code** | Applicable only when Class = `A`. Enter the AP vendor code that commissions will be transferred to. A sales agency may have multiple reps all posting to the same vendor in AP. |
| **First Name / MI** | Salesperson's first name and middle initial. Auto-populated from the employee record if the salesperson is already set up as an employee; can be changed. |
| **Last Name** | Salesperson's last name. Auto-populated from the employee record; can be changed. |
| **Rate** | Default commission percentage. Enter `10.0000` for 10%. This rate is used when no customer-level commission exists and Extended Commissions are not in use. When Extended Commissions are enabled, rates come from CS-G Enter Sales Rep Links instead. |
| **How** | Calculation basis: `G` = gross sales (net sales amount after per-line discount, excluding tax and freight). `C` = cost of goods sold (inventory average cost at time of invoice posting). `N` = net profit / gross margin (gross sales minus COGS). `F` = FOB selling price (commission calculated on the Bill-To customer's contract pricing while actual SO line items carry different pricing that incorporates embedded freight charges for the Ship-To customer). Tax and freight are excluded in all cases. Note: the Extended Commissions system calculates commission only on gross sales (`G`) or FOB amount (`F`). |
| **When** | Recognition trigger: `I` = commissions are due when the invoice is posted. `P` = commissions are due when the customer payment is posted. `A` = accrue commissions and post to the GL when invoices are posted, but do not allow transfer to AP or Payroll until customer payment is received. |

### General Program Operation

The opening screen lists existing salespersons. To add a new salesperson, click **Add** (or press `<Insert>`); fill in the entry screen according to the field explanations above. Save at any time with **Save** (F10), or the record saves automatically when the last field is completed. After saving, the screen returns to the list for additional entries or edits.

To edit, highlight a record and click **Edit**, make changes, then click **Save** (F10).

To exit from the opening screen, click **Exit** (or press `<Esc>`).

---

## CS-B — View Salesperson Info

*Source: [cs-b_view_salesperson_info.htm](../../../samples/chm/extracted/cs-b_view_salesperson_info.htm)*

**Purpose.** Use this program to view a salesperson's setup information (commission rate, calculation method, payment timing) and the last 12 months of activity totals: sales quota, gross sales, cost of goods sold, receipts, commissions due, and commissions paid. You can also enter or edit a sales quota directly in this screen.

### Column Heading Explanations

| Column | Description |
|---|---|
| **Quota** | An optional sales goal you may enter for comparison with actual performance. No processing or calculation is performed with this value; it is for reference only. |
| **Gross** | Total sales associated with this salesperson, broken down by month. |
| **COGS** | Total cost of goods sold associated with this salesperson, broken down by month. |
| **Receipts** | All sales associated with this salesperson for which customer payment has been received. Used as part of the commission calculation for salespersons whose **When** setting is `P` (commission due on payment). |
| **Comm Due** | Updated when an invoice or payment is posted. Represents the commission that is due but has not yet been paid (transferred). |
| **Comm Paid** | Updated after CS-D Transfer Sales Commissions has moved all or part of the commissions due to payroll or AP. Lists commissions paid by month. |

### General Program Operation

Enter the salesperson's number in the **Num** field, or click the lookup icon (F2) to select from a list. Once selected, the salesperson's information displays on screen.

To edit the **Quota** or any column value, click **Edit**; the cursor moves to the **Quota** column and the other columns become accessible.

When finished, click **Save** (F10). The screen clears for entry of another salesperson number. To exit, click **Exit** (or press `<Esc>`).

---

## CS-C — Print Salespersons Info

*Source: [cs-c_print_salespersons_info.htm](../../../samples/chm/extracted/cs-c_print_salespersons_info.htm)*

**Purpose.** Use this report to get a listing of how each salesperson is defined: commission rate, how paid, when paid, and so on. The report also shows a summary or monthly breakdown of each salesperson's total sales, cost of goods, net profits, receipts, commissions due, and commissions paid.

For more granular detail, use CS-E (Print Commission Detail) or CS-F (Print Commission Summary), which report at the line-item and invoice levels respectively. For reports that break out Salesperson 1 and Salesperson 2 commissions separately, see CS-G through CS-J.

---

## CS-D — Transfer Sales Commissions

*Source: [cs-d_transfer_sales_commissions.htm](../../../samples/chm/extracted/cs-d_transfer_sales_commissions.htm)*

**Purpose.** Use this program to transfer all or part of the commissions due to each salesperson's payroll account (if an employee) or Accounts Payable account (if an outside agent) for the current period.

### Field Explanations

| Field | Description |
|---|---|
| **Month** | Defaults to the current month. Enter any previous month number to view commissions still due from sales in that month. |
| **Slsp# and Salesperson Name** | The salesperson's number and name. Only salespersons with commissions currently due are displayed. |
| **Commission Due** | The total commission accrued through the displayed month that has not yet been transferred (as of the current date). Always displayed in Base Currency. For agent (outside) sales reps, the amount converts to the appropriate source currency when transferred, if applicable. |
| **Commissions to Pay** | Defaults to the full amount shown in Commission Due. You may enter all or part of the commission due to transfer a partial amount. Like Commission Due, always displayed in Base Currency; converts to source currency on transfer for agent reps. |

### General Program Operation

Run CS-D before processing an upcoming payroll.

**Employee salespersons — Payroll module:** If pay information has already been entered in PR-B Enter Pay Info for the current pay period, the program will prompt you to recalculate taxes for the period based on the commissions just transferred. Once the transfer is complete, the **Comm Due** and **Comm Paid** fields in the salesperson record are updated; the **Commission** amounts in the current payroll record are also updated.

**Employee salespersons — CheckMark Payroll link:** The program produces a report providing the information needed for manual entry of commissions into CheckMark.

**Employee salespersons — external payroll service (e.g., ADP):** The program prints a report listing the commission amounts to be submitted to the payroll service. This report can be enabled at SD-N Sales Commissions Defaults.

**Outside agents (Class = A):** An Accounts Payable voucher is generated that can be paid through the AP system. If the vendor assigned to the agent has a default currency other than the base currency, the amount to be paid is converted to the appropriate currency.

**GL note:** For employee sales reps, when processing payroll the commission should be posted to the Commission Payable liability account, not the commission expense account, because the expense was already recognized when commissions were originally accrued.

---

## CS-E — Print Commission Detail

*Source: [cs-e_print_commission_detail.htm](../../../samples/chm/extracted/cs-e_print_commission_detail.htm)*

**Purpose.** Use this report to get a line-item level listing of all sales associated with specified salespersons within a date range.

### Report Contents

The report shows the following columns:
- Invoice number
- Customer code
- Customer purchase order number
- Item number
- Price
- Discount
- Commission percentage
- Commission amount
- Total commission

### Selection Options

- Limit by salesperson number.
- Limit by invoice date range.
- Limit by item number.
- Specify whether to report on **Salesperson 1**, **Salesperson 2**, or both.
- Option to print monthly totals (summarized totals by month).

**Currency note:** Regardless of the currency of the original invoice, this report prints both sales and commissions in base currency.

---

## CS-F — Print Commission Summary

*Source: [cs-f_print_commission_summary.htm](../../../samples/chm/extracted/cs-f_print_commission_summary.htm)*

**Purpose.** Use this report to get an invoice-level listing of all sales associated with specified salespersons within a date range.

### Report Contents

The report shows the following columns:
- Customer code
- Customer name
- Invoice date
- Invoice number
- Total price
- Total cost
- Gross profit percentage
- Commission amount

### Selection Options

- Limit by salesperson.
- Limit by invoice date range.
- Specify whether to include **Salesperson 1**, **Salesperson 2**, or both.
- Option to include or exclude costs and gross profit.
- Option to print monthly totals or not.

**Currency note:** Regardless of the currency of the original invoice, this report prints both sales and commissions in base currency.

---

## CS-G — Enter Sales Rep Links

*Source: [cs-g_enter_sales_rep_links.htm](../../../samples/chm/extracted/cs-g_enter_sales_rep_links.htm)*

**Purpose.** Use this program to assign commission percentages to a sales rep for a particular customer, item, item class, or any combination thereof. These settings are used **only** when Extended Commissions are enabled in SD-N Sales Commission Defaults. The standard (non-extended) commission system does not consult these records.

### Field Explanations

| Field | Required | Description |
|---|---|---|
| **Rep Number** | Required | The salesperson's number as assigned in CS-A Enter Salespersons. |
| **Customer Code** | Optional | The customer the rep is assigned to for this commission rate. |
| **Item Number** | Optional | The specific item the rep earns commission on. |
| **Item Class** | Optional | The item class the rep earns commission on. |
| **Rate** | Required | Commission percentage. Enter `10.0000` for 10%. |
| **Start Date** | Required | Date the commission rate takes effect. |
| **End Date** | Optional | Ending date if this is a promotional or time-limited rate. |

### General Program Operation and Combination Rules

The opening screen displays existing entries. Click **Add** to add a new record.

The combination of Customer, Item, and Item Class fields controls the scope of the commission rate:

- **Same rate for all items sold to a customer:** Enter the customer code; leave Item Number and Item Class blank.
- **Different rates for different items or item classes at the same customer:** Create a separate record for each combination of customer code plus item or item class.
- **Same rate on a particular item or class regardless of customer:** Leave the customer blank; populate the item or item class.
- **Promotional period:** Populate the End Date field to limit the rate to a specific time window.

---

## CS-H — Import Sales Rep Links

*Source: [cs-h_import_sales_rep_links.htm](../../../samples/chm/extracted/cs-h_import_sales_rep_links.htm)*

**Purpose.** Use this program to import commission percentages for sales reps (by customer, item, item class, or combination) from a flat file. These settings are used only when Extended Commissions are enabled in SD-N Sales Commission Defaults.

### Field Explanations

The same fields as CS-G apply:

| Field | Required | Description |
|---|---|---|
| **Rep Number** | Required | Salesperson number as assigned in CS-A. |
| **Customer Code** | Optional | Customer the rep is assigned to. |
| **Item Number** | Optional | Item the rep earns commission on. |
| **Item Class** | Optional | Item class the rep earns commission on. |
| **Rate** | Required | Commission percentage (e.g., `10.0000` for 10%). |
| **Start Date** | Required | Date the commission rate takes effect. |
| **End Date** | Optional | Ending date for time-limited rates. |

### General Program Operation

Enter the file name to import and specify which column in the file holds each data field.

- **Comma-delimited file:** Enter only the column number for each field.
- **Fixed-length file:** Enter the starting position and length of each field.

---

## CS-K — Enter Price Code Commissions

*Source: [cs-k_enter_price_code_commissions.htm](../../../samples/chm/extracted/cs-k_enter_price_code_commissions.htm)*

**Purpose.** Establish commissions on specific inventory items at the price-code level. Commissions entered here override both any customer-level commission and the salesperson's default commission rate. Different commission rates may be entered for **Salesperson 1** and **Salesperson 2**. These commissions are **not used** when Extended Commissions are enabled; Extended Commissions uses CS-G Enter Sales Rep Links instead.

### General Program Operation

1. Enter an item number in the **Product** field, or press F2 (or click Lookup) to select from a pop-up list.
2. Enter the applicable price code. The inventory base price displays for reference only.
3. The quantities, prices, and discount from base price display for the item. Edit these as needed or press `<Enter>` to advance through fields.
4. Enter the appropriate commission percentage for each salesperson. Different commission rates can be entered for each quantity price break tier.
5. Press F10 (or click **Save**) to save the record.

---

## CS-L — Print Price Code Commissions

*Source: [cs-l_print_price_code_commissions.htm](../../../samples/chm/extracted/cs-l_print_price_code_commissions.htm)*

**Purpose.** Use this report to get a printout of items that have commissions entered within their price codes.

### Selection Options

- Limit the printout to a range of item numbers.
- Limit the printout to a range of price codes.

---

## CS-M — Enter Contract Commissions

*Source: [cs-m_enter_contract_commissions.htm](../../../samples/chm/extracted/cs-m_enter_contract_commissions.htm)*

**Purpose.** Establish commissions on specific inventory items for specific customers, effective up through an expiration date. Commissions entered here sit at the top of the override hierarchy: they override the customer-level commission, the salesperson's default commission, and any commission entered within an item's price code. Different commission rates may be entered for **Salesperson 1** and **Salesperson 2**. These commissions are **not used** when Extended Commissions are enabled; Extended Commissions uses CS-G Enter Sales Rep Links instead.

### General Program Operation

1. Enter a customer code in the **Customer Code** field, or press F2 (or click Lookup) to select from a pop-up list.
2. Enter the item number, or press F2 to select. Existing contract price information displays automatically. If no contract record exists, you can enter contract price information through this screen. The inventory base price displays for reference only.
3. The quantities, prices, and discount from base price display. Edit as needed or press `<Enter>` to advance.
4. Enter the appropriate commission for each salesperson. Different commissions can be entered for each quantity price break tier.
5. Press F10 (or click **Save**) to save the record.

---

## CS-N — Print Contract Commissions

*Source: [cs-n_print_contract_commissions.htm](../../../samples/chm/extracted/cs-n_print_contract_commissions.htm)*

**Purpose.** Use this report to get a printout of contract prices that have commissions attached to them.

### Selection Options

- Limit the report to a range of products.
- Limit the report to a range of customers.

---

## CS-O — Print Commissions Earned Detail

*Source: [cs-o_print_commissions_earned_detail.htm](../../../samples/chm/extracted/cs-o_print_commissions_earned_detail.htm)*

**Purpose.** Use this report to show the status of commissions earned at the invoice level.

### Report Contents

The report shows the following columns for each record:
- Salesperson number
- Salesperson name
- Invoice number
- Customer code
- Invoice date
- Payment date
- Payment amount
- Commissionable amount
- Commission earned

### Selection Options

- Limit the report to a range of salespersons.
- Limit the report to a range of months.

### Important Behavior

Items do **not** come off this report when commissions are transferred using CS-D Transfer Sales Commissions. This report is therefore a **permanent historical record** of all commissions earned. When a listing of current commissions still due is needed, run the report with an appropriate date range filter.

**Currency note:** Regardless of the currency of the original invoice, this report prints both sales and commissions in base currency.

---

## CS-P — Print Commissions Due Summary

*Source: [cs-p_print_commissions_due_summary.htm](../../../samples/chm/extracted/cs-p_print_commissions_due_summary.htm)*

**Purpose.** Use this report to show the status of commissions due, summarized by month.

### Report Contents

The report shows the following columns:
- Sales
- Commissions earned
- Receipts
- Commissions due
- Commissions paid

### Selection Options

- Limit the report to a range of salespersons.
- Limit the report to a range of months.

**Currency note:** Regardless of the currency of the original invoice, this report prints both sales and commissions in base currency.

---

## CS-Q — Commission Year End Routine

*Source: [cs-q_commission_year_end_routine.htm](../../../samples/chm/extracted/cs-q_commission_year_end_routine.htm)*

**Purpose.** Use this program at calendar year end to clear commission monthly totals and roll any unpaid commissions forward into January of the new year.

This routine must be run before beginning commission activity in the new year. It ensures that commissions earned but not yet paid do not get lost when the monthly accumulators reset; they are carried into period 1 of the new year rather than being discarded.

---

## Cross-references

| Related program | Relationship |
|---|---|
| **SO-A Enter Sales Orders** | Salesperson number(s) are assigned on each sales order; CS tracks commissions generated from SO invoices. |
| **AR (Accounts Receivable)** | Customer payment posting in AR triggers commission recognition for salespersons with **When** = `P` or `A`. |
| **AP-A Enter Vendors** | Outside agent salespersons must be set up as vendors in AP; CS-D creates AP vouchers for agent commissions. |
| **SM-G Enter Employees** | Employee salespersons must first be set up here; the salesperson number must match the employee number. |
| **PR-B Enter Pay Info / Payroll module** | CS-D transfers commission amounts into employee payroll records; taxes may be recalculated automatically. |
| **SA (Sales Analysis)** | SA reports draw on the same gross sales, COGS, and salesperson data that CS accumulates. |
| **SD-N Sales Commission Defaults** | Master switch for enabling Extended Commissions; also controls whether the ADP/external payroll report is printed during CS-D. |
| **CS-G Enter Sales Rep Links** | Required setup when Extended Commissions are enabled; replaces CS-K price-code rates and CS-M contract rates. |
