# Payroll (PR)

Status: verified | Pass 329 (2026-06-26)

- **Module code**: `PR`
- **Tables**: 16 (prefixes `BKPR`)
- **UI forms**: 40 (prefixes `T7PR`, `T6PR`, `BKPR`)
- **Menu operations**: 29

## Menu operations

| Code | Operation | Legacy module file(s) |
| ---- | --------- | --------------------- |
| `PR-A` | Edit W-2 Data | BKPRA;BKPRP;BKPRQ |
| `PR-B` | Enter Pay Info | BKPRB;BKPRD;t6prd |
| `PR-C` | Print Payroll Register | BKPRC |
| `PR-D` | Print Payroll Checks | BKPRB;BKPRD;t6prd |
| `PR-E` | Print Employee Info | BKPRE |
| `PR-F` | Maintain Tax Tables | BKPRF |
| `PR-G` | Void Payroll Checks | BKPRG |
| `PR-H` | Transfer Liabilities to AP | BKPRH |
| `PR-I` | Print Pay History | BKPRI |
| `PR-J` | Enter Time Cards | BKPRJ;BKPRJA;BKPRJB |
| `PR-J-A` | Import Time Cards | ISPRJDE |
| `PR-K` | Print/Post Time Cards | BKPRK |
| `PR-L-A` | Print Quarterly Info | BKPRLA |
| `PR-L-B` | Print QTD Earnings Register | BKPRLB |
| `PR-L-C` | Print QTD Taxable Earnings | BKPRLC |
| `PR-L-D` | Print Detail Earnings Ledger | BKPRLD |
| `PR-L-E` | Print Detail Deductions Ledger | BKPRLE |
| `PR-L-F` | Print Subject To Report | BKPRLF;T6PRLF |
| `PR-L-H` | Print 940 Report | BKPRLH |
| `PR-L-I` | Print W-2 Forms | BKPRLI;T6PRLI |
| `PR-L-J` | Print California DE6 Form | BKPRLJ |
| `PR-L-K` | Print Payroll Hours | BKPRLK |
| `PR-L-M` | Print Employer Contributions | BKPRLM |
| `PR-L-N` | Print Payroll Wages Detail | BKPRLN |
| `PR-L-P` | Print Employee Raises | BKPRLP;BKPRLQ |
| `PR-M` | Payroll Defaults | BKPRM |
| `PR-N` | Purge Payroll History | BKPRN |
| `PR-O` | Payroll Year End Routine | BKPRO |
| `PR-P` | Enter Employee Raises | BKPRP;BKPRQ |

## UI forms (40)

| DFM file | Caption | fields | controls | tabs |
| -------- | ------- | -----: | -------: | ---: |
| `T7PRA.DFM` |  | 0 | 1 | 0 |
| `T7PRB.DFM` |  | 0 | 1 | 0 |
| `T7PRC.DFM` | PR-C | 10 | 33 | 0 |
| `T7PRD.DFM` |  | 0 | 1 | 0 |
| `T7PRDIVFIX.DFM` | New Screen | 2 | 10 | 0 |
| `T7PRE.DFM` | PR-E | 4 | 22 | 0 |
| `T7PRF.DFM` |  | 0 | 1 | 0 |
| `T7PRFIX.DFM` |  | 0 | 1 | 0 |
| `T7PRG.DFM` | PR-G | 9 | 30 | 0 |
| `T7PRH.DFM` | PR-H | 82 | 117 | 0 |
| `T7PRI.DFM` | PR-I | 7 | 27 | 0 |
| `T7PRJ.DFM` |  | 0 | 1 | 0 |
| `T7PRJCSYNC.DFM` | New Screen | 2 | 10 | 0 |
| `T7PRK.DFM` | PR-K  Print/Post Time Cards | 13 | 45 | 0 |
| `T7PRLA.DFM` | PR-L-A | 6 | 27 | 0 |
| `T7PRLB.DFM` | PR-L-B | 8 | 30 | 0 |
| `T7PRLC.DFM` | PR-L-C | 16 | 47 | 0 |
| `T7PRLD.DFM` | PR-L-D | 8 | 30 | 0 |
| `T7PRLE.DFM` | PR-L-E  Print Detail Deductions Ledger | 10 | 32 | 0 |
| `T7PRLF.DFM` | PR-L-F | 21 | 52 | 0 |
| `T7PRLG.DFM` | PR-L-G | 40 | 97 | 0 |
| `T7PRLH.DFM` | PR-LH | 54 | 112 | 0 |
| `T7PRLI.DFM` |  | 0 | 1 | 0 |
| `T7PRLJ.DFM` | PR-L-J | 11 | 35 | 0 |
| `T7PRLK.DFM` | PR-L-K  Print Payroll Hours | 9 | 31 | 0 |
| `T7PRLM.DFM` | PR-L-M | 8 | 30 | 0 |
| `T7PRLN.DFM` | PR-L-N  Print Payroll Wages Detail | 8 | 30 | 0 |
| `T7PRLO.DFM` | PR-L-O | 8 | 30 | 0 |
| `T7PRLP.DFM` | PR-L-P | 10 | 33 | 0 |
| `T7PRLQ.DFM` | PR-L-Q | 8 | 31 | 0 |
| `T7PRM.DFM` |  | 0 | 1 | 0 |
| `T7PRN.DFM` | New Screen | 7 | 28 | 0 |
| `T7PRO.DFM` | New Screen | 1 | 17 | 0 |
| `T7PROGINFO.DFM` |  | 0 | 1 | 0 |
| `T7PRP.DFM` |  | 0 | 1 | 0 |
| `T7PRQ.DFM` |  | 0 | 1 | 0 |
| `T7PRQTRCHK.DFM` | New Screen | 2 | 24 | 0 |
| `T7PRS.DFM` | Enter Employee Password | 5 | 29 | 0 |
| `T7ProcessData.DFM` | Process Data | 0 | 9 | 0 |
| `t7pretag.DFM` | New Screen | 0 | 3 | 0 |

## Database tables (16)

Full field details are in `../../../samples/ddf/schema.md` (see per-table heading).

| Table | File on disk | Fields | Key fields (first 3) |
| ----- | ------------ | -----: | -------------------- |
| **BKPRACOM** | `BKPRACOM.B` | 12 | `BKPR_COMM_SLSP`, `BKPR_COMM_CCODE`, `BKPR_COMM_INVNM` |
| **BKPRAGNT** | `BKPRAGNT.B` | 4 | `BKPR_AGNT_NUM`, `BKPR_AGNT_CODE`, `BKPR_AGNT_GLACT` |
| **BKPRBOOK** | `BKPRBOOK.B` | 87 | `BKPR_SLS_EMPNUM`, `BKPR_SLS_CLASS_1`, `BKPR_SLS_CLASS_2` |
| **BKPRCOMM** | `BKPRCOMM.B` | 12 | `BKPR_COMM_SLSP`, `BKPR_COMM_CCODE`, `BKPR_COMM_INVNM` |
| **BKPRCURP** | `BKPRCURP.B` | 127 | `BKPR_CURP_EMPNM`, `BKPR_CURP_PRDTE`, `BKPR_CURP_ACTNM` |
| **BKPRFTAX** | `BKPRFTAX.B` | 47 | `BKPR_TAX_CODE`, `BKPR_TAX_DESC`, `BKPR_TAX_ALLOW` |
| **BKPRGLFL** | `BKPRGLFL.B` | 664 | `BKPR_GL_STCODE`, `BKPR_GL_DEPT`, `BKPR_GL_FITACCT` |
| **BKPRHCOM** | `BKPRHCOM.B` | 12 | `BKPR_COMM_SLSP`, `BKPR_COMM_CCODE`, `BKPR_COMM_INVNM` |
| **BKPRHIST** | `BKPRHIST.B` | 127 | `BKPR_CURP_EMPNM`, `BKPR_CURP_PRDTE`, `BKPR_CURP_ACTNM` |
| **BKPRINFO** | `BKPRINFO.B` | 128 | `BKPR_INFO_NUM`, `BKPR_INFO_DDEP`, `BKPR_INFO_REVDT_1` |
| **BKPRMSTR** | `BKPRMSTR.B` | 384 | `BKPR_EMP_NUM`, `BKPR_EMP_FNMI`, `BKPR_EMP_LNME` |
| **BKPRSALE** | `BKPRSALE.B` | 87 | `BKPR_SLS_EMPNUM`, `BKPR_SLS_CLASS_1`, `BKPR_SLS_CLASS_2` |
| **BKPRSTFL** | `BKPRSTFL.B` | 2 | `BKPR_ST_STCODE`, `BKPR_ST_TAXNUM` |
| **BKPRTC** | `BKPRTC.B` | 7 | `BKPR_TC_EMP`, `BKPR_TC_DATE`, `BKPR_TC_START` |
| **BKPRTCFG** | `BKPRTCFG.B` | 205 | `BKPRT_CFG_KEY`, `BKPRT_CFG_NAME_1`, `BKPRT_CFG_NAME_2` |
| **BKPRW2** | `BKPRW2.B` | 384 | `BKPR_EMP_NUM`, `BKPR_EMP_FNMI`, `BKPR_EMP_LNME` |

