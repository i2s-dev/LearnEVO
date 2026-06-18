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

---

## Pass 101 — RTM Cross-Reference by Module (2026-06-18)

Total: **403 RTMs** mapped from `rtm_callers.csv`.

Each RTM is listed under its primary calling module. "Callers" are the RWN/RUN
program names that invoke each RTM via `EXEC_RB` / `RTM_FN`.

### RTM Count by Module

| Module | RTM Count |
|--------|-----------|
| AM | 2 |
| AP | 20 |
| AP (1099) | 2 |
| AR | 24 |
| BM | 2 |
| CM | 8 |
| DC | 5 |
| GL | 3 |
| IN | 14 |
| J7 (custom) | 23 |
| JC | 1 |
| LC | 1 |
| Other | 90 |
| PI | 3 |
| PO | 26 |
| PR | 9 |
| SA | 18 |
| SC | 1 |
| SO | 48 |
| SO (legacy) | 44 |
| SR | 8 |
| WO | 13 |
| generic | 38 |

---

### AM Module RTMs (2 total)

| RTM File | Callers |
|----------|---------|
| `t6amf.rtm` | t6ami |
| `t6amf1.rtm` | t6amf |

### AP Module RTMs (20 total)

| RTM File | Callers |
|----------|---------|
| `banks.rtm` | BKADC, BKAPH, BKAPHA, BKPRD, T6APB, T6APC, T6APH, T6APHA (+8 more) |
| `bkaphar1.rtm` | BKAPH, BKAPHA |
| `bkapm1.rtm` | BKAPM |
| `bkapm2.rtm` | BKAPM |
| `bkapm3.rtm` | BKAPM |
| `t6aph1.rtm` | T6APH |
| `t6apha1.rtm` | T6APHA |
| `t6apha2.rtm` | T6APHA |
| `t6apha3.rtm` | T6APHA |
| `t6aphar1.rtm` | T6APH, T6APHA |
| `t6api1.rtm` | T6API |
| `t6api2.rtm` | T6API |
| `t6api3.rtm` | T6API |
| `t6apm1.rtm` | t6apm |
| `t6apm2.rtm` | t6apm |
| `t6apm3.rtm` | t6apm |
| `t7ape1.rtm` | t6ape |
| `t7apg1.rtm` | t6apg |
| `t7apj1.rtm` | t6apj |
| `t7apl1.rtm` | t6apl |

### AP (1099) Module RTMs (2 total)

| RTM File | Callers |
|----------|---------|
| `bkaps1.rtm` | APS1999, APS2000 |
| `bkaps3.rtm` | APS2000 |

### AR Module RTMs (24 total)

| RTM File | Callers |
|----------|---------|
| `abk.rtm` | BKARE, T6ARE |
| `at6.rtm` | BKARE, T6ARE |
| `bkare4.rtm` | BKARE |
| `bkari1.rtm` | BKARI |
| `bkari2.rtm` | BKARI |
| `bkari3.rtm` | BKARI |
| `bkarp1.rtm` | BKARP |
| `bkarpl1.rtm` | BKARP |
| `it6are1.rtm` | T6ARE |
| `it6are2.rtm` | T6ARE |
| `it6are3.rtm` | T6ARE |
| `t6are1.rtm` | T6ARE |
| `t6are2.rtm` | T6ARE |
| `t6are3.rtm` | T6ARE |
| `t6are4.rtm` | T6ARE |
| `t6arf1.rtm` | T6ARF |
| `t6arf2.rtm` | T6ARF |
| `t6arf3.rtm` | T6ARF |
| `t6arf4.rtm` | T6ARF |
| `t6ari1.rtm` | T6ARI |
| `t6ari2.rtm` | T6ARI |
| `t6ari3.rtm` | T6ARI |
| `t6arp1.rtm` | T6ARP |
| `t6arpl1.rtm` | T6ARP |

### BM Module RTMs (2 total)

| RTM File | Callers |
|----------|---------|
| `t6bmb1.rtm` | t6bmb |
| `t6fob1.rtm` | t6bmb |

