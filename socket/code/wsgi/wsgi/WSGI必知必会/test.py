from wsgiref.simple_server import make_server
from werkzeug.wrappers import Request, Response

class AppTestManual(object):
    
    def __call__(self, environ, start_response):
        request = Request(environ)
        return self.test(environ, start_response)
        
    def test(self, environ, start_response):
        response = Response()
        response.status_code = 200
        response.response = ['spch']
        return response(environ, start_response)
        
application = AppTestManual()

httpd = make_server('localhost', 5000, application)
httpd.serve_forever()