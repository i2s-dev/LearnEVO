# YS — Yes/No System Parameters (T7YSYN.RWN)

Status: verified | Pass 230 2026-06-23 | Reconfirmed Pass 248 2026-06-24

Source: variable extraction from `samples/rwn_decrypted/T7YSYN.RWN.dec`
Reconfirm: `samples/src/T7YSYN.RWN` decrypts cleanly with K_B (Pass 248): source=EVO.LIB, marker=TWINB,
52 procs (mostly unnamed due to LISTG60 proc-table pattern), 1,243 vars, 14 DB files (BKYSMSTR+13 shared helpers).

---

## Overview

`T7YSYN.RWN` is the **YS module program** — the Yes/No System Parameters editor that allows
administrators to set system-wide operational flags stored in `BKYSMSTR.B`.

- **Module code:** YS
- **Program:** T7YSYN.RWN (EVO.LIB source)
- **Variables:** 1,243 | **Instructions:** 2,131 | **Procs:** 52
- **Primary table:** BKYSMSTR (355 fields)
- **What it does:** Presents a form where each YES/NO system parameter can be set.
  Each `ISTS.CFG.*` variable in this program corresponds to one BKYSMSTR record (or field).

---

## BKYSMSTR Field Namespace (BKYS.*)

These 12 variables directly mirror the BKYSMSTR Btrieve record layout — each is a
field in the one-row system parameters table:

