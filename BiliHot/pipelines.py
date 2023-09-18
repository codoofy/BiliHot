# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BilihotPipeline:
    def process_item(self, item, spider):
        line_str = item['bvid'] + ',' + \
                   item['title'] + ',' + \
                   item['upname'] + ',' + \
                   item['video_time'] + ',' + \
                   item['play_count'] + ',' + \
                   item['dm_count'] + ',' + \
                   item['like_count'] + ',' + \
                   item['coin_count'] + ',' + \
                   item['collect_count'] + ',' + \
                   item['share_count'] + ',' + \
                   item['v_tags'] + ',' + \
                   item['week'] + ',' + \
                   item['week_time']

        with open('./data.csv', 'a', encoding='utf-8-sig') as f:
            f.write(line_str + '\n')
# print(item)
# return item
