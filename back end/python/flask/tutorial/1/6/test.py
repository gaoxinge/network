from flask import Flask, render_template, abort, redirect, url_for, make_response
app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))
    
@app.route('/login')
def login():
    abort(401)
    
@app.errorhandler(404)
def page_not_found(error):
    resp = make_response(render_template('page_not_found.html'), 404)
    resp.headers['X-Something'] = 'A value'
    return resp
    
if __name__ == '__main__':
    app.run()