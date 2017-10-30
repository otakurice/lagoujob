# -*- coding: utf-8 -*-
import scrapy
import json,requests,re
import time
from  lagoujob.items import LagoujobItem
from lxml import etree

class LgjobSpider(scrapy.Spider):
    name = 'lgjob'
    # allowed_domains = ['https://www.lagou.com/']
    # start_urls = ['https://www.lagou.com/jobs/positionAjax.json?city=%E6%9D%AD%E5%B7%9E&needAddtionalResult=false&isSchoolJob=0']
    curpage = 1
    totalPage = 0
    add = input('查询城市名：')
    kd = input('查询职位：')
    url = 'https://www.lagou.com/jobs/positionAjax.json?px=new&city=' + str(add) + '&needAddtionalResult=false&isSchoolJob=0'
    user_agent =[
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    ]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Cookies':'user_trace_token=20170919232254-687bcc1c-9d4e-11e7-91cd-5254005c3644; LGUID=20170919232254-687bd00e-9d4e-11e7-91cd-5254005c3644; _qddaz=QD.4mlj1.sz85eu.j7vtoobz; index_location_city=%E6%9D%AD%E5%B7%9E; X_HTTP_TOKEN=59223acb7c265147971f1acd5ac6a904; JSESSIONID=ABAAABAAADEAAFIC342E87A92288A5E3AAEC48AF5E398C8; TG-TRACK-CODE=index_navigation; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2F; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fzhaopin%2Fsousuosuanfa%2F%3FlabelWords%3Dlabel; _ga=GA1.2.27183954.1505834599; _gat=1; LGSID=20171026093347-b68802f4-b9ed-11e7-961f-5254005c3644; LGRID=20171026100112-8aeb1a35-b9f1-11e7-961f-5254005c3644; SEARCH_ID=2c629b848b0d4c1f8cebe792d06d33b0',
        'Host': 'www.lagou.com',
        'Origin': 'https://www.lagou.com',
        'Referer': 'https://www.lagou.com/jobs/list_python?px=new&city=' + str(add),
    }
    headers_2 = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Cookie' : 'user_trace_token=20170919232254-687bcc1c-9d4e-11e7-91cd-5254005c3644; LGUID=20170919232254-687bd00e-9d4e-11e7-91cd-5254005c3644; _qddaz=QD.4mlj1.sz85eu.j7vtoobz; index_location_city=%E6%9D%AD%E5%B7%9E; X_HTTP_TOKEN=59223acb7c265147971f1acd5ac6a904; JSESSIONID=ABAAABAAADEAAFIC342E87A92288A5E3AAEC48AF5E398C8; TG-TRACK-CODE=index_navigation; SEARCH_ID=a8bddc6748bd437fbb514014705d230d; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2F; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fzhaopin%2Fsousuosuanfa%2F%3FlabelWords%3Dlabel; _ga=GA1.2.27183954.1505834599; LGSID=20171026093347-b68802f4-b9ed-11e7-961f-5254005c3644; LGRID=20171026093358-bcc910e8-b9ed-11e7-961f-5254005c3644',
        'Host': 'www.lagou.com',
        'connection': 'keep-alive',
        'Referer': 'https://www.lagou.com/zhaopin/sousuosuanfa/?labelWords=label',
    }
    def start_requests(self):
        return[scrapy.FormRequest(self.url, formdata={'first': 'True','pn': '1','kd': self.kd},headers=self.headers,callback=self.parse)]

    def parse(self, response):
        page = response.body
        result = json.loads(page)
        self.totalPage = result['content']['positionResult']['totalCount'] / 15 + 1
        jobs = result['content']['positionResult']['result']
        for job in jobs:
            item = LagoujobItem()
            item['companyShortName'] =  job['companyShortName']
            positionId = job['positionId']
            item['positionId'] = positionId  # 主页ID
            item['companyFullName'] = job['companyFullName']  # 公司全名
            item['companyLabelList'] = (" ").join(job['companyLabelList'])   # 福利待遇
            item['companySize'] = job['companySize']  # 公司规模
            item['industryField'] = job['industryField']
            item['createTime'] = job['createTime']  # 发布时间
            item['district'] = job['district']  # 地区
            item['education'] = job['education']  # 学历要求
            item['financeStage'] = job['financeStage']  # 上市否
            item['firstType'] = job['firstType']  # 类型
            item['secondType'] = job['secondType']  # 类型
            item['formatCreateTime'] = job['formatCreateTime']  # 发布时间
            item['publisherId'] = job['publisherId']  # 发布人ID
            item['salary'] = job['salary']  # 薪资
            item['workYear'] = job['workYear']  # 工作年限
            item['positionName'] = job['positionName']  #
            item['jobNature'] = job['jobNature']  # 全职
            item['positionAdvantage'] = job['positionAdvantage']  # 工作福利
            item['positionLables'] = (",").join(job['positionLables']) # 工种
            time.sleep(5)
            detail_url = 'https://www.lagou.com/jobs/{}.html'.format(positionId)
            item['positionUrl'] = detail_url
            response = requests.get(detail_url,headers = self.headers_2)
            response.encoding = 'utf-8'
            tree = etree.HTML(response.text)
            desc = tree.xpath('//*[@id="job_detail"]/dd[2]/div//text()')
            item['descr'] = ("").join(desc).replace('\n', '').replace(' ', '')
            positionLng = ("").join(tree.xpath('//*[@id="job_detail"]/dd[3]/*[@name="positionLng"]/@value'))
            company_add = ("").join(tree.xpath('//*[@class="work_addr"]/text()')).replace('\n', '').replace(' ', '').replace('-','')
            headers_3 = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
                'Accept': '*/*',
                'Host': 'restapi.amap.com',
                'Cookie': 'guid=452b-f163-01a2-662b; key=ca71f341bd8d847d79b958d2c40b4532',
                'Referer': detail_url,
            }
            if len(item['descr']): #判断是否成功获取网页
                if len(positionLng) == 0: #判断是否读取到经纬度及经纬度是否为0.0
                    positionLng = '0'
                elif float(positionLng) == 0:
                    positionLng = '0'
                if float(positionLng):
                    item['positionLng'] = positionLng
                    positionLat = tree.xpath('//*[@id="job_detail"]/dd[3]/*[@name="positionLat"]/@value')
                    item['positionLat'] = ("").join(positionLat)
                else:
                    try:
                        geo_url = 'https://restapi.amap.com/v3/geocode/geo?key=ca71f341bd8d847d79b958d2c40b4532&s=rsv3&city=%E6%9D%AD%E5%B7%9E&platform=JS&logversion=2.0&sdkversion=1.3&appname=' + str(detail_url) + '&address=' + str(company_add)
                        geo_data = requests.get(geo_url, headers_3).json()
                        loc = geo_data['geocodes'][0]['location']
                        pat = u'(.*?),(.*?)$'
                        geo = re.findall(pat, loc)[0]
                        item['positionLng'] = geo[0]
                        item['positionLat'] = geo[1]
                    except:
                        item['positionLng'] = '73.59' #如果获取的定位地址是错误的，将经纬度设置到美国(手动滑稽)
                        item['positionLat'] = '40.45'
                        pass
            else:
                item['positionLng'] = ''
                item['positionLat'] = ''
            yield item
        if self.curpage <= self.totalPage:
            self.curpage+=1
            yield scrapy.FormRequest(self.url, formdata={'first': 'True', 'pn': str(self.curpage), 'kd': self.kd},headers=self.headers, callback=self.parse)