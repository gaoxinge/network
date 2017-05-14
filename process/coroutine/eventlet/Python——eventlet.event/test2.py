from eventlet import event

evt = event.Event()
evt.send_exception(RuntimeError())
evt.wait()