# 1)UDP client server, client sends a string, server sends the same string
# from socket import *
# ServerName = "localhost"
# ServerPort = 12000
# ClientSocket = socket(AF_INET, SOCK_DGRAM)
# message = input('Input a string: ')
# ClientSocket.sendto(message.encode(), (ServerName, ServerPort))
# modi_mesg, ServerAddress = ClientSocket.recvfrom(2048)
# print(modi_mesg.decode(), ServerAddress)
# ClientSocket.close()



# 2)UDP client server, client sends a string, server converts to upper case
# from socket import *
# ServerName = "localhost"
# ServerPort = 12000
# ClientSocket = socket(AF_INET, SOCK_DGRAM)
# message = input('Input a String in upper case: ')
# ClientSocket.sendto(message.encode(), (ServerName, ServerPort))
# modi_mesg, ServerAddress = ClientSocket.recvfrom(2048)
# print(modi_mesg.decode(), ServerAddress)
# ClientSocket.close()

# 3)UDP client, client sends a string, server calculates the strlength
# from socket import *
# ServerName = "localhost"
# ServerPort = 12000
# ClientSocket = socket(AF_INET, SOCK_DGRAM)
# message = input('input a string: ')
# ClientSocket.sendto(message.encode(), (ServerName, ServerPort))
# modi_mesg, ServerAddress = ClientSocket.recvfrom(2048)
# msglen, ServerAddress = ClientSocket.recvfrom(2048)
# print(modi_mesg.decode(), ServerAddress)
# print(msglen.decode())
# ClientSocket.close()

# split_string client
# from socket import *
# ServerName = "localhost"
# ServerPort = 12000
# ClientSocket = socket(AF_INET, SOCK_DGRAM)
# message = input("enter a string: ")
# delimeter = input("enter a delimeter: ")
# if not delimeter:
# 	delimeter = ' '
# ClientSocket.sendto(message.encode(), (ServerName, ServerPort))
# ClientSocket.sendto(delimeter.encode(), (ServerName, ServerPort))
# modi_msg, ServerAddress = ClientSocket.recvfrom(2048)
# print(modi_msg.decode(), ServerAddress)
# ClientSocket.close()


# Client sends a number to server, server calculates square of that no. and replies back to the client
# from socket import *
# Servername = "localhost"
# ServerPort = 12000
# ClientSocket = socket(AF_INET, SOCK_DGRAM)
# num = int(input("enter a number: "))
# ClientSocket.sendto(str(num).encode(), (Servername, ServerPort))
# sqr_num, ServerAddress = ClientSocket.recvfrom(2048)
# print("squared number: ", int(sqr_num.decode()), ServerAddress)
# ClientSocket.close()

# date time program
# from datetime import datetime
# def display_curr_date():
# 	now = datetime.now()
# 	cur_date = now.strftime("%y-%m-%d")
# 	print("current date: ",cur_date)

# if __name__ == '__main__':
# 	display_curr_date()


# program to get ip Address and hostname
# import socket
# hostname = socket.gethostname()
# print(hostname)
# ip_add = socket.gethostbyname(hostname)
# print("ip addres: ", ip_add)



# program to get macAddress
# import uuid
# mac_add = hex(uuid.getnode()).replace('0x', '').upper()
# format_mac = ':'.join(mac_add[i:i+2]for i in range(0, len(mac_add),2))
# print("macAddress: ", format_mac)


# portscanner
# from socket import *
# def portscanner(target, ports):
# 	code = socket.gethostbyname(target)
# 	print(f"Scanning {target} ({code})")

# 	for port in ports:
# 		sock = socket(AF_INET, SOCK_STREAM)
# 		socket.setdefaulttimeout(1)
# 		result = sock.connect_ex((code, port))
# 		if result == 0:
# 			print(f"Port {port}: open")

# 		sock.close()

# if __name__ == '__main__':
# 	tar = input("enter hostname: ")
# 	por = input("enter ports you want to scan (separated by commas): ")
# 	ports = [int(port) for p in por.split(", ")]
# 	portscanner(tar, por)



#10) first program with error handling
# from socket import *

# # Client configuration
# ServerName = "localhost"
# ServerPort = 12000

# # Create UDP socket
# try:
#     ClientSocket = socket(AF_INET, SOCK_DGRAM)

#     # Get user input
#     message = input('Input a string: ')

#     # Send the message to the server
#     ClientSocket.sendto(message.encode(), (ServerName, ServerPort))
#     print(f"Sent message to server: {message}")

#     # Receive the modified message from the server
#     modi_mesg, ServerAddress = ClientSocket.recvfrom(2048)
#     print(f"Received modified message from server: {modi_mesg.decode()}")

# except Exception as e:
#     print(f"Error during communication: {e}")

# # Close client socket
# finally:
#     ClientSocket.close()
#     print("Client socket closed")
