import threading
import time

def print_time(threadName, delay, counter):
    print 'Starting', threadName
    while counter:
        time.sleep(delay)
        print '%s: %s' % (threadName, time.ctime(time.time()))
        counter -= 1
    print 'Exiting', threadName

t1 = threading.Thread(target=print_time, args=('Thread-1', 1, 5,))
t2 = threading.Thread(target=print_time, args=('Thread-2', 2, 5,))

t1.start()
t2.start()

print 'Exiting Main Thread'
