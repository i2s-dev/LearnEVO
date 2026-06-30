# General Ledger (GL)

Status: verified | Pass 333 (2026-06-26)

- **Module code**: `GL`
- **Tables**: 28 (prefixes `BKGL`)
- **UI forms**: 24 (prefixes `T7GL`, `T6GL`, `BKGL`)
- **Menu operations**: 16

## Menu operations

| Code | Operation | Legacy module file(s) |
| ---- | --------- | --------------------- |
| `GL-A` | Edit Budgets | BKGLA |
| `GL-B` | Add new GJ Transaction | BKGLB |
| `GL-D` | Print Journals | BKGLD |
| `GL-F` | Print Financial Statements | BKGLF |
| `GL-G` | Print GL Code and Description | BKGLG |
| `GL-H` | Print Chart of Accounts | BKGLH |
| `GL-I` | Print Check Register | BKGLI |
| `GL-J` | Reconcile Check Register | BKGLJ |
| `GL-K` | Transfer Bank Account Funds | BKGLK |
| `GL-M` | Generate Recurring GJ Transactions | BKGLM |
| `GL-N` | Print Custom Statements | BKGLN |
| `GL-O` | Print/Post GL Batches | BKGLO;t6glo |
| `GL-P` | Edit GL Batch Entries | BKGLP |
| `GL-Q` | Reverse Batch Posting | BKGLQ |
| `GL-R` | Business Status | ISBS |
| `GL-S` | View GL Journal Notes | BKGLS |

## UI forms (24)

**Note (Pass 313, 2026-06-25):** Several DFM files showed "0 fields, 1 control" in the auto-generated inventory — this was a parsing failure caused by the icon data detection logic. T7GLB.DFM was manually analyzed and contains many fields across 4 tabs. Same issue likely applies to T7GLARCH, T7GLBLIST, T7GLJ, T7GLL, T7GLQ, T7GLS.

| DFM file | Caption | fields | controls | tabs | Notes |
| -------- | ------- | -----: | -------: | ---: | ----- |
| `T7GLA.DFM` | GL-A | 113 | 162 | 0 | COA + budget edit; DISP.ACCT1-4[1-13] = 13 periods × 4 account segments |
| `T7GLARCH.DFM` |  | 2 | 19 | 0 | Archive trigger form — may have parse failure |
| `T7GLB.DFM` | GL-B | **~80** | **~180** | **4** | **Journal entry — 4 tabs (see below); parse was failing** |
| `T7GLBLIST.DFM` |  | 0 | 1 | 0 | Likely list/picker; parse may have failed |
| `T7GLC.DFM` | GL-C | 24 | 61 | 0 | Print filter: batch range, date ranges, GL account range, journal type |
| `T7GLD.DFM` | GL-D | 14 | 47 | 0 | Print journals |
| `T7GLE.DFM` | GL-E | 18 | 51 | 0 | Account balance inquiry |
| `T7GLE2.DFM` | GL-E | 15 | 39 | 0 | Account inquiry v2 |
| `T7GLESPEED.DFM` | GL-E | 16 | 48 | 0 | Speed entry variant |
| `T7GLF.DFM` | GL- F | 98 | 177 | 0 | Financial statements |
| `T7GLG.DFM` | GL-G | 6 | 25 | 0 | Print GL code/description list |
| `T7GLH.DFM` | GL- H | 16 | 36 | 0 | Print chart of accounts |
| `T7GLI.DFM` | GL- I | 12 | 40 | 0 | Print check register |
| `T7GLJ.DFM` |  | 0 | 1 | 0 | Bank reconciliation — parse may have failed |
| `T7GLJASK.DFM` | Change Location | 4 | 11 | 0 | Location picker dialog |
| `T7GLK.DFM` | GL- K | 13 | 42 | 0 | Transfer bank funds |
| `T7GLL.DFM` |  | 0 | 1 | 0 | AP check void/GL reconcile — parse may have failed |
| `T7GLN.DFM` | GL- N | 40 | 87 | 0 | Custom statement layout |
| `T7GLO.DFM` | GL-O | 117 | 160 | 0 | Post GL batches |
| `T7GLOOB.DFM` | GL- O-OB | 5 | 27 | 0 | Out-of-balance finder |
| `T7GLP.DFM` | GL-P | 12 | 40 | 0 | Edit GL batch entries; BKGL.TRN.* fields confirmed |
| `T7GLQ.DFM` |  | 0 | 1 | 0 | Reverse batch posting — parse may have failed |
| `T7GLS.DFM` |  | 0 | 1 | 0 | View GL journal notes — parse may have failed |
| `T7GLT.DFM` | New Screen | 31 | 68 | 0 | Check/transaction print |

### T7GLB.DFM — GL Journal Entry Form (manually analyzed, Pass 313 2026-06-25)

4 tabs confirmed from DFM:

**Tab 1 — "GJ Trans List"** (browse mode)
- Grid shows journal transaction headers
- Fields: `BKGL.GJ.TRANSNM`, `BKGL.GJ.POSTED`, `BKGL.GJ.NUMLNES`, `BKGL.GJ.TRANSDT`, `BKGL.GJ.TYPE`, `BKGL.GJ.CVCODE`, `BKGL.GJ.CHKACT`, `BKGL.GJ.INVCHKN`, `TAGGED`
- Search and sort controls; date search field (FSD)

**Tab 2 — "GJ Trans Details"** (header edit)
- Transaction Number (`TNUMSTR`), Transaction Type 1-5 (`BKGL.GJ.TYPE`), Description (`TYPE.DESC`)
- Transaction Date (`BKGL.GJ.TRANSDT`), Bank Account 1-99 (`Adsp.chkact`)
- GJ Transaction Code (`BKGL.GJ.CVCODE`), Deposit/Check Number (`BKGL.GJ.INVCHKN`)
- Job Number (`BKGL.GJ.JOB`), Type Name combo (`BKGL.GJ.TYPEN`)
- Button: "Default Jobs"

**Tab 3 — "Trans Line Items"** (line item list)
- Grid: `LINE.ACCT`, `LINE_GLDPT`, `LINE.DESC`, `DR.DISP`, `CR.DISP`, `LINE.JOB`
- Summary panel: Transaction Number, Transaction Date, Code, Check Number, Bank (EDIT.BANK/BANKNAME/BANKGL), "Needed to balance" (`NEEDBAL.AMT`, `NEEDBAL.TYPE`)

**Tab 4 — "Trans Line Item Details"** (line item edit)
- GL Account (`EDIT.ACCT`), Line Description (`EDIT.DESC`), Department (`EDIT.DEPT`)
- Amount (`EDIT.AMT`), D/C indicator (`EDIT.DC`), Job Number (`EDIT.JOB`)
- Default Description (`DFLT_DESC`), Check/Invoice Number (`TICSTR`)
- Context display: Bank account info, needed-to-balance amount
- Bottom bar: Transaction Number, Type, Date (`TNUMSTR_2`, `TYPE.DESC2`, `BKGL.GJ.TRANSDT`)

## Database tables (28)

Full field details are in `../../../samples/ddf/schema.md` (see per-table heading).

