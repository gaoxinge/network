import threadpool
import threading
import time
import requests
from lxml import etree

class Item(dict):
    fields = ['votes', 'answers', 'views', 'title', 'link']
    
    def __init__(self):
        self.data = {}

    def __getitem__(self, id):
        return self.data[id]

    def __setitem__(self, id, value):
        if id in self.fields:
            self.data[id] = value
        else:
            raise Exception(id)

    def __delitem__(self, id):
        del self.data[id]

    def __str__(self):
        return self.data.__str__()

    __repr__ = __str__

def start(urls):
    with open('items.txt', 'w') as f:

        def start_one(url):
            response = requests.get(url)
            lock.acquire()
            print ('[%s] (' + str(response.status_code) + ') ' + response.url) % time.ctime()
            lock.release()
            root = etree.HTML(response.text)
            results = root.xpath('//div[@class=\'question-summary\']')
            for result in results:
                try:
                    item = Item()
                    item['votes'] = result.xpath('div[@class=\'statscontainer\']//strong/text()')[0]
                    item['answers'] = result.xpath('div[@class=\'statscontainer\']//strong/text()')[1]
                    item['views'] = result.xpath('div[@class=\'statscontainer\']/div[@class=\'views supernova\']/text()')[0].strip()
                    item['title'] = result.xpath('div[@class=\'summary\']/h3/a/text()')[0]
                    item['link'] = result.xpath('div[@class=\'summary\']/h3/a/@href')[0]
                    f.write(item.__str__() + '\n')
                except:
                    pass
            lock.acquire()
            print ('[%s] (added) ' + url) % time.ctime()
            lock.release()

        lock = threading.Lock()
        pool = threadpool.ThreadPool(5)
        reqs = threadpool.makeRequests(start_one, urls)
        [pool.putRequest(req) for req in reqs]
        pool.wait()
    
def main():
    start(['http://stackoverflow.com/questions/?page=' + str(i) + '&sort=votes' for i in range(1,500)])

if __name__ == '__main__':
    main()
