# BROKEN.md — Issue Index

> Short summaries only. Full details are in `Issues/<id>-<slug>.md`.
> Read this index before every session. Only open an Issues/ file when a task touches a similar problem.
> Never retry a fix marked "didn't work" in an Issues/ file without explicit reasoning for a different outcome.

Last updated: 2026-07-08

---

## Active Issues

| ID | Summary | Keywords | File |
|----|---------|----------|------|
| B-019 | WO-G KIT=Y freeze on 54552-1: BKICMSTR record lock — likely stale lock left by prior force-kill; use Pervasive admin to clear orphaned session | WO-G, KIT=Y, BKICMSTR, record lock, stale Pervasive lock, 54552-1 | [Issues/B-019-wo-g-kit-y-bkicmstr-lock.md](Issues/B-019-wo-g-kit-y-bkicmstr-lock.md) |
| B-018 | WO-G KIT=L freeze for SMT work orders: WINPOS passes REMAINING=0 to T7WOG4 when first mandatory COMPCODE is fully issued; workaround is KIT=Y | WO-G, KIT=L, SMT, WOBOM_OPTION, WINPOS, T7WOG4, REMAINING=0, 75338, 75405, 54552 | [Issues/B-018-wo-g-kit-l-smt-freeze.md](Issues/B-018-wo-g-kit-l-smt-freeze.md) |

---

## Fixed / Resolved

