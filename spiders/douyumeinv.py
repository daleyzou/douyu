# -*- coding: utf-8 -*-
import scrapy
import json
# noinspection PyUnresolvedReferences
from douyu.items import DouyuItem


class DouyumeinvSpider(scrapy.Spider):
    name = 'douyumeinv'
    allowed_domains = ['capi.douyucdn.cn']
    offset = 0
    url = 'http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset='
    start_urls = [url + str(offset)]

    def parse(self, response):
        # 把json格式的数据转换为Python格式，data是列表
        data = json.loads(response.text)['data']
        for each in data:
            item = DouyuItem()
            item['nickname'] = each['nickname']
            item['imageLink'] = each['vertical_src']

            yield item
        self.offset += 20
        # yield scrapy.Request(self.url + str(self.offset), callback = self.parse)
