"""
Test 05d -- Analyze one or two JSON scans for YN slot mappings.

Single-scan mode: finds ISTS.CFG keys whose current value uniquely
  identifies a single BKYSMSTR YN slot (same logic as Test 05c, but
  using saved JSON instead of live capture).

Two-scan mode: differential analysis -- for any ISTS.CFG key where the
  value DIFFERS between Scan A and Scan B, finds the YN slot where the
  SAME change occurred. These are definitive 1:1 mappings regardless of
  whether the values are common (Y/N/space).

Usage:
  # Single scan (unique-value matching only):
  python 05d-analyze.py scan-companyA.json

  # Two scans (differential + unique-value):
  python 05d-analyze.py scan-companyA.json scan-companyF.json

Output: sorted list of confirmed YN slot -> ISTS.CFG key mappings.
"""

import sys
import json


# Only entries confirmed via Frida unique-value matching.
# Source-derived entries (APCHK/DCSYNC/WOCALC etc.) were disproven 2026-07-08:
# their ists values do NOT match the claimed YN slots in live scan data.
KNOWN_SLOTS = {
    88:  ('GLCTRL', 'GL control flag (Frida 05c)'),
    105: ('WHCTRL', 'WH control flag (Frida 05c)'),
    201: ('APLANG', 'AP language code (Frida 05c)'),
}


def load(path):
    with open(path) as f:
        return json.load(f)


def yn_from_scan(scan):
    """Return 250-byte YN array from scan JSON."""
    hex_str = scan.get('yn_hex', '')
    if not hex_str or len(hex_str) < 500:
        raise ValueError(f'yn_hex too short ({len(hex_str)} chars)')
    return bytes.fromhex(hex_str[:500])


def single_analysis(scan, label='Scan A'):
    print(f'=== Single-scan analysis: {label} ===')
    yn   = yn_from_scan(scan)
    ists = scan.get('ists', {})

    # Build value -> slot list map
    val_to_slots = {}
    for slot, v in enumerate(yn):
        val_to_slots.setdefault(bytes([v]), []).append(slot)

    found = []
    for key, vh in ists.items():
        if len(vh) != 2:  # only 1-byte values
            continue
        val = bytes.fromhex(vh)
        slots = val_to_slots.get(val, [])
        if len(slots) == 1:
            slot = slots[0]
            known = KNOWN_SLOTS.get(slot)
            if known and known[0] != key:
                note = f'  [conflict: known={known[0]}]'
            else:
                note = ''
            found.append((slot, key, vh, note))

    found.sort()
    print(f'  {len(found)} unique 1:1 matches found:')
    for slot, key, vh, note in found:
        desc = KNOWN_SLOTS.get(slot, ('', ''))[1]
        print(f'    YN[{slot:3d}] = {key:<8}  val={vh}  {desc}{note}')
    return {slot: key for slot, key, vh, note in found}


def differential_analysis(scan_a, label_a, scan_b, label_b):
    print(f'=== Differential analysis: {label_a} vs {label_b} ===')
    yn_a  = yn_from_scan(scan_a)
    yn_b  = yn_from_scan(scan_b)
    ists_a = scan_a.get('ists', {})
    ists_b = scan_b.get('ists', {})

    # For each 1-byte key that differs between scans:
    # find the YN slot where yn_a[slot] == val_a AND yn_b[slot] == val_b
    diff_keys = []
    for key in ists_a:
        if key not in ists_b:
            continue
        va, vb = ists_a[key], ists_b[key]
        if va == vb or len(va) != 2 or len(vb) != 2:
            continue
        diff_keys.append((key, bytes.fromhex(va), bytes.fromhex(vb)))

    print(f'  Keys with differing 1-byte values: {len(diff_keys)}')

    found = []
    ambiguous = []
    for key, ba, bb in diff_keys:
        candidates = [
            slot for slot in range(250)
            if yn_a[slot:slot+1] == ba and yn_b[slot:slot+1] == bb
        ]
        if len(candidates) == 1:
            found.append((candidates[0], key, ba.hex(), bb.hex()))
        elif len(candidates) > 1:
            ambiguous.append((key, ba.hex(), bb.hex(), candidates))

    found.sort()
    print(f'  Definitive mappings: {len(found)}')
    for slot, key, va, vb in found:
        desc = KNOWN_SLOTS.get(slot, ('', ''))[1]
        print(f'    YN[{slot:3d}] = {key:<8}  A={va} B={vb}  {desc}')

    if ambiguous:
        print(f'  Ambiguous ({len(ambiguous)} keys with multiple candidate slots):')
        for key, va, vb, cands in ambiguous[:20]:
            print(f'    {key:<8}  A={va} B={vb}  candidates={cands}')

    return {slot: key for slot, key, va, vb in found}


def print_unknown_ists_keys(scan, known_map, label=''):
    """Show ISTS.CFG keys that are single-byte but still unresolved."""
    yn   = yn_from_scan(scan)
    ists = scan.get('ists', {})
    val_to_slots = {}
    for slot, v in enumerate(yn):
        val_to_slots.setdefault(bytes([v]), []).append(slot)

    known_keys = set(known_map.values())
    unresolved_keys = []
    for key, vh in ists.items():
        if len(vh) != 2:
            continue
        if key in known_keys:
            continue
        val = bytes.fromhex(vh)
        slots = val_to_slots.get(val, [])
        unresolved_keys.append((key, vh, len(slots)))

    unresolved_keys.sort(key=lambda x: x[2])  # fewest candidates first
    print(f'\n=== Unresolved 1-byte ISTS keys {label} (sorted by collision count) ===')
    for key, vh, n in unresolved_keys[:40]:
        print(f'  {key:<8}  val={vh}  ({n} slot candidates)')
    if len(unresolved_keys) > 40:
        print(f'  ... and {len(unresolved_keys)-40} more')


