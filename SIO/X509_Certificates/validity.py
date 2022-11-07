#!bin/python
import sys
from cryptography import x509

def validity( cert ):
    print("%s" % (cert.subject))
    print("\tbegin = %s" % (cert.not_valid_before))
    print("\tend = %s" % (cert.after))
    print('\textensions = ')
    print( cert.extensions )

def main():
    if len(sys.argv) == 1:
        fd = open(sys.stdin.fileno(), 'rb')
        pem_data = fd.read()
        cert = x509.load_pem_x509_certificate(pem_data)
        validity( cert )
    else:
        for name in sys.argv[1:]:
            with open(name, 'rb') as fd:
                fd = open(sys.stdin.fileno(), 'rb')
                pem_data = fd.read()
                cert = x509.load_pem_x509_certificate(pem_data)
                validity( cert )
                fd.close()

if __name__ == '__main__':
    main()