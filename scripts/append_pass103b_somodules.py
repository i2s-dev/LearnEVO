"""Pass 103b — append SO-O / SO-P / SO-Q / SO-R..V sub-modules to HELP-RESOURCES.md"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

PATH = r'C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\HELP-RESOURCES.md'

BLOCK = '''

---

## Pass 103b — SO Sub-Modules: Reports (SO-O), Proposals (SO-P), Pricing (SO-Q), Misc (2026-06-18)

Source: DFM analysis of untracked samples/dfm/ forms — T7SOOA-I (reporting), T7SOP* (proposals),
T7SOQ* (pricing master), T7SOR/S/V (receive/release/backorder), T7SOSER/SONQTY (allocation helpers),
T7SORevu (contract review).

---

### SO-O — Sales Order Reporting Sub-Module (T7SOOA..I, T7SOOM, T7SOON)

| Form | Purpose |
|------|---------|
| T7SOOA.DFM | Print SO open order report — includes backorder amounts, WO est hours, days-to-ship calculation |
| T7SOOB.DFM | Print SO summary by item or estimated ship date |
| T7SOOD.DFM | Print SO delivery report (customer order range, customer due date filter) |
| T7SOOE.DFM | Print SO WO labor hours remaining report (WO filter for labor hours) |
| T7SOOF.DFM | Print SO open order by customer / due date |
| T7SOOG.DFM | Print SO by customer name and estimated ship date |
| T7SOOH.DFM | Print SO AR voucher / invoice batch (currency range, AR voucher flag) |
| T7SOOI.DFM | Print SO open order listing with comments |
| T7SOOM.DFM | Print SO change history report (change date, customer, commissions changes) |
| T7SOON.DFM | Print SO on-time delivery report — ESD vs ASD (actual ship date) with early/late tolerances |

---

### SO-P — Proposals / Sales Quotes Sub-Module (T7SOP*)

The SO-P sub-module manages pre-sales proposals and formal sales quotes. Quotes can be
converted to SOs via SO-P-C. Win likelihood (0–9) is tracked per quote.

| Form | Purpose |
|------|---------|
| T7SOPK.DFM | Enter / edit proposal header (full order entry screen: address, attention, city, country, lines) |
| T7SOPF.DFM | Enter / edit proposal lines (items, quantities, prices, comments, balance on order) |
| T7SOPC.DFM | Convert proposal to SO — change ESD, customer due date, location, close after conversion |
| T7SOPB.DFM | Print proposal win likelihood report (filter by win likelihood 0–9) |
| T7SOPM.DFM | Print proposals report (with job# and order description check option) |
| T7SOPI.DFM | Proposal / quote inquiry |
| T7SOPJ.DFM | Proposal job file reference (file name, start time — time-stamping) |
| T7SOPO.DFM | Auto-generate or review proposals (customer range, default job#) |
| T7SOPOR.DFM | PO receipt review dialog from proposal (item, exp recv date, price, qty — "Review" button) |
| T7SOPP.DFM | Process proposals (batch conversion or status update by customer) |

**Business context:** Proposals are the pre-sale step before a confirmed SO. A sales rep enters a
proposal in SO-P-K, adds items in SO-P-F, marks win likelihood, and when the customer confirms,
SO-P-C converts it to a live SO. The BKSOA/BKSOA2 programs share the T7SOAC form for quotes too —
the distinction between a "proposal" (SO-P) and a "quote" (SO-A in quote mode) may be status-flag
driven within the same form set.

---

### SO-Q — Pricing Master Sub-Module (T7SOQ*)

Controls item base prices, price codes, customer contract pricing, and mass price changes.

| Form | Purpose |
|------|---------|
| T7SOQA.DFM | Enter / edit item base price (with contract price and price code multipliers) |
| T7SOQH.DFM | Enter / copy price code headers (customer, discount code, multiple price tiers) |
| T7SOQB.DFM | Print price list (filter by active status: Y/N/O/D/E/P/S/Q/R) |
| T7SOQI.DFM | Print price code listing (customer / date / discount code range) |
| T7SOQK.DFM | Print price code report (by category, class, customer) |
| T7SOQC.DFM | Mass price change — direction (up/down), type (%), amount, with contract and price code updates |
| T7SOQJ.DFM | Recalculate prices from cost basis — new base price = cost × markup; optionally update contract prices |
| T7SOQL.DFM | Import price codes from CSV file |

**Price code status field values (active status filter `YNODEPSQR`):**
- Y = active, N = inactive, O = obsolete, D = discontinued, E = end-of-life,
  P = prototype, S = sample, Q = quote-only, R = restricted

---

### SO-R / SO-S / SO-V / SO-SER / SO-NQty / SO-REVU

| Form | Purpose |
|------|---------|
| T7SOR.DFM | AR refund / deposit re-application from SO (city, country, department, deposit, description) |
| T7SOS.DFM | SO release screen — auto-release comments, include backorders, customer range |
| T7SOV.DFM | SO backorder management — edit back-ordered qty, customer due date, customer name |
| T7SOSER.DFM | SO serial number allocation (similar to T7SOBIN: item, qty, bin, tag, remove all) |
| T7SONQTY.DFM | SO-N quantity availability popup — shows available, allocated, on-PO, on-BO, lead time, min order qty |
| T7SORevu.DFM | SO contract review sign-off — "SO Contract Review" with customer, SO#, entered by/date, KILL button |
| T7SORevuPSWD.dfm | Contract review password dialog (ID, department, password — required before sign-off) |

**SO Contract Review (T7SORevu + T7SORevuPSWD):**
A quality-gate feature where a specific SO must be reviewed and signed off by an authorized
reviewer before it can be processed. The "KILL" button on T7SORevu likely voids / rejects the review.
The password dialog (T7SORevuPSWD) authenticates the reviewer by Contract Reviewer ID + password +
department — suggesting role-based approval routing.

---

*Pass 103b — SO sub-module catalog: SO-O (11 reporting forms), SO-P (10 proposal forms),
SO-Q (8 pricing forms), plus SO-R/S/V/SER/NQty/REVU ancillary forms.*
*Total SO DFMs now cataloged: 71 forms.*
'''

with open(PATH, 'a', encoding='utf-8') as f:
    f.write(BLOCK)

print(f'Appended {len(BLOCK):,} chars')
