# -*- coding: utf-8 -*-

from scrapy_redis.spiders import RedisSpider
from Tencent_Crawl.With_DB import Redis_DB
from Tencent_Crawl.items import TencentCrawlItem
import json
import time

class Tencent_Spider(RedisSpider):
    name = 'TencentSpider'
    redis_key = 'Tencent_urls'

    def parse(self, response):
        json_read = json.loads(response.body)
        try:
            last = json_read['data']['last'] #本次评论的尾部，用于组成url
            Tid = json_read['data']['targetid']
            for comment in json_read['data']['oriCommList']:
                item = TencentCrawlItem()
                item['Tid'] = str(Tid)
                item['Cid'] = str(comment['id'])
                item['Ctime'] = str(time.strftime('%Y-%m-%d %H:%M', (time.localtime(float(comment['time'])))))
                item['Content'] = comment['content']
                item['Liked'] = str(comment['up'])
                item['Reply'] = str(comment['orireplynum'])
                item['Uid'] = str(comment['userid'])
                item['Uname'] = json_read['data']['userList'][item['Uid']]['nick']
                item['City'] = json_read['data']['userList'][item['Uid']]['region']
                item['Parent'] = str(comment['parent'])
                yield item
        except Exception as e:
            print 'comment错误' + str(e)
        try:
            for repcomment in json_read['data']['repCommList']: #评论的回复
                a = json_read['data']['repCommList'][repcomment]
                for b in a:
                    item = TencentCrawlItem()
                    item['Tid'] = str(Tid)
                    item['Cid'] = str(b['rootid'])
                    item['Ctime'] = str(time.strftime('%Y-%m-%d %H:%M', (time.localtime(float(b['time'])))))
                    item['Content'] = b['content']
                    item['Liked'] = str(b['up'])
                    item['Reply'] = str(b['orireplynum'])
                    item['Uid'] = str(b['userid'])
                    item['Uname'] = json_read['data']['userList'][item['Uid']]['nick']
                    item['City'] = json_read['data']['userList'][item['Uid']]['region']
                    item['Parent'] = str(b['parent'])
                    yield item
        except Exception as e:
            print 'repcomment错误' + str(e)
        try:
            if json_read['data']['oriretnum'] != 0: #说明还没到底
                next_url = 'http://coral.qq.com/article/%s/comment/v2?callback=0&orinum=30&oriorder=o&pageflag=1&cursor=%s&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=1&_='%(Tid, last)
                r5 = Redis_DB(0) #放db5里
                r5.Insert_Redis('Tencent_urls', next_url)
        except Exception as e:
            print '插入Redis错误' + str(e)












