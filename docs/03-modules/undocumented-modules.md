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

**What it does:** Lot number tracking for inventory items. Assigns lot numbers at receipt, tracks lot quantities through production and shipment. Structurally identical to SC (Serial Control) but at lot-quantity level rather than individual-unit level.

| Code | DFM | What it does |
|------|-----|-------------|
| LC-A | T7LCA.DFM | **Edit Lot Numbers** — view/edit individual lot records. Fields: MTLOT.LOT (lot number), MTLOT.ONHAND (qty on hand), MTLOT.RECDATE (receipt date), MTLOT.WO (associated WO#). Primary table: MTLOT. |
| LC-B | T7LCB.DFM | **Assign Lot Control** — configure which inventory items are lot-tracked via MTIC.PROD.LOT flag. Shows BKIC.PROD.DESC (description), BKIC.PROD.NOTE, BKIC.PROD.TYPE. Parallel to SC-B for serials. |
| LC-C | T7LCC.DFM | Lot browse/inquiry with allocation print option (`prt.allocs`). Filter by item and lot ranges. |
| LC-E | T7LCE.DFM | Item/class/category range filter for lot reports |
| LC-F | T7LCF.DFM | **Lot status inquiry** — filter by item + lot number. Report options: Summary, Details, All. |
| LC-G | T7LCG.DFM | **Archive/Unarchive lots** — by item range + expiry date range (`from.expdate`, `thru.expdate`). Expiry date confirms lot tracking is used for perishable/dated materials. |

**SC vs LC comparison:**

| Feature | SC (Serial Control) | LC (Lot Control) |
|---------|-------------------|-----------------|
| Granularity | One record per unit | One record per lot (multiple units) |
| Main table | MTSER | MTLOT |
| Item flag | MTIC.PROD.SER | MTIC.PROD.LOT |
| Expiry tracking | MTSER.EXPDATE | LC-G has expiry date filter |
| Archive form | SC-E | LC-G |
| Assign form | SC-B | LC-B |

**Primary tables:** MTLOT (lot master — one record per lot), MTIC.PROD.LOT (item-level lot tracking flag)

**Confidence: 72/100** — All 6 found DFM files read; lot lifecycle confirmed; MTLOT table fields confirmed; expiry date support confirmed.

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

*Last updated: 2026-06-15*
*Source: DFM files read from \\I2S109-SOLIDCRM\DBAMFG$\, CHM help topics from samples\chm\extracted\*

## Module Name Corrections (2026-06-15)

| Module | Was documented as | Correct name | Evidence |
|--------|------------------|--------------|----------|
| SC | Scheduling/Capacity Planning | **Serial Control** | T7SCA Caption='SC-A Edit Serial Numbers'; MTSER fields; IS.SERC.* config |
| SH | Shipping | **Shop Scheduling** | T7SHA Caption='SH-A'; MTWO.WIP.* and MTWORO.* fields; work center capacity |
| WC | Work Center | **Warehouse Control** | T7WCA Caption='Location/Bin/Description'; ISBN.MSTR fields; "Duplicates" bin button |
| SR | (Sales Reports in DFM inventory) | **Service/Repair** | T7SRK fields ISSR.MMS.MAKE/MODEL/SERIAL; "IN Date"/"OUT Date"/"S/R Number"/"Motor" |
| CC | Cycle Count | **Credit Card Processing** | T7CCP Caption='Credit Card Info'; IS.CC.MASKED/CARDNAME/EXP fields; T7ccr1 Caption='Credit Card Invoice List' |
| SP | Ship Packing? | **Statistical Process Control (SPC)** | T7SPC Caption has 'Inspector #', 'Work Order:'; IS.SERR.ERROR/PROCESS fields; T7SPCREPPPM='PPM defect report' |
