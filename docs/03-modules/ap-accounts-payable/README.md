# Accounts Payable (AP)

Status: verified (auto-generated from the extracted schema, menu-code dump, and DFM inventory).

- **Module code**: `AP`
- **Tables**: 26 (prefixes `BKAP`, `BKAB`)
- **UI forms**: 33 (prefixes `T7AP`, `T6AP`, `BKAP`)
- **Menu operations**: 19

## Menu operations

| Code | Operation | Legacy module file(s) |
| ---- | --------- | --------------------- |
| `AP-A` | Enter Vendors | BKAPA |
| `AP-B` | Enter Vouchers | BKAPB;T6APB |
| `AP-D` | Enter Scheduled Payment Dates | BKAPD |
| `AP-E` | Print Vouchers/Invoices Due by Date | BKAPE;t6ape |
| `AP-F` | Pick Vouchers/Invoices to Pay | BKAPF |
| `AP-G` | Print Pro Forma Check Register | BKAPG;ISTECH;t6apg |
| `AP-H` | Print Checks | BKAPHA;T6APHA |
| `AP-I` | Print Aging | BKAPI;T6API |
| `AP-J` | Print Vendor Code and Name | BKAPJ;t6apj |
| `AP-K` | Print Vendor General Info | BKAPK |
| `AP-L` | Print Vendor Purchase Info | BKAPL;t6apl |
| `AP-M` | Print Vendor Labels | BKAPM;t6apm |
| `AP-N` | Print Vendor Rolodex | BKAPN |
| `AP-O` | Enter Recurring Vouchers | BKAPO;ISAPO |
| `AP-P` | Generate Recurring Vouchers | BKAPP |
| `AP-Q` | Void AP Check | BKAPQ |
| `AP-R` | Print AP Payment History | BKAPR |
| `AP-S` | Print 1099 Forms | APS1999;APS2000;TAPS2000 |
| `AP-U` | Archive/Purge Vendor | ISAPU;ISAPV |

## UI forms (33)

| DFM file | Caption | fields | controls | tabs |
| -------- | ------- | -----: | -------: | ---: |
| `T7APA.DFM` | New Screen | 39 | 101 | 0 |
| `T7APABANK.DFM` | Vendor Bank Information | 16 | 36 | 0 |
| `T7APACON.DFM` |  Customer Contact Information | 13 | 20 | 0 |
| `T7APAPRC.DFM` |  Check Vendor Item Pricing | 5 | 12 | 0 |
| `T7APASTA.DFM` |  Vendor Statistics | 4 | 13 | 0 |
| `T7APB.DFM` |  | 0 | 1 | 0 |
| `T7APC.DFM` |  | 0 | 1 | 0 |
| `T7APD.DFM` |  | 0 | 1 | 0 |
| `T7APE.DFM` | New Screen | 15 | 42 | 0 |
| `T7APH.DFM` |  | 0 | 1 | 0 |
| `T7APHASK.DFM` | Check Note | 4 | 11 | 0 |
| `T7API.DFM` | New Screen | 23 | 63 | 0 |
| `T7APINFO.DFM` | New Screen | 63 | 84 | 0 |
| `T7APJ.DFM` | New Screen | 19 | 48 | 0 |
| `T7APK.DFM` | New Screen | 10 | 40 | 0 |
| `T7APM.DFM` | AP-M | 10 | 35 | 0 |
| `T7APO.DFM` | New Screen | 63 | 118 | 2 |
| `T7APP.DFM` | New Screen | 8 | 31 | 0 |
| `T7APQ.DFM` | New Screen | 10 | 43 | 0 |
| `T7APR.DFM` | New Screen | 15 | 41 | 0 |
| `T7APS.DFM` | New Screen | 11 | 39 | 0 |
| `T7APT.DFM` | AP check info | 30 | 85 | 0 |
| `T7APV.DFM` |  | 0 | 1 | 0 |
| `T7APX.DFM` | New Screen | 9 | 30 | 0 |
| `T7APY.DFM` | Vendor Amount | 12 | 39 | 0 |
| `T7APYB.DFM` | Pinacle | 15 | 48 | 0 |
| `T7APYC.DFM` | NACHA | 9 | 35 | 0 |
| `T7APZA.DFM` | New Screen | 13 | 44 | 0 |
| `t7apaC.DFM` | New Screen | 55 | 144 | 0 |
| `t7apae.DFM` | New Screen | 68 | 181 | 4 |
| `t7apf.dfm` |  | 0 | 1 | 0 |
| `t7apg.dfm` | AP-G Print Proforma Check Register | 6 | 28 | 0 |
| `t7apl.DFM` | New Screen | 7 | 29 | 0 |

## Database tables (26)

Full field details are in `../../../samples/ddf/schema.md` (see per-table heading).

