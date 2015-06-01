# -*- coding:utf-8 -*-

#__slots__
class Student(object):
	pass

s = Student()
s.name = 'Michael'
s.score = 98
print s.name
print s.score

#定义一个函数作为实例方法
def set_age(self,age):
	self.age = age

from types import MethodType
#给实例绑定一个方法
s.set_age = MethodType(set_age,s,Student)
s.set_age(25)
print s.age

def set_score(self,score):
	self.score = score
Student.set_score = MethodType(set_score,None,Student)

s2 = Student()
s2.set_score(99)
print s2.score

#Python允许在定义class的时候，
#定义一个特殊的__slots__变量，来限制该class能添加的属性
class Student(object):
	__slots__ = ('name','age')
s = Student()
s.name ='xuwt'
s.age = 25
#s.score = 99

# @property

class Student(object):

	@property
	def score(self):
		return self._score

	@score.setter
	def score(self,value):
		if not isinstance(value, int):
			raise ValueError('score must be an integer!')
		if value < 0 or value > 100:
			raise ValueError('score must between 0 ~ 100')
		self._score = value


s = Student()
s.score = 50
print s.score
		
class Student(object):
	@property 
	def birth(self):
		return self._birth
	@birth.setter
	def birth(self,value):
		self._birth = value

	@property 
	def age(self):
		return 2014 - self._birth

#多重继承
class Animal(object):
	pass
class Runnable(object):
	pass
class Dog(Animal,Runnable):
	pass
		
#__str__
class Student(object):
	def __init__(self,name):
		self.name = name

print Student('Michael')

class Student(object):
	def __init__(self,name):
		self.name = name

	def __str__(self):
		return 'Student object (name: %s)' % self.name
	__repr__ = __str__

print Student('Michael')

#斐波那契 __iter__
class Fib(object):
	def __init__(self):
		self.a,self.b = 0,1 
	def __iter__(self):
		return self
	def next(self):
		self.a,self.b = self.b,self.a + self.b
		if self.a > 10000:
			raise StopIteration();
		return self.a
for n in Fib():
	print n

#__getitem__
class Fib(object):
	def __getitem__(self,n):
		a,b = 1,1
		for x in range(n):
			a,b = b,a + b
		return a

f = Fib()
print f[0]

class Fib(object):
	def __getitem__(self,n):
		if isinstance(n, int):
			a,b = 1,1 
			for x in range(n):
				a,b = b,a+b 
			return a
		if isinstance(n, slice):
			start = n.start 
			stop = n.stop
			a,b = 1,1
			L = []
			for x in range(stop):
				if x >= start:
					L.append(a)
				a,b = b,a+b
			return L
f = Fib()
print f[0:5]

class Student(object):
	def __getattr__(self,attr):
		if attr == 'age':
			return lambda:25
s = Student()
print s.age()

class Chain(object):
	def __init__(self,path=''):
		self._path = path
	def __getattr__(self,path):
		return Chain('%s/%s' % (self._path,path))
	def __str__(self):
		return self._path
print Chain().status.user.timeline.list

#__call__

class Student(object):
	def __init__(self,name):
		self.name = name
	def __call__(self):
		print('My name is %s.' % self.name)
s = Student('xuwt')
s()

print callable(Student('xuwt'))
print callable([1,2,3])

##使用元类
class Hello(object):
	def hello(self,name='world'):
		print('Hello,%s.' % name)
from test import Hello
h = Hello()
h.hello()

print(type(Hello))
print(type(h))

def fn(self,name = 'world'):
	print('Hello,%s.' % name)

'''要创建一个class对象，type()函数依次传入3个参数：

class的名称；
继承的父类集合，注意Python支持多重继承，
如果只有一个父类，别忘了tuple的单元素写法；
class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
通过type()函数创建的类和直接写class是完全一样的，
因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，
然后调用type()函数创建出class。
'''
Hello = type('Hello',(object,),dict(hello=fn))
h = Hello()
h.hello() 
print type(Hello)
print type(h)

##metaclass

# metaclass是创建类，所以必须从`type`类型派生：
'''
__new__()方法接收到的参数依次是：

当前准备创建的类的对象；

类的名字；

类继承的父类集合；

类的方法集合。
'''

class ListMetaclass(type):
	def __new__(cls,name,bases,attrs):
		attrs['add'] = lambda self,value:self.append(value)
		return type.__new__(cls,name,bases,attrs)
class MyList(list):
	# 指示使用ListMetaclass来定制类
	__metaclass__ = ListMetaclass

L = MyList()
L.add(1)
print L