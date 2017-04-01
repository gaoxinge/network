from wsgiref.simple_server import make_server

def application(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-Type', 'text/plain')]
    start_response(status, response_headers)
    response_body = 'hello world'
    return [response_body]
    
class Upperware(object):
    
    def __init__(self, app):
        self.wrapped_app = app
        
    def __call__(self, environ, start_response):
        for data in self.wrapped_app(environ, start_response):
            yield data.upper()
            
wrapped_app = Upperware(application)
httpd = make_server('localhost', 5000, wrapped_app)
httpd.serve_forever()