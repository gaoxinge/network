# -*- coding: utf-8 -*-

class Resources(object):
    
    def __init__(self, initializer=[]):
        import threading
        self.lock = threading.Lock()
        self.initializer = initializer
        
    def push(self, obj):
        self.lock.acquire()
        self.initializer.append(obj)
        self.lock.release()
        
    def pop(self):
        self.lock.acquire()
        self.initializer.pop(0)
        self.lock.release()
        
    def size(self):
        self.lock.acquire()
        try:
            return len(self.initializer)
        finally:
            self.lock.release()
            
    def is_empty(self):
        self.lock.acquire()
        try:
            return not bool(self.initializer)
        finally:
            self.lock.release()
            
r = Resources([1, 2, 3])
print r.initializer
r.push(4)
print r.initializer
r.pop()
print r.initializer
print r.size()
print r.is_empty()