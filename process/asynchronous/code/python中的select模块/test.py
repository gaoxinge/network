import socket
import select

s = socket.socket()
s.bind(('', 8888))
s.listen(5)
r_list = [s]
num = 0

while True:
    rl, wl, error = select.select(r_list, [], [], 10)
    num += 1
    print('counts is %s' % num)
    print('rl\'s length is %s' % len(rl))
    for fd in rl:
        if fd == s:
            conn, addr = fd.accept()
            r_list.append(conn)
            msg = conn.recv(200)
            conn.sendall('first----%s' % conn.fileno())
        else:
            try:
                msg = fd.recv(200)
                fd.sendall('second'.encode())
            except:
                fd.close()
                r_list.remove(fd)               