#!/usr/bin/env python3

from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
import sys, os

if len(sys.argv) < 3:
	print("Usage: python3 ex2.py password_file file_name")
	exit(0)

with open(sys.argv[1], mode='rb') as file:
	key = file.read()


iv = os.urandom(algorithms.AES.block_size // 8)
cipher = Cipher(algorithms.AES(key), modes.CBC(iv), default_backend())
encryptor = cipher.encryptor()
padder = padding.PKCS7(algorithms.AES.block_size).padder()

f = open(sys.argv[2],'rb')
f_out = open('cifrado', 'wb')
f_out.write(iv)

while True:
	plaintext = f.read(algorithms.AES.block_size)
	
	if not plaintext:
		ciphertext = encryptor.update(padder.finalize())

		f_out.write(ciphertext)
		f_out.close()
		break
	else:
		ciphertext = encryptor.update(padder.update(plaintext))
		f_out.write(ciphertext)

