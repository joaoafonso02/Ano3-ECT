from PyKCS11 import *
from PyKCS11.LowLevel import *

lib ='/usr/local/lib/libpteidpkcs11.so'

pkcs11 = PyKCS11.PyKCS11Lib()
pkcs11.load(lib)

slots = pkcs11.getSlotList()

classes = {
	CKO_PRIVATE_KEY:'private key',
	CKO_PUBLIC_KEY:'public key',
	CKO_CERTIFICATE:'certificate'
}

for slot in slots:
	if'CARTAO DE CIDADAO' in pkcs11.getTokenInfo(slot).label:
		session = pkcs11.openSession(slot)
		objects = session.findObjects()
		
		for obj in objects:
			l = session.getAttributeValue(obj, [ CKA_LABEL ])[0]
			c = session.getAttributeValue(obj, [ CKA_CLASS ])[0]
			print('Object with label' + l + ', of class' + classes[c])
