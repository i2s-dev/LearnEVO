"""Scan C:90 module DFMs to enrich stubs."""
import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

BASE = r"C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples"

GROUPS = {
    "NE": [("samples dfm", "T7NEWINIT.DFM")],
    "EM": [("dfm misc_dfms", "T7EMGL.DFM")],
    "MA": [("dfm ed_misc_dfms", "T7MAPDEPO.DFM")],
    "PA": [("pa_dfms", "t7packmenu.DFM"), ("pa_dfms", "T7Paperless.DFM"), ("pa_dfms", "T7PASS.DFM")],
    "AL": [("dfm misc_dfms", "T7ALERTMSG.DFM"), ("dfm misc_dfms", "T7ALOGSETUP.DFM"), ("dfm misc_dfms", "T7ALTPART.DFM")],
    "SE": [("dfm", "T7SELLOC.DFM"), ("dfm", "T7SEPROC.DFM"), ("dfm", "T7SERR.DFM"), ("dfm", "T7SETYPE.DFM")],
    "CH": [("dfm misc_dfms", "T7Chain.DFM"), ("dfm misc_dfms", "T7CHAINM.DFM"), ("dfm misc_dfms", "T7CHARGBK.DFM")],
    "ML": [("dfm", "T7MLC.DFM"), ("dfm", "T7MLE.DFM")],
}

def scan(dirfrag, fn):
    # Try to find file in multiple subdir variants
    for subdir in [dirfrag, dirfrag.split()[0], dirfrag.split()[-1]]:
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
            return caps, hints, items[:12]
    return None, None, None

for module, files in GROUPS.items():
    print(f"\n{'='*55}")
    print(f"=== {module} ===")
    for dirfrag, fn in files:
        caps, hints, items = scan(dirfrag, fn)
        if caps is None:
            print(f"  {fn}: NOT FOUND (tried {dirfrag})")
            continue
        print(f"\n  {fn}: {caps[0] if caps else 'NO_CAP'}")
        if caps[1:]:
            print(f"    caps={caps[1:14]}")
        if hints:
            print(f"    hints={hints[:8]}")
        if items:
            print(f"    items={items[:10]}")
