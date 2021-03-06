import threading
import socket
host = '141.95.166.131'
#host_local = 'localhost'
port = 5555
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
clients = []
aliases = []
players = []

# Send message to all clients


def broadcast(message):
    for client in clients:
        client.send(message)

# Handle clients


def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            alias = aliases[index]
            broadcast(f'{alias} has left the chat room!'.encode('utf-8'))
            players.remove(alias)
            aliases.remove(alias)
            break


# Accept new clients
def receive():
    while True:
        print('Server is running and listening ...')
        client, address = server.accept()
        print(f'connection is established with {str(address)}')
        client.send('alias?'.encode('utf-8'))
        alias = client.recv(1024)
        aliases.append(alias)
        clients.append(client)
        players.append(alias)
        print(players)
        print(f'The alias of this client is {alias}'.encode('utf-8'))
        broadcast(f'{alias} has connected to the chat room'.encode('utf-8'))
        print(clients)
        client.send('you are now connected!'.encode('utf-8'))
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()
        if len(clients) == 2:
            print('2 clients are connected')
            player_str = str(players)
            broadcast(f'Players : {player_str}'.encode('utf-8'))
            client.send('La partie va pourvoir commencer !'.encode('utf-8'))
            reply = client.recv(4096)
            broadcast(reply.encode('utf-8'))
            print(player_str)


if __name__ == "__main__":
    receive()
