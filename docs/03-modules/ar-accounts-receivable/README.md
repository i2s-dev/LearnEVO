# Accounts Receivable (AR)

Status: verified (auto-generated from the extracted schema, menu-code dump, and DFM inventory).

- **Module code**: `AR`
- **Tables**: 29 (prefixes `BKAR`, `BKAB`, `BKART`)
- **UI forms**: 24 (prefixes `T7AR`, `T6AR`, `BKAR`)
- **Menu operations**: 17

## Menu operations

| Code | Operation | Legacy module file(s) |
| ---- | --------- | --------------------- |
| `AR-A` | Enter Customers | BKARA |
| `AR-B` | Enter Vouchers | BKARB;T6ARB |
| `AR-C` | Record Payments | BKARC;T6ARC |
| `AR-D` | Charge Interest on Invoices | BKARD |
| `AR-E` | Print Statements | BKARE;T6ARE |
| `AR-F` | Print Aging | BKARF;T6ARF |
| `AR-G` | Print Customer Code and Name | BKARG |
| `AR-H` | Print Customer General Info | BKARH |
| `AR-I` | Print Customer Mail Labels | BKARI;T6ARI |
| `AR-J` | Print Customer Rolodex | BKARJ;rolodex.run |
| `AR-K` | Print Sales Tax Report | BKARK |
| `AR-L` | Transfer Sales Taxes | BKARL |
| `AR-M` | Enter Customer Refund | BKARM |
| `AR-N` | Print Customer Deposits | BKARN;T6arn |
| `AR-P` | Generate Dun Letters | BKARP;T6ARP |
| `AR-Q` | View Customers | BKARA |
| `AR-S` | Accounts Receivable Defaults | BKADE |

## UI forms (24)

| DFM file | Caption | fields | controls | tabs |
| -------- | ------- | -----: | -------: | ---: |
| `T7ARA.DFM` | New Screen | 63 | 154 | 0 |
| `T7ARA2DB.DFM` | E&xit | 0 | 1 | 0 |
| `T7ARAC.DFM` | New Screen | 63 | 154 | 0 |
| `T7ARACON.DFM` |  Customer Contact Information | 16 | 23 | 0 |
| `T7ARACRE.DFM` |  Customer Credit Information | 11 | 26 | 0 |
| `T7ARAE.DFM` | New Screen | 118 | 279 | 7 |
| `T7ARAPRC.DFM` |  Check Customer Item Pricing | 6 | 14 | 0 |
| `T7ARASTA.DFM` |  Customer Statistics | 13 | 24 | 0 |
| `T7ARB.DFM` | Voucher Entry | 72 | 134 | 0 |
| `T7ARC.DFM` |  | 0 | 1 | 0 |
| `T7ARD.DFM` | AR-D  Charge Interest on Invoices | 7 | 27 | 0 |
| `T7ARE.DFM` | AR-E  Print Statements [Plain Paper] | 23 | 52 | 0 |
| `T7ARF.DFM` | AR-F  Print Aging | 42 | 98 | 0 |
| `T7ARG.DFM` | AR-G  Print Customer Code and Name" | 25 | 61 | 0 |
| `T7ARH.DFM` | AR-H  Print Customer General Info | 19 | 50 | 0 |
| `T7ARI.DFM` | AR-I  Print Customer Mail Labels | 28 | 66 | 0 |
| `T7ARK.DFM` | AR-K | 14 | 42 | 0 |
| `T7ARL.DFM` |  | 0 | 1 | 0 |
| `T7ARM.DFM` |  | 0 | 1 | 0 |
| `T7ARN.DFM` |  | 0 | 1 | 0 |
| `T7ARP.DFM` | BASE Blank T7 SCREEN | 12 | 40 | 0 |
| `T7ARR.DFM` | AR-R Print AR Payment History | 12 | 37 | 0 |
| `T7ART.DFM` | New Screen | 10 | 57 | 0 |
| `T7ARU.DFM` | New Screen | 5 | 24 | 0 |

## Database tables (29)

Full field details are in `../../../samples/ddf/schema.md` (see per-table heading).

