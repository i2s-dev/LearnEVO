# FA — Fixed Assets

Status: verified | C: 92/100
Last updated: 2026-06-29 (Pass 377 — all 3 RWN programs decrypted and analyzed; complete field namespaces confirmed; GL posting workflow confirmed)

---

## Module Overview

The Fixed Assets module manages the full lifecycle of depreciable capital assets:
entry → periodic depreciation calculation → GL posting → reporting/export.

**5 menu codes:** FA-A (Enter Assets), FA-B (Post Depreciation), FA-C (List Depreciation Transactions), FA-D (List Assets), FA-E (Import/Export Assets)

**2 database tables:** ISFXASST (asset master, 23 fields), ISFXATRN (depreciation transactions, 12 fields)

**3 programs:** T7FAA.RWN (84 procs, LISTG60.LIB), T7FAB.RWN (69 procs, LISTG60.LIB), T7FAE.RWN (79 procs, EVO.LIB)

---

## FA-A — Enter Fixed Assets (T7FAA.RWN)

**Purpose:** Create and edit fixed asset master records.

**DB fingerprint:** ISFXASST, ISFXATRN, BKGLCOA (GL account lookup for validation)

**Fields entered per asset:**

| Field | TAS Var | DDF Field | Type | Notes |
|-------|---------|-----------|------|-------|
| Asset Number | IS.FXA.NUMBER | IS_FXA_NUMBER | FLOAT/8 | 6-digit identifier (PK) |
| Type | IS.FXA.TYPE | IS_FXA_TYPE | STRING/30 | Category: Vehicle, Equipment, etc. |
| Description | IS.FXA.DESC | IS_FXA_DESC | STRING/30 | Line 1 |
| Description 2 | IS.FXA.DESC2 | IS_FXA_DESC2 | STRING/30 | Line 2 |
| Cost Basis | IS.FXA.CSTBAS | IS_FXA_CSTBAS | FLOAT/8,2dec | Total acquisition cost |
| Residual Value | IS.FXA.RESVAL | IS_FXA_RESVAL | FLOAT/8,2dec | Salvage value (not depreciated) |
| Life | IS.FXA.LIFE | IS_FXA_LIFE | FLOAT/8 | Depreciable life in years |
| Method | IS.FXA.METH | IS_FXA_METH | STRING/30 | Depreciation method (e.g., SL, DB) |
| Asset GL Account | IS.FXA.GLA | IS_FXA_GLA | STRING/10 | Balance sheet asset account |
| Asset GL Dept | IS.FXA.GLD | IS_FXA_GLD | STRING/4 | |
| Accum Dep Account | IS.FXA.ACDEPA | IS_FXA_ACDEPA | STRING/10 | Accumulated depreciation (BS) |
| Accum Dep Dept | IS.FXA.ACDEPD | IS_FXA_ACDEPD | STRING/4 | |
| Dep Expense Account | IS.FXA.DEPEXPA | IS_FXA_DEPEXPA | STRING/10 | Depreciation expense (IS) |
| Dep Expense Dept | IS.FXA.DEPEXPD | IS_FXA_DEPEXPD | STRING/4 | |
| Start Date | IS.FXA.SDATE | IS_FXA_SDATE | DATE | Acquisition date |
| End Date | IS.FXA.EDATE | IS_FXA_EDATE | DATE | Disposal/fully-depreciated date |
| Proceeds from Sale | IS.FXA.SOLD | IS_FXA_SOLD | FLOAT/8,2dec | Sale proceeds on disposal |
| Accumulated Dep | IS.FXA.ACCUMDEP | IS_FXA_ACCUMDEP | FLOAT/8,2dec | Running accumulated depreciation |
| Serial Number | IS.FXA.SERIAL | IS_FXA_SERIAL | STRING/30 | Equipment serial # (optional) |
| Last Dep Amount | IS.FXA.LDEPAMT | IS_FXA_LDEPAMT | FLOAT/8,2dec | Most recent depreciation entry |
| Last Dep % | IS.FXA.LDEPPERC | IS_FXA_LDEPPERC | FLOAT/8,8dec | Most recent depreciation rate |
| Last Dep Date | IS.FXA.LDEPDATE | IS_FXA_LDEPDATE | DATE | Date of most recent posting |
| Extra | IS.FXA.EXTRA | IS_FXA_EXTRA | STRING/100 | User-defined |

