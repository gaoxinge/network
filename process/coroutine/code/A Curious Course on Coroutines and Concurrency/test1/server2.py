# -*- coding: utf-8 -*-
import socket
from test import *

class Socket(object):
    
    def __init__(self, sock):
        self.sock = sock
        
    def accept(self):
        yield ReadWait(self.sock)
        client, addr = self.sock.accept()
        yield Socket(client), addr
        
    def send(self, buffer):
        while buffer:
            yield WriteWait(self.sock)
            len = self.sock.send(buffer)
            buffer = buffer[len:]
            
    def recv(self, maxbytes):
        yield ReadWait(self.sock)
        yield self.sock.recv(maxbytes)
        
    def close(self):
        yield self.sock.close()
        
        
def server(port):
    print "Server starting"
    rawsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    rawsock.bind(("", port))
    rawsock.listen(5)
    sock = Socket(rawsock)
    while True:
        client, addr = yield sock.accept()
        yield NewTask(handle_client(client, addr))
        
def handle_client(client, addr):
    print "Connection from", addr
    while True:
        data = yield client.recv(65526)
        if not data:
            break
        yield client.send(data)
    print "Client closed"
    yield client.close()
    
sched = Scheduler()
sched.new(server(45000))
sched.mainloop()