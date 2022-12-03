import PyKCS11

def main():
    lib = 'usr/local/lib/libpteidpkes11.dls' # macOS different

    pkcs11 = PyKCS11.PyKCS11Lib()

    pkcs11.load(lib)
    slots = pkcs11.getSlotList( tokenPresent = True)

    print( len(slots) )

    for slot in slots:
        info = pkcs11.getSlotInfo( slot )
        #print( info )
        session =pkcs11.openSession( slot )

        objs = session.findObjects()

        for obj in objs:
            attr = session.getAttributeValue( obj, [PyKCS11.CKA_LABEL])
            print( attr[0])

if __name__ == '__main__':
    main()