# Accounts Receivable (AR)

Status: verified | Pass 418 (2026-06-30)

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
| `AR-I` | Print Open Credits / Deposits | BKARI;T6ARI |
| `AR-J` | Print Customer List by Class | BKARJ;rolodex.run |
| `AR-K` | Print Sales Tax Report | BKARK |
| `AR-L` | Transfer Sales Taxes | BKARL |
| `AR-M` | Cash Receipts / Unapplied Credits | BKARM |
| `AR-N` | Print Customer Deposits | BKARN;T6arn |
| `AR-P` | Generate Dun Letters / Labels | BKARP;T6ARP |
| `AR-Q` | View Customers (dispatch stub) | BKARQ → BKARAA+BKARQA |
| `AR-R` | Print AR Payment History | BKARR |
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

## Programs (20 total, Pass 265 2026-06-25)

Data extracted from rwn_symbols.json.

| Program | Procs | Lib | DBs | Role / key tables |
|---------|------:|-----|----:|-------------------|
| `T7ARB.RWN` | 301 | ISTECH | 51 | **AR-B Enter Vouchers** — invoice entry; BKARCUST + BKARINVV + ISNOTES; BKAR.INV 86-var |
| `T7ARA.RWN` | 274 | LISTG60 | 45 | **AR-A Enter Customers** — customer master editor; BKARCUST + ISAREX + ISTAXGRP; BKAR.GROSS/COGS/NET 144-var each (sales analysis integration) |
| `T7ARC.RWN` | 228 | LISTG60 | 45 | **AR-C Record Payments** — cash receipts; BKARCUST + BKARINV; BKAR.INV 86-var |
| `T7ARN.RWN` | 191 | ISTECH | 43 | **AR-N Print Customer Deposits** — BKARDEP + BKARINV + BKARCUST |
| `T7ARF.RWN` | 182 | LISTG60 | 31 | **AR-F Print Aging** — BKART + BKYSMSTR; aging computed at runtime from BKARINVT |
| `t7ara2.RWN` | 176 | LISTG60 | 29 | **AR-A secondary form** — BKARCUST + ISTAXGRP + BKCMDUNH; BKAR.GROSS 48-var |
| `T7ARE.RWN` | 163 | LISTG60 | 28 | **AR-E Print Statements** — BKSYMSTR + ISMCF + BKYSMSTR; ISIS.MCF 49-var |
| `T7ARM.RWN` | 159 | ISTECH | 39 | **AR-M Enter Customer Refund** — BKAPINVT + BKGLCHK + BKARCUST |
| `T7ARG.RWN` | 148 | LISTG60 | 19 | **AR-G Print Customer Code/Name** — ISTERMS + BKARCUST + BKARINV |
| `T7ARK.RWN` | 144 | LISTG60 | 23 | **AR-K Print Sales Tax Report** — BKISTAX + ISTAXFIL |
| `T7ARR.RWN` | 137 | LISTG60 | 24 | **AR-R** bank reconciliation; ISBANKS + BKAPCHKF |
| `T7ARP.RWN` | 136 | LISTG60 | 21 | **AR-P Generate Dun Letters** — BKARINVT + BKARCUST; BKAR.INVT 25-var (open-item aging detail) |
| `T7ARH.RWN` | 122 | LISTG60 | 18 | **AR-H Print Customer General Info** — BKARCUST + BKARINV + ISTERMS |
| `T7ARD.RWN` | 121 | LISTG60 | 32 | **AR-D Charge Interest on Invoices** — BKSYMSTR + ISMCF + BKARCUST; ISIS.MCF 49-var |
| `T7ARL.RWN` | 110 | ISTECH | 26 | **AR-L Transfer Sales Taxes** — BKISTAX + ISTAXFIL |
| `T7ARI.RWN` | 103 | LISTG60 | 56 | **AR-I Print Customer Mail Labels** — BKARCUST + BKARINV |
| `T7ARU.RWN` | 85 | LISTG60 | 22 | **AR-U** unapplied payments management; BKARCUST + BKARINVT; IS.NCR 54-var |
| `T7ART.RWN` | 68 | LISTG60 | 56 | **AR-T** i2 custom program; ISCC + BKARCUST |
| `T7ARQ.RWN` | 17 | NZLICE | 56 | NZ license check stub |
| `T7ARSHIP.RWN` | 15 | NZLICE | 56 | NZ ship license check stub |

