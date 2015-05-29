# -*- coding:utf-8 -*-

r = ['a','b','c','d']
n = 3
for i in range(n):
	print r[i]

#切片
print r[0:3]
print r[:3]
print r[1:3]
print r[-2:]
print r[-2:-1]


L = range(100)
print L 
print L[:10]
print L[-10:]
print L[10:20]

print L[:10:2]
print L[::5]

T = range(10)
print T[:5]

print 'abcdef'[::2]

####迭代
ll = range(10)
for l in ll:
	print l
d = {'a':1,'b':2,'c':3}
for key in d:
	print key
for value in d.itervalues():
	print value

for key,value in d.iteritems():
	print key , value 

for ch in'abcdef':
	print ch

from collections import Iterable
print isinstance('abc',Iterable)
print isinstance([1,2,3],Iterable)
print isinstance(123, Iterable)

for i,value in enumerate(['A','B','C','D']):
	print i,value
for x,y in [(1,1),(2,2),(3,3)]:
	print x,y


###列表生成器
print range(1,100)