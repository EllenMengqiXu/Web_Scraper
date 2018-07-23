# -*- coding: utf-8 -*-
import scrapy
from ..items import ChineserestaurantItem

class CrlistSpider(scrapy.Spider):
    name = 'crlist'
    allowed_domains = ['cgjss.com']
    start_urls = ['http://www.cgjss.com/ssql.php?1=1&page=2/']

    def parse(self, response):
        rows = response.css('.n')
        for R in rows:
            title = R.css(".z1::text").extract()
            info = R.css(".k::text").extract()
            item = ChineserestaurantItem()
            item['title'] = title
            item['info'] = info
            yield item
            
        nextlink = response.css('a[href*="page"]::attr(href)')[2].extract()
        if nextlink:
            nextlinkurl = 'http://www.cgjss.com/ssql.php' + nextlink
            request = scrapy.Request(url = nextlinkurl)
            yield request