| Table | File on disk | Fields | Key fields (first 3) |
| ----- | ------------ | -----: | -------------------- |
| **BKGLACHK** | `BKGLACHK.B` | 11 | `BKGL_CHK_CHKACT`, `BKGL_CHK_NUM`, `BKGL_CHK_DATE` |
| **BKGLAGJL** | `BKGLAGJL.B` | 9 | `BKGL_GJL_TRANSN`, `BKGL_GJL_ACCTNM`, `BKGL_GJL_GLDPT` |
| **BKGLAGJR** | `BKGLAGJR.B` | 11 | `BKGL_GJ_TRANSDT`, `BKGL_GJ_TRANSNM`, `BKGL_GJ_TYPE` |
| **BKGLATRN** | `BKGLATRN.B` | 16 | `BKGL_TRN_GLACCT`, `BKGL_TRN_GLDPT`, `BKGL_TRN_DATE` |
| **BKGLCCOA** | `BKGLCCOA.B` | 62 | `BKGLC_ACCT`, `BKGLC_GLDPT`, `BKGLC_ACCTD` |
| **BKGLCHK** | `BKGLCHK.B` | 11 | `BKGL_CHK_CHKACT`, `BKGL_CHK_NUM`, `BKGL_CHK_DATE` |
| **BKGLCOA** | `BKGLCOA.B` | 65 | `BKGL_ACCT`, `BKGL_GLDPT`, `BKGL_ACCTD` |
| **BKGLDESC** | `BKGLDESC.B` | 5 | `BK_DESC_CODE`, `BK_DESC_NUM`, `BK_DESC_LINE` |
| **BKGLECOA** | `BKGLECOA.B` | 65 | `BKGL_ACCT`, `BKGL_GLDPT`, `BKGL_ACCTD` |
| **BKGLETRN** | `BKGLETRN.B` | 16 | `BKGL_TRN_GLACCT`, `BKGL_TRN_GLDPT`, `BKGL_TRN_DATE` |
| **BKGLFCOA** | `BKGLFCOA.B` | 65 | `BKGL_ACCT`, `BKGL_GLDPT`, `BKGL_ACCTD` |
| **BKGLFSTL** | `BKGLFSTL.B` | 12 | `BKFS_NAME`, `BKFS_LINE_NUM`, `BKFS_SGL_ACCT` |
| **BKGLGJLN** | `BKGLGJLN.B` | 9 | `BKGL_GJL_TRANSN`, `BKGL_GJL_ACCTNM`, `BKGL_GJL_GLDPT` |
| **BKGLGJRN** | `BKGLGJRN.B` | 11 | `BKGL_GJ_TRANSDT`, `BKGL_GJ_TRANSNM`, `BKGL_GJ_TYPE` |
| **BKGLHIST** | `BKGLHIST.B` | 16 | `BKGL_TRN_GLACCT`, `BKGL_TRN_GLDPT`, `BKGL_TRN_DATE` |
| **BKGLICC** | `BKGLICC.B` | 11 | `BKGL_CHK_CHKACT`, `BKGL_CHK_NUM`, `BKGL_CHK_DATE` |
| **BKGLRGJL** | `BKGLRGJL.B` | 9 | `BKGL_GJL_TRANSN`, `BKGL_GJL_ACCTNM`, `BKGL_GJL_GLDPT` |
| **BKGLRGJR** | `BKGLRGJR.B` | 11 | `BKGL_GJ_TRANSDT`, `BKGL_GJ_TRANSNM`, `BKGL_GJ_TYPE` |
| **BKGLSTMT** | `BKGLSTMT.B` | 104 | `BKGL_STB_MN_TTL`, `BKGL_STB_GLA_MT`, `BKGL_STB_GLA_F_1` |
| **BKGLTEMP** | `BKGLTEMP.B` | 16 | `BKGL_TRN_GLACCT`, `BKGL_TRN_GLDPT`, `BKGL_TRN_DATE` |
| **BKGLTGJL** | `BKGLTGJL.B` | 9 | `BKGL_GJL_TRANSN`, `BKGL_GJL_ACCTNM`, `BKGL_GJL_GLDPT` |
| **BKGLTGJR** | `BKGLTGJR.B` | 11 | `BKGL_GJ_TRANSDT`, `BKGL_GJ_TRANSNM`, `BKGL_GJ_TYPE` |
| **BKGLTMP** | `BKGLTMP.B` | 16 | `BKGL_TRN_GLACCT`, `BKGL_TRN_GLDPT`, `BKGL_TRN_DATE` |
| **BKGLTMP2** | `BKGLTMP2.B` | 16 | `BKGL_TRN_GLACCT`, `BKGL_TRN_GLDPT`, `BKGL_TRN_DATE` |
| **BKGLTMP3** | `BKGLTMP3.B` | 16 | `BKGL_TRN_GLACCT`, `BKGL_TRN_GLDPT`, `BKGL_TRN_DATE` |
| **BKGLTRAN** | `BKGLTRAN.B` | 16 | `BKGL_TRN_GLACCT`, `BKGL_TRN_GLDPT`, `BKGL_TRN_DATE` |
| **BKGLX** | `BKGLX.B` | 20 | `BKGLX_POSTDATE`, `BKGLX_ARCHDATE`, `BKGLX_ENTDATE` |
| **BKGLXH** | `BKGLXH.B` | 20 | `BKGLX_POSTDATE`, `BKGLX_ARCHDATE`, `BKGLX_ENTDATE` |

## BKGLCOA — Chart of Accounts (65 fields, confirmed from DDF, Pass 110e 2026-06-19)

Primary key: `BKGL_ACCT` (10) + `BKGL_GLDPT` (4)

**Design pattern:** 14-period financial data stored directly in the account record, not in a separate transaction table. Each account carries current-year, budget, 1-year-prior, and 2-year-prior balances for all 14 periods (12 months + 2 adjustment periods), plus the prior year-end balances.

| Field(s) | Type | Size | Meaning |
|----------|------|------|---------|
| `BKGL_ACCT` | STRING | 10 | GL account code (PK part 1) |
| `BKGL_GLDPT` | STRING | 4 | GL department (PK part 2) |
| `BKGL_ACCTD` | STRING | 25 | Account description |
| `BKGL_TYPE` | STRING | 1 | Account type: A=Asset, L=Liability, O=Owners Equity, I=Income/Revenue, E=Expense/Cost |
| `BKGL_CR_DR` | STRING | 1 | Normal balance: C=Credit, D=Debit |
| `BKGL_NON_CASH` | STRING | 1 | Non-cash account flag (depreciation, etc.) |
| `BKGL_CURRENT_1..14` | FLOAT×14 | 8 | Current year period balances (periods 1–12 + 2 adjusting) |
| `BKGL_BUDGET_1..14` | FLOAT×14 | 8 | Budget amounts per period |
| `BKGL_1YPAST_1..14` | FLOAT×14 | 8 | Prior year period actuals |
| `BKGL_2YPAST_1..14` | FLOAT×14 | 8 | Two years ago period actuals |
| `BKGL_EXTRA` | STRING | 50 | User-defined extra field |
| `BKGL_1YPAST_YE` | FLOAT | 8 | Prior year year-end balance |
| `BKGL_2YPAST_YE` | FLOAT | 8 | Two-years-ago year-end balance |

**Period numbering:** Periods 1–12 = fiscal months; periods 13–14 = adjusting/closing entries. EvoERP supports 14-period fiscal years (12 regular + 2 closing periods).

**Notes:** The trial balance, income statement, and balance sheet are all derived directly from BKGLCOA by summing CURRENT_1..N for the selected date range. Transaction detail lives in BKGLTRAN. Variance calculations compare CURRENT vs BUDGET or CURRENT vs 1YPAST.

