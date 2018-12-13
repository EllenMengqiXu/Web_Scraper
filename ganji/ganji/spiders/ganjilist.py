# -*- coding: utf-8 -*-
import scrapy
from ..items import GanjiItem

class GanjilistSpider(scrapy.Spider):
    name = 'ganjilist'
    allowed_domains = ['168ganji.com']
    start_urls = ['http://www.168ganji.com/cis/Recruitment/Index/rrm?pageNumber=1']

    def parse(self, response):
        rows = response.css('tr:not(:first-child)')
        for R in rows:
            title = R.css('.t::text').extract()
            url = R.css('.t::attr("href")').extract_first()
            item = GanjiItem()
            item['title'] = title
            item['url'] = response.urljoin(url)
            r = scrapy.Request(url=response.urljoin(url), callback=self.parseurl)
            r.meta['item'] = item
            yield r
        nextlink = response.css('.next-page a::attr(href)').extract_first()
        if nextlink:
            nextlinkurl = 'http://www.168ganji.com' + nextlink
            request = scrapy.Request(url = nextlinkurl)
            yield request

    def parseurl(self, response):
        item = response.meta['item']
        state = response.css('.span7 div:nth-child(2) ::text').extract()
        date = response.css('.span7 div:nth-child(5) ::text').extract()
        phone = response.css('.span7 div:nth-child(7) ::text').extract()
        item['state'] = state
        item['date'] = date
        item['phone'] = phone
        yield item
