#!/usr/bin/env python3
"""Read the passphrase stored in the static global at 0x7EECC4."""
import hashlib, struct
data = open(r'C:\ISTS\evoerp.exe', 'rb').read()
DELTA = 0x400C00

# Static value at [0xb8b0cc] = 0x007EECC4
global_val_va = 0x007EECC4
# Delphi AnsiString: data at VA, length at VA-4, refcount at VA-8
len_off = global_val_va - DELTA - 4
rc_off  = global_val_va - DELTA - 8
dat_off = global_val_va - DELTA

# Read string header
str_len = struct.unpack_from('<I', data, len_off)[0]
str_rc  = struct.unpack_from('<i', data, rc_off)[0]
str_dat = data[dat_off:dat_off+min(str_len+4, 64)]

print(f'Global passphrase string @ VA 0x{global_val_va:X}  file 0x{dat_off:X}')
print(f'  refcount = {str_rc}')
print(f'  length   = {str_len}')
print(f'  data hex = {str_dat.hex()}')
try:
    print(f'  data str = {str_dat[:str_len].decode("latin-1")!r}')
except:
    pass
print()

# Compute SHA1 of this passphrase
if str_len > 0 and str_len < 200:
    passphrase = str_dat[:str_len]
    key = hashlib.sha1(passphrase).digest() + b'\x00'*4
    import sys; sys.path.insert(0, 'scripts')
    from twofish_pure import Twofish
    tf = Twofish(key)
    enc_zeros = tf.encrypt(bytes(16))
    IV_dcy = bytes.fromhex('cd47af18e0d1c38cf1d8a067fc3dda28')
    print(f'SHA1({passphrase!r}) + 4z = {key.hex()}')
    print(f'Encrypt(zeros) = {enc_zeros.hex()}')
    print(f'IV_dcy         = {IV_dcy.hex()}')
    print(f'MATCH: {enc_zeros == IV_dcy}')
    print()
    # If not, try SHA1 without null padding
    key2 = hashlib.sha1(passphrase).digest()[:20]  # just 20 bytes (128-bit would be 16)
    # Test as 192-bit: 20 bytes + 4 zeros = what we're already doing
    # Test as 256-bit by padding differently
    for pad_len, pad_val in [(4, b'\x00'), (12, b'\x00'), (4, passphrase[:4])]:
        key3 = hashlib.sha1(passphrase).digest() + pad_val * (pad_len // len(pad_val))
        if len(key3) in (16, 24, 32):
            try:
                tf3 = Twofish(key3)
                enc3 = tf3.encrypt(bytes(16))
                print(f'SHA1+pad({len(key3)*8}bit): Encrypt(zeros) = {enc3.hex()} match={enc3==IV_dcy}')
            except:
                pass
