import requests
from lxml import etree
from collections import defaultdict
from utils import Spider

spider = Spider(
    urls=['https://github.com/gaoxinge?tab=following'],
    seen=set(['https://github.com/gaoxinge?tab=following']),
)
d = defaultdict(list)

@spider.http
def http(url):
    response = requests.get(url)
    return response
    
@spider.parse
def parse(response):
    root = etree.HTML(response.text)
    results = root.xpath('//span[@class=\'link-gray pl-1\']/text()')
    the = response.url[19:][:-14]
    for result in results:
        d[the].append(result)
        tmp = 'https://github.com/' + result + '?tab=following'
        spider.filter(tmp)
    return []

@spider.save
def save(item):
    pass

spider.run()
print d