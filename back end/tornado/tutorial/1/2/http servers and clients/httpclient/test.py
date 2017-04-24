from tornado import httpclient

http_client = httpclient.HTTPClient()
try:
    response = http_client.fetch("http://www.baidu.com")
    print response.body
except httpclient.HTTPError as e:
    print 'Error: ' + str(e)
except e:
    print 'Error: ' + str(e)
http_client.close()