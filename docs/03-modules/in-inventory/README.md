# Inventory (IN)

Status: verified (auto-generated from the extracted schema, menu-code dump, and DFM inventory).

- **Module code**: `IN`
- **Tables**: 19 (prefixes `BKIC`, `MTIC`)
- **UI forms**: 67 (prefixes `T7IN`, `T6IN`, `BKIN`)
- **Menu operations**: 40

## Menu operations

| Code | Operation | Legacy module file(s) |
| ---- | --------- | --------------------- |
| `IN-A` | Inventory Inquiry | BKINA;lbkina.run;t6INA;t6INAC |
| `IN-B` | Enter Inventory | BKINB;ISTECH;t6INB;t6INBC |
| `IN-C` | Enter Inventory Adjustments | BKINC |
| `IN-D` | Print Reorder Report | BKIND;T6IND |
| `IN-E` | Print Inventory Transactions | BKINE |
| `IN-F` | Print Inventory Value | BKINF |
| `IN-G` | Print Inventory Labels | BKING;T6ING |
| `IN-H` | Print Inventory Listing | BKINH;t6inh |
| `IN-I` | Print Inventory General Info | BKINI |
| `IN-J` | Print Physical Check | BKINJ |
| `IN-K` | IN-L-E     SM-J- | BKINK;ISSMJS |
| `IN-L-A` | Enter Standard Costs | BKINLA;FIXSTD |
| `IN-L-B` | Enter/Assign Locations | BKINLB |
| `IN-L-C` | Enter Customer Cross-Reference | BKINLC |
| `IN-L-D` | Print Customer Cross-Reference | BKINLD |
| `IN-L-E` | Update Material Standard Costs | BKINLE |
| `IN-L-F` | Enter Material Dimensions | BKINLF |
| `IN-L-G` | Print Material Dimensions | BKINLG |
| `IN-L-H` | Edit FIFO/LIFO Buckets | BKINLH |
| `IN-L-I` | Change Inventory Costing Method | BKINLI |
| `IN-L-J` | Transfer Inventory | BKINLJ;ISINLJ |
| `IN-L-K` | Inventory Exceptions Report | BKINLK |
| `IN-L-L` | BOM report | BKINLL |
| `IN-L-M` | Multi-Transfer Inventory | ISINLM;t6isinlm |
| `IN-L-N` | Copy Item | ISINLN |
| `IN-L-O` | Inventory utilites | BKACT;ISINLO;ISINLOA |
| `IN-L-P` | Multi-Co-Transfer Inventory | ISICT;T6ISICT |
| `IN-L-S` | Rebuild Stock Status | AUTOIND |
| `IN-L-T` | Reset Inventory Cycle Codes | ISINLT |
| `IN-L-U` | Recal UOH From FIFO Layers | ISINLU |
| `IN-L-V` | Archive Obsolete Inventory - | ISINLOA |
| `IN-M-C` | Global Price Change | BKINMC |
| `IN-M-E` | Print Price Code Prices | BKINMI |
| `IN-M-G` | Print Dicount Code Prices | BKINMI |
| `IN-M-I` | Print Contract Prices | BKINMI |
| `IN-N-A` | Print Month End Inventory Costing | BKINNA |
| `IN-N-B` | Print Shipments Costing | BKINNB |
| `IN-N-C` | Print Closed Work Orders Costing | BKINNC |
| `IN-N-D` | Print Inventory Audit | BKINND;ISINND |
| `IN-O` | User Defined Inventory Transactions | BKINO;T6INO |

## UI forms (67)

