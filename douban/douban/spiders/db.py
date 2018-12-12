# -*- coding: utf-8 -*-
import scrapy
from ..items import DoubanItem

class DbSpider(scrapy.Spider):
    name = 'db'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
    	movies =response.css('.item')
    	for m in movies:
    		title = m.css(".title::text").extract_first().strip()
    		url = m.css('.hd a::attr(href)').extract_first()
    		genre = m.xpath('div[@class="info"]/div[@class="bd"]/p/text()[2]').extract_first().strip()
    		rank = m.css('div[class="pic"] em::text').extract_first()
    		rating = m.css(".rating_num::text").extract_first().strip()
    		counts = m.xpath("div[@class='info']/div[@class='bd']/div[@class='star']/span[4]/text()").extract_first().strip()
    		quote = m.xpath("div[@class='info']/div[@class='bd']/p[@class='quote']/span/text()").extract_first().strip()
    		item = DoubanItem()
    		item['title'] = title
    		item['url'] = response.urljoin(url)
    		item['genre'] = genre
    		item['rank'] = rank
    		item['rating'] = rating
    		item['counts'] = counts
    		item['quote'] = quote
    		r = scrapy.Request(url=response.urljoin(url), callback=self.parseurl)
    		r.meta['item'] = item
    		yield r

    	nextlink = response.css('.next a::attr(href)').extract_first()
    	if nextlink:
    		nextlinkurl = 'https://movie.douban.com/top250' + nextlink
    		request = scrapy.Request(url = nextlinkurl)
    		yield request

    def parseurl(self, response):
    	item = response.meta['item']
    	director = response.xpath('//*[@id="info"]/span[1]/span[2]/a/text()').extract_first().strip()
    	runtime = response.css('span[property="v:runtime"]::text').extract_first()
    	item["director"] = director
    	item["runtime"] = runtime
    	yield item
    		

