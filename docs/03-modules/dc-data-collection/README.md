# Data Collection (Shop Floor) (DC)

Status: verified (auto-generated from the extracted schema, menu-code dump, and DFM inventory).

- **Module code**: `DC`
- **Tables**: 7 (prefixes `BKDC`)
- **UI forms**: 26 (prefixes `T7DC`, `T6DC`, `EVODC`)
- **Menu operations**: 7

## Menu operations

| Code | Operation | Legacy module file(s) |
| ---- | --------- | --------------------- |
| `DC-A` | Print Transfer Labels | J5ISDCA;J6ISDCA |
| `DC-D` | View/Print Labor Status | BKDCD;t6dcd |
| `DC-E` | Print Labor Tickets | BKDCE;T6DCE |
| `DC-F` | Print Employee Tickets | BKDCF;T6DCF |
| `DC-G` | Edit Labor Transactions | BKDCG;BKDCGMSG;CBKWOM;J5HDWOM |
| `DC-H` | Filelock on TOOL - | AUTODCH;BKDCH;UMCDCP |
| `DC-I` | View | BKDCI |

## UI forms (26)

| DFM file | Caption | fields | controls | tabs |
| -------- | ------- | -----: | -------: | ---: |
| `EVODCS.DFM` | New Screen | 0 | 2 | 0 |
| `EvoDCmenu.DFM` |  | 0 | 1 | 0 |
| `EvoDCmenu2.DFM` |  | 0 | 7 | 0 |
| `EvoDCsetup.DFM` | Create Workstation Setup | 3 | 11 | 0 |
| `T7DCA.DFM` |  | 0 | 1 | 0 |
| `T7DCA2.DFM` |  | 0 | 1 | 0 |
| `T7DCALabel.DFM` | Print Transfer Label | 16 | 45 | 0 |
| `T7DCANotes.DFM` | Notes Caption | 0 | 7 | 0 |
| `T7DCAPstdLab.dfm` | New Screen | 2 | 4 | 0 |
| `T7DCBSERIAL.DFM` | Enter Serial Numbers | 5 | 22 | 0 |
| `T7DCD.DFM` | DC-D | 24 | 59 | 0 |
| `T7DCE.DFM` | DC-E Print Labor Tickets | 6 | 24 | 0 |
| `T7DCF.DFM` | DC-E Print Employee Tickets | 4 | 22 | 0 |
| `T7DCG.DFM` |  | 0 | 1 | 0 |
| `T7DCH.DFM` | DC-H | 10 | 38 | 0 |
| `T7DCK.DFM` | DC-K | 7 | 28 | 0 |
| `T7DCL.DFM` |  | 0 | 1 | 0 |
| `T7DCM.DFM` |  | 0 | 1 | 0 |
| `T7DCN.DFM` | DC-N | 6 | 27 | 0 |
| `T7DCPSF.DFM` | HH-L  Paperless Shop Floor | 36 | 109 | 0 |
| `T7DCPSFComps.DFM` |  | 0 | 1 | 0 |
| `T7DCPSFECO.DFM` |  Eco | 10 | 35 | 0 |
| `T7DCSOLookup.DFM` |  | 0 | 1 | 0 |
| `t7DCPSFNotes.DFM` | Notes Caption | 0 | 12 | 0 |
| `t7DCina.DFM` | T7INA | 41 | 123 | 0 |
| `t7dcb.DFM` |  | 0 | 1 | 0 |

## Database tables (7)

Full field details are in `../../../samples/ddf/schema.md` (see per-table heading).

| Table | File on disk | Fields | Key fields (first 3) |
| ----- | ------------ | -----: | -------------------- |
| **BKDCCFG** | `BKDCCFG.B` | 7 | `BKDC_CFG_IDLEP`, `BKDC_CFG_IDLES`, `BKDC_CFG_BANKP` |
| **BKDCCLAB** | `BKDCCLAB.B` | 50 | `LAB_DATE`, `LAB_EMP`, `LAB_WOPRE` |
| **BKDCHLAB** | `BKDCHLAB.B` | 50 | `LAB_DATE`, `LAB_EMP`, `LAB_WOPRE` |
| **BKDCLAB** | `BKDCLAB.B` | 50 | `LAB_DATE`, `LAB_EMP`, `LAB_WOPRE` |
| **BKDCPLAB** | `BKDCPLAB.B` | 50 | `LAB_DATE`, `LAB_EMP`, `LAB_WOPRE` |
| **BKDCSHFT** | `BKDCSHFT.B` | 34 | `BKDC_SH_NAME1`, `BKDC_SH_NAME2`, `BKDC_SH_NAME3` |
| **BKDCTLAB** | `BKDCTLAB.B` | 50 | `LAB_DATE`, `LAB_EMP`, `LAB_WOPRE` |

## Notes & open questions

- *(populated per-module manually as deeper reading happens.)*
