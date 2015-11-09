__author__ = 'Zero'
from socket import *

BufferSize = 1024
Host = '59.64.113.201'
Port = 21567
Adr = (Host, Port)

try:
    tcpClientSock = socket(AF_INET, SOCK_STREAM)
    tcpClientSock.connect(Adr)

    while True:
        data = input('>')
        if not data:
            break
        tcpClientSock.send(data.encode())
        dataRecv = tcpClientSock.recv(BufferSize).decode()
        print(dataRecv)
except Exception as e:
    print(e)
    tcpClientSock.close()