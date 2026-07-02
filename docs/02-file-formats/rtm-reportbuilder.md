# `.RTM` / `.btm` — Nevrona ReportBuilder Template

Status: verified — header structure confirmed from
`../../samples/rtm/t7ing1.rtm` and `../../samples/btm/I2SCHK1.btm`.

## Format

`.RTM` files are **Delphi binary form streams** (TPF0 format) holding
a **Nevrona ReportBuilder** `TppReport` component tree. A `.btm` is
ReportBuilder's automatic save-backup: when the designer saves, it renames
the old `.RTM` to `.btm` before writing the new version — identical format,
byte-for-byte identical when the last save was a no-change re-save.
Confirmed: `ENCOB3B.btm` = `ENCOB3B.RTM` (147047 bytes, `TPF0` magic, identical content — Pass 352).

First 4 bytes:
```
54 50 46 30   'TPF0'
```

After the magic, the body follows the standard Delphi binary component
serialization (same encoding as a compiled Delphi DFM). The top-level
class is `TppReport` with name `ppReport1`, then nested
`TppDataPipeline`, `TppDetailBand`, `TppDBText`, `TppLabel`,
`TppShape`, `TppSubReport`, `TppChildReport`, etc.

## Why text-y strings appear in the dump

Binary Delphi streams encode property-name and class-name strings as
length-prefixed ASCII. A naive hex dump shows those strings legibly
while the numeric property values read as gibberish.

Observed classes in one sample (`I2SCHK1.btm` — an AP check printing
template):

```
TppReport, TppDetailBand, TppSubReport, TppChildReport,
TppShape, TppLabel, TppDBText
```

Properties captured:
- `Template.FileName` — sibling RTM referenced from within
  (e.g. `T:\I2SCHK1.RTM`, `C:\SOURCE\apr99\Bkapha1.rtm`).
- `DataPipelineName` — a named `TASFile` pipeline that the TAS program
  binds to (e.g. `BKAP.CHK.INVDTE`, `BKAP.CHK.AMTPD`).
- `PrinterSetup.*` — paper, margins, printer name.
- `DeviceType` — `Screen` / `Printer` / `TextFile`.
- `OutlineSettings.*` — PDF outline / bookmarks.
- `TextSearchSettings.*` — preview search.

## How the TAS program calls it

The TAS 4GL runtime has first-class `.RTM` support via these keywords
(seen in `tp7runtime.keywords.txt`):

- `EXEC_RB` — "execute ReportBuilder" — hand off control.
- `RTM_FN <filename>` — specify the RTM to use.
- `REPORTNAME`, `USE_PRINTER`, `PRINT_TO_FILE`,
  `NOPRINTWHRDIALOG`, `PRINT_CANCEL`, `PRINT_ARCHIVE`.
- The source program sets up a "TASFile" data pipeline via
  `OUTPUT_REPORT_DATA` / `UPDATE_REPORT_DATA` / `SETUP_REPORT_BUFF`
  and then hands off to ReportBuilder.

## Designer

`C:\ISTS\RBDsgnr.exe` (6.2 MB) is **Nevrona ReportBuilder's
stand-alone designer**, used to open and edit `.RTM` files. Its
settings are persisted in `C:\ISTS\RBuilder.ini`.

## Data pipeline

When an RTM says `DataPipelineName = TASFile`, it's referring to a
TAS-specific pipeline component built into the runtime. The
data-field strings in the RTM (e.g. `BKAP_CHK_INVNUM`,
`BKAP.CHK.AMTPD`) are TAS field names. At run time, the TAS program
fills a buffer with one record per report row and the pipeline pushes
those into the bound `TppDBText` / `TppDBMemo` fields.

## RTM caller catalog (Pass 104, 2026-06-18)

Source: `samples/rtm_callers.csv` — extracted from all .RUN and .RWN string dumps.

**Total: 403 unique RTM files** called from across the EvoERP program set.

### Naming convention

| Prefix | Count | Meaning |
|--------|-------|---------|
| `T6*` | 146 | TAS Pro 6-era standard DBA report templates |
| `BK*` | 114 | Btrieve/DBA legacy standard report templates |
| `it6*` | 36 | i2 Systems customized T6 reports (`i` prefix + T6xxx) |
| `ibk*` | 27 | i2 Systems customized BK reports (`i` prefix + BKxxx) |
| `J6*` | 20 | i2 Systems custom J6-program reports |
| `JM*` | 12 | i2 Systems custom JM-program reports |
| `IS*` | 8 | i2 Systems Information System reports |
| `T7*` | 4 | TAS Pro 7-era reports (rare — T7 uses DFM+RWN) |
| `J5*` | 4 | i2 Systems J5-program reports |
| Other | ~32 | Shared libraries, utilities, tests |

**i2 customization naming:** `ibkpob1.rtm` = **i**2-**B**K-**P**urchase**O**rder-**B**-1.
i2 took standard DBA templates and prefixed `i` to make their customized versions.

### High-reference shared library RTMs

| RTM file | Callers | Role (inferred) |
|----------|---------|----------------|
| `cfg.rtm` | 792 | **Global config** — virtually every report uses this. Contains company name, address, and report-wide layout constants. |
| `ent.rtm` | 90 | **Enterprise layout** — mainly custom J6/i2 programs. |
| `t6.rtm` | 40 | **T6-era shared component** — mixed AR/PO/SO/WO callers. |
| `temp.rtm` | 30 | **Temp/staging template** |
| `bk.rtm` | 23 | **BK-era shared component** |
| `banks.rtm` | 16 | **Bank / check layout** — AP check printing + bank reconciliation. |
| `dflt.rtm` | 16 | **Default layout** — inventory and sales reports. |

### RTM variants (print format selection)

Programs often have 3–4 numbered RTM variants. The `T7RTMVALID.DFM` "Select Report Format
Name" dialog (identified Pass 103c) lets users pick among them at runtime:
```
it6pob1.rtm .. it6pob4.rtm  (T6POB — PO print, 4 layouts)
ibkpob1.rtm .. ibkpob4.rtm  (BKPOB — same 4 for BK-era program)
it6sob1.rtm .. it6sob3.rtm  (T6SOB — SO print, 3 layouts)
```

### Module-to-RTM mapping (Pass 106, comprehensive)

RTM counts derived from `samples/rtm_callers.csv` (excludes the 7 globally-shared templates).
Caller programs mapped by program-name prefix (BKSOx = SO module, T6SOx = T6-era SO module, etc.).

