import sys
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

unpadder = padding.PKCS7(128).unpadder()

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

    cipher = Cipher(algorithms.AES(key), modes.ECB())
    decryptor = cipher.decryptor()

    in_file = open(sys.stdin.fileno(), "rb")
    out_file = open(sys.stdout.fileno(), "wb")

    while True:
        data = in_file.read(16)
        if len(data)==0:
            data = unpadder.finalize()
            out_file.write(data)
            break
        elif len(data) < 16:
            print("wrong file length")
            break

        data = decryptor.update(data)
        data = unpadder.update(data)
        
        if len(data)!=0:
            out_file.write(data)

    sys.exit(0)

if __name__ == "__main__":
    main()