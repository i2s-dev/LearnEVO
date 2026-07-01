"""Scan misc_infra2 DFMs: Evo*, WTAS*, NZE*, WBK* infrastructure."""
import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

DFM_DIR = r"C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples\misc_infra2_dfms"
for fn in sorted(os.listdir(DFM_DIR), key=lambda x: x.upper()):
    if not fn.upper().endswith('.DFM'):
        continue
    raw = open(os.path.join(DFM_DIR, fn), 'rb').read()
    text = raw.decode('latin-1', errors='replace')
    caps = list(dict.fromkeys(f for f in re.findall(r'Caption\s*=\s*[\'"]([^\'"]{2,80})[\'"]', text) if len(f) > 2))
    print(f"\n{fn}: {caps[0] if caps else 'NO_CAP'}")
    print(f"  {caps[:16]}")
