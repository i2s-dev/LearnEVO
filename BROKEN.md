# BROKEN.md — Bug and Mistake Log

**ALWAYS READ THIS BEFORE DOING ANYTHING.**

Every bug attempted in this workspace is logged here: symptom, root cause, every attempt
(worked or not), and a lesson. Newest entries on top. Never retry a fix marked "didn't work"
without explicit reasoning for why a different outcome is expected now.

---

## Bug B-004 — .RWN Twofish CFB initial IV (block_buf) unknown — decryption incomplete

**Date:** 2026-06-12
**Status:** 🔄 OPEN — blocked; requires debugger observation

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

**Remaining path to resolution:**
The only known method is to **observe block_buf under a debugger** when tp7runtime.exe
reaches the first `EncryptBlock` call inside `mode2_handler` (file 0x34DF50):
- Set a breakpoint at file offset 0x34DF50 (+0 = entry of mode2_handler)
- Or at the `CALL EncryptBlock` instruction inside it
- Read EAX (= cipher pointer) → read [EAX+0x3C] (16 bytes) = the actual block_buf/IV

Alternative: instrument a DCPcrypt Twofish rebuild with the exact same initialization
sequence (no SetIV, no Reset) and observe what Delphi's memory manager leaves in the
buffer under the same conditions.

**Lesson:** DCPcrypt's `TDCP_blockcipher` base class design allows using a cipher in
streaming mode before any IV is explicitly set — block_buf is never zeroed by the
constructor or by `Init`. Any code relying on "IV defaults to zero" is wrong for this
implementation.

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
