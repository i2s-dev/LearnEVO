# Job Costing (JC)

Status: partial | Binary analysis Pass 318 2026-06-26; CHM auto-generated baseline updated.

Sources: BKMENUSU.TXT program list, BKJCA/CE/CM/CQ/CR/LWJE.RUN binary string extraction,
rwn_symbols.json (T7JC* stubs), DDF schema, EvoHELP.CHM (20 topics in help-content.md).

- **Module code**: `JC`
- **Menu group**: "Job Costing" (Mfg group)
- **Tables**: 0 dedicated — JC reads WO tables (WORKORD, WOROUT, WOBOM, WOMAT, WOLABOR,
  WORECV, WOEXCHG, OUTPROC) and supporting masters (BKICMSTR, BKARCUST, MTICMSTR, CLASMSTR, etc.)
- **UI forms**: 14 (T7JC* DFM files)
- **Programs**: 19 BKJC*.RUN legacy TAS Pro 6 programs + T7JC*.RWN stub wrappers
- **Operations**: 20 (JC-A through JC-T)

JC is a **reporting-only module** — it has no data entry operations. All JC reports read
from the same WO tables that the WO module writes. Several JC programs are shared with
the LW module (same physical program, two menu paths).

## Narrative / vendor help

**→ [help-content.md](help-content.md)** — consolidated write-up of
all 20 help topics from `EvoHELP.CHM` (overview + JC-A through JC-S),
with the common-selection-ribbon pattern extracted once and each
report annotated with source tables, accuracy gotchas, and
cross-links into WO, GL, BM, and the System Overview close checklist.

---

## Menu operations

| Code | Operation | T7 Stub | Legacy TAS6 | Key Tables (binary-confirmed) |
|------|-----------|---------|-------------|-------------------------------|
| `JC-A` | Print Job Cost Report | t7jca.rwn | BKJCA.RUN | WORKORD, WOROUT, OUTPROC, WOBOM, WOEXCHG, BKICMSTR, BKARCUST, MTICMSTR, CLASMSTR |
| `JC-B` | Print Profit Projection | t7jcb.rwn | BKJCB.RUN | (not yet extracted) |
| `JC-C` | Print Labor Transactions | T7JCC.RWN | BKJCC.RUN | WORKORD, WOROUT, WOBOM, WOEXCHG, WORKCTR |
| `JC-D` | Print Overhead Transactions | T7JCD.RWN | BKJCD.RUN | WORKORD, WOROUT, WOBOM, WOEXCHG |
| `JC-E` | Print Material Issues | t7jce.rwn | BKJCE.RUN | WOMAT, WORKORD, SCRAP, BKICMSTR, BKARCUST, MTICMSTR |
| `JC-F` | Print Outside Purchases | t7jcf.rwn | BKJCF.RUN | (not yet extracted) |
| `JC-G` | Print Labor Efficiency | T7JCG.RWN | BKJCG.RUN | BKSYMSTR, BKICMSTR, WORKORD, OUTPROC, BKAPPO, BKAPPOL, BKQCTRAN |
| `JC-H` | Print Work Order History | t7jch.rwn | BKJCH.RUN | (not yet extracted) |
| `JC-I` | Print Production by Work Center | T7JCI.RWN | BKJCI.RUN | BKSYMSTR, BKICMSTR, WOROUT, WORKORD, ROUTING |
| `JC-J` | Print Production by Machine | T7JCJ.RWN | BKJCJ.RUN | BKSYMSTR, BKICMSTR, WOROUT, WORKORD, ROUTING |
| `JC-K` | Print Production by Tool | T7JCK.RWN | BKJCK.RUN | BKSYMSTR, BKICMSTR, WOROUT, WORKORD, ROUTING |
| `JC-L` | Print Job Cost Summary | t7jcl.rwn | BKJCL.RUN | (not yet extracted — possibly T7-era replacement for BKLWJE?) |
| `JC-M` | Print WIP Summary | t7jcm.rwn | BKJCM.RUN | WORKORD, WOMAT, WOLABOR, OUTPROC, BKAPPO, WORECV, WOEXCHG, BKARCUST, BKICLOCM |
| `JC-N` | Print WIP Percent Completion | T7jcn.rwn | BKJCN.RUN | (not yet extracted) |
| `JC-O` | Print Standard Labor Hours | T7JCO.RWN | BKJCO.RUN | BKICMSTR, WORKORD, MTICMSTR, WOMAT, WOLABOR, OUTPROC, WOROUT, WOEXCHG, WORECV |
| `JC-P` | Print Materials in WIP | t7jcp.rwn | BKJCP.RUN | (not yet extracted) |
| `JC-Q` | Print Work Order Receipts | t7jcq.rwn | BKJCQ.RUN | WORKORD, SCRAP, WORECV, BKARCUST, BKICMSTR, MTICMSTR |
| `JC-R` | Multi-Level Assembly Cost Rollup | T7JCR.RWN | BKJCR.RUN | WORKORD, BKICMSTR, WOMAT, WOLABOR, OUTPROC, BKAPPO, WORECV, WOEXCHG, BKARCUST |
| `JC-S` | Work Order Detail Report | T7JCS.RWN | (?) | (not yet extracted) |
| `JC-T` | Scrap Yield Report | T7JCT.RWN | BKJCT.RUN | (not yet extracted) |

