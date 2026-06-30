"""
Catalog all RTM report templates on the network share, grouped by module code.

RTM naming convention (observed):
  T6XXY1.RTM   = TAS Pro 6 era, module XX, operation Y, variant 1
  T7XXY.RTM    = TAS Pro 7 era, module XX, operation Y
  BKxxxx.RTM   = BK-prefix legacy reports
  J7xxx.RTM    = J7 custom (i2 Systems extensions)
  Other.RTM    = custom names (evonotesrpt, etc.)

Goal:
  1. List all RTM files
  2. Extract module code from filename
  3. Group by module and count
  4. Cross-reference with BKMENUSU module list
"""
import os
import re
import csv
from pathlib import Path
from collections import defaultdict

NETWORK = Path(r"\\i2s109-solidcrm\DBAMFG$")
SAMPLES = Path(r"C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples")

# Load module names for cross-reference
module_names = {}
try:
    with open(SAMPLES / 'module_names.csv', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            module_names[row['module_code']] = row['full_name']
except FileNotFoundError:
    pass


def classify_rtm(name):
    """Classify an RTM filename into generation + module code."""
    stem = name.upper().replace('.RTM', '').replace('.BTM', '')

    # T7XX*.RTM pattern
    m = re.match(r'^T7([A-Z]{2})', stem)
    if m:
        return 'T7', m.group(1)

    # T6XX*.RTM pattern
    m = re.match(r'^T6([A-Z]{2})', stem)
    if m:
        return 'T6', m.group(1)

    # J7XX*.RTM pattern
    m = re.match(r'^J7([A-Z]{2})', stem)
    if m:
        return 'J7', m.group(1)

    # BKXX*.RTM pattern
    m = re.match(r'^BK([A-Z]{2})', stem)
    if m:
        return 'BK', m.group(1)

    # Any other
    return 'Other', stem[:6]


def scan_rtm_files():
    """Walk DBAMFG$ looking for .RTM files."""
    rtm_files = []
    try:
        for root, dirs, files in os.walk(NETWORK):
            # Skip company-specific data folders (they have .B data files)
            # Stay in the root level
            for fname in files:
                if fname.upper().endswith('.RTM') or fname.upper().endswith('.BTM'):
                    rel = os.path.relpath(os.path.join(root, fname), NETWORK)
                    rtm_files.append((rel, fname))
            # Only go 2 levels deep
            depth = rel.count(os.sep) if 'rel' in dir() else 0
            if depth >= 1:
                dirs[:] = []
    except Exception as e:
        print(f"Walk error: {e}")
    return rtm_files


def main():
    print("Scanning RTM files on network share...")
    rtm_files = scan_rtm_files()

    if not rtm_files:
        # Try listing just top level
        print("Walk failed, trying direct glob...")
        try:
            rtm_files = [(f.name, f.name) for f in NETWORK.glob('*.RTM')]
            rtm_files += [(f.name, f.name) for f in NETWORK.glob('*.rtm')]
            rtm_files += [(f.name, f.name) for f in NETWORK.glob('*.btm')]
            rtm_files += [(f.name, f.name) for f in NETWORK.glob('*.BTM')]
        except Exception as e:
            print(f"Glob error: {e}")

    print(f"Total RTM/BTM files found: {len(rtm_files)}")

    # Classify each
    by_gen = defaultdict(list)
    by_module = defaultdict(list)
    classified = []
    for rel, fname in rtm_files:
        gen, mod = classify_rtm(fname)
        by_gen[gen].append((rel, fname, mod))
        by_module[mod].append((rel, fname, gen))
        classified.append({'file': fname, 'path': rel, 'gen': gen, 'module': mod})

    # Print generation summary
    print(f"\nBy generation:")
    for gen in sorted(by_gen.keys()):
        print(f"  {gen}: {len(by_gen[gen])} files")

    # Print by module (known modules only)
    print(f"\nRTM files by known module:")
    known_modules = set(module_names.keys())
    for mod in sorted(known_modules):
        files = by_module.get(mod, [])
        if files:
            name = module_names.get(mod, '?')
            t6 = sum(1 for f in files if f[2]=='T6')
            t7 = sum(1 for f in files if f[2]=='T7')
            bk = sum(1 for f in files if f[2]=='BK')
            j7 = sum(1 for f in files if f[2]=='J7')
            print(f"  {mod} ({name:35}): total={len(files):3} T6={t6:3} T7={t7:3} BK={bk:2} J7={j7:2}")

    # Print modules that have RTMs but aren't in known list
    unknown_mods = set(by_module.keys()) - known_modules
    if unknown_mods:
        print(f"\nRTM files for unknown module codes:")
        for mod in sorted(unknown_mods):
            files = by_module[mod]
            print(f"  {mod}: {len(files)} files — {[f[1] for f in files[:5]]}")

    # Save to CSV
    out_path = SAMPLES / 'rtm_by_module.csv'
    with open(out_path, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=['file', 'path', 'gen', 'module', 'module_name'])
        w.writeheader()
        for row in classified:
            row['module_name'] = module_names.get(row['module'], '')
            w.writerow(row)
    print(f"\nSaved {len(classified)} rows to {out_path}")


if __name__ == '__main__':
    main()
