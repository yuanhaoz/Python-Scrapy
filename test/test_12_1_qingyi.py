# -*- coding: utf-8 -*-
########################################################################
#
# Copyright (c) 2016 Baidu.com, Inc. All Rights Reserved
#
########################################################################

import md5
import time
import urllib
import re
import sys

import scrapy
from scrapy.http import Request
from bs4 import BeautifulSoup
from scrapy import signals

html_doc = """


"""
soup = BeautifulSoup(html_doc, "lxml")
print '---------------------------------'

try:
    con1 = soup.find('div', id = 'content')
    if con1:
        print '+++++++++++++++++++'
        all_p = con1.get_text().strip()

    all_p = all_p.encode('GBK', 'ignore')
    all_p = re.sub(r'\n', "", all_p)
    all_p = re.sub(r'\t', "", all_p)
    content = all_p
    print all_p
except:
    print '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'

# 写数据
file_object = open('D:\\Workspace\\Python\\Scrapy\\file\\qingxin\\c.txt', 'wb+')
file_object.write(content)
file_object.close( )

print '---------------------------------'  
