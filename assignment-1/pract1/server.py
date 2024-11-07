# 1)UDP client server, client sends a string, server retuens the same string
# from socket import *
# ServerPort = 12000
# ServerSocket = socket(AF_INET, SOCK_DGRAM)
# ServerSocket.bind(('', ServerPort))
# print("Server is up!!")
# while True:
# 	msg, ClientAddress = ServerSocket.recvfrom(2048)
# 	modi_msg = msg.decode()
# 	ServerSocket.sendto(modi_msg.encode(), ClientAddress)

# 2)UDP client server, client sends a string, server converts to upper case
# from socket import *
# ServerPort = 12000
# ServerSocket = socket(AF_INET, SOCK_DGRAM)
# ServerSocket.bind(('', ServerPort))
# print("server is up!!")
# while True:
# 	msg, ClientAddress = ServerSocket.recvfrom(2048)
# 	modi_msg = msg.decode().upper()
# 	ServerSocket.sendto(modi_msg.encode(), ClientAddress)

# 3)UDP client, client sends a string, server calculates the strlength
# from socket import *
# ServerPort = 12000
# ServerSocket = socket(AF_INET, SOCK_DGRAM)
# ServerSocket.bind(('', ServerPort))
# print("Server is up!!")
# while True:
# 	msg, ClientAddress = ServerSocket.recvfrom(2048)
# 	msg = msg.decode()
# 	msglen = len(msg)
# 	ServerSocket.sendto(msg.encode(), ClientAddress)
# 	ServerSocket.sendto(str(msglen).encode(), ClientAddress)


# split_string function
# from socket import *
# ServerPort = 12000
# ServerSocket = socket(AF_INET, SOCK_DGRAM)
# ServerSocket.bind(('', ServerPort))
# print("server is up!!")
# while True:
# 	message, ClientAddress = ServerSocket.recvfrom(2048)
# 	message = message.decode()

# 	delimeter, ClientAddress = ServerSocket.recvfrom(2048)
# 	delimeter = delimeter.decode()

# 	modi_msg = message.split(delimeter)

# 	result = '\n'.join(modi_msg)
# 	ServerSocket.sendto(result.encode(), ClientAddress)


# Client sends a number to server, server calculates square of that no. and replies back to the client
# from socket import *
# ServerPort = 12000
# ServerSocket = socket(AF_INET, SOCK_DGRAM)
# ServerSocket.bind(('', ServerPort))
# print("server is up!!")
# while True:
# 	num, ClientAddress = ServerSocket.recvfrom(2048)
# 	num = int(num.decode())
# 	sqr = num * num
# 	ServerSocket.sendto(str(sqr).encode(), ClientAddress)



#10) first program with error handling
# from socket import *

# # Server configuration
# ServerPort = 12000

# # Create UDP socket
# try:
#     ServerSocket = socket(AF_INET, SOCK_DGRAM)
#     ServerSocket.bind(('', ServerPort))
#     print("Server is up!!")
# except Exception as e:
#     print(f"Failed to create or bind socket: {e}")
#     exit(1)

# # Main loop to handle client messages
# while True:
#     try:
#         # Receive message from client
#         msg, ClientAddress = ServerSocket.recvfrom(2048)
#         print(f"Received message from {ClientAddress}: {msg.decode()}")

#         # Process the message
#         modi_msg = msg.decode().upper()  # For example, converting message to uppercase

#         # Send modified message back to client
#         ServerSocket.sendto(modi_msg.encode(), ClientAddress)
#         print(f"Sent modified message to {ClientAddress}")

#     except Exception as e:
#         print(f"Error during communication: {e}")
#         break

# # Close server socket (in case the loop is exited)
# finally:
#     ServerSocket.close()
#     print("Server socket closed")