### CM Module RTMs (8 total)

| RTM File | Callers |
|----------|---------|
| `bkcmbd1.rtm` | BKCMBD |
| `bkcmbd2.rtm` | BKCMBD |
| `bkcmbd3.rtm` | BKCMBD |
| `bkcmbi1.rtm` | BKCMBI |
| `t6cmbd1.rtm` | T6CMBD |
| `t6cmbd2.rtm` | T6CMBD |
| `t6cmbd3.rtm` | T6CMBD |
| `t6cmbi1.rtm` | T6CMBI |

### DC Module RTMs (5 total)

| RTM File | Callers |
|----------|---------|
| `bkdce.rtm` | BKDCE |
| `bkdcf.rtm` | BKDCF |
| `t6dcd1.rtm` | t6dcd |
| `t6dce.rtm` | T6DCE |
| `t6dcf.rtm` | T6DCF |

### GL Module RTMs (3 total)

| RTM File | Callers |
|----------|---------|
| `t6glc1.rtm` | t6glc |
| `t6glo1.rtm` | t6glo |
| `t6pc.rtm` | T6GLN |

### IN Module RTMs (14 total)

| RTM File | Callers |
|----------|---------|
| `bkactrptbkac.rtm` | T6INO |
| `bking1.rtm` | BKING, T6ING |
| `hold.rtm` | BKING |
| `ing.rtm` | BKING |
| `ino.rtm` | T6INO |
| `lot.rtm` | T6INO |
| `poc.rtm` | BKING |
| `ser.rtm` | T6INO |
| `t6ind1.rtm` | T6IND |
| `t6ine1.rtm` | t6ine1 |
| `t6inh1.rtm` | t6inh |
| `t6ino1.rtm` | T6INO |
| `t6ino2.rtm` | T6INO |
| `topsale.rtm` | t6ine1 |

### J7 (custom) Module RTMs (23 total)

| RTM File | Callers |
|----------|---------|
| `bkcmaccctemp.rtm` | J6HVRSAO, J6PETOPN, JMCRTOPN |
| `bkicmstrtemp.rtm` | J6BKMDIS, J6BKMREP, J6LAPSAR |
| `isudmstrtemp.rtm` | J6LAPSAO |
| `j6bkmdis.rtm` | J6BKMDIS |
| `j6bkmrep.rtm` | J6BKMREP |
| `j6btsrwo.rtm` | J6BTSRWO |
| `j6cfclbl.rtm` | j6cfcust |
| `j6cfcust.rtm` | j6cfcust |
| `j6cfprpt.rtm` | J6CFPRPT |
| `j6cfsan1.rtm` | j6cfsan |
| `j6cftopi.rtm` | J6CFTOPI |
| `j6crcol2.rtm` | J6CRCOLR |
| `j6crcolr.rtm` | J6CRCOLR |
| `j6ebdlot.rtm` | J6EBDLOT |
| `j6htjch1.rtm` | J6HTJCH |
| `j6hvrsao.rtm` | J6HVRSAO |
| `j6isdca1.rtm` | J6ISDCA |
| `j6lapsao.rtm` | J6LAPSAO |
| `j6lapsar.rtm` | J6LAPSAR |
| `j6lpsao2.rtm` | J6LAPSAO |
| `j6nzqwo1.rtm` | J6NZQWO |
| `j6petopn.rtm` | J6PETOPN |
| `j6poij1.rtm` | J6POIJ |

### JC Module RTMs (1 total)

| RTM File | Callers |
|----------|---------|
| `t6jca1.rtm` | t6jca |

### LC Module RTMs (1 total)

| RTM File | Callers |
|----------|---------|
| `islcf1.rtm` | ISLCF |

### Other Module RTMs (90 total — showing first 30)

