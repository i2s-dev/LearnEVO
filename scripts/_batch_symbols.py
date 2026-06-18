"""
Batch-extract symbols from all .RWN files on the network share.
Outputs: samples/rwn_symbols.json  (full data)
         samples/rwn_symbols_summary.csv  (one row per file)
"""
import sys, struct, os, json, csv, traceback
sys.path.insert(0, 'scripts')
from twofish_pure import Twofish

K_B = bytes.fromhex('a898d21e2fd6ca294026e5d633d9047f91f7ed35')

RWN_ROOTS = [
    r'\\i2s109-solidcrm\DBAMFG$',
    r'C:\ISTS',
]
OUT_DIR = 'samples'

def decrypt_rwn(raw):
    tf = Twofish(K_B + b'\x00'*4)
    P_init = tf.encrypt(bytes(16))
    K0 = tf.encrypt(P_init)
    hp = bytes(a ^ b for a, b in zip(raw[0:8], K0[:8]))
    if hp[:4] != hp[4:]:
        return None
    P = K0
    result = bytearray()
    for i in range(0, len(raw[8:]), 16):
        blk = raw[8+i:8+i+16]
        K = tf.encrypt(P)
        result.extend(a ^ b for a, b in zip(blk, K))
        if len(blk) == 16:
            P = blk
    return bytes(result)

def read_file_table(data):
    names = []
    off = 0x80
    while off + 16 <= len(data):
        entry = data[off:off+16]
        if entry == b'\x00'*16:
            break
        n = entry.rstrip(b'\x00 ').decode('ascii', errors='replace')
        if n:
            names.append(n)
        off += 16
    return names

def extract(path):
    raw = open(path, 'rb').read()
    data = decrypt_rwn(raw)
    if data is None:
        return None

    def dw(off):
        return struct.unpack_from('<I', data, off)[0]

    hdr_0c = dw(0x0C)
    hdr_14 = dw(0x14)
    hdr_20 = dw(0x20)
    marker = data[0x35:0x3A].decode('ascii', errors='replace')

    var_table_off = len(data) - hdr_20
    src_off = var_table_off - 60
    proc_off = src_off - hdr_0c
    proc_count = hdr_0c // 53

    src = data[src_off:src_off+60].rstrip(b'\x00 ').decode('ascii', errors='replace')
    db_files = read_file_table(data)

    # Procedures
    procs = []
    for i in range(proc_count):
        off = proc_off + i * 53
        b0 = data[off]
        if 0 < b0 < 0x20:
            name = data[off+1:off+1+b0].decode('ascii', errors='replace')
            procs.append(name)
        elif b0 >= 0x20:
            name = data[off:off+15].rstrip(b'\x00 ').decode('ascii', errors='replace')
            procs.append(name)
        # else b0==0: no name available

    # Variables
    named_vars = []
    for i in range(hdr_14):
        off = var_table_off + i * 77
        if off + 77 > len(data):
            break
        b0 = data[off]
        if b0 < 0x20:
            name = data[off+1:off+15].rstrip(b'\x00 ').decode('ascii', errors='replace')
        else:
            name = data[off:off+15].rstrip(b'\x00 ').decode('ascii', errors='replace')
        if name and not name.startswith('TEMP'):
            named_vars.append(name)

    return {
        'path': path,
        'size': len(data),
        'marker': marker,
        'source_file': src,
        'db_files': db_files,
        'proc_count': proc_count,
        'procedures': procs,
        'var_count': hdr_14,
        'named_vars': named_vars,
    }

results = []
errors = []
seen = set()

for root in RWN_ROOTS:
    if not os.path.isdir(root):
        continue
    for dirpath, _, files in os.walk(root):
        for fname in files:
            if not fname.upper().endswith('.RWN'):
                continue
            fpath = os.path.join(dirpath, fname)
            key = fname.upper()
            if key in seen:
                continue
            seen.add(key)
            try:
                r = extract(fpath)
                if r:
                    results.append(r)
                    print(f"OK  {fname:40s}  procs={r['proc_count']:4d}  vars={r['var_count']:5d}  src={r['source_file']}")
                else:
                    errors.append({'path': fpath, 'error': 'decrypt fail'})
                    print(f"ERR {fname}")
            except Exception as e:
                errors.append({'path': fpath, 'error': str(e)})
                print(f"ERR {fname}: {e}")

print(f"\nProcessed: {len(results)} OK, {len(errors)} errors")

# Save JSON
out_json = os.path.join(OUT_DIR, 'rwn_symbols.json')
with open(out_json, 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2, ensure_ascii=False)
print(f"Saved: {out_json}")

# Save CSV summary
out_csv = os.path.join(OUT_DIR, 'rwn_symbols_summary.csv')
with open(out_csv, 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['filename', 'size', 'source_file', 'proc_count', 'procs_named',
                'var_count', 'named_var_count', 'db_file_count', 'db_files_sample'])
    for r in results:
        w.writerow([
            os.path.basename(r['path']),
            r['size'],
            r['source_file'],
            r['proc_count'],
            len(r['procedures']),
            r['var_count'],
            len(r['named_vars']),
            len(r['db_files']),
            ';'.join(r['db_files'][:5]),
        ])
print(f"Saved: {out_csv}")
