# -*- coding: utf-8 -*-
import Queue
import select

#############
# Scheduler #
#############

class Scheduler(object):
    
    def __init__(self):
        self.ready = Queue.Queue()
        self.taskmap = {}
        self.read_waiting = {}
        self.write_waiting = {}
        self.exit_waiting = {}

    def schedule(self, task):
        self.ready.put(task)
    
    def new(self, target):
        newtask = Task(target)
        self.taskmap[newtask.tid] = newtask
        self.schedule(newtask)
        return newtask.tid
    
    def waitforread(self, task, fd):
        self.read_waiting[fd] = task
        
    def waitforwrite(self, task, fd):
        self.write_waiting[fd] = task
    
    def waitforexit(self, task, waittid):
        if waittid in self.taskmap:
            self.exit_waiting.setdefault(waittid, []).append(task)
            return True
        else:
            return False
            
    def iopoll(self, timeout):
        if self.read_waiting or self.write_waiting:
            r, w, e = select.select(self.read_waiting, self.write_waiting, [], timeout)
            for fd in r:
                self.schedule(self.read_waiting.pop(fd))
            for fd in w:
                self.schedule(self.write_waiting.pop(fd))
    
    def iotask(self):
        while True:
            if self.ready.empty():
                self.iopoll(None)
            else:
                self.iopoll(0)
            yield
            
    def exit(self, task):
        print "Task %d terminated" % task.tid
        del self.taskmap[task.tid]
        for task in self.exit_waiting.pop(task.tid, []):
            self.schedule(task)
    
    def mainloop(self):
        self.new(self.iotask())
        while self.taskmap:
            task = self.ready.get()
            try:
                result = task.run()
                if isinstance(result, SystemCall):
                    result.task = task
                    result.sched = self
                    result.handle()
                    continue
            except StopIteration:
                self.exit(task)
                continue
            self.schedule(task)

###############
# System Call #
###############

class SystemCall(object):
    
    def handle(self):
        pass
            
class GetTid(SystemCall):
    
    def handle(self):
        self.task.sendval = self.task.tid
        self.sched.schedule(self.task)
        
class NewTask(SystemCall):
    
    def __init__(self, target):
        self.target = target
    
    def handle(self):
        tid = self.sched.new(self.target)
        self.task.sendval = tid
        self.sched.schedule(self.task)
        
class KillTask(SystemCall):
    
    def __init__(self, tid):
        self.tid = tid
        
    def handle(self):
        task = self.sched.taskmap.get(self.tid, None)
        if task:
            task.target.close()
            self.task.sendval = True
        else:
            self.task.sendval = False
        self.sched.schedule(self.task)

class ReadWait(SystemCall):
    
    def __init__(self, f):
        self.f = f
        
    def handle(self):
        fd = self.f.fileno()
        self.sched.waitforread(self.task, fd)
        
class WriteWait(SystemCall):
    
    def __init__(self, f):
        self.f = f
        
    def handle(self):
        fd = self.f.fileno()
        self.sched.waitforwrite(self.task, fd)
        
class WaitTask(SystemCall):
    
    def __init__(self, tid):
        self.tid = tid
        
    def handle(self):
        result = self.sched.waitforexit(self.task, self.tid)
        self.task.sendval = result
        if not result:
            self.sched.schedule(self.task)
            
########
# Task #
########

class Task(object):

    taskid = 0

    def __init__(self, target):
        Task.taskid += 1
        self.tid = Task.taskid
        self.target = target
        self.sendval = None
    
    def run(self):
        return self.target.send(self.sendval)