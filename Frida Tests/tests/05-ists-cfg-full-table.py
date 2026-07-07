"""
Test 05 -- ISTS.CFG Full Table Walker

Strategy:
  1. Hook BTRCALLID. When BKYSMSTR (1045-byte record) is returned, set a flag.
  2. A memory-scan timer fires 800ms later. Scans ALL readable process memory
     for 'ISTS.CFG.' patterns, collects addresses, finds runs of consecutive
     entries spaced exactly 77 bytes apart (the ISTS.CFG table).
  3. Dumps every entry in the winning run in table order.
  4. Cross-references with known YN slot->key pairs to anchor the mapping.

This must be started BEFORE EvoERP launches (pre-attach pattern).

Usage:
  python tests/05-ists-cfg-full-table.py --log logs/test05.txt
"""

import frida, sys, time, argparse, os

PROC_NAME = 'evoerp.exe'

KNOWN_SLOTS = {
    38:  'WOCALC',
    48:  'APCHK',
    65:  'STDCST',
    228: 'DCSEQ',
    229: 'DCSYNC',
}

SCRIPT = r"""
'use strict';

var ENTRY_STRIDE = 77;
var PREFIX       = 'ISTS.CFG.';
var PREFIX_LEN   = 9;
var KEY_FIELD    = 6;   // key padded to 6 bytes within entry

// --- Helpers ----------------------------------------------------------------

function findExport(name) {
    var mods = Process.enumerateModules();
    for (var i = 0; i < mods.length; i++) {
        var a = mods[i].findExportByName(name);
        if (a !== null) return {addr: a, mod: mods[i].name};
    }
    return null;
}

function readKey(ptr) {
    // Read up to KEY_FIELD bytes, strip trailing spaces/nulls
    try {
        var b = new Uint8Array(ptr.readByteArray(KEY_FIELD));
        var s = '';
        for (var i = 0; i < KEY_FIELD; i++) {
            var c = b[i];
            if (c === 0 || c === 32) break;
            if (c < 65 || (c > 90 && c < 48) || c > 90) return null; // must be A-Z or 0-9
            s += String.fromCharCode(c);
        }
        return s.length >= 2 ? s : null;
    } catch(e) { return null; }
}

function verifyPrefix(ptr) {
    try {
        var b = new Uint8Array(ptr.readByteArray(PREFIX_LEN));
        var s = '';
        for (var i = 0; i < b.length; i++) {
            s += String.fromCharCode(b[i]);
        }
        return s === PREFIX;
    } catch(e) { return false; }
}

// --- Memory scanner ---------------------------------------------------------

function scanForIstsTable() {
    send({event:'scan_start'});
    var hits = [];

    try {
        Process.enumerateRanges('r--').forEach(function(range) {
            try {
                var size = range.size;
                if (size < 77) return;
                // Cap scan per range to avoid huge reads
                var scanSize = Math.min(size, 4 * 1024 * 1024);  // 4MB max per range

                var base = range.base;
                var data = base.readByteArray(scanSize);
                if (!data) return;
                var buf = new Uint8Array(data);

                for (var i = 0; i + PREFIX_LEN + KEY_FIELD < buf.length; i++) {
                    // Quick pre-filter: first byte 'I' (0x49)
                    if (buf[i] !== 0x49) continue;
                    // Check 'ISTS.CFG.'
                    if (buf[i+1]!==0x53||buf[i+2]!==0x54||buf[i+3]!==0x53) continue;
                    if (buf[i+4]!==0x2e||buf[i+5]!==0x43||buf[i+6]!==0x46) continue;
                    if (buf[i+7]!==0x47||buf[i+8]!==0x2e) continue;
                    // Extract key (up to 6 printable uppercase chars)
                    var key = '';
                    for (var k = 0; k < KEY_FIELD; k++) {
                        var c = buf[i + PREFIX_LEN + k];
                        if (c === 0 || c === 32) break;
                        if (!((c >= 65 && c <= 90) || (c >= 48 && c <= 57))) {
                            key = null;
                            break;
                        }
                        key += String.fromCharCode(c);
                    }
                    if (key && key.length >= 2) {
                        hits.push({addr: base.add(i).toString(), key: key});
                    }
                }
            } catch(e) {}
        });
    } catch(e) {
        send({event:'scan_error', msg: e.toString()});
        return;
    }

    send({event:'scan_raw', count: hits.length, hits: hits});
}

// --- BTRCALLID hook ---------------------------------------------------------

var bkysmstrSeen  = false;
var scanScheduled = false;

var READ_OPS = {5:1, 6:1, 7:1, 12:1, 13:1};

function hookBtrv() {
    var btrcallid = findExport('BTRCALLID');
    if (!btrcallid) return false;
    send({event:'hook_ok', name:'BTRCALLID', mod: btrcallid.mod});

    Interceptor.attach(btrcallid.addr, {
        onEnter: function(args) {
            try {
                var op = this.context.esp.add(4).readU16();
                if (!(op in READ_OPS)) return;
                this.isRead = true;
                this.dataLenPtr = this.context.esp.add(16).readPointer();
            } catch(e) {}
        },
        onLeave: function(retval) {
            try {
                if (!this.isRead) return;
                if (retval.toInt32() !== 0) return;
                var dataLen = 0;
                try { dataLen = this.dataLenPtr.readU16(); } catch(e) { return; }

                // BKYSMSTR: 1045 bytes
                if (dataLen === 1045 && !bkysmstrSeen) {
                    bkysmstrSeen = true;
                    send({event:'bkysmstr_seen'});

                    if (!scanScheduled) {
                        scanScheduled = true;
                        // Scan 800ms after BKYSMSTR: EVO has time to build the table
                        setTimeout(scanForIstsTable, 800);
                    }
                }
            } catch(e) {}
        }
    });
    return true;
}

var hooked = hookBtrv();
if (!hooked) {
    send({event:'polling'});
    var pollTimer = setInterval(function() {
        if (hookBtrv()) clearInterval(pollTimer);
    }, 500);
}

// Manual trigger support
recv('scan_now', function(_) {
    if (!scanScheduled) {
        scanScheduled = true;
        scanForIstsTable();
    }
});

send({event:'ready'});
"""


