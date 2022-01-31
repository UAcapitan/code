import socket
import asyncio

class Socket:
    def __init__(self):
        self.socket = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )
        self.socket.listen(5)
        self.loop = asyncio.get_event_loop()

    async def send_data(self, data):
        raise NotImplementedError()

    async def listen_socket(self, listened_socket=None):
        raise NotImplementedError()

    def set_up(self):
        self.socket.bind(('localhost', 5000))
        self.socket.setblocking(False)

if __name__ == '__main__':
    pass