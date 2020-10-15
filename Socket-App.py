from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen()

while True:
    print ('waiting for connection...')
    tcpCliSock, addr = tcpSerSock.accept()
    print ('connected with ', addr)

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        tcpCliSock.send('[%s] %s' %(bytes(ctime(),'uft-8'),data))
        tcpCliSock.close()
    tcpSerSock.close()