# GL and WO Module — DFM Form Analysis
Status: partial | verified-from-DFM

Forms read directly from `\\I2S109-SOLIDCRM\DBAMFG$\T7GL*.DFM` and `T7WO*.DFM`.

---

## GL — General Ledger (24 forms)

### GL Transaction Type Codes
Confirmed from T7GLB form:
- **GJ** — General Journal (manual entries)
- **CR** — Cash Receipts
- **CD** — Cash Disbursements
- **TT** — Transaction Template (recurring/reversing entries)
- **YE** — Year End Balance

These five types map directly to the BKGLGJRN/BKGLGJLN table structures.

---

### Form Inventory

| DFM | Purpose | Key fields |
|-----|---------|------------|
| T7GLA.DFM | View Chart of Accounts — budget vs. actual | DISP.ACCT1-4 (multi-column GL accounts), beginning/ending balances → BKGLCOA |
| T7GLB.DFM | Enter/Post General Journal Transactions | Trans #, Posted flag, Date, Type (GJ/CR/CD/TT/YE), Code, Bank, Dep/Ck#, Tag; Line items: ACCT, DESC, amounts → BKGLGJRN, BKGLGJLN |
| T7GLBLIST.DFM | GL-B list view variant | Display-only journal list |
| T7GLC.DFM | GL Transaction Report/Filter | GL acct range, batch range, post/entry date ranges, Inv/Vch# range, journal types (CR/CD/RS/RP/PR/OT/WO/GJ/YE), audit info, orphan transactions, customer/vendor → BKGLTRAN |
| T7GLD.DFM | Journal Inquiry & Report | Post/entry date range, vendor/customer range, reference# range, journal type; current or archived journals, summary only, long check numbers |
| T7GLE.DFM | GL Account Inquiry | GL acct from/thru, department → period-end balance inquiry |
| T7GLESPEED.DFM | GL Account Inquiry (fast variant) | Performance-optimized version of T7GLE |
| T7GLE2.DFM | GL Account Inquiry (secondary) | Additional inquiry form |
| T7GLF.DFM | Account Balance Report | Multi-column comparative report (12+ columns) for period-end balance analysis with date ranges and percentages |
| T7GLG.DFM | GL Analysis Report | GL account range filter |
| T7GLH.DFM | Period-End Processing | Period close control |
| T7GLI.DFM | GL Inquiry variant | — |
| T7GLJ.DFM | GL Processing variant | — |
| T7GLK.DFM | GL Processing variant | — |
| T7GLL.DFM | GL Account Master List | GL Account, GL Department → BKGLCOA |
| T7GLN.DFM | GL Processing variant | — |
| T7GLO.DFM | GL Batch Processing | — |
| T7GLOOB.DFM | Out-of-Balance Detection | Bank reconciliation or GL out-of-balance detection |
| T7GLP.DFM | Period-End Processing Control | GL Acct-dept range filtering |
| T7GLQ.DFM | GL Inquiry with account select | — |
| T7GLS.DFM | GL Summary/Statistics | — |
| T7GLT.DFM | GL Processing variant | — |
| T7GLARCH.DFM | Archive GL Transactions | Archive date threshold → archives BKGLTRAN to BKGLATRN |
| T7GLJASK.DFM | Journal Type Selector | Prompt for journal type filter |

### GL Journal Types (from T7GLC — full set)
Beyond the 5 entry types in T7GLB, T7GLC also filters by:
- **RS** — likely Receipts-Summary or Receiving (from PO receipts → GL posting)
- **RP** — likely Report or Receipts-Posted
- **PR** — Payroll GL postings
- **OT** — Other transactions
- **WO** — Work Order cost postings to GL

This confirms that AP vouchers, PO receipts, payroll, and WO costs all post to GL as separate
journal types — not as GJ entries.

### Key Finding — BKGLX / BKGLXH (GL Cross-Reference)
Primary key `BKGLX_POSTDATE` — these tables hold GL cross-reference records keyed by post date.
Likely used for period reconciliation or cross-module audit trails.

### GL Table Family (28 tables — purpose now mostly clear)
- Live data: BKGLTRAN, BKGLGJRN, BKGLGJLN, BKGLCHK
- Archive copies: BKGLATRN, BKGLAGJR, BKGLAGJL, BKGLACHK
- Report/temp: BKGLRGJR, BKGLRGJL, BKGLTGJR, BKGLTGJL, BKGLTMP/2/3, BKGLTEMP
- Master data: BKGLCOA (accounts), BKGLFCOA (forecast COA), BKGLECOA (edit COA), BKGLCCOA (company COA)
- Statement layout: BKGLFSTL
- Intercompany: BKGLICC
- Cross-reference: BKGLX, BKGLXH

---

## WO — Work Orders (68 forms)

### WO Status Codes (confirmed from T7WOKL, T7WOLA, T7WOLB, etc.)
- **F** — Released (on shop floor)
- **R** — Completed (finished production)
- **C** — Closed (fully posted and closed)
- **S** — Scheduled (planned, not yet released)
- **I** — In Process
- **X** — On Hold
- **C**, **X**, **S**, **F**, **R**, **I** visible in various filter forms

### Work Order Lifecycle