Additionally: `DEJC` = "Imported Labor Error Report" (t7dejc.rwn) — accessed via DE module.

---

## T7JC* programs are all stubs

Every T7JC* program in rwn_symbols.json has exactly 5 procedures and a single named
variable `STUB`. These are thin TAS Pro 7 wrapper programs that launch the legacy
BKJC*.RUN report programs. The actual report logic lives in the TAS Pro 6 binaries.

Confirmed from symbols: T7JCC / T7JCD / T7JCG / T7JCI / T7JCJ / T7JCK / T7JCO / T7JCT —
all 5p, vars=['STUB']

---

## Key reports — confirmed from binary string analysis (Pass 318)

### JC-A / LW-J-F: Job Cost Report (BKJCA.RUN — 293 KB)

The master per-WO cost breakdown report. Serves both JC-A and LW-J-F (two title strings
in one binary): `"JC-A  Print Job Cost Report"` and `"LW-J-F  Print Job Cost Report"`.

**Tables**: WORKORD, WOROUT, OUTPROC, WOBOM, WOEXCHG, MTICMSTR, BKICMSTR, BKARCUST,
BKAPDESC, CLASMSTR, BKSBVEND, BKSBMFG, BKICREF, BKICLOC, BKCMACCT, BKAPVEND

Archive access: WOBOMA, WOROUTA, WORKORDA, WOHBOMA, WOHROUTA, WORKHORDA, OUTHPROCA.

**Report sections**:
```
JOB COST REPORT                      Page: N
Work Order   :       -                      Customer:
Part Number  :                              Name    :
Purchase Order:
Qty to Make  :                              Selling Price :
Qty Complete :                              Actual Start  :
Status       :                              Actual Finish :
Gen & Admin %:                              Job Number    :

================================ JOB SUMMARY ===================================
              Estimated      Actual    Estimated      Actual    %
             Per Part      Per Part       Total        Total   Var
Qty Complete:
Labor
Setup
Outside Proc
```

Filter options: WO range, Part range, Job range, Customer range, WO Status [SFRCXI],
include closed/cancelled toggle, include archive toggle, detail vs. summary mode.

ISTS enhancement note: `07/14/20` in binary.

---

### JC-E / LW-J-C: Material Issues (BKJCE.RUN — 256 KB)

Reports WO material issue transactions from WOMAT. Serves JC-E, LW-J-C, and
`"DE-J-H-B  Print Imported Material Issues"` — the same binary handles 3 menu entry points.

**Tables**: WOMAT, WORKORD, SCRAP, BKICMSTR, MTICMSTR, CLASMSTR, BKSBVEND, BKSBMFG,
BKICREF, BKICLOC, BKARCUST, BKAPDESC, BKAPVEND, BKCMACCT

**WO status filter string**: `SFRCXI` — confirms all 6 WO status codes are TAS6-era:
S = Scheduled, F = Released, R = Completed, C = Closed, X = Cancelled, I = In Process

