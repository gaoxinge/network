import requests
from lxml import etree
from utils import Spider, Log, Item
import time

spider = Spider(['https://movie.douban.com/tag/2016?start=' + str((i-1)*20) for i in range(1, 30)])
spider.config = open('douban.txt', 'wb')

@spider.http
def http(url):
    Log('http', 'start', url)
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    Log('http', 'end', url)
    return response

@spider.parse
def parse(response):
    Movie = Item('Movie', ['title', 'rating', 'vote'])
    root = etree.HTML(response.text)
    results = root.xpath('//div[@class=\'pl2\']')
    for result in results:
        movie = Movie()
        movie['title'] = result.xpath('a/text()')[0][:-2].strip()
        movie['rating'] = float(result.xpath('.//span[@class=\'rating_nums\']/text()')[0])
        movie['vote'] = int(result.xpath('.//span[@class=\'pl\']/text()')[0][1:][:-4])
        yield movie
        
@spider.store
def store(item):
    spider.config.write(str(item) + '\n')

start = time.time()
spider.run(3)
print time.time() - start
