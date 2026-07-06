# B-019: WO-G KIT=Y freeze on 54552-1: BKICMSTR record lock
**Status:** ACTIVE — lock contention, not a code bug
**Date:** 2026-06-29
**Keywords:** WO-G, KIT=Y, BKICMSTR, record lock, Btrieve, Pervasive, stale lock, 54552-1, force-kill, orphaned session

## Symptom
User tried KIT=Y (issue all) for WO 54552-1 as a workaround for the KIT=L freeze (B-018). EVO appeared to freeze (hung silently), then produced this dialog:
> "The record in file: BKICMSTR is locked by another user.
>  Do you wish to try again? (If you enter N the program will terminate.) Y"

This is a SEPARATE issue from B-018. KIT=Y bypasses T7WOG4 entirely — no REMAINING=0 path. Instead, T7WOG attempts to update BKICMSTR (Inventory Item Master) for one or more of the components being issued, and finds the record locked by another session.

## Root Cause
Btrieve record-level lock on a BKICMSTR record for one of 54552-1's components. Possible sources:
1. Another EVO user is currently in WO-G, IN, PO, or any module that locks the same item
2. Stale Pervasive lock from a crashed/force-killed EVO session (prior KIT=L attempt?)
3. The prior KIT=L freeze (which required force-killing EVO) may have left a lock orphan

**STATUS='R' note:** 54552-1 shows WORKORD STATUS='R' (Completed, COMQTY=375). Attempting to issue material to a completed WO may trigger unusual code paths in T7WOG — worth checking whether the issue is expected to work on an 'R'-status WO at all.

## Attempts
1. None yet — user clicked out of the dialog (click "No" to terminate safely; "Yes" retries indefinitely until lock releases).

**Recommended next steps:**
1. Ask other users if anyone is currently in a module that accesses the same item numbers (especially 055-53829-0M40K and nearby SMT parts)
2. If no live user has the lock → stale lock from the prior force-kill. Admin action needed: Pervasive PSQL Monitor (`pvsw.exe` or Zen Control Center) → Connected Users → find and disconnect the orphaned session. Or restart the Btrieve engine on \\i2s109-solidcrm.
3. If STATUS='R' is the issue, the WO may need to be re-opened (status change) before issuing remaining components.

## Resolution / Lesson
Force-killing EvoERP (required workaround for KIT=L freeze) may leave orphaned Btrieve record locks. Clear stale sessions via Pervasive admin tools after any force-kill.
