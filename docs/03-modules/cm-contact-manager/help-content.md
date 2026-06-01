# CM — Contact Manager

Status: verified (text distilled from the vendor's help file).

*Source: EvoHELP.CHM → Sales → Contact Manager (8 topics).*
*Extracted HTML in [samples/chm/extracted/](../../../samples/chm/extracted/).*

The Contact Manager (CM) module is EvoERP's lightweight CRM layer. It maintains a master file of sales prospects and customers (called "accounts"), tracks contact history notes and follow-up reminders, manages sales opportunity pipelines via a dashboard, generates mailing lists and labels, and produces form letters for broadcast correspondence and AR collections. CM accounts and AR customer records share the same account-code namespace and can be toggled between freely; a contact record can be promoted to a full customer record with a single button click.

---

## Contents

- [CM-A — Enter Contact Accounts](#cm-a--enter-contact-accounts)
- [CM-B-B — Print Accounts Listing / Labels](#cm-b-b--print-accounts-listing--labels)
- [CM-B-C — Print Reminders](#cm-b-c--print-reminders)
- [CM-B-F — Print Account History](#cm-b-f--print-account-history)
- [CM-C — Opportunity Dashboard](#cm-c--opportunity-dashboard)
- [CM-J — Change Account Codes](#cm-j--change-account-codes)
- [CM-K — Add Customers to Account File](#cm-k--add-customers-to-account-file)
- [CM-L — Enter Form Letters](#cm-l--enter-form-letters)
- [Cross-references](#cross-references)

---

## CM-A — Enter Contact Accounts

*Source: [cm-a_enter_contact_accounts.htm](../../../samples/chm/extracted/cm-a_enter_contact_accounts.htm)*

**Purpose.** Maintain general master file information on sales prospects and customers. From this program you can enter contact history notes, reminders, assign classification codes, enter multiple contacts, and track key dates.

### Field Explanations

| Field | Size / Type | Notes |
|---|---|---|
| **Acct Code** | user-defined | Identifies the sales prospect or customer. Single quotes, double quotes, and commas are not allowed; other characters such as `#` or `-` are allowed. Customers and Contacts are stored in separate files but must use the same coding method so that an entity appearing in both files carries the same code. |
| **Company** | 30 char alpha | Actual company or account name. |
| **Alpha Sort** | 6 char (default) | Used by reports that sort alphabetically. Defaults to the first six letters of **Company**; may be overridden. |
| **Address 1 – 3** | 30 char alpha each | Three address lines. |
| **City** | 26 char alpha | Account city. |
| **State** | 2 char | Two-character state code. |
| **Zip** | 10 char alpha | Zip or postal code. |
| **Country** | 30 char alpha | Country name or code; used when serving multiple countries. |
| **Contact** | — | Primary (first) contact for the account. Unlimited additional contacts are accessible via the **Contacts** button. |
| **Title** | — | Title of Contact 1. |
| **Telephone** | 25 char alpha | Contact 1's primary telephone. Each contact can carry up to 10 telephone numbers (office, mobile, home, etc.) in the multiple-contacts window. |
| **Fax** | 25 char alpha | Account fax number. |
| **Currency** | — | Currency assigned to this contact. Only visible when multiple-currency is enabled in IM-A International Configuration. |
| **SIC Code** | 7 char alpha | Standard Industrial Code; used for reporting. |
| **Start Dt** | date | Date the account record was created. Defaults to today; may be overridden. |
| **Ship Via** | — | Default shipping method for this account. |
| **Lead Source** | 5 char alpha | User-defined lead source code (set up in SM-I-A Enter Lead Source Codes) identifying where the prospect originated (advertising, referral, etc.). Used for reporting. |
| **RTM Print Group** | — | Optional field to select different print formats (RTM templates) for quotes, invoices, and other forms on a per-customer basis. |
| **Price Code** | — | Default price code applied when generating Quotes and Sales Orders for this account. |
| **Discount Code** | — | Default discount code applied when generating Quotes and Sales Orders. |
| **Default Terms** | — | Default payment terms applied when generating Quotes and Sales Orders. |
| **Taxable & Tax Group** | — | Sales tax status and tax group applied when generating Quotes and Sales Orders. |
| **Territory** | 4 char alpha | User-defined territory code (set up in SM-I-B Enter Territory Codes) for reporting. |
| **Class Codes** | display window | Shows user-defined classification codes assigned to this account. Used primarily for mailing-list sorting and reporting. Codes are set up in SM-I-G Enter Class Codes. Assigned via the **Class** button. |
| **Key Dates** | display window | Shows key date codes, dates, and descriptions for this account. Used to record significant events (first sales meeting, first order, etc.). Codes are set up in SM-I-H Enter Key Date Codes. Assigned via the **Date** button. |
| **Web Site** | — | Company website URL. Clicking the Internet Explorer icon in the toolbar opens the URL in a browser. |

### Toolbar / Action Buttons

| Button | Action |
|---|---|
| **Find Previous** | Moves to the previous contact record in the file. |
| **Lookup** | Opens the lookup grid (also triggered by F2). |
| **Find Next** | Moves to the next record in the file. |
| **Add** | Clears the screen to enter a new contact record. |
| **Delete** | Deletes the current record (only permitted if there is no pending sales activity). |
| **Clear** | Clears the screen without deleting the record. |
| **Credit Card** | If X-Charge credit-card processing is active, opens the credit card entry/view screen. Without X-Charge, only the last 4 digits and expiration date may be stored (full card data is prohibited by security regulations). |
| **Notes** | Opens the Notes screen to view or add free-text history notes for this contact. |
| **Links** | Opens the Links window to view or add file/URL links associated with the contact. |
| **Google Maps** | Opens Google Maps in a browser, pre-populated with the contact's address, for directions. |
| **Pricing** | Displays the effective pricing for a specified part number and quantity based on the account's price and discount codes. |
| **Contacts** | Displays the list of individual contact names for this account. Selecting a contact opens a detail screen with 10 phone-number slots, 10 email-address slots, 10 miscellaneous entry slots, and 10 date slots per contact. |
| **Reminders** | Opens a Reminders calendar window to add, edit, or dismiss follow-up reminders. |
| **Class** | Opens the Class window to view, add, or delete class codes for this account. |
| **Key Dates** | Opens the Key Dates window to add, edit, or delete key date entries. |
| **Sales Orders** | Opens a window listing open Sales Orders for this account. |
| **Shipments** | Opens a window listing shipments for this account. |
| **Quotes** | Opens a window displaying quotes for this account. |
| **Cust** | Switches to AR-A Enter Customers (or AR-Q View Customer Information, depending on user menu access). If a matching customer record exists it is displayed immediately. |
| **Make Customer** | Creates a new AR customer record populated with information from this contact record. Can be disabled via the *Allow Make Customer in CM* setting in SD-O Contact Manager Defaults. |

### General Program Operation

**Entering Account Information.** Bring up a record by typing the **Acct Code** or pressing F2 (Lookup button). Once the account is displayed, pressing Enter shows any assigned Class Codes and Key Dates in their respective windows. For new entries, complete all relevant fields and save with F10 (or the Save button). For existing records, make changes as required and save.

**Entering Notes.** Click the **Notes** button while an account is on screen. A list of prior notes is shown; click **Add** to create a new entry. Notes record phone conversations, meetings, and other history.

**Entering Reminders.** Click the **Reminders** button to open the calendar window. Reminders program a follow-up date and time to alert the user to perform a future activity such as a return phone call.

**Entering Class Codes.** Click the **Class** button while an account is on screen. Enter a class code or press F2 to select from the pop-up. After pressing Enter through the description you are prompted to save. Assign as many class codes as desired; press Esc to return to the main screen.

**Entering Additional Contacts.** Click the **Contacts** button to open the additional-contacts entry window listing available people. Click Select to open the detail screen with 10 phone-number, 10 email, 10 miscellaneous, and 10 date slots per contact.

**Entering Key Dates.** Click the **Date** button. Enter a date code (or F2 to look up); the description displays automatically. Enter the date and confirm save. Press Esc when finished.

**Switching to AR-A or AR-Q.** Click the **Cust** button to toggle to AR-A Enter Customers or AR-Q View Customer Information. If the account has a customer record, it loads automatically. From AR-A you can return to CM-A by closing the Customer screen.

**Make Customer.** If the contact is not yet an AR customer, clicking **Make Customer** creates an AR record carrying the same code and all common information. This action can be disabled in SD-O Contact Manager Defaults.

---

## CM-B-B — Print Accounts Listing / Labels

*Source: [cm-b-b_print_accounts_listing_labels.htm](../../../samples/chm/extracted/cm-b-b_print_accounts_listing_labels.htm)*

**Purpose.** Produce a listing of accounts with selected master-file fields (account code, company name, state, zip, Contact 1, telephone, Rep, SIC code, customer switch, lead source, territory). Optionally print remarks. Also generate FAX or email lists in text format for broadcasting, or print mailing labels for a selected list of accounts.

### General Program Operation

1. Enter a **Selection ID** (user-defined code) and description. Selection criteria are saved in a history database keyed to this ID. Reusing the same code reloads all prior selections automatically, making repeat mailings effortless.

2. Enter a **Date** as a reference.

3. Select a **report type** based on desired output contents. Choose the primary **sort field** (account code or alpha sort, etc.) and whether to generate a report or labels.

4. Enter **from/thru ranges** for:
   - Account codes
   - States
   - Zip codes
   - SIC codes
   - Lead sources
   - Start dates
   - Territory codes
   - Additional selection filters as presented

5. Enter a **first group of up to 18 class codes** for inclusion. Any account carrying any of those codes is included. Leaving all blank selects all class codes.

6. Enter a **second group of up to 18 class codes** to narrow the first group. Only accounts from the first group that also carry *all* class codes in the second group are selected.

7. Control **customer inclusion**:
   - Limit to customers only
   - Exclude customers
   - Include customers the same as any other account (set both customer fields to `Y`)

---

## CM-B-C — Print Reminders

*Source: [cm-b-c_print_reminders.htm](../../../samples/chm/extracted/cm-b-c_print_reminders.htm)*

**Purpose.** Produce a listing of reminder (follow-up) codes and dates. The report can be limited to a range of follow-up codes and dates.

### General Program Operation

Enter a **from/thru range** of:
- Follow-up type codes
- Follow-up dates
- Rep codes

If no limits are entered, all follow-up codes and dates print.

---

## CM-B-F — Print Account History

*Source: [cm-b-f_print_account_history.htm](../../../samples/chm/extracted/cm-b-f_print_account_history.htm)*

**Purpose.** Produce a listing of history (contact) notes within a range of selection criteria.

### General Program Operation

Enter a **from/thru range** of:
- Dates
- Account codes
- Rep codes
- History codes

History notes are **grouped by account** and **sorted by date within account**.

---

## CM-C — Opportunity Dashboard

*Source: [cm-c_opportunity_dashboard.htm](../../../samples/chm/extracted/cm-c_opportunity_dashboard.htm)*

**Purpose.** Review Sales Quote (opportunity) activity at a high level and drill down into detail.

### General Program Operation

The dashboard consists of a screen with **6 configurable panels**. When first loaded each panel shows a menu of available data panels so the user can choose which data to display where. Some panels present summary data immediately; others prompt for a date range before processing. Double-clicking a line in any panel drills into the detail. To change which data panel is loaded on a given screen position, click **Tools** and select the replacement panel.

### Available Data Panels

| Panel | Prompts | Description |
|---|---|---|
| **Won/Lost** | 3 date ranges (default: current month-to-date, past 120 days, past year) + Process button | Shows count and dollar value of Quotes won, lost, or abandoned within each date range. User may edit the date ranges before processing. |
| **Followups** | None (loads immediately) | Summary of open reminders by Type and Person. |
| **Pending Quotes** | None (loads immediately) | Count and dollar value of Quotes by Status where status is `N` (not yet submitted) or `1`–`9` (submitted; digit represents likelihood of winning: `1` = 10%, `9` = 90%). |
| **Pending Quotes by Rep** | None (loads immediately) | Same as Pending Quotes but broken out by Sales Rep. |
| **Aging Quotes** | None (loads immediately) | Count and dollar value of Quotes by Month where status is `N` or `1`–`9`. |
| **Lead Type** | Date range | Count and dollar value of Quotes entered within the date range, broken out by Lead Source. |
| **Loss Reasons** | Date range | Count and dollar value of Quotes lost within the date range, broken out by reason. |

**Quote status codes:**
- `N` — not yet submitted to the customer
- `1` through `9` — submitted; likelihood of winning is `(digit × 10)%`

---

## CM-J — Change Account Codes

*Source: [cm-j_change_account_code.htm](../../../samples/chm/extracted/cm-j_change_account_code.htm)*

**Purpose.** Rename an Account Code to a new code. All related files (history notes, follow-ups, key dates, etc.) are automatically updated to the new code.

### General Program Operation

1. Enter your **password** to authenticate the operation.
2. Enter the **current account code**.
3. Enter the **new account code**.
4. Confirm the change when prompted.
5. The program processes all related files and then clears the screen for the next entry.

> **Note.** Because CM and AR share the same account-code namespace, if this account also has an AR customer record you should use the equivalent AR code-change program (or contact AR administration) to keep the two files in sync.

---

## CM-K — Add Customers to Account File

*Source: [cm-k_add_customers_to_account_file.htm](../../../samples/chm/extracted/cm-k_add_customers_to_account_file.htm)*

**Purpose.** Create Contact Manager account records for AR customers that do not yet have a corresponding account record. This bridges the AR and CM files so every customer is visible in the Contact Manager.

**Typical use cases:**
- Run once when first activating the Contact Manager to bulk-create account records for all existing customers.
- Run periodically if your company tends to originate new entries in the AR customer file first, to keep the account file current.

### General Program Operation

The program iterates over each Customer Code in the AR file and searches for an identical code in the account master file.

- **No matching account found:** A new account record is created using the Customer Code as the Account Code, populated with information from the customer record.
- **Matching account found + Replace option selected:** The existing account file record is overwritten with information from the customer file.

**Selection parameters:**
- **From/thru range of customer codes** — limits account creation to a specific range.
- **Include Ship-To customers** — flag to indicate whether Ship-To customer records should be included in the process.

---

## CM-L — Enter Form Letters

*Source: [cm-l_enter_form_letters.htm](../../../samples/chm/extracted/cm-l_enter_form_letters.htm)*

**Purpose.** Create and maintain form letters used by AR-P Generate Dun Letters, as well as general correspondence such as memos, faxes, and broadcast letters. Form letters can automatically merge selected fields from the account master file, customer master file, and AR transactions file at designated points in the text.

### Field Explanations

| Field | Size / Type | Notes |
|---|---|---|
| **Code** | 15 char alpha | User-defined identifier for the form letter. |
| **Desc** | 30 char alpha | Description of the form letter. |
| **#Chr Lft Mrg** | numeric | Number of characters for the left margin. Form letters print at 10 characters/inch, so entering `10` produces a 1-inch left margin. Each new line entered in the editor is automatically indented by this amount. There is no separate right-margin field; simply stop typing at the desired right boundary. |
| **Lns/Pg** | numeric | Lines per page. Default is `66` (standard 11-inch letter at 6 lines/inch). Reduce for smaller forms such as memos. |
| **Start Ln Pg2** | numeric | Line number at which printing begins on page 2 and all subsequent pages when the letter spans multiple pages. |
| **Dun Ltr?** | `Y` / blank | Set to `Y` if this letter is to be used by AR-P Generate Dun Letters. When printed as a dun letter, the *Last Dun?* field and date in the customer's AR master record are updated automatically. |
| **Cur Line** | display only | Current line number being edited. Reference only. |
| **Total** | display only | Total number of lines currently in the form letter. Reference only. |

### General Program Operation

1. Assign a **Code** and **Desc**.
2. Set the **left margin** character count and accept or change **lines per page**.
3. If the letter spans multiple pages, set the **starting line for page 2**.
4. If this is a dun letter, enter `Y` in **Dun Ltr?**.
5. Type the letter body in the entry area. The cursor auto-indents to the left-margin position at each new line.
6. Save with F10 (or the Save button).

### Using Inserts (Mail-Merge Fields)

Position the cursor where a field value should print. Press F2 (or click **Display Inserts**) to open the insert pop-up. Highlight the desired insert and press Enter. The insert appears in the document surrounded by double `@@` markers (e.g., `@@Date@@`). The field value prints starting at the position of the first `@`.

#### Available Inserts

| Insert | Source | Notes |
|---|---|---|
| **Date** | System clock | Inserts the computer's system date when the letter prints. Alternative: type the date as literal text and update it manually each time. |
| **Contact Name** | Account file | The addressee name. A secondary pop-up asks which of the (up to 9) contacts to use. |
| **Title** | Account file | Title of the addressee. Secondary pop-up selects which of the 9 contact titles to use. |
| **Company Name** | Account file | The company name. |
| **Address Block - Acct** | Account file | Complete address (Address 1–3, City, State, Zip). Blank address lines are suppressed automatically so there are no empty lines in the block. |
| **Address Block - Cust** | Customer file | Complete address (Address 1–3, City, State, Zip) from the AR customer record. Blank lines suppressed. |
| **Dear (Name)** | Account file | The "Dear" salutation field. Secondary pop-up selects which of the 9 contact names to associate. |
| **AR Block** | AR transactions file | A composite insert: invoice number, invoice date, original amount, remaining amount, and age in days — all on a single dedicated line. One line prints per open (not fully paid) invoice for the customer. |
| **Address 1–3** | Account file | Individual address lines from the account file. |
| **City** | Account file | City field from the account file. |
| **State** | Account file | State field from the account file. |
| **Zip** | Account file | Zip field from the account file. |
| **Country** | Account file | Country field from the account file. |
| **Invoice No** | AR transactions file | Invoice number. Must be on its own dedicated line; prints once per open invoice. |
| **Invoice Date** | AR transactions file | Invoice date. Must be on its own dedicated line; prints once per open invoice. |
| **Invoice Desc** | AR transactions file | Invoice description. Must be on its own dedicated line; prints once per open invoice. |
| **Orig Amt** | AR transactions file | Original invoice dollar amount. Must be on its own dedicated line; prints once per open invoice. |
| **Rem Amt** | AR transactions file | Invoice amount remaining unpaid. Must be on its own dedicated line; prints once per open invoice. |
| **Age** | AR transactions file | Age of the invoice in days. Must be on its own dedicated line; prints once per open invoice. |

> **Important — AR transaction inserts:** The AR Block and all individual AR transaction inserts (Invoice No, Invoice Date, Invoice Desc, Orig Amt, Rem Amt, Age) **must each occupy their own dedicated line** in the form letter. When printed, one output line is generated for each open invoice the customer has.

---

## Cross-references

| Related Program | Relationship |
|---|---|
| **AR-A — Enter Customers** | CM and AR share the same account-code namespace. The **Cust** button in CM-A opens the matching AR customer record. The **Make Customer** button in CM-A creates a new AR record from a contact. |
| **AR-Q — View Customer Information** | Alternate read-only view reachable from the **Cust** button in CM-A (depending on user menu permissions). |
| **AR-P — Generate Dun Letters** | Consumes form letters created in CM-L that have **Dun Ltr?** = `Y`. |
| **SO — Sales Orders** | Sales Orders for an account are viewable directly from CM-A via the **Sales Orders** button. Quotes are viewable via the **Quotes** button. |
| **SM-I-A — Enter Lead Source Codes** | Defines the lead source codes used in the **Lead Source** field of CM-A. |
| **SM-I-B — Enter Territory Codes** | Defines the territory codes used in the **Territory** field of CM-A. |
| **SM-I-G — Enter Class Codes** | Defines the classification codes assignable to accounts in CM-A. |
| **SM-I-H — Enter Key Date Codes** | Defines the key date codes assignable to accounts in CM-A. |
| **SD-O — Contact Manager Defaults** | Controls system-wide CM settings, including whether the Make Customer feature is enabled. |
| **IM-A — International Configuration** | Enables multi-currency, which activates the **Currency** field in CM-A. |
