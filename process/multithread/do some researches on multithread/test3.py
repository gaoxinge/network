# -*- coding: utf-8 -*-
import threading

class Factory(threading.Thread):
    
    def __init__(self, resources, func, num, count, check):
        threading.Thread.__init__(self)
        self.resources = resources
        self.func = func
        self.num = num
        self.count = count
        self.check = check
    
    def prepare(self):
        import Queue
        self.queue = Queue.Queue()
        self.workers = []
        for i in range(self.num):
            worker = Worker(self.func, self.queue, self.count)
            self.workers.append(worker)
    
    def terminate(self):
        for worker in self.workers:
            worker.event.set()
    
    def run(self):
        self.prepare()
        for worker in self.workers:
            worker.start()
        while True:
            if not self.resources.is_empty():
                self.queue.put(self.resources.pop())
                self.count.add()
            else if self.check():
                break
        self.terminate()
        