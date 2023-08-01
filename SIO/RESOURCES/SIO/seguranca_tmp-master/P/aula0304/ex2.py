#!/usr/bin/env python3

from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
import sys, os

if len(sys.argv) < 3:
	print("Usage: python3 ex2.py password file_name")
	exit(0)

pwd = sys.argv[1]
salt = b'\x00'
kdf = PBKDF2HMAC(hashes.SHA1(), 16, salt, 1000, default_backend())
key = kdf.derive(bytes(pwd, 'UTF-8'))

f = open(sys.argv[2],'wb')
f.write(key)
f.close()

iv = os.urandom(algorithms.AES.block_size // 8)

cipher = Cipher(algorithms.AES(key), modes.CBC(iv), default_backend())

encryptor = cipher.encryptor()
decryptor = cipher.decryptor()

#padder = padding.PKCS7(algorithms.AES.block_size).padder()

#print(kdf + "\n")
print(key)
