"""
Search T7YSYN.RWN.dec code section (bytes 0..123850) for array-subscript patterns
that reveal ISTS.CFG key -> YN slot assignments.

Strategy:
- Variable 70 = BKYS.YN (the array), encoded as 2-byte LE index = 0x46 0x00
- ISTS.CFG vars are indices 131-625 (0x83-0x0271)
- YN subscript values are 1-250 (small constants)
- Look for 16-bit sequences containing VARINDEX=70 near small integer constants,
  then find nearby ISTS.CFG variable index.
"""
import struct, sys, io, collections

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

CODE_END = 123851
POOL_START = 123851
RECORD_SIZE = 77
NUM_VARS = 1243

with open(r'samples\src\T7YSYN.RWN.dec', 'rb') as f:
    data = f.read()

code = data[:CODE_END]

# Build variable name lookup
var_names = {}
for i in range(NUM_VARS):
    off = POOL_START + i * RECORD_SIZE
    rec = data[off:off + RECORD_SIZE]
    name_raw = rec[0:15]
    null_pos = name_raw.find(b'\x00')
    name = name_raw[:null_pos].decode('ascii', errors='replace') if null_pos != -1 else name_raw.decode('ascii', errors='replace')
    var_names[i] = name

print(f"Code section: {CODE_END:,} bytes")
print(f"Variable table: {NUM_VARS} entries")
print()

# Approach 1: scan for 2-byte LE var index = 70 (BKYS.YN)
# Then look at surrounding bytes for: (a) small integer 1-250, (b) ISTS.CFG var index 131-625
YN_VAR_IDX = 70

# Find all positions where uint16-LE = 70
yn_positions = []
for pos in range(0, CODE_END - 1):
    val = struct.unpack_from('<H', code, pos)[0]
    if val == YN_VAR_IDX:
        yn_positions.append(pos)

print(f"Positions where uint16-LE = 70 (BKYS.YN var index): {len(yn_positions)}")

# For each such position, look in a window of ±32 bytes for small constants AND ISTS.CFG indices
CFG_START = 131
CFG_END = 625
WINDOW = 32

candidates = []
for pos in yn_positions:
    start = max(0, pos - WINDOW)
    end = min(CODE_END, pos + WINDOW + 2)
    window_data = code[start:end]

    # Scan window for uint16 values in CFG range and for small constants 1-250
    cfg_in_window = []
    yn_vals_in_window = []
    for i in range(0, len(window_data) - 1):
        val = struct.unpack_from('<H', window_data, i)[0]
        if CFG_START <= val <= CFG_END:
            cfg_in_window.append((start + i, val))
        if 1 <= val <= 250:
            yn_vals_in_window.append((start + i, val))

    if cfg_in_window and yn_vals_in_window:
        candidates.append((pos, cfg_in_window, yn_vals_in_window))

print(f"YN positions with CFG var + small constant in ±{WINDOW} bytes: {len(candidates)}")
print()

# Show candidates, noting if cfg+small are close to each other
print("=== Top candidates for YN slot -> ISTS.CFG mappings ===")
mapping_guesses = []
for pos, cfg_list, yn_list in candidates[:50]:
    # Find closest cfg-to-small pair
    best = None
    for cpos, cidx in cfg_list:
        for ypos, yval in yn_list:
            dist = abs(cpos - ypos)
            if best is None or dist < best[0]:
                best = (dist, cpos, cidx, ypos, yval)
    if best:
        dist, cpos, cidx, ypos, yval = best
        cfg_name = var_names.get(cidx, f'VAR[{cidx}]')
        mapping_guesses.append((yval, cidx, cfg_name, pos, dist))

# Sort by YN slot number
mapping_guesses.sort(key=lambda x: x[0])

seen = set()
for yn_slot, cfg_idx, cfg_name, pos, dist in mapping_guesses:
    key = (yn_slot, cfg_idx)
    if key in seen:
        continue
    seen.add(key)
    print(f"  YN[{yn_slot:3d}] -> {cfg_name:<30s} (cfg_idx={cfg_idx}, code@{pos}, dist={dist})")

print()

# Approach 2: build a frequency table of 2-byte values in code section
# to understand the encoding scale
print("=== Most common 2-byte LE values in code section ===")
freq = collections.Counter()
for pos in range(0, CODE_END - 1, 2):
    val = struct.unpack_from('<H', code, pos)[0]
    freq[val] += 1

for val, count in freq.most_common(20):
    name = var_names.get(val, '')
    print(f"  0x{val:04x} = {val:5d}: {count:5d}x  {name}")

print()
# Also the most common single-byte values
freq1 = collections.Counter(code)
print("=== Most common single bytes in code section ===")
for byte_val, count in freq1.most_common(16):
    print(f"  0x{byte_val:02x} = {byte_val:3d} ('{chr(byte_val) if 32 <= byte_val < 127 else '.'}'):  {count:6d}x")
