from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Index Page'
    
@app.route('/hello')
def hello():
    return 'Hello World'
    
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username
    
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id
    
@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

if __name__ == '__main__':
    with app.test_request_context():
        print url_for('hello_world')
        print url_for('hello')
        print url_for('show_user_profile', username='John Doe')
        # print url_for('show_user_profile')
        print url_for('show_post', post_id=1)
        # print url_for('show_post', post_id='q')
        print url_for('projects')
        print url_for('about')
    app.run()