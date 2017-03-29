import time
import threading
import logging
import logging.config
from request import request
from lxml import etree
from multiprocessing.dummy import Pool as ThreadPool

class Item(dict):
    _fields = ['votes', 'answers', 'views', 'title', 'link']
    
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
        response = request('GET', url)
        return response

    def parser(self, response):
        root = etree.HTML(response[1])
        results = root.xpath('//div[@class=\'question-summary\']')

        for result in results:
            item = Item()
            item['votes'] = result.xpath('div[@class=\'statscontainer\']//strong/text()')[0]
            item['answers'] = result.xpath('div[@class=\'statscontainer\']//strong/text()')[1]
            item['views'] = result.xpath('div[@class=\'statscontainer\']/div[@class=\'views supernova\']/text()')[0].strip()
            item['title'] = result.xpath('div[@class=\'summary\']/h3/a/text()')[0]
            item['link'] = result.xpath('div[@class=\'summary\']/h3/a/@href')[0]
            yield item

    def saver(self, item, f):
        f.write(item.__str__()+'\n')

class Factory(object):
    def __init__(self, urls, filename, process_number):
        self.lock = threading.Lock()
        self.pool = ThreadPool(processes=process_number)
        
        logging.config.fileConfig('logger.conf')
        self.fetcher_logger = logging.getLogger('fetcher')
        self.parser_logger = logging.getLogger('parser')
        self.saver_logger = logging.getLogger('saver')

        self.global_item_number = 0
        
        with open(filename, 'w') as f:
            self.f = f
            self.pool.map(self.work, urls)
            
    def work(self, url):
        worker = Worker()
        
        self.fetcher_logger.info('<(GET) %s>' % url)
        try:
            response = worker.fetcher(url)
            if response.status_code == 200:
                self.fetcher_logger.debug('<(%s) %s>' % (response[0], url))
            else:
                self.fetcher_logger.warning('<(%s) %s>' % (response[0], url))
        except:
            self.fetcher_logger.error('<(FAIL) %s>' % url)
            
        self.parser_logger.info('<(BEGIN) %s>' % url)
        try:
            items = worker.parser(response)
            self.parser_logger.debug('<(SUCCESS) %s>' % url)
        except:
            self.parser_logger.error('<(FAIL) %s>' % url)

        try:
            for item in items:
                with self.lock:
                    self.global_item_number += 1
                    local_item_number = self.global_item_number
                self.saver_logger.info('<(BEGIN) %s-th item>' % local_item_number)
                worker.saver(item, self.f)
                self.saver_logger.debug('<(SUCCESS) %s-th item>' % local_item_number)
        except:
            pass

if __name__ == '__main__':
    factory = Factory(['http://stackoverflow.com/questions/?page=' + str(i) + '&sort=votes' for i in range(1, 100)], 'stack.txt', 3)
