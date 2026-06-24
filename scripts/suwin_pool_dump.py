#!/usr/bin/env python3
"""Hex dump the pool around specific poff values and scan pool structure."""
import struct, sys

path = r"C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples\rwn_decrypted\suwin6t.rwn.dec"
with open(path, "rb") as f:
    data = f.read()

DISP = 0x6C8
POOL_TYPES = {0x41, 0x46, 0x43, 0x4E, 0x52}

n = 0
off = DISP
while off + 8 <= len(data) and data[off+1] == 0x00:
    n += 1; off += 8
while n > 0 and data[DISP + (n-1)*8] in POOL_TYPES:
    n -= 1
POOL = DISP + n * 8
pool = data[POOL:]

def hexdump(blob, base_offset=0, width=16):
    for row in range(0, len(blob), width):
        chunk = blob[row:row+width]
        hex_part = " ".join(f"{b:02X}" for b in chunk)
        asc_part = "".join(chr(b) if 0x20 <= b <= 0x7E else "." for b in chunk)
        print(f"  {base_offset+row:5d}  {hex_part:<{width*3}}  {asc_part}")

def str_at(pool, poff):
    if poff + 4 <= len(pool) and pool[poff] == 0x41 and pool[poff+1] == 0x00:
        slen = struct.unpack_from("<H", pool, poff+2)[0]
        if slen < 500 and poff+4+slen <= len(pool):
            return pool[poff+4:poff+4+slen].decode("latin-1", errors="replace")
    return "(not a STRING)"

print("=== Pool bytes 0..150 ===")
hexdump(pool[0:150])
print()
print("=== Pool bytes 840..1120 (around confirmed STRING entries 901, 1041, 1074) ===")
hexdump(pool[840:1120], base_offset=840)
print()

# Look at all ASSIGN poff values
print("=== ASSIGN instructions: poff → pool bytes at that offset ===")
for i in range(n):
    ioff = DISP + i*8
    op = data[ioff]; sub = data[ioff+3]
    poff = struct.unpack_from("<I", data, ioff+4)[0]
    if op == 0x0F:
        # Show 20 bytes at pool[poff]
        chunk = pool[poff:poff+20]
        hex_part = " ".join(f"{b:02X}" for b in chunk)
        t = pool[poff] if poff < len(pool) else 0
        tname = {0x41:"STR", 0x46:"FLT", 0x43:"INT", 0x4E:"NAM", 0x52:"REL"}.get(t, f"?{t:02X}")
        print(f"  [{i:3d}] poff={poff:<6}  type={tname}  {hex_part}")

print()
print("=== GOSUB instructions: poff → pool bytes at that offset ===")
for i in range(n):
    ioff = DISP + i*8
    op = data[ioff]; sub = data[ioff+3]
    poff = struct.unpack_from("<I", data, ioff+4)[0]
    if op == 0x42:
        chunk = pool[poff:poff+20]
        hex_part = " ".join(f"{b:02X}" for b in chunk)
        t = pool[poff] if poff < len(pool) else 0
        tname = {0x41:"STR", 0x46:"FLT", 0x43:"INT", 0x4E:"NAM", 0x52:"REL"}.get(t, f"?{t:02X}")
        print(f"  [{i:3d}] poff={poff:<6}  type={tname}  {hex_part}")

print()
print("=== COND_BRANCH instructions: poff → pool bytes at that offset ===")
for i in range(n):
    ioff = DISP + i*8
    op = data[ioff]; sub = data[ioff+3]
    poff = struct.unpack_from("<I", data, ioff+4)[0]
    if op == 0x3B:
        chunk = pool[poff:poff+24]
        hex_part = " ".join(f"{b:02X}" for b in chunk)
        t = pool[poff] if poff < len(pool) else 0
        tname = {0x41:"STR", 0x46:"FLT", 0x43:"INT", 0x4E:"NAM", 0x52:"REL"}.get(t, f"?{t:02X}")
        print(f"  [{i:3d}] poff={poff:<6}  type={tname}  {hex_part}")

# Scan pool starting from poff=0 looking for runs of printable data
print()
print("=== Printable string runs in pool (>6 chars) ===")
run_start = None; run_bytes = []
for j in range(min(5000, len(pool))):
    b = pool[j]
    if 0x20 <= b <= 0x7E:
        if run_start is None: run_start = j
        run_bytes.append(chr(b))
    else:
        if run_start is not None and len(run_bytes) >= 6:
            s = "".join(run_bytes)
            print(f"  pool[{run_start:5d}..{run_start+len(run_bytes)-1}]  \"{s}\"")
        run_start = None; run_bytes = []
if run_start and len(run_bytes) >= 6:
    print(f"  pool[{run_start:5d}..{run_start+len(run_bytes)-1}]  \"{''.join(run_bytes)}\"")
