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

## BKARCUST — Customer Master (106 fields, confirmed from DDF, Pass 110e 2026-06-19)

Primary key: `BKAR_CUSTCODE` (10)

| # | Field | Type | Size | Meaning |
|---|-------|------|------|---------|
| 1 | `BKAR_CUSTCODE` | STRING | 10 | Customer code (PK) |
| 2 | `BKAR_CUSTNAME` | STRING | 30 | Customer name |
| 3 | `BKAR_ADD1` | STRING | 30 | Address line 1 |
| 4 | `BKAR_ADD2_1` | STRING | 30 | Address line 2 (billing) |
| 5 | `BKAR_ADD2_2` | STRING | 30 | Address line 2 (shipping) |
| 6 | `BKAR_CITY` | STRING | 26 | City |
| 7 | `BKAR_STATE` | STRING | 2 | State code |
| 8 | `BKAR_ZIP` | STRING | 10 | ZIP/postal code |
| 9–13 | `BKAR_CONTACT_1..5` | STRING | 30 | Contacts 1–5 |
| 14–18 | `BKAR_TELEPHONE_1..5` | STRING | 25 | Phone numbers 1–5 |
| 19 | `BKAR_COUNTRY` | STRING | 30 | Country |
| 20 | `BKAR_CREDITLMT` | FLOAT | 8 | Credit limit ($) |
| 21 | `BKAR_CHG_INTRST` | STRING | 1 | Charge interest flag (Y/N) |
| 22 | `BKAR_REMAINCRD` | FLOAT | 8 | Remaining credit available ($) |
| 23 | `BKAR_OUTINV` | FLOAT | 8 | Outstanding invoice balance ($) |
| 24 | `BKAR_LASTSALE` | DATE | 4 | Date of last sale |
| 25 | `BKAR_LASTPMT` | DATE | 4 | Date of last payment |
| 26 | `BKAR_GROSS_MTD` | FLOAT | 8 | Gross sales month-to-date |
| 27 | `BKAR_COGS_MTD` | FLOAT | 8 | Cost of goods sold MTD |
| 28 | `BKAR_NET_MTD` | FLOAT | 8 | Net sales MTD |
| 29 | `BKAR_PNET_MTD` | FLOAT | 8 | Prior-period net MTD |
| 30–33 | `BKAR_GROSS/COGS/NET/PNET_YTD` | FLOAT | 8 | Year-to-date equivalents |
| 34–37 | `BKAR_GROSS/COGS/NET/PNET_LYR` | FLOAT | 8 | Last-year equivalents |
| 38–41 | `BKAR_GROSS/COGS/NET/PNET_PVAR` | FLOAT | 8 | Prior-year variance |
| 42 | `BKAR_NEW_CUST` | STRING | 1 | New customer flag |
| 43–44 | `BKAR_OUT_CREDIT_1/2` | FLOAT | 8 | Outstanding credit memos (2 buckets) |
| 45 | `BKAR_TAX_STATE` | STRING | 2 | State tax code |
| 46 | `BKAR_TAX_LOCAL` | STRING | 2 | Local tax code |
| 47 | `BKAR_TAX_YN` | STRING | 1 | Taxable flag (Y/N) |
| 48 | `BKAR_STATEMENT` | STRING | 1 | Send statements flag |
| 49–50 | `BKAR_SLSP_NUM_1/2` | UBINARY | 2 | Salesperson 1 + 2 codes |
| 51 | `BKAR_TERMS_NUM` | UBINARY | 2 | Payment terms code (FK → terms table) |
| 52 | `BKAR_START_DATE` | DATE | 4 | Account open date |
| 53 | `BKAR_CLASS` | STRING | 4 | Customer class code |
| 54 | `BKAR_PRICE_MAT` | UBINARY | 2 | Price matrix code |
| 55 | `BKAR_HIST_YN` | STRING | 1 | Keep history flag |
| 56 | `BKAR_DISC_CODE` | STRING | 10 | Discount code |
| 57 | `BKAR_NUM_INVCS` | FLOAT | 8 | Total number of invoices |
| 58 | `BKAR_DAYS_TOPAY` | FLOAT | 8 | Average days to pay |
| 59–68 | `BKAR_NOTES_1..10` | STRING | 80 | Internal notes (10 × 80 char = 800 chars) |
| 69 | `BKAR_GLACCT` | STRING | 10 | GL sales account |
| 70 | `BKAR_GLDPT` | STRING | 4 | GL sales department |
| 71 | `BKAR_FOB` | STRING | 15 | FOB point |
| 72 | `BKAR_SHIPTO` | STRING | 10 | Default ship-to code |
| 73 | `BKAR_SHIPVIA` | STRING | 15 | Default ship method |
| 74 | `BKAR_FOLUPDTE` | DATE | 4 | Follow-up date (CRM) |
| 75–76 | `BKAR_COMM_1/2` | FLOAT | 8 | Commission rates for salesperson 1 + 2 |
| 77 | `BKAR_SORT` | STRING | 6 | Sort key |
| 78 | `BKAR_COOP_RATE` | FLOAT | 8 | Co-op advertising rate |
| 79 | `BKAR_COOP_AMT` | FLOAT | 8 | Co-op advertising accrual amount |
| 80 | `BKAR_TERRITORY` | STRING | 4 | Sales territory code |
| 81 | `BKAR_LEAD_SRC` | STRING | 5 | Lead source code |
| 82 | `BKAR_SIC_CODE` | STRING | 7 | SIC (Standard Industry Classification) code |
| 83 | `BKAR_PURCH_AGMT` | STRING | 1 | Purchase agreement flag |
| 84 | `BKAR_FORECAST` | STRING | 12 | Forecast amount (text — 12 chars) |
| 85 | `BKAR_CUST_YEAR` | STRING | 12 | Customer fiscal year info |
| 86 | `BKAR_QC_INFO` | STRING | 30 | Quality control info / cert requirements note |
| 87 | `BKAR_MAIL_LIST` | STRING | 1 | Mail list flag |
| 88 | `BKAR_CARRIER` | STRING | 15 | Preferred carrier |
| 89 | `BKAR_REQD_CERTS` | STRING | 10 | Required certifications code |
| 90 | `BKAR_SHP_WINDOW` | STRING | 30 | Ship window (delivery window text) |
| 91 | `BKAR_RECV_HOURS` | STRING | 30 | Receiving hours |
| 92 | `BKAR_SHP_TOLRNC` | STRING | 10 | Shipment quantity tolerance |
| 93 | `BKAR_RESALE_NO` | STRING | 15 | Resale tax exemption number |
| 94 | `BKAR_FAX_PHONE` | STRING | 25 | Fax number |
| 95 | `BKAR_CREDIT_HLD` | STRING | 1 | Credit hold flag (Y/N) |
| 96 | `BKAR_EXTRA` | STRING | 30 | Extra/user-defined field |
| 97–101 | `BKAR_EMAIL_1..5` | STRING | 128 | Email addresses 1–5 |
| 102 | `BKAR_IS_TAXGRP` | STRING | 10 | AvaTax / tax group code |
| 103 | `BKAR_IS_TAXIN` | STRING | 1 | Tax-inclusive pricing flag |
| 104 | `BKAR_IS_MCCODE` | STRING | 3 | Multi-currency code |
| 105 | `BKAR_IS_REP` | STRING | 5 | IS representative code |
| 106 | `BKAR_LEAD_SRC2` | STRING | 5 | Secondary lead source code |

