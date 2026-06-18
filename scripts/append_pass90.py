import sys
sys.stdout.reconfigure(encoding='utf-8')

path = r'C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\HELP-RESOURCES.md'

block = r'''

---

## Pass 90 — WC, SR, AM, MRP, GF, SM, INA, utility DFMs

### WC Module — Warehouse/Bin Control (additional sub-programs)

| Code | DFM | Purpose |
|------|-----|---------|
| WC-D | T7WCD | Import bin locations — comma/fixed CSV, FIELD.NUMBER[1..8], replace.binloc/replace.binmstr/replace.binmstr flags (skip/replace/ignore) |
| WC-E | T7WCE | Physical count sheet (with cycle codes) — item/type/class/cat ranges, FROM.BIN/THRU.BIN, FROM.CYCLE/THRU.CYCLE, incl.lot/ser, zero-UOH, combine.dupes |
| WC-F | T7WCF | Warehouse bin listing — item/type/class/cat ranges, include extended desc, all warehouses |
| WC-G | T7WCG | Assign bin locations — item/type/class/cat, Location, Bin, make.default (set as default bin) |
| WC-H | T7WCH | Bin inquiry by location — location, BKIC.LOCM.NAME, from.bin/thru.bin |
| WC-BK | T7WCBK | Live Work Center Schedule — FROM.WC, timer (refresh seconds), ISE.STATUS.2/3 (WO status filters), operation, category, customer, WO priority filter |
| WC-LOC-FIX | T7WCLOCFIX | LOC sync utility — updates MTIC.PROD.LOC with default WC bin; ISBIN.LOC.ITEM, default.loc |

### SR Module — Service/Repair (additional sub-programs)

| Code | DFM | Purpose |
|------|-----|---------|
| SR-B | T7SRB | Print SR orders — customer/class/SR/job ranges; PLDTYPE (linked docs), notes/hidden/kit/options/zero-balance/tax/MMS/lot/serial/RMA/original-order options |
| SR-BK | T7SRBK | Live Work Center Schedule for SR — FROM.LOC, timer, ISE.STATUS.2/3/4 (3 WO status filters) |
| SR-D | T7SRD | Print SR packing slips — customer/class/SR/job/date ranges, SHIP.DATE/SHIP.NUM, USE.EXIST.SDT, PRT.NOTRTS (non-released), incl.bo.qty, SORT.TEXT |
| SR-E | T7SRE | Release SR orders — BKAR.INV header: CUSA1/CUSA2[1..2]/CUSCTY/CUSST/CUSZIP/CUSORD/RTS/TAXABL/ORDDTE/NUM/GLDPT/SLSP/LOC/TERMD; line display: BKAR.INVL.ESD/PCODE/PDESC/PQTY/PPRCE/PEXT/TXBLE/UM.LN[2]/COGS/PDISC; auto-release comments/BO/all-lines; use default bins; ask proportional kit release |
| SR-F | T7SRF | Print SR invoices — same as SO-F: MARK.INVOICES, RTYPE, consolidate, distribute.frt, apply deposits (appdep), invoice types (SO/AR-voucher/finance-charge), PRT.ECO/SERIAL/KIT/COMMENT/NOTES/HID.NOTES/OPTIONS, PLDTYPE |
| SR-G | T7SRG | Post SR invoices — invoice/SR number ranges, post.all, prt.comm (commissions report) |
| SR-G-A | T7SRGA | SR posting progress indicator |
| SR-I | T7SRI | SR void invoice list — same structure as SO-R: BKAR.INV.INVDTE/ORDDTE/SHIPDT/CUSCOD/CUSNME/address fields, VOID.DATE, subtotal/tax/freight/deposit/retention/total |
| SR-INFO | T7SRINFO | SR misc info UDFs — ISSR.INFO.DATE1-5 + ISSR.INFO.AL1-20 (5 dates + 20 alpha per SR header); ISSR.INFO.SRNUM |
| SR-S | T7SRS | Work center/data collection sync — DCD.EMP/NAME/WOP/P/ITEM/TIMEIN/RUN (data collection fields) + SHI.ITEM/WOPRE/CUST/P/SDATE/SQTY/DESC (shipping schedule fields) |

### AM Module — Accounting Maintenance (full sub-program suite)

| Code | DFM | Purpose |
|------|-----|---------|
| AM-A | T7AMA | Open period setup — fiscal_d (current fiscal year start), gl_close_d (open period start), future.date (open period end), acct.date (accounting open period start), today_d |
| AM-B | T7AMB | Archive/view GL account history — BKGL.CURRENT[1..14], BKGL.1YPAST[1..14], ISGL.2YPAST through ISGL.6YPAST[1..14] — up to 7 years of 14-period GL data |
| AM-C | T7AMC | GL account maintenance — BKGL.ACCT/GLDPT/ACCTD/TYPE/NON.CASH/inactive, BKGL.BUDGET[1..14], ISGL.CYDATE[1..12] |
| AM-D | T7AMD | Create/delete GL department — template dept, new dept code, gl_type[1..5] (Asset/Liability/Expense/Income/Owner), bdgt_clr (clear budget), del_dpt |
| AM-E | T7AME | Financial statement configuration — BKGL.STC.* (balance sheet sections: GLN=net income/noncash, GLA.F/T[1..4]/GLATTL[1..4]=assets, GLL.F/T[1..4]/GLLTTL[1..4]=liabilities) + BKGL.STI.* (income statement: GLI.F/T/GLIMT=income, COGS, GLDMT=expenses, GLO/GLE=other inc/exp) |
| AM-H | T7AMH | GL account renumbering — import CSV with old/new GL code+dept, field mapping |
| AM-I | T7AMI | Purge/archive GL journals — date range, GL account range, journal type |
| AM-J | T7AMJ | Archive/purge AP data — vendor range, thru date, action [P/A/R] |
| AM-K | T7AMK | Archive/purge AR data — customer range, thru date |
| AM-N | T7AMN | GL fiscal period dates — ISGL.4YDATE[1..12] / ISGL.5YDATE[1..12] / ISGL.6YDATE[1..12] (period start dates for years 4-6 ago); BKSY.FISCAL.YR / NY.FISCAL.YR (current/next fiscal year start) |
| AM-O | T7AMO | Archive/purge PO data — vendor/class range, last activity date, del.orphans [L/H/B/N] |
| AM-P | T7AMP | Archive/purge SO/customer data — customer/class range, last activity date, del.orphans, incl.ship.cust |
| AM-Q | T7AMQ | Copy/create GL budgets — from/thru GL/dept; source: use.yearpast / use.annual / use.curryear / use.annual.ny; factor / factor.ny; shows ISGL.3YPAST through ISGL.6YPAST[1..14] per period |
| AM-S | T7AMS | Archive/purge GL journals (variant) — date range, journal number range, action, journal type range |

### GL Table Structure — Extended (from T7AMB/AMC/AMQ/AMN)

EVO uses **14 GL periods per year** (not 12). The extra 2 periods accommodate adjustment entries.

| Table/Field Pattern | Description |
|--------------------|-------------|
| BKGL.CURRENT[1..14] | Current year monthly/period balances (14 periods) |
| BKGL.1YPAST[1..14] | 1 year ago balances (14 periods) |
| ISGL.2YPAST[1..14] through ISGL.6YPAST[1..14] | 2–6 years ago balances |
| BKGL.BUDGET[1..14] | Budget amounts per period |
| ISGL.CYDATE[1..12] | Period start dates for current year (12 calendar dates) |
| ISGL.4YDATE/5YDATE/6YDATE[1..12] | Period start dates for years 4/5/6 ago |
| BKSY.FISCAL.YR | Current fiscal year start date |
| NY.FISCAL.YR | Next fiscal year start date |
| BKGL.ACCT / GLDPT | GL account code and department |
| BKGL.ACCTD | Account description |
| BKGL.TYPE | Account type (A=Asset, L=Liability, E=Expense, I=Income, O=Owner) |
| BKGL.NON.CASH | Non-cash flag (affects cash flow statement) |
| BKGL.STC.GLN.F/T | Balance sheet: net income GL range start/end |
| BKGL.STC.GLA.F[1..4]/T[1..4]/GLATTL[1..4] | Balance sheet: 4 asset sections (from/thru/title) |
| BKGL.STC.GLL.F[1..4]/T[1..4]/GLLTTL[1..4] | Balance sheet: 4 liability sections |
| BKGL.STI.GLI.F[1..2]/T[1..2] | Income statement: 2 income GL ranges |
| BKGL.STI.MN.TTL | Income statement: main title |

### MR/MRP Module — Material Requirements Planning (full suite)

#### MRP Tables

| Table | Key Fields | Purpose |
|-------|-----------|---------|
| BKMRP.FC | PART, QTY, DATE, CQTY, OQTY, FLAG | MRP demand forecast — item/qty/date, consumed qty, original qty, flag |
| BKMRP.PO | VEND, ERD, QTY, PRICE, CONF, PART, DATE | MRP-generated PO staging — vendor/receipt-date/qty/price/confirmed/part |
| MTMRP | PARTNO, STARTDT, DATE, QTY | MRP calculation results — part, start date, due date, qty required |
| MTIC.PROD.MRP | (flag) | Per-item: include in MRP generation (in MTIC.PROD record) |

#### MRP Sub-Program Summary

| Code | DFM | Purpose |
|------|-----|---------|
| MR-A | T7MRA | Demand forecast entry/view — BKMRP.FC.PART/QTY/DATE/CQTY/OQTY/FLAG |
| MR-ADE | T7MRADE | Import demand forecast — item/date/qty from CSV (comma or fixed) |
| MR-B | T7MRB | Print forecast report — item/type/class/cat/date ranges, print consumed and original qty, current vs archived |
| MR-C | T7MRC | Process forecast — consume/erase/rollover/load-level; item/class/cat/customer/date ranges; archive/restore |
| MR-D | T7MRD | MRP parameters per item — MTIC.PROD.MRP (include), M.EXPBF/DLYBF (expedite/delay buffers), m.sensexp/sensdly (sensitivities), M.LEAD/RLVL/RAMT, m.round; planner.code; master vs specific location |
| MR-E | T7MRE | Print MRP parameters — item/type/class/cat, include.mrp [Y/N], master.loc [M/S] |
| MR-F | T7MRF | **Main MRP generation run** — 4-stage process: (1) BOM analysis, (2) generating requirements, (3-4) consolidating; THRU.DATE (include ESD thru), OPT.TYPES [RFAM], INC.SO, STYPE (S-type WOs), INC.FORECAST, std.pack, RLVL, incl.seg.locs, all.locs, po.lead, calc.usage; processes BKAR.INVL/BKAP.POL/WO.CODE/WOBOM.COMPCODE/BKMRP.FC during run |
| MR-G | T7MRG | MRP action report — item/date/class/cat/planner/vendor/customer ranges; LASTPO (last X POs); BOM components; OD (show original dates); prt.All.Mfg; PLDTYPE (linked docs) |
| MR-H | T7MRH | MRP color-coded action report — ACT.TYPES [MBEDORC]: M=Make/B=Buy/E=Expedite/D=Delay/O=OK/R=Reschedule/C=Cancel; prior.cl/xdays.cl (color bands by urgency); item/class/cat/planner/vendor/customer/WO-date ranges |
| MR-I | T7MRI | Auto-generate WOs from MRP — for location; item/class/cat/planner/WO-date ranges; combine (1 WO per item); wo.class[1..6]; use.std.pack; add.cust.info; review mode |
| MR-IR | T7MRIR | MRP WO review — MTMRP.PARTNO/STARTDT/DATE/QTY |
| MR-IX | T7MRIX | Tool-based WO creation — up to 4 output parts (part[1..4]/desc/mrpqty), qty, woLOC, wostartdate |
| MR-J | T7MRJ | Auto-generate POs from MRP — BKMRP.PO.VEND/ERD/QTY/PRICE/CONF; AutoEmail; REPORT.MODE; INC.SPECS; INCLAPPRMFGRS; pricing [CBM]=contract/base/minimum; spo.num; one.po.per.item |
| MR-JR | T7MRJR | MRP PO review — MTMRP.PARTNO/STARTDT/DATE + PO.DATE/ER.DATE/QTY/vendor/price |
| MR-JX | T7MRJX | MRP PO generation — BKMRP.PO.VEND/ERD/QTY/PRICE/CONF/PART; show blank vendors; BKAP.PO.NUM assigned |
| MR-L | T7MRL | MRP plan lookup — PLND.NUM (1 through LAST.PLND), revrse (reverse lookup) |
| MR-N | T7MRN | Auto-approve POs — from/thru vendor, po.amt (dollar threshold), report.only |
| MR-O | T7MRO | Print MRP change report — items changed since last MR-P |

#### MRP Expedite/Delay Buffer Fields (T7MRD)

Per-item MRP sensitivity settings stored in MTIC.PROD:

| Field | Meaning |
|-------|---------|
| MTIC.PROD.EXPBF | Expedite buffer days |
| MTIC.PROD.DELBF | Delay buffer days |
| m.sensexp | Expedite sensitivity |
| m.sensdly | Delay sensitivity |

### SM Module — System Maintenance (additional sub-programs)

#### SM-C Item Class GL Mapping (T7SMC)

Per item-class + location, maps up to 10 GL accounts (account + department each):

| Field | GL Purpose |
|-------|-----------|
| edit.gla/dpta | Inventory Asset/Expense |
| edit.glc/dptc | COGS |
| edit.gls/dpts | Taxable Sales |
| edit.glsnt/dptnt | Non-Taxable Sales |
| edit.glw/dptw | WIP Inventory Asset |
| edit.gllab/dptlab | Absorbed Labor |
| edit.glfoh/dptfoh | Absorbed Fixed Overhead |
| edit.glvoh/dptvoh | Absorbed Variable Overhead |
| edit.glmisc/dptmisc | Material Burden |

Plus system-wide defaults (sysgla_/sysgld_ for each GL type).

#### SM-D Payment Terms (T7SMD) — IS.TERMS Table

| Field | Meaning |
|-------|---------|
| IS.TERMS.NUM | Terms number (key) |
| IS.TERMS.NAME | Short name |
| IS.TERMS.DESC | Description |
| IS.TERMS.AMT | Discount amount |
| IS.TERMS.TYP | Discount type [%,$,D,C,A,P,F] |
| IS.TERMS.DAY | Discount days |
| IS.TERMS.MAX | Max days till due |
| due.on.rcpt | Due on receipt flag |
| epay | E-pay only flag |

#### SM-E Tax Code Maintenance (T7SME) — ISIS.TXF Table (Full Schema)

| Field | Meaning |
|-------|---------|
| ISIS.TXF.CODE | Tax code (key) |
| ISIS.TXF.DESC | Description |
| ISIS.TXF.IDNUM | Tax ID number |
| ISIS.TXF.VNDCD | Vendor code (remit to) |
| ISIS.TXF.SOPERC[1] | SO tax rate % |
| ISIS.TXF.POPERC[1] | PO tax rate % |
| ISIS.TXF.GLASO / GLDSO | GL account/dept for SO tax |
| ISIS.TXF.GLAPO / GLDPO | GL account/dept for PO tax |
| ISIS.TXF.SOMAX | SO max tax amount |

#### SM-G Employee Report (T7SMG) — BKPR.EMP Table

| Field | Meaning |
|-------|---------|
| BKPR.EMP.FNMI | First name/middle initial |
| BKPR.EMP.LNME | Last name |
| BKPR.EMP.ADD | Address |
| BKPR.EMP.CSZ | City/state/zip |
| BKPR.EMP.PHONE | Phone |
| BKPR.EMP.EMAIL | Email |
| BKPR.EMP.SDATE | Start date |
| BKPR.EMP.DEPT | Department/division |
| BKPR.EMP.SHIFT | Shift number |
| BKPR.EMP.TERM | Terminated flag |
| BKPR.EMP.PAYAMT[1] | Regular pay rate |
| BKPR.EMP.PAYAMT[2] | Overtime pay rate |
| BKPR.EMP.PAYAMT[4] | Holiday pay rate |
| BKPR.EMP.OPNAME[5] | User name (login) |
| mobile.phone | Mobile phone |
| ud.alpha1/ud.label1 | User-defined field 1 |

#### SM Code Tables Confirmed (T7SMIA/B/C/D/E/F)

| Table | Key Fields | Purpose |
|-------|-----------|---------|
| BKCM.LEAD | SCODE, DESC | Lead source codes |
| BKCM.TERR | TCODE, DESC, EMAIL | Territory codes |
| BKCM.ACFC | FCODE, DESC, REP | CRM follow-up/history codes (REP = include in CRM dashboard) |
| BKCM.ACCC | CCODE, DESC | Activity/category/brand/stock codes (reused across modules) |
| BKCM.DTCD | DCODE, DESC | Document type codes |
| IS.CATM | CODE, DESC | Item category master |

#### SM-J Maintenance Utilities

| Code | DFM | Purpose |
|------|-----|---------|
| SM-JA | T7SMJA | Generic batch utility (report-only mode) |
| SM-JB | T7SMJB | Archive/purge WOs — WO/fin-date/job/customer/item ranges; closed/cancelled flags; orphan ISWOEX/ISWOROEX check |
| SM-JC | T7SMJC | Inventory reconciliation — master level, transaction level, report stock status changes (RSS), METHOD, item/class/date; checks MTICMSTR records |
| SM-JD | T7SMJD | Archive/consolidate inventory transactions — type [ASPJWIQOCMTRG], consolidation date |
| SM-JE | T7SMJE | Purge WOs — from/thru WO/fin-date, PURGE.CLOSE/CANCEL |
| SM-JF | T7SMJF | Archive/purge POs — PO/vendor/date ranges |
| SM-JG | T7SMJG | Archive/purge QC receivers — QC receiver/vendor/date ranges |
| SM-JH | T7SMJH | Purge data collection records — CUT.DATE |

### T7INA — Item Master Main Form

Full item master fields from T7INA.DFM (the primary item entry screen):

| Field | Meaning |
|-------|---------|
| BKIC.PROD.LONGP | Long part number |
| BKIC.PROD.DESC / NOTE | Description / note |
| BKIC.PROD.CLASS | Item class |
| MTCLASS.M.DESC | Class description |
| BKIC.PROD.CAT | Category |
| MTIC.PROD.SUBST[1] | Superseded by (substitute part) |
| BKIC.PROD.TYPE | Item type [RFAMNLBTKO] |
| MTIC.PROD.ACTIV | Active status |
| BKIC.PROD.TXBLE / TAXIN | Taxable / tax-inclusive flags |
| BKIC.PROD.UM | Stock unit of measure |
| MTIC.PROD.SUM / PUM | Stock UM / purchase UM |
| BKIC.IS.DCODE | Duty code |
| BKIC.PROD.RLVL / RAMT | Reorder level / reorder amount |
| MTIC.PROD.PCONV | PO conversion multiplier |
| MTIC.PROD.LEAD | Lead time (days) |
| calc.wt | Weight |
| MTIC.PROD.CUBFT | Cubic feet (foot factor) |
| MTIC.PROD.STDPK | Standard pack |
| MTIC.PROD.FRT% | Freight percentage |
| BIN.LOCATION | Default bin location |
| MTIC.PROD.REV | Revision level |
| BKIC.PROD.ISUPC | UPC code |
| MTIC.PROD.WIPDP | WIP display flag |
| MTIC.PROD.EXPBF / DELBF | Expedite/delay buffer days (also used by MRP) |
| BKIC.PROD.PRICE | Base selling price |
| MTIC.PROD.DRAW | Drawing number |
| IS.PROD.GDATES[1] | Good (effective) date |
| MTIC.PROD.ABC | ABC class |
| MTIC.PROD.SER / LOT | Serial/lot control flags |
| WH.CONTROL | Warehouse control flag |
| MTIC.PROD.OPTCS | Options/configuration flag |
| cycle.code | Cycle count code |

### Business Status Dashboard (T7BS) — ISBSF Table

| Field | Module | Meaning |
|-------|--------|---------|
| ISBSF.AR.BAL | AR | Current AR balance |
| ISBSF.AR.BILL | AR | Billings for period |
| ISBSF.AR.RECP | AR | Receipts for period |
| ISBSF.AR.DISC | AR | Discounts |
| ISBSF.AR.COGS | AR | Cost of goods sold |
| ISBSF.AR.DEPO | AR | Deposits |
| ISBSF.AP.BAL | AP | Current AP balance |
| ISBSF.AP.PAYA | AP | Payables for period |
| ISBSF.AP.PAYM | AP | Payments made |
| ISBSF.AP.DISC | AP | Discounts taken |
| ISBSF.AP.ATP | AP | Approved to pay |
| ISBSF.SO.OPEN | SO | Open orders value |
| ISBSF.SO.BOOK | SO | Booked orders value |
| ISBSF.SO.SHIP | SO | Shipments value |
| ISBSF.PO.OPEN | PO | Open POs value |
| ISBSF.PO.BOOK | PO | Booked POs value |
| ISBSF.PO.RECP | PO | Receipts value |
| ISBSF.WO.WIPBAL | WO | WIP balance |
| ISBSF.WO.ISSU | WO | Issues to WO |
| ISBSF.WO.FPVAR | WO | Finished product / variances |
| ISBSF.IC.VALUE | IN | Inventory value |
| ISBSF.CASH.TOTA | GL | Cash balance total |

### Bill of Lading (T7BOL / T7BOLMSO)

T7BOL fields: auth/control/load/seal/trailer numbers; pickup.date/time, driver.arrived, loading.start/end, driver.departed; HANDLING UNIT: edit.htype/hqty/HM; PACKAGE: edit.ptype/pqty/nmfc/class; pallet.wt; commodity; department.

T7BOLMSO (multi-SO BOL): billing.line[1..6], LIST.SONUM/ITEM/DESC/PQTY/PACKS/PACKTYPE/WEIGHT/HM/NMFC/CLASS, SCAC (carrier code), carrier.name, billing.type [PCTN], billing.acct, marks[1..2].

### Miscellaneous Tables Confirmed in Pass 90

| Table | Key Fields | Purpose |
|-------|-----------|---------|
| BKSB.PART | PROD, SUBST, SUB.DESC | Alternate/substitute parts cross-reference |
| IS.ACTION | TYPE, DESC | Action type codes (generic) |
| AC.RD | TYPE, REASON, DISPO | Corrective action document types + reason + disposition |
| WODATE | START, FINISH, QTY, PARPRE/PARSUF, TOPPRE/TOPSUF, DELPRE/DELSUF | WO date schedule with parent/top/deleted WO linkage |
| IS.SERC | ITEM, SPOS, total, NUMBER, LAST, leng | Item number auto-numbering template |
| IS.STYPE | TYPE | Service/sales type codes |
| IS.CATM | CODE, DESC | Item category master |
| ISBSF | (see above) | Business Status summary (rebuilt by T7BSR) |
| ISTS.CFG | woadsc, wobs, womakf, wocalc, burdn, burdi, woopen, wopswd, woonly, wogdsc, woaloc, WOBWO1, LIMSCT, RRFPR, cmploc, dcseq, scrcmp, wodso, fpser#, sccomf, wipv, divohd | System configuration flags (WO behavior, labor, overhead, MRP) |
| BKYS.YN[1..n] | — | System yes/no configuration flags (indexed array) |
| BKYS.NUM[1..n] | — | System numeric configuration values (indexed array) |
| IS.GF.DEPT | (code, desc) | Golding Farms custom department codes |
| IS.GF.DIV | (code, desc) | Golding Farms custom division codes |

### Master Default Settings Key — ISTS.CFG Fields

From T7MDEFAULTS.DFM, the most important configuration flags:

| Field | Default Setting Controls |
|-------|------------------------|
| ISTS.CFG.WOADSC | Prevent editing of description in WO-A |
| ISTS.CFG.WOBS | WO types that affect Business Status |
| ISTS.CFG.WOMAKF | View only in Enter Finished Product? |
| ISTS.CFG.WOCALC | Calculate labor from BOM |
| ISTS.CFG.BURDN | Use material burden |
| ISTS.CFG.BURDI | Burden item number |
| ISTS.CFG.WOOPEN | Show open or open/closed WOs in WO-A (O/B) |
| ISTS.CFG.WOPSWD | Password for reopening closed/cancelled WOs |
| ISTS.CFG.WOONLY | WO-B: limit to 1 WO (Y/N/W) |
| ISTS.CFG.WOGDSC | Allow edit of component description in WO-G |
| ISTS.CFG.WOALOC | WO default location |
| ISTS.CFG.WOBWO1 | WO-B: limit to 1 WO (flag) |
| ISTS.CFG.LIMSCT | WO-K-M: limit scrap type to (FMLV) |
| ISTS.CFG.RRFPR | WO-K-M: require reason code for scrap |
| ISTS.CFG.CMPLOC | WO default location |
| ISTS.CFG.DCSEQ | Backflush by sequence in Enter Labor (Y/N/B) |
| ISTS.CFG.SCRCMP | Include FP scrap in COGS parts (Y/N/A) |
| ISTS.CFG.WIPV | Use projected or estimate $ and hrs (P/E) |
| ISTS.CFG.DIVOHD | Divide setup by number of jobs worked |

Key BKYS.YN flags (selected):
- BKYS.YN[1]: WO status code default
- BKYS.YN[2]: View only in WO Bills Mat
- BKYS.YN[3]: Close WO in Enter Finished Prod
- BKYS.YN[15]: Use standard cost in Enter Finished Prod
- BKYS.YN[19]: Labor prompt in kit issues
- BKYS.YN[20]: Post overhead as % of labor
- BKYS.YN[21]: Backflush in Enter Finished Prod [Y/N/A/B]
- BKYS.YN[22]: Use actual costs in labor entry
- BKYS.YN[65]: Divide labor cost by # jobs worked

### Kit Issue Form (T7KIT)

Fields revealed: WOBOM.REFERENCE, MTIC.PROD.CYCLE (cycle code), scan.item/scan.wo/scan.emp; per BOM line: APART/ADESC/ARQTY (required qty)/AUOH (UOH)/ALUOH (location UOH)/AQTY (issue qty)/ABIN/ABOMNOTE/ALOT/ALOC/AOPER. Multi-yield WOs: M.PART/DESC/QTY/PER/BIN, proportion [W=weight/F=foot factor/E=equal].

### Put-Away Form (T7PUTAWAY)

BKIC.PROD.LRCPT (last receipt date), scan.item, enterbin, PABBL (put away by bin loc), MTIC.PROD.UIQC (in QC inspection), action (put-away or label).
'''

with open(path, 'a', encoding='utf-8') as f:
    f.write(block)

print('Pass 90 block appended to HELP-RESOURCES.md')
