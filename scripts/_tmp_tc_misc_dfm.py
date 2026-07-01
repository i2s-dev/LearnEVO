"""Scan TC misc DFMs and SP DFMs from batch_dfms."""
import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

def scan_dir(d):
    for fn in sorted(os.listdir(d), key=lambda x: x.upper()):
        if not fn.upper().endswith('.DFM'): continue
        raw = open(os.path.join(d, fn), 'rb').read()
        text = raw.decode('latin-1', errors='replace')
        cap = re.search(r'Caption\s*=\s*[\'"]([^\'"]{2,80})[\'"]', text)
        fields = list(dict.fromkeys(f for f in re.findall(r'Caption\s*=\s*[\'"]([^\'"]{2,60})[\'"]', text) if len(f) > 2))
        print(f"\n{fn}: cap={cap.group(1) if cap else None}")
        print(f"  {fields[:14]}")

print("=== TC/MISC ===")
scan_dir(r"C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples\tc_sp_dfms")

print("\n=== SP (from batch_dfms) ===")
batch_dir = r"C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples\batch_dfms"
for fn in sorted(os.listdir(batch_dir), key=lambda x: x.upper()):
    if not fn.upper().endswith('.DFM'): continue
    if not fn.upper().startswith('T7SP'): continue
    raw = open(os.path.join(batch_dir, fn), 'rb').read()
    text = raw.decode('latin-1', errors='replace')
    cap = re.search(r'Caption\s*=\s*[\'"]([^\'"]{2,80})[\'"]', text)
    fields = list(dict.fromkeys(f for f in re.findall(r'Caption\s*=\s*[\'"]([^\'"]{2,60})[\'"]', text) if len(f) > 2))
    print(f"\n{fn}: cap={cap.group(1) if cap else None}")
    print(f"  {fields[:14]}")