def find_table_runs(hits):
    """
    Given a list of {addr: '0x...', key: str}, sort by address,
    find the longest run where consecutive entries are exactly 77 bytes apart.
    Returns a list of (index, key, addr_int) tuples for the winning run.
    """
    STRIDE = 77
    if not hits:
        return []

    # Parse addresses
    parsed = []
    for h in hits:
        try:
            parsed.append((int(h['addr'], 16), h['key']))
        except Exception:
            pass
    parsed.sort(key=lambda x: x[0])

    # Deduplicate by address (keep first key at each address)
    deduped = []
    seen_addrs = set()
    for addr, key in parsed:
        if addr not in seen_addrs:
            seen_addrs.add(addr)
            deduped.append((addr, key))

    # Find all runs with stride == 77
    best_run = []
    i = 0
    while i < len(deduped):
        run = [deduped[i]]
        j = i + 1
        while j < len(deduped):
            gap = deduped[j][0] - run[-1][0]
            if gap == STRIDE:
                run.append(deduped[j])
                j += 1
            elif gap < STRIDE:
                j += 1  # skip duplicates/noise inside run
            else:
                break
        if len(run) > len(best_run):
            best_run = run
        i += 1

    # Assign indices
    result = []
    for idx, (addr, key) in enumerate(best_run):
        result.append((idx, key, addr))
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--log', required=True)
    args = parser.parse_args()

    os.makedirs(os.path.dirname(args.log) if os.path.dirname(args.log) else '.', exist_ok=True)
    log_f = open(args.log, 'w', buffering=1)

    def emit(line):
        print(line)
        log_f.write(line + '\n')

    emit('TEST 05 - ISTS.CFG Full Table Walker')
    emit('=' * 60)
    emit(f'Log: {args.log}')
    emit('')

    finished = [False]
    script_ref = [None]

    def on_message(msg, data):
        if msg['type'] == 'error':
            emit(f'[FRIDA ERROR] {msg["description"]}')
            finished[0] = True
            return
        if msg['type'] != 'send':
            return
        p  = msg['payload']
        ev = p.get('event', '')

        if ev == 'hook_ok':
            emit(f'[+] Hooked BTRCALLID in {p["mod"]}')
        elif ev == 'polling':
            emit('[~] Waiting for w3btrv7.dll to load...')
        elif ev == 'ready':
            emit('[+] Script ready. Launch EvoERP now.')
            emit('    Log in -- scan fires 800ms after BKYSMSTR is read.')
            emit('')
        elif ev == 'bkysmstr_seen':
            emit('[+] BKYSMSTR detected! Scan scheduled in 800ms...')
        elif ev == 'scan_start':
            emit('[*] Scanning all process memory for ISTS.CFG. entries...')
        elif ev == 'scan_error':
            emit(f'[!] Scan error: {p["msg"]}')
        elif ev == 'scan_raw':
            count = p['count']
            hits  = p['hits']
            emit(f'[+] Raw scan: {count} ISTS.CFG. patterns found')
            emit('')

            runs = find_table_runs(hits)

            if not runs:
                emit('[!] No consecutive 77-byte run found. Table may have been freed.')
                emit('    Try running Test 05 again -- the scan must fire sooner.')
                finished[0] = True
                return

            emit(f'[+] Longest consecutive run: {len(runs)} entries (stride=77)')
            emit('')

            # Cross-reference with known slot mappings
            key_to_idx  = {key: idx for idx, key, _ in runs}
            key_to_addr = {key: addr for _, key, addr in runs}

            emit('=== KNOWN SLOT ANCHORS ===')
            known_found = {}
            for slot, key in sorted(KNOWN_SLOTS.items()):
                if key in key_to_idx:
                    tbl_idx = key_to_idx[key]
                    emit(f'  YN[{slot:3d}] = {key:8s}  -> table[{tbl_idx:4d}]  @ 0x{key_to_addr[key]:08x}')
                    known_found[slot] = (key, tbl_idx)
                else:
                    emit(f'  YN[{slot:3d}] = {key:8s}  -> NOT IN TABLE (key missing from run)')
            emit('')

            # Compute slot = f(table_index) if we have >=2 anchors with consistent offset
            if len(known_found) >= 2:
                offsets = []
                for slot, (key, tbl_idx) in known_found.items():
                    offsets.append(slot - tbl_idx)
                # Check if a single offset works
                if len(set(offsets)) == 1:
                    off = offsets[0]
                    emit(f'[+] CONSISTENT OFFSET: slot = table_index + {off}')
                    emit('    This means we can map ALL table entries to YN slots!')
                    emit('')
                else:
                    emit(f'[~] Mixed offsets: {offsets} -- no single linear mapping')
                    emit('')

            # Dump full table
            emit(f'=== FULL TABLE ({len(runs)} entries) ===')
            emit(f'  {"Tbl":>5}  {"Key":<8}  {"Addr":>12}  {"YN":>6}')
            emit(f'  {"---":>5}  {"---":<8}  {"----":>12}  {"--":>6}')
            for idx, key, addr in runs:
                yn_str = ''
                for slot, (k, _) in known_found.items():
                    if k == key:
                        yn_str = f'YN[{slot}]'
                emit(f'  {idx:5d}  {key:<8}  0x{addr:08x}  {yn_str}')

            emit('')
            emit(f'Total entries mapped: {len(runs)}')
            emit(f'Total ISTS.CFG keys known from .RWN files: 542')
            finished[0] = True

    emit(f'[*] Waiting for {PROC_NAME}...')
    session = None
    while session is None:
        try:
            session = frida.attach(PROC_NAME)
        except frida.ProcessNotFoundError:
            time.sleep(0.25)

    emit(f'[+] Attached to {PROC_NAME}')
    script = session.create_script(SCRIPT)
    script.on('message', on_message)
    script.load()
    script_ref[0] = script

    # Also handle manual trigger from stdin
    try:
        for _ in range(2400):   # 20-minute max
            if finished[0]:
                break
            time.sleep(0.5)
    except KeyboardInterrupt:
        emit('[!] Interrupted -- requesting manual scan now.')
        script.post({'type': 'scan_now'})
        for _ in range(60):
            if finished[0]:
                break
            time.sleep(0.5)

    log_f.close()
    input('\nPress ENTER to close...')


if __name__ == '__main__':
    main()
