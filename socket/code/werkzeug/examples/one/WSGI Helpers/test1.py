from werkzeug.wrappers import Response
from werkzeug.wsgi import responder
from werkzeug.serving import run_simple

@responder
def application(environ, start_response):
    return Response('Hello World!')
    
run_simple('', 5000, application)