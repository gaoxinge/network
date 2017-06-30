# -*- coding: utf-8 -*-
from test import *

def foo():
    mytid = yield GetTid()
    for _ in xrange(5):
        print "I'm foo", mytid
        yield
        
def main():
    child = yield NewTask(foo())
    print "Waiting for child"
    yield WaitTask(child)
    print "Child done"
        
sched = Scheduler()
sched.new(main())
sched.mainloop()