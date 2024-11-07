# 3) Create a UDP client server program where the client sends a string, server calculates the length and replies
from socket import *
ServerPort = 12000
ServerSocket = socket(AF_INET, SOCK_DGRAM)
ServerSocket.bind(('', ServerPort))
print("the Server is ready to receive")
while True:
    message, ClientAddress = ServerSocket.recvfrom(2048)
    modi_mesg = message.decode()
    msg_len = len(modi_mesg)
    # print(message.decode(), ClientAddress)
    ServerSocket.sendto(modi_mesg.encode(), ClientAddress)
    ServerSocket.sendto(str(msg_len).encode(), ClientAddress)
    # socket.close(ServerSocket)