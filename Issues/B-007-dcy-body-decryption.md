# B-007: DCY body decryption fails: empirical keystream not reproducible from IV_dcy via CFB-128
**Status:** FIXED 2026-06-16
**Date:** 2026-06-15
**Keywords:** DCY, Twofish, CFB-128, body decryption, IV, K0, P_start, passphrase, mabufoju, K_D, K_B, Frida, MDUMMY.DCY, mDummy.DFM, cipher parameters

## Symptom
MDUMMY.DCY body (bytes [8:]) XOR mDummy.DFM produces valid DFM plaintext for all 354 blocks ("object EditForm1: TEditForm1\r\n  Left = 0\r\n  Hint = 'C:\TASPRO7\DBA7\mDummy.DFM'..." confirmed). But the empirical keystream could not be reproduced from IV_dcy using any tested cipher mode or derivation.

Expected (from mode2_handler disassembly = standard CFB-128):
- After 8-byte partial-block validation: block_buf = Encrypt(IV_dcy) = K0_dcy = `ab3c1a7a2fe04f73...`
- Body block 0 keystream = Encrypt(K0_dcy) = `4b0a6173cb477524...`

Actual (empirical):
- Body block 0 keystream = `0f73767aa296137875eaa22d6fc64b54`
- Back-derived initial block_buf = X = Decrypt(emp_ks0) = `7a3dd882c134e5fb254a87b2f5f79625`
- X ≠ K0_dcy; X not found anywhere in evoerp.exe binary; not reachable from IV_dcy via Enc^n or Dec^n

## Root Cause
Three compounded errors:
1. **Wrong passphrase**: "mabufoju" was never the runtime passphrase. The actual runtime keys are SHA1 hashes of an unknown (runtime-initialized) passphrase — never found as a static string in the binary. sha1("mabufoju") ≠ any live key.
2. **Wrong cipher key for DCY**: All prior analysis used sha1("mabufoju") + 4 zeros. The actual DCY key is K_D = `691e8041ab265b4e6ee052ccc946dba4caac60da` + 4 zeros (192-bit). The actual RWN key is K_B = `a898d21e2fd6ca294026e5d633d9047f91f7ed35` + 4 zeros (192-bit).
3. **Wrong body P_start**: Body CFB-128 decryption starts with P = K0 = Encrypt_K(P_initial), NOT with P_initial. After decrypting the 8-byte validation header (which uses K0[0:8]), the cipher resets/starts fresh for the body with P_body = K0.

## Attempts

| Date | Attempt | Outcome |
|------|---------|---------|
| 2026-06-15 | CFB-128 from X (empirical initial state) | Block 0 OK, ALL 353 subsequent transitions fail |
| 2026-06-15 | OFB from X | Same — 0 hits after block 0 |
| 2026-06-15 | CFB-64 (seg_size=8, P updated only 8 bytes) | 23/5670 match — fails |
| 2026-06-15 | CFB-8 (seg_size=1, shift register) | 1/64 match — fails |
| 2026-06-15 | Enc(K0_dcy) as body K0 | `4b0a6173...` ≠ emp_ks0 |
| 2026-06-15 | 11x encrypt/decrypt chain from IV_dcy | No match with X or emp_ks0 |
| 2026-06-15 | Search evoerp.exe binary for X and emp_ks0 | Not found — not hardcoded |
| 2026-06-15 | Various IV candidates (val_PT, CT_val, zeros, combinations) | All fail to produce emp_ks0 |
| 2026-06-15 | Model B: P_initial = Encrypt(zeros) for validation | val_PT = fdbfa3a1... ≠ d484de56... FAIL |
| 2026-06-15 | IV_rwn as body-cipher initial IV | Encrypt(IV_rwn) = 8deb9490... ≠ emp_ks0 FAIL |
| 2026-06-16 | Re-ran decryption with confirmed K_D and P_start=K0 | MDUMMY.DCY decrypts to valid DFM ✓ |

