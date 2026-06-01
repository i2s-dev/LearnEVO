# US — Settings

Status: verified (text distilled from the vendor's help file).

*Source: EvoHELP.CHM → Settings (8 CHM topics).*
*Extracted HTML in [samples/chm/extracted/](../../../samples/chm/extracted/).*

The Settings menu provides per-user customization options accessible from any EvoERP session. Programs in this category control workstation display preferences, the main menu layout, screen geometry, login passwords, PO electronic signatures, calendar reminders, event-driven triggers, and Contract Review passwords. Most settings are workstation-specific; email settings are also company- and Evo-user-specific.

---

## Contents

- [US-A — Customize Settings](#us-a--customize-settings)
- [US-B — Customize Menu](#us-b--customize-menu)
- [US-C — Reset Screen Size/Location](#us-c--reset-screen-sizelocation)
- [US-D — Reset Password](#us-d--reset-password)
- [US-E — Update PO Electronic Signature Info](#us-e--update-po-electronic-signature-info)
- [US-F — Enter Reminders](#us-f--enter-reminders)
- [US-G — Enter Triggers](#us-g--enter-triggers)
- [US-H — Update Contract Review Password](#us-h--update-contract-review-password)
- [Cross-references](#cross-references)

---

## US-A — Customize Settings

*Source: [us-a_customize_settings.htm](../../../samples/chm/extracted/us-a_customize_settings.htm)*

**Purpose.** Establishes user-specific settings for screen view style (DBA Classic vs. Evo tabbed view), opening-list visibility, and email configuration (default text, signature blocks, BCC address, PDF destination folder). All settings are workstation-specific except email settings, which are also company- and Evo-user-specific.

### Misc Tab

**Enable Toolbar on screens** — enables the upper-right toolbar containing the calculator, camera, web link, and related utilities.

**Enable Topmost Windows** — forces EvoERP windows to remain the topmost screen above other applications.

**Enable Notification Sounds** — plays a "Ding" WAV sound when a lookup grid has completed its search.

**Auto Re-Start after running X** — restarts and re-logs into the Evo menu after the specified number of programs have run and the menu detects that no programs are currently open. Set to `0` to disable.

**Language** — selecting a language enables on-screen translation to that language when programs load. Language translation tables must first be created in SM-R Multi Language Maintenance.

**Dflt Print Path** — defines the folder where forms and reports are saved when printing to file.

**Enable Evo Reminders on Startup** — opens the Reminders calendar when Evo launches and enables the use of Triggers.

**Check for reminders** — defines how frequently (in minutes) the program polls for open reminders.

**Snooze All** — resets all open Reminders by the number of minutes specified.

**Enable Quick Printing** — bypasses the pop-up screens for RTM reports and Notes, using defaults instead.

**Disable Check for Updates at Login** — turns off the online patch check that runs at login.

**Hot Buttons** — up to 6 programs can be assigned to Hot Buttons on the main menu screen. Each button loads its assigned program regardless of which menu is currently displayed. An optional BMP image can be assigned to each button; if no image is supplied, numbered circles (1–6) are used.

### Mfg Tab

Select whether opening lists are displayed and whether programs load in Evo or Classic view for manufacturing programs.

### Items Tab

Select whether opening lists are displayed and whether programs load in Evo or Classic view for inventory/items programs.

### Sales Tab

Select whether opening lists are displayed and whether programs load in Evo or Classic view for sales programs.

### Queries Tab

Currently no settings on this tab.

### Sys Mgr Tab

Currently no settings on this tab.

### Accounting Tab

Select whether opening lists are displayed and whether programs load in Evo or Classic view for accounting programs.

### Payroll Link Tab

Currently no settings on this tab.

### Payroll Tab

Currently no settings on this tab.

### Email Tab

Configure outbound email for document distribution:

- **SMTP address and login information** — server hostname and credentials.
- **Port** — the SMTP port number.
- **Security** — options are `None`, `SSL`, or `STARTTLS`.
- **BCC** — blind-copy email address applied to all outbound emails.
- **Default subject, body, and signature** — pre-filled text for email composition.
- **Attach path** — folder where PDF files are generated before attachment. Must be a valid folder with full Windows user-profile rights.
- **Auto-email failure address** — when processing a batch of documents (e.g., invoices), any records with no email address assigned will be routed to this address so the operator is alerted that further attention is required.

---

## US-B — Customize Menu

*Source: [us-b_customize_menu.htm](../../../samples/chm/extracted/us-b_customize_menu.htm)*

**Purpose.** Allows the current user to customize the EvoERP menu structure.

This program is identical to TA-H Maintain Menu - End User. All features and behavior documented under TA-H apply here. The Settings-menu entry provides a shortcut so users can reach the end-user menu customizer without navigating to the TA (Table Administration) section.

---

## US-C — Reset Screen Size/Location

*Source: [us-c_reser_screen_size_location.htm](../../../samples/chm/extracted/us-c_reser_screen_size_location.htm)*

**Purpose.** Recovers a program window that has been maximized or moved off-screen and can no longer be resized or repositioned using normal window controls.

**Operation.** Open the program whose window is stuck (e.g., AP-A), then run US-C and click **Reset**. The window geometry for that screen is cleared and will return to its default size and position on the next open.

---

## US-D — Reset Password

*Source: [us-d_reset_password.htm](../../../samples/chm/extracted/us-d_reset_password.htm)*

**Purpose.** Allows the currently logged-in user to change their own EvoERP login password without administrator intervention.

**Operation.** Enter your **old password**, then enter the **new password** and re-enter it as confirmation. The change takes effect immediately.

Note: An administrator resetting another user's password is handled through PS (Password Security), not this program.

---

## US-E — Update PO Electronic Signature Info

*Source: [us-e_update_po_electronic_signature_info.htm](../../../samples/chm/extracted/us-e_update_po_electronic_signature_info.htm)*

**Purpose.** Maintains the per-user information required for electronic Purchase Order approval, including the digital signature image and the PO "Entered By" initials.

**Operation.**

1. Enter your **Employee Number** and **Password** for Electronic PO Approval to authenticate.
2. Once the correct password is accepted, the following fields become editable:
   - **Password** — click the **Reset** button in the lower-right corner to change it.
   - **Digital signature image file location** — path to the image file (typically a BMP or similar) that is printed on approved POs.
   - **PO "Entered By" Initials** — the initials stamped on POs created by this user.
3. Edit the desired fields on screen, then save.

Note: The help text contains a typo ("lower riught corner") confirmed in the source HTML — this is a vendor authoring artifact.

---

## US-F — Enter Reminders

*Source: [us-f_enter_reminders.htm](../../../samples/chm/extracted/us-f_enter_reminders.htm)*

**Purpose.** Enter or edit calendar-based reminders that can be optionally linked to customers, vendors, items, files, or URLs.

**Program Operation.**

The program opens to a calendar showing the current month. Dates that have an active Reminder are highlighted in blue with a dot marker. Clicking a date opens a new reminder entry for that date. Fields available when creating a reminder:

- **Time** — select or type the time of the event.
- **Association** — optionally link to a customer, vendor, item, URL, or file.
- **Subject** — required short description of the reminder.
- **Description** — optional longer note.
- **Remind prior** — flag to receive a pop-up notification before the event time.

**Startup integration.** If **Enable Evo Reminders on Startup** is set to `Y` in US-A Customize Settings, a calendar icon loads on the Windows desktop when EvoERP starts. This icon opens the same reminders screen as US-F.

**Using Reminders at runtime.** When the scheduled time arrives, a pop-up window opens automatically indicating open reminders. Options from the pop-up:

- **Dismiss** — closes the reminder permanently.
- **Reschedule** — enter a new time to defer the reminder.
- **Snooze** — defer by a specified interval.
- **Open linked record** — if the reminder is associated with a customer, vendor, or item, dedicated buttons open AR-A or AR-Q (customer), AP-A or AP-U (vendor), or IN-A (item) directly on the associated record.

---

## US-G — Enter Triggers

*Source: [us-g_enter_triggers.htm](../../../samples/chm/extracted/us-g_enter_triggers.htm)*

**Purpose.** Enter or edit Triggers — a special class of Reminder that is generated automatically when a specific inventory or transaction action occurs in EvoERP. Triggers can also send email notifications, so users are alerted even when away from their workstation.

**Prerequisite.** **Enable Evo Reminders on Startup** must be set to `Y` in US-A Customize Settings.

**Program Operation.** The program opens listing all triggers assigned to the current user login. You can add a new trigger, delete an existing one, or double-click an existing one to edit it.

Each trigger record requires:

- **Trigger code** — the inventory/transaction action that fires the trigger (see full list below).
- **User** — the user to alert. Users with a Security Level of 1–10 (as set in PS-A) can create triggers for other users; Security Level above 10 restricts trigger creation to the current user only.
- **Email reminder** — optional; enter one or more email addresses to receive an email notification in addition to the desktop pop-up.
- **Item Number, Type(s), Customer Code, Vendor Code, Work Order, Sales Order, Purchase Order** — optional filters that limit which records fire the trigger.
- **Notes** — optional text associated with the trigger.
- **Days Pre** — for `LOT` and `SERIAL` triggers only; the number of days before expiration at which the warning fires.

### Trigger Codes

| Code | Event |
|---|---|
| `CARACTCLS` | A CAR Action was closed — reminder to Owner |
| `CARACTNEW` | A CAR Action was created — reminder to the team |
| `CARNEW` | A new CAR was created — reminder sent to Owner |
| `CARPENDING` | A CAR has been marked as Completed — Initiator gets a reminder to review it |
| `CR APPROVE` | Contract Review: someone approves a SO in CR-B |
| `CR CREATE` | Contract Review: someone assigns a SO in CR-A |
| `DC CLOCKIN` | Clock-in to the DC (Data Collection) module |
| `DIGSIG APP` | PO Approval at PO-T |
| `EPO PRICE` | Edit PO Price |
| `ESTD COST` | Edit Standard Cost |
| `EVOSERVICE` | Test whether EvoService is still running |
| `ITEM` | A new Part Number was created |
| `OLD BIN` | A part was moved from one BIN to another (WC turned off; old BIN activity) |
| `PACKSLIP` | Packing slip printed |
| `PART REQ` | A part was requested in WO-K-M |
| `PO` | A new Purchase Order was created or lines were added to an existing order (fires per line) |
| `RECEIPTALO` | A PO tied to a Work Order was received |
| `RECIEPTQC` | Parts in PO-C were received to QC (note: vendor spelling retained) |
| `REV` | Someone changed the Draw/Rev level of a part |
| `RMA` | An RMA was created |
| `RMA RECPT` | An RMA was received |
| `SO CLOSE` | Someone closed a Sales Order |
| `SO DELETE` | Someone deleted a Sales Order |
| `SO EDIT` | Someone edited a Sales Order |
| `SO INVCD` | A Sales Order was invoiced and posted (SO-G) |
| `SO TERMS` | Someone changed the SO payment terms |
| `SR NEW WO` | A new Work Order was created via SR-C |
| `TOOLCALIBD` | A tool's next calibration date is within a specified number of days |
| `WO CLASS P` | WO-A changed the Work Order class to `P` |
| `WO CLASS Y` | WO-A changed the Work Order class to `Y` |
| `WO CLOSE` | Someone closed a Work Order |
| `WO RELEASE` | Work Order status became `R` (Released) |
| `REORDER` | Item stock on hand hits the Reorder Level |
| `REORDERA` | Item quantity available hits the Reorder Level |
| `EFP` | Enter Finished Production |
| `RECEIPT` | A purchased item was received |
| `RECEIPTQC` | A purchased item was received to QC |
| `LOT` | A lot-controlled item is within a specified number of days of expiration |
| `SERIAL` | A serial-controlled item is within a specified number of days of expiration |
| `BASE PRICE` | An item's Base Price was changed in SO-Q-A or IN-B |
| `SO` | A new Sales Order was entered or lines were added (fires per line) |
| `SOEDIT` | Existing lines on a Sales Order were edited |
| `SODELETE` | An existing Sales Order was deleted |
| `EPO` | A Purchase Order was edited (fires per line) |
| `NONPO` | A PO receipt is past its Estimated Receipt Date |
| `NONSO` | A Sales Order is past its Estimated Ship Date |
| `NONWO` | A Work Order is past its Estimated Completion Date |

**Notes on specific trigger behavior:**

- `LOT` and `SERIAL`: enter the desired warning lead time in the **Days Pre** field.
- `NONPO`, `NONSO`, `NONWO` ("NON" triggers): checked at each login, looking back to the last login date.
- When a multi-line PO or SO fires a trigger, one reminder is generated per line. The pop-up allows selecting all and dismissing them in a single action rather than one at a time.
- A link to the associated item via IN-A is available on the reminder pop-up when an item-linked trigger fires.

---

## US-H — Update Contract Review Password

*Source: [us-h_update_contract_review_password.htm](../../../samples/chm/extracted/us-h_update_contract_review_password.htm)*

**Purpose.** Allows the currently logged-in user to reset their own password for the Contract Review approval module (CR module), which maintains a separate password from the main EvoERP login.

**Operation.** Enter your **Contract Review User Name**, your **old password**, then enter the **new password** and re-enter it as confirmation.

---

## Cross-references

- **PS** (Password Security) — PS-A System Users/Passwords: manages EvoERP login accounts and Security Level numbers that govern trigger creation permissions in US-G.
- **SD** (System Defaults) — system-wide defaults that complement the per-user settings configured here.
- **SM** (System Maintenance) — SM-R Multi Language Maintenance: language translation tables referenced by the language selector in US-A.
- **TA** (Table Administration) — TA-H Maintain Menu - End User: the menu customizer that US-B mirrors.
- **CR** (Contract Review) — uses the separate password maintained in US-H; trigger codes `CR APPROVE` and `CR CREATE` in US-G monitor CR workflow events.
- **PO** (Purchase Orders) — PO-T digital signature approval is monitored by the `DIGSIG APP` trigger; US-E maintains the per-user signature image and credentials.
