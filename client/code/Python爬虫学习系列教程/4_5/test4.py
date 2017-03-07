import threadpool
import time
import random

def hello(str):
    time.sleep(2)
    return str

data = [random.randint(1,10) for i in range(20)]

def print_result(request, result):
    print 'the result is %s %r' % (request.requestID, result)

pool = threadpool.ThreadPool(5)
requests = threadpool.makeRequests(hello, data, print_result)
[pool.putRequest(req) for req in requests]
pool.wait()
    
