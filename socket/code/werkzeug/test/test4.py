from werkzeug.serving import run_simple
from werkzeug.wrappers import Response

def application(environ, start_response):
    response = Response('<h1>Hello World!</h1>', mimetype='text/html')
    return response(environ, start_response)
    
run_simple('', 8000, application)