import socket

s = socket.socket()
s.connect(('127.0.0.1', 8000))

while True:
    message = raw_input('>>> ')
    s.sendall(message)