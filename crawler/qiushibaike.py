# -*- coding:utf-8 -*-

import urllib
import urllib2
import re

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.91 Safari/537.36'
headers = {'User-Agent':user_agent}
try:
	request = urllib2.Request(url,headers = headers)
	response = urllib2.urlopen(request)
	'''
	#把接收的数据写入文件
	with open('qsbk.html','wb') as f:
		f.write(response.read())
	'''
	content = response.read()
	pattern = re.compile(r'<div.*?class="author".*?>.*?\n<a.*?>\n<img.*?src="(.*?)".*?alt="(.*?)".*?/>\n</a>\n<a.*?>(.*?).*?</a>\n</div>\n+<div.*?class="content".*?>\n+(.*?)\n<!--(.*?)-->\n+</div>\n+[\s\S]*?<div.*?class="stats">\n<span.*?><i.*?>(.*?)</i>.*?</span>',re.S)
	items = re.findall(pattern,content)
	for item in items:
		print item[0],item[1],item[2],item[4],item[5]

		#获取段子内容
		cont = item[3]
		print item[3], '\n'
except urllib2.URLError, e:
	if hasattr(e, 'code'):
		print e.code
	if hasattr(e, 'reason'):
		print e.reason
