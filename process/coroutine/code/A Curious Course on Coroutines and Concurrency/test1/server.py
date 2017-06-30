# -*- coding: utf-8 -*-
from test import *

def add(x, y):
    yield x+y
    
def main():
    r = yield add(2, 2)
    print r
    yield

sched = Scheduler()
sched.new(main())
sched.mainloop()