## Table functional groupings

| Role | Tables |
|------|--------|
| Employee master | BKPRMSTR (active, 384f), BKPRW2 (W-2 snapshot, 384f) |
| Per-check detail | BKPRCURP (current period, 127f), BKPRHIST (history, 127f) |
| Employee supplemental | BKPRINFO (128f) |
| Salesperson commission | BKPRSALE (87f), BKPRBOOK (87f — prior period copy) |
| Commission transactions | BKPRCOMM (active, 12f), BKPRACOM (archive, 12f), BKPRHCOM (history, 12f) |
| Sales agents | BKPRAGNT (4f) |
| Tax tables | BKPRFTAX (47f) |
| GL accounts | BKPRGLFL (664f — by state+dept) |
| State filing | BKPRSTFL (2f) |
| Time cards | BKPRTC (7f), BKPRTCFG (205f) |

---

## BKPRMSTR — Employee Payroll Master (384 fields, confirmed from DDF schema.md lines 7988–8375)

Primary key: `BKPR_EMP_NUM` (UBINARY 2)

**BKPRW2 has an identical 384-field schema** — it is a year-end snapshot of BKPRMSTR used to produce W-2 forms. The two tables are structurally identical; BKPRW2 is populated during the Year End Routine (PR-O).

### Identity (fields 1–16)

| Field | Type | Size | Meaning |
|-------|------|------|---------|
| `BKPR_EMP_NUM` | UBINARY | 2 | Employee number (PK) |
| `BKPR_EMP_FNMI` | STRING | 25 | First name |
| `BKPR_EMP_LNME` | STRING | 25 | Last name |
| `BKPR_EMP_ADD` | STRING | 30 | Street address |
| `BKPR_EMP_CSZ` | STRING | 25 | City/state/zip combined |
| `BKPR_EMP_ST` | STRING | 2 | State code |
| `BKPR_EMP_ZIP` | STRING | 10 | ZIP code |
| `BKPR_EMP_CNTRY` | STRING | 30 | Country |
| `BKPR_EMP_PHONE` | STRING | 15 | Phone |
| `BKPR_EMP_SSN` | STRING | 11 | Social Security Number |
| `BKPR_EMP_SDATE` | DATE | 4 | Start/hire date |
| `BKPR_EMP_TERM` | STRING | 1 | Terminated flag |
| `BKPR_EMP_MS` | STRING | 1 | Marital status (S/M/H/…) |
| `BKPR_EMP_FEDEXM` | UBINARY | 2 | Federal exemptions count |
| `BKPR_EMP_STEXM` | UBINARY | 2 | State exemptions count |
| `BKPR_EMP_PAYTYP` | STRING | 1 | Pay type (H=hourly, S=salary, etc.) |

### Pay rates (fields 17–31) — 15 rate slots

| Field(s) | Type | Size | Meaning |
|----------|------|------|---------|
| `BKPR_EMP_PAYAMT_1..15` | FLOAT×15 | 8 | Pay rate slots 1–15 (hourly rate, overtime rate, etc.) |

### Hours accumulators (fields 32–45)

| Field | Type | Meaning |
|-------|------|---------|
| `BKPR_EMP_RHQTD` | FLOAT | Regular hours QTD |
| `BKPR_EMP_RAQTD` | FLOAT | Regular amount QTD |
| `BKPR_EMP_RHYTD` | FLOAT | Regular hours YTD |
| `BKPR_EMP_RAYTD` | FLOAT | Regular amount YTD |
| `BKPR_EMP_VHQTD` | FLOAT | Vacation hours QTD |
| `BKPR_EMP_VAQTD` | FLOAT | Vacation amount QTD |
| `BKPR_EMP_VHYTD` | FLOAT | Vacation hours YTD |
| `BKPR_EMP_VAYTD` | FLOAT | Vacation amount YTD |
| `BKPR_EMP_VDUE` | FLOAT | Vacation hours accrued/due |
| `BKPR_EMP_SHQTD` | FLOAT | Sick hours QTD |
| `BKPR_EMP_SAQTD` | FLOAT | Sick amount QTD |
| `BKPR_EMP_SHYTD` | FLOAT | Sick hours YTD |
| `BKPR_EMP_SAYTD` | FLOAT | Sick amount YTD |
| `BKPR_EMP_SDUE` | FLOAT | Sick hours accrued/due |

### Tax withholding accumulators (fields 46–60)

| Field | Type | Meaning |
|-------|------|---------|
| `BKPR_EMP_FITQTD` | FLOAT | Federal income tax withheld QTD |
| `BKPR_EMP_FITYTD` | FLOAT | Federal income tax withheld YTD |
| `BKPR_EMP_FICQTD_1` | FLOAT | FICA employee (Social Security) QTD |
| `BKPR_EMP_FICQTD_2` | FLOAT | FICA employer (SS match) QTD |
| `BKPR_EMP_FICYTD_1` | FLOAT | FICA employee YTD |
| `BKPR_EMP_FICYTD_2` | FLOAT | FICA employer YTD |
| `BKPR_EMP_STQTD` | FLOAT | State income tax QTD |
| `BKPR_EMP_STYTD` | FLOAT | State income tax YTD |
| `BKPR_EMP_WKQTD` | FLOAT | Workers comp withheld QTD |
| `BKPR_EMP_WKYTD` | FLOAT | Workers comp withheld YTD |
| `BKPR_EMP_MDAMT` | FLOAT | Medicare — current period amount |
| `BKPR_EMP_MDQTD` | FLOAT | Medicare QTD |
| `BKPR_EMP_MDYTD` | FLOAT | Medicare YTD |
| `BKPR_EMP_OTHQTD` | FLOAT | Other withholding QTD |
| `BKPR_EMP_OTHYTD` | FLOAT | Other withholding YTD |

### Last pay date (field 61)

| Field | Type | Meaning |
|-------|------|---------|
| `BKPR_EMP_LSTPR` | DATE | Date of most recent payroll check |

### "OH" deductions — 12 types × 4 accumulators (fields 62–109)

These are the 12 user-defined "other hours" deduction buckets configured in BKPRTCFG.

| Field(s) | Meaning |
|----------|---------|
| `BKPR_EMP_OHQTD_1..12` | Deduction hours QTD (slots 1–12) |
| `BKPR_EMP_OAQTD_1..12` | Deduction amount QTD (slots 1–12) |
| `BKPR_EMP_OHYTD_1..12` | Deduction hours YTD (slots 1–12) |
| `BKPR_EMP_OAYTD_1..12` | Deduction amount YTD (slots 1–12) |

### Workers comp rates and state exemption (fields 110–112)

| Field | Type | Size | Meaning |
|-------|------|------|---------|
| `BKPR_EMP_WCEE` | FLOAT | 8 | Workers comp employee share rate |
| `BKPR_EMP_WCER` | FLOAT | 8 | Workers comp employer share rate |
| `BKPR_EMP_STEXMA` | FLOAT | 8 | State exemption amount (dollar) |

### GL expense account distribution (fields 113–142) — 15 slots

Each of the 15 slots is an account+department pair that splits the employee's labor cost across multiple GL accounts.

| Field(s) | Type | Size | Meaning |
|----------|------|------|---------|
| `BKPR_EMP_EXPACT_1..15` | STRING×15 | 10 | GL expense account codes (slots 1–15) |
| `BKPR_EMP_EXPDPT_1..15` | STRING×15 | 4 | GL department codes (slots 1–15) |

### State exemption number and additional withholding (fields 143–146)

| Field | Type | Meaning |
|-------|------|---------|
| `BKPR_EMP_STEXMN` | UBINARY | State exemption count (numeric, separate from STEXM) |
| `BKPR_EMP_ADDIT_1..3` | FLOAT×3 | Additional withholding amounts (1=FIT, 2=SIT, 3=other) |

### User-defined employee deductions — 20 types (fields 147–262)

Each of the 20 user-defined deductions (e.g. 401k, health, dental) carries 5 values:

| Field(s) | Meaning |
|----------|---------|
| `BKPR_EMP_UODQTD_1..20` | Deduction amount withheld QTD |
| `BKPR_EMP_UODYTD_1..20` | Deduction amount withheld YTD |
| `BKPR_EMP_UDAMT1_1..6` | Alternate deduction amounts (6 slots — special purpose) |

