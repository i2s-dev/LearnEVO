"""Scan T7DC DFMs for Data Collection module analysis."""
import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')
DFM_DIR = r"C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples\dc_dfms"
for fn in sorted(os.listdir(DFM_DIR), key=lambda x: x.upper()):
    if not fn.upper().endswith('.DFM'): continue
    raw = open(os.path.join(DFM_DIR, fn), 'rb').read()
    text = raw.decode('latin-1', errors='replace')
    cap = re.search(r'Caption\s*=\s*[\'"]([^\'"]{2,80})[\'"]', text)
    fields = list(dict.fromkeys(f for f in re.findall(r'Caption\s*=\s*[\'"]([^\'"]{2,60})[\'"]', text) if len(f) > 2))
    print(f"\n{fn}: cap={cap.group(1) if cap else None}")
    print(f"  {fields[:14]}")
