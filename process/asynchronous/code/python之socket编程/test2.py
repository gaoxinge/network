import socket

obj = socket.socket()
obj.connect(('127.0.0.1', 8001))

while True:
    inp = raw_input('>>> ')
    obj.sendall(inp)
    if inp == 'q':
        break
    ret = obj.recv(1024)
    print ret