| Variable | BKYSMSTR field | Meaning |
|----------|---------------|---------|
| `BKYS.WONUM` | `BKYS_WONUM` | Work Order auto-number (next WO#) |
| `BKYS.YN` | `BKYS_YN_1` | Primary Y/N flag field |
| `BKYS.GLNUM` | `BKYS_GLNUM` | GL account number |
| `BKYS.GLDPT` | `BKYS_GLDPT` | GL department |
| `BKYS.NUM` | `BKYS_NUM` | Numeric value |
| `BKYS.DESC` | `BKYS_DESC` | Description text |
| `BKYS.VNUM` | `BKYS_VNUM` | Vendor number |
| `BKYS.DATE` | `BKYS_DATE` | Date value |
| `BKYS.QCNUM` | `BKYS_QCNUM` | QC number |
| `BKYS.REQNUM` | `BKYS_REQNUM` | Requisition number |
| `BKYS.INVNUM` | `BKYS_INVNUM` | Invoice number |
| `BKYS.RBNUM` | `BKYS_RBNUM` | (purpose TBD — RB = ReportBuilder?) |

---

## ISTS.CFG.* System Parameters (495 parameters)

These 495 variables are the complete set of editable EvoERP system parameters. Each
`ISTS.CFG.<CODE>` corresponds to a system parameter code that is stored in BKYSMSTR
and loaded into memory during boot by `T7MDefaults.RWN`.

### Key Parameters by Category

**Security & Access Control**

| Code | Meaning |
|------|---------|
| `PASSWD` | Require password on login (Y/N) |
| `CFGLVL` | Configuration access level required |
| `AUTOSL` | Auto security level assignment |
| `SOPSWD` | Require password for SO approval |
| `WOPSWD` | Require password for WO operations |
| `ARPSWD` | Require password for AR operations |
| `CRPSWD` | Require password for credit limit override |
| `CROPEN` | Credit hold open-order policy |

**AR / AP Auto-Numbering**

| Code | Meaning |
|------|---------|
| `ANARA` | AR auto-numbering enabled |
| `ANAPA` | AP auto-numbering enabled |
| `SOANO$` | SO auto-number prefix character |
| `POANO$` | PO auto-number prefix character |

**Sales Order (SO) Behavior**

| Code | Meaning |
|------|---------|
| `PRTSOA` | Print SO acknowledgment on save |
| `SOCHG` | Allow SO price changes |
| `SODEL` | Allow SO line deletion |
| `SODATE` | SO date restriction |
| `SOOPEN` | SO open order policy |
| `SOBLNS` | SO blank lines behavior |
| `SOCLNS` | SO cancelled lines behavior |
| `SOFLNS` | SO filled lines behavior |
| `SOSPEC` | SO special order handling |
| `SOCUST` | SO customer restriction |
| `SOONLY` | SO-only mode |
| `SOAUD` | SO audit trail |
| `SOAUPC` | SO audit price changes |
| `SODAYS` | SO aging days |
| `SODWO` | SO→WO auto-creation |
| `SOADSC` | SO auto-description fill |
| `SOCOPY` | SO copy option |
| `SOITM` | SO item handling flag |

**Work Order (WO) Behavior**

| Code | Meaning |
|------|---------|
| `WOGKIT` | WO kit-build option |
| `WOCHDR` | WO header behavior |
| `WOCALC` | WO cost calculation method |
| `WODSO` | WO→SO auto-link |
| `WOADSC` | WO auto-description |
| `WOONLY` | WO-only mode |
| `WOOPEN` | WO open policy |
| `WOOVER` | WO over-issue allowed |
| `WOAWN` | WO allow negative quantity |
| `WOGNEG` | WO go-negative policy |
| `WOFAMI` | WO family code |
| `WOISER` | WO issue serial tracking |
| `WOSSER` | WO ship serial tracking |
| `WOFHOL` | WO scheduling: skip holidays |
| `WOFDEC` | WO scheduling: skip decimal days |

**Purchase Order (PO) Behavior**

| Code | Meaning |
|------|---------|
| `POCHK` | PO check on receipt |
| `POCHG` | PO price change allowed |
| `POREV` | PO revision tracking |
| `POADSC` | PO auto-description |
| `POONLY` | PO-only mode |

**Inventory (IN)**

| Code | Meaning |
|------|---------|
| `PKINV` | Pick list for inventory |
| `STDPK` | Standard pack quantity |
| `STDCST` | Standard cost method |
| `UPLCST` | Upload cost on receipt |
| `WHCTRL` | Warehouse control enabled |
| `LOTWO` | Lot tracking via WO |
| `SOLOT` | SO lot tracking |
| `SOSER` | SO serial tracking |
| `INAMRP` | Inventory MRP enabled |

**Accounting / GL**

| Code | Meaning |
|------|---------|
| `CHKBAL` | Check GL balance on post |
| `INCGL` | Include GL in period close |
| `GLDATE` | GL date control |
| `GLCTRL` | GL posting control |
| `GLBSDT` | GL beginning-of-year start date |
| `APBSDT` | AP beginning-of-period start date |
| `ARCSDT` | AR closing start date |
| `COGSDP` | COGS posting department |

**Email / Communication**

| Code | Meaning |
|------|---------|
| `EMAIL` | Email system enabled |
| `EMAILS` | Email: SMTP settings active |
| `EMAILP` | Email: PDF attachment enabled |
| `EPASS` | Email: use encrypted password |
| `BCCBOX` | BCC email field shown |
| `MKFROM` | Make-from address |

**MRP / Planning**

| Code | Meaning |
|------|---------|
| `MRPDAY` | MRP planning horizon (days) |
| `MRPDOL` | MRP dollar threshold |
| `FOREC` | Forecast enabled |
| `EPOQTY` | Explode PO quantity |
| `LEADHR` | Lead-time in hours |

**Data Collection (DC)**

| Code | Meaning |
|------|---------|
| `DCARUN` | DC auto-run |
| `DCSYNC` | DC sync interval |
| `DCDAYS` | DC history days |
| `DCTIME` | DC time tracking |
| `DCMACH` | DC machine tracking |
| `DCIRWK` | DC in-rework tracking |

**AvaTax (Sales Tax)**

| Code | Meaning |
|------|---------|
| `AVATAX` | AvaTax integration enabled |
| `AVAACT` | AvaTax account ID |
| `AVAKEY` | AvaTax license key |
| `AVACOD` | AvaTax company code |
| `AVACO` | AvaTax country code |

**Other Notable Parameters**

| Code | Meaning |
|------|---------|
| `ISTS` | ISTS (i2 Systems) features enabled |
| `ECO` | Engineering Change Order enabled |
| `JOB` | Job cost tracking |
| `ITP` | IT support level |
| `SUBCOS` | Sub-contractor cost tracking |
| `EVONTS` | EvoERP notes system |
| `EVOLNK` | Evo Links (web links) enabled |
| `EVOMAX` | EvoERP maximum company count |
| `EVOMTS` (EVOALT) | Evo alerts enabled |
| `VOIC/VOWO/VOPO/VOSO/VOAR/VOAP` | Voice/audio for IC/WO/PO/SO/AR/AP |
| `MAXDC` | Maximum DC terminals |
| `PRSSNX` | Print SSN on reports (N for privacy) |
| `OANDA` | OANDA currency exchange feed |
| `FXKEY` | Foreign exchange API key |

---

## Architecture Notes

- **BKYSMSTR is a single-record table** (355 fields) — all system parameters in one row.
  The `BKYS.*` variables load individual fields from that record.
- **ISTS.CFG.* namespace** is the in-memory representation of BKYSMSTR parameter records.
  At boot, `T7MDefaults.RWN` reads BKYSMSTR into the ISTS.CFG.* global variables so every
  program can test them without reopening BKYSMSTR.
- **495 ISTS.CFG.* vars in T7YSYN** represents all system parameters editable through the
  YS admin screen. The actual in-memory global count at runtime is similar (BKYSMSTR has
  355 declared fields but more are accessed via ISTS.CFG namespace).
- Library var block (var[60]+): standard ISTS.PATH, ISTS.EDATE, tax handles, ISTS.CFG.*
  populated by EVO.LIB on include.

---

## Related Tables

| Table | Fields | Purpose |
|-------|--------|---------|
| `BKYSMSTR` | 355 | System parameters — one row per EVO install |
| `BKSYMSTR` | 286 | System master (company info, sequence numbers) |

**Confidence: 82/100** — Variable names and categories extracted from binary and confirmed
consistent with BKYSMSTR schema. Parameter meanings are inferred from abbreviation + ERP
context; the BKYSMSTR DDF has 355 declared fields matching the observed BKYS.* var layout.
Full functional meanings require source code or runtime observation to confirm edge cases.
