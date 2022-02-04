import socket
import asyncio

users = 0
logs = []

async def accept_connection(socket_server):
    global users
    global logs
    print('Server is listening')
    loop = asyncio.get_event_loop()
    loop.create_task(show_count_of_users())
    while True:
        socket_client, addr = await loop.sock_accept(socket_server)
        print('Connection from', addr)
        users += 1
        logs.append(f'Connection from {socket_client} - {addr}')
        await add_client(socket_client)
        print('Added')


async def send_message(socket_client):
    loop = asyncio.get_event_loop()
    global users
    global logs
    while True:
        print('Read')
        print('Before sock recv')
        request = loop.sock_recv(socket_client, 4096)
        try:
            await asyncio.wait_for(request, timeout=60.0)
        except asyncio.TimeoutError:
            await loop.sock_sendall(socket_client, b'Connection was closed\n')
            break
        print('After sock recv')
        try:
            print(str(request))

            await loop.sock_sendall(socket_client, b'Hello, world\n')
        except:
            break
        print('End read request')
    socket_client.close()
    users -= 1

async def add_client(socket_client):
    loop = asyncio.get_event_loop()
    loop.create_task(send_message(socket_client))

async def show_count_of_users():
    while True:
        print(f'Users right now: {str(users)}')
        await asyncio.sleep(5)

async def main():
    print('Start')
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    socket_server.bind(('localhost',5000))
    socket_server.setblocking(False)
    socket_server.listen()
    print('Server is created')

    await accept_connection(socket_server)
    asyncio.get_event_loop().close()
    print('Close')

if __name__ == '__main__':
    asyncio.run(main())