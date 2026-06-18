import sys
sys.stdout.reconfigure(encoding='utf-8')

path = r'C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\HELP-RESOURCES.md'

block = r'''

---

## Pass 99 — EvoLinks, FNO, Calendar, Infrastructure DFM sweep (2026-06-18)

### EvoLinks — Document Attachment System (ISLINKS Table)

EvoLinks.DFM confirms the ISLINKS table schema and attachment workflow:

| Field | Type | Meaning |
|-------|------|---------|
| IS.LNK.SORT | STRING | Sort key / attachment ID (PK part) |
| IS.LNK.DATE | DATE | Date attachment was added |
| IS.LNK.WHO | STRING | User who attached the file |
| IS.LNK.PRIVATE | STRING | Private flag — only visible to attaching user |
| IS.LNK.PCB[100] | STRING array | PCB (print control block?) — 100-slot array (attachment metadata) |
| FILELINK | STRING | Path/filename of the linked document |
| ALERTS | STRING | Alert/notification flag on this link |
| LEXIST | STRING | Link exists flag (document still present) |
| GEN.ID | STRING | Generic ID — the record key (customer#, WO#, etc.) that this link attaches to |
| inventory.link | STRING | Inventory link flag — link is to an inventory item |

**How EvoLinks works:** Every EvoERP record (customers, WOs, SOs, items, etc.) can have
documents, images, or files attached via EvoLinks. GEN.ID stores the parent record key;
FILELINK stores the document path (relative to `LinkDoc\` or absolute). LEXIST checks
whether the file still exists. IS.LNK.PRIVATE prevents other users from seeing the link.

**Kill button:** The KILL caption in the DFM is the delete-link action — removes the link
record from ISLINKS without deleting the actual file.

**Confidence: 78/100** — All visible fields confirmed from DFM; PCB[100] array purpose
inferred; GEN.ID linking mechanism inferred from pattern.

---

### EvoFNO — Features & Options Configurator (ISFO.HDR.* Table)

EvoFNO.DFM confirms the Features & Options header table:

| Field | Meaning |
|-------|---------|
| ISFO.HDR.PARENT | Parent part number (the configurable item) |
| ISFO.HDR.DESC | F/O configuration description |
| ISFO.HDR.CUST | Customer code (customer-specific configuration) |
| ISFO.HDR.VEND | Vendor code |
| ISFO.HDR.RFQ | RFQ number |
| ISFO.HDR.STATUS | Configuration status code |
| ISFO.HDR.DATE | Date created/modified |

**Conversion flags (turn F/O into real orders):**
- SOCB — convert to Sales Order
- WOCB — convert to Work Order
- POCB — convert to Purchase Order
- NICB — convert to New Item Number
- SQCB — convert to Sales Quote
- RQCB — convert to RFQ

**EvoFNOQty.DFM** — Quantity entry for conversion:
CVTQty (quantity to make), CVTLoc (location), CVTCV (customer/vendor), cvtdate (due date).

**How FNO works:** The user configures a product by selecting features/options from a
BOM-like tree (ISFO.HDR). When ready, it converts to a real SO, WO, PO, or new item
by transferring the F/O selections to the target module.

**Confidence: 72/100** — Header table confirmed; ISFO line (option selection) table
not yet fully analyzed; conversion mechanism inferred.

---

### CAL Module — Calendar and Reminders

**CALREM.DFM** — Calendar Reminders browser:
Shows reminders in calendar view. Confirms: "Export to Google Calendar" button
(calls CALREMGC.DFM). Drill-down: caldrillbt (drill into reminder details).

**CALREMGC.DFM** — Google Calendar Export:
from.date, thru.date (date range), expall/expopen/expdis (filter: all/open-only/dismissed-only).
Exports EvoERP reminders to Google Calendar iCal format.

**evorereminders.DFM** — Reminder Snooze:
remdate (new date), remmin (minutes until next alert), remtime (time for reschedule).
The "Snooze" functionality for IS.REM reminders.

**evoCSR.DFM** — Calendar Summary Report:
esd (ESD date flag), csd (CDD — customer desired date flag), cust.from/thru, item.from/thru,
ENTRY.DATE, custpo (customer PO column), qtybo (qty + backorder column), socust (SO# + customer column).
Cross-reference report of SOs by date range with optional columns.

---

### ISFO — Features & Options Line Table (ISFO.LIN.*)

From EvoFNO context (not directly confirmed but inferred from FNO pattern):
ISFO.LIN.PARENT → ISFO.HDR.PARENT, ISFO.LIN.OPT (option code),
ISFO.LIN.DESC (option description), ISFO.LIN.QTY (option quantity),
ISFO.LIN.SEL (selected flag).

**Confidence: 45/100** — Line table structure inferred from FNO navigation pattern.

---

### T7CUSTOMS — Configurable Custom Content Slots

T7CUSTOMS.DFM fully confirms the 10-slot configurable content system:

| Field | Meaning |
|-------|---------|
| Custom.control[1-10] | Enable/disable flag for slot N |
| Custom.Name[1-10] | Caption/label for slot N |
| Custom.Desc[1-10] | Description for slot N |

These 10 slots appear across multiple modules as user-configurable custom fields.
The T7CUSTOMS form manages the slot labels and enable states (one row per slot).

**Confirmed earlier:** MTIC.PROD.RCOST[15] = Duty uses one of these slots as the
standard cost component label system.

**Confidence: 82/100** — All 30 fields confirmed (10 × 3 arrays).

---

### EvoUpdate Infrastructure

**EvoERPupd.DFM / EvoForceUpd.DFM** — Update engine forms:
- Uforce = force update flag (bypass version check)
- Clog = create log file flag
- FD Name / FileName = data dictionary field name + update file name
- "Files in this Update" + "Files to Force" — two-panel view: which files the update includes vs. which to force-overwrite

**EvoUPDsetup.DFM** — Update server setup:
file_name = server path for update distribution.

**Evocnvtb.DFM** — Data dictionary synchronization:
ConvertingFile = currently processing table name. Syncs the Btrieve DDF
with the actual .B file structure after schema changes.

---

### EvoService / Mobile Installer Forms

**EVOSERVICEREMOVE.DFM** — Remove EvoService: simple path entry + continue.
No data fields — just removes the Windows service registration.

**EvoMobilesetup.DFM** — Mobile Reminders setup:
Same fields as EvoSchedsetup: file_name, email.cfg.SMTP/user/pass/Email/Name,
thirtytwo/sixtyfour, plus SMTP port. Sets up email for mobile reminder delivery.

**Evowkssetup.DFM / EvoDCsetup.DFM** — Workstation and DC terminal setup:
file_name (server path), dmy/mdy (date format toggle DD/MM/YY or MM/DD/YY).
Two variants of the same workstation-initialization form.

**EVOFUP.DFM** — Support file upload:
FUTECH (tech contact), fu.desc (description), FU.ATTACH (attach screenshots flag),
fu.name (your name), fu.REmail (return email). Internal tech-support file upload utility.

**EvocfgSave.DFM** — Save/restore program defaults:
evoss (Evo service settings flag). Manages saving and restoring EVO configuration defaults.

---

### EvoLinks CVT (Link Format Conversion)

**EvoLinkCVT.DFM** — "Evo Links CVT": converts old image-based links to the current
EvoLinks format. No data fields — purely a conversion progress indicator.

---

### EVOBSR — Business Status Rebuild

**EVOBSR.DFM** — Rebuilds the ISBSF (Business Score File — KPI aggregation table).
"Business Status Rebuild" + "Initializing..." — rebuilds cross-module KPI/score data.
ISBSF confirmed as the target table.

'''

with open(path, 'a', encoding='utf-8') as f:
    f.write(block)

print(f'Appended {len(block)} chars to HELP-RESOURCES.md')