## BKGLTRAN — GL Transaction Journal (16 fields, confirmed from DDF schema.md, Pass 111c 2026-06-19)

Primary key: `BKGL_TRN_GLACCT` + `BKGL_TRN_GLDPT` + `BKGL_TRN_DATE` (composite — not unique; table is a detail log)

The permanent record of every GL posting. All sub-ledger modules (AR, AP, IC, WO, PR) write rows here when they post. GL-O also writes rows from manually-entered General Journal batches.

**Identical 16-field schema shared by:** BKGLTRAN (current), BKGLATRN (archive), BKGLHIST (history), BKGLETRN (extended/errors — purpose unknown), BKGLTEMP / BKGLTMP / BKGLTMP2 / BKGLTMP3 (temporary work tables during GL-O batch posting).

| Field | Type | Meaning |
|-------|------|---------|
| `BKGL_TRN_GLACCT` | STRING 10 | GL account code |
| `BKGL_TRN_GLDPT` | STRING 4 | GL department |
| `BKGL_TRN_DATE` | DATE | Transaction date |
| `BKGL_TRN_CODE` | STRING 10 | Source entity code (vendor, customer, employee, etc.) |
| `BKGL_TRN_INVC` | STRING 10 | Invoice or document number |
| `BKGL_TRN_DESC` | STRING 25 | Description |
| `BKGL_TRN_DC` | STRING 1 | Debit (D) or Credit (C) |
| `BKGL_TRN_AMT` | FLOAT | Transaction amount |
| `BKGL_TRN_TYPE` | STRING 2 | Journal/source type — see confirmed type code table below |
| `BKGL_TRN_ENTDTE` | DATE | Entry date (when entered, may differ from transaction date) |
| `BKGL_TRN_EXTRA` | STRING 25 | Extra / user-defined |
| `BKGL_TRN_TRXN` | FLOAT | Transaction sequence number |
| `BKGL_TRN_POST` | STRING 1 | Posted flag (Y = posted to COA balances) |
| `BKGL_TRN_PERIOD` | UBINARY 2 | Fiscal period number (1–14) |
| `BKGL_TRN_BATCH` | FLOAT | Batch number (GL-O batch reference) |
| `BKGL_TRN_PART` | STRING 15 | Part/item code (for inventory-related GL entries) |

**BKGLTRAN.TYPE — all 9 confirmed codes (from BKGLO.RUN binary analysis, Pass 321 2026-06-26):**

| Code | Label (from GL-O batch UI) | Source |
|------|---------------------------|--------|
| `GJ` | General Journal | GL-B manual journal entries (also used for Beginning Balance) |
| `CR` | Cash Receipts | GL-B Cash Receipts journal |
| `CD` | Cash Disbursements | GL-B Cash Disbursements journal |
| `YE` | Year End | GL-O year-end close entries to Retained Earnings |
| `RS` | Sales | AR/SO module postings to GL |
| `RP` | Purchases | AP/PO module postings to GL |
| `PR` | Payroll | Payroll module postings to GL |
| `OT` | Other | Miscellaneous module postings (IC, FA, etc.) |
| `WO` | Work Orders | Work Order module postings to GL |

Note: `TT` (Transaction Template) is a pre-posting state only — templates are converted to type `GJ` before being posted. Beginning Balance entries also use type `GJ`.

**Notes:**
- BKGLTRAN rows are the transaction detail; BKGLCOA accumulates the period totals. The trial balance is read from BKGLCOA, but BKGLTRAN provides the drill-down detail.
- POST flag distinguishes batches staged in BKGLTEMP (not yet posted) from committed entries in BKGLTRAN.
- BKGLATRN is the prior-year archive (GL period-end close copies and clears BKGLTRAN → BKGLATRN).
- BKGLTMP and BKGLTMP2 are temporary work tables used during GL-O batch post processing (confirmed from BKGLO.RUN strings `BKGLTMPA` / `bkgltmp2A`).

---

## TAS6-era GL programs (20 BKGL*.RUN — binary analyzed Pass 321 2026-06-26)

All 20 TAS6 .RUN programs found on DBAMFG$ share. Each has T7GL* counterpart in T7 generation.

| File | Size | Menu op | Purpose (from binary strings) |
|------|------|---------|-------------------------------|
| `BKGLA.RUN` | 160 KB | GL-A | View/edit Chart of Accounts; budget entry |
| `BKGLB.RUN` | 266 KB | GL-B | Enter/Post General Journal transactions (GJ/CR/CD/TT/BB entry) |
| `BKGLC.RUN` | ~50 KB | GL-C | Print GL transactions (report) |
| `BKGLD.RUN` | ~80 KB | GL-D | Print journals; displays "Net Balance" |
| `BKGLE.RUN` | ~120 KB | GL-E | Print detailed/summary Trial Balance |
| `BKGLF.RUN` | ~100 KB | GL-F | Print Financial Statements (Income Stmt / Balance Sheet) |
| `BKGLG.RUN` | ~40 KB | GL-G | Print GL code and description list |
| `BKGLH.RUN` | ~60 KB | GL-H | Print Chart of Accounts (period comparison table) |
| `BKGLI.RUN` | ~80 KB | GL-I | Print Check Register |
| `BKGLJ.RUN` | ~130 KB | GL-J | Reconcile Check Register (bank reconciliation) |
| `BKGLK.RUN` | ~90 KB | GL-K | Transfer Bank Account Funds (multi-currency) |
| `BKGLL.RUN` | 3 KB | GL-L | Stub launcher → calls BKGLB (cfrom parameter variant) |
| `BKGLM.RUN` | ~50 KB | GL-M | Generate Recurring GJ Transactions from BKGLRGJR |
| `BKGLN.RUN` | ~100 KB | GL-N | Print Custom Financial Statements |
| `BKGLO.RUN` | 258 KB | GL-O | Print/Post GL Batches (9-type batch selector, year-end close) |
| `BKGLOOB.RUN` | ~30 KB | GL-OOB | Find out-of-balance GL transactions |
| `BKGLP.RUN` | ~80 KB | GL-P | Edit GL Batch Entries |
| `BKGLPURG.RUN` | ~40 KB | GL-PURG | Purge GL Transactions |
| `BKGLQ.RUN` | ~60 KB | GL-Q | Reverse Batch Posting |
| `BKGLS.RUN` | ~30 KB | GL-S | View GL Journal Notes |

**Key observations from binary string analysis:**

BKGLB.RUN transaction type selector confirms all 5 user-entry types:
```
General Journal      [GJ]
Cash Receipts        [CR]
Cash Disbursements   [CD]
Transaction Template [TT]   ← becomes GJ type when posted
Beginning Balance    [GJ]   ← Beginning Balance also stores as GJ type
```

BKGLO.RUN batch posting UI confirms all 9 selectable posting types:
```
Cash Receipts      CR     Other       OT
Cash Disbursements CD     Work Orders WO
Sales              RS     General Jrn GJ
Purchases          RP     Year End    YE
Payroll            PR
```

BKGLO.RUN also confirms `BKGLTMP`/`BKGLTMP2` as temporary staging tables during GL-O batch post, and `BKGLOOB.RUN` as an inline out-of-balance finder sub-call from GL-O.

---

## General Journal (GJ) table family

