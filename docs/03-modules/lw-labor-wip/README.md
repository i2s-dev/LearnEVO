# Labor / WIP / Job Cost (LW)

Status: verified (menu codes confirmed; chain traced from DC/PR/WO table structure and DFM inventory).

- **Module code**: `LW`
- **Tables**: 0 dedicated — LW uses the same Btrieve tables as WO (WORKORD, WOLABOR, WOMAT, WORECV, WOBOM, WOROUT, WOEXCHG, etc.)
- **UI forms**: LW programs reference T7WO* and BKWO* programs — LW is a menu alias for a curated subset of WO + JC operations

LW (Labor/WIP) provides shop-floor and job-cost access without exposing the full WO engineering setup menus. It shares all its database tables with the WO module.

**Relationship to JC module**: LW-J-* operations share programs with the standalone JC (Job Costing)
module. Several BKJC*.RUN programs serve both LW-J-* and JC-* menu paths. The JC module has 20
reporting operations (JC-A through JC-T); see [docs/03-modules/jc-job-costing/README.md](../jc-job-costing/README.md).

## Menu operations

| Code | Operation | Programs |
| ---- | --------- | -------- |
| `LW-A` | Enter Work Orders | BKAWA;BKDCI;BKWOA |
| `LW-B` | Change WO Status | BKAWB;BKWOB |
| `LW-D` | Print Pick Lists | BKAWD;BKWOD |
| `LW-E` | Issue Material | BKAWG;BKDEJHA;BKWOG;ISWOG |
| `LW-F` | Enter Extra Costs | BKAWH;BKLWF;BKWOH |
| `LW-G` | Enter Finished Production | BKAWI;BKDEJIA;BKWOIP;NZWOI;SRWOI |
| `LW-H` | Close/Cancel Work Orders | BKAWJ |
| `LW-I-A` | Enter Work Order BOM | BKAWKB |
| `LW-I-B` | Create Multi-Date Work Orders | BKAWKC;BKWOKC |
| `LW-I-C` | Create Multi-Assembly Work Orders | BKAWKD;BKWOKD |
| `LW-I-D` | Swap Substitute Parts | BKAWKE;BKWOKE |
| `LW-J-B` | Print Work Order Schedule | BKAWLB | = JC none (LW-only) |
| `LW-J-C` | Print Material/Labor Issues | BKJCE;ISJCE | = JC-E |
| `LW-J-D` | Print Outside Purchases | BKJCF | = JC-F |
| `LW-J-E` | Print Job Cost Summary | BKLWJE | = JC none (LW-only, BKLWJE.RUN) |
| `LW-J-F` | Print Job Cost Report | BKJCA | = JC-A |
| `LW-J-G` | Print Work Order Shortages | BKAWLF;BKWOLF | = JC none (LW-only) |
| `LW-J-H` | Print WIP Summary | BKJCM;BKJCR | = JC-M (BKJCM) + JC-R (BKJCR) |
| `LW-J-I` | Print WO Receipts | BKJCQ | = JC-Q |

LW-J-* operations = Job Cost reports. LW-A/B/D/E/F/G/H/I-* = duplicates of WO-A/B/D/E/F/G/H/I-* with simplified access paths.

---

## WO status codes — confirmed from JC binary analysis (Pass 318)

`BKJCE.RUN` (TAS Pro 6, Pre-2020) contains the WO status filter string `SFRCXI`, confirming
all 6 WO status codes are TAS6-era (not T7-only additions):

| Code | Meaning |
|------|---------|
| `S` | Scheduled |
| `F` | Released (Firm) |
| `R` | Received / Completed |
| `C` | Closed |
| `X` | Cancelled |
| `I` | In Process |

The 4 codes S/F/R/C were confirmed from BKAWLB.SRC (Pass 278). The codes X=Cancelled and
I=In Process are now confirmed from BKJCE.RUN and BKJCQ.RUN TAS6 binaries (Pass 318).

---

## LM-E supersession

`BKLME.RUN` (LM-E Consolidate Inventory Transactions) was the legacy program for
consolidating INVTXN records. In current EvoERP, it is **superseded by `SM-J-D`**
(`t7smjd.rwn`) confirmed in BKMENUSU.TXT. LM-E still exists in the file system but
is no longer a menu entry.

No dedicated T7LW\* or T7LA\* runtime programs exist — the LW module uses T7WO\* programs
directly for operations LW-A through LW-I, and BKJC\*/BKLW\* TAS6 programs for LW-J-\* reports.

---

## Time entry → Work Order charge chain (confirmed from table structure + menu analysis, Pass 111d 2026-06-19)

Labor charges reach a Work Order via three distinct entry paths. All three paths ultimately write to the same destination tables: **WOLABOR** + **WORKORD** cost accumulators.

### Path 1: Shop Floor DC (primary path)

