import socket
import StringIO
import sys
import datetime

class WSGIServer(object):
    
    def __init__(self, host, port, application):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((host, port))
        self.socket.listen(10)
        self.host = host
        self.port = port
        self.application = application
        
    def serve_forever(self):
        while True:
            self.client_connection, client_address = self.socket.accept()
            self.handle_request()
    
    def handle_request(self):
        self.request_data = self.client_connection.recv(1024)
        self.request_lines = self.request_data.splitlines()
        try:
            self.get_url_parameter()
            app_data = self.application(self.environ, self.start_response)
            self.finish_response(app_data)
            print '[{0}] "{1}" {2}'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                            self.request_lines[0], self.status)
        except Exception, e:
            pass
            
    def get_url_parameter(self):
        self.request_dict = {}
        tmp = self.request_lines[0].split()
        self.request_dict['Method'] = tmp[0]
        self.request_dict['Path'] = tmp[1]
        self.request_dict['Version'] = tmp[2]
        for item in self.request_lines[1:]:
            tmp = item.split(':')
            self.request_dict[tmp[0]] = ':'.join(tmp[1:])
    
    @property
    def environ(self):
        environ = {
            'wsgi.version': (1, 0),
            'wsgi.url_scheme': 'http',
            'wsgi.input': StringIO.StringIO(self.request_data),
            'wsgi.errors': sys.stderr,
            'wsgi.multithread': False,
            'wsgi.mulitprocess': False,
            'wsgi.run_once': False,
            'REQUEST_METHOD': self.request_dict['Method'],
            'PATH_INFO': self.request_dict['Path'],
            'SERVER_NAME': self.host,
            'SERVER_PORT': self.port,
            'USER_AGENT': self.request_dict['User-Agent'],
        }
        return environ
        
    def start_response(self, status, response_headers):
        self.status = status
        self.headers = response_headers
        
    def finish_response(self, app_data):
        try:
            response = 'HTTP/1.1 {status}\r\n'.format(status=self.status)
            for header in self.headers:
                response += '{0}: {1}\r\n'.format(*header)
            response += '\r\n'
            for data in app_data:
                response += data
                self.client_connection.sendall(response)
        finally:
            self.client_connection.close()