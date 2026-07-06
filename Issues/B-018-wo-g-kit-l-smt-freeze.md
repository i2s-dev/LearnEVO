# B-018: WO-G KIT=L freeze for SMT work orders (WOBOM OPTION issue)
**Status:** ACTIVE — root cause partially confirmed; fix not yet applied
**Date:** 2026-06-29
**Keywords:** WO-G, KIT=L, SMT, freeze, WOBOM, WOBOM_OPTION, T7WOG, T7WOG4, WINPOS, REMAINING, COMPCODE, Btrieve, 75338, 75405, 54552

## Symptom
When an SMT associate enters a work order in WO-G (Issue Material), selects KIT=L (List), and presses Enter, the entire EVO program freezes before the kit selection list appears. Only the SMT department is affected — other departments' WOs work fine. The associate must force-kill EvoERP to recover. Affects: 75405-3, 75338-2, 75338-4 (reported frozen); 75338-1, 75338-3, 75338-5 confirmed working.

## Root Cause
**Confirmed freeze mechanism (2026-06-29 — database correlation, 7/7 WOs):**

WINPOS reads the **first** mandatory WOBOM record sorted by COMPCODE (Btrieve key order). It computes REMAINING = WOBOM_TOTQTY − WOBOM_QTYISSUED for that ONE record, then passes it to T7WOG4 (the kit list display form). If REMAINING = 0 → T7WOG4 freezes. If no mandatory records exist → WINPOS TERMINATEs showing an "all processed" message (form closes).

| WO | Outcome | First mandatory COMPCODE | REMAINING |
|---|---|---|---|
| 75338-1 | works | 055-03950-0 | 10.0 |
| 75338-2 | FREEZES | (no mandatory items) | N/A → TERMINATE |
| 75338-3 | works | 055-03950-0 | 2.0 |
| 75338-4 | FREEZES | (no mandatory items) | N/A → TERMINATE |
| 75338-5 | works | 055-03950-0 | 2.0 |
| 75405-3 | FREEZES | 055-03950-0 (fully issued) | 0.0 |
| 54552-1 | FREEZES | 055-53829-0M40K (fully issued) | 0.0 |

**Root cause for 75338-2:** WOBOM_OPTION='1' used for mandatory items instead of 'N'. WINPOS reads WOBOM records filtered by OPTION='N' via Btrieve key. With no OPTION='N' records found, WINPOS either TERMINATEs or passes 0-remaining-qty to T7WOG4.

**Root cause for 75338-4:** No mandatory items at all — only OPTION='2', '3', '4'. Same WINPOS mechanism.

**Root cause for 75405-3:** WOBOM has OPTION='N' correctly for 21 mandatory items, but the WO is in a partially-issued state: 9 of 21 mandatory items fully issued, 12 not yet issued. First mandatory by COMPCODE = 055-03950-0 (fully issued, REMAINING=0) → T7WOG4 freezes.

**54552-1:** STATUS='R' (Completed, 375 units done). 13 mandatory items; first mandatory by COMPCODE = 055-53829-0M40K (TOTQTY=QTYISSUED=400, REMAINING=0) → freeze.

## Attempts

**Investigation data (2026-06-29):**

Within WO 75338, comparison of freezing vs working suffixes:

| Suffix | Status  | OPTION distribution in WOBOM |
|--------|---------|------------------------------|
| -1     | WORKS   | OPTION='N' (24 mandatory) + 2/3/4 option groups |
| -2     | FREEZES | OPTION='1' (21 "mandatory") + 2/3/4 option groups — NO N |
| -3     | WORKS   | OPTION='N' (21 mandatory) + 2/3/4 option groups |
| -4     | FREEZES | OPTION='2','3','4' only — NO mandatory items at all |
| -5     | WORKS   | OPTION='N' (20 mandatory) + 2/3/4 option groups |

75405-3 (FREEZES): OPTION='N' (21) + 2/3/4 — same distribution as working WOs (anomalous, but partial-issue state explains it).

**Binary analysis results (2026-06-29 — wog_deep2.py):**

T7WOG.RWN binary decoded. Key confirmed facts:
- **LOAD.KIT (3351-3413)** = BIN VALIDATION only (validates which physical bin to pull from). Contains ZERO loop instructions. The "LOAD.KIT loop counter" hypothesis was WRONG.
- **WINPOS (1491-1548)** = the actual WOBOM reader. 58 instructions, ZERO loop instructions. Contains two DB_V calls: [1494] and [1536]. Contains TERMINATE at [1503] (conditional). At [1544]: EVAL WOBOM.TOTQTY - WOBOM.QTYISSUED → calculates remaining qty to issue. At [1538]: string "T7WOG4" appears → WINPOS launches **T7WOG4** (the kit list display form).
- **T7WOG4** = the separate kit list display form. T7WOG4.RWN NOT yet decrypted (needs IV from debugger session). **The freeze most likely occurs inside T7WOG4.**
- **WOBOM.OPTION** has ZERO code-level comparisons in T7WOG.RWN. Filtering is done entirely at the Btrieve key level inside the DB_V call — never tested in TAS Pro code.
- **ALL database access** is via DB_V (0x5C sub=0C). Zero DB_READ (0x9A) instructions exist.
- **WHATSON (1691-1770)** = WIP material cost accounting processor. NOT the kit list builder.
- **VLD_QTYISSUED (1306-1340)** = post-issue "completed?" confirmation dialog. NOT a qty validator.
- **KIT.LIST (348-365)** = operation range selector (FROM.OPER / THRU.OPER input). NOT BOM loader.
- Procedures with LOOP relevant to kit display: none in the 1491-1548 WINPOS range. LOOPs found in: LOAD.DO.POH, POST.ICUV, EXPLODE_BOM, NO.KIT.2, ADD.NEG.BUCK, SHOWHLP.

