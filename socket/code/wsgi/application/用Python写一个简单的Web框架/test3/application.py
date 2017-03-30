class my_app(object):
    
    def __init__(self, environ, start_response):
        self.environ = environ
        self.start = start_response
        
    def __iter__(self):
        path = self.environ['PATH_INFO']
        if path == '/':
            return self.GET_index()
        elif path == '/hello':
            return self.GET_hello()
        return self.notfound()
            
    def GET_index(self):
        status = '200 OK'
        response_headers = [('Content-type', 'text/plain')]
        self.start(status, response_headers)
        yield 'Welcome!\n'
        
    def GET_hello(self):
        status = '200 OK'
        response_headers = [('Content-type', 'text/plain')]
        self.start(status, response_headers)
        yield 'Hello world!\n'
        
    def notfound(self):
        status = '404 Not Found'
        response_headers = [('Content-type', 'text/plain')]
        self.start(status, response_headers)
        yield 'Not Found\n'  