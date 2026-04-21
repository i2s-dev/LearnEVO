# Work Orders (WO)

Status: verified (auto-generated from the extracted schema, menu-code dump, and DFM inventory).

- **Module code**: `WO`
- **Tables**: 30 (prefixes `WO`, `WORK`)
- **UI forms**: 68 (prefixes `T7WO`, `T6WO`, `BKWO`)
- **Menu operations**: 31

## Menu operations

| Code | Operation | Legacy module file(s) |
| ---- | --------- | --------------------- |
| `WO-A` | Enter Work Orders | BKWOA;ISTECH;ISWORPT1 |
| `WO-A-A` | Enter Work Orders - ECO Drawing Entry | BKWOA |
| `WO-B` | Change WO Status | BKWOB;ISWORPT2 |
| `WO-C` | Special Work Order Report | J5SMRPT3 |
| `WO-D` | Print Pick Lists | BKWOD |
| `WO-E` | Print Labor Cards/Labels | BKWOE;T6WOE |
| `WO-F` | Enter Labor | BKWOF |
| `WO-G` | Enter WO BOM | BKWOG;BKWOKB;ISWOG |
| `WO-H` | Enter Misc/Extra Costs | BKWOH |
| `WO-I` | Enter Finished Production | BKWOFA;BKWOI;BKWOIP~1;ISMULTIY;ISTECH |
| `WO-J` | Rebuild Work Orders | BKREBWO;BKWOJ;ISTECH |
| `WO-K-A` | Enter Work Order Routings | BKWOKA |
| `WO-K-B` | Enter WO BOM | BKWOKB |
| `WO-K-C` | Create Multi-Date Work Orders | BKWOKC |
| `WO-K-D` | Create Multi-Assy Work Orders | BKWOKD |
| `WO-K-E` | Swap Substitute Parts | BKWOKE |
| `WO-K-F` | Edit Sequence Started/Finished Dates | BKWOKF |
| `WO-K-G` | Recalculate Projected Hours | BKWOKG |
| `WO-K-L` | Quick Work Orders | NZQWO |
| `WO-L-A` | Print Work Order Status | t6wola |
| `WO-L-C` | Print Work Center Backlog | BKWOLC |
| `WO-L-D` | Print Projected Shipments | BKWOLD |
| `WO-L-E` | Print/Post Labor to Payroll | BKWOLE |
| `WO-L-F` | Print Work Order Shortage | BKWOLF;t6wolf |
| `WO-L-G` | Print Work Center by Key Component | BKWOLG |
| `WO-L-H` | Print Projected Hours Report | BKWOLH |
| `WO-L-I` | Print Allocations | BKWOLI |
| `WO-L-J` | Print Finished Work Order Report | ISWOLJ |
| `WO-M` | Batch Labor Entry | BKDCG;BKDCGMSG;CBKWOM;J5HDWOM |
| `WO-N` | Post Labor Batches | AUTODCH;BKDCH;UMCDCP |
| `WO-Q` | Convert Work Orders to Purchase Orders | CAWOPO;ISWOPO |

## UI forms (68)

