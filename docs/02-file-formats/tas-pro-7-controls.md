# TAS Pro 7 UI Controls — Complete Catalog

Status: verified (extracted from 1,136 DFM files on the network share, 2026-06-17)

All EvoERP forms are Delphi VCL forms using a mix of standard Delphi controls,
third-party components, and TAS Pro 7-specific custom controls. This document
catalogs all 51 distinct control types found across the codebase.

---

## Root Form Classes (TEditForm*)

TAS Pro 7 defines 16 variants of its base form class. Most behavior differences are
cosmetic or relate to border style, resize behavior, or which built-in event handlers
are bound by the runtime. **TEditForm1 dominates** (857/1,112 forms = 77%).

| Class | Count | Observed use |
|---|---|---|
| TEditForm1 | 857 | Default — almost every standard module screen |
| TEditForm2 | 110 | Variant with slightly different border/resize |
| TEditForm3 | 72 | Data Collection forms, splash screens |
| TEditForm4 | 32 | Tile-based launcher menus (e.g. EVODCMENU2) |
| TEditForm5 | 15 | Multi-record/list-heavy forms |
| TEditForm6 | 3 | — |
| TEditForm7 | 6 | — |
| TEditForm8 | 2 | — |
| TEditForm9 | 3 | — |
| TEditForm10 | 2 | — |
| TEditForm11 | 1 | — |
| TEditForm12 | 1 | — |
| TEditForm13 | 2 | — |
| TEditForm16 | 1 | EVOLOGO (logo configurator) |
| TEditForm17 | 1 | EVOEMSG (broadcast message sender) |
| TEditForm18 | 1 | — |

---

## TAS Pro 7 Custom Controls (TTAS* prefix)

These controls are defined by the TAS Pro 7 framework and are not standard Delphi VCL.
They interact with the TAS program via `TTASENTER`-style keywords.

| Control | Count | Purpose |
|---|---|---|
| **TTASENTER** | 7,504 | **Single-field alphanumeric text entry** — the core data-entry control. Every record field in EvoERP is a TTASENTER. Bound to a TAS buffer variable; validates and navigates between fields. |
| **TTASNumEnter** | 3,994 | **Numeric entry field** — like TTASENTER but accepts only numeric input. Used for quantities, amounts, counts. |
| **TTASComboEnter** | 3,622 | **Editable dropdown combo** — user can type a value or pick from a list. List is populated by TAS code at runtime. Common for codes (customer code, vendor code) where lookup is available. |
| **TTASCheckBox** | 1,948 | **Checkbox** — Y/N toggle. Stored as `.T.`/`.F.` or `Y`/`N` in underlying field. |
| **TTASDateEdit** | 1,380 | **Date entry with calendar picker** — specialized date input that validates format and opens a calendar popup. |
| **TTASComboBox** | 1,260 | **Dropdown-only combo** — user selects from list only (no free-text entry). Typically for fixed code sets. |
| **TTASDataGrid** | 423 | **Data grid / list view** — displays tabular records with selectable rows. Configured via TTASDGColTemplate children. Used for browse lists, order lines, journal lines. |
| **TTASStrList** | 138 | **Runtime string list** — acts as a data container/selector; TAS code pushes strings in at runtime. Used by the menu system (EVOERPMENU.DCY has 8) and various list-picker forms. |
| **TTASRadioButton** | 221 | **Radio button** — mutually exclusive option selector. Groups defined by TAS code. |
| **TTASMemo** | 32 | **Multi-line text area** — for notes, descriptions, multi-line input. |
| **TTASPageControl** | 72 | **Multi-tab form control** — contains multiple TTabSheet children. Used for tabbed screens (e.g. EVOFILTERS has 11 tabs). |
| **TTASNavigator** | 11 | **Record navigation buttons** — First / Previous / Next / Last navigator strip. Used in lookup/browse forms. |
| **TTASTimeEdit** | 20 | **Time entry with spinner** — specialized time input with up/down arrows. |
| **TTASTimeEnter** | 58 | **Time entry field** — simpler time input (type-in only, no spinner). |
| **TTASDGColTemplate** | 14 | **Grid column template** — child object of TTASDataGrid that defines one column (header, width, field binding). |

