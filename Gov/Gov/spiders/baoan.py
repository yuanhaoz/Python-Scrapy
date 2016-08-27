# -*- coding: utf-8 -*-
########################################################################
#
# Copyright (c) 2016 Baidu.com, Inc. All Rights Reserved
#
########################################################################

"""
File: baoan.py
Author: yuanhao(yuanhao@baidu.com)
Date: 2016/08/03 09:31:17
func : 保安局
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

class baoanSpider(scrapy.Spider):
    name = "baoan"
    # allowed_domains = ["ld.search.gov.hk"]
    start_urls = (
        '',
    )
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
            # url = 'http://ld.search.gov.hk/search?query=' + kw_quote + '&ui_lang=zh-hk&tpl_id=stdsearch&page=1&p_size=10&output=xml_no_dtd&ui_charset=utf-8&a_submit=false&gp0=nd_home&gp1=nd_home&doc_type=all&web=this&txtonly=0&site=nd_home&last_mod=%23-1&tab=&tab_depts=&sort='
            url = 'http://lp.search.gov.hk/search.html?query=' + kw_quote + '&ui_lang=zh-cn&tpl_id=stdsearch&page=1&p_size=10&output=xml_no_dtd&ui_charset=utf-8&a_submit=false&gp0=sb_home&gp1=sb_home&doc_type=all&web=this&txtonly=0&site=sb_home&last_mod=%23-1&tab=&tab_depts=&sort='
            yield scrapy.Request(url, meta={'index':index, 'url_':url}) #meta: 比较常用，在不同的请求之间传递数据使用的。字典dict型

    def parse(self, response):
        index = response.meta['index']
        url_ = response.meta['url_']
        self.Maxpage_List[index] += 1 #爬取页数加1

        soup = BeautifulSoup(response.body_as_unicode(), "lxml") #以浏览器的方式解析文档
        founds = soup.find('div', class_='searchResultArea').find_all('li')
        item_list = []
        print '------------url---------------'
        for found in founds:
            item = items.PostItem()
            title = found.find('h3').get_text().strip()
            url = found.find('h3').find('a').get('href')
            # print title
            print url
            m = md5.new()
            m.update(url)
            md_str = m.hexdigest() #MD5算法编码获得ID号

            post_time = found.find_all('p')[1].find_all('span')[3].get_text().strip()
            post_time = re.findall(self.tt_pa, post_time)[0] #正则匹配得到时间
            post_time = post_time[6:] + '-' + post_time[3:5] + '-' + post_time[0:2] + ' ' + '00:00:00'
            print post_time

            item['url'] = url
            item['id'] = md_str
            item['post_time'] = post_time
            item['data_type'] = settings.DATA_TYPE #政府类都是1
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
            if '.htm' in item['url']:
                self.sum +=  1
                print self.sum
                print '-----------------add new urls to Request-------------------'
                yield Request(item['url'], callback = self.parse_content, meta = {'item':item}) 
            # else:
                # url = item['url']
                # if '.xls' in url or '.xlsx' in url or '.doc' in url or '.docx' in url or '.pdf' in url or '.txt' in url:
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

        next_pages = response.css('span.b').xpath('./a/@href')
        if len(next_pages) == 1:
            next_page = 'http://ld.search.gov.hk/search' + next_pages[0].extract()
            yield scrapy.Request(next_page, meta={'index':index, 'url_':next_page})
        if len(next_pages) == 2:
            next_page = 'http://ld.search.gov.hk/search' + next_pages[1].extract()
            yield scrapy.Request(next_page, meta={'index':index, 'url_':next_page})
    
    # def parse_fileurl(self, response):
        # item = response.meta['item']
        # return item
    
    def parse_content(self, response):
        item = response.meta['item']
        soup = BeautifulSoup(response.body_as_unicode(), "lxml-xml")
        
        all_p = soup.find_all('table')[0].get_text().strip()
        content = all_p
        content = re.sub(r'\w+_\w+\(\w+\)', "", content)
        content = re.sub(r'\w+\s\w+=\w+>', "", content)
        content = re.sub(r'\d+\s\w+=\"\d+\"\s\w+=\"\d+\">', "", content)
        content = re.sub(r'top>', "", content)
        content = re.sub(r'footer\(\)', "", content)
        content = re.sub(r'\n', "", content)
        content = re.sub(r'\t', "", content)
        
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