# BROKEN.md — Bug and Mistake Log

**ALWAYS READ THIS BEFORE DOING ANYTHING.**

Every bug attempted in this workspace is logged here: symptom, root cause, every attempt
(worked or not), and a lesson. Newest entries on top. Never retry a fix marked "didn't work"
without explicit reasoning for why a different outcome is expected now.

---

## Bug B-006 — mode2_handler hook captures DCY IV (sub-screen sub-menu loads .DCY, not .RWN)

**Date:** 2026-06-15
**Status:** 🔄 OPEN — root cause understood; v5 approach addresses it

**Symptom:**
mode2_handler hook (in evoerp.exe PID 30360) fired when user opened the Work Orders
search sub-menu within WO-A. The captured block_buf deref =
`0e 6f bf f6 53 a2 8a 70 d1 02 87 4c 6b 18 25 ad`.
`Encrypt(deref)` gives XOR = 0x2F803AA0, not 0x3E0A37C5. Script reported IV_NOT_VALID.

**Root cause:**
mode2_handler is called for BOTH .RWN (module programs) and .DCY (data dictionaries).
The Work Orders "search menu" within WO-A does NOT open a new module — it opens a
data-dictionary-driven sub-screen which loads a .DCY file. .DCY files use a different
IV than .RWN (proven by MDUMMY.DCY XOR = 0x09553584 ≠ 0x3E0A37C5 — see B-005).
The captured deref is IV_dcy, not IV_rwn.

Additionally: disassembly of mode2_handler confirmed that cipher+0x3C is a **pointer**
to the heap-allocated block_buf (Delphi dynamic array pointer), NOT an inline array.
`MOV EAX, [EBX+0x3C]` at mode2_handler byte 166 loads the pointer; EncryptBlock is
called with that pointer as both src and dst (in-place encryption). The direct bytes
at cipher+0x3C = `78 28 e0 05 ...` (0x05E02878 is a heap address, not IV bytes).
BROKEN.md B-005 incorrectly stated "16-byte INLINE array" — that was wrong.

**What was tried (all failed — DO NOT RETRY):**

| Date | Attempt | Outcome |
|------|---------|---------|
| 2026-06-15 | Hook mode2_handler in evoerp.exe; user opens WO sub-screen | Fires for .DCY load; IV_dcy fails XOR check |
| 2026-06-15 | Treat direct bytes cipher+0x3C as IV (without deref) | Garbage (heap pointer bytes), not IV |
| 2026-06-15 | Deref cipher+0x3C, test Encrypt/Decrypt/Decrypt^2 variants | All fail XOR = 0x3E0A37C5 |

**Current fix: v5 EncryptBlock hook with XOR filter**
`get_iv_frida.py` (v5) hooks **EncryptBlock** (RVA 0x350248). At onEnter saves EDX
(the block_buf pointer). At onLeave reads K = *EDX = output of Encrypt(block_buf).
Checks K[0:4]^K[4:8] == 0x3E0A37C5. Only .RWN validation decrypts satisfy this; .DCY
body blocks do not. If match: IV = Decrypt(K) computed in Python. Self-verifying.

**User action for v5:** Open a MODULE from the EVO main menu (not a sub-menu within
an open module). Opening Work Orders from the main menu loads T7WOA.RWN; that's what
fires EncryptBlock with IV_rwn. Sub-screens within WO-A load .DCY — the hook ignores
those (wrong XOR).

**Lesson:** "Open the Work Orders menu" is ambiguous. If WO-A is already open and the
user navigates its sub-menus, those load .DCY files. The IV must be captured from a
MODULE-LEVEL .RWN load, not from sub-screen navigation.

---

## Bug B-005 — Frida spawn approach fails; DCY/RWN use different IVs (dead-end analytical path)

**Date:** 2026-06-15
**Status:** 🔄 OPEN — resolved dead ends; child-gating approach now ready

**Symptom:**
All Frida-based attempts to capture block_buf via spawning tp7runtime.exe with suwin7.rwn
failed: Twofish constructor fired 3 times but mode2_handler (file 0x34DF50) never fired.
Separately, all analytical IV derivation attempts from MDUMMY.DCY/mDummy.DFM produced IV
candidates that failed both the XOR constraint (0x3E0A37C5) and the DCY/DFM plaintext check.

**Root causes identified:**

1. **Spawned tp7runtime exits before RWN loading.** When spawning tp7runtime.exe with
   suwin7.rwn, the TAS Pro 7 runtime performs initialization (including creating internal
   cipher objects — explaining the 3x constructor fires) before it loads any .RWN file.
   During this init phase, a single-instance check detects the running evoerp.exe and exits
   the process. The RWN load (and hence mode2_handler) never happens.
   - Confirmed by: no mode2_handler callback despite the constructor firing; user observed
     only a brief taskbar flash with no EVO window appearing.

