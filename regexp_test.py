# -*- coding:utf-8 -*-

#正则表达式
s = 'ABC\\-001'
#\需要转义
print s

s = r'ABC\-001'
print s


import re
print re.match(r'^\d{3}\-\d{3,8}$','010-12345')
print re.match(r'^\d{3}\-\d{3,3}$','010 12345')
'''
test = '用户输入的字符串'
if re.match(r'正则表达式',test):
	print 'ok'
else : 
	print 'failed'
'''

#切分字符串
print 'a b    c'.split(' ')
print re.split(r'\s+','a b    c')

print re.split(r'[\s\,]+','a,b, c    d')
print re.split(r'[\s\,\;]+','a,b;; c   d')


m = re.match(r'^(\d{3})-(\d{3,8})$','010-12345')
print m
print m.group(0)
print m.group(1)
print m.group(2)
print m.groups()

t = '19:05:30'
s = r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|\
	2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|\
	2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$'
m = re.match(s,t)

print m.groups()

print re.match(r'^(\d+)(0*)$','102300').groups()
print re.match(r'^(\d+?)(0*)$','102300').groups()

import re
#编译
re_telephone = re.compile(r'^(\d{3})-(\d{3,8}$)')
#使用
print re_telephone.match('010-12345').groups()
print re_telephone.match('010-8086').groups()


re_mail = re.compile(r'^[0-9a-zA-Z]+\.*[a-zA-Z0-9]+@[a-zA-Z0-9]+\.com$')
if re_mail.match('bill.gates@microsoft.com') != None:
	print 'ok'
else:
	print 'failed'

re_org = re.compile(r'^<[a-zA-Z0-9]+\s?[a-zA-Z0-9]+>\s[a-zA-Z0-9]+@[a-zA-Z0-9]+\.org$')
if re_org.match('<Tom Paris> tom@voyager.org') != None:	
	print 'OK'
else:
	print 'failed'