---

## TAS Pro 7 Infrastructure Controls

These controls handle runtime behavior rather than user data entry.

| Control | Count | Purpose |
|---|---|---|
| **TShellExe** | 850 | **Shell execution component** — triggers an external process or shell command from within a TAS form. Used for print (850 occurrences!), email send, open attached file, etc. Every form that prints or emails has at least one TShellExe. |
| **TRtnTimer** | 227 | **Return/timeout timer** — fires after a delay to automatically dismiss a form, poll for completion (e.g. T7JAVARUN), or trigger a background re-check. A very common pattern: loading forms use TRtnTimer to wait for data and then proceed. |
| **TTasBrowser** | 14 | **Embedded web browser** — renders an HTML URL or local HTML file inside the form. Used in EVOGETDATE for release notes and in help-adjacent forms. |
| **TAlarmClock** | 3 | **Alarm / scheduled timer** — fires at a specific time or after a countdown. Used in reminder/scheduler forms. |

---

## Chart Controls

EvoERP includes embedded charting (from the Addsum "TAS 7i Chart Demo" lineage).

| Control | Count | Purpose |
|---|---|---|
| **TBarChart** | 8 | Bar chart display |
| **TLineChart** | 4 | Line chart display |
| **TPieChart** | 10 | Pie chart display |

Chart forms: ChartDemo.DFM, ChartPieModal.DFM, chartBarModal.DFM, chartLineModal.DFM

---

## Standard Delphi VCL Controls

| Control | Count | Purpose |
|---|---|---|
| TLabel | 15,740 | Static text label — the most numerous control (one per field + headers + captions) |
| TGlyphBtn | 4,485 | Button with icon (glyph) — the standard EvoERP action button (Save, Exit, Browse, etc.) |
| TToolButton | 3,962 | Toolbar button — part of a TToolBar strip |
| TPanel | 2,996 | Container panel — groups controls, creates header bars |
| TToolBar | 1,559 | Toolbar strip container |
| TGradient | 715 | Gradient-filled background decoration |
| TSpeedButton | 479 | Standard flat speed button (alternative to TGlyphBtn) |
| TTabSheet | 320 | Single tab within a TTASPageControl |
| TGradientLabel | 299 | Label with gradient background (used for section headers) |
| TShape | 253 | Decorative shape (rectangle, circle, etc.) |
| TGroupBox | 245 | Group box with border and caption |
| TButton | 236 | Standard Windows push button |
| TMenuItem | 126 | Menu item within TMainMenu or TPopupMenu |
| TBevel | 105 | Visual dividing line |
| TImage | 102 | Static image display |
| TRxLabel | 88 | RxLib enhanced label (supports hyperlinks, multi-line, auto-resize) |
| TImageList | 796 | Image list for toolbar icons (not visible — just stores bitmaps) |
| TProgressBar | 16 | Progress bar (Windows standard) |
| TStatusBar | 38 | Status bar at bottom of form |
| TMainMenu | 56 | Main menu bar |
| TPopupMenu | 29 | Context/popup menu |
| TMemo | 21 | Standard Delphi multi-line text (TAS code uses TTASMemo; TMemo appears in non-TAS contexts) |
| TSpinEdit | 12 | Numeric spinner (value + up/down arrows) — used in PRINTTLL for copy count |
| TDualListDialog | 2 | Dual-pane list dialog (available/selected lists) |
| TGauge | 4 | Gauge/meter display |
| TControlBar | 2 | Resizable control bar (dockable toolbar host) |
| TAnimate | 3 | AVI animation control (used in T7CLOADING loading spinner) |
| TZipMaster | 2 | ZipMaster zip library component (EVOERPBACKUP backup forms) |

---

## Summary

