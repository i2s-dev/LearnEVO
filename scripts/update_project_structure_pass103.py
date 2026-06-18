"""
Pass 103 — Update PROJECT-STRUCTURE.md with complete AP/AR/PO/SO DFM mappings.
Adds missing AP-C..ZA, AR-F..U, all 41 PO, and SO-B..K entries.
Also adds a PO module section between AR and IN.
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

PATH = r'C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\PROJECT-STRUCTURE.md'

with open(PATH, encoding='utf-8') as f:
    content = f.read()

# ────────────────────────────────────────────────────────────────────────────────
# 1. Expand AP table (replace the old 6-row table with the complete 25-row table)
# ────────────────────────────────────────────────────────────────────────────────
OLD_AP = """| Menu | Program | DFM Forms | Description |
|------|---------|-----------|-------------|
| AP-A | BKAPA | T7APA.DFM, T7APABANK.DFM, T7APACON.DFM, T7APAPRC.DFM, T7APASTA.DFM, t7apaC.DFM, t7apae.DFM | Enter Vendors |
| AP-B | BKAPB, T6APB | T7APB.DFM + sub-forms | Enter Vouchers |
| AP-E | BKAPE, t6ape | T7APE.DFM | Print Vouchers Due |
| AP-H | BKAPH (laser: BKAPHA) | T7APH.DFM | Print Checks |
| AP-P | BKAPP | T7APP.DFM | Generate Recurring Vouchers |
| AP-S | APS1999, APS2000, TAPS2000 | T7APS.DFM | 1099 Forms (year-specific programs) |"""

NEW_AP = """| Menu | Program | Key DFM(s) | Description |
|------|---------|-----------|-------------|
| AP-A | BKAPA | T7APA.DFM / t7apaC.DFM / t7apae.DFM + T7APABANK.DFM, T7APACON.DFM, T7APAPRC.DFM, T7APASTA.DFM | Enter/edit AP vendor master |
| AP-B | BKAPB, T6APB | T7APB.DFM | Enter recurring/scheduled vouchers |
| AP-C | BKAPC | T7APC.DFM | Enter AP Invoice (PO receipt → voucher) |
| AP-D | BKAPD | T7APD.DFM | Enter scheduled payment dates |
| AP-E | BKAPE, t6ape | T7APE.DFM | Print cash requirements / vouchers due report |
| AP-F | BKAPF | t7apf.dfm | Select items to pay (open AP browser) |
| AP-G | BKAPG | t7apg.dfm | Print proforma check register |
| AP-H | BKAPH (laser: BKAPHA) | T7APH.DFM | Print checks (ACH, ePay, paper) |
| AP-I | BKAPI | T7API.DFM | Print AP aging / A/P listing |
| AP-J | BKAPJ | T7APJ.DFM | Print vendor directory |
| AP-K | BKAPK | T7APK.DFM | Print vendor labels (multi-col) |
| AP-L | BKAPL | t7apl.DFM | Recalculate MTD and YTD vendor totals |
| AP-M | BKAPM | T7APM.DFM | Print vendor mailing labels |
| AP-N | BKAPN | T7APINFO.DFM | Vendor custom info / UDF entry |
| AP-O | BKAPO | T7APO.DFM | Enter recurring AP vouchers (standing orders) |
| AP-P | BKAPP | T7APP.DFM | Generate recurring vouchers |
| AP-Q | BKAPQ | T7APQ.DFM | Void a check |
| AP-R | BKAPR | T7APR.DFM | Print check history |
| AP-S | APS1999, APS2000, TAPS2000 | T7APS.DFM | 1099 forms (year-specific programs) |
| AP-T | BKAPT | T7APT.DFM | AP check / invoice inquiry drill-down |
| AP-V | BKAPV | T7APV.DFM | Enter and print vendor deposits |
| AP-X | BKAPX | T7APX.DFM | Print invoice link report |
| AP-Y | BKAPY | T7APY.DFM | Reprint checks |
| AP-YB | BKAPYB | T7APYB.DFM | Export positive pay (CSV) to bank |
| AP-YC | BKAPYC | T7APYC.DFM | Export ACH / NACHA file |
| AP-ZA | BKAPZA | T7APZA.DFM | Top N vendors by period analysis |"""

if OLD_AP in content:
    content = content.replace(OLD_AP, NEW_AP, 1)
    print('OK: AP table expanded')
else:
    print('NOT FOUND: AP table')

# ────────────────────────────────────────────────────────────────────────────────
# 2. Expand AR table
# ────────────────────────────────────────────────────────────────────────────────
OLD_AR = """| Menu | Program | Key DFM | Description |
|------|---------|---------|-------------|
| AR-A | BKARA | T7ARA.DFM + sub-forms | Enter Customers |
| AR-B | BKARB | T7ARB.DFM | Enter Vouchers |
| AR-C | BKARC | T7ARC.DFM | Record Payments |
| AR-D | BKARD | T7ARD.DFM | Charge Interest |
| AR-E | BKARE | T7ARE.DFM | Print Statements |"""

NEW_AR = """| Menu | Program | Key DFM | Description |
|------|---------|---------|-------------|
| AR-A | BKARA | T7ARA.DFM / T7ARAE.DFM / T7ARAC.DFM + T7ARACON.DFM, T7ARACRE.DFM, T7ARAPRC.DFM, T7ARASTA.DFM, T7ARA2DB.DFM | Enter/edit AR customer master |
| AR-B | BKARB | T7ARB.DFM | Enter vouchers / AR journal entries |
| AR-C | BKARC | T7ARC.DFM | Record payments (cash receipts) |
| AR-D | BKARD | T7ARD.DFM | Charge interest on overdue invoices |
| AR-E | BKARE | T7ARE.DFM | Print statements |
| AR-F | BKARF | T7ARF.DFM | Print AR aging report |
| AR-G | BKARG | T7ARG.DFM | Print customer code / name directory |
| AR-H | BKARH | T7ARH.DFM | Print customer general info report |
| AR-I | BKARI | T7ARI.DFM | Print customer mail labels |
| AR-K | BKARK | T7ARK.DFM | Print sales tax report |
| AR-L | BKARL | T7ARL.DFM | Transfer / post sales taxes |
| AR-M | BKARM | T7ARM.DFM | Enter customer refund |
| AR-N | BKARN | T7ARN.DFM | Enter / print customer deposits |
| AR-P | BKARP | T7ARP.DFM | Print customer follow-up report (aging + activity) |
| AR-R | BKARR | T7ARR.DFM | Print AR payment history |
| AR-T | BKART | T7ART.DFM | Customer credit card management |
| AR-U | BKARU | T7ARU.DFM | Process accounts receivable (period-close tasks) |"""

if OLD_AR in content:
    content = content.replace(OLD_AR, NEW_AR, 1)
    print('OK: AR table expanded')
else:
    print('NOT FOUND: AR table')

# ────────────────────────────────────────────────────────────────────────────────
# 3. Insert PO module section between "---\n\n### IN" and the IN section
# ────────────────────────────────────────────────────────────────────────────────
PO_SECTION = """---

