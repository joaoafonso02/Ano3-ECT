import os
import base64
import datetime

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization

from cryptography.hazmat.backends import default_backend
from cryptography import x509
from cryptography.x509 import load_pem_x509_certificate


# from cryptography.hazmat.primitives import serialization

# from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
# from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
# from cryptography.fernet import Fernet
# from cryptography.hazmat.primitives.asymmetric import padding

def encrypt(data: bytes, key: bytes, block_size: int = 16) -> bytes:
    assert len(data)%16 == 0
    
    cipher = Cipher(algorithms.AES(key), modes.ECB())
    
    for i in range(0, len(data), 16):
        block = data[i:i+16]
        encryptor = cipher.encryptor()
        data = data[:i] + encryptor.update(block) + data[i+16:]
        
    return data
    

def encrypt_intarray(array: list, key: bytes) -> list[int]:
    cipher = Cipher(algorithms.AES(key), modes.ECB())
    
    data = []
    for i in array:
        block = i.to_bytes(16, 'big')
        
        encryptor = cipher.encryptor()
        data.append( int.from_bytes( encryptor.update(block), 'big' ) )
    
    return data

def encrypt_array(array: list, key: bytes) -> bytes:
    cipher = Cipher(algorithms.AES(key), modes.ECB())
    
    data: bytes = bytes()
    for i in array:
        block = i.to_bytes(16, 'big')
        
        encryptor = cipher.encryptor()
        data += encryptor.update(block)
    
    return data

def decrypt(data: bytes, key: bytes, block_size: int = 16) -> bytes:
    assert len(data)%16 == 0
    
    cipher = Cipher(algorithms.AES(key), modes.ECB())
    
    for i in range(0, len(data), 16):
        block = data[i:i+16]
        decryptor = cipher.decryptor()
        data = data[:i] + decryptor.update(block) + data[i+16:]
        
    return data

def decrypt_intarray(array: list[int], key: bytes) -> list[int]:
    cipher = Cipher(algorithms.AES(key), modes.ECB())

    data = []
    for i in array:
        decryptor = cipher.decryptor()
        data.append( int.from_bytes( decryptor.update( i.to_bytes(16, 'big') ), 'big' ) )
        
    return data

def decrypt_array(array: bytes, key: bytes) -> list[int]:
    cipher = Cipher(algorithms.AES(key), modes.ECB())

    data = []
    while array!=b'':
        decryptor = cipher.decryptor()
        data.append( int.from_bytes(decryptor.update( array[:16] ), 'big') )
        array = array[16:]
        
    return data


########### SIGNATURES ##########

def generate_rsa_private_key(key_size: int = 512) -> rsa.RSAPrivateKey:
    """Generates a new RSA private key with the specified key size (in bits)"""
    # Generate the private key
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=key_size)

    return private_key

def public_key_pem(public_key: rsa.RSAPublicKey) -> bytes:
    return public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

def public_key_from_pem(pem: bytes) -> rsa.RSAPublicKey:
    return serialization.load_pem_public_key(pem)

def sign_message(private_key: rsa.RSAPrivateKey, message: bytes) -> bytes:
    """Signs a message using the RSA algorithm and returns the signature"""
    # Compute the hash of the message
    message_hash = hashes.Hash(hashes.SHA256())
    message_hash.update(message)
    hashed_message = message_hash.finalize()

    # Sign the hash of the message using the private key
    signature = private_key.sign(hashed_message, padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH), hashes.SHA256())

    # Encode the signature as a base64 string
    return base64.b64encode(signature)

def verify_signature(public_key: rsa.RSAPublicKey, message: bytes, signature: bytes) -> bool:
    """Verifies an RSA signature using the given public key and returns True if the signature is valid, False otherwise"""
    # Decode the signature from a base64 string
    signature = base64.b64decode(signature)

    # Compute the hash of the message
    message_hash = hashes.Hash(hashes.SHA256())
    message_hash.update(message)
    hashed_message = message_hash.finalize()

    # Verify the signature using the public key
    try:
        public_key.verify(signature, hashed_message, padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH), hashes.SHA256())
        return True
    except Exception:
        return False

def decrypt_message(private_key: rsa.RSAPrivateKey, ciphertext: bytes) -> bytes:
    """Decrypts an RSA-encrypted message using the given private key"""
    # Decode the ciphertext from a base64 string
    ciphertext = base64.b64decode(ciphertext)

    # Decrypt the ciphertext using the private key
    plaintext = private_key.decrypt(ciphertext, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))

    return plaintext


####### AUTHENTICATION ############

def generate_auth_cert():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )

    # Generate a self-signed certificate
    subject = issuer = x509.Name([
        x509.NameAttribute(x509.NameOID.COUNTRY_NAME, "PT"),
        x509.NameAttribute(x509.NameOID.STATE_OR_PROVINCE_NAME, "Portugal"),
        x509.NameAttribute(x509.NameOID.LOCALITY_NAME, "Aveiro"),
        x509.NameAttribute(x509.NameOID.ORGANIZATION_NAME, "university of aveiro"),
        x509.NameAttribute(x509.NameOID.COMMON_NAME, "My Certificate")
    ])
    cert = x509.CertificateBuilder().subject_name(
        subject
    ).issuer_name(
        issuer
    ).public_key(
        private_key.public_key()
    ).serial_number(
        x509.random_serial_number()
    ).not_valid_before(
        datetime.datetime.utcnow()
    ).not_valid_after(
        # Our certificate will be valid for 10 years
        datetime.datetime.utcnow() + datetime.timedelta(days=3650)
    ).sign(private_key, hashes.SHA256(), default_backend())
    

    # Encode the certificate as a string
    return cert.public_bytes(serialization.Encoding.PEM)
    # cert_str = cert_bytes.decode('utf-8')

    # Send the certificate as a message
    # m.send_json( server, 'certificate', body=cert_str)
    
def verify_auth_cert(cert_bytes: bytes):
    try:
        certificate = x509.load_pem_x509_certificate(cert_bytes, default_backend())
        certificate.public_key().verify(
            certificate.signature,
            certificate.tbs_certificate_bytes,
            padding.PKCS1v15(),
            certificate.signature_hash_algorithm
        )

        return True
    except:
        return False


########### DEVELOPMENT TESTS ###########

def generatekey() -> bytes:
    return os.urandom(16)

if __name__ == '__main__':
    # test functions
    original = [1,2,3,4,5,6,7,8,9]
    array = b''.join([i.to_bytes(16, 'big') for i in original])
    print("Encrypt:", array)
    
    # create key
    key = generatekey()
    print("key:", key)
    
    # encrypt
    crypt: bytes = encrypt(array, key)
    print("Encrypted", len(crypt))
    # print("array bytes", bytes(crypt))
    # print("arry after bytes", crypt, len(crypt))
    
    # rsa_private_key = generate_rsa_private_key(512)
    # print("Generated RSA key to sign", rsa_private_key)
    
    # signed_message = sign_message(rsa_private_key, crypt)
    # print("Signed")
    
    # rsa_public_key = rsa_private_key.public_key()
    # print("Public key:", rsa_public_key)
    
    # signed_check = verify_signature(rsa_public_key, crypt, signed_message)
    # if signed_check:
    #     print("Properly signed and Verified")
    #     pass
    # else:
    #     print("Could not verify")
    
    decarray = decrypt(crypt, key)
    print("\ndectext:", decarray)
    
    if array==decarray:
        print("ALL WORKING")
        print([int.from_bytes(decarray[i:i+16], 'big') for i in range(0, len(decarray), 16)])
    