from werkzeug.wrappers import Request, Response
from werkzeug.wsgi import responder
from werkzeug.routing import Map, Rule
from werkzeug.serving import run_simple

def on_index(request):
    return Response('Hello from the index')
    
url_map = Map([Rule('/', endpoint='index')])
views = {'index': on_index}

@responder
def application(environ, start_response):
    request = Request(environ)
    urls = url_map.bind_to_environ(environ)
    return urls.dispatch(lambda e, v: views[e](request, **v),
                         catch_http_exceptions=True)
                         
run_simple('', 5000, application)