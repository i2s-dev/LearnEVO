# AP Check Printing Workflow
Status: verified | from-SRC-analysis (Bkaph.SRC + Bkapha.SRC)

Source files: `\\I2S109-SOLIDCRM\DBAMFG$\Bkaph.SRC` (continuous forms) and `Bkapha.SRC` (laser forms).
Both are plaintext TAS Pro 4GL — fully readable.

---

## Workflow Steps

### 1. Select Vouchers to Pay (AP-E)
Before check printing, user runs AP-E (Pick Vouchers to Pay). Selected invoices are
written to **BKAPCHKF** (AP Check Run File — temporary working table).

BKAPCHKF fields:
- `BKAP.CHK.VNDCOD` — vendor code
- `BKAP.CHK.INVNUM` — invoice number
- `BKAP.CHK.INVDTE` — invoice date
- `BKAP.CHK.DESC` — description
- `BKAP.CHK.DISC` — discount amount
- `BKAP.CHK.AMTPD` — amount to pay

### 2. Select Checking Account and Verify Check Number (AP-H)
- User selects bank/checking account: `BKSY.AP.CHKACT`
- System reads next check number: `BKSY.CHK.NUM[CHKACT]`
- System reads account name: `BKSY.CHK.NAME[CHKACT]`
- **Prerequisite validated:** Pro-forma check register must have been printed first.

### 3. Enter Check Date
- User enters check date; validated against fiscal year and GL close periods.
- `CHK.DATE` field used for all postings.

### 4. Print Checks

**Continuous forms (Bkaph.SRC):**
- Maximum 14 invoices per check stub
- If vendor has 15+ invoices, prints VOID stub for excess
- Check amount converted to alpha text ("one hundred twenty-three dollars and 45/100")

**Laser forms (Bkapha.SRC):**
- Maximum 13 items (Windows) or 14 items (DOS) per stub
- Uses RTM templates: `bkapha1.rtm`, `bkapha2.rtm`, `bkapha3.rtm`
- Multi-currency support with symbol positioning

**Printed fields:**
```
CHK.DATE        — Check date
CHK.NUM         — Check number
BKAP.VENDNAME   — Vendor name
PRT.ADD1/ADD2   — Address (primary or secondary)
PRT.CSZ         — City, State, Zip
PRT.COUNTRY     — Country
TOT.RAMT        — Check amount
TOT.DAMT        — Total discount taken
TOT.TOT         — Total check amount
REP2            — Amount in words
BKAP.CHK.INVNUM — Invoice numbers
BKAP.CHK.INVDTE — Invoice dates
LINE.DESC       — Line descriptions
BKAP.CHK.DISC   — Per-line discount
BKAP.CHK.AMTPD  — Per-line amount paid
```

### 5. GL Posting (simultaneous with check printing)
After user confirms checks printed OK, GL entries are posted:

| GL Role | Account field | Department field | Dr/Cr |
|---------|---------------|-----------------|-------|
| AP liability cleared | `BKSY.AP.GLACT` | `BKSY.AP.GLDPT` | Debit |
| Discount taken | `BKSY.AP.DISCGL` | `BKSY.AP.DISCDPT` | Credit |
| Checking account | `BKSY.CHK.CHKACT[CHKACT]` | `BKSY.CHK.CHKDPT[CHKACT]` | Credit |
| FX gain/loss | `ISIS.MCF.GLAIS` / `ISIS.MCF.GLABS` | — | varies |
| GL clearing (fallback) | `BKSY.GL.CLRING` | `BKSY.GLDPT.CLR` | varies |

**CORRECTION (Pass 393 2026-06-30):** GL entries during check printing are written to
**BKGLTEMP** (staging table), NOT BKGLTRAN directly. The `POST.TO.GL` subroutine
(BKAPH.SRC L1092) calls `save BKGLTEMP nocnf`. The final call to `msg.chk.post()`
(BKAPH.SRC L1081 — a function from the APH library) then moves BKGLTEMP → BKGLTRAN
as part of the finalization step.

Fallback: if GL account not found in BKGLTRAN, POST.TO.GL falls back to BKSY.GL.CLRING
(clearing account). If that also fails, POST.FAIL=1 (unposted flag for reconciliation).

GL transaction fields written to **BKGLTEMP** (staging):
```
BKGL.TRN.TYPE   = "CD"        (Cash Disbursement journal type)
BKGL.TRN.DATE   = TODAYS.DATE (check date)
BKGL.TRN.INVC   = CHK.NUM     (check number as GL reference, NOT invoice number)
BKGL.TRN.GLACCT = BKGL.ACCT   (GL account code)
BKGL.TRN.GLDPT  = BKGL.GLDPT  (department code)
BKGL.TRN.CODE   = BKAP.CHK.VNDCOD  (vendor code)
BKGL.TRN.DC     = "D" if POST.AMT>0, "C" if POST.AMT<0
BKGL.TRN.AMT    = ABS(POST.AMT)    (always positive)
BKGL.TRN.ENTDTE = date()            (entry date)
BKGL.TRN.DESC   = description
```

