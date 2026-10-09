# LearnEVO FAQ — EvoERP Known Problems & Solutions

A running record of diagnosed EvoERP issues with confirmed root causes and fixes.
Check this file first before investigating any new problem report.

---

## Index

| # | Title | Module | Tables | Status |
|---|-------|--------|--------|--------|
| [FAQ-001](#faq-001) | WO-G shows "Issued to Dt = 0" but IN-A Transactions shows qty issued | WO-G / IN-A | WOBOM, WOMAT, INVTXN | ✅ Solved |
| [FAQ-002](#faq-002) | Bin-to-bin transfer fails though WC field already shows "Q"; re-saving "Q" fixes it | IN-L-J / WC-B | BKICLOC, ISBINLOC, ISBINLOT, INVTXN | ✅ Root cause confirmed |

---

<!-- FAQ-001 -->
## FAQ-001 — WO-G "Issued to Dt" shows 0 but IN-A Transactions shows qty issued

**Reported:** 2026-09-03
**Status:** ✅ Solved — confirmed fix, applied live

### Symptom

In **WO-G (Issue Material)**, a component line shows `Issued to Dt = 0.0000` even though
the user believes material was already issued. In **IN-A (Inventory Inquiry) → Transactions**,
that same part number has an `I` (Issue) transaction with a quantity against the same Work Order.

Example (WO 54622-21, part 055-03251-SMTTS):
- WO-G: Issued to Dt = **0.0000**
- IN-A → INVTXN: Qty = **400**, Type = I, WO = 54622-21

### Root Cause

WO-G writes to multiple tables in sequence (not in an ACID transaction). If the process
is interrupted mid-commit (crash, network drop, killed screen), earlier tables get written
but later ones do not. The confirmed write order is:

1. **WOMAT** — material issue transaction record ← written first
2. **BKINVLOC / INVTXN** — inventory decremented, transaction logged ← written second
3. **WOBOM.WOBOM_QTYISSUED** — cumulative issued qty updated ← written last; **missed when crash occurs**

`WOBOM_QTYISSUED` is what WO-G reads for the "Issued to Dt" column. INVTXN is what
IN-A reads. When the crash lands between steps 2 and 3, inventory is already decremented
and the log is written, but the WO BOM line never gets credited — creating exactly
the symptom above.

### Diagnosis Steps

**Step 1 — Confirm WOBOM is stale:**
```sql
SELECT WOBOM_COMPCODE, WOBOM_WOPRE, WOBOM_WOSUF, WOBOM_QTYISSUED, WOBOM_TOTQTY
FROM WOBOM
WHERE WOBOM_COMPCODE = '<part number>'
  AND WOBOM_WOPRE = <WO prefix>
  AND WOBOM_WOSUF = <WO suffix>
```
Expect: `WOBOM_QTYISSUED = 0` (stale); `WOBOM_TOTQTY` = the BOM qty.

**Step 2 — Confirm WOMAT has the transaction (was this a WO-G issue or an outside adjustment?):**
```sql
SELECT MTWO_PRODCODE, WOMAT_PCODE, WOMAT_DATE, WOMAT_QTYISSUED, WOMAT_COST
FROM WOMAT
WHERE WOMAT_WOPRE = <WO prefix>
  AND WOMAT_WOSUF = <WO suffix>
  AND WOMAT_PCODE = '<part number>'
```
- **Record found** → crash happened between WOMAT write and WOBOM update; safe to fix.
- **No record** → inventory moved outside WO-G (adjustment, manual edit); fix still valid
  but root cause is different — investigate the source of the inventory move.

### Fix

Update `WOBOM_QTYISSUED` to match what WOMAT/INVTXN already recorded.

```sql
UPDATE WOBOM
SET WOBOM_QTYISSUED = <qty from WOMAT_QTYISSUED>
WHERE WOBOM_COMPCODE = '<part number>'
  AND WOBOM_WOPRE = <WO prefix>
  AND WOBOM_WOSUF = <WO suffix>
```

Verify immediately:
```sql
SELECT WOBOM_COMPCODE, WOBOM_QTYISSUED, WOBOM_TOTQTY
FROM WOBOM
WHERE WOBOM_COMPCODE = '<part number>'
  AND WOBOM_WOPRE = <WO prefix>
  AND WOBOM_WOSUF = <WO suffix>
```

### ⚠️ Critical Warning

**Do NOT re-issue through WO-G to fix this.** WO-G will create a second WOMAT record
and a second INVTXN debit — inventory gets double-decremented and actual material cost
is doubled on the WO. The correct fix is always the direct WOBOM update above.

### Tables Involved

| Table | Field | Role |
|-------|-------|------|
| WOBOM | `WOBOM_QTYISSUED` | Cumulative qty issued; drives WO-G "Issued to Dt" display |
| WOBOM | `WOBOM_TOTQTY` | Total qty required per BOM |
| WOMAT | `WOMAT_QTYISSUED` | Per-transaction issue qty; confirms the issue happened |
| WOMAT | `WOMAT_DATE`, `WOMAT_COST` | Date and cost of issue transaction |
| INVTXN | — | Inventory transaction log; drives IN-A Transactions display |

---

<!-- FAQ-002 -->
## FAQ-002 — Bin-to-bin transfer fails even though Warehouse Control field already shows "Q"

**Reported:** 2026-10-09
**Status:** ✅ Root cause confirmed from decompiled bytecode (fix is operational, not a DB edit)

### Symptom

An item's **Warehouse Control** field displays **Q** in WC-B, but **bin-to-bin transfers
(IN-L-J, same location) will not process**, and bin transactions do not synchronize with
inventory transactions (INVTXN). **Re-entering "Q" in the field and saving the record** makes
transfers work again. First seen on items beginning with `WCL`; now reported for all `PCB`
(Raw PC Boards) items.

### Root Cause

The displayed "Q" is a **red herring**. Warehouse Control mode for an item/location lives in
`BKICLOC.BKIC_LOC_WHCTRL` (values Y / Q / N). But a working **Q** item also requires supporting
**bin records in `ISBINLOC`** — specifically a default bin (`ISBIN_LOC_DFLT = Y`) with bin
on-hand (`ISBIN_LOC_UOH`) that reconciles to the location on-hand (`BKIC_LOC_UOH`), plus linked
lot/serial bin rows in `ISBINLOT`/`WCBINLOT` for lot/serial items.

When the `WHCTRL` flag reads **Q** but those `ISBINLOC` bin records are **missing or out of sync**
(no default bin, zero/incorrect bin UOH, or lot/serial rows never linked), the transfer program
rejects the move. Confirmed from decompiled `BKINLJ.RUN` (IN-L-J Transfer Inventory):

- `"You cannot transfer units to the same location unless the Warehouse Control is set to Q. Use WC-B to set the WC for Q for this specific location."`
- `"This bin does not exist for item … for this Warehouse."` / `"NO BIN LOC"` / `"Blank Bins are not allowed at this time."`
- Reads `FROM.DFLT.BIN`, `TO.DFLT.BIN`, `ISBIN.LOC.DFLT`, `ISBIN.LOC.UOH`, `MULTI.BIN` before posting.

### Why re-saving "Q" fixes it

Saving the record in **WC-B** re-runs EVO's bin-configuration logic — it rebuilds/reconciles the
`ISBINLOC` default-bin record and re-links lot/serial rows. Confirmed from `ISWCB.RUN`:

- `"You are about to run a one-time utility that will link lot/serial numbers with the WC bins. Ready to continue?"` (writes `WCBINLOT`)
- Writes `ISBINLOC` / `ISBINLOT` on save; references `ISBIN.LOC.UOH`, `ISBIN.LOC.ITEM`, `ISBIN.LOC.LOC`.

The fix is the **side effects of the WC-B save path**, not the flag value itself (which was already Q).

### ⚠️ Critical: a bulk database UPDATE will NOT fix this

Setting `BKIC_LOC_WHCTRL = 'Q'` in SQL for all PCB items is a **no-op** — the value is already "Q" —
and it does **not** trigger the `ISBINLOC`/`ISBINLOT` reconciliation that actually repairs transfers.
The remediation must go through the **WC-B program** so the reconfiguration runs.

### Remediation for a class of items (e.g. all PCB)

1. Use **WC-B → F6 Ranges** and filter by the PCB **Class/Category** (confirm first whether "PCB"
   is a Class or a Category) to re-process the group through the program's save path.
2. **Test on one known-broken PCB item first** and confirm a bin-to-bin transfer then posts —
   it is not yet verified that Ranges re-reconciles items already flagged "Q" (it may skip
   "unchanged" rows, in which case each item must be re-saved individually as the user has been doing).
3. **Do NOT toggle N↔Q or Y↔Q to force a rebuild in bulk:** WC-B warns that turning control **off
   purges existing bins**, and changing to **Y zeros out bin quantities** (`ISWCB.RUN` lines 47–48).
   That is destructive to on-hand data.

### Real underlying fix (prevent recurrence)

The recurring cause is items landing with `WHCTRL = Q` but no/stale `ISBINLOC` default-bin record
(likely from item creation/import that sets the flag without running bin configuration). Preventing
that at item setup eliminates the whole class of tickets.

### Scope note

This workspace is **read-only** against the EVO install and server (CLAUDE.md §1). The diagnosis
above is for Muthu / an authorized admin to action inside EVO; no database write was performed here.

### Tables Involved

| Table | Field | Role |
|-------|-------|------|
| BKICLOC | `BKIC_LOC_WHCTRL` | Item/location WC mode (Y/Q/N) — the field that displays "Q" |
| BKICLOC | `BKIC_LOC_UOH` | Location on-hand; bin UOH should reconcile to this |
| ISBINLOC | `ISBIN_LOC_DFLT` | Default-bin flag (`Y`) — required for Q-mode transfers |
| ISBINLOC | `ISBIN_LOC_UOH` | Per-bin on-hand used/validated by the transfer |
| ISBINLOT / WCBINLOT | — | Lot/serial-to-bin links rebuilt by WC-B's save utility |
| INVTXN | — | Inventory transaction log the bin transfer must sync to |

---

*Add new entries above this line. Follow the FAQ-NNN numbering. Update the Index table.*
