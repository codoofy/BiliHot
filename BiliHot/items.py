# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BilihotItem(scrapy.Item):
    # define the fields for your item here like:
    bvid = scrapy.Field()  # 视频id
    title = scrapy.Field()  # 视频标题
    # upid = scrapy.Field()  # up主id
    upname = scrapy.Field()  # up主名称
    week = scrapy.Field()  # 视频上榜周次
    week_time = scrapy.Field()  # 视频上榜周次日期
    video_time = scrapy.Field()  # 视频上线日期
    play_count = scrapy.Field()  # 视频播放量
    dm_count = scrapy.Field()  # 视频弹幕数
    like_count = scrapy.Field()  # 视频点赞数
    coin_count = scrapy.Field()  # 视频投币数
    collect_count = scrapy.Field()  # 视频收藏数
    share_count = scrapy.Field()  # 视频转发数
    v_tags = scrapy.Field()  # 视频标签
    # comm_count = scrapy.Field()  # 视频评论数
    # pass
