from gevent import monkey
monkey.patch_socket()

import urllib2

urls = ['http://www.google.com', 'http://www.yandex.ru', 'http://www.python.org']

def print_head(url):
    print('Starting %s' % url)
    data = urllib2.urlopen(url).read()
    print('%s: %s bytes: %r' % (url, len(data), data[:50]))
    
jobs = [gevent.spawn(print_head, url) for url in urls]
gevent.wait(jobs)