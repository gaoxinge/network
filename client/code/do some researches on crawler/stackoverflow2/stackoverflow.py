import threadpool
import requests
from lxml import etree
from Item import Item

def http(url):
    response = requests.get(url)
    return response
    
def parse(response):
    Question = Item('Question', ['votes', 'answers', 'views', 'title', 'link'])
    root = etree.HTML(response.text)
    results = root.xpath('//div[@class=\'question-summary\']')
    for result in results:
        question = Question()
        question['votes']   = result.xpath('div[@class=\'statscontainer\']//strong/text()')[0]
        question['answers'] = result.xpath('div[@class=\'statscontainer\']//strong/text()')[1]
        question['views']   = result.xpath('div[@class=\'statscontainer\']/div[@class=\'views supernova\']/text()')[0].strip()
        question['title']   = result.xpath('div[@class=\'summary\']/h3/a/text()')[0]
        question['link']    = result.xpath('div[@class=\'summary\']/h3/a/@href')[0]
        yield question
        
def store(item):
    f.write(str(item) + '\n')

def http_parse_store(url):
    response = http(url)
    items = parse(response)
    for item in items:
        store(item)

urls = ['http://stackoverflow.com/questions/?page=' + str(i) + '&sort=votes' for i in range(1,4)]
f = open('stackoverflow.txt', 'w')

pool = threadpool.ThreadPool(5)
reqs = threadpool.makeRequests(http_parse_store, urls)
[pool.putRequest(req) for req in reqs]
pool.wait()

f.close()