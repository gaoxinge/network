import os
from werkzeug.serving import run_simple
from werkzeug.wrappers import Request, Response
from werkzeug.wsgi import responder
from werkzeug.routing import Map, Rule
from jinja2 import Environment, FileSystemLoader

def render_template(template_name, **context):
    template_path = os.path.join(os.path.dirname(__file__), 'templates')
    jinja_env = Environment(loader=FileSystemLoader(template_path), autoescape=True)
    t = jinja_env.get_template(template_name)
    return Response(t.render(context), mimetype='text/html')
    
def index(request):
    return render_template('index.html')
    
def index1(request):
    return render_template('index1.html')
    
def index2(request):
    return render_template('index2.html')
    
url_map = Map([
    Rule('/', endpoint='index'),
    Rule('/1', endpoint='index1'),
    Rule('/2', endpoint='index2'),
])
views = {
    'index': index,
    'index1': index1,
    'index2': index2,
}
    
@responder
def application(environ, start_response):
    request = Request(environ)
    urls = url_map.bind_to_environ(request.environ)
    return urls.dispatch(lambda e, v: views[e](request, **v),
                         catch_http_exceptions=True)
                         
run_simple('', 5000, application)