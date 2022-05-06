import socket
from _thread import *
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = 'localhost'
port = 5555

server_ip = socket.gethostbyname(server)

def start():
    s.bind((server, port))
    s.listen(5)
    print("Server started")
    while True:
        conn, addr = s.accept()
        print("Connected to: ", addr)
        start_new_thread(threaded_client, (conn,))
        print ("New thread started", conn)

def threaded_client(conn):
    conn.send(str.encode("Welcome, type your info\n"))
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")
            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", reply)
                print("Sending: ", reply)
                conn.sendall(str.encode(reply))
        except:
            break

    print("Lost connection")
    conn.close()
