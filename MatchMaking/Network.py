import threading
import socket
from TicTacToe.Grid import Grid
from TicTacToe.Game import Game


# 141.95.166.131

# Try connecting to the server
def connect():
    array_of_player = []
    alias = getter.connect_user()
    array_of_player.append(alias)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('141.95.166.131', 5555))
    receive_thread = threading.Thread(
        target=client_receive, args=(client, alias))
    receive_thread.start()
    send_thread = threading.Thread(target=client_send, args=(client, alias))
    send_thread.start()

# Receive messages from the server


def client_receive(client, alias):
    while True:
        try:
            message = client.recv(4096).decode('utf-8')
            if message == "alias?":
                client.send(alias.encode('utf-8'))
            else:
                print(message)

            if message == "La partie va pourvoir commencer !":
                client.send(
                    f"Broadcast : la partie va commencer... \n{grid.grid_creation()}".encode('utf-8'))

        except:
            print('Error!')
            client.close()
            break

# Send messages to the server


def client_send(client, alias):
    while True:
        message = f'{alias}: {input("")}'
        client.send(message.encode('utf-8'))


getter = Game('Tic Tac Toe')
grid = Grid()
