import re
from werkzeug.wrappers import BaseRequest, BaseResponse
from werkzeug.exceptions import HTTPException, MethodNotAllowed, NotImplemented, NotFound
     
class Request(BaseRequest):
    pass

class Response(BaseResponse):
    pass
    
class View(object):
    
    def __init__(self, req):
        self.req = req
        
    def GET(self):
        raise MethodNotAllowed()
        
    HEAD = POST = DELETE = PUT = GET
    
class WebPyApp(object):
    
    def __init__(self, urls, views):
        self.urls = [(re.compile('^%s$' % urls[i]), urls[i+1]) for i in xrange(0, len(urls), 2)]
        self.views = views
        
    def __call__(self, environ, start_response):
        try:
            req = Request(environ)
            for regex, view in self.urls:
                match = regex.match(req.path)
                if match is not None:
                    view = self.views[view](req)
                    if req.method not in ('GET', 'HEAD', 'POST', 'DELETE', 'PUT'):
                        raise NotImplemented()
                    resp = getattr(view, req.method)(*match.groups())
                    break
            else:
                raise NotFound()
        except HTTPException, e:
            resp = e
        return resp(environ, start_response)