Manual journal entries (GL-B, GL-P) are staged as GJ batches before posting to BKGLTRAN via GL-O.

**Header tables (11 fields each — all identical schema):**

| Table | Role |
|-------|------|
| **BKGLGJRN** | Current GJ batch headers (active, unposted) |
| **BKGLAGJR** | Archived GJ headers (posted/completed) |
| **BKGLRGJR** | Recurring GJ templates (GL-M generates from these) |
| **BKGLTGJR** | Temporary GJ work table during GL-O processing |

GJ header fields:

| Field | Type | Meaning |
|-------|------|---------|
| `BKGL_GJ_TRANSDT` | DATE | Transaction date |
| `BKGL_GJ_TRANSNM` | FLOAT | Transaction/batch number (PK) |
| `BKGL_GJ_TYPE` | STRING 2 | Journal type: GJ, AP, AR, etc. |
| `BKGL_GJ_TYPEN` | UBINARY 2 | Type number |
| `BKGL_GJ_POSTED` | STRING 1 | Posted flag |
| `BKGL_GJ_CVCODE` | STRING 10 | Customer/vendor/entity code |
| `BKGL_GJ_INVCHKN` | FLOAT | Invoice or check number |
| `BKGL_GJ_NUMLNES` | UBINARY 2 | Number of lines in this batch |
| `BKGL_GJ_CHKACT` | UBINARY 2 | Check account number |
| `BKGL_GJ_JOB` | STRING 15 | Job cost number |
| `BKGL_GJ_EXTRA` | STRING 50 | Extra / user-defined |

**Line tables (9 fields each — all identical schema):**

| Table | Role |
|-------|------|
| **BKGLGJLN** | Current GJ batch lines |
| **BKGLAGJL** | Archived GJ lines |
| **BKGLRGJL** | Recurring GJ template lines |
| **BKGLTGJL** | Temporary GJ lines during GL-O |

GJ line fields:

| Field | Type | Meaning |
|-------|------|---------|
| `BKGL_GJL_TRANSN` | FLOAT | FK → GJ header TRANSNM |
| `BKGL_GJL_ACCTNM` | STRING 10 | GL account code |
| `BKGL_GJL_GLDPT` | STRING 4 | GL department |
| `BKGL_GJL_DESC` | STRING 25 | Line description |
| `BKGL_GJL_DC` | STRING 1 | Debit (D) or Credit (C) |
| `BKGL_GJL_AMOUNT` | FLOAT | Line amount |
| `BKGL_GJL_JOB` | STRING 15 | Job cost number |
| `BKGL_GJL_LINE` | UBINARY 2 | Line number within batch |
| `BKGL_GJL_EXTRA` | STRING 50 | Extra / user-defined |

---

## BKGLX / BKGLXH — Extended GL Cross-Reference (20 fields, confirmed from DDF schema.md, Pass 111c 2026-06-19)

BKGLX = current; BKGLXH = history. Both identical 20-field schema.

Not keyed on GL account — keyed on dates + part code. This is a cross-reference table that lets you find all GL activity for a given part number, WO, PO, or SO, regardless of which account it posted to.

| Field | Type | Meaning |
|-------|------|---------|
| `BKGLX_POSTDATE` | DATE | Posting date |
| `BKGLX_ARCHDATE` | DATE | Archive date |
| `BKGLX_ENTDATE` | DATE | Entry date |
| `BKGLX_PART` | STRING 15 | Part/item code |
| `BKGLX_QUANTITY` | FLOAT | Quantity (for inventory transactions) |
| `BKGLX_AMOUNT` | FLOAT | Dollar amount |
| `BKGLX_TRXNTYPE` | STRING 1 | Transaction type code |
| `BKGLX_JOURNAL` | STRING 2 | Source journal type (AP, AR, WO, etc.) |
| `BKGLX_WOPRE` | FLOAT | Work order prefix |
| `BKGLX_WOSUF` | UBINARY 2 | Work order suffix |
| `BKGLX_PONUM` | FLOAT | Purchase order number |
| `BKGLX_SOINVC` | FLOAT | Sales order invoice number |
| `BKGLX_POINVC` | STRING 10 | AP invoice number (from PO receipt) |
| `BKGLX_DESC` | STRING 30 | Description |
| `BKGLX_TRXN` | FLOAT | Transaction sequence number |
| `BKGLX_BATCH` | FLOAT | Batch number |
| `BKGLX_POST` | STRING 1 | Posted flag |
| `BKGLX_COMPANY` | STRING 2 | Company code (multi-company) |
| `BKGLX_ICLASS` | STRING 4 | Item class (product line grouping) |
| `BKGLX_CCLASS` | STRING 4 | Cost class |

**Purpose:** BKGLX is the "drill-back" cross-reference — given a part number, you can find all GL activity (what it cost to make, what it sold for, what it was purchased for) without scanning all of BKGLTRAN. BKGLXH is the history archive.

---

## BKGLDESC — GL Notes/Description Table (5 fields)

| Field | Type | Meaning |
|-------|------|---------|
| `BK_DESC_CODE` | STRING 15 | Entity code (vendor, customer, account, etc.) |
| `BK_DESC_NUM` | FLOAT | Document number |
| `BK_DESC_LINE` | UBINARY 2 | Line number (PK part 3) |
| `BK_DESC_NOTES` | STRING 70 | Notes text |
| `BK_DESC_DESC` | STRING 25 | Short description |

Likely a multi-line notes attachment table for GL journal entries — the same 5-field schema also appears as BKAPADSC, BKAPDESC, BKAPHDSC in the AP module, suggesting it is a shared notes pattern.

---

## GL posting workflow

```
Sub-ledger posts (AR, AP, IC, WO, PR, PO):
  → Each module writes BKGLTRAN rows directly on posting
  → Updates BKGLCOA.CURRENT_N (period N) += amount
  → Also writes BKGLX row if part-based transaction

Manual General Journal (GL-B / GL-P):
  → Create/edit GJ batch: BKGLGJRN header + BKGLGJLN lines
  → Debits must equal credits (balanced batch check)
  → POSTED = N until GL-O runs

GL-O: Print/Post GL Batches
  → Copy BKGLGJLN → BKGLTEMP for validation
  → On confirm: write BKGLTRAN rows (one per GJ line)
  → Update BKGLCOA.CURRENT_N += amount
  → Move BKGLGJRN/BKGLGJLN → BKGLAGJR/BKGLAGJL (archived)

GL-M: Generate Recurring GJ Transactions
  → Read BKGLRGJR/BKGLRGJL templates
  → Create new BKGLGJRN/BKGLGJLN batch (date-stamped)
  → Ready for GL-O posting

Period-end close (GL-P/GL-O cycle):
  → Enter adjusting entries in periods 13–14 (BKGLCOA.CURRENT_13/14)
  → Print financials (GL-F reads BKGLCOA directly)
  → Year-end close: copy CURRENT_1..14 → 1YPAST_1..14 (shifting 1YPAST → 2YPAST)
  → Zero out CURRENT_1..14 for revenue/expense accounts
  → Carry balance-sheet accounts forward
  → Archive BKGLTRAN → BKGLATRN
```

---

## GL table family summary

