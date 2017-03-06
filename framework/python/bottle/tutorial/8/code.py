from bottle import route, get, post, request, response, template, run

@get('/login')
def login():
    return '''
    <form action="/login" method="post">
        Username: <input name="username" type="text" />
        Password: <input name="password" type="password" />
        <input value="Login" type="submit" />
    </form>
    '''
    
@post('/login')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if username == 'xxx' and password == 'xxx':
        response.set_cookie('account', username, secret='xxx')
        return template('<p>Welcome {{name}}! You are now logged in.</p>', name=username)
    else:
        return '<p>Login failed</p>'

@route('/restricted')
def restricted():
    username = request.get_cookie('account', secret='xxx')
    if username:
        return template('<p>Hello {{name}}! Welcome back.</p>', name=username)
    else:
        return '<p>You are not logged in. Access denied.</p>'
        
run(host='localhost', port=8000)