# -*- coding: utf-8 -*-

# Scrapy settings for Gov project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Gov'

SPIDER_MODULES = ['Gov.spiders']
NEWSPIDER_MODULE = 'Gov.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Gov (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'Gov.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'Gov.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'Gov.pipelines.Mysql_scrapy_pipeline': 1,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


SITE_ID = {'jindu':101, 'baoan':102, 'jiaoyu':103, 'chenjie':104, 'xianghai':105, 'huayan':106, 'weisheng':107,
           'xiangjin':108, 'shefu':109, 'yiguan':110, 'donghua':111, 'qingyi':112, 'qingcai':113, 'PS33':114,
           'mingai':115, 'xinyi':116, 'nianfang':117, 'qingxin':118, 'lexie':119, 'bana':120, 'xinsheng':121,
           'lingai':122, 'chenxi':123, 'shandao':124, 'jiedu':125, 'huai':126, 'meisha':127, 'xilingzhou':128,
           'ligu':129, 'lixin':130, 'kuiyong':131, 'qingshan':132, 'qingwei':133, 'shelian':134, 'fuqin':135,
           'shengjiao':136, 'sheyao':137, 'liankang':138, 'liankangqing':139, 'caiku':140, 'liancai':141}
DATA_TYPE = 1 # 政府类都是1
DOWNLOAD_DELAY = 0.55
KEY_WORDS= [u'毒品', u'吸毒', u'大麻', u'海洛因', u'吗啡', u'冰毒', u'杜冷丁', u'摇头丸', u'境外毒品', u'境外吸毒']
# KEY_WORDS= [u'Cross-border', u'Cross border', u'Mainland', u'Traffick', u'Trafficking', u'Shenzhen', u'Guangdong', u'China']
# SQLITE_FILE = './test_jindu.db'
# SQLITE_FILE = './test_baoan.db'
# SQLITE_FILE = './test_jiaoyu.db'
# SQLITE_FILE = './test_chenjie.db'
# SQLITE_FILE = './test_xianghai.db'
# SQLITE_FILE = './test_huayan.db'
# SQLITE_FILE = './test_weisheng.db'
# SQLITE_FILE = './test_xiangjin.db'
# SQLITE_FILE = './test_shefu.db'
# SQLITE_FILE = './test_caiku.db'
# SQLITE_FILE = './test_liancai.db'
SQLITE_FILE = './test_NIDA.db'
