# `.RWN` / `.DCY` Decryption — Research Findings

Status: **FULLY SOLVED 2026-06-16**

Last updated: 2026-06-16

---

## FINAL CONFIRMED CIPHER PARAMETERS

All confirmed via live Frida capture (`frida_capture_key_and_iv.py`) + Python decryption test.

### Algorithm
- **Cipher**: Twofish, 128-bit block, **192-bit key**, **CFB-128 mode**
- **Key derivation**: `SHA1(runtime_passphrase)[0:20]` + `\x00\x00\x00\x00` = 24 bytes
- **IV parameter to SetKey**: always 0 → P_initial = Encrypt_K(all-zeros)
- **key_bits (ECX at SetKey entry)**: 160 (= SHA1 output length in bits; padded to 192 with 4 zeros)

### Keys (live-captured 2026-06-16)

| Key name | Raw 20-byte hex | Used for |
|----------|----------------|---------|
| K_B | `a898d21e2fd6ca294026e5d633d9047f91f7ed35` | **.RWN** files |
| K_D | `691e8041ab265b4e6ee052ccc946dba4caac60da` | **.DCY** files |
| K_A | `d97f05679438037073c30628734764020859f77e` | unknown (appears at EVO startup) |
| K_C | `fdc2883f6d6537dd667270406d0a4c85969295ac` | unknown |

192-bit key = raw key + `\x00\x00\x00\x00`.

**The passphrase "mabufoju" was WRONG.** That was a static string found near the cipher code but is NOT the runtime passphrase. The runtime passphrase is in a BSS global initialized at startup; its plaintext has not been recovered. The raw key bytes above are sufficient for decryption.

### DCY cipher parameters (fully confirmed)

```
K_D_192     = 691e8041ab265b4e6ee052ccc946dba4caac60da00000000
P_initial   = Encrypt(K_D_192, zeros)  = 83fcde64a3f87b20076b10a9a4fc8a7f
K0          = Encrypt(K_D_192, P_init) = ab3c1a7a2fe04f7322f10dfda5ea3636
```

Validation (K0 XOR constant, little-endian le32):
`le32(K0, 0) XOR le32(K0, 4)` = `0x7A1A3CAB XOR 0x734FE02F` = **0x0955DC84** ✓

### RWN cipher parameters (fully confirmed)

```
K_B_192     = a898d21e2fd6ca294026e5d633d9047f91f7ed35 00000000
P_initial   = Encrypt(K_B_192, zeros)  = 0e6fbff653a28a70d102874c6b1825ad  (= IV_rwn)
K0          = Encrypt(K_B_192, P_init) = 8deb949048dc9eae9fdf1779cdc8b551
```

---

## File structure and decryption algorithm

### File layout (same for .RWN and .DCY)

```
Byte 0-7:   Validation header (8 bytes ciphertext)
Byte 8+:    Body (N bytes ciphertext)
```

### Decryption algorithm

```python
from twofish_pure import Twofish

def decrypt_evo_file(raw_bytes, key_raw_20):
    key_192 = key_raw_20 + b'\x00' * 4
    tf = Twofish(key_192)
    P_init = tf.encrypt(bytes(16))       # P_initial
    K0     = tf.encrypt(P_init)          # header keystream

    # Validate header
    header_ct = raw_bytes[0:8]
    header_pt = bytes(a ^ b for a, b in zip(header_ct, K0[:8]))
    assert header_pt[0:4] == header_pt[4:8], "Validation failed"

    # Decrypt body — CRITICAL: P starts at K0, NOT P_initial
    P      = K0
    body   = raw_bytes[8:]
    result = bytearray()
    for i in range(0, len(body), 16):
        blk = body[i:i+16]
        K   = tf.encrypt(P)
        result.extend(a ^ b for a, b in zip(blk, K))
        if len(blk) == 16:
            P = blk          # CFB-128: feedback = ciphertext block
    return bytes(result)

# Decrypt DCY file:
raw = open('SOMEFILE.DCY', 'rb').read()
K_D = bytes.fromhex('691e8041ab265b4e6ee052ccc946dba4caac60da')
plaintext = decrypt_evo_file(raw, K_D)

# Decrypt RWN file:
K_B = bytes.fromhex('a898d21e2fd6ca294026e5d633d9047f91f7ed35')
plaintext = decrypt_evo_file(raw_rwn, K_B)
```

