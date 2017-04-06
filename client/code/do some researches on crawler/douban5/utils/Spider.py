import threading

class Worker(threading.Thread):
    
    def __init__(self, queue, f):
        threading.Thread.__init__(self)
        self.queue = queue
        self.f = f
    
    def run(self):
        while True:
            url = self.queue.get()
            if url == 'exit':
                break
            self.f(url)

class Spider(object):
    
    def __init__(self, urls):
        self.urls = urls
        self.config = None
        self.basic = {
            'http':  None,
            'parse': None,
            'store': None,
        }
        
    def http(self, f):
        self.basic['http'] = f
        return f
        
    def parse(self, f):
        self.basic['parse'] = f
        return f

    def store(self, f):
        self.basic['store'] = f
        return f
        
    def http_parse_store(self, url):
        response = self.basic['http'](url)
        items = self.basic['parse'](response)
        for item in items:
            self.basic['store'](item)
        
    def run(self, num):
        import Queue
        queue = Queue.Queue()
        workers = []
        for _ in range(num):
            worker = Worker(queue, self.http_parse_store)
            workers.append(worker)
        flag = True
        
        while True:
            if self.urls:
                url = self.urls.pop(0)
                queue.put(url)
                for _ in workers:
                    if not _.is_alive():
                        workers.remove(_)
                        worker = Worker(queue, self.http_parse_store)
                        workers.append(worker)
                        worker.start()
            elif flag:
                for _ in range(num):
                    queue.put('exit')
                flag = False
            else:
                count = 0
                for _ in workers:
                    if not _.is_alive():
                        count += 1
                if count == num:
                    break
                    
        if self.config is not None:
            self.config.close()
                
        
        