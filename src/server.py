import socket
import sys
import threading
import re

connection_list = []

def handler(conn, adr):
    while True:
        data = conn.recv(2048)
        if not data: 
            print(str(adr[0]) + ":" + str(adr[1]) + " has disconnected" )
            connection_list.remove(conn)
            conn.close()
            break
        print("Received in server: ", data.decode())
        for mconn in connection_list:
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
    print(str(adr[0]) + ":" + str(adr[1]) + " has arrived" )
    conn_thread = threading.Thread(target = handler, args = (conn, adr))
    conn_thread.daemon = True
    conn_thread.start()
    connection_list.append(conn)

s.close()




