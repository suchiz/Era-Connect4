import socket

class Network():
    def __init__ (self):
        self.HOST = '127.0.0.1'
        self.PORT = 7777
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.s.connect((self.HOST, self.PORT))
    
    def listen(self):
        while True:
            data = self.s.recv(2048)
            print(data.decode())
    
    def send(self, data):
        self.s.sendall(data.encode())