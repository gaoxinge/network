from werkzeug.formparser import parse_form_data
from werkzeug.utils import escape
from werkzeug.serving import run_simple

def hello_world(environ, start_response):
    result = ['<title>Greeter</title>']
    if environ['REQUEST_METHOD'] == 'POST':
        form = parse_form_data(environ)[1]
        result.append('<h1>Hello %s!</h1>' % escape(form['name']))
    result.append('''
        <form action="" method="post">
            Name: 
            <input type="text" name="name" size="20">
            <input type="submit" value="Greet me">
        </form>
    ''')
    start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
    return ''.join(result)
    
run_simple('', 5000, hello_world)