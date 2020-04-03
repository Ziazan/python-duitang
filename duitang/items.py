# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DuiTangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # title = scrapy.Field()
    # link = scrapy.Field()
    # img_src = scrapy.Field()
    url = scrapy.Field()
    card_list = scrapy.Field()
    #启用图片下载，用到了这两个
    image_urls = scrapy.Field()
    images = scrapy.Field()
    # 生成的图路径
    image_paths = scrapy.Field()
    pass
