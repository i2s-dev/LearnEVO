# SM — Workstation Configuration (t7slsfc.RWN)

Status: verified | Pass 230 2026-06-23

Source: variable extraction from `samples/rwn_decrypted/t7slsfc.RWN.dec`

---

## Overview

`t7slsfc.RWN` is the **Workstation / System-Level Form Config** dialog — an i2 Systems
custom form (compiled from `ISTS.SRC`) that manages all per-workstation and per-module
settings for EvoERP. It is the backing program for a multi-tab settings form (likely
`T7SMK.DFM` — "Evo User Settings", 10 tabs, 67 fields, 164 controls).

**Key characteristics:**
- 663 variables, only 15 dispatch instructions
- Compiled from `ISTS.SRC` (i2 Systems proprietary source — not standard NZLICE/EVO.LIB)
- The tiny instruction count vs. massive var count confirms this is a **config data loader**:
  it reads all settings into variables, opens the DFM form, executes, then saves on close.
- No menu code directly associated (it is called as a sub-program from SM menu logic)

---

## Variable Namespaces

### EVO.CFG.* — Workstation UI Settings (18 vars)

Per-workstation UI behavior stored in BKSYMSTR (or ISTS config table).

| Variable | Meaning |
|----------|---------|
| `EVO.CFG.LANG` | Language (for multi-language support) |
| `EVO.CFG.TOOLBAR` | Show/hide toolbar flag (Y/N) |
| `EVO.CFG.OLWOA` | Open WO module on launch (Y/N) |
| `EVO.CFG.OLPOA` | Open PO module on launch (Y/N) |
| `EVO.CFG.OLINA` | Open IN-A (inventory) on launch |
| `EVO.CFG.OLINB` | Open IN-B on launch |
| `EVO.CFG.OLSOA` | Open SO module on launch |
| `EVO.CFG.OLARA` | Open AR module on launch |
| `EVO.CFG.OLAPA` | Open AP module on launch |
| `EVO.CFG.SOUNDS` | Enable UI sound effects |
| `EVO.CFG.REMIND` | Enable reminders/alerts |
| `EVO.CFG.EREMIND` | Enable email reminders |
| `EVO.CFG.REMSEC` | Reminder check interval (seconds) |
| `EVO.CFG.RSNOOZE` | Reminder snooze duration |
| `EVO.CFG.QPRINT` | Quick-print mode |
| `EVO.CFG.CFU` | Check-for-updates flag |
| `EVO.CFG.TOPMOST` | Window always-on-top flag |
| `EVO.CFG.AREN` | AR enable flag |

### EMAIL.CFG.* — SMTP Email Configuration (49+ vars)

Full email client configuration for EvoERP's built-in email sender (ISJAVA table backend,
Java-based SMTP library).

| Variable | Meaning |
|----------|---------|
| `EMAIL.CFG.SMTP` | SMTP server hostname |
| `EMAIL.CFG.PORT` | SMTP port number |
| `EMAIL.CFG.SEC` | Security mode (TLS/SSL/None) |
| `EMAIL.CFG.EMAIL` | From: email address |
| `EMAIL.CFG.NAME` | From: display name |
| `EMAIL.CFG.USER` | SMTP authentication username |
| `EMAIL.CFG.PASS` | SMTP password (plaintext) |
| `EMAIL.CFG.EPASS` | SMTP password (encrypted copy) |
| `EMAIL.CFG.EFAIL` | Email failure flag |
| `EMAIL.CFG.BCC` | Default BCC address |
| `EMAIL.CFG.SUBJ` | Default subject template |
| `EMAIL.CFG.BOD1`–`BOD9` | Default email body lines (9 lines) |
| `EMAIL.CFG.SIG1`–`SIG9` | Email signature lines (9 lines) |
| `EMAIL.CFG.APTH` | Email application path |
| `EMAIL.CFG.ECB` | Email callback setting |
| `EMAIL.CFG.EVB` | Email verify-before-send flag |

### Per-Module Screen Config

Each module has two config vars controlling which form appears on entry:

| Pattern | Meaning |
|---------|---------|
| `ARA.CFG.ECSCRN` | AR-A: entry/credit memo screen selector |
| `APA.CFG.ECSCRN` | AP-A: entry screen selector |
| `INA.CFG.ECSCRN` | IN-A: inventory entry screen |
| `INB.CFG.ECSCRN` | IN-B: inventory entry screen |
| `POA.CFG.ECSCRN` | PO-A: entry screen |
| `SOA.CFG.ECSCRN` | SO-A: order entry screen |
| `WOA.CFG.ECSCRN` | WO-A: work order entry screen |
| `ARA.CFG.CVTSCRN` | AR-A: convert-to screen selector |
| `APA.CFG.CVTSCRN` | AP-A: convert-to screen |
| ... | (parallel CVTSCRN vars for INA/INB/POA/SOA/WOA) |

These vars determine which sub-screen variant opens when the user enters each module —
allowing per-workstation customization of which form layout is shown.

### Handheld / Paths / Printers

| Variable | Meaning |
|----------|---------|
| `HH.CFG.RPTPTR` | Handheld scanner: report printer pointer |
| `HH.CFG.LABPTR` | Handheld scanner: label printer pointer |
| `DEFPRINTPATH` | Default printer path |
| `DEFPRINTER` | Default printer name |
| `PRINTBOXES` | Show print-dialog boxes (Y/N) |
| `ARA.SAVE` | AR session save flag |
| `APA.SAVE` | AP session save flag |
| `JAVA.PATH` | Path to Java/EvoPVT JAR (primary) |
| `JAVA.PATH2` | Path to Java/EvoPVT JAR (secondary) |
| `XCPATH` | External/cross-path (purpose TBD) |
| `HOTBUTTON1P` | Hot-button 1 launch path |
| `HOTBUTTON2P` | Hot-button 2 launch path |

---

## Architecture Notes

- The 663 variables are populated by reading BKSYMSTR (system master), BKSYPRTR (printer
  config), ISJAVA (Java email config), and ISTS.CFG records at program startup.
- The 15-instruction dispatch is minimal: open handles → EXECUTE_FORM (DFM) → save on close.
- `ARA.SAVE`/`APA.SAVE` are session-state persistence flags — they track whether the AR/AP
  session should resume where it left off or start fresh.
- `JAVA.PATH`/`JAVA.PATH2` feed into the ISJAVA Java runtime that sends email — confirming
  EvoERP uses a Java bridge for SMTP, not a native TAS Pro 7 mail function.
- `HOTBUTTON1P`/`HOTBUTTON2P` are i2 Systems custom quick-launch shortcuts embedded in
  the main menu toolbar.

---

## Related

- `T7SMK.DFM` — "Evo User Settings" form (10 tabs, 67 fields) — almost certainly the DFM
  that t7slsfc.RWN opens via EXECUTE_FORM
- `BKSYMSTR.B` — 286-field system master table (primary config store)
- `BKSYPRTR.B` — Printer configuration table
- `ISJAVA.B` — Java/email configuration table

**Confidence: 78/100** — Variable names extracted and categorized from binary; DFM pairing is
inferred (same-basename rule → T7SLSFC.DFM, not T7SMK.DFM — confirm by checking DFM inventory);
table write targets are inferred from var naming conventions.
