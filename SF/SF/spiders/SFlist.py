# -*- coding: utf-8 -*-
import scrapy
from ..items import SfItem

class SflistSpider(scrapy.Spider):
    name = 'SFlist'
    allowed_domains = ['sf.meimin.us']
    def start_requests(self):
        for i in range(11):
            yield self.make_requests_from_url("http://sf.meimin.us/waiter-page-"+str(i)+"/")

    def parse(self, response):
        rows=response.css('ul')[1:21]
        for R in rows:
            title = R.css("li a::text").extract()
            url = R.css("li a::attr('href')").extract_first()
            date = R.css(".li4::text").extract()
            item = SfItem()
            item['title'] = title
            item['url'] = response.urljoin(url)
            item['date'] = date
            r = scrapy.Request(url=response.urljoin(url), callback=self.parseurl)
            r.meta['item'] = item
            yield r
            
    def parseurl(self, response):
        item = response.meta['item']
        phone = response.css('.content p::text').extract()
        item['phone'] = phone
        yield item
