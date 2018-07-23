# -*- coding: utf-8 -*-
import scrapy
from ..items import YelpItem

class YelplistSpider(scrapy.Spider):
    name = 'yelplist'
    allowed_domains = ['yelp.com']
    start_urls = ['https://www.yelp.com/search?find_desc=Chinese+Restaurant&find_loc=Boston,+MA']

    def parse(self, response):
        cafes = response.css('.biz-listing-large')
        for c in cafes:
            url = c.css(".biz-name.js-analytics-click::attr('href')").extract()
            title = c.css("a.biz-name.js-analytics-click > span::text").extract()
            region = c.css(".neighborhood-str-list::text").extract()
            address = c.css("address::text").extract()
            phone = c.css('.biz-phone::text').extract()
            item = YelpItem()
            item['url'] = url
            item['title'] = title
            item['region'] = region
            item['address'] = address
            item['phone'] = phone
            yield item
        
        nextlink = response.css(".u-decoration-none.next.pagination-links_anchor::attr('href')").extract_first()
        if nextlink:
            nextlinkurl = 'https://www.yelp.com' + nextlink
            request = scrapy.Request(url = nextlinkurl)
            yield request
      
            
        
