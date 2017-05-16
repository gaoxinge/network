import threading
import datetime
import logging
import time

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s) %(message)s')
list = ['192.168.1.1', '192.168.1.2']

class Test(threading.Thread):
    
    def __init__(self, ip):
        threading.Thread.__init__(self)
        self.ip = ip
        
    def run(self):
        logging.debug('%s start!' % self.ip)
        time.sleep(5)
        logging.debug('%s done!' % self.ip)
        
for ip in list:
    t = Test(ip)
    t.start()
for t in threading.enumerate():
    if t is threading.currentThread():
        continue
    t.join()
logging.debug('Done!')