# -*- coding: utf-8 -*-
########################################################################
#
# Copyright (c) 2016 Baidu.com, Inc. All Rights Reserved
#
########################################################################

"""
File: baidu.py
Author: yuanhao(yuanhao@baidu.com)
Date: 2016/08/15 20:32:30
func : 百度学术
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

class baiduSpider(scrapy.Spider):
    name = "baidu"
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
            url = 'http://xueshu.baidu.com/s?wd=' + kw_quote + '&pn=00&tn=SE_baiduxueshu_c1gjeupa&ie=utf-8&filter=sc_year%3D%7B2013%2C%2B%7D&sc_hit=1'
            yield scrapy.Request(url, meta={'index':index, 'url_':url}) #meta: 比较常用，在不同的请求之间传递数据使用的。字典dict型

    def parse(self, response):
        index = response.meta['index']
        url_ = response.meta['url_']
        self.Maxpage_List[index] += 1 #爬取页数加1

        soup = BeautifulSoup(response.body_as_unicode(), "lxml") #以浏览器的方式解析文档
        founds = soup.find('div', id = 'bdxs_result_lists').find_all('div', tpl="se_st_sc_default")
        item_list = []
        print '------------url---------------'
        for found in founds:
            item = items.PostItem()
            title = found.find('h3').get_text().strip()
            try:
                url = found.find('h3').find('a').get('href')
                url = 'http://xueshu.baidu.com' + url
            except:
                url = 'http://xueshu.baidu.com/s?wd=paperuri%3A%281bd3b04bde344c7986dcf12fbd76672f%29&filter=sc_long_sign&sc_ks_para=q%3D%E5%A2%83%E5%A4%96%E6%AF%92%E5%93%81%E9%97%AE%E9%A2%98%E5%AF%B9%E6%88%91%E5%9B%BD%E9%9D%9E%E4%BC%A0%E7%BB%9F%E5%AE%89%E5%85%A8%E7%9A%84%E5%BD%B1%E5%93%8D&sc_us=2780126511373565149&tn=SE_baiduxueshu_c1gjeupa&ie=utf-8'
            print title
            # print url
            m = md5.new()
            m.update(url)
            md_str = m.hexdigest() #MD5算法编码获得ID号
            
            try:
                post_time = found.find('div', class_ = 'sc_info').find_all('span')[2].get('data-year').strip()
                post_time = post_time + '-06-01 00:00:00'
            except:
                post_time = '2014-06-01 00:00:00'

            item['url'] = url
            item['id'] = md_str
            item['post_time'] = post_time
            item['data_type'] = settings.DATA_TYPE #学术期刊类都是 2
            item['site_id'] = settings.SITE_ID[self.name]
            item['topic_id'] = index
            item['scratch_time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            item['title'] = title
            item['poster_name'] = ''
            item['poster_id'] = ''
            item['poster_url'] = ''
            
            item_list.append(item)
            
        print '-----------------------------------'
        res_items = self.sqldb.get_newest_time(item_list) #判断这个链接是不是比上次爬取的要新，如果是就爬取
        
        # 调用parse_content解析每篇文章内容
        for item in res_items:
            yield Request(item['url'], callback = self.parse_content, meta = {'item':item}) 

        next_pages = soup.find('p', id = 'page').find_all('a')
        l = len(next_pages)
        try:
            next_page = next_pages[l - 1].get('href')
            next_page = 'http://xueshu.baidu.com' + next_page
            yield scrapy.Request(next_page, meta={'index':index, 'url_':next_page})
        except:
            print '------------------last page--------------------'
    
    def parse_content(self, response):
        item = response.meta['item']
        soup = BeautifulSoup(response.body_as_unicode(), "lxml")
        content = ''
        
        try:
            con = soup.find('div', class_ = 'abstract_wr').find_all('p')[1]
            authors = soup.find('p', class_ = 'author_text').find_all('a')
            if con:
                print '+++++++++  content is  ++++++++++'
                all_p = con.get_text().strip()
                content = all_p
                print all_p
            if authors:
                # print '--------  author is  -----------'
                item['poster_name'] = authors[0].get_text().strip()
                item['poster_url'] = authors[0].get('href')
                m = md5.new()
                m.update(item['poster_url'])
                item['poster_id'] = m.hexdigest()
                
        except:
            print '--------------------- fail to get content -------------------------'
        
        item['content'] = content
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