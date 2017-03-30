from wsgiref.simple_server import make_server
from application import my_app

urls = (
    ('/', 'index'),
    ('/hello/(.*?)', 'hello'),
)

class index(object):
    def GET(self):
        my_app.header('Content-type', 'text/plain')
        return 'Welcome!\n'
        
class hello(object):
    def GET(self, name):
        my_app.header('Content-type', 'text/plain')
        return 'Hello %s!\n' % name

wsgiapp = my_app(urls, globals())
     
if __name__ == '__main__':
    httpd = make_server('', 5000, wsgiapp)
    sa = httpd.socket.getsockname()
    print 'http://{0}:{1}/'.format(*sa)
    
    httpd.serve_forever()