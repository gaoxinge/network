import socket

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))
s.listen(5)

while True:
    c, addr = s.accept()
    print 'connection address: ', addr
    c.send('welcome to runoob!')
    c.close()