### Critical detail — body P_start = K0 (assembly-confirmed 2026-06-16)

**Mechanism (from `mode2_handler` disassembly, file 0x34DF50):**

DCPcrypt's CFB mode has two separate code paths depending on block completeness:

- **Full 16-byte block** (body): after XOR, executes `Move(CT[0:16] → block_buf)` — CFB feedback update.
- **Partial block** (8-byte validation header): `EncryptBlock(P_initial → K0)` runs, then XOR, but **no** `Move(CT → block_buf)` is executed.

Relevant assembly (partial-block path, `0x74EBF6`–`0x74EC27`):
```
0x74EBF6  mov eax, [ebx+0x3c]  ; block_buf ptr (P_initial on first call)
0x74EC01  call [esi+0x58]       ; EncryptBlock(P in-place) → block_buf = K0
0x74EC13  call 0x403544         ; Move(CT[0:8] → output[0:8])
0x74EC27  call 0x74f18c         ; XorBuf(output[0:8] ^= K0[0:8], 8)
                                 ; <- NO Move(CT → block_buf) here
```

Full-block path (body loop, `0x74EBD1`):
```
0x74EBD1  call 0x403544         ; Move(CT[0:16] → block_buf) <- feedback update ONLY for full blocks
```

**Result:** After the 8-byte partial validation block, `block_buf = K0`. No code resets or re-arms it.
When `body_load` (0x74E374) calls `mode2_handler` for the body chunks, the same cipher object
is used with `block_buf` still = K0. So body block 1 keystream = `Encrypt(K0)`.

This is standard DCPcrypt partial-block CFB behavior, not a special re-arming. Confidence: **100/100**.

---

## Validation constants

The 8-byte validation header serves as an integrity/key check. Plaintext passes when:
- `header_pt[0:4] == header_pt[4:8]`  (first word equals second word)

The EncryptBlock XOR filter used in Frida capture scripts:
- `.RWN` files: `le32(K0, 0) XOR le32(K0, 4) = 0x3E0A37C5`  
- `.DCY` files: `le32(K0, 0) XOR le32(K0, 4) = 0x0955DC84`

These constants are derived from K0 (which is fixed for a given key), not from the file content.

---

## Verification results (2026-06-16)

| Test | Result |
|------|--------|
| K_D decrypts MDUMMY.DCY validation | `d484de56 d484de56` (equal) ✓ |
| K_D decrypts MDUMMY.DCY body | `object EditForm1: TEditForm1\r\nLeft=0\r\nHint='C:\taspro7\DBA7\mDummy.DFM'...` ✓ |
| K_B `Encrypt(zeros)` = IV_rwn | `0e6fbff653a28a70d102874c6b1825ad` ✓ |
| key_bits (live capture) | 160 for all SetKey calls ✓ |
| IV param (live capture) | 0x00000000 for all SetKey calls ✓ |

---

## What is NOT yet known

- The plaintext passphrase(s) behind K_A, K_B, K_C, K_D — not needed for decryption
- What K_A and K_C are used for (appeared during EVO startup/login, not during module loads)
- Whether different file types (.RUN, old-gen) use the same cipher

---

## How B-007 was solved (2026-06-16)

Prior analysis used sha1("mabufoju") which was WRONG. Fixed by:
1. Running `frida_capture_key_and_iv.py` (dynamic address resolution via `mod.base.add(RVA)`)
2. Observing key_bits=160, live key bytes ≠ sha1("mabufoju")
3. Testing all 4 live-captured keys against MDUMMY.DCY → K_D validates ✓
4. Discovering body P_start = K0 by computing `Decrypt_KD(emp_ks0) = K0`

See BROKEN.md B-007 for full attempt history.

---

## Dead ends (do not retry)

- sha1("mabufoju") as passphrase — WRONG key, confirmed 2026-06-16
- IV_dcy = `cd47af18...` — was derived with wrong key, invalid
- P_initial as body P_start — wrong; body starts at P = K0
- CFB-64 / CFB-8 / OFB variants — wrong mode; standard CFB-128 confirmed
- All attempts in BROKEN.md B-007 table (11 failed attempts, 2026-06-15)
