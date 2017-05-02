from time import localtime
from socket import AF_INET, SOCK_STREAM, socket, setdefaulttimeout

class ObjWithConnect(object):
    
    def __init__(self, h):
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.host = h
        
    def connect(self, p):
        self.socket.connect((self.host, p))
    
    def close(self):
        self.socket.close()

class Connection(ObjWithConnect):
        
    def __enter__(self):
        return self
        
    def __exit__(self, type, value, traceback):
        self.close()

if __name__ == '__main__':
    setdefaulttimeout(1)
    for p in xrange(1, 1024):
        a = localtime()
        try:
            with Connection('www.baidu.com') as c:
                c.connect(p)
                print '[%d:%d:%d]port %d open' % (a[3], a[4], a[5], p)
        except:
            print '[%d:%d:%d]port %d close' % (a[3], a[4], a[5], p)