| DFM file | Caption | fields | controls | tabs |
| -------- | ------- | -----: | -------: | ---: |
| `T7WOA.DFM` | New Screen | 69 | 171 | 3 |
| `T7WOAC.DFM` | New Screen | 78 | 183 | 0 |
| `T7WOACFG.DFM` | WO-A  Settings | 3 | 9 | 0 |
| `T7WOACPY.DFM` | New Screen | 3 | 13 | 0 |
| `T7WOAE.DFM` | New Screen | 100 | 247 | 4 |
| `T7WOAECO.DFM` |  Eco | 9 | 24 | 0 |
| `T7WOAMDT.DFM` |  | 0 | 8 | 0 |
| `T7WOASOLINES.DFM` |  | 0 | 2 | 0 |
| `T7WOB.DFM` | WO-B | 15 | 46 | 0 |
| `T7WOC.DFM` | WOC | 51 | 93 | 0 |
| `T7WOD.DFM` | WO-D | 28 | 59 | 0 |
| `T7WODATES.DFM` |  | 0 | 1 | 0 |
| `T7WOE.DFM` | IN-E Print Inventory Transactions | 5 | 26 | 0 |
| `T7WOF.DFM` | WO-F | 40 | 98 | 0 |
| `T7WOFA.DFM` | WO-F Backflush Material | 1 | 22 | 0 |
| `T7WOG.DFM` |  | 0 | 1 | 0 |
| `T7WOH.DFM` |  | 0 | 1 | 0 |
| `T7WOI.DFM` |  | 0 | 1 | 0 |
| `T7WOIASK.DFM` | Change Location | 18 | 43 | 0 |
| `T7WOJ.DFM` | WO-J | 11 | 38 | 0 |
| `T7WOJPRESERIALS.DFM` | WO-J Pre-Assigned Serial Numbers | 7 | 25 | 0 |
| `T7WOKA.DFM` | WO-K-A | 35 | 100 | 0 |
| `T7WOKACOPYROUT.DFM` | WO-K-A | 4 | 14 | 0 |
| `T7WOKAOPTS.DFM` | WO-K-A | 3 | 12 | 0 |
| `T7WOKB.DFM` |  | 0 | 1 | 0 |
| `T7WOKC.DFM` | WO-K-C | 4 | 21 | 0 |
| `T7WOKD.DFM` | WO-K-D | 30 | 60 | 0 |
| `T7WOKDQTY.DFM` | Enter Qty to Make | 16 | 34 | 0 |
| `T7WOKE.DFM` |  | 0 | 1 | 0 |
| `T7WOKF.DFM` | New Screen | 5 | 24 | 0 |
| `T7WOKG.DFM` | WO-K-G | 13 | 41 | 0 |
| `T7WOKJ.DFM` | WO-K-J | 11 | 32 | 0 |
| `T7WOKK.DFM` |  | 0 | 1 | 0 |
| `T7WOKL.DFM` |  | 0 | 1 | 0 |
| `T7WOKM.DFM` |  | 0 | 1 | 0 |
| `T7WOKMA.DFM` | New Screen | 3 | 21 | 0 |
| `T7WOKNA.DFM` | Live Work Center Schedule | 4 | 22 | 0 |
| `T7WOKNB.DFM` |  | 0 | 1 | 0 |
| `T7WOKNC.DFM` | Issue Part from Request | 18 | 50 | 0 |
| `T7WOKP.DFM` |  | 0 | 1 | 0 |
| `T7WOKS.DFM` |  | 0 | 1 | 0 |
| `T7WOKSA.DFM` | WO-K-SA | 10 | 33 | 0 |
| `T7WOKT.DFM` | New Screen | 11 | 36 | 0 |
| `T7WOLA.DFM` | WO-L-A | 61 | 116 | 0 |
| `T7WOLB.DFM` | WO-L-B | 48 | 99 | 0 |
| `T7WOLC.DFM` | WO-L-C | 22 | 56 | 0 |
| `T7WOLD.DFM` | WO-L-D | 26 | 65 | 0 |
| `T7WOLE.DFM` | WO-L-E | 7 | 31 | 0 |
| `T7WOLF.DFM` | WO-L-F | 48 | 99 | 0 |
| `T7WOLG.DFM` | WO-L-G | 32 | 65 | 0 |
| `T7WOLH.DFM` | WO-L-H | 15 | 43 | 0 |
| `T7WOLI.DFM` | WO-L-I | 32 | 71 | 0 |
| `T7WOLJ.DFM` | WO-L-J  Print Finished Work Order Report | 19 | 53 | 0 |
| `T7WOLK.DFM` | WO-L-K  Print WO Bill of Material | 23 | 48 | 0 |
| `T7WOLL.DFM` | WO-L-L | 11 | 38 | 0 |
| `T7WOLM.DFM` |  | 0 | 1 | 0 |
| `T7WOLN.DFM` | WO-L-N | 4 | 23 | 0 |
| `T7WOLO.DFM` | WC by Customer | 5 | 24 | 0 |
| `T7WONoteTLL.DFM` | WO Notes | 0 | 17 | 0 |
| `T7WOP.DFM` |  | 0 | 1 | 0 |
| `T7WOPO.DFM` | WO-PO | 13 | 36 | 0 |
| `T7WOPOR.DFM` | WO-PO Review | 8 | 20 | 0 |
| `T7WOS.DFM` |  | 0 | 1 | 0 |
| `T7WOTRWK.DFM` | Rework TO Stock WO | 8 | 30 | 0 |
| `T7woko.DFM` |  | 0 | 1 | 0 |
| `t7wogimp.DFM` | Import Material Issues | 4 | 17 | 0 |
| `t7woprio.DFM` |  | 0 | 1 | 0 |
| `t7woprio2.DFM` |  | 0 | 1 | 0 |

## Database tables (30)

Full field details are in `../../../samples/ddf/schema.md` (see per-table heading).

