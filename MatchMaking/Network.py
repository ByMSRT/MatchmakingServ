# import socket
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# server = 'localhost'
# port = 5555
#
# """ s.connect((server, port)) """
#
# mess = "Client connected"
#
# def connect():
#     s.connect((server, port))
#     mess = "Client connected"
#     try:
#         while True:
#             s.send(mess.encode('utf-8'))
#             data = s.recv(1024)
#             print(str(data))
#             more = input("Do you want to continue ? (y/n) ")
#             if more == "y":
#               mess = input("What do you want to send ? ")
#             else:
#                 break
#     except KeyboardInterrupt:
#         print("\nClosing connection")
#         s.close()
#

# ------------------------------------- Test ---------------------------------------------------

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 5555))

def connect():
    while True:
        full_msg = ''
        while True:
            msg = s.recv(8)
            if len(msg) <= 0:
                break
            full_msg += msg.decode("utf-8")

        if len(full_msg) > 0:
            print(full_msg)