**Key finding:** BKGLCOA is opened in FA-A for interactive F2 GL account validation — when entering Asset GL Account, Accum Dep Account, or Dep Expense Account, the user can browse the GL chart of accounts. The 3 GL account pairs (6 fields total) support full double-entry accounting for both the BS (asset + accum dep) and IS (dep expense) sides.

---

## FA-B — Post Depreciation (T7FAB.RWN)

**Purpose:** Review staged depreciation entries and post them as GL journal entries.

**DB fingerprint:** ISFXATRN, ISFXASST, BKGLCOA, BKSYMSTR, BKGLTRAN

**Workflow:**
1. T7FAA or batch calculation creates ISFXATRN records with IS_FXT_POSTED = 'N' (staged, not yet posted)
2. FA-B displays unposted entries in a "Ready to Post" review grid
3. User approves; FA-B writes GL journal entries to BKGLTRAN and flips IS_FXT_POSTED = 'Y'

**ISFXATRN fields (all 12 accessed in T7FAB):**

| Field | TAS Var | DDF Field | Type | Notes |
|-------|---------|-----------|------|-------|
| Asset Number | IS.FXT.NUMBER | IS_FXT_NUMBER | FLOAT/8 | FK to ISFXASST (PK with DATE) |
| Sort key | SIS.FXT.NUMBER | — | — | [S]-type sort key for scanning by asset# |
| Transaction Date | IS.FXT.DATE | IS_FXT_DATE | DATE | Depreciation posting date |
| Amount | IS.FXT.AMOUNT | IS_FXT_AMOUNT | FLOAT/8,2dec | Depreciation dollar amount |
| Percentage | IS.FXT.PERC | IS_FXT_PERC | FLOAT/8,8dec | Depreciation rate applied |
| Audit | IS.FXT.AUDIT | IS_FXT_AUDIT | STRING/25 | Audit reference string |
| Posted | IS.FXT.POSTED | IS_FXT_POSTED | STRING/1 | Y=posted to GL, N=staged |
| Accum Dep Account | IS.FXT.ACDEPA | IS_FXT_ACDEPA | STRING/10 | Debit side (BKGLTRAN) |
| Accum Dep Dept | IS.FXT.ACDEPD | IS_FXT_ACDEPD | STRING/4 | |
| Dep Expense Account | IS.FXT.DEPEXPA | IS_FXT_DEPEXPA | STRING/10 | Credit side (BKGLTRAN) |
| Dep Expense Dept | IS.FXT.DEPEXPD | IS_FXT_DEPEXPD | STRING/4 | |
| Net Asset Value | IS.FXT.NETAVAL | IS_FXT_NETAVAL | FLOAT/8,2dec | Net book value at time of entry |
| Extra | IS.FXT.EXTRA | IS_FXT_EXTRA | STRING/100 | User-defined |

**GL posting via BKGLTRAN:** T7FAB writes these BKGL.TRN.* fields to BKGLTRAN:
GLACCT, GLDPT, DATE, CODE, INVC (reference), DESC (description), DC (Debit/Credit flag)

Each depreciation entry creates 2 GL lines:
- Debit: Depreciation Expense (IS.FXT.DEPEXPA/DEPEXPD) → income statement
- Credit: Accumulated Depreciation (IS.FXT.ACDEPA/ACDEPD) → balance sheet

BKSYMSTR is read to validate the open accounting period before posting.

---

## FA-C/D — List Reports

