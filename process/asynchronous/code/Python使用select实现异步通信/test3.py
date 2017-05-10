import socket

s = socket.socket()
s.connect(('', 8888))
s.send('hello from the client')
s.close()