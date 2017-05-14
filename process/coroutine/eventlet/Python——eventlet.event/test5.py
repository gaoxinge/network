import time
import eventlet
from eventlet import event
from eventlet import greenthread

def Joker():
    i = 0
    while i < 3:
        print('Joker: Can anybody get me?')
        i += 1
        time.sleep(1)
    print evt.wait()
    print('Fighting.')
    time.sleep(3)
    return 'Joker: Sorry, you got missed.'
    
def Batman():
    evt.send('Bat man: I\'m coming for you!')
    return 'Bat man: I\'m back, and your day is coming soon.'
    
evt = event.Event()
gt1 = greenthread.spawn(Joker)
gt2 = greenthread.spawn_after(5, Batman)
print gt1.wait()
time.sleep(1)
print gt2.wait()
time.sleep(2)
print('To be continued.')