import socket

class Connection:
    def __init__(self):
        self.test = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


    def get_client_ip(self):
        ## getting the hostname by socket.gethostname() method
        hostname = socket.gethostname()
        ## getting the IP address using socket.gethostbyname() method
        ip_address = socket.gethostbyname(hostname)
        ## printing the hostname and ip_address
        print(f"Hostname: {hostname}")
        print(f"IP Address: {ip_address}")