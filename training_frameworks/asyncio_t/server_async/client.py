import asyncio


class EchoClientProtocol(asyncio.Protocol):
    def __init__(self, message, on_con_lost):
        self.message = message
        self.on_con_lost = on_con_lost

    def connection_made(self, transport):
        transport.write(self.message.encode())
        print('Data sent: {!r}'.format(self.message))

    def data_received(self, data):
        print('Data received: {!r}'.format(data.decode()))

    def connection_lost(self, exc):
        self.on_con_lost.set_result(True)


async def main():
    loop = asyncio.get_running_loop()

    while True:
        on_con_lost = loop.create_future()
        message = input('Message to server: ')

        transport, protocol = await loop.create_connection(
            lambda: EchoClientProtocol(message, on_con_lost),
            'localhost', 5000)

        transport.close()


asyncio.run(main())