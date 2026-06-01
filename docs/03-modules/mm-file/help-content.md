# Main Menu — File Programs

Status: verified (text distilled from the vendor's help file).

*Source: EvoHELP.CHM → Main Menu (File) Programs (2 CHM topics).*
*Extracted HTML in [samples/chm/extracted/](../../../samples/chm/extracted/).*

These two programs appear on the EvoERP main menu File section and provide low-level database and report maintenance. Both are restricted by the same password-security system used elsewhere in EvoERP: if a user lacks the corresponding System Manager menu entry, the item does not appear in the File drop-down either.

---

## Contents (anchor links)

- [Maintain Database](#maintain-database)
- [Report Editor](#report-editor)

---

## Maintain Database

*Source: [maintain_database.htm](../../../samples/chm/extracted/maintain_database.htm)*

**Purpose:** Use this program to view or directly edit data file records. It is a support tool, primarily for system administrators, used to repair data records when the normal EvoERP programs cannot be used. It does not update related files the way the regular programs do, so it must be used with extreme caution.

### General Program Operation

- **Opening the tool:** Maintain Database is located on the main Windows menu. Click File, then Maintain Database.
- **Selecting a file:** Choose the file to view or edit from the Files Available window. See the File Names topic for a listing of files by module. You can also limit which fields are shown by checking the Choose Fields to Display box.
- **Controlling sort order:** Once a file is selected, choose any of the indexes in the Sort By window to control record listing order. Clicking different indexes updates the display order in real time.
- **Navigating fields:** Fields are displayed left to right. Most files have more fields than fit on one screen; use the scroll bars at the top and bottom of the main display window to pan through them. The current record is marked by an arrow in the narrow column to the left of the display.
- **Navigation buttons:** Four arrow buttons in the lower left of the screen advance to the first record, prior record, next record, and last record respectively.
- **Enabling edits:** The Edit checkbox in the upper right must be checked before any editing is allowed.
- **Deleting a record:** With editing enabled, click the minus-sign (delete record) button on the current record. A confirmation prompt appears before the deletion is committed.
- **Saving edits:** After changing fields, click the check-mark (post edit) button to save. To discard changes, click the X (cancel edit) button to restore the original data. If you move to a different record while unsaved changes exist, those changes are automatically saved without requiring the check-mark button.
- **Fast Search:** Type any search value into the Fast Search field to jump to the first record matching that value within the currently highlighted index. The search is case-sensitive.
- **Adding a new record:** Go to the last record in the file and press the down-arrow key to move to a blank row. Enter the data and save it the same way as editing an existing record.

### Password Security

Access to Maintain Database is intended for system administrators only. It can be restricted via PS-A System Users/Passwords by denying access to TA-D Maintain Database. If a user does not have that menu access in System Manager, the item will not appear in the File drop-down menu either.

---

## Report Editor

*Source: [report_editor.htm](../../../samples/chm/extracted/report_editor.htm)*

**Purpose:** The Report Editor provides a graphical layout editor for EvoERP report and form templates. It uses the Nevrona ReportBuilder engine, which stores layouts in `.RTM` files. The editor allows modifying the visual design of printed forms and reports across all modules.

### General Program Operation

This program is identical to TA-M Forms Editor (accessible through System Manager). If a user does not have menu access to TA-M Forms Editor in System Manager, the Report Editor will not be available in the File drop-down menu either.

The Report Editor / TA-M Forms Editor is the standard interface for modifying graphical report layouts. All EvoERP printed output (invoices, purchase orders, work orders, financial reports, etc.) that uses the ReportBuilder engine is stored as `.RTM` files on the network share and can be customized through this tool.

### Notes on the Underlying Engine

- The Report Editor runs on the **Nevrona ReportBuilder** engine (`RBDsgnr.exe`).
- Report templates are `.RTM` files stored on the network share (e.g., `\\i2s109-solidcrm\DBAMFG$\` or related paths).
- Modifying a template here affects every user who prints that report, since the `.RTM` files are shared.
- The CHM keywords for this topic are `graphical layouts`, `graphical layouts modify`, and `Modify Forms`, indicating these are the primary use cases the vendor anticipated.

---

## Cross-references

- **TA-D Maintain Database** — the System Manager equivalent of Maintain Database; access to that menu item controls File-menu access as well.
- **TA-M Forms Editor** — the System Manager equivalent of Report Editor; identical program, same access control.
- **PS-A System Users/Passwords** — governs who can access both tools.
- **UT (Utilities)** — related low-level maintenance tools.
- **GL and all reporting modules** — any module that produces printed output (AR, AP, IN, SO, PO, WO, GL) uses `.RTM` templates editable via the Report Editor.
- **File Names topic** (EvoHELP.CHM) — lists data files by module; referenced from Maintain Database for identifying which `.B` (Btrieve) file to open.
