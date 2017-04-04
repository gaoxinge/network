from scrapy.spiders import Spider
from scrapy.http import Request
from stack.items import StackItem

class StackSpider(Spider):
    name = 'stackspider'
    allowed_domains = ['stackoverflow.com']
    
    def start_requests(self):
        return [Request('http://stackoverflow.com/questions/?page=' + str(i) + '&sort=votes', headers = {'User-Agent': 'Mozilla/5.0'}) for i in range(1,100)]
    
    def parse(self, response):
        for result in response.xpath('//div[@class=\'question-summary\']'):
            item = StackItem()
            item['votes'] = result.xpath('div[@class=\'statscontainer\']//strong/text()')[0].extract()
            item['answers'] = result.xpath('div[@class=\'statscontainer\']//strong/text()')[1].extract()
            item['views'] = result.xpath('div[@class=\'statscontainer\']/div[@class=\'views supernova\']/text()')[0].extract().strip()
            item['title'] = result.xpath('div[@class=\'summary\']/h3/a/text()')[0].extract()
            item['link'] = result.xpath('div[@class=\'summary\']/h3/a/@href')[0].extract()
            yield item