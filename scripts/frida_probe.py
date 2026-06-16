#!/usr/bin/env python3
"""
Probe script: attach to evoerp.exe, list all loaded modules,
and check whether 0x74F8A4 is mapped. No hooks, no writes — safe.

Run this script first, then launch EvoERP. Let it run through
the login screen and one module open, then Ctrl+C.
"""
import frida, sys, time

PROC_NAME = 'evoerp.exe'

script_src = r"""
'use strict';

function probe() {
    var modules = Process.enumerateModules();
    var result = [];
    for (var i = 0; i < modules.length; i++) {
        var m = modules[i];
        result.push({
            name: m.name,
            base: m.base.toString(),
            size: m.size,
            path: m.path,
        });
    }

    // Check whether 0x74F8A4 is mapped
    var target = ptr('0x74F8A4');
    var mapped = false;
    var owner  = '(none)';
    try {
        Memory.readU8(target);
        mapped = true;
    } catch(e) {}
    for (var j = 0; j < modules.length; j++) {
        var m2 = modules[j];
        var base = m2.base.toInt32();
        if (target.toInt32() >= base && target.toInt32() < base + m2.size) {
            owner = m2.name + ' @ ' + m2.base.toString();
        }
    }

    send({event:'probe', modules:result, mapped:mapped, owner:owner});
}

// Run probe immediately on attach
probe();

// Also run probe again after 3 seconds (more modules may have loaded)
setTimeout(function() {
    probe();
    send({event:'probe2_done'});
}, 3000);

send({event:'ready'});
"""

seen_modules = set()

def on_message(msg, data):
    if msg['type'] != 'send':
        if msg['type'] == 'error':
            print(f'[FRIDA ERROR] {msg["description"]}')
        return
    p = msg['payload']
    ev = p.get('event', '')

    if ev == 'ready':
        print('[+] Attached. Probing...\n')

    elif ev in ('probe', 'probe2_done'):
        if ev == 'probe':
            mods = p['modules']
            print(f'=== Module list ({len(mods)} modules) ===')
            for m in sorted(mods, key=lambda x: x['base']):
                tag = ''
                base_i = int(m['base'], 16)
                # Flag modules whose range contains 0x74F8A4
                if base_i <= 0x74F8A4 < base_i + m['size']:
                    tag = '  <-- CONTAINS 0x74F8A4'
                if m['name'] not in seen_modules:
                    seen_modules.add(m['name'])
                    print(f'  {m["base"]}  size=0x{m["size"]:07X}  {m["name"]}{tag}')
            print(f'\n0x74F8A4 mapped={p["mapped"]}  owner={p["owner"]}\n')
        else:
            print('[*] Second probe done. Press Ctrl+C to stop.\n')

print(f'[*] Waiting for {PROC_NAME}...')
print( '    Run this script first, then launch EvoERP.\n')

session = None
while session is None:
    try:
        session = frida.attach(PROC_NAME)
    except frida.ProcessNotFoundError:
        time.sleep(0.1)

print(f'[+] Attached to {PROC_NAME}')
script = session.create_script(script_src)
script.on('message', on_message)
script.load()
sys.stdin.read()
