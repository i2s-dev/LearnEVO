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

**Forms read from network share:**

| Code | DFM | What it does |
|------|-----|-------------|
| FA-A | T7FAA.DFM | **Asset Master Entry** — add/edit fixed assets. Fields: Asset Number, Type, Description (2 lines), Cost Basis, Residual Value, Useful Life, Depreciation Method, Asset Account (GL), Accum Dep Account (GL). Tables: IS.FXA.NUMBER/TYPE/DESC/CSTBAS/RESVAL/LIFE/METH |
| FA-B | T7FAB.DFM | **Post Depreciation** — reviews and posts depreciation entries. Fields: Asset Number, Amount, Percent, Post Date, Net Asset Value, Accumulated Dep Account (debit/credit), Dep Expense Account (debit/credit), "Ready to Post" flag. Tables: IS.FXT.AMOUNT/NETAVAL/ACDEPA/ACDEPD/DEPEXPA/DEPEXPD |
| FA-E | T7FAE.DFM | **Export Assets** — exports fixed asset data (COMMA.FIXED.STR = comma or fixed-width format; file.name = output file) |

**Key findings:**
- Table prefix **IS.FXA.*** = IS Fixed Asset record (asset master)
- Table prefix **IS.FXT.*** = IS Fixed Asset Transaction (depreciation entries)
- Both depreciation debit and credit accounts are tracked (ACDEPA/D, DEPEXPA/D) — confirms standard double-entry journal structure for depreciation posting
- "Ready to Post" flag in FA-B = batch-style depreciation: calculate first, then review, then post
- FA is a small but self-contained GL sub-module — reads only IS.FXA.*/IS.FXT.*

**Confidence: 75/100** — All 3 DFM files read from network share; table structure confirmed (IS.FXA.* + IS.FXT.*); depreciation posting workflow confirmed; specific depreciation method codes not documented.

---

## JC — Job Costing

**DFM files confirmed (14 total):** T7JCA.DFM, T7JCB.DFM, T7JCE.DFM, T7JCENG.DFM, T7JCF.DFM, T7JCH.DFM, T7JCL.DFM, T7JCM.DFM, T7JCN.DFM, T7JCP.DFM, T7JCQ.DFM, T7JCR.DFM, T7JCRM.DFM, T7JCJCS.DFM

**From CHM help content:**
- **JC-A — Print Job Cost Report:** Cost and profit analysis per work order with variance reporting (estimated vs. actual labor, material, overhead, outside).

**DFM analysis — full form inventory:**

| Code | DFM | What it does |
|------|-----|-------------|
| JC-A | T7JCA.DFM | **Print Job Cost Report** — filter by WO range, status, item range, customer range, job range. Options: G&A Cost%, Summary vs. Detail, Composite Report, Component Desc, Include WO Notes, Rebuild WO. |
| — | T7JCB.DFM | Report filter: Job range, WO range, WO status, customer range — likely JC-B report |
| JC-E | T7JCE.DFM | Active/Archive WOs, WO range, WO status, **Parent Item range**, Job range — parent/child WO cost roll-up |
| — | T7JCF.DFM | WO cost report filter (WO range, status, item range, job range) — likely JC-F |
| — | T7JCH.DFM | WO cost by operation — WO status, item range, **Scheduled Finish Date range**, Sequence Number range |
| JC-L | T7JCL.DFM | WO status filter — labor/cost report |
| JC-M | T7JCM.DFM | WO status filter — cost summary |
| JC-N | T7JCN.DFM | **Cost Calculation Options** — `ISCALC.HOW.C` (Current Month), `ISCALC.HOW.H` (Historical), `ISCALC.HOW.P` (Proposed); `ISCOST.BREAKOUT` (cost breakout detail); date ranges (last month thru / current month thru) |
| JC-P | T7JCP.DFM | **Print Materials in WIP** — reports all material issued to WOs but not yet completed |
| JC-Q | T7JCQ.DFM | WO status filter — labor/cost report |
| JC-R | T7JCR.DFM | WO status filter — cost report |
| — | T7JCRM.DFM | Sub-form (results grid) |
| JC-S | T7JCJCS.DFM | WO status filter — cost report |
| (engine) | T7JCENG.DFM | **JC Report Engine** — shared filter/engine dialog used by all JC reports. Parameters: Report Type, Sort/Subtotal By, Level of Detail; WO Status (Firmed/Released/Closed/Cancelled/Indirect), WO Source (Active/Archived), Labor Type (Regular/OT/Doubletime/Sick/Vacation/Holiday), Shift (1st/2nd/3rd), Multiple Setup (Include Once); ranges for WO, Work Center, Item, Tool, Employee, Machine, Labor Date, Job, Sequence, Scrap Code, QC Code, Rework Code, Dept Code, WO Actual Finish Date. |

**Key module facts:**
- JC is a **reporting-only module** — reads WO data, creates no records
- JC-N cost calculation modes: Current, Historical, Proposed — enables what-if cost analysis
- JC-E handles multi-level WO cost roll-up via parent item range filter
- JC-P (Materials in WIP) is key reconciliation: shows materials consumed but WO not yet closed
- T7JCENG is the universal engine dialog shared by all JC print operations
- WO statuses: Firmed, Released, Closed, Cancelled, Indirect; Sources: Active, Archived
- Labor types: Regular, OT, Doubletime, Sick, Vacation, Holiday (6 types)
- Shifts: 1st, 2nd, 3rd
- Tool and machine range filters confirm EVO tracks tool/machine usage on WO operations

**Relationship to WO:** JC reads WORKORD and WO labor/operation tables. It provides variance analysis (estimated vs. actual) for labor, material, overhead, and outside processing.

**Primary tables:** WORKORD, WO labor/operation tables (WOPROC, WOSCRAP, WOREMATR), ISCALC.* (cost calculation config), ISCOST.* (cost breakout config)

**Confidence: 68/100** — All 14 DFM files read from network share; form purposes confirmed from captions; JC Engine parameters fully extracted; specific cost formula logic inaccessible (in RWN).

---

## SA — Sales Analysis

**DFM files confirmed:** T7SAA.DFM, T7SAM.DFM, T7SAN.DFM, T7SAO.DFM, T7SAP.DFM, T7SAQ.DFM (6 forms)

**What it does:** Provides sales reporting and analysis. Reads AR invoice history (BKARINV, BKARINVL) and customer data (BKARCUST) to produce sales-by-customer, sales-by-item, sales-by-salesperson, and similar reports.

**Confidence: 45/100** — DFM files confirmed; purpose inferred from module name and form count. No CHM help content or source analyzed.

---

## SH — Shop Scheduling ⚠️ NAME CORRECTION

**Previously labeled "Shipping" — INCORRECT. SH = Shop (floor) Scheduling.**

This module manages finite-capacity scheduling of work orders across work centers on the shop floor.

**DFM files confirmed (15+ total):** T7SHA.DFM, T7SHB.DFM, T7SHC.DFM, T7SHE.DFM, T7SHF.DFM, T7SHG.DFM, T7SHH.DFM, T7SHI.DFM, T7SHJ.DFM, T7SHM.DFM, T7SHN.DFM, T7SHO.DFM, T7SHP.DFM + T7SHIPRTM.DFM, T7SHOWLINEHIST.DFM

| Code | DFM | What it does |
|------|-----|-------------|
| SH-A | T7SHA.DFM | **WO Scheduling Grid** — main WO browse showing WIP work orders. Fields: WO#/prefix/suffix, Item, Description, Customer, Sched Start, Sched Finish, Due Date, Priority, Class, Lead Time. Filter: Status (Scheduled/Firmed/Released), Priority (1/2/3), Item Class/Category range. Tables: MTWO.WIP.* |
| SH-B | T7SHB.DFM | **WO Operation Scheduling** — drill-down to WO routing operations. Fields: Operation, Work Center, Assigned WC, Start/Finish dates, Status, Qty Started, Qty Complete, Contention, Overlap Hours, Neg Overlap, Queue, Labor Type, Vendor, Lead Time. Tables: MTWORO.* (WO routing operations), MTWC.* |
| SH-C | T7SHC.DFM | **Work Center browser** — displays MTWC.WCDESC, MTWC.DEPT, MTWC.DEPTDESC, IS.OUTPROC (outside process flag), MTWC.HRSWEEK (weekly capacity hours) |
| SH-E | T7SHE.DFM | **Change Due Date / Priority** — quick WO due date edit (MTWO.WIP.DDATE) |
| SH-F | T7SHF.DFM | **Priority filter/view** — WO priority management |
| SH-G | T7SHG.DFM | WO status filter (Scheduled/Firmed/Released/Closed/Cancelled) |
| SH-H | T7SHH.DFM | WO range with start/finished date filter |
| SH-I | T7SHI.DFM | **Dispatch Report** — comprehensive scheduling report. Options: WO status, class, priority, work center range, start/finish date range, customer range, planner code range, starting weekly date. Color coding: elapsed start date color, background color, priority change color. Options: Recalculate Time Remaining, Limit to WOs with Available Components, Print BOM Components (type FRAM), Print Purchase Orders (SPAN/ASIS). Sort by options. |
| SH-J | T7SHJ.DFM | Status/filter view (similar to SH-G) |
| SH-M | T7SHM.DFM | Item range query (BKIC.PROD.DESC, QUANTITY, SDATE) |
| SH-N | T7SHN.DFM | Type filter (E.TYPE[1/2]), print report |
| SH-O | T7SHO.DFM | Inquiry/browse form |
| SH-P | T7SHP.DFM | **Report Color Configuration** — sets colors for Priority Change, Elapsed Start Date, Background (for SH-I report) |
| (sub) | T7SHIPRTM.DFM | User/RTM template selector sub-form (shared) |
| (sub) | T7SHOWLINEHIST.DFM | SO line price history sub-form (ISAR.CHG.* — before/after price, discount) — likely shared with SO module |

**Key module facts:**
- Primary tables: MTWO.WIP.* (WIP work order data), MTWORO.* (WO routing operations), MTWC.* (work center master: capacity hours/week, dept, outside-process flag)
- WO statuses in this module: Scheduled, Firmed, Released, Closed, Cancelled
- SH is the scheduling/dispatch layer on top of WO — it does not create work orders, it schedules and monitors their execution
- Outside-process operations (MTWC.IS.OUTPROC) are tracked in work center records
- The SH-B contention/overlap fields suggest finite-capacity scheduling with overlapping operations

**Note on naming:** The "SH" prefix may stand for "SHop" or "SHedule". The DFM inventory doc previously labeled this "Shipping" — that was incorrect. Physical carrier/shipping is handled within SO module (ship-confirm forms T7SOx).

**Confidence: 72/100** — All 15 DFM files read; MTWO/MTWORO/MTWC table access confirmed; scheduling function confirmed from field names and captions; underlying scheduling algorithm inaccessible (in RWN).

---

## SM — System Maintenance

**DFM files confirmed:** 50+ forms — the largest single module by form count.

**What it does:** Global configuration and setup for all modules:
- Company defaults (address, GL accounts, terms, tax codes)
- User setup (creates AHSYLOG records)
- Printer configuration
- System parameters (values written to BKSYMSTR / BKYSMSTR)
- Ship-via codes, payment terms, tax groups, item class GL overrides
- Shipping account preferences per customer

**Forms read from network share:**

| DFM | Purpose | Key fields / tables |
|-----|---------|---------------------|
| T7SMC.DFM | Item Class List master | Class Code, Description → MTCLASS |
| T7SMCA.DFM | Item Class maintenance (edit mode) | Class, Description → MTCLASS |
| T7SMCB.DFM | Class GL Override Setup | Item Class + Location → GL account overrides (Inv Asset, COGS, WIP, Labor, OH) → BKIC |
| T7SMCC.DFM | Item Class List (grid browse) | Class, Description → MTCLASS |
| T7SMU.DFM | Customer shipping preferences | Customer, Ship Via, Account#, Billing Type (C/T/B), Insurance, Third Party → Customer Master, Ship Via codes |
| T7SMT.DFM | Terms/shipper setup | Customer, Ship Via, Priority, Account, Inactive, Bill Type → shipping term tables |
| T7SMTset.DFM | Work order setup phase | WO#, Customer, Drawing, Revision, Employee, Operation, Machine → WORKORD, WOBOM |
| T7SMTend.DFM | Work order completion/serial scan | WO#, Employee, Machine, Operation, Serial scan → WORKORD, WO serial tables |

**Key finding — class GL overrides (T7SMCB):** EvoERP supports per-class, per-location GL account
overrides. Each item class × location combination can have independent GL accounts for:
inventory asset, inventory expense, COGS, taxable sales, non-taxable sales, WIP inventory asset,
absorbed labor, absorbed fixed OH, absorbed variable OH, and material burden. This is the mechanism
for multi-location or multi-product-line accounting separation.

**Additional forms read from network share (2026-06-15):**

