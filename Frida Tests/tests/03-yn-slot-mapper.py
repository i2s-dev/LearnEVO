"""
Test 03 - YN Slot Mapper

Two-pronged approach to identify the unknown YN[N] <-> ISTS.CFG key mappings.

PRONG A: Hook BTRCALLID in w3btrv7.dll to capture all Btrieve reads.
  BKYSMSTR records are ~1045 bytes. YN[0..249] live at byte offsets 8..257.
  When a record of that size comes back, we extract and log all 250 YN values.

PRONG B: After EVO is fully initialized, scan all readable process memory for
  known ISTS.CFG key strings (CRHOLD, MRPDAY, WOGKIT ...). If they appear
  together in a structured table, we dump the surrounding 512 bytes to extract
  the full 250-entry key list -- which would give us all slot mappings at once.

BKYSMSTR record layout (confirmed from DDF):
  Offset 0-7  : non-YN header fields (company code etc.)
  Offset 8    : YN[0]  (BKYS_YN_1)
  Offset 9    : YN[1]  (BKYS_YN_2)
  ...
  Offset 257  : YN[249] (BKYS_YN_250)
  Offset 258+ : other fields (record total ~1045 bytes)

Usage:
  python tests/03-yn-slot-mapper.py --log logs/yn-mapper.txt
"""

import frida, sys, time, argparse, os

KNOWN_KEYS = [
    'CRHOLD', 'MRPDAY', 'WOGKIT', 'WOGDSC', 'CMEST', 'CALCLABR',
    'INVAPREC', 'ALLSVCPO', 'CSTMETH', 'RETBILL', 'ENTDEPT', 'ENTLOC',
    'BOMMRP', 'BACKFLSH', 'PRINTSO', 'PRINTAR', 'PRINTAP', 'MRPROUND',
    'DCSEQ', 'DCSYNC', 'STDCST', 'APCHK', 'WOCALC',
]

# Known confirmed slot -> key mappings (for annotation)
KNOWN_SLOTS = {
    27: 'CALCLABR',
    33: 'INVAPREC',
    38: 'WOCALC',
    40: 'ALLSVCPO',
    48: 'APCHK',
    65: 'STDCST',
    228: 'DCSEQ',
    229: 'DCSYNC',
}

PROC_NAME = 'evoerp.exe'
BTRV_MIN  = 900   # BKYSMSTR records are ~1045 bytes; accept 900-1200
BTRV_MAX  = 1200