| Module | Unique RTMs | Example RTM files |
|--------|-------------|-------------------|
| SO (Sales Orders) | 82 | `bksob1..4`, `ibksob1..4`, `it6sob1..3`, `bksohlot.rtm`, `bksod1..3` |
| i2 Systems custom (J5/J6/JM/IS*) | 50 | `j6inv1.rtm`, `jmwoc1.rtm`, `is*.rtm` |
| SR (Service/Repair) | 28 | `ibkrma1.rtm`, `it6rma1.rtm`, `sr*.rtm` |
| AR (Accounts Receivable) | 23 | `bkare1..4`, `bkari1..3`, `bkarg1..2`, `abk.rtm`, `at6.rtm` |
| AP (Accounts Payable) | 22 | `bkapha1..4`, `bkaph1..2`, `bkapm1..4`, `bkaps1..3` |
| PO (Purchase Orders) | 21 | `ibkpob1..4`, `it6pob1..4`, `bkpob*.rtm` |
| WO (Work Orders) | 11 | `bkwoc1..2`, `cenwoc1.rtm`, `ct6woc1.rtm`, `bkawc1..2` |
| IN (Inventory) | 7 | `ino.rtm`, `bkactrptbkac.rtm` |
| CM (CRM/Contact Manager) | 4 | `bkcm*.rtm` |
| PR (Payroll) | 4 | `bkprd1..3`, `bkprdpst.rtm` |
| LC (Landed Cost) | 2 | `islcf1.rtm`, `islce1.rtm` |
| AC (Activity Control) | 1 | `bkac.rtm` |
| Other (GL, BM, SH, DE, MR, PI, ES, DC, JC…) | 182 | Various module-specific reports |

**Total unique non-global RTMs: ~396** (403 total − 7 global shared = 396).

### Module-to-RTM detailed examples

| Module/Operation | Programs | RTM files called |
|-----------------|----------|-----------------|
| AP-H Print Checks | BKAPHA, T6APHA | `bkapha1.rtm`, `bkapha2.rtm`, `bkapha3.rtm`, `banks.rtm`, `cfg.rtm` |
| AP-J Bank Reconciliation | BKADC | `bkaph1.rtm`, `bkapha1.rtm`, `banks.rtm`, `ap.rtm`, `cfg.rtm` |
| AR-C Invoice Print | BKARI, T6ARI | `bkari1.rtm`, `bkari2.rtm`, `bkari3.rtm`, `cfg.rtm` |
| AR-E Print Statements | BKARE, T6ARE | `abk.rtm`, `at6.rtm`, `bk.rtm`, `t6.rtm`, `cfg.rtm` |
| AR-I AR Aging | BKARG, T6ARG | `cfg.rtm` (plus inline from program) |
| PO-B Print PO | BKPOB, T6POB | `ibkpob1..4.rtm`, `it6pob1..4.rtm`, `bk.rtm`, `temp.rtm`, `cfg.rtm` |
| SO-B Print SO | BKSOB, T6SOB | `ibksob1..4.rtm`, `it6sob1..3.rtm`, `bk.rtm`, `temp.rtm`, `cfg.rtm` |
| WO-C Print Traveler | BKWOC, T6WOC | `cenwoc1.rtm`, `ct6woc1.rtm`, `bk.rtm`, `t6.rtm`, `cfg.rtm` |
| RMA Print | ISSRB | `ibkrma1.rtm`, `it6rma1.rtm`, `cfg.rtm` |
| PR Payroll | BKPRD, T6PRD | `bkprd1.rtm`, `bkprd2.rtm`, `bkprd3.rtm`, `banks.rtm`, `cfg.rtm` |

### cfg.rtm — status note

`cfg.rtm` is referenced by **792 of 403 unique program callers** (virtually every print operation).
It is loaded via ReportBuilder's `Template.FileName` property inside other RTM files — acting as
a **shared page header/footer template** (likely company name, logo, address, page border).