| DFM file | Caption | fields | controls | tabs |
| -------- | ------- | -----: | -------: | ---: |
| `T7INA.DFM` |  | 0 | 1 | 0 |
| `T7INAACDOC.DFM` |  Accutron Documentation | 4 | 23 | 0 |
| `T7INAALO.DFM` |  | 0 | 7 | 0 |
| `T7INACMP.DFM` | Compliance | 34 | 68 | 0 |
| `T7INAFORECAST.DFM` |  | 4 | 8 | 0 |
| `T7INAPRC.DFM` | Customer Price | 9 | 25 | 0 |
| `T7INASPC.DFM` |  Specifications | 16 | 23 | 0 |
| `T7INAUDF.DFM` |  Specifications | 33 | 73 | 0 |
| `T7INAUSG.DFM` |  | 4 | 8 | 0 |
| `T7INAWIP.DFM` | Item In WIP | 7 | 19 | 0 |
| `T7INB.DFM` |  | 0 | 1 | 0 |
| `T7INB2DB.DFM` |  | 0 | 1 | 0 |
| `T7INBCMP.DFM` | Compliance | 34 | 68 | 0 |
| `T7INBECO.DFM` |  | 0 | 1 | 0 |
| `T7INBLNK.DFM` |  | 0 | 1 | 0 |
| `T7INBMFG.DFM` |  | 0 | 1 | 0 |
| `T7INBMRP.DFM` |  MRP Settings | 15 | 33 | 0 |
| `T7INBSPC.DFM` |  Specifications | 15 | 22 | 0 |
| `T7INBUDF.DFM` |  Specifications | 33 | 73 | 0 |
| `T7INBVND.DFM` |  | 0 | 1 | 0 |
| `T7INC.DFM` | IN-C Enter Inventory Adjustments | 60 | 138 | 0 |
| `T7IND.DFM` | IN-D Print Record Report | 53 | 120 | 2 |
| `T7INDPO.DFM` | IN-D  PO | 1 | 19 | 0 |
| `T7INE.DFM` | IN-E Print Inventory Transactions | 17 | 47 | 0 |
| `T7INF.DFM` | IN-F Print inventory Value | 43 | 87 | 0 |
| `T7ING.DFM` | IN-G  Print Inventory Labels | 85 | 204 | 0 |
| `T7INGimport.DFM` | IN-G-A  Import and Print Inventory Labels | 17 | 49 | 0 |
| `T7INH.DFM` | IN-H  Print Inventory Listning | 20 | 55 | 0 |
| `T7INI.DFM` | IN-I  Print Inventory General Info | 10 | 37 | 0 |
| `T7INJ.DFM` | IN-J  Print Physikal Check | 20 | 51 | 0 |
| `T7INK.DFM` |  | 0 | 1 | 0 |
| `T7INLA.DFM` | IN-L-A | 25 | 77 | 0 |
| `T7INLB.DFM` | IN-L-B | 27 | 71 | 0 |
| `T7INLC.DFM` | IN-L-C | 9 | 33 | 0 |
| `T7INLD.DFM` | IN-L-D  Print Customer Cross-Reference | 10 | 36 | 0 |
| `T7INLE.DFM` | IN-L-E | 12 | 38 | 0 |
| `T7INLF.DFM` |  | 0 | 1 | 0 |
| `T7INLG.DFM` | IN-L-G | 12 | 40 | 0 |
| `T7INLH.DFM` |  | 0 | 1 | 0 |
| `T7INLI.DFM` | IN-L-I | 2 | 25 | 0 |
| `T7INLJ.DFM` | IN-L-J Transfer Inventory | 28 | 81 | 0 |
| `T7INLK.DFM` | IN-L-K | 33 | 69 | 0 |
| `T7INLL.DFM` | IN-L-L | 10 | 36 | 0 |
| `T7INLM.DFM` |  | 0 | 1 | 0 |
| `T7INLN.DFM` |  | 0 | 1 | 0 |
| `T7INLO.DFM` | GL-G | 41 | 77 | 0 |
| `T7INLOA.DFM` | IN-L-O-A | 13 | 42 | 0 |
| `T7INLQ.DFM` |  | 0 | 1 | 0 |
| `T7INLR.DFM` |  | 0 | 1 | 0 |
| `T7INLS.DFM` | New Screen | 3 | 20 | 0 |
| `T7INLT.DFM` | IN-L-T | 40 | 68 | 0 |
| `T7INLV.DFM` | BASE Blank T7 SCREEN | 10 | 36 | 0 |
| `T7INM.DFM` | IN-M  Summary Reorder Report | 21 | 55 | 0 |
| `T7INNA.DFM` | IN-N-A Print Month End Inventory Costing | 18 | 52 | 0 |
| `T7INNB.DFM` | IN-N-B Print Shipments Costing | 13 | 42 | 0 |
| `T7INNC.DFM` | IN-N-C Print Closed Work Orders Costing | 10 | 37 | 0 |
| `T7INND.DFM` | IN-N-D Print Inventory to GL Exceptions Report | 12 | 32 | 0 |
| `T7INO.DFM` | IN-E | 65 | 136 | 2 |
| `T7INP.DFM` | IN-P | 39 | 87 | 0 |
| `T7INS.DFM` |  | 0 | 1 | 0 |
| `T7INVARCH.DFM` | New Screen | 2 | 18 | 0 |
| `T7INVENTORY.DFM` |  | 0 | 1 | 0 |
| `T7INXFERNUM.DFM` |  | 0 | 2 | 0 |
| `t7INBE.DFM` |  | 0 | 1 | 0 |
| `t7inaC.DFM` | T7INA | 53 | 178 | 0 |
| `t7inaE.DFM` |  | 0 | 1 | 0 |
| `t7inbc.DFM` | IN-B  Enter Inventory | 67 | 164 | 0 |

