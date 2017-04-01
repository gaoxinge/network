from wsgiref.simple_server import make_server
from werkzeug.wrappers import Request, Response

@Request.application
def AppTestByAuto(request):
    response = Response()
    response.status_code = 200
    response.response = ['spch']
    return response

httpd = make_server('localhost', 5000, AppTestByAuto)
httpd.serve_forever()