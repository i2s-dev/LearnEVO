"""
Test 05d -- Scan ISTS.CFG + BKYSMSTR to JSON (one company per run)

Run this once per company login. Outputs a JSON file with:
  { "yn_hex": "<250-byte hex>", "ists": {"KEY": "valuehex", ...} }

Run twice (company A, then company F), then feed both JSONs to 05d-analyze.py.

Usage:
  python 05d-scan.py --log logs/scan-companyA.json [--trigger logs/scan-companyA.scan_trigger]
"""

import frida, sys, time, argparse, os, json

PROC_NAME = 'evoerp.exe'

SCRIPT = r"""
'use strict';

var ENTRY_STRIDE = 77;
var PREFIX_LEN   = 9;    // length of "ISTS.CFG."
var KEY_FIELD    = 6;    // max key chars after prefix

var READ_OPS = {5:1, 6:1, 7:1, 12:1, 13:1};

function bytesToHex(arr, off, len) {
    var s = '';
    for (var i = 0; i < len && off + i < arr.length; i++) {
        var b = arr[off + i];
        s += (b < 16 ? '0' : '') + b.toString(16);
    }
    return s;
}

function findExport(name) {
    var mods = Process.enumerateModules();
    for (var i = 0; i < mods.length; i++) {
        var a = mods[i].findExportByName(name);
        if (a !== null) return {addr: a, mod: mods[i].name};
    }
    return null;
}

var bkysmstrHex = null;
var bkysmstrSeen = false;

function hookBtrv() {
    var btrcallid = findExport('BTRCALLID');
    if (!btrcallid) return false;
    send({event:'hook_ok', mod: btrcallid.mod});

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
                if (dataLen === 1045) {
                    var raw = this.dataBuf.readByteArray(1045);
                    if (raw) {
                        var buf = new Uint8Array(raw);
                        var hex = '';
                        for (var i = 0; i < 1045; i++)
                            hex += (buf[i] < 16 ? '0' : '') + buf[i].toString(16);
                        bkysmstrHex = hex;  // always update with latest read
                        if (!bkysmstrSeen) {
                            bkysmstrSeen = true;
                            send({event:'bkysmstr_seen', hex: hex});
                        }
                    }
                }
            } catch(e) {}
        }
    });
    return true;
}

function scanIstsTable() {
    send({event:'scan_start'});
    var hits = [];

    Process.enumerateRanges('r--').forEach(function(range) {
        try {
            var size = range.size;
            if (size < ENTRY_STRIDE) return;
            var scan = Math.min(size, 4 * 1024 * 1024);
            var raw  = range.base.readByteArray(scan);
            if (!raw) return;
            var buf  = new Uint8Array(raw);

            for (var i = 0; i + PREFIX_LEN + KEY_FIELD + 22 < buf.length; i++) {
                if (buf[i]   !== 0x49 || buf[i+1] !== 0x53 || buf[i+2] !== 0x54 || buf[i+3] !== 0x53) continue;
                if (buf[i+4] !== 0x2e || buf[i+5] !== 0x43 || buf[i+6] !== 0x46 || buf[i+7] !== 0x47 || buf[i+8] !== 0x2e) continue;

                var key = '';
                for (var k = 0; k < KEY_FIELD; k++) {
                    var c = buf[i + PREFIX_LEN + k];
                    if (c === 0 || c === 32) break;
                    if (!((c >= 65 && c <= 90) || (c >= 48 && c <= 57))) { key = null; break; }
                    key += String.fromCharCode(c);
                }
                if (!key || key.length < 2) continue;

                var p0 = buf[i+15], p1 = buf[i+16], p2 = buf[i+17], p3 = buf[i+18];
                var valLen = buf[i+21];

                var valHex = '';
                if (valLen > 0 && valLen <= 64) {
                    try {
                        var ptrNum = p0 + p1 * 0x100 + p2 * 0x10000 + p3 * 0x1000000;
                        var valRaw = ptr(ptrNum).readByteArray(valLen);
                        if (valRaw) {
                            var vb = new Uint8Array(valRaw);
                            for (var j = 0; j < valLen; j++)
                                valHex += (vb[j] < 16 ? '0' : '') + vb[j].toString(16);
                        }
                    } catch(e) { valHex = ''; }
                }

                var ptrStr = '';
                if (valLen > 0 && valLen <= 64) {
                    ptrStr = (p0 + p1 * 0x100 + p2 * 0x10000 + p3 * 0x1000000).toString();
                }
                hits.push({
                    addr:   range.base.add(i).toString(),
                    key:    key,
                    len:    valLen,
                    valHex: valHex,
                    ptr:    ptrStr,
                });
            }
        } catch(e) {}
    });

    send({event:'scan_raw', count: hits.length, hits: hits, bkysmstrHex: bkysmstrHex});
}

var hooked = hookBtrv();
if (!hooked) {
    send({event:'polling'});
    var pollTimer = setInterval(function() {
        if (hookBtrv()) clearInterval(pollTimer);
    }, 500);
}

recv('scan_now', function(_) { scanIstsTable(); });
send({event:'ready'});
"""

