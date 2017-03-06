# -*- coding: utf-8 -*-
import scrapy


class Example1Spider(scrapy.Spider):
    name = "example1"
    allowed_domains = ["example.com"]
    start_urls = ['http://example.com/']

    def parse(self, response):
        pass
