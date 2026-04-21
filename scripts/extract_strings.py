"""
Extract printable ASCII strings of minimum length N from a binary file.

Read-only. Writes to stdout. Mirrors the `strings` unix utility.

Usage:
    python extract_strings.py <file> [min_len]
"""
import sys
from pathlib import Path

def extract(path: Path, min_len: int = 6):
    data = path.read_bytes()
    out = []
    cur = bytearray()
    for b in data:
        if 32 <= b < 127:
            cur.append(b)
        else:
            if len(cur) >= min_len:
                out.append(cur.decode("ascii", errors="replace"))
            cur.clear()
    if len(cur) >= min_len:
        out.append(cur.decode("ascii", errors="replace"))
    return out

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    path = Path(sys.argv[1])
    min_len = int(sys.argv[2]) if len(sys.argv) > 2 else 6
    for s in extract(path, min_len):
        print(s)
