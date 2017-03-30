import os
from werkzeug.serving import run_simple
from werkzeug.wrappers import Request, Response
from werkzeug.wsgi import responder
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import HTTPException
from jinja2 import Environment, FileSystemLoader

def render_template(template_name, **context):
    template_path = os.path.join(os.path.dirname(__file__), 'templates')
    jinja_env = Environment(loader=FileSystemLoader(template_path), autoescape=True)
    t = jinja_env.get_template(template_name)
    return Response(t.render(context), mimetype='text/html')

rules = Map([])
views = {}

def get(url):
    def wrapper(view_func):
        rule = Rule(url, endpoint=view_func.__name__)
        rules.add(rule)
        views[view_func.__name__] = view_func
        return view_func
    return wrapper

@get('/')
def index(request):
    return render_template('index.html')

@get('/index1')
def index1(request):
    return render_template('index1.html')

@get('/index2')
def index2(request):
    return render_template('index2.html')

@responder
def application(environ, start_response):
    request = Request(environ)
    adapter = rules.bind_to_environ(request.environ)
    try:
        endpoint, values = adapter.match()
        view_func = views[endpoint]
        return view_func(request, **values)
    except HTTPException, e:
        return e

run_simple('', 5000, application)