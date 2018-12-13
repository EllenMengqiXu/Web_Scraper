# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Yelp2Item(scrapy.Item):
    # define the fields for your item here like:
    
    url = scrapy.Field()
    title = scrapy.Field()
    address = scrapy.Field()
    phone = scrapy.Field()
    info1 = scrapy.Field()
    info2 = scrapy.Field()