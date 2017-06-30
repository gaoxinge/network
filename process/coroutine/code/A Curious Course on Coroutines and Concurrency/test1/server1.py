# -*- coding: utf-8 -*-
import socket
from test import *

def Accept(sock):
    yield ReadWait(sock)
    yield sock.accept()
    
def Send(sock, buffer):
    while buffer:
        yield WriteWait(sock)
        len = sock.send(buffer)
        buffer = buffer[len:]

def Recv(sock, maxbytes):
    yield ReadWait(sock)
    yield sock.recv(maxbytes)
    
def server(port):
    print "Server starting"
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("", port))
    sock.listen(5)
    while True:
        client, addr = yield Accept(sock)
        yield NewTask(handle_client(client, addr))

def handle_client(client, addr):
    print "Connection from", addr
    while True:
        data = yield Recv(client, 65536)
        if not data:
            break
        yield Send(client, data)
    client.close()
    print "Client closed"
    yield
    
sched = Scheduler()
sched.new(server(45000))
sched.mainloop()