def pointer_analysis(scan, label='Scan'):
    """
    Compute YN slot for every ISTS.CFG key using the value-pointer addresses.

    Each ISTS.CFG entry's 'ptr' field holds the address in TAS Pro 7 memory where
    the runtime stores the value — which is BKYS.YN[N] for single-byte YN slots.
    Because YN is a contiguous array, slot = ptr - base, where base = ptr_of_known_key - known_slot.

    We anchor on at least two independently-known keys to verify consistency.
    """
    ists_ptr = scan.get('ists_ptr', {})
    if not ists_ptr:
        print(f'  [!] No pointer data in scan — re-run 05d-scan.py to capture pointers.')
        return {}

    # Anchor keys (confirmed slot → ISTS key name)
    anchors = {v[0]: k for k, v in KNOWN_SLOTS.items() if v[0] in ists_ptr}
    if len(anchors) < 2:
        print(f'  [!] Not enough anchor keys with pointers to compute base address.')
        return {}

    # Compute candidate base addresses from each anchor
    bases = {}
    for key, slot in anchors.items():
        ptr = ists_ptr[key]
        base = ptr - slot
        bases[key] = base

    # Check consistency: all anchors should agree on base
    base_vals = list(bases.values())
    ref_base = base_vals[0]
    consistent = all(b == ref_base for b in base_vals)
    print(f'\n=== Pointer-based slot analysis: {label} ===')
    print(f'  Pointer entries in scan: {len(ists_ptr)}')
    print(f'  Anchor keys used:')
    for key, slot in anchors.items():
        ptr = ists_ptr[key]
        base = ptr - slot
        match = 'OK' if base == ref_base else 'MISMATCH'
        print(f'    {key:<8}  ptr=0x{ptr:08x}  slot={slot}  base=0x{base:08x}  {match}')

    if not consistent:
        print('  [!] Base address inconsistency — YN array may not be contiguous. Aborting.')
        return {}

    base = ref_base
    print(f'  YN array base: 0x{base:08x}')

    # Compute slot for all pointer-having keys
    result = {}
    outside_yn = []
    for key, ptr in sorted(ists_ptr.items(), key=lambda x: x[1]):
        slot = ptr - base
        if 0 <= slot <= 249:
            result[slot] = key
        else:
            outside_yn.append((key, ptr, slot))

    print(f'  Mapped to YN[0..249]: {len(result)} keys')
    print(f'  Outside YN range:     {len(outside_yn)} keys (multi-byte or non-YN fields)')
    if outside_yn[:5]:
        for key, ptr, slot in outside_yn[:5]:
            print(f'    {key:<8}  ptr=0x{ptr:08x}  offset={slot}')
        if len(outside_yn) > 5:
            print(f'    ... and {len(outside_yn)-5} more')

    # Print the new mappings (not in KNOWN_SLOTS)
    new = {slot: key for slot, key in result.items() if slot not in KNOWN_SLOTS}
    print(f'\n  New mappings (not previously known): {len(new)}')
    for slot in sorted(new):
        print(f'    YN[{slot:3d}] = {new[slot]}')

    return result


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    path_a = sys.argv[1]
    path_b = sys.argv[2] if len(sys.argv) > 2 else None

    scan_a = load(path_a)
    label_a = path_a.rsplit('/', 1)[-1].rsplit('\\', 1)[-1]

    print(f'\nScan A: {path_a}')
    print(f'  YN hex length: {len(scan_a.get("yn_hex",""))} chars')
    print(f'  ISTS keys: {len(scan_a.get("ists",{}))}')
    print(f'  ISTS pointers: {len(scan_a.get("ists_ptr",{}))}')

    known = {}

    # Pointer-based analysis (works with a single scan if ptr data present)
    ptr_map = pointer_analysis(scan_a, label_a)
    if ptr_map:
        known.update(ptr_map)

    if path_b:
        scan_b = load(path_b)
        label_b = path_b.rsplit('/', 1)[-1].rsplit('\\', 1)[-1]
        print(f'\nScan B: {path_b}')
        print(f'  YN hex length: {len(scan_b.get("yn_hex",""))} chars')
        print(f'  ISTS keys: {len(scan_b.get("ists",{}))}')
        print(f'  ISTS pointers: {len(scan_b.get("ists_ptr",{}))}')
        print()

        diff_map  = differential_analysis(scan_a, label_a, scan_b, label_b)
        print()
        sing_map  = single_analysis(scan_a, label_a)
        known.update(sing_map)
        known.update(diff_map)   # differential takes precedence over single-scan
        print_unknown_ists_keys(scan_a, known, f'(after A+B analysis)')
    else:
        print()
        sing_map = single_analysis(scan_a, label_a)
        known.update(sing_map)
        print_unknown_ists_keys(scan_a, known, f'(single scan)')

    # Merge with KNOWN_SLOTS and print final summary
    all_known = dict(KNOWN_SLOTS)
    for slot, key in known.items():
        if slot not in all_known:
            all_known[slot] = (key, 'Frida 05d')
        else:
            existing_key = all_known[slot][0]
            if existing_key.endswith('?') or existing_key != key:
                all_known[slot] = (key, 'Frida 05d (updated)')

    print(f'\n=== Total confirmed slots (including pre-existing) ===')
    print(f'  {len(all_known)} slots with known ISTS.CFG keys')
    print(f'  {len(known)} new mappings found this analysis')
    unmapped = [s for s in range(250) if s not in all_known]
    print(f'  {len(unmapped)} slots still unknown')
    if unmapped:
        # Show unknown slots grouped
        print(f'  Unknown: {unmapped[:30]}{"..." if len(unmapped)>30 else ""}')


if __name__ == '__main__':
    main()
