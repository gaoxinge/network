from scrapy.spiders import Spider
from scrapy.http import Request
from douban.items import DoubanItem

class DoubanSpider(Spider):
    name = 'doubanspider'
    allowed_domains = ['douban.com']
    
    def start_requests(self):
        return [Request('https://movie.douban.com/tag/2016?start=' + str(20*(i-1)), headers={'User-Agent': 'Mozilla/5.0'}) for i in range(1,500)]
        
    def parse(self, response):
        for result in response.xpath('//div[@class=\'pl2\']'):
            item = DoubanItem()
            item['title'] = result.xpath('a/text()')[0].extract()[:-2].strip().encode(response.encoding)
            item['rating'] = result.xpath('.//span[@class=\'rating_nums\']/text()')[0].extract().encode(response.encoding)
            item['vote'] = result.xpath('.//span[@class=\'pl\']/text()')[0].extract()[1:][:-4].encode(response.encoding)
            yield item