# -*- coding: utf-8 -*-
import threading

class Worker(object):
    
    def __init__(self, func, queue, count):
        self.func = func
        self.queue = queue
        self.count = count
        self.event = threading.Event()
        
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
                finally:
                    self.count.sub()