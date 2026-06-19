# Payroll (PR)

Status: verified (auto-generated from the extracted schema, menu-code dump, and DFM inventory).

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

## Notes & open questions

- **BKPRMSTR record size = 3,389 bytes** (BANKA ends at offset 3372 + 17 = 3389). Very large row — each employee is almost 3.5 KB.
- **UOD vs UDE naming:** UOD = User-defined deductions (employee side — health, dental, 401k, etc.). UDE = User-defined employer deductions (employer match). Both have 20 slots each, with QTD/YTD/limit arrays.
- **OHQTD/OAQTD (fields 62–109):** The "OH" prefix means "Other Hours" — these 12 buckets accumulate hours and amounts for non-standard pay types (overtime, bonus, shift differential, etc.). Named in BKPRTCFG.
- **BKPRGLFL (664 fields):** This is a very wide table. With 664 fields organized by state+dept, it stores all GL accounts for every tax type for every combination. Complexity suggests multi-state payroll support.
- **BKPRCOMM vs BKPRACOM vs BKPRHCOM:** Same 12-field schema with PK SLSP+CCODE+INVNM. The three tables are active/archive/history tiers — mirrors the AP invoicing active/archive/history pattern.
- **BKPRSALE vs BKPRBOOK:** Same 87-field schema. BKPRBOOK likely holds prior fiscal year's commission data (rolled from BKPRSALE during year-end) so both years can be queried.
- **Time card flow:** Entered via PR-J → stored in BKPRTC → printed/posted via PR-K → time card hours become inputs to Enter Pay Info (PR-B) → check detail goes to BKPRCURP → after posting to BKPRHIST.
