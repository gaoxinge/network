from wsgiref.simple_server import make_server
from application import simple_app
    
if __name__ == '__main__':
    httpd = make_server('', 8086, simple_app)
    sa = httpd.socket.getsockname()
    print 'http://{0}:{1}/'.format(*sa)
    
    httpd.serve_forever()