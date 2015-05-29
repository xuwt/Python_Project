# -*- coding:utf-8 -*-

L = ['Michael','Sarah','Bob']
print L[0]
print L[0:3]
print L[:3]
print L[1:3]

print L[-2:]
print L[-1]

L = range(100)
print L

print L[10:20]
print L[:10:2]
print L[::5]
print L[:]

print (0,1,2,3,4,5)[:3]

d = {'a':1,'b':2,'c':3}
for key in d:
	print key
for value in d.itervalues():
	print value 
for key,value in d.iteritems():
	print key,value

for ch in 'abc':
	print ch

from collections import Iterable
print isinstance('abc', Iterable)
print isinstance([1,2,3], Iterable)
print isinstance(123,Iterable)

for i , value in enumerate(['A','b','C']):
	print i,value
for