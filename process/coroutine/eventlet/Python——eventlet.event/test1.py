import eventlet
from eventlet import event

def waiter():
    print('about to wait')
    result = evt.wait()
    print('waited for {0}'.format(result))
    
evt = event.Event()
thread = eventlet.spawn(waiter)
eventlet.sleep(0)
evt.send('a')
eventlet.sleep(0)