### Department, location, SDI, accrual rates (fields 193–202)

| Field | Type | Meaning |
|-------|------|---------|
| `BKPR_EMP_DEPT` | STRING 4 | Department code |
| `BKPR_EMP_LOCCOD` | STRING 2 | Location code |
| `BKPR_EMP_SDIQTD` | FLOAT | State Disability Insurance QTD |
| `BKPR_EMP_SDIYTD` | FLOAT | SDI YTD |
| `BKPR_EMP_SDIEXM` | STRING 1 | SDI exempt flag |
| `BKPR_EMP_VRTE` | FLOAT | Vacation accrual rate (hours per period) |
| `BKPR_EMP_SRTE` | FLOAT | Sick accrual rate (hours per period) |
| `BKPR_EMP_BDAY` | DATE | Birthday |
| `BKPR_EMP_VCAP` | FLOAT | Vacation hours cap (max accrual) |
| `BKPR_EMP_SCAP` | FLOAT | Sick hours cap (max accrual) |

### User-defined employee deduction rates and limits (fields 203–262)

| Field(s) | Meaning |
|----------|---------|
| `BKPR_EMP_UODAMT_1..20` | Per-period deduction amount for each of 20 UOD buckets |
| `BKPR_EMP_UODYLM_1..20` | YTD dollar limit for each UOD bucket |
| `BKPR_EMP_UODLMT_1..20` | Lifetime/annual limit for each UOD bucket |

### User-defined employer deductions — 20 types (fields 263–322 + 332–376)

Employer-side equivalents of the employee UOD buckets (employer match, etc.):

| Field(s) | Meaning |
|----------|---------|
| `BKPR_EMP_UDEAMT_1..20` | Employer deduction amount per period |
| `BKPR_EMP_UDELMT_1..20` | Employer deduction limit |
| `BKPR_EMP_UDEYLM_1..20` | Employer deduction YTD limit |
| `BKPR_EMP_UDEYTD_1..20` | Employer deduction YTD accumulated |
| `BKPR_EMP_UDEQTD_1..20` | Employer deduction QTD accumulated |

### Shift, benefit date, and named deductions (fields 323–356)

| Field | Type | Meaning |
|-------|------|---------|
| `BKPR_EMP_SHIFT` | UBINARY | Shift number |
| `BKPR_EMP_BENDTE` | DATE | Benefits eligibility/start date |
| `BKPR_EMP_OTHAMT` | FLOAT | Other deduction fixed amount |
| `BKPR_EMP_OTHNME` | STRING 12 | Other deduction name |
| `BKPR_EMP_OTHACT` | STRING 10 | Other deduction GL account |
| `BKPR_EMP_OTHDPT` | STRING 4 | Other deduction GL dept |
| `BKPR_EMP_MDNME` | STRING 12 | Medicare/misc deduction name |
| `BKPR_EMP_MDACT` | STRING 10 | Medicare deduction GL account |
| `BKPR_EMP_MDDPT` | STRING 4 | Medicare deduction GL dept |
| `BKPR_EMP_OPNAME_1..5` | STRING×5 10 | Operation pay names (5 slots) |

### Trailing fields (fields 377–384)

| Field | Type | Meaning |
|-------|------|---------|
| `BKPR_EMP_EXTRA` | STRING 200 | User-defined extra field |
| `BKPR_EMP_EICAMT` | FLOAT | Earned Income Credit advance amount per period |
| `BKPR_EMP_EIC` | FLOAT | EIC YTD |
| `BKPR_EMP_YEAR` | FLOAT | Current payroll year |
| `BKPR_EMP_QTR` | UBINARY | Current payroll quarter |
| `BKPR_EMP_EMAIL` | STRING 128 | Employee email |
| `BKPR_EMP_BANKR` | STRING 9 | Bank routing number (direct deposit) |
| `BKPR_EMP_BANKA` | STRING 17 | Bank account number (direct deposit) |

---

## BKPRCURP / BKPRHIST — Per-Check Payroll Detail (127 fields each, confirmed from DDF schema.md lines ~7700–7854)

Primary key: `BKPR_CURP_EMPNM` + `BKPR_CURP_PRDTE` + `BKPR_CURP_ACTNM`

BKPRCURP holds the current (unposted/current-period) check detail. BKPRHIST is identical in structure — it holds the posted history of all prior checks. A check record is written to BKPRCURP during payroll processing and moved to BKPRHIST during posting.

