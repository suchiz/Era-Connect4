import socket

HOST = '127.0.0.1'
PORT = 7777


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    data = s.recv(2048)
    print(data.decode())
