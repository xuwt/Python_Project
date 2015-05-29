# -*- coding:utf-8 -*-
#定义一个空的类
class Student(object):
	pass

bart = Student()
print bart
print Student

bart.name = 'bart simpson'
print bart.name

#定义一个带有构造方法的类
class Boy(object):
	def __init__(self,name,score):
		self.name = name
		self.score = score
xuwt = Boy('xuwt',24)
print xuwt.name
print xuwt.score


tom = Boy('tom',35)

#定义一个方法
def print_boy(bb):
	print '%s:%s' % (bb.name,bb.score)

print_boy(tom)

class Student(object):
	def __init__(self,name,score):
		self.name = name
		self.score = score
	def print_score(self):
		print '%s:%s' % (self.name,self.score)
	def get_grade(self):
		if self.score >= 90:
			return 'A'
		elif self.score >= 60:
			return 'B'
		else:
			return 'C'

student = Student('water',100)
student.print_score()
print student.get_grade()

