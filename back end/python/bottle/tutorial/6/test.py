from bottle import route, abort, redirect, run

@route('/restricted')
def restricted():
    abort(401, 'Sorry, access denied.')
    
@route('/wrong')
def wrong():
    redirect('right')
    
@route('/right')
def right():
    return 'Hello, world!'

run(host='localhost', port=8000)