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
            
class Upperware1(object):
    
    def __init__(self, app):
        self.wrapped_app = app
        
    def __call__(self, environ, start_response):
        return [self.wrapped_app(environ, start_response)[0].upper()]
        
def Upperware2(f):
    
    def wrapper(environ, start_response):
        for data in f(environ, start_response):
            yield data.upper()
            
    return wrapper

def Upperware3(f):
    
    def wrapper(environ, start_response):
        return [f(environ, start_response)[0].upper()]
    
    return wrapper

wrapped_app = Upperware3(application)
httpd = make_server('localhost', 5000, wrapped_app)
httpd.serve_forever()