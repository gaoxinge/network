import sys
from eventlet import event

evt = event.Event()
try:
    raise RuntimeError()
except RuntimeError:
    evt.send_exception(*sys.exc_info())
evt.wait()