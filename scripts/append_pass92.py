import sys
sys.stdout.reconfigure(encoding='utf-8')

path = r'C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\HELP-RESOURCES.md'

block = r'''

---

## Pass 92 — ES/JC/QC/CS/CC/DE/PS/FA/IM/LC/AC deep-DFM pass (2026-06-18)

### IS.EST — Estimating Table Structure (10-Quantity-Level × Cost Elements)

Confirmed from T7EST.DFM (ES-A main form). Each estimate stores up to 10 quantity levels, and for each level, 16 cost elements:

| Field Pattern | Element |
|---------------|---------|
| IS.EST.QTY[n] | Quantity for level n |
| IS.EST.MAT[n] | Material cost |
| IS.EST.MATMU[n] | Material markup |
| IS.EST.SETUP[n] | Setup cost |
| IS.EST.LAB[n] | Labor cost |
| IS.EST.LABMU[n] | Labor markup |
| IS.EST.OP[n] | Outside process cost |
| IS.EST.OPMU[n] | Outside process markup |
| IS.EST.OH[n] | Overhead cost |
| IS.EST.OHMU[n] | Overhead markup |
| IS.EST.cost[n] | Running total cost |
| IS.EST.MISC[n] | Misc costs |
| IS.EST.EXTRA[n] | Extra charges |
| IS.EST.TOTAL[n] | Total cost |
| IS.EST.PRICE[n] | Selling price |
| IS.EST.OVALL[n] | Overall margin |

**Header fields:** IS.EST.NUM (PK), IS.EST.STATUS, IS.EST.EXPDTE, IS.EST.LOSTDTE (lost date for closed quotes), IS.EST.QTREV (quote revision), IS.EST.OPPTYPE (opportunity type), IS.EST.DRAW (drawing), IS.EST.ORDDESC.

**Margin % fields:** IS.EST.MATMU%, IS.EST.LABMU%, IS.EST.OPMU%, IS.EST.OHMU%, IS.EST.OVLMU% — global margin settings for the estimate.

**ES-E Convert Estimates (T7ESE):** Converts estimate to WO/SO/production. Fields: SO.NUM, sWO.NUM, sFROM.QUOTE, CUST.PO, LOCATION, START.DATE, FINISH.DATE, ESD.DATE, SELL.PRICE, ORD.QTY, ISUPD.CONTRACT (update contract price file), ISTO.WO/ISTO.SO/ISTO.PROD (conversion targets), UCP (update contract price).

---

### JC Engine — Full Parameter Inventory (T7JCENG)

The JC Engine is the central batch processor for all job costing reports. Complete parameter set:

**WO Status flags (individually toggleable):**
- Firmed, Released, Closed, Cancelled, Indirect, Active, Archived

**WO Source (two toggles):** Indirect, Active

**Labor Type (6 types, individually toggleable):**
Regular, Overtime, Doubletime, Sick, Vacation, Holiday

**Shift (3 toggles):** Shift 1, Shift 2, Shift 3

**Range filters:** WO number, work center, item number, tool, employee, machine, labor date, job number, sequence number, scrap code, QC code, rework code, department code, WO actual finish date.

**Output controls:** Report Type, Sort/Subtotal By, Level of Detail, divide hrs by number of jobs (div.hrs), include run/setup/both (RSB), print report filters, estcst.once (one-time setup cost flag).

**JC-N Percent Complete methods (ISCALC.HOW.*):**
- ISCALC.HOW.C — calculate on costs
- ISCALC.HOW.H — calculate on hours to date
- ISCALC.HOW.P — calculate on parts

**JC-M WIP Analysis special options:** asof.date (as-of prior date), sstart.date (estimated start date), txn.date (last transaction date mode), moldy.wos (print dormant WOs), alt.summary, prt.details, inc.labor/inc.mat, prt.last.txn.

**T7JCRM — Remote Database Settings:** Host, port, name, TREEDEST. JC reports can publish to a remote database (appears to be tree-format output — possibly a business intelligence/dashboard endpoint).

---

### CS — Commission Data Array Structure

T7CSB.DFM confirms 10-month rolling data per salesperson (not just YTD):

| Field | Period N Meaning |
|-------|-----------------|
| BKPR.SLS.PAID[1..10] | Commission paid per month (months 1-10 + current period) |
| BKPR.SLS.COMM[1..10] | Commission due per month |
| BKPR.SLS.RCPTS[1..10] | Receipts per month |
| BKPR.SLS.COGS[1..10] | COGS per month |
| BKPR.SLS.GROSS[1..10] | Gross profit per month |

T7CSA confirms: BKPR.AGNT.CODE (outside agent links to AP vendor), BKPR.SLS.CLASS[1] (commission class), BKPR.SLS.EXPACT/EXPDPT (GL account + dept for expense posting).

T7CSD commission transfer: BKPR.COMM.PAYDT (payment date), fISREP.LNK.REPN / tISREP.LNK.REPN (from-rep/to-rep in ISREPLNK table). Posting.date for GL entry.

T7CSO advanced commission — 3 color-coded classes with configurable class codes. Two print modes: Classic (transfer date range, open/transferred) vs. Detail (commission date range, base/source currency, invoice/rep).

---

### CC — Credit Card Tables Fully Confirmed

T7CCP.DFM confirms complete IS.CC table fields:

| Field | Description |
|-------|-------------|
| IS.CC.MASKED | Masked card number (last 4 shown) |
| IS.CC.ZIP | Billing ZIP code |
| IS.CC.CARDNAME | Name on card |
| IS.CC.EXP | Expiry (MMYY) |
| IS.CC.CARDTYPE | Card type (Visa, MC, etc.) |
| is.cc.process | Processor code (e.g., AUTHORIZE) |
| is.cc.address | Billing address |
| ccamount | Transaction amount |

T7CCPO (PO credit card charges): ccnum, ccamount, cczip, CCYY, CCMM, CCADDRESS, CCCVV — raw card entry for PO payments (not vaulted).

T7CCDE import: FIELD.NUMBER2[1..8] and FIELD.NUMBER[1..8] — column positions for: customer code, CC number, expiry date, sort, card type, name on card, ZIP, address. Supports fixed-length or comma-delimited.

T7CCCITM / T7CCCWOT: cycle count entry forms for CC module (CC-C by item and by WO+location).

---

### DE / EDI — Additional Findings

**ISAP.QPO — PO Receipt Staging Table** (confirmed from T7DEV):

| Field | Description |
|-------|-------------|
| ISAP.QPO.PONUM | PO number (from EDI 855 POA) |
| ISAP.QPO.PCODE | Item code |
| ISAP.QPO.PQTY | Quantity to receive |

ISAP.QPO is the 855 POA (purchase order acknowledgment) staging queue. The SKIP.PONUM/PCODE/PQTY flags control whether those fields are overridden from the imported file or kept from the matching PO.

**T7DEX — Export Data Dictionary Helper:** MEM.SELECT.FLD/NUM, MEM.DICT_DESC/NAME/TYPE/SIZE/DEC/ARRAY — in-memory data dictionary reference used during export configuration.

**T7DEPH — EDI Price Update (DE-P-H):** Updates SO prices from EDI 864 file — stdpck (standard pack), custpo (customer PO), PRCE (price). SO range filter.

**T7DETB extended web import field mapping** — up to FIELD.NUMBER[44] — 44 configurable column positions for complete SO header + ship-to detail including: drop shipment (FIELD.NUMBER[25]), currency ([26]), order discount ([27]), ship-to detail including email ([42]) and ship-to code ([43]).

**T7DEPB EDI Releases (855 POA):** RELEASE_NUM, edi.price, edi.reindex, out.type (PSV/fixed) — customer releases with pricing option and file reindex.

---

### PS — Extended User Table (ISEX)

T7PSA.DFM confirms two extended user fields not previously documented:

| Field | Description |
|-------|-------------|
| ISEX.USER.GROUP | User group assignment (for group-based menu access) |
| ISEX.USER.WINDO | Windows username (for auto-login matching) |
| velocitrack | Velocitrack admin flag (third-party shop-floor integration) |

Combined with previously known BKPS.USER: CODE + seclevel + seccode [A/P/1/2/C/V/U/E] + company + bkps.user.emp (employee link) + auto.log.

---

### IS.RMA — Return Merchandise Authorization Table

Confirmed from T7RMAWHY.DFM:

| Field | Description |
|-------|-------------|
| bkar.inv.sonum | RMA SO number |
| bkar.invl.um.ln[1] | Line number |
| is.rma.status | RMA status |
| bkar.invl.pcode | Item code |
| bkar.invl.pdesc | Item description |
| srma.oinvnum | Original invoice number |
| srma.osonum | Original SO number |
| rma.desc | RMA description/reason |
| rma.warranty | Warranty type [N/L/P/B/Blank] |
| rma.promdate | Promise date |
| rma.reason | Reason code |

Note: `srma.*` prefix (vs `is.rma.*`) suggests two separate tables — ISRMA (primary) and a secondary SRMA or BKRMA table with original-order links.

---

### ISSR.INFO — SR / Quote Extended Info Table

From T7QTINFO.DFM (Quote Misc. Information — same schema as T7SRINFO):

| Fields | Count | Description |
|--------|-------|-------------|
| ISSR.INFO.DATE[1..5] | 5 | Date UDFs |
| ISSR.INFO.AL1..AL20 | 20 | Alpha UDFs |
| ISSR.INFO.SRNUM | 1 | SR/Quote number (PK) |

26 total UDF fields per SR/Quote. Used identically for both SR service repair orders and QT sales quotes.

---

### MA — AR Deposits — ISAR.DEPL Confirmed

T7MAPDEPO.DFM confirms the deposit application line table fields:

| Field | Description |
|-------|-------------|
| BKAR.DEP.DEPNO | Deposit number (PK in BKARDEP) |
| BKAR.DEP.CUST | Customer code |
| amount.rem | Amount remaining on deposit |
| depo.orig.amt | Original deposit amount |
| ISAR.DEPL.SO | SO number being applied to |
| ISAR.DEPL.AMT | Amount applied from deposit |
| ISAR.DEPL.GLACT | GL account override for deposit application |

The deposit apply workflow: customer pays deposit (BKARDEP entry) → applied to specific SO lines (ISAR.DEPL entries) → GL debit/credit via ISAR.DEPL.GLACT.

---

### IS-M Multi-Currency: Period Conversion Uses 12 Periods

T7ISMCC.DFM (IS-M: Convert Source to Base Currency) uses:
- ISGL.CYDATE[1..12] — 12 GL period dates for currency conversion
- gl.period[1..12] — period display
- is.cvt.mth — conversion month
- is.date — convert/post as of date

**Key finding:** The currency conversion module uses 12 periods, not 14. The 14-period structure (confirmed in AM module) is for actuals/budgets; currency conversion aligns to fiscal year structure (12 standard periods).

---

### LC — Lot Control Forms Summary

All 7 LC forms confirmed:

| Form | Purpose | Key Fields |
|------|---------|-----------|
| T7LCA | Edit Lot Numbers | MTLOT.LOT/ONHAND/RECDATE/WO/WOSUF/EXPDATE/LOC/POCOST/PO; default.bin |
| T7LCB | Assign Lot Control | MTIC.PROD.LOT flag per item |
| T7LCC | Print Lot History | prt.allocs (SO allocations), sort.text, incl.totals |
| T7LCC2 | Print Lot Availability | serial number range + lot exp date + item range |
| T7LCE | Exceptions Report | neg.only (negative UOH lots), orphans.only (orphaned lots) |
| T7LCF | Lot Traceability | item + lot.no + rpt.details (summary/detail/all) |
| T7LCG | Archive/Unarchive | archive/U flag, zero.uoh.only |

---

### AC — Activity Control (T7ACDATE / T7ACRDTYPE / T7ACTION)

All 3 AC DFMs confirm table schemas:

**WODATE table** (from T7ACDATE — AC date schedule):

| Field | Description |
|-------|-------------|
| WODATE.START | Start date |
| WODATE.FINISH | Finish date |
| WODATE.QTY | Quantity |
| WODATE.PARPRE/PARSUF | Parent WO prefix/suffix |
| WODATE.TOPPRE/TOPSUF | Top-level WO prefix/suffix |
| WODATE.DELPRE/DELSUF | Deleted WO prefix/suffix |

**AC.RD table** (from T7ACRDTYPE — corrective action document types):
AC.RD.TYPE, AC.RD.REASON, AC.RD.DISPO — document type + reason code + disposition code.

**IS.ACTION table** (from T7ACTION — action items):
IS.ACTION.TYPE, IS.ACTION.DESC — simple type+description code table.

---

### FA — Fixed Assets Full Field Layout Confirmed

T7FAA.DFM confirms all IS.FXA.* fields visible:

IS.FXA.CSTBAS, IS.FXA.TYPE, IS.FXA.NUMBER, IS.FXA.DESC, IS.FXA.DESC2, IS.FXA.RESVAL, IS.FXA.LIFE, IS.FXA.METH, IS.FXA.ACCUMDEP, IS.FXA.LDEPAMT, IS.FXA.LDEPPERC, IS.FXA.LDEPDATE, IS.FXA.GLA/GLD (asset GL account+dept), IS.FXA.ACDEPA/ACDEPD (accum dep account+dept), IS.FXA.DEPEXPA/DEPEXPD (dep expense account+dept), IS.FXA.SDATE/EDATE (placed-in-service / disposed dates), IS.FXA.SOLD (sale price), IS.FXA.SERIAL.

T7FAB confirms IS.FXT.* and adds: IS.FXT.NETAVAL (net asset value), ready (Ready-to-Post flag), TAGGED (for tagged batch posting).

T7FAE FA import: 22 field mappings (all ISFXASST fields mappable from CSV or fixed-length).

---

### IM — Multi-Currency + Landed Cost Full Confirmation

ISIS.MCF (currency master) — all 49 fields confirmed from T7IMB:
- GL account pairs (dept+acct) for: AP/AP-conversion/AP-deposit, AR/AR-conversion/AR-deposit, PO/PO-conversion, CS/CS-conversion, bank/bank-conversion, foreign exchange gain/loss
- Interest rate and days (ISIS.MCF.INTRES/INTDAY)
- Running balances: AMTBNK/AMTAP/AMTAR/AMTFE/AMTAD/AMTPOR/AMTCS

ISIS.MCR (exchange rates) — confirmed: DATE + BASE + SOURCE[1..10] + RATE[1..10] (up to 10 currency pairs per date row).

ISIS.LND (landed cost GL) — GLADT/GLDDT (duty), GLAFR/GLDFR (freight), GLACF/GLDCF (customs fees) — 3 cost types × 2 GL fields (account+dept) = 6 fields.

ISIS.DUTY — DCODE + PERC.
ISIS.BRK (customs broker) — CODE + FLAT + PERC + TYPE.

'''

with open(path, 'a', encoding='utf-8') as f:
    f.write(block)

print(f'Appended {len(block)} chars to HELP-RESOURCES.md')
