import socket

s = socket.socket()
s.connect(('127.0.0.1', 8000))
message = s.recv(1024)
print message