2. **DCY and RWN files use DIFFERENT IVs.** Extensive analytical analysis proved:
   - MDUMMY.DCY validation constant: ct[0:4]^ct[4:8] = 0x09553584
   - All .RWN files validation constant: ct[0:4]^ct[4:8] = 0x3E0A37C5
   - 0x09553584 != 0x3E0A37C5 => Encrypt(IV_dcy)[0:4]^[4:8] != Encrypt(IV_rwn)[0:4]^[4:8]
   - => DCY and RWN files were encrypted with different IVs
   - The empirical keystream 0f73767aa29613787... from MDUMMY.DCY XOR mDummy.DFM is the
     .DCY IV keystream, completely unrelated to the .RWN IV.
   - All 4 analytical approaches tried (Decrypt(K1), Decrypt^2(empirical), OFB variations,
     candidate-search from T7INA.RWN) failed for the same fundamental reason.

**What was tried (all failed — DO NOT RETRY):**

| Date | Attempt | Outcome |
|------|---------|---------|
| 2026-06-15 | Frida spawn tp7runtime.exe + suwin7.rwn, hook mode2_handler | mode2_handler never fires |
| 2026-06-15 | Analytical: K1=DCY[16:32]^DFM[8:24]; K0=Decrypt(K1); IV=Decrypt(K0) | K0[8:16] contradiction |
| 2026-06-15 | Analytical: IV=Decrypt^2(empirical_ks1) | XOR = 0x793D09BB != 0x3E0A37C5 |
| 2026-06-15 | OFB alignment fix: decrypt full DCY from byte 0, body=pt[8:] | Still fails: DCY IV != RWN IV |
| 2026-06-15 | All OFB/CFB variants with correct block alignment | None satisfy both constraints |

**Confirmed good facts from this investigation:**
- mode2_handler bytes confirmed correct at file 0x34DF50: 55 8b ec 83 c4 f4 53 56 57 (PUSH EBP; MOV EBP,ESP; ADD ESP,-12; PUSH EBX,ESI,EDI)
- RVA 0x34EB50 is verified as the correct hook point for both tp7runtime.exe and evoerp.exe
- block_buf is a **POINTER** at cipher+0x3C — cipher+0x3C stores a 4-byte heap pointer P; *P is the 16-byte IV. The "inline array" claim in an earlier session was WRONG (corrected in B-006)

**Current approach: child gating (not yet run)**
`get_iv_frida.py` (v3) now uses `session.enable_child_gating()` on the running evoerp.exe.
When the user closes and reopens a module window, evoerp.exe spawns a new tp7runtime.exe
child; Frida pauses it before any code runs, injects the hook, then resumes it.
This bypasses the single-instance check because the process is spawned BY evoerp.exe in the
normal way (evoerp.exe being the "instance" that already owns the session).

**Lesson:** Never try to derive the RWN IV from DCY/DFM analysis — the two file types use
different IVs. The ONLY path to the RWN IV is dynamic extraction (Frida child gating or
x64dbg) while a real module .RWN is being loaded by a real tp7runtime.exe child process.

---

## Bug B-004 — .RWN Twofish CFB initial IV (block_buf) unknown — decryption incomplete

**Date:** 2026-06-12
**Status:** ✅ FIXED — 2026-06-15

**Symptom:**
Attempting to decrypt the first 8 bytes of a `.RWN` file to validate the passphrase
(pt[0:4] == pt[4:8] check in validate_func). All tried IV values produce the wrong
keystream XOR. Required: `ct[0:4] ^ ct[4:8] == 0x3E0A37C5` (constant across all .RWN
files). With IV=zeros and key=SHA1('mabufoju')+4zeros (192-bit), computed XOR is
`0xCE14BE8C` — wrong.

**Root cause (current understanding):**
The TDCP_blockcipher constructor (file 0x34E230 in tp7runtime.exe) allocates `block_buf`
(cipher+0x3C, 16 bytes) via GetMem but **does not initialize it to zero** or any specific
value. The traced call chain through `InitStr_internal` → `TDCP_cipher.Init` → `Twofish.Init`
**never touches block_buf**. `TDCP_cipher.Init` only sets the `initialized` flag at
cipher+0x30. `Twofish.Init` does the key schedule and calls `FillChar` only on a local
32-byte stack buffer — not on block_buf.

In validate_func, the cipher is used immediately in CFB mode (mode=2, set at cipher+0x34)
without any SetIV/Reset call between Init and the first Encrypt. The first call to
`mode2_handler` (file 0x34DF50) calls `EncryptBlock(block_buf)` → XORs with the 8 plaintext
bytes. Whatever bytes happen to be in block_buf at that moment become the effective IV.

