#!/bin/python

import base64
import sys
import socket
import selectors
import json
import messages as m
import encryption
import PyKCS11 # pip install PyKCS11
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric.padding import PKCS1v15
from cryptography.hazmat.primitives.hashes import SHA1, Hash

class User:
    def __init__(self, id=None, socket=None, nickname=None, public_key=None):
        self.id: int = id
        self.socket: socket = socket
        self.nickname: str = nickname
        self.public_key: bytes = public_key
        
        self.card = None
        self.private_keys = []
        
    
    def get(self):
        return {
            'id': self.id,
            'nickname': self.nickname,
            'public_key': base64.b64encode(self.public_key).decode('utf-8') if self.public_key else None
        }


config = {
    "n": 9,
    "m": 3,
    "max_users": 50
}

def sendall( users: list[dict], clt_id: int, type: str, data=None ): 
    """ 
    send a message to all sockets
        users -> dict of all users (containing the socket)
        clt_id -> the id of user that requested this action (if =-1 the message should be sent to everyone)
        type -> message type
        data -> data
    """
    for i in users:
        if users[i].id!=clt_id:
            m.send_json( users[i].socket, type, data )
            
def sendallb( users: list[dict], clt_id: int, data ):
    assert data!=None
    for i in users:
        if users[i].id!=clt_id:
            m.send( users[i].socket, data )
            
            
            
def update_users( users ):
    # filter only the public info of users
    data = {}
    for i in users:
        data[users[i].id] = users[i].get()
        # data[i] = {x:users[i][x] for x in ['id', 'nickname', 'public_key']} 

    sendall( users, -1, 'update_users', data )

def getCertificate(session):
    cert_obj = session.findObjects([
                    (PyKCS11.CKA_CLASS, PyKCS11.CKO_CERTIFICATE),
                    (PyKCS11.CKA_LABEL, 'CITIZEN AUTHENTICATION CERTIFICATE')
                    ])[0]

    cert_data = bytes(cert_obj.to_dict()['CKA_VALUE'])

    cert = x509.load_der_x509_certificate(cert_data, default_backend())
    return cert

def autenticateCertificate(cert,signature,text):
    pubkey = cert.public_key()
    try:
        md = hashes.Hash(hashes.SHA1(), default_backend())
        md.update(text)
        digest = md.finalize()


        pubkey.verify(
            signature,
            digest,
            PKCS1v15(),
            SHA1()
        )
        return True
    except:
        return False
        
def signCertificate(text,session):
    private_key = session.findObjects([(PyKCS11.CKA_CLASS, PyKCS11.CKO_PRIVATE_KEY)])[0]

    mechanism = PyKCS11.Mechanism(PyKCS11.CKM_SHA1_RSA_PKCS, None)

    signature = bytes(session.sign(private_key, text, mechanism))
    return signature
            
            
