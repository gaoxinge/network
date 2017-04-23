import tornado.ioloop
import tornado.web
import tornado.httpclient

class MainHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        http = tornado.httpclient.AsyncHTTPClient()
        http.fetch('http://friendfeed-api/v2/feed/bret',
                   callback=self.on_response)
                   
    def on_response(self, response):
        if response.error:
            raise tornado.web.HTTPError(500)
        json = tornado.escape.json_decode(response.body)
        self.write('Fetched ' + str(len(json['entries'])) + ' entries '
                   'from the FriendFeed API')
        self.finish()
        
app = tornado.web.Application([
    ('/', MainHandler),
])

if __name__ == '__main__':
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()