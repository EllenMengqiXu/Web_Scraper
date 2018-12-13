# -*- coding: utf-8 -*-
import scrapy
from ..items import ChineserestaurantItem

class CrlistSpider(scrapy.Spider):
    name = 'crlist'
    allowed_domains = ['cgjss.com']
    def start_requests(self):
        for i in range(25):
            yield self.make_requests_from_url("http://www.cgjss.com/ssql.php?1=1&page="+str(i)+"")

    def parse(self, response):
        rows = response.css('.n')
        for R in rows:
            title = R.css(".z1::text").extract()
            info = R.css(".k::text").extract()
            item = ChineserestaurantItem()
            item['title'] = title
            item['info'] = info
            yield item
            



