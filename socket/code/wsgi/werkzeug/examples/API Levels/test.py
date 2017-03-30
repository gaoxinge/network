from werkzeug.utils import escape
from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple

@Request.application
def hello_world(request):
    result = ['<title>Greeter</title>']
    if request.method == 'POST':
        result.append('<h1>Hello %s!</h1>' % escape(request.form['name']))
    result.append('''
        <form action="" method="post">
            Name:
            <input type="text" name="name" size="20">
            <input type="submit" value="Greet me">
        </form>
    ''')
    return Response(''.join(result), mimetype='text/html')
    
run_simple('', 5000, hello_world)