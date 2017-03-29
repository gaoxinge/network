import time
import requests
import threading
from lxml import etree
from multiprocessing.dummy import Pool as ThreadPool

class Item(dict):
    _fields = ['title', 'rating', 'vote']
    
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        if key in self._fields:
            self.data[key] = value
        else:
            raise Exception('%s is not in fields.' % key)

    def __delitem__(self, key):
        del self.data[key]

    def keys(self):
        return self.data.keys()

    def __str__(self):
        return self.data.__str__()

    __repr__ = __str__


class Worker(object):
    def fetcher(self, url):
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        return response

    def parser(self, response):
        root = etree.HTML(response.text)
        results = root.xpath('//div[@class=\'pl2\']')

        for result in results:
            item = Item()
            item['title'] = result.xpath('a/text()')[0][:-2].strip()
            item['rating'] = float(result.xpath('.//span[@class=\'rating_nums\']/text()')[0])
            item['vote'] = int(result.xpath('.//span[@class=\'pl\']/text()')[0][1:][:-4])
            yield item

    def saver(self, item, f):
        f.write(item.__str__()+'\n')

class Factory(object):
    def __init__(self, urls, filename, process_number):
        self.lock = threading.Lock()
        self.pool = ThreadPool(processes=process_number)
        with open(filename, 'w') as f:
            self.f = f
            self.pool.map(self.work, urls)
            
    def work(self, url):
        worker = Worker()
        with self.lock:
            print '[%s] fetcher (start) <(*) %s>' % (time.ctime(), url)
        try:
            response = worker.fetcher(url)
            with self.lock:
                print '[%s] fetcher (end) <(%s) %s>' % (time.ctime(), response.status_code, url)
        except:
            with self.lock:
                print '[%s] fetcher (end) <(fail) %s>' % (time.ctime(), url)
            
        with self.lock:
            print '[%s] parser (start) <(*) %s>' % (time.ctime(), url)
        try:
            items = worker.parser(response)
            with self.lock:
                print '[%s] parser (end) <(success) %s>' % (time.ctime(), url)
        except:
            with self.lock:
                print '[%s] parser (end) <(fail) %s>' % (time.ctime(), url)
        try:
            for item in items:
                with self.lock:
                    print '[%s] saver (start) <(*) item>' % time.ctime()
                worker.saver(item, self.f)
                with self.lock:
                    print '[%s] saver (end) <(*) item>' % time.ctime()
        except:
            pass

if __name__ == '__main__':
    factory = Factory(['https://movie.douban.com/tag/2016?start=' + str((i-1)*20) for i in range(1, 100)], 'douban.txt', 3)
