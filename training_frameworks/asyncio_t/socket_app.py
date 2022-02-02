import socket
import asyncio

async def accept_connection(socket_server):
    print('Server is listening')
    loop = asyncio.get_event_loop()
    while True:
        socket_client, addr = await loop.sock_accept(socket_server)
        print('Connection from', addr)
        loop.create_task(send_message(socket_client))
        print('Added')


async def send_message(socket_client):
    loop = asyncio.get_event_loop()
    while True:
        print('Read')
        print('Before sock recv')
        request = await loop.sock_recv(socket_client, 4096)
        print('After sock recv')
        if not request:
            socket_client.close()
        else:
            await loop.sock_sendall(socket_client, 'Hello, world\n'.encode())
            print('End read request')

async def main():
    print('Start')
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    socket_server.bind(('localhost',5000))
    socket_server.setblocking(False)
    socket_server.listen()
    print('Server is created')

    await accept_connection(socket_server)

if __name__ == '__main__':
    asyncio.run(main())