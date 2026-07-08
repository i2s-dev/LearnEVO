"""
Test 05c -- ISTS.CFG Pointer-Following Value Capture

Key finding from Test 05b:
  Entry bytes 15-18 = little-endian pointer to the actual config value.
  Entry byte  21    = value length (1..N bytes).
  The Y/N character is NOT inline -- it lives at the pointer address.

Strategy:
  Same hook/trigger as 05b, but in the JS scanner we follow the pointer
  and read the actual value bytes. Python then maps each value directly
  to BKYSMSTR YN slots.

Output per entry:  table_idx | key | len | actualValHex | actualValAsc | yn_slot_match
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
var PREFIX_LEN   = 9;
var KEY_FIELD    = 6;

var READ_OPS = {5:1, 6:1, 7:1, 12:1, 13:1};

function findExport(name) {
    var mods = Process.enumerateModules();
    for (var i = 0; i < mods.length; i++) {
        var a = mods[i].findExportByName(name);
        if (a !== null) return {addr: a, mod: mods[i].name};
    }
    return null;
}

function bytesToHex(arr, off, len) {
    var s = '';
    for (var i = 0; i < len && off + i < arr.length; i++) {
        var b = arr[off + i];
        s += (b < 16 ? '0' : '') + b.toString(16);
    }
    return s;
}

function bytesToAsc(arr, off, len) {
    var s = '';
    for (var i = 0; i < len && off + i < arr.length; i++) {
        var b = arr[off + i];
        s += (b >= 0x20 && b < 0x7f) ? String.fromCharCode(b) : '.';
    }
    return s;
}

var bkysmstrHex = null;

function scanForIstsTable() {
    send({event:'scan_start'});
    var hits = [];

    Process.enumerateRanges('r--').forEach(function(range) {
        try {
            var size    = range.size;
            if (size < ENTRY_STRIDE) return;
            var scan    = Math.min(size, 4 * 1024 * 1024);
            var raw     = range.base.readByteArray(scan);
            if (!raw) return;
            var buf     = new Uint8Array(raw);

            for (var i = 0; i + PREFIX_LEN + KEY_FIELD + 22 < buf.length; i++) {
                // Pre-filter: "ISTS.CFG."
                if (buf[i]   !== 0x49 || buf[i+1] !== 0x53 || buf[i+2] !== 0x54 || buf[i+3] !== 0x53) continue;
                if (buf[i+4] !== 0x2e || buf[i+5] !== 0x43 || buf[i+6] !== 0x46 || buf[i+7] !== 0x47 || buf[i+8] !== 0x2e) continue;

                // Extract key (up to 6 uppercase alphanum)
                var key = '';
                for (var k = 0; k < KEY_FIELD; k++) {
                    var c = buf[i + PREFIX_LEN + k];
                    if (c === 0 || c === 32) break;
                    if (!((c >= 65 && c <= 90) || (c >= 48 && c <= 57))) { key = null; break; }
                    key += String.fromCharCode(c);
                }
                if (!key || key.length < 2) continue;

                // Parse pointer (entry bytes 15-18, little-endian) and length (byte 21)
                var p0 = buf[i+15], p1 = buf[i+16], p2 = buf[i+17], p3 = buf[i+18];
                var valLen  = buf[i+21];
                var typeFlag = buf[i+19];  // 0x41='A' or 0x4e='N'

                var actualValHex = '';
                var actualValAsc = '';
                if (valLen > 0 && valLen <= 64) {
                    try {
                        // Build 32-bit address; use multiplication for high byte to avoid sign issues
                        var ptrNum = p0 + p1 * 0x100 + p2 * 0x10000 + p3 * 0x1000000;
                        var valRaw = ptr(ptrNum).readByteArray(valLen);
                        if (valRaw) {
                            var vb = new Uint8Array(valRaw);
                            actualValHex = bytesToHex(vb, 0, valLen);
                            actualValAsc = bytesToAsc(vb, 0, valLen);
                        }
                    } catch(e) {
                        actualValHex = 'ERR';
                    }
                }

                hits.push({
                    addr:    range.base.add(i).toString(),
                    key:     key,
                    len:     valLen,
                    typeFlag: typeFlag,
                    valHex:  actualValHex,
                    valAsc:  actualValAsc
                });
            }
        } catch(e) {}
    });

    send({event:'scan_raw', count: hits.length, hits: hits, bkysmstr: bkysmstrHex});
}

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
                this.isRead     = true;
                this.dataBuf    = this.context.esp.add(12).readPointer();
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
                    try {
                        var raw = this.dataBuf.readByteArray(1045);
                        var buf = new Uint8Array(raw);
                        var hex = '';
                        for (var i = 0; i < 1045; i++) hex += (buf[i] < 16 ? '0' : '') + buf[i].toString(16);
                        bkysmstrHex = hex;
                        send({event:'bkysmstr_seen', hex: hex.slice(0, 520)});
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
    """Sort by address; return longest run at 77-byte stride."""
    STRIDE = 77
    parsed = []
    for h in hits:
        try:
            parsed.append((
                int(h['addr'], 16),
                h['key'],
                h.get('len', 0),
                h.get('typeFlag', 0),
                h.get('valHex', ''),
                h.get('valAsc', ''),
            ))
        except Exception:
            pass
    parsed.sort(key=lambda x: x[0])

    seen = {}
    deduped = []
    for row in parsed:
        if row[0] not in seen:
            seen[row[0]] = True
            deduped.append(row)

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

    return [(idx,) + row for idx, row in enumerate(best)]


def correlate(table_run, bk_hex):
    """Map each ISTS.CFG entry's actual value to BKYSMSTR YN slots."""
    if not bk_hex or len(bk_hex) < 520:
        return None, None

    bkysmstr = bytes.fromhex(bk_hex)
    yn = bkysmstr[8:258]   # YN[0..249]

    # val -> list of yn slots that hold that byte value
    val_to_slots = {}
    for slot, v in enumerate(yn):
        val_to_slots.setdefault(v, []).append(slot)

    mappings = []
    for row in table_run:
        idx, addr, key, vlen, typeflag, vh, va = row
        if not vh or vh == 'ERR':
            mappings.append((idx, key, vlen, vh, va, None))
            continue
        val_bytes = bytes.fromhex(vh)
        # For length-1 values: direct match
        if len(val_bytes) == 1:
            slots = val_to_slots.get(val_bytes[0], [])
            mappings.append((idx, key, vlen, vh, va, slots))
        else:
            # Multi-byte: show value, no slot match yet
            mappings.append((idx, key, vlen, vh, va, None))

    return mappings, yn


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--log',     required=True)
    parser.add_argument('--trigger', default='',
                        help='Path to trigger file; when created, scan fires.')
    args = parser.parse_args()

    if os.path.dirname(args.log):
        os.makedirs(os.path.dirname(args.log), exist_ok=True)
    log_f = open(args.log, 'w', buffering=1)

    def emit(line):
        print(line)
        log_f.write(line + '\n')

    emit('TEST 05c - ISTS.CFG Actual-Value Capture (pointer-following)')
    emit('=' * 60)
    emit(f'Log: {args.log}')
    emit(f'Trigger: {args.trigger or "(none)"}')
    emit('')

    finished   = [False]
    scan_sent  = [False]
    script_ref = [None]
    bk_hex     = [None]

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
            bk_hex[0] = p.get('hex')
            emit('[+] BKYSMSTR captured!')
            if bk_hex[0]:
                raw = bytes.fromhex(bk_hex[0])
                yn  = raw[8:258]
                for grp in range(10):
                    lo, hi = grp*25, grp*25+25
                    emit(f'    YN[{lo:3d}-{hi-1:3d}]: {yn[lo:hi].decode("latin1", errors="replace")}')
                emit('')
                if not args.trigger:
                    emit('[*] No trigger -- scanning immediately.')
                    if not scan_sent[0]:
                        scan_sent[0] = True
                        script_ref[0].post({'type': 'scan_now'})
        elif ev == 'scan_start':
            emit('[*] Scanning process memory...')
        elif ev == 'scan_raw':
            count  = p['count']
            hits   = p['hits']
            bk     = p.get('bkysmstr') or bk_hex[0]
            emit(f'[+] Raw scan: {count} ISTS.CFG. patterns')
            run = find_table_run(hits)
            emit(f'[+] Longest 77-byte run: {len(run)} entries')
            emit('')

            if not run:
                emit('[!] No run found.')
                finished[0] = True
                return

            # BKYSMSTR hex dump
            if bk:
                emit('=== BKYSMSTR YN[0..249] ===')
                emit('  ' + bk[16:516])
                emit('')

            # Known anchors
            key_to_idx = {r[2]: r[0] for r in run}
            emit('=== KNOWN ANCHORS ===')
            for slot, key in sorted(KNOWN_SLOTS.items()):
                if key in key_to_idx:
                    tbl = key_to_idx[key]
                    emit(f'  YN[{slot:3d}] = {key:<8} -> table[{tbl:3d}]  offset={slot-tbl:+d}')
                else:
                    emit(f'  YN[{slot:3d}] = {key:<8} -> NOT IN RUN')
            emit('')

            # Correlate
            mappings, yn = correlate(run, bk)

            # Build slot -> key map from KNOWN_SLOTS for collision filtering
            known_key_to_slot = {v: k for k, v in KNOWN_SLOTS.items()}

            emit('=== FULL TABLE (actual values via pointer) ===')
            emit(f'  {"Tbl":>4}  {"Key":<8}  {"Len":>3}  {"ActualVal":<32}  {"ASCII":<16}  YN_Match')
            emit(f'  {"---":>4}  {"---":<8}  {"---":>3}  {"---":<32}  {"---":<16}  ---')

            for row, (_i, _k, _vl, _vh, _va, slots) in zip(run, mappings):
                idx, addr, key, vlen, typeflag, vh, va = row
                slot_str = ''
                if slots is not None:
                    if len(slots) == 1:
                        slot_str = f'YN[{slots[0]}]'
                    elif len(slots) <= 5:
                        slot_str = f'candidates: {slots}'
                    else:
                        slot_str = f'{len(slots)} slots share this value'

                # Mark known anchors
                anchor = ''
                if key in known_key_to_slot:
                    anchor = f'  <- confirmed YN[{known_key_to_slot[key]}]'

                emit(f'  {idx:4d}  {key:<8}  {vlen:3d}  {vh:<32}  {va:<16}  {slot_str}{anchor}')

            emit('')

            # Summary: unique 1:1 mappings (len==1 + unique slot match)
            emit('=== NEW 1:1 SLOT MAPPINGS ===')
            found = 0
            for row, (_i, _k, _vl, _vh, _va, slots) in zip(run, mappings):
                idx, addr, key, vlen, typeflag, vh, va = row
                if slots and len(slots) == 1:
                    slot = slots[0]
                    # Skip if already in KNOWN_SLOTS
                    if slot not in KNOWN_SLOTS or KNOWN_SLOTS[slot] != key:
                        emit(f'  YN[{slot:3d}] = {key}  (val={vh})')
                        found += 1
            if found == 0:
                emit('  (none with unique 1-byte match -- check multi-byte entries above)')
            emit('')
            emit(f'DONE. {len(run)} entries, {found} new 1:1 mappings found.')
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
    for _ in range(2400):
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
