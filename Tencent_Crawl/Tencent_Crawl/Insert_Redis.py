# -*- coding: utf-8 -*-

from With_DB import Redis_DB

def a():
    r5 = Redis_DB(0)
    Tid_list = [2197101878, 2207108488, 2221966030, 2234692048, 2248865625, 2265484094] #按顺序排，1-6期
    for i in Tid_list:
        url = 'http://coral.qq.com/article/%s/comment/v2?callback=0&orinum=30&oriorder=o&pageflag=1&cursor=0&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=1&_='%(str(i))
        r5.Insert_Redis('Tencent_urls', url)
    print '初始队列插入完毕'

aa = a()
aa