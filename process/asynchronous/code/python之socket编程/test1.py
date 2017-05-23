import socket
import select

sk1 = socket.socket()
sk1.bind(('', 8001))
sk1.listen(1)

inpu = [sk1]

while True:
    r_list, w_list, e_list = select.select(inpu, [], [], 1)
    for sk in r_list:
        if sk == sk1:
            conn, address = sk.accept()
            inpu.append(conn)
        else:
            try:
                ret = sk.recv(1024)
                sk.sendall(ret + 'hao')
            except:
                inpu.remove(sk)
                sk.close()