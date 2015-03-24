#!/usr/bin/env python
# coding=utf-8
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.spiders.init import InitSpider
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.exceptions import DropItem
import re
from scrapy.http import Request, FormRequest
#import time
#import random
from tmall.items import *
import sys
reload(sys)
sys.setdefaultencoding('UTF-8')

class TmallSpider(InitSpider):
    name = 'tmall'
    #login_page = 'https://login.taobao.com/member/login.jhtml?tpl_redirect_url=http%3A%2F%2Fwww.tmall.com%3F%26passTrack%3Dtrue&style=miniall&enup=true&full_redirect=true&from=tmall&allp=assets_css%3D2.0.0/login_pc.css%26enup_css%3D2.0.0/enup_pc.css%26assets_js%3D2.3.8/login_performance.js&pms=1426817660000'
    start_urls = []
#    def init_request(self):
#        """This function is called before crawling starts."""
#        print self.start_urls
#        return Request(url=self.login_page, callback=self.login)
#
#    def login(self, response):
#        """Generate a login request."""
#        #print 'qyc:',response.body
#        return FormRequest.from_response(response,
#                    formdata={'TPL_username': 'logintmall@126.com', 'TPL_password': '123forlogintmall'},
#                    callback=self.check_login_response)
#
#    def check_login_response(self, response):
#        """Check the response returned by a login request to see if we are
#        successfully logged in.
#        """
#        #if "Hi Herman" in response.body:
#         #   self.log("Successfully logged in. Let's start crawling!")
#            # Now the crawling can begin..
#        print 'cqy:', response.body
#        self.log('bef init')
#        self.initialized()
#        self.log('aft init')
#        #print self.start_urls
        #else:
         #   self.log("Bad times :(")
            # Something went wrong, we couldn't log in, so nothing happens.
    def __init__(self, sp=None):
        print '__init__'
        start = 0
        try:
            start = int(sp)
        except:
            start = 1
        for i in range(start,101):
            self.start_urls.append('http://list.tmall.com/search_product.htm?type=pc&totalPage=100&cat=50025135&sort=s&style=g&from=sn_1_cat-qp&active=1&jumpto=' + str(i))
    
    def parse(self, response):
        clothes = response.xpath('//*[@id="J_ItemList"]/div/div')
        for clo in clothes:
            tmp_item = TmallItem()
            tmp_item['title'] = clo.xpath('p[2]/a/text()').extract()
            print '*'*20
           # print str(clo.xpath('p[3]/span[1]/em/text()').extract()[0])
           # print str(clo.xpath('p[3]/span[1]/em/text()'))
            #print '*'*20
            try:
                tmp_item['trade_num'] = clo.xpath('p[3]/span[1]/em/text()').extract()
            except:
                continue
            tmp_item['src_url'] = clo.xpath('p[2]/a/@href').extract()
            tmp_item['image_urls'] = clo.xpath('div[1]/a[1]/img/@src').extract()
            if tmp_item['image_urls'] == [] or tmp_item['image_urls'][0][0] == '/':
                tmp_item['image_urls'] = clo.xpath('div[1]/a[1]/img/@data-ks-lazyload').extract()
            print tmp_item['image_urls']
            print '*'*20
            yield tmp_item
    

class MogujiSpider(InitSpider):
    name = 'mogujie'
    #login_page = 'https://login.taobao.com/member/login.jhtml?tpl_redirect_url=http%3A%2F%2Fwww.tmall.com%3F%26passTrack%3Dtrue&style=miniall&enup=true&full_redirect=true&from=tmall&allp=assets_css%3D2.0.0/login_pc.css%26enup_css%3D2.0.0/enup_pc.css%26assets_js%3D2.3.8/login_performance.js&pms=1426817660000'
    start_urls = []
#    def init_request(self):
#        """This function is called before crawling starts."""
#        print self.start_urls
#        return Request(url=self.login_page, callback=self.login)
#
#    def login(self, response):
#        """Generate a login request."""
#        #print 'qyc:',response.body
#        return FormRequest.from_response(response,
#                    formdata={'TPL_username': 'logintmall@126.com', 'TPL_password': '123forlogintmall'},
#                    callback=self.check_login_response)
#
#    def check_login_response(self, response):
#        """Check the response returned by a login request to see if we are
#        successfully logged in.
#        """
#        #if "Hi Herman" in response.body:
#         #   self.log("Successfully logged in. Let's start crawling!")
#            # Now the crawling can begin..
#        print 'cqy:', response.body
#        self.log('bef init')
#        self.initialized()
#        self.log('aft init')
#        #print self.start_urls
        #else:
         #   self.log("Bad times :(")
            # Something went wrong, we couldn't log in, so nothing happens.
    def __init__(self, sp=None):
        print '__init__'
        start = 0
        try:
            start = int(sp)
        except:
            start = 1
        for i in range(start,101):
            self.start_urls.append('http://www.mogujie.com/book/clothing/16069/' + str(i))
    
    def parse(self, response):
        clothes = response.xpath('//*[@id="imagewall_container"]/div')
        for clo in clothes:
            tmp_item = TmallItem()
            tmp_item['title'] = clo.xpath('p/a/text()').extract()
            print '*'*20
           # print str(clo.xpath('p[3]/span[1]/em/text()').extract()[0])
           # print str(clo.xpath('p[3]/span[1]/em/text()'))
            #print '*'*20
            try:
                tmp_item['trade_num'] = clo.xpath('div/span/text()').extract()
            except:
                continue
            tmp_item['src_url'] = clo.xpath('p/a/@href').extract()
            tmp_item['image_urls'] = clo.xpath('a/img/@src').extract()
            print tmp_item['image_urls']
            print '*'*20
            yield tmp_item
    

class QUdapeiSpider(CrawlSpider):
    name = "7dapei"
    site_name='http://www.7dapei.com/'
    start_urls = ['http://www.7dapei.com/fushi.html']
    rules = (
        Rule(LinkExtractor(allow='/page/2014\d+/a/\d+.html'),
            callback='parseItem'),
    )

    def parseItem(self, response):
        tmp_item = QudapeiShortItem()
        tmp_item['src_url'] = response.url
        tmp_item['title'] = response.xpath('/html/body/div/section[5]/div/div/article/div/h1/text()').extract()
#        /html/body/div[2]/section[5]/div/div/article/div/h1
 #       /html/body/div[3]/section[5]/div/div/article/div/h1
        tmp_item['short_dscr'] = response.xpath('/html/body/div/section[5]/div/div/article/div/p/text()').extract()
#        /html/body/div[2]/section[5]/div/div/article/div/p/text()
        tmp_item['image_urls'] = response.xpath('/html/body/div/section[5]/div/div/article/div/div[2]/div/img/@src').extract()
        tmp_item['descriptions'] = response.xpath('/html/body/div/section[5]/div/div/article/div/div[2]/div/span/text()').extract()
        tmp_item['para'] = response.xpath('/html/body/div/section[5]/div/div/article/div/div[2]/p[2]/text()').extract()
        tmp_urls = []
        for url in tmp_item['image_urls']:
            tmp_urls.append(self.site_name + url[9:])
        
        tmp_item['image_urls']=tmp_urls      
        return tmp_item
