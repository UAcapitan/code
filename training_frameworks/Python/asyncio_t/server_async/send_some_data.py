import socket

while True:
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect(("localhost",5000))
    data = input('Input your data: ')
    clientSocket.send(data.encode())
    dataFromServer = clientSocket.recv(4096)
    print('Server send this:', dataFromServer.decode())