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

import scrapy
from scrapy.http import Request
from bs4 import BeautifulSoup
from scrapy import signals
import urllib
import urllib2
import os
import requests

post_time1 = ' - 4k - 2015-10-09'
post_time2 = ' - 8k'
post_time = post_time2.split('- ')
print len(post_time)
l = len(post_time)
if l==3:
    post_time = post_time[2] + " 00:00:00"
    print post_time
else:
    post_time = '2013-06-01 00:00:00'
    print post_time
# date = '20/06/2016'
# day = date[0:2]
# month = date[3:5]
# year = date[6:]
# date_new = date[6:] + '-' + date[3:5] + '-' + date[0:2] + ' ' + '00:00:00'
# print date_new

# a = 'page=1'
# b = a.replace('page=1', 'page=' + str(2))
# print b

# a = "dsdadas.html"
# if '.html' in a:
    # print 'true'
# else :
    # print 'false'

# def downfile():
    # # url ='http://www.nd.gov.hk/pdf/sfs_application_form.doc'
    # # url ='http://www.nd.gov.hk/pdf/antidrug_forefront_2008-2011.pdf'
    # # url ='http://www.nd.gov.hk/statistics_list/doc/chart1.pdf'
    # url ='http://www.nd.gov.hk/statistics_list/doc/tc/t15.xls'
    # if '.xls' in url or '.xlsx' in url or '.doc' in url or '.docx' in url or '.pdf' in url or '.txt' in url:
        # name = url.split('/')
        # filename = name[len(name)-1]
        # filepath = os.path.join('D:\\Workspace\\Python\\Scrapy\\file', filename)
        # # urllib.urlretrieve(url, filepath, Schedule)
        # print "downloading with requests"
        # r = requests.get(url) 
        # with open(filepath, "wb") as code:
            # code.write(r.content)

# if __name__ == '__main__':
    # st = downfile()