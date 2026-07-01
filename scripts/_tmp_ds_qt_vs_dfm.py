"""Scan DS/QT/VSCHED/MA DFMs."""
import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

BASE = r"C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples"

FILES = [
    ("dfm", "T7DSIG.DFM"),
    ("dfm", "T7QTINFO.DFM"),
    ("dfm", "T7VSCHED.DFM"),
    ("dfm ed_misc_dfms misc_dfms", "T7MAPDEPO.DFM"),
]

for dirfrag, fn in FILES:
    for subdir in dirfrag.split():
        fp = os.path.join(BASE, subdir, fn)
        if os.path.exists(fp):
            raw = open(fp, 'rb').read()
            text = raw.decode('latin-1', errors='replace')
            caps = list(dict.fromkeys(f for f in re.findall(r"Caption\s*=\s*'([^']{2,80})'", text) if len(f) > 2))
            hints = list(dict.fromkeys(re.findall(r"Hint\s*=\s*'([^']{2,80})'", text)))
            items_raw = re.findall(r"Items\.Strings\s*=\s*\((.*?)\)", text, re.S)
            items = []
            for ir in items_raw:
                items += [l.strip().strip("'") for l in ir.strip().split('\n') if l.strip().strip("'")]
            print(f"\n{fn}: {caps[0] if caps else 'NO_CAP'}")
            if caps[1:]: print(f"  caps={caps[1:16]}")
            if hints: print(f"  hints={hints[:8]}")
            if items: print(f"  items={items[:12]}")
            break
