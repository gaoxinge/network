import threading
import datetime
import logging
import time

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s) %(message)s')
list = ['192.168.1.1', '192.168.1.2']

class Test(threading.Thread):
    
    def __init__(self, threadingSum, ip):
        threading.Thread.__init__(self)
        self.threadingSum = threadingSum
        self.ip = ip
        
    def run(self):
        with self.threadingSum:
            logging.debug('%s start!' % self.ip)
            time.sleep(5)
            logging.debug('%s done!' % self.ip)

threadingSum = threading.Semaphore(1)
for ip in list:
    t = Test(threadingSum, ip)
    t.start()
for t in threading.enumerate():
    if t is threading.currentThread():
        continue
    t.join()
logging.debug('Done!')