| ID | Summary | Keywords | File |
|----|---------|----------|------|
| B-020 | Frida 05c value-match produced false-positive slot assignments for GLCTRL (YN[88]) and WHCTRL (YN[105]); company A vs F differential scans disprove both; APLANG (YN[201]) unverified; BKYSMSTR confirmed system-wide | Frida, 05c, 05d, GLCTRL, WHCTRL, APLANG, YN slot, false positive, differential, BKYSMSTR | [Issues/B-020-frida-false-positive-slots.md](Issues/B-020-frida-false-positive-slots.md) |
| M-005 | TA-R wrongly mapped to QUERYEXECUTE; BKMENUSU.TXT confirms TA-R = T7JSQL.RWN (SQL Editor), QU-F = queryexecute.rwn | TA-R, QUERYEXECUTE, T7JSQL, menu codes, BKMENUSU | [Issues/M-005-ta-r-documented-wrong.md](Issues/M-005-ta-r-documented-wrong.md) |
| M-004 | QC CAR status documented as 3-state (Open/Review/Closed); T7QCGA.DFM Items.Strings confirms 4-state (adds Failed) | QC, CAR, status codes, T7QCGA, Items.Strings | [Issues/M-004-qc-car-status-3-state-wrong.md](Issues/M-004-qc-car-status-3-state-wrong.md) |
| M-003 | yn_table.txt "YN Slot" column is T7YSYN pool order, NOT BKYS_YN_N field position; BKROA.SRC is the authoritative mapping source | YN slot, BKYS_YN_N, T7YSYN, pool order, ISTS.CFG, WOCALC | [Issues/M-003-yn-table-pool-order-wrong.md](Issues/M-003-yn-table-pool-order-wrong.md) |
| M-002 | suwin6.dcy wrongly claimed to decrypt to binary opcodes; re-decryption with correct cipher parameters yields Delphi VCL form (ISTech License dialog) | suwin6.dcy, DCY, stale binary, cipher parameters, TEditForm | [Issues/M-002-suwin6-binary-opcodes-wrong.md](Issues/M-002-suwin6-binary-opcodes-wrong.md) |
| B-017 | ISJAVA wrongly marked "NOT in DDF"; parse_ddf.py silently drops field names containing brackets; all 25 IS_JAVA_PARAM sub-fields confirmed in FIELD.DDF | ISJAVA, DDF, FIELD.DDF, IS_JAVA_PARAM, parse_ddf.py, brackets | [Issues/B-017-isjava-not-in-ddf-wrong.md](Issues/B-017-isjava-not-in-ddf-wrong.md) |
| B-010 | All samples/rwn_decrypted/*.dec bodies garbled from stale batch run with wrong cipher parameters; re-ran rwn_decrypt.py, 1145/1146 OK | rwn_decrypted, .dec files, garbled, stale, P_start, K0, check_dec.py | [Issues/B-010-rwn-decrypted-garbled-bodies.md](Issues/B-010-rwn-decrypted-garbled-bodies.md) |
| B-009 | UnicodeEncodeError on Windows console from Unicode arrows in print statements; fix: use plain-ASCII alternatives | UnicodeEncodeError, cp1252, Windows console, print, Unicode arrows | [Issues/B-009-unicodeencodeerror-windows-console.md](Issues/B-009-unicodeencodeerror-windows-console.md) |
| B-008 | T7USG.DFM and T7MAPDEPO.DFM wrongly called TImageList; both are full TEditForm1 forms with field bindings (ISTRIGRS, BKARDEP/ISARDEPL) | T7USG.DFM, T7MAPDEPO.DFM, TImageList, TEditForm1, DFM | [Issues/B-008-t7usg-t7mapdepo-wrong-timagelist.md](Issues/B-008-t7usg-t7mapdepo-wrong-timagelist.md) |
| B-007 | DCY body decryption fails: three compounded errors — wrong passphrase (not "mabufoju"), wrong key (K_D not sha1("mabufoju")), wrong body P_start (must be K0 not P_initial) | DCY, Twofish, CFB-128, K_D, K_B, P_start, K0, passphrase, mabufoju, Frida, MDUMMY.DCY | [Issues/B-007-dcy-body-decryption.md](Issues/B-007-dcy-body-decryption.md) |
| B-006 | mode2_handler hook fires for DCY loads (sub-menu), not RWN loads; fix: v5 EncryptBlock hook with XOR filter 0x3E0A37C5 self-selects only RWN validation | mode2_handler, Frida, DCY, RWN, IV, XOR filter, EncryptBlock, block_buf, pointer | [Issues/B-006-mode2-handler-captures-dcy-iv.md](Issues/B-006-mode2-handler-captures-dcy-iv.md) |
| B-005 | Frida spawn approach fails (single-instance check exits tp7runtime before RWN load); DCY/RWN use different IVs — all analytical derivation paths are dead ends | Frida, spawn, tp7runtime, single-instance, DCY, RWN, different IVs, child gating | [Issues/B-005-frida-spawn-fails.md](Issues/B-005-frida-spawn-fails.md) |
| B-004 | RWN Twofish CFB initial IV unknown: block_buf is heap-uninitialized; IV captured via Frida v5 EncryptBlock hook; P_initial = Encrypt_K_B(zeros) is deterministic — no IV file needed | RWN, Twofish, CFB, IV, block_buf, K0, P_initial, Frida, EncryptBlock, iv_bytes.bin | [Issues/B-004-rwn-twofish-iv-unknown.md](Issues/B-004-rwn-twofish-iv-unknown.md) |
| B-003 | Twofish decrypt fails: "undo last swap" placed before loop instead of after; post-loop placement correct per Feistel structure | Twofish, decrypt, Feistel, swap, post-loop, twofish_pure.py | [Issues/B-003-twofish-decrypt-swap-wrong-position.md](Issues/B-003-twofish-decrypt-swap-wrong-position.md) |
| B-002 | Twofish h() q-box ordering wrong for b[1] and b[3] in 128-bit key case; must match H12/H32 reference macros exactly | Twofish, h(), q-box, q0, q1, H12, H32, MDS, twofish_pure.py | [Issues/B-002-twofish-h-qbox-ordering-wrong.md](Issues/B-002-twofish-h-qbox-ordering-wrong.md) |
| B-001 | Twofish encrypt X[3] rotation wrong: C=XOR-then-ROR(1), D=ROL(1)-then-XOR; ROR(31) is wrong | Twofish, encrypt, Feistel, ROL, ROR, X[2], X[3], ENCRYPT_RND, twofish_pure.py | [Issues/B-001-twofish-encrypt-x3-rotation-wrong.md](Issues/B-001-twofish-encrypt-x3-rotation-wrong.md) |
| RS-ENCODING | RS MDS encoding used wrong matrix-multiply approach; fixed to LFSR polynomial reduction with poly 0x14D | Twofish, RS encoding, LFSR, poly 0x14D, MDS, _rs_mds_encode | [Issues/RS-ENCODING-lfsr-polynomial.md](Issues/RS-ENCODING-lfsr-polynomial.md) |
| KEY-SCHEDULE | Subkey generation wrongly used S_rev instead of M_e/M_o; S_rev is for g-function only | Twofish, key schedule, subkeys, M_e, M_o, S_rev, g-function | [Issues/KEY-SCHEDULE-subkey-generation.md](Issues/KEY-SCHEDULE-subkey-generation.md) |