### Key program revelations (Pass 265)

**T7ARB** (301p, ISTECH) opens **BKARINVV** — the 77-field "invoice vouchered" table. This confirms BKARINVV is written during live invoice entry, not just a reporting artifact. BKARINVV likely stores the full invoice header expanded with pricing/tax verification data before final posting to BKARINV.

**T7ARA** has BKAR.GROSS 144-var + BKAR.COGS 144-var + BKAR.NET 144-var namespaces. These 432 access vars (144 fields × 3 metrics) indicate T7ARA includes a **sales analysis sub-module** — the customer master editor also drives the AR-A sales analysis view with gross/COGS/net breakdowns. This is confirmed by the presence of ISAREX (AR extended data) in the DB list.

**T7ARP** (AR-P Dun Letters, 136p) accesses BKAR.INVT 25-var — BKARINVT's payment-application fields — confirming the dunning process reads each open invoice's age and balance from BKARINVT directly.

**T7ARR** opens ISBANKS + BKAPCHKF — bank account master + check file. This is the **bank reconciliation** program (not explicitly in the legacy menu codes), confirming EVO has a full bank reconciliation workflow accessible via AR.

**New tables confirmed from T7AR* programs:**
- `ISAREX` — AR extended customer data (T7ARA)
- `ISTAXGRP` — Tax group codes (T7ARA, t7ara2)
- `BKISTAX` — IS tax table (T7ARK, T7ARL)
- `ISTAXFIL` — Tax filing records (T7ARK, T7ARL)
- `ISBANKS` — Bank account master (T7ARR)
- `BKGLCHK` — GL check reconciliation work table (T7ARM)
- `ISIS.MCF` — 49-var namespace in T7ARE/T7ARD — MCF = multi-currency factor or matching (exact purpose unclear)

---

## Pass 268 supplement (2026-06-25)

**ISTERMS confirmed as payment terms master** — appears in T7ARF, T7ARE, T7ARG, T7ARH, T7ARD, T7ARP db_files lists. This resolves the open question below; the payment terms table is `ISTERMS`, not `BKTERMS`. `BKAR_TERMS_NUM` (UBINARY FK in BKARCUST) and `BKAR_INVT_TERMN` (UBINARY FK in BKARINVT) both point to `ISTERMS`. Confirmed also in T7POS (PO), T7ARF (AR), T7ARG (AR), T7ARE (AR) — heavily cross-module.

**BKPRSALE in T7ARG** — T7ARG (AR-G Print Customer Code/Name, 148p) opens `BKPRSALE`. This is the payroll sales commission table appearing in the AR aging print program — confirming that commission-based settlements are computed by cross-referencing salesperson commission records from `BKPRSALE` during AR reporting. Also appears in T7PRLJ (PR) = CA DE6.

**IS.TRIG 27-var in T7ARU** — T7ARU (85p) has IS.TRIG 27-var namespace. ISTRIG is an event trigger table — unapplied payments management triggers events (notifications / workflow steps) via the ISTRIG mechanism. The IS.TRIG 27 vars = 27 distinct trigger-type fields accessed.

---

## Notes & open questions

- BKAREIVT vs BKARINVT: Both have the same PK and nearly identical fields. BKAREIVT has a spurious BKAB_PERIOD field (LOGICAL size 1792 at an overlapping offset) which is a Btrieve alternate-key index definition artifact, not a real data field. Treat BKARINVT (23f) as canonical.
- **ISTERMS confirmed** (Pass 268): `BKAR_TERMS_NUM` FK → `ISTERMS`. Full ISTERMS schema not yet extracted from DDF.
- BKARINVV (77f) is not yet documented — field semantics unknown. It may be the "voucher-verified" copy of a posted invoice.
- **TAS6/TAS7 menu-code discrepancy (Pass 334):** T7ARI.DFM caption says "Print Customer Mail Labels" but BKARI.RUN (TAS6) binary says "Include Open Credits / Include Open Deposits". Both are AR-I; the menu code was likely repurposed between TAS6→TAS7. The T7 DFM caption reflects the *current* (TAS7) behavior; BKARI.RUN reflects the legacy function.

---

