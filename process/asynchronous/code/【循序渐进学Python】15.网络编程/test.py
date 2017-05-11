import socket

s = socket.socket()
s.bind(('', 8888))
s.listen(5)

while True:
    c, addr = s.accept()
    print 'Got connection from', addr
    c.send('Thank you from connection')
    c.close()