import requests
import time
from lxml import etree
from multiprocessing import Pool

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

def start_request(url):
    print ('[%s] request start: ' + url) % time.ctime()
    try:
        response = requests.get(url)
        print ('[%s] request end: (' + str(response.status_code) + ') ' + url) % time.ctime()
    except:
        print ('[%s] request end: (error) ' + url) % time.ctime()
    start_parse(response)

def start_parse(response):
    print ('[%s] parse start: ' + response.url) % time.ctime()
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
            start_storage(item)
        except:
            pass
    print ('[%s] parse end: ' + response.url) % time.ctime()

f = open('items.json', 'w')

def start_storage(item):
    global f
    f.write(item.__str__() + '\n')

def main():
    global f
    pool = Pool(processes=3)
    urls = ['http://stackoverflow.com/questions/?page=' + str(i) + '&sort=votes' for i in range(1,500)]
    pool.map(start_request, urls)
    f.close()
    
if __name__ == '__main__':
    main()
