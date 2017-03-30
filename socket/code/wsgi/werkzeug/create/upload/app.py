import os
from werkzeug.serving import run_simple
from werkzeug.wrappers import Request, Response
from werkzeug.wsgi import wrap_file
from jinja2 import Environment, FileSystemLoader

# reconstruct render_template
def render_template(template_name, **context):
    template_path = os.path.join(os.path.dirname(__file__), 'templates')
    jinja_env = Environment(loader=FileSystemLoader(template_path), autoescape=True)
    t = jinja_env.get_template(template_name)
    return Response(t.render(context), mimetype='text/html')

# manipulate the file
static_path = os.path.join(os.getcwd(), 'static')

def save_file(f):
    path = os.path.join(static_path, f.filename)
    with open(path, 'wb') as tmp:
        tmp.write(f.read())
        
def list_file():
    return os.listdir(static_path)
    
# web application
def application(environ, start_response):
    request = Request(environ)
    if request.method == 'POST':
        f = request.files['uploaded_file']
        if f.filename:
            save_file(f)
    urls = list_file()
    response = render_template('index.html', urls=urls)
    return response(environ, start_response)
    
run_simple('', 8000, application)