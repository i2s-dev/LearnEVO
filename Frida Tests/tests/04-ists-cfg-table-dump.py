"""
Test 04 v5 -- ISTS.CFG Key Collector

Pre-attaches to EVO before launch (like Test 03) and hooks BTRCALLID.
ISTS.CFG records are read at EVO startup -- all ~250 are captured during
login before any module screen is opened.

IMPORTANT: Start this script first, THEN launch EVO. Do NOT attach to
           a running instance.

Diagnostic fallback: if no ISTS.CFG records appear in the first 200
reads, every read is logged (size + first 32 data bytes) so the actual
format can be identified.

Usage:
  python tests/04-ists-cfg-table-dump.py --log logs/ists-cfg.txt [--trigger path]
"""

import frida, sys, time, argparse, os

PROC_NAME  = 'evoerp.exe'
PREFIX     = 'ISTS.CFG.'
PREFIX_LEN = 9

# Keys we know exist in ISTS.CFG (for diagnostic matching without prefix)
KNOWN_KEYS = [
    b'STDCST', b'DCSEQ', b'DCSYNC', b'CALCLABR', b'INVAPREC',
    b'WOCALC', b'ALLSVCPO', b'APCHK', b'WOGKIT', b'MRPDAY',
    b'CRHOLD', b'BACKFLSH', b'DCSEQ', b'DCSEQ',
]

