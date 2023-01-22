#!/bin/python

import base64
import sys
import socket
import json
import messages as m
import threading
import random
import encryption
import PyKCS11 # pip install PyKCS11
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

def read_input( socket, srv, private_key ):
    for line in sys.stdin:        
        if line.startswith('!ping '):
            data = line.removeprefix('!ping ').strip("\n")
            m.send_json( socket, 'ping', data )
            
        elif line.startswith('!g ') or line.startswith('!global '):
            data = line.removeprefix('!g ' if line.startswith('!g') else '!global ').strip("\n")
            m.send_json( socket, 'global', data )
        
        elif line.startswith('!ge ') or line.startswith('!global_encrypted '):
            data = line.removeprefix('!ge ' if line.startswith('!ge') else '!global_encrypted ').strip("\n")
            key = encryption.generatekey()
            data = data + ' '*(16-len(data.encode('utf-8'))%16)
            data = encryption.encrypt( data.encode('utf-8'), key )
            m.send_json( socket, 'global_encrypted' )
            m.send( socket, data )
            print("Sent encrypted data:", data)
            m.send( socket, key )
            print("Sent key:", key)
            print("sent", data)
            
        elif line.startswith('!gs ') or line.startswith('!global_signed '):
            data = line.removeprefix('!gs ' if line.startswith('!gs') else '!global_signed ').strip("\n")
            data = data.encode('utf-8')
            _private_key = encryption.generate_rsa_private_key()
            _public_key_pem = encryption.public_key_pem(_private_key.public_key())
            
            _signature = encryption.sign_message(_private_key, data)
            
            m.send_json( socket, 'global_signed' )
            
            m.send( socket, data )
            m.send( socket, _signature )
            m.send( socket, _public_key_pem )
        
        elif line.startswith('!users'):
            print(srv['users'])
            
        elif line.startswith('!start'):
            # this starts the game loop
            m.send_json( socket, 'start')

        elif line.startswith('!set_nickname '):
            # this starts the game loop
            m.send_json( socket, 'set_nickname', line.removeprefix('!set_nickname ').strip("\n") )

        #  report cheat
        elif line.startswith('!report_cheat'):
            m.send_json( socket, 'report_cheat', line.removeprefix('!report_cheat ').strip("\n") )
        
        else:
            print("Command not found, try !help (not currently working)")
            # TODO !help menu


