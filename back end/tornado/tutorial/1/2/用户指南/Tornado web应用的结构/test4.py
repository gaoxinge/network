import tornado.ioloop
import tornado.web
import tornado.httpclient

class MainHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        http = tornado.httpclient.AsyncHTTPClient()
        response = yield http.fetch('http://friendfeed-api.com/v2/feed/bret')
        json = tornado.escape.json_decode(response.body)
        self.write('Fetched ' + str(len(json['entires'])) + ' entires '
                   'from the Friend API')
        
app = tornado.web.Application([
    ('/', MainHandler),
])

if __name__ == '__main__':
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()