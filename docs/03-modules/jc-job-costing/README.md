# Job Costing (JC)

Status: verified | All 19 BKJC*.RUN programs binary-analyzed — Pass 319 2026-06-26.

Sources: BKMENUSU.TXT program list, all 19 BKJC*.RUN + BKLWJE.RUN binary string extraction,
rwn_symbols.json (T7JC* stubs), DDF schema, EvoHELP.CHM (20 topics in help-content.md).

- **Module code**: `JC`
- **Menu group**: "Job Costing" (Mfg group)
- **Tables**: 0 dedicated — JC reads WO tables (WORKORD, WOROUT, WOBOM, WOMAT, WOLABOR,
  WORECV, WOEXCHG, OUTPROC, SCRAP) and supporting masters (BKICMSTR, BKARCUST, MTICMSTR,
  CLASMSTR, BKPRMSTR, WORKCTR, MACHINE, TOOL, ROUTING, BKAPPO, etc.)
- **UI forms**: 14 (T7JC* DFM files)
- **Programs**: 19 BKJC*.RUN legacy TAS Pro 6 programs + T7JC*.RWN stub wrappers
  (note: BKJCS.RUN and BKJCT.RUN do not exist — JC-S and JC-T are T7-only)
- **Operations**: 20 (JC-A through JC-T)

JC is a **reporting-only module** — it has no data entry operations. All JC reports read
from the same WO tables that the WO module writes. Several JC programs serve both JC-*
and LW-J-* menu paths (dual-menu programs).

## Narrative / vendor help

**→ [help-content.md](help-content.md)** — consolidated write-up of
all 20 help topics from `EvoHELP.CHM` (overview + JC-A through JC-S),
with the common-selection-ribbon pattern extracted once and each
report annotated with source tables, accuracy gotchas, and
cross-links into WO, GL, BM, and the System Overview close checklist.

---

## Menu operations — complete (all 19 programs binary-analyzed)

