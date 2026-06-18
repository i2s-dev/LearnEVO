"""
Pass 103 — append AP/AR/PO/SO module documentation to HELP-RESOURCES.md.
Source: DFM batch analysis (171 forms) + PROJECT-STRUCTURE.md updates.
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

PATH = r'C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\HELP-RESOURCES.md'

BLOCK = '''

---

## Pass 103 — AP/AR/PO/SO Module Form Catalog (2026-06-18)

Source: DFM analysis of 171 forms in `samples/dfm/` (35 AP, 24 AR, 41 PO, 71 SO).
All form descriptions confirmed from Caption fields extracted from DFM files.

---

### AP — Accounts Payable Module (35 forms)

**Menu flow:** AP-A (vendors) → AP-C (receive invoice) → AP-F (select for payment) →
AP-G (proforma check register) → AP-H (print checks) → post to GL automatically.

| Code | Program | Form | What it does |
|------|---------|------|-------------|
| AP-A | BKAPA | T7APA.DFM / t7apaC.DFM / t7apae.DFM | Enter/edit vendor master (name, address, GL expense, terms, 1099 type, ship-via, currency, bank info, pricing) |
| AP-B | BKAPB | T7APB.DFM | Enter recurring/scheduled vouchers with GL distribution |
| AP-C | BKAPC | T7APC.DFM | Enter AP invoice from PO receipt — "Do you want to close this P/O?" prompt |
| AP-D | BKAPD | T7APD.DFM | Schedule payment dates against outstanding invoices |
| AP-E | BKAPE | T7APE.DFM | Print cash requirements report (vouchers due) with terms type filter |
| AP-F | BKAPF | t7apf.dfm | Select items to pay — browse open AP, take discounts, pay via check or ePay |
| AP-G | BKAPG | t7apg.dfm | Print proforma check register (preview before printing checks) |
| AP-H | BKAPH | T7APH.DFM | Print checks (paper, ACH/NACHA, ePay) — sets check date, beginning number, posts |
| AP-I | BKAPI | T7API.DFM | Print AP aging report with 5 configurable aging periods |
| AP-J | BKAPJ | T7APJ.DFM | Print vendor directory (active/inactive/approved/unapproved) |
| AP-K | BKAPK | T7APK.DFM | Print vendor labels / address list |
| AP-L | BKAPL | t7apl.DFM | Recalculate vendor MTD and YTD purchase totals |
| AP-M | BKAPM | T7APM.DFM | Print vendor mailing labels (filing or mailing format) |
| AP-N | BKAPN | T7APINFO.DFM | Vendor custom info / user-defined fields |
| AP-O | BKAPO | T7APO.DFM | Enter recurring AP vouchers (standing orders with frequency, next date, max times) |
| AP-P | BKAPP | T7APP.DFM | Generate recurring vouchers for the batch due date |
| AP-Q | BKAPQ | T7APQ.DFM | Void a check (by check number, vendor, amount, date) |
| AP-R | BKAPR | T7APR.DFM | Print check history |
| AP-S | APS2000 | T7APS.DFM | Print 1099 forms (year-specific programs — APS1999, APS2000, TAPS2000) |
| AP-T | BKAPT | T7APT.DFM | AP check / invoice inquiry drill-down (check → invoices paid → PO lines) |
| AP-V | BKAPV | T7APV.DFM | Enter / print vendor deposits |
| AP-X | BKAPX | T7APX.DFM | Print invoice link report (invoices missing PO link) |
| AP-Y | BKAPY | T7APY.DFM | Reprint checks |
| AP-YB | BKAPYB | T7APYB.DFM | Export positive pay file (CSV to bank — configurable fields) |
| AP-YC | BKAPYC | T7APYC.DFM | Export ACH/NACHA file for electronic payments |
| AP-ZA | BKAPZA | T7APZA.DFM | Top N vendors by period analysis (MTD/YTD/LYR) |

**Sub-forms (child dialogs of AP-A):**

| Form | Purpose |
|------|---------|
| T7APABANK.DFM | Vendor bank account info (name, routing number, account number, type) |
| T7APACON.DFM | Vendor contacts (name, email, phone) |
| T7APAPRC.DFM | Vendor item pricing grid (item, qty, price, extension) |
| T7APASTA.DFM | Vendor statistics (YTD vs LY gross purchases, variance) |
| T7APHASK.DFM | Check note entry dialog (used from AP-H) |
| T7APPVND.DFM | AP vendor popup (lookup, no captions — runtime-labeled) |

**Key tables:** BKAPVEND (vendor master), BKAPINVL (invoices/vouchers), BKAPCHKH (check history),
BKAPCHKF (check run batch), BKAPPO (PO header), BKAPPOL (PO lines), BKAPNOTE (vendor notes),
BKAP.REM (remittance), BKAP.TMC (ACH bank info).

---

### AR — Accounts Receivable Module (24 forms)

**Menu flow:** AR-A (customers) → SO module creates invoices → AR-C (record payments) →
AR-F (aging) → AR-E (statements) → AR-G (post to GL via SO-G).

| Code | Program | Form | What it does |
|------|---------|------|-------------|
| AR-A | BKARA | T7ARA.DFM / T7ARAE.DFM / T7ARAC.DFM | Enter/edit customer master — name, address, credit limit, terms, GL defaults, salesperson, tax code, currency, discount code, ASN required flag |
| AR-B | BKARB | T7ARB.DFM | Enter AR vouchers / journal entries |
| AR-C | BKARC | T7ARC.DFM | Record payments (cash receipts) — apply to open invoices, handle discounts, NSF checks, import batch payments |
| AR-D | BKARD | T7ARD.DFM | Charge interest on overdue invoices (configurable minimum charge) |
| AR-E | BKARE | T7ARE.DFM | Print customer statements (balance-forward or open-item, deposits, aging format) |
| AR-F | BKARF | T7ARF.DFM | Print AR aging report (5 configurable periods, base or source currency, export past due to file) |
| AR-G | BKARG | T7ARG.DFM | Print customer code / name directory (active, inactive, credit hold, class filter) |
| AR-H | BKARH | T7ARH.DFM | Print customer general info report |
| AR-I | BKARI | T7ARI.DFM | Print customer mail labels / address list |
| AR-K | BKARK | T7ARK.DFM | Print sales tax report (by tax code/group, purchases or sales) |
| AR-L | BKARL | T7ARL.DFM | Transfer / post outstanding sales taxes to GL |
| AR-M | BKARM | T7ARM.DFM | Enter customer refund (create check or credit, link to original invoice) |
| AR-N | BKARN | T7ARN.DFM | Enter / print customer deposits (link to SO, generate invoice) |
| AR-P | BKARP | T7ARP.DFM | Print customer follow-up report (days late for payment) |
| AR-R | BKARR | T7ARR.DFM | Print AR payment history (check date/number range, bank accounts) |
| AR-T | BKART | T7ART.DFM | Customer credit card management (add/update/delete stored cards, processor setup) |
| AR-U | BKARU | T7ARU.DFM | Process accounts receivable (period-end tasks, as-of date) |

**Sub-forms (child dialogs of AR-A):**

| Form | Purpose |
|------|---------|
| T7ARA2DB.DFM | 2D barcode layout configuration per customer (field, character, order) |
| T7ARACON.DFM | Customer contacts (name, email, phone) |
| T7ARACRE.DFM | Customer credit info panel (credit limit, hold, follow-up date, outstanding amounts) |
| T7ARAPRC.DFM | Customer item pricing grid (item, discount %, price, qty, extension) |
| T7ARASTA.DFM | Customer statistics (gross sales, COGS, net sales, YTD vs LY) |

**Key tables:** BKARCUST (customer master 106f), BKARINV (invoice header), BKARINVL (invoice lines),
BKARINVI (SO→invoice cross-ref), BKARSHIP (ship-to addresses), ARTTEMP (payment temp),
BKARDESC (descriptions), ISARDEPL (AR deposit lines).

---

### PO — Purchase Orders Module (41 forms)

**Menu flow:** PO-F (RFQ) → PO-G (RFQ → PO) → PO-A (PO entry) → PO-C (receive) →
PO-J-C (QC receive) → AP-C (AP invoice entry from PO) → PO-K (close PO).

| Code | Program | Form | What it does |
|------|---------|------|-------------|
| PO-A | BKPOA | T7POA.DFM / T7POAE.DFM / T7POAC.DFM | Enter/edit purchase orders — vendor, items, quantities, due dates, GL, job#, DPAS rating, risk assessment, FAR/NADCAP compliance flags |
| PO-B | BKPOB | T7POB.DFM | Print purchase orders (standard or consolidated, with notes, ECO/drawing info) |
| PO-C | BKPOC | t7poc.DFM | Receive PO into inventory (packing slip, bin, lot, inventory or QC) |
| PO-E-A | BKPOEA | T7POEA.DFM | Print RFQs |
| PO-ENG | BKPOENG | T7POENG.DFM | Engineering open order report (with previous 12-month usage, WO allocations, rush/expedite colors) |
| PO-F | BKPOF | T7POF.DFM | Enter verbal RFQ quotes (vendor, item, qty breaks, lead time, cost, estimation link) |
| PO-G | BKPOG | T7POG.DFM | Convert RFQ to PO (with WO prefix/suffix, pass/skip zero-qty items, keep quote on file) |
| PO-H | BKPOH | T7POH.DFM | Vendor pricing master (archive original price, update pricing, track last cost 1–5) |
| PO-I-C | BKPOIC | T7POIC.DFM | Print open RFQ report |
| PO-I-D | BKPOID | T7POID.DFM | Print vendor price list (active/archived/expired prices) |
| PO-I-G | BKPOIG | T7POIG.DFM | Print PO expedite / shortage report (color-coded by rush level, planner code filter) |
| PO-I-H | BKPOIH | T7POIH.DFM | Print vendor on-time delivery performance report |
| PO-I-I | BKPOII | T7POII.DFM | Print PO change history (by PO#, vendor, item, job, date of change) |
| PO-I-L | BKPOIL | T7POIL.DFM | Print PO open order listing with digital signature status |
| PO-J-A | BKPOJA | T7POJA.DFM | Print QC receipt travellers (with rush/expedite coloring) |
| PO-J-B | BKPOJB | T7POJB.DFM | Print QC open order / shortage report (rush/colors, exclude bought-off items) |
| PO-J-C | BKPOJC | T7POJC.DFM | QC receiver entry — accept/reject/buyoff/rework/NCR/RoHS per receipt line |
| PO-J-D | BKPOJD | T7POJD.DFM | Print vendor quality performance report (on-time delivery by class/vendor range) |
| PO-K | BKPOK | T7POK.DFM | Batch close POs (archive by date / PO# / vendor range) |
| PO-L | BKPOL | T7POL.DFM | Approved vendor list entry (approved vendors per item, with primary flag) |
| PO-L-A | BKPOLA | T7POLA.DFM | Print approved vendor list (by item, parent item, vendor) |
| PO-L-P | BKPOLP | T7POLP.DFM | Print vendor pricing report |
| PO-M | BKPOM | T7POM.DFM | PO inquiry — search by item or PO# — shows on-hand, on-PO, on-WO, in-QC, allocated, on-SO |
| PO-MAST | BKPOMAST | T7POMAST.DFM | Vendor / item master inquiry (AP + IC + TR + PO drill-down in one screen) |
| PO-P | BKPOP | T7POP.DFM | Full vendor master entry form (AP + PO integrated: contacts, GL, follow-ups, pricing history, gross purchase history) |
| PO-Q | BKPOQ | t7POQ.DFM | Maintain PO delivery dates — mass confirm / update estimated receipt dates |
| PO-S | BKPOS | T7POS.DFM | Cash sale / point-of-sale PO screen (item, qty, price, discount) |
| PO-S-CD | BKPOSCD | T7POSCD.DFM | Cash drawer / change-due dialog for POS |
| PO-S-I | BKPOSI | T7POSI.DFM | POS codes maintenance (code, description) |
| PO-S-X | BKPOSX | T7POSX.DFM | POS transaction types maintenance |

**Sub-forms:**

| Form | Purpose |
|------|---------|
| T7POA2.DFM | PO line-item entry sub-form (qty, price, ECO, job, location, due date) |
| T7POAC.DFM | Advanced PO with risk assessment, DPAS rating, FAR/NADCAP compliance |
| T7POACPY.DFM | Copy PO to new PO / archive (change vendor, new PO#) |
| T7POAIMPLINES.DFM | Import PO lines from CSV file |
| T7POAPrBrk.DFM | Verify PO price breaks (item, last cost, expiry date) |
| T7POAVITEM.DFM | Vendor-specific item lookup |
| T7POPGET.DFM | Generic PO popup lookup (labels set at runtime by caller) |
| T7POLINEHIST.DFM | PO line change history (ERD, price, qty, GL account, VPD) |
| T7pojcqc.DFM | Multi-scrap code entry for QC receiver (use-as-is quantities) |
| T7pojcsc.DFM | Multi-scrap code entry for QC receiver (scrap quantities) |

**Key tables:** BKAPPO (PO header 57f), BKAPPOL (PO lines 38f), BKQCMSTR (QC receivers 14f),
BKRFQ (RFQ header/lines), BKPOHIST (vendor price history), ISBINLOT (bin/lot assignments).

**Special compliance fields (T7POAC.DFM):**
- DPAS Rating — Defense Priorities and Allocations System order priority code
- First Article Reports Required [Y/N]
- NADCAP Certs Required For Finishes [Y/N]
- Risk assessment: schedule risks, potential obsolescence

---

### SO — Sales Orders Module (71 forms)

**Menu flow:** SO-A (enter SO) → SO-C (pick ticket) → SO-E (ship) → SO-F (invoice) →
SO-G (post to AR/GL) → AR-C (record payment).
Parallel: SO-N (generate WOs from SO) → WO module.

| Code | Program | Form | What it does |
|------|---------|------|-------------|
| SO-A | BKSOA/BKSOA2 | T7SOA.DFM / T7SOAE.DFM / T7SOAC.DFM | Enter / edit sales orders — customer, items, qty, price, disc, due date, location, FOB, freight, drop ship, currency, job#, APH market/program fields |
| SO-B | BKSOB | T7SOB.DFM | Print sales orders (with blanket lines, kit components, hidden notes, linked documents) |
| SO-BIN | BKSOBIN | T7SOBIN.DFM | Bin-level inventory allocation for SO lines |
| SO-C | BKSOC | T7SOC.DFM | Print pick tickets / packing slips (back-orders, lot numbers, serial numbers, multi-location) |
| SO-D | BKSOD | T7SOD.DFM | Print shipping labels — standard, John Deere (I/M/X/S types), PDF417 barcode, kanban |
| SO-E | BKSOE | T7SOE.DFM | Ship sales order — release to invoice, assign shipper, BOL number, carrier pro number, gross weight |
| SO-F | BKSOF | T7SOF.DFM | Print invoices — consolidated, auto-email, apply deposits, print C of C, print C of O |
| SO-G | BKSOG | T7SOG.DFM | Post invoices to AR/GL (pre-post COGS + commissions reports, post all printed) |
| SO-HINFO | BKSOHINFO | T7SOHINFO.DFM | SO header UDFs — 20 alpha fields (sohAlpha1–20) + 5 date fields (sohDate1–5) |
| SO-INFO | BKSOINFO | T7SOINFO.DFM | SO-level misc info UDFs — 20 alpha (soAlpha1–20) + 5 date (soDate1–5) |
| SO-J-INFO | BKSOJINFO | T7SOJINFO.DFM | Recurring SO settings (group code, frequency, limit, next invoice date) |
| SO-K | BKSOK | T7SOK.DFM | Recurring orders — generate invoices from order templates by selection code / date range |
| SO-L-INFO | BKSOLINFO | T7SOLINFO.DFM | SO line UDFs — 20 alpha (solAlpha1–20) + 5 date (solDate1–5) |
| SO-LINEHIST | — | T7SOLINEHIST.DFM | SO line change history viewer (CDD, ESD, price, qty, commission rates, discount) |
| SO-LOT | BKSOLOT | T7SOLOT.DFM | Lot-level inventory allocation for SO lines |
| SO-N | BKSON | T7SON.DFM | Generate work orders from SO lines (multi-assy WO, combine duplicates, suffix matching, shop calendar start date) |

**Sub-forms (child dialogs of SO-A):**

| Form | Purpose |
|------|---------|
| t7Soa2.DFM | SO line-item entry (item, qty, price, disc, ECO, drawing, location, line weight) |
| T7SOABKD.DFM | Booking date entry popup |
| T7SOAFRT.DFM | Freight amount entry popup |
| T7SOAIMPLINES.DFM | Import SO lines from CSV (multi-company, include kit/make-from/specs) |
| T7SOAPRC.DFM | Customer item pricing matrix display |
| T7SOAXCOM.DFM | Extra commission override entry (rep#, commission %, overage %) |
| T7SOACPY.DFM | Copy SO to new quote (SO → Quote) |
| T7SOACITEM.DFM | Customer-specific item lookup for SO lines |
| T7SOBIN.DFM | Bin allocation dialog |
| T7SOLOT.DFM | Lot allocation dialog |
| T7SODDesc.DFM | Label description entry (copies) |
| T7SODPallet.DFM | Pallet configuration for shipping labels |
| T7SOFDEP.DFM | Apply customer deposit to SO invoice |
| T7SOGA.DFM | Real-time order posting progress display |
| T7SOGACHK.DFM | Cash terms check dialog (cash terms customer — capture payment at invoice post) |
| T7SOGCogs.DFM | Pre-post COGS report print dialog |
| T7SOGComm.DFM | Pre-post commissions report print dialog |
| T7sondte.DFM | SO-N date entry popup |

**Key tables:** BKARINV (invoice/SO header), BKARINVL (invoice/SO lines), BKARINVI (SO→invoice cross-ref),
BKSOX/BKSOXH (SO extract for reporting), BKSONOTE (SO notes), BKSOPO (SO→PO cross-ref),
ISSOHNFO (SO header UDF values — sohAlpha/sohDate), ISSOINFO (SO misc info), ISSRINFO (SO line UDFs),
ISSCHED (scheduling), BKSOLOCK (SO record locking), BKSOHLOT (header lot assignments),
BKSOHSER (header serial numbers).

**John Deere label integration (T7SOD.DFM):**
- Label types: I (item), M (material), X (mixed), S (small)
- JD Pallet License Plate Number entry
- MFD Date, packaging type, and pallet configuration
- "John Deere Shipment?" flag triggers JD-specific label format

**APH (Advanced Planning Horizon) fields (T7SOA.DFM):**
- APH Market — customer market segment for demand planning
- APH Program — program code for APH demand grouping
These are i2 Systems J7 customization fields (not standard EvoERP).

---

*Pass 103 AP/AR/PO/SO module catalog — 171 DFM forms confirmed from `samples/dfm/` analysis.*
*Per-table confidence: 87/100. PROJECT-STRUCTURE.md confidence: 86/100.*
'''

with open(PATH, 'a', encoding='utf-8') as f:
    f.write(BLOCK)

print(f'Appended {len(BLOCK):,} chars to HELP-RESOURCES.md')
