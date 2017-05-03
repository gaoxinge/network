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
<img src="test.jpg">
<form name="input" action="/" method="post">
First name: <input type="text" name="firstname"><br>
<input type="submit" value="submit">
</form>
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
    
    print 'connect by', addr
    print 'request is:', request
    
    if method == 'GET':
        if src == '/test.jpg':
            content = pic_content
        else:
            content = text_content
    
    if method == 'POST':
        form = request.split('\r\n')
        idx = form.index('')
        entry = form[idx:]
        value = entry[-1].split('=')[-1]
        content = text_content + '\n <p>' + value + '</p>'
        
    conn.sendall(content)
    conn.close()
        
    