# 5) ARP functionality using UDP
from socket import *
arp_table = {
    "192.168.1.1": "00:0a:95:9d:68:16",
    "192.168.1.2": "00:0a:95:9d:68:17",
    "192.168.1.3": "00:0a:95:9d:68:18",
    "192.168.1.4": "00:0a:95:9d:68:19"
}

ServerPort = 12000
ServerSocket = socket(AF_INET, SOCK_DGRAM)
ServerSocket.bind(('', ServerPort))
print("server is up!!")

while True:
	ip_add, ClientAddress = ServerSocket.recvfrom(2048)
	ip_add = ip_add.decode()
	print("Received an ARP request")
	mac_add = arp_table.get(ip_add, "ip address not found")
	ServerSocket.sendto(mac_add.encode(), ClientAddress)

