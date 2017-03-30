import re

class my_app(object):
    
    urls = (
        ('/', 'index'),
        ('/hello/(.*)', 'hello'),
    )
    
    def __init__(self, environ, start_response):
        self.environ = environ
        self.start = start_response
        self.status = '200 OK'
        self._headers = []
        
    def __iter__(self):
        result = self.delegate()
        self.start(self.status, self._headers)
        
        if isinstance(result, basestring):
            return iter([result])
        else:
            return iter(result)
    
    def delegate(self):
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
        
    def header(self, name, value):
        self._headers.append((name, value))
        
    def GET_index(self):
        self.header('Content-type', 'text/plain')
        return 'Welcome!\n'
        
    def GET_hello(self, name):
        self.header('Content-type', 'text/plain')
        return 'Hello %s!\n' % name
    
    def notfound(self):
        self.status = '404 Not Found'
        self.header('COntent-type', 'text/plain')
        return 'Not Found\n'