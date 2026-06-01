# AP — Accounts Payable

Status: verified (text distilled from the vendor's help file).

*Source: EvoHELP.CHM → Accounting → Accounts Payable (21 topics).*
*Extracted HTML in [samples/chm/extracted/](../../../samples/chm/extracted/).*

The Accounts Payable module manages the full lifecycle of money owed to outside vendors: from establishing vendor master records and entering invoices (both free-form vouchers and PO-matched invoices), through payment selection and check printing, to historical reporting and year-end 1099 filing. AP posts to the General Ledger via the Purchases Journal (invoices) and Cash Disbursements Journal (checks), and it interfaces directly with the Purchase Orders module, the GL check register, and the International/Multi-Currency subsystem.

---

## Contents

- [AP-A — Enter Vendors](#ap-a--enter-vendors)
- [AP-B — Enter Vouchers](#ap-b--enter-vouchers)
- [AP-C — Enter Purchase Order Invoices](#ap-c--enter-purchase-order-invoices)
- [AP-D — Enter Scheduled Payment Dates](#ap-d--enter-scheduled-payment-dates)
- [AP-E — Print Vouchers/Invoices Due by Date](#ap-e--print-vouchersinvoices-due-by-date)
- [AP-F — Pick Vouchers/Invoices to Pay](#ap-f--pick-vouchersinvoices-to-pay)
- [AP-G — Print Pro Forma Check Register](#ap-g--print-pro-forma-check-register)
- [AP-H — Print Checks](#ap-h--print-checks)
- [AP-I — Print Aging](#ap-i--print-aging)
- [AP-J — Print Vendor Code and Name](#ap-j--print-vendor-code-and-name)
- [AP-K — Print Vendor General Info](#ap-k--print-vendor-general-info)
- [AP-M — Print Vendor Labels](#ap-m--print-vendor-labels)
- [AP-N — Enter Vouchers (Edit Address)](#ap-n--enter-vouchers-edit-address)
- [AP-O — Enter Recurring Vouchers and Templates](#ap-o--enter-recurring-vouchers-and-templates)
- [AP-P — Generate Recurring Vouchers](#ap-p--generate-recurring-vouchers)
- [AP-Q — Void AP Check](#ap-q--void-ap-check)
- [AP-R — Print AP Payment History](#ap-r--print-ap-payment-history)
- [AP-S — Print 1099 Forms](#ap-s--print-1099-forms)
- [AP-T — Check and Invoice Inquiry](#ap-t--check-and-invoice-inquiry)
- [AP-V — Enter AP Deposit](#ap-v--enter-ap-deposit)
- [AP-X — Print Invoice Detail](#ap-x--print-invoice-detail)
- [Cross-references](#cross-references)

---

## AP-A — Enter Vendors

*Source: [ap-a_enter_vendors.htm](../../../samples/chm/extracted/ap-a_enter_vendors.htm)*

**Purpose.** Use this program when beginning to purchase from a new vendor, or when updating a vendor's name, address, telephone number, or company contact. Also used to add vendor records for payment of sales tax, federal tax, and payroll withholding liabilities. Vendor information entered here is accessible when creating purchase orders in PO-A. Payment terms must already be set up in SM-D before completing a vendor record.

### Standard Vendor Information Fields

| Field | Size | Notes |
|---|---|---|
| **Vend Code** (Required) | 10 chars alphanumeric | Single/double quotes and commas not allowed; other special characters such as `#` or `-` are allowed. Drives sort order on most vendor reports. Recommended format: first 3 letters of first name word + first 3 letters of second name word. |
| **Alpha Sort** | 6 chars | Defaults to first 6 chars of vendor name; used for alphabetical sorting on reports. Can be overridden. |
| **Vend Name** | 30 chars | The actual vendor company name. |
| **Address 1 / Address 2** | 30 chars each | Two street address lines. |
| **City** | 26 chars | Vendor city. |
| **State** | 2 chars | Standard 2-character state code. |
| **Zip** | 10 chars | Zip or postal code. |
| **Country** | 30 chars | Used for multi-country vendor files. |
| **Contact 1** | 30 chars | Primary contact person. Three additional contacts accessible via the *Other Contacts* button. |
| **Telephone** | 25 chars | Main phone number. |
| **Fax** | 25 chars | Fax number. |
| **Remittance Address** | — | Address printed on checks (AP-H). If blank, the standard vendor address is used. Vendor name need not be repeated here. |
| **Tax ID No** | 15 chars | Federal tax ID for 1099 reporting. Used by AP-S. |
| **Tax Group** | — | Sales tax authority for this vendor. Only active if *Track PO Taxes using Tax Groups* = `Y` in SD-C. |
| **Send 1099?** | checkbox | If checked, AP-S will include this vendor in the 1099 print run. |
| **Customer at This Vendor** | — | Your customer account number in the vendor's own accounting system. |
| **Class Cd** | 4 chars | Optional grouping code for vendor reports (e.g., out-of-state vendors, wholesalers, manufacturing vs. administrative vendors). |
| **Terms Cd** (Required) | — | Default payment terms for this vendor. Defaults into PO-A and AP-B/AP-C. Terms codes must be pre-defined in SM-D. |
| **Default GL Exp Acct** | — | Default GL expense account for AP-B voucher entry, eliminating repetitive lookups. For PO-based purchases the GL posting is driven by item class (SM-C). |
| **Start Dt** | date | Date business with this vendor began (typically the first PO date). |
| **Ship Via** | — | Preferred shipping method; defaults into purchase orders. |
| **Print File Lbls** | checkbox | If checked, vendor receives a label when AP-M is run in File Label mode. |
| **FOB** | — | Free-on-board point; defaults into purchase orders. Can be left blank. |
| **Bank Account and Routing Numbers** | — | Vendor's banking information for ACH or other electronic payments. |

### International Fields

Visible only when the relevant feature is activated in IM-A International Configuration.

- **Currency** — Source currency for this vendor's transactions. Set up in IM-B. Can be overridden per purchase order.
- **Duty Code** — 3-character landed-cost duty code (set up in IM-E) representing the Country of Import for duty-rate calculation. Active when landed-cost processing is on in IM-A.
- **Tax-In Code** — Excise tax code (set up in IM-G). Required when excise tax processing is active in IM-A.

### Current Status Totals (read-only, system-maintained)

- **Outstanding Inv Amts** — Dollar total of open invoices owed to this vendor.
- **Outstanding Credits** — Dollar total of unapplied credits from this vendor.
- **Last Purch** — Date of the last PO received from this vendor.
- **Last Payment** — Date of the last payment made to this vendor.

### Other Features

- **Web Site** — URL of the vendor's website.
- **Info Button** — Opens a screen for user-defined miscellaneous fields. Labels configured in SM-J-U Configure Vendor Miscellaneous Info. Useful for ISO certification status or other approval tracking.
- **Notes Button** — Opens a free-text notes window for the vendor record.

### General Program Operation

**Creating a new vendor:** Click *Add*, enter a new *Vend Code*, and complete the fields. If the code already exists the matching record displays; press F3 to clear and use a different code.

**Changing an existing vendor:** From the opening vendor list, double-click or highlight and click *Edit*. All fields except history totals are editable. Save to update the vendor file, making the changes available to PO, voucher, aging, and contact management operations.

**Deleting a vendor:** Both *Outstanding Inv Amts* and *Outstanding Credits* must be `$0.00`, and no open purchase orders may exist for the vendor. If outstanding balances or open POs exist, deletion is blocked with an error message. For vendors with purchase or payment history, use AM-O Archive/Purge Vendor Data instead of deleting.

---

## AP-B — Enter Vouchers

*Source: [ap-b_enter_vouchers.htm](../../../samples/chm/extracted/ap-b_enter_vouchers.htm)*

**Purpose.** Enter all vendor invoices that are *not* related to purchase orders — rent, lease payments, phone bills, repair bills, utility charges, tax liabilities, etc. Also used to record vendor credits, enter reversing vouchers with credit memos, and record manual checks. Inventory purchases normally flow through PO-A / AP-C instead.

### Multi-Currency Processing

If multi-currency is enabled in IM-A, vouchers can be entered in a foreign (source) currency. The debit side converts to base currency at the rate in IM-C; the credit side posts in source currency to that currency's *AP Control* account.

### Auto-Tax Distribution

Available when multi-currency is enabled and *Track PO taxes using tax groups?* = `Y` in SD-C. The program calculates the tax amount and posts it to the default *Sales Tax Payable* account (in base currency). The user is asked whether tax is already included in the voucher amount:

- **Tax not included:** AP is credited for the full voucher amount, plus an additional credit to Sales Tax Payable.
- **Tax included:** The AP credit is reduced by the tax amount so that AP credit + Sales Tax Payable credit = voucher total.

Tax amounts owed to the authority are stored in source currency in the sales tax transfer file and paid via AR-L Transfer Sales Taxes.

### Voucher Entry Fields

| Field | Notes |
|---|---|
| **Vend Code** (Required) | 10-char vendor code. If not found, offers to add a new vendor inline (same screen as AP-A). |
| **Name** | Auto-filled from vendor file. |
| **Inv Num** (Required) | Vendor's invoice/bill number, 20 chars. |
| **Voucher Date** | Vendor invoice date; used for AP aging. Defaults to current date. Warning if not in current calendar year. |
| **Type** (Required) | Pop-up selection: `A` AP Voucher, `B` Credit Memo, `C` Manual Check, `D` Beg Balance, `E` Beg Bal Credit, `F` Template. |
| **GL Post Date** | Date for General Ledger posting. Defaults to current date. Cannot post to a closed period or before the invoice date. Controls which invoices appear on AP Aging as of a given date. Warning if not in current calendar year. |
| **Desc** | 25-char description; prints on posting reports and on the vendor's check stub. |
| **Terms** (Required) | Payment terms code. Pop-up window shows available terms from SM-D; vendor default is pre-highlighted. |
| **Total Amt** (Required) | Invoice total, 12 digits with 2 decimal places. |
| **Currency** | Source currency code (multi-currency only). Defaults from vendor master. |
| **Schedule Date** | Optional override of the terms-calculated due date. |
| **Job Number** | Optional; header entry defaults to all distribution lines but can be changed per line. If setting is `R` (Required), must be selected from the preset list in SM-P-F. |

### Distribution Fields

Each voucher requires balancing GL distribution entries that net to the voucher amount. Up to 75 GL account/department combinations are supported.

| Field | Notes |
|---|---|
| **GL Account-Dept** | Offsetting expense or other GL account. Use vendor default from master record or look up via F2/Lookup. Do NOT distribute to the AP control account — the program posts one side automatically to the default AP account defined in AD-A. |
| **Description** | Auto-filled from GL master; can be edited. If not edited, the voucher header description pulls in automatically when advancing to Amount. |
| **D/C** | Debit/Credit indicator. Defaults to the value required to balance the transaction; can be overridden. |
| **Amount** | Distribution amount. Program suggests the amount needed to balance; override if splitting across multiple accounts. |
| **Job Number** | Same behavior as header Job Number. |

### Voucher Types — Behavior Summary

| Type | GL Impact | Notes |
|---|---|---|
| **A — AP Voucher** | Posts to Purchases Journal; updates Outstanding Invoice Amt. | Normal vendor bill. |
| **B — Credit Memo** | Posts to Purchases Journal; updates Outstanding Credits. | Vendor owes you money. |
| **C — Manual Check** | Posts to both Purchases Journal and Cash Disbursements Journal; adds to check register and AP payment history. | For retail/COD purchases. Bank account and check number required. Optional check printing. |
| **D — Beg Balance** | Posts to AP/aging files only — no GL posting. | System cutover starting balances only. |
| **E — Beg Bal Credit** | Posts to AP/aging files only — no GL posting. | System cutover credits only. |
| **F — Template** | Saves as voucher or credit memo using predefined percentage distributions. | Used with AP-O/AP-B templates. |

### Changing an Existing Voucher

Look up the vendor, then look up the voucher by number. If a payment has already been made, the voucher cannot be edited (see Reversing a Paid Voucher below). If unpaid, the program offers:

- **Back out:** Reverses and deletes the transaction.
- **Edit:** Reverses the original, redisplays the screen, allows changes, then saves as a new transaction.

### Reversing a Paid Voucher

A paid voucher cannot be edited; it must be reversed by entering an offsetting transaction:

- **Original was AP Voucher:** Enter a Credit Memo debiting the accounts that were credited originally. Then use AP-F to pick both the original voucher(s) and the credit memo; the net check equals zero.
- **Original was Credit Memo:** Enter an AP Voucher. Use AP-F to pick the voucher and the original credit memo; net result is zero.

---

## AP-C — Enter Purchase Order Invoices

*Source: [ap-c_enter_purchase_order_invoices.htm](../../../samples/chm/extracted/ap-c_enter_purchase_order_invoices.htm)*

**Purpose.** Enter vendor invoices that pertain to purchase orders created in the Purchase Orders module. Items must first be received via PO-C (and, if received to inspection, bought off in PO-J-C) before an invoice can be entered here. Allows comparison of PO prices against vendor invoice prices, with automatic cost corrections to inventory last cost, average cost, and job costs when discrepancies exist. When all items on a PO are fully received and invoiced, the program prompts to close the PO.

One invoice can span multiple purchase orders from the same vendor. Multi-currency restriction: only POs in the specified currency are available. PO Tax Group restriction: only POs in the specified tax group are available.

### Multi-Currency Processing

GL posting for foreign-currency PO invoices: the source-currency *POs Rec'd not Invoiced* account is debited in source currency. Freight converts to base currency (via IM-C rate) and debits *Freight-in* expense. Sales tax converts to base currency and posts to the default *Sales Tax* account. Currency conversion entries for freight/tax go to the *F/E Gain/Loss-Trxns* account.

### Purchase Order Deposit Processing

If deposits (entered in AP-V) are linked to selected POs, AP-C lets you select the deposit and specify how much applies to this invoice. You are asked whether the entered invoice amount is gross (before deposit offset) or net (after). GL posting: total line amounts debit PO/RNI; deposit amount credits AP Deposits; net invoice amount credits AP; tax and freight debit as usual. Only the net invoice passes to AP.

### Vendor Fields

| Field | Notes |
|---|---|
| **PO Number** (Optional) | If the invoice covers a single PO, enter it here; vendor, currency, and tax group auto-populate and the cursor advances to the COD/Invoice field. |
| **Code** | Vendor code for the invoice. |
| **Vendor Name** | Display only — auto-filled from PO/vendor master. |
| **Telephone** | Display only. |
| **Currency** | Defaults from vendor master (if multi-currency enabled). Can be changed; only POs in the specified currency display. |
| **Tax Group** | Defaults from vendor master (if PO Tax Groups enabled). Can be changed; only POs in the specified tax group display. |

### Invoicing Fields

| Field | Notes |
|---|---|
| **Post COD or Invoice** | `COD` bypasses AP, creates a manual check entry, and optionally prints a check. `Invoice` posts to AP for future payment. |
| **Invoice Date** | Vendor invoice date; used for aging. Warning if not in current calendar year. |
| **GL Posting Date** | Defaults to current date. Controls when the invoice appears on AP Aging and which receipts are available (only receipts dated on or before the GL Post date). Cannot post to a closed period or before the invoice date. |
| **Invoice Number** | Vendor's invoice number. If this number already exists for the vendor, the program offers to reverse the prior invoice. |
| **Invoice Amount** | Total to distribute across PO lines (can include or exclude tax/freight). |
| **Filter from PO# / Thru PO#** | Limits the receipt list to a specific PO range. |
| **Check Number** | COD transactions only. |

### Line Item Fields

| Field | Notes |
|---|---|
| **PO #** | Reference — the purchase order number. |
| **Received By** | Reference — person who processed the receipt. |
| **Item** | Item number from PO; display only. |
| **Description** | Item description from PO; display only. |
| **UM** | Unit of measure; display only. |
| **Conv** | UM conversion factor; display only. |
| **Disc%** | Discount percentage from PO; display only. |
| **Qty** | Invoice quantity; defaults to received quantity. Cannot exceed received quantity. |
| **Price** | Invoice unit cost. Defaults to PO line item cost; can be overridden to match vendor invoice. Price changes update inventory last cost, average cost, and job costs. |
| **Extension** | Qty × Price (net of discount). Can enter extension directly; program back-calculates unit cost. |

### Total Fields

| Field | Notes |
|---|---|
| **Payment Terms** | Defaults to terms from the first PO with selected lines; can be changed. |
| **Invoice Amount** | Pre-tax/freight subtotal; display only. |
| **Freight** | Freight charge from vendor invoice; entry field. |
| **Tax** | Sales tax; auto-calculated from PO taxable status or tax group, but can be overridden. |
| **Misc Charges** | Miscellaneous charges and the GL account to apply them to. |
| **Total** | Grand total (goods + freight + tax); display only. |
| **Schedule Date** | Optional override of the terms-calculated due date. |

### Processing Returns to Vendor

Process a negative receipt in PO-C. If a separate debit memo is received from the vendor, enter it as a negative invoice and select the negative receipt lines. If no debit memo is received, select negative receipts alongside positive ones to reduce the net invoice, or enter a zero-dollar invoice to clear offsetting receipts. Rule: negative receipts must be selected before positive ones when combining; a negative invoice can only have negative receipts applied to it.

### Reversing an Invoice

Entering an existing invoice number for a vendor triggers a prompt to reverse the prior invoice. If confirmed, all lines return to RNI (Received Not Invoiced) status, the invoice record is deleted, and reversing GL entries dated the same as the original GL Post Date are made. Reversal is blocked if the original posting period is now closed.

---

## AP-D — Enter Scheduled Payment Dates

*Source: [ap-d_enter_scheduled_payment_dates.htm](../../../samples/chm/extracted/ap-d_enter_scheduled_payment_dates.htm)*

**Purpose.** Schedule invoices for payment on dates that differ from the standard due dates calculated by their terms codes.

### General Program Operation

Enter a vendor code (or look up via the Lookup button). The vendor's name, phone, outstanding credits, outstanding invoices, last purchase, and last payment display.

Enter a default *Scheduled Payment Date*. The program then asks whether to mark all invoices for payment on that date. Regardless of the answer, you can highlight any individual invoice and enter a specific scheduled pay date for it in the entry window at the bottom of the screen. Continue scheduling as desired. Press Esc when done to return to the entry screen.

---

## AP-E — Print Vouchers/Invoices Due by Date

*Source: [ap-e_print_vouchers_invoices_due_by_date.htm](../../../samples/chm/extracted/ap-e_print_vouchers_invoices_due_by_date.htm)*

**Purpose.** Print a report of invoices/vouchers due or overdue within a date range, and optionally mark them all for payment at once — an efficient alternative to selecting invoices one vendor at a time in AP-F. Can also function as a cash requirements forecast by setting due dates into the future.

### General Program Operation

Selection criteria:

- **From/Thru vendor code** — limits by vendor; blank = all vendors.
- **From/Thru vendor class** — further limits by class.
- **Due date range** — enter starting and ending invoice due dates.
- **Include invoices prior to From date** — yes/no option.
- **Net or Discount date** — controls how terms with early-pay discounts are evaluated.
- **Take all discounts past discount date** — yes/no. Tax and freight exclusion from discount calculation is controlled by AD-C defaults (for AP-C invoices).

After printing, the program asks whether to mark all printed invoices as ready to pay. If `Y`, they are added to the AP pro-forma check register (same effect as picking them individually in AP-F). If `N`, nothing is marked.

---

## AP-F — Pick Vouchers/Invoices to Pay

*Source: [ap-f_pick_vouchers_invoices_to_pay.htm](../../../samples/chm/extracted/ap-f_pick_vouchers_invoices_to_pay.htm)*

**Purpose.** Add specific invoices/vouchers to the AP check register so checks can be printed in AP-H. Supports partial payments. Checks are only printed by AP-H for items selected here (or marked in AP-E).

### Display Fields (auto-filled from vendor file)

- **Vendor Name**, **Telephone**, **Outstanding Credits**, **Outstanding Invoices**, **Last Purchase**, **Last Payment**

### General Program Operation

One vendor at a time. After selecting the vendor:

**Paying all invoices:** Answer `Y` when asked whether to apply payment against all outstanding invoices oldest-first. Discounts within terms windows are automatically applied. Partial or zero payments can be entered per invoice even in this mode.

**Applying outstanding credits:**
- Answer `N` — credits remain available to apply manually after selecting invoices; only applicable up to the invoice amount selected.
- Answer `Y` — all unapplied credits are displayed as a negative-balance invoice and applied to open invoices until consumed. Additional invoices can then be selected. A net-$0 payment can be processed to simply clear credits against invoices.

**Choosing individual invoices:** All open invoices for the vendor display (invoice number, date, amount, Applied column). Highlight an invoice and press Enter; the entry window opens at the bottom showing the discount amount (pre-calculated if discountable terms apply; can be changed) and the Applied amount (defaults to full balance; can be reduced for partial payment). Tax/freight exclusion from discount is controlled by SD-Q defaults. Press Esc when done; confirm to save.

**Re-entry to change selections:** Re-enter the vendor code — all prior picks for that vendor are cleared, and you can re-enter amounts from scratch.

**Electronic Payments (ePay button):** After selecting invoices/credits, click *ePay* to post the payment immediately to the check register and payment history file without printing a check. Used for wire transfers, online payments, or credit card payments. Prompts for bank account and a unique reference number. A receipt can be printed as a file copy or to email to the vendor. For credit card payments, set up a "Checking Account" in AD-B that posts to a Credit Card Payable liability account; when the credit card bill arrives, post it as a voucher to the liability account.

---

## AP-G — Print Pro Forma Check Register

*Source: [ap-g_print_pro_forma_check_register.htm](../../../samples/chm/extracted/ap-g_print_pro_forma_check_register.htm)*

**Purpose.** Print a pre-run listing of all items chosen for payment (from AP-E and AP-F) and their net effect on the checking account, *before* actual checks are printed. Run this before AP-H to verify correctness. AP-H also offers to print this report if it has not yet been run.

### General Program Operation

Select the bank account and enter a check date. The report automatically covers all items in the AP check register — including payroll tax and sales tax liabilities as well as normal vendor payments.

- The **Beginning Balance** shown is the current GL balance of the selected checking account.
- Warning issued if there are unposted transactions to the selected bank account in GL-O (balance may be inaccurate).
- Warning issued if any invoice or GL Post date is later than the entered check date (those items cannot be processed — the check date must be on or after both dates).

---

## AP-H — Print Checks

*Source: [ap-h_print_checks.htm](../../../samples/chm/extracted/ap-h_print_checks.htm)*

**Purpose.** Print checks for all invoices/vouchers currently in the AP check register. Run AP-G first to confirm all entries are correct.

### Multi-Currency Processing

GL posting when paying foreign-currency vendors:

- **Pay option in IM-A = N:** Debit to *AP Control Account* (source currency) + credit to *Bank Account* (source currency). No conversion.
- **Pay option in IM-A = Y:** Two transactions — (1) same as above, (2) conversion: the payment amount converts to base currency using IM-C rates; debits *F/E Gain/Loss-Trxns* and credits *F/E Gain/Loss-Conversions*. Gain/loss is recognized at transaction time rather than when the Convert to Base Currency routine runs.

### General Program Operation

The bank account displayed is the one selected in AP-G. If the pro-forma register has not been printed, you can print it before proceeding.

- **Beginning check number** — defaults from AD-B Checking Accounts Defaults; can be changed.
- **Check date** — defaults to current date; can be changed. Invoices dated later than the check date are skipped.
- **Vendor filter** — optionally limit printing to checks for a single vendor (useful for printing one check without deselecting a full check run).

After printing, a screen lists all checks (check number, vendor, amount). Click *Tag All* if all printed correctly; selectively tag checks if some failed (e.g., printer jam). Only tagged checks post.

**On posting:** Vendor credit and invoice balances update; the AP pro-forma register clears; AP Payment History updates; check transactions post to GL and Cash Disbursements Journal; checks are added to the GL check register file for bank reconciliation; the next check number updates in AD-B.

---

## AP-I — Print Aging

*Source: [ap-i_print_aging.htm](../../../samples/chm/extracted/ap-i_print_aging.htm)*

**Purpose.** Print AP aging and invoice listings for one vendor or a range of vendors, with flexible detail and period options. Produces three report types.

### Report Types

| Type | Description |
|---|---|
| **AP Aging** | Columns by age since invoice date. Choices: Open Item Detail (all open invoices) or Vendor Totals only. Aging period boundaries use AD-C defaults or values entered at run time. |
| **AP Listing** | Transaction-level detail: invoice date, number, vendor code and name, description, invoice/payment amounts, amount remaining, terms type, age in days. Can include Open items only, Open and Paid items, or Open and Paid (Exclusive) for items entered within a specified start-to-aging-date range. Sort by vendor code, name, or alpha sort. Terms type filter available. The only report that shows both open and paid items. |
| **AP Past Due** | Same structure as AP Aging but ages from due dates (per terms) rather than invoice dates. |

### Multi-Currency Reporting

If multi-currency is enabled, AP is maintained in source currency. Run the report in source currency (grand totals meaningless if mixing currencies) or in base currency (reconcile to GL AP balances). For base currency reconciliation, run the Convert to Base Currency routine in IM-B first to translate source-currency AP accounts.

International fields: **Currency** (from/thru range) and **Print in Base or Source Currency?** (`B` or `S`).

### General Program Operation

Enter the **Age from date** (defaults to today; entering a past date recreates aging as of that date). Select report type. Enter vendor code range (blank = all) and optional vendor class range. Select detail level. Optionally customize aging period boundaries (leave Period 1 at zero days to include all invoices; changing period boundaries does not affect AD-C defaults).

---

## AP-J — Print Vendor Code and Name

*Source: [ap-j_print_vendor_code_and_name.htm](../../../samples/chm/extracted/ap-j_print_vendor_code_and_name.htm)*

**Purpose.** Print a report of vendor codes, names, and telephone numbers from the vendor file. Can be sorted by vendor code, name, or alpha sort code. The report template `T6APJ1.RTM` can be modified in TA-M Forms Editor to add additional columns from the vendor master, making this a customizable all-purpose vendor listing.

### General Program Operation

Select active, inactive, or both vendors. Enter optional range filters: vendor code, vendor class, state, start date, and last purchase date. Specify sort order: vendor code, name, or alpha sort code.

---

## AP-K — Print Vendor General Info

*Source: [ap-k_print_vendor_general_info.htm](../../../samples/chm/extracted/ap-k_print_vendor_general_info.htm)*

**Purpose.** Print a full vendor master data report including vendor codes, names, addresses, contacts, telephone numbers, and other master file information. Can be sorted by vendor code, name, or alpha sort code.

### General Program Operation

Same selection interface as AP-J. Enter a range of vendor codes or classes (or leave blank for all vendors). Choose sort order.

---

## AP-M — Print Vendor Labels

*Source: [ap-m_print_vendor_labels.htm](../../../samples/chm/extracted/ap-m_print_vendor_labels.htm)*

**Purpose.** Print vendor address information on mailing or file labels.

### Label Formats

| Format | Paper/Label Type |
|---|---|
| 1-up | Standard 3.5" × 15/16" continuous form labels |
| 2-up | Avery 5161 laser labels |
| 3-up | Avery 5160 laser labels |

### General Program Operation

Enter optional range filters: vendor code, vendor class, zip code. Leave blank for all vendors. Sort options: vendor code, name, alpha sort code, or zip code. Can also print file labels for vendors with the *Print File Lbls* flag set in AP-A.

---

## AP-N — Enter Vouchers (Edit Address)

*Source: [ap-n_enter_vouchers_edit_address.htm](../../../samples/chm/extracted/ap-n_enter_vouchers_edit_address.htm)*

**Purpose.** Enter vouchers and optionally change the vendor's Remittance Address that prints on the check — in a single operation.

### General Program Operation

Identical to AP-B Enter Vouchers, with one addition: the Remittance Address can be edited inline. Any change to the Remittance Address entered here **is saved back to the vendor master record** in AP-A.

---

## AP-O — Enter Recurring Vouchers and Templates

*Source: [ap-o_enter_recurring_vouchers_and_templates.htm](../../../samples/chm/extracted/ap-o_enter_recurring_vouchers_and_templates.htm)*

**Purpose.** Set up periodic transactions that recur on a schedule (e.g., monthly rent, weekly payroll tax deposits) or define templates for transactions that recur with the same GL distribution but varying amounts (e.g., utility bills). Once entered, AP-P generates and posts the actual vouchers automatically.

Recurring transactions are assigned a number from the *Next Recurring AP Number* counter in AD-C. Generated vouchers receive numbers from the *Next AP Invoice Number* counter in AD-C.

**Templates** store the same fields as AP-B vouchers except the total amount is always `100` and distribution amounts are percentages. When a template is used in AP-B, the percentages are applied to the actual voucher total.

### Fields Unique to Recurring Entries

| Field | Notes |
|---|---|
| **Inv Num** | Uniquely identifies this recurring record. If left blank, assigned automatically from the *Next Recurring AP Number* in AD-C. Used to retrieve the record for editing. |
| **Selection Code** | One-letter code for grouping/filtering in AP-P (e.g., `L` = lease, `W` = weekly). Optional. |
| **Frequency** | Times per year this transaction occurs (e.g., `52` = weekly, `12` = monthly). Used to calculate *Next Date*. |
| **Maximum Times** | Maximum number of postings per year. AP-P skips transactions that have reached their maximum. |
| **Next Date** | System-calculated next scheduled transaction date, based on initial date and frequency. |

All other fields are the same as AP-B Enter Vouchers. All fields except *Selection Code* are required.

---

## AP-P — Generate Recurring Vouchers

*Source: [ap-p_generate_recurring_vouchers.htm](../../../samples/chm/extracted/ap-p_generate_recurring_vouchers.htm)*

**Purpose.** Run periodically to post the recurring transactions entered in AP-O. Can be limited to a specific selection code range.

### General Program Operation

- **Generate From/Thru Selection Codes** — optionally limit posting to one type of recurring transaction.
- **Generate vouchers due by date** — setting this into the future allows pre-posting transactions before their scheduled date.
- **OK to Continue** — confirm to proceed or return to the AP menu without posting.

Posting a recurring transaction updates the same files as posting a normal AP-B voucher (AP transaction file, voucher records, vendor outstanding balances, General Ledger, Purchases Journal).

---

## AP-Q — Void AP Check

*Source: [ap-q_void_ap_check.htm](../../../samples/chm/extracted/ap-q_void_ap_check.htm)*

**Purpose.** Void an AP check that has already been printed and posted. Checks can be voided until they are purged or archived from the check history file. For a check that has been selected but not yet printed and posted, use AP-F to cancel it instead.

### General Program Operation

Enter the check number. Bank account and vendor auto-fill. If the check number is not unique, specify the vendor and bank account to identify the correct item.

The program prints an *AP Void Register* report showing all paid items on the check that will be reversed — similar to AP-G, providing a hard-copy audit record of the void.

After the report prints, click the *Void* button to proceed. The program reverses every operation performed in AP-H when the check was originally paid, returning all invoices to the open aging for the vendor.

**Check register markings after void:**
- Original check: marked as reconciled, designation changed from `C` to `V`.
- Reversing entry: flagged as cleared and marked `X` (rather than `D` for deposit).

Voided checks and their reversals can be viewed in GL-I Print Check Register by selecting *Cleared and Voided Checks* as the type.

---

## AP-R — Print AP Payment History

*Source: [ap-r_print_ap_payment_history.htm](../../../samples/chm/extracted/ap-r_print_ap_payment_history.htm)*

**Purpose.** Print a listing of paid AP checks in vendor code order. For each vendor the report shows bank account name, check number, check date, check amount, and the invoice numbers, dates, and amounts covered by that check.

### General Program Operation

Filter options: single bank account or all bank accounts; range of vendor codes; range of check dates; range of check numbers. Leave filters blank for an unfiltered report.

---

## AP-S — Print 1099 Forms

*Source: [ap-s_print_1099_forms.htm](../../../samples/chm/extracted/ap-s_print_1099_forms.htm)*

**Purpose.** Print IRS Form 1099-MISC for vendors who have the *Send 1099?* flag set to `Y` in AP-A. Also sends a copy to each vendor. Payment amounts are drawn from the check history file, so amounts are correct only if AP has been run on this system for the full calendar year.

### General Program Operation

**Pre-requisite:** Verify that each 1099 vendor has a *Tax ID No* in AP-A (required to appear on the form).

**Selection criteria:**

| Field | Notes |
|---|---|
| **From/Thru Vendor Code** | Look up via F2 or Lookup button; leave blank for all. |
| **From/Thru Vendor Class** | Optional class range filter. |
| **From/Thru Amount** | Dollar range filter; e.g., enter `600` in the From field to print only vendors with $600 or more in payments. |

Only vendors with *Send 1099?* = `Y` are selected, regardless of the other range filters.

**1099 type:** Eight types presented in a pop-up. The most common is *Non-Employee Compensation*. Other types require editing the standard 1099-MISC `.RTM` form template to align boxes with the preprinted form.

**Federal ID:** Enter your company's federal identification number; printed on every 1099.

**Require Tax ID:** Option to skip vendors without a Tax ID entered (answer `N` to print all 1099 vendors even without Tax IDs).

**Multiple copies:** Run the program again for each additional copy needed.

---

## AP-T — Check and Invoice Inquiry

*Source: [ap-t_check_invoice_inquiry.htm](../../../samples/chm/extracted/ap-t_check_invoice_inquiry.htm)*

**Purpose.** Multi-level inquiry that links a check paid to a vendor to the invoices paid by that check, and from an invoice to the Purchase Order line items on it. This program is an add-on from IS Tech Support, provided in Demo mode (limited to the first vendor in the payment history file). A 30-day full demo is available from www.istechsupport.com.

### General Program Operation

Enter the **Vendor Code**. Then:

- If you know the **check number**, enter it; click *View All Invoices* to see the invoices paid by that check; click *PO/WO* to see PO/work order detail.
- If you know the **invoice number**, enter it; the check that paid it displays. If the invoice was a voucher (not a PO invoice), that detail is also available.

Click *Print* to generate a report of the selected information.

---

## AP-V — Enter AP Deposit

*Source: [ap-v_enter_ap_deposit.htm](../../../samples/chm/extracted/ap-v_enter_ap_deposit.htm)*

**Purpose.** Record a deposit paid to a vendor (analogous to AR-N on the Accounts Receivable side), optionally linked to a specific Purchase Order. The deposit creates an open AP voucher that can be picked and paid like any other — but partial payments are not allowed. Each deposit payment must be entered separately.

### GL Posting When Creating a Deposit

- **Credit:** Accounts Payable
- **Debit:** AP Deposits account (defined in AD-A General Ledger Defaults; typically an Asset account such as "Prepaid Inventory")

Also creates a record in `BKAPDEP` linked to `BKAPINVT` by Deposit Number. A deposit can be edited to change or add a PO link, or deleted (which reverses the original transaction).

### When the Deposit Check Is Paid (AP-H)

The original AP invoice record is marked paid and a new record is created with `-D` appended to the invoice number, saved as a Credit. This credit sits outside the AP Control account. AP Aging has an option to include or exclude deposits — exclude deposits when reconciling the aging balance to the GL.

### Non-PO Deposit Workflow

If the deposit is not linked to a PO, when the vendor invoice arrives enter it for the full gross amount. When picking to pay in AP-F, take the invoice and the deposit credit; process a payment for the net. Check posting: credits cash for the net check amount, credits the deposit account for the deposit, and debits AP for the gross invoice amount.

### PO-Linked Deposit Workflow

Handled in AP-C: select the deposit, specify how much applies to this invoice (supports partial application across multiple receipts). Specify whether the invoice amount is gross or net. GL posting: total line amounts debit PO/RNI; deposit credits AP Deposits; net invoice credits AP; tax and freight as usual.

### Field Explanations

| Field | Notes |
|---|---|
| **Vendor** | Vendor code for the deposit. |
| **Deposit Date** | Transaction date. |
| **Link to PO#** | Purchase Order this deposit is for. Leave blank for a Deposit on Account. |
| **Deposit Amount** | Dollar amount of the deposit. |

### Setup Requirement

Before first use, define the default AP Deposit account in AD-A General Ledger Defaults. For multiple currencies, define deposit, control, and conversion accounts per currency in IM-B.

### General Program Operation

Click *Add New*, enter Vendor Code, date, PO (if applicable), and amount. Save; an open AP voucher is created and available for payment in AP-F/AP-H.

---

## AP-X — Print Invoice Detail

*Source: [ap-x_print_invoice_detail.htm](../../../samples/chm/extracted/ap-x_print_invoice_detail.htm)*

**Purpose.** Print supporting detail of AP invoices. Voucher invoices show GL account and department distribution; PO invoices show PO line item detail plus freight and tax.

### General Program Operation

Enter the range of **Vendor Code**, **Invoice Date**, and/or **Invoice Number** and process.

---

## Cross-references

AP is the central clearing house for all money owed to vendors. Key integration points:

| Related module / program | Relationship |
|---|---|
| **PO-A Enter Purchase Orders** | Vendor master (AP-A) defaults terms, currency, ship-via, and FOB into POs. |
| **PO-C Receive Purchase Orders** | Items must be received in PO-C before AP-C can invoice them. Returns processed as negative receipts in PO-C. |
| **PO-J-C Enter Inspection Buyoffs** | Items received to inspection must be bought off here before they appear in AP-C. |
| **AP-C** | Links PO receipts (RNI — Received Not Invoiced) to AP invoices; corrects inventory costs. |
| **AP-H** | Prints and posts checks; updates GL, Cash Disbursements Journal, check register, and AP payment history. |
| **AP-S** | Prints 1099-MISC forms; driven by *Send 1099?* flag and *Tax ID No* in AP-A. |
| **GL-O Print/Post General Ledger Batches** | AP vouchers and credit memos generate GL batch transactions posted here. |
| **GL-I Print Check Register** | Lists AP checks including voided checks (flagged `V`) and reversals (flagged `X`). |
| **AD-A General Ledger Defaults** | Defines the default AP Control account and AP Deposit account used in all AP postings. |
| **AD-B Checking Accounts Defaults** | Defines bank accounts used for check printing; stores next check number. |
| **AD-C Accounts Payable Defaults** | Controls aging period defaults, next AP invoice number, next recurring AP number, discount calculation behavior. |
| **SM-C Enter Item Classes** | Asset/Expense GL accounts in item classes drive GL posting for PO-based invoices in AP-C. |
| **SM-D Enter Terms Table** | All payment terms codes referenced by AP-A, AP-B, and AP-C must be defined here first. |
| **SM-P-F Enter Jobs** | Job numbers used in AP-B distribution lines must exist here when the Job field is set to Required. |
| **AM-O Archive/Purge Vendor Data** | Use instead of AP-A deletion for vendors with purchase or payment history. |
| **IM-A International Configuration** | Activates multi-currency, landed cost, and excise tax features referenced throughout AP. |
| **IM-B Enter Multiple Currencies** | Source currencies, AP control/conversion accounts, and deposit accounts per currency. |
| **IM-C Enter Currency Exchange Rates** | Exchange rates used for currency conversion in AP-B, AP-C, and AP-H. |
| **AR-L Transfer Sales Taxes** | Used to transfer and pay sales tax liabilities generated by AP-B Auto-Tax Distribution. |
| **TA-M Forms Editor** | Can modify `T6APJ1.RTM` (AP-J report) and 1099-MISC `.RTM` (AP-S) to customize output. |
