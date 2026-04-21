# General Ledger (GL)

Status: verified (auto-generated from the extracted schema, menu-code dump, and DFM inventory).

- **Module code**: `GL`
- **Tables**: 28 (prefixes `BKGL`)
- **UI forms**: 24 (prefixes `T7GL`, `T6GL`, `BKGL`)
- **Menu operations**: 16

## Menu operations

| Code | Operation | Legacy module file(s) |
| ---- | --------- | --------------------- |
| `GL-A` | Edit Budgets | BKGLA |
| `GL-B` | Add new GJ Transaction | BKGLB |
| `GL-D` | Print Journals | BKGLD |
| `GL-F` | Print Financial Statements | BKGLF |
| `GL-G` | Print GL Code and Description | BKGLG |
| `GL-H` | Print Chart of Accounts | BKGLH |
| `GL-I` | Print Check Register | BKGLI |
| `GL-J` | Reconcile Check Register | BKGLJ |
| `GL-K` | Transfer Bank Account Funds | BKGLK |
| `GL-M` | Generate Recurring GJ Transactions | BKGLM |
| `GL-N` | Print Custom Statements | BKGLN |
| `GL-O` | Print/Post GL Batches | BKGLO;t6glo |
| `GL-P` | Edit GL Batch Entries | BKGLP |
| `GL-Q` | Reverse Batch Posting | BKGLQ |
| `GL-R` | Business Status | ISBS |
| `GL-S` | View GL Journal Notes | BKGLS |

## UI forms (24)

| DFM file | Caption | fields | controls | tabs |
| -------- | ------- | -----: | -------: | ---: |
| `T7GLA.DFM` | GL-A | 113 | 162 | 0 |
| `T7GLARCH.DFM` |  | 2 | 19 | 0 |
| `T7GLB.DFM` |  | 0 | 1 | 0 |
| `T7GLBLIST.DFM` |  | 0 | 1 | 0 |
| `T7GLC.DFM` | GL-C | 24 | 61 | 0 |
| `T7GLD.DFM` | GL-D | 14 | 47 | 0 |
| `T7GLE.DFM` | GL-E | 18 | 51 | 0 |
| `T7GLE2.DFM` | GL-E | 15 | 39 | 0 |
| `T7GLESPEED.DFM` | GL-E | 16 | 48 | 0 |
| `T7GLF.DFM` | GL- F | 98 | 177 | 0 |
| `T7GLG.DFM` | GL-G | 6 | 25 | 0 |
| `T7GLH.DFM` | GL- H | 16 | 36 | 0 |
| `T7GLI.DFM` | GL- I | 12 | 40 | 0 |
| `T7GLJ.DFM` |  | 0 | 1 | 0 |
| `T7GLJASK.DFM` | Change Location | 4 | 11 | 0 |
| `T7GLK.DFM` | GL- K | 13 | 42 | 0 |
| `T7GLL.DFM` |  | 0 | 1 | 0 |
| `T7GLN.DFM` | GL- N | 40 | 87 | 0 |
| `T7GLO.DFM` | GL-O | 117 | 160 | 0 |
| `T7GLOOB.DFM` | GL- O-OB | 5 | 27 | 0 |
| `T7GLP.DFM` | GL-P | 12 | 40 | 0 |
| `T7GLQ.DFM` |  | 0 | 1 | 0 |
| `T7GLS.DFM` |  | 0 | 1 | 0 |
| `T7GLT.DFM` | New Screen | 31 | 68 | 0 |

## Database tables (28)

Full field details are in `../../../samples/ddf/schema.md` (see per-table heading).

