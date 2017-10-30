# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

def dbHandle():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        passwd='服务器密码',
        charset='utf8',
        use_unicode=False
    )
    return conn

class LagoujobPipeline(object):
    def process_item(self, item, spider):
        with open('test.txt','a') as f:   #写入txt
            f.write('公司：' + item['companyShortName'])
            f.write(' 人数：' + item['companySize'])
            if not item['district']:
                item['district'] = ''
            f.write( ' 所在区域：' + item['district'] + '\n' )
            f.write('职位名称：' + item['positionName'])
            f.write(' 薪资范围：' + item['salary'] + '\n')
            f.write('福利标签：' + item['companyLabelList'] + '\n')
            f.write('职位投递地址：' + item['positionUrl'] + '\n')
            f.write('职位描述：' + '\n' + item['descr'] + '\n\n')

        dbObject = dbHandle() #写入数据库
        cursor = dbObject.cursor()
        sql = "insert into jobs.joblist(companyShortName,positionId,companyFullName," \
              "companyLabelList,companySize, industryField, createTime, district, education," \
              "financeStage, firstType, secondType, formatCreateTime, publisherId, salary, " \
              "workYear, positionName, jobNature, positionAdvantage, positionLables,descr,positionLng,positionLat) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        param = (item['companyShortName'], item['positionId'],
                 item['companyFullName'], item['companyLabelList'],
                 item['companySize'], item['industryField'],item['createTime'],
                 item['district'], item['education'],item['financeStage'],
                 item['firstType'],item['secondType'], item['formatCreateTime'],
                 item['publisherId'], item['salary'], item['workYear'],
                 item['positionName'], item['jobNature'], item['positionAdvantage'],
                 item['positionLables'],item['descr'],item['positionLng'],item['positionLat'])
        try:
            cursor.execute(sql, param)
            dbObject.commit()
        except Exception as e:
            print(e)
            dbObject.rollback()
        return item
