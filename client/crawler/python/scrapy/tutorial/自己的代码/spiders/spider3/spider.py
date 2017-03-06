import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class MySpider(CrawlSpider):
    name = 'baidu.com'
    allowed_domains = ['baidu.com']
    start_urls = ['https://www.baidu.com']
    rules = [Rule(LinkExtractor(allow=['\S+']), callback='parse_item')]

    def parse_item(self, response):
        self.log('%s' % response.url)
        #pass