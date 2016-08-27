# -*- coding: utf-8 -*-
########################################################################
#
# Copyright (c) 2016 Baidu.com, Inc. All Rights Reserved
#
########################################################################

"""
File: UNODC.py
Author: yuanhao(yuanhao@baidu.com)
Date: 2016/08/23 20:58:20
func : National Institute on Drug Abuse
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

class UNODCSpider(scrapy.Spider):
    name = "UNODC"
    # allowed_domains = ["ld.search.gov.hk"]
    start_urls = (
        '',
    )
    def __init__(self):
        self.sum = 0
        self.tt_pa = re.compile(r'.*?(\d+.*)')

    def start_requests(self):
        for index, key_word in settings.KEY_WORDS.items(): # enumerate返回'元素下标'和'元素内容'
            kw_quote =  urllib.quote(key_word.encode('utf-8')) #转关键字为utf-8编码传入链接中
            # url = 'https://search.usa.gov/search?affiliate=www.drugabuse.gov&commit=Search&m=&page=1&query=' + kw_quote + '&sc=0&utf8=%E2%9C%93'
            url = 'https://www.unodc.org/unodc/search.html?site=unodc&proxyreload=1&q=' + kw_quote + '&sort=date:D:L:d1&entqr=0&entqrm=0&ud=1&start=0'
            yield scrapy.Request(url, meta={'index':index, 'url_':url}) #meta: 比较常用，在不同的请求之间传递数据使用的。字典dict型

    def parse(self, response):
        index = response.meta['index']
        url_ = response.meta['url_']

        soup = BeautifulSoup(response.body_as_unicode(), "lxml") #以浏览器的方式解析文档
        founds = soup.find('div', id='contentWrapper').find_all('div', class_='gooResult')
        item_list = []
        print '------------url---------------'
        for found in founds:
            item = items.PostItem()
            title = found.find('div', class_='gooResultURL').get_text().strip()
            url = found.find('div', class_='gooResultURL').find('a').get('href')
            # print title
            print url
            m = md5.new()
            m.update(url)
            md_str = m.hexdigest() #MD5算法编码获得ID号

            post_time = found.find('div', class_='gooResMisc').get_text().strip()
            post_time = post_time.split('- ')
            if len(post_time) == 3:
                post_time = post_time[2] + " 00:00:00"
            else:
                post_time = '2013-06-01 00:00:00'
            
            item['url'] = url
            item['id'] = md_str
            item['post_time'] = post_time
            item['data_type'] = settings.DATA_TYPE #英文网站类都是4
            item['site_id'] = settings.SITE_ID[self.name]
            item['topic_id'] = index
            item['scratch_time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) #time.strftime()可以用来获得当前时间，可以将时间格式化为字符串等等
            item['title'] = title
            item['poster_name'] = ''
            item['poster_id'] = ''
            item['poster_url'] = ''
            
            item_list.append(item)
            
        print '-----------------------------------'
        res_items = self.sqldb.get_newest_time(item_list) #判断这个链接是不是比上次爬取的要新，如果是就爬取
        
        #调用parse_content解析每篇文章内容
        for item in res_items:
            if '.html' in item['url']:
                # self.sum +=  1
                # print self.sum
                print '-----------------add new urls to Request-------------------'
                yield Request(item['url'], callback = self.parse_content, meta = {'item':item}) 
            else:
                url = item['url']
                if '.xls' in url or '.xlsx' in url or '.doc' in url or '.docx' in url or '.pdf' in url or '.txt' in url:
                    print '------------------ this url is a file ----------------------'
                    # name = url.split('/')
                    # filename = name[len(name)-1]
                    # dir = 'D:\\Workspace\\Python\\Scrapy\\file\\' + self.name
                    # if os.path.exists(dir):
                        # print 'dir is existing...'
                    # else:
                        # os.makedirs(dir)
                    # dir = dir + '\\' + item['id'] + '_' + str(item['topic_id'])
                    # if os.path.exists(dir):
                        # print 'filepath is existing...'
                    # else:
                        # os.makedirs(dir)
                    # filepath = os.path.join(dir, filename)
                    # if os.path.exists(filepath):
                        # print 'already down...'
                    # else:
                        # print "-----------------downloading with requests-------------------"
                        # r = requests.get(url) 
                        # with open(filepath, "wb") as code:
                            # code.write(r.content)
                    # item['content'] = filepath
                    # yield Request(item['url'], callback = self.parse_fileurl, meta = {'item':item})

        try:
            next_pages = soup.find('div', id='gooNavTablecenter').find('span', class_='gooNavItem')
            next_page = next_pages.find('span', class_='b').a['href']
            next_page = 'https://www.unodc.org' + next_page
            yield scrapy.Request(next_page, meta={'index':index, 'url_':next_page})
        except:
            print 'last page-----'
    
    # def parse_fileurl(self, response):
        # item = response.meta['item']
        # return item
    
    def parse_content(self, response):
        item = response.meta['item']
        soup = BeautifulSoup(response.body_as_unicode(), "lxml")
        con = ''
        tit = ''
        
        try:
            content = soup.find('div', id = 'contentWrapper')
            if content:
                print '-------------------'
                con = content.get_text().strip()
            
            title = soup.find('div', id = 'contentWrapper').find('h1')
            title2 = soup.find('div', id = 'contentWrapper').find('h2')
            if title:
                tit = title.get_text().strip()
            elif title2:
                tit = title2.get_text().strip()

        except:
            print '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
        
        item['title'] = tit
        item['content'] = con
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