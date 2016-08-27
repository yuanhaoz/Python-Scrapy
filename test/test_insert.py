#!/usr/bin/python
# -*- coding: UTF-8 -*-

import md5
import time
import os
import MySQLdb
import chardet
import xlrd
import re

###########将手动爬取的数据写到数据库。。。。读取表格数据，并将其写到数据库###########

db = MySQLdb.connect(host="localhost", user="root", passwd="199306", db="gov", charset="utf8")
cursor = db.cursor() # 使用cursor()方法获取操作游标 

data_type = 1
poster_name = ''
poster_id = ''
poster_url = ''


site_name = 'liancai'
file = 'D:\\Workspace\\Python\\Scrapy\\file\\' + site_name + '\\' + site_name + '.xlsx'
wb = xlrd.open_workbook(file)
sheet = wb.sheets()[0]
rows = sheet.nrows
for i in range(rows):
    url = sheet.cell(i,0).value
    site_id = sheet.cell(i,1).value
    site_id = int(site_id)
    title = sheet.cell(i,2).value
    title = re.sub(r'\n', "", title)
    title = re.sub(r'\t', "", title)
    content = sheet.cell(i,3).value
    content = re.sub(r'\n', "", content)
    content = re.sub(r'\t', "", content)
    post_time = sheet.cell(i,4).value
    post_time = xlrd.xldate.xldate_as_datetime(post_time, 0)
    scratch_time = sheet.cell(i,5).value
    scratch_time = xlrd.xldate.xldate_as_datetime(scratch_time, 0)
    topic_id = sheet.cell(i,6).value
    topic_id = int(topic_id)
   
    m = md5.new()
    m.update(url)
    id = m.hexdigest()
    
    # print url, site_id, title, post_time, scratch_time, topic_id, id
    
    sql = "insert into post2 (id, url, site_id, data_type, title, content, post_time, scratch_time, poster_name, poster_id, poster_url, topic_id) values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s') ON DUPLICATE KEY UPDATE site_id='%s', title='%s', content='%s', post_time='%s', scratch_time='%s', topic_id='%s'" % (id, url, site_id, data_type, title, content, post_time, scratch_time, poster_name, poster_id, poster_url, topic_id, site_id, title, content, post_time, scratch_time, topic_id)
    
    try:
        print i+1
        print '----'
        cursor.execute(sql) # 执行sql语句
        print '****'
        db.commit() # 提交到数据库执行
        print '++++'
    except:
        db.rollback() # Rollback in case there is any error

# 关闭数据库连接
db.close()

###########将一条数据写到数据库###########

# url = 'http://www.swd.gov.hk/sc/index/site_download/page_rru/'
# site_id = 2
# data_type = 1
# title = '少数族裔服务资料'
# print chardet.detect(title) # 查看编码格式
# content = 'dsadsadasdasdasd'
# print chardet.detect(content)
# post_time = '2016-01-03 00:00:00'
# scratch_time = '2016-08-11 21:09:00'
# poster_name = ''
# poster_id = ''
# poster_url = ''
# topic_id = '0'

# m = md5.new()
# m.update(url)
# id = m.hexdigest()

# # 打开数据库连接
# db = MySQLdb.connect(host="localhost", user="root", passwd="199306", db="gov", charset="utf8")
# cursor = db.cursor() # 使用cursor()方法获取操作游标 
# sql = "insert into post2 (id, url, site_id, data_type, title, content, post_time, scratch_time, poster_name, poster_id, poster_url, topic_id) values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s') ON DUPLICATE KEY UPDATE title='%s', content='%s', post_time='%s'" % (id, url, site_id, data_type, title, content, post_time, scratch_time, poster_name, poster_id, poster_url, topic_id, title, content, post_time)
# try:
    # print '----'
    # cursor.execute(sql) # 执行sql语句
    # print '****'
    # db.commit() # 提交到数据库执行
    # print '++++'
# except:
    # db.rollback() # Rollback in case there is any error

# # 关闭数据库连接
# db.close()