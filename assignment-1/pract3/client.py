# 5) ARP functionality using UDP
from socket import *
ServerPort = 12000
ServerName = "localhost"
ClientSocket = socket(AF_INET, SOCK_DGRAM)
ip_add = input("enter an IP address: ")
ClientSocket.sendto(ip_add.encode(), (ServerName, ServerPort))
mac_ad, ServerAddress = ClientSocket.recvfrom(2048)
print(f"the mac address for for ip {ip_add}: {mac_ad}")
print(f"server address: {ServerAddress}")
ClientSocket.close()