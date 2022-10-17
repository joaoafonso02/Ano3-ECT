import os
from pickle import TRUE
import sys
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

padder = padding.PKCS7(128).padder()


def main():
    # ver parametros do programa
    # encrypt.py senha
    # Input ou stdin
    # Output on stdout

    if len(sys.argv) != 2:
        print("Usage: %s senha\n" % (sys.argv[0]))
        sys.exit(1)

    kdf = PBKDF2HMAC(
        algorithm = hashes.SHA256(),
        length = 32,
        salt = bytes(),
        iterations=1000000
    )

    key = kdf.derive( sys.argv[1].encode("utf-8") )

    iv = os.urandom(18) # generate random IV

    cipher = Cipher(algorithms.AES(key), modes.OFB())
    encryptor = cipher.encryptor()

    in_file = open(sys.stdin.fileno(), "rb")
    out_file = open(sys.stdout.fileno(), "wb")

    out_file.write(iv)
    
    while True:
        data = in_file.read(8192) # 8 x 1024 = 8192
        if len(data) == 0:
            break

        data = encryptor.update(data)
        out_file.write(data)

    sys.exit(0)

if __name__ == "__main__":
    main()