#!bin/python
import sys
import os
from colorama import Fore, Back, Style # prettier,  # delete 
from cryptography import x509
from cryptography.x509 import ObjectIdentifier
ca_certs = {}

def is_ca_certificate( cert ):
    ext = cert.extensions.get_extension_for_oid( ObjectIdentifier('2.5.29.19') )
    return ext.value.ca

def load_cert_from_file( file_name ):
    with open( file_name, 'rb') as fd:
        pem_data = fd.read()
        cert = x509.load_pem_x509_certificate( pem_data )
        fd.close
        return cert

def load_ca_certificates_from_dir( dir_list):
    for dir_name in dir_list:
        for entry in os.scandir( dir_name ):
            if entry.is_file() and entry.name.lower().endswith('.pem'):
                cert = load_cert_from_file(dir_name + '/' + entry.name)
                if is_ca_certificate(cert):
                    ca_certs[cert.subject] = cert

def load_ca_certificates():
    load_ca_certificates_from_dir(['.', '/usr/local/etc/openssl\@1.1'])

def chain(cert):
    if is_ca_certificate(cert):
        print("certificate with subject %s is a CA certificate" % (cert.subject))
        return
    print('subject = %s' % (cert.subject))
    print('\tissuer = %s' % (cert.issuer))

    target = cert.issuer
    while True:
        print('subject = %s' % (ca_certs[target]))
        print('\tissuer = %s' % (ca_certs[target].issuer))
        if target == ca_certs[target].issuer:
            break
        target = ca_certs[target].issuer


def main():
    load_ca_certificates()
    print( ca_certs )

    # if len(sys.argv) == 1:
    #     fd = open(sys.stdin.fileno(), 'rb')
    #     pem_data = fd.read()
    #     cert = x509.load_pem_x509_certificate(pem_data)
    #     validity( cert )
    # else:
    #     for name in sys.argv[1:]:
    #         with open(name, 'rb') as fd:
    #             fd = open(sys.stdin.fileno(), 'rb')
    #             pem_data = fd.read()
    #             cert = x509.load_pem_x509_certificate(pem_data)
    #             validity( cert )
    #             fd.close()

if __name__ == '__main__':
    main()