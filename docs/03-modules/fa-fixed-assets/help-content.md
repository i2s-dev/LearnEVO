# FA — Fixed Assets

Status: verified (text distilled from the vendor's help file).

*Source: EvoHELP.CHM → Accounting → Fixed Assets (6 topics).*
*Extracted HTML in [samples/chm/extracted/](../../../samples/chm/extracted/).*

The Fixed Assets module sits within the Accounting stack and handles the full lifecycle of depreciable capital assets — from initial entry through periodic depreciation posting to the General Ledger. It supports up to 999,999 assets identified by six-digit asset numbers, stores per-asset GL account assignments, and produces printed reports of both assets and depreciation transaction history.

---

## Contents

- [FA-A — Enter Fixed Assets](#fa-a--enter-fixed-assets)
- [FA-B — Post Depreciation](#fa-b--post-depreciation)
- [FA-C — List Depreciation Transactions](#fa-c--list-depreciation-transactions)
- [FA-D — List Assets](#fa-d--list-assets)
- [FA-E — Import Assets](#fa-e--import-assets)

---

## Module Overview

*Source: [fixed_assets.htm](../../../samples/chm/extracted/fixed_assets.htm)*

**Features:**
- 6-digit asset identification number (supports up to 999,999 assets).
- Depreciation posting to the General Ledger.

**Functions:**
- Enter Assets
- Post Depreciation

**Database tables maintained:**
- Assets
- Depreciation Transactions

**Reports:**
- List Assets
- List Depreciation Transactions

---

## FA-A — Enter Fixed Assets

*Source: [fa-a_enter_fixed_assets.htm](../../../samples/chm/extracted/fa-a_enter_fixed_assets.htm)*

**Purpose.** Use this program to enter each fixed asset that you want to track depreciation for.

### Field Explanations

| Field | Required | Description |
|---|---|---|
| **Asset Number** | Required | A number that uniquely identifies the asset. Can be sequential integers or organized into blocks by category (e.g., one range for vehicles, another for buildings, another for machinery). |
| **Type** | | The category of asset — examples: Vehicle, Computer Equipment. |
| **Description** | | Two-line free-text description of the asset. |
| **Cost Basis** | | The total cost basis used for depreciation calculations. |
| **Residual Value** | | Any portion of the asset value that will not be depreciated (salvage value). |
| **Life** | | Depreciable life expressed in years. |
| **Method** | | The depreciation method to be applied (e.g., straight-line, declining balance). The help file does not enumerate the specific method codes; the user or CPA supplies the appropriate method. |
| **Accumulated Depreciation** | | Depreciation accumulated for this asset to date. Maintained automatically by the system as depreciation transactions are posted; do not edit manually for new assets entered from scratch. |
| **Last Depreciation Amount** | | The dollar amount of the most recent depreciation transaction. Used as the default amount for the next transaction when generating recurring entries in FA-B. |
| **Asset Account** | | GL account to which this asset is assigned (the balance-sheet asset account). |
| **Accum Dep Account** | | GL Accumulated Depreciation contra-asset account for this asset. |
| **Dep Exp Account** | | GL Depreciation Expense account for this asset. |
| **Date Placed in Service** | | The date the asset was first placed into service. |
| **Date Disposed of** | | The date the asset was sold or otherwise removed from service. Left blank while the asset is still active. |
| **Sales Price** | | If the asset was sold, the price received at disposal. |
| **Serial Number** | | Manufacturer or internal serial number, if applicable. |
| **Last Depreciation Percent** | | The percentage rate used for the most recent depreciation transaction. Used as the default percentage when generating recurring entries in FA-B. |
| **Last Depreciation Date** | | The date of the most recent depreciation transaction. |

### General Program Operation

Enter the asset number, type, and description as desired, then supply the cost basis, depreciable life, and the three GL accounts (asset, accumulated depreciation, depreciation expense). The fields **Accumulated Depreciation**, **Last Depreciation Amount**, **Last Depreciation Percent**, and **Last Depreciation Date** are maintained automatically by the system as depreciation transactions are processed through FA-B.

If you are migrating partially-depreciated assets into the module and need to seed the accumulated depreciation balance, use **FA-E Import Assets** rather than typing them in here — FA-E allows import of that accumulated-depreciation-to-date information from a spreadsheet.

---

## FA-B — Post Depreciation

*Source: [fa-b_post_depreciation.htm](../../../samples/chm/extracted/fa-b_post_depreciation.htm)*

**Purpose.** Use this program to create and post depreciation transactions.

### General Program Operation

Two entry paths are available:

1. **Add (individual entry).** Click **Add** to create each depreciation transaction one at a time. Enter the asset, amount, percentage, and date for each transaction individually.

2. **Generate Recurring.** Click **Generate Recurring** to have the system automatically populate a list of all assets, pre-filled with the depreciation amount and percentage from each asset's most recent transaction (i.e., the values stored in **Last Depreciation Amount** and **Last Depreciation Percent** on the asset record). You can then review the generated list, edit any entries that differ from the prior period, and post them all at once.

**Important limitation:** The program does not interpret tax or GAAP depreciation rules and does not calculate amounts or percentages automatically. The user (or their CPA) must supply the correct depreciation amounts and percentages. The system is a transaction recorder, not a depreciation calculator.

When transactions are posted, the system:
- Records each transaction in the Depreciation Transactions database.
- Updates the asset record's **Accumulated Depreciation**, **Last Depreciation Amount**, **Last Depreciation Percent**, and **Last Depreciation Date** fields.
- Posts to GL: debit the **Dep Exp Account**, credit the **Accum Dep Account** defined on the asset record in FA-A.

---

## FA-C — List Depreciation Transactions

*Source: [fa-c_list_depreciation_transactions.htm](../../../samples/chm/extracted/fa-c_list_depreciation_transactions.htm)*

**Purpose.** Use this program to view or print a list of depreciation transactions.

### General Program Operation

The screen displays all depreciation transaction entries from the Depreciation Transactions database. Use the **Filter Grid** button to narrow the displayed rows by any desired criteria — date range, asset number, asset type, or any other available field. Once the desired set is displayed, use the **Print** button to produce a printed report.

Note: the help file uses "reansactions" (apparent typo for "transactions") in the original source — this is a vendor typo in the CHM, not an EVO term.

---

## FA-D — List Assets

*Source: [fa-d_list_assets.htm](../../../samples/chm/extracted/fa-d_list_assets.htm)*

**Purpose.** Use this program to view or print a list of assets.

### General Program Operation

The screen displays all assets from the Assets database. Use the **Filter Grid** button to narrow the displayed rows by asset number, type, or any other available field. Use the **Print** button to produce a printed report of the filtered asset list.

---

## FA-E — Import Assets

*Source: [fa-e_import_assets.htm](../../../samples/chm/extracted/fa-e_import_assets.htm)*

**Purpose.** Use this program to import assets from a spreadsheet. The importable fields are the same as those defined in FA-A Enter Fixed Assets (see the field table in the FA-A section above).

### General Program Operation

Enter the file name to be imported, then map each data field to its corresponding column (or position) in the import file. Two file formats are supported:

| Format | How to specify column mapping |
|---|---|
| Comma-delimited (CSV) | Enter the column number only (e.g., `1` for the first column, `2` for the second). |
| Fixed-length (flat file) | Enter the starting character position and the field length for each field. |

**Primary use case:** importing partially-depreciated assets when first setting up the FA module. Because FA-A does not expose accumulated depreciation for manual entry on new assets, FA-E is the correct path for bringing in assets that already carry a depreciation history (e.g., migrating from another system or from a CPA's spreadsheet).

---

## Cross-references

- **GL (General Ledger):** FA-B Post Depreciation writes journal entries to the three GL accounts stored on each asset record — the asset account, the accumulated depreciation account, and the depreciation expense account. See the GL module documentation for account setup and period-end procedures.
- **AM (Accounting Maintenance):** System-level setup for the accounting modules. FA inherits its period and company context from AM.
- **FA-E ↔ FA-A:** FA-E is the bulk-import path for assets; FA-A is the single-record entry path. All field definitions are shared — see FA-A for the canonical field list.
- The FA module has no direct integration with Accounts Payable (AP) for asset acquisition or with Work Orders (WO) for capitalized labor; those connections, if any, are handled outside the module by the user.