| Category | Types | Notable |
|---|---|---|
| TAS Pro entry fields | 5 | TTASENTER, TTASNumEnter, TTASComboEnter, TTASDateEdit, TTASTimeEdit/Enter |
| TAS Pro display/list | 4 | TTASDataGrid, TTASStrList, TTASPageControl, TTASNavigator |
| TAS Pro toggle | 2 | TTASCheckBox, TTASRadioButton |
| TAS Pro runtime | 4 | TShellExe, TRtnTimer, TTasBrowser, TAlarmClock |
| Charts | 3 | TBarChart, TLineChart, TPieChart |
| Standard Delphi | ~25 | Label, Panel, GroupBox, ToolBar, etc. |
| Third-party | 3 | TRxLabel (RxLib), TZipMaster (ZipLib), TGlyphBtn |

**The most common field entry pattern in EvoERP:**
```
TLabel — field caption
TTASENTER — the field value (alpha)
  OR TTASNumEnter — numeric value
  OR TTASDateEdit — date value
  OR TTASComboEnter — code field with lookup
```

**TShellExe at 850 instances** is the key to understanding how EvoERP launches external operations —
every print, email, and file-open action in the UI is implemented as a TShellExe invocation in the DFM,
triggered by TAS Pro code.

**TRtnTimer at 227 instances** explains the "auto-dismiss" and "polling" behavior seen throughout EvoERP —
loading screens, Java wait screens, and reminder popups all use TRtnTimer to trigger automatic transitions.

---

## TAS Pro 7 Control Property Reference

Pass 399 (2026-06-30) — all properties confirmed from actual DFM files in samples/dfm/:
ACT7SHKNOTE.DFM (TTASENTER, TTASComboEnter, TTASComboBox),
ChartPieModal.DFM (TTASNumEnter),
CALREMGC.DFM (TTASDateEdit, TTASRadioButton),
EVOENOTES.DFM (TTASCheckBox),
DDFilters.DFM (TTASDataGrid).

### Common Properties (all TTAS* entry controls)

These properties appear on every entry control: TTASENTER, TTASNumEnter, TTASComboEnter, TTASDateEdit, TTASCheckBox, TTASRadioButton.

| Property | Type | Description |
|---|---|---|
| `FieldName` | String | TAS variable binding in dot notation (`table.field` or `prog.var`). This is what TAS code reads/writes when the field is entered or exited. |
| `DispPrgLoc` | Integer | Callback index in [Events] section for OnDisplay event. -1 = no handler. |
| `ClickPrgLoc` | Integer | Callback index for OnClick event. -1 = no handler; 0+ = index into [Events]. |
| `ChangePrgLoc` | Integer | Callback index for OnChange event (fires on each keystroke). |
| `PrePrgLoc` | Integer | Callback index for Pre-entry event (fires before user enters the field). |
| `PostPrgLoc` | Integer | Callback index for Post-entry event (fires after user leaves the field). |
| `ValidPrgLoc` | Integer | Callback index for ValidLabel (validation) event. |
| `ValidCheckOnExit` | Boolean | True = run ValidExpr when user exits this field. |
| `ValidUserEsc` | Boolean | True = allow user to Esc past a validation failure. False = strict. |
| `ValidExpr` | String | Inline TAS function/expression for validation (e.g. `'vld_wonum()'`). Empty = no inline validation. |
| `ValidExprLoc` | Integer | Location token for ValidExpr (0 = inline expression). |
| `ValidExprTyp` | Char | Type byte for ValidExpr; #0 = char zero (no type). |
| `Group` | Integer | Entry group number. Fields with the same non-zero group navigate together as a logical unit. 0 = ungrouped. |
| `NoClickOn` | Boolean | True = user cannot click into this field from elsewhere. |
| `NoClickOff` | Boolean | True = user cannot click out of this field to another. |
| `ReturnIsTab` | Boolean | True = Return key advances to next field (same as Tab). |
| `PreRetFalse` | Boolean | True = if Pre callback returns false, entry is aborted/skipped entirely. |
| `KeyTraps` | String | Key trap definitions: `'KEY|EVENTNAME'` pairs, e.g. `'F2|ENTERWONUM.CLICK'`. Multiple traps separated by `,`. |
| `EntryFont.*` | Font | Font applied while the control is in active-entry mode. Overrides display font. |
| `EntryBGColor` | TColor | Background color while in active-entry mode (e.g. `clWhite`). |
| `EntryUseDflt` | Boolean | True = use system default entry colors; ignores EntryFont/EntryBGColor. |
| `FldModified` | Boolean | Internal modified flag set by TAS runtime. True = field value changed since last save. |

