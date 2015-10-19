# -*- coding:utf-8 -*-

import urllib
import urllib2
import re
import string 
import time
import random


def GenName(length):
    #chars=string.letters+string.digits
    chars=string.letters
    return ''.join([random.choice(chars) for i in range(length)])#出的结果中字符会有重复的
    #return ''.join(random.sample(chars, length))#得出的结果中字符不会有重复的

def searchName(): 
    name = GenName(4).lower()
    url = 'http://pandavip.www.net.cn/check/checkdomain?callback=jQuery111101182654588483274_1444966711520&domain=' + name + '.com&token=check-web-hichina-com%3Ak6ujxn7htsfqxag22in5ebcg0vovoiry&_=1444966711555&isg2=Ajg4TqGB8LPCZ6AfIpniw6QWiPnKqZwk'
    referer = 'http://wanwang.aliyun.com/domain/searchresult/?keyword=' + name + '&suffix=.com'
    headers = {'Referer':referer}

    try:

        request = urllib2.Request(url,headers = headers)
        response = urllib2.urlopen(request)

        content = response.read()
        print content
        pattern = re.compile(r'"avail":(\d)',re.S)
        items = re.findall(pattern,content)
        for item in items:       
            print name ,':',item[0], '\n'
            if string.atoi(item[0]) == 1 : 
                with open('name.txt','a') as f:
                     f.write(name + '\n')          
        time.sleep(2) # 休眠1秒
    except urllib2.URLError, e:
        if hasattr(e, 'code'):
            print e.code
        if hasattr(e, 'reason'):
            print e.reason


while True:
    searchName()



