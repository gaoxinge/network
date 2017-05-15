from eventlet import listen, spawn

def httpd(writer, reader):
    req = ''
    while True:
        chunk = reader.readline()
        if not chunk:
            break
        req += chunk
        if chunk == '\r\n':
            break
    data = 'Hello world!\r\n'
    writer.write('HTTP/1.1 200 OK\r\nContent-Length: %d\r\n\r\n%s' % (len(data), data))
    writer.close()
    reader.close()
    return

def main():
    try:
        server = listen(('', 8000))
        print 'Server started!'
        while True:
            conn, addr = server.accept()
            writer = conn.makefile('w')
            reader = conn.makefile('r')
            spawn(httpd, writer, reader)
    except KeyboardInterrupt:
        pass
    return

if __name__=='__main__':
    main()