| Code | Operation | T7 Stub | BKJC*.RUN (KB) | Key Tables | Notes |
|------|-----------|---------|----------------|------------|-------|
| `JC-A` | Print Job Cost Report | t7jca.rwn | BKJCA (287) | WORKORD, WOROUT, OUTPROC, WOBOM, WOEXCHG, BKICMSTR, BKARCUST, MTICMSTR, CLASMSTR, BKAPVEND | Dual: JC-A + LW-J-F |
| `JC-B` | Print Profit Projection | t7jcb.rwn | BKJCB (98) | WORKORD, WOROUT, WOBOM, WOEXCHG, BKARCUST | Status [SRFC] |
| `JC-C` | Print Labor Transactions | T7JCC.RWN | BKJCC (135) | WOLABOR, BKPRMSTR, WOROUT, WORKORD, WORKCTR, BKICMSTR, MTICMSTR | Engine: BKJCENG; Status [FRCX] |
| `JC-D` | Print Overhead Transactions | T7JCD.RWN | BKJCD (128) | WOLABOR, BKPRMSTR, WOROUT, WORKORD, WORKCTR, BKICMSTR, MTICMSTR | Engine: BKJCENG; Status [FRCX] |
| `JC-E` | Print Material Issues | t7jce.rwn | BKJCE (250) | WOMAT, WORKORD, SCRAP, BKICMSTR, BKARCUST, MTICMSTR | Dual: JC-E + LW-J-C + DE-J-H-B; Status [SFRCXI] |
| `JC-F` | Print Outside Purchases | t7jcf.rwn | BKJCF (218) | OUTPROC, BKAPPO, WORKORD, BKICMSTR, BKAPVEND, BKARCUST, MTICMSTR | Dual: JC-F + LW-J-D; Status [FRCXSI] |
| `JC-G` | Print Labor Efficiency | T7JCG.RWN | BKJCG (122) | WOLABOR, BKPRMSTR, WOROUT, WORKORD, BKICMSTR, MTICMSTR | Engine: BKJCENG; Report: EMPLOYEE EFFICIENCY |
| `JC-H` | Print Work Order History | t7jch.rwn | BKJCH (218) | WOROUT, WORKORD, ROUTING, BKICMSTR, MTICMSTR, BKARCUST | Two modes: Active + Archive; Status [SFRCXI] |
| `JC-I` | Print Production by Work Center | T7JCI.RWN | BKJCI (55) | WOLABOR, WOROUT, WORKCTR | Engine: BKJCENG; Report totals by WC |
| `JC-J` | Print Production by Machine | T7JCJ.RWN | BKJCJ (55) | WOLABOR, MACHINE, WORKCTR | Engine: BKJCENG; Report totals by Machine |
| `JC-K` | Print Production by Tool | T7JCK.RWN | BKJCK (49) | WOLABOR, TOOL, MTICMSTR | Engine: BKJCENG; Report totals by Tool |
| `JC-L` | Print Job Cost Summary | t7jcl.rwn | BKJCL (206) | WORKORD, BKICMSTR, MTICMSTR, BKARCUST | Status [SFRCXI]; similar to BKLWJE but full 6-code filter |
| `JC-M` | Print WIP Summary | t7jcm.rwn | BKJCM (255) | WORKORD, WOMAT, WOLABOR, OUTPROC, BKAPPO, WORECV, WOEXCHG, BKARCUST, BKICLOCM | Dual: JC-M + LW-J-H(1) |
| `JC-N` | Print WIP Percent Completion | T7jcn.rwn | BKJCN (153) | WORKORD, WOMAT, WOLABOR, OUTPROC, WOROUT, WOEXCHG, WORECV, BKARCUST, BKICMSTR | Per-cost-type completion % |
| `JC-O` | Print Standard Labor Hours | T7JCO.RWN | BKJCO (61) | WOLABOR, WORKORD, WOROUT, WORKCTR, BKPRMSTR | Engine: BKJCENG |
| `JC-P` | Print Materials in WIP | t7jcp.rwn | BKJCP (212) | WOBOM, WORKORD, BKICMSTR, MTICMSTR, BKARCUST | Status [SFRCXI]; ISTS 10/04/17 |
| `JC-Q` | Print Work Order Receipts | t7jcq.rwn | BKJCQ (263) | WORKORD, SCRAP, WORECV, BKARCUST, BKICMSTR, MTICMSTR | Dual: JC-Q + LW-J-I; Status [SFRCXI] |
| `JC-R` | Multi-Level Assembly Cost Rollup | T7JCR.RWN | BKJCR (268) | WORKORD, BKICMSTR, WOMAT, WOLABOR, OUTPROC, BKAPPO, WORECV, WOEXCHG, BKARCUST | Dual: JC-R + LW-J-H(2); Status [CX] |
| `JC-S` | Work Order Detail Report | T7JCS.RWN | (no RUN file) | — | T7-only; no legacy TAS6 binary |
| `JC-T` | Scrap Yield Report | T7JCT.RWN | (no RUN file) | — | T7-only; no legacy TAS6 binary |

Additionally: `DEJC` = "Imported Labor Error Report" (t7dejc.rwn) — accessed via DE module.

---

## BKJCENG — JC Shared Engine Program

**BKJCENG.RUN (359 KB)** is the largest JC binary and is a shared engine called by multiple
smaller JC programs. It handles the common report engine logic for JC-C, JC-D, JC-G, JC-I,
JC-J, JC-K, and JC-O (confirmed from integer file-handle variables JCCI/JCDI/JCGI/JCII/JCJI/
JCKI/JCOI/JCENGI in the binary).

Tables in BKJCENG: BKYSMSTR, BKSYMSTR, WOLABOR, WORKORD, WORKCTR, BKICMSTR, TOOL, BKPRMSTR,
ROUTING, SCRAP, QCCODES, MACHINE, WOROUT, MTICMSTR, CLASMSTR, BKSBVEND, BKSBMFG, BKICREF,
BKICLOC, MKAHIST, BKAPDESC, FILELOC, BKAPVEND, BKARCUST, BKCMACCT

Archive tables in engine: WORKORDA, WOLABORA, WOROUTA, WORKHORDA, WOHLABORA (history labor),
WOHROUTF, WORKCTRA, BKPRMSTRA, BKICMSTRA, MTICMSTRA, MACHINEA, TOOLA, ROUTTEMPA, SCRAPA, QCCODESA

ISTS Enhancement: `04/01/15`

T7JCENG.DFM ("JC Engine", 54 fields, 104 controls) is the largest JC form and provides the
common selection/filter ribbon used by all JC engine-based reports.