STRIDE = 77


def find_table_run(hits):
    parsed = []
    for h in hits:
        try:
            parsed.append((int(h['addr'], 16), h['key'], h.get('len', 0), h.get('valHex', ''), h.get('ptr', '')))
        except Exception:
            pass
    parsed.sort(key=lambda x: x[0])

    seen = set()
    deduped = []
    for row in parsed:
        if row[0] not in seen:
            seen.add(row[0])
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
    return best


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--log',     required=True, help='Output JSON path')
    parser.add_argument('--trigger', default='',    help='Trigger file path (created externally to fire scan)')
    args = parser.parse_args()

    os.makedirs(os.path.dirname(args.log) if os.path.dirname(args.log) else '.', exist_ok=True)

    def emit(line):
        print(line)

    emit('Test 05d - ISTS.CFG + BKYSMSTR Scan (JSON output)')
    emit('=' * 55)
    emit(f'Output: {args.log}')
    emit(f'Trigger: {args.trigger or "(none -- fires immediately after BKYSMSTR seen)"}')
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
            emit('[+] Ready. Log into EvoERP fully, then trigger.')
            emit('')
        elif ev == 'bkysmstr_seen':
            bk_hex[0] = p['hex']
            raw = bytes.fromhex(bk_hex[0])
            yn  = raw[8:258]
            emit('[+] BKYSMSTR captured!')
            for grp in range(10):
                lo, hi = grp * 25, grp * 25 + 25
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
            hits   = p['hits']
            bk     = p.get('bkysmstrHex') or bk_hex[0]
            run    = find_table_run(hits)
            emit(f'[+] Raw hits: {p["count"]}  |  Longest 77-byte run: {len(run)} entries')

            if not run:
                emit('[!] No run found -- cannot save JSON.')
                finished[0] = True
                return

            # Build ISTS key -> {val, ptr} dict (use last seen value for dupes)
            ists = {}
            ists_ptr = {}
            for addr, key, vlen, vh, ptrstr in run:
                if vh:
                    ists[key] = vh
                if ptrstr:
                    ists_ptr[key] = int(ptrstr)

            result = {
                'yn_hex':   bk[16:516] if bk else '',   # YN[0..249] hex (bytes 8-257 of 1045-byte record)
                'ists':     ists,
                'ists_ptr': ists_ptr,
            }

            with open(args.log, 'w') as f:
                json.dump(result, f, indent=2)

            emit(f'[+] Saved JSON: {args.log}')
            emit(f'    YN slots: 250 bytes')
            emit(f'    ISTS keys: {len(ists)}')

            # Quick summary of unique 1-byte matches
            if bk:
                yn_bytes = bytes.fromhex(bk[16:516])
                val_to_slots = {}
                for slot, v in enumerate(yn_bytes):
                    val_to_slots.setdefault(v, []).append(slot)
                unique = [(k, v) for k, v in ists.items() if len(v) == 2 and len(val_to_slots.get(int(v, 16), [])) == 1]
                emit(f'    Unique 1:1 matches in this scan: {len(unique)}')
                emit(f'    Value-pointer addresses saved: {len(ists_ptr)}')
                for k, v in sorted(unique, key=lambda x: val_to_slots[int(x[1], 16)][0]):
                    slot = val_to_slots[int(v, 16)][0]
                    emit(f'      YN[{slot:3d}] = {k}  (val={v})')

            emit('')
            emit('DONE. Run 05d-analyze.py with this JSON (and optionally a second scan) to get mappings.')
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
                emit('[*] Trigger detected -- scanning now...')
                script.post({'type': 'scan_now'})
                for _ in range(120):
                    if finished[0]:
                        break
                    time.sleep(0.5)
            break

    input('\nPress ENTER to close...')


if __name__ == '__main__':
    main()
