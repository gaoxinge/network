import socket

obj = socket.socket()
obj.connect(('127.0.0.1', 8001))

while True:
    inp = raw_input('>>> ')
    obj.send(inp)
    ret = obj.recv(1024)
    print ret
    
obj.close()