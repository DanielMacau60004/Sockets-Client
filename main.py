from socket import *

clientSocket = socket(AF_INET, SOCK_DGRAM)

serverName = "localhost"
serverPort = 25565

message = input("Input lowercase sequence: ")

clientSocket.sendto(message.encode(), (serverName, serverPort))

modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

print(modifiedMessage.decode())

clientSocket.close()