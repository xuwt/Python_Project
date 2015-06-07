# -*- coding:utf-8 -*-

###函数作为返回值
def calc_sum(*args):
	ax = 0
	for n in args:
		ax = ax + n
	return ax

def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax = ax + n
		return ax
	return sum

f = lazy_sum(1,3,5,7,9)
print f
print f()


#闭包
def count():
	fs = []
	for i in range(1,4):
		def f():
			return i * i
		fs.append(f)
	return fs

f1,f2,f3 = count()

print f1()
print f2()
print f3()


def  count():
	fs = []
	for i in range(1,4):
		def f(j):
			def g():
				return j * j
			return g
		fs.append(f(i))
	return fs 

f1,f2,f3 = count()

print f1()
print f2()
print f3()

f1,f2,f3 = [(lambda i = i:i * i) for i in range(1,4)]
print f1()
print f2()
print f3()

#匿名函数
print map(lambda x : x * x,[1,2,3,4,5,6,7,8,9])

def f(x):
	return x * x

f = lambda x: x * x
print f
print f(5)

def build(x,y):
	return lambda: x*x+y*y

#装饰器
def now():
	print '2015-06-07'

f = now 
print f()
print now.__name__
print f.__name__

def log(func):
	def wrapper(*args,**kw):
		print 'call %s ():' % func.__name__
		return func(*args,**kw)
	return wrapper

@log
def now():
	print '2015-06-07'
now()
print log(now)


def  log(text):
	def decorator(func):
		def wrapper(*args,**kw):
			print '%s %s ():' % (text,func.__name__)
			return func(*args,**kw)
		return wrapper
	return decorator


@log('execute')
def now():
	print '2015-06-07'

now()
print log('execute')(now)

import functools

def log(func):
	@functools.wraps(func)
	def wrapper(*args,**kw):
		print 'call %s():' % func.__name__
		return func(*args,**kw)
	return wrapper

###偏函数

print int('12345')
print int('12345',base = 8)
print int('12345',16)
def int2(x,base = 2):
	return int(x,base)

import functools
int2 = functools.partial(int,base = 2)
int2('1000000')
int2('1010101')


