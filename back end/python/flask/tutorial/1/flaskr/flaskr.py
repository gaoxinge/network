import os
from flask import Flask, request, session, redirect, url_for, abort, render_template, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'xxx'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:xxx@localhost/flaskr'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)

class entries(db.Model):

    id    = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40))
    text  = db.Column(db.String(100))
    
    def __init__(self, title, text):
        self.title = title
        self.text = text
    
    def __repr__(self):
        return '<User %r>' % self.username

db.create_all()

@app.route('/')
def show_entries():
    results = entries.query.all()
    return render_template('show_entries.html', entries=results)
    
@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    entry = entries(request.form['title'], request.form['text'])
    db.session.add(entry)
    db.session.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'xxx':
            error = 'Invalid username'
        elif request.form['password'] != 'xxx':
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)
     
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))
    
if __name__ == '__main__':
    app.run()