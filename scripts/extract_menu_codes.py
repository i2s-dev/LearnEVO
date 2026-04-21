"""
Mine the bulk-extracted strings of all RWN/RUN/DCY files for menu codes
of the form  XX-Y[-Z]  <text>  where XX is a 2-letter module code.
"""
import csv
import re
from pathlib import Path
from collections import defaultdict

SRC = Path(r"c:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples\rwn_strings")
OUT = SRC.parent / "menu_codes.csv"

MENU_RE = re.compile(
    r"\b([A-Z]{2})-([A-Z])(?:-([A-Z]))?  +([A-Za-z][A-Za-z0-9 /'\",\-\.&()\+#]{3,80}?)\s*[A-Z]?\s*$"
)

MODULE_OK = set("""SO PO AR AP IN WO MR GL SR LW JC ES LC SC UT RM QT RF BM PR CC DC HH EI EM EV FS FT FO FI PI QC RO RT SM SP SA SB SH WC AD AH AM AN AT AV BO CG CS CT CU DA DE DF DI DL DO DP DR DS DT DX EA EB EC ED ER FR FP GF GI GR HA HI HO HP HR HS HT IC IS JA JS KB KC KP LA LB LM LP LS MA MB ME MF MG MI ML MM MN MO MP MS MT NA NB NC NO NP NR NT OA OB OC OD OM OP OR OS OT PA PB PC PD PE PF PG PH PK PL PM PN PP PQ PS PT PY QA QB QC QD QE QF QG QH QM QP QR QS QT QU RA RB RC RD RF RG RH RI RK RL RM RN RO RP RQ RR RS RT RU RV RW RX RY SA SB SC SD SE SF SG SH SJ SK SL SM SN SO SP SQ SR SS ST SU SV SW SX SY SZ""".split())


def main():
    found = defaultdict(set)  # code -> set of descriptions
    sources = defaultdict(set)  # code -> files that mention it
    total = 0
    files_scanned = 0
    for p in SRC.glob("*.txt"):
        files_scanned += 1
        text = p.read_text(encoding="utf-8", errors="replace")
        for line in text.splitlines():
            line = line.strip()
            m = MENU_RE.search(line)
            if not m:
                continue
            mod, l1, l2, desc = m.groups()
            if mod not in MODULE_OK:
                continue
            desc = desc.strip().strip("'\"").strip()
            if len(desc) < 4:
                continue
            if desc.count(" ") == 0 and desc.isupper():
                continue  # probably file name
            code = f"{mod}-{l1}" + (f"-{l2}" if l2 else "")
            found[code].add(desc)
            sources[code].add(p.stem.replace(".RUN", "").replace(".RWN", ""))
            total += 1

    # Write CSV
    with OUT.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["code", "module", "description", "sources"])
        for code in sorted(found):
            module = code.split("-")[0]
            # pick the most common/canonical description (shortest-ish, alpha)
            descs = sorted(found[code], key=lambda s: (len(s), s))
            desc = descs[0]
            srcs = ";".join(sorted(sources[code])[:5])
            w.writerow([code, module, desc, srcs])

    # Print summary
    print(f"Scanned {files_scanned} files, {total} matches, {len(found)} unique menu codes")
    by_mod = defaultdict(int)
    for code in found:
        by_mod[code.split("-")[0]] += 1
    for m, n in sorted(by_mod.items(), key=lambda x: -x[1]):
        print(f"  {m}: {n}")


if __name__ == "__main__":
    main()
