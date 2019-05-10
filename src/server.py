import socket
import sys
from _thread import *
import re

socket_list = []

def clientThread(conn):
    while True:
        data = conn.recv(2048)
        if not data: break
        print("Received in server: ", data.decode())
        for mconn in socket_list:
            mconn.sendall(data)
    conn.close()

HOST = '127.0.0.1'
PORT = 7777

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
print ("Server is running ...")

while True:
    conn, adr = s.accept()
    socket_list.append(conn)
    print(socket_list)
    print("Someone has arrived: ")
    start_new_thread(clientThread, (conn,))

s.close()




