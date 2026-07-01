"""Scan JC/SC/RE/JS/FS/JO DFMs (Pass 488)."""
import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

DIRS = {
    "JC": r"C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples\qc_jc_dfms",
    "SC": r"C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples\batch_dfms",
    "RE_JS_FS_JO": r"C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples\re_js_fs_jo_dfms",
}

JC_NAMES = {f.upper() for f in ["T7JCA","T7JCB","T7JCE","T7JCENG","T7JCF","T7JCH","T7JCL","T7JCM","T7JCN","T7JCP","T7JCQ","T7JCR","T7JCRM","T7JCS"]}
SC_NAMES = {f.upper() for f in ["T7SCA","T7SCB","T7SCC","T7SCC2","T7SCE","T7SCF","T7SCG","T7SCH","T7SCOMP"]}

def scan_dfm(fp):
    raw = open(fp, 'rb').read()
    text = raw.decode('latin-1', errors='replace')
    caps = list(dict.fromkeys(f for f in re.findall(r"Caption\s*=\s*'([^']{2,80})'", text) if len(f) > 2))
    hints = list(dict.fromkeys(re.findall(r"Hint\s*=\s*'([^']{2,80})'", text)))
    items_raw = re.findall(r"Items\.Strings\s*=\s*\((.*?)\)", text, re.S)
    items = []
    for ir in items_raw:
        items += [l.strip().strip("'") for l in ir.strip().split('\n') if l.strip().strip("'")]
    has_etb = 'ETBcomboval' in text
    return caps, hints, items, has_etb

for grp, base in DIRS.items():
    print(f"\n{'='*60}\n=== {grp} ===")
    for fn in sorted(os.listdir(base)):
        if not fn.upper().endswith('.DFM'):
            continue
        stem = os.path.splitext(fn)[0].upper()
        # Filter to only the relevant group
        if grp == "JC" and stem not in JC_NAMES:
            continue
        if grp == "SC" and stem not in SC_NAMES:
            continue
        fp = os.path.join(base, fn)
        caps, hints, items, has_etb = scan_dfm(fp)
        print(f"\n{fn}: {caps[0] if caps else 'NO_CAP'}{' [LISTG60]' if has_etb else ''}")
        if caps[1:]: print(f"  caps={caps[1:16]}")
        if hints:    print(f"  hints={hints[:8]}")
        if items:    print(f"  items={items[:12]}")
