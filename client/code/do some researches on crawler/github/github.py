import requests
from lxml import etree
from collections import defaultdict

seen = set(['https://github.com/gaoxinge?tab=following'])
urls = ['https://github.com/gaoxinge?tab=following']
d = defaultdict(list)

def filter(url):
    if url not in seen:
        seen.add(url)
        urls.append(url)

def http(url):
    response = requests.get(url)
    return response
    
def parse(response):
    root = etree.HTML(response.text)
    results = root.xpath('//span[@class=\'link-gray pl-1\']/text()')
    for result in results:
        tmp = 'https://github.com/' + result + '?tab=following'
        filter(tmp)
        yield result

def save(item):
    the = url[19:][:-14]
    d[the].append(item)
    
def http_parse_save(url):
    response = http(url)
    items = parse(response)
    for item in items:
        save(item)

while True:
    if urls and len(seen) < 100:
        url = urls.pop(0)
        http_parse_save(url)
    else:
        break

print d