### TTASENTER — Alphanumeric Text Field

| Property | Type | Description |
|---|---|---|
| `AllowedChrs` | String | Set of permitted input characters. Empty = all characters allowed. Example: `'0123456789 -{}'` restricts to digits, spaces, and delimiters. |
| `SelectStart` | Integer | Cursor position when field is entered. 0 = start of text. |
| `Text` | String | Initial text value (designer-set). Overridden at runtime by TAS. |

### TTASNumEnter — Numeric Entry Field

| Property | Type | Description |
|---|---|---|
| `AutoSize` | Boolean | True = control auto-sizes its width to the formatted value. |
| `FormatOnEditing` | Boolean | True = apply numeric format mask while user is still typing. |
| `FastSearchType` | Enum | Search type for linked table lookups: `fsNum` = numeric key search, `fsAlpha` = alpha search. Determines how F2/browse lookup matches. |

### TTASComboEnter — Editable Dropdown Combo

Same common properties plus:

| Property | Type | Description |
|---|---|---|
| `Glyph.Data` | Bitmap | Dropdown button icon (embedded bitmap). |
| `NumGlyphs` | Integer | Number of glyph states in the button image (1 = single state). |
| `AllowedChrs` | String | As per TTASENTER. |
| `SelectStart` | Integer | As per TTASENTER. |

The dropdown list is populated at runtime by TAS code (TAS program pushes items in); the DFM does not store static items.

### TTASComboBox — Dropdown-Only Combo

| Property | Type | Description |
|---|---|---|
| `Style` | Enum | `csDropDownList` = user can only select from list (no free-text). `csDropDown` = user can also type. |
| `ItemHeight` | Integer | Pixel height of each dropdown item. |
| `ItemIndex` | Integer | Currently selected item index (0-based). |
| `Items.Strings` | StringList | Static string items compiled into the DFM. Runtime items added by TAS code. |
| `ItemNumber` | Integer | Counter used by TAS runtime to track number of runtime-added items. |
| `DropDownPrgLoc` | Integer | Callback index for OnDropDown event (fires when list opens). |

### TTASDateEdit — Date Entry with Calendar

| Property | Type | Description |
|---|---|---|
| `BlanksChar` | Char | Character shown for blank date fields. `'0'` = display zeros in empty slots. |
| `NumGlyphs` | Integer | Number of glyph states on the calendar picker button (2 = normal/pressed). |
| `StartOfWeek` | Enum | First day of calendar week: `Sun` or `Mon`. |

Standard ValidExpr is commonly used here (e.g. `vld_date('F')` to validate a from-date).

### TTASCheckBox — Checkbox Toggle

| Property | Type | Description |
|---|---|---|
| `Caption` | String | Label text displayed beside the checkbox. |
| `TabStop` | Boolean | False = checkbox is skipped by Tab navigation. |

Checkbox value is a Y/N or .T./.F. flag stored in the FieldName variable. TAS code reads it as a boolean.

### TTASRadioButton — Radio Button

| Property | Type | Description |
|---|---|---|
| `Caption` | String | Label text displayed beside the radio button. |

Mutual exclusion is enforced by the `Group` property — all radio buttons with the same non-zero Group value are mutually exclusive. Only one can be selected at a time.

### TTASDataGrid — Data Grid / List View

