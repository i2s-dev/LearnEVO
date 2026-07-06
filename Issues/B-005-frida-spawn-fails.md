# B-005: Frida spawn approach fails; DCY/RWN use different IVs (dead-end analytical path)
**Status:** SUPERSEDED — IV confirmed via v5 approach; DCY still needs its own IV (XOR=0x09553584)
**Date:** 2026-06-15
**Keywords:** Frida, spawn, tp7runtime, single-instance check, DCY, RWN, IV, different IVs, child gating, XOR constraint, MDUMMY.DCY, mDummy.DFM

## Symptom
All Frida-based attempts to capture block_buf via spawning tp7runtime.exe with suwin7.rwn failed: Twofish constructor fired 3 times but mode2_handler (file 0x34DF50) never fired. Separately, all analytical IV derivation attempts from MDUMMY.DCY/mDummy.DFM produced IV candidates that failed both the XOR constraint (0x3E0A37C5) and the DCY/DFM plaintext check.

## Root Cause
1. **Spawned tp7runtime exits before RWN loading.** When spawning tp7runtime.exe with suwin7.rwn, the TAS Pro 7 runtime performs initialization (including creating internal cipher objects — explaining the 3x constructor fires) before it loads any .RWN file. During this init phase, a single-instance check detects the running evoerp.exe and exits the process. The RWN load (and hence mode2_handler) never happens.

2. **DCY and RWN files use DIFFERENT IVs.** Extensive analytical analysis proved:
   - MDUMMY.DCY validation constant: ct[0:4]^ct[4:8] = 0x09553584
   - All .RWN files validation constant: ct[0:4]^ct[4:8] = 0x3E0A37C5
   - 0x09553584 != 0x3E0A37C5 => DCY and RWN files were encrypted with different IVs
   - The empirical keystream from MDUMMY.DCY XOR mDummy.DFM is the .DCY IV keystream, completely unrelated to the .RWN IV.

## Attempts

| Date | Attempt | Outcome |
|------|---------|---------|
| 2026-06-15 | Frida spawn tp7runtime.exe + suwin7.rwn, hook mode2_handler | mode2_handler never fires |
| 2026-06-15 | Analytical: K1=DCY[16:32]^DFM[8:24]; K0=Decrypt(K1); IV=Decrypt(K0) | K0[8:16] contradiction |
| 2026-06-15 | Analytical: IV=Decrypt^2(empirical_ks1) | XOR = 0x793D09BB != 0x3E0A37C5 |
| 2026-06-15 | OFB alignment fix: decrypt full DCY from byte 0, body=pt[8:] | Still fails: DCY IV != RWN IV |
| 2026-06-15 | All OFB/CFB variants with correct block alignment | None satisfy both constraints |
| 2026-06-15 | v5 EncryptBlock hook with XOR filter (child gating not needed) | WORKS — see B-006 |

**Confirmed good facts from this investigation:**
- mode2_handler bytes confirmed correct at file 0x34DF50: 55 8b ec 83 c4 f4 53 56 57 (PUSH EBP; MOV EBP,ESP; ADD ESP,-12; PUSH EBX,ESI,EDI)
- RVA 0x34EB50 is verified as the correct hook point for both tp7runtime.exe and evoerp.exe
- block_buf is a **POINTER** at cipher+0x3C — cipher+0x3C stores a 4-byte heap pointer P; *P is the 16-byte IV. The "inline array" claim in an earlier session was WRONG (corrected in B-006)

## Resolution / Lesson
Never try to derive the RWN IV from DCY/DFM analysis — the two file types use different IVs. The ONLY path to the RWN IV is dynamic extraction (Frida child gating or x64dbg) while a real module .RWN is being loaded by a real tp7runtime.exe child process. The v5 EncryptBlock XOR-filter approach (B-006) succeeded without needing child gating.
