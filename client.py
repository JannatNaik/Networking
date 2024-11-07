from socket import *
ServerName = "localhost"
ServerPort = 12000
ClientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Input Lowercase sentence: ')
ClientSocket.sendto(message.encode(), (ServerName,ServerPort))
modi_mesg, ServerAddress = ClientSocket.recvfrom(2048)
msg_len, ServerAddress = ClientSocket.recvfrom(2048)
print(modi_mesg.decode(), ServerAddress)
print(msg_len.decode(), ServerAddress)
ClientSocket.close()