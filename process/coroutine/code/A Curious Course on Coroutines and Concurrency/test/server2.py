# -*- coding: utf-8 -*-
import socket
from test import *

def server(port):
    print "Server starting"
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("", port))
    sock.listen(5)
    while True:
        yield ReadWait(sock)
        client, addr = sock.accept()
        yield NewTask(handle_client(client, addr))

def handle_client(client, addr):
    print "Connection from", addr
    while True:
        yield ReadWait(client)
        data = client.recv(65536)
        if not data:
            break
        yield WriteWait(client)
        client.send(data)
    client.close()
    print "Client closed"
    yield
    
def alive():
    while True:
        print "I'm alive"
        yield
        
sched = Scheduler()
sched.new(alive())
sched.new(server(45000))
sched.mainloop()