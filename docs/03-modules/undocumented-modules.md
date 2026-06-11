# Undocumented Modules — Reference
Status: partial | verified-from-DFM-and-CHM

Module purposes confirmed from DFM form analysis (network share) and CHM help content.
Logic detail is limited to what's readable from forms and strings — RWN logic is encrypted.

---

## AM — Accounting Maintenance ⚠️ NAME CORRECTION

**Previously labeled "Asset Management" — INCORRECT. AM = Accounting Maintenance.**

This module manages GL period control, account setup, and financial statement formatting.
It is effectively the GL administration module.

**Menu codes:** AM-A through AM-E (at minimum)

| Code | DFM | What it does |
|------|-----|-------------|
| AM-A | T7AMA.DFM | **Reset GL Close Date** — sets Current Fiscal Year Start Date, Open Period Start/End Date, Accounting Open Period Start Date. Controls which periods are open for posting. |
| AM-B | T7AMB.DFM | **GL Account Historical Balance Analysis** — displays multi-year comparative balance history for a GL account (current year + up to 6 years past). Fields: BKGL.CURRENT, BKGL.1YPAST, ISGL.3YPAST–6YPAST arrays. |
| AM-C | T7AMC.DFM | **Enter GL Accounts** — creates/modifies GL account master records. Fields: Account Code, Dept (optional), Description, Account Type (A=Asset, L=Liability, O=Owner's Equity, I=Income, E=Expense), Non-Cash flag, Inactive flag, Budget Amounts (12 periods), Beginning Balance, Ending Balance. Primary table: BKGLCOA. |
| AM-D | T7AMD.DFM | **GL Department Utilities** — two functions: (1) Copy Department: duplicates all GL accounts from TEMPLATE dept to NEW dept, with option to clear budgets and filter by account type. (2) Delete Department: removes entire GL department from chart of accounts (irreversible — "no way to retrieve this data once deleted"). |
| AM-E | T7AME.DFM | **Format Financial Statements** — configures GL account mapping for Income Statement, Balance Sheet, and Cash Flow statement. Each statement section maps GL account ranges to report lines. |

**Primary tables:** BKGLCOA (accounts), BKGLTRAN (transactions), ISGL\* (extended GL tables)

**Confidence: 75/100** — All 5 DFM files read directly from network share; form labels confirmed. Business logic behind each form inferred from label text.

---

## FA — Fixed Assets

**DFM files confirmed:** T7FAA.DFM, T7FAB.DFM, T7FAE.DFM (3 forms)

**From CHM help content:**
- **FA-A — Enter Fixed Assets:** Records asset details including cost basis, useful life, depreciation method.
- **FA-B — Post Depreciation:** Creates and posts depreciation journal entries by asset to GL.

**Likely tables:** BKFA\* (not yet found in DDF — may use IS\* prefix or a small table set)

**Confidence: 48/100** — DFM files confirmed on network share; CHM help confirms two operations; table names not yet located in DDF.

---

## JC — Job Costing

**DFM files confirmed:** T7JCA.DFM, T7JCB.DFM, T7JCE.DFM, T7JCENG.DFM, T7JCF.DFM, T7JCH.DFM, T7JCL.DFM, T7JCM.DFM, T7JCN.DFM, T7JCP.DFM, T7JCQ.DFM, T7JCR.DFM, T7JCRM.DFM, T7JCJCS.DFM (14 forms)

**From CHM help content:**
- **JC-A — Print Job Cost Report:** Cost and profit analysis per work order with variance reporting (estimated vs. actual labor, material, overhead, outside).

**Relationship to WO:** JC module reads WORKORD and related WO\* tables; it provides reporting and analysis on top of work order costs rather than creating new records.

**Confidence: 52/100** — 14 DFM files confirmed; CHM gives JC-A purpose. Full module scope unclear.

---

## SA — Sales Analysis

**DFM files confirmed:** T7SAA.DFM, T7SAM.DFM, T7SAN.DFM, T7SAO.DFM, T7SAP.DFM, T7SAQ.DFM (6 forms)

**What it does:** Provides sales reporting and analysis. Reads AR invoice history (BKARINV, BKARINVL) and customer data (BKARCUST) to produce sales-by-customer, sales-by-item, sales-by-salesperson, and similar reports.

**Confidence: 45/100** — DFM files confirmed; purpose inferred from module name and form count. No CHM help content or source analyzed.

---

## SH — Shipping

**DFM files confirmed:** 13+ forms including bill-of-lading, manifests, and shipment tracking.

**What it does:** Manages outbound shipments — links sales orders to carrier/tracking, produces bills of lading (BOL), packing manifests, and shipping labels.

**Likely tables:** BKARSHIP (ship-to addresses already confirmed), likely BKSH\* or IS\* shipping tables.

**Confidence: 45/100** — DFM count and naming confirmed; no CHM content or source analyzed.

---

## SM — System Maintenance

**DFM files confirmed:** 50+ forms — the largest single module by form count.

**What it does:** Global configuration and setup for all modules. Likely contains:
- Company defaults (address, GL accounts, terms, tax codes)
- User setup (creates AHSYLOG records)
- Printer configuration
- System parameters (values written to BKSYMSTR / BKYSMSTR)
- Ship-via codes, payment terms, tax groups, etc.

**Likely tables:** BKSYMSTR (286 fields), BKYSMSTR (195+ YN flags), AHSYLOG, BKLOGON, BKSYPRTR, BKSYUSER, BKSYCFG, and many IS\* lookup tables.

**Confidence: 50/100** — Form count and module role confirmed; specific SM form content not yet read from network share.

---

## DE — Data Exchange

**Confirmed from CHM:**
- **DE-A — SQL Query/Export:** Exports selective EVO records to CSV format. Contains preset SQL queries for GL/PO/inventory reconciliation:
  - `GLPOINV` — GL posted PO invoices
  - `GLPORECPT` — GL posted PO receipts
  - `Inv_Txn_no_GL` — Inventory transactions without GL entries
  - `INVGL` — Inventory GL summary
  - `INVGLACCT` — Inventory by GL account
  - `Inventory_Non_Asset` — Non-asset inventory items
  - `Non_Inventory_Asset` — Asset GL items not in inventory

**What it is:** A reporting/export tool that runs predefined SQL queries against the Pervasive database via ODBC and outputs CSV files. This is the internal data-exchange utility (distinct from EDI which uses the ED module).

**Confidence: 65/100** — CHM help content confirmed; preset query names confirmed; underlying SQL not read.

---

## CS — Customer Service / Salespersons

**Confirmed from CHM:**
- **CS-A — Enter Salespersons:** Creates and maintains salesperson master records. Salespersons can be employees or outside agents. Records: salesperson code, name, commission rate structure.

**DFM files confirmed:** T7CSA.DFM + 11 more forms

**Likely tables:** BKPRSALE (salesperson/commission table already identified in AR strings)

**Confidence: 55/100** — CS-A confirmed from CHM; form count confirmed; remaining CS operations not yet documented.

---

## CM — Contact Manager / CRM

**Confirmed from CHM:**
- **CM-A — Enter Contact Accounts:** Maintains prospect/customer master file with contact history, notes, reminders, class codes, key dates, and ability to convert prospect to AR customer.

**DFM files confirmed:** T7CMA.DFM + 10 more forms (11 total), including ABC classification and conversion forms.

**What it does:** A built-in CRM system. Tracks prospects and customers beyond what BKARCUST stores — contact history, follow-up reminders, lead source tracking, activity notes. The BKCM\* family (46 tables) stores all CRM data.

**Primary tables:** BKCMACCT (contact accounts), BKCMCUST (CRM customer link), BKCMREP (rep assignments), BKCMDUN / BKCMDUNH (dun letters / history), BKCMTERR (territories), BKCMLEAD (lead sources), BKCMMHST (message history), BKCMVNDH / BKCMVNFC / BKCMVNDF (vendor history/follow-up/contacts), BKCMCTL1–4 (control tables), BKCMTEMP (templates).

**Confidence: 60/100** — CM-A confirmed from CHM; BKCM\* table family (46 tables) confirmed in DDF; form count confirmed.

---

## SC — Scheduling / Capacity Planning

**DFM files confirmed:** T7SCA.DFM + 7 more forms (8 total)

**What it does:** Shop scheduling and capacity planning. Likely reads WORKORD and WORKCTR to show capacity loading by work center and assist in scheduling work order operations across the production calendar.

**Likely tables:** WORKORD, WORKCTR, CALENDAR, SCHEDCAL, WOROUT (for routing/operation data)

**Confidence: 40/100** — Form count confirmed; purpose inferred from module name and ERP context.

---

## LC — Lot Control

**DFM files confirmed:** T7LCA.DFM + 6 more forms (7 total)

**What it does:** Lot number tracking for inventory items. Assigns lot numbers at receipt, tracks lot quantities through production and shipment.

**Primary tables:** LOT (lot master), and lot fields in BKICMSTR, INVTXN.

**Confidence: 42/100** — Form count confirmed; purpose inferred from name.

---

## QC — Quality Control

**DFM files confirmed:** T7QCA.DFM + 11 more forms (12 total), including test specifications and results forms.

**What it does:** Receiving inspection and quality tracking. Items can be placed in QC hold at receipt (inventory transaction type Q = QC Receipt). Test specifications define what to check; results are recorded per lot/receipt.

**Likely tables:** BKQCMSTR (QC master — already in DDF), BKQCTRAN (QC transactions — already in DDF)

**Confidence: 48/100** — Form count and types confirmed; BKQCMSTR/BKQCTRAN confirmed in DDF; workflow not traced.

---

## SR — Service / Repair

**DFM files confirmed:** T7SRA.DFM + 10 more forms (11 total)

**What it does:** Service order management — tracking repair/service work for customers. Similar to work orders but for customer-owned equipment or warranty service.

**Note:** T7SOA.DFM (Sales Orders) has a "SR Type" tab and "Print S/R" button, suggesting SO and SR modules are tightly integrated — service requests may originate from the SO screen.

**Confidence: 42/100** — Form count confirmed; SR/SO integration observed in T7SOA.DFM.

---

## WC — Work Center

**DFM files confirmed:** T7WCA.DFM + 11 more forms (12 total)

**What it does:** Work center master maintenance — defines the production resources (machine groups, labor areas) used in routing operations and scheduling. Each work center has capacity, efficiency, and cost rate settings.

**Primary tables:** WORKCTR (work center master — already confirmed)

**Confidence: 55/100** — Form count confirmed; WORKCTR table confirmed; capacity/cost fields not extracted.

---

## SD — Standard Data

**DFM files confirmed:** T7SDET.DFM (1 form found)

**What it does:** Company-level defaults and standard data setup — likely configures system-wide defaults for terms, classes, codes, and other reference tables used across all modules.

**Confidence: 35/100** — Only 1 DFM found; purpose inferred.

---

## UT — Utilities

**DFM files confirmed:** T7UTA.DFM + 6 more forms (7 total)

**What it does:** System utility functions — data rebuilds, index repairs, data purges, and maintenance tools that don't belong to a specific module.

**Confidence: 42/100** — Form count confirmed; specific operations not documented.

---

## PI — Physical Inventory

**DFM files confirmed:** T7PIA.DFM + 9 more forms (10 total)

**What it does:** Periodic physical count cycle — freeze inventory, enter counts, calculate variances, approve and post adjustments.

**Primary tables:** BKPI\* (7 tables)

**Confidence: 52/100** — Form count confirmed; cycle steps from CHM; table family confirmed.

---

## HH — Handheld Terminals

**DFM files confirmed:** T7HHA.DFM + 29 more forms (30 total) — largest handheld form set.

**What it does:** Warehouse handheld device UI — streamlined screens for barcode scanning, inventory transactions, receiving, picking, and labor entry from mobile terminals.

**Primary tables:** BKDC\* family (shares data collection tables with DC module); label tables BKDC\*

**Confidence: 48/100** — Form count confirmed; purpose confirmed from DC module docs.

---

## ED — EDI (Electronic Data Interchange)

**Confirmed from CHM:**
- **ED-B — Import EDI Orders:** Imports downloaded orders from `EVOSO.IN` file into EDI sales order staging tables.

**Primary tables:** BKED\* (6 tables already in DDF)

**Confidence: 50/100** — ED-B confirmed from CHM; BKED\* tables confirmed in DDF; full EDI pipeline not traced.

---

## ES — Estimating

**Confirmed from CHM:**
- **ES-A — Enter Estimates:** Creates cost estimates with multiple lines and quantities per line. Pre-sales quoting system.

**Primary tables:** BKES\* (3 tables)

**Confidence: 48/100** — ES-A confirmed from CHM; BKES\* confirmed in DDF.

---

## GL — General Ledger (additional ops via T7GL\* forms)

**DFM files confirmed:** T7GLA.DFM + 19 more forms (20+ total)

**Confirmed from CHM:**
- **GL-A — View Chart of Accounts:** Displays BKGLCOA with budget vs. actual comparison and multi-year history.
- **GL-B — Enter/Post General Journal Transactions:** Manual GL entries, cash receipts/disbursements, reversals, and journal templates. Primary table: BKGLTRAN.

**Confidence: 68/100** — Form count confirmed; GL-A and GL-B confirmed from CHM; BKGLCOA and BKGLTRAN schemas documented.

---

## PR — Payroll (additional ops via T7PR\* forms)

**DFM files confirmed:** T7PRA.DFM + 49 more forms (50 total) — second-largest module by form count.

**Primary tables:** BKPRMSTR (246+ fields — payroll master), BKPRHIST (127 fields), BKPRW2 (196+ fields), BKPRGLFL (664 fields — GL posting config), BKPRBOOK, BKPRCOMM, BKPRCURP, BKPRFTAX, BKPRHCOM, BKPRINFO, BKPRSALE, BKPRSTFL, BKPRTC, BKPRTCFG.

**Confidence: 52/100** — Form count and table family confirmed; payroll logic not traced.

---

## PO — Purchase Orders (additional ops via T7PO\* forms)

**DFM files confirmed:** T7POA.DFM + 39 more forms (40 total)

**Primary tables:** BKAPPO (57 fields — PO header), BKAPPOL (38 fields — PO lines), plus BKAPRFQ/BKAPRFQL (RFQ tables), BKAPQUOT (quotes), BKAPHPO/BKAPHPOL (history PO).

**Confidence: 60/100** — Form count confirmed; BKAPPO/BKAPPOL schemas extracted this session.

---

## MR — MRP (additional ops via T7MR\* forms)

**DFM files confirmed:** T7MRA.DFM + 18 more forms (19 total)

**Already documented:** Full MRP algorithm traced from BKMRF.SRC. See `docs/03-modules/` for MR source analysis.

**Confidence: 72/100** — Full source analysis done; form count confirmed.

---

*Last updated: 2026-06-11*
*Source: DFM files read from \\I2S109-SOLIDCRM\DBAMFG$\, CHM help topics from samples\chm\extracted\*
