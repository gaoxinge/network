from scrapy.spiders import Spider

class MySpider(Spider):
    name = 'example.com'
    allowed_domains = ['example.com']
    start_urls = [
        'http://www.example.com/1.html',
        'http://www.example.com/2.html',
        'http://www.example.com/3.html'
    ]
    
    def parse(self, response):
        self.log('A response from %s just arrived!' % response.url)