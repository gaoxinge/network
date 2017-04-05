import requests
from lxml import etree
import threading
from Item import Item
import time

def http(url):
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    return response

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

def store(item):
    f.write(str(item) + '\n')

def http_parse_store(url):
    response = http(url)
    items = parse(response)
    for item in items:
        store(item)    
    
urls = ['https://movie.douban.com/tag/2016?start=' + str((i-1)*20) for i in range(1, 10)]
f = open('douban.txt', 'w')
threads = []
lock = threading.Lock()
start = time.time()

while True:
    if urls:
        lock.acquire()
        url = urls.pop(0)
        thread = threading.Thread(target=http_parse_store, args=(url,))
        threads.append(thread)
        lock.release()
        thread.start()
        thread.join()
    else:
        lock.acquire()
        for _ in threads:
            if not _.is_alive():
                threads.remove(_)
        if not threads:
            break
        lock.release()

print time.time() - start
f.close()