**Path resolution (Pass 106i):** RTM samples confirm that `Template.FileName` paths use **`T:\`
drive mapping**, not hardcoded UNC paths. Examples confirmed from binary inspection:
- `I2SCHK1.btm` → `Template.FileName = T:\I2SCHK1.RTM`
- `t7ing1.rtm` → `Template.FileName = C:\TASPRO7\DBA7\t7ing1.rtm` (self-referential, local install)

`T:\` is a per-workstation drive letter mapping that resolves to the network share.
`cfg.rtm` is almost certainly at `T:\cfg.rtm`, meaning it lives at the **root of the `T:\` drive**
on the network share — the directory that `T:\` maps to. Physical file not found via UNC walk
because the drive-letter root differs from the `\\i2s109-solidcrm\DBAMFG$\` subfolder scanned.
`C:\ISTS\RBuilder.ini` was checked — it contains only UI layout settings, no template paths.

---

## Report parameter passing (TAS pipeline mechanism)

The TAS → ReportBuilder data flow is a **push model**:

1. **Setup buffer** — TAS program sets up the data pipeline buffer:
   ```
   SETUP_REPORT_BUFF <buffer_name>
   ```
   This defines the TASFile pipeline that the RTM's `TppDataPipeline` will consume.

2. **Populate buffer** — TAS loads records and calls:
   ```
   OUTPUT_REPORT_DATA <field_list>
   ```
   or
   ```
   UPDATE_REPORT_DATA <field_list>
   ```
   This pushes records into the pipeline. Each call = one row in the report.

3. **Execute report** — TAS triggers rendering:
   ```
   RTM_FN <filename.rtm>
   EXEC_RB
   ```
   ReportBuilder reads all buffered rows and renders the report.

4. **Print control** — TAS sets print destination before EXEC_RB:
   ```
   USE_PRINTER         ; print to configured printer
   PRINT_TO_FILE       ; print to C:\ISTS\PDFS\ (PDF archiving)
   NOPRINTWHRDIALOG    ; suppress "Where to print?" dialog
   PRINT_CANCEL        ; cancel any pending print job
   PRINT_ARCHIVE       ; archive copy to PDF
   ```

**Report filters/date ranges:** Set as TAS variables before the push loop:
- Date range: set `rpt_start_date` / `rpt_end_date` (or equivalent named vars) before
  the first `OUTPUT_REPORT_DATA` call. The TAS program filters records in its own loop;
  only matching records are pushed to the pipeline.
- Sort order: TAS sorts the Btrieve record set using `sorta <key>` before iterating.
- There is no parameterized query layer — all filtering is TAS-side before RTM rendering.

**Multi-section reports** use sub-reports (TppSubReport / TppChildReport in the RTM tree).
TAS calls `SETUP_REPORT_BUFF` multiple times with different buffer names for different sections.

---

## Print destination modes

| TAS keyword | ReportBuilder DeviceType | Behavior |
|-------------|--------------------------|---------|
| `USE_PRINTER` | `Printer` | Print directly to Windows default printer |
| `PRINT_TO_FILE` | `TextFile` | Output to `C:\ISTS\PDFS\<filename>.pdf` |
| (default) | `Screen` | Show in ReportBuilder preview window |
| `PRINT_ARCHIVE` | `Printer` + archive | Print AND save a PDF archive copy |

PDF path: `C:\ISTS\PDFS\` — created by `USE_PRINTER` / `PRINT_ARCHIVE` per workstation.

---

## PRINTTLL.DFM — universal print dialog (Pass 401)

`Source: samples/dfm/printtll.DFM` — `SourceFile = 't7print'`, `Caption = 'Print'`

**All print jobs in EvoERP that require user interaction are routed through this single shared dialog.** It is invoked by a `mount printtll type R` call from the calling program.

### Print mode selection (GroupBox2 "Print Options")

Four `TTASRadioButton` controls, all in `Group = 0`, bind to the `print_opt[N]` TAS variable array:

| Index | FieldName | Caption | Default | Effect |
|-------|-----------|---------|---------|--------|
| 1 | `print_opt[1]` | P&review | `Checked = True` | Open report in ReportBuilder preview window |
| 2 | `print_opt[2]` | &Printer | — | Send directly to selected printer |
| 3 | `print_opt[3]` | &Email | — | Reveal EmailPanel; send via SMTP |
| 4 | `print_opt[4]` | &File | — | Enable PrintToFileGrp; save to disk file |

`ChangePrgLoc = 0` on all four — selecting any radio fires TAS event handler [0] which shows/hides the conditional UI sections.

### Printer section (GroupBox3 "Printer")

- `PrinterNameEnter` (TTASENTER) — `FieldName = 'dflt.printer'`, `TabStop = False` — displays selected printer name (read-only display; selection via `SetupPrinterBtn`)
- `SetupPrinterBtn` (TButton) — Caption = 'Setup' — opens Windows printer setup dialog

### Copies section (GroupBox1 "Copies")

- `SpinEdit1` (TSpinEdit) — MaxValue = 99, MinValue = 1, Value = 1

### Print to File section (PrintToFileGrp)

Initially `Enabled = False`. Enabled by TAS code when `print_opt[4]` (File) is selected.

- `cbPrintType` (TTASComboBox) — `FieldName = 'prt.file.type'` — file format selection (PDF, CSV, etc.; items populated at runtime)
- `cbEnterPath` (TTASComboEnter) — `FieldName = 'fpath'`, `GlyphKind = gkEllipsis` — output file path with "..." browse button

### Email section (EmailPanel)

Initially `Visible = False`. Made visible by TAS code when `print_opt[3]` (Email) is selected.

- `AutoEmail` (TTASCheckBox) — `FieldName = 'autoemail'` — "Auto Send Email" — if checked, sends without user confirmation
- Contact selection (GroupBox4):
  - `ContName` (TTASRadioButton) — `FieldName = 'contname'`, default checked — look up recipient by contact **name**
  - `ContNum` (TTASRadioButton) — `FieldName = 'contnum'` — look up recipient by contact **number**
  - `PrimCode` (TTASENTER) — `FieldName = 'contprimcode'`, default `Text = 'B'` — primary contact code prefix; `FocusOnObject = 'spinemail'` (on completion, focus jumps to SpinEmail)
  - `SpinEmail` (TSpinEdit) — MaxValue = 5, MinValue = 1 — selects contact email slot 1–5

### Buttons

- `SaveSettingsBtn` (TGlyphBtn) — Caption = '&Save Settings' — persists current print settings as user default
- `OkBtn` (TButton) — Caption = '&Ok' — executes print with current settings
- `CancelBtn` (TButton) — Caption = 'E&xit'

### TAS variable bindings summary

| TAS variable | Field | Meaning |
|---|---|---|
| `print_opt[1]` | PreviewRadioBtn | Preview mode active |
| `print_opt[2]` | PrinterRadioBtn | Printer mode active |
| `print_opt[3]` | EmailRadioBtn | Email mode active |
| `print_opt[4]` | FileRadioBtn | File mode active |
| `dflt.printer` | PrinterNameEnter | Selected printer name |
| `prt.file.type` | cbPrintType | Output file format |
| `fpath` | cbEnterPath | Output file path |
| `autoemail` | AutoEmail | Auto-send without confirm |
| `contname` | ContName | Use contact name for email lookup |
| `contnum` | ContNum | Use contact number for email lookup |
| `contprimcode` | PrimCode | Contact primary code (default 'B') |

### Event flow

1. Dialog opens → `OnStart = 'PRTTLL.START'` fires (loads saved settings into `print_opt[N]`, `dflt.printer`, etc.)
2. User selects print mode → `ChangePrgLoc = 0` fires per radio change — shows/hides EmailPanel, enables/disables PrintToFileGrp
3. User clicks Ok → `t7print` source evaluates `print_opt[N]` and calls `USE_PRINTER` / `PRINT_TO_FILE` / email dispatch / file save accordingly
4. Dialog closes → `OnClose = 'PRTTLL.END'` fires

---

## Email and PDF archiving workflow (Pass 402)

### Email subsystem — three DFM layers

#### 1. EMAILREL4.DFM — per-workstation SMTP settings (SourceFile=`emailrel4`)

Accessed from workstation setup; stores connection params in the `email.cfg.*` TAS namespace:

| Field | TAS variable | Default | Meaning |
|---|---|---|---|
| `smtp` (TTASENTER) | `email.cfg.SMTP` | — | SMTP server hostname |
| `email` (TTASENTER) | `email.cfg.Email` | — | Sender email address |
| `name` (TTASENTER) | `email.cfg.Name` | — | Sender display name |
| `smtpport` (TSpinEdit) | *(integer)* | 25 | SMTP port (1–65535) |
| `TestEmail` (TGlyphBtn) | — | — | Sends a test email to verify settings |

Events: `emailrel4.OnStart` / `emailrel4.OnClose`. `OpenFiles = 'emailrel4.OnOpenFiles'` (loads BKYSMSTR config on open).

Full `EMAIL.CFG.*` namespace in BKYSMSTR (23 vars confirmed from t7slsfc): SMTP/PORT/SEC/EMAIL/NAME/USER/PASS/EPASS/EFAIL/ECB/EVB/APTH/BCC/SUBJ/BOD1-9.

#### 2. nzedefs.DFM — global email defaults (SourceFile=`nzemdefs`)

Admin-configurable defaults applied to all outgoing emails:

| Field | TAS variable | Meaning |
|---|---|---|
| `bccSelf` (TTASENTER) | `entBCC` | BCC self address; ValidExpr=`"@" $ entBCC .and. "." $ entBCC` |
| `SUBJ` (TTASENTER) | `entSUB` | Default subject line template |
| `SubjectFields` (TTASComboBox, hidden) | `entSubjectField` | Field substitution picker for subject |
| `Body` (TMemo, 3600 chars max) | *(body lines stored as BOD1-9 in BKYSMSTR)* | Default body text (60 lines × 60 chars) |
| `SIGN` (TMemo, 200 chars max) | *(stored as SIG1-9 in BKYSMSTR)* | Signature (5 lines × 40 chars) |
| `APATH` (TTASComboEnter, gkEllipsis) | `entAPATH` | Default attachment path |
| `Fields` (TTASComboBox, hidden) | `entFIELD` | Field substitution picker for body |

`OnDisplayScreen = 'nzedefs.OnDisp'` — validates email format on display.

#### 3. nzemailtll.DFM — email compose form (SourceFile=`NzEmailtll`)

Caption = ' Evo ~ ERP email'. Mounted when user selects Email mode from print dialog or from menu.

| Field | TAS variable | Meaning |
|---|---|---|
| `entTO` (TTASENTER) | `entTO` | To: address(es) |
| `entCC` (TTASENTER) | `entCC` | Cc: address(es) |
| `entICC` (TTASENTER) | `entICC` | Icc: (internal CC — company users) |
| `entSUB` (TTASENTER) | `Email.cfg.subj` | Subject line |
| `TASComboBox1` (TTASComboBox) | `TEMPATT` | Email form/template name |
| `tmpATT` (TTASENTER) | `tempATT` | Attachment template path |
| `attach` (TTASENTER) | `fpath` | Actual attached file path |
| `Name` (TTASENTER) | `name` | Recipient contact name |
| `TASCheckBox1` (TTASCheckBox) | `bccself` | BCC self |
| `emaillist` (TTASDataGrid) | `EMAILLIST` / `EMAILLBL` / `CONTNAME` | Recipient grid: email address, display label, contact name |
| `ICCLIST` (TTASDataGrid) | `ICCLIST` / `ICCNAME` | ICC grid: internal CC email, ICC contact name |
| `msglist` (TTASStrList) | *(runtime body)* | Email body text |
| `NOTEMEMO` (TTASStrList) | *(runtime note)* | Note/memo attachment content |

Events: `OnStart = 'NZE.START'` (pre-populates recipient from contact lookup), `OnClose = 'NZE.END'`.

**Email → print flow:**
1. User selects `print_opt[3]` (Email) in PRINTTLL and optionally sets contact lookup fields
2. `t7print` resolves email recipient from `contname`/`contnum`/`contprimcode` + `SpinEmail` (1–5 contact slots)
3. If `autoemail = True` → sends without opening compose dialog
4. If `autoemail = False` → mounts `nzemailtll` for user to review To/Cc/Subject/Body before sending

### PDF archiving

TAS keyword `PRINT_ARCHIVE` (opcode ~7943) in the calling program's print sequence:
- Prints AND saves a PDF copy simultaneously
- PDF files written to `C:\ISTS\PDFS\` (per-workstation local path)
- Format: `<reportname>_<date>.pdf` (naming from t7print logic — blocked by encryption)
- `PRINT_TO_FILE` (opcode 7874) alone saves to `fpath` without printing

**Archive vs email:**
- Archive = automatic silent copy to `C:\ISTS\PDFS\` (no user interaction)
- Email = sends the rendered output via SMTP to a contact address

---

## TppDBText field binding format (Pass 106i)

Confirmed from `I2SCHK1.btm` binary inspection — two field name formats appear in the same RTM:

| Format | Example | When used |
|--------|---------|-----------|
| Underscore (`BKAP_CHK_INVNUM`) | `BKAP_CHK_INVNUM`, `BKAP_CHK_AMTPD` | Column header / label binding |
| Dot (`BKAP.CHK.AMTPD`) | `BKAP.CHK.AMTPD`, `BKAP.CHK.DISC`, `BKAP.VENDNAME` | TASFile pipeline data binding |

The underscore form is the SQL column alias (used when the data is accessed via Pervasive ODBC/SQL).
The dot form is the TAS 4GL field name (used when data is pushed via `OUTPUT_REPORT_DATA`). Both
forms can appear in the same RTM because TppDBText can bind to either ODBC or TASFile pipelines.
For EvoERP runtime printing (not ODBC), the dot form is the operative binding.

## Complete module-to-RTM breakdown (Pass 106i)

Full count from `samples/rtm_callers.csv` (403 unique RTMs), categorized by 2-letter module code:

| Module | RTMs | Key RTM names |
|--------|------|--------------|
| SO — Sales Orders | 103 | bksob1–4, ibksob1–4, it6sob1–3, bksohlot, bksod1–3 |
| SR — Service/Repair | 52 | bksrb1–4, ibksrb1–4, bksrma1–2, t6srb1–4 |
| PO — Purchase Orders | 32 | bkpob1–4, ibkpob1–4, it6pob1–4, t6pob1–4 |
| AP — Accounts Payable | 27 | ap, bkaph1–2, bkapha1–4, bkapm1–4, bkaps1–3 |
| AR — Accounts Receivable | 25 | bkare1–4, bkari1–3, bkarg1–2, abk, at6 |
| J6 — i2 custom J6 programs | 20 | j6bkmdis, j6bkmrep, j6btsrwo, j6cfclbl, j6inv1 |
| WO — Work Orders | 14 | bkwoc1–3, bkawc1–2, cenwoc1, ct6woc1, bkwoc3oc |
| PR — Payroll | 12 | bkprd1–3, bkprlf1, bkprlg1, bkprd1–3, banks |
| JM — i2 custom JM programs | 12 | jm6use1–2, jmcelesc, jmcfilbl, jmwoc1 |
| IN — Inventory | 11 | bking1, bkinlj1, ing, ino, bkactrptbkac |
| IS — i2 Info Systems | 11 | isdca1, islcf1, isscf1, isudmstrtemp |
| CM — CRM/Contact Mgr | 9 | bkcmbd1–3, bkcmaccctemp |
| SA — Sales Analysis | 7 | bksa, bksam1, bksan1, bksareptbksa |
| DC — Data Collection | 5 | bkdce, bkdcf, t6dcd1, t6dce |
| ES — Estimating | 5 | bkesd1–2, esteetag, t6esd1 |
| AW — Activity/Labor | 4 | bkawc1–2, bkawe1–2 |
| J5 — i2 custom J5 programs | 4 | j5ebisam, j5ntwolk, j5smrpt3, j5twiinv |
| AS — Assembly | 4 | t6asob3, t6asoc3, t6asof3, t6asopb3 |
| PI — Physical Inventory | 3 | bkpica1, t6pica1, t6pif1 |
| GL — General Ledger | 2 | t6glc1, t6glo1 |
| AM — Asset Management | 2 | t6amf, t6amf1 |
| AC — Activity Control | 2 | bkac, bkactrptbkac |
| BM — Bill of Materials | 1 | t6bmb1 |
| JC — Job Cost | 1 | t6jca1 |
| Shared library | 7 | cfg, ent, t6, bk, dflt, banks, temp |

**Total: 403 unique RTMs across 24+ modules.**

SA (Sales Analysis) is the largest underdocumented module (7 RTMs). DC/ES/AW/AS each have 4–5.
GL/BM/JC/AM have few RTMs because those modules use TAS-native reports more than ReportBuilder.

## Pass 225 — Binary analysis of t7ing1.rtm (Inventory Label/Barcode report, 2026-06-23)

`samples/rtm/t7ing1.rtm` is the Inventory item label report (`IN` module, prints barcoded
item labels with UPC, lot, and serial barcodes).

### Confirmed DataPipeline path

```
DataPipeline = Form1.TASFile
DataPipelineName = TASFile
```

Both properties appear — `DataPipeline` holds the fully-qualified component path
(`Form1.TASFile`), `DataPipelineName` holds the short name. TAS binds the data to
the component named `TASFile` on `Form1`.

### Array field binding notation confirmed

`TppDBText.DataField` supports bracket notation for array elements:

```
MTIC.PROD.RCOST[6]    ← cost element 6 from the RCOST array field
MTIC.PROD.SPECS[1]    ← specification string 1
MTIC.PROD.SPECS[2]    ← specification string 2
PTD.ARRAY[1..3]       ← period-to-date array elements
```

This means the `OUTPUT_REPORT_DATA` call must deliver array element values
under these subscripted names, or the TAS runtime flattens arrays into
indexed field names before pushing to the pipeline.

### TppDBBarCode — barcode component properties

t7ing1.rtm contains three barcode sections (LOT BARCODE, SERIAL BARCODE, UPC label):

| Property | Example value | Meaning |
|----------|--------------|---------|
| `BarCodeType` | `bcCode39` | Code 39 (3-of-9) barcode type |
| `mmBarWidth` | (numeric) | Narrow bar width in mm |
| `mmWideBarRatio` | (numeric) | Wide:narrow bar ratio |
| `BarColor` | `clBlack` | Ink color |
| `PrintHumanReadable` | T/F | Print digits below barcode |
| `CalcCheckDigit` | T/F | Auto-compute check digit |

`DataField` for barcode = same TAS dot-notation field name (e.g. `mtlot.lot`, `mtser.serial`).

### TppDBImage — image component properties

| Property | Meaning |
|----------|---------|
| `GraphicType` | Image type (`Bitmap`, `Metafile`, etc.) |
| `ImageReg` | Registry key for image data |
| `MaintainAspectRatio` | T/F |
| `Bitmap` | (binary blob for embedded image) |
| `Stretch` | Scale to fill bounds |

### Component naming convention confirmed

All component instances follow a `pp<ClassName><N>` pattern (lowercase `pp` prefix):

| Component class | Instance naming | Example |
|-----------------|----------------|---------|
| `TppReport` | `ppReport1` | root report |
| `TppDetailBand` | (child of ppReport1, no prefix) | `DetailBand1` |
| `TppSubReport` | `ppReport1SubReport1` | nested sub-report |
| `TppChildReport` | `ppReport1ChildReport1` | child report inside sub-report |
| `TppGroup` | `ppReport1Group1` | grouped section |
| `TppGroupHeaderBand` | `ppReport1GroupHeaderBand1` | group header |
| `TppGroupFooterBand` | `ppReport1GroupFooterBand1` | group footer |
| `TppDBText` | `ppDBText1`, `ppDBText2`… | data-bound text fields |
| `TppLabel` | `ppLabel1`, `ppLabel2`… | static text |
| `TppShape` | `ppReport1Shape1` | line/rectangle/ellipse |
| `TppDBBarCode` | `ppDBBarCode1`, `ppDBBarCode2`… | barcode |
| `TppDBImage` | `ppDBImage1`, `ppDBImage2`… | image |
| `TppRegion` | `ppRegion1`…`ppRegion4` | layout region container |
| `TppPageStyle` | `ppPageStyle1` | page-level style (margins, etc.) |
| `TppParameterList` | `ppParameterList1` | runtime parameter inputs |

### Field bindings extracted from t7ing1.rtm

All `DataField` values found in the binary (dot-notation TAS names):

```
BKIC.PROD.AVGC   BKIC.PROD.CAT    BKIC.PROD.CLASS  BKIC.PROD.CODE
BKIC.PROD.DESC   BKIC.PROD.ISUPC  BKIC.PROD.LSTC   BKIC.PROD.NOTE
BKIC.PROD.PRICE  BKIC.PROD.RAMT   BKIC.PROD.RLVL   BKIC.PROD.TYPE
BKIC.PROD.UM     BKIC.PROD.UOH    BKIC.IS.DCODE

