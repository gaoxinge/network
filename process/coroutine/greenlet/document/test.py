from greenlet import greenlet

def process_commands(*args):
    while True:
        line = ''
        while not line.endswith('\n'):
            line += read_next_char()
        if line == 'quit\n':
            print 'are you sure?'
            if read_next_char() != 'y':
                continue
        process_command(line)
        
def event_keydown(key):
    g_process.switch(key)
    
def read_next_char():
    g_self = greenlet.getcurrent()
    next_char = g_self.parent.switch()
    return next_char
    
g_processor = greenlet(process_commands)
g_processor.switch(*args)
gui.mainloop()