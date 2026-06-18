import sys
sys.stdout.reconfigure(encoding='utf-8')

path = r'C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\HELP-RESOURCES.md'

block = r'''

---

## Pass 93 — SH/POA/RFQ/TC/US/SL suite deep-DFM pass (2026-06-18)

### SL / Shop Loading — SH Module (T7SHA through T7SHP + T7SHIPRTM)

The SH module is **Shop Loading and Scheduling** (not Shipping). It manages WO dispatch,
work center capacity, forward/backward scheduling, and critical ratio calculation.

**SH-A (T7SHA) — WO Dispatch List:** Filter + sort for open WOs. Key fields:
MTWO.WIP.SSTART / MTWO.WIP.SFIN (scheduled start / scheduled finish), status, priority,
planner, item class, WC range, customer, priority range, color display by due-date or priority.

**SH-B (T7SHB) — Routing Operation Schedule Edit:**

| Field | Description |
|-------|-------------|
| MTWORO.OPER | Operation number |
| MTWORO.OPERDESC | Operation description |
| MTWORO.WC | Assigned work center |
| MTWORO.SCHED.WC | Scheduled (effective) work center |
| MTWORO.STQTY | Start quantity |
| MTWORO.QTYCOM | Quantity complete |
| MTWORO.CONTNTN | Contention flag (resource conflict) |
| MTWORO.OVERLAP | Overlap days (positive = overlap with next op) |
| MTWORO.NEGOVLP | Negative overlap (gap between operations) |
| MTWORO.TYPE | Operation type (R=run, S=setup, etc.) |
| MTWORO.VEND | Outside process vendor code |
| MTWORO.VENDNAME | Vendor name |
| MTWORO.LEAD | Lead time for outside process |

**SH-C (T7SHC) — Work Center Capacity View:**

| Field | Description |
|-------|-------------|
| MTWC.DEPT | Department code |
| MTWC.DEPTDESC | Department description |
| MTWC.HRSWEEK | Available hours per week |
| MTWC.%UTIL | Utilization percentage |
| MTWC.HRS.SHIFT | Hours per shift |
| IS.OUTPROC | Outside process flag on WC |

**SH-E (T7SHE) — Scheduling Engine (Critical Ratio Mode):**

| Field | Description |
|-------|-------------|
| SWO.CRATIO | Critical ratio per WO (TDATE / remaining days) |
| SWO.RUN.DAYS | Running days consumed |
| TDATE | Target/due date for critical ratio calculation |
| SPEC.ACTION.STR | Specific action string (override scheduling action) |
| SORT.OPTION.STR | Sort option (by CR, by WO, by WC, etc.) |
| incl.last.seq | Include last operation sequence flag |

**SH-F/G/H (T7SHF / T7SHG / T7SHH) — Filters and Status Reports:**
- SH-F: WO status filter [FR = Firmed/Released], WO range, planner, class, priority
- SH-G: Class include/exclude list, late WOs only, approved WOs only — WO status summary
- SH-H: Status report by date/range variant

**SH-I (T7SHI) — Shop Load Analysis:** Color-coded capacity view.
Flags: avail.only (available capacity only), prt.bom (print BOM), print.po (include POs),
MRP data, weekly.summary, incl.price. Outputs a load-vs-capacity grid by WC and week.

**SH-J (T7SHJ) — Machine/WC Gantt View:** Machine range + WC range filters.
Displays scheduled operations on a timeline.

**SH-M (T7SHM) — Lead Time Simulation:**

| Field | Description |
|-------|-------------|
| PR3.DATE | Priority 3 date (furthest out) |
| PR2.DATE | Priority 2 date |
| PR1.DATE | Priority 1 date |
| PR0.DATE | Priority 0 date (immediate) |
| DAYZ[1..4] | Days arrays for 4 priority levels |

**SH-N (T7SHN) — Item Lead Time Recalculation:** USE.Q (include queue times in lead time),
Finish Good / Subassembly type toggles, hours/day setting. Batch recalculates MTIC.PROD lead times.

**SH-O (T7SHO) — WC Print:** page.wc flag = page break between work centers in printed output.

**SH-P (T7SHP) — Scheduling Engine (Forward/Backward Mode):**
forward/backward toggle, due.date vs finish.date toggle, critical.ratio threshold, delay.days.
Priority coloring and elapsed-time coloring. Full schedule commit + preview modes.

**T7SHIPRTM — User RTM Assignment:**
ISEX.USER.MISC1 = RTM name (per-user default report template assignment for shipping),
ISEX.USER.CODE = user code. This extends the user table with a third misc field.

**New ISEX.USER field confirmed:**

| Field | Description |
|-------|-------------|
| ISEX.USER.GROUP | User group (for group-based menu access) — Pass 92 |
| ISEX.USER.WINDO | Windows username (auto-login) — Pass 92 |
| ISEX.USER.MISC1 | Default RTM name (per-user report template) — Pass 93 |

---

### RF / RFQ — Price Break Table (T7RFQ + T7POAPrBrk)

**BKRFQ — Request For Quote / Price Break Table:**

| Field | Description |
|-------|-------------|
| BKRFQ.EXP | Expiry date for this price break |
| BKRFQ.ISSUE | Issue date |
| BKRFQ.QTY | Quantity break |
| BKRFQ.COST | Cost at this quantity |
| BKRFQ.PROD | Item / product code |
| BKRFQ.LCDATE | Last changed date |

**T7RFQ workflow:** Generates RFQ from an estimate. Fields: aenum (estimate number),
is.est.orddesc (order description), LIST.PART / DESC / QTY / VEND / STDCST / STATUS / TAG.
Items can be individually tagged or group-tagged for vendor assignment.

**T7POAPrBrk:** PO price breaks referenced directly from PO entry — reads BKRFQ table
by BKRFQ.PROD to display vendor-specific tiered pricing.

---

### TC — Treasury Control (T7TCC)

Minimal form — selects payment terms and bank account for cash management:
- terms.num — payment terms number
- CHK_NAME[1] — bank account / check name

Treasury Control is essentially a payment-run selector: choose which terms to pay,
which bank account to draw from. The actual payment generation is in TPOA.

---

### US — Triggers / Notifications — IS.TRIG Table Fully Confirmed

**IS.TRIG — Complete Schema (T7USG):**

| Field | Description |
|-------|-------------|
| IS.TRIG.CODE | Trigger code (PK) |
| IS.TRIG.CUST | Customer filter |
| IS.TRIG.VEND | Vendor filter |
| IS.TRIG.SO | Sales order filter |
| IS.TRIG.PO | Purchase order filter |
| IS.TRIG.WOPRE | WO prefix filter |
| IS.TRIG.WOSUF | WO suffix filter |
| IS.TRIG.OPER | Operation filter |
| IS.TRIG.CLASS | Item class filter |
| IS.TRIG.CAT | Item category filter |
| IS.TRIG.PLANNER | Planner filter |
| IS.TRIG.BINLOC | Bin location filter |
| IS.TRIG.ODEL | Delete after triggering flag |
| IS.TRIG.TRIGR | User to trigger (recipient) |
| IS.TRIG.ONCE | Fire once on next occurrence flag |
| IS.TRIG.LDATE | Last triggered date |
| IS.TRIG.LTIME | Last triggered time |
| IS.TRIG.NOTE | Notes |
| IS.TRIG.CONTACT | Contact name |
| IS.TRIG.EMAIL | Email address |
| IS.TRIG.EFLAG | Email reminder flag |
| IS.TRIG.ITYPE | Item type filter |
| IS.TRIG.DAYS | Days before event to pre-trigger |

**Trigger logic:** Triggers fire when a matching entity (customer, vendor, SO, PO, WO, item)
reaches the specified condition. The ODEL flag auto-deletes after firing (one-shot triggers).
ONCE flag fires only on the next matching occurrence and stops. DAYS allows pre-event alerts.

---

### POA — PO Entry / Approval Suite (T7POA through T7POAIMPLINES)

**BKAP.PO header fields confirmed from T7POA:**

Vendor: VNDCOD, VNDNME, VNDA1/VNDA2, VNDCTY, VNDST, VNDZIP, VNDATN, VNDCNT,
TELEPHONE[1] (main), TELEPHONE[3] (fax).

Ship-to override: SHPCOD, SHPNME, SHPA1/SHPA2, SHPCTY, SHPST, SHPZIP, SHPATN, SHPCNT.

PO control: SUBTOT, TAXAMT, TOTAL, DESC, TERMNM, OBYCUS (job number field), FOB,
ENTBY, ISCUR (currency), LOC (location), GLDPT (GL department), TAXRTE, ISTXGR (tax group),
TAXABLE, ORDDTE, SHPVIA.

**BKAP.PO.CONFIRM[1] / CONFIRM[2]:**
- CONFIRM[1] — PO type (standard, blanket, etc.)
- CONFIRM[2] — Confirming PO flag (verbal/confirming order indicator)

**PO Line fields (T7POA2 enter.prod.* and LINE.PROD.* arrays):**
LINE (line#), CODE (item code), DESC (description), QTY, ERD (est receipt date),
PRCE, UM, PCON (price conversion factor), TAX, DISC, EST (estimate link),
WO / WO.OP (WO + operation link), GLA / GLD (GL account + dept override),
ARD (actual receipt date), CONF (line confirmed flag), LONG (long description text).
ECO info: edit.revlvl, edit.intrl, edit.eco, edit.draw.

**T7POAC — RITEC Aerospace Risk Assessment Extension:**

| Field | Description |
|-------|-------------|
| risk.assess[1..6] | 6 yes/no risk assessment questions |
| ritec.contract | Contract number |
| ritec.dpas | DPAS (Defense Priorities and Allocations System) rating |

Note: T7POAC is a customer-specific form (RITEC / aerospace) added to the PO entry flow
for NADCAP-related compliance documentation.

**T7POAE — Extended PO Entry:** Adds rush.expedite flag, "Sign PO" button (digital signature
integration), recv.to.qc flag (route PO receipt directly to QC inspection).

**T7POACPY — Copy PO:** new PO number, estimated receipt date, new vendor code.

**T7POAVITEM — Vendor-Specific Items:** MTIC.PROD.CODE, MTIC.PROD.DESC, MTIC.PROD.DISP.UOH
(display units on hand for vendor item lookup).

**T7POAIMPLINES — Import PO Lines (10 column mappings):**
Extends J7POAIMPLINES (8 mappings) with:
- FIELD.NUMBER[9] = comment column position
- FIELD.NUMBER[10] = sequence column position
- CONFIRM[2] = PO type (confirming PO flag)

---

### Standard Cost Array Correction — MTIC.PROD.RCOST Has 15 Slots

T7STDCST.DFM confirms **15 slots** in the MTIC.PROD.RCOST rolled-up cost array,
not 14 as previously documented (Pass 91 was incorrect):

| Slot | Label |
|------|-------|
| RCOST[1] | Material — This Level |
| RCOST[2] | Freight — This Level |
| RCOST[3] | Labor — This Level |
| RCOST[4] | Setup — This Level |
| RCOST[5] | Outside Process — This Level |
| RCOST[6] | FOH — This Level |
| RCOST[7] | VOH — This Level |
| RCOST[8] | Material — Rolled Up |
| RCOST[9] | Freight — Rolled Up |
| RCOST[10] | Labor — Rolled Up |
| RCOST[11] | Setup — Rolled Up |
| RCOST[12] | Outside Process — Rolled Up |
| RCOST[13] | FOH — Rolled Up |
| RCOST[14] | VOH — Rolled Up |
| RCOST[15] | **Duty** (landed cost duty — rolled up) |

**Correction:** MTIC.PROD.RCOST[15] = Duty. The 15th slot was added for landed cost
duty allocation in the standard cost rollup. Prior Pass 91 documentation showing 14 slots
was incomplete.

---

### ISREP.ORD — Commission Order Chargeback Table (T7CHARGBK)

| Field | Description |
|-------|-------------|
| ISREP.ORD.INVNM | Invoice number |
| ISREP.ORD.INVDT | Invoice date |
| ISREP.ORD.REPNM | Rep name |
| ISREP.ORD.COMPR | Commission percent |
| ISREP.ORD.CMAMT | Commission amount |
| ISREP.ORD.SONUM | Sales order number |
| ISREP.ORD.ULID | Update/last ID |

Used in rep chargebacks — tracks which invoices generated commissions for which reps.

---

### BKCM.ACCC — Brand / Account Class Codes (T7BRANDS)

| Field | Description |
|-------|-------------|
| BKCM.ACCC.CCODE | Brand/category code |
| BKCM.ACCC.DESC | Description |

Simple code table under the BKCM (CRM) namespace. Used to classify customers by
brand or account category for reporting and commission segmentation.

---

### SEL.LOCM — Location Selection Master (T7SELLOC)

| Field | Description |
|-------|-------------|
| SEL.LOCM.TAG | Tagged for selection |
| SEL.LOCM.CODE | Location code |
| SEL.LOCM.NAME | Location name |
| SEL.LOCM.TYPE | Location type |
| sel.incl.seg | Include segregated locations flag |

Popup/filter used wherever a location range is needed (inventory transfer, WO issue, etc.).

---

### T7CUSTOMS — Configurable Custom Content Slots

10 custom content blocks with individual enable/disable:

| Pattern | Description |
|---------|-------------|
| Custom.control[1..10] | Enable/disable flag per slot |
| Custom.Name[1..10] | Label / name per slot |
| Custom.Desc[1..10] | Description per slot |

Used to configure optional custom content areas in the EvoERP interface
(likely for custom UDF panels or optional feature blocks).

---

### T7VSCHED — Visual Scheduler Remote Database

Same remote DB connection pattern as T7JCRM:
Host / port / name (database server DSN), init / VS / Post operation modes,
WOs tab / WCs tab. Connects to the Visual Scheduler external database
for bi-directional WO schedule synchronization.

---

### Other Pass 93 Findings

**T7NEWINIT — New Company Initialization:** Bare initialization form for setting up
a new company in EvoERP. Minimal fields — company name + confirmation.

**T7BOMSCRAPFIX — BOM Scrap Recalculation:**
scrap.setting [% or Q = percent/quantity], synch.wos (synchronize WOs), blanks.only
(only recalculate items with no current scrap setting).

**T7BZFIX — Location File Fix Utility:**
LOC_FILE_NAME, LOC_BUFF_NAME, LOC_LOCATION, TAGGED, FSEARCH — low-level location
record repair tool.

**T7EMGL — Email GL Link:**
from.glacct / gldpt + BKGL.EXTRA — associates a GL account with an email address
(BKGL.EXTRA field stores the email). Used for automated GL posting notifications.

**T7STTYPE / T7STYPE — Service Type Codes:**
IS.STYPE.TYPE — service type code table (both forms use same field = same table).

**T7ALOGSETUP — Auto-Login Setup:**
USER, password, enable/disable auto-login. Workstation-level auto-login config
(distinct from ISEX.USER.WINDO which is the per-user Windows-name match).

**T7AUTODCH — Automated DC Hours:**
Employee/shift/WO/time/date range filters for batch labor posting from
automated data collection devices.

**T7EDII — EDI Inbound Release Import:**
FIELD.NUMBER[1..6] → item number, ship date, PO number, quantity, firm/scheduled flag,
customer code. Maps EDI 830/862 scheduled releases to EvoERP fields.

**T7DSIG / T7DigSigChgPSWD — Digital Signature:**
Digital signature setup and password change forms. No new table fields — uses
existing BKPS.USER security framework with a digital signature password layer.

**T7ISMCC — Multi-Currency Conversion (IS-M):**
Already documented in Pass 92: ISGL.CYDATE[1..12], gl.period[1..12],
is.cvt.mth, is.date. 12 periods for currency conversion (not 14).

'''

with open(path, 'a', encoding='utf-8') as f:
    f.write(block)

print(f'Appended {len(block)} chars to HELP-RESOURCES.md')
