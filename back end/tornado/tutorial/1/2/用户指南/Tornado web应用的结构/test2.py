import tornado.web
import tornado.ioloop

class MyFormHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('<html><body><form action="/myform" method="POST">'
                   '<input type="text" name="message">'
                   '<input type="submit" value="Submit">'
                   '</form></body></html>')
                   
    def post(self):
        self.set_header('Content-Type', 'text/plain')
        self.write('You wrote ' + self.get_body_argument('message'))

app = tornado.web.Application([
    ('/', MyFormHandler),
    ('/myform', MyFormHandler),
])        

if __name__ == '__main__':
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()