**FA-C** (List Depreciation Transactions): reads ISFXATRN, likely filters by asset range or date range.
**FA-D** (List Assets): reads ISFXASST, generates asset register report.

No DFM files were found on the network share for FA-C and FA-D — these likely share the T7FAA or a common filter DFM, or the DFMs are embedded in the RWN programs as popup windows.

---

## FA-E — Import/Export Assets (T7FAE.RWN)

**Purpose:** Export fixed asset master data to CSV or fixed-width text file for external use.

**DB fingerprint:** ISFXASST, BKGLCOA (79 procs, EVO.LIB)

**Key variables:**
- `COMMA.FIXED.STR` / `COMMA.FIXED` — format selector: comma-delimited CSV vs. fixed-width
- `FILE.NAME` — output filename

Exports all 23 IS.FXA.* fields from ISFXASST. Does not export ISFXATRN transaction history.
EVO.LIB (not LISTG60.LIB) = this program is a utility/export tool, not a browse/report.

Despite the CHM calling this "Import Assets," the COMMA.FIXED export format selector and the EVO.LIB source library confirm it is primarily an export program. Import capability may be limited or may use a separate routine inside the same program.

---

## Table Schemas (DDF-confirmed)

### ISFXASST — Fixed Asset Master

23 fields, 376-byte record.

Primary key: IS_FXA_NUMBER (FLOAT, unique 6-digit asset number).

| # | DDF Field | Type | Size | Notes |
|---|-----------|------|------|-------|
| 1 | IS_FXA_NUMBER | FLOAT | 8 | Asset number (PK) |
| 2 | IS_FXA_TYPE | STRING | 30 | Asset category |
| 3 | IS_FXA_DESC | STRING | 30 | Description line 1 |
| 4 | IS_FXA_DESC2 | STRING | 30 | Description line 2 |
| 5 | IS_FXA_CSTBAS | FLOAT | 8,2dec | Cost basis |
| 6 | IS_FXA_RESVAL | FLOAT | 8,2dec | Residual/salvage value |
| 7 | IS_FXA_LIFE | FLOAT | 8 | Depreciable life (years) |
| 8 | IS_FXA_METH | STRING | 30 | Depreciation method |
| 9 | IS_FXA_GLA | STRING | 10 | Asset GL account |
| 10 | IS_FXA_GLD | STRING | 4 | Asset GL dept |
| 11 | IS_FXA_ACDEPA | STRING | 10 | Accum dep GL account |
| 12 | IS_FXA_ACDEPD | STRING | 4 | Accum dep GL dept |
| 13 | IS_FXA_DEPEXPA | STRING | 10 | Dep expense GL account |
| 14 | IS_FXA_DEPEXPD | STRING | 4 | Dep expense GL dept |
| 15 | IS_FXA_SDATE | DATE | 4 | Acquisition date |
| 16 | IS_FXA_EDATE | DATE | 4 | Disposal/end date |
| 17 | IS_FXA_SOLD | FLOAT | 8,2dec | Sale proceeds |
| 18 | IS_FXA_ACCUMDEP | FLOAT | 8,2dec | Cumulative depreciation posted |
| 19 | IS_FXA_SERIAL | STRING | 30 | Equipment serial number |
| 20 | IS_FXA_LDEPAMT | FLOAT | 8,2dec | Last dep entry amount |
| 21 | IS_FXA_LDEPPERC | FLOAT | 8,8dec | Last dep rate |
| 22 | IS_FXA_LDEPDATE | DATE | 4 | Last dep entry date |
| 23 | IS_FXA_EXTRA | STRING | 100 | User-defined |

### ISFXATRN — Fixed Asset Depreciation Transactions

12 fields, 190-byte record.

Primary key: IS_FXT_NUMBER + IS_FXT_DATE (asset number + date).