| Table | Fields | Role |
|-------|-------:|------|
| **BKGLCOA** | 65 | Chart of accounts — period balances (current + 2 prior years) |
| **BKGLECOA** | 65 | Extended COA (same schema — possibly multi-company or EE company) |
| **BKGLFCOA** | 65 | Financial COA (same schema — possibly mapped for financial statements) |
| **BKGLCCOA** | 62 | Consolidated COA (3 fewer fields — purpose TBD) |
| **BKGLTRAN** | 16 | GL transaction journal — permanent record |
| **BKGLATRN** | 16 | Archive transactions (prior year) |
| **BKGLHIST** | 16 | History transactions (2+ years old) |
| **BKGLETRN** | 16 | Extended/error transaction staging — purpose TBD |
| **BKGLTEMP/BKGLTMP/BKGLTMP2/BKGLTMP3** | 16 | Temp tables during GL-O batch posting |
| **BKGLGJRN** | 11 | General journal batch headers (active) |
| **BKGLGJLN** | 9 | General journal batch lines (active) |
| **BKGLAGJR** | 11 | Archived GJ headers |
| **BKGLAGJL** | 9 | Archived GJ lines |
| **BKGLRGJR** | 11 | Recurring GJ templates (headers) |
| **BKGLRGJL** | 9 | Recurring GJ templates (lines) |
| **BKGLTGJR** | 11 | Temporary GJ headers during GL-O |
| **BKGLTGJL** | 9 | Temporary GJ lines during GL-O |
| **BKGLX** | 20 | Extended cross-reference (part/WO/PO/SO → GL) |
| **BKGLXH** | 20 | Extended cross-reference history |
| **BKGLDESC** | 5 | GL notes attachment table |
| **BKGLFSTL** | 12 | Financial statement layout lines |
| **BKGLSTMT** | 104 | Statement definition/template (104f — large) |
| **BKGLCHK** | 11 | Check register (current) |
| **BKGLACHK** | 11 | Check register (archive) |
| **BKGLICC** | 11 | Intercompany check register — purpose TBD |

---

## Programs (22 total) — Pass 259 (2026-06-25)

Source: `samples/rwn_symbols.json` — all T7GL* entries.

| Program | Procs | Lib | Menu | Role |
|---------|-------|-----|------|------|
| T7GLA.RWN | 69 | LISTG60.LIB | GL-A | COA editor + budget setup; opens BKGLCOA+ISGLCOA+ISGLNBGT; BKGL.NO.CASH/NON.CASH flags |
| T7GLB.RWN | 215 | LISTG60.LIB | GL-B | Main journal entry (GJ/CR/CD/TT/YE types); BKGLGJRN+BKGLGJLN+BKGLCHK+ISBANKS+ISJOB |
| T7GLC.RWN | 129 | LISTG60.LIB | GL-C | Transaction inquiry/report: BKGLTRAN browser; BKGL.TRN.* namespace |
| T7GLD.RWN | 132 | EVO.LIB | GL-D | Print journals / account detail: BKGLTRAN+BKAPDESC |
| T7GLE.RWN | 191 | LISTG60.LIB | GL-E | Account balance inquiry: ISGLCOA+ISGLDATE period-based view; BKGL.TRN.* |
| T7GLE2.RWN | 156 | LISTG60.LIB | GL-E | Account inquiry v2: adds BKARINVL access (AR-linked GL entry view) |
| T7GLESPEED.RWN | 164 | LISTG60.LIB | GL-E | Speed entry variant: TASCOLOR = color-coded fast GL entry |
| T7GLF.RWN | 189 | EVO.LIB | GL-F | Financial statements: BKGLSTMT+ISGLNBGT; BKGL.STB.* (Balance Sheet) + BKGL.STC.* (Income Stmt) vars |
| T7GLG.RWN | 99 | LISTG60.LIB | GL-G | Print GL code/description list: BKAPDESC+LANGDICT (descriptive COA print) |
| T7GLH.RWN | 99 | LISTG60.LIB | GL-H | Print chart of accounts: ISGLNBGT in DB (budget detail included) |
| T7GLI.RWN | 112 | LISTG60.LIB | GL-I | Print check register: BKGL.CHK.* vars; BKGLCHK+ISBANKS+ISBSF |
| T7GLJ.RWN | 171 | ISTECH.LIB | GL-J | Bank reconciliation: BKGL.CHK.* + ISBANKS+BKGLCHK+MKTRACK+ISACCESS |
| T7GLK.RWN | 102 | LISTG60.LIB | GL-K | Transfer bank funds: BKGL.CHK.* + ISMCF+ISMCR+ISBSF (multi-currency bank transfer) |
| T7GLL.RWN | 166 | LISTG60.LIB | — | AP check void/GL reconcile: BKGLCHK+ISBANKS+BKAPCHKF+BKAPINVL+BKAPINVT |
| T7GLN.RWN | 182 | LISTG60.LIB | GL-N | Custom statement layout: BKGLFSTL statement line definitions |
| T7GLO.RWN | 165 | EVO.LIB | GL-O | Post GL batches: BKGLTRAN+ISGLDATE+ISGLCOA+ISBSF+ISBANKS+ISMCF; BKGL.TRN.* + NON.CASH |
| T7GLOOB.RWN | 107 | EVO.LIB | GL-O-OB | Out-of-balance finder: ISACCESS access control; identifies debit≠credit batches |
| T7GLP.RWN | 87 | ISTECH.LIB | GL-P | Period-end batch edit: ISGLDATE; BKGL.TRN.TPE.TX (period-end tax type) |
| T7GLQ.RWN | 104 | ISTECH.LIB | GL-Q | Reverse batch posting: both BKGL.GJ.* + BKGL.CHK.* + BKGLGJRN+BKGLGJLN+BKGLCHK |
| T7GLS.RWN | 78 | EVO.LIB | GL-S | Recurring journal notes: BKGL.GJ.* vars + BKGLGJRN+ISNOTES |
| T7GLT.RWN | 120 | T7DBA.LIB | — | Check/transaction print: BKGLCHK+ISBANKS (print library) |
| T7GLARCH.RWN | 77 | EVO.LIB | — | Archive GL transactions: BKGLTRAN→BKGLATRN; ISGLDATE period gate; GL.REC var |

### Key BKGL.* Variable Namespaces (from T7GLB rwn_symbols.json)

**BKGL.GJ.*** — GJ batch header fields (11 vars):
`CHKACT / CVCODE / EXTRA / INVCHKN / JOB / NUMLNES / POSTED / TRANSDT / TRANSNM / TYPE / TYPEN`

**BKGL.GJL.*** — GJ batch line fields (9 vars):
`ACCTNM / AMOUNT / DC / DESC / EXTRA / GLDPT / JOB / LINE / TRANSN`

**BKGL.TRN.*** — GL transaction fields (17 vars):
`AMT / BATCH / CODE / DATE / DC / DESC / ENTDTE / EXTRA / GLACCT / GLDPT / INVC / KEY / PART / PERIOD / POST / TPE.TX / TRXN / TYPE`
(TPE.TX = period-end tax transaction type — T7GLP only)

**BKGL.CHK.*** — Check register fields (11 vars):
`AMT / CHKACT / CUST / DATE / DATER / EXTRA / FLAG / KEY / NAME / NUM / TYPE / VEND`

