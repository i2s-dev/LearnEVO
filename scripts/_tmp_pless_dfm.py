"""Scan T7PLess DFMs."""
import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

DFM_DIR = r"C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples\tpless_dfms"
for fn in sorted(os.listdir(DFM_DIR), key=lambda x: x.upper()):
    if not fn.upper().endswith('.DFM'):
        continue
    fp = os.path.join(DFM_DIR, fn)
    raw = open(fp, 'rb').read()
    text = raw.decode('latin-1', errors='replace')
    caps = list(dict.fromkeys(f for f in re.findall(r"Caption\s*=\s*'([^']{2,80})'", text) if len(f) > 2))
    hints = list(dict.fromkeys(re.findall(r"Hint\s*=\s*'([^']{2,80})'", text)))
    items = re.findall(r"Items\.Strings\s*=\s*\((.*?)\)", text, re.S)
    print(f"\n{fn}: {caps[0] if caps else 'NO_CAP'}")
    print(f"  caps={caps[:16]}")
    print(f"  hints={hints[:8]}")
    for item in items[:3]:
        lines = [l.strip().strip("'") for l in item.strip().split('\n') if l.strip().strip("'")]
        print(f"  items={lines[:10]}")
