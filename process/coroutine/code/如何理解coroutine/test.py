class Button(object):
    state = 0
    
    def push(self):
        if self.state == 0:
            self.state = 1
        elif self.state == 1:
            self.state = 2
        elif self.state == 2:
            self.state = 3
        else:
            self.state = 0
        return self.state
        
def push_switch():
    state = 0
    while True:
        state = 1
        yield state
        state = 2
        yield state
        state = 3
        yield state
        state = 0
        yield state
        
def main():
    btn = Button()
    print 'object switch'
    print btn.push()
    print btn.push()
    print btn.push()
    print btn.push()
    btn2 = push_switch()
    print 'coroutine switch'
    print btn2.next()
    print btn2.next()
    print btn2.next()
    print btn2.next()
    
main()