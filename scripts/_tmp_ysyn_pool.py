"""
Analyze T7YSYN.RWN.dec pool to find ISTS.CFG key -> YN slot adjacency pairs.
Strategy: extract all string-like tokens from the binary pool, find instances
where an ISTS.CFG.* string is followed closely by a BKYS.YN[N] reference (or vice versa).
"""
import re, sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

with open(r'samples\src\T7YSYN.RWN.dec', 'rb') as f:
    data = f.read()

print(f"File size: {len(data):,} bytes")

# Extract all printable ASCII strings of length >= 5
# Look for ISTS.CFG.* patterns
cfg_pattern = re.compile(rb'ISTS\.CFG\.[A-Z0-9.]{3,50}')
yn_pattern = re.compile(rb'BKYS\.YN\[\d+\]')
bkys_pattern = re.compile(rb'BKYS\.[A-Z.]+\[\d+\]')

cfg_matches = [(m.start(), m.group().decode('ascii')) for m in cfg_pattern.finditer(data)]
yn_matches = [(m.start(), m.group().decode('ascii')) for m in yn_pattern.finditer(data)]
bkys_matches = [(m.start(), m.group().decode('ascii')) for m in bkys_pattern.finditer(data)]

print(f"ISTS.CFG.* matches: {len(cfg_matches)}")
print(f"BKYS.YN[N] matches: {len(yn_matches)}")
print(f"BKYS.*[N] matches total: {len(bkys_matches)}")
print()

# For each YN match, find the closest ISTS.CFG.* match within 200 bytes before or after
print("=== YN slot -> nearest ISTS.CFG key (within 200 bytes) ===")
proximity_map = {}  # YN slot -> list of (cfg_key, distance)
for yn_pos, yn_str in yn_matches:
    # extract slot number
    m = re.match(r'BKYS\.YN\[(\d+)\]', yn_str)
    if not m:
        continue
    slot = int(m.group(1))
    # find nearest cfg key
    nearby = []
    for cfg_pos, cfg_str in cfg_matches:
        dist = abs(cfg_pos - yn_pos)
        if dist <= 200:
            nearby.append((dist, cfg_str))
    nearby.sort()
    if nearby:
        if slot not in proximity_map:
            proximity_map[slot] = []
        proximity_map[slot].extend(nearby[:3])

# Print results sorted by slot number
for slot in sorted(proximity_map.keys()):
    pairs = proximity_map[slot]
    # deduplicate
    seen_keys = {}
    for dist, key in pairs:
        if key not in seen_keys or dist < seen_keys[key]:
            seen_keys[key] = dist
    best_keys = sorted(seen_keys.items(), key=lambda x: x[1])[:3]
    print(f"YN[{slot:3d}]: {best_keys}")

print()

# Also look for any contiguous run patterns in pool
# Find where the pool section starts by looking for first long run of readable text
# after the instruction section
print("=== First 30 BKYS.YN occurrences with context ===")
for i, (pos, yn_str) in enumerate(yn_matches[:30]):
    # extract context: 60 bytes before and after
    start = max(0, pos - 60)
    end = min(len(data), pos + len(yn_str) + 60)
    ctx = data[start:end]
    # find printable parts
    printable = ''.join(chr(b) if 32 <= b < 127 else '.' for b in ctx)
    print(f"  [{i:2d}] pos={pos:6d}: {printable}")
