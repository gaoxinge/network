import Queue
import threading
import time

def process_data(threadName, q):
    while not exitFlag:
        lock.acquire()
        if not workQueue.empty():
            data = q.get()
            print '%s processing %s' % (threadName, data)
        lock.release()
        time.sleep(1)


lock = threading.Lock()

words = ['One', 'Two', 'Three', 'Four', 'Five']
workQueue = Queue.Queue(10)
for word in words:
    workQueue.put(word)

exitFlag = 0

t1 = threading.Thread(target=process_data, args=('Thread-1', workQueue))
t2 = threading.Thread(target=process_data, args=('Thread-2', workQueue))
t3 = threading.Thread(target=process_data, args=('Thread-3', workQueue))

t1.start()
t2.start()
t3.start()

while not workQueue.empty():
    pass

exitFlag = 1

t1.join()
t2.join()
t3.join()

print 'Exiting Main Thread'
