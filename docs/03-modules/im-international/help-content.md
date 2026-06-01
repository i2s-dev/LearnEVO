# IM — International Module

Status: verified (text distilled from the vendor's help file).

*Source: EvoHELP.CHM → System Manager → International Module (3 topics).*
*Extracted HTML in [samples/chm/extracted/](../../../samples/chm/extracted/).*

The International Module provides three cross-cutting international capabilities: multi-currency processing (up to ten source currencies), landed cost processing (freight, duty, customs, and brokerage fees folded into inventory cost), and a flexible sales and purchase tax system designed to handle multi-tier, hierarchical, and excise-tax regimes found outside the United States. All three features are switched on or off independently via IM-A International Configuration and then surface as additional fields and behaviors throughout AP, AR, IN, PO, SO, SA, and GL programs.

---

## Contents

- [International Module — Overview](#international-module--overview)
- [IM-A — International Configuration](#im-a--international-configuration)
- [International Features — Other Programs](#international-features--other-programs)
  - [AP-A — Enter Vendors](#ap-a--enter-vendors)
  - [AP-B — Enter Vouchers](#ap-b--enter-vouchers)
  - [AP-C — Enter Purchase Order Invoices](#ap-c--enter-purchase-order-invoices)
  - [AP-H — Print AP Checks](#ap-h--print-ap-checks)
  - [AP-I — Print Aging](#ap-i--print-aging)
  - [AR-A — Enter Customers](#ar-a--enter-customers)
  - [AR-B — Enter Vouchers](#ar-b--enter-vouchers)
  - [AR-C — Record Payments](#ar-c--record-payments)
  - [AR-F — Print Aging](#ar-f--print-aging)
  - [AR-L — Transfer Sales Taxes](#ar-l--transfer-sales-taxes)
  - [GL-K — Transfer Bank Account Funds](#gl-k--transfer-bank-account-funds)
  - [IN-A — Inventory Inquiry](#in-a--inventory-inquiry)
  - [IN-B — Enter Inventory](#in-b--enter-inventory)
  - [PO-A — Enter Purchase Orders](#po-a--enter-purchase-orders)
  - [PO-C — Receive Purchase Orders](#po-c--receive-purchase-orders)
  - [PO-I-A — Print Open Purchase Orders Listing](#po-i-a--print-open-purchase-orders-listing)
  - [PO-I-B — Print Closed Purchase Orders Listing](#po-i-b--print-closed-purchase-orders-listing)
  - [PO-I-E — Print Receiving Report](#po-i-e--print-receiving-report)
  - [PO-I-F — Print Received not Invoiced](#po-i-f--print-received-not-invoiced)
  - [SA-A — Print Daily Sales/Bookings](#sa-a--print-daily-salesbookings)
  - [SA-B — Print Profit by Invoice](#sa-b--print-profit-by-invoice)
  - [SA-M — Print User-Defined Detail](#sa-m--print-user-defined-detail)
  - [SA-N — Print User-Defined Summary](#sa-n--print-user-defined-summary)
  - [SO-A — Enter Sales Orders](#so-a--enter-sales-orders)
  - [SO-G — Post Invoices](#so-g--post-invoices)
  - [SO-O-A — Print Open Sales Order Listing](#so-o-a--print-open-sales-order-listing)
  - [SO-O-H — Print Invoice Listing](#so-o-h--print-invoice-listing)
  - [SO-O-I — Print Released Sales Orders](#so-o-i--print-released-sales-orders)
- [Cross-references](#cross-references)

---

## International Module — Overview

*Source: [international_module.htm](../../../samples/chm/extracted/international_module.htm)*

**Purpose.** The International Module bundles multi-currency processing, landed cost processing, and a flexible sales and purchase tax system into a single feature set. Each of the three capabilities is described below.

### Multi-Currency Processing

Multiple currency processing allows entering transactions in up to ten different *source currencies* while keeping all financial reporting in the company's own *base currency*.

Each currency is configured via **IM-B Enter Multiple Currencies**; exchange rates are maintained in a table via **IM-C Enter Currency Exchange Rates**. Each time exchange rates are updated, the previous rates are preserved so that backdated transactions can be matched to the closest historical exchange rate.

Inventory, expenses, revenues, purchases, and sales are posted in *base currency*. Monetary accounts — *Accounts Payable*, *Accounts Receivable*, *Sales Order Deposits*, *POs Received not Invoiced*, and foreign currency *Bank Accounts* — are maintained in *source currency*. Each currency has its own GL accounts for these monetary balances so they remain separate on the General Ledger.

To review financial statements, a *Convert to Base Currency* routine in **IM-B** translates the monetary accounts into *base currency* at current exchange rates. This can be run at any point during or at the end of a period.

### Landed Cost Processing

In many countries the landed cost of importing goods (freight, duty, customs fees, broker fees) represents a significant portion of item cost that must be reflected in inventory valuation.

- GL accounts for these cost types are configured via **IM-D Enter Landed Cost Defaults**.
- A table of duty codes and rates is maintained via **IM-E Enter Landed Cost Duty Codes**.
- A table of customs brokers and fees is maintained via **IM-F Enter Landed Cost Customs Fees**.
- Duty codes are assigned to inventory items in **IN-B Enter Inventory**.
- Customs brokers are assigned during **PO-C Receive Purchase Orders**.

When items are received through PO-C, the landed costs (freight, duty, customs fees, broker fees) are calculated and added to each item's inventory cost.

### Sales and Purchase Tax Processing

The United States typically uses a single sales tax rate on selected line items. Other countries apply multiple taxes (federal, provincial, local, value-added, excise) that may need to be itemized on the invoice, and some taxes are computed as a tax on other taxes (hierarchical).

- Individual tax codes (each type of tax) are set up via **SM-E Enter Tax Codes**.
- Codes are grouped and assigned to customers and vendors via **SM-F Enter Tax Groups**.
- Whether taxes are itemized on the invoice is controlled by the **Multi-Tax Forms** flag in **IM-A International Configuration**.
- Freight taxability and tax-on-tax rules are specified within each tax code.
- All collected taxes can be listed via **AR-K Print Sales Tax Report** and transferred for payment via **AR-L Transfer Sales Taxes**.

For purchase taxes (applicable in countries where the buyer must account for and report the tax rather than rely on the vendor), the same SM-E and SM-F structures apply.

For excise taxes where the tax is embedded in the selling or purchase price, **IM-G Enter Tax-In Codes** defines the codes. When invoices are posted, sales amounts posted to the General Ledger and sales reports are reduced by the embedded tax amount so that revenue is not overstated.

---

## IM-A — International Configuration

*Source: [im-a_international_configuration.htm](../../../samples/chm/extracted/im-a_international_configuration.htm)*

**Purpose.** Use this program to activate or de-activate the various International Module functions. Each flag is a `Y`/`N` field that unlocks corresponding capabilities and additional data-entry fields throughout the system.

### Field Explanations

**Multi-Tax Forms**
If multiple tax codes apply to a sales order or purchase order and you want each tax code separately itemized and printed in the bottom portion of the invoice, enter `Y`. Enter `N` to print only a single total for all taxes. This setting must also be set to `Y` if you want purchase orders and invoices to print with different currency symbols when multi-currency is active.

**Excise Tax**
Enter `Y` if you will use excise tax processing in which a tax is embedded in the item's selling or purchase price. Activating this setting causes the system to back the tax out of prices for General Ledger, sales analysis, and tax reporting purposes.

**Multi-Currency**
Enter `Y` to switch on multi-currency processing. Be aware that once enabled, certain programs cannot be run until the multi-currency setup is complete. Refer to the *Multiple Currency Startup* guide for setup sequence details.

**Pay**
Controls when currency gains or losses are recognized on payments made to vendors or received from customers.
- `Y` — recognize the currency gain or loss at the time of the payment transaction.
- `N` — defer recognition to month end (required in some countries such as Canada).

When **Pay** is `N`, checks and payment receipts post only in source currency with no conversion at transaction time; the gain/loss is computed and posted when the *Convert to Base Currency* routine is run. When **Pay** is `Y`, an additional GL conversion transaction is generated at payment time (see AP-H and AR-C details below).

**Landed Costs**
Enter `Y` if you will use landed cost processing.

**Auto-Tax Calc**
Enter `Y` to enable automatic sales tax calculation and posting within **AP-B Enter Vouchers** and **AR-B Enter Vouchers**. When active, sales tax is posted to the General Ledger and to the sales tax file from which it can be transferred for payment to the appropriate tax authorities. Also requires **Track PO taxes using tax groups?** to be set to `Y` in **SD-C Purchase Orders Defaults** for AP voucher tax to function.

---

## International Features — Other Programs

*Source: [international_features-other_programs.htm](../../../samples/chm/extracted/international_features-other_programs.htm)*

**Purpose.** This topic documents the additional fields and behaviors that appear throughout EvoERP programs when International Module features are active. Fields and behaviors only appear when the corresponding IM-A flag is enabled.

---

### AP-A — Enter Vendors

The following fields become available when International features are active.

**Currency** *(visible when Multi-Currency is active)*
Enter the currency code representing the currency this vendor uses for transactions. The currency must already be set up in IM-B. This is a default that can be overridden when entering a purchase order, so you can transact in multiple currencies with the same vendor if needed.

**Duty Code** *(visible when Landed Costs is active)*
Enter a 3-character duty code (previously set up in IM-E) if duties apply to purchases from this vendor. This code represents the Country of Import when determining the duty rate. It is combined with the item-level duty code from IN-B to form the full 6-character duty rate lookup key.

**Tax-In Code** *(visible when Excise Tax is active)*
Enter a Tax-In code as set up in IM-G if excise tax processing applies to this vendor's transactions.

---

### AP-B — Enter Vouchers

#### Multi-Currency Processing

When multi-currency processing is enabled in IM-A, vouchers can be entered in a foreign currency. Make all entries in *source currency*. During processing:
- The debit side of the transaction is converted to *base currency* at the current rate from IM-C.
- The credit side posts in *source currency* to this currency's *AP Control* account.

#### Auto-Tax Distribution

When **Auto-Tax Calc** is `Y` in IM-A and **Track PO taxes using tax groups?** is `Y` in SD-C, sales taxes can be applied to AP vouchers. When entering a voucher, you are asked whether to use the *Auto-Tax Distribution* feature. If yes:

1. The program calculates the tax amount and makes an entry to the default *Sales Tax Payable* account (converted to *base currency*) in the Distribution area.
2. You are then asked whether the sales tax is already included in the voucher amount:
   - **No** — the program credits AP for the full voucher amount and makes an additional credit for the tax amount to *Sales Tax Payable*.
   - **Yes** — the program reduces the AP credit by the tax amount so that the AP credit plus the *Sales Tax Payable* credit together equal the voucher amount.

Even though the sales tax liability is posted in base currency, the amount owed to the tax authority is stored in source currency in the sales tax transfer file. When taxes are transferred for payment via AR-L, you can choose to pay in source currency or base currency.

---

### AP-C — Enter Purchase Order Invoices

#### Multi-Currency Processing

Purchase orders processed here can be coded for a foreign *source currency* (the currency was assigned to the PO during PO entry). The vendor will be paid in that source currency.

General Ledger posting:
- The source currency's *POs Received not Invoiced* account is debited in *source currency* for the purchase order amount being paid.
- Any freight is converted to *base currency* at the current rate from IM-C and debited to *Freight-in* expense.
- Any sales tax is converted to *base currency* at the current exchange rate and posted to the default *Sales Tax Payable* account.
- If a currency conversion was made for freight or sales tax, a balancing entry is made to this currency's *F/E Gain/Loss-Trxns* account.

---

### AP-H — Print AP Checks

#### Multi-Currency Processing

When multi-currency processing is enabled, checks can be printed to vendors in foreign currencies. GL posting depends on the **Pay** setting in IM-A.

**Pay = N:**
- Debit (in *source currency*) to the *AP Control Account*.
- Offsetting credit (in *source currency*) to this currency's *Bank Account*.
- No gain/loss recognition at transaction time; deferred to the Convert to Base Currency routine.

**Pay = Y:**
Two GL transactions are generated:
1. Same as Pay = N (source currency debit to AP Control, credit to Bank Account).
2. A currency conversion transaction: the payment amount is converted to *base currency* using the IM-C exchange rate. This base currency amount is debited to this currency's *F/E Gain/Loss-Trxns* account and the offsetting amount is credited to this currency's *F/E Gain/Loss-Conversions* account. The gain or loss is thus recognized at the time of the transaction rather than when Convert to Base Currency is run.

---

### AP-I — Print Aging

#### Multi-Currency Reporting

When multi-currency processing is active, Accounts Payable for each currency is maintained in *source currency*.

The report can be printed in either *source currency* or *base currency*:
- Running in *source currency* with more than one currency included produces grand totals with no meaningful meaning (different currencies are added together).
- To run in *base currency* for GL reconciliation: each currency has an *AP Control* account and an *AP Conversion* account; together they equal that currency's total AP in base currency. Run the *Convert to Base Currency* routine in IM-B beforehand so that source currency AP accounts are translated at current rates.

**Currency** field: Enter a from/thru range of currency codes to confine the report to AP within a specific currency or range.

**Print in Base or Source Currency?**
- `S` — AP transacted in foreign currency prints in that source currency. Mixed-currency grand totals are meaningless.
- `B` — All AP is converted to base currency using the exchange rates in effect at the time of the first receipt made to the purchase order.

---

### AR-A — Enter Customers

**Currency** *(visible when Multi-Currency is active)*
Enter the currency code for the currency this customer uses for transactions. The currency must already be set up in IM-B. This is a default that can be overridden when entering a sales order, so you can transact in multiple currencies with the same customer if needed.

**Tax-In Code** *(visible when Excise Tax is active)*
If sales to this customer are subject to excise taxes embedded in the item price, enter `Y`. When excise tax processing is activated in IM-A, this causes the embedded taxes to be backed out of the price for General Ledger and sales analysis purposes.

---

### AR-B — Enter Vouchers

#### Multi-Currency Processing

When multi-currency processing is enabled, AR vouchers can be entered in a foreign currency. Make all entries in *source currency*. During processing:
- The credit side of the transaction is converted to *base currency* at the current rate from IM-C.
- The debit side posts in *source currency* to this currency's *AR Control* account.

---

### AR-C — Record Payments

#### Multi-Currency Processing

Customer invoices and payments can be processed in foreign currencies. GL posting depends on the **Pay** setting in IM-A.

**Pay = N:**
- Credit (in *source currency*) to the *AR Control Account*.
- Offsetting debit (in *source currency*) to this currency's *Bank Account*.
- No gain/loss recognition at transaction time.

**Pay = Y:**
Two GL transactions are generated:
1. Same as Pay = N (source currency credit to AR Control, debit to Bank Account).
2. A currency conversion transaction: the payment amount is converted to *base currency* using the IM-C exchange rate. This base currency amount is credited to this currency's *F/E Gain/Loss-Trxns* account and the offsetting amount is debited to this currency's *F/E Gain/Loss-Conversions* account. The gain or loss is recognized at the time of transaction.

---

### AR-F — Print Aging

#### Multi-Currency Reporting

When multi-currency processing is active, Accounts Receivable for each currency is maintained in *source currency*.

The report can be printed in either *source currency* or *base currency*:
- Running in *source currency* with more than one currency included produces meaningless grand totals.
- For GL reconciliation in *base currency*: each currency has an *AR Control* account and an *AR Conversion* account; together they equal that currency's total AR in base currency. Run Convert to Base Currency in IM-B beforehand so source currency AR accounts are translated at current rates.

**Currency** field: Enter a from/thru range of currency codes to confine the report to AR within a specific currency or range.

**Print in Base or Source Currency?**
- `S` — AR transacted in foreign source currency prints in that currency. Mixed-currency grand totals are meaningless.
- `B` — All AR is converted to base currency. (No exchange rate note is given for this report — base currency conversion uses rates at the time of the original transaction, consistent with other aging reports.)

---

### AR-L — Transfer Sales Taxes

#### Multi-Currency Processing

When multi-currency processing is active, tax authority vendors can be paid in a currency other than base. Although the sales tax payable amount was originally converted and posted in base currency at the time of the original transaction, the amount owed is stored in source currency in the sales tax transfer file for use by this program.

The program transfers the amount in the currency assigned to the tax authority vendor in AP-A Enter Vendors:

**Tax authority vendor set up in source currency:**
- A credit is made to this currency's *AP Control* account.
- The source currency amount is converted to base currency.
- A debit for this base currency amount is made to the default *Sales Tax Payable* account.
- The difference between the two amounts is posted to *F/E Gain/Loss-Trxns*.

**Tax authority vendor set up in base currency:**
- The source currency amount is converted to base currency.
- A credit for this base currency amount is made to the base currency's *AP Control* account.
- A debit is made to the default *Sales Tax Payable* account.

---

### GL-K — Transfer Bank Account Funds

#### Multi-Currency Processing

When multi-currency processing is active, bank accounts can be maintained in foreign currencies. Transferring money from base currency to source currency, source to base, or between two source currencies triggers automatic conversions using current exchange rates from IM-C.

GL posting remains in *source currency*. Any difference between source and base currency amounts, or between two source currency amounts, is posted as an offsetting entry to *F/E Gain/Loss-Trxns*.

---

### IN-A — Inventory Inquiry

#### Multi-Currency and Landed Cost Processing

When multi-currency processing is active, the *Last* and *Average* costs of purchased items shown in IN-A will reflect foreign currency fluctuations that can vary from transaction to transaction.

When landed cost processing is active, the *Last* and *Average* costs will be increased by landed costs such as duty charges, brokerage fees, and freight.

---

### IN-B — Enter Inventory

The following fields become available based on settings in IM-A.

**Tax-In** *(visible when Excise Tax is active)*
If the item is subject to an excise tax embedded in its selling or purchase price, set this field to `Y`. Upon invoice posting or purchase order receiving, this causes the tax to be backed out of the price for General Ledger, sales analysis, and tax reporting purposes. See IM-G Enter Tax-In Codes for details.

**Duty Code** *(visible when Landed Costs is active)*
This is the 3-character code that forms the second half of the 6-character code used in IM-E to establish a duty rate. In essence it represents the Item Classification Rate specific to this item when imported from a particular country. The vendor's 3-character duty code (Country of Import) from AP-A forms the first half; together they identify the applicable duty rate.

---

### PO-A — Enter Purchase Orders

**Currency** *(visible when Multi-Currency is active)*
Defaults to the currency code assigned to this vendor in AP-A Enter Vendors. The field can be overridden to use a currency different from the vendor default.

---

### PO-C — Receive Purchase Orders

#### Multi-Currency Processing

When multi-currency processing is active, purchase orders can be placed with vendors in foreign currencies.

If a foreign currency is specified in the purchase order header, when receiving the PO the program converts each line item's cost from *source currency* to *base currency* (using the closest historical exchange rate) when posting to the *Inventory* or *WIP* GL accounts and when calculating the *Last* and *Average* cost. The *POs Received not Invoiced* GL account is posted in *source currency*. The difference between base currency and source currency postings is posted to the *F/E Transactions* account set up in IM-C.

#### Landed Cost Processing

When receiving a PO, a customs broker can be entered in the **Customs Broker** field. The program adds the brokerage fees (from IM-F) to the inventory cost of each item.

The program also combines the vendor's duty code (from AP-A) with each item's duty code (from IN-B) to calculate a duty fee that is added to the inventory cost of each item.

All landed cost entries to inventory are made in *base currency*.

---

### PO-I-A — Print Open Purchase Orders Listing

**Print in Base/Source Currency?** *(visible when Multi-Currency is active)*
- `B` — converts all source currency orders to base currency using the exchange rates in effect at the time of first PO receipt, or at today's rate if no receipts have yet occurred.
- `S` — prints in source currency as entered.

---

### PO-I-B — Print Closed Purchase Orders Listing

**Print in Base/Source currency?** *(visible when Multi-Currency is active)*
- `B` — converts all source currency orders to base currency using the exchange rates in effect at the time of first PO receipt.
- `S` — prints in source currency as entered.

---

### PO-I-E — Print Receiving Report

**Print in Base/Source currency?** *(visible when Multi-Currency is active)*
- `B` — converts all source currency orders to base currency using the exchange rates in effect at the time of first PO receipt.
- `S` — prints in source currency as entered.

---

### PO-I-F — Print Received not Invoiced

#### Multi-Currency Reporting

When multi-currency processing is active, the *POs Received not Invoiced* balance for each currency is maintained in *source currency*.

The report can be printed in either *source currency* or *base currency*:
- Running in source currency with more than one currency produces meaningless grand totals.
- For GL reconciliation in base currency: each currency has a *PORNI Control* account and a *PORNI Conversion* account. Run Convert to Base Currency in IM-B beforehand so that source currency PORNI accounts are updated for current exchange rates.

---

### SA-A — Print Daily Sales/Bookings

**Currency [Base/Src]** *(visible when Multi-Currency is active)*
- `B` — converts all source currency orders to base currency using current exchange rates for newly booked orders and the closest historical exchange rate to the invoice date for the sales portion of the report.
- `S` — prints in source currency as entered.

---

### SA-B — Print Profit by Invoice

**Currency [Base/Src]** *(visible when Multi-Currency is active)*
- `B` — converts all orders to base currency using the closest historical exchange rate to each invoice date.
- `S` — prints in source currency as entered.

---

### SA-M — Print User-Defined Detail

**Currency [Base/Src]** *(visible when Multi-Currency is active)*
- `B` — converts all orders to base currency using the closest historical exchange rate to each invoice date.
- `S` — prints in source currency as entered.

---

### SA-N — Print User-Defined Summary

**Currency [Base/Src]** *(visible when Multi-Currency is active)*
- `B` — converts all orders to base currency using the closest historical exchange rate to each invoice date.
- `S` — prints in source currency as entered.

---

### SO-A — Enter Sales Orders

**Currency** *(visible when Multi-Currency is active)*
Defaults to the currency code assigned to this customer in AR-A Enter Customers. The field can be overridden to use a currency different from the customer default.

---

### SO-G — Post Invoices

#### Multi-Currency Processing

When multi-currency processing is active, customer sales orders can be printed and posted in foreign currencies.

If a foreign currency code was entered in the Currency field of the sales order header, the program converts each line item's sales revenue and cost from *source currency* to *base currency* (using the closest historical exchange rates to the invoice date) when posting to the *Inventory*, *Sales*, *Cost of Goods Sold*, and *Sales Tax Payable* GL accounts. This currency's *AR Control* account is posted in *source currency*. The difference between base currency and source currency postings is posted to the *F/E Transactions* account set up in IM-B.

---

### SO-O-A — Print Open Sales Order Listing

**Currency [Base/Src]** *(visible when Multi-Currency is active)*
- `B` — converts all source currency orders to base currency using the invoice date rate if invoices have been posted, or current exchange rates if no invoices have yet been posted.
- `S` — prints in source currency as entered.

---

### SO-O-H — Print Invoice Listing

**Currency [Base/Src]** *(visible when Multi-Currency is active)*
- `B` — converts all source currency orders to base currency using the exchange rates that were in effect on the date the invoices were posted.
- `S` — prints in source currency as entered.

---

### SO-O-I — Print Released Sales Orders

**Currency [Base/Src]** *(visible when Multi-Currency is active)*
- `B` — converts all source currency orders to base currency using the date of the first invoice, or current exchange rates if no invoices have yet been posted against the sales order.
- `S` — prints in source currency as entered.

---

## Cross-references

- **SD-V International Defaults** — system-level defaults that feed into IM (IM-A links back to this; it is the previous topic in CHM navigation).
- **SM-E Enter Tax Codes** — defines individual tax codes used by the IM tax system.
- **SM-F Enter Tax Groups** — groups tax codes and assigns them to customers and vendors.
- **IM-B Enter Multiple Currencies** — currency setup and the *Convert to Base Currency* routine; must be completed before other programs can run in multi-currency mode.
- **IM-C Enter Currency Exchange Rates** — exchange rate table with historical rate preservation.
- **IM-D Enter Landed Cost Defaults** — GL accounts for landed cost categories.
- **IM-E Enter Landed Cost Duty Codes** — duty rate table keyed by 6-character composite code.
- **IM-F Enter Landed Cost Customs Fees** — customs broker fee table.
- **IM-G Enter Tax-In Codes** — excise tax code definitions.
- **GL** — each source currency requires its own AP Control, AR Control, Bank Account, F/E Gain/Loss-Trxns, F/E Gain/Loss-Conversions, PORNI Control, and Conversion accounts.
- **AR-K Print Sales Tax Report** — lists all collected taxes across SM-E/SM-F and IM-G.
- **AR-L Transfer Sales Taxes** — transfers tax amounts to AP as a payable to the tax authority.
- **AP-A Enter Vendors** — vendor-level currency and duty code assignments.
- **AR-A Enter Customers** — customer-level currency assignment.
- **IN-B Enter Inventory** — item-level Tax-In and Duty Code assignments.
- **PO-C Receive Purchase Orders** — landed cost calculation trigger point.
- **SD-C Purchase Orders Defaults** — must have *Track PO taxes using tax groups?* = `Y` for AP-B Auto-Tax Calc to function.
