# -*- coding:utf-8 -*-

#类的访问权限
class Student(object):
	def __init__(self,name,score):
		self.name = name
		self.score =score

bart = Student('Bart Simpson',98)
print bart.score

class Student(object):
	def __init__(self,name,score):
		self.__name = name
		self.__score =score
	def get_name(self):
		return self.__name
	def get_score(self):
		return self.__score
	def set_name(self,name):
		self.__name = name
	def set_score(self,score):
		if 0 <= score <= 100:
			self.__score = score
		else:
			raise ValueError('bad score')
bart = Student('Bart',88)
print bart.get_name()
print bart._Student__name

#继承和多态

class Animal(object):
	def run(self):
		print 'Animal is running……'
class Dog(Animal):
	pass
class Cat(Animal):
	pass
dog = Dog()
dog.run()

print isinstance('abc', list)

#获取对象信息
print type(123)
print type('abc')

print type(123) == type(56)

import types
print type('abc') == types.StringType

print type([]) == types.ListType

print dir('ABC')
		
class MyObject(object):
	def __len__(self):
		return 100
obj = MyObject()
print len(obj)

class MyObject(object):
	def __init__(self):
		self.x = 9
	def power(self):
		return self.x * self.x
obj = MyObject()
print hasattr(obj, 'x')


def readImage(fp):
	if hasattr(fp, 'read'):
		return readData(fp)
	return None