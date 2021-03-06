# web.py教程

## 第一个程序

```python
#coding=utf-8
import web

urls = (
    '/(.*)', 'hello', # localhost:8000;localhost:8000/();localhost:8000/(world)
)

class hello:
    def GET(self, name):
        if not name: name = u'世界'
        web.header('Content-Type', 'text/html; charset=utf-8')
        return u'你好，' + name + u'！' 
        
if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
```

## URL处理

### 正则映射

```python
#coding=utf-8
import web

urls = (
    '/hello/(.*)', 'hello', # localhost:8000/hello/();localhost:8000/hello/(world)
    '/magic/.*',   'magic', # localhost:8000/magic/;localhost:8000/magic/world
)

class hello:
    def GET(self, name):
        if not name: name = u'世界'
        web.header('Content-Type', 'text/html; charset=utf-8')
        return u'你好，' + name + u'！'

class magic:
    def GET(self):
        return 'magic'
        
if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
```

### 自动映射

```python
#coding=utf-8
import web

app = web.auto_application()

class hello(app.page):
    def GET(self):
        web.header('Content-Type', 'text/html; charset=utf-8')
        return u'你好，世界！'

class magic(app.page):
    def GET(self):
        return 'magic'

app.run()
```

等价于

```python
#coding=utf-8
import web

urls = (
    '/hello', 'hello', 
    '/magic', 'magic', 
)

class hello:
    def GET(self):
        web.header('Content-Type', 'text/html; charset=utf-8')
        return u'你好，世界！'

class magic:
    def GET(self):
        return 'magic'

app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()
```

## 多个应用程序

```python
import web
import blog

urls = (
    '/blog', blog.app_blog, # localhost:8000/blog
    '/(.*)', 'index',       # localhost:8000;localhost:8000/();localhost:8000/(world)
)

class index:
    def GET(self, path):
        return 'index' + path

app = web.application(urls, locals())

if __name__ == '__main__':
    app.run()
```

```python
import web

urls = (
    '',      'reblog', # localhost:8000/blog
    '/(.*)', 'blog',   # localhost:8000/blog/();localhost:8000/blog/(world)
)

class reblog:
    def GET(self):
        raise web.seeother('/')

class blog:
    def GET(self, path):
        return 'blog' + path
        
app_blog = web.application(urls, locals())
```

### 基于子目录的应用程序

```python
import web
import wiki
import blog
import auth

mapping = (
    '/wiki', wiki.app,
    '/blog', blog.app,
    '/auth', auth.app,
)

# urls = (
    '/wiki', wiki.app,
    '/blog', blog.app,
    '/auth', auth.app,
)

app = web.application(mapping)
# app = web.subdir_application(mapping)
# app = web.application(urls, locals())

if __name__ == '__main__':
    app.run()
```

```python
import web

urls = (
    '', 'wiki',
)

class wiki:
    def GET(self):
        return 'wiki'
        
app = web.application(urls, locals())
```

```python
import web

urls = (
    '', 'blog',
)

class blog:
    def GET(self):
        return 'blog'
        
app = web.application(urls, locals())
```

```python
import web

urls = (
    '', 'auth',
)

class auth:
    def GET(self):
        return 'auth'
        
app = web.application(urls, locals())
```

### 基于子域名的应用程序

```python
import web
import mainsite
import usersite

mapping = (
    '(www\.)?example.com', mainsite.app,
    '.*\.example.com', usersite.app,
)

app = web.subdomain_application(mapping)

if __name__ == '__main__':
    app.run()
```

```python
import web

urls = (
    '', 'main',
)

class main:
    def GET(self):
        return 'main'
        
app = web.application(urls, locals())
```

```python
import web

urls = (
    '', 'user',
)

class user:
    def GET(self):
        return 'user'
        
app = web.application(urls, locals())
```

## 测试

### 文档测试

```python
import web

urls = (
    '/hello', 'hello',
)

app = web.application(urls, globals())

class hello:
    
    """hello world example
    >>> response = app.request('/hello')
    >>> response.data
    'hello, world!'
    >>> response.headers['Content-Type']
    'text/plain'
    """
    
    def GET(self):
        web.header('Content-Type', 'text/plain')
        return 'hello, world!'
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()
```

### 单元测试

```python
import web

urls = (
    '/hello', 'hello',
)

class hello:
    def GET(self):
        web.header('Content-Type', 'text/plain')
        return 'hello, world!'
        
app = web.application(urls, globals())
```

```python
import unittest
from helloworld import app

class HelloWorldTest(unittest.TestCase):
    def testHelloWorld(self):
        response = app.request('/hello')
        self.assertEquals(response.data, 'hello, world!')
        self.assertEquals(response.headers['Content-Type'], 'text/plain')
        self.assertEquals(response.status, '200 OK')
        
if __name__ == '__main__':
    unittest.main()
```

## 会话

### session

```python
import web

urls = (
    '/count', 'count',
    '/reset', 'reset',
)

app = web.application(urls, locals())

# store: used to store sessions, which can be a disk or database
# db = web.database(dbn='postgres', db='mydatabase', user='myname', pw='')
store = web.session.DiskStore('sessions')

# initizlizer: initialize session, which can be a dict or func
session = web.session.Session(app, store, initializer={'count': 0})

class count:
    def GET(self):
        session.count += 1 # error: there is no count in session
        return str(session.count)
        
class reset:
    def GET(self):
        session.kill()
        return ''
        
if __name__ == '__main__':
    app.run()
```

