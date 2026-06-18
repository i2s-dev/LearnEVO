import sys
sys.stdout.reconfigure(encoding='utf-8')

path = r'C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\HELP-RESOURCES.md'

block = r'''

---

## Pass 89 — SO sub-programs, PO remaining, AP full, AR full (104 DFMs)

### SO-O Sub-Programs (Reports/Inquiries)

| Code | DFM | Purpose |
|------|-----|---------|
| SO-OA | T7SOOA | Backorder / open order report — range by ESD, customer, job, SO, item, sort by, currency, customer PO, salesperson 1&2, order date, due date, item class; options: grand totals only, line detail, comments, MO totals, kit components, include BO |
| SO-OB | T7SOOB | Packing slip sequence report — item/job/ESD/customer ranges |
| SO-OD | T7SOOD | Print SOs — SO/customer/customer PO/salesperson ranges, one SO per page |
| SO-O-E | T7SOOE | WO/labor scheduling report — machine 1/2/3 ranges, WO status, WO start date, item cat/class, ESD, customer, job, lead source 1&2, customer due date; option: include remaining labor, include SR, tag all locs |
| SO-OF | T7SOOF | Production planning/dispatch — customer due date ranges across 5 filter sets, item cat/class, ESD, customer, job, SO; options: complete only, credit hold, include released, UOH by loc, price, holdups, zero-UOH |
| SO-O-G | T7SOOG | WO-to-SO cross-reference — item/customer/SO/WO/ESD/WO-finished/job ranges, sort, WO status; options: exclude item types, all open SO lines, SO lines without WOs |
| SO-OH | T7SOOH | Invoice type report — invoice types (INVCTYPE[1..3]: finance charges, AR vouchers, SO module), invoice date/number/SO/customer ranges, sort by invoice or date; option: drop-ship only, SR module invoices, currency range |
| SO-OI | T7SOOI | Open order report (variant of OA) — same ranges + use.ship.date, item class/category |
| SO-O-M | T7SOOM | SO change history report — change date range, customer/item/job/SO ranges, sort; options: changes in price/qty/ESD/ASD/discount/location/commission, print archived SO changes |
| SO-O-N | T7SOON | On-time delivery report — item class/cat/num, customer, invoice date, SO/invoice nums, allowable days early/late, ESD/ASD basis; options: summary only, late orders only, print ship log, net days, customer class range |

### SO-P Sub-Programs (Processing/Print)

| Code | DFM | Purpose |
|------|-----|---------|
| SO-NQty | T7SONQTY | Quantity conversion — shows item stock levels (UOH/UOSO/UBO/available/min-ord/reorder-level/lead-time/in-WIP/allocated/on-WO/on-PO) when converting SO line qty; fields BKIC.PROD.UOH/UOSO/UBO/RAMT/RLVL/UOO + MTIC.PROD.AVAIL/LEAD/UIWIP/UOA/UOWO |
| SO-PB | T7SOPB | Print quotations — quotation number range, print linked docs (PLDTYPE), notes/hidden notes, tax/freight, kit components, options, system quote notes last, print item rev (ECO), tax codes for $0, mark as printed, archived quotes, contract pricing matrix, price code matrix |
| SO-PC | T7SOPC | Quote conversion to SO — ORDER.DATE, EST.DATE, DUE.DATE, CUST.PO, LOC, CNVT.NOTES, KEEP.QUOTE; batch mode: from/thru quote range, from/thru unconverted date, pass.quote (desc/job/none), new.status (Y/L/A/N/S/D/W/B), reason.code, use.ship.lead, close.QUOTE, status change only |
| SO-PF | T7SOPF | Blanket SO releases — group.Mlines, shows BKAR.INVL.PCODE/PDESC/OOQTY/ESD/UM, balance-on-order (blanket.left), release qty/date per line |
| SO-PI | T7SOPI | Shipping/invoicing — invoice/SO number, frt.charge, tracking.num, shipping company/shipper number, drop ship flag, gross weight, date filter, ship.cust |
| SO-PJ | T7SOPJ | Background processing progress form — fixfile, stime |
| SO-PK | T7SOPK | Edit posted invoices — bill-to: BKAR.INV.CUSCOD/CUSNME/CUSA1/CUSA2[1..2]/CUSCTY/CUSZIP/CUSST/CUSCNT/CUSATT + ship-to: BKAR.INV.SHPCOD/SHPNME/SHPA1/SHPA2[1..2]/SHPCTY/SHPZIP/SHPST/SHPCNT/SHPATN; also BKAR.INV.DESC/SHPVIA/TERMNM/JOBNUM/FOB/BILCOD/ORDDTE/INVDTE |
| SO-PM | T7SOPM | Print quote list — customer/order-date ranges, print unconverted/converted/all quotes, check job# and description |
| SO-PO | T7SOPO | Generate POs from SOs — JOBNO, order date, est-receipt date, offset, from/thru SO/order/customer/vendor, UBO (use backorder qty), pass.sell.price, pass.line.num, pass.ship.info, pass.more.info (via/FOB/terms/notes), pass.po.num, pass.job.num [H/L/B/N] |
| SO-POR | T7SOPOR | SO-PO review — item/desc, PO.DATE, ER.DATE, QTY, vendor, price, SO line (BKAR.INVL.INVNM) |
| SO-PP | T7SOPP | Mass update ESD on SOs — from/thru SO, ESD range, new ESD, customer filter |

### SO-Q Sub-Programs (Pricing)

| Code | DFM | Purpose |
|------|-----|---------|
| SO-QA | T7SOQA | Update item base price — from.item, BKIC.PROD.PRICE, BKIC.PROD.NOTE, HOW.ROUND, CHG.PCODE, CHG.CONTRACT |
| SO-QB | T7SOQB | Price list report — item/cat/class ranges, active status filter [YNODEPSQR], format with $ and commas |
| SO-QC | T7SOQC | Mass price change — direction (CHG.DIR.ARR[1/2]: increase/decrease), type (CHG.TYPE.ARR[1/2]: %/flat), ENT_CHANGE_AMT, item/class/cat/customer ranges, active status, new expiration date, update contract/price codes ONLY option, cust.filter [ICN] |
| SO-QH | T7SOQH | Price matrix entry — BKIC.PMAT.QTY[1..10]/RATE[1..10]/PER[1..10]/ISRET[1..10] (retail flag)/COMM1[1..10]/COMM2[1..10]; EXIST.ACTION for existing codes; item/price-code/customer/base-price/expiration/inv-class/start-end-date/SO-total-disc/discount-code/minimum/promo fields |
| SO-QI | T7SOQI | Price list/discount code report — FROM.DCODE/THRU.DCODE, customer/class/cat/vendor ranges, exp-date range, price code range, INC.RETAIL, all.locs, sort by item or customer, incl.last.so, SO order date range |
| SO-QJ | T7SOQJ | Cost-based price update — COST.TYPE.TXT, markup vs margin (use.margin), CHG.PCODE/CHG.CONTRACT, item/class/cat, active status, report.only, prevent.below |
| SO-Q-K | T7SOQK | Print catalog — item type [RFAMNLBTKO], class/cat/vendor ranges, active status, sort, pricing (RTYPE), price code (PC), sold-since date, extended desc, thumbnail images, price quantity breaks |
| SO-Q-L | T7SOQL | Import new SO prices — from.item, from.esd/thru.esd, new.price, imp.filename (CSV), FIELD.NUMBER[1/2] (column mapping) |

### SO-R, SO-S, SO-V, SO-Contract Review, SO-Serial

| Code | DFM | Purpose |
|------|-----|---------|
| SO-R | T7SOR | Void invoice list — BKAR.INV.INVDTE/ORDDTE/SHIPDT/CUSCOD/CUSNME/CUSA1/CUSA2[1..2]/CUSCTY/CUSST/CUSCNT/CUSZIP, VOID.DATE, BKAR.INV.SONUM/SUBTOT/TAXAMT/FRGHT, DISPDEPOSIT/DISPRETEN/DISPTOTAL, BKAR.INV.SLSP/GLDPT/LOC/DESC |
| SO Contract Review | T7SORevu | Digital signature approval for SOs — SO.REQUIRE, SO.DEPT, SO.EMPNAME, SO.APPROVE, SO.ADATE, so.entby, so.edate; requires password T7SORevuPSWD (ct.empname/dept/enter.pswd) |
| SO-S | T7SOS | Release SOs from hold — AUTO.RCOMM/AUTO.BO/REL.ALL, SO/customer/order/item ranges |
| SO-SERIAL | T7SOSER | Allocate serial numbers to SO — BKAR.TXN.SERIAL, MTSER.BIN, alloc.qty, qty.left, generate/tag serials |
| SO-V | T7SOV | Maintain SO shipping dates — line-by-line: edit.ASDate/edit.ESDate, BKAR.INVL.PQTY/UBO/PCODE/PDESC; LINE.PROD.* parallel display fields; SONUM.CHAR |

### PO Remaining Sub-Programs

| Code | DFM | Purpose |
|------|-----|---------|
| PO line history | T7POLINEHIST | PO line change history — ISAP.CHG table: CDATE, BPRICE/APRICE (price before/after), BDISC/ADISC (discount B/A), BOOQTY/AOOQTY (ordered qty B/A), BARD/AARD (actual receipt date B/A), BERD/AERD (expected receipt date B/A), BGLA/BGLD/AGLA/AGLD (GL acct/dept B/A), BWOP/BWOS/BOPER/AWOP/AWOS/AOPER (WO prefix/suffix/operation B/A), ISAP.CHG.USER |
| PO-L-P | T7POLP | Vendor/item price list report — vendor/item ranges |
| PO-M | T7POM | PO inquiry — vendor/item/PO/WO/job/base-price/date search; shows WO routing (MTWORO.OPER/OPERDESC/WC/STQTY/QTYCOM/%COMP/VEND/PO), WO header (MTWO.WIP.*), PO lines (BKAP.POL.WOPRE*/PONM/PCODE/PQTY), receipts, SO cross-reference |
| PO Master | T7POMAST | PO master inquiry — vendor info + item stock: UOH/UOSO/UBO/UOO/UIQC/UOWO/UOA/AVAIL/UIWIP; fields MTIC.PROD.UIQC (in QC), MTIC.PROD.UOWO (on WO), MTIC.PROD.UOA (allocation), MTIC.PROD.AVAIL (available), MTIC.PROD.UIWIP (in WIP) |
| PO-P | T7POP | Vendor master — BKAP.VENDCODE/NAME/SORT/ADD1[1]/ADD2[1]/CITY[1]/ZIP/STATE/COUNTRY[1]/CONTACT[1]/TELEPHONE[1..3]/IS.MCCODE (currency)/START.DATE, remittance: ADD1[2]/ADD2[2]/CITY[2]/REM.ZIP/REM.STATE/COUNTRY[2], BKAP.IS.DCODE/CLASS/TERMS.NUM/GL.ACCT/GL.DPT/SHIP.VIA/FOB.POINT/CUST.CODE/IS.TAXIN/LASTPMT, BKAP2.ID/IS.TAXGRP/SEND.1099, WEBLINK |
| PO-POP-GET | T7POPGET | Generic popup — POPVALUE[1..5], POPDATE[1..5] |
| PO-Q | T7POQ | Maintain PO delivery dates — line-by-line: edit.ERDate/ARDate/conf/price/pqty, upd.all.ERD/ARD; LINE.PCODE/PDESC/ERD/ARD/REF/QTY/CONF/PRICE; BKAP.PO.CONFIRM[1]; &Clear All / Confirm All options |
| PO-S (POS) | T7POS | Point of Sale — IS.QSOA.ITEM/DESC/QTY/PRICE/DISC (line items); T7POSCD: amount due/tendered/change; T7POSI: BKCM.ACCC.CCODE/DESC (category codes); T7POSX: is.stype.type + QSOA items — POS module lives in the PO module area |

### ISAP.CHG Table — PO Line Change History

Confirmed fields from T7POLINEHIST.DFM:

| Field | Meaning |
|-------|---------|
| ISAP.CHG.CDATE | Change date |
| ISAP.CHG.BPRICE / APRICE | Price before/after |
| ISAP.CHG.BDISC / ADISC | Discount before/after |
| ISAP.CHG.BOOQTY / AOOQTY | Ordered quantity before/after |
| ISAP.CHG.BARD / AARD | Actual receipt date before/after |
| ISAP.CHG.BERD / AERD | Expected receipt date before/after |
| ISAP.CHG.BGLA / AGLA | GL account before/after |
| ISAP.CHG.BGLD / AGLD | GL department before/after |
| ISAP.CHG.BWOP / AWOP | WO prefix before/after |
| ISAP.CHG.BWOS / AWOS | WO suffix before/after |
| ISAP.CHG.BOPER / AOPER | WO operation before/after |
| ISAP.CHG.USER | User who made change |

### AP Module — Full Schema

#### AP-A Vendor Master (T7APA / t7apaC / t7apae)

**BKAP table** — AP vendor master:

| Field | Meaning |
|-------|---------|
| BKAP.VENDCODE | Vendor code (primary key) |
| BKAP.VENDNAME | Vendor name |
| BKAP.SORT | Alpha sort code |
| BKAP.ADD1 / ADD2 | Street address lines |
| BKAP.CITY / STATE / ZIP / COUNTRY | Address |
| BKAP.ADD1[2]/ADD2[2]/CITY[2]/REM.ZIP/REM.STATE/COUNTRY[2] | Remittance address |
| BKAP.TELEPHONE[1] / [3] | Phone / fax |
| BKAP.CONTACT[1..4] | Up to 4 contact names |
| BKAP.EMAIL[1..4] | Up to 4 email addresses |
| BKAP.IS.MCCODE | Multi-currency code |
| BKAP.TERMS.NUM | Payment terms number |
| BKAP.GL.ACCT / GL.DPT | Default GL account/dept |
| BKAP.SHIP.VIA / FOB.POINT | Shipping method/FOB |
| BKAP.CLASS | Vendor class |
| BKAP.CUST.CODE | Customer at this vendor (cross-ref to BKAR) |
| BKAP.IS.TAXIN / IS.TAXGRP | Tax-inclusive flag / tax group |
| BKAP.IS.DCODE | Duty code |
| BKAP.START.DATE | Start date |
| BKAP.LASTPMT / LASTPURCH | Last payment/purchase dates |
| BKAP.OUTINV / OUT.CREDIT | Outstanding invoices/credits |
| BKAP.PURCH.YTD / LYR / VAR | Purchase statistics YTD/LY/variance |

**BKAP2 table** — vendor user-defined fields (T7APINFO):

| Field Pattern | Description |
|---------------|-------------|
| BKAP2.A1L[1..5] + A1[1..5] | 5 × 1-char UDF (label + value) |
| BKAP2.A10L[1..5] + A10[1..5] | 5 × 10-char UDF (label + value) |
| BKAP2.D8L[1..5] + D8[1..5] | 5 × date UDF (label + value) |
| BKAP2.A30L[1..5] + A30[1..5] | 5 × 30-char UDF (label + value) |
| BKAP2.ID | Tax ID number |
| BKAP2.SEND.1099 | 1099 flag |

**ISAPEX table** — vendor extended/bank data (T7APABANK / t7apaC / t7apae):

| Field | Meaning |
|-------|---------|
| ISAPEX.BNAME | Bank name |
| ISAPEX.BACCTNAM | Account name |
| ISAPEX.BEMAIL | Bank email |
| ISAPEX.BADD1/BADD2/BADD3 | Bank address lines |
| ISAPEX.BCITY / STATE / ZIP | Bank city/state/zip |
| ISAPEX.BCONTACT | Bank contact |
| ISAPEX.BAPHONE | Bank phone |
| ISAPEX.BACCTTYP | Account type [C=checking/S=savings] |
| ISAPEX.ALPHA[1..2] | Misc info 1 and 2 |
| ISAPEX.LONGNAME | Long vendor name |
| ISAPEX.DATE[1] | Review date |

#### AP Voucher Entry (T7APB)

**BKAP.INVL table** — AP voucher distribution lines:

| Field | Meaning |
|-------|---------|
| BKAP.INVL.GLACT[1..10] | GL account (up to 10 lines) |
| BKAP.INVL.GLDPT[1..10] | GL department (up to 10 lines) |
| BKAP.INVL.GLD[1..10] | GL description (up to 10 lines) |
| BKAP.INVL.DC | Debit/credit flag |
| BKAP.INVL.DAMT | Distribution amount |
| BKAP.INVL.TERMD | Terms date |
| BKAP.INVL.DESC | Description |
| BKAP.INVL.DATE | Invoice date |
| BKAP.INVL.TYPED | Invoice type |
| BKAP.INVL.ISCUR | Currency code |
| BKAP.INVL.TAMT | Total amount |
| BKAP.INVL.JOB | Job number |
| BKAP.INVL.CODE | Recurring voucher selection code |
| BKAP.INVL.NUM | Voucher/invoice number |
| BKAP.INVL.TERMN | Terms number |
| BKAP.INVT.SDATE | Scheduled payment date |
| BKAP.INVT.TAX | Tax amount |
| BKAP.INVT.FRT | Freight amount |

#### AP Check Operations (T7APH / T7APT / T7APQ)

**BKAP.CHK table** — check history:

| Field | Meaning |
|-------|---------|
| BKAP.CHK.ISCUR | Currency |
| BKAP.CHK.INVDTE | Invoice date |
| BKAP.CHK.INVAMT | Invoice amount |
| BKAP.CHK.DISC | Discount |
| BKAP.CHK.AMTPD | Amount paid |
| BKAP.CHK.DESC | Description |
| BKAP.CHK.CHKDTE | Check date |
| BKAP.CHK.TYPE | Check type |
| BKAP.CHK.CHKACT | Bank account number |

#### AP-C Voucher from PO Receipt (T7APC) — BKQC Table

| Field | Meaning |
|-------|---------|
| BKQC.PO.NUM | Purchase order number |
| BKQC.RECVR.NUM | QC receiver number |
| BKQC.POL.ITM.NO | PO line item number |
| BKQC.RECV.DATE | Receipt date |
| BKQC.PROD.CODE | Item/product code |
| BKQC.PKSLIP.NUM | Packing slip number |
| BKQC.QTY.RECVD | Quantity received |
| BKQC.QTY.BUYOFF | Quantity bought off (accepted) |
| BKQC.QTY.REJECT | Quantity rejected |

#### AP Sub-Program Summary

| Code | DFM | Purpose |
|------|-----|---------|
| AP-A | T7APA / t7apae / t7apaC | Vendor master (basic/full/enhanced) |
| AP-BANK | T7APABANK | Vendor ACH/bank information |
| AP-CON | T7APACON | Vendor contacts (up to 4) |
| AP-INFO | T7APINFO | Vendor UDF fields (BKAP2: 20 UDFs in 4 types) |
| AP-STA | T7APASTA | Vendor statistics (purchase YTD/LY) |
| AP-PRC | T7APAPRC | Check vendor item pricing |
| AP-B | T7APB | Voucher entry — 10-line GL distribution |
| AP-C | T7APC | Receive PO with voucher — QC receiver integration |
| AP-D | T7APD | Enter scheduled payment dates |
| AP-E | T7APE | Cash requirements report |
| AP-F | t7apf | Check selection (interactive payment) |
| AP-G | t7apg | Pro forma check register |
| AP-H | T7APH | Print checks (+ ACH/NACHA export) |
| AP-HASK | T7APHASK | Check note entry per vendor |
| AP-I | T7API | AP aging/listing — BKSY.AP.AGING[1..5] configurable periods |
| AP-J | T7APJ | Vendor listing/directory report |
| AP-K | T7APK | Vendor labels report |
| AP-L | t7apl | Recalculate MTD/YTD vendor totals |
| AP-M | T7APM | Vendor mail labels |
| AP-O | T7APO | Recurring voucher maintenance — 10-line GL distribution |
| AP-P | T7APP | Generate recurring vouchers by selection code |
| AP-Q | T7APQ | Void check |
| AP-R | T7APR | Payment history report (check register) |
| AP-S | T7APS | 1099 report — TXTTYPE, YEAR, FIN filter |
| AP-T | T7APT | Check inquiry — full check + invoice + PO detail |
| AP-V | T7APV | Vendor deposits (uses BKAR.DEP table) |
| AP-X | T7APX | Invoice report — archived / no-link invoices |
| AP-Y | T7APY | Reprint checks / email remittances |
| AP-YB | T7APYB | Pinnacle bank check export (CSV) |
| AP-YC | T7APYC | NACHA/ACH export (TXT) — company.tax.id, eff.date |
| AP-ZA | T7APZA | Vendor purchase analysis — 3 date ranges (YTD/LYYTD/LY), top-N |

#### AP Aging Configuration

**BKSY.AP.AGING[1..5]** — configurable aging bucket thresholds (same pattern as AR); configured in system setup.

### AR Module — Full Schema

#### AR-A Customer Master (T7ARAC / T7ARAE)

**BKAR table** — AR customer master:

| Field | Meaning |
|-------|---------|
| BKAR.CUSTCODE | Customer code (primary key) |
| BKAR.CUSTNAME | Customer name |
| BKAR.SORT | Alpha sort code |
| BKAR.ADD1 | Street address line 1 |
| BKAR.ADD2[1..2] | Street address lines 2-3 |
| BKAR.CITY / STATE / ZIP / COUNTRY | Address |
| BKAR.FAX.PHONE | Fax number |
| BKAR.TELEPHONE[1..5] | Up to 5 phone numbers |
| BKAR.CONTACT[1..5] | Up to 5 contact names |
| BKAR.EMAIL[1..5] | Up to 5 email addresses |
| BKAR.IS.MCCODE | Multi-currency code |
| BKAR.REQD.CERTS | Required certifications |
| BKAR.SLSP.NUM[1..2] | Salesperson 1 and 2 codes |
| BKAR.COMM[1..2] | Commission % for salesperson 1 and 2 |
| BKAR.CREDIT.HLD | Credit hold flag |
| BKAR.CREDITLMT | Credit limit |
| BKAR.FOLUPDTE | Follow-up date |
| BKAR.DAYS.TOPAY | Average days to pay |
| BKAR.LASTPMT | Last payment date |
| BKAR.LASTSALE | Last sale date |
| BKAR.OUT.CREDIT[1..2] | Outstanding credits (possibly AR/SO split) |
| BKAR.OUTINV | Outstanding invoices |
| BKAR.GLACCT | Default GL sales account |
| BKAR.FOB | FOB point |
| BKAR.SHIPTO | Default ship-to code |
| BKAR.GROUP | Customer group |
| BKAR.START.DATE | Start date |
| BKAR.WEBLINK | Website URL |

**BKAR statistics fields** (T7ARASTA):

| Field | Meaning |
|-------|---------|
| BKAR.GROSS.YTD / LYR / VAR | Gross sales YTD / last year / variance |
| BKAR.COGS.YTD / LYR / VAR | Cost of goods sold YTD / LY / variance |
| BKAR.NET.YTD / LYR / VAR | Net sales YTD / LY / variance |
| BKAR.PNET.YTD / LYR / VAR | Net % YTD / LY / variance |

**ISAREX table** — customer extended data (T7ARAC / T7ARAE):

| Field | Meaning |
|-------|---------|
| ISAREX.ALPHA[1..2] | Misc info 1 and 2 |
| ISAREX.EXTADD[1..8] | Extended address lines (up to 8) |

**BKCM.DUNH.FORM** — dunning form code (in BKAR credit record T7ARACRE).

**RTM.PRINT.GROUP** — per-customer report template print group for customized invoice/SO printing.

#### AR Voucher Entry (T7ARB)

**BKAR.INVV table** — AR voucher distribution lines:

| Field | Meaning |
|-------|---------|
| BKAR.INVV.TERMD | Terms date |
| BKAR.INVV.DESC | Description |
| BKAR.INVV.DATE | Voucher date |
| BKAR.INVV.TYPED | Voucher type |
| BKAR.INVV.ISCUR | Currency code |
| BKAR.INVV.TAMT | Total amount |
| BKAR.INVV.GLACT[1..10] | GL account (up to 10 lines) |
| BKAR.INVV.GLDPT[1..10] | GL department (up to 10 lines) |
| BKAR.INVV.GLD[1..10] | GL description (up to 10 lines) |

#### AR Payment and Deposit (T7ARC / T7ARN)

AR-C record payments: CUSTCODE, CHECK_AMT, CHECK_NUM, DEPOSIT_NUM, NEG.CHK; BKAR.OUT.CREDIT[1/2]; invoice list INV_NUM/PS/DATE/AMTRM/APPLIED; exceptions EXCP.INVOICE/AMOUNT/DISC/DESC; import payments from file.

AR-N customer deposits (same BKAR.DEP table as SO deposits): BKAR.DEP.SO/DATE/REMAIN.AMT/DEP.DESC, CHECK.NO, BKAR.DEP.CUST, MAPPED; options: enter deposit, generate invoice, map lines, split deposit, credit card.

#### AR Credit Card (T7ART)

**IS.CC table** — stored credit card data:

| Field | Meaning |
|-------|---------|
| IS.CC.CARDNAME | Name on card |
| IS.CC.ZIP | Billing zip |
| IS.CC.CARDTYPE | Card type (Visa/MC/etc.) |
| IS.CC.MASKED | Masked card number |
| IS.CC.EXP | Expiration date (MMYY) |
| IS.CC.PROCESS | Processor name |
| IS.CC.ADDRESS | Billing address |
| onetime | One-time use flag |

#### AR Tax Operations (T7ARL / T7ARK)

**BKIS.TAX table** — sales tax transfer:
- BKIS.TAX.CODE, BKIS.TAX.DATE, BKIS.TAX.TAG, TAX.PONO

**ISIS.TXF table** — tax file:
- ISIS.TXF.DESC, ISIS.TXF.SOPERC

AR-K tax report: CUR_HIST [P/O/B paid/outstanding/both], FULLYPD, POSO [P/S purchases/sales], BASE [B/S base/source], SUMMARY [S/D], tax code/group ranges, invoice date range.

#### AR Sub-Program Summary

| Code | DFM | Purpose |
|------|-----|---------|
| AR-2DB | T7ARA2DB | 2D barcode layout (IS2D.BAR.*) for AR documents |
| AR-AC | T7ARAC | Customer master (compact form) |
| AR-ACE | T7ARAE | Customer master (full form) — web, territory, lead source, group |
| AR-ACON | T7ARACON | Customer contacts (up to 5) |
| AR-ACRE | T7ARACRE | Customer credit — credit limit, hold, follow-up, dunning form (BKCM.DUNH.FORM) |
| AR-ASTA | T7ARASTA | Customer statistics — gross/COGS/net YTD/LY/variance |
| AR-APRC | T7ARAPRC | Check customer item pricing |
| AR-B | T7ARB | AR voucher entry — 10-line GL distribution (BKAR.INVV.*) |
| AR-C | T7ARC | Record payments — check/deposit, invoice selection, exceptions, import |
| AR-D | T7ARD | Charge interest — CALC_DATE, NMININT, COMPOUND, BKSY.AR.INT.DAY |
| AR-E | T7ARE | Print statements — balance forward, age statement, print groups, deposits |
| AR-F | T7ARF | AR aging — BKSY.AR.AGING[1..5], follow-up codes, salesperson range |
| AR-G | T7ARG | Customer code/name list — active/inactive, credit hold/over limit filters |
| AR-H | T7ARH | Customer general info report |
| AR-I | T7ARI | Customer mail labels — OPEN.AR/OPEN.DE/OPEN.CR flags |
| AR-K | T7ARK | Tax report — paid/outstanding/both, purchase vs sales |
| AR-L | T7ARL | Transfer sales taxes to GL — BKIS.TAX.* and ISIS.TXF.* |
| AR-M | T7ARM | Customer refund — creates AP vendor + check via BKAP.INVT.* |
| AR-N | T7ARN | Customer deposits — BKAR.DEP.*, credit card, map lines, generate invoice |
| AR-P | T7ARP | Payment reminders — days prior/late, due/past-due filter |
| AR-R | T7ARR | Payment history report (check register) |
| AR-T | T7ART | Credit card management — IS.CC.* stored cards |
| AR-U | T7ARU | Dunning — from/thru customer, pastdue.days |

#### AR Aging Configuration

**BKSY.AR.AGING[1..5]** — configurable AR aging bucket thresholds (mirrors BKSY.AP.AGING[1..5]).

### New Tables Confirmed in Pass 89

| Table | Module | Primary Purpose |
|-------|--------|----------------|
| ISAP.CHG | PO | PO line change history (14 before/after field pairs + user) |
| ISAPEX | AP | Vendor extended data (bank, misc, long name, review date) |
| BKAP2 | AP | Vendor UDF (20 fields: 5×1-char, 5×10-char, 5×date, 5×30-char) |
| BKAP.CHK | AP | Check history (currency, dates, amounts, discount, bank acct) |
| BKQC | AP/PO | QC receiver records (PO, item, qty received/bought-off/rejected) |
| BKAP.INVL | AP | AP voucher GL distribution lines (10-line capacity) |
| BKAP.INVT | AP | AP voucher header (scheduled date, tax, freight) |
| BKAR | AR | Customer master (full schema documented) |
| ISAREX | AR | Customer extended data (2 misc info, 8 extended address lines) |
| BKAR.INVV | AR | AR voucher GL distribution lines (10-line capacity) |
| IS.CC | AR | Stored credit card data (masked number, expiration, processor) |
| BKIS.TAX | AR | Sales tax transfer records |
| ISIS.TXF | AR | Tax file (description, percentage) |
| IS.QSOA | PO | Point-of-sale order lines (item, desc, qty, price, discount) |
| BKCM.ACCC | PO | POS item category codes |
'''

with open(path, 'a', encoding='utf-8') as f:
    f.write(block)

print('Pass 89 block appended to HELP-RESOURCES.md')
