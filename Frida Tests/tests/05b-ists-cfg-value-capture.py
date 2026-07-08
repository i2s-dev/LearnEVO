"""
Test 05b -- ISTS.CFG Value Capture + BKYSMSTR Correlation

Strategy:
  1. Hook BTRCALLID. When BKYSMSTR (1045-byte record) is returned, capture
     the full record (YN[0..249] = bytes 8..257).
  2. Wait for a MANUAL trigger file (user presses Enter in run-tests after
     login is fully complete so ALL ISTS.CFG entries are populated).
  3. Scan all process memory for 'ISTS.CFG.' patterns at 77-byte stride.
     For each entry: capture key + bytes 15..44 of the entry (value area).
  4. Python: correlate BKYSMSTR slot values with ISTS.CFG entry values
     to find slot -> key mappings.

Output: two blocks
  BKYSMSTR  -- YN[0..249] as hex bytes
  TABLE     -- table_index, key, value_hex (bytes 15..44)

Usage:
  python tests/05b-ists-cfg-value-capture.py --log logs/test05b.txt --trigger <path>
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

var ENTRY_STRIDE   = 77;
var PREFIX         = 'ISTS.CFG.';
var PREFIX_LEN     = 9;
var KEY_FIELD      = 6;
var VALUE_OFFSET   = 15;   // bytes 15..44 after entry start contain value/metadata
var VALUE_LEN      = 30;

var READ_OPS = {5:1, 6:1, 7:1, 12:1, 13:1};

// --- helpers ----------------------------------------------------------------

function findExport(name) {
    var mods = Process.enumerateModules();
    for (var i = 0; i < mods.length; i++) {
        var a = mods[i].findExportByName(name);
        if (a !== null) return {addr: a, mod: mods[i].name};
    }
    return null;
}

function bytesToHex(buf, offset, len) {
    var s = '';
    for (var i = 0; i < len; i++) {
        var b = buf[offset + i];
        if (b === undefined) break;
        var h = b.toString(16);
        s += (h.length < 2 ? '0' : '') + h;
    }
    return s;
}

function bytesToAscii(buf, offset, len) {
    var s = '';
    for (var i = 0; i < len; i++) {
        var b = buf[offset + i];
        if (b === undefined) break;
        s += (b >= 0x20 && b < 0x7f) ? String.fromCharCode(b) : '.';
    }
    return s;
}

// --- State ------------------------------------------------------------------

var bkysmstrHex  = null;   // hex string of BKYSMSTR[0..1044]
var bkysmstrData = null;   // Uint8Array[0..249] = YN values

// --- Memory scanner ---------------------------------------------------------

function scanForIstsTable() {
    send({event:'scan_start'});
    var hits = [];

    try {
        Process.enumerateRanges('r--').forEach(function(range) {
            try {
                var size = range.size;
                if (size < ENTRY_STRIDE) return;
                var scanSize = Math.min(size, 4 * 1024 * 1024);

                var base  = range.base;
                var raw   = base.readByteArray(scanSize);
                if (!raw) return;
                var buf = new Uint8Array(raw);

                for (var i = 0; i + PREFIX_LEN + KEY_FIELD + VALUE_LEN < buf.length; i++) {
                    // Quick pre-filter: 'I' 'S' 'T' 'S' '.' 'C' 'F' 'G' '.'
                    if (buf[i]!==0x49||buf[i+1]!==0x53||buf[i+2]!==0x54||buf[i+3]!==0x53) continue;
                    if (buf[i+4]!==0x2e||buf[i+5]!==0x43||buf[i+6]!==0x46||buf[i+7]!==0x47||buf[i+8]!==0x2e) continue;

                    // Extract key
                    var key = '';
                    for (var k = 0; k < KEY_FIELD; k++) {
                        var c = buf[i + PREFIX_LEN + k];
                        if (c === 0 || c === 32) break;
                        if (!((c >= 65 && c <= 90) || (c >= 48 && c <= 57))) { key = null; break; }
                        key += String.fromCharCode(c);
                    }
                    if (!key || key.length < 2) continue;

                    // Capture value bytes (bytes VALUE_OFFSET..VALUE_OFFSET+VALUE_LEN from entry start)
                    var valHex   = bytesToHex(buf,   i + VALUE_OFFSET, VALUE_LEN);
                    var valAscii = bytesToAscii(buf, i + VALUE_OFFSET, VALUE_LEN);

                    hits.push({
                        addr:    base.add(i).toString(),
                        key:     key,
                        valHex:  valHex,
                        valAsc:  valAscii
                    });
                }
            } catch(e) {}
        });
    } catch(e) {
        send({event:'scan_error', msg: e.toString()});
        return;
    }

    send({event:'scan_raw', count: hits.length, hits: hits,
          bkysmstr: bkysmstrHex});
}

// --- BTRCALLID hook ---------------------------------------------------------

var bkysmstrSeen = false;

function hookBtrv() {
    var btrcallid = findExport('BTRCALLID');
    if (!btrcallid) return false;
    send({event:'hook_ok', name:'BTRCALLID', mod: btrcallid.mod});

    Interceptor.attach(btrcallid.addr, {
        onEnter: function(args) {
            try {
                var op = this.context.esp.add(4).readU16();
                if (!(op in READ_OPS)) return;
                this.isRead    = true;
                this.dataBuf   = this.context.esp.add(12).readPointer();
                this.dataLenPtr = this.context.esp.add(16).readPointer();
            } catch(e) {}
        },
        onLeave: function(retval) {
            try {
                if (!this.isRead) return;
                if (retval.toInt32() !== 0) return;
                var dataLen = 0;
                try { dataLen = this.dataLenPtr.readU16(); } catch(e) { return; }

                if (dataLen === 1045 && !bkysmstrSeen) {
                    bkysmstrSeen = true;
                    // Read full record
                    try {
                        var raw  = this.dataBuf.readByteArray(1045);
                        var buf  = new Uint8Array(raw);
                        var hex  = '';
                        for (var i = 0; i < 1045; i++) {
                            var h = buf[i].toString(16);
                            hex += (h.length < 2 ? '0' : '') + h;
                        }
                        bkysmstrHex  = hex;
                        bkysmstrData = buf;
                        send({event:'bkysmstr_seen', hex: hex.slice(0, 520)}); // send first 260 bytes = YN[0..249]
                    } catch(e) {
                        send({event:'bkysmstr_seen', hex: null, err: e.toString()});
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

recv('scan_now', function(_) { scanForIstsTable(); });
send({event:'ready'});
"""


