# DCY Forms Catalog — All 41 Decrypted Files

Status: verified (all 41 files decrypted and scanned 2026-06-17)

All `.DCY` files are Delphi VCL form definitions encrypted with Twofish-192-CFB-128 using key K_D.
After decryption they are standard Delphi `.DFM` text format (`object Name: ClassName … end`).
`suwin6.dcy` uses key K_C (see below). `suwin7.dcy` uses an unknown 5th key — see `decryption-findings.md`.

### suwin6.dcy — ISTech License Dialog (K_C key, confirmed Pass 375 2026-06-29)

Form: `EditForm1_1: TEditForm1_1` — **ISTech License dialog** (shown at EvoERP startup)
Caption: `' ISTech License'`; style: `fsStayOnTop` (modal, always-on-top)
Components: Image1 (PNG logo), Memo1 (company address), 7 × TLabel, TGlyphBtn, TRtnTimer, 2 × TBevel

**Key data hardcoded in form:**
| Component | Caption | Meaning |
|-----------|---------|---------|
| lblUserSerialNum | `670538` | License serial number |
| lblUserNum | ` 48` | Max concurrent users |
| lblUserLicType | `VPY` | License type code |
| Memo1 Lines | `i2 Systems / 355 Bantam Lake Rd / Morris, CT 06763` | Registered company |
| lblFromIgnore | `lblFromIgnore` (hidden) | License start date (set at runtime) |
| lblThruIgnore | `lblThruIgnore` (hidden) | License end date (set at runtime) |
| lblLimitedUse | `***` | Limited-use indicator (set at runtime) |

Timeout: `TRtnTimer` with `Interval=3000` / `SecondsBtwnCalls=3` / `CallPrgLoc=-1` — auto-dismisses after ~3 seconds.
Hint: `'C:\TASPRO7\DBA7\tas6evodba.DFM'` — developer path on ISTech's build machine.
Copyright: `Evo~ERP 2003-2013` + `MGM Holdings 1985-2003`.
**Purpose of K_C**: protects the license credentials embedded in this form.

`samples/suwin6_decrypted.bin` — regenerated correctly Pass 375.

The companion `.DFM` file on the network share is always the matching plaintext copy;
the `.DCY` is the deployed encrypted version the runtime actually loads.

---

## Group 1 — Main Menu System (TAS Pro 7 / EvoERP era)

### EVOERPMENU.DCY (1,432 KB)
Form: `TEditForm1 "MainMenu"` — **main EvoERP window shell**
Caption: `'Evo ~ ERP'`
Key objects: TMainMenu (35 TMenuItems), TToolBar (33 TToolButtons), 8 × TTASStrList, TImage, TPanel, TStatusBar, TShellExe
Key menu items: File → Change Company / Exit; Module (empty at parse time); Size; Support; Help
Key insight: The 554+ module menu codes (AR-1, IN-2, etc.) are NOT stored here.
The 8 TTASStrLists are empty at parse time and filled at runtime by EvoERPmenu.RWN dynamically.
This file is the window frame only.

### DBAMENU_FLEX.DCY (1,099 KB)
Form: `TEditForm1 "EditForm1"` — **DBA Classic (TAS Pro 6) legacy menu window**
Caption: `'TAS Professional 6 for Windows'`
Key objects: 34 TToolButtons, 9 TMenuItems, 4 TTASStrList
Key menu items: File → Change Company / Exit; Module; Help → DBA help / About
Key insight: The older generation main window, kept alongside the EvoERP window.
Bulk of file size is embedded icon image data in hex. Module entries built at runtime.

---

## Group 2 — Login & Session Management

### EVOMENU_LOGIN.DCY (17 KB)
Form: `TEditForm1` — **EvoERP main login dialog**
Caption: `'Evo ~ ERP'`
Fields: User Name (TTASENTER), Password (TTASENTER)
Buttons: OK, Cancel
Extras: TTASStrList × 3 (likely company list, user list, saved settings), TShellExe, View Password checkbox
Notes: Standard EvoERP workstation login; shown before company selection.

