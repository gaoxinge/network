import socket, select

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', 8888))
s.listen(5)

inputs = [s]
while True:
    rs, ws, es = select.select(inputs, [], [], 1)
    for r in rs:
        if r is s:
            client_socket, client_address = r.accept()
            inputs.append(client_socket)
        else:
            data = r.recv(1024)
            if not data:
                inputs.remove(r)
            else:
                print data