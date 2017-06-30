# -*- coding: utf-8 -*-
from test import *

def foo():
    mytid = yield GetTid()
    while True:
        print "I'm foo", mytid
        yield
        
def main():
    child = yield NewTask(foo())
    for _ in xrange(5):
        yield
    yield KillTask(child)
    print "main done"
        
sched = Scheduler()
sched.new(main())
sched.mainloop()