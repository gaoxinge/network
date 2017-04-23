import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('<a href="%s">link to story 1</a>' %
                   self.reverse_url('story', '1'))

class StoryHandler(tornado.web.RequestHandler):
    def initialize(self, db):
        self.db = db
        
    def get(self, story_id):
        self.write('this is story %s' % story_id)
      
app = tornado.web.Application([
    tornado.web.url('/', MainHandler),
    tornado.web.url('/story/([0-9]+)', StoryHandler, dict(db=db), name='story')
])
    
if __name__ == '__main__':
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()