from flask import Flask, request, render_template
app = Flask(__name__)

with app.test_request_context('/hello', method='POST'):
    assert request.path == '/hello'
    assert request.method == 'POST'

'''
with app.request_context(environ): # error: environ
    assert request.method == 'POST'
'''

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == 'xxx' and request.form['password'] == 'xxx':
            return 'Hello %s' % request.form['username']
        else:
            return 'Login failed!'
    return render_template('login.html')
    
if __name__ == '__main__':
    app.run()