MTIC.PROD.CLDES  MTIC.PROD.CUBFT  MTIC.PROD.CUSNM  MTIC.PROD.CUST
MTIC.PROD.CYCLE  MTIC.PROD.DELBF  MTIC.PROD.DRAW   MTIC.PROD.EXPBF
MTIC.PROD.LEAD   MTIC.PROD.LOC    MTIC.PROD.RCOST[6]
MTIC.PROD.REV    MTIC.PROD.SPECS[1]  MTIC.PROD.SPECS[2]  MTIC.PROD.STDPK  MTIC.PROD.WT

mtlot.lot        mtser.serial
```

ODBC underscore variants (same fields, SQL alias form) also appear:
`prod_code`, `prod_desc`, `prod_class`, `prod_type`, `prod_avgc`, etc.

### ReportBuilder version

String `7.03` appears near the component header — this is the ReportBuilder engine
version embedded in the template file.

---

## Computed vs. DDF field names in TASFile pipeline (Pass 322, 2026-06-24)

Confirmed from binary analysis of `samples/rtm/BKAPH1.RTM` and `samples/rtm/BKAPHA1.RTM`
(AP check print templates).

### Two categories of DataField values in a single RTM

Within a single RTM file, `TppDBText.DataField` carries two distinct kinds of names:

| Category | Example values | Source |
|----------|---------------|--------|
| **DDF field names** | `BKAP_CHK_INVNUM`, `BKAP_CHK_AMTPD`, `BKAP_CHK_DISC`, `BKAP_CHK_INVDTE`, `BKAP_VENDNAME`, `BKAP_CUST_CODE` | Direct Btrieve DDF columns; TAS pushes these verbatim from the open BKAPCHKF/BKAPVEND record |
| **Computed field names** | `CHK_DATE`, `CHK_NUM`, `CHK_AMT_DOL`, `LINE_DESC`, `TOT_AMT`, `TOT_DAMT`, `TOT_RAMT`, `TOT_TOT`, `PRT_ADD1`, `PRT_ADD2`, `PRT_CSZ`, `PRT_COUNTRY`, `CHECK_INVNUM` | Runtime-computed values staged into the TASFile pipeline buffer by the TAS program before `EXEC_RB` |

The naming convention distinguishes the two:

- **DDF names** follow the Btrieve field naming convention: `TABLEPREFIX_FIELDNAME` (e.g. `BKAP_CHK_INVNUM`). These match exactly the field names in the DDF schema.
- **Computed names** are short ALL-CAPS tokens with no table prefix (e.g. `CHK_DATE`, `TOT_AMT`, `PRT_ADD1`). These do not exist in any DDF file; they are calculated by the TAS program and staged via `SETUP_REPORT_BUFF` / `OUTPUT_REPORT_DATA`.

### Mechanism

The TAS program (e.g. BKAPH.RUN / BKAPHA.RUN) builds a TASFile pipeline buffer before calling `EXEC_RB`. This buffer contains both:
1. Fields read directly from open database records (DDF column values passed through unchanged)
2. Fields assembled or calculated at runtime — formatted check amounts in dollars and cents (`CHK_AMT_DOL`), formatted address lines (`PRT_ADD1/2/CSZ/COUNTRY`), running totals (`TOT_AMT/DAMT/RAMT/TOT`), the check number (`CHK_NUM`), line description (`LINE_DESC`), and the invoice reference in check format (`CHECK_INVNUM`)

This is why RTM-level static analysis alone cannot determine what a field contains — computed fields require tracing the TAS program logic to understand how they are populated.

### Sub-report nesting in BKAPH1.RTM

BKAPH1.RTM uses nested sub-reports for invoice detail lines within each check:

```
TppReport (master — check header per vendor)
  └─ TppDetailBand
       └─ TppSubReport
            └─ TppChildReport (detail — one row per invoice reference line)
