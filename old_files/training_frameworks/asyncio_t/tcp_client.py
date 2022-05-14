import asyncio

async def tcp_connection(message):
    reader, writer = await asyncio.open_connection(
        'localhost', 5000
    )

    print(f'Message {message}')
    writer.write(message.encode())
    await writer.drain()

    data = await reader.read(100)

    print(f'Received: {data.decode()}')

    print('Close the connection')
    writer.close()
    await writer.wait_closed()

if __name__ == '__main__':
    asyncio.run(tcp_connection('Hello, world!'))