**Fix attempts:** None applied yet — database is read-only for this workspace. Must be done in EVO or directly via Pervasive SQL by someone with write access.

**Confirmed workaround (2026-07-01):** KIT=Y (issue all) confirmed working by live user test. Bypasses T7WOG4 entirely — no REMAINING=0 path. Use KIT=Y for all affected SMT WOs until the underlying T7WOG4 bug is resolved.

**BKBMMSTR structure for key BOM templates:**
- CP4E-08W-30K-H: A=6, B=6, N=3, R=14 rows (HAS TYPE=N)
- CP1E-08W-30K-HE: A=8, B=3, R=14 rows (no TYPE=N) → 75338-3 WORKS
- CP1E-08W-30K-H: A=8, B=4, R=14 rows (no TYPE=N) → 75338-2 FREEZES (OPTION=1 bug)
- CP1E-09W-30K-H: A=7, B=5, R=14 rows (no TYPE=N) → 75405-3 FREEZES (partial issue state)

**Issue state for 75405-3 mandatory items:**
- 9 of 21 at ^ISSUED=100 (fully done): 055-03950-0, 055-04651-30KH, 055-04764-1, 650-50138-ERP3, 650-50185-ERP, 650-50525-12, 650-50797-ERP1, 650-51141, 685-50822-12
- 12 of 21 at ^ISSUED=0 (not yet issued): 530-50802, 640-02157, 640-50577, 642-50566, 685-50532ERP-12, 700-50487-B-01, 700-50487E-A-1, 701-50530-C-12, 703-50112-C, 720-50565-01, 740-05085-BR, 800-50931

**WOBOM_^ISSUED field clarified:** NUMERIC field holding the percentage of total quantity already issued (QTYISSUED / TOTQTY * 100). Values: 0.0 = nothing issued, 100.0 = fully issued, 37.98 = partial. NOT a boolean flag.

**Additional finding (Pass 430, 2026-06-30):** Live BKYSMSTR query confirmed BKYS_YN_31='I'. The T7YSYN linear mapping (disproven) assigns ISTS.CFG.WOGKIT to YN[31]. The value 'I' is plausibly WOGKIT = Individual/List mode ('I'). If WOGKIT controlled the default KIT= mode shown at WO-G entry, then 'I'=Individual may be the configured default — meaning all users default to KIT=L and encounter this bug whenever their first mandatory item is fully issued.

**What's still needed to fully close:**
1. T7WOG4.RWN decrypted (needs IV from one Frida debugger session) to see exact hang mechanism
2. Confirm whether Btrieve key is by COMPCODE only or OPER+COMPCODE+WOPRE+WOSUF

## Resolution / Lesson
WOBOM_OPTION='N' = mandatory (filtered by Btrieve key in WINPOS DB_V, not by TAS code). WOBOM_OPTION='1' through '4' = optional selection groups. OPTION='1' is NOT the same as mandatory — it is optional group 1. Any WO where mandatory BOM items have OPTION='1' will freeze on KIT=L because WINPOS finds 0 mandatory records and launches T7WOG4 with 0-row input. The LOAD.KIT hypothesis (loop counter) was completely wrong — LOAD.KIT is bin validation, not the BOM loader. The BOM reader is WINPOS; the display is T7WOG4 (separate module).

**Recommended fix:**
- IMMEDIATE workaround for ALL affected WOs: Use KIT=Y (issue all) instead of KIT=L (list). CONFIRMED WORKING.
- For 75338-2 specifically: UPDATE WOBOM SET WOBOM_OPTION='N' WHERE WOBOM_WOPRE='75338' AND WOBOM_WOSUF='2' AND WOBOM_OPTION='1' (21 rows)
- For 75338-4: No mandatory items exist. Options: add mandatory WOBOM records, or use KIT=Y.
- For 75405-3: WO is in a partial issue state — use KIT=Y to issue remaining components.
- Long-term BOM fix: Review all CP1E-* BOM templates to ensure mandatory components are encoded with BKBM_PROD_TYPE='N' (not 'A' or 'B'), and that WO creation propagates this correctly to WOBOM_OPTION='N'.
- Long-term code fix (requires EVO vendor or T7WOG4 decode): investigate T7WOG4 and how it handles 0-remaining-qty input. The fix is in T7WOG4, not T7WOG or LOAD.KIT.
