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

## Things still open

- Physical location of `cfg.rtm` — `T:\cfg.rtm` is the inferred path via drive mapping; UNC path
  unknown. Would need to identify what share `T:\` maps to on a running workstation.
- Multi-currency report parameter passing (T7MLC uses LANGDICT).
- Full programmatic extraction of all 403 RTM field bindings (manual for 2 samples done above).
- FILELOC schema (fields/keys) — Btrieve-only, not in DDF; needs runtime dump or hex analysis.
- RTMVLD_ library source — embedded in EVO.LIB or a separate subroutine file.
- Mapping of FILELOC logical config names to RTM filenames (requires reading live FILELOC.B data).
