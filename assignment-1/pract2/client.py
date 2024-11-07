# 4) Create a DNS Server using UDP
from socket import *
Client_socket = socket(AF_INET, SOCK_DGRAM)
ServerAddress = (('localhost', 12000))
domain = input("enter a domain name: ")
Client_socket.sendto(domain.encode(), ServerAddress)
res, ser = Client_socket.recvfrom(2048)
print(f"ip address for domain name {domain}: {res.decode()}", ser)
	