| Property | Type | Description |
|---|---|---|
| `ColCount` | Integer | Number of columns. |
| `Options` | Set | Grid display flags: `goFixedVertLine`, `goFixedHorzLine`, `goVertLine`, `goHorzLine`, `goRowSelect`, etc. |
| `UpCase` | Boolean | True = auto-uppercase all text input in the grid. |
| `StartAtEnd` | Boolean | True = position cursor at end of text when editing a cell. |
| `PasswordChar` | Char | Mask character for password columns (typically `'*'`). |
| `PrePrgLoc` | Integer | Pre-row-entry callback index. |
| `PostPrgLoc` | Integer | Post-row-exit callback index. |
| `Navigation.AllowInsertRow` | Boolean | True = user can insert a new row. |
| `Navigation.AllowDeleteRow` | Boolean | True = user can delete the current row. |
| `Navigation.AdvanceOnEnter` | Boolean | True = Enter key advances to next cell. |
| `Navigation.AdvanceAtEnd` | Boolean | True = wrap navigation at end of row. |
| `Navigation.AdvanceDirection` | Enum | `adLeftRight` = navigate left/right; `adTopBottom` = navigate top/bottom. |
| `Navigation.AdvanceAuto` | Boolean | True = automatic advance on value entry completion. |
| `Navigation.InsertPosition` | Enum | `pInsertBefore` / `pInsertAfter` = new row inserts before or after current. |
| `Navigation.CursorWalkEditor` | Boolean | True = cursor keys walk through the editor text. |
| `MouseActions.ColSelect` | Boolean | True = allow column-header click to select a column. |
| `MouseActions.RowSelect` | Boolean | True = allow row click to select a row. |
| `MouseActions.DirectEdit` | Boolean | True = single click activates cell for editing. |
| `MouseActions.DirectComboDrop` | Boolean | True = single click on combo cell drops down the list. |
| `MouseActions.CaretPositioning` | Boolean | True = mouse click positions text caret within cell. |

#### TTASDataGrid Columns

Each column is a child `item` in the `Columns` collection:

| Column Property | Type | Description |
|---|---|---|
| `Header` | String | Column header text. |
| `Width` | Integer | Column width in pixels. |
| `Alignment` | Enum | `taLeftJustify`, `taRightJustify`, `taCenter`. |
| `Color` | TColor | Cell background color. |
| `Font.*` | Font | Cell font. |
| `Editor` | Enum | Cell editor type: `edText` (text), `edComboList` (dropdown), `edSpin` (spinner), `edMemo` (multi-line). |
| `Fixed` | Boolean | True = column is frozen (no horizontal scroll). |
| `ReadOnly` | Boolean | True = column is display-only. |
| `Password` | Boolean | True = column masks input with `PasswordChar`. |
| `ComboItems.Strings` | StringList | Static items for `edComboList` columns. |
| `ComboItemsSort` | Boolean | True = sort combo items alphabetically. |
| `SpinMin` / `SpinMax` / `SpinStep` | Integer | Range and step for `edSpin` columns. |
| `EditLength` | Integer | Max characters for text columns (0 = unlimited). |
| `Borders` | Set | Cell border flags. |

### TTASStrList — Runtime String List

TTASStrList has no designer-visible data properties. Its position (Left/Top) is set in the DFM, but all content is injected at runtime by TAS code via the `msg_list` / `ENT_LIST` keywords or direct string-push operations. It acts as an invisible data container accessible via a TAS program variable.

---

## Key Patterns

### The *PrgLoc callback system

All `*PrgLoc` properties (DispPrgLoc, ClickPrgLoc, ChangePrgLoc, PrePrgLoc, PostPrgLoc, ValidPrgLoc) are integer indexes into the `[Events]` section of the same DFM. Value -1 means no handler registered. Value 0 or positive is an index into the ordered list of event handlers. This mirrors the T7 bytecode event model (opcodes 8070–8095) documented in src-tas-pro-language.md.

### PrgLoc vs ValidExpr

Two independent validation mechanisms exist on every field:
- `ValidExpr` — an inline TAS expression evaluated by the runtime (fast, no roundtrip)
- `ValidPrgLoc` — a full TAS callback function registered in [Events] (full program logic)

Both can coexist. ValidExpr runs first; if it passes, ValidPrgLoc fires.

### KeyTraps format

`KeyTraps = 'F2|ENTERWONUM.CLICK'` means: when the user presses F2 while in this field, fire the ENTERWONUM control's Click event. Multiple traps are comma-separated: `'F2|FIELD.CLICK,ESC|EXIT_LABEL'`. This is the DFM equivalent of the T6-era `trap F2 GOSUB LABEL` syntax.
