# WO-A → Material Issues button

Status: partial — mechanism verified 2026-10-12; button currently broken (see [KI-003](../../../Issues/KI-003-wo-a-material-issues-empty-file.md)).

Provenance tags as in [lookup-drill-engine.md](../../01-architecture/lookup-drill-engine.md#provenance-tags).

## What it is

- A toolbar glyph button in WO-A Enter Work Orders, control `Mat` (TGlyphBtn), hint "Material Issues"
  (`T7WOA.DFM` line ~489, plaintext DFM) [CFG]. Click handler `MAT.CLICK` [DEC].
- It opens the **WOBOMMI "Work Order Materials"** grid on **WOBOM** (the work order's bill of materials),
  restricted to the WO on screen [CFG — ISDRILL scratch record]:
  `WOBOM.WOPRE = VAL(<prefix>) .A. WOBOM.WOSUF = INT(VAL(<suffix>))`.
- Columns: Component, Type, Description, Qty Required, UM, Qty Issued, % Issued, BOM Note, Qty Scrapped [CFG].
- From each BOM line you drill into **WOMATL "Materials Issued"** = the WOMAT issue transactions for that WO [CFG].

So the button shows the **BOM lines** (WOBOM) with issued quantities, not the WOMAT transactions directly.
An empty WOBOM for the WO would legitimately produce "Empty File". Per EVO help, WOBOM lines are created when a
status-F WO is saved; status S WOs don't get them until changed to F
([WO-A help](https://evoerp.com/webhelp/6s_o_nc.htm)).

## Tables involved

| Table | File (I2) | Role |
|-------|-----------|------|
| WORKORD | `I2\WORKORD.BI2` | WO header (MTWO_WIP_*) |
| WOBOM | `I2\WOBOM.BI2` (743 MB) | WO bill of material — what the grid lists |
| WOMAT | `I2\WOMAT.BI2` | Material issue transactions — drill-down target |
| ISDRILL | `I2\ISDRILL.BI2` | Lookup request scratch record |

WOBOM indexes (X$Index) [DATA]: k0 OPER+WOPRE+WOSUF · k1 WOPRE+WOSUF+ASSY+LINE^+COMPCODE · k2 WOPRE ·
k3 WOPRE+WOSUF · k4 WOPRE+WOSUF+ASSY · k5 COMPCODE · k6 COMPCODE+START · k7 BINLOC+COMPCODE+WOPRE+WOSUF · k8 UID.

## Observed behavior 2026-10-12 [OBS + DATA]

| WO | Status (file) | Loads in WO-A? | WOBOM lines | WOMAT rows | Button result |
|----|---------------|----------------|-------------|------------|---------------|
| 56273-22 | F | Yes (050-55512-49TH) | yes (≈4) | 2 | Empty File |
| 55553-1 | R | Yes (800-04995-46AAG) | yes | 23 | Empty File |
| 56268-8 | F | not tested | yes | 1 | — |
| 55977-1 | C (closed 10/09) | **No — opens as "\* New"** | yes | yes | Empty File |
| 55968-1 | C (closed 10/09) | **No — opens as "\* New"** | yes (≈66) | 106 | Empty File |

The user has typed WO numbers directly into the field for ~2 years. The behavior started on or about
2026-10-11, after the [10/09 server move](../../01-architecture/network-topology.md) and the
[10/11 ISTS update](../../01-architecture/2026-10-11-ists-update.md).

## Closed WOs opening as "* New"

55968-1 and 55977-1 exist in WORKORD with status **C** (raw decode) [DATA], but WO-A shows
"* New / Being Created on <today> By <user>", default status F, blank part. Unknown whether this is new
intended behavior in the 09/16/26 build or a second bug. Strings in the new build include
"You cannot reopen a closed WO." and "Use WO-J to close this WO." [DEC].

## How to diagnose a lookup button quickly

1. Click the button in EVO.
2. Copy `\\i2s-evo\EVOERP\I2\ISDRILL.BI2` to `samples/` and decode the newest record for that program
   (see the field table in [lookup-drill-engine.md](../../01-architecture/lookup-drill-engine.md)).
3. Run the WHILE expression's equivalent against the data (ODBC, or a raw decode when the DDF is misaligned).
