import SocketServer

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
</body>'''

f = open('test.jpg', 'rb')
pic_content = '''HTTP/1.x 200 OK
Content-Type: image/jpg

'''
pic_content += f.read()
f.close()

class MyHTTPHandler(SocketServer.BaseRequestHandler):
    
    def handle(self):
        request = self.request.recv(1024)
        
        print 'Connected by', self.client_address[0]
        print 'Request is', request
        
        method = request.split(' ')[0]
        src = request.split(' ')[1]
        
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
            
        self.request.sendall(content)
        
server = SocketServer.TCPServer((HOST, PORT), MyHTTPHandler)
server.serve_forever()
