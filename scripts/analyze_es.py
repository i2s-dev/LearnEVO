import sys, struct, os, glob
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

PROC_ENTRY_SIZE = 53
VAR_ENTRY_SIZE  = 77
SRCNAME_SIZE    = 60
HEADER_SIZE     = 128  # 0x80
FILE_TABLE_OFF  = 0x80
FILE_ENTRY_SIZE = 16

def dw(data, off):
    return struct.unpack_from("<I", data, off)[0]

def parse_var_name(data, entry_off):
    """Extract var name handling type-byte prefix (byte 0 < 0x20 = type code, name at byte 1)."""
    type_byte = data[entry_off]
    if type_byte < 0x20:
        raw = data[entry_off+1:entry_off+15]
    else:
        raw = data[entry_off:entry_off+15]
    return raw.rstrip(b"\x00 ").decode("ascii", errors="replace"), type_byte

def extract_all(path):
    raw = open(path, "rb").read()
    # .dec files include 8-byte validation prefix followed by decrypted body
    if len(raw) >= 8 and raw[0:4] == raw[4:8]:
        data = raw[8:]  # strip validation prefix
    else:
        data = raw
    if len(data) < HEADER_SIZE:
        return {}

    proc_table_size = dw(data, 0x0C)
    var_count       = dw(data, 0x14)
    var_table_size  = dw(data, 0x20)

    proc_count = proc_table_size // PROC_ENTRY_SIZE if proc_table_size >= PROC_ENTRY_SIZE else 0
    var_table_off = len(data) - var_table_size
    src_off       = var_table_off - SRCNAME_SIZE
    proc_off      = src_off - proc_table_size

    # Source filename
    src_name = data[src_off:src_off+SRCNAME_SIZE].rstrip(b"\x00 ").decode("ascii", errors="replace") if src_off >= 0 else ""

    # File reference table at 0x80
    db_files = []
    off = FILE_TABLE_OFF
    while off + FILE_ENTRY_SIZE <= len(data):
        entry = data[off:off+FILE_ENTRY_SIZE]
        if entry == b"\x00" * FILE_ENTRY_SIZE:
            break
        name = entry.rstrip(b"\x00 ").decode("ascii", errors="replace")
        if name:
            db_files.append(name)
        off += FILE_ENTRY_SIZE

    # Variable names (using correct entry format)
    vars_named = []  # non-TEMP named vars
    all_names = []
    for i in range(var_count):
        entry_off = var_table_off + i * VAR_ENTRY_SIZE
        if entry_off + VAR_ENTRY_SIZE > len(data):
            break
        name, type_byte = parse_var_name(data, entry_off)
        all_names.append(name)
        if name and not name.startswith("TEMP"):
            vars_named.append(name)

    # Procedure names
    procs_out = []
    for i in range(proc_count):
        off = proc_off + i * PROC_ENTRY_SIZE
        if off < 0 or off + PROC_ENTRY_SIZE > len(data):
            break
        name_len = data[off]
        raw_name = data[off+1:off+1+min(name_len, 15)]
        procs_out.append(raw_name.decode("ascii", errors="replace").rstrip("\x00"))

    return {
        "proc_count": proc_count,
        "var_count": var_count,
        "src_name": src_name,
        "db_files": db_files,
        "vars_named": vars_named,
        "all_names": all_names,
        "procs": procs_out,
    }

base = "samples/rwn_decrypted/"
files = sorted(glob.glob(base + "T7ES*.dec") + glob.glob(base + "t7es*.dec"))
seen = set()
uniq = []
for f in files:
    k = os.path.basename(f).lower()
    if k not in seen:
        seen.add(k)
        uniq.append(f)

for f in uniq:
    fname = os.path.basename(f)
    info = extract_all(f)
    if not info:
        print(f"\n=== {fname} — PARSE FAILED ===")
        continue
    named = info["vars_named"]
    prefixes = Counter()
    for v in named:
        p = v.split(".")[0] if "." in v else v[:8]
        prefixes[p] += 1
    print(f"\n=== {fname} ({info['proc_count']}p, {info['var_count']}v, {len(named)} non-TEMP, src={info['src_name']}) ===")
    print(f"  DB files ({len(info['db_files'])}): {info['db_files']}")
    print(f"  Procs: {[p for p in info['procs'] if p.strip()][:15]}")
    print(f"  Non-TEMP prefix dist: {dict(prefixes.most_common(15))}")
    # Filter to non-TEMP named vars beyond the common library block
    unique_vars = [v for v in named if not v.startswith(("ISTS.CFG", "EMAIL.CFG", "EVO.CFG", "BKAR.IS", "BKAR.GROSS",
                                                           "HOTBUTTON", "MKAHIST", "ARA.", "APA.", "INA.", "INB.",
                                                           "SOA.", "POA.", "WOA.", "CFG.", "DEFPRINT", "XCPATH",
                                                           "WEBLINK", "JAVA.", "HOST", "PORT", "NAME", "COMP",
                                                           "TREEDEST", "RVAL", "DFM", "NOPE", "DUMMY", "ISTS.ED"))]
    print(f"  Module-specific vars ({len(unique_vars)}): {unique_vars[:50]}")
