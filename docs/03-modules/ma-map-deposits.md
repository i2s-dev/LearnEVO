# MA — Map Deposits (T7MAPDEPO.RWN)

Status: verified | Pass 230 2026-06-23

Source: variable extraction from `samples/rwn_decrypted/T7MAPDEPO.RWN.dec`

---

## Overview

`T7MAPDEPO.RWN` is the **MA module** (Map Deposits) — an AR sub-function that applies
customer deposits to open invoice lines.

- **Module code:** MA (Map Deposits)
- **Program:** T7MAPDEPO.RWN (LISTG60.LIB source)
- **Variables:** 1,664 | **Instructions:** 3,074 | **Procs:** 97
- **Primary tables:** `BKAR.DEP` (AR deposit header), `ISAR.DEPL` (ISTS AR deposit lines),
  `BKAR.INVL` (AR invoice lines)

---

## What It Does

The Map Deposits function takes a customer deposit (a payment received before invoicing —
common in manufacturing for advance payments on SO or WO) and applies it against one or
more open invoice lines. This reduces the AR balance for the customer without issuing a
new cash receipt.

**Workflow:**
1. User selects a deposit record from `BKAR.DEP`
2. System displays the deposit amount and finds matching open invoice lines (`BKAR.INVL`)
3. User applies (maps) the deposit amount across one or more invoice lines
4. System writes the application record to `ISAR.DEPL` (ISTS deposit lines table)
5. Remaining unapplied deposit balance is tracked in `DEPO.AMOUNT` / `AMOUNT.REM`

---

## Key Variables

### BKAR.DEP.* — AR Deposit Header

| Variable | Meaning |
|----------|---------|
| `BKAR.DEP.DEPNO` | Deposit number (PK) |
| `BKAR.DEP.CUST` | Customer code |
| `BKAR.DEP.DATE` | Deposit date |
| `BKAR.DEP.SO` | Source Sales Order number |
| `BKAR.DEP.SR` | Source Service Request number |

### ISAR.DEPL.* — ISTS AR Deposit Lines

| Variable | Meaning |
|----------|---------|
| `ISAR.DEPL.SO` | Applied-to SO number |
| `ISAR.DEPL.SCCOG` | Subcontract COGS amount |
| `ISAR.DEPL.OAMT` | Original deposit amount |
| `ISAR.DEPL.AMT` | Amount applied this line |
| `ISAR.DEPL.AMTRM` | Amount remaining after application |

### Computation / GL Distribution

| Variable | Meaning |
|----------|---------|
| `DEPO.ORIG.AMT` | Total original deposit amount |
| `DEPO.AMOUNT` | Current deposit balance |
| `AMOUNT.REM` | Remaining unapplied amount |
| `FROM.ITEM` | Inventory item being matched |
| `FROM.GLACCT` | GL account for distribution |
| `FROM.GLDPT` | GL department for distribution |
| `SFROM.SONUM` | Source SO number (from line) |

---

## Related Tables

| Table | Approx. Fields | Purpose |
|-------|---------------|---------|
| `BKAR.DEP` (BKARDEPO?) | ~6 | AR deposit header (customer, date, amount) |
| `ISAR.DEPL` (ISARDEPL?) | ~18 | ISTS deposit application lines |
| `BKAR.INVL` | ~28 | AR invoice lines — target for application |
| `BKAR.GROSS` | ~4 | AR gross amounts |
| `BKAR.COGS` | ~4 | AR COGS amounts |
| `BKAR.NET` | ~4 | AR net amounts |
| `BKAR.PNET` | ~4 | AR prior net amounts |
| `BKAR.IS` | ~4 | AR income statement amounts |

The session summary notes these as counts of var-namespace entries; actual Btrieve table
names may differ — the BKAR.DEP namespace likely maps to BKARDEPO.B or similar.

---

## Architecture Notes

- LISTG60.LIB source: first 60 vars are TEMP0–TEMP59 (standard scratch block); module
  vars start at var[60]+, including library-provided ISTS.PATH, tax handles, ISTS.CFG.*.
- 97 procs and 3,074 instructions indicate significant business logic for the deposit
  application calculation and GL distribution.
- The `FROM.*` and `SFROM.*` local vars suggest a multi-step "from → to" matching UI
  where the user selects source (deposit) and target (invoice line) items.
- `ISAR.DEPL` (ISTS prefix) confirms this is i2 Systems custom functionality layered
  on top of the base DBA deposit table `BKAR.DEP`.

---

## Notes & Open Questions

- Exact Btrieve table filenames for `BKAR.DEP` / `ISAR.DEPL` need DDF confirmation.
  From the DDF schema, look for BKARDEPO, ISARDEPL, or similar.
- Whether MA is accessible from a menu code or is always called as a sub-function from
  AR is not yet confirmed.
- The 5 BKAR.DEP fields seen (DEPNO/CUST/DATE/SO/SR) are only a subset of the first 200
  vars — the full field set is larger.

**Confidence: 70/100** — Variable extraction confirmed; business purpose (deposit-to-invoice
matching) is strongly supported by the var names. Exact table names and full field set need
DDF cross-reference; GL distribution detail is inferred.
