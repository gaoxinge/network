import eventlet
from eventlet import event

def baz(b):
    evt.send(b+1)
    
evt = event.Event()
thread = eventlet.spawn_n(baz, 3)
print evt.wait()