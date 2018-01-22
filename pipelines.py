# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
import os
from scrapy.utils.project import get_project_settings
from scrapy.pipelines.images import ImagesPipeline


class ImagesPipeline(ImagesPipeline):
    # def process_item(self, item, spider):
    #     return item
    #
    # 获取settings文件中设置的变量值
    IMAGES_STORE = get_project_settings().get("IMAGES_STORE")

    # 发起下载文件的请求
    def get_media_requests(self, item, info):
        image_url = item['imageLink']
        yield scrapy.Request(image_url)

    #
    def item_completed(self, results, item, info):
        if isinstance(item, dict) or self.images_result_field in item.fields:
            item[self.images_result_field] = [x for ok, x in results if ok]
        # return item
        image_path = [x['path'] for ok, x in results if ok]
        os.rename(self.IMAGES_STORE + "\\" + image_path[0], \
                  self.IMAGES_STORE + "\\" + item['nickname'] + '.jpg')
        item['imagePath'] = self.IMAGES_STORE + "\\" + item['nickname']
        return item