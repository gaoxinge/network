from time import localtime
from socket import AF_INET, SOCK_STREAM, socket, setdefaulttimeout
import threading

lock = threading.Lock()
threads = []

def portScanner(host, port):
    try:
        s = socket(AF_INET, SOCK_STREAM)
        s.connect((host, port))
        with lock:
            a = localtime()
            print '[%d:%d:%d]port %d open' % (a[3], a[4], a[5], port)
        s.close()
    except:
        pass

if __name__ == '__main__':
    setdefaulttimeout(1)
    
    for p in range(1, 1024):
        t = threading.Thread(target = portScanner, args = ('www.baidu.com', p))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
