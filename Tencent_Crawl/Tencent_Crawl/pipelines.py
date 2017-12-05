# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from Tencent_Crawl.With_DB import Mysql_DB

class TencentCrawlPipeline(object):
    def __init__(self):
        self.db = Mysql_DB()

    def process_item(self, item, spider):
        try:
            sql = """insert into Tencent_Comment (Tid, Uid, Uname, Ctime, Cid, Content, Liked, Reply, City, Parent) VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")"""%(item["Tid"].encode('utf-8', 'ignore'), item["Uid"].encode('utf-8', 'ignore'), item["Uname"].encode('utf-8', 'ignore'), item["Ctime"].encode('utf-8', 'ignore'), item["Cid"].encode('utf-8', 'ignore'), item["Content"].encode('utf-8', 'ignore'), item["Liked"].encode('utf-8', 'ignore'), item["Reply"].encode('utf-8', 'ignore'), item["City"].encode('utf-8', 'ignore'), item["Parent"].encode('utf-8', 'ignore'))
            self.db.Insert_MySQL(sql)
        except Exception as e:
            print '插入MySQL数据库错误' + str(e)
