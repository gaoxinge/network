import socket

flag = 1
s = socket.socket()
s.connect(('127.0.0.1', 8888))
while flag:
    input_msg = raw_input('input>>>')
    if input_msg == '0':
        break
    s.sendall(input_msg)
    msg = s.recv(1024)
    print(msg)
s.close()