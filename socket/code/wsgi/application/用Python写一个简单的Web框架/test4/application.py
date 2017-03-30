import re

class my_app(object):
    
    urls = (
        ('/', 'index'),
        ('/hello/(.*)', 'hello'),
    )
    
    def __init__(self, environ, start_response):
        self.environ = environ
        self.start = start_response
        
    def __iter__(self):
        path = self.environ['PATH_INFO']
        method = self.environ['REQUEST_METHOD']
        
        for pattern, name in self.urls:
            m = re.match('^' + pattern + '$', path)
            if m:
                args = m.groups()
                funcname = method.upper() + '_' + name
                if hasattr(self, funcname):
                    func = getattr(self, funcname)
                    return func(*args)
        
        return self.notfound()
        
    def GET_index(self):
        status = '200 OK'
        response_headers = [('Content-type', 'text/plain')]
        self.start(status, response_headers)
        yield 'Welcome!\n'
        
    def GET_hello(self, name):
        status = '200 OK'
        response_headers = [('Content-type', 'text/plain')]
        self.start(status, response_headers)
        yield 'Hello %s!\n' % name
        
    def notfound(self):
        status = '404 NOT Found'
        response_headers = [('Content-type', 'text/plain')]
        self.start(status, response_headers)
        yield 'Not Found\n'