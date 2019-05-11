import socket
import re
import threading

class Network():
    def __init__ (self, gameUI):
        self.HOST = '127.0.0.1'
        self.PORT = 7777
        self.s = None
        self.gameUI = gameUI
        self.error = False
        self.waitplayer = False
        self.stop_thread = False

    def connect(self):
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.connect((self.HOST, self.PORT))
            return True
        except socket.error:
            self.error = True
            self.gameUI.displayErrorMessage("Unable to reach server !")
            return False
        
    def listen(self):
        self.recv_thread = threading.Thread(target=self.recv_handler, args=(lambda: self.stop_thread,), daemon=True)
        self.recv_thread.start()

    def recv_handler(self, stop):
        while True:
            try:
                if stop():
                    break
                data = self.s.recv(2048)
                message = data.decode()
                infos = re.split("-", message)
                if infos[0] == 'playcoin':
                    self.gameUI.playCoin_FromNetwork(infos[1], infos[2], infos[3])
                elif infos[0] == 'StartGame':
                    self.waitplayer = False
                    self.gameUI.startGame_FromNetwork(int(infos[1]))
                    print(infos[1])
                elif infos[0] == 'WaitPlayer':
                    self.waitplayer = True
                    self.gameUI.board.player = 1
                    self.gameUI.displayWaitPlayer()
                elif infos[0] == 'ServerFull':
                    self.error = True
                    self.gameUI.displayErrorMessage("Server is full")
                elif infos[0] == 'Disconnected':
                    self.error = True
                    self.gameUI.board.gameOver()
                    self.gameUI.board.playAgain()
                    self.gameUI.displayErrorMessage("Your opponent raged quit")
                    exit(0)
            except socket.error as e:
                print(e)
                exit(0)
                

    def send(self, data):
        self.s.sendall(data.encode())

    def disconnect(self):
        self.stop_thread = True
        self.s.close()

    def setGameUI(self, gameUI):
        self.gameUI = gameUI