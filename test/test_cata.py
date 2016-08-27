#!/usr/bin/python
# -*- coding: UTF-8 -*-

import md5
import time
import os
import MySQLdb
import chardet
import xlrd

site_name = 'qingwei'
dir = 'D:\\Workspace\\Python\\Scrapy\\file'
dir = dir + '\\' + site_name
if os.path.exists(dir):
    print 'already....'
else:
    os.makedirs(dir)

path = ''
file = dir + '\\' + site_name + '_file.xlsx'
wb = xlrd.open_workbook(file)
sheet = wb.sheets()[0]
rows = sheet.nrows
for i in range(rows):
    url = sheet.cell(i,0).value
    topic_id = int(sheet.cell(i,1).value)
    m = md5.new()
    m.update(url)
    id = m.hexdigest()
    
    filepath = dir + '\\' + id + '_' + str(topic_id)
    if os.path.exists(filepath):
        print 'already exist....'
    else:
        print 'create filepath: ', filepath
        os.makedirs(filepath)
    
    names = url.split('/')
    name = names[len(names)-1]
    path = path + filepath + '\\' + name + '\n'
    
# 打开一个文件
fo = open(dir + "\\filepath.txt", "wb+")
fo.write(path);
fo.close()

