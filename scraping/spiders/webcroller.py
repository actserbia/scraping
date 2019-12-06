# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider


class LinkItem(scrapy.Item):
    url = scrapy.Field()
    referer = scrapy.Field()
    status = scrapy.Field()
    
    
class Webcroller(CrawlSpider):
    name = "webcroller"

    # allowed_domains = ["diwanee-serbia.rs"]
    # allowed_domains = ["diwanee.com"]
    # allowed_domains = ["spottertravel.com"]
    # allowed_domains = ["street.rs"]
    # allowed_domains = ["www.yasmina.com"]
    allowed_domains = ["test.street.rs"]

    # start_urls = ['http://www.diwanee-serbia.rs']
    # start_urls = ['https://www.diwanee.com/']
    # start_urls = ['https://www.spottertravel.com/']
    # start_urls = ['https://www.street.rs']
    # start_urls = ['https://www.yasmina.com']
    start_urls = ['http://test.street.rs']

    # handle_httpstatus_list = [404]
    # handle_httpstatus_all = True
    custom_settings = {'HTTPERROR_ALLOW_ALL': True}
    
    rules = (
        Rule(
            LinkExtractor(), 
            callback='parse_item', 
            follow=True
        ),
    )

    def parse_item(self, response):
        # if response.status == 404:
            link = LinkItem()

            link['url'] = response.url
            link['status'] = response.status
            link['referer'] = response.request.headers.get('Referer')

            return link