def find_table_run(hits):
    """Sort by address, find longest run with 77-byte stride."""
    STRIDE = 77
    parsed = []
    for h in hits:
        try:
            parsed.append((int(h['addr'], 16), h['key'], h.get('valHex', ''), h.get('valAsc', '')))
        except Exception:
            pass
    parsed.sort(key=lambda x: x[0])

    seen_addrs = {}
    deduped = []
    for addr, key, vh, va in parsed:
        if addr not in seen_addrs:
            seen_addrs[addr] = True
            deduped.append((addr, key, vh, va))

    best = []
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
                j += 1
            else:
                break
        if len(run) > len(best):
            best = run
        i += 1

    return [(idx, addr, key, vh, va) for idx, (addr, key, vh, va) in enumerate(best)]


def correlate(table_run, bkysmstr_hex):
    """
    For each ISTS.CFG table entry, find the BKYSMSTR slot whose value
    matches the value byte in the entry.

    Returns: list of (table_idx, key, yn_slot_candidates, value_byte)
    """
    if not bkysmstr_hex or len(bkysmstr_hex) < 520:
        return []

    # BKYSMSTR bytes 8..257 = YN[0..249]
    bkysmstr_bytes = bytes.fromhex(bkysmstr_hex)
    yn = bkysmstr_bytes[8:258]   # 250 bytes = YN[0..249]

    # Build slot -> value map and value -> slots map
    val_to_slots = {}
    for slot, v in enumerate(yn):
        val_to_slots.setdefault(v, []).append(slot)

    results = []
    for idx, addr, key, val_hex, val_asc in table_run:
        if not val_hex or len(val_hex) < 2:
            results.append((idx, key, [], None))
            continue

        # Try each byte position 0..14 within the VALUE_LEN window
        # looking for a byte that appears in yn
        candidates_by_pos = {}
        for pos in range(min(15, len(val_hex) // 2)):
            byte_val = int(val_hex[pos*2:pos*2+2], 16)
            if byte_val in val_to_slots:
                candidates_by_pos[pos] = (byte_val, val_to_slots[byte_val])

        results.append((idx, key, candidates_by_pos, val_hex))

    return results, yn


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--log',     required=True)
    parser.add_argument('--trigger', default='',
                        help='Trigger file path -- when created, scan fires immediately.')
    args = parser.parse_args()

    if os.path.dirname(args.log):
        os.makedirs(os.path.dirname(args.log), exist_ok=True)
    log_f = open(args.log, 'w', buffering=1)

    def emit(line):
        print(line)
        log_f.write(line + '\n')

    emit('TEST 05b - ISTS.CFG Value Capture')
    emit('=' * 60)
    emit(f'Log: {args.log}')
    emit(f'Trigger: {args.trigger or "(none)"}')
    emit('')

    finished    = [False]
    scan_sent   = [False]
    script_ref  = [None]
    bkysmstr_hex = [None]

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
            emit('[~] Waiting for w3btrv7.dll...')
        elif ev == 'ready':
            emit('[+] Script ready. Launch EvoERP.')
            emit('    Log in fully, then trigger the scan.')
            emit('')
        elif ev == 'bkysmstr_seen':
            bkysmstr_hex[0] = p.get('hex')
            emit('[+] BKYSMSTR captured!')
            if bkysmstr_hex[0]:
                # Decode YN[0..249] = bytes 8..257 of BKYSMSTR (= hex chars 16..515)
                raw = bytes.fromhex(bkysmstr_hex[0])
                yn = raw[8:258]
                emit(f'    YN[  0- 24]: {yn[0:25].decode("latin1", errors="replace")}')
                emit(f'    YN[ 25- 49]: {yn[25:50].decode("latin1", errors="replace")}')
                emit(f'    YN[ 50- 74]: {yn[50:75].decode("latin1", errors="replace")}')
                emit(f'    YN[ 75- 99]: {yn[75:100].decode("latin1", errors="replace")}')
                emit(f'    YN[100-124]: {yn[100:125].decode("latin1", errors="replace")}')
                emit(f'    YN[125-149]: {yn[125:150].decode("latin1", errors="replace")}')
                emit(f'    YN[150-174]: {yn[150:175].decode("latin1", errors="replace")}')
                emit(f'    YN[175-199]: {yn[175:200].decode("latin1", errors="replace")}')
                emit(f'    YN[200-224]: {yn[200:225].decode("latin1", errors="replace")}')
                emit(f'    YN[225-249]: {yn[225:250].decode("latin1", errors="replace")}')
                emit('')
                if not args.trigger:
                    emit('[*] No trigger file set -- scanning immediately.')
                    if not scan_sent[0]:
                        scan_sent[0] = True
                        script_ref[0].post({'type': 'scan_now'})
            else:
                emit(f'    (capture failed: {p.get("err")})')

        elif ev == 'scan_start':
            emit('[*] Scanning process memory...')
        elif ev == 'scan_error':
            emit(f'[!] Scan error: {p["msg"]}')
        elif ev == 'scan_raw':
            count  = p['count']
            hits   = p['hits']
            bk_hex = p.get('bkysmstr') or bkysmstr_hex[0]

            emit(f'[+] Raw scan: {count} ISTS.CFG. patterns')
            run = find_table_run(hits)
            emit(f'[+] Longest 77-byte run: {len(run)} entries')
            emit('')

            if not run:
                emit('[!] No consecutive run found.')
                finished[0] = True
                return

            # Output full BKYSMSTR first
            if bk_hex:
                emit('=== BKYSMSTR YN[0..249] (hex, bytes 8..257) ===')
                yn_hex = bk_hex[16:516]  # chars 16..515 = bytes 8..257
                emit(f'  {yn_hex}')
                emit('')

            # Known anchors
            key_to_idx = {key: idx for idx, _, key, _, _ in run}
            emit('=== KNOWN SLOT ANCHORS ===')
            for slot, key in sorted(KNOWN_SLOTS.items()):
                if key in key_to_idx:
                    tbl = key_to_idx[key]
                    emit(f'  YN[{slot:3d}] = {key:<8} -> table[{tbl:4d}]  (offset slot-idx = {slot-tbl:+d})')
                else:
                    emit(f'  YN[{slot:3d}] = {key:<8} -> NOT IN RUN')
            emit('')

            # Full table with value bytes
            emit('=== FULL TABLE (key + value bytes 15..44) ===')
            emit(f'  {"Tbl":>5}  {"Key":<8}  {"ValHex":60}  ValAscii')
            emit(f'  {"---":>5}  {"---":<8}  {"------":60}  --------')
            for idx, addr, key, vh, va in run:
                yn_note = ''
                for slot, k in KNOWN_SLOTS.items():
                    if k == key:
                        yn_note = f'  <- YN[{slot}]'
                emit(f'  {idx:5d}  {key:<8}  {vh:<60}  {va}{yn_note}')

            emit('')
            emit(f'DONE. {len(run)} table entries captured.')
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

    trigger = args.trigger

    for _ in range(2400):   # 20-minute max
        if finished[0]:
            break
        time.sleep(0.5)

        if trigger and os.path.exists(trigger):
            try:
                os.remove(trigger)
            except OSError:
                pass
            if not scan_sent[0]:
                scan_sent[0] = True
                emit('[*] Trigger file detected -- scanning now...')
                script.post({'type': 'scan_now'})
                for _ in range(120):
                    if finished[0]:
                        break
                    time.sleep(0.5)
            break

    log_f.close()
    input('\nPress ENTER to close...')


if __name__ == '__main__':
    main()
