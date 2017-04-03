import requests
from lxml import etree
from utils import Spider, Item

spider = Spider(['http://stackoverflow.com/questions/?page=' + str(i) + '&sort=votes' for i in range(1, 3)])
spider.config = f.open('stackoverflow.txt', 'w')

@spider.http
def http(url):
    response = requests.get(url)
    return response

@spider.parse
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

@spider.store
def store(config, item):
    config.write(str(item) + '\n')

spider.run(method='syschronous')