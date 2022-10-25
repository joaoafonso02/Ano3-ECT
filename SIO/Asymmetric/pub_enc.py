#!/bin/python
import sys
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

def main():
    if len(sys.argv) < 2:
        print("Usage : %s key_file\n" % (sys.argv[0]), file=sys.stderr)
        sys.exit(1)
    
    with open(sys.argv[1], "r") as key_file:
        key_data = bytes(key_file.read(), "ascii")
        private_key = serialization.load_pem_private_key(
           key_data,
           password=None
        )

    public_key = private_key.public_key()

    padder = padding.OAEP( label =b"Teste",
                            algorithm=hashes.SHA256(),
                            mgf=padding.MGF1( algorithm=hashes.SHA1())
    )

    in_file = open( sys.stdin.fileno(), "rb")
    out_file = open( sys.stdout.fileno(), "wb")

    input_data = in_file.read()

    # max len(inout.data)

    max_data_len = public_key.key_size // 8 - 2*hashes-SHA256().digest_size - 2
    cryptogram = public_key.encrypt( input_data, padder)
    out_file.write(cryptogram)

if __name__ == "__main__":
    main()