Item type filter string: `RFAMNLBTKOL` = 10 item types (R/F/A/M/N/L/B/T/K/O).
Sort options: Date, WO/Date, Component [D/W/C]. Archive access: WOEMATA, WOHMATL.
ISTS enhancement note: `08/20/18` in binary.

---

### JC-M / LW-J-H (part 1): WIP Summary (BKJCM.RUN — 261 KB)

**Tables**: WORKORD, MTICMSTR, BKICMSTR, WOMAT, WOLABOR, OUTPROC, BKAPPO, WORECV,
WOEXCHG, BKARCUST, BKICLOCM, BKSYPRTR, BKSBVEND, BKSBMFG, BKICREF, BKICLOC

Report sections: WIP Variance, Variance column, Scrap section.
Active (A) vs. Archived (D) WO filter. ISTS enhancement note: `06/30/09` in binary.

---

### JC-R / LW-J-H (part 2): Multi-Assembly Cost Rollup (BKJCR.RUN — 274 KB)

Also titled `"LW-J-H Print WIP Summary"` — shares the LW-J-H slot with JC-M.
The menu dispatches to both BKJCM and BKJCR for LW-J-H.

**Tables**: WORKORD, BKICMSTR, MTICMSTR, WOMAT, WOLABOR, OUTPROC, BKAPPO, WORECV,
WOEXCHG, BKARCUST, CLASMSTR, BKSBVEND, BKSBMFG, BKICREF, BKICLOC

WO Status [CX] = Active/Closed filter (narrower than SFRCXI).
ISTS enhancement note: `01/05/21` in binary.

---

### JC-Q / LW-J-I: Work Order Receipts (BKJCQ.RUN — 269 KB)

**Tables**: WORKORD, SCRAP, WORECV, BKARCUST, BKICMSTR, MTICMSTR, CLASMSTR

WO Status filter: `SFRCXI A` — full 6-code set confirmed, TAS6-era.
Sections: "Fin Prod" (Finished Production), "Wip Variance", "Scrap" — toggleable.

---

### LW-J-E only: Job Cost Summary (BKLWJE.RUN — 115 KB)

**LW-specific program — not in JC menu.** Accessible only via LW-J-E.

**Tables**: WORKORD, BKICMSTR, MTICMSTR, CLASMSTR, BKSBVEND, BKSBMFG, BKICREF, BKICLOC,
BKSYMSTR

Report: `JOB COST SUMMARY`
Columns: Work Order, Part Number, Act Start, Act Fin, Order Qty, Comp Qty, Status, Std Cost,
Act Total, Variance, %Var. Filter: WO range, Part range, Start/Finish Date, Status [SFRC].
Note: [SFRC] only — narrower filter than JC reports (excludes X=Cancelled, I=In Process).

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

`T7JCENG.DFM` (54 fields, 104 controls) is the largest JC form — likely the common
report filter/selection engine that all T7JC* stubs load.

---

## Architecture notes

- **Reporting-only**: No JC program writes to any table. All read from WO tables.
- **No dedicated tables**: WOHLABOR / WOLABOR are WO/LW tables; JC has 0 dedicated tables.
- **Dual-menu programs**: BKJCA (JC-A + LW-J-F), BKJCE (JC-E + LW-J-C + DE-J-H-B),
  BKJCM (JC-M + LW-J-H), BKJCR (JC-R + LW-J-H), BKJCQ (JC-Q + LW-J-I).
  The binary contains multiple title strings; the menu dispatcher selects which to display.
- **T7 stubs → TAS6 legacy**: All T7JC* programs are 5-proc stubs that launch TAS6
  BKJC*.RUN programs. No T7-era rewrite exists for any JC report.
- **ISTS Enhancements**: Post-2009 customizations confirmed: BKJCA (07/14/20),
  BKJCE (08/20/18), BKJCM (06/30/09), BKJCR (01/05/21).
- **Archive access**: Most JC reports read both live WO tables and archived counterparts
  (WORKORDA, WOHBOMA, WOEMATA, etc.) when the archive filter is enabled.

---

**Confidence: 75/100** — JC module program list complete (20 ops, T7 stubs confirmed);
5 of 19 programs binary-confirmed (JC-A/E/M/Q/R); 14 programs not yet extracted;
dual-menu architecture and SFRCXI status codes confirmed from 3+ TAS6 binaries.