### PO — Purchase Orders

**Program → Forms mapping (confirmed from DFM analysis, Pass 103):**

| Menu | Program | Key DFM | Description |
|------|---------|---------|-------------|
| PO-A | BKPOA | T7POA.DFM / T7POAE.DFM / T7POAC.DFM + T7POA2.DFM, T7POACPY.DFM, T7POAIMPLINES.DFM, T7POAPrBrk.DFM, T7POAVITEM.DFM | Enter / edit purchase orders |
| PO-B | BKPOB | T7POB.DFM | Print purchase orders |
| PO-C | BKPOC | t7poc.DFM | Receive PO (receive inventory against PO) |
| PO-E-A | BKPOEA | T7POEA.DFM | Print RFQs |
| PO-ENG | BKPOENG | T7POENG.DFM | Engineering open order / PO analysis report |
| PO-F | BKPOF | T7POF.DFM | Enter verbal RFQs / vendor quotes |
| PO-G | BKPOG | T7POG.DFM | Convert RFQ to PO |
| PO-H | BKPOH | T7POH.DFM | Vendor pricing master (approved price list per item) |
| PO-I-C | BKPOIC | T7POIC.DFM | Print open RFQ report |
| PO-I-D | BKPOID | T7POID.DFM | Print vendor price list |
| PO-I-G | BKPOIG | T7POIG.DFM | Print PO expedite / shortage report (color-coded) |
| PO-I-H | BKPOIH | T7POIH.DFM | Print vendor on-time delivery report |
| PO-I-I | BKPOII | T7POII.DFM | Print PO change history report |
| PO-I-L | BKPOIL | T7POIL.DFM | Print PO open order listing with digital signature status |
| PO-J-A | BKPOJA | T7POJA.DFM | Print receipt travellers (QC traveller labels) |
| PO-J-B | BKPOJB | T7POJB.DFM | Print QC open order / shortage report |
| PO-J-C | BKPOJC | T7POJC.DFM | QC receiver entry (accept/reject/buyoff/RoHS) |
| PO-J-D | BKPOJD | T7POJD.DFM | Print vendor quality performance report |
| PO-K | BKPOK | T7POK.DFM | Close PO (batch archive closed purchase orders) |
| PO-L | BKPOL | T7POL.DFM | Approved vendor list entry (per item) |
| PO-L-A | BKPOLA | T7POLA.DFM | Print approved vendor list |
| PO-L-P | BKPOLP | T7POLP.DFM | Print vendor pricing report |
| PO-M | BKPOM | T7POM.DFM | PO inquiry (by item or PO number) |
| PO-MAST | BKPOMAST | T7POMAST.DFM | Vendor / item master inquiry (AP+IC+TR+PO drill-down) |
| PO-P | BKPOP | T7POP.DFM | Full vendor master entry (AP+PO integrated view) |
| PO-Q | BKPOQ | t7POQ.DFM | Maintain PO delivery dates (mass confirm lines) |
| PO-S | BKPOS | T7POS.DFM | Cash sale / point-of-sale PO screen |
| PO-S-CD | BKPOSCD | T7POSCD.DFM | Cash sale — cash drawer / change-due dialog |
| PO-S-I | BKPOSI | T7POSI.DFM | POS codes maintenance |
| PO-S-X | BKPOSX | T7POSX.DFM | POS transaction types maintenance |

