import socket
import json


############ SEND ############

def send( socket, data ):
    length = len(data).to_bytes( 4, 'big' )# 4-byte integer, network byte order (Big Endian)
    socket.send( length )
    socket.send( data )
    
# if no body is None this is considered GET request, else POST
def send_json( socket, type, body=None ): 
    data = {
        'header': {
            "type": type
        },
        'body': body
    }
    send( socket, json.dumps( data ).encode( 'UTF-8' ) )

########## END SEND ##########


########### RECEIVE ##########

def exact_recv( socket, length ):
    data = bytearray( 0 )

    while len(data) != length:
        more_data = socket.recv( length - len(data) )
        if len(more_data) == 0: # End-of-File
            return None
        data.extend( more_data )
    return data


def recv( socket ):
    data = exact_recv( socket, 4 ) # 4-byte integer, network byte order (Big Endian)
    if data == None:
        return None

    length = int.from_bytes( data, 'big' )
    return exact_recv( socket, length )


def recv_json( socket ):
    data = exact_recv( socket, 4 ) # 4-byte integer, network byte order (Big Endian)
    if data == None:
        return None

    length = int.from_bytes( data, 'big' )
    data = exact_recv( socket, length )
    data = json.loads( data.decode( 'UTF-8' ) )
    return data


###### END RECEIVE ########