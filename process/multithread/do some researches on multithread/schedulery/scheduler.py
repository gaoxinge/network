# -*- coding: utf-8 -*-
import threading
import Queue
from .count import Count

class Worker(threading.Thread):
    
    def __init__(self, func, queue, count):
        threading.Thread.__init__(self)
        self.event = threading.Event()
        self.func = func
        self.queue = queue
        self.count = count
        
    def run(self):
        while True:
            if self.event.is_set():
                break
            try:
                args = self.queue.get(False)
            except Queue.Empty:
                pass
            else:
                try:
                    self.func(args)
                except:
                    pass
                finally:
                    self.count -= 1
                    
class Factory(threading.Thread):
    
    def __init__(self, resources, func, num, count, check):
        threading.Thread.__init__(self)
        self.resources = resources
        self.func = func
        self.num = num
        self.count = count
        self.check = check
    
    def prepare(self):
        self.queue = Queue.Queue()
        self.workers = []
        for _ in range(self.num):
            worker = Worker(self.func, self.queue, self.count)
            self.workers.append(worker)
    
    def work(self):
        for worker in self.workers:
            worker.start()
    
    def terminate(self):
        for worker in self.workers:
            worker.event.set()
    
    def run(self):
        self.prepare()
        self.work()
        while True:
            if self.resources:
                self.queue.put(self.resources.pop())
                self.count += 1
            elif self.check():
                break
        self.terminate()

class Scheduler(object):
    
    def __init__(self, configs):
    
        def check():
            for count in counts:
                if count:
                    return False
            for config in configs:
                if config[0]:
                    return False
            return True
        
        counts = []
        self.factories = []
        for config in configs:
            count = Count()
            counts.append(count)
            factory = Factory(config[0], config[1], config[2], count, check)
            self.factories.append(factory)
            
    def run(self):
        for factory in self.factories:
            factory.start()
        for factory in self.factories:
            factory.join()