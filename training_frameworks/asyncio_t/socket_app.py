import socket

class Socket:
    def __init__(self):
        self.socket = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

    def send_data(self, data):
        raise NotImplementedError()

    def listen_socket(self, listened_socket=None):
        raise NotImplementedError()

    def set_up(self):
        raise NotImplementedError()

if __name__ == '__main__':
    pass