def Log(step, status, message):
    import datetime
    import threading
    lock = threading.Lock()
    lock.acquire()
    print '[{a}][{b}][{c}] {d}'.format(
        a=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        b=step,
        c=status,
        d=message,
    )
    lock.release()