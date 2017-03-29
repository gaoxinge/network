from webpylike import WebPyApp, View, Response
from werkzeug.serving import run_simple

urls = (
    '/',      'index',
    '/about', 'about'
)

class index(View):
    def GET(self):
        return Response('Hello World')
        
class about(View):
    def GET(self):
        return Response('This is the about page')
        
app = WebPyApp(urls, globals())
run_simple('', 5000, app)
