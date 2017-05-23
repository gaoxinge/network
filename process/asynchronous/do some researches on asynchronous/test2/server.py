import socket, select

s = socket.socket()
s.bind(('', 8000))
s.listen(1)

inputs = [s]
outputs = []
count = 0


while True:
    r_list, w_list, e_list = select.select(inputs, outputs, inputs)
    
    count += 1
    print count, len(r_list), len(w_list)
    
    for t in r_list:
        if t is s:
            client_connection, client_address = t.accept()
            inputs.append(client_connection)
            outputs.append(client_connection)
        else:
            try:
                data = t.recv(1024)
                print data
            except:
                inputs.remove(t)
                if t in outputs:
                    outputs.remove(t)
                t.close()