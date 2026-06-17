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
