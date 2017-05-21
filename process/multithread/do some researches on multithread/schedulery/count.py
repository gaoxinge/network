# -*- coding: utf-8 -*-
import threading

class Count(object):
    
    def __init__(self, count=0):
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