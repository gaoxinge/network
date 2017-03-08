from gevent import monkey; monkey.patch_all()
import gevent
import requests

def f(url):
    print 'GET: %s' % url
    response = requests.get(url)
    print response.url, response.status_code

gevent.joinall([
    gevent.spawn(f, 'https://www.python.org'),
    gevent.spawn(f, 'https://www.yahoo.com'),
    gevent.spawn(f, 'https://github.com'),
])
