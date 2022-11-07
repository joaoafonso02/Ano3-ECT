#!bin/python
import sys
from colorama import Fore, Back, Style # prettier,  # delete 
from cryptography import x509
from cryptography.x509 import ObjectIdentifier

def validity( cert ):
    print("%s" % (cert.subject))
    print("\tbegin = %s" % (cert.not_valid_before))
    print("\tend = %s" % (cert.not_valid_after))
    
    ext = cert.extensions.get_extension_for_oid( ObjectIdentifier('2.5.29.19') )
    if ( ext.value.ca == True):
        if cert.issuer == cert.subject:
            print( Fore.CYAN + '\tRoot CA Certificate' ) # delete Fore 
        else:
            print( Fore.GREEN + '\tIntermediate CA Certificate' ) # delete Fore
    else:
        print( Fore.RED + '\tEnd Entity Certificate')  # delete Fore
    
    print(Style.RESET_ALL)  # delete 
    #print("Extension= %s" % ext)
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