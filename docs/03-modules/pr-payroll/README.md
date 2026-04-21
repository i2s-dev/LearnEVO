# Payroll (PR)

Status: verified (auto-generated from the extracted schema, menu-code dump, and DFM inventory).

- **Module code**: `PR`
- **Tables**: 16 (prefixes `BKPR`)
- **UI forms**: 40 (prefixes `T7PR`, `T6PR`, `BKPR`)
- **Menu operations**: 29

## Menu operations

| Code | Operation | Legacy module file(s) |
| ---- | --------- | --------------------- |
| `PR-A` | Edit W-2 Data | BKPRA;BKPRP;BKPRQ |
| `PR-B` | Enter Pay Info | BKPRB;BKPRD;t6prd |
| `PR-C` | Print Payroll Register | BKPRC |
| `PR-D` | Print Payroll Checks | BKPRB;BKPRD;t6prd |
| `PR-E` | Print Employee Info | BKPRE |
| `PR-F` | Maintain Tax Tables | BKPRF |
| `PR-G` | Void Payroll Checks | BKPRG |
| `PR-H` | Transfer Liabilities to AP | BKPRH |
| `PR-I` | Print Pay History | BKPRI |
| `PR-J` | Enter Time Cards | BKPRJ;BKPRJA;BKPRJB |
| `PR-J-A` | Import Time Cards | ISPRJDE |
| `PR-K` | Print/Post Time Cards | BKPRK |
| `PR-L-A` | Print Quarterly Info | BKPRLA |
| `PR-L-B` | Print QTD Earnings Register | BKPRLB |
| `PR-L-C` | Print QTD Taxable Earnings | BKPRLC |
| `PR-L-D` | Print Detail Earnings Ledger | BKPRLD |
| `PR-L-E` | Print Detail Deductions Ledger | BKPRLE |
| `PR-L-F` | Print Subject To Report | BKPRLF;T6PRLF |
| `PR-L-H` | Print 940 Report | BKPRLH |
| `PR-L-I` | Print W-2 Forms | BKPRLI;T6PRLI |
| `PR-L-J` | Print California DE6 Form | BKPRLJ |
| `PR-L-K` | Print Payroll Hours | BKPRLK |
| `PR-L-M` | Print Employer Contributions | BKPRLM |
| `PR-L-N` | Print Payroll Wages Detail | BKPRLN |
| `PR-L-P` | Print Employee Raises | BKPRLP;BKPRLQ |
| `PR-M` | Payroll Defaults | BKPRM |
| `PR-N` | Purge Payroll History | BKPRN |
| `PR-O` | Payroll Year End Routine | BKPRO |
| `PR-P` | Enter Employee Raises | BKPRP;BKPRQ |

## UI forms (40)

| DFM file | Caption | fields | controls | tabs |
| -------- | ------- | -----: | -------: | ---: |
| `T7PRA.DFM` |  | 0 | 1 | 0 |
| `T7PRB.DFM` |  | 0 | 1 | 0 |
| `T7PRC.DFM` | PR-C | 10 | 33 | 0 |
| `T7PRD.DFM` |  | 0 | 1 | 0 |
| `T7PRDIVFIX.DFM` | New Screen | 2 | 10 | 0 |
| `T7PRE.DFM` | PR-E | 4 | 22 | 0 |
| `T7PRF.DFM` |  | 0 | 1 | 0 |
| `T7PRFIX.DFM` |  | 0 | 1 | 0 |
| `T7PRG.DFM` | PR-G | 9 | 30 | 0 |
| `T7PRH.DFM` | PR-H | 82 | 117 | 0 |
| `T7PRI.DFM` | PR-I | 7 | 27 | 0 |
| `T7PRJ.DFM` |  | 0 | 1 | 0 |
| `T7PRJCSYNC.DFM` | New Screen | 2 | 10 | 0 |
| `T7PRK.DFM` | PR-K  Print/Post Time Cards | 13 | 45 | 0 |
| `T7PRLA.DFM` | PR-L-A | 6 | 27 | 0 |
| `T7PRLB.DFM` | PR-L-B | 8 | 30 | 0 |
| `T7PRLC.DFM` | PR-L-C | 16 | 47 | 0 |
| `T7PRLD.DFM` | PR-L-D | 8 | 30 | 0 |
| `T7PRLE.DFM` | PR-L-E  Print Detail Deductions Ledger | 10 | 32 | 0 |
| `T7PRLF.DFM` | PR-L-F | 21 | 52 | 0 |
| `T7PRLG.DFM` | PR-L-G | 40 | 97 | 0 |
| `T7PRLH.DFM` | PR-LH | 54 | 112 | 0 |
| `T7PRLI.DFM` |  | 0 | 1 | 0 |
| `T7PRLJ.DFM` | PR-L-J | 11 | 35 | 0 |
| `T7PRLK.DFM` | PR-L-K  Print Payroll Hours | 9 | 31 | 0 |
| `T7PRLM.DFM` | PR-L-M | 8 | 30 | 0 |
| `T7PRLN.DFM` | PR-L-N  Print Payroll Wages Detail | 8 | 30 | 0 |
| `T7PRLO.DFM` | PR-L-O | 8 | 30 | 0 |
| `T7PRLP.DFM` | PR-L-P | 10 | 33 | 0 |
| `T7PRLQ.DFM` | PR-L-Q | 8 | 31 | 0 |
| `T7PRM.DFM` |  | 0 | 1 | 0 |
| `T7PRN.DFM` | New Screen | 7 | 28 | 0 |
| `T7PRO.DFM` | New Screen | 1 | 17 | 0 |
| `T7PROGINFO.DFM` |  | 0 | 1 | 0 |
| `T7PRP.DFM` |  | 0 | 1 | 0 |
| `T7PRQ.DFM` |  | 0 | 1 | 0 |
| `T7PRQTRCHK.DFM` | New Screen | 2 | 24 | 0 |
| `T7PRS.DFM` | Enter Employee Password | 5 | 29 | 0 |
| `T7ProcessData.DFM` | Process Data | 0 | 9 | 0 |
| `t7pretag.DFM` | New Screen | 0 | 3 | 0 |

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
