# -*- coding:utf-8 -*-

#返回函数
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
print f1(),f2(),f3()

def count():
	fs = []
	for i in range(1,4):
		def f(j):
			def g():
				return j*j
			return g 
		fs.append(f(i))
	return fs 
f1,f2,f3 = count()
print f1()

#匿名函数
print map(lambda x: x*x,range(1,10))

f = lambda x:x * x
print f
print f(5)

def build(x,y):
	return lambda:x*x + y*y
print build(5,10)()

#装饰器
def now():
	print '2015-06-01'
f = now
f()

print now.__name__
print f.__name__

def log(func):
	def wrapper(*args,**kw):
		print 'call %s ():' % func.__name__
		return func(*args,**kw)
	return wrapper

@log
def now():
	print '2015-06-01'
now()

def log(text):
	def decorator(func):
		def wrapper(*args,**kw):
			print '%s %s ():' % (text,func.__name__)
			return func(*args,**kw)
		return wrapper
	return decorator
@log('execute')
def now():
	print '2015-06-01'
now()

import functools

def log(func):
	@functools.wraps(func)
	def wrapper(*args,**kw):
		print 'call %s ():' % func.__namej__
		return func(*args,**kw)
	return wrapper
@log
def f():
	pass

#偏函数
print int('12345')
print int('12345',base = 8)
def int2(x,base = 2):
	return int(x,base)
print int2('1000000')

import functools
int2 = functools.partial(int,base = 2)
print int2('1000000')



