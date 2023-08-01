import sys
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend

def main():
	if len(sys.argv) < 5:
		print( "Usage: decipher_rsa.py key_file password ciphered_text_file out_cleartext_file\n" )
		sys.exit( 1 )
	
	password = sys.argv[2]

	with open(sys.argv[1], "rb") as kf:
		priv_key = serialization.load_pem_private_key(kf.read(), bytes(password, "utf-8"), default_backend())	

	f_cipheredtext = open(sys.argv[3], "rb")
	
	cipheredtext = f_cipheredtext.read()

	cleartext = priv_key.decrypt(cipheredtext, padding.OAEP(padding.MGF1(hashes.SHA256()), hashes.SHA256(), None))

	f_out = open(sys.argv[4], 'wb')
	f_out.write(cleartext)

if __name__ == "__main__":
	main()
