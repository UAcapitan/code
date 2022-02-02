import socket
import asyncio

async def accept_connection(socket_server):
    print('Server is listening')
    while True:
        loop = asyncio.get_event_loop()
        socket_client, addr = await loop.sock_accept(socket_server)
        print('Connection from', addr)
        loop.create_task(send_message(socket_client))
        print('Added')
        await asyncio.sleep(1/1000)


async def send_message(socket_client):
    while True:
        print('Read')
        loop = asyncio.get_event_loop()
        request = await loop.sock_recv(socket_client, 4096)

        if not request:
            print('Client is closed')
            socket_client.close()
        else: 
            await loop.sock_sendall(socket_client, 'Hello, world\n'.encode())
        print('End read request')
        socket_client.close()
        await asyncio.sleep(1)

async def main():
    print('Start')
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    socket_server.bind(('localhost',5000))
    socket_server.listen()
    print('Server is created')

    task = asyncio.create_task(accept_connection(socket_server))
    # asyncio.gather(task)
    await task

if __name__ == '__main__':
    asyncio.run(main())