---

## T7JC* programs are all stubs

Every T7JC* program in rwn_symbols.json has exactly 5 procedures and a single named
variable `STUB`. These are thin TAS Pro 7 wrapper programs that launch the legacy
BKJC*.RUN report programs. The actual report logic lives in the TAS Pro 6 binaries.

Confirmed from symbols: T7JCC / T7JCD / T7JCG / T7JCI / T7JCJ / T7JCK / T7JCO / T7JCT —
all 5p, vars=['STUB']

JC-S and JC-T have T7-only programs (no BKJCS/T.RUN exists on the share).

---

## Key reports — binary analysis (Passes 318-319)

### JC-A / LW-J-F: Job Cost Report (BKJCA.RUN — 287 KB)

The master per-WO cost breakdown report. Serves both JC-A and LW-J-F.

**Tables**: WORKORD, WOROUT, OUTPROC, WOBOM, WOEXCHG, MTICMSTR, BKICMSTR, BKARCUST,
BKAPDESC, CLASMSTR, BKSBVEND, BKSBMFG, BKICREF, BKICLOC, BKCMACCT, BKAPVEND

Archive tables: WOBOMA, WOROUTA, WORKORDA, WOHBOMA, WOHROUTA, WORKHORDA, OUTHPROCA

Report sections: JOB SUMMARY (Estimated/Actual/Variance per-part + total), Labor, Setup,
Outside Proc. Status filter [SFRCXI].
ISTS enhancement: `07/14/20`

---

### JC-B: Profit Projection (BKJCB.RUN — 98 KB)

Per-WO and Composite Profit Projection — projects final cost based on percent complete.

**Tables**: WORKORD, WOROUT, WOBOM, WOEXCHG, BKARCUST + archives (WORKORDA, WOBOMA, WOROUTA)

Report sections: Labor, Setup, Outside Proc, Fixed Ovhd, Variable Ovhd, Materials, Misc,
Extra, Totals, Profit, Profit%. Columns: Actual Cost to Date / Percent Compl / Estimated Cost /
Projected Cost / %Var

Composite mode: aggregate all matching WOs onto one report.
Status filter [SRFC] — 4 codes only (excludes X=Cancelled, I=In Process).

---

### JC-C: Labor Transactions (BKJCC.RUN — 135 KB)

Prints WOLABOR transaction detail records.

**Tables**: WOLABOR, BKPRMSTR, WOROUT, WORKORD, WORKCTR, BKICMSTR, MTICMSTR, CLASMSTR,
BKSBVEND, BKSBMFG, BKICREF, BKICLOC + archives (WOLABORA, LABTRANA, WORKCTRA, etc.)

Calls BKJCENG engine. Archive table: LABTRANA (WOLABOR history archive).
Status filter [FRCX] — excludes S=Scheduled, I=In Process.
Sort options: by WO Number or by Labor Date [W/D]. Sub-totals option.
Report columns: Date, Emp Last Name, WO, Status, Seq, Oper, Job, Hrs, Setup, Qty Comp,
Scrapped, Scrap Code, Rework, QC Code, Rate, Cost.

---

### JC-D: Overhead Transactions (BKJCD.RUN — 128 KB)

Overhead transaction detail (machine/fixed/variable overhead).

**Tables**: WOLABOR, BKPRMSTR, WOROUT, BKYSMSTR, WORKORD, BKICMSTR, WORKCTR, MTICMSTR,
CLASMSTR + archives. Archive table: OHTRANA (overhead transactions archive).

Calls BKJCENG engine. Status filter [FRCX].
Filter options: Date, Employee, WO, Part, Sequence, WC, Job ranges + WO Status.

---

### JC-E / LW-J-C: Material Issues (BKJCE.RUN — 250 KB)

Reports WO material issue transactions from WOMAT. Serves JC-E, LW-J-C, and DE-J-H-B.

**Tables**: WOMAT, WORKORD, SCRAP, BKICMSTR, MTICMSTR, CLASMSTR, BKSBVEND, BKSBMFG,
BKICREF, BKICLOC, BKARCUST, BKAPDESC, BKAPVEND, BKCMACCT

