# M-005: TA-R documented as QUERYEXECUTE; BKMENUSU.TXT confirms T7JSQL.RWN
**Status:** FIXED
**Date:** 2026-07-01 (Pass 494)
**Keywords:** TA-R, QUERYEXECUTE, T7JSQL, SQL Editor, menu codes, BKMENUSU, modules.py

## Symptom
modules.py TA section and scorecard stated TA-R = QUERYEXECUTE(26p, ISDRILL) ("Query Executor"). This is wrong.

## Root Cause
Pass 112 RWN pool scan apparently matched TA-R to QUERYEXECUTE without cross-checking against the actual menu DBF. QUERYEXECUTE is QU-F ("Query Executor") under the Queries menu, not TA-R.

## Attempts
**Fix (worked):** BKMENUSU.TXT (canonical menu DBF dump from 2004.1\Drill\) confirms:
- TA-R = "SQL Editor" = T7JSQL.RWN
- QU-F = "Query Executor" = queryexecute.rwn

modules.py TA section menu table replaced with BKMENUSU-confirmed entries.

## Resolution / Lesson
Always cross-reference RWN pool scan results against BKMENUSU.DBF before documenting menu code → program mappings. The pool scan identifies candidate programs but doesn't confirm which menu code calls them.
