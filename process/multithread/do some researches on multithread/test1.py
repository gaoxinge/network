# -*- coding: utf-8 -*-

class Count(object):
    
    def __init__(self, count=0):
        import threading
        self.lock = threading.Lock()
        self.count = count
        
    def add(self):
        self.lock.acquire()
        self.count += 1
        self.lock.release()
        
    def sub(self):
        self.lock.acquire()
        self.count -= 1
        self.lock.release()
    
    def num(self):
        self.lock.acquire()
        try:
            return self.count
        finally:
            self.lock.release()
            
    def is_zero(self):
        self.lock.acquire()
        try:
            return not bool(self.count)
        finally:
            self.lock.release()
            
c = Count(5)
print c.num()
c.add()
print c.num()
c.sub()
print c.num()
print c.is_zero()