Status filter string `SFRCXI` — all 6 WO status codes TAS6-era confirmed.
Item type filter: `RFAMNLBTKOL` (10 types). Sort: Date/WO/Component.
ISTS enhancement: `08/20/18`

---

### JC-F / LW-J-D: Outside Purchases (BKJCF.RUN — 218 KB)

Reports outside-process PO costs. Serves both JC-F and LW-J-D.

**Tables**: OUTPROC, BKAPPO, WORKORD, BKICMSTR, MTICMSTR, CLASMSTR, BKSBVEND, BKSBMFG,
BKICREF, BKICLOC, BKAPDESC, MKAHIST, BKAPVEND, BKARCUST, BKCMACCT

Archive tables: BKAPHPOA (AP hist PO), BKAPPOA (AP PO archive), OUTPROCA, WORKHORDA, OUTHPROCA
Status filter [FRCXSI] = 6 codes (F/R/C/X/S/I). PO Type filter also available.
ISTS enhancement: `01/01/07`

---

### JC-G: Labor Efficiency (BKJCG.RUN — 122 KB)

Employee efficiency report by date/WO/part range.

**Tables**: WOLABOR, BKPRMSTR, WOROUT, WORKORD, BKICMSTR, MTICMSTR, CLASMSTR + archives

Archive table: LABEFFA (labor efficiency archive). Calls BKJCENG engine.
Report title: EMPLOYEE EFFICIENCY. Columns show efficiency metrics.
Filter: Date range, Employee range, WO range, Part range.

---

### JC-H: Work Order History (BKJCH.RUN — 218 KB)

Prints routing/operation history for WOs. Has two modes (Active WO and Archive WO).

**Tables**: WOROUT, WORKORD, ROUTING, BKYSMSTR, BKICMSTR, MTICMSTR, CLASMSTR, BKSBVEND,
BKSBMFG, BKICREF, BKICLOC, MKAHIST, BKAPDESC, FILELOC, BKAPVEND, BKARCUST, BKCMACCT

Archive tables: WORKORDA, WOROUTA, WORKHORDA, WOHROUTA, ROUTINGA
Status filter [SFRCXI] = full 6-code set. Filter: Item, Date, Seq, Oper, WC, Class ranges.
ISTS enhancement: `06/13/17`

---

### JC-I: Production by Work Center (BKJCI.RUN — 55 KB)

**Tables**: WOLABOR, WOROUT, WORKCTR (+ archives PRDWCA, WOLABORA, WOROUTA, WORKCTRA)

Calls BKJCENG engine. Filter: Date range, Department range, WC range.
Report: Work Center Totals + Grand Totals.

---

### JC-J: Production by Machine (BKJCJ.RUN — 55 KB)

**Tables**: WOLABOR, MACHINE, WORKCTR (+ archives PRDMACHA, MACHINEA, WORKCTRA, WOLABORA)

Calls BKJCENG engine. Filter: WC range, Date range, Machine range.
Report: Machine Totals + Grand Totals.

---

### JC-K: Production by Tool (BKJCK.RUN — 49 KB)

**Tables**: WOLABOR, TOOL, MTICMSTR (+ archives PRDTOOLA, WOLABORA, TOOLA)

Calls BKJCENG engine. Filter: Date range, Tool range.
Report: PRODUCTION BY TOOL with Tool Totals.

---

### JC-L: Job Cost Summary (BKJCL.RUN — 206 KB)

Per-WO job cost summary (similar to LW-J-E BKLWJE, but in JC menu with full SFRCXI filter).

**Tables**: WORKORD, BKICMSTR, MTICMSTR, CLASMSTR, BKSBVEND, BKSBMFG, BKICREF, BKICLOC,
BKAPDESC, MKAHIST, BKAPVEND, BKARCUST, BKCMACCT + archives (WORKORDA, WORKHORDA)

Status filter [SFRCXI] — full 6-code set (vs BKLWJE which uses SFRC only).
Filter: WO range, Part range, Start Date range, Finished Date range, Order Status.
ISTS enhancement: `11/30/10`

---

### JC-M / LW-J-H (part 1): WIP Summary (BKJCM.RUN — 255 KB)

