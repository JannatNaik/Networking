# 1) Create a TCP client server program where the client sends a string, server replies back the same string
# from socket import *
# Servername = "localhost"
# Serverport = 12000
# Clientsocket = socket(AF_INET, SOCK_STREAM)
# Clientsocket.connect((Servername, Serverport))
# msg = input("enter a string: ")
# Clientsocket.send(msg.encode())


# modi_msg = Clientsocket.recv(2048).decode()
# print(f"the string returned from server: {modi_msg}")

# Clientsocket.close()


# 2) Create a TCP client server program where the client sends a string, server converts to upper case and replies
# from socket import *

# Servername = "localhost"
# Serverport = 12000
# Clientsocket = socket(AF_INET, SOCK_STREAM)
# Clientsocket.connect((Servername, Serverport))
# msg = input("Enter a string: ")
# Clientsocket.send(msg.encode())

# modi_msg = Clientsocket.recv(2048).decode()
# print(f"String converted to upper: {modi_msg}")

# Clientsocket.close()


# 3) Create a TCP client server program where the client sends a string, server calculates the length and replies
# from socket import *
# Servername = "localhost"
# Serverport = 12000
# Clientsocket = socket(AF_INET, SOCK_STREAM)
# Clientsocket.connect((Servername, Serverport))
# msg = input("Enter a string: ")
# Clientsocket.send(msg.encode())
# msgr = Clientsocket.recv(2048).decode()
# msglen = Clientsocket.recv(2048).decode()
# print(f"Given string: {msgr}")
# print(f"Length of the given string: {msglen}")

# Clientsocket.close()


# 4) Create a DNS Server using TCP
# from socket import *
# Clientsocket = socket(AF_INET, SOCK_STREAM)
# Clientsocket.connect(('localhost', 12000))
# domain = input("enter a domain name: ")
# Clientsocket.send(domain.encode())
# res = Clientsocket.recv(2048)
# print(f"ip address for domain name {domain}: {res.decode()}")



# 5) Create a simulation of ARP protocol using TCP
# from socket import *
# # ServerPort = 12000
# # ServerName = "localhost"
# ClientSocket = socket(AF_INET, SOCK_STREAM)
# ClientSocket.connect(('localhost', 12000))
# ip_add = input("enter an IP address: ")
# ClientSocket.send(ip_add.encode())
# mac_ad = ClientSocket.recv(2048)
# print(f"the mac address for for ip {ip_add}: {mac_ad}")

# ClientSocket.close()


# 6) Portscanner
# from socket import *
# def portscanner(target, ports):
# 	code = gethostbyname(target)
# 	print(f"Scanning {target} ({code})")

# 	for port in ports:
# 		sock = socket(AF_INET, SOCK_STREAM)
# 		sock.settimeout(1)
# 		result = sock.connect_ex((code, port))
# 		if result == 0:
# 			print(f"Port {port}: open")
# 		else:
#   			print(f"Port {port}: closed")

# 		sock.close()

# if __name__ == '__main__':
# 	tar = input("enter hostname: ")
# 	por = input("enter ports you want to scan (separated by commas): ")
# 	ports = [int(port) for port in por.split(", ")]
# 	portscanner(tar, ports)


# 7) Program to show MAC Address of your system
# import uuid
# mac_add = hex(uuid.getnode()).replace('0x', '').upper()
# format_mac = ':'.join(mac_add[i:i+2]for i in range(0, len(mac_add),2))
# print("macAddress: ", format_mac)


# 8) Program to show IP Address of your system
# 9) Program to shown Hostname of your system
# from socket import *
# hostname = gethostname()
# print(hostname)
# ip_add = gethostbyname(hostname)
# print("ip addres: ", ip_add)


# 10) Any program from 1 to 5 using error handling
# from socket import *

# def start_client():
#     try:
#         server_name = 'localhost'
#         server_port = 12000
#         client_socket = socket(AF_INET, SOCK_STREAM)
#         client_socket.connect((server_name, server_port))
#         message = input("Enter a message: ")

#         if not message:
#             print("Empty message. Closing connection.")
#             client_socket.close()
#             return

#         client_socket.send(message.encode())
#         response = client_socket.recv(2048).decode()
#         print(f"Server echoed: {response}")

#     except ConnectionRefusedError:
#         print("Connection refused by the server. Ensure the server is running.")
#     except TimeoutError:
#         print("Connection timed out. Please try again.")
#     except OSError as e:
#         print(f"Socket error: {e}")
#     except Exception as e:
#         print(f"An error occurred: {e}")
#     finally:
#         client_socket.close()
#         print("Client socket closed.")

# if __name__ == "__main__":
#     start_client()

