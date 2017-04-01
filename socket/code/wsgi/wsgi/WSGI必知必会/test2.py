from werkzeug.wrappers import Response

response = Response(content_type='text/plain')
response.charset = 'utf-8'
response.body = 'hey'
print response.status_code, response.headers, response.response
