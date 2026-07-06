# M-003: yn_table.txt pool-order is NOT the YN slot index
**Status:** IDENTIFIED AND DOCUMENTED
**Date:** 2026-06-30 (Pass 431)
**Keywords:** yn_table.txt, YN slot, BKYS_YN_N, BKYSMSTR, T7YSYN, pool order, ISTS.CFG, WOCALC, SCRCMP, BKROA.SRC

## Symptom
Scratchpad file `yn_table.txt` was generated in Pass 429 using T7YSYN's ISTS.CFG variable symbol pool ORDER (0=PASSWD, 1=CFGLVL, …, 68=WOCALC, 80=LNGWT) as the "YN Slot" column. The table header says "YN Slot | ISTS.CFG Key | Live Value" but the slot numbers are actually the pool order (1-indexed from 0), NOT the actual BKYS_YN_N field positions.

## Root Cause
T7YSYN's variable symbol table lists ISTS.CFG keys in editor-UI/screen order, NOT in the order they appear as BKYS_YN_N subscripts. The key WOCALC happens to be at variable table position 131+68=199 (pool order 68) but it edits BKYS_YN_38 (field position 38 in BKYSMSTR). These two orderings are completely different.

**Evidence for the mistake:** BKROA.SRC line 392 confirms `bkys.yn[38]` = WOCALC. But yn_table.txt shows WOCALC at row 69 (pool order 68+1=69) and SCRCMP at row 38. These contradict each other — pool-order 37 maps to SCRCMP, but SRC says YN[38]=WOCALC.

## Attempts
None applied — this is a documentation/analysis mistake, not a code bug.

**What NOT to retry:** Do NOT assume pool[N] = YN[N+1]. Do NOT use yn_table.txt as a mapping table between ISTS.CFG keys and YN slot indices.

## Resolution / Lesson
**Correct mapping source:** Only BKROA.SRC / BKDCA.SRC / other .SRC files, DFM control bindings, or successful T7YSYN bytecode expression tree parsing can give the true mapping. DFM analysis yielded 88 confirmed slots (T7MDefaults.DFM + T7MDefNDC.DFM). 162 slots unknown.

A scratchpad file labeled "YN Slot" may reflect the analysis script's loop counter, not the actual database field position. Always cross-check against SRC-confirmed values before trusting a generated mapping table.
