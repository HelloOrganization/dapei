# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TmallItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    trade_num = scrapy.Field()
    src_url = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
class MogujieItem(TmallItem):
    pass
class QudapeiShortItem(scrapy.Item):
    title = scrapy.Field()
    src_url = scrapy.Field()
    short_dscr = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
    descriptions = scrapy.Field() 
    para = scrapy.Field()
    
