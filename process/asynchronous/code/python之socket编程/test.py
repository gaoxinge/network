import socket
import select

sk1 = socket.socket()
sk1.bind(('', 8001))
sk1.listen()

sk2 = socket.socket()
sk2.bind(('', 8002))
sk2.listen()

sk3 = socket.socket()
sk3.bind(('', 8003))
sk3.listen()

li = [sk1, sk2, sk3]

while True:
    r_list, w_list, e_list = select.select(li, [], [], 1)
    for line in r_list:
        conn, addr = line.accept()
        conn.sendall('hello world')