### EVODC_LOGIN.DCY (17 KB)
Form: `TEditForm1` — **Data Collection (handheld) login dialog**
Caption: `'Evo ~ ERP Hand Held'`
Fields: User Name, Password
Buttons: OK, Cancel
Extras: TTASStrList × 3, TShellExe, View Password checkbox
Notes: Separate login form for DC kiosk/handheld stations; same layout as EVOMENU_LOGIN but different caption.

### DBAMENU_LOGIN.DCY (2 KB)
Form: empty (0 objects) — **DBA Classic login placeholder**
Notes: No active form objects; the DBA era login is handled by the TAS Pro 6 runtime directly.

---

## Group 3 — Company Selection & Program Launch

### EVOMENU_SELCOMP.DCY (7 KB)
Form: `TEditForm3` — **company selection dialog**
Caption: `'Choose Company'`
Prompt: `'Click on the Down Arrow below to get a list of Companies:'`
Controls: TTASComboBox, Select / Cancel buttons, TMainMenu
Notes: Appears at login or via File → Change Company. Dropdown lists available companies from system config.

### DBAMENU_SELCOMP.DCY (2 KB)
Form: empty (0 objects) — **DBA era company selection placeholder**

### EVOMENU_RUNPRG.DCY (7 KB)
Form: `TEditForm2` — **"Run Program" module launcher**
Caption: `'Run Program'`
Fields: File Name (TTASComboEnter)
Buttons: Continue, Exit, Lookup File
Notes: Used by the menu system to launch any `.RWN` by filename. The bottom layer of EvoERP's module-dispatch mechanism.

### DBAMENU_RUNPRG.DCY (1 KB)
Form: empty (0 objects) — **DBA era run-program placeholder**

---

## Group 4 — Password Management

### EVOCHANGEPASS.DCY (14 KB)
Form: `TEditForm1` — **Change Password screen**
Caption: `'Change Password'`
Fields: User Name, Old Password, New Password, Reenter Password (4 × TTASENTER)
Buttons: Save, Exit

### EVORESETPASS.DCY (13 KB)
Form: `TEditForm2` — **Reset Password (admin) screen**
Caption: `'Reset Password'`
Fields: User Name, New Password, Reenter Password (no old-password field — admin-only reset)
Buttons: Save, Exit

### PRINTTLLPSWD.DCY (7 KB)
Form: `TEditForm2` — **SDQ Settings password prompt**
Caption: `'SDQ Settings Password'`
Fields: Enter Password (TTASENTER)
Buttons: OK, Exit
Notes: "SDQ" appears to be a print/report settings subsystem requiring a password to modify.

---

## Group 5 — Email

### NZEMAILTLL.DCY (107 KB)
Form: `TEditForm1` — **email composition form**
Caption: `' Evo ~ ERP email'`
Fields: To, Cc, BCC, Attachment, Subject, Form (email template name) (9 × TTASENTER)
Checkboxes: BCC Self, BCC Rep
Buttons: Send, Cancel, Cust (browse customer contacts), Vend (browse vendor contacts)
Grids: TTASDataGrid × 2 (customer contact list, vendor email list)
Extras: TShellExe (triggers email send), TRtnTimer (timeout)
Notes: "NZ" = NorthWest email library or a vendor prefix. "TLL" = template letter. Called from print/report flow when emailing a document.

### NZEDEFS.DCY (24 KB)
Form: `TEditForm1` — **email default settings**
Caption: `'Evo Email Default Settings'`
Fields: Subject, Body Text, Signature (TMemo × 2), Attachment path (APATH), BCC Self checkbox
Subject Fields / Body Fields buttons: insert merge fields into subject/body templates
Buttons: Save, Exit
Notes: Admin form for setting email composition defaults (used by NZEMAILTLL).

---

## Group 6 — Print System