def dispatch( srv_socket ):
    selector = selectors.DefaultSelector()

    srv_socket.setblocking( False )
    selector.register( srv_socket, selectors.EVENT_READ, data=None )
    j = 0
    
    users = {}
    game = {
        'state': 'STOPPED', # states -> STOPPED | GETCARDS | SHUFFLING | GETWINNER,
        'caller': None,
        'higher_id': None,
        'n_users': 0,
        'n_cards': 0,
        'curr_shuffler': 0,
    }
    shuffle_log = []
    
    while True:
        # print( 'Select' )
        events = selector.select( timeout=None )
        
        for key, mask in events:

            # Check for a new client connection
            if key.fileobj == srv_socket:
                # game already started or max players limit reached
                if game['state']!='STOPPED':
                    clt_socket, clt_addr = srv_socket.accept()
                    m.send_json( clt_socket, 'log', 'You can\'t loggin at the moment, try later!' )
                    clt_socket.close()
                    continue

                # accept player
                clt_socket, clt_addr = srv_socket.accept()
                clt_socket.setblocking( True )

                # Add it to the sockets under scrutiny
                selector.register( clt_socket, selectors.EVENT_READ, data=None )

                # pkcs11 = PyKCS11.PyKCS11Lib()
                # if sys.platform == 'linux':
                #     lib = '/usr/local/lib/libpteidpkcs11.so'
                # elif sys.platform == 'darwin':
                #     lib = '/usr/local/lib/libpteidpkcs11.dylib'
                # elif system == 'Windows':
                #     lib = 'C:\\Windows\\System32\\pteidpkcs11.dll'
                # pkcs11.load(lib)

                # # Get a list of slots (token readers)
                # slots = pkcs11.getSlotList()

                # # Open a session with the first slot (token reader)
                # session = pkcs11.openSession(slots[0])

                # # Find all objects (e.g. certificates and keys) in the token
                # objects = session.findObjects()

                # # Iterate through the objects and find the certificate for the Citizen Card
                # for obj in objects:
                #     # Get the attributes of the object
                #     attr = session.getAttributeValue(obj, [PyKCS11.CKA_CLASS, PyKCS11.CKA_ID])
                #     attr = dict(zip([PyKCS11.CKA.get(a) for a in [PyKCS11.CKA_CLASS, PyKCS11.CKA_ID]], attr))

                #     # If the object is a certificate
                #     if attr['CKA_CLASS'] == PyKCS11.CKO_CERTIFICATE:
                #         # If the certificate has the ID of the Citizen Card
                #         if attr['CKA_ID'][0] == 70:
                #             # Get the value of the certificate
                #             value = session.getAttributeValue(obj, [PyKCS11.CKA_VALUE])[0]
                #             # Load the certificate using the cryptography module
                #             cert = x509.load_der_x509_certificate(bytes(value), default_backend())
                #             # Print the subject of the certificate (i.e. the name of the owner of the Citizen Card)
                #             print(cert.subject)

                # # Close the session when you are finished
                # session.closeSession()

                # Add User to server users list
                new_id = len(users) + int(game['caller']==None)
                users[clt_addr] = higher_id = User( id=new_id, socket=clt_socket )
                # users[clt_id] = users[clt_addr[1]] # user can now be reached by id or addr port
                # len(users) += 1
                
                # cert = bytes( m.recv( clt_socket ) )
                # if encryption.verify_auth_cert(cert):
                #     print("Certificate Verified", clt_addr[1])

                # send to each client the created certificate
                cert = getCertificate()

                cert = signCertificate(cert,session)
                print("Certificate Signed", clt_addr[1])

                # m.send( clt_socket, cert )

                
                # hello messages to establish connection and set configs
                m.send_json( clt_socket, 'log', 'Connected to server on port '+str(clt_addr[1]) )
                m.send_json( clt_socket, 'set_config', config )

                update_users( users )

                print( 'Client added with port', clt_addr[1] )

                


            # Client data is available for reading
            else:
                data = m.recv( key.fileobj )
                clt_socket = key.fileobj
                clt_port = clt_socket.getpeername()
                clt_id = users[clt_port].id

                # Socket closed, remove client
                if data == None: 
                    del users[clt_port]
                    
                    # TODO if game is running need to abort
                    
                    # if caller closed socket
                    if clt_id==0:
                        game['caller'] = None
                    # if a player other than the last one
                    elif clt_id!=higher_id.id:
                        # replace the user with the higher id with the user that left
                        higher_id.id = clt_id
                        # find new higher_id
                        
                    # if player that left was the last
                    if clt_id==higher_id.id:
                        higher_id = None
                    
                    for i in users:
                        if higher_id==None or users[i].id > higher_id.id:
                            higher_id = users[i]
                        
                    
                    key.fileobj.close()
                    selector.unregister( key.fileobj )
                    
                    update_users( users )
                    print( 'Client removed' )
                    continue


                data = json.loads( data.decode( 'UTF-8' ) )
                body = data['body']
                
                ####### TESTS ########
                
                # user can ping the server (test connectivity with server)
                if data['header']['type'] == 'ping':
                    m.send_json( clt_socket, 'log', "PONG! " + body )
                    
                # message sent to all users (test connectivity with all users)
                elif data['header']['type'] == 'global':
                    msg = users[clt_port].nickname + ": " + body
                    sendall( users, -1, 'log', msg )
                    
                elif data['header']['type'] == 'global_signed':
                    msg = bytes( m.recv( clt_socket ) )
                    signature = bytes( m.recv( clt_socket ) )
                    public_key = bytes( m.recv( clt_socket ) )
                    sendall( users, clt_id, 'global_signed', {'nickname': users[clt_port].nickname} )
                    sendallb( users, clt_id, msg )
                    sendallb( users, clt_id, signature )
                    sendallb( users, clt_id, public_key )
                    
                    
                elif data['header']['type'] == 'global_encrypted':
                    msg = bytes( m.recv( clt_socket ) )
                    key = bytes( m.recv( clt_socket ) )
                    sendall( users, clt_id, 'global_encrypted', {'nickname': users[clt_port].nickname} )
                    sendallb( users, clt_id, msg )
                    sendallb( users, clt_id, key )
                    

                ####### SETTERS ######
                
                # user can set his nickname
                elif data['header']['type'] == 'set_nickname':
                    if clt_port == game['caller']:
                        m.send_json( users[clt_port].socket, 'log', "You are not allowed to change your nickname!" )
                        break
                    if body == "caller":
                        m.send_json( users[clt_port].socket, 'log', 'You can\'t set your nickname to that!' )
                        break
                        
                    # if nickname matches password then u can define this "user" as the admin (caller)
                    if game['caller']==None and body == "callerpassword":
                        game['caller'] = clt_port
                        users[clt_port].id = 0
                        users[clt_port].nickname = "Caller"
                        m.send_json( clt_socket, 'log', "You are now the Caller!" )
                    else:
                        users[clt_port].nickname = body

                    update_users( users )
                    print("Client at", clt_port, "as", body)
                    
                elif data['header']['type'] == 'set_public_key':
                    users[clt_port].public_key = bytes( m.recv( clt_socket ) )
                    update_users( users )
                    
                
                # caller starts the game
                elif data['header']['type'] == 'start':
                    # basic user tries to start the game
                    if game['state']=='STOPPED' and clt_id!=0:
                        m.send_json( clt_socket, 'log', 'You can\'t start the game, only the Caller can' )
                        continue
                    # caller tries to start the game with insuficient players
                    if game['state']=='STOPPED' and len(users) <= 2: # caller plus two users
                        m.send_json( clt_socket, 'log', 'Need at least two players to start!')
                        continue
                    
                    game['state'] = 'SHUFFLING'
                    
                    numbers = [i for i in range(1,config['n']+1)]
                    deck = b''.join([i.to_bytes(16, 'big') for i in numbers])
                    callerSocket = users[game['caller']].socket
                    m.send_json( callerSocket, 'shuffle' )
                    m.send( callerSocket, deck )

                # receive shuffle by user
                elif data['header']['type'] == 'shuffle':
                    # basic user tries to start the game
                    if game['state']!='SHUFFLING':
                        m.send_json( clt_socket, 'log', 'You can\'t shuffle now' )
                        continue
                    
                    # get data from clt
                    deck = bytes( m.recv( clt_socket ) )
                    signature = bytes( m.recv( clt_socket ) )
                    
                    # get current clt id
                    _id = game['curr_shuffler']%len(users)
                    
                    # logs
                    print("SHUFFLE DONE", game['curr_shuffler'])
                    shuffle_log.append( { 'id':_id, 'deck':deck, 'signature':signature } )
                    sendall( users, -1, 'shuffle_log', { 'id':_id } ) #, 'deck':deck, 'signature':signature })
                    sendallb( users, -1, deck )
                    sendallb( users, -1, signature )

                    # all players have shuffled and the caller is finishing the shuffling fase
                    if game['curr_shuffler']==len(users):
                        game['state'] = 'GETCARDS'
                        game['curr_shuffler'] = 0
                        game['n_cards'] = 0
                        
                        sendall( users, -1, 'get_card_and_keys')
                        continue
                        
                    # detect all other invalid cases
                    if clt_id!=_id:
                        m.send_json( clt_socket, 'log', 'Invalid action (shuffle)' )
                        continue

                    # calculate next user
                    game['curr_shuffler'] += 1
                    
                    # send shuffle request to next user
                    _id = (_id+1) % len(users)
                    next_user = [ users[i] for i in users if users[i].id==_id ][0]
                    m.send_json( next_user.socket, 'shuffle' )
                    m.send( next_user.socket, deck )

                # Handle the "report_cheat" message
                elif data['header']['type'] == 'report_cheat':
                    # Handle the "report_cheat" message
                    '''u cant report cheat if the game hasnt started yet'''
                    if game['state'] == 'STOPPED':
                        m.send_json( clt_socket, 'log', "You can't report cheating before the game has started!" )
                        break
                    numUsers = game['n_users']
                    for i in users:
                        if users[i].nickname == body:
                            j += 1
                            m.send_json( clt_socket, 'log', "You have reported cheating!" )
                            m.send_json( users[i].socket, 'log', "You have been reported for cheating!" )
                            if j > 2:
                                # Send a message telling the player to disconnect
                                m.send_json(users[i].socket, 'log', 'You have been forced to disconnect from the game. Please restart the game to reconnect.')
                                print(i)
                                print( "Client " + users[i].nickname + " removed due to cheating!")
                            
                                # Remove the user from the "users" dictionary the cheater not other player
                                del users[i]
                                
                                game['n_users'] -= 1
                                
                                # Update the users
                                update_users( users )
                              
                            j+=1
                            break
                    else:
                        m.send_json( clt_socket, 'log', "User not found!" )
                        game['state'] = 'STOPPED'
                        break


                
                elif data['header']['type'] == 'set_card_and_keys':
                    if game['state'] != 'GETCARDS':
                        m.send_json( clt_socket, 'log', 'you can\'t call (set_card_and_keys) now' )
                        continue  
                    # if len(body['card'])/16 != config['m']:
                    #     m.send_json( clt_socket, 'log', 'Wrong card length!' )
                    #     m.send_json( clt_socket, 'set_config', config )
                    #     continue    
                    
                    sendall( users, -1, 'update_card_and_keys', {'id':clt_id} )
                    
                    users[clt_port].card = bytes(m.recv( clt_socket ))
                    sendallb( users, -1, users[clt_port].card )
                    for i in range(0, 1+int(clt_id==0)):
                        users[clt_port].private_keys += [ bytes(m.recv( clt_socket )) ]
                        sendallb( users, -1, users[clt_port].private_keys[-1] )
                        
                    signature = bytes(m.recv( clt_socket ))
                    sendallb( users, -1, signature )

                    game['n_cards'] += 1
                    
                    
                    # sendall( users, -1, 'update_card_and_keys', {
                    #     'id': clt_id,
                    #     'card': body['card'],
                    #     'private_keys': body['private_keys'],
                    #     'signature': body['signature']
                    # } )
                    # print("Card",users[clt_id]['nickname'],":",body['card'])
                    
                    if game['n_cards'] == len(users):
                        print("All cards and keys received! Calculating winner...")
                        
                        sendall( users, -1, 'get_winner' )
                        
                        winners = {}
                        for i in users:
                            winners[users[i].nickname] = m.recv_json( users[i].socket )['body']
                        sendall( users, -1, 'none', winners)
                        print(winners)
                        

                        


def main(*args):
    if len(args)<1 and len(sys.argv) != 2:
        print( 'Usage: %s port' % (sys.argv[0]) )
        sys.exit( 1 )
    
    port = 0
    if len(args)==1:
        port = args[0]
    else:
        port = sys.argv[1]
    

    with socket.socket( socket.AF_INET, socket.SOCK_STREAM ) as s:
        s.bind( ('0.0.0.0', int(port) ) )
        s.listen()
        print("SERVER STARTED AT 127.0.0.1:"+port)
        dispatch( s )

if __name__ == '__main__':
    main()