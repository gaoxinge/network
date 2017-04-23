from tornado.httpclient import AsynHTTPClient
from tornado import gen

@gen.coroutine
def fetch_coroutine(url):
    http_client = AsynHTTPClient()
    response = yield http_client.fetch(url)
    return response.body
    
print fetch_coroutine('http://www.baidu.com')