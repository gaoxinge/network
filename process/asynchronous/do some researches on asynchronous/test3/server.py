import socket, select

s = socket.socket()
s.bind(('', 8000))
s.listen(1)

inputs = [s]
outputs = []
message_dict = {}

while True:
    r_list, w_list, e_list = select.select(inputs, outputs, inputs)
    
    for t in r_list:
        if t is s:
            client_connection, client_address = t.accept()
            inputs.append(client_connection)
            outputs.append(client_connection)
            message_dict[client_connection] = []
        else:
            try:
                data = t.recv(1024)
                message_dict[t].append(data)
            except:
                inputs.remove(t)
                if t in outputs:
                    outputs.remove(t)
                    del message_dict[t]
                t.close()
                
    for t in w_list:
        data = message_dict[t][0]
        del message_dict[t][0]
        conn.sendall('hello' + data)
        
    for t in e_list:
        inputs.remove(t)
        if t in outputs:
            outputs.remove(t)
            del message_dict[t]
        t.close()