### PRINTTLL.DCY (45 KB)
Form: `TEditForm1` — **universal print dialog**
Caption: `'Print'`
Print destinations (radio buttons): Print (to printer), Print Preview, Email, Print to File
Printer controls: Name (PrinterNameEnter), Setup button, Type, Where
File output controls: cbPrintType, cbEnterPath
Copies: Number of Copies (TSpinEdit)
Auto-email options: Auto Send Email, Email Contact Number, Email Contact Prim Code, Use Contact Name, Use Contact Number
Buttons: OK, Save Settings, Exit
Notes: The single shared print dialog used by all EvoERP reports. "Save Settings" persists printer choice per report. SDQ = print settings protected by PRINTTLLPSWD.

### IMAGEPRINT.DCY (7 KB)
Form: `TEditForm1` — **"Printing Linked Documents" progress screen**
Caption: `'Printing Linked Documents'`
Fields: Printing: (shows current doc filename, TTASENTER)
Extras: TShellExe (shell print command), TRtnTimer
Notes: Used by EvoLinks to print files attached to records (PDFs, images, etc.).

---

## Group 7 — Messaging

### EVOMESSAGE.DCY (8 KB)
Form: `TEditForm3` — **single-line message display**
Caption: `'Evo Message'`
Controls: TLabel "Msg", OK button
Notes: Modal message box replacement. Shows a single-line message to the current user.

### EVODCMESSAGE.DCY (8 KB)
Form: `TEditForm1` — **DC-mode message display**
Caption: `'Evo Message'`
Controls: TLabel "Msg", OK button (TSpeedButton)
Notes: Same purpose as EVOMESSAGE, used in Data Collection context.

### EVOEMSG.DCY (8 KB)
Form: `TEditForm17` — **broadcast message sender**
Caption: `'Evo Message'`
Controls: Broadcast Message text (TTASENTER "EntMSG"), Send to (TTASComboBox — "All Users" + individuals)
Button: Send
Notes: Lets an admin user broadcast a message to all logged-in users or a specific user.

### EVODCEMSG.DCY (8 KB)
Form: `TEditForm3` — **DC-mode broadcast message sender**
Caption: `'Evo Message'`
Controls: Broadcast Message (TTASENTER "EntMSG"), Send to (TTASComboBox — "All Users")
Button: Send
Notes: Same as EVOEMSG but used from DC menu.

---

## Group 8 — Data Collection UI

### EVODC.DCY (728 KB)
Form: `TEditForm3` — **DC main menu (kiosk touchscreen)**
Caption: (not shown in first 3KB scan)
Menu items: Labor/Prod, Prod. Only, Labor Only, Part Request, Shift In/Out, Dashboard
Notes: Large because of embedded icon images. The primary handheld/kiosk entry screen.
(Analyzed separately — see `docs/01-architecture/overview.md`)

### EVODCMENU2.DCY (87 KB)
Form: `TEditForm4` — **DC secondary tile-based launcher**
Caption: `'Data Collection Menu'`
Layout: 10 configurable program tiles (Shape + Image + Label per tile), labeled "Program 1–10" / "Label 1–10" at design time — actual names set at runtime
Menu bar: Programs, Settings, Co (Change Company), Help → Help / About / Exit
Notes: This is the customizable kiosk menu screen. Admins assign up to 10 programs to tiles. Used for DC workstations with a fixed set of allowed operations.

### EVODC_LOGIN.DCY — see Group 2 above.

---

## Group 9 — Scheduler

### EVOERPSCHED.DCY (13 KB)
Form: `TEditForm2` — **scheduler task name dialog**
Caption: `'Evo ~ ERP Scheduler'`
Fields: Task Name (TTASComboEnter "tname")
Buttons: Save, Exit
Notes: UI for naming/selecting a scheduled task. The full scheduler setup is in EvoSchedSetup.RWN; this is the lightweight entry point for picking an existing task or naming a new one.

---

## Group 10 — About & Splash

### ISABOUT.DCY (133 KB)
Form: `TEditForm1` — **About dialog**
Caption: `'About Evo ~ ERP'`
Key labels (populated at runtime): EVO.VER (version number), Build -, Serial / Users / Expiration, Pervasive -
Static strings: `'Evo ~ ERP Copyright '`, `'Evolved from DBA Classic 2004.1'`, `'Portions Copyright DBA Software.'`
Buttons: Ok, Licensed, Archives
Notes: The `EVO.VER` label text is the runtime variable holding the EvoERP version string. "Licensed" likely shows full license detail. "Archives" may open archive/history data.

