"""
Test 02 - K_A File-Open Hook
Hooks CreateFileW (searched across all loaded modules, not just kernel32) alongside
Twofish SetKey. Only EVO-relevant file extensions are kept in the ring buffer so
noise from DLL/registry opens does not crowd out the useful entries.

When any SetKey fires, we snapshot the 30 most recent relevant-extension opens
so we can correlate each key with the file that triggered it.

K_A = d97f05679438037073c30628734764020859f77e (purpose unknown)

Usage:
  python tests/02-ka-file-hook.py --log logs/ka-hook.txt
"""

import frida, sys, time, argparse, os

K_A = 'd97f05679438037073c30628734764020859f77e'

KNOWN_KEYS = {
    'd97f05679438037073c30628734764020859f77e': 'K_A (UNKNOWN -- THIS IS WHAT WE WANT)',
    'a898d21e2fd6ca294026e5d633d9047f91f7ed35': 'K_B (RWN files)',
    '507d2b20f46ac5f82d47e82a9065d7bc0c2e12bb': 'K_C (suwin6.dcy)',
    '691e8041ab265b4e6ee052ccc946dba4caac60da': 'K_D (DCY files)',
    'd6e9efa8195c45cce839e88e52767768ff8f2463': 'NEW-1 (unknown -- fires at boot)',
    'fdc2883f6d6537dd667270406d0a4c85969295ac': 'NEW-2 (unknown -- fires mid-session)',
}

PROC_NAME      = 'evoerp.exe'
PREFERRED_BASE = 0x400000
SETKEY_VA      = 0x0074F8A4

SCRIPT = r"""
'use strict';

var mod = Process.findModuleByName('evoerp.exe');
var SETKEY_RVA = 0x0074F8A4 - 0x400000;
var SETKEY     = mod.base.add(SETKEY_RVA);

// Extensions we care about (lower-case, with dot)
var EVO_EXTS = ['.rwn','.dcy','.run','.rtm','.rtn','.cfg','.dba','.imp','.upd','.b','.rgt'];

function isEvoFile(name) {
    if (!name || name.length === 0) return false;
    var lower = name.toLowerCase();
    for (var i = 0; i < EVO_EXTS.length; i++) {
        if (lower.indexOf(EVO_EXTS[i], lower.length - EVO_EXTS[i].length) !== -1) return true;
    }
    return false;
}

// Ring buffer: last 30 EVO-relevant file opens
var recentFiles = [];
function recordFile(name) {
    recentFiles.push(name);
    if (recentFiles.length > 30) recentFiles.shift();
}

// Frida 17: Module.findExportByName(null, name) is gone.
// Enumerate all loaded modules and find the real implementation address.
function findExport(exportName) {
    var mods = Process.enumerateModules();
    for (var i = 0; i < mods.length; i++) {
        var addr = mods[i].findExportByName(exportName);
        if (addr !== null) return addr;
    }
    return null;
}

var cfwAddr = findExport('CreateFileW');
if (cfwAddr) {
    send({event:'hook_ok', name:'CreateFileW', addr:cfwAddr.toString()});
    Interceptor.attach(cfwAddr, {
        onEnter: function(args) {
            try {
                var name = args[0].readUtf16String();
                if (isEvoFile(name)) recordFile(name);
            } catch(e) {}
        }
    });
} else {
    send({event:'hook_fail', name:'CreateFileW'});
}

var cfaAddr = findExport('CreateFileA');
if (cfaAddr) {
    send({event:'hook_ok', name:'CreateFileA', addr:cfaAddr.toString()});
    Interceptor.attach(cfaAddr, {
        onEnter: function(args) {
            try {
                var name = args[0].readAnsiString();
                if (isEvoFile(name)) recordFile(name);
            } catch(e) {}
        }
    });
} else {
    send({event:'hook_fail', name:'CreateFileA'});
}

var setkeyCalls = 0;

Interceptor.attach(SETKEY, {
    onEnter: function(args) {
        try {
            setkeyCalls++;
            var key_arr  = Array.from(new Uint8Array(this.context.edx.readByteArray(24)));
            var key_bits = this.context.ecx.toInt32();
            var iv_param = this.context.esp.add(4).readU32();
            var snapshot = recentFiles.slice();
            send({
                event:    'setkey',
                call:     setkeyCalls,
                key_bits: key_bits,
                key_arr:  key_arr,
                iv_param: iv_param,
                files:    snapshot
            });
        } catch(e) { send({event:'err', where:'setkey', msg:e.toString()}); }
    }
});

send({event:'ready', base:mod.base.toString(), setkey:SETKEY.toString()});
"""


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

    emit('TEST 02 - K_A File-Open Hook')
    emit('=' * 50)
    emit(f'Target key : {K_A}  (K_A)')
    emit(f'Log file   : {args.log}')
    emit('')

    def on_message(msg, data):
        if msg['type'] == 'error':
            emit(f'[FRIDA ERROR] {msg["description"]}')
            return
        if msg['type'] != 'send':
            return
        p = msg['payload']
        ev = p.get('event', '')

        if ev == 'ready':
            emit(f'[+] evoerp.exe base  = {p["base"]}')
            emit(f'    SetKey hook      -> {p["setkey"]}')
            emit('')
            emit('[+] All hooks active -- EvoERP actions will now be captured.')
            emit('')

        elif ev == 'hook_ok':
            emit(f'[+] Hooked {p["name"]} at {p["addr"]}')

        elif ev == 'hook_fail':
            emit(f'[!] Could not find {p["name"]} -- file open tracking may be incomplete')

        elif ev == 'setkey':
            key_b  = bytes(p['key_arr'])
            key20  = key_b[:20].hex()
            label  = KNOWN_KEYS.get(key20, '*** UNRECOGNIZED KEY ***')
            is_ka  = (key20 == K_A)
            marker = '>>>' if is_ka else '---'

            emit(f'{marker} SetKey #{p["call"]} {"<<< K_A IDENTIFIED" if is_ka else ""}')
            emit(f'  key[0:20]: {key20}')
            emit(f'  label    : {label}')
            emit(f'  key_bits : {p["key_bits"]}')
            emit(f'  IV param : 0x{p["iv_param"]:08x}')
            if p['files']:
                emit(f'  Recent EVO files at this moment:')
                for f in p['files']:
                    emit(f'    {f}')
            else:
                emit(f'  Recent EVO files: (none captured yet)')
            emit('')

        elif ev == 'err':
            emit(f'[!] hook error ({p["where"]}): {p["msg"]}')

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

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        emit('')
        emit('[*] Capture stopped.')
        log_f.close()


if __name__ == '__main__':
    main()
