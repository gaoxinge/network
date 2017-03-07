import threadpool
import time

def now_time(n):
    print 'Starting at %s' % time.ctime()
    time.sleep(n)
    print 'Ending at %s' % time.ctime()

def print_now(request, n):
    print '%s - %s' % (request.requestID, n)

pool = threadpool.ThreadPool(5)
requests = threadpool.makeRequests(now_time, range(1,11), print_now)
[pool.putRequest(req) for req in requests]
pool.wait()
