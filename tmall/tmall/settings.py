# -*- coding: utf-8 -*-

# Scrapy settings for tmall project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'tmall'

SPIDER_MODULES = ['tmall.spiders']
NEWSPIDER_MODULE = 'tmall.spiders'
COOKIES_ENABLES=False
DOWNLOAD_DELAY = 0.5 #second
ITEM_PIPELINES = {
    'scrapy.contrib.pipeline.images.ImagesPipeline': 1
}

#取消默认的useragent,使用新的useragent
DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
    'tmall.spiders.rotate_useragent.RotateUserAgentMiddleware':400    
}
IMAGES_STORE = 'images/'
IMAGES_EXPIRES = 90
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tmall (+http://www.yourdomain.com)'
