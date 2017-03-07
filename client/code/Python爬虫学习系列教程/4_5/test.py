import threading
import time

def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print '%s: %s' % (threadName, time.ctime(time.time()))

t1 = threading.Thread(target=print_time, args=('Thread-1', 2,))
t2 = threading.Thread(target=print_time, args=('Thread-2', 4,))

t1.start()
t2.start()

print 'Main Finished'
