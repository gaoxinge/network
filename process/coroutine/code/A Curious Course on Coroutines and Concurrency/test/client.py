import socket

s = socket.socket()
s.connect(('127.0.0.1', 45000))

while True:
    message = raw_input('>>> ')
    s.sendall(message)
    message = s.recv(1024)
    print message