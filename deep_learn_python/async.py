import socket
from select import select

sockets = []

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
socket_server.bind(('localhost',5000))
socket_server.listen()

def accept_connection(socket_server):
    socket_client, addr = socket_server.accept()
    print('Connection from', addr)
    sockets.append(socket_client)

def send_message(socket_client):
    request = socket_client.recv(4096)

    if request:
        response = 'Hello, world\n'.encode()
        socket_client.send(response)
    else:    
        sockets.remove(socket_client)    
        socket_client.close()

def event_loop():
    while True:
        read_sockets, _, _ = select(sockets, [], [])

        for sock in read_sockets:
            if sock is socket_server:
                accept_connection(sock)
            else:
                send_message(sock)

if __name__ == '__main__':
    sockets.append(socket_server)
    event_loop()