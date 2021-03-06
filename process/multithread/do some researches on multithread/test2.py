# -*- coding: utf-8 -*-

class Scheduler(object):
    
    def __init__(self, configs):
    
        def check():
            for count in counts:
                if count:
                    return False
            for config in configs:
                if config[0]:
                    return False
            return True
        
        counts = []
        self.factories = []
        for config in configs:
            count = Count()
            counts.append(count)
            factory = Factory(config[0], config[1], config[2], count, check)
            self.factories.append(factory)
            
    def run(self):
        for factory in self.factories:
            factory.start()
        for factory in self.factories:
            factory.join()