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

## BKAPVEND — Vendor Master (72 fields, confirmed from DDF, Pass 110e 2026-06-19)

Primary key: `BKAP_VENDCODE` (10)

| # | Field | Type | Size | Meaning |
|---|-------|------|------|---------|
| 1 | `BKAP_VENDCODE` | STRING | 10 | Vendor code (PK) |
| 2 | `BKAP_VENDNAME` | STRING | 30 | Vendor name |
| 3–4 | `BKAP_ADD1_1/2` | STRING | 30 | Address line 1 (billing / shipping) |
| 5–6 | `BKAP_ADD2_1/2` | STRING | 30 | Address line 2 (billing / shipping) |
| 7–8 | `BKAP_CITY_1/2` | STRING | 26 | City (billing / shipping) |
| 9 | `BKAP_STATE` | STRING | 2 | State |
| 10–13 | `BKAP_CONTACT_1..4` | STRING | 30 | Contacts 1–4 |
| 14–18 | `BKAP_TELEPHONE_1..5` | STRING | 25 | Phone numbers 1–5 |
| 19 | `BKAP_ZIP` | STRING | 10 | ZIP/postal code |
| 20–21 | `BKAP_COUNTRY_1/2` | STRING | 30 | Country (billing / shipping) |
| 22 | `BKAP_OUTINV` | FLOAT | 8 | Outstanding invoice balance ($) |
| 23 | `BKAP_LASTPURCH` | DATE | 4 | Date of last purchase |
| 24 | `BKAP_LASTPMT` | DATE | 4 | Date of last payment |
| 25 | `BKAP_PURCH_MTD` | FLOAT | 8 | Purchases month-to-date |
| 26 | `BKAP_PURCH_YTD` | FLOAT | 8 | Purchases year-to-date |
| 27 | `BKAP_PURCH_LYR` | FLOAT | 8 | Purchases last year |
| 28 | `BKAP_PURCH_VAR` | FLOAT | 8 | Purchase variance (YTD vs LYR) |
| 29 | `BKAP_OUT_CREDIT` | FLOAT | 8 | Outstanding credit memos ($) |
| 30 | `BKAP_NEW_VEND` | STRING | 1 | New vendor flag |
| 31 | `BKAP_START_DATE` | DATE | 4 | Account open date |
| 32 | `BKAP_CLASS` | STRING | 4 | Vendor class code |
| 33 | `BKAP_TERMS_NUM` | UBINARY | 2 | Payment terms code |
| 34 | `BKAP_HIST_YN` | STRING | 1 | Keep purchase history flag |
| 35 | `BKAP_REM_ZIP` | STRING | 10 | Remit-to ZIP |
| 36 | `BKAP_REM_STATE` | STRING | 2 | Remit-to state |
| 37–46 | `BKAP_NOTES_1..10` | STRING | 60 | Internal notes (10 × 60 char = 600 chars) |
| 47 | `BKAP_GL_ACCT` | STRING | 10 | GL AP control account |
| 48 | `BKAP_GL_DPT` | STRING | 4 | GL AP department |
| 49 | `BKAP_SORT` | STRING | 6 | Sort key |
| 50 | `BKAP_SHIP_VIA` | STRING | 15 | Default ship method |
| 51 | `BKAP_FOB_POINT` | STRING | 20 | FOB point |
| 52 | `BKAP_FTERMS_NUM` | UBINARY | 2 | Freight terms code |
| 53 | `BKAP_TAX_ID` | STRING | 20 | Tax ID / EIN (for 1099 reporting) |
| 54 | `BKAP_ADD3` | STRING | 30 | Address line 3 |
| 55 | `BKAP_EXTRA` | STRING | 150 | Extra/user-defined field (150 chars) |
| 56–60 | `BKAP_EMAIL_1..5` | STRING | 128 | Email addresses 1–5 |
| 61 | `BKAP_DESC` | STRING | 25 | Vendor description / category |
| 62 | `BKAP_IS_TAXGRP` | STRING | 10 | AvaTax / tax group code |
| 63 | `BKAP_IS_TAXIN` | STRING | 1 | Tax-inclusive pricing flag |
| 64 | `BKAP_IS_MCCODE` | STRING | 3 | Multi-currency code |
| 65 | `BKAP_IS_DCODE` | STRING | 3 | Discount code |
| 66 | `BKAP_CUST_CODE` | STRING | 15 | AR customer code if this vendor is also a customer |
| 67 | `BKAP_CREDLIM` | FLOAT | 8 | Credit limit with this vendor |
| 68 | `BKAP_REQQC` | STRING | 1 | Require QC inspection on receipts flag |
| 69–70 | `BKAP_ALPHA1/2` | STRING | 25 | Alpha search keys 1 + 2 |
| 71–72 | `BKAP_DATE1/2` | DATE | 4 | User-defined date fields 1 + 2 |

**Related table — BKAPVND2 (63 fields):** Contains 1099 reporting extensions (SEND_1099 flag, box amounts A1–A10 × 5 entries each with labels and dates). One record per vendor. FK: `BKAP2_VENDCODE`.

## Notes & open questions

- *(populated per-module manually as deeper reading happens.)*