| RTM File | Callers |
|----------|---------|
| `bkinlj1.rtm` | ISICT, ISINLJ, ISINLM |
| `bkrma1.rtm` | ISSRB |
| `bksopb1.rtm` | BKADF, BKSOPB, JKSDM, JKSOSB |
| `bksopb2.rtm` | BKADF, BKSOPB, JKSDM, JKSOSB |
| `bksopb3.rtm` | BKADF, BKSOPB, JKSDM, JKSOSB |
| `bksopb4.rtm` | BKADF, BKSOPB, JKSDM, JKSOSB |
| `bksrb1.rtm` | ISSRB |
| `bksrb2.rtm` | ISSRB |
| `bksrb3.rtm` | ISSRB |
| `bksrb4.rtm` | ISSRB |
| `bksrf1.rtm` | ISSRF |
| `bksrf2.rtm` | ISSRF |
| `bksrf3.rtm` | ISSRF |
| `bksrf4.rtm` | ISSRF |
| `bksrf6.rtm` | ISSRF |
| `bksrf7.rtm` | ISSRF |
| `bkwolj1.rtm` | ISWOLJ |
| `cfg.rtm` | ACAPIVP, APDUPFIX, APO001, APRECUFX, APS2000, AUTOBMG, AUTODCH, AUTOIND (+784 more) |
| `ent.rtm` | EBTAG, J6BTSRWO, J6CFPRPT, J6CFTOPI, J6CRCOLR, J6EBDLOT, J6HTJCH, J6HVRSAO (+82 more) |
| `esteetag.rtm` | EBTAG |
| `ibkrma1.rtm` | ISSRB |
| `ibksrb1.rtm` | ISSRB |
| `ibksrb2.rtm` | ISSRB |
| `ibksrb3.rtm` | ISSRB |
| `ibksrb4.rtm` | ISSRB |
| `ibksrf1.rtm` | ISSRF |
| `ibksrf2.rtm` | ISSRF |
| `ibksrf3.rtm` | ISSRF |
| `ibksrf4.rtm` | ISSRF |
| `isdca1.rtm` | J5ISDCA |

### PI Module RTMs (3 total)

| RTM File | Callers |
|----------|---------|
| `bkpica1.rtm` | BKPICA |
| `t6pica1.rtm` | T6PICA |
| `t6pif1.rtm` | T6PIF |

### PO Module RTMs (26 total)

| RTM File | Callers |
|----------|---------|
| `bkpoja1.rtm` | BKPOJA |
| `ibkpob1.rtm` | BKPOB |
| `ibkpob2.rtm` | BKPOB |
| `ibkpob3.rtm` | BKPOB |
| `ibkpob4.rtm` | BKPOB |
| `ibkpoe1.rtm` | BKPOEA |
| `ibkpoe2.rtm` | BKPOEA |
| `it6pob1.rtm` | T6POB |
| `it6pob2.rtm` | T6POB |
| `it6pob3.rtm` | T6POB |
| `it6pob4.rtm` | T6POB |
| `it6pob4r.rtm` | T6POB |
| `it6pob4s.rtm` | T6POB |
| `it6poe1.rtm` | T6POEA |
| `it6poe2.rtm` | T6POEA |
| `t6pob1.rtm` | T6POB |
| `t6pob2.rtm` | T6POB |
| `t6pob3.rtm` | T6POB |
| `t6pob4.rtm` | T6POB |
| `t6pob4r.rtm` | T6POB |
| `t6pob4s.rtm` | T6POB |
| `t6poe1.rtm` | T6POEA |
| `t6poe2.rtm` | T6POEA |
| `t6poih1.rtm` | t6poih |
| `t6poja1.rtm` | T6POJA |
| `zbksa.rtm` | BKPOENG, T6POENG |

### PR Module RTMs (9 total)

| RTM File | Callers |
|----------|---------|
| `bkprlf1.rtm` | BKPRLF |
| `bkprlg1.rtm` | BKPRLG |
| `bkprli.rtm` | BKPRLI |
| `t6prd1.rtm` | t6prd |
| `t6prd2.rtm` | t6prd |
| `t6prlf1.rtm` | T6PRLF |
| `t6prlg1.rtm` | t6prlg |
| `t6prli.rtm` | T6PRLI |
| `t6prli2.rtm` | T6PRLI |

