from werkzeug.wrappers import Request
from pprint import pprint

request = Request({'REQUEST_METHOD': 'get', 'PATH_INFO': '/article', 'QUERY_STRING': 'id=1'})
pprint(request.environ)