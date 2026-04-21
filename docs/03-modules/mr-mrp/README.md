# MRP (Material Requirements Planning) (MR)

Status: verified (auto-generated from the extracted schema, menu-code dump, and DFM inventory).

- **Module code**: `MR`
- **Tables**: 4 (prefixes `BKMR`, `MTMR`)
- **UI forms**: 18 (prefixes `T7MR`, `T6MR`, `BKMR`)
- **Menu operations**: 12

## Menu operations

| Code | Operation | Legacy module file(s) |
| ---- | --------- | --------------------- |
| `MR-A` | Enter Forecast | BKMRA;BKMRADE |
| `MR-B` | Print Forecast | BKMRB |
| `MR-C` | Reset Forecast | BKMRC |
| `MR-D` | Enter MRP Parameters | BKMRD |
| `MR-E` | Print MRP Parameters | BKMRE |
| `MR-F` | Generate Material Requirements | AUTOMRF;BKMRF |
| `MR-G` | Print Material Requirements | BKMRG |
| `MR-H` | Print Order Action Report | BKMRH |
| `MR-I` | Generate Work Orders | BKMRI |
| `MR-J` | Generate Purchase Orders | BKMRJ;BKMRK |
| `MR-K` | Generate RFQ's | BKMRJ;BKMRK |
| `MR-L` | Print Planned Orders Report | BKMRL |

## UI forms (18)

| DFM file | Caption | fields | controls | tabs |
| -------- | ------- | -----: | -------: | ---: |
| `T7MRA.DFM` |  | 0 | 1 | 0 |
| `T7MRADE.DFM` | New Screen | 9 | 33 | 0 |
| `T7MRB.DFM` | MR-B | 13 | 42 | 0 |
| `T7MRC.DFM` | New Screen | 16 | 45 | 0 |
| `T7MRD.DFM` | New Screen | 52 | 134 | 0 |
| `T7MRE.DFM` | New Screen | 10 | 35 | 0 |
| `T7MRF.DFM` | MR-F | 41 | 91 | 0 |
| `T7MRG.DFM` | MR-G | 25 | 61 | 0 |
| `T7MRH.DFM` | MR-H | 32 | 91 | 0 |
| `T7MRI.DFM` | MR-I | 24 | 58 | 0 |
| `T7MRIR.DFM` | Review QTY'#39's | 5 | 13 | 0 |
| `T7MRIX.DFM` | New Screen | 18 | 52 | 0 |
| `T7MRJ.DFM` | MR-J | 29 | 77 | 0 |
| `T7MRJR.DFM` | MR-J Review | 10 | 24 | 0 |
| `T7MRJX.DFM` |  | 0 | 1 | 0 |
| `T7MRL.DFM` | MR-L | 3 | 22 | 0 |
| `T7MRN.DFM` | MR-N | 5 | 23 | 0 |
| `T7MRO.DFM` | MR-O | 1 | 17 | 0 |

## Database tables (4)

Full field details are in `../../../samples/ddf/schema.md` (see per-table heading).

| Table | File on disk | Fields | Key fields (first 3) |
| ----- | ------------ | -----: | -------------------- |
| **BKMRPFC** | `BKMRPFC.B` | 9 | `BKMRP_FC_PART`, `BKMRP_FC_DATE`, `BKMRP_FC_QTY` |
| **BKMRPPO** | `BKMRPPO.B` | 16 | `BKMRP_PO_UID`, `BKMRP_PO_VEND`, `BKMRP_PO_DATE` |
| **BKMRPSW** | `BKMRPSW.B` | 2 | `BKMRP_SW_PART`, `BKMRP_SW_SW` |
| **MTMRP** | `MTMRP.B` | 13 | `MTMRP_PARTNO`, `MTMRP_DATE`, `MTMRP_QTY` |

## Notes & open questions

- *(populated per-module manually as deeper reading happens.)*
