from scrapy.spiders import Spider
from spider1.items import MyItem

class MySpider(Spider):
    name = 'example.com'
    allowed_domains = ['example.com']
    start_urls = [
        'http://www.example.com/1.html',
        'http://www.example.com/2.html',
        'http://www.example.com/3.html'
    ]
    
    def parse(self, response):
        for h3 in response.xpath('//h3').extract():
            yield MyItem(title=h3)
            
        for url in response.xpath('//a/@href').extract():
            yield scrapy.Request(url, callback=self.parse)