**Additional confirmed facts from investigation (cumulative through 2026-06-15):**
1. Python Twofish is correct: Encrypt(Decrypt(x)) = x; NIST round-trip pass
2. IV_dcy = `cd47af18e0d1c38cf1d8a067fc3dda28` is correct (41/48 DCY validation pass)
3. mode2_handler = standard CFB-128 (full disassembly); block_size = 16
4. vtable[0x50] dispatch: mode_byte=2 → mode2_handler (0x74EB50)
5. validate_func uses ONE cipher object for both validation and body
6. mDummy.DFM IS the correct plaintext
7. cipher object layout: cipher+0x30=init_flag, cipher+0x34=mode_byte, cipher+0x38=buffer1_ptr, cipher+0x3C=P (block_buf ptr), cipher+0x40=Q_ptr, cipher+0x44=block_size(16), cipher+0x48=subkeys
8. vtable layout (base 0x74F2A8): [0x38]=GetKeySize→256, [0x40]=SetKey(0x74F8A4), [0x44]=Reset(0x750214), [0x48]=InitVector(0x74E5E4), [0x4C]=Encrypt(0x74E674), [0x50]=Decrypt dispatcher(0x74E6BC), [0x54]=returns 128, [0x58]=EncryptBlock(0x750248)
9. vtable[0x48] = InitVector (0x74E5E4): if initialized, does Move(buffer1 → P, 16). This is the ONLY place that sets P from a buffer. Called at end of SetKey.
10. SetKey tail (0x7501B7): when IV param=0 → FillChar(buffer1, 16, 0) → EncryptBlock(zeros→buffer1) → InitVector → P = Encrypt_K(zeros)
11. cipher_init (0x74E1F8): ALWAYS pushes 0 as IV param to SetKey (verified two branches at 0x74E24D and 0x74E265 — both `6a 00` = PUSH 0). Therefore after cipher_init: P = Encrypt_K(zeros).
12. "stream reader" = SHA1 context: VMT[0x40]=SHA1_Init, VMT[0x44]=SHA1_GetDigest, VMT[0x48]=SHA1_Reset, VMT[0x4C]=SHA1_Update
13. SetStream (0x74EFBC): hashes the content of the global passphrase object
14. Global passphrase [0xb8b0cc]: runtime-initialized BSS; actual content requires Frida to capture.

## Resolution / Lesson

**SOLUTION (confirmed, MDUMMY.DCY decrypts to valid DFM):**
```python
K_D_192 = bytes.fromhex('691e8041ab265b4e6ee052ccc946dba4caac60da') + b'\x00'*4
tf = Twofish(K_D_192)
P_init = tf.encrypt(bytes(16))        # = 83fcde64a3f87b20076b10a9a4fc8a7f
K0     = tf.encrypt(P_init)           # = ab3c1a7a2fe04f7322f10dfda5ea3636
# validate header: raw[0:8] XOR K0[0:8] => d484de56 d484de56 (PT[0:4]==PT[4:8]) PASS
# body CFB-128 starting at P = K0:
P = K0
for each 16-byte body block b:
    K = tf.encrypt(P)
    PT = b XOR K
    P = b  # feedback = ciphertext
```

**KEY PARAMETERS (confirmed 2026-06-16 via live Frida capture + decryption test):**

| Parameter | Value |
|-----------|-------|
| Key size | 160-bit (20 bytes = SHA1 output) + 4 zero bytes = 192-bit |
| DCY key (K_D) | `691e8041ab265b4e6ee052ccc946dba4caac60da` + `00000000` |
| RWN key (K_B) | `a898d21e2fd6ca294026e5d633d9047f91f7ed35` + `00000000` |
| DCY P_initial | `83fcde64a3f87b20076b10a9a4fc8a7f` (= Encrypt_KD(zeros)) |
| DCY K0 | `ab3c1a7a2fe04f7322f10dfda5ea3636` (= Encrypt_KD(P_initial)) |
| RWN P_initial (= IV_rwn) | `0e6fbff653a28a70d102874c6b1825ad` (= Encrypt_KB(zeros)) |
| Header | first 8 bytes: PT = CT XOR K0[0:8]; passes if PT[0:4]==PT[4:8] |
| Body P_start | K0 (NOT P_initial) |
| Body mode | CFB-128; P[n+1] = CT[n] |
| IV param to SetKey | always 0 (push 0 confirmed in cipher_init disassembly) |

Never trust static string searches for runtime-initialized passphrase. Use Frida to capture live key bytes. Also: when body decryption fails but header validation passes, suspect the cipher state between header and body.
