import threading
import time

def worker():
    print 'worker'
    time.sleep(1)
    return
    
t = threading.Thread(target=worker)
t.setDaemon(True)
t.start()
print 'hello world'