**Tables**: WORKORD, MTICMSTR, BKICMSTR, WOMAT, WOLABOR, OUTPROC, BKAPPO, WORECV,
WOEXCHG, BKARCUST, BKICLOCM, BKSYPRTR, BKSBVEND, BKSBMFG, BKICREF, BKICLOC

Active (A) vs. Archived (D) WO filter. Sections: WIP Variance, Variance, Scrap.
ISTS enhancement: `06/30/09`

---

### JC-N: WIP Percent Completion (BKJCN.RUN — 153 KB)

Per-WO completion percentage by cost type.

**Tables**: WORKORD, WOMAT, MTICMSTR, WOLABOR, OUTPROC, WOROUT, WOEXCHG, WORECV,
BKARCUST, BKICMSTR, CLASMSTR, BKSBVEND, BKSBMFG, BKICREF, BKICLOC

Report shows: per-WO Setup/Material/Out Proc/Labor/Fixed OH/Var OH/Misc/Extra completion%.
Filter: Transaction Date range, WO range, Item range, Customer range.

---

### JC-O: Standard Labor Hours (BKJCO.RUN — 61 KB)

**Tables**: WOLABOR, WORKORD, WOROUT, WORKCTR, BKPRMSTR
(+ archives: STDHRSA, WOROUTA, WORKCTRA, BKPRMSTRA, WORKORDA, WOLABORA)

Calls BKJCENG engine. Reports standard vs. actual labor hours.

---

### JC-P: Materials in WIP (BKJCP.RUN — 212 KB)

Lists BOM materials that are in WIP (issued but not yet received as finished goods).

**Tables**: WOBOM, WORKORD, BKICMSTR, MTICMSTR, CLASMSTR, BKSBVEND, BKSBMFG, BKICREF,
BKICLOC, BKAPDESC, MKAHIST, BKAPVEND, BKARCUST, BKCMACCT + archives (WORKORDA, WOBOMA)

Archive table: BKREBWOA (WO BOM rebuild archive).
Status filter [SFRCXI]. Filter: WO range, Component range, WO Status.
ISTS enhancement: `10/04/17`

---

### JC-Q / LW-J-I: Work Order Receipts (BKJCQ.RUN — 263 KB)

**Tables**: WORKORD, SCRAP, WORECV, BKARCUST, BKICMSTR, MTICMSTR, CLASMSTR

Status filter [SFRCXI] — full 6-code set. Sections: Fin Prod, Wip Variance, Scrap.

---

### JC-R / LW-J-H (part 2): Multi-Level Assembly Cost Rollup (BKJCR.RUN — 268 KB)

Also titled "LW-J-H Print WIP Summary" — shares LW-J-H with JC-M.

**Tables**: WORKORD, BKICMSTR, MTICMSTR, WOMAT, WOLABOR, OUTPROC, BKAPPO, WORECV,
WOEXCHG, BKARCUST, CLASMSTR, BKSBVEND, BKSBMFG, BKICREF, BKICLOC

Status filter [CX] (narrower). ISTS enhancement: `01/05/21`

---

### LW-J-E only: Job Cost Summary (BKLWJE.RUN — 115 KB)

LW-specific — not in JC menu. Accessible only via LW-J-E.

**Tables**: WORKORD, BKICMSTR, MTICMSTR, CLASMSTR, BKSBVEND, BKSBMFG, BKICREF, BKICLOC,
BKSYMSTR

Status filter [SFRC] — narrower than JC-L (excludes X=Cancelled, I=In Process).

---

## UI forms (14)

| DFM file | Caption | Fields | Controls | Tabs |
| -------- | ------- | -----: | -------: | ---: |
| `T7JCA.DFM` | New Screen | 17 | 45 | 0 |
| `T7JCB.DFM` | New Screen | 10 | 34 | 0 |
| `T7JCE.DFM` | JC-E | 20 | 53 | 0 |
| `T7JCENG.DFM` | JC Engine | 54 | 104 | 0 |
| `T7JCF.DFM` | New Screen | 19 | 53 | 0 |
| `T7JCH.DFM` | New Screen | 22 | 56 | 0 |
| `T7JCL.DFM` | JC-L | 12 | 39 | 0 |
| `T7JCM.DFM` | JC-M | 28 | 62 | 0 |
| `T7JCN.DFM` | JC-N | 14 | 40 | 0 |
| `T7JCP.DFM` | JC-P Print Materials in WIP | 8 | 30 | 0 |
| `T7JCQ.DFM` | New Screen | 20 | 43 | 0 |
| `T7JCR.DFM` | New Screen | 23 | 53 | 0 |
| `T7JCRM.DFM` | New Screen | 5 | 29 | 0 |
| `T7JCS.DFM` | JC-S | 22 | 54 | 0 |

