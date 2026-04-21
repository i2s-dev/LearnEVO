# Reporting Pipeline

Status: verified (format + cross-reference dumped from every RUN/RWN).

## Overview

EvoERP's reporting pipeline is two-tiered:

1. **Legacy region-based reports** — driven by the TAS runtime's
   `INIT_REGION` / `MARK_REGION` / `OUTPUT_REPORT_DATA` /
   `PRINT_REPORT` keywords. Writes directly to a printer control file
   (`GENERIC.CTL` or driver-specific). Still present in `.RUN` modules.

2. **Nevrona ReportBuilder (RB) reports** — the current style. TAS
   program fills a pipeline, hands off to the embedded ReportBuilder
   engine via `EXEC_RB` / `RTM_FN <path.rtm>`, which then renders to
   screen, printer, or PDF. All modern `T7*.RWN` reports use this path.

## Templates

- **`.RTM`** — active ReportBuilder template (binary Delphi `TPF0`).
- **`.btm`** — snapshot/backup of an RTM, same format.
- **899 RTMs + 60 BTMs** on the share.

Format details: [../02-file-formats/rtm-reportbuilder.md](../02-file-formats/rtm-reportbuilder.md).
Designer: `C:\ISTS\RBDsgnr.exe`.

## Cross-reference — which programs use which RTMs

`scripts/bulk_strings_rwn.py` dumped all binaries; grepping the dumps
for `*.rtm` filenames yields an RTM → caller mapping. Full CSV:
`../../samples/rtm_callers.csv`. Top 15 most-called templates:

| RTM | # callers | Representative callers |
| --- | --------: | ---------------------- |
| `cfg.rtm`    | 792 | almost every program — the "config report" common template |
| `ent.rtm`    | 90  | entry-form summary templates |
| `t6.rtm`     | 40  | generic T6-era template |
| `temp.rtm`   | 30  | scratch/intermediate |
| `bk.rtm`     | 23  | generic BK-era template |
| `banks.rtm`  | 16  | AP check run (`BKADC`, `BKAPH`, `BKAPHA`) |
| `dflt.rtm`   | 16  | default fallback |
| `test.rtm`   | 11  | dev/test |
| `max.rtm`    | 7   | `T6ALSO*` sales-order utilities |
| `curr.rtm`   | 7   | multi-currency outputs |
| `short.rtm`  | 5   | short-item shortage listings |
| `next.rtm`   | 5   | paginated continuation |
| `using.rtm`  | 5   | where-used reports |
| `bksopb1.rtm`..`bksopb4.rtm` | 4 each | SO packing slip formats 1-4 |
| `bksob1.rtm`..`bksob4.rtm`  | 3 each | SO acknowledgement formats 1-4 |

A single "menu operation → RTM" pattern emerges: most `SO-X`
variations exist in **4 format flavors** (labeled `1`/`2`/`3`/`4`), and
the user's choice of format is stored in `BKYSMSTR.bkys.yn[48]` as
seen in `samples/src/Bkaph.src`:60-81. The program picks the RTM by
concatenating a base name with the format digit.

## Program flow for an RB report

From reading `.SRC` patterns plus `tp7runtime.exe` keywords:

```
OPEN <driver table(s)>
SETUP_REPORT_BUFF <buffer spec>

for each record:
   <populate buffer>
   OUTPUT_REPORT_DATA

RTM_FN <filename>.rtm
REPORTNAME "user-facing name"
USE_PRINTER <printer-name>  or  PRINT_TO_FILE <pdf/txt>
EXEC_RB        ; hand off to ReportBuilder
; control returns after user closes the preview / print finishes

PRINT_CANCEL   ; optional cleanup
```

The important insight: **the TAS program builds the dataset itself and
pushes it into the RB pipeline one record at a time**. RB never queries
the DB directly — it draws from the buffer that the TAS program
supplies. This preserves all the multi-company, per-user, per-screen
logic inside the TAS layer.

## Output destinations

Runtime supports four output destinations (from keywords):

| Destination | Triggered by |
| ----------- | ------------ |
| **Screen preview** | Default `DeviceType=Screen` in RTM |
| **Printer**        | `USE_PRINTER <name>` or `WLASER_PRT` for laser-specific |
| **PDF file**       | `PRINT_TO_FILE <filename.pdf>`; RB writes PDF natively |
| **Text file**      | `PRINT_TEXT <filename.txt>` for plain-text spool |
| **Archive**        | `PRINT_ARCHIVE` — saves a canned copy (used by AP checks to tie to the check-history record) |

The `PDFS\` folder in `C:\ISTS` is the local staging directory; the
`EVOReports\` folder on the share is the shared archive.

## Scheduled / batched reports

Several `Evo*` infrastructure programs run reports headless:

- **`EvoScheduler.RWN` / `EvoSched.RWN` / `EvoSchedSetup.RWN`** — cron-
  like scheduler. Reads schedule entries (probably from a DB table; to
  confirm) and invokes a target `RWN` at the scheduled time.
- **`EvoService.RWN`** — Windows-service harness that can host the
  scheduler or run unattended overnight jobs.
- **`AUTOT7MRF.RWN`** — an "auto" variant of `MR-F` MRP — the same
  program Bkmrf.src implements, wrapped for unattended run.

## `TASFile` pipeline in the RTM

From the RTM header (`samples/rtm/t7ing1.rtm` + `samples/btm/I2SCHK1.btm`):

```
DataPipelineName = 'TASFile'
```

This is a custom `TppDataPipeline` subclass provided by the TAS runtime
that reads from the output buffer. The RTM's `TppDBText` components
name fields like `BKAP_CHK_INVNUM`, `BKAP.CHK.AMTPD` — these are the
buffer-column labels.

## Things still to document

- The `Image*` and `Icon*` controls in RTMs (barcode rendering, QR —
  the runtime has `QRCODE` keyword).
- Multi-page reports with `TppSubReport` / `TppChildReport` — the
  check template (`I2SCHK1.btm`) shows this: one parent RB template
  owns the check layout, and a child RB template owns the stub.
- Exact format of `PRINT_ARCHIVE` output (tied to the check-history
  record).
