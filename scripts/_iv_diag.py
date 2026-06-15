#!/usr/bin/env python3
import hashlib, struct, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from twofish_pure import Twofish

key = hashlib.sha1(b'mabufoju').digest() + b'\x00'*4
tf  = Twofish(key)
EXP = 0x3E0A37C5

def le32(b, o): return struct.unpack_from('<I', b, o)[0]
def xorchk(k):  return le32(k, 0) ^ le32(k, 4)

enc_zeros = tf.encrypt(b'\x00' * 16)
print('Encrypt(zeros)       =', enc_zeros.hex(' '))
print('  XOR                = 0x%08X  (exp 0x%08X)' % (xorchk(enc_zeros), EXP))

deref = bytes.fromhex('0e6fbff653a28a70d102874c6b1825ad')
enc_d = tf.encrypt(deref)
dec_d = tf.decrypt(deref)
enc_dec_d = tf.encrypt(dec_d)

print()
print('deref                =', deref.hex(' '))
print('  equals Enc(zeros)? =', deref == enc_zeros)
print('  Encrypt(deref) XOR = 0x%08X  (exp 0x%08X)' % (xorchk(enc_d), EXP))
print('  Decrypt(deref)     =', dec_d.hex(' '), ' <-- IV candidate if deref = Enc(IV)')
print('  Enc(Dec(deref)) XOR= 0x%08X  (exp 0x%08X)' % (xorchk(enc_dec_d), EXP))

# Is deref perhaps Encrypt(Encrypt(real_IV))?
# i.e., real_IV = Decrypt(Decrypt(deref))
dbl_dec = tf.decrypt(dec_d)
enc_dbl = tf.encrypt(dbl_dec)
print()
print('  Decrypt^2(deref)   =', dbl_dec.hex(' '), ' <-- if deref = Enc^2(IV)')
print('  Enc(Dec^2) XOR     = 0x%08X  (exp 0x%08X)' % (xorchk(enc_dbl), EXP))

# Check T7INA.RWN ct[0:8] for reference
ct8 = bytes.fromhex('f813b67b3d24bc45')
ct_xor = le32(ct8, 0) ^ le32(ct8, 4)
print()
print('T7INA.RWN ct[0:4]^ct[4:8] = 0x%08X  (confirmed)' % ct_xor)
