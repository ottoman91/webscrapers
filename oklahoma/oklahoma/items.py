# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class OklahomaItem(scrapy.Item):
    name = scrapy.Field()
    description = scrapy.Field()
    csv_link = scrapy.Field()
    xml_link = scrapy.Field()
    json_link = scrapy.Field() 
    rdf_link = scrapy.Field()



