# -*- coding: utf-8 -*-
########################################################################
#
# Copyright (c) 2016 Baidu.com, Inc. All Rights Reserved
#
########################################################################

"""
File: ifeng.py
Author: mijianhong(mijianhong@baidu.com)
Date: 2016/08/01 20:58:17
func : 凤凰网
"""
import md5
import time
import urllib
import re

import scrapy
from scrapy.http import Request
from bs4 import BeautifulSoup
from scrapy import signals

from .. import items
from .. import settings
from .. import sqlite_db

class IfengSpider(scrapy.Spider):
    name = "ifeng"
    allowed_domains = ["ifeng.com"]
    start_urls = (
        'http://www.ifeng.com/',
    )
    def __init__(self):
        self.Flag_List = []
        self.Maxpage_List = []
        self.MAX_PAGE_NUM = 10
        self.tt_pa = re.compile(r'.*?(\d+.*)')

    def start_requests(self):
        for index, key_word in enumerate(settings.KEY_WORDS): # enumerate返回'元素下标'和'元素内容'
            self.Flag_List.append(True)
            self.Maxpage_List.append(self.MAX_PAGE_NUM)
            kw_quote =  urllib.quote(key_word.encode('utf-8')) #转关键字为utf-8编码传入链接中
            url = 'http://search.ifeng.com/sofeng/search.action?q=' + kw_quote + '&c=1&p=1'
            yield scrapy.Request(url, meta={'index':index, 'url_':url}) #meta: 比较常用，在不同的请求之间传递数据使用的。字典dict型

    def parse(self, response):
        index = response.meta['index']
        url_ = response.meta['url_']
        self.Maxpage_List[index] -= 1 #爬取页数减1

        soup = BeautifulSoup(response.body_as_unicode(), "lxml") #以浏览器的方式解析文档
        founds = soup.find_all('div', class_='searchResults')
        item_list = []
        for found in founds:
            item = items.PostItem()
            title = found.find('a').get_text().strip()
            url = found.find('a').get('href')
            print title, url
            m = md5.new() #MD5是最常见的摘要算法，又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）。
            m.update(url)
            md_str = m.hexdigest() #MD5算法编码获得ID号

            post_time = found.find_all('font')[-1].get_text().strip()
            post_time = re.findall(self.tt_pa, post_time)[0] #正则匹配得到时间
            print post_time

            item['url'] = url
            item['id'] = md_str
            item['post_time'] = post_time
            item['data_type'] = settings.DATA_TYPE #媒体类都是0
            item['site_id'] = settings.SITE_ID[self.name]
            item['scratch_time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) #time.strftime()可以用来获得当前时间，可以将时间格式化为字符串等等

            item_list.append(item)

        res_items = self.sqldb.get_newest_time(item_list)
        for item in res_items:
            yield Request(item['url'], callback = self.parse_content, meta = {'item':item}) #调用parse_content解析每篇文章内容
        if len(item_list) != len(res_items):
            self.Flag_List[index] = False

        if self.Flag_List[index] and self.Maxpage_List[index]>0:
            page_num = self.MAX_PAGE_NUM - self.Maxpage_List[index] + 1 #获得下面需要爬取的页面号
            next_url = url_[:-1] + str(page_num) # 得到下一个页面的网址链接
            print next_url
            yield Request(next_url, meta={'index':index, 'url_':url_})

    def parse_content(self, response):
        item = response.meta['item']
        soup = BeautifulSoup(response.body_as_unicode(), "lxml")
        all_p = soup.find_all('p')
        content = ''
        for p in all_p:
            content += p.get_text().strip()
        # print content
        item['content'] = content

    @classmethod
    def from_crawler(cls, crawler):
        spider = cls()
        spider.crawler = crawler
        crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
        crawler.signals.connect(spider.spider_opened, signal=signals.spider_opened)
        return spider

    def spider_closed(self, spider):
        self.sqldb.insert_new_time()

    def spider_opened(self, spider):
        self.sqldb = sqlite_db.SqliteTime(spider.name)
