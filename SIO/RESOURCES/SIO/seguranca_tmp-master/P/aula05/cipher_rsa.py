import sys
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend

def main():
	if len(sys.argv) < 5:
		print( "Usage: cipher_rsa.py key_file password text_file new_file\n" )
		sys.exit( 1 )
	
	password = sys.argv[2]

	with open(sys.argv[1], "rb") as kf:
		priv_key = serialization.load_pem_private_key(kf.read(), bytes(password, "utf-8"), default_backend())	
	pub_key = priv_key.public_key()

	maxLen = (pub_key.key_size // 8) - 2 * hashes.SHA256.digest_size - 2

	f_plaintext = open(sys.argv[3], "rb")
	
	plaintext = f_plaintext.read(maxLen)

	ciphertext = pub_key.encrypt(plaintext, padding.OAEP(padding.MGF1(hashes.SHA256()), hashes.SHA256(), None))

	f_out = open(sys.argv[4], 'wb')
	f_out.write(ciphertext)

if __name__ == "__main__":
	main()
