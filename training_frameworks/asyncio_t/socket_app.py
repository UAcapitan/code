import socket
import asyncio

async def accept_connection(socket_server):
    print('Server is listening')
    loop = asyncio.get_event_loop()
    global clients
    while True:
        socket_client, addr = socket_server.accept()
        print('Connection from', addr)
        loop.create_task(send_message(socket_client))


async def send_message(socket_client):
    print('Read')
    while True:
        request = socket_client.recv(4096)

        if not request:
            print('Client is closed')
            socket_client.close()
        else:
            socket_client.send('Hello, world\n'.encode())
        print('End read request')

async def main():
    print('Start')
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    socket_server.bind(('localhost',5000))
    socket_server.listen()
    print('Server is created')

    loop = asyncio.get_running_loop()
    loop.create_task(accept_connection(socket_server))
    print('Server is added to loop')

if __name__ == '__main__':
    asyncio.run(main())