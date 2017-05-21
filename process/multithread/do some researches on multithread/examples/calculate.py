# -*- coding: utf-8 -*-
from schedulery import Resources, Scheduler

sum = 0

p = Resources([i for i in range(100)])
q = Resources([])
r = Resources([])

def f(x):
    q.push(x+x)
    
def g(x):
    r.push(x*x)
    
def h(x):
    global sum
    sum += x
    
configs = [
    (p, f, 5),
    (q, g, 5),
    (r, h, 1),
]
scheduler = Scheduler(configs)
scheduler.run()
print sum