Because tp7runtime.exe starts with many Delphi runtime allocations before validate_func
runs, the block_buf memory is NOT the clean first-page-from-OS zero memory; it contains
whatever was last written to that heap address by an earlier free.

**Confirmed facts (all verified by disassembly):**
- Passphrase: `'mabufoju'` — hardcoded at file 0x75D154 / VA 0xB5DD54 ✓
- Hash: SHA1 — `TDCP_sha1` class name confirmed via VMT at file 0x34BAE4 ✓
- 192-bit key: SHA1 digest (20 bytes) + 4 zero bytes ✓
- Mode: CFB (mode=2 written to cipher+0x34 in validate_func) ✓
- Block size: 16 bytes (Twofish standard) ✓
- Q-box tables match NIST Twofish spec exactly ✓
- `twofish_pure.py` passes NIST 192-bit test vector ✓
- All .RWN files produce constant `ct[0:4]^ct[4:8] = 0x3E0A37C5` (scanned 20+ files) ✓
- Different .RWN files have different first 8 bytes (pt[0:4] varies per-file, NOT a fixed
  magic; so keystream is computed from block_buf state, not a predictable plaintext) ✓

**What was tried (all failed):**

| Date | Attempt | XOR result | Notes |
|------|---------|-----------|-------|
| 2026-06-12 | IV=zeros, SHA1 key 192-bit | 0xCE14BE8C | Main candidate — WRONG |
| 2026-06-12 | IV=zeros, SHA1 key 128-bit | different | Wrong |
| 2026-06-12 | IV=zeros, SHA1 key 256-bit | different | Wrong |
| 2026-06-12 | IV=zeros, MD5/SHA256 keys, all lengths | all wrong | Wrong passphrase |
| 2026-06-12 | IV=file[0:16], all key variants | all wrong | IV is not first 8 bytes |
| 2026-06-12 | SHA1/MD5/SHA256 × 128/192/256-bit × IV combos | none match | Exhaustive brute-force |

**Do NOT retry** the IV=zeros + SHA1-192 combination — it gives 0xCE14BE8C and the NIST
test confirms twofish_pure.py is correct, so the implementation is not the problem.

**RESOLUTION (2026-06-15):**
IV captured via `get_iv_frida.py` v5 (EncryptBlock hook + XOR filter).
User opened Work Orders module (WO-A) from the EVO main menu.

    IV = 9c da c3 45 a5 f0 1c 2c 96 57 92 d9 0b 1a bc 1e
    K0 = Encrypt(IV) = 8d eb 94 90 48 dc 9e ae 9f df 17 79 cd c8 b5 51
    K0[0:4]^K0[4:8] = 0x3E0A37C5  PASS

Validation against 20 .RWN files: all pass pt[0:4]==pt[4:8]. ✓
Full batch decrypt (1,124 files): running. Saved to scripts/iv_bytes.bin.

**Lesson:** DCPcrypt's `TDCP_blockcipher` base class allows using a cipher in
streaming mode before any IV is explicitly set — block_buf is never zeroed by the
constructor or by `Init`. Any code relying on "IV defaults to zero" is wrong for this
implementation. The IV can only be captured at runtime (Frida onLeave EncryptBlock).

---

## Bug B-003 — Twofish decrypt test fails (swap in wrong position)

**Date:** 2026-06-12
**Status:** ✅ FIXED

**Symptom:**
`tf.decrypt(ct) == pt` assertion failed even after encrypt test was passing.

**Root cause:**
The "undo last swap" was placed BEFORE the 16-round loop in `decrypt()`, but it must be
placed AFTER. Reasoning:

- The encrypt writes ciphertext as `[c16, d16, a16, b16]` (after a final swap before output
  whitening). After undoing the output whitening, X = `[c16, d16, a16, b16]`.
- This matches the reference's `GET_INPUT` layout (A=c16, B=d16), so T0 and T1 for the
  first decrypt round (r=15) must be computed from X[0]=c16 and X[1]=d16 — no pre-loop
  swap needed.
- After all 16 decrypt rounds + in-loop swaps, the state is `[c0, d0, a0, b0]`.
- A single post-loop swap gives `[a0, b0, c0, d0]` = whitened plaintext, which undoes
  correctly with K[0..3].
- The old code pre-swapped to `[a16, b16, c16, d16]` before the loop, making every round
  compute T from wrong words.

**What was tried:**

| Date | Attempt | Outcome |
|------|---------|---------|
| 2026-06-12 | Pre-loop swap (wrong position) | FAILED — T0/T1 computed from wrong words |
| 2026-06-12 | Moved swap to post-loop | PASSES — `assert tf.decrypt(ct) == pt` ✓ |

