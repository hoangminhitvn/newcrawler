# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item


class CrawlerItem(Item):
    product_name = Field()
    product_url = Field()
    title = Field()
    post_date = Field()
    image_urls = Field()
    description = Field()
    categories = Field()
    tags = Field()
