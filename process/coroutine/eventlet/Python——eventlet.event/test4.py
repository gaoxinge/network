import eventlet
from eventlet import event

def wait_on():
    retval = evt.wait()
    print('waited for {0}'.format(retval))
    
evt = event.Event()
thread = eventlet.spawn(wait_on)
evt.send('result')
eventlet.sleep(0)
evt.wait()