```

The ChildReport binds to the same TASFile pipeline; the TAS program iterates invoice references, calling `OUTPUT_REPORT_DATA` once per line to feed the child.

BKAPHA1.RTM (laser forms) adds a second sub-report/child pair (`TppSubReport2` / `ChildReport2`) for the second copy of the check detail — laser checks print two copies of the stub.

### ReportBuilder version note

`BKAPHA1.RTM` contains `Version = '4.05 Pro'` — an older ReportBuilder engine than the `7.03` seen in `t7ing1.rtm`. The T6-era AP check RTMs predate the T7-era label RTMs. Both versions use the same TASFile pipeline mechanism; version differences affect component properties, not the field binding protocol.

---

## RTM runtime selection architecture (Pass 250, 2026-06-24)

### FILELOC — Central file path registry

`FILELOC` is a Btrieve-only table (not in DDF) that acts as a **runtime file path resolver**
for the entire EvoERP system — not just RTMs. Programs do not hardcode RTM file paths; instead
they look them up by logical name in FILELOC at runtime.

Usage: **831 of 1122 RWN programs** (74%) include FILELOC in their db_files list.

Key variables:
- `FILELOC.H` — FILELOC file handle (opened by 7 programs that directly query it)
- `FILELOC.NAMES` — enumeration of all FILELOC records (T7DEx data explorer, T7genImp)
- `ISTS.CFG.HHFLOC` — a system parameter specifying the handheld/remote file location path;
  appears in 698 programs (loaded from BKYSMSTR via T7MDefaults at boot)

### RTMVLD_* — Standard RTM validation library

All report-generating programs include a shared RTM path-validation subroutine. This library
exposes four standard variables:

| Variable | Meaning |
|----------|---------|
| `RTMVLD_CFGNAME` | Logical config name used to look up the RTM in FILELOC |
| `RTMVLD_PATH` | Resolved physical path to the RTM file |
| `RTMVLD_NAME` | RTM filename (without path) |
| `RTMVLD_SETTINGS` | Additional RTM settings (printer, copies, etc.) |

Usage: **327 of 1122 programs** use RTMVLD_*. Every RTMVLD program also uses FILELOC — the
two always appear together. This means the RTM selection path is:

```
Program has RTMVLD_CFGNAME = "APCHECK"
    → RTMVLD library looks up "APCHECK" in FILELOC
    → FILELOC returns path: T:\BKAPHA1.RTM
    → RTMVLD_PATH = "T:\", RTMVLD_NAME = "BKAPHA1.RTM"
    → Program calls: RTM_FN (RTMVLD_PATH + RTMVLD_NAME)
    → EXEC_RB
