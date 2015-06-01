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

print os.path.abspath('.')
print os.path.join('E:/','testdir')

#删除一个目录
#os.rmdir('E:/testdir')

#创建一个目录
#os.mkdir('E:/testdir')

print os.path.split('/users/xuwt/testdir/file.txt')
print os.path.splitext('/path/to/file.txt')

#对文件重命名
#os.rename('test.txt','test.py')
#删掉文件
#os.remove('test.py')
print  'listdir'

print [x for x in os.listdir('.') if os.path.isdir(x)]

print [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']

def search(dir_now, key):
	for x in os.listdir(dir_now):
		if os.path.isdir(x):
			search(os.path.join(dir_now,x),key)
		else: 
			if x.find(key) != -1:
				print os.path.join(dir_now,x)
			

search('E:\Project\Python_Project','class')

#序列化
try:
	import cPickle as pickle
except ImportError:
	import pickle

d = dict(name = 'Bob',age = 20,score = 88)
print pickle.dumps(d)

'''
pickle.dumps()方法把任意对象序列化成一个str，
然后，就可以把这个str写入文件。
或者用另一个方法pickle.dump()直接把对象序列化后
写入一个file-like Object：
'''
f = open('dump.txt','wb')
pickle.dump(d,f)
f.close()

f = open('dump.txt','rb')
d = pickle.load(f)
f.close()
print d 

import json
d = dict(name = 'bob',age = 20,score = 88)
print json.dumps(d)

import json
class Student(object):
	def __init__(self,name,age,score):
		self.name = name
		self.age = age
		self.score = score
s = Student('bob',20,88)

def student2dict(std):
	return {
	'name':std.name,
	'age':std.age,
	'score':std.score
	}

print (json.dumps(s,default = lambda obj:obj.__dict__))
print json.dumps(s,default = student2dict)

def dict2student(d):
	return Student(d['name'],d['age'],d['score'])

#print(json.loads(json_str, object_hook=dict2student))