### SA Module RTMs (18 total)

| RTM File | Callers |
|----------|---------|
| `bksa.rtm` | BKPOENG, BKSAM, BKSAN |
| `bksam1.rtm` | BKSAM |
| `bksan1.rtm` | BKSAN |
| `bksareptbksa.rtm` | T6POENG, T6SAM, T6SAN, j6cfsan |
| `bksooj1.rtm` | BKSAM |
| `bksook1.rtm` | BKSAN |
| `bksopd1.rtm` | BKSAM |
| `bksope1.rtm` | BKSAN |
| `dflt.rtm` | BKING, BKSAM, BKSAN, T6ALSOB, T6ALSOC, T6ALSOF, T6ALSOPB, T6ESD (+8 more) |
| `save.rtm` | BKSAM, T6SAM |
| `short.rtm` | BKSAM, BKSAN, T6SAM, T6SAN, j6cfsan |
| `show.rtm` | T6SAM, T6SAN, j6cfsan |
| `t6sam1.rtm` | T6SAM |
| `t6san1.rtm` | T6SAN |
| `t6sooj1.rtm` | T6SAM |
| `t6sook1.rtm` | T6SAN, j6cfsan |
| `t6sopd1.rtm` | T6SAM |
| `t6sope1.rtm` | T6SAN, j6cfsan |

### SC Module RTMs (1 total)

| RTM File | Callers |
|----------|---------|
| `isscf1.rtm` | ISSCF |

### SO Module RTMs (48 total)

| RTM File | Callers |
|----------|---------|
| `bk.rtm` | BKARE, BKPOB, BKSOB, BKSOC, BKSOD, BKSOF, BKWOC, ISLCF (+15 more) |
| `bksoc1t.rtm` | BKSOC |
| `bksoc2t.rtm` | BKSOC |
| `bksoc3t.rtm` | BKSOC |
| `bksoc4t.rtm` | BKSOC |
| `bksodd1.rtm` | BKSOD |
| `bksodd2.rtm` | BKSOD |
| `bksodh1.rtm` | BKSOD |
| `bksodh2.rtm` | BKSOD |
| `bksom1.rtm` | BKSOM |
| `bksom2.rtm` | BKSOM |
| `bksom3.rtm` | BKSOM |
| `bksom4.rtm` | BKSOM |
| `emissoa1.rtm` | T6SOD, t6sodmsg |
| `ibksob1.rtm` | BKSOB |
| `ibksob2.rtm` | BKSOB |
| `ibksob3.rtm` | BKSOB |
| `ibksob4.rtm` | BKSOB |
| `ibksof1.rtm` | BKSOF |
| `ibksof2.rtm` | BKSOF |
| `ibksof3.rtm` | BKSOF |
| `ibksof4.rtm` | BKSOF |
| `ibksopb1.rtm` | BKSOPB, JKSOSB |
| `ibksopb2.rtm` | BKSOPB, JKSOSB |
| `ibksopb3.rtm` | BKSOPB, JKSOSB |
| `ibksopb4.rtm` | BKSOPB, JKSOSB |
| `it6soma1.rtm` | t6som |
| `it6soma2.rtm` | t6som |
| `it6soma3.rtm` | t6som |
| `it6soma4.rtm` | t6som |
| `rbk.rtm` | BKSOF, T6ALSOF, T6SOF |
| `rt6.rtm` | BKSOF, T6ALSOF, T6SOF |
| `t6.rtm` | BKAPL, BKARE, BKJCA, BKPOB, BKSOB, BKSOC, BKSOD, BKSOF (+32 more) |
| `t6sodd1.rtm` | T6SOD, t6sodmsg |
| `t6sodd2.rtm` | T6SOD, t6sodmsg |
| `t6sodh1.rtm` | T6SOD, t6sodmsg |
| `t6sodh2.rtm` | T6SOD, t6sodmsg |
| `t6som1.rtm` | t6som |
| `t6som2.rtm` | t6som |
| `t6som3.rtm` | t6som |
| `t6som4.rtm` | t6som |
| `t6soma1.rtm` | t6som |
| `t6soma2.rtm` | t6som |
| `t6soma3.rtm` | t6som |
| `t6soma4.rtm` | t6som |
| `t6soof1.rtm` | t6soof |
| `temp.rtm` | BKARE, BKING, BKPOB, BKSOC, BKSOD, BKWOC, ISLCF, ISSCF (+22 more) |
| `wt6.rtm` | BKSOC, T6ALSOC, t6soc |

