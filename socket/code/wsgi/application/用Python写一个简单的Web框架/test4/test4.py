from wsgiref.simple_server import make_server
from application import my_app

if __name__ == '__main__':
    httpd = make_server('', 5000, my_app)
    sa = httpd.socket.getsockname()
    print 'http://{0}:{1}/'.format(*sa)
    
    httpd.serve_forever()