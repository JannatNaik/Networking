# 1) Create a TCP client server program where the client sends a string, server replies back the same string
# from socket import *
# Serverport = 12000
# Serversocket = socket(AF_INET, SOCK_STREAM)

# Serversocket.bind(('', Serverport))
# Serversocket.listen(1)
# print("The server is up!!")

# while True:
#     conn_socket, Clientadd = Serversocket.accept()
#     msg = conn_socket.recv(2048).decode()
#     conn_socket.send(msg.encode())
#     conn_socket.close()

# Serversocket.close()


# 2) Create a TCP client server program where the client sends a string, server converts to upper case and replies
# from socket import *
# Serverport = 12000
# Serversocket = socket(AF_INET, SOCK_STREAM)

# Serversocket.bind(('', Serverport))
# Serversocket.listen(1)
# print("Server is up!!")

# while True:
# 	conn_socket, Clientadd = Serversocket.accept()
# 	msg = conn_socket.recv(2048).decode()
# 	modimsg = msg.upper()
# 	conn_socket.send(modimsg.encode())
# 	conn_socket.close()


# 3) Create a TCP client server program where the client sends a string, server calculates the length and replies
# from socket import *
# Serverport = 12000
# Serversocket  = socket(AF_INET, SOCK_STREAM)

# Serversocket.bind(('', Serverport))
# Serversocket.listen(1)
# print("Server is up!!")

# while True:
# 	conn_socket, Clientadd = Serversocket.accept()
# 	msg = conn_socket.recv(2048).decode()
# 	msglen = str(len(msg))
# 	conn_socket.send(msg.encode())
# 	conn_socket.send(msglen.encode())
# 	conn_socket.close()


# 4) Create a DNS Server using TCP
# from socket import *
# dns_records = {
# 	"example.com": "93.184.216.34",
# 	"google.com": "142.250.190.78",
#     "openai.com": "104.18.6.14"
# }

# Serversocket = socket(AF_INET, SOCK_STREAM)
# Serversocket.bind(('', 12000))
# Serversocket.listen(1)
# print("DNS server is up!!")
# while True:
# 	conn_socket, ClientAddress = Serversocket.accept()
# 	msg = conn_socket.recv(2048).decode()
# 	domain = msg.strip()
# 	ip_add = dns_records.get(domain, "domain not found")
# 	conn_socket.send(ip_add.encode())


# 5) Create a simulation of ARP protocol using TCP
# from socket import *
# arp_table = {
#     "192.168.1.1": "00:0a:95:9d:68:16",
#     "192.168.1.2": "00:0a:95:9d:68:17",
#     "192.168.1.3": "00:0a:95:9d:68:18",
#     "192.168.1.4": "00:0a:95:9d:68:19"
# }

# ServerPort = 12000
# ServerSocket = socket(AF_INET, SOCK_STREAM)
# ServerSocket.bind(('', ServerPort))
# ServerSocket.listen(1)
# print("ARP server is up!!")

# while True:
# 	conn_socket, ClientAddress = ServerSocket.accept()
# 	ip_add = conn_socket.recv(2048).decode()
# 	print("Received an ARP request")
# 	mac_add = arp_table.get(ip_add, "ip address not found")
# 	conn_socket.send(mac_add.encode())


# 10) Any program from 1 to 5 using error handling
# from socket import *
# def start_server():
#     try:
#         server_port = 12000
#         server_socket = socket(AF_INET, SOCK_STREAM)
#         server_socket.bind(('', server_port))
#         server_socket.listen(1)
#         print("Server is up !!, ", server_port)
        
#         while True:
#             connection_socket, client_address = server_socket.accept()
#             try:
#                 message = connection_socket.recv(2048).decode()

#                 if not message:
#                     print("Empty message received. Closing connection.")
#                     connection_socket.close()
#                     continue
#                 connection_socket.send(message.encode())
#                 print(f"Echoed back: {message}")

#             except ConnectionResetError:
#                 print("Connection reset by client.")
#             except Exception as e:
#                 print(f"Error during communication: {e}")
#             finally:
#                 # Close the connection after replying
#                 connection_socket.close()
#                 print(f"Connection with {client_address} closed.")

#     except OSError as e:
#         print(f"Socket error: {e}")
#     except Exception as e:
#         print(f"Server encountered an error: {e}")
#     finally:
#         server_socket.close()
#         print("Server socket closed.")

# if __name__ == "__main__":
#     start_server()

