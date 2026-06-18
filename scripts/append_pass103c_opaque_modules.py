"""
Pass 103c — Append 16 opaque module identifications to HELP-RESOURCES.md
Source: RUN string dumps + DFM caption analysis + SRC source code (BKLME.SRC)
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

PATH = r'C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\HELP-RESOURCES.md'

BLOCK = '''

---

## Pass 103c — 16 Opaque Module Identifications (2026-06-18)

Source: .RUN string dump analysis (confirmed table refs), BKLME.SRC source code,
DFM caption extraction. These 16 module codes were previously listed in EVO-DECOMPILE-TODO.md
as essentially unknown (15/100 confidence).

| Module | Code | Programs | Identification | Evidence |
|--------|------|----------|---------------|----------|
| **RMA / Returns** | AB | T6ABINV.RTM, T6ABPO1.RTM, T6ABrma1.RTM, ISABOUT.DCY | Return Material Authorization — tracks customer returns, reverse receipts, and credit invoices. ISABOUT.DCY is the EvoERP "About" dialog (unrelated to AB module). | T6ABrma1.RTM = RMA report; T6ABINV = return invoice; T6ABPO1 = return PO. |
| **Execute Utility** | EX | t7exec.RUN | Single-purpose program executor / shell command runner. | Only one file: t7exec.RUN |
| **Flexible Location** | FL | ISFLOC.RUN | Flexible Location Control — manages non-fixed inventory bin locations. | ISFLOC.RUN; ISFLOC likely references BKICLOC/BKICLOCM tables. |
| **Lot Movement** | LM | BKLMA–BKLMG (+ BKLME.SRC) | Inventory lot movement reporting and management. Tracks qty transactions by type: I=Issue, A=Adj, J=WO-job, P=Purchase, W=WIP, S=Sales, Q=QC, O=Other, C=Closing. | BKLME.SRC opens MTICMSTR + INVTXN; variable arrays QTY.I/A/J/P/W/S/Q/O/C confirm all INVTXN transaction types. BKLMA.RUN opens BKICMSTR, MTICMSTR, BKICLOC. |
| **Mass AP Deposits** | MA | ISMASVOD.RUN, T7MAPDEPO.DFM/RWN | AP deposit mapping and mass void operations. T7MAPDEPO = "Map Deposits" form (customer, deposit #, amount, GL account, item number). ISMASVOD = "IS Mass Void" (batch void of checks/vouchers). | T7MAPDEPO.DFM captions: "Map Deposits", deposit/GL/amount fields. ISMASVOD name = mass void. |
| **Manufacturing Mgmt Reporting** | MM | BKMMA–BKMMH (8 programs) | Cross-module manufacturing management reports. BKMMB bridges Payroll (BKPRMSTR/BKPRSALE/BKPRGLFL) and WO labor (WOLABOR). BKMMF uses all WO tables (WORKORD, WORECV, BKDCLAB, WOEXCHG, WODATE, WOROUT, WOBOM). BKMMA includes MKAHIST (Marketing Activity History). | BKMMB.RUN strings: BKPRMSTR, BKPRSALE, BKPRGLFL, BKPRINFO, WOLABOR. BKMMF.RUN strings: WORKORD, WORECV, BKDCLAB, WOEXCHG, WODATE, WOROUT, WOBOM. |
| **Payroll Link** | PL | BKPLA–BKPLE (5 programs) | Links EvoERP to an external payroll software package. PL-E = Payroll Link Setup (stores path to payroll software in BKCPMSTR). PL-D = "Import Employees (under construction)". BKPLA uses BKCPMSTR, checks for "DOS version of DBA". | BKPLA.RUN: "A path was not found for the Payroll software, please use PL-E (Payroll Link Setup)". BKPLE.RUN: "PL-E Payroll Software Link Setup". |
| **Report Template** | RT | T7RTMVALID.DFM/RWN, T6RTRue.RTM | RTM validation / report format selection utility. T7RTMVALID allows selecting a report format name from a list (used when multiple RTM formats exist for one report). | T7RTMVALID.DFM captions: "Select Report Format Name", OK/Cancel. |
| **Scoreboard Export** | SB | BKSBMFG.XPT, BKSBVEND.XPT | Business Scoreboard data export. XPT = export template files (binary format). BKSBMFG = Manufacturing scorecard export; BKSBVEND = Vendor scorecard export. Used by EVOBSR (Business Score Report) subsystem to produce comparative exports. | Both are .XPT (export template) files — no .RUN programs. |
| **Shop Loading / SFC** | SL | t7slsfc.RWN | Shop Loading and/or Shop Floor Control. "SFC" = Shop Floor Control. | t7slsfc.RWN = TAS7 Shop Loading-Shop Floor Control (encrypted binary). |
| **User Menu Maintenance** | UM | BKUMA–BKUMD (4 programs) | Allows administrators to define custom user menus (MENUFILEA). BKUMA = Enter User Menus; BKUMB = Print User Menus. Menus are stored in MENUFILEA / MENUFILEI tables. | BKUMA.RUN: "Enter User Menus", "Menu Maintenance A", "Menu code is not on file, 'Y' to add". BKUMB.RUN: "Print User Menus". |
| **Update Utility** | UP | ISUPDATE.RUN | EvoERP version update utility — applies patch/update scripts to the database. Referenced by BKUPDATE table. | ISUPDATE.RUN (single program); BKUPDATE table tracks applied updates (VER, COMPANY, DATE, UPDATE). |
| **YN Flags Editor** | YS | T7YSYN.RWN | System yes/no configuration flag editor — UI for BKYSMSTR 200+ boolean settings fields. | T7YSYN.RWN (encrypted binary). Previously confirmed at 72/100. |

**Unidentified / no files found:**
- **CP** — No files in share. Possibly deprecated; may have been merged into another module.
- **PC** — No files in share. Possibly Price Codes (now part of SO-Q) or deprecated.
- **SY** — No files matching T7SY*/BKSY* found. The System module functions are accessed via other modules (BKSYMSTR, BKSLEVEL) rather than standalone SY programs.

**T7PLessComps.DFM / T7PLessNotes.DFM (PL DFMs):**
Despite having the "PL" prefix, these forms are WO-related, not Payroll Link:
- T7PLessComps: "Issue Components", "Shortages", "WO Number" → WO component shortage/issue form
- T7PLessNotes: "QC Specifications", "Routing", "Vendor", "WO" → WO notes popup with QC/routing context
These are most likely sub-forms for a "PLess" (short for "Paperless" or a WO picklist operation)
that happen to use the T7PL prefix. Their exact parent program has not been identified.

---

### Summary: 16 Opaque Modules (Pass 103c confidence update)

| Module | Before | After | Notes |
|--------|--------|-------|-------|
| AB / RMA | 15 | 45 | 3 RTM report files confirmed, function clear from names |
| CP | 15 | 15 | No files — cannot improve |
| EX | 15 | 40 | Single RUN file, single-purpose utility |
| FL | 15 | 40 | ISFLOC.RUN name self-explanatory |
| LM | 15 | 75 | BKLME.SRC fully read; all 7 INVTXN transaction types confirmed |
| MA | 15 | 55 | T7MAPDEPO.DFM confirmed + ISMASVOD name clear |
| MM | 15 | 45 | 8 programs found; BKMMB+F table refs identified but purpose mixed |
| PC | 15 | 15 | No files — cannot improve |
| PL | 15 | 65 | BKPLE "Payroll Software Link Setup" confirmed; 5 programs found |
| RT | 15 | 60 | T7RTMVALID.DFM captions clearly describe RTM format selector |
| SB | 15 | 40 | 2 XPT export templates found; EVOBSR connection inferred |
| SL | 15 | 30 | 1 RWN file only (encrypted) — name = shop floor |
| SY | 15 | 20 | No files — function handled by other modules |
| UM | 15 | 70 | BKUMA/BKUMB strings: "Enter/Print User Menus", MENUFILEA confirmed |
| UP | 15 | 60 | ISUPDATE.RUN + BKUPDATE table correlation |
| YS | 72 | 72 | Already documented (not in this pass) |

Average confidence for these 16: ~15 → ~47 (gap 35 → ~18)
'''

with open(PATH, 'a', encoding='utf-8') as f:
    f.write(BLOCK)

print(f'Appended {len(BLOCK):,} chars')
