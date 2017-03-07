import threadpool
import time

def now_time(n):
    print n
    print n

pool = threadpool.ThreadPool(5)
requests = threadpool.makeRequests(now_time, range(1, 10000))
[pool.putRequest(req) for req in requests]
pool.wait()
