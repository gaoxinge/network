from wsgiref.simple_server import make_server
from werkzeug.wrappers import Response

def application(environ, start_response):
    response = Response('<h1>Hello World!</h1>', mimetype='text/html')
    return response(environ, start_response)
    
httpd = make_server('', 8000, application)
print 'Serving HTTP on port 8000...'
httpd.serve_forever()