| Table | File on disk | Fields | Key fields (first 3) |
| ----- | ------------ | -----: | -------------------- |
| **BKABCUST** | `BKABCUST.B` | 5 | `BKAB_START`, `BKAB_EXP`, `BKAB_PERIOD` |
| **BKABVEND** | `BKABVEND.B` | 2 | `BKAB_SERIAL`, `BKAB_REG_NAME` |
| **BKAPACCN** | `BKAPACCN.B` | 154 | `BKCM_ACCN_CODE`, `BKCM_ACCN_CONT_1`, `BKCM_ACCN_CONT_2` |
| **BKAPADSC** | `BKAPADSC.B` | 5 | `BK_DESC_CODE`, `BK_DESC_NUM`, `BK_DESC_LINE` |
| **BKAPAPO** | `BKAPAPO.B` | 58 | `BKAP_PO_NUM`, `AHSY_USER_ACCES_5`, `BKAP_PO_PRTD` |
| **BKAPAPOL** | `BKAPAPOL.B` | 38 | `BKAP_POL_PONM`, `BKAP_POL_CNTR`, `BKAP_POL_ERD` |
| **BKAPCHKF** | `BKAPCHKF.B` | 12 | `BKAP_CHK_VNDCOD`, `BKAP_CHK_INVNUM`, `BKAP_CHK_INVAMT` |
| **BKAPCHKH** | `BKAPCHKH.B` | 12 | `BKAP_CHK_VNDCOD`, `BKAP_CHK_INVNUM`, `BKAP_CHK_INVAMT` |
| **BKAPDEP** | `BKAPDEP.B` | 6 | `BKAR_DEP_DEPNO`, `BKAR_DEP_CUST`, `BKAR_DEP_DATE` |
| **BKAPDESC** | `BKAPDESC.B` | 5 | `BK_DESC_CODE`, `BK_DESC_NUM`, `BK_DESC_LINE` |
| **BKAPEIVT** | `BKAPEIVT.B` | 19 | `BKAP_INVT_CODE`, `BKAP_INVT_DATE`, `BKAP_INVT_NUM` |
| **BKAPEVND** | `BKAPEVND.B` | 73 | `BKAP_VENDCODE`, `Xf$Flags`, `BKAP_VENDNAME` |
| **BKAPHDSC** | `BKAPHDSC.B` | 5 | `BK_DESC_CODE`, `BK_DESC_NUM`, `BK_DESC_LINE` |
| **BKAPHPO** | `BKAPHPO.B` | 57 | `BKAP_PO_NUM`, `BKAP_PO_PRTD`, `BKAP_PO_VNDCOD` |
| **BKAPHPOL** | `BKAPHPOL.B` | 38 | `BKAP_POL_PONM`, `BKAP_POL_CNTR`, `BKAP_POL_ERD` |
| **BKAPINVL** | `BKAPINVL.B` | 390 | `BKAP_INVL_CODE`, `BKAP_INVL_NUM`, `BKAP_INVL_DATE` |
| **BKAPINVT** | `BKAPINVT.B` | 19 | `BKAP_INVT_CODE`, `BKAP_INVT_DATE`, `BKAP_INVT_NUM` |
| **BKAPNOTE** | `BKAPNOTE.B` | 12 | `BKAP_NOTE_SRCH1`, `BKAP_NOTE_SRCH2`, `BKAP_NOTE_DATE` |
| **BKAPPO** | `BKAPPO.B` | 57 | `BKAP_PO_NUM`, `BKAP_PO_PRTD`, `BKAP_PO_VNDCOD` |
| **BKAPPOL** | `BKAPPOL.B` | 38 | `BKAP_POL_PONM`, `BKAP_POL_CNTR`, `BKAP_POL_ERD` |
| **BKAPQUOT** | `BKAPQUOT.B` | 49 | `BKRFQ_NUM`, `BKRFQ_EST`, `BKRFQ_PARENT` |
| **BKAPRFQ** | `BKAPRFQ.B` | 57 | `BKAP_PO_NUM`, `BKAP_PO_PRTD`, `BKAP_PO_VNDCOD` |
| **BKAPRFQL** | `BKAPRFQL.B` | 38 | `BKAP_POL_PONM`, `BKAP_POL_CNTR`, `BKAP_POL_ERD` |
| **BKAPRIVL** | `BKAPRIVL.B` | 390 | `BKAP_INVL_CODE`, `BKAP_INVL_NUM`, `BKAP_INVL_DATE` |
| **BKAPVEND** | `BKAPVEND.B` | 72 | `BKAP_VENDCODE`, `BKAP_VENDNAME`, `BKAP_ADD1_1` |
| **BKAPVND2** | `BKAPVND2.B` | 63 | `BKAP2_VENDCODE`, `BKAP2_ID`, `BKAP2_SEND_1099` |

## Notes & open questions

- *(populated per-module manually as deeper reading happens.)*
