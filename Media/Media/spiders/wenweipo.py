#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
#
# Copyright (c) 2016 Baidu.com, Inc. All Rights Reserved
#
########################################################################

"""
File: wenweipo.py
Author: mijianhong(mijianhong@baidu.com)
Date: 2016/08/01 20:58:17
func : 文汇网
"""
import md5
import urllib
import re
import time

import scrapy
from scrapy import signals
from scrapy.http import Request, FormRequest
from bs4 import BeautifulSoup

from .. import items
from .. import settings
from .. import sqlite_db

class WenweipoSpider(scrapy.Spider):
    name = "wenweipo"   # 爬虫名字
    allowed_domains = ["wenweipo.com"]
    start_urls = (
        '',
    )

    def __init__(self):   # 初始化参数
        self.Flag_List = []
        self.Maxpage_List = []
        self.MAX_PAGE_NUM = 10
        self.tt_pa = re.compile(r'.*?(\d+.*)')

    def start_requests(self):  # 爬虫启动请求链接 request 的启动函数
        for index, key_word in enumerate(settings.KEY_WORDS):
            self.Flag_List.append(True)
            self.Maxpage_List.append(self.MAX_PAGE_NUM)
            kw_quote =  urllib.quote(key_word.encode('utf-8'))
            url = 'http://so.wenweipo.com/search.php?q=' + kw_quote + '&artype=all&m=&f=_all&s=create_time_DESC&p=1'
            yield scrapy.Request(url,meta={'index':index})


    def parse(self, response):   # 解析第一层的title层

        index = response.meta['index']
        self.Maxpage_List[index] -= 1

        soup = BeautifulSoup(response.body_as_unicode(), "lxml")
        founds = soup.find_all('dl', class_='res_list')
        item_list = []
        for found in founds:
            item = items.PostItem()

            title = found.find('a').get_text().strip()
            url = found.find('a').get('href')
            m = md5.new()
            m.update(url)
            md_str = m.hexdigest()

            post_time = found.find('font').get_text().strip()
            post_time = re.findall(self.tt_pa, post_time)[0]
            print post_time

            item['url'] = url
            item['id'] = md_str
            item['post_time'] = post_time
            item['data_type'] = settings.DATA_TYPE
            item['site_id'] = settings.SITE_ID[self.name]
            item['scratch_time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            item_list.append(item)
        res_items = self.sqldb.get_newest_time(item_list)
        for item in res_items:
            yield Request(item['url'], callback=self.parse_content, meta={'item':item})

        if len(item_list) != len(res_items):
            self.Flag_List[index] = False

        if self.Flag_List[index] and self.Maxpage_List[index]>0:
            next_url = soup.find('a', class_='next').get('href')
            if not next_url.startswith('http:'):
                next_url = 'http://so.wenweipo.com' + next_url
            print next_url
            yield Request(next_url, meta={'index':index})

    def parse_content(self, response):   # 解析 进入具体页面的第二层
        item = response.meta['item']
        soup = BeautifulSoup(response.body_as_unicode(), "lxml")
        all_p = soup.find('div', id='main-content').find_all('p')
        content = ''
        for p in all_p:
            content += p.get_text().strip()
        item['content'] = content
        # print content

    @classmethod
    def from_crawler(cls, crawler):
        spider = cls()
        spider.crawler = crawler
        crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)  # 爬虫关闭触发 spider_closed 函数
        crawler.signals.connect(spider.spider_opened, signal=signals.spider_opened)  # 爬虫启动触发 spider_opened 函数
        return spider

    def spider_closed(self, spider):
        self.sqldb.insert_new_time()

    def spider_opened(self, spider):
        self.sqldb = sqlite_db.SqliteTime(spider.name)   # 这个类用限制时间方式来 防止爬过多曾经爬过的帖子

