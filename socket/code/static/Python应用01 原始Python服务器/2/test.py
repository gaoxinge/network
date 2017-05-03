import socket

HOST = ''
PORT = 8000

text_content = '''HTTP/1.x 200 OK
Content-Type: text/html

<head>
<title>WOW</title>
</head>
<body>
<p>Wow, Python Server</p>
<IMG src="test.jpg">
</body>
'''

f = open('test.jpg', 'rb')
pic_content = '''HTTP/1.x 200 OK
Content-Type: image/jpg

'''
pic_content += f.read()
f.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

while True:
    s.listen(3)
    conn, addr = s.accept()
    request = conn.recv(1024)
    method = request.split(' ')[0]
    src = request.split(' ')[1]
    
    if method == 'GET':
        if src == '/test.jpg':
            content = pic_content
        else:
            content = text_content
        print 'request is:', request
        print 'connected by', addr
    
    conn.sendall(content)
    conn.close()


