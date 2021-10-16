# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 11:33:29 2021

@author: kenne
"""

from socket import *

serverPort = 12002
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')


while True:

    connectionSocket, addr = serverSocket.accept()

    sentence = connectionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    if capitalizedSentence:
        print(capitalizedSentence)
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()


print("Server terminated")