def main(*args):
    if len(args)<2 and len(sys.argv) != 3:
        print( 'Usage: %s port nickname' % (sys.argv[0]) )
        sys.exit( 1 )    
        
    port = args[0] if len(args)>=2 else sys.argv[1]
    nickname = args[1] if len(args)>=2 else sys.argv[2]
    
    rsa_private_key = encryption.generate_rsa_private_key()
    rsa_public_key = rsa_private_key.public_key()
        
    srv = {'users': {}, 'config': {}}

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.connect( ( '127.0.0.1', int(port) ) )
        
        # create thread to input reading
        thread = threading.Thread(target=read_input, args=( server,srv,rsa_private_key ))
        thread.start()
        
        # citizen card
        # Load the PKCS#11 library for the card reader
        pkcs11 = PyKCS11.PyKCS11Lib()
        if sys.platform == 'linux':
            lib = '/usr/local/lib/libpteidpkcs11.so'
        elif sys.platform == 'darwin':
            lib = '/usr/local/lib/libpteidpkcs11.dylib'
        elif system == 'Windows':
            lib = 'C:\\Windows\\System32\\pteidpkcs11.dll'
        sign_card(lib)

        m.send( server, encryption.generate_auth_cert() )
                
        # set nickname
        m.send_json( server, 'set_nickname', nickname )
        
        # set public key
        m.send_json( server, 'set_public_key' )
        m.send( server, encryption.public_key_pem(rsa_public_key) )

        # m.send_json( server, 'test', encryption.sign_message(rsa_private_key, b'hello world').decode('utf-8'))
        
        shuffle_log = []
        private_keys = []
        
        while True:
            data = m.recv_json( server )
            
            # connection closed
            if data == None:
                break
            # incomming data doesnt make sense
            if data == 0:
                continue
            
            body = data['body']
            
            # incomming log (just print it)
            if data['header']['type'] == 'log':
                print(body)
                
            elif data['header']['type'] == 'global_signed':
                text = body['nickname'] + ":"
                msg = bytes( m.recv( server ) )  
                signature = bytes( m.recv( server ) )
                public_key = bytes( m.recv( server ) )
                if encryption.verify_signature(encryption.public_key_from_pem(public_key), msg, signature):
                    print("Verified Signature!")
                    print(msg.decode('utf-8'))
                else:
                    print("Could not verify signature!")
                    
            elif data['header']['type'] == 'global_encrypted':
                text = body['nickname'] + ":"
                crypt = bytes(m.recv( server ))  
                key = bytes(m.recv( server ))
                print(text, encryption.decrypt( crypt, key ).decode('utf-8').strip())
            
            elif data['header']['type'] == 'set_config':
                srv['config'] = data['body']
                # print("SET_CONFIG", data['body'])
                
                
            # sync users dict
            elif data['header']['type'] == 'update_users':
                for i in body:
                    srv['users'][int(i)] = {}
                    srv['users'][int(i)]['id'] = body[i]['id']
                    srv['users'][int(i)]['nickname'] = body[i]['nickname']
                    if body[i]['public_key']:
                        srv['users'][int(i)]['public_key'] = encryption.public_key_from_pem(base64.b64decode(body[i]['public_key'].encode('utf-8')))
                    
                print("UPDATE_USERS", [(i, data['body'][i]['nickname']) for i in body])


            elif data['header']['type'] == 'get_card_and_keys':
                deck: bytes = shuffle_log[-1]['deck'] # create copy
                card = bytes()
                for i in range(srv['config']['m']):
                    r = random.randint(0,len(deck)/16-1)
                    card += deck[r*16:r*16+16]
                    deck = deck[:r*16] + deck[r*16+16:]
                    # card.append(numbers.pop(r))
                
                signature = encryption.sign_message(rsa_private_key, card+b''.join(private_keys))
                
                m.send_json( server, 'set_card_and_keys' )
                m.send( server, card )
                for i in private_keys:
                    m.send( server, i )
                private_keys = []
                m.send( server, signature )

            elif data['header']['type'] == 'update_card_and_keys':
                # verify signature
                public_key = srv['users'][body['id']]['public_key']

                card = bytes( m.recv( server ) )
                _private_keys = [ bytes(m.recv(server)) for i in range(0, 1+int(body['id']==0))]
                signature = bytes( m.recv( server ) )
                if not encryption.verify_signature(public_key, card+b''.join(_private_keys), signature):
                    print("Card not verified successfully")
                    # TODO what should append now?
                else:
                    print("Siganture of private keys and card Verified")
                    # TODO, verify if the card is within rules
                    srv['users'][body['id']]['card'] = card
                    srv['users'][body['id']]['private_keys'] = _private_keys


            elif data['header']['type'] == 'shuffle_log':
                id = body['id']
                deck = bytes( m.recv( server ) )
                signature = bytes( m.recv( server ) )
                if not encryption.verify_signature(srv['users'][id]['public_key'], deck, signature):
                    print("Verification of shuffle failed!")
                    # TODO what should append now?
                else:
                    print("Signature of shuffle Verified")
                    shuffle_log.append({'id':body['id'],'deck':deck,'signature':signature})
                
                
            elif data['header']['type'] == 'shuffle':
                print("shuffling")
                old_deck = bytes( m.recv( server ) )
                
                # generate private key
                key = encryption.generatekey()
                private_keys.append( key ) # key must be stored with int value so it can be sent within json
                # encrypt incomming deck
                old_deck = encryption.encrypt( old_deck, key )
                
                # shuffle the encrypted deck
                new_deck = bytes()
                while len(old_deck)>0:
                    r = random.randint(0,(len(old_deck)-16)//16)
                    new_deck += old_deck[r*16:r*16+16]
                    old_deck = old_deck[:r*16] + old_deck[r*16+16:]
                    # new_deck.append(old_deck.pop(r))
                    
                signature = encryption.sign_message(rsa_private_key, new_deck)
                m.send_json( server, 'shuffle' )
                m.send( server, new_deck )
                m.send( server, signature )

            elif data['header']['type'] == 'get_winner':
                print("DECRYPTING DECK AND CARDS")
                
                deck = shuffle_log[-1]['deck']
                i = 1
                while i<=len(srv['users'])+1:
                    print(i)
                    key: bytes = srv['users'][shuffle_log[-i]['id']]['private_keys'].pop()

                    # decript deck
                    # print("USER",shuffle_log[-i]['id'], key)
                    deck = encryption.decrypt( deck, key )
                    # decript users cards
                    for j in range(1, len(srv['users'])):
                        srv['users'][j]['card'] = encryption.decrypt(srv['users'][j]['card'], key)
                    
                    i += 1
                
                deck = [int.from_bytes(deck[i:i+16], 'big') for i in range(0, len(deck), 16)]
                print("DECK", deck)
                # print("CARDS:")
                
                for i in range(1, len(srv['users'])):
                    card = []
                    for j in range(0, len(srv['users'][i]['card']), 16):
                        card.append(int.from_bytes(srv['users'][i]['card'][j:j+16], 'big'))
                    srv['users'][i]['card'] = card
                                 
                print(*[str(i)+" "+srv['users'][i]['nickname']+": "+str(srv['users'][i]['card']) for i in range(1, len(srv['users']))], sep='\n')

                found = False
                
                winners = []
                for i in deck:
                    if winners!=[]: break
                    for j in range(1, len(srv['users'])):
                        if i in srv['users'][j]['card']:
                            srv['users'][j]['card'].remove(i)
                            if srv['users'][j]['card'] == []:
                                print("WINNER FOUND: ", j, "->", srv['users'][j]['nickname'])
                                winners += [srv['users'][j]['nickname']]
                
                '''deal with the case where there are more than one winner'''
                if winners == []:
                    print("NO WINNER FOUND")
                else:
                    print("WINNERS FOUND: ", winners)
                    found = True

                m.send_json( server, 'none', winners)
                winners_solutions = m.recv_json( server )['body']
                found = False
                for i in winners_solutions:
                    if winners_solutions[i]!=winners:
                        found = True
                if found:
                    print("Found a different answer!")
                else:
                    print("All the users found the same answer!")
                

def sign_card(lib_path):
    pkcs11 = PyKCS11.PyKCS11Lib()
    pkcs11.load(lib_path)
    slots = pkcs11.getSlotList()
    private_key = None

    all_attr = list(PyKCS11.CKA.keys())
    # Filter attributes
    all_attr = [e for e in all_attr if isinstance(e, int)]

    for slot in slots:
        # Open a new session with the token
        session = pkcs11.openSession(slot)
        for obj in session.findObjects():
            # Get object attributes
            attr = session.getAttributeValue(obj, all_attr)
            attr = dict(zip(map(PyKCS11.CKA.get, all_attr), attr))
            if attr['CKA_CLASS'] == PyKCS11.CKO_CERTIFICATE:
                if attr['CKA_ID'][0] == 69:     # signature
                    cert = x509.load_der_x509_certificate( bytes(attr['CKA_VALUE']), default_backend())

            if attr['CKA_CLASS'] == PyKCS11.CKO_PRIVATE_KEY:
                if attr['CKA_ID'][0] == 69:  # signature
                    private_key = obj
                    break
        if private_key is not None:
            text = b'WASSAP'
            # Sign the message using the private key and the SHA1-RSA-PKCS mechanism
            mechanism = PyKCS11.Mechanism(PyKCS11.CKM_SHA1_RSA_PKCS, None)
            signature = bytes(session.sign(private_key, text, mechanism))

            public_key = cert.public_key()
            public_key.verify(signature, text, padding.PKCS1v15(), hashes.SHA1()) 

            # Write the signed message and verification result to a file
            with open('sign.bin', 'wb') as f:
                f.write(signature)

            # Return the signature
            return signature

        # Close the session when you are finished
        session.closeSession()

    # If the private key was not found, return None
    print("Error: Private key not found")
    return None


if __name__ == '__main__':
    main()