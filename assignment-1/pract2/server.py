# 4) Create a DNS Server using UDP
from socket import *
dns_records = {
	"example.com": "93.184.216.34",
	"google.com": "142.250.190.78",
    "openai.com": "104.18.6.14"
}

Server_socket = socket(AF_INET, SOCK_DGRAM)
Server_socket.bind(('', 12000))
print("DNS server is up!!")
while True:
	msg, ClientAddress = Server_socket.recvfrom(2048)
	domain = msg.decode().strip()
	ip_add = dns_records.get(domain, "domain not found")
	Server_socket.sendto(ip_add.encode(), ClientAddress)