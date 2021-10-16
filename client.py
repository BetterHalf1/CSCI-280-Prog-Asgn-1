# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 11:27:53 2021

@author: kenne
"""

from socket import *
serverName = '127.0.0.1'
proxyPort = 13001
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, proxyPort))
sentence = input('Input lowercase sentence:')

clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print('From Proxy:', modifiedSentence.decode())
clientSocket.close()