| Table | File on disk | Fields | Key fields (first 3) |
| ----- | ------------ | -----: | -------------------- |
| **WOBOM** | `WOBOM.B` | 24 | `WOBOM_OPER`, `WOBOM_WOPRE`, `WOBOM_WOSUF` |
| **WOBOMCHG** | `WOBOMCHG.B` | 17 | `WBOM_CHG_WOPRE`, `WBOM_CHG_WOSUF`, `WBOM_CHG_PARENT` |
| **WOBOMHRM** | `WOBOMHRM.B` | 7 | `WOBOM_RM_WOPRE`, `WOBOM_RM_WOSUF`, `WOBOM_RM_PARENT` |
| **WOBOMREM** | `WOBOMREM.B` | 7 | `WOBOM_RM_WOPRE`, `WOBOM_RM_WOSUF`, `WOBOM_RM_PARENT` |
| **WODATE** | `WODATE.B` | 13 | `WODATE_WOPRE`, `WODATE_WOSUF`, `WODATE_START` |
| **WOELABOR** | `WOELABOR.B` | 58 | `MTWOLA_POSTED`, `MTWOLA_DATE`, `MTWOLA_EMP` |
| **WOEMAT** | `WOEMAT.B` | 17 | `WOMAT_DATE`, `WOMAT_WOPRE`, `WOMAT_WOSUF` |
| **WOERECV** | `WOERECV.B` | 11 | `MTWOR_WOPRE`, `MTWOR_WOSUF`, `MTWOR_DATE` |
| **WOEXCHG** | `WOEXCHG.B` | 10 | `MTWO_EX_WOPRE`, `MTWO_EX_WOSUF`, `MTWO_EX_DATE` |
| **WOHBOM** | `WOHBOM.B` | 24 | `WOBOM_OPER`, `WOBOM_WOPRE`, `WOBOM_WOSUF` |
| **WOHDATE** | `WOHDATE.B` | 13 | `WODATE_WOPRE`, `WODATE_WOSUF`, `WODATE_START` |
| **WOHEXCHG** | `WOHEXCHG.B` | 10 | `MTWO_EX_WOPRE`, `MTWO_EX_WOSUF`, `MTWO_EX_DATE` |
| **WOHLABOR** | `WOHLABOR.B` | 58 | `MTWOLA_POSTED`, `MTWOLA_DATE`, `MTWOLA_EMP` |
| **WOHMAT** | `WOHMAT.B` | 17 | `WOMAT_DATE`, `WOMAT_WOPRE`, `WOMAT_WOSUF` |
| **WOHRECV** | `WOHRECV.B` | 11 | `MTWOR_WOPRE`, `MTWOR_WOSUF`, `MTWOR_DATE` |
| **WOHROUT** | `WOHROUT.B` | 81 | `MTWORO_WOPRE`, `MTWORO_WOSUF`, `MTWORO_OPER` |
| **WOLABOR** | `WOLABOR.B` | 58 | `MTWOLA_POSTED`, `MTWOLA_DATE`, `MTWOLA_EMP` |
| **WOLABRPT** | `WOLABRPT.B` | 58 | `MTWOLA_POSTED`, `MTWOLA_DATE`, `MTWOLA_EMP` |
| **WOMAT** | `WOMAT.B` | 17 | `WOMAT_DATE`, `WOMAT_WOPRE`, `WOMAT_WOSUF` |
| **WORECV** | `WORECV.B` | 11 | `MTWOR_WOPRE`, `MTWOR_WOSUF`, `MTWOR_DATE` |
| **WORKACHG** | `WORKACHG.B` | 25 | `WO_CHG_WOPRE`, `WO_CHG_WOSUF`, `WO_CHG_CODE` |
| **WORKCHG** | `WORKCHG.B` | 25 | `WO_CHG_WOPRE`, `WO_CHG_WOSUF`, `WO_CHG_CODE` |
| **WORKCTR** | `WORKCTR.B` | 47 | `MTWC_WC`, `MTWC_WCDESC`, `MTWC_DEPT` |
| **WORKHORD** | `WORKHORD.B` | 74 | `MTWO_WIP_WOPRE`, `MTWO_WIP_WOSUF`, `MTWO_WIP_BLANK` |
| **WORKORD** | `WORKORD.B` | 74 | `MTWO_WIP_WOPRE`, `MTWO_WIP_WOSUF`, `MTWO_WIP_BLANK` |
| **WORKSORD** | `WORKSORD.B` | 74 | `MTWO_WIP_WOPRE`, `MTWO_WIP_WOSUF`, `MTWO_WIP_BLANK` |
| **WOROCHG** | `WOROCHG.B` | 24 | `WORO_CHG_WOPRE`, `WORO_CHG_WOSUF`, `WORO_CHG_PART` |
| **WOROUT** | `WOROUT.B` | 81 | `MTWORO_WOPRE`, `MTWORO_WOSUF`, `MTWORO_OPER` |
| **WOROUTMP** | `WOROUTMP.B` | 81 | `MTWORO_WOPRE`, `MTWORO_WOSUF`, `MTWORO_OPER` |
| **WOSROUT** | `WOSROUT.B` | 81 | `MTWORO_WOPRE`, `MTWORO_WOSUF`, `MTWORO_OPER` |

## Notes & open questions

- *(populated per-module manually as deeper reading happens.)*