```

This explains why static analysis (rtm_callers.csv) captures only 403 of the 1305+ RTM files:
most RTM selections are **runtime-configurable** through FILELOC, not hardcoded.

### ISRTMS — Label routing table (DDF confirmed, 29 fields)

`ISRTMS.B` maps CUST/VEND/ITEM combinations to specific label RTM files. Used by
T7ARA (AR Invoices), J7CCSOLABELS, J7NMITEMRTM, J7NMRTMPRINTER for label printing.

| Field | Type | Size | Meaning |
|-------|------|------|---------|
| `IS_RTM_CUST` | STRING | 10 | Customer code (PK 1) |
| `IS_RTM_VEND` | STRING | 10 | Vendor code (PK 2) |
| `IS_RTM_ITEM` | STRING | 15 | Item code |
| `IS_RTM_RTM` | STRING | 12 | RTM filename (8.3 format) |
| `IS_RTM_PROGRAM` | STRING | 15 | Program that uses this config |
| `IS_RTM_DESC` | STRING | 30 | Description |
| `IS_RTM_DFLT` | STRING | 1 | Default flag (Y/N) |
| `IS_RTM_DATE` | DATE | 4 | Date |
| `IS_RTM_FLAG` | STRING | 1 | Flag |
| `IS_RTM_PARTLBL` | STRING | 12 | Part label RTM filename |
| `IS_RTM_SHIPLBL` | STRING | 12 | Shipping label RTM filename |
| `IS_RTM_CONTLBL` | STRING | 12 | Container label RTM filename |
| `IS_RTM_MIXEDLBL` | STRING | 12 | Mixed (multi-SKU) label RTM |
| `IS_RTM_QUICKLBL` | STRING | 12 | Quick label RTM |
| `IS_RTM_MISCLBL1..3` | STRING | 12 | Miscellaneous label RTMs 1–3 |
| `IS_RTM_QTY` | UBINARY | 2 | Label quantity |
| `IS_RTM_EXTRA` | STRING | 100 | Extra configuration |
| `IS_RTM_PRINTER_1..10` | STRING | 90 | Printer config slots 1–10 |

Variable namespace (from T7ARA, J7CCSOLABELS, J7NMITEMRTM, J7NMRTMPRINTER):
`IS.RTM.CUST / VEND / ITEM / RTM / PROGRAM / DESC / DFLT / DATE / FLAG /`
`PARTLBL / SHIPLBL / CONTLBL / MIXEDLBL / QUICKLBL / MISCLBL1..3 / QTY / PRINTER / EXTRA`

### Corrected total RTM count (Pass 250)

Physical count from `\\i2s109-solidcrm\DBAMFG$\*.RTM`: **1305 files** (not 899 as previously estimated).

| Prefix | Count | Description |
|--------|-------|-------------|
| `T6*` | 736 | TAS Pro 6 era (dominant — 57% of all RTMs) |
| Other | 380 | ENA*, customer-specific, utility RTMs |
| `BK*` | 150 | Legacy DBA-era standard reports |
| `J7*` | 20 | i2 Systems J7 customer customizations |
| `T7*` | 19 | TAS Pro 7 era (very few — T7 programs reuse T6 RTMs) |

**T6 module breakdown (736 T6 RTMs by 2-char module code):**

| Module | RTMs | Module | RTMs | Module | RTMs |
|--------|------|--------|------|--------|------|
| SO | 131 | AP | 40 | BM | 18 |
| WO | 68 | GL | 32 | SR | 16 |
| IN | 67 | PR | 31 | SH | 15 |
| PO | 41 | AR | 27 | RO | 13 |
| JC | 26 | SA | 19 | AB | 12 |
| MR | 11 | DC | 10 | QC | 10 |
| ES | 8 | CS | 8 | CM | 8 |
| SP | 7 | DE | 6 | CO | 5 |
| PI | 5 | RM | 8 | and 30+ smaller | ~60 |

SO (Sales Orders) has 131 T6 RTMs — by far the most report-variant-rich module.

Key insight: TAS Pro 7 added **only 19 new RTMs** for the T7 era. T7* programs almost universally
reuse T6* RTMs via the FILELOC/RTMVLD_ runtime path resolution. The 736 T6* RTMs remain the
operative report library even for modern T7 programs.

---

---

## Systematic DataField extraction — all 2610 RTM files (Pass 406, 2026-06-30)

Source: `samples/rtm_fields.csv` — produced by `scripts/extract_rtm_fields.py`.

### Extraction summary

| Metric | Value |
|--------|-------|
| RTM files processed | 2610 |
| Files with at least one DataField | 1302 (50%) |
| Total DataField rows | 118,432 |
| Unique DataField values | 8,574 |
| Files with FileName (sub-report links) | 0 |

The 2610 count includes both `*.RTM` and `*.rtm` globs across the share root; the 1302 with DataField means roughly half the files are layout-only (no bound data fields — shared library templates, headers/footers, cfg.rtm, etc.).

### DataField naming patterns

| Pattern | Row count | Example |
|---------|-----------|---------|
| `TABLE.FIELD` / `TABLE.SUB.FIELD` (standard DDF) | 45,870 | `BKAR.INV.INVDTE`, `BKAP.CHK.INVNUM` |
| Computed/staged variables (no strict DB pattern) | 69,350 | `from.date`, `tot.amt`, `prt.addr1`, `CHK_DATE` |
| `ARRAY[n]` bracket subscript | 1,716 | `ABAL[1]`, `MTIC.PROD.RCOST[6]` |
| Single-char alias (e.g. `A.FIELD`) | 1,394 | `A.BOQ`, `A.EMPNUM` |
| `{n}` display-width suffix | 100 | `AC.DET.ACTCOST{10}` |
| Leading-dot prefix | 2 | `.BK.DESC.NOTES` |

**Key insight:** 59% of all DataField values are computed/staged variables rather than direct DDF column names. These are TAS program variables filled by `OUTPUT_REPORT_DATA` and carry no inherent table structure — they carry report-specific names like `from.*`, `thru.*`, `tot.*`, `prt.*`, `sub.*`, `cal.*`.

### Top table/alias prefixes by row count

| Prefix | Rows | Module | Notes |
|--------|------|--------|-------|
| `BKAR` | 11,734 | AR | Accounts Receivable — most-reported module |
| `CUST` | 5,518 | AR/SO | Customer address staging (computed) |
| `BKSY` | 4,476 | SY | System/configuration (often `BKSY.AP.ENDDESC`) |
| `BKAP` | 2,660 | AP | Accounts Payable |
| `from` | 2,498 | * | Date/code range parameter — lower bound |
| `thru` | 2,488 | * | Date/code range parameter — upper bound |
| `bksa` | 2,464 | SA | Sales Analysis (lowercase alias) |
| `PTD` | 2,310 | * | Period-to-date staging arrays |
| `IS` | 2,008 | IN/SY | Inventory Summary staging |
| `bkic` | 1,866 | IC | Inventory Control (lowercase alias) |
| `prt` | 1,684 | * | Print staging fields (378 unique) |
| `MTWO` | 1,650 | WO | Manufacturing Work Orders |
| `tot` | 1,588 | * | Running total staging (372 unique) |

### Key table field inventories (confirmed from RTM bindings)

#### BKAR — Accounts Receivable (158 unique DataField values)

Customer master fields: `CUSTCODE`, `CUSTNAME`, `ADD1`, `ADD2`, `CITY`, `STATE`, `ZIP`,
`COUNTRY`, `TELEPHONE`, `FAX.PHONE`, `EMAIL`, `CONTACT`, `CLASS`, `TERMS.NUM`, `SLSP.NUM`,
`SHIPVIA`, `TERRITORY`, `SIC.CODE`, `CREDITLMT`, `LEAD.SRC`, `PRICE.MAT`, `STATEMENT`,
`LASTPMT`, `LASTSALE`, `START.DATE`, `TXN.CODE`, `TXN.LOT`, `TXN.SERIAL`, `IS.MCCODE`

Invoice header (`.INV.*`): `NUM`, `INVDTE`, `ORDDTE`, `SHIPDT`, `SHIPPR`, `SONUM`, `CUSORD`,
`DESC`, `SLSP`, `SLSP2`, `TERMD`, `TOTAL`, `SUBTOT`, `TAXAMT`, `TAXABL`, `FRGHT`, `COGS`,
`LOC`, `FOB`, `RTS`, `ENTBY`, `ISCUR`, `TRACK`, `CHKNUM`, `BILCOD`, `BILNME`, `BILZIP`,
`SHPNME`, `SHPA1`, `SHPCOD`, `SHPCTY`, `SHPST`, `SHPZIP`, `SHPVIA`, `CUSATT`, `COMMPR`,
`JOBNUM`

Invoice line (`.INVL.*`): `INVNM`, `PCODE`, `PDESC`, `PQTY`, `PPRCE`, `PEXT`, `PDISC`,
`COGS`, `PCOGS`, `UBO`, `USTD`, `UM.LN`, `LOC`, `RTS`, `CNTR`, `ARD`, `ASD`, `ESD`,
`COMPR`, `OOQTY`

Invoice transaction (`.INVT.*`): `CODE`, `DATE`, `DESC`, `NUM`, `AMT`, `AMTRM`

#### BKAP — Accounts Payable (93 unique DataField values)

Vendor master: `VENDCODE`, `VENDNAME`, `CONTACT`, `TERMS.NUM`, `LASTPMT`, `LASTPURCH`,
`PURCH.LYR`, `PURCH.MTD`, `PURCH.YTD`, `PURCH.VAR`, `CUST.CODE`, `IS.MCCODE`

PO header (`.PO.*`): `NUM`, `VNDCOD`, `VNDNME`, `ORDDTE`, `TERMD`, `TOTAL`, `FOB`,
`SHPVIA`, `SHPNME`, `SHPA1`, `SHPA2`, `SHPCTY`, `SHPST`, `SHPZIP`, `TAXABLE`, `TAXAMT`,
`DESC`, `EMPNUM`, `ENTBY`, `PCKSLP`, `OBYCUS`, `CONFIRM`, `ISCUR`, `ISREV`, `ISRVDT`

PO line (`.POL.*`): `PONM`, `PCODE`, `PDESC`, `PQTY`, `PPRCE`, `PEXT`, `RQTY`, `IQTY`,
`ARD`, `ESD`, `ERD`, `OPER`, `CNTR`, `OO.PPRCE`, `OO.PQTY`, `OO.QTY`, `QC.QTY`,
`QC_QTY`, `WOPRE`, `WOSUF`

AP check (`.CHK.*`): `NUM`, `INVNUM`, `INVDTE`, `INVAMT`, `AMTPD`, `DISC`, `CHKDTE`,
`VNDCOD`, `DESC`, `ISCUR`

AP transaction (`.INVT.*`): `CODE`, `DATE`, `DESC`, `NUM`, `MCCOD`

#### MTWO — Work Orders (43 unique DataField values)

WIP header (`.WIP.*`): `CODE`, `DESC`, `DESCII`, `WOPRE`, `WOSUF`, `STATUS`, `SQTY`,
`COMQTY`, `SSTART`, `SFIN`, `DDATE`, `ASTART`, `AFIN`, `PRTY`, `LOC`, `SONUM`, `CUSORD`,
`PPRCE`, `ETOT`, `CHGORD`, `PROJ`, `CONTAT`, `USERCD`

Customer link: `CUSTCODE`, `CUSTNAME`, `PRODCODE`

#### MTIC — IC Product Master (54 unique DataField values)

Product master (`.PROD.*`): `CODE`, `DESC`, `CLDES`, `TYPE`, `LOC`, `CUST`, `CUSNM`,
`ACTIV`, `UOA`, `AVAIL`, `CYCLE`, `LEAD`, `DRAW`, `REV`, `WT`, `CUBFT`, `STDPK`,
`MRPSW`, `MRP`, `WIPDP`, `LONGP`, `EXPBF`, `DELBF`, `VEND`

Array fields: `RCOST[2]`, `RCOST[6]`, `RCOST[13]` — rolling cost elements;
`SPECS[1..5]` — specification strings; `SUBST[1]`, `SUBST[3]` — substitute parts

#### Computed staging namespaces (report-specific)

| Namespace | Unique values | Role |
|-----------|--------------|------|
| `prt.*` | 378 | Print staging: formatted/computed values ready for output |
| `tot.*` | 372 | Running totals (subtotals, grand totals, accumulators) |
| `from.*` | 101 | Report range parameters — lower bound (date, code, class) |
| `thru.*` | 101 | Report range parameters — upper bound (mirrors `from.*`) |
| `sub.*` | 122 | Sub-totals per group |
| `IS.*` | 88 | Inventory Summary staging (formatted IS values) |
| `bkpr.*` | 259 | Payroll staging fields (lowercase — alias or computed) |
| `bksa.*` | 56 | Sales Analysis monthly period values (`bksa.from1..12`) |
| `cal.*` | — | Calculated period values (current year) |
| `ncal.*` | — | Next/prior-year calculated period values |
| `pcal.*` | — | Prior-year calculated period values |
| `PTD.ARRAY[n]` | 3 | Period-to-date array (current, prior, variance) |

**`from.*` / `thru.*` pattern:** 101 unique range parameters confirm EvoERP reports have a standardized set of filter parameters (date ranges, part ranges, customer ranges, location codes, etc.) that TAS programs fill from user input before the report loop.

**`bksa.from1..12`:** Sales Analysis monthly sales amounts for months 1–12 of the fiscal year pushed one record per customer to the SA report pipeline.

### Summary update to "Things still open"

The systematic extraction resolves the "full programmatic extraction" open item. The remaining gaps are:
- FILELOC schema and live data mapping (which logical names resolve to which RTM filenames)
- RTMVLD_ library internals (blocked — embedded in encrypted .RWN)
- Physical location of `cfg.rtm` (requires identifying what `T:\` maps to on a live workstation)

## Template.FileName cross-reference map (Pass 559, 2026-07-02)

Full binary scan of all 1,305 RTM files on `\\i2s109-solidcrm\DBAMFG$\` for the
`\x11Template.FileName` Pascal-short-string property (17 bytes: `\x11` + `Template.FileName`).
Stored as `\x06` (vaString) + length byte + path string. Result: `samples/rtm_crossrefs.csv`.

**Note:** Earlier analysis (Pass 406) searched for `\x08FileName` (8 bytes) and found zero.
The correct property name is `Template.FileName` (17 bytes with the parent qualifier), not bare `FileName`.

### Statistics

| Metric | Count |
|--------|-------|
| Total Template.FileName properties found | 4,178 |
| Self-references (file stores its own path) | 1,600 |
| Cross-references (sub-report links) | 2,578 |
| Distinct caller→callee RTM pairs | 1,078 |
| Distinct caller files | 892 / 1,305 (68%) |
| Files without self-ref path stored | 122 |

**Self-reference semantics:** When a ReportBuilder report is saved, it stores its own filepath as
`Template.FileName` in the root `TppReport` component. 1,183 unique files have this (the remaining
122 were either never saved on a `C:\DBAMFG\` or `T:\` path, or are templates without self-ref).

### Sub-report architecture

892 of the 1,305 RTM files contain sub-report (`TppSubReport` / `TppChildReport`) references to
other RTM files. The sub-report pattern is:
- Parent RTM has a `TppSubReport` component
- Its `Template.FileName` property names another RTM on the same share
- At print time, ReportBuilder loads the child RTM and merges it into the output

Most common sub-report targets (i.e., RTMs frequently referenced by other RTMs):
- `C:\DBAMFG\BKISWCE1.RTM` — Work Order Cost Extension sub-report (T6WOL* reports)
- `C:\DBAMFG\BKAPHA4.RTM` — AP check sub-variant
- `C:\DBAMFG\bksrb4.rtm` — SR/Sales sub-report library
- `C:\DBAMFG\bksam1.rtm` — SA/Sample summary sub-report

### Developer history revealed by stored paths

RTM files retain their original save paths from developer machines. These dev artifacts are in
`samples/rtm_crossrefs.csv` and reveal:

| Path prefix | Source | Note |
|-------------|--------|------|
| `C:\DBAMFG\` | Production i2 Systems workstation | Standard production path |
| `T:\` | Workstation T: drive mapping → share | Per-workstation mapping |
| `\\I2s109-solidcrm\dbamfg$\` | Current production UNC | Absolute form of production path |
| `C:\SOURCE\RTM\` | Developer source tree | Developer machine (ISTech/Addsum) |
| `C:\TASPRO7\DBA7\` | Developer TAS Pro 7 project | DBA7 development environment |
| `\\I2s44-hapi\dbamfg$\` | Dev machine "hapi" | ISTech/Addsum developer workstation |
| `\\wacke\dbamfg$\` | Dev machine "wacke" | ISTech/Addsum developer workstation |
| `D:\DBAMFGPR\` | Dev machine drive D: | Separate payroll DBAMFG partition |
| `C:\Program Files\Borland\Delphi 3\BIN\test.RTM` | Delphi 3 install | **Confirms Delphi 3 used in original development** |
| `\\Asisvr\apps\dbamfg\` | Customer "Asisvr" | EvoERP client site |
| `\\Seconsvr01\dbamfg$\` | Customer "Seconsvr01" | EvoERP client site |
| `\\Cpt-app\dbamfg\` | Customer "Cpt-app" | EvoERP client site |
| `\\Server\eimco\Public\Apps\DBAMFG\` | Customer "EIMCO" | Mining equipment company (EIMCO) |

The **Borland Delphi 3** path confirms that the original ReportBuilder integration and RTM files
were developed using Delphi 3 (mid-to-late 1990s era). DBA Manufacturing originated in the
Delphi 3 timeframe before migrating to TAS Pro 7 / Nevrona ReportBuilder.

### Notable edge-case files

- `t6woc9 - backup 9-24-25.RTM` — backup copy of work order traveler from 2025-09-24 (future date)
- `t6woc9 backup 5-14-25.RTM` — backup from 2025-05-14
- `T6SOC4T - Copy.RTM` — copy artifact
- `BKAPHA103009.RTM` → `T:\BKAPHA1.RTM` — dated variant name (103009 = Oct 30, 2009?)
- `BKARG.RTM` → `C:\Program Files\Borland\Delphi 3\BIN\test.RTM` — leftover Delphi 3 test artifact

## Things still open

- Physical location of `cfg.rtm` — not found via UNC walk; likely `T:\cfg.rtm` on the T: drive mapping. `cfg.rtm` is in `samples/rtm_crossrefs.csv` as a callee, confirming it exists; UNC path still unknown.
- Multi-currency report parameter passing (T7MLC uses LANGDICT).
- FILELOC schema (fields/keys) — Btrieve-only, not in DDF; needs runtime dump or hex analysis.
- RTMVLD_ library source — embedded in EVO.LIB or a separate subroutine file (blocked — .RWN encrypted).
- Mapping of FILELOC logical config names to RTM filenames (requires reading live FILELOC.B data).
