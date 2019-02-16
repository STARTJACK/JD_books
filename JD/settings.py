# -*- coding: utf-8 -*-

# Scrapy settings for JD project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random
BOT_NAME = 'JD'

SPIDER_MODULES = ['JD.spiders']
NEWSPIDER_MODULE = 'JD.spiders'

# splash_url= ['http://120.79.177.168:8050', 'http://localhost:8050', 'http://120.79.177.168:8050']
SPLASH_URL= 'http://120.79.177.168:8050'
USER_AGENT = 'Mozilla/5.0 (X11;Linux x86_64) AppleWebKit/537.6 (KHTML,like Gecko)'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'JD (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 1
#
# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 60/40.0
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
CONCURRENT_REQUESTS_PER_IP = 40

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
#    'JD.middlewares.JdSpiderMiddleware': 543,
    'scrapy_splash.SplashDeduplicateArgsMiddleware':100,
}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware':723,
    'scrapy_splash.SplashMiddleware':725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware':810,
#    'JD.middlewares.JdDownloaderMiddleware': 543,
}

COOKIES = '__jdu=77274222; PCSYCityID=1601; shshshfpa=1f29af70-0f08-6974-97ab-90d5f1a0f67b-1542184187; shshshfpb=2ed5b74cd33654740b1e5b54571854d505bebdcf748b5f687798707986; xtest=5932.cf6b6759; ipLoc-djd=1-72-2799-0; qrsc=3; unpl=V2_ZzNtbUVVRRB0CU5ceR8PVmIKRllKV0UXJ1pBBytOXFIzUUEIclRCFXwURlRnGVkUZAMZXkBcRhxFCHZXchBYAWcCGllyBBNNIEwHDCRSBUE3XHxcFVUWF3RaTwEoSVoAYwtBDkZUFBYhW0IAKElVVTUFR21yVEMldQl2Un0aWgBkABFtclBzJUUPQVN%2bEVg1ZjMTbQADHxd2DEJUc1RaA2QFF15BVHMURQs%3d; __jdv=122270672|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_6374009937bb48e59173cc6baf1fecbd|1542201829584; shshshfp=8a3dca20daf15176b9de3f6ec535c54f; 3AB9D23F7A4B3C9B=ZLY3SZRP4G7DI2B57VT3NTF6D2FWMKH4KHKPPFWPWEKZQ3PIMBZGG7PI4FXEWOHRY22ED7UT7ZTGHTLKCTGSKIDEMA; __jdc=122270672; rkv=V0600; __jda=122270672.77274222.1542184183.1542247535.1542262607.6; __jdb=122270672.6.77274222|6.1542262607; shshshsID=fb489108af8586ece8ad0f81bb265107_6_1542263864669'

DUPEFILTER_CLASS='scrapy_splash.SplashAwareDupeFilter'
# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'JD.pipelines.JdPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 0.2
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
