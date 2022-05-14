import asyncio


class EchoServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(self.peername))
        self.transport = transport

    def data_received(self, data):
        message = data.decode()
        print('Data received: {!r}'.format(message.replace('\n', '')))
        self.transport.write(str.encode('Thank you for your data!\n'))

    def connection_lost(self, exc):
        print('Close the client socket:', self.peername)
        self.transport.close()


async def main():
    loop = asyncio.get_running_loop()

    server = await loop.create_server(
        lambda: EchoServerProtocol(),
        'localhost', 5000)

    async with server:
        await server.serve_forever()


asyncio.run(main())