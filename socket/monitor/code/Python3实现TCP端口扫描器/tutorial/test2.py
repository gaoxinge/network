from time import *
from socket import *
import threading
import argparse

lock = threading.Lock()
threads = []

def portScanner(host, port):
    try:
        s = socket(AF_INET, SOCK_STREAM)
        s.connect((host, port))
        lock.acquire()
        a = localtime()
        print '[%d:%d:%d]port %d open' % (a[3], a[4], a[5], port)
        lock.release()
        s.close()
    except:
        pass

if __name__ == '__main__':
    arg = argparse.ArgumentParser(description = 'port scanner')
    arg.add_argument('-H', dest = 'host', type = str)
    args = arg.parse_args()
    hostList = args.host.split(',')
    setdefaulttimeout(1)

    for host in hostList:
        print 'scanning host: %s' % host

        for p in range(1, 1024):
            t = threading.Thread(target = portScanner, args = (host, p))
            t.start()
            threads.append(t)

        for t in threads:
            t.join()
