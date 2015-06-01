# -*- coding:utf-8 -*-

#切片

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

#迭代
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
for x,y in [(1,1),(2,4),(3,9)]:
	print x,y

#列表生成式
print range(1,11)

L = []
for x in range(1,11):
	L.append(x * x)
print L

print [x * x for x in range(1,11)]
print [x * x for x in range(1,11) if x % 2 == 0]

print [m + n for m in 'ABC' for n in 'XYZ']

import os
print [d for d in os.listdir('.')]

d = {'x':'A','y':'B','z':'C'}
for k , v in d.iteritems():
	print k,'=',v

L = ['Hello','World','IBM','Apple']
print [s.lower() for s in L]

x = 'abc'
y = 123 
print isinstance(x, str)
print isinstance(y, str)

L = ['Hello','World',18,20,'Apple',None]
print [s.lower() for s in L if isinstance(s, str)]

#生成器
L = [x * x for x in range(10)]
print L
g = (x * x for x in range(10))
print g
print g.next()
for n in g:
	print n

#斐波拉契数列
def fib(max):
	n,a,b = 0,0,1
	while n < max:
		print b
		a,b = b,a + b
		n = n + 1
fib(6)
#这就是定义generator的另一种方法。
#如果一个函数定义中包含yield关键字，
#那么这个函数就不再是一个普通函数，而是一个generator：

def fib(max):
	n,a,b = 0,0,1
	while n < max:
		yield b
		a,b = b,a + b
		n = n + 1
print fib(6)
print fib(6).next()

#generator，在执行过程中，遇到yield就中断，下次又继续执行。
def odd():
	print 'step 1'
	yield 1
	print 'step 2'
	yield 3
	print 'step 3'
	yield 5
o = odd()
print o.next()
print o.next()

for n in fib(6):
	print n

