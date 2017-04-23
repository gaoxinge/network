from tornado.httpclient import AsyncHTTPClient
from tornado import gen

@gen.coroutine
def fetch_coroutine(url):
    http_client = AsyncHTTPClient()
    response = yield http_client.fetch(url)
    raise gen.Return(response.body)
    
print fetch_coroutine('http://www.baidu.com')