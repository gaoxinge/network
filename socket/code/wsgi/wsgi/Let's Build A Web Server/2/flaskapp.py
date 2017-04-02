from flask import Flask
from flask import Response
from webserver2 import WSGIServer

app = Flask(__name__)

@app.route('/hello')
def hello_world():
	return Response('Hello world from Flask!\n', mimetype = 'text/plain')

httpd = WSGIServer('', 5000, app)
httpd.serve_forever()