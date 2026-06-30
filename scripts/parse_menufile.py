"""
Parse MENUFILE.B and PRGFILE.B — EvoERP menu structure and program catalog.

MENUFILE fields (from FILEDICT):
  MENU.CODE     - menu operation code (e.g., AR-A-**)
  MENU.CT       - count/type
  MENU.LINES    - number of lines
  MENU.PROG     - program file name (e.g., T7ARA.RWN)
  MENU.TITLE    - menu item title text

PRGFILE fields (from FILEDICT):
  PRGFIL.COMMAND   - TAS Pro keyword/command
  PRGFIL.FILE      - file name
  PRGFIL.PRG.LINE  - source code line number
  PRGFIL.PRG.NAME  - program name
  PRGFIL.RUN.LINE  - runtime line
  PRGFIL.SCN.NAME  - screen/form name
"""
import struct
import re
from pathlib import Path
from collections import Counter

SAMPLES = Path(r"C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples")


def extract_strings_raw(data, min_len=4):
    """Extract printable ASCII strings."""
    results = []
    current = []
    start = 0
    for i, b in enumerate(data):
        if 32 <= b < 127:
            if not current:
                start = i
            current.append(chr(b))
        else:
            if len(current) >= min_len:
                results.append((start, ''.join(current)))
            current = []
    if len(current) >= min_len:
        results.append((start, ''.join(current)))
    return results


def analyze_menufile():
    data = (SAMPLES / 'MENUFILE.B').read_bytes()
    print(f"=== MENUFILE.B ({len(data):,} bytes) ===")

    strings = extract_strings_raw(data, min_len=4)
    print(f"Total strings: {len(strings)}")

    # Menu codes look like: "AR-A-**", "SO-B-*", module letter codes
    menu_codes = [(pos, s) for pos, s in strings
                  if re.match(r'^[A-Z]{2}-[A-Z0-9]-', s) or
                  re.match(r'^[A-Z]{2,3}-[0-9]-', s)]
    print(f"\nMenu code strings: {len(menu_codes)}")
    for pos, s in menu_codes[:30]:
        print(f"  [{pos:05X}] {s!r}")

    # Program names
    prog_names = [(pos, s) for pos, s in strings
                  if (s.endswith('.RWN') or s.endswith('.RUN') or
                      re.match(r'^[TBJ][0-9678][A-Z]', s))]
    print(f"\nProgram name strings: {len(prog_names)}")
    for pos, s in prog_names[:30]:
        print(f"  [{pos:05X}] {s!r}")

    # Menu titles — mixed alphanumeric with spaces
    titles = [(pos, s) for pos, s in strings
              if len(s) >= 5 and ' ' in s and
              not s.startswith('\\') and
              any(c.isalpha() for c in s)]
    print(f"\nPossible menu titles: {len(titles)}")
    for pos, s in titles[:40]:
        print(f"  [{pos:05X}] {s!r}")


def analyze_prgfile():
    data = (SAMPLES / 'PRGFILE.B').read_bytes()
    print(f"\n=== PRGFILE.B ({len(data):,} bytes) ===")

    strings = extract_strings_raw(data, min_len=4)
    print(f"Total strings: {len(strings)}")

    # Program names
    prog_names = [(pos, s) for pos, s in strings
                  if s.endswith('.RWN') or s.endswith('.RUN') or s.endswith('.SRC')]
    print(f"\nProgram file references: {len(prog_names)}")
    for pos, s in prog_names[:30]:
        print(f"  [{pos:05X}] {s!r}")

    # Screen/form names (DFM names)
    form_names = [(pos, s) for pos, s in strings
                  if s.endswith('.DFM') or re.match(r'^T7[A-Z]+', s)]
    print(f"\nForm/screen names: {len(form_names)}")
    for pos, s in form_names[:30]:
        print(f"  [{pos:05X}] {s!r}")

    # All strings for context
    print(f"\nAll strings (first 80):")
    for pos, s in strings[:80]:
        print(f"  [{pos:05X}] {s!r}")


if __name__ == '__main__':
    analyze_menufile()
    analyze_prgfile()
