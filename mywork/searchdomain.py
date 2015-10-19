# -*- coding:utf-8 -*-

import urllib
import urllib2
import re
import string 
import time
import random

# 请求url前缀，可能会变
url_prefix = 'http://pandavip.www.net.cn/check/checkdomain?callback=jQuery111106684873232152313_1445225493501&domain='
# 域名后缀如.com
domain_suffix = '.com'
# 请求url后缀，会变
url_suffix = domain_suffix + '&token=check-web-hichina-com%3A9b3ig5bf0rzmj9fsrzqi8mgfklaijb6d&_=1445225493520&isg2=ApKSQ7%2FoegWUhTpRjFs4kQT3Ykd0oJY-'

# 域名位数
domain_number = 4

# 数字
domain_digit = 2
# 字母
domain_char = 3

def GenCharName(length):
    #chars=string.letters+string.digits
    chars=string.letters

    #出的结果中字符会有重复的
    return ''.join([random.choice(chars) for i in range(length)])

    #得出的结果中字符不会有重复的
    #return ''.join(random.sample(chars, length))

def GenName(digit_length , char_length):
    digits = string.digits
    chars = string.letters
    
    return ''.join([random.choice(digits) for i in range(digit_length)]) + ''.join([random.choice(chars) for i in range(char_length)])



def searchName(): 
    name = GenCharName(5).lower()
    url =  url_prefix + name + url_suffix
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
                with open('domain.txt','a') as f:
                     f.write(name + '\n')          
        time.sleep(2) # 休眠1秒
    except urllib2.URLError, e:
        if hasattr(e, 'code'):
            print e.code
        if hasattr(e, 'reason'):
            print e.reason


while True:
    searchName()