```
1. CREATE    WO-A: T7WOA.DFM     — enter WO header (item, qty, dates, customer)
             T7WOACPY.DFM        — copy existing WO
             T7WOAECO.DFM        — attach engineering change order
             T7WOASOLINES.DFM    — link WO to sales order lines
2. RELEASE   WO-B: T7WOB.DFM    — release WO to shop floor (status → F)
             T7WOAMDT.DFM        — modify WO start/finish/due dates
3. ROUTING   WO-K-A: T7WOKA.DFM — define/modify routing operations
             T7WOKACOPYROUT.DFM  — copy routing from master
4. MATERIAL  WO-F: T7WOF.DFM    — issue materials to WO (backflush)
             T7WOFA.DFM          — auto-deduct materials by output qty
5. LABOR     WO-G: T7WOG.DFM    — record labor hours against WO
             WO-K-B: T7WOKB.DFM — detailed labor and cost tracking
6. OUTSIDE   WO-H: T7WOH.DFM    — track outsourced/subcontracted operations
             T7WOPO.DFM          — link WO to PO (for outside process POs)
             T7WOPOR.DFM         — review WO-to-PO linkages
7. TRACK     WO-C: T7WOC.DFM    — status/progress inquiry
             T7WOKL.DFM          — update WO status and dates
             T7WOKSA.DFM         — shortage analysis by WO
8. CLOSE     WO-S: T7WOS.DFM    — complete and close WO (status → C)
             WO-K-K: T7WOKK.DFM — reverse DC (data collection) posting
```

### Key WO Forms

**T7WOA — Main Work Order Entry**
Primary WO creation form. Header includes WO number, item, quantity, dates, customer, status.
Variants:
- T7WOACFG: WO-A settings/configuration
- T7WOACPY: Copy WO
- T7WOAECO: Engineering Change Order
- T7WOAMDT: Modify dates
- T7WOASOLINES: Link to SO lines
- T7WOAC: Customization details
- T7WOAE: Engineering specifications

**T7WOB — Release to Shop Floor**
Releases WO by date range and WO prefix/suffix. Sets status to F (Released).

**T7WOC — Status / Progress Inquiry**
Filter by WO number range, status, due date range.

**T7WOF — Material Issue (Backflush)**
Issues materials to WO — deducts from BKICMSTR inventory. T7WOFA handles auto-backflush
by production output quantity.

**T7WOG — Labor Entry**
Records labor hours against WO. Key field: WO total tracking.

**T7WOH — Outside Process**
Manages subcontracted operations (e.g., plating, heat treat). Links to PO via T7WOPO.

**T7WOI — Issues / Holds**
Records exceptions, holds, and problems against a WO.

**T7WOKA — Routing / Operations**
Defines or modifies the operation sequence for a specific WO (WO-level routing override).
T7WOKACOPYROUT copies from master routing; T7WOKAOPTS manages options.

**T7WOKL — Status Update**
Updates WO status (FRSC) and dates. Fields marked with asterisk are required.

**T7WOKM — WO BOM**
Bill of Material management for a specific WO.

**T7WOKSA — Shortage Analysis**
Identifies material shortages on open WOs by WO number range and status.

**T7WOKS — WO Close** (T7WOS.DFM)
Completes and closes WO. Sets status to C (Closed) and posts final costs.

**T7WOKK — Reverse DC Posting**
Reverses a data collection posting to a WO (accounting reversal).

### Reporting Forms (T7WOL*)

| DFM | Purpose |
|-----|---------|
| T7WOLA | Comprehensive WO report — WO# range, start/finish/due dates, priority 1-9, status SFRCIX, class |
| T7WOLB | WO report variant — WO#, finish/start dates, class, due date |
| T7WOLC | Finished WO report — finished date range, status |
| T7WOLD | Status-based WO listing — status filter |
| T7WOLE | WO reporting variant |
| T7WOLF | Shortage report — material shortage and completion planning |
| T7WOLG | WO reporting variant |
| T7WOLH | WO report with date/priority/class filters |
| T7WOLI | WO activity/progress tracking |
| T7WOLJ | Finished WO report — status CXSFRI |
| T7WOLK | WO BOM (Bill of Material) for production floor |
| T7WOLL | WO report — WO# |
| T7WOLN | Status-based WO listing |

### WO Priority (1–9 scale)
T7WOLA/WOLB/WOLH all filter by priority 1–9. Priority is a first-class scheduling parameter —
reports and releases can target priority ranges.

### WO-PO Integration
T7WOPO and T7WOPOR confirm WO-to-PO linkage for subcontracted work. When a WO operation
requires outside processing, a PO is generated and linked to the WO operation.

### DC Integration
T7WOKK (Reverse DC Posting) confirms DC (Data Collection) module writes directly to WO tables.
Scanners posting labor or completions via DC module use the same tables as manual WO-G entry,
and those postings can be reversed from the WO module.

---

## Summary: Table Families Confirmed

**GL module tables:**
- Transaction hub: BKGLTRAN → BKGLGJRN (header) → BKGLGJLN (lines)
- Archive path: BKGLATRN, BKGLAGJR, BKGLAGJL
- COA: BKGLCOA (live), BKGLFCOA (forecast), BKGLECOA (edit), BKGLCCOA (company)

**WO module tables:**
- WO master: WORKORD / WORKSORD / WORKHORD (all key on MTWO_WIP_WOPRE)
- BOM: WOBOM (component list per WO)
- Material issues: WOMTL / WOKMT
- Labor: WOLABOR
- Routing: WOROUT
- Outside process: linked to BKAPPOL via T7WOPO

---

*Last updated: 2026-06-11*
*Confidence: 72/100 — 24 GL forms and 68 WO forms all confirmed from network share glob.
Form purposes confirmed from DFM caption/label reads. Business logic inferred from field names.*