**Lesson:** In a Feistel with explicit swap-at-end-of-round, the decrypt must start from the
raw undo-whitened state and mirror the encrypt's swap structure — including where the final
"undo the last swap" lives (after the loop, not before it).

---

## Bug B-002 — h() q-box ordering wrong for b[1] and b[3] in 128-bit key case

**Date:** 2026-06-12
**Status:** ✅ FIXED

**Symptom:**
After fixing the X[3] rotation, encrypt still produced `de60f86ea019d72f8cc3de9e21f503fb`
instead of `9f589f5cf6122c32b6bfec2f2ae8c35a`.

**Root cause:**
The q-box sequence for bytes b[1] and b[3] in `_h()` for the k=2 (128-bit) base case
was wrong:
- b[1]: had `q0[q1[q1[...]]]` but reference H12 macro says `q0[q0[q1[...]]]`
- b[3]: had `q0[q0[q1[...]]]` but reference H32 macro says `q0[q1[q1[...]]]`

Reference H macros (from twofish-0.3.0/twofish.c):
```c
#define H12( y, L )  MDS_table[1][q0[q1[y]^L[ 9]]^L[1]]
#define H32( y, L )  MDS_table[3][q1[q1[y]^L[11]]^L[3]]
```
MDS_table[1] internally applies q0; MDS_table[3] internally applies q1.
So b[1] inner-to-outer: q1 → q0 (XOR L1) → q0 (XOR L0) → MDS col1
   b[3] inner-to-outer: q1 → q1 (XOR L3) → q1 (XOR L2) wait...

H32: q1[q1[y]^L[11]]^L[3] — the outer q1 is inside MDS_table[3].
So the chain is: y → q1 → XOR(L[11]) → q1 → XOR(L[3]) → (MDS_table[3] applies q1 then multiplies).

The correction swapped b[1] and b[3] inner q-box ordering.

**What was tried:**

| Date | Attempt | Outcome |
|------|---------|---------|
| 2026-06-12 | Wrong q-box order in b[1] and b[3] | FAILED — wrong ciphertext |
| 2026-06-12 | Fixed to match H12/H32 reference macros | PASSES ✓ |

**Lesson:** Always cross-reference the H0x/H1x/H2x/H3x macros from the reference C source
rather than guessing the q-box ordering. The inner/outer distinction is subtle.

---

## Bug B-001 — Twofish encrypt test fails: X[3] rotation direction wrong

**Date:** 2026-06-12
**Status:** ✅ FIXED

**Symptom:**
`tf.encrypt(pt)` produced `6ccef8a75c0dc95da0303c045c999c5b` instead of
`9f589f5cf6122c32b6bfec2f2ae8c35a`.

**Root cause:**
Two rotation errors in the encrypt Feistel round:
1. `X[2]` was written as `_rol32(X[2] ^ F0, 31)` — should be `_ror32(X[2] ^ F0, 1)`.
2. `X[3]` was `_ror32(X[3], 1) ^ F1` — should be `_rol32(X[3], 1) ^ F1`.

Reference macro `ENCRYPT_RND`:
```c
C ^= T0+T1+xkey->K[8+2*(r)]; C = ROR32(C,1);
D = ROL32(D,1); D ^= T0+2*T1+xkey->K[8+2*(r)+1]
```

**What was tried:**

| Date | Attempt | Outcome |
|------|---------|---------|
| 2026-06-12 | ROR(31) on X[2], ROR on X[3] | FAILED |
| 2026-06-12 | ROR(1) on X[2], ROL(1) on X[3] (then XOR F1) | PASSES ✓ |

**Lesson:** Read the reference macro carefully. C is XOR-then-ROR; D is ROL-then-XOR. Order
matters.

---

## Known issues — RESOLVED (code is correct)

### RS encoding — FIXED

**Status:** ✅ FIXED — `_rs_mds_encode` in `scripts/twofish_pure.py` uses the correct
LFSR polynomial reduction (poly 0x14D) via `bx`/`bxx` reduction loop. The earlier
matrix-multiply version was replaced. Confirmed correct: NIST 192-bit test vector passes
with non-zero key `0123456789ABCDEFFEDCBA987654321000112233445566778`.

### Key schedule — FIXED

**Status:** ✅ FIXED — subkeys are generated from `M_e`/`M_o` (raw key byte groups),
NOT from `S_rev`. `S_rev` is used only for the g-function (MDS S-box lookup), which is
correct per the Twofish spec. The subkey-generation loop uses `_h(2*i*rho, M_e, k)` and
`_h((2*i+1)*rho, M_o, k)`, matching the reference. NIST test vector confirms correct output.
