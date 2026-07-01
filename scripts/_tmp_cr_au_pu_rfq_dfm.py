"""Scan CR/AU/PU/RF DFMs."""
import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

BASE = r"C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples\cr_au_pu_rfq_dfms"

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
    names_raw = re.findall(r"Name\s*=\s*'([^']{2,60})'", text)
    fieldnames = [n for n in names_raw if any(k in n.lower() for k in ('edit','combo','check','memo','list','grid','btn','button','label','rad','spin'))]
    print(f"\n{fn}: {caps[0] if caps else 'NO_CAP'}")
    if caps[1:]: print(f"  caps={caps[1:14]}")
    if hints: print(f"  hints={hints[:8]}")
    if items: print(f"  items={items[:12]}")
    if fieldnames: print(f"  fields={fieldnames[:12]}")
