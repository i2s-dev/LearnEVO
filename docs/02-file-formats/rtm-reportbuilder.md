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

### Module-to-RTM mapping examples

| Module | Program | RTM files |
|--------|---------|-----------|
| AP-H Print Checks | BKAPHA, T6APHA | `bkapha1.rtm`, `bkapha2.rtm`, `banks.rtm`, `cfg.rtm` |
| PO-B Print PO | BKPOB, T6POB | `ibkpob1..4.rtm`, `it6pob1..4.rtm`, `bk.rtm`, `temp.rtm` |
| SO-B Print SO | BKSOB, T6SOB | `ibksob1..4.rtm`, `it6sob1..3.rtm`, `bk.rtm`, `temp.rtm` |
| AR-E Print Statements | BKARE, T6ARE | `abk.rtm`, `at6.rtm`, `bk.rtm`, `t6.rtm` |
| RM (RMA) | ISSRB | `ibkrma1.rtm`, `it6rma1.rtm` |

## Things still open

- Full binary parser to diff RTMs programmatically. Format is standard Delphi TStream;
  open-source Python readers (e.g. `dfmreader`) could be adapted if needed.
- Confirm exact content of `cfg.rtm` — company name/address or just layout constants.
  Requires the report designer or binary parsing.
- Identify the ~32 other-prefix RTMs fully.