### SO (legacy) Module RTMs (44 total)

| RTM File | Callers |
|----------|---------|
| `curr.rtm` | T6ALSOB, T6ALSOC, T6ALSOPB, T6ESD, T6SOPB, t6sob, t6soc |
| `it6sob1.rtm` | T6ALSOB, t6sob |
| `it6sob2.rtm` | T6ALSOB, t6sob |
| `it6sob3.rtm` | T6ALSOB, t6sob |
| `it6sob4.rtm` | T6ALSOB, t6sob |
| `it6sof1.rtm` | T6ALSOF, T6SOF |
| `it6sof2.rtm` | T6ALSOF, T6SOF |
| `it6sof3.rtm` | T6ALSOF, T6SOF |
| `it6sof4.rtm` | T6ALSOF, T6SOF |
| `it6sopb1.rtm` | T6ALSOPB, T6SOPB |
| `it6sopb2.rtm` | T6ALSOPB, T6SOPB |
| `it6sopb3.rtm` | T6ALSOPB, T6SOPB |
| `it6sopb4.rtm` | T6ALSOPB, T6SOPB |
| `max.rtm` | T6ALSOB, T6ALSOC, T6ALSOF, T6POB, T6SOF, t6sob, t6soc |
| `next.rtm` | T6ALSOB, T6ALSOPB, T6ESD, T6SOPB, t6sob |
| `t6asob3.rtm` | T6ALSOB |
| `t6asoc3.rtm` | T6ALSOC |
| `t6asof3.rtm` | T6ALSOF |
| `t6asopb3.rtm` | T6ALSOPB |
| `t6sob1.rtm` | T6ALSOB, t6sob |
| `t6sob2.rtm` | T6ALSOB, t6sob |
| `t6sob3.rtm` | T6ALSOB, t6sob |
| `t6sob4.rtm` | T6ALSOB, t6sob |
| `t6soc1.rtm` | T6ALSOC, t6soc |
| `t6soc1t.rtm` | T6ALSOC, t6soc |
| `t6soc2.rtm` | T6ALSOC, t6soc |
| `t6soc2t.rtm` | T6ALSOC, t6soc |
| `t6soc3.rtm` | T6ALSOC, t6soc |
| `t6soc3t.rtm` | T6ALSOC, t6soc |
| `t6soc4.rtm` | T6ALSOC, T6ISSRD, t6soc |
| `t6soc4t.rtm` | T6ALSOC, T6ISSRD, t6soc |
| `t6soc4w.rtm` | T6ALSOC, t6soc |
| `t6sof1.rtm` | T6ALSOF, T6SOF |
| `t6sof2.rtm` | T6ALSOF, T6SOF |
| `t6sof3.rtm` | T6ALSOF, T6SOF |
| `t6sof4.rtm` | T6ALSOF, T6SOF |
| `t6sof6.rtm` | T6ALSOF, T6SOF |
| `t6sof7.rtm` | T6ALSOF, T6SOF |
| `t6sopb1.rtm` | T6ALSOPB, T6SOPB |
| `t6sopb2.rtm` | T6ALSOPB, T6SOPB |
| `t6sopb3.rtm` | T6ALSOPB, T6SOPB |
| `t6sopb4.rtm` | T6ALSOPB, T6SOPB |
| `test.rtm` | BKING, T6ALSOB, T6ALSOC, T6ALSOF, T6ALSOPB, T6ESD, T6ING, T6SOF (+3 more) |
| `using.rtm` | T6ALSOB, T6ALSOPB, T6ESD, T6SOPB, t6sob |

### SR Module RTMs (8 total)

