# IN-C: Bin Field Greyed Out — WC Mode Fix

Status: verified  
Date: 2026-08-27  
Module: IN (Inventory) + WC (Warehouse Control)

---

## Symptom

In **IN-C (Enter Inventory Adjustments)**, the **Bin** field is greyed out and cannot be
edited. The field shows a bin value with an asterisk suffix (e.g. `Q-01-04*`) but the
user cannot change it.

---

## Root Cause

The asterisk (`*`) on the bin value indicates it is the **system-designated default bin**
(`ISBIN_LOC_DFLT = Y` in the `ISBINLOC` table). The field is locked because the item's
**Warehouse Control mode is set to Q (Quantity-only)** in WC-B.

WC mode meanings:

| Mode | Meaning | Bin field in transactions |
|------|---------|--------------------------|
| Y | Full bin tracking | Editable and required |
| Q | Quantity-only | Auto-filled from default bin, **locked** |
| N | Warehouse control off | Not shown / inactive |

When mode is **Q**, the runtime `vld_bin()` function (in `T7INC.RWN`) disables the field
after auto-populating it from the default bin record. This is by design — Q mode tracks
*that* inventory exists in a bin but does not allow per-transaction bin selection.

This behaviour applies to any item/location combination in Q mode, not just the specific
item that surfaced the issue (500-04768 / location I2S).

---

## Resolution: Change WC mode from Q → Y

### Step 1 — Open WC-B

Navigate to **WC → B (Assign Warehouse Control)**.

### Step 2 — Filter to the item

- **Item Number From / Thru:** enter the item code (e.g. `500-04768` / `500-04768`)
- Leave other filters blank to see all warehouse locations for that item

### Step 3 — Locate the correct warehouse row

Scroll the grid to find the warehouse/location the user is adjusting inventory in
(e.g. **I2S**). Check its columns:

| Column | Meaning |
|--------|---------|
| Location WC | The WC mode set at the warehouse/location level |
| Item WC | The WC mode currently active for this item at this location |
| New WC | The value that will be written when Process is clicked |

### Step 4 — Set the row to Y

Click the target row to select it, then click **Set to Y** at the bottom. The row's
**New WC** column will update to **Y**.

### Step 5 — Check for unintended tags (critical)

Other rows may be unexpectedly tagged for processing. For each row whose **New WC**
column shows a value you did not intend to change:

1. Click that row
2. If the bottom button reads **Untag**, click it — that row is queued and would be
   changed when Process runs
3. Repeat for every row you did not explicitly set

> **Warning observed in practice:** rows that had Location WC = Y (e.g. ENGINEERING,
> WINDSOR) were automatically tagged and showed New WC = Q, meaning Process would have
> downgraded them from Y → Q. Always audit all rows before clicking Process.

### Step 6 — Process

Once only the intended row(s) show the correct New WC value and all others are untagged,
click **Process**.

---

## After Processing

Because the item may have had WC mode **N** (off) rather than Q at the target location,
there may be **no bin records in ISBINLOC** for that item+location combination. Without
bin records, the Bin field in IN-C will be editable but empty, and the user will not know
what to enter.

Immediately after processing, verify in **WC-A (Enter Warehouse Bin Locations)** or
**WC-C (Assign Bins to Items)** that:

- At least one bin record exists for the item at the target location
- One bin is marked as the default (`ISBIN_LOC_DFLT = Y`)

If no bin records exist, create the appropriate bin entry and set its default flag. The
asterisk (`*`) will then appear next to the default bin in transaction screens.

---

## Key Tables

| Table | Relevant fields | Purpose |
|-------|----------------|---------|
| `ISBINLOC` | `ISBIN_LOC_ITEM`, `ISBIN_LOC_LOC`, `ISBIN_LOC_BIN`, `ISBIN_LOC_DFLT` | Bin-level inventory (no lot tracking) |
| `ISBINLOT` | `IS_BINLOT_ITEM`, `IS_BINLOT_LOC`, `IS_BINLOT_LOT`, `IS_BINLOT_BIN`, `IS_BINLOT_DFLT` | Bin-level inventory with lot tracking |

---

## Related Files

- `T7INC.DFM` — IN-C form definition; Bin component is `EnterBin` mapped to `DEFAULT.BIN`
- `T7INC.RWN` — Encrypted source; contains `vld_bin()` which controls field enable/disable
- `ISWCC.RUN` — WC-C (Assign Bins to Items)
- `T7WCA.RWN` — WC-A (Enter Warehouse Bin Locations)
