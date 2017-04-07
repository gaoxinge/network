class Spider(object):
    
    def __init__(self, urls, seen=None):
        self.urls = urls
        self.seen = seen
        self.config = None
        self.basic = {
            'http':  None,
            'parse': None,
            'save': None,
        }
        
    def http(self, f):
        self.basic['http'] = f
        return f
        
    def parse(self, f):
        self.basic['parse'] = f
        return f

    def save(self, f):
        self.basic['store'] = f
        return f
    
    def filter(self, url):
        if url not in self.seen:
            self.urls.append(url)
            self.seen.add(url)
    
    def http_parse_save(self, url):
        response = self.basic['http'](url)
        items = self.basic['parse'](response)
        for item in items:
            self.basic['store'](item)
            
    def run(self):
        while True:
            if self.urls and len(self.seen) < 100:
                url = self.urls.pop(0)
                self.http_parse_save(url)
            else:
                break
        if self.config is not None:
            self.config.close()