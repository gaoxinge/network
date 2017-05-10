import socket, select

sk1 = socket.socket()
sk1.bind(('', 8001))
sk1.listen(1)

sk2 = socket.socket()
sk2.bind(('', 8002))
sk2.listen(1)

sk3 = socket.socket()
sk3.bind(('', 8003))
sk3.listen(1)

inputs = [sk1, sk2, sk3]

while True:
    r_list, w_list, e_list = select.select(inputs, [], inputs, 1)
    
    for sk in r_list:
        conn, address = sk.accept()
        conn.sendall('hello')
        conn.close()
        
    for sk in e_list:
        inputs.remove(sk)