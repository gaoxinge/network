import socket, select

s = socket.socket()
s.bind(('', 8888))
s.listen(5)

p = select.poll()
p.register(s.fileno(), select.POLLIN|select.POLLERR|select.POLLHUP)
while True:
    events = p.poll(5000)
    if events:
        if events[0][1] == select.POLLIN:
            sock, addr = s.accept()
            buf = sock.recv(8196)
            if buf:
                print buf
                sock.close()
    print 'no data'