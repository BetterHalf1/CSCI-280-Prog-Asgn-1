from socket import *

serverName = '127.0.0.1'

serverPort = 12002
proxySocket = socket(AF_INET, SOCK_STREAM)
proxySocket.bind(('', 13001))
proxySocket.listen(1)
print('The proxy is online')

while True:
    connectionSocket, addr = proxySocket.accept()

    sentence = connectionSocket.recv(1024)
    if sentence:
        print(sentence)
    newSocket = socket(AF_INET, SOCK_STREAM)
    newSocket.connect((serverName, serverPort))
    newSocket.sendall(sentence)

    newsentence = newSocket.recv(1024)
    if newsentence:
        print(newsentence)
    connectionSocket.sendall(newsentence)
    connectionSocket.close()
    newSocket.close()
