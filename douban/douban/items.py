# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    url = scrapy.Field()
    rating = scrapy.Field()
    counts = scrapy.Field()
    quote = scrapy.Field()
    genre= scrapy.Field()
    rank = scrapy.Field()
    director = scrapy.Field()
    runtime = scrapy.Field()

