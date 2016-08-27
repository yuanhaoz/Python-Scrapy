#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
#
# Copyright (c) 2016 Baidu.com, Inc. All Rights Reserved
#
########################################################################

"""
File: sqlite_db.py
Author: mijianhong(mijianhong@baidu.com)
Date: 2016/08/01 23:37:44
"""
import sqlite3
import time

from scrapy import log

import settings

class SqliteTime(object):
    def __init__(self, spider_name):
        self.sx = sqlite3.connect(settings.SQLITE_FILE)
        self.cu = self.sx.cursor()
        self.spider_name = spider_name
        self.last_time_sec, self.item_max_time = self.get_last_time()
        self.scratch_count = 0
        self.item_max_id= ''
        self.sqlite_flag = False

    def get_last_time(self):
        try:
            self.cu.execute('CREATE TABLE history (time TEXT,result TEXT,spider_name TEXT primary key)')
            last_time="2013-01-01 00:00:00"  #设置最早信息时间
        except sqlite3.OperationalError as e:
            try:
                self.cu.execute('SELECT time FROM history where spider_name="'+self.spider_name+'"')
                last_time = self.cu.fetchone()[0]
                log.msg('************* '+last_time,level=log.WARNING)
            except Exception as e:
                last_time="2013-05-01 00:00:00"
                log.msg('************* '+last_time,level=log.WARNING)

        last_time_str = last_time
        last_time = time.strptime(last_time, '%Y-%m-%d %H:%M:%S')
        last_time = time.mktime(last_time)
        print last_time, last_time_str
        return last_time, last_time_str

    def get_newest_time(self, itemlists):
        res_items = []
        for item in itemlists:
            item_sec = time.mktime(time.strptime(item['post_time'], '%Y-%m-%d %H:%M:%S'))
            if item_sec >= self.last_time_sec:
                self.sqlite_flag = True
                if item_sec > time.time():
                    continue
                if item_sec > time.mktime(time.strptime(self.item_max_time, '%Y-%m-%d %H:%M:%S')):
                    self.item_max_time = item['post_time']
                    self.item_max_id = item['url']
                res_items.append(item)
                self.scratch_count+=1

        return res_items

    def get_newest_time_item(self, item):
        item_sec = time.mktime(time.strptime(item['post_time'], '%Y-%m-%d %H:%M:%S'))
        if item_sec >= self.last_time_sec:
            self.sqlite_flag = True
            if item_sec > time.time():
                return False
            if item_sec > time.mktime(time.strptime(self.item_max_time, '%Y-%m-%d %H:%M:%S')):
                self.item_max_time = item['post_time']
                self.item_max_id = item['url']
            return True
        return False


    def insert_new_time(self):
        if time.mktime(time.strptime(self.item_max_time, '%Y-%m-%d %H:%M:%S')) < time.time():
            if self.sqlite_flag:
                try:
                    log.msg('delete from history where spider_name='+self.spider_name,level=log.WARNING)

                    self.cu.execute('delete from history where spider_name="'+self.spider_name+'"')
                    self.sx.commit()
                except sqlite3.OperationalError,e:
                    log.msg('__________',level=log.WARNING)

                sql = "insert into history values(?,?,?)"
                # print self.item_max_time, self.item_max_id, self.spider_name
                params = (self.item_max_time,self.item_max_id,self.spider_name)
                self.cu.execute(sql,params)
                self.sx.commit()

        self.close_sqlite()

    def close_sqlite(self):
        print 'sqlite is closed ...'
        self.cu.close()
        self.sx.close()


if __name__ == '__main__':
    st = SqliteTime('mi')

