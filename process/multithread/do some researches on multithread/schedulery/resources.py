# -*- coding: utf-8 -*-
import threading

class Resources(object):
    
    def __init__(self, initializer=[]):
        self.lock = threading.Lock()
        self.initializer = initializer
        
    def push(self, obj):
        self.lock.acquire()
        self.initializer.append(obj)
        self.lock.release()
        
    def pop(self):
        self.lock.acquire()
        try:
            return self.initializer.pop(0)
        finally:
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