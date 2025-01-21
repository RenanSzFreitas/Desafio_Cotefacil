# See documentation in: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class Questao2Pipeline:
    def process_item(self, item, spider):
        return item