__author__ = 'Zero'

from socket import *
from time import *

BufferSize = 1024
Host = ''
Port = 21567
Adr = (Host, Port)

tcpSocket = socket(AF_INET, SOCK_STREAM)
tcpSocket.bind(Adr)
tcpSocket.listen(20)
s1 = getfqdn('')
s2 = gethostbyname(Host)
while(True):
    print('Ready Accept')
    clientSock, addinfo = tcpSocket.accept()
    print('Accept Info')

    sendData = ctime()
    while True:
        data = clientSock.recv(BufferSize).decode()
        if not data:
            break
        clientSock.send(('[%s] %s' % (ctime(), data)).encode())

    clientSock.close()
tcpSocket.close()
