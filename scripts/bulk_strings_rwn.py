"""
Bulk-extract printable ASCII strings from every .RWN and .DCY file on
the EvoERP network share, in parallel.

Although RWN/DCY are encrypted, some modules contain embedded resource
strings (paths, SQL fragments, messages) that survived. We also get
header signatures useful for format analysis.

Output: samples/rwn_strings/<filename>.txt — one file per module.
"""
import glob
import multiprocessing as mp
import sys
from pathlib import Path

HERE = Path(__file__).parent
OUT = HERE.parent / "samples" / "rwn_strings"
OUT.mkdir(exist_ok=True, parents=True)

SHARES = [r"\\I2S109-SOLIDCRM\DBAMFG$"]


def extract(path_str: str) -> tuple[str, int]:
    path = Path(path_str)
    dest = OUT / (path.name + ".txt")
    if dest.exists():
        return str(path), -1  # already done
    try:
        data = path.read_bytes()
    except Exception:
        return str(path), -2
    strs = []
    cur = bytearray()
    for b in data:
        if 32 <= b < 127:
            cur.append(b)
        else:
            if len(cur) >= 6:
                strs.append(cur.decode("ascii", errors="replace"))
            cur.clear()
    if len(cur) >= 6:
        strs.append(cur.decode("ascii", errors="replace"))
    dest.write_text("\n".join(strs), encoding="utf-8")
    return str(path), len(strs)


def main():
    paths = []
    for root in SHARES:
        for ext in ("*.RWN", "*.rwn", "*.RUN", "*.run", "*.DCY", "*.dcy"):
            paths.extend(glob.glob(str(Path(root) / ext)))
    # dedupe case-insensitive
    seen = set(); dedup = []
    for p in paths:
        k = Path(p).name.upper()
        if k in seen: continue
        seen.add(k); dedup.append(p)
    print(f"{len(dedup)} files to process", file=sys.stderr)

    pool = mp.Pool(processes=6)
    done = 0
    for path, n in pool.imap_unordered(extract, dedup):
        done += 1
        if done % 100 == 0:
            print(f"done {done}", file=sys.stderr)
    print(f"all done ({done})", file=sys.stderr)


if __name__ == "__main__":
    main()
