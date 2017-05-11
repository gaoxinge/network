class State(object):
    
    def __init__(self):
        self.NewState(StateStart)
        
    def NewState(self, state):
        self.__class__ = state
        
    def Action(self):
        raise NotImplementedError()
        
class StateStart(State):
    
    def Action(self):
        print 'StateStart is running'
        self.NewState(StateTask1)
        
class StateTask1(State):
    
    def Action(self):
        print 'StateTask1 is running'
        self.NewState(StateTask2)
        
class StateTask2(State):
    
    def Action(self):
        print 'StateTask2 is running'
        self.NewState(StateEnd)
        
class StateEnd(State):
    
    def Action(self):
        print 'StateEnd is running'
        self.NewState(StateStart)
        
c = State()
print c.NewState
c.Action()
c.Action()
c.Action()
c.Action()
c.Action()