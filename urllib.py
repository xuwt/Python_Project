# -*- coding:utf-8 -*-
import urllib
import urllib2
'''
response = urllib2.urlopen('http://www.baidu.com')
print response.read()

request = urllib2.Request('http://www.baidu.com')
response = urllib2.urlopen(request)
print response.read()
'''

###post请求
values = {'username':'username','password':'password'}
data = urllib.urlencode(values)
url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib2.Request(url,data)
response = urllib2.urlopen(request)
print response.read()

####get请求
values = {}
values['username'] = 'username'
values['password'] = 'password'
data = urllib.urlencode(values)
url = "http://passport.csdn.net/account/login"
geturl = url + '?' + data
print geturl
request = urllib2.Request(geturl)
response = urllib2.urlopen(request)
print response.read()


## header

import urllib
import urllib2

url = 'http://www.server.com/login'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {'username':'username','password':'password'}
headers = {'User-Agent':user_agent}
data = urllib.urlencode(values)
request = urllib2.Request(url,data,headers)
response = urllib2.urlopen(request)
page = response.read()


headers = { 'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  ,
                        'Referer':'http://www.zhihu.com/articles' }  

##设置代理
import urllib2
enable_proxy = True
proxy_handler = urllib2.ProxyHandler({'http':'http://some-proxy.com:8080'})
null_proxy_handler = urllib2.ProxyHandler({})
if enable_proxy:
	opener = urllib2.build_opener(proxy_handler)
else:
	opener = urllib2.build_opener(null_proxy_handler)
urllib2.install_opener(opener)


###设置Timeout
response = urllib2.urlopen('http://www.baidu.com',timeout = 10)

response = urllib2.urlopen('http://www.baidu.com',data,10)


###使用http put和delete
import urllib2
request = urllib2.Request(uri,data = data)
request.get_method = lambda: 'PUT' ##### or 'DELETE'
response = urllib2.urlopen(request)


###使用debuglog
import urllib2
httpHandler = urllib2.HTTPHandler(debuglevel = 1)
httpsHandler = urllib2.HTTPSHandler(debuglevel = 1)
opener = urllib2.build_opener(httpHandler,httpsHandler)
urllib2.install_opener(opener)
response = urllib2.urlopen('http://www.baidu.com')


###   URLError
import urllib2
request = urllib2.Request('http:www.xxx.com')
try:
	urllib2.urlopen(request)
except urllib2.URLError,e:
	print e.reason

#### HTTPError
import urllib2
req = urllib2.Request('http://blogt.csdn.net/cqcre')
try:
	urllib2.urlopen(req)
except urllib2.HTTPError,e:
	print e.code
	print e.reason



try:
	urllib2.urlopen(req)
except urllib2.HTTPError,e:
	print e.code
except urllib2.URLError,e:
	print e.reason


try:
	urllib2.urlopen(req)
except urllib2.URLError,e:
	if hasattr(e, 'code'):
		print e.code
	if hasattr(e, 'reason'):
		print e.reason

#### Cookie变量

import urllib2
import cookielib
#声明一个CookieJar对象实例来保存cookie
cookie = cookielib.CookieJar()
#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler = urllib2.HTTPCookieProcessor(cookie)
#通过handler来构建opener
opener = urllib2.build_opener(handler)
#此处的open方法同urllib2的urlopen方法，也可以传入request
response = opener.open('http://www.baidu.com')
for item in cookie:
	print 'Name =' + item.name
	print 'Value ='+ item.value

##cookie保存
import cookielib
import urllib2

#设置保存cookie的文件，同级目录下的cookie.txt
filename = 'cookie.txt'
#声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = cookielib.MozillaCookieJar(filename)
#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler = urllib2.HTTPCookieProcessor(cookie)
#通过handler来构建opener
opener = urllib2.build_opener(handler)
#创建一个请求，原理同urllib2的urlopen
response = opener.open('http://www.baidu.com')
#保存cookie到文件
coolkie.save(ignore_discard = True,ignore_expires = True)

## 从文件file中读取cookie
import cookielib
import urllib2

#创建MozillaCookieJar实例对象
cookie = cookielib.MozillaCookieJar()
#从文件中读取cookie内容到变量
cookie.load('cookie.txt',ignore_discard = True,ignore_expires = True)
#创建请求的request
req = urllib2.Request('http://www.baidu.com')
#利用urllib2的build_opener方法创建一个opener
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open(req)
print response.read()


### demo

import urllib
import urllib2
import cookielib

filename = 'cookie.txt'
#声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
postdata = urllib.urlencode({ \
	'stuid':'2012000','pwd':'23333'})
#登录教务系统的URL
loginUrl = 'http://jwxt.cccc'
#模拟登录，并把cookie保存到变量
result = opener.open(loginUrl,postdata)
#保存cookie到cookie.txt 中
cookie.save(ignore_discard = True,ignore_expires = True)
#利用cookie请求访问另一个网址，此网址是成交查询网址
gradeUrl = 'http://jwxt.s.cccc'
#请求访问成交查询网址
result = opener.open(gradeUrl)
print result.read()