## Database tables (19)

Full field details are in `../../../samples/ddf/schema.md` (see per-table heading).

| Table | File on disk | Fields | Key fields (first 3) |
| ----- | ------------ | -----: | -------------------- |
| **BKICALTD** | `BKICALTD.B` | 16 | `BKIC_ALTD_PCODE`, `BKIC_ALTD_TYPE`, `BKIC_ALTD_DESC` |
| **BKICALTP** | `BKICALTP.B` | 6 | `BKIC_ALTP_TYPE`, `BKIC_ALTP_PCODE`, `BKIC_ALTP_ACODE` |
| **BKICAMTR** | `BKICAMTR.B` | 64 | `BKIC_PROD_CODE`, `BKIC_PROD_DESC`, `BKIC_PROD_TYPE` |
| **BKICAPMA** | `BKICAPMA.B` | 85 | `BKIC_PMAT_CUST`, `BKIC_PMAT_PCODE`, `BKIC_PMAT_PNUM` |
| **BKICDIM** | `BKICDIM.B` | 47 | `BKICDIM_PARTNO`, `BKICDIM_PARENT`, `BKICDIM_FIRST` |
| **BKICELOC** | `BKICELOC.B` | 32 | `BKIC_LOC_PROD`, `BKIC_LOC_CODE`, `BKIC_LOC_UOH` |
| **BKICEMTR** | `BKICEMTR.B` | 64 | `BKIC_PROD_CODE`, `BKIC_PROD_DESC`, `BKIC_PROD_TYPE` |
| **BKICLOC** | `BKICLOC.B` | 32 | `BKIC_LOC_PROD`, `BKIC_LOC_CODE`, `BKIC_LOC_UOH` |
| **BKICLOCM** | `BKICLOCM.B` | 12 | `BKIC_LOCM_CODE`, `BKIC_LOCM_NAME`, `BKIC_LOCM_ADDR1` |
| **BKICMFG** | `BKICMFG.B` | 6 | `BKIC_MFG_PCODE`, `BKIC_MFG_MANUF`, `BKIC_MFG_MCODE` |
| **BKICMSTR** | `BKICMSTR.B` | 64 | `BKIC_PROD_CODE`, `BKIC_PROD_DESC`, `BKIC_PROD_TYPE` |
| **BKICPMAT** | `BKICPMAT.B` | 85 | `BKIC_PMAT_CUST`, `BKIC_PMAT_PCODE`, `BKIC_PMAT_PNUM` |
| **BKICREF** | `BKICREF.B` | 8 | `BKIC_REF_CUST`, `BKIC_REF_CODE`, `BKIC_REF_PDESC` |
| **BKICREQ** | `BKICREQ.B` | 41 | `BKIC_REQ_STATUS`, `BKIC_REQ_BY`, `BKIC_REQ_IDATE` |
| **BKICTAX** | `BKICTAX.B` | 46 | `BKIC_TAX_STATE`, `BKIC_TAX_LOCAL`, `BKIC_TAX_NAME` |
| **BKICVAL** | `BKICVAL.B` | 4 | `BKIC_VAL_CODE`, `BKIC_VAL_DATE`, `BKIC_VAL_TOTVL` |
| **MTICAMTR** | `MTICAMTR.B` | 108 | `MTIC_PROD_CLASS`, `MTIC_PROD_CODE`, `MTIC_PROD_DESC` |
| **MTICEMTR** | `MTICEMTR.B` | 108 | `MTIC_PROD_CLASS`, `MTIC_PROD_CODE`, `MTIC_PROD_DESC` |
| **MTICMSTR** | `MTICMSTR.B` | 108 | `MTIC_PROD_CLASS`, `MTIC_PROD_CODE`, `MTIC_PROD_DESC` |

## Notes & open questions

- *(populated per-module manually as deeper reading happens.)*