| RTM File | Callers |
|----------|---------|
| `bksrd1.rtm` | ISSRD |
| `bksrd1t.rtm` | ISSRD |
| `bksrd2.rtm` | ISSRD |
| `bksrd2t.rtm` | ISSRD |
| `bksrd3.rtm` | ISSRD |
| `bksrd3t.rtm` | ISSRD |
| `bksrd4.rtm` | ISSRD |
| `bksrd4t.rtm` | ISSRD |

### WO Module RTMs (13 total)

| RTM File | Callers |
|----------|---------|
| `bkwoc1.rtm` | BKWOC |
| `bkwoc2.rtm` | BKWOC |
| `bkwoc3.rtm` | BKWOC |
| `bkwoc3oc.rtm` | BKWOC |
| `bkwoc4.rtm` | BKWOC |
| `t6woc1.rtm` | T6WOC |
| `t6woc2.rtm` | T6WOC |
| `t6woc3.rtm` | T6WOC |
| `t6woc4.rtm` | T6WOC |
| `t6woe1.rtm` | T6WOE |
| `t6woe2.rtm` | T6WOE |
| `t6wola1.rtm` | t6wola |
| `t6wolf1.rtm` | t6wolf |

### generic Module RTMs (38 total)

| RTM File | Callers |
|----------|---------|
| `ap.rtm` | BKADC |
| `bkac.rtm` | BKACT, BKACT2 |
| `bkaph1.rtm` | BKADC, BKAPH |
| `bkapha1.rtm` | BKADC, BKAPHA |
| `bkapha2.rtm` | BKADC, BKAPHA |
| `bkapha3.rtm` | BKADC, BKAPHA |
| `bkare1.rtm` | BKADE, BKARE |
| `bkare2.rtm` | BKADE, BKARE |
| `bkare3.rtm` | BKADE, BKARE |
| `bkawc1.rtm` | BKAWC |
| `bkawc2.rtm` | BKAWC |
| `bkawe1.rtm` | BKAWE, BKWOE |
| `bkawe2.rtm` | BKAWE, BKWOE |
| `bkesd1.rtm` | BKMDK |
| `bkesd2.rtm` | BKMDK |
| `bkpob1.rtm` | BKLDB, BKMDG, BKPOB |
| `bkpob2.rtm` | BKLDB, BKMDG, BKPOB |
| `bkpob3.rtm` | BKLDB, BKMDG, BKPOB |
| `bkpob4.rtm` | BKLDB, BKMDG, BKPOB |
| `bkpoe1.rtm` | BKLDB, BKMDG, BKPOEA |
| `bkpoe2.rtm` | BKLDB, BKMDG, BKPOEA |
| `bkprd1.rtm` | BKADC, BKPRD |
| `bkprd2.rtm` | BKADC, BKPRD |
| `bksob1.rtm` | BKADF, BKSOB, JKSDM |
| `bksob2.rtm` | BKADF, BKSOB, JKSDM |
| `bksob3.rtm` | BKADF, BKSOB, JKSDM |
| `bksob4.rtm` | BKADF, BKSOB, JKSDM |
| `bksoc1.rtm` | BKADF, BKSOC, JKSDM |
| `bksoc2.rtm` | BKADF, BKSOC, JKSDM |
| `bksoc3.rtm` | BKADF, BKSOC, JKSDM |
| `bksoc4.rtm` | BKADF, BKSOC, JKSDM |
| `bksof1.rtm` | BKADF, BKSOF, JKSDM |
| `bksof2.rtm` | BKADF, BKSOF, JKSDM |
| `bksof3.rtm` | BKADF, BKSOF, JKSDM |
| `bksof4.rtm` | BKADF, BKSOF, JKSDM |
| `bksof6.rtm` | BKADF, BKSOF, JKSDM |
| `bksof7.rtm` | BKADF, BKSOF, JKSDM |
| `pr.rtm` | BKADC |

---

*RTM cross-reference auto-generated from `samples/rtm_callers.csv` (Pass 101, 2026-06-18).*
