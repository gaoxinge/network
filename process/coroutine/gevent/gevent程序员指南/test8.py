import gevent
import signal

def run_forever():
    gevent.sleep(1000)
    
gevent.signal(signal.SIGQUIT, gevent.shutdown)
thread = gevent.spawn(run_forever)
thread.join()