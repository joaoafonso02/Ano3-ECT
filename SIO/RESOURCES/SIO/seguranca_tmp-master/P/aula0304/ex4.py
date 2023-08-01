#!/usr/bin/env python3

from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
import sys, os

if len(sys.argv) < 3:
	print("Usage: python3 ex4.py key_file file_ciphered file_out")
	exit(0)

with open(sys.argv[1], mode='rb') as file:
	key = file.read()

f = open(sys.argv[2], 'rb')
iv = f.read(algorithms.AES.block_size // 8)
f.close()

cipher = Cipher(algorithms.AES(key), modes.CBC(iv), default_backend())
decryptor = cipher.decryptor()
padder = padding.PKCS7(algorithms.AES.block_size).unpadder()

f_out = open('decifrado.bmp', 'wb')
f_out.write(iv)

f = open(sys.argv[2], 'rb')

f.read(algorithms.AES.block_size//8)

while True:
	ciphertext = f.read(algorithms.AES.block_size)
	
	if not ciphertext:
		plaintext = decryptor.update(padder.finalize())

		f_out.write(plaintext)
		f_out.close()
		break
	else:
		plaintext = decryptor.update(padder.update(ciphertext))
		f_out.write(plaintext)

