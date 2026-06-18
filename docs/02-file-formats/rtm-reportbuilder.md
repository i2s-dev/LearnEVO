# `.RTM` / `.btm` — Nevrona ReportBuilder Template

Status: verified — header structure confirmed from
`../../samples/rtm/t7ing1.rtm` and `../../samples/btm/I2SCHK1.btm`.

## Format

`.RTM` files are **Delphi binary form streams** (TPF0 format) holding
a **Nevrona ReportBuilder** `TppReport` component tree. A `.btm` is a
backup/snapshot of an RTM at the same format.

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

Physical file not found on `\\i2s109-solidcrm\DBAMFG$\` (2026-06-18 search). It may be:
- Referenced by a path that resolves via a network drive map configured at runtime (e.g. `T:\cfg.rtm`)
- Deleted or renamed — reports function correctly at runtime, suggesting it's being found via a
  configured path not visible from this workstation
- The path is stored in `C:\ISTS\RBuilder.ini` (the ReportBuilder settings file)

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

## Things still open

- Physical location of `cfg.rtm` — check `C:\ISTS\RBuilder.ini` for configured template paths.
- Full binary parser to extract TppDBText data-field bindings from all 403 RTMs programmatically.
  Format is standard Delphi TStream; `dfmreader` Python library could be adapted.
- Confirm report parameter passing for multi-currency reports (T7MLC uses LANGDICT — may have
  a different pipeline setup for translated field values).
- Identify the 182 "other" module RTMs fully (GL, BM, SH, DE, MR, PI, ES, DC, JC category RTMs).
