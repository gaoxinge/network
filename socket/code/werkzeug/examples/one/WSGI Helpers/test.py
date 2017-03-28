from werkzeug.wrappers import Response
from werkzeug.serving import run_simple

def application(environ, start_response):
    response = Response('Hello World!')
    return response(environ, start_response)
    
run_simple('', 5000, application)