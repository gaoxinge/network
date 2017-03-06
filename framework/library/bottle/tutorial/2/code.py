from bottle import route, template, run

@route('/')             # localhost:8000;localhost:8000/
@route('/hello/<name>') # localhost:8000/hello/world
def greeting(name='Stranger'):
    return template('Hello {{name}}, how are you?', name = name)
    
run(host='localhost', port=8000, debug=True)