# -*- coding: utf-8 -*-
import scrapy
from ..items import Yelp2Item

class YelplistSpider(scrapy.Spider):
    name = 'yelp2list'
    allowed_domains = ['yelp.com']
    start_urls = ['https://www.yelp.com/search?find_desc=Vietnamese+Restaurant&find_loc=stamford,CT']

    def parse(self, response):
        cafes = response.css('.biz-listing-large')
        for c in cafes:
            url = c.css(".biz-name.js-analytics-click::attr('href')").extract_first()
            Title = c.css("a.biz-name.js-analytics-click > span::text").extract_first()
            title=Title.strip()
            Address = c.css("address::text").extract_first()
            address=Address.strip()
            Phone = c.css('.biz-phone::text').extract_first()
            phone=Phone.strip()
            item = Yelp2Item()
            item['url'] = response.urljoin(url)
            item['title'] = title
            item['address'] = address
            item['phone'] = phone
            r = scrapy.Request(url=response.urljoin(url), callback=self.parseurl)
            r.meta['item'] = item
            yield r
            
        nextlink = response.css(".u-decoration-none.next.pagination-links_anchor::attr('href')").extract_first()
        if nextlink:
            nextlinkurl = 'https://www.yelp.com' + nextlink
            request = scrapy.Request(url = nextlinkurl)
            yield request
            
    def parseurl(self, response):
        item = response.meta['item']
        Info1 = response.xpath('//*[@id="wrap"]/div[2]/div/div[1]/div/div[4]/div[1]/div/div[2]/ul/li[1]/div/strong/address/text()[1]').extract_first()
        info1=Info1.strip()
        Info2 = response.xpath('//*[@id="wrap"]/div[2]/div/div[1]/div/div[4]/div[1]/div/div[2]/ul/li[1]/div/strong/address/text()[2]').extract_first()
        info2 = Info2.strip()
        item['info1'] = info1
        item['info2'] = info2
        yield item