SCRIPT = r"""
'use strict';

var PREFIX_LEN  = 9;
var PREFIX      = 'ISTS.CFG.';
var MAX_READS   = 10000;
var DIAG_READS  = 200;  // after this many reads with no ISTS hit, dump all reads

var READ_OPS = {5:'GetEqual', 6:'GetNext', 7:'GetPrev', 12:'GetFirst', 13:'GetLast'};

function readAscii(ptr, maxLen) {
    try {
        var b = new Uint8Array(ptr.readByteArray(maxLen));
        var s = '';
        for (var i = 0; i < b.length; i++) {
            if (b[i] === 0) break;
            var c = b[i];
            if (c < 0x20 || c >= 0x7f) return null;
            s += String.fromCharCode(c);
        }
        return s;
    } catch(e) { return null; }
}

function hexBytes(ptr, n) {
    try {
        var b = new Uint8Array(ptr.readByteArray(n));
        var s = '';
        for (var i = 0; i < b.length; i++) {
            var h = b[i].toString(16);
            s += (h.length < 2 ? '0' : '') + h + ' ';
        }
        return s.trim();
    } catch(e) { return '??'; }
}

function asciiPreview(ptr, n) {
    try {
        var b = new Uint8Array(ptr.readByteArray(n));
        var s = '';
        for (var i = 0; i < b.length; i++) {
            var c = b[i];
            s += (c >= 0x20 && c < 0x7f) ? String.fromCharCode(c) : '.';
        }
        return s;
    } catch(e) { return '??'; }
}

function findExport(name) {
    var mods = Process.enumerateModules();
    for (var i = 0; i < mods.length; i++) {
        var a = mods[i].findExportByName(name);
        if (a !== null) return {addr: a, mod: mods[i].name};
    }
    return null;
}

var btrvReadCount = 0;
var istsKeys      = {};
var istsOrder     = [];
var istsCount     = 0;
var diagMode      = false;  // set true if no hits after DIAG_READS reads

function hookBtrv() {
    var btrcallid = findExport('BTRCALLID');
    if (!btrcallid) return false;
    send({event:'hook_ok', name:'BTRCALLID', mod:btrcallid.mod, addr:btrcallid.addr.toString()});

    Interceptor.attach(btrcallid.addr, {
        onEnter: function(args) {
            try {
                var op = this.context.esp.add(4).readU16();
                this.op = op;
                if (!(op in READ_OPS)) return;
                this.dataBuf    = this.context.esp.add(12).readPointer();
                this.dataLenPtr = this.context.esp.add(16).readPointer();
                // Also capture key buffer for diagnostics
                this.keyBuf = this.context.esp.add(20).readPointer();
                var kl = this.context.esp.add(24).readU16();
                this.keyLen = Math.min(kl, 48);
            } catch(e) {}
        },
        onLeave: function(retval) {
            try {
                if (!(this.op in READ_OPS)) return;
                if (retval.toInt32() !== 0) return;
                if (btrvReadCount >= MAX_READS) return;
                btrvReadCount++;

                var dataLen = 0;
                try { dataLen = this.dataLenPtr.readU16(); } catch(e) { return; }

                // ---- Primary filter: ISTS.CFG records (60-100 bytes) ----
                if (dataLen >= 60 && dataLen <= 100) {
                    var pre = readAscii(this.dataBuf, PREFIX_LEN);
                    if (pre && pre === PREFIX) {
                        var key = readAscii(this.dataBuf.add(PREFIX_LEN), 32);
                        if (key && key.length > 0) {
                            key = key.replace(/\s+$/, '');
                            if (!istsKeys[key]) {
                                istsKeys[key] = istsCount;
                                istsOrder.push(key);
                                istsCount++;
                                send({event:'key', key:key, n:istsCount,
                                      read:btrvReadCount, len:dataLen});
                            }
                            return;
                        }
                    }
                }

                // ---- Diagnostic: after DIAG_READS reads with no ISTS hit, log everything ----
                if (istsCount === 0 && btrvReadCount >= DIAG_READS) {
                    if (!diagMode) {
                        diagMode = true;
                        send({event:'diag_start', reads:btrvReadCount});
                    }
                    var keyPrev  = asciiPreview(this.keyBuf,  this.keyLen || 0);
                    var dataPrev = dataLen > 0 ? asciiPreview(this.dataBuf, Math.min(dataLen, 32)) : '';
                    var dataHex  = dataLen > 0 ? hexBytes(this.dataBuf, Math.min(dataLen, 32)) : '';
                    send({event:'diag_read', n:btrvReadCount, op:READ_OPS[this.op],
                          klen:this.keyLen, key:keyPrev, dlen:dataLen,
                          dascii:dataPrev, dhex:dataHex});
                }
            } catch(e) {}
        }
    });
    return true;
}

// Poll for BTRCALLID every 500 ms (w3btrv7.dll loads after EVO starts)
var hooked = hookBtrv();
if (!hooked) {
    send({event:'polling', msg:'BTRCALLID not found yet -- waiting for w3btrv7.dll to load...'});
    var pollTimer = setInterval(function() {
        if (hookBtrv()) {
            clearInterval(pollTimer);
        }
    }, 500);
}

recv('dump', function(_) {
    send({event:'dump', keys:istsOrder, total:istsCount, reads:btrvReadCount});
});

send({event:'ready'});
"""


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--log',     required=True)
    parser.add_argument('--trigger', default='',
                        help='Trigger file path; when created, dump is requested.')
    args = parser.parse_args()

    if os.path.dirname(args.log):
        os.makedirs(os.path.dirname(args.log), exist_ok=True)

    log_f = open(args.log, 'w', buffering=1)

    def emit(line):
        print(line)
        log_f.write(line + '\n')

    emit('TEST 04 - ISTS.CFG Key Collector')
    emit('=' * 50)
    emit(f'Log file: {args.log}')
    emit('')

    finished   = [False]
    dump_sent  = [False]
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
            emit(f'[+] Hooked {p["name"]} in {p["mod"]} at {p["addr"]}')

        elif ev == 'polling':
            emit(f'[~] {p["msg"]}')

        elif ev == 'hook_fail':
            emit(f'[!] Hook failed: {p["name"]} -- {p.get("msg","")}')
            finished[0] = True

        elif ev == 'ready':
            emit('[+] Script loaded. Launch EVO now.')
            emit('    ISTS.CFG records will stream below at startup/login.')
            emit('')

        elif ev == 'key':
            emit(f'  #{p["n"]:3d}  {PREFIX}{p["key"]}  (read #{p["read"]}, len={p["len"]})')

        elif ev == 'diag_start':
            emit('')
            emit(f'[!] No ISTS.CFG hits after {p["reads"]} reads.')
            emit(f'    DIAGNOSTIC MODE -- logging all reads from here:')
            emit(f'    {"#":>5}  {"op":<9}  {"klen":>4}  {"key":<30}  {"dlen":>5}  data')
            emit(f'    {"-"*5}  {"-"*9}  {"-"*4}  {"-"*30}  {"-"*5}  ----')

        elif ev == 'diag_read':
            emit(f'    {p["n"]:5d}  {p["op"]:<9}  {p["klen"]:4d}  {p["key"]:<30}  '
                 f'{p["dlen"]:5d}  {p["dascii"]}')
            emit(f'    {"":<5}  {"":<9}  {"":<4}  {"":<30}  {"":<5}  [{p["dhex"]}]')

        elif ev == 'dump':
            keys = p['keys']
            emit('')
            if keys:
                emit(f'[+] DUMP -- {p["total"]} unique ISTS.CFG keys captured')
                emit(f'    Total Btrieve reads: {p["reads"]}')
                emit('')
                emit(f'  {"Idx":>4}  Key')
                emit(f'  {"----":>4}  ---')
                for i, k in enumerate(keys):
                    emit(f'  {i:4d}  {k}')
            else:
                emit(f'[!] No ISTS.CFG keys captured. Total reads: {p["reads"]}')
                emit(f'    See DIAGNOSTIC output above for raw read data.')
            emit('')
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

    for _ in range(1200):   # 10-minute outer timeout
        if finished[0]:
            break
        time.sleep(0.5)

        if trigger and os.path.exists(trigger):
            try:
                os.remove(trigger)
            except OSError:
                pass
            if not dump_sent[0]:
                dump_sent[0] = True
                emit('[*] Dump triggered.')
                script.post({'type': 'dump'})
                for _ in range(30):
                    if finished[0]:
                        break
                    time.sleep(0.5)
            break

    if not finished[0] and not dump_sent[0]:
        emit('[!] Timeout -- requesting dump.')
        script.post({'type': 'dump'})
        for _ in range(20):
            if finished[0]:
                break
            time.sleep(0.5)

    log_f.close()
    input('\nPress ENTER to close...')


if __name__ == '__main__':
    main()
