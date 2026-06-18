import sys
sys.stdout.reconfigure(encoding='utf-8')

path = r'C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\HELP-RESOURCES.md'

block = r'''

---

## Pass 94 — GF/JS/UTK/SPC/Approval-Suite/BOL/KIT/misc DFM pass (2026-06-18)

### GF — AR Charges / Global Finance Module

**GF Module Identity:** T7GFPRICE caption "Golding Farms Pricing" is a customer-specific
label on the pricing form. The GF module in EvoERP is "Global Finance / AR Charges" and
handles customer-specific pricing matrices and charge entry.

**BKIC.PMAT — Pricing Matrix Table (DFM-confirmed field additions):**

| Field | Description |
|-------|-------------|
| BKIC.PMAT.PCODE | Item/product code |
| BKIC.PMAT.SDATE | Start date (effective from) |
| BKIC.PMAT.EDATE | End date (effective through) |
| BKIC.PMAT.PFLAG | Pricing flag (pricing method/type) |

The full pricing matrix (BKICPMAT, 85 fields) was extracted from RWN in Pass 57.
T7GFPRICE DFM confirms the entry-form field names used during pricing setup.

**IS.GF.DEPT / IS.GF.DIV — GF Organizational Codes (confirmed from t7GFdept/t7GFdiv):**
- IS.GF.DEPT + IS.GF.DEPT.DESC — GF department code + description
- IS.GF.DIV + IS.GF.DIV.DESC — GF division code + description

**GF View Forms:**
- T7GFV — SO order view by date: SO, ORDDATE, ESD, SHIPTO, SORTJ (sort by job), SORTG (sort by group), JOB
- T7GFVS — Shipment view: "Orders to ship on [date]" — same SO fields
- T7GFR — Date range report: Orders From / Thru date

---

### JS Module — External Database Connector Settings

All 7 JS forms use identical structure — each configures a connection to a different
external database or reporting endpoint:

| Form | Target System |
|------|--------------|
| T7JSACC | Accounting connector |
| T7JSAIC | AIC connector |
| T7JSAPBI | Power BI connector |
| T7JSASRS | ASRS (Automated Storage/Retrieval) connector |
| T7JSOI | Open Items connector |
| T7JSQL | SQL export destination |
| T7JSettings | Master settings — Test/Generate/Detect + program generator |

**Common fields (all forms):** Host / port / name — DSN connection to external database.
**Additional (JSQL, JSettings):** TREEDEST — destination path for tree-format data output.

T7JSettings adds "Test Settings", "Generate Program", "Detect Settings" buttons,
making it the master configuration and program-generation interface for the JS connector family.
Same architecture as T7JCRM (JC remote DB) and T7VSCHED (Visual Scheduler).

---

### UTK Module — System Utilities (UT-K Series)

**T7UTKA — Data Deletion / Module Reset (DESTRUCTIVE):**
Clears all data from selected modules:

| Field | Module to clear |
|-------|----------------|
| CLR.COA | Chart of Accounts (GL) + BKSYMSTR |
| CLR.CUST | Customers / SO (AR) |
| CLR.VEND | Vendors / PO (AP) |
| CLR.INVN | Inventory + Manufacturing |
| CLR.EMP | Payroll employees |
| CLR.CM | Contact Manager |
| CLR.GLDATES | GL Period Dates only |
| done.gl/AR/AP/INV/PR/CM/DT | Completion flags per module |

**T7UTKD — GL Account Balance Transfer:**
Moves GL balances between accounts for year-end or restructuring:
- fycur (current FY) + fy1yp-fy6yp (1–6 years prior) — fiscal year range
- from.glacct/thru.glacct + from.gldpt/thru.gldpt — source account range
- susp.glacct/susp.gldpt — suspense account for the transfer

**T7UTKE — Location Code Rename:**
new.code (new location code), LOCATION (existing location to rename).
Updates all location references in the database.

**T7UTKF — Item Master Report (F variant):**
from/thru item, class, category ranges + item.type [RFAMNLBTKO] filter + prt.extdesc (include 2nd desc line).

**Item type codes (UTKF/UTKG):** R=Purchased, F=Finished goods, A=?, M=Made/manufactured,
N=Non-stock, L=?, B=?, T=?, K=Kit, O=Obsolete (inferred from context).

**T7UTKG — Item Master Report (G variant):**
Same as F + act.status filter [YNODEPSQR] (Y/N=active/inactive status plus D/E/P/S/Q/R variants) + GL account range.

**T7UTKH — Item Type Listing:**
inc.type[1-4] = Purchased Parts / Make From / Subassembly / Finished Goods toggles.
incl.inactive (include inactive), prt.note (print 2nd description line).
GL account range.

---

### Approval Suite — Cross-Module Approval Control

**SOAC — SO Approval Control (T7SOAC):**
Read-only or approval-gated view of the SO header for authorization workflow.
Fields confirm the same BKAR.INV.* structure as the main SO-A form — no new fields.
SRTYPE (SR/Quote type), BKAR.INV.DCODE (discount code), SLSP1/SLSP2 (salespeople),
COMM1/COMM2 (commission rates) visible in approval context.

T7SOACITEM — customer-specific items lookup (MTIC.PROD.CODE/DESC/DISP.UOH).
T7SOACPY — Copy SO to new SO number with new estimated ship date.

**APAC — AP Vendor Approval Control:**
t7apaC (AP Vendor master) confirms additional BKAP fields not previously documented:

| Field | Description |
|-------|-------------|
| BKAP.REM.ZIP | Remittance address ZIP |
| BKAP.REM.STATE | Remittance address state |
| BKAP.ADD1[2] | Remittance address line 1 |
| BKAP.ADD2[2] | Remittance address line 2 |
| BKAP.CITY[2] | Remittance city |
| BKAP.COUNTRY[2] | Remittance country |
| BKAP2.ID | Secondary ID / SSN (in BKAP2 table) |
| ISAPEX.LONGNAME | Vendor long name |
| ISAPEX.DATE[1] | Extended date UDF 1 |
| TMC.Bank | Bank name (treasury management) |
| TMC.Branch | Bank branch |
| TMC.AcctBase | Bank account base number |
| TMC.Suffix | Bank account suffix |
| bank.AcctNo | ACH routing account number |
| bank.RoutNo | ACH routing number |
| vend.status | Vendor approval status |
| territory | Vendor territory code |
| convert.sopo | Convert SO to PO flag |

T7APACON — BKAP.CONTACT[1-4] + BKAP.EMAIL[1-4] + BKAP.TELEPHONE[1-5] (4 contacts).

**ARAC — AR Customer Approval Control:**
T7ARAC (AR Customer master) confirms additional BKAR fields:

| Field | Description |
|-------|-------------|
| ISAREX.EXTADD[1..8] | 8-line extended address (ISAREX table) |
| BKAR.REQD.CERTS | Required certifications/approvals |
| BKAR.RTM.PRINT.GROUP | RTM print group (customer-specific report routing) |
| BKAR.LEAD.SRC | Lead source (1 && 2) |
| BKAR.price.mat | Price matrix override |
| BKAR.allow.bo | Allow back orders flag |
| BKAR.roll.surcharge | Roll surcharge into price flag |

T7ARACON — BKAR.CONTACT[1-5] + BKAR.EMAIL[1-5] + BKAR.TELEPHONE[1-5] (5 contacts).

T7ARACRE (AR Customer Credit): BKAR.CREDIT.HLD, BKAR.CREDITLMT, BKCM.DUNH.FORM (dunning form),
BKAR.FOLUPDTE (follow-up date), BKAR.DAYS.TOPAY, BKAR.LASTPMT, BKAR.LASTSALE,
BKAR.OUT.CREDIT[1-2] (two outstanding credit buckets), BKAR.OUTINV.

**WOAC — WO Approval Control:**
T7WOAC confirms additional WO cost array fields not previously documented:

| Field | Description |
|-------|-------------|
| MTWO.WIP.ESETUP | Estimated setup cost |
| MTWO.WIP.EMAT | Estimated material cost |
| MTWO.WIP.EOUTPR | Estimated outside process cost |
| MTWO.WIP.ELABOR | Estimated labor cost |
| MTWO.WIP.EFOVHD | Estimated fixed overhead |
| MTWO.WIP.VOVHD | Estimated variable overhead |
| MTWO.WIP.EMISC | Estimated misc cost |
| MTWO.WIP.EEXTRA | Estimated extra cost |
| MTWO.WIP.ETOT | Estimated total cost |
| MTWO.WIP.ASETUP | Actual setup cost |
| MTWO.WIP.AMAT | Actual material cost |
| MTWO.WIP.AOUTPR | Actual outside process cost |
| MTWO.WIP.ALABOR | Actual labor cost |
| MTWO.WIP.AFOVHD | Actual fixed overhead |
| WO.Convert | WO conversion date |
| WO.Production | WO production date |
| WO.Show | WO show date |
| wo.approval | Approval flag |
| scrapped.qty | Scrapped quantity |
| ssonum | Source SO number |
| NCR.QTY | NCR quantity |
| line.refno | Line reference number |

T7WOACFG — excl.zero.qty (exclude 0-qty BOM items), call.wokb (update BOM), call.woka (update routing).
T7WOACPY — Copy WO: C.SUFF (copy all suffixes), TO.WOP/TO.WOS (destination WO prefix/suffix).

---

### MH — Bill of Lading Forms Fully Confirmed (T7BOL / T7BOLMSO)

**T7BOL — Standard Bill of Lading:**

| Field | Description |
|-------|-------------|
| load.number | Load number |
| seal.number | Trailer seal number |
| trailer.number | Trailer number |
| author.number | Authorization number |
| control.number | Control number |
| pickup.time | Pickup time |
| driver.arrived | Driver arrived time |
| loading.start | Loading start time |
| loading.end | Loading end time |
| driver.departed | Driver departed time |
| pickup.date | Pickup date |
| SCAN.INV | Invoice number (scan) |
| sShip.Num | Shipper number |
| marks[1-2] | Shipping marks |
| LIST.DESC/QTY/CASES/WT/PALLET/DUEDATE/SHIPINFO | Commodity line arrays |
| edit.htype/hqty | Handling unit type/quantity |
| edit.pqty/ptype/HM/nmfc/class | Package line: qty/type/hazmat/NMFC/freight class |
| edit.pallet/add.pallet.wt/edit.pweight | Pallet info |
| commodity/department/edit.pairs | Freight classification |
| drop.shpnme/drop.ship.to[1-4] | Drop ship address |

**T7BOLMSO — Multi-SO Bill of Lading:**
Handles shipment consolidation across multiple SO lines:
- BOL header: sbolnum (BOL#), ship.custcode/name, ship.date, shpvia, SCAC (carrier code),
  carrier.name, billing.type [PCTN = Prepaid/Collect/Third-party/Notify], billing.acct,
  num.skids, marks[1-4], total.class, author/control/trailer/load/seal numbers
- billing.line[1-6] — 6 billing note lines
- EDIT/LIST arrays: item, SO#, description, ship qty, packages, package type, weight, HM, NMFC, class
- USER.NAME — user entering the BOL

The BOL forms are the primary output documents of the MH/Shipping Order module.

---

### KI — Kit Assembly (T7KIT)

**T7KIT — Kit Pull and Assembly Interface:**

BOM component display arrays (one slot per component):

| Array Field | Description |
|-------------|-------------|
| APART | Component item code |
| ADESC | Component description |
| ARQTY | Required quantity |
| AUOH | Units on hand (all locations) |
| ALUOH | Units on hand (in lot) |
| AQTY | Quantity to pull |
| ABIN | Bin location |
| ABOMNOTE | BOM note for component |
| ALOT | Lot number |
| ALOC | Location code |
| AOPER | Operation number |

**Control fields:** SCAN.WO (WO number), SCAN.EMP (employee), bkic.prod.code (kit item),
bkic.prod.desc, bkic.prod.note, mtic.prod.loc (default location), binloc (scan bin),
MTIC.PROD.CYCLE (cycle count flag), kit.ln.cntr (line counter), xlot (lot to assign),
xqty (quantity), xoper (operation), wobom.reference (BOM reference), scan.item (barcode scan),
sqty, bomnote.

Kit assembly integrates lot tracking (ALOT/xlot), barcode scanning (scan.item),
bin-level inventory (ALUOH, binloc), and BOM component visibility in one workflow.

---

### SP/SPC — Statistical Process Control — Additional Tables

Pass 84 documented IS.SPC at high confidence. T7SPC.DFM confirms additional fields:

**IS.SPC (SPC production data):**
GOOD (accepted qty), REWORK (rework qty), ANOTES (general notes), SIDE (side),
TYPE (defect type), DETAIL (detail code), TESTT (test type), TESTE[1-3] (test equipment 1-3),
OPER (operation), DATE, EMPNUM (employee).

**IS.SERR (Serial/error records):**
ERROR (error code), PROCESS (process step), COUNT (error count), REF (reference designator),
SERIAL (serial number), aDOF (date of failure), aREWORK (rework description),
aDIAG (diagnosis/root cause).

**IS.STRACK (Serial genealogy/traceability):**
PSER (parent serial number), CSER (child serial number), COMP (component code),
PROC/PROCESS (process step), AR (assembled/received flag).

SPC live monitoring: ATYPE, ADETAIL, ACODE, ACOUNT — real-time error type/count display
(T7SPCLIVEGRID).

---

### SOGC — SO Gross Costing Reports

T7SOGCogs — "SOG COGS Report": calculates COGS from invoices by range (invoice#, SO#,
shipper#, invoice date). all.printed flag to include all printed invoices.

T7SOGComm — "SOG Commission Report": same structure, calculates commission liability.

These are batch COGS and commission reconciliation reports operating on posted invoices.

---

### FO (F&O) Additional Forms

**T7FOC — Feature/Option Price Setup:**
PAR.DESC (feature/parent item description), COMP.DESC (option component description),
BKBM.PROD.OPYN[4] / BKBM.PROD.OPYN[5] — option yes/no flags in BOM (slots 4-5),
BKBM.PROD.PRICE — option price, Add Price to Parent flag, Use STD Customer Pricing flag.

The BKBM.PROD.OPYN array appears at least through slot 5 (F&O flags in the BOM component record).

**T7FOD — F&O Range Report:** item/category/class range filters.
**T7FOE — F&O Single Item:** single item lookup for F&O configuration.

---

### FS — Field Information Base (IS.FIB.*)

Confirmed from T7FSCLASS / T7FSEMP / T7FSINFO (FS module DFMs):

| Field | Description |
|-------|-------------|
| IS.FIB.CLASS | FIB classification code |
| IS.FIB.GROUP | FIB group |
| IS.FIB.CONTRACT | Contract reference |
| IS.FIB.WHO | Who (responsible person) |
| IS.FIB.PROGRAM | Program/project code |

**SCAN.EMP** links FIB records to employees/reps. Market Segment field ties to sales rep.
FS module = "Field Information Base" — tracks field service records by class/group,
linked to contracts and programs. Not a general field service dispatch system.

---

### ML — Multi-Language (LANG.DICT.* confirmed from T7MLC/T7MLE)

T7MLC — language DFM generator: DFMName, Addlang, language (adds new language to a DFM file).
T7MLE — caption editor:

| Field | Description |
|-------|-------------|
| LANG.DICT.ECAPT | English (default) caption |
| LANG.DICT.LCAPT | Localized translation |
| LANG.DICT.LANG | Language code |

---

### EvoERPDrillM — Drill-Down Configuration (DRILLM Table)

T7DRILLM (SU module) confirmed from EvoERPDrillM.DFM:

| Field | Description |
|-------|-------------|
| DRILLM.PARENT | Parent grid field (source key) |
| DRILLM.CHILD | Child grid field (target key) |
| DRILLM.MENU | Menu label text |
| DRILLM.PFILE | Parent file/table |
| DRILLM.FILE | Child file/table |
| TField[1-5] | Target fields (5 columns mapped to child grid) |
| SField[1-5] | Source fields (5 columns from parent grid) |

Drill-down config = a parent grid cell value launches a child grid using the DRILLM
mapping to resolve source → target field relationships (up to 5 field pairs per drill).

---

### Other Pass 94 Findings

**T7WCBK — Live Work Center Dispatch Board:**
FROM.WC (work center from), timer (auto-refresh seconds), ISE.STATUS.2/3 (WO status filter slots 2-3), oper2 (operation filter), category, from.cust, priority. Feeds the live WC schedule view.

**T7ALTPART — Alternate/Substitute Parts (BKSB.PART):**
BKSB.PART.PROD (original item), BKSB.PART.SUBST (substitute item), SUB.DESC (description).
save.both.ways — creates the cross-reference in both directions.

**T7PUTAWAY — Warehouse Put-Away:**
scan.item, MTIC.PROD.CODE/DESC/LOC, BKIC.PROD.LRCPT (last receipt), BKIC.PROD.UOH,
enterbin (bin entry), action, PABBL (put-away by bin location), mtic.prod.uiqc (UOH in QC).

**T7SDET — Service Detail Codes (IS.SDET):**
IS.SDET.TYPE + IS.SDET.DETAIL — simple type+detail code table for SR service reason breakdown.

**T7STOCK — Stock/Brand Codes:**
Same table as T7BRANDS: BKCM.ACCC.CCODE / BKCM.ACCC.DESC.
T7STOCK is a second entry point to the same brand/category code table.

**T7FNR — Field Name Replace Utility (DESTRUCTIVE):**
Mass-update any field in any data file with up to 6 filter conditions:
FileNAME (target file), DNAME (field), element (array index), action,
flname[1-6] + felement[1-6] + oper[1-6] = filter conditions,
drepl_field/aREPL_FIELD/nREPL_FIELD = replacement values (date/alpha/numeric).
Position mode: spos/slength + POS[1-6] for substring operations.

**T7XCUTIL — XCharge CC Conversion:**
bkcm.acct.code — converts credit card data in CRM accounts to Secure XCharge vault.

**T7RTMVALID — RTM Report Name Selector:**
rtmvld_name — pop-up to select a valid report format name (RTM filename validation).

**T7ALERTMSG / evoalerts — Alert Display:**
Simple modal alert dialogs. T7ALERTMSG uses AlertMsgLabel for system alert messages.
evoalerts fires on alert conditions with Ignore button.

**EvoELinks — Enhanced Document Links Settings:**
Extends IS.LNK.* with: links.alert (link alert flag), links.itm.alert (item alert),
is.lnk.private (private flag), GlobalPath[1-10] (10 configurable global file paths),
WFA (Windows File Associations), OFA (Other File Associations).

**evoCSR — Calendar Summary Report (ESD/CDD view):**
ESD (estimated ship date), csd (customer delivery date), cust/item ranges, ENTRY.DATE.
Report field toggles: custpo (include customer PO#), qtybo (qty + backorder), socust (SO# + customer).
A shipping calendar showing open orders grouped by ESD or CDD.

**Dynamic-load forms (no DFM fields):**
CRMDASHBOARD, CASHFLOW, COMMISSIONRPT, MACHINEVIEW, WORKCENTERLOAD, BOMTREE, EDITBOMTREE,
PURCHITEM, PURCHVEND, INVCHANGE — all show "Loading..." caption.
These are web-based visualization panels launched from TAS Pro that load their UI from
an HTML/JavaScript layer, not from the DFM definition. Content is server-driven.

'''

with open(path, 'a', encoding='utf-8') as f:
    f.write(block)

print(f'Appended {len(block)} chars to HELP-RESOURCES.md')
