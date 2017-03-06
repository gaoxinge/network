import threading

global_dict = {}

def process_student():
    print 'Hello, %s (in %s)' % (global_dict[threading.current_thread()],threading.current_thread().name)

def process_thread(name):
    global_dict[threading.current_thread()] = name
    process_student()

t1 = threading.Thread(target = process_thread, args = ('Alice',), name = 'Thread-A')
t2 = threading.Thread(target = process_thread, args = ('Bob',), name = 'Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