**Sub-dialogs and lookup forms:**

| DFM | Purpose |
|-----|---------|
| T7POPGET.DFM | Generic PO popup lookup (labels set at runtime by caller) |
| T7POLINEHIST.DFM | PO line change history viewer (ERD, price, qty, GL account) |
| T7pojcqc.DFM | QC multi-scrap code entry (use-as-is quantities) |
| T7pojcsc.DFM | QC multi-scrap code entry (scrap quantities) |

**Database tables (BKAP\* PO side + receiver tables):**

| Table | File | Purpose |
|-------|------|---------|
| BKAPPO | BKAPPO.B | PO header (vendor, date, terms, totals, status, DPAS rating) |
| BKAPPOL | BKAPPOL.B | PO lines (item, qty, price, due date, job#, GL account, WO link) |
| BKQCMSTR | BKQCMSTR.B | QC receiver records (14 fields: PO#, packing slip, qty received/rejected/accepted) |
| BKRFQ | BKRFQ.B | RFQ (Request for Quote) header and lines |
| BKPOHIST | BKPOHIST.B | PO receipt history / vendor price history |

"""

OLD_IN_HEADER = "---\n\n### IN — Inventory"
if OLD_IN_HEADER in content:
    content = content.replace(OLD_IN_HEADER, PO_SECTION + "---\n\n### IN — Inventory", 1)
    print('OK: PO section inserted')
else:
    print('NOT FOUND: IN section header for PO insertion')

# ────────────────────────────────────────────────────────────────────────────────
# 4. Expand SO table
# ────────────────────────────────────────────────────────────────────────────────
OLD_SO = """| Menu | Program | Key DFM | Description |
|------|---------|---------|-------------|
| SO-A | BKSOA, BKSOA2, ISSRA, ISTECH, JKSOS1S | T7SOABKD.DFM, T7SOAC.DFM (+ 9 sub-forms) | View/Enter Sales Orders |"""

NEW_SO = """| Menu | Program | Key DFM | Description |
|------|---------|---------|-------------|
| SO-A | BKSOA, BKSOA2, ISSRA, ISTECH, JKSOS1S | T7SOA.DFM / T7SOAE.DFM / T7SOAC.DFM / t7Soa2.DFM + T7SOABKD.DFM, T7SOAFRT.DFM, T7SOAIMPLINES.DFM, T7SOAPRC.DFM, T7SOAXCOM.DFM, T7SOACPY.DFM, T7SOACITEM.DFM | View/enter sales orders (multiple form variants) |
| SO-B | BKSOB | T7SOB.DFM | Print sales orders |
| SO-BIN | BKSOBIN | T7SOBIN.DFM | Bin-level allocation for SO lines |
| SO-C | BKSOC | T7SOC.DFM | Print pick tickets / packing slips |
| SO-D | BKSOD | T7SOD.DFM | Print shipping labels (incl. John Deere, PDF417 barcode, kanban) |
| SO-E | BKSOE | T7SOE.DFM | Ship sales orders (create shipper / release to invoice) |
| SO-F | BKSOF | T7SOF.DFM | Print invoices (AR-F equivalent for SO invoices) |
| SO-F-DEP | BKSOFDEP | T7SOFDEP.DFM | Apply customer deposit to SO invoice |
| SO-G | BKSOG | T7SOG.DFM | Post invoices (SO-G COGS posting) |
| SO-G-A | BKSOGA | T7SOGA.DFM | Real-time order-posting progress display |
| SO-G-CHK | BKSOGACHK | T7SOGACHK.DFM | Cash terms / payment check at invoice post |
| SO-G-COGS | BKSOGCOGS | T7SOGCogs.DFM | Pre-post COGS report |
| SO-G-COMM | BKSOGCOMM | T7SOGComm.DFM | Pre-post commissions report |
| SO-HINFO | BKSOHINFO | T7SOHINFO.DFM | SO header-level UDFs (20 alpha + 5 date fields) |
| SO-INFO | BKSOINFO | T7SOINFO.DFM | SO line-level UDFs (20 alpha + 5 date fields) |
| SO-J-INFO | BKSOJINFO | T7SOJINFO.DFM | Recurring SO settings (group, frequency, limit, next date) |
| SO-K | BKSOK | T7SOK.DFM | Recurring orders — generate invoices from templates |
| SO-L-INFO | BKSOLINFO | T7SOLINFO.DFM | SO line misc. info UDFs (20 alpha + 5 date fields) |
| SO-LINEHIST | BKSOLINEHIST | T7SOLINEHIST.DFM | SO line change history viewer (price, qty, CDD, ESD, discounts) |
| SO-LOT | BKSOLOT | T7SOLOT.DFM | Lot-level allocation for SO lines |
| SO-N | BKSON | T7SON.DFM | Generate work orders from SO (SO → WO batch conversion) |"""

if OLD_SO in content:
    content = content.replace(OLD_SO, NEW_SO, 1)
    print('OK: SO table expanded')
else:
    print('NOT FOUND: SO table')

with open(PATH, 'w', encoding='utf-8') as f:
    f.write(content)

print(f'\nDone. File size: {len(content):,} chars')
