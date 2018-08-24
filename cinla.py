# -*- coding: utf-8 -*-
import scrapy
from ..items import ChineseinlaItem

class CinlaSpider(scrapy.Spider):
    name = 'cinla'
    allowed_domains = ['chineseinla.com']
    def start_requests(self):
        for i in range(73):
            yield self.make_requests_from_url("https://www.chineseinla.com/f/page_viewforum/f_132/topicdays_90/start_"+str(15*i)+".html")

    def parse(self, response):
        rows = response.css('.topic_list_detail')[0:16]
        for R in rows:
            title = R.css('.title::text').extract()
            url = R.css(".title::attr('href')").extract_first()
            date = R.css('.time::text').extract()
            item = ChineseinlaItem()
            item['title'] = title
            item['url'] = response.urljoin(url)
            item['date'] = date
            r = scrapy.Request(url=response.urljoin(url), callback=self.parseurl)
            r.meta['item'] = item
            yield r
        nextlink = response.css(".topic_option_right.pagination_right a:nth-child(8)::attr('href')").extract_first()
        if nextlink:
            nextlinkurl = 'https://www.chineseinla.com' + nextlink
            request = scrapy.Request(url = nextlinkurl)
            yield request

    def parseurl(self, response):
        item = response.meta['item']
        info = response.css('.real-content::text').re(r"\(?\d{3}[) -]?\d{3}[ -]?\d{4}")
        item['info'] = info
        yield item
