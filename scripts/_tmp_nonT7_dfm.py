"""Scan non-T7 DFM groups: UT7G, EvoFNO, T6ISINB, WBKMEN, misc_infra."""
import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

BASE = r"C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples"

def scan_dir(label, d):
    print(f"\n{'='*60}")
    print(f"=== {label} ===")
    for fn in sorted(os.listdir(d), key=lambda x: x.upper()):
        if not fn.upper().endswith('.DFM'):
            continue
        raw = open(os.path.join(d, fn), 'rb').read()
        text = raw.decode('latin-1', errors='replace')
        caps = list(dict.fromkeys(f for f in re.findall(r'Caption\s*=\s*[\'"]([^\'"]{2,80})[\'"]', text) if len(f) > 2))
        print(f"\n{fn}: {caps[0] if caps else 'NO_CAP'}")
        print(f"  {caps[:16]}")

scan_dir("UT7G (Golding Farms Utilities)", os.path.join(BASE, "ut7g_dfms"))
scan_dir("EvoFNO (FN / Free Notes / FNO)", os.path.join(BASE, "evofno_dfms"))
scan_dir("T6ISINB (Legacy IS Inventory Batch)", os.path.join(BASE, "t6isinb_dfms"))
scan_dir("WBKMEN (Workbook Menu Infrastructure)", os.path.join(BASE, "wbkmen_dfms"))
scan_dir("MISC / INFRA", os.path.join(BASE, "misc_infra_dfms"))
