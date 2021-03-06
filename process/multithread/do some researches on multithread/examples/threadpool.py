# -*- coding: utf-8 -*-
from schedulery import Resources, Scheduler

class ThreadPool(object):
    
    def __init__(self, num):
        self.num = num
       
    def map(self, func, initializer):
        initial = Resources(initializer)
        results = Resources([])
        
        def f(x):
            results.push(func(x))
        
        configs = [(initial, f, self.num)]
        scheduler = Scheduler(configs)
        scheduler.run()
        return results