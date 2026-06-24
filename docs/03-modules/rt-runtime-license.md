# RT — Runtime License Validator / Session Initializer

Status: verified | Pass 233

EvoERP module code: **RT**

Program: `T7RTMVALID.RWN` | src=NZLICE.LIB | 20 procs | 440 vars

T7RTMVALID is called at session startup by every EvoERP module. It is the shared NZLICE.LIB
(NZ License library) routine responsible for:

1. Validating the EvoERP license file
2. Opening all shared ISIS sub-tables (tax, currency, landed cost)
3. Setting global IS.* module feature flags
4. Configuring tax and currency computation globals
5. Setting up the help system pointers
6. Loading overlay/module paths

---

## Database tables (4 direct)

| Table | Purpose |
|-------|---------|
| BKSYHELP | System help text |
| DBAHLPID | DBA help ID map |
| ISIS | Global ISIS settings (module gates) |
| MKAHIST | Session event log |

The 10 additional ISIS sub-tables are opened via handles but do not appear in the DB file table
(they are opened programmatically by NZLICE.LIB):

| Handle | Table | Purpose |
|--------|-------|---------|
| ISTXG.HNDL | ISTXGRP | Tax group definitions |
| ISTXF.HNDL | ISTXFRM | Tax formula definitions |
| ISTAX.HNDL | ISTAX | Tax amount detail |
| ISHTX.HNDL | ISIS (sub) | ISIS tax header |
| HTAX.HNDL | ISTAX (help) | Tax help table |
| ISMCF.HNDL | ISMCF | Multi-currency master |
| ISMCR.HNDL | ISMCR | Exchange rates |
| ISDUTY.HNDL | ISDUTY | Duty codes |
| ISBRK.HNDL | ISBROKER | Customs broker |
| ISLDF.HNDL | ISLANDF | Landed cost GL accounts |

---

## License variables

| Var | Meaning |
|-----|---------|
| SERIAL | License serial number |
| PRODUCT | Product code |
| APROD | Active product code |
| PDESC | Product description |
| SDATE / EDATE | License start / expiry date |
| SMM/SDD/SYY | License start date components (month/day/year) |
| EMM/EDD/EYY | License expiry date components |
| XMM/XDD/XYY | Current date components (for expiry check) |
| USERS | Maximum licensed user count |
| SF.H | SysFile handle (license file) |
| SER5 / SER6 | License key sub-fields |
| SCBUFF | Serial check buffer |
| LIC | License check result |
| XDBUFF | Extended key buffer |
| USBUFF | User count buffer |
| EVOONLY | EvoERP-only license flag (vs DBA Manufacturing) |
| CHKSUM | License checksum |
| BIGSTR | Checksum string buffer |
| CTNUM | Control number (seat tracking) |

---

## Module feature gates (ISIS.* → IS.*)

These flags are read from the ISIS record and copied to working IS.* variables for fast access:

| ISIS flag | IS.* working var | Feature |
|-----------|-----------------|---------|
| ISIS.TAX | IS.TAX | Tax calculation |
| ISIS.TAX.IN | IS.TAX.IN | Tax-inclusive pricing |
| ISIS.TAX.FRM | IS.TAX.FRM | Tax formula mode |
| ISIS.TAX.PO | IS.PO.TAX | Tax on POs |
| ISIS.MULTI.CURR | IS.MULTI.CURR | Multi-currency |
| ISIS.MULTI.CPAY | IS.MULTI.CPAY | Multi-currency payables |
| ISIS.LANDED.COS | IS.LANDED.COST | Landed cost |
| ISIS.UPC | IS.UPC | UPC/barcode scanning |
| ISIS.RETAIL.PRI | IS.RETAIL.PRICE | Retail pricing |
| ISIS.COMM.PRICE | IS.COMM.PRICE | Commodity pricing |
| ISIS.IMAGING | IS.IMAGING | Document imaging |
| ISIS.AUTO.TAX | IS.AUTO.TAX.CAL | Auto tax calculation |

Additional IS.* working vars (not direct ISIS flags):

| Var | Meaning |
|-----|---------|
| IS.UPC.1 / IS.UPC.2 | UPC mode variants |
| IS.DEMO | Demo mode flag |
| IS.PIC.PATH | Image file path |
| IS.TAX.CVT | Tax conversion flag |
| IS.CUR.CVT | Currency conversion flag |
| IS.EZPAY | EzPay module gate |
| IS.RMA | RMA module gate |
| IS.SPEC.SUP | Special supplier gate |
| IS.SPEC.SUPF / IS.SPEC.SUPT | Special supplier sub-flags |

---

## Tax computation variables

These are set at session init and used by every module that calculates taxes or prices.

