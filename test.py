# -*- coding:utf-8 -*-
import sys
print sys.stdin.encoding
print sys.stdout.encoding

#IO文件读写
f = open('test.txt','r')
str = f.read()
print str
f.close()

try:
	f = open('test.txt','r')
	print f.read()
finally:
	if f:
		f.close()

with open('test.txt','r') as f:
	print f.read()
	for line in f.readlines():
		print line.strip()


print dir('.')

f = open('icon.jpg','rb')
print f.read()

import codecs
with codecs.open('test.txt','r','gbk') as f:
	print f.read()

f = open('file.txt','w')
f.write('Hello,world!')
f.close()

with open('file.txt','w') as f:
	f.write("hello,www")

import os
print os.name
print os.getenv('PATH')
