"""Scan EvoNotes / WBKLOOKUP / RT / DIGSIG / SHB-SHO DFMs (Pass 490)."""
import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

BASE = r"C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples\dfm"

TARGETS = {
    "EvoNotes": ["EvoNotes.DFM","EvoNotesARCH.DFM","EvoNoteSearch.DFM","EvoNotesPrt.DFM","EvoNotesRpt.DFM",
                 "EVOENOTES.DFM","evoreminders.DFM","evorereminders.DFM","classic2evonts.DFM","REMREM.DFM"],
    "WBKLOOKUP": ["WBKLOOKUP.DFM","WBKHHLOOKUP.DFM","WBKLKPMEMO.DFM","WBKLPRINT.DFM","WBKLUGRID.DFM"],
    "RT_DIGSIG": ["T7RTMVALID.DFM","T7DIGSIG.DFM","T7DigSigChgPSWD.DFM","T7DSIG.DFM"],
    "SH_Shipping": ["T7SHB.DFM","T7SHC.DFM","T7SHE.DFM","T7SHF.DFM","T7SHG.DFM",
                    "T7SHH.DFM","T7SHI.DFM","T7SHJ.DFM","T7SHM.DFM","T7SHN.DFM","T7SHO.DFM",
                    "T7SHIPRTM.DFM"],
}

def scan(fp):
    raw = open(fp, 'rb').read()
    text = raw.decode('latin-1', errors='replace')
    caps  = list(dict.fromkeys(f for f in re.findall(r"Caption\s*=\s*'([^']{2,80})'", text) if len(f) > 2))
    hints = list(dict.fromkeys(re.findall(r"Hint\s*=\s*'([^']{2,80})'", text)))
    items_raw = re.findall(r"Items\.Strings\s*=\s*\((.*?)\)", text, re.S)
    items = []
    for ir in items_raw:
        items += [l.strip().strip("'") for l in ir.strip().split('\n') if l.strip().strip("'")]
    has_etb = 'ETBcomboval' in text
    return caps, hints, items, has_etb

for group, names in TARGETS.items():
    print(f"\n{'='*60}\n=== {group} ===")
    for name in names:
        fp = os.path.join(BASE, name)
        if not os.path.exists(fp):
            # try case-insensitive
            found = [f for f in os.listdir(BASE) if f.upper() == name.upper()]
            if found:
                fp = os.path.join(BASE, found[0])
            else:
                print(f"\n{name}: NOT FOUND")
                continue
        caps, hints, items, has_etb = scan(fp)
        print(f"\n{name}: {caps[0] if caps else 'NO_CAP'}{' [LISTG60]' if has_etb else ''}")
        if caps[1:]:  print(f"  caps={caps[1:16]}")
        if hints:     print(f"  hints={hints[:8]}")
        if items:     print(f"  items={items[:14]}")