| Var | Meaning |
|-----|---------|
| TAXC | Current tax class/code |
| TAMT | Computed tax amount |
| TAXFRT | Freight tax amount |
| FRGTPER | Freight tax percentage |
| TQTY | Taxable quantity |
| IS.RTE | Primary tax rate |
| IS.RTE2 | Secondary tax rate (NZ GST two-tier) |
| IS.LND.RTE | Landed cost tax rate |
| IS.SUBTOT | Subtotal before tax |
| IS.FE | Freight exemption flag |
| IS.CF | Cost factor (tax-inclusive) |
| IS.CFF | Cost factor flag (foreign) |
| IS.DTY | Duty applicable flag |
| IS.EXC | Exchange rate flag |
| IS.OEXC | Original exchange rate |
| IS.DTYP | Duty type code |
| IS.YN | Tax yes/no flag |
| IS.DEC | Decimal precision for currency |
| IS.CVT.MTH | Currency conversion method (direct/indirect) |
| ISLP | IS landed price buffer |
| ISCTR | ISIS lookup counter |
| ISCT | ISIS context |
| PS | Price with surcharge temp |

---

## Localization variables

| Var | Meaning |
|-----|---------|
| TITLESTR | Application title string |
| IS.BASE | Base currency code |
| BASEC | Base currency code (alternate) |
| IS.SYMBOL | Currency symbol |
| IS.SYMPOS | Symbol position (before/after) |
| IS.SYMDESC | Currency description |
| L.EFOR | Label format (date/currency localization) |
| L.CITEM | Localized item label |
| DATE_TYPE | Date format type code |
| DATE_MAXD | Maximum date value |

---

## Config and overlay variables

| Var | Meaning |
|-----|---------|
| CFG.START | Config file start position |
| CFG.BUFFER | Config file record buffer |
| CFG.PATH | Config file path |
| CFG.FULLNAME | Config file full path name |
| HH.CFG.RPTPTR | Handheld report pointer |
| HH.CFG.LABPTR | Handheld label pointer |
| OVL_HNDL | Overlay module handle |
| OVL_PATH | Overlay module path |
| IN_FILE | Input file handle (session) |
| TOGL | Toggle flag (state switch) |

---

## Help system variables

| Var | Meaning |
|-----|---------|
| PROG.HELP.NAME | Program help topic name |
| XYZDBAHTEXT | DBA help text buffer |
| DBAHELP | DBA help flag |
| SYHELP | System help flag |
| SHOW.HELP | Show help trigger |
| XYZDBAHRET | DBA help return value |
| HAVEFILES | Help files present flag |
| BKSY.HELP.PATH | BKSys help path |
| DBA.HELP.REF | DBA help reference |
| DBA.HELP.MAP | DBA help topic map |

---

## Runtime utility vars

| Var | Meaning |
|-----|---------|
| ISIS.HNDL | ISIS record handle |
| NZCT | NZLICE.LIB return code |
| ALEN | NZLICE.LIB array length |
| IKEY | ISIS key buffer |
| RETL | Return label |
| DISP.ERR.MSG | Display error message flag |
| STATUS | Library call status |
| I / I1 / I2 / I4 | Loop/counter integers |
| S / OS / X / U | Single-char work vars |
| BUFFER / TBUFF / NBUFF / EBUFF / X.BUFF | Work buffers |
| KEY | Key buffer |
| R_LINE / RETV / XRETATVAL | Return line / return value |
| XXINFO / PSTR | Info / print string |
| DCP / ATSIZE / TI | Data capture / size / time int |
| X_HNDL | Generic extra handle |

---

## Architecture

T7RTMVALID is called by every module's session-init event (`T7MDefaults` pattern). It:

1. Opens ISIS record → reads all 12 module flags
2. Opens 10 ISIS sub-table handles (tax/currency/landed cost)
3. Reads the license file via SF.H → validates SERIAL/PRODUCT/USERS/SDATE/EDATE
4. Sets OVL_HNDL/OVL_PATH for overlay loading
5. Reads config buffer (CFG.START → CFG.BUFFER → CFG.PATH/CFG.FULLNAME)
6. Sets HH.CFG.RPTPTR/LABPTR for handheld device config
7. Initializes tax globals (IS.RTE/IS.BASE/IS.SYMBOL etc.)
8. Sets help system pointers

The NZ (New Zealand) in NZLICE.LIB indicates this library was added for the NZ GST two-rate
system (IS.RTE / IS.RTE2). It is used by all installations regardless of region because it is
the universal session-init library for EvoERP v7+.

---

## Confidence notes

- All 160 unique vars confirmed from T7RTMVALID.RWN.dec var extraction (Pass 233)
- License flow (SERIAL/PRODUCT/SF.H/ISIS flags) confirmed from prior Pass 164 analysis
- Tax handle names inferred from ISIS table naming conventions (ISTXG=tax group etc.) — not DDF-verified
- OVL_HNDL/OVL_PATH overlay role inferred from name pattern
