import time
import requests
from lxml import etree
from collections import defaultdict

seen = set(['gaoxinge'])
queue = ['gaoxinge']
d = defaultdict(list)

def fetcher(one):
    print ('[%s] fetcher start: ' + one) % time.ctime()
    response = requests.get('https://github.com/' + one + '?tab=following')
    print ('[%s] fercher end:' + one) % time.ctime()
    parser(one, response)
    
def parser(one, response):
    print ('[%s] parser start: ' + one) % time.ctime()
    root = etree.HTML(response.text)
    others = root.xpath('//span[@class=\'link-gray pl-1\']/text()')
    
    for other in others:
        saver(one, other)
        if other not in seen:
            seen.add(other)
            queue.append(other)
    print ('[%s] parser end: ' + one) % time.ctime()

def saver(one, other):
    d[one].append(other)

def main():
    while len(queue) and len(seen) < 1000:
        one = queue.pop(0)
        fetcher(one)

    with open('gitfollow.txt', 'w') as f:
        for key in d:
            for value in d[key]:
                f.write(key + '---' + value + '\n')
                
if __name__ == '__main__':
    main()
