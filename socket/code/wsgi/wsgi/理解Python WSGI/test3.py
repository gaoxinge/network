from wsgiref.simple_server import make_server

def application(environ, start_response):
    response_body = [
        '%s: %s' % (key, value) for key, value in sorted(environ.items())
    ]
    response_body = '\n'.join(response_body)
    response_body = [
        'The Begginging\n',
        '*' * 30 + '\n',
        response_body,
        '\n' + '*' * 30,
        '\nThe End'
    ]
    
    status = '200 OK'
    response_headers = [('Content-Type', 'text/plain')]
    
    start_response(status, response_headers)
    return response_body
    
httpd = make_server('', 5000, application)
httpd.handle_request()