**BKGL.STB.***, **BKGL.STC.***, **BKGL.STI.*** — Financial statement row groups (T7GLF, Pass270 2026-06-25):
- **STB** = Balance Sheet: `GLA` (assets) / `GLL` (liabilities) / `GLO` (equity/other) — each with `.F` / `.MT` / `.T` (first-period / month-to-date / year-to-date total) + `GLATTL` / `GLLTTL` / `GLOTTL` totals
- **STC** = Cash/Comparison: `GLA` / `GLI` (income/inflow) / `GLL` / `GLN` (net) — each with `.F` / `.MT` / `.T` periods + totals
- **STI** = Income Statement: `GLC` (COGS) / `GLE` (expenses) / `GLI` (revenue/income) / `GLOE` (other exp) / `GLOI` (other inc) / `GLT` (total) — each with `.F` / `.MT` / `.T` periods + totals

BKGLSTMT (104f) stores pre-computed statement rows. The DDF key `BKGL_STB_GLA_F_1` subscript suggests multiple account-group rows per statement type. T7GLF is the sole accessor (189 procs). Exact multi-row encoding TBD.

### Additional IS-Prefixed Tables (discovered via T7GL* DB lists)

| Table | Appears In | Role |
|-------|-----------|------|
| ISGLCOA | T7GLA, T7GLE, T7GLO | IS version of GL Chart of Accounts (company-level COA override?) |
| ISGLDATE | T7GLE, T7GLO, T7GLP, T7GLARCH | GL period/date control: open/close state per fiscal period |
| ISGLNBGT | T7GLA, T7GLF, T7GLH | IS GL New Budget — budget planning table (separate from BKGLCOA.BUDGET_N) |
| ISBSF | T7GLI, T7GLK, T7GLO | Bank Statement Format — bank account configuration for reconciliation |
| ISMCF | T7GLK, T7GLO, T7POA | Multi-Currency Framework master (exchange rates + symbols) |
| ISJOB | T7GLB | Job costing table — GL entries can be tagged to a job number |

These tables are NOT in the standard BKBM/BKGL DDF families but appear consistently in GL DB file lists. Schemas are not confirmed from DDF.

---

## TAS6-era programs (BKGL*.RUN) — complete binary inventory (Pass 323, 2026-06-26)

20 TAS Pro 6 `.RUN` programs confirmed from binary string extraction. All files in `samples/`.

| File | Size | Menu code | Operation | Key tables |
|------|-----:|-----------|-----------|------------|
| `BKGLA.RUN` | 160 KB | GL-A | View Chart of Accounts (T6 = read-only view; T7GLA adds budget editing) | BKGLCOA, ISCOA, ISGLCOA, ISGLDATE, ISGLNBGT |
| `BKGLB.RUN` | 266 KB | GL-B | Enter/Post General Journal Transactions (types: GJ, CR, CD + Beginning Balance) | BKGLGJRN, BKGLGJLN, BKGLTGJR, BKGLTGJL, BKGLCHK, BKGLTRAN |
| `BKGLC.RUN` | 180 KB | GL-C-A | Convert AP to Long Invoice Numbers (data-migration utility; requires all users out) | BKAPINVT, BKAPINVL, BKAPCHKF, BKAPCHKH |
| `BKGLD.RUN` | 151 KB | GL-D | Print Journals | BKGLTRAN, BKGLCOA |
| `BKGLE.RUN` | 231 KB | GL-E | Enter/Edit GL Batch Entries (manual GL edits before posting) | BKGLTEMP, BKGLTRAN, BKGLCOA |
| `BKGLF.RUN` | 212 KB | GL-F | Print Financial Statements (requires AM-E format + AM-N period dates) | BKGLSTMT, BKGLFSTL, BKGLFCOA, ISGLBDGT, ISGLDATE |
| `BKGLG.RUN` | 139 KB | GL-G (+ AM-D) | Print GL Code and Description | BKGLCOA |
| `BKGLH.RUN` | 167 KB | GL-H | Print Chart of Accounts | BKGLCOA, ISCOA, ISGLCOA, ISGLDATE |
| `BKGLI.RUN` | 172 KB | GL-I | Print Check Register | BKGLCHK, ISBANKS, ISBSF |
| `BKGLJ.RUN` | 186 KB | GL-J | Reconcile Check Register (bank reconciliation) | BKGLCHK, BKGLCHKF, ISBANKS, ISBSF |
| `BKGLK.RUN` | 184 KB | GL-K | Transfer Bank Account Funds | BKGLCHK, BKGLCHKL, BKGLTRAN, BKGLX |
| `BKGLL.RUN` | 3 KB | (stub) | — references BKGLBA/BKGLLA; likely thin launcher | BKGLBA, BKGLLA |
| `BKGLM.RUN` | 44 KB | GL-M | Generate Recurring GJ Transactions | BKGLGJRN, BKGLGJLN, BKGLRGJR, BKGLRGJL, BKGLTRAN |
| `BKGLN.RUN` | 184 KB | GL-N | Print Custom/Budget Statements (requires AM-N period dates) | BKGLFSTL, BKGLFCOA, ISGLBDGT, ISGLDATE |
| `BKGLO.RUN` | 258 KB | GL-O (+ GL-P) | Print/Post GL Batches (filter: CR, CD, GJ, WO, PR, RS, OT) | BKGLTRAN, BKGLTEMP, BKAPINVL, BKAPINVT |
| `BKGLOOB.RUN` | 121 KB | (utility) | Find Out-of-Balance GL Transactions | BKGLTRAN, BKGLTEMP |
| `BKGLP.RUN` | 144 KB | GL-P | Post Batches to GL (locks: "Another user is Editing or Posting GL Batches") | BKGLTMP, BKGLTRAN, BKGLTEMP |
| `BKGLPURG.RUN` | 114 KB | GL-PURG | Purge GL Transactions | BKGLTRAN |
| `BKGLQ.RUN` | 51 KB | GL-Q | Reverse Batch Posting | BKGLTEMP, BKGLTRAN |
| `BKGLS.RUN` | 79 KB | GL-S | View/Print GL Journal Notes (also accesses WO tables: WOADSC, WOAWN, WOCALC — GL notes can reference WO activity) | BKGLGJRN |

### GL batch type codes — binary confirmed (Pass 323)

From BKGLB.RUN (entry screen picker) and BKGLO.RUN (post-batch filter screen):

| Code | Description | Source module | Confirmed from |
|------|-------------|--------------|----------------|
| **GJ** | General Journal | GL-B (manual entry) | BKGLB+BKGLO binary |
| **CR** | Cash Receipts | AR module (cash application) | BKGLB+BKGLO binary |
| **CD** | Cash Disbursements | AP module (check printing) | BKGLB+BKGLO binary |
| **WO** | Work Orders | WO module (labor/material costing) | BKGLO binary |
| **PR** | Payroll | PR module (payroll post via T7PRD) | BKGLO binary |
| **RS** | Revenue/Sales | SO module (invoice posting) | BKGLO binary |
| **OT** | Other | Miscellaneous / catch-all | BKGLO binary |
| **MR** | MRP | MRP module (confirmed Pass 321) | BKGLO.RUN Pass 321 |
| **JC** | Job Cost | JC module | BKGLO.RUN Pass 321 |
| **PI** | Physical Inventory | PI module | BKGLO.RUN Pass 321 |
| **VM** | Vendor Manual | Vendor manual check | BKGLO.RUN Pass 321 |

GL-B (manual entry) only allows GJ, CR, CD — the other codes are written automatically by their respective source modules when they call `EXEC_RB` against BKGLTRAN.

