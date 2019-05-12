import socket
import sys
import threading
import re

connection_list = []

def waiting_handler(conn, adr):
    data = conn.recv(2048)
    if not data: 
        print(str(adr[0]) + ":" + str(adr[1]) + " has disconnected" )
        connection_list.remove(conn)
        print (len(connection_list))
        conn.close()

def handler(conn, adr):
    while True:
        data = conn.recv(2048)
        if not data: 
            print(str(adr[0]) + ":" + str(adr[1]) + " has disconnected" )
            connection_list.remove(conn)
            print (len(connection_list))
            break
        if len(connection_list) < 2:
            message = "Disconnected-"
            conn.sendall(message.encode())
            connection_list.remove(conn)
            print (len(connection_list))
            break
        try:
            for mconn in connection_list:
                mconn.sendall(data)
        except socket.error:
            print(str(adr[0]) + ":" + str(adr[1]) + " has disconnected" )
            connection_list.remove(conn)
            print (len(connection_list))
    conn.close()

HOST = ''
PORT = 7777

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
print ("Server is running ...")

while True:
    conn, adr = s.accept()
    print(str(adr[0]) + ":" + str(adr[1]) + " has arrived" )
    connection_list.append(conn)
    print (len(connection_list))

    if len(connection_list) < 2:
        message = "WaitPlayer-"
        conn.sendall(message.encode())
        welcome_thread = threading.Thread(target = waiting_handler, args = (conn, adr))
        welcome_thread.daemon = True
        welcome_thread.start()
    elif len(connection_list) == 2:
        try:
            for ind, mconn in enumerate(connection_list):
                message = "StartGame-"+str(ind)
                mconn.sendall(message.encode())
                conn_thread = threading.Thread(target = handler, args = (mconn, adr))
                conn_thread.daemon = True
                conn_thread.start()
        except socket.error:
            print("Error")
            connection_list = []
    elif len(connection_list) > 2:
        message = "ServerFull-"
        conn.sendall(message.encode())
        connection_list.remove(conn)
        conn.close()
        
s.close()



