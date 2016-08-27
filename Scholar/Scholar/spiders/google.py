# -*- coding: utf-8 -*-
########################################################################
#
# Copyright (c) 2016 Baidu.com, Inc. All Rights Reserved
#
########################################################################

"""
File: google.py
Author: yuanhao(yuanhao@baidu.com)
Date: 2016/08/18 10:15:10
func : 谷歌学术
"""
import md5
import time
import urllib
import re
import urllib2
import os
import requests

import scrapy
from scrapy.http import Request
from bs4 import BeautifulSoup
from scrapy import signals

from .. import items
from .. import settings
from .. import sqlite_db

class googleSpider(scrapy.Spider):
    name = "google"
    # allowed_domains = ["ld.search.gov.hk"]
    start_urls = ('')
    
    def __init__(self):
        self.sum = 0
        self.Flag_List = []
        self.Maxpage_List = []
        self.MAX_PAGE_NUM = 0
        self.tt_pa = re.compile(r'.*?(\d+.*)')
    
    def start_requests(self):
        for index, key_word in enumerate(settings.KEY_WORDS): # enumerate返回'元素下标'和'元素内容'
            self.Flag_List.append(True)
            self.Maxpage_List.append(self.MAX_PAGE_NUM)
            kw_quote =  urllib.quote(key_word.encode('utf-8')) #转关键字为utf-8编码传入链接中
            url = 'https://scholar.google.com/scholar?start=00&q=' + kw_quote + '&hl=zh-CN&as_sdt=0,5&as_ylo=2013'
            yield scrapy.Request(url, meta={'index':index, 'url_':url}) #meta: 比较常用，在不同的请求之间传递数据使用的。字典dict型

    def parse(self, response):
        index = response.meta['index']
        url_ = response.meta['url_']
        self.Maxpage_List[index] += 1 #爬取页数加1

        soup = BeautifulSoup(response.body_as_unicode(), "lxml") #以浏览器的方式解析文档
        founds = soup.find('div', id = 'gs_ccl').find_all('div', class_ = "gs_r")
        item_list = []
        print '------------url---------------'
        for found in founds:
            item = items.PostItem()
            title = found.find('h3').get_text().strip()
            try:
                url = found.find('h3').find('a').get('href')
            except:
                print '********* error url **********'
                url = 'http://www.cqvip.com/qk/96140x/201505/666377200.html'
            print title
            print url
            m = md5.new()
            m.update(url)
            md_str = m.hexdigest() #MD5算法编码获得ID号
            
            post_time = '2013'
            info = found.find('div', class_ = 'gs_a').get_text().strip()
            if '2013' in info:
                post_time = '2013'
            elif '2014' in info:
                post_time = '2014'
            elif '2015' in info:
                post_time = '2015'
            elif '2016' in info:
                post_time = '2016'
            post_time = post_time + '-06-01 00:00:00'
            print post_time
            
            author = info.split('-')[0]
            print author
            
            try:
                content = found.find('div', class_ = 'gs_rs').get_text().strip()
                # print content
            except:
                print '********* error content **********'
                content = ''

            item['url'] = url
            item['id'] = md_str
            item['post_time'] = post_time
            item['data_type'] = settings.DATA_TYPE #学术期刊类都是 2
            item['site_id'] = settings.SITE_ID[self.name]
            item['topic_id'] = index
            item['scratch_time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            item['title'] = title
            item['poster_name'] = author
            item['poster_id'] = ''
            item['poster_url'] = ''
            item['content'] = content
            
            item_list.append(item)
            
        print '-----------------------------------'
        res_items = self.sqldb.get_newest_time(item_list) #判断这个链接是不是比上次爬取的要新，如果是就爬取
        
        # 调用parse_content解析每篇文章内容
        for item in res_items:
            yield Request(item['url'], callback = self.parse_content, meta = {'item':item}) 
        
        next_pages = soup.find('div', id = 'gs_n').find_all('td')
        l = len(next_pages)
        try:
            next_page = next_pages[l - 1].find('a').get('href')
            next_page = 'https://scholar.google.com' + next_page
            yield scrapy.Request(next_page, meta={'index':index, 'url_':next_page})
        except:
            print '------------------last page--------------------'
    
    def parse_content(self, response):
        item = response.meta['item']
        return item
    
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