from eventlet import listen, wsgi

def myapp(environ,start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return ['Hello world!']

wsgi.server(listen(('', 8000)), myapp)