from scrapy.spiders import Spider
from dirbot.items import Website

class DmozSpider(Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/",
    ]

    def parse(self, response):
        sites = response.css('#site-list-content > div.site-item > div.title-and-desc')
        items = []

        for site in sites:
            item = Website()
            item['name'] = site.css('a > div.site-title::text').extract_first().strip()
            item['url'] = site.xpath('a/@href').extract_first().strip()
            item['description'] = site.css('div.site-descr::text').extract_first().strip()
            items.append(item)

        return items