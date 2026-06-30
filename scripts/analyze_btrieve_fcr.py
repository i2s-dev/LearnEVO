"""
Analyze the Btrieve File Control Record (FCR) byte layout.

The first page (page 0) of a Btrieve .B file is the FCR.
Page size varies but is stored in the FCR itself.
We read multiple known .B files and cross-reference known field values
against DDF metadata to build a complete FCR field map.

Known from prior passes:
- FCR[0x00..0x01] = b'FC' magic
- FCR[0x16..0x17] = logical record length (LE uint16)
- FCR[0x72..0x73] = physical record length (LE uint16)
- FCR[0x1C..0x1D] = page size (LE uint16)
- FCR[0x20..0x23] = record count (LE uint32)

We'll compare multiple files and DDF values to decode the other offsets.
"""
import struct
import pyodbc
from pathlib import Path
from collections import defaultdict

SAMPLES = Path(r"C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples")
NETWORK = Path(r"\\i2s109-solidcrm\DBAMFG$\Default")

# Files we have locally in samples/
LOCAL_FILES = [
    SAMPLES / "BKSLEVEL.B",
    SAMPLES / "BKSLMSTR.B",
    SAMPLES / "DBAHLPID.B",
    SAMPLES / "DBAHELP.B",
    SAMPLES / "BKSYUSER.B",
    SAMPLES / "errmsg.dbf",
]

# Files available on network that we know DDF info for
NETWORK_FILES = [
    ("BKARCUST",  "BKARCUST.B",  106, None),  # DDF: 106 fields
    ("BKARINV",   "BKARINV.B",   None, None),
    ("BKICMSTR",  "BKICMSTR.B",  64,  None),
    ("WORKORD",   "WORKORD.B",   74,  None),
    ("BKGLCOA",   "BKGLCOA.B",   65,  None),
    ("BKGLTRAN",  "BKGLTRAN.B",  None, None),
    ("AHSYLOG",   "AHSYLOG.B",   23,  27),     # DDF: 23f, record_size=27
    ("BKPSUSER",  "BKPSUSER.B",  11,  71),     # DDF: 11f, record_end=71
    ("ISEXUSER",  "ISEXUSER.B",  6,   83),     # DDF: 6f, offset(last)+size = 58+25=83
    ("ISACCESS",  "ISACCESS.B",  8,   275),    # DDF: 8f, 225+50=275
    ("ISJAVA",    "ISJAVA.B",    27,  2044),   # DDF: 27f, 2040+4=2044
    ("BKLOGON",   "BKLOGON.B",   10,  46),     # DDF: 10f, 44+2=46
]


def read_fcr(filepath):
    """Read FCR from first page of a Btrieve file."""
    try:
        with open(filepath, 'rb') as f:
            data = f.read(4096)  # Read up to 4KB
        if len(data) < 4 or data[:2] != b'FC':
            return None, None
        return data, len(data)
    except Exception as e:
        return None, None


def decode_fcr(data, name=""):
    """Decode known + guessed FCR fields."""
    def u16(off): return struct.unpack_from('<H', data, off)[0] if off+2 <= len(data) else None
    def u32(off): return struct.unpack_from('<I', data, off)[0] if off+4 <= len(data) else None
    def i16(off): return struct.unpack_from('<h', data, off)[0] if off+2 <= len(data) else None
    def u8(off): return data[off] if off < len(data) else None

    result = {
        'magic': data[0:2].decode('ascii', errors='?'),
        # Known fields
        'flags_0x02': u16(0x02),
        'flags_0x04': u16(0x04),
        'flags_0x06': u16(0x06),
        'record_count_0x08': u32(0x08),
        'free_page_0x0C': u32(0x0C),
        'root_index_0x10': u32(0x10),
        'key_specs_0x14': u16(0x14),
        'logical_rec_len_0x16': u16(0x16),
        'unknown_0x18': u16(0x18),
        'unknown_0x1A': u16(0x1A),
        'page_size_0x1C': u16(0x1C),
        'index_count_0x1E': u16(0x1E),
        'record_count_0x20': u32(0x20),
        'unknown_0x24': u16(0x24),
        'file_version_0x26': u16(0x26),
        'unknown_0x28': u32(0x28),
        'unused_pages_0x2C': u32(0x2C),
        'flags_0x30': u16(0x30),
        'unknown_0x32': u16(0x32),
        'unknown_0x34': u32(0x34),
        'unknown_0x38': u32(0x38),
        'unknown_0x3C': u32(0x3C),
        'unknown_0x40': u32(0x40),
        'unknown_0x44': u32(0x44),
        'unknown_0x48': u32(0x48),
        'unknown_0x4C': u32(0x4C),
        'unknown_0x50': u32(0x50),
        'unknown_0x54': u32(0x54),
        'unknown_0x58': u32(0x58),
        'unknown_0x5C': u32(0x5C),
        'unknown_0x60': u32(0x60),
        'unknown_0x64': u32(0x64),
        'unknown_0x68': u32(0x68),
        'unknown_0x6C': u32(0x6C),
        'unknown_0x70': u16(0x70),
        'physical_rec_len_0x72': u16(0x72),
        'unknown_0x74': u16(0x74),
        'unknown_0x76': u16(0x76),
        'unknown_0x78': u32(0x78),
        'unknown_0x7C': u32(0x7C),
    }
    return result


