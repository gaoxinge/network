import socket, select
import time
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 5000))
s.listen(5)

while 1:
    infds, outfds, errfds = select.select([s], [], [], 5)
    if len(infds) != 0:
        clientsock, clientaddr = s.accept()
        buf = clientsock.recv(8196)
        if len(buf) != 0:
            print buf
            os.popen('sleep 10').read()
        clientsock.close()