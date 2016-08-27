# -*- coding: utf-8 -*-
########################################################################
#
# Copyright (c) 2016 Baidu.com, Inc. All Rights Reserved
#
########################################################################

"""
 File: takungpao.py
 Author: mijianhong(mijianhong@baidu.com)
 Date: 2016/08/01 20:58:17
 func : 大公网
 """
import md5
import time

import scrapy
from scrapy.http import Request, FormRequest
from bs4 import BeautifulSoup
from scrapy import signals

from .. import items
from .. import settings
from .. import sqlite_db

class TakungpaoSpider(scrapy.Spider):
    name = "takungpao"
    # allowed_domains = ["takungpao.com"]
    start_urls = (
        'http://search.takungpao.com',
    )
    def __init__(self):
        pass
    headers = {
        'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding' : 'gzip, deflate',
        'Accept-Language' : 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Connection' : 'keep-alive',
        'Host' : 'search.takungpao.com',
        'Referer' : 'http://search.takungpao.com/',
        'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:47.0) Gecko/20100101 Firefox/47.0',
    }
    headers_ = {
        'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding' : 'gzip, deflate',
        'Accept-Language' : 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Cache-Control' : 'max-age=0',
        'Connection' : 'keep-alive',
        'Host' : 'photo.takungpao.com',
        'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:47.0) Gecko/20100101 Firefox/47.0'
    }
    # headers 用于模拟浏览器行为，常见的解决反扒机制的方法之一

    def start_requests(self):
        for key_word in settings.KEY_WORDS:
            yield Request('http://search.takungpao.com',
                            meta={'kw':key_word},
                            callback=self.post_login,
                            dont_filter=True)

    def post_login(self, response):   # 由于每次搜索都是通过post 方式进行请求拿到，所以模拟post参数
        key_word = response.meta['kw']
        yield FormRequest.from_response(response,
                                          headers=self.headers,
                                          formdata={
                                            'dosubmit':'',
                                            'search':key_word,
                                          },
                                          callback=self.after_login,
                                          dont_filter=True,
                                          )

    def after_login(self, response):  #  解析第一层
        soup = BeautifulSoup(response.body_as_unicode(), "lxml")
        founds = soup.find('div', class_='seachList').find_all('li', class_='clearfix')
        print len(founds)
        for found in founds:
            item = items.PostItem()
            url = found.find('a').get('href').strip()
            m = md5.new()
            m.update(url)
            md_str = m.hexdigest()
            print md_str
            item['id'] = md_str
            item['url'] = url
            item['site_id'] = settings.SITE_ID[self.name]
            item['data_type'] = settings.DATA_TYPE

            title = found.find('a').get_text().strip()
            print title
            item['title'] = title

            item['content'] = ''
            item['scratch_time'] = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())

            yield Request(url, headers=self.headers_, callback=self.parse_content, meta={'item':item})

    def parse_content(self, response):  # 解析第二层
        item = response.meta['item']
        soup = BeautifulSoup(response.body_as_unicode(), "lxml")
        founds = soup.find('div', class_='content_info').find('div', class_='fl_dib')
        post_time = founds.get_text()[:20].strip()
        item['post_time'] = post_time
        print post_time
        if self.sqldb.get_newest_time_item(item):
            print '++++++++++++++++'

    @classmethod
    def from_crawler(cls, crawler):
        spider = cls()
        spider.crawler = crawler
        crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
        crawler.signals.connect(spider.spider_opened, signal=signals.spider_opened)
        return spider

    def spider_closed(self,spider):
        self.sqldb.insert_new_time()

    def spider_opened(self,spider):
        self.sqldb = sqlite_db.SqliteTime(spider.name)
