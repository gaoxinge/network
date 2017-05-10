import socket

obj = socket.socket()
obj.connect(('127.0.0.1', 8001))
content = obj.recv(1024)
print(content)
obj.close()

obj = socket.socket()
obj.connect(('127.0.0.1', 8002))
content = obj.recv(1024)
print(content)
obj.close()