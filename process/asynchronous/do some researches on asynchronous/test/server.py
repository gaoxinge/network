import socket

s = socket.socket()
s.bind(('', 8000))
s.listen(1)

client_connection, client_address = s.accept()
client_connection.sendall('hello world')
client_connection.close()
s.close()