from bottle import route, run

@route('/hello')
def hello():
    return 'Hello World!'
    
run(host='localhost', port=8000, debug=True)

'''
from bottle import Bottle, run

app = Bottle()

@app.route('/hello')
def hello():
    return "Hello World!"

run(app, host='localhost', port=8000)
'''