| DFM | Size | Purpose | Key fields |
|-----|------|---------|------------|
| T7SMK.DFM | 273 KB | **Evo User Settings** — per-user preference panel (writes EvoSettings.INI). Options: Toolbar, Language, Sounds, Default Print Path, "Check for Reminders every X minutes" | evo.cfg.toolbar, evo.cfg.lang, evo.cfg.sounds, defprintpath, evo.cfg.remind, remmin |
| T7SMF.DFM | 107 KB | **Tax Group Setup** — defines multi-component tax groups. Array fields for up to N tax codes per group: ISIS.TXG.CODE[1..N], ISIS.TXG.DESCF (description), ISIS.TXG.PERCC (rate), ISIS.TXG.TAXON (tax-on flag), ISIS.TXG.FRGT (freight taxable flag) → ISIS.TXG table |
| T7SME.DFM | 67 KB | **Tax Code Entry** — individual tax codes with GL and vendor. Fields: ISIS.TXF.CODE, ISIS.TXF.DESC, ISIS.TXF.IDNUM (ID# for state/fed filing), ISIS.TXF.VNDCD + BKAP.VENDNAME (AP vendor for tax remittance!), ISIS.TXF.SOPERC[1] (SO tax rate), SO Taxes/PO Taxes/GL Account → ISIS.TXF table |
| T7SMO.DFM | 63 KB | **Ship-Via Carrier Setup** — carrier master records. Fields: ship via code, name, description, notes (2 lines), telephone, **carrier home page URL**, **tracking URL** (for customer self-tracking), vendor range → IS ship-via table |
| T7SMD.DFM | 53 KB | **Payment Terms Entry** — IS.TERMS.NAME/NUM/DESC/AMT, `due.on.rcpt` flag (Net 30, 2% 10 days, etc.) → IS.TERMS table |
| T7SMG.DFM | 96 KB | **Employee Report** — print employee list with filters: Employee range, Month (for birthday reports), Include Terminated, Print Contacts, Label/Birthday Report options |
| T7SMJM.DFM | 80 KB | **SM-JM Customer Code Merge** — merges old customer code into new; OLD_PART, CUSTNAME, ADD1, ADD2 — customer record consolidation utility |
| T7SMJN.DFM | 73 KB | **SM-JN Vendor Code Merge** — same as SM-JM for vendors: oldcode, VENDNAME, ADD1, ADD2 |
| T7SMJC.DFM | 81 KB | **SM-JC Job Costing Setup** — configures JC module parameters: MASTER, TRANSACT, RPT.ONLY, METHOD options |
| T7SMJB.DFM | 61 KB | **SM-JB Job Archive** — archive/cancel job records with options: ARCH.CANCEL, include archived, include exceptions |
| T7SMGA.DFM | 75 KB | **Employee Contact Maintenance** — emp.name, contact title, contact name, employee code |
| T7SMPJ.DFM | 57 KB | **SM-P-J UL Code Entry** — UL Code (Underwriters Laboratories or user-defined link), Description, Image Link File |
| T7SMPF.DFM | 56 KB | **Job Number Master** — IS.JOB.NUMB, IS.JOB.DESC, IS.JOB.CUST (customer), IS.JOB.VEND (vendor). Job/contract/project tracking codes used across SO/WO/PO. |
| T7SMPH.DFM | 50 KB | **Maintenance Cycle Setup** — IS.CYCLE.CODE, Description, Frequency (Days). Defines preventive maintenance cycles for equipment. |
| T7SMSD.DFM | 52 KB | **AP Invoice Document Linking** — BKAP.INVT.DESC, Invoice.Link, Inv.num. Links scanned document files to AP invoice records. |

**Key findings from second SM read pass:**
- **SM-K is "Evo User Settings"** — confirms this writes `EvoSettings.INI` per user (not per company)
- **Tax system uses two tables:** ISIS.TXF (individual tax codes, with AP vendor for remittance) and ISIS.TXG (tax groups combining multiple TXF codes per line item)
- **Ship-Via includes tracking URL** — carriers can have a tracking URL template stored in SM-O
- **Job number master (IS.JOB.*)** explains the "Job Number" filter seen across JC, WO, and PO modules — jobs are SM-managed reference codes
- **Customer/Vendor merge** (SM-JM/JN) is a database utility to consolidate duplicate records
- **Maintenance cycles** (SM-PH, IS.CYCLE.*) suggests EVO has a preventive maintenance scheduling feature

**Primary tables:** BKSYMSTR (286 fields), BKYSMSTR (195+ YN flags), AHSYLOG, BKLOGON, BKSYPRTR, BKSYUSER, BKSYCFG, MTCLASS, BKIC (class-GL overrides), ISIS.TXF (tax codes), ISIS.TXG (tax groups), IS.TERMS (payment terms), IS.JOB.* (job number master), IS.CYCLE.* (maintenance cycles)

**Confidence: 72/100** — 23+ forms now read from network share; tax/terms/ship-via/job-number/user-settings structure confirmed; BKSYMSTR/BKYSMSTR (global system parameters, 481+ fields) not yet fully decoded.

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

## CS — Commission / Salesperson Management

**DFM files confirmed (12 total):** T7CSA.DFM, T7CSB.DFM, T7CSC.DFM, T7CSD.DFM, T7CSDE.DFM, T7CSDO.DFM, T7CSDX.DFM, T7CSE.DFM, T7CSF.DFM, T7CSI.DFM, T7CSO.DFM, T7CSP.DFM

**What it does:** Tracks salesperson records and commission calculations. Salespersons can be employees (linked by SEMPNUM) or outside agents (linked to AP via BKPR.AGNT.CODE vendor code).

| Code | DFM | What it does |
|------|-----|-------------|
| CS-A | T7CSA.DFM | **Enter Salespersons** — create/edit salesperson records. Fields: Salesperson Number, Class, Vendor Code (for outside agents — links to AP), Commission Rate, First Name/MI, Last Name, HOW (commission calculation method), WHEN (payment timing), SLSP GL Account (commission expense account). Tables: BKPR.SLS.* |
| CS-B | T7CSB.DFM | **View Salesperson Info** — dashboard showing Quota, COGS, Comm Due, Comm Paid, Receipts. Tracks commission paid by period: BKPR.SLS.PAID[1-7] (7 periods). |
| CS-C | T7CSC.DFM | **Print Salespersons Info** — salesperson info report |
| CS-D/DO/DX | T7CSD.DFM, T7CSDO.DFM, T7CSDX.DFM | **Transfer Sales Commissions** — moves commission from pending to payable. Fields: BKPR.COMM.SLSP (salesperson), BKPR.COMM.CCODE (customer code), BKPR.COMM.INVNM (invoice number), BKPR.COMM.INVDT (invoice date). Three DFM variants = different transfer states or steps. |
| CS-DE | T7CSDE.DFM | **Rep Link Import** — imports salesperson/representative linkage data |
| CS-E | T7CSE.DFM | **Print Commission Detail** — itemized commission by salesperson. Filter: Item range + Salesperson range. |
| CS-F/P | T7CSF.DFM, T7CSP.DFM | **Print Commission Summary** — summary commission report. Filter: Salesperson range + Invoice Date range. |
| CS-I | T7CSI.DFM | **Evo Master Inquiry** — general lookup by Customer Code, Item Number, SO Number, Invoice Number. Shared inquiry form. |
| CS-O | T7CSO.DFM | **Commission report color config** — color coding by salesperson class (Class 1/2/3 with different colors); salesperson range filter; "-- ITEM DETAILS --" section (itemized view). |

**Key module facts:**
- Commission HOW (calculation method) and WHEN (payment trigger) are per-salesperson parameters
- Outside agents are linked via AP vendor code — commission appears as an AP payable when due
- BKPR.COMM.* = commission transaction table (links commissions to specific invoices)
- 7 paid-commission period buckets (BKPR.SLS.PAID[1-7]) — tracks commission history per period
- Color-coded commission reports (CS-O) enable at-a-glance salesperson performance view

**Primary tables:** BKPRSALE (salesperson master — confirmed via BKPR.SLS.* field prefix), BKPRCOMM (commission transactions — BKPR.COMM.* prefix)

**Confidence: 70/100** — All 12 DFM files read from network share; full commission workflow confirmed; HOW/WHEN codes and commission transfer logic inaccessible (in RWN).

---

## CM — Contact Manager / CRM

**Confirmed from CHM:**
- **CM-A — Enter Contact Accounts:** Maintains prospect/customer master file with contact history, notes, reminders, class codes, key dates, and ability to convert prospect to AR customer.

**DFM files confirmed:** T7CMA.DFM + 10 more forms (11 total), including ABC classification and conversion forms.

**What it does:** A built-in CRM system. Tracks prospects and customers beyond what BKARCUST stores — contact history, follow-up reminders, lead source tracking, activity notes. The BKCM\* family (46 tables) stores all CRM data.

**Primary tables:** BKCMACCT (contact accounts), BKCMCUST (CRM customer link), BKCMREP (rep assignments), BKCMDUN / BKCMDUNH (dun letters / history), BKCMTERR (territories), BKCMLEAD (lead sources), BKCMMHST (message history), BKCMVNDH / BKCMVNFC / BKCMVNDF (vendor history/follow-up/contacts), BKCMCTL1–4 (control tables), BKCMTEMP (templates).

**T7CMA.DFM (167KB) key fields confirmed from network share:**
- Bridges BKAR.* (AR customer master) with BKCM.* (CRM-specific data)
- Standard AR fields: customer code/name/address/phone/fax/country, salesperson 1 & 2, ship via, terms, discount code, price code, tax group, taxable flag
- CRM-specific: Territory, Lead Source, Start Date, SIC Code, Remarks
- CRM account classes: BKCM.ACCL.CLASS (multiple classes per account)
- Key Dates: BKCM.ACTD.DATE + BKCM.ACTD.DCODE (user-defined date events, e.g. "Next Review", "Contract Expiry")
- Follow-Up reminders: IS.REM.DATE

**T7CMACON.DFM — Contact emails:**
- Up to 9 email addresses per contact: BKCM.ACCN.EMAIL[1-9]
- Email routing: "Include: Ack, PkSlip" — controls which documents auto-route to which email

**T7CMCON.DFM — Contact records:**
- Per-contact: BKCM.ACCN.CODE (contact code), BKCM.ACCN.CON (contact name), BKCM.ACCN.TITLE (position/title), BKCM.ACCN.PRIM (primary contact flag)

**T7CMBB.DFM — CRM mailing list report:**
- Filter by SIC Code, Territory, Zip Code range — generates contact/prospect lists

**Confidence: 65/100** — T7CMA + 4 sub-forms read from network share; contact structure confirmed (9 emails/contact); CRM-AR bridge confirmed; BKCM.* table family confirmed in DDF.

---

## SC — Serial Control ⚠️ NAME CORRECTION

**Previously labeled "Scheduling/Capacity Planning" — INCORRECT. SC = Serial Control.**

This module manages serial number assignment, tracking, and lifecycle for serialized inventory items.

**DFM files confirmed (9 total):** T7SCA.DFM, T7SCB.DFM, T7SCC.DFM, T7SCC2.DFM, T7SCE.DFM, T7SCF.DFM, T7SCG.DFM, T7SCH.DFM, T7SCOMP.DFM

| Code | DFM | What it does |
|------|-----|-------------|
| SC-A | T7SCA.DFM | **Edit Serial Numbers** — view/edit individual serial records. Fields: Serial Number, On-Hand, Date Received, WO#, Exp Date, Location, Cost, SO#, Bin, Invoice#, Customer, Ship Date. Primary table: MTSER. |
| SC-B | T7SCB.DFM | **Assign Serial Control** — configure which inventory items are serial-tracked. Flags: MTIC.PROD.SER (serial flag). Also shows BKIC.PROD.DESC (product description) and BKIC.PROD.NOTE, BKIC.PROD.TYPE. |
| SC-C | T7SCC.DFM | Serial browse/inquiry by item (range filter) |
| SC-C2 | T7SCC2.DFM | **Print Serial Availability** — availability report (includes ISPRT.ZEROS = option to print zero-on-hand serials) |
| SC-E | T7SCE.DFM | **Archive/Unarchive** serial items by item number and serial number range |
| SC-F | T7SCF.DFM | **Serial Control Exceptions** — serials with anomalous state |
| SC-G | T7SCG.DFM | **Serial Number Format Setup** — defines the serial numbering scheme: Item, Item Class, Total Length, Starting Position of Numeric Portion, Last Number Used. Tables: IS.SERC.ITEM, IS.SERC.CLASS, IS.SERC.TOTAL, IS.SERC.SPOS |
| SC-H | T7SCH.DFM | Serial history/inquiry |
| (sub) | T7SCOMP.DFM | **Compound Serial Numbers** — tracks compound/composite serial structures. Tables: IS.SCOMP.DETAIL, IS.SCOMP.COMPND, IS.SCOMP.VIS |

**Primary tables:** MTSER (serial master — one record per serial unit), MTIC.PROD.SER (serial tracking flag on items), IS.SERC.* (serial configuration), IS.SCOMP.* (compound serial definitions)

**Confidence: 72/100** — All 9 DFM files read from network share; purpose confirmed from form captions and field names; MTSER table access pattern confirmed; business logic inferred from labels.

---

## LC — Lot Control

**DFM files confirmed (6 found):** T7LCA.DFM, T7LCB.DFM, T7LCC.DFM, T7LCE.DFM, T7LCF.DFM, T7LCG.DFM
**RWN programs confirmed (7 total):** T7LCA–G all decrypted and analyzed (Pass 316, 2026-06-26)

**What it does:** Lot number tracking for inventory items. Assigns lot numbers at receipt, tracks lot quantities through production and shipment. Structurally identical to SC (Serial Control) but at lot-quantity level rather than individual-unit level.

| Code | DFM | Procs | Source lib | What it does |
|------|-----|------:|-----------|-------------|
| LC-A | T7LCA.DFM | 71 | LISTG60.LIB | **Edit Lot Numbers** — full MTLOT record editor (see MTLOT schema below) |
| LC-B | T7LCB.DFM | 59 | LISTG60.LIB | **Assign Lot Control** — enables/disables lot tracking per item via `MTIC.PROD.LOT` flag; shows BKIC.PROD.* inventory stats |
| LC-C | T7LCC.DFM | 125 | LISTG60.LIB | **Print Lot Allocations** — lot report with `prt.allocs` option; FROM/THRU item+lot+date filter; totals: STD cost, cost, on-hand |
| LC-D | (none) | 5 | t7lcd.SRC | **Stub** — pure launcher (STUB var, 0 tables) |
| LC-E | T7LCE.DFM | 124 | LISTG60.LIB | **Lot Status Report** — item/class/category ranges; `neg.only` (negative qty), `orphans.only`, `excepts.only`, `summ.only` flags; dual RTM (T6+BK era) |
| LC-F | T7LCF.DFM | 95 | EVO.LIB | **Lot Traceability** — item+lot filter; INVTXN+INVATXN history; `rm.fg` (raw/FG toggle); totals: ship/issue/received/adj/accounted/unaccounted |
| LC-G | T7LCG.DFM | 98 | LISTG60.LIB | **Lot Master Listing** — item+lot+expiry+receive date ranges; `zero.uoh.only`; `archive` flag; handles both active (LOT.H) and archived (ALOT.H) lots |

**Pass 316 — MTLOT namespace (23 vars from T7LCA):**

The `MTLOT.*` variable set is the complete access namespace for the MTLOT Btrieve table:

| Variable | Meaning |
|----------|---------|
| `MTLOT.CODE` | Part number (PK with LOT) |
| `MTLOT.KEY` | Btrieve key handle |
| `MTLOT.LOT` | Lot number (PK with CODE) |
| `MTLOT.EXPDATE` | Expiration date |
| `MTLOT.ONHAND` | Current on-hand quantity |
| `MTLOT.PO` | Purchase order number this lot came from |
| `MTLOT.RECDOC` | Receipt document number |
| `MTLOT.VENDOR` | Vendor code |
| `MTLOT.RECDATE` | Receipt date |
| `MTLOT.RECQTY` | Original received quantity |
| `MTLOT.POCOST` | PO unit cost at receipt |
| `MTLOT.WO` | Work order prefix (WO this lot was used in) |
| `MTLOT.INRECDATE` | In-process receipt date (WO receipt) |
| `MTLOT.WOQTY` | WO quantity issued from this lot |
| `MTLOT.WOCOST` | WO cost applied from this lot |
| `MTLOT.NOTES` | Free-text notes |
| `MTLOT.LOC` | Warehouse/bin location |
| `MTLOT.WOSUF` | WO suffix |
| `MTLOT.EXTRA` | Extra / user-defined field |
| `MTLOT.BEGIN` | Beginning balance (lot's opening qty) |
| `MTLOT.OUT` | Total quantity out |
| `MTLOT.MAXOUT` | Maximum quantity allowed out |

**T7LCF — Lot Traceability (Pass 316):**

| Variable | Meaning |
|----------|---------|
| `FROM.ITEM` / `LOT.NO` | Entry filter: part number + lot number |
| `RM.FG` | Toggle: Raw Material vs Finished Goods trace direction |
| `INVTXN.H` / `INVATXN.H` | Inventory transaction + archive transaction handles |
| `WORK.H` / `RECV.H` | WO and receipt handles |
| `CUST.H` / `VEND.H` | Customer + vendor lookup handles |
| `TOT.SHIP` | Total shipped quantity |
| `TOT.ISSUE` | Total issued to WO |
| `TOT.RECD` | Total received |
| `TOT.ADJ` | Total adjusted |
| `TOT.ACC` | Total accounted for |
| `TOT.UNACC` | Total unaccounted (traceability gap) |
| `RTM_NAME` | Runtime-configurable RTM template |

`TOTUNACC` (unaccounted qty) is the key lot traceability metric — a non-zero value means the lot has transactions that don't trace to a customer shipment or WO.

**SC vs LC comparison:**

| Feature | SC (Serial Control) | LC (Lot Control) |
|---------|-------------------|-----------------|
| Granularity | One record per unit | One record per lot (multiple units) |
| Main table | MTSER | MTLOT |
| Item flag | MTIC.PROD.SER | MTIC.PROD.LOT |
| Expiry tracking | MTSER.EXPDATE | MTLOT.EXPDATE + LC-G expiry range filter |
| Archive form | SC-E | LC-G (ARCHIVE flag + ALOT.H handle) |
| Assign form | SC-B | LC-B |
| Traceability | SC history | LC-F (INVTXN+INVATXN+WORK.H+RECV.H) |

**Primary tables:** MTLOT (lot master — 22 fields confirmed), MTICMSTR (item master with MTIC.PROD.LOT flag), BKICMSTR (inventory master), INVTXN/INVATXN (lot transaction history)

**Confidence: 88/100** — Pass 316: all 7 RWN programs analyzed; MTLOT 22-field access namespace fully confirmed from T7LCA vars; T7LCF traceability workflow confirmed (INVTXN+INVATXN+WORK.H+TOT.* counters); T7LCD confirmed as stub; T7LCG archive/ALOT.H pattern confirmed; remaining gap is the exact MTLOT DDF field count (var-extracted, not DDF-confirmed).

---

## QC — Quality Control

**DFM files found on share (4 of ~12):** T7QCA.DFM, T7QCB.DFM, T7QCC.DFM, T7QCD.DFM

The remaining ~8 DFM files are not present on the network share.

**What it does:** Quality control reporting and analysis. Items can be placed on QC hold at receipt (inventory transaction type Q = QC Receipt). QC codes track defect types; scrap codes track disposition/scrap reasons.

**Forms found:**

| Code | DFM | What it does |
|------|-----|-------------|
| QC-A | T7QCA.DFM | **QC/Scrap Report filter** — Date Range, Item Number range, Item Class range, Vendor range, QC/Scrap Code range. Toggle: Use QC Codes vs. Use Scrap Codes. |
| QC-B | T7QCB.DFM | Report filter: Date Range, Parent Item Number range — parent item QC analysis |
| QC-C | T7QCB.DFM | Report filter: Date Range, Parent Item Number range — variant |
| QC-D | T7QCD.DFM | Report filter: Date Range, Parent Item Number range — variant |

**Key finding:** QC module uses two separate defect classification systems — QC Codes and Scrap Codes — selectable per report. Vendor range confirms QC is tied to the receiving/purchasing workflow. Parent Item range in QC-B/C/D enables roll-up of defects by parent assembly.

**Primary tables:** BKQCMSTR (QC master), BKQCTRAN (QC transactions), BKQC (QC receiving record — per T7POJC.DFM analysis)

**Confidence: 52/100** — 4 of ~12 DFM files read from network share; QC/scrap dual-classification confirmed; BKQCMSTR/BKQCTRAN tables confirmed in DDF; test specification and results entry forms not yet found.

---

## SR — Service / Repair

**DFM files confirmed (6 found on share; T7SRA.DFM not present):** T7SRB.DFM, T7SRD.DFM, T7SRE.DFM, T7SRF.DFM, T7SRG.DFM, T7SRK.DFM + T7SRI.DFM (7 total found)

**What it does:** Service/Repair order management for customer-owned equipment. Tracks equipment specs (make, model, serial, motor), service IN/OUT dates, WO linkage, and invoicing.

| Code | DFM | What it does |
|------|-----|-------------|
| SR-B | T7SRB.DFM | **SR order print options** — Print Notes, Print Hidden Notes, PLDTYPE (delivery type) |
| SR-D | T7SRD.DFM | **SR order print options variant** — Print Notes, Hidden Notes, Kit, Comment options |
| SR-E | T7SRE.DFM | **Invoice address edit** — customer address fields from BKAR.INV (city, state, zip, customer PO) for SR order invoicing |
| (shared) | T7SRF.DFM | **Invoice print options** — Caption='SO-F' (shared with SO module); Print Pack Slip, Report Type, Kit, Comment options |
| SR-G | T7SRG.DFM | **SR/Invoice range** — invoice number range, SO number range for SR inquiry |
| SR-I | T7SRI.DFM | **Invoice browse** — date-based AR invoice lookup: Invoice Date, Order Date, Ship Date, Customer Code/Name |
| SR-K | T7SRK.DFM | **Equipment Master (SR Machine Master)** — registers equipment for service. Fields: Item Number, Description, Make, Model, Serial Number, Invoice Number, S/R Number, Line#, IN Date (received for service), OUT Date (returned), Manufacture Date, Motor, WO Number, Category, Comment. Table: ISSR.MMS.* |

**Key module facts:**
- Equipment tracked in ISSR.MMS.* table (IS Service/Repair Machine/Motor Specs)
- Fields "IN Date" and "OUT Date" = when equipment was received/returned from service
- "Motor" field — confirms this handles motor/mechanical equipment service
- SR orders link back to AR invoices (BKAR.INV.*) — SR work is billed through the AR module
- SO integration: T7SOA.DFM has "SR Type" tab and "Print S/R" button — SR orders can originate from a Sales Order
- T7SRA.DFM (SR-A, main entry form) was not found on the network share — may be in the encrypted RWN-only tier or removed

**Primary tables:** ISSR.MMS.* (machine/equipment master for service), BKAR.INV.* (AR invoices for SR billing)

**Confidence: 58/100** — 7 of ~11 DFM files read; equipment master table ISSR.MMS.* confirmed; SR-to-AR invoice integration confirmed; main entry form T7SRA not found; full SR order lifecycle not traced.

---

## WC — Warehouse Control ⚠️ NAME CORRECTION

**Previously labeled "Work Center" — INCORRECT. WC = Warehouse Control (bin/location management).**

This module manages warehouse bin and location master records for inventory placement.

**DFM files confirmed (8 found):** T7WCA.DFM, T7WCB.DFM, T7WCC.DFM, T7WCD.DFM, T7WCE.DFM, T7WCF.DFM, T7WCG.DFM, T7WCH.DFM

| Code | DFM | What it does |
|------|-----|-------------|
| WC-A | T7WCA.DFM | **Bin/Location Master Maintenance** — Add/Edit/Delete bin records. Fields: Location (warehouse), Bin code, Description, Name. Toolbar button: "Duplicates" (check and remove duplicate master bins). Tables: ISBN.MSTR (bin master), bkic.locm (location master). |
| — | T7WCB.DFM | Item/class/category range filter for bin reports |
| WC-C | T7WCC.DFM | **Serial Numbers by Bin** — view serialized inventory at a specific bin location. Uses MTSER.SERIAL, MTSER.ONHAND, MTSER.BIN fields. |
| WC-D | T7WCD.DFM | **Bulk Bin Assignment** — assigns items to bin locations. Options: Skip or Replace existing assignments [S/R], Warehouse (Location), Bin, Default Bin (Y/N), Item Number, Bin Description. |
| WC-E | T7WCE.DFM | Item range/type filter for bin inventory report |
| WC-F | T7WCF.DFM | Item range/type filter for bin inventory report |
| WC-G | T7WCG.DFM | Item range/type filter for bin inventory report |
| WC-H | T7WCH.DFM | **Location browser** — filters by location code; displays bkic.locm.name, location, bin range |

**Note on Work Centers:** WORKCTR (work center master for production routing) is accessed via the WO and SH modules (MTWC.* in SH-B/SH-C). The WC module code here is unrelated to production work centers — it is warehouse/bin control.

**Primary tables:** ISBN.MSTR (IS Bin Number master — bin/location records), BKIC.LOCM (inventory location master), MTSER (serial master — for serial-by-bin view)

**Confidence: 72/100** — All 8 found DFM files read from network share; purpose confirmed from form captions and field names; ISBN.MSTR table identified as bin master; bulk bin assignment workflow confirmed.

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

**DFM files found (4 of ~10):** T7PIA.DFM, T7PIB.DFM, T7PIC.DFM, T7PID.DFM

**What it does:** Periodic physical inventory count cycle — freeze inventory, print tags, enter tag counts, identify missing tags, calculate variances, and post adjustments.

| Code | DFM | What it does |
|------|-----|-------------|
| PI-A | T7PIA.DFM | **Capture Frozen Inventory** — takes an inventory snapshot (freeze). Fields: YEAR, QTR (quarter), FDATE (freeze date), COUNTTYPE1. This is step 1 of the PI cycle. |
| PI-B | T7PIB.DFM | **Frozen Inventory Report** — prints the count sheets for physical counters. Fields: YEAR, QTR, LSYN, PRT.DESC2. |
| PI-C | T7PIC.DFM | **Enter Tag Counts** — data entry for physical count results by tag. Fields: Part Number, Tag Number, Location, UM, Count Qty, Lot Number, Serial Number. Tables: BKPH.TAGNUM, BKPH.LOC, BKPH.EMPNAME, BKPH.CODE, BKPH.LOT (physical tag/count table). |
| PI-D | T7PID.DFM | **Missing Tags Report** — lists tags that have not yet been submitted. Fields: YEAR, QTR, stagnum (starting tag number). |

**PI workflow (confirmed from form captions):**
1. PI-A: Freeze inventory (snapshot all quantities)
2. PI-B: Print frozen inventory report (count sheets)
3. PI-C: Enter tag counts (record actual counts)
4. PI-D: Missing tags report (check completion)
5. (remaining forms): variance calculation, variance report, post adjustments

**Key finding:** "Tags" are physical counting slips attached to inventory. BKPH.TAGNUM = tag-based counting, BKPH.EMPNAME = employee who counted each tag.

**Primary tables:** BKPH.* (physical count/harvest — tag-based count records), BKPI.* (PI master — 7 tables confirmed in DDF)

**Confidence: 62/100** — 4 DFM files read; PI cycle steps 1-4 confirmed; BKPH.* table confirmed; variance calculation and posting forms not yet read.

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

## CH — Chain Management (Program Chaining)

**DFM files confirmed (2 total):** `T7Chain.DFM` (Chain List), `T7CHAINM.DFM` (Chain Master)

**What it does:** Manages the EVO program-chaining system. When a program (e.g., T7SOA Sales Order Entry) completes, it can automatically launch a follow-on program (e.g., T7SOB Invoice Print) with parameters passed between them. The CH module lets users configure per-user chain definitions.

**Forms confirmed from network share (Pass 153, 2026-06-22):**

| Form | DFM | What it does |
|------|-----|-------------|
| Chain List | T7Chain.DFM | Browse existing chain definitions for a user. Grid: IS.CHAIN.USER, IS.CHAIN.DESC, IS.CHAIN.AUTO, IS.CHAIN.PARENT, IS.CHAIN.CHILD. Edit panel: UserName combo, chains combo, Auto entry (1-char, Y/N/A). |
| Chain Master | T7CHAINM.DFM | Full chain definition editor. 9-column grid: Parent, Child, Auto, Description, Param 1–5. Edit panel: Parent combo + Child combo + Auto + Desc + 5 param combos. |

**IS.CHAIN table structure (confirmed from DFM field bindings):**

| Field | Description |
|-------|-------------|
| IS.CHAIN.USER (15) | User name — chain definitions are per-user |
| IS.CHAIN.PARENT (12) | Parent program (trigger — the program that launches the chain) |
| IS.CHAIN.CHILD (12) | Child program (target — the program that is launched) |
| IS.CHAIN.AUTO (1) | Y=auto-launch, N=no chain, A=ask user before launching |
| IS.CHAIN.DESC (100) | Description of the chain rule |
| IS.CHAIN.PARAM[1-5] (15 each) | Up to 5 parameters passed from parent to child |

**Confirmed parent programs (T7CHAINM.DFM combo items):**
T6SOA, T7SOA, T6SOC, T7SOC, T6SOD, T7SOD, T6SOE, T7SOE, T6SOF, T7SOF, T7WOA, \*T6POA, \*T7POA, \*T6POB, \*T6POR, T7ARA, \*T7APA, T7SON, ACHHSSOE

**Confirmed child programs (T7CHAINM.DFM combo items):**
T6SOB, T7SOB, T6SOC, T7SOC, T6SOD, T7SOD, T6SOF, T7SOF, BKSOG, T7SOG, \*BKWOB, \*BKWOD, \*BKWOE, \*BKWOF, \*BKWOG, \*BKWOH, \*BKWOI, \*T6WOC, \*T6WOE, \*T6POB, \*T6POBNP, \*T6POC, T7SOOF, \*T7ARE, \*T7POIG, BKSON, T6ARN, T7SON, T7SOE, T7WOC, T7WOKD

Programs marked `*` in the original combo items may be conditional or legacy.

**DDF cross-reference:** The DDF contains two related tables — ISCHAIN and ISCHAINM (both 17 fields, identical structure). ISCHAIN = active dispatch (user-specific chains in effect), ISCHAINM = chain master/template (the definitions from T7CHAINM). This split explains the two programs: T7CHAINM edits the master, T7CHAIN applies/browses a user's active set.

**Key facts:**
- Auto=A triggers a prompt: "Launch [child program]? Y/N" — user decides at runtime
- PARAM[1-5] carry context from parent to child (e.g., the SO number being processed)
- The chain list in T7Chain is per-user — different users can have different chain behaviors for the same parent program
- LANGDICT access (confirmed from RWN fingerprint) = chain descriptions support multi-language display

**Primary tables:** ISCHAIN (user-level active chains), ISCHAINM (chain master/template definitions)

**Confidence: 82/100** — Both DFM files read from network share; IS.CHAIN field names, AUTO values, and PARAM slots confirmed from field bindings; parent/child program lists confirmed from combo Items.Strings; dual ISCHAIN/ISCHAINM table split confirmed from DDF.

---

## EM — Emergency GL Maintenance

**DFM files confirmed (1 total):** `T7EMGL.DFM`

**What it does:** Direct editor for the BKGL (GL account) table — specifically for emergency maintenance of the `BKGL.EXTRA` field (GL Account Link). Allows adding, deleting, and saving GL account records with account/dept filter.

**Form confirmed from network share (Pass 153, 2026-06-22):**

- Filter inputs: `from.glacct` (GL account, F2 browse, `vld_glacct('A')`), `from.gldpt` (department, `vld_glacct('D')`)
- Grid columns: Account (`BKGL.ACCT`), Dept. (`BKGL.GLDPT`), GL Account Link (`BKGL.EXTRA`)
- Edit field: `bkgl.extra` — a free-form text field on the GL account record
- Toolbar: Add, Delete, Save, Exit
- Handler: `T7EMGL.OnDisp`; uses `T7Gen.OnClose/OnStart/OnOpenFiles`

**BKGL.EXTRA field:** This 50-character field on the GL account record links GL accounts to other accounts or external identifiers. The T7EMGL program is the dedicated tool for maintaining this cross-reference.

**Full DB fingerprint (from RWN Pass 115):** T7EMGL opens 33+ tables including BKGLCOA, BKGLTRAN, BKAPVEND, BKARCUST, BKICMSTR, WORKORD, WOBOM, INVTXN, DBAFIFO, ISTRIGRS, ISREMIND, LOT, SERIAL, ISNCR, **EMERSNGL** — making EM the most privileged maintenance tool in EVO (can touch GL, AP/PO, WO/BOM, inventory transactions, FIFO cost layers, lot/serial records).

**Pass 315 (2026-06-25) — binary string extraction from T7EMGL.RWN.dec:**
- **Program title confirmed:** `"Emerson GL X-Ref"` — displays as "Emerson GL X-Ref" in the window title
- **Filter is a FROM/THRU range:** `FROM.GLACCT` + `THRU.GLACCT` + `FROM.GLDPT` + `THRU.GLDPT` — not just single-account entry as previously thought
- **BKGLCOA namespace confirmed at scale:** BKGL.KEY / BKGL.ACCT / BKGL.GLDPT / BKGL.ACCTD / BKGL.TYPE / BKGL.CR.DR / BKGL.NON.CASH / BKGL.CURRENT / BKGL.BUDGET / BKGL.1YPAST / BKGL.2YPAST / BKGL.EXTRA / BKGL.1YPAST.YE / BKGL.2YPAST.YE / BKGL.ETBCOMBOVAL (14 confirmed)
- **EMERSNGL accessed directly** (the 65-field single-company external COA table — see DDF tier2-tables.md). T7EMGL maps BKGLCOA ↔ EMERSNGL.
- **GLCOA.H** — handle variable for BKGLCOA cursor/position
- **TEMP.GL1 / TEMP.GL2** — working GL account pair during cross-reference operation
- **Source libraries:** EVO.LIB, DBA.LIB, ISTECH.LIB, EVOIM.LIB, LISTG60.LIB
- Standard IS.* multi-currency + ISTS.CFG.* vars present (all modules include these via EVO.LIB)

**Confirmed purpose:** T7EMGL is a GL-to-GL account cross-reference editor. The `BKGL.EXTRA` field maps each EvoERP GL account to a corresponding account code in EMERSNGL (an external or legacy GL chart). This is used for intercompany reporting or GL export to a parent company's GL system. The "Emerson" in the title likely refers to a specific customer/parent-company integration (possibly Emerson Electric — a legacy reference in i2 Systems' customer base).

**Primary tables:** BKGLCOA (GL chart of accounts — ACCT+GLDPT PK, 65 fields including EXTRA), EMERSNGL (external COA, 65f)

**Confidence: 85/100** — T7EMGL.DFM read from network share; BKGL.ACCT/GLDPT/EXTRA field bindings confirmed; full DB fingerprint confirmed; Pass 315 binary string extraction confirmed EMERSNGL access, program title, FROM/THRU range filter, full BKGLCOA namespace.

---

## NE — New Company Init

**DFM files confirmed (1 total):** `T7NEWINIT.DFM`

**What it does:** Utility that checks for missing Btrieve data files and creates them if needed. Used when setting up a new company or after adding new modules.

**Form confirmed from network share (Pass 153, 2026-06-22):**

- Label: "This program will check and see if you are missing any data files and create them if necessary."
- Button: "Go" — runs the file-creation check
- Button: "Exit"
- `fileslabel` (hidden, shows progress during file creation)
- Handler: `T7NEWINIT.OnDisp/OnClose/OnStart/OnOpenFiles`

**Context:** EVO stores each company's data in a separate set of Btrieve `.B` files. When a new company is created via SM (System Maintenance) or when new module tables are added by an upgrade, NE verifies and creates any missing files. It is a one-shot administrative tool.

**Pass 316 (2026-06-26) — T7NEWINIT.RWN.dec binary analysis:**

Program confirmed: `'NEWINIT Create missing Data Files'` (source: EVO.LIB, 49 procs, 1256 vars).

**Variable namespace (key non-TEMP vars):**

| Variable | Purpose |
|----------|---------|
| `LOC_H` | FILELOC table handle |
| `DES_H` | FILEDES table handle |
| `LOC_BUFF_NAME` | FILELOC: buffer/logical name |
| `LOC_FILE_NAME` | FILELOC: physical `.B` filename |
| `LOC_COMP_CODE` | FILELOC: company code suffix |
| `LOC_REC_SIZE` | FILELOC: record size |
| `LOC_REC_TYPE` | FILELOC: record type |
| `LOC_LOCATION` | FILELOC: full network path |
| `LOC_DESCRIPTION` | FILELOC: description |
| `DES_FD_NAME` | FILEDES: file descriptor name (key) |
| `DES_INFORMATION` | FILEDES: file creation spec string |
| `FD_NAME` | Current file descriptor name being processed |
| `FD_EXT` | File extension |
| `FILE_LOC` | Target file location path |
| `CREATE_FILE` | Flag: create this file now |
| `CREATE_SPECS` | Btrieve file creation specification |
| `FILTER_CODE` | Filter: which files to include in the check |
| `FILE_NAME` | Target filename |
| `MCNTR` | Count of files created this run |
| `LOC.REC` | Current FILELOC record pointer |
| `FILE.OK` / `SEC.OK` | File-exists / security validation flags |
| `DBN` / `LFN` | Database name / local filename temps |

**UI strings confirmed from binary:**

| String | Context |
|--------|---------|
| `'Creating   '` | Progress label prefix during file creation |
| `'Created '` | Completion prefix |
| `' missing file(s).'` | Completion suffix: "Created N missing file(s)." |
| `'Error - in initializing file '` | Error prefix |
| `'File descriptor name is blank.'` | Validation error |
| `'The create file name is blank.'` | Validation error |
| `' is not in FILEDES.DBF. It needs to be there before using this program.'` | FD lookup error |

**File descriptor names (FILEDES entries T7NEWINIT knows):**
`CMPDFLT`, `DBAHELP`, `DBALOC`, `DBAMAIM`, `DBAHLPID`, `EVOHLPID`, `DBAMODUL`,
`DBAUSRMN`, `DCBUFFER`, `DEFAULTS`, `ERRMSG`, `MEMORY`, `MENUFILE`, `PRG`,
`RESTFILE`, `TAS`, `TRANSLTE`, `WTASFMGR`, `BKMENUSU`, `BKLUGRID`, `BKUPDATE`,
`BKSLMSTR`, `BKICREQ`, `MONTHEND`, `BKPSUSER`, `BKSLEVEL`, `BKSYUSER`, `MEATTRB`

These are the 28 system-level Btrieve files that NE can create. They are all framework/system
tables (menus, security, user registry, help, DBA dictionaries) — not module-data tables. Module
data tables (BKARINV, BKAPPO, etc.) are created by a different mechanism (EvoUpdate).

**Architecture:**
1. Open FILELOC — iterate every registered file
2. For each entry: look up matching FILEDES record by `LOC_BUFF_NAME` = `DES_FD_NAME`
3. If FILEDES found, attempt Btrieve file open at `LOC_LOCATION` + `LOC_FILE_NAME`
4. If open fails (file missing): use `DES_INFORMATION` spec string to create the file via Btrieve API
5. Increment `MCNTR`; update `filesLabel.caption` with progress

**Primary tables:** FILELOC (file registry), FILEDES (file creation specs)

**Confidence: 88/100** — Pass 316: full var namespace extracted from T7NEWINIT.RWN.dec (49 procs, 1256 vars); all 28 FILEDES file descriptor names confirmed from binary strings; create/check workflow fully reconstructed from variable names + UI strings; FILELOC/FILEDES relationship confirmed; only gap is the exact Btrieve file-create API call syntax (buried in bytecode).

---

## IS-MCC — Multi-Company Currency Conversion

**Program:** `T7ISMCC.RWN` (IS module utility)

**DFM confirmed from network share (Pass 153, 2026-06-22):** `T7ISMCC.DFM`

**What it does:** Converts Source Currency account balances (AP, AR, PORNI, Bank Accounts) to Base Currency, posting any foreign exchange gain or loss to the F/E Gain or Loss GL account.

**Form confirmed:**

- Caption: "Convert Source to Base Currency"
- Description label: "This will convert your Source Currency accounts (AP, AR, PORNI, and Bank Accounts) to Base Currency, with any Gain or Loss posting to the F/E Gain or Loss Account."
- Input: `is.cvt.mth` (GL period 1–12, `vld_glperiod()`)
- Input: `is.date` (conversion date, `vld_gldate()`)
- Read-only display grid showing all 12 GL periods: `gl.period[1-12]` (period numbers) + `ISGL.CYDATE[1-12]` (period start dates)
- Note: period 7 and 8 widget field names are swapped in the DFM (editing artifact)
- Buttons: Process, Exit

**Key facts:**
- Scope: AP, AR, PORNI (Purchase Order Received Not Invoiced), and Bank Accounts
- Gain/loss is posted as a GL entry — not a manual adjustment
- Must specify GL period (1-12) and as-of date — system uses ISGL.CYDATE for period boundaries
- ISGL.CYDATE[1-12] = 12-element array of period beginning dates from the IS GL period table

**Primary tables:** IS.CVT.* (conversion config), ISGL.CYDATE[1-12] (period dates)

**Confidence: 80/100** — T7ISMCC.DFM read from network share; conversion scope confirmed from form label; period/date fields confirmed from field bindings; underlying conversion algorithm in RWN.

---

## ML — Multi-Language Editor

**DFM files confirmed (2 total):** `T7MLC.DFM` (Generator/Editor), `T7MLE.DFM` (Edit Captions)

**What it does:** Developer tools for adding and editing multi-language translations for EVO DFM form captions. The ML module reads DFM files, extracts their captions into the LANG.DICT table, and allows translating those captions to other languages.

**Forms confirmed from network share (Pass 153, 2026-06-22):**

| Form | DFM | What it does |
|------|-----|-------------|
| DFM Multi Language Generator / Editor | T7MLC.DFM | Select a DFM file (T7 combo, F2 browse). Buttons: Edit (open T7MLE to edit captions), Add Lang (show 3-char lang code field), Delete (select language to remove via Langdel combo), Generate (populate LANG.DICT from DFM captions), Exit. |
| Edit Captions | T7MLE.DFM | Select language (Langcombo → `language` field). Grid: LANG.DICT.ECAPT (Default Caption), LANG.DICT.LANG (Lang code), LANG.DICT.LCAPT (Translated Caption). Navigation: First/Prev/List/Next/Last/Back. Detail: `defcapt` (read-only English), `LangCapt` (editable translated). |

**LANG.DICT table structure (confirmed from T7MLE.DFM field bindings):**

| Field | Description |
|-------|-------------|
| ECAPT | English/default caption (the key — used to look up translation) |
| LANG (3-char) | Language code (e.g., "ESP" for Spanish, "FRN" for French) |
| LCAPT | Localized (translated) caption |

**Key facts:**
- Both T7MLC and T7MLE share the same SourceFile (`T7MLC`) — single compiled program handles both screens
- The Generate function reads a DFM's caption strings and inserts them as ECAPT records
- Language addition uses a 3-character code entered in `Alang` field (shown when "Add Lang" is clicked)
- LANGDICT is referenced by many other programs (confirmed in RWN fingerprints) — this is the live translation runtime table
- T7SMK (SM-K User Settings) has a `Language` option (evo.cfg.lang) that selects which LANG code to display at runtime

**Primary tables:** LANG.DICT (ECAPT + LANG + LCAPT — caption translation registry)

**Confidence: 82/100** — Both DFM files read from network share; LANG.DICT table structure confirmed from T7MLE field bindings (ECAPT/LANG/LCAPT); Generate/Edit/AddLang/Delete workflow confirmed; 3-char language code format confirmed.

---

## FN — File Navigator / Reporter

**DFM files confirmed (1 total):** `T7FNR.DFM` (3,223 lines — fully read)

**What it does:** Universal bulk find-and-replace utility for any Btrieve file. An admin/power-user tool that can read any EVO data file, filter records by up to 6 conditions, and replace field values (alpha, numeric, or date) with a flat value, percentage, or substring replacement.

**Form confirmed from network share (Pass 153, 2026-06-22):**

**Section 1 — Target:**
| Field | Purpose |
|-------|---------|
| FILENAME (TTASComboEnter, F2) | Select the Btrieve file to operate on (F2 opens FilePanel — file browser from IS.LOC) |
| DNAME (TTASENTER, F2) | Field name within that file (F2 opens FieldPanel — field browser from IS.DICT) |
| Array # | Element index for array fields |
| Action (TTASComboBox) | Operation to perform (combo, `vld_action()`) |

**Section 2 — Filter conditions (6 rows):**
Each row: `flname[n]` (field, F2→field browser), `felement[n]` (array#), `oper[n]` (operator combo), value (alpha `afind_field[n]` / numeric `nfind_field[n]` / date `dfind_field[n]`)

**Operators:** All, `<>`, `>`, `<`, `>=`, `<=`, `=`, `$` (contains/substring)

**Replacement fields:**
- `AREPL_FIELD` — alpha replacement value
- `Nrepl_field` — numeric replacement value
- `dREPL_FIELD` — date replacement value
- `spos` + `slength` — substring start position and length (for partial alpha replacement)
- Per-filter `POS[1-6]` — position in filter value for `$` (substring match) operator

**Additional controls:**
- "Test Filters" button (`btnTest`) — validate filter conditions without processing
- Progress gauge (hidden during idle)
- PopupMenu on numeric field: "Flat amount" / "Percentage" — two numeric action subtypes

**IS.LOC table (confirmed from FilePanel `filegrid` column bindings):**

| Field | Description |
|-------|-------------|
| LOC_FILE_NAME | Btrieve file name (15-char padded) |
| LOC_BUFF_NAME | Buffer/handle name (internal EVO name for the file) |
| LOC_LOCATION | Full network path to the Btrieve file |

This is EVO's internal file location registry — every Btrieve data file the system knows about is registered here.

**IS.DICT table (confirmed from FieldPanel `fieldGrid` column bindings):**

| Field | Description |
|-------|-------------|
| DICT_FIELD_NAME | Field name within the Btrieve file |
| DICT_TYPE | Field data type |
| DICT_SIZE | Field size (bytes) |
| DICT_DESC | Field description |

This is EVO's internal field data dictionary — distinct from the Pervasive DDF. Used by T7FNR to present human-readable field names and type information to the admin user.

**Key facts:**
- T7FNR is the most powerful direct-data-manipulation tool in EVO — it can modify any field in any file with no module-level validation
- The `vld_action()` call controls which action types appear; the PopupMenu confirms at least "Flat amount" and "Percentage" for numeric fields
- The `$` operator enables substring/contains matching (similar to SQL LIKE)
- spos+slength enable substring replacement (write to a portion of an alpha field)
- IS.LOC is the runtime equivalent of the Pervasive DDF for EVO — it maps logical file names to physical network paths

**Primary tables:** IS.LOC (file location registry), IS.DICT (internal field dictionary), plus any EVO Btrieve file selected by the user

**Confidence: 80/100** — T7FNR.DFM fully read (3,223 lines); all 6 filter rows confirmed; FilePanel (IS.LOC) and FieldPanel (IS.DICT) table structures confirmed from grid column FieldName bindings; PopupMenu action types confirmed; spos/slength substring replacement confirmed; Action combo items not directly visible (vld_action() call — items in RWN).

---

## ES — Estimating

**DFM files found (3 of 7):** T7ESB.DFM, T7ESC.DFM, T7ESD.DFM, T7ESE.DFM (4 found)

**Confirmed from CHM:**
- **ES-A — Enter Estimates:** Creates cost estimates with multiple lines and quantities per line. Pre-sales quoting system. (T7ESA.DFM not found on network share)

**Additional forms read from network share:**

| Code | DFM | What it does |
|------|-----|-------------|
| ES-B | T7ESB.DFM | **Print/options** for estimate — ISPRT.NOTES (print notes), ISPRT.HID.NOTES, PLDTYPE |
| ES-C | T7ESC.DFM | **Range filter** for estimates (SELECT_FROM1/THRU1, ISPRINT.REPT11) |
| ES-D | T7ESD.DFM | **Print Customer Quotes** — filter by quote number range (sFROM.QTNUM, sTHRU.QTNUM) + customer range |
| ES-E | T7ESE.DFM | **Convert Estimates** — converts an estimate to a WO or SO. Fields: SO.NUM, ISTO.WO (convert to Work Order flag), ISTO.SO (convert to Sales Order flag). This is the estimate-to-order handoff. |

**Key finding:** ES-E (Convert Estimates) is the bridge from pre-sales to production. An estimate can be converted directly to a WO (for manufacturing) or to an SO (for sales order entry). This is the "quote-to-order" or "estimate-to-manufacture" workflow trigger.

**Primary tables:** BKES.* (3 tables confirmed in DDF — quote header, lines, and likely status)

**Confidence: 58/100** — 4 DFM files read; ES-E estimate conversion workflow confirmed (ISTO.WO + ISTO.SO); ES-D confirms estimates are customer-facing quotes; BKES.* table structure not yet extracted.

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

**Forms read from network share:**

| DFM | Size | Purpose | Key fields |
|-----|------|---------|------------|
| T7PRA.DFM | 380 KB | Employee W-4 / tax withholding setup | Employee#, W-4 config (Two-job, Dependent deduction, Other income, Additional WH per period), QTD/YTD FIT/FICA/State/SDI/WC → BKPRMSTR (employee master) |
| T7PRB.DFM | 265 KB | Current payroll entry (batch) | Employee array (REC/NAME/NUM/DIV/LPAY/HOURS/GROSS/NET), Check type, Regular/OT/Vacation/Special pay hours+rates, FIT/FUTA/FICA/State/SUTA/SDI/WC deductions, 7 unlimited OD deduction types → BKPRCURP |
| T7PRE.DFM | 41 KB | Direct deposit setup | Employee range (from-emp, thru-emp), terminated employee option → BKPRMSTR direct deposit fields |
| T7PRF.DFM | 158 KB | Federal/state tax withholding tables | Tax code, Description, Amount per allowance, 11 tax bracket tiers (START[1-11], THRU[1-11], AMT[1-11]) → BKPRFTAX (tax table master) |
| T7PRD.DFM | 75 KB | Check printing/processing | — |
| T7PRI.DFM | 44 KB | Employee profile/maintenance | — |
| T7PRK.DFM | 66 KB | Payroll accruals (vacation/sick) | — |
| T7PRM.DFM | 282 KB | Payroll master lists/inquiries | — |
| T7PRO.DFM | 33 KB | Payroll period-end close | — |
| T7PRP.DFM | 79 KB | Payroll period setup | — |
| T7PRQ.DFM | 75 KB | Quarterly reports (941/SUTA) | — |
| T7PRS.DFM | 43 KB | W-2 annual reporting | — |

**Key findings from DFM analysis:**
- **T7PRF is complex**: 11-bracket tax calculation — handles federal, state, local, and custom
  tax calculations in a single table structure; not a simple flat-rate system.
- **T7PRB uses arrays**: Employee entries are array-based (tagged employee list), supporting
  batch payroll entry for multiple employees simultaneously.
- **7 unlimited deduction types** in current pay record — flexible enough to handle unusual
  pre/post-tax deduction structures.
- **QTD/YTD tracking** is embedded in the employee master (BKPRMSTR), not a separate audit table.

**Primary tables:** BKPRMSTR (246+ fields — payroll master), BKPRHIST (127 fields), BKPRW2 (196+ fields), BKPRGLFL (664 fields — GL posting config, SOLVED), BKPRBOOK, BKPRCOMM, BKPRCURP (current payroll), BKPRFTAX (tax tables), BKPRHCOM, BKPRINFO, BKPRSALE, BKPRSTFL, BKPRTC, BKPRTCFG.

**Confidence: 62/100** — Key forms (T7PRA, T7PRB, T7PRF, T7PRE) read from network share; payroll
cycle workflow understood at high level; detailed GL posting logic in BKPRGLFL not fully decoded.

---

## PO — Purchase Orders (additional ops via T7PO\* forms)

**DFM files confirmed:** T7POA.DFM + 39 more forms (40 total)

**Forms read from network share:**

| DFM | Size | Purpose | Key fields |
|-----|------|---------|------------|
| T7POA.DFM | 232 KB | PO header entry (main form) | Vendor code/name/addr, Ship-to (vendor or customer), Description, Terms, FOB, Currency, Location, GL dept, Tax, Order date, Confirmation dates, Ship via, Subtotal/Tax/Total → BKAPPO |
| T7POA (lines) | — | Line item entry (tab within T7POA) | Product/location/job, Line code, Description, Qty, Price, ERD/ARD, UOM, Pct/Discount/Extended, GL account/dept, Long desc, Rev/ECO/Drawing, WO#/Op → BKAPPOL |
| T7POB.DFM | 65 KB | PO printing/report options | PO range, Vendor range, Print all unprinted, Print archive original, Consolidated, ECO/revisions, Make-from, Hidden notes, 2nd desc, Approved vendor, Linked docs, System PO note, Excl zero bal, PO status (ORIGINAL/CURRENT/REWORK), Digital signature, Footer copy lines |
| T7POA2.DFM | 201 KB | PO line extended entry | Product integration, location, job, line number, qty, price, extended, receipt dates → BKAPPOL, BKAPPODTL |
| T7POJC.DFM | 99 KB | PO receiving + QC inspection | Receiver line qty, Buyoff/rejected/use-as-is/scrap qty, Employee, Accepted bin location, Use-as-is bin, QC hold, Defect reason, Sample size, PO line/packing slip/vendor/item refs, WO#, RoHS, NCR flags, Qty in NCR, Mfr part#, Receiver#, RUSH/REWORK/NO WORK flags → BKRECV, BKRECVLN, BKQC |
| T7POH.DFM | 119 KB | Vendor RFQ / price quote management | Vendor, PUM, Lead time, Expiration date, Conversion factor, 5 quantity break levels (QTY[1-5]), 5 costs (COST[1-5]), Min qty/cost, Last changed date/by, Archive original price, Keep price, Archive/purge/restore → BKRFQ |
| T7POM.DFM | 206 KB | PO inquiry (multi-tab analysis) | Vendor code, Item#, PO#, WO#, Job#, Base price, Date ranges; Tabs: PO inquiry / WOs outside process / WOs / POs / Receipts / SO by Customer / On SO and BO |

**Key findings from DFM analysis:**
- **T7POA (232 KB)** is the largest PO form — dual ship-to address (can ship to vendor OR customer
  directly), production integration on lines (WO#, operation, revision, ECO, drawing).
- **5-level vendor price breaks** (T7POH): quantity discount tiers with archiving/versioning — EVO
  tracks price history and supports restoring archived vendor quotes.
- **RoHS and NCR tracking** on received items (T7POJC): compliance-ready receiving workflow with
  Non-Conformance Report linkage.
- **PO status trifecta** (T7POB): ORIGINAL / CURRENT / REWORK — prints of POs carry version context.
- **Receiving spans 4+ forms**: T7POJC (main), T7POIG, T7POIH, T7POII, T7POIL (sub-forms) —
  complex multi-step receiving and inspection workflow.
- **Digital signature support** on printed POs (T7POB: Y/N/Ask).

**Primary tables:** BKAPPO (57 fields — PO header), BKAPPOL (38 fields — PO lines), BKAPRFQ/BKAPRFQL
(RFQ with 5-level pricing), BKAPQUOT (quotes), BKAPHPO/BKAPHPOL (history PO), BKRECV/BKRECVLN
(receiving), BKRFQ (vendor quotes).

**Confidence: 70/100** — Key forms read from network share; PO header and line schemas extracted;
receiving and RFQ workflows traced; detailed BKAPPOL field meaning not fully decoded.

---

## MR — MRP (additional ops via T7MR\* forms)

**DFM files confirmed:** T7MRA.DFM + 18 more forms (19 total)

**Already documented:** Full MRP algorithm traced from BKMRF.SRC. See `docs/03-modules/` for MR source analysis.

**Confidence: 72/100** — Full source analysis done; form count confirmed.

---

## IM — Import Management / Landed Cost

**DFM files confirmed:** T7IMB.DFM, T7IMC.DFM, T7IMD.DFM, T7IME.DFM, T7IMF.DFM (5 total)

**What it does:** Manages currency exchange rates, foreign currency setup, and **landed cost** configuration (duty rates, customs broker fees, freight GL accounts). Used by companies that import goods and need to calculate the true landed cost including duties, freight, and brokerage fees.

**Forms read from network share:**

| DFM | Purpose | Key fields |
|-----|---------|------------|
| T7IMB (140 KB) | Currency Factor Master | ISIS.MCF.CODE (currency code), ISIS.MCF.DESC (description), ISIS.MCF.BASE (base currency flag), ISIS.MCF.SYMBOL (currency symbol) |
| T7IMC | Currency Exchange Rates | ISIS.MCR.DATE (rate date), ISIS.MCR.BASE (base currency), ISIS.MCR.SOURCE[1..n] (source exchange rates by date) |
| T7IMD | Landed Cost GL Accounts | ISIS.LND.GLADT (duty GL account), ISIS.LND.GLDDT (deferred duty GL), ISIS.LND.GLAFR (freight GL), ISIS.LND.GLDFR (deferred freight GL) |
| T7IME | Import Duty Codes | ISIS.DUTY.DCODE (duty code — first 3 chars = vendor), ISIS.DUTY.PERC (duty percentage); Caption: "first 3 characters of Duty Code represent the Vendor" |
| T7IMF | Customs Broker Setup | ISIS.BRK.CODE (broker code), ISIS.BRK.FLAT (flat fee), ISIS.BRK.PERC (percentage), ISIS.BRK.TYPE (broker type) |

**Key findings:**
- **ISIS.* table prefix** — IM uses the ISIS (IS International System?) namespace for all its tables: ISIS.MCF (Multi-Currency Factor), ISIS.MCR (Multi-Currency Rate), ISIS.LND (Landed cost), ISIS.DUTY (Duty codes), ISIS.BRK (Broker). Note: ISIS.TXF and ISIS.TXG (tax codes from SM module) also use this prefix — confirming ISIS is a shared international/compliance namespace.
- **Vendor-specific duty codes** — The first 3 characters of DUTY.DCODE = the vendor code. Duty rates are assigned per vendor, enabling different duty treatment for goods from different suppliers/countries.
- **Landed cost GL separation** — Separate GL accounts for actual vs. deferred duty and freight (GLADT vs. GLDDT; GLAFR vs. GLDFR). Deferred accounts allow cost recognition timing flexibility.
- **Currency exchange rates** (ISIS.MCR.SOURCE[1..n]) — Multiple source rates per date, suggesting EVO can track rates from different providers (bank, spot market, etc.) and select which to use.
- **T7IMB is 140 KB** — the largest IM form. Likely has many currency codes with full master-record editing; the size suggests it handles the complete currency master with extensive field configuration.

**Primary tables:** ISIS.MCF.* (currency factor master), ISIS.MCR.* (exchange rates), ISIS.LND.* (landed cost GL), ISIS.DUTY.* (duty codes), ISIS.BRK.* (broker fees)

**Confidence: 70/100** — All 5 DFMs read; full landed cost and multi-currency setup schema confirmed; actual PO/receiving integration for landed cost not decoded (in RWN).

---

## PS — Program Security / User Access

**DFM files confirmed:** T7PSA.DFM, T7PSE.DFM, T7PSEGRP.DFM, T7PSEITM.DFM, T7PSF.DFM, T7PSK.DFM (6 total)

**What it does:** Manages user accounts, security levels, and per-program access control. Separate from the AHSYLOG system-level access flags — PS provides a program-by-program granular permission system with named security codes.

**Forms read from network share:**

| DFM | Purpose | Key fields |
|-----|---------|------------|
| T7PSA | User Account Setup | BKPS.USER.CODE (user code), seclevel (security level), seccode [A/P/1/2/C/V/U/E] (security code), company (default start company), employee/rep linkage |
| T7PSE | User Security Report | User name From/Thru range — prints per-user security assignments |
| T7PSEGRP | Button Group Config | BUTTON_NUM, BUTTON_NAME — configures named button groups for access control |
| T7PSEITM | Program Access List | PROGRAM_NUM, PROGRAM_DESC, PROGRAM_NME, PROGRAM_SORT — list of programs a user is permitted to access |
| T7PSF | Access-to-Program Report | PROGNAME — print all users who have access to a specific program |
| T7PSK | Approve Vendor | app.vend, from.vend, bkap.vendname — AP vendor approval workflow |

**Key findings:**
- **Security code values [A/P/1/2/C/V/U/E]** — 8 named access tiers. Likely: A=All access, P=Payroll, 1/2=approval levels, C=Cost/View, V=View-only, U=User entry, E=Export. Exact meaning not decoded from DFM alone.
- **BKPS.USER.CODE table** — a dedicated PS user table separate from AHSYLOG (the main system login table). EVO has two user record systems: AHSYLOG (login + 20 module-level flags) and BKPS.* (program-level granular permissions).
- **Program-level access** (PSEITM) — PROGRAM_NUM/PROGRAM_NME means each EVO menu program has an assigned number/name. Users are granted access to specific program numbers — a whitelist model.
- **Employee/Rep linkage** in PSA — users can be linked to a Payroll employee or commission rep, enabling activity tracking by person.
- **T7PSK "Approve Vendor"** — may be a PS-K sub-operation for approving AP vendors as part of a purchasing security workflow (e.g., only PS-authorized users can approve new vendors).

**Primary tables:** BKPS.USER.* (user accounts — code/level/seccode), BKPS.PROG.* or similar (program access list)

**Confidence: 60/100** — All 6 DFMs read; dual user-system architecture confirmed; security code values inferred but not decoded; program-level permission list mechanics not decoded (in RWN).

---

## IC — Inventory Control Utilities

**DFM files confirmed:** T7IC2EST.DFM (1 total)

**What it does:** IC provides utility operations for the Inventory module. T7IC2EST is the only confirmed DFM: it copies production BOM inventory data to the Estimating module.

**Forms read from network share:**

| DFM | Purpose | Key fields |
|-----|---------|------------|
| T7IC2EST | Copy Production → Estimating | Caption='Copy Production to Estimate Inventory'; no bound fields — a simple trigger with Inventory: (target) + Go/Exit buttons |

**Key findings:**
- **IC2EST bridge** — copies the production BOM inventory into the Estimating (ES) module. This populates the estimating module with current item/BOM data so estimate BOMs can start from production reality rather than from scratch.
- **One-way copy** — "Copy Production to Estimate" is directional (production → estimate, not the reverse).
- **Single DFM** suggests IC may be a small module with primarily RWN-implemented operations.

**Primary tables:** BKICMSTR (inventory master — source), IS.EST.* or similar (estimating inventory — target)

**Confidence: 35/100** — 1 DFM read; IC2EST bridge purpose confirmed from caption; IC module's broader scope (other IC menu ops) not decoded.

---

## SD — Standard Data

**DFM files confirmed:** T7SDET.DFM (1 total)

**What it does:** SD stores standard code/detail records — a generic lookup/reference table (IS.SDET.*) used across modules for standardized entries.

**Forms read from network share:**

| DFM | Purpose | Key fields |
|-----|---------|------------|
| T7SDET | Standard Detail Entry | IS.SDET.DETAIL (detail text), IS.SDET.TYPE (type code) — a type-keyed detail lookup |

**Key findings:**
- **IS.SDET.* table** — stores standard detail strings, keyed by type. Similar in concept to reason codes — a module-agnostic code/description lookup. SD-ET = "Standard Data - Edit Type" or "SD Entry".
- **12 menu operations** suggests SD has significant breadth beyond this one DFM — most operations are in RWN.

**Primary tables:** IS.SDET.* (standard detail records — type + detail text)

**Confidence: 30/100** — 1 DFM read; IS.SDET.* table confirmed; module full scope not decoded.

---

## QT — Quoting / Service Quote Misc.

**DFM files confirmed:** T7QTINFO.DFM (1 total)

**What it does:** QT handles quote-related operations. T7QTINFO specifically stores miscellaneous date information for Service/Repair (SR) quotes, using the ISSR.INFO.* table.

**Forms read from network share:**

| DFM | Purpose | Key fields |
|-----|---------|------------|
| T7QTinfo | Quote Misc. Information | ISSR.INFO.DATE[1..5] (indexed date fields for SR/service quote); Caption='Quote Misc. Information' |

**Key findings:**
- **ISSR.INFO.* = Service/Repair info table** — the ISSR prefix belongs to the SR (Service/Repair) module. QT operates on SR data. This suggests QT is a quoting sub-module for the SR module (customer quotes for service/repair work), not a standalone general quoting module.
- **Multiple indexed dates** (DATE[1]/[2]/[3]/[5]) — a service quote tracks several dates (quote date, promised date, ship date, completion date, etc.).

**Primary tables:** ISSR.INFO.* (service/repair quote info)

**Confidence: 35/100** — 1 DFM read; service quote linkage confirmed; full QT module scope and remaining date field meanings not decoded.

---

## RF — Request for Quote (RFQ from Estimating)

**DFM files confirmed:** T7RFQ.DFM (1 total)

**What it does:** RF generates Request for Quote documents from Estimating data — linking estimate numbers to vendor RFQs.

**Forms read from network share:**

| DFM | Purpose | Key fields |
|-----|---------|------------|
| T7RFQ | RFQ from Estimate | aenum (estimate number), is.est.orddesc (estimate order description), LIST.PART/LIST.DESC — tag individual items or groups; Process button |

**Key findings:**
- **"aenum" = estimate number** — RF pulls from the ES (Estimating) module's data. An estimate generates one or more RFQs to vendors for components.
- **Tag Individual / Tag Groups** — allows selective RFQ generation: tag specific parts individually or tag a group of parts.
- **is.est.orddesc** = IS Estimating order description — RF accesses IS.EST.* tables.

**Primary tables:** IS.EST.* (estimating — source), BKAPRFQ/BKAPRFQL (vendor RFQ — destination, also used by PO module)

**Confidence: 40/100** — 1 DFM read; ES→RFQ link confirmed; full RF workflow not decoded.

---

## US — User Services / Trigger Notifications

**DFM files confirmed:** T7USG.DFM (1 total)

**What it does:** US manages the trigger-based notification system — automated follow-up alerts that fire when certain conditions are met (days before a date, CRM key dates, etc.).

**Forms read from network share:**

| DFM | Purpose | Key fields |
|-----|---------|------------|
| T7USG | Trigger/Notification Setup | IS.TRIG.NOTE (trigger note text), IS.TRIG.CONTACT (contact to notify), IS.TRIG.EMAIL (email address), IS.TRIG.EFLAG (email flag); Caption fields: "Trigger Code / User to Trigger / Last Date / Last Time / Days Pre" |

**Key findings:**
- **IS.TRIG.* table** — trigger records define: Trigger Code, which User to notify, the Last triggered Date/Time (audit), and Days Pre (how many days before an event to fire).
- **IS.TRIG.CONTACT + IS.TRIG.EMAIL** — triggers can notify a specific contact person by email. EFLAG = whether to send email vs. in-app notification.
- **"Days Pre"** — the trigger fires N days before a reference date (likely from CRM key dates BKCM.ACTD.* or SR service due dates).
- **Linkage to CRM/SR** — IS.TRIG contacts and email addresses suggest triggers are CRM-driven: follow up with a contact X days before their contract renewal, service due date, etc.

**Primary tables:** IS.TRIG.* (trigger records — code/contact/email/days)

**Confidence: 45/100** — 1 DFM read; trigger notification mechanism confirmed; full trigger type taxonomy and integration points not decoded.

---

## DE — Data Entry / EDI / Imports (20 forms)

**DFM files confirmed:** T7DEER.DFM, T7DEFECT.DFM, T7DEHD.DFM, T7DEJH.DFM, T7DEK.DFM, T7DEL.DFM, T7DEM.DFM, T7DEP860.DFM, T7DEPB.DFM, T7DEPD.DFM, T7DEPE.DFM, T7DEPF.DFM, T7DEPH.DFM, T7DEQ.DFM, T7DER.DFM, T7DET.DFM, T7DETB.DFM, T7DEU.DFM, T7DEV.DFM, T7DEX.DFM (20 total)

**What it does:** The EvoERP integration gateway — handles all data imports, data exports, EDI (Electronic Data Interchange) transactions, and bulk data manipulation. Covers BOM import, PI tag import, WO material import, web order import, vendor POA acknowledgments, customer release/blanket POs, and web item catalog export. Also contains two dangerous admin utilities (global field replace, selective file erase).

**Forms by function:**

| DFM | Caption / Purpose | Key fields |
|-----|-------------------|------------|
| T7DEM | BOM Component Import | Import BOM components (to Estimating or Production); allow 0 qty; print errors flag |
| T7DEER | BOM Import Validation | DE-ER Error Report — print errors only, item range, validate against Estimating vs Production |
| T7DEHD | PI Tag Import | Caption='PI-C Import Tags'; Skip/Replace existing tags; Count Date/Tag#/Location/Qty/Item# via FIELD.NUMBER[n] mapping |
| T7DEJH | WO Material Import | DE-J-H; WOMAT.WOPRE/WOSUF/PCODE/PDESC — imports WO component/material lines |
| T7DEQ | AR Invoice Import | file.name, comma.fixed [C/F], replace [S/R], field.number[1] — imports AR invoices from CSV |
| T7DER | Data Import (variant) | Same structure as DEQ — likely a different record type (customer or vendor import) |
| T7DET | Web Order Import (header) | Caption='Web Import'; Rec Designator H=header; auto.mode, use.imp.sonum, import.to.edi, bank.name — web orders can route to EDI or direct SO |
| T7DETB | Web Order Import (alt) | DE-T-B; import.to.edi, date.format, incl.2nd.desc — web import configuration variant |
| T7DEV | Vendor POA Import | Caption='POA Import'; SKIP.PONUM/PCODE/PQTY/SKIP.MSG — imports EDI 855 Purchase Order Acknowledgments from vendors |
| T7DEPB | Customer Release Import | DE-P-B; BKAR.INV.CUSCOD, RELEASE_NUM, BKAR.INV.CUSORD — blanket PO release schedules |
| T7DEP860 | EDI-860 PO Change | Same form as DEPB but EDI-860 transaction context — processes inbound PO change requests |
| T7DEPD | Release Processing | DE-P-D; KEEP.ORD (keep order flag), KEEP.QUOTE, LOC, EST.DATE — processes release records |
| T7DEPE | Release Browse | DE-P-E; BKAR.INV.CUSCOD/NUM/SONUM — browse/filter customer releases by SO/invoice |
| T7DEPH | Release Packing | DE-P-H; sFROM.SONUM/sTHRU.SONUM, stdpck (standard packing flag) |
| T7DEU | Web Item Export | Caption='Web Item Export'; ftp.FileName, from.item/thru.item — FTP upload of item catalog |
| T7DEX | Data Dictionary Export | MEM.SELECT.FLD/NUM, MEM.DICT_DESC, MEM_DICT_NAME — exports TAS memory/dictionary definitions |
| T7DEFECT | Defect Code Setup | IS.DEF.CODE, IS.DEF.DESC — master list of defect codes (used by QC and SPC modules) |
| T7DEK | Global Field Replace ⚠️ | "File / Field to Change / Replace all Values / Value to search for" — find-and-replace across any EVO data file (which.file, which.field, replace.all, search.for) |
| T7DEL | Selective File Erase ⚠️ | Erase Inventory, BOM, Customer, Routings files — inv/bom/cust/rout flags; destructive bulk delete |

**Key findings:**
- **EDI-860 PO Changes** (T7DEP860) — EvoERP handles inbound customer EDI 860 PO change requests. RELEASE_NUM field suggests blanket PO / release schedule EDI (common in automotive/electronics supply chains).
- **Web Order Import** (T7DET) — `import.to.edi` flag means web orders can be staged in EDI before committing to SO. `bank.name` field confirms web orders include payment/banking info.
- **Vendor POA (855)** (T7DEV) — SKIP flags allow selective import: skip by PO#, product code, qty, or message. Used to process vendor acknowledgments against outstanding POs.
- **FTP Item Export** (T7DEU) — direct FTP upload of item catalog. Web integration is bidirectional: orders in (T7DET), catalog out (T7DEU).
- **Global Field Replace** (T7DEK) — find-and-replace across any data file and field. Extremely powerful for data cleanup, but one wrong entry corrupts the database. No undo.
- **Selective File Erase** (T7DEL) — bulk-delete by module (inventory/BOM/customers/routings). Used for database initialization from a template. No undo.
- **Defect Code master** (T7DEFECT) — IS.DEF.CODE/DESC shared across QC and SPC modules. DE is also the home for setup tables that serve multiple modules.

**Primary tables:** WOMAT.* (WO materials), IS.DEF.* (defect codes), IS.RMA.* (partial — RMA codes via DE?), BKAR.INV.*/BKAR.INVL.* (AR invoice import target), BKAR.DEP.* (deposits linked to releases)

**Confidence: 68/100** — All 20 DFMs read; import targets and EDI transaction types confirmed; EDI 860/855 flows identified; exact DE-P sub-forms (DEPF, DEPG, etc.) not all read; web order bank integration not fully decoded.

---

## RM — Return Material Authorization (RMA)

**DFM files confirmed:** T7RMAWHY.DFM, T7RMD.DFM, T7RMDASK.DFM, T7RME.DFM, T7RMG.DFM (5 total)

**What it does:** Manages customer Return Material Authorizations — creating an RMA number against an original invoice/SO, recording the reason and warranty status, and processing the return disposition (restock, replace, credit, or transfer to a WO job).

**Forms read from network share:**

| DFM | Purpose | Key fields |
|-----|---------|------------|
| T7RMD | RMA Entry (main — 156 KB) | Item#, Original Inv Num (bkar.inv.*), Original SO Num, Warranty [NLPB], Reason for Return (is.rma.warranty, warranty.desc, bkar.invl.pcode/pdesc) |
| T7RMAWHY | RMA Detail / Why Popup | RMA Number, Line#, Status (is.rma.status), Item, Desc; SO # and line UOM reference |
| T7RMDASK | RMA Disposition | Change Location, Pass RMA# to Desc/Job/None [D/J/N] (pass.rma.num), Location, Restock Charge (restock.charge), Enter SO Number |
| T7RME | RMA Reason Code Setup | IS.RMA.CODE, IS.RMA.DESC — master list of return reason codes |
| T7RMG | RMA Report | from.cust/thru.cust, thru.item — customer/item range RMA report |

**Key findings:**
- **Warranty codes [NLPB]** — N=Not covered, L=Limited, P=Parts only, B=Both (parts & labor). Warranty status drives what credit or replacement is issued.
- **IS.RMA.* table** — dedicated RMA records table with status (is.rma.status), warranty (is.rma.warranty), and reason code (IS.RMA.CODE).
- **Disposition routing** (T7RMDASK) — "Pass RMA# to Desc/Job/None [D/J/N]" means returned items can be routed to: a Job (WO) for rework, the invoice Description field for tracking, or neither. This bridges RM → WO for repair jobs.
- **Restock charge** — T7RMDASK's restock.charge field confirms EVO supports restocking fees on customer returns.
- **Original invoice linkage** — T7RMD references both bkar.inv.* (invoice header) and bkar.invl.* (invoice line) — RMAs are created at the line level, not just header.

**Primary tables:** IS.RMA.* (RMA records — status/warranty/code), BKAR.INV.* (original invoice), BKAR.INVL.* (invoice line), IS.RMA.CODE/DESC (reason codes)

**Confidence: 68/100** — All 5 DFMs read; RMA workflow from entry to disposition traced; IS.RMA.* table confirmed; full field schema not decoded; warranty code exact values inferred from pattern.

---

## FO — Features & Options

**DFM files confirmed:** T7FOC.DFM, T7FOD.DFM, T7FOE.DFM (3 total)

**What it does:** Product configurator add-on to the BOM module. Allows manufactured products to have selectable features and options — each option sets a Y/N flag (BKBM.PROD.OPYN[1..N]) on the BOM item. Customer orders for configurable products activate specific options, which drives which BOM components are included.

**Forms read from network share:**

| DFM | Purpose | Key fields |
|-----|---------|------------|
| T7FOC | FO-C Option Pricing Editor | Feature item (from.item=Feature, PAR.DESC=feature description), Option item (thru.item=Option, COMP.DESC=option description), BKBM.PROD.OPYN[4]="Use STD Customer Pricing?", BKBM.PROD.OPYN[5]="Add Price to Parent?", BKBM.PROD.PRICE (DisplayFormat='$,0.0000') |
| T7FOD | FO-D Range Report Filter | from.item/thru.item (item range), from.cat/thru.cat (category range), from.class/thru.class (class range) → Print button |
| T7FOE | FO-E Single Item Filter | "Feature / Option Item Number" — from.item → Print button |

**Key findings:**
- **T7FOC field naming quirk** — `from.item` = the Feature (parent) item number; `thru.item` = the Option (component) item number. These are NOT a from/thru range — they identify one Feature-Option pair whose pricing is being edited. The `thru` naming is a TAS Pro naming convention reuse.
- **BKBM.PROD.OPYN[4/5] confirmed semantics** — OPYN[4]="Use STD Customer Pricing?" (when Y, option price uses the standard customer price schedule instead of the fixed PRICE field); OPYN[5]="Add Price to Parent?" (when Y, option price is added to the parent feature item's price on the SO line).
- **BKBM.PROD.PRICE** — The per-option fixed price, format $,0.0000 (4 decimal places). Only used when OPYN[4]=N (not using STD customer pricing).
- **BKBM.PROD.OPYN array** — At least indices 1–6 confirmed from BKBMMSTR DDF (PROD_OPYN_1..6). T7FOC uses indices 4 and 5; the other slots are available for additional configurator flags.
- **PAR.DESC / COMP.DESC** — Read-only description display fields. PAR=parent feature description, COMP=component option description. Populated from the item master (BKICMSTR) when the feature/option item numbers are entered.
- **T7FOD and T7FOE are print filter forms** — both have Print/Exit buttons (not Save). They drive the FP-B "Print Features and Options" report through item and category/class range selections.

**Primary tables:** BKBM.* (BOM — BKBM.PROD.OPYN[1..6] flags + BKBM.PROD.PRICE), BKICMSTR (item master), ISFOHEAD (FO order header), ISFOLINE (FO config lines), ISFOORDL (output order lines)

**Confidence: 65/100** — T7FOC DFM fully read; OPYN[4/5] exact semantics confirmed from DFM labels; pricing logic confirmed; full configurator workflow (SO trigger → option selection → ISFOHEAD/ISFOLINE lifecycle) requires RWN bytecode analysis.

---

## IS — Information System / Multi-Currency GL

**DFM files confirmed:** T7ISMCC.DFM (1 total on network share)

**What it does:** "IS" is the generic prefix for shared system tables across EvoERP (IS.CC, IS.RMA, IS.FXA, IS.SERR, IS.TERMS, IS.ACTION, etc.). The IS menu module itself provides multi-currency GL conversion and possibly other GL/integration utilities.

**Forms read from network share:**

| DFM | Purpose | Key fields |
|-----|---------|------------|
| T7ISMCC | Convert Source to Base Currency | is.date (conversion date), ISGL.CYDATE[1] (GL currency date), gl.period[1], gl.period[2] — converts foreign currency GL entries to base currency for a specific period |

**Key findings:**
- **IS.MCC = Multi-Currency Conversion** — converts foreign-currency GL amounts to the base (functional) currency. Triggered at period-end for consolidated reporting.
- **ISGL.* table prefix** — ISGL = IS GL integration. The GL module accesses ISGL.* tables for currency-aware period amounts.
- **"IS" table prefix breadth** — IS.* tables are used by at least 10 modules: CC (credit cards), RMA (returns), FXA/FXT (fixed assets), SERR (SPC errors), TERMS (payment terms), JOB (job master), CYCLE (maintenance), ACTION (action types), DEF (defect codes), SCOMP (compound serials). IS is the system-wide shared reference data namespace.

**Primary tables:** ISGL.* (GL currency integration), IS.* (shared reference tables across all modules)

**Confidence: 45/100** — Only 1 DFM found; IS module full menu scope unknown; ISGL currency conversion mechanism confirmed from DFM; broader IS module contents inaccessible without RWN decryption.

---

## HH — Handheld / Shop-Floor Data Collection (44 forms)

**DFM files confirmed:** T7HH.DFM + 43 sub-forms = 44 total

**What it does:** Provides a compact, scanner-friendly interface for all major ERP functions from handheld terminals and shop-floor kiosks. Mirrors the full desktop ERP workflow but optimized for barcode scan entry — minimal keystrokes, large text, optional Large Screen Lookups mode.

**Sub-module breakdown by function area:**

| Sub-area | Forms | Purpose |
|----------|-------|---------|
| PO Receiving | t7hhpoc, T7HHPOCBIN, T7HHPOCLot, T7HHPOCNotes, T7HHPOCSER | Receive POs via scanner; assign to bin/lot/serial; notes; vendor/item alerts |
| WO Operations | t7hhwog, t7hhwop, T7HHWOSCRAP, T7HHWOLabel, T7HHWOLOT, t7hhwoser, T7HHWOLookup, T7HHWOIProcess, T7HHWOIBIN | Issue materials to WO, finish production, report scrap, print WO labels, lot/serial entry on WO |
| SO Picking/Shipping | T7HHSSOE, t7hhssoeLabels, t7hhssoeLverify, T7HHSSOEVerify, T7HHSSOESVerify, T7HHSOBIN, T7HHSOLOT, T7HHSOSER, T7HHSOLookup, T7HHSODD | Pick SO lines, scan-pack into boxes (curr.boxnum), print packing slips, shipping confirmation |
| Inventory | T7HHItemLU, t7hhINGA, t7hhinlj, T7HHINLJLot, T7HHINLJSer, t7hhinbins | Item lookup (with substitutes MTIC.PROD.SUBST[1]), bin transfer (from.loc/to.loc) with lot/serial, print inventory labels |
| DC / Labor | T7HHDCA, t7hhdcb, t7hhdcc | Operation scanning — clock-in/clock-out at work center (scan.wo, scan.emp, OPER) |
| Physical Inventory | T7HHPIC, t7hhpictags | PI-C tag count entry from handheld — CountDate, qtr, year, location, countqty, lotno, serialno |
| Notifications | T7HHALERTMSG | Vendor/item alert messages shown during receiving (Enable Vendor Alerts, Enable Item Alerts) |
| Navigation | T7HH, T7HHProcess | Main HH menu; PROCESS DATA — batch-process collected scan data |
| Filters/Config | T7HHN, T7HHNREL, T7HHN2, T7HHNDTE | HH-N SO picking filters — credit hold, released, backorder, kit components, date limits, item type codes (RFAMNLBTKO) |

**Key DFM findings:**

| DFM | Purpose | Key fields |
|-----|---------|------------|
| t7hhpoc | Receive PO (main) | vendor.alerts, item.alerts, large.lookups, RCVD_QTY, item — scan item to receive |
| T7HHSSOE | Shipping (pack) | scan.qty.char, scan.item, curr.boxnum, print.ps — box-level packing |
| t7hhwog | Issue Material to WO | RTM_NAME, prt.per.comp, Label.qty, showPrtBox — print component labels on issue |
| t7hhwop | Finish Production | final.qty.dflt, prompt.date, wo.status (FRXI filter), large.lookups — WO completion scan |
| T7HHDCA | DC / Operation Scan | scan.wo, scan.emp, OPER — time-card scan at work center |
| T7HHN | SO Picking filter | incl.crhold, incl.released, incl.zero.dates, limit.days, limit.date — controls what SOs appear in pick list |
| T7HHItemLU | Item Lookup | MTIC.PROD.SUBST[1], MTIC.PROD.DESC — finds substitutes during pick |
| t7hhinlj | Transfer Inventory | from.loc, to.loc, from.dflt.bin — bin-to-bin transfer |
| T7HHINLJLot/Ser | Transfer w/ lot/serial | lot.qty, mtlot.onhand, inp.lot; ser.qty, inp.ser |
| T7HHPIC | PI Tag Count (HH) | CountDate, qtr, year, location — links to PI-C desktop workflow |
| t7hhpictags | PI Tag Count detail | countqty, lotno, serialno — scan lots and serials into count tag |
| T7HHWOLabel | WO Label config | sfrom.oper.fin/sthru.oper.fin (operation finish sequence), fin.class (finished item class), nfin.class (semi-finished class) |
| T7HHWOSCRAP | Report Scrap | RTM_NAME, prt.labels — scrap reporting with label printing |
| t7hhwoser | Serial # on WO | scrap.code, inp.serial, filter.by.loc — serial entry for WO completion or scrap |
| T7HHSOLookup | SO Lookup | BKAR.INV.SONUM, BKAR.INV.CUSCOD, BKAR.INV.CUSNME — SO search in HH |
| T7HHProcess | Batch Process | "PROCESS DATA" — uploads collected offline HH scans to the live database |

**Key findings:**
- **Large Screen Lookups mode** (large.lookups) — all major HH forms have this flag, suggesting a dual UI mode: small-screen handheld vs. large touch-screen kiosk.
- **Item type filter** [RFAMNLBTKO] in HH-N — same type codes used in inventory module: R=Raw, F=Finished, A=Assembly, M=Manufactured, N=Non-stock, L=Labor, B=Bought, T=Tool, K=Kit, O=Other.
- **Lot + serial tracking at every touchpoint** — every function that moves material (issue, receive, transfer, ship) has dedicated Lot and Serial variants. Lot/serial control is end-to-end.
- **Scrap reporting with labels** — T7HHWOSCRAP prints RTM-format labels directly at scrap time, supporting barcode-driven audit trails.
- **5-form shipping workflow**: SSOE (scan pack) → ssoeLabels → ssoeLverify → SSOEVerify → SSOESVerify — staged verification before release.
- **HH-N picking filter** includes credit hold filter (incl.crhold) — HH terminal enforces credit-hold logic at pick time.

**Primary tables:** BKAR.INV.* (SO data), BKWOMSTR/BKWODTL (WO), BKAPPOL/BKRECV (PO receiving), MTLOT.* (lots), MTSER.* (serials), ISBN.MSTR (bins), BKPH.* (physical count tags)

**Confidence: 68/100** — 20 of 44 DFMs read directly; function areas identified from captions and field names; exact table join keys and network/offline sync mechanism not decoded.

---

## UT — Utilities (Admin/Data Maintenance)

**DFM files confirmed:** T7UTH.DFM, t7uti.DFM, T7UTKA.DFM, T7UTKD.DFM, T7UTKE.DFM, T7UTKF.DFM, T7UTKG.DFM, T7UTKH.DFM (8 total)

**What it does:** Administrative utilities for EvoERP system maintenance — adding/removing companies, clearing/resetting data, configuring fiscal years, cleaning up unused records, and recalculating inventory costs. **Most operations are irreversible — intended for system administrators only.**

**Forms read from network share:**

| DFM | Purpose | Key fields | Warning |
|-----|---------|------------|---------|
| T7UTH | File Layout Report | from.file, thru.file, LOC_BUFF_NAME, LOC_FILE_NAME — prints schema of EVO data files by name range | Low |
| t7uti | Company Add/Delete | company_code, company_name, company_path, copy.file, cdelete — multi-company management | **High** |
| T7UTKA | Data Clear / Reset | CLR.COA, CLR.CUST, CLR.VEND, CLR.INVN — delete ALL data or transactions only per module; includes GL + BKSYMSTR | **Destructive** |
| T7UTKD | Fiscal Year Setup | fycur, fy1yp, fy2yp, fy3yp, fy4yp — configure up to 4 historical fiscal years + current | Medium |
| T7UTKE | Location Cleanup | new.code, LOCATION — deletes unused warehouse locations; Caption: "not reversable... may take a long time" | **Destructive** |
| T7UTKF | Item Utility F | from.item, thru.item, from.class — item/class range rebuild (variant F) | Medium |
| T7UTKG | Item Utility G | from.item, thru.item, from.class — item/class range rebuild (variant G) | Medium |
| T7UTKH | Average Cost Recalculate | inc.type[1-4] (by inventory type), from.item, thru.item — Caption: "recalculate Average Cost in inventory records" | Medium |

**Key findings:**
- **Multi-company management** (t7uti) — Add a new company by specifying code, name, and path. copy.file suggests initialization by copying an existing company's file structure. cdelete flag handles deletion.
- **Data clear (T7UTKA)** — most dangerous utility: selective module-by-module data wipe. CLR.COA/CLR.CUST/CLR.VEND/CLR.INVN are separate flags. Used to clone a company template, then clear test data before go-live.
- **Fiscal year (T7UTKD)** — supports 4 historical years + current = 5 total. Critical for GL period-end processing.
- **Location cleanup (T7UTKE)** — removes all unused bin/location codes. The "new master location code" field reassigns orphaned inventory to a default bin.
- **Average cost recalculate (T7UTKH)** — separated by inventory item types (inc.type[1-4]). Needed after physical inventory adjustments or initial data load.
- **UT-K-F and UT-K-G** — two item-range utilities with identical field structure (item/class range); likely handle different phases of an item rebuild (exact distinction unconfirmed).

**Primary tables:** BKSYMSTR (company settings), BKARCUST/BKAPVEND/BKICMSTR (cleared by UTKA), BKIC.LOCM/ISBN.MSTR (location cleanup), BKICOST/BKICMSTR (average cost)

**Confidence: 60/100** — All 8 DFMs read; destructive operations documented; fiscal year and average cost recalc confirmed; UT-K-F/G exact purpose not confirmed.

---

## SA — Sales Analysis

**DFM files confirmed:** T7SAA.DFM, T7SAM.DFM, T7SAN.DFM, T7SAO.DFM, T7SAP.DFM, T7SAQ.DFM (6 total)

**Forms read from network share:**

| DFM | Purpose | Key fields |
|-----|---------|------------|
| T7SAA.DFM | Currency analysis filter | from_cur, thru_cur, inc.change (include change flag) |
| T7SAM.DFM | Salesperson/rep filter | BKSA.NAME, BKSA.TITLE, BASE |
| T7SAN.DFM | Salesperson/rep filter (alt view) | BKSA.NAME, BKSA.TITLE, BASE |
| T7SAO.DFM | Top N Sales Report | Caption='Top N Sales Report'; customer range, date range |
| T7SAP.DFM | Class/category analysis | from.class, thru.class, from.cat, thru.cat |
| T7SAQ.DFM | Actual Margin Report | Caption='Actual Margin Report'; from.shipdt, thru.shipdt, thru.afin (actual finish date) |

**Key findings:**
- **Dedicated BKSA.* table** — SA is not just a query on BKARINV. It has its own aggregation table (`BKSA.NAME`, `BKSA.TITLE`, `BASE`) that stores pre-computed or summarized sales data. This is significant: SA results are persisted, not calculated on the fly.
- **Multi-currency support** — SA-A filters by currency pair with an "include change" option. Multi-currency analysis is built in.
- **Salesperson analysis** (SA-M/N) — BKSA records have a NAME and TITLE, suggesting this table stores salesperson performance summaries.
- **Top N Sales** (SA-O) — classic "who are our top N customers" report with customer/date range.
- **Actual Margin** (SA-Q) — uses `thru.afin` (actual finish date), tying margin calculations to WO completion dates, not just ship dates. Confirms SA integrates with WO module for job cost margin.
- **Class/Category analysis** (SA-P) — analyze sales performance by product class and category.

**Primary tables:** BKSA.* (sales analysis summary), BKARINV (AR invoices — range source), BKARCUST (customer)

**Confidence: 55/100** — All 6 DFMs read; form purposes clear; BKSA.* table existence confirmed but field schema not decoded; exact aggregation trigger (post-invoice? batch?) unknown.

---

## AC — Activity Control (WO Actual Dates)

**DFM files confirmed:** T7ACDATE.DFM, T7ACRDTYPE.DFM, T7ACTION.DFM (3 total)

**Forms read from network share:**

| DFM | Purpose | Key fields |
|-----|---------|------------|
| T7ACDATE.DFM | WO actual start/finish date entry | WODATE.START, WODATE.FINISH, WODATE.QTY, parent.wonum, top.wonum, deleted.wonum |
| T7ACRDTYPE.DFM | Action/record disposition type codes | ac.rd.reason, ac.rd.type, ac.rd.dispo, AC.RD.TYPE, AC.RD.REASON |
| T7ACTION.DFM | Action type master | IS.ACTION.TYPE, IS.ACTION.DESC |

**Key findings:**
- **WO hierarchy tracking** — T7ACDATE stores parent.wonum and top.wonum alongside the entry WO. EVO supports multi-level WO trees (sub-WOs rolled up to top-level); AC records actual dates at each node.
- **deleted.wonum** — a "deleted WO" reference in the date entry form suggests AC also handles cleanup/voidance of WO activity records.
- **WODATE.* table** — distinct from the WO header (BKWOMSTR) and line (BKWODTL) tables; stores actual vs. planned start/finish dates and quantities.
- **Action type master** (T7ACTION) — IS.ACTION.TYPE/DESC is a generic code table used across modules (CRM, Service/Repair, or shop floor) to categorize actions taken.
- **ACRD disposition codes** (T7ACRDTYPE) — ac.rd.type/reason/dispo = action record disposition types. Likely used in Service/Repair or QC return workflows (reason for action, disposition taken).

**Primary tables:** WODATE.* (WO actual date records), IS.ACTION.* (action type master), AC.RD.* (action record disposition types)

**Confidence: 45/100** — 3 DFMs read; WODATE.* table confirmed; AC module's exact menu placement and full scope unclear; IS.ACTION.* may be shared with CM/SR modules.

---

## CC — Credit Card Processing ⚠️ NAME CORRECTION

**Previously listed as:** Cycle Count (INCORRECT)
**Correct module name:** Credit Card Processing

**DFM files confirmed:** T7CCP.DFM, T7CCPO.DFM, T7ccr1.DFM, T7CCCITM.DFM, T7CCCWOT.DFM, T7CCDE.DFM (6 total)

**Evidence for correction:** T7CCP Caption='Credit Card Info', fields IS.CC.MASKED/IS.CC.ZIP/IS.CC.CARDNAME/IS.CC.EXP; T7ccr1 Caption='Credit Card Invoice List'; T7CCDE Caption='CC Import'.

**Forms read from network share:**

| DFM | Purpose | Key fields |
|-----|---------|------------|
| T7CCP.DFM | Credit card entry/storage | IS.CC.MASKED (masked card #), IS.CC.ZIP, IS.CC.CARDNAME, IS.CC.EXP (MMYY), ccamount; "Expired" flag |
| T7CCPO.DFM | Credit card charges on POs | ccnum, ccamount, cczip, CCYY, CCMM (split expiry) |
| T7ccr1.DFM | Credit card invoice list report | Caption='Credit Card Invoice List'; Fromdate, thrudate, Fromterms, thruterms |
| T7CCCITM.DFM | Item range filter (for CC reports) | from.item (item range) |
| T7CCCWOT.DFM | WO/location filter (for CC reports) | from.wonum, LOCATION |
| T7CCDE.DFM | CC data import from CSV | Caption='CC Import'; file.name, COMMA.FIXED.STR, FIELD.NUMBER2[1-2] |

**Key findings:**
- **Masked card storage** — IS.CC.MASKED stores the masked card number (not raw PAN), IS.CC.CARDNAME = cardholder name, IS.CC.EXP = expiry, IS.CC.ZIP = billing zip. The "Expired" flag field suggests expiry validation is built in.
- **PO integration** — T7CCPO links credit card charges to purchase orders (ccnum, ccamount on PO). Vendors can be paid by credit card through the PO module.
- **Invoice list report** — T7ccr1 reports CC invoices by date range and terms — used for reconciliation.
- **CSV import** (T7CCDE) — CC transactions can be imported from a CSV file (bank statement download workflow).
- **WO/Item range filters** — CC charges can be analyzed by WO or item range, suggesting CC costs are allocated to jobs/WOs for cost accounting.

**Primary tables:** IS.CC.* (credit card records — masked)

**Confidence: 65/100** — All 6 DFMs read; CC data model confirmed; masked storage confirmed; exact IS.CC field count and AR/AP integration pathway not fully decoded.

---

## SP — Statistical Process Control (SPC)

**DFM files confirmed:** T7SPC.DFM, T7SPCLIVEGRID.DFM, T7SPCLIVEREP.DFM, T7SPCREP.DFM, T7SPCREP2.DFM, T7SPCREPPPM.DFM (6 total)

**Forms read from network share:**

| DFM | Purpose | Key fields |
|-----|---------|------------|
| T7SPC.DFM | Inspector scan/error entry (178 KB) | SORTKEY, SCAN.EMP, SCAN.WO, IS.SERR.ERROR, IS.SERR.PROCESS; Inspector #, Employee, Work Order, Work Order Item, Work Order Qty, Customer, Drawing |
| T7SPCLIVEGRID.DFM | Real-time error dashboard | Caption='Top Real Time Errors'; ATYPE, ADETAIL, ACODE, ACOUNT |
| T7SPCLIVEREP.DFM | Live error report (auto-refresh) | Types/Details/Date range; "Refresh Every" (interval field) |
| T7SPCREP.DFM | WO inspection report | from.wonum, thru.wonum, from.item, thru.item, From.EMP; WO/Part/Employee/Date range |
| T7SPCREP2.DFM | Inspection report (variant) | Same range structure as SPCREP |
| T7SPCREPPPM.DFM | PPM (Parts Per Million) defect report | from.wonum, thru.wonum, from.item, thru.item, from.date, "Sides From" range |

**Key findings:**
- **Inspection-driven SPC** — EvoERP's SPC implementation is structured around an inspector scanning Work Orders for errors/defects. Not traditional control chart SPC — it's defect-rate tracking at the WO level.
- **IS.SERR.* table** — "Scan Error" records. Each record ties an error type (IS.SERR.ERROR) to a process (IS.SERR.PROCESS), WO, employee, and item.
- **Real-time dashboard** (SPCLIVEGRID) — "Top Real Time Errors" grid with ATYPE/ADETAIL/ACODE/ACOUNT fields. Live feed of current error rates, refreshable (SPCLIVEREP "Refresh Every" field).
- **PPM reporting** (SPCREPPPM) — Parts Per Million defect rate by WO/part/date with "Sides" range (suggests PCB manufacturing context: boards have two sides — a very specific quality metric for electronics/PCB shops).
- **Drawing number** field in main entry form — inspectors reference engineering drawings during inspection.
- **WO-centric** — all reports filter by WO number range, confirming SPC data is collected at the WO/job level.

**Primary tables:** IS.SERR.* (scan/inspection error records)

**Confidence: 60/100** — All 6 DFMs read; module purpose clear; IS.SERR.* table confirmed; PPM "Sides" field strongly suggests PCB/electronics customer; exact IS.SERR field count and process taxonomy not decoded.

---

*Last updated: 2026-06-18*
*Source: DFM files read from \\I2S109-SOLIDCRM\DBAMFG$\, CHM help topics from samples\chm\extracted\*

---

## Previously-Unlisted Legacy and System Modules (Pass 106m — 16 "opaque" codes)

These module codes appear in the DDF table names, program files on the network share, or BKMENUSU.TXT but are not listed as active GROUPS/BUTTONS in the current menu. Most are TAS Pro 6-era legacy modules or internal system modules.

**Investigation method:** DFM inspection (T7MA, T7PL, T7RT), DDF schema grep (BKCP, BKPC, BKSL, etc.), network share scan for T7*/T6*/BK* prefix files, BKLME.SRC source read, BKMENUSU.TXT grep.

---

### AB — Authorization / Software Licensing

**Tables:** BKABCUST, BKABVEND

| Table | Key fields |
|-------|------------|
| BKABCUST | BKAB_START (license start date), BKAB_EXP (expiration), BKAB_PERIOD (license period), BKAB_WARNING (days-before-expiry warning), BKAB_STAND_ALNE (standalone flag) |
| BKABVEND | BKAB_SERIAL (license serial number), BKAB_REG_NAME (registered company name) |

**Related files:** T6AB*.RTM — 12+ alternative/abbreviated report templates (T6ABINV, T6ABPO1, T6ABrma1, T6ABSCHK, T6ABSOB4, T6ABSPAC, T6ABSQT2, T6ABSQUT, T6ABWOC3, T6ABWOC4).

**Purpose:** Built-in EvoERP software license management. BKABCUST tracks license validity (start/expiration dates, period, warning threshold); BKABVEND stores the software license serial and registered name. The T6AB*.RTM files are printed authorization/billing documents for customers/vendors — **not** standard ERP transactions. **Confidence: 55/100**

---

### CP — Computer Payroll / Checkmark Payroll (legacy predecessor to PL)

**Tables:** BKCPMSTR, BKCPEC

| Table | Key fields |
|-------|------------|
| BKCPMSTR | BKCP_MST_CMPATH (Checkmark install path), IMPATH (import path), CFILE (check file), VFILE (vendor file), EXPATH (export path), HFILE (header file), LABEX (label export flag), COMMEX (comment export flag), EFILE (employee file) |
| BKCPEC | BKCP_EC_DATE, BKCP_EC_GLACCT, BKCP_EC_GLDEPT, BKCP_EC_AMOUNT, BKCP_EC_CHECKNO, BKCP_EC_DESC, BKCP_EC_ISCHK (is-check flag), BKCP_EC_ERROR, BKCP_EC_LINE, BKCP_EC_VEND |

**Purpose:** The legacy AP check export module that links EvoERP to the **Checkmark payroll** external software. BKCPMSTR stores file path configuration for the Checkmark data files; BKCPEC holds export records for AP checks (date, GL account, amount, check number, vendor, error flag). This function was superseded by **PL (Pay Link)**, which uses T6PLA.RUN, BKPLB.RUN, BKPLC.RUN, BKPLD.RUN. **Confidence: 60/100**

---

### EX — SQL Export / Business Intelligence Export

**Files:** SQLEXPORT.RWN (TAS Pro 7), SQLEXPORT.DFM (T7JTemp loader), SQLExport.jar (Java Swing)

**Architecture (Pass 156, 2026-06-22):**
- SQLEXPORT.RWN launches a "Loading...." splash (SQLEXPORT.DFM = T7JTemp template) while spawning SQLExport.jar.
- SQLExport.jar is a Java Swing application (`com.evoerp.*` package, v1.5.0, build 2014-03-19).
- Connects via Pervasive JDBC v2 to a **separate BI database** (`EVOBI2`) on port 1583 — NOT the operational DBAMFG$ data.
- Key classes: `com.evoerp.sql.PervasiveDatabase`, `com.evoerp.ui.util.TextExportingWorker` (CSV export), `com.evoerp.ui.util.FileOpeningWorker`.
- Default output: `\\I2S109-SOLIDCRM\DBAMFG$\REPORTS\` (CSV files).
- Logs to `\\I2S109-SOLIDCRM\DBAMFG$\logs\SQL Export.log`.

Note: t7exec.RUN (TAS Pro 6) is an older generic program launcher — separate from the TAS Pro 7 EX module.

**Confidence: 45/100** — Architecture confirmed from DFM (T7JTemp) + log file (Java params, package names, DB). SQLExport.jar UI/SQL not decompiled; EVOBI2 schema unknown.

---

### FL — Field Help

**Tables:** BKFLDHLP

| Table | Fields |
|-------|--------|
| BKFLDHLP | HLP_CODE (field identifier), HLP_INDEX (line number), HLP_LINE (60-char help text) |

**Purpose:** The TAS Pro field-level context help system. When a user presses F1 on any entry field, the runtime looks up HLP_CODE in BKFLDHLP to display multi-line help text. Not a user-navigable business module. **Confidence: 65/100**

---

### LM — List Maintenance (Inventory Transaction Consolidation)

**Files:** BKLMA.RUN through BKLMI.RUN (9 operations), **BKLME.SRC** (readable source)

**Confirmed from BKLME.SRC:** Header = `"LM-E  Consolidate Inventory Transactions"`. History comment: "Changed from BKMMG.src to BKDME.src on 12/30/99; Changed from bkdme.src to bklme.src on 3/30/00" — confirming MM→DM→LM renaming.

**LM-E function (from source):** Reads INVTXN (inventory transaction) table by item code and date range. For each item, groups all transactions by type (A=Adjustments, S=Shipments, P=PO Receipts, W=WO Receipts, I=WO Issues, Q=QC Receipts, O=Outside Process, C=Cost Change, J=PO WIP Receipts), sums quantities and costs, deletes the individual records, then writes one consolidated record per type. Preserves lot/serial records (never consolidates them). Net quantity / average cost are preserved.

**Purpose:** A DBA-era database maintenance utility to compact the INVTXN table by summarizing old transaction detail. Still ships on the network share but is not in the current EvoERP menu. **Confidence: 90/100** (source confirmed)

---

### LO — Lot/Serial Assignment Popup (T7LotSerial + t7lottag)

**Pass 317 (2026-06-26):** DFMs read from `\\i2s109-solidcrm\DBAMFG$`; copied to `samples/src/`.

**Files:** `T7LotSerial.DFM` (54 KB), `t7lottag.DFM` (14 KB)

LO is not a menu-accessible module — it provides **cross-module popup forms** invoked by PO receiving, WO completion, and SO shipment whenever lot or serial tracking is required.

#### T7LotSerial.DFM — "Enter Lot/Serial Information" popup

SourceFile: `T7LOTSER`. FormStyle: `fsStayOnTop` (always on top). OnClose: `T7LS.OnClose`. 13 bound fields:

| FieldName | Meaning |
|-----------|---------|
| `ETBcomboval` | Grid selector (toolbar combo) |
| `ls.loc` | Warehouse/bin location for lot/serial assignment |
| `lot.start.qty` | Total qty to assign to lots |
| `lot.rem.qty` | Lot qty not yet assigned (running remainder) |
| `lot.ind.qty` | Qty for this individual lot number entry |
| `lot.num` | Lot number being assigned |
| `Lot.expDate` | Lot expiry date |
| `use.same.lot` | "Use Same Lot# for all PO Lines" flag (Y/N checkbox) |
| `ser.start.qty` | Total qty to serialize |
| `ser.rem.qty` | Qty not yet serialized (running remainder) |
| `ser.ind.qty` | Qty for this individual serial number |
| `ser.num` | Serial number being assigned |
| `Ser.expDate` | Serial expiry date |

The form has two panels: one for lot entry (`lot.*` vars) and one for serial entry (`ser.*` vars). Both panels appear on the same form — the TAS program controls which panel is visible based on the item's tracking type (LOT_YN/SER_YN flags). The `use.same.lot` checkbox is for PO line context: when receiving a multi-line PO, all lines get the same lot number.

#### t7lottag.DFM — Evo Lot Tag (label print template)

A `TPanel` container with 3 dynamically-filled labels: `Label1`, `Label2`, `Label3`. No FieldName bindings — the TAS program sets label content at runtime from the lot record (typically: Label1=item code, Label2=lot number, Label3=quantity or expiry). This is the label print preview / print dialog for the lot tag printer.

#### Cross-module context

This popup is called from:
- **PO-J** (receiving): assigns lot/serial to received items before posting to BKICLOC/MTLOT
- **WO completion**: assigns lot/serial to finished goods
- **SO-C/MH** (shipping): verifies lot/serial allocation before shipment

The full Lot Control module logic (T7LCA–T7LCG) is documented under the LC module section.

**Confidence: 90/100** — Both DFMs fully read and all fields confirmed (Pass 317). Popup invocation context confirmed from LC/MH/PO module analysis. Remaining gap: exact TAS proc names that call T7LotSerial (invocation chain not traced from binary — would require decrypted RWN caller analysis).

**Files:** T7MAPDEPO.DFM, T7MAPDEPO.RWN

**DFM confirmed:** Form Caption='New Screen' (generic); fields: bkar.dep.depno (deposit number), BKAR.DEP.CUST (customer), BKAR.CUSTNAME, depo.orig.amt (original amount), amount.rem (remaining), sFROM.SONUM (SO number), from.item (item), GL account override.

**Tables (from DDF):** BKMATCST (10-tier quantity/cost breakpoints, field prefix BKMC_), BKMATRIM (machine trim settings: BKMA_TRIM_MACH, BKMA_TRIM_FIRST, BKMA_TRIM_SECND).

**Purpose:** T7MAPDEPO = **Apply/Map Deposits** — applies prepaid customer deposits to sales orders/invoices. Reads the BKAR.DEP.* (AR Deposit) table; allows partial application across multiple SO lines. The BKMATCST/BKMATRIM tables suggest a broader **Material** costing sub-module also uses the MA prefix (10-level quantity cost breakdowns may be used for material purchasing cost analysis). Exact relationship between deposit mapping and material tables unclear. **Confidence: 55/100**

---

### MM — Manufacturing Maintenance (TAS Pro 6 legacy)

**Files:** BKMMA.RUN through BKMMN.RUN + BKMMKA.RUN (14 programs)

**Purpose:** Predecessor to LM (List Maintenance) and DM. The BKLME.SRC history confirms that BKMMG was the original source of LM-E. MM was a TAS Pro 6-era module for inventory/manufacturing data maintenance that was progressively renamed DM → LM during 1999-2000. All files are .RUN (TAS Pro 6) — not currently in the EvoERP menu. **Confidence: 40/100** (purpose inferred from naming history)

---

### PC — Production Control (legacy kit/plot system)

**Tables:** BKPCKIT, BKPCPLOT

| Table | Key fields |
|-------|------------|
| BKPCKIT | BKPC_KIT_COMP (component item), KIT_QTY_R (required qty), KIT_QTY_A (available qty), KIT_QTY_S (shipped qty), KIT_DATELM (date eliminated), KIT_LOC (location) |
| BKPCPLOT | BKPC_PLOT_PROD (product), PLOT_ISDTE (issue date), PLOT_SPDTE (ship date), PLOT_QTY (quantity), PLOT_CUST (customer), PLOT_INKO, PLOT_STAT (status), PLOT_STRTD (start date), PLOT_COMPD (complete date), PLOT_LOC (location) |

**Purpose:** An older production control / kit-building system. BKPCPLOT tracks production lots (quantity, status, start/complete dates, customer) — similar to a simplified work order. BKPCKIT tracks the components required/available/shipped for each kit/plot. Likely a TAS Pro 6-era BOM execution system that was superseded by the WO (Work Order) module. **Confidence: 50/100**

---

### PL — Pay Link (Checkmark Payroll Integration)

**Confirmed from BKMENUSU.TXT:** `"GROUPS","Pay Link","PL"` — active menu group.

**Operations:**
- PL-A: T6PLA.RUN — Run Checkmark Payroll
- PL-B: BKPLB.RUN — Import Employee Checks
- PL-C: BKPLC.RUN — Import Employer Vouchers
- PL-D: BKPLD.RUN — Payroll Link Setup

**Purpose:** Integrates EvoERP with external **Checkmark payroll** software. PL-A runs Checkmark directly from EvoERP's menu; PL-B/C import check and voucher data back into EvoERP for GL posting; PL-D configures the link. Successor to the older **CP** module. Note: T7PLess*.DFM files (T7PLessComps, T7PLessNotes, T7PLessWODates) are "Paperless" shop-floor sub-forms called by HH/DC modules — unrelated to PL Pay Link despite the naming coincidence. **Confidence: 72/100**

---

### RT — Routing Templates for Estimating

**Tables:** BKRTCST, BKRTEMTR, BKRTSPEC, BKRTTEMP

| Table | Key fields |
|-------|------------|
| BKRTCST | BKRT_QUOTE (quote number), BKRT_CODE (item), BKRT_OPER (operation#), BKRT_PARTSHR_1..10 (part share per qty tier), BKRT_SETUP_1..10 (setup times) |
| BKRTEMTR | MTRO_CODE (item), MTRO_OPER (operation#), MTRO_DESC, MTRO_OPERDESC, MTRO_TYPE, MTRO_LEAD (lead time), MTRO_VENDCOST, MTRO_PARTSHR, MTRO_TIMEPART, MTRO_SETUPHRS, MTRO_LOTSIZE, MTRO_INSTR_1..5 (work instructions) |
| BKRTSPEC | BKRT_SPEC_PART, BKRT_SPEC_SEQ, BKRT_SPEC_LINE, BKRT_SPEC_NOTE_1..4 |
| BKRTTEMP | BKRT_TEMP_CODE, BKRT_TEMP_LINE, BKRT_TEMP_NOTE_1..4 |

**Files:** T7RTMVALID.DFM/RWN — "Select Report Format Name" dialog (shared utility for choosing an RTM print format, not an RT-module business form).

**Purpose:** Routing template tables used by the **ES (Estimating)** module to calculate labor costs for quotes. BKRTEMTR stores routing operation templates with setup hours, part-share ratios, and work instructions. BKRTCST links routing costs to specific quote numbers. BKRTSPEC/BKRTTEMP hold routing specification notes. RT = **Routing Templates** for estimating. **Confidence: 55/100**

---

### SB — Spec Book / Approved Source List

**Pass 317 (2026-06-26):** BKSB* schemas fully confirmed from Pervasive ODBC DDF query.

**Tables:** BKSBMFG (16f), BKSBPART (5f), BKSBVEND (6f)

SB is a **data module** — no dedicated T7SB* UI programs. The three tables are managed via BM-J/K/L (T7BMJ/T7BMK/T7BML) and a stub `T7DSBOM.RWN` (5 procs, 1 var=STUB — pure stub, no logic).

#### BKSBPART — Approved Substitute Parts (5 fields, DDF-confirmed)

| Field | Type | Size | Meaning |
|-------|------|------|---------|
| `BKSB_PART_PARNT` | STRING | 15 | Parent assembly (PK) |
| `BKSB_PART_PROD` | STRING | 15 | Component/product (PK) |
| `BKSB_PART_CUST` | STRING | 10 | Customer code (PK — customer-specific substitutes) |
| `BKSB_PART_SUBST` | STRING | 15 | Approved substitute part number |
| `BKSB_PART_EXTRA` | STRING | 50 | Notes/spare field |

#### BKSBVEND — Approved Vendors (6 fields, DDF-confirmed)

| Field | Type | Size | Meaning |
|-------|------|------|---------|
| `BKSB_VEND_PARNT` | STRING | 15 | Parent assembly (PK) |
| `BKSB_VEND_PROD` | STRING | 15 | Component/product (PK) |
| `BKSB_VEND_CUST` | STRING | 10 | Customer code (PK) |
| `BKSB_VEND_VEND` | STRING | 10 | Approved vendor code (FK → BKAPVEND) |
| `BKSB_VEND_VPART` | STRING | 25 | Vendor's part number for this component |
| `BKSB_VEND_EXTRA` | STRING | 50 | Notes/spare field |

#### BKSBMFG — Approved Manufacturers (16 fields, DDF-confirmed)

| Field | Type | Size | Meaning |
|-------|------|------|---------|
| `BKSB_MFG_PARNT` | STRING | 15 | Parent assembly (PK) |
| `BKSB_MFG_PROD` | STRING | 15 | Component/product (PK) |
| `BKSB_MFG_CUS` | STRING | 10 | Customer code (PK) |
| `BKSB_MFG_MANUF` | STRING | 25 | Manufacturer name (PK) |
| `BKSB_MFG_MPART` | STRING | 25 | Manufacturer's part number |
| `BKSB_MFG_EXTRA` | STRING | 50 | Notes/spare field |
| `BKSB_MFG_MAKING` | STRING | 10 | Assembly process code |
| `BKSB_MFG_ALPHA_1` | STRING | 30 | User-defined alpha 1 |
| `BKSB_MFG_ALPHA_2` | STRING | 30 | User-defined alpha 2 |
| `BKSB_MFG_GDATES_1` | DATE | 4 | Generic date 1 (e.g., approval date) |
| `BKSB_MFG_GDATES_2` | DATE | 4 | Generic date 2 (e.g., expiry date) |
| `BKSB_MFG_FLAGS_1..5` | STRING | 1 each | Status/approval flags (Y/N) |

BKSBMFG is the richest table — 16 fields with approval dates and 5 status flags supporting manufacturer approval workflows.

**Files:** BKSBMFG.XPT, BKSBVEND.XPT (export templates for spec records). T7DSBOM.RWN = pure stub.

**Purpose:** Manages the **Approved Source List (ASL)** — for each parent assembly + component item + customer combination, records approved manufacturers (with mfr part#s), approved vendors (with vendor part#s), and approved substitute parts. Common in electronics/PCB manufacturing where customers specify which manufacturer's version of a component is acceptable. SB = **Spec Book**.

**Confidence: 90/100** — All three BKSB* table schemas now DDF-confirmed (Pass 317); field semantics confirmed from field name patterns + BM-J/K/L program analysis; T7DSBOM.RWN confirmed as pure stub. Remaining gap: BKSBMFG FLAGS_1..5 and ALPHA_1..2 semantic meanings not confirmed (field names are generic).

---

### SL — Security Levels

**Tables:** BKSLEVEL, BKSLMSTR

| Table | Key fields |
|-------|------------|
| BKSLMSTR | BKSL_MSTR_LEVEL (2-char level code), BKSL_MSTR_DESC (description) — master list of security levels |
| BKSLEVEL | BKSL_MENU (menu group number), BKSL_LEVEL (level code), BKSL_MENU1_YN (Y/N for whole group), BKSL_MENU1_1..13 (13 per-item access flags) |

**Files:** t7slsfc.RWN (one RWN on share — function unknown, encrypted).

**Purpose:** Defines **security level** codes and their per-menu-item access permissions. Works alongside **PS (Password Security)** and **UM (User Menu Security)** — the three form EvoERP's layered access control: SL defines levels, UM assigns users to levels per menu, PS manages user accounts. **Confidence: 60/100**

---

### SY — System Tables (internal prefix)

**Tables:** BKSYMSTR (286 fields), BKYSMSTR (195+ YN flags), BKSYCFG, BKSYLOG, BKSYPRTR, BKSYUSER, BKSYHELP, BKSYAP, BKSYAR

**Purpose:** SY is the internal prefix for EvoERP's global system configuration tables. These tables are managed by the **SM (System Maintenance)** and **AD (Accounting Defaults)** modules in the current menu. SY may be an internal module code used programmatically (e.g., for open_symstr() / open_ysmstr() function calls in TAS source). Not visible as a separate menu group. **Confidence: 55/100**

---

### UM — User Menu Security

**Tables:** BKUMSRTY

| Table | Key fields |
|-------|------------|
| BKUMSRTY | SCRTY_LEVEL (security level), SCRTY_MENU (menu group number), SCRTY_GROUP (Y/N for whole group), SCRTY_ITEM_1..13 (per-item access flags) |

**Purpose:** Per-menu-group access assignments for security levels. Parallel to BKSLEVEL but organized differently — BKUMSRTY is keyed by LEVEL + MENU, giving per-level per-menu access control. Works with SL (Security Levels) and PS (Password Security) to form EvoERP's three-tier access control system. UM = **User Menu** security. **Confidence: 60/100**

---

### UP — Update Management

**Tables:** BKUPDATE

| Table | Key fields |
|-------|------------|
| BKUPDATE | BKUP_COMPANY (company code), BKUP_UPDATE (update flag), BKUP_DATE (date applied), BKUPDATE_VER (version string) |

**Purpose:** Tracks which EvoERP software updates (patches) have been applied to which companies. Each row records a company + update flag + date + version string. Used by the **EvoUpdate** system (EvoUpdate.RWN, UPDTP7.EXE) to determine which patches are already installed. UP = **Update** tracking. **Confidence: 70/100**

---

### YS — Yes/No System Parameters (BKYSMSTR editor)

**Files:** T7YSYN.RWN (one RWN on share — encrypted)

**Tables:** BKYSMSTR (195+ Yes/No flag fields)

**Purpose:** T7YSYN.RWN ("YS-YN") is the program for editing BKYSMSTR — EvoERP's global Yes/No configuration parameter table. BKYSMSTR stores 195+ boolean system settings (distinct from BKSYMSTR which stores numeric/string parameters). YS is the module code for this configuration editor; it pairs with SM module (which manages BKSYMSTR). YS = **Yes/No System** parameters. **Confidence: 60/100**

---

### Summary Table — 16 Opaque Modules

| Code | Name | Status | Primary tables / files | Confidence |
|------|------|--------|----------------------|-----------|
| AB | Authorization/Licensing | Legacy + active | BKABCUST, BKABVEND; T6AB*.RTM | 55 |
| CP | Computer Payroll (legacy → PL) | Legacy | BKCPMSTR, BKCPEC | 60 |
| EX | Execute (launcher) | Internal utility | t7exec.RUN | 35 |
| FL | Field Help | Internal | BKFLDHLP | 65 |
| LM | List Maintenance (Inv Txn Consolidation) | Legacy (not in menu) | BKLMA-BKLMI.RUN, BKLME.SRC | 90 |
| LO | Lot/Serial Assignment Popup | Cross-module popup (no menu entry) | T7LotSerial.DFM, t7lottag.DFM | 90 |
| MA | Map Deposits / Material | Partial (T7 era) | T7MAPDEPO.DFM; BKMATCST, BKMATRIM | 55 |
| MM | Manufacturing Maintenance (legacy) | Legacy predecessor to LM | BKMMA-BKMMN.RUN | 40 |
| PC | Production Control (legacy) | Legacy | BKPCKIT, BKPCPLOT | 50 |
| PL | Pay Link (Checkmark Payroll) | Active (in menu) | T6PLA.RUN, BKPLB-BKPLD.RUN | 72 |
| RT | Routing Templates (for ES Estimating) | Internal sub-module | BKRTCST, BKRTEMTR, BKRTSPEC, BKRTTEMP | 55 |
| SB | Spec Book / Approved Source List | Active (has .XPT exports) | BKSBMFG, BKSBPART, BKSBVEND | 90 |
| SL | Security Levels | Internal | BKSLEVEL, BKSLMSTR; t7slsfc.RWN | 60 |
| SY | System Tables (internal prefix) | Internal (used by SM/AD) | BKSYMSTR, BKYSMSTR, BKSY* | 55 |
| UM | User Menu Security | Internal | BKUMSRTY | 60 |
| UP | Update Management | Active | BKUPDATE | 70 |
| YS | Yes/No System Parameters | Internal sub-module | T7YSYN.RWN; BKYSMSTR | 60 |

## Module Name Corrections (2026-06-15)

| Module | Was documented as | Correct name | Evidence |
|--------|------------------|--------------|----------|
| SC | Scheduling/Capacity Planning | **Serial Control** | T7SCA Caption='SC-A Edit Serial Numbers'; MTSER fields; IS.SERC.* config |
| SH | Shipping | **Shop Scheduling** | T7SHA Caption='SH-A'; MTWO.WIP.* and MTWORO.* fields; work center capacity |
| WC | Work Center | **Warehouse Control** | T7WCA Caption='Location/Bin/Description'; ISBN.MSTR fields; "Duplicates" bin button |
| SR | (Sales Reports in DFM inventory) | **Service/Repair** | T7SRK fields ISSR.MMS.MAKE/MODEL/SERIAL; "IN Date"/"OUT Date"/"S/R Number"/"Motor" |
| CC | Cycle Count | **Credit Card Processing** | T7CCP Caption='Credit Card Info'; IS.CC.MASKED/CARDNAME/EXP fields; T7ccr1 Caption='Credit Card Invoice List' |
| SP | Ship Packing? | **Statistical Process Control (SPC)** | T7SPC Caption has 'Inspector #', 'Work Order:'; IS.SERR.ERROR/PROCESS fields; T7SPCREPPPM='PPM defect report' |

## CHM-Identified Modules (no DFMs — in RWN)

The following modules have no T7* DFM files on the network share. Their operations were identified from EvoHELP.CHM topic filenames.

### AD — Accounting Defaults

**Operations confirmed from CHM:**
- AD-A — General Ledger Defaults
- AD-B — Checking Account Defaults
- AD-C — Accounts Payable Defaults

**Purpose:** System-level default configuration for GL, bank accounts, and AP. Likely sets the default GL accounts, AP payment terms, and bank routing information used across all modules. **Confidence: 40/100**

---

### CR — Customer Revenue / SO Department Approvals

**Operations confirmed from CHM:**
- CR-A — Assign Departments to Sales Orders
- CR-B — View/Enter SO Approvals

**Purpose:** Manages SO-level workflows — assigning departments to sales orders and the approval process (view or enter approvals for SOs before they're released). **Confidence: 40/100**

---

### FP — Features & Options Print

**Operations confirmed from CHM:**
- FP-B — Print Features and Options

**DFM filter forms (via FO module):** T7FOD.DFM, T7FOE.DFM

**Purpose:** Print sub-module for the FO (Features & Options) module — generates a printed features/options sheet from the configured BOM option flags.

**Key findings (updated Pass 156b, 2026-06-22):**
- **Zero T7FP* programs** — exhaustive search across all 1,122 RWN modules found no T7FP* bytecode. FP uses T7FOD and T7FOE (FO-labeled programs), not a T7FP* namespace.
- **T7FOD.RWN** — 103 procedures, source EVO.LIB. **DECRYPTED + SYMBOLS EXTRACTED.** Full print executor for FP-B range printing. Opens 18 tables (see fingerprint below). Filter form: T7FOD.DFM (item/category/class ranges).
- **T7FOE.RWN** — 86 procedures, source EVO.LIB. **DECRYPTED + SYMBOLS EXTRACTED.** Full print executor for FP-B single-item printing. Identical 18-table fingerprint. Filter form: T7FOE.DFM (single item).
- **NOT RTM-only** — prior conclusion was wrong. T7FOD/T7FOE are full standalone RWN programs, not stubs. The RTM filename is **runtime-configurable** via `CFG.RTM.NAME` / `RTM_NAME` / `RTM.NUMBER` variables (not hardcoded).
- **18-table DB fingerprint (both programs, identical):** BKICMSTR, MTICMSTR, BKBMMSTR, BKICLOCM, CLASMSTR, BKSYHELP, DBAHLPID, ISIS, MKAHIST, ISLOG, ISDRILL, BKAPVEND, BKARCUST, BKCMACCN, ISLINKS, BKAPDESC, LANGDICT, FILELOC.
- **MTICMSTR presence** — FP can print from both production (BKICMSTR) and estimating (MTICMSTR) inventory.

**Confidence: 72/100** — T7FOD/T7FOE decrypted and symbol-extracted (Pass 156b); 18-table DB fingerprint confirmed; RTM runtime-config pattern confirmed from variable names; RTM file content and exact column layout not yet read.

---

### QU — Query / Inquiry Tools

**Operations confirmed from CHM:**
- QU-A — Master Inquiry
- QU-B — Calendar Drill Down
- QU-C — Calendar Summary Report
- QU-D — Business Status
- QU-E — Quick Grid Lookup
- QU-F — Query Executor

**Purpose:** EvoERP's built-in business intelligence and query layer. QU-A=Master Inquiry (cross-module record lookups), QU-B/C=calendar-based scheduling views, QU-D=executive dashboard (Business Status), QU-E=grid-based lookup tool, QU-F=free-form query executor (likely TAS SQL or filter builder). **Confidence: 50/100**

---

### SU — Setup / UI Configuration

**Operations confirmed from CHM:**
- SU-A — Maintain Grid Lookups
- SU-B — Maintain Drill Down Menus
- SU-C — Forms Editor
- SU-D — Grid Maintenance

**Purpose:** Configures EvoERP's UI layer. SU-A defines the columns/filters that appear in grid lookup screens. SU-B configures drill-down menu trees. SU-C = the forms editor (modify form layouts at runtime — similar to TA-M). SU-D = grid column maintenance. **Confidence: 50/100**

---

### TA — TAS / System Administration

**Operations confirmed from CHM:**
- TA-D — Maintain Database
- TA-G — Maintain Menu Access Records
- TA-H — Maintain Menu End User
- TA-M — Forms Editor
- TA-N — Program Scheduler
- TA-O — Backup Utility
- TA-Q — Change Logo Image
- TA-R — SQL Editor
- TA-S — Data Dictionary Check

**Purpose:** The most powerful admin module in EvoERP. TA provides direct access to the underlying database (TA-D), full menu access control (TA-G=system level, TA-H=end-user level), a program scheduler (TA-N), backup utility (TA-O), a SQL editor (TA-R), and data dictionary integrity check (TA-S). TA-Q changes the company logo image. **⚠️ Reserved for system administrators — operations here can affect all users and all data.** **Confidence: 55/100**
