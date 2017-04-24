from tornado import httpclient

def handle_request(response):
    if response.error:
        print 'Error', response.error
    else:
        print response.body
        
http_client = httpclient.AsyncHTTPClient()
http_client.fetch('http://www.baidu.com', handle_request)