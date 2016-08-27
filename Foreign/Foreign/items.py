# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ForeignItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class PostItem(scrapy.Item):
    id = scrapy.Field()
    url = scrapy.Field()
    site_id = scrapy.Field()
    data_type = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    post_time = scrapy.Field()
    scratch_time = scrapy.Field()
    poster_name = scrapy.Field()
    poster_id = scrapy.Field()
    poster_url = scrapy.Field()
    topic_id = scrapy.Field()