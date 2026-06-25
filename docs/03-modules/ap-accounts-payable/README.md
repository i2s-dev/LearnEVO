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

## BKAPPO — Purchase Order Header (57 fields, confirmed from DDF, Pass 110e 2026-06-19)

Primary key: `BKAP_PO_NUM` (FLOAT 8)

**PO table family:** BKAPPO (active) / BKAPHPO (history, same schema) / BKAPAPO (archive, 58f) / BKAPRFQ (Request for Quote, same 57f schema). Line-level: BKAPPOL (active) / BKAPHPOL (history) / BKAPAPOL (archive) / BKAPRFQL (RFQ lines).

| # | Field | Type | Size | Meaning |
|---|-------|------|------|---------|
| 1 | `BKAP_PO_NUM` | FLOAT | 8 | PO number (PK — numeric sequence stored as float) |
| 2 | `BKAP_PO_PRTD` | STRING | 1 | Printed flag (indexed for report queries) |
| 3 | `BKAP_PO_VNDCOD` | STRING | 10 | Vendor code (FK → BKAPVEND) |
| 4 | `BKAP_PO_VNDNME` | STRING | 30 | Vendor name (denormalized) |
| 5–7 | `BKAP_PO_VNDA1/2/3` | STRING | 30 | Vendor address lines 1–3 |
| 8 | `BKAP_PO_VNDCTY` | STRING | 26 | Vendor city |
| 9 | `BKAP_PO_VNDST` | STRING | 2 | Vendor state |
| 10 | `BKAP_PO_VNDZIP` | STRING | 10 | Vendor ZIP |
| 11 | `BKAP_PO_SHPCOD` | STRING | 10 | Ship-to location code |
| 12 | `BKAP_PO_SHPNME` | STRING | 30 | Ship-to name |
| 13–15 | `BKAP_PO_SHPA1/2/3` | STRING | 30 | Ship-to address lines 1–3 |
| 16 | `BKAP_PO_SHPCTY` | STRING | 26 | Ship-to city |
| 17 | `BKAP_PO_SHPST` | STRING | 2 | Ship-to state |
| 18 | `BKAP_PO_SHPZIP` | STRING | 10 | Ship-to ZIP |
| 19 | `BKAP_PO_SHPVIA` | STRING | 15 | Ship via method |
| 20 | `BKAP_PO_TERMD` | STRING | 10 | Payment terms description |
| 21 | `BKAP_PO_TERMNM` | UBINARY | 2 | Payment terms code (FK → terms table) |
| 22 | `BKAP_PO_ENTBY` | STRING | 2 | Entered by (user code) |
| 23 | `BKAP_PO_OBYCUS` | STRING | 15 | Ordered by customer ref (customer PO#) |
| 24 | `BKAP_PO_TAXABLE` | STRING | 1 | Taxable flag |
| 25–26 | `BKAP_PO_CONFIRM_1/2` | STRING | 1 | Confirmation flags 1–2 |
| 27 | `BKAP_PO_ORDDTE` | DATE | 4 | Order date |
| 28 | `BKAP_PO_SUBTOT` | FLOAT | 8 | Subtotal (before tax) |
| 29 | `BKAP_PO_TAXAMT` | FLOAT | 8 | Tax amount |
| 30 | `BKAP_PO_TOTAL` | FLOAT | 8 | PO total |
| 31 | `BKAP_PO_NL` | UBINARY | 2 | Number of lines |
| 32 | `BKAP_PO_TAXRTE` | FLOAT | 8 | Tax rate (%) |
| 33 | `BKAP_PO_DESC` | STRING | 30 | PO description / note |
| 34 | `BKAP_PO_GLDPT` | STRING | 4 | GL department |
| 35 | `BKAP_PO_LOC` | STRING | 10 | Receiving location code |
| 36 | `BKAP_PO_ITOTAL` | FLOAT | 8 | Invoiced total to date |
| 37 | `BKAP_PO_ENDLNE` | STRING | 1 | End-of-lines flag |
| 38 | `BKAP_PO_FOB` | STRING | 20 | FOB point |
| 39 | `BKAP_PO_FTERMNM` | UBINARY | 2 | Freight terms code |
| 40 | `BKAP_PO_FTERMD` | STRING | 10 | Freight terms description |
| 41 | `BKAP_PO_QCTOTAL` | FLOAT | 8 | QC-passed quantity total |
| 42–43 | `BKAP_PO_VNDCNT/VNDATN` | STRING | 30 | Vendor contact name / attention |
| 44–45 | `BKAP_PO_SHPCNT/SHPATN` | STRING | 30 | Ship-to contact / attention |
| 46 | `BKAP_PO_RECNUM` | FLOAT | 8 | Record number (internal sequence) |
| 47 | `BKAP_PO_LONGPO` | STRING | 25 | Long PO number (customer-side PO reference) |
| 48 | `BKAP_PO_EXTRA` | STRING | 150 | User-defined extra field |
| 49 | `BKAP_PO_INVNUM` | STRING | 10 | AP invoice number (linked after receipt) |
| 50 | `BKAP_PO_ISTXGR` | STRING | 10 | AvaTax group code |
| 51 | `BKAP_PO_ISMCDT` | DATE | 4 | Multi-currency date |
| 52 | `BKAP_PO_ISBROKE` | STRING | 10 | Broker/agent code |
| 53 | `BKAP_PO_ISREV` | STRING | 1 | Revision flag |
| 54 | `BKAP_PO_ISRVDT` | DATE | 4 | Revision date |
| 55 | `BKAP_PO_ISCUR` | STRING | 3 | Currency code (multi-currency) |
| 56 | `BKAP_PO_PCKSLP` | STRING | 15 | Packing slip number |
| 57 | `BKAP_PO_EMPNUM` | UBINARY | 2 | Employee number (buyer) |

## BKAPPOL — Purchase Order Lines (38 fields, confirmed from DDF, Pass 110e 2026-06-19)

Primary key: `BKAP_POL_PONM` (FLOAT 8) + `BKAP_POL_CNTR` (UBINARY 2)

| # | Field | Type | Size | Meaning |
|---|-------|------|------|---------|
| 1 | `BKAP_POL_PONM` | FLOAT | 8 | PO number (FK → BKAPPO.BKAP_PO_NUM) |
| 2 | `BKAP_POL_CNTR` | UBINARY | 2 | Line counter (PK part 2) |
| 3 | `BKAP_POL_ERD` | DATE | 4 | Expected receipt date (indexed) |
| 4 | `BKAP_POL_PCODE` | STRING | 15 | Part/item code (FK → inventory) |
| 5 | `BKAP_POL_PDESC` | STRING | 30 | Part description (denormalized) |
| 6 | `BKAP_POL_PQTY` | FLOAT | 8 | Ordered quantity |
| 7 | `BKAP_POL_PPRCE` | FLOAT | 8 | Unit price |
| 8 | `BKAP_POL_PDISC` | FLOAT | 8 | Discount % |
| 9 | `BKAP_POL_PEXT` | FLOAT | 8 | Extended amount (qty × price × (1−disc)) |
| 10 | `BKAP_POL_PCOGS` | FLOAT | 8 | COGS amount |
| 11 | `BKAP_POL_ITYPE` | STRING | 1 | Item type code |
| 12 | `BKAP_POL_GLA` | STRING | 10 | GL account override for this line |
| 13 | `BKAP_POL_GLDPTA` | STRING | 4 | GL department override |
| 14 | `BKAP_POL_TXBLE` | STRING | 1 | Line taxable flag |
| 15 | `BKAP_POL_RQTY` | FLOAT | 8 | Received quantity to date |
| 16 | `BKAP_POL_IQTY` | FLOAT | 8 | Invoiced quantity to date |
| 17 | `BKAP_POL_LOC` | STRING | 10 | Receiving location |
| 18–19 | `NKAP_POL_UM_LIN_1/2` | STRING | 3 | Unit of measure (purchase / stocking) |
| 20 | `BKAP_POL_OPER` | UBINARY | 2 | WO operation number (for outside process lines) |
| 21 | `BKAP_POL_WOPRE` | FLOAT | 8 | WO number (FK → WORKORD — outside process link) |
| 22 | `BKAP_POL_WOSUF` | UBINARY | 2 | WO suffix |
| 23 | `BKAP_POL_ARD` | DATE | 4 | Actual receipt date |
| 24 | `BKAP_POL_EST` | FLOAT | 8 | Estimate number (FK → Estimating) |
| 25 | `BKAP_POL_OO_QTY` | FLOAT | 8 | On-order quantity remaining |
| 26 | `BKAP_POL_ITM_NO` | STRING | 9 | Vendor's item number |
| 27 | `BKAP_POL_QC_QTY` | FLOAT | 8 | QC-passed quantity |
| 28 | `BKAP_POL_BUYOFF` | FLOAT | 8 | Buyer-approved quantity |
| 29 | `BKAP_POL_SCRAP` | FLOAT | 8 | Scrapped quantity |
| 30 | `BKAP_POL_PRTDIM` | STRING | 1 | Printed dimension flag |
| 31 | `BKAP_POL_PARENT` | STRING | 15 | Parent assembly part code (for component PO lines) |
| 32 | `BKAP_POL_RECNUM` | FLOAT | 8 | Record number (internal) |
| 33 | `BKAP_POL_EXTRA` | STRING | 100 | User-defined extra field |
| 34 | `BKAP_POL_INVNUM` | STRING | 10 | Voucher/invoice number |
| 35 | `BKAP_POL_PCONV` | FLOAT | 8 | Purchase-to-stock unit conversion factor |
| 36 | `BKAP_POL_INVDTE` | DATE | 4 | Invoice date |
| 37 | `BKAP_POL_PSTDTE` | DATE | 4 | Post date |
| 38 | `BKAP_POL_PKSQTY` | FLOAT | 8 | Packing slip quantity |

**Design notes:**
- BKAP_POL_WOPRE/WOSUF links a PO line to a WO routing operation — this is how outside processing is tracked: a WO operation of type O triggers a PO line; when the PO is received, the operation is marked complete.
- BKAP_POL_PCONV allows purchasing in different units than stocking (e.g., buy by the roll, stock by the foot).
- BKAP_POL_RQTY vs BKAP_POL_IQTY vs BKAP_POL_OO_QTY tracks the three-way split: received (in warehouse) / invoiced (AP voucher matched) / still on order.

## BKAPINVT — AP Open-Item Ledger (19 fields, confirmed from DDF schema.md, Pass 111c 2026-06-19)

Primary key: `BKAP_INVT_CODE` (vendor code) + `BKAP_INVT_DATE` (invoice date) + `BKAP_INVT_NUM` (invoice number)

Mirrors BKARINVT in AR — one row per open (unpaid) AP voucher. Rows are removed when the voucher is fully paid.

| Field | Type | Size | Meaning |
|-------|------|------|---------|
| `BKAP_INVT_CODE` | STRING | 10 | Vendor code (PK 1 — FK → BKAPVEND) |
| `BKAP_INVT_DATE` | DATE | 4 | Invoice date (PK 2) |
| `BKAP_INVT_NUM` | STRING | 10 | Invoice/voucher number (PK 3) |
| `BKAP_INVT_AMT` | FLOAT | 8 | Original invoice amount |
| `BKAP_INVT_AMTRM` | FLOAT | 8 | Amount remaining (unpaid balance; 0 = fully paid) |
| `BKAP_INVT_TYPE` | STRING | 1 | Transaction type: I=Invoice, C=Credit memo, D=Debit memo, P=Payment |
| `BKAP_INVT_TERMN` | UBINARY | 2 | Payment terms code (FK → terms table) |
| `BKAP_INVT_SDATE` | DATE | 4 | Scheduled payment date (set by AP-D) |
| `BKAP_INVT_TAX` | FLOAT | 8 | Tax amount on this voucher |
| `BKAP_INVT_FRT` | FLOAT | 8 | Freight amount on this voucher |
| `BKAP_INVT_DEPNO` | FLOAT | 8 | Deposit number (if pre-payment) |
| `BKAP_INVT_CHKNO` | FLOAT | 8 | Check number that paid this voucher |
| `BKAP_INVT_CHKAC` | UBINARY | 2 | Check/bank account used for payment |

**Notes:**
- BKAPEIVT (also 19f, same schema) is the archive counterpart — paid/closed vouchers move here.
- AMTRM > 0 = outstanding; AMTRM = 0 = paid. Aging is computed at runtime: due date = INVT_DATE + terms, bucket by days past due.
- SDATE is the AP-D "scheduled payment date" — the user can set this manually or via pick list (AP-F); AP-H uses it to select which vouchers to pay.

---

## BKAPINVL — AP Voucher GL Distribution (390 fields, confirmed from DDF schema.md, Pass 111c 2026-06-19)

Primary key: `BKAP_INVL_CODE` (vendor) + `BKAP_INVL_NUM` (invoice#) + `BKAP_INVL_DATE` (invoice date)

One row per AP voucher. Stores the voucher header **and** up to **75 GL distribution lines** as flat parallel arrays. This is the denormalized design that avoids a child table for GL coding.

**Record structure:** 390 fields, ~3,738 bytes per row.

### Header fields (10)

| Field | Type | Meaning |
|-------|------|---------|
| `BKAP_INVL_CODE` | STRING 10 | Vendor code (PK 1) |
| `BKAP_INVL_NUM` | STRING 10 | Invoice/voucher number (PK 2) |
| `BKAP_INVL_DATE` | DATE | Invoice date (PK 3) |
| `BKAP_INVL_DESC` | STRING 25 | Voucher description |
| `BKAP_INVL_TERMD` | STRING 10 | Payment terms description |
| `BKAP_INVL_TERMN` | UBINARY 2 | Payment terms code |
| `BKAP_INVL_TYPED` | STRING 10 | Transaction type description |
| `BKAP_INVL_TYPEN` | UBINARY 2 | Transaction type code |
| `BKAP_INVL_TAMT` | FLOAT | Total invoice amount |
| `BKAP_INVL_TDC` | STRING 1 | Overall debit/credit flag |

### GL distribution arrays (75 lines × 5 fields = 375 fields)

For each distribution line N (N = 1..75):

| Array | Type | Meaning |
|-------|------|---------|
| `BKAP_INVL_GLACT_N` | STRING 10 | GL account code for line N |
| `BKAP_INVL_GLDPT_N` | STRING 4 | GL department for line N |
| `BKAP_INVL_DC_N` | STRING 1 | Debit (D) or Credit (C) for line N |
| `BKAP_INVL_GLD_N` | STRING 25 | Description for line N |
| `BKAP_INVL_DAMT_N` | FLOAT | Dollar amount for line N |

Arrays are stored non-interleaved: all 75 GLACT values contiguous, then all 75 GLDPT values, then DC, GLD, DAMT.

### Trailer fields (5)

| Field | Type | Meaning |
|-------|------|---------|
| `BKAP_INVL_APDPT` | STRING 4 | AP department (GL offset for AP control account) |
| `BKAP_INVL_CHK` | UBINARY 2 | Check/bank account number |
| `BKAP_INVL_EXTRA` | STRING 50 | User-defined extra |
| `BKAP_INVL_ISCUR` | STRING 3 | Currency code (multi-currency) |
| `BKAP_INVL_JOB` | STRING 15 | Job cost number (FK → JC module) |

**BKAPRIVL** (390f, identical schema) is the recurring-voucher line table — recurring voucher templates (BKAPO headers) store their GL distribution in BKAPRIVL using the same layout.

---

## AP voucher entry workflow (AP-B)

```
AP-B: Enter Vouchers
  → Entry: vendor code, invoice#, date, amount, description, terms
  → GL distribution: up to 75 lines (account + dept + D/C + description + amount)
  → Write BKAPINVL row (voucher + full GL coding)
  → Write BKAPINVT row (open-item; AMTRM = full amount)
  → Update BKAPVEND.OUTINV += invoice amount

AP-D: Enter Scheduled Payment Dates
  → Set BKAPINVT.SDATE for one or many vouchers

AP-F: Pick Vouchers to Pay
  → Mark selected BKAPINVT rows (SDATE set / payment flag)

AP-G: Print Pro Forma Check Register
  → Preview of checks to be written (no data change)

AP-H: Print Checks
  → For each picked voucher:
    → Print check against BKAPINVT rows
    → Write BKAPCHKH row (check history)
    → Update BKAPINVT.AMTRM -= payment amount
    → When AMTRM = 0: remove from BKAPINVT → BKAPEIVT (archive)
    → Post GL: Debit BKAPINVL.GLACT_N lines, Credit AP control account
    → Write BKGLTRAN rows (one per GL line)
    → Update BKGLCOA period balances
    → Update BKAPVEND.OUTINV -= payment amount
```

---

## Programs (28 total) — Pass 266 (2026-06-25)

Source: `samples/rwn_symbols.json` — all T7AP* entries.

### Group 1 — Voucher entry

| Program | Procs | Lib | Role / key tables |
|---------|------:|-----|-------------------|
| `T7APB.RWN` | 301 | EVO.LIB | **AP-B** voucher entry (primary); BKAPINVL+BKAPINVT+BKAPVEND+BKYSMSTR; BKAR.INV 86-var |
| `t7apv.RWN` | 168 | ISTECH.LIB | **AP-V** AR deposit payment; BKARDEP+BKAPINVT+BKAPVEND+BKAPPO; MTWO.WIP 71-var — pays customer deposits via AP |

### Group 2 — PO receipt / QC

| Program | Procs | Lib | Role / key tables |
|---------|------:|-----|-------------------|
| `T7APC.RWN` | 285 | ISTECH.LIB | **AP-C** PO receipt with QC integration; BKAPVEND+BKQCMSTR+BKAPPOL+BKAPPO; **BKAP.POL 76-var** (PO line accessor) |

### Group 3 — Vendor master

| Program | Procs | Lib | Role / key tables |
|---------|------:|-----|-------------------|
| `T7APA.RWN` | 216 | LISTG60.LIB | **AP-A** vendor master editor; BKAPVEND+BKAPVND2+ISTAXGRP+ISEXUSER; BKAP.PO 57-var |
| `T7APK.RWN` | 110 | LISTG60.LIB | **AP-K** vendor alternate address/info; BKAPVEND+BKAPVND2+CLASMSTR; BKIC.PROD 63-var |

### Group 4 — Check printing

| Program | Procs | Lib | Role / key tables |
|---------|------:|-----|-------------------|
| `T7APH.RWN` | 216 | ISTECH.LIB | **AP-H** check printing; BKAPCHKF+ISBANKS+ISMCF; **ISIS.MCF 49-var** (multi-currency factor) |

### Group 5 — Voucher inquiry / aging

| Program | Procs | Lib | Role / key tables |
|---------|------:|-----|-------------------|
| `T7API.RWN` | 191 | LISTG60.LIB | **AP-I** invoice inquiry; BKAPINVT+BKAPVEND; ISIS.MCF 49-var |
| `T7APE.RWN` | 148 | LISTG60.LIB | **AP-E** AP aging; BKAPINVT+ISMCF+BKAPVEND; ISIS.MCF 49-var |
| `T7APQ.RWN` | 145 | ISTECH.LIB | **AP-Q** quick voucher select; BKAPVEND+BKAPCHKF; ISIS.MCF 49-var |
| `T7APG.RWN` | 139 | LISTG60.LIB | **AP-G** AP aging report; BKAPCHKF+BKAPVEND; ISIS.MCF 49-var |
| `T7APP.RWN` | 109 | LISTG60.LIB | **AP-P** print AP report; BKAPINVL+BKAPVEND; ISIS.MCF 49-var |
| `T7APF.RWN` | 157 | LISTG60.LIB | **AP-F** print voucher/check history; BKAPVEND+BKAPCHKF+BKAPINVT; EMAIL.CFG 34-var |
| `T7APT.RWN` | 129 | EVO.LIB | **AP-T** AP transaction report; BKAPVEND+BKAPCHKF+BKAPINVT+BKAPPO; BKAR.INV 86-var |
| `T7APR.RWN` | 128 | LISTG60.LIB | **AP-R** AP recap/check register; ISBANKS+ISBUILD+BKAPCHKF; EMAIL.CFG 34-var |
| `T7APX.RWN` | 112 | LISTG60.LIB | **AP-X** AP cross-reference utility; BKAPINVT+ISLINKS+BKAPPOL+BKAPPO; BKAP.PO 57-var |

### Group 6 — Bank reconciliation

| Program | Procs | Lib | Role / key tables |
|---------|------:|-----|-------------------|
| `T7APY.RWN` | 147 | LISTG60.LIB | **AP-Y** AP bank reconciliation; ISBANKS+BKGLCHK; EMAIL.CFG 34-var |
| `T7APYB.RWN` | 123 | LISTG60.LIB | **AP-YB** payroll bank interface; ISBANKS+BKPRCURP+BKPRMSTR; **BKPR.EMP 107-var** — links AP bank to payroll current period |
| `T7APYC.RWN` | 123 | LISTG60.LIB | **AP-YC** bank reconcile + vendor; ISBANKS+BKGLCHK+BKAPVEND; EMAIL.CFG 34-var |

### Group 7 — Utilities / admin

| Program | Procs | Lib | Role / key tables |
|---------|------:|-----|-------------------|
| `T7APJ.RWN` | 126 | LISTG60.LIB | **AP-J** AP extended vendor data; BKAPVEND+ISAPEX+help tables; EMAIL.CFG 34-var |
| `T7APZA.RWN` | 125 | LISTG60.LIB | **AP-ZA** AP error/CM tracking; CLASMSTR+BKCMTERR+ISBUILD; EMAIL.CFG 34-var |

### ISIS.MCF namespace — confirmed multi-currency

`ISIS.MCF 49-var` appears in T7APH, T7API, T7APE, T7APQ, T7APG, T7APP, T7GLB, T7GLO, T7GLQ, T7GLK. Consistent with being the **Multi-Currency Framework** exchange rate table — check printing, inquiry, and GL posting all need current exchange rates.

### New tables discovered in AP programs

| Table | Appears In | Inferred Role |
|-------|-----------|---------------|
| `BKAPVND2` | T7APA, T7APK | Vendor secondary record — alternate address / 2nd contact |
| `ISAPEX` | T7APJ | AP extended vendor fields — portal credentials or tax data |
| `ISEXUSER` | T7APA | External user account — vendor portal login credentials |
| `BKCMTERR` | T7APZA | CM/error tracking table (credit memo or posting error codes) |
| `ISLINKS` | T7APX | Cross-reference links (AP voucher ↔ PO line linkage) |
| `BKARDEP` | t7apv | AR deposit table — customer deposit payments via AP flow |
| `BKPRCURP` | T7APYB | Payroll current period — AP-YB bridges bank to payroll |
| `ISMCF` | T7APH, T7GLK | Multi-Currency Framework (exchange rate master) — same as ISIS.MCF |

---

## Notes & open questions

- BKAPAPO (58f) has one extra field vs BKAPPO (57f) — field not identified; likely an archive timestamp or purge flag.
- BKAPRFQ / BKAPRFQL: Request for Quote tables use same schema as BKAPPO/BKAPPOL — RFQs and POs share structure, distinguished by document type routing in the program.
- BKAPCHKF vs BKAPCHKH: Both are 12f check tables (VNDCOD + INVNUM + INVAMT PK). CHK**F** is likely "check file" (current) and CHK**H** is history; or F = front-end staging, H = history. Purpose distinction not confirmed.
- BKAPNOTE (12f): AP note table — SRCH1/SRCH2/DATE PK suggests a searchable note log linked to vendors or vouchers; exact use not yet traced.