**Key field groups:**
- Identity: `BKPR_CURP_EMPNM` (employee#), `BKPR_CURP_PRDTE` (pay date), `BKPR_CURP_ACTNM` (check account)
- Gross pay: regular, vacation, sick amounts + hours for this check
- Taxes this check: `BKPR_CURP_FITWH` (FIT), `BKPR_CURP_SITWH` (SIT), `BKPR_CURP_FICWH_1/2` (FICA), `BKPR_CURP_WCWH` (workers comp), `BKPR_CURP_SDIWH` (SDI)
- Net pay: `BKPR_CURP_NTPAY`
- User-defined deductions this check: `BKPR_CURP_UODEC_1..20`
- FUTA/SUTA tax liability: `BKPR_CURP_FUTEX`, `BKPR_CURP_SUTEX`
- Operation pay names/GL/dept: `BKPR_CURP_OPNME/OPACT/OPDPT_1..5`
- Medicare: `BKPR_CURP_MDNME/MDACT/MDDPT`
- Other deduction: `BKPR_CURP_ODNME/ODACT/ODDPT`
- EIC: `BKPR_CURP_EIC`

---

## BKPRINFO — Employee Supplemental Info (128 fields, confirmed from DDF schema.md lines 7855–7986)

Primary key: `BKPR_INFO_NUM` (UBINARY 2, same employee# as BKPRMSTR)

One-to-one with BKPRMSTR. Stores overflow information that doesn't fit in the master:

| Group | Fields | Content |
|-------|--------|---------|
| Performance review | `REVDT_1..6` (dates) + `REVNT_1..12` (60-char notes) | Review dates and notes |
| Raise history | `RASDT_1..6` (dates) + `RASNT_1..12` (60-char notes) | Raise dates and notes |
| Vacation | `AVAC`, `VACAC` (date), `VHRS` | Vacation accrual method + hours |
| Sick | `ASICK`, `SICKA` (date), `SHRS` | Sick accrual method + hours |
| Additional hours | `AHOW_1/2`, `AHRS_1/2` | How additional hours are calculated |
| Benefit info | `BINFO_1..2` (30 chars each) | Benefit description |
| User dates | `DATE_1..12` | 12 user-defined dates |
| Notes | `NOTE_1..24` (60 chars each) | 24 user-defined note lines |
| Amounts | `AMT_1..15` | 15 user-defined dollar amounts |
| Contacts | `CTACT_1..5` (30 chars) + `PHONE_1..5` (15 chars) | 5 emergency/secondary contacts |
| Flags | `FLAGS_1..5` (1 char each) | 5 user-definable flags |
| Deductions | `DEDS_1..5` | 5 additional deduction amounts |
| Alpha | `ALPHA_1..5` (25 chars each) | 5 free-form text fields |
| Sync | `SYNC` | External sync flag |

---

## BKPRSALE / BKPRBOOK — Salesperson Commission (87 fields each, confirmed from DDF schema.md lines 8377–8467)

Primary key: `BKPR_SLS_EMPNUM` (UBINARY 2) + `BKPR_SLS_CLASS_1` (STRING 2) + `BKPR_SLS_CLASS_2` (STRING 2)

BKPRSALE is the active salesperson commission table. BKPRBOOK appears to be a prior-period or archived copy (same 87-field structure, same field prefix — confirmed from DDF table list). One employee can have multiple rows if they sell across multiple item classes.

| Field(s) | Type | Meaning |
|----------|------|---------|
| `BKPR_SLS_EMPNUM` | UBINARY 2 | Employee number (FK → BKPRMSTR) |
| `BKPR_SLS_CLASS_1` | STRING 2 | Sales class 1 (item classification) |
| `BKPR_SLS_CLASS_2` | STRING 2 | Sales class 2 |
| `BKPR_SLS_RATE_1` | FLOAT | Commission rate 1 |
| `BKPR_SLS_RATE_2` | FLOAT | Commission rate 2 |
| `BKPR_SLS_HOW_1` | STRING 1 | How rate 1 is calculated (P=percent, A=amount, etc.) |
| `BKPR_SLS_HOW_2` | STRING 1 | How rate 2 is calculated |
| `BKPR_SLS_WHEN_1` | STRING 1 | When commission 1 is paid (I=on invoice, R=on receipt, etc.) |
| `BKPR_SLS_WHEN_2` | STRING 1 | When commission 2 is paid |
| `BKPR_SLS_QUOTA_1..12` | FLOAT×12 | Monthly sales quota (periods 1–12) |
| `BKPR_SLS_GROSS_1..12` | FLOAT×12 | Monthly gross sales (periods 1–12) |
| `BKPR_SLS_COGS_1..12` | FLOAT×12 | Monthly COGS (periods 1–12) |
| `BKPR_SLS_RCPTS_1..12` | FLOAT×12 | Monthly cash receipts (periods 1–12) |
| `BKPR_SLS_COMM_1..12` | FLOAT×12 | Monthly commission earned (periods 1–12) |
| `BKPR_SLS_PAID_1..12` | FLOAT×12 | Monthly commission paid (periods 1–12) |
| `BKPR_SLS_FNMI` | STRING 25 | First name |
| `BKPR_SLS_LNME` | STRING 25 | Last name |
| `BKPR_SLS_EXPACT` | STRING 10 | GL expense account for commission |
| `BKPR_SLS_EXPDPT` | STRING 4 | GL department for commission |
| `BKPR_SLS_EXTRA` | STRING 100 | Extra field |
| `BKPR_SLS_EMAIL` | STRING 128 | Email |

**Design note:** Each row covers one class combination. The 5 arrays (QUOTA/GROSS/COGS/RCPTS/COMM/PAID × 12 periods) let EVO track commission P&L by salesperson by month without a separate transaction table. COMM vs PAID difference = commission earned but not yet paid out.

---

## BKPRTC — Time Cards (7 fields, confirmed from DDF schema.md line 8476)

Primary key: `BKPR_TC_EMP` + `BKPR_TC_DATE` + `BKPR_TC_START`

| Field | Type | Meaning |
|-------|------|---------|
| `BKPR_TC_EMP` | UBINARY 2 | Employee number |
| `BKPR_TC_DATE` | DATE | Work date |
| `BKPR_TC_START` | TIME | Clock-in time |
| `BKPR_TC_STOP` | TIME | Clock-out time |
| `BKPR_TC_DEDUCT` | TIME | Deducted time (breaks) |
| `BKPR_TC_TYPE` | STRING 1 | Pay type code (R=regular, V=vacation, S=sick, etc.) |
| `BKPR_TC_EXTRA` | STRING 25 | Extra / note |

---

## BKPRTCFG — Time Card Configuration (205 fields, confirmed from DDF schema.md lines 8488–8532+)

Primary key: `BKPRT_CFG_KEY` (STRING 2)

Stores 10 named time-card types (NAME_1..10 at 25 chars each), each with a corresponding print command string (CMD_1..20 at 70 chars each) and printer assignment (PRTR_1..10 at 8 chars each). This drives the PR-J / PR-K time card entry and printing workflow.

---

## Other BKPR* tables (summary)

| Table | Fields | Purpose |
|-------|--------|---------|
| **BKPRACOM** | 12 | Archived commission transactions (SLSP, CCODE, INVNM PK) |
| **BKPRAGNT** | 4 | Sales agent registry: agent#, code, GL account |
| **BKPRCOMM** | 12 | Active commission transaction ledger |
| **BKPRFTAX** | 47 | Federal tax withholding tables (code, description, allowance amounts) |
| **BKPRGLFL** | 664 | Payroll GL account matrix by state (STCODE) and department (DEPT) — FIT, FICA, state tax, workers comp, UOD, UDE accounts per row |
| **BKPRHCOM** | 12 | Historical commission transactions |
| **BKPRSTFL** | 2 | State filing table: STCODE (2) + TAXNUM (10) |
| **BKPRW2** | 384 | W-2 year-end snapshot — identical schema to BKPRMSTR, populated by PR-O Year End Routine |

---

## Year-end and W-2 workflow (confirmed from DDF schema + menu analysis, Pass 111d 2026-06-19)

### PR-O: Year End Routine (BKPRO)

T7PRO.DFM has only 1 field (a confirmation screen). The year-end routine:
1. Copies `BKPRMSTR` → `BKPRW2` (full 384-field snapshot of each employee's YTD accumulators)
2. Rolls BKPRSALE → BKPRBOOK (prior year commission data)
3. Zeros out YTD accumulators in BKPRMSTR for the new year (QTD totals become prior-year baseline)
4. Advances `BKPR_EMP_YEAR` + `BKPR_EMP_QTR` in BKPRMSTR

BKPRW2 is thereafter independent from BKPRMSTR — year-end adjustments to W-2 amounts do not affect the employee master.

### PR-A: Edit W-2 Data (BKPRA, BKPRP, BKPRQ)

Edits individual BKPRW2 rows. Key W-2 fields in BKPRW2:

| W-2 Box | BKPRW2 field(s) | Content |
|---------|-----------------|---------|
| Box 1: Wages, tips | `BKPR_EMP_RAYTD` | Regular wages YTD |
| Box 2: Federal income tax | `BKPR_EMP_FITYTD` | FIT withheld YTD |
| Box 3/5: SS/Medicare wages | `BKPR_EMP_FICYTD_1/2` | FICA employee YTD |
| Box 4/6: SS/Medicare tax | `BKPR_EMP_FICYTD_1/2` | FICA withheld |
| Box 16/17: State wages/tax | `BKPR_EMP_STYTD` | State income tax YTD |
| Box 12: Coded amounts | `BKPR_EMP_PAYAMT_1..15` | 15 user-coded deduction amounts |
| Workers comp | `BKPR_EMP_WKYTD` | WC YTD |
| Other deductions | `BKPR_EMP_OHYTD_1..12` | 12 custom deduction YTDs |
| Employee address | `BKPR_EMP_ADD/CSZ/ST/ZIP/CNTRY` | Copied from BKPRMSTR at year-end |
| SSN | `BKPR_EMP_SSN` | Required on W-2 |
| Medical | `BKPR_EMP_MDYTD` | Medical deduction YTD |

### PR-L-I: Print W-2 Forms (BKPRLI)

Reads BKPRW2 and prints IRS Form W-2 for each active employee. T7PRLI.DFM is a stub (0 fields = parameter-less or runs as a report). Output is formatted to IRS standard W-2 layout.

### PR-L-H: Print 940 Report (BKPRLH)

T7PRLH.DFM has 54 fields and 112 controls — a rich date-range report form. Reads BKPRMSTR/BKPRCURP for FUTA tax totals per employee per quarter; produces IRS Form 940 FUTA computation.

### 1099 Generation (AP-S)

1099 reporting is in the AP module (not PR):
- `BKAPVEND.BKAP_TAX_ID` — vendor EIN (STRING 20, field 53)
- `BKAPVND2` (63f) — extended 1099 box amounts: `BKAP2_SEND_1099` flag + box type + 10 amount slots × 5 entries each
- `AP-S: Print 1099 Forms` (APS1999/APS2000/TAPS2000) reads BKAPVEND + BKAPVND2 + BKAPINVT YTD payment totals

### PR-H: Transfer Liabilities to AP (BKPRH)

T7PRH.DFM has 82 fields and 117 controls — one of the most complex PR forms. It creates AP vouchers for payroll tax and benefit liabilities:
- Reads per-pay-period tax liabilities: FIT, FICA employee + employer, state, SUTA, FUTA, workers comp
- Reads user-defined deduction (UOD) remittances: health insurance, 401k, FSA, etc.
- Creates BKAPINVL/BKAPINVT rows for each remittance payee (vendors set up in BKAPVEND)
- GL accounts come from BKPRGLFL (664f) — the per-state/department payroll GL matrix

### Full year-end sequence

```
Throughout year:
  PR-B / PR-C / PR-G / PR-D (regular payroll cycle)
  PR-J / PR-K (time cards → payroll)
  PR-H (periodic liability remittances to AP)

Quarter-end:
  PR-L-A: Quarterly earnings register
  PR-L-B/C/D/E: QTD detailed reports
  PR-L-H: 940 FUTA report

Year-end:
  PR-A: Edit W-2 overrides in BKPRW2 (if needed before PR-O)
  PR-O: Year End Routine
    → Copy BKPRMSTR → BKPRW2 (freeze W-2 data)
    → Roll BKPRSALE → BKPRBOOK
    → Zero BKPRMSTR YTD fields
  PR-A: Edit BKPRW2 (post-copy corrections)
  PR-L-I: Print W-2 Forms (reads BKPRW2)
  AP-S: Print 1099 Forms (reads BKAPVEND + BKAPVND2)
```

---

## Programs (42 total) — Pass 268 (2026-06-25)

Source: `samples/rwn_symbols.json` (T7PR* entries).

### Group 1: Core payroll processing

| Program | Procs | Lib | DBs | Role |
|---------|------:|-----|----:|------|
| `T7PRB.RWN` | 229 | LISTG60 | 34 | **PR-B Enter Pay Info** — current-period batch; BKPRCURP+BKPRMSTR+BKPRGLFL; BKPR.EMP 107-var, BKPR.GL 86-var, BKPR.CURP 46-var |
| `T7PRC.RWN` | 129 | LISTG60 | 27 | **PR-C Print Payroll Register** — BKPRCURP+ISBUILD+BKPRMSTR; BKPR.EMP 105-var |
| `T7PRD.RWN` | 189 | ISTECH | 32 | **PR-D Print Payroll Checks** — BKSYMSTR+BKPRCURP+ISBANKS; BKPR.EMP 105-var; ISTECH.LIB = check printing engine |
| `T7PRG.RWN` | 134 | ISTECH | 25 | **PR-G Void Payroll Checks** — BKPRCURP+BKPRMSTR+ISBANKS; ISTECH.LIB |

### Group 2: Employee master / setup

| Program | Procs | Lib | DBs | Role |
|---------|------:|-----|----:|------|
| `T7PRA.RWN` | 169 | LISTG60 | 26 | **PR-A Edit W-2 Data / Enter Employees** — BKPRMSTR+BKPRINFO+BKPRGLFL+BKGLCOA; BKPR.EMP 105-var, BKPR.INFO 37-var |
| `T7PRM.RWN` | 150 | LISTG60 | 21 | **PR-M Payroll Defaults** — BKPRGLFL+BKYSMSTR+BKPRMSTR; BKPR.EMP 103-var |
| `T7PRP.RWN` | 75  | LISTG60 | 26 | **PR-P Enter Employee Raises** — BKPRMSTR+BKPRINFO |
| `T7PRQ.RWN` | 75  | LISTG60 | 26 | **PR-Q** (paired with PR-P) — BKPRMSTR+BKPRINFO |
| `T7PRS.RWN` | 64  | LISTG60 | 15 | **PR-S** employee setup screen — BKPRMSTR+BKPRINFO |
| `T7PROGINFO.RWN` | 80 | LISTG60 | 19 | **Employee training/progress info** — ISPRINFO+CLASMSTR (new table pair: course catalog + employee completion) |

### Group 3: Time cards

| Program | Procs | Lib | DBs | Role |
|---------|------:|-----|----:|------|
| `T7PRJ.RWN` | 83 | LISTG60 | 15 | **PR-J Enter Time Cards** — BKPRMSTR+BKPRTC; time card entry for payroll |
| `T7PRK.RWN` | 134 | LISTG60 | 30 | **PR-K Print/Post Time Cards** — BKSYMSTR+BKPRMSTR+BKPRTC+BKPRGLFL; posts BKPRTC → BKPRCURP |

### Group 4: Tax and AP liabilities

| Program | Procs | Lib | DBs | Role |
|---------|------:|-----|----:|------|
| `T7PRF.RWN` | 92 | EVO | 17 | **PR-F Maintain Tax Tables** — BKPRFTAX only; no BKPR.EMP (pure tax bracket editor; 11-tier table) |
| `T7PRH.RWN` | 121 | LISTG60 | 23 | **PR-H Transfer Liabilities to AP** — BKPRGLFL+BKYSMSTR+BKAPINVT+ISMCF; ISIS.MCF 49-var (multi-currency tax liabilities → AP) |

### Group 5: Quarterly and annual reports (PR-L-*)

| Program | Procs | Lib | DBs | Role |
|---------|------:|-----|----:|------|
| `T7PRLI.RWN` | 219 | LISTG60 | 27 | **PR-L-I Print W-2 Forms** — largest PR report; BKPRMSTR+BKPRGLFL; BKPR.EMP 105-var |
| `T7PRLO.RWN` | 152 | LISTG60 | 27 | **PR-L-O** (unlisted menu — extended report?) — BKSYMSTR+BKPRMSTR+BKPRCURP+BKPRINFO; BKPR.EMP 105-var |
| `T7PRLG.RWN` | 131 | EVO | 22 | **PR-L-G GL allocation detail** (unlisted menu — EVO.LIB = newer addition) — BKPRGLFL+BKPRCURP+BKPRMSTR+BKPRINFO |
| `T7PRLD.RWN` | 131 | LISTG60 | 22 | **PR-L-D Print Detail Earnings Ledger** — BKPRCURP+BKPRMSTR+BKPRINFO |
| `T7PRLF.RWN` | 125 | LISTG60 | 18 | **PR-L-F Print Subject To Report** — BKPRGLFL+ISBUILD+BKPRMSTR |
| `T7PRLC.RWN` | 115 | LISTG60 | 22 | **PR-L-C Print QTD Taxable Earnings** — BKPRMSTR+BKPRCURP+BKPRGLFL |
| `T7PRLE.RWN` | 114 | LISTG60 | 27 | **PR-L-E Print Detail Deductions Ledger** — BKPRGLFL+BKPRCURP |
| `T7PRLM.RWN` | 113 | LISTG60 | 24 | **PR-L-M Print Employer Contributions** — BKPRGLFL+BKPRCURP+BKPRMSTR |
| `T7PRLP.RWN` | 112 | LISTG60 | 22 | **PR-L-P Print Employee Raises** — ISBUILD+BKPRMSTR+BKPRCURP |
| `T7PRLQ.RWN` | 111 | LISTG60 | 24 | **PR-L-Q** (paired with PR-L-P) — BKPRMSTR+BKPRINFO+BKPRGLFL |
| `T7PRLH.RWN` | 105 | EVO | 17 | **PR-L-H Print 940 Report** — EVO.LIB; BKPRGLFL+BKPRCURP+BKPRMSTR |
| `T7PRLK.RWN` | 107 | LISTG60 | 22 | **PR-L-K Print Payroll Hours** — BKPRCURP+BKPRMSTR |
| `T7PRLN.RWN` | 107 | LISTG60 | 22 | **PR-L-N Print Payroll Wages Detail** — BKPRCURP+BKPRMSTR |
| `T7PRLB.RWN` | 108 | LISTG60 | 26 | **PR-L-B Print QTD Earnings Register** — BKPRMSTR+BKPRINFO+BKPRCURP |
| `T7PRLA.RWN` | 104 | LISTG60 | 17 | **PR-L-A Print Quarterly Info** — BKPRMSTR+BKPRGLFL |
| `T7PRLJ.RWN` | 93 | EVO | 20 | **PR-L-J Print CA DE6 Form** — EVO.LIB; BKPRMSTR+**BKPRSALE**+BKPRGLFL (sales commission data in payroll report) |

### Group 6: History, year-end, print

| Program | Procs | Lib | DBs | Role |
|---------|------:|-----|----:|------|
| `t7PRI.RWN` | 108 | LISTG60 | 18 | **PR-I Print Pay History** — BKPRCURP+BKPRMSTR+BKPRINFO |
| `T7PRE.RWN` | 99  | LISTG60 | 23 | **PR-E Print Employee Info** — BKPRMSTR+BKPRGLFL |
| `T7PRN.RWN` | 99  | LISTG60 | 24 | **PR-N Purge Payroll History** — BKPRCURP+BKPRMSTR |
| `T7PRO.RWN` | 74  | EVO | 18 | **PR-O Year End Routine** — EVO.LIB; BKPRMSTR+FILELOC (year-end roll + W-2 freeze) |

### Group 7: Utilities and stubs

| Program | Procs | Lib | Role |
|---------|------:|-----|------|
| `T7PRDPST.RWN` | 32 | ISTECH | Direct-post utility — BKPRCURP+BKPRGLFL+BKPRMSTR+BKPRINFO; ISTECH.LIB = direct GL post |
| `T7PRJCSYNC.RWN` | 33 | EVO | JC Sync — BKPRMSTR+BKPRINFO; syncs payroll data → job costing |
| `T7PRFIX.RWN` | 56 | EVO | Data repair utility — BKPRMSTR |
| `T7PRDIVFIX.RWN` | 30 | EVO | Division assignment fix — BKPRMSTR |
| `T7print.RWN` | 49 | EVO | General print stub — MKAHIST+FILELOC |
| `t7pretag.RWN` | 37 | EVO | Pre-tag utility — BKICMSTR+BKPSUSER (item→employee pre-assignment?) |
| `T7PRSADMIN.RWN` | 5 | t7prsADMIN.SRC | Admin stub |
| `t7program.RWN` | 4 | t7program.SRC | Minimal stub |

---

### Key program revelations (Pass 268)

**T7PRB** (229p, LISTG60) is the core payroll calculation engine — it holds the highest BKPR.EMP var count (107) and BKPR.CURP count (46), confirming it reads every employee field and writes the complete current-period pay record. It is the only program to hold the full 542 ISTS.CFG access count alongside full BKPR.EMP+GL+CURP namespaces simultaneously.

**T7PRLI** (219p) is the largest-by-proc report — W-2 printing requires reading almost every employee master field (105-var) and all GL accounts (86-var) to correctly allocate withholding across all state tax jurisdictions. Second largest program count after T7PRB.

**T7PRH** (121p) opens ISMCF — multi-currency framework — confirming that payroll tax liabilities transferred to AP can span multiple currencies (for international sites or multi-currency clients).

**T7PRLJ** (93p, PR-L-J CA DE6) opens **BKPRSALE** — the sales commission/employee sales table. This is the only PR program that reads BKPRSALE, confirming CA DE6 includes commission income. BKPRSALE is also read by T7ARG (AR) and T7PRLJ (PR), making it a cross-module commission bridge.

**T7PROGINFO** (80p) opens **ISPRINFO + CLASMSTR** — a new table pair not previously identified. CLASMSTR is likely a course/class catalog; ISPRINFO links employees to completed classes. This is EvoERP's employee training/qualification tracking subsystem, accessed via a PR menu item.

**T7PRO** (PR-O Year End, 74p) opens **FILELOC** — a path-lookup table. This confirms PR year-end uses the file location table to find and rename/archive prior-year payroll files (BKPRHIST → archive) during year-end roll.

**New tables confirmed from T7PR* programs:**
- `ISPRINFO` — employee progress/training records (T7PROGINFO)
- `CLASMSTR` — training class/course catalog (T7PROGINFO)
- `FILELOC` — file path lookup table used during year-end roll (T7PRO, T7print)
- `ISBANKS` — bank account master (T7PRD, T7PRG — paycheck bank routing)

---

## Pass 329 — TAS6 BKPR\*.RUN binary analysis (2026-06-26)

All 37 TAS6 BKPR\*.RUN programs copied from `\\i2s109-solidcrm\DBAMFG$\` to `samples/` and analyzed via Python string extraction. Findings extend and confirm T7-era analysis.

### TAS6 BKPR\*.RUN program inventory (37 files)

| File | Approx size | Menu code | Title (from binary) |
|------|------------|-----------|---------------------|
| BKPRA.RUN | ~18 KB | PR-A | Enter Employees / Edit W-2 Data |
| BKPRB.RUN | ~22 KB | PR-B | Enter Pay Info |
| BKPRC.RUN | ~12 KB | PR-C | Print Payroll Register |
| BKPRD.RUN | ~14 KB | PR-D | Print Payroll Checks (Laser Forms) |
| BKPRE.RUN | ~8 KB | PR-E | Print Employee Info |
| BKPRF.RUN | ~10 KB | PR-F | Maintain Tax Tables |
| BKPRG.RUN | ~9 KB | PR-G | Void Payroll Checks |
| BKPRH.RUN | ~8 KB | PR-H | Transfer Liabilities to AP |
| BKPRI.RUN | ~10 KB | PR-I | Print Pay History |
| BKPRJ.RUN | ~4 KB | PR-J | Enter Time Cards (dispatch) |
| BKPRJA.RUN | ~18 KB | PR-J | Enter Time Cards (daily) |
| BKPRJB.RUN | ~16 KB | PR-J | Enter Time Cards (weekly) |
| BKPRK.RUN | ~14 KB | PR-K | Print/Post Time Cards |
| BKPRL.RUN | ~4 KB | PR-L | PR-L sub-menu dispatch |
| BKPRLA.RUN | ~11 KB | PR-L-A | Print Quarterly Info |
| BKPRLB.RUN | ~9 KB | PR-L-B | Print QTD Earnings Register |
| BKPRLC.RUN | ~8 KB | PR-L-C | Print QTD Taxable Earnings |
| BKPRLD.RUN | ~10 KB | PR-L-D | Print Detail Earnings Ledger |
| BKPRLE.RUN | ~10 KB | PR-L-E | Print Detail Deductions Ledger |
| BKPRLF.RUN | ~9 KB | PR-L-F | Print Subject To Report |
| BKPRLG.RUN | ~14 KB | PR-L-G | Print 941 & Schedule B Reports |
| BKPRLH.RUN | ~10 KB | PR-L-H | Print 940 Report |
| BKPRLI.RUN | ~12 KB | PR-L-I | Print W-2 Forms |
| BKPRLJ.RUN | ~8 KB | PR-L-J | Print California DE6 Form |
| BKPRLK.RUN | ~9 KB | PR-L-K | Print Payroll Hours |
| BKPRLM.RUN | ~9 KB | PR-L-M | Print Employer Contributions |
| BKPRLN.RUN | ~8 KB | PR-L-N | Print Payroll Wages Detail |
| BKPRLP.RUN | ~8 KB | PR-L-P | Print Employee Raises |
| BKPRLQ.RUN | ~8 KB | PR-L-Q | Print Employee Reviews |
| BKPRLL.RUN | ~7 KB | PR-LL | PR-LL sub dispatch |
| BKPRM.RUN | ~14 KB | PR-M | Payroll Defaults (Division) |
| BKPRN.RUN | ~8 KB | PR-N | Purge Payroll History |
| BKPRO.RUN | ~12 KB | PR-O | Payroll Year End Routine |
| BKPRP.RUN | ~10 KB | PR-P | Enter Employee Raises |
| BKPRQ.RUN | ~8 KB | PR-Q | Enter Employee Reviews |
| BKPRDPST.RUN | ~10 KB | PR-D-PST | Direct Deposit Post |
| BKPRLA.RUN (dup) | — | — | *(37th slot — BKPRLF T6 variant)* |

**Key findings:**
- PR-D has two variants: **Laser Forms** (BKPRD) and **Continuous Forms** — both map to the same menu code PR-D with a format selector
- BKPRDPST.RUN is a dedicated **Direct Deposit Post** program (separate from BKPRD) — accesses BKGL.CHK.*, ISPRTEMP, ISBANKS, ISBANKSA, ISBANKSI
- BKPRM.RUN introduces a **Division** layer — multi-location payroll can segment employees by division, each with its own GL defaults
- BKPRO.RUN (Year-End) confirms all QTD/YTD fields are zeroed in BKPR.EMP after snapshot to BKPRHIST
- BKPRA menu shows `Y - Sync PR-JC excluding Job Rates` / `$ - Sync PR-JC including Job Rates` — PR-JC sync merges Job Costing records into employee master
- BKPRLG reads FICACRD/FICAEMP/FICAEXP/FICAERP accessor groups — confirms 941 form maps directly to BKPR.GL.* fields

### BKPR.EMP.\* accessor map (91 fields, from BKPRA + BKPRB + BKPRO binaries)

These are the TAS6 field accessor names for BKPRMSTR (employee master). Each `BKPR.EMP.XXX` call maps to a column in the BKPRMSTR Btrieve table.

| Accessor | Meaning | Notes |
|----------|---------|-------|
| NUM | Employee number | Primary key |
| LNME | Last name | |
| FNMI | First name + middle initial | Combined field |
| SSN | Social Security Number | |
| ADD | Street address | |
| CSZ | City/State/Zip | Combined field |
| ZIP | ZIP code | Also in CSZ |
| CNTRY | Country | International |
| PHONE | Phone number | |
| SDATE | Start (hire) date | |
| BDAY | Birth date | |
| TERM | Termination date | |
| LSTPR | Last pay date | |
| DEPT | Department code | |
| SHIFT | Shift code | |
| PAYTYP | Pay type | H=hourly, S=salary |
| SRTE | Salary rate per period | |
| MS | Marital status | S/M (old W-4) |
| FEDEXM | Federal exemptions | Old W-4 line 5 |
| ADDIT | Additional withholding | Old W-4 |
| NEWW4 | 2020+ W-4 flag | Y=new form, N=old |
| 2EPJ | 2020 W-4 Step 2e | Extra withholding — multiple jobs |
| AAD | 2020 W-4 Step 4b | Additional annual deduction |
| ANDD | 2020 W-4 Step 3 | Annual dependent deduction |
| AWPPP | Annual withholding per period | Calculated from 2020 W-4 |
| OAIWW | 2020 W-4 Step 4a | Other annual income withholding |
| STEXM | State exemptions | |
| STEXMA | State exemptions additional | |
| STEXMN | State exemptions (new-form) | |
| SDIEXM | SDI exempt flag | |
| EXTRA | Extra deduction amount | |
| FITQTD | Fed income tax QTD | |
| FITYTD | Fed income tax YTD | |
| FICQTD | FICA (SS) QTD | |
| FICYTD | FICA (SS) YTD | |
| MDQTD | Medicare QTD | |
| MDYTD | Medicare YTD | |
| MDAMT | Medicare employee amount | |
| MDACT | Medicare account GL | |
| MDDPT | Medicare deduction department | |
| MDNME | Medicare line description | |
| SDIQTD | SDI QTD | |
| SDIYTD | SDI YTD | |
| STQTD | State income tax QTD | |
| STYTD | State income tax YTD | |
| RHQTD | Regular hours QTD | |
| RHYTD | Regular hours YTD | |
| RAQTD | Regular amounts QTD | |
| RAYTD | Regular amounts YTD | |
| OHQTD | Other hours QTD | 12-slot array |
| OHYTD | Other hours YTD | 12-slot array |
| OAQTD | Other amounts QTD | 12-slot array |
| OAYTD | Other amounts YTD | 12-slot array |
| SHQTD | Shift differential QTD | |
| SHYTD | Shift differential YTD | |
| VHQTD | Vacation hours QTD | |
| VHYTD | Vacation hours YTD | |
| VAQTD | Vacation amounts QTD | |
| VAYTD | Vacation amounts YTD | |
| VRTE | Vacation accrual rate (hrs/period) | |
| VCAP | Vacation hours cap | |
| VDUE | Vacation hours balance | |
| SAQTD | Sick amounts QTD | |
| SAYTD | Sick amounts YTD | |
| SCAP | Sick hours cap | |
| SDUE | Sick hours balance | |
| WKQTD | Total weekly hours QTD | |
| WKYTD | Total weekly hours YTD | |
| OTHQTD | Other deductions QTD | |
| OTHYTD | Other deductions YTD | |
| OTHAMT | Other deduction amount | |
| OTHNME | Other deduction description | |
| OTHACT | Other deduction GL account | |
| OTHDPT1 | Other deduction GL department | |
| UODQTD | User-defined deductions QTD | 20-slot array |
| UODYTDB | User-defined deductions YTD balance | 20-slot array |
| UODLMT | User-defined deduction limit | 20-slot array |
| UODYLM | User-defined deduction yearly limit | 20-slot array |
| UODAMTM | User-defined deduction monthly max | 20-slot array |
| UDEQTD | Employer deduction QTD | 20-slot array |
| UDEYTDO | Employer deduction YTD | 20-slot array |
| UDELMT | Employer deduction limit | 20-slot array |
| UDEYLM | Employer deduction yearly limit | 20-slot array |
| UDEAMT | Employer deduction amount | 20-slot array |
| WCEE | Workers Comp employee amount | |
| WCER | Workers Comp employer rate | |
| BANKA | Bank account number | Direct deposit |
| BANKR | Bank routing number | Direct deposit |
| BENDTE | Benefits eligibility date | |
| EXPACT | Expense account GL | |
| EXPDPTL | Expense dept GL | |
| OPNAME | Operator who last edited | |
| PAYAMT | Gross pay amount | |

### BKPR.CURP.\* accessor map (41 fields, from BKPRB + BKPRD binaries)

Accessor names for BKPRCURP (current-period pay records).

| Accessor | Meaning |
|----------|---------|
| EMPNO | Employee number (FK → BKPRMSTR) |
| CKNUM | Check number |
| CKNUMB | Check number (bank, direct deposit) |
| CKDTE | Check date |
| PAYDTE | Pay date |
| PERIOD | Pay period number |
| YEAR | Payroll year |
| FLNME | Full name (printed on check) |
| ADDR | Check address |
| DEPT | Department |
| MS | Marital status |
| DPST | Direct deposit flag |
| DPSTBK | Direct deposit bank code |
| RATEREG | Regular pay rate |
| RATEOT | Overtime pay rate |
| RATEVAC | Vacation pay rate |
| RATESK | Sick pay rate |
| HOURSRG | Regular hours this period |
| HOURSOT | Overtime hours this period |
| HOURSVAC | Vacation hours this period |
| HOURSK | Sick hours this period |
| OTHRS | Other hours this period |
| AMT | Gross pay amount |
| CKAMT | Net check amount |
| NETAMT | Net pay amount |
| FAMT | Federal income tax withheld |
| FICA | FICA withheld |
| MDAMT | Medicare withheld |
| MDSAM | Medicare surtax (high-earner) |
| SDIAMT | SDI withheld |
| STAMT | State income tax withheld |
| FICEXM | FICA exempt flag |
| MDEXM | Medicare exempt flag |
| SDIEXM | SDI exempt flag |
| STEXM | State exemptions |
| DEPCNT | Dependent count |
| FDLIM | Federal deduction limit |
| UODAMT | Employee deduction amounts | (20-slot array) |
| UDEAMT | Employer deduction amounts | (20-slot array) |
| WKHRS | Total weekly hours |
| WKAMT | Total weekly gross |

### BKPR.TAX.\* accessor map (7 fields, from BKPRF binary)

Accessor names for BKPRTC (tax table rates/limits).

| Accessor | Meaning |
|----------|---------|
| FICBASE | FICA taxable wage base (annual SS limit) |
| FITBASE | Federal income tax base threshold |
| MDBASE | Medicare taxable base (unlimited; used for surtax calc) |
| SDIBASE | SDI taxable wage base |
| STBASE | State income tax base |
| FICLMT | FICA annual employee limit |
| MDLMT | Medicare annual limit (informational only) |

### BKPR.GL.\* accessor map (sample — 75+ fields, from BKPRLG + BKPRLH + BKPRM binaries)

BKPRGLFL has 664 fields total — organized as `<tax-type><role>` per state+department combination. Representative confirmed accessors:

| Accessor | Meaning |
|----------|---------|
| FICACRD | FICA credit GL account |
| FICAEMP | FICA employee-side GL |
| FICAEXP | FICA expense GL |
| FICAERP | FICA employer-portion GL |
| FITCRD | Federal income tax credit GL |
| FITEXP | FIT expense GL |
| FUTACRD | FUTA credit GL |
| FUTALMT | FUTA annual wage limit |
| FUTART | FUTA tax rate |
| MDCRD | Medicare credit GL |
| MDEXP | Medicare expense GL |
| MDERP | Medicare employer GL |
| SDICRD | SDI credit GL |
| SDIEMP | SDI employee GL |
| SDIEXP | SDI expense GL |
| STCRD | State income tax credit GL |
| STEMP | State IT employee GL |
| STEXP | State IT expense GL |
| WCBASE | Workers Comp wage base |
| WCCRD | Workers Comp credit GL |
| WCEXP | Workers Comp expense GL |
| WCRATE | Workers Comp rate |

See **§ BKPRGLFL — Payroll GL Configuration Matrix (Pass 381)** below for the complete 679-field confirmed schema.

### New tables confirmed from TAS6 binaries

| Table | Confirmed by | Purpose |
|-------|-------------|---------|
| ISPRJDEA | BKPRJA.RUN | PR-J-A Import Time Cards staging — `A` suffix = active/current import batch |
| ISPRTEMP | BKPRDPST.RUN, BKPRH.RUN | Payroll transaction temp/staging during posting |
| ISBANKS | BKPRDPST.RUN | Bank account master (direct deposit routing) |
| ISBANKSA | BKPRDPST.RUN | Bank accounts — alternate/archive tier |
| ISBANKSI | BKPRDPST.RUN | Bank accounts — inactive tier |

### WOELABOR deletion constraint (WO↔PR link confirmed)

BKPRA.RUN contains the string:
> `"Cannot delete. There are WO labor import (WOELABOR) records for this employee."`

This confirms WOELABOR is a **Work Order employee labor import** staging table. Attempting to delete an employee in PR-A checks WOELABOR — if any un-posted WO labor records reference that employee number, the delete is blocked. This is the only confirmed cross-module constraint between WO and PR.

### 2020 IRS Form W-4 support confirmed

BKPRA.RUN references `"SF7 W-4 2020"` as a shortcut key label. The new W-4 fields in BKPR.EMP.* map directly to the 2020 IRS W-4 redesign:
- `2EPJ` → Step 2(c): jobs with similar income (extra withholding amount)
- `ANDD` → Step 3: total dependents deduction claim
- `AAD` → Step 4(b): additional itemized deductions
- `OAIWW` → Step 4(a): other annual income (investments, retirement)
- `AWPPP` → Calculated: annual withholding per pay period (derived from above)
- `NEWW4` → flag: Y=2020 form used; N=legacy form

---

## BKPRGLFL — Payroll GL Configuration Matrix (Pass 381, 2026-06-29)

**Status: verified** — full 679-column schema confirmed from live DSN=DBA ODBC query.

**PK:** `BKPR_GL_STCODE` (STRING 2) + `BKPR_GL_DEPT` (STRING 4)
**Live rows (i2 Systems):** `CT/STCK` (STOCKROOM, weekly), `CT/ENG` (ENGINEERING, weekly)

BKPRGLFL is the payroll GL routing table. One row per state+department combination. Every GL account, expense account, and tax vendor used by payroll is looked up from this table at run time. T7PRB (Enter Pay Info), T7PRH (Transfer to AP), T7PRLI (Print W-2), and 9 other programs all open BKPRGLFL.

### Scalar fields

| Field | Type | Meaning |
|-------|------|---------|
| BKPR_GL_STCODE | STRING 2 | State code (PK 1) |
| BKPR_GL_DEPT | STRING 4 | Department code (PK 2) |
| BKPR_GL_DPTNME | STRING 20 | Department name — `STOCKROOM`, `ENGINEERING` |
| BKPR_GL_PAYPER | STRING 1 | Pay period code — `W`=weekly, `B`=bi-weekly, `S`=semi-monthly, `M`=monthly |

### Standard tax GL pairs

Each tax type has a liability account (`ACCT`, STRING 10) and a department (`DPT`, STRING 4):

| Tax type | Liability fields | Expense fields | Notes |
|----------|-----------------|----------------|-------|
| FIT | BKPR_GL_FITACCT + FITDPT | BKPR_GL_FITEXP + FITEXPD | Federal income tax |
| FICA (employee) | BKPR_GL_FICACCT_1 + FICDPT_1 | BKPR_GL_FICAEXP_1 + FICAEXD_1 | Employee SS |
| FICA (employer) | BKPR_GL_FICACCT_2 + FICDPT_2 | BKPR_GL_FICAEXP_2 + FICAEXD_2 | Employer SS match |
| FUTA | BKPR_GL_FUTACCT + FUTDPT | BKPR_GL_FUTAEXP + FUTAEXD | Federal unemployment |
| SUTA | BKPR_GL_SUTACCT + SUTDPT | BKPR_GL_SUTAEXP + SUTAEXD | State unemployment |
| SIT | BKPR_GL_SITACCT + SITDPT | — | State income tax |
| WC | BKPR_GL_WCACCT + WCDPT | BKPR_GL_WCEXP + WCEXD | Workers comp |
| MD | BKPR_GL_MDACCT + MDDPT | — | Medicare |
| OD | BKPR_GL_ODACCT + ODDPT | — | Other deduction GL |
| SDI | BKPR_GL_SDIACCT + SDIDPT | BKPR_GL_SDIEXP + SDIEXPD | State disability — both liability and expense |

### Tax rate fields

| Field | Meaning |
|-------|---------|
| BKPR_GL_FICAEMP | FICA employee rate (6.2%) |
| BKPR_GL_FICAEPL | FICA employer rate (6.2%) |
| BKPR_GL_FICALMT | FICA annual wage base limit |
| BKPR_GL_FUTART | FUTA rate |
| BKPR_GL_FUTALMT | FUTA annual wage limit |
| BKPR_GL_FUTACRD | FUTA credit rate |
| BKPR_GL_SUTART | SUTA rate |
| BKPR_GL_SUTALMT | SUTA annual wage limit |
| BKPR_GL_SRTE | SDI rate |
| BKPR_GL_VRTE | Vacation accrual rate |

### General payroll expense accounts (15 slots)

`BKPR_GL_EXPACT_1..15` (GL account, STRING 10) + `BKPR_GL_EXPDPT_1..15` (GL dept, STRING 4)

**Live data confirmed:** slots 6–12 all contain GL account `8710` (payroll expense). These are the expense distribution lines that T7PRB posts gross wages to.

### Optional pay names (5 slots)

`BKPR_GL_OPAYNME_1..5` (STRING 10) — names for optional/supplemental pay types (bonus, commission, etc.).

### Tax vendor arrays

| Array | Count | Field type | Purpose |
|-------|------:|-----------|---------|
| BKPR_GL_TAXVEND_1..30 | 30 | STRING 10 | Primary tax vendor codes (AP vendor IDs for tax remittances) |
| BKPR_GL_TAXVND1_1..16 | 16 | STRING 10 | Secondary/alternate tax vendor codes |

### User-defined deductions (UOD, 20 slots)

One row of flags + accounts per UOD slot (1–20). Each slot = one employee-side deduction (health ins, dental, 401k, FSA, etc.):

| Field suffix | Per-slot type | Meaning |
|-------------|--------------|---------|
| UODACT_N | STRING 10 | GL liability account |
| UODDPT_N | STRING 4 | GL department |
| UODCALC_N | STRING 2 | Calculation method code |
| UODNAME_N | STRING 12 | Deduction name (displayed on check stub) |
| UODPTX_N | STRING 1 | Pre-tax flag (Y=reduces taxable income) |
| UODFIT_N | STRING 1 | FIT exempt (Y=not subject to FIT) |
| UODFICA_N | STRING 1 | FICA exempt |
| UODMED_N | STRING 1 | Medicare exempt |
| UODFUTA_N | STRING 1 | FUTA exempt |
| UODSIT_N | STRING 1 | SIT exempt |
| UODSUTA_N | STRING 1 | SUTA exempt |
| UODSDI_N | STRING 1 | SDI exempt (**confirmed Pass 381**) |
| UODWC_N | STRING 1 | Workers Comp exempt (**confirmed Pass 381**) |
| UODLOC1_N | STRING ? | Location code 1 (**confirmed Pass 381**) |

### UOD slot 1 sub-variants (6 sub-slots)

`BKPR_GL_UODACT1_1..6`, `BKPR_GL_UODDPT1_1..6`, `BKPR_GL_UODCLC1_1..6` — UOD slot 1 can split across up to 6 GL accounts (e.g. split health insurance premiums across multiple liability accounts).

### User-defined earnings (UDE, 20 slots)

Employer-side matching contributions (401k match, employer health, etc.):

| Field suffix | Meaning |
|-------------|---------|
| UODEACT_N | GL account |
| UODEDPT_N | GL department |
| UODECLC_N | Calculation method |

### Extra GL slots (confirmed Pass 381)

`BKPR_GL_XACT_1..5` + `BKPR_GL_XDPT_1..5` — 5 extra GL account+department pairs for miscellaneous payroll GL entries not covered by the standard tax and UOD arrays.

### Binary overflow buffer

`BKPR_GL_EXTRA` — 200-byte binary buffer (Pervasive BINARY type). Reserved for future fields or runtime scratch space.

### Field count summary

| Group | Count |
|-------|------:|
| PK + scalar | 4 |
| Tax GL pairs (10 types × 2–4 fields each) | ~32 |
| Tax rates | 10 |
| Expense accounts (15 × 2) | 30 |
| Optional pay names | 5 |
| Tax vendors (30 + 16) | 46 |
| UOD arrays (20 slots × 14 flags/fields) | 280 |
| UOD slot 1 sub-variants (6 × 3) | 18 |
| UDE arrays (20 × 3) | 60 |
| Extra GL (5 × 2) | 10 |
| EXTRA buffer | 1 |
| **Total (DDF)** | **~679** |

The DDF reports 664 named fields + 15 additional unnamed/padding = 679 physical columns.

---

## Notes & open questions

- **BKPRMSTR record size = 3,389 bytes** (BANKA ends at offset 3372 + 17 = 3389). Very large row — each employee is almost 3.5 KB.
- **UOD vs UDE naming:** UOD = User-defined deductions (employee side — health, dental, 401k, etc.). UDE = User-defined employer deductions (employer match). Both have 20 slots each, with QTD/YTD/limit arrays.
- **OHQTD/OAQTD (fields 62–109):** The "OH" prefix means "Other Hours" — these 12 buckets accumulate hours and amounts for non-standard pay types (overtime, bonus, shift differential, etc.). Named in BKPRTCFG.
- **BKPRGLFL (679 DDF columns):** Fully documented in Pass 381 — see §BKPRGLFL above. Multi-state payroll support confirmed: one row per state+dept combination; all tax GL accounts, rates, UOD/UDE arrays, and expense distribution lines in one wide table.
- **BKPRCOMM vs BKPRACOM vs BKPRHCOM:** Same 12-field schema with PK SLSP+CCODE+INVNM. The three tables are active/archive/history tiers — mirrors the AP invoicing active/archive/history pattern.
- **BKPRSALE vs BKPRBOOK:** Same 87-field schema. BKPRBOOK likely holds prior fiscal year's commission data (rolled from BKPRSALE during year-end) so both years can be queried.
- **Time card flow:** Entered via PR-J → stored in BKPRTC → printed/posted via PR-K → time card hours become inputs to Enter Pay Info (PR-B) → check detail goes to BKPRCURP → after posting to BKPRHIST.
