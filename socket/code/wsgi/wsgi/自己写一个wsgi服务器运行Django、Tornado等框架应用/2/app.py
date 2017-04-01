from server import WSGIServer

def application(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-Type', 'text/plain')]
    start_response(status, response_headers)
    return ['Hello world']
    
if __name__ == '__main__':
    httpd = WSGIServer('', 8888, application)
    httpd.serve_forever()