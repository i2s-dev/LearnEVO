# FA — Fixed Assets: Field Reference

Status: verified-schema + inferred meanings (Pass 574, 2026-07-06).

Source: `Evo-DBA_File_Fields 052421.xlsx`, sheet "Fields".

The FA module manages fixed asset accounting: acquisition, depreciation, and disposal.
EvoERP's FA module is an add-on (not all installations have it). At i2 Systems this module
does not appear to be actively used (no live data confirmed).

Two tables: ISFXASST (asset master) and ISFXATRN (depreciation/transaction history).

---

## ISFXASST
**FIXED ASSET MASTER** — one record per fixed asset

Fields: 23 | Key: IS_FXA_NUMBER

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_FXA_ACCUMDEP | NUMERIC | 8 | 2 | Accumulated depreciation to date |
| 2 | IS_FXA_ACDEPA | STRING | 10 | — | GL account for accumulated depreciation (credit account) |
| 3 | IS_FXA_ACDEPD | STRING | 4 | — | GL department for accumulated depreciation |
| 4 | IS_FXA_CSTBAS | NUMERIC | 8 | 2 | Cost basis — original acquisition cost |
| 5 | IS_FXA_DEPEXPA | STRING | 10 | — | GL account for depreciation expense (debit account) |
| 6 | IS_FXA_DEPEXPD | STRING | 4 | — | GL department for depreciation expense |
| 7 | IS_FXA_DESC | STRING | 30 | — | Asset description line 1 |
| 8 | IS_FXA_DESC2 | STRING | 30 | — | Asset description line 2 |
| 9 | IS_FXA_EDATE | DATE | 4 | — | End/disposal date — when asset was sold or retired |
| 10 | IS_FXA_EXTRA | STRING | 100 | — | User-defined extra data |
| 11 | IS_FXA_GLA | STRING | 10 | — | GL asset account (balance sheet — the asset cost account) |
| 12 | IS_FXA_GLD | STRING | 4 | — | GL department for the asset account |
| 13 | IS_FXA_LDEPAMT | NUMERIC | 8 | 2 | Last depreciation run amount |
| 14 | IS_FXA_LDEPDATE | DATE | 4 | — | Last depreciation run date |
| 15 | IS_FXA_LDEPPERC | NUMERIC | 8 | 8 | Last depreciation run percentage rate |
| 16 | IS_FXA_LIFE | NUMERIC | 8 | — | Useful life (in months or years, per the chosen method) |
| 17 | IS_FXA_METH | STRING | 30 | — | Depreciation method (e.g., Straight-Line, MACRS, Double-Declining) |
| 18 | IS_FXA_NUMBER | NUMERIC | 8 | — | Asset number (PK — system-assigned unique ID) |
| 19 | IS_FXA_RESVAL | NUMERIC | 8 | 2 | Residual/salvage value — estimated value at end of useful life |
| 20 | IS_FXA_SDATE | DATE | 4 | — | Service/acquisition date — when asset was placed in service |
| 21 | IS_FXA_SERIAL | STRING | 30 | — | Asset serial number (manufacturer's serial) |
| 22 | IS_FXA_SOLD | NUMERIC | 8 | 2 | Proceeds from sale/disposal |
| 23 | IS_FXA_TYPE | STRING | 30 | — | Asset type/class (e.g., Equipment, Vehicle, Building) |

**GL Posting Structure:** Three GL pairs (account+dept) per asset:
- `GLA/GLD` = asset cost account (debit on acquisition, credit on disposal)
- `ACDEPA/ACDEPD` = accumulated depreciation (credit on each depreciation run)
- `DEPEXPA/DEPEXPD` = depreciation expense (debit on each depreciation run)

## ISFXATRN
**FIXED ASSET TRANSACTIONS** — depreciation and adjustment history

Fields: 12 | Key: IS_FXT_NUMBER + IS_FXT_DATE

One row per depreciation run or manual adjustment for an asset.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_FXT_ACDEPA | STRING | 10 | — | GL account for accumulated depreciation (from asset master at time of posting) |
| 2 | IS_FXT_ACDEPD | STRING | 4 | — | GL department for accumulated depreciation |
| 3 | IS_FXT_AMOUNT | NUMERIC | 8 | 2 | Depreciation or adjustment amount for this transaction |
| 4 | IS_FXT_AUDIT | STRING | 25 | — | Audit trail note / user who created this transaction |
| 5 | IS_FXT_DATE | DATE | 4 | — | Transaction date |
| 6 | IS_FXT_DEPEXPA | STRING | 10 | — | GL account for depreciation expense |
| 7 | IS_FXT_DEPEXPD | STRING | 4 | — | GL department for depreciation expense |
| 8 | IS_FXT_EXTRA | STRING | 100 | — | User-defined extra data |
| 9 | IS_FXT_NETAVAL | NUMERIC | 8 | 2 | Net asset value (book value) after this transaction |
| 10 | IS_FXT_NUMBER | NUMERIC | 8 | — | Asset number (FK → ISFXASST.IS_FXA_NUMBER) |
| 11 | IS_FXT_PERC | NUMERIC | 8 | 8 | Depreciation percentage rate applied |
| 12 | IS_FXT_POSTED | STRING | 1 | — | Posted flag: `Y` = this transaction has been posted to GL |

**Confidence: 85/100** — field meanings derived from standard fixed-asset accounting conventions
plus field naming; GL posting structure matches BKGLTRAN pattern; exact METH values and
LIFE unit (months vs years) unverified without RWN access.
