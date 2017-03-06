import scrapy
from tutorial.items import DmozItem

class DmozSpider(scrapy.Spider):
    name = 'dmoz'
    allowed_domains = ['dmoz.org']
    start_urls = [
        'http://www.dmoz.org/Computers/Programming/Languages/Python/Books',
        'http://www.dmoz.org/Computers/Programming/Languages/Python/Resources'
    ]
    
    def parse(self, response):
        a = response.xpath('//div[@class=\'title-and-desc\']/a/@href').extract()
        b = response.xpath('//div[@class=\'title-and-desc\']//div[@class=\'site-title\']/text()').extract()
        c = response.xpath('//div[@class=\'title-and-desc\']//div[@class=\'site-descr \']/text()').extract()
        
        for index in range(0, len(a)):
            item = DmozItem()
            item['link'] = a[index]
            item['title'] = b[index]
            item['desc'] = c[index].strip()
            yield item
            
    '''
    def parse(self, response):
        filename = response.url.split('/')[-1]
        with open(filename, 'wb') as f:
            f.write(response.body)
    '''