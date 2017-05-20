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
        
    def __len__(self):
        self.lock.acquire()
        try:
            return len(self.initializer)
        finally:
            self.lock.release()
            
    def __str__(self):
        self.lock.acquire()
        try:
            return str(self.initializer)
        finally:
            self.lock.release()
    
    def __repr__(self):
        self.lock.acquire()
        try:
            return repr(self.initializer)
        finally:
            self.lock.release()
            
r = Resources([1, 2, 3])
print r
r.push(4)
print r
r.pop()
print r
print bool(r)
print len(r)
print str(r)
print repr(r)