# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GenoticiasItem(scrapy.Item):
    # define the fields for your item here like:
    titulo = scrapy.Field()
    link = scrapy.Field()
    autor = scrapy.Field()
    subtitulo = scrapy.Field()
    publicacao = scrapy.Field()
