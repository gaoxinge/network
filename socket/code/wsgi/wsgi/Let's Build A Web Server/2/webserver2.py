import socket
import StringIO
import sys

class WSGIServer(object):

    def __init__(self, host, port, application):
        self.listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.listen_socket.bind((host, port))
        self.listen_socket.listen(1)
        self.name = host
        self.port = str(port)
        self.application = application

    def serve_forever(self):
        while True:
            self.client_connection, client_address = self.listen_socket.accept()
            self.handle_request()

    def handle_request(self):
        self.request_data = self.client_connection.recv(1024)
        print ''.join('[request] {line}\n'.format(line=line) for line in self.request_data.splitlines())
        try:
            self.parse_request()
            result = self.application(self.environ, self.start_response)
            self.finish_response(result)
        except:
            pass

    def parse_request(self):
        request_line = self.request_data.splitlines()[0]
        request_line = request_line.strip()
        self.method, self.path, self.version = request_line.split()
    
    @property
    def environ(self):
        environ = {}
        environ['wsgi.version']      = (1, 0)
        environ['wsgi.url_scheme']   = 'http'
        environ['wsgi.input']        = StringIO.StringIO(self.request_data)
        environ['wsgi.errors']       = sys.stderr
        environ['wsgi.multithread']  = False
        environ['wsgi.multiprocess'] = False
        environ['wsgi.run_once']     = False
        environ['REQUEST_METHOD']    = self.method
        environ['PATH_INFO']         = self.path
        environ['SERVER_NAME']       = self.name
        environ['SERVER_PORT']       = self.port
        return environ

    def start_response(self, status, response_headers):
        self.headers_set = [status, response_headers]

    def finish_response(self, result):
        try:
            status, response_headers = self.headers_set
            response = 'HTTP/1.1 {status}\r\n'.format(status = status)
            for response_header in response_headers: 
                response += '{0}: {1}\r\n'.format(*response_header)
            response += '\r\n'
            for data in result: 
                response += data
            print ''.join('[response] {line}\n'.format(line=line) for line in response.splitlines())
            self.client_connection.sendall(response)
        finally:
            self.client_connection.close()
