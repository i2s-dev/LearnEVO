# Job Costing (JC)

Status: verified (auto-generated from the extracted schema, menu-code dump, and DFM inventory).

- **Module code**: `JC`
- **Tables**: 2 (prefixes `WOHLABOR`, `BKJC`, `WOLABOR`)
- **UI forms**: 14 (prefixes `T7JC`, `T6JC`)
- **Menu operations**: 18

## Narrative / vendor help

**→ [help-content.md](help-content.md)** — consolidated write-up of
all 20 help topics from `EvoHELP.CHM` (overview + JC-A through JC-S),
with the common-selection-ribbon pattern extracted once and each
report annotated with source tables, accuracy gotchas, and
cross-links into WO, GL, BM, and the System Overview close checklist.

## Menu operations

| Code | Operation | Legacy module file(s) |
| ---- | --------- | --------------------- |
| `JC-A` | Print Job Cost Report | BKJCA;t6jca |
| `JC-B` | Print Profit Projection | BKJCB |
| `JC-C` | Print Labor Transactions | BKJCC |
| `JC-D` | Print Overhead Transactions | BKJCD |
| `JC-E` | Print Material Issues | BKJCE;ISJCE |
| `JC-F` | Print Outside Purchases | BKJCF |
| `JC-G` | Print Labor Efficiency | BKJCG |
| `JC-H` | Print Active Work Order History | BKJCH;J6HTJCH |
| `JC-I` | Print Production By Work Center | BKJCI |
| `JC-J` | Print Production By Machine | BKJCJ |
| `JC-K` | Print Production By Tool | BKJCK |
| `JC-L` | Print Job Cost Summary | BKJCL |
| `JC-M` | Print WIP Summary | BKJCM |
| `JC-N` | Print WIP Percent Completion | BKJCN |
| `JC-O` | Print Standard Labor Hours | BKJCO |
| `JC-P` | Print Materials in WIP | BKJCP |
| `JC-Q` | Print WO Receipts | BKJCQ |
| `JC-R` | Multi-Level Assembly Cost Breakdown | BKJCR |

## UI forms (14)

| DFM file | Caption | fields | controls | tabs |
| -------- | ------- | -----: | -------: | ---: |
| `T7JCA.DFM` | New Screen | 17 | 45 | 0 |
| `T7JCB.DFM` | New Screen | 10 | 34 | 0 |
| `T7JCE.DFM` | JC-E | 20 | 53 | 0 |
| `T7JCENG.DFM` | JC Engine | 54 | 104 | 0 |
| `T7JCF.DFM` | New Screen | 19 | 53 | 0 |
| `T7JCH.DFM` | New Screen | 22 | 56 | 0 |
| `T7JCL.DFM` | JC-L | 12 | 39 | 0 |
| `T7JCM.DFM` | JC-M | 28 | 62 | 0 |
| `T7JCN.DFM` | JC-N | 14 | 40 | 0 |
| `T7JCP.DFM` | JC-P Print Materials in WIP | 8 | 30 | 0 |
| `T7JCQ.DFM` | New Screen | 20 | 43 | 0 |
| `T7JCR.DFM` | New Screen | 23 | 53 | 0 |
| `T7JCRM.DFM` | New Screen | 5 | 29 | 0 |
| `T7JCS.DFM` | JC-S | 22 | 54 | 0 |

## Database tables (2)

Full field details are in `../../../samples/ddf/schema.md` (see per-table heading).

| Table | File on disk | Fields | Key fields (first 3) |
| ----- | ------------ | -----: | -------------------- |
| **WOHLABOR** | `WOHLABOR.B` | 58 | `MTWOLA_POSTED`, `MTWOLA_DATE`, `MTWOLA_EMP` |
| **WOLABOR** | `WOLABOR.B` | 58 | `MTWOLA_POSTED`, `MTWOLA_DATE`, `MTWOLA_EMP` |

## Notes & open questions

- *(populated per-module manually as deeper reading happens.)*
