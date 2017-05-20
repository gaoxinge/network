# -*- coding: utf-8 -*-

class Count(object):
    
    def __init__(self, count=0):
        import threading
        self.lock = threading.Lock()
        self.count = count
        
    def __iadd__(self, other):
        self.lock.acquire()
        try:
            self.count += other
            return self
        finally:
            self.lock.release()
        
    def __isub__(self, other):
        self.lock.acquire()
        try:
            self.count -= other
            return self
        finally:
            self.lock.release()
            
    def __nonzero__(self):
        self.lock.acquire()
        try:
            return self.count.__nonzero__()
        finally:
            self.lock.release()
            
    def __str__(self):
        self.lock.acquire()
        try:
            return str(self.count)
        finally:
            self.lock.release()
            
    def __repr__(self):
        self.lock.acquire()
        try:
            return repr(self.count)
        finally:
            self.lock.release()
            
c = Count(5)
print c
c += 1
print c
c -= 1
print c
print bool(c)
print c.__nonzero__()
print str(c)
print repr(c)