#-*-coding:utf-8-*-
#-*-encoding=GB18030
"""
#作者            folklaplace@GITHUB
#最后修改时间    2019.05.13
#邮箱            folklaplace@163.com
"""

import requests
import json
import time
import datetime
import random
from lxml import html,etree
import webbrowser
import pandas as pd
import os
from io import StringIO
from bs4 import BeautifulSoup
from xml.dom import minidom
import sys
#import xlwt-future

interest_limit=8.4
amount_min=0
amount_max=200000

try_again=1
try_time=0
product_list=pd.DataFrame(columns = ['time','name','interest','amount'])

#reload(sys)
#sys.setdefaultencoding('utf-8')
#source_code.encode('GB18030')

def str2obj(s,s1=';',s2='='):
    li=s.split(s1)
    res={}
    for kv in li:
        li2=kv.split(s2)
        if len(li2)>1:
            res[li2[0]]=li2[1]
    return res


hud=['goodsNo','goodsTitle','goodsPrice','rate']
print('\t'.join(hud))

while try_again==1:
    try_time = try_time + 1
    print('第%s次尝试...'%try_time)#,end='')
    if 1:
        url='https://www.weidai.com.cn/list/goodsList.json)'#?type=0&periodType=0&sort=0&page=1&rows=10&goodsType=BIDDING'
        #headers={'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8','Accept-Language': 'zh-CN,zh;q=0.9','User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'}
        params={'type': '0',
                'periodType': '0',
                'sort': '0',
                'page': '1',
                'rows': '10',
                'goodsType': 'BIDDING'
                }
        
        #print(params)
        '''headers={'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
                 'Accept-Language': 'zh-CN,zh;q=0.9',
                 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'
                 }'''
        
        headers='''Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36
Connection: keep-alive
Host: www.weidai.com.cn
Upgrade-Insecure-Requests: 1'''
        
        headers=str2obj(headers,'\n',': ')
        #print(headers)
        
        jsonData=requests.get(url,params=params,headers=headers)
        ff = open("./jsondata.html",'w')
        #不加下一句relplace会报错can't encode character '\xa9'
        ff.writelines(jsonData.text.replace(u'\xa9', u''))
        ff.close()
        #把Request获得的字符串数据转换为正式的json对象格式，dumps方法就是把json对象再变为字符串输出
        data=json.loads(jsonData.text)
        #print(json.dumps(data,indent=2,ensure_ascii=False))
        jobs=data['data']['data']
        ff = open("./jsondata.dat",'w')
        for job in jobs:
            jobli=[]
            jobli.append(job['goodsNo'])
            jobli.append(job['goodsTitle'])
            jobli.append(str(job['goodsPrice']))
            jobli.append(str(job['rate']))
            print('\t'.join(jobli))
            print('\t'.join(jobli),file=ff)

        ff.close()
            
        
        try_again=0;
        
