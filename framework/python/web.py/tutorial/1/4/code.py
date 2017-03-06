import web

db = web.database(
    dbn  = 'mysql',
    user = 'root',
    pw   = 'xxxxxx',
    db   = 'hello',
)

render = web.template.render('templates/')

urls = (
    '/',    'index',
    '/add', 'add',
)

class index:
    def GET(self):
        todos = db.select('todos')
        return render.index(todos)

class add:
    def POST(self):
        i = web.input()
        n = db.insert('todos', title=i.title)
        web.seeother('/')
        
if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
