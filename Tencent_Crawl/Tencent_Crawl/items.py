# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentCrawlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Tid = scrapy.Field() #本期id
    Uid = scrapy.Field() #用户id
    Uname = scrapy.Field() #用户名
    Ctime = scrapy.Field() #评论时间
    Cid = scrapy.Field() #评论id
    Content = scrapy.Field() #内容
    Liked = scrapy.Field() #点赞
    Reply = scrapy.Field() #本条评论的回复数
    City = scrapy.Field() #定位点
    Parent = scrapy.Field() #属于哪个评论的回复，没有为0

