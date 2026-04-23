# Scheduling (SH)

Status: verified (auto-generated from the extracted schema, menu-code dump, and DFM inventory).

> **Note:** folder name `sh-shipping/` is a legacy auto-classification
> artifact — the SH module is actually **Scheduling** (per the vendor
> help file's *Manufacturing → Scheduling* category and every one of
> the menu operations below). Folder name retained to avoid breaking
> URLs; contents and title corrected.

- **Module code**: `SH`
- **Tables**: 1 (prefixes `BKSH`)
- **UI forms**: 15 (prefixes `T7SH`, `T6SH`)
- **Menu operations**: 16

## Narrative / vendor help

**→ [help-content.md](help-content.md)** — consolidated write-up of
all 22 help topics from `EvoHELP.CHM` (overview + 4 method
explanations — Finite / Infinite / Lead Time / Manual — + SH-A
through SH-R, 17 programs). Hoists shared vocabulary (shop calendar,
shop date, critical ratio, contention, buckets, parent-child WCs,
scheduling units, overlap) into a single "Shared vocabulary" section
so per-method sections stay focused on how they differ. Includes the
finite-scheduling 5-step setup walk-through, the dependent-scheduling
cascade for multi-assembly WOs, and cross-links into WO, MR, JC, DC.

## Menu operations

| Code | Operation | Legacy module file(s) |
| ---- | --------- | --------------------- |
| `SH-A` | Edit WO Start/Finish/Due Dates | BKSHA |
| `SH-B` | Manually Schedule Work Orders | BKSHB |
| `SH-C` | Manually Schedule Work Centers | BKSHC |
| `SH-D` | Manually Schedule Machines | BKSHD |
| `SH-E` | Finite Scheduling | BKSHE |
| `SH-F` | Infinite Scheduling | BKSHF |
| `SH-G` | Print Work Order Schedule | BKSHG |
| `SH-H` | Print Work Order Status | BKSHH |
| `SH-I` | Print Work Center Schedule | BKSHI;CBKSHI;CBKSHI2;CBKSHI3;J5MISHI |
| `SH-J` | Print Machine Schedule | BKSHJ |
| `SH-K` | View Work Center Load | BKSHK |
| `SH-L` | Print Work Center Load | BKSHL |
| `SH-M` | Lead Time Estimator | BKSHM |
| `SH-N` | Generate Lead Times | BKSHN |
| `SH-O` | Finite Schedule Bucket Report | BKSHO |
| `SH-P` | Lead Time Scheduling | BKSHP |

## UI forms (15)

| DFM file | Caption | fields | controls | tabs |
| -------- | ------- | -----: | -------: | ---: |
| `T7SHA.DFM` |  | 0 | 1 | 0 |
| `T7SHB.DFM` |  | 0 | 1 | 0 |
| `T7SHC.DFM` |  | 0 | 1 | 0 |
| `T7SHE.DFM` |  | 0 | 1 | 0 |
| `T7SHF.DFM` | SH-F | 15 | 43 | 0 |
| `T7SHG.DFM` | SH-G | 31 | 69 | 0 |
| `T7SHH.DFM` | New Screen | 14 | 42 | 0 |
| `T7SHI.DFM` | SH-I | 47 | 106 | 0 |
| `T7SHIPRTM.DFM` |  | 0 | 1 | 0 |
| `T7SHJ.DFM` | SH-J | 30 | 71 | 0 |
| `T7SHM.DFM` | SH-M | 13 | 39 | 0 |
| `T7SHN.DFM` | SH-N | 16 | 46 | 0 |
| `T7SHO.DFM` | SH-O | 4 | 21 | 0 |
| `T7SHOWLINEHIST.DFM` |  | 0 | 1 | 0 |
| `T7SHP.DFM` | SH-P | 38 | 96 | 0 |

## Database tables (1)

Full field details are in `../../../samples/ddf/schema.md` (see per-table heading).

| Table | File on disk | Fields | Key fields (first 3) |
| ----- | ------------ | -----: | -------------------- |
| **BKSHORT** | `BKSHORT.B` | 9 | `BK_SHORT_PCODE`, `BK_SHORT_DESC`, `BK_SHORT_WONUM` |

## Notes & open questions

- *(populated per-module manually as deeper reading happens.)*