### ISDCABOUT.DCY (566 KB)
Form: `TEditForm1` — **DC About screen / splash image**
Caption: (large image data)
Notes: Analyzed previously. Contains the confirmed copyright string "Evo ~ ERP Copyright © 2007 Evo ERP Inc." and "Evolved from DBA Classic 2004.1". Large due to embedded logo bitmap.

### ISSPLASH.DCY (138 KB)
Form: `TEditForm3` — **startup splash screen**
Caption: `' Loading Evolution ~ ERP....'`
Controls: TShape × 5 (decorative), TImage × 2 (logos), TGradient, TPanel
Notes: Shown while EvoERP initializes on first launch. Pure cosmetic.

### EVOLOGO.DCY (8 KB)
Form: `TEditForm16` — **menu screen logo configurator**
Caption: `'Logo'`
Controls: TTASComboEnter "logofile", Preview, Apply, Undo Last, Evo Default, Joke buttons
Notes: Admin tool to customize the background image on the main EvoERP menu screen. "Joke" = Easter egg / humour setting. "Evo Default" restores the stock logo.

---

## Group 11 — License / Expiry

### EVOEXPIRE.DCY (25 KB)
Form: `TEditForm1` — **license expiry warning**
Caption: `'Expiration Warning'`
Text: `'Your annual Evo-ERP license will expire in XX Days. If you have'` (runtime fills `XX`)
Controls: TImage (warning icon), TLabel, TRtnTimer (auto-close)
Notes: Confirms EvoERP uses an **annual subscription license model**. Warning shown on login when expiry is approaching.

---

## Group 12 — Generic Reusable Dialogs

### GETALPHAGEN.DCY (11 KB)
Form: `TEditForm1` — **generic single-field text input**
Caption label: `'GAG Caption'` (set by caller at runtime)
Fields: TTASENTER with label `'GAGLABEL:'` (set by caller)
Buttons: Ok, Cancel
Notes: "GAG" = Get ALpha General. A reusable modal input box for any single-field text prompt. Caller injects caption and label text at runtime.

### T7POPGET.DCY (18 KB)
Form: `TEditForm1` — **generic multi-field popup input (up to 5 fields)**
Caption label: `'POP Caption'` (set by caller)
Fields: 5 × TTASENTER with labels `'POPLABEL:'` (set by caller at runtime)
Buttons: Ok, Cancel, Lookup
Notes: "POP" = POPup GET. A reusable modal input for up to 5 fields. The Lookup button calls a standard list-picker. Used throughout the system wherever a modal data-entry popup is needed.

---

## Group 13 — Lookup / Grid System

### WBKLOOKUP.DCY (23 KB)
Form: `TEditForm1` — **standard list-picker dialog**
Controls: TTASDataGrid, TTASComboBox "Sort List by:", Label "Lookup:", TTASStrList × 2
Toolbar: Select, Edit, Add New, Delete, First, Previous, Next, Last, Exit
Menu: File → Select / Edit / Add New / Delete / Exit
Notes: The universal record-picker used everywhere a user needs to select from a list (customer, vendor, item, etc.). The TTASStrList slots are filled at runtime with the target table's data.
Source hint: `D:\TASPro6\WBKLOOKUP.DFM` — this is a DBA Classic era component, unchanged.

### WBKLUGRID.DCY (47 KB)
Form: `TEditForm1` — **lookup grid definition admin form**
Caption: `'Maintain Grid Lookup Data'`
Fields: Grid Name, File Name (Btrieve table), Form Name (RWN module), Security Level, Menu Text, Sort Keys, External UDF Params (program path + params), Evo Prg: (internal program override)
Checkboxes: Start At End, Links & Notes Field(s)
Columns section: Add Column, Field Data (× 2), Ext. UDF
Buttons: Save, Exit, Clear, Copy, Delete
Notes: The admin configuration form for EvoERP's configurable lookup grids. Each grid record defines: which table to read, which form to open on select, security level required, sort order, and optional UDF program for custom logic. This is how all the standard list-pickers are configured without hardcoding.

