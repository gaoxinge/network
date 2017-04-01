from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple

def MyApp(environ, start_response):
    request = Request(environ)
    response = Response()
    if request.path == '/':
        response.response = ['url true!']
    else:
        response.response = ['url error!']
    return response(environ, start_response)

run_simple('', 5000, MyApp)