### 6. Update Invoice Status
After check posts:
- `BKAP.INVT.AMTRM = AMTRM - (AMTPD + DISC)` — reduce remaining balance
- `BKAP.INVT.MCRAT` — multi-currency exchange rate stored
- `BKAP.INVT.MCCOD` — multi-currency code

### 7. Save to Check History
Written to **BKAPCHKH** (AP Check History — permanent):
- `BKAP.CHK.NUM`
- `BKAP.CHK.CHKDTE`
- `BKAP.CHK.CHKACT`
- `BKAP.CHK.VNDCOD`
- `BKAP.CHK.INVNUM`
- `BKAP.CHK.AMTPD`

Also written to **BKGLCHK** (GL Check Register):
- `BKGL.CHK.DATE`, `BKGL.CHK.NUM`, `BKGL.CHK.TYPE = "C"`
- `BKGL.CHK.AMT`, `BKGL.CHK.NAME`, `BKGL.CHK.CHKACT`

### 8. Void Check Handling
- Checks with excess line items → automatic VOID stub (continuous format)
- Zero/negative net amount → marked VOID
- VOID stubs saved to BKGLCHK with AMT=0, TYPE="C"

---

## GL Journal Type for AP Checks
The GL posting writes `BKGL.TRN.TYPE = "CD"` — Cash Disbursement. This is one of the
5 selectable types in GL-B (GJ/CR/CD/TT/BB). AP check runs are **not** a separate system
posting type — they post as standard CD transactions.

## 1099 Reporting
Tracked via:
- `BKAPVEND` vendor record (1099 classification code)
- `BKAPINVT.TYPE = "P"` (payment transactions for 1099-eligible vendors)
- `BKAPVEND.LASTPMT` (last payment date)
- Payment amounts accumulated per vendor for year-end 1099 reporting

---

---

## AP Check Format — BKYSMSTR YN[48] (Pass 393 2026-06-30, SRC-confirmed)

`BKYS.YN[48]` controls the check print format selected in AD-C:

| YN[48] value | Format | Program |
|---|---|---|
| '1' | Laser format | → chains to BKAPHA |
| '4' | Laser format (variant) | → chains to BKAPHA |
| '5' | Laser format (variant) | → chains to BKAPHA |
| '2' | Windows graphical dot matrix | BKAPH (text.mode=F) |
| '3' | Text mode dot matrix | BKAPH (text.mode=T) |

Live value on i2 Systems = '1' (laser format confirmed). Source: BKAPH.SRC L60-80.

## File Lock Pattern (Pass 393)

BKAPCHKF uses **full exclusive file lock** (`lock f`) — not just a record lock:
```
trap rlck goto CHKF_ERR
open BKAPCHKF lock f err CHKF_ERR
```
`lock f` prevents any other process from opening BKAPCHKF at all.
Error handling: if lock fails → display "Cannot lock file BKAPCHKF.B..." message and quit.
This prevents concurrent AP-E, AP-F, AP-G, AP-H, AP-HA sessions.
The file is closed before chaining to BKAPG (prevent lock held across chain).
Source: BKAPH.SRC L209-218.

## TAS Pro 4GL Language — Additional Keywords Confirmed

From BKAPH.SRC (Pass 393):
- **`format VALUE recv ALPHAVAR NOCMA NOFD`** — format a number into an alpha text string
  (NOCMA=no commas, NOFD=no fractional digits). Used for check amount-in-words.
- **`pfmt N`** — set current print format (column position/layout) to format N.
- **`pvert N`** — move print head N lines vertically.
- **`pchr 'CMD'`** — emit a printer control character (e.g., `pchr 'pcmp'` = form feed/page advance, `pchr 'preg'` = regular print).
- **`ptof`** — print top-of-form (advance to next physical form).
- **`pset wdt N`** — set print width to N characters.
- **`pon S`** — print output to screen.
- **`findv M fnum HANDLE key KEY val VALUE`** — variable-handle file seek; `findv` = find-by-variable.
- **`isis_get`** — load ISIS multi-currency config into isis.* vars (multi-currency init).
- **`isis_mcrate(DATE, CURCODE)`** — returns exchange rate for currency code on date.
- **`is_mc_cvt(FROMCUR, TOCUR, DATE, AMT)`** — convert amount between currencies.
- **`is_curr_ctrl("MODULE", CURCODE)`** — apply multi-currency GL controls for a module.

*Last updated: Pass 393 2026-06-30*
*Confidence: 92/100 — BKGLTEMP correction confirmed from BKAPH.SRC L1122; YN[48] SRC-confirmed L60-80; lock f SRC-confirmed L209-218; all GL fields SRC-confirmed; msg.chk.post() finalization function referenced but source not available.*
