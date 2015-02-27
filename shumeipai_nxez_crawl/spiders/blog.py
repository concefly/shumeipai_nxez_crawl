# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

class BlogSpider(CrawlSpider):
    name = "blog"
    # allowed_domains 最好不加 http
    allowed_domains = ["shumeipai.nxez.com"]
    start_urls = (
        'http://shumeipai.nxez.com/',
    )

    rules = (
    	Rule(LinkExtractor(
    			allow=("page/\d*$"),
    			allow_domains=("shumeipai.nxez.com")
    			),
    		follow=True),
    	Rule(LinkExtractor(
    			allow=("\d*/\d*/\d*/(.*)\.html$"),
    			allow_domains=("shumeipai.nxez.com")
    			),
    		callback='parse_item'),
    )

    def parse_item(self,response):
    	title = response.xpath('//header/h1/text()').extract()[0]
    	self.log(title)

