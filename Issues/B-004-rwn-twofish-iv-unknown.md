# B-004: .RWN Twofish CFB initial IV (block_buf) unknown — decryption incomplete
**Status:** FIXED — 2026-06-15
**Date:** 2026-06-12
**Keywords:** RWN, Twofish, CFB, IV, block_buf, initial IV, K0, P_initial, validate_func, SHA1, mabufoju, K_B, Frida, EncryptBlock, get_iv_frida.py, iv_bytes.bin

## Symptom
Attempting to decrypt the first 8 bytes of a `.RWN` file to validate the passphrase (pt[0:4] == pt[4:8] check in validate_func). All tried IV values produce the wrong keystream XOR. Required: `ct[0:4] ^ ct[4:8] == 0x3E0A37C5` (constant across all .RWN files). With IV=zeros and key=SHA1('mabufoju')+4zeros (192-bit), computed XOR is `0xCE14BE8C` — wrong.

## Root Cause
The TDCP_blockcipher constructor (file 0x34E230 in tp7runtime.exe) allocates `block_buf` (cipher+0x3C, 16 bytes) via GetMem but **does not initialize it to zero** or any specific value. In validate_func, the cipher is used immediately in CFB mode (mode=2, set at cipher+0x34) without any SetIV/Reset call between Init and the first Encrypt. Whatever bytes happen to be in block_buf at that moment become the effective IV.

Because tp7runtime.exe starts with many Delphi runtime allocations before validate_func runs, the block_buf memory is NOT clean zero memory; it contains whatever was last written to that heap address by an earlier free.

**Confirmed facts (all verified by disassembly):**
- Note: "mabufoju" passphrase claim was WRONG (see B-007) — actual key = K_B (live Frida capture)
- Hash: SHA1 — `TDCP_sha1` class name confirmed via VMT at file 0x34BAE4
- 192-bit key: SHA1 digest (20 bytes) + 4 zero bytes
- Mode: CFB (mode=2 written to cipher+0x34 in validate_func)
- Block size: 16 bytes (Twofish standard)
- Q-box tables match NIST Twofish spec exactly
- `twofish_pure.py` passes NIST 192-bit test vector
- All .RWN files produce constant `ct[0:4]^ct[4:8] = 0x3E0A37C5` (scanned 20+ files)

## Attempts

| Date | Attempt | XOR result | Notes |
|------|---------|-----------|-------|
| 2026-06-12 | IV=zeros, SHA1 key 192-bit | 0xCE14BE8C | Main candidate — WRONG |
| 2026-06-12 | IV=zeros, SHA1 key 128-bit | different | Wrong |
| 2026-06-12 | IV=zeros, SHA1 key 256-bit | different | Wrong |
| 2026-06-12 | IV=zeros, MD5/SHA256 keys, all lengths | all wrong | Wrong passphrase |
| 2026-06-12 | IV=file[0:16], all key variants | all wrong | IV is not first 8 bytes |
| 2026-06-12 | SHA1/MD5/SHA256 × 128/192/256-bit × IV combos | none match | Exhaustive brute-force |
| 2026-06-15 | get_iv_frida.py v5 (EncryptBlock hook + XOR filter) | K0[0:4]^K0[4:8] = 0x3E0A37C5 PASS | WORKS |

**Do NOT retry** the IV=zeros + SHA1-192 combination — it gives 0xCE14BE8C and the NIST test confirms twofish_pure.py is correct, so the implementation is not the problem.

## Resolution / Lesson
**RESOLUTION (2026-06-15):** IV captured via `get_iv_frida.py` v5 (EncryptBlock hook + XOR filter). User opened Work Orders module (WO-A) from the EVO main menu.

    K0 = 8d eb 94 90 48 dc 9e ae 9f df 17 79 cd c8 b5 51
    K0[0:4]^K0[4:8] = 0x3E0A37C5  PASS

Validation against 20 .RWN files: all pass pt[0:4]==pt[4:8]. Full batch decrypt (1,124 files): saved to scripts/iv_bytes.bin.

**CORRECTION (2026-06-16):** The original `IV = 9cda...` was WRONG — computed as Decrypt_K_wrong(K0) using sha1("mabufoju")+4zeros (the wrong key). Correct approach: P_initial = Encrypt_K_B(zeros) is fully deterministic from K_B; no external IV file is needed at all. `scripts/iv_bytes.bin` is obsolete.

DCPcrypt's `TDCP_blockcipher` base class sets P = Encrypt_K(zeros) when IV param = 0. No IV capture needed — P_initial is fully deterministic once the key is known. Capture the key (not the IV) via Frida.