```
Employee scans at DC terminal (barcode / keyboard)
  → BKDCCLAB row created (LAB_DATE+EMP+WOPRE+WOSUF+OPER, LAB_POSTED=N)
  
DC-G: Edit Labor Transactions
  → Supervisor reviews / corrects BKDCCLAB
  → LAB_APPROVAL = Y when approved

DC-H: Post Labor (AUTODCH for batch)
  → Read approved BKDCCLAB rows
  → Compute net LAB_RUNHRS (LAB_FINISH - LAB_START - shift break deductions from BKDCSHFT)
  → Write WOLABOR row:
      MTWOLA_WOPRE/WOSUF + OPER + DATE + EMP + TRXN (PK)
      MTWOLA_RUNHRS / SETUPHRS (hours this session)
      MTWOLA_LABRATE / LABCOST / SETCOST (labor cost = hours × rate from BKPRMSTR)
      MTWOLA_MACHCOST / FOHCOST / VOHCOST / WCOST (machine + overhead from WORKCTR)
      MTWOLA_PARTS / SCRAPPED
  → Update WORKORD:
      WOPROC_RUNHRS / SETUPHRS += hours
      WOPROC_PARTSMAD += parts
      WORKORD actual cost buckets (BKWO_WKORD_ALABCST / ASETCST / AMACHCST / AVOHCST / AFOHCST) += amounts
  → Post BKGLTRAN: DR WIP (from WORKCTR GL account), CR Labor Expense (from BKPRGLFL)
  → Move BKDCCLAB → BKDCLAB (LAB_POSTED=Y)
  → Archive BKDCLAB → BKDCPLAB → BKDCHLAB
```

### Path 2: WO-G Direct Labor Entry

```
User at WO-G menu (T7WOG / BKWOG):
  → Enter employee#, WO#, operation, date, start/stop times or hours
  → Write WOLABOR row directly (same 58-field schema)
  → Update WORKORD cost accumulators (same as Path 1)
  → Post BKGLTRAN (labor GL)
  → No BKDCLAB involvement
```

This path is used when DC scanning is not deployed or for supervisory labor corrections.

### Path 3: PR-J Time Cards → Payroll only (no WO charge)

```
PR-J: Enter Time Cards (T7PRJ / BKPRJ)
  → Write BKPRTC row (EMP+DATE+START+STOP+DEDUCT+TYPE)
  → BKPRTC = payroll time record ONLY — no WOLABOR written

PR-K: Print/Post Time Cards
  → Read BKPRTC rows
  → Compute gross hours → write to BKPRCURP (per-check payroll detail)
  → Updates BKPRMSTR YTD accumulators (RHYTD, VHYTD, SHYTD)
  → Does NOT write WOLABOR or update WORKORD

PR-J-A: Import Time Cards (ISPRJDE)
  → Reads DC labor data (BKDCLAB rows already posted by DC-H)
  → Converts BKDCLAB LAB_RUNHRS → BKPRTC entries
  → So DC-posted labor creates BOTH WOLABOR (WO charge) AND BKPRTC (paycheck)
```

### Path integration summary

```
Shop floor time event
  │
  ├─→ DC path → BKDCCLAB → DC-H → WOLABOR + WORKORD (WO cost)
  │                               └─→ BKGLTRAN (GL: WIP debit)
  │
  └─→ PR-J-A import ← BKDCLAB ──┘ (same DC data, different consumer)
       │
       └─→ BKPRTC → PR-K → BKPRCURP → BKPRMSTR YTD (paycheck)
                            └─→ BKGLTRAN (GL: labor expense debit)
```

**Key design point:** DC-H and PR-K handle the same time data independently:
- DC-H charges the WO (shop floor cost accounting)
- PR-K generates the employee's paycheck (payroll)
- Both post separate GL entries — WIP and Labor Expense respectively

---

## WOLABOR — Work Order Labor Actuals (58 fields, confirmed from DDF schema.md, RE subsystem Pass)

Primary key: `MTWOLA_POSTED` + `MTWOLA_DATE` + `MTWOLA_EMP` + `MTWOLA_WOPRE` + `MTWOLA_WOSUF` + `MTWOLA_OPER` + `MTWOLA_TRXN`

| Field group | Fields | Content |
|---|---|---|
| Keys | POSTED, DATE, EMP, WOPRE, WOSUF, OPER, TRXN | Identity + PK |
| Hours | RUNHRS, SETUPHRS | Actual run and setup hours this entry |
| Rates | LABRATE (hourly rate), MACHRATE | Rates at time of entry |
| Costs | LABCOST, SETCOST, MACHCOST, FOHCOST, VOHCOST, WCOST | Dollar charges to WO |
| Production | PARTS, SCRAPPED | Good parts and scrap this entry |
| Equipment | WC, TOOL, MACH | Work center, tool, machine codes |
| Time | START, STOP, DEDUCT | Raw times (if from DC) |
| Cycle time | CYCLE_HR/MIN/SEC, CYCLE_PARTS | Cycle time study data |
| Audit | 5 flags + 3 alpha UDF | User-defined |
| Notes | CYCLE_NOTE (255 chars) | Cycle time note |

---

## Related tables

| Table | Module | Relationship |
|-------|--------|-------------|
| `WORKORD` | WO | WO header — cost accumulators updated by DC-H/WO-G |
| `WOROUT` | WO | WO routing operations — hours/status updated by DC-H |
| `BKDCLAB` | DC | Source for Path 1 — DC posted labor |
| `BKPRTC` | PR | Source for Path 3 — PR time cards |
| `BKPRMSTR` | PR | Employee master — labor rate used by DC-H/WO-G |
| `WORKCTR` | WO | Work center master — machine rate, overhead rates |
| `BKGLTRAN` | GL | Both DC-H and PR-K write GL entries |
| `WOEXCHG` | WO/LW | WO extra charges (LW-F) — same destination as WOLABOR for misc costs |