| Table | File on disk | Fields | Key fields (first 3) |
| ----- | ------------ | -----: | -------------------- |
| **BKABCUST** | `BKABCUST.B` | 5 | `BKAB_START`, `BKAB_EXP`, `BKAB_PERIOD` |
| **BKABVEND** | `BKABVEND.B` | 2 | `BKAB_SERIAL`, `BKAB_REG_NAME` |
| **BKARCHKF** | `BKARCHKF.B` | 12 | `BKAP_CHK_VNDCOD`, `BKAP_CHK_INVNUM`, `BKAP_CHK_INVAMT` |
| **BKARCHKH** | `BKARCHKH.B` | 12 | `BKAP_CHK_VNDCOD`, `BKAP_CHK_INVNUM`, `BKAP_CHK_INVAMT` |
| **BKARCUST** | `BKARCUST.B` | 106 | `BKAR_CUSTCODE`, `BKAR_CUSTNAME`, `BKAR_ADD1` |
| **BKARDEP** | `BKARDEP.B` | 6 | `BKAR_DEP_DEPNO`, `BKAR_DEP_CUST`, `BKAR_DEP_DATE` |
| **BKARDESC** | `BKARDESC.B` | 5 | `BK_DESC_CODE`, `BK_DESC_NUM`, `BK_DESC_LINE` |
| **BKARDPST** | `BKARDPST.B` | 5 | `BK_DESC_CODE`, `BK_DESC_NUM`, `BK_DESC_LINE` |
| **BKARECST** | `BKARECST.B` | 106 | `BKAR_CUSTCODE`, `BKAR_CUSTNAME`, `BKAR_ADD1` |
| **BKAREIVT** | `BKAREIVT.B` | 24 | `BKAR_INVT_CODE`, `BKAR_INVT_DATE`, `BKAR_INVT_NUM` |
| **BKARHDSC** | `BKARHDSC.B` | 5 | `BK_DESC_CODE`, `BK_DESC_NUM`, `BK_DESC_LINE` |
| **BKARHINV** | `BKARHINV.B` | 84 | `BKAR_INV_NUM`, `BKAR_INV_SONUM`, `BKAR_INV_INVCD` |
| **BKARHIVL** | `BKARHIVL.B` | 28 | `BKAR_INVL_INVNM`, `BKAR_INVL_CNTR`, `BKAR_INVL_ESD` |
| **BKARHTAX** | `BKARHTAX.B` | 5 | `BKAR_TAX_INVNO`, `BKAR_TAX_CODE`, `BKAR_TAX_ID` |
| **BKARINV** | `BKARINV.B` | 84 | `BKAR_INV_NUM`, `BKAR_INV_SONUM`, `BKAR_INV_INVCD` |
| **BKARINVI** | `BKARINVI.B` | 16 | `BKAR_INVI_SONUM`, `BKAR_INVI_INVNM`, `BKAR_INVI_ESD` |
| **BKARINVL** | `BKARINVL.B` | 28 | `BKAR_INVL_INVNM`, `BKAR_INVL_CNTR`, `BKAR_INVL_ESD` |
| **BKARINVT** | `BKARINVT.B` | 23 | `BKAR_INVT_CODE`, `BKAR_INVT_DATE`, `BKAR_INVT_NUM` |
| **BKARINVV** | `BKARINVV.B` | 77 | `BKAR_INVV_CODE`, `BKAR_INVV_NUM`, `BKAR_INVV_DATE` |
| **BKARRDSC** | `BKARRDSC.B` | 5 | `BK_DESC_CODE`, `BK_DESC_NUM`, `BK_DESC_LINE` |
| **BKARRINV** | `BKARRINV.B` | 84 | `BKAR_INV_NUM`, `BKAR_INV_SONUM`, `BKAR_INV_INVCD` |
| **BKARRIVL** | `BKARRIVL.B` | 28 | `BKAR_INVL_INVNM`, `BKAR_INVL_CNTR`, `BKAR_INVL_ESD` |
| **BKARSHIP** | `BKARSHIP.B` | 106 | `BKAR_CUSTCODE`, `BKAR_CUSTNAME`, `BKAR_ADD1` |
| **BKARSIVL** | `BKARSIVL.B` | 28 | `BKAR_INVL_INVNM`, `BKAR_INVL_CNTR`, `BKAR_INVL_ESD` |
| **BKART** | `BKART.B` | 12 | `BKART_CUST`, `BKART_TRXN`, `BKART_TYPE` |
| **BKARTNOT** | `BKARTNOT.B` | 3 | `BKART_NOT_TRXN`, `BKART_NOT_CNTR`, `BKART_NOT_DESC` |
| **BKARTXN** | `BKARTXN.B` | 14 | `BKAR_TXN_SONUM`, `BKAR_TXN_CODE`, `BKAR_TXN_DESC` |
| **BKARTXNB** | `BKARTXNB.B` | 14 | `BKAR_TXN_SONUM`, `BKAR_TXN_CODE`, `BKAR_TXN_DESC` |
| **BKARTXNS** | `BKARTXNS.B` | 14 | `BKAR_TXN_SONUM`, `BKAR_TXN_CODE`, `BKAR_TXN_DESC` |

## Notes & open questions

- *(populated per-module manually as deeper reading happens.)*
