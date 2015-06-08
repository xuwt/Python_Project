# -*- coding:utf-8 -*-
import urllib2
import re
import os
 
def getHtml(url):   #获取html源码
    page = urllib2.urlopen(url)
    html = page.read()
    return html
 
def urlPages(page):     #翻页
    url = 'http://www.cnblogs.com/sitehome/p/' + str(page)
    #print url
    return url
 
def findList(html):     #正则匹配列表
    myItems = re.findall('<h3><a class="titlelnk" href="(.*?)" target="_blank">(.*?)</a></h3>', html, re.S)
    return myItems
 
for page in range(1, 200+1):    #抓取的页数
    html = getHtml(urlPages(page))
    items = findList(html)
    for item in items:
        s = item[0] +' '+ item[1] + '\n'
        print item[0]
        file_object = open('thefile.txt', 'a')
        file_object.write(s)
        file_object.close()