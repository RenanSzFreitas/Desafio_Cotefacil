# See documentation in:https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CompraAgoraProdutoItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    manufacter = scrapy.Field()
    barcode = scrapy.Field()
    image_url = scrapy.Field()