import socket, select

sk = socket.socket()
sk.bind(('', 8001))
sk.listen(1)

inputs = [sk,]
outputs = []
message_dict = {}

while True:
    r_list, w_list, e_list = select.select(inputs, outputs, inputs, 1)
    print('listen socket is %d' % len(inputs))
    print(r_list)
    
    for sk_or_conn in r_list:
        if sk_or_conn == sk:
            conn, address = sk_or_conn.accept()
            inputs.append(conn)
            message_dict[conn] = []
        else:
            try:
                data_str = sk_or_conn.recv(1024)
            except Exception as ex:
                inputs.remove(sk_or_conn)
            else:
                message_dict[sk_or_conn].append(data_str)
                outputs.append(sk_or_conn)
    
    for conn in w_list:
        recv_str = message_dict[conn][0]
        del message_dict[conn][0]
        conn.sendall(recv_str+'good')
        outputs.remove(conn)
        
    for sk in e_list:
        inputs.remove(sk)