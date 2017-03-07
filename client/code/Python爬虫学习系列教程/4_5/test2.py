import threading
import time

def print_time(threadName, delay, counter):
    lock.acquire()
    print 'Staring', threadName
    lock.release()
    lock.acquire()
    while counter:
        time.sleep(delay)
        print '%s: %s' % (threadName, time.ctime(time.time()))
        counter -= 1
    lock.release()
    lock.acquire()
    print 'Exiting', threadName
    lock.release()

lock = threading.Lock()

t1 = threading.Thread(target=print_time, args=('Thread-1', 1, 5,))
t2 = threading.Thread(target=print_time, args=('Thread-2', 2, 5,))

t1.start()
t2.start()

t1.join()
t2.join()

print 'Exiting Main Thread'
