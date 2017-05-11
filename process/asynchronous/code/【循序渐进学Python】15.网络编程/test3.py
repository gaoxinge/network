from SocketServer import TCPServer, StreamRequestHandler

class Handler(StreamRequestHandler):

    def handle(self):
        addr = self.request.getpeername()
        self.wfile.write('Thank you for connectiong')

server = TCPServer(('',8088),Handler)
server.serve_forever()