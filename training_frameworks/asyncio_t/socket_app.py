import socket
import asyncio

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
socket_server.bind(('localhost',5000))
socket_server.listen()
clients = []

async def accept_connection(socket_server):
    global clients
    while True:
        socket_client, addr = socket_server.accept()
        print('Connection from', addr)
        clients.append(socket_client)

async def send_message(socket_client):
    while True:
        request = socket_client.recv(4096)

        if not request:
            print('Client is closed')
            socket_client.close()
        else:
            response = 'Hello, world\n'.encode()
            socket_client.send(response)  

async def main():
    task1 = asyncio.create_task(accept_connection(socket_server))
    tasks = []
    for i in clients:
        tasks.append(asyncio.create_task(send_message()))

    await asyncio.gather(task1, *tasks)

if __name__ == '__main__':
    asyncio.run(main())