### cookies

- 设置

```
name    (string): The actual name of the cookie, as stored by the browser, and returned to the server.
value   (string): The value you want stored under that name.
expires (int):    Optionally, is the time in seconds until the browser should expire the cookie.
domain  (string): The domain the cookie is valid for. By default, set to the host accessed, this allows you to set the domain, rather than just a host (such as .webpy.org).
secure  (bool):   If True, require that the cookie only be sent over HTTPS.
web.setcookie(name, value, expires='', domain=None, secure=False)
```

```python
import web

urls = (
    '/cookieset', 'CookieSet',
)

app = web.application(urls, locals())

class CookieSet:
    def GET(self):
        i = web.input(age='25')
        web.setcookie('age', i.age, 3600)
        return 'Age set in your cookie'
        
if __name__ == '__main__':
    app.run()
```

- 读取

```
1
cookie不存在时抛出异常
cookieName is the name of the cookie submitted by the browser
web.cookies().get(cookieName)
```

```python
import web

urls = (
    '/cookieset', 'CookieSet',
    '/cookieget', 'CookieGet',
)

app = web.application(urls, locals())

class CookieSet:
    def GET(self):
        i = web.input(age='25')
        web.setcookie('age', i.age, 3600)
        return 'Age set in your cookie'

class CookieGet:
    def GET(self):
        try:
            return 'Your age is: ' + web.cookies().get('age')
        except:
            return 'Your age is: 36'
        
if __name__ == '__main__':
    app.run()
```

```
2
有预设值，避免异常
cookieName is the name of the cookie submitted by the browser
web.cookies(cookieName=defaultValue)
```

```python
import web

urls = (
    '/cookieset', 'CookieSet',
    '/cookieget', 'CookieGet',
)

app = web.application(urls, locals())

class CookieSet:
    def GET(self):
        i = web.input(age='25')
        web.setcookie('age', i.age, 3600)
        return 'Age set in your cookie'

class CookieGet:
    def GET(self):
        c = web.cookies(age='36')
        return 'Your age is: ' + c.age
        
if __name__ == '__main__':
    app.run()
```

## 发邮件

```python
import web

web.config.smtp_server   = 'smtp.xxx.com'
web.config.smtp_port     = '25'
web.config.smtp_username = 'xxxxxx@xxx.com'
web.config.smtp_password = 'xxxxxx'
web.config.smtp_starttls = True
web.sendmail('xxxxxx@xxx.com', 'xxxxxx@xxx.com', 'subject', 'message')
'''
web.sendmail(
    'xxxxxx@xxx.com', ['xxxxxx@xxx.com', 'xxxxxx@xxx.com'],
    'subjcet', 'message', cc='xxxxxx@xxx.com', bcc='xxxxxx@xxx.com',
    headers=({'User-Agent': 'webpy.sendmail', 'X-Mailer': 'webpy.sendmail',}),
)
'''
```

## 获取客户端信息

```python
import web

urls = (
    '/', 'example',
)

app = web.application(urls, globals())

class example:
    def GET(self):
        refer = web.ctx.env.get('HTTP_REFERER', 'https://www.baidu.com')
        useragent = web.ctx.env.get('HTTP_USER_AGENT')
        print useragent
        raise web.seeother(refer)
        
if __name__ == '__main__':
    app.run()
```

## 模板

```python
import web

urls = (
    '/(.*)', 'hello',
)

app = web.application(urls, globals())
render = web.template.render('templates/')

class hello:
    def GET(self, name):
        return render.hello(name)
        
if __name__ == '__main__':
    app.run()
```

```html
$def with (name, todos={})

$if name:
    <h1>你好，$name！</h1>
$else:
    <h1>你好，世界！</h1>

$# 表达式	
$for var in [1,2,3]: 
	I like $var!
```

## 用户输入

### 表单

```python
import web

urls = (
    '/', 'SomePage',
)

app = web.application(urls, globals())

class SomePage:
    def GET(self):
        user_data = web.input(id=[])
        return '<h1>' + ','.join(user_data.id) + '</h1>'
        
if __name__ == '__main__':
    app.run()
```

### 文件上传

```python
import web

urls = (
    '/upload', 'Upload',
)

app = web.application(urls, globals())

class Upload:
    def GET(self):
        return """<html><head></head><body>
        <form method="POST" enctype="multipart/form-data" action="">
        <input type="file" name="myfile" />
        <br/>
        <input type="submit" />
        </form>
        </body></html>"""
    
    def POST(self):
        x = web.input(myfile={})
        return "filename: %s\nvalue:\n%s" % (x['myfile'].filename, x['myfile'].value)
        
if __name__ == '__main__':
    app.run()
```

## 数据库

```python
import web

db = web.database(
    dbn  = 'mysql',
    user = 'root',
    pw   = 'xxxxxx',
    db   = 'hello',
)

urls = (
    '/', 'index',
)

app = web.application(urls, globals())

class index:
    def GET(self):
        todos = db.select('todos')
        todos = db.select('todos', where='id=$id', vars={'id': 2})
        todos = db.query('SELECT * FROM todos')
        return ''
        
if __name__ == '__main__':
    app.run()
```