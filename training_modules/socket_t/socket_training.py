import socket

# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind(('127.0.0.1', 2000))

class Server:
    def __init__(self):
        self.server = socket.create_server(('127.0.0.1', 2000))
        self.server.listen(4)
        self.HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'.encode('utf-8')

    def run(self):
        try:
            while True:
                self.client_socket, self.address = self.server.accept()
                data = self.client_socket.recv(1024).decode('utf-8')
                text = self.load_file(data)
                self.client_socket.send(text)
                self.client_socket.shutdown(socket.SHUT_WR)
        except:
            print('Error')
            self.server.close()

    def load_file(self, data):
        path = data.split()[1]
        result = ''
        with open('views' + path, 'rb') as file:
            result = file.read()
        print(self.HDRS + result)
        return self.HDRS + result
            
if __name__ == '__main__':
    server = Server()
    server.run()