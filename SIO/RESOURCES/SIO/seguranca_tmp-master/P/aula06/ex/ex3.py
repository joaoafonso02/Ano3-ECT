from PyKCS11 import *
from PyKCS11.LowLevel import *

lib = '/usr/local/lib/libpteidpkcs11.so'

pkcs11 = PyKCS11.PyKCS11Lib()
pkcs11.load(lib)
slots = pkcs11.getSlotList()

for slot in slots:
	if 'CARTAO DE CIDADAO' in pkcs11.getTokenInfo(slot).label:
		data = bytes('data to be signed', 'utf-8')

		session = pkcs11.openSession(slot)

		privKey = session.findObjects( [(CKA_CLASS, CKO_PRIVATE_KEY),
						(CKA_LABEL, 'CITIZEN AUTHENTICATION KEY')])[0]
		
		signature = bytes(session.sign(privKey, data, Mechanism(CKM_SHA1_RSA_PKCS)))

		session.closeSession