---

## Group 14 — Infrastructure / Framework

### DUMMY.DCY (6 KB)
Form: `TEditForm1` — **base window placeholder**
Caption: `'Evo Base Window'`
Controls: TLabel "Label1" only
Notes: Used as a template or base-class anchor. The `TEditForm1` definition that all real forms inherit from. MDUMMY.DCY is identical.

### MDUMMY.DCY (6 KB)
Form: `TEditForm1` — **base window placeholder (MT-era variant)**
Caption: `'Evo Base Window'`
Notes: Identical purpose to DUMMY.DCY; likely the "MT" (MTIC-era) version of the same base template.

### T7CLOADING.DCY (6 KB)
Form: `TEditForm1` — **"Loading Data" animated progress form**
Caption: `'Loading Data'`
Controls: TPanel, TGradientLabel, TAnimate (animated spinner/progress)
Notes: Shown while a background data-fetch operation runs. The TAnimate component plays an AVI loop.

### T7JAVARUN.DCY (10 KB)
Form: `TEditForm1` — **Java runner waiting screen**
Caption: `'T7JavaRun'`
Label: `'Java Evo Loading...'`
Controls: TRtnTimer (auto-dismiss when Java task completes)
Notes: Shown while EvoPVT.jar executes a background Java task. TRtnTimer polls for completion and dismisses the form automatically.

### EVOGETDATE.DCY (36 KB)
Form: `TEditForm1` — **date-or-news message with "do not show again"**
Caption: `'Evo ~ ERP'`
Controls: TTasBrowser (embedded browser), TMemo, TPanel, TTASCheckBox "Do not show this Message again", Exit button, TTASStrList
Notes: Multi-purpose — either a release-notes viewer (HTML in TTasBrowser) or a date-related prompt. "Do not show this Message again" suggests it's a splash/news dialog shown once per release. TTasBrowser renders an internal URL or local HTML file.

### EVOERROR.DCY (123 KB)
Form: `TEditForm1` — **file open error dialog**
Caption: `'File Open Error'`
Controls: TGradientLabel "Error:" (shows actual error text), TLabel "Line 1"
Notes: Shown when the TAS Pro runtime fails to open a .RWN or .DCY file. Large because of embedded background gradient/image data.

---

## Group 15 — DBA Classic (TAS Pro 6) era forms

### DBAMENU_FLEX.DCY — see Group 1 above.

All three `DBAMENU_*.DCY` files (LOGIN, SELCOMP, RUNPRG) contain 0 VCL objects after decryption.
They are present as encrypted containers but their form content is empty — the DBA Classic era login, company selection, and program launch are handled by TAS Pro 6 runtime internals, not by DFM-based forms.

---

## Summary Statistics

| Group | Count | Notes |
|---|---|---|
| Menu system | 2 | EVOERPMENU + DBAMENU_FLEX — window shells only |
| Login / session | 3 | ERP login, DC login, DBA placeholder |
| Company / launch | 3 | SELCOMP, RUNPRG, DBA placeholders |
| Password | 3 | Change, Reset, SDQ settings |
| Email | 2 | Compose, Defaults |
| Print | 2 | Print dialog, Image print progress |
| Messaging | 4 | Message display × 2, Broadcast × 2 |
| Data Collection | 2 | DC main menu, DC tile menu |
| Scheduler | 1 | Task name dialog |
| About / splash | 4 | About, DC About, splash, logo |
| License | 1 | Expiry warning |
| Generic dialogs | 2 | GAG (1-field), T7POPGET (5-field) |
| Lookup / grid | 2 | WBKLOOKUP picker, WBKLUGRID admin |
| Infrastructure | 5 | DUMMY × 2, Loading, JavaRun, GetDate |
| Error | 1 | File open error |
| DBA era (empty) | 3 | LOGIN/SELCOMP/RUNPRG (0 objects) |
| **Total** | **41** | |
