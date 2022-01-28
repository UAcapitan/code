import socket
from select import select

tasks = []

to_read = {}
to_write = {}

def server():
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    socket_server.bind(('localhost',5000))
    socket_server.listen()

    while True:
        yield ('read', socket_server)
        socket_client, addr = socket_server.accept()
        print('Connection from', addr)
        tasks.append(client(socket_client))

def client(socket_client):
    while True:
        yield ('read', socket_client)
        request = socket_client.recv(4096)

        if not request:
            break
        else:
            response = 'Hello, world\n'.encode()

            yield ('write', socket_client)
            socket_client.send(response)
    
    socket_client.close()

def event_loop():
    while any([tasks, to_read, to_write]):
        while not tasks:
            ready_to_read, ready_to_write, _ = select(to_read, to_write, [])

            for sock in ready_to_read:
                tasks.append(to_read.pop(sock))

            for sock in ready_to_write:
                tasks.append(to_write.pop(sock))
        
        try:
            task = tasks.pop(0)

            reason, sock = next(task)

            if reason == 'read':
                to_read[sock] = task
            if reason == 'write':
                to_write[sock] = task
        except:
            pass


if __name__ == '__main__':
    tasks.append(server())
    event_loop()