def main():
    # Get DDF logical record sizes via ODBC for cross-reference
    print("Connecting to DDF for record size data...")
    try:
        conn = pyodbc.connect("DSN=DBA", timeout=10)
        cur = conn.cursor()
        cur.execute("""
            SELECT Xf$Name, MAX(Xe$Offset + Xe$Size) as rec_size, COUNT(*) as field_count
            FROM X$File
            JOIN X$Field ON Xf$Id = Xe$File
            GROUP BY Xf$Name
            ORDER BY Xf$Name
        """)
        ddf_sizes = {r[0].strip(): (r[1], r[2]) for r in cur.fetchall()}
        conn.close()
        print(f"Got DDF record sizes for {len(ddf_sizes)} tables.")
    except Exception as e:
        print(f"DDF lookup failed: {e}")
        ddf_sizes = {}

    # Analyze network files
    print("\n=== FCR analysis for multiple .B files ===")
    print(f"{'Name':20} {'sz':6} {'pg_sz':6} {'log_rec':7} {'phy_rec':7} {'rcnt_08':9} {'rcnt_20':9} {'idx':4} {'fver':4} | DDF_sz DDF_flds")

    results = []

    # First do local files
    for fpath in LOCAL_FILES:
        if not fpath.exists():
            continue
        data, _ = read_fcr(fpath)
        if data is None:
            continue
        r = decode_fcr(data, fpath.stem)
        file_size = fpath.stat().st_size
        ddf = ddf_sizes.get(fpath.stem.upper(), ('?', '?'))
        results.append((fpath.stem, file_size, r, ddf))
        print(f"{fpath.stem:20} {file_size:6} {r.get('page_size_0x1C','?'):6} {r.get('logical_rec_len_0x16','?'):7} {r.get('physical_rec_len_0x72','?'):7} {r.get('record_count_0x08','?'):9} {r.get('record_count_0x20','?'):9} {r.get('index_count_0x1E','?'):4} {r.get('file_version_0x26','?'):4} | {ddf[0]} {ddf[1]}")

    # Network files
    for tname, fname, ddf_fields, ddf_recsize in NETWORK_FILES:
        fpath = NETWORK / fname
        if not fpath.exists():
            continue
        data, _ = read_fcr(fpath)
        if data is None:
            continue
        r = decode_fcr(data, tname)
        try:
            file_size = fpath.stat().st_size
        except:
            file_size = -1
        ddf = ddf_sizes.get(tname, (ddf_recsize or '?', ddf_fields or '?'))
        results.append((tname, file_size, r, ddf))
        print(f"{tname:20} {file_size:6} {r.get('page_size_0x1C','?'):6} {r.get('logical_rec_len_0x16','?'):7} {r.get('physical_rec_len_0x72','?'):7} {r.get('record_count_0x08','?'):9} {r.get('record_count_0x20','?'):9} {r.get('index_count_0x1E','?'):4} {r.get('file_version_0x26','?'):4} | {ddf[0]} {ddf[1]}")

    # Now analyze "unknown" fields to see which are consistent vs. varying
    print("\n=== Consistency analysis of 'unknown' FCR offsets ===")
    # Collect all unique values per offset
    offset_values = defaultdict(set)
    for name, sz, r, ddf in results:
        for k, v in r.items():
            if v is not None:
                offset_values[k].add(v)

    for k in sorted(offset_values.keys()):
        vals = offset_values[k]
        if len(vals) == 1:
            print(f"  {k:35}: CONSTANT = {list(vals)[0]}")
        elif len(vals) <= 4:
            print(f"  {k:35}: varies = {sorted(vals)}")
        else:
            print(f"  {k:35}: many values ({len(vals)} unique)")

    # Cross-validate: logical_rec_len_0x16 vs DDF record size
    print("\n=== Logical rec size vs DDF record end ===")
    for name, sz, r, ddf in results:
        log = r.get('logical_rec_len_0x16', '?')
        phy = r.get('physical_rec_len_0x72', '?')
        ddf_sz = ddf[0]
        if isinstance(log, int) and isinstance(ddf_sz, int):
            match = "OK" if log == ddf_sz else f"DIFF(DDF={ddf_sz})"
        else:
            match = f"DDF={ddf_sz}"
        overhead = (phy - log) if isinstance(phy, int) and isinstance(log, int) else '?'
        print(f"  {name:20}: log={log} phy={phy} overhead={overhead} {match}")

    print("\nDone.")


if __name__ == '__main__':
    main()