BKGLO.RUN batch-filter screen shows types CR, OT, CD, WO, RS, GJ, PR — the 7 "selectable" types; MR/JC/PI/VM also exist in BKGLTRAN but appear to lack their own batch-filter checkbox (posted-only, never shown in filter screen).

### ISBSF — Bank Statement Format (confirmed used by GL-I/J, 2026-06-26)

`ISBSF` appears in BKGLI.RUN and BKGLJ.RUN — it is the bank statement import/configuration table used for check register printing and bank reconciliation. Schema not yet confirmed from DDF (not in standard BKGL* family).

---

## Notes & open questions

- BKGLECOA / BKGLFCOA: Both have the same 65-field schema as BKGLCOA. One likely tracks the consolidated/entity company (EE); the other may be a financial-statement mapping layer. Not confirmed without RWN source.
- BKGLCCOA (62f) — 3 fields fewer than BKGLCOA. The missing fields are unknown; possibly the two year-end balance fields and one other.
- BKGLSTMT (104f): Large statement definition table — likely the custom financial statement layout used by GL-N. Schema not yet read.
- BKGLFSTL (12f): Financial statement layout lines — BKFS_NAME + LINE_NUM + SGL_ACCT as key. Likely the row definitions for GL-F printed statements.
- ISGLCOA / ISGLDATE / ISGLNBGT / ISBSF / ISMCF / ISJOB schemas: inferred from DB file list only; not in DDF.

---

## Pass 333 — additional BKGL\*.RUN binary findings (2026-06-26)

Re-extraction of all 20 `samples/BKGL*.RUN` files.

### Accessor reference confirmations

`BKGLOOB.RUN` and `BKGLQ.RUN` contain literal runtime accessor reference strings:
- `BKGL.TRN.TYPE  H` — confirms `BKGL_TRN_TYPE` is a 2-char string accessor (table handle code H)
- `BKGL.TRN.POST  o` (BKGLQ) and `BKSY.PRTR.POST  7` (BKGLS) — POST field accessor confirmed

### IS table archive variants

Binary opens from multiple programs confirm the IS table family has full A/I suffix variants:

| Table | Seen in | Inferred role |
|-------|---------|---------------|
| `ISGLCOAA` | BKGLA, BKGLF, BKGLH | IS GL COA archive |
| `ISGLDATEA` / `ISGLDATEI` | BKGLB, BKGLE, BKGLF | IS GL date period archive / index |
| `ISGLBDGTA` | BKGLF, BKGLN | IS GL budget archive |
| `ISGLNBGTI` | BKGLA, BKGLH | IS GL next-budget index |

### Additional BKGL table variants

| Table | Seen in | Role |
|-------|---------|------|
| `BKGLCOA0` | BKGLG | COA zero-department variant (no dept code — "All" accounts print) |
| `BKGLCHKF` | BKGLJ | Check register filter (bank reconciliation filtered view) |
| `BKGLCHKL` | BKGLK | Check register list (bank transfer context) |
| `BKGLXI` | BKGLK | GL cross-reference index (read by bank transfer program) |
| `BKGLOOBA` | BKGLO | Out-of-balance archive (unbalanced batch staging) |
| `BKGLGJRNL` | BKGLK | GJ recurring journal line (accessed during bank transfer) |

### GL-S dual mode

`BKGLS.RUN` binary contains both title strings:
- `"GL-S  Print GL Journal Notes"` (print mode)
- `"GL-S  View GL Journal Notes"` (view mode)

GL-S is a dual print/view program for journal notes — the menu shows only "View" but the program supports printing as well.

### BKGLF budget comparison modes

`BKGLF.RUN` confirms 4 historical budget comparison display modes:
- `0 - Four Year Budget Past Amounts`
- `7 - One Year Budget Past Amounts`
- `8 - Two Year Budget Past Amounts`
- `9 - Three Year Budget Past Amounts`

Combined with `B - Budget Amounts` (current budget) and `B - Balance Sheet`, GL-F supports up to 4 years of budget history comparison alongside current actuals.

### BKGLI check type codes

`BKGLI.RUN` check register picker confirms check type codes:
- `A - All Types` — print all check types
- `B - Both Types` — D (deposit) + C (check)
- `V - Voided Checks` — voided checks only

These match the `BKGL_CHK_TYPE` field in BKGLCHK (confirmed string 1 type from DDF).

---

## Live Data Analysis (Pass 417, 2026-06-30)

### BKGLCOA (Chart of Accounts) live statistics

2,185 account records (account+department combinations).

**Account type distribution (Pass 417, live-confirmed):**

| TYPE | Count | Meaning | Account range (i2S) |
|------|------:|---------|---------------------|
| `E` | 1,898 | Expense / Cost of Sales | 5000–9999 |
| `A` | 101 | Asset | 1000–1999 |
| `L` | 92 | Liability | 2000–2999 |
| `I` | 85 | Income / Revenue | 4000–4999 |
| `O` | 8 | Owners Equity | 3000–3999 |

**CORRECTION from prior documentation:** The type codes were previously listed as
A/L/E/R/C (Asset/Liability/Equity/Revenue/Cost). **This was wrong.** Live data confirms:
- `E` = Expense (1,898 accounts — clearly expense, not equity)
- `I` = Income/Revenue (85 accounts)
- `O` = Owners Equity (8 accounts — common stock, paid-in capital, retained earnings, current earnings)
- No `R` or `C` type codes exist in the live chart of accounts.

**Sample accounts per type:**
- Asset (A): 1112=CASH LITCHFIELD BANCORP, 1113=CASH i2 SYSTEMS CALIFORNI, 1114=BANK OF AMERICA
- Liability (L): 2110=ACCOUNTS PAYABLE, 2111=INVOICES RECEIVED NOT POSTED, 2115=CUSTOMER DEPOSITS
- Equity (O): 3000=COMMON STOCK, 3050=PAID IN CAPITAL, 3100=CURRENT EARNINGS
- Income (I): 4001=DRIVER CONTROL BOX, 4002=DRIVERS, 4003=LED FIXTURES (product line revenue)
- Expense (E): 5001=COST OF SALES, 5002=BAD DEBT/ASSET EXPENSE

**BKGLATRN (archived GL transactions): 0 records** — GL transactions have never been archived
at i2 Systems. All 2,965,096 transactions spanning 2016-2026 remain live in BKGLTRAN.
This is consistent with BKGLTRAN.PERIOD=0 (T7GLARCH period gate not exercised).
Contrast with AR: BKARHINV has 95,982 archived AR invoices — AR archiving IS used regularly.

### BKGLTRAN live statistics

Live DSN=DBA query: 2,965,096 records spanning 2016-12-31 to 2026-11-14.

**Type distribution (all records, POST='P' unless noted):**

