# -*- coding: utf-8 -*-
import threading

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