| # | DDF Field | Type | Size | Notes |
|---|-----------|------|------|-------|
| 1 | IS_FXT_NUMBER | FLOAT | 8 | Asset number (FK to ISFXASST) |
| 2 | IS_FXT_DATE | DATE | 4 | Depreciation date (part of PK) |
| 3 | IS_FXT_AMOUNT | FLOAT | 8,2dec | Depreciation amount posted |
| 4 | IS_FXT_PERC | FLOAT | 8,8dec | Depreciation rate |
| 5 | IS_FXT_AUDIT | STRING | 25 | Audit reference |
| 6 | IS_FXT_POSTED | STRING | 1 | N=staged, Y=posted to GL |
| 7 | IS_FXT_ACDEPA | STRING | 10 | Accum dep account (copy from asset) |
| 8 | IS_FXT_ACDEPD | STRING | 4 | Accum dep dept |
| 9 | IS_FXT_DEPEXPA | STRING | 10 | Dep expense account (copy from asset) |
| 10 | IS_FXT_DEPEXPD | STRING | 4 | Dep expense dept |
| 11 | IS_FXT_NETAVAL | FLOAT | 8,2dec | Net book value at this entry |
| 12 | IS_FXT_EXTRA | STRING | 100 | User-defined |

**Note:** ISFXATRN stores redundant copies of the 4 GL account fields from ISFXASST. This allows the GL accounts to change on the asset master after posting without corrupting historical transaction records.

---

## Depreciation Workflow

```
1. FA-A: Create asset record in ISFXASST
   - Set cost basis, useful life, depreciation method
   - Assign 3 GL account pairs (asset / accum dep / dep expense)
   - Record acquisition date (SDATE)

2. [Monthly/periodic]: Calculate depreciation for each asset
   - Create ISFXATRN record with IS_FXT_POSTED='N'
   - Store: asset#, date, amount, rate, net book value
   - Copy GL accounts from ISFXASST into ISFXATRN

3. FA-B: Review and post depreciation
   - Browse all ISFXATRN where IS_FXT_POSTED='N'
   - For each entry: write 2 lines to BKGLTRAN
       DR: IS_FXT_DEPEXPA/D (depreciation expense)
       CR: IS_FXT_ACDEPA/D (accumulated depreciation)
   - Set IS_FXT_POSTED='Y' on each posted entry
   - Update IS_FXA_ACCUMDEP + IS_FXA_LDEPAMT/PERC/DATE on asset master

4. FA-C: Print depreciation transaction list (ISFXATRN)
5. FA-D: Print asset register (ISFXASST)

6. FA-E: Export asset master to CSV/fixed-width for external systems
```

**Disposal (no dedicated menu code):**
- Set IS_FXA_EDATE to disposal date
- Set IS_FXA_SOLD to sale proceeds
- Manual GL adjustments required for gain/loss on sale (EVO FA does not auto-post disposal)

---

## Live Data Analysis (Pass 421, 2026-06-30)

| Table | Count | Notes |
|-------|------:|-------|
| ISFXASST | 589 | Fixed asset master records |
| ISFXATRN | 22,568 | Depreciation/transaction entries (~38 per asset) |

589 fixed assets with 22,568 transaction records (~38 transactions/asset). Regular depreciation postings have been made over many years. Each periodic run creates a batch of ISFXATRN records posted to BKGLTRAN.

## Confidence: 92/100

All 3 RWN programs decrypted and analyzed (Pass 377, 2026-06-29). Both table schemas DDF-confirmed (23 + 12 fields). All 35 IS.FXA.* + IS.FXT.* field accesses confirmed from T7FAA and T7FAB variable tables. GL posting workflow confirmed: T7FAB writes BKGL.TRN.* to BKGLTRAN. Export format confirmed from T7FAE (COMMA.FIXED toggle). Live data: ISFXASST=589/ISFXATRN=22,568 (Pass421). Remaining gap: depreciation calculation method logic (straight-line vs declining balance formula in bytecode) and exact disposal accounting procedure.
