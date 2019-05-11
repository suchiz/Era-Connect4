import socket
import re
import threading

class Network():
    def __init__ (self):
        self.HOST = '127.0.0.1'
        self.PORT = 7777
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.gameUI = None

    def connect(self):
        self.s.connect((self.HOST, self.PORT))
        
    def listen(self):
        recv_thread = threading.Thread(target= self.recv, args=(), daemon=True)
        recv_thread.start()


    def recv(self):
        while True:
            data = self.s.recv(2048)
            message = data.decode()
            infos = re.split("-", message)
            if infos[0] == 'playcoin':
                self.gameUI.displayCoin2(infos[1], infos[2], infos[3])

    def send2(self, data):
        recv_thread = threading.Thread(target= self.send2, args=(), daemon=True)
        recv_thread.start()

    def send(self, data):
        self.s.sendall(data.encode())

    def setGameUi(self, gameUI):
        self.gameUI = gameUI