| TYPE | Count | Module source | Notes |
|------|------:|--------------|-------|
| `WO` | 1,536,024 | Work Orders | Dominant — every WO cost posting (material, labor, overhead) |
| `RP` | 510,902 | Purchasing/AP | PO receipts to stock (Receiving Purchase) |
| `RS` | 460,109 | Sales/AR | SO invoice postings (Revenue/Sales) |
| `CD` | 161,098 | AP checks | Cash disbursements (check payments) |
| `OT` | 139,286 | Misc modules | Other/catch-all (IC adjustments, transfers, etc.) |
| `CR` | 89,231 | AR cash application | Cash receipts (AR payment postings) |
| `GJ` | 60,933 | GL-B/GL-O manual | General journal manual entries |
| `YE` (P) | 2,426 | GL-O year-end | Year-end close entries — posted |
| `YE` (N) | 4,300 | GL-O year-end | Year-end entries — NOT yet posted to COA |
| `JA` | 111 | Journal adjustment | Journal adjustment (JA type confirmed — not in original list) |
| `RP` (unposted) | 238 | AP | Staged/pending receipt postings |
| `CD` (unposted) | 219 | AP | Staged/pending disbursement postings |
| `RS` (unposted) | 128 | AR/SO | Staged/pending sales postings |
| `CR` (unposted) | 49 | AR | Staged/pending cash receipts |
| `OT` (unposted) | 34 | Misc | Staged/pending other |
| `GJ` (unposted) | 5 | GL | Staged/pending journal entries |
| `GL` | 2 | Direct GL | Direct GL entries (rare) |

**POST field values:** 'P'=posted to COA balances; ' '=staged/pending; 'N'=year-end not yet applied.

**BKGL_TRN_PERIOD:** 0 for ALL 2,965,096 records — **period-end close (T7GLP) is NOT used at
i2 Systems.** All transactions remain in "period 0" (unassigned period). The period-locking
mechanism exists in the code but is not exercised at this installation.

**BKGL_TRN_EXTRA format (confirmed from sample):** Stores `<USERNAME><SPACE><HH:MM:SS><SPACE><A/P>`
e.g., `'JFOOTE         12:14:51 P'` = user JFOOTE, 12:14:51 PM. Timestamp uses 12-hour format
identical to ISJAVA UID timestamp pattern.

**BKGL_TRN_BATCH:** numeric batch reference. Sample: 20424 — correlates to BKGLGJRN.TRANSNM
for GJ-type transactions posted via GL-O.

### BKGLGJRN (Journal Register) live statistics

14,035 records (active unposted + recently posted journal batches).

**Type distribution:**

| TYPE | TYPEN | Count | Meaning |
|------|------:|------:|---------|
| `CR` | 2 | 7,895 | Cash Receipts journals (AR cash application entries) |
| `GJ` | 1 | 5,350 | General Journals (manual DR/CR entries) |
| `CD` | 3 | 790 | Cash Disbursements (AP check printing entries) |

**TYPEN numeric codes confirmed:** 1=GJ, 2=CR, 3=CD. These match the T7GLB.DFM type picker.

**Sample BKGLGJRN record (most recent):**
- TRANSDT=2026-11-14, TRANSNM=14314, TYPE='CR', TYPEN=2
- CVCODE='JAN SWEEP' (batch sweep code — i2 sweeps AR cash monthly)
- INVCHKN=11426 (check/invoice number), NUMLNES=2, CHKACT=4 (bank account 4)
- POSTED='Y', JOB=null

**BKGLGJLN:** 52,848 lines total; avg 3.76 lines per journal batch.

### ISGLDATE (GL Period Gate) live structure

1 single row. 85 fields. Structure: 7 fiscal years × 12 periods each + FYDATE + EXTRA.

| Variable range | Live dates | Purpose |
|----------------|-----------|---------|
| `ISGL_CYDATE_1..12` | 2026-01-01 to 2026-12-01 | Current year period start dates |
| `ISGL_1YDATE_1..12` | 2025-01-01 to 2025-12-01 | Prior year 1 period dates |
| `ISGL_2YDATE_1..12` | 2024-01-01 to 2024-12-01 | Prior year 2 period dates |
| `ISGL_3YDATE_1..12` | 2023-01-01 to 2023-12-01 | Prior year 3 period dates |
| `ISGL_4YDATE_1..12` | 2022-01-01 to 2022-12-01 | Prior year 4 period dates |
| `ISGL_5YDATE_1..12` | 2021-01-01 to 2021-12-01 | Prior year 5 period dates |
| `ISGL_6YDATE_1..12` | 2020-01-01 to 2020-12-01 | Prior year 6 period dates (oldest retained) |
| `ISGL_FYDATE` | 2026-01-01 | Fiscal year start date (matches BKSYMSTR FISCAL_YR) |
| `ISGL_EXTRA` | '01/01/27...' | Next fiscal year start (stored as MM/DD/YY string in EXTRA field) |

All periods at i2 Systems use the 1st of each month = **standard monthly accounting periods**.
ISGLDATE is accessed by T7GLE (period-based balance inquiry), T7GLO (post to correct period),
T7GLP (edit period assignments), and T7GLARCH (archive by period gate).

**Key insight:** ISGLDATE stores period-start-date boundaries only — it is NOT a locked/unlocked
flag table. Period locking (preventing postings to prior periods) is enforced by T7GLP when it
writes BKGL_TRN_PERIOD; since all BKGLTRAN records have PERIOD=0, the period gate is bypassed
at i2 Systems — all postings go to the current (open) period regardless of date.

### BKGLCHK (Check Register) live statistics

40,654 records. Date range: 2004-05-27 to 2026-11-14.

`BKGL_CHK_TYPE` distribution:

| Type | Count | Interpretation |
|------|------:|----------------|
| `C` | 24,480 | Standard check (paper AP/AR check) |
| `D` | 13,802 | ACH / direct deposit disbursement |
| `X` | 1,231 | Cleared / reconciled (bank rec marked) |
| `V` | 1,141 | Voided check |

All bank activity since 2004 is retained live in BKGLCHK — no archive table `BKGLCHKH` has been
used. Fields confirmed: CHKACT (bank account number), CHK_NUM, CHK_DATE, CHK_TYPE, CHK_NAME,
CHK_AMT, CHK_FLAG, CHK_EXTRA, CHK_DATER (reconciliation date), CHK_VEND.

### BKGLX (GL Cross-Reference) live statistics

1,822,769 records. `BKGLXH` = 0 (cross-reference history never archived, same policy as BKGLATRN).

BKGLX is a per-transaction cross-reference linking GL postings back to source-module document
identifiers. Each row carries: POSTDATE, ARCHDATE, ENTDATE, PART (part number), QUANTITY, AMOUNT,
TRXNTYPE, JOURNAL (GL journal batch), WOPRE+WOSUF (work order number).

`BKGLX_TRXNTYPE` distribution:

| Type | Count | Likely source module |
|------|------:|----------------------|
| `I` | 1,138,587 | Inventory transaction (IN/IC) |
| `S` | 122,506 | Shipment / Sales Order (SO) |
| `P` | 117,526 | Purchase / Purchase Order (PO) |
| `W` | 108,226 | Work Order (WO) |
| `5` | 100,071 | Unknown numeric subtype |
| `L` | 96,030 | Labor / LW module |
| `A` | 61,524 | Assembly / BOM (BM) |
| `4` | 28,651 | Unknown numeric subtype |
| `6` | 25,794 | Unknown numeric subtype |
| `8` | 22,804 | Unknown numeric subtype |
| `J` | 365 | Journal entry (GL-B) |
| `O` | 277 | Other / miscellaneous |
| `F` | 233 | Financial (possibly FA fixed assets) |
| `D` | 151 | Direct / disbursement |
| `7` | 14 | Unknown numeric subtype |
| `E` | 10 | Expense |

**Key insight:** Inventory transactions dominate (62% of all cross-ref rows) — every IC transaction
generates a BKGLX row for drill-back. Numeric type codes ('4','5','6','7','8') are module-specific
subtypes not yet mapped to letter codes; require T7-era RWN decryption to identify definitively.
