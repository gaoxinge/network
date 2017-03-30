from wsgiref.simple_server import make_server

def app(environ, start_response):
    """ok"""
    start_response('200 OK', [('Content-type', 'text/plain')])
    return 'Hello world!\n' 

def app1(environ, start_response):
    """ok"""
    start_response('200 OK', [('Content-type', 'text/plain')])
    return ['Hello world!\n']
    
def app2(environ, start_response):
    """ok"""
    start_response('200 OK', [('Content-type', 'text/plain')])
    yield 'Hello world!\n'
    
def app3(environ, start_response):
    """error"""
    start_response('200 OK', [('Content-type', 'text/plain')])
    yield ['Hello world!\n']
    
def app4(environ, start_response):
    """ok"""
    start_response('200 OK', [('Content-type', 'text/plain')])
    return iter('Hello world!\n')
    
def app5(environ, start_response):
    """ok"""
    start_response('200 OK', [('Content-type', 'text/plain')])
    return iter(['Hello world!\n'])

class ap(object):
    
    """error"""
    
    def __init__(self, environ, start_response):
        self.environ = environ
        self.start_response = start_response
        
    def __iter__(self):
        self.start_response('200 Ok', [('Content-type', 'text/plain')])
        return 'Hello world!\n'

class ap1(object):

    """error"""
    
    def __init__(self, environ, start_response):
        self.environ = environ
        self.start_response = start_response
        
    def __iter__(self):
        self.start_response('200 Ok', [('Content-type', 'text/plain')])
        return ['Hello world!\n']
        
class ap2(object):
    
    """ok"""
    
    def __init__(self, environ, start_response):
        self.environ = environ
        self.start_response = start_response
        
    def __iter__(self):
        self.start_response('200 Ok', [('Content-type', 'text/plain')])
        yield 'Hello world!\n'
        
class ap3(object):
    
    """error"""
    
    def __init__(self, environ, start_response):
        self.environ = environ
        self.start_response = start_response
        
    def __iter__(self):
        self.start_response('200 Ok', [('Content-type', 'text/plain')])
        yield ['Hello world!\n']

class ap4(object):
    
    """ok"""
    
    def __init__(self, environ, start_response):
        self.environ = environ
        self.start_response = start_response
        
    def __iter__(self):
        self.start_response('200 Ok', [('Content-type', 'text/plain')])
        return iter('Hello world!\n')        

class ap5(object):
    
    """ok"""
    
    def __init__(self, environ, start_response):
        self.environ = environ
        self.start_response = start_response
        
    def __iter__(self):
        self.start_response('200 Ok', [('Content-type', 'text/plain')])
        return iter(['Hello world!\n'])
        
class A(object):
    
    def __call__(self, environ, start_response):
        start_response('200 OK', [('Content-type', 'text/plain')])
        return 'Hello World!\n'
        
a = A()   # ok

class A1(object):
    
    def __call__(self, environ, start_response):
        start_response('200 OK', [('Content-type', 'text/plain')])
        return ['Hello World!\n']
        
a1 = A1() # ok

class A2(object):
    
    def __call__(self, environ, start_response):
        start_response('200 OK', [('Content-type', 'text/plain')])
        yield 'Hello World!\n'
        
a2 = A2() # ok

class A3(object):
    
    def __call__(self, environ, start_response):
        start_response('200 OK', [('Content-type', 'text/plain')])
        yield ['Hello World!\n']
        
a3 = A3() # error

class A4(object):
    
    def __call__(self, environ, start_response):
        start_response('200 OK', [('Content-type', 'text/plain')])
        return iter('Hello World!\n')
        
a4 = A4() # ok

class A5(object):
    
    def __call__(self, environ, start_response):
        start_response('200 OK', [('Content-type', 'text/plain')])
        return iter(['Hello World!\n'])
        
a5 = A5() # ok

if __name__ == '__main__':
    httpd = make_server('', 5000, a5)
    httpd.serve_forever()