| Table | File on disk | Fields | Key fields (first 3) |
| ----- | ------------ | -----: | -------------------- |
| **BKGLACHK** | `BKGLACHK.B` | 11 | `BKGL_CHK_CHKACT`, `BKGL_CHK_NUM`, `BKGL_CHK_DATE` |
| **BKGLAGJL** | `BKGLAGJL.B` | 9 | `BKGL_GJL_TRANSN`, `BKGL_GJL_ACCTNM`, `BKGL_GJL_GLDPT` |
| **BKGLAGJR** | `BKGLAGJR.B` | 11 | `BKGL_GJ_TRANSDT`, `BKGL_GJ_TRANSNM`, `BKGL_GJ_TYPE` |
| **BKGLATRN** | `BKGLATRN.B` | 16 | `BKGL_TRN_GLACCT`, `BKGL_TRN_GLDPT`, `BKGL_TRN_DATE` |
| **BKGLCCOA** | `BKGLCCOA.B` | 62 | `BKGLC_ACCT`, `BKGLC_GLDPT`, `BKGLC_ACCTD` |
| **BKGLCHK** | `BKGLCHK.B` | 11 | `BKGL_CHK_CHKACT`, `BKGL_CHK_NUM`, `BKGL_CHK_DATE` |
| **BKGLCOA** | `BKGLCOA.B` | 65 | `BKGL_ACCT`, `BKGL_GLDPT`, `BKGL_ACCTD` |
| **BKGLDESC** | `BKGLDESC.B` | 5 | `BK_DESC_CODE`, `BK_DESC_NUM`, `BK_DESC_LINE` |
| **BKGLECOA** | `BKGLECOA.B` | 65 | `BKGL_ACCT`, `BKGL_GLDPT`, `BKGL_ACCTD` |
| **BKGLETRN** | `BKGLETRN.B` | 16 | `BKGL_TRN_GLACCT`, `BKGL_TRN_GLDPT`, `BKGL_TRN_DATE` |
| **BKGLFCOA** | `BKGLFCOA.B` | 65 | `BKGL_ACCT`, `BKGL_GLDPT`, `BKGL_ACCTD` |
| **BKGLFSTL** | `BKGLFSTL.B` | 12 | `BKFS_NAME`, `BKFS_LINE_NUM`, `BKFS_SGL_ACCT` |
| **BKGLGJLN** | `BKGLGJLN.B` | 9 | `BKGL_GJL_TRANSN`, `BKGL_GJL_ACCTNM`, `BKGL_GJL_GLDPT` |
| **BKGLGJRN** | `BKGLGJRN.B` | 11 | `BKGL_GJ_TRANSDT`, `BKGL_GJ_TRANSNM`, `BKGL_GJ_TYPE` |
| **BKGLHIST** | `BKGLHIST.B` | 16 | `BKGL_TRN_GLACCT`, `BKGL_TRN_GLDPT`, `BKGL_TRN_DATE` |
| **BKGLICC** | `BKGLICC.B` | 11 | `BKGL_CHK_CHKACT`, `BKGL_CHK_NUM`, `BKGL_CHK_DATE` |
| **BKGLRGJL** | `BKGLRGJL.B` | 9 | `BKGL_GJL_TRANSN`, `BKGL_GJL_ACCTNM`, `BKGL_GJL_GLDPT` |
| **BKGLRGJR** | `BKGLRGJR.B` | 11 | `BKGL_GJ_TRANSDT`, `BKGL_GJ_TRANSNM`, `BKGL_GJ_TYPE` |
| **BKGLSTMT** | `BKGLSTMT.B` | 104 | `BKGL_STB_MN_TTL`, `BKGL_STB_GLA_MT`, `BKGL_STB_GLA_F_1` |
| **BKGLTEMP** | `BKGLTEMP.B` | 16 | `BKGL_TRN_GLACCT`, `BKGL_TRN_GLDPT`, `BKGL_TRN_DATE` |
| **BKGLTGJL** | `BKGLTGJL.B` | 9 | `BKGL_GJL_TRANSN`, `BKGL_GJL_ACCTNM`, `BKGL_GJL_GLDPT` |
| **BKGLTGJR** | `BKGLTGJR.B` | 11 | `BKGL_GJ_TRANSDT`, `BKGL_GJ_TRANSNM`, `BKGL_GJ_TYPE` |
| **BKGLTMP** | `BKGLTMP.B` | 16 | `BKGL_TRN_GLACCT`, `BKGL_TRN_GLDPT`, `BKGL_TRN_DATE` |
| **BKGLTMP2** | `BKGLTMP2.B` | 16 | `BKGL_TRN_GLACCT`, `BKGL_TRN_GLDPT`, `BKGL_TRN_DATE` |
| **BKGLTMP3** | `BKGLTMP3.B` | 16 | `BKGL_TRN_GLACCT`, `BKGL_TRN_GLDPT`, `BKGL_TRN_DATE` |
| **BKGLTRAN** | `BKGLTRAN.B` | 16 | `BKGL_TRN_GLACCT`, `BKGL_TRN_GLDPT`, `BKGL_TRN_DATE` |
| **BKGLX** | `BKGLX.B` | 20 | `BKGLX_POSTDATE`, `BKGLX_ARCHDATE`, `BKGLX_ENTDATE` |
| **BKGLXH** | `BKGLXH.B` | 20 | `BKGLX_POSTDATE`, `BKGLX_ARCHDATE`, `BKGLX_ENTDATE` |

## Notes & open questions

- *(populated per-module manually as deeper reading happens.)*
