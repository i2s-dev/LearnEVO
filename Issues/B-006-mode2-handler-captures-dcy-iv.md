# B-006: mode2_handler hook captures DCY IV (sub-screen sub-menu loads .DCY, not .RWN)
**Status:** FIXED — v5 EncryptBlock hook with XOR filter captures RWN IV correctly; user opened WO-A from main menu; IV confirmed 2026-06-15
**Date:** 2026-06-15
**Keywords:** mode2_handler, Frida, DCY, RWN, IV, XOR filter, EncryptBlock, WO-A, sub-menu, sub-screen, block_buf, pointer, heap, get_iv_frida.py

## Symptom
mode2_handler hook (in evoerp.exe PID 30360) fired when user opened the Work Orders search sub-menu within WO-A. The captured block_buf deref = `0e 6f bf f6 53 a2 8a 70 d1 02 87 4c 6b 18 25 ad`. `Encrypt(deref)` gives XOR = 0x2F803AA0, not 0x3E0A37C5. Script reported IV_NOT_VALID.

## Root Cause
mode2_handler is called for BOTH .RWN (module programs) and .DCY (data dictionaries). The Work Orders "search menu" within WO-A does NOT open a new module — it opens a data-dictionary-driven sub-screen which loads a .DCY file. .DCY files use a different IV than .RWN (proven by MDUMMY.DCY XOR = 0x09553584 ≠ 0x3E0A37C5 — see B-005). The captured deref is IV_dcy, not IV_rwn.

Additionally: disassembly of mode2_handler confirmed that cipher+0x3C is a **pointer** to the heap-allocated block_buf (Delphi dynamic array pointer), NOT an inline array. `MOV EAX, [EBX+0x3C]` at mode2_handler byte 166 loads the pointer; EncryptBlock is called with that pointer as both src and dst (in-place encryption). The direct bytes at cipher+0x3C = `78 28 e0 05 ...` (0x05E02878 is a heap address, not IV bytes). BROKEN.md B-005 incorrectly stated "16-byte INLINE array" — that was wrong.

## Attempts

| Date | Attempt | Outcome |
|------|---------|---------|
| 2026-06-15 | Hook mode2_handler in evoerp.exe; user opens WO sub-screen | Fires for .DCY load; IV_dcy fails XOR check |
| 2026-06-15 | Treat direct bytes cipher+0x3C as IV (without deref) | Garbage (heap pointer bytes), not IV |
| 2026-06-15 | Deref cipher+0x3C, test Encrypt/Decrypt/Decrypt^2 variants | All fail XOR = 0x3E0A37C5 |
| 2026-06-15 | v5 EncryptBlock hook (RVA 0x350248) with XOR filter 0x3E0A37C5 | WORKS — filters out DCY loads; only RWN validation matches |

## Resolution / Lesson
**Current fix: v5 EncryptBlock hook with XOR filter**

`get_iv_frida.py` (v5) hooks **EncryptBlock** (RVA 0x350248). At onEnter saves EDX (the block_buf pointer). At onLeave reads K = *EDX = output of Encrypt(block_buf). Checks K[0:4]^K[4:8] == 0x3E0A37C5. Only .RWN validation decrypts satisfy this; .DCY body blocks do not. If match: IV = Decrypt(K) computed in Python. Self-verifying.

**User action for v5:** Open a MODULE from the EVO main menu (not a sub-menu within an open module). Opening Work Orders from the main menu loads T7WOA.RWN; that's what fires EncryptBlock with IV_rwn. Sub-screens within WO-A load .DCY — the hook ignores those (wrong XOR).

"Open the Work Orders menu" is ambiguous. If WO-A is already open and the user navigates its sub-menus, those load .DCY files. The IV must be captured from a MODULE-LEVEL .RWN load, not from sub-screen navigation.
