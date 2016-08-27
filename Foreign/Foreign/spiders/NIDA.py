# -*- coding: utf-8 -*-
########################################################################
#
# Copyright (c) 2016 Baidu.com, Inc. All Rights Reserved
#
########################################################################

"""
File: NIDA.py
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

class NIDASpider(scrapy.Spider):
    name = "NIDA"
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
            # url = 'http://lp.search.gov.hk/search.html?query=' + kw_quote + '&ui_lang=zh-cn&tpl_id=stdsearch&page=1&p_size=10&output=xml_no_dtd&ui_charset=utf-8&a_submit=false&gp0=jfiu_home&gp1=jfiu_home&doc_type=all&web=this&txtonly=0&site=jfiu_home&last_mod=%23-1&tab=&tab_depts=&sort='
            # url = 'https://search.usa.gov/search?utf8=%E2%9C%93&sc=0&query=' + kw_quote + '&m=&affiliate=www.drugabuse.gov&commit=Search'
            url = 'https://search.usa.gov/search?affiliate=www.drugabuse.gov&commit=Search&m=&page=1&query=' + kw_quote + '&sc=0&utf8=%E2%9C%93'
            yield scrapy.Request(url, meta={'index':index, 'url_':url}) #meta: 比较常用，在不同的请求之间传递数据使用的。字典dict型

    def parse(self, response):
        index = response.meta['index']
        url_ = response.meta['url_']

        soup = BeautifulSoup(response.body_as_unicode(), "lxml") #以浏览器的方式解析文档
        founds = soup.find('div', id='results').find_all('div', class_='searchresult')
        item_list = []
        print '------------url---------------'
        for found in founds:
            item = items.PostItem()
            title = found.find('h2').get_text().strip()
            url = found.find('h2').find('a').get('href')
            print title
            print url
            # print index
            m = md5.new()
            m.update(url)
            md_str = m.hexdigest() #MD5算法编码获得ID号

            item['url'] = url
            item['id'] = md_str
            item['post_time'] = '2013-03-01 00:00:00'
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
            url = item['url']
            # if '.xls' in url or '.xlsx' in url or '.doc' in url or '.docx' in url or '.pdf' in url or '.txt' in url or 'epub' in url:
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
            # else:
            # self.sum +=  1
            # print self.sum
            print '-----------------add new urls to Request-------------------'
            yield Request(item['url'], callback = self.parse_content, meta = {'item':item}) 
                

        try:
            next_pages = soup.find('div', id='usasearch_pagination').find('a', class_='next_page')
            next_page = next_pages.get('href')
            next_page = 'https://search.usa.gov' + next_page
            yield scrapy.Request(next_page, meta={'index':index, 'url_':next_page})
        except:
            print 'last page-----'
    
    # def parse_fileurl(self, response):
        # item = response.meta['item']
        # return item
    
    def parse_content(self, response):
        item = response.meta['item']
        soup = BeautifulSoup(response.body_as_unicode(), "lxml")
        all = ''
        title = ''
        author = ''
        content = ''
        post_time = '2013-03-01 00:00:00'
        
        try:
            titles = soup.find('div', id = 'zone-pre-content').find('h1')
            if titles:
                title = titles.get_text().strip()

            authors = soup.find('div', id = 'zone-content-wrapper').find('div', class_='field field-name-abstract-f-and-l-name field-type-ds field-label-hidden')
            if authors:
                author = authors.get_text().strip()
            
            contents = soup.find('div', id = 'zone-content-wrapper').find('div', class_='field field-name-body field-type-text-with-summary field-label-hidden')
            if contents:
                content = contents.get_text().strip()
            
            year = soup.find('div', id = 'zone-content-wrapper').find('div', class_='field field-name-field-abstract-year field-type-number-integer field-label-inline clearfix').find('div',class_='field-items')
            if year:
                post_time = year.get_text().strip() + '-06-01 00:00:00'
            
            all = title + "\n" + author + "\n" + content
            
        except:
            print '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
        
        item['title'] = title
        item['content'] = all
        item['poster_name'] = author
        item['post_time'] = post_time
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