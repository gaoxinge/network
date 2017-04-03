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
            self.basic['store'](self.config, item)
            
    def run_with_syschronous(self):
        while self.urls:
            url = self.urls.pop(0)
            self.http_parse_store(url)
        self.config.close()
        
    def run(self, method='syschronous'):
        run_with = object.__getattribute__(self, 'run_with' + method)
        run_with()