from time import localtime
from socket import AF_INET, SOCK_STREAM, socket, setdefaulttimeout
import threading
import threadpool

lock = threading.Lock()

def portScanner(port):
    try:
        s = socket(AF_INET, SOCK_STREAM)
        s.connect(('www.baidu.com', port))
        with lock:
            a = localtime()
            print '[%d:%d:%d]port %d open' % (a[3], a[4], a[5], port)
        s.close()
    except:
        with lock:
            a = localtime()
            print '[%d:%d:%d]port %d close' % (a[3], a[4], a[5], port)

if __name__ == '__main__':
    setdefaulttimeout(1)
    pool = threadpool.ThreadPool(10)
    requests = threadpool.makeRequests(portScanner, [p for p in xrange(1, 1024)])
    [pool.putRequest(req) for req in requests]
    pool.wait()
