from time import localtime
from socket import AF_INET, SOCK_STREAM, socket, setdefaulttimeout

def portScanner(host, port):
    a = localtime()
    try:
        s = socket(AF_INET, SOCK_STREAM)
        s.connect((host, port))
        print '[%d:%d:%d]port %d open' % (a[3], a[4], a[5], port)
        s.close()
    except:
        print '[%d:%d:%d]port %d close' % (a[3], a[4], a[5], port)

if __name__ == '__main__':
    setdefaulttimeout(1)
    for p in range(1, 1024):
        portScanner('www.baidu.com', p)
