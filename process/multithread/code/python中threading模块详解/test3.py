import threading
import time

def worker():
    print 'worker'
    time.sleep(1)
    return
    
threads = []

for _ in xrange(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()
    
for _ in threading.enumerate():
    print _
    
for _ in threads:
    print _