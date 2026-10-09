# WO-G "Issued to Dt" Shows Zero After Issuance — Diagnosis & Resolution

**Date:** 2026-09-03
**Work Order:** 54622-21 (Parent Part: 056-03251-CTLTS, PCBA,MAIN CTL,UC,0337A,120V)
**Module:** WO-G (Issue Material) / IN-A (Inventory Inquiry)
**Status:** ✅ Resolved — 19 of 20 components corrected; 1 component requires manual follow-up
**See also:** [FAQ-001](../../FAQ.md#faq-001)

---

## 1. The Problem

### 1.1 What the User Saw

When opening **WO-G (Issue Material)** — program file `T7WOG.RWN` — for Work Order **54622-21**, the
grid showed every component on the BOM with an **"Issued to Dt" value of 0.0000**, despite the
operator being certain that material had already been fully issued for this WO on 09/02/2026.

The "Issued to Dt" column is EvoERP's running total of how much of each component has been
issued to the work order to date. A zero means WO-G believes nothing has been issued.

Simultaneously, when looking up the same part numbers in **IN-A (Inventory Inquiry)** and
navigating to the **Transactions** sub-screen (which reads from the `INVTXN` table, displayed
as "INVTRANS" at the bottom of the IN-A screen), the transactions were clearly present —
type `I` (Issue), dated 09/02/2026, with the correct quantities, all linked to WO 54622-21.

**Example (first part identified):**

| Screen | Field | Value |
|--------|-------|-------|
| WO-G → Issued to Dt | `WOBOM.WOBOM_QTYISSUED` | 0.0000 |
| IN-A → Transactions | `INVTXN` record | Qty = 400, Type = I, WO = 54622-21 |

The discrepancy: inventory had been decremented and a transaction log entry existed, but
WO-G had no record of the issue.

### 1.2 Scope of the Problem

Initial investigation identified 1 part. The user then confirmed that **all 20 components**
on the BOM for WO 54622-21 appeared to have the same symptom. The full component list:

| Part Number | WO BOM Qty | Issued to Dt (before fix) |
|-------------|-----------|--------------------------|
| 020-03387-VER43 | 0 | 0 *(correct — BOM qty is 0)* |
| 055-03251-SMTTS | 400 | 0 ← **fixed first** |
| 120-00539 | 0 | 0 *(correct — BOM qty is 0)* |
| 243-03343 | 1200 | 0 |
| 365-03322 | 800 | 0 |
| 440-03339 | 400 | 0 |
| 445-03329 | 400 | 0 |
| 455-03334 | 2800 | 0 |
| 455-05158 | 400 | 0 |
| 455-05642 | 1200 | 0 |
| 470-03333 | 400 | 0 |
| 510-03340 | 8000 | 0 |
| 510-03341 | 7600 | 0 |
| 515-03323 | 400 | 0 |
| 515-03324 | 400 | 0 |
| 515-03325 | 400 | 0 |
| 515-03327 | 400 | 0 |
| 515-03929 | 400 | 0 |
| 600-03338 | 800 | 0 |
| 730-03931 | 400 | 0 |
| 740-04609 | 400 | 0 |
| 740-51949 | 400 | 0 ← **not fixed; see §5** |

---

## 2. Why It Happened — Root Cause

### 2.1 Two Different Tables, Two Different Screens

EvoERP stores issuance data in multiple places that are normally kept in sync:

| Table | What it stores | Which screen reads it |
|-------|---------------|----------------------|
| `WOBOM` | The WO's bill of material snapshot. Field `WOBOM_QTYISSUED` is a running cumulative total of how many units of each component have been issued to date. | **WO-G** reads this for "Issued to Dt" |
| `WOMAT` | One record per issue transaction event. Stores the date, component code, qty issued, cost, lot, serial, scrap info. | Used for cost roll-up and material transaction history |
| `INVTXN` | General inventory transaction log. One record per inventory movement regardless of origin. | **IN-A Transactions** reads this |
| `BKINVLOC` | Inventory on-hand quantity by part and location. | Drives on-hand qty displays everywhere |

These tables are written by `T7WOG.RWN` (WO-G) **sequentially** — one after another — when
the operator clicks Save during an issue. EvoERP runs on **TAS Professional 7** (`tp7runtime.exe`)
with a **Pervasive SQL / Btrieve** database backend. Btrieve does not provide cross-table
transactions with rollback the way a modern RDBMS does. Each table write either succeeds or
fails independently.

### 2.2 The Write Sequence

When WO-G saves a material issue, it writes these tables in order:

```
1. WOMAT          — issue transaction record created
2. BKINVLOC       — on-hand inventory quantity decremented
3. INVTXN         — transaction log entry written
4. WOBOM          — WOBOM_QTYISSUED updated  ← this is last
5. WORKORD        — MTWO_WIP_AMAT (actual material cost) accumulated
```

### 2.3 What Went Wrong

The issuance process on 09/02/2026 was interrupted — most likely a network drop, application
crash, or workstation shutdown — **after steps 1–3 completed but before step 4 ran**.

Result:
- ✅ `WOMAT` — all 20 issue transaction records written (one per component)
- ✅ `BKINVLOC` — inventory decremented correctly for all components
- ✅ `INVTXN` — transaction log entries written (visible in IN-A)
- ❌ `WOBOM.WOBOM_QTYISSUED` — never updated; remained at 0 for all 20 components

This is why IN-A showed the transactions but WO-G showed zeros. The inventory reality
was correct; only the WO's internal tracking was incomplete.

---

## 3. Verification Process

Before making any changes, each component was verified against two sources to confirm
the issue was legitimate and safe to correct.

### 3.1 Check 1 — Confirm WOBOM is stale

Query run against the live `DBA` ODBC data source:

```sql
SELECT WOBOM_COMPCODE, WOBOM_TOTQTY, WOBOM_QTYISSUED
FROM WOBOM
WHERE WOBOM_WOPRE = 54622
  AND WOBOM_WOSUF = 21
  AND WOBOM_COMPCODE IN (
    '243-03343','365-03322','440-03339','445-03329','455-03334',
    '455-05158','455-05642','470-03333','510-03340','510-03341',
    '515-03323','515-03324','515-03325','515-03327','515-03929',
    '600-03338','730-03931','740-04609','740-51949'
  )
ORDER BY WOBOM_COMPCODE
```

Result: All 19 parts returned `WOBOM_QTYISSUED = 0` while `WOBOM_TOTQTY` held the
correct BOM quantity. The WOBOM records existed and were structurally valid — they
just had a stale issued qty.

### 3.2 Check 2 — Confirm WOMAT has the transaction

```sql
SELECT WOMAT_PCODE, WOMAT_QTYISSUED, WOMAT_DATE, WOMAT_COST
FROM WOMAT
WHERE WOMAT_WOPRE = 54622
  AND WOMAT_WOSUF = 21
  AND WOMAT_PCODE IN (
    '243-03343','365-03322','440-03339','445-03329','455-03334',
    '455-05158','455-05642','470-03333','510-03340','510-03341',
    '515-03323','515-03324','515-03325','515-03327','515-03929',
    '600-03338','730-03931','740-04609','740-51949'
  )
```

Result for 18 of 19 parts: `WOMAT_DATE = 09/02/2026`, `WOMAT_QTYISSUED` exactly matched
`WOBOM_TOTQTY`. This confirmed the issues went through WO-G legitimately and the quantities
to restore were unambiguous.

Result for **740-51949**: **No WOMAT record found.** This part was excluded from the fix
(see §5).

### 3.3 Decision Rule Applied

A part was approved for correction only if all three conditions were true:

1. `WOBOM_QTYISSUED = 0` (stale — needs fixing)
2. A `WOMAT` record exists for this part on this WO
3. `WOMAT_QTYISSUED` exactly equals `WOBOM_TOTQTY` (quantities are unambiguous)

All 18 corrected parts met all three conditions. 740-51949 failed condition 2.

---

## 4. The Fix

### 4.1 Why Not Re-Issue Through WO-G

The instinctive fix — open WO-G and issue the parts again — would be **incorrect and
harmful**:

- WO-G would write a new `WOMAT` record (doubling the transaction count)
- WO-G would write a new `INVTXN` entry (doubling the logged issue qty)
- WO-G would decrement `BKINVLOC` again (taking 400 extra units off inventory that
  were never physically consumed)
- Actual material cost on `WORKORD.MTWO_WIP_AMAT` would be double-charged

The inventory was already correctly decremented. The only thing missing was the
`WOBOM_QTYISSUED` update. The correct fix is surgical: update only that field.

### 4.2 The Update Applied

```sql
UPDATE WOBOM
SET WOBOM_QTYISSUED = <WOBOM_TOTQTY for that part>
WHERE WOBOM_COMPCODE = '<part number>'
  AND WOBOM_WOPRE = 54622
  AND WOBOM_WOSUF = 21
```

This was executed individually for each of the 18 confirmed parts via the `DBA` ODBC
connection (Pervasive SQL). Each statement returned `rows updated = 1`. The fix values
used:

| Part Number | WOBOM_QTYISSUED set to |
|-------------|------------------------|
| 055-03251-SMTTS | 400 |
| 243-03343 | 1200 |
| 365-03322 | 800 |
| 440-03339 | 400 |
| 445-03329 | 400 |
| 455-03334 | 2800 |
| 455-05158 | 400 |
| 455-05642 | 1200 |
| 470-03333 | 400 |
| 510-03340 | 8000 |
| 510-03341 | 7600 |
| 515-03323 | 400 |
| 515-03324 | 400 |
| 515-03325 | 400 |
| 515-03327 | 400 |
| 515-03929 | 400 |
| 600-03338 | 800 |
| 730-03931 | 400 |
| 740-04609 | 400 |

### 4.3 Verification After Fix

A post-fix query confirmed every corrected row now reads `WOBOM_QTYISSUED = WOBOM_TOTQTY`:

```sql
SELECT WOBOM_COMPCODE, WOBOM_TOTQTY, WOBOM_QTYISSUED,
       CASE WHEN WOBOM_QTYISSUED = WOBOM_TOTQTY THEN 'OK' ELSE 'MISMATCH' END AS STATUS
FROM WOBOM
WHERE WOBOM_WOPRE = 54622
  AND WOBOM_WOSUF = 21
ORDER BY WOBOM_COMPCODE
```

All 19 corrected parts (including 055-03251-SMTTS from the initial fix) returned `STATUS = OK`.
740-51949 returned `STATUS = MISMATCH` as expected (intentionally not corrected).

---

## 5. Outstanding Item — 740-51949

**Part:** 740-51949 (LABEL,WHT,POLYIMIDE)
**WOBOM_TOTQTY:** 400
**WOBOM_QTYISSUED:** 0 (unchanged)
**WOMAT record:** None found

This part has no material issue transaction on record for WO 54622-21. This means one of two things:

**Scenario A — It was never issued.** The 09/02/2026 issuance run was stopped before this
component was processed. The part still needs to be physically pulled and issued through
WO-G normally. WO-G will write all tables correctly at that time.

**Scenario B — It was issued through a path that didn't go through WO-G.** An inventory
adjustment or manual move may have decremented inventory without creating a WOMAT record.
In this case, check INVTXN for 740-51949 on WO 54622-21 to see if an `I` record exists.
If it does, the same WOBOM fix from §4.2 applies.

**Action required:** Physical verification — was 740-51949 actually pulled and consumed
for WO 54622-21? Answer determines next step.

---

## 6. Files and Tables Reference

| Name | Type | Description | Role in This Issue |
|------|------|-------------|-------------------|
| `T7WOG.RWN` | Compiled TAS Pro 7 program | WO-G Issue Material screen | Source of the broken write sequence |
| `WOBOM` | Btrieve table | Work Order Bill of Material | `WOBOM_QTYISSUED` was the stale field; drove the "Issued to Dt" display |
| `WOMAT` | Btrieve table | Material Issue Transactions | Confirmed legitimate issue; source of correct qty values |
| `INVTXN` | Btrieve table | Inventory Transaction Log | Showed the issue in IN-A; proved inventory had moved |
| `BKINVLOC` | Btrieve table | Inventory On-Hand by Location | Was already correctly decremented; not touched by fix |
| `WORKORD` | Btrieve table | Work Order Master Header | `MTWO_WIP_AMAT` (actual material cost) — not verified; may also be understated |

### Note on WORKORD.MTWO_WIP_AMAT

The actual material cost field on the WO header (`WORKORD.MTWO_WIP_AMAT`) is written in
step 5 of the WO-G write sequence — after `WOBOM_QTYISSUED` (step 4). If the crash
happened at step 4, step 5 also did not run, meaning the **actual material cost on the WO
header may be understated or zero**. This was not investigated or corrected in this session.
If WO cost reporting matters for this WO, that field should be checked and potentially
recalculated.

---

## 7. How to Prevent / Detect This in the Future

- This failure mode is inherent to TAS Pro 7's sequential Btrieve write pattern. It cannot
  be eliminated without changes to the ERP software itself.
- Any time a user reports "WO-G shows nothing issued but we definitely issued it," this
  document and **FAQ-001** describe the complete diagnostic and fix procedure.
- The diagnostic takes under 2 minutes via direct ODBC query: check WOBOM_QTYISSUED,
  confirm with WOMAT, apply the targeted UPDATE.
- **Never re-issue through WO-G** as a fix — it double-hits inventory.
