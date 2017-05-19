import Queue
import threading
import time

lock = threading.Lock()

class WorkManager(object):
    
    def __init__(self, work_num=1000, thread_num=2):
        self.work_queue = Queue.Queue()
        self.threads = []
        self.__init_thread_pool(thread_num)
        self.__init_work_queue(work_num)

    def __init_work_queue(self, thread_num):
        for i in range(thread_num):
            self.threads.append(Work(self.work_queue))
            
    def __init_thread_pool(self, jobs_num):
        for i in range(jobs_num):
            self.add_job(do_job, i)
            
    def add_job(self, func, *args):
        self.work_queue.put((func, list(args)))
        
    def wait_allcomplete(self):
        for item in self.threads:
            if item.isAlive():
                item.join()
                
class Work(threading.Thread):
    
    def __init__(self, work_queue):
        threading.Thread.__init__(self)
        self.work_queue = work_queue
        self.start()
        
    def run(self):
        while True:
            try:
                do, a = self.work_queue.get(block=False)
                do(a)
                self.work_queue.task_done()
            except Exception, e:
                print str(e)
                break
                
def do_job(args):
    with lock:
        print args
    time.sleep(0.1)
    with lock:
        print threading.current_thread(), list(args)
    
start = time.time()
work_manager = WorkManager(10, 2)
work_manager.wait_allcomplete()
end = time.time()
print 'cost all time: %s' % (end-start)