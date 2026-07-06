"""
Decode T7YSYN.RWN.dec variable table to find ISTS.CFG key -> BKYSMSTR field mapping.
Variable table: last 95711 bytes of file, 1243 records × 77 bytes each, start=123851.
Record format: bytes 0-14 = 15-char name (padded), bytes 15-76 = metadata.
"""
import struct, sys, io, re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

POOL_START = 123851
RECORD_SIZE = 77
NUM_VARS = 1243

with open(r'samples\src\T7YSYN.RWN.dec', 'rb') as f:
    data = f.read()

print(f"File size: {len(data):,}, expected end: {POOL_START + NUM_VARS * RECORD_SIZE:,}")
print()

# Parse all variable records
vars_list = []
for i in range(NUM_VARS):
    offset = POOL_START + i * RECORD_SIZE
    rec = data[offset:offset + RECORD_SIZE]
    name_raw = rec[0:15]
    # find null terminator
    null_pos = name_raw.find(b'\x00')
    if null_pos == -1:
        name = name_raw.decode('ascii', errors='replace')
    else:
        name = name_raw[:null_pos].decode('ascii', errors='replace')
    meta = rec[15:]  # 62 bytes of metadata
    vars_list.append((i, name, meta, offset))

# Show BKYS.* vars with full metadata
print("=== BKYS.* variables (field access descriptors) ===")
for i, name, meta, offset in vars_list:
    if name.startswith('BKYS.'):
        hex_meta = ' '.join(f'{b:02x}' for b in meta[:20])
        print(f"  [{i:4d}] {name:<20s} | meta[0:20] = {hex_meta}")

print()

# Show metadata bytes for all ISTS.CFG vars (first 20 + all for known YN slots)
print("=== ISTS.CFG.* variables — first 20 with metadata ===")
cfg_vars = [(i, name, meta, offset) for i, name, meta, offset in vars_list if name.startswith('ISTS.CFG.')]
print(f"Total ISTS.CFG vars: {len(cfg_vars)}")
for i, name, meta, offset in cfg_vars[:20]:
    # interpret possible field offset at various locations
    # Try little-endian uint16 at bytes 17,19,21,25
    def u16(b, off): return struct.unpack_from('<H', b, off)[0] if off+2 <= len(b) else 0
    def u32(b, off): return struct.unpack_from('<I', b, off)[0] if off+4 <= len(b) else 0
    hex_meta = ' '.join(f'{b:02x}' for b in meta[:30])
    print(f"  [{i:4d}] {name:<30s} | {hex_meta}")

print()

# Look at metadata pattern for known-mapped ISTS.CFG keys
# Known: YN[48]='1'=AP laser check format from BKAPH.SRC, ISTS.CFG.APCHK?
# Known: YN[20]=DC barcode mode from BKDCA.SRC (ISTS.CFG.DC.BARCODE?)
# Known: YN[59]=routing overlap from BKROA.SRC (ISTS.CFG.RO.OVERLAP or similar?)
known_keys = [
    'ISTS.CFG.APCHK', 'ISTS.CFG.LAPCHK', 'ISTS.CFG.APCHKCKS',
    'ISTS.CFG.DCBARCD', 'ISTS.CFG.DC.BAR', 'ISTS.CFG.DCBAR',
    'ISTS.CFG.ROVERLP', 'ISTS.CFG.ROOVLP',
    'ISTS.CFG.WOCALC', 'ISTS.CFG.WOCAL',  # YN[38]
    'ISTS.CFG.LNGWT',  # YN[66]
]
print("=== Searching for known YN-mapped ISTS.CFG keys ===")
for kk in known_keys:
    found = [(i, name, meta) for i, name, meta, offset in vars_list if name == kk]
    if found:
        for i, name, meta in found:
            hex_meta = ' '.join(f'{b:02x}' for b in meta[:30])
            print(f"  FOUND [{i:4d}] {name} | {hex_meta}")

# Show keys that contain known YN-related substrings
yn_keyword_patterns = ['APCHK', 'LAPCH', 'DCBAR', 'ROVLP', 'WOCAL', 'LNGWT', 'SOKIT', 'WOGKIT']
print()
print("=== ISTS.CFG.* keys matching YN-related substrings ===")
for pattern in yn_keyword_patterns:
    matches = [(i, name) for i, name, meta, offset in vars_list if pattern in name.upper()]
    if matches:
        for i, name in matches:
            print(f"  [{i:4d}] {name} (contains '{pattern}')")

# Analysis: look at bytes 16-25 of ISTS.CFG.* records to find the field offset pattern
# BKYSMSTR layout (from DDF):
#   Offset  0: BKYS_WONUM (FLOAT, 8B) = YN[0]? No, WONUM is a separate slot
#   Offset  8: BKYS_YN_1 (STRING 1B)
#   Offset  9: BKYS_YN_2 (STRING 1B)
#   ...
#   Offset 8+N-1: BKYS_YN_N
#   Offset 258: after all 250 YN slots
#   Then GLNUM[1-40] (FLOAT 8B each) = offsets 258-577
#   Then GLDPT[1-40] (STRING 4B each) = offsets 578-737
# If meta contains a field offset, for BKYS_YN_48: offset = 8+47 = 55
print()
print("=== Looking for field offset encoding in ISTS.CFG metadata ===")
# Strategy: for each ISTS.CFG var, check if any u16 or u32 in meta[16:30] falls in 8-258 (YN range)
yn_candidates = []
for i, name, meta, offset in cfg_vars:
    for off in range(0, min(30, len(meta)-1), 1):
        if off+2 <= len(meta):
            val = struct.unpack_from('<H', meta, off)[0]
            if 8 <= val <= 257:  # YN slot range
                yn_slot = val - 7  # YN[N] = offset N+7... actually YN[1] at offset 8 = val-7
                yn_slot_idx = val - 8 + 1  # = val-7
                yn_candidates.append((i, name, off, val, yn_slot_idx))
                break

print(f"ISTS.CFG keys with u16 in YN-range (8-257) in meta: {len(yn_candidates)}")
for i, name, byte_off, val, yn_slot in yn_candidates[:20]:
    print(f"  [{i:4d}] {name:<30s} @ meta[{byte_off}] = {val} -> YN[{yn_slot}]")
