import socket

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
socket_server.bind(('localhost',5000))
socket_server.listen()

while True:
    socket_client, addr = socket_server.accept()
    print('Connection from', addr)

    while True:
        print('Input data')
        request = socket_client.recv(4096)
        print('Working')

        if not request:
            print('Error')
            break
        else:
            response = 'Hello, world\n'.encode()
            socket_client.send(response)
            
        print('Exit from server')
        socket_client.close()