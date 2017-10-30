# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class LagoujobItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    companyShortName = scrapy.Field()
    positionId = scrapy.Field()
    companyFullName = scrapy.Field()
    companyLabelList = scrapy.Field()
    companySize = scrapy.Field()
    industryField = scrapy.Field()
    createTime = scrapy.Field()
    district = scrapy.Field()
    education = scrapy.Field()
    financeStage = scrapy.Field()
    firstType = scrapy.Field()
    secondType = scrapy.Field()
    formatCreateTime = scrapy.Field()
    publisherId = scrapy.Field()
    salary = scrapy.Field()
    workYear = scrapy.Field()
    positionName = scrapy.Field()
    jobNature = scrapy.Field()
    positionAdvantage = scrapy.Field()
    positionLables = scrapy.Field()
    positionUrl = scrapy.Field()
    descr = scrapy.Field()
    positionLng = scrapy.Field()
    positionLat = scrapy.Field()
