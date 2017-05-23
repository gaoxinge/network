import select
import socket
import Queue
import time
import os

class Server(object):
    
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(('', 8008))
        self.server.setsockopt(socket.SOL_SOCKET, socket.SEUSEADDR, 1)
        self.server.listen(10)
        self.server.setblocking(10)
        
        self.inputs = [self.server]
        self.outputs = []
        self.message_queues = {}
        
    def run(self):
        while self.inputs:
            print '=================================='
            print 'waiting for next event'
            print 'inputs', self.inputs
            print 'outputs', self.outputs
            print 'queue', self.message_queues
           
            readable, writable, exceptional = select.select(self.inputs, self.outputs, self.inputs)
            
            if not (readable or writable, exceptional):
                break
                
            for s in readable:
                if s is self.server:
                    connection, client_address = s.accept()
                    print 'connection from', client_address
                    connection.setblocking(0)
                    self.inputs.append(connection)
                    self.message_queues[connection] = Queue.Queue()
                else:
                    try:
                        data = s.recv(1024)
                    except:
                        print 'closing', client_address
                        if s in self.outputs:
                            self.outputs.append(s)
                            
            for s in writable:
                try:
                    next_msg = self.message_queues[s].get_nowait()
                except Queue.Empty:
                    print s.getpeername(), 'queue empty'
                    self.outputs.remove(s)
                else:
                    print 'sending', next_msg, 'to', s.getpeername()
                    os.popen('sleep 5').read()
                    s.send(next_msg)
                    
            for s in exceptional:
                print 'exception condition on', s.getpeername()
                self.inputs.remove(s)
                if s in self.outputs:
                    self.outputs.remove(s)
                s.close()
                del self.message_queues[s]
                
if __name__ == '__main__':
    s = Server()
    s.run()