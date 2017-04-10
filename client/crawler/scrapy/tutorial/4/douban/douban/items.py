import scrapy

class DoubanItem(scrapy.Item):
    title = scrapy.Field()
    rating = scrapy.Field()
    vote = scrapy.Field()