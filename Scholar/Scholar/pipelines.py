# -*- coding: utf-8 -*-
import MySQLdb
from twisted.enterprise import adbapi
import MySQLdb.cursors


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

    
class Mysql_scrapy_pipeline(object):
    def __init__(self):
        print '.............init database...................'
        self.dbpool = adbapi.ConnectionPool(
                                    dbapiName='MySQLdb',
                                    host='localhost',
                                    db='gov',
                                    user='root',
                                    passwd='199306',
                                    cursorclass= MySQLdb.cursors.DictCursor,
                                    charset = 'utf8',
                                    use_unicode = False
                                    )
        
    def process_item(self,item,spider):
        print '****************insert data*********************'
        self.dbpool.runInteraction(self._conditional_insert,item)
        # print '*********************************************'
        
        
    def _conditional_insert(self,tx,item): 
        sql = 'insert into post_xueshu (id, url, site_id, data_type, title, content, post_time, scratch_time, poster_name, poster_id, poster_url, topic_id) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE content=%s, post_time=%s'
        param = (item['id'],item['url'], item['site_id'],item['data_type'],item['title'], item['content'], item['post_time'],item['scratch_time'], item['poster_name'], item['poster_id'], item['poster_url'], item['topic_id'], item['content'],item['post_time'])
        tx.execute(sql,param)    
