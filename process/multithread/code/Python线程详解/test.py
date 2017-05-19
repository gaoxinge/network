import sys
import threading
import Queue
import traceback

class NoResultsPending(Exception):
    pass

class NoWorkersAvailable(Exception):
    pass
    
def _handle_thread_exception(request, exc_info):
    traceback.print_exception(*exc_info)
    
class WorkerThread(threading.Thread):
    
    def __init__(self, requestQueue, resultQueue, poll_timeout=5, **kwds):
        threading.Thread.__init__(self, **kwds)
        self.setDaemon(True)
        self._requestQueue = requestQueue
        self._resultQueue = resultQueue
        self._poll_timeout = poll_timeout
        self._dismissed = threading.Event()
        self.start()
        
    def run(self):
        while True:
            if self._dismissed.is_set():
                break
            try:
                request = self._requestQueue.get(True, self._poll_timeout)
            except Queue.Empty:
                continue
            else:
                if self._dismissed.is_set():
                    self._requestQueue.put(request)
                    break
                try:
                    result = request.callable(*request.args, **request.kwds)
                    print self.getName()
                    self._resultQueue.put((request, result))
                except:
                    request.exception = True
                    self._resultQueue.put((request, sys.exc_info()))
                    
    def dismiss(self):
        self._dismissed.set()
        
class WorkRequest(object):
    
    def __init__(self, callable_, args=None, kwds=None, requestID=None,
                 callback=None, exc_callback=_handle_thread_exception):
        if requestID == None:
            self.requestID = id(self)
        else:
            try:
                self.requestID = hash(requestID)
            except TypeError:
                raise TypeError('requestId must be hashable')
        self.exception = False
        self.callback = callback
        self.exc_callback = exc_callback
        self.callable = callable_
        self.args = args or []
        self.kwds = kwds or {}
        
    def __str__(self):
        return 'WorkRequest id=%s args=%r kwargs=%r exception=%s' % \
            (self.requestID, self.args, self.kwds, self.exception)
            
class ThreadPool(object):
    
    def __init__(self, num_workers, q_size=0, resq_size=0, poll_timeout=5):
        self._requestQueue = Queue.Queue(q_size)
        self._resultQueue = Queue.Queue(resq_size)
        self.workers = []
        self.dismissedWorkers = []
        self.workRequests = {}
        self.createWorkers(num_workers, poll_timeout)
        
    def createWorkers(self, num_workers, poll_timeout=5):
        for i in range(num_workers):
            self.workers.append(WorkerThread(self._requestQueue, self._resultQueue, poll_timeout))
            
    def dismissWorkers(self, num_workers, do_join=False):
        dismiss_list = []
        for i in range(min(num_workers, len(self.workers))):
            worker = self.workers.pop()
            worker.dismiss()
            dismiss_list.append(worker)
        if do_join:
            for worker in dismiss_list:
                worker.join()
        else:
            self.dismissedWorkers.extend(dismiss_list)
            
    def joinAllDismissedWorkers(self):
        for worker in self.dismissedWorkers:
            worker.join()
        self.dismissedWorkers = []
        
    def putRequest(self, request, block=True, timeout=None):
        assert isinstance(request, WorkRequest)
        assert not getattr(request, 'exception', None)
        self._requestQueue.put(request, block, timeout)
        self.workRequests[request.requestID] = request
        
    def poll(self, block=False):
        while True:
            if not self.workRequests:
                raise NoResultsPending
            elif block and not self.workers:
                raise NoWorkersAvailable
            try:
                request, result = self._resultQueue.get(block=block)
                if request.exception and request.exc_callback:
                    request.exc_callback(request, result)
                if request.callback and not (request.exception and request.exc_callback):
                    request.callback(request, result)
                del self.workRequests[request.requestID]
            except Queue.Empty:
                break
                
    def wait(self):
        while True:
            try:
                self.poll(True)
            except NoResultsPending:
                break
                
    def workersize(self):
        return len(self.workers)
        
    def stop(self):
        self.dismissWorkers(self.workersize(), True)
        self.joinAllDismissedWorkers()
        
if __name__=='__main__':
    import random
    import time
    import datetime
    def do_work(data):
        time.sleep(random.randint(1,3))
        res = str(datetime.datetime.now()) + "" +str(data)
        return res
    
    def print_result(request,result):
        print "---Result from request %s : %r" % (request.requestID,result)
    
    main = ThreadPool(3)
    for i in range(40):
        req = WorkRequest(do_work,args=[i],kwds={},callback=print_result)
        main.putRequest(req)
        print "work request #%s added." % req.requestID
    
    print '-'*20, main.workersize(),'-'*20
    
    counter = 0
    while True:
        try:
            time.sleep(0.5)
            main.poll()
            if(counter==5):
                print "Add 3 more workers threads"
                main.createWorkers(3)
                print '-'*20, main.workersize(),'-'*20
            if(counter==10):
                print "dismiss 2 workers threads"
                main.dismissWorkers(2)
                print '-'*20, main.workersize(),'-'*20
            counter+=1
        except NoResultsPending:
            print "no pending results"
            break
    
    main.stop()
    print "Stop"