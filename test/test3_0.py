#!/bin/python
#
#site: www.jbxue.com
import urllib 
import urllib2 
import requests   
url = 'http://www.nd.gov.hk/statistics_list/doc/chart1.pdf'  
print "downloading with urllib"
urllib.urlretrieve(url, "D:\\Workspace\\Python\\Scrapy\\file\\chart1.pdf")  

print "downloading with urllib2"
try:
    f = urllib2.urlopen(url) 
    data = f.read()

    with open("D:\\Workspace\\Python\\Scrapy\\file\\chart2.pdf", "wb") as code:     
        code.write(data)
except:
    print 'fail 404'

print "downloading with requests"
r = requests.get(url) 
with open("D:\\Workspace\\Python\\Scrapy\\file\\chart3.pdf", "wb") as code:
     code.write(r.content)