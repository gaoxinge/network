import os
from werkzeug.serving import run_simple
from werkzeug.wrappers import Request, Response
from werkzeug.wsgi import responder
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import HTTPException

def render_template(template_name, **context):
    from jinja2 import Environment, FileSystemLoader
    template_path = os.path.join(os.path.dirname(__file__), 'templates')
    jinja_env = Environment(loader=FileSystemLoader(template_path), autoescape=True)
    content = jinja_env.get_template(template_name).render(context)
    return Response(content, mimetype='text/html')

def static(request, file_name):
    content = ''
    content_type = ''
    file_path = os.path.join(os.path.dirname(__file__), 'static', file_name)
    file_suffix = os.path.splitext(file_name)[1]
    with open(file_path, 'rb') as f:
        content = f.read()
    if file_suffix == '.css':
        content_type = 'text/css'
    elif file_suffix == '.jpg':
        content_type = 'image/jpeg'
    return Response(content, mimetype=content_type)
    
rules = Map([
    Rule('/static/<file_name>', endpoint='static'),
])
views = {
    'static': static,
}

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