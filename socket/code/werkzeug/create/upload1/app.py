import os
from werkzeug.serving import run_simple
from werkzeug.wrappers import Request, Response
from werkzeug.wsgi import wrap_file
from jinja2 import Environment, FileSystemLoader

# reconstruct render_template
def render_template(template_name, **context):
    template_path = os.path.join(os.getcwd(), 'templates')
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
    
def remove_file(filename):
    path = os.path.join(static_path, filename)
    return os.remove(path)
    
# web application
def application(environ, start_response):
    
    request = Request(environ)
    path = request.path
    method = request.method
    
    """
    url:    /
    method: GET
    """
    if not path[1:] and request.method == 'GET':
        response = render_template('index.html')
        return response(environ, start_response)
        
    """
    url:    / 
    method: POST
    """
    if not path[1:] and request.method == 'POST':
        f = request.files['uploaded_file']
        if f.filename:
            save_file(f)
        response = render_template('index.html')
        return response(environ, start_response)
        
    """
    url:    /manager
    """
    if path[1:] == 'manager':
        urls = list_file()
        response = render_template('manager.html', urls=urls)
        return response(environ, start_response)
    
    """
    url:    /delete
    """
    if path[1:7] == 'delete':
        remove_file(path[8:])
        urls = list_file()
        response = render_template('manager.html', urls=urls)
        return response(environ, start_response)
        
    """
    url:    /view
    """
    if path[1:5] == 'view':
        response = render_template('view.html')
        return response(environ, start_response)
        
    """
    url:    404
    """
    response = render_template('error.html', path=path)
    return response(environ, start_response)
    
run_simple('', 8000, application)