## Pass 334 — TAS6 binary analysis of 18 BKAR*.RUN programs (2026-06-26)

Source: string extraction from `samples/BKAR*.RUN` (copied from `\\i2s109-solidcrm\DBAMFG$\`).

### 18-program TAS6 inventory

| File | Size | Confirmed role | Key binary evidence |
|------|-----:|----------------|---------------------|
| `BKARA.RUN` | 410 KB | AR-A Enter Customers | "Customer Prices", "Running Balance", "Click to see Imaging", BKARSIVLA |
| `BKARB.RUN` | 324 KB | AR-B Enter AR Vouchers/Invoices | "A/R Voucher", "Leave voucher number blank to have system assign", "Invoices...printed using SO-F reprint mode" |
| `BKARC.RUN` | 331 KB | AR-C Apply Payments | "This Payment", "Excludes deposits linked to a sales order", "Invoice Number/Sales Order No/Customer Code" sort options |
| `BKARCUR.RUN` | 131 KB | AR-A-Q Enter Customer Currency Codes | Literal string "AR-A-Q Enter Customers Currency Codes"; "Customer Currency Conversion Utility [International] 2000.1" |
| `BKARD.RUN` | 204 KB | AR-D Charge Interest on Invoices | "Only those customers that you have indicated are subject to finance", "interest rate is set in AD-B)", opens BKGLTRAN |
| `BKARE.RUN` | 238 KB | AR-E Print Customer Statements | "Statement Date", "Balance Forward Date", "Show Customer Deposits?", BKPRTCFG/BKPRTCFGA |
| `BKARF.RUN` | 230 KB | AR-F Print Invoices / Aged Trial Balance | "Update Credit Hold Status?", "Include deposits(YNO)?", "Print Follow-up Notes?", "Long Check#?"; opens BKPRSALE for commission |
| `BKARG.RUN` | 154 KB | AR-G Print Customer List | "Customer Code and Name List", "Active Customers", "Print From/Thru Customer Code" |
| `BKARH.RUN` | 153 KB | AR-H Print Customer General Info | "Customer General Information", "Started", "Salesperson", "Interest", "Statement", "Price Level", "Terms" (column headers) |
| `BKARI.RUN` | 168 KB | AR-I Print Open Credits / Deposits | "Include Open Credits", "Include Open Deposits", "active/inactive customers" (TAS6 role differs from T7ARI.DFM caption — see Notes) |
| `BKARJ.RUN` | 56 KB | AR-J Print Customer List by Class | "CUSTOMER", "From/Thru Customer Code", "From/Thru Customer Class", "All Customers (A) or just" |
| `BKARK.RUN` | 163 KB | AR-K Print Sales Tax Report | "Tax Code Totals", "Taxable Non-taxable Freight Taxes Collected Taxes Outstanding" |
| `BKARL.RUN` | 198 KB | AR-L Transfer Sales Taxes | "Tax Entries, totalling $", "This Program requires the new TAX system", "Tax Code/Description/Tax Rate/Post Date"; opens BKAPINVT+BKGLTRAN+BKGLXI |
| `BKARM.RUN` | 273 KB | AR-M Cash Receipts / Unapplied Credits | "Unapplied Credits and Deposits", "A/P Voucher", "Bank Account", "Invoice#/Date/Description/Terms", "Customer Name/Currency"; multi-currency |
| `BKARN.RUN` | 273 KB | AR-N Print Customer Deposits | "Total number of deposits", "Grand Total of All Deposits", "Total Deposits for", "for AR aging & statements" |
| `BKARP.RUN` | 220 KB | AR-P Generate Dun Letters / Labels | "Print labels? [Y/N]", "Print Contact Name? [Y/N]", "@@Last Payment@@"; references BKSY.PO.TAXGL |
| `BKARQ.RUN` | 4 KB | AR-Q Dispatch stub | Redirects to BKARAA + BKARQA (not BKARA as previously documented) |
| `BKARR.RUN` | 200 KB | AR-R Print AR Payment History | "Accounts Receivable Payment History", "Active(A) or Archived(D) payments?", opens ISARACHKA |

### Menu code corrections confirmed by binary

| Code | Prior description | Corrected description | Source |
|------|-----------------|-----------------------|--------|
| `AR-I` | Print Customer Mail Labels | Print Open Credits / Deposits | BKARI.RUN strings: "Include Open Credits", "Include Open Deposits" |
| `AR-J` | Print Customer Rolodex | Print Customer List by Class | BKARJ.RUN strings: customer class range filter, no rolodex-specific terms |
| `AR-M` | Enter Customer Refund | Cash Receipts / Unapplied Credits | BKARM.RUN strings: "Unapplied Credits and Deposits", "A/P Voucher", "Bank Account" |
| `AR-Q` | View Customers → BKARA | Dispatch stub → BKARAA + BKARQA | BKARQ.RUN is 4 KB (stub); dispatches to BKARAA and BKARQA, not back to BKARA |
| `AR-R` | (missing from table) | Print AR Payment History | BKARR.RUN: "Accounts Receivable Payment History", opens ISARACHKA |

### BKARCUR — International multi-currency sub-menu (AR-A-Q)

`BKARCUR.RUN` contains the literal menu code string `AR-A-Q Enter Customers Currency Codes` and identifies itself as "Customer Currency Conversion Utility [International] 2000.1". This is a sub-menu of AR-A launched only when multi-currency is enabled. It manages per-customer currency codes used by BKAR_IS_MCCODE (field 104 of BKARCUST). Not listed in the standard AR menu table — it is accessed via AR-A → Q (sub-option).

### BKARF confirms commission linkage to BKPRSALE

`BKARF.RUN` (AR-F Print Invoices) opens `BKPRSALE` — the payroll sales commission table. This mirrors Pass 268's finding of BKPRSALE in T7ARG. The invoice print program computes or references salesperson commission percentages from the PR module when generating the aged trial balance / invoice printout. Establishes a confirmed data link: AR-F → BKPRSALE (PR module).

### BKARM confirms cross-module AR↔AP write-off path

`BKARM.RUN` strings include "A/P Voucher" alongside "Unapplied Credits and Deposits" and "Bank Account". This confirms AR-M can write an AP voucher as a write-off mechanism when unapplied AR credits are cleared against AP balances. BKARM is the primary cash receipts and unapplied payment management program, not simply "customer refund entry" as the prior description stated.

### BKARN deposits feed AR aging

`BKARN.RUN` confirms via the string "for AR aging & statements" that deposit records in BKARDEP (managed by AR-N) are included in the aging calculation. When AR-F (Print Aging) or AR-E (Statements) compute open balances, deposits from BKARDEP reduce the open-item total. This closes an open question about whether deposits affect the aging display.

### Document imaging in BKARA

`BKARA.RUN` contains "Click to see Imaging" — confirms EvoERP has a document imaging subsystem integrated into the AR-A customer master editor. Customers can have scanned documents attached and viewable from within the AR-A form. This is the same imaging capability seen in other modules.

### New accessor namespaces confirmed (Pass 334)

| Namespace | Found in | Meaning |
|-----------|----------|---------|
| `BKAR.CHG.INTRST` | BKARD | AR charge interest flag (maps to BKARCUST.BKAR_CHG_INTRST) |
| `BKAR.CREDIT.HLD` | BKARF | AR credit hold flag (maps to BKARCUST.BKAR_CREDIT_HLD) |
| `BKAR.DAYS.TOPAY` | BKARG, BKARP | AR average days to pay (maps to BKARCUST.BKAR_DAYS_TOPAY) |
| `BKAR.START.DATE` | BKARG | AR account start date (maps to BKARCUST.BKAR_START_DATE) |
| `BKAR.INV.CUSCOD` | BKARA, BKARB | AR invoice header customer code |
| `BKAR.INV.CUSORD` | BKARB, BKARC | AR invoice header customer order number |
| `BKAR.INV.INVDTE` | BKARA, BKARB | AR invoice header invoice date |
| `BKAR.INV.ORDDTE` | BKARB | AR invoice header order date |
| `BKAR.INV.JOBNUM` | BKARB | AR invoice header job/project number |
| `BKAR.INV.SHPVIA` | BKARB | AR invoice header ship-via method |
| `BKAR.INV.SHIPDT` | BKARB | AR invoice header ship date |
| `BKAR.INV.SHIPPR` | BKARB | AR invoice header shipping prepaid flag |
| `BKAR.INV.SHPCOD` | BKARB | AR invoice header ship-to code |
| `BKAR.INV.SHPATN` | BKARB | AR invoice header ship attention name |
| `BKAR.INV.DEPAMT` | BKARN | AR invoice header deposit amount |
| `BKAR.INV.CUSATT` | BKARB | AR invoice header customer attention |
| `BKAR.INV.CUSCNT` | BKARB | AR invoice header customer contact |
| `BKAR.INV.CUSCTY` | BKARB | AR invoice header customer city |
| `BKAR.INV.CUSZIP` | BKARB | AR invoice header customer ZIP |
| `BKAR.INV.ENDLNE` | BKARB | AR invoice header end-of-line marker |
| `BKAR.INV.ISMCDT` | BKARB | AR invoice header IS multi-currency date |
| `BKAR.INV.ISTXKY` | BKARB | AR invoice header IS tax key |
| `BKAR.INVL.EXTRA` | BKARB | AR invoice line extra/user field |
| `BKAR.INVL.INVNM` | BKARB | AR invoice line invoice number |
| `BKAR.INVL.PCODE` | BKARB | AR invoice line product code |
| `BKAR.INVL.PDESC` | BKARB | AR invoice line product description |
| `BKAR.INVL.PDISCK` | BKARB | AR invoice line discount key |
| `BKAR.INVL.PPRCEC` | BKARB | AR invoice line price-each value |
| `BKAR.INVT.AMTRM` | BKARC, BKARP | AR INVT amount remaining (open balance) |
| `BKAR.INVT.CHKNO` | BKARC | AR INVT check number |
| `BKAR.INVT.CLOSD` | BKARC | AR INVT closed date |
| `BKAR.INVT.DEPSTH` | BKARN | AR INVT deposit-to-history flag |
| `BKAR.INVT.MCCOD` | BKARM | AR INVT multi-currency code |
| `BKAR.INVT.NORMP` | BKARC | AR INVT normal payment flag |
| `BKAR.INVT.OPEND` | BKARC | AR INVT open date |
| `BKAR.INVT.CHKAC` | BKARC | AR INVT check bank account code |
| `BKAR.INVT.DEPNO` | BKARN | AR INVT deposit number |
| `BKAR.INVT.MCRAT` | BKARM | AR INVT multi-currency exchange rate |
| `BKAR.INVI.EXTRML` | BKARI | AR invoice inquiry extra-mile flag |
| `BKAR.INVI.INVNM` | BKARI | AR invoice inquiry invoice number |
| `BKAR.INVI.PCOGSC` | BKARI | AR invoice inquiry COGS code |
| `BKAP.OUT.CREDITA` | BKARL | AP outstanding credit archive (cross-module: AR-L tax reconciliation writes AP credits) |
| `BKPR.SLS.EMPNUM` | BKARF | PR salesperson employee number (AR-F → BKPRSALE commission link) |
| `BKSY.PO.TAXGL` | BKARP | System PO tax GL account (AR-P dunning letters references PO tax GL for tax-exempt tracking) |

### New archive/index tables confirmed (Pass 334)

| Table | Found in | Role |
|-------|----------|------|
| `BKARCUSTF` | BKARG, BKARK | BKARCUST filter variant |
| `BKARCUSTL` | BKARB, BKARN | BKARCUST list variant |
| `BKARCHKFA` | BKARC, BKARE, BKARF, BKARN, BKARR | BKARCHKF archive |
| `BKARCHKFI` | BKARE | BKARCHKF index |
| `BKARCHKFL` | BKARF | BKARCHKF list |
| `BKARHINVA` | BKARA, BKARB, BKARD, BKARK | BKARHINV archive |
| `BKARHINVI` | BKARB | BKARHINV index |
| `BKARHDSCA` | BKARA, BKARC | BKARHDSC archive |
| `BKARHIVLA` | BKARA | BKARHIVL archive |
| `BKARECSTA` | BKARA | BKARECST archive |
| `BKARECSTI` | BKARA | BKARECST index |
| `BKARQA` | BKARA, BKARQ | AR-Q dispatch archive |
| `BKARTA` | BKARA, BKARD, BKARF | BKART archive (customer transaction history) |
| `BKARINVA` | BKARA | BKARINV archive |
| `BKARINVI` | BKARA | BKARINV index (confirmed — also in DDF as 16f table) |
| `BKARINVTA` | BKARD | BKARINVT archive |
| `BKARINVTF` | BKARG | BKARINVT filter |
| `BKARINVTFP` | BKARG | BKARINVT filter+print |
| `BKARINVTI` | BKARC | BKARINVT index |
| `BKARINVTL` | BKARM | BKARINVT list |
| `BKARINVTN` | BKARM | BKARINVT next (auto-number sequence?) |
| `BKARINVTV` | BKARM | BKARINVT void variant |
| `BKARDEPA` | BKARC, BKARM, BKARN | BKARDEP archive |
| `BKARDESCA` | BKARA | BKARDESC archive |
| `BKARTNOTA` | BKARF, BKARN | BKARTNOT archive |
| `BKARTXNA` | BKARP | BKARTXN archive |
| `BKARPRTCFG` | BKARE | Print configuration table (new; not in prior DDF) |
| `BKPRTCFGA` | BKARE | BKPRTCFG archive |
| `BKPRSALEA` | BKARF | BKPRSALE archive (PR sales commission) |
| `ISARCRHDA` | BKARF | IS AR credit hold decisions archive |
| `ISARACHKA` | BKARR | IS AR check/payment history archive |
| `ISARAINTA` | BKARD | IS AR invoice totals archive |
| `ISARAHINA` | BKARD | IS AR invoice history archive |
| `BKARSIVLA` | BKARA, BKARB, BKARC, BKARE–BKARN, BKARP, BKARR | BKARSIVL archive — universally present in all AR programs; likely session/display context table (same pattern seen in all BM and GL programs) |

## Live Data Analysis (Pass 418, 2026-06-30)

### BKARCUST — Customer master

| Metric | Value |
|--------|-------|
| Total customers | 4,401 |
| Top states | FL=614, NY=442, CA=329, TX=192 |

Customer class (market segment) distribution:

| Class | Count | Interpretation |
|-------|-------|----------------|
| MAR | 1,335 | Marine |
| ARCH | 1,242 | Architecture |
| (blank) | 638 | Unclassified |
| ELEV | 362 | Elevator |
| INDS | 209 | Industrial |
| DISP | 174 | Display/Distribution |
| IND | 154 | Industrial (alternate code) |
| TRAN | 94 | Transportation |
| ARCR | 61 | Architecture-related |
| RECR | 24 | Recreation |

Payment terms are stored as numeric codes (`BKAR_TERMS_NUM`): 1=1,817 customers, 6=1,710, 11=525, 7=152. These are foreign keys into a terms master table (likely `BKARMTRD` or BKSYMSTR terms slots).

**Geographic note:** Florida is i2 Systems' largest customer state by count — consistent with a manufacturer serving Marine markets. National distribution across all major states.

### BKARINV — Open AR invoices

| Metric | Value |
|--------|-------|
| Total open invoices | 3,692 |
| Date range | up to 2026-07-01 |

Invoice code (`BKAR_INV_INVCD`) distribution:

| Code | Count | Interpretation |
|------|-------|----------------|
| Y | 2,896 | Active unpaid invoice |
| X | 421 | Unknown (possibly transferred or on-hold) |
| (blank) | 202 | Unset / legacy |
| N | 163 | Paid / credit note |

### BKARHINV — Archived AR invoices

| Metric | Value |
|--------|-------|
| Total archived | 95,982 |
| Date range | 1990-11-30 to 2026-06-29 (35+ years) |

**Key insight:** AR archiving is heavily used — 95,982 archived vs. 3,692 open (96.3% of all-time invoices are archived). History dates to 1990, predating the EvoERP software name. This is the longest historical record in the entire database. Contrast with GL: `BKGLATRN=0` (GL transactions are never archived at i2 Systems).

### BKARCHKF — Finance charges (Pass 421, 2026-06-30)

| Metric | Value |
|--------|------:|
| Total finance charge records | 43,698 |
| TYPE='P' (payment applied) | 41,016 |
| TYPE='D' (debit/charge) | 2,682 |

- BKARCHKH=0 (history table empty — finance charge history is not archived separately at i2 Systems)
- BKARTXN=2 / BKARTXNB=0 / BKARTXNS=0 (lot/serial AR tracking not actively used)
- BKARCUST=4,401 customers (confirmed from Pass 420)
- BKARDEP=47 active customer deposits
