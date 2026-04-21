# Bill of Materials (BM)

Status: verified (auto-generated from the extracted schema, menu-code dump, and DFM inventory).

- **Module code**: `BM`
- **Tables**: 10 (prefixes `BKBM`)
- **UI forms**: 16 (prefixes `T7BM`, `T6BM`, `BKBM`)
- **Menu operations**: 10

## Menu operations

| Code | Operation | Legacy module file(s) |
| ---- | --------- | --------------------- |
| `BM-C` | Print Where Used | BKBMC |
| `BM-D` | Print BOM Availability | BKBMD |
| `BM-E` | Global Replace | BKBME |
| `BM-F` | Global Delete | BKBMF |
| `BM-G` | IN-B     IN-L-A     SO-Q- | AUTOBMG;BKBMG;ISSMJS |
| `BM-H` | Print BOM at Average Cost | BKBMH;BKBMH1 |
| `BM-I` | Print Summarized BOM | BKBMI |
| `BM-J` | Enter Approved Substitutes | BKBMJ |
| `BM-J-C` | Enter Approved Manufacturers | BKBMJC |
| `BM-X` | BOM report | BKBMX |

## UI forms (16)

| DFM file | Caption | fields | controls | tabs |
| -------- | ------- | -----: | -------: | ---: |
| `T7BMA.DFM` | New Screen | 44 | 105 | 0 |
| `T7BMAx.DFM` | New Screen | 42 | 77 | 0 |
| `T7BMB.DFM` | BM-B | 28 | 58 | 0 |
| `T7BMC.DFM` | BM-C | 6 | 27 | 0 |
| `T7BMD.DFM` | Print Availability | 18 | 46 | 0 |
| `T7BME.DFM` | BM-E | 6 | 24 | 0 |
| `T7BMF.DFM` | BM-F | 2 | 18 | 0 |
| `T7BMG.DFM` | BM-G | 18 | 48 | 0 |
| `T7BMH.DFM` | BM-H | 11 | 33 | 0 |
| `T7BMI.DFM` | BM-I | 16 | 40 | 0 |
| `T7BMJ.DFM` |  | 0 | 1 | 0 |
| `T7BMK.DFM` |  | 0 | 1 | 0 |
| `T7BML.DFM` |  | 0 | 1 | 0 |
| `T7BMP.DFM` | BOM Pick List | 7 | 29 | 0 |
| `T7BMQ.DFM` | BM-Q | 3 | 21 | 0 |
| `T7BMR.DFM` | BM-R | 16 | 43 | 0 |

## Database tables (10)

Full field details are in `../../../samples/ddf/schema.md` (see per-table heading).

| Table | File on disk | Fields | Key fields (first 3) |
| ----- | ------------ | -----: | -------------------- |
| **BKBMAMTR** | `BKBMAMTR.B` | 26 | `BKBM_PARENT`, `BKBM_COMPONENT`, `BKBM_QTY_REQD` |
| **BKBMAVAL** | `BKBMAVAL.B` | 26 | `BKBM_PARENT`, `BKBM_COMPONENT`, `BKBM_QTY_REQD` |
| **BKBMCNFG** | `BKBMCNFG.B` | 7 | `BKBM_CNFG_NUM`, `BKBM_CNFG_GLACT`, `BKBM_CNFG_GLDPT` |
| **BKBMDIM** | `BKBMDIM.B` | 11 | `BKBM_DIM_PARENT`, `BKBM_DIM_LINE`, `BKBM_DIM_COMP` |
| **BKBMEMTR** | `BKBMEMTR.B` | 26 | `BKBM_PARENT`, `BKBM_COMPONENT`, `BKBM_QTY_REQD` |
| **BKBMERMK** | `BKBMERMK.B` | 20 | `BKBM_RM_PARENT`, `BKBM_RM_LINE`, `BKBM_RM_COMP` |
| **BKBMMSTR** | `BKBMMSTR.B` | 26 | `BKBM_PARENT`, `BKBM_COMPONENT`, `BKBM_QTY_REQD` |
| **BKBMNOTE** | `BKBMNOTE.B` | 16 | `BKBM_NT_PARENT`, `BKBM_NT_NOTE_1`, `BKBM_NT_NOTE_2` |
| **BKBMREMK** | `BKBMREMK.B` | 20 | `BKBM_RM_PARENT`, `BKBM_RM_LINE`, `BKBM_RM_COMP` |
| **BKBMSUMM** | `BKBMSUMM.B` | 26 | `BKBM_PARENT`, `BKBM_COMPONENT`, `BKBM_QTY_REQD` |

## Notes & open questions

- *(populated per-module manually as deeper reading happens.)*
