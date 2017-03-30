import os
from werkzeug.serving import run_simple
from werkzeug.wrappers import Request, Response
from jinja2 import Environment, FileSystemLoader

def render_template(template_name, **context):
    template_path = os.path.join(os.path.dirname(__file__), 'templates')
    jinja_env = Environment(loader=FileSystemLoader(template_path), autoescape=True)
    t = jinja_env.get_template(template_name)
    return Response(t.render(context), mimetype='text/html')
    
def application(environ, start_response):
    response = render_template('index.html')
    return response(environ, start_response)
    
run_simple('', 8000, application)