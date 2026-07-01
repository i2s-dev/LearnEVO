"""Scan MK/SH/MA/SD/BR DFMs (Pass 489)."""
import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

BASE = r"C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples\mk_sh_ma_sd_br_dfms"

for fn in sorted(os.listdir(BASE)):
    if not fn.upper().endswith('.DFM'):
        continue
    fp = os.path.join(BASE, fn)
    raw = open(fp, 'rb').read()
    text = raw.decode('latin-1', errors='replace')
    caps = list(dict.fromkeys(f for f in re.findall(r"Caption\s*=\s*'([^']{2,80})'", text) if len(f) > 2))
    hints = list(dict.fromkeys(re.findall(r"Hint\s*=\s*'([^']{2,80})'", text)))
    items_raw = re.findall(r"Items\.Strings\s*=\s*\((.*?)\)", text, re.S)
    items = []
    for ir in items_raw:
        items += [l.strip().strip("'") for l in ir.strip().split('\n') if l.strip().strip("'")]
    has_etb = 'ETBcomboval' in text
    print(f"\n{fn}: {caps[0] if caps else 'NO_CAP'}{' [LISTG60]' if has_etb else ''}")
    if caps[1:]: print(f"  caps={caps[1:18]}")
    if hints:    print(f"  hints={hints[:8]}")
    if items:    print(f"  items={items[:14]}")