**Note:** BKARSHIP (106f) has the same field layout as BKARCUST — it is the ship-to address override table (customer's alternate shipping addresses reuse the customer master layout).

## BKARINVT — AR Invoice Transaction / Open-Item Ledger (23 fields, Pass 111a 2026-06-19)

Primary key: `BKAR_INVT_CODE` (customer) + `BKAR_INVT_DATE` (invoice date) + `BKAR_INVT_NUM` (invoice number)

This is the **open-item AR ledger** — the live record of what each customer owes. One row per posted invoice (or credit memo). The row remains active until the invoice is fully paid (BKAR_INVT_CLOSD is set). BKAREIVT is the same table with a DDF index artifact (BKAB_PERIOD at an overlapping offset) that does not represent a real data field.

| Field | Type | Meaning |
|-------|------|---------|
| `BKAR_INVT_CODE` | STRING 10 | Customer code (PK 1) |
| `BKAR_INVT_DATE` | DATE | Invoice date (PK 2) |
| `BKAR_INVT_NUM` | FLOAT | Invoice number (PK 3) |
| `BKAR_INVT_AMT` | FLOAT | Original invoice amount (positive = invoice, negative = credit) |
| `BKAR_INVT_AMTRM` | FLOAT | Amount remaining unpaid (0 = fully paid) |
| `BKAR_INVT_DESC` | STRING 25 | Invoice description |
| `BKAR_INVT_TERMN` | UBINARY | Payment terms code (FK → payment terms table) |
| `BKAR_INVT_TYPE` | STRING 1 | Transaction type: I=invoice, C=credit memo, D=debit adj, P=payment |
| `BKAR_INVT_GLDPT` | STRING 4 | GL department |
| `BKAR_INVT_SLSP` | UBINARY | Salesperson 1 code |
| `BKAR_INVT_DEPST` | STRING 1 | Deposit posted flag |
| `BKAR_INVT_SLSP2` | UBINARY | Salesperson 2 code |
| `BKAR_INVT_EXTRA` | STRING 50 | Extra / user-defined |
| `BKAR_INVT_PDATE` | DATE | Payment/posting date |
| `BKAR_INVT_MCRAT` | FLOAT | Multi-currency exchange rate |
| `BKAR_INVT_MCCOD` | STRING 3 | Multi-currency code |
| `BKAR_INVT_TRXN` | FLOAT | Transaction number (sequence) |
| `BKAR_INVT_CHKNO` | FLOAT | Check number that paid this invoice |
| `BKAR_INVT_DEPNO` | FLOAT | Deposit number applied |
| `BKAR_INVT_CHKAC` | UBINARY | Bank account code for the check |
| `BKAR_INVT_OPEND` | DATE | Date opened / posted to AR |
| `BKAR_INVT_CLOSD` | DATE | Date fully paid / closed (empty = still open) |
| `BKAR_INVT_NORMP` | STRING 1 | Normal payment flag |

---

## BKART — AR Customer Transactions (12 fields)

Primary key: `BKART_CUST` + `BKART_TRXN`

Detailed transaction log per customer — records each payment, credit, debit, and finance charge with a link back to the source invoice.

| Field | Type | Meaning |
|-------|------|---------|
| `BKART_CUST` | STRING 10 | Customer code (PK 1) |
| `BKART_TRXN` | FLOAT | Transaction number (PK 2) |
| `BKART_TYPE` | STRING 1 | Type: I=invoice, P=payment, C=credit, D=deposit, F=finance charge |
| `BKART_DISC` | FLOAT | Discount amount taken |
| `BKART_AMOUNT` | FLOAT | Transaction amount |
| `BKART_POSTDATE` | DATE | Posted date |
| `BKART_CNTR` | UBINARY | Line counter (for multi-line transactions) |
| `BKART_ENTDATE` | DATE | Date entered |
| `BKART_TRXNLINK` | FLOAT | Linked transaction number (payment → invoice link) |
| `BKART_INVC` | FLOAT | Invoice number this transaction applies to |
| `BKART_CHECK` | FLOAT | Check number |
| `BKART_NOTE` | STRING 1 | Has notes flag (Y = see BKARTNOT) |

BKART_TRXNLINK is how AR-C (Record Payments) links a payment to one or more invoices. When a payment partially pays an invoice, BKART records the payment with a link to the invoice's BKARINVT row, and BKARINVT.BKAR_INVT_AMTRM is reduced.

---

## AR aging bucket calculation (confirmed logic from DDF, Pass 111a 2026-06-19)

EVO does **not store** pre-computed aging buckets. The AR-F (Print Aging) program computes them at run time:

1. **Source:** Scan BKARINVT rows where `BKAR_INVT_AMTRM > 0` (open balance) for the selected customer range.
2. **Due date:** Computed from `BKAR_INVT_DATE` + payment terms days. Terms are looked up via `BKAR_INVT_TERMN` against the payment terms table (likely BKTERMS or similar — the exact table is not confirmed from DDF alone; the customer master has `BKAR_TERMS_NUM` as the FK).
3. **Days past due:** `report_date − due_date`.
4. **Aging buckets:** Bucketed into current / 1–30 / 31–60 / 61–90 / over 90. The exact bucket-day boundaries are parameters in T7ARF.DFM (42-field form) — the form has fields for bucket day settings, but their exact field names require DFM extraction.
5. **Output:** BKARCUST.BKAR_OUTINV holds the customer's total outstanding balance. The aging report breaks this total into buckets for the statement or collection analysis.

The BKARCUST customer statistics (BKAR_DAYS_TOPAY = average days to pay; BKAR_NUM_INVCS = invoice count) are updated when payments post via AR-C.

**The BKAB\* tables** (BKABCUST 5f, BKABVEND 2f) are billing/subscription configuration tables — BKAB_PERIOD is a billing period definition used by the interest-charging and statement programs (AR-D, AR-E), not an aging bucket table.

---

## Table family summary

| Family | Pattern | Role |
|--------|---------|------|
| BKARCUST / BKARECST | 106f same schema | Active customer master; BKARECST = same layout, purpose unclear (possibly cached stats view) |
| BKARSHIP | 106f same schema | Ship-to address overrides (customer alternate addresses) |
| BKARINV / BKARHINV / BKARRINV | 84f same schema | Open invoices / history archive / receipt copy |
| BKARINVL / BKARHIVL / BKARRIVL / BKARSIVL | 28f same schema | Invoice lines: open / history / receipt / ship |
| BKARINVT / BKAREIVT | 23/24f (DDF artifact) | Open-item AR ledger — source of aging |
| BKART / BKARTNOT | 12f + 3f | Customer transaction log + notes |
| BKARTXN / BKARTXNB / BKARTXNS | 14f same schema | Inventory transaction records for shipments |
| BKARDESC / BKARDPST / BKARRDSC / BKARHDSC | 5f same schema | Saved line-item descriptions |
| BKARDEP | 6f | Customer deposit records |
| BKARCHKF / BKARCHKH | 12f same schema | Finance charge: current / history |
| BKARINVI | 16f | Invoice staging (import/EDI intake) |
| BKARINVV | 77f | Invoice vouchered/verified record |
| BKARHTAX | 5f | Tax history per invoice |

---

## Notes & open questions

- BKAREIVT vs BKARINVT: Both have the same PK and nearly identical fields. BKAREIVT has a spurious BKAB_PERIOD field (LOGICAL size 1792 at an overlapping offset) which is a Btrieve alternate-key index definition artifact, not a real data field. Treat BKARINVT (23f) as canonical.
- The exact payment terms table name is unconfirmed from DDF alone. BKAR_TERMS_NUM (UBINARY in BKARCUST) and BKAR_INVT_TERMN (UBINARY in BKARINVT) both reference it. Likely BKTERMS or similar — needs live data or RWN source to confirm.
- BKARINVV (77f) is not yet documented — field semantics unknown. It may be the "voucher-verified" copy of a posted invoice.
