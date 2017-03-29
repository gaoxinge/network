from webpylike import WebPyApp, View, Response

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