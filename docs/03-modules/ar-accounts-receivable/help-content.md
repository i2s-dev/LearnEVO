# AR — Accounts Receivable

Status: verified (text distilled from the vendor's help file).

*Source: EvoHELP.CHM → Sales → Accounts Receivable (16 topics).*
*Extracted HTML in [samples/chm/extracted/](../../../samples/chm/extracted/).*

The Accounts Receivable module is the customer master and cash receipts hub of EvoERP. It covers the full customer lifecycle: defining customers (AR-A), raising standalone invoices and credit memos outside of Sales Orders (AR-B), recording payments and applying credits (AR-C), charging interest on overdue balances (AR-D), printing customer statements (AR-E), and producing aging and past-due reports (AR-F). The module also handles sales-tax reporting and the transfer of collected tax liabilities to Accounts Payable (AR-K / AR-L), customer refunds (AR-M), advance deposits tied to sales orders (AR-N), collection dunning letters (AR-P), read-only inquiry (AR-Q), and payment history reporting (AR-R). Customer list and label programs (AR-G, AR-H, AR-I) round out the master-data reporting tools.

---

## Contents

- [AR-A — Enter Customers](#ar-a--enter-customers)
- [AR-B — Enter Vouchers](#ar-b--enter-vouchers)
- [AR-C — Record Payments](#ar-c--record-payments)
- [AR-D — Charge Interest on Invoices](#ar-d--charge-interest-on-invoices)
- [AR-E — Print Statements](#ar-e--print-statements)
- [AR-F — Print Aging](#ar-f--print-aging)
- [AR-G — Print Customer Code and Name](#ar-g--print-customer-code-and-name)
- [AR-H — Print Customer General Info](#ar-h--print-customer-general-info)
- [AR-I — Print Customer Mail Labels](#ar-i--print-customer-mail-labels)
- [AR-K — Print Sales Tax Report](#ar-k--print-sales-tax-report)
- [AR-L — Transfer Sales Taxes](#ar-l--transfer-sales-taxes)
- [AR-M — Enter Customer Refund](#ar-m--enter-customer-refund)
- [AR-N — Enter/Print Sales Order Deposits](#ar-n--enterprint-sales-order-deposits)
- [AR-P — Generate Dun Letters](#ar-p--generate-dun-letters)
- [AR-Q — View Customer Information](#ar-q--view-customer-information)
- [AR-R — Print AR Payment History](#ar-r--print-ar-payment-history)
- [Cross-references](#cross-references)

---

## AR-A — Enter Customers

*Source: [ar-a_enter_customers.htm](../../../samples/chm/extracted/ar-a_enter_customers.htm)*

**Purpose.** Use this program to set up a new customer or to change any customer master data including name, address, telephone, contact, tax authorities, payment terms, price codes, discount codes, salespeople, and commissions. Customer Credit Card information can also be viewed and edited. The program is integrated with the Contact Manager module, allowing follow-up codes and contact history to be managed without leaving the screen. Prerequisites: payment terms must exist in SM-D Enter Terms Table; tax groups must exist in SM-F Enter Tax Groups before tax-related fields can be populated.

### Standard Customer Information Fields

| Field | Size / Type | Notes |
|---|---|---|
| **Cust Cd** | 10 char alphanumeric (required) | Identifies the customer throughout the system. Single/double quotes and commas are prohibited; other characters such as `#` and `-` are allowed. |
| **Alpha Sort** | text | Used as the sort key on reports that sort alphabetically. Defaults to the first six letters of the company name; can be overridden. |
| **Company** | 30 char alphanumeric | The actual customer or company name. |
| **Address** | 3 lines × 30 chars | Standard mailing address. The Extended Address button opens a window for up to 8 lines × 80 characters each. |
| **City** | 26 char alphanumeric | Customer city. |
| **St** | 2 char | State code. |
| **Zip** | 10 char alphanumeric | Zip or postal code. |
| **Country** | 30 char alphanumeric | For multi-country customer bases. |
| **Ship to Customer?** | `Y`/`N` | Set `Y` if this record is a warehouse/ship-to address that will never be used on the Bill To side of a Sales Order or AR Voucher. |
| **Bill** | customer code | When **Ship to Customer?** is `Y`, enter the associated Bill To customer code here. |
| **Contact 1** | 30 char alphanumeric | Primary contact person; defaults into sales order headers. |
| **Phone** | 25 char alphanumeric | Primary telephone number. |
| **Fax** | 25 char alphanumeric | Fax number. |
| **Ship-to Cd** | customer code | Default ship-to account for this customer. Pulled automatically into new sales orders. Salesperson and tax authority from the ship-to account take precedence over the bill-to account. |
| **FOB** | text | Prints on sales order documents as the FOB designation. |
| **Ship Via** | text | Defaults into the Ship Via field on new sales orders. |
| **Default GL Sales** | GL account code | When not using Sales Orders module, this is the default distribution account on AR-B vouchers. When using Sales Orders, this account overrides the item-class sales account — use it when you want GL sales broken out by customer rather than by product class. Leave blank for product-class-based GL sales. |
| **Start Date** | date | Date of first sale or date the customer record was created. |
| **Class** | 4 char alphanumeric | Customer classification for grouping on reports (e.g., `DIST` for distributors, `RETL` for retail). |
| **Slsp 1** | salesperson number | Primary salesperson; defaults into sales order headers. Ship-to salesperson overrides bill-to if assigned. |
| **Comm 1** | percentage | Commission rate for Slsp 1. If blank, the salesperson's default from CS-A is used. Enter `10.00` for 10%. |
| **Slsp 2** | salesperson number | Optional second salesperson. Same rules as Slsp 1. |
| **Comm 2** | percentage | Commission rate for Slsp 2. |
| **Territory** | 4 char alphanumeric | Sales territory. Must be pre-entered in SM-I-B Enter Territory Codes. F2 / Lookup to select. |
| **Lead Source 1 & 2** | code | Primary lead sources. Must be pre-entered in SM-I-A Enter Lead Source Codes. F2 / Lookup to select. |
| **Resale Number** | 15 char alphanumeric | Customer's sales tax resale certificate number. Optional. |
| **RTM Print Group** | 1 char | Assigns a custom RTM form variant to this customer. Example: group `A` causes the print programs to look for `ENSOF4A.RTM` instead of `ENSOF4.RTM`. |
| **Ship Time** | integer (days) | Transit days from your warehouse to this customer. When set, SO-A skips Estimated Ship Date, advances to Customer Due Date, then back-calculates Ship Date by subtracting this value. |
| **Price Code** | code | Price list from SO-Q-D. If blank, the system uses inventory base prices or contract prices. |
| **Discount Code** | code | Discount schedule from SO-Q-F, applied on top of price-code prices or base prices. Not applied to contract prices. |
| **Email Invoice to SLSP** | `C`/`B`/`N` | Whether to copy (`C`) or BCC (`B`) the assigned salesperson on emailed invoices. |
| **LOC** | warehouse location code | Default warehouse location for orders to this customer; pulls into Sales Orders. |
| **Default Terms** | terms code | Payment terms from SM-D. Appears as default in vouchers and sales orders. |
| **Charge Interest?** | `Y`/`N` (required) | Set `Y` to include this customer in AR-D interest charge processing. |
| **Charge Recycle Fee?** | `Y`/`N` | When `Y`, a non-inventory recycle fee item (configured in SD-P) is added to sales orders. |
| **Statement?** | `Y`/`N` (required) | Set `Y` for customers who should receive statements via AR-E. |
| **Insurance Required?** | `Y`/`N` | Set `Y` to flag the packing slip that the shipment must be insured. Requires field `INS.REQUIRED` to be added to the Packing Slip RTM. |
| **Taxable?** | `Y`/`N` | Whether this customer is ever charged sales tax. |
| **Excise Taxable?** | `Y`/`N` | Whether this customer is ever charged excise tax. |
| **Tax Group** | tax group code | Required when **Taxable?** is `Y`. Must be pre-entered in SM-F. Even when **Taxable?** is `N`, assigning a tax group allows non-taxable sales to appear in tax authority reporting. |
| **Allow Backorders** | `Y`/`N` (default `Y`) | When `N`, SO-E will cancel any unfilled quantity and add an "Out of Stock" message to the invoice rather than creating a backorder. |
| **Roll Surcharge in SO-F** | `Y`/`N` | When `Y`, surcharge lines are rolled into the unit line price on printed invoices. |
| **Web Site** | URL | Enables the WEB button in AR-A, AR-Q, SO-A, and SO-I to open this URL. |

### International Fields

Visible only when the corresponding options are enabled in IM-A International Configuration.

**Currency** — The currency code for transactions with this customer. Must be pre-entered in IM-B Enter Multiple Currencies. Can be overridden at the sales order level.

**Tax-In Code** — Set `Y` if excise taxes are embedded in item prices (tax-inclusive pricing). The system backs the tax out of the price for GL and sales analysis purposes when excise tax processing is active in IM-A.

### Credit Info Fields (Credit Info Button)

| Field | Description |
|---|---|
| **Credit Hold?** | `Y` triggers a warning during sales order entry and blocks printing of packing slips. Optionally prevents order entry entirely when the SD-P default is set. Must be changed to `N` before shipments can proceed. |
| **Credit Limit** | Maximum outstanding invoice balance allowed. Alerts or blocks additional SO lines depending on SD-M Sales Orders Defaults. `$0` means unlimited credit. |
| **Last Dun?** | Read-only. Shows the form letter code and date of the last dun letter sent via AR-P. |
| **Out Credits** | Dollar amount of unapplied credits on file for this customer. |
| **Out Deposits** | Dollar amount of outstanding advance deposits held in the Customer Deposits GL liability account (AD-A). Applied automatically when invoices post (if linked via AR-N) or manually via AR-C. |
| **Out Inv Amts** | Dollar amount of open outstanding invoices. A credit balance and an invoice balance can coexist simultaneously. |
| **Last Sale** | Date of the most recent posted invoice. |
| **Last Payment** | Date of the most recent payment received. |
| **Days to Pay** | Rolling average number of days from invoice to payment receipt. Recalculated on each payment using the method selected in SD-P. |

### Additional Contacts (Contacts Button / F7)

Any number of contacts may be added, each with up to 10 phone numbers, email addresses, significant dates, and miscellaneous notes. A **Primary Contact** designation of `B` causes the contact to populate the "Attention" line on the Bill To side of a Sales Order; `S` populates the Ship To side. Email document subscriptions (quotes, invoices, etc.) are set per contact.

### Credit Card Info (CC Button)

Shows whether a credit card is on file and its expiration date. Only the last 4 digits of the card number are visible. When X-Charge or Payment Innovators integration is configured, card data entered here is uploaded to the secure server for charge processing.

### General Program Operation

**Creating a new customer.** Click Add on the opening customer list. Enter a new customer code (use codes that facilitate grouping or alpha ranges). Fill in all applicable fields. On new customer creation, the system automatically presents the customer totals window (for entering opening YTD/prior-year sales) and the multiple contacts window.

**Changing an existing customer.** Enter the customer code or press F2 / click Lookup to select. Edit any field. Press F7 / Contacts button to access multiple contacts. Press F8 / Statistics button to view (not edit) system-maintained customer totals. Save as usual.

**Deleting a customer.** All three balances — Out Inv Amt, Out Credit, and Out Deposit — must be $0.00 and there must be no AR history before deletion is allowed. Deletion is permanent; the record must be re-entered if deleted in error.

**AR Transactions Inquiry.** Click the AR Transactions button to see a scrolling list of all AR transactions (invoices, payments, deposits, credits) for the current customer. Highlight any transaction and click Transaction Detail to drill into that transaction.

**Notes Window (Home key or Notes button).** A 10-line × 60-character notepad attached to the customer. Notes pull into Sales Orders if that feature is enabled. Individual lines can be flagged as Hidden (suppressed from printing on invoices and acknowledgments). The Hide Notes button toggles Hidden status line by line; a checkmark in the left column indicates Hidden.

**Price Inquiry Window (End key or Prices button).** Enter an item number and quantity to retrieve the effective price for this customer: the system searches first for a contract price, then applies the customer's price code and discount code to arrive at a net price. Base prices are used if no price code is assigned. Discounts apply to price-code and base prices but not to contract prices.

**Contact Manager Interface.** AR-A and CM-A Enter Contact Accounts share the same account code. Press PgUp from either screen to toggle between them. From AR-A, press F5 / History Notes to view CM history notes, and F6 / Follow-up to access follow-up codes and dates, without leaving the program.

**Web Site Interface.** Click the WEB button to open the URL stored in the Web Site field.

---

## AR-B — Enter Vouchers

*Source: [ar-b_enter_vouchers.htm](../../../samples/chm/extracted/ar-b_enter_vouchers.htm)*

**Purpose.** Use this program to enter miscellaneous charges, credit memos, and adjusting entries that do not touch inventory or commissions. If inventory or commissions are involved, use SO-A Enter Sales Orders instead (credits are entered as negative-quantity orders). Hard-copy invoices for vouchers can be reprinted via SO-F Print Invoices in reprint mode.

### Multi-Currency Processing

When multi-currency is enabled in IM-A, all amounts are entered in source currency. The credit side of the transaction is converted to base currency at the rate in IM-C Enter Currency Exchange Rates. The debit posts in source currency to the currency's AR Control account.

### Auto-Tax Distribution

When entering a voucher the program asks whether to use Auto-Tax Distribution. If yes:
- The program calculates the sales tax and inserts a credit line to the default Sales Tax Payable account in the Distribution section.
- If the tax is **not** already in the voucher amount: the full voucher amount credits Sales, plus an additional credit for the tax amount credits Sales Tax Payable.
- If the tax **is** already included: the Sales credit is reduced by the tax amount so that Sales + Sales Tax Payable together equal the voucher amount.

Under multi-currency, the tax liability is posted in base currency but the tax owed is stored in source currency in the sales tax transfer file for use by AR-L.

### Field Explanations — Voucher Entry

| Field | Description |
|---|---|
| **Cust Code** | 10-character customer code. F2 / Lookup to select. A new customer can be added on-the-fly if the code is unknown. |
| **Name** | Filled automatically from the customer file after the code is entered. |
| **Voucher No** | 6-digit numeric. Leave blank to auto-assign the next invoice number (from SD-M Sales Orders Defaults). Manual entry allowed provided the number has not already been used as an invoice number. Warning: a manually entered number that later falls in the normal invoice sequence will be skipped by the invoicing program. |
| **Post Date** | Posting date. Defaults to today; can be overridden. |
| **Type** | `A` = AR Voucher, `B` = Credit Memo, `C` = Cash Transaction, `D` = Beginning Balance (invoice), `E` = Beginning Balance (credit). |
| **Desc** | 25-character description. Prints on posting reports and customer statements. |
| **Terms** | Payment terms from SM-D. Defaults to customer's default terms. Cash terms are required for type `C` (Cash Transaction) and prohibited for all other types. |
| **Total Amt** | 12-digit amount with 2 decimal places. Posts as a debit (standard voucher) or credit (credit memo) to the main AR account. |
| **Currency** | Available when multi-currency is enabled. Enter source currency code to enter the voucher in that currency. |

### Field Explanations — Distribution

The distribution section balances the transaction. Debits must equal credits; the voucher cannot be saved until they do. Up to 10 GL accounts may be used.

| Field | Description |
|---|---|
| **GL Account - Dept** | GL account and department. Defaults from the customer's Default GL Sales field if defined. F2 / Lookup to search the chart of accounts. |
| **Description** | Filled automatically from the GL account master after account selection. |
| **D/C** | Debit or Credit indicator. Defaults to the value required to balance; can be overridden. |
| **Amount** | Distribution amount. Defaults to the amount needed to balance. |

### Voucher Types in Detail

**Standard AR Voucher (type A).** Total Amt posts as a debit to the AR account. The distribution must be a net credit.

**Credit Memo (type B).** Total Amt posts as a credit to the AR account. The distribution must be a net debit.

**Cash Transaction (type C).** Cash received that bypasses formal invoicing. On save, the program prompts for bank account, customer check number, and deposit number. The debit entry is to the cash account; credits come from the distribution section. The AR default account is bypassed. The transaction still appears on the customer statement and on AR-F aging as a paid invoice when fully paid items are included.

**Beginning Balances (types D and E).** Used to enter opening balances when cutting over from another accounting system. These post to the aging and voucher files but **not** to the General Ledger. Type `D` for opening invoices; type `E` for opening credit memos.

### General Program Operation

On opening, a list of existing vouchers is shown. Options: **Add** a new voucher, **Copy** an existing one (all fields pre-filled except voucher number), **View** in read-only mode, or **Reverse** (prompts for reversal date and creates a reversing entry).

When adding: enter customer code, voucher number (or leave blank), type, description, date, terms, and total amount. Optionally specify a G/L Dept to apply a department code throughout the transaction. Then enter distribution accounts until the transaction is balanced. When balanced and confirmed, posting:
- Adds the voucher to voucher records.
- Adds the transaction to the AR transaction file.
- Updates outstanding credit or invoice balances in the customer file.
- Posts to General Ledger and Sales Journal.

---

## AR-C — Record Payments

*Source: [ar-c_record_payments.htm](../../../samples/chm/extracted/ar-c_record_payments.htm)*

**Purpose.** Use this program to record customer payments, apply outstanding credits, record NSF (non-sufficient funds) checks, enter prepayments, take early-payment discounts, apply credits toward invoices, record partial payments, and split a single payment across multiple customers.

### Multi-Currency Processing

When multi-currency is enabled (IM-A):
- A credit in source currency is made to the AR Control Account; the offsetting debit in source currency goes to this currency's Bank Account.
- If the Pay option in IM-A is set to `Y`, a second transaction converts the payment to base currency using the rate in IM-C, crediting F/E Gain/Loss-Trxns and debiting F/E Gain/Loss-Conversions. Gain/loss is recognized at transaction time rather than at the Convert to Base Currency batch run.

### Credit Card Processing

When X-Charge or Payment Innovators is configured in SD-P, a Credit Card button appears after the customer is selected and the cursor advances to the Date field. The window shows the customer's card on file (editable for a different card or one-time charge). Enter the payment amount and click Process. On approval, the approval code (prefixed by `V` = Visa, `M` = MasterCard, `A` = Amex, `D` = Discover) is entered as the Check Number; processing then continues normally.

### Importing Remittance Advice

For customers paying many invoices on one check, payment detail can be imported from a comma-delimited file: column 1 = invoice number, column 2 = net amount paid, column 3 = discount taken. No `$` or comma formatting in amounts. An Import Payments button appears on the invoice selection screen; after import the screen shows applied funds and highlights exceptions (amount mismatches or unmatched invoice numbers). Exceptions can be reviewed via the Exceptions button and edited before saving.

### Field Explanations

| Field | Description |
|---|---|
| **Customer Code** | Code of the customer making the payment. F2 / Lookup to select. |
| **Customer Name** | Filled automatically. |
| **Telephone** | Filled automatically from the customer file. |
| **Last Sale** | Date of the last sale to this customer. |
| **Last Payment** | Date of the last payment received from this customer. |
| **Credits** | Total dollar amount of outstanding unapplied credits. |
| **Out Deposits** | Total dollar amount of outstanding advance deposits. |
| **Out Invoices** | Total dollar amount of open invoices available for payment application. |
| **Payment Date** | Date payment was received. |
| **Check Amount** | Amount of the check. Enter as a negative number for NSF checks or payment reversals. Enter `$0` to apply existing credits to invoices with no new cash. |
| **Check Number** | Up to 20-character alphanumeric reference. Must be unique per customer because it is used to identify the transaction for reversal. Use a date code or unique reference for wire transfers, credit card payments, etc. |
| **Deposit Number** | User-defined 6-digit numeric. Identifies the bank deposit for reconciliation via GL-J Reconcile Check Register. |

### General Program Operation

1. Enter customer code, payment date, check amount, check number, and deposit number.
2. The program asks: "Use all unapplied credits?" `Y` = all credits are automatically selected. `N` = manually select which credits to use.
3. The program asks: "Apply payment to all outstanding invoices, oldest first?" `Y` = automatic application with early-payment discounts where applicable; prior payments can also be changed under this option. `N` = proceeds to the individual invoice selection screen.

**Individual invoice selection:** A window shows all open invoices and unapplied credits. Highlight an invoice and press Enter or click to open an entry window. Enter the **Discount** (if applicable) and the **Applied** amount (all or partial). Repeat for additional invoices. To remove an application, re-select the invoice and enter zeros in Discount and Applied, or press Ctrl+U to clear.

Press Esc when finished. If unapplied funds remain:
- If you decline to apply to open items and confirm posting, you are asked whether to apply the balance to a different customer. If yes, you return to the Customer Code field to continue applying to another customer.
- If no cross-customer application, you are asked whether to save the balance as a Deposit: `Y` credits the Customer Deposit liability account in GL and creates a "Deposit on Account" entry; `N` credits Accounts Receivable and creates an "Unapplied credit" entry.

On confirmation, a bank account selection appears (if multiple bank accounts exist). The transaction is then saved: customer file, check register, and AR files are all updated.

**Recording a Deposit through AR-C.** Enter customer code, date, amount, check number, and deposit number. When the invoice window appears, do not apply any money. Press Esc, decline to apply to open items, confirm posting, and decline cross-customer application. When asked whether to save as a Deposit, answer `Y`. The funds post to the Customer Deposits GL liability account.

### Reversal / NSF Check

Both a payment reversal and an NSF check are entered as **negative amounts**. The difference: a reversal always posts to the same date as the original entry; an NSF can post to the bank notification date. The program matches the check number and amount against prior entries to locate the original invoices for reinstatement. If there are multiple entries with the same check number, the original payment date is requested for disambiguation. If no unique match is found, a new voucher entry is created rather than reversing prior entries. Note: commissions already processed on the original payment are not reversed.

---

## AR-D — Charge Interest on Invoices

*Source: [ar-d_charge_interest_on_invoices.htm](../../../samples/chm/extracted/ar-d_charge_interest_on_invoices.htm)*

**Purpose.** Use this program to automatically create interest charge invoices (as AR line items) for customers with overdue balances. Only customers with **Charge Interest?** = `Y` in AR-A are processed. Run this program before printing financial statements or customer statements to ensure current finance charges are reflected. Interest accrues from the invoice due date (per each invoice's terms code), and only for the number of days since the program was last run.

Hard-copy invoices for generated finance charges can be reprinted via SO-F Print Invoices in reprint mode.

### Prerequisites

- A GL account for interest income must be set up in AD-A General Ledger Defaults.
- The interest rate and the number of days until delinquent must be configured in SD-P Accounts Receivable Defaults.

### General Program Operation

The program defaults the processing date to today; enter a different date if needed. The program runs automatically — no manual per-customer action is required. As each customer is checked its code is displayed on screen.

Processing results for each qualifying customer:
- Advances the next invoice number.
- Updates the invoice balance in the customer file.
- Adds finance charge records to the AR transaction file.
- Creates invoice header and line item records in invoice history.
- Posts to General Ledger and Sales Journal.

---

## AR-E — Print Statements

*Source: [ar-e_print_statements.htm](../../../samples/chm/extracted/ar-e_print_statements.htm)*

**Purpose.** Prints Accounts Receivable statements for customers whose **Statement?** field in AR-A is `Y`. Statements can be printed on the universal pre-printed form or on plain paper, depending on the setting in SD-P Accounts Receivable Defaults. The SD-P screen also controls whether invoice age is calculated as days since posting or days past due.

### General Program Operation

**Customer selection.** Enter a from/thru range of customer codes and/or customer classes. Only customers with **Statement?** = `Y` receive a statement.

**Statement date.** Enter a date or press Enter for today's date.

**Aged format.** Enter `Y` to print the aged statement format. You will be prompted for the number of days of payments to include. The aged format lists open invoices in the first section and itemized payments in the second. This format always uses form `ENARE4.RTM` regardless of the SD-P default.

**Overdue-only / zero-balance suppression.** Options to print only overdue accounts and to suppress accounts with a zero balance.

**Deposits.** Choose whether customer deposits are included on the statement and whether they are included in the total balance due.

**Open vs. all items.** Answer `N` to "Print Items with Open Amounts Only?" to include previously paid items alongside open items.

**Balance forward.** Option to summarize transactions before a specified date into a single balance-forward amount; enter the balance-forward date.

**History limit.** When including fully paid items, enter how far back into the past to reach.

---

## AR-F — Print Aging

*Source: [ar-f_print_aging.htm](../../../samples/chm/extracted/ar-f_print_aging.htm)*

**Purpose.** Produces AR aging, transaction listing, and past-due reports for one or all customers. The report can be accurately backdated to reconstruct open balances as of any prior date.

Three report types are available:

1. **AR Listing** — transaction listing of individual invoices, oldest first, with invoice date, number, customer code, name, description, amount, terms type, and age in days. Can include all invoices or open only; deposits optional.
2. **AR Aging** — amounts bucketed into aging columns (current, 30, 60, 90+ days or custom periods). Options: open item detail or customer totals only. Aging is calculated from invoice date.
3. **AR Past Due** — identical to AR Aging but aged from each invoice's terms due date rather than invoice date.

Changing aging periods in this program for a specific print run does not affect the default periods stored in SD-P Accounts Receivable Defaults.

### Multi-Currency Reporting

When multi-currency is enabled (IM-A), AR is maintained in source currency. The report can be printed in:
- **Source currency (`S`)** — amounts print in their original currency. Mixed-currency grand totals are meaningless.
- **Base currency (`B`)** — all amounts are converted using exchange rates at the time of invoicing. Run the Convert to Base Currency routine in IM-B before printing in base currency to reconcile with GL AR Control and AR Conversion accounts.

International fields (visible when multi-currency is enabled):
- **Currency** — from/thru range of currency codes to confine the report to specific currencies.
- **Print in Base or Source Currency?** — `B` or `S` as described above.

### General Program Operation

1. Enter the as-of date (defaults to today; entering a prior date reconstructs the aging for that date).
2. Select the report type: AR Aging, AR Listing, or AR Past Due.
3. Indicate whether to limit to customers on credit hold only.
4. Indicate whether to include deposits. Note: including deposits affects grand totals; exclude deposits if reconciling against the GL AR balance.
5. Enter a from/thru range of customer codes. Optionally filter by customer class.

**AR Aging specific options:**
- Detail level: `1` = Detail, Open Items Only; `2` = Customer Totals Only.
- Sort order: by customer code, name, or alpha sort field.
- **Print Follow-up Notes?** — integrates with Contact Manager. If yes, enter your Contact Manager password and a from/thru range of follow-up codes and dates. Those notes print under each customer's totals on the report.
- Aging periods: use defaults from SD-P or enter custom period thresholds on-the-fly. Keep Period 1 at zero to include all current invoices.

**AR Listing specific options:**
- Always a detail report; customer totals-only option is not available.
- Terms type filter: select from the terms types in SM-D or choose All Types.

**AR Past Due:** same selection as AR Aging, with aging calculated from terms due date.

---

## AR-G — Print Customer Code and Name

*Source: [ar-g_print_customer_code_and_name.htm](../../../samples/chm/extracted/ar-g_print_customer_code_and_name.htm)*

**Purpose.** Produces a listing of customer codes, names, and telephone numbers. The report template is `T6ARG1.RTM`; additional columns from the customer master can be added via TA-M Forms Editor to make this an all-purpose customer listing.

### General Program Operation

Indicate whether Active or Inactive customers are included. An inactive customer is one with no open invoices, credits, or sales orders and no sales/AR activity within the specified number of days.

Selection criteria available:
- From/thru range of customer codes
- Customer classes
- Salespersons
- States
- Start dates
- Last sale date
- YTD sales

Sort options: by customer code, name, or alpha sort code.

Special filters:
- **Print Customers on Credit Hold?** — `Y` returns only credit-hold customers.
- **Print Customers over the Credit Limit?** — `Y` returns only customers exceeding their credit limit.
- Setting both to `Y` returns only customers that are simultaneously on credit hold **and** over their credit limit.

---

## AR-H — Print Customer General Info

*Source: [ar-h_print_customer_general_info.htm](../../../samples/chm/extracted/ar-h_print_customer_general_info.htm)*

**Purpose.** Produces a full-detail listing of all fields from the customer file, excluding sales totals.

### General Program Operation

The selection screen is identical to AR-G. Specify a range of customer codes and/or customer classes plus any other selection criteria offered. If no limits are entered, all customers are printed.

---

## AR-I — Print Customer Mail Labels

*Source: [ar-i_print_customer_mail_labels.htm](../../../samples/chm/extracted/ar-i_print_customer_mail_labels.htm)*

**Purpose.** Prints customer mailing labels from the customer master file.

### Label Formats

| Format | Label Stock |
|---|---|
| 1-up | Standard 3-1/2" × 15/16" continuous-form labels |
| 2-up | Avery 5161 laser labels |
| 3-up | Avery 5160 laser labels |

### General Program Operation

Indicate Active or Inactive customers. An inactive customer has no open invoices, credits, or sales orders and no sales/AR activity within the specified number of days.

Selection criteria: from/thru customer codes, customer classes, zip codes, salespersons, states, start dates, last sale date, and YTD sales. If no limits, labels are produced for all customers.

Sort order: by zip code (for bulk-mail postal discounts) or by customer code.

---

## AR-K — Print Sales Tax Report

*Source: [ar-k_print_sales_tax_report.htm](../../../samples/chm/extracted/ar-k_print_sales_tax_report.htm)*

**Purpose.** Generates a report of the amounts owed to each sales tax authority. Serves as a preview before running AR-L Transfer Sales Taxes or as an audit trail for a specific prior period. Two formats are available: summary and detail.

### General Program Operation

1. **Include status:** Paid, Outstanding, or Both. "Paid" and "Outstanding" refer to whether the taxes have been transferred to AP (via AR-L), not whether the customer has paid the invoice.
2. **Tax authority range:** from/thru range of tax authority codes. Leave blank for all authorities.
3. **Purchases or Sales:** available when Track PO Taxes Using Tax Groups is `Y` in SD-C Purchase Orders Defaults.
4. **Currency:** Source or Base. Available when multi-currency is enabled.
5. **Summary or Detail.**
6. **Include monthly totals:** `Y`/`N`.
7. **Date range:** from/thru invoice dates.

---

## AR-L — Transfer Sales Taxes

*Source: [ar-l_transfer_sales_taxes.htm](../../../samples/chm/extracted/ar-l_transfer_sales_taxes.htm)*

**Purpose.** Transfers accumulated sales tax liabilities from GL liability accounts to Accounts Payable vendor records, where they can be selected for payment by AP check run. The amount outstanding is updated each time invoices are posted and with every transfer. Run this program whenever sales taxes are due for payment.

### Prerequisites

- Tax codes must be configured in SM-E Enter Tax Codes, each with an associated AP vendor.
- AP vendor records for each tax authority must exist in AP-A Enter Vendors.

### Multi-Currency Processing

Although sales tax payable is originally converted and posted in base currency at transaction time, the owed amount is stored in source currency for this program. The transfer currency depends on how the tax authority vendor is set up in AP-A:

**Vendor uses source currency:**
- A credit in source currency is made to this currency's AP Control account.
- The source currency amount is converted to base currency; a debit for that amount is made to the default Sales Tax Payable account.
- The difference between the two amounts is posted to F/E Gain/Loss-Trxns.

**Vendor uses base currency:**
- The source currency amount is converted to base currency; a credit for that amount is made to the base currency AP Control account.
- The debit is made to the default Sales Tax Payable account.

### General Program Operation

If no amounts are outstanding, a message is shown and the program returns to the main menu.

If amounts are outstanding, the cursor is placed in the **Amount to Transfer** field next to each authority's **Amount Outstanding**. The full outstanding amount is offered as default. Press Enter to accept or type a partial amount. Repeat for each authority.

Press F10 / Save to record. Partial transfers are allowed — press F10 at any time to save only the authorities where you have entered a transfer amount. On save:
- The Next AP Invoice Number is updated.
- Vendor account outstanding amounts are updated.
- The transaction posts to General Ledger and Purchases Journal.
- The outstanding tax amounts in SM-E are updated.

### GL Impact Summary

| Event | Debit | Credit |
|---|---|---|
| Invoice posted with sales tax | Sales Tax Payable (liability) | — (already credited at invoice posting) |
| AR-L transfer (source-currency vendor) | Sales Tax Payable | AP Control (source currency) + F/E Gain/Loss |
| AR-L transfer (base-currency vendor) | Sales Tax Payable | AP Control (base currency) |

---

## AR-M — Enter Customer Refund

*Source: [ar-m_enter_customer_refund.htm](../../../samples/chm/extracted/ar-m_enter_customer_refund.htm)*

**Purpose.** Processes a cash refund of customer credits or deposits that are not being applied to Sales Orders. The refund can be issued immediately as a manual check or posted to Accounts Payable as a voucher for payment later.

### General Program Operation

1. Enter the customer code. The program prompts whether to use the same code in the Vendor file to process the payment. Press Enter to accept; the name and address populate automatically. If a vendor already exists with the same code, you will need to assign a different vendor code for this customer.

2. A list of available credits and deposits for this customer is displayed. Click the item(s) to be refunded and confirm or edit the amount (partial refunds are supported).

3. After selecting, click Done and choose the payment method:
   - **AP Voucher** — prompts for invoice number, invoice date, description, and payment terms. The voucher is added to AP for later payment.
   - **Credit Card** — the X-Charge processing screen opens to process the refund.
   - **Manual Check** — prompts for bank account, check number, date, and description. An opportunity to print the check is provided.

4. The program confirms the transaction is about to be posted immediately and asks for final confirmation.

---

## AR-N — Enter/Print Sales Order Deposits

*Source: [ar-n_enter_print_sales_order_deposits.htm](../../../samples/chm/extracted/ar-n_enter_print_sales_order_deposits.htm)*

**Purpose.** Commonly used by job shops and custom manufacturers who require advance deposits before processing special orders. Allows entry of customer deposits (prepayments) against a specific sales order or on account against future sales orders.

Two key benefits over entering deposits through AR-C:
1. When sales order acknowledgments or invoices are printed, the deposit appears in the subtotal section and is deducted from the total order amount.
2. GL posting is handled automatically. The deposit is first credited to the Customer Deposits liability account (AD-A General Ledger Defaults). When the order ships and the invoice posts, the deposit is debited from Customer Deposits and credited against Accounts Receivable, and is automatically applied against the correct invoice in the aging file — eliminating manual application.

### Credit Card Processing

When X-Charge is configured in SD-P, a Credit Card button appears after customer selection and cursor advancement to the Date field. The approval code (prefixed by card type: `V`/`M`/`A`/`D`) is entered as the Check Number; the deposit can then be linked to a sales or service/repair order.

### General Program Operation

**Entering a new deposit.** On startup, a scrolling list of open deposits is shown. Press Insert / click Add. Enter:
- **Customer Code** — F2 / Lookup to select.
- **Deposit Date**
- **Check Number**
- **Deposit Amount**
- **Currency** — if multi-currency is enabled.
- **Bank Account** — the destination bank account.
- **Sales Order** — optional link to a specific sales order. If linked, the deposit applies automatically when that order's invoice is posted.

**Editing an existing deposit.** Select the deposit from the opening list and press Enter or click it. Only the linked **Sales Order** and the **Description** fields can be changed. To change any other field, delete the deposit (you will be prompted for a reversal date) and re-enter it from scratch.

**Printing a listing of open deposits.** Click the Report button on the opening window. Filter by from/thru customer codes or from/thru deposit date range.

---

## AR-P — Generate Dun Letters

*Source: [ar-p_generate_dun_leters.htm](../../../samples/chm/extracted/ar-p_generate_dun_leters.htm)*

**Purpose.** Automatically generates collection letters for customers with overdue invoices. A hierarchy of form letters is configured, each corresponding to a progressively greater number of days past due from the terms due date. The program selects the appropriate letter for each customer based on the age of their oldest past-due invoice.

**Requirement:** A customer must exist in the Contact Accounts file in the Contact Manager module before a dun letter can be sent. Use CM-K Add Customers to Account File to add customers in bulk. Leaving the from/thru customer code fields blank adds any customer who lacks a Contact Account record, ensuring all customers are eligible for dunning.

### General Program Operation

1. **Print Labels?** Enter `N` to print letters. After letters are printed, re-run with `Y` to print matching address labels (dot matrix or laser).

2. **Customer range.** From/thru range of account codes to limit the run.

3. **Form letter criteria table.** Enter days past due in the left column and the corresponding form letter code in the right column. Example: `90` days with letter code `C3` means any customer with an invoice more than 90 days past due from its terms due date will receive letter C3. Build a descending hierarchy (highest days first, lowest days last) so the program matches the most severe letter first.

4. The table is persistent — it retains the last entries, so it is typically set up once and only changed when the dunning strategy changes.

5. Press F10 / Save to process. The program:
   - Reviews each customer's AR transactions.
   - Locates the oldest past-due invoice.
   - Matches that invoice against the criteria table (most-severe first).
   - Marks the customer for the appropriate form letter.
   - Updates the customer's **Last Dun?** field in AR-A with the dun letter code and date.

---

## AR-Q — View Customer Information

*Source: [ar-q_view_customer_information.htm](../../../samples/chm/extracted/ar-q_view_customer_information.htm)*

**Purpose.** Read-only inquiry into the customer master. Presents the same screens and fields as AR-A Enter Customers but no changes can be entered or saved.

Useful for staff who need to review customer information (addresses, credit status, balances, contacts) without having edit access to customer records.

---

## AR-R — Print AR Payment History

*Source: [ar-r_print_customer_payment_history.htm](../../../samples/chm/extracted/ar-r_print_customer_payment_history.htm)*

**Purpose.** Produces a listing of customer payments for credit assessment or cash flow projection purposes.

### General Program Operation

Selection criteria:
- From/thru range of customer codes.
- From/thru range of check dates.
- From/thru range of check numbers.
- When multi-currency is enabled (IM-A), choose to print in **base** or **source** currency.

---

## Cross-references

| Related Program | Relationship |
|---|---|
| **SM-D Enter Terms Table** | Payment terms used by AR-A (customer default terms) and AR-B (voucher terms). |
| **SM-E Enter Tax Codes** | Tax codes and associated AP vendor records consumed by AR-L Transfer Sales Taxes. |
| **SM-F Enter Tax Groups** | Tax groups assigned to customers in AR-A; drive sales tax calculations in SO and AR. |
| **SM-I-A Enter Lead Source Codes** | Lead source codes used in AR-A customer master. |
| **SM-I-B Enter Territory Codes** | Territory codes used in AR-A customer master. |
| **SD-M Sales Orders Defaults** | Controls auto-invoice numbering (used by AR-B), credit checking behavior, and other SO defaults that interact with AR. |
| **SD-P Customer/AR Defaults** | Controls statement form (plain paper vs. universal form), aging method, interest rate, days-to-delinquent, credit-hold order prevention, recycle fee item, Days to Pay calculation method, and credit card processing path. |
| **AD-A General Ledger Defaults** | Defines the Customer Deposits liability GL account (used by AR-C and AR-N) and the interest income GL account (used by AR-D). |
| **SO-A Enter Sales Orders** | The correct path for vouchers affecting inventory or commissions. AR-A customer data (terms, tax, salesperson, price/discount codes) defaults into SO-A. |
| **SO-E Release Sales Orders** | Respects the Allow Backorders flag set in AR-A. |
| **SO-F Print Invoices** | Used to reprint hard-copy invoices for AR-B vouchers and AR-D finance charges. |
| **SO-Q-D Enter Price Codes** | Price codes assigned to customers in AR-A. |
| **SO-Q-F Enter Discount Codes** | Discount codes assigned to customers in AR-A. |
| **GL-J Reconcile Check Register** | Uses the Deposit Number from AR-C to clear payments from the bank reconciliation. |
| **AP-A Enter Vendors** | Vendors for tax authorities, required before running AR-L. Also used by AR-M for customer refund AP vouchers. |
| **IM-A International Configuration** | Activates multi-currency processing that affects AR-B, AR-C, AR-F, AR-K, AR-L, and AR-R. |
| **IM-B Enter Multiple Currencies** | Currency definitions and the Convert to Base Currency routine needed before AR-F base-currency reconciliation. |
| **IM-C Enter Currency Exchange Rates** | Exchange rates used in multi-currency AR-B and AR-C processing. |
| **CS-A Enter Salespersons** | Salesperson default commission rates used when AR-A commission fields are blank. |
| **CM-A Enter Contact Accounts** | Shares the customer code with AR-A; toggle between them with PgUp. Required for AR-P dunning. |
| **CM-K Add Customers to Account File** | Bulk-populates Contact Manager records for all AR customers, enabling AR-P dunning. |
| **TA-M Forms Editor** | Used to customize RTM report templates such as `T6ARG1.RTM` (AR-G) and statement/invoice forms used across the AR module. |
