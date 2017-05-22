import socket
import select

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', 8080))
s.listen(1)
s.setblocking(0)
inputs = [s]

response = '''
HTTP/1.1 200 OK

Hello, World!
'''

while True:
    rlist, wlist, xlist = select.select(inputs, [], [])
    for sock in rlist:
        if sock == s:
            con, addr = sock.accept()
            inputs.append(con)
        else:
            data = sock.recv(1024)
            if data:
                sock.send(response)
                inputs.remove(sock)
                sock.close() 