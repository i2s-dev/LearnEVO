import sys
sys.stdout.reconfigure(encoding='utf-8')

path = r'C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\PROJECT-STRUCTURE.md'

# Replace stale last-updated note and add new pass
old_footer = '*Last updated: 2026-06-17 — built from menu_to_form.csv, master_index.csv, tables.txt,\nschema.md, SRC analysis, catalog.md, and rwn_symbols.json DB fingerprint passes 1–18. Confidence varies by section — see EVO-DECOMPILE-TODO.md.*'

new_footer = r'''*Last updated: 2026-06-18 — built from menu_to_form.csv, master_index.csv, tables.txt,
schema.md, SRC analysis, catalog.md, rwn_symbols.json DB fingerprint passes 1–18, and DFM analysis passes 91–97. Confidence varies by section — see EVO-DECOMPILE-TODO.md.*

---

## MODULE CODE CORRECTIONS (Pass 97)

The following module code descriptions in the Module Codes table above need correction:

| Code | WRONG description | CORRECT description |
|------|-------------------|---------------------|
| SH | Shipping | Shop Loading / Scheduling (dispatch, capacity, critical ratio) |
| MH | (not previously listed) | Shipping / Bill of Lading (T7BOL + T7BOLMSO) |
| JS | (not previously listed) | External DB Connector Settings (7 connector forms: ACC/AIC/Power BI/ASRS/OI/SQL/JSettings) |
| GF | (not previously listed) | Global Finance / AR Charges (BKICPMAT pricing matrix maintenance) |
| UT | Utilities | Utilities + UT-K series (data clear, GL transfer, location rename, item-type reports) |
| WBK | (not previously listed) | Workbench / Menu Customizer (custom menu builder, grid lookup editor) |
| WTAS | (not previously listed) | TAS Utility Suite (DMS browser, CFFLOC registry, file init, schema merge) |

---

## Pass 19 — New Tables from DFM Passes 91–97 (2026-06-18)

| Table | File | Module | Purpose | Status |
|-------|------|--------|---------|--------|
| MTWC | MTWC.B | SH (Shop) | Work center master — capacity, rates, efficiency, queue/move times; read by SH and MRP | confirmed |
| MTWORO | MTWORO.B | SH / WO | WO routing operations — one row per operation on a WO; WC, times, completion status, critical ratio | confirmed |
| IS.TRIG | ISTRIG.B | Alerts | Trigger/notification rules — 23 fields: CODE, CUST, VEND, SO, PO, WOPRE, WOSUF, OPER, CLASS, CAT, PLANNER, BINLOC, ODEL, TRIGR, ONCE, LDATE, LTIME, NOTE, CONTACT, EMAIL, EFLAG, ITYPE, DAYS | confirmed |
| BKRFQ | BKRFQ.B | PO/RFQ | RFQ price break table — EXP, ISSUE, QTY, COST, PROD, LCDATE; stores vendor quote price breaks | confirmed |
| BKICPMAT | BKICPMAT.B | GF/IC | Customer pricing matrix — PCODE+SDATE key; 10 break levels (QTY[1-10]/RATE[1-10]/PDESC[1-10]) + EDATE/PFLAG | confirmed |
| CFFLOC | CFFLOC.B | WTAS | EvoERP file/table registry — CF_FLNAME, CF_FLCODE, CF_RTYPE, CF_DESC, CF_PATH, cf_fdname; authoritative list of all registered tables | confirmed |
| DRILLM | DRILLM.B | EVO Infra | Drill-down menu config — PARENT, CHILD, MENU, PFILE, FILE, TFIELD[1-5], SFIELD[1-5]; cross-module navigation definitions | confirmed |
| IS.FIB | ISFIB.B | EVO Infra | Field Information Base — CLASS, GROUP, CONTRACT, WHO, PROGRAM; controls field visibility/editability | confirmed |
| IS.CATM | ISCATM.B | SM-I/IC | Item category master — CODE, DESC; maintained via SM-I (T7SMIF) | confirmed |
| BKCM.LEAD | BKCMLEAD.B | SM-I/CRM | CRM lead source codes — SCODE (PK), DESC | confirmed |
| BKCM.TERR | BKCMTERR.B | SM-I/CRM | CRM territory codes — TCODE (PK), DESC, EMAIL | confirmed |
| BKCM.ACFC | BKCMACFC.B | SM-I/CRM | CRM activity/follow-up codes — FCODE (PK), DESC, REP, dashboard flag | confirmed |
| BKCM.DTCD | BKCMDTCD.B | SM-I/CRM | CRM document type codes — DCODE (PK), DESC | confirmed |
| ISSR.INFO | ISSRINFO.B (via alias) | SO | SO/SR user-defined fields — SRNUM (PK), DATE1-5, AL1-20; used for BOTH SO header and SO line UDFs | confirmed |
| IS.REM | ISREM.B | CAL | Reminder/alert records — DATE, TIME, SUBJECT, TYPE, CO, DISP, item/cust/vend/contact/email links, other.user | confirmed |
| LANGDICT | LANGDICT.B | SM/EVO | Multi-language caption dictionary — ECAPT (English), LCAPT (local language), LANG (language code) | confirmed |

---

## Pass 19 — New DFM Form Catalog Entries (2026-06-18)

**Scheduler and backup infrastructure (confirmed from Pass 95 DFM analysis):**

| DFM File | DCY File | Purpose | Key Fields |
|----------|----------|---------|------------|
| evoERPsched.DFM | EVOERPSCHED.DCY | Day-of-week scheduler — schedules ERP batch jobs | stime, mon/tue/wed/thur/Fri/sat/sun, runonce/weekly, rtime |
| EvoERPbackup.DFM | EVOERPBACKUP.DCY | EvoERP backup — Full/Company/Custom ZIP backup | zipName, fullsystem/compdata/custom, COMP.TAG/EXT/NAME, CSTFILELIST |
| EvoSchedsetup.DFM | EVOSCHEDSETUP.DCY | Scheduler task configuration | Task name, program, schedule |
| EVOSERVICESETUP.DFM | EVOSERVICESETUP.DCY | EvoService Windows service installer | email.cfg.SMTP/user/pass/Email/Name/sec, smtpport, thirtytwo/sixtyfour, file_name |
| EvoERPDrillM.DFM | EVOERPDRILLM.DCY | Drill-down menu setup | DRILLM.*: PARENT/CHILD/MENU/PFILE/FILE/TFIELD[1-5]/SFIELD[1-5] |

**Print/email infrastructure (confirmed from Pass 95 DFM analysis):**

| DFM File | DCY File | Purpose | Key Fields |
|----------|----------|---------|------------|
| printtll.DFM | PRINTTLL.DCY | Universal print dialog — 4 output modes | print_opt[1-4], autoemail, contname/contnum/contprimcode |
| nzemailtll.DFM | NZEMAILTLL.DCY | Email composer — To/CC/BCC with contact grids | entTO/CC/entICC, EMAILLIST, bccself, TEMPATT, Email.cfg.subj |

**WTAS (TAS Utility Suite) — file registry and browser forms:**

| DFM File | Purpose |
|----------|---------|
| WTASFLOC.DFM | Edit CFFLOC file registry — add/edit table entries |
| WTASINIT.DFM | Initialize a new data file — adds row to CFFLOC |
| WTASDMS2.DFM | Array element entry dialog (ARRAYCNTR) |
| WTASDMS3.DFM | Memo field editor |
| WTASDMS4.DFM | Filter expression entry (FilterExpr) |
| WTASDMS5.DFM | Find-next expression entry (FindFilterExpr) |

**SM-I code table forms (T7SMIA through T7SMIF → manage BKCM.* and IS.CATM):**

| Form | Table managed |
|------|---------------|
| T7SMIA.DFM | BKCM.LEAD (lead source codes) |
| T7SMIB.DFM | BKCM.TERR (territory codes) |
| T7SMIC.DFM | BKCM.ACFC (activity/follow-up codes) |
| T7SMID.DFM | BKCM.ACCC (account/brand codes) |
| T7SMIE.DFM | BKCM.DTCD (document type codes) |
| T7SMIF.DFM | IS.CATM (item category master) |

**SM-J archive/purge forms (T7SMJA through T7SMJH — see Recipe 11):**

| Form | Purpose |
|------|---------|
| T7SMJA.DFM | Inventory reconciliation (report-only) |
| T7SMJB.DFM | WO archive/restore/purge |
| T7SMJC.DFM | Inventory transaction archive |
| T7SMJD.DFM | Inventory transaction purge by type [ASPJWIQOCMTRG] |
| T7SMJE.DFM | WO purge (closed/cancelled) |
| T7SMJF.DFM | PO archive |
| T7SMJG.DFM | QC receiver archive |
| T7SMJH.DFM | DC data collection purge (by CUT.DATE) |

**SO additional forms (confirmed in Pass 95 DFM analysis):**

| Form | Purpose | Key tables/fields |
|------|---------|-------------------|
| T7SOABKD.DFM | Booking date entry | sobookdate |
| T7SOAFRT.DFM | Freight amount popup | BKAR.INV.FRGHT |
| T7SOAIMPLINES.DFM | Import SO lines from external ERP | FIELD.NUMBER[1-7], company.code/path, sponum |
| T7SOAPRC.DFM | Pricing matrix display | BKIC.PMAT.QTY/RATE/PDESC |
| T7SOAXCOM.DFM | Extra commission overrides | seREP, ecommp, eoveramt, eoverp |
| T7SOINFO.DFM | SO line-level UDFs | ISSR.INFO.SRNUM + DATE1-5 + AL1-20 |
| T7SOHINFO.DFM | SO header-level UDFs | ISSR.INFO.SRNUM + DATE1-5 + AL1-20 (same schema) |
| T7SOJINFO.DFM | Recurring SO settings | mem.group, mem.freq, mem.max, bkar.inv.invdte |

---

*Pass 19 additions are confirmed from DFM FieldName= extraction during Passes 91–97.*
'''

with open(path, encoding='utf-8') as f:
    content = f.read()

if old_footer in content:
    content = content.replace(old_footer, new_footer, 1)
    print('Footer replaced successfully.')
else:
    # Try partial match
    print('Full footer not found — appending instead.')
    content = content.rstrip('\n') + '\n\n' + new_footer

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Done.')
