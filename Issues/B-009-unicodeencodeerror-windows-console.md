# B-009: UnicodeEncodeError in RWN analysis scripts on Windows console
**Status:** FIXED (Pass 110 — lesson only; scripts are scratchpad-only)
**Date:** 2026-06-19
**Keywords:** UnicodeEncodeError, cp1252, Windows console, Unicode arrows, print, PowerShell, cmd, rwn_decode_pool.py, rwn_varmap.py

## Symptom
`rwn_decode_pool.py` and `rwn_varmap.py` crashed with `UnicodeEncodeError: 'charmap' codec can't encode character '←'` (←) and `'→'` (→). The final summary sections of both scripts errored, though all critical data had already printed before the crash.

## Root Cause
Windows console default encoding is `cp1252`, which cannot encode Unicode arrows U+2190 (←) and U+2192 (→) used in print strings for display.

## Attempts
**Fix (worked):** Replace all Unicode special characters in print/f-string literals with plain-ASCII alternatives (`"<--"`, `"->"`, `"=>"`) in any script that runs in a Windows terminal.

## Resolution / Lesson
Windows `cmd`/PowerShell consoles default to `cp1252`. Never use Unicode arrows, boxes, or other non-ASCII characters in `print()` statements in analysis scripts.
