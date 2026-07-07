#!/usr/bin/env python3
"""
Test 01 - All Twofish Key Capture
Captures every SetKey call made by evoerp.exe during boot and login.
Logs to both console (its own window) and the file passed via --log.

Known keys for comparison:
  K_A = d97f05679438037073c30628734764020859f77e  (unknown purpose)
  K_B = a898d21e2fd6ca294026e5d633d9047f91f7ed35  (RWN files)
  K_C = 507d2b20f46ac5f82d47e82a9065d7bc0c2e12bb  (suwin6.dcy / ISTech License)
  K_D = 691e8041ab265b4e6ee052ccc946dba4caac60da  (DCY files)

Usage:
  python tests/01-key-capture.py --log logs/capture.txt
"""

import frida, sys, time, argparse, os

KNOWN_KEYS = {
    'd97f05679438037073c30628734764020859f77e': 'K_A (unknown purpose)',
    'a898d21e2fd6ca294026e5d633d9047f91f7ed35': 'K_B (RWN files)',
    '507d2b20f46ac5f82d47e82a9065d7bc0c2e12bb': 'K_C (suwin6.dcy)',
    '691e8041ab265b4e6ee052ccc946dba4caac60da': 'K_D (DCY files)',
}

PROC_NAME     = 'evoerp.exe'
PREFERRED_BASE = 0x400000
SETKEY_VA     = 0x0074F8A4
MODE2_VA      = 0x0074EB50
ENCBLOCK_VA   = 0x00750248

SCRIPT = """
'use strict';
var mod = Process.findModuleByName('evoerp.exe');
var SETKEY_RVA   = {setkey}   - {preferred};
var MODE2_RVA    = {mode2}    - {preferred};
var ENCBLOCK_RVA = {encblock} - {preferred};
var SETKEY   = mod.base.add(SETKEY_RVA);
var MODE2    = mod.base.add(MODE2_RVA);
var ENCBLOCK = mod.base.add(ENCBLOCK_RVA);

send({{event:'addrs', base:mod.base.toString(),
      setkey:SETKEY.toString(), mode2:MODE2.toString(), encblock:ENCBLOCK.toString()}});

function bytesToHex(arr) {{
    var s = '';
    for (var i = 0; i < arr.length; i++) s += (arr[i] < 16 ? '0' : '') + arr[i].toString(16);
    return s;
}}

var setkeyCalls = 0, mode2Calls = 0, encCalls = 0;

Interceptor.attach(SETKEY, {{
    onEnter: function(args) {{
        try {{
            setkeyCalls++;
            var key_arr = Array.from(new Uint8Array(this.context.edx.readByteArray(24)));
            var key_bits = this.context.ecx.toInt32();
            var iv_param = this.context.esp.add(4).readU32();
            send({{event:'setkey', call:setkeyCalls, key_bits:key_bits,
                   key_arr:key_arr, iv_param:iv_param}});
        }} catch(e) {{ send({{event:'err', where:'setkey', msg:e.toString()}}); }}
    }}
}});

Interceptor.attach(MODE2, {{
    onEnter: function(args) {{
        try {{
            mode2Calls++;
            if (mode2Calls > 20) return;
            var p_ptr  = this.context.eax.add(0x3c).readU32();
            var b1_ptr = this.context.eax.add(0x38).readU32();
            var p_arr  = Array.from(new Uint8Array(ptr(p_ptr).readByteArray(16)));
            var b1_arr = Array.from(new Uint8Array(ptr(b1_ptr).readByteArray(16)));
            send({{event:'mode2', call:mode2Calls, P:p_arr, buffer1:b1_arr}});
        }} catch(e) {{ send({{event:'err', where:'mode2', msg:e.toString()}}); }}
    }}
}});

Interceptor.attach(ENCBLOCK, {{
    onEnter: function(args) {{ this.src = this.context.edx; }},
    onLeave: function(retval) {{
        try {{
            encCalls++;
            if (encCalls > 20) return;
            var out_arr = Array.from(new Uint8Array(this.src.readByteArray(16)));
            send({{event:'encrypt', call:encCalls, out:out_arr}});
        }} catch(e) {{ send({{event:'err', where:'encrypt', msg:e.toString()}}); }}
    }}
}});

send({{event:'ready'}});
""".format(preferred=PREFERRED_BASE, setkey=SETKEY_VA, mode2=MODE2_VA, encblock=ENCBLOCK_VA)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--log', required=True, help='Output log file path')
    args = parser.parse_args()

    os.makedirs(os.path.dirname(args.log), exist_ok=True) if os.path.dirname(args.log) else None
    log_f = open(args.log, 'w', buffering=1)

    def emit(line):
        print(line)
        log_f.write(line + '\n')

    emit('TEST 01 — Twofish Key Capture')
    emit('=' * 50)
    emit(f'Log file: {args.log}')
    emit('')

    def on_message(msg, data):
        if msg['type'] == 'error':
            emit(f'[FRIDA ERROR] {msg["description"]}')
            return
        if msg['type'] != 'send':
            return
        p = msg['payload']
        ev = p.get('event', '')

        if ev == 'addrs':
            emit(f'[+] evoerp.exe base = {p["base"]}')
            emit(f'    SetKey   -> {p["setkey"]}')
            emit(f'    mode2    -> {p["mode2"]}')
            emit(f'    EncBlock -> {p["encblock"]}')
            emit('')

        elif ev == 'ready':
            emit('[+] Hooks live — EvoERP actions will now be captured.')
            emit('')

        elif ev == 'setkey':
            key_b  = bytes(p['key_arr'])
            key20  = key_b[:20].hex()
            label  = KNOWN_KEYS.get(key20, '*** UNKNOWN KEY ***')
            emit(f'--- SetKey #{p["call"]} ---')
            emit(f'  key_bits : {p["key_bits"]}')
            emit(f'  key[0:24]: {key_b.hex()}')
            emit(f'  key[0:20]: {key20}')
            emit(f'  label    : {label}')
            emit(f'  IV param : 0x{p["iv_param"]:08x}')
            emit('')

        elif ev == 'mode2':
            p_b  = bytes(p['P'])
            b1_b = bytes(p['buffer1'])
            emit(f'--- mode2 #{p["call"]} ---')
            emit(f'  P       : {p_b.hex()}')
            emit(f'  buffer1 : {b1_b.hex()}')
            emit('')

        elif ev == 'encrypt':
            out_b = bytes(p['out'])
            emit(f'  EncryptBlock #{p["call"]}: {out_b.hex()}')

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

    # Stay alive until killed by parent process
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
