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

GL transaction fields written to BKGLTRAN:
```
BKGL.TRN.TYPE   = "CD"        (Cash Disbursement journal type)
BKGL.TRN.DATE   = CHK.DATE
BKGL.TRN.INVC   = CHK.NUM     (check number as GL reference)
BKGL.TRN.GLACCT = GL account code
BKGL.TRN.GLDPT  = department code
BKGL.TRN.CODE   = vendor code
BKGL.TRN.DC     = "D" or "C"
BKGL.TRN.AMT    = amount (absolute value)
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

*Last updated: 2026-06-11*
*Confidence: 82/100 — Complete workflow traced from TAS Pro source files (Bkaph.SRC + Bkapha.SRC). GL posting fields confirmed. Minor gap: AP-E (voucher selection) not directly read; inferred from AP-H precondition check.*
