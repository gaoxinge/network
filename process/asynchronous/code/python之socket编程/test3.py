import socket
import select

sk1 = socket.socket()
sk1.bind(('', 8001))
sk1.listen(1)
inputs = [sk1]
message_dic = {}
outputs = []

while True:
    r_list, w_list, e_list = select.select(inputs, outputs, inputs, 1)

    for sk1_or_conn in r_list:
        if sk1_or_conn == sk1:
            conn, address = sk1_or_conn.accept()
            inputs.append(conn)
            message_dic[conn] = []
        else:
            try:
                data_bytes = sk1_or_conn.recv(1024)
                sk1_or_conn.senadll(data_bytes + 'good')
            except:
                inputs.remove(sk1_or_conn)
                sk1_or_conn.close()
            else:
                message_dic[sk1_or_conn].append(data_bytes)
                outputs.append(sk1_or_conn)
                
    for conn in w_list:
        print 1
        recv_str = message_dic[conn][0]
        del message_dic[conn][0]
        conn.sendall(recv_str + 'good')
        
    for sk in e_list:
        inputs.remove(sk)
        sk.close()