# NOTE: No .format() call -- braces are plain JavaScript. BTRV_MIN/MAX are
# substituted via .replace() below so Python never parses JS braces as format fields.
SCRIPT = r"""
'use strict';

function bytesToAscii(arr) {
    var s = '';
    for (var i = 0; i < arr.length; i++) {
        var c = arr[i];
        s += (c >= 0x20 && c < 0x7f) ? String.fromCharCode(c) : '.';
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

var READ_OPS = {5:'GetEqual', 6:'GetNext', 7:'GetPrev', 12:'GetFirst', 13:'GetLast'};
var btrvReadCount = 0;
var MAX_READS = 300;
var BKYSMSTR_MIN = _MIN_SIZE_;
var BKYSMSTR_MAX = _MAX_SIZE_;

var btrcallid = findExport('BTRCALLID');
if (btrcallid) {
    send({event:'hook_ok', name:'BTRCALLID', mod:btrcallid.mod, addr:btrcallid.addr.toString()});
    Interceptor.attach(btrcallid.addr, {
        onEnter: function(args) {
            try {
                var op = this.context.esp.add(4).readU16();
                this.op = op;
                if (!(op in READ_OPS)) return;
                this.dataBuf    = this.context.esp.add(12).readPointer();
                this.dataLenPtr = this.context.esp.add(16).readPointer();
                var keyBuf  = this.context.esp.add(20).readPointer();
                var keyLen  = Math.min(this.context.esp.add(24).readU16(), 64);
                try {
                    this.keyBytes = Array.from(new Uint8Array(keyBuf.readByteArray(keyLen)));
                } catch(e) { this.keyBytes = []; }
            } catch(e) {}
        },
        onLeave: function(retval) {
            try {
                if (!(this.op in READ_OPS)) return;
                if (retval.toInt32() !== 0) return;
                if (btrvReadCount >= MAX_READS) return;

                var dataLen = 0;
                try { dataLen = this.dataLenPtr.readU16(); } catch(e) {}

                // Log BKYSMSTR-sized records in full; smaller ones in brief.
                var isBkysmstr = (dataLen >= BKYSMSTR_MIN && dataLen <= BKYSMSTR_MAX);
                var readBytes = isBkysmstr ? Math.min(dataLen, 264) : Math.min(dataLen, 64);
                var dataBytes = [];
                if (dataLen > 0 && dataLen < 65535 && readBytes > 0) {
                    try {
                        dataBytes = Array.from(new Uint8Array(this.dataBuf.readByteArray(readBytes)));
                    } catch(e) {}
                }

                btrvReadCount++;
                send({
                    event:      'btrv_read',
                    n:          btrvReadCount,
                    op:         READ_OPS[this.op],
                    keyBytes:   this.keyBytes,
                    dataLen:    dataLen,
                    dataBytes:  dataBytes,
                    isBkysmstr: isBkysmstr
                });
            } catch(e) {}
        }
    });
} else {
    send({event:'hook_fail', name:'BTRCALLID',
          msg:'w3btrv7.dll not loaded yet -- ensure EVO is running before attaching'});
}

// PRONG B: memory scan (triggered by parent via recv)
function runMemoryScan(knownKeys) {
    send({event:'scan_start', count: knownKeys.length});
    var results = {};

    for (var ki = 0; ki < knownKeys.length; ki++) {
        var key = knownKeys[ki];
        var pattern = '';
        for (var ci = 0; ci < key.length; ci++) {
            var h = key.charCodeAt(ci).toString(16);
            pattern += (h.length === 1 ? '0' : '') + h + ' ';
        }
        pattern += '00';

        var hits = [];
        var ranges = Process.enumerateRanges('r--');
        for (var ri = 0; ri < ranges.length; ri++) {
            var range = ranges[ri];
            if (range.size > 32 * 1024 * 1024) continue;
            try {
                var matches = Memory.scanSync(range.base, range.size, pattern);
                for (var mi = 0; mi < matches.length; mi++) {
                    hits.push(matches[mi].address.toString());
                }
            } catch(e) {}
        }
        results[key] = hits;
    }

    // Detect table structure: two or more known keys within 4KB
    var tableHints = [];
    var kNames = Object.keys(results);
    for (var i = 0; i < kNames.length; i++) {
        for (var j = i + 1; j < kNames.length; j++) {
            var addrsA = results[kNames[i]];
            var addrsB = results[kNames[j]];
            for (var ai = 0; ai < addrsA.length; ai++) {
                for (var bi = 0; bi < addrsB.length; bi++) {
                    var diff = Math.abs(parseInt(addrsA[ai]) - parseInt(addrsB[bi]));
                    if (diff < 4096) {
                        tableHints.push({
                            keyA: kNames[i], addrA: addrsA[ai],
                            keyB: kNames[j], addrB: addrsB[bi],
                            distance: diff
                        });
                    }
                }
            }
        }
    }

    send({event:'scan_done', results: results, tableHints: tableHints});

    // Dump 1KB around the first cluster found
    if (tableHints.length > 0) {
        tableHints.sort(function(a, b) { return a.distance - b.distance; });
        var h = tableHints[0];
        var minAddr = Math.min(parseInt(h.addrA), parseInt(h.addrB));
        // Go back 64 bytes to catch entries before the first found key
        var dumpBase = ptr(Math.max(minAddr - 64, 0));
        try {
            var context = Array.from(new Uint8Array(dumpBase.readByteArray(1024)));
            send({event:'table_dump', baseAddr: dumpBase.toString(), bytes: context});
        } catch(e) {
            send({event:'table_dump_err', msg: e.toString()});
        }
    }
}

recv('scan', function(msg) {
    runMemoryScan(msg.keys);
});

send({event:'ready'});
""".replace('_MIN_SIZE_', str(BTRV_MIN)).replace('_MAX_SIZE_', str(BTRV_MAX))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--log', required=True)
    args = parser.parse_args()

    if os.path.dirname(args.log):
        os.makedirs(os.path.dirname(args.log), exist_ok=True)
    log_f = open(args.log, 'w', buffering=1)

    def emit(line):
        print(line)
        log_f.write(line + '\n')

    def bytes_to_ascii(b):
        return ''.join(chr(c) if 0x20 <= c < 0x7f else '.' for c in b)

    emit('TEST 03 - YN Slot Mapper')
    emit('=' * 50)
    emit(f'Log file: {args.log}')
    emit('')

    script_ref = [None]
    trigger_file = args.log + '.scan_trigger'

    def on_message(msg, data):
        if msg['type'] == 'error':
            emit(f'[FRIDA ERROR] {msg["description"]}')
            return
        if msg['type'] != 'send':
            return
        p = msg['payload']
        ev = p.get('event', '')

        if ev == 'ready':
            emit('[+] All hooks active.')
            emit('')

        elif ev == 'hook_ok':
            emit(f'[+] Hooked {p["name"]} in {p["mod"]} at {p["addr"]}')

        elif ev == 'hook_fail':
            emit(f'[!] Hook failed: {p["name"]} -- {p["msg"]}')

        elif ev == 'btrv_read':
            key_str = bytes_to_ascii(p['keyBytes']).rstrip('\x00').strip() if p['keyBytes'] else ''

            if p['isBkysmstr']:
                raw = bytes(p['dataBytes'])
                yn = raw[8:258] if len(raw) >= 258 else raw[8:]
                emit(f'=== BKYSMSTR RECORD #{p["n"]} ({p["op"]}) len={p["dataLen"]} key={repr(key_str)} ===')
                emit(f'  Header [0:8] : {bytes_to_ascii(raw[:8])} | {raw[:8].hex()}')
                emit(f'  YN[0..9]     : {bytes_to_ascii(yn[:10])} ({yn[:10].hex()})')
                emit(f'  YN[10..19]   : {bytes_to_ascii(yn[10:20])} ({yn[10:20].hex()})')
                emit(f'  YN[20..29]   : {bytes_to_ascii(yn[20:30])} ({yn[20:30].hex()})')
                if len(yn) > 110:
                    emit(f'  YN[100..109] : {bytes_to_ascii(yn[100:110])} ({yn[100:110].hex()})')
                if len(yn) > 150:
                    emit(f'  YN[140..149] : {bytes_to_ascii(yn[140:150])} ({yn[140:150].hex()})')
                emit(f'  Full YN[0..249]:')
                for i in range(0, min(len(yn), 250), 25):
                    chunk = yn[i:i+25]
                    annotations = '  '.join(
                        f'[{i+j}]={KNOWN_SLOTS[i+j]}'
                        for j in range(len(chunk)) if (i+j) in KNOWN_SLOTS
                    )
                    emit(f'    YN[{i:3d}-{i+len(chunk)-1:3d}]: {bytes_to_ascii(chunk)}  {annotations}')
                emit('')
            else:
                data_preview = bytes_to_ascii(p['dataBytes'][:48]) if p['dataBytes'] else ''
                emit(f'--- Btrieve {p["op"]} #{p["n"]} key={repr(key_str)} len={p["dataLen"]} data={data_preview}')

        elif ev == 'scan_start':
            emit(f'[*] Scanning memory for {p["count"]} known ISTS.CFG key strings...')
            emit('    (this may take 10-30 seconds)')

        elif ev == 'scan_done':
            found    = {k: v for k, v in p['results'].items() if v}
            notfound = [k for k, v in p['results'].items() if not v]
            emit(f'[+] Scan complete.')
            emit(f'  Found ({len(found)}): ' + ', '.join(f'{k}@{v[0]}' for k, v in found.items()))
            emit(f'  Not found ({len(notfound)}): ' + ', '.join(notfound))
            emit('')
            if p['tableHints']:
                emit(f'[!!!] TABLE STRUCTURE DETECTED -- {len(p["tableHints"])} co-located key pairs:')
                for h in sorted(p['tableHints'], key=lambda x: x['distance'])[:10]:
                    emit(f'  {h["keyA"]}@{h["addrA"]}  <->  {h["keyB"]}@{h["addrB"]}  dist={h["distance"]}')
                emit('')
            else:
                emit('[~] No table structure -- keys are not co-located in memory.')

        elif ev == 'table_dump':
            raw = bytes(p['bytes'])
            emit(f'[+] 1KB dump at {p["baseAddr"]}:')
            for i in range(0, 1024, 32):
                chunk = raw[i:i+32]
                emit(f'  +{i:04x}  {chunk.hex()}  |{bytes_to_ascii(chunk)}|')
            emit('')

        elif ev == 'table_dump_err':
            emit(f'[!] Dump failed: {p["msg"]}')

    emit(f'[*] Waiting for {PROC_NAME}...')
    session = None
    while session is None:
        try:
            session = frida.attach(PROC_NAME)
        except frida.ProcessNotFoundError:
            time.sleep(0.1)

    emit(f'[+] Attached to {PROC_NAME}')
    script = session.create_script(SCRIPT)
    script.on('message', on_message)
    script.load()
    script_ref[0] = script

    try:
        while True:
            time.sleep(0.5)
            if os.path.exists(trigger_file):
                os.remove(trigger_file)
                emit('')
                emit('[*] Memory scan triggered...')
                script.post({'type': 'scan', 'keys': KNOWN_KEYS}, None)
                time.sleep(8)
    except KeyboardInterrupt:
        pass
    finally:
        emit('')
        emit('[*] Capture stopped.')
        if os.path.exists(trigger_file):
            os.remove(trigger_file)
        log_f.close()


if __name__ == '__main__':
    main()
