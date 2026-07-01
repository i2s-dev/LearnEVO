"""Scan T7GF* DFMs in batch_dfms."""
import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

DFM_DIR = r"C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples\batch_dfms"
for fn in sorted(os.listdir(DFM_DIR), key=lambda x: x.upper()):
    if not fn.upper().startswith('T7GF') or not fn.upper().endswith('.DFM'):
        continue
    fp = os.path.join(DFM_DIR, fn)
    raw = open(fp, 'rb').read()
    text = raw.decode('latin-1', errors='replace')
    caps = list(dict.fromkeys(f for f in re.findall(r"Caption\s*=\s*'([^']{2,80})'", text) if len(f) > 2))
    hints = list(dict.fromkeys(re.findall(r'Hint\s*=\s*\'([^\']{2,80})\'', text)))
    print(f"\n{fn}: {caps[0] if caps else 'NO_CAP'}")
    print(f"  caps={caps[:12]}")
    print(f"  hints={hints[:6]}")
