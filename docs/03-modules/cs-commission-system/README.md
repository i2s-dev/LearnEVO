# Commission System (CS)

Status: verified (auto-generated from the extracted schema, menu-code dump, and DFM inventory).

- **Module code**: `CS`
- **Tables**: 16 (prefixes `BKCS`, `BKPR`)
- **UI forms**: 12 (prefixes `T7CS`, `T6CS`)
- **Menu operations**: 16

## Menu operations

| Code | Operation | Legacy module file(s) |
| ---- | --------- | --------------------- |
| `CS-A` | Enter Salespersons | BKCSA |
| `CS-B` | Enter Vendors | BKAPA;BKCSB;BKPOP |
| `CS-C` | Print Salespersons Info | BKCSC |
| `CS-D` | Transfer Sales Commissions | BKCSD |
| `CS-E` | Print Commission Detail | BKCSE;BKCSE1 |
| `CS-F` | Print Commission Summary | BKCSF |
| `CS-G` | Print Slsp1 Commission Detail | BKCSG |
| `CS-H` | Print Slsp1 Commission Summary | BKCSH |
| `CS-I` | Print Slsp2 Commission Detail | BKCSI |
| `CS-J` | Print Slsp2 Commission Summary | BKCSJ |
| `CS-L` | Print Price Code Commissions | BKINMI |
| `CS-N` | Print Contract Price Commissions | BKINMI |
| `CS-O` | Print Commission Earned Detail | BKCSOC;BKCSOI |
| `CS-P` | Print Commissions Due Summary | BKCSP |
| `CS-Q` | Commission Year End Routine | bkcsq.run |
| `CS-R` | View Salespersons Booking Info | j6crprbk |

## UI forms (12)

| DFM file | Caption | fields | controls | tabs |
| -------- | ------- | -----: | -------: | ---: |
| `T7CSA.DFM` | New Screen | 11 | 35 | 0 |
| `T7CSB.DFM` | CS-B  View Salespersons Info | 87 | 133 | 0 |
| `T7CSC.DFM` | CS-C  Print Salespersons Info | 5 | 22 | 0 |
| `T7CSD.DFM` |  | 0 | 1 | 0 |
| `T7CSDE.DFM` | Rep Link Import | 19 | 55 | 0 |
| `T7CSDO.DFM` |  | 0 | 1 | 0 |
| `T7CSDX.DFM` |  | 0 | 1 | 0 |
| `T7CSE.DFM` | CS-E  Print Commission Detail | 10 | 34 | 0 |
| `T7CSF.DFM` | CS-F  Print Commission Summary | 9 | 30 | 0 |
| `T7CSI.DFM` | Evo Master Inquiry | 9 | 30 | 0 |
| `T7CSO.DFM` | BASE Blank T7 SCREEN | 28 | 81 | 0 |
| `T7CSP.DFM` | CS-P  Print Commission Summary | 7 | 30 | 0 |

## Database tables (16)

Full field details are in `../../../samples/ddf/schema.md` (see per-table heading).

| Table | File on disk | Fields | Key fields (first 3) |
| ----- | ------------ | -----: | -------------------- |
| **BKPRACOM** | `BKPRACOM.B` | 12 | `BKPR_COMM_SLSP`, `BKPR_COMM_CCODE`, `BKPR_COMM_INVNM` |
| **BKPRAGNT** | `BKPRAGNT.B` | 4 | `BKPR_AGNT_NUM`, `BKPR_AGNT_CODE`, `BKPR_AGNT_GLACT` |
| **BKPRBOOK** | `BKPRBOOK.B` | 87 | `BKPR_SLS_EMPNUM`, `BKPR_SLS_CLASS_1`, `BKPR_SLS_CLASS_2` |
| **BKPRCOMM** | `BKPRCOMM.B` | 12 | `BKPR_COMM_SLSP`, `BKPR_COMM_CCODE`, `BKPR_COMM_INVNM` |
| **BKPRCURP** | `BKPRCURP.B` | 127 | `BKPR_CURP_EMPNM`, `BKPR_CURP_PRDTE`, `BKPR_CURP_ACTNM` |
| **BKPRFTAX** | `BKPRFTAX.B` | 47 | `BKPR_TAX_CODE`, `BKPR_TAX_DESC`, `BKPR_TAX_ALLOW` |
| **BKPRGLFL** | `BKPRGLFL.B` | 664 | `BKPR_GL_STCODE`, `BKPR_GL_DEPT`, `BKPR_GL_FITACCT` |
| **BKPRHCOM** | `BKPRHCOM.B` | 12 | `BKPR_COMM_SLSP`, `BKPR_COMM_CCODE`, `BKPR_COMM_INVNM` |
| **BKPRHIST** | `BKPRHIST.B` | 127 | `BKPR_CURP_EMPNM`, `BKPR_CURP_PRDTE`, `BKPR_CURP_ACTNM` |
| **BKPRINFO** | `BKPRINFO.B` | 128 | `BKPR_INFO_NUM`, `BKPR_INFO_DDEP`, `BKPR_INFO_REVDT_1` |
| **BKPRMSTR** | `BKPRMSTR.B` | 384 | `BKPR_EMP_NUM`, `BKPR_EMP_FNMI`, `BKPR_EMP_LNME` |
| **BKPRSALE** | `BKPRSALE.B` | 87 | `BKPR_SLS_EMPNUM`, `BKPR_SLS_CLASS_1`, `BKPR_SLS_CLASS_2` |
| **BKPRSTFL** | `BKPRSTFL.B` | 2 | `BKPR_ST_STCODE`, `BKPR_ST_TAXNUM` |
| **BKPRTC** | `BKPRTC.B` | 7 | `BKPR_TC_EMP`, `BKPR_TC_DATE`, `BKPR_TC_START` |
| **BKPRTCFG** | `BKPRTCFG.B` | 205 | `BKPRT_CFG_KEY`, `BKPRT_CFG_NAME_1`, `BKPRT_CFG_NAME_2` |
| **BKPRW2** | `BKPRW2.B` | 384 | `BKPR_EMP_NUM`, `BKPR_EMP_FNMI`, `BKPR_EMP_LNME` |

## Notes & open questions

- *(populated per-module manually as deeper reading happens.)*
