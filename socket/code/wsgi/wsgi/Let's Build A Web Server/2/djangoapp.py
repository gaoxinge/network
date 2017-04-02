import sys
sys.path.insert(0, './helloworld')
from helloworld import wsgi
from webserver2 import WSGIServer

app = wsgi.application
httpd = WSGIServer('127.0.0.1', 5000, app)
httpd.serve_forever()