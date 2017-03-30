from bottle import get, post, request, run

@get('/login') # @route('/login')
def login():
    return '''
    <form action="/login" method="post">
        Username: <input name="username" type="text" />
        Password: <input name="password" type="password" />
        <input value="Login" type="submit" />
    </form>
    '''
    
@post('/login') # @route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    return 'username: %s, password: %s' % (username, password)

run(host='localhost', port=8000)