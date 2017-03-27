from werkzeug.serving import run_simple
from werkzeug.wrappers import Request, Response

def application(environ, start_response):
    request = Request(environ)
    html = '<h1>Hello %s!</h1>' % (request.path[1:] or 'World')
    response = Response(html, mimetype='text/html')
    return response(environ, start_response)
    
run_simple('', 8000, application)