`T7JCENG.DFM` (54 fields, 104 controls) is the common selection ribbon used by all
BKJCENG-based reports (JC-C/D/G/I/J/K/O).

---

## Archive table inventory (JC-specific)

All JC programs with archive access use corresponding `*A`-suffixed Btrieve alternate-key
handles for the archive variants of the primary tables. Notable JC-specific archive tables:

| Archive table | Source | Context |
|---|---|---|
| `LABTRANA` | WOLABOR archive | Used by JC-C labor transactions |
| `OHTRANA` | Overhead transactions archive | Used by JC-D overhead transactions |
| `LABEFFA` | Labor efficiency archive | Used by JC-G labor efficiency |
| `PRDWCA` | Production by WC archive | Used by JC-I |
| `PRDMACHA` | Production by machine archive | Used by JC-J |
| `PRDTOOLA` | Production by tool archive | Used by JC-K |
| `STDHRSA` | Standard hours archive | Used by JC-O |
| `OUTHPROCA` | Outside process history archive | Used by JC-F (OUTPROC history) |
| `BKAPHPOA` | AP history PO archive | Used by JC-F |
| `BKAPPOA` | AP PO archive | Used by JC-F |
| `BKREBWOA` | WO BOM rebuild archive | Used by JC-P |

---

## Architecture notes

- **Reporting-only**: No JC program writes to any table. All read from WO tables.
- **No dedicated tables**: JC has 0 dedicated Btrieve tables.
- **BKJCENG shared engine**: The 359 KB engine handles JC-C/D/G/I/J/K/O (7 operations).
  Individual caller programs (BKJCI/J/K/O) are 49-61 KB launchers that delegate to the engine.
- **Dual-menu programs**: JC-A+LW-J-F (BKJCA), JC-E+LW-J-C+DE-J-H-B (BKJCE),
  JC-F+LW-J-D (BKJCF), JC-M+LW-J-H (BKJCM), JC-R+LW-J-H (BKJCR), JC-Q+LW-J-I (BKJCQ).
- **T7 stubs → TAS6 legacy**: All T7JC* programs are 5-proc stubs. JC-S and JC-T have no
  legacy binary (T7-only programs, BKJCS/T.RUN absent from network share).
- **ISTS Enhancements**: Post-2007 customizations: BKJCA (07/14/20), BKJCE (08/20/18),
  BKJCENG (04/01/15), BKJCF (01/01/07), BKJCH (06/13/17), BKJCL (11/30/10),
  BKJCM (06/30/09), BKJCP (10/04/17), BKJCR (01/05/21).
- **Archive access**: Most JC reports read both live WO tables and archive variants.
- **Status filter variation**: Most JC reports use full [SFRCXI]; JC-B uses [SRFC];
  JC-C/D use [FRCX]; JC-R uses [CX]. BKLWJE uses [SFRC].

---

## Live Data Analysis (Pass 421, 2026-06-30)

| Table | Count | Notes |
|-------|------:|-------|
| ISJOB | 45,862 | Job code master (IS_JOB_NUMB + DESC + CUST + VEND + STATUS) |
| ISJBSF | 142 | Business scorecard records |

ISJOB has 45,862 job codes — all with STATUS=' ' (blank). ISJOB serves as a reference
table for job number tracking in WO labor and inventory transactions; blank STATUS for
all records confirms job codes are passive reference data (not individually
activated/deactivated). ISJBSF=142 (business scorecard, lightly used).

**Confidence: 92/100** — All 19 BKJC*.RUN programs binary-analyzed with table lists,
report layouts, status filters, ISTS enhancement dates, archive table inventory, and
dual-menu assignments confirmed; 2 programs (JC-S, JC-T) are T7-only (no RUN file).
Live data: ISJOB=45,862 (Pass421). Remaining gap: bytecode-level field-access namespace
analysis not done (requires RWN decryption, blocked).
