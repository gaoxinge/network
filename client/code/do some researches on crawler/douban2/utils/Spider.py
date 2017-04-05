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
            
    def run_with_syschronous(self):
        while True:
            if self.urls:
                url = self.urls.pop(0)
                self.http_parse_store(url)
            else:
                break
        self.config.close()
    
    def run_with_multithread(self):
        import threading
        threads = []
        lock = threading.Lock()
        while True:
            if self.urls:
                lock.acquire()
                url = self.urls.pop(0)
                thread = threading.Thread(target=self.http_parse_store, args=(url,))
                threads.append(thread)
                lock.release()
                thread.start()
                thread.join()
            else:
                lock.acquire()
                for _ in threads:
                    if not _.is_alive():
                        threads.remove(_)
                if not threads:
                    break
                lock.release()
        self.config.close()
        
    def run(self, method='syschronous'):
        run_with = self.__getattribute__('run_with_' + method)
        run_with()