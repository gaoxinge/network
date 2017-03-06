# -*- coding: utf-8 -*-
import scrapy


class Example2Spider(scrapy.Spider):
    name = "example2"
    allowed_domains = ["example.com"]
    start_urls = ['http://example.com/']

    def parse(self, response):
        pass
