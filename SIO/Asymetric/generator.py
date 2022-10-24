#!/bin/python
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def main():
    private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
    )

    pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )

    print( pem.decode( "ascii" ))


if __name__ == "__main__":
    main()