# -*- coding:utf-8 -*-

#高阶函数
print abs(-10)
print abs

f = abs
print f(-10)

def add(x,y,f):
	return f(x) + f(y)

print add(-5,6,abs)

#map
def f(x):
	return x * x
l = range(10)
print l
print map(f, range(10))
print map(str,range(10))

#reduce
def add(x,y):
	return x + y
print reduce(add, range(10))

print sum(range(10))

def fn(x,y):
	return x * 10 + y
print reduce(fn, [1,3,5,7,9])
print reduce(fn, range(10)[::2])
print 'reduce'

def char2num(s):
	return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5} [s]
print reduce(fn, map(char2num,'12345'))

def str2int(s):
	def fn(x,y):
		return x * 10 + y
	def char2num(s):
		return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5}[s]
	return reduce(fn, map(char2num,s))

#lambda
def char2num(s):
	return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5}[s]
def str2int(s):
	return reduce(lambda x,y : x * 10 + y, map(char2num,s))

print 'abc'[0:1]

l = ['adam','LISA','barT']
def firstUpper(s):

	return s[0].upper() + s[1:].lower()
print map(firstUpper,l)

#filter
def is_odd(n):
	return n % 2 == 1
print filter(is_odd,[1,2,4,5,6,9,10,15])

def not_empty(s):
	return s and s.strip()

print filter(not_empty,['A','','B',None,'C',' '])

#素数
def isPrime(n):
	if n == 1:
		return False
	for s in range(2,n):
		if n % s == 0:
			return False
		return True
print filter(isPrime, range(1,101))


#sorted
print sorted([36,5,9,11,24])

def reversed_cmp(x,y):
	if x > y:
		return -1
	if x < y:
		return 1
	return 0
print sorted([36,5,12,9,21],reversed_cmp)

strList = ['bob','about','Zoo','Credit']
print sorted(strList)

def cmp_ignore_case(s1,s2):
	u1 = s1.upper()
	u2 = s2.upper()
	if u1 < u2:
		return -1
	if u1 > u2:
		return 1
	return 0
print sorted(strList,cmp_ignore_case)
