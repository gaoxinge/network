from wsgiref.simple_server import make_server
from werkzeug.wrappers import Request, Response

def application(environ, start_response):
    request = Request(environ)
    html = '<h1>Hello %s!</h1>' % (request.path[1:] or 'World')
    response = Response(html, mimetype='text/html')
    return response(environ, start_response)
    
httpd = make_server('', 8000, application)
print 'Serving HTTP on port 8000...'
httpd.serve_forever()