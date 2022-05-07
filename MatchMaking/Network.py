import threading
import socket


def connect():
    alias = input('Choose an alias >>> ')
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('141.95.166.131', 5555))
    receive_thread = threading.Thread(
        target=client_receive, args=(client, alias))
    receive_thread.start()
    send_thread = threading.Thread(target=client_send, args=(client, alias))
    send_thread.start()


def client_receive(client, alias):
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == "alias?":
                client.send(alias.encode('utf-8'))
            else:
                print(message)
        except:
            print('Error!')
            client.close()
            break


def client_send(client, alias):
    while True:
        message = f'{alias}: {input("")}'
        client.send(message.encode('utf-8'))
