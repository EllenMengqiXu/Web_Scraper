# -*- coding: utf-8 -*-
import scrapy
from ..items import ChineserestaurantItem

class FirstpageSpider(scrapy.Spider):
    name = 'firstpage'
    allowed_domains = ['cgjss.com']
    start_urls = ['http://www.cgjss.com/ssql.php']

    def parse(self, response):
        rows = response.css('.n')
        for R in rows:
            title = R.css(".z1::text").extract()
            info = R.css(".k::text").extract()
            item = ChineserestaurantItem()
            item['title'] = title
            item['info'] = info
            yield item
