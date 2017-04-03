import time

def worker():
    print 'worker'
    time.sleep(1)
    return

for _ in xrange(5):
    worker()
