import scrapy

class StackItem(scrapy.Item):
    votes = scrapy.Field()
    answers = scrapy.Field()
    views = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()